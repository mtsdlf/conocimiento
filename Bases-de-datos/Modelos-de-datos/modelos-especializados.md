---
resumen: >-
  Los modelos especializados organizan el dato para un solo tipo de pregunta: relaciones entre
  cosas (grafos), mediciones a lo largo del tiempo (series de tiempo), texto por relevancia
  (búsqueda full-text) y parecido entre elementos (vectores). Muchas veces una base relacional con
  su búsqueda de texto o una extensión alcanza.
estado: borrador
estabilidad: estable
fuentes:
  - "Neo4j, What is a graph database: https://neo4j.com/docs/getting-started/get-started-with-neo4j/graph-database/"
  - "PostgreSQL Documentation, 12.1 Introduction (Full Text Search): https://www.postgresql.org/docs/current/textsearch-intro.html"
  - "Elastic, Full-text search: https://www.elastic.co/docs/solutions/search/full-text (según un resumen)"
  - "pgvector, README: https://github.com/pgvector/pgvector"
  - "Tiger Data, TimescaleDB hypertables: https://www.tigerdata.com/docs/reference/timescaledb/hypertables (según un resultado del buscador; no se leyó la página)"
  - "modern-sql.com, The SQL standard: https://modern-sql.com/standard"
  - "Bases-de-datos/.investigacion/ (informes del 2026-11-27)"
aliases: [base de grafos, graph database, series de tiempo, time series database, búsqueda full-text, full-text search, base vectorial, vector database]
creado: 2026-11-27
revisado:
---

# Modelos especializados

Los modelos especializados organizan el dato para un solo tipo de pregunta: relaciones entre
cosas (grafos), mediciones a lo largo del tiempo (series de tiempo), texto por relevancia
(búsqueda full-text) y parecido entre elementos (vectores). Muchas veces una base relacional con
su búsqueda de texto o una extensión alcanza.

Son la cuarta familia de [modelos de datos](modelos-de-datos.md). En el sistema de un comercio casi
nunca son la base principal: acompañan a una [base relacional](base-relacional.md) que guarda
pedidos, clientes y stock, y resuelven una pregunta que esa base contesta mal o lento.

## Cuatro modelos, cuatro preguntas

| Modelo | Pregunta del comercio que resuelve | Cómo guarda el dato | Alternativa dentro de PostgreSQL |
|---|---|---|---|
| Grafos | "Quienes compraron esto también compraron..." a varios saltos | Nodos, relaciones con tipo y propiedades | Sin fuente leída (ver más abajo) |
| Series de tiempo | Ventas por minuto, temperatura de una cámara de frío | Mediciones con marca de tiempo, partidas por rango | La extensión TimescaleDB |
| Búsqueda full-text | Buscar "zapatillas running" en el catálogo y ordenar por relevancia | Índice de palabras normalizadas | La búsqueda de texto que trae el motor |
| Vectores | Productos parecidos a este, búsqueda por significado | Listas de números que representan cada elemento | La extensión pgvector |

## Grafos: cuando importa la relación

Según Neo4j, una base de grafos "stores data as nodes, relationships, and properties instead of in
tables or documents". Las relaciones son "named connections between two nodes", con un tipo y
propiedades propias. Sirve cuando las preguntas "revolve around the relationship between elements,
not the elements themselves".

En un comercio, cliente y producto son nodos, y "compró" es una relación. Recomendar productos
siguiendo compras de clientes parecidos a varios saltos es la pregunta típica. Neo4j sostiene que en
un grafo no hay uniones y que las relaciones se recorren directamente; es una afirmación del
fabricante, no contrastada con una fuente independiente.

El estándar SQL ya se movió hacia este lado: SQL:2023 agregó la parte "9075-16:2023 Property Graph
Queries (SQL/PGQ)", según modern-sql.com. Qué motores la implementan no se verificó.

## Series de tiempo: mediciones que solo crecen

Una serie de tiempo es una sucesión de mediciones con fecha y hora que casi nunca se modifican: se
agregan al final y se consultan por rango. Según la documentación de TimescaleDB, leída solo por el
buscador, un hypertable es una tabla de PostgreSQL que la extensión divide automáticamente en partes
por tiempo, y una consulta filtrada por fecha lee solo las partes de ese rango.

Para el comercio, las ventas diarias de un año entran cómodas en una tabla común con un
[índice](../SQL/indice.md) por fecha. Una extensión o una base dedicada se justifican con lecturas de
sensores o eventos por segundo; esa frontera es una inferencia, no un umbral de fuente.

## Búsqueda full-text: el motor ya la trae

PostgreSQL trae búsqueda de texto sin extensiones. La documentación la define como la capacidad de
"identify natural-language documents that satisfy a query, and optionally to sort them by relevance
to the query". Usa los tipos `tsvector` y `tsquery` y el operador `@@`.

La diferencia con `LIKE '%running%'` es grande. La búsqueda de texto reconoce formas de la misma
palabra ("satisfies" y "satisfy"), ordena por relevancia y puede usar índices, mientras que `LIKE` y
las expresiones regulares "tend to be slow because there is no index support". Para buscar en el
catálogo o en las notas de los pedidos de un comercio, esto alcanza.

Un motor aparte, como Elasticsearch, analiza e indexa los campos de texto con puntaje de relevancia
y puede combinarlo con búsqueda vectorial para búsqueda híbrida, según un resumen de su
documentación. Que convenga cuando la búsqueda es el producto principal o hay que afinar la
relevancia a fondo es una inferencia: la página leída no compara contra una base de datos.

## Vectores: buscar por parecido

Un vector es una lista de números que representa un elemento, por ejemplo la descripción de un
producto pasada por un modelo de IA. Dos productos parecidos tienen vectores cercanos, y buscar
"productos como este" es buscar los vectores más próximos.

pgvector es "Open-source vector similarity search for Postgres" y permite "Store your vectors with
the rest of your data". Por defecto la búsqueda es exacta ("perfect recall"). Con un índice pasa a
ser aproximada, que "trades some recall for speed": encuentra casi siempre los más cercanos, más
rápido.

Hay dos índices. HNSW da mejor relación entre velocidad y precisión, pero tarda más en construirse y
usa más memoria; IVFFlat se construye más rápido y consulta peor. Un vector admite hasta 16.000
dimensiones, pero para indexar el tipo `vector` el tope es 2.000. El argumento del proyecto es que
los vectores quedan con "ACID compliance, point-in-time recovery, JOINs, and all of the other great
features of Postgres".

## Cuándo alcanza la base relacional

Ninguna fuente leída da un umbral, así que lo que sigue es una conclusión propia apoyada en lo
citado:

- **Texto**: el full-text de PostgreSQL alcanza para un catálogo o un buscador interno. Un motor
  aparte entra cuando la búsqueda es el producto.
- **Vectores**: pgvector alcanza si ya se usa PostgreSQL y se quieren los vectores junto al resto de
  los datos y dentro de las mismas [transacciones](../Transacciones/transacciones.md).
- **Series de tiempo**: una tabla con índice por fecha alcanza para ventas; TimescaleDB mantiene SQL
  y las demás tablas cuando el volumen crece.
- **Grafos**: sin respuesta todavía.

Cada base extra es un sistema más para operar, respaldar y mantener sincronizado con la principal.
Ese costo entra en los [criterios de elección](../Elegir-una-base/criterios-de-eleccion.md).

> [!NOTE]
> Sin fuente todavía: grafos dentro de una base relacional (consultas recursivas o extensiones) y
> una fuente sobre grafos independiente del fabricante; una lectura directa de la documentación de
> TimescaleDB o InfluxDB y el umbral desde el que una tabla común deja de alcanzar para series de
> tiempo; la frontera entre el full-text de PostgreSQL y un motor como Elasticsearch u OpenSearch;
> un umbral de volumen para pgvector y una comparación con una base vectorial dedicada.
