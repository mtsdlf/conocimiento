# Fundamentos y entrada del tema Datos: informe de investigación

Fecha de la investigación: 2026-11-27. Marcas: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Nota metodológica: WebFetch devuelve el texto pasado por un modelo chico, así que lo marcado [L] fue leído de esa extracción (no a mano). Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad.

## Veredicto sobre la división del árbol

- El campo no divide el trabajo en "verticales" sino en un recorrido del dato (generar, almacenar, ingerir, transformar, servir) más preocupaciones transversales (seguridad, gestión, calidad). El árbol aprobado calza bastante con ese recorrido: Ingesta-y-transformacion y Modelado-y-almacenamiento son etapas; Gobierno-y-calidad es transversal (en Reis y Housley es "data management"; en DAMA es el centro de la rueda); Análisis, Estadística, Analítica-de-producto y Visualización-y-BI son el tramo "serve" (servir) y lo que hace el consumidor del dato.
- Dos desajustes a decir en la entrada del tema: (1) Estadística no es una etapa del recorrido; es una disciplina que atraviesa Análisis y experimentación. (2) Reis y Housley no cubren análisis ni BI (su ciclo termina en "servir" y sirve a analítica, ML y reverse ETL); DAMA sí tiene "Data Warehousing and BI" como área pero no estadística ni analítica de producto. Ninguna de las dos fuentes de marco cubre Analítica-de-producto: esa vertical es del mundo de producto (Amplitude, Mixpanel), no de ingeniería ni de gestión de datos.

---

## 1. Recorrido del dato: ciclo de vida de Reis y Housley y rueda DAMA

### Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca | Nota |
|---|---|---|---|---|---|
| Reis y Housley, Fundamentals of Data Engineering, cap. 2 (O'Reilly, 2022) | https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html | primaria | 3/3/2/3 | [S] (la fetch dio 403; contenido confirmado vía buscador) | Fuente canónica; leerla en el libro |
| Joe Reis, "The Data Engineering Lifecycle and Undercurrents, 4 Years Later" (substack del autor) | https://joereis.substack.com/p/the-data-engineering-lifecycle-and | primaria (autor) | 3/2/1/3 | [L] | Fechada 2026-07-27; recencia alta |
| DAMA International, infografías DMBOK2R | https://dama.org/dmbok2r-infographics/ | primaria | 3/2/1/3 | [L] | Lista diagramas de contexto, no "las 11 áreas" |
| DAMA, revisión 2024 del DMBOK 2.0 | https://dama.org/dama-dmbok-revision/ | primaria | 3/1/1/3 | [L] | |
| Dawiso, glosario DAMA-DMBOK | https://www.dawiso.com/glossary/dama-dmbok | secundaria (proveedor) | 1/1/1/1 | [S] | Única que dio la lista de 11 por nombre |
| DAMA, "What Is DAMA International?" (2026-04-14) | https://dama.org/2026/04/14/what-is-dama-international-a-guide-for-data-professionals/ | primaria | 2/1/1/1 | [S] | Dice "11 core knowledge areas" |

### Afirmaciones

- Etapas del ciclo (5): generation, storage, ingestion, transformation, serving. El autor las lista como "Generate", "Store", "Ingest", "Transform", "Serve" en https://joereis.substack.com/p/the-data-engineering-lifecycle-and (confirmación del autor en 2026; el libro usa los sustantivos, según el resumen del buscador de https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html).
- Undercurrents (6): "Security", "Data management", "DataOps", "Data architecture", "Orchestration", "Software engineering" (https://joereis.substack.com/p/the-data-engineering-lifecycle-and). Lista confirmada por el autor, no solo por secundarias.
- El libro salió el 26 de julio de 2022 según el mismo post de Reis (https://joereis.substack.com/p/the-data-engineering-lifecycle-and). O'Reilly/buscador lo da como "June 2022": discrepancia de fecha de publicación (junio en el catálogo, 26 de julio en el autor); en el tema conviene citar solo "2022".
- Reis (2026) considera un séptimo undercurrent, FinOps ("not fully sold yet"), y duda si IA/ML debería ser uno; agregaría "More depth on data modeling" (https://joereis.substack.com/p/the-data-engineering-lifecycle-and). Sirve para decir que el marco es vivo.
- El ciclo cubre solo las etapas que controla el ingeniero de datos, no todo el ciclo de vida del dato (resumen del buscador sobre https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html) [S].
- DAMA-DMBOK2: la página oficial de infografías enumera 14 diagramas de contexto, no 11: Data Handling Ethics; Data Governance and Stewardship; Data Architecture; Data Modeling and Design; Data Storage and Operations; Data Security; Data Integration and Interoperability; Document and Content Management; Reference and Master Data; Data Warehousing and Business Intelligence; Metadata Management; Data Quality Management; Big Data and Data Science; Data Management Maturity Assessment (https://dama.org/dmbok2r-infographics/).
- DISCREPANCIA a dar con las dos versiones: la cifra "11 áreas de conocimiento" (con gobierno en el centro) viene de DAMA misma en un artículo de 2026 (https://dama.org/2026/04/14/what-is-dama-international-a-guide-for-data-professionals/) y de secundarias; un resumen del buscador dice que otra página de DAMA habla de 10. Las 11 por nombre según Dawiso (https://www.dawiso.com/glossary/dama-dmbok): Data Governance, Data Architecture, Data Modeling & Design, Data Storage & Operations, Data Security, Data Integration & Interoperability, Document & Content Management, Reference & Master Data, Data Warehousing & BI, Metadata Management, Data Quality. Esta lista coincide con las áreas 2 a 12 de la página de DAMA menos "Data Handling Ethics" (que el DMBOK2 trata como capítulo propio, no como rueda). Una sola fuente secundaria por nombre: no verificada contra el libro.
- Edición: DAMA-DMBOK2 es de 2017 (Wikipedia, según el buscador, "2017 July 1" [S]) y hay una revisión 2024: "The 2024 Revision of the DAMA-DMBOK 2.0 ® is a maintenance release" con "terminology updates, minor structural refinements, and improved representations"; "No material changes were made to the overarching data management framework, knowledge areas, or their definitions" (https://dama.org/dama-dmbok-revision/). Existe un "DAMA-DMBOK 3.0 Project" (solo enlace de navegación, sin contenido).
- Cómo se relacionan (síntesis propia, marcada como inferencia): el ciclo de Reis y Housley es una vista de proceso (qué le pasa al dato en orden) para quien construye; la rueda DAMA es una vista de funciones de gestión (qué capacidades necesita una organización) para quien gobierna. Se solapan: "data management" es un undercurrent en uno y la rueda entera en el otro; calidad, seguridad, metadatos y modelado son áreas DAMA y aparecen distribuidas en el ciclo. Ninguna fuente leída compara los dos marcos explícitamente: es hueco.

### Recurso canónico

Reis y Housley, cap. 1 y 2: el diagrama del ciclo con los undercurrents debajo. Fijarse en que sirve para ubicar en qué tramo está un problema ("el dato llega tarde" es ingesta; "los números no coinciden" es transformación o gestión). Complemento: el post de Reis de 2026 para lo que cambiaría. Para la rueda DAMA, la página de infografías de dama.org y, para el detalle, el libro (no gratuito).

---

## 2. Roles de datos

### Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca | Nota |
|---|---|---|---|---|---|
| dbt Labs, "Analytics engineer vs data analyst" | https://www.getdbt.com/blog/analytics-engineer-vs-data-analyst | proveedor (marcar) | 2/2/1/2 | [L] | No trata data scientist |
| dbt Labs, "What is analytics engineering" | https://www.getdbt.com/blog/what-is-analytics-engineering | proveedor (marcar) | 2/2/1/2 | [L] | |
| U.S. BLS OOH, Data Scientists | https://www.bls.gov/ooh/math/data-scientists.htm | primaria | 3/2/1/3 | [L] | Modificada 2026-08-27 |
| Microsoft, study guide PL-300 | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300 | primaria (proveedor) | 3/3/2/3 | [L] | Habilidades al 2026-04-20 |
| Sysarmy, resultados encuesta 2026.1 | https://sysarmy.com/blog/posts/resultados-de-la-encuesta-de-sueldos-2026-1/ | primaria (voluntaria, autorreportada) | 2/1/1/3 | [L] | Sin desglose por rol en la página |
| iProfesional con cifras Sysarmy por rol | https://www.iprofesional.com/management/378368-sueldo-de-los-profesionales-it-en-argentina-puestos-mejor-pagos | secundaria | 1/1/1/1 | [S] | Período incierto; no usar |
| IBM Think (data analyst vs data scientist) | https://www.ibm.com/think/topics/data-analyst-vs-data-scientist | proveedor | - | no leída: la URL probada era un índice | Hueco |

### Afirmaciones

- Analista de datos (dbt Labs, proveedor): "Data analysts transform raw data into business insights"; se enfocan en problemas de negocio, tendencias, reportes y visualizaciones (https://www.getdbt.com/blog/analytics-engineer-vs-data-analyst).
- Ingeniero de datos (dbt Labs): "Data engineers build systems to collect and process data"; crean "the foundation for all data work" con pipelines e infraestructura confiables (misma URL). En la otra nota: extrae de los sistemas fuente, transforma y carga al warehouse (https://www.getdbt.com/blog/what-is-analytics-engineering).
- Analytics engineer (dbt Labs): "Analytics engineers provide clean data sets to users"; exploración, preparación, transformación y documentación, con control de versiones y CI/CD; "spends their time transforming, testing, deploying, and documenting data". El texto admite que las fronteras son borrosas y que a veces hace trabajo de analista. Hay conflicto de intereses: dbt Labs vende la herramienta de la que nace el rol.
- Historia del rol según dbt Labs: antes de 2012 se contrataba primero un ingeniero de datos; después de 2012 los warehouses en la nube, servicios de pipelines gestionados y BI de autoservicio facilitaron cargar y reportar, y llegaron números en conflicto; "This is when dbt entered the market"; "Starting in 2018, the author and the Locally Optimistic community 'started calling this role the analytics engineer.'" (https://www.getdbt.com/blog/what-is-analytics-engineering).
- Data scientist (BLS, primaria): "Data scientists use analytical tools and techniques to extract meaningful insights from data"; identifican datos útiles, los limpian, construyen y prueban algoritmos y modelos de machine learning, visualizan y recomiendan acciones. Mediana 2025: $120.230 por año; 275.600 empleos (2025); crecimiento proyectado 2025-35: 35%; educación típica: bachelor's en matemática, estadística, computación o afín (https://www.bls.gov/ooh/math/data-scientists.htm). Es dato de EE.UU., no de Argentina.
- BI/Power BI data analyst (Microsoft PL-300): "deliver actionable insights by working with available data and applying domain expertise"; trabaja con interesados de negocio y "collaborate with analytics engineers and data engineers to identify and acquire data"; usa Power BI para preparar, modelar, visualizar y analizar, y gestionar y asegurar; debe dominar Power Query y DAX (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300). Esta única frase de Microsoft ubica los cuatro roles (analista BI, analytics engineer, data engineer) en una sola cadena.
- Mercado argentino: Sysarmy 2026.1: 5.074 participantes y 4.939 respuestas analizadas; publicada el 6 de marzo de 2026 (https://sysarmy.com/blog/posts/resultados-de-la-encuesta-de-sueldos-2026-1/). La página no desglosa roles de datos; remite al dataset abierto y al análisis de Openqube, que no pude leer. Cifras por rol que aparecieron en iProfesional (Data Engineer $1.297.652; BI/Data Analyst $1.219.920; Data Scientist $1.123.486) son de período y estadístico (promedio vs mediana) no identificados; no usarlas (https://www.iprofesional.com/management/378368-sueldo-de-los-profesionales-it-en-argentina-puestos-mejor-pagos) [S].
- Tramo que cubre cada rol (síntesis propia, apoyada en las citas de arriba): data engineer = generar/ingerir/almacenar; analytics engineer = transformar y modelar (hacia los datasets limpios); analista de datos y analista BI = servir (consultas, reportes, dashboards); data scientist = modelos y análisis avanzado sobre el dato servido. Las fuentes no dan un diagrama de tramos único: es construcción nuestra.

### Qué se pide aprender primero a un analista

- Google Data Analytics Certificate: planilla (Sheets/Excel) y SQL primero, luego visualización con Tableau, y Python recién en el curso 7 (ver sección 5; https://www.coursera.org/professional-certificates/google-data-analytics).
- PL-300 exige Power Query y DAX (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300).
- BLS pide estadística, computación y programación orientada a datos para data scientists (https://www.bls.gov/ooh/math/data-scientists.htm).
- Lo pedido en búsquedas laborales (avisos) no se investigó: hueco.

### Recurso canónico

Para el vocabulario de roles: el study guide de PL-300 (audiencia, qué hace el analista y con quién colabora) y la página de BLS para data scientist; la nota de dbt Labs solo para analytics engineer, avisando que es proveedor.

---

## 3. Historia breve

### Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| DATAVERSITY, "A Short History of Data Warehousing" | https://www.dataversity.net/a-short-history-of-data-warehousing/ | secundaria | 2/2/1/2 | [L] |
| Kimball Group, ficha de The Data Warehouse Toolkit | https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/ | primaria | 3/1/1/3 | [L] |
| dbt Labs, "What is analytics engineering" | https://www.getdbt.com/blog/what-is-analytics-engineering | proveedor | 2/2/1/2 | [L] |
| dbt Labs, "Four years in" (julio 2020) | https://www.getdbt.com/blog/four-years-in-from-misfits-to-mainstream | proveedor | 2/1/1/2 | [L] |
| Gupta et al., Amazon Redshift (paper, CMU) | https://www.cs.cmu.edu/~15721-f24/papers/Redshift.pdf | primaria | 3/2/1/3 | [S] (el PDF no se pudo leer; dato vía buscador) |
| First Round Review / Contrary Research (fundación de dbt) | https://review.firstround.com/dbt-labs-path-to-product-market-fit/ | secundaria | 2/2/1/1 | [S] |

### Afirmaciones con fecha

- Años 70: Bill Inmon empezó a hablar de principios de data warehouse y acuñó el término; 1986: se fundó Red Brick Systems (Kimball); 1988: un artículo del IBM Systems Journal introdujo "business data warehouse"; 1992: Inmon publicó Building the Data Warehouse y Kimball dejó Red Brick; 1996: Kimball publicó por primera vez The Data Warehouse Toolkit; fines de los 90: Inmon desarrolló la Corporate Information Factory (https://www.dataversity.net/a-short-history-of-data-warehousing/). Una sola fuente secundaria para esta cronología; el 1992 y el 1996 coinciden con lo que devolvió el buscador sobre los dos libros.
- La necesidad de soporte a decisiones es anterior al modelo relacional y a SQL (mismo artículo). No hay fecha de "sistemas de soporte a decisiones" ni de la etiqueta "BI" en lo leído: hueco.
- Definición clásica de Inmon: "a subject oriented, integrated, non volatile, time variant collection of data for management's decision making" (resumen de buscador sobre el libro, https://www.oreilly.com/library/view/building-the-data/9780764599446/ch01.html) [S]. Citar el texto del libro, no esta paráfrasis.
- Inmon top-down y centralizado; Kimball bottom-up y dimensional (resultado del buscador, [S]; varias secundarias parafraseando lo mismo cuentan como una).
- Big data: paper de MapReduce de Jeffrey Dean y Sanjay Ghemawat, OSDI 2004 (buscador, [S]); Hadoop nació en 2006 como derivado del crawler Nutch (una fuente secundaria, [S]; la página de releases de Apache dio 404). Sin verificar.
- Nube y ELT: Amazon Redshift salió en febrero de 2013 según un paper de AWS (https://www.cs.cmu.edu/~15721-f24/papers/Redshift.pdf) [S]. dbt Labs dice que desde 2012 los warehouses en la nube cambiaron el panorama (https://www.getdbt.com/blog/what-is-analytics-engineering).
- dbt: fundada en 2016 como Fishtown Analytics (Tristan Handy, Drew Banin, Connor McArthur), renombrada dbt Labs en 2021 (https://review.firstround.com/dbt-labs-path-to-product-market-fit/ y secundarias, [S]); el post de dbt de julio 2020 habla de la comunidad "of 2016-2018" y de cuatro años de la empresa (https://www.getdbt.com/blog/four-years-in-from-misfits-to-mainstream). Término "analytics engineer" desde 2018 según dbt Labs (ver sección 2). Reporte de fusión dbt-Fivetran en octubre de 2025 de una nota del Inquirer: sin verificar, y fuera del alcance de la historia (por eso no se incluye).
- Discrepancia: un perfil dice que el newsletter de Handy empezó en 2015 y otra fuente que empezó a escribir en 2017-2018; no es dato necesario para la nota.
- Ralph Kimball y Margy Ross, The Data Warehouse Toolkit, 3rd Edition, Wiley, 2013 (https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/).

### Recurso canónico

Para la línea de tiempo, el artículo de DATAVERSITY (corto) como mapa y, para cada hito, el libro original. Hueco: no hay una fuente primaria única sobre "de DSS a BI a analytics engineering"; la nota debería armar la cronología con estas piezas y decir cuáles son sin verificar.

---

## 4. Fuentes de referencia por vertical (bibliografía canónica)

Verificadas en esta ronda (con URL):

| Vertical | Obra | Edición/año verificado | URL | Marca |
|---|---|---|---|---|
| Ingeniería de datos (Fundamentos) | Reis y Housley, Fundamentals of Data Engineering | O'Reilly, 2022 (junio según catálogo; 26 julio según el autor) | https://joereis.substack.com/p/the-data-engineering-lifecycle-and | [L] |
| Sistemas de datos | Kleppmann y Riccomini, Designing Data-Intensive Applications, 2.ª ed. | O'Reilly, 2026 (febrero según O'Reilly en línea; marzo 2026 según el blog del autor y varias librerías; discrepan) | https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html | [S] |
| Modelado de warehouse | Kimball y Ross, The Data Warehouse Toolkit, 3.ª ed. | Wiley, 2013 | https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/ | [L] |
| Modelado de warehouse | Inmon, Building the Data Warehouse | 1992 (primera edición) | https://www.dataversity.net/a-short-history-of-data-warehousing/ | [L] |
| Estadística | James, Witten, Hastie, Tibshirani: ISL con R 1.ª 2013, 2.ª 2021 (versión corregida jun 2023); ISL con Python 2023; PDFs gratuitos | | https://www.statlearning.com/ | [L] |
| Estadística | OpenIntro Statistics, 4.ª edición (por la nomenclatura "os4"; año sin confirmar), PDF gratuito | | https://www.openintro.org/book/os/ | [M] |
| Gestión de datos | DAMA-DMBOK2 (2017), revisión de mantenimiento 2024 | | https://dama.org/dama-dmbok-revision/ | [L] |
| Análisis | Programa Google Data Analytics (Coursera) | ver sección 5 | https://www.coursera.org/professional-certificates/google-data-analytics | [L] |
| Análisis BI | Microsoft PL-300 study guide | habilidades al 2026-04-20 | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300 | [L] |
| Marco de roles | BLS OOH Data Scientists | 2026-08-27 | https://www.bls.gov/ooh/math/data-scientists.htm | [L] |

Del mapa de fuentes del brief, NO verificadas por mí en esta ronda (declarar como hueco): Linstedt (Data Vault), CRISP-DM 1.0 (2000), NIST/SEMATECH e-Handbook, declaración ASA sobre p-valores (2016), Kohavi/Tang/Xu (2020), Cleveland y McGill (1984), Tufte, Few, Knaflic, Munzner. Corresponden a otros ángulos del plan; no las cito con año.

---

## 5. Ruta de aprendizaje de Data Analytics

### Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| Coursera, Google Data Analytics Professional Certificate | https://www.coursera.org/professional-certificates/google-data-analytics | primaria (proveedor del curso) | 2/3/2/3 | [L] |
| Microsoft, study guide PL-300 | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300 | primaria | 3/3/2/3 | [L] |

### Afirmaciones

- Orden del Google DA (página de Coursera, sin fecha de actualización: dice "Recently updated"): 1 Foundations: Data, Data, Everywhere (13 h); 2 Ask Questions to Make Data-Driven Decisions (15 h); 3 Prepare Data for Exploration (19 h); 4 Process Data from Dirty to Clean (16 h); 5 Analyze Data to Answer Questions (25 h); 6 Share Data Through the Art of Visualization (19 h); 7 Introduction to Data Analysis Using Python (27 h); 8 Google Data Analytics Capstone: Complete a Case Study (11 h); 9 Accelerate Your Job Search with AI (6 h). Nivel principiante, sin título ni experiencia previa. Ritmo: 6 meses a 10 horas por semana (https://www.coursera.org/professional-certificates/google-data-analytics).
- Discrepancias dentro de la misma página: las horas por curso suman 151 y la página dice "over 180 hours"; la lista de herramientas incluye R, ggplot2 y Rmarkdown pero el FAQ dice que R no está en el currículo; y una versión previa vista en el buscador mostraba 8 cursos con R y Tableau. Por eso el programa cambió: el curso 7 actual usa Python (el mapeo de herramientas por curso lo infirió el extractor de las listas de habilidades, no lo dice la página).
- Herramientas por tramo: planilla en 1, 2, 4, 5; SQL en 3, 4, 5; Tableau en 6; Python (Pandas, NumPy) en 7.
- Ejercicios típicos: el programa cierra con un caso (capstone, curso 8). Qué datasets abiertos usa no se pudo confirmar en lo leído: hueco.
- PL-300 (Microsoft), pesos del examen según habilidades medidas al 20 de abril de 2026: Prepare the data 25-30%; Model the data 25-30%; Visualize and analyze the data 25-30%; Manage and secure Power BI 15-20%. Incluye crear tablas de hechos y de dimensiones, relaciones, funciones DAX (CALCULATE, time intelligence) y seguridad por filas (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300). Modificación 2026-11-05 (metadato de la página). Nótese que el examen incluye Copilot desde 2026.
- Orden pedagógico que se deduce (inferencia nuestra): preguntar bien y ubicar el dato, preparar y limpiar, analizar con SQL/planilla, visualizar y contar, recién después programación. Ambos programas dedican un tercio o más a preparar/limpiar.
- Otros programas (IBM, Dataquest, Coderhouse, etc.) no se investigaron: hueco.

### Recurso canónico

Google DA, cursos 2 a 6 como secuencia (qué orden da el campo a quien llega de planillas) y PL-300 como lista de habilidades verificables con peso. Fijarse en el reparto de tiempo: casi la mitad va a preparar y limpiar datos.

---

## Puntos de contacto con otros temas de la base

- Analítica-de-producto toca North Star, activación y experimento A/B (Producto) y incrementalidad y economía unitaria (Marketing): en este ángulo solo hay que decir que el rol que mide producto cae en el tramo "servir" y que la calidad del dato (gobierno) es previa a cualquier cohorte o experimento. No se investigó más.

## Huecos

1. Lista de las áreas del DMBOK2 contra el libro: DAMA dice 11 en su artículo y 14 diagramas en su página; solo una secundaria da las 11 por nombre.
2. Cómo se relacionan Reis y Housley con DAMA: ninguna fuente leída los compara; la relación de esta nota es inferencia propia.
3. Mercado argentino: Sysarmy 2026.1 no mostró roles ni sueldos de datos en la página de resultados; falta leer el dataset o el informe de Openqube. Las cifras de iProfesional son de período dudoso.
4. IBM como fuente de roles: no leída (la URL era un índice). Faltan avisos de trabajo reales para saber qué se pide primero.
5. Historia: sin fuente primaria para soporte a decisiones, la etiqueta BI y Hadoop 2006 (la página de releases dio 404); Redshift 2013 y MapReduce 2004 solo por buscador.
6. Bibliografía no verificada: Linstedt, CRISP-DM, NIST, ASA, Kohavi, Cleveland-McGill, Tufte, Few, Knaflic, Munzner; año de OpenIntro 4.ª; fecha exacta de Kleppmann 2.ª (febrero vs. marzo 2026).
7. Ejercicios y datasets abiertos típicos de los programas: no confirmados.
8. El cap. 2 de Reis y Housley no se pudo abrir (403): la lista de etapas y undercurrents está confirmada por el propio autor (2026) pero no por el texto del libro.
