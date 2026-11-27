# Contabilidad de gestión: informe de investigación

Fecha de la investigación: 2026-11-27. Ángulo: la vertical Contabilidad de gestión (management accounting) de la base sobre Contabilidad. Lector: quien construye software de gestión; en segundo lugar quien lo vende o implementa.

## Cómo leer las marcas y los puntajes

Marcas de lectura:

- **[L]** leí el texto completo (o el cuerpo entero) del documento, bajado y convertido a texto por mí. Las citas literales son de ese texto.
- **[L~]** abrí la página, pero la herramienta de lectura la pasó por un extractor automático que devolvió pasajes y cifras. Las citas son literales según el extractor; no vi la página entera. Conviene releerla antes de citar en la nota final.
- **[M]** solo metadatos o abstract.
- **[S]** solo un resumen del buscador o secundario.

Puntajes de 1 a 3: A = autoridad, P = profundidad, E = ejemplos, U = unicidad (qué aporta que otra fuente de la lista no aporte). Tipo: primaria (P) o secundaria (S).

Convención: cuando digo «OpenStax» me refiero al libro *Principles of Accounting, Volume 2: Managerial Accounting* (el dominio es `openstax.org/books/principles-managerial-accounting/pages/...`; el título del libro en el sitio no es *Principles of Managerial Accounting* a secas). Es una sola fuente aunque aparezca en muchas filas: es un mismo libro, y las páginas «Summary», «Key Terms» y los problem sets no cuentan como fuentes aparte.

Aviso sobre el dato web: todo lo traído de la web es dato. En los resultados del buscador aparecieron fragmentos de claves de respuestas que contradicen el texto del capítulo (uno decía que los reportes gerenciales deben cumplir GAAP); los descarté y me quedé con el texto del capítulo.

---

## 0. Veredicto sobre el árbol propuesto

El árbol (contabilidad-de-gestion, costos-y-costeo, punto-de-equilibrio, presupuesto, centros-de-costo) **coincide en lo grueso con cómo el campo divide la vertical**, pero con tres desajustes que conviene decidir antes de escribir.

Cómo lo divide el libro de texto que más pesa (OpenStax, índice por capítulos, verificado en las URL de cada sección):

| Cap. OpenStax | Tema | Nota del árbol propuesto |
|---|---|---|
| 1 | Qué es la contabilidad de gestión y en qué se diferencia de la financiera | contabilidad-de-gestion |
| 2 | Conceptos básicos: comportamiento y clasificación de costos | costos-y-costeo |
| 3 | Costo-volumen-utilidad (CVP): margen de contribución, equilibrio, margen de seguridad, mezcla | punto-de-equilibrio |
| 4 | Costeo por órdenes | costos-y-costeo |
| 5 | Costeo por procesos | costos-y-costeo |
| 6 | Asignación de costos indirectos, ABC, absorción frente a variable | costos-y-costeo |
| 7 | Presupuestos (maestro, estático, flexible, base cero) | presupuesto |
| 8 | Costos estándar y variaciones | costos-y-costeo (o presupuesto) |
| 9 | Centros de responsabilidad, precios de transferencia | centros-de-costo |
| 10 | Decisiones con costos relevantes (aceptar un pedido especial, hacer o comprar) | **no está en el árbol** |
| 12 | Medición del desempeño (en el sitio aparece «12.1 Explain the Importance of Performance Measurement») | **no está en el árbol** |

Desajustes, para decidir:

1. **`costos-y-costeo` es la nota sobrecargada.** Junta clasificación de costos (cap. 2), tres sistemas de acumulación (órdenes, procesos, ABC), dos métodos de tratar el costo fijo (absorción y variable) y el costeo estándar con sus variaciones. El campo las trata en cuatro capítulos distintos (2, 4–5, 6, 8). Propongo dividir en dos notas: una de **clasificación de costos** (la base de todo, la lee cualquiera) y una de **sistemas de costeo** (órdenes, procesos, absorción frente a variable, estándar, ABC). Alternativa mínima: dejarla entera pero con las capas internas bien separadas.
2. **Las variaciones del estándar y el análisis de desvíos del presupuesto son lo mismo.** OpenStax las trata en dos capítulos (8, y 7.5), pero el mecanismo es el mismo: real contra esperado, separado en efecto precio y efecto cantidad (o volumen y eficiencia). Hay que elegir una dueña. Propongo que el análisis de desvíos viva en `presupuesto` y que `costos-y-costeo` solo defina el costo estándar y enlace.
3. **Faltan dos temas del campo:** las **decisiones con costos relevantes** (cap. 10: pedido especial, hacer o comprar, cerrar un segmento) y la **medición del desempeño** (cap. 12; Balanced Scorecard, ROI, valor económico agregado). Para quien construye software de gestión, los costos relevantes son probablemente más útiles que ABC. No los pedís; los marco como hueco de alcance, no como error.

Una observación sobre `punto-de-equilibrio`: el campo no lo trata como tema propio sino como una herramienta del CVP, que a su vez depende de la clasificación fijo/variable. La nota puede existir con ese nombre (es el que busca la gente), pero en el cuerpo conviene decir que es la «punta» del costo-volumen-utilidad y enlazar a costos-y-costeo para la clasificación.

---

## 1. contabilidad-de-gestion (entrada)

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 1.1 | OpenStax, 1.2 «Distinguish between Financial and Managerial Accounting» | https://openstax.org/books/principles-managerial-accounting/pages/1-2-distinguish-between-financial-and-managerial-accounting | P (libro de texto) | 3 | 2 | 1 | 2 | [L~] |
| 1.2 | AICPA y CIMA, *Global Management Accounting Principles* (PDF, copia hospedada en eclass.aueb.gr; el original está en aicpa-cima.com, no lo verifiqué) | https://eclass.aueb.gr/modules/document/file.php/LOXR285/Yliko_Peraitero_Meletis/global-management-accounting-principles.pdf | P (marco profesional) | 3 | 2 | 1 | 3 | [L] parcial (leí la definición y los cuatro principios, no las 140 000 caracteres) |
| 1.3 | Accounting Today, «IMA redefines management accounting» (12-dic-2008) | https://www.accountingtoday.com/news/ima-redefines-management-accounting | S (noticia sobre la definición de IMA) | 2 | 1 | 1 | 2 | [L~] |
| 1.4 | Kaplan, «One Cost System Isn't Enough», HBR, enero de 1988 (copia PDF en eclass.aueb.gr) | https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf | P | 3 | 2 | 2 | 3 | [L] |
| 1.5 | Johnson y Kaplan, *Relevance Lost: The Rise and Fall of Management Accounting* (HBS Press, 1987), registros de catálogo | https://libcat.library.tamu.edu/Record/in00000583263/Description | P (el libro), pero yo solo vi el catálogo | 3 | — | — | 3 | [M] |
| 1.6 | strategy+business, artículo sobre *Relevance Lost* | http://www.strategy-business.com/article/11409 | S | 2 | 1 | 1 | 1 | [L~] |
| 1.7 | CIMA, *Management Accounting: Official Terminology* (2.ª ed., Eaton, 2005) | https://shop.elsevier.com/books/management-accounting-official-terminology/eaton/978-0-7506-6827-9 | P, pero solo la ficha de venta | 3 | — | — | 2 | [M] |

### Afirmaciones (cada una con su URL)

**Para quién informa y por qué no tiene normas obligatorias**

- La información gerencial «is gathered and reported for a more specific purpose for internal users»; la financiera «tends to be used primarily by external users». https://openstax.org/books/principles-managerial-accounting/pages/1-2-distinguish-between-financial-and-managerial-accounting
- «financial accounting is governed by rules set out by the Financial Accounting Standards Board» y «Managerial accounting is not governed by GAAP». https://openstax.org/books/principles-managerial-accounting/pages/1-2-distinguish-between-financial-and-managerial-accounting
- Orientación temporal: «managerial accounting focuses more on the future» frente a «financial accounting focuses on reporting what has already happened». https://openstax.org/books/principles-managerial-accounting/pages/1-2-distinguish-between-financial-and-managerial-accounting
- Detalle y verificación: «Managerial accounting has a more specific focus, and the information is more detailed and timelier.» y, para los reportes: «Financial reports rely on structure.» frente a «There are no rules, guidelines, or principles to follow.» y «no independent audits». https://openstax.org/books/principles-managerial-accounting/pages/1-2-distinguish-between-financial-and-managerial-accounting
- Kaplan (1988) da la explicación estructural de por qué no hay norma y por qué eso importa: los sistemas de costos tienen que atender tres funciones distintas, y la primera es la única regulada: «Inventory valuation for financial and tax statements, allocating periodic production costs between goods sold and goods in stock», «Operational control, providing feedback to production and department managers on the resources consumed (labor, materials, energy, overhead) during an operating period» e «Individual product cost measurement». https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf
- Y la consecuencia: «And when compromises have to be made, the demands of the financial reporting function (inventory valuation) invariably triumph. The more managerially relevant functions of operational control and product costing usually suffer.» y «No single system can adequately cover all three functions. The demands of each differ in terms of reporting frequency, degree of allocation, nature of cost variability, system scope, and degree of objectivity». https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf
- Sobre la regla de reparto de la contabilidad financiera: «Financial accounting principles do not require that assigned overhead costs be causally related to the demands of individual products, so many companies continue to use direct labor to allocate overhead, even though direct labor may account for less than 5% of total manufacturing costs.» https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf

**Definiciones oficiales (dos, y no coinciden en el énfasis)**

- AICPA y CIMA (GMAP): «Management accounting is the sourcing, analysis, communication and use of decision-relevant financial and non-financial information to generate and preserve value for organisations.» https://eclass.aueb.gr/modules/document/file.php/LOXR285/Yliko_Peraitero_Meletis/global-management-accounting-principles.pdf
- Los cuatro principios del mismo documento: «Communication provides insight that is influential», «Information is relevant», «Impact on value is analysed», «Stewardship builds trust». https://eclass.aueb.gr/modules/document/file.php/LOXR285/Yliko_Peraitero_Meletis/global-management-accounting-principles.pdf
- IMA (definición publicada el 12-dic-2008, elaborada por un subcomité de la Foundation for Applied Research): «Management accounting is a profession that involves partnering in management decision-making, devising planning and performance management systems, and providing expertise in financial reporting and control to assist management in the formulation and implementation of an organization's strategy.» https://www.accountingtoday.com/news/ima-redefines-management-accounting
- **Discrepancia a dar en la nota:** la de IMA define una *profesión* (y mete «financial reporting and control» dentro de lo que sabe el contador de gestión); la de AICPA/CIMA define una *actividad* sobre información «decision-relevant» y habla de «value». La primera pone el acento en quien lo hace y en la estrategia; la segunda, en la información y en la decisión. Para esta base conviene la segunda, porque es la que habla de información.
- La definición de CIMA en la *Official Terminology* de 2005 (que habla de «create, protect, preserve and increase value») solo la vi citada por terceros; no la verifiqué en el texto. https://shop.elsevier.com/books/management-accounting-official-terminology/eaton/978-0-7506-6827-9 [M]. Ver huecos.

**Historia y crítica (por qué existe una norma implícita de «lo que sirve» y por qué se discutió)**

- *Relevance Lost* (Harvard Business School Press, Boston, 1987, xiii + 269 pp., ISBN 0875841384) es el libro de Johnson y Kaplan. https://libcat.library.tamu.edu/Record/in00000583263/Description [M]
- Resumen secundario de su tesis, según un comentarista: todo lo significativo de la contabilidad de gestión estadounidense «was known by 1925 and, thus, with the passage of six decades, had lost its relevance» (no pude fijar la fuente primaria de esta cita; viene del buscador). Ver huecos. [S]
- strategy+business lo describe así: la contabilidad de costos «had become poisonously destructive to its hosts», y «The net effect was to make managers more dependent on the numbers.» http://www.strategy-business.com/article/11409 [L~]

### Ejemplo con números

No hay un ejemplo numérico natural para una nota de entrada; el que más sirve es el de Kaplan (1988) de dos empresas que ilustran las tres funciones, pero no trae cifras. Lo que sí trae cifras es el contraste financiera/gestión en la nota de costeo (ver sección 2, ejemplo de Outdoor Nation: el mismo año da $3 000 de resultado con absorción y $0 con costeo variable). Recomiendo usar ese como ejemplo de entrada: muestra con números que «dos informes legítimos, dos resultados distintos».

### Recurso canónico

**OpenStax, sección 1.2** (https://openstax.org/books/principles-managerial-accounting/pages/1-2-distinguish-between-financial-and-managerial-accounting): la tabla de contrastes en lenguaje llano. Fijarse en: la frase «not governed by GAAP», que es la respuesta directa a «por qué no tiene normas obligatorias». Complemento obligatorio: **Kaplan 1988** (HBR), el apartado de las tres funciones, que explica *por qué* conviene tener más de un sistema. Y la definición de **GMAP** para citar «decision-relevant».

---

## 2. costos-y-costeo

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 2.1 | OpenStax 2.2 «Identify and Apply Basic Cost Behavior Patterns» | https://openstax.org/books/principles-managerial-accounting/pages/2-2-identify-and-apply-basic-cost-behavior-patterns | P | 3 | 2 | 3 | 2 | [L~] |
| 2.2 | OpenStax 4.1 «Distinguish between Job Order Costing and Process Costing» | https://openstax.org/books/principles-managerial-accounting/pages/4-1-distinguish-between-job-order-costing-and-process-costing | P | 3 | 2 | 2 | 2 | [L~] |
| 2.3 | OpenStax 5.3 «Equivalent Units … Initial Processing Stage» | https://openstax.org/books/principles-managerial-accounting/pages/5-3-explain-and-compute-equivalent-units-and-total-cost-of-production-in-an-initial-processing-stage | P | 3 | 3 | 3 | 2 | [L~] |
| 2.4 | OpenStax 6.5 «Compare and Contrast Variable and Absorption Costing» | https://openstax.org/books/principles-managerial-accounting/pages/6-5-compare-and-contrast-variable-and-absorption-costing | P | 3 | 3 | 3 | 2 | [L~] |
| 2.5 | OpenStax 6.3 «Calculate Activity-Based Product Costs» y 6.4 «Compare and Contrast Traditional and ABC Systems» | https://openstax.org/books/principles-managerial-accounting/pages/6-3-calculate-activity-based-product-costs ; https://openstax.org/books/principles-managerial-accounting/pages/6-4-compare-and-contrast-traditional-and-activity-based-costing-systems | P | 3 | 3 | 3 | 2 | [L~] |
| 2.6 | OpenStax 8.1 «How and Why a Standard Cost Is Developed» y 8.2 «Materials Variances» | https://openstax.org/books/principles-managerial-accounting/pages/8-1-explain-how-and-why-a-standard-cost-is-developed ; https://openstax.org/books/principles-managerial-accounting/pages/8-2-compute-and-evaluate-materials-variances | P | 3 | 3 | 3 | 2 | [L~] |
| 2.7 | Kaplan y Anderson, «Time-Driven Activity-Based Costing», HBR, nov. 2004 (copia PDF en cours.univ-paris1.fr) | https://cours.univ-paris1.fr/pluginfile.php/2483984/mod_resource/content/2/Kaplan%20Anderson%202004%20hbr.pdf | P | 3 | 3 | 3 | 3 | [L] |
| 2.8 | Kaplan, «One Cost System Isn't Enough», HBR, ene. 1988 | (la misma de 1.4) | P | 3 | 2 | 2 | 3 | [L] |
| 2.9 | Cooper y Kaplan, «Measure Costs Right: Make the Right Decisions», HBR, sep.–oct. 1988, pp. 96–103 (ficha de HBR) | https://store.hbr.org/product/measure-costs-right-make-the-right-decisions/88503 | P, solo la ficha | 3 | — | — | 3 | [M] |
| 2.10 | Kaplan y Cooper, *Cost & Effect* (HBS Press, 1998, xi + 357 pp., ISBN 0875847889), catálogo | https://libcat.library.tamu.edu/Record/in00001407786/Description | P, solo el catálogo | 3 | — | — | 3 | [M] |
| 2.11 | IMA, SMA «The Conceptual Framework for Managerial Costing» (2014) y «Developing an Effective Managerial Costing Model» (2019) | https://www.imanet.org/newsletters/inside-ima/2019/may/new-sma-proposes-a-more-effective-managerial-costing-model | P, solo la noticia | 2 | — | — | 3 | [S] |

### Afirmaciones (cada una con su URL)

**Clasificación**

- Costo fijo: «an unavoidable operating expense that does not change in total over the short term». Variable: «varies in direct proportion to the level of activity within the business». Mixto: «Mixed costs are those that have both a fixed and variable component.» Rango relevante: «a specific activity level that is bounded by a minimum and maximum amount». https://openstax.org/books/principles-managerial-accounting/pages/2-2-identify-and-apply-basic-cost-behavior-patterns
- Directo e indirecto, de producto y del período: la búsqueda indica que OpenStax trata materiales y mano de obra directos como rastreables al producto y los indirectos como parte de la carga fabril (manufacturing overhead), y los costos del período como los que se gastan cuando se incurren (por ejemplo ventas y administración). Esto lo vi solo en un resumen del buscador; no abrí 4.2 ni el glosario del capítulo 2. https://openstax.org/books/principles-managerial-accounting/pages/4-2-describe-and-identify-the-three-major-components-of-product-costs-under-job-order-costing [S]
- Matiz que hay que dar en la nota: el mismo costo puede clasificarse distinto según para qué se use el dato (resumen de la sección 2.2, vía buscador). https://openstax.org/books/principles-managerial-accounting/pages/2-2-identify-and-apply-basic-cost-behavior-patterns [S]

**Órdenes y procesos**

- Órdenes: «Job order costing is an accounting system that traces the individual costs directly to a final job or service»; industrias de ejemplo: producción de películas, imprentas, agencias de publicidad, constructoras, y también estudios contables, consultoras y talleres. Procesos: «costs are accounted for by the production process or production department instead of by the product or by the job»; ejemplos: golf balls de Titleist, cereales de Kellogg's, helados Turkey Hill, nafta de CITGO. https://openstax.org/books/principles-managerial-accounting/pages/4-1-distinguish-between-job-order-costing-and-process-costing
- Unidades equivalentes: «The equivalent unit computation determines the number of units» «if each is manufactured in its entirety before manufacturing the next unit.» https://openstax.org/books/principles-managerial-accounting/pages/5-3-explain-and-compute-equivalent-units-and-total-cost-of-production-in-an-initial-processing-stage

**Absorción frente a variable**

- Variable: «a method in which all variable costs (direct material, direct labor, and variable overhead) are assigned to a product», y «fixed overhead costs are expensed in the period incurred». Absorción: «a method that applies all direct costs, fixed overhead, and variable manufacturing overhead to the cost of the product». https://openstax.org/books/principles-managerial-accounting/pages/6-5-compare-and-contrast-variable-and-absorption-costing
- Por qué dan resultados distintos con stock: según el extractor, el texto explica que cuando la producción supera a las ventas, la utilidad con costeo variable es menor porque con absorción parte del costo fijo queda en el inventario final; al revés cuando se vende más de lo que se produce; y que con el tiempo la diferencia tiende a cero. (Resumen del buscador; el ejemplo de abajo lo confirma numéricamente.) https://openstax.org/books/principles-managerial-accounting/pages/6-5-compare-and-contrast-variable-and-absorption-costing [S]
- Con absorción el gerente puede mover resultado produciendo de más (lo dice el resumen del buscador sobre el mismo capítulo); y el costeo variable no cumple GAAP pero sirve para CVP. https://openstax.org/books/principles-managerial-accounting/pages/6-5-compare-and-contrast-variable-and-absorption-costing [S]

**Costeo estándar y variaciones**

- «A standard cost is an expected cost that a company usually establishes at the beginning of a fiscal year». Estándar ideal: «An ideal standard level is set assuming that everything is perfect» (poco realista); alcanzable: «an attainable standard, which is one that employees can reach with reasonable effort». https://openstax.org/books/principles-managerial-accounting/pages/8-1-explain-how-and-why-a-standard-cost-is-developed
- Fórmulas: «Direct Materials Price Variance equals (Actual Price per Unit of Materials minus Standard Price per Unit of Materials) times Actual Quantity of Materials Used.» y «Direct Materials Quantity Variance equals (Actual Quantity of Materials Used for Units Produced minus Standard Quantity of Materials Expected for the Units Produced) times Standard Price.» https://openstax.org/books/principles-managerial-accounting/pages/8-2-compute-and-evaluate-materials-variances

**ABC y su crítica**

- «Activity-based costing (ABC) is the process that assigns overhead to products based on the various activities that drive overhead costs.» https://openstax.org/books/principles-managerial-accounting/pages/6-3-calculate-activity-based-product-costs
- Ventajas según OpenStax: «There are multiple overhead cost pools, and each has its own unique measure of activity.»; «Both nonmanufacturing costs and manufacturing costs may be assigned to products.» Límites: «It is more expensive, as there is a cost to collect and analyze cost driver information»; «An ABC system takes much more to implement and operate»; y que los efectos son asimétricos: «there is usually a larger change in the per-unit costs of the low-volume products.» Además, la empresa sigue necesitando el costo tradicional para los estados contables. https://openstax.org/books/principles-managerial-accounting/pages/6-4-compare-and-contrast-traditional-and-activity-based-costing-systems
- La crítica de Kaplan al propio ABC (2004): «Many companies abandoned activity-based costing because it did not capture the complexity of their operations, took too long to implement, and was too expensive to build and maintain.» https://cours.univ-paris1.fr/pluginfile.php/2483984/mod_resource/content/2/Kaplan%20Anderson%202004%20hbr.pdf
- Escala del problema, con cifras: en la operación de brokerage de un gran banco, el relevamiento de tiempos «required 70,000 employees at more than 100 facilities to submit monthly reports of their time allocation. The company employed 14 people full-time just to manage the data collection». Un modelo con 150 actividades y 600 000 objetos de costo corrido mensualmente por dos años «would require data estimates, calculations, and storage for more than 2 billion items». https://cours.univ-paris1.fr/pluginfile.php/2483984/mod_resource/content/2/Kaplan%20Anderson%202004%20hbr.pdf
- El defecto técnico del ABC clásico: «When people estimate how much time they spend on a list of activities handed to them, they invariably report percentages that add up to 100», o sea que nadie declara tiempo ocioso, y las tarifas se calculan «assuming that resources are working at full capacity». Las tarifas quedan sobreestimadas «by the reciprocal of the capacity utilization percentage: At 80% utilization, the rates are 25% too high; at 67% utilization, the rates are 50% too high.» https://cours.univ-paris1.fr/pluginfile.php/2483984/mod_resource/content/2/Kaplan%20Anderson%202004%20hbr.pdf
- La propuesta (time-driven ABC): estimar solo dos parámetros, «the cost per time unit of supplying resource capacity and the unit times of consumption of resource capacity by products, services, and customers». Regla práctica: la capacidad práctica es 80 % a 85 % de la teórica, y alcanza con acertar «within 5% to 10%». https://cours.univ-paris1.fr/pluginfile.php/2483984/mod_resource/content/2/Kaplan%20Anderson%202004%20hbr.pdf
- Ecuaciones de tiempo: «Packaging Time = 0.5 + 6.5 [if special packaging required] + 2.0 [if shipping by air]», con la observación de que muchos ERP «already store data on order, packaging, distribution method, and other characteristics». https://cours.univ-paris1.fr/pluginfile.php/2483984/mod_resource/content/2/Kaplan%20Anderson%202004%20hbr.pdf (Esto es lo más cercano al lector de software que hay en toda la vertical.)
- Kaplan, 1988, sobre el estado previo a ABC: los sistemas que se hacen «mainly to value inventory for financial and tax statements» no dan la información «accurate and timely» que se necesita; el costo de producto se centra en «the least important cost component—direct labor—and ignore expenses involved in designing, marketing, distributing, and servicing goods.» https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf

**Discrepancias a dar en la nota**

- **Sobre cuánto aporta ABC.** OpenStax lo presenta como método con ventajas y costos; Kaplan y Anderson (coautor del 2004 y fundador de Acorn Systems, una empresa de software y consultoría de ABC, según su propia nota de autor) dicen que el ABC clásico fracasó a gran escala y que la solución es su variante. Hay conflicto de interés declarado en la propia ficha del artículo: «Kaplan serves on the board of Acorn Systems». https://cours.univ-paris1.fr/pluginfile.php/2483984/mod_resource/content/2/Kaplan%20Anderson%202004%20hbr.pdf
- **Sobre el costeo estándar.** OpenStax lo explica como herramienta de control; Kaplan (1988) cuenta el caso de la química que lo usó, perdió el costo real de producto y debió rehacerlo. Es el mismo tema visto desde la función que cada uno prioriza. https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf

### Ejemplos con números (tomados de fuente)

**a) Clasificación: fijos y variables (Carolina Yachts, OpenStax 2.2).** «Carolina Yachts produces 625 boats per year, and their total annual fixed costs are $1,560,000.» El costo fijo promedio es «$2,496 per boat»; con «total variable costs of $6,875,000» el variable promedio es «$11,000 per boat». Mixto (Ocean Breeze): «$2,000 per month, regardless of the number of rooms rented» más «$5.00 per room per night»; a 60 habitaciones el total es $2 300. Escalonado (Tony's T-Shirts): «Y = $6,000 + $0.75x», pero pasadas las 2 000 remeras el fijo sube de $6 000 a $8 000. https://openstax.org/books/principles-managerial-accounting/pages/2-2-identify-and-apply-basic-cost-behavior-patterns

**b) Absorción frente a variable (Outdoor Nation, OpenStax 6.5).** Datos: «It manufactures 5,000 units annually and sells them for $15 per unit.» Fijo de fábrica $15 000 por año; fijos de ventas y administración $21 000; materiales, mano de obra y variable de fábrica suman $5 por unidad; $1 por unidad de costo variable de venta; fijo por unidad $3. Producción constante de 5 000 unidades; ventas: 5 000, 4 000 y 6 000.

| Año | Unidades vendidas | Utilidad con absorción | Utilidad con variable | Diferencia |
|---|---|---|---|---|
| 1 | 5 000 | $9 000 | $9 000 | $0 |
| 2 | 4 000 | $3 000 | $0 | $3 000 |
| 3 | 6 000 | $15 000 | $18 000 | −$3 000 |

Explicación de la fuente: en el año 2, 1 000 unidades sin vender llevan $3 000 de fijo en el inventario final, por eso la utilidad con absorción es mayor; en el año 3 esos $3 000 salen del inventario como costo de lo vendido. https://openstax.org/books/principles-managerial-accounting/pages/6-5-compare-and-contrast-variable-and-absorption-costing

(Verificación mía, no de la fuente: margen de contribución $15 − $5 − $1 = $9; con variable, año 1: 5 000 × 9 − 36 000 = $9 000; año 2: 4 000 × 9 − 36 000 = $0. Coincide.)

**c) Costeo por procesos, unidades equivalentes (Rock City Percussion, OpenStax 5.3).** 8 700 unidades a contabilizar, 7 500 terminadas, 1 200 en proceso. Los materiales se agregan al inicio (100 % completas para materiales) y «only 35% complete with regard to conversion costs», o sea 420 unidades equivalentes de conversión (1 200 × 35 %). Totales: 8 700 equivalentes de materiales y 7 920 de conversión. Costo por unidad equivalente: materiales $1,17 y conversión $2,80; total $3,97. https://openstax.org/books/principles-managerial-accounting/pages/5-3-explain-and-compute-equivalent-units-and-total-cost-of-production-in-an-initial-processing-stage

**d) Costo estándar y variación (OpenStax 8.1 y 8.2).** Tarjeta de costo estándar de una bicicleta: materiales 4 libras × $5,25 = $21,00; mano de obra de ensamblado 2,75 h × $11,00 = $30,25; de terminación 4 h × $15,00 = $60,00; variable de fábrica 6,75 h × $5,00 = $33,75; fijo 6,75 h × $3,00 = $20,25; total $165,25 (suma verificada por mí). Variación (Connie's Candy): estándar $7,00 por libra y 0,25 libras por caja. Con precio real de $9,00 y 20 libras: «($9.00–$7.00)×20lbs. = $40 or $40 (Unfavorable)». Con 0,50 libras por caja: «(0.50lb.–0.25lb.)×$7.00 = $1.75 or $1.75 (Unfavorable)». Total: «(0.50lbs.×$9.00)–(0.25lbs.×$7.00) = $4.50–$1.75 = $2.75 (Unfavorable)». https://openstax.org/books/principles-managerial-accounting/pages/8-1-explain-how-and-why-a-standard-cost-is-developed ; https://openstax.org/books/principles-managerial-accounting/pages/8-2-compute-and-evaluate-materials-variances

**e) ABC tradicional, tres productos (Musicality, OpenStax 6.3 y 6.4).** Carga fabril estimada $2 500 000 en cinco pools: preparar máquinas $200 000, comprar materiales $500 000, inspeccionar $300 000, ensamblar $600 000, producción tecnológica $900 000. Tarifas ABC: $40 por preparación de máquina, $50 por requisición de compra, $15 por hora de inspección, $20 por parte que requiere mano de obra, $6 por hora-máquina. Carga por unidad: $9,00 (Solo), $8,15 (Band), $1,70 (Orchestra). Costo por unidad con ABC: $22,50, $16,90 y $17,70; con el método tradicional: $18,50, $16,75 y $20,00; diferencia: $4,00, $0,15 y −$2,30. La página concluye que «ABC showed that the Solo product creates a loss for the company.» https://openstax.org/books/principles-managerial-accounting/pages/6-3-calculate-activity-based-product-costs ; https://openstax.org/books/principles-managerial-accounting/pages/6-4-compare-and-contrast-traditional-and-activity-based-costing-systems

**f) ABC clásico frente a time-driven (departamento de atención al cliente, Kaplan y Anderson 2004).** Gastos de $560 000 por trimestre; actividad trimestral: 49 000 pedidos, 1 400 consultas, 2 500 verificaciones de crédito. ABC clásico (70 %, 10 %, 20 % del tiempo según encuesta): $8 por pedido, $40 por consulta, $44,80 por verificación. Time-driven: 28 empleados, 10 560 minutos por mes cada uno, capacidad práctica de 80 %, o sea 700 000 minutos; costo por minuto $0,80 ($560 000 ÷ 700 000). Tiempos unitarios: 8, 44 y 50 minutos. Tarifas: $6,40 por pedido, $35,20 por consulta, $40 por verificación. Uso real: 578 600 minutos, $462 880, «only 83% of the practical capacity». En el trimestre siguiente (51 000 pedidos, 1 150 consultas, 2 700 verificaciones): usados $474 880 sobre $560 000 suministrados; capacidad no usada $85 120. Si una verificación baja de 50 a 20 minutos, la tarifa pasa de $40 a $16. https://cours.univ-paris1.fr/pluginfile.php/2483984/mod_resource/content/2/Kaplan%20Anderson%202004%20hbr.pdf

Nota: en la copia del PDF, los dígitos salen con ruido de OCR en el texto extraído (por ejemplo «S313,600»). Las cifras que cito las reconstruí y verifiqué por cuenta (392 000 ÷ 49 000 = 8; 560 000 ÷ 700 000 = 0,80; 8 × 0,80 = 6,40).

### Recursos canónicos

- **Clasificación, absorción frente a variable, órdenes y procesos, estándar:** OpenStax capítulos 2, 4–6 y 8. Para la nota de absorción/variable, la **sección 6.5**, tabla de Outdoor Nation: fijarse en que el *único* movimiento entre los dos métodos es el fijo que queda en el inventario, y que con producción constante la diferencia es exactamente el fijo unitario por la variación de stock.
- **ABC y su crítica:** **Kaplan y Anderson (2004)**, primeras dos páginas (el problema) y el ejemplo del departamento de atención. Fijarse en la corrección por capacidad práctica (el «25 % too high» a 80 % de utilización) y en el informe con «Unused Capacity», que es lo que un software puede mostrar y rara vez muestra. Leerlo con la reserva del interés comercial de Kaplan en la variante.
- **Por qué el costeo para decidir y el costeo contable son sistemas distintos:** **Kaplan (1988)**, «One Cost System Isn't Enough», el apartado de las tres funciones y su tabla «Different Functions, Different Demands».

---

## 3. punto-de-equilibrio

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 3.1 | OpenStax 3.1 «Contribution Margin» | https://openstax.org/books/principles-managerial-accounting/pages/3-1-explain-contribution-margin-and-calculate-contribution-margin-per-unit-contribution-margin-ratio-and-total-contribution-margin | P | 3 | 2 | 3 | 2 | [L~] |
| 3.2 | OpenStax 3.2 «Break-Even Point in Units and Dollars» | https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars | P | 3 | 3 | 3 | 2 | [L~] |
| 3.3 | OpenStax 3.3 «Break-Even Sensitivity Analysis for a Single Product» | https://openstax.org/books/principles-managerial-accounting/pages/3-3-perform-break-even-sensitivity-analysis-for-a-single-product-under-changing-business-situations | P | 3 | 2 | 3 | 1 | [L~] |
| 3.4 | OpenStax 3.4 «… Multi-Product Environment» | https://openstax.org/books/principles-managerial-accounting/pages/3-4-perform-break-even-sensitivity-analysis-for-a-multi-product-environment-under-changing-business-situations | P | 3 | 3 | 3 | 2 | [L~] |
| 3.5 | OpenStax 3.5 «Margin of Safety and Operating Leverage» | https://openstax.org/books/principles-managerial-accounting/pages/3-5-calculate-and-interpret-a-companys-margin-of-safety-and-operating-leverage | P | 3 | 2 | 3 | 2 | [L~] |

Las cinco filas son un solo libro. No encontré una segunda fuente independiente para este componente: ver huecos.

### Afirmaciones

- «Contribution margin is the amount by which a product's selling price exceeds its total variable cost per unit.» Razón: «The contribution margin ratio is the percentage of a unit's selling price that exceeds total unit variable costs.» Total: «the total amount by which total sales exceed total variable costs.» https://openstax.org/books/principles-managerial-accounting/pages/3-1-explain-contribution-margin-and-calculate-contribution-margin-per-unit-contribution-margin-ratio-and-total-contribution-margin
- Equilibrio en unidades: «Total Fixed Costs divided by Contribution Margin per Unit». En pesos (dólares en el original): «Fixed Costs divided by Contribution Margin ratio». Con utilidad objetivo, el numerador pasa a «Fixed costs + desired profit». La utilidad antes de impuestos se obtiene de la de después de impuestos como «After-tax profit / (1 – tax rate)». https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars
- Margen de seguridad: «A company's margin of safety is the difference between its current sales and its break-even sales.» Fórmula: «Total Budgeted (or actual sales) minus Break-Even Sales.» https://openstax.org/books/principles-managerial-accounting/pages/3-5-calculate-and-interpret-a-companys-margin-of-safety-and-operating-leverage
- Apalancamiento operativo: «Operating leverage is a measurement of how sensitive net operating income is to a percentage change in sales dollars.» https://openstax.org/books/principles-managerial-accounting/pages/3-5-calculate-and-interpret-a-companys-margin-of-safety-and-operating-leverage
- Varios productos: la mezcla se trata como una «composite unit», «a selection of discrete products associated together in proportion to the sales mix»; se suma el margen de contribución de los componentes y se divide el fijo por ese margen compuesto. Resumen de la sección: «If the sales mix of a company changes, then the break-even point changes». https://openstax.org/books/principles-managerial-accounting/pages/3-4-perform-break-even-sensitivity-analysis-for-a-multi-product-environment-under-changing-business-situations ; https://openstax.org/books/principles-managerial-accounting/pages/3-summary
- Sensibilidad: un aumento de precio baja el equilibrio; más costo fijo lo sube sin cambiar el margen unitario. El texto lo cuida con la salvedad «this is assuming the higher sales price does not decrease the number of units sold.» y con que el nuevo equilibrio sea realista, «within the relevant range». https://openstax.org/books/principles-managerial-accounting/pages/3-3-perform-break-even-sensitivity-analysis-for-a-single-product-under-changing-business-situations

**Supuestos y límites.** El extractor de la página 3.3 confirmó que el texto **no enumera** los supuestos del CVP (linealidad, precio constante, mezcla constante, rango relevante, inventario sin cambios); solo toca dos de ellos al pasar (rango relevante, volumen que no baja al subir el precio). Un resumen del buscador atribuyó a la sección 3.2 la lista «linearity, constant per-unit selling price, no inventory change, and constant sales mix», pero **no pude verificarla en el texto**, y no la doy como cita. Los supuestos se pueden escribir en la nota como consecuencia lógica de las fórmulas, citando 3.4 para el de mezcla («the sales mix is assumed constant» según el buscador) y 3.3 para precio y rango relevante. Ver huecos.

**Discrepancias dentro de la propia fuente (para no copiar errores):**

- La página 3.5 rotula «1,900 units» como el equilibrio en el cuadro del ejemplo Manteo, pero el equilibrio en pesos es $153 000, que a $90 por unidad ($225 000 ÷ 2 500) son 1 700 unidades; las 1 900 incluyen un margen de seguridad objetivo de $10 000. https://openstax.org/books/principles-managerial-accounting/pages/3-5-calculate-and-interpret-a-companys-margin-of-safety-and-operating-leverage
- La página 3.1 dice que el modelo Blue Jay aportó «$36,000» en abril, pero su propio cálculo da $40 000 (500 × $80). https://openstax.org/books/principles-managerial-accounting/pages/3-1-explain-contribution-margin-and-calculate-contribution-margin-per-unit-contribution-margin-ratio-and-total-contribution-margin

### Ejemplos con números

**a) Un producto (Hicks Manufacturing, Blue Jay, OpenStax 3.1 y 3.2).** Precio $100, variable $20, margen de contribución $80 por unidad (razón 0,80). Fijos $18 000 por mes. Equilibrio: $18 000 ÷ $80 = 225 unidades, o $18 000 ÷ 0,80 = $22 500. A 175 unidades la utilidad operativa es −$4 000; a 300 unidades, $6 000. Utilidad objetivo de $16 000: (18 000 + 16 000) ÷ 80 = 425 unidades, o $42 500. Objetivo de $24 000 después de impuestos con tasa de 40 %: $24 000 ÷ (1 − 0,40) = $40 000 antes de impuestos; (18 000 + 40 000) ÷ 80 = 725 unidades, $72 500. https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars

**b) Un servicio (Marshall & Hirito, declaraciones de impuestos).** Cobra $400 por declaración, variable $150, margen $250; fijos $14 000 por mes; equilibrio 56 declaraciones o $22 400; con objetivo de $10 000, 96 declaraciones o $38 400. (Útil para el lector que vende servicios y no productos.) https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars

**c) Margen de seguridad (Manteo Machine, OpenStax 3.5).** Ventas actuales (2 500 unidades) $225 000; equilibrio $153 000; margen de seguridad $72 000, es decir 32 % de las ventas ($72 000 ÷ $225 000). https://openstax.org/books/principles-managerial-accounting/pages/3-5-calculate-and-interpret-a-companys-margin-of-safety-and-operating-leverage (El 32 % lo calculé yo a partir de las dos cifras de la fuente; la fuente de búsqueda también lo da.)

**d) Mezcla (West Brothers, vinilos, OpenStax 3.4).** Tres productos por pie cuadrado: de obra básica $6,25 con variable $3,25; arquitectónico $7,75 con $4,50; de restauración $9,25 con $6,25. Mezcla 5:3:2. Precio de la unidad compuesta $73,00; variable $42,25; margen compuesto $30,75. Fijos $145 000 por año. Equilibrio: $145 000 ÷ $30,75 = 4 715,45, redondeado a 4 716 unidades compuestas; por producto: 23 577, 14 146 y 9 431 pies cuadrados, total 47 154. https://openstax.org/books/principles-managerial-accounting/pages/3-4-perform-break-even-sensitivity-analysis-for-a-multi-product-environment-under-changing-business-situations

**e) Sensibilidad (cafetería con máquina de espresso, OpenStax 3.3).** La máquina cuesta $15 000, baja el variable por taza de $1,50 a $1,45 (margen $2,25 a $2,30), sube el fijo mensual de $2 475 a $2 875 por la cuota; el equilibrio pasa de 1 100 a 1 250 unidades y de $4 125,00 a $4 687,50; la utilidad a 1 500 unidades cae de $900 a $575. Moraleja para la nota: bajar un costo variable no mejora el equilibrio si el fijo sube más. https://openstax.org/books/principles-managerial-accounting/pages/3-3-perform-break-even-sensitivity-analysis-for-a-single-product-under-changing-business-situations

### Recurso canónico

**OpenStax, capítulo 3, secciones 3.1, 3.2 y 3.5**, en ese orden. Para la nota: el ejemplo de Hicks (un producto, números redondos, con la prueba a 175 y 300 unidades) como columna vertebral, y el de West Brothers (3.4) para la mezcla. Fijarse en: que la mezcla es un supuesto, no un dato, y que el equilibrio de varios productos se mueve solo con cambiar la mezcla. Cuidado con los dos errores de la fuente (Manteo, Blue Jay).

---

## 4. presupuesto

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 4.1 | OpenStax 7.1 «How and Why Managers Use Budgets» | https://openstax.org/books/principles-managerial-accounting/pages/7-1-describe-how-and-why-managers-use-budgets | P | 3 | 2 | 1 | 2 | [L~] |
| 4.2 | OpenStax 7.4 «Prepare Flexible Budgets» | https://openstax.org/books/principles-managerial-accounting/pages/7-4-prepare-flexible-budgets | P | 3 | 3 | 3 | 2 | [L~] |
| 4.3 | OpenStax 7.5 «Budgets Used to Evaluate Goals» (solo el título del buscador) | https://openstax.org/books/principles-managerial-accounting/pages/7-5-explain-how-budgets-are-used-to-evaluate-goals | P | 3 | — | — | 2 | [M] |
| 4.4 | Hope y Fraser, «Who Needs Budgets?», HBR, vol. 81 n.º 2, feb. 2003, pp. 108–115 (ficha) | https://www.library.hbs.edu/working-knowledge/why-budgeting-kills-your-company (entrevista de HBS Working Knowledge que lo comenta) | S (comentario del artículo; el artículo es primario pero no lo leí) | 2 | 2 | 2 | 2 | [L~] |
| 4.5 | Hope y Fraser, *Beyond Budgeting: How Managers Can Break Free from the Annual Performance Trap*, HBS Press, 2003 | https://www.oreilly.com/library/view/beyond-budgeting/9781422163252/e9781422163252_fm02.html | P, solo ficha | 3 | — | — | 3 | [M] |
| 4.6 | Bogsnes (Beyond Budgeting Institute), white paper «Beyond Budgeting at 25», mar. 2023 | https://bbrt.org/wp-content/uploads/bb-white-paper.pdf | P (la propia institución que promueve la posición), parte interesada | 2 | 2 | 1 | 3 | [L] |
| 4.7 | Libby y Lindsay, «Beyond budgeting or budgeting reconsidered? A survey of North-American budgeting practice», *Management Accounting Research* 21 (2010) 56–75 | https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/8/36875/files/2016/12/Libby-Lindsay_budgeting_survey-17bvsph.pdf | P, estudio empírico | 3 | 3 | 2 | 3 | [L] |

### Afirmaciones

**Presupuesto maestro, operativo y financiero**

- «A master budget is one that includes two areas, operational and financial, each of which has its own sub-budgets.» El operativo «helps plan future revenue and expenses and results in a projected income statement»; el financiero «plans the use of assets and liabilities and results in a projected balance sheet.» https://openstax.org/books/principles-managerial-accounting/pages/7-1-describe-how-and-why-managers-use-budgets
- Propósitos: «A good budgeting system will help a company reach its strategic goals» y «Budgeting is a formal method to communicate a company's plans to its internal stakeholders». https://openstax.org/books/principles-managerial-accounting/pages/7-1-describe-how-and-why-managers-use-budgets
- Según el resumen del buscador, el maestro y todos sus presupuestos componentes son «static budgets». https://openstax.org/books/principles-managerial-accounting/pages/7-summary [S]

**Estático, flexible, base cero**

- «A static budget is one that is prepared based on a single level of output for a given period.» «A flexible budget is one based on different volumes of sales.» «A flexible budget flexes the static budget for each anticipated level of production.» https://openstax.org/books/principles-managerial-accounting/pages/7-4-prepare-flexible-budgets
- «Zero-based budgeting begins with zero dollars and then adds to the budget only revenues and expenses» que se justifiquen; su costo: «every expense needs to be justified, including obvious ones, so it takes a lot of time to complete.» https://openstax.org/books/principles-managerial-accounting/pages/7-1-describe-how-and-why-managers-use-budgets
- Presupuesto móvil (rolling): «it also takes management away from other duties as it requires continual updating». https://openstax.org/books/principles-managerial-accounting/pages/7-1-describe-how-and-why-managers-use-budgets

**Análisis de desvíos (presupuesto frente a real)**

- No logré leer la sección 7.5 (solo el título). La sección 7.4 **no trae resultados reales ni desvíos**: lo confirmó el extractor («The page does not include actual results or variance calculations»). El desvío de materiales con números está en 8.2 (ver sección 2, ejemplo d). Queda como hueco armar un ejemplo de desvío de presupuesto flexible con fuente. Ver huecos.

**Sesgos de comportamiento (en el propio libro de texto)**

- «managers might be tempted to set artificially low standards to ensure that targets are hit» y «employees may feel a tension between reporting actual results and reporting results that reach the predetermined goals». https://openstax.org/books/principles-managerial-accounting/pages/7-1-describe-how-and-why-managers-use-budgets

**Beyond Budgeting (posición contraria)**

- Origen y estructura: el Beyond Budgeting Institute dice que el modelo se desarrolló en 1998, y que hoy son doce principios, seis de liderazgo y seis de procesos de gestión. «When the Beyond Budgeting model was developed in 1998…». https://bbrt.org/wp-content/uploads/bb-white-paper.pdf
- Principios de liderazgo, textuales: 1. Purpose: «Engage and inspire people around bold and noble causes; not around short-term financial targets»; 2. Values; 3. Transparency; 4. Autonomy: «Trust people with freedom to act»; 5. Organisation: «organise around accountable teams»; 6. Customers. Principios de procesos: 7. Targets: «Set directional, ambitious and relative goals; avoid fixed and cascaded targets»; 8. Forecasts: «Make forecasting a lean and unbiased process; not a rigid and political exercise»; 9. Resource allocation: «Plan and make resources available as needed; not through detailed annual budget allocations»; 10. Performance evaluation: «Evaluate performance holistically to guide interventions; not based on measurement only and not for rewards only»; 11. Rewards: «Reward shared success against competition; not against fixed performance contracts»; 12. Coordination: «Organise management processes dynamically around business rhythms and events; not around the calendar year only». https://bbrt.org/wp-content/uploads/bb-white-paper.pdf
- Matiz importante: el propio Instituto dice que el modelo no es un menú sino un conjunto, con una escala de «fixed (traditional budgeting)» a «decoupled (budget purpose separation)», «continuous» y «relative». Y advierte que ha visto implementaciones «reduced to Rolling Forecasting exercises or just a more dynamic resource allocation». https://bbrt.org/wp-content/uploads/bb-white-paper.pdf
- La lista de principios cambió con los años, y el Instituto lo admite: «The Beyond Budgeting principles have evolved over the years and have been updated several times». Otras fuentes ofrecen listas distintas (una de 2011 con otro agrupamiento) y una (no verificada) dice que Hope y Fraser empezaron con diez principios. https://bbrt.org/wp-content/uploads/bb-white-paper.pdf ; https://www.oreilly.com/library/view/this-is-beyond/9781394171248/c03.xhtml [S]
- La crítica original, según la entrevista de HBS Working Knowledge: el presupuesto funciona como «implicit contract» y los incentivos pueden llegar a «97 percent of a U.S. manager's annual salary»; hay «distortion, misrepresentation, and gaming»; el que quiere más plata pide «50 percent more than you need»; es «a vestige of the old command-and-control approach to management». https://www.library.hbs.edu/working-knowledge/why-budgeting-kills-your-company
- Cifras de la misma entrevista (que no verifiqué en el artículo original): «The average billion-dollar company spends up to 25,000 person-days a year on budgeting»; algunos procesos «take up to six months and 20 percent of management's time»; una encuesta de Hackett encontró que 60 a 90 por ciento de las 2 000 mayores empresas globales usan contratos de desempeño fijos; Svenska Handelsbanken (11 regiones, 550 sucursales) dejó el presupuesto a principios de los años setenta. https://www.library.hbs.edu/working-knowledge/why-budgeting-kills-your-company
- La alternativa de Hope y Fraser en esa entrevista: metas de referencia a 2–3 años, contratos de mejora relativa evaluados por pares, pronósticos móviles a cinco trimestres y recursos asignados según se necesiten. Bruns propone mantener el presupuesto pero cambiar la remuneración. https://www.library.hbs.edu/working-knowledge/why-budgeting-kills-your-company
- **Evidencia en contra de la tesis:** Libby y Lindsay (2010), dos encuestas a organizaciones medianas y grandes de Norteamérica; muestra de 558 cuestionarios (346 de Canadá y 212 de EE. UU.), con tasa de respuesta de 13,6 % en la muestra canadiense y 1,5 % en la de miembros de IMA. 79 % (440 de 558) usa el presupuesto para control; de ese grupo, 94 % dice que no piensa abandonarlo, 5 % tal vez, 1 % sí. Conclusión del abstract: «budgets continue to be used for control purposes and are perceived to be value-added. While problems exist with budgets, organizations are adapting their use to account for these problems rather than abandoning budgets altogether.» Y 46 % de los canadienses planeaba cambiar o adaptar su sistema en los dos años siguientes (los motivos más citados: preparar el presupuesto lleva tiempo y su beneficio puede no valerlo, y la falta de flexibilidad frente a un entorno cambiante). https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/8/36875/files/2016/12/Libby-Lindsay_budgeting_survey-17bvsph.pdf
- La misma fuente cita otra encuesta, finlandesa (Ekholm y Wallin, 2000): 15 % pensaba abandonar el presupuesto tradicional, 61 % mejorarlo y 24 % seguir igual. https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/8/36875/files/2016/12/Libby-Lindsay_budgeting_survey-17bvsph.pdf
- Salvedad sobre Libby y Lindsay: la respuesta del 1,5 % en la muestra de IMA es muy baja, y los autores lo señalan como limitación. https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/8/36875/files/2016/12/Libby-Lindsay_budgeting_survey-17bvsph.pdf
- Quien promueve la posición también aporta cifras de adopción (BCG y Bain, encuestas a sus clientes; «Almost 60% reported increased sales» entre los practicantes). Son datos de la parte interesada y de una encuesta a practicantes ya adoptantes, y no los pondría como evidencia independiente. https://bbrt.org/wp-content/uploads/bb-white-paper.pdf

**Discrepancias a dar en la nota**

- Hope y Fraser dicen que el presupuesto debe abandonarse; Bruns (en la misma entrevista) dice que no hace falta abandonarlo si se cambia la remuneración; el libro de texto de OpenStax lo presenta como herramienta con sus costos de comportamiento; Libby y Lindsay encuentran que casi todos lo mantienen. Cuatro posiciones, no dos.

### Ejemplo con números (presupuesto flexible, Big Bad Bikes, OpenStax 7.4)

Costos por unidad: materiales $4, mano de obra $15, variable de fábrica $3, variable de ventas y administración $3; fijos de fábrica $29 000 y de ventas y administración $18 000 en todos los escenarios.

| | A 1 000 unidades a $70 | A 1 500 unidades a $70 (presupuesto estático) | A 1 500 unidades a $75 |
|---|---|---|---|
| Ventas | $70 000 | $105 000 | $112 500 |
| Costo de lo vendido | $51 000 | $62 000 | $62 000 |
| Utilidad bruta | $19 000 | $43 000 | $50 500 |
| Utilidad neta | −$2 500 | $20 250 | $27 750 |

(El mismo estado a 2 500 unidades a $75 da ventas de $187 500 y utilidad neta de $76 597.) La fuente muestra cómo se «flexa» el presupuesto por nivel de actividad; **no** trae el real ni el desvío. https://openstax.org/books/principles-managerial-accounting/pages/7-4-prepare-flexible-budgets

Para el desvío con números hay que combinarlo con el ejemplo de Connie's Candy (sección 2, ejemplo d), que sí separa efecto precio y efecto cantidad.

### Recurso canónico

- **Para la técnica:** OpenStax capítulo 7, secciones 7.1 y 7.4. Fijarse en: la diferencia entre estático y flexible (el estático se prepara a un solo volumen; comparar real a otro volumen contra él mezcla el efecto volumen con el de eficiencia).
- **Para la crítica:** primero **Libby y Lindsay (2010)** (la evidencia), después los **doce principios en el white paper de Bogsnes (2023)** (la propuesta, con la salvedad de que lo escribe quien la promueve). El artículo original de Hope y Fraser (HBR, feb. 2003) queda como lectura por conseguir (no lo leí).

---

## 5. centros-de-costo

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 5.1 | OpenStax 9.3 «Types of Responsibility Centers» | https://openstax.org/books/principles-managerial-accounting/pages/9-3-describe-the-types-of-responsibility-centers | P | 3 | 2 | 3 | 2 | [L~] |
| 5.2 | OpenStax 9.4 (efectos de las decisiones en la evaluación; trae precios de transferencia y costos asignados) | https://openstax.org/books/principles-managerial-accounting/pages/9-4-describe-the-effects-of-various-decisions-on-performance-evaluation-of-responsibility-centers | P | 3 | 2 | 3 | 2 | [L~] |
| 5.3 | Lumen Learning (SUNY), «Step Method of Allocation» (con «Direct Method» y «Reciprocal Method» en el mismo curso) | https://courses.lumenlearning.com/suny-managacct/chapter/step-method-of-allocation/ | P (libro de texto abierto) | 2 | 2 | 3 | 2 | [L~] |
| 5.4 | Microsoft Learn, «Plan your chart of accounts» (Dynamics 365 Finance), actualizada el 2026-04-02 según su metadato | https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/plan-chart-of-accounts | P (documentación de producto: describe cómo lo hace un producto, no cómo debe ser) | 2 | 2 | 1 | 3 | [L~] |
| 5.5 | Odoo 19.0, «Analytic accounting» | https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/analytic_accounting.html | P (documentación de producto) | 2 | 2 | 1 | 3 | [L~] (leí los primeros 100 000 de 103 561 caracteres) |
| 5.6 | Microsoft Learn, «Allocation bases» (cost accounting) | https://learn.microsoft.com/en-us/dynamics365/finance/cost-accounting/allocation-bases | P (documentación de producto) | 2 | 2 | 2 | 2 | [S] (solo el resumen del buscador) |

### Afirmaciones

**Tipos de centros de responsabilidad**

- «A cost center is an organizational segment in which a manager is held responsible only for costs.» «A revenue center is an organizational segment in which a manager is held accountable only for revenues.» «A profit center is an organizational segment in which a manager is responsible for both revenues and costs.» Centro de inversión: el gerente responde por la utilidad y por el capital invertido. https://openstax.org/books/principles-managerial-accounting/pages/9-3-describe-the-types-of-responsibility-centers
- Contabilidad por responsabilidad: «assigning the responsibility of accounting for particular segments of the company» a una persona o grupo. https://openstax.org/books/principles-managerial-accounting/pages/9-3-describe-the-types-of-responsibility-centers
- Principio de controlabilidad: el objetivo es «evaluate managers only on the decisions over which they have control»; los costos asignados «cannot be controlled by the responsibility center manager» y no deben pesar en su evaluación. https://openstax.org/books/principles-managerial-accounting/pages/9-4-describe-the-effects-of-various-decisions-on-performance-evaluation-of-responsibility-centers

**Asignación y prorrateo de indirectos**

- Método escalonado (step-down): «This method allocates service costs to the operating departments and other service departments in a sequential process.» https://courses.lumenlearning.com/suny-managacct/chapter/step-method-of-allocation/
- Los tres métodos (según el buscador y los títulos del mismo curso): directo (ignora los servicios entre departamentos de servicio), escalonado (reconoce solo relaciones en un sentido, y lo que ya se repartió no vuelve) y recíproco (ecuaciones simultáneas). Solo abrí el escalonado. https://courses.lumenlearning.com/suny-managacct/chapter/direct-method-of-allocation/ ; https://courses.lumenlearning.com/suny-managacct/chapter/reciprocal-method-of-allocation/ [S]

**Precios de transferencia (mención)**

- «the pricing process put into place when one segment of a business "sells" goods to another segment of the same business.» «There are three primary transfer pricing approaches: market-based prices, cost-based prices, or negotiated prices.» Costo: «the price may be based on either total variable cost, full cost, or a cost-plus scenario». Negociado: «the company allows the buying segment and the selling segment to negotiate the transfer price». https://openstax.org/books/principles-managerial-accounting/pages/9-4-describe-the-effects-of-various-decisions-on-performance-evaluation-of-responsibility-centers

**Por qué vive en dimensiones y no en el plan de cuentas**

- Esta afirmación **no la hace ninguna fuente de contabilidad de gestión que haya leído**; la sostiene la documentación de dos productos, y como tal es la práctica de esos productos, no una regla de la disciplina.
- Microsoft: «A chart of accounts is a collection of accounts that define a financial framework. To further track the transactions in these accounts, add segments. These segments are known as financial dimensions. For example, an expense account might include financial dimensions that are named Department, Cost center, and Purpose.» Y el plan de cuentas «is a structured list of a legal entity's general ledger accounts. Use the list to prepare financial reports for authorities and owners.» Los factores de diseño del plan de cuentas que lista son los requisitos de reporte del país o región, los de la entidad legal y el grado de detalle requerido por organismos externos y por la propia organización. https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/plan-chart-of-accounts
- Odoo: la contabilidad analítica «helps track costs and revenues and analyze a project's or service's profitability»; los planes «group analytic accounts, allowing the company to analyze its accounting» (por proyecto o por departamento); «The distribution of costs in one or more analytic accounts can be set in each» factura o comprobante, y se puede repartir por porcentajes. https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/analytic_accounting.html
- La razón de fondo, que enlaza con Kaplan (1988): el plan de cuentas atiende a la función regulada (informar afuera) y por eso lo condicionan la norma y el país; la dimensión es una etiqueta ortogonal que se puede cambiar sin tocar los saldos legales. Esto es mi inferencia de lectura cruzada de las dos documentaciones y de Kaplan, no una cita; en la nota debe aparecer como argumento de diseño, no como regla de la disciplina. https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf

### Ejemplos con números

**a) Centros de responsabilidad (Apparel World, OpenStax 9.3).** Centro de costo, el departamento de limpieza: costos reales de $19 725 contra presupuesto de $18 745, un exceso de $980 (5,2 %). Centro de utilidad, ropa de niños: ganó $32 647 contra $28 756 presupuestados, $3 891 (13,5 %) por encima, con ingresos de $176 400 contra $147 200. Centro de inversión: retorno sobre la inversión de 25,9 % en ropa de niños ($3 891 ÷ $15 000) y 3,9 % en ropa de mujeres ($2 533 ÷ $65 000). https://openstax.org/books/principles-managerial-accounting/pages/9-3-describe-the-types-of-responsibility-centers

**b) Reparto de servicios escalonado (Lumen).** Costos: mantenimiento $8 000 (1 000 horas-máquina, 100 empleados); administración $4 000 (2 000 horas, 200 empleados); operativo 1 $32 000 (1 500 horas, 250 empleados); operativo 2 $36 000 (2 500 horas, 150 empleados). Paso 1, mantenimiento por horas-máquina: $8 000 ÷ 6 000 = $1,3333 por hora, a administración $2 667, al operativo 1 $2 000, al operativo 2 $3 333. Paso 2, administración ($4 000 + $2 667 = $6 667) por empleados de los operativos (400): $4 167 al operativo 1 y $2 500 al operativo 2. Totales finales: operativo 1 $38 167, operativo 2 $41 833 (suman $80 000, que es el costo total de partida). https://courses.lumenlearning.com/suny-managacct/chapter/step-method-of-allocation/

(Verificación mía: 8 000 + 4 000 + 32 000 + 36 000 = 80 000; 38 167 + 41 833 = 80 000.)

**c) Precio de transferencia (Regal Paper, OpenStax 9.4).** Con capacidad ociosa, la división papel puede cubrir el pedido de 500 000 cubiertas; a precio de mercado, $12 (el mismo que a clientes externos); a costo más 20 %, $8 × 120 % = $9,60; sin capacidad ociosa, «the transfer price would be the cost plus the contribution margin, which is $8 + $4, or $12.» https://openstax.org/books/principles-managerial-accounting/pages/9-4-describe-the-effects-of-various-decisions-on-performance-evaluation-of-responsibility-centers

### Recurso canónico

- **Para los tipos de centros y la regla de controlabilidad:** **OpenStax 9.3 y 9.4**. Fijarse en el cuadro de Apparel World, que muestra los tres tipos con cifras, y en la frase de controlabilidad.
- **Para el reparto de indirectos:** **el curso Lumen (SUNY), los tres métodos en orden** (directo, escalonado, recíproco), con el escalonado como el que muestra cómo importa el orden. Para alguien de software, la comparación directo/escalonado/recíproco equivale a la pregunta «¿se resuelve una vez o en cadena o como sistema de ecuaciones?».
- **Para dimensiones:** **Microsoft Learn «Plan your chart of accounts»**, en el primer párrafo, junto con la documentación analítica de Odoo; presentados como ejemplo de práctica, con el matiz de que son dos productos.

---

## 6. Huecos (lo que no encontré o no pude verificar)

Orden de importancia para quien escribe las notas.

1. **No hay segunda fuente independiente para punto de equilibrio ni para centros de costo.** Todo viene de OpenStax. Faltan: un texto de otro autor (Horngren, Garrison) o de una fuente profesional (IMA/CIMA) que confirme las fórmulas; y, para la nota de centros de costo, una fuente que no sea documentación de producto sobre «dimensiones frente a plan de cuentas».
2. **Supuestos del CVP sin fuente verificada.** El libro no los enumera en las páginas que leí (3.3 y la summary del 3). Un resumen del buscador le atribuyó a 3.2 «linearity, constant per-unit selling price, no inventory change, and constant sales mix», pero no lo verifiqué. Hay que encontrar un texto que los liste (por ejemplo en otro libro de texto abierto).
3. **Análisis de desvíos del presupuesto (real frente a flexible) sin ejemplo con números de fuente.** No pude leer 7.5; 7.4 solo trae escenarios presupuestados. Lo mejor que hay hoy es el desvío de materiales de 8.2. Hay que leer 7.5 o los problem sets del capítulo 7 (en el sitio, «Ch. 7 Problem Set A/B»).
3 bis. **Costeo por órdenes: sin ejemplo numérico.** Intenté 4.4 con una URL inventada y dio 404; no busqué la URL real. El ejemplo de procesos (5.3) sí está.
4. **Fuentes primarias de la crítica histórica no leídas:** *Relevance Lost* (1987) solo en catálogo; Cooper y Kaplan (1988) «Measure Costs Right» solo ficha de HBR; Kaplan y Cooper (1998) *Cost & Effect* solo catálogo; Hope y Fraser (2003) el artículo y el libro, no leídos (la crítica viene de una entrevista de HBS y de la institución que promueve la posición). Kaplan (1984) «The Evolution of Management Accounting» tampoco. La cita de «known by 1925» sobre *Relevance Lost* viene del buscador y no tiene fuente fijada.
5. **Definición de CIMA (*Official Terminology*, 2005)** solo en ficha de venta; y la edición actual del GMAP (segunda edición, 28-jun-2023 según AICPA y CIMA) no la abrí: usé una copia anterior (mención de 2017 como año de formación de la asociación, edición de 2014 con retoques), alojada en un sitio universitario. La definición no cambió entre ediciones, según una fuente secundaria; está sin verificar en el original.
6. **Statements on Management Accounting de IMA:** solo vi que existen (por ejemplo «The Conceptual Framework for Managerial Costing», 2014, y «Developing an Effective Managerial Costing Model», 2019). No las leí; la redirección de imanet.org a imaglobal.org impidió abrir la ficha. Podrían ser la fuente profesional que falta en costos-y-costeo.
7. **Costeo estándar: crítica.** No encontré fuente que discuta cuándo los estándares estorban (por ejemplo, con mejora continua). Solo el caso de Kaplan (1988).
8. **Clasificación de costos, parte sin leer:** directos e indirectos, de producto y del período: solo por resumen del buscador; no abrí 4.2 ni el glosario del capítulo 2.
9. **Contexto de software ausente:** ninguna fuente trata cómo modelar estos conceptos en un sistema (tarifas de asignación versionadas, reglas de reparto, dimensiones obligatorias). Solo Microsoft y Odoo en documentación, y el comentario de Kaplan y Anderson sobre ERP que ya guarda los atributos de las órdenes. Probablemente es lo que el lector más va a querer y lo menos documentado en fuentes de calidad.
10. **Temas del campo que el árbol no cubre:** decisiones con costos relevantes (OpenStax cap. 10, página 10.2 «Evaluate and Determine Whether to Accept or Reject a Special Order» vista solo por título) y medición del desempeño (cap. 12). No investigados.
11. **Erratas de la fuente a corregir al copiar:** OpenStax 3.5 (Manteo: «1,900 units» frente a $153 000 de equilibrio); 3.1 (Blue Jay: «$36,000» frente a $40 000); 8.1 (café: tarifa de variable «$0.50» frente a un costo de $0,05 que es el que suma $0,60). Las edades de las páginas de OpenStax aparecen en el buscador como de unos 2 843 días (edición de 2019); hay que fijarse si salió una edición nueva.
12. **Sobre la lectura [L~]:** la mayoría de las páginas de OpenStax pasaron por un extractor automático. Las citas literales son del extractor; antes de ponerlas entre comillas en una nota vigente, vale releer la página en el original.
