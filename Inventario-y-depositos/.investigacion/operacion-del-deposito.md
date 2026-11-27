# Operación del depósito: informe de investigación (capa cruda)

Fecha de lectura: 2026-11-27. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario. Puntajes 1-3: autoridad / profundidad / ejemplos / unicidad.

## Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1 | Bartholdi y Hackman, *Warehouse & Distribution Science*, release 0.98.1 (16-ago-2019), PDF 3,9 MB | https://www.warehouse-science.com/book/editions/wh-sci-0.98.1.pdf (índice en https://www.warehouse-science.com/book/index.html) | primaria (libro) | 3/3/3/3 | [L] caps. 2, 3, 4 y 13 y fragmentos de 8-9; del resto, solo el índice |
| 2 | De Koster, Le-Duc y Roodbergen (2007), "Design and control of warehouse order picking: a literature review", EJOR 182(2), 481-501, DOI 10.1016/j.ejor.2006.07.009 | https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf (repositorio abierto de Erasmus) | primaria (paper de revisión) | 3/3/2/3 | [L] parcial: secciones 1, 2, 4 y 7 y la Fig. 4; batching y zoning solo por fragmentos |
| 3 | Odoo 17.0, "Reservation methods" | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/reservation_methods.html | primaria (doc de producto; solo evidencia de práctica) | 2/1/2/1 | [S] (lectura mediada por el fetcher) |
| 4 | Odoo 17.0, "Use locations" | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations.html | primaria (doc de producto) | 2/1/2/1 | [S] |
| 5 | ERPNext, "Quality Inspection" | https://docs.frappe.io/erpnext/user/manual/en/quality-inspection | primaria (doc de producto) | 2/1/2/1 | [S] |
| 6 | APQC PCF 7.4, 4.4.3 "Operate warehousing" (texto ya extraído, scratchpad/inv/apqc-4.txt) | archivo local del brief | primaria (taxonomía) | 2/1/1/2 | [L] el fragmento |

Odoo "Putaway rules" (varias URL) y ERPNext Stock dieron 404 o no se leyeron.

Independencia: las fuentes 3-5 son documentación de producto; solo prueban que la práctica existe y las notas no deben nombrarlas. 1 y 2 son independientes (De Koster cita a Bartholdi y Hackman solo en una frase sobre travel time y sobre el problema forward-reserve).

## 1. Ubicaciones y direccionamiento

- "Each storage location in a warehouse is assigned a unique address. This includes both fixed storage locations, such as a portion of a shelf and mobile locations such as the forks of a lift truck." (Fuente 1, §2.4, p. 14.) La ubicación es un recurso caro: alquiler, clima, seguridad, equipamiento.
- Ubicación fija (dedicated) frente a compartida (shared) (Fuente 1, §2.4). Dedicada: "each location is reserved for an assigned product and only that product may be stored there"; "on average the storage capacity is only about 50% utilized". Compartida: un producto en más de una ubicación y, al vaciarse una, se reasigna. Costos: los operarios no aprenden las ubicaciones y hay que dirigirlos con un sistema; "shared storage requires greater software support and also more disciplined warehouse processes". Ejemplo numérico literal: dos semanas de stock en dos ubicaciones iguales con picking de una sola: utilización 75% la primera semana, 50% la segunda y "62.5%" en las dos.
- Riesgo de la ubicación libre: un picker mandado al otro lado "may be tempted to pick the product from a more convenient location, thus creating discrepancies between book and physical inventory at two locations" (Fuente 1, §2.4).
- Hay que llevar "a second inventory, not of product, but of storage locations": qué ubicaciones están libres, su tamaño y el peso que soportan (Fuente 1, §3.2). El stock locator es "the ability to manage an inventory of storage locations in addition to an inventory of product" y habilita put-away y picking dirigidos (§4.2).
- Slotting: "A more detailed product layout, usually called a 'slotting', will explicitly account for the geometry of storage and tell exactly where each SKU should be located (for example, on the third shelf of the second section of aisle 2, oriented with case width to the front)." (Fuente 1, cap. 2, p. 17-18.) Sirve también de ejemplo de dirección: estante, sección, pasillo.
- Políticas de asignación según De Koster et al. (Fuente 2, §4.2): "random storage, closest open location storage, dedicated storage, full turnover storage and class based storage". Clase = por rotación (ABC), con las rápidas cerca de la puerta (§4.3). Verificar antes de citar los resultados comparativos (full-turnover frente a class-based), leídos solo en parte.
- Zona de reserva y zona de picking (forward-reserve): "it is in many cases efficient to separate the bulk stock (reserve area) from the pick stock (forward area)... the smaller the area, the lower the average travel times" (Fuente 2, §4.1). Reponer la zona de picking cuesta más que un pick: "A restock is more expensive than a pick"; regla práctica "one restocker to every five pickers" (Fuente 1, §3.3).
- Práctica: ubicaciones en jerarquía padre/hijo con rutas como "WH/Stock/Zone A/Refrigerator 1"; tipos de ubicación: proveedor, vista, interna, cliente, pérdida de inventario, producción, tránsito (Fuente 4). Prueba que depósito > zona > ubicación es corriente y que las mermas y el tránsito se modelan como ubicaciones virtuales.

## 2. Recepción, calidad en la recepción y put-away

- Recepción (Fuente 1, §3.1): aviso previo de llegada; "It is not unusual for warehouses to schedule trucks to within 30-minute time windows"; "it is likely to be scanned to register its arrival so that ownership is assumed, payments dispatched, and so that it is known to be available to fulfill customer demand. Product will be inspected and any exceptions noted, such as damage, incorrect counts, wrong descriptions". Recibir son "about 10% of operating costs" de un CD típico; put-away "about 15%" (§3.2). Las cifras vienen de terceros citados por el libro; sin segunda fuente.
- Put-away: "where you store the product determines to a large extent how quickly and at what cost you later retrieve it" (Fuente 1, §3.2). Se escanea la ubicación para registrar dónde quedó.
- Efecto contable: "receipt drives the paying of bills to suppliers upstream; and shipping drives the sending of invoices downstream" (Fuente 1, §4.1). Frontera con Compras (cruce de tres vías) y Contabilidad.
- Cross-docking: "less inventory (because all product flows right through) and less labor (because product does not have to be put away and later retrieved)" (Fuente 1, §13.1). Puertas de recepción ("strip") y de despacho ("stack") (§13.2). El caso de terminales de carga es más de cadena de suministro; acá alcanza definición y frontera.
- Calidad en la recepción: "Quality assurance" figura entre las funciones básicas de un WMS (Fuente 1, §4.3). En la práctica, la inspección se crea sobre el recibo en borrador y "submission of a stock delivery/receipt document will be allowed only after a Quality Inspection is done against it" para los ítems con criterios de inspección (Fuente 5, [S]). La cuarentena como estado: sin fuente sólida leída (ver huecos).
- APQC 4.4.3.2 "Receive, inspect, and store inbound deliveries" (Fuente 6): la taxonomía junta recibir, inspeccionar y ubicar, como el árbol propuesto.

## 3. Reserva

- Bartholdi: al llegar el pedido el depósito "must perform checks such as verifying that inventory is available to ship"; el WMS "checks the order against available inventory and identifies any shortages" (Fuente 1, §3.3). No usa la palabra reserva.
- Práctica (evidencia): tres momentos para reservar: "At Confirmation" ("Reserves products only when a sales order is confirmed, and if stock is already available"), "Manually" ("product availability must be checked manually, and the required quantity must be reserved manually") y "Before scheduled date" (cuántos días antes de la entrega programada, por defecto 0) (Fuente 3, [S]).
- Reserva blanda o dura, asignación de lote (FEFO) y liberación: sin fuente libre leída (hueco). El comprometido y el ATP están en el CPIM (scratchpad/inv/cpim.txt) y en la nota de fecha prometida.

## 4. Preparación de pedidos y embalaje hasta la puerta

- Peso del picking: "Order-picking typically accounts for about 55% of warehouse operating costs" (Fuente 1, §3.3); "cost of order picking is estimated to be as much as 55% of the total warehouse operating expense" (Fuente 2, abstract). Las dos remiten a la misma literatura de origen: una sola cifra con dos reportes.
- Composición del tiempo del picker (discrepan). Fuente 1 §3.3: viaje 55%, búsqueda 15%, extracción 10%, papeleo y otras 20%. Fuente 2, Fig. 4 (de Tompkins et al., 2003): viaje 50%, búsqueda 20%, pick 15%, preparación 10%, otros 5%. Se dan las dos; coinciden en que el viaje domina. Fuente 1, §3.6: "Most of the expense in a typical warehouse is in labor; most of that is in order-picking; and most of that is in travel."
- Vocabulario (Fuente 1, §3.3): línea de pedido (order-line) frente a línea de picking (pick-line); ejemplo literal: pedido de 15 unidades de un artículo con cajas de 12 se convierte en dos líneas, 1 caja y 3 unidades. Picking de cajas completas frente a "broken-case or split-case" (el más intensivo en trabajo). "Pick face", "sku density", "pick density".
- Variantes (Fuente 2, §2): "picking by article (batch picking) or pick by order (discrete picking)"; "sort-while-pick" frente a "pick-and-sort"; zoning: "a logical storage area ... is split in multiple parts, each with different order pickers", progresivo (los pedidos pasan de zona en zona) o sincronizado (en paralelo); "The term wave picking is used if orders for a common destination (for example, departure at a fixed time with a certain carrier) are released simultaneously for picking in multiple warehouse areas"; tamaño de la ola "often between 30 minutes to 2 hours"; la ola siguiente solo empieza al completarse la anterior.
- Cuándo agrupar (Fuente 1, §3.3): "It is almost always better to batch single-line orders because no sortation is required. Very large orders do not need to be batched... The problem then is with orders of medium-size." Regla: agrupar cuando el costo de separar y el espacio extra son menores que la caminata extra evitada.
- Zonas como línea de montaje: los pedidos salen en la secuencia en que se liberaron, pero hay que balancear la línea (Fuente 1, §3.3.1).
- Ruteo (Fuente 2, §7): caso del viajante (Steiner TSP); en la práctica se usan heurísticas (return, midpoint, s-shape y otras) porque el óptimo no existe para todo layout y a los operarios les parece "illogical". Verificar definiciones exactas antes de citar.
- Embalaje y control (Fuente 1, §3.4-3.5): "this is a convenient time to check that the customer order is complete and accurate. Order accuracy is a key measure of service"; "returns are expensive to handle (up to ten times the cost of shipping the product out)"; "Packed product may be scanned to register the availability of a customer order for shipping"; el escaneo del trailer registra su salida. Esa salida es donde empieza el despacho.
- Consolidar o enviar parcial: "Amazon ... will likely ship separate packages if you order two books fifteen minutes apart" (Fuente 1, §3.4). Ejemplo de decisión de política.
- APQC 4.4.3.4 "Pick, pack, and ship product for delivery" (Fuente 6) incluye el envío en el mismo proceso; en este tema se corta en la puerta.

## Recursos canónicos propuestos

1. Bartholdi y Hackman, cap. 3 "Warehouse operations" (p. 23-29) como columna vertebral de recibir, ubicar, preparar, embalar y despachar; más §2.4 (ubicación fija frente a compartida) y cap. 4 (el stock locator). Fijarse en las cifras de costo por etapa y en la idea de "inventario de ubicaciones". Nota de copyright de la portada: "may be freely copied for educational purposes — but not for resale — as long as the authors' names and the copyright notice appear clearly". No es licencia abierta: se cita y enlaza, no se copia.
2. De Koster, Le-Duc y Roodbergen (2007), §2 (variantes), §4 (asignación) y §7 (ruteo): mapa de decisiones del picking manual. Es una revisión sobre picking manual; no cubre recepción ni reserva.
3. APQC PCF 4.4.3 como lista de verificación de lo que cubre "operar el depósito".
4. Pendiente de leer: Gu, Goetschalckx y McGinnis (2007) como mapa de las cuatro funciones.

## Sobre el árbol

El campo divide el depósito como el árbol (recibir, ubicar, preparar, embalar), con una salvedad: Bartholdi y Hackman, APQC y los WMS incluyen el despacho como paso final del mismo flujo. El árbol corta en la puerta; es una frontera válida pero hay que marcarla en la nota. Queda una zona gris entre Operación del depósito y Reposición: la reposición de la zona de picking desde la reserva (forward-reserve). Propuesta: la reposición interna entre zonas es de acá, y la política de cuándo y cuánto pedir es de Reposición.

## Huecos

- Gu, Goetschalckx y McGinnis (2007): no se leyó (el presupuesto de búsqueda web se agotó).
- Cuarentena e inspección: sin fuente sólida; ERPNext e Odoo solo vía fetcher y la doc de ERPNext leída no menciona almacén de rechazados. Faltan Dynamics 365 y SAP EWM.
- Reserva blanda y dura, asignación de lote y liberación: sin fuente primaria; solo Odoo (momentos de reserva).
- Put-away rules y estrategias de put-away de un WMS (URL de Odoo dio 404): sin leer.
- Bartholdi caps. 6-8 (layout), 9 (slotting detallado), 10 (ruteo) y 11 (flujo de trabajo): solo índice y fragmentos. De Koster §5-6 (batching, zoning) y las heurísticas de ruteo, leídos en parte; la versión es el PDF del repositorio, no la del editor.
- Frazelle, *World-Class Warehousing*: no consultado.
- Costos de recibir (10%) y put-away (15%): una sola fuente (Bartholdi citando a terceros).
