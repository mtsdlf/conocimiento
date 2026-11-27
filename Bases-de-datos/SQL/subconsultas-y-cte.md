---
resumen: >-
  Una subconsulta es una consulta dentro de otra, que aporta un valor, una lista o una tabla; una
  CTE (WITH) le pone nombre a esa consulta para usarla como una tabla temporal y leer la consulta de
  arriba hacia abajo. La versión recursiva recorre jerarquías y genera series.
estado: borrador
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 9.25 Subquery Expressions: https://www.postgresql.org/docs/current/functions-subquery.html"
  - "PostgreSQL Documentation, 7.8 WITH Queries (Common Table Expressions): https://www.postgresql.org/docs/current/queries-with.html"
  - "PostgreSQL Documentation, 7.2.1.5 LATERAL Subqueries: https://www.postgresql.org/docs/current/queries-table-expressions.html"
  - "PostgreSQL Documentation, SELECT (DISTINCT ON): https://www.postgresql.org/docs/current/sql-select.html"
  - "PostgreSQL Documentation, 3.5 Window Functions: https://www.postgresql.org/docs/current/tutorial-window.html"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [subconsulta, subquery, CTE, common table expression, WITH, consulta recursiva, WITH RECURSIVE, EXISTS, LATERAL]
creado: 2026-11-27
revisado:
---

# Subconsultas y CTE

Una subconsulta es una consulta dentro de otra, que aporta un valor, una lista o una tabla; una
CTE (WITH) le pone nombre a esa consulta para usarla como una tabla temporal y leer la consulta de
arriba hacia abajo. La versión recursiva recorre jerarquías y genera series.

Sirven para lo que una sola [consulta SELECT](consulta-select.md) no puede hacer en un paso: filtrar
por algo que hay que calcular antes, como un agregado o una [función de ventana](funciones-de-ventana.md).

## Dónde puede ir una subconsulta

Según lo que devuelve, va en un lugar distinto:

| Devuelve | Va en | Ejemplo |
|---|---|---|
| un valor | `SELECT` o `WHERE`, donde iría una columna | `(SELECT count(*) FROM pedidos p WHERE p.cliente_id = c.id)` |
| una lista | `WHERE ... IN (...)` | `WHERE id IN (SELECT cliente_id FROM pedidos)` |
| si existe alguna fila | `WHERE EXISTS (...)` | ver abajo |
| una tabla | `FROM` o `JOIN`, con un alias | `JOIN (SELECT pedido_id, sum(...) ...) t ON ...` |

Una subconsulta es **correlacionada** cuando usa columnas de la consulta de afuera, como `c.id` en
el primer ejemplo. La documentación de PostgreSQL lo describe así: "The subquery can refer to
variables from the surrounding query, which will act as constants during any one evaluation of the
subquery". Conceptualmente se evalúa una vez por fila de afuera; el motor puede optimizarla.

## EXISTS: si hay al menos una pareja

`EXISTS` da verdadero si la subconsulta devuelve alguna fila. Los clientes que compraron alguna vez:

```sql
SELECT c.nombre
FROM clientes c
WHERE EXISTS (SELECT 1 FROM pedidos p WHERE p.cliente_id = c.id);
```

A diferencia de un join, no repite a Ana por tener dos pedidos. La documentación lo compara con un
inner join que "produces at most one output row for each tab1 row", y por eso es la salida al
[join que multiplica filas](join.md#un-join-que-multiplica-filas) cuando solo importa si hay pareja.
Lo que se ponga en la lista de la subconsulta no importa: `EXISTS(SELECT * ...)` y
`EXISTS(SELECT 1 ...)` "are actually equivalent in PostgreSQL". `NOT EXISTS` da los que no tienen
pareja: Carla.

## NOT IN con un NULL no devuelve nada

`IN` y `NOT IN` comparan contra una lista, y si la lista tiene un NULL entra la
[lógica de tres valores](null-y-tipos.md#la-lógica-de-tres-valores). La documentación de PostgreSQL:
si no hay coincidencia "and at least one right-hand row yields null, the result of the NOT IN
construct will be null, not true".

Con una columna `referido_por` en `clientes`, que dice qué cliente recomendó a cada uno y está vacía
para casi todos, la pregunta "clientes que no recomendaron a nadie" escrita con `NOT IN`:

```sql
SELECT nombre FROM clientes
WHERE id NOT IN (SELECT referido_por FROM clientes);
-- 0 filas
```

Devuelve cero filas, aunque tres de los cuatro clientes no recomendaron a nadie. Para cada cliente,
"no está entre 1, NULL, NULL, NULL" da desconocido: podría ser alguno de los NULL. Con `NOT EXISTS`
el problema no existe:

```sql
SELECT c.nombre FROM clientes c
WHERE NOT EXISTS (SELECT 1 FROM clientes r WHERE r.referido_por = c.id);
-- Bruno, Carla, Diego
```

La regla: para "los que no están en", `NOT EXISTS`. `NOT IN` solo es seguro si la columna de la
subconsulta es `NOT NULL`.

## WITH: nombrar un paso intermedio

Una CTE, según la documentación, "can be thought of as defining temporary tables that exist just for
one query". Se escribe primero y se usa después, como una tabla. Los clientes que compraron más que
el promedio:

```sql
WITH ventas AS (
  SELECT p.cliente_id, sum(i.cantidad * i.precio_unitario) AS total
  FROM pedidos p
  JOIN items_pedido i ON i.pedido_id = p.id
  GROUP BY p.cliente_id
)
SELECT c.nombre, v.total
FROM ventas v
JOIN clientes c ON c.id = v.cliente_id
WHERE v.total > (SELECT avg(total) FROM ventas);
```

`ventas` se usa dos veces: para unirla con clientes y para calcular el promedio. Con subconsultas,
el mismo cálculo se escribiría dos veces. Una consulta con varias CTE se lee como una receta, paso
por paso, y ese es el motivo principal para usarlas.

En PostgreSQL, una CTE que se usa una sola vez se integra a la consulta principal y se optimiza con
ella; una que se usa más de una vez se calcula una vez y se guarda. `MATERIALIZED` y `NOT
MATERIALIZED` fuerzan una u otra cosa. Una CTE también puede ser un `INSERT`, `UPDATE`, `DELETE` o
`MERGE`, que se combina con `RETURNING` de [modificar datos](modificar-datos.md).

## WITH RECURSIVE: series y jerarquías

Una CTE recursiva tiene un término inicial y uno que se refiere a la propia CTE, unidos por `UNION
ALL`. El ejemplo de la documentación suma de 1 a 100:

```sql
WITH RECURSIVE t(n) AS (
  VALUES (1)
  UNION ALL
  SELECT n + 1 FROM t WHERE n < 100
)
SELECT sum(n) FROM t;   -- 5050
```

Según la documentación, el motor evalúa el término inicial, lo pone en una tabla de trabajo y repite
el término recursivo "so long as the working table is not empty". La condición `n < 100` es la que
corta; sin ella la consulta no termina. Con `UNION` en vez de `UNION ALL` se descartan las filas
repetidas.

En un comercio sirve para dos cosas. Una es generar un calendario para que los días sin ventas
aparezcan con cero:

```sql
WITH RECURSIVE dias(d) AS (
  SELECT date '2026-11-08'
  UNION ALL
  SELECT d + 1 FROM dias WHERE d < date '2026-11-16'
)
SELECT d, count(p.id) AS pedidos
FROM dias
LEFT JOIN pedidos p ON p.fecha::date = d
GROUP BY d
ORDER BY d;
```

La otra es recorrer una jerarquía: categorías dentro de categorías, o la cadena de quién refirió a
quién. En PostgreSQL, `generate_series` hace el calendario más corto, pero es una extensión.

## LATERAL: una subconsulta por fila

Una subconsulta en `FROM` normalmente no ve las otras tablas del `FROM`. Con `LATERAL` sí: "This
allows them to reference columns provided by preceding FROM items". Así se puede pedir, por cada
cliente, sus N pedidos más recientes. La documentación agrega que "It is often particularly handy
to LEFT JOIN to a LATERAL subquery, so that source rows will appear in the result even if the
LATERAL subquery produces no rows for them". No todos los motores lo tienen: SQLite no lo acepta
(se comprobó al ejecutarlo).

## El último pedido de cada cliente, de cuatro formas

Es la pregunta de "el último (o el mayor) de cada grupo". Las cuatro formas son ejemplos propios:
la documentación da los ingredientes pero no el caso completo. Se ejecutaron en PostgreSQL 18.4 con
un empate a propósito: Bruno tiene dos pedidos con la misma fecha y hora (ids 3 y 5).

**1. Subconsulta correlacionada.** Anda en cualquier motor.

```sql
SELECT p.cliente_id, p.id, p.fecha
FROM pedidos p
WHERE p.fecha = (SELECT max(p2.fecha) FROM pedidos p2 WHERE p2.cliente_id = p.cliente_id);
```

Devuelve los dos pedidos empatados de Bruno. Puede ser lo que se quiere o no; si hace falta uno
solo, hay que agregar un desempate.

**2. Función de ventana.** Estándar; se comprobó en PostgreSQL y en SQLite.

```sql
WITH numerados AS (
  SELECT p.*,
         row_number() OVER (PARTITION BY cliente_id ORDER BY fecha DESC, id DESC) AS n
  FROM pedidos p
)
SELECT cliente_id, id, fecha FROM numerados WHERE n = 1;
```

Devuelve uno por cliente; el `id DESC` decide el empate (gana el 5). Va en una CTE porque las
ventanas "are permitted only in the SELECT list and the ORDER BY clause": escribir `WHERE
row_number() OVER (...) = 1` da "window functions are not allowed in WHERE". Cambiando
`row_number` por `rank` vuelven los empates, como en la forma 1. Es la más flexible: con `n <= 3`
salen los tres últimos.

**3. DISTINCT ON.** Extensión de PostgreSQL; la más corta.

```sql
SELECT DISTINCT ON (cliente_id) cliente_id, id, fecha
FROM pedidos
ORDER BY cliente_id, fecha DESC, id DESC;
```

Se queda con la primera fila de cada `cliente_id` según el `ORDER BY`. La documentación pide que
"The DISTINCT ON expression(s) must match the leftmost ORDER BY expression(s)". SQLite no la acepta.

**4. LEFT JOIN LATERAL.** Sin soporte en SQLite.

```sql
SELECT c.nombre, u.id, u.fecha
FROM clientes c
LEFT JOIN LATERAL (
  SELECT p.id, p.fecha
  FROM pedidos p
  WHERE p.cliente_id = c.id
  ORDER BY p.fecha DESC, p.id DESC
  LIMIT 1
) u ON true;
```

Es la única de las cuatro que parte de `clientes` y por eso muestra a Carla, sin pedido. Con un
[índice](indice.md) en `pedidos (cliente_id, fecha)`, cada subconsulta lee una sola entrada del
índice, lo que la hace la más rápida cuando hay pocos clientes y muchos pedidos (inferencia a partir
de cómo funciona el índice; no se midió).

Cuál usar: la de ventana es la opción por defecto, porque es estándar, anda en más motores y se extiende a "los N
últimos"; `DISTINCT ON` cuando el motor es PostgreSQL y se quiere brevedad; `LATERAL` cuando hacen
falta también los clientes sin pedidos o hay que traer varias columnas del último pedido. No se
encontró un recurso canónico que compare las cuatro.

## Para leer en la fuente

La sección 9.25 de la documentación de PostgreSQL ("Subquery Expressions"), con las notas sobre
NULL en `IN` y `NOT IN`; fijarse en la frase "null, not true". Para CTE, la 7.8 "WITH Queries", que
explica el algoritmo de la recursiva.
