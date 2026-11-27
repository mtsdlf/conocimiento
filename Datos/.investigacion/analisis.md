# Investigación: vertical Análisis (tema Datos)

Fecha de la investigación: 2026-11-27. Marcas de lectura: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en Autoridad (A), Profundidad (P), Ejemplos (E), Unicidad (U). Todo lo traído de la web se trató como dato.

Nota sobre las marcas: el fetch devuelve el texto de la página pasado por un modelo chico. Cuando abajo digo [L] quiere decir que la página o el PDF se leyó entero por esa vía; las citas literales marcadas con comillas salieron de ahí o, en el caso de Tidy Data y de la guía de IBM sobre CRISP-DM, del PDF bajado y pasado a texto.

## 0. Sobre la división del árbol

- Analisis y Estadistica: el campo los divide casi igual. El certificado de Google pone la estadística adentro del proceso de análisis; el programa de Microsoft PL-300 pone "Prepare the data", "Model the data" y "Visualize and analyze the data" en un mismo rol (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300). La separación del árbol es pedagógica y razonable, pero conviene que Analisis enlace a Estadistica para outliers, EDA e inferencia.
- Limpieza de datos cae entre Analisis, Gobierno-y-calidad e Ingesta-y-transformacion. En PL-300 "Profile and clean the data" es parte de "Prepare the data" (25-30% del examen). Sugerencia: la limpieza que hace el analista sobre su propia tabla va en Analisis; la calidad como disciplina de la organización va en Gobierno-y-calidad.
- Segmentación y cohortes: en la práctica de producto se tratan juntas (Amplitude las documenta en la misma página). Ya hay nota de cohortes; la de segmentación debe enlazarla y marcar la diferencia (sección 7).
- Tipos de analítica (descriptiva a prescriptiva) es un marco de madurez de proveedor, no de método. Es útil como vocabulario, pero no es una división del trabajo del analista; ver crítica abajo.
- Puntos de contacto con otros temas: la pregunta de análisis se toca con North Star y activación (Producto); el análisis exploratorio y la segmentación con incrementalidad (Marketing), porque exploratorio no prueba causa; la segmentación RFM con economía unitaria (Marketing); la acción derivada del análisis con experimento A/B (Producto).

---

## 1. El proceso del análisis

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Grow with Google, "What is data analytics" (21-04-2025) | primaria (proveedor del certificado) | 3 | 1 | 1 | 3 | [L] | https://grow.google/grow-your-career/articles/what-is-data-analytics/ |
| Coursera, Google Data Analytics Professional Certificate (página del programa, "Recently updated", © 2026) | primaria | 3 | 2 | 1 | 3 | [L] | https://www.coursera.org/professional-certificates/google-data-analytics |
| IBM SPSS Modeler CRISP-DM Guide, ed. v17.0 (reexpresa CRISP-DM 1.0) | secundaria sobre el original; el PDF original (SPSS/NCR/Daimler/OHRA) no se pudo bajar | 2 | 3 | 2 | 1 | [L] | https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/17.0FP1/en/ModelerCRISPDM.pdf |
| CRISP-DM, Wikipedia | secundaria | 1 | 2 | 1 | 1 | [S] | https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining |
| Study guide PL-300 de Microsoft (actualizado 2026-11-05; habilidades medidas desde 2026-04-20) | primaria | 3 | 2 | 1 | 2 | [L] | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300 |
| Plotnikova, Dumas, Milani (PeerJ CS, 2020), revisión de 207 publicaciones de CRISP-DM, KDD y SEMMA | primaria (revisión) | 3 | 3 | 2 | 3 | [S] (la página dio 403; solo resumen del buscador) | https://peerj.com/articles/cs-267 |

### Afirmaciones

- Las seis fases de Google son ask, prepare, process, analyze, share, act. La página de Grow with Google las lista "Ask, Prepare, Process, Analyze, Share, Act" como los pasos de "How data analytics works" (https://grow.google/grow-your-career/articles/what-is-data-analytics/). La descripción fina de cada fase (por ejemplo "Process: limpiar y transformar") viene de resúmenes secundarios, no del texto oficial del curso; el buscador no encontró un documento oficial de Google con el texto completo de las seis fases.
- El certificado se cursa en 9 cursos en Coursera (Foundations; Ask Questions...; Prepare Data...; Process Data from Dirty to Clean; Analyze Data...; Share Data Through the Art of Visualization; Intro to Data Analysis Using Python; Capstone; Accelerate Your Job Search with AI). La página dice "over 180 hours" pero los cursos listados suman 151 horas: dos números que discrepan en la propia página (https://www.coursera.org/professional-certificates/google-data-analytics). Los cursos 1 al 6 cubren las seis fases; no hay un curso dedicado a "act". El curso de Python (curso 7) y el de IA son agregados recientes al programa; las versiones anteriores lo cerraban con R.
- CRISP-DM tiene seis fases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment (índice de los capítulos 2 a 7 de la guía de IBM, https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/17.0FP1/en/ModelerCRISPDM.pdf). Cita literal: "The life cycle model consists of six phases with arrows indicating the most important and frequent dependencies between phases. The sequence of the phases is not strict. In fact, most projects move back and forth between phases as necessary."
- Origen de CRISP-DM: concebido en 1996, proyecto ESPRIT de la UE en 1997, consorcio de ISL, Teradata, Daimler AG, NCR y OHRA; primera versión presentada en Bruselas en marzo de 1999 (https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining). Hay una fecha discrepante en circulación: el PDF "CRISP-DM 1.0" se cita como agosto de 2000 (resultado de búsqueda, no verificado en el PDF; [S]).
- Uso: encuestas de KDnuggets en 2002, 2004, 2007 y 2014 lo encontraron como metodología líder entre los mineros de datos que respondieron; la otra nombrada fue SEMMA. La página no da porcentajes (https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining).
- Vigencia: los intentos de actualizarlo empezaron en 2006 y no habían producido versión nueva a junio de 2015; el sitio original está inactivo; IBM publicó ASUM-DM en 2015 como extensión (misma fuente). Críticas de revisiones secundarias: no incluye gestión de proyecto ni soporte operativo posterior al despliegue (reseña PMC, [S]; https://pmc.ncbi.nlm.nih.gov/articles/PMC9044260); es "casi una cascada" aunque admite volver atrás (reseña SBC 2024, [S]; https://journals-sol.sbc.org.br/index.php/reviews/article/download/3757/2996/23245).
- Cómo se comparan. Las dos se solapan casi uno a uno, con tres diferencias de intención:
  1. Google: pensado para el analista de negocio que responde preguntas con tablas y gráficos; arranca por "ask" y termina en "act" (decisión). CRISP-DM: pensado para proyectos de minería de datos/modelado; arranca por entender el negocio y termina en desplegar un modelo.
  2. Google separa "process" (limpieza) de "prepare" (conseguir y organizar los datos); CRISP-DM los junta en Data Preparation (limpieza, construcción de atributos, integración, formateo; índice de la guía de IBM).
  3. CRISP-DM tiene Evaluación explícita (¿el modelo cumple el objetivo de negocio?); Google la reparte entre "analyze" y "share". La guía de IBM aclara que si el objetivo no es modelar (ejemplo de lavado de dinero) pesan más Data Understanding y Preparation, es decir, el proceso se adapta.
  No encontré una comparación publicada con método entre ambos; la correspondencia anterior es mía y se debe marcar como tal en la nota. La revisión de Plotnikova et al. compara CRISP-DM, KDD y SEMMA pero no pude leerla.
- Microsoft no define "proceso" sino un perfil: "Prepare the data (25-30%)", "Model the data (25-30%)", "Visualize and analyze the data (25-30%)", "Manage and secure Power BI (15-20%)" (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300). Es el recorte de un rol con una herramienta (Power BI), útil como tercer punto de vista.

### Recurso canónico
Para entender el proceso: la guía CRISP-DM (la versión de IBM, capítulo 1 y las secciones de Business Understanding y Data Preparation) porque es el texto con tareas y entregables explícitos; fijarse en las flechas de dependencia entre fases y en que no hay orden estricto. Para el camino práctico del principiante: los cursos 2 a 6 del certificado de Google, tratando las seis fases como ruta de aprendizaje, no como estándar.

---

## 2. Tipos de analítica: descriptiva, diagnóstica, predictiva, prescriptiva

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| CRM Magazine / destinationCRM, cobertura del Gartner Data & Analytics Summit 2017 (08-03-2017), con Peter Krensky | secundaria (periodística sobre un analista de Gartner) | 2 | 1 | 1 | 2 | [L] | https://www.destinationcrm.com/Articles/CRM-News/CRM-Featured-Articles/Gartner-Data-and-Analytics-Summit-2017-Day-2-The-Evolution-of-Analytics-116832.aspx |
| InformationWeek, sobre el Magic Quadrant 2013 de BI y analítica | secundaria | 2 | 1 | 1 | 2 | [S] | https://www.informationweek.com/data-management/gartner-magic-quadrant-looks-beyond-business-intelligence |
| Lepenioti et al., "Prescriptive analytics: Literature review and research challenges", Int. J. of Information Management 50 (2020) 57-70, DOI 10.1016/j.ijinfomgt.2019.04.003 | primaria (revisión académica) | 3 | 3 | 1 | 3 | [M] | https://ideas.repec.org/a/eee/ininma/v50y2020icp57-70.html |
| Gartner Insights Abstract (documento 7310630) | primaria, pero de pago | 3 | ? | ? | 3 | [no leído] | https://www.gartner.com/en/documents/7310630 |

### Afirmaciones

- Origen: el marco es de Gartner, al que se llama "Analytic Ascendancy Model". Fuentes de segunda mano discrepan en la fecha: algunas dicen 2012 ("definido en 2012" según un resumen de un Magic Quadrant); una revisión de 2024 en arXiv lo atribuye a un documento cerrado de 2013 y otro trabajo lo cita como "Maoz, 2013" (https://arxiv.org/pdf/1705.04958 y https://arxiv.org/pdf/2412.00034, [S]). No pude abrir el documento original de Gartner (de pago). Dos fechas posibles, 2012 y 2013, ninguna verificada en la fuente primaria. Una afirmación de un blog (Towards AI) de que se inspira en el Capability Maturity Model de ingeniería de software es de un solo blog, no la usaría sin más (https://pub.towardsai.net/the-analytics-maturity-model-how-to-know-where-your-data-team-actually-stands-24953688f57d).
- Definiciones de Gartner por boca de Krensky en 2017, literales: "descriptive analytics, which identify what happened"; "diagnostic analytics, which identify how it happened"; "predictive analytics, which identify what will happen"; "prescriptive analytics, which identify what should be done". Bajo predictiva entran "predictions, forecasting, and simulation"; bajo prescriptiva, "rules and optimization" (https://www.destinationcrm.com/Articles/CRM-News/CRM-Featured-Articles/Gartner-Data-and-Analytics-Summit-2017-Day-2-The-Evolution-of-Analytics-116832.aspx). Nótese que "diagnostic" aparece como "how it happened" en esta fuente y como "why" en otros resúmenes; el criterio de la nota debería ser "por qué pasó".
- Cifras de adopción de 2017 que circulan (74% descriptiva, 34% diagnóstica, 11% predictiva, 1% prescriptiva) vienen de un blog que cita a Gartner (https://pub.towardsai.net/the-analytics-maturity-model-how-to-know-where-your-data-team-actually-stands-24953688f57d, [S]); la nota de CRM Magazine que debería respaldarlas no contiene porcentajes. Sin respaldo directo: no usar como dato.
- Visión académica: la literatura académica tiende a nombrar tres tipos (descriptiva, predictiva, prescriptiva); Lepenioti et al. dicen que "prescriptive analytics, which seeks to find the best course of action for the future" es el paso siguiente de madurez y que el foco académico e industrial sigue en "descriptive and predictive analytics" (https://ideas.repec.org/a/eee/ininma/v50y2020icp57-70.html). Es decir, la diagnóstica es una categoría de Gartner/mercado más que académica.
- Críticas (mías, a partir de lo anterior, marcarlas como razonamiento y no como cita): (a) es un marco de madurez de organizaciones con la implicancia comercial de que "más arriba es mejor", pero una pregunta puede merecer una respuesta descriptiva; (b) las categorías no son etapas que se superan: se usan todas a la vez; (c) predictiva y prescriptiva dependen de modelos y de estadística (vertical Estadistica), y diagnóstica sigue siendo exploratoria, no causal (ver incrementalidad en Marketing y experimento A/B en Producto).

### Recurso canónico
No hay un texto neutral y gratuito del origen. Para el vocabulario: la nota de CRM Magazine por la cita directa de las cuatro definiciones. Para la crítica y el estado del campo: Lepenioti et al. (2020), solo introducción y conclusiones. Declararlo como hueco: falta el documento original de Gartner.

---

## 3. La pregunta de análisis

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Coursera, curso 2 "Ask Questions to Make Data-Driven Decisions" (programa del curso; copyright 2026) | primaria | 3 | 1 | 1 | 3 | [L] | https://www.coursera.org/learn/ask-questions-make-decisions |
| Guía de estudio de terceros (Trusted Institute) sobre SMART del curso 2 | secundaria | 1 | 2 | 2 | 1 | [S] | https://trustedinstitute.com/concept/google-data-analytics/ask-questions-data-driven-decisions/smart-questions-methodology/ |
| Provost y Fawcett, *Data Science for Business*, cap. 2 "Business Problems and Data Science Solutions" (O'Reilly, 2013) | primaria (libro) | 3 | 3 | 2 | 3 | [M] (índice y secundarios) | https://oreilly.com/library/view/data-science-for/9781449374273 |
| IBM, CRISP-DM guide, fase Business Understanding | secundaria sobre el original | 2 | 2 | 2 | 1 | [S] | https://www.ibm.com/docs/SS3RA7_sub/modeler_crispdm_ddita/clementine/crisp_help/crisp_business_objectives.html |
| Microsoft, "Business Problem Formulation" (blog de Machine Learning, archivo) | primaria (proveedor), viejo | 2 | 2 | 1 | 2 | [S] | https://docs.microsoft.com/en-us/archive/blogs/machinelearning/the-advanced-analytics-solution-building-process-business-problem-formulation |

### Afirmaciones

- El curso 2 del certificado tiene cuatro módulos (Ask effective questions, 3 h; Make data-driven decisions, 2 h; Spreadsheet magic, 7 h; Always remember the stakeholder, 3 h) y en el módulo 1 incluye "SMART questions" (video de 7 minutos) y "More about SMART questions" (lectura); la página no define SMART (https://www.coursera.org/learn/ask-questions-make-decisions).
- SMART según una guía de estudio de terceros (no oficial): specific, measurable, action-oriented, relevant, time-bound. Ejemplo literal: no-SMART "Is our website good?"; SMART "What was the average session duration and bounce rate for our homepage during the last quarter?" (https://trustedinstitute.com/concept/google-data-analytics/ask-questions-data-driven-decisions/smart-questions-methodology/, [S]). Ojo: "SMART" para metas (S-M-A-R-T con "achievable") es otro acrónimo; el de preguntas del curso usa "action-oriented". Confusión frecuente, vale una línea en la nota.
- Otras guías: Provost y Fawcett dedican una sección a pasar "From Business Problems to Data Mining Tasks" y sostienen que los problemas de negocio rara vez llegan como clasificación, regresión o clustering, hay que reformularlos (https://oreilly.com/library/view/data-science-for/9781449374273; resumen en https://arxiv.org/pdf/1901.02547, [S]). Ejemplos de un deck de curso basado en el libro: "Which customers are likely to respond to an offer?" (probabilidad de clase), "How much will a customer use the service?" (regresión), "Do our customers form natural groups?" (agrupamiento) (deck en Google Slides, [S], baja confianza).
- CRISP-DM separa objetivos de negocio, en términos de negocio, de objetivos de minería de datos, en términos técnicos (diapositivas de Purdue, [S]: https://www.cs.purdue.edu/homes/jhonorio/22spring-cs49000dsc-phase1-business-understanding.pdf). Microsoft pregunta si el problema es predictivo o explicativo (blog de Microsoft, [S]).
- Lo que tienen en común: la pregunta nombra la métrica, la población y el período, y dice qué decisión cambia con la respuesta. Esto es síntesis mía de las fuentes de arriba, no cita.

### Recurso canónico
Ninguno único y fuerte. Propongo el módulo 1 del curso 2 de Google (video y lectura de SMART) para el método, y el capítulo 2 de Provost y Fawcett para pasar de problema de negocio a tarea analítica; fijarse en que la pregunta SMART deja la decisión explícita. Hueco: no hay una fuente primaria que defina SMART-de-preguntas por escrito accesible sin inscribirse.

---

## 4. Limpieza de datos

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Wickham, "Tidy Data", Journal of Statistical Software 59(10), 2014 | primaria | 3 | 3 | 3 | 3 | [L] (PDF) | https://www.jstatsoft.org/article/view/v059i10 ; PDF https://vita.had.co.nz/papers/tidy-data.pdf |
| Rubin, "Inference and missing data", Biometrika 63(3), 581-592, 1976 | primaria (seminal) | 3 | 3 | 1 | 3 | [S] | https://dash.harvard.edu/entities/publication/73120378-8764-6bd4-e053-0100007fdf3b |
| NIST/SEMATECH e-Handbook, sección 7.1.6 "What are outliers in the data?" | primaria | 3 | 2 | 2 | 3 | [L] | https://itl.nist.gov/div898/handbook/prc/section1/prc16.htm |
| pandas 3.1.1, "Working with missing data" | primaria (documentación oficial, versión actual) | 3 | 2 | 3 | 2 | [L] | https://pandas.pydata.org/docs/user_guide/missing_data.html |
| PL-300, "Profile and clean the data" | primaria | 3 | 1 | 1 | 2 | [L] | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300 |

### Afirmaciones

- Datos ordenados: abstract literal, "Tidy datasets are easy to manipulate, model and visualize, and have a specific structure: each variable is a column, each observation is a row, and each type of observational unit is a table." Tres reglas: cada variable es una columna, cada observación una fila, cada tipo de unidad observacional una tabla (https://www.jstatsoft.org/article/view/v059i10). Publicado el 12-09-2014, vol. 59, número 10. Cita: "A huge amount of effort is spent cleaning data to get it ready for analysis" (misma URL). El artículo se limita a "data tidying", una parte chica de la limpieza.
- Los cinco problemas más comunes de datos desordenados, literales del PDF, sección 3: "Column headers are values, not variable names."; "Multiple variables are stored in one column."; "Variables are stored in both rows and columns."; "Multiple types of observational units are stored in the same table."; "A single observational unit is stored in multiple tables." Y la idea de Tolstoy: "tidy datasets are all alike but every messy dataset is messy in its own way." (https://vita.had.co.nz/papers/tidy-data.pdf).
- Faltantes: Rubin (1976) formalizó los mecanismos de datos faltantes tratando los indicadores de faltante como variables aleatorias. Los tres nombres que se usan hoy: MCAR (faltante completamente al azar, no depende de ningún valor), MAR (depende solo de lo observado), MNAR (depende del valor no observado). Matiz: Rubin no introdujo los nombres MCAR ni MNAR, solo MAR (resumen de la Universidad de Melbourne y revisiones, [S]; https://pmc.ncbi.nlm.nih.gov/articles/PMC7615108 y https://scc.ms.unimelb.edu.au/resources/preparing-your-data/missing-data). Hay inconsistencia de uso de MAR y MCAR documentada en la literatura. Consecuencia práctica para la nota: borrar o imputar no es neutro; hay que preguntarse por qué falta.
- Faltantes en herramientas: en pandas, "`dropna()` drops rows or columns with missing data" y "`fillna()` replaces NA values with non-NA data"; "Equality comparisons between `np.nan`, `NaT`, and `NA` do not act like `None`" (np.nan == np.nan da False), así que `df == np.nan` no encuentra faltantes: usar `isna()` (https://pandas.pydata.org/docs/user_guide/missing_data.html, versión 3.1.1). Esa página no cubre duplicados (hueco; ver abajo).
- Outliers: NIST: "An outlier is an observation that lies an abnormal distance from other values in a random sample from a population." y "Outliers should be investigated carefully."; antes de sacar un punto hay que entender por qué apareció. Vallas: "lower inner fence: Q1 - 1.5*IQ", "upper inner fence: Q3 + 1.5*IQ", "lower outer fence: Q1 - 3*IQ", "upper outer fence: Q3 + 3*IQ"; más allá de las internas son atípicos leves, más allá de las externas, extremos (https://itl.nist.gov/div898/handbook/prc/section1/prc16.htm). La página no atribuye la regla de 1.5 a Tukey; una página de MedCalc dice que Tukey eligió el 1.5 "empíricamente" ([S]; https://www.medcalc.org/en/book/outlier-detection.php). La prueba de Grubbs sirve para un solo atípico en datos aproximadamente normales; para varios, NIST recomienda Tietjen-Moore o ESD generalizado ([S]; https://itl.nist.gov/div898/handbook/eda/section3/eda35h.htm).
- PL-300 pone en "Profile and clean the data": "Evaluate data, including data statistics and column properties", "Resolve inconsistencies, unexpected or null values, and data quality issues", "Resolve data import errors" (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300). Formatos (tipos de dato, fechas, texto): "Select appropriate column data types" figura en "Transform and load" de la misma guía.
- Duplicados: no encontré fuente primaria con la definición ni criterio; hueco.

### Recurso canónico
Wickham (2014), secciones 2 y 3 (definición de tidy y los cinco problemas con sus arreglos). Fijarse en que el artículo usa tablas chicas para cada problema y que el arreglo siempre es llevar a "una variable, una columna". Para faltantes y atípicos como decisión (no como receta): NIST 7.1.6 para atípicos, más una fuente introductoria de faltantes (hueco; Rubin 1976 es demasiado técnico para este nivel).

---

## 5. SQL para análisis

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| PostgreSQL 19, tutorial 3.5 "Window Functions" | primaria (documentación oficial) | 3 | 2 | 3 | 2 | [L] | https://www.postgresql.org/docs/current/tutorial-window.html |
| PostgreSQL 19, 7.2 "Table Expressions" (JOIN, WHERE, GROUP BY, HAVING) | primaria | 3 | 3 | 2 | 2 | [L] | https://www.postgresql.org/docs/current/queries-table-expressions.html |
| PostgreSQL 19, 9.2 "Comparison Functions and Operators" (NULL) | primaria | 3 | 2 | 3 | 2 | [L] | https://www.postgresql.org/docs/current/functions-comparison.html |
| Kimball Group, técnica "Grain" | primaria (autoridad en modelado) | 3 | 1 | 1 | 3 | [L] | https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/ |
| Google Cloud Community, "The problem of SQL fanouts" (Brett Sauve, 22-06-2022) | secundaria (comunidad de proveedor) | 2 | 2 | 2 | 2 | [L] | https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220.md |
| Holistics docs, "Fan-out resolution" | secundaria (proveedor de BI) | 2 | 2 | 1 | 2 | [S] | https://docs.holistics.io/docs/joins/fan-out-resolution |

### Afirmaciones

- La documentación consultada es de PostgreSQL 19, que según el banner de la página salió el 19-11-2026. Ejemplos ahí verificados valen para otras bases (la sintaxis de ventanas es SQL estándar), pero conviene decir que se probó con PostgreSQL.
- Orden de procesamiento: "The optional `WHERE`, `GROUP BY`, and `HAVING` clauses in the table expression specify a pipeline of successive transformations performed on the table derived in the `FROM` clause." y "After passing the `WHERE` filter, the derived input table might be subject to grouping, using the `GROUP BY` clause, and elimination of group rows using the `HAVING` clause." (https://www.postgresql.org/docs/current/queries-table-expressions.html). Idea para la nota: se lee FROM, después WHERE, GROUP BY, HAVING, y recién al final SELECT.
- Joins: INNER JOIN: "For each row R1 of T1, the joined table has a row for each row in T2 that satisfies the join condition with R1." LEFT OUTER JOIN: "First, an inner join is performed. Then, for each row in T1 that does not satisfy the join condition with any row in T2, a joined row is added with null values in columns of T2. Thus, the joined table always has at least one row for each row in T1." (misma URL). La primera frase ya explica el fan-out: una fila de T1 se repite por cada coincidencia en T2.
- Funciones de ventana, literal: "A _window function_ performs a calculation across a set of table rows that are somehow related to the current row." y "window functions do not cause rows to become grouped into a single output row like non-window aggregate calls would. Instead, the rows retain their separate identities." `PARTITION BY` "divides the rows into groups, or partitions, that share the same values"; el `ORDER BY` dentro de `OVER` controla el orden de procesamiento. Ejemplo oficial: `SELECT depname, empno, salary, row_number() OVER (PARTITION BY depname ORDER BY salary DESC) FROM empsalary;` devuelve las 10 filas (https://www.postgresql.org/docs/current/tutorial-window.html).
- Grano: Kimball: "The grain establishes exactly what a single fact table row represents." Declararlo es "a binding contract on the design", va antes de elegir dimensiones y hechos, y "every candidate dimension or fact must be consistent with the grain" (https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/). El analista lo usa a la inversa: antes de usar una tabla, preguntar "¿qué es una fila?". Pasar del concepto de Kimball a "grano de cualquier tabla" es extensión mía; marcarla así. Se toca con Modelado-y-almacenamiento.
- Fan-out: definición literal de la comunidad de Google: "Since the joined table has more rows than the primary table, we say that a _fanout_ has occurred." Lo causan los joins uno-a-muchos; uno-a-uno y muchos-a-uno no. Chequeo: `COUNT(*)` de la tabla principal y de la tabla principal con `LEFT JOIN` a la otra; si el conteo sube, hay fan-out; el autor aclara que entender el tipo de join es mejor que contar, porque contar no detecta riesgo futuro (https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220.md). Arreglo habitual: agregar el lado "muchos" a una fila por clave en una subconsulta antes de unir (descrito por varios blogs, por ejemplo https://buttondown.com/SystemCraftPress/archive/your-join-is-quietly-doubling-your-numbers/, [S], calidad baja; "28% de inflación de ingresos sobre unos 100.000 pedidos" es de un repositorio personal de GitHub, anecdótico, no usar como dato). Una herramienta de BI (Holistics) documenta que sus "symmetric aggregates" solo dan bien si la clave declarada es de verdad única; si no, "silently" mal (https://docs.holistics.io/docs/joins/fan-out-resolution, [S]). Es un caso de "cómo falla".
- NULL, literal: "Ordinary comparison operators yield null (signifying 'unknown'), not true or false, when either input is null. For example, `7 = NULL` yields null, as does `7 <> NULL`." y "Do _not_ write `_expression_ = NULL` because `NULL` is not 'equal to' `NULL`." Para testear: `IS NULL` / `IS NOT NULL`; para comparar tratando NULL como un valor, `IS [NOT] DISTINCT FROM` (https://www.postgresql.org/docs/current/functions-comparison.html). Otros errores clásicos con NULL (agregados que ignoran NULL, `NOT IN` con NULL en la subconsulta) no los verifiqué en fuente primaria; hueco.
- LEFT JOIN y NULL: después de un LEFT JOIN, las columnas de la derecha pueden venir en NULL; un `WHERE` sobre esas columnas las vuelve en un INNER JOIN encubierto. Esto es inferencia mía a partir de la definición citada de LEFT OUTER JOIN y del pipeline FROM, WHERE; verificarlo con un ejemplo corrido antes de escribirlo.

### Recurso canónico
La documentación de PostgreSQL, capítulos 2 al 3 (tutorial: SELECT, joins, agregados, ventanas) y 7.2. Fijarse en el ejemplo `empsalary`, que se repite en todo el tutorial y permite al principiante seguir una sola tabla. Para el grano y el fan-out: nota de Kimball (corta) más el hilo de Google Cloud Community. Hueco: no hay un libro o curso primario sobre "SQL para análisis" que haya revisado; no corrí consultas.

---

## 6. Análisis exploratorio (EDA)

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| NIST/SEMATECH e-Handbook, 1.1.1 y 1.1.2 (EDA y su relación con enfoques clásico y bayesiano) | primaria | 3 | 2 | 1 | 3 | [L] | https://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm ; https://www.itl.nist.gov/div898/handbook/eda/section1/eda12.htm |
| Tukey, *Exploratory Data Analysis*, Addison-Wesley, 1977 | primaria (libro) | 3 | 3 | 3 | 3 | [S] (sin acceso al texto; citas por Friendly/Hoaglin) | referenciado en https://datavis.ca/papers/EDA-history.pdf (el fetch falló por certificado) |
| Wickham y Grolemund, *R for Data Science* 2ª ed., cap. de EDA | primaria (libro abierto) | 3 | 2 | 3 | 2 | [L] | https://r4ds.hadley.nz/EDA.html |
| Anscombe, "Graphs in Statistical Analysis", The American Statistician 27(1), 17-21, 1973 (DOI 10.1080/00031305.1973.10478966) | primaria (paper) | 3 | 2 | 3 | 3 | [S] | https://en.wikipedia.org/wiki/Anscombe%27s_quartet |

### Afirmaciones

- NIST define EDA como "an approach/philosophy for data analysis that employs a variety of techniques (mostly graphical)" y como "a philosophy as to how we dissect a data set" (https://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm). La página no tiene fecha. Contraste con enfoque clásico y bayesiano (1.1.2): en el clásico, "the data collection is followed by the imposition of a model"; en EDA, la recolección "is followed immediately by analysis with a goal of inferring what model would be appropriate"; en el bayesiano se impone "a data-independent distribution on the parameters of the selected model" (https://www.itl.nist.gov/div898/handbook/eda/section1/eda12.htm). Ninguna de las dos páginas menciona a Tukey.
- Tukey (1977), p. 1, según la revisión histórica de Hoaglin: "Exploratory data analysis is detective work — numerical detective work or counting detective work — or graphical detective work" ([S], vía resultado de búsqueda; sin leer el texto de origen). La contraposición con el análisis confirmatorio como "tribunal" (evaluar evidencia) y su idea de que ambos "pueden y deben avanzar en paralelo" aparecen en fuentes secundarias ([S]; https://methods.sagepub.com/ency/edvol/embed/encyc-of-research-design/chpt/exploratory-data-analysis). Discrepancia de fecha: algunas fuentes dicen que EDA aparece impreso en 1970 (ediciones preliminares) y el libro es 1977.
- R4DS 2ª ed.: EDA "is not a formal process with a strict set of rules", es "more a state of mind"; las dos preguntas guía son "What type of variation occurs within my variables?" y "What type of covariation occurs between my variables?" (https://r4ds.hadley.nz/EDA.html). Útil porque da un método concreto para el principiante.
- Anscombe (1973): cuatro conjuntos de 11 pares (x, y) con estadísticos resumen casi idénticos y gráficos muy distintos; el paper buscaba contrarrestar la creencia de que "numerical calculations are exact, but graphs are rough" ([S], vía Wikipedia; https://en.wikipedia.org/wiki/Anscombe%27s_quartet). Seguimiento de Matejka y Fitzmaurice (2017) con el "datasaurus dozen" ([S], solo título verificado). Es el mejor ejemplo para enseñar por qué mirar antes de resumir.
- Límite: el análisis exploratorio genera hipótesis; no prueba causa. Se toca con incrementalidad (Marketing) y experimento A/B (Producto); el vínculo es inferencia mía a partir de la contraposición exploratorio/confirmatorio.

### Recurso canónico
NIST 1.1.1 y 1.1.2 para el concepto (cortas, estables); R4DS cap. EDA para la práctica (las dos preguntas) y Anscombe como ejemplo. Tukey (1977) es el texto fundacional, pero no pude leerlo; el libro es denso y no es para quien no sabe estadística: citarlo, no recomendarlo como lectura inicial.

---

## 7. Segmentación de clientes y diferencia con cohortes

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| IBM SPSS Statistics, "RFM Analysis" (v23) | primaria (documentación de proveedor, vieja) | 2 | 2 | 1 | 2 | [L] | https://www.ibm.com/support/knowledgecenter/SSLVMB_23.0.0/spss/rfm/rfm_intro.xml.html |
| Bult y Wansbeek, "Optimal Selection for Direct Mail", Marketing Science 14(4), 378-394, 1995 | primaria (paper) | 3 | 3 | 1 | 3 | [M] | https://ideas.repec.org/a/inm/ormksc/v14y1995i4p378-394.html |
| DMA (UK), "Use RFM modelling to generate successful customer segments" | secundaria (gremio) | 2 | 1 | 1 | 1 | [S] | https://dma.org.uk/article/use-rfm-modelling-to-generate-successful-customer-segments |
| Amplitude, "Segments and cohorts" (última actualización 2026-10-29) | primaria (documentación de proveedor), reciente | 2 | 2 | 1 | 2 | [L] | https://amplitude.com/docs/analytics/segments/segments-and-cohorts |
| Userpilot (blog) y SendPulse (glosario) sobre segmentos vs cohortes | secundaria (blogs de proveedor) | 1 | 1 | 1 | 1 | [S] | https://userpilot.com/blog/?p=12946 ; https://sendpulse.com/en/support/glossary/cohort-analysis |

### Afirmaciones

- RFM (recency, frequency, monetary), según IBM: "The most important factor in identifying customers who are likely to respond to a new offer is recency."; recencia es la fecha o el tiempo desde la última compra; frecuencia, cuántas compras; monetario, "total amount spent". Cada eje se rankea en categorías (en un esquema de cinco, 5 es lo mejor y 1 lo peor) y los tres puntajes se concatenan: el mejor puntaje posible es 555. La propia página la llama una "simple theory" y no presenta validación estadística; los datos de entrada son por cliente, y si hay varias transacciones por cliente hay que resumirlas antes (https://www.ibm.com/support/knowledgecenter/SSLVMB_23.0.0/spss/rfm/rfm_intro.xml.html).
- Origen disputado: la DMA dice que Bult y Wansbeek introdujeron RFM en 1995; otras fuentes lo ubican antes (Cullinan, y Hughes, *Strategic Database Marketing*, 1994) (resumen de búsqueda, [S]). El abstract de Bult y Wansbeek (1995) habla de un método para elegir a quién enviar correo directo que "explicitly accounts for the profit function", no de inventar RFM; la lectura prudente es que su aporte es el marco de optimización (https://ideas.repec.org/a/inm/ormksc/v14y1995i4p378-394.html). Origen real de RFM: no verificado en fuente primaria; declarado como hueco.
- Otras segmentaciones (no verificadas en esta ronda): por valor (RFM, CLV), demográfica, por comportamiento/uso, por necesidades, por canal de adquisición, por plan o producto; los k-means u otras técnicas de agrupamiento. Solo RFM y el contraste con cohortes fueron respaldados con fuentes. Hueco.
- Diferencia con cohortes. Amplitude: un segmento es "An advanced filter for analysis. A segment returns the events that meet a set of user, session, or event conditions."; una cohorte es "An audience. A cohort returns the set of users who met conditions in a fixed or dynamic date range."; "A user-scoped segment automatically uses the date range of the chart or dashboard you apply it to"; "A cohort uses its own date range." (https://amplitude.com/docs/analytics/segments/segments-and-cohorts, 2026-10-29). Userpilot y SendPulse coinciden en que la cohorte se define por una ventana de tiempo (por ejemplo mes de alta) y el segmento por rasgos o conducta sin anclaje temporal, y que se complementan ([S], blogs de proveedor). Esta definición viene de documentación de un proveedor; en estadística y en epidemiología, "cohorte" tiene otro sentido (Wikipedia lo nota: https://www.wikipedia.org/wiki/Cohort_analysis).
  Para la nota: cohorte = quién entró cuándo (eje tiempo); segmento = qué tipo de cliente es (eje atributo o conducta). Se cruzan: se puede mirar retención por segmento dentro de una cohorte. Ya hay notas de cohortes, retención y churn: enlazar, no repetir.
- Punto de contacto con otros temas: la segmentación sirve para decidir a qué segmento dirigir una acción (Marketing), pero que un segmento compre más no prueba que la acción sobre él cause más compras (incrementalidad). Vinculado a economía unitaria si se calcula valor por segmento.

### Recurso canónico
Para RFM: la página de IBM (corta, explica el cálculo paso a paso) más la advertencia de que es una regla práctica sin validación; fijarse en la concatenación 555 y en que los puntos de corte los elige el analista. Para la diferencia con cohortes: la documentación de Amplitude (fechada 2026-10-29), declarando que es de un proveedor.

---

## 8. Ficha: herramientas del analista (a 2026-11-27)

Las versiones que siguen son lo que las páginas oficiales mostraban hoy.

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| pandas, "What's new" (índice) | primaria | 3 | 2 | 1 | 3 | [L] | https://pandas.pydata.org/docs/whatsnew/index.html |
| pandas, "What's new in 3.0.0 (January 21, 2026)" | primaria | 3 | 3 | 2 | 3 | [L] (los primeros 100.000 de 269.902 caracteres) | https://pandas.pydata.org/docs/whatsnew/v3.0.0.html |
| python.org, Downloads | primaria | 3 | 1 | 1 | 3 | [L] | https://www.python.org/downloads/ |
| PostgreSQL 19 docs (banner: lanzada el 19-11-2026) | primaria | 3 | 3 | 3 | 3 | [L] | https://www.postgresql.org/docs/current/ |
| JupyterLab: PyPI y changelog | primaria/espejo | 3 | 1 | 1 | 2 | [S] | https://simple-repository.app.cern.ch/project/jupyterlab ; https://jupyterlab.readthedocs.io/en/4.6.x/getting_started/changelog.html |
| Microsoft PL-300 study guide | primaria | 3 | 2 | 1 | 2 | [L] | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300 |

### Hechos fechados

- Python: última versión estable listada, 3.15.2 (25-10-2026). 3.15 salió el 2026-10-09; 3.14 y 3.15 reciben correcciones; 3.13, 3.12 y 3.11 solo seguridad; 3.10 llegó a fin de vida el 2026-10-01 (https://www.python.org/downloads/).
- pandas: 3.1.1 del 04-11-2026 (3.1.0 el 22-10-2026). Línea 3.0.0 del 2026-01-21. Cambios que rompen código de tutoriales viejos: tipo de texto dedicado por defecto ("a dedicated string data type is enabled by default (backed by PyArrow under the hood, if installed, otherwise falling back to being backed by NumPy `object`-dtype)"); Copy-on-Write: "chained assignment ... will stop working" y se quita `SettingWithCopyWarning`; pandas 3.0.0 "supports Python 3.11 and higher" (https://pandas.pydata.org/docs/whatsnew/v3.0.0.html). Para materiales viejos (incluido el del certificado de Google, que se grabó cuando pandas era 1.x/2.x), vale una advertencia en la nota. Las notas de la versión recomiendan pasar primero por 2.3 y arreglar las advertencias de deprecación.
- JupyterLab: la versión más nueva encontrada, 4.5.6 (11-03-2026); la 4.6 solo en alfas hasta marzo de 2026. Puede haber una más nueva que el buscador no mostró; verificar antes de publicar ([S], baja confianza).
- PostgreSQL 19: documentación "Current". El banner dice lanzada el 19-11-2026, es decir, hace ocho días; si la nota enseña SQL sobre una base concreta, fijar la versión.
- DuckDB: no pude confirmar versión ni descripción (la página devolvió una redirección a "docs/2.0/"); no incluir en la ficha sin verificar.
- Planillas (Excel, Google Sheets): sin fuente oficial consultada en esta ronda. Lo que sí hay: el curso 2 del certificado de Google dedica el módulo 3 ("Spreadsheet magic", 7 horas) a planillas, y el certificado usa SQL y Python como siguientes pasos (https://www.coursera.org/learn/ask-questions-make-decisions y https://www.coursera.org/professional-certificates/google-data-analytics). Hueco: versiones y límites actuales de filas.
- Power BI: PL-300 mide habilidades desde el 2026-04-20; exige "Power Query" y "DAX" (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300). Corresponde sobre todo a Visualizacion-y-BI; acá solo un puntero.

### Cómo decidir entre herramientas
No encontré una comparación con método publicada (cuándo planilla, SQL o Python). Se puede describir qué hace cada una, no cuál conviene; la guía por tamaño de datos y repetibilidad sería criterio propio, a marcar como tal. Hueco.

### Recurso canónico
Para cada herramienta, su documentación oficial con versión: PostgreSQL (tutorial, capítulos 2 a 3), pandas ("10 minutes to pandas" y "Working with missing data"), Python (python.org). Fijarse en que las tres páginas muestran la versión en el encabezado y que la nota debe copiarla.

---

## 9. Huecos principales

1. Documento original de Gartner (Analytic Ascendancy Model): sin acceso (de pago); fecha 2012 frente a 2013 sin resolver; cifras de adopción 2017 sin respaldo directo.
2. CRISP-DM 1.0 original (PDF de 2000): no se pudo bajar (403 en el servidor de SMU y 404 en otro); la información del proceso viene de la guía de IBM y de Wikipedia. Sin comparación con método entre CRISP-DM y las seis fases de Google. Revisión de Plotnikova et al. (2020) sin leer (403).
3. Texto oficial del curso de Google (definiciones de las seis fases y de SMART): solo páginas de programa y resúmenes de terceros.
4. Tukey (1977) sin leer; el texto "detective work" viene de una revisión secundaria; la revisión de Friendly no se pudo abrir (certificado).
5. Limpieza: nada primario sobre duplicados ni sobre formatos (fechas, texto, unidades); nada sobre imputación como método (solo Rubin 1976 por resumen).
6. SQL: no se corrió código para verificar los ejemplos; NOT IN con NULL, agregados que ignoran NULL y el LEFT JOIN con filtro en WHERE no verificados en fuente primaria; no hay fuente primaria sobre "SQL para análisis" como tema.
7. Segmentación: origen real de RFM sin verificar; otras técnicas de segmentación (agrupamiento, CLV) sin fuente; la definición de cohorte vs. segmento es de documentación y blogs de proveedores.
8. Herramientas: planillas, DuckDB y comparativa sin fuente; JupyterLab con baja confianza de recencia.
9. En general, las páginas se leyeron por un resumidor automático, no a ojo; las citas literales de pandas, PostgreSQL, NIST, Kimball, IBM y Amplitude conviene volver a cotejarlas al escribir las notas definitivas.
