---
resumen: >-
  La bibliografía del tema Bases de datos: qué leer para entender los conceptos, para escribir SQL,
  para que las consultas anden rápido, para escribir código seguro y para saber cómo fallan los
  motores, con qué parte leer de cada fuente, en qué fijarse y cuánto se verificó.
estado: borrador
estabilidad: semi
fuentes:
  - "Martin Kleppmann, Designing Data-Intensive Applications (O'Reilly): https://dataintensive.net/ (solo la ficha del sitio)"
  - "Michael Stonebraker y Andrew Pavlo, What Goes Around Comes Around... And Around..., SIGMOD Record 53(2), junio de 2024, pp. 21-37: https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf"
  - "PostgreSQL Documentation, cap. 7 Queries: https://www.postgresql.org/docs/current/queries.html"
  - "PostgreSQL Documentation, cap. 13 Concurrency Control: https://www.postgresql.org/docs/current/mvcc.html"
  - "Markus Winand, Use The Index, Luke: https://use-the-index-luke.com/"
  - "Markus Winand, Modern SQL: https://modern-sql.com/"
  - "Bill Karwin, SQL Antipatterns, Volume 1 (Pragmatic Bookshelf, octubre de 2022): https://pragprog.com/titles/bksap1/sql-antipatterns-volume-1/ (solo la tabla de capítulos)"
  - "OWASP, SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html"
  - "OWASP Top 10 2021, A03 Injection: https://top10.owasp.org/2021/A03_2021-Injection"
  - "OWASP Top 10:2025 (Injection en A05): https://top10.owasp.org/2025/"
  - "Jepsen, índice de análisis: https://jepsen.io/analyses"
  - "CMU 15-445/645 Database Systems, Fall 2025: https://15445.courses.cs.cmu.edu/fall2025/schedule.html (solo el calendario)"
  - "Berenson y otros, A Critique of ANSI SQL Isolation Levels, SIGMOD 1995: https://arxiv.org/abs/cs/0701157 (abstract)"
  - "Warszawski y Bailis, ACIDRain, SIGMOD 2017: https://www.bailis.org/papers/acidrain-sigmod2017.pdf"
  - "Bases-de-datos/.investigacion/ (informes del 2026-11-27)"
aliases: [fuentes de bases de datos, bibliografía de bases de datos, qué leer de bases de datos, libros de SQL, database reading list]
creado: 2026-11-27
revisado:
---

# Fuentes de bases de datos

La bibliografía del tema Bases de datos: qué leer para entender los conceptos, para escribir SQL,
para que las consultas anden rápido, para escribir código seguro y para saber cómo fallan los
motores, con qué parte leer de cada fuente, en qué fijarse y cuánto se verificó.

Cada fuente lleva cuánto se leyó para escribir las notas del tema. Una fuente marcada "solo la
ficha" o "solo el abstract" puede ser excelente, pero lo que las notas dicen de ella no se contrastó
con el texto.

## Cómo se pesa una fuente de bases de datos

Ninguna fuente leída da pesos por tipo: los pesos son de esta base.

| Tipo | Ejemplos | Sirve para | Peso | Por qué |
|---|---|---|---|---|
| Documentación oficial de cada motor | PostgreSQL, MySQL, SQL Server, SQLite | Qué hace ese motor, con qué sintaxis y qué garantiza | Alto, para su motor | Es la definición del comportamiento; describe su motor y no compara |
| Análisis empíricos independientes | Jepsen | Si un motor cumple lo que su documentación promete | Alto | Pruebas publicadas con método; muestran errores, no prueban su ausencia |
| Papers con revisión | Codd 1970, Berenson y otros 1995, ACIDRain 2017, Stonebraker y Pavlo 2024 | Conceptos, historia y mediciones | Alto | Método publicado; algunos autores son parte interesada |
| Libros y sitios de practicantes | Kleppmann, Winand, Karwin, Fowler | Explicar y ordenar el campo | Medio-alto | Buenos para entender; sus benchmarks son de un caso |
| Guías de seguridad | OWASP | Cómo escribir código que no se pueda atacar | Alto en su tema | Consenso de la industria, mantenido en abierto |
| Blogs de proveedores y comparativas | Páginas de quien vende una base o un servicio administrado | Ubicarse y conocer opciones | Bajo | Favorecen lo que venden |

## Para entender los conceptos

- **Martin Kleppmann, *Designing Data-Intensive Applications* (O'Reilly).** Una explicación de
  referencia, para un público técnico general, de modelos de datos y transacciones: ACID, niveles de
  aislamiento, write skew y serializabilidad. Conviene leer el capítulo de modelos de datos y el de
  transacciones, y fijarse en cómo arma cada anomalía con un ejemplo. **Advertencia:** la edición
  vigente, la editorial de cada edición y la numeración de capítulos no se verificaron; el sitio del
  autor no da esos datos y no se confirmó si hay una segunda edición. Las notas del tema citan "caps.
  2 y 7" sin haberlo comprobado.
- **Stonebraker y Pavlo, "What Goes Around Comes Around... And Around..." (2024).** Repasa veinte
  años de alternativas al modelo relacional (MapReduce, clave-valor, documentos, columnas, vectores,
  grafos) y sostiene que SQL absorbe lo bueno de cada una. Leer la introducción y la sección de
  documentos, que es corta y toma posición clara; fijarse en lo que concede a los documentos
  (sin N+1, sin traducir objetos a tablas). Stonebraker fundó empresas relacionales: es parte
  interesada. Se leyeron el abstract, la sección de documentos y las conclusiones.
- **Berenson, Bernstein, Gray y otros, "A Critique of ANSI SQL Isolation Levels" (1995).** El paper
  que mostró que las definiciones del estándar no describen bien los niveles que usan los motores, y
  que definió snapshot isolation. Leer el abstract y la tabla de fenómenos. Solo se leyó el abstract.

## Para escribir SQL

- **Documentación de PostgreSQL, capítulo 7 (Queries).** La referencia de cómo se arma una consulta.
  Leer 7.1 para la forma general, 7.2 para `FROM`, joins, `WHERE` y `GROUP BY`, y 7.8 para `WITH`.
  Fijarse en la diferencia entre poner una condición en `ON` o en `WHERE` en un outer join: "That does
  not matter with inner joins, but it matters a lot with outer joins". Para ventanas, el tutorial 3.5.
- **Markus Winand, modern-sql.com.** Qué agrega cada edición del estándar y qué motor soporta qué.
  Leer la página del estándar para el mapa de ediciones y la de cada característica que se use
  (`FILTER`, `IS DISTINCT FROM`). Fijarse en las matrices de soporte: lo que PostgreSQL trata como
  normal puede faltar en otro motor. El sitio no declara licencia abierta: se cita con enlace.
- **Bill Karwin, *SQL Antipatterns, Volume 1* (Pragmatic Bookshelf, octubre de 2022, 378 páginas).**
  Errores comunes de diseño y de consulta, cada uno con su solución: tratar NULL como un valor
  común ("Fear of the Unknown"), columnas implícitas con `SELECT *`, inyección SQL. Leer los
  capítulos de lo que se esté por hacer; fijarse en el par antipatrón y solución de cada uno. Solo se
  vio la tabla de capítulos.
- **CMU 15-445/645 Database Systems.** Curso universitario con el calendario publicado. Según el
  resumen de un buscador, el de otoño de 2026 lo da Jignesh Patel. La clase 2 del calendario de
  otoño de 2025 se llama "Modern SQL". Solo se vio la fila del calendario: el contenido de esa clase
  y cuánto del curso trata el interior del motor, que queda fuera de este tema, no se verificaron.

Los ejercicios para practicar (pgexercises, SQLBolt, Select Star SQL) están en la
[ruta de SQL](ruta-de-sql.md).

## Para que las consultas anden rápido

- **Markus Winand, use-the-index-luke.com** (y su libro *SQL Performance Explained*). La explicación
  de índices para quien escribe consultas, sin entrar al motor. Leer el capítulo "The Where Clause":
  las páginas de claves concatenadas, de funciones y de `LIKE`. Fijarse en la regla de las columnas
  de la izquierda ("a database can use a concatenated index when searching with the leading
  (leftmost) columns") y en por qué `LIKE '%texto'` no usa el índice. Su cifra de que un índice más
  puede multiplicar por cien el tiempo de un `INSERT` es de un caso de la página, no una regla. Del
  libro solo se vieron los capítulos.
- **Documentación de PostgreSQL, 14.1 Using EXPLAIN.** Cómo se lee un plan. Fijarse en que los
  costos son unidades arbitrarias y en que `EXPLAIN ANALYZE` ejecuta la consulta de verdad: para un
  `UPDATE`, hay que envolverlo en `BEGIN` y `ROLLBACK`. Se aplica en [índice](../SQL/indice.md).

## Para escribir código seguro

- **OWASP, SQL Injection Prevention Cheat Sheet.** La guía de referencia contra la inyección SQL.
  Leer "Primary Defenses" y la parte de lista permitida. Fijarse en que los nombres de tabla o de
  columna y el sentido de un `ORDER BY` no se pueden parametrizar, y ahí va una lista de valores
  permitidos; y en que "input validation complements parameter binding; it does not replace it".
- **OWASP Top 10 2021, A03 Injection.** Para dimensionar el problema: en 2021, "94% of the
  applications were tested for some form of injection". En la edición 2025
  (https://top10.owasp.org/2025/) Injection quedó quinta (A05); sus cifras no se revisaron, así que
  conviene leerla antes de citar números nuevos.

Cómo se aplican las dos está en [SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md).

## Para las transacciones y cómo fallan los motores

- **Documentación de PostgreSQL, capítulo 13 (Concurrency Control).** La referencia de cómo se hacen
  las transacciones en un motor real. Leer 13.1 (MVCC), 13.2 (niveles) y 13.3 (bloqueos explícitos).
  Fijarse en la tabla 13.1, en los párrafos de Read Committed sobre dos sesiones que actualizan la
  misma fila y en la obligación de reintentar ante el SQLSTATE `40001`. Se aplica en
  [nivel de aislamiento](../Transacciones/nivel-de-aislamiento.md) y
  [concurrencia](../Transacciones/concurrencia.md).
- **Jepsen.** Análisis independientes que prueban si un motor cumple lo que promete. Leer el
  abstract y la sección del nivel que se use en los análisis de PostgreSQL 12.3 (2020), MySQL 8.0.34
  (2023), MongoDB 4.2.6 (2020) y Amazon RDS for PostgreSQL 17.4 (2025). Fijarse en qué es un error
  corregido y qué es el comportamiento esperado del nivel. Los análisis se leyeron por su resumen.
- **Warszawski y Bailis, "ACIDRain" (SIGMOD 2017).** El estudio de 12 aplicaciones de comercio
  electrónico con 22 ataques de concurrencia. Leer el abstract y la introducción; fijarse en que 17
  de los 22 aparecen aun con el aislamiento más fuerte. Se leyeron el abstract, la introducción y el
  análisis.
- **La página de aislamiento de cada motor.** Para MySQL, SQL Server y SQLite, que tienen otro nivel
  por defecto que PostgreSQL; las direcciones están en
  [nivel de aislamiento](../Transacciones/nivel-de-aislamiento.md).

## Lo que falta leer

> [!NOTE]
> Sin fuente todavía: la edición y los capítulos de Kleppmann; *Database System Concepts* de
> Silberschatz, que no se abrió; el cuerpo de Codd 1970; el contenido de CMU 15-445; los libros de
> Winand y Karwin más allá de su índice; y una fuente neutral que defina el problema N+1.
