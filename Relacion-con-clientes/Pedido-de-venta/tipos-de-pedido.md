---
resumen: >-
  Los tipos de pedido son las variantes del pedido de venta que cambian qué se compromete y cuándo: el de contado, que se supone entregado y cobrado en el acto; el común a plazo; el pedido abierto o marco, que fija condiciones para entregas futuras; el recurrente, que se repite solo; y el de muestra, sin cargo. Las devoluciones y la consignación son vecinos, no tipos.
estado: vigente
estabilidad: estable
fuentes:
  - "SAP R/3 4.7, Sales Document Types: https://help.sap.com/saphelp_470/helpdata/en/dd/55fb06545a11d1a7020000e829fd11/content.htm"
  - "Microsoft Dynamics 365 SCM, Sales agreements overview: https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements"
  - "Microsoft Dynamics 365 Business Central, Work with blanket sales orders: https://learn.microsoft.com/en-CA/dynamics365/business-central/sales-how-to-create-blanket-sales-orders"
  - "ERPNext, Blanket Order: https://docs.frappe.io/erpnext/user/manual/en/blanket-order"
  - "Odoo 17, Subscriptions: https://www.odoo.com/documentation/17.0/applications/sales/subscriptions.html"
  - "Odoo 18, Consignment: https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/owned_stock.html"
  - "Relacion-con-clientes/.investigacion/presupuesto-y-pedido.md (sección G)"
aliases: [tipos de pedido, order types, sales document types, pedido de contado, cash sale, venta de mostrador, pedido abierto, pedido marco, contrato marco, blanket order, sales agreement, acuerdo de venta, scheduling agreement, pedido recurrente, suscripción, subscription, muestra sin cargo, free-of-charge delivery]
creado: 2026-11-27
revisado: 2026-11-27
---

# Tipos de pedido

Los tipos de pedido son las variantes del pedido de venta que cambian qué se compromete y cuándo: el de contado, que se supone entregado y cobrado en el acto; el común a plazo; el pedido abierto o marco, que fija condiciones para entregas futuras; el recurrente, que se repite solo; y el de muestra, sin cargo. Las devoluciones y la consignación son vecinos, no tipos.

Todos comparten la forma del [pedido de venta](pedido-de-venta.md). Lo que cambia entre uno y otro es cuándo se entrega, cuándo se factura y si el pedido mueve stock o solo fija condiciones.

## Una taxonomía de referencia

Un ERP de un proveedor grande tiene la clasificación más completa de las leídas, y sirve como mapa aunque los nombres sean suyos:

| Grupo | Tipos |
|---|---|
| Preventa | consulta, presupuesto, entrega sin cargo |
| Pedidos | pedido común, venta de contado, pedido urgente |
| Acuerdos marco | contrato por cantidad, contrato de mantenimiento, contrato de alquiler, programa de entregas |
| Aparte | reclamos y devoluciones |

Dos cosas se ven en la tabla. Los acuerdos marco no son pedidos: son otro tipo de documento del que salen pedidos. Y las devoluciones van en un grupo aparte. La misma documentación aclara que cada empresa puede sumar sus propios tipos.

## Contado y a plazo

El pedido **común** es el que se confirma, se entrega después y se factura según la política (al confirmar o al entregar). Si se paga después, la deuda va a la [cuenta corriente](../../Comercio-electronico/Comercio-B2B/cuenta-corriente-y-credito.md) del cliente, con el plazo de sus [condiciones comerciales](../Registro-del-cliente/condiciones-comerciales.md).

El pedido **de contado** (venta de mostrador) es un tipo propio en el ERP de la tabla, igual que el pedido urgente. Que se entregue y se cobre en el mismo momento es la hipótesis de la base, sin confirmar en la fuente. Que el sistema lo trate como pedido o no es una decisión de diseño; tratarlo como pedido deja la misma cadena de documentos para todas las ventas. Esto es criterio de la base.

> [!NOTE] Sin fuente todavía: qué distingue al pedido de contado en los sistemas (si genera entrega y factura en el acto) y cómo lo resuelve el software de gestión argentino.

## El pedido abierto: tres lecturas del mismo nombre

El pedido abierto (también pedido marco, contrato marco o acuerdo de venta) fija con un cliente condiciones para un período, y de él salen pedidos concretos a medida que el cliente pide. Las fuentes lo definen de tres maneras distintas, y quien diseña tiene que elegir cuál:

1. **Un compromiso con precio.** En un ERP de un proveedor grande, el acuerdo de venta compromete al cliente a comprar cierta cantidad o cierto monto en un período, a cambio de precios, descuentos u otras condiciones especiales. Puede comprometer cantidad de un producto, monto de un producto, monto de una categoría o monto total; tiene fecha de inicio y de vencimiento; de él se liberan pedidos, y todos los renglones vinculados cuentan para el cumplimiento. Admite políticas: no pasar el máximo, precio fijo, monto mínimo y máximo por liberación. Antes se llamaba pedido abierto.
2. **Una hoja de planificación que no reserva.** En otro producto del mismo proveedor, el pedido abierto sirve para una cantidad grande que se entrega en envíos chicos a lo largo del tiempo, y la razón para usarlo es justamente que sus cantidades no afectan la disponibilidad: es una hoja para seguir, prever y planificar. Cada entrega se convierte en un pedido, que no puede pasar la cantidad del renglón del marco.
3. **Una referencia.** En un sistema abierto, según su resumen, registra un compromiso de largo plazo pero no mueve mercadería ni plata: los pedidos lo citan, y el sistema controla cuánto se pidió contra lo comprometido.

La diferencia importa para la [fecha prometida](fecha-prometida.md): en la lectura 2, las cantidades del marco explícitamente no afectan la disponibilidad. Y para el precio: en la 1, el precio del acuerdo manda sobre la lista (ver [precio y descuentos](../Presupuesto/precio-y-descuentos.md)).

## El pedido recurrente

El pedido recurrente se repite solo con una frecuencia: una suscripción, un abono, una entrega mensual de insumos. En un sistema abierto, un pedido con un plan de recurrencia se convierte en suscripción; el período se mide en semanas, meses o años, y la suscripción se cierra sola si el cliente no paga. El modelo de negocio está en [SaaS](../../Emprender/Modelo-de-negocio/saas.md) y en [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md); acá interesa que el pedido deja de ser un hecho único y pasa a generar entregas y facturas periódicas.

> [!NOTE] Sin fuente todavía: los estados de una suscripción y cómo se renueva.

## La muestra sin cargo

El ERP de la tabla tiene la entrega sin cargo como tipo de documento de preventa. Lo demás es criterio de la base: es mercadería que sale sin factura para que el cliente la pruebe, sale del stock y tiene que registrarse para que el inventario cierre, pero no genera deuda.

> [!NOTE] Sin fuente todavía: la muestra sin cargo en sistemas abiertos (según su resumen, no tiene un flujo propio).

## Lo que no es un tipo de pedido

- **Devoluciones.** Desandan una venta y van como documento propio que apunta al pedido original; en un ERP de un proveedor grande, la devolución de un pedido que salió de un acuerdo queda vinculada al acuerdo. El proceso de recibir, revisar y reponer está en [devoluciones](../../Comercio-electronico/Operaciones-del-comercio/devoluciones.md); el reclamo, en Servicio al cliente.
- **Consignación.** La recibida (el proveedor deja su mercadería en el depósito de la empresa, y la empresa la vende con un presupuesto común) es de Inventario y Compras. La entregada (la mercadería de la empresa en el local del cliente) no apareció en la documentación oficial leída.
- **Los canales.** Un pedido que entra por un vendedor, un portal o un chat sigue siendo del mismo tipo; los canales están en [pedido B2B](../../Comercio-electronico/Comercio-B2B/pedido-b2b.md) y [preventa y autoventa](../../Comercio-electronico/Comercio-B2B/preventa-y-autoventa.md).
