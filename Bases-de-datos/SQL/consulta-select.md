---
resumen: >-
  Una consulta SELECT pide filas a la base: de qué tablas, con qué condición, qué columnas, en qué
  orden y cuántas. Sus cláusulas se escriben en un orden y se evalúan en otro, y casi todos los
  errores de quien empieza salen de esa diferencia.
estado: borrador
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, SELECT (sección Description): https://www.postgresql.org/docs/current/sql-select.html"
  - "PostgreSQL Documentation, 7.1 Queries Overview: https://www.postgresql.org/docs/current/queries-overview.html"
  - "SQLBolt, SQL Lesson 12: Order of execution of a Query: https://sqlbolt.com/"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [SELECT, consulta, query, orden lógico de ejecución, logical query processing]
creado: 2026-11-27
revisado:
---

# Consulta SELECT

Una consulta SELECT pide filas a la base: de qué tablas, con qué condición, qué columnas, en qué
orden y cuántas. Sus cláusulas se escriben en un orden y se evalúan en otro, y casi todos los
errores de quien empieza salen de esa diferencia.

## Las cláusulas de una consulta

Con las tablas del comercio de [SQL](sql.md), los dos productos más caros que tienen stock:

```sql
SELECT nombre, precio          -- qué columnas
FROM productos                 -- de qué tabla
WHERE stock > 0                -- qué filas
ORDER BY precio DESC           -- en qué orden
LIMIT 2;                       -- cuántas (LIMIT es de PostgreSQL, MySQL y SQLite)
```

La forma general, según la documentación de PostgreSQL, es
`[WITH with_queries] SELECT select_list FROM table_expression [sort_specification]`. Entre `FROM` y
el orden pueden ir `WHERE`, `GROUP BY` y `HAVING`, que se ven en [agregación](agregacion.md). Todas
son opcionales salvo `SELECT`: PostgreSQL acepta `SELECT 3 * 4;` sin tabla, como calculadora.

## El orden en que se evalúan las cláusulas

La documentación de `SELECT` de PostgreSQL describe el procesamiento en pasos numerados. Reducidos
a lo que importa para escribir consultas:

1. `FROM`: "All elements in the FROM list are computed", incluidos los [joins](join.md).
2. `WHERE`: se descartan las filas que no cumplen la condición.
3. `GROUP BY` y `HAVING`: se forman los grupos, y `HAVING` "eliminates groups that do not satisfy the
   given condition".
4. La lista de `SELECT`: se calculan las columnas de salida y sus alias.
5. `DISTINCT`: se eliminan las filas repetidas.
6. `ORDER BY`: se ordena.
7. `LIMIT` u `OFFSET`: se recorta.

Es un orden lógico, un modelo para predecir el resultado, no lo que hace el motor paso a paso. La
misma página aclara que PostgreSQL "will effectively evaluate output expressions after sorting and
limiting" cuando eso no cambia el resultado. El resultado es siempre el que daría el orden lógico;
la forma de llegar la elige el planificador.

## Por qué un alias no se ve en WHERE

Un alias se crea en el paso 4, y `WHERE` se evalúa en el paso 2: todavía no existe. Esta consulta
falla:

```sql
SELECT nombre, precio * 1.21 AS precio_con_iva
FROM productos
WHERE precio_con_iva > 10000;
-- ERROR:  column "precio_con_iva" does not exist
```

Se arregla repitiendo la expresión en `WHERE` (`WHERE precio * 1.21 > 10000`) o calculándola en una
[subconsulta o CTE](subconsultas-y-cte.md). En cambio, `ORDER BY precio_con_iva` sí funciona, porque
`ORDER BY` va después de `SELECT`. Lo mismo explica que no se pueda filtrar por un agregado en
`WHERE` (para eso está `HAVING`) ni por una [función de ventana](funciones-de-ventana.md) (para eso
hace falta una subconsulta).

## Sin ORDER BY no hay orden

Una tabla no tiene un orden propio. Sin `ORDER BY`, PostgreSQL devuelve las filas "in whatever order
the system finds fastest to produce", y ese orden puede cambiar de un día para otro sin que nadie
toque nada. Con `LIMIT` el problema se agrava: sin `ORDER BY` se obtiene "an unpredictable subset of
the query's rows", y "It is even possible for repeated executions of the same LIMIT query to return
different subsets of the rows". Toda consulta que muestra "los primeros N" lleva `ORDER BY`, y si el
criterio puede empatar (dos productos con el mismo precio), una segunda columna que desempate,
como `ORDER BY precio DESC, id`.

## WHERE filtra filas con condiciones

`WHERE` recibe una condición que se evalúa por fila. Las que dan verdadero quedan; las que dan falso
o desconocido se van. Ese "desconocido" es el resultado de comparar con un NULL, y es la razón por
la que `WHERE ciudad <> 'Rosario'` no devuelve a los clientes sin ciudad. Está explicado en
[NULL y tipos](null-y-tipos.md#la-lógica-de-tres-valores).

Los operadores comunes son `=`, `<>`, `<`, `>`, `BETWEEN`, `IN (...)`, `LIKE` con `%` como
comodín, e `IS NULL`. Para fechas conviene un rango semiabierto, que además deja usar un
[índice](indice.md):

```sql
SELECT id, cliente_id, fecha
FROM pedidos
WHERE fecha >= '2026-11-01' AND fecha < '2026-12-01';   -- todo noviembre
```

## Para seguir con práctica

SQLBolt tiene una lección dedicada al orden de evaluación, "SQL Lesson 12: Order of execution of a
Query"; conviene hacerla después de las de filtrado y orden. Los ejercicios en orden están en la
[ruta de SQL](../Fundamentos/ruta-de-sql.md).
