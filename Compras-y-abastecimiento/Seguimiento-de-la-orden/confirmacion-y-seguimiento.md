---
resumen: >-
  La confirmación es la respuesta del proveedor a una orden de compra emitida, que acepta, rechaza o cambia el precio, la cantidad o la fecha; el seguimiento es lo que hace Compras después para que la entrega llegue cuando se confirmó. Entre las dos queda la fecha confirmada, que es la que usa el resto de la empresa para planificar.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Approve and confirm purchase orders (Dynamics 365 Supply Chain Management), secciones de revisión externa y confirmación: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation"
  - "Odoo 18, Request for quotation (Order Deadline, Expected Arrival; según su resumen): https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/purchase/manage_deals/rfq.html"
  - "Cornell LII, UCC § 2-207 (según su resumen): https://www.law.cornell.edu/ucc/2/2-207"
  - "Wikipedia, Advance ship notice (según su resumen): https://en.wikipedia.org/wiki/Advance_ship_notice"
  - "Wikipedia, Expediting (según su resumen): https://en.wikipedia.org/wiki/Expediting"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3.5 y 4.4.2.3: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), sección 6"
aliases: [confirmación de la orden, acuse del proveedor, acknowledgement, order acknowledgment, PO confirmation, fecha confirmada, confirmed date, seguimiento de entregas, expediting, activación de pedidos, aviso de despacho, advance ship notice, ASN, EDI 856, DESADV]
creado: 2026-11-27
revisado:
---

# Confirmación y seguimiento

La confirmación es la respuesta del proveedor a una orden de compra emitida, que acepta, rechaza o cambia el precio, la cantidad o la fecha; el seguimiento es lo que hace Compras después para que la entrega llegue cuando se confirmó. Entre las dos queda la fecha confirmada, que es la que usa el resto de la empresa para planificar.

Es el primer paso de [Seguimiento de la orden](seguimiento-de-la-orden.md), entre la orden emitida de [Orden de compra](../Orden-de-compra/orden-de-compra.md) y la [recepción contra lo pedido](recepcion-contra-lo-pedido.md). APQC 7.4 lo nombra 4.2.3.5 «Expedite orders and satisfy inquiries».

## Lo que el proveedor contesta

En la documentación de un ERP grande, después de aprobar la orden se le puede hacer una consulta al proveedor sobre precios, descuentos o fechas, y la orden queda en revisión externa. Si el proveedor tiene un portal, aprueba o rechaza ahí; el rechazo trae un motivo y sugerencias de cambio, y la orden sigue en revisión hasta resolverlo. La confirmación registra la orden como comprometida y guarda una copia exacta de lo confirmado. Así queda un historial de versiones, que [cambios y cancelaciones](../Orden-de-compra/cambios-y-cancelaciones-de-la-orden.md) usa cuando la orden se modifica.

Otro sistema, según su resumen, pone dos fechas en el pedido. Una es la fecha límite para que el proveedor confirme que va a entregar; la otra, la llegada esperada, se calcula con esa fecha y el [plazo de entrega](../Proveedores/condiciones-del-proveedor.md) del proveedor. También deja pedirle por correo que confirme la fecha de envío.

> [!NOTE] Sin fuente todavía: qué se hace cuando la fecha confirmada difiere de la pedida (aceptarla, buscar otro proveedor, avisar a quien pidió) y quién lo decide. Las fuentes leídas solo muestran los dos campos.

## Un acuse con términos propios también obliga

El acuse no es solo un trámite. En el derecho de los Estados Unidos (UCC § 2-207, según su resumen), una confirmación escrita enviada en tiempo razonable vale como aceptación aunque traiga términos distintos, salvo que la aceptación se condicione expresamente a ellos. Entre comerciantes, los términos agregados entran al contrato salvo excepciones. Es una sola fuente y un solo régimen; lo que vale en la Argentina va en [Compras y abastecimiento en la Argentina](../compras-y-abastecimiento-en-argentina.md). Para un sistema, la consecuencia es guardar el acuse tal como llegó, no solo marcar la orden como confirmada (inferencia de la base).

## El aviso de despacho y la persecución de entregas

El aviso de despacho (advance ship notice) avisa qué entregas vienen, ligadas a una lista de empaque. Según su resumen en Wikipedia, suele viajar por intercambio electrónico, como EDI 856 (X12) o DESADV (EDIFACT), y puede detallar el pedido, la mercadería, el embalaje, el transportista y el código de cada unidad. Le sirve al depósito que recibe: escanea en lugar de desembalar y ve antes de la descarga las diferencias entre lo esperado y lo enviado.

El seguimiento (expediting) es asegurar que lo comprado llegue a tiempo y con la calidad pedida. La misma enciclopedia lo describe con cuatro niveles de control (producción, calidad, embalaje y transporte, y proyecto), típicos de proyectos grandes como astilleros o refinerías; la página pide más citas.

> [!NOTE] Sin fuente todavía: una fuente de práctica sobre cómo se organiza el seguimiento en una empresa común (a qué órdenes se les hace, con qué anticipación se llama al proveedor, cuándo se escala). Ningún libro de texto se leyó para este componente.

Si la entrega llega tarde o incompleta, el registro de la fecha confirmada y de la fecha real alimenta la [evaluación de proveedores](../Proveedores/evaluacion-de-proveedores.md), donde se mide el cumplimiento de las entregas. Lo que vigila el flujo de entrada desde el lado de la logística (APQC 4.4.2.3) es de Cadena de suministro y logística, todavía no armado.
