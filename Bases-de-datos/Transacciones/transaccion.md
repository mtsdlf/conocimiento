---
resumen: >-
  Una transacción es un grupo de operaciones que la base trata como una sola: o se aplican todas
  (COMMIT) o no se aplica ninguna (ROLLBACK), y las otras sesiones no ven los pasos intermedios.
  Las cuatro propiedades ACID dicen qué promete y cada una tiene un límite que conviene conocer.
estado: borrador
estabilidad: estable
fuentes:
  - "PostgreSQL Documentation, 3.4 Transactions: https://www.postgresql.org/docs/current/tutorial-transactions.html"
  - "PostgreSQL Documentation, Appendix M. Glossary (ACID, Atomicity, Consistency, Isolation, Durability, Transaction, Commit, Rollback, Savepoint): https://www.postgresql.org/docs/current/glossary.html"
  - "PostgreSQL Documentation, 13.2 Transaction Isolation: https://www.postgresql.org/docs/current/transaction-iso.html"
  - "PostgreSQL Documentation, 5.5 Constraints: https://www.postgresql.org/docs/current/ddl-constraints.html"
  - "Warszawski y Bailis, ACIDRain, SIGMOD 2017: https://www.bailis.org/papers/acidrain-sigmod2017.pdf (abstract, introducción y análisis)"
  - "Bases-de-datos/.investigacion/modelos-transacciones-elegir.md, sección 2"
aliases: [transacción, transaction, ACID, commit, rollback, savepoint, punto de guardado, atomicidad, durabilidad]
creado: 2026-11-27
revisado:
---

# Transacción

Una transacción es un grupo de operaciones que la base trata como una sola: o se aplican todas
(COMMIT) o no se aplica ninguna (ROLLBACK), y las otras sesiones no ven los pasos intermedios.
Las cuatro propiedades ACID dicen qué promete y cada una tiene un límite que conviene conocer.

La documentación de PostgreSQL lo resume así: "The essential point of a transaction is that it
bundles multiple steps into a single, all-or-nothing operation". Es la pieza base de la vertical
[Transacciones](transacciones.md); qué ve una transacción de las demás está en
[nivel de aislamiento](nivel-de-aislamiento.md), y cómo se usa para que dos escrituras no se pisen,
en [concurrencia](concurrencia.md).

## Un pedido con BEGIN, COMMIT y ROLLBACK

En PostgreSQL una transacción se arma rodeando las sentencias con `BEGIN` y `COMMIT`. Con las
tablas de [definir tablas](../SQL/definir-tablas.md), confirmar un pedido de Bruno (cliente 2) por
un Mate (producto 2) queda así:

```sql
BEGIN;
INSERT INTO pedidos (cliente_id) VALUES (2) RETURNING id;   -- devuelve el id nuevo: 5
INSERT INTO items_pedido (pedido_id, producto_id, cantidad, precio_unitario)
  VALUES (5, 2, 1, 12000);                                  -- el Mate, al precio de hoy
UPDATE productos SET stock = stock - 1 WHERE id = 2;
COMMIT;
```

El id del pedido lo genera la base (`GENERATED ALWAYS AS IDENTITY`), así que no se escribe:
`RETURNING` lo devuelve y la aplicación lo usa en el ítem. Con los datos iniciales de la
[ruta de SQL](../Fundamentos/ruta-de-sql.md) sale el 5; se comprobó al ejecutarlo en PostgreSQL
18.4. El `UPDATE` de este ejemplo descuenta sin mirar si queda stock; cómo descontar sin vender lo
que no hay está en [concurrencia](concurrencia.md).

Si a mitad de camino la aplicación decide no seguir (el cliente canceló, el pago falló), manda
`ROLLBACK` en lugar de `COMMIT` y "all our updates so far will be canceled". Si una sentencia da
error, la transacción no termina sola: según la documentación, "goes into an aborted state" y
rechaza todo salvo `COMMIT` y `ROLLBACK`.

Aunque no se escriba `BEGIN`, hay transacción. PostgreSQL "actually treats every SQL statement as
being executed within a transaction": cada sentencia suelta lleva un `BEGIN` y un `COMMIT`
implícitos. Por eso dos sentencias sueltas seguidas son dos transacciones, y un corte entre ellas
deja aplicada solo la primera.

Un punto de guardado (`SAVEPOINT`) marca un lugar dentro de la transacción al que se puede volver
con `ROLLBACK TO` sin descartar lo anterior. Sirve, por ejemplo, para intentar aplicar un cupón y,
si falla, seguir con el pedido sin él.

## Qué promete cada letra de ACID y qué no

ACID son las iniciales de cuatro propiedades que, según el glosario de PostgreSQL, buscan
"guarantee validity in concurrent operation and even in event of errors, power failures, etc."
Cada una promete algo más chico de lo que el nombre sugiere.

| Letra | Qué promete (glosario de PostgreSQL) | Qué no promete |
|---|---|---|
| Atomicidad | "either all its operations complete as a single unit or none do", y tras una caída "no partial results are visible after recovery" | Que el resultado sea el que la aplicación quería: un pedido entero mal calculado se guarda entero |
| Consistencia | Que los datos cumplen las restricciones de integridad; si al hacer COMMIT alguna no se cumple, la transacción "is automatically rolled back" | Que se cumplan reglas que la base no conoce: si `stock` no tiene un `CHECK (stock >= 0)`, la base deja guardar −1 |
| Aislamiento | "the effects of a transaction are not visible to concurrent transactions before it commits" | Que dos transacciones no se pisen: lo que ve cada una de las ya confirmadas depende del [nivel de aislamiento](nivel-de-aislamiento.md) |
| Durabilidad | "once a transaction has been committed, the changes remain even after a system failure or crash" | Que los datos sobrevivan a perder el disco: eso es respaldo y réplica, requisitos al [elegir una base administrada](../Elegir-una-base/base-administrada.md) |

La C es la única letra que depende de quien diseña las tablas. Las reglas que la base hace cumplir
son las que se declaran con `NOT NULL`, `UNIQUE`, claves foráneas y `CHECK`, como explica
[definir tablas](../SQL/definir-tablas.md). Un detalle de la documentación de restricciones: "a
check constraint is satisfied if the check expression evaluates to true or the null value", así
que un `CHECK` sin `NOT NULL` deja pasar valores vacíos.

La I es la que más se malinterpreta. El glosario define transacción como un grupo de comandos cuyos
efectos "are not visible to other sessions until the transaction is complete, and possibly even
later, depending on the isolation level". Lo que no dice es que una transacción no vea lo que otra
confirmó mientras ella estaba abierta: en el nivel por defecto de PostgreSQL, READ COMMITTED, cada
sentencia ve los datos confirmados hasta ese momento.

## Cómo falla una transacción mal usada

Las fallas más comunes no son de la base sino de dónde la aplicación pone los límites de la
transacción. Tres formas típicas:

- **Leer en una transacción y escribir en otra.** La aplicación consulta el stock, decide en su
  código y después manda el `UPDATE`. Entre la lectura y la escritura otra sesión pudo cambiar el
  dato; es la actualización perdida que trata [concurrencia](concurrencia.md).
- **Operaciones que deberían ir juntas en transacciones separadas.** Sin `BEGIN`, cada sentencia se
  confirma sola, y un error a mitad de camino deja datos a medias.
- **Confiar en el nivel por defecto.** ACIDRain (Warszawski y Bailis, 2017) encontró 22 ataques
  en 12 aplicaciones de comercio electrónico; 17 se dan incluso con el aislamiento más fuerte, por
  uso incorrecto de las transacciones.

Una transacción también falla a propósito: en niveles altos de aislamiento la base puede abortarla
con un error de serialización, y la aplicación tiene que reintentarla entera. Cómo se hace está en
[concurrencia](concurrencia.md#reintentar-ante-una-falla-de-serialización).

La versión corta y oficial es la sección 3.4 del tutorial de PostgreSQL, con un ejemplo de
transferencia entre cuentas: conviene leerla entera y fijarse en la parte de puntos de guardado.
