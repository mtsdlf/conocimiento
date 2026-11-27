---
resumen: >-
  El plan maestro de producción (MPS) dice cuánto se va a fabricar de cada artículo final, o de cada módulo, en cada período. Baja el plan agregado a artículos y semanas, es la entrada principal del MRP y es la fuente de lo que ventas puede prometer; por eso se protege con barreras de tiempo que limitan quién puede cambiarlo y cuándo.
estado: borrador
estabilidad: estable
fuentes:
  - "ASCM, CPIM Version 6.1, 2019 Edition, módulo 1, sección F «Master Planning», pp. 1-207 a 1-211 (extracto de muestra; cita el APICS Dictionary, 15.ª ed.): https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "IBM, COPICS, Volume III, cap. 4 «Master Production Schedule Planning» (marzo de 1972), form G320-1976-0: https://mirrorservice.org/sites/www.bitsavers.org/pdf/ibm/370/COPICS/G320-1976-0_COPICS_Volume_3_197203.pdf"
  - "Gershwin, S. B., Material Requirements Planning, diapositivas de MIT 2.853/2.854 (MIT OCW, otoño de 2016), diapositivas 6 y 31: https://ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/4eec617bb52d64f4ea1bed6d9905bc00_MIT2_854F16_MatrialRequire.pdf"
  - "Diapositivas «Material Requirements Planning (MRP) for Dependent Demand Systems», SMU, curso 5362 (2004): https://s2.smu.edu/~barr/5362/2004/04p20MRP.pdf"
  - "Documentación de un sistema comercial, «Time Fence Control»: https://docs.oracle.com/cd/E18727_01/doc.121/e15188/T478564T479135.htm"
  - "Documentación de otro sistema comercial, «Time Fences and the Time Series» (según el resumen): https://docs.oracle.com/en/applications/jd-edwards/supply-chain-manufacturing/9.2/eoarp/time-fences-and-the-time-series.html"
  - "Documentación de un sistema comercial, «Forecast Consumption» (según el resumen): https://docs.oracle.com/cd/E16582_01/doc.91/e15139/forecast_consumption.htm"
  - "ERP Information, «Frozen Zone in Supply Chain (Slushy, Liquid & Time Fences)» (blog comercial, secundaria débil, según el resumen): https://www.erp-information.com/frozen-zone.html"
  - "Open-exam-prep, «6.3 Using and Maintaining the Master Schedule» (guía comercial de estudio, secundaria débil, según el resumen): https://open-exam-prep.com/study-guides/cpim/master-scheduling/using-maintaining-mps"
  - "Wikipedia, Final assembly schedule (secundaria, según el resumen): https://en.wikipedia.org/wiki/Final_assembly_schedule"
  - "Documentación de un sistema abierto, «Master production schedule» (rama 19.0): https://raw.githubusercontent.com/odoo/documentation/19.0/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst"
  - "Produccion/.investigacion/planificacion.md (sección 2) y planificacion-2.md (secciones 1 a 3), 2026-11-27"
aliases: [plan maestro de producción, plan maestro, programa maestro de producción, programa maestro, master production schedule, MPS, master schedule, planificación maestra, master scheduling, programador maestro, master scheduler, barrera de tiempo, time fence, barrera de demanda, demand time fence, DTF, barrera de planificación, planning time fence, PTF, barrera de liberación, release time fence, zona congelada, frozen zone, zona semicongelada, slushy zone, zona abierta, liquid zone, consumo del pronóstico, forecast consumption, disponible para prometer del plan maestro, ATP, available to promise, programa de ensamble final, final assembly schedule, FAS, cubeta, time bucket]
creado: 2026-11-27
revisado:
---

# Plan maestro de producción

El plan maestro de producción (MPS) dice cuánto se va a fabricar de cada artículo final, o de cada módulo, en cada período. Baja el plan agregado a artículos y semanas, es la entrada principal del MRP y es la fuente de lo que ventas puede prometer; por eso se protege con barreras de tiempo que limitan quién puede cambiarlo y cuándo.

Es el segundo escalón de [Planificación de la producción](planificacion-de-la-produccion.md), entre el [plan de ventas y operaciones](../../Cadena-de-suministro-y-logistica/Planificacion/plan-de-ventas-y-operaciones.md), que es de Cadena, y el [MRP](mrp.md). Unas diapositivas de un curso abierto lo definen por su grano: «Individual product production, by period». Las de la Universidad de Tesalia, sobre Hopp y Spearman, lo llaman «a fundamental input of MRP» (traducción de la base). Si entra en los recursos críticos de la planta lo prueba la capacidad gruesa, en [planificación de capacidad](planificacion-de-capacidad.md#capacidad-gruesa-el-plan-maestro-contra-los-recursos-críticos). Qué artículo se planifica acá depende de la estrategia: productos terminados, módulos o pedidos, según [fabricar para stock o contra pedido](fabricar-para-stock-o-contra-pedido.md).

> [!NOTE] Sin fuente todavía: la definición de «master production schedule» del diccionario de ASCM o de Vollmann y otros. Las que se leyeron son de cursos y enciclopedias.

## Una grilla por artículo y período

El plan maestro es una tabla: una fila por artículo, una columna por período. Las diapositivas del MIT dicen que el tiempo se divide en «time buckets — days, weeks, or whatever is convenient». Un sistema abierto deja elegir el rango («Default Time Range»: año, mes, semana o día) y la cantidad de períodos.

La cuenta de cada celda es la misma que se haría en una planilla. Ese sistema abierto la escribe así:

- «Forecasted Stock = Starting Stock - Forecasted Demand - Indirect Demand Forecast + Replenishment»
- «Replenishment = Safety Stock Target - Starting Stock + Forecasted Demand + Indirect Demand Forecast»

La demanda indirecta es la de un artículo que también es componente de otro: «The forecasted demand for the component from existing MOs». El stock de seguridad objetivo es un piso por período. El plan no crea órdenes por sí solo: «The MPS only suggests the amount of product to be replenished», y por producto se elige si la reposición se dispara a mano, sola o nunca.

## Barreras y zonas de tiempo

Cambiar el plan cerca de la fecha cuesta más que cambiarlo lejos, porque ya se compró material y se cargó capacidad. Las barreras de tiempo dividen el horizonte en tramos con reglas distintas para cambiar.

**El origen: congelado y firme.** Un manual de 1972 ya usaba la palabra entre comillas: el plan «can be defined as "frozen" over a given time span beyond the current date - say, for the next month», y en ese tramo «Changes to the schedule cannot normally be made». Distinguía una parte firme y una tentativa. Su ejemplo es un plan de 18 meses en el que los primeros 6 son firmes, con productos «in various stages of commitment and correspondingly difficult to change»; la parte tentativa es «merely a plan for the execution of which money has not yet been expended». El criterio que da vale hoy: «The consequences (cost) of a previous decision constitute the practical limits of changing that decision».

**Las barreras en un sistema.** La documentación de un sistema comercial define tres, cada una como una cantidad de días desde hoy:

| Barrera | Qué hace adentro |
|---|---|
| De demanda | el plan no cuenta el pronóstico; solo la demanda real, los pedidos |
| De planificación | el sistema no adelanta órdenes ni crea órdenes nuevas; sí puede postergar o cancelar las que sobran |
| De liberación | el sistema libera solo las órdenes planificadas a la planta o a compras |

Una orden firme crea una barrera implícita, porque es «frozen in quantity and time (unavailable for rescheduling)». Otro sistema comercial usa otros nombres: una barrera de congelamiento («Freeze Fence») dentro de la cual no crea ni replanifica órdenes, y una de planificación que decide cómo se usa la demanda. Los nombres no coinciden entre sistemas.

**Las zonas y quién autoriza.** El único texto primario leído que nombra una zona es el material de ASCM: un pedido que no entra en lo disponible pide una entrada nueva en el plan y queda sujeto a «master scheduler approval, since it is in the slushy zone and changing the schedule could impact production efficiency». El esquema completo de tres zonas aparece en material de estudio y en un blog comercial, sin fuente primaria:

| Zona | Dónde | Quién autoriza un cambio, según esas fuentes |
|---|---|---|
| Congelada («frozen») | de hoy a la barrera de demanda | la dirección: «Changes discouraged or barred without high-level approval» |
| Semicongelada («slushy») | entre las dos barreras | el programador maestro, negociando con ventas y planta |
| Abierta («liquid») | después de la barrera de planificación | el sistema, que puede regenerar el plan libremente |

> [!NOTE] Sin fuente todavía: la palabra «liquid» no aparece en ninguna fuente primaria leída, y tampoco las definiciones de «demand time fence» y «planning time fence» del diccionario de ASCM. La tabla de zonas sale de una guía de estudio y de un blog comercial; las cifras de semanas que dan para cada zona varían y son ilustrativas.

En lean, ASCM aclara que lo que se tira con señales de demanda «will not use time fences», y que lo que se sigue empujando sí se beneficia de ellas, «because schedule stability in turn promotes production stability».

## El pedido consume el pronóstico

El plan maestro parte de un pronóstico, y los pedidos que llegan no se suman a él: lo consumen. Un sistema comercial lo define así: el consumo del pronóstico supone que los pedidos «reduce, or consume, the forecasted quantities», para que no se traten «as additional demand to the forecast during a planning period»; lo que queda es el pronóstico sin consumir. El mismo sistema procesa los pedidos contra el pronóstico de cada período en orden de llegada, y puede consumir por cliente.

La idea es anterior a la palabra. El manual de 1972 dice que cada pedido «is then allocated against the master production schedule. Provided the demand is covered by the schedule, no further action is necessary». Si no entra, hay que decidir entre cambiar el plan o postergar la entrega, y aumentar el plan solo es posible si hay material y capacidad.

Dentro de la barrera de demanda solo cuentan los pedidos. Afuera, una diapositiva sin autor usa como demanda el máximo entre pronóstico y pedidos; no se encontró la regla en una fuente con nombre.

> [!NOTE] Sin fuente todavía: el consumo hacia adelante y hacia atrás (qué período consume un pedido que cae donde el pronóstico ya se agotó) en una fuente académica.

## El disponible para prometer del plan maestro

El disponible para prometer (ATP) sale del plan maestro. El diccionario de ASCM, citado en el CPIM, lo define como «the uncommitted portion of a company's inventory and planned production maintained in the master schedule to support customer-order promising», que se calcula «for each period in which an MPS receipt is scheduled». El CPIM lo explica así: lo comprometido del plan, en forma de pedidos, deja la parte sin comprometer para quien todavía no pidió.

El método discreto tiene dos fórmulas, literales del CPIM:

- «First Period ATP = Beginning Inventory − Sum of Customer Orders Before Period Containing First Scheduled MPS Receipt»
- «ATP for Periods Containing MPS = Scheduled MPS Receipt − Sum of Customer Orders Before Next Period Containing Scheduled MPS Receipt»

El ejemplo parte de 70 unidades en stock y entradas del plan maestro de 100:

| Semana | Entrada | Pedidos hasta la próxima entrada | ATP | ATP corregido |
|---|---|---|---|---|
| 1 | 70 en stock | 48 | 70 − 48 = 22 | 22 |
| 2 | 100 | 66 | 100 − 66 = 34 | 15 |
| 3 | 100 | 57 + 62 | 100 − 119 = −19 | 0 |
| 5 | 100 | 30 + 0 | 100 − 30 = 70 | 70 |

En la semana 3 los pedidos superan la entrada. La regla es «Reduce the prior ATP by the amount by which the next ATP would be negative»: las 19 que faltan se toman de la semana 2 (34 − 19 = 15) y la 3 queda en 0. Las cuentas verifican. Los pedidos de cada semana vienen de una figura que es imagen; la tabla usa solo las sumas del texto.

Para el vendedor, según el CPIM: puede prometer hasta 22 para despacho inmediato, porque de las 70 en stock 48 ya tienen dueño, y «If the customer can wait a week, the salesperson can promise up to 15 additional units». Cada pedido que entra baja el ATP. Un pedido mayor que lo disponible pide cambiar el plan, y ahí entra la aprobación del programador maestro de la zona semicongelada.

El método acumulado y lo que cuenta como oferta y como compromiso están en [disponible para prometer](../../Inventario-y-depositos/Existencias/disponible-para-prometer.md), de Inventario; la fecha que se le dice al cliente, en [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md), de Relación con clientes.

## El programa de ensamble final

Cuando el producto se arma con opciones, el plan maestro se hace de módulos y el producto terminado aparece en otro programa, el de ensamble final (FAS). Wikipedia lo define, según su resumen, como «a schedule of end items to finish the product for specific customer orders», necesario «when end products do not appear in the MPS».

El manual de 1972 dice cuándo son el mismo programa y cuándo no. Coinciden con productos simples, sin opciones, y con productos complejos fabricados contra pedido. Se separan cuando el plazo de fabricación supera el de entrega: el programa de ensamble final se arma con los pedidos, más tarde, y lo que dejó listo el plan maestro lo limita. Cómo se planifican las opciones está en [fabricar para stock o contra pedido](fabricar-para-stock-o-contra-pedido.md#la-lista-de-planificación-para-las-opciones).

## Qué guarda un plan maestro

- Por artículo, depósito y período: stock inicial, pronóstico, pronóstico consumido y sin consumir, pedidos, demanda indirecta, cantidad planificada, stock proyectado y ATP.
- Por artículo: stock de seguridad objetivo, mínimo a reponer, cómo se dispara la reposición y el plazo acumulado.
- Por artículo o por plan: las barreras de tiempo en días. En los sistemas abiertos leídos no se encontró un campo de barrera; en los comerciales sí.
- Por orden: si es planificada o firme.
- Por plan: el vínculo con el pronóstico y con los pedidos de venta que lo alimentan, y la versión. El nerviosismo se mide comparando versiones (ver [MRP](mrp.md#por-qué-el-mrp-es-nervioso)).
