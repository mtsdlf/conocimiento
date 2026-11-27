---
resumen: >-
  Una transacción agrupa varias operaciones para que la base las aplique todas o ninguna y para
  que las demás sesiones no vean los pasos intermedios. Esta vertical explica qué garantiza una
  transacción, qué ve de las otras según su nivel de aislamiento y cómo se evita que dos clientes
  compren el último producto.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 3.4 Transactions: https://www.postgresql.org/docs/current/tutorial-transactions.html"
  - "PostgreSQL Documentation, 13.2 Transaction Isolation: https://www.postgresql.org/docs/current/transaction-iso.html"
  - "PostgreSQL Documentation, 13.3 Explicit Locking: https://www.postgresql.org/docs/current/explicit-locking.html"
  - "Warszawski y Bailis, ACIDRain: Concurrency-Related Attacks on Database-Backed Web Applications, SIGMOD 2017: https://www.bailis.org/papers/acidrain-sigmod2017.pdf (abstract, introducción y análisis)"
  - "Martin Kleppmann, Designing Data-Intensive Applications (O'Reilly), capítulo Transactions: https://dataintensive.net/ (no se leyó; la edición y los números de capítulo no se verificaron)"
  - "Bases-de-datos/.investigacion/modelos-transacciones-elegir.md, sección 2; Bases-de-datos/.investigacion/modelos-transacciones-elegir-huecos.md, secciones 2 y 3"
aliases: [transacciones, control de concurrencia, transactions, concurrency control]
creado: 2026-11-27
revisado: 2026-11-27
---

# Transacciones

Una transacción agrupa varias operaciones para que la base las aplique todas o ninguna y para
que las demás sesiones no vean los pasos intermedios. Esta vertical explica qué garantiza una
transacción, qué ve de las otras según su nivel de aislamiento y cómo se evita que dos clientes
compren el último producto.

Dentro de [Bases de datos](../bases-de-datos.md), las transacciones son lo que hace que una base
sea más que un lugar donde se guardan filas. Las escrituras que agrupan son las de
[modificar datos](../SQL/modificar-datos.md) (`INSERT`, `UPDATE`, `DELETE`), y las garantías que
dan dependen del motor, por eso son un requisito en los
[criterios de elección](../Elegir-una-base/criterios-de-eleccion.md). Desde el código, la
transacción la abre y la cierra la aplicación o su ORM, como cuenta
[SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md).

## Por qué un pedido necesita una transacción

Confirmar un pedido en un comercio son al menos dos escrituras: insertar el pedido y descontar el
stock. Si la luz se corta entre una y otra, sin transacción queda un pedido sin descuento o un
descuento sin pedido. Con transacción, según la documentación de PostgreSQL, "if an error occurs
that prevents the transaction from completing, then none of the steps affect the database at all".

El segundo problema aparece con más de un usuario. Dos clientes que compran a la vez leen el mismo
stock y los dos creen que queda una unidad. Que la base aplique cada pedido entero no alcanza:
hace falta decidir qué ve cada transacción de lo que escribe la otra, y ahí entran el nivel de
aislamiento y los bloqueos.

## Lo que la transacción no resuelve sola

La creencia más cara del tema es que envolver el código en `BEGIN` y `COMMIT` evita las carreras.
No lo hace. El nivel por defecto de PostgreSQL y de SQL Server es READ COMMITTED, que según la
tabla de PostgreSQL deja pasar lecturas no repetibles, fantasmas y anomalías de serialización. Y
cada motor implementa distinto el mismo nombre de nivel.

ACIDRain (Warszawski y Bailis, 2017) lo midió en 12 aplicaciones de comercio electrónico y
encontró 22 ataques críticos, como corromper el inventario o gastar de más una gift card. De esos,
17 aparecen incluso con el aislamiento más fuerte, porque la aplicación usa mal las
transacciones. La salida para el stock es escribir de forma que la base haga la comprobación (una
actualización condicional o un bloqueo explícito), como explica [concurrencia](concurrencia.md).

## Qué hay adentro de Transacciones

Se leen en este orden: primero qué es una transacción, después qué ve de las otras y al final
cómo se programa para que dos escrituras no se pisen.

- [Transacción](transaccion.md) — las cuatro garantías ACID, `COMMIT`, `ROLLBACK` y los puntos de
  guardado, con lo que cada letra promete y lo que no.
- [Nivel de aislamiento](nivel-de-aislamiento.md) — las cuatro anomalías, los cuatro niveles, el
  nivel por defecto de cada motor y por qué el mismo nombre no garantiza lo mismo.
- [Concurrencia](concurrencia.md) — el caso del último producto: actualización perdida, la
  actualización condicional, el bloqueo pesimista y el optimista, reintentos y deadlocks.

Para entender el tema a fondo, la explicación de referencia para un público general es el capítulo
de transacciones de *Designing Data-Intensive Applications* de Kleppmann (ACID, niveles, write skew
y serializabilidad); la edición y los números de capítulo no se verificaron. La referencia de cómo
se hace en un motor es el capítulo 13 de la documentación de PostgreSQL, en particular la tabla
13.1 y lo que dice de reintentar. Las dos están en
[fuentes de bases de datos](../Fundamentos/fuentes-de-bases-de-datos.md).
