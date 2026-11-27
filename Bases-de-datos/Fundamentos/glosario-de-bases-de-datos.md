---
resumen: >-
  Los términos de bases de datos que más se confunden, cada uno con su nombre en inglés, una
  definición corta apoyada en la documentación de PostgreSQL y la nota del tema donde se trata.
estado: borrador
estabilidad: semi
fuentes:
  - "PostgreSQL Documentation, Appendix M. Glossary: https://www.postgresql.org/docs/current/glossary.html"
  - "PostgreSQL Documentation, 9.2 Comparison Functions and Operators: https://www.postgresql.org/docs/current/functions-comparison.html"
  - "PostgreSQL Documentation, 7.8 WITH Queries: https://www.postgresql.org/docs/current/queries-with.html"
  - "PostgreSQL Documentation, 3.5 Window Functions: https://www.postgresql.org/docs/current/tutorial-window.html"
  - "PostgreSQL Documentation, INSERT (ON CONFLICT Clause y Compatibility): https://www.postgresql.org/docs/current/sql-insert.html"
  - "PostgreSQL Documentation, 14.1 Using EXPLAIN: https://www.postgresql.org/docs/current/using-explain.html"
  - "PostgreSQL Documentation, 13.1 Introduction (MVCC) y 13.2 Transaction Isolation: https://www.postgresql.org/docs/current/mvcc-intro.html y https://www.postgresql.org/docs/current/transaction-iso.html"
  - "SQLite, UPSERT: https://www.sqlite.org/lang_upsert.html"
  - "OWASP, SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html"
  - "Las notas del tema que enlaza cada término, con sus propias fuentes"
  - "Bases-de-datos/.investigacion/posicion-contraria-y-fundamentos.md (glosario mínimo, sin fuente) y Bases-de-datos/.investigacion/sql.md"
aliases: [glosario de bases de datos, términos de bases de datos, vocabulario de bases de datos, database glossary]
creado: 2026-11-27
revisado:
---

# Glosario de bases de datos

Los términos de bases de datos que más se confunden, cada uno con su nombre en inglés, una
definición corta apoyada en la documentación de PostgreSQL y la nota del tema donde se trata.

Las definiciones siguen el glosario de PostgreSQL (apéndice M) o, si el término no está ahí, la
página de su documentación que lo trata; las que no tienen fuente lo dicen. En el tema se usa el
término de la primera columna.

## Los datos y su forma

| Término | Inglés | Qué es | Dónde vive |
|---|---|---|---|
| Base de datos | Database | Para PostgreSQL, "a named collection of local SQL objects": un conjunto con nombre de tablas y otros objetos. En el habla corriente también se le dice así al programa, que en esta base se llama motor | [Bases de datos](../bases-de-datos.md) |
| Motor de base de datos | DBMS, database engine, database server | El programa que guarda los datos y atiende las consultas. PostgreSQL lo llama instancia: un grupo de procesos que maneja "exactly one database cluster with all its databases" | [Motores de bases de datos](../Elegir-una-base/motores-de-bases-de-datos.md) |
| Relación | Relation | En matemática, "a set of tuples", que es el sentido de "relational database". No quiere decir "vínculo entre tablas": una relación es una tabla. PostgreSQL usa además la palabra para cualquier objeto con nombre y columnas (tablas, vistas, índices, secuencias) | [Base relacional](../Modelos-de-datos/base-relacional.md) |
| Tabla | Table | Un conjunto de filas con la misma estructura: la misma cantidad de columnas, en el mismo orden, con el mismo nombre y tipo. Es "the most common form of relation" | [Definir tablas](../SQL/definir-tablas.md) |
| Tupla, fila, registro | Tuple, row, record | Un conjunto de valores en un orden fijo. Según PostgreSQL, se le dice fila cuando el orden lo da una tabla y registro cuando lo da el resultado de una consulta. En el tema se usa fila | [Base relacional](../Modelos-de-datos/base-relacional.md) |
| Columna, atributo | Column, attribute | Un elemento con nombre y tipo de dato dentro de una fila; columna es "an attribute found in a table or view" | [Definir tablas](../SQL/definir-tablas.md) |
| Esquema (estructura) | Schema | La estructura declarada de una base: tablas, columnas, tipos y restricciones. Es el uso corriente; el glosario de PostgreSQL no lo define con este sentido | [Definir tablas](../SQL/definir-tablas.md) |
| Esquema (espacio de nombres) | Schema | En PostgreSQL, "a namespace for SQL objects, which all reside in the same database": una carpeta dentro de la base, como `public`. Mismo nombre, otra cosa que el sentido anterior | [Definir tablas](../SQL/definir-tablas.md) |
| Tipo de dato | Data type | Qué clase de valor admite una columna (número, texto, fecha). El glosario de PostgreSQL no tiene entrada propia | [NULL y tipos](../SQL/null-y-tipos.md) |
| NULL | NULL | La marca de valor desconocido o ausente. Las comparaciones con NULL dan NULL, "not true or false": `7 = NULL` no es falso sino desconocido | [NULL y tipos](../SQL/null-y-tipos.md) |
| Restricción | Constraint | "A restriction on the values of data allowed within a table": una regla que la base hace cumplir (`NOT NULL`, `UNIQUE`, `CHECK`, claves) | [Definir tablas](../SQL/definir-tablas.md) |
| Clave primaria | Primary key | La columna o columnas que identifican cada fila: un caso de restricción única que además impide valores nulos. Hay "only one primary key per table" | [Definir tablas](../SQL/definir-tablas.md) |
| Clave foránea | Foreign key | Una restricción que exige que el valor de unas columnas identifique "zero or one row in another (or, infrequently, the same) table": el cliente de un pedido tiene que existir | [Definir tablas](../SQL/definir-tablas.md) |
| Restricción única | Unique constraint | Impide que un valor o una combinación de valores aparezca dos veces en la tabla | [Definir tablas](../SQL/definir-tablas.md) |
| Vista | View | Una consulta guardada con nombre, sin datos propios: cada vez que se la usa, su definición se reemplaza en la consulta "as if the user had typed it as a subquery" | [Definir tablas](../SQL/definir-tablas.md) |
| Índice | Index | Una estructura derivada de una tabla que permite encontrar filas rápido sin leerla entera; acelera lecturas y encarece escrituras | [Índice](../SQL/indice.md) |

## Consultar y modificar

| Término | Inglés | Qué es | Dónde vive |
|---|---|---|---|
| SQL | Structured Query Language | El lenguaje de las bases relacionales para consultar, modificar y definir datos; tiene un estándar ISO y un dialecto por motor. Sin definición propia en el glosario de PostgreSQL | [SQL](../SQL/sql.md) |
| Consulta | Query | Para PostgreSQL, un pedido del cliente a la base "usually to return results or to modify data". Confunde porque en castellano se piensa como lectura, y un `UPDATE` también es una consulta | [Consulta SELECT](../SQL/consulta-select.md) |
| Join | Join | Combinar filas de dos tablas según una condición, como pedidos con sus clientes | [Join](../SQL/join.md) |
| Agregación | Aggregation | Resumir muchas filas en una por grupo con funciones como `SUM` o `COUNT` y `GROUP BY` | [Agregación](../SQL/agregacion.md) |
| Subconsulta | Subquery | Una consulta adentro de otra. Sin definición propia en el glosario de PostgreSQL | [Subconsultas y CTE](../SQL/subconsultas-y-cte.md) |
| CTE | Common table expression, `WITH` query | Una consulta auxiliar con nombre al principio de otra, con `WITH`; según PostgreSQL, "can be thought of as defining temporary tables that exist just for one query" | [Subconsultas y CTE](../SQL/subconsultas-y-cte.md) |
| Función de ventana | Window function | Un cálculo sobre filas relacionadas con la fila actual que, a diferencia de `GROUP BY`, no las colapsa: "the rows retain their separate identities" | [Funciones de ventana](../SQL/funciones-de-ventana.md) |
| Upsert | Upsert | Insertar una fila o, si ya existe, actualizarla. En PostgreSQL y SQLite es `INSERT ... ON CONFLICT ... DO UPDATE`; según SQLite, "UPSERT is not standard SQL", y el estándar tiene `MERGE` | [Modificar datos](../SQL/modificar-datos.md) |
| Plan de ejecución | Query plan, `EXPLAIN` | Cómo decidió la base resolver una consulta (leer toda la tabla, usar un índice). `EXPLAIN` lo muestra; con `ANALYZE`, "EXPLAIN actually executes the query" | [Índice](../SQL/indice.md) |
| Migración | Migration | Un cambio versionado al esquema (agregar una columna, una tabla), aplicado en orden y registrado. Sin definición en el glosario de PostgreSQL | [Definir tablas](../SQL/definir-tablas.md) |
| ORM | Object-relational mapper | Una biblioteca que traduce objetos del código a filas y genera el SQL. Sin definición en el glosario de PostgreSQL; OWASP la nombra entre las formas seguras de hablarle a la base | [SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md) |
| Problema N+1 | N+1 query problem | Una consulta para traer N filas y después una más por cada una, en vez de una sola con un join. No se encontró una definición neutral, solo ejemplos de un ORM concreto | [SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md) |
| Inyección SQL | SQL injection | Meter código SQL dentro de un dato que la aplicación pega en una consulta. La defensa principal de OWASP es "define the SQL structure separately from its data values": consultas parametrizadas | [SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md) |

## Transacciones

| Término | Inglés | Qué es | Dónde vive |
|---|---|---|---|
| Transacción | Transaction | Comandos que "all succeed or all fail as a single unit", y cuyos efectos no ven las demás sesiones hasta que termina | [Transacción](../Transacciones/transaccion.md) |
| Commit | Commit | Cerrar una transacción aplicando sus cambios, lo que los hace visibles y asegura su durabilidad | [Transacción](../Transacciones/transaccion.md) |
| Rollback | Rollback | Deshacer todo lo hecho desde el principio de la transacción | [Transacción](../Transacciones/transaccion.md) |
| Punto de guardado | Savepoint | Una marca dentro de una transacción a la que se puede volver sin descartar lo anterior | [Transacción](../Transacciones/transaccion.md) |
| ACID | Atomicity, consistency, isolation, durability | Las cuatro propiedades de una transacción: todo o nada, restricciones cumplidas al confirmar, efectos invisibles para las demás hasta el commit, y cambios que sobreviven a una caída | [Transacción](../Transacciones/transaccion.md) |
| Nivel de aislamiento | Isolation level | Cuánto ve una transacción de lo que escriben las otras: Read Uncommitted, Read Committed, Repeatable Read o Serializable. Por defecto cambia según el motor | [Nivel de aislamiento](../Transacciones/nivel-de-aislamiento.md) |
| MVCC | Multiversion concurrency control | Guardar varias versiones de cada fila para que cada sentencia lea una foto de los datos; por eso, en PostgreSQL, "reading never blocks writing and writing never blocks reading" | [Nivel de aislamiento](../Transacciones/nivel-de-aislamiento.md) |
| Actualización perdida | Lost update | Dos transacciones leen el mismo valor y la segunda escritura pisa a la primera. Es el caso de vender dos veces el último producto | [Concurrencia](../Transacciones/concurrencia.md) |
| Bloqueo pesimista | Pessimistic locking, `SELECT ... FOR UPDATE` | Bloquear las filas al leerlas para que nadie las cambie hasta el fin de la transacción | [Concurrencia](../Transacciones/concurrencia.md) |
| Bloqueo optimista | Optimistic locking | No bloquear al leer y detectar el conflicto al escribir, por ejemplo con una columna de versión | [Concurrencia](../Transacciones/concurrencia.md) |
| Deadlock | Deadlock | Dos transacciones que se esperan mutuamente; la base aborta una de las dos | [Concurrencia](../Transacciones/concurrencia.md) |
| Falla de serialización | Serialization failure | El error con que la base aborta una transacción que chocó con otra en Repeatable Read o Serializable; en PostgreSQL, SQLSTATE `40001`. Se reintenta la transacción entera | [Concurrencia](../Transacciones/concurrencia.md) |
