---
resumen: >-
  La orden de compra es el documento con el que una empresa le pide a un proveedor ciertos productos o servicios, en cierta cantidad, a cierto precio y para cierta fecha. Es un documento con estados que siguen tres ejes a la vez (si está aprobada, cuánto se recibió y cuánto se facturó), y es el punto donde la necesidad interna pasa a ser un compromiso con alguien de afuera.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3 «Order materials and services»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Wikipedia, Purchase order (según su resumen): https://en.wikipedia.org/wiki/Purchase_order"
  - "Microsoft, Dynamics 365 Supply Chain Management, Approve and confirm purchase orders: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation"
  - "ERPNext, Purchase Order (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-order"
  - "Cornell Law School LII, UCC § 2-207 (según su resumen): https://www.law.cornell.edu/ucc/2/2-207"
  - "CIPS, The thirteen steps of the procurement process (según su resumen): https://1prd-dxp.cips.org/intelligence-hub/procurement/procurement-process"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (secciones 1 a 4) y apqc-4-2.md"
aliases: [orden de compra, OC, purchase order, PO, nota de pedido al proveedor, pedido de compra, pedido al proveedor, estados de la orden de compra]
creado: 2026-11-27
revisado:
---

# Orden de compra

La orden de compra es el documento con el que una empresa le pide a un proveedor ciertos productos o servicios, en cierta cantidad, a cierto precio y para cierta fecha. Es un documento con estados que siguen tres ejes a la vez (si está aprobada, cuánto se recibió y cuánto se facturó), y es el punto donde la necesidad interna pasa a ser un compromiso con alguien de afuera.

Es la tercera de las cuatro partes de [Compras y abastecimiento](../compras-y-abastecimiento.md). Nace de una [solicitud de compra](solicitud-de-compra.md) aprobada, de un pedido de cotización o de un [contrato marco](../Abastecimiento-estrategico/contrato-marco.md), y toma del [registro del proveedor](../Proveedores/proveedores.md) a quién se le pide y en qué [condiciones](../Proveedores/condiciones-del-proveedor.md). Una vez emitida, su vida sigue en [Seguimiento de la orden](../Seguimiento-de-la-orden/seguimiento-de-la-orden.md). Del otro lado, es el [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) del proveedor.

## Qué le pide la orden al proveedor

Los campos que aparecen en las fuentes leídas son el proveedor, los renglones con cantidad, unidad y precio, el depósito de destino, la fecha requerida, las condiciones de pago y de entrega, los impuestos y la referencia a la solicitud o la cotización de origen. Un sistema abierto da un ejemplo: 200 adaptadores a USD 18, USD 3.600 en total, con el precio tomado de la cotización aceptada.

Emitir la orden no forma un contrato por sí solo: sin un contrato previo, lo forma la aceptación del proveedor (según el resumen del artículo de Wikipedia). Qué pasa cuando el acuse agrega términos propios, según la ley de los Estados Unidos, está en [confirmación y seguimiento](../Seguimiento-de-la-orden/confirmacion-y-seguimiento.md). Sin fuente todavía para la Argentina.

## Los estados: tres ejes cruzados

Los estados de una orden no forman una línea. Las fuentes mezclan tres preguntas distintas: si la empresa ya aprobó lo que pide, cuánto llegó y cuánto facturó el proveedor. Un ERP grande lleva el primer eje con siete estados cuando el control de cambios está activo (el de revisión externa sale de su sección sobre la confirmación):

| Estado de aprobación | Qué significa |
|---|---|
| Borrador | Se está armando; se puede cambiar libremente |
| En revisión | Espera la aprobación interna |
| Rechazada | Quien aprueba no la aceptó |
| Aprobada | Aprobada adentro; recién ahí genera movimientos de stock esperado |
| En revisión externa | Consulta al proveedor sobre precios, descuentos o fechas de recepción; si tiene portal, ahí aprueba o rechaza |
| Confirmada | Registrada como comprometida; no se llega sin pasar por aprobada |
| Finalizada | Cerrada financieramente; no admite cambios. No es lo mismo que cerrar el saldo, que se explica en [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md) |

Un sistema abierto, en cambio, lleva el avance con estos estados: a recibir y facturar, a recibir, a facturar, completada, en espera, cerrada y cancelada. Son el cruce de los otros dos ejes, cuánto se recibió (nada, una parte, todo) y cuánto se facturó, más tres salidas: pausar, dejar de procesar el saldo o anular (lectura de esta base). El mismo problema, del lado de la venta, está en el [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md).

Modelar el estado como una sola lista de valores hace que la orden mienta: dice «recibida» cuando faltan renglones, o «aprobada» cuando ya se facturó. Por eso cada renglón lleva lo suyo y la cabecera resume; es criterio de la base. «Enviada al proveedor» no aparece como estado de la orden en ninguna fuente leída.

## Qué dispara aprobar y confirmar

Según el resumen de la documentación de un sistema abierto, someter la orden compromete la compra pero no mueve stock ni asienta en el mayor: los recibos y las facturas se controlan contra ella. En el ERP grande, la orden genera movimientos de stock esperado, el que está en camino, solo al llegar a aprobada, y ese stock no se puede reservar antes. Al confirmarla, el sistema guarda una copia exacta de lo confirmado (las versiones están en [cambios y cancelaciones](cambios-y-cancelaciones-de-la-orden.md)) y, si están activas, genera las distribuciones contables y verifica el presupuesto.

La deuda con el proveedor la registra Contabilidad: al recibir, como recibido sin facturar, y se confirma con la factura ([compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md)). Quién aprueba según el monto lo dice la matriz de [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md), que tiene una fila para la orden de compra; acá importa que aprobar sea un paso registrado, con quién, cuándo y sobre qué versión (criterio de la base).

## Dónde está en los marcos de procesos

APQC 7.4 tiene un grupo propio, 4.2.3 «Order materials and services», con siete pasos. Este tema los reparte entre esta vertical y la siguiente:

| Código | Paso | Dónde está en la base |
|---|---|---|
| 4.2.3.1 | «Process/Review requisitions» | [solicitud de compra](solicitud-de-compra.md) |
| 4.2.3.2 | «Approve requisitions» | [solicitud de compra](solicitud-de-compra.md) |
| 4.2.3.3 | «Solicit supplier quotes» | [cotización y licitación](../Abastecimiento-estrategico/cotizacion-y-licitacion.md) |
| 4.2.3.4 | «Create/Distribute purchase orders» | esta nota y [tipos de orden](tipos-de-orden.md) |
| 4.2.3.5 | «Expedite orders and satisfy inquiries» | [confirmación y seguimiento](../Seguimiento-de-la-orden/confirmacion-y-seguimiento.md) |
| 4.2.3.6 | «Reconcile purchase orders» | [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md) |
| 4.2.3.7 | «Research/Resolve order exceptions» | [diferencias y devoluciones](../Seguimiento-de-la-orden/diferencias-y-devoluciones.md) y [cambios y cancelaciones](cambios-y-cancelaciones-de-la-orden.md) |

APQC pone el pedido de cotización dentro de ordenar; la base lo deja en Abastecimiento estratégico, donde se comparan las ofertas. CIPS no tiene un paso para la orden: cae dentro de su paso 9, «Contract award and implementation» (según su resumen).

## Lo que pasa después de emitir

El acuse del proveedor, la recepción contra lo pedido, el saldo y las diferencias son de [Seguimiento de la orden](../Seguimiento-de-la-orden/seguimiento-de-la-orden.md), la vertical hermana.

## Qué hay en Orden de compra

- [Solicitud de compra](solicitud-de-compra.md): el pedido interno, quién pide y quién aprueba, y la compra fuera del circuito.
- [Tipos de orden](tipos-de-orden.md): puntual, abierta, contra contrato, de servicios y en consignación, y qué cambia en cada una.
- [Cambios y cancelaciones](cambios-y-cancelaciones-de-la-orden.md): modificar una orden emitida, cuándo vuelve a aprobarse, cancelar el total o el saldo y cerrar sin cancelar.
