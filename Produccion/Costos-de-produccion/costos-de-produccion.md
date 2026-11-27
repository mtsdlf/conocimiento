---
resumen: >-
  Costos de producción es la parte que dice cuánto cuesta lo fabricado: el costo estándar de cada producto, que sale de la lista de materiales y la ruta, el costo real que junta cada orden con los consumos y las horas de la planta, y las variaciones entre los dos. El método de costeo y el registro en los libros son de Contabilidad; acá, de dónde salen los datos.
estado: vigente
estabilidad: estable
fuentes:
  - "Resolución Técnica 17 FACPCE, texto ordenado de junio de 2003 (Consejo Profesional de CABA), sección 4.2.6 «Bienes producidos» (leída en el texto): https://www.consejo.org.ar/storage/attachments/RT_FACPCE17_TO2003.pdf-bGCewZIHs8.pdf"
  - "Resolución Técnica 54 FACPCE, Norma Unificada Argentina de Contabilidad, T.O. RT 59 y modificatorias, párrafos 104 a 110, 114 y 290 a 295 (leída en el texto publicado por el Consejo Profesional de CABA, no en la FACPCE): https://consejo.org.ar/storage/attachments/Resolucion%20Tecnica%20N%2054%20(TO%20RT%2059%20y%20modi-7TbUsld18i.pdf"
  - "Consejo Profesional de CABA, Resolución P. 460/2024 (11 de julio de 2024), que adopta la RT 59 y fija la vigencia (leída): https://www.consejo.org.ar/storage/attachments/P.460-2024-RT.%20Nro.%2059.pdf-jUINVCulEQ.pdf"
  - "Gisela Bertolino, Bienes de cambio y costo de ventas en la RT 54, La Ley (de 2022, leída; alojada por el consejo de Salta): https://www.consejosalta.org.ar/wp-content/uploads/Bienes-de-cambio-y-costo-de-ventas.-Analisis-de-los-cambios-a-su-tratamiento-contable-en-el-marco-de-la-nueva-RT-54.pdf"
  - "IFRS Foundation, NIC 2 Inventarios, párrafos 12 a 14 y 21 (según el extractor, con citas acortadas): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html"
  - "Dummies, Cost Accounting: Job Costs for Spoilage, Reworked Products, and Scrap (secundaria, según el resumen): https://www.dummies.com/article/business-careers-money/business/accounting/general-accounting/cost-accounting-job-costs-for-spoilage-reworked-products-and-scrap-164765"
  - "Iowa State (ISUDP), curso de contabilidad de gestión (según el resumen del buscador; la página no abrió): https://iastate.pressbooks.pub/isudp-2025-202/?p=23"
  - "Documentación de un sistema abierto, Bill of Materials (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials"
  - "Documentación de un sistema abierto, Work Order (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/work-order"
  - "Documentación de un sistema comercial, Bills of Material: Cost Calculation (según el resumen): https://help.myob.com.au/advanced/Docs/Published/UserGuide/BOM_Cost_Calculation.html"
  - "Produccion/.investigacion/costos.md (secciones 1, 4, 5 y 6), 2026-11-27"
  - "Produccion/.investigacion/costos-2.md (RT 54 y RT 59), 2026-11-27"
aliases: [costos de producción, costo de producción, costo de fabricación, manufacturing cost, production cost, costo industrial, merma normal, merma anormal, normal spoilage, abnormal spoilage, rechazo, reproceso, retrabajo, rework, desecho, scrap, ociosidad, capacidad ociosa, idle capacity]
creado: 2026-11-27
revisado: 2026-11-27
---

# Costos de producción

Costos de producción es la parte que dice cuánto cuesta lo fabricado: el costo estándar de cada producto, que sale de la lista de materiales y la ruta, el costo real que junta cada orden con los consumos y las horas de la planta, y las variaciones entre los dos. El método de costeo y el registro en los libros son de Contabilidad; acá, de dónde salen los datos.

Es la cuarta de las cinco partes de [Producción](../produccion.md). Recibe de [Producto y proceso](../Producto-y-proceso/producto-y-proceso.md) la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) y la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md), que son la base del costo estándar. Recibe de [Ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md) lo que pasó en cada [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md): los consumos, las horas y lo declarado como bueno o rechazado. Le entrega a [Contabilidad](../../Contabilidad/contabilidad.md) el costo de cada orden para que lo registre.

## Los datos de la planta que alimentan el costo

El costo de un producto fabricado es la suma de cantidades por precios, y casi todas las cantidades salen de la planta. Un sistema abierto calcula el costo de la lista «from the Valuation Rate of the raw materials/sub-assemblies involved and the Operation costs» (según el resumen).

| Dato | De dónde sale | Qué pone en el costo |
|---|---|---|
| Lista de materiales | [Producto y proceso](../Producto-y-proceso/lista-de-materiales.md) | la cantidad de cada componente por unidad, con su porcentaje de merma: el material estándar |
| Ruta de fabricación | [Producto y proceso](../Producto-y-proceso/ruta-de-fabricacion.md) | las operaciones, el centro de trabajo de cada una, el tiempo de preparación, el de ejecución y el tamaño de lote: las horas estándar |
| Tasa del centro de trabajo | la ruta, con el valor que fija Contabilidad | cuánto cuesta una hora de máquina, de mano de obra y de carga fabril en ese centro: pasa las horas a pesos |
| Costo unitario de lo comprado | la valuación del inventario, en Contabilidad | el precio de cada componente que no se fabrica |
| Consumos | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md) | el material real de cada orden |
| Horas | los partes de horas por operación | la mano de obra y la carga fabril reales de cada orden |
| Declaraciones | [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md) | cuántas unidades salieron buenas y cuántas rechazadas: entre cuántas se divide el costo y contra qué se miden las variaciones |

Las primeras cuatro filas arman el [costo estándar del producto](costo-estandar-del-producto.md): lo que debería costar, calculado nivel por nivel. Las últimas tres arman el [costo real de la orden](costo-real-de-la-orden.md): lo que costó. Un error en la lista o en la ruta pasa al costo de cada orden y aparece como una variación que nadie causó en la planta (inferencia de la base). En papel alcanzan la ficha técnica del producto, una hoja de costos por orden y una planilla de horas.

## Dónde corta con Contabilidad

Producción guarda cantidades y las cuenta por orden; Contabilidad decide cómo se valúan y se registran.

| Acá, en Producción | Allá, en Contabilidad |
|---|---|
| El costo estándar de cada producto, por la lista y la ruta | Qué [sistema de costeo](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md) se usa: órdenes o procesos, absorción o variable, real o estándar, ABC |
| El costo real de cada orden y su saldo mientras está abierta | El asiento que lo registra y el [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md) cuando se vende |
| Las variaciones de cada orden y su causa en la planta | El análisis de desvíos en general, en [presupuesto](../../Contabilidad/Contabilidad-de-gestion/presupuesto.md) |
| La tasa por hora de cada centro de trabajo, como dato de la ruta | Qué es fijo, variable, directo o indirecto, en [clasificación de costos](../../Contabilidad/Contabilidad-de-gestion/clasificacion-de-costos.md), y cómo se reparte la carga fabril entre [centros de costo](../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md) |

Este tema llama variación a lo que Contabilidad llama desvío: la diferencia entre lo real y el estándar. Es un solo concepto con dos nombres; las fórmulas de la planta están en [costo real de la orden](costo-real-de-la-orden.md#las-variaciones-de-la-orden-y-las-del-período).

El centro de trabajo no es el centro de costo. El primero es un lugar de la planta donde se hace una operación, con su capacidad y su tasa; el segundo, un área cuyo responsable responde por un gasto. Que cada centro de trabajo cuelgue de un centro de costo y saque su tasa de ese reparto es inferencia de la base. Si la empresa costea por procesos, la producción en proceso se mide en unidades equivalentes, que están en sistemas de costeo; este tema trabaja con órdenes.

## Mermas, rechazos y reproceso: normal frente a anormal

Toda fabricación pierde algo: material que se corta, piezas que salen mal, unidades que hay que rehacer. La norma contable argentina separa lo normal de lo anormal: lo anormal va a resultados del período. De la NIC 2 se leyó solo lo que dice de la carga fija (párrafo 13); sus párrafos sobre desperdicios anormales no. Merma, rechazo, desecho y reproceso se usan acá con el sentido que les da [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#la-declaración-de-producción).

La norma contable argentina lo dice literal. Hoy es la Resolución Técnica 54 de la FACPCE (Norma Unificada Argentina de Contabilidad), que reemplazó a la RT 17 para las entidades que no aplican las NIIF. En su texto ordenado (T.O. RT 59 y modificatorias), el párrafo 105 suma al costo de un bien producido los materiales e insumos, los costos de conversión «tanto variables como fijos», los costos de puesta en marcha y pruebas, y los financieros que correspondan. Y el párrafo 107 lo recorta:

> «Una entidad no incluirá en el costo de producción, en el costo de construcción ni en el costo de implantación, de un activo ninguno de los siguientes conceptos: a) las improductividades físicas o ineficiencias en el uso de los factores en general; y b) la ociosidad producida por la falta de aprovechamiento de los factores fijos como consecuencia de la utilización de la capacidad de planta por debajo de su nivel de actividad normal.»

Para los desperdicios, el párrafo 108: «Una entidad reconocerá los importes correspondientes a improductividades o ineficiencias (tales como cantidades anormales de materiales, mano de obra u otros costos de conversión desperdiciados), razonablemente determinables y que distorsionen el costo de los bienes producidos, como resultados del período y no como componentes del costo.» El nivel normal, en el párrafo 109, debe «equivaler a la producción que espera alcanzar en promedio durante varios períodos» y «representar un indicador realista, generalmente por debajo de su capacidad total». La norma separa tres cosas (la ineficiencia, la ociosidad bajo el nivel normal y el desperdicio anormal) y manda las tres a resultados. [Producción en la Argentina](../produccion-en-argentina.md) enlaza acá para esta norma.

### Qué cambió de la RT 17 a la RT 54

Lo que la RT 17 decía en su sección 4.2.6 sigue igual en el fondo. Una comentarista de la norma (Bertolino, 2022) escribe sobre los párrafos 104 a 110: «la determinación del costo de producción o construcción no presenta diferencia alguna respecto de lo normado actualmente tanto por la RT 17 como por la RT 41». Cambia la redacción, que pasa de «no debe incluir» a «no incluirá», y el nivel normal, que se explica en dos párrafos (109 y 110) con el ejemplo de los ciclos de la actividad y la precisión de los presupuestos. La lista de componentes también cambió: la RT 54 agrega los costos de puesta en marcha y pruebas, que la lista de 2003 no traía (comparación de la base). Y el estado de resultados debe mostrar por separado las pérdidas por ineficiencia y ociosidad, dentro de otros gastos (párrafo 309 e).

La RT 59 no cambia nada de esto. Es la resolución que, según la que la adopta en la Ciudad, «contiene en su segunda parte el nuevo texto ordenado de la Resolución Técnica N° 54» más aclaraciones sobre ciertos párrafos. Las aclaraciones leídas no tocan los párrafos 104 a 110.

Rige, en la Ciudad de Buenos Aires, para los ejercicios iniciados desde el 1 de enero de 2025, con aplicación anticipada para los ejercicios finalizados desde el 30 de septiembre de 2024 (Resolución P. 460/2024 del consejo, art. 5°). La FACPCE fija otra fecha y cada consejo adopta la suya: está en [normas contables en Argentina](../../Contabilidad/Estados-contables/normas-contables-en-argentina.md). Se aplica a toda entidad que no aplique la RT 26, o sea las NIIF (párrafo 3); los párrafos del costo no distinguen entre pequeñas, medianas y demás.

> [!NOTE] Sin fuente todavía: que la FACPCE derogue la RT 17 de manera expresa. La resolución del consejo de la Ciudad deroga, desde la vigencia, las resoluciones que adoptaron las modificaciones de la RT 17 y la unificación de 2005, y no nombra a la RT 17 como tal; las notas de Contabilidad registran que las fuentes discrepan sobre qué RT derogó la 54. Tampoco se pudo abrir el texto en el sitio de la FACPCE (ni el informe 14 del CENCyA, que es de 2014 y trata la RT 17), ni el consejo de la provincia de Buenos Aires. La RT 17 queda en esta base como antecedente.

La NIC 2 coincide en la carga fija: según el extractor, su párrafo 13 la asigna «based on the normal capacity», y «Unallocated overheads are recognised as an expense in the period in which they are incurred». Sus párrafos sobre desperdicios anormales (16 a 18) no se leyeron. Lo que la carga fija no absorbe es la variación de volumen, que es del período y no de una orden ([costo real de la orden](costo-real-de-la-orden.md)).

### Cómo se separa lo normal de lo anormal

Con una tasa normal fijada de antemano; la RT 17 no da un porcentaje. En los sistemas, la merma normal ya está en el estándar: uno comercial calcula el material como «Qty. Required * (1 + Scrap Factor)» y uno abierto guarda un porcentaje de merma por renglón de la lista (según el resumen). Inferencia de la base: la merma normal es parte del [costo estándar](costo-estandar-del-producto.md), y lo que la pasa aparece como variación de uso de material en el [costo real de la orden](costo-real-de-la-orden.md).

Una fuente de divulgación (según el resumen) dice que el rechazo normal «is included in cost of manufacturing, and it's part of job costing», y que el anormal se saca de la producción en proceso: sus costos «are posted to a loss account». La merma normal se le carga a la orden que la causó, neta de lo que se recupere vendiendo el desecho, o se reparte entre todas por la carga fabril, según sea propia de la orden o del proceso.

| Caso | Dónde va, según las fuentes secundarias (resúmenes) |
|---|---|
| Merma o rechazo normal, propio de la orden | a la orden |
| Merma o rechazo normal, propio del proceso | a la carga fabril, y de ahí a todas las órdenes |
| Merma o rechazo anormal | a una cuenta de pérdida del período |
| Reproceso normal | a la carga fabril |
| Reproceso anormal | a pérdida |
| Reproceso que pide el cliente | a la orden |

> [!NOTE] Sin fuente todavía: una fuente primaria abierta con números de merma normal y anormal y de reproceso en el costeo por órdenes. La tabla sale de resúmenes de fuentes secundarias; el capítulo de Horngren sobre «Spoilage, Rework, and Scrap» solo apareció en copias no oficiales.

### Qué decide la planta y qué decide el costo

La decisión sobre la pieza rechazada (reprocesar, reparar, usar como está con concesión, desechar o devolver al proveedor) es de Calidad y se registra como [no conformidad](../Calidad/no-conformidad.md). La declaración de la merma, del desecho que se vende y del subproducto es de [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md). Acá se decide solo dónde va su costo. La merma que aparece en el depósito al contar (rotura, robo, vencimiento) es otra cosa y es de Inventario, en [ajustes y mermas](../../Inventario-y-depositos/Control-del-stock/ajustes-y-mermas.md).

## Qué guarda un sistema para costear la producción

- Por componente de la lista y por operación: el porcentaje de merma normal.
- Por centro de trabajo: la tasa por hora de máquina, de mano de obra y de carga fabril, con su vigencia.
- Por orden: la merma real por operación y motivo, la diferencia entre la real y la normal, el destino del desecho (depósito de desecho, valor de recupero o subproducto) y la orden de reproceso vinculada a la original, con su costo y quién lo paga.

## Qué hay en Costos de producción

- [Costo estándar del producto](costo-estandar-del-producto.md): cómo se acumula el costo por la lista y la ruta, nivel por nivel, con un ejemplo de dos niveles; cuándo se recalcula.
- [Costo real de la orden](costo-real-de-la-orden.md): qué se le carga a la orden, la producción en proceso, el cierre y el pase a terminado, y las variaciones de la orden frente a las del período.
