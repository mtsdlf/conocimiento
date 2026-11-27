---
resumen: >-
  Un pedido de venta confirmado cambia de cinco maneras: se entrega en partes, deja cantidades pendientes de entrega, se pausa, se cierra sin entregar lo que falta o se anula entero; además, se puede bloquear para que no se despache o no se facture. Cada cambio tiene que dejar rastro y avisar a los dominios que ya actuaron sobre el pedido.
estado: vigente
estabilidad: semi
fuentes:
  - "ERPNext, Sales Order (entrega y facturación parciales; pausar, cerrar y anular): https://docs.frappe.io/erpnext/user/manual/en/sales-order"
  - "Odoo 19, Create quotations (bloquear pedidos confirmados): https://www.odoo.com/documentation/19.0/applications/sales/sales/sales_quotations/create_quotations.html"
  - "Microsoft Dynamics 365 SCM, Sales agreements overview (cambiar un pedido vinculado a un acuerdo): https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements"
  - "SAP R/3 4.6C, bloqueos de entrega y de facturación: https://help.sap.com/saphelp_46c/helpdata/en/dd/55fc2e545a11d1a7020000e829fd11/content.htm"
  - "SAP Business One 9.0, backorder processing (según su resumen): https://help.sap.com/saphelp_sbo900/helpdata/EN/1b/b8feb2dc8a47b687cbf672f89c1962/content.htm"
  - "ERPNext, Authorization Rule: https://docs.frappe.io/erpnext/user/manual/en/authorization-rule"
  - "ERPNext, Customer (el límite de crédito bloquea operaciones): https://docs.frappe.io/erpnext/user/manual/en/customer"
  - "Microsoft Dynamics 365 Customer Engagement, tabla Account (el límite de crédito como referencia): https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md (componente 2, límite de crédito)"
  - "APQC, Process Classification Framework 7.4, 3.5.4.5 «Process back orders and updates»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Relacion-con-clientes/.investigacion/presupuesto-y-pedido.md (sección H)"
aliases: [cambiar un pedido, modificar pedido, order change, cancelar pedido, anular pedido, cancel order, cerrar pedido, close order, pedido en espera, on hold, entrega parcial, partial delivery, pendiente de entrega, backorder, back order, bloqueo de pedido, order block, delivery block, billing block, bloqueo por crédito, credit block]
creado: 2026-11-27
revisado: 2026-11-27
---

# Cambios y cancelaciones

Un pedido de venta confirmado cambia de cinco maneras: se entrega en partes, deja cantidades pendientes de entrega, se pausa, se cierra sin entregar lo que falta o se anula entero; además, se puede bloquear para que no se despache o no se facture. Cada cambio tiene que dejar rastro y avisar a los dominios que ya actuaron sobre el pedido.

Un [pedido de venta](pedido-de-venta.md) pocas veces se cumple tal como se confirmó: falta stock, el cliente cambia de idea, el crédito no alcanza. Esta nota trata cómo se registra eso. Es la parte del dominio con menos fuentes, y los huecos están marcados.

## Entregar en partes y lo pendiente de entrega

Un pedido se puede entregar o facturar en varias veces. En un sistema abierto, cada entrega y cada factura es un documento propio que apunta al pedido, y el pedido lleva el porcentaje entregado y el facturado. Por eso sus estados son el cruce de dos ejes y no una línea (ver [pedido de venta](pedido-de-venta.md)).

Lo que falta entregar es lo **pendiente de entrega** (backorder). APQC 7.4 le da un paso propio en la gestión de pedidos: «Process back orders and updates» (3.5.4.5). Con lo pendiente hay tres caminos, según el resumen de la documentación de un ERP: entregar la diferencia, actualizar la cantidad después del envío o cerrar lo que queda abierto del renglón.

La decisión es comercial y es del cliente tanto como de la empresa: si espera, si acepta un reemplazo o si prefiere que se cierre. Por eso conviene que lo pendiente quede a la vista en el pedido, con su propia [fecha prometida](fecha-prometida.md), y no escondido en el depósito. Esto es criterio de la base.

> [!NOTE] Sin fuente todavía: una definición de backorder y su ciclo en una fuente primaria (ASCM o un manual de un ERP actual).

## Pausar, cerrar y anular no son lo mismo

Un sistema abierto distingue tres acciones, y es la distinción más clara de las fuentes leídas:

| Acción | Qué hace | Qué pasa con lo ya hecho |
|---|---|---|
| Pausar (en espera) | Detiene el cumplimiento hasta nuevo aviso | Queda; el pedido sigue vivo |
| Cerrar | Decide no entregar lo que falta | Lo entregado y facturado queda; lo pendiente se da por terminado |
| Anular | Deshace el pedido entero | Criterio de la base: no debería haber nada hecho, o hay que deshacerlo primero |

Lo que sigue es criterio de la base. Cerrar es la salida normal de un pedido con pendientes que el cliente ya no quiere. Anular es para el pedido que no debió existir. Un pedido anulado no se borra: queda con su estado, igual que un [presupuesto](../Presupuesto/presupuesto.md) anulado.

> [!NOTE] Sin fuente todavía: la cancelación pedida por el cliente (con qué anticipación, con qué cargo) y cómo la registran los sistemas.

## Modificar un pedido confirmado

Cambiar la cantidad, la fecha o el precio de un pedido confirmado es el cambio más delicado, porque otros ya actuaron: Inventario reservó, quizás Cadena de suministro preparó el despacho, quizás Contabilidad facturó. Las fuentes leídas dicen poco:

- Un sistema abierto permite impedir toda edición de los pedidos confirmados.
- En un ERP de un proveedor grande, un pedido liberado de un acuerdo con el cliente solo se puede cambiar en fecha, precio, descuento o cantidad si antes se quita el vínculo con el acuerdo.

Sin fuente que lo diga, la regla que la base propone es tratar el cambio como un documento: o una versión nueva del pedido, o un pedido de ajuste que suma o resta. En cualquiera de los dos, el cambio tiene que volver a pasar por la disponibilidad y avisar a quien ya reservó o facturó. Es el mismo problema que un [cambio de alcance](../../Desarrollo/Encargo/cambios-de-alcance.md) en un encargo de software: lo acordado cambia y hay que dejar escrito qué cambió y quién lo aceptó.

> [!NOTE] Sin fuente todavía: qué pasa con la reserva y con la fecha prometida cuando cambia la cantidad o la fecha de un pedido ya reservado.

## Bloquear un pedido

Un bloqueo detiene una parte del cumplimiento sin cambiar el pedido. Un ERP de un proveedor grande distingue dos:

- **Bloqueo de entrega**: se puede poner en la cabecera, en un renglón o en una fecha de entrega del renglón.
- **Bloqueo de facturación**: se puede poner en la cabecera o en un renglón.

Lo que dispara un bloqueo suele ser una de tres causas (la lista es criterio de la base):

1. **Crédito.** El cliente pasó su límite o tiene deuda vencida. El límite es un dato de sus [condiciones comerciales](../Registro-del-cliente/condiciones-comerciales.md); quién lo fija y cuándo se levanta el bloqueo es de Tesorería. Un sistema abierto lo vuelve una regla que bloquea las operaciones; un CRM de un proveedor grande lo trata como referencia (el detalle, en condiciones comerciales). Según su resumen, el ERP de los bloqueos también tiene bloqueo por crédito, y los pedidos pendientes pueden caer en él cuando vuelve el stock.
2. **Aprobación.** El pedido pasa un umbral de monto o de descuento y espera que lo confirme alguien con más autoridad; en un sistema abierto, es una regla de autorización (ver [precio y descuentos](../Presupuesto/precio-y-descuentos.md)).
3. **Precio.** El precio del renglón quedó por debajo de lo permitido.

> [!NOTE] Sin fuente todavía: el bloqueo por precio (no se encontró en las fuentes leídas).

Un pedido bloqueado tiene que decir por qué y quién lo puede liberar; un bloqueo sin motivo a la vista termina en un cliente que llama para saber por qué no le llegó nada. Esto es criterio de la base.
