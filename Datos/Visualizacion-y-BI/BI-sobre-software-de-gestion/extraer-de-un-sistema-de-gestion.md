---
resumen: >-
  Extraer de un sistema de gestión es copiar sus datos a un lugar donde se puedan analizar sin
  cargar la base que factura: por exportación completa, por fecha de modificación, leyendo el
  registro de cambios de la base o por la API del producto. Lo difícil es traer bien lo que cambió
  después: las anulaciones, los movimientos con fecha pasada y los períodos reabiertos.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, Reporting Database (2004, revisado 2014): https://martinfowler.com/bliki/ReportingDatabase.html"
  - "PostgreSQL, Concurrency Control, Introduction: https://www.postgresql.org/docs/current/mvcc-intro.html"
  - "PostgreSQL, Hot Standby, Handling Query Conflicts: https://www.postgresql.org/docs/current/hot-standby.html"
  - "PostgreSQL, Logical Decoding Concepts: https://www.postgresql.org/docs/current/logicaldecoding-explanation.html"
  - "Gunnar Morling, Five Advantages of Log-Based Change Data Capture (2018): https://debezium.io/blog/2018/07/19/advantages-of-log-based-change-data-capture/"
  - "Documentación de un conector de datos, JDBC Source configuration (modo timestamp y timestamp.delay.interval.ms): https://docs.confluent.io/kafka-connectors/jdbc/10.8/source-connector/source_config_options.html"
  - "Ralph Kimball, The 38 Subsystems of ETL (2004): https://www.informationweek.com/software/information-management/the-38-subsystems-of-etl/d/d-id/1028653"
  - "Bob Becker, The Subsystems of ETL Revisited (Kimball Group, 2007): https://www.kimballgroup.com/2007/10/subsystems-of-etl-revisited/"
  - "Berti, Park, Rafiei y van der Aalst, A generic approach to extract object-centric event data from databases supporting SAP ERP, Journal of Intelligent Information Systems 61 (2023): https://www.vdaalst.com/publications/p1431.pdf"
  - "Documentación del ERP de un proveedor grande, exportar entidades a una base propia: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database"
  - "Documentación de una plataforma de un proveedor grande, Service protection API limits: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits"
  - "Kimball Group, Late Arriving Fact y Late Arriving Dimension: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/late-arriving-fact/"
  - "Martin Fowler, Reversal Adjustment (2006): https://martinfowler.com/eaaDev/ReversalAdjustment.html"
  - "Datos/.investigacion/bi-gestion-extraccion.md (2026-11-27)"
aliases: [extracción del ERP, extraer datos del ERP, ERP extraction, sacar datos del sistema de gestión, réplica de lectura, read replica, extracción incremental, marca de agua, watermark]
creado: 2026-11-27
revisado:
---

# Extraer de un sistema de gestión

Extraer de un sistema de gestión es copiar sus datos a un lugar donde se puedan analizar sin cargar la base que factura: por exportación completa, por fecha de modificación, leyendo el registro de cambios de la base o por la API del producto. Lo difícil es traer bien lo que cambió después: las anulaciones, los movimientos con fecha pasada y los períodos reabiertos.

Es el primer paso del [BI sobre el software de gestión](bi-sobre-software-de-gestion.md). Las maneras generales de traer un dato están en [ingesta](../../Ingesta-y-transformacion/ingesta.md), y por qué el análisis va en una copia, en [OLTP y OLAP](../../Modelado-y-almacenamiento/oltp-y-olap.md). El intercambio con la tienda o el banco es de [integración y migración](../../../Software-de-gestion/Columnas-tecnicas/integracion-y-migracion.md).

## Qué pasa si se consulta la base en vivo

Una consulta de cuatro años de facturas compite con la factura de ahora. Fowler: «Queries run against the reporting database don't add to the load on the operational database».

En una base con control de versiones, el costo no está en los bloqueos: «reading never blocks writing and writing never blocks reading», según la documentación de un motor de código abierto. Una consulta larga abierta impide limpiar las versiones viejas de filas que podría ver. Una réplica de lectura cancela las consultas largas que chocan con los cambios del primario, o se atrasa si las espera. Si avisa al primario para evitarlo, el primario demora la limpieza y puede crecer de más; aun así, «the cleanup situation will be no worse than if the standby queries were running directly on the primary server».

En lectura de esta base, la réplica sirve para consultas cortas y para extraer; el análisis de años va a un [almacén analítico](../../Modelado-y-almacenamiento/almacenes-analiticos.md).

## Cuatro formas de sacar el dato

| Forma | Qué trae | Dónde falla |
|---|---|---|
| Exportación completa | todas las filas de cada tabla, cada vez | tarda más cuanto más crece la base; sirve para maestros y tablas chicas |
| Incremental por fecha de modificación | las filas cambiadas desde la última corrida (la marca de agua) | no ve los borrados, pierde los cambios intermedios y las filas que cambian sin tocar la fecha |
| Copia de cambios desde el registro de la base | cada alta, cambio y borrado | exige acceso al registro, que se retiene mientras el lector no lo consume |
| API o exportación del producto | lo que el producto expone, con su lógica aplicada | tiene límites de uso y no siempre trae el borrado ni la historia |

Las fallas de las dos filas del medio vienen de las fuentes de abajo; las de la primera y la última son lectura de esta base. Kimball ya enumeraba en 2004 tres técnicas para detectar cambios: «Source log file readers, source date and sequence number filters, and CRC-based record comparison»; la última compara cada fila con la extracción anterior.

La marca de agua falla de cuatro maneras. Morling, de un proyecto abierto de copia de cambios, nombra dos: «polling will not allow you to identify any records that have been deleted since the last poll», y «you might miss intermediary data changes that happen between two runs». La documentación de un conector suma la tercera: el modo por fecha «assumes the column is updated with each write». La cuarta asoma en un parámetro que existe «to allow transactions with an earlier timestamp to complete»: una transacción que empezó antes de la marca y confirma después no se trae nunca.

Leer el registro de la base trae también los borrados. La documentación del mismo motor define la decodificación lógica como extraer «all persistent changes to a database's tables» desde el registro de escritura, y el proyecto abierto confirma: «Can capture deletes». A cambio, la base retiene el registro que un lector definido no leyó, «even when there is no connection using them».

## Lo propio de un ERP como origen

El esquema de un ERP no se entiende solo. Un trabajo académico sobre un ERP grande dice que su base «contains hundreds of thousands of tables», que escribir las consultas «requires a huge amount of domain knowledge» y que «the coherence of the schema is maintained at the application level». Una factura puede repartirse en cabecera, renglones, impuestos y vencimientos sin que la base diga cómo se relacionan (lectura de esta base).

El proveedor decide por dónde se sale. La documentación del ERP de un proveedor grande dice que «The application doesn't allow T-SQL connections to the production database» y ofrece exportar sus entidades a una base del cliente. En un producto vendido como servicio suele quedar solo la API (lectura de esta base). Otra plataforma pone límites de uso por ventana de tiempo y recomienda integración continua en lugar de trabajos masivos nocturnos. Esas vías cambian: según un tercero con interés comercial, un proveedor grande anunció en 2026 que bloquea una vía que usaban herramientas de terceros. Antes de diseñar la extracción hay que leer qué permite el contrato (lectura de esta base).

La lógica vive en el producto. Un importe en la base puede estar sin impuestos, en la moneda de la operación o con el signo de un documento que resta, y la API suele devolverlo ya interpretado. En lectura de esta base, extraer de la base exige reproducir esa lógica, y por la API, aceptar sus límites.

> [!NOTE]
> Sin fuente todavía: un texto neutral sobre las extracciones de un ERP (la sección «ERP System Sources» de *The Data Warehouse ETL Toolkit* de Kimball y Caserta no se leyó) y una fuente académica sobre extraer de un producto vendido como servicio con límites de API.

## Los cambios que llegan después

Un sistema de gestión cambia el pasado de tres maneras:

1. La anulación. Un [documento](../../../Software-de-gestion/Columnas-tecnicas/documento-y-estados.md) confirmado no se edita: se anula con otro, como la nota de crédito. Fowler corrige cada movimiento con «two new entries», una de ellas «a simple reversal of the previous entry». Para el BI son filas nuevas, y la factura original sigue ahí.
2. El movimiento con fecha pasada. Una factura de proveedor de octubre se carga en noviembre con su fecha del hecho, y la extracción que filtra por fecha del documento («traer octubre») no la trae. Las dos fechas están en [fechas, vigencias y cierre](../../../Software-de-gestion/Columnas-tecnicas/fechas-vigencias-y-cierre.md#la-fecha-del-hecho-y-la-fecha-de-registro).
3. El período reabierto. Si alguien levanta la [fecha de bloqueo](../../../Software-de-gestion/Columnas-tecnicas/fechas-vigencias-y-cierre.md#la-fecha-de-bloqueo) y agrega un asiento, cambia un período que el BI daba por cerrado.

Kimball llama hecho tardío a una fila cuyo contexto ya cambió, y pide las claves de dimensión «that were effective when the late arriving measurement event occurred» ([historia en el BI de gestión](historia-en-el-bi-de-gestion.md)).

La regla (lectura de esta base): extraer por fecha de modificación, nunca por fecha del documento, y releer una ventana hacia atrás en cada corrida. La ventana llega hasta la fecha de bloqueo: lo anterior al último cierre no debería cambiar, y si cambia, lo detecta la [conciliación](conciliar-el-bi.md).

> [!NOTE]
> Sin fuente todavía: una fuente neutral que trate la nota de crédito, el asiento retroactivo y el período reabierto como problemas de extracción. Lo más cercano son Fowler (corregir por reversión), Kimball (hechos tardíos) y Golfarelli y Rizzi (2007), que separan tiempo de transacción y tiempo válido, de quienes solo se leyó el resumen.

## Cada cuánto hay que extraer

Fowler sostiene que «many reporting needs work perfectly well with yesterday's data». En un BI de gestión suele ser cierto: el margen del mes o la antigüedad de saldos no cambian de decisión por unas horas (lectura de esta base). La copia de cambios en flujo se justifica cuando una decisión depende de lo que pasó hace minutos, o cuando la carga completa ya tarda demasiado y el origen no tiene una fecha de modificación confiable ([ingesta](../../Ingesta-y-transformacion/ingesta.md#la-latencia-que-hace-falta-decide)).

## Cómo falla la extracción

- Las anulaciones no llegan. El BI muestra ventas ya anuladas porque la extracción no trae notas de crédito, o filtra «confirmadas» y la anulada cambió de estado.
- Octubre cambia en diciembre. Un movimiento con fecha pasada o un período reabierto mueve un total ya informado sin explicación.
- El análisis frena la facturación. La consulta pesada corre sobre la base en hora pico.
- La lógica mal copiada. Un importe se suma sin el signo del documento, o en la moneda de la operación y no en la de la empresa ([multiempresa y moneda en el BI](multiempresa-y-moneda-en-el-bi.md)).
- El lector olvidado. Un lector de cambios que nadie consume retiene el registro hasta llenar el disco.
