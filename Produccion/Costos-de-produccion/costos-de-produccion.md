---
resumen: >-
  Costos de producción es la parte que dice cuánto cuesta lo fabricado: el costo estándar de cada producto, que sale de la lista de materiales y la ruta, el costo real que junta cada orden con los consumos y las horas de la planta, y las variaciones entre los dos. El método de costeo y el registro en los libros son de Contabilidad; acá, de dónde salen los datos.
estado: borrador
estabilidad: estable
fuentes:
  - "Resolución Técnica 17 FACPCE, texto ordenado de junio de 2003 (Consejo Profesional de CABA), sección 4.2.6 «Bienes producidos» (leída entera): https://www.consejo.org.ar/storage/attachments/RT_FACPCE17_TO2003.pdf-bGCewZIHs8.pdf"
  - "IFRS Foundation, NIC 2 Inventarios, párrafos 12 a 14 y 21 (según el extractor, con citas acortadas): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html"
  - "Dummies, Cost Accounting: Job Costs for Spoilage, Reworked Products, and Scrap (secundaria, según el resumen): https://www.dummies.com/article/business-careers-money/business/accounting/general-accounting/cost-accounting-job-costs-for-spoilage-reworked-products-and-scrap-164765"
  - "Iowa State (ISUDP), curso de contabilidad de gestión (según el resumen del buscador; la página no abrió): https://iastate.pressbooks.pub/isudp-2025-202/?p=23"
  - "Documentación de un sistema abierto, Bill of Materials (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials"
  - "Documentación de un sistema abierto, Work Order (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/work-order"
  - "Documentación de un sistema comercial, Bills of Material: Cost Calculation (según el resumen): https://help.myob.com.au/advanced/Docs/Published/UserGuide/BOM_Cost_Calculation.html"
  - "Produccion/.investigacion/costos.md (secciones 1, 4, 5 y 6), 2026-11-27"
aliases: [costos de producción, costo de producción, costo de fabricación, manufacturing cost, production cost, costo industrial, merma normal, merma anormal, normal spoilage, abnormal spoilage, rechazo, reproceso, retrabajo, rework, desecho, scrap, ociosidad, capacidad ociosa, idle capacity]
creado: 2026-11-27
revisado:
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

Toda fabricación pierde algo: material que se corta, piezas que salen mal, unidades que hay que rehacer. Las normas contestan igual si esa pérdida es costo del producto: lo normal va al producto y lo anormal, a resultados del período. Merma, rechazo, desecho y reproceso se usan acá con el sentido que les da [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md#la-declaración-de-producción).

La Resolución Técnica 17 de la FACPCE, norma contable argentina, lo dice literal. Su sección 4.2.6 suma al costo de un bien producido los materiales, los costos de conversión «tanto variables como fijos» y los financieros asignables, y lo recorta:

> «El costo de los bienes producidos no debe incluir la porción de los costos ocasionados por: a) improductividades físicas o ineficiencias en el uso de los factores en general; b) la ociosidad producida por la falta de aprovechamiento de los factores fijos originada en la no-utilización de la capacidad de planta a su "nivel de actividad normal".»

Para los desperdicios agrega: «Los importes correspondientes a cantidades anormales de materiales, mano de obra u otros costos de conversión desperdiciados, razonablemente determinables y que distorsionen el costo de los bienes producidos, no participarán en su determinación y deben ser reconocidos como resultados del período.» El nivel normal es «la producción que se espera alcanzar como promedio de varios períodos», por debajo de la capacidad total, «un indicador realista y no como un objetivo ideal». Separa tres cosas que el campo suele mezclar (la ineficiencia, la ociosidad bajo el nivel normal y el desperdicio anormal) y manda las tres a resultados. [Producción en la Argentina](../produccion-en-argentina.md) enlaza acá para esta norma.

> [!NOTE] Sin fuente todavía: el texto vigente. La RT 17 se leyó en el texto ordenado de 2003; la RT 54 unificó las normas contables para la mayoría de las empresas y se consulta en texto ordenado (ver [normas contables en Argentina](../../Contabilidad/Estados-contables/normas-contables-en-argentina.md)). Falta confirmar en el texto vigente de la FACPCE que la exclusión de lo anormal y de la ociosidad sigue igual, y una segunda fuente argentina independiente (el informe 14 del CENCyA es la candidata).

La NIC 2 coincide en la carga fija: según el extractor, su párrafo 13 la asigna «based on the normal capacity», y «Unallocated overheads are recognised as an expense in the period in which they are incurred». Sus párrafos sobre desperdicios anormales (16 a 18) no se leyeron. Lo que la carga fija no absorbe es la variación de volumen, que es del período y no de una orden ([costo real de la orden](costo-real-de-la-orden.md)).

### Cómo se separa lo normal de lo anormal

Con una tasa normal fijada de antemano; la RT 17 no da un porcentaje. En los sistemas, la merma normal ya está en el estándar: uno comercial calcula el material como «Qty. Required * (1 + Scrap Factor)» y uno abierto guarda un porcentaje de merma por renglón de la lista (según el resumen). Inferencia de la base: la merma normal es parte del [costo estándar](costo-estandar-del-producto.md), y lo que la pasa aparece como variación de uso de material en el [costo real de la orden](costo-real-de-la-orden.md).

Una fuente de divulgación (según el resumen) dice que el rechazo normal «is included in cost of manufacturing, and it's part of job costing», y que el anormal se saca de la producción en proceso: sus costos «are posted to a loss account». La merma normal se le carga a la orden que la causó, neta de lo que se recupere vendiendo el desecho, o se reparte entre todas por la carga fabril, según sea propia de la orden o del proceso.

| Caso | Dónde va, según las fuentes secundarias |
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
