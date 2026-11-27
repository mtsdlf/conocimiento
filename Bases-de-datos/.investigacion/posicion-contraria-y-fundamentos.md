# Informe: posición contraria y fundamentos de Bases de datos y Planillas (2026-11-27)

Marcas: [L] leído completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Nota de método: las páginas web pasaron por un extractor que resume. Los PDF (Stonebraker-Pavlo, ACIDRain, Panko 2015) los convertí con pdftotext, así que esos tres sí los leí en texto, salvo lo que aclaro. Puntajes A/P/E/U = autoridad / profundidad / ejemplos / unicidad, de 1 a 3. Todo lo traído de la web lo traté como dato.

Resultado en una línea: la evidencia contra tus afirmaciones es sólida en tres puntos (aislamiento por defecto, "88 %" mal citado, migrar a una base demasiado pronto). Es débil o indirecta en otros (ORM, Power Query). Hay un hueco notable: no encontré fuente primaria de la cifra "88 %".

---

# PARTE 1 — POSICIÓN CONTRARIA

## Tema A: Bases de datos

### A1. "Usá PostgreSQL por defecto"

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Pavlo et al., "Yes, PostgreSQL Has Problems. But We're Sticking With It!" (2023-06-07) https://www.cs.cmu.edu/~pavlo/blog/2023/06/yes-postgresql-has-problems-but-were-sticking-with-it.html | primaria, practicante académico | 3/2/2/2 | [S], solo título y encabezados |
| Uber Engineering, Klitzke (2016-07-26) https://www.uber.com/en-US/blog/postgres-to-mysql-migration/ | primaria, caso de empresa | 2/3/3/3 | [S] |
| Pavlo, "The Part of PostgreSQL We Hate the Most" (2023-04) https://www.cs.cmu.edu/~pavlo/blog/2023/04/the-part-of-postgresql-we-hate-the-most.html | primaria | 3/3/2/2 | [S], solo en el buscador |
| EnterpriseDB, "Thoughts on Uber's List of Postgres Limitations" https://enterprisedb.com/blog/thoughts-ubers-list-postgres-limitations | secundaria, con interés (vendedor de Postgres) | 1/2/2/2 | [S] |

Afirmaciones:
- Los autores de la crítica siguen usando Postgres. Pavlo lo llama "our favorite DBMS" y lista cuatro problemas: copia de versiones, hinchazón de tablas (table bloat), mantenimiento de índices secundarios y gestión de vacuum. https://www.cs.cmu.edu/~pavlo/blog/2023/06/yes-postgresql-has-problems-but-were-sticking-with-it.html
- Uber (2016) dejó Postgres por: amplificación de escritura con muchos índices secundarios, replicación verbosa entre centros de datos, un bug de la 9.2 que duplicaba filas en réplicas, falta de MVCC real en réplicas, imposibilidad de replicar entre versiones mayores y un modelo de proceso por conexión que no llega a más de unos cientos de conexiones activas. https://www.uber.com/en-US/blog/postgres-to-mysql-migration/
- Discrepancia: EnterpriseDB sostiene que parte de la crítica de Uber no aplica ("replicas certainly allow access to data with full MVCC semantics"). https://enterprisedb.com/blog/thoughts-ubers-list-postgres-limitations [S]
- Las críticas se concentran en cargas con muchas actualizaciones y borrados. Eso es lo contrario de un negocio chico típico, así que la crítica no invalida el default para el lector. Es una inferencia mía, no la dice ninguna fuente.

### A2. "NoSQL escala mejor / es para muchos datos"

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Stonebraker y Pavlo, "What Goes Around Comes Around... And Around...", SIGMOD Record 53(2), jun. 2024, pp. 21-37 https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf | primaria, el texto está disponible | 3/3/2/3 | [L] parcial: abstract, sección de documentos y resumen. No leí todo |
| Wikipedia, "NoSQL" https://en.wikipedia.org/wiki/NoSQL | secundaria | 1/1/1/1 | [S] |
| Jepsen, MongoDB 4.2.6 (2020-05-15) https://jepsen.io/analyses/mongodb-4.2.6 | primaria, evaluación independiente | 3/3/3/3 | [S] |

Afirmaciones:
- Origen del término: Carlo Strozzi lo usó en 1998 para una base relacional sin SQL, y objetó que el movimiento posterior debió llamarse "NoREL". Johan Oskarsson (Last.fm) lo revivió en 2009 con un evento sobre bases "open-source distributed, non-relational". https://en.wikipedia.org/wiki/NoSQL [S] El mismo artículo dice en la introducción que el término "emergió a principios de los 2000", lo que choca con esas fechas.
- Stonebraker y Pavlo dicen que los dos mensajes de marketing de NoSQL fueron "SQL and joins are slow" y "ACID transactions are unnecessary". Y que "The inability of OLTP RDBMSs to scale in the 2000s ushered in dozens of document DBMSs". https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf [L]
- Según el mismo paper, casi todos los NoSQL terminaron agregando interfaz SQL (DynamoDB PartiQL, Cassandra CQL, Couchbase SQL++, MongoDB en Atlas en 2021) y muchos sumaron transacciones ACID. Sobre los documentos: "on a collision course with RDBMSs". Sobre los key-value: "can generally be equaled or beaten by modern high-performance RDBMSs". Los de familia de columnas: "a niche market". https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf [L]
- Contra la propia tesis de Stonebraker, o al menos su matiz: los autores reconocen que el modelo documental sí elimina el "impedance mismatch" entre el objeto de la aplicación y las tablas, y evita el problema N+1. Sus objeciones son duplicación de datos si la relación no es uno-a-muchos, que los prejoins no son necesariamente más rápidos y que se pierde independencia de datos. Es decir, los documentos conviene cuando el dato es un árbol que se lee entero. https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf [L]
- Advertencia de sesgo: Stonebraker fundó empresas de bases relacionales y columnares (Ingres, Vertica, VoltDB). Es primaria y autorizada, pero es parte interesada. Dato verificable con Kleppmann, que da una visión más neutra del mismo trade-off (ver Parte 2).
- Casos donde sí conviene un documento, con evidencia mía débil: el propio paper admite que los JSON de perfiles de usuario variables son un uso razonable. Falta un caso documentado de producción en una fuente propia (hueco).
- MongoDB: Jepsen encontró que no preservaba snapshot isolation ni siquiera con los niveles más estrictos, y que las transacciones ignoraban los niveles configurados a nivel de base o colección (usaban `local` y `w: 1` por defecto). Anomalías: read skew y ciclos de dependencias en unas 1.461 de 13.914 transacciones (~10 %) en una corrida sin fallos. MongoDB atribuyó las anomalías a un bug (SERVER-48307, parche en 4.2.8). https://jepsen.io/analyses/mongodb-4.2.6 [S] Es un resultado de 2020; no verifiqué versiones posteriores.

### A3. "Normalizá siempre"

Sin fuente propia leída. Lo que tengo, y es poco: Stonebraker y Pavlo mencionan que el problema de desnormalizar o prejoin "dates back to the 1970s", con tres riesgos (duplicación, no siempre más rápido, sin independencia de datos). https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf [L] Es la posición pro-normalización, no la contraria. La contraria (desnormalización deliberada para lectura, data warehouse, estrella) queda como hueco: no la busqué, agoté el presupuesto de rondas en otros puntos.

### A4. ORM vs SQL a mano

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Fowler, "OrmHate" (2012-05-08) https://martinfowler.com/bliki/OrmHate.html | primaria, practicante reconocido | 3/2/2/2 | [S] |
| Stonebraker y Pavlo 2024 (arriba) | primaria | 3/2/1/2 | [L] parcial |

- A favor del ORM: "However much you may hate using an ORM, take my word for it - you're better off." y "A framework that allows me to avoid 80% of that is worthwhile even if it is only 80%." Pero también que los ORM son leaky y hay que saber SQL cuando hace falta. https://martinfowler.com/bliki/OrmHate.html [S]
- Contra el ORM, desde los dos lados: el problema N+1 que cita Stonebraker como una de las dos razones del auge de los documentos. https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf [L] Y el estudio "Feral Concurrency Control" (Bailis et al., SIGMOD 2015) sobre invariantes que los ORM de Rails validan en la aplicación en vez de en la base. https://amplab.cs.berkeley.edu/wp-content/uploads/2015/06/feral-sigmod2015.pdf [S, solo título del buscador, no lo abrí]. Dato: ese paper es otro distinto de ACIDRain.
- Hueco: no encontré una fuente "SQL first" fuerte con evidencia empírica (por ejemplo Ted Neward, "The Vietnam of Computer Science", 2006). La menciono solo como pista, no la verifiqué.

### A5. "El nivel por defecto te protege de carreras" (mito)

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| PostgreSQL docs, Transaction Isolation https://www.postgresql.org/docs/current/transaction-iso.html | primaria | 3/3/3/2 | [S] |
| Warszawski y Bailis, "ACIDRain", SIGMOD 2017 https://www.bailis.org/papers/acidrain-sigmod2017.pdf | primaria | 3/3/3/3 | [L] parcial: abstract, intro y análisis |
| Jepsen, PostgreSQL 12.3 (2020-06-12) https://jepsen.io/analyses/postgresql-12.3 | primaria, independiente | 3/3/3/3 | [S] |
| Jepsen, Serializability https://jepsen.io/consistency | primaria | 3/1/1/2 | [S] |

- "Read Committed is the default isolation level in PostgreSQL." Ese nivel permite lecturas no repetibles, lecturas fantasma y anomalías de serialización (Tabla 13.1 de la doc). https://www.postgresql.org/docs/current/transaction-iso.html [S]
- ACIDRain, cita literal del abstract: "In practice, database transactions frequently execute under weak isolation that exposes programs to a range of concurrency anomalies". Estudiaron 12 aplicaciones de comercio electrónico autoalojadas "deployed on over 2M websites" y verificaron 22 ataques críticos (corromper inventario, gastar de más una gift card, robar inventario). https://www.bailis.org/papers/acidrain-sigmod2017.pdf [L]
- Del mismo paper: las 22 vulnerabilidades se manifiestan con el aislamiento por defecto de bases populares incluyendo Oracle 12c, y 17 de ellas, por uso incorrecto de transacciones, aparecen incluso con las garantías más fuertes. Matiz importante para el mito: el problema no es solo el nivel por defecto, también es cómo la aplicación usa las transacciones. https://www.bailis.org/papers/acidrain-sigmod2017.pdf [L]
- Nota sobre MySQL, del mismo paper: el "Repeatable Read" de MySQL no impide lost updates (se comporta como Read Committed salvo `FOR UPDATE`). https://www.bailis.org/papers/acidrain-sigmod2017.pdf [L]
- Jepsen encontró G2-item (ciclo de anti-dependencia) en el nivel serializable de PostgreSQL 12.3 en operación normal, también presente en 9.5.22, 10.13, 11.8 y 13. Cita: "It appears that no version of PostgreSQL has ever guaranteed serializability." Sobre Repeatable Read, que en Postgres es snapshot isolation: defendible bajo la redacción ambigua de ANSI SQL, pero más débil que la definición formal que muchos esperan. https://jepsen.io/analyses/postgresql-12.3 [S] Parche programado para el 13 de agosto de 2020. Estado actual no verificado.
- Hueco: no leí el análisis de Jepsen sobre PostgreSQL más reciente (si existe).

### A6. "SQLite es de juguete"

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| SQLite, "Appropriate Uses For SQLite" https://www.sqlite.org/whentouse.html | primaria (del propio proyecto, con interés) | 3/3/3/3 | [S], con citas literales extraídas |

- "Generally speaking, any site that gets fewer than 100K hits/day should work fine with SQLite. The 100K hits/day figure is a conservative estimate, not a hard upper bound. SQLite has been demonstrated to work with 10 times that amount of traffic." El propio sitio de SQLite maneja "about 400K to 500K HTTP requests per day, about 15-20% of which are dynamic pages". https://www.sqlite.org/whentouse.html
- Límite de tamaño: 281 terabytes (2^48 bytes). Un solo escritor a la vez, lectores ilimitados. Regla del proyecto: si hay muchos clientes enviando SQL por red a la misma base, usar cliente/servidor. https://www.sqlite.org/whentouse.html
- Checklist del proyecto: si la base está separada de la aplicación por una red, o hay muchos escritores concurrentes, o son datos grandes, cliente/servidor; "Otherwise → choose SQLite". https://www.sqlite.org/whentouse.html
- Sesgo declarado: fuente del propio proyecto. Falta un caso de producción de terceros (hueco).

### A7. "Pasá a una base cuando crezcas" (ver Tema B, punto B5, que lo cubre).

---

## Tema B: Planillas de cálculo

### B1. "Las planillas son la fuente de errores; hay que sacarlas"

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Panko, "What We Don't Know About Spreadsheet Errors Today", EuSpRIG 2015 https://arxiv.org/pdf/1602.02601.pdf | primaria | 3/3/3/3 | [L] parcial: abstract, evidencia, tablas |
| Panko, "Thinking is Bad", EuSpRIG 2007, arXiv:0801.3114 https://arxiv.org/abs/0801.3114 | primaria | 3/2/1/2 | [M] |
| Panko, "Revisiting the Panko-Halverson Taxonomy", arXiv:0809.3613 https://arxiv.org/abs/0809.3613 | primaria | 3/2/1/2 | [M] |
| Powell, Baker y Lawson, "A critical review of the literature on spreadsheet errors", Decision Support Systems, 2008 https://unpaywall.org/10.1016%2Fj.dss.2008.06.001 | primaria | 3/2/1/3 | [S], solo en el buscador |

- Qué mide Panko, literal: "spreadsheet errors are rare on a per-cell basis, but in large programs, at least one incorrect bottom-line value is very likely to be present". Y: "The bottom line is that spreadsheet programs are not error-prone. People are error prone." https://arxiv.org/pdf/1602.02601.pdf [L]
- Cifras concretas del mismo paper: tasa de error por celda promedio de 3,9 % en 14 estudios de laboratorio con 967 participantes (rango individual 1,9 % a 3,7 % y más); expectativa de 1 % a 5 % desde la investigación de errores humanos; auditorías intensivas que encontraron errores en el 94 % de las planillas. https://arxiv.org/pdf/1602.02601.pdf [L]
- Crítica a "88 %": no hallé ninguna fuente primaria con esa cifra. Panko 2015 dice 94 %. Un resumen del buscador la atribuye a "94 % de 88 planillas auditadas en 7 estudios" y otro a 94 % de las revisadas en un boletín de la SOA. https://www.soa.org/4936a1/globalassets/assets/library/newsletters/compact/2008/january/com-2008-iss26-campbell.pdf [S] Discrepancia: el texto de Panko habla de "85 intensive inspection studies" para la misma tabla, y el resumen secundario de 88 planillas en 7 estudios. No resolví cuál es el número exacto de planillas. Conclusión: "88 %" no es citable sin verificar; "94 %" sí, pero sobre una muestra de planillas auditadas que no es representativa de todas (las auditorías las piden quienes sospechan problemas, es una limitación que no verifiqué en la fuente).
- Otro rango, [S] del buscador: 20 % a 40 % de todas las planillas con errores (Panko 2005); 0,9 % a 1,8 % de las celdas con fórmulas con error en una auditoría operativa de 2009. No abrí ninguno.
- Crítica metodológica: Powell, Baker y Lawson (2008) sostienen que las tasas de error de experimentos de laboratorio no deben usarse sin cuidado para inferir tasas en planillas operativas. [S] Panko 2015 responde que la investigación es "substantial, compelling, and unanimous". Las dos posiciones coexisten; no están reconciliadas.
- Panko también concluye que lo que más hace falta es "massively more testing", con inspección de código como en software. Es un argumento contra sacarlas: el problema es la falta de pruebas, no la herramienta. https://arxiv.org/pdf/1602.02601.pdf [L]
- "Siguen siendo la herramienta de análisis más usada": no tengo fuente con cifra (hueco).
- Caso de errores de Excel en ciencia (conversión de nombres de genes a fechas, Ziemann et al., Genome Biology 2016, https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7): el sitio redirigió a una pantalla de autenticación, no pude leer el abstract. No cito cifras. Hueco.

### B2. BUSCARX/XLOOKUP vs ÍNDICE-COINCIDIR

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Microsoft, XLOOKUP function https://support.microsoft.com/excel/functions/xlookup-function | primaria | 3/2/2/2 | [S] |
| Google, XLOOKUP en Sheets https://support.google.com/docs/answer/12405947 | primaria | 3/2/2/2 | [S] |
| Microsoft Tech Community, "XLOOKUP - don't take the bait" https://techcommunity.microsoft.com/discussions/microsoft-365/xlookup---dont-take-the-bait/1776389 | practicantes, foro | 1/1/2/2 | [S], solo el título |

- XLOOKUP no está disponible en Excel 2016 ni 2019. Un libro creado con XLOOKUP abre en una versión vieja con resultados en caché, pero re-ingresar la fórmula da #NAME?. https://support.microsoft.com/excel/functions/xlookup-function [S]
- Google Sheets sí tiene XLOOKUP: `XLOOKUP(search_key, lookup_range, result_range, missing_value, match_mode, search_mode)`, con coincidencia exacta por defecto. https://support.google.com/docs/answer/12405947 [S]
- El argumento de compatibilidad a favor de INDEX/MATCH es el que sostiene el debate. No leí el hilo "don't take the bait"; no sé qué argumento concreto defiende. Hueco.

### B3. Power Query y tablas dinámicas vs fórmulas transparentes

Sin fuente leída. Lo único: la doctrina FAST pide fórmulas "simple, clear" y transparentes para modeladores y no modeladores. https://fast-standard.org/the-fast-standard/ [S] Eso es la posición pro-fórmula, no una crítica a Power Query. Hueco completo en la posición contraria (por ejemplo, el costo de reproducibilidad o auditoría de pasos de Power Query).

### B4. FAST vs otros estándares

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| FAST Standard Organisation https://fast-standard.org/the-fast-standard/ | primaria | 3/2/1/3 | [S] |
| ICAEW, Financial Modelling Code (nov. 2018) https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx | primaria | 3/2/2/3 | [M] |

- FAST significa "Flexible, Appropriate, Structured & Transparent"; lo mantiene la FAST Standard Organisation Limited (sociedad sin fines de lucro del Reino Unido, Company No. 07617819); versión 02c, julio de 2019, según el nombre del archivo del enlace. https://fast-standard.org/the-fast-standard/ [S]
- El Código de ICAEW (nov. 2018) "is not intended to be a tick-box compliance tool; rather it is a framework". Construye sobre los "Twenty principles for good spreadsheet practice". Las fuentes los presentan como complementarios, no rivales, según un resumen del buscador. https://www.icaew.com/technical/technology/Excel community/Improve your financial modelling practice [S]
- SMART: no encontré nada. No lo afirmes sin fuente. Es un hueco, y puede que no exista como estándar.

### B5. "Pasá a una base cuando crezcas"

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Resultados del buscador (Retool, Airtable, Softr, Jotform, Basedash, etc.) | secundarias, casi todas de vendedores | 1/1/1/1 | [S] |

- La señal más repetida para mudarse: la planilla pasó de lugar donde se hacen cuentas a lugar donde el negocio guarda su verdad; varias personas editan los mismos registros; se gasta más tiempo manteniéndola que usando los datos. [S]
- Costo de mudarse temprano: un autor dice que una planilla que se entiende es más fácil de limpiar y migrar después que una base armada a las apuradas. Riesgo de migración: muchas fallan tras cargar los datos porque la gente no técnica ya no puede tocarlos y vuelve a la planilla. [S]
- Herramientas intermedias: Airtable (aspecto de planilla, funcionamiento de base) y Notion databases; este último es más lento con miles de registros según una comparación. Precios de Airtable contradictorios entre fuentes (45 USD por usuario al mes en Business en una, 9 y 19 USD en Pro y Business en otra). No uses precios sin verificar en la página oficial. [S]
- Sesgo: casi todo lo que sale en las primeras páginas lo escribe quien vende una de las alternativas. Es la evidencia más débil de este informe. Hueco: ninguna fuente neutral ni estudio empírico.

---

# PARTE 2 — FUNDAMENTOS

## Tema A: Bases de datos

### Historia

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Codd (1970), CACM 13(6) https://courses.cs.washington.edu/courses/cse544/02sp/papers/codd70.pdf | primaria | 3/3/2/3 | [M], solo metadatos y abstract en el buscador. No leí el cuerpo |
| IBM, "The relational database" https://www.ibm.com/history/relational-database | primaria institucional (con interés) | 2/2/1/2 | [S] |
| ANSI blog, SQL standard https://blog.ansi.org/?p=158690 y NIST FIPS 127 https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub127.pdf | secundaria y primaria | 2/1/1/2 | [S] |
| Stonebraker, "Future Trends in Data Base Systems" (1988) https://dsf.berkeley.edu/papers/ERL-M88-07.pdf | primaria | 3/2/1/3 | [S] |

- Codd, E. F., "A Relational Model of Data for Large Shared Data Banks", Communications of the ACM, vol. 13, n.º 6, junio de 1970, desde IBM Research, San José. Los números de página 377-387 no los confirmé; el buscador solo mostró que empieza en la 377. Abstract: introduce "a model based on n-ary relations, a normal form for data base relations, and the concept of a universal data sublanguage"; busca "maximal independence between programs on the one hand and machine representation and organization of data on the other". https://courses.cs.washington.edu/courses/cse544/02sp/papers/codd70.pdf [M]
- System R: "a group of programmers in 1973 undertook an industrial-strength implementation". Chamberlin y Boyce inventaron SQL junto con System R (IBM no menciona SEQUEL en esa página). Oracle (entonces Relational Software) "produced the first commercially available relational database in 1977"; DB2 se entregó en 1983 en MVS. https://www.ibm.com/history/relational-database [S]
- Primer estándar SQL: ANSI X3.135-1986, aprobado el 16 de octubre de 1986 por el comité X3H2; ISO lo adoptó como ISO 9075 en 1987; revisiones en 1989 y 1992 (SQL-86, SQL-89, SQL-92). https://blog.ansi.org/?p=158690 [S] Stonebraker (1988) ya llamaba a SQL "intergalactic standard" y señalaba que ANSI SQL, DB2 y SQL/DS eran versiones algo distintas. https://dsf.berkeley.edu/papers/ERL-M88-07.pdf [S]
- NoSQL: ver A2 (Strozzi 1998, Oskarsson 2009).
- Stonebraker y Pavlo 2005 y 2024: el primero repasa los movimientos de modelado (jerárquico, red, relacional, entidad-relación) desde los 60; el de 2024 cubre 20 años de MapReduce, key-value, documentos, columnas, texto, array, vectores y grafos. https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf [L] parcial

### Escuelas en conflicto
- Relacional vs NoSQL: ver A2. Tesis de Stonebraker-Pavlo: SQL absorbe las buenas ideas de las alternativas. Sesgo declarado en A2.
- SQL primero vs ORM: ver A4.

### Bibliografía de referencia
- Kleppmann, *Designing Data-Intensive Applications*. Sitio del autor: derechos 2014-2019; la ficha no dio edición, editorial ni capítulos (la página enlaza al índice de O'Reilly). https://dataintensive.net/ [M]. Qué leer: no pude verificarlo. Sin lectura propia, no recomiendo capítulos concretos. Hueco: confirmar la 2.ª edición.
- Codd 1970 (arriba), solo para historia; es denso para este lector.
- Stonebraker y Pavlo 2024, introducción y sección de documentos, accesible y con posición clara. https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf
- Documentación de PostgreSQL, capítulo "Transaction Isolation". https://www.postgresql.org/docs/current/transaction-iso.html
- Cursos canónicos de SQL (por ejemplo CMU 15-445, Pavlo): no verificado. Hueco.

### Glosario mínimo (términos que confunden)
Este glosario no tiene fuente verificada; son definiciones estándar mías, para contrastar contra la doc de PostgreSQL antes de publicar.
- Relación (formal) = tabla; tupla = fila = registro; atributo = columna.
- Esquema: la estructura declarada (tablas, columnas, tipos, restricciones). Ojo: en PostgreSQL "schema" también es un espacio de nombres dentro de una base. Dos usos distintos.
- Clave primaria: identifica una fila. Clave foránea: apunta a la clave de otra tabla.
- Índice: estructura auxiliar para encontrar filas rápido. Cuesta escritura (ver Uber en A1).
- Transacción: grupo de operaciones que se aplican juntas o no se aplican. Aislamiento (la I de ACID) tiene niveles, y por defecto en Postgres es Read Committed (ver A5).
- Consulta: pedido de lectura (también se usa para instrucciones que escriben, lo que confunde).

## Tema B: Planillas

### Historia

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Wikipedia, Microsoft Excel https://en.wikipedia.org/wiki/Microsoft_Excel | secundaria | 1/2/1/1 | [S], leí hasta el carácter 100.000 de 180.966 |
| Wikipedia, Google Sheets https://en.wikipedia.org/wiki/Google_Sheets | secundaria | 1/2/1/1 | [S] |
| Computer History Museum, Software Arts y VisiCalc (buscador) https://www.computerhistory.org/revolution/digital-logic/12/287/1231 | secundaria institucional | 2/1/1/1 | [S], no abierto |

- VisiCalc: Software Arts se fundó en 1979 (Bricklin y Frankston); se vendió vía VisiCorp (Dan Fylstra); unos 1 millón de copias vendidas en su vida; desarrollo central en dos meses en el invierno de 1978-79, según un resumen del buscador. https://www.computerhistory.org/collections/catalog/102738286 [S] No pude abrir la página del propio Bricklin (error de certificado en bricklin.com); fuente primaria pendiente. Hueco.
- Lotus 1-2-3: dominante hacia 1983. Excel para Macintosh: anunciado el 2 de mayo de 1985, lanzado el 30 de septiembre de 1985. Excel 2.0 para Windows: lanzado el 19 de noviembre de 1987. https://en.wikipedia.org/wiki/Microsoft_Excel [S]
- Matrices dinámicas: pre-lanzamientos desde 2018; en builds de Office 365 para Insiders hacia marzo de 2020. LAMBDA: 3 de diciembre de 2020. Dato sin fecha de XLOOKUP en esa página. https://en.wikipedia.org/wiki/Microsoft_Excel [S]
- Google Sheets: fecha de lanzamiento 9 de marzo de 2006 en el cuadro; prueba limitada desde el 6 de junio de 2006; beta abierta a todos el 11 de octubre de 2006; renombrado Google Sheets en octubre de 2012; adquirió XL2Web (2Web Technologies) en 2006. https://en.wikipedia.org/wiki/Google_Sheets [S] Discrepancia interna: 9 de marzo vs 6 de junio de 2006 como "lanzamiento"; no resolví cuál cuenta.

### Escuelas en conflicto
- FAST vs Código ICAEW: ver B4. Las fuentes los tratan como complementarios. FAST detalla reglas de construcción; ICAEW da principios. SMART no verificado.

### Bibliografía de referencia
- ICAEW, "Twenty principles for good spreadsheet practice" y Financial Modelling Code. https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx [M]
- Panko 2015, para saber qué se mide de verdad. Leer el abstract y la sección 2. https://arxiv.org/pdf/1602.02601.pdf
- EuSpRIG (arXiv) como archivo de actas. No verifiqué una selección más amplia.
- Libros y cursos canónicos de Excel/Sheets para negocio chico: no investigados. Hueco.

### Glosario mínimo
Sin fuente verificada; definiciones estándar mías.
- Libro (workbook, el archivo) > hoja (sheet) > celda; rango = conjunto de celdas contiguas.
- Referencia: la dirección de una celda (A1). Relativa o absoluta ($A$1). Es la fuente de errores típica al copiar fórmulas.
- Fórmula: lo que empieza con `=`. Función: una pieza con nombre dentro de la fórmula (SUMAR, BUSCARX).
- Tabla dinámica: resumen interactivo que agrupa y cuenta filas sin escribir fórmulas. Distinta de "tabla" de Excel (rango con nombre que crece solo).
- Matriz dinámica: fórmula cuyo resultado se derrama a celdas vecinas; en Excel desde 2018-2020 (ver historia); en Google Sheets existe ARRAYFORMULA, sin verificar.

---

# HUECOS (declarados)

1. Cifra "88 %": sin fuente primaria. Hay un 94 % verificado en Panko 2015 y una explicación secundaria no confirmada (88 planillas en 7 estudios). No resolví 85 vs 88.
2. Desnormalización deliberada (A3): sin fuente propia. No busqué.
3. SQL primero con evidencia empírica (A4): sin fuente. Neward y otras solo como pista.
4. Casos de documentos que sí convienen, con fuente de producción (A2): solo el reconocimiento de Stonebraker-Pavlo.
5. SQLite en producción de terceros (A6): solo fuente del propio proyecto.
6. Power Query y tablas dinámicas vs fórmulas (B3): ninguna fuente. Tampoco hay crítica a Power Query.
7. "Planillas, herramienta de análisis más usada" (B1): sin cifra de fuente.
8. Gene names en Excel (Ziemann 2016): bloqueado por autenticación, sin cifras.
9. Bricklin primario sobre VisiCalc: bricklin.com falló por certificado. Lotus 1-2-3 solo vía Wikipedia.
10. SMART como estándar de modelado: sin resultados. Origen, edición y fecha de FAST solo por la propia organización, 02c de julio de 2019; no verifiqué si hay una edición posterior (hoy es 2026-11-27).
11. Kleppmann: sin edición, editorial ni capítulos confirmados. Cursos canónicos de SQL y de Excel sin investigar.
12. Migración temprana a una base (B5): solo fuentes de vendedores.
13. Del paper de Stonebraker-Pavlo 2024 leí abstract, sección de documentos y resumen de conclusiones. No leí el resto (arquitecturas, nube, NewSQL, vectores).
14. Jepsen sobre PostgreSQL: solo 12.3 (2020) y MongoDB 4.2.6 (2020). No verifiqué si hay análisis posteriores.
15. No leí el cuerpo de Codd 1970; las páginas 377-387 no están confirmadas.
16. Casi toda la Parte 2 tiene marca [S] o [M]; antes de publicar, el glosario de ambos temas y las fechas de planillas conviene contrastarlos con fuente primaria.

Archivos: ninguno escrito en el repo. Texto convertido de PDF en el directorio temporal de la sesión (`/tmp/claude-1000/x/`), no es entregable.
