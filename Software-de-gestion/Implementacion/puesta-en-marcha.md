---
resumen: >-
  La puesta en marcha es el momento en que la empresa deja de operar en el sistema viejo y empieza a operar en el nuevo. Se hace de una vez, por fases o con los dos sistemas en paralelo, pasa por un corte ensayado con un plan para volver atrás y sigue con unas semanas de hipercuidado; no hay estudios sólidos que digan cuál de las tres formas falla menos.
estado: borrador
estabilidad: semi
fuentes:
  - "Guía de implementación de un proveedor grande, estrategia de corte, ms.date 2024-01-30 (leída): https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/prepare-go-live-cutover-strategy"
  - "Material de la metodología de implementación de otro proveedor grande, hipercuidado en la fase de despliegue (según resumen): https://learning.sap.com/courses/discovering-sap-activate-implementation-tools-and-methodology/describing-the-methodology-structure"
  - "Mabert, Soni y Venkataramanan (2003), Enterprise resource planning: managing the implementation process, EJOR 146(2) (citado por un tercero): https://econpapers.repec.org/RePEc:eee:ejores:v:146:y:2003:i:2:p:302-314"
  - "Material docente que resume estudios sobre una vez frente a fases, incluido Bernroider y Leseure (2005) (según resumen): https://www.dea.univr.it:443/documenti/OccorrenzaIns/matdid/matdid965805.pdf"
  - "CIO.com, Supply chain: Hershey's bittersweet lesson, 2002-11-15 (leído): https://www.cio.com/article/2440386/supply-chain-management/supply-chain---hershey-s-bittersweet-lesson.html"
  - "Computerworld, Halloween less spooky for Hershey's this year, 2001-01-05 (leído): https://www.computerworld.com/article/1577198/halloween-less-spooky-for-hershey-s-this-year.html"
  - "Consultancy.uk sobre la cancelación de un proyecto de ERP en una cadena de supermercados europea (según resumen; la prensa remite a una sola fuente primaria): https://www.consultancy.uk/news/18243/lidl-cancels-sap-introduction-having-sunk-500-million-into-it"
  - "Panorama Consulting Solutions, 2017 Report on ERP Systems & Enterprise Software (leído): https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf"
  - "Software-de-gestion/.investigacion/implementacion.md"
aliases: [puesta en marcha, go-live, arranque, corte, cutover, big bang, de una vez, por fases, phased rollout, en paralelo, parallel run, hipercuidado, hypercare, ensayo de corte, mock cutover, vuelta atrás, rollback, go/no-go]
creado: 2026-11-27
revisado:
---

# Puesta en marcha

La puesta en marcha es el momento en que la empresa deja de operar en el sistema viejo y empieza a operar en el nuevo. Se hace de una vez, por fases o con los dos sistemas en paralelo, pasa por un corte ensayado con un plan para volver atrás y sigue con unas semanas de hipercuidado; no hay estudios sólidos que digan cuál de las tres formas falla menos.

Cierra la fase de proyecto de la [implementación](implementacion.md). Necesita que la [migración de datos](migracion-de-datos.md) esté ensayada y conciliada, y abre la estabilización que se cuenta en [después de la puesta en marcha](despues-de-la-puesta-en-marcha.md). En lectura de esta base, en el modelo de Markus y Tanis es el paso de la fase de proyecto a la de estabilización.

## De una vez, por fases o en paralelo

Hay tres formas de pasar de un sistema a otro, y se pueden combinar: por fases de una vez cada una, por ejemplo.

| Forma | Qué se hace | Qué se gana | Qué se arriesga |
|---|---|---|---|
| De una vez (big bang) | Todos los módulos y todos los lugares pasan el mismo día | No hay que mantener puentes entre el sistema viejo y el nuevo | Si algo falla, falla todo a la vez |
| Por fases | Se pasa de a un módulo, una sucursal o una empresa del grupo | Cada fase enseña algo a la siguiente y el daño queda acotado | Durante meses conviven los dos sistemas, con interfaces que después se tiran |
| En paralelo | Los dos sistemas operan a la vez y se comparan los resultados | Hay con qué comparar cada número | Se carga todo dos veces, y la gente deja de cargar bien en uno de los dos |

La tabla es lectura de esta base. Ir por fases es la versión de negocio de [strangler fig](../../Arquitectura/Estilos/strangler-fig.md), el patrón de reemplazar un sistema de a partes sin apagarlo: el argumento de riesgo y valor es el mismo, y el costo también son las piezas de transición. En un software de gestión las partes comparten datos (el pedido de venta mueve stock y deja un asiento), y cada corte por módulo deja una interfaz temporal entre los dos sistemas.

## Lo que se sabe de cuál falla menos

No se encontró un estudio comparativo sólido entre las formas de poner en marcha. Lo que hay son estudios chicos, que esta base conoce solo por resúmenes de terceros:

- Mabert y otros (2003) concluyen que las empresas que pudieron poner en marcha de una vez tuvieron los plazos de implantación más cortos.
- Una entrevista a 30 manufactureras halló que las chicas que pusieron en marcha de una vez anduvieron mejor que las grandes que fueron por fases, con el tamaño como posible confusor.
- Un estudio europeo sobre presupuesto no halló que la forma de puesta en marcha influya en el costo.
- Bernroider y Leseure (2005) encuentran que las pymes eligen más la puesta de una vez y las grandes, por fases.

En lectura de esta base, el tamaño parece pesar mucho en la forma: una empresa chica con un solo lugar no tiene fases naturales, y una grande con varias empresas o países no tiene un día en que todo pueda parar.

## El corte

El corte (cutover) es el paso concreto de un sistema al otro. La guía de implementación de un proveedor grande lo define como el paso «when you switch from your old system to the new one», y avisa: «During cutover, you can't use your old system or your new one». Según esa guía, suele durar menos de 48 horas.

Lo que la guía pide, en pasos:

1. Escribí un plan de corte con cada tarea, su responsable y un suplente, y cómo se verifica que salió.
2. Ensayá el corte entero varias veces («mock cutover») con los mismos datos, herramientas y personas que en el real.
3. Fijá condiciones de entrada, entre ellas una migración «ready and tested», y una revisión de preparación antes del corte, que esa guía declara obligatoria.
4. Decidí seguir o no seguir (go/no-go) con criterios.
5. Tené un plan para volver atrás (rollback).
6. Verificá al final que los datos estén completos y exactos en producción, y pasá el sistema a soporte.

La fecha del corte es también la de los saldos de apertura de la [migración](migracion-de-datos.md). En lectura de esta base, importa tanto como el plan: un corte se pone donde el negocio puede frenar, lejos de la temporada alta, del cierre de mes y de los vencimientos fiscales, y desde ese día el sistema viejo debería quedar con una [fecha de bloqueo](../Columnas-tecnicas/fechas-vigencias-y-cierre.md) que impida registrar en él.

## Hipercuidado

La metodología de un proveedor grande ubica el hipercuidado (hypercare), según un resumen, dentro de la fase de despliegue. No se encontró una definición neutral del término. En lectura de esta base, es el período inmediato a la puesta en marcha en que el equipo del proyecto sigue al lado de los usuarios, con atención reforzada y prioridad para los errores que frenan la operación.

En lectura de esta base, el hipercuidado responde a que la interrupción es lo esperable. En la encuesta de Panorama Consulting de 2017 (342 respuestas, muestra autoseleccionada, consultora que vende gestión de implantaciones), el 56 % tuvo una interrupción operativa material en la puesta en marcha, y el 68 % de esos la sufrió durante cuatro semanas o menos.

## Cuando la puesta en marcha sale mal

Un fabricante de golosinas de Estados Unidos tenía un sistema de 112 millones de dólares que juntaba ERP, CRM y planificación de la cadena, de tres productos distintos. En septiembre de 1999 su director ejecutivo anunció problemas con los pedidos y que no se entregarían unos 100 millones de dólares en golosinas para Halloween; la acción cayó más de 8 % ese día, según CIO.com. Las ganancias del tercer trimestre cayeron 19 %, según Computerworld. Las fuentes leídas no dicen si el sistema se puso en marcha de una vez o por fases. En lectura de esta base, el caso ilustra el costo de una falla en la puesta en marcha cerca de la temporada alta.

Un proyecto se puede cancelar después de años. Una cadena de supermercados europea detuvo en 2018 un proyecto de ERP iniciado en 2011 y volvió a su sistema anterior, según resúmenes de prensa que no se leyeron enteros y que remiten a una sola fuente primaria. El costo de unos 500 millones de euros que se repite no fue confirmado por la empresa ni por el proveedor.

- Cortar en la fecha comprometida y no en la que dan los ensayos: el criterio de go/no-go se vuelve una formalidad.
- No tener vuelta atrás: si el viejo ya no puede recibir operaciones, un error grave en el nuevo frena la facturación.
- Terminar el hipercuidado por calendario: el equipo se va cuando vence el contrato y no cuando bajan los errores.
