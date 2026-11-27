# Informe: Analítica de producto (métricas, embudo) y Visualización y BI

Fecha de la investigación: 2026-11-27. Marcas: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U). Muchos PDF no se pudieron leer (binarios): se declara en cada caso.

## Observación sobre el árbol

Analítica-de-producto y Visualización-y-BI coinciden con cómo el campo las divide. Dos notas: (1) la "capa semántica" cae entre Visualización-y-BI y Modelado-y-almacenamiento/Gobierno (dbt la define en la capa de modelado, no en la de BI); conviene una nota en BI que enlace a las otras. (2) "Definición de métrica" se toca con Gobierno-y-calidad (catálogo, glosario de negocio). Puntos de contacto con otros temas: árbol de métricas con North Star (Producto); conversión de embudo con activación y con experimento A/B (Producto); ley de Goodhart con incrementalidad (Marketing); el tipo de métrica "conversion" de dbt con embudos.

---

## 1. Definición de métrica, KPI, árbol de métricas, vanidad, Goodhart

### Fuentes
| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| dbt Docs, "Metrics: types and definition components" https://docs.getdbt.com/docs/build/metrics-overview | primaria (proveedor, doc oficial) | 3/3/3/2 | [S] (leída vía WebFetch con resumen del modelo) |
| Ries, "Why Vanity Metrics Are Dangerous" (reimpresión) https://nextbigideaclub.com/magazine/ericries-vanity-metrics-dangerous/4781/istock_000028679138_large-2/ | primaria (reimpresión) | 3/2/2/3 | [S] |
| Strathern 1997, European Review 5(3) 305-321 https://ideas.repec.org/a/cup/eurrev/v5y1997i03p305-321_00.html (PDF https://www.Gwern.net/doc/statistics/decision/1997-strathern.pdf) | primaria | 3/3/1/3 | [M] (el PDF vino binario, no se leyó) |
| Wikipedia, Goodhart's law https://en.wikipedia.org/wiki/Goodhart%27s_law | secundaria (compila citas con fuente) | 1/2/2/1 | [S] |

### Afirmaciones
- Qué fija la definición en una herramienta real: nombre, tipo (simple, ratio, cumulative, derived, conversion), agregación (`agg`: sum, count_distinct, etc.) y expresión, filtro ("Consider it as your WHERE clause"), numerador y denominador en las de ratio, ventana (`window`) en las acumuladas y de conversión. El grano de tiempo NO va en la métrica: lo declara la columna de tiempo y se elige al consultar, solo en grano igual o más grueso. https://docs.getdbt.com/docs/build/metrics-overview
- Para "que dos personas calculen igual" entonces: numerador, denominador, grano (de la fila y de la fecha), ventana, filtros y unidad contada (usuarios únicos vs eventos). Esta lista es síntesis mía a partir de los parámetros de dbt y de las opciones de embudo (sección 2); ninguna fuente la enuncia así. Hueco: no hallé un texto canónico independiente de proveedor que la enuncie.
- KPI vs métrica: no busqué fuente primaria; la distinción habitual (KPI = métrica atada a un objetivo) queda como hueco sin fuente.
- Árbol de métricas / driver tree: no se halló fuente primaria en las rondas hechas (hueco).
- Ries, vanity metrics: sus rasgos según el texto: "count a technical process, not a number of human beings", son totales agregados, y no tienen "no built-in measure of causality". Las métricas accionables son "more work". El artículo NO trae las "tres A" (accionable, accesible, auditable); un repost secundario las atribuye a Ries, sin confirmar. https://nextbigideaclub.com/magazine/ericries-vanity-metrics-dangerous/4781/istock_000028679138_large-2/
- Goodhart 1975, literal: "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." Fuente: Goodhart, "Problems of Monetary Management: The UK Experience", en Courakis (ed.), Inflation, Depression, and Economic Policy in the West, Barnes and Noble, 1975, p. 116 (cita y página según Wikipedia, no verificadas en el original). https://en.wikipedia.org/wiki/Goodhart%27s_law
- Strathern 1997, literal: "When a measure becomes a target, it ceases to be a good measure." European Review 5(3), pp. 305-321. La referencia bibliográfica está confirmada en https://ideas.repec.org/a/cup/eurrev/v5y1997i03p305-321_00.html; la frase literal en el texto del artículo viene de Wikipedia y de un buscador, no la pude leer en el PDF.
- Hoskin 1996 (puente entre ambos): "That every measure which becomes a target becomes a bad measure", en Accountability: Power, Ethos and the Technologies of Managing, pp. 265-282 (según Wikipedia). Importante: la frase popular NO es de Goodhart; es de Strathern, que la formula a partir de Hoskin.

### Recurso canónico
- Definición de métrica: la página de métricas de dbt (todos los tipos y parámetros), como lista de qué hay que decidir. Ojo: es de proveedor.
- Goodhart: citar las dos formulaciones con su autor y año; leer del artículo de Strathern la sección donde la enuncia (pendiente de leer en el original).

---

## 2. Embudo (funnel)

### Fuentes
| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Amplitude, Funnel analysis (build) https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-build | primaria (doc oficial) | 3/3/2/2 | [S] |
| Amplitude, Funnel analysis (interpret) https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-interpret | primaria | 3/3/2/2 | [S] |
| PostHog, Funnels https://posthog.com/docs/product-analytics/funnels | primaria | 3/3/2/2 | [S] |
| GA4, Funnel exploration https://support.google.com/analytics/answer/9327974 | primaria | 3/2/2/2 | [S] |
| Mixpanel, Funnels overview https://docs.mixpanel.com/docs/reports/funnels/funnels-overview | primaria | 3/1/1/1 | [S] (solo dice que calcula conversiones "within a particular time window") |

Todas fechadas en la consulta del 2026-11-27; la página no muestra fecha de edición en lo leído.

### Afirmaciones
- Amplitude: "a converted user is one who triggers the events you specified, in the specified order". Tres modos: This order (puede haber otros eventos en el medio), Any order, Exact order (ningún otro evento). Se puede excluir a quien dispare un evento de exclusión entre pasos. El segmento de usuario aplica solo al evento inicial. https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-build
- Amplitude, ventana de conversión: "the longest a converting user can take between entering a funnel and completing it"; por defecto un día (UTC), mínimo un segundo, máximo 90 días (366 en algunas organizaciones). Conversión total: "(Users who triggered every event in the funnel) divided by (Users who triggered the funnel's first event)". Cuenta usuarios únicos por defecto, o totales de eventos. En la conversión en el tiempo, el usuario cae en el período en que entró al embudo aunque convierta después. https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-interpret
- PostHog: orden Sequential (otros eventos en el medio permitidos), Strict (nada en el medio) o Any order. Ventana: "how long a user has to complete the funnel after their first step" (sin default en la página). Conversión global (cada paso vs el primero) vs relativa (cada paso vs el anterior). Si un evento ocurre fuera del rango de fechas o no pasa el filtro, el usuario sale. https://posthog.com/docs/product-analytics/funnels
- GA4: embudo abierto (se puede entrar en cualquier paso) vs cerrado (solo entra quien empieza en el primero); "indirectly followed by" (puede haber acciones en el medio) vs "directly followed by". https://support.google.com/analytics/answer/9327974
- Entonces "embudo estricto vs no" son dos ejes distintos en las herramientas: orden estricto (nada en el medio) y entrada abierta/cerrada. Y las herramientas no coinciden en nombres ni defaults: hay que fijar la ventana y el orden al reportar.
- dbt tiene un tipo de métrica "conversion" (evento base seguido de evento de conversión de una entidad dentro de una ventana). https://docs.getdbt.com/docs/build/metrics-overview

### Analítica web y de e-commerce (una línea para enlazar)
- GA4, eventos recomendados de e-commerce, en orden del recorrido: view_item_list, select_item, view_item, add_to_cart, add_to_wishlist, view_cart, remove_from_cart, begin_checkout, add_shipping_info, add_payment_info, purchase, refund; más view_promotion y select_promotion. https://developers.google.com/analytics/devguides/collection/ga4/ecommerce [S] (fecha de última actualización no visible: hueco). Es el embudo de tienda ya armado.
- Analítica web en general: no se investigó fuente propia (hueco menor; alcanza con la línea de GA4).

### Recurso canónico
Amplitude "interpret" (fórmula, ventana, unidad contada) más PostHog (los tres modos de orden y conversión relativa vs global). Fijarse en: ventana, orden, unidad contada, fecha de entrada.

---

## 3. Elegir un gráfico y errores típicos

### Fuentes
| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Cleveland y McGill 1984, "Graphical Perception", JASA 79 (JSTOR https://www.jstor.org/stable/2288400) | primaria | 3/3/2/3 | [S] (JSTOR no cargó; solo resúmenes del buscador) |
| Heer y Bostock, replicación en Mechanical Turk (CHI 2010) https://idl.cs.washington.edu/files/2010-CrowdsourcingGraphicalPerception-CHI.pdf | primaria | 3/2/1/2 | [S] (URL dio 404 al leerla; solo lo que dijo el buscador) |
| FT Visual Vocabulary https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary | primaria (guía de elección) | 3/2/3/3 | [S] |
| Datawrapper, barras desde cero https://www.datawrapper.de/academy/why-our-column-and-bar-charts-start-at-zero | secundaria (practicante) | 2/2/2/1 | [S] (solo título en resultados) |
| Tableau Research (Correll et al.) vía https://ar5iv.arxiv.org/html/1907.02035 | primaria | 3/2/1/2 | [S] |
| Guía de visualización de la Comisión Europea https://data.europa.eu/apps/data-visualisation-guide/starting-bars-at-zero | primaria institucional | 2/2/2/1 | [S] |
| ONS https://digitalblog.ons.gov.uk/2016/06/27/does-the-axis-have-to-start-at-zero-part-1-line-charts | primaria institucional | 2/2/2/1 | [S] |

### Afirmaciones
- Cleveland y McGill (JASA, 1984) identifican tareas perceptuales elementales (la figura 1 ilustra 10). Orden de precisión según un resumen de curso: posición en escala común, posición en escalas no alineadas, longitud/dirección/ángulo, área, volumen/curvatura, sombreado/saturación de color. El resumen aclara que las diferencias promedio de exactitud a veces son de uno o dos en cien. Heer y Bostock lo replicaron y el ranking "largely held". Críticas posteriores: el orden es el más común, "by no means universal". https://vis.pku.edu.cn/course/visclass_f25/material/Graphical_perception.pdf ; https://arxiv.org/pdf/2212.10533 (ambos solo vistos en el buscador). No pude leer el abstract original: no cito literal.
- FT Visual Vocabulary agrupa los gráficos por la relación que se muestra: Deviation, Correlation, Ranking, Distribution, Change over Time, Part-to-whole, Magnitude, Spatial, Flow. Se apoya en Graphic Continuum de Schwabish y Ribecca. https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary
- Eje truncado: en barras, truncar el eje rompe la convención de que la diferencia de altura es proporcional a la diferencia de valores (Tableau Research); en líneas el caso es más defendible porque el dato se codifica por posición y no por longitud (ONS). Discrepancia entre fuentes: Datawrapper/CE dicen cero siempre en barras; Knaflic también discute el caso (https://www.storytellingwithdata.com/blog/2021/6/29/my-bars-dont-start-at-zero, solo título). https://ar5iv.arxiv.org/html/1907.02035 ; https://digitalblog.ons.gov.uk/2016/06/27/does-the-axis-have-to-start-at-zero-part-1-line-charts
- Tortas y doble eje: no hallé fuente primaria en las tres rondas. Lo que sí hay: la lógica de Cleveland-McGill (ángulo y área se leen peor que posición/longitud) explica por qué las tortas son difíciles de comparar; es inferencia mía, no cita. Hueco.

### Recurso canónico
FT Visual Vocabulary (el póster, para elegir por relación) y Cleveland-McGill (el ranking, con la salvedad de que es orientativo). Hueco: Few "Show Me the Numbers" no se leyó.

---

## 4. Dashboard

### Fuentes
| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Few, "Dashboard Confusion" (Intelligent Enterprise, 2004), reproducido en https://www.informationweek.com/government/dashboard-confusion-2 | primaria (reimpresión) | 3/2/1/3 | [S] |
| Reseña UXmatters de Information Dashboard Design (2006) https://www.uxmatters.com/mt/archives/2007/04/book-review-information-dashboard-design.php | secundaria | 2/2/2/1 | [S] |
| Few, "Why Most Dashboards Fail" https://blogs.ischool.berkeley.edu/i247s13/files/2013/02/WhyMostDashboardsFail.pdf | primaria | 3/2/2/2 | [M] (PDF binario, no leído) |

### Afirmaciones
- Few (2004): "A dashboard is a visual display of the most important information needed to achieve one or more objectives." El resto de la definición ("consolidated and arranged on a single screen so the information can be monitored at a glance") me llegó por resumen, no literal verificado. https://www.informationweek.com/government/dashboard-confusion-2
- En el libro de 2006, según la reseña: "A dashboard fits on a single computer screen" y "Dashboards are used to monitor information at a glance". Few clasifica por rol: estratégico, analítico, operativo; el rol es lo que más condiciona el diseño. Simplicidad como guía; condensar por resumen y por excepción. Otras fuentes agregan un tipo "táctico" que no es de Few. https://www.uxmatters.com/mt/archives/2007/04/book-review-information-dashboard-design.php
- Few (2007) distingue el dashboard de un "faceted analytical display" (varios gráficos interactivos en una pantalla para analizar). Esto importa: la mayoría de lo que llaman dashboard en Power BI o Looker Studio caería ahí. (Vía Tableau PDF https://www.tableau.com/sites/default/files/webinars/what_the_heck_is_a_dashboard_anyways.pdf, solo buscador.)

### Recurso canónico
Few, Information Dashboard Design (2006), capítulos de definición y los errores de diseño; más "Dashboard Confusion" para la cita. Fijarse en: una pantalla, para qué decisión, qué es excepción.

---

## 5. Capa semántica

### Fuentes
| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| dbt, Semantic Layer https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl | primaria (proveedor) | 3/2/2/2 | [S] |
| Looker, qué es LookML https://docs.cloud.google.com/looker/docs/what-is-lookml | primaria | 3/2/3/2 | [S] |
| Microsoft Learn, Semantic models in the Power BI service (ms.date 2025-10-01, updated_at 2026-04-28) https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand | primaria | 3/2/1/2 | [L] |
| Superset README https://github.com/apache/superset | primaria | 2/1/1/1 | [S] |

### Afirmaciones
- dbt: el Semantic Layer "lets data teams define metrics (such as revenue) on top of existing dbt models"; como la definición vive en la capa de modelado y no en la de BI, todas las herramientas usan la misma, y si cambia se refresca donde se invoque. Lo impulsa MetricFlow. Disponible en planes Starter y Enterprise (la página es inconsistente sobre Enterprise+). https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
- LookML es el lenguaje de Looker para modelos semánticos: describe dimensiones, agregados, cálculos y relaciones, y Looker genera el SQL; el usuario de negocio consulta sin escribir SQL. La página no usa el término "capa semántica". https://docs.cloud.google.com/looker/docs/what-is-lookml
- Power BI: el semantic model "represent a source of data that's ready for reporting and visualization"; los de Desktop son "effectively an Analysis Services tabular model"; modos Import, DirectQuery, Composite; seguridad por filas (RLS). Antes se llamaba "dataset" (la doc dice que usa semantic model y model casi como sinónimos). https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand
- Superset se describe con "a lightweight semantic layer". https://github.com/apache/superset
- Relación con la definición de métrica: la capa semántica es donde la definición (sección 1) se escribe una vez y se ejecuta; la tabla de parámetros de dbt es literalmente esa definición. Inferencia mía enlazando las fuentes.
- Hueco: no hay una fuente neutral (no de proveedor) que defina "capa semántica"; todo viene de proveedores.

### Recurso canónico
Doc de dbt Semantic Layer + página de métricas (para el concepto con YAML concreto); LookML para la versión histórica de la idea.

---

## 6. Contar con datos

### Fuentes
| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Knaflic, Storytelling with Data (Wiley 2015) https://oreilly.com/library/view/storytelling-with-data/9781119002253 | primaria | 3/3/3/2 | [M] |
| storytellingwithdata.com/books https://www.storytellingwithdata.com/books | primaria | 2/1/1/1 | [L] (no lista los pasos) |
| Resumen secundario (Goodreads, SuperSummary) | secundaria | 1/1/1/1 | [S] |

### Afirmaciones
- Los seis pasos (secundaria, no confirmados en el texto del libro): entender el contexto, elegir un visual efectivo, eliminar el desorden, dirigir la atención, pensar como diseñador, contar una historia. https://www.goodreads.com/notes/27156297-storytelling-with-data/1987374-bryan-tanner (solo buscador). El sitio oficial habla de "our proven, simple process for creating a clear and well-designed graph from selecting the chart type to thinking like a designer".
- Minto / pirámide en la presentación de hallazgos: NO se investigó fuente primaria (queda como hueco; hay un plugin local `pyramid-principle` en el entorno, pero no es fuente). Qué se podría decir sin fuente: respuesta primero, argumentos agrupados debajo.

### Recurso canónico
Knaflic, el libro, cap. 1-2 (contexto: audiencia, qué necesitan hacer, "big idea") a verificar al leerlo; confirmar nombres literales de los capítulos.

---

## 7. Ficha de herramientas de BI (fecha 2026-11-27)

| Herramienta | Licencia / precio público | Fuente | Marca |
|---|---|---|---|
| Power BI | Desktop gratis ("is available as a free download"); Pro USD 14,00 por usuario por mes (pago anual); Premium Per User USD 24,00 por usuario por mes (pago anual); para compartir hay que pasar a Pro o Premium | https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing | [S] |
| Metabase | Open Source gratis, AGPL; Starter (nube) USD 100/mes o 1.080/año, 5 usuarios, USD 6/mes extra por usuario; Pro USD 575/mes o 6.210/año, 10 usuarios; Enterprise desde USD 20.000/año | https://www.metabase.com/pricing/ | [S] |
| Superset | Apache-2.0; "Data Visualization and Data Exploration Platform" con constructor sin código, editor SQL y capa semántica liviana; versión y fecha de release no visibles | https://github.com/apache/superset | [S] |
| Tableau | Standard: Creator USD 75, Explorer 42, Viewer 15; Enterprise: Creator 115, Explorer 70, Viewer 35 (por usuario por mes, pago anual); al menos una licencia Creator por despliegue; precios varían por región | https://www.tableau.com/pricing/cloud (403 al leerlo directo; cifras de resultados del buscador de las páginas de Tableau) | [S] |
| Looker Studio | La versión gratuita existe (no verificada en esta ronda); Pro: la mayoría de las fuentes dicen USD 9 por usuario por proyecto por mes, una dice USD 7; no confirmé el precio oficial | https://docs.cloud.google.com/looker/docs/studio/pro-subscription-overview (precio oficial no accesible) | [S] |

Discrepancia declarada: Looker Studio Pro, 9 vs 7 USD por usuario/proyecto/mes. Para Argentina: precios en USD sin impuestos; hueco, no se vio moneda local ni impuestos.

---

## Huecos principales
1. Minto/pirámide aplicada a presentar hallazgos: sin fuente leída.
2. KPI vs métrica y árbol de métricas / driver tree: sin fuente primaria; la lista "qué fija una definición" es síntesis propia.
3. Goodhart: la frase de Strathern y la de Goodhart 1975 con su página vienen de Wikipedia; el PDF de Strathern no se pudo leer. Ries "tres A" sin confirmar.
4. Cleveland y McGill 1984 y Heer y Bostock: solo vistos en resúmenes; JSTOR y el PDF no cargaron. Few: definición completa y tipos, solo por reseñas.
5. Tortas y doble eje: sin fuente primaria. Visual Vocabulary no cubre errores.
6. Mixpanel: la página de conceptos avanzados dio 404, no hay ventana ni orden. Fechas de última edición de las docs de Amplitude, PostHog y GA4 no visibles.
7. Precios: Looker Studio Pro sin precio oficial; Tableau solo vía buscador (403); Looker Studio gratuito y moneda local sin verificar.
8. Casi todo lo leído fue vía un modelo que resume la página (marca [S]), no texto completo; solo la doc de Power BI se leyó entera [L].
