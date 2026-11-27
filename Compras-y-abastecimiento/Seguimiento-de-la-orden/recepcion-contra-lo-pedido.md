---
resumen: >-
  La recepción contra lo pedido es la comparación, renglón por renglón, de lo que el depósito contó al recibir con lo que dice la orden de compra. Lo que coincide dentro de la tolerancia da por cumplido el renglón; lo que falta queda como saldo pendiente, hasta que llega o hasta que alguien cierra el renglón.
estado: borrador
estabilidad: semi
fuentes:
  - "SAP, Underdeliveries, Overdeliveries, and Final Deliveries (versión 4.6C; según su resumen): https://help.sap.com/saphelp_46c/helpdata/en/a5/63343943a211d189410000e829fbbd/content.htm"
  - "SAP Learning, Applying Tolerances and the Delivery Completed Indicator (solo resultado de búsqueda): https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/applying-tolerances-and-the-delivery-completed-indicator"
  - "ERPNext, Purchase Receipt (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt"
  - "ERPNext, Purchase Order (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-order"
  - "Microsoft Learn, Approve and confirm purchase orders (Dynamics 365 Supply Chain Management), «Deliver remainder»: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3.6 «Reconcile purchase orders»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), sección 7"
aliases: [recepción contra lo pedido, recepción contra la orden, recepción contra orden de compra, cruce de dos vías, two-way match, goods receipt against purchase order, tolerancia, tolerancia de recepción, tolerance, subentrega, underdelivery, sobreentrega, overdelivery, entrega parcial, partial delivery, saldo pendiente, backorder, deliver remainder, entrega completa, delivery completed, cierre de la orden]
creado: 2026-11-27
revisado:
---

# Recepción contra lo pedido

La recepción contra lo pedido es la comparación, renglón por renglón, de lo que el depósito contó al recibir con lo que dice la orden de compra. Lo que coincide dentro de la tolerancia da por cumplido el renglón; lo que falta queda como saldo pendiente, hasta que llega o hasta que alguien cierra el renglón.

Es el centro de [Seguimiento de la orden](seguimiento-de-la-orden.md) y el punto donde termina el trabajo de Compras. APQC 7.4 lo llama 4.2.3.6 «Reconcile purchase orders». Lo que no coincide y no se resuelve con la tolerancia pasa a [diferencias y devoluciones](diferencias-y-devoluciones.md).

## Dos comparaciones, de dos dominios

El depósito cuenta, inspecciona y ubica lo que llega; eso es de Inventario y depósitos, en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md). Compras toma ese conteo y lo compara con la orden en cantidad: es un cruce de dos vías, orden contra recepción. Contabilidad hace después el [cruce de tres vías](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md#el-cruce-de-tres-vías-visto-desde-el-registro), que suma la factura y controla precio y cantidad facturada.

En un ERP abierto, según su resumen, el recibo se crea normalmente desde la orden y trae el proveedor, los renglones, las cantidades, los precios y los impuestos. Al confirmarlo, actualiza la cantidad y el porcentaje recibido de la orden, pero no crea la deuda con el proveedor: la crea la factura. Que el recibo apunte a la orden es lo que permite la comparación; un ingreso de mercadería suelto, sin orden, obliga a hacerla a mano (inferencia de la base).

## La tolerancia decide qué diferencia se acepta sola

Una tolerancia es el margen, en porcentaje, dentro del cual lo recibido se acepta como si fuera lo pedido. Un ERP grande, en una versión de los años noventa y según su resumen, trata distinto los dos lados:

- **Subentrega.** Por defecto se permite y se toma como entrega parcial, con un aviso. Si el renglón tiene tolerancia de subentrega, lo recibido dentro de ella se acepta sin aviso.
- **Sobreentrega.** Por defecto no se permite y da error. Se habilita con un porcentaje de tolerancia o con una marca de «ilimitada»; lo que supera la cantidad más la tolerancia se rechaza.

Las tolerancias se fijan en el maestro del artículo, en el registro artículo-proveedor o en el renglón de la orden, y el maestro vale por defecto. El registro artículo-proveedor está en [condiciones del proveedor](../Proveedores/condiciones-del-proveedor.md). Un ERP abierto tiene un porcentaje de sobrerrecepción que bloquea lo que lo supera, y aconseja revisar primero la unidad de compra y su conversión. Una caja de 12 cargada como unidad dispara la tolerancia aunque la mercadería sea la correcta.

> [!NOTE] Sin fuente todavía: la tolerancia de precio (que es del cruce de la factura, no de la recepción) y qué se hace con una entrega anticipada, que llega antes de la fecha confirmada.

## Entregas parciales y saldo pendiente

Una orden puede recibirse en varias entregas: cada recibo descuenta del renglón y la orden queda abierta por el resto. Ese resto es el saldo pendiente. Un ERP grande lo muestra como «Deliver remainder» y deja cambiarlo en un renglón en borrador; un ERP abierto mantiene la orden abierta hasta que todo está recibido o hasta que se la cierra.

> [!NOTE] Sin fuente todavía: una definición del saldo pendiente (backorder) del lado del comprador. Ninguna fuente leída de órdenes de compra usa esa palabra.

Con «pedimos 100 y llegaron 90», el renglón queda con 90 recibidas y 10 de saldo. Si el depósito apartó 2 por rotas, el cálculo depende de qué hace la empresa con ellas: si pide reposición, el saldo sube a 12; si pide crédito, sigue en 10 y las 2 salen por devolución. Ese reparto es criterio de la base y se decide en [diferencias y devoluciones](diferencias-y-devoluciones.md).

## Cerrar el renglón aunque no llegó todo

Cerrar con saldo es decidir que el resto no va a llegar. En el ERP grande eso es una marca de entrega completa: la cantidad abierta pasa a cero aunque falte mercadería, y aun así se pueden registrar recibos posteriores. La marca se pone sola cuando se recibe todo o se entra en la tolerancia, o a mano. Si una devolución baja lo entregado por debajo de la tolerancia, el sistema la quita y avisa. En el ERP abierto, cerrar la orden significa que el resto no se procesará, y no revierte lo ya registrado por recibos y facturas.

Cerrar no es cancelar. Cancelar el resto de una orden confirmada es un cambio de la orden y está en [cambios y cancelaciones](../Orden-de-compra/cambios-y-cancelaciones-de-la-orden.md). Cerrar el renglón es lo que hace Compras cuando acepta que la diferencia queda así. Un saldo que nadie cierra hace que la orden figure como compra en camino, y que quien planifica cuente con mercadería que no viene (inferencia de la base).

## Los servicios no se cuentan

Un servicio no llega en un camión: en lugar de un recibo se registra una aceptación del servicio prestado, que referencia la orden y contra la que se controla la factura. Está en [tipos de orden](../Orden-de-compra/tipos-de-orden.md).
