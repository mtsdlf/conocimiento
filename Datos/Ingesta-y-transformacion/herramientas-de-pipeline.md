---
resumen: >-
  Qué hace, con qué licencia y a qué precio de lista se ofrecen seis herramientas de ingesta,
  transformación y orquestación de datos, leídas el 2026-11-27.
estado: vigente
estabilidad: volatil
fuentes:
  - "Airbyte, pricing y repo: https://airbyte.com/pricing; https://github.com/airbytehq/airbyte"
  - "Fivetran, pricing: https://www.fivetran.com/pricing"
  - "dbt, documentación y repo de dbt Core: https://docs.getdbt.com/docs/introduction; https://github.com/dbt-labs/dbt-core"
  - "Apache Airflow, repo: https://github.com/apache/airflow"
  - "Dagster, pricing y repo: https://dagster.io/pricing; https://github.com/dagster-io/dagster"
  - "Prefect, pricing y repo: https://www.prefect.io/pricing; https://github.com/PrefectHQ/prefect"
  - "Debezium, sitio oficial: https://debezium.io/"
  - "Datos/.investigacion/modelado-e-ingesta.md (secciones 7 y 10)"
aliases: [herramientas de ETL, herramientas de ELT, orquestadores]
creado: 2026-11-27
revisado: 2026-11-27
---

# Herramientas de pipeline

Qué hace, con qué licencia y a qué precio de lista se ofrecen seis herramientas de ingesta,
transformación y orquestación de datos, leídas el 2026-11-27.

Implementan la [ingesta](ingesta.md), la [transformación](etl-y-elt.md) y la
[orquestación](orquestacion.md). Si un negocio chico necesita alguna está en [ingesta y
transformación](ingesta-y-transformacion.md).

Copiado de la página de precios y del repositorio de cada herramienta el 2026-11-27. Son precios de
lista en USD; ninguna fila es una comparación con método, son las páginas de cada proveedor.

| Herramienta | Qué hace | Licencia | Precio de lista | Fuente |
|---|---|---|---|---|
| Airbyte | ingesta con conectores (ELT) | el repo muestra MIT y Elastic License v2; qué parte va con cuál no quedó confirmado | autoalojado gratis; Cloud Standard desde 20 por mes (5 créditos, cerca de 1 GB sincronizado); Plus desde 189 por mes (40 créditos); Pro y Enterprise Flex a cotización; prueba de 14 días con 400 créditos | [precios](https://airbyte.com/pricing) |
| Fivetran | ingesta administrada | propietaria | planes Free, Standard, Enterprise y Business Critical. Free: 500.000 filas activas por mes. Standard: 5 de base de 1 a 1 millón de filas activas, decreciente con el volumen; transformaciones a 0,01 por ejecución de modelo entre 5.001 y 30.000 | [precios](https://www.fivetran.com/pricing) |
| dbt | transformación en SQL adentro del almacén | dbt Core, Apache 2.0; la relación entre Core y el motor nuevo en Rust no quedó clara | gratis de usar; lo de la plataforma pide cuenta, gratis o paga | [documentación](https://docs.getdbt.com/docs/introduction) |
| Airflow | orquestación | Apache-2.0 | gratis, autoalojado; versión 3.4.0 | [repo](https://github.com/apache/airflow) |
| Dagster | orquestación centrada en las tablas que produce | Apache-2.0 | Cloud: Solo 10 por mes, Starter 100 por mes, Pro a cotización; crédito a 0,040 (Solo) y 0,035 (Starter) por uso; prueba de 30 días | [precios](https://dagster.io/pricing) |
| Prefect | orquestación en Python | Apache-2.0 | Cloud: Hobby gratis (2 usuarios, 5 deployments); Starter 100 por mes; Team 100 por usuario por mes; Enterprise a cotización | [precios](https://www.prefect.io/pricing) |

Para copiar cambios de una base (CDC), [Debezium](https://debezium.io/) es abierto, con licencia
Apache 2.0; su última versión estable al 2026-11-27 es 3.7.1.Final.

Dos cosas que las páginas no dejan claras: en Airbyte, los 5 créditos por 1 GB del plan Standard no
cuadran con los 400 créditos por 100 GB de la prueba, como señala la misma página; y en dbt, qué es
Core y qué es la versión nueva.
