---
resumen: >-
  Ocho pasos para aprender SQL en orden, sobre las tablas de un comercio: en cada uno, la idea que
  hay que tener en la cabeza, una predicción, un ejemplo resuelto, un caso modificado y un
  ejercicio para hacer solo, con las respuestas escondidas y los recursos de práctica de afuera.
estado: borrador
estabilidad: semi
fuentes:
  - "SQLBolt: https://sqlbolt.com/"
  - "PostgreSQL Exercises: https://pgexercises.com/"
  - "Zi Chong Kao, Select Star SQL: https://selectstarsql.com/"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [aprender SQL, ejercicios de SQL, curso de SQL]
creado: 2026-11-27
revisado:
---

# Ruta de SQL

Ocho pasos para aprender SQL en orden, sobre las tablas de un comercio: en cada uno, la idea que
hay que tener en la cabeza, una predicción, un ejemplo resuelto, un caso modificado y un
ejercicio para hacer solo, con las respuestas escondidas y los recursos de práctica de afuera.

Cada paso corresponde a una nota de la vertical [SQL](../SQL/sql.md), que tiene la explicación
completa. La ruta da por sabido usar una planilla y nada más. Todas las respuestas salieron de
ejecutar las consultas en PostgreSQL 18.4 el 2026-11-27, y lo que se dice de SQLite, en SQLite
3.53.2: son las versiones que había instaladas, distintas de las vigentes de la
[ficha de motores](../Elegir-una-base/motores-de-bases-de-datos.md).

## Cómo usar cada paso

1. Leé el modelo mental y la nota enlazada.
2. Escribí tu predicción antes de abrir la respuesta. Equivocarse acá es lo que más enseña.
3. Leé el ejemplo resuelto y ejecutalo.
4. Hacé el caso modificado y el ejercicio solo, y recién después abrí las respuestas.
5. Terminá con los ejercicios de afuera que indica el paso.

## Preparar la base de práctica

Hace falta un PostgreSQL donde ejecutar. Sirve uno instalado en la computadora o cualquier servicio
que dé una consola de PostgreSQL. Creá las tablas y los datos con este script, que también usan los
ejemplos de las notas:

```sql
SET TimeZone = 'America/Argentina/Buenos_Aires';

CREATE TABLE clientes (
  id     integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nombre text NOT NULL,
  email  text UNIQUE,
  ciudad text
);
CREATE TABLE productos (
  id     integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nombre text NOT NULL,
  precio numeric(12,2) NOT NULL CHECK (precio > 0),
  stock  integer NOT NULL DEFAULT 0 CHECK (stock >= 0)
);
CREATE TABLE pedidos (
  id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  cliente_id integer NOT NULL REFERENCES clientes (id),
  fecha      timestamptz NOT NULL DEFAULT now(),
  envio      numeric(12,2) NOT NULL DEFAULT 0
);
CREATE TABLE items_pedido (
  pedido_id       integer NOT NULL REFERENCES pedidos (id) ON DELETE CASCADE,
  producto_id     integer NOT NULL REFERENCES productos (id),
  cantidad        integer NOT NULL CHECK (cantidad > 0),
  precio_unitario numeric(12,2) NOT NULL,
  PRIMARY KEY (pedido_id, producto_id)
);

INSERT INTO clientes (nombre, email, ciudad) VALUES
  ('Ana', 'ana@example.com', 'Rosario'),
  ('Bruno', 'bruno@example.com', 'Córdoba'),
  ('Carla', NULL, NULL),
  ('Diego', 'diego@example.com', 'Rosario');
INSERT INTO productos (nombre, precio, stock) VALUES
  ('Yerba 1 kg', 4500, 30), ('Mate', 12000, 5), ('Bombilla', 6000, 0);
INSERT INTO pedidos (cliente_id, fecha, envio) VALUES
  (1, '2026-10-02 10:00-03', 1500),
  (1, '2026-11-10 18:30-03', 0),
  (2, '2026-11-15 09:00-03', 2000),
  (4, '2026-09-20 12:00-03', 0);
INSERT INTO items_pedido VALUES
  (1, 1, 2, 4500), (1, 2, 1, 12000),
  (2, 1, 1, 4500),
  (3, 2, 1, 12000), (3, 3, 2, 6000),
  (4, 1, 3, 4200);
```

Con esos datos, Ana tiene dos pedidos (octubre y noviembre), Bruno uno (noviembre), Diego uno
(septiembre) y Carla ninguno, además de no tener email ni ciudad. La Bombilla no tiene stock.

## Paso 1: pedir filas

**Modelo mental.** Una consulta dice qué filas se quieren, no cómo buscarlas, y sus cláusulas se
evalúan en otro orden que el escrito: `FROM`, `WHERE`, `SELECT`, `ORDER BY`, `LIMIT`. Nota:
[consulta SELECT](../SQL/consulta-select.md).

**Predicción.** ¿Qué devuelve esto?

```sql
SELECT nombre FROM productos WHERE stock > 0 ORDER BY precio LIMIT 1;
```

<details><summary>Respuesta</summary>

`Yerba 1 kg`. `WHERE` deja la Yerba y el Mate (la Bombilla no tiene stock), `ORDER BY precio` los
ordena de menor a mayor y `LIMIT 1` se queda con el primero.

</details>

**Ejemplo resuelto.** Los productos sin stock:

```sql
SELECT nombre FROM productos WHERE stock = 0;   -- Bombilla
```

**Caso modificado.** Los clientes de Rosario, ordenados por nombre.

<details><summary>Respuesta</summary>

```sql
SELECT nombre FROM clientes WHERE ciudad = 'Rosario' ORDER BY nombre;   -- Ana, Diego
```

</details>

**Para hacer solo.** Los pedidos de noviembre de 2026, del más nuevo al más viejo, con su `id` y su
fecha.

<details><summary>Respuesta</summary>

```sql
SELECT id, fecha
FROM pedidos
WHERE fecha >= '2026-11-01' AND fecha < '2026-12-01'
ORDER BY fecha DESC;   -- 3, 2
```

El rango semiabierto (`>=` el primero, `<` el primero del mes siguiente) incluye todo noviembre
sin preocuparse por la hora del último día.

</details>

**Afuera.** Las lecciones 1 a 5 de [SQLBolt](https://sqlbolt.com/), que corren en el navegador sin
instalar nada, y la lección 12 sobre el orden de evaluación. Es la entrada más suave para quien
viene de planillas.

## Paso 2: unir tablas

**Modelo mental.** Un join combina cada fila de una tabla con las filas de otra que cumplen la
condición. El inner join descarta las que no tienen pareja; el left join las conserva con NULL.
Una fila con N parejas sale N veces. Nota: [join](../SQL/join.md).

**Predicción.** ¿Cuántas filas da `clientes JOIN pedidos ON pedidos.cliente_id = clientes.id`? ¿Y
con `LEFT JOIN`?

<details><summary>Respuesta</summary>

4 y 5. Con `JOIN` sale una fila por pedido (Ana dos veces, Bruno, Diego) y Carla no aparece. Con
`LEFT JOIN` se suma Carla, con el pedido vacío.

</details>

**Ejemplo resuelto.** Qué compró cada cliente, uniendo las cuatro tablas:

```sql
SELECT c.nombre, p.id AS pedido, pr.nombre AS producto, i.cantidad
FROM clientes c
JOIN pedidos p       ON p.cliente_id = c.id
JOIN items_pedido i  ON i.pedido_id = p.id
JOIN productos pr    ON pr.id = i.producto_id
ORDER BY p.id, pr.nombre;
```

Seis filas, una por ítem. Cada join agrega una tabla y su condición une la clave foránea con la
clave primaria.

**Caso modificado.** Los productos que Ana (`id` 1) nunca compró.

<details><summary>Respuesta</summary>

```sql
SELECT pr.nombre
FROM productos pr
WHERE NOT EXISTS (
  SELECT 1
  FROM items_pedido i
  JOIN pedidos p ON p.id = i.pedido_id
  WHERE p.cliente_id = 1 AND i.producto_id = pr.id
);   -- Bombilla
```

`NOT EXISTS` se ve a fondo en el paso 5; acá alcanza con leerlo como "no existe un ítem de Ana con
este producto".

</details>

**Para hacer solo.** Los clientes de Rosario con el `id` de cada uno de sus pedidos, incluidos los
que no tienen pedidos.

<details><summary>Respuesta</summary>

```sql
SELECT c.nombre, p.id
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
WHERE c.ciudad = 'Rosario'
ORDER BY p.id;   -- Ana 1, Ana 2, Diego 4
```

El filtro va en `WHERE` porque es sobre la tabla de la izquierda. Un filtro sobre `pedidos` iría
en el `ON`, como explica [join](../SQL/join.md#on-contra-where-en-un-left-join).

</details>

**Afuera.** Las lecciones 6 y 7 de SQLBolt y la categoría "Joins and Subqueries" de
[pgexercises](https://pgexercises.com/), que usa PostgreSQL sobre un único conjunto de datos.

## Paso 3: agrupar y sumar

**Modelo mental.** `GROUP BY` deja una fila por grupo, y cada columna de la salida tiene que tener
un solo valor por grupo: o está en el `GROUP BY` o va dentro de un agregado. `WHERE` filtra filas
antes de agrupar; `HAVING`, grupos después. Nota: [agregación](../SQL/agregacion.md).

**Predicción.** ¿Qué valores le dan a Carla `count(*)` y `count(p.id)` en esta consulta?

```sql
SELECT c.nombre, count(*), count(p.id)
FROM clientes c LEFT JOIN pedidos p ON p.cliente_id = c.id
GROUP BY c.id, c.nombre;
```

<details><summary>Respuesta</summary>

1 y 0. El LEFT JOIN le dejó una fila con el pedido en NULL: `count(*)` cuenta esa fila y
`count(p.id)` no cuenta el NULL. Para contar pedidos, `count(p.id)`.

</details>

**Ejemplo resuelto.** Unidades e importe vendido por producto:

```sql
SELECT pr.nombre,
       sum(i.cantidad) AS unidades,
       sum(i.cantidad * i.precio_unitario) AS importe
FROM productos pr
LEFT JOIN items_pedido i ON i.producto_id = pr.id
GROUP BY pr.id, pr.nombre
ORDER BY importe DESC;
-- Yerba 1 kg 6 26100.00 / Mate 2 24000.00 / Bombilla 2 12000.00
```

El importe usa `precio_unitario` del ítem, no el precio actual del producto: la Yerba de Diego se
vendió a 4200.

**Caso modificado.** El total vendido por cliente en noviembre de 2026, incluidos los que no
compraron, con 0 en vez de vacío.

<details><summary>Respuesta</summary>

```sql
SELECT c.nombre, coalesce(sum(i.cantidad * i.precio_unitario), 0) AS total
FROM clientes c
LEFT JOIN pedidos p      ON p.cliente_id = c.id
                        AND p.fecha >= '2026-11-01' AND p.fecha < '2026-12-01'
LEFT JOIN items_pedido i ON i.pedido_id = p.id
GROUP BY c.id, c.nombre
ORDER BY total DESC;   -- Bruno 24000, Ana 4500, Diego 0, Carla 0
```

La explicación pieza por pieza está en [agregación](../SQL/agregacion.md#el-total-vendido-por-cliente-incluidos-los-que-no-compraron).

</details>

**Para hacer solo.** Los clientes que compraron más de 20000 en total, sumando todos sus pedidos.

<details><summary>Respuesta</summary>

```sql
SELECT c.nombre, sum(i.cantidad * i.precio_unitario) AS total
FROM clientes c
JOIN pedidos p      ON p.cliente_id = c.id
JOIN items_pedido i ON i.pedido_id = p.id
GROUP BY c.id, c.nombre
HAVING sum(i.cantidad * i.precio_unitario) > 20000;   -- Ana 25500, Bruno 24000
```

La condición va en `HAVING` porque usa un agregado.

</details>

**Afuera.** La categoría "Aggregates" de pgexercises, y los capítulos 3 y 4 de
[Select Star SQL](https://selectstarsql.com/), un libro interactivo gratuito ("free of charge, free
of ads and doesn't require registration") que trabaja agregación y joins con datos reales.

## Paso 4: convivir con NULL

**Modelo mental.** NULL es "no se sabe", y comparar con algo que no se sabe da desconocido. `WHERE`
solo deja pasar lo verdadero, así que las filas con NULL desaparecen de cualquier comparación que
no pregunte por NULL. Nota: [NULL y tipos](../SQL/null-y-tipos.md).

**Predicción.** ¿Qué número devuelve esto?

```sql
SELECT count(*) FROM clientes WHERE ciudad <> 'Córdoba';
```

<details><summary>Respuesta</summary>

2: Ana y Diego. Carla no tiene ciudad, y `NULL <> 'Córdoba'` da desconocido.

</details>

**Ejemplo resuelto.** Para contar a Carla también:

```sql
SELECT count(*) FROM clientes WHERE ciudad IS DISTINCT FROM 'Córdoba';   -- 3
```

`IS DISTINCT FROM` trata al NULL como un valor más. La alternativa es
`WHERE ciudad <> 'Córdoba' OR ciudad IS NULL`.

**Caso modificado.** La lista de clientes con su email, mostrando "(sin email)" donde falta.

<details><summary>Respuesta</summary>

```sql
SELECT nombre, coalesce(email, '(sin email)') AS email FROM clientes;
```

</details>

**Para hacer solo.** Sin ejecutarla, ¿qué devuelve `SELECT count(email), count(*) FROM clientes;`?

<details><summary>Respuesta</summary>

3 y 4. `count(email)` no cuenta el NULL de Carla.

</details>

**Afuera.** La lección de SQLBolt sobre NULL.

## Paso 5: consultas dentro de consultas

**Modelo mental.** Una subconsulta aporta un valor, una lista o una tabla a la consulta de afuera.
`EXISTS` pregunta si hay al menos una pareja y no repite filas. Una CTE (`WITH`) le pone nombre a un
paso intermedio. Nota: [subconsultas y CTE](../SQL/subconsultas-y-cte.md).

**Predicción.** ¿Qué devuelve esto?

```sql
SELECT nombre FROM clientes
WHERE ciudad NOT IN (SELECT ciudad FROM clientes WHERE nombre = 'Carla');
```

<details><summary>Respuesta</summary>

Ninguna fila. La subconsulta devuelve la ciudad de Carla, que es NULL, y "no está en (NULL)" da
desconocido para todos. Es la trampa de `NOT IN`, en
[subconsultas y CTE](../SQL/subconsultas-y-cte.md#not-in-con-un-null-no-devuelve-nada).

</details>

**Ejemplo resuelto.** Los clientes que compraron alguna vez, sin repetir a Ana:

```sql
SELECT c.nombre
FROM clientes c
WHERE EXISTS (SELECT 1 FROM pedidos p WHERE p.cliente_id = c.id);   -- Ana, Bruno, Diego
```

**Caso modificado.** Los productos que no se vendieron en octubre de 2026.

<details><summary>Respuesta</summary>

```sql
SELECT pr.nombre
FROM productos pr
WHERE NOT EXISTS (
  SELECT 1
  FROM items_pedido i
  JOIN pedidos p ON p.id = i.pedido_id
  WHERE i.producto_id = pr.id
    AND p.fecha >= '2026-10-01' AND p.fecha < '2026-11-01'
);   -- Bombilla
```

</details>

**Para hacer solo.** El último pedido de cada cliente que compró: `cliente_id`, `id` del pedido y
fecha. Con cualquiera de las formas.

<details><summary>Respuesta</summary>

Ana 2, Bruno 3, Diego 4. Las cuatro formas (subconsulta correlacionada, ventana, `DISTINCT ON` y
`LATERAL`), con sus diferencias ante empates, están en
[subconsultas y CTE](../SQL/subconsultas-y-cte.md#el-último-pedido-de-cada-cliente-de-cuatro-formas).

</details>

**Afuera.** La categoría "Recursive" de pgexercises, para las CTE recursivas. SQLBolt solo menciona
las subconsultas como tema extra.

## Paso 6: calcular sin colapsar filas

**Modelo mental.** Una función de ventana calcula sobre un grupo de filas (la partición) y le pone
el resultado a cada fila, sin juntarlas como `GROUP BY`. Nota:
[funciones de ventana](../SQL/funciones-de-ventana.md).

**Predicción.** ¿Cuántas filas devuelve esto, y qué valor tiene la última columna para el pedido 1?

```sql
SELECT id, cliente_id, count(*) OVER (PARTITION BY cliente_id) AS pedidos_del_cliente
FROM pedidos;
```

<details><summary>Respuesta</summary>

Cuatro filas, una por pedido; con `GROUP BY cliente_id` serían tres. El pedido 1 dice 2, porque Ana
tiene dos pedidos.

</details>

**Ejemplo resuelto.** El porcentaje de cada ítem en el total de su pedido:

```sql
SELECT pedido_id, producto_id,
       round(100 * cantidad * precio_unitario
             / sum(cantidad * precio_unitario) OVER (PARTITION BY pedido_id), 1) AS porcentaje
FROM items_pedido;
-- pedido 1: 42.9 y 57.1; pedido 3: 50.0 y 50.0
```

**Caso modificado.** Numerar los pedidos de cada cliente del primero al último.

<details><summary>Respuesta</summary>

```sql
SELECT cliente_id, id,
       row_number() OVER (PARTITION BY cliente_id ORDER BY fecha) AS numero
FROM pedidos;   -- Ana: 1 y 2; Bruno: 1; Diego: 1
```

</details>

**Para hacer solo.** Cuántos días pasaron entre cada pedido y el anterior del mismo cliente.

<details><summary>Respuesta</summary>

```sql
SELECT cliente_id, id,
       fecha::date - lag(fecha::date) OVER (PARTITION BY cliente_id ORDER BY fecha) AS dias
FROM pedidos;
```

El segundo pedido de Ana da 39; los demás, NULL, porque no tienen pedido anterior.

</details>

**Afuera.** Ninguno de los tres recursos tiene una sección fuerte de ventanas: pgexercises las
menciona sin categoría propia y SQLBolt no las cubre. El tutorial 3.5 "Window Functions" de la
documentación de PostgreSQL es la mejor lectura para este paso.

## Paso 7: escribir datos

**Modelo mental.** `UPDATE` y `DELETE` afectan a todas las filas que cumplen el `WHERE`, y sin
`WHERE` a todas. Se prueban dentro de `BEGIN` ... `ROLLBACK` mirando cuántas filas tocaron. Nota:
[modificar datos](../SQL/modificar-datos.md).

**Predicción.** ¿Qué responde la base?

```sql
UPDATE productos SET stock = stock - 1 WHERE id = 3 AND stock >= 1;
```

<details><summary>Respuesta</summary>

`UPDATE 0`. La Bombilla tiene stock 0, así que ninguna fila cumple la condición y no se vende lo
que no hay. Por qué conviene descontar así está en
[modificar datos](../SQL/modificar-datos.md#descontar-stock-sin-vender-lo-que-no-hay).

</details>

**Ejemplo resuelto.** Cargar un cliente que puede existir ya, identificado por email:

```sql
BEGIN;
INSERT INTO clientes (nombre, email, ciudad)
VALUES ('Bruno Díaz', 'bruno@example.com', 'Córdoba')
ON CONFLICT (email) DO UPDATE SET nombre = EXCLUDED.nombre
RETURNING id, nombre;   -- 2, Bruno Díaz: actualizó, no insertó
ROLLBACK;
```

**Caso modificado.** Lo mismo, pero si el email ya existe no se toca nada.

<details><summary>Respuesta</summary>

`ON CONFLICT (email) DO NOTHING`. Con `RETURNING id` no devuelve ninguna fila, y la base responde
`INSERT 0 0`.

</details>

**Para hacer solo.** Subir 10 % el precio de los productos con menos de 10 unidades de stock,
dentro de una transacción, verificando cuántos cambiaron antes de confirmar.

<details><summary>Respuesta</summary>

```sql
BEGIN;
UPDATE productos SET precio = precio * 1.10 WHERE stock < 10 RETURNING id, nombre, precio;
-- UPDATE 2: Mate 13200.00, Bombilla 6600.00
ROLLBACK;   -- o COMMIT si es lo que se quería
```

</details>

**Afuera.** La categoría "Modifying data" de pgexercises y las lecciones de SQLBolt sobre
`INSERT`, `UPDATE` y `DELETE`.

## Paso 8: tablas e índices

**Modelo mental.** Las restricciones de la tabla son reglas que la base hace cumplir a cualquiera.
Un índice deja encontrar filas sin leer la tabla entera, y `EXPLAIN` muestra si se usa. Notas:
[definir tablas](../SQL/definir-tablas.md) e [índice](../SQL/indice.md).

**Predicción.** Con `CHECK (descuento BETWEEN 0 AND 50)` en una columna sin `NOT NULL`, ¿la base
acepta un descuento NULL?

<details><summary>Respuesta</summary>

Sí. Un `CHECK` se cumple si la expresión da verdadero o NULL. Para prohibir el vacío hace falta
`NOT NULL`.

</details>

**Ejemplo resuelto.** Con cuatro pedidos, el motor recorre la tabla entera aunque haya índice,
porque es más barato. Para ver un índice en acción hacen falta más filas:

```sql
INSERT INTO clientes (nombre, email)
SELECT 'Cliente ' || g, 'c' || g || '@example.com' FROM generate_series(1, 5000) g;

INSERT INTO pedidos (cliente_id, fecha)
SELECT c.id, timestamptz '2025-01-01' + g * interval '5 minutes'
FROM generate_series(1, 100000) g
JOIN clientes c ON c.email = 'c' || (1 + g % 5000) || '@example.com';

ANALYZE;
EXPLAIN ANALYZE SELECT * FROM pedidos WHERE cliente_id = 42;   -- Seq Scan

CREATE INDEX pedidos_cliente_id_idx ON pedidos (cliente_id);
EXPLAIN ANALYZE SELECT * FROM pedidos WHERE cliente_id = 42;   -- Bitmap Index Scan
```

`generate_series` es de PostgreSQL. Cada cliente generado queda con 20 pedidos, y la tabla, con
100.004 (los 4 del script inicial más los 100.000). Los pedidos se asignan por email y no por número
de cliente porque un `INSERT ... ON CONFLICT` del paso 7 gasta números de la secuencia aunque no
inserte ni se confirme, y los clientes nuevos pueden no empezar en el 5. Compará el
`Execution Time` de los dos planes.

**Caso modificado.** Creá un índice en `pedidos (fecha)` y mirá el plan de
`SELECT count(*) FROM pedidos WHERE fecha::date = '2025-06-01';`. ¿Usa el índice?

<details><summary>Respuesta</summary>

No: el plan es `Seq Scan`. La conversión `fecha::date` transforma la columna, y el índice está
ordenado por la columna sin transformar.

</details>

**Para hacer solo.** Reescribí esa consulta para que use el índice.

<details><summary>Respuesta</summary>

```sql
SELECT count(*) FROM pedidos
WHERE fecha >= '2025-06-01' AND fecha < '2025-06-02';   -- Index Only Scan using pedidos_fecha_idx
```

</details>

**Afuera.** La lección de SQLBolt sobre crear tablas. Ninguno de los tres recursos cubre índices;
para eso, el capítulo "The Where Clause" de [Use The Index, Luke!](https://use-the-index-luke.com/).

## Los tres recursos de práctica

| Recurso | Qué es | Para qué paso |
|---|---|---|
| [SQLBolt](https://sqlbolt.com/) | 18 lecciones interactivas en el navegador | 1 a 4, 7 y 8; la entrada más suave; no cubre ventanas ni CTE |
| [pgexercises](https://pgexercises.com/) | preguntas sobre un único conjunto de datos, en PostgreSQL, con licencia CC BY-SA 3.0 | 2, 3, 5 y 7; categorías Basic, Joins and Subqueries, Modifying data, Aggregates, Date, String y Recursive |
| [Select Star SQL](https://selectstarsql.com/) | libro interactivo de cinco capítulos, gratuito, con datos CC0 | 3, como cierre de agregación y joins |

Ninguno de los tres cubre bien las funciones de ventana ni los índices. Las páginas de SQLBolt y de
pgexercises no dicen si son gratuitas.
