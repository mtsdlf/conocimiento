---
resumen: >-
  La capa semántica es el lugar donde las métricas y dimensiones de un negocio se definen una sola
  vez, por encima de las tablas, para que todas las herramientas que consultan usen la misma
  definición.
estado: borrador
estabilidad: estable
fuentes:
  - "dbt Docs, Semantic Layer (según su resumen): https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl"
  - "dbt Docs, Metrics: types and definition components (según su resumen): https://docs.getdbt.com/docs/build/metrics-overview"
  - "Google Cloud, What is LookML (según su resumen): https://docs.cloud.google.com/looker/docs/what-is-lookml"
  - "Microsoft Learn, Semantic models in the Power BI service (actualizada el 2026-04-28, leída entera): https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand"
  - "Apache Superset, README (según su resumen): https://github.com/apache/superset"
  - "Datos/.investigacion/metricas-y-visualizacion.md (sección 5)"
aliases: [semantic layer, modelo semántico, semantic model, capa de métricas, metrics layer]
creado: 2026-11-27
revisado:
---

# Capa semántica

La capa semántica es el lugar donde las métricas y dimensiones de un negocio se definen una sola
vez, por encima de las tablas, para que todas las herramientas que consultan usen la misma
definición.

Es la [definición de métrica](../Analitica-de-producto/definicion-de-metrica.md) puesta en un
sistema. La definición es el contenido: numerador, denominador, ventana, filtros. La capa semántica
es donde ese contenido se escribe una vez y se ejecuta cada vez que alguien pide el número. La
relación es una inferencia de la base: la lista de parámetros que pide una herramienta de capa
semántica es, pieza por pieza, una definición de métrica.

## El problema que resuelve: tres tableros, tres números

Sin capa semántica, cada tablero, cada planilla y cada consulta calcula la métrica por su cuenta.
El tablero de ventas resta devoluciones, el de marketing no, y la planilla de la dirección cuenta
por fecha de pedido. Los tres dicen «ventas» y ninguno coincide. Con una capa semántica, la métrica
«ventas» existe en un solo lugar y las tres herramientas la piden por su nombre (ejemplo de la
base).

La documentación de dbt lo dice así: su capa semántica "lets data teams define metrics (such as
revenue) on top of existing dbt models"; como la definición vive en la capa de modelado y no en la
de BI, todas las herramientas usan la misma, y si cambia, cambia en todas.

## De qué está hecha

Una capa semántica describe tres cosas sobre las tablas (lectura de la base, a partir de las
documentaciones):

- Dimensiones: los atributos por los que se corta un número, como fecha, canal, categoría o
  provincia.
- Medidas y métricas: las agregaciones (suma del importe, conteo de clientes distintos) y las
  métricas que se arman con ellas, con sus filtros.
- Relaciones: cómo se unen las tablas, para que quien consulta no tenga que escribir los joins.

Con eso, la herramienta genera la consulta. Según su documentación, el lenguaje de modelado de
Looker describe dimensiones, agregados, cálculos y relaciones, y Looker genera el SQL; el usuario de
negocio consulta sin escribirlo. Las dimensiones y las tablas de hechos que la capa necesita son las
del [modelado dimensional](../Modelado-y-almacenamiento/modelado-dimensional.md).

## En qué capa vive

Hay dos lugares posibles, y la diferencia importa (lectura de la base):

| Dónde | Ventaja | Costo |
|---|---|---|
| En la herramienta de BI | Viene incluida y se arma con la herramienta | Solo la usa esa herramienta; una planilla o un segundo BI calculan aparte |
| En la capa de modelado, antes del BI | Todas las herramientas leen la misma definición | Una pieza más que mantener, y en algunos casos un plan pago |

Las herramientas de BI traen su propio modelo semántico. La documentación de Microsoft, leída entera,
dice que un modelo semántico de Power BI "represent[s] a source of data that's ready for reporting
and visualization", que antes se llamaba «dataset» y que admite seguridad por filas. Superset se
describe con "a lightweight semantic layer". dbt, en cambio, pone la definición en la capa de
modelado para que la compartan todas.

> [!IMPORTANT]
> No hay una fuente neutral que defina «capa semántica»: todas las leídas son de proveedores, y cada
> una la ubica donde vende su producto. La página de Looker ni siquiera usa el término. Quien define
> la métrica en la herramienta de BI queda atado a ella; quien la define en la capa de modelado suma
> una pieza. Cuál conviene depende de cuántas herramientas leen los mismos números (lectura de la
> base).

## Cuándo la necesita un negocio chico

Un comercio con una sola persona que arma los reportes no necesita un sistema: necesita una hoja con
cada métrica escrita según la [definición de métrica](../Analitica-de-producto/definicion-de-metrica.md),
y que todos los reportes la respeten. El modelo semántico de la propia herramienta de BI alcanza
mientras haya una sola. La capa en el modelado se justifica cuando varias herramientas o varias
personas leen los mismos números y empiezan a no coincidir (lectura de la base). De dónde sale cada
dato que la capa usa es tema de [metadatos y linaje](../Gobierno-y-calidad/metadatos-y-linaje.md).

Para ver el concepto con un ejemplo escrito, la documentación de la capa semántica de dbt junto con
su página de métricas muestra cada parámetro de una definición. Conviene leerla sabiendo que es de
un proveedor. Qué herramienta trae qué está en la [ficha de herramientas de BI](herramientas-de-bi.md).
