---
resumen: >-
  La logística inversa es mover la mercadería desde su destino final de vuelta hacia atrás en la cadena, para recuperar valor o descartarla como corresponde: devoluciones de clientes, rechazos en la entrega, envases y pallets retornables, retiros del mercado. Empieza con una autorización de devolución y termina en una disposición, que decide si lo devuelto vuelve al stock, se repara, se desarma o se da de baja.
estado: vigente
estabilidad: estable
fuentes:
  - "Wikipedia, Reverse logistics (según el resumen; la definición la atribuye a la Reverse Logistics Association): https://en.wikipedia.org/wiki/Reverse_logistics"
  - "Wikipedia, Return merchandise authorization (según el resumen): https://en.wikipedia.org/wiki/Return_merchandise_authorization"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.4.1.7 «Define reverse logistics strategy», 4.4.2.4 «Manage flow of returned products», 4.4.2.5 «Manage disposition of returned products» (4.4.2.5.1 a 4.4.2.5.4), 6.4.5 y 10.4.4: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Rogers, D. S. y Tibben-Lembke, R. S. (1999), Going Backwards: Reverse Logistics Trends and Practices, RLEC Press, Pittsburgh; no leído, fecha según las listas de referencias de Crossref: https://api.crossref.org/works/10.1108/13598540210447719 y https://api.crossref.org/works/10.1002/j.2158-1592.2001.tb00007.x"
  - "Rogers, D. S. y Tibben-Lembke, R. S. (2001), An examination of reverse logistics practices, Journal of Business Logistics 22(2), según el abstract del registro: https://doi.org/10.1002/j.2158-1592.2001.tb00007.x"
  - "UN/EDIFACT, mensaje DESADV, directorio D.96A, sección de principios (aviso de devolución), en un espejo de un vendedor: https://www.stylusstudio.com/edifact/D96A/DESADV.htm"
  - "Apache OFBiz, datos semilla de pedidos, estados, motivos y tipos de devolución: https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/data/seed/OrderSeedData.xml"
  - "Apache OFBiz, datos semilla de producto, tipos de envío: https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/data/seed/ProductSeedData.xml"
  - "Odoo 17.0, modelo de transferencias (return_id, default_location_return_id): https://raw.githubusercontent.com/odoo/odoo/17.0/addons/stock/models/stock_picking.py"
  - "ERPNext, nota de entrega, devolución y estado «Return Issued» (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/delivery-note"
  - "Cadena-de-suministro-y-logistica/.investigacion/despacho-y-entrega.md (componente logistica-inversa)"
  - "Cadena-de-suministro-y-logistica/.investigacion/despacho-y-entrega-2.md (componente logistica-inversa)"
aliases: [logística inversa, logística reversa, reverse logistics, devolución, devoluciones, returns, returns management, gestión de devoluciones, autorización de devolución, RMA, return merchandise authorization, RA, disposición, disposition, reacondicionado, refurbishment, retornables, envases retornables, pallets retornables, retiro del mercado, recall, reemplazo anticipado, cross-ship replacement]
creado: 2026-11-27
revisado: 2026-11-27
---

# Logística inversa

La logística inversa es mover la mercadería desde su destino final de vuelta hacia atrás en la cadena, para recuperar valor o descartarla como corresponde: devoluciones de clientes, rechazos en la entrega, envases y pallets retornables, retiros del mercado. Empieza con una autorización de devolución y termina en una disposición, que decide si lo devuelto vuelve al stock, se repara, se desarma o se da de baja.

Es el camino de vuelta de [Despacho y entrega](despacho-y-entrega.md). Arranca donde la [prueba de entrega](prueba-de-entrega.md) registra un rechazo, o después, cuando el cliente pide devolver. Lo devuelto reingresa al stock por la [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md#lo-que-no-pasa-la-inspección) de Inventario, que lo inspecciona como cualquier entrada. La devolución en una tienda online, con lo que cuesta y lo que obliga la ley de defensa del consumidor en la Argentina, está en [devoluciones](../../Comercio-electronico/Operaciones-del-comercio/devoluciones.md).

## Qué vuelve por la cadena

La definición que circula, citada por una fuente secundaria a la Reverse Logistics Association, es «the process of moving goods from their typical final destination for the purpose of capturing value, or proper disposal». Una obra que se cita como referencia del campo es *Going Backwards: Reverse Logistics Trends and Practices*, de Rogers y Tibben-Lembke (RLEC Press, 1999). Antes hubo una ponencia de los mismos autores en octubre de 1998, y en 2001 publicaron un artículo que, según su abstract, desarrolla «a working definition of reverse logistics». Ni el libro ni el artículo se leyeron, y la definición de los autores no se pudo verificar.

La misma fuente secundaria cita a Rogers (2002) para decir que el campo no se agota en las devoluciones: abarca «activities related to returns avoidance, gatekeeping, disposal, and all other after-market supply chain issues».

Lo que vuelve tiene destinos distintos; los destinos son los que lista la misma fuente, y los ejemplos y el agrupamiento son de la base:

| Qué vuelve | Ejemplo | Destino posible |
|---|---|---|
| Devolución del cliente | no lo quería, llegó fallado, talle equivocado | reacondicionado o remanufacturado, reventa en un mercado secundario |
| Rechazo en la entrega | el destinatario no lo recibe, un contra reembolso rechazado | vuelta al origen y reingreso al stock |
| Devolución por crédito | diarios y revistas no vendidos | crédito al comercio |
| Envases y embalajes de circuito cerrado | pallets, cajones, barriles | reutilización |
| Producto al final de su vida | aparatos eléctricos y electrónicos | reciclado; en Europa, la directiva de residuos eléctricos hace responsable al productor, según la misma fuente (la norma no se leyó) |

> [!NOTE] Sin fuente todavía: el retiro del mercado (recall) como flujo logístico, que APQC solo nombra en otra categoría («6.4.5 Monitor and audit recall effectiveness»); la gestión de envases retornables con saldo por cliente; y tasas de devolución por industria con fuente primaria y año.

## La autorización de devolución

La devolución empieza antes de que el producto se mueva: alguien la autoriza. Una fuente secundaria describe la autorización de devolución (RMA, return merchandise authorization) como «a part of the process of returning a product to receive a refund, replacement, or repair», y agrega que «The issuance of an RMA is a key gatekeeping point in the reverse logistics cycle». Se emite antes de que el cliente renuncie a la propiedad del producto.

Autorizar es filtrar. Lo que no se autoriza no se mueve, y lo que se autoriza llega identificado: qué es, de qué venta, por qué vuelve y qué espera el cliente. Esa lectura es de la base.

La resolución puede adelantarse a la devolución. La misma fuente menciona el reemplazo anticipado, que se manda antes de recibir el original. Uno de los sistemas abiertos lo tiene como tipos de resolución propios, «Cross-Ship Replacement» y «Replace Immediately».

## La disposición: qué se hace con lo devuelto

APQC 7.4 trata lo devuelto como un flujo de entrada, dentro de 4.4.2 «Plan and manage inbound material flow». Tiene un paso para el movimiento, 4.4.2.4 «Manage flow of returned products», y otro para decidir qué se hace, 4.4.2.5 «Manage disposition of returned products», con cuatro tareas:

1. 4.4.2.5.1 «Determine quality of controlled part»: inspeccionar.
2. 4.4.2.5.2 «Perform salvage activities»: rescatar lo que sirve.
3. 4.4.2.5.3 «Manage repair/refurbishment»: reparar o reacondicionar.
4. 4.4.2.5.4 «Return to finished goods inventory»: volver al stock de producto terminado.

La estrategia está más arriba, en 4.4.1.7 «Define reverse logistics strategy», y los centros de recolección de productos usados en otra categoría, 10.4.4 «Manage take-back centers».

La inspección y el estado en que queda lo que no pasa son de Inventario: la [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md) pone lo devuelto en un estado no disponible hasta decidir, y los estados están en [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md). La logística inversa se ocupa del viaje de vuelta y de la decisión de a dónde va.

## El viaje de vuelta

La devolución entre empresas usa el mismo aviso que el despacho. El texto del mensaje DESADV de UN/EDIFACT dice que «serves both as a specification for Delivery Despatch Advice and also as a Returns Despatch Advice message». El que devuelve avisa qué manda, con los mismos datos por bulto que en el [despacho](despacho.md).

Uno de los sistemas abiertos modela la devolución de venta como un tipo de envío entrante, al lado de la salida a cliente, la compra, la devolución a proveedor y el traslado. Es decir, el viaje de vuelta es otro envío, con su transportista y su seguimiento.

## Lo que un sistema guarda de una devolución

Los tres sistemas abiertos consultados coinciden en el patrón: la devolución es un documento propio, vinculado al original, con su estado y su motivo. El agrupamiento es de la base.

- Autorización: cliente, venta o despacho de origen, renglones con cantidad (nunca más de lo entregado), motivo y resolución pedida.
- Motivos: uno de los sistemas trae «Did Not Want Item», «Defective Item», «Mis-Shipped Item», «Digital Fulfillment Failed», «COD Payment Rejected», «Size Exchange» y «Normal Return».
- Resolución: el mismo sistema trae, entre otras, «Store Credit», «Refund», «Wait Replacement», «Cross-Ship Replacement» y «Repair Replacement».
- Estados: el mismo sistema usa «Requested», «Accepted», «Received», «Completed», «Manual Refund Required» y «Cancelled» para la devolución de un cliente. El paso «Received» va antes de «Completed»: el reembolso o el reemplazo se cierra después de recibir. Para la devolución a un proveedor usa «Requested», «Accepted», «Shipped», «Completed» y «Cancelled».
- Vínculo con el original: otro sistema vincula cada devolución al documento de salida del que sale («Return of») y tiene una ubicación de devoluciones por defecto. Un tercero, según su resumen, marca la nota de entrega original como «Return Issued» cuando se devolvió todo.
- Disposición: resultado de la inspección y destino (stock, reparación, rescate de partes, baja), cada uno como un movimiento de stock nuevo.

La plata de la devolución (la nota de crédito, el reembolso) no es de este tema: el documento de devolución la dispara, pero se registra en ventas y en Contabilidad (criterio de la base).

## Fallas de la logística inversa

Estas fallas son criterio de la base:

- Se recibe sin autorización. Llega un bulto que nadie esperaba, sin saber de qué venta es ni qué quiere el cliente.
- Lo devuelto vuelve directo a disponible. Sin inspección, se vuelve a vender algo fallado.
- La devolución edita el despacho original. Se pierde qué se entregó y qué volvió; tienen que ser dos documentos.
- Se mide la entrega y no la vuelta. Una devolución por envío equivocado es una falla del despacho, y el [nivel de servicio logístico](nivel-de-servicio-logistico.md) la tiene que ver.
