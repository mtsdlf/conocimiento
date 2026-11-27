---
resumen: >-
  Definir una tabla es declarar sus columnas, sus tipos y las reglas que la base hace cumplir
  (clave primaria, claves foráneas, NOT NULL, UNIQUE, CHECK); los cambios posteriores se aplican con
  migraciones versionadas, y una vista guarda una consulta con nombre.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 5.5 Constraints: https://www.postgresql.org/docs/current/ddl-constraints.html"
  - "PostgreSQL Documentation, ALTER TABLE (sección Notes): https://www.postgresql.org/docs/current/sql-altertable.html"
  - "PostgreSQL Documentation, CREATE MATERIALIZED VIEW: https://www.postgresql.org/docs/current/sql-creatematerializedview.html"
  - "Redgate Flyway, Migrations: https://documentation.red-gate.com/fd/migrations-271585107.html"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [CREATE TABLE, DDL, restricciones, constraints, migración, migrations, vista, view, vista materializada]
creado: 2026-11-27
revisado: 2026-11-27
---

# Definir tablas

Definir una tabla es declarar sus columnas, sus tipos y las reglas que la base hace cumplir
(clave primaria, claves foráneas, NOT NULL, UNIQUE, CHECK); los cambios posteriores se aplican con
migraciones versionadas, y una vista guarda una consulta con nombre.

Es lo que convierte la idea del [modelo relacional](../Modelos-de-datos/base-relacional.md) en
tablas concretas. Qué tablas hacen falta y cómo se reparten los datos entre ellas es diseño de
datos; acá se queda la parte de SQL.

## Las cuatro tablas del comercio

```sql
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
```

Es un ejemplo propio, ejecutado en PostgreSQL 18.4. Algunas decisiones que conviene ver:

- **`GENERATED ALWAYS AS IDENTITY`** hace que la base numere los `id`. La forma de pedirlo cambia
  entre motores.
- **`precio_unitario` está en `items_pedido`** aunque el precio ya esté en `productos`: el pedido
  tiene que recordar cuánto se cobró, aunque el precio del producto cambie después.
- **`items_pedido` tiene una clave primaria de dos columnas**: un producto aparece una vez por
  pedido, con su cantidad.
- **El dinero es `numeric` y la fecha es `timestamptz`**, por las razones de
  [NULL y tipos](null-y-tipos.md).

## Las restricciones son reglas que nadie se puede saltear

Una restricción declarada en la tabla se cumple para cualquier programa, script o persona que
escriba en la base, no solo para la aplicación que la validó. Ese es el motivo para declararlas
aunque la aplicación también valide.

| Restricción | Qué impide | Detalle que sorprende |
|---|---|---|
| `NOT NULL` | que falte el dato | es la única que impide el vacío |
| `UNIQUE` | dos filas con el mismo valor | según la documentación, "two null values are not considered equal", así que admite varios NULL (salvo con `NULLS NOT DISTINCT`) |
| `PRIMARY KEY` | filas sin identificar o repetidas | equivale a único más no nulo |
| `REFERENCES` (clave foránea) | apuntar a una fila que no existe | decide qué pasa al borrar la fila apuntada (abajo) |
| `CHECK (...)` | valores fuera de una regla | se cumple si la expresión da "true or the null value": deja pasar NULL |

Que `CHECK` deje pasar NULL se ve con un descuento que tiene que estar entre 0 y 50: `CHECK
(descuento BETWEEN 0 AND 50)` rechaza un 60 y acepta un NULL. Si el descuento es obligatorio, hace
falta además `NOT NULL`. Es la [lógica de tres valores](null-y-tipos.md#la-lógica-de-tres-valores)
aplicada a una regla.

## Qué pasa al borrar un cliente con pedidos

Cada clave foránea dice qué hacer cuando se borra la fila a la que apunta. Según la documentación de
PostgreSQL, "The default ON DELETE action is ON DELETE NO ACTION": el borrado se rechaza si quedan
filas que apuntan. Las otras opciones son `RESTRICT` (parecida, pero que no se puede postergar al
final de la transacción), `CASCADE` (borra también las filas que apuntan), `SET NULL` y
`SET DEFAULT`.

En el comercio, `pedidos.cliente_id` no declara acción, así que no se puede borrar un cliente que
tiene pedidos: la historia de ventas no se pierde por accidente. `items_pedido.pedido_id` declara
`CASCADE`, porque un ítem no tiene sentido sin su pedido. Según el resumen de la documentación,
`CASCADE` conviene solo cuando las filas hijas no pueden existir sin la madre.

## Cambiar una tabla que ya tiene datos

Las tablas cambian: una columna nueva, una restricción más. `ALTER TABLE` hace el cambio, y el
riesgo es el bloqueo: según la documentación de PostgreSQL, "An ACCESS EXCLUSIVE lock is acquired
unless explicitly noted", y mientras dura nadie puede leer ni escribir esa tabla.

```sql
ALTER TABLE pedidos
  ADD COLUMN estado text NOT NULL DEFAULT 'pendiente'
  CHECK (estado IN ('pendiente', 'pagado', 'enviado', 'cancelado'));
```

Agregar una columna con un valor por defecto constante es rápido aunque la tabla sea grande: el
valor se guarda en los metadatos, "making the ALTER TABLE very fast even on large tables". Con un
valor por defecto que cambia en cada fila (como `clock_timestamp()`), la base reescribe la tabla
entera y sus índices. Para agregar una clave foránea a una tabla grande, la documentación describe
un camino en dos pasos que bloquea menos: crearla con `NOT VALID` y después validarla con `VALIDATE
CONSTRAINT`.

## Migraciones: los cambios de esquema como código

Una migración es un archivo con un cambio de esquema (un `CREATE TABLE`, un `ALTER TABLE`) que se
guarda en el repositorio junto al código y se aplica en orden en cada base: desarrollo, prueba y
producción. Así todas las bases tienen el mismo esquema y se sabe qué cambió y cuándo. Flyway, una
de las herramientas que lo hacen, describe migraciones "versioned or repeatable or baseline" y
registra las ya aplicadas en una tabla de historial dentro de la misma base.

La práctica que se suele recomendar es no editar una migración ya aplicada y escribir una nueva que
corrija, para que el historial sea el mismo en todas las bases.

> [!NOTE] Sin fuente todavía: la convención de nombres de los archivos de migración, la regla de no
> editar una migración aplicada y la verificación con sumas de control no se confirmaron en una
> fuente primaria. Las herramientas concretas van en una ficha que todavía no existe.

## Vistas: una consulta con nombre

Una vista guarda una consulta y se usa como si fuera una tabla:

```sql
CREATE VIEW ventas_por_cliente AS
SELECT c.id, c.nombre, coalesce(sum(i.cantidad * i.precio_unitario), 0) AS total
FROM clientes c
LEFT JOIN pedidos p      ON p.cliente_id = c.id
LEFT JOIN items_pedido i ON i.pedido_id = p.id
GROUP BY c.id, c.nombre;

SELECT * FROM ventas_por_cliente WHERE total > 0;
```

La vista no guarda datos: cada vez que se consulta, se ejecuta la consulta de adentro, así que
siempre está al día. Sirve para no repetir un cálculo en diez lugares y para darle a alguien acceso
a un resumen sin darle acceso a las tablas.

Una **vista materializada** sí guarda el resultado. Según la documentación de PostgreSQL, la consulta
"is executed and used to populate the view at the time the command is issued [...] and may be
refreshed later using REFRESH MATERIALIZED VIEW". No se actualiza sola: al ejecutarlo con un ítem
nuevo, la vista común mostró 31500 y la materializada siguió en 25500 hasta el `REFRESH`. Sirve para
cálculos caros que se pueden mostrar con un rato de atraso, como un tablero.

## Para leer en la fuente

La sección 5.5 "Constraints" de la documentación de PostgreSQL, con ejemplos de cada restricción;
fijarse en la frase sobre CHECK y NULL. Para cambios en tablas con datos, la sección "Notes" de la
página de `ALTER TABLE`.
