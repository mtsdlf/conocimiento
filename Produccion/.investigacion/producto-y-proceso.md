# Producción — ángulo Producto y proceso (datos maestros de fabricación)

Fecha de la investigación: 2026-11-27. Alcance: lista de materiales (BOM), ruta de fabricación y centro de trabajo, cambios de ingeniería. Las pruebas de sistemas se anotan como "un sistema abierto" o "un sistema comercial" y se deja la URL. Marcas: [L] leí el texto de la página, [M] metadatos o índice, [S] resumen secundario o del buscador. Puntaje de 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

Aviso de método: no pude acceder al texto literal del APICS/ASCM Dictionary, ni a Orlicky ni a Vollmann (de pago o sin copia pública verificable). Las definiciones "APICS" llegan por terceros y se marcan [S]. Ver sección de huecos.

---

## 0. Cómo encaja la división del árbol con el campo

La división (BOM / ruta y centro de trabajo / cambios de ingeniería) coincide con cómo los sistemas parten los datos maestros de fabricación. Dos observaciones:

1. En los sistemas la BOM y la ruta suelen colgar de la misma cabecera. En un sistema abierto la operación pertenece a una sola BOM; en otro la ruta es una plantilla que se aplica a la BOM. Conviene decir en la nota de ruta que "la ruta puede ser un maestro aparte o parte de la BOM", y que es decisión de diseño, no del dominio.
2. En producción de procesos (química, alimentos) el campo no separa BOM y ruta: usa fórmula o receta (ISA-88), que junta insumos, parámetros, equipos y procedimiento. Ahí la división del árbol se queda corta; conviene una sección o nota propia de fórmula/receta.

Los cambios de ingeniería vienen de otra disciplina (gestión de la configuración, ISO 10007), no de la planificación. La norma es una guía de calidad; la disposición del stock y de las órdenes abiertas sólo la encontré explícita en la práctica de los sistemas, no en la norma (de la norma sólo leí el índice).

---

## 1. Lista de materiales (BOM)

### 1.1 Fuentes

| # | Fuente | Tipo | URL | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 1 | Documentación de BOM de un sistema abierto (v18.0) | primaria (de sistema) | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/manufacturing/basic_setup/bill_configuration.html | [L] | 2/2/2/2 |
| 2 | Manual de BOM de otro sistema abierto | primaria (de sistema) | https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials | [L] | 2/3/2/2 |
| 3 | Documentación de BOM y fórmulas de un sistema comercial (página con fecha 2025-07-10) | primaria (de sistema) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom | [L] | 2/3/2/3 |
| 4 | Glosario de un sistema comercial: lista fantasma ("Paraphrased from the APICS Dictionary, Eighth Edition") | secundaria del APICS Dictionary | https://docs.infor.com/csi/9.01.x/en-us/csbiolh/lsm1454143871331.html | [L] | 1/1/1/1 |
| 5 | Manual de BOM de otro sistema comercial (fantasma, modelo / clase de opción) | primaria (de sistema) | https://docs.oracle.com/cd/A60725_05/html/comnls/us/bom/bomov02.htm | [L] | 2/1/1/1 |
| 6 | Artículo IISE Magazine (terminología IISE de "phantom assembly") | secundaria | https://www.iise.org/iemagazine/2021-03/html/sanchez/sanchez.html | [L] | 1/1/1/1 |
| 7 | Ayuda de un sistema comercial: código de nivel más bajo | primaria (de sistema) | https://docs.infor.com/csb/9.01.x/en-us/csbiolh/mergedprojects/sl_invprod/fields/l/low_level_code_item_master_general.htm | [S] | 1/1/1/1 |
| 8 | Ayuda de otro sistema comercial: código de nivel más bajo | primaria (de sistema) | https://docs.oracle.com/en/applications/jd-edwards/supply-chain-manufacturing/9.2/eoarp/low-level-code.html | [S] | 1/1/1/1 |

Las fuentes 4, 5, 7 y 8 son documentación de proveedores: muestran que los sistemas implementan el vocabulario del campo, no son evidencia independiente del campo.

### 1.2 Afirmaciones

**Qué es una BOM y sus niveles**
- "A bill of materials (BOM) defines the components that are required in order to produce a product. The components can be raw materials, semi-finished products, or ingredients." (fuente 3)
- "A single BOM describes a single level that is identified by a unique ID. Components might have their own BOMs that are referenced by BOM versions." El multinivel es una cadena de BOM de un nivel. (fuente 3)
- En un sistema abierto: "each item (sub-assembly) could have its own BOM", formando un árbol de BOM anidadas. Cada fila guarda cantidad, operación, BOM de subensamble por defecto, almacén de origen y porcentaje de merma. (fuente 2)

**Cantidad por unidad y base de la BOM**
- "Quantity: Enter the quantity of the Item that will be manufactured from this Bill of Materials." La BOM tiene una cantidad base de producto, y las cantidades de componentes se refieren a ella. (fuente 2)

**Merma y rendimiento**
- Merma de componente: porcentaje por fila ("scrap percentage"). (fuente 2)
- Pérdida de proceso: si el ítem de merma es el mismo que el producido, pasa a ser "Process Loss Item" y su cantidad se resta de la salida. (fuente 2)
- En un sistema comercial las versiones de fórmula tienen "yield, co-product and by-product definitions, and the cost distribution instructions for the formula." (fuente 3)
- Son dos conceptos: merma del componente (se consume más de lo que entra al producto) y rendimiento de la salida (sale menos de lo teórico). Los sistemas los guardan por separado. Hueco: no tengo la definición literal del APICS Dictionary de "yield" ni "scrap factor".

**Lista fantasma**
- Parafraseado del APICS Dictionary (8.ª edición, según el sitio): subensamble que se fabrica sólo para entrar en otro ensamble, agrupa componentes bajo un número de ítem, se construye físicamente pero no se almacena, y MRP traspasa los requerimientos a sus componentes. Sinónimos: blow-through, transient bill of material, pseudo bill of material. Único literal: "Paraphrased from the APICS Dictionary, Eighth Edition". (fuente 4) [S]
- Terminología IISE: "A bill of material coding and structuring technique used primarily for transient (non-stocked) sub-assemblies." Sinónimos: "phantom bill of material, blow through". (fuente 6)
- "A phantom assembly is a non-stocked assembly that lets you group together material needed to produce a subassembly." Y: "As a subassembly, however, they lose their identity as distinct assemblies and are a collection of their components." (fuente 5)
- En un sistema abierto: una BOM fantasma "produces no item and only groups raw materials" y se explota sola dentro de otras BOM (paráfrasis de la página); además hay un indicador por fila "Do Not Explode". (fuente 2)
- Advertencia de práctica: "Extensive use of phantom BOMs in many levels has an effect on performance... you should avoid deep hierarchies of phantoms. Instead, use pre-exploded production BOMs and routes." (fuente 3)
- Matiz entre fuentes: la fuente 3 dice que el fantasma también funde sus operaciones en la ruta del padre ("the operations of that route are merged into the parent route"); las demás sólo hablan de materiales. No afirmar como universal.

**Lista de planificación, modular, variantes**
- "Planning BOM – Used to do planning for material requirements. The demand of components and ingredients is calculated based on the demand of the finished products." (fuente 3)
- Cuando un modelo o clase de opción es componente de otra lista, "the component supply type is phantom." (fuente 5)
- Variantes en un sistema abierto: "When the field is left blank, the component is used in all product variants." Lo mismo para operaciones. Una BOM con renglones aplicables a variantes, en lugar de una BOM por variante. (fuente 1)
- En un sistema comercial la versión se acota: "The validity of BOM versions and formula versions can be constrained by period, quantity, site, specific product dimensions, and other criteria." (fuente 3)
- Hueco: no encontré definición literal de planning bill, modular bill, super bill ni de BOM configurable en una fuente del campo.

**Lista de ingeniería frente a lista de fabricación**
- Un sistema comercial distingue cinco tipos: borrador, ingeniería, planificación, producción y costeo. "Engineering BOMs are structured to simplify the design process and group complex products into engineering modules... the engineering BOM must be converted to an actual production BOM." Y: "In simple implementations, a planning BOM, production BOM, and costing BOM can be modeled as one BOM." (fuente 3)
- Discrepancia: los dos sistemas abiertos leídos manejan una BOM con un tipo (fabricar / kit) y no separan ingeniería de producción en el maestro (fuentes 1 y 2). La separación aparece donde hay gestión de cambios o PLM.

**Subproductos y coproductos**
- Un sistema abierto: "a residual product that is created during production in addition to the main product of a BoM". Campos: producto, cantidad, unidad y operación donde se produce (opcional). Ejemplo: el subproducto "Mush" sale de "Grind grapes" al producir vino tinto. (fuente 1)
- Un sistema comercial: la fórmula (subtipo de BOM para procesos) "describes co-products and by-products". (fuente 3)
- Otro sistema abierto tenía una tabla de "Scrap Items" y la reemplazó por "Secondary Items" en su versión 16. (fuente 2)
- Hueco: no obtuve la distinción literal APICS coproducto / subproducto; sólo la práctica de sistemas. No afirmar diferencias de costeo sin fuente.

**Código de nivel más bajo**
- "Low Level Coding: The lowest position in which a material can appear in a BOM (bill of material). This represents the sequence in which items are run through MRP." (fuente 7, [S])
- "Each item has a low-level code that represents the lowest level at which the item appears in all current, job, and production schedule bills of material (BOMs)." (fuente 8, [S])
- "A low-level code of 0 indicates that the item is an end item (finished good) and is not a subcomponent of another item." (fuente 8, [S])
- Sirve para netear un componente una sola vez aunque aparezca en varios niveles. Es cálculo de MRP (frontera con Planificación), pero el dato se deriva de la BOM.
- Hueco: la definición de Orlicky y la del APICS Dictionary no se obtuvieron.

### 1.3 Recurso canónico propuesto

- APICS/ASCM Dictionary, entradas "bill of material", "phantom bill of material", "low-level code", "yield", "co-product", "by-product". No lo pude leer; hay que consultarlo con acceso.
- Vollmann, Berry, Whybark y Jacobs, *Manufacturing Planning and Control for Supply Chain Management*, capítulos de datos maestros. No pude acceder; leerlo antes de cerrar definiciones.
- Lo mejor leído: la fuente 3, que separa tipos de BOM, versiones, aprobación y activación. Fijarse en los cinco tipos de BOM, las versiones acotadas por período y cantidad, y los tipos de línea (ítem, fantasma, suministro anclado, proveedor).

### 1.4 Qué registra un sistema (mínimo)

- Cabecera: ítem producido, cantidad base y unidad, estado (borrador, enviada, cancelada), activa sí/no, por defecto sí/no, fantasma sí/no, tipo (fabricar / kit), versión y vigencia (desde-hasta, a veces por cantidad o sitio). Fuentes 1, 2 y 3.
- Renglón: componente, cantidad, unidad, % de merma, tipo de línea, operación en que se consume, "no explotar", aplicabilidad a variantes, BOM de subensamble por defecto, almacén de origen. Fuentes 1, 2 y 3.
- Salidas adicionales: subproductos y coproductos (ítem, cantidad, unidad, operación), pérdida de proceso. Fuentes 1, 2 y 3.
- Derivados: lista explotada ("Materials Required (Exploded)", fuente 2), código de nivel más bajo (fuentes 7 y 8), costo de la BOM (fuentes 2 y 3).

---

## 2. Ruta de fabricación y centro de trabajo

### 2.1 Fuentes

| # | Fuente | Tipo | URL | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 9 | Manual de ruta de un sistema abierto | primaria (de sistema) | https://docs.frappe.io/erpnext/user/manual/en/routing | [L] | 2/2/1/2 |
| 10 | Manual de estación de trabajo del mismo sistema abierto | primaria (de sistema) | https://docs.frappe.io/erpnext/user/manual/en/workstation | [L] | 2/2/1/2 |
| 11 | Centros de trabajo de otro sistema abierto (v18.0) | primaria (de sistema) | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/manufacturing/advanced_configuration/using_work_centers.html | [L] (primeros 100000 caracteres) | 2/3/2/2 |
| 12 | OEE en ese sistema abierto (para la frontera) | primaria (de sistema) | https://www.odoo.com/documentation/master/applications/inventory_and_mrp/manufacturing/reporting/oee.html | [S] | 2/1/1/1 |
| 13 | Guía de lead time de un sistema comercial (cola, preparación, movimiento) | primaria (de sistema) | https://docs.oracle.com/cd/E26228_01/doc.93/e21779/ap_ld_tms.htm | [S] | 1/2/1/1 |
| 14 | Mismo sistema, "Understanding Lead Time" | primaria (de sistema) | https://docs.oracle.com/en/applications/jd-edwards/supply-chain-manufacturing/9.2/eoapd/understanding-lead-time.html | [L] | 1/1/1/1 |
| 15 | Campos de tiempos de operación de otro sistema comercial | primaria (de sistema) | https://docs.infor.com/ln/2022.x/en-us/lnolh/cpordplanug/cpomlt000130.html | [S] | 1/1/1/1 |
| 16 | Presentación de entrenamiento que atribuye a APICS capacidad nominal, utilización y eficiencia | secundaria, dudosa | https://www.scribd.com/document/578912928/05-BSCM-v4-1-PPT | [S] | 1/1/1/1 |
| 17 | Wiki comunitaria de un sistema abierto (rutas y tareas como "work effort") | secundaria (comunidad) | https://cwiki.apache.org/confluence/spaces/OFBENDUSER/pages/349637112/A+practical+guide+to+setup+Routing+in+Apache+OFBiz+for+Manufactures+in+4+easy+Steps. | [S] | 1/1/2/1 |
| 18 | ISA-88 en Wikipedia | secundaria | https://en.wikipedia.org/wiki/ISA-88 | [S] | 1/2/1/1 |
| 19 | "Recipe Management with ISA-S88", Control Engineering | secundaria | https://www.controleng.com/recipe-management-with-isa-s88/ | [S] | 1/2/1/1 |

### 2.2 Afirmaciones

**Ruta y operaciones**
- Un sistema abierto: la ruta "stores all Operations along with the description, hourly rate, operation time, batch size, etc." Cada fila tiene operación y estación por defecto; tiempo "in minutes"; "Batch Size" es la cantidad de unidades procesadas en esa operación; el costo se calcula "based on the Hourly Rate and the Operation Time". (fuente 9)
- Secuencia: un "Sequence ID" obliga a completar las operaciones en orden; "An Operation cannot be completed before its precedents, or the system throws a validation error." (fuente 9, parafraseado de la página)
- Otro sistema abierto: operación con centro de trabajo, duración medida o manual, hoja de trabajo y aplicabilidad a variantes. "Each operation is unique, as it is always exclusively linked to one BoM." (fuente 1)
- Discrepancia de diseño: en el primero la ruta es una plantilla que se aplica a la BOM (fuentes 2 y 9); en el segundo la operación pertenece a una sola BOM (fuente 1). El dominio sólo exige una secuencia de operaciones con recurso y tiempo.

**Tiempos: preparación, ejecución, cola, movimiento**
- Cola: "The number of hours that a job waits at a work center before setup or work is performed on it." Preparación: "The number of hours required to prepare machinery to run a specific item, regardless of quantity." Movimiento: "The hours a work order is in transit from the completion of one operation to the beginning of the next." (fuente 13, [S]; literales del resumen del buscador, no leí la página)
- Ejecución por unidad: "The sum of the run times, as defined by the prime load codes for the work centers, factored by the routing time basis and converted to the lead time per unit." (fuente 14)
- Lead time de fabricación: "The total number of workdays required to complete a product, from its lowest-level components to the final item, assuming that all purchased items are in-house." (fuente 14)
- Las entradas del cálculo son "Routing labor, setup, queue, move, and machine run hours". (fuente 14)
- Otro sistema comercial lista cola, espera y movimiento como campos de la operación, sin definir "espera" (fuente 15, [S]). Que "espera" y "cola" sean casi sinónimos es inferencia del buscador, no una definición.
- Un sistema abierto registra "Setup Time" ("the time required before work can commence on a work order") y "Cleanup Time" ("breakdown or cleanup time required after a work order is finished") en el centro de trabajo. (fuente 11)
- Observación: los dos sistemas abiertos leídos (fuentes 9 y 11) no tienen cola, espera ni movimiento como campos de operación, aunque son los tiempos que la teoría considera dominantes del lead time. No encontré una fuente leída que sostenga esa afirmación de la teoría; no la hago.

**Centro de trabajo, capacidad, calendario**
- Un sistema abierto: horas de trabajo con inicio y fin, turnos, lista de feriados para que no cuenten como días de trabajo; "Production Capacity is the total number of jobs can be executed at the same time in the respective workstation." Al programar una orden, el sistema chequea la disponibilidad contra esas horas. (fuente 10)
- Otro sistema abierto: "Working Hours: the hours that work center can be used during the week"; "Capacity: the number of products that can be processed at the work center simultaneously"; "Time Efficiency: a multiplier for how using this work center affects the normal speed of execution of a work order"; "OEE Target: the target for efficiency at the work center"; "Cost per hour: the operating expense of that workstation"; "Alternative Workcenters: where a work order should be carried out if this work center is not available". (fuente 11)
- Dos sentidos de capacidad: en los sistemas abiertos es paralelismo (cuántos trabajos a la vez, fuentes 10 y 11); en la planificación de capacidad se mide en horas por período. La capacidad en horas se deriva de calendario, eficiencia y utilización.
- Capacidad nominal: "available time × utilization × efficiency", con utilización ("hours actually worked over available hours") y eficiencia ("standard hours produced over hours actually worked"). Sólo me llegó por una presentación que dice basarse en APICS (fuente 16, [S], baja confianza); verificar contra el diccionario antes de publicar.
- El término "eficiencia" tiene dos usos: en la fuente 11 es un multiplicador de velocidad frente al tiempo de la BOM (en la versión 16 de esa documentación, según el buscador, 200 % divide a la mitad el tiempo, [S]); en la definición APICS atribuida es horas estándar producidas sobre horas trabajadas. Cuidar el glosario.

**Fórmula y receta (procesos)**
- ISA-88: una receta contiene "a header, a formula, equipment requirements, a procedure, and other batch processing support information"; la fórmula incluye insumos, parámetros y salidas, no sólo proporciones. Tipos: receta general (independiente de equipo y sitio), maestra (con capacidades de equipo) y de control (copia de un lote, con identificación de lote y de material). (fuentes 18 y 19, [S])
- En un sistema comercial la fórmula es "a subtype of BOM that is typically used for process manufacturing", con coproductos, subproductos y rendimiento por versión. (fuente 3)
- Correspondencia propuesta (inferencia mía, ninguna fuente la hace): fórmula ≈ BOM más parámetros; procedimiento ≈ ruta, pero jerárquico y consciente del equipo; los requisitos de equipo no tienen equivalente directo en una ruta.

### 2.3 Recurso canónico propuesto

- ISA-95 / IEC 62264 (modelo de recursos y definiciones de producción; lo cubre Fundamentos) e ISA-88 / IEC 61512 (recetas). Textos oficiales de pago; sólo tengo [S].
- Vollmann et al. (datos maestros y capacidad) y Hopp y Spearman, *Factory Physics* (tiempo de ciclo, cola y utilización). No los leí. Fijarse en cómo definen el tiempo de ciclo y qué parte es cola.
- Evidencia de datos: fuente 11 (centro de trabajo) y fuente 9 (ruta).

### 2.4 Qué registra un sistema (mínimo)

- Operación: secuencia, descripción, centro de trabajo, tiempo de preparación, tiempo de ejecución por unidad o lote, tamaño de lote de la operación, a veces cola, espera y movimiento, materiales que consume y subproductos que genera, instrucciones. Fuentes 1, 9, 11 y 15.
- Centro de trabajo: calendario y horas, feriados, capacidad, eficiencia, meta de OEE, costo por hora (con componentes como electricidad, alquiler, consumibles y sueldos), preparación y limpieza, centros alternativos. Fuentes 10 y 11.
- Los estados de ejecución (orden, tarjeta de trabajo) son de Ejecución-en-planta.

---

## 3. Cambios de ingeniería

### 3.1 Fuentes

| # | Fuente | Tipo | URL | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 20 | ISO 10007:2017, vista previa (índice, prólogo, introducción) | primaria | https://cdn.standards.iteh.ai/samples/70400/c1702ad12e3e4fe99ce2f15a60fe9ad7/ISO-10007-2017.pdf | [M] (el cuerpo es de pago) | 3/1/1/3 |
| 21 | ISO 10007:2017, páginas oficiales | primaria (metadatos) | https://www.iso.org/standard/70400.html y https://committee.iso.org/sites/tc176/home/projects/published/iso-10007-2017.html | [S] | 3/1/1/1 |
| 22 | Manual de ECO de un sistema comercial (estados, vigencia, disposición) | primaria (de sistema) | https://docs.oracle.com/cd/E18727_01/doc.121/e13687/T269960T269964.htm | [L] | 2/3/2/3 |
| 23 | ECO de un sistema abierto (etapas, aprobadores, versiones) | primaria (de sistema) | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/plm/manage_changes/engineering_change_orders.html | [L] (100000 de 101268 caracteres) | 2/2/2/2 |
| 24 | Aprobación y activación de versiones de BOM en un sistema comercial | primaria (de sistema) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom | [L] | (misma fuente 3) |
| 25 | Wikipedia, "Engineering change order" | secundaria | https://en.wikipedia.org/wiki/Engineering_change_order | [L] | 1/1/1/1 |
| 26 | Fecha de uso agotado ("use-up") en un sistema comercial | primaria (de sistema) | https://docs.oracle.com/en/cloud/saas/readiness/scm/24b/plm24b/24B-plm-wn-f32012.htm | [S] | 1/1/1/2 |

### 3.2 Afirmaciones

**Control de cambios en la norma**
- "This third edition cancels and replaces the second edition (ISO 10007:2003), which has been technically revised. This edition aligns ISO 10007 with ISO 9000:2015 and ISO 9001:2015." (fuente 20)
- "Configuration management is a management activity that applies technical and administrative direction over the life cycle of a product and service, its configuration identification and status, and related product and service configuration information." (fuente 20)
- "Configuration management can be used to meet the product and service identification and traceability requirements specified in ISO 9001:2015, 8.5.2." (fuente 20)
- El índice muestra la estructura: 4.2 "Dispositioning authority"; 5.3 identificación (estructura del producto, información de configuración, líneas base); 5.4 control de cambios, con 5.4.2 "Initiation, identification and documentation of the need for change", 5.4.3 "Evaluation of change", 5.4.4 "Disposition of change", 5.4.5 "Implementation and verification of change"; 5.5 contabilidad de estado; 5.6 auditoría. (fuente 20)
- Según el buscador, la edición 2017 fue "last reviewed and confirmed in 2023" y hay un borrador de cuarta edición (fuente 21, [S]). Verificar en la página oficial.
- No leí el cuerpo (definiciones de línea base, solicitud de cambio, requisitos de disposición). No lo cito.

**ECR, ECO, ECN**
- Wikipedia: la ECO es un "document approved by the design activity that describes and authorizes the implementation of an engineering change" (la página no define ECR y avisa que le faltan citas). Contenido mínimo: identificación de la pieza, motivos, descripción antes y después, documentos y áreas afectados, aprobación e instrucciones de oportunidad (por ejemplo, desechar de inmediato el stock actual o esperar a la próxima corrida). Sinónimos: ECN, EC, ERN. (fuente 25, baja confianza)
- Hueco: sin fuente primaria para la distinción ECR (solicitud, antes de decidir) frente a ECO (orden, ya autorizada). En los sistemas leídos la solicitud no aparece como objeto aparte: una sola ECO con etapas (fuente 23) o con estado y estado de aprobación (fuente 22).

**Revisión, versión y vigencia**
- Un sistema abierto: al iniciar la revisión se copia la BOM de producción con "The next available version number" (V2, V3); mientras la ECO está abierta "the changes stay in the revised BoM and do not affect the production BoM"; al aplicar, la BOM de producción original se archiva y la revisada pasa a ser la nueva. (fuente 23)
- Vigencia en ese sistema: "As soon as possible" o una fecha específica. (fuente 23)
- Un sistema comercial: "You should assign an effective date and model / unit number for each revised item on an ECO."; también una "early effective date that determines the earliest date that you can manually implement a change"; "Rescheduling does not change the ECO or revised item status, only the dates." (fuente 22)
- Una ECO agrupa ítems revisados "logically related to each other, such as a new product introduction", y cada ítem revisado puede tener varios componentes revisados. "Revised items can be either items or bills." (fuente 22)
- Otro sistema comercial verifica que no haya dos versiones activas en conflicto: "You receive an error message if the version that you're trying to activate conflicts with a version that is already active." Permite aprobar y activar las BOM de un cambio "for one activation date". (fuente 24)
- Vigencia por agotamiento: hay sistemas que calculan la fecha de vigencia de un componente reemplazado a partir de cuándo se agota el stock proyectado ("Calculate Use-Up Date"). (fuente 26, [S])

**Disposición del stock y de las órdenes abiertas**
- Opciones de disposición del ítem revisado en un sistema comercial (fuente 22): por defecto "No change required"; "Scrap the revised item in WIP and inventory when you implement the revised item" (también sólo inventario o sólo WIP); retrabajo en WIP e inventario, sólo inventario o sólo WIP; "Use the revised item until you exhaust WIP and inventory for the item" (también sólo WIP); "Use the revised item until it reaches a particular serial number".
- Es decir, se decide por ítem revisado y por lugar (inventario o producción en proceso), con cuatro acciones: sin cambio, desechar, retrabajar, agotar. Una sola fuente de sistema para esta tabla.
- Wikipedia coincide en la forma: la ECO trae instrucciones de oportunidad sobre el stock (fuente 25, baja confianza).
- Hueco: la regla sobre las órdenes de producción ya liberadas (terminar con la versión vieja, reabrirlas, re-explotarlas) no está en ninguna fuente primaria que haya leído.

**Quién aprueba**
- Sistema abierto: las etapas de verificación son "stages that require approval before the revised changes can be applied to the production BoM"; los aprobadores deben aceptar antes de habilitarse "Apply Changes". (fuente 23)
- Sistema comercial: estados de aprobación "Not Submitted for Approval", "Approval Requested", "Approved", "Rejected"; "Engineering does not let you set the ECO Status field to Implemented or Scheduled if the approval status has not been set to Approved." (fuente 22)
- Otro sistema comercial: "Before a BOM version can be used in the planning or manufacturing process, it must be approved." (fuente 24)
- En la norma "Dispositioning authority" (4.2) y "Disposition of change" (5.4.4) son cláusulas; sólo conozco los títulos (fuente 20). Wikipedia: aprueban "only those individuals that are authorized", normalmente especialistas de su área con "a final overall approval from management" (fuente 25, baja confianza).
- Ninguna fuente leída exige una junta de control de cambios; no lo afirmo.

**Estados**
- Sistema comercial, ECO: Open ("The ECO is not complete; you can still make changes"), Hold ("The ECO cannot be implemented"), Release, Schedule, Implement ("You can no longer make changes to an implemented ECO"), Cancel ("All unimplemented revised items are cancelled"). Ítem revisado: Open, Schedule, Implement. (fuente 22)
- Sistema abierto: la ECO sigue las etapas de su tipo; al aplicar pasa a una etapa de cierre. (fuente 23)

### 3.3 Recurso canónico propuesto

- ISO 10007:2017, cláusulas 4.2, 5.3 y 5.4. Es de pago; el índice y la introducción se verifican en la vista previa. Alguien con acceso debe leer 5.4 antes de citar requisitos.
- Para el modelo de datos: la fuente 22 (estados, vigencia, disposición) y la fuente 23 (flujo con aprobadores y versiones).
- Fijarse en: qué se hace con el stock y el trabajo en proceso cuando el cambio entra en vigor, y la vigencia por fecha o por número de serie.

### 3.4 Qué registra un sistema (mínimo)

- ECO: identificador, motivo, ítems afectados y cambio (antes y después), estado (abierto, en espera, liberado, programado, implementado, cancelado), estado de aprobación y aprobadores, vigencia (fecha, "lo antes posible" o número de serie o de modelo), disposición del stock y del WIP por ítem, documentos afectados. Fuentes 22, 23 y 25.
- Resultado en el maestro: nueva versión de BOM y ruta con vigencia, la anterior archivada, y una sola versión activa por período, sitio y cantidad. Fuentes 23 y 24.

---

## 4. Huecos

1. APICS/ASCM Dictionary: ninguna entrada leída en texto literal (BOM, phantom, low-level code, yield, scrap, co-product, by-product, rated capacity, utilization, efficiency, queue, setup, effectivity, engineering change). Todo lo "APICS" es [S].
2. Orlicky, Vollmann, Hopp y Spearman: sin acceso. Lo de tiempos y capacidad viene de documentación de sistemas, que usa el vocabulario del campo pero no es la fuente original.
3. ISO 10007:2017: sólo índice, prólogo e introducción. Sin 5.4 ni 4.2 ni definiciones. La norma no define ECR/ECO.
4. ECR frente a ECO, y órdenes abiertas ante un cambio: sin fuente primaria. La tabla de disposición es de una sola fuente de sistema comercial.
5. Subproducto frente a coproducto: sin definición del campo.
6. Lista de planificación, modular, super bill y configurables: sin fuente del campo.
7. Cola, espera y movimiento: definiciones sólo [S] del buscador; sin fuente para la afirmación clásica de que la cola domina el tiempo de ciclo.
8. ISA-88, ISA-95, IEC 61512, IEC 62264: sólo resúmenes secundarios.
9. Un sistema abierto de ERP libre (OFBiz): la wiki oficial pedía acceso y sólo vi resultados del buscador; no confirmé campos de BOM ni ruta. Sin afirmaciones.
10. Evidencia empírica o casos de cambios de ingeniería y su costo: no busqué.
11. Evidencia en contra (críticas de la BOM multinivel, rutas fijas frente a flexibles): no la busqué; corresponde a Fundamentos.
12. Normativa argentina (IRAM; ANMAT en alimentos y medicamentos para fórmula maestra y registros de lote): no cubierto desde este ángulo, no verificado.

### Fronteras con los vecinos

- Código de nivel más bajo, explosión, desfase: MRP, de Planificación-de-la-produccion; aquí sólo el dato derivado de la BOM.
- Costo estándar por lista y ruta: Costos-de-produccion; aquí sólo los datos que lo habilitan (costo por hora, tiempos).
- OEE como medida: Ejecucion-en-planta; el centro de trabajo sólo guarda eficiencia y meta.
- Disposición del stock en el depósito: Inventario y depósitos; aquí sólo la decisión de qué hacer con él.
- Disposición de no conformidad y CAPA: Calidad; una ECO puede nacer de una acción correctiva.
