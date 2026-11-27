---
resumen: >-
  La agregación junta muchas filas en una con funciones como count, sum o avg; con GROUP BY lo hace
  por grupo (un total por cliente, por mes, por producto) y con HAVING filtra los grupos que
  resultan.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 4.2.7 Aggregate Expressions: https://www.postgresql.org/docs/current/sql-expressions.html"
  - "PostgreSQL Documentation, 7.2.3 y 7.2.4 GROUP BY, HAVING, GROUPING SETS, CUBE y ROLLUP: https://www.postgresql.org/docs/current/queries-table-expressions.html"
  - "PostgreSQL Documentation, SELECT: https://www.postgresql.org/docs/current/sql-select.html"
  - "MySQL 8.4 Reference Manual, MySQL Handling of GROUP BY: https://dev.mysql.com/doc/refman/8.4/en/group-by-handling.html"
  - "Markus Winand, modern-sql.com, The filter clause: https://modern-sql.com/feature/filter"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [GROUP BY, HAVING, funciones de agregado, aggregate functions, agrupar]
creado: 2026-11-27
revisado: 2026-11-27
---

# Agregación

La agregación junta muchas filas en una con funciones como count, sum o avg; con GROUP BY lo hace
por grupo (un total por cliente, por mes, por producto) y con HAVING filtra los grupos que
resultan.

Es la [tabla dinámica](../../Planillas-de-calculo/Analisis/tabla-dinamica.md) de la planilla escrita como consulta. Se evalúa después de `FROM` y `WHERE` y
antes de la lista de `SELECT`, según el orden de la [consulta SELECT](consulta-select.md).

## El total vendido por cliente, incluidos los que no compraron

La pregunta junta tres piezas: unir clientes con pedidos e ítems, conservar a los que no tienen
pedidos y sumar por cliente.

```sql
SELECT c.nombre,
       coalesce(sum(i.cantidad * i.precio_unitario), 0) AS total
FROM clientes c
LEFT JOIN pedidos p      ON p.cliente_id = c.id
                        AND p.fecha >= '2026-11-01' AND p.fecha < '2026-12-01'
LEFT JOIN items_pedido i ON i.pedido_id = p.id
GROUP BY c.id, c.nombre
ORDER BY total DESC;
```

| nombre | total |
|---|---|
| Bruno | 24000.00 |
| Ana | 4500.00 |
| Diego | 0 |
| Carla | 0 |

Cada pieza tiene una razón:

- **Los dos LEFT JOIN** conservan a Carla (sin pedidos) y a Diego (sin pedidos en noviembre).
- **El filtro de fecha va en el ON** del join con pedidos, no en `WHERE`; en `WHERE` borraría a
  quienes no compraron, como explica [join](join.md#on-contra-where-en-un-left-join).
- **`coalesce(..., 0)`** convierte en cero la suma de quienes no compraron. Sin él, `sum` sobre filas
  que solo tienen NULL devuelve NULL, no 0 (ver [NULL y tipos](null-y-tipos.md)).
- **`GROUP BY c.id, c.nombre`** agrupa por la clave y no solo por el nombre, para que dos clientes
  que se llaman igual no se sumen juntos.

Para "el mes pasado" relativo al día en que se corre, el rango se calcula:
`p.fecha >= date_trunc('month', now()) - interval '1 month' AND p.fecha < date_trunc('month', now())`.
Para "los últimos 30 días", `p.fecha >= now() - interval '30 days'`. Las dos son de PostgreSQL.

## Qué se puede poner en el SELECT de una consulta agrupada

Después de agrupar queda una fila por grupo, así que cada columna de la salida tiene que tener un
solo valor por grupo. La documentación de PostgreSQL: "columns that are not listed in GROUP BY
cannot be referenced except in aggregate expressions".

```sql
SELECT c.nombre, c.ciudad, count(p.id)
FROM clientes c LEFT JOIN pedidos p ON p.cliente_id = c.id
GROUP BY c.nombre;
-- ERROR:  column "c.ciudad" must appear in the GROUP BY clause or be used in an aggregate function
```

Agrupar por `c.id`, la clave primaria, sí deja usar `c.nombre` y `c.ciudad` en PostgreSQL (se
comprobó al ejecutarlo): con la clave fija, el resto de las columnas de esa tabla tiene un solo
valor. No todos los motores detectan esa dependencia funcional, y donde no la detectan hay que
listar todas las columnas en `GROUP BY`; MySQL 8.4 sí la detecta, según su manual: "MySQL implements
detection of functional dependence".

## count(*) y count(columna) cuentan cosas distintas

`count(*)` cuenta filas; `count(columna)` cuenta los valores que no son NULL. La documentación de
PostgreSQL lo resume en "Most aggregate functions ignore null inputs", con este ejemplo:

```sql
WITH vals (f1) AS ( VALUES (1),(3),(4),(3),(2),(null) )
SELECT count(*) AS total, count(f1) AS non_null, COUNT(DISTINCT f1) AS distinct FROM vals;
-- total = 6, non_null = 5, distinct = 4
```

Con un LEFT JOIN la diferencia decide el resultado. Contar pedidos por cliente con `count(*)` le da
1 a Carla, que no tiene ninguno, porque el LEFT JOIN le dejó una fila. `count(p.id)` le da 0, que
es lo correcto. `avg` también ignora los NULL: el promedio de 10, NULL y 20 es 15, no 10.

## WHERE filtra filas y HAVING filtra grupos

`WHERE` se aplica antes de agrupar y no puede usar agregados; `HAVING` se aplica después y sí. Los
clientes con dos pedidos o más:

```sql
SELECT cliente_id, count(*) AS pedidos
FROM pedidos
GROUP BY cliente_id
HAVING count(*) >= 2;
```

Si la condición no usa un agregado (por ejemplo, la fecha), va en `WHERE`: descarta filas antes de
agrupar, que es más barato y más claro. Un detalle de evaluación que cita la documentación de
`SELECT`: "all aggregate functions are evaluated before evaluating any 'scalar' expressions in the
HAVING clause or SELECT list", así que un `CASE` no sirve para evitar que se calcule un agregado.

## Contar con condición: FILTER

`FILTER` aplica un agregado solo a las filas que cumplen una condición, y permite varios conteos en
una sola pasada:

```sql
SELECT count(*) AS pedidos,
       count(*) FILTER (WHERE envio = 0) AS con_envio_gratis
FROM pedidos;
```

Según Winand, "SQL:2003 introduced the filter clause", que es estándar pero "barely supported
today, but is easy to emulate using case". La forma que anda en cualquier motor es
`sum(CASE WHEN envio = 0 THEN 1 ELSE 0 END)`. PostgreSQL y SQLite aceptan `FILTER` (en SQLite se
comprobó al ejecutarlo).

## Subtotales con ROLLUP

`GROUP BY ROLLUP (ciudad, nombre)` devuelve el detalle por cliente, un subtotal por ciudad y un
total general en la misma consulta. Según la documentación, ROLLUP representa la lista de
expresiones "and all prefixes of the list including the empty list"; `CUBE` agrega todas las
combinaciones. En las filas de subtotal, las columnas que no participan salen en NULL, y eso se
confunde con un NULL real: con los datos de prueba, la fila de Carla (sin ciudad) y el subtotal
de "ciudad desconocida" se ven iguales. La documentación lo advierte; la función `GROUPING()`, que
los distingue, no se leyó en esta ronda.

## Cuando la suma da de más

Si un total sale el doble o el triple de lo esperado, casi siempre hay un join de uno a muchos
antes del `GROUP BY` que repite filas. El diagnóstico y la salida (agregar cada tabla a su nivel
antes de unir) están en [join](join.md#un-join-que-multiplica-filas). Ese nivel es el
[grano](../../Datos/Analisis/sql-para-analisis.md#el-grano-qué-es-una-fila) de la tabla: qué
representa una fila.

## Para leer en la fuente

La sección 4.2.7 "Aggregate Expressions" de PostgreSQL trae el ejemplo de `count`; la 7.2.4,
`GROUPING SETS`, `ROLLUP` y `CUBE`. En la [ruta de SQL](../Fundamentos/ruta-de-sql.md), la categoría
"Aggregates" de pgexercises es la práctica que corresponde.
