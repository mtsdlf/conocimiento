---
resumen: >-
  La confirmación es la respuesta del proveedor a una orden de compra emitida, que acepta, rechaza o cambia el precio, la cantidad o la fecha; el seguimiento es lo que hace Compras después para que la entrega llegue cuando se confirmó. Entre las dos queda la fecha confirmada, que es la que promete el proveedor.
estado: vigente
estabilidad: semi
fuentes:
  - "Microsoft Learn, Approve and confirm purchase orders (Dynamics 365 Supply Chain Management), secciones de revisión externa y confirmación: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation"
  - "Odoo 18, Request for quotation (Order Deadline, Expected Arrival; según su resumen): https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/purchase/manage_deals/rfq.html"
  - "Cornell LII, UCC § 2-207 (texto leído): https://www.law.cornell.edu/ucc/2/2-207"
  - "Wikipedia, Purchase order (según su resumen): https://en.wikipedia.org/wiki/Purchase_order"
  - "ERPNext, Supplier Scorecard (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/supplier-scorecard"
  - "Wikipedia, Advance ship notice (según su resumen): https://en.wikipedia.org/wiki/Advance_ship_notice"
  - "Wikipedia, Expediting (según su resumen): https://en.wikipedia.org/wiki/Expediting"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3.5 y 4.4.2.3: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), sección 6"
aliases: [confirmación de la orden, acuse del proveedor, acknowledgement, order acknowledgment, PO confirmation, fecha confirmada, confirmed date, fecha requerida, fecha esperada, seguimiento de entregas, expediting, activación de pedidos, aviso de despacho, advance ship notice, ASN, EDI 856, DESADV]
creado: 2026-11-27
revisado: 2026-11-27
---

# Confirmación y seguimiento

La confirmación es la respuesta del proveedor a una orden de compra emitida, que acepta, rechaza o cambia el precio, la cantidad o la fecha; el seguimiento es lo que hace Compras después para que la entrega llegue cuando se confirmó. Entre las dos queda la fecha confirmada, que es la que promete el proveedor.

Es el primer paso de [Seguimiento de la orden](seguimiento-de-la-orden.md), entre la orden emitida de [Orden de compra](../Orden-de-compra/orden-de-compra.md) y la [recepción contra lo pedido](recepcion-contra-lo-pedido.md). El paso de APQC 7.4 que más se le parece es 4.2.3.5 «Expedite orders and satisfy inquiries» (lectura de esta base).

## Lo que el proveedor contesta

En la documentación de un ERP grande, después de aprobar la orden se le puede hacer una consulta al proveedor sobre precios, descuentos o fechas, y la orden queda en revisión externa, un estado entre la aprobada y la confirmada que figura en los [estados de la orden](../Orden-de-compra/orden-de-compra.md). Si el proveedor tiene un portal, aprueba o rechaza ahí; el rechazo trae un motivo y sugerencias de cambio, y la orden sigue en revisión hasta resolverlo. La confirmación registra la orden como comprometida y guarda una copia exacta de lo confirmado; qué pasa con esa copia cuando la orden cambia está en [cambios y cancelaciones](../Orden-de-compra/cambios-y-cancelaciones-de-la-orden.md).

Otro sistema, según su resumen, pone dos fechas en el pedido. Una es la fecha límite para que el proveedor confirme que va a entregar; la otra, la llegada esperada, se calcula con esa fecha y el [plazo de entrega](../Proveedores/condiciones-del-proveedor.md) del proveedor. También deja pedirle por correo que confirme la fecha de envío.

## Tres fechas

El tema usa tres nombres para tres fechas. La fecha requerida es la que pide quien compra y va en la orden. La fecha esperada es la que calcula el sistema: en el sistema recién descrito sale de la fecha límite de confirmación más el plazo de entrega. La fecha confirmada es la que promete el proveedor al acusar la orden. La separación en tres es criterio de la base; las fuentes leídas solo muestran campos de fecha en la orden y el cálculo de la esperada.

> [!NOTE] Sin fuente todavía: qué se hace cuando la fecha confirmada difiere de la requerida (aceptarla, buscar otro proveedor, avisar a quien pidió) y quién lo decide. Las fuentes leídas solo muestran los dos campos.

## Un acuse con términos propios también obliga

Según el resumen de Wikipedia, emitir una orden no forma por sí solo un contrato; sin contrato previo, lo forma la aceptación del vendedor. En el derecho de los Estados Unidos (UCC § 2-207(1), texto leído), una confirmación escrita enviada en tiempo razonable vale como aceptación aunque traiga términos adicionales o distintos, salvo que la aceptación se condicione expresamente a ellos. Esos términos se tratan como propuestas de agregado; entre comerciantes entran al contrato salvo que la oferta limite la aceptación a sus términos, que los altere de manera sustancial o que se los objete en un plazo razonable (§ 2-207(2)). Si las partes actúan como si hubiera contrato aunque los escritos no lo formen, el contrato existe y sus términos son los que coinciden en los escritos (§ 2-207(3)). Es una sola fuente y un solo régimen, el de los Estados Unidos; sin fuente todavía para la Argentina. Para un sistema, la consecuencia es guardar el acuse tal como llegó, no solo marcar la orden como confirmada (inferencia de la base).

## El aviso de despacho y el seguimiento de entregas

El aviso de despacho (advance ship notice) avisa qué entregas vienen, ligadas a una lista de empaque. Según su resumen en Wikipedia, suele viajar por intercambio electrónico, como EDI 856 (X12) o DESADV (EDIFACT), y puede detallar el pedido, la mercadería, el embalaje, el transportista y el código de cada unidad. Qué hace el depósito con el aviso está en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md).

El seguimiento de entregas (expediting) es asegurar que lo comprado llegue a tiempo y con la calidad pedida. Según su resumen, la misma enciclopedia lo describe con cuatro niveles de control (producción, calidad, embalaje y transporte, y proyecto), típicos de proyectos grandes como astilleros o refinerías; la página pide más citas.

> [!NOTE] Sin fuente todavía: una fuente de práctica sobre cómo se organiza el seguimiento en una empresa común (a qué órdenes se les hace, con qué anticipación se llama al proveedor, cuándo se escala). Ningún libro de texto se leyó para este componente.

Si la entrega llega tarde o incompleta, el registro de la fecha confirmada y de la fecha real alimenta la [evaluación de proveedores](../Proveedores/evaluacion-de-proveedores.md). Un tablero de un ERP abierto, según su resumen, mide el cumplimiento como entregas a tiempo sobre entregas totales. Lo que vigila el flujo de entrada desde el lado de la logística (APQC 4.4.2.3) está en [flujo de entrada](../../Cadena-de-suministro-y-logistica/Transporte/flujo-de-entrada.md), de Cadena de suministro y logística.
