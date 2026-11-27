---
resumen: >-
  Un índice es una estructura aparte, ordenada por una o más columnas, que deja encontrar filas sin
  recorrer la tabla entera; acelera las lecturas que filtran u ordenan por esas columnas y encarece
  cada escritura. EXPLAIN muestra si el motor lo usa.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 11.1 Index Types: https://www.postgresql.org/docs/current/indexes-types.html"
  - "PostgreSQL Documentation, 11.3 Multicolumn Indexes: https://www.postgresql.org/docs/current/indexes-multicolumn.html"
  - "PostgreSQL Documentation, 11.7 Indexes on Expressions: https://www.postgresql.org/docs/current/indexes-expressional.html"
  - "PostgreSQL Documentation, 14.1 Using EXPLAIN: https://www.postgresql.org/docs/current/using-explain.html"
  - "Markus Winand, Use The Index, Luke!, Concatenated Keys: https://use-the-index-luke.com/sql/where-clause/the-equals-operator/concatenated-keys"
  - "Markus Winand, Use The Index, Luke!, LIKE performance tuning: https://use-the-index-luke.com/sql/where-clause/searching-for-ranges/like-performance-tuning"
  - "Markus Winand, Use The Index, Luke!, Case-insensitive search: https://use-the-index-luke.com/sql/where-clause/functions/case-insensitive-search"
  - "Markus Winand, Use The Index, Luke!, Insert: https://use-the-index-luke.com/sql/dml/insert"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [index, índices, EXPLAIN, plan de ejecución, query plan, índice compuesto]
creado: 2026-11-27
revisado: 2026-11-27
---

# Índice

Un índice es una estructura aparte, ordenada por una o más columnas, que deja encontrar filas sin
recorrer la tabla entera; acelera las lecturas que filtran u ordenan por esas columnas y encarece
cada escritura. EXPLAIN muestra si el motor lo usa.

Funciona como el índice alfabético de un libro: para encontrar un tema no se lee el libro entero,
se busca en una lista ordenada que dice en qué página está. Cómo está hecho por dentro (el árbol B)
queda fuera del tema; acá importa cuándo se usa y cómo se ve.

## Qué mirar primero cuando una consulta tarda

Con 100 mil pedidos, buscar los de un cliente sin índice obliga a leer todos. Los planes de esta
sección salen de las tablas y el script de 100.000 pedidos de la
[ruta de SQL](../Fundamentos/ruta-de-sql.md#paso-8-tablas-e-índices). El primer paso es
pedirle el plan al motor con `EXPLAIN ANALYZE`:

```sql
EXPLAIN ANALYZE SELECT * FROM pedidos WHERE cliente_id = 42;
```

```
Seq Scan on pedidos  (cost=0.00..1887.05 rows=20 width=19) (actual time=0.048..22.328 rows=20.00 loops=1)
  Filter: (cliente_id = 42)
  Rows Removed by Filter: 99984
Execution Time: 22.408 ms
```

`Seq Scan` es un recorrido secuencial: leyó las 100.004 filas (los 4 pedidos del script
base más los 100.000 generados) y descartó 99.984 para quedarse con 20. Después de crear el índice:

```sql
CREATE INDEX pedidos_cliente_id_idx ON pedidos (cliente_id);
```

```
Bitmap Heap Scan on pedidos  (cost=4.45..74.07 rows=20 width=19) (actual time=0.051..0.110 rows=20.00 loops=1)
  Recheck Cond: (cliente_id = 42)
  ->  Bitmap Index Scan on pedidos_cliente_id_idx  (cost=0.00..4.44 rows=20 width=0)
        Index Cond: (cliente_id = 42)
Execution Time: 0.148 ms
```

El motor encontró las 20 filas en el índice y fue a buscar solo esas: de 22,4 a 0,15 milisegundos.
Son mediciones propias en PostgreSQL 18.4 con datos de prueba, el 2026-11-27; muestran el orden de
magnitud, no una cifra para comparar.

La lista para una consulta lenta, en orden:

1. Corré `EXPLAIN ANALYZE` y buscá un `Seq Scan` sobre una tabla grande con un `Filter` que descarta
   casi todo.
2. Mirá las columnas de ese filtro y de los joins: ¿tienen índice? Declarar una clave foránea, como las de
   [definir tablas](definir-tablas.md), no crea un índice: en las tablas de prueba, `pedidos.cliente_id` no tenía ninguno hasta crearlo.
3. Si tienen índice y no se usa, buscá una función o una conversión sobre la columna (abajo).
4. Si la consulta es rápida pero se ejecuta cientos de veces por pantalla, el problema no es el
   índice sino el [problema N+1](sql-desde-una-aplicacion.md#el-problema-n1).

## Leer un plan

`EXPLAIN` muestra el plan que eligió el planificador; `EXPLAIN ANALYZE` además lo ejecuta y agrega
los tiempos y las filas reales. Algunas claves para leerlo, de la documentación de PostgreSQL:

- **`cost`** está en "arbitrary units", no en milisegundos. El primer número es el costo hasta la
  primera fila y el segundo, hasta la última. Sirve para comparar planes entre sí.
- **`rows`** en la parte de `cost` es la estimación; en la parte de `actual`, lo que pasó. Una
  diferencia grande entre las dos indica que el planificador estimó mal.
- **Se lee de adentro hacia afuera**: las líneas con más sangría se ejecutan primero y le pasan
  filas a la de arriba.
- **`EXPLAIN ANALYZE` ejecuta de verdad**: "With this option, EXPLAIN actually executes the query".
  Para analizar un `UPDATE` o un `DELETE` sin cambiar datos, la documentación propone
  `BEGIN; EXPLAIN ANALYZE UPDATE ...; ROLLBACK;`.

## Cuándo el motor no usa el índice aunque exista

**Cuando la consulta trae muchas filas.** `WHERE cliente_id > 10` devuelve casi toda la tabla, y el
plan es `Seq Scan` aunque el índice exista: leer la tabla de corrido es más barato que saltar del
índice a la tabla cien mil veces. El planificador decide según cuántas filas estima.

**Cuando hay una función o una conversión sobre la columna.** El índice está ordenado por la
columna, no por lo que resulta de transformarla. Winand lo llama así: la función es "just a black
box" para el optimizador. Con un índice en `pedidos (fecha)`:

```sql
-- no usa el índice: Seq Scan
SELECT count(*) FROM pedidos WHERE fecha::date = '2025-06-01';

-- usa el índice: Index Only Scan using pedidos_fecha_idx
SELECT count(*) FROM pedidos WHERE fecha >= '2025-06-01' AND fecha < '2025-06-02';
```

La segunda forma dice lo mismo sin tocar la columna. Cuando la transformación es inevitable, como
buscar emails sin distinguir mayúsculas, PostgreSQL permite indexar la expresión:
`CREATE INDEX clientes_lower_email_idx ON clientes (lower(email));` hace que `WHERE lower(email) =
'...'` use el índice. El costo, según la documentación: estos índices "are relatively expensive to
maintain, because the derived expression(s) must be computed for each row insertion and non-HOT
update" (una actualización non-HOT es la que obliga a tocar también los índices de la tabla).

**Cuando un LIKE empieza con comodín.** Un índice sirve para `LIKE 'c42%'` (el comienzo está fijo)
pero no para `LIKE '%42@example.com'`. Winand: "Avoid LIKE expressions with leading wildcards".
Además, en PostgreSQL con una configuración regional distinta de C, el índice común no sirve ni para
`LIKE 'c42%'`: hace falta una clase de operador especial, como `CREATE INDEX ... ON clientes (email
text_pattern_ops)`. Se comprobó al ejecutarlo: sin esa clase el plan fue `Seq Scan`; con ella, un
recorrido del índice.

## El orden de las columnas en un índice compuesto

Un índice puede tener varias columnas, y el orden importa. Winand usa la guía telefónica: está
ordenada por apellido y después por nombre, así que sirve para buscar por apellido, o por apellido
y nombre, pero no solo por nombre. "In general, a database can use a concatenated index when
searching with the leading (leftmost) columns".

Con un índice en `pedidos (cliente_id, fecha)`:

- `WHERE cliente_id = 42 AND fecha >= '2025-06-01'` usa las dos columnas del índice.
- `WHERE cliente_id = 42` usa la primera.
- `WHERE fecha >= '2025-06-01' AND fecha < '2025-06-02'` no puede usarlo bien: con los datos de
  prueba, el plan fue `Seq Scan`.

La regla de la documentación de PostgreSQL: las igualdades sobre las primeras columnas, más una
desigualdad sobre la primera columna sin igualdad, "will always be used to limit the portion of the
index that is scanned". De ahí sale el criterio práctico: primero las columnas que se comparan con
`=`, después la del rango. La documentación menciona además una optimización ("skip scan") que puede
usar el índice sin condición sobre la primera columna, pero solo conviene con pocos valores
distintos en ella.

El mismo índice sirve para el último pedido de cada cliente con `LATERAL`, de
[subconsultas y CTE](subconsultas-y-cte.md#el-último-pedido-de-cada-cliente-de-cuatro-formas).

## Lo que cuesta un índice

Cada índice se actualiza en cada `INSERT`, en cada `DELETE` y en los `UPDATE` que tocan sus
columnas. Winand sostiene que "The number of indexes on a table is the most dominant factor for
insert performance", y en un caso medido en su sitio, "adding a single index is enough to increase
the execute time by a factor of a hundred". Es la medición de un caso, no una regla general. La
consecuencia práctica: un índice se crea para una consulta que lo necesita, no "por las dudas" en
cada columna. Las restricciones `PRIMARY KEY` y `UNIQUE` crean el suyo solas: en las tablas de prueba, la base
creó `clientes_pkey` y `clientes_email_key` sin que nadie los pidiera.

## Para leer en la fuente

Para quien escribe consultas, el capítulo "The Where Clause" de use-the-index-luke.com, de Winand:
las páginas de claves concatenadas, funciones y LIKE. Para leer planes, la sección 14.1 "Using
EXPLAIN" de PostgreSQL; fijarse en que el planificador puede elegir `Seq Scan` aunque haya índice.
El sitio de Winand no declara licencia abierta: se enlaza, no se copia.
