---
tipo: concepto
resumen: >-
  Los servicios de datos operacionales de Azure: Storage Accounts para objetos y archivos, Azure
  SQL para relacional, Cosmos DB para NoSQL distribuido, PostgreSQL y MySQL Flexible Server, y
  Azure Managed Redis como cache; qué resuelve cada uno y cuándo se elige.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Azure Storage redundancy: https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy"
  - "Microsoft Learn, Access tiers for blob data: https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview"
  - "Microsoft Learn, What is Azure SQL?: https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview"
  - "Microsoft Learn, Consistency levels in Azure Cosmos DB: https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels"
  - "Microsoft Learn, Azure Database for PostgreSQL overview: https://learn.microsoft.com/en-us/azure/postgresql/overview"
  - "Microsoft Learn, Azure Cache for Redis retirement FAQ: https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Datos, SQL vs Cosmos y gotchas)"
aliases: [Storage Account, Azure SQL, Cosmos DB, PostgreSQL Flexible Server, Azure Managed Redis, Azure Cache for Redis]
parte_de: []
requiere: []
relacionado: []
---

# Almacenamiento y bases de datos en Azure

Los servicios de datos operacionales de Azure: Storage Accounts para objetos y archivos, Azure
SQL para relacional, Cosmos DB para NoSQL distribuido, PostgreSQL y MySQL Flexible Server, y
Azure Managed Redis como cache; qué resuelve cada uno y cuándo se elige.

## Por qué importa

El dato es lo más difícil de mover después. El modelo (relacional o documentos), la redundancia y
la clave de partición se eligen al principio y cambiarlos implica migrar.

## Cómo funciona

| Servicio | Se elige cuando | Lo que hay que decidir |
|---|---|---|
| **Storage Account** (Blob, Files, ADLS Gen2) | Objetos, archivos, data lake | Redundancia y tier de acceso; versionado y borrado suave |
| **Azure SQL Database** | Relacional, transacciones ACID, JOINs | Serverless (se pausa en dev) o provisionado; Hyperscale para crecer hasta 128 TB |
| **Azure SQL Managed Instance** | Migrar un SQL Server con funciones de instancia | Vive en una VNet propia; hasta 16 TB |
| **Cosmos DB** | Baja latencia global, esquema flexible, varias regiones | Clave de partición y nivel de consistencia |
| **PostgreSQL / MySQL Flexible Server** | Motor abierto administrado | HA por zona y réplicas de lectura |
| **Azure Managed Redis** | Cache, sesiones, rate limiting | Reemplaza a Azure Cache for Redis |

- **Redundancia de Storage**: LRS (tres copias en un datacenter), ZRS (en tres zonas), GRS y GZRS
  (más una copia en la región secundaria). Solo las variantes RA- dejan leer la secundaria.
- **Tiers de blob**: Hot, Cool (mínimo 30 días), Cold (90) y Archive (180, fuera de línea, hasta
  15 horas para rehidratar). Una lifecycle policy mueve los blobs entre tiers por antigüedad.
- **Cosmos DB**: la clave de partición tiene que tener muchos valores y repartir la carga pareja;
  una mala clave crea particiones calientes. Hay cinco niveles de consistencia, de Strong a
  Eventual; Session es el más usado.
- **Retiros**: Azure Cache for Redis Enterprise se retira el 31 de marzo de 2027 y los tiers
  Basic, Standard y Premium el 30 de septiembre de 2028; el reemplazo es Azure Managed Redis.
- **Acceso**: todos admiten [Private endpoint](private-endpoint.md) y acceso público apagado.

## Ejemplo

Un e-commerce guarda pedidos en Azure SQL (transacciones entre pedido, pago y stock), el catálogo
en Cosmos DB con clave de partición por categoría para leerlo rápido en varias regiones, las
imágenes en Blob con tier Cool para las de productos discontinuados y las sesiones en Managed
Redis.

## No confundir con

La analítica (Data Lake, Databricks, Fabric): procesa grandes volúmenes para reportes. Estos
servicios atienden a la aplicación en línea.

## Relaciones

- La usa: [Alta disponibilidad y DR en Azure](alta-disponibilidad-y-dr-en-azure.md) — la réplica de cada servicio de datos.
- La usa: [Arquitecturas de referencia en Azure](arquitecturas-de-referencia-en-azure.md) — los datos detrás de cada patrón.
