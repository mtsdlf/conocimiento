---
resumen: >-
  El nivel de aislamiento decide qué ve una transacción de lo que escriben las otras al mismo
  tiempo. El estándar SQL define cuatro niveles según qué anomalías permiten, pero cada motor
  tiene otro nivel por defecto y el mismo nombre se comporta distinto según el motor.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 13.2 Transaction Isolation (tabla 13.1 y definiciones de las anomalías): https://www.postgresql.org/docs/current/transaction-iso.html"
  - "PostgreSQL Documentation, 13.1 Introduction (MVCC): https://www.postgresql.org/docs/current/mvcc-intro.html"
  - "MySQL 8.4 Reference Manual, Transaction Isolation Levels: https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html"
  - "Microsoft Learn, SET TRANSACTION ISOLATION LEVEL (Transact-SQL), actualizada 2026-11-02: https://learn.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql"
  - "SQLite, Isolation In SQLite: https://www.sqlite.org/isolation.html"
  - "Berenson, Bernstein, Gray, Melton, O'Neil y O'Neil, A Critique of ANSI SQL Isolation Levels, SIGMOD 1995: https://arxiv.org/abs/cs/0701157 (solo el abstract)"
  - "Jepsen, PostgreSQL 12.3 (2020-06-12): https://jepsen.io/analyses/postgresql-12.3 (según el resumen del abstract)"
  - "Jepsen, MySQL 8.0.34 (Alvaro y Kingsbury, 2023-12-19): https://jepsen.io/analyses/mysql-8.0.34 (según resumen)"
  - "Bases-de-datos/.investigacion/modelos-transacciones-elegir.md, sección 2; Bases-de-datos/.investigacion/modelos-transacciones-elegir-huecos.md, sección 3"
aliases: [nivel de aislamiento, aislamiento, isolation level, transaction isolation, read committed, repeatable read, serializable, snapshot isolation, lectura sucia, lectura fantasma, write skew]
creado: 2026-11-27
revisado: 2026-11-27
---

# Nivel de aislamiento

El nivel de aislamiento decide qué ve una transacción de lo que escriben las otras al mismo
tiempo. El estándar SQL define cuatro niveles según qué anomalías permiten, pero cada motor
tiene otro nivel por defecto y el mismo nombre se comporta distinto según el motor.

Es la I de ACID que presenta [transacción](transaccion.md). Aislar del todo saldría caro: si cada
transacción esperara a que terminen las demás, un comercio con muchos clientes atendería de a uno.
Los niveles son un trato entre velocidad y anomalías permitidas, y el caso práctico de ese trato
(el último producto) está en [concurrencia](concurrencia.md).

## Las cuatro anomalías, con las palabras de PostgreSQL

La documentación de PostgreSQL define cuatro fenómenos que un nivel puede permitir o impedir. Las
definiciones van literales, con un ejemplo de comercio al lado.

| Anomalía | Definición de PostgreSQL | En un comercio |
|---|---|---|
| Lectura sucia (dirty read) | "A transaction reads data written by a concurrent uncommitted transaction." | Un informe muestra un pedido que después se canceló con ROLLBACK |
| Lectura no repetible (nonrepeatable read) | "A transaction re-reads data it has previously read and finds that data has been modified by another transaction (that committed since the initial read)." | La transacción lee el stock en 1, lo vuelve a leer y ya es 0 |
| Lectura fantasma (phantom read) | "A transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction." | Cuenta los pedidos de hoy dos veces y la segunda aparece uno nuevo |
| Anomalía de serialización | "The result of successfully committing a group of transactions is inconsistent with all possible orderings of running those transactions one at a time." | Dos transacciones, cada una correcta sola, dejan juntas un estado imposible |

La última es la más difícil de ver. La documentación de PostgreSQL trae un ejemplo sin ponerle
nombre; Jepsen y Kleppmann lo llaman write skew: dos transacciones leen lo mismo, cada una escribe
una fila distinta y ninguna ve la escritura de la otra. Ninguna fila se
pisó, pero la regla que las dos comprobaron dejó de cumplirse.

## Qué permite cada nivel en PostgreSQL

La tabla 13.1 de la documentación de PostgreSQL, tal cual:

| Nivel | Lectura sucia | No repetible | Fantasma | Anomalía de serialización |
|---|---|---|---|---|
| Read uncommitted | Allowed, but not in PG | Possible | Possible | Possible |
| Read committed | Not possible | Possible | Possible | Possible |
| Repeatable read | Not possible | Not possible | Allowed, but not in PG | Possible |
| Serializable | Not possible | Not possible | Not possible | Not possible |

Las celdas "but not in PG" son donde PostgreSQL da más que el mínimo del estándar. Se pueden pedir
los cuatro niveles, pero "internally only three distinct isolation levels are implemented, i.e.,
PostgreSQL's Read Uncommitted mode behaves like Read Committed". Y "Read Committed is the default
isolation level in PostgreSQL".

PostgreSQL implementa esto con versiones de las filas (MVCC): cada sentencia ve "a snapshot of data
(a database version) as it was some time ago", y por eso "reading never blocks writing and writing
never blocks reading". En Read Committed la foto se toma en cada sentencia; en Repeatable Read, una
sola vez para toda la transacción.

El nivel se cambia por transacción:

```sql
BEGIN ISOLATION LEVEL SERIALIZABLE;
SELECT stock FROM productos WHERE id = 7;
UPDATE productos SET stock = stock - 1 WHERE id = 7;
COMMIT;
```

Subir el nivel tiene un costo: en Repeatable Read y Serializable la base aborta transacciones con
un error de serialización, y la aplicación "must be prepared to retry transactions due to
serialization failures". Cómo se reintenta está en
[concurrencia](concurrencia.md#reintentar-ante-una-falla-de-serialización).

## El nivel por defecto cambia de un motor a otro

Cada motor arranca en un nivel distinto, según su propia documentación.

| Motor | Nivel por defecto | Cita de la documentación |
|---|---|---|
| PostgreSQL | READ COMMITTED | "Read Committed is the default isolation level in PostgreSQL." |
| MySQL (InnoDB) | REPEATABLE READ | "The default isolation level for InnoDB is REPEATABLE READ." |
| SQL Server | READ COMMITTED, con bloqueos compartidos | "This option is the SQL Server default." |
| Azure SQL Database | READ COMMITTED con versionado de filas | "`READ_COMMITTED_SNAPSHOT` `ON` is the default on Azure SQL Database" |
| SQLite | SERIALIZABLE | "all transactions in SQLite show 'serializable' isolation" |

SQL Server y Azure SQL comparten nombre de nivel y no comparten mecanismo. Con
`READ_COMMITTED_SNAPSHOT` apagado, como viene en SQL Server, Read Committed usa bloqueos
compartidos; encendido, como viene en Azure SQL, cada sentencia lee "a transactionally consistent
snapshot of the data as it existed at the start of the statement". Una inferencia de ese
mecanismo: un sistema que pasa de uno a otro puede ver otra concurrencia sin cambiar una línea de
SQL.

SQLite llega a serializable por el camino más simple: "SQLite implements serializable transactions
by actually serializing the writes. There can only be a single writer at a time." En modo WAL un
lector ve una foto fija, y si después intenta escribir con una foto vieja falla con
`SQLITE_BUSY_SNAPSHOT`; la documentación indica empezar con `BEGIN IMMEDIATE` para evitarlo.

## El mismo nombre no garantiza lo mismo

> [!IMPORTANT]
> Repeatable Read significa cosas distintas en PostgreSQL y en MySQL, y ninguno coincide del todo
> con la lectura más común del estándar.
>
> - **PostgreSQL.** Su Repeatable Read ya impide los fantasmas, que el estándar permitiría, pero
>   deja pasar anomalías de serialización. Jepsen, en su análisis de PostgreSQL 12.3 (2020), lo
>   resume así: "PostgreSQL 'repeatable read' is actually snapshot isolation" (aislamiento por
>   instantánea: la transacción lee una foto fija y solo choca si escribe una fila que otra ya
>   escribió). Si dos
>   transacciones actualizan la misma fila, PostgreSQL aborta a la segunda con "could not
>   serialize access due to concurrent update", así que no hay actualización perdida; el write
>   skew, en cambio, pasa.
> - **MySQL.** Según su documentación, en Repeatable Read "consistent reads within the same
>   transaction read the snapshot established by the first read" y bloquea rangos con gap locks y
>   next-key locks (bloqueos sobre el hueco entre filas de un índice, para que otra transacción no
>   inserte ahí). Jepsen, en su análisis de MySQL 8.0.34 (2023), encontró que "MySQL's Repeatable
>   Read routinely allows G2-item, even on a single healthy node" (G2-item es el nombre que usa Jepsen
>   para una anomalía de la familia del write skew) y que "MySQL Repeatable Read
>   transactions cannot safely read a value and then write it": permite la actualización perdida.
>   ACIDRain (2017) ya había señalado que el Repeatable Read de MySQL no impide la actualización
>   perdida salvo con `FOR UPDATE`. Jepsen cita además una nota de la propia documentación de MySQL
>   según la cual los cambios de otras transacciones pueden volverse visibles.
> - **Serializable tampoco es un absoluto.** El mismo análisis de PostgreSQL 12.3 encontró que
>   "transactions executed with serializable isolation on a single PostgreSQL instance were not, in
>   fact, serializable", por un error en la detección de conflictos. Jepsen informó el parche como
>   programado para la versión menor del 13 de agosto de 2020; que esa versión haya salido con el
>   arreglo no se verificó.
> - **Las pruebas no prueban la ausencia de errores.** En el análisis de MySQL 8.0.34, Jepsen aclara
>   que sus pruebas muestran que hay errores, no que no los haya.
>
> Los dos análisis de Jepsen se leyeron por su resumen, no enteros.

El origen de este desorden está en el estándar. Berenson, Bernstein, Gray y otros lo plantearon en
1995, en "A Critique of ANSI SQL Isolation Levels": según su abstract, "these phenomena and the
ANSI SQL definitions fail to characterize several popular isolation levels". El paper propone
fenómenos nuevos y define snapshot isolation. Solo se leyó el abstract; la lista completa de
fenómenos que propone no se verificó.

La consecuencia práctica es leer la página de aislamiento del motor que se usa, no la del estándar,
y no suponer que un sistema que andaba bien en PostgreSQL va a andar igual en MySQL. Para el stock
y los saldos, lo seguro es no depender del nivel: escribir de forma que la base haga la
comprobación, como muestra [concurrencia](concurrencia.md).

## Qué leer de cada motor

La referencia es la sección 13.2 de la documentación de PostgreSQL: conviene leer la tabla 13.1 y
los párrafos de Read Committed sobre qué pasa cuando dos sesiones actualizan la misma fila. Para
otro motor, la página de aislamiento de ese motor (las de MySQL, SQL Server y SQLite están en las
fuentes). Para ver cómo fallan en la práctica, el abstract y la sección de Repeatable Read del
análisis de Jepsen sobre MySQL 8.0.34.
