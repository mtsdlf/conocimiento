---
resumen: >-
  Licencia, modelo de precio y precio de lista de siete motores para analizar datos, de los
  warehouses en la nube a los motores gratis que corren en una sola máquina, leídos el 2026-11-27.
estado: vigente
estabilidad: volatil
fuentes:
  - "Google Cloud, BigQuery pricing (no se pudo leer): https://cloud.google.com/bigquery/pricing"
  - "Snowflake, Service Consumption Table: https://snowflake.com/legal-files/CreditConsumptionTable.pdf"
  - "Snowflake, Understanding overall cost: https://docs.snowflake.com/en/user-guide/cost-understanding-overall"
  - "AWS, Amazon Redshift pricing: https://aws.amazon.com/redshift/pricing/"
  - "Databricks, pricing: https://www.databricks.com/product/pricing y https://www.databricks.com/product/pricing/databricks-sql"
  - "DuckDB, FAQ: https://duckdb.org/faq.html"
  - "PostgreSQL, About y License: https://www.postgresql.org/about/ y https://www.postgresql.org/about/licence/"
  - "ClickHouse, pricing: https://clickhouse.com/pricing; repo: https://github.com/ClickHouse/ClickHouse"
  - "Datos/.investigacion/modelado-e-ingesta.md (sección 6)"
aliases: [warehouses en la nube, precios de data warehouse]
creado: 2026-11-27
revisado: 2026-11-27
---

# Motores analíticos

Licencia, modelo de precio y precio de lista de siete motores para analizar datos, de los
warehouses en la nube a los motores gratis que corren en una sola máquina, leídos el 2026-11-27.

Implementan los [almacenes analíticos](almacenes-analiticos.md). Los warehouses en la nube guardan
por columnas, como explica [OLTP y OLAP](oltp-y-olap.md); PostgreSQL, en cambio, guarda por filas
(lectura de la base). Si un negocio chico necesita uno está en
[modelado y almacenamiento](modelado-y-almacenamiento.md).

Copiado de la página de precios o de licencia de cada proveedor el 2026-11-27. Son precios de lista
en USD, en la región US East salvo que se diga otra; cambian por región y por contrato, y la región
de Sudamérica no se buscó.

## Warehouses en la nube

| Motor | Modelo de precio | Precio de lista | Fuente |
|---|---|---|---|
| BigQuery | por TiB escaneado (bajo demanda) o por slot-hora (ediciones); almacenamiento por GiB (modelo también sin verificar) | sin verificar: la página oficial no cargó en tres intentos | [precios](https://cloud.google.com/bigquery/pricing) |
| Snowflake | créditos de cómputo más almacenamiento por TB; por segundo, con mínimo de 60 segundos; no cobra el ingreso de datos | por crédito: Standard 2,00; Enterprise 3,00; Business Critical 4,00; VPS 6,00. Almacenamiento 23,00 por TB/mes | [tabla de consumo](https://snowflake.com/legal-files/CreditConsumptionTable.pdf) |
| Redshift | Serverless por RPU-hora; provisionado por nodo-hora; almacenamiento por GB-mes | 0,375 por RPU-hora; nodo ra3.4xlarge 3,26 por hora; almacenamiento 0,024 por GB-mes; prueba de 300 por 90 días en Serverless | [precios](https://aws.amazon.com/redshift/pricing/) |
| Databricks | DBU (unidad normalizada de procesamiento) por segundo, más la infraestructura de la nube | sin verificar: la tarifa por DBU no cargó; prueba de 14 días | [precios](https://www.databricks.com/product/pricing) |
| ClickHouse Cloud | unidad de cómputo-hora (8 GiB de RAM y 2 vCPU) más almacenamiento; el código es Apache-2.0 | por unidad-hora en AWS us-east-1: Basic 0,21811; Scale 0,29846; Enterprise 0,39030. Almacenamiento 25,30 por TB/mes; prueba de 300 en créditos por 30 días | [precios](https://clickhouse.com/pricing) |

El PDF de Snowflake no muestra la fecha de vigencia de la versión en USD; según el buscador, la
versión en EUR dice «Pricing Updated: January 5, 2026».

## Motores gratis para empezar

| Motor | Licencia | Qué es | Fuente |
|---|---|---|---|
| DuckDB | MIT | motor de una sola máquina, dentro del programa o por línea de comandos; probado «on machines with 100+ CPU cores and terabytes of memory» | [FAQ](https://duckdb.org/faq.html) |
| PostgreSQL | PostgreSQL License | la base relacional de uso general, usada como warehouse chico; versión 19, publicada el 19 de noviembre de 2026 | [About](https://www.postgresql.org/about/) |

> [!NOTE]
> Sin fuente todavía: el precio de BigQuery y la tarifa por DBU de Databricks SQL, y una fuente
> sobre en qué volumen PostgreSQL deja de alcanzar como warehouse.
