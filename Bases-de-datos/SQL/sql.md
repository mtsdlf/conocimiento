---
resumen: >-
  SQL es el lenguaje con que se consulta, se modifica y se define una base relacional: se escribe
  qué filas se quieren y el motor decide cómo buscarlas. Casi todos los motores relacionales lo
  hablan, cada uno con su dialecto.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, cap. 7 Queries: https://www.postgresql.org/docs/current/queries-overview.html"
  - "PostgreSQL Documentation, SELECT: https://www.postgresql.org/docs/current/sql-select.html"
  - "Markus Winand, modern-sql.com, The SQL Standard: https://modern-sql.com/standard"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [Structured Query Language, lenguaje SQL]
creado: 2026-11-27
revisado: 2026-11-27
---

# SQL

SQL es el lenguaje con que se consulta, se modifica y se define una base relacional: se escribe
qué filas se quieren y el motor decide cómo buscarlas. Casi todos los motores relacionales lo
hablan, cada uno con su dialecto.

Es la vertical más honda de [Bases de datos](../bases-de-datos.md). Se apoya en el
[modelo relacional](../Modelos-de-datos/base-relacional.md), que pone las tablas y las claves, y
le pasa a [Transacciones](../Transacciones/transacciones.md) las escrituras que tienen que contar
como una sola. El uso de SQL para análisis (cohortes, almacenes analíticos) está en
[Datos](../../Datos/datos.md); acá se queda el lenguaje, del lado de quien construye un sistema.

## Las cuatro tablas de todos los ejemplos

Todas las notas de la vertical usan el mismo comercio, con cuatro tablas. La definición completa,
con sus restricciones, está en [definir tablas](definir-tablas.md).

| Tabla | Columnas | Qué guarda |
|---|---|---|
| `clientes` | `id`, `nombre`, `email`, `ciudad` | quien compra; `email` y `ciudad` pueden faltar |
| `productos` | `id`, `nombre`, `precio`, `stock` | lo que se vende |
| `pedidos` | `id`, `cliente_id`, `fecha`, `envio` | cada compra, con el costo de envío del pedido entero |
| `items_pedido` | `pedido_id`, `producto_id`, `cantidad`, `precio_unitario` | qué productos lleva cada pedido, con el precio de ese momento |

El SQL es de PostgreSQL. Lo que es extensión de PostgreSQL y no del estándar se marca en cada
caso, y la [ficha de dialectos](dialectos-de-sql.md) dice cómo se escribe en otros motores. Los
resultados que se muestran salieron de ejecutar las consultas en PostgreSQL 18.4 con datos de
prueba, el 2026-11-27, y los contrastes con SQLite, en SQLite 3.53.2. Son las versiones que había
instaladas, distintas de las vigentes que lista la
[ficha de motores](../Elegir-una-base/motores-de-bases-de-datos.md).

## Una consulta dice qué, no cómo

Una consulta SQL describe el resultado: qué columnas, de qué tablas, con qué condición. No dice si
el motor recorre la tabla entera o usa un [índice](indice.md); eso lo decide el planificador (la parte del motor que elige cómo ejecutar cada consulta), y por
eso una consulta lenta se arregla muchas veces sin tocar su texto. La contracara es que el orden
en que se escriben las cláusulas no es el orden en que se evalúan: `SELECT` va primero en el texto
y se evalúa casi al final, como cuenta [consulta SELECT](consulta-select.md). La mayoría de las
sorpresas de quien empieza salen de ahí.

SQL tiene tres partes que se usan distinto. Una aclaración de palabras: en sentido amplio, como lo
usa el [glosario](../Fundamentos/glosario-de-bases-de-datos.md), "consulta" es cualquier pedido a
la base, incluidos los que modifican; acá "consultar" es solo leer.

- **Consultar**: `SELECT` y todo lo que va adentro (unir, agrupar, subconsultas, ventanas). Es lo
  que más se escribe y lo que ocupa la mayor parte de la vertical.
- **Modificar**: `INSERT`, `UPDATE`, `DELETE` y el upsert, en [modificar datos](modificar-datos.md).
- **Definir**: `CREATE TABLE`, las restricciones, los cambios de esquema y las vistas, en
  [definir tablas](definir-tablas.md).

## Dónde se equivoca quien empieza

Tres errores explican buena parte de los resultados mal calculados, y los tres devuelven un número
sin dar error:

1. **Un join que multiplica filas.** Unir un pedido con sus ítems repite el pedido una vez por
   ítem; sumar después una columna del pedido (el envío) la cuenta varias veces. Está en
   [join](join.md#un-join-que-multiplica-filas).
2. **Un NULL en una comparación.** `ciudad <> 'Rosario'` no devuelve a los clientes sin ciudad, y
   `NOT IN` con un NULL en la lista no devuelve nada. Es la lógica de tres valores, en
   [NULL y tipos](null-y-tipos.md#la-lógica-de-tres-valores).
3. **Un filtro en el lugar equivocado de un LEFT JOIN.** Poner en `WHERE` una condición sobre la
   tabla de la derecha elimina las filas que el LEFT JOIN venía a conservar. También en
   [join](join.md#on-contra-where-en-un-left-join).

## El estándar y los dialectos

SQL tiene un estándar ISO (ISO/IEC 9075), que se publica por ediciones con nombre de año. modern-sql.com
lista primero SQL:2023, que agregó una parte para consultas sobre grafos; que sea la edición vigente
sale de un buscador y no se confirmó en el catálogo de ISO. Ningún
motor implementa el estándar entero y todos agregan extensiones propias: el núcleo de
`SELECT`, `JOIN`, `GROUP BY` e `INSERT` se escribe igual en todos, y las diferencias aparecen en
límites de filas, upsert, tipos de fecha y booleanos. La lista concreta está en la
[ficha de dialectos](dialectos-de-sql.md).

## Qué hay adentro de SQL, en orden de lectura

Cada componente supone los anteriores. Los ejercicios para practicar cada paso están en la
[ruta de SQL](../Fundamentos/ruta-de-sql.md).

1. [Consulta SELECT](consulta-select.md) — las cláusulas de una consulta y el orden lógico en que se
   evalúan; por qué un alias no se ve en `WHERE`.
2. [Join](join.md) — unir tablas: inner, left, cross, autojoin, anti-join; el join que multiplica
   filas.
3. [Agregación](agregacion.md) — `GROUP BY`, `HAVING`, `count`, `sum` y `FILTER`; el total vendido
   por cliente.
4. [NULL y tipos](null-y-tipos.md) — la lógica de tres valores, `COALESCE`, dinero con `numeric`,
   fechas con zona horaria. Conviene leerla apenas aparece el primer NULL raro.
5. [Subconsultas y CTE](subconsultas-y-cte.md) — consultas dentro de consultas, `EXISTS`, `WITH` y
   la recursiva; el último pedido de cada cliente de cuatro formas.
6. [Funciones de ventana](funciones-de-ventana.md) — calcular sobre un grupo de filas sin colapsarlas:
   rankings, acumulados, la fila anterior.
7. [Modificar datos](modificar-datos.md) — `INSERT`, `UPDATE`, `DELETE`, `RETURNING` y el upsert
   como patrón.
8. [Definir tablas](definir-tablas.md) — `CREATE TABLE`, restricciones, migraciones y vistas.
9. [Índice](indice.md) — qué es, cuándo lo usa el motor y cómo leer un plan con `EXPLAIN`.
10. [SQL desde una aplicación](sql-desde-una-aplicacion.md) — parámetros, inyección SQL, ORM y el
    problema N+1.

- [Dialectos de SQL](dialectos-de-sql.md) — ficha con las diferencias entre PostgreSQL, MySQL,
  SQLite y SQL Server, copiada el 2026-11-27.
