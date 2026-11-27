---
resumen: >-
  OLTP es el trabajo de la base que atiende a la aplicación (muchas transacciones chicas, de pocas
  filas cada una) y OLAP el de la base para analizar (pocas consultas que recorren muchas filas y
  pocas columnas); por esa diferencia, el análisis se hace sobre una copia.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Kleppmann, Designing Data-Intensive Applications, cap. 3 (1ª ed.) / cap. 4 (2ª ed.), secciones Transaction Processing versus Analytics y Column-Oriented Storage; no leído, estructura y resumen vía buscador: https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/ch03.html"
  - "Henrik Warne, reseña de Designing Data-Intensive Applications (2019): https://henrikwarne.com/2019/07/27/book-review-designing-data-intensive-applications/"
  - "Stonebraker et al., C-Store: A Column-oriented DBMS, VLDB 2005, pp. 553-564 (cita vía buscador): https://dblp.org/rec/conf/vldb/StonebrakerABCCFLLMOORTZ05.html"
  - "Google Cloud, Introducción a BigQuery: https://docs.cloud.google.com/bigquery/docs/introduction"
  - "Datos/.investigacion/modelado-e-ingesta.md (secciones 1 y 4)"
aliases: [OLTP, OLAP, transaccional y analítico, base transaccional, base analítica]
creado: 2026-11-27
revisado:
---

# OLTP y OLAP

OLTP es el trabajo de la base que atiende a la aplicación (muchas transacciones chicas, de pocas
filas cada una) y OLAP el de la base para analizar (pocas consultas que recorren muchas filas y
pocas columnas); por esa diferencia, el análisis se hace sobre una copia.

Las siglas vienen de *online transaction processing* y *online analytical processing*. Es la
primera decisión de [modelado y almacenamiento](modelado-y-almacenamiento.md): de qué base sale un
número.

## Dos maneras de leer la misma tabla de pedidos

Una tienda online guarda sus pedidos en una tabla con veinte columnas: número, cliente, fecha,
dirección, medio de pago, estado, importe y otras. La aplicación hace consultas de un tipo: trae el
pedido 48.213 entero para mostrarlo, o cambia su estado a «enviado». Toca una fila y casi todas sus
columnas, y lo hace miles de veces por día, cada vez en milisegundos.

El análisis pregunta otra cosa: cuánto se vendió por mes en los últimos dos años. Esa consulta
recorre todas las filas y usa dos columnas, fecha e importe. Según los resúmenes secundarios del
libro de Kleppmann, OLTP sirve a usuarios finales con transacciones chicas, y OLAP agrega valores
de millones de registros.

| | OLTP (la aplicación) | OLAP (el análisis) |
|---|---|---|
| Quién consulta | la aplicación, por cada cliente | una persona o un tablero |
| Qué lee | pocas filas, casi todas las columnas | muchas filas, pocas columnas |
| Qué escribe | altas y cambios todo el tiempo | cargas por tandas |
| Qué importa | que cada operación sea rápida y no se pierda | que la suma de millones de filas tarde poco |

Las dos últimas filas de la tabla son lectura de la base.

## Por qué se analiza sobre una copia

Una consulta que recorre dos años de pedidos ocupa a la base que, al mismo tiempo, tiene que cobrar
el pedido de un cliente. Por eso el análisis se hace sobre una copia de solo lectura: el data warehouse,
según el mismo resumen, evita que las consultas analíticas interfieran con la producción. Llevar los
datos hasta esa copia es la [ingesta](../Ingesta-y-transformacion/ingesta.md).

En un negocio chico la separación puede esperar. Si la base de la tienda tiene unas decenas de
miles de pedidos, una consulta de análisis tarda poco y no molesta (lectura de la base). Una réplica
de lectura de la misma base es un paso intermedio común antes de un almacén aparte (lectura de la base). Cuándo conviene
dar el salto está en la entrada de la vertical.

## Por qué el almacén analítico guarda por columnas

El patrón de lectura cambia cómo se guarda el dato en el disco. Una base transaccional guarda cada
fila junta, porque casi siempre la necesita entera (lectura de la base). Un motor analítico guarda cada columna junta: el
paper de C-Store (2005) lo explica con que la base «need only read the values of columns required
for processing a given query» (cita tomada del buscador). La documentación de un warehouse en la
nube lo describe igual: guarda los datos «in columns rather than rows», optimizado para consultas
analíticas.

Para la consulta de ventas por mes, guardar por columnas significa leer dos columnas de veinte. Las
columnas, además, se comprimen bien porque repiten valores (lectura de la base). Qué almacenes funcionan así está en
[almacenes analíticos](almacenes-analiticos.md), y los motores concretos en la ficha de
[motores analíticos](motores-analiticos.md).

## Dónde se lee la versión larga

El recurso canónico es el capítulo de almacenamiento de *Designing Data-Intensive Applications*, de
Martin Kleppmann: las secciones «Transaction Processing versus Analytics» y «Column-Oriented
Storage» (cap. 3 de la primera edición, cap. 4 de la segunda). Conviene fijarse en por qué leer
pocas filas con todas las columnas, o muchas filas con pocas, lleva a dos diseños de motor
distintos.

> [!NOTE]
> Sin fuente todavía: la definición literal de OLTP y OLAP en el texto de Kleppmann; el capítulo no
> se pudo leer y lo de arriba sale de resúmenes secundarios.

Las bases de una aplicación en la nube, con sus servicios y su redundancia, están en
[datos operacionales](../../Cloud/Datos-operacionales/datos-operacionales.md) de Cloud.
