# Informe de investigación: Bases de datos (tres verticales chicas)

Fecha de corte: 2026-11-27. Todo lo que traje de la web lo traté como dato.

Marcas: [L] leído completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Casi todo lo leí a través de WebFetch, que devuelve un resumen hecho por un modelo chico, y por eso puse [L] solo cuando la página entera se leyó y se citó literal. Los números de versión son los que mostró la página al momento de la lectura y conviene recontrolarlos antes de confirmar la nota.

Los puntajes van de 1 a 3 en autoridad, profundidad, ejemplos y unicidad (A/P/E/U), más recencia (R) en lo volátil.

## Sobre la división del árbol

La división en tres verticales (modelos de datos, transacciones, elegir una base) coincide con cómo el campo parte el tema. Kleppmann tiene Data Models (cap. 2) y Transactions (cap. 7) como capítulos separados. Dos cosas a tener en cuenta:

- Elegir una base no tiene un texto canónico propio. Es una síntesis de las otras dos verticales más la operación, y las fuentes que lo tratan son documentación oficial, DB-Engines (que mide popularidad) y opinión de practicantes. Conviene decirlo en la nota.
- La vertical de modelos especializados (grafos, series de tiempo, búsqueda full-text, vectores) quedó sin fuentes leídas. Es un hueco declarado más abajo.
- "Base administrada vs propia" cruza dos verticales: es una decisión de elección, pero sus requisitos (respaldo, réplica, alta disponibilidad) son operación. Eso coincide con tu planteo de verlos como requisitos y no como operación.

---

## 1. Modelos de datos

| Fuente | URL | Tipo | A/P/E/U | R | Marca |
|---|---|---|---|---|---|
| Codd 1970, "A Relational Model of Data for Large Shared Data Banks" | https://www.engineering.upenn.edu/~zives/03f/cis550/codd.pdf (el sitio ACM dio 403) | primaria | 3/2/1/3 | n/a | [M] solo descargué el PDF, que es un escaneo sin texto; título y año de memoria, no verificados |
| MongoDB, Data Modeling | https://www.mongodb.com/docs/manual/data-modeling/ | primaria, oficial | 3/2/2/2 | vigente | [L] |
| Redis, quick start de data store | https://redis.io/docs/latest/develop/get-started/data-store/ | primaria, oficial | 3/1/3/1 | vigente | [L] |
| Redis, persistencia | https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/ | primaria, oficial | 3/3/2/2 | vigente (menciona 8.10.0) | [L] |
| CMU 15-445, Fall 2026 | https://15445.courses.cs.cmu.edu/ | primaria (curso) | 3/3/1/2 | Fall 2026 | [S] |
| Kleppmann, DDIA | https://dataintensive.net/ | primaria (libro) | 3/3/3/3 | n/a | [M] la página no trae índice ni edición; O'Reilly dio 403 |

Afirmaciones:

- **Esquema flexible (documentos).** "Documents within a single collection are not required to have the same set of fields or data types." Se puede evolucionar el modelo "without rewriting existing documents or running a schema migration". https://www.mongodb.com/docs/manual/data-modeling/
- **Principio de diseño documental.** "A core principle of data modeling in MongoDB is that data that's accessed together should be stored together." Se pueden "embedding or referencing" los datos, y se puede imponer estructura con schema validation "if needed". https://www.mongodb.com/docs/manual/data-modeling/
- **Clave-valor.** Redis "stands for Remote Dictionary Server". Sus strings guardan "text, serialized objects, counter values, and binary arrays". Los hashes sirven para "plain objects". https://redis.io/docs/latest/develop/get-started/data-store/
- **Redis puede guardar a disco.** Ofrece RDB (snapshots), AOF (log de escrituras), ninguna persistencia ("sometimes used when caching") o RDB más AOF. La política por defecto de AOF es `appendfsync everysec`, con la que "you can only lose one second worth of writes". Con RDB solo, hay que estar "prepared to lose the latest minutes of data". https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/
- **Redis como otros modelos.** Su propia documentación lo ofrece también como base de documentos y de vectores (enlaces "Next steps"). https://redis.io/docs/latest/develop/get-started/data-store/
- **CMU 15-445 (Fall 2026, Jignesh Patel)** enseña el modelo relacional junto con los de documentos y clave-valor, y usa como texto Database System Concepts, 7.ª ed. https://15445.courses.cs.cmu.edu/

Discrepancia o cuidado: la página de CMU solo la leí por resumen del buscador, así que no cito su lista de temas como literal.

Recurso canónico:
- **Qué es y cómo se compara.** Kleppmann, DDIA, cap. 2 (Data Models and Query Languages): fijarse en la comparación relacional vs documentos (cuándo el impedimento objeto-relacional pesa y cuándo las uniones many-to-many favorecen a lo relacional). Aviso: confirmar si la 2.ª edición cambió los números de capítulo.
- **Cómo se hace.** Documentación oficial de cada motor: MongoDB Data Modeling (embeber vs referenciar) y Redis (tipos y persistencia).
- **Para citar de dónde viene lo relacional.** Codd 1970, solo la introducción. No es lectura para el público objetivo.

---

## 2. Transacciones

| Fuente | URL | Tipo | A/P/E/U | R | Marca |
|---|---|---|---|---|---|
| PostgreSQL docs, 13.2 Transaction Isolation | https://www.postgresql.org/docs/current/transaction-iso.html | primaria, oficial | 3/3/3/3 | docs 19.0 (la página decía "PostgreSQL 19.0 Documentation") | [L] por tabla y citas literales; la sección 13.2.3 la tomé por resumen |
| PostgreSQL docs, 13.1 MVCC intro | https://www.postgresql.org/docs/current/mvcc-intro.html | primaria | 3/2/1/2 | vigente | [L] |
| PostgreSQL docs, 13.3 Explicit Locking | https://www.postgresql.org/docs/current/explicit-locking.html | primaria | 3/3/2/2 | vigente | [L] |
| Berenson et al. 1995, "A Critique of ANSI SQL Isolation Levels" | https://arxiv.org/abs/cs/0701157 | primaria (paper) | 3/3/2/3 | 1995 | [M] solo abstract |
| Jepsen, PostgreSQL 12.3 | https://jepsen.io/analyses/postgresql-12.3 | primaria (análisis empírico) | 3/3/3/3 | 2020-06-12 | [S] resumen del abstract |
| Jepsen, Amazon RDS for PostgreSQL 17.4 | https://jepsen.io/analyses/amazon-rds-for-postgresql-17.4 | primaria | 3/3/2/3 | 2025-04-29 | [S] |
| Jepsen, índice de análisis | https://jepsen.io/analyses | índice | 2/1/1/1 | 2026 | [L] |
| Kleppmann DDIA cap. 7 | https://dataintensive.net/ | primaria | 3/3/3/3 | n/a | [M] |
| Silberschatz, Database System Concepts | (no se abrió) | primaria | 3/3/2/2 | n/a | no leído |

Afirmaciones con URL:

- **Anomalías y definiciones literales.** Lectura sucia: "A transaction reads data written by a concurrent uncommitted transaction." Lectura no repetible: "A transaction re-reads data it has previously read and finds that data has been modified by another transaction (that committed since the initial read)." Fantasma: "A transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction." Anomalía de serialización: "The result of successfully committing a group of transactions is inconsistent with all possible orderings of running those transactions one at a time." https://www.postgresql.org/docs/current/transaction-iso.html
- **Los cuatro niveles en PostgreSQL.** Se pueden pedir los cuatro, pero "internally only three distinct isolation levels are implemented, i.e., PostgreSQL's Read Uncommitted mode behaves like Read Committed". El defecto es Read Committed. En la tabla, Repeatable Read no permite fantasmas "in PG" y sí permite anomalía de serialización, que es el hueco donde vive el write skew. https://www.postgresql.org/docs/current/transaction-iso.html
- **MVCC.** "reading never blocks writing and writing never blocks reading." Cada sentencia ve "a snapshot of data (a database version) as it was some time ago". Esto aplica por sentencia en Read Committed. https://www.postgresql.org/docs/current/mvcc-intro.html
- **UPDATE condicional (el caso del último producto).** En Read Committed, si el primero commitea, "the second updater ... will attempt to apply its operation to the updated version of the row. The search condition of the command (the WHERE clause) is re-evaluated to see if the updated version of the row still matches". Por eso `UPDATE ... SET stock = stock - 1 WHERE stock > 0` es seguro en este motor y nivel. Es mi inferencia del mecanismo que cita la página: el ejemplo de stock no está en la documentación, y la página usa transferencias de cuentas. https://www.postgresql.org/docs/current/transaction-iso.html
- **Bloqueo pesimista.** "FOR UPDATE causes the rows retrieved by the SELECT statement to be locked as though for update. This prevents them from being locked, modified or deleted by other transactions until the current transaction ends." Los bloqueos de fila "block only writers and lockers to the same row". https://www.postgresql.org/docs/current/explicit-locking.html
- **Reintento en niveles altos.** En Repeatable Read o Serializable, SELECT FOR UPDATE da error si la fila cambió desde que empezó la transacción. Las aplicaciones "must be prepared to retry transactions due to serialization failures", con SQLSTATE 40001. https://www.postgresql.org/docs/current/explicit-locking.html y https://www.postgresql.org/docs/current/transaction-iso.html
- **Deadlocks.** PostgreSQL los detecta y aborta una transacción. "The best defense against deadlocks is generally to avoid them by being certain that all applications ... acquire locks on multiple objects in a consistent order." https://www.postgresql.org/docs/current/explicit-locking.html
- **Por qué las definiciones ANSI no alcanzan.** Abstract de Berenson et al.: "these phenomena and the ANSI SQL definitions fail to characterize several popular isolation levels"; se introducen fenómenos nuevos y se define Snapshot Isolation. Presentado en SIGMOD 1995, subido a arXiv el 2007-01-25. https://arxiv.org/abs/cs/0701157 La lista concreta de fenómenos (P0 a P4, A5A read skew, A5B write skew) es de mi memoria y no la pude verificar: el PDF de Microsoft Research vino comprimido y sin texto.
- **Cómo falla (Jepsen).** Con PostgreSQL 12.3: "transactions executed with serializable isolation on a single PostgreSQL instance were not, in fact, serializable"; se observó G2-item (patrón afín al write skew), con un bug de detección de conflictos corregido en un menor siguiente. "PostgreSQL 'repeatable read' is actually snapshot isolation." https://jepsen.io/analyses/postgresql-12.3
- **Jepsen sobre RDS.** "Amazon RDS for PostgreSQL multi-AZ clusters violate Snapshot Isolation"; hay Long Fork en clústeres sanos, en todas las versiones probadas de 13.15 a 17.4; no se observó write skew. El autor lo califica como "a cursory exploration". Hay una actualización del 2025-05-03 que atribuye la causa a que el primario ordena la visibilidad por un lock en memoria y los secundarios por el orden del WAL. https://jepsen.io/analyses/amazon-rds-for-postgresql-17.4

Discrepancia a registrar: el estándar ANSI y la documentación de PostgreSQL definen Repeatable Read de forma distinta. Para ANSI debería prohibir fantasmas y PostgreSQL ya los impide, mientras que sí permite write skew (según Jepsen, por ser snapshot isolation). Hay que contarlo como diferencia entre motores, no como error. Otros motores (MySQL, SQL Server, MongoDB) pueden diferir; no lo verifiqué.

Recurso canónico:
- **Qué es (conceptual).** Kleppmann, DDIA cap. 7 (Transactions): ACID, niveles de aislamiento, write skew, serializabilidad. Es la mejor explicación para el público. Aviso: citar de la edición vigente, y no pude confirmar si hay 2.ª edición.
- **Cómo se hace.** PostgreSQL docs cap. 13: leer 13.1 (MVCC), 13.2 (niveles, con la tabla) y 13.3 (bloqueos explícitos). Fijarse en la tabla 13.1 y en la cláusula de reintento.
- **Para ver que los niveles no coinciden con el estándar.** Berenson et al. 1995, leer el abstract y la tabla de fenómenos.
- **Cómo falla.** Jepsen sobre PostgreSQL 12.3: fijarse en que el write skew en Serializable fue un bug ya corregido, mientras que en Repeatable Read es comportamiento esperado.

---

## 3. Elegir una base

### Fichas de motores (versiones al 2026-11-27)

| Motor | Versión vigente leída | Fuente | Recencia | Marca |
|---|---|---|---|---|
| PostgreSQL | 19.0 (2026-11-19); 18.7 (primera versión 2025-09-25, EOL 2030-11-14); 17.12; 16.16; 15.20 (EOL 2027-11-11) | https://www.postgresql.org/support/versioning/ | muy reciente | [L] tabla |
| MySQL | 8.4.13.1 (2026-11-24; la serie 8.4 es la de soporte largo, la página no lo dice); 9.7.4.1 (2026-11-24, serie 9.x de innovación) | https://dev.mysql.com/doc/relnotes/mysql/8.4/en/ y https://dev.mysql.com/doc/relnotes/mysql/9.7/en/ | muy reciente | [S] |
| SQLite | 3.54.1 (2026-10-16); 3.54.0 (2026-10-09); 3.53.4 (2026-07-24) | https://www.sqlite.org/changes.html | reciente | [S] solo los primeros 100.000 de ~408.000 caracteres |
| MongoDB | 9.0 serie estable actual (9.0.0 el 2026-09-28; 9.0.8 el 2026-11-10; 9.0.7 el mismo día corrigió 27 CVEs); anteriores 8.3, 8.0, 7.0 | https://www.mongodb.com/docs/manual/release-notes/ y https://www.mongodb.com/docs/manual/release-notes/9.0/ | reciente | [S] |
| Redis | 8.12.0 (22 de noviembre, la página no dice el año); parche de seguridad del 26 de octubre en 8.10.3 y ramas anteriores | https://github.com/redis/redis/releases | reciente | [S] |

Licencia de Redis: desde la 8.0, Redis Open Source se ofrece bajo "RSALv2 or SSPLv1 or AGPLv3", a elección. https://redis.io/legal/licenses/ [L]

### Fichas de servicios administrados (precios leídos hoy)

| Servicio | Datos leídos | Fuente | Marca |
|---|---|---|---|
| Neon | Free: 100 CU-horas/proyecto/mes, 1 GB por proyecto, PITR de 6 horas. Launch: $0,106/CU-hora, $0,35/GB-mes, PITR hasta 7 días a $0,20/GB-mes. Scale: $0,222/CU-hora, PITR hasta 30 días. "No minimum monthly fee" en planes pagos. Página actualizada 2026-11-24. | https://neon.com/docs/introduction/plans | [S] |
| Supabase | Free: 500 MB, sin backups automáticos ni PITR, pausa tras 1 semana sin actividad. Pro: desde $25/mes, 8 GB, backups diarios 7 días, PITR como extra de $100/mes por 7 días. Team: desde $599/mes, backups 14 días. | https://supabase.com/pricing | [S] |
| Amazon RDS | Multi-AZ puede ser de una instancia en espera (que no atiende lecturas) o de un clúster con dos en espera (que sí las atienden). No leí retención de backups ni precios. | https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html | [S] |

Aviso de seguridad sobre la fuente: la página de Neon traía instrucciones dirigidas a asistentes de IA (instalar skills, enviar feedback a una URL externa). No las seguí.

### Criterios y afirmaciones

- **Cuándo alcanza SQLite.** "SQLite does not compete with client/server databases. SQLite competes with fopen()." Sitios con menos de 100K visitas por día "should work fine", y la cifra es "a conservative estimate, not a hard upper bound". Se evita cuando varios clientes acceden por red al mismo archivo, o con escritura intensa. Límite de tamaño: 281 terabytes (2^48 bytes). "SQLite supports an unlimited number of simultaneous readers, but it will only allow one writer at any instant in time." Regla: dispositivo local, poca concurrencia de escritura y menos de un terabyte, SQLite "is almost always a better solution". https://www.sqlite.org/whentouse.html [L]
- **Popularidad (no calidad).** Stack Overflow Developer Survey 2025, bases más usadas por todos los encuestados / por desarrolladores profesionales: PostgreSQL 55,6% / 58,2%; MySQL 40,5% / 39,6%; SQLite 37,5% / 36,9%; Redis 28% / 30,7%; MongoDB 24% / 24,3%. https://survey.stackoverflow.co/2025/technology#most-popular-technologies-database [S]. No encontré una edición 2026 y la página no dice si existe.
- **DB-Engines (popularidad, no calidad).** El sitio no se pudo abrir (error de certificado). Por terceros: en julio 2026 Oracle 1132, MySQL 846, SQL Server 698, PostgreSQL 687, MongoDB 386, Snowflake 216 (https://hellogithub.com/en/report/db-engines [S]). Un artículo de Redgate dice que el orden de los cuatro primeros no cambió en 12 meses (https://www.red-gate.com/simple-talk/databases/what-are-the-top-database-platforms-in-2026-a-look-at-the-latest-data/ [S]). Falta la edición de noviembre 2026.
- **Crítica de "elegí PostgreSQL por defecto".** Resultados del buscador, no los leí completos [S]:
  - El apéndice "When not to use Postgres" del libro "Just Use Postgres" (Manning) dice que no es "silver bullet" y que no conviene reemplazar una base que funciona solo por estandarizar. https://livebook.manning.com/book/just-use-postgres/appendix-b
  - Hilo de pgsql-general de 2019 (Pavel Stehule) desaconsejando Postgres como caché o para datos efímeros de mucha actualización. https://www.postgresql.org/message-id/CAFj8pRA9Chqr2m2_AieG02fyDq3oJcM6RrE3Z%2BGsceiqTv17-A%40mail.gmail.com
  - Postgres FM: si el equipo tiene mucha experiencia con otra base, el argumento a favor se debilita. https://postgres.fm/episodes/when-not-to-use-postgres
- **Respaldo, réplica y alta disponibilidad como requisitos.** Redis recomienda combinar RDB y AOF si se quiere "a degree of data safety comparable to what PostgreSQL can provide you"; con solo RDB, "be prepared to lose the latest minutes". https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/ En administrados el respaldo cambia mucho por plan: en Supabase Free no hay backups (https://supabase.com/pricing) y en Neon Free la restauración es de 6 horas (https://neon.com/docs/introduction/plans). Y alta disponibilidad no garantiza el aislamiento esperado: Jepsen encontró que RDS Multi-AZ en clúster es más débil que una instancia única (https://jepsen.io/analyses/amazon-rds-for-postgresql-17.4).

Discrepancias a registrar:
- MongoDB: la página de release notes decía que la serie previa era 8.3 y no 8.2 ni 8.1. No lo pude contrastar con otra fuente. Antes de publicar, confirmar en https://www.mongodb.com/docs/manual/release-notes/.
- MySQL: la propia página de 8.4 no dice "LTS"; que 8.4 sea la serie de soporte largo es conocimiento previo mío y la página de 9.7 solo lo sugiere. Confirmar en la política de releases de MySQL.
- Dos números de versión de PostgreSQL conviven en lo leído: la página de versionado muestra 19.0 como lanzada el 2026-11-19 y la 18.7 como actual de su serie. Las dos son coherentes entre sí, pero la 19.0 es muy reciente (8 días) y conviene decir cuál se recomienda.

Recurso canónico:
- **Elegir una base.** No hay uno solo. Propongo SQLite "Appropriate Uses" (https://www.sqlite.org/whentouse.html) por tener criterios explícitos y una lista de verificación; fijarse en las cuatro preguntas del final. Para el lado de "cuándo no PostgreSQL", el apéndice B de "Just Use Postgres" es opinión de practicante, no autoridad.
- **Qué hay hoy.** Las páginas oficiales de versiones (PostgreSQL versioning, release notes de MySQL y MongoDB, releases de Redis, changes de SQLite). Recencia alta pero volátil; cada una debe llevar fecha de lectura.
- **Popularidad.** Stack Overflow Developer Survey y DB-Engines, siempre rotulados como popularidad.

---

## Huecos

- **Modelos especializados** (grafos, series de tiempo, full-text, vectores): no busqué fuentes. Solo tengo menciones de pasada: MongoDB 9.0 cambió cómo guarda series de tiempo, Redis se ofrece como base de vectores y de documentos. Falta una fuente por cada modelo (por ejemplo, documentación de PostgreSQL sobre full-text y de pgvector, y algo canónico para grafos).
- **SQL y cómo escribirlo para quien viene de planillas:** no busqué nada (tutorial oficial de PostgreSQL, SQLite o similar). Es una necesidad central de la vertical de modelos y de la meta de enseñar SQL.
- **Libros no verificados:** Kleppmann (edición, índice y numeración de capítulos; O'Reilly y la página del autor no dieron los datos) y Silberschatz no se abrieron. Los números de capítulo que cité (2 y 7) vienen de tu mapa, no de una fuente leída.
- **Codd 1970:** PDF descargado pero sin texto legible. Falta título, abstract y año verificados. Ruta del archivo, por si se hace OCR: `/home/dela/.claude/projects/-home-dela-repos-personal-conocimiento/b5a4531d-70a6-4caa-badd-e0bc0c1d29d4/tool-results/webfetch-1795750278452-1ws0nf.pdf`.
- **Berenson:** solo abstract. Los fenómenos P0 a P4, A5A y A5B quedan sin verificar (el PDF de Microsoft Research venía comprimido).
- **Locking optimista con versión:** no encontré una fuente oficial que describa el patrón de columna de versión; solo el bloqueo pesimista (FOR UPDATE) está respaldado.
- **MySQL, MongoDB y SQLite en transacciones:** no verifiqué sus niveles de aislamiento por defecto ni sus diferencias con PostgreSQL. MySQL (InnoDB) y MongoDB pueden comportarse distinto en Repeatable Read; no lo leí. Jepsen tiene un análisis de MySQL 8.0.34 (2023-12-19) y uno de MongoDB 4.2.6 (2020-05-15) que no abrí.
- **Respaldo y alta disponibilidad en administrados:** de RDS leí solo el esquema Multi-AZ, no retención de backups ni precios. Supabase y Neon tienen precios y retención leídos, pero no su SLA ni su política de réplicas.
- **DB-Engines:** el sitio no se pudo leer (error de certificado) y la edición de noviembre 2026 quedó sin verificar.
- **Crítica de "PostgreSQL por defecto":** las fuentes que traje son de segunda mano (buscador) y de opinión. Falta una lectura completa de al menos una (por ejemplo el hilo de 2019 o la charla de Postgres FM), y ninguna es sistemática.
- **Encuesta de Stack Overflow 2026:** sin confirmar si existe.
- **SQLite changes:** solo leí los primeros 100.000 de ~408.000 caracteres, suficiente para la versión vigente, no para el historial.
