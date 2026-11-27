---
resumen: >-
  Los criterios para elegir una base son siete: el modelo de datos, la consistencia que hace falta,
  cuántos escriben a la vez, la escala, quién la opera, el costo y lo que ya sabe el equipo. Para
  el sistema de un comercio suelen llevar a PostgreSQL, o a SQLite si escribe un solo programa en un
  solo equipo.
estado: borrador
estabilidad: semi
fuentes:
  - "SQLite, Appropriate Uses For SQLite: https://www.sqlite.org/whentouse.html"
  - "SQLite, Isolation In SQLite: https://www.sqlite.org/isolation.html"
  - "Uber Engineering, Evan Klitzke, Why Uber Engineering Switched from Postgres to MySQL, 2016-07-26: https://www.uber.com/en-US/blog/postgres-to-mysql-migration/ (según un resumen)"
  - "EnterpriseDB, Thoughts on Uber's List of Postgres Limitations: https://enterprisedb.com/blog/thoughts-ubers-list-postgres-limitations (según un resumen)"
  - "Andrew Pavlo y otros, Yes, PostgreSQL Has Problems. But We're Sticking With It!, 2023-06-07: https://www.cs.cmu.edu/~pavlo/blog/2023/06/yes-postgresql-has-problems-but-were-sticking-with-it.html (según un resumen; leídos título y encabezados)"
  - "Andrew Pavlo, The Part of PostgreSQL We Hate the Most, 2023-04: https://www.cs.cmu.edu/~pavlo/blog/2023/04/the-part-of-postgresql-we-hate-the-most.html (solo por el buscador)"
  - "Just Use Postgres (Manning), apéndice B When not to use Postgres: https://livebook.manning.com/book/just-use-postgres/appendix-b (según un resumen del buscador)"
  - "Postgres FM, When not to use Postgres: https://postgres.fm/episodes/when-not-to-use-postgres (según un resumen del buscador)"
  - "Stack Overflow Developer Survey 2025, Databases: https://survey.stackoverflow.co/2025/technology#most-popular-technologies-database (según un resumen)"
  - "Jepsen, MySQL 8.0.34, 2023-12-19: https://jepsen.io/analyses/mysql-8.0.34 (según un resumen)"
  - "Bases-de-datos/.investigacion/ (informes del 2026-11-27)"
aliases: [criterios para elegir una base de datos, database selection criteria, PostgreSQL por defecto, cuándo usar SQLite]
creado: 2026-11-27
revisado:
---

# Criterios de elección

Los criterios para elegir una base son siete: el modelo de datos, la consistencia que hace falta,
cuántos escriben a la vez, la escala, quién la opera, el costo y lo que ya sabe el equipo. Para
el sistema de un comercio suelen llevar a PostgreSQL, o a SQLite si escribe un solo programa en un
solo equipo.

Es el componente central de [Elegir una base](elegir-una-base.md). Los criterios no pesan igual:
los dos primeros salen de cómo es el dato y casi nunca cambian; los últimos dependen del momento
del negocio y del equipo.

## Los siete criterios aplicados a un comercio

| Criterio | La pregunta | En el sistema de un comercio |
|---|---|---|
| Modelo | ¿Qué preguntas se le hacen a los datos? | Pedidos, clientes, productos y stock que se cruzan: [relacional](../Modelos-de-datos/base-relacional.md) |
| Consistencia | ¿Qué pasa si dos operaciones se pisan? | El stock no puede quedar negativo: hacen falta [transacciones](../Transacciones/transaccion.md) |
| Concurrencia de escritura | ¿Cuántos escriben a la vez y desde dónde? | Una caja en un local: pocos; una tienda web: muchos usuarios a la vez |
| Escala | ¿Cuántos datos y cuántas consultas por segundo? | Casi siempre poco para cualquier motor; se revisa con cifras reales |
| Operación | ¿Quién la instala, respalda, actualiza y vigila? | Rara vez hay alguien dedicado: pesa la [base administrada](base-administrada.md) |
| Costo | ¿Cuánto sale con el respaldo que hace falta? | El plan gratis puede no traer copias; ver la [ficha](motores-de-bases-de-datos.md) |
| Experiencia del equipo | ¿Qué motor conoce quien la va a usar? | Un motor bien conocido ahorra errores de configuración |

## Consistencia y concurrencia van juntas

La consistencia que hace falta depende de cuántos escriben sobre el mismo dato. Si dos clientes
compran el último producto a la vez, el sistema tiene que vender uno solo. Eso se resuelve con una
escritura condicional o un bloqueo, como explica [concurrencia](../Transacciones/concurrencia.md), y
la base tiene que soportarlo.

Al comparar motores, el nombre de un nivel no alcanza. Según un resumen del análisis de Jepsen sobre
MySQL 8.0.34, "MySQL's Repeatable Read routinely allows G2-item, even on a single healthy node", y
sus transacciones en ese nivel "cannot safely read a value and then write it". El mismo nombre de
nivel en PostgreSQL se comporta distinto. Las diferencias están en
[nivel de aislamiento](../Transacciones/nivel-de-aislamiento.md).

## PostgreSQL por defecto, y para qué cargas falla

El consejo corriente para un sistema nuevo es empezar con PostgreSQL. Lo respaldan su modelo
relacional, su búsqueda de texto y sus extensiones (ver
[modelos especializados](../Modelos-de-datos/modelos-especializados.md)) y su popularidad. Las
críticas existen y son concretas:

- **Uber, 2016.** Según un resumen del artículo, Uber dejó PostgreSQL por la amplificación de
  escritura con muchos índices secundarios, la replicación verbosa entre centros de datos, un bug
  de la versión 9.2 que duplicaba filas en réplicas, la imposibilidad de replicar entre versiones
  mayores y un proceso por conexión que no llegaba a más de unos cientos de conexiones activas.
- **Pavlo, 2023.** Según un resumen de su artículo, Andrew Pavlo, de la Carnegie Mellon, llama a
  PostgreSQL "our favorite DBMS" y aun así lista cuatro problemas: la copia de versiones de las filas, la hinchazón de las tablas,
  el mantenimiento de índices secundarios y la gestión de vacuum. El título resume la posición:
  "Yes, PostgreSQL Has Problems. But We're Sticking With It!".
- **Practicantes.** Según resúmenes del buscador, el apéndice "When not to use Postgres" del libro
  *Just Use Postgres* dice que no es "silver bullet" y que no conviene reemplazar una base que
  funciona solo por estandarizar; Postgres FM sostiene que si el equipo domina otra base, el
  argumento a favor se debilita.

> [!IMPORTANT]
> **Qué carga critican.** EnterpriseDB, que vende servicios de PostgreSQL, sostiene que parte de la
> crítica de Uber no aplica: "replicas certainly allow access to data with full MVCC semantics".
> Las críticas de Uber y de Pavlo apuntan a cargas con muchísimas actualizaciones y borrados, muchos
> índices y replicación entre centros de datos. El sistema de un comercio chico o mediano es lo
> contrario: pocas escrituras por segundo y lecturas que se cruzan. Que por eso la crítica no
> invalida el consejo es una inferencia, no lo dice ninguna fuente leída.

## Cuándo alcanza SQLite

SQLite no es un servidor: es una biblioteca que guarda la base en un archivo del mismo equipo. El
proyecto lo dice así: "SQLite does not compete with client/server databases. SQLite competes with
fopen()." La página de usos apropiados da cifras concretas:

- Tráfico: "Generally speaking, any site that gets fewer than 100K hits/day should work fine with
  SQLite. The 100K hits/day figure is a conservative estimate, not a hard upper bound. SQLite has
  been demonstrated to work with 10 times that amount of traffic."
- El propio sitio de SQLite maneja "about 400K to 500K HTTP requests per day, about 15-20% of which
  are dynamic pages".
- Tamaño: hasta 281 terabytes (2^48 bytes).
- Escritura: "SQLite supports an unlimited number of simultaneous readers, but it will only allow
  one writer at any instant in time." Según la página de aislamiento, implementa transacciones
  serializables "by actually serializing the writes".

La regla del proyecto: si los datos están en un dispositivo local, con poca concurrencia de
escritura y menos de un terabyte, SQLite "is almost always a better solution". Se usa una base
cliente-servidor cuando la base está separada de la aplicación por una red, cuando hay muchos
escritores concurrentes o cuando los datos son muy grandes; "Otherwise → choose SQLite".

Para el comercio, eso significa que la caja de un local, una aplicación de escritorio o un sitio
chico con un solo servidor entran en SQLite. Una tienda web con varios servidores o varias
personas cargando pedidos desde distintos lugares pide PostgreSQL u otra base cliente-servidor.

> [!IMPORTANT]
> Las cifras de SQLite vienen del propio proyecto, que tiene interés en el motor. No hay un caso de
> producción de terceros leído que las confirme.

## La popularidad dice qué se usa, no qué conviene

En la encuesta de Stack Overflow 2025, según un resumen de sus resultados, las bases más usadas por
todos los encuestados y por desarrolladores profesionales fueron PostgreSQL (55,6 % y 58,2 %),
MySQL (40,5 % y 39,6 %), SQLite (37,5 % y 36,9 %), Redis (28 % y 30,7 %) y MongoDB (24 % y 24,3 %).
Es una medida de popularidad: sirve para saber que hay gente, documentación y servicios
administrados para el motor, y que un equipo nuevo probablemente lo conozca. No mide si es la
base correcta para un sistema.

> [!NOTE]
> Sin fuente todavía: una lectura completa de al menos una crítica a PostgreSQL por defecto (el hilo
> de 2019, Postgres FM o el artículo de Uber entero), una fuente sistemática y no de opinión sobre
> cuándo no conviene, un caso de producción de SQLite de terceros, y la edición 2026 de la encuesta
> de Stack Overflow o el ranking de DB-Engines.
