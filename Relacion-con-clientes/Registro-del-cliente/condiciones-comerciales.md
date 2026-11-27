---
resumen: >-
  Las condiciones comerciales son los datos del cliente que fijan cómo se le vende: qué lista de precios se le aplica, en qué plazo paga, hasta cuánto se le fía, en qué moneda se le factura, qué vendedor lo atiende y en qué zona está. Se cargan en el registro del cliente y cada presupuesto o pedido nuevo las toma como valor inicial.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, tabla Account: https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account (como evidencia de práctica)"
  - "Microsoft Learn, tabla Opportunity: https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/opportunity (como evidencia de práctica)"
  - "ERPNext, Customer: https://docs.frappe.io/erpnext/user/manual/en/customer (como evidencia de práctica)"
  - "Odoo 19.0, Contactos: https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html (como evidencia de práctica)"
  - "SAP Library 4.70, «Partner Functions»: https://help.sap.com/saphelp_470/helpdata/en/7f/f6341aac6111d2b44c006094b9ea37/content.htm"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md, componente 2"
aliases: [condiciones del cliente, condición de pago, payment terms, límite de crédito, credit limit, lista de precios del cliente, vendedor asignado, zona de venta]
creado: 2026-11-27
revisado:
---

# Condiciones comerciales

Las condiciones comerciales son los datos del cliente que fijan cómo se le vende: qué lista de precios se le aplica, en qué plazo paga, hasta cuánto se le fía, en qué moneda se le factura, qué vendedor lo atiende y en qué zona está. Se cargan en el registro del cliente y cada presupuesto o pedido nuevo las toma como valor inicial.

Son la parte del [registro del cliente](registro-del-cliente.md) que más pesa en la operación diaria. Viajan al [presupuesto](../Presupuesto/presupuesto.md), donde la lista de precios alimenta [precio y descuentos](../Presupuesto/precio-y-descuentos.md), y al [pedido de venta](../Pedido-de-venta/pedido-de-venta.md), donde el límite de crédito puede frenar la confirmación. No hay fuente fuera de los productos que las enumere: lo que sigue es lo que coinciden en guardar tres sistemas de gestión distintos, contado como práctica común.

## Qué condiciones guarda el cliente

| Condición | Qué fija | Cómo la usan los sistemas |
|---|---|---|
| Lista de precios | De qué lista sale el precio de cada producto para este cliente | Un sistema abierto la guarda en el cliente como lista por defecto; otro la elige desde el contacto; un CRM grande la pone en la oportunidad y no en la cuenta |
| Condición de pago | Cuándo vence lo que se le factura: de contado, a 30 días, a 60 | Los ejemplos de un CRM grande son a 30, 45 y 60 días, y un descuento por pagar en 10 días |
| Límite de crédito | Hasta cuánto puede deber el cliente | Como dato de referencia o como regla que bloquea (ver abajo) |
| Moneda | En qué moneda se le presupuesta y factura | Un sistema abierto la usa como moneda por defecto de cada documento nuevo |
| Vendedor | Quién lo atiende | Un dueño único, o un equipo con porcentajes (ver [cartera de clientes](cartera-de-clientes.md)) |
| Zona o territorio | Dónde está, para asignar y analizar | Un árbol de territorios o una lista que carga la empresa |
| Datos fiscales | Su identificación tributaria y su categoría de impuestos | Un número de identificación y una categoría de impuestos; lo argentino, en [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md) |

Un sistema abierto separa expresamente la condición de pago del límite de crédito: la plantilla de pagos decide cuándo vence cada importe y no agranda el crédito del cliente. Confundirlos es un error común de diseño: el plazo dice cuándo, el límite dice cuánto.

## El límite de crédito: dato o regla

Dos diseños conviven. En un CRM de un proveedor grande, el límite de crédito es un dato de referencia, útil cuando se habla con el cliente de facturas y saldos. En un sistema de gestión abierto es una regla: el sistema bloquea las operaciones cuando lo que el cliente debe supera el límite fijado para la empresa.

La diferencia importa para quien construye el pedido. Con el primer diseño el vendedor ve el número y decide; con el segundo, el [pedido de venta](../Pedido-de-venta/pedido-de-venta.md) queda bloqueado hasta que alguien con autoridad lo libera. En los dos casos, el límite lo fija Tesorería, que decide a quién fiar y cuánto; este tema solo lo guarda y lo aplica. Cómo se ve en la venta entre empresas argentina, con la cuenta corriente y el cheque, está en [cuenta corriente y crédito](../../Comercio-electronico/Comercio-B2B/cuenta-corriente-y-credito.md).

## Del cliente o del pagador

Cuando el que compra y el que paga son registros distintos (ver comprador, pagador y destinatario en [cuenta y contacto](cuenta-y-contacto.md)), hay que decidir de qué registro se lee cada condición. La condición de pago y el límite de crédito son del que paga: un local de una cadena no tiene crédito propio si paga la casa matriz. En el diseño más detallado, el de SAP, las condiciones se cargan además por área de ventas, de modo que un mismo cliente puede tener condiciones distintas según qué parte de la empresa le venda; esto se conoce por resúmenes. En los sistemas más chicos, todo queda en el cliente.

## Valor inicial, no valor fijo

Las condiciones del cliente se copian al documento como valor inicial, y el documento puede cambiarlas: un pedido puntual con otro plazo, un presupuesto con otra lista. Un sistema abierto lo dice para los precios: la lista sugiere, pero se puede pisar en el pedido. Lo que se pisa queda en el documento y no cambia el cliente. Eso permite saber, meses después, con qué condición se vendió cada cosa, aunque la del cliente haya cambiado.

Cuando el precio depende del cliente más que del producto, como en la venta mayorista, la lista por cliente se vuelve el centro del negocio: está aplicado a ese caso en [precio por cliente](../../Comercio-electronico/Comercio-B2B/precio-por-cliente.md).

> [!NOTE] Sin fuente todavía: si las condiciones deben tener vigencia (desde y hasta cuándo valen) en el registro del cliente; las fuentes leídas solo guardan el valor actual.
