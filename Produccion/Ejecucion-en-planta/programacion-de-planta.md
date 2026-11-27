---
resumen: >-
  La programación de planta decide en qué orden y en qué momento pasa cada orden de producción por cada centro de trabajo, dentro de la capacidad que hay. Su salida es el programa detallado y la lista de despacho de cada centro, y sus reglas van desde ordenar la cola por fecha de entrega hasta subordinar toda la planta al cuello de botella o dejar que el consumo dispare la producción con kanban.
estado: vigente
estabilidad: semi
fuentes:
  - "Apuntes de un curso de la Universidad de Kentucky, reglas de prioridad (definiciones y fórmulas): https://www.uky.edu/~dsianita/300/schedule.html"
  - "Dartmouth, CO 454, Lecture 3 (SPT y WSPT con demostración): https://cs.dartmouth.edu/~deepc/Courses/S09/Lectures/lecture3.pdf"
  - "Nieberg, Single Machine Scheduling, Universidad de Bonn (EDD): https://www.or.uni-bonn.de/lectures/ss10/scheduling_data/sched10_2.pdf"
  - "Schwiegelshohn (2006), Scheduling Problems and Solutions, material del curso de Pinedo en NYU (EDD con interrupción): https://web-static.stern.nyu.edu/om/faculty/pinedo/scheduling/schwiegelshohn2006.pdf"
  - "Baker y Trietsch, Principles of Sequencing and Scheduling, 2.ª ed., notas de investigación del cap. 2 (Smith 1956, Jackson 1955, Emmons 1969): https://faculty.tuck.dartmouth.edu/images/uploads/faculty/principles-sequencing-scheduling-2e/Notes2e2.pdf"
  - "Wikipedia, Scheduling (production processes) (hacia adelante y hacia atrás): https://en.wikipedia.org/wiki/Scheduling_(production_processes)"
  - "IISE, Z94.14 Operations & Inventory Planning & Control, entrada backward scheduling (según el resumen): https://www.iise.org/Details.aspx?id=2402"
  - "Documentación de Work Order de un sistema abierto (programación de las operaciones): https://docs.frappe.io/erpnext/user/manual/en/work-order"
  - "ANSI/ISA-95.00.03-2013, vista previa (finite capacity scheduling): https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf"
  - "Gallego, apuntes de Columbia sobre Factory Physics (cuello de botella y WIP crítico): https://www.columbia.edu/~gmg2/4000/pdfold/throughput.pdf"
  - "Watson, Blackstone y Gardiner (2007), The evolution of a management philosophy: The theory of constraints, Journal of Operations Management 25:387-402 (copia en la Universidad de Ferrara): https://www.unife.it/economia/lm.economia/insegnamenti/management-strategico-dei-costi-dimpresa/casi-studio/TheoryConstraints.pdf"
  - "Toyota Motor Corporation, Toyota Production System: https://global.toyota/en/company/vision-and-philosophy/production-system/"
  - "Toyota UK, Kanban - Toyota Production System guide: https://mag.toyota.co.uk/kanban-toyota-production-system/"
  - "Toyota UK, Heijunka - Toyota Production System guide: https://mag.toyota.co.uk/heijunka"
  - "Cambridge Institute for Manufacturing, Decision Support Tools, Kanbans: https://www.ifm.eng.cam.ac.uk/research/dstools/kanbans/"
  - "Produccion/.investigacion/ejecucion-en-planta.md (sección 3) y ejecucion-en-planta-2.md (secciones 2 a 4), 2026-11-27"
aliases: [programación de planta, programación de la producción, production scheduling, shop floor scheduling, secuenciación, sequencing, programa detallado, detailed production schedule, work schedule, lista de despacho, dispatch list, job list, reglas de despacho, dispatching rules, reglas de prioridad, FCFS, primero en llegar primero en salir, SPT, menor tiempo de proceso, EDD, fecha de entrega más temprana, razón crítica, critical ratio, holgura, slack, programación hacia adelante, forward scheduling, programación hacia atrás, backward scheduling, carga finita, finite capacity scheduling, cuello de botella, bottleneck, WIP crítico, critical WIP, cinco pasos de enfoque, five focusing steps, tambor-amortiguador-cuerda, drum-buffer-rope, DBR, kanban, heijunka, nivelación de la producción, production leveling, cumplimiento del programa, schedule adherence]
creado: 2026-11-27
revisado: 2026-11-27
---

# Programación de planta

La programación de planta decide en qué orden y en qué momento pasa cada orden de producción por cada centro de trabajo, dentro de la capacidad que hay. Su salida es el programa detallado y la lista de despacho de cada centro, y sus reglas van desde ordenar la cola por fecha de entrega hasta subordinar toda la planta al cuello de botella o dejar que el consumo dispare la producción con kanban.

Es el paso de [Ejecución en planta](ejecucion-en-planta.md) donde el plan choca con las máquinas. El [MRP](../Planificacion-de-la-produccion/mrp.md) fija fechas sin mirar la capacidad y la [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md) dice si las horas alcanzan por período; acá se decide qué va primero en cada centro de la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md). Lo que se programa son las operaciones de cada [orden de producción](orden-de-produccion.md) liberada. Los nombres del programa detallado y de la lista de despacho son los de ISA-95, explicados en [marcos de la producción](../Fundamentos/marcos-de-la-produccion.md#el-vocabulario-de-la-edición-2013). Cuándo se puede parar un equipo para mantenimiento es una negociación con [planificación y programación](../../Activos-y-mantenimiento/Orden-de-trabajo/planificacion-y-programacion.md#parar-el-equipo-el-acuerdo-con-producción) de mantenimiento.

## Cuatro reglas de despacho

Una regla de despacho ordena la cola de un centro de trabajo. Las definiciones son de los apuntes de un curso (fuente débil):

| Regla | Qué va primero |
|---|---|
| FCFS, primero en llegar | el que llegó antes |
| SPT, menor tiempo de proceso | el más corto |
| EDD, fecha de entrega más temprana | el que vence antes |
| Razón crítica | el menor valor de «Time remaining before due date/Remaining processing time» |

Los mismos apuntes definen la holgura como «time remaining before due date - remaining processing time»: la menor va primero.

Dos de las reglas tienen un resultado demostrado para una sola máquina. Con todos los trabajos disponibles al inicio, «The SPT rule gives an optimal schedule» para la suma de los tiempos de terminación, y por eso minimiza el tiempo medio de flujo. EDD «is optimal for 1||Lmax»: minimiza el atraso máximo. Si los trabajos llegan en momentos distintos, EDD sigue siendo óptima si se permite interrumpir un trabajo; sin interrupción, el problema es «strongly NP complete». La razón crítica no tiene un resultado de optimalidad en ninguna fuente leída.

> [!IMPORTANT]
> De quién es la regla EDD. La tradición la atribuye a Jackson (1955). Baker y Trietsch, en las notas de su libro, dicen que «the EDD result is often attributed to Jackson (1955), which is an unpublished working paper», pero que según Smith, Jackson la generalizó al caso con llegadas, «which suggests that the basic EDD is still due to Smith» (1956). Agregan que el nombre EDD lo acuñó Emmons en 1969. No se leyó a Smith ni a Jackson.

### Las cuatro reglas en una máquina

Un caso de la base: cuatro órdenes esperan en la misma máquina, en este orden de llegada.

| Orden | Tiempo de proceso (días) | Entrega (día) |
|---|---|---|
| A | 6 | 8 |
| B | 2 | 6 |
| C | 8 | 18 |
| D | 3 | 15 |

Resultados (cuentas de la base; la razón crítica se recalcula cada vez que se libera la máquina, porque usa el tiempo que falta):

| Regla | Secuencia | Flujo medio (días) | Atraso máximo (días) | Órdenes atrasadas |
|---|---|---|---|---|
| FCFS | A, B, C, D | 12,25 | 4 (D) | 2 |
| SPT | B, D, A, C | 9,25 | 3 (A) | 2 |
| EDD | B, A, D, C | 10 | 1 (C) | 1 |
| Razón crítica | A, B, C, D | 12,25 | 4 (D) | 2 |

SPT da el menor flujo medio y EDD el menor atraso máximo, como dicen los teoremas. Acá la razón crítica coincide con FCFS: en el día 6, B tiene razón 0 y va primero. Con varias máquinas, llegadas escalonadas y preparaciones, las reglas son heurísticas y ninguna gana siempre.

## Hacia adelante o hacia atrás

Programar hacia adelante es, según Wikipedia, «planning the tasks from the date resources become available to determine the shipping date or the due date». Hacia atrás es partir de la entrega: «planning the tasks from the due date or required-by date to determine the start date and/or any changes in capacity required». El glosario del IISE define igual la programación hacia atrás, según el resumen.

Un sistema abierto programa hacia adelante con capacidad finita: ubica cada operación «serially after the planned start date based on the Workstation availability», dentro de un horizonte que «is set to 30 Days by default». Como criterio de la base, hacia atrás sirve para no empezar antes de tiempo, y hacia adelante, para saber si la fecha prometida es posible.

La carga finita la define ISA-95 como la programación «where work is scheduled for a set of manufacturing resources, in such a way that no capacity scheduled exceeds the capacity available». La diferencia con la carga infinita del MRP se discute en [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md).

> [!NOTE] Sin fuente todavía: las definiciones de programación hacia adelante y hacia atrás, razón crítica y FCFS en el diccionario de ASCM o en un libro de texto.

## El cuello de botella marca el ritmo

En *Factory Physics*, según unos apuntes de Columbia, la tasa del cuello de botella es «the rate of the process center having least long-term capacity», y la producción en proceso crítica (WIP crítico) es «Wo = rb To», con To el tiempo de proceso sin esperas. El ejemplo de los apuntes: con una tasa de media unidad por hora y 8 horas de proceso, el WIP crítico es 0,5 × 8 = 4. Debajo de ese nivel, la línea no llega a su ritmo máximo; encima, más producción en proceso solo alarga el tiempo de ciclo, como dice la ley de Little en [Ejecución en planta](ejecucion-en-planta.md#la-ley-de-little-ordena-la-planta) (lectura de la base).

### Los cinco pasos y tambor-amortiguador-cuerda

La teoría de las restricciones convierte esa idea en un procedimiento. Su origen y la discusión sobre su evidencia están en [fundamentos de producción](../Fundamentos/fundamentos-de-produccion.md). Según la revisión de Watson, Blackstone y Gardiner (2007), los cinco pasos son:

1. «identify the constraint».
2. Explotarla: lograr «the highest rate of throughput possible within the confines of the system's current resources».
3. «subordinate the system to the constraint».
4. Elevarla: sumar capacidad en la restricción.
5. Volver a empezar: «if in the previous steps a constraint has been broken, start over; do not let inertia set in».

Tambor-amortiguador-cuerda es la aplicación de esos pasos al programa. La misma revisión lo resume así: «The constraint, or drum, determines the pace of production. The rope is the material release mechanism; releases material to the first operation at a pace determined by the constraint. Material release is offset from the constraint schedule by a fixed amount of time, the buffer». El nombre viene de metáforas de *The Goal*, detalladas en *The Race* (Goldratt y Fox, 1986).

El amortiguador es un tiempo, no una cantidad. Hay tres: de tiempo, delante de la restricción; de envío, un poco de terminado para proteger las entregas; y de capacidad, la que les sobra a los centros que no son restricción. El largo de la cuerda fija la producción en proceso, y Watson y otros marcan el compromiso: un amortiguador más grande protege más a la restricción, pero liberar antes «increases both WIP and lead time».

## Kanban: que el consumo dispare la producción

Toyota define el justo a tiempo como «making only what is needed, when it is needed, and in the amount needed». El mecanismo, en su sitio global: el proceso anterior tiene un depósito de terminados del que el siguiente retira lo que necesita, y repone «whatever was picked up». Kanban es la señal: según Toyota UK, «A system that conveys information between processes and automatically orders parts as they are used up», donde cada caja lleva su tarjeta y las tarjetas vuelven al proceso anterior como órdenes.

Según el Instituto de Manufactura de Cambridge, hay dos tarjetas básicas: la de retiro, que dice qué y cuánto llevarse del proceso anterior, y la de producción, que dice qué y cuánto fabricar. Quitar tarjetas acorta los tiempos, pero deja el sistema «more vulnerable to breakdowns». Como la cantidad de tarjetas fija el inventario en circulación, kanban limita la producción en proceso (lectura de la base).

Toyota UK enumera seis reglas: «1) Never pass on defective products; 2) Take only what is needed; 3) Produce the exact quantity required; 4) Level the production; 5) Fine-tune production; and 6) Stabilise and rationalise the process». Hay varias versiones de las reglas según la edición del manual o el libro; esta es la de la filial británica.

Kanban no reemplaza el plan. Cambridge aclara que ajusta la producción a cambios de la demanda «of up to + or - 10%» y que «The system requires planned monthly and weekly production schedules». La nivelación (heijunka) prepara ese terreno: Toyota UK la define como «production leveling (finding and keeping average production volumes)», y la logra «by assembling a mix of models within each batch».

> [!NOTE] Sin fuente todavía: las reglas de kanban en su texto original (Sugimori y otros, 1977; Ohno; Monden).

## Cumplimiento del programa

> [!NOTE] Sin fuente todavía: una definición y una fórmula del cumplimiento del programa de producción. Como inferencia de la base, se mide comparando, por período, las órdenes u operaciones terminadas en su fecha con las programadas. Una crítica académica a la OEE señala que esa medida «does not consider compliance with the production plan» (ver [eficiencia global del equipo](eficiencia-global-del-equipo.md)).

## Qué guarda un programa de planta

- Por operación programada: centro de trabajo, inicio y fin planificados, posición en la cola, estado y tiempos reales.
- Por orden: fecha de entrega comprometida y tiempo de proceso restante, que son los datos de SPT, EDD y la razón crítica. La regla no se guarda: se calcula.
- El calendario de cada centro, con sus turnos y las ventanas reservadas para mantenimiento.
- Con restricciones: cuál centro es el cuello de botella, el tiempo de amortiguador por producto y la fecha de liberación del material que resulta.
- Con kanban: por bucle, artículo, cantidad por contenedor, proceso proveedor y cliente, número de tarjetas y estado de cada una.

Lo de restricciones y kanban sale de las fuentes, no de un sistema leído. En papel, el programa es un tablero por centro con las órdenes en fila, y kanban, las tarjetas mismas.
