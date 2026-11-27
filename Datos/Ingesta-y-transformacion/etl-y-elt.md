---
resumen: >-
  ETL y ELT son dos órdenes para el mismo trabajo: en ETL el dato se transforma antes de cargarlo
  en el almacén; en ELT se carga crudo y se transforma después, adentro del almacén.
estado: vigente
estabilidad: estable
fuentes:
  - "dbt Labs (Daniel Poppy), Understanding ELT: Extract, Load, Transform (6 sep. 2023): https://www.getdbt.com/blog/extract-load-transform"
  - "O'Reilly, Understanding ETL, edición actualizada, distribuida por Databricks (vía buscador): https://www.databricks.com/sites/default/files/2025-08/Understanding_ETL_Updated-edition.pdf"
  - "Joe Reis y Matt Housley, Fundamentals of Data Engineering, cap. 7, sección ETL versus ELT (O'Reilly, 2022); no leído"
  - "Datos/.investigacion/modelado-e-ingesta.md (sección 8 y sobre la división del árbol)"
aliases: [ETL, ELT, transformación de datos, extract transform load, extraer transformar cargar]
creado: 2026-11-27
revisado: 2026-11-27
---

# ETL y ELT

ETL y ELT son dos órdenes para el mismo trabajo: en ETL el dato se transforma antes de cargarlo
en el almacén; en ELT se carga crudo y se transforma después, adentro del almacén.

Las letras son *extract*, *transform* y *load*: extraer del origen, transformar y cargar. La
extracción y la carga son la [ingesta](ingesta.md); la transformación es lo que convierte tablas
crudas en el [modelo dimensional](../Modelado-y-almacenamiento/modelado-dimensional.md) que se
analiza. Es la pieza del medio de [ingesta y
transformación](ingesta-y-transformacion.md).

## Qué se hace al transformar

Transformar es todo lo que pasa entre la copia cruda y la tabla que usa un tablero. En una tienda,
por ejemplo:

- Limpiar: sacar pedidos de prueba, unificar «CABA», «Capital» y «C.A.B.A.», convertir fechas.
- Unir: juntar pedidos de la tienda con pagos del procesador por número de pedido.
- Calcular: importe neto de descuentos y devoluciones, margen con el costo de cada producto.
- Dar forma: armar la tabla de hechos de ventas con su grano y las dimensiones de cliente y
  producto.

Es el mismo trabajo que la [limpieza de datos](../Analisis/limpieza-de-datos.md) del análisis, pero
escrito una vez y corrido siempre, en lugar de repetido a mano en cada planilla (lectura de la
base).

## Transformar antes o después de cargar

En ETL, según un artículo de dbt Labs, «data is transformed before being loaded into the data
warehouse»; en ELT, «raw data is loaded first and transformations are applied later». ETL era el
método más común hacia el data warehouse relacional, y ELT «has become popular, especially with data
lakes», según el extracto del buscador de una guía de O'Reilly.

| | ETL | ELT |
|---|---|---|
| Dónde se transforma | en un servidor o herramienta aparte, antes del almacén | adentro del almacén, casi siempre con SQL |
| Qué queda en el almacén | solo lo transformado | lo crudo y lo transformado |
| Si una regla estaba mal | hay que volver a extraer del origen | se vuelve a transformar desde lo crudo |

Las filas de la tabla, salvo la definición de cada orden, son lectura de la base.

ELT ganó terreno con la nube, porque el almacén ofrece almacenamiento y cómputo a demanda y permite
«perform transformations at scale using the cloud's vast computational resources», según dbt Labs.
Quien lo afirma vende una herramienta de ELT. Como la transformación queda en SQL adentro del
almacén, la puede escribir quien analiza (lectura de la base); quién se ocupa de ese tramo se cuenta en [roles de
datos](../Fundamentos/roles-de-datos.md).

## Cuándo conviene cada uno

ELT conviene cuando el almacén es potente y barato de consultar, y cuando se quiere poder rehacer
una transformación sin volver al origen. ETL sigue teniendo sentido cuando no se puede guardar el
dato crudo, por ejemplo porque trae datos personales que no deberían llegar al almacén y hay que
quitarlos antes; qué datos personales se pueden guardar está en [privacidad de datos
personales](../Gobierno-y-calidad/privacidad-de-datos-personales.md). Los dos criterios son
lectura de la base.

En un negocio chico la frontera se borra: una consulta SQL programada sobre la base de la tienda, o
una vista, ya es una transformación. Lo que importa es que las reglas estén escritas en un solo
lugar, que es la misma idea de la [capa semántica](../Visualizacion-y-BI/capa-semantica.md) para las
métricas.

> [!NOTE]
> Sin fuente todavía: una crítica a ELT con método (costo de cómputo, almacenes llenos de tablas
> crudas sin dueño); solo se encontraron posiciones de proveedores.

## Dónde se lee la versión larga

Reis y Housley, *Fundamentals of Data Engineering*, cap. 7, sección «ETL versus ELT»; no se pudo
leer y la recomendación sale de la estructura del capítulo. Como alternativa abierta, el artículo de
dbt Labs sobre ELT, leído sabiendo que lo escribe el proveedor que defiende ese orden. Las
herramientas de transformación están en la ficha de [herramientas de
pipeline](herramientas-de-pipeline.md).
