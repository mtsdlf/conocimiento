---
resumen: >-
  Existencias es la parte del dominio que dice qué tiene la empresa: cada artículo, cuántas unidades hay, en qué lugar, de qué lote y en qué estado, y cuánto de eso se puede prometer a un pedido nuevo. Todo lo demás del tema la cambia, la corrige o la consulta.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, Inventory Visibility: on-hand change schedule y available-to-promise (fórmula de disponible por estados): https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-available-to-promise"
  - "Odoo 17, Use locations (ubicaciones virtuales de tránsito y de pérdida de inventario; según el resumen leído): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations.html"
  - "Caplice, C. (MIT CTL), Inventory Management: Probabilistic Demand, ESD.260 lección 11, oct. 2006, diap. 5 (posición de inventario): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf"
  - "DeHoratius y Raman (2008), Inventory Record Inaccuracy: An Empirical Analysis, Management Science 54(4), 627-641: https://doi.org/10.1287/mnsc.1070.0789 (según el resumen)"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (2026-11-27)"
  - "Inventario-y-depositos/.investigacion/operacion-del-deposito.md y reposicion.md (2026-11-27)"
aliases: [existencias, stock, inventario disponible, on hand, stock on hand, inventory balance, saldo de stock]
creado: 2026-11-27
revisado:
---

# Existencias

Existencias es la parte del dominio que dice qué tiene la empresa: cada artículo, cuántas unidades hay, en qué lugar, de qué lote y en qué estado, y cuánto de eso se puede prometer a un pedido nuevo. Todo lo demás del tema la cambia, la corrige o la consulta.

Es el centro de [Inventario y depósitos](../inventario-y-depositos.md). La [operación del depósito](../Operacion-del-deposito/operacion-del-deposito.md) la cambia con cada recepción, reserva y salida; el [control del stock](../Control-del-stock/control-del-stock.md) la cuenta y la corrige; [reposición](../Reposicion/reposicion.md) mira la posición de stock para decidir cuándo pedir más; y el [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) consulta cuánto hay disponible antes de fijar la [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md). Cuánto vale lo que hay no es de acá: es [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md), de Contabilidad.

## La fórmula del stock: una cantidad con cuatro coordenadas

Una cantidad de stock dice poco si no se sabe de qué, dónde y en qué condición. La base la escribe así (criterio de la base, armado sobre la práctica de los sistemas que se citan abajo):

> cantidad = f(artículo, lugar, lote o serie, estado)

| Coordenada | Qué fija | Nota que la explica |
|---|---|---|
| Artículo | Qué cosa se cuenta y en qué unidad | [artículo](articulo.md) |
| Lugar | El depósito, la zona y la ubicación donde está | [ubicaciones](../Operacion-del-deposito/ubicaciones.md) |
| Lote o serie | Qué partida o qué unidad identificada, cuando el artículo se sigue así | [lote y serie](lote-y-serie.md) |
| Estado | Si se puede usar, si ya está apartada, si espera inspección | [estados del stock](estados-del-stock.md) |

La práctica separa así las cantidades. El ERP de un proveedor grande calcula lo disponible sumando y restando cantidades que guarda aparte: stock físico, en inspección de calidad, entrante, reservado en firme, reservado en blando y saliente. Un sistema abierto modela el tránsito y las pérdidas de inventario como ubicaciones virtuales (según el resumen leído), es decir, los mete en la coordenada del lugar. La misma idea, aplicada a una tienda online, está en [catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md).

No todos los artículos usan las cuatro. Un comercio chico con un solo local lleva artículo y cantidad; el lote aparece cuando hay vencimiento o una obligación de rastrear, y el estado aparece en cuanto alguien aparta mercadería para un pedido que todavía no salió.

## La cantidad es un saldo de movimientos

Ninguna de esas cantidades se escribe a mano. Cada una es la suma de los movimientos que la tocaron: una recepción suma en un lugar y un estado, una transferencia resta de un lugar y suma en otro, una reserva pasa unidades de disponible a comprometido sin moverlas del estante. Un error se corrige con otro movimiento, no pisando el número. Cómo se guarda eso en una base está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md), y en una planilla, en [planilla de stock](../../Planillas-de-calculo/Diseno-de-planillas/planilla-de-stock.md).

Por eso un cambio de estado también es un movimiento. Liberar un lote de la cuarentena, bloquear unidades dañadas o deshacer una reserva dejan un registro con fecha y responsable, aunque nadie haya tocado una caja (criterio de la base).

## Tres cantidades que se confunden

Tres cifras se calculan sobre las mismas existencias y contestan preguntas distintas:

| Cifra | Pregunta | Qué suma y qué resta | Quién la usa |
|---|---|---|---|
| Stock físico | ¿Cuánto hay en el estante? | Todo lo que está en el lugar, en cualquier estado | el depósito y el [conteo cíclico](../Control-del-stock/conteo-ciclico.md) |
| Disponible para prometer | ¿Cuánto se le puede comprometer a un pedido nuevo, y para cuándo? | Oferta confirmada menos demanda comprometida, por período | ventas, con [disponible para prometer](disponible-para-prometer.md) |
| Posición de stock | ¿Hace falta pedir más? | Según Caplice, «IP = Inventory Position = (IOH) + (Inv On Order) – (Backorders) – (Committed)» | [punto de pedido](../Reposicion/punto-de-pedido.md) |

La diferencia está en lo comprometido: el físico no lo resta, lo disponible lo resta período por período y la posición de stock lo resta todo junto, sumando lo que ya se pidió al proveedor.

## Cómo fallan las existencias

- **El número no es el del estante.** DeHoratius y Raman (2008) encontraron que el 65 % de casi 370.000 registros de 37 tiendas de un minorista eran inexactos (según el resumen; es un solo minorista). Lo disponible, la reserva y el punto de pedido heredan ese error. Es el problema de [control del stock](../Control-del-stock/control-del-stock.md).
- **Lo comprometido se descuenta dos veces.** Si un pedido confirmado resta como pedido y su reserva resta otra vez como reserva, lo disponible da menos de lo que hay. Qué cuenta como comprometido se decide una sola vez, en [disponible para prometer](disponible-para-prometer.md).
- **La unidad no es la misma.** Si se compra por caja y se vende por unidad sin una conversión en el [artículo](articulo.md), el saldo mezcla cajas con unidades.
- **El estado vive en la cabeza de alguien.** Mercadería rota que sigue en el estante sin marcar se vende como disponible; el estado tiene que estar en el registro, en [estados del stock](estados-del-stock.md).

## Qué hay adentro de Existencias

- [Artículo](articulo.md): el dato maestro de lo que se guarda, con su código, su unidad de medida y sus conversiones, y si lleva stock; leer primero.
- [Lote y serie](lote-y-serie.md): cuándo se sigue una partida o una unidad identificada, el vencimiento y el orden de salida (FIFO, FEFO).
- [Estados del stock](estados-del-stock.md): la lista de estados en que se reparte una cantidad (físico, disponible, comprometido, en tránsito, en cuarentena, bloqueado, de terceros); las demás notas del tema la enlazan.
- [Disponible para prometer](disponible-para-prometer.md): el cálculo de cuánto se puede comprometer a un pedido nuevo en cada fecha, con los métodos discreto y acumulado y qué cuenta como comprometido.

Apartar unidades para un pedido es un verbo de la operación y está en [reserva](../Operacion-del-deposito/reserva.md); su resultado es el estado comprometido de esta vertical.
