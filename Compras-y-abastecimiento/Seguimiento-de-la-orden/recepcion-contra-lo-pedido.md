---
resumen: >-
  La recepción contra lo pedido es la comparación, renglón por renglón, de lo que el depósito contó al recibir con lo que dice la orden de compra. Lo que coincide dentro de la tolerancia da por cumplido el renglón; lo que falta queda como saldo pendiente, hasta que llega o hasta que alguien cierra el renglón.
estado: vigente
estabilidad: semi
fuentes:
  - "SAP, Underdeliveries, Overdeliveries, and Final Deliveries (versión 4.6C; según su resumen): https://help.sap.com/saphelp_46c/helpdata/en/a5/63343943a211d189410000e829fbbd/content.htm"
  - "SAP Learning, Applying Tolerances and the Delivery Completed Indicator (solo resultado de búsqueda): https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/applying-tolerances-and-the-delivery-completed-indicator"
  - "ERPNext, Purchase Receipt (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt"
  - "ERPNext, Purchase Order (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-order"
  - "Microsoft Learn, Approve and confirm purchase orders (Dynamics 365 Supply Chain Management), «Deliver remainder»: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3.6 «Reconcile purchase orders»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), sección 7"
aliases: [recepción contra lo pedido, recepción contra la orden, recepción contra orden de compra, goods receipt against purchase order, tolerancia, tolerancia de recepción, tolerance, subentrega, underdelivery, sobreentrega, overdelivery, entrega parcial, partial delivery, saldo pendiente, open quantity, quantity on order, remaining quantity, deliver remainder, entrega completa, delivery completed, cierre de la orden, cerrar el renglón]
creado: 2026-11-27
revisado: 2026-11-27
---

# Recepción contra lo pedido

La recepción contra lo pedido es la comparación, renglón por renglón, de lo que el depósito contó al recibir con lo que dice la orden de compra. Lo que coincide dentro de la tolerancia da por cumplido el renglón; lo que falta queda como saldo pendiente, hasta que llega o hasta que alguien cierra el renglón.

Es el centro de [Seguimiento de la orden](seguimiento-de-la-orden.md) y el punto donde termina el trabajo de Compras. El paso de APQC 7.4 que más se le parece es 4.2.3.6 «Reconcile purchase orders» (lectura de esta base). Lo que no coincide y no se resuelve con la tolerancia pasa a [diferencias y devoluciones](diferencias-y-devoluciones.md).

## Dos comparaciones, de dos dominios

El depósito cuenta, inspecciona y ubica lo que llega; eso es de Inventario y depósitos, en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md). Compras toma ese conteo y lo compara con la orden en cantidad. Contabilidad hace después el [cruce de tres vías](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md#el-cruce-de-tres-vías-visto-desde-el-registro), que suma la factura y controla precio y cantidad facturada.

En un ERP abierto, según su resumen, el recibo se crea normalmente desde la orden y trae el proveedor, los renglones, las cantidades, los precios y los impuestos. Al confirmarlo, actualiza la cantidad y el porcentaje recibido de la orden, pero en ese sistema no crea la deuda con el proveedor: la crea la factura de compra. La deuda la registra Contabilidad: al recibir, como recibido sin facturar, y se confirma con la factura ([compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md#lo-recibido-sin-facturar)). Que el recibo apunte a la orden es lo que permite la comparación; un ingreso de mercadería suelto, sin orden, obliga a hacerla a mano (inferencia de la base).

## La tolerancia decide qué diferencia se acepta sola

La tolerancia de recepción es el margen, en porcentaje, dentro del cual la cantidad recibida se acepta como si fuera la pedida. Un ERP grande, en una versión antigua y según su resumen, trata distinto los dos lados:

- **Subentrega.** Por defecto se permite y se toma como entrega parcial, con un aviso. Si el renglón tiene tolerancia de subentrega, lo recibido dentro de ella se acepta sin aviso.
- **Sobreentrega.** Por defecto no se permite y da error. Se habilita con un porcentaje de tolerancia o con una marca de «ilimitada»; lo que supera la cantidad más la tolerancia se rechaza.

Las tolerancias se fijan en el maestro del artículo, en el registro artículo-proveedor o en el renglón de la orden, y el maestro vale por defecto (esto último según un resultado de búsqueda de otra página del mismo fabricante). El registro artículo-proveedor y la unidad de compra están en [condiciones del proveedor](../Proveedores/condiciones-del-proveedor.md). Un ERP abierto, según su resumen, tiene un porcentaje de sobrerrecepción que bloquea lo que lo supera, y aconseja revisar primero la unidad de compra y su conversión. Un ejemplo de la base: una caja de 12 cargada como unidad dispara la tolerancia aunque la mercadería sea la correcta.

> [!NOTE] Sin fuente todavía: qué se hace con una entrega anticipada, que llega antes de la fecha confirmada. La tolerancia de precio no es de la recepción: es del cruce de tres vías, en [compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md#el-cruce-de-tres-vías-visto-desde-el-registro).

## Entregas parciales y saldo pendiente

Una orden puede recibirse en varias entregas: cada recibo descuenta del renglón y la orden queda abierta por el resto. Ese resto es el saldo pendiente: lo pedido menos lo recibido. Un ERP grande lo lleva como la cantidad que falta entregar y deja cambiarla en un renglón en borrador; un ERP abierto, según su resumen, mantiene la orden abierta hasta que todo está recibido o hasta que se la cierra.

> [!NOTE] Sin fuente todavía: un nombre establecido para el saldo pendiente del lado del comprador. Ninguna fuente leída de órdenes de compra usa la palabra backorder, que en esta base es lo que se le debe a un cliente, del lado de la venta (como en [existencias](../../Inventario-y-depositos/Existencias/existencias.md)).

Lo rechazado no entra en esa cuenta: se resuelve aparte, por devolución, reposición o nota de crédito, y si se pide reposición el saldo vuelve a subir. Con «pedimos 100, llegaron 90, dos rotas», hay 90 recibidas (88 aceptadas y 2 rechazadas) y un saldo pendiente de 10. La orden queda abierta por 10, con 2 rechazadas sin resolver. Si se pide reposición de las 2, el saldo sube a 12; si se pide crédito, sigue en 10. Esta regla y el reparto son criterio de la base, y qué se pide por las rechazadas se decide en [diferencias y devoluciones](diferencias-y-devoluciones.md).

## Cerrar el renglón aunque no llegó todo

Cerrar es dejar de esperar el saldo pendiente: se decide que el resto no va a llegar. En el ERP grande eso es una marca de entrega completa: la cantidad abierta pasa a cero aunque falte mercadería, y aun así se pueden registrar recibos posteriores. La marca se pone sola cuando se recibe todo o se entra en la tolerancia, o a mano. Si una devolución baja lo entregado por debajo de la tolerancia, el sistema la quita y avisa. En el ERP abierto, según su resumen, cerrar la orden significa que el resto no se procesará, y se hace solo cuando el resto no se va a recibir ni a facturar.

Cerrar no es cancelar ni finalizar. Finalizar es el cierre administrativo o financiero de una orden ya completa. Cancelar el resto de una orden confirmada es un cambio de la orden y está en [cambios y cancelaciones](../Orden-de-compra/cambios-y-cancelaciones-de-la-orden.md). Cerrar el renglón es lo que hace Compras cuando acepta que la diferencia queda así. Un saldo que nadie cierra hace que la orden figure como compra en camino, y que quien planifica cuente con mercadería que no viene (inferencia de la base).

## Los servicios no se cuentan

Un servicio no llega en un camión: en lugar de un recibo se registra una hoja de aceptación de servicios, que referencia la orden y contra la que se controla la factura. Está en [tipos de orden](../Orden-de-compra/tipos-de-orden.md).
