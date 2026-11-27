---
resumen: >-
  Un join combina las filas de dos tablas según una condición, casi siempre que la clave foránea de
  una coincida con la clave primaria de la otra. El tipo de join decide qué pasa con las filas que
  no tienen pareja, y unir una fila con varias la repite.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 7.2.1 Joined Tables: https://www.postgresql.org/docs/current/queries-table-expressions.html"
  - "MySQL 8.4 Reference Manual, JOIN Clause: https://dev.mysql.com/doc/refman/8.4/en/join.html"
  - "PostgreSQL Documentation, 9.25 Subquery Expressions (EXISTS): https://www.postgresql.org/docs/current/functions-subquery.html"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [JOIN, unión de tablas, inner join, left join, outer join, fan-out]
creado: 2026-11-27
revisado: 2026-11-27
---

# Join

Un join combina las filas de dos tablas según una condición, casi siempre que la clave foránea de
una coincida con la clave primaria de la otra. El tipo de join decide qué pasa con las filas que
no tienen pareja, y unir una fila con varias la repite.

Es lo que hace útil al [modelo relacional](../Modelos-de-datos/base-relacional.md): los datos se
guardan una vez cada uno, en su tabla, y se juntan al consultar. Se evalúa en el `FROM`, el primer
paso de la [consulta SELECT](consulta-select.md).

Los resultados de esta nota salen de cuatro clientes de prueba: Ana (dos pedidos), Bruno (uno),
Carla (ninguno, y sin ciudad) y Diego (uno, de septiembre).

## Inner join: solo las filas con pareja

`JOIN` (o `INNER JOIN`) deja las combinaciones que cumplen la condición. Según la documentación de
PostgreSQL, "for each row R1 of T1, the joined table has a row for each row in T2 that satisfies the
join condition".

```sql
SELECT c.nombre, p.id AS pedido, p.fecha::date
FROM clientes c
JOIN pedidos p ON p.cliente_id = c.id;
```

Devuelve cuatro filas: Ana dos veces, Bruno y Diego. Carla no aparece, porque no tiene pedidos.
Las letras `c` y `p` son alias de tabla; hacen falta en cuanto dos tablas tienen una columna con el
mismo nombre (las dos tienen `id`).

## Left join: todas las filas de la izquierda

`LEFT JOIN` conserva cada fila de la tabla de la izquierda aunque no tenga pareja, y completa con
NULL las columnas de la derecha. La documentación lo dice así: "the joined table always has at least
one row for each row in T1".

```sql
SELECT c.nombre, p.id AS pedido
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id;
```

Ahora salen cinco filas, y la de Carla trae `pedido` vacío. Es el join de las preguntas que dicen
"incluidos los que no": clientes sin compras, productos sin ventas.

`RIGHT JOIN` es lo mismo con los lados cambiados. La documentación de MySQL recomienda no usarlo:
"To keep code portable across databases, it is recommended that you use LEFT JOIN instead of RIGHT
JOIN". `FULL JOIN` conserva las filas sin pareja de los dos lados; PostgreSQL y SQLite lo tienen (en
SQLite, comprobado en 3.53.2), y
la gramática de JOIN de MySQL 8.4 no lo documenta (ver la [ficha de dialectos](dialectos-de-sql.md)).

## ON contra WHERE en un left join

Dónde se pone un filtro sobre la tabla de la derecha cambia el resultado. La documentación de
PostgreSQL: "a restriction placed in the ON clause is processed before the join, while a
restriction placed in the WHERE clause is processed after the join. That does not matter with inner
joins, but it matters a lot with outer joins."

Clientes con sus pedidos de noviembre, incluidos los que no compraron. Con el filtro en `WHERE`:

```sql
SELECT c.nombre, p.id AS pedido
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
WHERE p.fecha >= '2026-11-01' AND p.fecha < '2026-12-01';
```

Devuelve solo a Ana y a Bruno. Carla y Diego desaparecen: el LEFT JOIN les dio una fila con
`p.fecha` en NULL, y `WHERE` la descartó porque comparar NULL con una fecha da desconocido (la
[lógica de tres valores](null-y-tipos.md#la-lógica-de-tres-valores)). El LEFT JOIN quedó convertido
en un inner join sin que nada avise.

Con el filtro en `ON`, el join busca pareja solo entre los pedidos de noviembre y conserva a todos
los clientes:

```sql
SELECT c.nombre, p.id AS pedido
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
                   AND p.fecha >= '2026-11-01' AND p.fecha < '2026-12-01';
```

Devuelve a los cuatro, con Carla y Diego sin pedido. La regla práctica: en un LEFT JOIN, las
condiciones sobre la tabla de la derecha van en `ON`; las condiciones sobre la de la izquierda van
en `WHERE`.

## Un join que multiplica filas

Unir una fila con N filas de otra tabla produce N filas, y cada una repite los datos de la primera.
Eso es correcto mientras se miren las filas; se vuelve un error al sumar. Al problema se lo llama
fan-out. La documentación oficial no lo trata como tema; se deriva de la definición de inner join
citada arriba. Cómo lo chequea un analista y qué pasa con las herramientas de BI que lo corrigen
solas está en [SQL para análisis](../../Datos/Analisis/sql-para-analisis.md#un-join-que-multiplica-filas).

El envío es una columna del pedido. El pedido 1 de Ana costó 1500 de envío y tiene dos ítems:

```sql
SELECT p.cliente_id, sum(p.envio) AS envio, sum(i.cantidad * i.precio_unitario) AS productos
FROM pedidos p
JOIN items_pedido i ON i.pedido_id = p.id
GROUP BY p.cliente_id;
```

| cliente_id | envio | productos |
|---|---|---|
| 1 | 3000.00 | 25500.00 |
| 2 | 4000.00 | 24000.00 |
| 4 | 0.00 | 12600.00 |

La suma de productos está bien; la del envío está duplicada, porque cada pedido apareció una vez por
ítem. No hay error ni advertencia. La salida es agregar cada tabla a su nivel (su
[grano](../../Datos/Analisis/sql-para-analisis.md#el-grano-qué-es-una-fila), lo que representa una
fila) antes de unirlas:

```sql
SELECT p.cliente_id, sum(p.envio) AS envio, sum(t.productos) AS productos
FROM pedidos p
JOIN (SELECT pedido_id, sum(cantidad * precio_unitario) AS productos
      FROM items_pedido
      GROUP BY pedido_id) t ON t.pedido_id = p.id
GROUP BY p.cliente_id;
```

Ahora el envío da 1500, 2000 y 0. Cuando solo hace falta saber si existe una pareja (clientes que
compraron alguna vez), `EXISTS` no multiplica: según la documentación de PostgreSQL, se comporta
"like an inner join on col2, but it produces at most one output row for each tab1 row". Está en
[subconsultas y CTE](subconsultas-y-cte.md). La señal de alarma es un join de uno a muchos seguido de
`sum` o `count` sobre columnas del lado "uno"; [agregación](agregacion.md) vuelve sobre esto.

## Anti-join: las filas sin pareja

Para los clientes que nunca compraron hay dos formas. Con LEFT JOIN y la pareja en NULL, el patrón
que documenta MySQL:

```sql
SELECT c.nombre
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
WHERE p.id IS NULL;
```

O con `NOT EXISTS`, que se lee más directo y no tiene problemas con NULL. Las dos devuelven a Carla.
`NOT IN (SELECT cliente_id FROM pedidos)` también funciona acá, pero solo porque `cliente_id` no
admite NULL; con una columna que los admite, `NOT IN` no devuelve nada (ver
[subconsultas y CTE](subconsultas-y-cte.md#not-in-con-un-null-no-devuelve-nada)).

## Cross join y autojoin

`CROSS JOIN` combina cada fila de una tabla con cada fila de la otra, sin condición. Según la
documentación de PostgreSQL, "If the tables have N and M rows respectively, the joined table will
have N * M rows": cuatro clientes por tres productos dan 12 filas. Sirve para armar todas las
combinaciones (cada cliente con cada producto, para ver qué no compró nadie) y aparece por error
cuando se olvida la condición de un join.

Un autojoin une una tabla consigo misma, con dos alias. Clientes de la misma ciudad:

```sql
SELECT a.nombre, b.nombre AS vecino, a.ciudad
FROM clientes a
JOIN clientes b ON b.ciudad = a.ciudad AND b.id > a.id;
```

Devuelve Ana y Diego, de Rosario. `b.id > a.id` evita que cada cliente se empareje consigo mismo y
que cada par salga dos veces. El caso típico es una tabla que se apunta a sí misma, como un cliente
que fue referido por otro cliente. No se encontró una página de documentación oficial dedicada al
autojoin; el ejemplo es propio.

## Para leer en la fuente

La sección 7.2.1 "Joined Tables" de la documentación de PostgreSQL trae los tipos de join con
tablas de ejemplo; conviene leer la parte de ON contra WHERE y comparar con el ejemplo de noviembre
de arriba.
