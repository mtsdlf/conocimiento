# Ejecución en planta: informe de investigación

Alcance: orden de producción, consumo y declaración, programación de planta, subcontratación (fasón), OEE y la relación ERP/MES (ISA-95). Fecha de la búsqueda: 2026-11-27.

Aviso sobre las marcas. Las páginas web las leí con una herramienta que devuelve un resumen del texto, no el texto crudo. Por eso esas páginas están marcadas [S]. [L] solo se usa para el PDF de vista previa de ISA-95.00.03 (texto extraído con pdftotext; es un extracto de la norma, no la norma completa) y para unos apuntes de clase de Columbia (texto extraído). Las citas literales están entre comillas, en el idioma original, tal como las devolvió la herramienta; ninguna fue contrastada contra el original.

Huecos graves (detalle al final): no pude leer Factory Physics, The Goal, Pinedo, Nakajima ni la APICS Dictionary. Las reglas de despacho y el DBR están respaldados solo con fuentes secundarias. Los estados "planificada / firme / liberada" son vocabulario de la APICS sin texto primario a mano.

---

## 1. Orden de producción

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Documentación de Work Order de un sistema abierto | https://docs.frappe.io/erpnext/user/manual/en/work-order | primaria (práctica de sistemas) | [S] | 2 | 3 | 2 | 3 |
| 1.2 | Documentación de Job Card de un sistema abierto | https://docs.frappe.io/erpnext/user/manual/en/job-card | primaria (práctica) | [S] | 2 | 2 | 2 | 3 |
| 1.3 | Código del modelo de orden de fabricación de un sistema abierto (v18), visto en un resumen del buscador | https://sources.debian.org/data/main/o/odoo/18.0.0%2Bdfsg-2/addons/mrp/models/mrp_production.py | primaria (código) | [S] | 2 | 2 | 1 | 3 |
| 1.4 | ISA-95.00.03-2013, vista previa (terminología "Job Order") | https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf | primaria | [L] (extracto) | 3 | 1 | 1 | 2 |

### Afirmaciones

- Estados de la orden en un sistema abierto (v18), según el resumen del código (1.3 [S]): seis estados, "Draft, Confirmed, In Progress, To Close, Done, and Cancelled". Confirmed dispara las reglas de stock y el reabastecimiento de componentes; In Progress, la producción empezó en la orden o en una operación; To Close, la producción terminó y falta cerrar a mano; Done, cerrada. Conviene leer el campo de estado del modelo para citarlo directo.
- Otro sistema abierto (1.1 [S]) no lista estados de la orden; solo "Stopped" (botón Stop; hay que devolver antes el material del almacén en proceso y se puede reabrir) y estados por operación: "Pending, Work In Progress, or Completed".
- Qué hace ese sistema al emitir la orden (1.1 [S]): "Raw materials are reserved in the source warehouses", las operaciones se programan "after the planned start date based on workstation availability" y se crean tarjetas de trabajo en borrador. "Warehouses are mandatory for submitting a Work Order": origen, en proceso (WIP), destino y chatarra.
- Al iniciar y terminar (1.1 [S]): el material pasa al almacén en proceso con un movimiento "Material Transfer for Manufacture"; al terminar, otro movimiento descuenta del almacén en proceso y suma al de terminados; se puede terminar una cantidad parcial.
- Terminología ISA-95 (1.4 [L]): la edición 2013 cambió nombres: "Detailed Production Schedule changed to Work Schedule", "Production Dispatch List changed to Job list", "Production Work Order changed to Job Order". Para ISA-95, lo que la planta ejecuta es una "Job Order".
- Estados "planificada, firme, liberada, en curso, terminada, cerrada": no los encontré en una fuente primaria legible. Planificada/firme es la distinción de MRP, y la APICS Dictionary la define, pero no pude leerla. Hueco: no los presento como estándar.
- Qué se verifica al liberar (material y capacidad): el sistema de 1.1 reserva material al emitir y programa contra la disponibilidad del centro de trabajo; el de 1.3 dispara el reabastecimiento al confirmar. Un botón "Check availability" aparece en un resumen de buscador sobre la documentación de un sistema abierto (no la leí). Evidencia débil.
- Documentos que acompañan: la tarjeta de trabajo "stores actual production information about a particular Operation performed on a particular Workstation"; el flujo es "Move Materials > Start Job > Complete Job > Submit" (1.2 [S]). Es evidencia de una hoja por operación con tiempos, cantidad y empleado.
- Orden discreta frente a repetitiva y por procesos: sin fuente. Solo sé, por 1.4 [L], que ISA-95.00.03 referencia a ISA-88 ("ANSI/ISA-88.00.01-2010, Batch Control") entre sus normas; ahí vive la receta. Hueco.

### Qué registra un sistema (mínimo)

Producto y cantidad a fabricar; lista de materiales y ruta usadas (versión); fechas de inicio y entrega planificadas; estado; almacenes de origen, en proceso, destino y chatarra; material requerido, transferido y consumido por componente; por operación: centro de trabajo, cantidad completada, tiempo real, estado; vínculo con el pedido de venta o proyecto de origen. Evidencia: 1.1, 1.2 (un sistema abierto).

### Recurso canónico propuesto

APICS/ASCM Dictionary para el vocabulario de estados (entradas de orden planificada, firme y liberada), más Vollmann et al., Manufacturing Planning and Control, capítulo de control de la actividad de planta. Ninguno leído. Como evidencia de datos, la documentación de la orden y la tarjeta de trabajo de un sistema abierto (1.1, 1.2).

---

## 2. Consumo de materiales y declaración de producción

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 2.1 | Glosario de un sistema que cita la APICS Dictionary, 8ª ed., entrada "backflush" | https://erp.smcusa.com/SyteLine/Language/en-US/mergedProjects/sl_main/other/glossary/def_backflush.htm | secundaria (cita primaria) | [S] | 2 | 1 | 1 | 1 |
| 2.2 | Work Order de un sistema abierto (igual que 1.1) | https://docs.frappe.io/erpnext/user/manual/en/work-order | primaria (práctica) | [S] | 2 | 3 | 2 | 3 |
| 2.3 | Job Card de un sistema abierto (igual que 1.2) | https://docs.frappe.io/erpnext/user/manual/en/job-card | primaria (práctica) | [S] | 2 | 2 | 2 | 3 |

### Afirmaciones

- Backflush, atribuido a la APICS Dictionary, 8ª edición: "The deduction from inventory records of the component parts used in an assembly or subassembly" "by exploding the bill of materials by the production count of assemblies produced." (2.1 [S]). Cita secundaria de una edición vieja; la vigente no la leí.
- Un sistema abierto (2.2 [S]) ofrece dos modos: transferir el material a un almacén en proceso y consumir desde ahí, o marcar "Backflush Raw Materials From Work-in-Progress Warehouse", que crea un movimiento de tipo 'Manufacture' que "consumes raw materials, produces finished goods". También permite saltear la transferencia ("Skip Material Transfer"): "Finish" crea el movimiento de fabricación directo. La página no dice sobre qué cantidad se hace el backflush.
- Chatarra: "If the BOM results in Scrap material, the Scrap Warehouse needs to be selected." (2.2 [S]). No explica la valuación.
- Merma de proceso: "Process Loss Qty will be calculated only when the Pending Qty is zero, indicating that the operation is fully completed"; ejemplo: 10 a fabricar, 6 completadas, 0 pendientes, "the remaining 4 become process loss" (2.3 [S]). Es decisión de ese sistema, no estándar.
- Subproducto y coproducto: sin fuente legible. Hueco.
- Frontera con stock: en 2.2 el consumo y el ingreso del terminado son movimientos de stock (del dominio de Inventario); Producción decide cuánto y desde/hacia dónde. Es observación mía, no cita.

### Qué registra un sistema (mínimo)

Por componente: cantidad requerida, transferida, consumida y devuelta; modo de consumo (manual o backflush); cantidad producida buena, rechazada/chatarra y merma, con su almacén; lote o serie del terminado cuando corresponda (frontera con Calidad e Inventario); fecha y quién declaró. Evidencia: 2.2, 2.3.

### Recurso canónico propuesto

La entrada "backflush" de la APICS Dictionary vigente para la definición, y Vollmann et al. para cuándo conviene y su riesgo (exige lista de materiales exacta; esa advertencia salió de un sitio contable secundario, accountingtools.com, no leído entero).

---

## 3. Programación de planta

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Journal of Business Inquiry (UVU), artículo que cita a Pinedo sobre SPT/EDD | https://journals.uvu.edu/index.php/jbi/article/download/88/68 | secundaria | [S] | 1 | 1 | 1 | 1 |
| 3.2 | Apuntes de Gallego (Columbia), sobre Factory Physics | https://www.columbia.edu/~gmg2/4000/pdfold/throughput.pdf | secundaria | [L] | 2 | 2 | 3 | 2 |
| 3.3 | Wikipedia, Little's law | https://en.wikipedia.org/wiki/Little%27s_law | secundaria | [S] | 1 | 2 | 1 | 1 |
| 3.4 | Wikipedia, Theory of constraints | https://en.wikipedia.org/wiki/Theory_of_constraints | secundaria | [S] | 1 | 2 | 1 | 1 |
| 3.5 | Wikipedia, Heijunka | https://en.wikipedia.org/wiki/Heijunka | secundaria | [S] | 1 | 1 | 2 | 1 |
| 3.6 | Toyota, Production system | https://global.toyota/en/company/vision-and-philosophy/production-system/ | primaria | [S] | 3 | 1 | 1 | 2 |
| 3.7 | ISA-95.00.03-2013, vista previa | https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf | primaria | [L] (extracto) | 3 | 1 | 1 | 2 |
| 3.8 | Entrevista a Spearman (Lean Blog) | https://www.leanblog.org/2007/05/leanblog-podcast-25-mark-spearman/ | secundaria | [S] | 1 | 1 | 1 | 1 |
| 3.9 | arXiv, Elements of Scheduling (resultado de búsqueda sobre Smith 1956 / Jackson 1955) | https://arxiv.org/pdf/2001.06005 | secundaria | [M] | 2 | 2 | 1 | 1 |

### Afirmaciones

- Reglas de despacho: según 3.1 [S], "SPT provides the optimal sequence with regard to the flow time criterion" y EDD con el criterio de "longest delay" (máximo atraso), citando a Pinedo; SPT y EDD "generate better sequences than FCFS, CR, and SS" (según el resumen). FCFS es la línea de base. Razón crítica: tiempo hasta la entrega sobre tiempo de proceso, menor primero, según resúmenes de buscador y sin resultado de optimalidad. Los resultados clásicos (Smith 1956, SPT; Jackson 1955, EDD; una máquina) los vi atribuidos solo en resúmenes de buscador (3.9 [M]); uno de ellos pone una condición sobre preemption para EDD que no pude aclarar. No leí a Smith, Jackson ni Pinedo.
- Programación hacia adelante y hacia atrás: sin fuente legible. Hueco.
- Carga finita: "finite capacity scheduling: scheduling methodology where work is scheduled for a set of manufacturing resources, in such a way that no capacity scheduled exceeds the capacity available" (3.7 [L]). Cita más sólida de este componente.
- Ley de Little: "the long-term average number of customers (L) in a stationary system is equal to" la tasa media de llegada efectiva "times the average time a customer spends in the system", L = λW; "Little published in 1961 his proof of the law"; "The only requirement is that the system be ergodic." (3.3 [S]). En manufactura se escribe WIP = TH x CT y se llama "Little's Law" (3.2 [L]). No pude abrir el artículo original (Operations Research, 1961).
- Factory Physics, vía apuntes (3.2 [L]): "The bottleneck rate rb is the rate of the process center having least long-term capacity"; "Critical WIP is defined to be Wo = rb To", con To el tiempo de proceso crudo; ejemplo: "To = 8 so the bottleneck rate is half a unit per hour and the raw processing time is eight hours. Finally, critical WIP is Wo = rb To = 0.5 * 8 = 4". Subir la tasa del cuello mejora tiempo de ciclo y throughput "on WIP levels above Wo". Es un resumen de clase, no el libro. Spearman, en una entrevista: "every line has a Critical WIP level" (3.8 [S]).
- TOC: Goldratt la presenta "in his 1984 book titled The Goal"; "A constraint is anything that prevents the system from achieving its goal"; cinco pasos: identificar, decidir cómo explotar, "Subordinate everything else to the above decision.", elevar, y volver al paso 1 (3.4 [S]). DBR se describe como "a manufacturing execution methodology" (3.4 [S]). Tambor = el cuello marca el ritmo; amortiguador = reserva de trabajo o tiempo delante del cuello; cuerda = señal que libera material al ritmo del tambor. Esa definición viene de un resumen de buscador sobre material secundario (PMI, un capítulo de Taylor & Francis), sin leer la página. Fuentes discrepan sobre el origen del DBR: una enciclopedia lo atribuye a The Race, un capítulo dice que Goldratt y Fox lo describieron en detalle, y un trabajo de PMI dice que The Goal fijó el marco sin los detalles de aplicación. Críticas: "D. Trietsch ... argues that DBR methodology is inferior to competing methodologies" y "Gupta and Snyder (2009) argue that TOC has yet failed to demonstrate its effectiveness in the academic literature" (3.4 [S]).
- Kanban y nivelación: Toyota describe el JIT como "making only what is needed, when it is needed, and in the amount needed" y jidoka como "automation with a human touch" (3.6 [S]); esa página no menciona kanban ni heijunka. Heijunka: "for reducing the mura (unevenness) which in turn reduces muda (waste)"; ejemplo: demanda entre "800 and 1,200 units", producir al promedio de largo plazo y absorber con inventario; mezcla de modelos en lotes lo más chicos posible (3.5 [S]); cita a Ohno, Toyota Production System, p. 126, y a Womack, Jones y Roos. Kanban como mecanismo (tarjeta, cantidad máxima): sin fuente. Hueco.
- Cumplimiento del programa: sin fuente. Hueco.

### Qué registra un sistema (mínimo)

Por operación programada: centro de trabajo, inicio y fin planificados, secuencia o prioridad, estado, tiempos reales. Evidencia de un sistema abierto: programa las operaciones "after the planned start date based on workstation availability" con una ventana de programación configurable (1.1 [S]). Para el cumplimiento: fecha prometida frente a fecha real de terminación, por orden (propuesta mía, sin evidencia).

### Recurso canónico propuesto

Hopp y Spearman, Factory Physics, capítulo 7 (leyes básicas: Little, mejor caso, WIP crítico; la sección de mejor caso fue señalada por un resumen de buscador, sin verificar); Pinedo, Scheduling: Theory, Algorithms, and Systems, capítulos de una máquina; Goldratt, The Goal, y Goldratt y Fox, The Race, para DBR. Fijarse en el WIP crítico y en cómo la variabilidad obliga a tener más. Ninguno leído.

### Nota sobre el árbol

El campo separa "programación" (scheduling, teoría de una máquina y de taller) de "control de la actividad de planta" (despacho, seguimiento). El árbol las junta en Ejecución en planta; sirve, pero la teoría de secuenciación pesa más que lo que un sistema registra.

---

## 4. Subcontratación (fasón)

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 4.1 | Subcontracting de un sistema abierto | https://docs.frappe.io/erpnext/user/manual/en/subcontracting | primaria (práctica) | [S] | 2 | 3 | 2 | 3 |

### Afirmaciones

- Flujo en un sistema abierto (4.1 [S]): orden de compra subcontratada, donde "The Rate on the Items row is the agreed service cost"; orden de subcontratación con las materias primas a proveer calculadas desde la lista de materiales; movimiento "Material to Supplier" que mueve el material "from your warehouse to the Supplier's warehouse"; recepción de subcontratación, que consume el material en el almacén del proveedor ("a backflush") e ingresa el terminado al almacén aceptado, con chatarra opcional; y recepción de compra sin efecto de stock, porque la recepción de subcontratación ya actualizó stock y contabilidad.
- Qué se registra (4.1 [S]): costo del servicio, materiales provistos, reservados y consumidos, base del backflush (lista de materiales o lo realmente transferido), chatarra y su tasa, cuenta de gasto del servicio, factor de conversión.
- Una sola fuente, de un sistema abierto. Sin fuente teórica (APICS, Vollmann). Sin práctica argentina (remito, IVA): corresponde a la nota de Producción en la Argentina. Hueco.

### Qué registra un sistema (mínimo)

Proveedor y servicio contratado con su tarifa; material enviado (cantidad, fecha, documento), consumido y devuelto; producto recibido (aceptado y rechazado, fecha); saldo de material en poder del tercero; vínculo con la orden de compra. Evidencia: 4.1.

### Recurso canónico propuesto

La documentación de subcontratación de un sistema abierto, como evidencia de datos solamente. Para la teoría, el capítulo de Vollmann et al. sobre operaciones externas (no verificado).

---

## 5. Eficiencia global del equipo (OEE)

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 5.1 | Nakajima, Introduction to TPM: Total Productive Maintenance, Productivity Press, 1988 (ISBN 978-0-915299-23-2) | referenciado en https://en.wikipedia.org/wiki/Overall_equipment_effectiveness | primaria, no leída | solo referencia | 3 | 3 | 2 | 3 |
| 5.2 | oee.com, Calculating OEE | https://www.oee.com/calculating-oee/ | secundaria (sitio de proveedor) | [S] | 1 | 2 | 3 | 1 |
| 5.3 | oee.com, Six Big Losses | https://www.oee.com/oee-six-big-losses/ | secundaria (idem) | [S] | 1 | 2 | 2 | 1 |
| 5.4 | oee.com, World-Class OEE | https://www.oee.com/world-class-oee/ | secundaria (idem) | [S] | 1 | 2 | 1 | 2 |
| 5.5 | oee.com, TEEP | https://www.oee.com/teep/ | secundaria (idem) | [S] | 1 | 2 | 3 | 1 |
| 5.6 | Wikipedia, Overall equipment effectiveness | https://en.wikipedia.org/wiki/Overall_equipment_effectiveness | secundaria | [S] | 1 | 3 | 2 | 1 |
| 5.7 | Tractian y Fluke (resultados de búsqueda) | https://tractian.com/en/blog/world-class-oee ; https://www.fluke.com/ja-jp/learn/blog/predictive-maintenance/oee | secundaria (proveedores) | [M] | 1 | 1 | 1 | 1 |

oee.com, Tractian, Fluke y similares son sitios de proveedores y repiten la misma tradición sobre el 85 %: cuentan como una sola fuente para esa cifra, salvo donde discrepan.

### Afirmaciones

- Definición: OEE es "a measure of how well a manufacturing equipment is utilized compared to its full potential" (5.6 [S]). OEE = Disponibilidad x Rendimiento x Calidad.
- Fórmulas literales (5.2 [S]): "Availability = Run Time / Planned Production Time"; "Performance = (Ideal Cycle Time × Total Count) / Run Time"; "Quality = Good Count / Total Count"; "Ideal Cycle Time is the fastest cycle time that your process can achieve in optimal circumstances."
- Ejemplo numérico literal de oee.com (5.2 [S]): Planned Production Time 480 − 60 = 420 minutos; Run Time 420 − 47 = 373 minutos; Good Count 19,271 − 423 = 18,848; Availability 373 / 420 = 88.81 %; Performance (1.0 s × 19,271) / (373 × 60 s) = 86.11 %; Quality 18,848 / 19,271 = 97.80 %; OEE 0.8881 × 0.8611 × 0.9780 = 74.79 %. Verifiqué la cuenta: cierra.
- Ejemplo de Wikipedia (5.6 [S]): turno de 480 min, pausa de 30, parada de 60, quedan 390 min operando, 81.25 %; 242 unidades a 1.5 min = 363 min, 363 / 390 = 93.1 %; 242 producidas, 21 defectuosas, 221 buenas, 91.32 %; "Combined: 86.6% × 93% × 91.3% = 73.6%". Inconsistente: la disponibilidad se calcula como 81.25 % pero el combinado usa 86.6 % (que es 390/450). Con 81.25 % el producto da cerca de 69 % (cálculo mío). No recomiendo este ejemplo.
- Seis grandes pérdidas (5.3 [S]): Equipment Failure (disponibilidad: roturas de herramental, paradas no planificadas, falta de operarios o materiales, "starved or blocked"); Setup and Adjustments (disponibilidad: cambios de formato, ajustes, limpieza, calentamiento); Idling and Minor Stops (rendimiento); Reduced Speed (rendimiento); Process Defects (calidad); Reduced Yield (calidad: desperdicio al arranque). Wikipedia (5.6) usa una tabla más simple con otros nombres (Waiting, Breakdowns / Minor Stops, Reduced Speed / Scrap, Rework). Dos nomenclaturas; el original de Nakajima no lo leí.
- Origen y "clase mundial 85 %": "It is often thought that a World-Class OEE score is 85%"; "Seiichi Nakajima led the introduction of TPM, OEE and the Six Big Losses in the early 1970s"; "In his 1984 book, Introduction to TPM (translated to English and published in 1988 by Productivity Press)"; "Seiichi defined these numbers, based on his practical experience, as minimums for which companies should strive"; sus componentes son "90% Availability, 95% Performance, and 99% Quality"; los números "have roots in a particular place (Japan), at a particular time (1970s), and in a particular industry (automotive)"; "There is no one ideal OEE score or OEE industry standard to use as a benchmark for every company." (5.4 [S]). Discrepa Tractian (5.7 [M]): 90 / 95 / 99.9 % (da 85.4 %); Fluke: cada factor cerca de 95 %. Wikipedia: "To assume that 85% OEE is a 'world Class' target value is in many cases incorrect." y no da el origen (5.6 [S]). Un resumen de buscador sobre una página de Proficy dice 85 % para continuos y 80 % para batch ([M]). 0.90 × 0.95 × 0.99 = 84.6 %, que redondea a 85 % (cálculo mío). También discrepan en el año del libro: 1984 (oee.com) frente a 1988 (la edición en inglés, referencia de Wikipedia). La atribución a Nakajima es de segunda mano.
- TEEP: "TEEP = OEE × Utilization"; "Utilization = Planned Production Time / All Time"; "TEEP is the ratio of Fully Productive Time to All Time"; ejemplo: OEE 65 %, 80 horas programadas de 168, utilización 47.62 %, TEEP 30.95 % (5.5 [S]; cuenta verificada). Wikipedia lo llama "Loading" y lo define sobre horas calendario (5.6 [S]).
- Cómo se engaña (5.6 [S]): "Although tempting, OEE (as a number) is NOT suitable for comparing machines or benchmarking."; "OEE cannot be used to measure employee performance."; "OEE has properties of a geometric mean. As such it punishes variability among its subcomponents."; además menciona incentivos a falsear los números, terminología inconsistente y que asume un sistema cerrado y estático. Por construcción (lectura mía de las fórmulas, no cita): si el tiempo ideal de ciclo se fija flojo, el rendimiento sube; si las paradas planificadas se sacan del tiempo planificado, sube la disponibilidad (en el ejemplo de oee.com ya se descuentan 60 min de pausa).
- Frontera con Activos y mantenimiento: la disponibilidad como factor está allá (tema ya escrito); acá el OEE es la medida de la línea.

### Qué registra un sistema (mínimo)

Por equipo y turno: tiempo planificado, tiempos de parada con su causa (idealmente un código de las pérdidas), unidades totales y buenas, tiempo ideal de ciclo por producto. No hallé evidencia de OEE nativo en un sistema abierto; la tarjeta de trabajo (1.2) guarda tiempos y cantidad completada, que son la materia prima pero no el OEE.

### Recurso canónico propuesto

Nakajima, Introduction to TPM (1988), parte sobre efectividad del equipo y las seis pérdidas (no leído). Mientras tanto, oee.com para fórmula y ejemplo, con la salvedad de que es un sitio de proveedor. Fijarse en dos decisiones que cambian el número: qué entra en el tiempo planificado y cuál es el tiempo ideal de ciclo.

---

## 6. Relación ERP / MES según ISA-95

### Fuentes

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| 6.1 | ISA-95.00.03-2013, vista previa en PDF | https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf | primaria | [L] (extracto) | 3 | 2 | 1 | 3 |
| 6.2 | Página de ISA sobre el comité ISA-95 | https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa95 | primaria | [S] | 3 | 1 | 1 | 2 |
| 6.3 | Wikipedia, ANSI/ISA-95 | https://en.wikipedia.org/wiki/ANSI/ISA-95 | secundaria | [S] | 1 | 2 | 1 | 1 |
| 6.4 | Presentación de consultora (BR&L) sobre ISA-95 Part 1, citada por el buscador | https://fr.slideshare.net/florentflo2/t061isa9504pdf | secundaria | [M] | 1 | 1 | 1 | 1 |

### Afirmaciones

- Alcance: "This Part 3 standard shows activity models and data flows for manufacturing information that enables enterprise-control system integration. The modelled activities operate between Level 4 logistics and planning functions and Level 2 manual and automated process control functions." y "The goal of the standard is to reduce the risks, costs and errors associated with implementing enterprise systems and manufacturing operations systems in such a way that they inter-operate and easily integrate." (6.1 [L]). La parte cubre "a model of the activities associated with manufacturing operations management, Level 3 functions" y "an identification of some of the data exchanged between Level 3 activities." (6.1 [L]).
- Niveles: nivel 4 = "business planning and logistics functions"; nivel 2 = funciones de control de proceso; nivel 3 = manufacturing operations and control (6.1 [L]). La página de ISA (6.2 [S]) dice que "The interface initially considered is the interface between levels 3 and 4" del modelo Purdue y que el estándar define "electronic information exchange between the manufacturing control functions and other enterprise functions".
- Partes (6.3 [S]): 1 modelos y terminología; 2 atributos del modelo de objetos; 3 modelos de actividades de la gestión de operaciones de manufactura (nivel 3); 4 objetos y atributos; 5 transacciones de negocio a manufactura. Wikipedia dice que 4 y 5 estaban "in development" pero lista ediciones 2018 de ambas: la página es inconsistente.
- Qué se intercambia (orden, programa, consumo, declaración): lo respaldado por la norma (6.1 [L]) son los nombres de los objetos de 2013: Work Schedule, Job List, Job Order. La división "programa de producción (qué hacer y usar) y definición de producto hacia abajo; desempeño de producción (qué se hizo y usó) y capacidad hacia arriba" viene de una presentación de consultora (6.4 [M]); no la leí. B2MML como formato XML de esos mensajes: según resúmenes de buscador de una patente y de un blog de proveedor; no verificado. El contenido exacto de "production schedule" y "production performance" está en las partes 2 y 4, que no leí. Hueco.
- Reparto de tareas ERP y MES, según una patente que cita el estándar (resumen del buscador, baja confianza): en el nivel 3 el MES hace "Dispatching Production, Detailed Production Scheduling, Reliability Assurance"; en el nivel 4 el ERP hace "Plant Production Scheduling and Operational Management". Sostiene la separación del árbol entre planificar (ERP, otro ángulo) y ejecutar (MES), pero depende de la edición.

### Qué registra un sistema (mínimo)

El MES recibe la orden con su programa y la definición de producto, y devuelve desempeño: qué se produjo, qué se consumió, cuándo y con qué recursos. Sin MES, el ERP registra las mismas declaraciones directamente (1.1, 2.2). Esa equivalencia es observación mía.

### Recurso canónico propuesto

ANSI/ISA-95.00.03-2013 (e IEC 62264-3), modelos de actividad de nivel 3, más la Parte 2 para los atributos de los objetos. La vista previa pública solo trae introducción, alcance y cambios de nombres. Para un mapa de las partes, Wikipedia (6.3), confirmando contra ISA. Hay que pagar la norma para citar las tablas de objetos.

### Nota sobre el árbol

ISA-95 divide por niveles (4 planificación, 3 operaciones, 2 control). Ejecución en planta es nivel 3 y coincide, siempre que la planificación (MPS, MRP) se marque como nivel 4. ISA-95 tiene su lugar como marco en Fundamentos.

---

## 7. Huecos

1. No pude leer Factory Physics (Hopp y Spearman), The Goal ni The Race (Goldratt), Pinedo, Nakajima ni Vollmann et al. Todo lo atribuido a ellos viene de apuntes, Wikipedia o resúmenes de buscador.
2. Sin texto de la APICS/ASCM Dictionary: ni orden planificada, firme y liberada, ni la edición vigente de "backflush" (la definición citada es de la 8ª edición, de segunda mano).
3. Estados de la orden: solo dos sistemas abiertos, uno con la lista obtenida de un resumen del código. "Planificada, firme, liberada, en curso, terminada, cerrada" sin fuente primaria.
4. Orden discreta frente a repetitiva y por procesos (receta): sin fuente; solo la referencia de ISA-95 a ISA-88.
5. Subproducto y coproducto, rechazo y merma como conceptos generales: sin fuente fuera de la documentación de un sistema abierto.
6. Programación hacia adelante y hacia atrás, fórmula de la razón crítica y kanban como mecanismo: sin fuente primaria. Dos sitios de cursos (ecampusontario, uky.edu) dieron 403 o no los leí.
7. Cumplimiento del programa y su medición: sin fuente.
8. Contenido de los objetos de ISA-95 (production schedule, production performance): solo vista previa; qué fluye en cada sentido descansa en una presentación de consultora no leída.
9. Origen del 85 % de OEE: no verificado en Nakajima. Discrepancias: calidad 99 % (oee.com) frente a 99.9 % (Tractian); año del libro 1984 frente a 1988.
10. Little 1961 (Operations Research): el artículo no abrió (JSTOR); la cita sale de Wikipedia.
11. Subcontratación: una sola fuente (un sistema abierto); sin práctica argentina.
12. Kanban y heijunka: la página de Toyota no los trata; solo Wikipedia (heijunka) y Ohno/Womack de segunda mano.
13. El manual de Odoo (v18, orden de fabricación) devolvió 404; los estados vienen del código indexado, no de su manual. Las URL de docs.frappe.io responden y los redirects desde docs.erpnext.com apuntan allí.
