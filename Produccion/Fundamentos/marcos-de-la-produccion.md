---
resumen: >-
  Tres marcos cortan la producción en procesos o en niveles: el Process Classification Framework (PCF) de APQC, ISA-95 (IEC 62264), que separa la planificación del negocio de la gestión de las operaciones de planta, y SCOR, de ASCM. Ninguno corta como esta base, así que cada proceso se reparte entre las verticales del tema y sus vecinos.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework, Cross Industry, versión 7.4 (2024), procesos 4.1.1, 4.1.3, 4.1.4, 4.1.8 y 4.3, y 9.1.2.4 y 10.3: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "ISA, ISA-95 Standard (niveles y partes): https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard"
  - "ANSI/ISA-95.00.03-2013, vista previa (introducción, alcance, definiciones y cambios de nombres): https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf"
  - "ISA, comité ISA95: https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa95 (según el resumen)"
  - "Wikipedia, ISA-95: https://en.wikipedia.org/wiki/ISA-95 (secundaria)"
  - "ASCM, SCOR Digital Standard, introducción (© 2020, «SCOR v13 Updates»): https://www.ascm.org/globalassets/ascm_website_assets/docs/intro-and-front-matter-scor-digital-standard.pdf (leída para Cadena de suministro)"
  - "Produccion/.investigacion/fundamentos-y-contraria.md (sección 2) y ejecucion-en-planta.md (sección 6), 2026-11-27"
aliases: [marcos de la producción, PCF 4.3, APQC 4.3, Produce/Assemble/Test product, ISA-95, ANSI/ISA-95, IEC 62264, niveles de ISA-95, modelo Purdue, gestión de operaciones de manufactura, manufacturing operations management, MOM, Job Order, Work Schedule, Job List, Work Master, SCOR Make, CPIM]
creado: 2026-11-27
revisado:
---

# Marcos de la producción

Tres marcos cortan la producción en procesos o en niveles: el Process Classification Framework (PCF) de APQC, ISA-95 (IEC 62264), que separa la planificación del negocio de la gestión de las operaciones de planta, y SCOR, de ASCM. Ninguno corta como esta base, así que cada proceso se reparte entre las verticales del tema y sus vecinos.

Es parte de los [fundamentos de producción](fundamentos-de-produccion.md). Qué es el PCF y qué es SCOR en general, y cómo se reparten sus procesos de planificación y logística, está en [marcos de la cadena de suministro](../../Cadena-de-suministro-y-logistica/Fundamentos/marcos-de-la-cadena-de-suministro.md); acá van solo los procesos de la producción. Los límites con cada vecino están en el [alcance](../ALCANCE.md).

## El PCF de APQC: de 4.1 a 4.3

En la versión 7.4, la producción no es una categoría propia: vive en 4.0 «Manage Supply Chain for Physical Products». El plan está en 4.1 «Plan for and align supply chain resources» y la fabricación en 4.3 «Produce/Assemble/Test product». Los subprocesos van literales; el reparto es de la base.

| Proceso | Subprocesos del PCF 7.4 | Dónde va en la base |
|---|---|---|
| 4.1.1 Develop production and materials strategies | 4.1.1.1 Define manufacturing goals; .2 Define labor and materials policies; .3 Define outsourcing policies; .4 Define capital expense policies; .5 Define capacities; .6 Define production network and supply constraints; .7 Define production process; .8 Define standard operating procedures; .9 Define production workplace layout and infrastructure | Estrategia, sin nota propia. Lo más cercano: [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md) (.5), [subcontratación](../Ejecucion-en-planta/subcontratacion.md) (.3) y [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) (.7) |
| 4.1.3 Create materials plan | 4.1.3.1 Create unconstrained plan; .2 Collaborate with supplier and contract manufacturers; .3 Identify critical materials and supplier capacity; .4 Monitor material specifications; .5 Generate constrained plan; .6 Define production balance and control | [MRP](../Planificacion-de-la-produccion/mrp.md) (.1 y .5, con la [capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md)); [Compras y abastecimiento](../../Compras-y-abastecimiento/compras-y-abastecimiento.md) (.2 y .3); [cambios de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md) (.4). El .6 no tiene un lugar claro |
| 4.1.4 Create and manage master production schedule | 4.1.4.1 Model production network to enable simulation and optimization; .2 Create master production schedule; .3 Maintain master production schedule | [Plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md) |
| 4.1.8 Develop quality standards and procedures | 4.1.8.1 Establish quality targets; .2 Develop standard testing procedures; .3 Communicate quality specifications | [Calidad](../Calidad/calidad.md) y [plan de inspección](../Calidad/plan-de-inspeccion.md) |
| 4.3.1 Schedule production | 4.3.1.1 Model and simulate plant; .2 Generate line level plan; .3 Generate detailed schedule; .4 Schedule production orders and create lots; .5 Plan for preventive maintenance; .6 Request unplanned maintenance; .7 Release production orders and create lots | [Programación de planta](../Ejecucion-en-planta/programacion-de-planta.md) (.1 a .3); [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) (.4 y .7); [mantenimiento preventivo](../../Activos-y-mantenimiento/Estrategia-de-mantenimiento/mantenimiento-preventivo.md) (.5) y [solicitud de trabajo](../../Activos-y-mantenimiento/Orden-de-trabajo/solicitud-de-trabajo.md) (.6), de Activos y mantenimiento |
| 4.3.2 Produce/Assemble product | 4.3.2.1 Manage raw material inventory; .2 Execute detailed line schedule; .3 Report maintenance issues; .4 Rerun defective items; .5 Monitor and optimize production process (.5.1 Automate and control plant; .5.2 Perform advanced process control; .5.3 Perform real-time optimization; .5.4 Manage plant alarms and alerts); .6 Assess production performance | [Consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md), con el stock en [Inventario](../../Inventario-y-depositos/inventario-y-depositos.md) (.1); [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) (.2); [solicitud de trabajo](../../Activos-y-mantenimiento/Orden-de-trabajo/solicitud-de-trabajo.md) (.3); [no conformidad](../Calidad/no-conformidad.md) (.4); [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md) (.6). El .5 es automatización, fuera del perímetro |
| 4.3.3 Perform quality testing | 4.3.3.1 Calibrate test equipment; .2 Perform testing using the standard testing procedure; .3 Manage quality samples; .4 Record test results; .5 Track and analyze non-conformance trends; .6 Perform root cause analysis | [Plan de inspección](../Calidad/plan-de-inspeccion.md) (.1 a .4); [no conformidad](../Calidad/no-conformidad.md) (.5); [acción correctiva](../Calidad/accion-correctiva.md) (.6) |
| 4.3.4 Maintain production records and manage lot traceability | 4.3.4.1 Determine lot numbering system; .2 Determine lot use | [Trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md); el lote como atributo del stock, en [lote y serie](../../Inventario-y-depositos/Existencias/lote-y-serie.md) |

Tres diferencias con el árbol de la base. El PCF no nombra la lista de materiales ni los cambios de ingeniería: una búsqueda de «bill of material» y de «engineering change» en su texto no dio resultados, y el diseño del producto va en 2.0, que no se revisó. El costo del producto es 9.1.2.4 «Perform product costing», dentro de la contabilidad de costos (acá, [Costos de producción](../Costos-de-produccion/costos-de-produccion.md)), y el mantenimiento real es 10.3 «Maintain assets», con 10.3.1 «Plan asset maintenance» (4.3 solo lo pide). Y la capacidad no tiene un proceso de ejecución propio: aparece como estrategia (4.1.1.5) y como plan con restricciones (4.1.3.5).

## ISA-95: cinco niveles y la frontera entre ERP y MES

ISA-95, también ANSI/ISA-95 o IEC 62264, es según ISA «an international set of standards aimed at integrating logistics systems with manufacturing control systems». Ordena la empresa en cinco niveles:

| Nivel | Nombre en isa.org | En esta base |
|---|---|---|
| 0 | Physical production processes | Fuera del perímetro |
| 1 | Sensing and manipulating the production process | Fuera del perímetro (automatización) |
| 2 | Monitoring and supervising control | Fuera del perímetro (automatización) |
| 3 | Manufacturing operations management | Donde va el MES: [Ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md) y [Calidad](../Calidad/calidad.md) |
| 4 | Business planning and logistics | Donde va el ERP: [Planificación de la producción](../Planificacion-de-la-produccion/planificacion-de-la-produccion.md) y [Producto y proceso](../Producto-y-proceso/producto-y-proceso.md) |

La norma empezó por la frontera entre el 3 y el 4. Según el resumen de la página del comité, «The interface initially considered is the interface between levels 3 and 4» del modelo Purdue. La Parte 3 dice que sus actividades «operate between Level 4 logistics and planning functions and Level 2 manual and automated process control functions», y que su meta es «to reduce the risks, costs and errors associated with implementing enterprise systems and manufacturing operations systems in such a way that they inter-operate and easily integrate». Aclara que no pretende «suggest that there is only one way of implementing manufacturing operations». Qué columna de la tabla le toca a cada vertical es lectura de la base.

### Las ocho partes

Según isa.org: 1 «Models and Terminology»; 2 «Objects and Attributes for Enterprise-Control System Integration»; 3 «Activity Models of Manufacturing Operations Management»; 4 «Objects and Attributes for Manufacturing Operations Management Integration»; 5 «Business-to-Manufacturing Transactions»; 6 «Messaging Service Model»; 7 «Alias Service Model»; 8 «Information Exchange Profiles». Wikipedia llama a la Parte 3 «Models of Manufacturing Operations Management»; vale el nombre de ISA. La edición más antigua que cita Wikipedia es ANSI/ISA-95.00.01-2000; la Parte 3 vigente es de 2013 y la Parte 1 tiene edición 2025, según un buscador.

### El vocabulario de la edición 2013

La Parte 3 de 2013 cambió nombres que se cruzan con los de este tema. La correspondencia con los términos de la base es lectura de la base.

| ISA-95 desde 2013 | Nombre anterior | En esta base |
|---|---|---|
| Work Schedule | Detailed Production Schedule | El programa detallado de la [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md) |
| Job Order | Production Work Order | La [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) |
| Job List | Production Dispatch List | La lista de despacho de la [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md) |
| Work Master (nuevo) | — | «objects that define how work is to be done»: lo más cercano es la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) con su [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) |

La misma vista previa define la programación con capacidad finita como la que asigna trabajo «in such a way that no capacity scheduled exceeds the capacity available». Es la que discute [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md).

### Cuatro categorías de operaciones en el nivel 3

Según el resumen de un buscador, el nivel 3 se divide en cuatro categorías: «production, maintenance, quality ... and inventory operations management». De la norma solo se leyó la definición de la de inventario: «activities within Level 3 of a manufacturing facility which coordinate, direct, manage and track inventory and material movement within manufacturing operations». En la base, cada categoría tiene dueño: producción en [Ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md), mantenimiento en [Activos y mantenimiento](../../Activos-y-mantenimiento/activos-y-mantenimiento.md), calidad en [Calidad](../Calidad/calidad.md) e inventario en [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md), que registra la entrega de material a la orden.

> [!NOTE] Sin fuente todavía: las definiciones de las categorías de producción, mantenimiento y calidad de la Parte 3, los atributos de sus objetos (Parte 2 y Parte 4) y el año de origen de la serie. La norma completa es de pago; solo se leyó su vista previa.

## SCOR y CPIM: lo poco que se sabe

De SCOR, la base leyó solo la introducción de la v13 (2020), que organiza la cadena en «Plan, Source, Make, Deliver, Return and Enable». Make es de este tema; el resto se reparte como dice [marcos de la cadena de suministro](../../Cadena-de-suministro-y-logistica/Fundamentos/marcos-de-la-cadena-de-suministro.md#scor-qué-versión-se-leyó). Una versión de siete procesos lo llama Transform, pero solo consta en una fuente secundaria. De CPIM se sabe que es el programa de certificación en planificación de ASCM (ex APICS); su temario no se leyó. Sí se leyó un extracto de su material de estudio (versión 6.1, edición 2019), del que salen las definiciones del disponible para prometer de [plan maestro de producción](../Planificacion-de-la-produccion/plan-maestro-de-produccion.md#el-disponible-para-prometer-del-plan-maestro).

> [!NOTE] Sin fuente todavía: los subprocesos de Make (o Transform) de SCOR en cualquier versión, sus métricas propias de producción, y los módulos y el temario de CPIM.

## Lo que los marcos le piden a un sistema

Los marcos describen procesos, no datos. Lo que se deduce de ellos es inferencia de la base; lo que piden las escuelas y la evidencia está en [fundamentos de producción](fundamentos-de-produccion.md#lo-que-las-escuelas-le-piden-a-un-sistema).

- Dos versiones del plan de materiales: la que no mira restricciones y la que sí (4.1.3.1 y 4.1.3.5).
- La orden con su lote: el PCF crea el lote al programar y al liberar la orden (4.3.1.4 y 4.3.1.7), y pide una regla de numeración de lotes y el registro de su uso (4.3.4).
- Los resultados de los ensayos con la muestra y el equipo calibrado (4.3.3), guardados de forma que se puedan ver tendencias de no conformidades (4.3.3.5).
- Separar la orden de la receta: ISA-95 distingue la Job Order, lo que se ejecuta, del Work Master, cómo se hace. En un sistema, la orden apunta a la versión de la ruta y la lista que usó, y no las copia sin rastro.
- Un intercambio definido entre el ERP y el MES: qué baja al nivel 3 (la orden y el programa) y qué sube al 4 (lo producido, lo consumido, las horas). Sin MES, el ERP recibe esas mismas declaraciones directamente.
