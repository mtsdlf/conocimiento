---
resumen: >-
  Fundamentos reúne lo que cruza todo el tema Bases de datos sin ser una de sus partes: de dónde
  viene el modelo relacional, qué enfoques se disputan el campo, qué ideas repetidas no resisten la
  evidencia, qué leer y el vocabulario.
estado: borrador
estabilidad: estable
fuentes:
  - "E. F. Codd, A Relational Model of Data for Large Shared Data Banks, Communications of the ACM 13(6), junio de 1970: https://courses.cs.washington.edu/courses/cse544/02sp/papers/codd70.pdf (metadatos y abstract; el cuerpo no se leyó)"
  - "IBM, The relational database: https://www.ibm.com/history/relational-database (según resumen)"
  - "ANSI blog, sobre el estándar SQL: https://blog.ansi.org/?p=158690 (según resumen)"
  - "Michael Stonebraker y Andrew Pavlo, What Goes Around Comes Around... And Around..., SIGMOD Record 53(2), junio de 2024, pp. 21-37: https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf (abstract, sección de documentos y conclusiones)"
  - "Wikipedia, NoSQL: https://en.wikipedia.org/wiki/NoSQL (según resumen)"
  - "Martin Fowler, OrmHate (2012-05-08): https://martinfowler.com/bliki/OrmHate.html (según resumen)"
  - "Warszawski y Bailis, ACIDRain, SIGMOD 2017: https://www.bailis.org/papers/acidrain-sigmod2017.pdf (abstract, introducción y análisis)"
  - "PostgreSQL Documentation, 13.2 Transaction Isolation: https://www.postgresql.org/docs/current/transaction-iso.html"
  - "Jepsen, PostgreSQL 12.3 (2020-06-12): https://jepsen.io/analyses/postgresql-12.3 (según resumen)"
  - "Jepsen, MongoDB 4.2.6 (2020-05-15): https://jepsen.io/analyses/mongodb-4.2.6 (según resumen)"
  - "SQLite, Appropriate Uses For SQLite: https://www.sqlite.org/whentouse.html"
  - "Bases-de-datos/.investigacion/posicion-contraria-y-fundamentos.md"
aliases: [fundamentos de bases de datos, historia de las bases de datos, mitos de bases de datos, relacional contra NoSQL, ORM contra SQL]
creado: 2026-11-27
revisado:
---

# Fundamentos de bases de datos

Fundamentos reúne lo que cruza todo el tema Bases de datos sin ser una de sus partes: de dónde
viene el modelo relacional, qué enfoques se disputan el campo, qué ideas repetidas no resisten la
evidencia, qué leer y el vocabulario.

Queda fuera de las partes de [Bases de datos](../bases-de-datos.md) porque sirve para leer con
criterio las notas de todas ellas.

## De Codd a NoSQL

El modelo relacional nació en un paper. E. F. Codd, desde IBM Research en San José, publicó "A
Relational Model of Data for Large Shared Data Banks" en *Communications of the ACM* en junio de
1970. Según su abstract, introduce "a model based on n-ary relations, a normal form for data base
relations, and the concept of a universal data sublanguage", y busca "maximal independence between
programs on the one hand and machine representation and organization of data on the other".  El cuerpo
del paper no se leyó.

De ahí salieron los primeros motores. Según la página de historia de IBM, leída por resumen:

- En 1973, un grupo de IBM "undertook an industrial-strength implementation": System R, junto con el
  cual Chamberlin y Boyce inventaron SQL.
- En 1977, Relational Software, después Oracle, "produced the first commercially available
  relational database".
- En 1983, IBM entregó DB2.

SQL se volvió estándar en 1986. Según el blog de ANSI, también leído por resumen, ANSI aprobó la
norma X3.135-1986 el 16 de octubre de 1986, ISO la adoptó como ISO 9075 en 1987, y hubo revisiones
en 1989 y 1992: SQL-86, SQL-89 y SQL-92. Las ediciones posteriores y qué agrega cada una están en la
[ficha de dialectos de SQL](../SQL/dialectos-de-sql.md).

NoSQL tiene dos nacimientos. Según Wikipedia, Carlo Strozzi usó el término en 1998 para una base
relacional sin SQL, y Johan Oskarsson, de Last.fm, lo revivió en 2009 para un encuentro sobre bases
"open-source distributed, non-relational". El mismo artículo dice en otro lugar que el término
surgió a principios de los 2000; la discrepancia no se resolvió.

Según Stonebraker y Pavlo (2024), "the inability of OLTP RDBMSs to
scale in the 2000s ushered in dozens of document DBMSs" (RDBMS y DBMS son las siglas en inglés de motor relacional
y de motor de base de datos; OLTP, los que atienden las transacciones del día a día), con dos mensajes de venta: "SQL and joins
are slow" y "ACID transactions are unnecessary". Veinte años después, casi todos esos sistemas
sumaron una interfaz SQL y muchos, transacciones ACID.

## Relacional contra NoSQL

> [!IMPORTANT]
> El debate sigue abierto, aunque más chico de lo que fue.
>
> - **Del lado relacional.** Stonebraker y Pavlo (2024) sostienen que SQL absorbe las buenas ideas
>   de cada alternativa. De las bases de documentos dicen que están "on a collision course with
>   RDBMSs"; de las clave-valor, que "can generally be equaled or beaten by modern
>   high-performance RDBMSs"; de las de familia de columnas, que son "a niche market".
> - **Lo que el mismo paper concede a los documentos.** Un documento elimina la distancia entre el
>   objeto de la aplicación y las tablas, y evita el problema N+1. Las objeciones son tres: datos
>   duplicados si la relación no es de uno a muchos, uniones precalculadas que no siempre son más
>   rápidas y pérdida de independencia de los datos. Leído así, el documento conviene cuando el dato
>   es un árbol que se lee entero, como dice [base de documentos](../Modelos-de-datos/base-de-documentos.md).
> - **Sesgo.** Stonebraker fundó empresas de bases relacionales y columnares (Ingres, Vertica,
>   VoltDB; el dato no sale de una fuente leída): es una fuente primaria y autorizada, y también parte interesada. Kleppmann trata el
>   mismo dilema con una mirada más neutral, pero no se leyó.

Cómo elegir entre los dos está en [modelos de datos](../Modelos-de-datos/modelos-de-datos.md).

## ORM contra SQL a mano

> [!IMPORTANT]
> Un ORM traduce objetos del código a filas y genera el SQL. Se discute cuánto conviene.
>
> - **A favor del ORM.** Fowler, en "OrmHate" (2012), leído por resumen: "However much you may hate
>   using an ORM, take my word for it - you're better off", porque un marco que evita el 80% del
>   trabajo repetitivo "is worthwhile even if it is only 80%". Admite que hay que saber SQL igual.
> - **En contra.** El problema N+1, que Stonebraker y Pavlo cuentan entre las razones del auge de
>   los documentos: el ORM dispara una consulta por cada fila en lugar de una sola con un join. Y el
>   estudio "Feral Concurrency Control" (Bailis y otros, SIGMOD 2015), que según el resumen de un
>   buscador trata reglas que los ORM de Rails validan en la aplicación en vez de en la base; el
>   paper no se abrió.

> [!NOTE]
> Sin fuente todavía: una defensa de "SQL primero" con evidencia empírica. "The Vietnam of Computer
> Science" (Ted Neward, 2006) aparece como pista y no se verificó.

Cómo se usa cada camino desde el código, y cómo se evita el N+1, está en
[SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md).

## Ideas que no se sostienen

Cuatro frases que circulan como reglas y que la evidencia disponible no respalda tal cual, cada una
con su evidencia y el sesgo de esa evidencia.

### "NoSQL escala más"

La frase viene del marketing de los 2000, cuando los motores relacionales para transacciones no
escalaban, según Stonebraker y Pavlo (2024). El mismo paper registra que casi todos los NoSQL
terminaron agregando SQL (DynamoDB con PartiQL, Cassandra con CQL, Couchbase con SQL++, MongoDB en
Atlas en 2021) y que las clave-valor pueden ser igualadas o superadas por un relacional moderno. Lo
que decide un modelo es cómo se consultan los datos, no cuántos hay, como dice
[Bases de datos](../bases-de-datos.md#el-modelo-se-elige-por-cómo-se-va-a-consultar).

Jepsen, en su análisis de MongoDB 4.2.6 (2020, leído
por resumen), encontró que no preservaba snapshot isolation ni con los niveles más estrictos (anomalías en
unas 1.461 de 13.914 transacciones); MongoDB lo atribuyó a un error corregido en 4.2.8.

**Sesgo:** la evidencia principal es de Stonebraker, parte interesada del lado relacional. Falta un
caso de producción documentado donde un documento haya sido la mejor opción.

### "El nivel de aislamiento por defecto me protege de las carreras"

No protege. "Read Committed is the default isolation level in PostgreSQL", y según la tabla 13.1 de
su documentación ese nivel permite lecturas no repetibles, fantasmas y anomalías de serialización.
ACIDRain (Warszawski y Bailis, 2017) analizó 12 aplicaciones de comercio electrónico "deployed on
over 2M websites" y verificó 22 ataques críticos que se dan con el aislamiento por defecto de bases
populares. El matiz más útil: 17 de esos 22 aparecen incluso con el aislamiento más fuerte, porque
el problema también es cómo la aplicación usa las transacciones. Jepsen, sobre PostgreSQL 12.3
(2020, por resumen), encontró que ni el nivel Serializable lo era, por un error cuyo parche informó
como programado para la versión menor del 13 de agosto de 2020 (no se verificó que haya salido).

**Sesgo:** ACIDRain estudió aplicaciones autoalojadas buscando ataques, no una muestra al azar de
sistemas. Que la falla sea común es inferencia del tamaño de la muestra, no una medición. La salida
práctica está en [concurrencia](../Transacciones/concurrencia.md).

### "SQLite es de juguete"

El proyecto SQLite dice lo contrario con cifras: "any site that gets fewer than 100K hits/day should
work fine with SQLite", una estimación "conservative" que "has been demonstrated to work with 10
times that amount of traffic". Su propio sitio atiende "about 400K to 500K HTTP requests per day".
El límite de tamaño es de 281 terabytes. Lo que sí limita es la escritura: un solo escritor a la vez,
y la regla del proyecto es pasar a cliente-servidor si la base está separada de la aplicación por
una red, si hay muchos escritores simultáneos o si los datos son muy grandes.

**Sesgo:** la fuente es el propio proyecto. Falta un caso de producción de terceros. Cuándo alcanza
está en los [criterios de elección](../Elegir-una-base/criterios-de-eleccion.md).

### "Hay que normalizar siempre"

> [!NOTE]
> Sin fuente todavía: la posición contraria, la desnormalización deliberada para leer más rápido
> (como en los almacenes analíticos con esquema en estrella), no se buscó.

Lo único leído es la posición a favor de normalizar. Stonebraker y Pavlo (2024) dicen que el
problema de desnormalizar o precalcular uniones "dates back to the 1970s" y le ven tres riesgos:
datos duplicados, que no siempre es más rápido y que se pierde independencia de los datos. Que la
regla tenga excepciones es razonable pero, sin una fuente leída que las documente, queda como hueco.
Cómo se diseñan las tablas está en [base relacional](../Modelos-de-datos/base-relacional.md) y
[definir tablas](../SQL/definir-tablas.md).

## Qué hay en Fundamentos

- [Glosario de bases de datos](glosario-de-bases-de-datos.md) — los términos que confunden (relación,
  fila, los dos esquemas, claves, ACID) y la nota donde vive cada uno.
- [Fuentes de bases de datos](fuentes-de-bases-de-datos.md) — qué leer, qué parte y en qué fijarse.
- [Ruta de SQL](ruta-de-sql.md) — ejercicios en orden para aprender SQL desde cero.

## Qué falta en Fundamentos

La historia se apoya en resúmenes y abstracts. Faltan la desnormalización deliberada, una defensa
de SQL primero con datos, casos de terceros con documentos y con SQLite, y análisis de Jepsen
posteriores a 2020 sobre PostgreSQL y MongoDB.
