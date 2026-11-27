---
resumen: >-
  El costo estándar de un producto fabricado es lo que debería costar una unidad, calculado sumando nivel por nivel el material de la lista de materiales y la conversión de cada operación de la ruta (horas por la tasa de su centro de trabajo). Se fija para un período y es la vara contra la que se mide el costo real de cada orden.
estado: vigente
estabilidad: estable
fuentes:
  - "Documentación de un sistema comercial, Bills of Material: Cost Calculation (según el resumen): https://help.myob.com.au/advanced/Docs/Published/UserGuide/BOM_Cost_Calculation.html"
  - "Documentación de un sistema comercial, Example of Cost Rollup (según el resumen): https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fapma/example-of-cost-rollup.html"
  - "Documentación de un sistema abierto, Bill of Materials (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials"
  - "Documentación de un sistema abierto, Manufacturing order costs (según el resumen): https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/manufacturing/basic_setup/mo_costs.html"
  - "Paquete de investigación operativa, Roll-Up Cost in Indented Bill of Material (datos de entrada; la salida según el buscador): https://support.sas.com/documentation/onlinedoc/or/ex_code/131/bom8.html"
  - "IFRS Foundation, NIC 2 Inventarios, párrafo 21 (según el extractor, con citas acortadas): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html"
  - "AccountingTools, When should I update standard costs (secundaria, según el resumen): https://www.accountingtools.com/articles/when-should-i-update-standard-costs.html"
  - "OpenStax, Principles of Accounting, Volume 2: Managerial Accounting (2019), sección 8.1, como la cita Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md"
  - "Produccion/.investigacion/costos.md (sección 1), 2026-11-27"
aliases: [costo estándar del producto, costo estándar, standard cost, acumulación de costos, roll-up de costos, cost roll-up, costo de la lista de materiales, BOM cost, costeo de la lista, tasa del centro de trabajo, work center rate, tarifa horaria, escenario de costos, cost scenario]
creado: 2026-11-27
revisado: 2026-11-27
---

# Costo estándar del producto

El costo estándar de un producto fabricado es lo que debería costar una unidad, calculado sumando nivel por nivel el material de la lista de materiales y la conversión de cada operación de la ruta (horas por la tasa de su centro de trabajo). Se fija para un período y es la vara contra la que se mide el costo real de cada orden.

Qué es un costo estándar como método contable, ideal o alcanzable, y la tarjeta de costo de una bicicleta con sus cinco renglones, está en [sistemas de costeo](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md). Esta nota explica de dónde sale cada renglón en una fábrica: de la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md), de la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) y de la tasa de cada centro de trabajo. Es una de las dos piezas de [Costos de producción](costos-de-produccion.md); la otra es el [costo real de la orden](costo-real-de-la-orden.md).

## La norma lo acepta si se parece al real

La NIC 2 permite valuar el inventario a costo estándar con una condición. Según el extractor, su párrafo 21 dice que puede usarse «for convenience if the results approximate cost», y que «Standard costs take into account normal levels of materials and supplies, labour, efficiency and capacity utilisation». El estándar, entonces, supone consumos, eficiencia y uso de la capacidad normales: la merma normal va adentro y la anormal no, como explica [costos de producción](costos-de-produccion.md).

## Cada renglón: cantidad de la lista o de la ruta por un precio

Un sistema comercial documenta las fórmulas con que costea una lista y su ruta (según el resumen):

| Elemento | Fórmula de la fuente | De dónde sale la cantidad |
|---|---|---|
| Material | «Qty. Required * (1 + Scrap Factor)», por el costo unitario del componente | la lista, con su porcentaje de merma |
| Mano de obra | «((Setup time / Lot size) + Run time converted to hours per piece) * (Work Center Standard Cost)» | la ruta: preparación, ejecución y tamaño de lote |
| Máquina | «(Machine hours converted to hours per piece) * (Machine standard cost)» | la ruta |
| Carga fabril | «Overhead is calculated dependent on the overhead type», sin fórmula | según el tipo: una tasa por hora o un porcentaje |

La fórmula de mano de obra muestra cómo la tasa del centro de trabajo se vuelve costo por unidad. La preparación se reparte entre las unidades del lote y la ejecución se cuenta por pieza. Por eso el mismo producto tiene un costo unitario más alto si el estándar supone lotes más chicos (lectura de la fórmula).

Un sistema abierto calcula igual: el costo de operación sale de una tarifa por hora, el tiempo y el tamaño del lote. Guarda el costo por hora del centro de trabajo y el de cada empleado en campos distintos; el estimado usa el del centro y el real el del empleado. Su ejemplo: con US$ 50 por hora en el centro y US$ 60 en el empleado, el estimado se calcula a 50 y el real a 60 (según el resumen).

## Nivel por nivel, de abajo hacia arriba

El costo se acumula desde el componente más bajo de la lista hacia el producto final. Un sistema comercial lo dice así: con la opción multinivel, «the system first calculates costs for all subassemblies included in a bill of material» antes de costear el nivel de arriba. Otro, según el buscador, «builds the cost of assemblies, starting with the lowest level, and works up the structure». Según el mismo resultado, se empieza por el código de nivel bajo más alto y se sube. Que ese código sea el mismo con que el [MRP](../Planificacion-de-la-produccion/mrp.md) explota la lista, y que por él un componente que aparece en dos niveles se costee una sola vez, es inferencia de la base.

Cada nivel suma dos cosas: lo que viene de abajo (el costo ya acumulado de sus componentes) y lo que agrega él (su propio material y la conversión de sus operaciones). Un sistema comercial muestra el desglose por elemento con esas dos columnas, «Lower Level» y «This Level». Con ellas se ve cuánto de un producto final es material comprado y cuánto es conversión hecha en la planta.

Según un resultado del buscador sin verificar, la acumulación de un sistema comercial arrastra el material de un subconjunto fantasma pero no su ruta. Qué es una lista fantasma está en [lista de materiales](../Producto-y-proceso/lista-de-materiales.md).

## Un ejemplo de dos niveles

El ejemplo más completo que se encontró es de la documentación de un sistema comercial (según el resumen). El producto RS-ABCD se arma con dos subconjuntos, RS-AB y RS-CD, en lotes de una unidad.

| Artículo | Nivel | Lo que viene de abajo | Lo que agrega este nivel | Costo |
|---|---|---|---|---|
| RS-AB | 1 | material RS-A 1,50 y RS-B 2,00 | operario de máquina 2 × 1,00 = 2,00; ingeniero de fabricación 2 × 2,00 = 4,00 | 9,50 |
| RS-CD | 1 | material RS-C 3,00 y RS-D 4,00 | electricista 3,00; inspector 4,00 | 14,00 |
| RS-ABCD | 2 | RS-AB 9,50 y RS-CD 14,00 | operación 10, armado del bastidor: electricistas 2 × 5,00 = 10,00; operación 20, inspección: 4,00; carga fabril de planta 0,10 | 37,60 |

Las cuentas cierran (verificadas por la base): 1,50 + 2,00 + 2,00 + 4,00 = 9,50; 3,00 + 4,00 + 3,00 + 4,00 = 14,00; 9,50 + 14,00 + 10,00 = 33,50 en la operación 10, y 33,50 + 4,00 + 0,10 = 37,60.

La carga fabril del ejemplo es un porcentaje del material y no una tasa por hora: «Plant overhead: 1% of total material cost. Materials are RS-A (1.00) + RS-B (2.00) + RS-C (3.00) + RS-D (4.00) = 10.00, so 1% = 0.10.» La página tiene una inconsistencia menor: RS-A figura con 1,50 en el subconjunto, incluidos 0,50 de carga, y con 1,00 en la cuenta de la carga de planta. Se citan los totales.

Un segundo ejemplo, de un paquete de investigación operativa, es solo de material y tiene tres niveles. Una lámpara LA01 lleva una base B100, una pantalla S100 (4,10) y un conjunto de zócalo A100. Con los costos de los comprados de la fuente, la base calcula B100 = 1,30 + 9,25 + 5,00 + 4 × 0,20 = 16,35 (el primer sumando son 26 piezas de 0,05) y A100 = 0,40 + 3,50 + 4,70 = 8,60, así que LA01 = 16,35 + 4,10 + 8,60 = 29,05. Según el buscador, la salida de la fuente da lo mismo. El tornillo de 0,20 aparece en la base y en el zócalo, y eso obliga a costear por niveles y no rama por rama.

> [!NOTE] Sin fuente todavía: un libro de texto abierto con una acumulación multinivel numérica que incluya la ruta, la mano de obra por tasa del centro de trabajo y la carga fabril por tasa. Los dos ejemplos son de documentación de software, y el que tiene ruta usa la carga fabril como porcentaje del material.

## Cuándo se fija y cuándo se recalcula

Son dos actos distintos. El estándar se fija, según OpenStax (sección 8.1, como la cita [sistemas de costeo](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md)), por lo general al empezar el ejercicio. Recalcular la acumulación cuando cambia un precio, una lista o una ruta es otra cosa, y los sistemas lo ofrecen aparte. Un sistema abierto tiene un botón «Update Cost» y una opción para actualizar el costo de la lista solo; otro resetea el costo del producto «to the expected cost» de la lista y lleva aparte el costo promedio de las órdenes terminadas (según el resumen).

Un sistema comercial guarda cada corrida con su fecha y su escenario: su ejemplo es un «Cost Scenario effective 9/1/2020». Guardar el escenario permite recalcular sin pisar el estándar vigente y comparar los dos antes de adoptar el nuevo.

Sobre la frecuencia no hay norma. Una fuente secundaria (consultoras y proveedores que dicen lo mismo, contados como una sola fuente) describe la práctica común: una actualización por año con el presupuesto, más seguida si los costos son volátiles o ante un hecho puntual, como una suba sostenida de un proveedor o una tarifa nueva. Agrega una señal: si las variaciones van siempre para el mismo lado, el estándar está mal fijado.

Un [cambio de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md) que toca la lista o la ruta cambia también el costo que sale de ellas. Si el estándar no se recalcula, las órdenes nuevas van a mostrar una variación que no es de la planta sino del maestro (inferencia de la base).

> [!NOTE] Sin fuente todavía: evidencia de cuántas empresas actualizan el estándar cada año; la frecuencia anual sale de una sola fuente secundaria.

## Qué guarda un sistema para el costo estándar

- La lista de materiales con la cantidad por unidad y el porcentaje de merma de cada componente.
- La ruta con sus operaciones, el centro de trabajo de cada una, el tiempo de preparación, el de ejecución y el tamaño de lote.
- La tasa por hora de cada centro de trabajo (máquina, mano de obra y carga fabril), con su vigencia.
- El costo unitario de cada artículo comprado.
- Cada corrida de la acumulación, con su fecha y su escenario.
- El costo estándar resultante de cada artículo, por elemento (material, mano de obra, máquina, carga fabril) y separado en lo que viene de abajo y lo que agrega su nivel.
- El costo promedio real de las órdenes terminadas, para compararlo con el estándar.
