---
tipo: concepto
resumen: >-
  Azure Functions es el cómputo serverless de Azure: código que corre cuando llega un evento (HTTP,
  cola, timer, blob); el plan de hosting (Flex Consumption, Premium, Dedicated) decide si escala a
  cero, si tiene cold start y si entra a una VNet.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Azure Functions hosting options: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale"
  - "Microsoft Learn, Azure Functions Flex Consumption plan hosting: https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan"
  - "Microsoft Learn, Azure Functions overview: https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Functions y gotchas)"
aliases: [Azure Functions, Functions, serverless en Azure, Flex Consumption, Function App]
parte_de: []
requiere: []
relacionado: []
---

# Azure Functions

Azure Functions es el cómputo serverless de Azure: código que corre cuando llega un evento (HTTP,
cola, timer, blob); el plan de hosting (Flex Consumption, Premium, Dedicated) decide si escala a
cero, si tiene cold start y si entra a una VNet.

## Por qué importa

Para trabajo por eventos con picos impredecibles, no hay servidores que dimensionar ni pagar en
reposo. El plan elegido cambia el costo y el comportamiento más que el código: la misma función
puede tardar segundos en arrancar en un plan y responder al instante en otro.

## Cómo funciona

- **Triggers y bindings**: cada función tiene un disparador (HTTP, Service Bus, Event Grid, Blob,
  timer) y declara sus entradas y salidas sin escribir el código de conexión.
- **Lenguajes**: C#, Java, JavaScript, PowerShell y Python; otros (Go, Rust) con custom handlers.
- **Monitoreo**: se integra con Application Insights.

**Planes de hosting**, según Microsoft a octubre de 2026:

| Plan | Escala a cero | Cold start | VNet | Notas |
|---|---|---|---|---|
| **Flex Consumption** | Sí | Se evita con instancias *always ready* | Sí | Recomendado para serverless nuevo; solo Linux y código (sin contenedores), sin slots |
| **Premium** (Elastic Premium) | No | No: instancias precalentadas | Sí | Contenedores Linux propios |
| **Dedicated** (App Service plan) | No | No | Sí | Corre en un plan de App Service ya pagado |
| **Container Apps** | Sí | Al escalar desde cero | Sí | Functions dentro de un entorno de Container Apps |
| **Consumption** | Sí | Sí | No | Legado; en Linux se retira el 30 de septiembre de 2028 |

En Flex Consumption, las funciones HTTP, las de Blob y las de Durable escalan cada grupo junto;
las demás escalan por función.

## Ejemplo

Una función que redimensiona imágenes cada vez que se sube un blob, con picos en horario
comercial y nada de noche. En Flex Consumption escala a cero de noche; con una instancia *always
ready*, la primera imagen del día no espera el arranque. Como el Storage tiene acceso público
apagado, la integración con VNet del plan le permite leerlo por private endpoint.

## No confundir con

[Durable Functions](durable-functions.md): una extensión de Functions para flujos con estado (orquestaciones, esperas
largas). Functions sola no recuerda nada entre ejecuciones.

## Relaciones

- Base de: [Durable Functions](durable-functions.md) — la extensión con estado.
- La compara: [Elección de cómputo en Azure](eleccion-de-computo-en-azure.md) — cuándo Functions y cuándo Container Apps o App
  Service.
