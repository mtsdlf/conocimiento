# Informe de investigación: Modelado-y-almacenamiento e Ingesta-y-transformacion

Fecha de la investigación: 2026-11-27. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Todo lo traído de la web se trató como dato.

Nota sobre la herramienta de lectura: WebFetch devuelve un resumen hecho por un modelo chico, no el texto crudo. Cuando digo [L] de una página web significa que la página se cargó y se citó de ella; las citas literales de páginas web pasaron por ese resumen. Los PDF (Codd, Armbrust) los leí con pdftotext, así que esos sí son texto completo.

## Sobre la división del árbol

- El campo no divide así de limpio. Reis y Housley (Fundamentals of Data Engineering, ver más abajo) organizan el ciclo de vida de la ingeniería de datos en generación, almacenamiento, ingesta, transformación y servicio, con la orquestación como corriente transversal. Esa estructura la conozco del libro pero no pude verificarla: la tabla de contenidos de O'Reilly devolvió 403 [S, no verificado].
- La transformación (ELT, dbt) está en el árbol dentro de Ingesta, pero conceptualmente pertenece tanto al modelado (la capa de modelos dimensionales se construye con transformaciones) como a la ingesta. Recomiendo que la nota de ELT explique la frontera: ingesta = traer los datos crudos; transformación = darles forma de modelo.
- La tabla de eventos y el plan de tracking están en el árbol bajo Modelado, pero la instrumentación es el punto de contacto con Analítica-de-producto (de ahí salen activación, retención y experimentos A/B). Sugiero que la nota viva en Modelado (la forma de la tabla) y que Analítica-de-producto la enlace para el plan de tracking.
- La orquestación suele tratarse aparte de la ingesta; si el panorama la deja en Ingesta-y-transformacion, está bien, pero es un componente propio.

---

## 1. OLTP y OLAP, y por qué no se analiza sobre la base de la aplicación

| Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| Kleppmann, Designing Data-Intensive Applications, cap. 3 (1ª ed.) / cap. 4 (2ª ed.), sección "Transaction Processing versus Analytics" | https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/ch03.html | primaria (libro) | [S] (403 al leer directo; solo vi la estructura de secciones y resúmenes en el buscador) | 3/3/2/3 |
| Reseña de libro (Warne) y resumen de blog del capítulo | https://henrikwarne.com/2019/07/27/book-review-designing-data-intensive-applications/ | secundaria | [S] | 1/1/1/1 |

Afirmaciones:
- El libro separa los motores pensados para cargas transaccionales de los pensados para analítica; la sección se llama "Transaction Processing versus Analytics" y los temas siguientes son data warehousing, almacenamiento orientado a columnas, compresión y orden (confirmado por la estructura del capítulo en https://oreilly.com/library/view/designing-data-intensive-applications/9781098119058/ch04.html [S]).
- Según resúmenes secundarios, OLTP sirve a usuarios finales con transacciones chicas, y OLAP agrega valores de millones de registros; el warehouse es una copia de solo lectura de los datos transaccionales, que evita que las consultas analíticas interfieran con la producción (https://henrikwarne.com/2019/07/27/book-review-designing-data-intensive-applications/ [S]).

Recurso canónico: Kleppmann, DDIA, la sección "Transaction Processing versus Analytics" y "Column-Oriented Storage" (cap. 3 de la 1ª edición, cap. 4 de la 2ª). Fijarse en: por qué el patrón de acceso (pocas filas con todas las columnas vs muchas filas con pocas columnas) cambia el diseño del almacenamiento. Ojo: no pude leer el texto del libro; la definición literal de OLTP/OLAP queda por confirmar.

## 2. Modelo relacional: tablas, claves, normalización

| Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| Codd, "A Relational Model of Data for Large Shared Data Banks", Communications of the ACM 13(6), junio 1970, pp. 377-387 (copia en UPenn) | https://www.engineering.upenn.edu/~zives/03f/cis550/codd.pdf | primaria | [L] (PDF escaneado con capa de texto OCR; legible con pdftotext) | 3/3/2/3 |

Afirmaciones (todas de https://www.engineering.upenn.edu/~zives/03f/cis550/codd.pdf [L]):
- Abstract, inicio: "Future users of large data banks must be protected from having to know how the data is organized in the machine (the internal representation)." (reconstruido de la capa OCR, que está desordenada; el resto del abstract no lo verifiqué literal).
- Sección 1.4 "Normal form": "There is, in fact, a very simple elimination procedure, which we shall call normalization." Elimina los "dominios no simples" (relaciones anidadas dentro de otras).
- Define clave primaria: un dominio (o combinación de dominios) cuyos valores identifican de forma única cada fila de la relación: "Such a domain (or combination) is called a primary key." (ejemplo del paper: el número de pieza es clave primaria, el color no). El paper también define "foreign key" en su lista de conceptos (sección sobre redundancia y consistencia).
- Aclaración para la nota: la normalización de Codd 1970 es la primera forma normal; las formas 2ª y 3ª vienen en trabajos posteriores del mismo autor, que no verifiqué acá.

Recurso canónico: Codd 1970, secciones 1.3 (claves) y 1.4 (forma normal). Fijarse en la figura 3, que muestra una colección de relaciones anidadas antes y después de normalizar: es el mejor ejemplo para quien viene de la planilla. Aviso: es un paper académico denso; la nota debería traducirlo con una tabla de clientes y pedidos, no citarlo como lectura.

## 3. Modelado dimensional (Kimball), Inmon y Data Vault

| Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| Kimball Group, Dimensional Modeling Techniques (índice) | https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/ | primaria | [L] (solo títulos) | 3/1/1/2 |
| Kimball, Grain | http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/ | primaria | [L] | 3/2/1/3 |
| Kimball, Fact table structure | https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/fact-table-structure | primaria | [L] | 3/2/1/3 |
| Kimball, Star schemas and OLAP cubes | http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/star-schema-olap-cube/ | primaria | [L] | 3/1/1/2 |
| Kimball, Type 2: Add new row | http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-2 | primaria | [L] | 3/2/1/3 |
| Kimball Group, "Differences of Opinion" (2004) | https://www.kimballgroup.com/2004/03/differences-of-opinion/ | primaria (de una parte interesada) | [L] | 2/2/1/3 |
| Kimball y Ross, The Data Warehouse Toolkit, 3ª ed. | (libro; citado por la página de técnicas de Kimball) | primaria | [S] no leído | 3/3/3/3 |
| Databricks glossary, Data Vault | https://www.databricks.com/glossary/data-vault | secundaria, de proveedor | [L] | 1/1/1/1 |
| Linstedt y Olschimke, Building a Scalable Data Warehouse with Data Vault 2.0 (Elsevier) | https://shop.elsevier.com/books/building-a-scalable-data-warehouse-with-data-vault-20/linstedt/978-0-12-802510-9 | primaria (libro) | [S] (solo catálogo vía buscador) | 3/3/3/3 |

Afirmaciones:
- Grano: "Declaring the grain is the pivotal step in a dimensional design. The grain establishes exactly what a single fact table row represents." Además: "The grain declaration becomes a binding contract on the design", "The grain must be declared before choosing dimensions or facts" y "different grains must not be mixed in the same fact table." (http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/)
- Hechos: "A fact table contains the numeric measures produced by an operational measurement event in the real world." y "In addition to numeric measures, a fact table always contains foreign keys for each of its associated dimensions." (https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/fact-table-structure)
- Estrella: "Star schemas characteristically consist of fact tables linked to associated dimension tables"; el modelo dimensional divide los datos en medidas o en el contexto descriptivo "who, what, where, when, why, and how". (http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/star-schema-olap-cube/). La página de dimensiones no la pude leer; la definición literal de "dimension table" queda como hueco.
- Dimensiones lentamente cambiantes: tipos 0 "Retain original", 1 "Overwrite", 2 "Add new row", 3 "Add new attribute" (títulos, en el índice de Kimball). Tipo 2: "Slowly changing dimension type 2 changes add a new row in the dimension with the updated attribute values."; se asigna "a new primary surrogate key" que las tablas de hechos usan "from the moment of the update". (http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-2)
- Kimball vs la fábrica de información corporativa (CIF, la escuela de Inmon): la CIF carga "a third normal form (3NF) relational database containing atomic data"; Kimball sostiene "The Kimball approach says atomic data must be dimensionally structured", y "Conformed dimensions are the backbone of any enterprise approach"; los modelos se arman por proceso de negocio, no por área. (https://www.kimballgroup.com/2004/03/differences-of-opinion/). Ojo: es Kimball describiendo a su rival; el artículo no nombra a Inmon. Falta una fuente de Inmon que se describa a sí mismo.
- Data Vault: "A data vault is a data modeling design pattern used to build a data warehouse for enterprise-scale analytics"; hubs "represent core business concepts", links "represent relationships between hubs", satellites "store information about hubs and relationships between them." (https://www.databricks.com/glossary/data-vault). Que Dan Linstedt lo inventó y que la obra de referencia es el libro con Olschimke: catálogo de Elsevier, vía buscador [S]. Los satélites guardan historia con inserciones, no con actualizaciones; los links son de solo agregado (fuente secundaria vía buscador [S], no atribuida a una URL específica).

Recurso canónico: para dimensional, Kimball y Ross, The Data Warehouse Toolkit, cap. 1 (técnicas básicas: grano, hechos, dimensiones) y cap. 2 (SCD); alternativa gratuita, las páginas de técnicas del sitio de Kimball Group. Fijarse en el orden de decisiones: proceso de negocio, grano, dimensiones, hechos. Para Inmon, ningún texto primario leído (ver huecos). Para Data Vault, el libro de Linstedt y Olschimke, caps. 3-4.

## 4. Almacenes analíticos: data warehouse, data lake, lakehouse, columnar

| Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| Armbrust, Ghodsi, Xin, Zaharia, "Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics", CIDR 2021 | https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf | primaria (de autores de Databricks; tienen interés comercial) | [L] | 3/3/2/3 |
| Dixon, "Pentaho, Hadoop, and Data Lakes", blog, 14 octubre 2010 | https://jamesdixon.wordpress.com/2010/10/14/pentaho-hadoop-and-data-lakes/ | primaria (origen del término) | [L] | 3/1/2/3 |
| Fowler, bliki "DataLake" | https://martinfowler.com/bliki/DataLake.html | secundaria de autoridad | [L] | 3/1/1/2 |
| Definición de Inmon vía arXiv 1307.3448 (artículo sobre warehouse de salud) | https://arxiv.org/pdf/1307.3448 | secundaria | [S] | 1/1/1/1 |
| Springer, Encyclopedia of Database Systems (entrada de data warehouse) | https://link.springer.com/referenceworkentry/10.1007/978-1-4614-8265-9_121 | secundaria | [S] (acceso bloqueado, solo el buscador) | 2/1/1/1 |
| Stonebraker et al., "C-Store: A Column-oriented DBMS", VLDB 2005, pp. 553-564 | https://dblp.org/rec/conf/vldb/StonebrakerABCCFLLMOORTZ05.html (cita) | primaria | [M] (solo metadatos y extractos del buscador) | 3/2/1/3 |
| Google Cloud, Introducción a BigQuery | https://docs.cloud.google.com/bigquery/docs/introduction | primaria (documentación de producto) | [L] | 2/1/1/1 |

Afirmaciones:
- Data warehouse (Inmon). La definición circula en dos redacciones, y las dos coinciden en el contenido: "a data warehouse is a subject-oriented, integrated, nonvolatile, and time-variant collection of data in support of management's decisions" (Springer, vía buscador) y la misma con otro orden y "decision" en singular (arXiv). Fuentes: https://link.springer.com/referenceworkentry/10.1007/978-1-4614-8265-9_121 y https://arxiv.org/pdf/1307.3448 [S ambas]. Ninguna es el texto de Inmon (Building the Data Warehouse, 1992), así que la cita literal "de Inmon" no está verificada; hay que decir "atribuida a Inmon". Significado de los cuatro atributos (arXiv): orientado a temas = datos de un tema juntos; integrado = se resuelven conflictos de nombres y unidades; variante en el tiempo = registros con marca de tiempo, vistas actuales e históricas; no volátil = lo cargado no se modifica ni se borra.
- Data lake, origen: Dixon, 14 de octubre de 2010: "If you think of a datamart as a store of bottled water – cleansed and packaged and structured for easy consumption –" "the data lake is a large body of water in a more natural state." (https://jamesdixon.wordpress.com/2010/10/14/pentaho-hadoop-and-data-lakes/). Una pieza de TechRepublic ubica el término en 2008; la mayoría de las fuentes dice 2010, y la página original lo fecha en 2010 (dos fuentes discrepan; da las dos, la de 2010 está mejor respaldada).
- Data lake, definición y crítica: "The idea is to have a single store for all of the raw data that anyone in an organization might need to analyze."; la crítica de que es "a dumping ground for data of widely varying quality, better named a data swamp"; Fowler la llama "both valid and irrelevant". Fowler también anota que Dixon pensaba el lago para una sola fuente, y que varias formarían un "water garden". (https://martinfowler.com/bliki/DataLake.html)
- Lakehouse, definición literal del paper: "We define a Lakehouse as a data management system based on low-cost and directly-accessible storage that also provides traditional analytical DBMS management and performance features such as ACID transactions, data versioning, auditing, indexing, caching, and query optimization. Lakehouses thus combine the key benefits of data lakes and data warehouses: low-cost storage in an open format accessible by a variety of systems from the former, and powerful management and optimization features from the latter." Abstract: el paper sostiene que la arquitectura de warehouse "will wither in the coming years and be replaced by a new architectural pattern, the Lakehouse". Es una tesis de los autores (Databricks), no un consenso; los resultados de rendimiento son del propio sistema. (https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)
- Almacenamiento columnar: BigQuery guarda "data ... in columns rather than rows" y lo describe como "optimized for analytical queries"; almacenamiento y cómputo son capas independientes (https://docs.cloud.google.com/bigquery/docs/introduction). C-Store: "a DBMS need only read the values of columns required for processing a given query, and can avoid bringing into memory irrelevant attributes" (cita del buscador, [S], https://dblp.org/rec/conf/vldb/StonebrakerABCCFLLMOORTZ05.html no contiene el texto).

Recurso canónico: warehouse, lago y lakehouse: la introducción y la sección 2 del paper de Armbrust et al. (la historia de la primera y segunda generación y la definición); leerlo sabiendo que es un paper de venta de una arquitectura. Para el lago: la entrada de Dixon (corta) más Fowler para la crítica. Para columnar: el capítulo de almacenamiento de Kleppmann.

## 5. Tabla de eventos y plan de tracking

| Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| Segment, Spec: Track | https://segment.com/docs/connections/spec/track/ | primaria (documentación de proveedor) | no leída (403) | n/c |
| Google, GA4: "Events" | https://support.google.com/analytics/answer/9322688 | primaria | [L] | 3/1/1/2 |
| Google, GA4: límites de recolección y configuración | https://support.google.com/analytics/answer/9267744 | primaria | [L] | 3/2/1/3 |
| Amplitude, plan de implementación | https://amplitude.com/docs/get-started/plan-your-implementation | primaria (proveedor) | [L] | 2/1/1/2 |

Afirmaciones:
- GA4: "An event allows you to measure a specific interaction or occurrence on your website or app."; límite de "16 KB" por envío de datos de eventos; hasta "20 events" por lote; ignora eventos que llegan más de dos días después (https://support.google.com/analytics/answer/9322688).
- GA4, límites por evento: nombre de evento de "40 characters"; "25 event parameters" por evento; para flujos de app "500 per app user" nombres distintos de evento y para web "There is not limit on the number of distinctly named events" (https://support.google.com/analytics/answer/9267744). Son números volátiles: fecha de lectura 2026-11-27.
- Amplitude: "it's critical to create a tracking plan document that outlines what events and properties to track, why you're tracking them, and where they're tracked." y "A tracking plan should derive from the business outcomes you're trying to measure or improve." (https://amplitude.com/docs/get-started/plan-your-implementation). La página no define evento, propiedad de evento y propiedad de usuario.
- Segment (event, properties, userId): el modelo de la llamada Track está documentado en la spec de Segment, pero la página devolvió 403. El esquema (nombre del evento, propiedades, identificador de usuario o anónimo) es de conocimiento general mío, no verificado en esta tanda.

Recurso canónico: la spec de Track de Segment (la que más se cita como forma estándar de un evento) más la página de plan de implementación de Amplitude para el plan de tracking. Fijarse en: nombre del evento como verbo en pasado, propiedades como atributos del contexto, identificador de usuario estable. Nada de esto está confirmado en esta tanda, así que verificar la spec de Segment antes de escribir la nota.

## 6. Ficha: motores analíticos (precios al 2026-11-27)

| Motor | Modelo de precio / licencia | Dato | URL | Marca | Fiabilidad |
|---|---|---|---|---|---|
| BigQuery | por TiB escaneado (on-demand) o por slot-hora (ediciones); almacenamiento por GiB | las cifras no se pudieron verificar (la página oficial devolvió solo el título en 3 intentos); de memoria del modelo: ~6,25 USD/TiB, 1 TiB gratis al mes, ~0,02 USD/GiB-mes almacenamiento activo | https://cloud.google.com/bigquery/pricing | [S] no verificado | baja: tratar como hueco |
| Snowflake | créditos de cómputo + almacenamiento por TB; ediciones | Tabla 2(a) on demand, AWS US East (N. Virginia): Standard 2,00 USD, Enterprise 3,00 USD, Business Critical 4,00 USD, VPS 6,00 USD por crédito. Almacenamiento on demand AWS US East: 23,00 USD por TB/mes. Cargo por segundo con mínimo de 60 segundos; no cobra ingreso de datos. | https://snowflake.com/legal-files/CreditConsumptionTable.pdf ; https://docs.snowflake.com/en/user-guide/cost-understanding-overall | [L] (PDF leído con pdftotext) | alta; el PDF no mostró fecha de vigencia en mi búsqueda (la versión en EUR dice "Pricing Updated: January 5, 2026" por buscador [S]) |
| Redshift | Serverless por RPU-hora; provisionado por nodo-hora; almacenamiento gestionado por GB-mes | región US East (N. Virginia): 0,375 USD por RPU-hora; ra3.4xlarge 3,26 USD/h; almacenamiento 0,024 USD por GB-mes; prueba de 300 USD por 90 días en Serverless | https://aws.amazon.com/redshift/pricing/ | [L] | media-alta |
| Databricks | DBU (unidad normalizada de procesamiento), por segundo, más la infraestructura de la nube | "a normalized unit of processing power"; prueba de 14 días; las tarifas por DBU de Databricks SQL no cargaron (el precio mostraba "Loading...") | https://www.databricks.com/product/pricing y https://www.databricks.com/product/pricing/databricks-sql | [L] parcial | hueco: tarifa por DBU |
| DuckDB | gratis, licencia MIT | "fully open-source under the MIT license"; sistema de un solo nodo, "in-process" o línea de comandos; "tested on machines with 100+ CPU cores and terabytes of memory"; formato nativo "scales for multiple terabytes of data but this needs some planning" | https://duckdb.org/faq.html | [L] | alta |
| PostgreSQL como warehouse chico | gratis, "PostgreSQL License"; no se cobra el motor | la versión actual anunciada en la página es PostgreSQL 19, publicada el 19 de noviembre de 2026 | https://www.postgresql.org/about/ y https://www.postgresql.org/about/licence/ | [L] | alta para licencia y versión; ninguna fuente sobre cuándo se queda corto como warehouse (ver huecos) |
| ClickHouse | código Apache-2.0; en la nube (ClickHouse Cloud) por unidad de cómputo-hora más almacenamiento | AWS us-east-1: Basic 0,21811 USD, Scale 0,29846 USD, Enterprise 0,39030 USD por unidad de cómputo-hora (8 GiB RAM y 2 vCPU); almacenamiento 25,30 USD/TB/mes; prueba de 300 USD en créditos por 30 días sin tarjeta | https://clickhouse.com/pricing ; https://github.com/ClickHouse/ClickHouse | [L] | alta |

Notas:
- Los precios cambian por región y por fecha; todos están leídos el 2026-11-27 y son de lista, no de contrato.
- Snowflake: el PDF lista precios por región (por ejemplo, Standard en EU Dublín 2,60 USD, Tokio 2,85 USD). Para un comercio argentino la región relevante sería probablemente Sudamérica u otra; no la busqué.
- Descubrimiento, no citable como hecho: en un comercio chico, lo razonable es empezar con Postgres, DuckDB o una planilla antes que con un warehouse en la nube; es juicio mío, no una afirmación de fuente.

Recurso canónico: la página de precios de cada proveedor, siempre con fecha de lectura. Para Snowflake, el PDF "Service Consumption Table" es mejor que la página comercial.

## 7. Ingesta: por lotes, en flujo, CDC

| Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| Debezium, sitio oficial | https://debezium.io/ | primaria | [L] | 3/1/2/2 |
| Reis y Housley, Fundamentals of Data Engineering (O'Reilly, 2022), cap. "Ingestion" | https://oreilly.com/library/view/fundamentals-of-data/9781098108298 | primaria (libro) | [S] (403; solo la estructura del capítulo por el buscador) | 3/3/2/3 |
| Apache Flink, overview de conceptos | https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/overview/ | primaria | [L] | 2/1/1/1 |

Afirmaciones:
- CDC: Debezium es "an open source distributed platform for change data capture"; permite que las aplicaciones respondan a inserciones, actualizaciones y borrados que otras aplicaciones confirman en una base, sin cambiar las apps que escriben. Cada evento registra el tipo de operación, el estado de la fila antes y después, y metadatos de origen. Licencia Apache 2.0. Última versión estable al 2026-11-27: 3.7.1.Final (https://debezium.io/). El mecanismo, leer el registro de transacciones de la base, no quedó confirmado en lo que leí.
- Por lotes vs en flujo: la tabla de contenidos del libro de Reis y Housley, cap. 7 "Ingestion", tiene secciones "batch ingestion considerations" y "message and stream ingestion considerations", y "ETL versus ELT" (vía buscador, [S]). No encontré una definición literal de lote vs flujo: la página de Flink solo menciona "DataStream API (bounded/unbounded streams)" (https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/overview/). Hueco: definición con cita.

Recurso canónico: Reis y Housley, cap. 7 (batch vs streaming, CDC, push vs pull). Fijarse en las tensiones de cada diseño: latencia necesaria vs complejidad y costo. Para CDC, la página principal de Debezium y su documentación de arquitectura. No pude leer el libro.

## 8. ETL vs ELT

| Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| dbt Labs (Daniel Poppy), "Understanding ELT: Extract, Load, Transform", 6 sep 2023 | https://www.getdbt.com/blog/extract-load-transform | secundaria/proveedor (dbt vende la herramienta que defiende ELT) | [L] | 1/1/1/1 |
| O'Reilly, "Understanding ETL" (guía vía Databricks) | https://www.databricks.com/sites/default/files/2025-08/Understanding_ETL_Updated-edition.pdf | secundaria, de proveedor | [S] | 1/1/1/1 |

Afirmaciones:
- En ETL, "data is transformed before being loaded into the data warehouse"; en ELT, "raw data is loaded first and transformations are applied later". ELT ganó terreno con la nube porque dio almacenamiento y procesamiento a demanda, y permite "perform transformations at scale using the cloud's vast computational resources" (https://www.getdbt.com/blog/extract-load-transform; fuente de un proveedor con interés).
- ETL era el método más común hacia el warehouse relacional y ELT "has become popular, especially with data lakes" (extracto del buscador sobre una guía de O'Reilly, [S]; https://www.databricks.com/sites/default/files/2025-08/Understanding_ETL_Updated-edition.pdf).
- Las críticas a ELT no las encontré en fuentes con método: solo posiciones de proveedores. Ver huecos.

Recurso canónico: Reis y Housley, cap. 7, sección "ETL versus ELT" (no leída). Como alternativa abierta, el artículo de dbt, marcado como de proveedor.

## 9. Orquestación

| Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| Apache Airflow, documentación de DAGs (versión 3.4.0) | https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html | primaria | [L] | 3/2/2/2 |

Afirmaciones:
- "Dag" viene de "directed acyclic graph", pero el significado en Airflow "has grown beyond that literal data structure". Un Dag agrupa todo lo necesario para correr un workflow: calendario, tareas, dependencias entre tareas, callbacks y ajustes operativos. Las dependencias se declaran con `>>` y `<<`; por defecto una tarea corre solo si todas las anteriores tuvieron éxito, salvo que se cambien las reglas de disparo. Los reintentos se fijan en el Dag; ejemplo `default_args` con `{"retries": 2}`. (https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)

Recurso canónico: la página de DAGs de Airflow, el ejemplo de cuatro tareas A, B, C y D; fijarse en que el Dag no sabe qué pasa dentro de cada tarea. La definición matemática más corta no la verifiqué en un texto de teoría de grafos.

## 10. Ficha: herramientas de ingesta, transformación y orquestación (2026-11-27)

| Herramienta | Qué hace | Licencia | Precio publicado | URL | Marca |
|---|---|---|---|---|---|
| Airbyte | ingesta (ELT) | el repo muestra insignias MIT y ELv2 (Elastic License v2); la división plataforma/conectores no quedó confirmada | Open source gratis para autoalojar; Cloud Standard desde 20 USD/mes por 5 créditos (aprox. 1 GB de sincronización); Plus desde 189 USD/mes por 40 créditos; Pro y Enterprise Flex a cotización; prueba de 14 días con 400 créditos | https://airbyte.com/pricing ; https://github.com/airbytehq/airbyte | [L] |
| Fivetran | ingesta administrada | propietaria | planes Free, Standard, Enterprise, Business Critical; Free: 500.000 filas activas por mes (MAR) en conexiones; precio por MAR decreciente con el volumen; en Standard, 1 a 1 millón de MAR cuesta 5 USD de base; transformaciones 0,01 USD por ejecución de modelo entre 5.001 y 30.000 | https://www.fivetran.com/pricing | [L] |
| dbt | transformación en SQL dentro del warehouse | dbt Core (repo): Apache 2.0, con personalizaciones de la distribución bajo otra licencia de producto; la documentación dice que v2 es el motor en Rust "built on an open-source runtime" y que hay "dbt OSS" Apache 2.0; la relación exacta entre Core y las versiones nuevas no quedó clara | gratis de usar; capacidades de la plataforma requieren cuenta (gratis o paga) | https://docs.getdbt.com/docs/introduction ; https://github.com/dbt-labs/dbt-core | [L] |
| Airflow | orquestación | Apache-2.0 | gratis (autoalojado); versión 3.4.0 | https://github.com/apache/airflow | [L] |
| Dagster | orquestación centrada en activos de datos | Apache-2.0 ("Dagster is Apache 2.0 licensed") | Cloud: Solo 10 USD/mes, Starter 100 USD/mes, Pro a cotización; crédito 0,040 USD (Solo) y 0,035 USD (Starter) pay-as-you-go; prueba de 30 días | https://dagster.io/pricing ; https://github.com/dagster-io/dagster | [L] |
| Prefect | orquestación en Python | Apache-2.0 (repo) | Cloud: Hobby gratis (2 usuarios, 5 deployments); Starter 100 USD/mes; Team 100 USD por usuario por mes; Enterprise a cotización | https://www.prefect.io/pricing ; https://github.com/PrefectHQ/prefect | [L] |

Notas:
- La pregunta que mandaba el brief listaba un plan "Pro" de Prefect: la página no lo muestra, lista Hobby, Starter, Team y Enterprise.
- Airbyte: el "5 créditos por 1 GB" del plan Standard no cuadra con "400 créditos por 100 GB" de la prueba (la propia página lo señala); la medición exacta está en otra doc.
- Ninguna de estas es una comparación con método: son páginas de cada proveedor.

Recurso canónico: la página de precios y la de licencia de cada herramienta, fechada. Para orquestación, la documentación de Airflow como referencia del vocabulario.

---

## Huecos (lo que no encontré o no pude verificar)

1. BigQuery: precios literales (tres intentos, la página oficial solo devolvió el título). Las cifras que el lector de la página ofreció salen de memoria del modelo y no se citan como hecho.
2. Databricks SQL: tarifa por DBU (la tabla de precios no cargó).
3. Inmon: ninguna fuente primaria; la definición de data warehouse es "atribuida a Inmon" por dos fuentes secundarias con redacción levemente distinta. Hace falta "Building the Data Warehouse" o una entrevista del propio Inmon.
4. Linstedt: sin texto primario; solo un glosario de proveedor y el catálogo del libro.
5. Kleppmann y Reis y Housley: ambos libros dieron 403 en O'Reilly; no pude leer ningún texto literal de ellos. Definiciones de OLTP/OLAP, lote vs flujo, ETL vs ELT y orquestación como corriente transversal quedan sin cita literal de la fuente canónica. La estructura de capítulos vino del buscador.
6. Kimball: la definición literal de "dimension table" y los tipos 0, 1 y 3 de SCD (solo vi los títulos) quedan sin leer.
7. Segment (spec de Track): 403. El esquema de un evento (evento, propiedades, userId) no está verificado en esta tanda; GA4 y Amplitude solo cubren parte.
8. Codd: leí el PDF escaneado con capa OCR desordenada; la cita del abstract es reconstruida del texto OCR.
9. Críticas a ELT y a data lakes con método (estudios, incidentes): no las encontré en tres rondas; solo la crítica "data swamp" de Fowler. Tampoco hay fuente sobre cuándo Postgres deja de alcanzar como warehouse.
10. CDC: no confirmé en lo leído que se base en el registro de transacciones; solo la descripción general de Debezium. Falta una definición literal de lote vs streaming.
11. Airbyte: licencia exacta por componente (plataforma vs conectores) y dbt Core vs v2 (qué es qué) quedaron ambiguas en las fuentes leídas.
12. Precios de Snowflake: no ubiqué la fecha de vigencia del PDF de USD; los precios por región de Latinoamérica no se buscaron.
13. Puntos de contacto con otros temas (para las notas, sin investigar): el plan de tracking y la tabla de eventos alimentan activación y experimento A/B (Producto) y la medición de incrementalidad (Marketing); el grano del modelo dimensional y las dimensiones lentamente cambiantes se tocan con economía unitaria cuando el costo o el precio cambia en el tiempo.
