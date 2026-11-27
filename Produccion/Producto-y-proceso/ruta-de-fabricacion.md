---
resumen: >-
  La ruta de fabricación es la secuencia de operaciones por la que pasa un producto para fabricarse, con el centro de trabajo de cada una y sus tiempos de preparación y de ejecución. Con ella se calcula cuántas horas pide un plan, cuánto tarda una orden y cuánto cuesta la conversión.
estado: borrador
estabilidad: estable
fuentes:
  - "Manual de Routing de un sistema abierto: https://docs.frappe.io/erpnext/user/manual/en/routing"
  - "Manual de Workstation del mismo sistema abierto: https://docs.frappe.io/erpnext/user/manual/en/workstation"
  - "Centros de trabajo de otro sistema abierto (v18.0): https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/manufacturing/advanced_configuration/using_work_centers.html"
  - "Listas de materiales del mismo sistema abierto (v18.0), operaciones: https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/manufacturing/basic_setup/bill_configuration.html"
  - "Guía de plazos de un sistema comercial (cola, preparación, movimiento; resumen del buscador): https://docs.oracle.com/cd/E26228_01/doc.93/e21779/ap_ld_tms.htm"
  - "Mismo sistema comercial, «Understanding Lead Time»: https://docs.oracle.com/en/applications/jd-edwards/supply-chain-manufacturing/9.2/eoapd/understanding-lead-time.html"
  - "Campos de tiempos de operación de otro sistema comercial (resumen del buscador): https://docs.infor.com/ln/2022.x/en-us/lnolh/cpordplanug/cpomlt000130.html"
  - "Presentación de entrenamiento que atribuye a APICS la capacidad nominal, la utilización y la eficiencia (resumen del buscador, baja confianza): https://www.scribd.com/document/578912928/05-BSCM-v4-1-PPT"
  - "ISA-88 en Wikipedia (resumen secundario): https://en.wikipedia.org/wiki/ISA-88"
  - "Control Engineering, «Recipe Management with ISA-S88» (resumen secundario): https://www.controleng.com/recipe-management-with-isa-s88/"
  - "Documentación de un sistema comercial, «Bill of materials (BOM)» y fórmulas (página del 2025-07-10): https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom"
  - "Produccion/.investigacion/producto-y-proceso.md (2026-11-27), sección 2"
aliases: [ruta de fabricación, ruta, hoja de ruta, routing, route, hoja de operaciones, operation sheet, operación, operation, centro de trabajo, work center, workstation, puesto de trabajo, tiempo de preparación, setup time, tiempo de ejecución, run time, tiempo de cola, queue time, tiempo de movimiento, move time, plazo de fabricación, manufacturing lead time, capacidad nominal, rated capacity, eficiencia, efficiency, utilización, utilization, fórmula, receta, recipe, formula, ISA-88]
creado: 2026-11-27
revisado:
---

# Ruta de fabricación

La ruta de fabricación es la secuencia de operaciones por la que pasa un producto para fabricarse, con el centro de trabajo de cada una y sus tiempos de preparación y de ejecución. Con ella se calcula cuántas horas pide un plan, cuánto tarda una orden y cuánto cuesta la conversión.

Es el segundo dato maestro de [Producto y proceso](producto-y-proceso.md). La [lista de materiales](lista-de-materiales.md) dice qué lleva el producto; la ruta, cómo se hace. Las dos se cruzan en el renglón: cada componente puede consumirse en una operación determinada de la ruta.

## Operaciones en secuencia

Una ruta es una lista ordenada de operaciones. Un sistema abierto dice que la ruta «stores all Operations along with the description, hourly rate, operation time, batch size, etc.». Cada operación tiene un centro de trabajo por defecto, un tiempo en minutos y un tamaño de lote, que es la cantidad que se procesa de una vez en esa operación. En ese sistema la secuencia es obligatoria: una operación no se puede completar antes que las anteriores.

Los sistemas no coinciden en dónde vive la ruta. En uno es una plantilla que se aplica a varias listas; en otro, «Each operation is unique, as it is always exclusively linked to one BoM». Es decisión de diseño: el dominio solo exige una secuencia de operaciones con recurso y tiempo.

En papel, la ruta es la hoja de operaciones que acompaña al trabajo: paso, puesto, minutos de preparación y por pieza (criterio de la base). La [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) copia esa ruta y registra, operación por operación, lo que de verdad pasó.

## Los cuatro tiempos de una operación

El tiempo que una orden pasa en un centro de trabajo no es solo el de la máquina. La documentación de un sistema comercial, según lo que devolvió el buscador, separa cuatro tiempos:

| Tiempo | Definición, según la fuente | Depende de la cantidad |
|---|---|---|
| Cola | «The number of hours that a job waits at a work center before setup or work is performed on it» | no, depende de cuánto trabajo haya delante |
| Preparación | «The number of hours required to prepare machinery to run a specific item, regardless of quantity» | no |
| Ejecución | el tiempo de corrida por unidad, que se multiplica por la cantidad | sí |
| Movimiento | «The hours a work order is in transit from the completion of one operation to the beginning of the next» | no |

El mismo sistema comercial suma esas horas («Routing labor, setup, queue, move, and machine run hours») para calcular el plazo de fabricación, que define como «The total number of workdays required to complete a product, from its lowest-level components to the final item, assuming that all purchased items are in-house». Otro sistema comercial agrega un tiempo de espera, sin definirlo. Un sistema abierto guarda en el centro de trabajo la preparación y la limpieza posterior («breakdown or cleanup time required after a work order is finished»).

Los dos sistemas abiertos leídos no tienen campos de cola ni de movimiento: solo preparación y ejecución. Eso significa que el plazo que calculan con la ruta es el tiempo de máquina, no el que tarda la orden en cruzar la planta (inferencia de la base). La consecuencia para la [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md) y para el [MRP](../Planificacion-de-la-produccion/mrp.md), que usa un plazo fijo, se discute en esas notas.

> [!NOTE] Sin fuente todavía: la afirmación clásica de que la cola es la mayor parte del tiempo de ciclo (Hopp y Spearman, *Factory Physics*, no leído) y las definiciones de cola, preparación y movimiento del diccionario de APICS.

## El centro de trabajo: dónde se hace y cuánto puede

El centro de trabajo es el recurso donde se hace una operación: una máquina, un grupo de máquinas iguales, una línea o un puesto con personas. No tiene nota propia en la base porque se define y se usa en la ruta. Un sistema abierto le da estos datos:

| Dato | Qué es, según la documentación |
|---|---|
| Horario | «the hours that work center can be used during the week» |
| Capacidad | «the number of products that can be processed at the work center simultaneously» |
| Eficiencia de tiempo | «a multiplier for how using this work center affects the normal speed of execution of a work order» |
| Meta de OEE | «the target for efficiency at the work center» |
| Costo por hora | «the operating expense of that workstation» |
| Centros alternativos | dónde hacer el trabajo «if this work center is not available» |

Otro sistema abierto suma turnos y una lista de feriados que no cuentan como días de trabajo, y define la capacidad como «the total number of jobs can be executed at the same time». Al programar una orden, revisa la disponibilidad del centro contra esas horas.

La palabra capacidad tiene dos sentidos. En la ficha del centro de esos sistemas es paralelismo: cuántos trabajos a la vez. En la planificación de capacidad son horas por período, que se derivan del calendario, la eficiencia y la utilización. La meta de OEE es un dato del centro, pero la medida y su cálculo están en [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md). El costo por hora alimenta el [costo estándar del producto](../Costos-de-produccion/costo-estandar-del-producto.md).

## Eficiencia y utilización: dos acepciones de eficiencia

La eficiencia de un centro de trabajo se usa con dos sentidos distintos, y conviene no mezclarlos.

| Acepción | Qué mide | Fuente |
|---|---|---|
| Multiplicador de velocidad | cuánto más rápido o más lento trabaja el centro que el tiempo escrito en la ruta | un sistema abierto; según el buscador, en una versión anterior de su documentación, 200 % divide el tiempo a la mitad |
| Horas estándar sobre horas trabajadas | cuántas horas de trabajo «valen» las horas que se trabajaron | una presentación de entrenamiento que dice basarse en APICS; vista por el buscador, de baja confianza |

La segunda acepción viene con dos fórmulas más. La utilización es «hours actually worked over available hours», y la capacidad nominal es «available time × utilization × efficiency». Con 8 horas disponibles, 90 % de utilización y 95 % de eficiencia, la capacidad nominal da 6,84 horas estándar por día (cuenta de la base sobre una fórmula de baja confianza).

Las dos acepciones apuntan en el mismo sentido (más eficiencia, más trabajo por hora), pero se cargan distinto: una es un parámetro que se fija en el centro; la otra, un resultado que se mide después. Un sistema que guarda la primera y un tablero que informa la segunda pueden mostrar «eficiencia» con dos números que no se pueden comparar (inferencia de la base).

Las dos palabras aparecen otra vez en el tema con otros sentidos. La [eficiencia global del equipo](../Ejecucion-en-planta/eficiencia-global-del-equipo.md) (OEE) es otra medida, con sus tres factores, y la utilización de su variante TEEP divide el tiempo planificado por todo el calendario. La variación de eficiencia del [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md#las-variaciones-de-la-orden-y-las-del-período) es la segunda acepción valorizada: horas reales menos horas estándar, por la tarifa.

> [!NOTE] Sin fuente todavía: las definiciones de capacidad nominal, utilización y eficiencia del diccionario de APICS, leídas en el texto. Hasta entonces, la fórmula de la capacidad nominal tiene una sola fuente de baja confianza.

## Fórmula o receta en la fabricación por procesos

En la fabricación por procesos (alimentos, química, bebidas) no se separan la lista y la ruta: se usa la fórmula o receta, que las junta. Según los resúmenes secundarios de la norma ISA-88, una receta contiene «a header, a formula, equipment requirements, a procedure, and other batch processing support information». La fórmula incluye insumos, parámetros de proceso y salidas, no solo proporciones.

La norma distingue tres recetas, según los mismos resúmenes:

| Receta | Qué es |
|---|---|
| General | independiente del equipo y del sitio |
| Maestra | adaptada a las capacidades de un equipo |
| De control | la copia que se usa para un lote, con la identificación del lote y del material |

Un sistema comercial trata la fórmula como «a subtype of BOM that is typically used for process manufacturing», con rendimiento, coproductos y subproductos por versión. Como inferencia de la base, la fórmula se parece a la lista más los parámetros, y el procedimiento a la ruta, pero jerárquico y atado al equipo. Los requisitos de equipo no tienen equivalente en una ruta discreta. La receta de control, ligada a un lote, es lo que después permite la [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md).

> [!NOTE] Sin fuente todavía: el texto de ISA-88 (IEC 61512), de pago; todo lo de la receta viene de resúmenes secundarios.

## Qué guarda una ruta de fabricación

| Registro | Datos |
|---|---|
| Operación | secuencia, descripción, centro de trabajo, tiempo de preparación, tiempo de ejecución por unidad o por lote, tamaño de lote de la operación, a veces cola, espera y movimiento, materiales que consume, salidas que genera, instrucciones |
| Centro de trabajo | calendario, horario y feriados, capacidad, eficiencia, meta de OEE, costo por hora, preparación y limpieza, centros alternativos |

Campos de dos sistemas abiertos y uno comercial. Los estados de cada operación mientras se ejecuta son de la [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md). La versión y la vigencia de la ruta las administra [cambios de ingeniería](cambios-de-ingenieria.md), igual que las de la lista.
