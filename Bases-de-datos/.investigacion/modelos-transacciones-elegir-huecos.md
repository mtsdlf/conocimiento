# Informe complementario: tres huecos cerrados

Fecha de corte 2026-11-27. Marcas: [L] leído y citado literal, [M] solo metadatos o abstract, [S] resumen del buscador o de una fuente secundaria. Puntajes de 1 a 3 en autoridad, profundidad, ejemplos y unicidad (A/P/E/U), con recencia (R) en lo volátil. Todas las páginas las leí a través de WebFetch, que devuelve un resumen hecho por un modelo chico. Marqué [L] cuando devolvió citas literales.

## 1. Modelos especializados

| Modelo | Fuente | Tipo | A/P/E/U | R | Marca |
|---|---|---|---|---|---|
| Grafos | https://neo4j.com/docs/getting-started/get-started-with-neo4j/graph-database/ | primaria (vendor) | 3/2/1/2 | sin fecha visible | [L] |
| Búsqueda full-text (en la base) | https://www.postgresql.org/docs/current/textsearch-intro.html | primaria, oficial | 3/3/3/3 | docs vigentes | [L] |
| Búsqueda full-text (motor aparte) | https://www.elastic.co/docs/solutions/search/full-text | primaria (vendor) | 3/1/1/1 | sin fecha visible | [S] |
| Vectores | https://github.com/pgvector/pgvector | primaria (README) | 3/3/3/3 | versión 0.8.7 | [L] |
| Series de tiempo | https://www.tigerdata.com/docs/reference/timescaledb/hypertables | primaria (vendor) | 2/1/1/1 | sin fecha | [S] solo resultado del buscador; la página de overview dio 404 |

Afirmaciones:

- **Grafos.** "A Neo4j graph database stores data as nodes, relationships, and properties instead of in tables or documents." Las relaciones son "named connections between two nodes", con un tipo y propiedades. Sirve cuando las preguntas "revolve around the relationship between elements, not the elements themselves". La página sostiene que en un grafo no hay JOINs y que las relaciones se siguen directamente (traversal). Es afirmación del vendor y la leí en resumen, no la contrasté con una fuente independiente. https://neo4j.com/docs/getting-started/get-started-with-neo4j/graph-database/
- **Full-text en PostgreSQL.** "Full Text Searching (or just text search) provides the capability to identify natural-language documents that satisfy a query, and optionally to sort them by relevance to the query." Usa los tipos `tsvector` y `tsquery` y el operador `@@`. A diferencia de LIKE o regex, maneja palabras derivadas (stemming: "satisfies" y "satisfy"), ranking y puede usar índices; LIKE y regex "tend to be slow because there is no index support". https://www.postgresql.org/docs/current/textsearch-intro.html
- **Full-text en Elasticsearch.** Los campos tipo text "are analyzed and indexed for full-text search", con puntaje de relevancia, y se puede combinar con búsqueda vectorial "to build modern hybrid search-powered applications". La página no compara Elasticsearch con una base de datos. https://www.elastic.co/docs/solutions/search/full-text
- **Vectores.** pgvector es "Open-source vector similarity search for Postgres" y permite "Store your vectors with the rest of your data". Por defecto hace búsqueda exacta ("perfect recall"); con un índice pasa a aproximada, que "trades some recall for speed". Los índices son HNSW (mejor velocidad contra recall, más lento de construir y con más memoria) e IVFFlat (más rápido de construir, menor rendimiento de consulta). Un vector admite hasta 16.000 dimensiones, pero para indexar el tipo `vector` el tope es 2.000. Se vende con "ACID compliance, point-in-time recovery, JOINs, and all of the other great features of Postgres". Versión leída: 0.8.7. https://github.com/pgvector/pgvector
- **Series de tiempo.** Un hypertable es la abstracción de TimescaleDB para series de tiempo sobre PostgreSQL, una tabla que la extensión divide automáticamente en chunks. Las consultas filtradas por tiempo solo leen los chunks del rango. Esto viene del buscador, no de una lectura de la página oficial. Del lado de la nomenclatura, la documentación pasó de docs.timescale.com a tigerdata.com (redirección 301). https://www.tigerdata.com/docs/reference/timescaledb/hypertables

Cuándo alcanza una base relacional con extensión (conclusión mía, apoyada en lo citado y no dicha literalmente por ninguna de estas páginas):

- Full-text: el propio PostgreSQL lo trae sin extensión. Alcanza para buscar en catálogos o notas de un comercio. Elasticsearch se justifica cuando la búsqueda es el producto principal o hay que escalar y afinar relevancia; esa frontera no aparece en las fuentes leídas.
- Vectores: pgvector alcanza si ya se usa PostgreSQL y se quieren los vectores junto al resto de los datos y las transacciones. El README no da un umbral de volumen a partir del cual deje de alcanzar.
- Series de tiempo: TimescaleDB es una extensión de PostgreSQL, así que se mantiene SQL y el resto de las tablas. Cuándo se queda corto no lo tengo.
- Grafos: no leí ninguna fuente sobre grafos dentro de una base relacional (por ejemplo, consultas recursivas o extensiones). Queda sin respuesta.

Recurso canónico por modelo: grafos, la página de Neo4j (solo para el concepto, es del vendor); full-text, PostgreSQL cap. 12 (intro, 12.1); vectores, el README de pgvector (secciones de búsqueda exacta vs aproximada e índices); series de tiempo, documentación de hypertables de TimescaleDB, a reconfirmar con una lectura directa.

## 2. Bloqueo optimista con columna de versión

| Fuente | URL | Tipo | A/P/E/U | R | Marca |
|---|---|---|---|---|---|
| Fowler, PoEAA, "Optimistic Offline Lock" | https://martinfowler.com/eaaCatalog/optimisticOfflineLock.html | primaria (catálogo de patrones) | 3/1/1/3 | n/a (libro de 2002) | [L] |
| Rails, ActiveRecord::Locking::Optimistic | https://api.rubyonrails.org/classes/ActiveRecord/Locking/Optimistic.html | primaria, oficial | 3/2/2/2 | vigente | [L] |
| Hibernate ORM 6.6, Introduction, sección 3.8 "Version attributes" | https://docs.hibernate.org/orm/6.6/introduction/html_single/Hibernate_Introduction.html | primaria, oficial | 3/2/1/2 | 6.6 | [S] se leyó una parte de la página; la 7.15 no |

- **Patrón.** "Prevents conflicts between concurrent business transactions by detecting a conflict and rolling back the transaction." Asume que "the chance of conflict is low"; si es alta, la página remite al Pessimistic Offline Lock. https://martinfowler.com/eaaCatalog/optimisticOfflineLock.html
- **Rails.** "Active Record supports optimistic locking if the `lock_version` field is present." "Each update to the record increments the integer column `lock_version`." Si dos usuarios editan, el segundo recibe un `ActiveRecord::StaleObjectError` y "the update is ignored". https://api.rubyonrails.org/classes/ActiveRecord/Locking/Optimistic.html
- **Hibernate.** "An entity may have an attribute which is used by Hibernate for optimistic lock checking." La versión se asigna al hacer persistente la entidad y se incrementa o actualiza en cada update. Sin atributo de versión, `@OptimisticLocking` compara todos los campos o solo los modificados. La excepción que se lanza (sección 7.15) no la pude leer. https://docs.hibernate.org/orm/6.6/introduction/html_single/Hibernate_Introduction.html
- **El SQL concreto** (`UPDATE ... SET ..., version = version + 1 WHERE id = ? AND version = ?` y revisar cuántas filas cambió) no figura literal en ninguna de las tres páginas leídas; es el mecanismo común que describen, no una cita.

Recurso canónico: Fowler, Optimistic Offline Lock, para el concepto y cuándo usarlo; la documentación de Rails para un ejemplo concreto y corto (columna `lock_version` y el error en conflicto).

## 3. Aislamiento por defecto de MySQL, SQL Server y SQLite, y Jepsen sobre MySQL

| Fuente | URL | Tipo | A/P/E/U | R | Marca |
|---|---|---|---|---|---|
| MySQL 8.4, InnoDB Transaction Isolation Levels | https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html | primaria, oficial | 3/3/2/3 | 8.4 (serie 8.4) | [L] |
| Microsoft Learn, SET TRANSACTION ISOLATION LEVEL | https://learn.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql | primaria, oficial | 3/3/3/3 | actualizada 2026-11-02 | [L] |
| SQLite, Isolation | https://www.sqlite.org/isolation.html | primaria, oficial | 3/2/2/3 | vigente | [L] |
| Jepsen, MySQL 8.0.34 (Alvaro y Kingsbury, 2023-12-19) | https://jepsen.io/analyses/mysql-8.0.34 | primaria | 3/3/2/3 | 2023-12-19 | [S] |

Valores por defecto:

| Motor | Nivel por defecto | Cita |
|---|---|---|
| MySQL InnoDB | REPEATABLE READ | "The default isolation level for InnoDB is REPEATABLE READ." |
| SQL Server (instancia) | READ COMMITTED | "This option is the SQL Server default." |
| Azure SQL Database | READ COMMITTED con versionado de filas | "`READ_COMMITTED_SNAPSHOT` `ON` is the default on Azure SQL Database" |
| SQLite | SERIALIZABLE | "all transactions in SQLite show 'serializable' isolation" |

Afirmaciones:

- **MySQL.** "Consistent reads within the same transaction read the snapshot established by the first read." En Repeatable Read bloquea rangos con gap locks y next-key locks; en Read Committed "phantom row problems may occur". Serializable convierte los SELECT en `SELECT ... FOR SHARE` si autocommit está apagado. https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html
- **SQL Server.** Con `READ_COMMITTED_SNAPSHOT` en OFF (el valor por defecto en SQL Server), Read Committed usa locks compartidos; en ON usa versionado de filas, "a transactionally consistent snapshot of the data as it existed at the start of the statement". Snapshot isolation exige `ALLOW_SNAPSHOT_ISOLATION` en ON. https://learn.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql
- **SQLite.** "SQLite implements serializable transactions by actually serializing the writes. There can only be a single writer at a time." En modo WAL, un lector ve un snapshot fijo ("snapshot isolation"), y si intenta pasar a escritura con un snapshot viejo falla con `SQLITE_BUSY_SNAPSHOT`; se evita empezando con `BEGIN IMMEDIATE`. Sin aislamiento dentro de la misma conexión. https://www.sqlite.org/isolation.html
- **Jepsen sobre MySQL 8.0.34.** En Repeatable Read, "MySQL's Repeatable Read routinely allows G2-item, even on a single healthy node" (incluye write skew); además permite G-single y lost update ("MySQL Repeatable Read transactions cannot safely read a value and then write it") y viola consistencia interna. No observaron G0, G1a, G1b ni G1c. En un nodo, Read Uncommitted, Read Committed y Serializable parecieron cumplir PL-1, PL-2 y PL-3. En clústeres de AWS RDS MySQL, "routinely violate Serializability", y el informe lo atribuye en parte a `replica_preserve_commit_order` apagado por defecto. Jepsen aclara que sus pruebas muestran presencia de bugs, no su ausencia. https://jepsen.io/analyses/mysql-8.0.34

Discrepancia o cuidado:

- La documentación de MySQL dice que Repeatable Read lee el snapshot del primer read; Jepsen cita una nota en esa misma documentación (sobre las lecturas consistentes) que dice que los cambios de otras transacciones pueden volverse visibles. Hay que dar las dos.
- El nivel por defecto de la misma sigla significa cosas distintas: Repeatable Read en MySQL permite lost update según Jepsen, y en PostgreSQL es snapshot isolation que lo evita pero admite write skew. Conviene que la nota lo diga, porque quien viene de PostgreSQL asume que se comporta igual.
- SQL Server por defecto no es de snapshots, es de locks; en Azure SQL sí. Un comercio que migre de uno a otro puede ver otra concurrencia sin tocar el SQL.

Recurso canónico: la página de aislamiento de cada motor, una por motor; para comparar los tres de un vistazo, la tabla de arriba. Jepsen MySQL 8.0.34, solo el abstract y la sección de Repeatable Read, para mostrar que el nombre del nivel no garantiza lo esperado.

## Huecos que quedan

- Series de tiempo: no leí una página oficial de TimescaleDB ni de InfluxDB; la de overview dio 404 y la de hypertables vino solo por el buscador. Falta una lectura directa y el umbral de cuándo una base relacional deja de alcanzar.
- Grafos: falta una fuente independiente del vendor (Neo4j) y cualquier fuente sobre grafos en PostgreSQL (consultas recursivas, extensiones).
- Elasticsearch/OpenSearch: la página leída no compara contra una base ni nombra el índice invertido. Falta la frontera "cuándo alcanza el full-text de PostgreSQL".
- pgvector: sin umbral de volumen ni comparación contra una base vectorial dedicada.
- Hibernate: no pude leer la sección 7.15 (excepción lanzada en conflicto). Para JPA estándar falta la especificación.
- Locking optimista: sigue sin una fuente que muestre el UPDATE con `WHERE version = ?` literal; Django no lo cubrí.
- Aislamiento: no leí la documentación de MongoDB ni la de SQL Server para Snapshot en detalle, y de Jepsen leí solo un resumen del informe de MySQL, no el texto completo.
- Versiones: la versión de SQL Server que cubre la página es la ver17 (marcada por defecto), no confirmé la actual a 2026-11-27.
