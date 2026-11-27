---
resumen: >-
  Una función de ventana calcula sobre un grupo de filas relacionadas con la fila actual (su
  partición) sin colapsarlas en una: cada fila conserva su detalle y suma el resultado, como el
  total del pedido al lado de cada ítem, un ranking o un acumulado.
estado: borrador
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 3.5 Window Functions (tutorial): https://www.postgresql.org/docs/current/tutorial-window.html"
  - "PostgreSQL Documentation, 4.2.8 Window Function Calls: https://www.postgresql.org/docs/current/sql-expressions.html"
  - "PostgreSQL Documentation, 9.22 Window Functions: https://www.postgresql.org/docs/current/functions-window.html"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [window functions, ventana, OVER, PARTITION BY, row_number, rank, función analítica]
creado: 2026-11-27
revisado:
---

# Funciones de ventana

Una función de ventana calcula sobre un grupo de filas relacionadas con la fila actual (su
partición) sin colapsarlas en una: cada fila conserva su detalle y suma el resultado, como el
total del pedido al lado de cada ítem, un ranking o un acumulado.

## La diferencia con GROUP BY

[Agregación](agregacion.md) con `GROUP BY` devuelve una fila por grupo y pierde el detalle. Una
ventana devuelve todas las filas. La documentación de PostgreSQL lo dice así: "window functions do
not cause rows to become grouped into a single output row like non-window aggregate calls would.
Instead, the rows retain their separate identities".

Cada ítem con su subtotal y el total de su pedido:

```sql
SELECT i.pedido_id, i.producto_id,
       i.cantidad * i.precio_unitario AS subtotal,
       sum(i.cantidad * i.precio_unitario) OVER (PARTITION BY i.pedido_id) AS total_pedido
FROM items_pedido i;
```

| pedido_id | producto_id | subtotal | total_pedido |
|---|---|---|---|
| 1 | 1 | 9000.00 | 21000.00 |
| 1 | 2 | 12000.00 | 21000.00 |
| 2 | 1 | 4500.00 | 4500.00 |
| 3 | 2 | 12000.00 | 24000.00 |
| 3 | 3 | 12000.00 | 24000.00 |

Con eso, el peso de cada ítem en su pedido es una división en la misma consulta. Sin ventanas
haría falta agrupar en una subconsulta y unirla de vuelta.

## Las tres partes de OVER

`OVER (...)` convierte un agregado o una función de ranking en función de ventana. Adentro van tres
partes, todas opcionales:

- **`PARTITION BY`**: en qué grupos se divide el cálculo. Sin él, la ventana es la tabla entera.
- **`ORDER BY`**: en qué orden se recorren las filas de cada partición. Hace falta para rankings,
  acumulados y "la fila anterior".
- **El marco** (`ROWS`, `RANGE` o `GROUPS`): qué filas de la partición entran en el cálculo de cada
  fila. Si no se escribe, se usa uno por defecto que trae sorpresas (más abajo).

## Ranking: row_number, rank y dense_rank

Las tres numeran filas según el `ORDER BY` y difieren en los empates. Según la documentación,
`row_number` da "the number of the current row within its partition, counting from 1"; `rank` numera
"with gaps", y `dense_rank` "without gaps". Productos por unidades vendidas, con Mate y Bombilla
empatados en 2:

```sql
SELECT pr.nombre, sum(i.cantidad) AS unidades,
       row_number() OVER (ORDER BY sum(i.cantidad) DESC) AS row_number,
       rank()       OVER (ORDER BY sum(i.cantidad) DESC) AS rank,
       dense_rank() OVER (ORDER BY sum(i.cantidad) DESC) AS dense_rank
FROM items_pedido i
JOIN productos pr ON pr.id = i.producto_id
GROUP BY pr.nombre;
```

| nombre | unidades | row_number | rank | dense_rank |
|---|---|---|---|---|
| Yerba 1 kg | 6 | 1 | 1 | 1 |
| Bombilla | 2 | 2 | 2 | 2 |
| Mate | 2 | 3 | 2 | 2 |

Con un empate, `row_number` numera en un orden que no está garantizado: cuál de los dos sale
segundo puede cambiar. Si
importa, se agrega una columna más al `ORDER BY` de la ventana. Muestra también que una ventana se
puede aplicar sobre un agregado: se calcula después del `GROUP BY`.

El uso más común de `row_number` es quedarse con el primero de cada grupo, como el último pedido de
cada cliente, que está resuelto en [subconsultas y CTE](subconsultas-y-cte.md#el-último-pedido-de-cada-cliente-de-cuatro-formas).

## Acumulados y el marco por defecto

Con `ORDER BY` dentro de `OVER`, un `sum` se vuelve acumulado. El marco por defecto, según la
documentación: "if ORDER BY is supplied then the frame consists of all rows from the start of the
partition up through the current row, plus any following rows that are equal to the current row
according to the ORDER BY clause". Esa última parte hace que las filas empatadas en el orden reciban
el mismo acumulado:

```sql
WITH v(dia, monto) AS (VALUES (1, 100), (2, 50), (2, 30), (3, 20))
SELECT dia, monto,
       sum(monto) OVER (ORDER BY dia) AS por_defecto,
       sum(monto) OVER (ORDER BY dia ROWS UNBOUNDED PRECEDING) AS con_rows
FROM v;
```

| dia | monto | por_defecto | con_rows |
|---|---|---|---|
| 1 | 100 | 100 | 100 |
| 2 | 50 | 180 | 150 |
| 2 | 30 | 180 | 180 |
| 3 | 20 | 200 | 200 |

El marco por defecto es `RANGE`, que trata como un bloque a las filas con el mismo valor de orden.
`ROWS` cuenta filas una por una. Para un saldo o un acumulado fila por fila, `ROWS UNBOUNDED
PRECEDING` es lo que se quiere.

La misma regla rompe `last_value`: con el marco por defecto, el marco termina en la fila actual, y
`last_value` devuelve la fila actual en vez de la última de la partición. La documentación lo
advierte: "This is likely to give unhelpful results for last_value and sometimes also nth_value".
Se arregla con `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`, o se usa `first_value`
con el orden invertido.

## La fila anterior: lag y lead

`lag(columna)` trae el valor de la fila anterior de la partición y `lead(columna)`, el de la
siguiente. El desplazamiento por defecto es 1, y cuando no hay fila devuelven NULL. Días entre un
pedido y el anterior del mismo cliente:

```sql
SELECT cliente_id, id, fecha::date,
       fecha::date - lag(fecha::date) OVER (PARTITION BY cliente_id ORDER BY fecha) AS dias_desde_anterior
FROM pedidos;
```

El segundo pedido de Ana da 39 días; los primeros pedidos de cada cliente dan NULL. Es la base de
medidas como la frecuencia de compra, cuyo análisis está en [Datos](../../Datos/datos.md).

## Dónde se pueden usar

Las ventanas se calculan después de `WHERE`, `GROUP BY` y `HAVING`, en la lista de `SELECT`. La
documentación: "They are forbidden elsewhere, such as in GROUP BY, HAVING and WHERE clauses". Para
filtrar por el resultado de una ventana hace falta envolverla en una subconsulta o una CTE. Además,
"a row removed because it does not meet the WHERE condition is not seen by any window function": un
`WHERE` que filtra noviembre hace que el ranking y el acumulado se calculen solo con noviembre.

## Para leer en la fuente

El tutorial 3.5 "Window Functions" de PostgreSQL es corto y trae su propio ejemplo con salarios por
departamento; conviene leerlo entero y fijarse en el marco por defecto. La lista completa de
funciones está en la 9.22. Los recursos de ejercicios de la [ruta de SQL](../Fundamentos/ruta-de-sql.md)
casi no cubren ventanas.
