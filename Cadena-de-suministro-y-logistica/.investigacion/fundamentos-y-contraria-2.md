# Fundamentos y posición contraria, segunda ronda: Cadena de suministro y logística

Ángulo: verificar o descartar lo que la primera ronda dejó como [Mem] y cubrir sus huecos. No se editó el informe de la primera ronda (`fundamentos-y-contraria.md`).

## Advertencia de método

- Marcas: [L] leído completo o la sección completa; [M] metadatos o abstract; [S] resumen secundario o del buscador. Puntajes de 1 a 3: A autoridad, P profundidad, E ejemplos, U unicidad.
- Cómo se leyó. WebFetch no decodifica PDF, pero guarda el binario; se extrajo el texto con `pdftotext` (Fisher, APQC, SCOR DS, preprint de M5, glosario del CSCMP). Los abstracts de revistas salieron de las API abiertas de metadatos (Crossref, OpenAlex, Semantic Scholar), que reproducen el abstract del editor. Cada abstract citado como literal está así en la respuesta de la API; la URL de cada uno va al lado.
- Lo que no se pudo: ASCM bloquea clientes automáticos con una página de protección anti-bots (Incapsula) en `ascm.org/corporate-solutions/...` y `scor.ascm.org` devuelve solo "Loading..." o 404. No se la esquivó. El SCOR salió de un PDF del propio ASCM que sí se descargó (ver sección 2). ScienceDirect, Wiley, Springer, ResearchGate y el repositorio de Penn dan 403 o 404. El presupuesto de búsquedas se agotó otra vez a mitad de ronda.
- Las citas van en el idioma original y entre comillas. Donde la herramienta de lectura limitó la longitud de una cita, se usó el texto extraído del PDF o de la API, que es el literal.

## 0. Tabla de veredictos sobre las afirmaciones [Mem] de la primera ronda

Veredictos: **Confirmada** (con URL), **Corregida** (la primera ronda decía otra cosa, se da la versión con fuente), **Sin fuente** (no se encontró; sigue sin poder afirmarse).

| # | Afirmación [Mem] de la primera ronda | Veredicto | Fuente / qué hay |
|---|---|---|---|
| 1 | Fisher 1997: productos funcionales con cadena eficiente, innovadores con cadena que responde | Confirmada | PDF del artículo (HBR, marzo-abril 1997, producto 8509): https://eclass.upatras.gr/modules/document/file.php/MECH1277/%CE%95%CE%A1%CE%93%CE%91%CE%A3%CE%99%CE%95%CE%A3-PAPERS%20%CE%91%CE%9D%CE%9F%CE%99%CE%9E%CE%97%202024/2-Right%20Supply%20Chain%20B.pdf (sección 1) |
| 2 | Definición de cadena eficiente y cadena que responde | Confirmada, con literal | Mismo PDF, tabla "Physically Efficient Versus Market-Responsive Supply Chains" (sección 1) |
| 3 | APQC PCF: categoría 4 "Deliver physical products", 4.1 planificación de la cadena, 4.4 entrega/logística | Corregida | En la 7.4 la categoría 4.0 es "Manage Supply Chain for Physical Products", 4.1 "Plan for and align supply chain resources" y 4.4 "Manage logistics and warehousing" (sección 2). La numeración 4.1 y 4.4 se confirma; los nombres de la primera ronda no |
| 4 | SCOR DS: siete procesos Plan, Source, Transform, Order, Fulfill, Return, Orchestrate | Corregida (depende de la versión) | El SCOR DS que ASCM publica en su sitio (PDF "SCOR Digital Standard", v13, 2020) tiene seis: Plan, Source, Make, Deliver, Return, Enable. La versión de siete procesos solo consta en Wikipedia (y en un fragmento del buscador sobre la v14); el estándar 2022 de ASCM no se pudo leer (sección 2) |
| 5 | Cinco atributos de nivel 1: confiabilidad, capacidad de respuesta, agilidad, costo, activos | Confirmada (v13) | El mismo PDF de ASCM: Reliability, Responsiveness, Agility, Costs, Asset Management; con sus 10 métricas de nivel 1 (sección 2). Ajuste: el quinto es "Asset Management", no "Asset Management Efficiency" (nombre de la v12 en la memoria de la primera ronda) |
| 6 | SCOR, 1996, PRTM y AMR Research | Confirmada en parte | El PDF de ASCM dice "The SCOR model was established in 1996" y que ASCM es producto de la fusión del Supply Chain Council y APICS en 2014. Los nombres PRTM y AMR siguen solo en Wikipedia |
| 7 | CSCP, CLTD y CPIM como mapa del cuerpo de conocimiento | Sin fuente | ASCM bloqueada. Solo consta que el PDF de SCOR cita "APICS Certified Supply Chain Professional training" (código HT.0007) |
| 8 | Oliver y Webber (1982), "Supply-chain management: logistics catches up with strategy", Outlook, Booz Allen Hamilton | Confirmada en parte | Existe y está reeditado: Oliver, Webber, "Supply-Chain Management: Logistics Catches up with Strategy", en *The Roots of Logistics*, Springer 2012, pp. 183-194, DOI 10.1007/978-3-642-27922-5_15 (Crossref, https://api.crossref.org/works/10.1007/978-3-642-27922-5_15). El año 1982 y "Outlook" no se pudieron ver en una fuente; el texto no se pudo abrir (Springer 404) |
| 9 | Keith Oliver, Booz Allen Hamilton, introdujo el término en 1982 en el Financial Times | Sin fuente primaria | Solo Wikipedia: https://en.wikipedia.org/wiki/Supply_chain_management. La nota "Handfield" de esa página no se pudo leer |
| 10 | Lo de "tres décadas" de uso del término | Confirmada | Ellram y Cooper (2014), JSCM 50(1):8-20: "With over three decades of the use of the term 'supply chain management'..." https://api.crossref.org/works/10.1111/jscm.12043. Lummus y Vokurka (1999): "Interest in supply chain management has steadily increased since the 1980s" https://api.crossref.org/works/10.1108/02635579910243851 |
| 11 | Levinson, *The Box*: Ideal X en 1956, McLean | Confirmada en parte | Editorial: "In April 1956, a refitted oil tanker carried fifty-eight shipping containers from Newark to Houston." https://press.princeton.edu/books/paperback/9780691170817/the-box . La editorial dice abril de 1956 y 58 contenedores; el día 26 y el nombre "Ideal X" siguen solo en Wikipedia. Los capítulos 1 a 3 y 9 que recomendó la primera ronda: sin fuente |
| 12 | Forrester 1958 (artículo de HBR) frente a 1961 (libro) | Confirmada en parte | El artículo "Industrial Dynamics: A Major Breakthrough for Decision Makers" existe y está reeditado en *The Roots of Logistics* (2012), pp. 141-172, DOI 10.1007/978-3-642-27922-5_13 (Crossref). El año 1958 y "HBR" no constan en la fuente. El glosario del CSCMP dice "Forrester's Industrial Dynamics (1961)" |
| 13 | Lee, Padmanabhan y Whang: cuatro causas | Confirmada | Management Science 43(4):546-558, abstract literal en la sección 4.1 |
| 14 | Cachon, Randall y Schmidt: "wholesale... bullwhip... retail generally do not" | Confirmada, con abstract completo | Sección 4.1. La cita de la primera ronda era exacta |
| 15 | "El efecto látigo es menos común de lo que dicen los libros" | Corregida | Depende del nivel de agregación. Industrias de EE.UU. (Cachon et al.): casi no. Empresas públicas de EE.UU. (Bray y Mendelson 2012): "about two-thirds of firms bullwhip". Sección 4.1 |
| 16 | Competencias M: M1 y M3, "lo simple gana" | Confirmada | Conclusiones de M5 (preprint): M1 simple exponential smoothing; M3 "simple methods outperformed the relatively more complex ones" (sección 5) |
| 17 | M4: 12 de los 17 mejores eran combinaciones; ML puro, mal; ganador híbrido casi 10 % mejor | Confirmada con literal | Abstract de M4 2018 (sección 5) |
| 18 | M4: "hybrid approaches and combination of methods is the way forward" como cita | Corregida | Esa frase no está en el abstract. El abstract dice que describe "what the authors consider to be the way forward" y que el híbrido fue la sorpresa. La cita textual de la primera ronda no se pudo verificar |
| 19 | M5: ML puro ganó a todos los métodos estadísticos y sus combinaciones | Confirmada | Preprint de M5 (sección 5). Matiz: el ganador usó una combinación de pesos iguales de 6 modelos. "Combinar" sigue valiendo |
| 20 | S&OP, Thomé et al. (2012) "S&OP and the firm performance" | Corregida | Es IJPPM 61(4):359-381, de Tavares Thomé, Scavarda, Fernandez y Scavarda; abstract literal en la sección 6. El de IJPE 138(1):1-13 es otro (*A research synthesis*); su abstract no está accesible |
| 21 | "S&OP no siempre mejora el desempeño" (literatura: Grimson y Pyke 2007; Tuomikangas y Kaipia 2014; Thomé, Hollmann y Carmo 2014) | Corregida | Grimson y Pyke 2007 existe (IJLM 18(3):322-346) y es un marco de madurez, no mide efecto en desempeño. Tuomikangas y Kaipia 2014 existe (IJPE 154:243-262), sin abstract. "Thomé, Hollmann y Carmo 2014" es sobre CPFR, no sobre S&OP. El estudio con datos que sí hay es Thomé, Sousa y do Carmo (2014, IMDS 114(5)), que halla efecto positivo. Detalle en la sección 6 |
| 22 | Maister (1976) y la ley de la raíz cuadrada | Confirmada, con ajuste | IJPD 6(3):124-134. Maister habla de inventario total, no solo de stock de seguridad (sección 7) |
| 23 | Eppen (1979) para el caso normal | Confirmada | Management Science 25(5):498-501; abstract literal en la sección 7 |
| 24 | Zinn, Levy y Bowersox (1989) | Sin fuente | No apareció en Crossref. Se reemplaza por Oeser (2019), que sí mide el error de la ley con 26 casos (sección 7) |
| 25 | La ley "exagera" el ahorro | Confirmada, con dato | Oeser (2019), IJRDM 47(3):292-310: "The SRL seems to mostly overestimate inventory savings from centralisation" (sección 7) |
| 26 | Naylor, Naim y Berry (1999): leagility, lean aguas arriba y ágil aguas abajo | Confirmada la referencia; sin fuente el contenido | IJPE 62(1-2):107-118, DOI 10.1016/s0925-5273(98)00223-0. Sin abstract |
| 27 | Ivanov y la "viable supply chain" | Confirmada | Ivanov (2020), Annals of Operations Research 319(1):1411-1431 (sección 8) |
| 28 | Sheffi y Rice (resiliencia por redundancia o flexibilidad); Sheffi 2005 | Sin fuente | No se encontró su texto ni abstract. Solo hay referencias a obras posteriores de Sheffi |
| 29 | DDMRP: lo propone el Demand Driven Institute (Ptak y Smith); buffers por consumo real; evidencia independiente escasa | Confirmada en parte | Revisión sistemática independiente (Azzamouri et al. 2021): "DDMRP is not yet a mature method". Que lo propuso el Demand Driven Institute: sin fuente en esta ronda (sección 6) |
| 30 | "Pedido perfecto: completo, a tiempo, sin daño y con documentos correctos" | Confirmada | Glosario del CSCMP, cuatro criterios literales (sección 9) |
| 31 | "CSCMP separa logística como parte de la gestión de la cadena" | Confirmada | CSCMP: "Logistics management is that part of supply chain management..." (sección 9). El Council of Logistics Management (el CSCMP anterior) lo cambió en 1998 (Lambert, Cooper y Pagh 1998) |
| 32 | Incoterms: reglas de la ICC sobre quién asume costo y riesgo del transporte | Confirmada en parte | Glosario CSCMP: "International terms of sale developed by the International Chamber of Commerce to define sellers' and buyers' responsibilities." Costo y riesgo: sin fuente (ICC no leída; es de otro ángulo) |
| 33 | "Lo agregado se pronostica mejor que lo detallado" | Sin fuente / no sostenida | FPP3 no dice eso (sección 5.4). Lo que sí está: el agrupamiento reduce la variabilidad relativa (Eppen 1979) |
| 34 | MRP y DRP históricos (Orlicky 1975; Martin 1983) | Sin fuente | El glosario del CSCMP define DRP, pero sin autor ni año |
| 35 | Logística militar; Heskett, Glaskowsky e Ivie (1964) | Sin fuente | Solo reseñas indirectas en *Journal of Marketing* (Crossref); no se leyó el libro |
| 36 | "Tercerizar siempre baja costos" | Sin fuente | Sin búsqueda posible (presupuesto agotado) |
| 37 | Lista de revistas y asociaciones (sección 5 de la primera ronda) | Confirmada en parte | Existencia de artículos en *J. of Business Logistics* (Mentzer 2001), *Int. J. of Logistics Management* (Cooper et al. 1997), *IJPE*, *IJF*, *Management Science*, *MSOM*, *JSCM*, *IJPDLM*, *IMDS*. *J. Operations Management*, *Transportation Science*, la relación de JBL con el CSCMP y MITx: sin fuente |
| 38 | Dantzig y Ramser (1959), Croston (1972), Syntetos y Boylan, Hyndman y Koehler (2006) | Confirmadas las referencias | Dantzig y Ramser, *Management Science* 6(1):80-91; Croston, JORS 23(3):289-303; Syntetos y Boylan 2005, IJF 21(2):303-314; Hyndman y Koehler, IJF 22(4):679-688 (Crossref) |

## 1. Fisher 1997

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Fisher, "What Is the Right Supply Chain for Your Product?", HBR, marzo-abril 1997, producto 8509 (PDF en servidor de la Universidad de Patras): https://eclass.upatras.gr/modules/document/file.php/MECH1277/%CE%95%CE%A1%CE%93%CE%91%CE%A3%CE%99%CE%95%CE%A3-PAPERS%20%CE%91%CE%9D%CE%9F%CE%99%CE%9E%CE%97%202024/2-Right%20Supply%20Chain%20B.pdf | primaria (copia) | 3/3/3/3 | [L] texto completo extraído |

### Afirmaciones (literales)

- Qué es un producto funcional: "Functional products include the staples that people buy in a wide range of retail outlets, such as grocery stores and gas stations. Because such products satisfy basic needs, which don't change much over time, they have stable, predictable demand and long life cycles. But their stability invites competition, which often leads to low profit margins."
- El innovador: las empresas introducen innovaciones "to give customers an additional reason to buy their offerings. Fashion apparel and personal computers are obvious examples".
- Tabla "Functional Versus Innovative Products: Differences in Demand" (Functional, "Predictable Demand"; Innovative, "Unpredictable Demand"):

| Aspect of demand | Functional | Innovative |
|---|---|---|
| Product life cycle | more than 2 years | 3 months to 1 year |
| Contribution margin* | 5% to 20% | 20% to 60% |
| Product variety | low (10 to 20 variants per category) | high (often millions of variants per category) |
| Average margin of error in the forecast at the time production is committed | 10% | 40% to 100% |
| Average stockout rate | 1% to 2% | 10% to 40% |
| Average forced end-of-season markdown as percentage of full price | 0% | 10% to 25% |
| Lead time required for made-to-order products | 6 months to 1 year | 1 day to 2 weeks |

  (* "The contribution margin equals price minus variable cost divided by price and is expressed as a percentage.")
- Tabla "Physically Efficient Versus Market-Responsive Supply Chains":

| | Physically efficient process | Market-responsive process |
|---|---|---|
| Primary purpose | supply predictable demand efficiently at the lowest possible cost | respond quickly to unpredictable demand in order to minimize stockouts, forced markdowns, and obsolete inventory |
| Manufacturing focus | maintain high average utilization rate | deploy excess buffer capacity |
| Inventory strategy | generate high turns and minimize inventory throughout the chain | deploy significant buffer stocks of parts or finished goods |
| Lead-time focus | shorten lead time as long as it doesn't increase cost | invest aggressively in ways to reduce lead time |
| Approach to choosing suppliers | select primarily for cost and quality | select primarily for speed, flexibility, and quality |
| Product-design strategy | maximize performance and minimize cost | use modular design in order to postpone product differentiation for as long as possible |

- La matriz: "The four cells of the matrix represent the four possible combinations of products and priorities." Y: "Companies that have either an innovative product with an efficient supply chain (upper right-hand cell) or a functional product with a responsive supply chain (lower left-hand cell) tend to be the ones with problems." La figura de la matriz es una imagen y no se extrajo; el texto describe las celdas.
- Argumento económico: "Consider a typical innovative product with a contribution margin of 40% and an average stockout rate of 25%. The lost contribution to profit and overhead resulting from stockouts alone is huge: 40% x 25% = 10% of sales—an amount that usually exceeds profits before taxes." Para el funcional: "A contribution margin of 10% and an average stockout rate of 1% mean lost contribution to profit and overhead of only .1% of sales".
- Dos tipos de costo: "Physical costs are the costs of production, transportation, and inventory storage"; los de "mediation" surgen "when supply exceeds demand" o al revés (texto extraído; la frase completa está cortada por el formato de dos columnas).

### Qué registra un sistema

Por familia de producto: la clasificación funcional o innovador (con sus indicadores: ciclo de vida, margen de contribución, variedad, error de pronóstico, tasa de quiebre, liquidación forzada, plazo de pedido) y la estrategia de cadena asignada (eficiente o que responde). Es inferencia sobre las tablas, no cita.

### Recurso canónico

El artículo completo, las dos tablas y la matriz. En qué fijarse: los indicadores de la primera tabla son los atributos que un sistema tendría que poder calcular por familia para ubicarla.

## 2. Marcos

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| APQC Process Classification Framework, Cross Industry, versión 7.4, © 2024 APQC (PDF del brief) | primaria | 3/3/2/3 | [L] categoría 4 completa |
| ASCM, *SCOR Digital Standard* (introducción y texto previo, © ASCM 2020, "SCOR v13 Updates"): https://www.ascm.org/globalassets/ascm_website_assets/docs/intro-and-front-matter-scor-digital-standard.pdf | primaria | 3/2/2/3 | [L] 695 líneas de texto; solo la introducción, no los procesos de nivel 2 y 3 |
| https://en.wikipedia.org/wiki/Supply-chain_operations_reference (de la primera ronda) | secundaria | 1/2/1/1 | [S] |
| Páginas de ASCM (`scor-ds`, `scor.ascm.org`) | primaria | – | no accesibles (protección anti-bots, 404) |

### 2.1 APQC PCF 7.4, categoría 4 (literal, con el código APQC entre paréntesis)

**4.0 Manage Supply Chain for Physical Products (20022)**

**4.1 Plan for and align supply chain resources (10215)**, nivel 3:
- 4.1.1 Develop production and materials strategies (10221)
- 4.1.2 Manage demand for products (10222)
- 4.1.3 Create materials plan (10223)
- 4.1.4 Create and manage master production schedule (10224)
- 4.1.5 Plan distribution requirements (17042)
- 4.1.6 Establish distribution planning constraints (10226)
- 4.1.7 Review distribution planning policies (10227)
- 4.1.8 Develop quality standards and procedures (10368)

Los de nivel 4 que importan a este tema:
- 4.1.2 Manage demand for products: 4.1.2.1 Develop baseline demand forecasts; 4.1.2.2 Collaborate demand with customers; 4.1.2.3 Develop demand consensus forecast; 4.1.2.4 Determine available to promise; 4.1.2.5 Monitor activity against demand forecast and revise forecast; 4.1.2.6 Evaluate and revise demand forecasting approach; 4.1.2.7 Measure demand forecast accuracy.
- 4.1.5 Plan distribution requirements: 4.1.5.1 Maintain master data; .2 Determine finished goods inventory requirements at destination; .3 Determine product storage facility requirements; .4 Calculate requirements at destination; .5 Calculate consolidation at source; .6 Manage collaborative replenishment planning; .7 Calculate and optimize destination dispatch plan; .8 Manage dispatch plan attainment; .9 Calculate and optimize destination load plans; .10 Manage partner load plan; .11 Manage cost of supply; .12 Manage capacity utilization.
- 4.1.6: .1 Establish distribution center layout constraints; .2 inventory management constraints; .3 transportation management constraints; .4 storage management constraints.
- 4.1.7: .1 Review distribution network; .2 Establish sourcing relationships; .3 Establish dynamic deployment policies.

**4.4 Manage logistics and warehousing (10219)**, nivel 3:
- 4.4.1 Provide logistics governance (10338): 4.4.1.1 Translate customer service requirements into logistics requirements; .2 Design logistics network; .3 Communicate outsourcing needs; .4 Develop and maintain delivery service policy; .5 Optimize transportation schedules and costs; .6 Define key performance measures; .7 Define reverse logistics strategy.
- 4.4.2 Plan and manage inbound material flow (20936): .1 Plan inbound material receipts; .2 Manage inbound material flow; .3 Monitor inbound delivery performance; .4 Manage flow of returned products; .5 Manage disposition of returned products (con .5.1 Determine quality of controlled part, .5.2 Perform salvage activities, .5.3 Manage repair/refurbishment, .5.4 Return to finished goods inventory).
- 4.4.3 Operate warehousing (10340): .1 Manage and track inventory deployment; .2 Receive, inspect, and store inbound deliveries; .3 Track product availability; .4 Pick, pack, and ship product for delivery; .5 Track inventory accuracy; .6 Track third-party logistics storage and shipping performance; .7 Manage physical finished goods inventory; .8 Manage warehouse transfers.
- 4.4.4 Operate outbound transportation (10341): .1 Plan, transport, and deliver outbound product; .2 Track carrier delivery performance; .3 Manage transportation fleet; .4 Process and audit carrier invoices and documents.

Hallazgos para el árbol:
- Los límites del tema coinciden de cerca con el PCF: lo de este tema es 4.1.2 (demanda), 4.1.5 a 4.1.7 (distribución), 4.4.1 (red y gobierno logístico), 4.4.2.4 y 4.4.2.5 (flujo de devoluciones) y 4.4.4 (transporte de salida). 4.4.3 (almacén) es de Inventario y depósitos. 4.1.1, 4.1.3, 4.1.4 (materiales, plan maestro) son de Producción; 4.2 es de Compras.
- El PCF no tiene un nodo de S&OP: lo más cercano es 4.1.2.3 "Develop demand consensus forecast". Es una diferencia con SCOR y con el CSCMP, que sí lo nombran.
- El PCF no tiene comercio exterior ni aduana en la categoría 4. No se buscó en el resto del PDF.
- Primera ronda dijo que 4.4 era "entrega/logística"; es "Manage logistics and warehousing", e incluye el depósito.

### 2.2 SCOR Digital Standard (documento de ASCM, © 2020, "SCOR v13 Updates")

- Procesos de nivel 1: "The reference model ... is organized around the six primary management processes of Plan, Source, Make, Deliver, Return and Enable." En la sección Process: "The six macro-level SCOR processes, Plan, Source, Make, Deliver, Return and Enable". Códigos: "sP represents Plan, sS identifies Source, sM labels Make, sD denotes Deliver, and sR marks Return." Los de retorno se parten en "Source Return (sSR) and Deliver Return (sDR)".
- Cuatro secciones: "Performance ... Processes ... Practices ... People".
- Atributos (Tabla 1):
  - "Reliability: The ability to perform tasks as expected. Reliability focuses on the predictability of the outcome of a process. Typical metrics for the Reliability attribute include delivering a product on time, in the right quantity and at the right quality level."
  - "Responsiveness: The speed at which tasks are performed and the speed at which a supply chain provides products to the customer."
  - "Agility: The ability to respond to external influences and marketplace changes to gain or maintain a competitive advantage."
  - "Costs: The cost of operating the supply chain processes."
  - "Asset Management: The ability to efficiently utilize assets."
  - "Reliability, Responsiveness and Agility are considered customer-focused. Cost and Asset Management are considered internally focused."
- Métricas de nivel 1 (Tabla 2), literal:

| Atributo | Métrica de nivel 1 |
|---|---|
| Reliability | Perfect Order Fulfillment (RL.1.1) |
| Responsiveness | Order Fulfillment Cycle Time (RS.1.1) |
| Agility | Upside Supply Chain Adaptability (AG.1.1); Downside Supply Chain Adaptability (AG.1.2); Overall Value at Risk (AG.1.3) |
| Cost | Total Supply Chain Management Costs (CO.1.1); Cost of Goods Sold (COGS) (CO.1.2) |
| Asset Management | Cash-to-Cash Cycle Time (AM.1.1); Return on Fixed Assets (AM.1.2); Return on Working Capital (AM.1.3) |

- Nivel 2: "Make-to-Stock, Make-to-Order and Engineer-to-Order for Source, Make and Deliver processes and Defective; Maintenance, Repair and Overhaul; and Excess for Return processes." Ejemplo de nivel 3: "sD1.1 for Process Inquiry and Quote and sD1.2 for Receive, Enter and Validate Order".
- Alcance: "SCOR spans all customer interactions from order entry through paid invoice; all physical material transactions ... from the supplier's supplier to the customer's customer ... and all market interactions from the understanding of aggregate demand to the fulfillment of each order." Y: "SCOR does not address sales and marketing, including demand generation; product development; or research and development."
- Jerarquía: "ASCM has focused on the top three process levels, which are industry neutral." "Every organization ... will need to extend the model, at least to level 4".
- Familia de marcos: "DCOR", "SCOR" y "M4SC" (este último "translates business strategies into supply chain execution plans and policies").
- Historia: "The SCOR model was established in 1996"; "ASCM (formerly APICS) following the merger of the Supply Chain Council and APICS in 2014".
- Qué cambió en la v13: se agregó la métrica "Risk Mitigation Costs (Enable) (CO.3.23)" y 19 prácticas emergentes (entre ellas "Digital Twin", "Machine Learning", "Dynamic Routing").
- La versión de siete procesos (Plan, Source, Transform, Order, Fulfill, Return, Orchestrate):
  - Wikipedia (primera ronda) la atribuye a la versión de 2022.
  - Un fragmento del buscador sobre un documento no identificado [S]: "Six supply chain processes (plan, source, transform, order, fulfill, return) sit within these loops, all underpinned by the orchestration process." y que ASCM tiene un "SCOR 14.0".
  - No se pudo abrir ningún texto primario de esa versión. La primera ronda confundió los dos: las dos versiones existen. Hay que citar la versión que se mire.
- Discrepancia sobre atributos: la v13 coincide con los cinco de la primera ronda. No se sabe si la versión 2022 los cambió; no se leyó.

### 2.3 Qué registra un sistema

SCOR define métricas con códigos, no objetos, pero de las de nivel 1 se derivan los datos mínimos: pedido (fecha prometida, fecha real, completo o no, condición, documentación: "Perfect Order Fulfillment", "Perfect Condition (RL.2.4)"), ciclo del pedido ("Order Fulfillment Cycle Time"), y devolución (con su tipo: defectuosa, MRO, exceso). El PCF suma objetos de distribución: plan de despacho, plan de carga por destino, requerimiento por destino y consolidación en origen (4.1.5). Es inferencia sobre los títulos, no cita.

### 2.4 Recurso canónico

- SCOR DS: la introducción de ASCM (la tabla de atributos y la de métricas de nivel 1) y, de la versión vigente, las definiciones de cálculo de cada métrica. En qué fijarse: qué cuenta como pedido perfecto. Hueco: no se leyeron los niveles 2 y 3.
- APQC PCF 7.4: la categoría 4, páginas 11 y 12 del PDF. En qué fijarse: la numeración de cada nodo (sirve de código de proceso para el árbol).

## 3. Oliver y Webber (1982) y el origen del término

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Crossref, Oliver y Webber (reedición): https://api.crossref.org/works/10.1007/978-3-642-27922-5_15 | metadatos | 2/1/1/2 | [M] |
| Lummus y Vokurka (1999), IMDS 99(1):11-17, https://api.crossref.org/works/10.1108/02635579910243851 | primaria | 2/2/1/2 | [M] abstract |
| Cooper, Lambert y Pagh (1997), IJLM 8(1):1-14, https://api.crossref.org/works/10.1108/09574099710805556 | primaria | 3/2/1/3 | [M] |
| Lambert, Cooper y Pagh (1998), IJLM 9(2):1-20, https://api.crossref.org/works/10.1108/09574099810805807 | primaria | 3/2/1/2 | [M] |
| Mentzer et al. (2001), JBL 22(2):1-25, https://api.crossref.org/works/10.1002/j.2158-1592.2001.tb00001.x | primaria | 3/3/2/3 | [M] |
| Ellram y Cooper (2014), JSCM 50(1):8-20 | primaria | 3/2/1/2 | [M] |

### Afirmaciones

- El artículo existe como capítulo reeditado: Oliver y Webber, "Supply-Chain Management: Logistics Catches up with Strategy", *The Roots of Logistics*, Springer, 2012, pp. 183-194. No se pudo leer ni confirmar 1982 y *Outlook* en una fuente abierta. Lo único comprobable es el título y los dos autores. Por tanto: la atribución "Oliver y Webber (1982)" del brief y "Oliver, entrevista del FT, 1982" de Wikipedia no se resolvieron entre sí.
- La distinción logística y cadena como concepto: Lummus y Vokurka: "The term does not replace supplier partnerships, nor is it a description of the logistics function." Cooper, Lambert y Pagh: "there is a need for some level of coordination of activities and processes within and between organizations in the supply chain that extends beyond logistics. We believe that this is what should be called SCM." Lambert, Cooper y Pagh: "In 1998, the Council of Logistics Management modified its definition of logistics to indicate that logistics is a subset of supply chain management and that the two terms are not synonymous."
- Mentzer et al.: "so many definitions are used that there is little consensus on what it means". Un buen insumo para decir que el término no tiene una definición única.
- Ellram y Cooper: "With over three decades of the use of the term 'supply chain management', five academic and practitioner perspectives of supply chain management are described."

### Huecos

El texto de Oliver y Webber y la nota de Wikipedia "Handfield" (supuestamente la fuente de la atribución a Oliver). Si no se consiguen, la nota debe decir "se atribuye a Keith Oliver, de Booz Allen Hamilton, hacia 1982" y marcarlo como atribución.

## 4. Efecto látigo: Cachon, Randall y Schmidt (2007) y Bray y Mendelson (2012)

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Cachon, Randall y Schmidt (2007), MSOM 9(4):457-479, https://doi.org/10.1287/msom.1060.0149 (abstract vía https://api.openalex.org/works/doi:10.1287/msom.1060.0149) | primaria | 3/3/2/3 | [M] abstract completo |
| Bray y Mendelson (2012), Management Science 58(5):860-875, https://doi.org/10.1287/mnsc.1110.1467 (abstract vía https://api.crossref.org/works/10.1287/mnsc.1110.1467) | primaria | 3/3/2/3 | [M] abstract completo |
| Lee, Padmanabhan y Whang (1997), Management Science 43(4):546-558, https://doi.org/10.1287/mnsc.43.4.546 | primaria | 3/3/2/3 | [M] |

### 4.1 Afirmaciones (abstracts literales)

- Cachon, Randall y Schmidt: "The bullwhip effect is the phenomenon of increasing demand variability in the supply chain from downstream echelons (retail) to upstream echelons (manufacturing). The objective of this study is to document the strength of the bullwhip effect in industry-level U.S. data. In particular, we say an industry exhibits the bullwhip effect if the variance of the inflow of material to the industry (what macroeconomists often refer to as the variance of an industry's "production") is greater than the variance of the industry's sales. We find that wholesale industries exhibit a bullwhip effect, but retail industries generally do not exhibit the effect, nor do most manufacturing industries. Furthermore, we observe that manufacturing industries do not have substantially greater demand volatility than retail industries. Based on theoretical explanations for observing or not observing demand amplification, we are able to explain a substantial portion of the heterogeneity in the degree to which industries exhibit the bullwhip effect. In particular, the less seasonal an industry's demand, the more likely the industry amplifies volatility—highly seasonal industries tend to smooth demand volatility whereas nonseasonal industries tend to amplify."
- Bray y Mendelson (2012): "The bullwhip effect is the amplification of demand variability along a supply chain: a company bullwhips if it purchases from suppliers more variably than it sells to customers. ... We investigate the bullwhip effect in a sample of 4,689 public U.S. companies over 1974–2008. Overall, about two-thirds of firms bullwhip. The sample's mean and median bullwhips, both significantly positive, respectively measure 15.8% and 6.7% of total demand variability. ... From 1974–1994 to 1995–2008, our sample's mean bullwhip dropped by a third."
- Lee, Padmanabhan y Whang (1997): "the variance of orders may be larger than that of sales, and the distortion tends to increase as one moves upstream—a phenomenon termed 'bullwhip effect.' This paper analyzes four sources of the bullwhip effect: demand signal processing, rationing game, order batching, and price variations."
- Primera ronda dijo "5 % a 40 %" (cifra de Wikipedia): sigue sin fuente.

### 4.2 Las dos fuentes discrepan, y por qué

- Cachon et al.: datos de industrias enteras (agregados). El resultado es que la mayoría de las industrias minoristas y manufactureras no amplifican.
- Bray y Mendelson: datos de empresas. Dos tercios amplifican, con una media chica (15,8 % de la variabilidad total, mediana 6,7 %).
- Las dos son compatibles, porque medir por industria suaviza lo que pasa dentro de cada una. La nota no debe decir ni "el látigo casi no existe" ni "lo sufren todos": el efecto es real en la mayoría de las empresas, es de magnitud moderada y se atenúa con la estacionalidad (producir antes y suavizar) y con la información a tiempo. Matiz de Bray y Mendelson sobre la causa: las señales de demanda que la empresa conoce con menos de un trimestre de aviso explican 51 % del látigo, y con más de tres cuartos de aviso, 30 %.
- Primera ronda sostuvo "el efecto látigo es menos común de lo que dicen los libros" apoyándose solo en Cachon. Con Bray y Mendelson sobre la mesa, la frase solo vale para industrias agregadas.

### 4.3 Qué registra un sistema

Dos series por eslabón y período: pedidos emitidos y ventas (o despachos), para calcular la razón de varianzas, que es la definición operativa de ambos estudios ("the variance of the inflow ... greater than the variance of ... sales" o, en la empresa, "purchases from suppliers more variably than it sells"). Inferencia sobre las definiciones.

### 4.4 Recurso canónico

Cachon, Randall y Schmidt (2007), secciones de definición y datos, y Bray y Mendelson (2012). Fijarse en el nivel de agregación y en el control por estacionalidad. No se leyó el texto completo de ninguno.

## 5. Competencias M

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| M4 2018: Makridakis, Spiliotis y Assimakopoulos, "The M4 Competition: Results, findings, conclusion and way forward", IJF 34(4), https://doi.org/10.1016/j.ijforecast.2018.06.001 (abstract vía https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.ijforecast.2018.06.001) | primaria | 3/3/2/3 | [M] abstract completo |
| M4 2020: "The M4 Competition: 100,000 time series and 61 forecasting methods", IJF 36(1), https://doi.org/10.1016/j.ijforecast.2019.04.014 | primaria | 3/3/2/3 | [M] abstract; el texto da 403 en ScienceDirect |
| M5: "M5 accuracy competition: Results, findings, and conclusions", IJF 38(4):1346-1364 (2022), https://econpapers.repec.org/RePEc:eee:intfor:v:38:y:2022:i:4:p:1346-1364 | primaria | 3/3/3/3 | [M] abstract |
| Copia preprint del mismo artículo, https://statmodeling.stat.columbia.edu/wp-content/uploads/2021/10/M5_accuracy_competition.pdf (título de portada "The M5 Accuracy competition: Results, findings and conclusions") | primaria (preprint) | 3/3/3/3 | [L] texto completo extraído; la paginación no coincide con la final |
| Página de la competencia: https://www.unic.ac.cy/iff/research/forecasting/m5-competition/ | secundaria | 2/1/1/2 | [L] |

### Afirmaciones (literales)

- M4 2018, abstract: "The five major findings of the M4 Competitions are: 1. Out Of the 17 most accurate methods, 12 were "combinations" of mostly statistical approaches. 2. The biggest surprise was a "hybrid" approach that utilized both statistical and ML features. This method's average sMAPE was close to 10% more accurate than the combination benchmark used to compare the submitted methods. 3. The second most accurate method was a combination of seven statistical methods and one ML one, with the weights for the averaging being calculated by a ML algorithm ... 4. The two most accurate methods also achieved an amazing success in specifying the 95% prediction intervals correctly. 5. The six pure ML methods performed poorly, with none of them being more accurate than the combination benchmark and only one being more accurate than Naive2."
- M4 2020, abstract: "The aim of M4 was to replicate and extend the three previous competitions by: (a) significantly increasing the number of series, (b) expanding the number of forecasting methods, and (c) including prediction intervals in the evaluation process as well as point forecasts."
- M5, abstract del preprint: la competencia "extended the results of the previous four competitions by: (a) significantly expanding the number of participating methods, especially those in the category of Machine Learning, (b) including exogenous/explanatory variables in addition to the time series data, (c) using grouped, correlated time series, and (d) focusing on series that display intermittency." Abstract final (EconPapers): "to accurately predict 42,840 time series representing the hierarchical unit sales for the largest retail company in the world by revenue, Walmart."
- M5, conclusiones (preprint, sección 6), historia de las cuatro anteriores:
  - M1: "a simple exponential smoothing method rather than the statistically sophisticated Box-Jenkins methodology to ARIMA models. In addition, the competition established the value of combining".
  - M2: "human judgment did not improve the accuracy of the statistical forecasts and combining was the most accurate way".
  - M3 (3.003 series): "simple methods outperformed the relatively more complex ones, with a new simple method, called Theta ..., being the most accurate of all others on average, and forecast combinations continuing to produce more accurate results than the individual methods being combined."
  - M4: "the M4 ended a long forecasting winter by reversing the findings of the previous three competitions and concluding that two sophisticated methods, using a mixture of statistical and ML concepts, outperformed all others".
  - M5: "the M5 that proved the superiority of ML methods, particularly the LightGBM, with the 50 top-performing ones achieving a superior performance of more than 14% over the most accurate statistical benchmark and the top five more than 20%."
  - Síntesis: "What has remained constant in all five M competitions is the finding that combining improves forecasting accuracy. What has changed is the finding of M1, M2, and M3 that simple statistical methods were more accurate than more complex, sophisticated ones. In M4, only two sophisticated methods were found to be more accurate than simple, statistical ones ... On the contrary, in the M5 all 50 top-performing methods were ML. Therefore, M5 is the first M competition where all top-performing methods were both ML ones and significantly better than all statistical benchmarks and their combinations."
- M5, "Finding 2: The value of combining": "The winner of the M5 Accuracy competition employed a very simple, equal-weighted combination, involving 6 models, each one exploiting a different learning approach and train set." Es decir, combinar sigue valiendo dentro del ML.
- M5, tres hallazgos nuevos: "The superior accuracy of the LightGBM method"; "The benefits of external adjustments"; "The importance of exogenous/explanatory variables". Y los tres que se reafirman: "Combining", "Cross-learning", "Cross-validation".
- Contexto de M5: "The majority of the 42,840 time series display intermittency (sporadic sales including zeros)"; "around 100,000 submissions from more than 100 countries" (página de la competencia).

### Implicación para la nota

- "Lo simple gana" vale para M1 a M3 y, con matiz, para M4 (solo dos métodos sofisticados ganaron, y eran híbridos con base estadística). En M5 no vale: ganó el aprendizaje automático con datos de ventas jerárquicos, con variables explicativas y series intermitentes.
- Lo que sí se sostiene en las cinco: combinar mejora la precisión.
- Para la nota: el método simple (ingenuo, estacional, suavizado) es el piso de comparación, no el techo. Qué método rinde depende del volumen de series, de si hay variables externas y de la jerarquía.
- La cita "hybrid approaches and combination of methods is the way forward" de la primera ronda no se encontró en el abstract de M4 2018; no usarla como literal.
- El texto completo de M4 (2020) no se pudo leer. Lo que se sabe de M4 sale del abstract de 2018 y de lo que dice M5 sobre M4.

### Qué registra un sistema

La serie por artículo-ubicación-período con la jerarquía (producto, tienda, región, total), las variables explicativas (precio, evento, calendario), el método y su versión, y la métrica de error contra un pronóstico de referencia. M5 muestra que la jerarquía y las variables externas son datos de primera clase. Inferencia sobre el abstract.

### Recurso canónico

M5, sección 6 (conclusiones) y la sección de hallazgos 1 y 2; M4 2018, el abstract. Fijarse en que cada competencia tuvo datos distintos (M5 son ventas de una cadena minorista).

## 6. DDMRP y S&OP: evidencia independiente

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Azzamouri, Baptiste, Dessevre y Pellerin (2021), JIEM 14(3):439-456, https://jiem.org/index.php/jiem/article/view/3331 (abstract completo vía https://api.crossref.org/works/10.3926/jiem.3331) | primaria (revisión sistemática) | 2/3/1/3 | [M] |
| Tavares Thomé, Scavarda, Fernandez y Scavarda (2012), "Sales and operations planning and the firm performance", IJPPM 61(4):359-381, https://doi.org/10.1108/17410401211212643 | primaria (revisión sistemática) | 2/3/2/3 | [M] abstract completo |
| Tavares Thomé, Scavarda, Fernandez y Scavarda (2012), "Sales and operations planning: A research synthesis", IJPE 138(1):1-13, https://doi.org/10.1016/j.ijpe.2011.11.027 | primaria | 3/3/2/3 | solo metadatos: el editor retuvo el abstract |
| Thomé, Sousa y do Carmo (2014), "Complexity as contingency in sales and operations planning", IMDS 114(5):678-695, https://doi.org/10.1108/imds-10-2013-0448 | primaria (encuesta) | 2/3/2/3 | [M] abstract |
| Grimson y Pyke (2007), IJLM 18(3):322-346, https://doi.org/10.1108/09574090710835093 | primaria | 2/3/2/2 | [M] |
| Tuomikangas y Kaipia (2014), IJPE 154:243-262, https://doi.org/10.1016/j.ijpe.2014.04.026 | primaria | 3/3/2/3 | solo metadatos |

### 6.1 DDMRP

- Azzamouri et al. (abstract literal): "Demand Driven Material Requirements Planning (DDMRP) aims to deal with variability by adjusting inventory levels while maintaining, or even increasing, customer service levels. This approach bridges the push and pull approaches. Even though it first made its appearance in 2011, research in this field remains relatively limited. ... The systematic literature review approach adopted in this paper examines research dealing with the DDMRP approach published in different languages between 2009 and 2020. ... The results show that DDMRP is not yet a mature method and that the robustness of the approach still needs to be tested. More research is also required to determine scientifically some setting parameters, how the proposed DDMRP could be implemented in different industrial contexts with existing information systems."
- La revisión dice además que los trabajos anteriores "focused on the performance analysis and comparison"; esta se centra en la madurez científica. Es una revisión de la literatura, no una prueba de desempeño.
- Dos cosas que la primera ronda daba por supuestas: que lo propuso el Demand Driven Institute (Ptak y Smith) sigue sin fuente; "first made its appearance in 2011" sí consta. La fecha 2011 no coincide con la edad que se suele dar al método en las fuentes del propio instituto, que no se leyeron.
- Hueco: no se leyó ningún estudio de comparación de desempeño (simulación o caso). Miclo y otros: no encontrado. La nota puede decir "la revisión sistemática independiente más citada concluye que el método aún no es maduro y que su robustez falta probarla"; no puede decir nada sobre cuánto mejora.

### 6.2 S&OP

- IJPPM 2012, abstract literal: "The methodology adopted was a systematic literature review of 271 abstracts and 55 papers. Three databases were selected for the search – Emerald, EBSCO, and ScienceDirect. ... Although empirical evidence of the effects of S&OP in the supply chain is described, relatively few of the 55 papers reviewed estimate the effect of S&OP on firm performance. The research findings indicate a lack of unifying frameworks for the measurement of S&OP and constructs related to firm performance. The review offers partial evidence of the effect of S&OP on firm performance, suggesting the need for additional scientifically sound survey or case study research on S&OP." Y: "There is at least partial evidence that cross-functional planning processes can mitigate the negative effect of misaligned organisational structures and contradictory incentives schemes on firm performance."
- Thomé, Sousa y do Carmo (2014), abstract: "using data from a sample of 725 manufacturing plants from 21 countries. ... S&OP practices of organizational management, technological integration, measurement systems and integration of plans impact positively on manufacturing operational dimensions of quality, delivery and flexibility. Process complexity moderates the effect of S&OP practices, amplifying its impact upon all three performance dimensions." Es evidencia empírica a favor, y con un límite: medida sobre plantas manufactureras y dimensiones operativas, no sobre la rentabilidad.
- Grimson y Pyke (2007), abstract: marco de madurez de cinco etapas, 15 entrevistas; "little apparent relationship was found" entre tamaño o tipo de proceso y grado de integración; "business processes are enablers of S&OP plan integration, but that information technology is not clearly so"; "Because the sample size is small, the results should be considered to provide only preliminary insights."
- Primera ronda dijo que había una "literatura que discute que el efecto depende de la madurez y de la integración". Lo comprobable: la evidencia de efecto sobre el desempeño es parcial y escasa (IJPPM 2012), las pruebas cuantitativas existentes son positivas y con moderadores (IMDS 2014), y los marcos de madurez no miden efecto. Frase para la nota: "hay evidencia parcial de que el S&OP mejora el desempeño; falta evidencia sólida y unificada". No existe en lo leído un estudio que muestre que no mejora.
- Corrección de citas de la primera ronda: "Thomé, Hollmann y Carmo 2014" es "Research synthesis in collaborative planning forecast and replenishment" (IMDS 114(6):949-965), sobre CPFR; el de S&OP es el de Thomé, Sousa y do Carmo.
- Hueco: el abstract del IJPE (el que pedía el brief) no está accesible; el contenido es probablemente cercano al de IJPPM, pero no se puede afirmar.

### 6.3 Qué registra un sistema (S&OP)

Ciclo con fecha, versión de demanda y de oferta, decisiones y responsable. Las prácticas que los estudios miden ("organizational management, technological integration, measurement systems and integration of plans") sugieren que un sistema también guarda la reunión de consenso, las métricas por función y la conciliación de los planes. Inferencia sobre el abstract.

## 7. Ley de la raíz cuadrada

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Maister (1976), IJPD 6(3):124-134, https://doi.org/10.1108/eb014366 | primaria | 3/3/2/3 | [M] abstract (primer párrafo) |
| Eppen (1979), Management Science 25(5):498-501, https://doi.org/10.1287/mnsc.25.5.498 | primaria | 3/3/2/3 | [M] abstract completo |
| Oeser (2019), IJRDM 47(3):292-310, https://doi.org/10.1108/ijrdm-05-2017-0108 | primaria (empírica) | 2/3/3/3 | [M] abstract completo |

### Afirmaciones

- Maister: "to discuss the effect on inventory levels of centralisation, i.e., moving from a logistics system formed from a number of field warehouses to one where all demands are met from a single location. In particular, we shall examine the 'square root law of locations', a result which asserts that the total inventory in a system is proportional to the square root of the number of locations at which a product is stocked."
- Eppen: "(i) the expected holding and penalty costs in a decentralized system exceed those in a centralized system; (ii) the magnitude of the saving depends on the correlation of demands; and (iii) if demands are identical and uncorrelated, the costs increase as the square root of the number of consolidated demands."
- Oeser (2019): "In 26 company cases of reducing the number of warehouses, the estimation error of the SRL is analysed irrespective of its underlying assumptions. ... The analysis reveals an average estimation error for total inventory of 27.85 per cent (median=27.84 per cent), but a high variability across the cases. The SRL seems to mostly overestimate inventory savings from centralisation and inventory increases from decentralisation." Y: "Previous empirical research, however, has shown that mostly its underlying assumptions do not hold in practice."
- Correcciones a la primera ronda: (a) la ley habla de inventario total, no solo de stock de seguridad; (b) el resultado de Eppen es sobre costos esperados y vale con demandas idénticas e incorrelacionadas; (c) "Zinn, Levy y Bowersox (1989)" no se encontró en Crossref; se sustituye por Oeser. La corrección de "exagera" queda sostenida por Oeser, con 26 casos (un solo estudio, y los casos salieron de la literatura publicada, no de una muestra al azar).

### Límite con otros temas

El stock de seguridad por artículo es de Inventario y depósitos. Este tema trata cuántos depósitos de la red, y para eso la ley es una estimación con 28 % de error medio, no una regla.

## 8. Resiliencia

- Ivanov (2020), Annals of Operations Research 319(1):1411-1431, https://doi.org/10.1007/s10479-020-03640-6, abstract literal: "Viability is the ability of a supply chain (SC) to maintain itself and survive in a changing environment through a redesign of structures and replanning of performance with long-term impacts. In this paper, we theorize a new notion—the viable supply chain (VSC). In our approach, viability is considered as an underlying SC property spanning three perspectives, i.e., agility, resilience, and sustainability." [M]. Confirma la afirmación de la primera ronda.
- Sheffi y Rice, y la OCDE y McKinsey: no se pudo verificar en esta ronda.

## 9. Levinson, *The Box*, y McLean

- Editorial (Princeton University Press): "In April 1956, a refitted oil tanker carried fifty-eight shipping containers from Newark to Houston." "Ultimately, it took McLean's success in supplying U.S. forces in Vietnam to persuade the world of the container's potential." Edición: rústica, ISBN 9780691170817, 5 de abril de 2016, 540 páginas; la descripción dice que se publicó primero en tapa dura "on the fiftieth anniversary of the first container voyage" (compatible con 2006). https://press.princeton.edu/books/paperback/9780691170817/the-box [M, editorial].
- La editorial usa "McLean" sin nombre de pila; el nombre completo aparece en una reseña del *Times* citada en la misma página. Primera ronda: "Ideal X", 26 de abril: no están en la editorial.
- Hueco: reseña académica no encontrada (no hay búsqueda disponible); los capítulos recomendados no se verificaron.

## 10. Glosario: 28 términos con fuente

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| CSCMP, *Supply Chain Management Terms and Glossary*, "Updated: August 2013" (copia en https://www.cisco-eagle.com/uploads/cscmp/cscmp-glossary.pdf; la versión oficial `cscmp.org/.../glossary-2013.pdf` dio 404). Compilado por Kate Vitasek; el propio CSCMP dice que no endosa esas definiciones salvo las que marca como oficiales | secundaria (espejo no oficial) | 2/3/2/2 | [L] las entradas leídas |
| CSCMP, página de definiciones oficiales de gestión de la cadena y de logística: https://www.cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms/Marketing%20Request | primaria | 3/2/1/3 | [S] frases iniciales |
| ASCM, diccionario | primaria | – | no accesible |
| Fisher 1997 (PDF) y FPP3 (https://otexts.com/fpp3/accuracy.html, /simple-methods.html, de la primera ronda) | primarias | 3/3/2/3 | [L] |
| Libro abierto de la Universidad de Arkansas (https://uark.pressbooks.pub/introscm/) | – | – | 403, no se leyó |

El glosario del CSCMP es de 2013, una edición vieja (para lo estable, vale). Algunas definiciones están redactadas para EE.UU. y para transporte regulado.

### Tabla (definición con fuente, y veredicto sobre la de la primera ronda)

| Término | Definición con fuente (CSCMP 2013, salvo que se indique) | Veredicto sobre la de la primera ronda |
|---|---|---|
| supply chain (cadena de suministro) | "starting with unprocessed raw materials and ending with the final customer using the finished goods, the supply chain links many companies together." | Confirmada |
| supply chain management | "Supply chain management encompasses the planning and management of all activities involved in sourcing and procurement, conversion, and all logistics management activities. Importantly, it also includes coordination and collaboration with channel partners, which can be suppliers, intermediaries, third-party service providers, and customers." (oficial en la página del CSCMP) | Confirmada; agregar "incluye abastecimiento y conversión (fabricación)" |
| logistics management | "that part of supply chain management that plans, implements, and controls the efficient, effective forward and reverse flow and storage of goods, services, and related information between the point of origin and the point of consumption in order to meet customers' requirements." | Confirmada; agregar flujo directo e inverso |
| physical distribution | "The movement and storage functions associated with finished goods from manufacturing plants to warehouses and to customers; also, used synonymously with business logistics." | Ajustar: la primera ronda dijo "antecedente de la logística"; el CSCMP la da como sinónimo de logística de negocios |
| forecast | "An estimate of future customer demand." | Confirmada |
| demand planning | "The process of identifying, aggregating, and prioritizing, all sources of demand for the integrated supply chain of a product or service at the appropriate level, horizon and interval." | Ajustar: la primera ronda dijo "generar y acordar el pronóstico"; es más amplio (todas las fuentes de demanda, nivel, horizonte e intervalo) |
| S&OP | "A strategic planning process that reconciles conflicting business objectives and plans future supply chain actions. S&OP Planning usually involves various business functions such as sales, operations and finance to agree on a single plan/forecast that can be used to drive the entire business." | Ajustar: el CSCMP no dice "mensual" ni "hasta 18 meses"; eso solo está en Wikipedia |
| DRP | "A system of determining demands for inventory at distribution centers and consolidating demand information in reverse as input to the production and materials system." (y DRP II: "integrates distribution with manufacturing") | Ajustar: la primera ronda lo limitó a "quien no fabrica"; en el CSCMP el DRP consolida la demanda de los depósitos y se la pasa a producción. El PCF lo llama "Plan distribution requirements" (4.1.5) |
| bullwhip effect | "an observed phenomenon in forecast-driven distribution channels. The oscillating demand magnification upstream a supply chain is reminiscent of a cracking whip. The concept has its roots in J Forrester's Industrial Dynamics (1961) and thus it is also known as the Forrester Effect." | Confirmada; ver la definición operativa de la sección 4 (varianza de pedidos mayor que la de ventas) |
| push distribution | "The process of building product and pushing it into the distribution channel without receiving any information regarding requirements." | Confirmada |
| pull distribution | "Supply-chain action initiated by the customer. ... In a pull environment, a customer's purchase sends replenishment information back through the supply chain from retailer to distributor to manufacturer, so goods are 'pulled' through the supply chain." | Confirmada |
| postponement | "The delay of final activities (i.e., assembly, production, packaging, etc.) until the latest possible time." | Confirmada |
| efficient / responsive supply chain | Fisher 1997, tabla de la sección 1 ("supply predictable demand efficiently at the lowest possible cost" / "respond quickly to unpredictable demand in order to minimize stockouts, forced markdowns, and obsolete inventory") | Confirmada |
| distribution center | "The warehouse facility which holds inventory from manufacturing pending distribution to the appropriate stores." | Ajustar: el CSCMP dice "retiene inventario pendiente de distribución a las tiendas"; "recibe y despacha" no está |
| consolidation | "Combining two or more shipments in order to realize lower transportation rates." (inbound: "make-bulk"; outbound: "breakbulk") | Confirmada |
| truckload carrier | "Trucking companies, which move full truckloads of freight directly from the point of origin to destination." | Confirmada (FTL) |
| LTL carrier | "Trucking companies that consolidate and transport smaller (less than truckload) shipments of freight by utilizing a network of terminals and relay points." | Confirmada |
| intermodal transportation | "Transporting freight by using two or more transportation modes such as by truck and rail or truck and oceangoing vessel." | Ajustar: "misma unidad de carga" no figura en esta entrada |
| container | "A 'box,' typically 10 to 40 feet long, which is primarily used for ocean freight shipments. For travel to and from ports, containers are loaded onto truck chassis or on railroad flatcars." | Ajustar: no dice "normalizada (ISO)" |
| freight | "Goods being transported from one place to another." | Ajustar: "o su precio" no está en esta entrada |
| carrier | "A firm which transports goods or people via land, sea or air." | Confirmada |
| third-party logistics (3PL) | "Outsourcing all or much of a company's logistics operations to a specialized company." Y: "The term '3PL' was first used in the early 1970s to identify intermodal marketing companies (IMCs) in transportation contracts." | Confirmada |
| lead time | "The total time that elapses between an order's placement and its receipt. It includes the time required for order transmittal, order processing, order preparation, and transit." | Confirmada |
| service level | "A metric, shown as a percentage, which captures the ability to satisfy demand or responsiveness. Order fill rates and machine or process up-time are examples of service level measures." | Ajustar: es una métrica en porcentaje, no solo "probabilidad" |
| perfect order | "one which meets all of the following criteria: Delivered complete, with all items on the order in the quantity requested. Delivered on time to customer's request date ... Delivered with complete and accurate documentation supporting the order, including packing slips, bills of lading, and invoices. Delivered in perfect condition..." | Confirmada. SCOR la mide como "Perfect Order Fulfillment (RL.1.1)" |
| traceability | "1) The ability to track the location of a shipment as it moves through the shipping process to the customer. 2) The ability to determine the source and disposition of individual lot numbered or serial numbered products." | Confirmada; la entrada tiene dos sentidos |
| Incoterms | "International terms of sale developed by the International Chamber of Commerce to define sellers' and buyers' responsibilities." | Ajustar: "costo y riesgo del transporte" no figura en esta entrada |
| MAPE / MASE / método ingenuo | FPP3 (primera ronda): https://otexts.com/fpp3/accuracy.html y /simple-methods.html | Confirmadas por la primera ronda |
| resiliencia / agrupamiento de riesgo | Wikipedia: https://en.wikipedia.org/wiki/Supply_chain_resilience y https://en.wikipedia.org/wiki/Risk_pooling | Sin fuente de peso; quedan como las de la primera ronda |

Los 20 términos pedidos están cubiertos con fuente (los 25 primeros de la tabla más Fisher y FPP3). Los términos sin fuente en esta ronda (quedan con la definición de la base): leagility, lean, ágil, justo a tiempo, por si acaso, redundancia, flexibilidad, nearshoring, reshoring, red de distribución, decoupling point, ASCM, CSCMP, demanda intermitente, error de pronóstico. Una razón: el glosario del CSCMP no tiene entradas para "decoupling point", "nearshoring", "reshoring" ni "risk pooling" (se buscaron en el texto extraído).

## 11. Huecos que siguen abiertos

- Oliver y Webber: el texto, el año 1982 y *Outlook*; la nota de Handfield en Wikipedia.
- SCOR DS 2022 (versión de siete procesos): ningún texto primario; los niveles 2 y 3 del estándar; el diccionario y las certificaciones de ASCM (bloqueados).
- M4 2020 en texto completo (403).
- El abstract del IJPE de Thomé et al. (2012) y el de Tuomikangas y Kaipia (2014).
- Estudios de desempeño de DDMRP; Miclo y otros; quién propuso el método (Demand Driven Institute).
- Zinn, Levy y Bowersox (1989).
- Sheffi y Rice; el informe de la OCDE; McKinsey.
- Levinson: capítulos, día 26 de abril, reseña académica.
- "Tercerizar siempre baja costos"; logística militar; MRP y DRP históricos; JOM y *Transportation Science*; MITx.
- Glosario: términos sin entrada en el CSCMP (ver sección 10). El diccionario de ASCM no se pudo leer.
- Búsqueda: el presupuesto compartido de búsquedas se agotó dos veces; lo no encontrado se declara hueco, no inexistente.

## 12. Discrepancias con el árbol

- SCOR: dos versiones circulan (seis procesos con Enable, y siete con Order, Fulfill y Orchestrate). La tabla "qué proceso de SCOR es de qué tema" de la primera ronda debe indicar la versión. Con la v13 (Plan, Source, Make, Deliver, Return, Enable): este tema es dueño de Plan (pronóstico, S&OP), Deliver y Return en lo que pasa fuera del depósito, y de Enable solo en lo transversal.
- El PCF 7.4 es más fino que SCOR para este tema: 4.1.5 (DRP) y 4.4.4 (transporte de salida) coinciden casi uno a uno con los límites del brief, y la red de distribución es 4.4.1.2 y 4.1.7.1. Sirve de mapa del árbol. Pero el PCF no nombra al S&OP, y 4.4 incluye el depósito (4.4.3), que es de otro tema.
- La nota de la posición contraria conviene que se reparta dentro de cada mecanismo, como sugirió la primera ronda. Con lo verificado, cada mecanismo lleva su matiz: látigo (industria frente a empresa), raíz cuadrada (error medio de 28 % en 26 casos), pronóstico (lo simple como piso; ML gana en M5), S&OP (evidencia parcial), DDMRP (método aún no maduro según la revisión).
- La separación entre logística y cadena de suministro tiene fuente propia (CSCMP: la logística es "that part of supply chain management"; 1998, cambio de definición del CLM). Es un buen ancla para la nota de marcos.
