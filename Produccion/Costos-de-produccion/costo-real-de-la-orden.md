---
resumen: >-
  El costo real de la orden es lo que efectivamente costó fabricar lo que pidió una orden de producción: el material consumido, las horas trabajadas y la carga fabril aplicada, acumulados mientras la orden está abierta y pasados a producto terminado al cerrarla. Comparado con el costo estándar de lo producido, deja las variaciones de la orden.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Accounting, Volume 2: Managerial Accounting (2019), sección 4.3 (según el resumen): https://openstax.org/books/principles-managerial-accounting/pages/4-3-use-the-job-order-costing-method-to-trace-the-flow-of-product-costs-through-the-inventory-accounts"
  - "OpenStax, ídem, sección 4.5, hoja de costos del trabajo MAC001 (según el resumen): https://openstax.org/books/principles-managerial-accounting/pages/4-5-compute-the-cost-of-a-job-using-job-order-costing"
  - "OpenStax, ídem, sección 4.7, asientos (según el resumen): https://openstax.org/books/principles-managerial-accounting/pages/4-7-prepare-journal-entries-for-a-job-order-cost-system"
  - "OpenStax, ídem, sección 8.2, variaciones de materiales (según el resumen): https://openstax.org/books/principles-managerial-accounting/pages/8-2-compute-and-evaluate-materials-variances"
  - "OpenStax, ídem, sección 8.3, variaciones de mano de obra (según el resumen): https://openstax.org/books/principles-managerial-accounting/pages/8-3-compute-and-evaluate-labor-variances"
  - "OpenStax, ídem, sección 8.4, variaciones de carga fabril (según el resumen): https://openstax.org/books/principles-managerial-accounting/pages/8-4-compute-and-evaluate-overhead-variances"
  - "OpenStax, ídem, sección 8.5, uso del análisis de variaciones (según el resumen): https://openstax.org/books/principles-managerial-accounting/pages/8-5-describe-how-companies-use-variance-analysis"
  - "LibreTexts, Principles of Managerial Accounting (Jonick), 8.04 Factory overhead variances (según el resumen): https://biz.libretexts.org/Bookshelves/Accounting/Principles_of_Managerial_Accounting_(Jonick)/08%3A_Variance_Analysis/8.04%3A_Factory_overhead_variances"
  - "Documentación de un sistema abierto, Manufacturing order costs (según el resumen): https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/manufacturing/basic_setup/mo_costs.html"
  - "Documentación de un sistema abierto, Work Order (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/work-order"
  - "Resolución Técnica 17 FACPCE, texto ordenado de junio de 2003 (Consejo Profesional de CABA), sección 5.5 (leída en el texto): https://www.consejo.org.ar/storage/attachments/RT_FACPCE17_TO2003.pdf-bGCewZIHs8.pdf"
  - "Resolución Técnica 54 FACPCE, T.O. RT 59 y modificatorias, párrafos 107, 114 y 290 a 295 (leída en el texto publicado por el Consejo Profesional de CABA): https://consejo.org.ar/storage/attachments/Resolucion%20Tecnica%20N%2054%20(TO%20RT%2059%20y%20modi-7TbUsld18i.pdf"
  - "Gisela Bertolino, Bienes de cambio y costo de ventas en la RT 54, La Ley, 2022 (leída): https://www.consejosalta.org.ar/wp-content/uploads/Bienes-de-cambio-y-costo-de-ventas.-Analisis-de-los-cambios-a-su-tratamiento-contable-en-el-marco-de-la-nueva-RT-54.pdf"
  - "Produccion/.investigacion/costos.md (secciones 2, 3 y 5), 2026-11-27"
aliases: [costo real de la orden, costo de la orden, costo real, actual cost, job cost, hoja de costos, hoja de costos de la orden, job cost sheet, producción en proceso, productos en proceso, work in process, WIP, carga fabril aplicada, applied overhead, carga fabril sobreaplicada, carga fabril subaplicada, over-applied overhead, under-applied overhead, variación, desvío, variance, variación de uso, variación de cantidad, usage variance, variación de eficiencia, efficiency variance, variación de volumen, volume variance, costo de producción terminada, cost of goods manufactured]
creado: 2026-11-27
revisado: 2026-11-27
---

# Costo real de la orden

El costo real de la orden es lo que efectivamente costó fabricar lo que pidió una orden de producción: el material consumido, las horas trabajadas y la carga fabril aplicada, acumulados mientras la orden está abierta y pasados a producto terminado al cerrarla. Comparado con el costo estándar de lo producido, deja las variaciones de la orden.

Es la contracara del [costo estándar del producto](costo-estandar-del-producto.md), dentro de [Costos de producción](costos-de-produccion.md). La [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) y sus estados son de Ejecución en planta, y los consumos y lo declarado llegan de [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md). Los asientos y el [sistema de costeo](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md) son de Contabilidad.

## Lo que se le carga a la orden

Cada orden lleva su hoja de costos. OpenStax (sección 4.5) la define así: «A job cost sheet is a subsidiary ledger that identifies the individual costs for each job» (según el resumen). Tiene tres renglones:

- Material: lo que sale del depósito para la orden, al costo del inventario (en papel, la requisición).
- Mano de obra: las horas que los partes atribuyen a la orden, por su tarifa.
- Carga fabril aplicada: una tasa predeterminada por la base de reparto. No es la carga fabril real, que no se puede atribuir a una orden.

Un sistema abierto toma el costo real de operación de las tarjetas de trabajo de cada operación y permite cargar a mano «Any additional expenses you may have incurred when manufacturing the Item» (según el resumen).

### Un ejemplo: el trabajo MAC001

OpenStax (secciones 4.5 y 4.7) sigue un cartel de vinilo, el trabajo MAC001, empezado el 22/12/2018 y terminado el 22/2/2019.

| Renglón | Detalle | Importe |
|---|---|---|
| Material | vinilo 1 × $300; tinta negra 2 × $50; tinta roja 1 × $60; tinta dorada 1 × $60; ojales 12 × $10; madera 40 × $1,50 | $700 |
| Mano de obra | encargado de materiales $15; técnico de impresión $15; ayudantes 2 × $18 | $66 |
| Carga fabril aplicada | $66 × $2,50 por peso de mano de obra | $165 |
| Costo total | | $931 |

El trabajo se vendió a $2000; las sumas las verificó la base. La hoja impresa del libro tiene un error de tasa: muestra $1,50 sobre los $66, que darían $99 y no $165. La tasa del capítulo es $2,50 por peso de mano de obra ($165 ÷ $66), y es la que va en la tabla. Los asientos de la sección 4.7 parten la mano de obra en $30 de producción y $36 de terminación: el total coincide con la hoja, la partición no.

## La producción en proceso es la suma de las órdenes abiertas

Mientras una orden está abierta (liberada, en curso o terminada sin cerrar, en los [estados](../Ejecucion-en-planta/orden-de-produccion.md#los-estados-en-dos-sistemas-abiertos) que usa el tema), su costo acumulado es producción en proceso (WIP). Según un resultado del buscador sobre OpenStax 4.5, «the total of all the work in process job cost sheets equals the work in process inventory». No hacen falta unidades equivalentes: esas son del costeo por procesos, en [sistemas de costeo](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md).

Un sistema abierto transfiere el material a un depósito de producción en proceso al empezar, o saltea ese paso y lo da por consumido al terminar (según el resumen). La segunda es el consumo automático de [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md): más simple, pero la orden abierta no muestra su costo hasta el final (inferencia de la base).

## El cierre y el pase a terminado

Al cerrar la orden, su costo pasa de producción en proceso a productos terminados: según OpenStax 4.7, «an entry is made to transfer the total cost from the work in process inventory to the finished goods inventory». En el ejemplo:

| Hecho | Sale de | Entra en | Importe |
|---|---|---|---|
| Entrega de material a la orden | materias primas | producción en proceso | $700 |
| Mano de obra de la orden | sueldos de fábrica a pagar | producción en proceso | $66 |
| Carga fabril aplicada | carga fabril | producción en proceso | $165 |
| Cierre de la orden | producción en proceso | productos terminados | $931 |
| Venta | productos terminados | [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md) | $931 |

La carga fabril real del período (en el ejemplo, $21.000 de suministros, servicios, amortización, seguros e intereses, más $4000 de mano de obra indirecta) va a la cuenta de carga fabril, no a una orden. Lo acumulado y lo aplicado a todas las órdenes casi nunca coinciden: la diferencia es carga fabril sobreaplicada o subaplicada, y «an adjusting entry is made to dispose of the under- or overapplied overhead».

> [!NOTE] Sin fuente todavía: un ejemplo con números de carga fabril sobreaplicada o subaplicada y de su ajuste al cierre. OpenStax 4.7 la nombra sin cifras.

El costo de lo terminado en el período es producción en proceso inicial más los costos de fabricación del período menos producción en proceso final (OpenStax 4.3, según el resumen).

## La producción en proceso al cierre del período

Al cierre de un mes, la producción en proceso es la suma de las hojas de las órdenes abiertas. Eso pide que cada una tenga cargados sus consumos, horas y carga aplicada hasta la fecha de cierre (inferencia de la base).

El costo acumulado no es necesariamente el valor del balance, pero en la norma argentina vigente se acerca. La RT 54, párrafo 293, manda medir los bienes de cambio «producidos o construidos o que se encuentran en proceso de producción o construcción» por alguno de dos criterios: «a) costo de producción o costo de construcción; o b) costo de reproducción y/o reconstrucción». El costo de reproducción se arma con los mismos componentes del costo de producción, «expresando cada uno de ellos en términos de su reposición, a la fecha de la medición» (párrafo 114). El costo de las órdenes es, entonces, la base del valor (lectura de la base).

Esto cambió desde la RT 17. En el texto de 2003 valuaba lo que está en producción a costo de reposición con el mismo grado de avance o, si no se podía, a «su costo de reproducción», calculado con su sección 4.2.6, y admitía el valor neto de realización según el avance en procesos prolongados con cuatro condiciones. La RT 54 solo deja el valor neto de realización para los bienes «fungibles con mercado activo y comercializables sin esfuerzo significativo» (párrafo 295), y permite elegir entre costo de producción y de reproducción sin preferencia. Lo dice la comentarista Bertolino (2022): «La RT 54 no prevé otros casos particulares de medición de bienes de cambio, como sí lo hacen RT 17 y RT 41», entre ellos los bienes en proceso con anticipos que fijan precio, medidos «a su valor neto de realización, proporcionado de acuerdo con el grado de avance». El marco vigente, su vigencia y a quién alcanza están en [costos de producción](costos-de-produccion.md#qué-cambió-de-la-rt-17-a-la-rt-54) y en [normas contables en Argentina](../../Contabilidad/Estados-contables/normas-contables-en-argentina.md).

> [!NOTE] Sin fuente todavía: la RT 17 se leyó solo en el texto ordenado de 2003, y pudo cambiar con modificaciones posteriores antes de la RT 54; falta compararla con su texto final. La RT 54 se leyó en el T.O. del consejo de la Ciudad y no en la FACPCE.

## Planeado frente a real en un sistema

Un sistema abierto muestra por orden el costo estimado, «how much it should cost», y el real, «how much it actually costs», que se separan si cambian las cantidades, la duración de las operaciones o la tarifa del empleado (según el resumen). En su ejemplo, una orden de $65 ($50 de componentes y $15 de operaciones) terminó en $70 porque las operaciones tardaron diez minutos más; el costo promedio del producto quedó en $67,50.

## Las variaciones de la orden y las del período

Una variación es la diferencia entre lo real y el estándar para lo producido, separada en efecto precio y efecto cantidad; el análisis general está en [presupuesto](../../Contabilidad/Contabilidad-de-gestion/presupuesto.md), que la llama desvío. La planta agrega cuándo se calcula cada una: unas dependen de lo que consumió la orden y otras, del período entero.

| Variación | Fórmula | Se mide | De quién |
|---|---|---|---|
| Uso de material | (cantidad real − cantidad estándar para lo producido) × precio estándar | al cerrar la orden | de la orden |
| Eficiencia de mano de obra | (horas reales − horas estándar) × tarifa estándar | al cerrar la orden | de la orden |
| Eficiencia de la carga variable | (horas reales − horas estándar) × tasa variable estándar | al cerrar la orden | de la orden |
| Precio de material | (precio real − precio estándar) × cantidad real | al comprar | del período |
| Tarifa de mano de obra | (tarifa real − tarifa estándar) × horas reales | al liquidar | del período |
| Tasa de la carga variable | (tasa real − tasa estándar) × horas reales | al cierre del período | del período |
| Volumen de la carga fija | (horas a capacidad normal − horas estándar de lo producido) × tasa fija | al cierre del período | del período |

Las fórmulas son de OpenStax (secciones 8.2 a 8.4) y, la de volumen, de LibreTexts (Jonick 8.04). Las columnas «se mide» y «de quién» son inferencia de la base, salvo la del precio de material: las fuentes enseñan las variaciones juntas, por la fórmula. Esa tiene apoyo directo: «the material price variance is computed at the time of purchase and not when the material is used in production».

Los ejemplos de las fuentes:

- Material, Biglow Company (OpenStax 8.2): estándar de 8 onzas por botella a $0,85 la onza; 11.000 botellas; se compran y usan 89.000 onzas por $74.760, a $0,84. Precio: $890 favorable. Uso: (89.000 − 88.000) × $0,85 = $850 desfavorable. Total: $40 favorable.
- Mano de obra, Biglow (OpenStax 8.3): estándar de 1,5 horas por botella a $35 la hora, 16.500 horas para las 11.000; reales 16.000 horas por $565.600, a $35,35. Tarifa: $5.600 desfavorable. Eficiencia: (16.000 − 16.500) × $35 = $17.500 favorable. Total: $11.900 favorable ($565.600 reales contra $577.500 estándar). La solución impresa rotula el total como desfavorable y muestra $5.650 en una celda; las cuentas de la base dan lo de arriba.
- Carga variable, Connie's Candy (OpenStax 8.4): tasa estándar $4.000 ÷ 2.000 horas = $2,00; real $7.000 ÷ 2.500 horas = $2,80. Tasa: $2.000 desfavorable. Eficiencia: (2.500 − 2.000) × $2,00 = $1.000 desfavorable. Total: $3.000 desfavorable.
- Volumen de la carga fija (Jonick 8.04): carga fija presupuestada $70.000 sobre 10.000 horas de capacidad normal, $7 por hora; se producen 8.000 unidades de una hora. «Fixed factory overhead volume variance = (10,000 – 8,000) x $7 per direct labor hour = $14,000», desfavorable: «the fixed overhead was underutilized». Con 11.000 unidades da $7.000 favorable.

La variación de volumen es la ociosidad que la RT 54 deja fuera del costo (párrafo 107) ([costos de producción](costos-de-produccion.md)), y no es de ninguna orden: depende de cuánto se produjo en total frente a la capacidad normal (inferencia de la base; la capacidad, en [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md)). La de uso de material es donde aparece la merma por encima de la normal. La de eficiencia valoriza una de las acepciones de eficiencia de la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#eficiencia-y-utilización-dos-acepciones-de-eficiencia): horas estándar frente a horas trabajadas (lectura de la base).

> [!NOTE] Sin fuente todavía: la variación de gasto de la carga fija (real menos presupuestada) con fórmula y números. OpenStax 8.4 menciona dos variaciones de la carga fija sin nombrarlas ni calcularlas.

Según OpenStax 8.5, «the management responsible for the variances must explain any variances outside of a certain range», sin dar umbrales; explicar también las favorables deja ver si son sostenibles. Para la carga variable hace falta el supervisor de producción (8.4). Que el precio se le pregunte a compras y el uso a producción es inferencia de la base. Ningún sistema abierto leído calcula variaciones con nombre: muestran estimado frente a real.

## Qué guarda un sistema por cada orden

- La orden, con su estado y las cantidades planeada, producida y rechazada.
- Los consumos reales de material con su valor, los tiempos reales por operación, centro de trabajo y empleado, y los costos adicionales cargados a mano.
- El costo estimado y el real por elemento, el saldo en producción en proceso y el movimiento de cierre a productos terminados.
- Las horas estándar permitidas para lo producido y la variación por elemento, con su signo y su causa.
- Por período, la capacidad normal en horas de cada centro de trabajo.
