# Ejecución en planta, segunda ronda: cierre de huecos

Fecha de la búsqueda: 2026-11-27. Complementa a `ejecucion-en-planta.md` (primera ronda).

Cómo leí esta vez. Bajé los PDF y las páginas con curl y extraje el texto con pdftotext o quitando las etiquetas HTML, así que [L] significa texto crudo completo, sin resumen de un modelo. [S] es lo que devolvió un lector que resume (WebFetch) o un buscador. [M] son metadatos. Las citas literales están en el idioma original y salen del texto extraído (los PDF de Little perdieron la letra griega lambda en la extracción; la fórmula se ve igual en el título y en el resumen del artículo). Cada afirmación lleva su URL. "Un sistema abierto" es documentación de código abierto, sin nombrar al proveedor en el cuerpo del tema.

Resumen de lo cerrado y lo que sigue abierto:

| # | Hueco | Estado |
|---|---|---|
| 1 | Ley de Little | Cerrado: Little (2011) [L], con la versión de fábrica TH = WIP/CT |
| 2 | Reglas de despacho, hacia adelante y hacia atrás | Casi cerrado: SPT y EDD en tres textos [L]; razón crítica y FCFS en apuntes [L]; hacia adelante/atrás solo en Wikipedia [L] y en glosario IISE [S]; carga finita sigue siendo la cita de ISA-95 de la ronda 1 |
| 3 | TOC y DBR | Cerrado con una revisión académica [L] (Watson, Blackstone y Gardiner 2007); el TOCICO Dictionary y Rahman 1998 no abrieron |
| 4 | Kanban y JIT | Casi cerrado: Toyota (global y UK) [L] y un resumen de Cambridge IfM [L]; Sugimori et al. 1977 solo metadatos |
| 5 | OEE | Parcial: ISO 22400-2 vista previa [L] (términos APT y PBT, sin la fórmula del OEE); el 85 % y sus críticas con un artículo académico [S] |
| 6 | Orden discreta/repetitiva/proceso, estados, backflush | Estados cerrados con dos sistemas abiertos [L]; ISA-88 pagina oficial [L] sin definiciones; discreta/repetitiva sin fuente seria abierta; backflush en un glosario [S] |
| 7 | Subproducto y coproducto | Cerrado: NIC 2 párrafo 14, en inglés y en español (Diario Oficial UE) [L]; glosario IISE [S] discrepa en el uso de "coproducto" |

---

## 1. Ley de Little

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 1.1 | J. D. C. Little (2011), "Little's Law as Viewed on Its 50th Anniversary", Operations Research 59(3), pp. 536-549, doi 10.1287/opre.1110.0940 (copia de un curso de UMass) | https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf | primaria (el autor de la ley) | [L] | 3 | 3 | 3 | 3 |
| 1.2 | Registro bibliográfico de 1.1 | https://econpapers.repec.org/RePEc:inm:oropre:v:59:y:2011:i:3:p:536-549 | metadatos | [M] | 2 | 1 | 1 | 1 |

Nota de copia: el MIT (web.mit.edu/sgraves/...) devolvió una página HTML y no el PDF; la copia de UMass es el PDF con la primera página del artículo publicado. La copia de UMass no es del sitio de la editorial; la versión de referencia es el DOI.

### Afirmaciones (todas de 1.1 [L])

- Origen y nombre: "Fifty years ago, the author published a paper in Operations Research with the title, 'A proof for the queuing formula: L = λW' [Little, J. D. C. 1961. A proof for the queuing formula: L = λW. Oper. Res. 9(3) 383-387]. Over the years, L = λW has become widely known as 'Little's Law.' Basically, it is a theorem in queuing theory."
- Definición de cada término (versión de colas): "L = average number of items in the system during [0, T]"; "λ = average arrival rate in [0, T] (items/time unit)"; "W = average waiting time of an item during [0, T] (time units)".
- Enunciado y demostración: "Theorem LL.1 (Little's Law). For a queuing system observed over [0, T] that is empty at 0 and T and has 0 < T < ∞, the formula L = λW holds." Con L = A/T, λ = N/T, W = A/N (A es el área bajo la curva del número de ítems en el sistema), se llega a "L = A/T = (A/T)(N/N) = (N/T)(A/N) = λW".
- Condiciones, lo que Little aclara que no hace falta: "LL.1 holds under nonstationary conditions." y "LL.1 holds independent of queue discipline." (el orden de atención, FIFO, LIFO o por prioridad, no importa). Por qué vale: "An item in queue is also waiting. In other words, at the same time that a customer is standing in line and so can be counted, he or she is also accumulating minutes waiting."
- Cómo lo leen en gestión de operaciones, citando a Hopp y Spearman (2000): se escribe "T H = WIP/CT", con "T H = throughput", "WIP = work in process" y "CT = cycle time". Little y Graves (2008) señalan que "T H = WIP /CT is equivalent to λ = L/W" y que la diferencia es que en gestión de operaciones la ley se enuncia con la tasa de salida y no la de llegada: "This reflects the perspective of a typical operating manager, especially in manufacturing."
- Consecuencia práctica, literal: "any increase in output requires either an increase in work-in-process inventory or a reduction in cycle time or both, unless some change is made in the manufacturing process itself."
- Definiciones de Hopp y Spearman que Little reproduce: throughput es "the average output of a production process (machine, workstation, line, plant) per unit time"; WIP es "the inventory between the start and end points of a product routing"; cycle time es "the average time from release of a job at the beginning of the routing until it reaches an inventory point at the end of the routing (that is, the time the part spends as WIP.)".
- Sobre la liberación de trabajo: "in many contexts the output rate is determined exogenously ... The operations manager decides the arrivals based on desired outputs." (el proceso de llegadas es endógeno en una fábrica).
- Otra versión de fábrica que cita Little (de Hopp y Spearman, p. 49 del texto que menciona): "Process Lead Time = (Number of 'Things' in Process) / (Completions per Hour)".

Corrección a la ronda 1: la segunda condición ("The only requirement is that the system be ergodic.") salía de Wikipedia. Para la versión de muestra finita que da Little no hace falta estacionariedad ni ergodicidad: vale como identidad exacta sobre el intervalo observado. Para el enunciado de largo plazo con valores esperados sí hacen falta condiciones; no las verifiqué en un texto primario.

### Qué registra un sistema

Para poder usarla: por orden, la fecha de liberación y la de terminación (de ahí sale el tiempo de ciclo) y las cantidades en proceso por instante (de ahí el WIP). Evidencia de un sistema abierto: la orden guarda fecha de inicio planificada y fechas reales (https://docs.frappe.io/erpnext/user/manual/en/work-order [L]: "Planned Start Date", "Expected Delivery Date", "Actual Start Time, and Actual End Time").

### Recurso canónico propuesto

Little (2011), secciones 2.1 (demostración) y 4.2 (gestión de operaciones). Fijarse en que es una identidad sobre lo observado, no un pronóstico: "we are in the measurement business, not the forecasting business".

---

## 2. Reglas de despacho y programación hacia adelante y hacia atrás

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 2.1 | Baker y Trietsch, Principles of Sequencing and Scheduling (2.ª ed.), notas de investigación del cap. 2 (sitio de Tuck, Dartmouth) | https://faculty.tuck.dartmouth.edu/images/uploads/faculty/principles-sequencing-scheduling-2e/Notes2e2.pdf | secundaria (libro de texto, comenta las fuentes primarias) | [L] | 3 | 2 | 1 | 3 |
| 2.2 | Notas del cap. 1 del mismo libro | https://faculty.tuck.dartmouth.edu/images/uploads/faculty/principles-sequencing-scheduling-2e/Notes2e1.pdf | idem | [L] | 3 | 1 | 1 | 2 |
| 2.3 | Dartmouth CO 454, Lecture 3 (apuntes de curso; SPT con demostración) | https://cs.dartmouth.edu/~deepc/Courses/S09/Lectures/lecture3.pdf | secundaria | [L] | 2 | 3 | 1 | 1 |
| 2.4 | Nieberg, Single Machine Scheduling (diapositivas, Bonn) | https://www.or.uni-bonn.de/lectures/ss10/scheduling_data/sched10_2.pdf | secundaria | [L] | 2 | 2 | 1 | 1 |
| 2.5 | Schwiegelshohn, Scheduling Problems and Solutions (TU Dortmund, 2006; material del curso de Pinedo en NYU) | https://web-static.stern.nyu.edu/om/faculty/pinedo/scheduling/schwiegelshohn2006.pdf | secundaria | [L] | 2 | 2 | 1 | 1 |
| 2.6 | Apuntes de un curso (Univ. de Kentucky), reglas de prioridad | https://www.uky.edu/~dsianita/300/schedule.html | secundaria | [L] | 1 | 1 | 2 | 1 |
| 2.7 | Wikipedia, Scheduling (production processes) | https://en.wikipedia.org/wiki/Scheduling_(production_processes) | secundaria | [L] | 1 | 1 | 1 | 1 |
| 2.8 | Glosario IISE Z94.14, Operations & Inventory Planning & Control | https://www.iise.org/Details.aspx?id=2402 | secundaria (glosario de una asociación) | [S] | 2 | 1 | 1 | 2 |
| 2.9 | Documentación de Work Order de un sistema abierto | https://docs.frappe.io/erpnext/user/manual/en/work-order | primaria (práctica) | [L] | 2 | 3 | 2 | 3 |

### Afirmaciones

- SPT: "Process the jobs in increasing order of processing time." ("Definition 2.1. (SPT)") y "The SPT rule gives an optimal schedule (1 | | ΣCj)." ("Theorem 2.2"), con demostración por intercambio de pares consecutivos (2.3 [L]). Como el tiempo medio de flujo es la suma de los tiempos de terminación sobre n, el mismo orden lo minimiza; el paso de Cj a flujo medio es mi cuenta (sin liberaciones distintas de cero, flujo y terminación coinciden). La condición es una máquina y todos los trabajos disponibles en el instante 0.
- Regla ponderada: "Definition 2.3. (WSPT): Process the jobs in decreasing order of wj/pj." y "The WSPT rule gives an optimal schedule (1 | | Σ wj Cj)." (2.3 [L]); en las diapositivas de 2.5 [L] se la llama "Smith order".
- EDD: "Earliest due date first (EDD) is optimal for 1||Lmax (Jackson's EDD rule)" (2.4 [L]); "1 | rj , prmp | Lmax can be solved by the preemptive Earliest Due Date (EDD) first rule." y "The resulting schedule is optimal if it is nonpreemptive." (2.5 [L]). Es decir: con liberaciones distintas de cero la EDD es óptima si se permite interrumpir; el caso sin interrupción con liberaciones es "strongly NP complete" (2.5 [L], "1 | rj | Lmax is strongly NP complete."). Esto aclara la duda de la ronda 1 sobre la condición de interrupción.
- Atribución histórica (2.1 [L]): "Many of the basic models we covered in this chapter appeared for the first time in a seminal paper by Smith (1956)." y "We should note that the EDD result is often attributed to Jackson (1955), which is an unpublished working paper. According to Smith, however, Jackson had generalized EDD to the dynamic arrival case, which suggests that the basic EDD is still due to Smith." Además, "the terms SPT, SWPT and EDD are more recent. For example, to our knowledge, the term EDD was coined by Emmons (1969)." Las referencias completas que da el libro (2.1 [L]): "Smith, W.E. (1956) 'Various Optimizers for Single Stage Production,' Naval Research Logistics Quarterly 3, 59-66." y "Jackson, J.R. (1955) 'Scheduling a Production Line to Minimize Maximum Tardiness,' Research Report 43, Management Science Research Project, University of California, Los Angeles." Discrepancia: la tradición dice Jackson 1955 para EDD; Baker y Trietsch dicen que la EDD básica es de Smith. Hay que dar las dos. No leí ninguno de los dos originales.
- Definición de las reglas de prioridad, con la fórmula (2.6 [L]): la lista es "First Come First Serve (FCFS)", "Shortest Processing Time (SPT)", "Earliest Due Date (EDD)", "Slack Time Remaining (STR) = time remaining before due date - remaining processing time" ("The shortest STR goes first") y "Critical Ratio (CR) = Time remaining before due date/Remaining processing time" ("The smallest CR goes first"). Medidas de comparación del mismo texto: "Average Completion time/Mean flow time =(Total processing time + total waiting time)/Number of jobs" y "Average lateness = total late days/number of jobs". Fuente débil (apuntes de un curso, que remite a "pg.590" de un libro no identificado). Para FCFS no hallé una definición más formal que su nombre.
- Razón crítica: no hallé resultado de optimalidad en ningún texto. Las diapositivas de 2.5 y 2.4 no la tratan.
- Programación hacia adelante y hacia atrás (2.7 [L]): "Forward scheduling is planning the tasks from the date resources become available to determine the shipping date or the due date." y "Backward scheduling is planning the tasks from the due date or required-by date to determine the start date and/or any changes in capacity required." Glosario IISE (2.8 [S]): "BACKWARD SCHEDULING ... A technique in which the schedule is computed starting with the due date for the order and working backward" (remite a "FORWARD SCHEDULING"). Fuente primaria no hallada: es un hueco para APICS Dictionary.
- Evidencia de práctica: un sistema abierto "will reserve a slot for each of the Work Order Operations serially after the planned start date based on the Workstation availability" y deja configurar "the number of days for the system to try scheduling the operations in the Manufacturing Settings. This is set to 30 Days by default." (2.9 [L]). Es programación hacia adelante a partir de la fecha de inicio planificada, con capacidad finita por centro de trabajo y horario.
- Carga finita: sigue valiendo la cita de ISA-95.00.03 de la ronda 1 ("finite capacity scheduling: scheduling methodology where work is scheduled for a set of manufacturing resources, in such a way that no capacity scheduled exceeds the capacity available", https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf). Sin nueva fuente.

### Qué registra un sistema

Por operación programada: centro de trabajo, inicio y fin planificados, secuencia, estado; por orden, fecha de entrega comprometida (necesaria para EDD, STR y razón crítica) y tiempo de proceso restante (necesario para SPT y razón crítica). La regla de despacho no es un dato que se guarde: se calcula con esos campos. Evidencia: 2.9 [L].

### Recurso canónico propuesto

Baker y Trietsch, Principles of Sequencing and Scheduling, capítulo 2 (SPT, WSPT, EDD) y sus notas de investigación (2.1, abiertas); para el enunciado con demostración, 2.3. Fijarse en las condiciones: una máquina, trabajos disponibles al inicio, sin interrupción. Para el taller real (varias máquinas, liberaciones, preparaciones) las reglas son heurísticas y no óptimas.

---

## 3. Teoría de las restricciones: cinco pasos y tambor-amortiguador-cuerda

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 3.1 | K. J. Watson, J. H. Blackstone y S. C. Gardiner (2007), "The evolution of a management philosophy: The theory of constraints", Journal of Operations Management 25, pp. 387-402 (copia en el sitio de la Univ. de Ferrara) | https://www.unife.it/economia/lm.economia/insegnamenti/management-strategico-dei-costi-dimpresa/casi-studio/TheoryConstraints.pdf | secundaria (revisión académica, autores con trayectoria en APICS) | [L] | 3 | 3 | 2 | 2 |
| 3.2 | TOCICO (cursos), mencionan el Dictionary 2.ª ed. | https://learningcenter.tocico.org/courses/Introduction-to-the-Theory-of-Constraints | primaria (organización de la TOC) | [S] | 2 | 1 | 1 | 1 |
| 3.3 | Rahman (1998), IJOPM 18(4), pp. 336-355 | https://emerald.com/insight/content/doi/10.1108/01443579810199720/full/html | primaria (revisión) | [M] (paywall) | 2 | 3 | 1 | 2 |

### Afirmaciones (3.1 [L], salvo que se indique)

- Origen: "In 1984, he and Jeff Cox wrote The Goal, a manufacturing novel in which the protagonist, Alex Rogo, saves his plant with the help of some pointed questions by his mentor, Jonah." Y: "In twenty-five years, what started out as a scheduling software has evolved into a management philosophy".
- Los cinco pasos, literal: "At its most basic, The Goal outlines the Five Focusing Steps (5FS), the process by which TOC concepts are implemented." "The first of the Five Focusing Steps is to identify the constraint." "Once the constraint has been identified, the next step is to determine the most effective means to exploit it. Exploitation of the constraint seeks to achieve the highest rate of throughput possible within the confines of the system's current resources." "... the third step is to subordinate the system to the constraint." "... the fourth step elevates throughput by adding capacity to the system at the constraint location." "Finally, the fifth step renews the improvement cycle by stating 'if in the previous steps a constraint has been broken, start over; do not let inertia set in.'" Principio de base: "constraints determine the performance of a system."
- Prerrequisitos de la versión ampliada (POOGI): "The first prerequisite for implementation is to define the system under investigation and identify its purpose. Having defined the purpose of the system, the second prerequisite is to define measurements that align the system to that purpose."
- Definición de restricción, que Watson et al. toman del APICS Dictionary (Blackstone y Cox, 2004): "any element or factor that prevents a system from achieving a higher level of performance with respect to its goal". Tres formas: "physical (resource capacity less than demand), market (demand less than resource capacity), and policy (formal or informal rules that limit productive capacity of the system); DBR is intended to address market or physical constraints."
- Tambor, amortiguador y cuerda, literal: "The constraint, or drum, determines the pace of production. The rope is the material release mechanism; releases material to the first operation at a pace determined by the constraint. Material release is offset from the constraint schedule by a fixed amount of time, the buffer. Buffers are strategically placed to protect shipping dates and to prevent constraint processes from starvation due to a lack of materials." Origen del nombre: "This technique, which derives its name from metaphors developed in The Goal and spelled out in The Race, has been well defined in the literature (Goldratt and Fox, 1986; ...)". Esto resuelve la discrepancia de la ronda 1 sobre el origen: la metáfora nace en The Goal y se detalla en The Race (Goldratt y Fox, 1986).
- Tres tipos de amortiguador: "TOC makes use of three distinct buffer types: time, shipping, and capacity." Tiempo: "Time buffers offset the release of raw materials by the protection or buffer time allowed." Envío: "Shipping buffers maintain a small amount of finished good inventory used to protect due date performance". Capacidad: "Capacity buffers exist in a TOC system to the extent that non-constrained resources have extra capacity."
- La cuerda y el inventario: "the rope subordinates non-constraint machines to the constraint, releasing inventory to the production system based on the rate of consumption at the constraint. The 'length' of the rope, hence the amount of inventory in the system, is determined by the protection to the constraint provided by the buffer." Compromiso: "increasing buffer size increases the amount of protection for the constraint; however, releasing material earlier, increases both WIP and lead time."
- Evidencia empírica a favor (según la misma revisión): "rigorous testing of DBR indicates that TOC systems produce greater numbers of product while reducing inventory, manufacturing lead time, and the standard deviation of cycle time." Crítica, de la ronda 1 y sin contraste nuevo: Gupta y Snyder (2009) en Wikipedia [S] dicen lo contrario, que la TOC no demostró eficacia en la literatura académica. Dos fuentes que discrepan: darlas las dos. La revisión de Watson et al. es de 2007, anterior a la crítica de 2009.
- Medición: Watson et al. cuentan que Goldratt llevó la crítica a la contabilidad de costos: "cost accounting is public enemy number one to productivity" (Goldratt 1983, citado en 3.1 [L]). Frontera con Costos-de-produccion y con el sistema de costeo ya escrito.

### Qué registra un sistema

El recurso restricción identificado y su ritmo (tasa del cuello); el tiempo de amortiguador por producto o ruta; la fecha de liberación de material calculada hacia atrás desde el programa del tambor; el estado del amortiguador por orden (cuánto del amortiguador se consumió). Sin evidencia de un sistema abierto que lo registre de forma nativa (no lo busqué en esta ronda).

### Recurso canónico propuesto

Watson, Blackstone y Gardiner (2007) para el mapa de la TOC con definiciones citables y de acceso abierto; Goldratt y Cox, The Goal (1984), y Goldratt y Fox, The Race (1986), para el origen (no leídos). Fijarse en que DBR es la aplicación de programación de los pasos 2 y 3, y en que el amortiguador es un tiempo, no una cantidad.

---

## 4. Kanban, JIT y nivelación

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 4.1 | Toyota Motor Corporation, Production System (sitio global) | https://global.toyota/en/company/vision-and-philosophy/production-system/ | primaria | [L] | 3 | 2 | 1 | 3 |
| 4.2 | Toyota UK, "Kanban - Toyota Production System guide" | https://mag.toyota.co.uk/kanban-toyota-production-system/ | primaria (blog de la filial) | [L] | 3 | 1 | 1 | 2 |
| 4.3 | Toyota UK, "Heijunka - Toyota Production System guide" | https://mag.toyota.co.uk/heijunka | primaria (blog de la filial) | [L] | 3 | 1 | 2 | 2 |
| 4.4 | Cambridge Institute for Manufacturing, Decision Support Tools, "Kanbans" (cita a Monden 1993 y Schonberger 1982) | https://www.ifm.eng.cam.ac.uk/research/dstools/kanbans/ | secundaria | [L] | 2 | 2 | 3 | 2 |
| 4.5 | Sugimori, Kusunoki, Cho y Uchikawa (1977), "Toyota production system and Kanban system: materialization of just-in-time and respect-for-human system", International Journal of Production Research 15(6), pp. 553-564 | https://www.tandfonline.com/doi/pdf/10.1080/00207547708943149 (403) | primaria | [M] solo cita | 3 | 3 | 2 | 3 |

El DOI/URL de Taylor & Francis dio 403 y no hallé copia abierta. Los datos de volumen, número y páginas salen de un resumen del buscador; no los verifiqué en la editorial. Sin abstract.

### Afirmaciones

- JIT, literal (4.1 [L]): "The basic philosophy of the Toyota Production System is based on two pillars. The first pillar is jidoka ... 'automation with a human touch' ... The second pillar is Just-in-Time, based on the concept of synchronizing production processes ... by making only what is needed, when it is needed, and in the amount needed." Los principios: "1) Only make what is needed by the customer, when it is needed, and in the amount needed; 2) Don't allow goods and information to be held up during production; 3) Make them at the pace at which they're sold."
- Mecanismo de reposición, literal (4.1 [L]): "The preceding process has a store of finished products from which the next process can pick up the parts that it needs. The preceding process is also stocked in advance with the minimum number of parts needed to re-make parts picked up by the next process before the next pick-up, allowing it to immediately replenish whatever was picked up." Esta página global no usa la palabra "kanban" (verifiqué con búsqueda de texto); el mecanismo está descrito sin nombrarlo.
- Jidoka, literal (4.1 [L]): "when an abnormality occurs, such as a machine or equipment abnormality, quality abnormality, or a work delay, the machine or equipment can detect the abnormality and stop automatically, or the operator can stop the line by pulling the stop cord themselves."
- Origen del JIT (4.1 [L]): "TPS has evolved through many years of trial and error to improve efficiency based on the Just-in-Time concept developed by Kiichiro Toyoda"; y la cita de Kiichiro: "A complete car cannot be built if even one part is missing."
- Qué es kanban (4.2 [L]): "Kanban (English: Signboard): A system that conveys information between processes and automatically orders parts as they are used up. Every item or box of items that flows through the production process carries its own kanban. Kanbans come off items that have been used or transported and go back to the preceding processes as orders for additional items".
- Las reglas (4.2 [L]): "Toyota has six rules for the effective application of Kanban: 1) Never pass on defective products; 2) Take only what is needed; 3) Produce the exact quantity required; 4) Level the production; 5) Fine-tune production; and 6) Stabilise and rationalise the process." Un blog independiente (AllAboutLean, https://www.allaboutlean.com/toyotas-six-rules/, [S], aparecido en el buscador, no leído entero) advierte que hay varias versiones de las reglas (manual de 1973, manual de 1988, libro de Ohno): la lista es la de Toyota UK y puede diferir en otras ediciones.
- Tipos de tarjeta (4.4 [L]): "A Withdrawal Kanban - specifies the kind and quantity of product which a manufacturing process should withdraw from a preceding process." y "A Production-ordering Kanban - specifies the kind and quantity of product which the preceding process must produce ... often called an in-process Kanban or simply a production Kanban." Datos que lleva la tarjeta de retiro del ejemplo: proceso anterior, ubicación, cantidad por caja (20 unidades), forma del contenedor y número de tarjeta ("the 4th of 8 issued"). También existen tarjetas de proveedor y de señal: "Supplier Kanbans - to withdraw goods from external suppliers, and two types of Signal Kanban ... inserted near the bottom of a stack of items. These automatically initiate production of batch produced items when the stock reaches a pre-set re-order level."
- Cómo circula (4.4 [L]): "Each process ... has two Kanban 'post-boxes', one for withdrawal and one for production-ordering Kanbans." Un pallet lleno lleva tarjetas de producción; al retirarlo se las cambia por una de retiro; cuando se empieza a usar el pallet, la tarjeta de retiro vuelve al buzón.
- Alcance y límites (4.4 [L]): "Kanbans help simplify planning and to fine-tune production to meet changing customer demand of up to + or - 10%. The system requires planned monthly and weekly production schedules." y "Kanban systems can be tightened by removing cards or by reducing the number of parts on a pallet. The effect will be to speed the flow through the process and hence reduce lead times. However it also makes the system more vulnerable to breakdowns". Es decir, la cantidad de tarjetas es la cantidad de inventario en circulación, y relaciona con la ley de Little (inventario = tasa × tiempo).
- Nivelación (heijunka), literal (4.3 [L]): "Heijunka (English: Production smoothing or leveling): A technique to facilitate Just-In-Time (JIT) production, it means production leveling (finding and keeping average production volumes) and is used to smooth out production in all departments as well as that of the supplier over a period of time." "The Toyota Production System uses Heijunka to solve the former by assembling a mix of models within each batch, and ensuring that there is an inventory of product proportional to the variability in demand." "Just-In-Time delivery makes Heijunka possible." En la respuesta a un lector, Toyota UK dice que se usa "across our entire production system". Esto complementa a Wikipedia (heijunka) de la ronda 1; ya no depende de ella.
- Sugimori et al. (1977): solo la referencia. No hay texto. Hueco para citar las reglas originales.

### Qué registra un sistema

Por tarjeta o bucle: artículo, cantidad por contenedor, proceso proveedor y proceso cliente, ubicación de almacenamiento, número de tarjetas en el bucle y su estado (en vacío, en producción, en tránsito). Para nivelar: el programa de montaje final con la mezcla por turno. Sin evidencia de un sistema abierto en esta ronda.

### Recurso canónico propuesto

Toyota Production System en el sitio global (4.1) para JIT y jidoka, y la guía de kanban de Toyota UK (4.2) para las seis reglas. Para el mecanismo, Monden, Toyota Production System: An Integrated Approach to Just-In-Time (2.ª ed., 1993, no leído) y Sugimori et al. (1977). Fijarse en que la tarjeta es una orden de reposición entre dos procesos con una cantidad fija, y en que el número de tarjetas fija el inventario máximo.

---

## 5. OEE

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 5.1 | ISO 22400-2:2014, Automation systems and integration - KPIs for manufacturing operations management - Part 2: Definitions and descriptions (vista previa del distribuidor iTeh; la ficha oficial es https://www.iso.org/standard/54497.html) | https://cdn.standards.iteh.ai/samples/54497/10e33d2a34c144558b5e3024ee5e1cb0/ISO-22400-2-2014.pdf | primaria (extracto) | [L] (extracto) | 3 | 1 | 1 | 3 |
| 5.2 | Bengtsson, Andersson y Ekström (2022), "Measuring preconceived beliefs on the results of overall equipment effectiveness - A case study in the automotive manufacturing industry", Journal of Quality in Maintenance Engineering 28(2), pp. 391-410, doi 10.1108/JQME-03-2020-0016 | https://www.emerald.com/insight/content/doi/10.1108/JQME-03-2020-0016/full/html | secundaria (artículo académico que cita a Nakajima) | [S] | 2 | 2 | 1 | 1 |
| 5.3 | Bengtsson, Andersson y Ekström, "Misconceptions Within the Use of Overall Equipment Effectiveness - A Theoretical Discussion on Industrial Examples", Advances in Transdisciplinary Engineering 13 (SPS2020), pp. 36-47, doi 10.3233/ATDE200141 | https://ebooks.iospress.nl/pdf/doi/10.3233/ATDE200141 | secundaria | [M] (solo el resumen) | 2 | 1 | 1 | 1 |
| 5.4 | Muchiri y Pintelon (2008), "Performance measurement using overall equipment effectiveness (OEE): literature review and practical application discussion", International Journal of Production Research 46(13), pp. 3517-3535 | https://typeset.io/pdf/performance-measurement-using-overall-equipment-3udssbfefm.pdf (403) | primaria (revisión) | [M] solo cita | 3 | 3 | 2 | 3 |
| 5.5 | Nakajima, Introduction to TPM: Total Productive Maintenance, Productivity Press, 1988 | citado por 5.2 y por la ronda 1 | primaria | no leída | 3 | 3 | 2 | 3 |

### Afirmaciones

- ISO 22400-2 define términos de tiempo que el OEE usa (5.1 [L], extracto de las cláusulas 1 a 5.2): "The planned busy time shall be the planned operation time minus the planned downtime." (PBT, cláusula 5.1.2.4); "The planned operation time shall be the planned time in which a work unit can be used. The operation time is a scheduled time." (POT, 5.1.2.2); "The actual production time shall be the actual time during which a work unit is producing. It includes only the value-adding functions." (APT, 5.1.3.6); "The actual unit processing time shall be the actual production time plus the actual unit setup time." (AUPT); "The actual unit busy time shall be the actual unit processing time plus the actual unit delay time." (AUBT); "The planned run time per item shall be the planned time for producing one quantity unit." (PRI, 5.1.2.5). La lista de símbolos incluye "OEE overall equipment effectiveness" y "NOT net operating time", y el índice de la norma incluye "Annex B (informative) Alternative OEE calculation based on loss time model".
- Alcance (5.1 [L]): "ISO 22400 specifies key performance indicators (KPIs) used in manufacturing operations management (MOM)." y "With reference to equipment, the KPIs in this part of ISO 22400 relate to work units, as specified in IEC 62264."
- La fórmula literal del OEE de ISO 22400-2 (cláusula 6) no está en la vista previa: hueco. Un resumen de buscador la deja en Disponibilidad = APT / PBT ("Actual Production Time" sobre "Planned Busy Time"), que es coherente con los términos citados, pero no leí la cláusula; no la tomo como cita. Tres sitios de proveedores que escriben Disponibilidad = tiempo de marcha / tiempo de producción planificado usan otros términos (no ISO), lo que muestra que hay dos vocabularios para lo mismo (el de oee.com de la ronda 1 y el de ISO 22400). Un sitio de proveedor (Teeptrak) cita la norma con un título equivocado, así que no lo uso.
- Origen del 85 % (5.2 [S], el lector devolvió estas citas del artículo): Nakajima (1988) "presents the following ideal conditions for OEE: availability is greater than 90%, performance is greater than 95% and quality is greater than 99%." y "(0.90 × 0.95 × 0.99) 85%, which is commonly referred to as the world-class level." Los autores atribuyen el 85 % a Jonsson y Lesshammar (1999), no a Nakajima. Esto afina la ronda 1: oee.com atribuye el 85 % a Nakajima como mínimo, pero el artículo académico dice que la cifra de 85 % como "nivel de clase mundial" la formula una cita posterior; lo de Nakajima son las tres condiciones ideales. Coinciden en 90/95/99 (la ronda 1 había visto 99,9 % en Tractian: ese valor es del proveedor, no de la fuente académica).
- Críticas (5.2 [S]): los estudios empíricos "Ljungberg (1998), Hedman et al. (2016), and Ylipää et al. (2017)" muestran que los niveles de OEE en la industria son "a lot lower"; Koch (2003) lo explica por "different ways of setting the OEE definitions"; Ljungberg (1998) sostiene que la definición original "does not consider all factors that reduce capacity utilization"; las seis grandes pérdidas "have thus been multiplied in many practical applications"; y en las conclusiones: "OEE as a measure does not consider compliance with the production plan." Resumen del segundo artículo (5.3 [M]): desafíos como "lack of training and awareness, lack of focus, risk of misunderstanding the measure" y la crítica a "the view on and hunt for world class levels".
- Una fuente académica citada de segunda mano en el buscador (sin leer): "as there is no universally agreed method of applying OEE, the measured results have a risk of potentially being misinterpreted and manipulated" (no la uso como cita).
- Muchiri y Pintelon (2008): el texto no abrió (403). Solo confirmé título, revista, volumen y páginas por el buscador y que describe a TPM como el origen de OEE. No puedo citar su tratamiento del 85 %.
- Nakajima: no leído; las tres condiciones salen del artículo 5.2 (que cita "Nakajima [8]" con fecha 1988). El libro en japonés es de 1984 y la edición en inglés de 1988 (ronda 1): el artículo cita 1988.

### Qué registra un sistema

Sin cambios respecto de la ronda 1; ISO 22400-2 aporta el vocabulario de tiempos para las columnas: tiempo de operación planificado, parada planificada, tiempo ocupado planificado, tiempo de producción real, tiempo de preparación real, tiempo de demora real, y el tiempo planificado de marcha por unidad (PRI, base para el tiempo ideal de ciclo).

### Recurso canónico propuesto

ISO 22400-2:2014, cláusulas 5.1 y 6 (hay que comprar la norma para la fórmula; la vista previa da los términos); Muchiri y Pintelon (2008) para la revisión (no leído); Bengtsson et al. (2022) como crítica. Fijarse en que la norma define los tiempos con precisión (qué es tiempo ocupado planificado) y esa definición, no la fórmula, es lo que más cambia el número.

---

## 6. Tipos de orden, estados de la orden y consumo automático (backflush)

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 6.1 | Documentación de Work Order de un sistema abierto | https://docs.frappe.io/erpnext/user/manual/en/work-order | primaria (práctica) | [L] | 2 | 3 | 2 | 3 |
| 6.2 | Archivo de definición del campo de estado del Work Order de ese sistema (código fuente) | https://raw.githubusercontent.com/frappe/erpnext/develop/erpnext/manufacturing/doctype/work_order/work_order.json | primaria (código) | [L] | 2 | 2 | 1 | 3 |
| 6.3 | Código del modelo de orden de fabricación de otro sistema abierto (rama 18.0), campo de estado con su texto de ayuda | https://raw.githubusercontent.com/odoo/odoo/18.0/addons/mrp/models/mrp_production.py | primaria (código) | [L] | 2 | 2 | 1 | 3 |
| 6.4 | ISA, ISA-88 Series of Standards (página oficial) | https://www.isa.org/standards-and-publications/isa-standards/isa-88-standards | primaria | [L] (página) | 3 | 1 | 1 | 2 |
| 6.5 | Glosario IISE Z94.14 | https://www.iise.org/Details.aspx?id=2402 | secundaria | [S] | 2 | 1 | 1 | 2 |

### Estados de la orden (dos sistemas abiertos, discrepan)

- Primer sistema abierto (6.2 [L]): el campo de estado tiene diez valores: "Draft", "Submitted", "Not Started", "In Process", "Stock Reserved", "Stock Partially Reserved", "Completed", "Stopped", "Closed", "Cancelled". Esto amplía la ronda 1, que solo veía "Stopped": la lista pedida (Draft, Not Started, In Process, Completed, Stopped, Cancelled) está contenida en ella, con cuatro estados más ("Submitted", "Stock Reserved", "Stock Partially Reserved", "Closed"). Las reservas de stock aparecen como estado, no solo como campo.
- Segundo sistema abierto, con el texto de ayuda del propio código (6.3 [L]): estados "Draft", "Confirmed", "In Progress", "To Close", "Done", "Cancelled", con esta ayuda: "Draft: The MO is not confirmed yet."; "Confirmed: The MO is confirmed, the stock rules and the reordering of the components are trigerred."; "In Progress: The production has started (on the MO or on the WO)."; "To Close: The production is done, the MO has to be closed."; "Done: The MO is closed, the stock moves are posted."; "Cancelled: The MO has been cancelled, can't be confirmed anymore." Además un segundo campo independiente de disponibilidad de material: "Waiting", "Ready", "Waiting Another Operation" (con ayuda: "Ready: The material is available to start the production. Waiting: The material is not available to start the production.").
- Observación mía: en el primero, "Closed" y "Completed" son distintos; en el segundo, "To Close" es "producción terminada, falta cerrar" y "Done" es "cerrada, movimientos de stock registrados". Ambos separan terminar de cerrar y ambos tienen un estado de "detenida" (el primero) o de "disponibilidad de material" aparte (el segundo). Coinciden en: borrador, en curso, terminada, cerrada (el cierre contable/de stock), cancelada. No es un estándar: son dos decisiones de diseño. Sigue sin haber fuente primaria para planificada/firme/liberada (APICS Dictionary).
- Texto de la documentación (6.1 [L]): "When you stop a Work Order its status is changed to Stopped indicating that all production process against that Work Order has stopped." y "You can also re-open the stopped Work Order." Estados por operación: "Whether the Operation is Pending, Work In Progress, or Completed."

### Orden discreta, repetitiva y por procesos

- Sin definición seria hallada. Lo que hay: ISA, sobre ISA-88 (6.4 [L]): "The ISA-88 series of standards, also known as batch process control standards, bring clarity, structure and consistency to batch processing in pharmaceuticals, food and beverage industries, chemicals and other batch processing industries." y la Parte 1 "establishes a consistent set of models and terminology used in batch control systems." (la página la describe como "technology-agnostic"). Partes: 88.00.01-2010 modelos y terminología; 88.00.02-2001 estructuras de datos; 88.00.03-2003 recetas generales y de sitio; 88.00.04-2006 registros de producción por lotes. La página da el alcance, no las definiciones de receta, lote ni orden: hay que comprar la norma.
- Un resumen de buscador sobre documentación de sistemas propietarios (no leída) dice que el trabajo discreto es una orden de una cantidad de un artículo con fecha de terminación, el repetitivo es producción continua de una mezcla en una línea y el de procesos se basa en recetas y fórmulas. No lo cito: son vocabularios de proveedores, y SAP usa "orden de proceso" frente a "orden de producción" como convención propia. Hueco.

### Consumo automático (backflush)

- Glosario IISE Z94.14 (6.5 [S]): "BACK FLUSH. A method of recording issues from inventory by exploding the bill of material for the next higher assembly" (el lector truncó la frase). Coincide con la definición de la APICS Dictionary, 8.ª ed., citada en la ronda 1: "The deduction from inventory records of the component parts used in an assembly or subassembly ... by exploding the bill of materials by the production count of assemblies produced." Dos glosarios que dicen lo mismo, pero no son independientes (el de IISE hereda la tradición de APICS); cuento una sola línea.
- Práctica (6.1 [L]): "Backflush Raw Materials From Work-in-Progress Warehouse: Ticking this checkbox will automatically create a Stock Entry with the type 'Manufacture'. This means that the raw materials were consumed from the Source Warehouse, used to manufacture finished goods and another Stock Entry was created for your Target Warehouse." Y: "Skip Material Transfer to WIP Warehouse: Usually, a Stock Entry is created when the raw materials are transferred to a Work In Progress Warehouse. In this case, the raw material is considered to be consumed hence the Stock Entry is skipped." Campos por componente: "Required Quantity" ("calculated automatically based on the Bill Of Materials"), "Transferred Quantity" y "Consumed Quantity". También la devolución: "Return Components" crea el movimiento de vuelta, y se pueden transferir cantidades extra a partir de un porcentaje configurable ("Transfer Extra Raw Materials to WIP (%)").

### Qué registra un sistema

Estado de la orden (con el cierre separado de la terminación), estado de disponibilidad de material, cantidad requerida / transferida / consumida / devuelta por componente, modo de consumo (manual o backflush), operaciones con su estado y almacenes de origen, en proceso, destino y chatarra. Evidencia: 6.1, 6.2, 6.3.

### Recurso canónico propuesto

La documentación y el modelo de estados de los dos sistemas abiertos (6.1 a 6.3) como evidencia de datos; APICS Dictionary vigente para backflush y los tipos de orden (no leída); ISA-88.00.01 para el modelo de batch (de pago). Fijarse en que el estado "cerrada" es una decisión distinta de "terminada": al cerrar se congela la orden para costos y stock.

---

## 7. Subproducto y coproducto

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 7.1 | IAS 2 Inventories, versión consolidada de la Comisión Europea (Reglamento 1126/2008, al 16-09-2009) | https://moodle2.units.it/pluginfile.php/305507/mod_resource/content/1/ias2_en%20%282%29.pdf | primaria (texto oficial de la UE; copia en un sitio universitario) | [L] | 3 | 2 | 2 | 3 |
| 7.2 | NIC 2 Existencias, en el Reglamento (CE) n.º 1126/2008 de la Comisión, Diario Oficial de la UE L 320, 29.11.2008 (copia en el BOE, serie DOUE) | https://www.boe.es/doue/2008/320/L00001-00481.pdf | primaria (texto oficial) | [L] | 3 | 2 | 2 | 3 |
| 7.3 | Glosario IISE Z94.14 | https://www.iise.org/Details.aspx?id=2402 | secundaria | [S] | 2 | 1 | 1 | 2 |

7.1 y 7.2 son el mismo texto de la norma en dos idiomas: cuentan como una sola fuente. Que el reglamento de la UE sea el texto aplicable a la UE y no a la Argentina es una salvedad (la Argentina adopta las NIIF por la Resolución Técnica 26 de la FACPCE, que no leí). Para el aspecto de dinero hay una sola fuente con dos idiomas; la norma oficial del IASB en ifrs.org no la leí (hay una página con el HTML de la norma que el buscador mostró, pero el párrafo 14 no apareció en el texto devuelto).

### Afirmaciones

- Definición, en inglés (7.1 [L]), párrafo 14 de la NIC 2: "A production process may result in more than one product being produced simultaneously. This is the case, for example, when joint products are produced or when there is a main product and a by-product. When the costs of conversion of each product are not separately identifiable, they are allocated between the products on a rational and consistent basis. The allocation may be based, for example, on the relative sales value of each product either at the stage in the production process when the products become separately identifiable, or at the completion of production. Most by-products, by their nature, are immaterial. When this is the case, they are often measured at net realisable value and this value is deducted from the cost of the main product. As a result, the carrying amount of the main product is not materially different from its cost."
- La misma en español (7.2 [L], párrafo 14): "El proceso de producción puede dar lugar a la fabricación simultánea de más de un producto. Es el caso, por ejemplo, de la producción conjunta o de la producción de productos principales junto a subproductos. Cuando los costes de transformación de cada tipo de producto no sean identificables por separado, se distribuirá el coste total entre los productos, utilizando bases uniformes y racionales. La distribución puede basarse, por ejemplo, en el valor de mercado de cada producto, ya sea como producción en curso, en el momento en que los productos comienzan a poder identificarse por separado, o cuando se complete el proceso productivo. La mayoría de los subproductos, por su propia naturaleza, no poseen un valor significativo. Cuando este sea el caso, se medirán frecuentemente por su valor realizable neto, deduciendo esa cantidad del coste del producto principal. Como resultado de esta distribución, el importe en libros del producto principal no resultará significativamente diferente de su coste."
- La norma habla de "joint products" (productos conjuntos) y de "main product" más "by-product"; no define "coproducto" como término. El tratamiento contable (reparto del costo conjunto por valor de venta relativo; subproducto a valor neto realizable y restado del costo del principal) es de la norma; la definición de cada concepto es la del párrafo, que los distingue por ejemplo y no por una fórmula.
- Discrepancia con el glosario IISE (7.3 [S]): "BY-PRODUCT. A material of value produced as residual of or incidental to the production process." con "Syn: co-product." (sin entrada propia de coproducto). Es decir, IISE usa "coproducto" como sinónimo de subproducto, mientras que la NIC 2 distingue productos conjuntos (de valor comparable) de producto principal más subproducto. Dar las dos definiciones; en el tema conviene fijar que "coproducto" no tiene un sentido único en las fuentes.
- No hallé la entrada de coproducto en la APICS Dictionary.

### Qué registra un sistema

Por orden: productos obtenidos de una misma producción (el principal y los demás), con cantidad y destino de cada uno, y el valor o costo asignado (frontera con Costos-de-produccion: allá se decide la base de reparto). La ronda 1 vio que el primer sistema abierto trata la chatarra con un almacén aparte ("If the BOM results in Scrap material, the Scrap Warehouse needs to be selected.", 6.1 [L]); en esta ronda no busqué si ese sistema tiene un concepto nativo de subproducto o coproducto en la lista de materiales.

### Recurso canónico propuesto

NIC 2, párrafos 14 y 15 (el 14 se leyó entero; el 15 no), en el texto oficial. Fijarse en que el reparto se hace solo si los costos de transformación no son identificables por separado y en que el subproducto inmaterial se mide a valor neto realizable.

---

## 8. Huecos que quedan

1. Textos que no abrieron: TOCICO Dictionary (la URL de PDF probada dio 404 y la búsqueda no devolvió entradas), Rahman (1998) IJOPM (paywall), Sugimori et al. (1977) IJPR (403, sin abstract), Muchiri y Pintelon (2008) IJPR (403). Nakajima (1988), Goldratt y Cox (1984), Goldratt y Fox (1986), Hopp y Spearman, Pinedo, Monden, Smith (1956) y Jackson (1955) tampoco: todo lo que se les atribuye viene de un texto que los cita.
2. La fórmula literal del OEE en ISO 22400-2 (cláusula 6) y sus términos de disponibilidad, efectividad y calidad: la vista previa pública solo trae los términos de tiempo (PBT, APT, etc.). Hay que comprar la norma.
3. APICS/ASCM Dictionary: sin entradas leídas para orden discreta, repetitiva y por procesos, orden planificada, firme y liberada, backflush vigente, kanban, coproducto, hacia adelante y hacia atrás, razón crítica. Todo lo que reemplaza esto son apuntes o glosarios secundarios.
4. Orden discreta, repetitiva y por procesos: sin definición seria abierta. Solo el alcance de ISA-88 y vocabularios de proveedores.
5. Razón crítica: definida en apuntes de un curso, sin resultado de optimalidad; FCFS sin definición formal.
6. Programación hacia adelante y hacia atrás: Wikipedia (definición) y un glosario IISE (hacia atrás) únicamente; sin libro ni norma.
7. Carga finita: sigue siendo la sola cita de ISA-95.00.03.
8. El 85 % del OEE: no verificado contra Nakajima; el artículo académico lo atribuye a Jonsson y Lesshammar (1999) como "nivel de clase mundial" y a Nakajima solo las condiciones 90/95/99. El texto de ese artículo lo leí a través de un lector que resume ([S]); las citas no están contrastadas contra el original.
9. Dos sistemas abiertos para los estados de la orden, ambos leídos en código y ayuda; el manual de uno de ellos devolvió 404. Falta un tercer sistema y la APICS Dictionary para sostener que el patrón (terminar distinto de cerrar) es general.
10. Subproducto y coproducto: una sola fuente seria (la NIC 2, con dos idiomas) y es de contabilidad, no de producción; sin la Resolución Técnica argentina. El glosario IISE discrepa en el uso de "coproducto".
11. Kanban: sin el texto primario de las reglas (Sugimori et al., 1977; Ohno; Monden). Las reglas son las de la filial británica de Toyota; la página global no habla de kanban.
12. Los términos de la ley de Little con condiciones de largo plazo (estacionariedad, ergodicidad) no los verifiqué en un texto primario; Little (2011) cubre la versión de intervalo finito.
