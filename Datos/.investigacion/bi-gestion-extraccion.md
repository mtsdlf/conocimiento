# Investigación: sacar datos de un sistema transaccional (ERP) para analizarlos

Fecha: 2026-11-27. Material de trabajo para notas en borrador; no es una nota.

**Cómo leer las marcas de lectura.**
- *Página completa (texto crudo)*: vi el texto entero de la página tal cual.
- *Página completa (extracción)*: la herramienta bajó la página entera y me devolvió las frases pedidas, copiadas textuales. Vi esas frases, no el resto de la página.
- *PDF (pdftotext)*: bajé el PDF y leí las líneas citadas en el texto extraído.
- *Snippet*: solo vi el resultado de un buscador. No se cita como fuente firme.

Las citas están en el idioma original. Donde la herramienta no me dio la frase literal, lo digo y no la presento como cita.

---

## 1. Por qué consultar en vivo la base del sistema transaccional es un problema

### Fowler, «ReportingDatabase» (bliki)
URL: https://martinfowler.com/bliki/ReportingDatabase.html. Publicado el 2 de abril de 2004 y actualizado el 2 de abril de 2014. Página completa (extracción).
- «Such a reporting database is a completely different database to the operational database.»
- «Queries run against the reporting database don't add to the load on the operational database.»
- «The structure of the reporting database can be specifically designed to make it easier to write reports.»
- «The downside to a reporting database is that its data has to be kept up to date.»
- La herramienta también resumió (no es cita) que los informes contra el esquema operativo compiten con el trabajo transaccional y quedan atados a su estructura. Además, Fowler menciona como variante las vistas replicadas.

### PostgreSQL: lecturas y escrituras con MVCC (matiz importante)
URL: https://www.postgresql.org/docs/current/mvcc-intro.html. Página completa (extracción).
- «each SQL statement sees a snapshot of data (a *database version*) as it was some time ago, regardless of the current state of the underlying data.»
- «in MVCC locks acquired for querying (reading) data do not conflict with locks acquired for writing data, and so reading never blocks writing and writing never blocks reading.»
- **Matiz para la nota.** En motores MVCC el problema de una consulta larga no son tanto los bloqueos como la carga (CPU, E/S) y el snapshot que mantiene vivas versiones viejas de las filas (ver lo que sigue). En motores que bloquean filas al leer, sí hay contención por bloqueos, pero no encontré una fuente primaria neutral que lo diga (**hueco**).

### PostgreSQL: un snapshot abierto impide limpiar filas muertas
URL: https://www.postgresql.org/docs/current/routine-vacuuming.html. Página completa (extracción, búsqueda de términos).
- §24.1.2: «the row version must not be deleted while it is still potentially visible to other transactions.»
- §24.1.5: «End long-running open transactions.» Aparece entre los pasos para recuperarse del agotamiento de IDs de transacción.
- **Hueco.** La página actual no tiene una frase literal del tipo «una transacción larga impide que VACUUM quite filas muertas y produce bloat». El mecanismo se deduce de la frase de §24.1.2. Un snippet de la doc de autovacuum («no long-running transactions should be allowed to hold back every VACUUM operation's cutoff») venía de un adjunto de la lista de correo, no de la doc publicada. No lo verifiqué.

### PostgreSQL: réplica de lectura (hot standby), sus conflictos y el costo en el primario
URL: https://www.postgresql.org/docs/current/hot-standby.html (§«Handling Query Conflicts»). Página completa (extracción).
- «The standby server must either delay application of the WAL records (and everything after them, too) or else cancel the conflicting query so that the `DROP TABLE` can be applied.»
- «allowing WAL application to wait indefinitely may be very undesirable, because the standby's state will become increasingly far behind the primary's. Therefore, a mechanism is provided to forcibly cancel standby queries that conflict with to-be-applied WAL records.»
- «Conflicting queries will be canceled once it has taken longer than the relevant delay setting to apply any newly-received WAL data.»
- «if the standby server is meant for executing long-running queries, then a high or even infinite delay value may be preferable. Keep in mind however that a long-running query could cause other sessions on the standby server to not see recent changes on the primary, if it delays application of WAL records.»
- «Users should be clear that tables that are regularly and heavily updated on the primary server will quickly cause cancellation of longer running queries on the standby.»
- «The first option is to set the parameter `hot_standby_feedback`, which prevents `VACUUM` from removing recently-dead rows and so cleanup conflicts do not occur.»
- «If you do this, you should note that this will delay cleanup of dead rows on the primary, which may result in undesirable table bloat.»
- «However, the cleanup situation will be no worse than if the standby queries were running directly on the primary server, and you are still getting the benefit of off-loading execution onto the standby.» Esta frase sirve para la nota: confirma que consultar directo sobre el primario produce el mismo efecto.

URL: https://www.postgresql.org/docs/current/runtime-config-replication.html. Página completa (extracción).
- `hot_standby_feedback`: «This parameter can be used to eliminate query cancels caused by cleanup records, but can cause database bloat on the primary for some workloads.» El valor por defecto es `off`.
- `max_standby_streaming_delay`: «determines how long the standby server should wait before canceling standby queries that conflict with about-to-be-applied WAL entries». «The default is 30 seconds. A value of -1 allows the standby to wait forever for conflicting queries to complete.»

### PostgreSQL: el atraso de la réplica
URL: https://www.postgresql.org/docs/current/warm-standby.html. Página completa (extracción).
- «Streaming replication is asynchronous by default […], in which case there is a small delay between committing a transaction in the primary and the changes becoming visible in the standby. This delay is however much smaller than with file-based log shipping, typically under one second assuming the standby is powerful enough to keep up with the load.»
- «An important health indicator of streaming replication is the amount of WAL records generated in the primary, but not yet applied in the standby.»
- «Large differences between `pg_current_wal_lsn` and the view's `sent_lsn` field might indicate that the primary server is under heavy load, while differences between `sent_lsn` and `pg_last_wal_receive_lsn` on the standby might indicate network delay, or that the standby is under heavy load.»

---

## 2. Formas de extraer

### 2a. Extracción completa (full)
- Confluent JDBC Source, modo `bulk`. URL: https://docs.confluent.io/kafka-connectors/jdbc/current/source-connector/overview.html. Página completa (extracción). Citas: «This mode is unfiltered and therefore not incremental at all.» y «It will load all rows from a table on each iteration.» La herramienta resumió (no es cita) que el modo sirve para tablas donde se borran filas, siempre que el destino tolere duplicados.
- Dynamics 365 BYOD (evidencia de proveedor, no nombrar en la nota). URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database (ms.date 2026-09-26). Página completa (texto crudo).
  - «Export either all the records (*full push*) or only the records that changed or deleted (*incremental push*).»
  - «A full push deletes all existing records from an entity and then inserts the current set of records from the selected entity.»
  - «Use **Full push only** exports instead of **Incremental only** exports for smaller data sizes.» Esa frase da el ejemplo de entidades de unos 1.000 registros o menos.

### 2b. Incremental por columna de fecha (marca de agua) y sus fallas
**Sin borrados y sin cambios intermedios.** Gunnar Morling, «Five Advantages of Log-Based Change Data Capture», blog de Debezium, 19-07-2018. URL: https://debezium.io/blog/2018/07/19/advantages-of-log-based-change-data-capture/. Página completa (extracción).
- «Naturally, polling will not allow you to identify any records that have been deleted since the last poll.»
- «you might miss intermediary data changes that happen between two runs of the poll loop.»
- «all the captured tables need to have some column like LAST_UPDATE_TIMESTAMP which can be used to find changed rows.»
- «polling too frequently may cause performance issues (as the queries used for polling cause load on the source database).»

**Filas cambiadas sin tocar la fecha.** Airbyte, «Incremental Sync - Append». URL: https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append. Página completa (extracción).
- Del apartado Known Limitations: «if modifications to the underlying records are made without properly updating the cursor field». La herramienta lo devolvió como fragmento; el ejemplo de la doc es una fila con `updated_at` sin cambiar que nunca llega al warehouse.
- «Incremental will never delete or mutate existing records.»
- «By convention, sources should prefer resending data if the cursor field is ambiguous.»
- Resumido por la herramienta (no es cita): los cambios que pasan entre dos corridas no se capturan, y la doc remite a CDC como alternativa.

**Supuestos del modo timestamp y orden de commit.** Confluent, referencia de configuración del JDBC Source 10.8. URL: https://docs.confluent.io/kafka-connectors/jdbc/10.8/source-connector/source_config_options.html. Página completa (extracción).
- Modo timestamp: «use a timestamp (or timestamp-like) column to detect new and modified rows.» «This assumes the column is updated with each write, and that values are monotonically incrementing,» «but not necessarily unique.»
- Modo incrementing: «Note that this will not detect modifications or deletions of existing rows.»
- `timestamp.delay.interval.ms`: «After a row with a certain timestamp appears, this is the amount of time the connector waits to include it in the result.» «You can add a delay to allow transactions with an earlier timestamp to complete.» Esta es la evidencia de documentación del problema de orden de commit: una transacción que empezó antes (fecha más vieja) pero confirma después queda detrás de la marca de agua.
- Overview (URL de 2a): «this mode can't guarantee that all updated data will be delivered» y «The connector might not be able to fetch some records from a table in this mode.»

**Orden de commit, reportes de usuarios (snippets, evidencia débil).**
- https://forum.confluent.io/t/jdbc-source-connector-loses-data-in-incrementing-and-timestamp-incrementing-modes/3175. Snippet: una fila insertada sin confirmar queda atrás de otra que confirma antes.
- https://discuss.meltano.com/t/16354296/we-ve-noticed-that-with-tap-postgres-transferwise-incrementa. Snippet: faltan filas con fecha justo antes de la marca, probablemente por una transacción larga.
- **Hueco.** No encontré un artículo académico ni de documentación de base de datos que explique el problema de orden de commit con todas las letras. Lo más firme es la frase de Confluent sobre `timestamp.delay.interval.ms`.

**Reloj y zona horaria (snippet).** https://groups.google.com/g/confluent-platform/c/wZ5yYjaN18E. Snippet: se perdían registros porque el conector usaba CURRENT_TIMESTAMP y la base estaba en otra zona horaria. Es un reporte de usuario; **hueco** de fuente firme sobre el desfase de relojes.

**Borrados físicos (Stitch/Qlik).** Solo vi snippets; la página https://help.qlik.com/en-US/stitch/replication/replication-methods/key-based-incremental dio 404 al abrirla. El snippet decía: «When a record is hard deleted, or entirely removed from a source, its Replication Key value is also removed. Without a Replication Key value to check, Stitch can't identify the change and update the record in the destination.» No verificado.

### 2c. Captura de cambios desde el log (CDC)
**Debezium, «Features».** URL: https://debezium.io/documentation/reference/stable/features.html. Página completa (extracción). Ventajas frente a polling o dual writes:
- «Ensures that all data changes are captured»
- «Produces change events with a very low delay while avoiding increased CPU usage required for frequent polling.»
- «Requires no changes to your data model»
- «Can capture deletes»
- «Can capture old record state and additional metadata»
- Sobre el snapshot inicial: «an initial snapshot of a database's current state can be taken if a connector is started». La frase sigue con la condición de que no estén todos los logs.

**PostgreSQL, decodificación lógica.** URL: https://www.postgresql.org/docs/current/logicaldecoding-explanation.html. Página completa (extracción).
- «Logical decoding is the process of extracting all persistent changes to a database's tables into a coherent, easy to understand format which can be interpreted without detailed knowledge of the database's internal state.»
- «In PostgreSQL, logical decoding is implemented by decoding the contents of the write-ahead log, which describe changes on a storage level, into an application-specific form such as a stream of tuples or SQL statements.»
- El costo de CDC sobre el origen: «neither required WAL nor required rows from the system catalogs can be removed by `VACUUM` as long as they are required by a replication slot.» «They will prevent removal of required resources even when there is no connection using them.» «In extreme cases this could cause the database to shut down to prevent transaction ID wraparound […]. So if a slot is no longer required it should be dropped.»
- Esta página no enumera INSERT, UPDATE y DELETE. Para «incluye borrados» hay que citar a Debezium.

**MySQL, binary log.** URL: https://dev.mysql.com/doc/refman/8.4/en/binary-log.html. Página completa (extracción).
- «The binary log contains "events" that describe database changes such as table creation operations or changes to table data.»
- «For replication, the binary log on a replication source server provides a record of the data changes to be sent to replicas.»

**Kimball, subsistema de CDC (técnicas).** Ralph Kimball, «The 38 Subsystems of ETL», 23-11-2004 (InformationWeek). URL: https://www.informationweek.com/software/information-management/the-38-subsystems-of-etl/d/d-id/1028653. Página completa (extracción).
- Subsistema 1, Extract system: «Source data adapters, push/pull/dribble job schedulers, filtering and sorting at the source,» «proprietary data format conversions, and data staging after transfer to ETL environment.»
- Subsistema 2, Change data capture system: «Source log file readers, source date and sequence number filters, and CRC-based record comparison in ETL system.» Ahí están las tres técnicas: el log, la fecha o secuencia, y la comparación contra la extracción anterior.
- «You get the data out of its original source location (E)».

### 2d. Réplica de lectura
Ver PostgreSQL hot standby en §1: descarga el primario, pero trae cancelación de consultas, atraso, o bloat en el primario si se activa `hot_standby_feedback`.

### 2e. API de la aplicación o archivos de exportación
- BYOD (URL en 2a), sin acceso SQL a producción: «The application doesn't allow T-SQL connections to the production database.» La exportación sale por «data entities» de la aplicación («Currently, more than 1,700 data entities are available.») y también a formatos como CSV: «Use the **Export** page to export data into many target data formats, such as a comma-separated values (CSV) file.»
- Lectura consistente mientras corre la exportación: «there's always the challenge of ensuring that the reporting systems get consistent data from BYOD while the sync is in progress. […] The staging tables hold the data while data is being synced from the instance and hence constantly changes.»
- El incremental cae a completo cuando se pasa la retención: «The incremental push export doesn't run within the retention period. To prevent data loss, the export automatically falls back to the full push setting.»
- Entidades sin clave única: «you can enable change tracking only for entities that have a unique key. Therefore, there's a limitation on incremental push.»

---

## 3. Kimball Group sobre CDC y extracción
- Bob Becker, «The Subsystems of ETL Revisited», Kimball Group, 21-10-2007. URL: https://www.kimballgroup.com/2007/10/subsystems-of-etl-revisited/. Página completa (extracción).
  - Subsistema 1 (Data Profiling): «Explores a data source to determine its fit for inclusion as a source» «and the associated cleaning and conforming requirements.»
  - Subsistema 2 (CDC): «Isolates the changes that occurred in the source system to reduce the ETL processing burden.»
  - Subsistema 3 (Extract): «Extracts and moves source data into the data warehouse environment for further processing.»
  - Subsistema 16 (Late Arriving Data Handler): «Applies special modifications to the standard processing procedures to deal with late-arriving fact and dimension data.»
- Kimball 2004, los 38 subsistemas: ver §2c.
- **Hueco.** No encontré en kimballgroup.com un artículo ni un Design Tip específico sobre ERP o aplicaciones empaquetadas como origen. El libro *The Data Warehouse ETL Toolkit* (Kimball y Caserta, 2004) tiene en su índice un apartado «ERP System Sources», según un snippet, y apartados «Detecting Changes» y «Extraction Tips». No lo leí: la única copia accesible era un PDF de dudosa legitimidad alojado en un sitio universitario y no la usé. Si hace falta, conseguir el libro.
- **Hueco.** No pude leer el Design Tip #57 «Early Arriving Facts» (2004), que solo está en un PDF archivado.

---

## 4. Dificultades propias de las bases de un ERP o aplicación empaquetada

### Muchísimas tablas y conocimiento del dominio (académico)
Berti, Park, Rafiei y van der Aalst, «A generic approach to extract object-centric event data from databases supporting SAP ERP», *Journal of Intelligent Information Systems* (2023) 61:835–857, DOI 10.1007/s10844-023-00799-9. Copia del autor: https://www.vdaalst.com/publications/p1431.pdf. PDF (pdftotext).
- «extracting event logs is challenging due to the size of the data, and it remains ad-hoc.» (abstract)
- «Each of the aforementioned phases is challenging. First of all, process identification is not trivial since a database contains records of hundreds of different business processes. Despite knowing the target process to analyze, inferring the set of tables related to the target process is challenging, e.g., a database supporting an SAP ERP system contains hundreds of thousands of tables. Furthermore, formulating querying statements, e.g., SQL queries, requires a huge amount of domain knowledge.»
- La lógica vive en la aplicación: «in some information systems, such as SAP ERP, the coherence of the schema is maintained at the application level; moreover, the database updates could be stored as REDO logs, in-table versioning, or as separate change tables (de Murillas et al., 2015)».

Berti, Park, Rafiei y van der Aalst, «An Event Data Extraction Approach from SAP ERP for Process Mining», arXiv:2110.03467 (2021). URL: https://ar5iv.labs.arxiv.org/html/2110.03467. Página completa (extracción).
- «The ETL phase is usually the most time-consuming part of a process mining project»
- «Extracting data from an SAP ERP system is particularly challenging as it involves many different tables/objects.»
- «which requires extensive interaction with domain experts»
- Sobre las tablas de cambios: «A *change table* describes the changes in objects of the target business process, e.g., CDHDR and CDPOS are primary change tables.» Sirve para §5: en un ERP la historia de cambios puede vivir en tablas propias de la aplicación.

**Hueco: nombres crípticos.** Ningún texto que leí trata como dificultad los nombres abreviados de tablas y campos. Los papers usan nombres como EKKO o VBFA solo como ejemplos.

### Sin acceso directo a la base y restricciones del proveedor (evidencia de proveedor, no nombrar en la nota)
- Dynamics 365 F&O: «The application doesn't allow T-SQL connections to the production database.» (URL en 2a; texto crudo). La salida prevista son las entidades exportadas a una base propia del cliente.
- Nota SAP 3255746 (ODP-RFC). No leí la nota, que está tras login. Lo que sigue viene de un tercero con interés comercial: Christoph Schuler, Theobald Software, 23-04-2026. URL: https://theobald-software.com/en/blog/sap-note-325574. Página completa (extracción).
  - «Any use of ODP-RFC by customer or third-party applications to access SAP ABAP systems» queda prohibido (la frase la cortó la herramienta).
  - «Issues resulting from non-compliant use of ODP-RFC are the sole responsibility of the customer.»
  - «On April 21, 2026, SAP released Version 11 of Note 3255746.»
  - «From June 2026, a security patch will technically block unauthorized ODP-RFC calls.»
  - «A common misunderstanding: SAP Note 3255746 does not prohibit RFC as a communication protocol.»
  - Para la nota: el proveedor puede decidir, y cambiar, qué vías de extracción permite. Fuente secundaria con interés; tratar con cuidado.

### SaaS multi-tenant: solo API y con límites (evidencia de proveedor)
Microsoft Dataverse, «Service protection API limits» (ms.date 2026-10-26). URL: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits. Página completa (texto crudo).
- «To ensure consistent availability and performance for everyone, Dataverse applies limits to how APIs are used. These limits detect when client applications make extraordinary demands on server resources.»
- «With the Web API, Dataverse returns a 429 Too Many Requests error.»
- «Applications designed to load data into Dataverse or perform bulk updates must manage service protection API limit errors.»
- Por defecto, por servidor web: 6.000 solicitudes, 20 minutos de ejecución combinada y 52 o más solicitudes concurrentes, todo en una ventana deslizante de 5 minutos. La doc aclara: «These limits can change and might vary between different environments.»
- «If your current business processes depend on large periodic nightly, weekly, or monthly jobs that attempt to process large amounts of data in a short period of time, consider how you might enable a real-time data integration strategy.» Una voz de proveedor a favor de lo incremental y continuo.
- **Hueco.** No pude abrir la página de límites de API de Salesforce (403). No encontré una fuente académica sobre extracción desde SaaS multi-tenant con límites de API.

---

## 5. Documentos que cambian después: correcciones, anulaciones, hechos tardíos

### Kimball, hechos y dimensiones tardíos
- «Late Arriving Fact». URL: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/late-arriving-fact/. Página completa (extracción).
  - «A fact row is late arriving if the most current dimensional context for new fact rows does not match the incoming row.»
  - Qué hacer: buscar las «dimension keys that were effective when the late arriving measurement event occurred.»
- «Late Arriving Dimension». URL: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/late-arriving-dimension/. Página completa (extracción).
  - «special dimension rows are created with the unresolved natural keys as attributes.»
  - «the placeholder dimension rows are updated with type 1 overwrites.»
  - Sobre cambios retroactivos: «a new row needs to be inserted in the dimension table, and then the associated fact rows must be restated.»
- «Accumulating Snapshot Fact Table». URL: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/accumulating-snapshot-fact-table/. Página completa (extracción).
  - «As pipeline progress occurs, the accumulating fact table row is revisited and updated.»
  - «There is a date foreign key in the fact table for each critical milestone in the process.» Sirve para pedidos que avanzan de estado.

### Académico: mediciones tardías y tiempo de transacción frente a tiempo válido
Golfarelli y Rizzi, «Managing Late Measurements in Data Warehouses», *International Journal of Data Warehousing and Mining* 3(4):51–67, 2007. URL: https://ideas.repec.org/a/igg/jdwm00/v3y2007i4p51-67.html. Solo el abstract (extracción).
- «whenever late measurements of events take place»
- «the traditional design solutions fail in preserving accountability and query consistency»
- «based on the enforcement of the distinction between transaction time and valid time»
- En el snippet del buscador apareció la frase entera: «particularly when the events registered are subject to further updates, the traditional design solutions fail in preserving accountability and query consistency». No pude leer el paper completo (el PDF de scispace vino vacío).

### Fowler, correcciones en contabilidad: invertir en vez de editar
- «Reversal Adjustment», 2 de enero de 2006. URL: https://martinfowler.com/eaaDev/ReversalAdjustment.html. Página completa (extracción).
  - «For each entry that needs to be adjusted you create two new entries.»
  - «One entry is a simple reversal of the previous entry»
  - «Reversal Adjustment is a simple alternative when entries are immutable»
  - «it results in a lot of entries»
- «Retroactive Event», 12 de diciembre de 2005. URL: https://martinfowler.com/eaaDev/RetroactiveEvent.html. Página completa (extracción).
  - «Automatically correct the consequences of a incorrect event that's already been processed.»
  - «A rejected event is an event that you now realize was false and should never have been processed.»
  - «In rewind/replay we reverse the events backwards from the latest event to the branch point.»
  - La herramienta resumió (no es cita) que la tercera categoría es la de eventos fuera de orden, que se insertan en el punto de bifurcación.

### Huecos de §5
- No encontré una fuente neutral que trate específicamente la factura anulada por nota de crédito, el asiento con fecha retroactiva o el período reabierto como problema de extracción. Lo más cercano: Fowler (corrección por reversa), Golfarelli y Rizzi (eventos que se actualizan después) y Kimball (hechos tardíos, reexpresión). La conclusión práctica no la dice literal ninguna fuente y habría que presentarla como inferencia: extraer por fecha de registro o de modificación y no por fecha contable, y volver a leer una ventana hacia atrás.
- La consecuencia de «Morling: se pierden cambios intermedios» (§2b) es que un documento que cambió dos veces entre corridas muestra solo su último estado.

---

## 6. Frescura: cuán frescos tienen que ser los datos

### A favor de «alcanza con lo de ayer»: Fowler, ReportingDatabase (URL en §1)
- «This often works quite well since many reporting needs work perfectly well with yesterday's data.»
- Sobre mensajería para más frescura: «This is more complicated, but the data can be kept fresher.»
- «Reacting too quickly leads to a form of information panic». La herramienta devolvió un fragmento, no la frase entera.

### Voces contrarias: HTAP, analítica sobre datos frescos
Zhang, Li, Zhang, Zhang y Feng, «HTAP Databases: A Survey», arXiv:2404.15670 (2024; IEEE TKDE según el snippet). URL: https://arxiv.org/html/2404.15670v1. Leí los primeros 100.000 caracteres de unos 144.000 (extracción).
- Abstract: «combine transactions with analytics in order to enable real-time data analytics»
- §I: «eliminate the need for an explicit Extract-Transform-Load (ETL) process»
- §I: «the two types of workloads exhibit a completely different computing pattern and can intervene with each other». Sirve como respaldo académico de que mezclar cargas molesta.
- §II-B: «HTAP databases must balance a trade-off between data freshness and performance isolation.»
- §II-B: «may lead to low data freshness, hence the outdated results of data analytics»
- Otra encuesta, solo por snippet: Song, Zhou, Cui, Peng y Li, «A survey on hybrid transactional and analytical processing», *The VLDB Journal* (2024). https://link.springer.com/article/10.1007/s00778-024-00858-9. No leída.

Voz de proveedor con la misma dirección: Dataverse, la frase «consider how you might enable a real-time data integration strategy» (§4).

**Hueco.** El paper de Plattner (SIGMOD 2009, «A common database approach for OLTP and OLAP using an in-memory column database») no lo pude leer. Lo que bajé de hpi.de eran diapositivas: «Modern ERP systems are challenged by a mixed workload including OLAP-style queries, e.g., Dunning-run, Available-to-promise, and Real-time operational reporting». Plattner, además, no es neutral: es cofundador del proveedor que vende HANA.

---

## Resumen de huecos
1. No hay una frase literal de la doc de PostgreSQL que diga que una transacción larga en el primario produce bloat; se deduce de §24.1.2 y de la doc de hot standby.
2. No hay una fuente primaria neutral sobre contención por bloqueos en motores que no usan MVCC.
3. El orden de commit frente a la marca de agua solo tiene respaldo en la doc de Confluent (`timestamp.delay.interval.ms`) y en foros; falta una fuente académica.
4. El desfase de relojes y zonas horarias en la extracción incremental solo tiene un reporte de foro.
5. No encontré un artículo de Kimball sobre ERP o aplicaciones empaquetadas como origen, ni leí *The Data Warehouse ETL Toolkit* («ERP System Sources», «Detecting Changes»).
6. Ninguna fuente trata los nombres crípticos de tablas como dificultad.
7. Faltan una fuente académica sobre SaaS con límites de API y la página de límites de Salesforce (403).
8. Falta una fuente neutral sobre nota de crédito, asiento retroactivo y período reabierto como problema de extracción.
9. Del paper de Golfarelli y Rizzi solo tengo el abstract.
10. El paper de Plattner (2009) no lo leí.
