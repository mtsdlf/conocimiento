---
resumen: >-
  Los tipos de orden son las variantes de la orden de compra que cambian qué se compromete y cómo se da por cumplido: la puntual, por una compra con cantidad, precio y fecha; la orden abierta y la orden contra contrato, que son el uso de un contrato marco; la de servicios, que se cumple con una aceptación en lugar de una recepción; y la de consignación, donde lo que llega sigue siendo del proveedor.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Dynamics 365 Supply Chain Management, Purchase agreements: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements"
  - "ERPNext, Blanket Order (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/blanket-order"
  - "Odoo 18, Blanket orders (según su resumen): https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/purchase/manage_deals/blanket_orders.html"
  - "Wikipedia, Purchase order, orden planificada (según su resumen): https://en.wikipedia.org/wiki/Purchase_order"
  - "SAP R/3 4.6C, Service Entry and Acceptance for Purchase Orders (según su resumen): https://help.sap.com/saphelp_46c/helpdata/en/76/5aa8010d3211d3836f0000e8a5eb64/content.htm"
  - "Wikipedia, Consignment (según su resumen): https://en.wikipedia.org/wiki/Consignment"
  - "ERPNext, Material Request, propósito de subcontratación (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/material-request"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (sección 3)"
aliases: [tipos de orden, tipos de orden de compra, purchase order types, orden puntual, orden estándar, standard purchase order, orden abierta, blanket order, blanket purchase order, orden contra contrato, liberación, release order, call-off, orden planificada, planned purchase order, orden de servicios, hoja de entrada de servicios, service entry sheet, consignación, consignment]
creado: 2026-11-27
revisado:
---

# Tipos de orden

Los tipos de orden son las variantes de la orden de compra que cambian qué se compromete y cómo se da por cumplido: la puntual, por una compra con cantidad, precio y fecha; la orden abierta y la orden contra contrato, que son el uso de un contrato marco; la de servicios, que se cumple con una aceptación en lugar de una recepción; y la de consignación, donde lo que llega sigue siendo del proveedor.

Todos comparten la forma de la [orden de compra](orden-de-compra.md): cabecera, renglones y los mismos tres ejes de estado. Lo que cambia es si la orden mueve algo o solo fija condiciones, y qué documento prueba que se cumplió.

| Tipo | Qué compromete | Qué prueba que se cumplió |
|---|---|---|
| Puntual | Una cantidad, a un precio, para una fecha | La recepción de la mercadería |
| Orden abierta | Un total por un período, a precio pactado, que se consume de a partes | Las órdenes contra contrato que salen de ella |
| Orden contra contrato | Una entrega concreta, con el precio del contrato | La recepción, como una puntual |
| De servicios | Un trabajo a realizar | La aceptación del servicio |
| En consignación | Que el proveedor deje mercadería que sigue siendo suya | El consumo, no la llegada |

La tabla es una síntesis de la base; ninguna fuente leída da una taxonomía completa de órdenes de compra.

## La orden puntual

La orden puntual pide una cantidad de un artículo, a un precio, para una fecha, y se cumple cuando llega. Ninguna fuente la define como tipo aparte: es lo que todas llaman simplemente orden de compra. Los demás tipos se explican por lo que le cambian.

## Orden abierta y orden contra contrato: el uso del contrato marco

Cuando se compra lo mismo todo el año, no conviene negociar cada orden. El [contrato marco](../Abastecimiento-estrategico/contrato-marco.md) fija el precio y las condiciones por un período; se decide y se negocia en Abastecimiento estratégico. Acá está su uso: las órdenes que lo consumen.

La documentación de un ERP grande lo describe así: un acuerdo que compromete a comprar una cantidad o un monto «by using multiple purchase orders over time», a cambio de precios y descuentos especiales. Admite cuatro compromisos: cantidad de un producto, monto de un producto, monto de una categoría o monto de cualquier producto. Tiene vigencia, se activa y se cierra, y cada orden que sale de él es una liberación (release).

Tres sistemas distintos coinciden en el mecanismo: un compromiso total, órdenes que se liberan contra él y un saldo de lo que falta pedir. En un sistema abierto, cada orden actualiza la cantidad ya pedida del acuerdo, y las canceladas no cuentan. Cada orden sigue necesitando su fecha de entrega, su depósito, sus impuestos y su aprobación; el acuerdo no exime de aprobar.

La base usa dos nombres para el lado de la orden. **Orden abierta** es el compromiso por un total, cargado como documento de compras, del que se va descontando lo pedido; muchos sistemas la llaman blanket order y la tratan como el mismo objeto que el acuerdo. **Orden contra contrato** es cada orden concreta que sale de ella o del contrato marco, con cantidad y fecha propias. Que la orden abierta y el contrato marco se distingan es criterio de la base; las fuentes los mezclan, y el artículo de Wikipedia sobre blanket purchase order no existe. Wikipedia sí define la orden planificada como un compromiso de largo plazo con un proveedor, con órdenes individuales que van fijando las cantidades.

### Las reglas que hacen valer el contrato

El ERP grande tiene dos políticas que definen qué tan firme es el acuerdo. «Max is enforced» impide que el total de las órdenes supere el compromiso. «Price and discount is fixed» hace que, si una orden trae otro precio, se rompa el vínculo y ese renglón no cuente para cumplir el compromiso. Suma montos mínimo y máximo por liberación.

El acuerdo se aplica al crear la orden, no después, y guarda una versión cada vez que se confirma. Y el contrato no se cierra solo: en el sistema abierto, el acuerdo «may not automatically close» al vencer. Alguien tiene que mirar el saldo al final del período, porque lo que no se pidió es un compromiso no cumplido con el proveedor (inferencia de la base).

## La orden de servicios

Un servicio no llega en un camión, así que no hay recepción que contar. En un ERP grande, lo realizado se registra en una hoja de entrada de servicios que referencia la orden, y «before the vendor can send an invoice, you need to accept the service». La factura se controla contra la hoja aceptada, y la orden puede tener apagado el indicador de recepción de mercadería.

En la página leída, quien registra el servicio también lo acepta. Que la aceptación la haga alguien distinto de quien contrató, por [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md), es lectura de la base y no dato de la fuente. Cómo se compara la aceptación con lo pedido está en [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md).

## La orden en consignación

En la consignación, el dueño legal de la mercadería es el consignante hasta que se vende, y se le paga solo después de vendida y cobrada. El artículo leído la describe desde la venta minorista, con el proveedor como consignante. Para el comprador, eso significa tener en su depósito stock que todavía no es suyo; el registro tiene que separar lo propio de lo del proveedor, y la deuda nace con el consumo y no con la llegada. Esa lectura es de la base.

> [!NOTE] Sin fuente todavía: la consignación vista desde el comprador (cómo se registra el stock del proveedor en el depósito propio y qué documento dispara la compra y la factura).

## Los bordes: subcontratación y compra de activos

La subcontratación, en que se le manda material a un tercero para que lo transforme, aparece como propósito de la solicitud en un sistema abierto. Es un paso de la fabricación y va al tema Producción, todavía no armado; acá solo interesa que termina en una orden al proveedor. La compra de una máquina es una orden puntual; su alta como activo está en [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md) y su vida, en Activos y mantenimiento, todavía no armado.

Del lado de la venta, el espejo de esta nota es [tipos de pedido](../../Relacion-con-clientes/Pedido-de-venta/tipos-de-pedido.md): el pedido abierto del vendedor es la orden abierta del comprador.
