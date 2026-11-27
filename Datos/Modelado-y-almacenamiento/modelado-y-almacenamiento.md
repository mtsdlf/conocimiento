---
resumen: >-
  Modelado y almacenamiento es la parte de Datos que decide dónde se guarda el dato y con qué forma:
  la base de la aplicación o una copia para analizar, tablas normalizadas o un modelo de hechos y
  dimensiones, y un almacén analítico cuando hace falta.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Kleppmann, Designing Data-Intensive Applications, cap. 3 (1ª ed.), sección Transaction Processing versus Analytics, según resúmenes secundarios: https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/ch03.html"
  - "Kimball Group, Dimensional Modeling Techniques: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/"
  - "Jordan Tigani, Big Data is Dead (c. 2023): https://motherduck.com/blog/big-data-is-dead/"
  - "Datos/.investigacion/modelado-e-ingesta.md"
  - "Datos/.investigacion/posicion-contraria.md (sección 2)"
aliases: [almacenamiento de datos, modelado de datos, data modeling, data storage]
creado: 2026-11-27
revisado: 2026-11-27
---

# Modelado y almacenamiento

Modelado y almacenamiento es la parte de Datos que decide dónde se guarda el dato y con qué forma:
la base de la aplicación o una copia para analizar, tablas normalizadas o un modelo de hechos y
dimensiones, y un almacén analítico cuando hace falta.

Es el primer tramo del recorrido del dato. Lo que se guarda acá lo mueve
[Ingesta y transformación](../Ingesta-y-transformacion/ingesta-y-transformacion.md), lo
cuidan las reglas de [Gobierno y calidad](../Gobierno-y-calidad/gobierno-y-calidad.md) y lo
consulta el [Análisis](../Analisis/analisis.md). Las bases donde corre la aplicación de un negocio
en la nube, con su redundancia y su acceso privado, son de
[datos operacionales](../../Cloud/Datos-operacionales/datos-operacionales.md) en Cloud; acá
interesan por lo que se puede analizar de ellas.

## Cuándo hace falta un almacén aparte y cuándo no

La mayoría de los negocios chicos no necesita un almacén analítico para empezar. Las cifras sobre
cuánto dato tiene una empresa típica, y por qué vienen de un argumento de parte, están en
[cuánta infraestructura necesita un negocio chico](../datos.md#cuánta-infraestructura-necesita-un-negocio-chico).
Para un comercio con unos miles de ventas por mes, la planilla o la base de la propia tienda
alcanzan, y una base relacional común aguanta muchas consultas de análisis (lectura de la base).

El almacén aparte se justifica por tres razones. Una: hay varias fuentes que
cruzar (la tienda, el sistema de pagos, la planilla de costos) y ninguna las tiene juntas. Dos: las
consultas de análisis frenan la aplicación que atiende a los clientes. Tres: varias personas
consultan los mismos números y necesitan una sola versión. Las tres son criterio de la base y no
un umbral medido: no hay una fuente que diga en qué volumen una base común deja de alcanzar.

## Las cuatro decisiones de esta vertical

Guardar para analizar pide decidir, en orden, cuatro cosas:

1. Dónde se consulta. La base de la aplicación está hecha para escribir y leer pocas filas; la
   de análisis, para recorrer muchas filas y pocas columnas. Es la diferencia entre
   [OLTP y OLAP](oltp-y-olap.md).
2. Con qué forma se guarda el registro original. El [modelo relacional](modelo-relacional.md)
   reparte los datos en tablas con claves y evita repetir lo mismo en cada fila.
3. Con qué forma se analiza. El [modelado dimensional](modelado-dimensional.md) reordena esas
   tablas en hechos (lo que se mide) y dimensiones (el contexto), con un grano declarado.
4. En qué almacén vive. Un data warehouse, un data lake o un lakehouse, que se comparan en
   [almacenes analíticos](almacenes-analiticos.md).

Lo que hace un usuario en una app o una tienda se guarda aparte, como una fila por cada acción: es
la [tabla de eventos](tabla-de-eventos.md), de donde sale la
[analítica de producto](../Analitica-de-producto/analitica-de-producto.md).

## Cómo falla el modelado

Falla de tres maneras que se ven después en el tablero. La primera es analizar sobre la base de la
aplicación hasta que se pone lenta para los clientes. La segunda es mezclar granos: una tabla con
filas por pedido y filas por producto suma dos veces el mismo importe, y Kimball pide que «different
grains must not be mixed in the same fact table». La tercera es montar un almacén en la nube antes
de tener una pregunta que lo necesite, con costo mensual y ningún usuario (lectura de la base).

## Qué hay adentro de modelado y almacenamiento

- [OLTP y OLAP](oltp-y-olap.md) — la base que atiende la aplicación contra la base para analizar, y por qué el patrón de consulta cambia cómo se guarda.
- [Modelo relacional](modelo-relacional.md) — tablas, claves y normalización, explicadas desde la planilla.
- [Modelado dimensional](modelado-dimensional.md) — hechos, dimensiones y grano según Kimball, y las escuelas que discrepan.
- [Almacenes analíticos](almacenes-analiticos.md) — data warehouse, data lake y lakehouse: qué es cada uno y de dónde viene.
- [Tabla de eventos](tabla-de-eventos.md) — cómo se registra lo que hace un usuario y el plan de tracking que la ordena.
- [Motores analíticos](motores-analiticos.md) — ficha con licencia y precio de lista de siete motores, al 2026-11-27.
