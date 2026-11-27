---
resumen: >-
  Una orden de compra emitida se cambia o se cancela, y cada camino tiene su regla: el cambio la devuelve a borrador y puede pedir una nueva aprobación, y la cancelación solo alcanza a lo que no se recibió ni se facturó. Cada versión confirmada queda guardada, para saber qué se le pidió al proveedor y cuándo.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft, Dynamics 365 Supply Chain Management, Approve and confirm purchase orders (secciones «Changing purchase orders» y «Canceling purchase orders»): https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation"
  - "ERPNext, Purchase Order (cancelar y enmendar, cerrar; según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-order"
  - "Microsoft, Dynamics 365 Supply Chain Management, Purchase agreements (cambiar el precio rompe el vínculo): https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (sección 4)"
aliases: [cambios en la orden de compra, modificar orden de compra, change order, purchase order change, re-aprobación, reaprobación, re-approval, cancelar orden de compra, cancel purchase order, versión de la orden, cancelar y enmendar, cancel and amend, finalizar orden]
creado: 2026-11-27
revisado:
---

# Cambios y cancelaciones

Una orden de compra emitida se cambia o se cancela, y cada camino tiene su regla: el cambio la devuelve a borrador y puede pedir una nueva aprobación, y la cancelación solo alcanza a lo que no se recibió ni se facturó. Cada versión confirmada queda guardada, para saber qué se le pidió al proveedor y cuándo.

Es el componente de [Orden de compra](orden-de-compra.md) que cubre lo que pasa cuando la orden ya salió y algo cambia del lado de quien compra: el área pide más, el precio se renegoció o la necesidad desapareció. Lo que cambia del lado del proveedor (no puede entregar en fecha, manda menos, manda otra cosa) es de [Seguimiento de la orden](../Seguimiento-de-la-orden/seguimiento-de-la-orden.md). El espejo del lado de la venta es [cambios y cancelaciones del pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/cambios-y-cancelaciones.md).

## Cambiar una orden aprobada

En un ERP grande, con el control de cambios activo, una orden aprobada no se edita en el lugar. Se pide el cambio («Request change»), la orden vuelve a borrador y, al terminar, pasa otra vez por aprobación si la política lo exige. La política se llama regla de re-aprobación y define qué tipos de cambio obligan a aprobar de nuevo.

Qué cambios deberían pedir una nueva aprobación lo decide cada empresa. Lectura de esta base, no dato de la fuente: un cambio que sube el monto vuelve a pasar por la matriz de [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md), porque puede cruzar a un tramo que aprueba otra persona; una fecha corrida o un depósito de destino distinto, en general, no. Sin esa regla, una orden se aprueba por un monto chico y se agranda después, que es la misma trampa que el porcentaje de sobrepedido de la [solicitud de compra](solicitud-de-compra.md) (lectura de esta base).

Hay cambios que el sistema no deja hacer. Si parte del renglón ya se entregó, la cantidad pedida no se cambia en borrador. Y si la orden salió contra un [contrato marco](../Abastecimiento-estrategico/contrato-marco.md) con precio fijo, cambiarle el precio rompe el vínculo: ese renglón deja de contar para el compromiso (las reglas del contrato están en [contrato marco](../Abastecimiento-estrategico/contrato-marco.md); lo que hereda cada orden, en [tipos de orden](tipos-de-orden.md)).

## Las versiones de la orden

Cada vez que se confirma una orden, el ERP grande guarda una copia exacta de lo confirmado. El resultado es un historial de versiones: qué decía la orden el día que se confirmó y qué dijo después del cambio. Ese historial permite responder (lectura de esta base), frente a una diferencia en la recepción o en la factura, qué se le había pedido al proveedor en ese momento.

Un sistema abierto resuelve el cambio importante de otra manera: se cancela la orden y se crea una enmienda («cancel and amend»), sin tocar el historial (según el resumen de su documentación). Los dos caminos coinciden en que la versión vieja no se pisa (lectura de esta base). Que el sistema no permita editar en el lugar una orden ya aprobada es criterio de la base, coherente con lo que pide [controles sobre los sistemas](../../Contabilidad/Control-interno/controles-sobre-sistemas.md).

## Cancelar el total o el saldo

Una orden confirmada ya no se borra: se cancela. En el ERP grande se puede cancelar la cantidad total o el resto de un renglón, siempre que esa cantidad no se haya recibido ni facturado. El ejemplo de su documentación: un renglón de 5 unidades con 3 recibidas permite cancelar 2, y el renglón queda en recibido. Con control de cambios, la cancelación también pasa por aprobación.

Lo ya registrado pone límites. En el sistema abierto, los recibos o las facturas ligados a la orden pueden bloquear la cancelación; lo esperable es deshacer primero esos documentos, que son de Inventario y de Contabilidad (lectura de esta base). El ERP grande, además, tiene un paso final, finalizar, que deja la orden cerrada financieramente y evita que se siga procesando.

## Cerrar no es cancelar

Cerrar es dejar de esperar el saldo pendiente sin revertir lo ya recibido o facturado; cancelar anula la cantidad como si no se hubiera pedido. Cuándo se cierra y qué queda están en [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md). La diferencia importa para medir al proveedor: una orden cerrada con saldo cuenta como entrega incompleta y una cancelada por quien compra, no (lectura de esta base); la medición está en [evaluación de proveedores](../Proveedores/evaluacion-de-proveedores.md).

| Acción | Qué alcanza | Qué deja |
|---|---|---|
| Cambiar | Cualquier renglón no entregado | Una versión nueva, que puede pedir otra aprobación |
| Cancelar | Lo no recibido ni facturado | El renglón con lo que sí se recibió |
| Cerrar | El saldo pendiente | Todo lo registrado, sin revertir |
| Finalizar | La orden entera | La orden cerrada financieramente, sin más procesamiento |

## Avisarle al proveedor

Ninguna fuente leída dice quién le avisa al proveedor de un cambio o una cancelación, ni cómo. Que cada confirmación guarde una copia sugiere el camino: mandar la versión nueva y esperar que el proveedor la vuelva a aceptar, como con la orden original; es lectura de esta base. Cómo se registra el acuse está en [confirmación y seguimiento](../Seguimiento-de-la-orden/confirmacion-y-seguimiento.md).

Del lado legal, la orden aceptada puede ser ya un contrato, como se explica en [orden de compra](orden-de-compra.md), y cancelarla podría tener un costo con el proveedor. Las fuentes leídas no lo tratan.

> [!NOTE] Sin fuente todavía: quién avisa al proveedor de un cambio o una cancelación, qué se hace si no la acepta, y el costo de cancelar una orden ya aceptada; para la Argentina, nada todavía.
