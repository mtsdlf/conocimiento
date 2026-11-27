---
resumen: >-
  El despacho es el documento que registra lo que sale hacia un destinatario: qué pedidos y bultos junta, con qué transportista y en qué viaje, y por qué estados pasa hasta la entrega. Lo acompañan una identificación por bulto (el SSCC de GS1, en la etiqueta logística) y, entre empresas, un aviso de despacho anticipado que le dice al destinatario qué le va a llegar.
estado: vigente
estabilidad: semi
fuentes:
  - "GS1 General Specifications Standard, Release 26.0, ratificada, enero de 2026, secciones 1.3.5, 2.2.1, 3.3.1, 4.3.1 y 6.6: https://ref.gs1.org/standards/genspecs/"
  - "UN/EDIFACT, mensaje DESADV (Despatch advice), directorio D.96A, secciones 0 a 4.1, en un espejo de un vendedor de software (el directorio oficial de UNECE no se pudo abrir): https://www.stylusstudio.com/edifact/D96A/DESADV.htm"
  - "X12, set de transacciones 856 «Ship Notice/Manifest», descripción: https://x12.org/products/transaction-sets"
  - "Wikipedia, Advance ship notice (según el resumen): https://en.wikipedia.org/wiki/Advance_ship_notice"
  - "Apache OFBiz, datos semilla de producto, tipos de envío, estados del envío (SHIPMENT_STATUS) y del segmento de ruta con el transportista (SHPRTSG_CS_STATUS), líneas 678 a 731: https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/data/seed/ProductSeedData.xml"
  - "Odoo 17.0, modelo de transferencias (stock.picking), estados y campos: https://raw.githubusercontent.com/odoo/odoo/17.0/addons/stock/models/stock_picking.py"
  - "Odoo 17.0, transferencias por lotes (stock.picking.batch), estados: https://raw.githubusercontent.com/odoo/odoo/17.0/addons/stock_picking_batch/models/stock_picking_batch.py"
  - "Odoo 17.0, métodos de envío con transportista (según el resumen): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.html"
  - "ERPNext, definiciones de Shipment, Delivery Trip y Delivery Stop: https://raw.githubusercontent.com/frappe/erpnext/develop/erpnext/stock/doctype/shipment/shipment.json (y delivery_trip/delivery_trip.json, delivery_stop/delivery_stop.json en la misma ruta)"
  - "ERPNext, nota de entrega y viaje de entrega (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/delivery-note y https://docs.frappe.io/erpnext/user/manual/en/delivery-trip"
  - "Cadena-de-suministro-y-logistica/.investigacion/despacho-y-entrega.md (componente despacho)"
  - "Cadena-de-suministro-y-logistica/.investigacion/despacho-y-entrega-2.md (componente despacho)"
aliases: [despacho, documento de despacho, nota de entrega, delivery note, orden de entrega, envío, shipment, expedición, viaje de entrega, hoja de ruta, delivery trip, aviso de despacho, aviso de despacho anticipado, aviso anticipado de envío, ASN, advance ship notice, DESADV, despatch advice, EDI 856, ship notice/manifest, SSCC, serial shipping container code, etiqueta logística, GS1 logistic label, unidad logística, logistic unit, GS1-128, seguimiento, tracking, número de guía]
creado: 2026-11-27
revisado: 2026-11-27
---

# Despacho

El despacho es el documento que registra lo que sale hacia un destinatario: qué pedidos y bultos junta, con qué transportista y en qué viaje, y por qué estados pasa hasta la entrega. Lo acompañan una identificación por bulto (el SSCC de GS1, en la etiqueta logística) y, entre empresas, un aviso de despacho anticipado que le dice al destinatario qué le va a llegar.

Es el primer paso de [Despacho y entrega](despacho-y-entrega.md). Toma el bulto que [preparación de pedidos](../../Inventario-y-depositos/Operacion-del-deposito/preparacion-de-pedidos.md) dejó listo para salir y termina cuando el destinatario lo recibe y conforma, que es la [prueba de entrega](prueba-de-entrega.md). Qué transportista se elige, cuánto cobra y por dónde va son de [Transporte](../Transporte/transporte.md).

En este tema, despacho nombra ese documento, y despachar, confirmar la salida. El envío es lo que se le entrega a un transportista; el viaje de entrega, el recorrido de un vehículo con varios despachos; y la entrega, el momento en que el destinatario recibe. El despacho aduanero es otro trámite y está en [aduana](../Comercio-exterior/aduana.md).

## Despacho, envío con el transportista y viaje de entrega

Los tres sistemas abiertos consultados no coinciden en los estados, pero sí en una forma: separan lo que sale, el trato con el transportista y el viaje. La lectura del patrón es de la base; no es una norma.

| Documento | Qué registra | Lo que se vio en los sistemas |
|---|---|---|
| Despacho | qué sale, para quién, desde qué depósito, en qué bultos | un documento de salida que viene de un pedido y admite salidas parciales; los sistemas lo llaman entrega, nota de entrega o transferencia |
| Envío con el transportista | la reserva con el transportista, la guía y el estado que informa el transportista | un estado propio de la reserva, separado del de la mercadería |
| Viaje de entrega | qué despachos van en un vehículo, en qué orden y con qué conductor | «A Delivery Trip records Customer Deliveries in one vehicle», según el manual de un ERP abierto (resumen) |

Un camión propio que reparte a diez clientes es un viaje de entrega con diez despachos; un paquete dado a un transportista es un despacho con un envío y sin viaje propio (inferencia de la base).

## Los estados que recorre

No hay un estándar de estados para el despacho. Cada sistema abierto corta en un grano distinto:

- Uno modela el envío entero en un solo estado: «Input», «Scheduled», «Picked», «Packed», «Shipped», «Delivered» y «Cancelled». Declara qué transiciones valen: se puede cancelar hasta «Picked», pero de «Packed» solo se pasa a «Shipped» y de ahí a «Delivered». Separa en otro estado la reserva con el transportista: «Not Started», «Confirmed», «Accepted», «Voided».
- Otro usa una transferencia genérica, que sirve también para recibir y mover dentro del depósito: «Draft», «Waiting Another Operation», «Waiting», «Ready», «Done», «Cancelled». No tiene «en tránsito» ni «entregado». Las transferencias se agrupan en un lote con estados «Draft», «In progress», «Done» y «Cancelled».
- El tercero separa tres documentos. El envío con transportista tiene «Draft», «Submitted», «Booked», «Cancelled» y «Completed», y aparte un estado de seguimiento: «In Progress», «Delivered», «Returned», «Lost». El viaje de entrega tiene «Draft», «Scheduled», «In Transit», «Completed» y «Cancelled».

Tres cosas salen de comparar (lectura de la base). El estado de la mercadería y el del trámite con el transportista van separados. «En tránsito» vive en el viaje de entrega o en el seguimiento, no en el documento de salida; como estado del stock entre depósitos propios, está en [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md). Y ninguno de los tres tiene un estado de entrega fallida o de reintento: el más cercano es el «Returned» o «Lost» del seguimiento.

> [!NOTE] Sin fuente todavía: un estándar de estados del envío en tránsito (en camino, fallido, reintento) y de eventos de seguimiento, y una fuente sobre la confirmación de salida, la carga del vehículo y el manifiesto de carga.

## El bulto se identifica con el SSCC

Cada bulto o pallet que viaja es, en el vocabulario de GS1, una unidad logística: «A logistic unit is an item of any composition established for transport and/or storage that needs to be managed through the supply chain». La identifica el SSCC (Serial Shipping Container Code), que según las especificaciones generales de GS1 es «the GS1 identifier for an individual logistic unit».

El SSCC tiene siempre 18 dígitos: un dígito de extensión, el prefijo de empresa GS1 con una referencia serial, y un dígito de control al final. El largo del prefijo varía, pero el total no. El dígito de extensión y la referencia serial los asigna quien arma el bulto. El prefijo hace al código único en el mundo, pero según GS1 «does not identify the origin of the unit». Se codifica con el identificador de aplicación «AI (00)».

La regla que más le importa a un sistema es la de no repetir: «an individual SSCC number must not be reallocated within one year of the shipment date from the SSCC assignor to a trading partner». Una norma o un sector pueden alargar ese plazo. Un generador de SSCC tiene que guardar los ya usados con su fecha de envío (inferencia de la base).

## La etiqueta logística

La etiqueta logística de GS1 hace legible el SSCC en el bulto (secciones 2.2.1, 3.3.1 y 6.6 de la especificación). Según la especificación, «The SSCC is the single mandatory element for all GS1 Logistic Labels». El código de barras obligatorio es GS1-128, y se puede sumar un GS1 DataMatrix o un QR de GS1.

La etiqueta se arma en segmentos para el proveedor, el cliente y el transportista, y «Each label segment may be applied to the logistic unit at a different point in time as the relevant information becomes known». Así, el bulto puede salir del embalaje con el SSCC y recibir después los datos del transportista (lectura de la base). El SSCC es la clave que une el bulto físico con lo que viaja por intercambio electrónico de datos (EDI).

## El aviso de despacho anticipado

Entre empresas, el que despacha le avisa al que recibe qué le manda antes de que llegue. En UN/EDIFACT es el mensaje DESADV: «A message specifying details for goods despatched or ready for despatch under agreed conditions». En el estándar X12 es el set 856, «Ship Notice/Manifest». En inglés se lo llama ASN (advance ship notice), según una fuente secundaria.

Según la descripción de X12, el 856 lista «the contents of a shipment of goods as well as additional information relating to the shipment, such as order information, product description, physical characteristics, type of packaging, marking, carrier information, and configuration of goods within the transportation equipment». El DESADV, según su texto, se refiere a un vendedor y un comprador, y a un solo punto de despacho con uno o varios destinos. Le sirve al que recibe para:

- saber cuándo se despachó o cuándo va a estar lista la mercadería;
- tener el detalle exacto del envío;
- adelantar el trámite de aduana si el envío es internacional;
- empatar lo despachado con la factura que llega después.

El mismo mensaje DESADV sirve como aviso de devolución, que es el camino de [logística inversa](logistica-inversa.md). En el aviso va el SSCC de cada bulto: el que recibe escanea la etiqueta, busca el SSCC en el aviso y sabe qué hay adentro sin abrir. Ese uso es la razón del SSCC según GS1, que lo describe como la clave para «access information regarding the logistic unit in computer files».

> [!NOTE] Sin fuente todavía: una tabla de equivalencias campo a campo entre DESADV y 856, y el texto del DESADV en el directorio oficial de UN/EDIFACT (se leyó en un espejo de un vendedor).

## Lo que un sistema guarda del despacho

El armado es de la base, a partir de los datos que repiten los sistemas consultados y de lo que piden GS1 y el aviso.

- Despacho: tipo (salida a cliente, devolución, traslado entre depósitos), destinatario, dirección y contacto, depósito de origen, pedido de origen, renglones con artículo, cantidad y [lote o serie](../../Inventario-y-depositos/Existencias/lote-y-serie.md), peso, fecha programada, fecha límite y fecha en que se hizo. Admite salidas parciales: lo que no salió queda como despacho pendiente vinculado al original.
- Bulto: SSCC, contenido, peso, vínculo a la etiqueta. Las cantidades de los bultos no pueden superar las del despacho, según el resumen del manual de un ERP abierto.
- Envío con el transportista: transportista y servicio, dirección y franja de retiro, peso total, valor declarado, si va en pallets, número de guía, enlace de seguimiento, estado de la reserva y estado de seguimiento. Uno de los sistemas pide el peso del producto para el envío con el transportista y guarda una referencia de seguimiento en el documento de salida.
- Viaje de entrega: vehículo, conductor, hora de salida, distancia total y paradas ordenadas. Cada parada lleva cliente, dirección, despacho vinculado, llegada estimada y una marca de visitada. Lo que hace falta para armar el recorrido está en [consolidación y ruteo](../Transporte/consolidacion-y-ruteo.md#el-viaje-y-sus-paradas-en-un-sistema).
- Aviso de despacho: uno por envío, con el contenido por bulto y la referencia al pedido.

Cada cambio de estado es un hecho con fecha que no se edita, como en el [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md). A juicio de la base, la salida confirmada es la que baja el stock del depósito de origen.

## En la Argentina, el remito

En la Argentina, el documento que acompaña el traslado es el remito, que va también en una transferencia entre depósitos propios; sus reglas, el remito digital y el código de operación de traslado (COT) están en [Inventario y depósitos en la Argentina](../../Inventario-y-depositos/inventario-y-depositos-en-argentina.md). Para un despacho, el remito se emite antes de que la mercadería salga y la acompaña hasta el destino (lectura de esa nota).
