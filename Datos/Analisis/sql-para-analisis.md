---
resumen: >-
  SQL para análisis es el uso del lenguaje de consultas de las bases de datos para contestar
  preguntas: saber qué es una fila, unir tablas sin duplicar, agregar, tratar los NULL y calcular
  sobre filas vecinas con funciones de ventana.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL 19, 7.2 Table Expressions: https://www.postgresql.org/docs/current/queries-table-expressions.html"
  - "PostgreSQL 19, 9.2 Comparison Functions and Operators: https://www.postgresql.org/docs/current/functions-comparison.html"
  - "PostgreSQL 19, tutorial 3.5 Window Functions: https://www.postgresql.org/docs/current/tutorial-window.html"
  - "Kimball Group, Dimensional modeling techniques: Grain: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/"
  - "Brett Sauve, The problem of SQL fanouts, Google Cloud Community (22-06-2022): https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220.md"
  - "Holistics docs, Fan-out resolution (según resumen): https://docs.holistics.io/docs/joins/fan-out-resolution"
  - "Ejemplos corridos por la base en SQLite 3.53 el 2026-11-27, con sintaxis que también vale en PostgreSQL salvo las fechas"
  - "Datos/.investigacion/analisis.md"
aliases: [SQL, consultas SQL, SQL analítico, joins, fan-out, fanout, funciones de ventana, window functions, grano, granularidad, grain]
creado: 2026-11-27
revisado: 2026-11-27
---

# SQL para análisis

SQL para análisis es el uso del lenguaje de consultas de las bases de datos para contestar
preguntas: saber qué es una fila, unir tablas sin duplicar, agregar, tratar los NULL y calcular
sobre filas vecinas con funciones de ventana.

Es la herramienta principal de la fase de analizar del [análisis](analisis.md). La base de datos rechaza los errores de
sintaxis; los que importan son las consultas que corren y devuelven un número equivocado. Esta nota explica los cinco conceptos donde eso pasa. La sintaxis completa está
en el tutorial de PostgreSQL (capítulos 2 y 3, y la sección 7.2), que usa una sola tabla de
ejemplo en todo el recorrido. Qué motor y qué versión usar está en la ficha
[herramientas del analista](herramientas-del-analista.md).

Los ejemplos usan tres tablas de un comercio:

```sql
ventas(id_venta, fecha, id_cliente, canal, total)        -- una fila por venta
items_venta(id_venta, producto, cantidad, precio)        -- una fila por producto vendido
clientes(id_cliente, nombre, referido_por)               -- una fila por cliente
```

## Una consulta se lee en el orden en que se ejecuta

PostgreSQL describe las cláusulas como «a pipeline of successive transformations performed on the
table derived in the `FROM` clause». Se lee `FROM` (y sus joins), después `WHERE`, `GROUP BY`,
`HAVING` y recién al final `SELECT`. Por eso `WHERE` filtra filas antes de agrupar y `HAVING`
filtra grupos después:

```sql
-- Meses en que la tienda online vendió más de 800
SELECT date_trunc('month', fecha) AS mes, count(*) AS ventas, sum(total) AS facturado
FROM ventas
WHERE canal = 'tienda'          -- filtra ventas
GROUP BY mes
HAVING sum(total) > 800;        -- filtra meses
```

## El grano: qué es una fila

El grano es lo que representa una fila de una tabla. Kimball lo define para las tablas de hechos:
«The grain establishes exactly what a single fact table row represents», y pide declararlo antes
de elegir dimensiones y hechos. Llevarlo a cualquier tabla es una extensión de esta base, y es la primera pregunta
antes de consultar: en `ventas` una fila es una venta; en `items_venta`, un producto dentro de una
venta. Sumar `total` sobre la segunda tabla no da la facturación. El grano se diseña en el
[modelado dimensional](../Modelado-y-almacenamiento/modelado-dimensional.md).

## Un join que multiplica filas

Un join une dos tablas por una clave. La definición de PostgreSQL ya trae el riesgo: en un `INNER
JOIN`, «for each row R1 of T1, the joined table has a row for each row in T2 that satisfies the
join condition with R1». Si una venta tiene tres ítems, aparece tres veces. Un `LEFT JOIN` además
conserva las filas de la izquierda sin pareja, con NULL en las columnas de la derecha.

Cuando la tabla unida tiene más filas que la original, Sauve lo llama fan-out: «Since the joined
table has more rows than the primary table, we say that a fanout has occurred». Pasa en los joins
de uno a muchos. Con cinco ventas que suman 2.700 y seis ítems:

```sql
SELECT count(*), sum(v.total)
FROM ventas v JOIN items_venta i ON i.id_venta = v.id_venta;
-- 6 filas, 3.700: la venta de dos ítems se sumó dos veces
```

El arreglo es llevar el lado «muchos» al grano del otro antes de unir:

```sql
SELECT sum(v.total) AS facturado, sum(i.unidades) AS unidades
FROM ventas v
JOIN (SELECT id_venta, sum(cantidad) AS unidades
      FROM items_venta GROUP BY id_venta) i ON i.id_venta = v.id_venta;
-- 2.700 y 8: una fila por venta
```

Un chequeo rápido es contar filas antes y después del join. Sauve advierte que entender el tipo de
join es mejor que contar, porque el conteo de hoy no avisa del duplicado de mañana. Las
herramientas de BI que corrigen el fan-out solas dependen de que la clave declarada sea única de
verdad; si no lo es, según la documentación de Holistics, el resultado sale mal sin aviso.

## Agregar resume y pierde detalle

`GROUP BY` junta las filas que comparten valores y las funciones de agregación (`count`, `sum`,
`avg`, `min`, `max`) devuelven una fila por grupo. Toda columna del `SELECT` que no está agregada
tiene que estar en el `GROUP BY`. Un promedio agregado puede esconder lo que pasa adentro de cada
grupo: es la paradoja de Simpson, en [sesgos](../Estadistica/sesgos.md), y la razón para desagregar
en el [análisis exploratorio](analisis-exploratorio.md).

## NULL: el valor que no es igual a nada

NULL significa «desconocido». PostgreSQL lo explica así: «Ordinary comparison operators yield null
(signifying "unknown"), not true or false, when either input is null», y advierte: «Do not write
`expression = NULL` because `NULL` is not "equal to" `NULL`». Se pregunta con `IS NULL`.

Los casos siguientes los corrió la base sobre la tabla de ejemplo, con una venta sin canal:

```sql
SELECT count(*) FROM ventas WHERE canal = NULL;        -- 0: nunca es verdadero
SELECT count(*) FROM ventas WHERE canal IS NULL;       -- 1
SELECT count(*) FROM ventas WHERE canal <> 'local';    -- 2: la venta sin canal no entra
SELECT count(*), count(canal) FROM ventas;             -- 5 y 4: count(columna) salta los NULL
```

Dos trampas más. `NOT IN` contra una subconsulta que trae algún NULL no devuelve ninguna fila:

```sql
-- Clientes que no refirieron a nadie: devuelve vacío si algún referido_por es NULL
SELECT nombre FROM clientes
WHERE id_cliente NOT IN (SELECT referido_por FROM clientes);
-- Se arregla filtrando: ... WHERE referido_por IS NOT NULL
```

Y un filtro en `WHERE` sobre la tabla de la derecha de un `LEFT JOIN` descarta las filas sin
pareja, que traen NULL ahí: el join se vuelve interno sin que se note. El filtro va en el `ON`:

```sql
-- Ventas en línea por cliente, incluidos los que no compraron
SELECT c.nombre, count(v.id_venta)
FROM clientes c
LEFT JOIN ventas v ON v.id_cliente = c.id_cliente AND v.canal = 'tienda'
GROUP BY c.nombre;
-- Con "WHERE v.canal = 'tienda'" desaparecen los clientes con 0
```

## Funciones de ventana: calcular sin agrupar

Una función de ventana, según PostgreSQL, «performs a calculation across a set of table rows that
are somehow related to the current row», y a diferencia de una agregación, «the rows retain their
separate identities». `PARTITION BY` define el grupo y el `ORDER BY` dentro de `OVER`, el orden.
Sirven para lo que en una planilla se hace arrastrando una fórmula: acumulados, número de compra,
compra anterior, participación en el total.

```sql
SELECT id_cliente, fecha, total,
       sum(total)   OVER (PARTITION BY id_cliente ORDER BY fecha) AS acumulado,
       row_number() OVER (PARTITION BY id_cliente ORDER BY fecha) AS n_compra,
       lag(fecha)   OVER (PARTITION BY id_cliente ORDER BY fecha) AS compra_anterior
FROM ventas;
```

Con `n_compra = 1` se encuentra la primera compra de cada cliente, que es la base de una
[tabla de cohortes](../Analitica-de-producto/Lectura-de-cohortes/armar-una-tabla-de-cohortes.md).
Con `lag` se calcula cuántos días pasan entre compras, que entra en la recencia de la
[segmentación RFM](segmentacion-de-clientes.md).

> [!NOTE]
> Sin fuente todavía: un libro o curso de referencia sobre SQL para análisis como tema. Los casos
> de `NOT IN` y `LEFT JOIN` con NULL están verificados corriendo las consultas, no en una fuente
> primaria.
