---
resumen: >-
  Los tipos de orden son las variantes de la orden de compra que cambian qué se compromete y cómo se da por cumplido: la puntual, por una compra con cantidad, precio y fecha; la orden abierta, por un total o un período con entregas que se liberan de a poco; la orden contra contrato, que toma el precio y las condiciones de un contrato marco; la de servicios, que se cumple con una aceptación en lugar de una recepción; y la de consignación, donde lo que llega sigue siendo del proveedor.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft, Dynamics 365 Supply Chain Management, Purchase agreements: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements"
  - "ERPNext, Blanket Order (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/blanket-order"
  - "Odoo 18, Blanket orders (según su resumen): https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/purchase/manage_deals/blanket_orders.html"
  - "Wikipedia, Purchase order, orden planificada (según su resumen): https://en.wikipedia.org/wiki/Purchase_order"
  - "SAP R/3 4.6C, Service Entry and Acceptance for Purchase Orders (según su resumen): https://help.sap.com/saphelp_46c/helpdata/en/76/5aa8010d3211d3836f0000e8a5eb64/content.htm"
  - "Wikipedia, Consignment (según su resumen): https://en.wikipedia.org/wiki/Consignment"
  - "ERPNext, Material Request, propósito de subcontratación (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/material-request"
  - "ERPNext, Subcontracting (la orden de compra de subcontratación como primer documento): https://docs.frappe.io/erpnext/user/manual/en/subcontracting"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (sección 3)"
aliases: [tipos de orden, tipos de orden de compra, purchase order types, orden puntual, orden estándar, standard purchase order, orden abierta, blanket order, blanket purchase order, orden contra contrato, liberación, release order, call-off, orden planificada, planned purchase order, orden de servicios, hoja de aceptación de servicios, hoja de entrada de servicios, service entry sheet, consignación, consignment]
creado: 2026-11-27
revisado: 2026-11-27
---

# Tipos de orden

Los tipos de orden son las variantes de la orden de compra que cambian qué se compromete y cómo se da por cumplido: la puntual, por una compra con cantidad, precio y fecha; la orden abierta, por un total o un período con entregas que se liberan de a poco; la orden contra contrato, que toma el precio y las condiciones de un contrato marco; la de servicios, que se cumple con una aceptación en lugar de una recepción; y la de consignación, donde lo que llega sigue siendo del proveedor.

Todos comparten la forma de la [orden de compra](orden-de-compra.md): cabecera, renglones y los mismos tres ejes de estado. Lo que cambia es si la orden mueve algo o solo fija condiciones, y qué documento prueba que se cumplió.

| Tipo | Qué compromete | Qué prueba que se cumplió |
|---|---|---|
| Puntual | Una cantidad, a un precio, para una fecha | La recepción de la mercadería |
| Orden abierta | Un total o un período, con entregas que se liberan de a poco | Las entregas liberadas, cada una con su recepción |
| Orden contra contrato | Una entrega concreta, con el precio y las condiciones de un contrato marco | La recepción, como una puntual |
| De servicios | Un trabajo a realizar | La aceptación del servicio |
| En consignación | Que el proveedor deje mercadería que sigue siendo suya | El consumo, no la llegada |

La tabla es una síntesis de la base; ninguna fuente leída da una taxonomía completa de órdenes de compra.

## La orden puntual

La orden puntual pide una cantidad de un artículo, a un precio, para una fecha, y se cumple cuando llega. Ninguna fuente la define como tipo aparte: es lo que todas llaman simplemente orden de compra. Los demás tipos se explican por lo que le cambian.

## Orden abierta y orden contra contrato

Cuando se compra lo mismo todo el año, no conviene negociar cada orden. El [contrato marco](../Abastecimiento-estrategico/contrato-marco.md) fija el precio y las condiciones por un período; se decide y se negocia en Abastecimiento estratégico, y las reglas que lo hacen valer (vigencia, tope, saldo consumido, qué pasa con lo que no se consume) están en esa nota. Acá, qué toma de él cada orden y qué necesita.

**Orden abierta** es la orden de compra por un total o un período, con entregas que se liberan de a poco. **Orden contra contrato** es la orden que toma el precio y las condiciones de un contrato marco; también se la llama liberación, call-off o release. Varios sistemas llaman «blanket order» al documento que acá es el contrato marco, y no a la orden. Los tres sistemas leídos tratan el acuerdo y las órdenes que lo usan como objetos distintos, y la base sigue esa distinción. Wikipedia define la orden planificada como un compromiso de largo plazo con un proveedor, con órdenes individuales que van fijando las cantidades (según su resumen).

Lo que una orden hereda del contrato es el precio y las condiciones pactadas. Lo que sigue necesitando es su propia fecha de entrega, su depósito, sus impuestos y su aprobación: el contrato no exime de aprobar (según el resumen de la documentación de un sistema abierto). El ERP grande aplica el contrato al crear la orden, no después, y si el contrato tiene precio fijo, una orden con otro precio rompe el vínculo y ese renglón no cuenta para el compromiso. Cómo se lleva el saldo y qué pasa con lo no consumido está en [contrato marco](../Abastecimiento-estrategico/contrato-marco.md). Si el cambio llega después de emitida la orden, la regla está en [cambios y cancelaciones](cambios-y-cancelaciones-de-la-orden.md).

## La orden de servicios

Un servicio no llega en un camión, así que no hay recepción que contar. En un ERP grande, según el resumen de su documentación, lo realizado se registra en una hoja de aceptación de servicios (en ese sistema, «service entry sheet») que referencia la orden, y «before the vendor can send an invoice, you need to accept the service». La factura se controla contra la hoja aceptada, y la orden puede tener apagado el indicador de recepción de mercadería.

En la página leída, quien registra el servicio también lo acepta y no se nombra un aprobador aparte. Que la aceptación la haga alguien distinto de quien contrató, por [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md), es lectura de la base y no dato de la fuente. Cómo se compara la aceptación con lo pedido está en [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md).

## La orden en consignación

En la consignación, el dueño legal de la mercadería es el consignante hasta que se vende, y se le paga solo después de vendida y cobrada. El artículo leído la describe desde la venta minorista, con el proveedor como consignante. Para el comprador, eso significa tener en su depósito stock que todavía no es suyo, y el registro tiene que separar lo propio de lo del proveedor. La deuda la registra Contabilidad ([compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md)); la lectura de esta base es que, en una consignación, no corresponde registrarla al recibir sino cuando se consume o se vende lo recibido. Ninguna fuente leída lo confirma.

> [!NOTE] Sin fuente todavía: la consignación vista desde el comprador (cómo se registra el stock del proveedor en el depósito propio y qué documento dispara la compra y la factura).

## Los bordes: subcontratación y compra de activos

La subcontratación, en que se le manda material a un tercero para que lo transforme, aparece como propósito de la solicitud en un sistema abierto. Es un paso de la fabricación y está en [subcontratación](../../Produccion/Ejecucion-en-planta/subcontratacion.md), de Producción; acá solo interesa que termina en una orden al proveedor. La documentación de subcontratación del mismo sistema empieza por una orden de compra de subcontratación, cuyo precio es el del servicio y no el del producto. La compra de una máquina es una orden puntual (criterio de la base); su alta como activo está en [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md) y su vida, en [Activos y mantenimiento](../../Activos-y-mantenimiento/activos-y-mantenimiento.md), con el recorrido entero en [de la compra a la baja del activo](../../Procesos-de-negocio/de-la-compra-a-la-baja-del-activo.md).

Del lado de la venta, el espejo de esta nota es [tipos de pedido](../../Relacion-con-clientes/Pedido-de-venta/tipos-de-pedido.md): el pedido abierto del vendedor es la orden abierta del comprador.
