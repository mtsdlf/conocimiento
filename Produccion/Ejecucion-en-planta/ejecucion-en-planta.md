---
resumen: >-
  La ejecución en planta es la parte de la producción que convierte una orden liberada en producto terminado: decide en qué orden pasan los trabajos por las máquinas, entrega el material, registra lo consumido y lo producido, y mide cuánto rindió el equipo. En ISA-95 es el nivel 3, donde trabaja el MES, debajo de la planificación del nivel 4, donde está el ERP.
estado: borrador
estabilidad: estable
fuentes:
  - "ANSI/ISA-95.00.03-2013, vista previa (alcance, actividades del nivel 3, cambios de nombres): https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf"
  - "ISA, comité ISA95, interfaz entre los niveles 3 y 4 (según el resumen): https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa95"
  - "Presentación de una consultora sobre ISA-95 Parte 1, vista solo por el buscador (qué baja y qué sube entre niveles): https://fr.slideshare.net/florentflo2/t061isa9504pdf"
  - "Little, J. D. C. (2011), Little's Law as Viewed on Its 50th Anniversary, Operations Research 59(3):536-549, doi 10.1287/opre.1110.0940, secciones 2.1 y 4.2 (copia de un curso): https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf"
  - "APQC, Process Classification Framework 7.4 (2024), 4.3.1 y 4.3.2: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Documentación de Work Order de un sistema abierto (fechas planificadas y reales): https://docs.frappe.io/erpnext/user/manual/en/work-order"
  - "Produccion/.investigacion/ejecucion-en-planta.md (sección 6) y ejecucion-en-planta-2.md (sección 1), 2026-11-27"
aliases: [ejecución en planta, ejecución de la producción, control de la actividad de planta, shop floor control, production activity control, PAC, sistema de ejecución de manufactura, manufacturing execution system, MES, nivel 3 de ISA-95, ley de Little, Little's law, WIP = TH × CT, producción en proceso, work in process, WIP, tiempo de ciclo, cycle time, throughput, parte de producción]
creado: 2026-11-27
revisado:
---

# Ejecución en planta

La ejecución en planta es la parte de la producción que convierte una orden liberada en producto terminado: decide en qué orden pasan los trabajos por las máquinas, entrega el material, registra lo consumido y lo producido, y mide cuánto rindió el equipo. En ISA-95 es el nivel 3, donde trabaja el MES, debajo de la planificación del nivel 4, donde está el ERP.

Es la tercera de las cinco partes de [Producción](../produccion.md). Recibe de [Planificación de la producción](../Planificacion-de-la-produccion/planificacion-de-la-produccion.md) las órdenes planificadas que propone el [MRP](../Planificacion-de-la-produccion/mrp.md), y de [Producto y proceso](../Producto-y-proceso/producto-y-proceso.md) la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) y la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) que cada orden copia. Le entrega a [Costos de producción](../Costos-de-produccion/costos-de-produccion.md) los consumos y las horas de cada orden, y a [Calidad](../Calidad/calidad.md) lo producido y lo rechazado. En el PCF de APQC corresponde a 4.3.1 «Schedule production» y 4.3.2 «Produce/Assemble product»; el reparto proceso por proceso está en [marcos de la producción](../Fundamentos/marcos-de-la-produccion.md).

## De la orden propuesta al producto terminado

El recorrido de una orden por la planta tiene siete pasos. El orden es el de los sistemas abiertos leídos y del PCF; los nombres de los pasos son de la base.

1. **El MRP propone.** La orden planificada es una sugerencia que el próximo cálculo puede mover. Es de [Planificación de la producción](../Planificacion-de-la-produccion/planificacion-de-la-produccion.md).
2. **Se libera.** Alguien revisa que haya material, capacidad y una versión vigente de la lista y la ruta, y la orden pasa a la planta. Desde acá es una [orden de producción](orden-de-produccion.md).
3. **Se programa.** Cada operación recibe un centro de trabajo, un día y un lugar en la cola: es la [programación de planta](programacion-de-planta.md).
4. **Se entrega el material.** Los componentes salen del depósito hacia la orden, o se descuentan después por consumo automático: ver [consumo y declaración](consumo-y-declaracion.md). Si una operación la hace un tercero, el material viaja a él: ver [subcontratación](subcontratacion.md).
5. **Se ejecutan las operaciones.** Cada una deja tiempos, cantidades y quién la hizo, y de esos datos sale la [eficiencia global del equipo](eficiencia-global-del-equipo.md).
6. **Se declara lo producido.** Lo bueno entra al depósito de terminados; lo rechazado va a [no conformidad](../Calidad/no-conformidad.md).
7. **Se cierra.** La orden se congela y su costo pasa a producto terminado, como cuenta [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md).

Los pasos 4 y 6 son movimientos de stock y se registran en [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md), como filas que no se editan del [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md). Acá se decide qué orden los pide y qué cantidad corresponde; allá, de qué lugar sale y en qué estado queda. En papel, el recorrido es una carpeta por orden con la hoja de ruta, los vales de salida de depósito y el parte de producción de cada turno (criterio de la base).

## La frontera entre el ERP y el MES

ISA-95 separa la planificación del negocio (nivel 4) de la gestión de las operaciones de manufactura (nivel 3). La Parte 3 modela las actividades que «operate between Level 4 logistics and planning functions and Level 2 manual and automated process control functions», y la página del comité dice, según el resumen, que la primera interfaz que se estudió fue la de los niveles 3 y 4. Los niveles, las partes y el vocabulario de 2013 (Job Order, Work Schedule, Job List) están en [marcos de la producción](../Fundamentos/marcos-de-la-produccion.md#isa-95-cinco-niveles-y-la-frontera-entre-erp-y-mes); esta vertical es el nivel 3 del lado de producción.

Lo que cruza la frontera, como lo reparte la base:

| Sentido | Qué viaja | En esta base |
|---|---|---|
| Del 4 al 3 | la orden con su cantidad y fecha | [orden de producción](orden-de-produccion.md) |
| Del 4 al 3 | cómo se fabrica: la versión de la lista y la ruta | [lista de materiales](../Producto-y-proceso/lista-de-materiales.md), [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) |
| Dentro del 3 | el programa detallado y la lista de despacho de cada centro | [programación de planta](programacion-de-planta.md) |
| Del 3 al 4 | lo producido, lo rechazado y lo consumido, con sus lotes | [consumo y declaración](consumo-y-declaracion.md) |
| Del 3 al 4 | las horas por operación y las paradas | [orden de producción](orden-de-produccion.md), [eficiencia global del equipo](eficiencia-global-del-equipo.md) |

La división «el programa baja, el desempeño sube» aparece en una presentación de consultora sobre la Parte 1, vista solo por el buscador. Una patente que cita la norma, también vista solo por el buscador, pone en el nivel 3 «Dispatching Production, Detailed Production Scheduling, Reliability Assurance» y en el 4 «Plant Production Scheduling and Operational Management». Las dos son fuentes débiles; la tabla es lectura de la base.

> [!NOTE] Sin fuente todavía: el contenido de los objetos que se intercambian (programa de producción y desempeño de producción), que está en las Partes 2 y 4 de ISA-95, de pago, y el formato de mensajes que se les asocia.

Sin MES, el ERP recibe esas declaraciones directamente: un sistema abierto guarda en la orden las fechas planificadas y las reales («Actual Start Time, and Actual End Time»). La frontera de ISA-95 es entre funciones, no entre productos de software (inferencia de la base).

## La ley de Little ordena la planta

La idea que más explica una planta es una identidad: la producción en proceso es igual al ritmo de salida por el tiempo que pasa cada trabajo adentro. Little la demostró en 1961 para colas como L = λW. En su revisión de 2011 cuenta que en gestión de operaciones, siguiendo a Hopp y Spearman, se escribe «T H = WIP/CT»: throughput, producción en proceso y tiempo de ciclo. La diferencia es de mirada: se usa la tasa de salida y no la de llegada, porque «This reflects the perspective of a typical operating manager, especially in manufacturing».

Little reproduce las definiciones de Hopp y Spearman: el throughput es «the average output of a production process (machine, workstation, line, plant) per unit time»; la producción en proceso, «the inventory between the start and end points of a product routing», y el tiempo de ciclo, el que va de la liberación al final de la ruta.

Un caso: una planta que termina 40 órdenes por semana y tiene 120 abiertas tarda, en promedio, 3 semanas en terminar cada una (cuenta de la base). Si libera 60 órdenes más sin que el cuello de botella produzca más, el throughput sigue en 40 y el tiempo de ciclo pasa a 4,5 semanas. Little lo dice así: «any increase in output requires either an increase in work-in-process inventory or a reduction in cycle time or both, unless some change is made in the manufacturing process itself».

Tres cosas hacen útil la ley para quien diseña un sistema:

- **Vale sobre lo observado.** La versión que demuestra Little es exacta para un intervalo que empieza y termina vacío, y «holds under nonstationary conditions» y «independent of queue discipline». Es una medida, no un pronóstico: «we are in the measurement business, not the forecasting business».
- **En la fábrica, las llegadas las decide alguien.** Little observa que «The operations manager decides the arrivals based on desired outputs». Liberar órdenes es fijar la producción en proceso, y con ella el tiempo de ciclo.
- **Se mide con dos fechas.** Alcanza con la fecha de liberación y la de terminación de cada orden, y con contar las abiertas. Si las declaraciones llegan tarde, ninguna de las tres cuentas sirve (inferencia de la base).

Las escuelas que limitan la producción en proceso (kanban, CONWIP, tambor-amortiguador-cuerda) se apoyan en esta identidad; están en [programación de planta](programacion-de-planta.md) y en [fundamentos de producción](../Fundamentos/fundamentos-de-produccion.md#cuatro-escuelas-sobre-cómo-liberar-el-trabajo).

## Cómo falla la ejecución

Inferencia de la base, a partir de lo que piden las notas de la vertical:

- **Se libera sin material.** La orden entra a la planta, ocupa un lugar en el programa y espera. Sube la producción en proceso y, por la ley de Little, el tiempo de ciclo.
- **El consumo automático descuenta una lista equivocada.** El stock del sistema se aleja del estante sin que nadie cargue un error.
- **Se declara al final del turno o de la semana.** La planta no sabe qué tiene en proceso, el costo de la orden abierta no se ve y la OEE se calcula con recuerdos.
- **La orden se termina y no se cierra.** El costo queda abierto y las variaciones no aparecen en el mes en que ocurrieron.
- **Se mide la OEE sin decir cómo.** El número sube cambiando el tiempo ideal de ciclo o lo que cuenta como parada planificada, como explica [eficiencia global del equipo](eficiencia-global-del-equipo.md).

## Qué hay en Ejecución en planta

- [Orden de producción](orden-de-produccion.md): el documento, sus estados en dos sistemas abiertos, qué se controla al liberarla y qué se registra al cerrarla; orden discreta, repetitiva y por procesos.
- [Consumo y declaración](consumo-y-declaracion.md): entregar material o consumirlo automáticamente, declarar lo producido, merma, rechazo, subproducto y coproducto, y el lote que se usó.
- [Programación de planta](programacion-de-planta.md): reglas de despacho con un ejemplo, hacia adelante y hacia atrás, carga finita, cuello de botella, tambor-amortiguador-cuerda y kanban.
- [Subcontratación](subcontratacion.md): mandar material a un tercero para una operación, qué se registra y dónde corta con Compras e Inventario.
- [Eficiencia global del equipo](eficiencia-global-del-equipo.md): la OEE, sus tres factores, las seis grandes pérdidas, un ejemplo, el 85 % y cómo se engaña.
