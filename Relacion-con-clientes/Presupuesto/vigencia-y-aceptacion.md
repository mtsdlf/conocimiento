---
resumen: >-
  Un presupuesto vale hasta una fecha que dice él mismo; antes de esa fecha se puede revisar (llevar un historial de versiones solo se encontró documentado para los acuerdos de un ERP grande), y el cliente lo acepta firmándolo, mandando su orden de compra o pagando una seña. Con la aceptación se convierte en pedido de venta, y hay que decidir qué precio rige si cambió en el medio.
estado: vigente
estabilidad: estable
fuentes:
  - "ERPNext, Quotation (Valid Till, estado Expired, conversión a Sales Order): https://docs.frappe.io/erpnext/user/manual/en/quotation"
  - "ERPNext, Sales Order (referencia y fecha de la orden de compra del cliente): https://docs.frappe.io/erpnext/user/manual/en/sales-order"
  - "Odoo 18, Quotation deadlines: https://www.odoo.com/documentation/18.0/applications/sales/sales/sales_quotations/deadline.html"
  - "Odoo 17, Get a signature to validate: https://www.odoo.com/documentation/17.0/applications/sales/sales/send_quotations/get_signature_to_validate.html"
  - "Odoo 17, Invoicing policy: https://www.odoo.com/documentation/17.0/applications/sales/sales/invoicing/invoicing_policy.html"
  - "Odoo 19, Create quotations (validez por defecto; bloquear pedidos confirmados): https://www.odoo.com/documentation/19.0/applications/sales/sales/sales_quotations/create_quotations.html"
  - "Microsoft Dynamics 365 SCM, Sales agreements overview (historial de versiones al confirmar; precio fijo): https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements"
  - "Microsoft Dynamics 365 Business Central, Work with blanket sales orders (prepago): https://learn.microsoft.com/en-CA/dynamics365/business-central/sales-how-to-create-blanket-sales-orders"
  - "APQC, Process Classification Framework 7.4, 3.5.3.14 «Revise bid/proposal/quote»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Relacion-con-clientes/.investigacion/presupuesto-y-pedido.md (secciones A y D)"
aliases: [validez del presupuesto, vigencia de la oferta, quote validity, valid until, aceptación del presupuesto, quote acceptance, versión del presupuesto, revisión del presupuesto, seña, anticipo, down payment, orden de compra del cliente, customer purchase order]
creado: 2026-11-27
revisado: 2026-11-27
---

# Vigencia y aceptación

Un presupuesto vale hasta una fecha que dice él mismo; antes de esa fecha se puede revisar (llevar un historial de versiones solo se encontró documentado para los acuerdos de un ERP grande), y el cliente lo acepta firmándolo, mandando su orden de compra o pagando una seña. Con la aceptación se convierte en pedido de venta, y hay que decidir qué precio rige si cambió en el medio.

Es el final de la vida del [presupuesto](presupuesto.md) y el comienzo del [pedido de venta](../Pedido-de-venta/pedido-de-venta.md).

## Hasta cuándo vale un presupuesto

La fecha de validez es un campo de la cabecera: el último día en que la oferta vale. Pasada esa fecha sin respuesta, el presupuesto pasa a vencido, como en un sistema abierto. Otro toma la validez de una configuración general, o de la plantilla de presupuesto que se usó, y deja cambiarla antes de enviar. Ese mismo sistema muestra la fecha de vencimiento en la vista que recibe el cliente: la validez es parte de la oferta, no un dato interno.

La validez protege a quien vende de dos cosas: que cambien sus costos y que el cliente acepte meses después una oferta que ya no puede cumplir. Por eso el plazo suele ser más corto donde los precios se mueven rápido, como en una economía con inflación alta. Esto último es criterio de la base.

En la Argentina, el art. 974 del Código Civil y Comercial dice que «La oferta obliga al proponente, a no ser que lo contrario resulte de sus términos, de la naturaleza del negocio o de las circunstancias del caso», y para ciertos servicios al consumidor la ley exige que el presupuesto diga el plazo para aceptarlo; el detalle está en [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md).

## Revisar un presupuesto: versiones

APQC tiene un paso propio para esto: «Revise bid/proposal/quote» (3.5.3.14). El cliente pide sacar un renglón, cambiar una cantidad o un descuento, y la empresa manda otra oferta. Hay dos maneras de registrarlo:

- **Editar el mismo presupuesto.** Simple, pero se pierde lo que se ofreció antes, y si el cliente acepta «el del martes» no hay cómo saber cuál era.
- **Crear una versión nueva y dejar la anterior como reemplazada.** Cada versión conserva lo que dijo y la oportunidad muestra la historia. Un ERP de un proveedor grande hace algo parecido con los acuerdos con clientes: al confirmar uno, guarda la versión vigente en una tabla de historial y permite imprimir todas las revisiones.

Para el presupuesto, conviene la segunda en cuanto el documento se envió: lo que el cliente tiene en la mano no debería cambiar sin que quede rastro. Esto es criterio de la base.

> [!NOTE] Sin fuente todavía: cómo numeran y guardan las versiones de un presupuesto los sistemas abiertos (no apareció en su documentación).

## Cómo acepta el cliente

| Forma | Qué deja registrado | Cuándo es la habitual |
|---|---|---|
| Firma | La conformidad del cliente sobre la versión que firmó | Servicios, obras, ventas a consumidores |
| Orden de compra del cliente | El número y la fecha del documento del cliente, que el pedido guarda | Ventas a empresas con un área de compras |
| Seña o anticipo | Un cobro que confirma la operación | Productos a medida, ventas a consumidores |
| Aceptación verbal o por mensaje | Nada, salvo que alguien la anote | Comercios chicos; es la que más se discute después |

La columna de cuándo es habitual cada forma es criterio de la base.

Un sistema abierto deja aceptar en línea: el cliente abre el presupuesto en un portal, firma y, si corresponde, paga; al firmar, el vendedor recibe el aviso de que el pedido quedó confirmado. Otro sistema guarda en el pedido la referencia y la fecha de la orden de compra del cliente; que sea lo que el cliente va a citar cuando reciba la factura es inferencia de la base. Un tercero deja registrar un prepago en el pedido marco (ver [tipos de pedido](../Pedido-de-venta/tipos-de-pedido.md)).

Cobrar antes de entregar también se decide por política. Un sistema abierto tiene dos: facturar lo pedido (se puede facturar apenas se confirma) o facturar lo entregado (primero hay que validar la entrega). Que la seña sea un caso del primero es criterio de la base. Qué es la seña en la ley argentina está en [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md); cómo se registra el cobro es de Tesorería y Contabilidad.

## Del presupuesto aceptado al pedido

Aceptar es convertir. En un diseño, el presupuesto confirmado pasa a ser el pedido; en el otro, se crea un pedido que copia los renglones y guarda la referencia (los dos diseños están en [presupuesto](presupuesto.md)). Si el presupuesto tenía renglones alternativos, un sistema abierto puede preguntar cuál eligió el cliente. La fecha de entrega que decía el presupuesto pasa al pedido como fecha prometida, salvo que la disponibilidad diga otra cosa al confirmar (criterio de la base; ver [fecha prometida](../Pedido-de-venta/fecha-prometida.md)).

Después de convertir, conviene que lo confirmado no se pueda editar sin un procedimiento: un sistema abierto tiene una opción para bloquear los pedidos confirmados. Cómo se cambia un pedido después está en [cambios y cancelaciones](../Pedido-de-venta/cambios-y-cancelaciones.md).

## Qué precio rige si cambió en el medio

Si la lista de precios cambia mientras el presupuesto está vigente, la regla más defendible es que rige el precio del presupuesto: es lo que se ofreció y lo que el cliente aceptó. Eso pide que el pedido copie los precios del presupuesto en lugar de volver a buscarlos en la lista. Esto es criterio de la base; las fuentes leídas no lo dicen así.

Lo que sí documentan: en un sistema abierto, la lista solo sugiere precios, que se pueden pisar en el pedido; en un ERP de un proveedor grande, cuando un pedido sale de un acuerdo con precio fijo, cambiar el precio del renglón rompe el vínculo con el acuerdo.

> [!NOTE] Sin fuente todavía: qué hacen los sistemas con un presupuesto vencido que el cliente acepta tarde (reabrirlo, emitir una versión nueva o rechazarlo).
