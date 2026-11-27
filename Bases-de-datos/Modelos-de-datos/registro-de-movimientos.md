---
resumen: >-
  Un registro de movimientos guarda cada cambio de una cantidad (una compra, una venta, una
  devolución, un ajuste) como una fila que no se edita, y calcula el saldo sumando esas filas. Es la
  manera de llevar el stock, una cuenta corriente o cualquier saldo sin perder de dónde salió cada
  número.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, Event Sourcing (2005): https://martinfowler.com/eaaDev/EventSourcing.html"
  - "OpenStax, Principles of Financial Accounting, 6.2 Compare and Contrast Perpetual versus Periodic Inventory Systems: https://openstax.org/books/principles-financial-accounting/pages/6-2-compare-and-contrast-perpetual-versus-periodic-inventory-systems"
  - "PostgreSQL Documentation, Materialized Views: https://www.postgresql.org/docs/current/rules-materializedviews.html"
  - "Martin Kleppmann, Using logs to build a solid data infrastructure (2015): https://martin.kleppmann.com/2015/05/27/logs-for-data-infrastructure.html"
  - "Odoo 19, Count products: https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products.html"
  - "ERPNext, Stock Ledger: https://docs.frappe.io/erpnext/user/manual/en/stock-ledger"
  - "Greg Young citado por InfoQ (2016-04-26): https://www.infoq.com/news/2016/04/event-sourcing-anti-pattern"
  - "Chris Kiehl, Event Sourcing is Hard (2019): https://chriskiehl.com/article/event-sourcing-is-hard"
  - "Bases-de-datos/.investigacion/llevar-el-stock.md (2026-11-27)"
aliases: [movimientos de stock, libro de movimientos, ledger, stock ledger, kardex, inventario permanente, saldo calculado]
creado: 2026-11-27
revisado: 2026-11-27
---

# Registro de movimientos

Un registro de movimientos guarda cada cambio de una cantidad (una compra, una venta, una
devolución, un ajuste) como una fila que no se edita, y calcula el saldo sumando esas filas. Es la
manera de llevar el stock, una cuenta corriente o cualquier saldo sin perder de dónde salió cada
número.

Qué es el stock de un comercio (la variante, sus estados, la sobreventa) está en
[catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md). Esta nota trata cómo se
guarda en una base. La misma idea en una planilla está en
[planilla de stock](../../Planillas-de-calculo/Diseno-de-planillas/planilla-de-stock.md).

## Un número que se pisa o una lista que se suma

La tabla `productos` de [definir tablas](../SQL/definir-tablas.md) tiene una columna `stock` que cada venta
descuenta. Sirve para saber cuánto hay ahora, pero no dice por qué hay eso: si el número da 12 y en
el estante hay 11, no queda rastro de qué venta, devolución o error lo llevó ahí.

Un registro de movimientos guarda los hechos y deja el saldo como un cálculo:

```sql
CREATE TABLE movimientos_stock (
  id          integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  producto_id integer NOT NULL REFERENCES productos (id),
  fecha       timestamptz NOT NULL DEFAULT now(),
  tipo        text NOT NULL CHECK (tipo IN ('compra', 'venta', 'devolucion', 'ajuste', 'merma')),
  cantidad    integer NOT NULL CHECK (cantidad <> 0),   -- positiva entra, negativa sale
  pedido_id   integer REFERENCES pedidos (id),           -- de dónde viene, si viene de un pedido
  motivo      text
);
```

El saldo de cada producto es una [agregación](../SQL/agregacion.md), y el saldo a una fecha es la misma suma
cortada en esa fecha:

```sql
SELECT producto_id, sum(cantidad) AS stock
FROM movimientos_stock
GROUP BY producto_id;

SELECT sum(cantidad) AS stock_al_15
FROM movimientos_stock
WHERE producto_id = 7 AND fecha < '2026-11-16';
```

Con cinco movimientos de prueba (compra de 20, venta de 3, devolución de 1, venta de 5 y un ajuste
de −1) la primera consulta da 12 y la segunda, 18. Las consultas se probaron en SQLite con el
esquema adaptado.

Kleppmann describe la misma forma con otras palabras: un log es "an append-only, totally ordered
sequence of records", y un contador es un dato derivado del log. Fowler agrega que con la lista de
cambios se puede saber "the application state at any point in time", reproduciéndolos hasta la
fecha elegida.

## Un error se corrige con otro movimiento

Un movimiento no se edita ni se borra: si estaba mal, se agrega otro que lo compensa. Fowler
explica por qué conviene que los movimientos sean diferencias y no valores finales: revertir "add
$10" es simple, y revertir "set account to $110" obliga a guardar el valor anterior.

La contabilidad trabaja igual. En el inventario permanente que describe OpenStax, el sistema
"automatically updates and records the inventory account" con cada compra y cada venta, y el conteo
físico se compara con el saldo de los libros: la diferencia se registra como un asiento de ajuste,
no tachando lo anterior. El kardex de la contabilidad latinoamericana (fecha, entradas, salidas y
saldo de cada artículo) es esa misma ficha; para el kardex solo se encontraron blogs contables, no
una norma.

Los sistemas de gestión siguen el patrón. En Odoo, el conteo físico carga lo contado ("Counted")
contra lo que dice el sistema ("On Hand") y aplica la diferencia; ERPNext lleva un "Stock Ledger"
con los movimientos de compras, ventas, fabricación y transferencias. En una base propia, el conteo
se traduce en un movimiento de tipo `ajuste` por la diferencia, con el motivo escrito:

```sql
INSERT INTO movimientos_stock (producto_id, tipo, cantidad, motivo)
VALUES (7, 'ajuste', -1, 'conteo físico: había 12, el sistema decía 13');
```

## Saldo calculado, saldo guardado o los dos

Sumar todos los movimientos en cada consulta es lo más simple y siempre da bien, pero recorre más
filas a medida que pasa el tiempo. Hay tres maneras de llevarlo:

| Manera | Cómo | Lo que cuesta |
|---|---|---|
| Solo movimientos | El saldo se calcula con `sum` cada vez, con un [índice](../SQL/indice.md) por producto y fecha | Más lento cuanto más historia hay; no impide vender lo que no hay sin una consulta previa |
| Saldo materializado | Una vista materializada con el saldo por producto, que se refresca cada tanto | PostgreSQL avisa que "the data is not always current": sirve para reportes, no para decidir una venta |
| Saldo y movimiento juntos | Cada venta inserta el movimiento y descuenta la columna `stock` en la misma [transacción](../Transacciones/transaccion.md) | Dos lugares que tienen que coincidir; la transacción y un control periódico los mantienen iguales |

La tercera es la que suele convenir para el stock de un comercio, aunque es una inferencia de esta
base y no la propone ninguna fuente leída. Junta el rastro de los movimientos con la protección de
la [actualización condicional](../SQL/modificar-datos.md#descontar-stock-sin-vender-lo-que-no-hay): si el `UPDATE`
no afecta ninguna fila, no había stock y la transacción se deshace sin dejar movimiento.

```sql
BEGIN;
UPDATE productos SET stock = stock - 2 WHERE id = 7 AND stock >= 2 RETURNING stock;
-- si no devolvió ninguna fila: ROLLBACK
INSERT INTO movimientos_stock (producto_id, tipo, cantidad, pedido_id) VALUES (7, 'venta', -2, 41);
COMMIT;
```

El control periódico compara la columna con la suma de los movimientos; si difieren, algo escribió
por afuera de este camino. Por qué dos ventas simultáneas no se pisan con este `UPDATE` está en
[concurrencia](../Transacciones/concurrencia.md). Fowler propone algo parecido para no reproducir todo desde
cero: guardar una instantánea del estado (la de la noche anterior, por ejemplo) y reproducir solo lo
posterior. Cuántos movimientos hacen falta para que la suma completa se vuelva lenta no lo dice
ninguna fuente leída: depende del índice y de la máquina, y conviene medirlo con
[`EXPLAIN ANALYZE`](../SQL/indice.md).

## Una tabla de movimientos no es event sourcing

Event sourcing lleva la idea a todo el sistema: Fowler lo define como capturar "all changes to an
application state as a sequence of events", y el estado de la aplicación sale de reproducirlos. Una
tabla de movimientos de stock dentro de una base relacional común usa el mismo principio en un solo
lugar, sin cambiar cómo funciona el resto del sistema.

> [!IMPORTANT]
> **Las críticas apuntan al sistema entero, no a la tabla.** Greg Young, uno de los que difundieron
> el patrón, advirtió en 2016 contra "the common anti-pattern of building a whole system based on
> Event sourcing": según él, "CQRS and Event sourcing are not top-level architectures". Kiehl (2019)
> describe el costo en la práctica: "the shear volume of plumbing code involved is staggering", y
> discute el valor de auditoría que Fowler presenta como beneficio, porque los eventos de bajo
> nivel rara vez le interesan a alguien. Leído al revés, el consejo de Young respalda usar un
> registro de movimientos solo donde importa la historia, como el stock o una cuenta corriente;
> esto último es una lectura de esta base.

## Lo que queda abierto

> [!NOTE]
> Sin fuente todavía: una fuente primaria del patrón que guarda saldo y movimiento en la misma
> transacción; el texto de Kleppmann en *Designing Data-Intensive Applications* sobre el libro mayor
> (solo se vio una cita de un lector); los patrones contables de Fowler (solo se leyó el índice); y
> el kardex en una norma contable.

Ver también: [base relacional](base-relacional.md), [cuándo pasar a una base](../../Planillas-de-calculo/cuando-pasar-a-una-base.md).
