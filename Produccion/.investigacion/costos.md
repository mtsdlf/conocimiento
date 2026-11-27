# Producción: Costos de producción (informe de investigación)

Ángulo: el costo mirado desde la planta y la orden. Los sistemas de costeo como método contable (órdenes/procesos, absorción/variable, estándar, ABC) y el costo de lo vendido ya están escritos en `Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md` y `Contabilidad/Operaciones/costo-de-lo-vendido.md`: acá solo se enlazan. Esa nota ya trae la tarjeta de costo estándar de la bicicleta (OpenStax 8.1, total US$ 165,25) y el ejemplo de unidades equivalentes de Rock City (OpenStax 5.3); no se repiten.

Convención de marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Importante: las páginas web se leyeron a través de un extractor automático (WebFetch), que devuelve resúmenes y citas cortas, no la página entera. Por eso las páginas web llevan [S]. La única fuente leída con texto completo (extraído con `pdftotext`) es la RT 17, texto ordenado de 2003. Puntajes 1-3: A autoridad, P profundidad, E ejemplos, U unicidad.

Aviso: las citas de OpenStax salen del extractor, que las acorta. Antes de poner una cita textual en la nota, verificarla contra la página.

Las fuentes de proveedores de software (marcadas "comercial") sirven como evidencia de qué registra un sistema; en la nota hay que decir "un sistema" sin nombrarlo. Dejo el nombre acá solo para trazar.

---

## 1. Costo estándar del producto (acumulación por lista y ruta, cost roll-up)

### Fuentes

| # | Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| 1.1 | Un sistema abierto (Odoo), "Manufacturing order costs": https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/manufacturing/basic_setup/mo_costs.html | primaria (práctica de sistemas) | 2 | 2 | 3 | 2 | [S] |
| 1.2 | Un sistema abierto (ERPNext), "Bill of Materials": https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials | primaria (práctica de sistemas) | 2 | 2 | 1 | 2 | [S] |
| 1.3 | Un sistema comercial (Oracle), "Example of Cost Rollup": https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fapma/example-of-cost-rollup.html | primaria (práctica de sistemas) | 2 | 2 | 3 | 1 | [S] |
| 1.4 | Un sistema comercial (MYOB Acumatica), "Bills of Material: Cost Calculation": https://help.myob.com.au/advanced/Docs/Published/UserGuide/BOM_Cost_Calculation.html | primaria (práctica de sistemas) | 2 | 2 | 1 | 1 | [S] |
| 1.5 | Un paquete de investigación operativa (SAS), "Roll-Up Cost in Indented Bill of Material": https://support.sas.com/documentation/onlinedoc/or/ex_code/131/bom8.html | primaria (datos de entrada, sin la salida) | 1 | 1 | 2 | 1 | [S] |
| 1.6 | NIC 2 (IFRS Foundation), párrafo 21 sobre costo estándar: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html | primaria (norma) | 3 | 2 | 1 | 2 | [S] |
| 1.7 | AccountingTools, "When to update standard costs": https://www.accountingtools.com/articles/when-should-i-update-standard-costs.html (y otros resultados del buscador de consultoras y proveedores que dicen lo mismo: una sola fuente) | secundaria | 1 | 1 | 1 | 1 | [S] |
| 1.8 | OpenStax Vol. 2, 8.1 (tarjeta de costo estándar); no la releí: la cita `sistemas-de-costeo.md` | primaria | 3 | 2 | 3 | 1 | no leído acá |

### Afirmaciones

1. **Qué entra al costo estándar de un producto fabricado.** Según un sistema abierto, el costo de la lista de materiales se calcula "from the Valuation Rate of the raw materials/sub-assemblies involved and the Operation costs"; el costo de operación sale de una tarifa por hora, el tiempo y el tamaño del lote, y los centros de trabajo están "defined only for product costing and Work Order Operations scheduling purposes" (1.2). Otro sistema abierto: el costo de una orden "represents how much it should cost to complete an MO, based on the configuration of the product's bill of materials" (1.1).
2. **Fórmulas por componente (un sistema comercial, 1.4).** Mano de obra: "((Setup time / Lot size) + Run time converted to hours per piece) * (Work Center Standard Cost)". Máquinas: "(Machine hours converted to hours per piece) * (Machine standard cost)". Materiales: "Qty. Required * (1 + Scrap Factor)" (con tamaño de lote distinto de cero, se multiplica además por lote / tamaño de lote). Carga fabril: la fuente solo dice "Overhead is calculated dependent on the overhead type", sin fórmula. El preparado se reparte entre las unidades del lote y la corrida es por pieza: así la tarifa del centro de trabajo se convierte en costo por unidad.
3. **Orden de cálculo nivel por nivel.** Con la opción multinivel, "the system first calculates costs for all subassemblies included in a bill of material" antes del nivel de arriba (1.4). Otros sistemas comerciales dicen lo mismo según el buscador [S, no abrí las páginas]: se costea primero el nivel más bajo (el código de nivel bajo más alto) y se sube; Oracle: "builds the cost of assemblies, starting with the lowest level, and works up the structure". Una salvedad del mismo resultado [S, sin verificar]: el roll-up de un sistema comercial arrastra el material de un ensamble fantasma pero no su ruta.
4. **Ejemplo numérico literal de roll-up (un sistema comercial, 1.3).** Producto RS-ABCD, costo unitario 37,60, lote de 1.
   - RS-AB (nivel 1) = 9,50: material RS-A 1,50 + material RS-B 2,00 + operario de máquina 2 × 1,00 = 2,00 + ingeniero de fabricación 2 × 2,00 = 4,00.
   - RS-CD (nivel 1) = 14,00: material RS-C 3,00 + RS-D 4,00 + electricista 3,00 + inspector 4,00.
   - RS-ABCD (nivel 2): operación 10, armado del bastidor = 9,50 + 14,00 + electricistas 2 × 5,00 = 33,50; operación 20, inspección = 4,00; carga fabril de planta 0,10; total 33,50 + 4,00 + 0,10 = 37,60.
   - La fuente: "Plant overhead: 1% of total material cost. Materials are RS-A (1.00) + RS-B (2.00) + RS-C (3.00) + RS-D (4.00) = 10.00, so 1% = 0.10." O sea, una carga fabril como porcentaje del material, no como tasa por hora. La página trae un desglose por elemento de costo con "Lower Level" y "This Level" (lo que viene de abajo y lo que agrega este nivel), que permite ver cuánto de un ensamble final es material y cuánto conversión. Tiene inconsistencias menores (RS-A aparece con 1,50 "incluyendo 0,50 de carga" y como material de 1,00 en la cuenta de la carga de planta): si se cita, citar los totales.
5. **Ejemplo con datos de entrada literales y cálculo propio (1.5).** Lámpara LA01 = base B100 (1) + pantalla S100 (1) + conjunto de zócalo A100 (1). Estructura: B100 = 1100 (1) + 1200 (1) + 1300 (1) + 1400 (4); 1100 = 2100 (26); A100 = 1500 (1) + 1600 (1) + 1700 (1); 1500 = 1400 (2); 1700 = 2200 (12) + 2300 (1). Costos de los comprados: 1200 = 9,25; 1300 = 5,00; 1400 = 0,20; 2100 = 0,05; 1600 = 3,50; 2200 = 0,35; 2300 = 0,50; S100 = 4,10. Cálculo propio: 1100 = 26 × 0,05 = 1,30; B100 = 1,30 + 9,25 + 5,00 + 4 × 0,20 = 16,35; 1500 = 2 × 0,20 = 0,40; 1700 = 12 × 0,35 + 0,50 = 4,70; A100 = 0,40 + 3,50 + 4,70 = 8,60; LA01 = 16,35 + 4,10 + 8,60 = 29,05. El buscador reportó 29,05 como costo del tope en la salida de la fuente [S]; coincide. Es solo material (sin ruta ni conversión). Muestra el roll-up puro y que un mismo componente (el tornillo 1400) aparece en dos ramas.
6. **Tarifa por centro de trabajo, estimado y real.** En un sistema abierto el costo por hora del centro y el del empleado son campos distintos; el estimado usa la tarifa del centro y el real la de cada empleado (1.1: "The real cost is calculated using the hourly cost specific to each employee"; ejemplo: con $50/h del centro y $60/h del empleado, el estimado usa 50 y el real 60).
7. **Cuándo se actualiza.** Son dos cosas.
   - El estándar se fija "por lo general al empezar el ejercicio" (OpenStax 8.1, según `sistemas-de-costeo.md`).
   - Recalcular el costo cuando cambian precios o rutas es un acto aparte: un sistema abierto ofrece un botón "Update Cost" y una opción de actualizar el costo de la lista automáticamente (1.2), y otro tiene un botón que resetea el costo del producto "to the expected cost" de la lista, y lleva aparte el costo promedio de las órdenes terminadas (1.1).
   - Sobre la frecuencia, solo hay fuentes secundarias [S] (1.7): la práctica común es una actualización anual con el presupuesto, más frecuente si los costos son volátiles o ante un hecho (suba sostenida de un proveedor, nueva tarifa), y si las variaciones tienden siempre para el mismo lado hay señal de estándares mal fijados. No hay norma que fije la frecuencia.
8. **La norma contable acepta el estándar con una condición.** NIC 2, párrafo 21: el costo estándar "may be used for convenience if the results approximate cost"; "Standard costs take into account normal levels of materials and supplies, labour, efficiency and capacity utilisation" (1.6, extracto del extractor).

### Recurso canónico

- Mecanismo: la documentación de cálculo de costos de la lista de un sistema, con las fórmulas de mano de obra y máquina (1.4) y el ejemplo de dos niveles (1.3). Es práctica de sistemas, no de libro.
- Lógica contable: OpenStax Vol. 2, 8.1 (tarjeta de costo estándar): fijarse en que el estándar se arma con cantidad × precio por elemento.
- Hueco: no hallé un libro abierto con un roll-up multinivel numérico que incluya ruta, mano de obra y carga por tasa.

### Qué registra un sistema

Lista de materiales con cantidades y porcentaje de desecho por componente; ruta con operaciones, centro de trabajo, tiempo de preparación y de corrida, tamaño de lote; tarifa por hora del centro (máquina, mano de obra, carga fabril) con vigencia; costo unitario de cada comprado; corrida del roll-up con fecha y escenario ("Cost Scenario effective 9/1/2020" en 1.3); costo estándar resultante por elemento y por nivel ("Lower Level"/"This Level"); costo promedio real de las órdenes terminadas (1.1). Evidencia: 1.1 a 1.4.

---

## 2. Costo real de la orden y producción en proceso

### Fuentes

| # | Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| 2.1 | OpenStax Vol. 2, 4.3: https://openstax.org/books/principles-managerial-accounting/pages/4-3-use-the-job-order-costing-method-to-trace-the-flow-of-product-costs-through-the-inventory-accounts | primaria (libro abierto) | 3 | 2 | 2 | 2 | [S] |
| 2.2 | OpenStax Vol. 2, 4.5, hoja de costos del trabajo MAC001: https://openstax.org/books/principles-managerial-accounting/pages/4-5-compute-the-cost-of-a-job-using-job-order-costing | primaria | 3 | 2 | 3 | 2 | [S] |
| 2.3 | OpenStax Vol. 2, 4.7, asientos: https://openstax.org/books/principles-managerial-accounting/pages/4-7-prepare-journal-entries-for-a-job-order-cost-system | primaria | 3 | 2 | 3 | 2 | [S] |
| 2.4 | Un sistema abierto (ERPNext), "Work Order": https://docs.frappe.io/erpnext/user/manual/en/work-order | primaria (práctica de sistemas) | 2 | 2 | 1 | 2 | [S] |
| 2.5 | Un sistema abierto (Odoo), "Manufacturing order costs" (la misma que 1.1) | primaria (práctica de sistemas) | 2 | 2 | 3 | 1 | [S] |

### Afirmaciones

1. **La hoja de costos de la orden.** "A job cost sheet is a subsidiary ledger that identifies the individual costs for each job" (2.2). Cada trabajo tiene la suya con materiales, mano de obra y carga fabril; los costos de la requisición de materiales y de los partes de horas se anotan en la hoja, y la carga fabril se asigna desde la cuenta de carga fabril a cada trabajo. El total de las hojas de órdenes abiertas es el saldo de producción en proceso: "the total of all the work in process job cost sheets equals the work in process inventory" (resultado de búsqueda sobre OpenStax 4.5 [S]). Y: "A job order cost system continually updates each job cost sheet as materials, labor, and overhead are added. As a result, all inventory accounts are constantly maintained."
2. **Ejemplo numérico literal (2.2, 2.3).** Trabajo MAC001 (un cartel de vinilo), iniciado el 22/12/2018 y terminado el 22/2/2019. Materiales: vinilo 1 × $300 = $300; tinta negra 2 × $50 = $100; tinta roja 1 × $60 = $60; tinta dorada 1 × $60 = $60; ojales 12 × $10 = $120; madera 40 × $1,50 = $60; total $700. Mano de obra: $66 (hoja: encargado de materiales $15, técnico de impresión $15, ayudantes 2 × $18 = $36; asientos: $30 en producción y $36 en terminación; el total coincide, la partición no). Carga fabril aplicada: $165. Costo total $931 = 700 + 66 + 165. Venta a $2000. Advertencia: la hoja impresa muestra una tasa de $1,50 sobre 66, que daría $99, no $165; $165 / $66 = $2,50, la tasa por peso de mano de obra que usa el capítulo. Si se cita, decir $2,50 y que la hoja impresa tiene un error.
3. **Asientos de la orden (2.3).**
   - Requisición de materiales: debe Producción en proceso 700, haber Inventario de materias primas.
   - Mano de obra directa: debe Producción en proceso, haber Sueldos de fábrica a pagar. Mano de obra indirecta: debe Carga fabril 4000.
   - Carga fabril real: debe Carga fabril 21.000, haber suministros 1500, servicios 7000, amortización 7500, seguros 2917, intereses 2083.
   - Carga fabril aplicada a MAC001: debe Producción en proceso 165, haber Carga fabril 165.
   - Orden terminada: debe Productos terminados 931, haber Producción en proceso 931 ("an entry is made to transfer the total cost from the work in process inventory to the finished goods inventory").
   - Venta: debe Costo de lo vendido 931, haber Productos terminados 931; debe Cuentas a cobrar 2000, haber Ventas 2000.
   - Sobreaplicada o subaplicada: "an adjusting entry is made to dispose of the under- or overapplied overhead"; la página no muestra números (hueco).
4. **Costo de producción terminada.** Es producción en proceso inicial + costos de fabricación del período (materiales, mano de obra, carga fabril) - producción en proceso final: "the costs of all of the units that a company completed and transferred to the finished goods inventory" (2.1 [S]). Con eso y los productos terminados se llega al costo de lo vendido (ver `costo-de-lo-vendido.md`).
5. **Producción en proceso al cierre del período.** Con órdenes, el saldo es la suma de las hojas de órdenes abiertas; no hace falta unidades equivalentes (las de procesos están en `sistemas-de-costeo.md`). El balance argentino la mide distinto (sección 5).
6. **Planeado frente a real en un sistema (2.5).** Muestra el costo estimado ("how much it should cost") y el real ("how much it actually costs"). Antes de empezar, las dos columnas muestran lo mismo; el real se separa si cambian cantidades de componentes, duraciones de operaciones o tarifas del empleado. Ejemplo literal: componentes de un green de golf $50,00, operaciones $15,00, costo de la orden $65,00; las operaciones tardaron diez minutos más y el real subió a $70,00; el costo promedio del producto quedó en $67,50. Otro sistema abierto toma el costo real de operación de las tarjetas de trabajo (Job Cards), permite cargar "Any additional expenses you may have incurred when manufacturing the Item", y para empezar pide transferir las materias primas al depósito de producción en proceso ("you need to Transfer the Raw Materials to initiate the Manufacturing Process"), o saltear ese paso, en cuyo caso los materiales se consideran consumidos al terminar (2.4).

### Recurso canónico

OpenStax Vol. 2, cap. 4, secciones 4.3, 4.5 y 4.7: la hoja del trabajo MAC001 y la secuencia de asientos. Fijarse en que el saldo de producción en proceso es la suma de las hojas abiertas, y en la diferencia entre carga fabril real (la cuenta que acumula) y aplicada (lo que se carga a las órdenes).

### Qué registra un sistema

Orden con estado (pendiente, en proceso, terminada, detenida) y cantidades planeada y producida; consumos reales de materiales por orden y su valor; tiempos reales por operación, centro y empleado; costos adicionales cargados a mano; costo planeado y real por elemento; saldo de la orden en producción en proceso; movimiento de cierre a productos terminados. Evidencia: 2.4 y 2.5.

---

## 3. Variaciones de la orden

### Fuentes

| # | Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| 3.1 | OpenStax Vol. 2, 8.2, materiales: https://openstax.org/books/principles-managerial-accounting/pages/8-2-compute-and-evaluate-materials-variances | primaria | 3 | 2 | 3 | 2 | [S] |
| 3.2 | OpenStax Vol. 2, 8.3, mano de obra: https://openstax.org/books/principles-managerial-accounting/pages/8-3-compute-and-evaluate-labor-variances | primaria | 3 | 2 | 3 | 2 | [S] |
| 3.3 | OpenStax Vol. 2, 8.4, carga fabril: https://openstax.org/books/principles-managerial-accounting/pages/8-4-compute-and-evaluate-overhead-variances | primaria | 3 | 1 | 2 | 2 | [S] |
| 3.4 | OpenStax Vol. 2, 8.5, uso de la variación: https://openstax.org/books/principles-managerial-accounting/pages/8-5-describe-how-companies-use-variance-analysis | primaria | 3 | 2 | 1 | 2 | [S] |
| 3.5 | LibreTexts, Principles of Managerial Accounting (Jonick), 8.04: https://biz.libretexts.org/Bookshelves/Accounting/Principles_of_Managerial_Accounting_(Jonick)/08%3A_Variance_Analysis/8.04%3A_Factory_overhead_variances | primaria (libro abierto) | 2 | 2 | 3 | 2 | [S] |

3.1 a 3.4 son un solo libro. Para la variación de volumen (que OpenStax 8.4 no nombra ni calcula) la única fuente con números es 3.5.

### Afirmaciones

1. **Materiales (3.1).** Precio: (precio real - precio estándar) × cantidad real; cantidad: (cantidad real usada - cantidad estándar para lo producido) × precio estándar. Ejemplo literal, Biglow Company (estándar 8 onzas a $0,85 por onza; 11.000 botellas; 89.000 onzas compradas por $74.760): precio real $0,84; variación de precio $890 favorable; variación de cantidad $850 desfavorable (89.000 onzas usadas frente a 88.000 estándar); total $40 favorable. Dato clave: "the material price variance is computed at the time of purchase and not when the material is used in production": la de precio es de compras, no de la orden.
2. **Mano de obra (3.2).** Tarifa: (tarifa real - tarifa estándar) × horas reales; tiempo (la que otros llaman eficiencia): (horas reales - horas estándar) × tarifa estándar. Ejemplo literal, Biglow (estándar 1,5 horas a $35 por botella; 11.000 botellas; real 16.000 horas por $565.600): tarifa real $35,35; horas estándar 16.500; tarifa ($35,35 - $35,00) × 16.000 = $5.600 desfavorable; tiempo (16.000 - 16.500) × $35 = $17.500 favorable; total $11.900 favorable (cuenta del extractor; la solución impresa del libro rotula el total como desfavorable y muestra $5.650 en una celda, inconsistente; real $565.600 frente a estándar $577.500). Causas que cita: oferta y demanda de trabajadores, convenios, otro nivel de calificación (tarifa); mejoras de eficiencia o "carelessness or inefficiencies in production, or poor estimation when creating the standard usage" (tiempo).
3. **Carga fabril variable (3.3).** Tasa o gasto: (tasa variable real - estándar) × horas reales; eficiencia o controlable: (horas reales - horas estándar) × tasa variable estándar. Ejemplo literal, Connie's Candy: tasa estándar $4.000 / 2.000 horas = $2,00; real $7.000 / 2.500 horas = $2,80; tasa $2.000 desfavorable; eficiencia (2.500 - 2.000) × $2,00 = $1.000 desfavorable; total $3.000 desfavorable. La fuente: "Often, explanation of this variance will need clarification from the production supervisor".
4. **Volumen o capacidad de la carga fija (3.5).** "the difference between the budgeted fixed overhead at normal capacity and the standard fixed overhead for the actual units produced"; fórmula (horas estándar a capacidad normal - horas estándar de lo producido) × tasa fija. Ejemplo literal: fija presupuestada $70.000 sobre 10.000 horas de capacidad normal, tasa $7 por hora; producción 8.000 unidades de 1 hora; "Fixed factory overhead volume variance = (10,000 – 8,000) x $7 per direct labor hour = $14,000", desfavorable; con 11.000 unidades queda ($7.000), favorable. "The 8,000 standard hours are less than the 10,000 available at normal capacity, so the fixed overhead was underutilized." Es la contracara de la ociosidad que la norma argentina deja fuera del costo (sección 4). OpenStax 8.4 menciona dos variaciones de la carga fija ("One variance determines if too much or too little was spent... The other variance computes whether or not actual production was above or below the expected production level") sin nombrarlas ni calcularlas.
5. **Gasto de la carga fija (budget/spending).** Ninguna fuente que leí la define con fórmula y números (hueco). Qué es: carga fija real menos presupuestada, por inferencia de 3.3.
6. **Cuáles son de la orden y cuáles del período (inferencia propia sobre 3.1 a 3.5).** De la orden, porque dependen de lo que ella consumió: uso (cantidad) de material, eficiencia de mano de obra y eficiencia de la carga variable. Del período: precio de material (se mide al comprar, 3.1), tarifa de mano de obra, tasa o gasto de carga fabril y volumen o capacidad (depende de cuánto se produjo en total frente a la capacidad normal). Las fuentes no usan esta división.
7. **Quién las mira (3.4).** "the management responsible for the variances must explain any variances outside of a certain range." Algunas empresas piden explicar solo las desfavorables, otras las dos; explicar las favorables permite ver si son sostenibles. No hay umbrales numéricos. Hay advertencia de "manage to the variances" y se recomienda medir con más de un indicador. Para la carga variable, el supervisor de producción (3.3). Asignar precio a compras y uso a producción es inferencia.

### Recurso canónico

OpenStax Vol. 2, cap. 8, secciones 8.2 a 8.5 (esquema de cuatro variaciones y ejemplos de Biglow); para la variación de volumen, LibreTexts Jonick 8.04. Fijarse en que las variaciones de la orden se calculan contra las cantidades estándar para lo producido, no contra el presupuesto de entrada.

### Qué registra un sistema

Cantidades y precios estándar por elemento (sección 1) y reales (sección 2); horas estándar permitidas para la producción real; tarifa estándar del centro; capacidad normal en horas. Variación por orden y elemento con signo y causa. Evidencia de sistema: el costo estimado y el real de la orden (2.5) y los registros por operación (2.4). Ninguna de las documentaciones abiertas que leí calcula variaciones con nombre: lo anterior es inferencia.

---

## 4. Mermas, rechazos y reproceso en el costo (normal frente a anormal)

### Fuentes

| # | Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| 4.1 | Resolución Técnica 17 FACPCE, texto ordenado junio 2003 (Consejo Profesional de CABA), secciones 4.2.6 y 5.5: https://www.consejo.org.ar/storage/attachments/RT_FACPCE17_TO2003.pdf-bGCewZIHs8.pdf | primaria (norma) | 3 | 3 | 1 | 3 | [L] de 4.2.6 y 5.5 |
| 4.2 | NIC 2, párrafos 10 a 14: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html | primaria (norma) | 3 | 2 | 1 | 2 | [S] |
| 4.3 | Dummies, "Cost Accounting: Job Costs for Spoilage, Reworked Products, and Scrap": https://www.dummies.com/article/business-careers-money/business/accounting/general-accounting/cost-accounting-job-costs-for-spoilage-reworked-products-and-scrap-164765 | secundaria (divulgación) | 1 | 1 | 1 | 1 | [S] |
| 4.4 | Iowa State (ISUDP), curso de contabilidad de gestión: https://iastate.pressbooks.pub/isudp-2025-202/?p=23 | secundaria | 2 | 2 | 2 | 1 | [S] del buscador (la página dio 403) |
| 4.5 | Un sistema abierto (ERPNext), BOM y Work Order (1.2, 2.4) | primaria (práctica de sistemas) | 2 | 1 | 1 | 2 | [S] |
| 4.6 | OpenStax Vol. 2, definiciones del cap. 5: https://openstax.org/books/principles-managerial-accounting/pages/5-key-terms | primaria | 3 | 1 | 1 | 1 | [S] |

### Afirmaciones

1. **Argentina, norma primaria (4.1, [L]).** RT 17, 4.2.6, "Bienes producidos": "El costo de un bien producido es la suma de: a) los costos de los materiales e insumos necesarios para su producción; b) sus costos de conversión (mano de obra, servicios y otras cargas), tanto variables como fijos; c) los costos financieros que puedan asignárseles de acuerdo con las normas de la sección 4.2.7 (Costos financieros)." Y: "El costo de los bienes producidos no debe incluir la porción de los costos ocasionados por: a) improductividades físicas o ineficiencias en el uso de los factores en general; b) la ociosidad producida por la falta de aprovechamiento de los factores fijos originada en la no-utilización de la capacidad de planta a su "nivel de actividad normal"." Y: "Los importes correspondientes a cantidades anormales de materiales, mano de obra u otros costos de conversión desperdiciados, razonablemente determinables y que distorsionen el costo de los bienes producidos, no participarán en su determinación y deben ser reconocidos como resultados del período." Y: "El "nivel de actividad normal" es el que corresponde a la producción que se espera alcanzar como promedio de varios períodos bajo las circunstancias previstas, de modo que está por debajo de la capacidad total y debe considerarse como un indicador realista y no como un objetivo ideal."
2. **NIC 2 (4.2, [S]).** Párrafo 12: los costos de conversión incluyen "a systematic allocation of fixed and variable production overheads". Párrafo 13: "The allocation of fixed production overheads to the costs of conversion is based on the normal capacity" y "Unallocated overheads are recognised as an expense in the period in which they are incurred." Las dos normas coinciden en el núcleo: la carga fija se absorbe al nivel normal y lo no absorbido va a resultados. Los párrafos de NIC 2 que excluyen expresamente los desperdicios anormales (16 a 18) no los leí en esta ronda: la afirmación de que NIC 2 los excluye queda sin verificar (la RT 17 sí lo dice literal).
3. **Normal frente a anormal en el costeo por órdenes (4.3, 4.4 [S]).** Normal: "Normal spoilage is expected under the best of circumstances. The cost is included in cost of manufacturing, and it's part of job costing." Anormal: "Abnormal spoilage produces more defects than you would expect from normal production"; "Those costs are posted to a loss account"; no son parte del costo de fabricar o terminar el trabajo; el ajuste saca el costo de producción en proceso y lo lleva a pérdida. Sobre dónde se carga la normal las fuentes que mostró el buscador dan dos tratamientos: a la orden que la causó (neta del valor de venta del desecho) o repartida a todas las órdenes por la tasa de carga fabril. Parece depender del origen: propia de la orden o del proceso en general. El retrabajo sigue la misma división (normal a carga fabril, anormal a pérdida, pedido por el cliente a la orden) [S, sin fuente primaria].
4. **Cómo se separa lo anormal de lo normal.** Con una tasa normal definida de antemano. La RT 17 solo pide que la cantidad anormal sea "razonablemente determinable" y distorsione el costo; no fija un porcentaje. El buscador dio una fórmula de ejemplo (costo unitario sobre unidades buenas más pérdida normal, por las anormales) [S, sin números].
5. **Cómo lo refleja el estándar (inferencia propia).** La merma normal es parte del costo estándar: "Qty. Required * (1 + Scrap Factor)" (1.4), y un sistema abierto la guarda por componente ("each raw material row also has a scrap percentage", 1.2). Lo que pasa de ese porcentaje aparece como variación de cantidad de material (sección 3). Es decir, la merma normal es parte del estándar y la anormal es la variación.
6. **Desecho que se vende y subproducto.** Un sistema abierto lleva el residuo a un ítem de desecho con depósito propio y, si es el mismo producto que se fabrica, lo trata como "Process Loss Item" y resta su cantidad de la cantidad fabricada; un desecho puede tener tarifa "if it is a by-product and not waste" (1.2, 2.4). NIC 2 párr. 14: "Most by-products, by their nature, are immaterial." El subproducto y la declaración de merma son de Ejecución en planta; acá solo se marca la frontera.

### Recurso canónico

RT 17, sección 4.2.6 (texto ordenado de 2003 del Consejo de CABA). Fijarse en que la norma separa tres cosas que el campo suele mezclar: improductividad o ineficiencia, ociosidad bajo el nivel normal y cantidades anormales desperdiciadas; las tres van a resultados. Para el mecanismo de la orden no hallé un libro abierto con números (ver huecos).

### Qué registra un sistema

Porcentaje de merma por componente y operación (el estándar); merma real por orden (cantidad rechazada por operación y motivo); diferencia real menos normal (la parte anormal); destino del desecho (depósito de desecho, valor de recupero, subproducto); orden de retrabajo vinculada a la original con su costo adicional (y quién lo paga). Evidencia: 1.2 y 2.4.

---

## 5. Contexto argentino

- RT 17 FACPCE 4.2.6 [L]: costo de bien producido = materiales e insumos + conversión (variable y fija) + costos financieros asignables; quedan afuera improductividades, ociosidad bajo el nivel normal y cantidades anormales (cita en la sección 4).
- RT 17 5.5.3 [L]: bienes de cambio en producción o construcción mediante un proceso prolongado, a valor neto de realización proporcionado al grado de avance si se cumplen cuatro condiciones (anticipos que fijan precio; contrato que asegura la venta; capacidad financiera para terminar; certidumbre de la ganancia). "En los restantes casos, se utilizará el costo de reposición de los bienes con similar grado de avance de la producción o construcción, tomado de un mercado activo o, si esto no fuera posible, su costo de reproducción", que se determina con la sección 4.2.6 "y los métodos habitualmente seguidos por el ente para aplicarlas"; "Si la obtención del costo de reproducción fuera imposible o impracticable, se usará el costo original." Para bienes de cambio en general (5.5.4): costo de reposición, o el original si no se puede. Consecuencia: el costo acumulado de las órdenes es la base, no el valor de balance, de la producción en proceso argentina.
- Una sola fuente primaria (la norma, texto de 2003). Fuentes secundarias vistas solo en el buscador [S]: un artículo de la UNLPam sobre ociosidad (https://ojs.unlpam.edu.ar/index.php/perspectivas/article/download/3648/3759), el informe 14 del CENCyA-FACPCE con un ejemplo de asignación de fijos al nivel normal (https://www.facpce.org.ar/pdf/informe-14-cencya.pdf; no lo leí, es el mejor candidato para un ejemplo numérico argentino) y un trabajo de la UNMdP (https://nulan.mdp.edu.ar/4020/1/rondi-etal-2023.pdf; el PDF no se pudo leer) que según el buscador dice que la norma unificada (RT 54) no admite el valor neto de realización para bienes en proceso o producidos. El texto vigente (RT 54 con RT 59, y las modificaciones a la 17) hay que confirmarlo en el sitio de la FACPCE antes de citar como vigente.

---

## 6. Sobre la división del árbol

El árbol del brief encaja con cómo el campo divide Costos, con tres ajustes:
- Mermas, rechazos y reproceso el campo los trata como un tema propio (spoilage, rework, scrap, capítulo aparte en los libros de costos) y la norma argentina los trata dentro del costo de producción. Conviene un apartado propio en Costos, enlazado a Calidad (no conformidad y disposición) y a Ejecución en planta (declaración de merma y subproducto).
- Las variaciones mezclan dos tipos: de la orden (uso, eficiencia) y del período (precio, tarifa, volumen). Los libros las enseñan juntas por la fórmula, pero un sistema las calcula en momentos distintos (compra, orden, cierre); conviene explicarlo así.
- Producción en proceso con órdenes es un saldo (suma de hojas abiertas); con procesos, unidades equivalentes (ya en `sistemas-de-costeo.md`). En Producción corresponde la primera.

---

## 7. Huecos

1. Sin ejemplo numérico literal de roll-up estándar con material, mano de obra por tasa de centro y carga fabril en un libro de texto. El mejor (1.3) es de un sistema comercial y usa un porcentaje del material como carga; el de SAS (1.5) es solo material y el resultado es cálculo propio.
2. Sin números de sobreaplicada o subaplicada ni de su cierre (OpenStax 4.4 no cargó; 4.7 la nombra sin cifras).
3. Sin definición con números de la variación de gasto de la carga fija: OpenStax 8.4 no la calcula, Jonick 8.04 no la define. Las fuentes que el buscador mostró (Saylor 10.8, Lumen, ACCA, CPA Ireland) no se abrieron.
4. Sin fuente primaria abierta con números de merma normal y anormal ni de retrabajo en órdenes. Horngren, cap. 18 "Spoilage, Rework, and Scrap": solo hallé copias no oficiales (Scribd, pdfcoffee) y diapositivas; no las usé. Iowa State dio 403.
5. NIC 2 párrafos 16 a 18 sin leer; solo 10 a 14 y 21 vía extractor, con citas acortadas.
6. RT 17 leída en el texto ordenado de 2003; no verifiqué el texto vigente. Falta la segunda fuente independiente que el brief pide para ley: el informe 14 del CENCyA es el candidato.
7. Sin umbrales para investigar variaciones (OpenStax dice que cada empresa fija un rango) y sin evidencia de cuántas empresas actualizan el estándar cada año: la frecuencia anual es [S] de consultoras.
8. Ningún sistema abierto leído calcula variaciones con nombre (muestran estimado frente a real): lo que registra un sistema para variaciones es inferencia.
9. La URL de OpenStax 8.1 no cargó en esta ronda y la tarjeta de costo estándar no se releyó; verificar las URLs de OpenStax antes de citarlas (las de cap. 8 de esta ronda se hallaron por buscador).
