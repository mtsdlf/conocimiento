---
resumen: >-
  NULL es la marca de un dato que falta, y cualquier comparación con él da "desconocido" en vez de
  verdadero o falso; los tipos de columna deciden qué se puede guardar y cómo se calcula, y elegir
  mal el del dinero o el de las fechas da errores que no avisan.
estado: borrador
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 9.2 Comparison Functions and Operators: https://www.postgresql.org/docs/current/functions-comparison.html"
  - "PostgreSQL Documentation, 9.18 Conditional Expressions: https://www.postgresql.org/docs/current/functions-conditional.html"
  - "PostgreSQL Documentation, 8.1 Numeric Types: https://www.postgresql.org/docs/current/datatype-numeric.html"
  - "PostgreSQL Documentation, 8.5 Date/Time Types: https://www.postgresql.org/docs/current/datatype-datetime.html"
  - "SQLite, Datatypes In SQLite: https://www.sqlite.org/datatype3.html"
  - "Bill Karwin, SQL Antipatterns, Volume 1 (Pragmatic Bookshelf, 2022), cap. Fear of the Unknown: https://pragprog.com/titles/bksap1/sql-antipatterns-volume-1/ (solo la tabla de capítulos)"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [NULL, valor nulo, lógica de tres valores, three-valued logic, tipos de datos, data types]
creado: 2026-11-27
revisado:
---

# NULL y tipos

NULL es la marca de un dato que falta, y cualquier comparación con él da "desconocido" en vez de
verdadero o falso; los tipos de columna deciden qué se puede guardar y cómo se calcula, y elegir
mal el del dinero o el de las fechas da errores que no avisan.

Las dos cosas se tocan en todas las consultas. NULL aparece en el [LEFT JOIN](join.md), en los
agregados de [agregación](agregacion.md) y en `NOT IN` de [subconsultas y CTE](subconsultas-y-cte.md);
los tipos se declaran al [definir las tablas](definir-tablas.md).

## La lógica de tres valores

En SQL una condición puede dar verdadero, falso o desconocido. La documentación de PostgreSQL:
"Ordinary comparison operators yield null (signifying 'unknown'), not true or false, when either
input is null. For example, 7 = NULL yields null, as does 7 <> NULL."

`WHERE`, `ON` y `HAVING` se quedan solo con las filas que dan verdadero. Desconocido se descarta
igual que falso, y de ahí sale la sorpresa más común. La cliente Carla no tiene ciudad cargada:

```sql
SELECT nombre FROM clientes WHERE ciudad <> 'Rosario';
-- devuelve a Bruno; Carla no aparece
```

Para la base, la ciudad de Carla es desconocida, y no puede afirmar que no sea Rosario. Si se la
quiere incluir, hay que pedirlo: `WHERE ciudad <> 'Rosario' OR ciudad IS NULL`, o
`WHERE ciudad IS DISTINCT FROM 'Rosario'`.

`AND`, `OR` y `NOT` siguen reglas que se deducen de "desconocido puede ser cualquiera de los dos".
Comprobado en PostgreSQL:

| Expresión | Resultado | Por qué |
|---|---|---|
| `NULL AND false` | falso | con un falso alcanza |
| `NULL AND true` | desconocido | depende del NULL |
| `NULL OR true` | verdadero | con un verdadero alcanza |
| `NOT NULL` | desconocido | negar lo desconocido sigue siendo desconocido |
| `NULL = NULL` | desconocido | dos faltantes no son iguales entre sí |

## Cómo se pregunta por un NULL

Como `= NULL` nunca da verdadero, la documentación lo dice explícito: "Do not write expression =
NULL because NULL is not 'equal to' NULL". Se usa `IS NULL` o `IS NOT NULL`.

`IS DISTINCT FROM` compara tratando a NULL como un valor más: `NULL IS DISTINCT FROM NULL` da
falso y `1 IS DISTINCT FROM NULL` da verdadero. Sirve para detectar cambios entre dos columnas que
pueden estar vacías, donde `<>` fallaría en silencio.

## Los lugares donde NULL cambia el resultado

- **`NOT IN` con un NULL en la lista no devuelve ninguna fila.** Es el caso más grave, porque la
  consulta parece correcta. Está en [subconsultas y CTE](subconsultas-y-cte.md#not-in-con-un-null-no-devuelve-nada).
- **Un filtro en `WHERE` sobre la tabla de la derecha de un LEFT JOIN** descarta las filas que el
  join completó con NULL. Está en [join](join.md#on-contra-where-en-un-left-join).
- **Los agregados ignoran los NULL**: `count(columna)` no los cuenta y `avg` los saca del promedio.
  `sum` sobre ninguna fila, o sobre filas que solo tienen NULL, da NULL y no 0.
- **Un `CHECK` deja pasar NULL**: según la documentación, se cumple si la expresión da "true or the
  null value". Para prohibir el vacío hace falta `NOT NULL`, como explica [definir tablas](definir-tablas.md).
- **`UNIQUE` admite varios NULL**, porque dos NULL no se consideran iguales.

## Reemplazar un NULL: COALESCE y NULLIF

`COALESCE` "returns the first of its arguments that is not null": `coalesce(ciudad, '(sin ciudad)')`
muestra un texto donde falta el dato, y `coalesce(sum(...), 0)` convierte en cero el total de quien
no compró. `NULLIF(a, b)` hace lo inverso: devuelve NULL si los dos valores son iguales. Su uso
clásico es evitar la división por cero: `total / nullif(cantidad, 0)` da NULL en vez de un error.

Karwin dedica un capítulo de *SQL Antipatterns* a este tema, "Fear of the Unknown", con el
antipatrón "Treat NULL as an ordinary value, or the reverse" y la solución "Use NULL as a unique
value". Lo práctico que sale de ahí (inferencia propia, porque del libro solo se leyó la tabla de
capítulos): no usar valores de relleno como `0` o `''` para decir "no sé", y no usar NULL para algo
que sí se sabe.

## El dinero va en numeric

Para precios y montos, PostgreSQL recomienda `numeric`: "especially recommended for storing
monetary amounts and other quantities where exactness is required". Los tipos `real` y `double
precision` son "inexact", y la documentación advierte que "Comparing two floating-point values for
equality might not always work as expected":

```sql
SELECT 0.1::float8 + 0.2::float8 = 0.3::float8 AS flotante,   -- falso
       0.1::numeric + 0.2 = 0.3 AS numerico;                  -- verdadero
```

El costo es velocidad: `numeric` es más lento que los enteros y los flotantes, algo que, por
inferencia propia (no se midió), no se nota en el volumen de un comercio. Las columnas de precio del comercio son `numeric(12,2)`: hasta 12
dígitos, dos de ellos decimales.

Otra trampa de tipos: la división entre enteros descarta los decimales. `7 / 2` da 3; `7 / 2.0` o
`7::numeric / 2` dan 3.5. Pasa al calcular un promedio a mano con dos `count`.

## Las fechas con hora llevan zona horaria

PostgreSQL tiene `timestamp` (sin zona) y `timestamptz` (con zona). Un `timestamptz` se guarda en
UTC y se muestra en la zona de la sesión; según la documentación, "The originally stated or assumed
time zone is not retained and cannot be retrieved later". Un `timestamp` sin zona, en cambio,
"will silently ignore any time zone indication":

```sql
SELECT TIMESTAMP   '2026-11-27 10:00:00+02' AS sin_zona,   -- 2026-11-27 10:00:00 (el +02 se perdió)
       TIMESTAMPTZ '2026-11-27 10:00:00+02' AS con_zona;   -- 2026-11-27 05:00:00-03 en Buenos Aires
```

Para el momento en que pasó algo (un pedido, un pago) conviene `timestamptz`: dos servidores en
zonas distintas ven el mismo instante. Para una fecha sin hora (un cumpleaños, un vencimiento) está
`date`. Comparar un `timestamptz` con una fecha suelta (`fecha >= '2026-11-01'`) toma la medianoche
de la zona de la sesión, así que la zona de la sesión cambia qué pedidos caen en el mes.

## Convertir entre tipos

`CAST(valor AS tipo)` es la forma estándar; `valor::tipo` es la abreviatura de PostgreSQL.
`'42'::integer + 1` da 43; `'abc'::integer` da un error ("invalid input syntax for type integer").
Convertir una columna dentro de un `WHERE` (`fecha::date = '2026-11-15'`) impide usar el índice de
esa columna, como muestra [índice](indice.md).

## SQLite guarda lo que le den

SQLite usa tipado dinámico: "the datatype of a value is associated with the value itself, not with
its container". El tipo declarado de la columna es una afinidad, "recommended, not required": en una
columna `INTEGER` de SQLite entra el texto `'hola'` sin error (se comprobó al ejecutarlo). SQLite no
tiene tipo de fecha (las guarda como texto ISO 8601, número real o entero) ni booleano (guarda 0 y
1). El detalle por motor está en la [ficha de dialectos](dialectos-de-sql.md).
