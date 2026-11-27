# Investigación: Orden de compra y Seguimiento de la orden

Fecha de lectura: 2026-11-27. Ángulo: la parte transaccional (de la solicitud a lo recibido que coincide con lo pedido).

Aclaración de método. La cuota de búsqueda web de la sesión se agotó a mitad del trabajo, así que quedaron sin buscar el acuse del proveedor, las tarjetas de compra, las órdenes abiertas en políticas públicas y el seguimiento (expediting) en fuente de práctica. Las páginas se leyeron con un lector que devuelve un resumen del texto: salvo donde dice [L], la marca es [S] aunque la URL se haya abierto. No leí ningún libro de texto (van Weele, Monczka): no hay fuente de libro para ningún componente. Lo que sigue sobre «cómo lo hace un sistema» es documentación de software (evidencia de que la práctica existe); las notas no deben nombrar productos.

Marcas: [L] texto completo leído, [M] metadatos, [S] resumen secundario o del lector. Puntajes 1-3: autoridad / profundidad / ejemplos / unicidad.

## Observaciones sobre el árbol

1. El campo no separa «orden» de «seguimiento»: CIPS (13 pasos) no tiene pasos de orden, seguimiento ni cruce; salta de «Contract award and implementation» (9) a «Warehouse, logistics and receipt» (10) y a «Contract performance and improvement» (11). La división es de la base y se sostiene por el corte de #98; decirlo en `Fundamentos`.
2. Los estados de una orden mezclan tres ejes: aprobación (borrador, en revisión, aprobada, confirmada), avance físico (a recibir, recibida) y avance de facturación (a facturar, facturada), más las excepciones (en espera, cerrada, cancelada). `orden-de-compra.md` debería enseñar los ejes por separado; una lista única de estados confunde. Cada renglón tiene su estado y la cabecera resume.
3. La orden de servicios (hoja de aceptación en lugar de recepción) y la orden abierta cabrían en `tipos-de-orden.md`; `recepcion-contra-lo-pedido.md` solo las menciona y enlaza.
4. `diferencias-y-devoluciones.md` pisa el borde con Inventario (rechazo en la recepción) y con Contabilidad (nota de débito o de crédito). Se sostiene si el eje es la decisión comercial: qué se le pide al proveedor (crédito, reposición, reemplazo).
5. Poca fuente separa `confirmacion-y-seguimiento.md` de `seguimiento-de-la-orden.md`: en los sistemas leídos la confirmación del proveedor es un estado más de la orden. Sigue valiendo como nota aparte por su tema (fecha confirmada, ASN, expediting), pero es la más delgada en fuentes.
6. En la lista de estados de la tarea, «enviada» no es estado propio de la orden en ninguna fuente leída (en un ERP aparece solo en el pedido de cotización).

## 1. orden-de-compra (entrada)

### Fuentes

| # | Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 1.1 | Wikipedia, Purchase order | https://en.wikipedia.org/wiki/Purchase_order | secundaria | [S] | 1/1/1/1 |
| 1.2 | Documentación de un ERP de código abierto, Purchase Order | https://docs.frappe.io/erpnext/user/manual/en/purchase-order | práctica (producto) | [S] | 2/2/2/2 |
| 1.3 | Documentación de un ERP grande, Approve and confirm purchase orders | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation | práctica (producto) | [L] | 2/3/2/3 |
| 1.4 | Cornell LII, UCC 2-207 | https://www.law.cornell.edu/ucc/2/2-207 | primaria (ley de EE.UU.) | [S] | 3/2/1/2 |
| 1.5 | CIPS, The thirteen steps of the procurement process | https://1prd-dxp.cips.org/intelligence-hub/procurement/procurement-process | primaria | [S] | 3/1/1/2 |

### Afirmaciones

- Qué lleva. Un documento comercial del comprador al vendedor que indica «types, quantities, and agreed prices for products or services required»; la mayoría trae lista de bienes o servicios con precio, condiciones de pago e instrucciones de envío (1.1, secciones lead y Legal). Ejemplo de 1.2: 200 adaptadores a USD 18 = USD 3.600, con el precio tomado de la cotización aceptada y con depósito receptor y fecha de entrega. Campos que aparecen en las fuentes: proveedor, renglones con cantidad, precio y unidad, depósito de destino, fecha requerida, condiciones de pago y de entrega, impuestos, referencia a la solicitud o a la cotización de origen.
- Valor legal. «Issuing a PO does not by itself form a contract. Without a prior contract, the seller's acceptance forms one» (paráfrasis del lector sobre 1.1, Legal); la trata como instrumento regulado por el Código Uniforme de Comercio de EE.UU. (1.1). UCC 2-207(1): una expresión definida de aceptación o una confirmación escrita enviada en tiempo razonable opera como aceptación «even though it states terms additional to or different from those offered», «unless acceptance is expressly made conditional on assent to the additional or different terms»; entre comerciantes los términos adicionales entran al contrato salvo que la oferta limite la aceptación a sus términos, los altere materialmente u objeten en tiempo razonable (1.4). Es ley de EE.UU. y hay dos fuentes que dependen de ese régimen, no de dos regímenes; el derecho argentino no se buscó y va a la nota del país.
- Qué dispara. En 1.2, someter la orden compromete la compra pero no mueve stock ni asienta en el mayor; recibos y facturas se controlan contra ella. En 1.3 [L]: una orden «creates inventory transactions only when it reaches the Approved status» (ese stock en camino no se puede reservar hasta aprobarse); al confirmar se guarda una copia exacta de lo confirmado y se generan las distribuciones contables y las verificaciones de presupuesto, si están activas. De ahí: compromiso presupuestario y stock pedido o en tránsito; la cuenta a pagar nace después (ver `Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md`).
- Estados de aprobación (1.3 [L]): con control de cambios activo, seis: Draft, In review, Rejected, Approved, Confirmed, Finalized. «Confirmed» no se alcanza sin «Approved»; «Finalized» es financieramente cerrada y no admite cambios. Sin control de cambios, la orden nace aprobada. Estados de avance (1.2): To Receive and Bill, To Receive, To Bill, Completed, On Hold, Closed, Cancelled. Las dos fuentes miden ejes distintos; no se contradicen.
- CIPS no tiene paso «orden de compra»; cae en «Contract award and implementation» (paso 9) (1.5).
- «No PO, no pay»: algunas organizaciones devuelven las facturas sin número de orden (1.1, Legal). Una sola fuente, secundaria.

### Recurso canónico propuesto

No hay uno. Para el ciclo de estados, versiones y re-aprobación, la página 1.3 [L] es la más completa, pero es documentación de producto. Para la definición, el glosario de CIPS y Dobler y Burt, «Purchasing and Supply Management» (1996), ambos citados por Wikipedia y no leídos. En qué fijarse: la separación entre aprobación interna, confirmación del proveedor y avance de recepción.

## 2. solicitud-de-compra

### Fuentes

| # | Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 2.1 | Wikipedia, Purchase requisition | https://en.wikipedia.org/wiki/Purchase_requisition | secundaria | [S] | 1/1/1/1 |
| 2.2 | Doc. del ERP abierto, Material Request | https://docs.frappe.io/erpnext/user/manual/en/material-request | práctica (producto) | [S] | 2/2/2/2 |
| 2.3 | APQC, Maverick purchasing means slower, more costly purchases | https://www.apqc.org/blog/maverick-purchasing-means-slower-more-costly-purchases | primaria (benchmarking) | [S] | 2/2/2/3 |
| 2.4 | Coupa (cita el estudio de Hackett), Maverick Spend Report; solo resultado de búsqueda | https://get.coupa.com/rs/950-OLU-185/images/19-Maverick-Spend-Report.pdf | secundaria, de un proveedor | [S] | 1/1/1/1 |
| 2.5 | Penn State, Identifying and mitigating maverick spend; solo resultado de búsqueda | https://pure.psu.edu/en/publications/identifying-and-mitigating-maverick-spend/ | académica | [M] | 2/1/1/2 |
| 2.6 | Doc. del ERP grande, Purchase agreements | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements | práctica (producto) | [L] | 2/3/2/2 |

### Afirmaciones

- Qué es. «A request sent internally within a company to obtain purchased goods and services»: dice qué se necesita, cuánto, la fuente y el costo; sirve de autorización previa y garantiza compras «with the consent of the line manager and that a sufficient budget is available» (2.1). La sección no cita fuentes, la más débil; no nombra quién pide.
- Cómo la modela un sistema (2.2). La solicitud «records that internal requirement before the company asks suppliers for prices» y no genera asiento ni movimiento de stock. Sirve para comprar, transferir entre depósitos, consumir, fabricar o subcontratar. Estados: Draft, Pending, Partially Ordered / Ordered, Partially Received / Received, Stopped, Cancelled. De ella se pasa a un pedido de cotización o directo a la orden, conservando la referencia para saber cuánto de lo solicitado ya se ordenó. Puede crearse sola cuando el stock proyectado baja del nivel de reposición. La fuente no describe un flujo de aprobación formal. Aprobación según cargo y monto: `Contabilidad/Control-interno/autorizaciones.md`; acá solo en qué paso se aplica (inferencia: la solicitud la aprueba quien responde por el presupuesto del pedido; la orden, según el monto contra la matriz).
- La solicitud no reserva contra un acuerdo: el máximo del acuerdo se controla en la orden y no en la solicitud, «because requisitions aren't always approved» (2.6 [L]).
- Maverick spending. APQC: comprar por cuenta propia fuera del proceso estándar; ocurre porque se ve el proceso «too complicated or a waste of time». En las organizaciones de peor desempeño (ingresos de al menos USD 500 millones) es «2.5 percent or more of their total purchases»; las que más lo practican necesitan en la mediana «16 hours more to issue a purchase order to a vendor» y gastan USD 2,58 más de costo de compras por cada USD 1.000 comprados. Conclusión de APQC: no hace la compra más rápida ni más barata, aunque se lo crea (2.3). Cifras de Hackett que circulan (hasta 16 % de los ahorros negociados perdidos; casi 30 % del gasto indirecto fuera de contrato; cumplimiento de 91 % en los mejores contra 74 %) llegan por resúmenes de proveedores de software y los rangos discrepan entre ellos (2.4); no las leí en origen, no usar sin hacerlo. El benchmark de «lapasar» declara que sus cifras son ilustrativas.
- «Orden después de la factura» (after-the-fact PO): sin fuente que la defina ni la mida; solo aparece implícita en la política «no PO, no pay» (1.1). Hueco.
- Tarjetas de compra (P-cards) y catálogos internos: búsqueda bloqueada por cuota; hueco. Pista sin leer: la referencia 5 de Wikipedia (política de tarjetas de un consejo del Reino Unido).

### Recurso canónico propuesto

Para maverick, APQC (2.3): medición con método; fijarse en que son diferencias de mediana entre grupos, no causalidad. Para la solicitud: ninguno.

## 3. tipos-de-orden

### Fuentes

| # | Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 3.1 | Doc. del ERP grande, Purchase agreements | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements | práctica (producto) | [L] | 2/3/3/3 |
| 3.2 | Doc. del ERP abierto, Blanket Order | https://docs.frappe.io/erpnext/user/manual/en/blanket-order | práctica (producto) | [S] | 2/2/2/2 |
| 3.3 | Doc. de otro ERP abierto, Blanket orders | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/purchase/manage_deals/blanket_orders.html | práctica (producto) | [S] | 2/2/1/2 |
| 3.4 | Wikipedia, Purchase order (PPO, indent) | https://en.wikipedia.org/wiki/Purchase_order | secundaria | [S] | 1/1/1/1 |
| 3.5 | SAP, Service Entry and Acceptance for Purchase Orders (versión 4.6C) | https://help.sap.com/saphelp_46c/helpdata/en/76/5aa8010d3211d3836f0000e8a5eb64/content.htm | práctica (producto, antigua) | [S] | 2/2/1/2 |
| 3.6 | Wikipedia, Consignment | https://en.wikipedia.org/wiki/Consignment | secundaria | [S] | 1/1/1/1 |

### Afirmaciones

- Estándar o puntual: la orden por una compra con cantidad, precio y fecha. Ninguna fuente la define como tipo aparte; Wikipedia la trata como la orden general.
- Orden planificada. Wikipedia: planned purchase order, «a long-term commitment to buy from one supplier, with individual POs specifying quantities over time» (3.4). El artículo «Blanket purchase order» de Wikipedia da 404: no hay fuente propia para el término blanket ni para call-off.
- Acuerdo y liberaciones (3.1 [L]). «A contract that commits an organization to buy a specified quantity or amount by using multiple purchase orders over time. In exchange for this commitment, the buyer receives special prices and discounts». Cuatro compromisos: por cantidad de un producto, por valor de un producto, por valor de una categoría, por valor de cualquier producto. Tiene vigencia, se activa y se cierra. Políticas: «Max is enforced» (el total de las órdenes no supera el compromiso), «Price and discount is fixed» (si el precio de la orden difiere, se rompe el vínculo y el renglón no cuenta para cumplir el compromiso) y montos mínimo y máximo de liberación. El acuerdo se aplica al crear la orden, no después, y guarda versiones al confirmarse. Otro ERP (3.2): el compromiso es la cantidad total del período y la tarifa pactada; de ahí salen varias órdenes y se actualiza lo ya pedido; cada orden sigue necesitando su entrega, depósito, impuestos y aprobación; el acuerdo «may not automatically close» al vencer. Otro más (3.3): acuerdo de largo plazo para entregas recurrentes a precios acordados, con validez opcional. Tres productos coinciden en compromiso, liberaciones y saldo; «release» es el término del ERP grande.
- Frontera: el contrato como acuerdo es de `Abastecimiento-estrategico/contrato-marco.md`; acá su uso. Los tres sistemas tratan acuerdo y orden como objetos distintos.
- Orden de servicios (3.5, vía buscador y página leída). Los servicios realizados se registran en una hoja de entrada que referencia la orden, y «before the vendor can send an invoice, you need to accept the service»; la factura se controla contra la hoja aceptada, y el indicador de recepción de mercadería de la orden puede apagarse a favor de la aceptación. En la página leída quien registra también acepta y no se nombra aprobador aparte: la separación de funciones en ese paso es lectura propia, no dato.
- Consignación (3.6): el dueño legal es el consignante hasta la venta; se paga «only after the good is sold and has been paid for by the buyer»; el artículo habla de venta minorista. La mirada del comprador (stock propio en depósito que sigue siendo del proveedor hasta que se usa) no se leyó. Hueco.
- Subcontratación: el ERP abierto tiene el propósito «Subcontracting» en la solicitud (2.2) y el grande trata aparte las órdenes derivadas (1.3). Solo el borde con Producción.

### Recurso canónico propuesto

La página de acuerdos de compra del ERP grande (3.1 [L]): lo más completo sobre cómo se relacionan acuerdo y órdenes; fijarse en las políticas de máximo y de precio fijo. Producto, no definición.

## 4. cambios-y-cancelaciones

### Fuentes

| # | Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 4.1 | Doc. del ERP grande, Approve and confirm purchase orders (secciones «Changing» y «Canceling») | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation | práctica (producto) | [L] | 2/3/3/3 |
| 4.2 | Doc. del ERP abierto, Purchase Order | https://docs.frappe.io/erpnext/user/manual/en/purchase-order | práctica (producto) | [S] | 2/2/1/2 |

### Afirmaciones

- Cambiar (4.1 [L]). Con control de cambios, una orden aprobada vuelve a Draft con la acción «Request change»; al terminar puede requerir re-aprobación según una política «Re-approval rule for purchase orders» que define qué tipos de cambio la exigen. Cada confirmación guarda una copia exacta, de modo que hay historial de versiones. Si parte del renglón ya se entregó, no se cambia la cantidad pedida en borrador. 4.2: para un cambio comercial importante, cancelar y enmendar («cancel and amend»), sin tocar el historial; recibos o facturas vinculados pueden bloquear la cancelación. Qué cambios exigen re-aprobación lo fija una política: «si cambia el monto» es lo razonable, pero es inferencia, no dato.
- Cancelar (4.1 [L]). Confirmada, la orden ya no se borra; se cancela la cantidad total o el resto «provided that the quantity isn't received or invoiced». Ejemplo literal: cantidad 5, recibidas 3, se pueden cancelar 2 y el renglón queda en Received. «Finalize» evita más procesamiento. Bajo control de cambios, la cancelación también pasa por aprobación. Cerrar no es cancelar: en 4.2, «Closed» significa que el saldo no se procesará y no revierte lo ya registrado por recibos y facturas.
- Con un acuerdo, cambiar el precio de una orden rompe el vínculo con el compromiso (3.1).
- Quién avisa al proveedor: ninguna fuente lo dice. Que cada confirmación guarde una copia (4.1) sugiere reenviar la versión nueva y esperar nueva confirmación, pero es inferencia. Hueco.

### Recurso canónico propuesto

Las secciones «Changing purchase orders» y «Canceling purchase orders» de 4.1 [L]; el ejemplo numérico de cancelación parcial es el mejor hallado. Producto.

## 5. seguimiento-de-la-orden (entrada)

### Fuentes

| # | Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 5.1 | CIPS, thirteen steps | https://1prd-dxp.cips.org/intelligence-hub/procurement/procurement-process | primaria | [S] | 3/1/1/2 |
| 5.2 | APQC PCF 7.4, categoría 4.2 (del brief; no abierto) | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | primaria | no leída | - |
| 5.3 | Doc. del ERP abierto, Purchase Receipt | https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt | práctica (producto) | [S] | 2/2/1/2 |
| 5.4 | Doc. del ERP grande (estados y cierre) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation | práctica (producto) | [L] | 2/3/2/3 |

### Afirmaciones

- CIPS: paso 9 «Contract award and implementation», 10 «Warehouse, logistics and receipt» («Warehouse operations need to be a smooth and efficient process»; incluye «Frequency of deliveries»), 11 «Contract performance and improvement» («Contract performance should be monitors and reviewed at agreed periods» en la página), 12 gestión de la relación con proveedores, 13 gestión de activos (5.1 [S]). La página no trata pedido, seguimiento, factura ni pago. La parte transaccional la cubre APQC 4.2, que no abrí.
- Dónde termina Compras. En el ERP abierto la orden es Completed cuando está todo recibido y todo facturado (1.2, 5.3). En el grande, el renglón pasa a Received al recibirse lo pedido y la orden a Finalized cuando se cierra financieramente (5.4). Los sistemas mantienen la orden viva hasta la factura; el trabajo de Compras, según el corte de #98, termina antes, cuando lo recibido coincide con lo pedido. Conviene decirlo así en la nota: no es una contradicción, son dos cortes distintos.
- Estados de avance: ver sección 1.

### Recurso canónico propuesto

APQC PCF 7.4, 4.2 «Procure materials and services»: la secuencia de ejecución; sin leer. Quien arme la nota debería abrirlo.

## 6. confirmacion-y-seguimiento

### Fuentes

| # | Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 6.1 | Doc. del ERP grande, confirmación de la orden | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation | práctica (producto) | [L] | 2/3/2/3 |
| 6.2 | Doc. de otro ERP, RFQ | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/purchase/manage_deals/rfq.html | práctica (producto) | [S] | 2/2/1/2 |
| 6.3 | Wikipedia, Advance ship notice | https://en.wikipedia.org/wiki/Advance_ship_notice | secundaria | [S] | 1/2/1/2 |
| 6.4 | Wikipedia, Expediting | https://en.wikipedia.org/wiki/Expediting | secundaria | [S] | 1/1/1/2 |
| 6.5 | Doc. del ERP abierto, Supplier Scorecard | https://docs.frappe.io/erpnext/user/manual/en/supplier-scorecard | práctica (producto) | [S] | 2/2/2/2 |

### Afirmaciones

- Acuse o confirmación (6.1 [L]). Tras la aprobación, una consulta al proveedor (precios, descuentos, fechas de recepción) deja la orden «In external review». Si el proveedor tiene portal, aprueba o rechaza ahí; el rechazo trae motivo y sugerencias de cambio y la orden sigue en revisión externa. La confirmación registra la orden «as committed», guarda copia exacta y dispara las verificaciones presupuestarias. Se puede emitir una confirmación pro-forma para el proveedor, sin efecto contable. 6.2: el pedido tiene «Order Deadline» («the date by which the vendor must confirm their agreement to supply the products»), «Expected Arrival» calculada con ese plazo y el plazo de entrega del proveedor, y una casilla para pedirle que confirme la fecha de envío por correo. Fecha pedida contra confirmada: solo aparece como dos campos; ninguna fuente leída trata la comparación ni qué hacer si difieren. Hueco.
- El acuse del proveedor con términos propios puede formar contrato igual (UCC 2-207, ver 1.4).
- ASN (6.3 [S]). «A notification of pending and upcoming deliveries matched to a previously-provided packing list»; normalmente EDI: EDI 856 (X12) o DESADV (EDIFACT). Puede detallar pedido, mercadería, embalaje, transportista y códigos de barras de cada unidad. Su fin es dar aviso previo al depósito receptor; reduce costos de recepción (se escanea en lugar de desembalar), permite ver diferencias entre lo esperado y lo enviado y reportarlas al proveedor, y reasignar según el cumplimiento real. El artículo no menciona órdenes de compra por nombre.
- Expediting (6.4 [S]). «A concept in purchasing and project management for securing the quality and timely delivery of goods and components»: lo hace compras o un tercero, con cuatro niveles (control de producción, de calidad, de embalaje y transporte, y de proyecto); típico en proyectos grandes (astilleros, refinerías). La página está marcada «necesita más citas» y tiene referencias muertas o archivadas; el texto de ISM «Purchasing and Expediting — the True Facts» (enlace externo) no se leyó. Fuente débil.
- Medición: el scorecard (6.5) usa entregas a tiempo sobre entregas totales y cantidad aceptada sobre recibida, con ponderaciones que suman 100 (ejemplo 50/30/20) y estados (Preferred 85-100, Approved 70-84, Watch 50-69, Blocked bajo 50); el bloqueo impide nuevos pedidos y órdenes al proveedor y el artículo pide dejar excepción para emergencias o proveedor único. Eso es de `Proveedores/evaluacion-de-proveedores.md`; acá solo el enlace.

### Recurso canónico propuesto

ASN: Wikipedia sirve de introducción; el estándar es X12 856 / EDIFACT DESADV (no leídos). Seguimiento: ninguno encontrado; candidato, ISM (no leído).

## 7. recepcion-contra-lo-pedido

### Fuentes

| # | Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 7.1 | SAP, Underdeliveries, Overdeliveries, and Final Deliveries (versión 4.6C) | https://help.sap.com/saphelp_46c/helpdata/en/a5/63343943a211d189410000e829fbbd/content.htm | práctica (producto, antigua) | [S] | 2/2/1/3 |
| 7.2 | SAP Learning, Applying Tolerances and the Delivery Completed Indicator; solo resultado de búsqueda | https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/applying-tolerances-and-the-delivery-completed-indicator | práctica (producto) | [S] | 2/1/1/1 |
| 7.3 | Doc. del ERP abierto, Purchase Receipt | https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt | práctica (producto) | [S] | 2/2/2/2 |
| 7.4 | Doc. del ERP abierto, Purchase Order | https://docs.frappe.io/erpnext/user/manual/en/purchase-order | práctica (producto) | [S] | 2/2/1/2 |
| 7.5 | Doc. de otro ERP, control de facturas (cruce de tres vías) | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/purchase/manage_deals/control_bills.html | práctica (producto) | [S] | 2/1/1/1 |
| 7.6 | Doc. del ERP grande, Approve and confirm purchase orders («Deliver remainder») | https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation | práctica (producto) | [L] | 2/3/2/3 |

### Afirmaciones

- Cruce de dos vías orden-recepción: comparar lo recibido con lo pedido en cantidad. El de tres vías (con factura) es de Contabilidad. En 7.3, el recibo se crea normalmente desde la orden y trae proveedor, renglones, cantidades, precios e impuestos; al confirmarlo actualiza cantidad y porcentaje recibido de la orden, pero no crea la deuda: «el Purchase Invoice la crea». En 7.5, la política «cantidades recibidas» solo permite una factura en borrador a partir de lo ya recibido, y el cruce de tres vías marca el pago como excepción si se edita la factura.
- Tolerancias de cantidad (7.1 [S]). Por defecto «underdeliveries are allowed» y se toman como entrega parcial con un aviso; con una tolerancia de subentrega en el renglón, lo recibido dentro de ella se acepta sin aviso. «Overdeliveries are not allowed» por defecto (error); se habilitan con el indicador «ilimitada» o con un porcentaje de tolerancia; lo que supera la cantidad más la tolerancia se rechaza. Las tolerancias se fijan en el maestro del artículo, en el registro artículo-proveedor o en el renglón de la orden, y el maestro vale por defecto (7.2). En el ERP abierto hay un porcentaje de sobrerrecepción que bloquea lo que lo supera, con el consejo de revisar primero la unidad de compra y su conversión (7.3), y un porcentaje distinto de sobrepedido (la orden puede exceder la solicitud, por embalaje o mínimos del proveedor) que no debe usarse para ocultar un aumento no aprobado (7.4). Tolerancia de precio: ninguna fuente de este ángulo; es del cruce de la factura. Hueco.
- Entrega parcial y saldo. «One Purchase Order can be received through several Purchase Receipts»; la orden queda abierta por el resto y se cierra con «Close» solo cuando el resto no se recibirá ni facturará (7.3). En el ERP grande el saldo es «Deliver remainder» y puede cambiarse en un renglón en borrador (7.6 [L]). La palabra backorder no aparece en ninguna fuente leída de órdenes (en la literatura es lo que el proveedor no pudo despachar; sin fuente).
- Cerrar con saldo (7.1). El indicador de «entrega completa» marca el renglón cerrado: la cantidad abierta pasa a cero aunque no haya llegado todo, y aun así se pueden registrar recibos posteriores. Se activa solo al recibirse la cantidad completa o dentro de las tolerancias (según configuración por planta), o a mano; si una devolución baja lo entregado bajo la tolerancia, el sistema lo reinicia y avisa. En 7.3, «Closed» equivale a que el resto no se procesará.
- Entrega anticipada (antes de la fecha confirmada): sin fuente. Hueco.
- Recepción de servicios: hoja de aceptación (3.5).
- Frontera con la nota existente `Inventario-y-depositos/Operacion-del-deposito/recepcion.md`: ahí «Compras decide qué se le reclama» si llegan 90 de 100; acá se muestra cómo la orden registra ese faltante y si queda abierta o se cierra.

### Recurso canónico propuesto

SAP, «Underdeliveries, Overdeliveries, and Final Deliveries» (7.1): tiene un caso por cada decisión. Es producto y de una versión de los años 90; sirve como evidencia de práctica larga, no como definición. Coincide con el ERP abierto en subentrega como parcial, sobreentrega con tope y cierre manual del saldo: dos productos independientes.

## 8. diferencias-y-devoluciones

### Fuentes

| # | Fuente | URL | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|---|
| 8.1 | Microsoft Learn, Create vendor returns | https://learn.microsoft.com/en-us/training/modules/process-purchase-orders-dyn365-supply-chain-mgmt/7-create-vendor-returns | práctica (producto) | [L] | 2/2/3/2 |
| 8.2 | Oracle, Understanding the RTV Business Process (y Managing Vendor Returns); solo resultados de búsqueda | https://docs.oracle.com/en/applications/peoplesoft/financials-and-supply-chain-management/9.2.056/peoplesoft-purchasing/understanding-rtv-business-process.html | práctica (producto) | [S] | 2/2/2/2 |
| 8.3 | Doc. del ERP abierto, Purchase Receipt | https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt | práctica (producto) | [S] | 2/2/2/2 |
| 8.4 | Doc. del ERP abierto, Supplier Scorecard | https://docs.frappe.io/erpnext/user/manual/en/supplier-scorecard | práctica (producto) | [S] | 2/2/2/2 |
| 8.5 | OpenStax, Principles of Financial Accounting, 6.3 (ya citada en la base; no releída) | https://openstax.org/books/principles-financial-accounting/pages/6-3-analyze-and-record-transactions-for-merchandise-purchases-using-the-perpetual-inventory-system | libro de texto | no releída | - |

### Afirmaciones

- Devolución al proveedor (RTV). Se devuelve por tamaño o color equivocado, vencimiento, daño en el transporte o mal manejo, y «You must issue a vendor credit note when items are returned to the vendor» (8.1 [L]). Tres maneras de registrarla: una orden de tipo «Returned order», una línea con cantidad negativa, o copiar las líneas de la factura original (impide devolver más de lo recibido y usa el precio original). La primera exige número de autorización de devolución (RMA) y acción de devolución; «most vendors require you to include their Return Material Authorization (RMA) number», que actúa como preautorización. Para artículos con serie o lote hay que decir cuáles se devuelven.
- Acciones (8.2 [S]): devolución por crédito, por cambio o por reposición; la devolución por crédito permite generar sola la nota de débito (debit memo); los costos de reposición («restocking fees») entran en la nota. Los bienes rechazados al recibir no generan en ese sistema una RTV ni una nota de débito por sí mismos. Si el proveedor manda reemplazo en lugar de crédito, se recibe el reemplazo y la nota del proveedor se registra contra la orden de devolución (de la misma búsqueda; SAP).
- Nota de débito y nota de crédito: nombres opuestos según quién emite (el comprador emite la nota de débito que baja su deuda; el proveedor responde con nota de crédito). Aclarar en la nota. El asiento: OpenStax 6.3 (devolución de 15 impresoras: Cuentas a pagar 1.500 contra Inventario 1.500), ya en `compras-y-cuentas-a-pagar.md`.
- Rechazados (8.3 [S]): se carga la cantidad rechazada en el recibo, a un depósito separado; «Keeping rejected stock separate prevents damaged units from appearing as usable stock»; la devolución se crea después desde el recibo. La fuente no menciona nota de débito. Esto es de Inventario; acá, el reclamo.
- Faltantes y sobrantes: el faltante deja saldo abierto; el sobrante lo trata la tolerancia (sección 7). Plazos y costos del reclamo (quién paga el flete de vuelta): sin fuente. Hueco.
- Evaluación: el scorecard (8.4 [S]) toma cantidad aceptada sobre recibida (calidad) y entregas a tiempo sobre totales de las transacciones. Sin recepción registrada contra la orden no hay dato para evaluar (inferencia propia).

### Recurso canónico propuesto

Para la devolución, «Create vendor returns» (8.1 [L]): corta, con ejemplos y la lógica del RMA. Para el asiento, OpenStax 6.3.

## Huecos

- Libros de texto (van Weele, Monczka y otros): no leídos. Las definiciones de orden, tipos de orden y expediting salen solo de documentación de software y Wikipedia.
- CIPS glossary (PO y blanket order), glosario de ISM y «Purchasing and Expediting — the True Facts»: no leídos.
- APQC PCF 7.4, categoría 4.2: no abierto; es la fuente más probable para la secuencia procure-to-pay.
- Acuse del proveedor y comparación de fecha confirmada con fecha pedida: sin fuente más que dos campos de un ERP.
- P-cards, catálogos internos y «orden después de la factura»: sin fuente (búsqueda bloqueada por cuota).
- Quién avisa al proveedor de un cambio o una cancelación: sin fuente.
- Valor legal de la orden fuera de EE.UU.: solo UCC 2-207 y Wikipedia; sin segunda fuente independiente; lo argentino va a la nota del país.
- Tolerancia de precio y entrega anticipada: sin fuente.
- Consignación del lado comprador, y subcontratación: sin fuente propia.
- Cifras de maverick spending de Hackett: solo vía resúmenes de proveedores; usar APQC.
- Casi todo lo de «cómo lo hace un sistema» es documentación de producto; dos fuentes de SAP son de la versión 4.6C. No hay norma ni libro.
