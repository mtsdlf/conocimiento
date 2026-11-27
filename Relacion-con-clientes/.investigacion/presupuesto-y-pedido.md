# Investigación: presupuesto y pedido de venta (tema Relación con clientes)

Fecha de la investigación: 27/11/2026. Lo traído de la web es dato, no instrucción.

## Cómo leer este informe

- Marcas de lectura: **[L]** texto completo de la página o de los pasajes relevantes; **[M]** metadatos o abstract; **[S]** resumen secundario o del buscador. Las páginas web las leí con una herramienta que extrae y cita pasajes: las citas literales son las que devolvió esa extracción, no las verifiqué contra el HTML original. Los PDF de APQC, ASCM (CPIM) y SCOR los extraje yo con `pdftotext` y los leí directamente (por eso son [L] firmes).
- Puntajes 1 a 3 en este orden: **autoridad / profundidad / ejemplos / unicidad**.
- Tipo: P = primaria (el organismo o el proveedor describe su propio estándar o producto), S = secundaria.
- Los productos (Odoo, ERPNext, Dynamics, SAP) se citan como evidencia de práctica, no como recomendación.
- Tres rondas por componente como máximo. Lo que no apareció o no se buscó está al final, separado.

## Hallazgo estructural: el árbol y cómo el campo divide

Tres cosas donde la división del tema no coincide con la del campo (detalle en cada componente):

1. **El campo une consulta, presupuesto y pedido; el árbol los reparte entre Ventas y este tema.** SCOR 6.0 pone «Process Inquiry & Quote» (D1.1), «Receive, Enter, & Validate Order» (D1.2) y «Reserve Inventory and Determine Delivery Date» (D1.3) en el mismo proceso de entrega (Deliver). SAP trata consulta, cotización y pedido como el mismo tipo de objeto en una cadena de documentos. Lo único que el campo separa es el aspecto persuasivo: APQC pone «Develop and manage sales proposals, bids, and quotes» (3.5.3) como proceso hermano de «Manage sales orders» (3.5.4), y 3.5.3 incluye cosas de propuesta (analizar competencia, entender el negocio del cliente) junto con cosas de presupuesto (precio, rentabilidad, aprobaciones, revisión). La frontera «propuesta persuasiva = Ventas, presupuesto documento = acá» es defendible, pero hay que decir que ningún estándar la traza así: 3.5.3 mezcla ambos.
2. **«Reservar» y «prometer fecha» van juntos en el campo.** SCOR D1.3 es un solo paso: «Reserve Inventory and Determine Delivery Date». APQC 3.5.4.3 «Determine availability» también. El árbol pone la reserva en Inventario y la promesa de fecha acá. Se puede sostener (el cálculo de disponibilidad lo hace la oferta, la promesa al cliente es comercial), pero el cálculo de ATP sale del plan maestro y del inventario (ver F), de modo que hay que escribir el contrato entre ambos temas: quién calcula, quién promete.
3. **Un presupuesto aceptado no siempre es otro documento.** Odoo: «Once a quotation has been confirmed, it officially turns into a sales order» (el mismo registro cambia de estado). ERPNext: se crea un Sales Order nuevo desde la cotización («Create > Sales Order»), y la cotización queda «Ordered». SAP: son documentos distintos con referencia (document flow) aunque en tablas compartidas. La nota debe explicar los dos modelos (un registro que cambia de estado, o dos registros enlazados), porque quien construye software tiene que elegir.

---

## A. El presupuesto como documento (renglones, estados, validez, numeración, diferencia con la propuesta)

### Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Leído |
|---|---|---|---|---|
| ERPNext (Frappe), manual «Quotation» | https://docs.frappe.io/erpnext/user/manual/en/quotation | P (proveedor) | 2/2/2/2 | [L] |
| Odoo 19, «Create quotations» | https://www.odoo.com/documentation/19.0/applications/sales/sales/sales_quotations/create_quotations.html | P | 2/2/2/1 | [L] hasta el carácter 100000 de 111409 |
| Odoo 17, «Quotation templates» | https://www.odoo.com/documentation/17.0/applications/sales/sales/send_quotations/quote_template.html | P | 2/1/2/1 | [L] |
| Odoo 18, «Quotation deadlines» | https://www.odoo.com/documentation/18.0/applications/sales/sales/sales_quotations/deadline.html | P | 2/1/1/1 | [L] |
| APQC PCF v7.4 (agosto 2024), copia IFRC | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | P | 3/2/1/3 | [L] (pp. de 3.5) |
| SAP Help (R/3 4.7), «Sales Document Types» | https://help.sap.com/saphelp_470/helpdata/en/dd/55fb06545a11d1a7020000e829fd11/content.htm | P (histórico) | 2/2/2/2 | [L] |
| Ley 24.240 (InfoLEG), art. 21 | https://servicios.infoleg.gob.ar/infolegInternet/anexos/0-4999/638/texact.htm | P (norma) | 3/2/2/3 | [L] |
| ARCA, «Situaciones especiales de emisión de comprobantes» | https://www.arca.gob.ar/facturacion/comprobantes/situaciones-especiales.asp | P | 3/1/1/3 | [L] |
| Código Civil y Comercial art. 974, transcripción en leyfacil | https://leyfacil.com.ar/codigo-civil-y-comercial/articulo-974/ | S (transcripción) | 1/1/1/2 | [L] |

Odoo 17/18/19 y la plantilla repiten el mismo patrón (días de validez en la plantilla, fecha editable): cuentan como una sola fuente.

### Afirmaciones

- Qué es: ERPNext lo define como «a submittable sales transaction that can be shared as a proposal and converted into a Sales Order after acceptance». https://docs.frappe.io/erpnext/user/manual/en/quotation
- Estados en ERPNext: Draft («The Quotation is editable and has not been confirmed.»), Open («The submitted offer is active and awaits an outcome.»), Ordered («A Sales Order has been created from the Quotation.»), Lost («The offer did not convert. Record the reason for later analysis.»), Expired («The Valid Till date has passed.»), Cancelled. https://docs.frappe.io/erpnext/user/manual/en/quotation
- Validez: el campo «Valid Till» es «The last date on which the offer is valid.» https://docs.frappe.io/erpnext/user/manual/en/quotation
- Odoo toma la validez de una configuración global («Default Quotation Validity»); con plantilla, la fecha sale de la validez de la plantilla; se puede pisar antes de enviar. https://www.odoo.com/documentation/19.0/applications/sales/sales/sales_quotations/create_quotations.html y https://www.odoo.com/documentation/18.0/applications/sales/sales/sales_quotations/deadline.html. Con 0 días la plantilla vale sin vencimiento: «Setting it to 0 keeps the template valid indefinitely» (resumen del extractor, no cita textual) https://www.odoo.com/documentation/17.0/applications/sales/sales/send_quotations/quote_template.html
- Odoo, nombre de la validez en la plantilla de la versión 18: campo «Quotation expires after». https://www.odoo.com/documentation/18.0/applications/sales/sales/sales_quotations/deadline.html
- Presupuesto en la jerarquía de procesos de APQC: 3.5.3 «Develop and manage sales proposals, bids, and quotes» (11779) con hijos 3.5.3.1 «Receive Request For Proposal (RFP)/Request For Quote (RFQ)», 3.5.3.2 «Refine customer requirements», 3.5.3.4 «Perform competitive analysis», 3.5.3.6 «Understand customer business and requirements», 3.5.3.9 «Develop pricing and scheduling estimates», 3.5.3.10 «Conduct profitability analysis», 3.5.3.11 «Manage internal reviews», 3.5.3.12 «Manage internal approvals», 3.5.3.13 «Submit/present bid/proposal/quote to customer», 3.5.3.14 «Revise bid/proposal/quote», 3.5.3.15 «Manage notification outcome». https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf
- SAP lo agrupa como «Presales» junto con la consulta: «Inquiry (IN), Quotation (QT)». La página dice que «you may add your own sales document types». https://help.sap.com/saphelp_470/helpdata/en/dd/55fb06545a11d1a7020000e829fd11/content.htm
- Odoo, validez no es solo cortesía: el vencimiento aparece en la vista previa del cliente («clearly displays when that specific offer expires»). https://www.odoo.com/documentation/18.0/applications/sales/sales/sales_quotations/deadline.html
- Argentina, contenido mínimo: la Ley 24.240 art. 21 exige que «el prestador del servicio debe extender un presupuesto que contenga como mínimo los siguientes datos», entre ellos «La descripción del trabajo a realizar», «Una descripción detallada de los materiales a emplear», «Los precios de éstos y la mano de obra», «El tiempo en que se realizará el trabajo», «Si otorga o no garantía y en su caso, el alcance y duración de ésta», «El plazo para la aceptación del presupuesto». Aviso: el art. 21 empieza con «En los supuestos contemplados en el artículo anterior»; no leí el art. 20, así que no sé a qué servicios aplica (la página lo trata como servicio técnico y reparaciones). No se puede generalizar a todo presupuesto sin leerlo. https://servicios.infoleg.gob.ar/infolegInternet/anexos/0-4999/638/texact.htm
- Argentina, leyenda: «Las notas de pedido, órdenes de trabajo, presupuestos y/o documentos de análogas características se identificarán con la letra "X" y con la leyenda "DOCUMENTO NO VALIDO COMO FACTURA"». https://www.arca.gob.ar/facturacion/comprobantes/situaciones-especiales.asp (el texto me llegó partido en dos citas, la unión es mía).
- Argentina, vigencia como oferta: CCyC art. 974: «La oferta obliga al proponente, a no ser que lo contrario resulte de sus términos, de la naturaleza del negocio o de las circunstancias del caso.» y «Los plazos de vigencia de la oferta comienzan a correr desde la fecha de su recepción, excepto que contenga una previsión diferente.» https://leyfacil.com.ar/codigo-civil-y-comercial/articulo-974/ (transcripción secundaria; falta cotejar con InfoLEG).

### Discrepancia

Odoo (mismo registro que cambia de estado) contra ERPNext y SAP (documentos separados enlazados): ver hallazgo 3. No son contradictorios, son dos diseños.

### Recurso canónico propuesto

Para el patrón de estados y validez: manual «Quotation» de ERPNext. Para el lugar del presupuesto en el proceso: APQC PCF 3.5.3. Para Argentina: Ley 24.240 art. 21 + leyenda de ARCA + CCyC 974. No hay un estándar de la academia o de ASCM que defina «presupuesto»; el canónico es una convergencia de práctica.

---

## B. Precio y descuentos en el presupuesto

### Fuentes

| Fuente | URL | Tipo | Puntaje | Leído |
|---|---|---|---|---|
| Odoo 17, «Pricing» (listas de precios y descuentos) | https://www.odoo.com/documentation/17.0/applications/sales/sales/products_prices/prices/pricing.html | P | 2/3/3/2 | [L] hasta 100000 de 107540 |
| ERPNext, «Authorization Rule» | https://docs.frappe.io/erpnext/user/manual/en/authorization-rule | P | 2/1/2/3 | [L] |
| APQC PCF v7.4 (3.5.3.9, 3.5.3.10, 3.5.3.12) | ver A | P | 3/1/1/3 | [L] |
| Dynamics 365, «Sales agreements overview» | https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements | P | 2/3/3/3 | [L] |
| Módulos de terceros de Odoo para aprobar pedidos por monto | https://apps.odoo.com/apps/modules/17.0/sale_order_approval | S (módulo de terceros, no la documentación de Odoo) | 1/1/1/1 | [S] |

### Afirmaciones

- De dónde sale el precio: «A pricelist is a list of prices (or price rules) that Odoo uses to determine the appropriate price for a customer.» «Pricelists suggest certain prices, but they can always be overridden on the sales order.» Criterios: períodos y cantidad mínima («the new price in the Price column will be applied to orders of 2 or more products»). Sin criterio coincidente se aplica la lista por defecto. https://www.odoo.com/documentation/17.0/applications/sales/sales/products_prices/prices/pricing.html
- Descuento por renglón y total: la función «allows the ability to set a discount or increase the price on individual items in a sales order»; «Positive values for Disc.% will apply a discount, while negative values can be used to increase the price.» Tres formas: «On All Order Lines», «Global Discount» (se agrega un producto de descuento al pedido), «Fixed Amount». Política de visualización: «Discount included in the price» o «Show public price & discount to the customer». https://www.odoo.com/documentation/17.0/applications/sales/sales/products_prices/prices/pricing.html
- Precio acordado por contrato: en un acuerdo de venta de Dynamics «The prices and discounts of the sales agreement override the prices and discounts that are stated in any trade agreements that exist». https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements
- Aprobación: ERPNext define «Authorization Rule allows configuring a custom authorization / approval on a documents, based on conditions defined»; puede atarse a «Net Total, Grand Total, Discount %»; ejemplo: «If a Sales Order's Grand Total exceeds $1,000, then it should be verified/submitted by the Sales Manager only.» https://docs.frappe.io/erpnext/user/manual/en/authorization-rule
- Margen y aprobación en el proceso: APQC trae como pasos previos a presentar el presupuesto «Develop pricing and scheduling estimates» (3.5.3.9), «Conduct profitability analysis» (3.5.3.10) y «Manage internal approvals» (3.5.3.12). https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf
- Las aprobaciones por monto en Odoo, según el buscador, las dan módulos de terceros con un umbral «Minimum Amount» y un estado «To Approve»; no encontré esa función en la documentación oficial de Odoo [S]. https://apps.odoo.com/apps/modules/17.0/sale_order_approval

### Huecos del componente

- «Margen mínimo» como regla (piso de precio, margen sobre costo) no tiene fuente primaria leída: solo APQC lo nombra como análisis de rentabilidad (3.5.3.10). No leí ERPNext Pricing Rule ni la parte final (7540 caracteres) de la página de precios de Odoo.
- Precio por cantidad y por cliente ya están en `Comercio-electronico/Comercio-B2B/precio-por-cliente.md`: acá solo se enlazan.

### Recurso canónico

Odoo, «Pricing» (por claridad y ejemplos) para lista, cantidad y descuentos; ERPNext «Authorization Rule» para aprobación. Ninguno es estándar; ambos son patrón de práctica.

---

## C. Productos configurables (CPQ)

### Fuentes

| Fuente | URL | Tipo | Puntaje | Leído |
|---|---|---|---|---|
| Forza y Salvador, *Product Information Management for Mass Customization* (Palgrave Macmillan, 2006), copia en vdoc.pub | https://vdoc.pub/documents/product-information-management-for-mass-customization-connecting-customer-front-office-and-back-office-for-fast-and-efficient-customization-5rgv091itko0 | P (libro académico; la copia en vdoc.pub es de dudosa legalidad: se cita la obra, no se recomienda la copia) | 3/3/2/3 | [L] primeros 100000 de 402682 caracteres |
| Felfernig, Hotz, Bagley, Tiihonen, *Knowledge-Based Configuration: From Research to Business Cases* (Morgan Kaufmann, 2014, ISBN 978-0-12-415817-7) | https://shop.elsevier.com/books/knowledge-based-configuration/felfernig/978-0-12-415817-7 | P (libro) | 3/3/2/3 | [M] (ficha); el capítulo en O'Reilly dio 403 |
| ECAI 2006 Workshop on Configuration, *Proceedings* (Sinz y Haag, eds.) | https://fmv.jku.at/ecai-config-ws-2006/W16.pdf | P (actas) | 2/2/1/2 | [L] solo el prefacio |
| Dynamics 365, «Create a sales order for a configurable product» | https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/tasks/create-sales-order-configurable-product | P | 2/1/2/1 | [S] (por el buscador) |
| Oracle JD Edwards, «Understanding Configured Item Sales Orders» | https://docs.oracle.com/en/applications/jd-edwards/supply-chain-manufacturing/9.2/eoabc/understanding-configured-item-sales-orders.html | P | 2/1/2/1 | [S] |
| Odoo 17, plantillas de presupuesto con productos opcionales | https://www.odoo.com/documentation/17.0/applications/sales/sales/send_quotations/quote_template.html | P | 2/1/1/1 | [L] (solo una mención) |

### Afirmaciones

- Qué es configurar: «To offer product variety through product configuration means giving the customer the opportunity to customize the product» (cap. 1, §1.4). Forza y Salvador. https://vdoc.pub/documents/product-information-management-for-mass-customization-connecting-customer-front-office-and-back-office-for-fast-and-efficient-customization-5rgv091itko0
- El proceso va de pedir datos a documentar el producto: «all the activities from the collection of information about customer needs to the release of the product documentation» (cap. 2, §2.1). Dos mitades: «Commercial configuration represents the description of the product the customer is willing to buy» y technical configuration, «all the activities that generate the documentation of the product variant». Mismo enlace.
- Qué le pide la parte comercial al presupuesto: «Price and an indicative delivery time are fundamental outputs of the commercial configuration process.» (cap. 5, §5.2). Y: «it is more difficult to establish the price since each variant requires costs» (cap. 2, §2.2). Mismo enlace. Esto ata CPQ con la promesa de fecha de este tema.
- Cuándo hace falta (variedad y complejidad): «configurability is not a property of the specific product but of the product family» (cap. 2, §2.3). Mismo enlace. No encontré en lo leído un umbral numérico de cuándo conviene un configurador.
- Por qué se usa conocimiento y reglas: el prefacio de las actas dice «Powerful knowledge-representation models are necessary to capture the great variety and complexity of configurable products.» https://fmv.jku.at/ecai-config-ws-2006/W16.pdf
- Los sistemas de gestión lo traen en la línea del presupuesto: Dynamics AX 2012 ofrece «Configure line» en cotizaciones y pedidos solo para artículos con modelo de configuración activo [S]; JD Edwards procesa artículos configurados en pedidos y cotizaciones, y convertir cotización a pedido exige opciones de proceso [S]. Ambos vía buscador, sin lectura.
- Los datos de la ficha del libro de Felfernig: publicado el 13/5/2014, 384 páginas, autores en TU Graz (Felfernig), Univ. de Hamburgo (Hotz), Oracle (Bagley) y Aalto (Tiihonen) [S/M]. https://shop.elsevier.com/books/knowledge-based-configuration/felfernig/978-0-12-415817-7

### Huecos

- «CPQ» como término de industria (configure-price-quote) no apareció en ninguna fuente primaria o académica: es término de proveedores, y no leí ninguna definición literal. Lo que hay es configuración de producto (academia) y configuradores en presupuestos (ERP). Conviene decirlo en la nota.
- Reglas de compatibilidad y paquetes (bundles): no leí texto del libro de Felfernig; falta una cita literal de «constraint» o «compatibility».

### Recurso canónico

Forza y Salvador (2006), caps. 1, 2 y 5, para el concepto y la relación con el presupuesto; Felfernig et al. (2014) como referencia técnica sobre reglas, pendiente de lectura.

---

## D. Versiones, vigencia y aceptación del presupuesto

### Fuentes

| Fuente | URL | Tipo | Puntaje | Leído |
|---|---|---|---|---|
| Odoo 17, «Get a signature to validate» | https://www.odoo.com/documentation/17.0/applications/sales/sales/send_quotations/get_signature_to_validate.html | P | 2/2/2/2 | [L] |
| Odoo 17, «Invoicing policy» | https://www.odoo.com/documentation/17.0/applications/sales/sales/invoicing/invoicing_policy.html | P | 2/1/2/2 | [L] |
| ERPNext, «Sales Order» (campo del pedido de compra del cliente) | https://docs.frappe.io/erpnext/user/manual/en/sales-order | P | 2/3/2/2 | [L] |
| Dynamics 365, «Sales agreements overview» (versiones al confirmar) | ver B | P | 2/3/3/3 | [L] |
| Business Central, «Work with blanket sales orders» (anticipo) | https://learn.microsoft.com/en-CA/dynamics365/business-central/sales-how-to-create-blanket-sales-orders | P | 2/2/2/2 | [L] |
| CCyC art. 974 | ver A | S | 1/1/1/2 | [L] |

### Afirmaciones

- Aceptar por firma en línea (Odoo): el cliente abre el presupuesto en el portal, hace clic en «Sign & Pay», elige firma Auto, Draw o Load y pulsa «Accept & Sign»; después aparecen los medios de pago «only if online payment applies». Al firmar, «the salesperson attached to the sales order is instantly notified that the order is confirmed.» https://www.odoo.com/documentation/17.0/applications/sales/sales/send_quotations/get_signature_to_validate.html
- Aceptar con orden de compra del cliente (ERPNext): el pedido guarda «The customer's purchase-order reference and date». https://docs.frappe.io/erpnext/user/manual/en/sales-order
- Cobrar antes de entregar (Odoo): la política de facturación por defecto es «Invoice what is ordered» (se puede facturar al confirmar); la otra es «Invoice what is delivered» («The delivery must be validated before an invoice can be created»). La página de anticipos de Odoo no la leí. https://www.odoo.com/documentation/17.0/applications/sales/sales/invoicing/invoicing_policy.html
- Anticipo en el pedido marco (Business Central): la ficha del pedido tiene una pestaña de prepago con «summary information about any prepaid amounts». https://learn.microsoft.com/en-CA/dynamics365/business-central/sales-how-to-create-blanket-sales-orders
- Convertir en pedido (ERPNext): cuando el cliente acepta, «Create > Sales Order» sobre la cotización presentada; si la cotización tenía alternativas, «ERPNext may ask which alternative item to select». https://docs.frappe.io/erpnext/user/manual/en/quotation
- Confirmar en Odoo: «Once a quotation has been confirmed, it officially turns into a sales order». «Lock Confirmed Sales» («Ensure no further edits can be made to confirmed orders.») https://www.odoo.com/documentation/19.0/applications/sales/sales/sales_quotations/create_quotations.html
- Versiones: Dynamics guarda historial al confirmar un acuerdo («When you confirm a sales agreement, the current version of the sales agreement is stored in a history table») y permite «preview or print all revisions of the confirmations», para compartirlas con el cliente. https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements ; APQC nombra el paso «Revise bid/proposal/quote» (3.5.3.14). La revisión de presupuestos como tal (número de versión, qué conserva) no la encontré documentada en Odoo ni ERPNext.
- Si cambia el precio entre el presupuesto y el pedido: en Odoo la lista «suggest[s] certain prices» y se puede pisar en el pedido; en un acuerdo de Dynamics con «Price and discount is fixed», cambiar el precio de un renglón rompe el vínculo: «If the price is changed on the order line, the link to the commitment is broken.» Ninguna de las dos habla de un presupuesto vencido que se acepta tarde (hueco).
- Ley argentina: aceptar dentro del plazo perfecciona el contrato (CCyC art. 974, plazos de vigencia). El resumen del buscador agrega que el art. 980 dice que entre ausentes se perfecciona cuando el proponente recibe la aceptación en plazo [S, sin texto literal].

### Hueco

Numeración del presupuesto (series, prefijos, cómo se numeran las revisiones): no busqué con ronda propia. Es un hueco no cubierto, no un hallazgo negativo.

### Recurso canónico

Para aceptación y conversión: Odoo «Get a signature to validate» + ERPNext «Quotation». Para versiones, el patrón de Dynamics (historial al confirmar). Para Argentina, CCyC 974 contra InfoLEG.

---

## E. El pedido de venta: documento, estados, qué dispara y entrada de pedido

### Fuentes

| Fuente | URL | Tipo | Puntaje | Leído |
|---|---|---|---|---|
| ERPNext, «Sales Order» | https://docs.frappe.io/erpnext/user/manual/en/sales-order | P | 2/3/2/2 | [L] |
| Odoo, creación y confirmación (ver A) y entrega de un paso | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.html | P | 2/1/2/1 | [L] |
| APQC PCF v7.4, 3.5.4 «Manage sales orders» (10185) | ver A | P | 3/2/1/3 | [L] |
| APQC, medida «Total cost to perform the process "manage sales orders"» | https://apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/total-cost-perform-process-manage-3 | P | 3/1/1/2 | [S] (403 al abrir) |
| SCOR 6.0, *Quick Reference* (Supply-Chain Council), copia en Georgia Tech | https://www2.isye.gatech.edu/~lfm/8851/Sources/SCOR/SCORv6quickref.pdf | P (antigua) | 2/1/1/3 | [L] (títulos de proceso) |
| SAP Help R/3 4.7, «Sales Document Types» | ver A | P | 2/2/2/2 | [L] |
| Magal y Word, *Integrated Business Processes with ERP Systems* (Wiley, 2011), cap. 5 «The Fulfillment Process» | https://www.oreilly.com/library/view/integrated-business-processes/9780470478448/14_chap05.html | P (libro) | 3/3/2/2 | [S] (403; solo título y reseña del buscador) |
| Monk y Wagner, *Concepts in Enterprise Resource Planning* | https://scholarworks.wmich.edu/books/493 | P (libro) | 3/3/2/2 | [S] (diapositivas docentes de la 2.ª ed., de segunda mano) |

### Afirmaciones

- Qué es: un Sales Order «records a customer's confirmed request», con renglones, precios, cantidades y condiciones. Presentarlo «confirms the commitment and makes it available for the next steps». https://docs.frappe.io/erpnext/user/manual/en/sales-order
- Estados en ERPNext: Draft («Saved but not confirmed»), To Deliver and Bill («Submitted; delivery and billing are pending»), To Deliver, To Bill, On Hold («Processing is paused»), Closed («Remaining fulfillment was intentionally closed»). Mismo enlace. Observación: los estados son un cruce de dos ejes (entrega y facturación), no una línea.
- Qué dispara: «Next steps include Delivery Notes, Sales Invoices, and Payment Entries» (resumen del extractor). En Odoo, confirmar un pedido crea la entrega («Create a sales order … click Confirm. Open the Delivery smart button»). https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.html
- Fecha prometida en el pedido: el campo «Delivery Date» es «The default promised date»; «An item row can use a different date for split delivery schedules.» https://docs.frappe.io/erpnext/user/manual/en/sales-order
- Dónde está en un estándar de proceso (APQC 7.4): 3.5.4 «Manage sales orders» con 3.5.4.1 «Accept and validate sales orders» (10194), 3.5.4.2 «Collect and maintain account information» (con 3.5.4.2.1 a 3.5.4.2.8: «Administer key account details», «Retrieve full customer details», «Modify involved party details», «Record address details», «Record contact details», «Record key customer communication», «Review involved party information», «Terminate involved party information»), 3.5.4.3 «Determine availability» (10196), 3.5.4.4 «Determine fulfillment process» (10197), 3.5.4.5 «Process back orders and updates» (10199), 3.5.4.6 «Handle sales order inquiries including post-order fulfillment transactions» (10200). https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf
- Discrepancia de versiones de APQC: el buscador afirmó que en la 7.2.1 de Consumer Products el 3.5.4.5 es «Enter orders into system» y que en la 7.4 ya no está [S]; en la 7.4 que leí, 3.5.4.5 es «Process back orders and updates». No abrí la 7.2.1; no se puede afirmar el cambio. Citar siempre la versión.
- En SCOR 6.0 (producto en stock): D1.1 «Process Inquiry & Quote», D1.2 «Receive, Enter, & Validate Order», D1.3 «Reserve Inventory and Determine Delivery Date», D1.4 «Consolidate Orders»; para producto contra pedido (D2): D2.2 «Receive, Configure, Enter and Validate Order», D2.3 «Reserve Resources and Determine Delivery Date». https://www2.isye.gatech.edu/~lfm/8851/Sources/SCOR/SCORv6quickref.pdf . Discrepancia con lo pedido: en SCOR 6.0 no hay un proceso llamado solo «Order»; el buscador dice que versiones posteriores dividen «Order» y «Fulfill» (ver huecos, sin leer).
- Canales de entrada: no encontré una fuente que los enumere como «order entry channels». Lo único leído: Odoo, un producto recurrente vendido en la tienda en línea «will automatically create and confirm subscription quotations in the backend» (https://www.odoo.com/documentation/17.0/applications/sales/subscriptions.html). Las notas del Comercio-B2B ya cubren los canales; no repetir.
- Pedido y pedido por catálogo en la lectura de libros de texto: según diapositivas de curso basadas en Monk y Wagner (2.ª ed.) [S], el pedido puede partir de datos de una consulta o cotización y eso «minimiza errores»; no es lectura del libro.

### Recurso canónico

Estructura de proceso: APQC PCF 3.5.4 (citar versión 7.4) y SCOR D1.1 a D1.3. Documento y estados: ERPNext «Sales Order». Texto de libro, por leer: Magal y Word cap. 5 y Monk y Wagner.

---

## F. Disponibilidad y fecha prometida (ATP, CTP)

### Fuentes

| Fuente | URL | Tipo | Puntaje | Leído |
|---|---|---|---|---|
| ASCM/APICS, *CPIM* 6.1 (2019) Excerpt, sección F, cita del *APICS Dictionary* 15.ª ed. | https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf | P | 3/3/3/3 | [L] |
| Microsoft Learn, «Order promising concepts» (Dynamics 365 SCM) | https://learn.microsoft.com/en-us/training/modules/set-up-order-cash-supply-chain-management/order-promising | P | 2/3/3/2 | [L] |
| Wikipedia, «Available-to-promise» | https://en.wikipedia.org/wiki/Available-to-promise | S | 1/1/1/1 | [L] |
| APQC PCF 3.5.4.3 | ver E | P | 3/1/1/3 | [L] (solo el título) |
| Infor LN, ATP y CTP | https://docs.infor.com/ln/2026.10/en-us/lnolh/cpatpctpug/cpomat000100.html | P (proveedor) | 2/2/2/1 | [S] |

### Afirmaciones

- Definición ASCM de ATP: «the uncommitted portion of a company's inventory and planned production maintained in the master schedule to support customer-order promising. The ATP quantity is the uncommitted inventory balance in the first period and is normally calculated for each period in which an MPS receipt is scheduled. In the first period, ATP includes on-hand inventory less customer orders that are due and overdue.» (la fuente aclara «in part»). https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf
- Fórmulas (método discreto): «First Period ATP = Beginning Inventory − Sum of Customer Orders Before Period Containing First Scheduled MPS Receipt» con el ejemplo «70 units − 48 units = 22 units»; «ATP for Periods Containing MPS = Scheduled MPS Receipt − Sum of Customer Orders Before Next Period Containing Scheduled MPS Receipt», «100 units − 66 units = 34 units». El texto aclara que existen otros dos métodos (acumulado con y sin mirada hacia adelante) que no presenta. Mismo enlace.
- Definición ASCM de CTP (*Dictionary* 15.ª ed.): «The process of committing orders against available capacity as well as inventory. This process may involve multiple manufacturing or distribution sites. Used to determine when a new or unscheduled customer order can be delivered. Employs a finite-scheduling model of the manufacturing system to determine when an item can be delivered. … The objective is to reduce the time spent by production planners in expediting orders and adjusting plans because of inaccurate delivery-date promises.» Mismo enlace.
- Cómo lo hace un sistema (Dynamics): cinco métodos de control de la fecha de entrega: None («assumes that stock is always available»), Sales lead time («doesn't consider stock availability, known demand, or planned supply»), ATP («the quantity of an item that's available and that the company can promise to a customer on a specific date. The ATP calculation includes uncommitted inventory, lead times, planned receipts, and issues»), ATP + issue margin («the time that's required to prepare the items for shipment») y CTP («based on a dynamic plan (sales order line explosion). It checks availability and lead-time components in the BOM and process time in the routes of the finished product»). https://learn.microsoft.com/en-us/training/modules/set-up-order-cash-supply-chain-management/order-promising
- La misma página distingue dos fechas: «Requested ship date» y «Requested receipt date»; y una pantalla de «Delivery alternatives» con entrega parcial, otro sitio, otro transporte. Mismo enlace. Esto sirve para el límite con Cadena de suministro: la fecha de recepción depende del transporte.
- Quién es dueño de qué: en ASCM el ATP vive en el plan maestro de producción (MPS) y lo calculan los planificadores; el vendedor lo consulta («sales professionals will be able to view available-to-promise information in the organization's master schedule», CPIM excerpt). El pedido acá solo consume y compromete esa cifra. Esto sostiene la regla del tema («la fecha prometida es de acá»), pero el cálculo es de Inventario/Planificación.
- Wikipedia (secundaria): ATP es «a business function that provides a response to customer order inquiries, based on resource availability»; distingue Gross ATP y Net ATP; no define CTP y no da fórmula. Cita a Ball et al. (2004) y Zhao (2005, *Annals of Operations Research* 135, 65-85). https://en.wikipedia.org/wiki/Available-to-promise
- APQC 3.5.4.3 «Determine availability» (10196): título leído en el PDF 7.4. La definición («estimate capacity needed to fill orders: warehouse stock, production capacity, staffing») viene solo del buscador sobre la página de medidas de APQC [S]; esa página dio 403. No se puede citar literal.

### Discrepancias

- Dynamics dice que con ATP «Eliminates or reduces reservations because it considers sales orders that are already entered», mientras ASCM define ATP sobre el plan maestro, con pedidos «due and overdue» en el primer período. No son excluyentes (uno es el cálculo, otro es la implementación), pero la nota debe decir cuál cuenta.
- Business Central dice lo contrario sobre el pedido marco: las cantidades del pedido marco no afectan la disponibilidad («quantities entered on a blanket order don't affect item availability»), mientras que en Dynamics 365 SCM el acuerdo de venta es un compromiso del cliente con precio. Ver G.

### Recurso canónico

Definiciones: *APICS Dictionary* (ASCM) vía el CPIM excerpt, sin copia primaria del diccionario (no la abrí). Práctica: Microsoft Learn «Order promising concepts».

---

## G. Tipos de pedido

### Fuentes

| Fuente | URL | Tipo | Puntaje | Leído |
|---|---|---|---|---|
| SAP Help R/3 4.7, «Sales Document Types» | https://help.sap.com/saphelp_470/helpdata/en/dd/55fb06545a11d1a7020000e829fd11/content.htm | P (histórico) | 2/2/3/3 | [L] |
| Dynamics 365, «Sales agreements overview» | https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements | P | 2/3/3/3 | [L] |
| Business Central, «Work with blanket sales orders» | https://learn.microsoft.com/en-CA/dynamics365/business-central/sales-how-to-create-blanket-sales-orders | P | 2/3/3/2 | [L] |
| ERPNext, «Blanket Order» | https://docs.frappe.io/erpnext/user/manual/en/blanket-order | P | 2/1/1/1 | [L] |
| Odoo 17, «Subscriptions» | https://www.odoo.com/documentation/17.0/applications/sales/subscriptions.html | P | 2/2/2/2 | [L] |
| Odoo 18, «Consignment» | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/owned_stock.html | P | 2/2/2/2 | [L] |

Dynamics y Business Central son del mismo proveedor, pero describen cosas distintas (agreement vs blanket), por eso cuentan por separado.

### Afirmaciones

- Catálogo de tipos de SAP: Presales «Inquiry (IN), Quotation (QT), Free-of-charge delivery (FD)»; Sales orders «Standard sales order (OR), Cash sale (BV), Rush order (SO)»; Outline agreements «Quantity contract (CQ), Maintenance contract (WV), Rental contract (MV), Scheduling agreement (DS)»; además Complaints (CR, DR, SD) y Returns (RE) como grupos aparte. Los contratos y programas de entrega van en «outline agreements», no en «sales orders». https://help.sap.com/saphelp_470/helpdata/en/dd/55fb06545a11d1a7020000e829fd11/content.htm
- Contado o mostrador: SAP lo tiene como tipo propio, «Cash sale (BV)» y «Rush order (SO)». Mismo enlace. No leí qué lo distingue (por ejemplo entrega y factura en el acto).
- Pedido abierto o contrato marco: Dynamics: «A sales agreement is a contract that commits the customer to buy products in a specific quantity or for a specific amount over time, in exchange for special prices, special discounts, and other special terms»; cuatro tipos de compromiso (Product quantity, Product value, Product category value, Value); validez por «Effective date» y «Expiration date»; se libera con «Release order»; las líneas vinculadas cuentan para el cumplimiento («All sales order lines that are linked to a sales agreement contribute to fulfillment»); políticas «Max is enforced», «Price and discount is fixed», «Minimum release amount» y «Maximum release amount». https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements . Nota del proveedor: «In earlier versions, sales agreements were referred to as blanket sales orders.»
- Business Central: el pedido marco es «a framework for a long-term agreement», típico para «a large quantity that you deliver in small shipments over a period of time»; «The main reason for using a blanket order rather than a sales order is that quantities entered on a blanket order don't affect item availability. You can use them as a worksheet for monitoring, forecasting, and planning.»; cada entrega es un renglón que se convierte en pedido al despachar, y la cantidad del pedido no puede superar la del renglón del marco. https://learn.microsoft.com/en-CA/dynamics365/business-central/sales-how-to-create-blanket-sales-orders
- ERPNext: «records a long-term commitment to buy or sell specified items» pero no mueve mercadería ni plata; sirve de referencia de varios pedidos y controla la cantidad pedida contra la comprometida (resumen del extractor). https://docs.frappe.io/erpnext/user/manual/en/blanket-order
- Discrepancia a presentar: el pedido marco es un compromiso con precio y vigencia (Dynamics) o una hoja de planificación que no compromete stock (Business Central); ERPNext lo trata como referencia. Tres lecturas del mismo nombre; la nota debe definir qué compromete y qué no.
- Recurrente o suscripción: Odoo: «Sales orders with a defined recurring plan automatically become subscriptions», con plan de recurrencia en semanas, meses o años («The Days unit of measure cannot be used as a Billing Period»), y cierre automático por falta de pago. https://www.odoo.com/documentation/17.0/applications/sales/subscriptions.html . No leí los estados de la suscripción ni la renovación.
- Consignación (Odoo 18): se describe como el caso en que «suppliers will sometimes let companies store and sell products in the company's warehouse»; es la consignación recibida (el stock es del proveedor); se vende con un presupuesto normal a un cliente distinto del dueño. La consignación entregada (mi stock en casa del cliente) no está en la documentación oficial según el buscador, solo en foros. https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/owned_stock.html
- Devoluciones (frontera): en Dynamics se hace un pedido de devolución sobre el pedido original y se vincula al compromiso del acuerdo («you establish a relation between the sales agreement commitment, the sales order line, and the return order invoice»); SAP lo trata como grupo aparte (Returns, RE). Basta como frontera.

### Huecos

- Muestra sin cargo: SAP trae «Free-of-charge delivery (FD)» como tipo presales; Odoo no tiene flujo propio (según el buscador, no verificado).
- Pedido de contado en software de gestión argentino: no se buscó; es de la nota de Argentina.

### Recurso canónico

SAP «Sales Document Types» como taxonomía; Dynamics «Sales agreements overview» para el pedido abierto.

---

## H. Cambios, cancelaciones, entregas parciales, pendientes y bloqueos

### Fuentes

| Fuente | URL | Tipo | Puntaje | Leído |
|---|---|---|---|---|
| ERPNext, «Sales Order» | ver E | P | 2/3/2/2 | [L] |
| Dynamics 365, «Sales agreements overview» (modificar pedidos vinculados) | ver B | P | 2/3/3/3 | [L] |
| SAP Help R/3 4.6C, bloqueos de pedido | https://help.sap.com/saphelp_46c/helpdata/en/dd/55fc2e545a11d1a7020000e829fd11/content.htm | P | 2/1/1/2 | [L] |
| APQC PCF 3.5.4.5 | ver E | P | 3/1/1/3 | [L] (título) |
| SAP, bloqueos y *backorder processing* (resultados del buscador: ECC, Business One, KBA) | https://help.sap.com/saphelp_sbo900/helpdata/EN/1b/b8feb2dc8a47b687cbf672f89c1962/content.htm | P | 2/2/2/1 | [S] |
| Odoo, ERPNext: Lock Confirmed Sales (ver D) | ver D | P | 2/1/1/2 | [L] |

### Afirmaciones

- Entrega parcial: ERPNext: «An order can be partially delivered or billed across multiple documents.» y actualiza los porcentajes de entrega y facturación. https://docs.frappe.io/erpnext/user/manual/en/sales-order
- Pausar, cerrar, cancelar (ERPNext): Hold pausa («pause fulfillment»); «Close an order when you intentionally will not fulfill its remaining quantity.»; «Cancel a submitted order when the entire transaction should be reversed.» Mismo enlace. Es la distinción más clara de las leídas: cerrar es abandonar lo que falta, cancelar es deshacer todo.
- Modificar lo confirmado: Odoo permite impedirlo («Lock Confirmed Sales»: «Ensure no further edits can be made to confirmed orders»). En Dynamics, un pedido liberado de un acuerdo solo se puede cambiar en fecha, precio, descuento o cantidad quitando antes el vínculo con el acuerdo. https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements
- Pendientes (backorder): APQC 3.5.4.5 «Process back orders and updates» (7.4). La definición de backorder y su ciclo no la encontré en fuente primaria leída; el único texto es de SAP Business One según el buscador: tratar lo que falta entregando la diferencia, actualizando la cantidad tras el envío o cerrando «the remaining open quantity for the row» [S, producto distinto de SAP ERP]. https://help.sap.com/saphelp_sbo900/helpdata/EN/1b/b8feb2dc8a47b687cbf672f89c1962/content.htm
- Bloqueos (SAP 4.6C): se puede bloquear un pedido para dos funciones posteriores, «For shipping» y «For billing»; el bloqueo de entrega se pone «at header level as well as in the individual items and schedule lines» y el de facturación «at header level and for the individual items». https://help.sap.com/saphelp_46c/helpdata/en/dd/55fc2e545a11d1a7020000e829fd11/content.htm . El buscador agrega, sin lectura de fuente oficial, que un bloqueo de entrega puede impedir confirmar cantidades y que pedidos pendientes pueden caer en bloqueo por crédito al volver el stock [S].
- Bloqueo por crédito, precio o aprobación: el de aprobación está en ERPNext («Authorization Rule», ver B). El bloqueo por crédito existe en SAP según el buscador [S], pero la decisión de crédito es de Tesorería: acá solo se registra que el pedido queda bloqueado. Bloqueo por precio: no encontré fuente.

### Huecos

- Cambios a un pedido confirmado (qué se puede cambiar, qué reabre la reserva y la promesa de fecha): no hay fuente primaria leída sobre el efecto de cambiar cantidad o fecha en un pedido ya reservado. Solo el caso del acuerdo de Dynamics.
- Cancelación por parte del cliente y cargos: sin fuente.

### Recurso canónico

ERPNext «Sales Order» (hold, close, cancel, entrega parcial). Para bloqueos, no hay un recurso bueno; SAP 4.6C es el mejor leído y es histórico.

---

## Huecos del informe (lo que no apareció o no se buscó)

1. **ASCM CLTD, módulo «Customer and Order Management»**: el esquema (2026-cltd-module-content-outline.pdf) devolvió HTML vacío al abrirlo. Del buscador [S]: Módulo 3 «Customer and Order Management», sección A «Enable Customer and Relationship Management (CRM)», sección B «Enable Outbound and Inbound Order Management». No sé si hay subtemas de promesa y cumplimiento. Pendiente.
2. **APICS Dictionary** completo: solo las dos citas que reproduce el CPIM excerpt (ATP «in part», CTP completa). No conseguí el texto del diccionario.
3. **APQC 3.5.4.3**: solo el título y el código (10196) están leídos; la definición literal es [S].
4. **Magal y Word, Monk y Wagner**: sin lectura del texto; solo títulos y diapositivas docentes de segunda mano [S]. Las afirmaciones del capítulo «fulfillment» no se pueden atribuir.
5. **Felfernig et al. (2014)**: solo la ficha [M]. Sin citas de reglas de compatibilidad ni de paquetes. Forza y Salvador: leí el 25 % del texto.
6. **SCOR actual (Digital Standard)**: leí solo la 6.0 (2003), que no tiene «Order» como proceso. El buscador dice que SCOR 12 divide «Order» y «Fulfill» [S]. Se pidió «SCOR (proceso Order)»: no lo cubrí en su versión vigente.
7. **Numeración** del presupuesto: no se buscó.
8. **Revisión/versión de presupuestos** en Odoo y ERPNext: no encontrada en lo leído.
9. **Presupuesto vencido que se acepta tarde, o con precio cambiado**: sin fuente.
10. **Anticipo/seña** como mecanismo de aceptación: solo una mención (BC) y la política de facturación de Odoo; no leí «down payments» de Odoo.
11. **Canales de entrada de pedido (order entry)**: sin fuente propia; ya están en las notas B2B.
12. **Pedido de muestra y consignación entregada**: sin documentación oficial; solo la consignación recibida de Odoo.
13. **Margen mínimo**, **bloqueo por precio**, **cancelación por el cliente**, **cambio de un pedido ya reservado**: sin fuente primaria.
14. **Argentina**: no leí el art. 20 de la Ley 24.240 (de qué servicios habla el art. 21), ni el texto de InfoLEG del CCyC arts. 972, 974 y 980 (el 974 viene de una transcripción), ni cómo numera o rotula el presupuesto el software argentino. La leyenda de ARCA la leí en la página de «situaciones especiales», no en la resolución general que la sustenta.
15. **Descuentos y aprobaciones**: la documentación oficial de Odoo no mostró aprobación por monto (solo módulos de terceros [S]).

## Cosas que no se repiten (ya están en la base)

`Comercio-electronico/Comercio-B2B/pedido-b2b.md`, `precio-por-cliente.md` y `cuenta-corriente-y-credito.md` cubren el pedido mayorista, el precio por cliente y la cuenta corriente; acá solo se enlazan.
