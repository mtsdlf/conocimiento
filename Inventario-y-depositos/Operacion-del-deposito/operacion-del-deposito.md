---
resumen: >-
  La operación del depósito es lo que se hace con la mercadería entre la puerta de entrada y la de salida: recibirla, ubicarla, apartarla para un pedido y prepararla. Cada uno de esos pasos es un movimiento que cambia dónde está el stock o en qué estado, y casi todo su costo es trabajo de gente que camina.
estado: borrador
estabilidad: estable
fuentes:
  - "Bartholdi y Hackman, Warehouse & Distribution Science, versión 0.98.1 (16-ago-2019), cap. 3 «Warehouse operations» y §4.1-4.3: https://www.warehouse-science.com/book/editions/wh-sci-0.98.1.pdf"
  - "De Koster, Le-Duc y Roodbergen (2007), Design and control of warehouse order picking: a literature review, EJOR 182(2), 481-501, DOI 10.1016/j.ejor.2006.07.009: https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.4.3 «Operate warehousing»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Inventario-y-depositos/.investigacion/operacion-del-deposito.md (2026-11-27)"
aliases: [operación del depósito, operación del almacén, operaciones de depósito, warehouse operations, warehousing, operar el depósito, flujo del depósito, gestión de depósitos, WMS, warehouse management system]
creado: 2026-11-27
revisado:
---

# Operación del depósito

La operación del depósito es lo que se hace con la mercadería entre la puerta de entrada y la de salida: recibirla, ubicarla, apartarla para un pedido y prepararla. Cada uno de esos pasos es un movimiento que cambia dónde está el stock o en qué estado, y casi todo su costo es trabajo de gente que camina.

Es la parte activa de [Inventario y depósitos](../inventario-y-depositos.md). Cada recepción, cada reserva y cada salida cambia las cantidades de [Existencias](../Existencias/existencias.md), y lo hace con un movimiento nuevo, nunca pisando el número (la regla está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md)). [Control del stock](../Control-del-stock/control-del-stock.md) cuenta lo que esta vertical guardó y corrige lo que se registró mal. [Reposición](../Reposicion/reposicion.md) decide cuándo y cuánto traer de afuera; lo que llega entra por acá.

## El flujo de la puerta de entrada a la de salida

Bartholdi y Hackman ordenan el trabajo de un depósito en una secuencia que sigue al producto: recibir, guardar, preparar el pedido, embalar y despachar. APQC 7.4 dice casi lo mismo en 4.4.3 «Operate warehousing», con pasos como 4.4.3.2 «Receive, inspect, and store inbound deliveries» y 4.4.3.4 «Pick, pack, and ship product for delivery». La base agrega la reserva, que el libro trata como un chequeo de disponibilidad al llegar el pedido.

| Paso | Qué pasa con la mercadería | Qué cambia en el registro | Dónde está |
|---|---|---|---|
| Recibir | se descarga, se cuenta y se inspecciona | entra al stock, a veces en un estado que no se puede vender | [recepción](recepcion.md) |
| Ubicar | se lleva a un lugar del depósito | queda asociada a una ubicación | [recepción](recepcion.md) y [ubicaciones](ubicaciones.md) |
| Reponer la zona de picking | baja de la zona de reserva a la de preparación | cambia de ubicación, no de cantidad | [ubicaciones](ubicaciones.md) |
| Reservar | no se mueve | una cantidad pasa a comprometida para un pedido | [reserva](reserva.md) |
| Preparar | se saca del estante y se junta por pedido | sale de su ubicación | [preparación de pedidos](preparacion-de-pedidos.md) |
| Embalar y controlar | se arma el bulto y se verifica el pedido | queda lista para despachar | [preparación de pedidos](preparacion-de-pedidos.md) |

La mercadería recibida no está a la venta hasta que se registra. Bartholdi y Hackman cuentan que al llegar se escanea para que la empresa asuma la propiedad, pague al proveedor y sepa que tiene con qué atender pedidos. Del otro lado, el escaneo de lo embalado registra que el pedido está listo para salir.

## Dónde corta la base y dónde corta el campo

El campo no corta en la puerta. Bartholdi y Hackman ponen el despacho como último paso del mismo flujo, APQC junta preparar, embalar y despachar en un solo proceso (4.4.3.4), y los sistemas de gestión de depósitos lo incluyen. La base corta en la puerta de salida: el despacho, la carga del camión y el transporte son del tema Cadena de suministro y logística, todavía no armado. La frontera, como criterio de la base, es el registro de que el pedido embalado está listo para salir.

En la puerta de entrada el corte es parecido. Controlar que llegó lo pedido, contra la orden de compra, es de Compras y abastecimiento, todavía no armado. Esta vertical cuenta, inspecciona, aparta lo dudoso y ubica. El mismo libro marca el efecto hacia los costados: la recepción dispara el pago al proveedor y el despacho, la factura al cliente.

## Dónde se va el costo

Según Bartholdi y Hackman, que citan cifras de terceros, recibir es cerca del 10 % del costo operativo de un centro de distribución típico, guardar cerca del 15 % y preparar pedidos cerca del 55 %. La cifra del picking aparece también en De Koster, Le-Duc y Roodbergen («as much as 55%»), pero las dos remiten a la misma literatura de origen: es una sola cifra con dos reportes. Las de recibir y guardar tienen una sola fuente.

La idea que ordena la vertical es de Bartholdi y Hackman: la mayor parte del gasto de un depósito es mano de obra, la mayor parte de esa mano de obra es preparar pedidos y la mayor parte de preparar es caminar. Por eso casi todas las decisiones de diseño (qué va en cada ubicación, cómo se agrupan los pedidos, qué recorrido se hace) buscan acortar la caminata. Cómo se reparte el tiempo de quien prepara, según dos fuentes que no coinciden, está en [preparación de pedidos](preparacion-de-pedidos.md#dónde-se-va-el-tiempo-de-quien-prepara).

## Dos inventarios: el de productos y el de lugares

Un depósito con más de unos pocos pasillos lleva dos registros. Uno dice cuánto hay de cada artículo; el otro, qué ubicaciones están libres, de qué tamaño y cuánto peso aguantan. Bartholdi y Hackman llaman a la capacidad de llevar los dos «stock locator» y la ponen como lo que habilita a un sistema a decirle al operario dónde guardar y de dónde sacar. Está en [ubicaciones](ubicaciones.md).

## Cómo falla la operación

Las fallas típicas nacen en movimientos que pasan en el estante y no en el registro (criterio de la base, salvo donde se cita):

- **Sacar de otra ubicación.** Bartholdi y Hackman advierten que a quien se manda al otro extremo del depósito le tienta sacar el mismo artículo de un lugar más cerca; el total cuadra, pero dos ubicaciones quedan mal.
- **Guardar sin registrar dónde.** La mercadería existe y nadie la encuentra; para el sistema está disponible.
- **Vender lo que no pasó la inspección.** Si lo recibido entra directo como disponible, se puede prometer algo que después se rechaza.
- **No apartar al confirmar.** Dos pedidos se llevan la misma unidad y el segundo se entera en el estante.

Todas aparecen después como diferencias en el [conteo cíclico](../Control-del-stock/conteo-ciclico.md) y terminan en un ajuste ([ajustes y mermas](../Control-del-stock/ajustes-y-mermas.md)).

## Qué hay en Operación del depósito

- [Ubicaciones](ubicaciones.md): cómo se nombran los lugares del depósito (depósito, zona, ubicación), ubicación fija o libre, la zona de reserva y la de picking y la reposición entre ellas.
- [Recepción](recepcion.md): descargar, contar, inspeccionar, apartar en cuarentena y ubicar lo que llega; el cross-docking como recepción sin guardado.
- [Reserva](reserva.md): apartar stock para un pedido, en qué momento, de qué lote y cuándo se libera.
- [Preparación de pedidos](preparacion-de-pedidos.md): picking por pedido, por lote, por zona o por ola, y el embalaje y el control hasta la puerta.

En la Argentina, todo traslado de mercadería, también entre depósitos propios, va con remito; está en [Inventario y depósitos en la Argentina](../inventario-y-depositos-en-argentina.md). Si el depósito es de un tercero que prepara para una tienda online, el caso está en [fulfillment](../../Comercio-electronico/Operaciones-del-comercio/Envios-y-logistica/fulfillment.md).
