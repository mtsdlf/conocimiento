---
resumen: >-
  Los metadatos son los datos sobre los datos: qué significa cada columna, de qué tipo es, quién la
  mantiene y de dónde viene. El linaje es la parte de los metadatos que registra el camino de un
  dato, qué procesos lo leyeron y lo escribieron desde la fuente hasta el tablero.
estado: vigente
estabilidad: semi
fuentes:
  - "OpenLineage, Object model (según el resultado del buscador; versión 1.40.1 de la documentación): https://openlineage.io/docs/spec/object-model"
  - "OpenLineage, Facets (según el resultado del buscador): https://openlineage.io/docs/spec/facets/"
  - "DAMA-DMBOK2, cap. Metadata Management (Technics Publications), no leído: https://technicspub.com/dmbok2"
  - "Datos/.investigacion/gobierno-y-privacidad.md"
aliases: [metadatos, metadata, linaje, linaje de datos, data lineage, catálogo de datos, data catalog, diccionario de datos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Metadatos y linaje

Los metadatos son los datos sobre los datos: qué significa cada columna, de qué tipo es, quién la mantiene y de dónde viene. El linaje es la parte de los metadatos que registra el camino de un dato, qué procesos lo leyeron y lo escribieron desde la fuente hasta el tablero.

Dentro de [Gobierno y calidad](gobierno-y-calidad.md) contestan la pregunta que aparece cuando un número no cierra: ¿de dónde salió esto? Sin metadatos, la única forma de saber qué cuenta la columna `total` es preguntarle a quien armó la tabla, si todavía está.

## Tres formas de los metadatos, de la planilla al catálogo

Los metadatos crecen con el negocio, y cada forma sirve en su tamaño (lectura de la base):

| Forma | Qué guarda | Cuándo alcanza |
|---|---|---|
| Diccionario de datos | Una fila por columna: nombre, qué significa, tipo, valores posibles, quién la mantiene, de qué sistema viene | Un comercio con unas pocas tablas y una persona que las mira; puede ser una planilla |
| Catálogo de datos | El diccionario de todas las tablas, buscable, con dueño, descripción y uso, casi siempre armado leyendo las bases de forma automática | Varias fuentes y varias personas que buscan datos sin conocer cada tabla |
| Linaje | Qué proceso leyó qué tabla y escribió cuál, y cuándo | Cuando hay transformaciones encadenadas y hace falta saber qué rompe un cambio |

El diccionario es lo primero que conviene escribir, y lo más barato. Lo que hay que anotar sobre todo es el significado: que `fecha` es la de pago y no la de pedido, que `total` incluye el envío, que un pedido cancelado sigue en la tabla con otro estado. Esos detalles son los que hacen que dos personas lleguen a números distintos. El significado de una métrica (no de una columna) va un paso más arriba, en la [definición de métrica](../Analitica-de-producto/definicion-de-metrica.md) y la [capa semántica](../Visualizacion-y-BI/capa-semantica.md).

Los metadatos también dicen de quién es cada dato. La columna «quién la mantiene» del diccionario es donde queda escrito el dueño o el cuidador del que habla la [entrada de la vertical](gobierno-y-calidad.md#un-dueño-y-un-cuidador-por-conjunto-de-datos).

> [!NOTE]
> Sin fuente todavía: una definición canónica de metadatos, catálogo y linaje en una fuente primaria general. Está en el capítulo de gestión de metadatos del DMBOK2, que no se leyó. La tabla de formas es una propuesta de la base.

## El linaje se registra como ejecuciones que leen y escriben

El linaje se arma registrando cada ejecución de cada proceso. OpenLineage, una especificación abierta para recogerlo, se describe como «an open framework for data lineage collection and analysis» y modela tres cosas (según el resultado del buscador sobre su documentación):

- el **conjunto de datos** (*dataset*), una tabla o un archivo;
- el **trabajo** (*job*), un proceso que se repite, como la carga diaria de pedidos;
- la **ejecución** (*run*), cada vez que ese trabajo corre.

Cada ejecución avisa qué conjuntos leyó y cuáles escribió. Encadenando esos avisos sale el grafo: la tabla de pedidos de la tienda alimenta la tabla limpia de ventas, que alimenta la tabla de ventas por día, que alimenta el tablero. A cada pieza se le pueden colgar datos extra, como el esquema de una tabla o la consulta SQL de un trabajo; la especificación los llama *facets*.

El linaje sirve en las dos direcciones. Hacia atrás, para encontrar la causa: el número del tablero está mal, ¿qué tabla de origen cambió? Hacia adelante, para medir el impacto: si se cambia una columna en la base de la aplicación, ¿qué tableros se rompen? Cuando un [test de datos](calidad-de-datos.md) falla, es el linaje el que dice quién tiene que enterarse.

Los procesos que el linaje registra son los que arma [Ingesta y transformación](../Ingesta-y-transformacion/ingesta-y-transformacion.md), y el orden en que corren lo lleva la [orquestación](../Ingesta-y-transformacion/orquestacion.md). Muchas herramientas de transformación y de orquestación generan el linaje solas, porque ya saben qué lee y qué escribe cada paso (lectura de la base).

## Cómo falla

Un diccionario que nadie actualiza es peor que no tenerlo, porque se le cree. La regla práctica es que el diccionario se cambia en el mismo momento que la tabla, por la misma persona (lectura de la base). El linaje falla por los huecos: el paso que alguien hace a mano en una planilla y vuelve a subir no deja rastro, y es justo el que suele introducir el error.

En un negocio chico, el linaje entero cabe en un dibujo: de qué sistemas salen los datos (la tienda, el punto de venta, el sistema de gestión), qué planilla o proceso los junta y qué tablero los muestra. Ese dibujo, con una fecha, alcanza hasta que haya transformaciones encadenadas que nadie recuerde.
