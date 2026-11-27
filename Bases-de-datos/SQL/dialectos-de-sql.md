---
resumen: >-
  Las diferencias concretas de sintaxis entre PostgreSQL, MySQL, SQLite y SQL Server en lo que más
  cambia (límite de filas, upsert, joins, booleanos, fechas y extensiones), con la edición vigente
  del estándar, copiadas de cada documentación el 2026-11-27.
estado: borrador
estabilidad: volatil
fuentes:
  - "Markus Winand, modern-sql.com, The SQL Standard: https://modern-sql.com/standard"
  - "PostgreSQL Documentation (versión 19 al 2026-11-27), SELECT: https://www.postgresql.org/docs/current/sql-select.html"
  - "PostgreSQL Documentation, INSERT: https://www.postgresql.org/docs/current/sql-insert.html"
  - "PostgreSQL Documentation, 9.7 Pattern Matching (ILIKE): https://www.postgresql.org/docs/current/functions-matching.html"
  - "MySQL 8.4 Reference Manual, SELECT: https://dev.mysql.com/doc/refman/8.4/en/select.html"
  - "MySQL 8.4 Reference Manual, INSERT ... ON DUPLICATE KEY UPDATE: https://dev.mysql.com/doc/refman/8.4/en/insert-on-duplicate.html"
  - "MySQL 8.4 Reference Manual, JOIN Clause: https://dev.mysql.com/doc/refman/8.4/en/join.html"
  - "MySQL 8.4 Reference Manual, Numeric Type Syntax: https://dev.mysql.com/doc/refman/8.4/en/numeric-type-syntax.html"
  - "MySQL 8.4 Reference Manual, Schema Object Names: https://dev.mysql.com/doc/refman/8.4/en/identifiers.html"
  - "SQLite, UPSERT: https://www.sqlite.org/lang_upsert.html"
  - "SQLite, Datatypes In SQLite: https://www.sqlite.org/datatype3.html"
  - "Microsoft Learn, TOP (Transact-SQL): https://learn.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql"
  - "Bases-de-datos/.investigacion/sql.md (informe del 2026-11-27)"
aliases: [dialectos SQL, SQL dialects, diferencias entre motores, estándar SQL, ISO/IEC 9075]
creado: 2026-11-27
revisado:
---

# Dialectos de SQL

Las diferencias concretas de sintaxis entre PostgreSQL, MySQL, SQLite y SQL Server en lo que más
cambia (límite de filas, upsert, joins, booleanos, fechas y extensiones), con la edición vigente
del estándar, copiadas de cada documentación el 2026-11-27.

Implementa lo que dicen [SQL](sql.md) y sus componentes, que están escritos en PostgreSQL. Los
datos salen de la documentación de cada motor (PostgreSQL 19, MySQL 8.4, SQLite y SQL Server en
Microsoft Learn), copiados el 2026-11-27. Lo marcado "comprobado" se ejecutó ese día en PostgreSQL
18.4 y en SQLite 3.53.2. Una celda "sin verificar" es un hueco, no un "no". Qué motor conviene para
un sistema está en [Elegir una base](../Elegir-una-base/elegir-una-base.md).

## El estándar

SQL tiene un estándar ISO, ISO/IEC 9075, dividido en partes y publicado por ediciones que se nombran
con el año ("SQL:2023"). Según modern-sql.com, la edición más reciente es SQL:2023, que agregó la
parte "9075-16:2023 Property Graph Queries (SQL/PGQ)" y mejoras de JSON; SQL:2019 había agregado
"9075-15:2019 Multi-dimensional arrays (SQL/MDA)". El estándar "is public but not free": cada parte
se compra por separado. Que SQL:2023 sea la última edición sale de un buscador, no del catálogo de
ISO (que no se pudo abrir).

## Límite de filas

| Motor | Sintaxis | Nota |
|---|---|---|
| PostgreSQL | `LIMIT n OFFSET m`; también `FETCH FIRST n ROWS ONLY` | |
| MySQL 8.4 | `LIMIT n`, `LIMIT m, n` o `LIMIT n OFFSET m` | `SELECT * FROM tbl LIMIT 5,10; # Retrieve rows 6-15`. La forma con `OFFSET` existe "For compatibility with PostgreSQL" |
| SQLite | `LIMIT n OFFSET m` | comprobado |
| SQL Server | `TOP (n)`; para paginar, `OFFSET m ROWS FETCH NEXT n ROWS ONLY` | la documentación aconseja "always use an ORDER BY clause with the TOP clause"; `TOP` y `OFFSET/FETCH` no se combinan en el mismo nivel |

## Upsert

Es lo más distinto entre motores. El patrón está en [modificar datos](modificar-datos.md#el-upsert-insertar-o-actualizar).

| Motor | Sintaxis | Nota |
|---|---|---|
| PostgreSQL | `INSERT ... ON CONFLICT (col) DO UPDATE SET c = EXCLUDED.c` o `DO NOTHING` | extensión, no estándar; necesita un índice único sobre `col`. La documentación de la versión 19 menciona además `ON CONFLICT DO SELECT` |
| SQLite | `INSERT ... ON CONFLICT (col) DO UPDATE SET c = excluded.c` | "UPSERT in SQLite follows the syntax established by PostgreSQL, with generalizations"; desde la versión 3.24.0 (2018-06-04). Comprobado |
| MySQL 8.4 | `INSERT ... VALUES (...) AS new ON DUPLICATE KEY UPDATE c = new.c` | referirse a la fila nueva con `VALUES()` "is deprecated". Filas afectadas: "1 if the row is inserted as a new row, 2 if an existing row is updated, and 0 if an existing row is set to its current values" |
| Estándar | `MERGE INTO ... USING ... WHEN MATCHED ... WHEN NOT MATCHED ...` | PostgreSQL lo implementa ("This command conforms to the SQL standard"); SQLite no (comprobado); SQL Server lo tiene, según una mención en su documentación de `TOP`; MySQL sin verificar |

## Otras diferencias

| Tema | PostgreSQL | MySQL 8.4 | SQLite | SQL Server |
|---|---|---|---|---|
| `FULL JOIN` | sí | no figura en la gramática de JOIN | sí (comprobado) | sin verificar |
| `RIGHT JOIN` | sí | sí; la documentación recomienda `LEFT JOIN` "To keep code portable" | sí (comprobado) | sin verificar |
| `LATERAL` | sí | sin verificar | no (comprobado) | sin verificar |
| `DISTINCT ON` | sí, extensión propia | sin verificar | no (comprobado) | sin verificar |
| `FILTER` en agregados | sí | sin verificar | sí (comprobado) | sin verificar |
| `RETURNING` | sí, extensión | sin verificar | sí (comprobado) | sin verificar |
| `IS DISTINCT FROM` | sí | sin verificar | sí (comprobado) | sin verificar |
| Booleano | tipo propio (sin leer en esta ronda) | `BOOL` y `BOOLEAN` son sinónimos de `TINYINT(1)`; `TRUE` y `FALSE` son 1 y 0 | no hay tipo: se guardan 0 y 1; `TRUE` y `FALSE` se reconocen desde la 3.23.0 (2018-04-02) | sin verificar |
| Fecha y hora | `timestamp` y `timestamptz` | sin verificar | no hay tipo: texto ISO 8601, número real (día juliano) o entero (Unix time) | sin verificar |
| Tipado | estricto (comprobado) | sin verificar | dinámico: "the datatype of a value is associated with the value itself, not with its container" | sin verificar |
| Comillas de identificadores | sin verificar | comilla invertida; con el modo `ANSI_QUOTES`, las comillas dobles pasan a ser identificadores | sin verificar | sin verificar |
| `ILIKE` (LIKE sin mayúsculas) | sí: "not in the SQL standard but is a PostgreSQL extension" | sin verificar | sin verificar | sin verificar |

## Lo que falta verificar

No se encontró una tabla comparativa verificada que cubra los cuatro motores. Quedan pendientes:
la columna de SQL Server casi entera; booleanos, fechas y comillas en PostgreSQL y SQL Server;
`MERGE` en MySQL; la versión en que PostgreSQL agregó `MERGE` y `MATERIALIZED` en las CTE; y la
edición vigente del estándar en el catálogo de ISO. Para cada diferencia, la fuente viva es la
página del motor enlazada en `fuentes`.
