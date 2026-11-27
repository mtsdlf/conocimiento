---
resumen: >-
  INSERT agrega filas, UPDATE cambia las que cumplen una condición y DELETE las borra; el upsert
  inserta o actualiza según la fila ya exista, y RETURNING devuelve lo que se escribió sin otra
  consulta. Un UPDATE o un DELETE sin WHERE afecta a la tabla entera.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, INSERT (ON CONFLICT y Compatibility): https://www.postgresql.org/docs/current/sql-insert.html"
  - "PostgreSQL Documentation, UPDATE: https://www.postgresql.org/docs/current/sql-update.html"
  - "PostgreSQL Documentation, MERGE: https://www.postgresql.org/docs/current/sql-merge.html"
  - "PostgreSQL Documentation, 14.1 Using EXPLAIN (EXPLAIN ANALYZE dentro de una transacción): https://www.postgresql.org/docs/current/using-explain.html"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [INSERT, UPDATE, DELETE, upsert, RETURNING, MERGE, DML]
creado: 2026-11-27
revisado: 2026-11-27
---

# Modificar datos

INSERT agrega filas, UPDATE cambia las que cumplen una condición y DELETE las borra; el upsert
inserta o actualiza según la fila ya exista, y RETURNING devuelve lo que se escribió sin otra
consulta. Un UPDATE o un DELETE sin WHERE afecta a la tabla entera.

Cada escritura pasa por las restricciones que se declararon al [definir las tablas](definir-tablas.md):
un pedido con un cliente que no existe o un stock negativo se rechazan. Cuando varias escrituras
tienen que aplicarse juntas o ninguna (descontar stock y crear el pedido), van dentro de una
[transacción](../Transacciones/transaccion.md).

## INSERT y RETURNING

```sql
INSERT INTO clientes (nombre, email, ciudad)
VALUES ('Elena', 'elena@example.com', 'Mendoza')
RETURNING id;
```

Conviene nombrar siempre las columnas: si alguien agrega una columna a la tabla, un `INSERT` sin
lista de columnas se rompe o, peor, carga los valores corridos. `RETURNING` devuelve el `id` que
generó la base, y evita una segunda consulta para averiguarlo. Según la documentación, `RETURNING`
es una extensión de PostgreSQL; SQLite también la acepta (se comprobó al ejecutarlo). `INSERT ...
SELECT ...` carga el resultado de una consulta, por ejemplo desde una tabla de importación.

## UPDATE: siempre con WHERE

`UPDATE` cambia las filas que cumplen la condición; la documentación habla de "all rows that satisfy
the condition". Sin `WHERE`, todas cumplen: `UPDATE productos SET precio = precio * 1.10` aumenta
todos los precios. La documentación no lo dice con esas palabras; es la lectura directa de la
sintaxis, y es el error más caro de esta nota. Lo mismo vale para `DELETE FROM pedidos` sin `WHERE`.
No se encontró una fuente sobre protecciones de los motores contra este error.

La costumbre que lo previene es probar dentro de una transacción y mirar cuántas filas cambiaron
antes de confirmar:

```sql
BEGIN;
UPDATE productos SET precio = precio * 1.10 WHERE id = 1 RETURNING id, precio;
-- UPDATE 1: si dice otro número, ROLLBACK
ROLLBACK;   -- o COMMIT, si es lo esperado
```

La documentación de PostgreSQL usa la misma técnica para analizar un `UPDATE` con `EXPLAIN ANALYZE`
sin cambiar datos: `BEGIN; EXPLAIN ANALYZE UPDATE ...; ROLLBACK;`.

En PostgreSQL, `RETURNING` puede devolver el valor anterior y el nuevo con `old.` y `new.`
(`RETURNING old.precio AS antes, new.precio AS despues`). Es de versiones recientes: se probó en
PostgreSQL 18.4.

Un `UPDATE` puede tomar valores de otra tabla con `FROM` (extensión de PostgreSQL). La documentación
advierte que "you should ensure that the join produces at most one output row for each row to be
modified": si el join da dos filas para el mismo producto, cuál de los dos valores queda no está
definido.

## Descontar stock sin vender lo que no hay

El stock se descuenta con una condición en el mismo `UPDATE`, no leyendo primero y escribiendo
después:

```sql
UPDATE productos
SET stock = stock - 1
WHERE id = 3 AND stock >= 1
RETURNING stock;
```

Si no hay stock, actualiza cero filas y `RETURNING` no devuelve nada: la aplicación se entera de que
no se pudo vender. Leer el stock con un `SELECT` y después escribir el nuevo valor deja una ventana
en la que otra compra lee el mismo número. Por qué pasa y las otras salidas (bloqueo explícito,
bloqueo optimista) están en [concurrencia](../Transacciones/concurrencia.md). El `CHECK (stock >=
0)` de la tabla es la red de seguridad: si igual se intenta dejar el stock negativo, la base rechaza
la escritura.

## DELETE y las claves foráneas

`DELETE FROM pedidos WHERE id = 4` borra el pedido, y sus ítems se borran solos porque
`items_pedido` declara `ON DELETE CASCADE`. En cambio, `DELETE FROM clientes WHERE id = 1` falla
mientras el cliente tenga pedidos: la clave foránea de `pedidos` no tiene acción declarada y la
base rechaza el borrado ("violates foreign key constraint"). Qué acción conviene en cada clave está
en [definir tablas](definir-tablas.md#qué-pasa-al-borrar-un-cliente-con-pedidos).

Muchos sistemas no borran clientes ni pedidos: los marcan con una columna (`estado = 'cancelado'`,
`borrado_en`) para conservar la historia. Es una decisión de diseño, no de SQL.

## El upsert: insertar o actualizar

El upsert resuelve "si la fila ya existe, actualizala; si no, creala" en una sola sentencia
atómica. El caso típico es importar una lista de clientes donde algunos ya están cargados, o
procesar dos veces el mismo mensaje sin duplicar (la idea de la
[clave de idempotencia](../../Arquitectura/Sistemas-distribuidos/clave-de-idempotencia.md)). El patrón tiene tres partes:

1. **Una columna única que decide si la fila existe.** Para los clientes, el `email`. Sin un índice
   único sobre esa columna el upsert no funciona: PostgreSQL responde "there is no unique or
   exclusion constraint matching the ON CONFLICT specification".
2. **Qué hacer si no existe**: insertar.
3. **Qué hacer si existe**: actualizar algunas columnas con los valores nuevos, o no hacer nada.

En PostgreSQL:

```sql
INSERT INTO clientes (nombre, email, ciudad)
SELECT nombre, email, ciudad FROM clientes_import
ON CONFLICT (email) DO UPDATE
  SET nombre = EXCLUDED.nombre, ciudad = EXCLUDED.ciudad
RETURNING id, nombre;
```

`EXCLUDED` es la fila que se intentó insertar. `ON CONFLICT (email) DO NOTHING` deja la fila
existente como está; con `RETURNING`, según la documentación, solo se devuelven las filas realmente
insertadas o actualizadas.

La sintaxis es lo más distinto entre motores de todo SQL. La documentación de PostgreSQL dice que
`INSERT` "conforms to the SQL standard, except that the RETURNING clause is a PostgreSQL extension
[...] and the ability to specify an alternative action with ON CONFLICT". SQLite copia la sintaxis
de PostgreSQL, MySQL usa `ON DUPLICATE KEY UPDATE`, y la forma estándar es `MERGE`. Cómo se escribe
en cada uno está en la [ficha de dialectos](dialectos-de-sql.md#upsert).

Un efecto que se observó al ejecutarlo: en PostgreSQL, cada intento que termina en conflicto
consume un número de la secuencia de `id`, así que los `id` quedan con huecos. No es un error; los
`id` generados no prometen ser correlativos.

## MERGE, la forma estándar

`MERGE` compara una tabla de origen con la de destino y dice qué hacer cuando hay coincidencia y
cuando no. Según la documentación de PostgreSQL, "This command conforms to the SQL standard":

```sql
MERGE INTO clientes c
USING clientes_import i ON c.email = i.email
WHEN MATCHED THEN UPDATE SET ciudad = i.ciudad
WHEN NOT MATCHED THEN INSERT (nombre, email, ciudad) VALUES (i.nombre, i.email, i.ciudad);
```

Es más general que `ON CONFLICT`: puede borrar, puede tener varias condiciones y no necesita un
índice único (las tres cosas se comprobaron al ejecutarlo). SQLite no lo acepta (se comprobó al ejecutarlo). Para el upsert de una fila desde una
aplicación, en PostgreSQL se usa más `ON CONFLICT`.

## Para leer en la fuente

La página de `INSERT` de PostgreSQL, secciones "ON CONFLICT Clause" y "Compatibility": fijarse en
qué es estándar y qué es extensión.
