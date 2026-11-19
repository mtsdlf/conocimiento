---
tipo: concepto
resumen: >-
  Durable Functions es la extensión de Azure Functions para escribir flujos con estado
  (orquestadores) y objetos con estado (entidades) en código; resuelve seis patrones que las
  funciones sin estado resuelven mal.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, What are Durable Functions?: https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview"
  - "Microsoft Learn, Durable Task documentation (patrones): https://learn.microsoft.com/en-us/azure/durable-task/"
  - "Microsoft Learn, Durable Task storage providers: https://learn.microsoft.com/en-us/azure/durable-task/common/durable-task-storage-providers"
aliases: [Durable Functions, funciones durables, orquestador de Azure Functions]
parte_de: [azure-functions]
requiere: [azure-functions]
relacionado: []
---

# Durable Functions

Durable Functions es la extensión de Azure Functions para escribir flujos con estado
(orquestadores) y objetos con estado (entidades) en código; resuelve seis patrones que las
funciones sin estado resuelven mal.

## Por qué importa

Una función de [Azure Functions](azure-functions.md) no recuerda nada entre ejecuciones. Para encadenar pasos,
esperar a una persona o juntar resultados en paralelo, sin esta extensión hay que coordinar colas,
tablas de estado y timeouts a mano. Durable Functions guarda el progreso del flujo y lo retoma
después de un reinicio o de una espera larga.

## Cómo funciona

Hay tres tipos de función:

- **Orquestador**: describe el flujo en código (qué se llama, en qué orden, qué se espera). Tiene
  que ser determinista, porque la extensión lo vuelve a ejecutar desde su historial para
  reconstruir el estado.
- **Actividad**: hace el trabajo real (llamar a una API, escribir en una base). Puede no ser
  determinista.
- **Entidad**: un objeto chico con estado y operaciones, que procesa sus mensajes de a uno.

El estado y el historial se guardan en un proveedor de almacenamiento. Microsoft recomienda el
Durable Task Scheduler, administrado por Azure; también están Azure Storage, MSSQL y Netherite (con
soporte hasta el 31 de marzo de 2028). El plan Flex Consumption admite solo Azure Storage y el
Durable Task Scheduler.

## Los patrones

| Patrón | Qué resuelve | Ejemplo |
|---|---|---|
| Encadenamiento (function chaining) | Pasos en orden, la salida de uno es la entrada del siguiente | Validar, cobrar y facturar un pedido |
| Fan-out/fan-in | Lanzar muchas tareas en paralelo y esperar a todas para agregar | Procesar mil archivos y sumar los totales |
| API HTTP asíncrona | Una operación larga que el cliente consulta por un endpoint de estado | Generar un reporte que tarda minutos |
| Monitor | Consultar algo a intervalos flexibles hasta que cambia | Esperar a que termine un trabajo externo |
| Interacción humana | Esperar un evento externo con timeout y escalamiento | Aprobación de un gasto, que escala si pasan 72 horas |
| Agregador (entidades) | Juntar eventos de muchas fuentes en un solo objeto con estado | Un contador por dispositivo |

La documentación actual lista cuatro patrones (encadenamiento, fan-out/fan-in, monitor e
interacción humana) y trata la API asíncrona en las funciones HTTP y el agregador en las entidades.

El fan-in y el agregador son los que más cuestan sin la extensión: hay que saber cuándo
terminaron todas las tareas o evitar que dos ejecuciones modifiquen el mismo dato a la vez.

## No confundir con

Logic Apps, que también orquesta flujos con estado pero se diseña en un editor visual con
conectores. Durable Functions se escribe en código (C#, JavaScript, Python, Java, PowerShell).

## Relaciones

- Parte de y requiere: [Azure Functions](azure-functions.md) — es una extensión de Functions y corre en sus planes.
