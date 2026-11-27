# Investigación: vertical Despacho y entrega

Fecha de la investigación: 2026-11-27.

## Advertencia sobre el alcance real de este informe

El presupuesto de búsqueda web de la sesión estaba agotado (límite compartido de 200 búsquedas). Solo pude hacer fetch directo de URLs conocidas, y muchas dieron 403 o 404 (UNECE, GS1, IRU, documentación de Odoo, wikisource, web.archive.org no permitido). Lo que sigue es lo que sí se pudo verificar. Casi todo lo demás queda declarado como hueco y no se rellena de memoria. Las afirmaciones que no llevan URL verificada están marcadas «SIN FUENTE VERIFICADA» y no deben pasar a una nota vigente sin confirmarse.

Escala de puntaje: autoridad / profundidad / ejemplos / unicidad, de 1 a 3. Marcas: [L] leído completo o sección completa, [M] metadatos o abstract, [S] resumen secundario o del buscador (acá, el fetch devuelve un resumen hecho por un modelo sobre la página, así que todo lo web cuenta como [S] salvo lo que bajé como archivo).

---

## Componente: despacho-y-entrega (entrada)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| APQC PCF Cross-Industry v7.4 (agosto 2024) | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | primaria | 3/3/2/3 | [L] de la sección 4.4 y 4.1.5 (texto extraído con pdftotext del PDF de 35 páginas) |
| ERPNext, manual de la nota de entrega | https://docs.frappe.io/erpnext/user/manual/en/delivery-note | primaria (documentación de un sistema abierto) | 2/2/3/1 | [S] |

### Afirmaciones

- El PCF 7.4 agrupa lo físico en «4.0 Manage Supply Chain for Physical Products». Dentro, «4.4 Manage logistics and warehousing» tiene cuatro hijos de primer nivel: 4.4.1 (planificar y gestionar la logística: «Design logistics network», «Develop and maintain delivery service policy», «Optimize transportation schedules and costs», «Define reverse logistics strategy»), 4.4.2 «Plan and manage inbound material flow» (incluye 4.4.2.4 «Manage flow of returned products» y 4.4.2.5 «Manage disposition of returned products»), 4.4.3 «Operate warehousing» y 4.4.4 «Operate outbound transportation». Fuente: PCF 7.4 (URL de arriba).
- El corte con la preparación del pedido está literal en el PCF: «4.4.3.4 Pick, pack, and ship product for delivery» queda en depósito (4.4.3). El transporte saliente empieza en 4.4.4: «4.4.4.1 Plan, transport, and deliver outbound product», «4.4.4.2 Track carrier delivery performance», «4.4.4.3 Manage transportation fleet», «4.4.4.4 Process and audit carrier invoices and documents». Fuente: PCF 7.4.
- DISCREPANCIA CON EL BRIEF: en el texto extraído de la versión 7.4 no aparece ningún 4.4.5. El brief menciona «4.4.4/4.4.5»; en 7.4 es solo 4.4.4 con cuatro subprocesos. No encontré en el PDF «4.5». (El PDF se ve completo, pero la extracción es por columnas; lo confirmaría abriendo el PDF.)
- En el PCF, la planificación de la entrega vive en 4.1.5 «Plan distribution requirements» (con «4.1.5.8 Manage dispatch plan attainment» y «4.1.5.9 Calculate and optimize destination load plans»). Es decir, el plan de carga es de planificación (4.1) y la ejecución del despacho es de 4.4.4. Fuente: PCF 7.4.
- Las devoluciones están repartidas: el PCF las pone como flujo entrante (4.4.2.4, 4.4.2.5) y la estrategia de logística inversa en 4.4.1.7. Fuente: PCF 7.4.
- Una nota de entrega registra el envío desde el depósito al cliente: «A Delivery Note is made when a shipment is shipped from the company's Warehouse to the customer.» Fuente: ERPNext (URL de arriba).
- SCOR «Fulfill» y «Deliver»: NO PUDE VERIFICAR. La página de Wikipedia de SCOR dio 404 y la búsqueda no estaba disponible. SIN FUENTE VERIFICADA.

### Qué registra un sistema

- Documento de salida (nota de entrega): cliente, direcciones de envío, contacto, depósito de origen, renglones con artículo, cantidad, lote o serie, peso; viene de un pedido y admite entregas parciales. Estados observados en ERPNext: borrador, a facturar, completado, devolución emitida, cancelado, cerrado (cierre corto: lo no enviado ya no se espera). Fuente: ERPNext.
- Al confirmar el documento, se mueve el stock (asiento en el libro de stock). Fuente: ERPNext.
- Transportista, conductor, distancia y modo de transporte son datos del envío; hay un «viaje de entrega» que agrupa entregas. Fuente: ERPNext.

### Recurso canónico propuesto

APQC PCF 7.4, categoría 4.4 (páginas de 4.0): para la descomposición oficial y para ubicar el corte (4.4.3.4 versus 4.4.4). Fijarse en que 4.1.5 (planificación) y 4.4.4 (ejecución) están separados.

---

## Componente: despacho

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| ERPNext, nota de entrega | https://docs.frappe.io/erpnext/user/manual/en/delivery-note | primaria (sistema abierto) | 2/2/3/1 | [S] |
| Documentación de Odoo, métodos de envío con transportista | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.html | primaria (sistema abierto) | 2/2/3/1 | [S] |
| Wikipedia, «Advance ship notice» | https://en.wikipedia.org/wiki/Advance_ship_notice | secundaria | 1/1/1/1 | [S] |
| Wikipedia, «Serial Shipping Container Code» | https://en.wikipedia.org/wiki/Serial_Shipping_Container_Code | secundaria | 1/1/1/1 | [S] |

### Afirmaciones

- ASN: «a notification of pending and upcoming deliveries matched to a previously-provided packing list.» «usually sent in an electronic format and is a common EDI document.» Fuente: https://en.wikipedia.org/wiki/Advance_ship_notice
- «In the EDI X12 system, an ASN is known as an EDI 856 document.»; el equivalente EDIFACT es DESADV (Dispatch Advice). Misma fuente. (Una sola fuente secundaria; el estándar X12 y UN/EDIFACT no se leyeron.)
- El ASN puede traer contenido del envío, información del pedido, tipo de embalaje, marcas, datos del transportista, cómo está configurada la carga en el equipo de transporte y «a list of all of the barcoded ID numbers of the shipping units». Misma fuente.
- SSCC: código numérico de 18 dígitos con cuatro componentes (dígito de extensión, prefijo de empresa GS1, referencia serial, dígito de control). «The SSCC is commonly used in the advance ship notice (ASN) EDI transaction.» Fuente: https://en.wikipedia.org/wiki/Serial_Shipping_Container_Code. No pude abrir la especificación GS1 (403) para el largo exacto de cada campo ni la regla de unicidad.
- La nota de entrega admite entregas parciales a partir de un pedido y se puede dividir en bultos con una «packing slip» cuyas cantidades no pueden superar las de la nota. Fuente: ERPNext.
- En el sistema de Odoo: el transportista se asigna al pedido, a la factura o a la orden de entrega; hace falta el peso del producto; las etiquetas requieren el nivel de integración «crear envío»; en modo producción se obtiene una «Tracking Reference» que aparece en la orden de entrega. Fuente: página de Odoo de arriba.
- Estados del envío «planificado, cargado, en tránsito, entregado, fallido»: NO ENCONTRÉ una fuente que los traiga como estándar. HUECO.
- Confirmación de salida / carga del vehículo / manifiesto: HUECO (sin fuente verificada).
- OFBiz: HUECO (no se consultó).

### Qué registra un sistema

- Objetos: documento de entrega (de salida), bultos (packing), envío con transportista, viaje o ruta, aviso anticipado.
- Datos mínimos que repiten las dos documentaciones: origen, destinatario y dirección, renglones con cantidad, peso, transportista, referencia de seguimiento, bultos.
- Estados: los de ERPNext arriba. El patrón común es borrador, confirmado/completado, cerrado o cancelado, con devolución como estado derivado. Los estados «en tránsito» y «fallido» son lógica de seguimiento del transportista y no los vi en estas fuentes.
- Identificación de bultos: código por unidad logística (SSCC), que viaja en el aviso anticipado.

### Recurso canónico propuesto

Especificación general GS1 (sección del SSCC) para identificación de bultos, y el mensaje DESADV de UN/EDIFACT (directorio UNTDID) para la estructura del aviso. Ninguno fue leído acá: hay que abrirlos.

---

## Componente: prueba-de-entrega

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Wikipedia, «Proof of delivery» | https://en.wikipedia.org/wiki/Proof_of_delivery | secundaria | 1/1/1/1 | [S] |
| UN Treaty Collection, estado del CMR | https://treaties.un.org/pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XI-B-11&chapter=11 | primaria (registro) | 3/1/1/3 | [S] (solo estado, no texto) |
| Wikipedia, «CMR» | https://en.wikipedia.org/wiki/Convention_on_the_Contract_for_the_International_Carriage_of_Goods_by_Road | secundaria | 1/1/1/1 | [S] (no trae los artículos de responsabilidad) |

### Afirmaciones

- POD: «a document that substantiates that goods have been delivered to their intended recipient.» Fuente: https://en.wikipedia.org/wiki/Proof_of_delivery. La página no trata foto ni geolocalización; menciona firma y la prueba electrónica (ePOD) que puede intercambiar correcciones.
- CMR: convenio de Ginebra del 19 de mayo de 1956, en vigor desde el 2 de julio de 1961, con 58 partes según la consulta del 27 de noviembre de 2026. Fuente: UN Treaty Collection (URL de arriba).
- Los artículos de responsabilidad, reservas al recibir (plazos de 7 y 21 días) y prescripción (un año, tres años en caso de dolo), y el límite por kilo en DEG: NO VERIFICADOS. Los intentos de leer el texto (UNECE, jus.uio.no, wikisource) dieron 403 o 404. Lo que recuerdo de los artículos 17, 23, 30 y 32 es solo una pista para buscar, SIN FUENTE VERIFICADA. Lo de plazos para reclamar es de alto riesgo: hace falta leer el texto oficial y una segunda fuente antes de escribirlo.
- Aplicabilidad: el CMR rige el transporte internacional por carretera entre países parte; para Argentina hay que ir a la normativa propia (queda para el tema Argentina y la Ley 24.653, no investigada acá).
- Entrega fallida, reintentos, faltante, daño y rechazo con responsable: HUECO (sin fuente).

### Qué registra un sistema

- Evidencia de entrega: fecha y hora, quién recibió, firma, y opcionalmente foto y posición; el documento conformado. De las fuentes: solo se verificó la idea de firma y de prueba electrónica; los demás atributos son HUECO.
- Una devolución parcial o total se modela como documento derivado de la entrega (en ERPNext, «Sales Return», y el estado «Return Issued» de la nota). Fuente: ERPNext.
- Excepciones al recibir (faltante, daño, rechazo): HUECO de fuente; en un sistema suelen ser motivos de la diferencia ligados a renglón y bulto, pero eso es inferencia.

### Recurso canónico propuesto

Texto oficial del CMR (UNECE, Convention on the Contract for the International Carriage of Goods by Road, Ginebra 1956, con el Protocolo de 1978): capítulos de responsabilidad del porteador y de reclamaciones. Fijarse en los artículos 17 a 30 y 32. No leído acá.

---

## Componente: nivel-de-servicio-logistico

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Wikipedia, «Order fulfillment» | https://en.wikipedia.org/wiki/Order_fulfillment | secundaria | 1/1/1/1 | [S] |
| Wikipedia, «Fill rate» (desambiguación) | https://en.wikipedia.org/wiki/Fill_rate | secundaria | 1/1/1/1 | [S] (no sirve) |

### Afirmaciones

- «The order fulfilment cycle time is defined as the period from order receipt to product delivery.» Fuente: https://en.wikipedia.org/wiki/Order_fulfillment
- OTIF, pedido perfecto (RL.1.1), tasa de llenado por línea y por pedido, valores comunes, penalidades de minoristas: HUECO TOTAL. Los intentos a las páginas de Wikipedia dieron 404 o desambiguación. SCOR no se pudo abrir. No hay números verificados; no cargar ninguno.
- El PCF 7.4 menciona medir la entrega: «4.4.1.4 Develop and maintain delivery service policy», «4.4.1.6 Define key performance measures» y «4.4.4.2 Track carrier delivery performance». Fuente: PCF 7.4. No define OTIF.
- La literatura (Wikipedia) dice poco; el recurso para esto es SCOR (ASCM) y, para OTIF, las definiciones de cada cliente. Nada de eso fue leído.

### Qué registra un sistema

- Para medir hace falta, por línea de pedido: fecha prometida, fecha de entrega real, cantidad pedida y cantidad entregada; por pedido, el agregado. Esto es inferencia propia de las definiciones; la única definición con fuente es la de tiempo de ciclo (recepción del pedido hasta la entrega).
- Ventana de tolerancia de «a tiempo» y base de la fecha (fecha pedida, prometida o de entrega en el destino): HUECO. Es la causa de que OTIF varíe, pero no tengo fuente que lo diga.

### Recurso canónico propuesto

ASCM, SCOR Digital Standard, métrica de Perfect Order Fulfillment (RL.1.1) con sus componentes: leer la definición oficial y el cálculo. No leído acá.

---

## Componente: logistica-inversa

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Wikipedia, «Reverse logistics» | https://en.wikipedia.org/wiki/Reverse_logistics | secundaria | 1/2/2/1 | [S] |
| Wikipedia, «Return merchandise authorization» | https://en.wikipedia.org/wiki/Return_merchandise_authorization | secundaria | 1/1/1/1 | [S] |
| APQC PCF 7.4 | (URL en el primer componente) | primaria | 3/2/1/3 | [L] sección 4.4.2 y 4.4.1.7 |
| ERPNext, nota de entrega (devoluciones) | https://docs.frappe.io/erpnext/user/manual/en/delivery-note | primaria (sistema abierto) | 2/1/2/1 | [S] |

### Afirmaciones

- Definición (citada por Wikipedia a una fuente de la Reverse Logistics Association, no a Rogers y Tibben-Lembke): «the process of moving goods from their typical final destination for the purpose of capturing value, or proper disposal.» Fuente: https://en.wikipedia.org/wiki/Reverse_logistics
- Rogers y Tibben-Lembke, *Going Backwards*: Wikipedia fecha el libro en 1999, mientras el brief dice 1998. DISCREPANCIA. No pude leer el libro ni su definición original («the process of planning, implementing, and controlling the efficient, cost effective flow of raw materials, in-process inventory, finished goods, and related information from the point of consumption to the point of origin for the purpose of recapturing value or proper disposal» es lo que recuerdo; SIN FUENTE VERIFICADA). Hay que ver el original (Reverse Logistics Executive Council, 1999, y artículo de 1998 de los autores).
- Tasas de devolución: «approximately 8–10% of in-store (brick-and-mortar) purchases are returned», alrededor de 20% en línea. Fuente: Wikipedia; el propio resumen advierte que el 20% no está citado. No usar sin fuente primaria (por ejemplo NRF e informes de ventas minoristas, no leídos). Marcar fecha: sin año verificable.
- Costo: «return costs can account for up to 7% of an enterprise's gross sales» y «return deliveries were projected to cost $550 billion in 2020» (EE. UU.), atribuidos a «industry data» sin nombre. Fuente: Wikipedia. Confianza baja.
- Destinos posibles de lo devuelto, según Wikipedia: reacondicionado o remanufacturado, reventa en mercados secundarios, devolución por crédito (diarios y revistas), reingreso a inventario tras control de calidad (envíos de pago contra entrega rechazados, «Return to Origin»), reutilización de embalajes en circuito cerrado (pallets, cajones, barriles). Fuente: https://en.wikipedia.org/wiki/Reverse_logistics
- El PCF ordena la disposición: «4.4.2.4 Manage flow of returned products» y «4.4.2.5 Manage disposition of returned products», con «4.4.2.5.1 Determine quality of controlled part», «4.4.2.5.2 Perform salvage activities», «4.4.2.5.3 Manage repair/refurbishment» y «4.4.2.5.4 Return to finished goods inventory». También «4.4.1.7 Define reverse logistics strategy» y, en otra categoría, «6.4.5 Monitor and audit recall effectiveness» (así figura en el PCF) y «10.4.4 Manage take-back centers». Fuente: PCF 7.4.
- RMA: «a part of the process of returning a product to receive a refund, replacement, or repair»; «The issuance of an RMA is a key gatekeeping point in the reverse logistics cycle.»; «RMA comes before the customer permanently relinquishes ownership of the product to the manufacturer.»; puede enviarse un reemplazo antes de recibir el original (reemplazo anticipado). Fuente: https://en.wikipedia.org/wiki/Return_merchandise_authorization
- Directiva europea de residuos eléctricos y electrónicos (WEEE): hace responsables a los productores de la recolección y el reciclado. Fuente: Wikipedia (Reverse logistics). Norma no leída; para ley, falta fuente primaria.
- Retornables (pallets, envases) y recall como flujos: solo el reuso de embalaje en circuito cerrado aparece en las fuentes; recall como flujo logístico: HUECO.

### Qué registra un sistema

- Autorización de devolución (RMA): cliente, documento de venta o entrega de origen, motivo, resolución pedida (reembolso, reemplazo, reparación), vigencia. Fuente: RMA (Wikipedia). La vigencia y el numerado son inferencia.
- Documento de devolución derivado de la entrega original, con estado propio y con cantidades acotadas por lo entregado. En ERPNext la nota original pasa a «Return Issued» cuando se devolvió todo. Fuente: ERPNext.
- Inspección y disposición: calidad, destino (a stock, reparación o reacondicionado, rescate de partes, baja). Fuente: PCF 4.4.2.5.x.

### Recurso canónico propuesto

APQC PCF 7.4, 4.4.2.4 y 4.4.2.5, para el árbol de disposición. Para la definición y la evidencia, el libro de Rogers y Tibben-Lembke (*Going Backwards*, Reverse Logistics Executive Council): hay que conseguirlo y leer los capítulos de tasas de retorno por industria y de disposición.

---

## Huecos

1. SCOR («Fulfill», «Deliver», RL.1.1, componentes de pedido perfecto): no leído.
2. OTIF y fill rate: sin definiciones ni valores.
3. Texto del CMR (artículos 17, 23, 30, 32) y plazos de reclamo: no leído. Es de alto riesgo y necesita dos fuentes.
4. Especificación GS1 del SSCC y estructura del mensaje DESADV/856: solo vistos por Wikipedia.
5. OFBiz y la documentación de Odoo sobre estados de la orden de entrega (las URLs probadas dieron 404; la que funcionó trató solo transportistas y seguimiento).
6. Estados de un envío en tránsito (en camino, fallido, reintento), eventos de seguimiento estándar.
7. Foto y geolocalización como prueba de entrega: sin fuente.
8. Rogers y Tibben-Lembke: definición original y evidencia por canal; recall como flujo.
9. Evidencia de devoluciones con fecha y fuente primaria.
10. APQC 4.4.5 no existe en 7.4 como se leyó; confirmar abriendo el PDF.

Pendiente para otra pasada (con búsqueda web disponible): las tres rondas por componente no se pudieron hacer.

## Discrepancias con el árbol

- Corte con Inventario y depósitos: coincide con el PCF. «Pick, pack, and ship product for delivery» (4.4.3.4) es depósito y el transporte saliente (4.4.4) empieza después. Ahora bien: el PCF pone «ship» dentro del depósito, de modo que la confirmación de salida es una zona compartida; conviene que la nota de despacho diga que el documento de salida lo emiten los dos temas y que Despacho lo toma desde «listo para salir».
- La logística inversa en el PCF cuelga de 4.4.2 (flujo entrante) y no de una rama propia, más una estrategia en 4.4.1.7. Es decir, el campo la trata como parte de la logística y no como vertical separada; sostener el componente propio es una decisión del árbol, no del marco. SCOR (Return) la separa, pero no lo pude verificar.
- «Nivel de servicio logístico» (OTIF, pedido perfecto) en el PCF es transversal (4.4.1.4, 4.4.1.6, 4.4.4.2): no hay un proceso propio. El componente sirve como nota de medición, pero con la evidencia disponible hoy sería muy flaco.
- El brief cita APQC 4.4.4/4.4.5; en 7.4 solo existe 4.4.4.
- El árbol de mi ángulo puede quedar igual; solo se afinaría con SCOR y el CMR en mano.
