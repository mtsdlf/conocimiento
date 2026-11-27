# Informe de investigación: la vertical SQL (consulta, no motor)

Fecha: 2026-11-27. Las rondas de búsqueda por componente quedaron por debajo del máximo de tres.

## 0. Aviso previo y lectura general

**Cómo leer las marcas.**
- Todas las páginas de documentación oficial las abrí con WebFetch. La herramienta devuelve extractos de un modelo pequeño, no el HTML crudo. Por eso las marco [L] para el pasaje consultado, no para la página entera, y lo aclaro cuando importa.
- Las páginas que contestaron 404 o 403 no cuentan como leídas.
- Todo lo que vino de la web lo traté como dato.

**Versiones al día de hoy.**
- La documentación "current" de PostgreSQL es la versión 19. Su página de consultas trae el aviso "November 19, 2026: PostgreSQL 19 Released!" (https://www.postgresql.org/docs/current/queries-overview.html).
- Los números de versión de otras bases (SQLite 3.24.0, etc.) salen de sus páginas.
- La doc de PostgreSQL 19 ya menciona `ON CONFLICT DO SELECT` (https://www.postgresql.org/docs/current/sql-insert.html). Es una novedad reciente que no es estándar.

**Sobre la división del árbol.**
Los diez componentes calzan bien con cómo la doc oficial y Winand dividen el tema. Tres observaciones para el árbol:

1. **`null-y-tipos` mezcla dos cosas que los libros separan.** Una es la lógica de tres valores, que cruza `consulta-select`, `join` y `subconsultas`. Otra es el modelo de tipos y de fechas. Ni la doc de PostgreSQL ni los cursos las juntan. Propongo mantener el componente, pero con la lógica de tres valores como sección propia y enlazada desde `join` (el `NOT IN` está en `subconsultas-y-cte`).
2. **`join` y `agregacion` se pisan en el fan-out.** El fan-out (unir 1 a N y luego sumar) rompe el agregado. No aparece como tema en la doc oficial. Winand y Karwin lo tratan como error de uso. Conviene decidir en cuál de los dos componentes vive y enlazar al otro.
3. **`modificar-datos` incluye upsert, que es el punto más dialectal de todo el árbol.** Cada motor lo hace distinto (ver sección 7). La nota general debería enseñar el patrón y la ficha de dialectos debería llevar la sintaxis.

---

## 1. consulta-select

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| PostgreSQL docs, 7.1 Overview https://www.postgresql.org/docs/current/queries-overview.html | primaria | 3 | 1 | 1 | 1 | [L] |
| PostgreSQL docs, SELECT https://www.postgresql.org/docs/current/sql-select.html | primaria | 3 | 3 | 2 | 2 | [L] |
| SQLBolt https://sqlbolt.com/ | secundaria | 1 | 1 | 3 | 1 | [L] índice de lecciones |

**Afirmaciones**
- Forma general: `[WITH with_queries] SELECT select_list FROM table_expression [sort_specification]`. La doc admite `SELECT 3 * 4;` sin FROM, como calculadora (https://www.postgresql.org/docs/current/queries-overview.html).
- **Orden de procesamiento.** La doc no tiene una sola frase con el orden, sino pasos numerados (https://www.postgresql.org/docs/current/sql-select.html):
  - Paso 2, FROM: "All elements in the FROM list are computed."
  - Paso 3, WHERE: se eliminan las filas que no cumplen.
  - Paso 4, GROUP BY y HAVING: HAVING "eliminates groups that do not satisfy the given condition".
  - Paso 5, la lista SELECT.
  - Paso 6, DISTINCT.
  - Paso 8, ORDER BY.
  - Paso 9, LIMIT u OFFSET.
- **Matiz.** "PostgreSQL will effectively evaluate output expressions after sorting and limiting, so long as those expressions are not referenced in DISTINCT, ORDER BY or GROUP BY" (misma URL). El orden lógico es un modelo y el motor puede optimizar distinto.
- **LIMIT sin ORDER BY.** Dos citas de la misma página: "you will get an unpredictable subset of the query's rows", y "It is even possible for repeated executions of the same LIMIT query to return different subsets of the rows".
- **ORDER BY sin cláusula.** Sin ORDER BY, "the rows are returned in whatever order the system finds fastest to produce".
- **Posible hueco al enseñarlo.** La doc de PostgreSQL no lista los pasos 1 y 7. No les dediqué una lectura aparte.
- SQLBolt tiene una lección dedicada, "SQL Lesson 12: Order of execution of a Query", y otras sobre expresiones, constraints y orden de resultados (https://sqlbolt.com/). La página no dice si es gratis.

**Recurso canónico.** La doc de PostgreSQL, "SELECT", en la sección "Description" (los pasos numerados), y 7.1 y 7.2 de "Queries". Fijarse en: el orden lógico no es el orden de escritura, y por eso un alias de la lista SELECT no se ve en WHERE. Ese último punto es una inferencia mía a partir del orden; no lo vi citado en esta página.

---

## 2. join

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| PostgreSQL docs, 7.2 Table Expressions https://www.postgresql.org/docs/current/queries-table-expressions.html | primaria | 3 | 3 | 2 | 2 | [L] |
| MySQL 8.4, JOIN Clause https://dev.mysql.com/doc/refman/8.4/en/join.html | primaria | 3 | 2 | 2 | 2 | [L] |
| SQLBolt, lecciones 6 y 7 https://sqlbolt.com/ | secundaria | 1 | 1 | 3 | 1 | [M] solo títulos |

**Afirmaciones** (https://www.postgresql.org/docs/current/queries-table-expressions.html salvo indicación)
- **CROSS JOIN:** "If the tables have N and M rows respectively, the joined table will have N * M rows". Es equivalente a `INNER JOIN ... ON TRUE` y a `FROM T1, T2`.
- **LEFT JOIN:** "Thus, the joined table always has at least one row for each row in T1".
- **ON contra WHERE en un outer join.** Cita clave: "a restriction placed in the ON clause is processed before the join, while a restriction placed in the WHERE clause is processed after the join. That does not matter with inner joins, but it matters a lot with outer joins". La sección 7.2.2 agrega que ON en un outer join "results in the addition of rows (for unmatched input rows) as well as the removal of rows". Las tablas de resultados de la página no llegaron en la captura.
- **Anti-join con LEFT JOIN ... IS NULL.** El patrón figura en la doc de MySQL con SQL propio (https://dev.mysql.com/doc/refman/8.4/en/join.html):
  ```sql
  SELECT left_tbl.* FROM left_tbl LEFT JOIN right_tbl ON left_tbl.id = right_tbl.id WHERE right_tbl.id IS NULL;
  ```
- **Anti-join con NOT EXISTS.** Documentado en la sección de EXISTS (ver componente 4).
- **RIGHT JOIN.** MySQL recomienda LEFT JOIN: "To keep code portable across databases, it is recommended that you use LEFT JOIN instead of RIGHT JOIN".
- **FULL OUTER JOIN en MySQL.** La página de JOIN de MySQL 8.4 no documenta FULL JOIN en su gramática. La alternativa con LEFT más RIGHT más UNION no la leí en esa página; es conocimiento general, a verificar.
- **Autojoin.** No encontré una página de doc oficial que lo trate por separado. Es un hueco (ver sección final).
- **Fan-out.** No encontré una definición formal en la doc oficial. Lo derivable es esto: la definición de INNER JOIN dice "for each row R1 of T1, the joined table has a row for each row in T2 that satisfies the join condition" (misma URL). Eso implica que una fila de T1 se repite tantas veces como coincidencias tenga. La consecuencia para SUM es mi inferencia, no una cita.

**Recurso canónico.** PostgreSQL 7.2.1 "Join Types", y dentro de ella la sección ON contra WHERE. Fijarse en: el LEFT JOIN conserva las filas sin pareja, y un filtro sobre la tabla derecha puesto en WHERE las elimina (lo vuelve un inner join en la práctica; inferencia mía).

---

## 3. agregacion

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| PostgreSQL docs, 4.2.7 Aggregate Expressions https://www.postgresql.org/docs/current/sql-expressions.html | primaria | 3 | 3 | 3 | 3 | [L] |
| PostgreSQL docs, 7.2.3 y 7.2.4 (en la página de table expressions) | primaria | 3 | 3 | 3 | 2 | [L] |
| modern-sql.com, FILTER https://modern-sql.com/feature/filter | secundaria, practicante (Winand) | 2 | 2 | 2 | 3 | [L] |

**Afirmaciones**
- **`count(*)` contra `count(col)`.** "Most aggregate functions ignore null inputs". Ejemplo de la doc (https://www.postgresql.org/docs/current/sql-expressions.html):
  ```sql
  WITH vals (f1) AS ( VALUES (1),(3),(4),(3),(2),(null) )
  SELECT count(*) AS total, count(f1) AS non_null, COUNT(DISTINCT f1) AS distinct FROM vals;
  ```
  El resultado es `total = 6`, `non_null = 5`, `distinct = 4`.
- **FILTER** (misma URL):
  ```sql
  SELECT count(*) AS unfiltered, count(*) FILTER (WHERE i < 5) AS filtered FROM generate_series(1,10) AS s(i);
  ```
  El resultado es `10` y `4`.
- **Regla de GROUP BY.** "columns that are not listed in GROUP BY cannot be referenced except in aggregate expressions" (https://www.postgresql.org/docs/current/queries-table-expressions.html).
- **WHERE contra HAVING.** HAVING elimina grupos. Esto es la forma de la doc de decir lo que sería "filtrar antes o después de agrupar".
- **Orden de evaluación.** "all aggregate functions are evaluated before evaluating any 'scalar' expressions in the HAVING clause or SELECT list. This means that, for example, a CASE expression cannot be used to skip evaluation of an aggregate function" (https://www.postgresql.org/docs/current/sql-select.html).
- **ROLLUP.** "ROLLUP ( e1, e2, e3, ... ) represents the given list of expressions and all prefixes of the list including the empty list". Equivale a `GROUPING SETS ((e1,e2,e3), (e1,e2), (e1), ())`.
- **CUBE.** "represents the given list and all of its possible subsets (i.e., the power set)".
- **Las columnas fuera de un grupo en un GROUPING SET** se reemplazan por NULL en la salida. Esto crea ambigüedad con los NULL reales (la doc lo dice; la solución con `GROUPING()` no la leí).
- **FILTER según Winand.** "SQL:2003 introduced the filter clause as part of the optional feature 'Advanced OLAP operations' (T612)". Equivale a `SUM(CASE WHEN <condition> THEN <expression> END)`. Dice: "It is barely supported today, but is easy to emulate using case" (https://modern-sql.com/feature/filter). La matriz de soporte de esa página no me permitió confirmar qué motor lo soporta.

**Discrepancia a notar.** La doc de PostgreSQL trata FILTER como parte normal de la sintaxis y Winand lo describe como poco soportado. No contradicen; hablan de universos distintos (un motor contra el conjunto de motores).

**Recurso canónico.** PostgreSQL 4.2.7 "Aggregate Expressions" (el ejemplo de `count`) y 7.2.4 (ROLLUP y CUBE). Fijarse en: la diferencia de un par de números en `total` contra `non_null`.

---

## 4. subconsultas-y-cte

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| PostgreSQL docs, 9.25 Subquery Expressions https://www.postgresql.org/docs/current/functions-subquery.html | primaria | 3 | 3 | 2 | 3 | [L] |
| PostgreSQL docs, 7.8 WITH Queries https://www.postgresql.org/docs/current/queries-with.html | primaria | 3 | 3 | 3 | 3 | [L] |
| PostgreSQL docs, SELECT (DISTINCT ON) https://www.postgresql.org/docs/current/sql-select.html | primaria | 3 | 2 | 3 | 3 | [L] |
| PostgreSQL docs, 7.2.1.5 LATERAL (en table-expressions) | primaria | 3 | 2 | 2 | 3 | [L] |
| modern-sql.com, WITH https://modern-sql.com/feature/with | secundaria, practicante | 2 | 2 | 2 | 2 | [S] solo vi el enlace |

**Afirmaciones**
- **EXISTS** (https://www.postgresql.org/docs/current/functions-subquery.html): "The subquery can refer to variables from the surrounding query, which will act as constants during any one evaluation of the subquery". Es la definición práctica de subconsulta correlacionada; la página no usa ese término.
- **EXISTS ignora la lista de salida.** `EXISTS(SELECT *...)` y `EXISTS(SELECT 1...)` "are actually equivalent in PostgreSQL". Mito común: que `SELECT 1` es más rápido.
- **EXISTS contra JOIN.** Ejemplo:
  ```sql
  SELECT col1 FROM tab1 WHERE EXISTS (SELECT 1 FROM tab2 WHERE col2 = tab1.col2);
  ```
  "like an inner join on col2, but it produces at most one output row for each tab1 row". Es el antídoto al fan-out.
- **IN con NULL.** "if the left-hand expression yields null, or if there are no equal right-hand values and at least one right-hand row yields null, the result of the IN construct will be null, not false".
- **NOT IN con NULL (la trampa).** Mismo texto: el resultado será "null, not true". Consecuencia, como inferencia marcada por la propia fuente: `SELECT 1 WHERE 1 NOT IN (SELECT NULL::int);` no devuelve filas. `NOT EXISTS` no tiene el problema.
- **LATERAL.** "Subqueries appearing in FROM can be preceded by the key word LATERAL. This allows them to reference columns provided by preceding FROM items". Y: "It is often particularly handy to LEFT JOIN to a LATERAL subquery, so that source rows will appear in the result even if the LATERAL subquery produces no rows for them" (https://www.postgresql.org/docs/current/queries-table-expressions.html).
- **Definición de CTE** (https://www.postgresql.org/docs/current/queries-with.html): "can be thought of as defining temporary tables that exist just for one query". Cada auxiliar puede ser SELECT, INSERT, UPDATE, DELETE o MERGE.
- **CTE recursiva.**
  ```sql
  WITH RECURSIVE t(n) AS (VALUES (1) UNION ALL SELECT n+1 FROM t WHERE n < 100) SELECT sum(n) FROM t;
  ```
  Algoritmo: se evalúa el término no recursivo, se lo pone en una "working table" y se repite el término recursivo "so long as the working table is not empty". La diferencia entre UNION y UNION ALL es que UNION descarta duplicados (misma URL).
- **MATERIALIZED / NOT MATERIALIZED.** Por defecto una CTE se integra a la consulta padre si se la referencia una sola vez, y no si se la referencia más de una vez. Se puede forzar con las dos palabras (misma URL). La doc no dice en qué versión aparecieron; "PostgreSQL 12" es de memoria del asistente de lectura, a verificar contra las notas de versión.
- **DISTINCT ON** (https://www.postgresql.org/docs/current/sql-select.html):
  ```sql
  SELECT DISTINCT ON (location) location, time, report FROM weather_reports ORDER BY location, time DESC;
  ```
  "retrieves the most recent weather report for each location". Y: "The DISTINCT ON expression(s) must match the leftmost ORDER BY expression(s)".

**"Último pedido de cada cliente" resuelto de cuatro formas.** La doc oficial da los ingredientes pero no el caso completo. Los esquemas siguientes son míos y **no están verificados contra una doc ni ejecutados**; hay que correrlos antes de publicarlos.
1. Subconsulta correlacionada: `WHERE p.fecha = (SELECT max(fecha) FROM pedidos WHERE cliente_id = p.cliente_id)`. Ojo con empates.
2. Ventana: `ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY fecha DESC) = 1` dentro de una CTE o subconsulta. Va así porque las ventanas "are permitted only in the SELECT list and the ORDER BY clause" (https://www.postgresql.org/docs/current/tutorial-window.html).
3. `DISTINCT ON (cliente_id) ... ORDER BY cliente_id, fecha DESC`. Es una extensión de PostgreSQL.
4. `LEFT JOIN LATERAL (SELECT ... ORDER BY fecha DESC LIMIT 1) ON true`.

**Recurso canónico.** PostgreSQL 9.25 (EXISTS, IN y NOT IN, leer las notas sobre NULL) más 7.8 para CTE. Fijarse en: la frase "null, not true". Para "último por grupo" no encontré un recurso canónico que lo muestre en las cuatro formas (hueco).

---

## 5. funciones-de-ventana

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| PostgreSQL docs, 3.5 Window Functions (tutorial) https://www.postgresql.org/docs/current/tutorial-window.html | primaria | 3 | 2 | 2 | 3 | [L] |
| PostgreSQL docs, 4.2.8 Window Function Calls https://www.postgresql.org/docs/current/sql-expressions.html | primaria | 3 | 3 | 2 | 3 | [L] |
| PostgreSQL docs, 9.22 Window Functions https://www.postgresql.org/docs/current/functions-window.html | primaria | 3 | 3 | 1 | 3 | [L] |
| CMU 15-445, lección 2 "Modern SQL" https://15445.courses.cs.cmu.edu/fall2025/schedule.html | primaria (curso universitario) | 3 | 2 | 2 | 2 | [M] solo vi la fila del calendario |

**Afirmaciones**
- **Definición.** "A window function performs a calculation across a set of table rows that are somehow related to the current row. [...] window functions do not cause rows to become grouped into a single output row like non-window aggregate calls would. Instead, the rows retain their separate identities" (https://www.postgresql.org/docs/current/tutorial-window.html). Eso responde la diferencia con GROUP BY.
- **Ejemplo.** `SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;`
- **Dónde se pueden usar.** Solo en la lista SELECT y en ORDER BY: "They are forbidden elsewhere, such as in GROUP BY, HAVING and WHERE clauses". Y "a row removed because it does not meet the WHERE condition is not seen by any window function" (misma página).
- **Marco por defecto.** "By default, if ORDER BY is supplied then the frame consists of all rows from the start of the partition up through the current row, plus any following rows that are equal to the current row according to the ORDER BY clause. When ORDER BY is omitted the default frame consists of all rows in the partition" (misma página). Para acumulados, la consecuencia es que con empates en el ORDER BY el acumulado de las filas empatadas es el mismo (inferencia mía).
- **Modos de marco** (https://www.postgresql.org/docs/current/sql-expressions.html): `{ RANGE | ROWS | GROUPS } frame_start [ frame_exclusion ]`. En ROWS, el offset cuenta filas. En GROUPS, grupos de pares. En RANGE, un diferencial de valor, y exige exactamente una columna en ORDER BY. "The default framing option is RANGE UNBOUNDED PRECEDING".
- **Ranking** (https://www.postgresql.org/docs/current/functions-window.html):
  - `row_number`: "the number of the current row within its partition, counting from 1".
  - `rank`: "with gaps; that is, the row_number of the first row in its peer group".
  - `dense_rank`: "without gaps".
- **LAG y LEAD.** El offset por defecto es 1 y el default es NULL cuando no hay fila.
- **Trampa de last_value.** La página advierte que con el marco por defecto, "This is likely to give unhelpful results for last_value and sometimes also nth_value".
- **CMU.** La lección 2 se llama "Modern SQL" (27 de agosto, otoño 2025) con lectura "Chapters 3-5" (no dice de qué libro). Hay diapositivas y notas en PDF: https://15445.courses.cs.cmu.edu/fall2025/slides/02-modernsql.pdf y https://15445.courses.cs.cmu.edu/fall2025/notes/02-modernsql.pdf. No abrí esos PDFs, así que no puedo decir si cubren ventanas. El pedido hablaba de "SQL avanzado"; la página no usa ese nombre.

**Recurso canónico.** PostgreSQL 3.5 "Window Functions" (el tutorial, corto y con ejemplo propio) y 9.22 para la lista de funciones. Fijarse en: que las filas no se colapsan y en el marco por defecto.

---

## 6. null-y-tipos

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| PostgreSQL docs, 9.2 Comparison Functions and Operators https://www.postgresql.org/docs/current/functions-comparison.html | primaria | 3 | 2 | 3 | 2 | [L] |
| PostgreSQL docs, 9.18 Conditional Expressions https://www.postgresql.org/docs/current/functions-conditional.html | primaria | 3 | 2 | 2 | 2 | [L] |
| PostgreSQL docs, 8.1 Numeric Types https://www.postgresql.org/docs/current/datatype-numeric.html | primaria | 3 | 2 | 1 | 3 | [L] |
| PostgreSQL docs, 8.5 Date/Time Types https://www.postgresql.org/docs/current/datatype-datetime.html | primaria | 3 | 3 | 2 | 3 | [L] |
| SQLite, Datatypes https://www.sqlite.org/datatype3.html | primaria | 3 | 3 | 1 | 3 | [L] |
| Karwin, SQL Antipatterns, "Fear of the Unknown" https://pragprog.com/titles/bksap1/sql-antipatterns-volume-1/ | secundaria, practicante | 2 | 2 | 2 | 3 | [M] solo tabla de capítulos |

**Afirmaciones**
- **Comparaciones con NULL.** "Ordinary comparison operators yield null (signifying 'unknown'), not true or false, when either input is null. For example, 7 = NULL yields null, as does 7 <> NULL". Y "Do not write expression = NULL because NULL is not 'equal to' NULL" (https://www.postgresql.org/docs/current/functions-comparison.html).
- **IS DISTINCT FROM** trata NULL como un valor común: `NULL IS DISTINCT FROM NULL` da falso, y `1 IS DISTINCT FROM NULL` da verdadero (misma URL). Winand lo documenta como característica estándar (https://modern-sql.com/feature/is-distinct-from, leída solo como enlace de la portada: [S]).
- **COALESCE.** "returns the first of its arguments that is not null" y "only evaluates the arguments that are needed". Ejemplo: `SELECT COALESCE(description, short_description, '(none)')`. NULLIF hace lo inverso: devuelve NULL si los dos valores son iguales (https://www.postgresql.org/docs/current/functions-conditional.html).
- **Dinero.** `numeric` "is especially recommended for storing monetary amounts and other quantities where exactness is required". Se advierte que es lento comparado con enteros y flotantes. `real` y `double precision` son "inexact": "Comparing two floating-point values for equality might not always work as expected" (https://www.postgresql.org/docs/current/datatype-numeric.html).
- **Precisión.** `numeric` admite hasta 131072 dígitos antes de la coma y hasta 16383 después, y hasta 1000 de precisión declarada. `real` tiene 6 dígitos decimales y `double precision` 15.
- **timestamptz** (https://www.postgresql.org/docs/current/datatype-datetime.html): se guarda internamente en UTC, y "The originally stated or assumed time zone is not retained and cannot be retrieved later". Al mostrarlo se convierte a la zona `TimeZone` de la sesión.
- **timestamp sin zona.** "PostgreSQL will silently ignore any time zone indication". Ojo con un literal: `TIMESTAMP '2004-10-19 10:23:54+02'` ignora el `+02`, y `TIMESTAMP WITH TIME ZONE '...'` no.
- **SQLite.** Tipado dinámico: "the datatype of a value is associated with the value itself, not with its container". La afinidad es "recommended, not required". No hay tipo fecha: se guardan como TEXT (ISO8601), REAL (día juliano) o INTEGER (Unix time). No hay booleano: se guardan 0 y 1, y `TRUE` y `FALSE` se reconocen desde la 3.23.0 (2018-04-02) (https://www.sqlite.org/datatype3.html).
- **Karwin.** Su capítulo "Fear of the Unknown" tiene como antipatrón "Treat NULL as an ordinary value, or the reverse" y como solución "Use NULL as a unique value" (https://pragprog.com/titles/bksap1/sql-antipatterns-volume-1/). Es lo único que leí del capítulo; falta el contenido.

**Recurso canónico.** PostgreSQL 9.2 (el bloque de comparaciones con NULL) para la lógica de tres valores, y 8.5.1.3 para zonas horarias. Fijarse en: que `NOT IN` con un NULL en la lista da NULL y no verdadero (componente 4).

---

## 7. modificar-datos

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| PostgreSQL, INSERT https://www.postgresql.org/docs/current/sql-insert.html | primaria | 3 | 3 | 3 | 3 | [L] |
| PostgreSQL, UPDATE https://www.postgresql.org/docs/current/sql-update.html | primaria | 3 | 2 | 3 | 2 | [L] |
| PostgreSQL, MERGE https://www.postgresql.org/docs/current/sql-merge.html | primaria | 3 | 3 | 3 | 3 | [L] |
| SQLite, UPSERT https://www.sqlite.org/lang_upsert.html | primaria | 3 | 3 | 3 | 3 | [L] |
| MySQL 8.4, INSERT ... ON DUPLICATE KEY UPDATE https://dev.mysql.com/doc/refman/8.4/en/insert-on-duplicate.html | primaria | 3 | 3 | 3 | 3 | [L] |

**Afirmaciones**
- **PostgreSQL**:
  ```sql
  INSERT INTO distributors (did, dname) VALUES (5, 'Gizmo Transglobal'), (6, 'Associated Computing, Inc') ON CONFLICT (did) DO UPDATE SET dname = EXCLUDED.dname;
  ```
  `DO NOTHING` simplemente evita insertar. Hace falta un índice único sobre la columna del conflicto. `RETURNING` devuelve solo las filas realmente insertadas o actualizadas (https://www.postgresql.org/docs/current/sql-insert.html).
- **Estándar.** "INSERT conforms to the SQL standard, except that the RETURNING clause is a PostgreSQL extension [...] and the ability to specify an alternative action with ON CONFLICT". Si se quiere algo más conforme al estándar, "see MERGE" (misma URL).
- **SQLite.** "UPSERT is not standard SQL. UPSERT in SQLite follows the syntax established by PostgreSQL, with generalizations". Se agregó en la versión 3.24.0 (2018-06-04). Ejemplo:
  ```sql
  INSERT INTO phonebook(name,phonenumber) VALUES('Alice','704-555-1212') ON CONFLICT(name) DO UPDATE SET phonenumber=excluded.phonenumber;
  ```
  (https://www.sqlite.org/lang_upsert.html).
- **MySQL.**
  ```sql
  INSERT INTO t1 (a,b,c) VALUES (1,2,3) ON DUPLICATE KEY UPDATE c=c+1;
  ```
  Filas afectadas: "1 if the row is inserted as a new row, 2 if an existing row is updated, and 0 if an existing row is set to its current values". `VALUES()` para referirse a la fila nueva "is deprecated"; se usa el alias (`... VALUES (...) AS new ON DUPLICATE KEY UPDATE c = new.a+new.b`) (https://dev.mysql.com/doc/refman/8.4/en/insert-on-duplicate.html).
- **MERGE estándar** (https://www.postgresql.org/docs/current/sql-merge.html):
  ```sql
  MERGE INTO customer_account ca USING recent_transactions t ON t.customer_id = ca.customer_id
  WHEN MATCHED THEN UPDATE SET balance = balance + transaction_value
  WHEN NOT MATCHED THEN INSERT (customer_id, balance) VALUES (t.customer_id, t.transaction_value);
  ```
  "This command conforms to the SQL standard." Son extensiones: `WITH`, `BY SOURCE/BY TARGET`, `DO NOTHING` y `RETURNING`.
- **UPDATE sin WHERE.** La doc de PostgreSQL no lo dice explícito. Lo que dice es que actualiza "all rows that satisfy the condition" (https://www.postgresql.org/docs/current/sql-update.html). Que sin WHERE se actualiza todo es la lectura natural de la sintaxis, y es lo que hay que enseñar. No tengo una cita literal de doc ni una fuente de seguridad (hueco menor). Lo que sí dice la doc: con FROM "you should ensure that the join produces at most one output row for each row to be modified".
- **RETURNING en UPDATE**: `UPDATE weather SET temp_lo = temp_lo+1 ... RETURNING temp_lo, temp_hi, prcp, old.prcp AS old_prcp;`. El uso de `old.` en RETURNING es de versiones recientes; no leí desde cuándo.

**Recurso canónico.** PostgreSQL, "INSERT", sección "ON CONFLICT Clause" y "Compatibility". Fijarse en: qué es extensión y qué es estándar. Para el dialecto, el trío SQLite, MySQL y la nota de compatibilidad de PostgreSQL.

---

## 8. definir-tablas

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| PostgreSQL, 5.5 Constraints https://www.postgresql.org/docs/current/ddl-constraints.html | primaria | 3 | 3 | 3 | 3 | [L] |
| PostgreSQL, ALTER TABLE https://www.postgresql.org/docs/current/sql-altertable.html | primaria | 3 | 3 | 3 | 3 | [L] |
| PostgreSQL, CREATE MATERIALIZED VIEW https://www.postgresql.org/docs/current/sql-creatematerializedview.html | primaria | 3 | 2 | 1 | 3 | [L] |
| Flyway (Redgate), Migrations https://documentation.red-gate.com/fd/migrations-271585107.html | primaria de la herramienta | 2 | 1 | 1 | 2 | [L], poco contenido |

**Afirmaciones**
- **CHECK** (https://www.postgresql.org/docs/current/ddl-constraints.html): "a check constraint is satisfied if the check expression evaluates to true or the null value". Por eso un CHECK solo no impide NULL: hace falta NOT NULL.
- **UNIQUE.** "By default, two null values are not considered equal in this comparison", así que se pueden guardar varias filas con NULL en la columna única, salvo con `NULLS NOT DISTINCT`.
- **PRIMARY KEY** es único más no nulo.
- **FOREIGN KEY.** "The default ON DELETE action is ON DELETE NO ACTION". `RESTRICT` "does not allow the check to be deferred", `CASCADE` borra las filas dependientes, y hay `SET NULL` y `SET DEFAULT`. La doc recomienda CASCADE solo cuando las filas hijas no pueden existir sin la fila padre (esa guía la resumió el lector, no la cité literal).
- **Ejemplo de la doc**, con `products` y `orders`:
  ```sql
  CREATE TABLE products (product_no integer PRIMARY KEY, name text NOT NULL, price numeric CHECK (price > 0), sku text UNIQUE);
  CREATE TABLE orders (order_id integer PRIMARY KEY, product_no integer NOT NULL REFERENCES products (product_no) ON DELETE RESTRICT, quantity integer CHECK (quantity > 0));
  ```
  Ojo: este bloque lo armó el lector con el esquema de la doc, no es una cita literal. Es un buen punto de partida, pero conviene reescribirlo con las tablas del comercio.
- **ALTER TABLE ADD COLUMN con DEFAULT** (https://www.postgresql.org/docs/current/sql-altertable.html): con un default no volátil, el valor se guarda en los metadatos "making the ALTER TABLE very fast even on large tables". Con un default volátil (`clock_timestamp()`), una columna generada almacenada, una de identidad o un dominio con restricciones, se reescribe la tabla entera y sus índices.
- **Bloqueos.** "An ACCESS EXCLUSIVE lock is acquired unless explicitly noted". `ADD FOREIGN KEY` pide solo `SHARE ROW EXCLUSIVE`. Con `NOT VALID` se evita el escaneo largo, y después `VALIDATE CONSTRAINT` toma `SHARE UPDATE EXCLUSIVE`.
- **Vista materializada.** "The query is executed and used to populate the view at the time the command is issued [...] and may be refreshed later using REFRESH MATERIALIZED VIEW" (https://www.postgresql.org/docs/current/sql-creatematerializedview.html). Que no se actualiza sola es inferencia del lector.
- **Migraciones versionadas.** Flyway las describe como "versioned or repeatable or baseline" y registra lo aplicado en una tabla de historial. No logré confirmar de esa página la convención de nombres (`V1__...`), la inmutabilidad ni los checksums. Es un hueco.

**Recurso canónico.** PostgreSQL 5.5 "Constraints" y la sección "Notes" de ALTER TABLE. Fijarse en: que CHECK deja pasar NULL.

---

## 9. indice

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| use-the-index-luke.com (Winand), varias páginas | secundaria, practicante | 2 | 3 | 3 | 3 | [L] (páginas listadas abajo) |
| SQL Performance Explained, libro https://sql-performance-explained.com/ | secundaria, practicante | 2 | 3 | 2 | 3 | [M] metadatos y capítulos |
| PostgreSQL, 11.3 Multicolumn Indexes https://www.postgresql.org/docs/current/indexes-multicolumn.html | primaria | 3 | 2 | 2 | 2 | [L] |
| PostgreSQL, 11.1 Index Types (B-tree) https://www.postgresql.org/docs/current/indexes-types.html | primaria | 3 | 2 | 1 | 2 | [L] |
| PostgreSQL, 11.7 Indexes on Expressions https://www.postgresql.org/docs/current/indexes-expressional.html | primaria | 3 | 2 | 2 | 3 | [L] |
| PostgreSQL, 14.1 Using EXPLAIN https://www.postgresql.org/docs/current/using-explain.html | primaria | 3 | 3 | 3 | 3 | [L] |

**Afirmaciones**
- **Qué operadores usan un B-tree.** "the PostgreSQL query planner will consider using a B-tree index whenever an indexed column is involved in a comparison using one of these operators: < <= = >= >" (https://www.postgresql.org/docs/current/indexes-types.html).
- **LIKE.** Se usa un B-tree si el patrón es constante y está "anchored to the beginning of the string — for example, col LIKE 'foo%' [...] but not col LIKE '%bar'". Con una configuración regional que no sea C hace falta una clase de operador especial (misma URL). ILIKE usa el índice solo si el patrón empieza con caracteres que no cambian con mayúsculas.
- **Winand sobre LIKE.** "Avoid LIKE expressions with leading wildcards (e.g., '%TERM')". Esa condición "cannot serve as an access predicate". PostgreSQL es la excepción con un parámetro enlazado: "just does not use an index in that case" (https://use-the-index-luke.com/sql/where-clause/searching-for-ranges/like-performance-tuning).
- **Función sobre la columna.** En PostgreSQL: `WHERE lower(col1) = 'value'` puede usar un índice si se define `CREATE INDEX test1_lower_col1_idx ON test1 (lower(col1));`. Costo: los índices de expresión "are relatively expensive to maintain, because the derived expression(s) must be computed for each row insertion and non-HOT update" (https://www.postgresql.org/docs/current/indexes-expressional.html).
- **Winand sobre la misma idea.** "The UPPER function is just a black box" para el optimizador. Para SQL Server y MySQL hay que usar una columna calculada indexada, según la página (https://use-the-index-luke.com/sql/where-clause/functions/case-insensitive-search). **Discrepancia a notar:** la doc de PostgreSQL y Winand dicen lo mismo sobre PostgreSQL y Oracle, y difieren en que Winand señala que MySQL y SQL Server no tienen índices de función puros. Esa afirmación de Winand es sobre las versiones que cubría; no la verifiqué contra la doc actual de MySQL 8.4 (que tiene índices funcionales, según mi memoria: a confirmar).
- **Índice compuesto, orden de columnas.** Regla de la doc: "equality constraints on leading columns, plus any inequality constraints on the first column that does not have an equality constraint, will always be used to limit the portion of the index that is scanned". Para un índice `(a, b, c)` con `WHERE a = 5 AND b >= 42 AND c < 77`, "the index might have to be scanned from the first entry with a = 5 and b = 42 up through the last entry with a = 5" (https://www.postgresql.org/docs/current/indexes-multicolumn.html). Hay además una optimización de "skip scan" que puede aplicarse sin restricción sobre la columna inicial, pero solo conviene con pocos valores distintos.
- **Winand, mismo tema.** "In general, a database can use a concatenated index when searching with the leading (leftmost) columns", con la analogía de la guía telefónica (https://use-the-index-luke.com/sql/where-clause/the-equals-operator/concatenated-keys).
- **Costo en escritura (Winand).** "The number of indexes on a table is the most dominant factor for insert performance". "adding a single index is enough to increase the execute time by a factor of a hundred" (https://use-the-index-luke.com/sql/dml/insert). Es un benchmark de un caso de la página, no una regla general: yo lo citaría con esa etiqueta. Sobre UPDATE y DELETE la página no da cifras.
- **EXPLAIN** (https://www.postgresql.org/docs/current/using-explain.html):
  - Sin WHERE, el planificador elige "a simple sequential scan plan". Ejemplo: `Seq Scan on tenk1 (cost=0.00..445.00 rows=10000 width=244)`.
  - Con `WHERE unique1 = 42` aparece `Index Scan using tenk1_unique1 on tenk1 (cost=0.29..8.30 rows=1 width=244)`.
  - Los costos son "arbitrary units"; el tiempo real de ANALYZE es en milisegundos, así que no coinciden.
  - **Advertencia importante:** "With this option, EXPLAIN actually executes the query". Para analizar un UPDATE sin cambiar datos, la doc propone `BEGIN; EXPLAIN ANALYZE UPDATE ...; ROLLBACK;`.
  - El cálculo del costo del Seq Scan: (páginas leídas × `seq_page_cost`) + (filas × `cpu_tuple_cost`) = (345 × 1.0) + (10000 × 0.01) = 445.

**Recurso canónico.** Para quien consulta: use-the-index-luke.com, capítulo "The Where Clause" (páginas de concatenated keys, funciones y LIKE). Para leer un plan, PostgreSQL 14.1 "Using EXPLAIN". Fijarse en: que el planificador puede elegir Seq Scan aunque haya índice (si hay muchas filas o pocas), y que ANALYZE ejecuta de verdad. Marca de practicante: el sitio de Winand tiene copyright 2010-2026 y no declara licencia abierta; no citarlo masivamente.

---

## 10. sql-desde-una-aplicacion

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| OWASP SQL Injection Prevention Cheat Sheet https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html | primaria (estándar de la industria) | 3 | 2 | 2 | 3 | [L] |
| OWASP Top 10 2021, A03 Injection https://top10.owasp.org/2021/A03_2021-Injection | primaria | 3 | 1 | 1 | 2 | [L] |
| Django, QuerySet API https://docs.djangoproject.com/en/5.2/ref/models/querysets/ | primaria de una herramienta | 3 | 2 | 2 | 2 | [L] (primeros 100000 de 184649 caracteres) |
| Karwin, SQL Antipatterns, "SQL Injection" y "Implicit Columns" | secundaria, practicante | 2 | 2 | 1 | 3 | [M] |

**Afirmaciones**
- **Defensa primaria** (https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html): consultas parametrizadas, luego lista permitida para lo que no se puede parametrizar (nombres de tabla o columna, sentido del orden), y escapar a mano está "STRONGLY DISCOURAGED". "Input validation complements parameter binding; it does not replace it."
- **Cómo funciona.** "Define the SQL structure separately from its data values and bind those values through the database API". Ejemplo en Java:
  ```java
  String query = "SELECT account_balance FROM user_data WHERE user_name = ?";
  PreparedStatement statement = connection.prepareStatement(query);
  statement.setString(1, customerName);
  ```
  Una entrada como `tom' or '1'='1` se trata como un nombre literal. El ejemplo de OWASP no es de Python ni de JavaScript; la sintaxis del marcador (`?`, `$1`, `%s`) cambia según el driver (no verificado en esta ronda).
- **Por qué escapar es frágil.** "SQL escaping rules are not always straightforward", y varían entre dialectos; por ejemplo el modo `NO_BACKSLASH_ESCAPES` de MySQL.
- **Menor privilegio** como defensa adicional.
- **OWASP Top 10 2021 (A03).** "94% of the applications were tested for some form of injection", con tasa máxima de incidencia 19.09%, promedio 3.37%, 274,228 ocurrencias totales y 33 CWE asignados. "Injection slides down to the third position" (https://top10.owasp.org/2021/A03_2021-Injection). Es la edición 2021; la página lleva copyright "2021-2025" y no menciona una edición más nueva. **No verifiqué si existe una edición posterior de la lista** (hueco): antes de publicar el dato conviene mirar https://owasp.org/Top10/.
- **Con ORM.** OWASP indica como preferido una API segura que "avoids using the interpreter entirely", incluyendo ORMs (misma fuente).
- **N+1 y ORM** (https://docs.djangoproject.com/en/5.2/ref/models/querysets/): `select_related` "results in a single more complex query" con un JOIN. `prefetch_related` hace "a separate lookup for each relationship, and does the 'joining' in Python". Sobre el caso de las pizzas: sin precarga "Pizza.objects.all() will run a query on the Toppings table for every item in the Pizza QuerySet", y con `prefetch_related("toppings")` se reduce "to just two queries". Es una fuente de una herramienta concreta, no una definición general del problema N+1; no encontré una fuente neutral que lo defina (hueco).
- **Pool de conexiones en una línea.** No investigué una fuente para esto en esta ronda. Es un hueco.
- **Karwin.** La tabla de capítulos incluye "SQL Injection: Execute unverified input as code → Trust no one" e "Implicit Columns: A shortcut that gets you lost → Name columns explicitly" (https://pragprog.com/titles/bksap1/sql-antipatterns-volume-1/). Libro: Bill Karwin, Pragmatic Bookshelf, octubre 2022, 378 páginas, ISBN 9781680508987. Es el volumen 1.

**Recurso canónico.** OWASP SQL Injection Prevention Cheat Sheet, secciones "Primary Defenses" y la parte de lista permitida. Fijarse en: que el ORDER BY o un nombre de columna dinámico no se puede parametrizar, y que ahí se usa una lista de valores permitidos.

---

## 11. Ficha dialectos-de-sql

| Fuente | Tipo | Aut. | Prof. | Ej. | Unic. | Marca |
|---|---|---|---|---|---|---|
| modern-sql.com, estándar https://modern-sql.com/standard | secundaria, practicante | 2 | 2 | 1 | 3 | [L] |
| ISO/IEC 9075-2:2023, ficha de VDE y ANSI (vía buscador) | primaria (metadatos) | 3 | 1 | 1 | 2 | [S] resultado del buscador |
| MySQL 8.4, SELECT y JOIN, identificadores, tipos numéricos | primaria | 3 | 2 | 2 | 3 | [L] |
| SQL Server (Microsoft Learn), TOP https://learn.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql | primaria | 3 | 3 | 3 | 3 | [L] |
| SQLite, datatypes y upsert | primaria | 3 | 3 | 2 | 3 | [L] |
| PostgreSQL, pattern matching (ILIKE) https://www.postgresql.org/docs/current/functions-matching.html | primaria | 3 | 2 | 1 | 2 | [L] |

**El estándar**
- **Última edición.** El buscador devolvió que ISO/IEC 9075-2:2023 es la sexta edición, junio de 2023 (vista previa de VDE y ANSI). No encontré una edición más nueva en esos resultados, pero no revisé el catálogo de ISO directamente (el enlace https://www.iso.org/standard/76583.html dio 403). Marca [S]: hay que confirmarlo contra ISO antes de escribirlo como hecho.
- **Qué trae SQL:2023** (https://modern-sql.com/standard): la nueva parte "9075-16:2023 Property Graph Queries (SQL/PGQ)", y mejoras de JSON. SQL:2019 agregó "9075-15:2019 Multi-dimensional arrays (SQL/MDA)", y SQL:2016 cubrió reconocimiento de patrones de filas y JSON en informes técnicos gratuitos. La separación entre partes es la cita fiable; "JSON en la parte 2" no está confirmado.
- **Precios y acceso.** El estándar "is public but not free". Se mencionan precios de partes sueltas (por ejemplo, ISO/IEC 9075-15 a CHF 198). La parte 1 de SQL:2023 se puede bajar de ISO, según el sitio.
- **El estándar nombra el año como un nombre propio**: "SQL:2023". La numeración "ISO/IEC 9075" más el número de parte es la forma de citar. Wikipedia lo llama novena edición de la norma (resultado del buscador, [S]).

**Diferencias concretas verificadas**
- **Límite de filas.**
  - PostgreSQL: `LIMIT` y `OFFSET` (https://www.postgresql.org/docs/current/sql-select.html). El FETCH FIRST también lo menciona la doc.
  - MySQL: `LIMIT row_count` o `LIMIT offset, count`. Ejemplo literal: `SELECT * FROM tbl LIMIT 5,10; # Retrieve rows 6-15`. "For compatibility with PostgreSQL, MySQL also supports the LIMIT row_count OFFSET offset syntax" (https://dev.mysql.com/doc/refman/8.4/en/select.html).
  - SQL Server: `TOP (n)`. Con ORDER BY. La doc aconseja: "always use an ORDER BY clause with the TOP clause", y para paginar usar `OFFSET` y `FETCH` (https://learn.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql). `TOP` y `OFFSET/FETCH` no se pueden combinar en el mismo nivel.
- **Upsert.**
  - PostgreSQL y SQLite: `ON CONFLICT (...) DO UPDATE SET ... = EXCLUDED....` (SQLite escribe `excluded.`).
  - MySQL: `ON DUPLICATE KEY UPDATE`.
  - MERGE: estándar, está en PostgreSQL. Si lo tienen MySQL o SQLite no lo verifiqué. La página de modern-sql sobre MERGE dio 404 y no pude confirmarlo; SQL Server tiene MERGE, según una frase de la doc de TOP (menciona `MERGE`).
- **FULL OUTER JOIN.** La doc de MySQL 8.4 no lo documenta en su gramática de JOIN (ver componente 2).
- **Booleanos.**
  - MySQL: `BOOL` y `BOOLEAN` son sinónimos de `TINYINT(1)`. "A value of zero is considered false. Nonzero values are considered true", y `TRUE` y `FALSE` son alias de 1 y 0 (https://dev.mysql.com/doc/refman/8.4/en/numeric-type-syntax.html).
  - SQLite: no hay tipo booleano, se guardan 0 y 1.
  - PostgreSQL y SQL Server: no abrí la parte de booleanos (hueco).
- **Comillas de identificadores.** MySQL usa comillas inversas (backtick) para nombres. Con el modo `ANSI_QUOTES`, las comillas dobles pasan a ser identificadores y las cadenas solo pueden ir con comillas simples (https://dev.mysql.com/doc/refman/8.4/en/identifiers.html). La contrapartida en PostgreSQL y SQL Server (comillas dobles y corchetes) no la leí en esta ronda.
- **ILIKE.** "This is not in the SQL standard but is a PostgreSQL extension" (https://www.postgresql.org/docs/current/functions-matching.html).
- **Fechas.** PostgreSQL tiene `timestamp` y `timestamptz`. SQLite no tiene tipo de fecha. La parte de MySQL y SQL Server no se leyó.

**Recurso canónico.** modern-sql.com/standard para el mapa de ediciones, y para cada diferencia la página del motor correspondiente (arriba). No hay una única tabla comparativa verificada que cubra los cuatro motores; ese es el mayor hueco de esta ficha.

---

## 12. Recursos de ejercicios para la ruta de aprendizaje

| Recurso | Qué es | Marca | Observaciones |
|---|---|---|---|
| pgexercises.com https://pgexercises.com/ | Preguntas sobre un único dataset, para acompañar un libro o la doc | [L] portada | Categorías: Basic, Joins and Subqueries, Modifying data, Aggregates, Date, String, Recursive. Licencia CC BY-SA 3.0. La página no dice cuántos ejercicios tiene ni si es gratis. La portada menciona ventanas pero no hay categoría aparte. |
| SQLBolt https://sqlbolt.com/ | 18 lecciones y un cierre, interactivas en el navegador | [L] índice | Cubre SELECT, JOIN, NULL, agregados, orden de ejecución, INSERT/UPDATE/DELETE y DDL. No cubre ventanas ni CTE en las lecciones; menciona subconsultas y uniones como extras. |
| Select Star SQL https://selectstarsql.com/ | Libro interactivo de Zi Chong Kao | [L] portada | "free of charge, free of ads and doesn't require registration". Datos CC0. Cinco capítulos, el más interesante para agregación y joins (capítulos 3 y 4). |

**Propuesta.**
- Un recurso de ejercicios que mapee mejor a las tablas del comercio es **pgexercises.com**: tiene categoría de joins, modificar datos, agregados, fechas y recursivas, y usa PostgreSQL. Fijarse en: la categoría "Joins and Subqueries" y "Aggregates".
- SQLBolt es la entrada más suave para quien viene de planillas y cubre el orden de ejecución.
- Select Star SQL es un buen cierre por la parte de agregados y joins con datos reales.
- Ninguno cubre ventanas con fuerza ni indexación (hueco).

---

## 13. Huecos y cosas a verificar

1. **Autojoin y fan-out.** Sin fuente de doc oficial que los trate por separado. El fan-out solo lo derivo de la definición de INNER JOIN.
2. **"Último pedido de cada cliente" en las cuatro formas.** Los esquemas del componente 4 son míos, sin ejecutar. Falta una fuente canónica y una ejecución contra una base real.
3. **UPDATE y DELETE sin WHERE.** La doc no lo dice explícito; no encontré una cita ni una fuente sobre protecciones (por ejemplo `sql_safe_updates` en MySQL).
4. **Migraciones versionadas.** Falta una fuente primaria sobre convención de nombres, inmutabilidad y checksums (Flyway o Liquibase). La página que abrí no lo cubre.
5. **Pool de conexiones.** No lo investigué en esta ronda.
6. **N+1 neutral.** Solo tengo la doc de Django, que trata un caso concreto. Falta una definición independiente del ORM.
7. **OWASP Top 10.** Verificar si hay una edición posterior a 2021 antes de citar números.
8. **Dialectos.** Faltan: booleanos y fechas en PostgreSQL y SQL Server, comillas de identificadores en PostgreSQL y SQL Server, FULL JOIN y MERGE en MySQL y SQLite, soporte de FILTER y de LATERAL por motor (la página de modern-sql sobre LATERAL dio 404 y la de MERGE también; la matriz de FILTER no era legible), y la versión en que PostgreSQL agregó MERGE y MATERIALIZED (las dos de memoria, no de doc).
9. **Estándar.** Confirmar "última edición" directamente en ISO (la ficha dio 403 y la edición 2023 viene de un buscador [S]). Confirmar qué parte contiene JSON.
10. **Índices.** Sin cobertura de índices parciales, de cobertura (INCLUDE) ni de orden en ORDER BY; no están en el pedido pero salen naturalmente. La afirmación de Winand sobre MySQL sin índices funcionales no se contrastó con la doc actual de MySQL.
11. **CMU 15-445.** Solo vi la fila del calendario; no abrí las notas ni las diapositivas, así que no sé qué cubren de ventanas y CTE.
12. **Winand y Karwin.** Del libro de Winand solo vi capítulos y precio ([M]); de Karwin solo la tabla de capítulos ([M]). Las afirmaciones de Winand salen de su sitio web, no del libro. Ninguno declara licencia abierta, así que habría que citar con enlace y no reproducir.
13. **Tablas de resultados.** Los resultados de los ejemplos de ON contra WHERE de la doc de PostgreSQL no llegaron en la captura; hay que ejecutar el ejemplo con las tablas del comercio.
14. **Lecturas parciales.** La doc de Django se leyó hasta el caracter 100000 de 184649. Ninguna de las páginas fue leída como HTML crudo (extractos de un modelo), por lo que conviene volver a la fuente antes de usar una cita literal en una nota.
