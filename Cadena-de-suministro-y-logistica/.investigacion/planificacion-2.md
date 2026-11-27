# Planificación (vertical): informe de investigación, segunda ronda

Complementa a `planificacion.md` (no lo reemplaza ni lo corrige). Alcance: los huecos de las notas plan-de-ventas-y-operaciones, planificacion-de-la-distribucion, pronostico-de-demanda, error-de-pronostico, efecto-latigo y las secciones «Qué registra un sistema».

## Aviso de cobertura (leer primero)

- El presupuesto de búsqueda web de la sesión estaba agotado desde el primer intento (límite de 200 búsquedas compartido entre agentes). No se hizo ninguna búsqueda web. Todo lo de abajo viene de fetch directo: APIs de metadatos (Crossref, OpenAlex, Semantic Scholar), repositorios institucionales (Lancaster, Manchester), RePEc, PMC, Wikipedia (solo como índice de referencias), y el código y la documentación publicados en GitHub de dos sistemas abiertos.
- Límite de la herramienta de lectura: devuelve citas de hasta unos 120 caracteres. Los abstracts van, por eso, en fragmentos literales numerados; el orden es el del original.
- ScienceDirect (403), Springer (redirección de login), INFORMS, HBR (404), Wiley (403) y las URL antiguas de MIT CTL (404) no se pudieron leer. MIT OCW: el curso 15.762J existe y abre, pero no cubre S&OP ni DRP; no apareció una URL vigente de ESD.260 / 1.260.
- Quedan sin cubrir, y se declaran como hueco: ciclo de S&OP de la fuente de Wallace o de Oliver Wight (solo se leyó una descripción secundaria), estrategias de plan agregado de un libro abierto, DRP con ejemplo numérico, umbrales ADI/CV² desde la fuente, M4/M5 conclusiones (los abstracts no las traen), FVA, y Forrester 1958 (solo metadatos de la reedición).
- Convención: A = autoridad, P = profundidad, E = ejemplos, U = unicidad, de 1 a 3. Marca: [L] texto completo o sección completa, [M] metadatos o abstract, [S] resumen secundario o del buscador. «Sin verificar» = conocimiento previo, sin URL leída.

## Fuentes verificadas en esta ronda

| Id | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| G1 | Thomé, Scavarda, Fernandez y Scavarda (2012), «Sales and operations planning: A research synthesis», International Journal of Production Economics 138(1), 1-13. DOI 10.1016/j.ijpe.2011.11.027. Abstract en el índice RePEc | https://ideas.repec.org/a/eee/proeco/v138y2012i1p1-13.html | primaria (revisión sistemática; página de índice) | 3/2/1/3 | [M] abstract completo, literal |
| G2 | Metadatos del mismo artículo (Crossref y OpenAlex): autores António Márcio Tavares Thomé, Luiz Felipe Scavarda, Nicole Suclla Fernandez, Annibal José Scavarda; publicado en línea el 7-12-2011, número de 2012 | https://doi.org/10.1016/j.ijpe.2011.11.027 | primaria (registro) | 3/1/1/1 | [M] |
| G3 | Seeling, Kreuter, Scavarda, Thomé y Hellingrath (2021), «Global sales and operations planning: A multinational manufacturing company perspective», PLoS ONE 16(9): e0257572 (acceso abierto) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8454961 | primaria (estudio de caso, con revisión de la literatura) | 2/3/3/2 | [S] resumen devuelto por el lector, con citas cortas; no leído entero (faltaron los últimos 17.000 caracteres) |
| G4 | Wikipedia, «Sales and operations planning» (como índice de referencias y para los cinco pasos nombrados) | https://en.wikipedia.org/wiki/Sales_and_operations_planning | secundaria | 1/1/1/1 | [S] |
| G5 | Fildes, Goodwin, Lawrence y Nikolopoulos (2009), «Effective forecasting and judgmental adjustments: an empirical evaluation and strategies for improvement in supply-chain planning», International Journal of Forecasting 25(1), 3-23. DOI 10.1016/j.ijforecast.2008.11.010. Abstract en el repositorio de Lancaster | https://eprints.lancs.ac.uk/id/eprint/45487/ | primaria | 3/2/1/3 | [M] abstract completo, literal |
| G6 | Mismo artículo, repositorio de Manchester (segunda copia del abstract, con «© 2008 International Institute of Forecasters») | https://research.manchester.ac.uk/en/publications/b94715fa-9669-4dec-93ec-569919ee9bd8 | primaria (repositorio) | 3/1/1/1 | [M] (mismo texto que G5: cuenta como una sola fuente) |
| G7 | Makridakis, Spiliotis y Assimakopoulos (2020), «The M4 Competition: 100,000 time series and 61 forecasting methods», International Journal of Forecasting 36(1), 54-74. DOI 10.1016/j.ijforecast.2019.04.014. Abstract vía OpenAlex y RePEc | https://ideas.repec.org/a/eee/intfor/v36y2020i1p54-74.html | primaria | 3/2/1/3 | [M] |
| G8 | Makridakis, Spiliotis y Assimakopoulos (2022), «M5 accuracy competition: Results, findings, and conclusions», International Journal of Forecasting 38(4), 1346-1364. DOI 10.1016/j.ijforecast.2021.11.013. Abstract vía OpenAlex | https://doi.org/10.1016/j.ijforecast.2021.11.013 | primaria | 3/2/1/3 | [M] |
| G9 | Makridakis y Petropoulos (2020), «The M4 competition: Conclusions», International Journal of Forecasting 36(1), 224-227. DOI 10.1016/j.ijforecast.2019.05.006. Solo metadatos y palabras clave | https://doi.org/10.1016/j.ijforecast.2019.05.006 | primaria | 3/1/1/2 | [M] sin abstract |
| G10 | Syntetos, Boylan y Croston (2005), «On the categorization of demand patterns», Journal of the Operational Research Society 56(5), 495-503. DOI 10.1057/palgrave.jors.2601841. Abstract en OpenAlex y RePEc | https://ideas.repec.org/a/pal/jorsoc/v56y2005i5d10.1057_palgrave.jors.2601841.html | primaria | 3/2/1/3 | [M] abstract completo, literal |
| G11 | Syntetos y Boylan (2005), «The accuracy of intermittent demand estimates», International Journal of Forecasting 21(2), 303-314. DOI 10.1016/j.ijforecast.2004.10.001. Solo metadatos (RePEc: «No abstract is available for this item») | https://ideas.repec.org/a/eee/intfor/v21y2005i2p303-314.html | primaria | 3/1/1/3 | [M] sin abstract |
| G12 | Documentación de un sistema abierto de gestión, «Master production schedule» (rama 19.0, archivo `use_mps.rst` del repositorio de documentación) | https://github.com/odoo/documentation/blob/19.0/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst | primaria (documentación oficial de un sistema abierto) | 2/3/3/2 | [L] el archivo entero (371 líneas) |
| G13 | Definición de los tipos de datos «Sales Forecast», «Sales Forecast Item», «Master Production Schedule» y «Master Production Schedule Item» de otro sistema abierto de gestión (rama de desarrollo `develop`, archivos `.json` y `sales_forecast.py`) | https://github.com/frappe/erpnext/tree/develop/erpnext/manufacturing/doctype | primaria (código) | 2/2/1/3 | [L] de los campos; el `.py` solo por sus funciones y mensajes |
| G14 | Definición de la entidad `MrpEvent` de un tercer sistema abierto (archivo `manufacturing-entitymodel.xml`, rama `trunk`) | https://github.com/apache/ofbiz-framework/blob/trunk/applications/datamodel/entitydef/manufacturing-entitymodel.xml | primaria (código) | 2/1/1/2 | [L] de esa entidad |
| G15 | Sterman (1989), «Modeling Managerial Behavior: Misperceptions of Feedback in a Dynamic Decision Making Experiment», Management Science 35(3), 321-339. DOI 10.1287/mnsc.35.3.321. Abstract vía OpenAlex | https://doi.org/10.1287/mnsc.35.3.321 | primaria | 3/2/2/3 | [M] abstract completo, literal |
| G16 | Forrester, «Industrial Dynamics: A Major Breakthrough for Decision Makers», reedición en *The Roots of Logistics* (Springer, 2012), pp. 141-172. DOI 10.1007/978-3-642-27922-5_13. Solo el registro de Crossref | https://doi.org/10.1007/978-3-642-27922-5_13 | primaria (registro de la reedición) | 2/1/1/2 | [M] sin abstract |
| G17 | Wikipedia, «Tracking signal» (definición, fórmulas y referencias) | https://en.wikipedia.org/wiki/Tracking_signal | secundaria | 1/2/1/1 | [S] |
| G18 | Documentación del paquete de pronóstico de código abierto Nixtla `statsforecast`, «CrostonSBA» | https://nixtlaverse.nixtla.io/statsforecast/docs/models/crostonsba.html | secundaria (documentación de software) | 1/1/1/1 | [S] |
| G19 | MIT OpenCourseWare, 15.762J «Supply Chain Planning» (primavera 2011), programa | https://ocw.mit.edu/courses/15-762j-supply-chain-planning-spring-2011/pages/syllabus/ | primaria (curso abierto) | 3/1/1/1 | [L] del programa; sin contenido sobre S&OP, plan agregado ni DRP |

Nota: G1, G2 y las citas de G10 salen de índices (RePEc, OpenAlex, repositorios de universidades) que reproducen el abstract de la editorial; para cada artículo cuentan como una sola fuente.

## 1. plan-de-ventas-y-operaciones

### Afirmaciones verificadas

- Qué es y qué encontró la revisión sistemática. Abstract de Thomé et al. (2012) [G1], literal:
  - «Despite the growing body of literature on sales and operation planning (S&OP), efforts to synthesise the overall state of the art of research in this area are limited.»
  - «Within this context, this paper provides a systematic review of the literature on S&OP.»
  - «The purpose of this systematic review is twofold: (i) to integrate the highly dispersed work on S&OP in order to identify and analyse S&OP as a business process and (ii) to assemble quantitative evidence of its impact on the performance of the firm.»
  - «A literature search framework is proposed, with 271 papers reviewed and classified.»
  - «The framework embraces S&OP context information, inputs and goals, structure and processes, outcomes, and results.»
  - «The major expected outcome in most papers was a cross-functional integration of plans, although few studies report on the integration of finance plans into S&OP.»
  - «Despite the existence of common process descriptors and definitions of S&OP, there is a lack of unifying frameworks for maturity models, measurement of S&OP, and constructs related to the firm's performance.»
  - «The need for additional scientifically sound survey or case study research on S&OP is emphasised.»
  - Palabras clave: Supply chain management, Cross-functional alignment, Metrics, Collaboration, Integrated planning, Systematic review.
  - Corrige la ficha de la primera ronda: la revista, el volumen, las páginas y los cuatro autores son los que figuraban; el artículo se publicó en línea el 7-12-2011. [G2]
- Los cinco pasos del ciclo mensual, con nombre: «data gathering, demand planning, supply planning, pre-meeting, and executive meeting». La literatura de G3 los atribuye a Wallace y a Stahl. [G3, G4]. Cobertura de esta fuente: G3 es un estudio de caso de una multinacional, no el texto de Wallace; no se pudo leer a Wallace ni a Oliver Wight (el sitio de Wallace, `tfwallace.com`, devuelve 404). Los pasos de Oliver Wight no se verificaron.
- Cómo corre un ciclo concreto, según el estudio de caso G3 (muy específico de esa empresa; no es norma):
  - «usually once a month», nivel táctico. [G3]
  - La recolección de datos no cuenta como paso formal allí porque la carga del ERP es automática y diaria.
  - Demanda: primera semana del mes; ventas y marketing producen el plan de demanda a nivel agregado y por SKU; el resultado es un plan de demanda sin restricciones (unconstrained).
  - Abastecimiento: segunda semana, con el director de la cadena de suministro; se simula la capacidad; el resultado es un plan de abastecimiento con restricciones por SKU, con opciones de mitigación de las brechas.
  - Reunión previa: tercera semana, no siempre formal; participan los de los pasos anteriores y finanzas; sale una propuesta de S&OP con los dilemas sin resolver y un análisis financiero.
  - Reunión ejecutiva: última semana del mes, con el gerente general y los directores; es el punto de decisión del plan; la aprobación de mitigaciones que exceden la autoridad de los gerentes funcionales puede quedar en finanzas; el plan aprobado se comparte con la casa matriz.
- Quién participa: en la reunión previa, «representatives from different functional business areas (e.g., sales, marketing, and operations)»; en el paso cinco, «Company's senior managers and executives take part». Quién decide: la reunión ejecutiva. [G3]
- Horizonte: en el caso, el plan de demanda y el ejecutivo cubren «18-month horizon», por SKU con revisión por línea de producto y canal. [G3] La revisión de G3 afirma que «the S&OP planning horizon is extended and tends to merge with the multi-year strategic plan»; no da un rango de 12 a 24 meses. Una descripción secundaria dice que el proceso «covers up to 18 months at the product family level (or SKU)» y que se hace «typically ... monthly (or driven by events...)». [G4] Resultado: el horizonte de 18 a 24 meses de la primera ronda queda sin fuente primaria; la única cifra con fuente es 18 meses.
- Cuatro parámetros de diseño de Thomé et al., citados en G3: «meeting and collaboration, organisation, information technology (IT) and metrics».
- Relación con el presupuesto: en G3 el plan de S&OP «is compared to the budget with a risk analysis» antes de aprobarse, y ventas y abastecimiento buscan cumplir el presupuesto comprometido; no se define la diferencia entre ambos. Sobre el plan maestro de producción: G3 no lo trata; su plan «production master plan» alimenta el MRP. [G3]
- Uso por los sistemas: en un sistema abierto el plan maestro es una grilla por producto y período («MPS ... plan long-term replenishment for products against a manually-adjustable demand forecast»), un nivel más bajo que el plan por familia de S&OP; ver «Qué registra un sistema». [G12]

### Sin verificar (conocimiento previo, a confirmar)

- Los pasos de Oliver Wight y el texto de Wallace (Tom Wallace, *Sales & Operations Planning: The How-To Handbook*; «S&OP 101»). Las referencias de G4 apuntan a una serie de Lapide en el Journal of Business Forecasting, «Sales and Operations Planning Part I: The Process», alojada en `ctl.mit.edu`; el enlace dio 404 y no se leyó.
- Las estrategias de plan agregado (perseguir, nivelar, mixta): una fuente secundaria (Wikipedia, «Operations management») dice que el plan agregado de producción «comes in two fundamentally opposing varieties: plans which try to chase demand and level plans which try [to keep uniform capacity utilization]» [S]. La tercera variante (mixta o híbrida) no se encontró en ninguna fuente leída. Sigue pendiente un libro de texto o apuntes (Chopra y Meindl, Simchi-Levi et al.).
- Madurez de S&OP (Grimson y Pyke 2007): sin leer. Lo único verificado es que G1 dice que faltan marcos unificadores para los modelos de madurez.

### Qué registra un sistema

- La fuente más cercana a un plan de ventas y operaciones en un sistema son los dos pares de objetos de G13 (cabecera con partidas): un «pronóstico de ventas» y un «plan maestro de producción», ligado al anterior, sin una entidad de «reunión» ni de «decisión».
- Por lo que se verificó, el ciclo de S&OP en sí (versiones de plan, supuestos, brechas, decisiones de la reunión) no tiene un objeto en estos sistemas: el sistema registra el pronóstico y el plan, no el proceso de acuerdo. Es inferencia. Lo que sí muestra G3 son salidas con nombre propio por paso (plan de demanda sin restricciones, plan de abastecimiento con restricciones, propuesta con dilemas, plan aprobado), que son las versiones que haría falta guardar.

### Recurso canónico propuesto

Thomé et al. (2012) para la evidencia (leer el abstract completo y la tabla de marco de revisión, en la editorial) y G3 como ejemplo abierto y legible de un ciclo real (secciones «S&OP building blocks» y «Local and global steps»). Para la descripción práctica del proceso sigue faltando Wallace o Lapide, a leer antes de escribir.

## 2. planificacion-de-la-distribucion (DRP)

### Afirmaciones verificadas

- Una descripción secundaria define el DRP como «a method used in business administration for planning orders within a supply chain»; permite fijar parámetros de control de inventario como el stock de seguridad y calcular necesidades de inventario por período; consolida la demanda de varios centros de distribución con las fuentes de abastecimiento. Entradas listadas: demanda de un período futuro, recepciones programadas, inventario disponible al inicio, stock de seguridad. Variables: cantidad requerida, cantidad disponible restringida, cantidad de pedido recomendada, demanda pendiente (backorder) y existencias al cierre. [S: https://en.wikipedia.org/wiki/Distribution_resource_planning] La página no menciona a Martin, no trae la tabla ni un ejemplo, y su única referencia es Feigin, Katircioglu y Yao, «Distribution Resource Planning systems: a critique and enhancement» (sin URL).
- El MPS de un sistema abierto usa la relación `Forecasted Stock = Starting Stock - Forecasted Demand - Indirect Demand Forecast + Replenishment`, con la reposición sugerida `Replenishment = Safety Stock Target - Starting Stock + Forecasted Demand + Indirect Demand Forecast` (mínimo cero, o el mínimo a reponer si se configuró uno). [G12, [L]] Es la misma lógica de saldo proyectado por período que el DRP, y sirve para un ejemplo, pero no es un DRP: el sistema lo documenta para productos con plazo largo o demanda estacional y dice que el MPS no crea órdenes solo, sugiere cantidades.
- «Demanda indirecta»: una fila aparte para «the forecasted demand for the component from existing MOs»; aparece solo si el producto es componente de otro. [G12] Es el mecanismo análogo a que los pedidos planificados de un nivel inferior se vuelvan necesidades brutas del superior.
- APQC 4.1.5 (de la primera ronda) sigue siendo la única lista de pasos verificada del DRP.

### Sin verificar: componente casi sin fuente leída (hueco principal de esta ronda)

- André J. Martin, *Distribution Resource Planning* (1983): no se encontró un registro ni un texto legible; no se leyó. La tabla por período (necesidades brutas, recepciones programadas, stock proyectado, necesidades netas, pedidos planificados) y el paso de «los pedidos planificados de cada depósito pasan a ser necesidades brutas del central» siguen siendo conocimiento previo. No apareció un capítulo abierto ni apuntes universitarios con ejemplo numérico: no hay un ejemplo con fuente.

### Qué registra un sistema

- Un MPS por producto, almacén y período (columnas por período; «Default Time Range» anual, mensual, semanal o diario, y «Number of Periods»), con filas de existencia inicial, demanda pronosticada, demanda indirecta, reposición y existencia pronosticada; parámetros por producto: objetivo de stock de seguridad, mínimo a reponer y disparador de reposición (manual, automático o nunca); estados de la reposición por color según si la orden generada coincide con lo sugerido (verde: lista; gris: orden igual a lo sugerido; amarillo: menor; rojo: mayor). [G12, [L]]
- El plan maestro de otro sistema abierto: `Master Production Schedule` con almacén padre, fechas desde y hasta, vínculo al pronóstico de ventas y a las órdenes de venta y solicitudes de material; partidas con artículo, almacén, fecha de entrega, `planned_qty`, `order_release_date` (fecha de lanzamiento), lista de materiales y `cumulative_lead_time`. [G13, [L] de los campos] Es una fecha de lanzamiento desfasada por el plazo, que es lo que haría un DRP.
- El MRP de un tercer sistema abierto registra eventos por producto: `MrpEvent` con `mrpId`, `productId`, `eventDate`, `mrpEventTypeId`, `facilityId`, `quantity`, `eventName`, `isLate` (indicador) y `facilityIdTo` (instalación de destino, útil para transferencias entre depósitos). [G14, [L]] No se confirmó el catálogo de tipos de evento.
- Ninguno de los tres es un DRP multinivel de depósitos con árbol de abastecimiento; lo que muestran es el patrón común (saldo proyectado por período, fecha de lanzamiento con plazo, sugerencia no automática).

### Recurso canónico propuesto

Sin recurso verificado. Candidatos: Martin (1983) o el capítulo de DRP de un manual de operaciones (Chopra y Meindl, Silver, Pyke y Thomas); a leer. Mientras tanto, G12 sirve como ejemplo de la lógica del saldo proyectado y de la reposición sugerida.

## 3. pronostico-de-demanda

### Afirmaciones verificadas

- Competencia M4. Abstract literal [G7]:
  - «The M4 Competition follows on from the three previous M competitions, the purpose of which was to learn from empirical evidence both how to improve the forecasting accuracy and how such learning could be used to advance the theory and practice of forecasting.»
  - «The aim of M4 was to replicate and extend the three previous competitions by: (a) significantly increasing the number of series, (b) expanding the number of forecasting methods, and (c) including prediction intervals in the evaluation process as well as point forecasts.»
  - «This paper covers all aspects of M4 in detail, including its organization and running, the presentation of its results, the top-performing methods overall and by categories, its major findings and their implications, and the computational requirements of the various methods.»
  - «Finally, it summarizes its main conclusions and states the expectation that its series will become a testing ground for the evaluation of new methods and the improvement of the practice of forecasting, while also suggesting some ways forward for the field.»
  - El abstract no enuncia los resultados (quién ganó, cuánto ayudó el aprendizaje automático). La cifra «100.000 series y 61 métodos» está en el título. Las conclusiones están en el cuerpo del artículo y en G9, que no se leyeron (G9 trae solo palabras clave: «naive forecast, single exponential smoothing, ARIMA model, theta method, mean absolute percentage error, Box-Jenkins methodology»). La versión editorial de G7 es de acceso abierto (CC BY-NC-ND) en https://www.sciencedirect.com/science/article/pii/S0169207019301128/pdf, pero el servidor devolvió 403.
- Competencia M5 («Accuracy»). Abstract literal [G8]:
  - «In this study, we present the results of the M5 "Accuracy" competition, which was the first of two parallel challenges in the latest M competition with the aim of advancing the theory and practice of forecasting.»
  - «The main objective in the M5 "Accuracy" competition was to accurately predict 42,840 time series representing the hierarchical unit sales for the largest retail company in the world by revenue, Walmart.»
  - «The competition required the submission of 30,490 point forecasts for the lowest cross-sectional aggregation level of the data, which could then be summed up accordingly to estimate the forecasts for the remaining upward levels.»
  - «We provide details of the implementation of the M5 "Accuracy" challenge, as well as the results and best performing methods and summarize the major findings and conclusions.»
  - «Finally, we discuss the implications of these findings and suggest directions for future research.»
  - Tampoco enuncia los resultados. Existe una competencia gemela de incertidumbre, «The M5 uncertainty competition: Results, findings and conclusions», IJF 38(4), 1365-1385, DOI 10.1016/j.ijforecast.2021.10.009 (solo metadatos de Crossref).
  - Corrige la ficha de la primera ronda: M4 y M5 tienen los autores Makridakis, Spiliotis y Assimakopoulos; M4 en IJF 36(1), 54-74; M5 en IJF 38(4), 1346-1364.
- Ajuste por juicio. Abstract literal de Fildes, Goodwin, Lawrence y Nikolopoulos (2009) [G5, G6]:
  - «Demand forecasting is a crucial aspect of the planning process in supply-chain companies.»
  - «The most common approach to forecasting demand in these companies involves the use of a computerized forecasting system to produce initial forecasts and the subsequent judgmental adjustment of these forecasts by the company's demand planners, ostensibly to take into account exceptional circumstances expected over the planning horizon.»
  - «Making these adjustments can involve considerable management effort and time, but do they improve accuracy, and are some types of adjustment more effective than others?»
  - «To investigate this, we collected data on more than 60,000 forecasts and outcomes from four supply-chain companies.»
  - «In three of the companies, on average, judgmental adjustments increased accuracy.»
  - «However, a detailed analysis revealed that, while the relatively larger adjustments tended to lead to greater average improvements in accuracy, the smaller adjustments often damaged accuracy.»
  - «In addition, positive adjustments, which involved adjusting the forecast upwards, were much less likely to improve accuracy than negative adjustments.»
  - «They were also made in the wrong direction more frequently, suggesting a general bias towards optimism.»
  - «Models were then developed to eradicate such biases.»
  - «Based on both this statistical analysis and organisational observation, the paper goes on to analyse strategies designed to enhance the effectiveness of judgmental adjustments directly.»
  - Esto confirma lo que la primera ronda dejó sin verificar: los ajustes chicos «often damaged accuracy» y los positivos «were much less likely to improve accuracy». Ojo con la lectura: en tres de las cuatro empresas el ajuste, en promedio, mejoró la exactitud; no es «los ajustes empeoran».
- Demanda intermitente: la clasificación. Abstract literal de Syntetos, Boylan y Croston (2005) [G10]:
  - «The categorization of alternative demand patterns facilitates the selection of a forecasting method and it is an essential element of many inventory control software packages.»
  - «The common practice in the inventory control software industry is to arbitrarily categorize those demand patterns and then proceed to select an estimation procedure and optimize the forecast parameters.»
  - «Alternatively, forecasting methods can be directly compared, based on some theoretically quantified error measure, for the purpose of establishing regions of superior performance and then define the demand patterns based on the results.»
  - «It is this approach that is discussed in this paper and its application is demonstrated by considering EWMA, Croston's method and an alternative to Croston's estimator developed by the first two authors of this paper.»
  - «Comparison results are based on a theoretical analysis of the mean square error due to its mathematically tractable nature.»
  - «The categorization rules proposed are expressed in terms of the average inter-demand interval and the squared coefficient of variation of demand sizes.»
  - «The validity of the results is tested on 3000 real-intermittent demand data series coming from the automotive industry.»
  - El abstract no trae los umbrales. Hecho verificado: la clasificación usa dos variables, el intervalo medio entre demandas (ADI) y el cuadrado del coeficiente de variación del tamaño de la demanda (CV²), y se validó con 3.000 series del sector automotor. Los valores 1,32 y 0,49 quedan sin verificar. La documentación del paquete de R `tsintermittent` remite, para los esquemas de clasificación (incluido «SBC - Syntetos Boylan Croston»), a Petropoulos y Kourentzes (2015), Journal of the Operational Research Society, DOI 10.1057/jors.2014.62 [S: https://search.r-project.org/CRAN/refmans/tsintermittent/html/idclass.html]; esa página no se pudo leer (redirección de login de Springer).
- Corrección del método de Croston (SBA): el artículo de referencia es Syntetos y Boylan (2005), «The accuracy of intermittent demand estimates», IJF 21(2), 303-314 [G11, solo metadatos]; en las palabras clave de su registro: «intermittent demand forecasting, Croston's method, simple exponential smoothing, simple moving average». La fórmula se verifica solo de forma secundaria: la documentación de `statsforecast` la define multiplicando el cociente de Croston por (1 − α/2), con α la constante de suavizado [G18, [S]]; esa página no cita la fuente de la corrección. El sesgo del método original sí está en FPP3 (primera ronda, F7) con cita de Syntetos y Boylan (2001), «On the bias of intermittent demand estimates»; ese artículo de 2001 no se verificó por separado.
- Valor agregado del pronóstico (FVA): hay dos registros bibliográficos, sin texto leído. «Forecast Value Added Analysis», capítulo 4 de Gilliland, *The Business Forecasting Deal* (Wiley), DOI 10.1002/9781119199885.ch4, páginas 81-109; y «Forecast Value Added», capítulo 27 de Vandeput, *Data Science for Supply Chain Forecasting* (De Gruyter, 2021), DOI 10.1515/9783110671124-027, páginas 254-262 [M: registros de Crossref]. No se verificó la definición. La definición sigue siendo conocimiento previo: comparar la exactitud de cada paso del proceso contra un pronóstico ingenuo.

### Sin verificar (conocimiento previo, a confirmar)

- Qué ganó en M4 y M5 y por cuánto: lo de la primera ronda se mantiene sin verificar (híbrido de suavizado exponencial y redes en M4; modelos basados en árboles de gradiente en M5). Hay que leer el cuerpo de G7, G8 y G9 (la versión de acceso abierto de G7 y la de G8 en ScienceDirect devolvieron 403).
- Umbrales 1,32 y 0,49, la fórmula exacta de SBA y el origen de la sigla SBC.
- Definición y fuente de FVA (ver arriba).

### Qué registra un sistema

- Un sistema abierto (G13) guarda el pronóstico como documento con cabecera y partidas: empresa, almacén padre, fecha de publicación, fecha de inicio, frecuencia («Weekly» o «Monthly»), número de períodos, estado («Planned», «MPS Generated», «Cancelled») y por partida artículo, unidad, fecha de entrega, almacén y `demand_qty` (cantidad obligatoria; el código lanza error si falta). De esa cabecera se genera el plan maestro. El estado «MPS Generated» muestra que el pronóstico se «consume» al generar el plan.
- El mismo sistema trae un informe de «exponential smoothing forecasting» (G13): el método está en el sistema como informe, no como parámetro del pronóstico guardado.
- Otro sistema abierto (G12) permite sugerir la demanda pronosticada a partir de la historia con estas bases: «Actual Demand», «Previous Year», «Last 30 Days», «Last 3 Months», «Last 12 Months», con un factor de escala en porcentaje (por ejemplo 110 % para un crecimiento de 10 %); la demanda pronosticada se puede editar a mano por período y se puede ver junto a la «Actual Demand» (demanda confirmada por órdenes de venta). Es una forma de registrar el ajuste manual sobre un pronóstico estadístico simple.
- Lo que no mostró ninguno: versión del pronóstico con autor y fecha del ajuste (relevante para Fildes et al.: para medir si el ajuste ayudó hay que guardar el pronóstico antes y después), jerarquía de agregación, y el indicador de quiebre o de promoción. Es inferencia a partir de la ausencia; no se auditó la base completa.

### Recurso canónico propuesto

Para el ajuste: Fildes et al. (2009), abstract (leer el abstract completo; para las cifras por empresa hace falta el artículo). Para M4 y M5: leer las secciones de resultados y conclusiones, no el abstract. Para la intermitente: Syntetos, Boylan y Croston (2005) para la clasificación y, para los umbrales, Petropoulos y Kourentzes (2015) o el propio artículo.

## 4. error-de-pronostico

### Afirmaciones verificadas

- Señal de seguimiento (tracking signal). Definición literal: «monitors any forecasts that have been made in comparison with actuals, and warns when there are unexpected departures of the outcomes from the forecasts»; es un indicador simple del sesgo del pronóstico y se usa sobre todo cuando la validez del modelo está en duda. [G17, S]
  - Fórmula 1: señal = Σ(a_t − f_t) / MAD, con MAD = Σ|a_t − f_t| / n (a_t real, f_t pronóstico, n períodos).
  - Fórmula 2, de Trigg (1964), suavizada: E_t = β·e_t + (1 − β)·E_(t−1); M_t = β·|e_t| + (1 − β)·M_(t−1); T_t = |E_t / M_t|.
  - Umbral: la página no da un límite general; solo un ejemplo con β = 0,1 («a value of Tt greater than .51 indicates nonrandom errors»). Por lo tanto el ±4 a ±6 de la primera ronda sigue sin verificar. Referencias de esa página: Trigg (1964), «Monitoring a forecasting system», Operational Research Quarterly 15, 271-274; Trigg y Leach (1967), «Exponential smoothing with an adaptive response rate», Operational Research Quarterly 18(1), 53-59; Alstrom y Madsen (1996), «Tracking signals in inventory control systems: A simulation study», International Journal of Production Economics 45(1-3), 293-302, https://doi.org/10.1016/0925-5273(95)00120-4; Nahmias, *Production & Operations Analysis*, 5.ª ed. (2005); APICS Dictionary, 12.ª ed.
- Relación con el ajuste por juicio: G5 mide el efecto de ajustar sobre el error (ver sección 3); la señal de seguimiento sirve para detectar el sesgo que ese estudio encontró (optimismo).

### Sin verificar

- Umbral habitual de la señal (±4, ±6 o ±3,75 según el libro): sin fuente. A buscar en Nahmias o en el diccionario de ASCM/APICS.
- WAPE y FVA: siguen sin fuente primaria.

### Qué registra un sistema

- Para calcular la señal de seguimiento hace falta guardar, por artículo y período, el pronóstico y el real con signo (no solo el valor absoluto), y el acumulado o el valor suavizado de los dos (E y M en la fórmula de Trigg). Inferido de G17.

### Recurso canónico propuesto

Para la señal, un libro de texto: Nahmias (cap. de pronóstico) o el diccionario de ASCM; no se leyó ninguno. Mientras tanto, G17 sirve para la fórmula, no para el umbral.

## 5. efecto-latigo

### Afirmaciones verificadas

- Sterman (1989), metadatos y abstract. Management Science 35(3), 321-339, «Modeling Managerial Behavior: Misperceptions of Feedback in a Dynamic Decision Making Experiment», autor John D. Sterman (MIT Sloan). [G15]. Abstract literal:
  - «Studies in the psychology of individual choice have identified numerous cognitive and other bounds on human rationality, often producing systematic errors and biases.»
  - «This paper reports an experiment on the generation of macrodynamics from microstructure in a common managerial context.»
  - «Subjects manage a simulated inventory distribution system which contains multiple actors, feedbacks, nonlinearities, and time delays.»
  - «The interaction of individual decisions with the structure of the simulated firm produces aggregate dynamics which systematically diverge from optimal behavior.»
  - «An anchoring and adjustment heuristic for stock management is proposed as a model of the subjects' decision processes.»
  - «Econometric tests show the rule explains the subjects' behavior well.»
  - «The estimation results identify several 'misperceptions of feedback' which account for the poor performance of subjects.»
  - «In particular, subjects are shown to be insensitive to the feedbacks from their decisions to the environment.»
  - Nota: el abstract no dice «juego de la cerveza» ni «efecto látigo»; el experimento es el juego de distribución de inventario. La conexión con la cerveza la hace una fuente secundaria: Wikipedia dice que la secuencia del látigo «is well simulated by the beer distribution game that was developed by MIT Sloan School of Management in the 1960s» y cita a Sterman por la subestimación del inventario en camino [S: https://en.wikipedia.org/wiki/Bullwhip_effect]. La afirmación de la primera ronda («el decisor subestima el inventario en camino») no está en el abstract: sigue sin leerse en el cuerpo.
- Forrester. La fuente verificada es una reedición: Forrester, «Industrial Dynamics: A Major Breakthrough for Decision Makers», en *The Roots of Logistics* (Springer, 2012), pp. 141-172, DOI 10.1007/978-3-642-27922-5_13 [G16]. No se verificó que el original sea HBR 1958 (la página de HBR devolvió 404, y la de la reedición no abrió). Wikipedia, que no cita 1958, atribuye el origen de la idea a *Industrial Dynamics* (1961) de Forrester y la llama «Forrester effect». Resultado: el año 1958 y la revista siguen sin verificar en esta ronda; hay que confirmarlos en la reedición o en HBR.

### Sin verificar

- Metadatos exactos del original de Forrester en HBR (volumen, número, páginas) y su abstract.
- Qué dice el cuerpo de Sterman sobre el «stock en camino» (supply line).

### Qué registra un sistema

Sin novedades respecto de la primera ronda. Lo que da Sterman es el criterio de diseño: el efecto aparece por cómo se decide con demoras, así que un sistema que quiera moderarlo debe mostrar al decisor lo que ya está pedido y en camino, no solo el stock. Inferencia.

### Recurso canónico propuesto

Sterman (1989), abstract y la sección del modelo de decisión (la regla de anclaje y ajuste); para el origen, la reedición de Forrester si se logra leer.

## Huecos

1. Ciclo de S&OP de la fuente de Wallace (*How-To Handbook*, «S&OP 101») o de Oliver Wight: no leído; la única fuente de los pasos es secundaria o un caso. Los enlaces de Lapide y de Wallace listados por Wikipedia dieron 404.
2. Horizonte de 18 a 24 meses: solo hay 18 meses con fuente (un caso). Sin fuente para «24».
3. Estrategias de plan agregado (perseguir, nivelar, mixta): solo hay una frase secundaria sobre las dos primeras. La mixta no tiene fuente.
4. Diferencia S&OP y presupuesto y S&OP y plan maestro: sin definición en ninguna fuente leída; lo que hay es que el plan se contrasta con el presupuesto (G3) y que el plan maestro es la grilla por producto (G12, G13).
5. DRP: Martin (1983), la tabla y el ejemplo numérico: sin fuente. No se encontró un capítulo abierto ni apuntes.
6. M4 y M5: solo los abstracts, que no enuncian los resultados. Faltan las conclusiones del cuerpo (G7, G8 y G9).
7. Umbrales 1,32 y 0,49 y fórmula de SBA desde la fuente: sin verificar (solo la secundaria G18 para el factor).
8. Umbral de la señal de seguimiento: sin fuente.
9. FVA: solo registros bibliográficos.
10. Forrester 1958: solo la reedición de 2012.
11. Odoo, ERPNext y OFBiz: se leyeron la documentación de uno, los campos de otro y una entidad del tercero; no hay documentación de pronóstico de OFBiz (no se encontró una página) y no se leyó el código de la generación del pronóstico de ERPNext más que por nombres de funciones.
12. MIT OCW ESD.260 / 1.260: la URL del curso 1-260-logistics-and-supply-chain-management-fall-2006 y la de ids-730 dan 404; 15.762J abre pero no cubre estos temas.
13. Recencia: lo de los sistemas abiertos es de la rama de desarrollo de ERPNext y de la rama 19.0 de la documentación de Odoo, a la fecha de esta sesión; los campos pueden cambiar. Los artículos son estables.

## Discrepancias con el árbol

- Plan maestro y pronóstico: los sistemas abiertos guardan el pronóstico y el plan maestro de producción como objetos separados y encadenados (el segundo se genera del primero), y el plan maestro es de Producción. Para S&OP y DRP conviene decir en las notas que el sistema solo registra el pronóstico y el plan por producto y período; el acuerdo entre áreas (la reunión) no tiene objeto propio.
- El MPS de un sistema abierto es la grilla por producto, mientras S&OP (según G3 y G4) trabaja por familia o SKU con horizonte de unos 18 meses: la nota de S&OP debe enlazar a Producción para el plan maestro y no explicarlo.
- La definición de DRP con la que contamos (G17 aparte) es secundaria y sin tabla; no coincide con la lista de campos del MPS de los sistemas. Es probable que la nota de DRP deba apoyarse en un manual de operaciones y declarar que los sistemas abiertos leídos no lo implementan como tal.
- El efecto de Sterman es de comportamiento y el de Lee et al. es estructural: la nota de efecto-latigo puede conservar las dos explicaciones (ya recomendado en la primera ronda); el abstract de Sterman no usa la palabra «látigo».
- Sin cambios al árbol de seis notas.
