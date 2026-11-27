---
resumen: >-
  La bibliografía canónica del tema Datos, ordenada por vertical: qué obra leer para cada parte, qué
  edición se verificó y qué se cita solo por catálogo o resumen.
estado: vigente
estabilidad: semi
fuentes:
  - "Joe Reis, The Data Engineering Lifecycle and Undercurrents, 4 Years Later (2026): https://joereis.substack.com/p/the-data-engineering-lifecycle-and"
  - "Martin Kleppmann, Designing Data-Intensive Applications, 2nd edition (2026), según el resumen del buscador: https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html"
  - "Kimball Group, ficha de The Data Warehouse Toolkit, 3.ª ed.: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/"
  - "DAMA International, revisión 2024 del DAMA-DMBOK 2.0: https://dama.org/dama-dmbok-revision/"
  - "James, Witten, Hastie y Tibshirani, An Introduction to Statistical Learning: https://www.statlearning.com/"
  - "OpenIntro Statistics (solo la página del libro): https://www.openintro.org/book/os/"
  - "ASA, Statement on Statistical Significance and P-Values (2016): https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf"
  - "Kohavi, Tang y Xu, Trustworthy Online Controlled Experiments (solo el sitio y el índice): https://experimentguide.com/"
  - "Hernán y Robins, Causal Inference: What If (solo la página del libro): https://miguelhernan.org/whatifbook"
  - "Wickham, Tidy Data, Journal of Statistical Software 59(10), 2014: https://www.jstatsoft.org/article/view/v059i10"
  - "Wickham, Çetinkaya-Rundel y Grolemund, R for Data Science, 2.ª ed., cap. de EDA: https://r4ds.hadley.nz/EDA.html"
  - "IBM SPSS Modeler CRISP-DM Guide v17: https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/17.0FP1/en/ModelerCRISPDM.pdf"
  - "NIST/SEMATECH e-Handbook of Statistical Methods: https://www.itl.nist.gov/div898/handbook/"
  - "Few, Dashboard Confusion (2004), reimpresión: https://www.informationweek.com/government/dashboard-confusion-2"
  - "Financial Times, Visual Vocabulary: https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary"
  - "Coursera, Google Data Analytics Professional Certificate: https://www.coursera.org/professional-certificates/google-data-analytics"
  - "Microsoft, Study guide for Exam PL-300: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300"
  - "Datos/.investigacion/fundamentos.md, sección 4"
  - "Datos/.investigacion/analisis.md; Datos/.investigacion/estadistica.md; Datos/.investigacion/metricas-y-visualizacion.md; Datos/.investigacion/modelado-e-ingesta.md; Datos/.investigacion/posicion-contraria.md"
aliases: [bibliografía de datos, libros de datos, qué leer de datos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Bibliografía de datos

La bibliografía canónica del tema Datos, ordenada por vertical: qué obra leer para cada parte, qué
edición se verificó y qué se cita solo por catálogo o resumen.

Casi ningún libro del tema se leyó entero para escribir la base: las editoriales bloquearon la
lectura y muchas obras se conocen por su índice, su catálogo o un resumen. La columna «Verificado»
dice qué se pudo comprobar; lo demás queda marcado. Las notas de cada vertical dicen qué parte leer
y en qué fijarse.

## Cómo pesar lo que se lee sobre datos

Mucha de la literatura sobre datos la escriben quienes venden herramientas. El rol de analytics
engineer lo nombró dbt Labs, la arquitectura lakehouse la propusieron autores de la empresa que la
vende, y el argumento de que los datos de casi todos son chicos viene del cofundador de un motor para
datos chicos. Esas fuentes sirven, pero se citan diciendo quién habla. Las guías de certificación
(Google, Microsoft) son confiables para saber qué se pide, no para saber qué funciona. Para
estadística, los textos abiertos y las declaraciones de sociedades científicas pesan más que
cualquier blog.

## Todo el recorrido e ingeniería

| Obra | Verificado | Para qué |
|---|---|---|
| Reis y Housley, *Fundamentals of Data Engineering* | O'Reilly, 2022; el catálogo dice junio y el autor, 26 de julio | El ciclo de vida y los undercurrents, caps. 1 y 2; el texto no se pudo abrir |
| Kleppmann y Riccomini, *Designing Data-Intensive Applications*, 2.ª ed. | O'Reilly, 2026; febrero según O'Reilly, marzo según el blog del autor (por resumen) | Base de la aplicación contra base para analizar: cap. 3 de la 1.ª ed., cap. 4 de la 2.ª |
| DAMA International, *DAMA-DMBOK2* | 2017, con revisión de mantenimiento en 2024 sin cambios en las áreas | La rueda de funciones de gestión; ver [la discrepancia de áreas](fundamentos-de-datos.md#dos-marcos-que-dividen-el-campo) |

## Modelado y almacenamiento

| Obra | Verificado | Para qué |
|---|---|---|
| Kimball y Ross, *The Data Warehouse Toolkit*, 3.ª ed. | Wiley, 2013 | Modelado dimensional: grano, hechos, dimensiones (caps. 1 y 2); gratis, las páginas de técnicas de Kimball Group |
| Inmon, *Building the Data Warehouse* | 1.ª ed. de 1992, por una secundaria; la edición vigente no se verificó | La definición clásica del almacén corporativo |
| Linstedt y Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0* | Elsevier; solo el catálogo, año no verificado | Data Vault |
| Armbrust y otros, «Lakehouse», CIDR 2021 | paper leído | Almacén, lago y lakehouse; escrito por quienes venden la arquitectura |
| Codd, «A Relational Model of Data for Large Shared Data Banks» | Communications of the ACM 13(6), junio de 1970 | El modelo relacional, en su origen |

## Análisis

| Obra | Verificado | Para qué |
|---|---|---|
| Certificado Google Data Analytics (Coursera) | 9 cursos; la página no tiene fecha de actualización | El proceso de preguntar a actuar; cursos 2 a 6 |
| CRISP-DM 1.0 | leído por la guía de IBM v17; presentado en 1999 según Wikipedia, el PDF original se cita como de 2000 | El proceso de un proyecto de minería de datos |
| Wickham, «Tidy Data» | Journal of Statistical Software 59(10), 2014 | [Limpieza de datos](../Analisis/limpieza-de-datos.md): una variable, una columna (secs. 2 y 3) |
| Wickham, Çetinkaya-Rundel y Grolemund, *R for Data Science*, 2.ª ed. | libro abierto; cap. de EDA leído | [Análisis exploratorio](../Analisis/analisis-exploratorio.md) |
| NIST/SEMATECH e-Handbook | secciones 1.1 y 7.1.6 leídas, sin fecha en la página | EDA y valores atípicos |
| Tukey, *Exploratory Data Analysis* | Addison-Wesley, 1977; no leído | El texto fundacional; denso para empezar |
| Provost y Fawcett, *Data Science for Business* | O'Reilly, 2013; solo el índice | Pasar de un problema de negocio a una [pregunta de análisis](../Analisis/pregunta-de-analisis.md), cap. 2 |

## Estadística

| Obra | Verificado | Para qué |
|---|---|---|
| OpenIntro Statistics | PDF gratis; «4.ª ed.» por la sigla de la página, año sin confirmar | [Estadística descriptiva](../Estadistica/estadistica-descriptiva.md) (cap. 2) e inferencia (caps. 5 a 7) |
| James, Witten, Hastie y Tibshirani, *An Introduction to Statistical Learning* | con R: 1.ª ed. 2013, 2.ª 2021; con Python, 2023; PDFs gratis | El paso hacia modelos |
| ASA, declaración sobre p-valores, y Wasserstein y Lazar | The American Statistician 70(2), 129-133, 2016 | Qué no significa un p-valor; cuatro páginas, leídas |
| Hernán y Robins, *Causal Inference: What If* | Chapman & Hall/CRC, 2020, con versión web gratis; solo la página | [Correlación y causalidad](../Estadistica/correlacion-y-causalidad.md), parte 1 |
| Kohavi, Tang y Xu, *Trustworthy Online Controlled Experiments* | Cambridge UP, 2020; solo sitio e índice | [Significancia](../Estadistica/significancia.md) y el [experimento A/B](../../Producto/Medicion/experimento-ab.md); cap. 3 |
| Gelman y Carlin, «Beyond Power Calculations» | Perspectives on Psychological Science 9(6), 2014; por resumen | Por qué con poco tráfico los efectos salen exagerados |

## Visualización y BI

| Obra | Verificado | Para qué |
|---|---|---|
| Cleveland y McGill, «Graphical Perception» | JASA 79, 1984; solo resúmenes | El orden en que se leen posición, longitud, ángulo y área; [elegir un gráfico](../Visualizacion-y-BI/elegir-un-grafico.md) |
| Financial Times, *Visual Vocabulary* | póster abierto en GitHub | Elegir el gráfico por la relación que se muestra |
| Few, *Information Dashboard Design* y «Dashboard Confusion» | libro de 2006 por reseñas; artículo de 2004 en reimpresión | Qué es un [tablero](../Visualizacion-y-BI/tablero.md) |
| Knaflic, *Storytelling with Data* | Wiley, 2015; solo metadatos | [Contar con datos](../Visualizacion-y-BI/contar-con-datos.md), caps. 1 y 2 |
| Guía de la certificación PL-300 (Microsoft) | habilidades al 20 de abril de 2026 | La lista de lo que se le pide a un analista BI, con su peso |

## Roles

La guía de la certificación de Microsoft, la página de científicos de datos de la oficina de
estadísticas laborales de EE.UU. y dos notas de dbt Labs, que es proveedor. El detalle está en
[roles de datos](roles-de-datos.md).

## Lo que no se verificó

Recomendadas por el mapa de fuentes del tema y no verificadas en ninguna ronda: Tufte y Munzner
(visualización), Few, *Show Me the Numbers*, y la fecha de la edición vigente de Inmon. Tampoco se
leyó el texto de ningún libro de O'Reilly del tema. Hasta que se verifiquen, la base no las cita con
año ni con edición.
