---
resumen: >-
  Concurrencia es lo que pasa cuando dos transacciones leen y escriben los mismos datos a la vez,
  como dos clientes que compran el último producto. Se resuelve haciendo que la base compruebe la
  condición al escribir: con una actualización condicional, con un bloqueo pesimista o con un
  bloqueo optimista por versión, y reintentando cuando la base aborta.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 13.2 Transaction Isolation (13.2.1 y 13.2.2): https://www.postgresql.org/docs/current/transaction-iso.html"
  - "PostgreSQL Documentation, UPDATE (Outputs): https://www.postgresql.org/docs/current/sql-update.html"
  - "PostgreSQL Documentation, 13.3 Explicit Locking: https://www.postgresql.org/docs/current/explicit-locking.html"
  - "Martin Fowler, Patterns of Enterprise Application Architecture, Optimistic Offline Lock: https://martinfowler.com/eaaCatalog/optimisticOfflineLock.html"
  - "Ruby on Rails API, ActiveRecord::Locking::Optimistic: https://api.rubyonrails.org/classes/ActiveRecord/Locking/Optimistic.html"
  - "Warszawski y Bailis, ACIDRain: Concurrency-Related Attacks on Database-Backed Web Applications, SIGMOD 2017: https://www.bailis.org/papers/acidrain-sigmod2017.pdf (abstract, introducción y análisis)"
  - "Jepsen, MySQL 8.0.34 (2023-12-19): https://jepsen.io/analyses/mysql-8.0.34 (según resumen)"
  - "Bases-de-datos/.investigacion/modelos-transacciones-elegir.md, sección 2; Bases-de-datos/.investigacion/modelos-transacciones-elegir-huecos.md, secciones 2 y 3"
aliases: [concurrencia, control de concurrencia, actualización perdida, lost update, condición de carrera, race condition, bloqueo pesimista, bloqueo optimista, SELECT FOR UPDATE, optimistic locking, pessimistic locking, deadlock, interbloqueo, sobreventa]
creado: 2026-11-27
revisado: 2026-11-27
---

# Concurrencia

Concurrencia es lo que pasa cuando dos transacciones leen y escriben los mismos datos a la vez,
como dos clientes que compran el último producto. Se resuelve haciendo que la base compruebe la
condición al escribir: con una actualización condicional, con un bloqueo pesimista o con un
bloqueo optimista por versión, y reintentando cuando la base aborta.

Es la parte práctica de [Transacciones](transacciones.md): una [transacción](transaccion.md) sola
no evita estas carreras, y el [nivel de aislamiento](nivel-de-aislamiento.md) por defecto tampoco.

## Dos clientes y el último producto

La tabla `productos` tiene el producto 7 con `stock = 1`. Dos clientes aprietan "comprar" al mismo
tiempo y la aplicación hace, para cada uno, lo más natural:

```sql
SELECT stock FROM productos WHERE id = 7;     -- las dos sesiones leen 1
-- la aplicación ve que 1 > 0 y sigue
UPDATE productos SET stock = 0 WHERE id = 7;  -- las dos escriben 0
```

Las dos sesiones leyeron 1, las dos decidieron vender y las dos escribieron 0. Se vendieron dos
unidades de un producto que tenía una. Esto es una actualización perdida (lost update): la segunda
escritura pisa a la primera, que se calculó sobre un dato que ya no valía. Si en vez de `stock = 0`
la aplicación escribe `stock = stock - 1` sin condición, el resultado es −1: la base resta bien,
pero nadie le pidió que comprobara que quedaba stock.

El problema es el hueco entre leer y escribir: si la decisión se toma en el código de la
aplicación, la base no sabe que esa escritura dependía de esa lectura.

## La actualización condicional: que la base decida

La salida más simple es pasar la condición al `WHERE` y mirar cuántas filas cambió:

```sql
UPDATE productos
SET stock = stock - 1
WHERE id = 7 AND stock > 0
RETURNING stock;
```

Si la sentencia afectó una fila, la venta se hizo; si afectó cero, no quedaba stock y la aplicación
tiene que avisarle al cliente y deshacer el pedido. No hace falta el `SELECT` previo. PostgreSQL
responde con una etiqueta de la forma `UPDATE count`, y la aplicación tiene que leer ese número:
ignorarlo vuelve a abrir el agujero. La misma sentencia, con el `CHECK (stock >= 0)` como red de
seguridad, está en [modificar datos](../SQL/modificar-datos.md#descontar-stock-sin-vender-lo-que-no-hay).

Por qué esto es seguro en PostgreSQL con el nivel por defecto lo explica su documentación de Read
Committed. Cuando una sesión quiere actualizar una fila que otra está actualizando, "the would-be
updater will wait for the first updating transaction to commit or roll back". Si la primera
confirma, la segunda "will attempt to apply its operation to the updated version of the row. The
search condition of the command (the `WHERE` clause) is re-evaluated to see if the updated version
of the row still matches". En el caso del último producto, la segunda sesión espera, vuelve a
evaluar `stock > 0` contra el stock ya en 0 y no actualiza nada.

Que esto resuelva el caso del stock es una inferencia de ese mecanismo: la documentación de
PostgreSQL usa como ejemplo transferencias entre cuentas, no stock. En otros motores el mecanismo
puede ser distinto y no se verificó; antes de confiar en la actualización condicional en MySQL o
SQL Server, conviene leer cómo sus `UPDATE` encuentran y bloquean las filas.

Un `CHECK (stock >= 0)` en la tabla, como se declara en [definir tablas](../SQL/definir-tablas.md),
es una red de seguridad complementaria: si algún camino del código se olvida la condición, la base
rechaza el −1 en lugar de guardarlo.

## El bloqueo pesimista: SELECT ... FOR UPDATE

Cuando la decisión no cabe en un `WHERE` (hay que calcular un precio, consultar un cupón, llamar a
otro servicio), la salida es bloquear la fila al leerla:

```sql
BEGIN;
SELECT stock FROM productos WHERE id = 7 FOR UPDATE;
-- la aplicación decide con el stock leído; nadie más puede cambiarlo
UPDATE productos SET stock = stock - 1 WHERE id = 7;
COMMIT;
```

Según la documentación de PostgreSQL, "FOR UPDATE causes the rows retrieved by the SELECT statement
to be locked as though for update. This prevents them from being locked, modified or deleted by
other transactions until the current transaction ends." La segunda sesión se queda esperando en su
`SELECT ... FOR UPDATE` hasta que la primera confirma, y entonces lee el stock ya en 0. Los
bloqueos de fila "block only writers and lockers to the same row": quien solo lee sin `FOR UPDATE`
no espera.

El costo es la espera: mientras la transacción está abierta, las compras de ese producto hacen
fila. Por eso tiene que ser corta, sin esperar a un medio de pago con la fila bloqueada.

## El bloqueo optimista: una columna de versión

El bloqueo optimista no bloquea nada al leer: detecta el conflicto al escribir. Fowler lo describe
como un patrón que "prevents conflicts between concurrent business transactions by detecting a
conflict and rolling back the transaction", y que conviene cuando "the chance of conflict is low";
si es alta, remite al bloqueo pesimista.

La forma común es una columna de versión que se incrementa en cada escritura:

```sql
-- al leer, la aplicación guarda la versión
SELECT stock, version FROM productos WHERE id = 7;   -- stock 1, version 15

-- al escribir, exige que la versión no haya cambiado
UPDATE productos
SET stock = 0, version = version + 1
WHERE id = 7 AND version = 15;
```

Si la sentencia afectó cero filas, otra sesión escribió en el medio y la aplicación tiene que volver
a leer y decidir de nuevo, o avisarle al usuario. Este SQL no figura literal en las fuentes leídas:
es el mecanismo común que describen. Rails lo trae armado: "Active Record supports optimistic
locking if the `lock_version` field is present", "each update to the record increments the integer
column `lock_version`", y si dos usuarios editan el mismo registro, el segundo recibe un
`ActiveRecord::StaleObjectError` y "the update is ignored". Otros ORM tienen lo mismo con otro
nombre; cómo se usa desde el código está en [SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md).

Por inferencia propia, sirve cuando entre leer y escribir pasan minutos, como en un formulario de
edición: ninguna fuente leída lo dice así.

## Cuál de las tres conviene

| Salida | Cuándo conviene | Qué cuesta | Qué tiene que hacer la aplicación |
|---|---|---|---|
| Actualización condicional | La regla cabe en un `WHERE` (stock, saldo, cupos) | Casi nada | Leer las filas afectadas y actuar si son cero |
| Bloqueo pesimista (`FOR UPDATE`) | La decisión necesita lógica entre leer y escribir, y hay conflictos seguido | Esperas; riesgo de deadlock | Mantener la transacción corta |
| Bloqueo optimista (versión) | Los conflictos son raros o entre leer y escribir pasa mucho tiempo (inferencia propia) | Una columna; escrituras rechazadas | Reintentar o avisar cuando la versión no coincide |

Para el stock, la actualización condicional suele alcanzar y es la que menos puede salir mal: es
una recomendación de esta base, apoyada en el mecanismo de PostgreSQL, no de una fuente.

## Reintentar ante una falla de serialización

Si se sube el nivel a Repeatable Read o Serializable, la base aborta las transacciones que chocan.
En PostgreSQL, si una transacción Repeatable Read quiere actualizar una fila que otra cambió y
confirmó, falla con "ERROR: could not serialize access due to concurrent update". La documentación
es explícita: las aplicaciones "must be prepared to retry transactions due to serialization
failures", que "always return with an SQLSTATE value of '40001'".

El reintento es de la transacción entera, desde el `BEGIN`: la aplicación "should abort the current
transaction and retry the whole transaction from the beginning". Repetir solo la sentencia que
falló no sirve, porque las decisiones anteriores se tomaron con datos viejos. Según la misma
página, "only updating transactions might need to be retried; read-only transactions will never
have serialization conflicts". Los pasos:

1. Envolvé toda la operación (lecturas, decisiones y escrituras) en una función que empiece con
   `BEGIN` y termine con `COMMIT`.
2. Si la base devuelve SQLSTATE `40001`, hacé `ROLLBACK` y volvé a llamar a la función.
3. Poné un límite de intentos y, al pasarlo, devolvé un error al usuario.
4. No mandes nada afuera (correos, cobros) hasta después del `COMMIT`: un intento abortado no debe
   dejar efectos.

Reintentar la transacción en la base es distinto de que el cliente reintente el pedido entero
contra el servidor; para eso existe la [clave de idempotencia](../../Arquitectura/clave-de-idempotencia.md).

## Deadlocks y el orden de los bloqueos

Un deadlock pasa cuando dos transacciones se esperan mutuamente. Un pedido con los productos 3 y 7
bloquea primero el 3; otro, con los mismos productos, bloquea primero el 7; cada uno espera la fila
que tiene el otro. PostgreSQL los detecta y aborta una de las dos transacciones, que la aplicación
puede reintentar.

La documentación da la defensa: "The best defense against deadlocks is generally to avoid them by
being certain that all applications ... acquire locks on multiple objects in a consistent order."
En el comercio, eso es bloquear los productos de un pedido siempre en el mismo orden, por ejemplo
de menor a mayor `id`. Una inferencia de la misma regla: como el `UPDATE` también bloquea la fila,
la actualización condicional de varios productos conviene hacerla en ese mismo orden.

## Lo que mostró ACIDRain

ACIDRain (Warszawski y Bailis, SIGMOD 2017) es el estudio que muestra que esto no es teoría. Sus
autores analizaron 12 aplicaciones de comercio electrónico autoalojadas, "deployed on over 2M
websites", y verificaron 22 ataques críticos: corromper el inventario, gastar de más una gift card,
robar inventario. Parten de que "in practice, database transactions frequently execute under weak
isolation that exposes programs to a range of concurrency anomalies".

Las 22 vulnerabilidades se manifiestan con el aislamiento por defecto de bases populares, Oracle 12c
incluida. Y 17 de ellas aparecen incluso con el aislamiento más fuerte; el paper lo atribuye al uso
incorrecto de las transacciones. Una inferencia propia de cómo es ese uso incorrecto: subir el
nivel no alcanza si la lectura y la escritura no están en la misma transacción o si la condición
no llega a la base.

El mismo paper señala que el Repeatable Read de MySQL no impide la actualización perdida salvo con
`FOR UPDATE`; las diferencias entre motores están en
[nivel de aislamiento](nivel-de-aislamiento.md#el-mismo-nombre-no-garantiza-lo-mismo).
