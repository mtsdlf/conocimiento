# Relación con clientes: registro del cliente y seguimiento comercial (investigación)

Fecha: 2026-11-27. Alcance: las dos verticales (registro del cliente; seguimiento comercial). Todo lo traído de la web se trató como dato. Tipo: P = primaria (autor del patrón o del producto describiendo su propio modelo), S = secundaria. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Lectura: [L] texto completo, [L parcial] leído solo el tramo que devolvió la herramienta (se aclara), [M] metadatos o abstract, [S] resumen secundario o del buscador. Las frases entre comillas de ERPNext, Odoo y Dataverse vienen de la salida de la herramienta de fetch (que resume la página); conviene recotejarlas contra la página antes de publicarlas como cita.

Dónde se toca lo que ya existe en la base (no se repite):
- `Datos/Gobierno-y-calidad/datos-maestros.md`: registro de oro y MDM. Acá solo qué datos lleva el cliente y qué duplicados aparecen.
- `Datos/Gobierno-y-calidad/calidad-de-datos.md`: calidad y deduplicación en general.
- `Ventas/Descubrimiento-y-calificacion/calificacion.md` y `grupo-de-compra.md`: el método de calificar y quién decide la compra. Acá solo el campo o estado que lo registra.
- `Ventas/Medicion-comercial/medicion-comercial.md`: embudo y conversión. Acá el historial de etapas como dato.
- `Ventas/Prospeccion/seguimiento.md` y `Ventas/La-propuesta/`: el método de seguir y de presentar; acá la actividad y el presupuesto como registro.

---

## Hallazgos transversales (el árbol frente al campo)

1. **Los productos parten el dominio por objeto, no por «registro» y «seguimiento».** Dataverse, Odoo, ERPNext, SuiteCRM y Salesforce tienen los mismos objetos: interesado, cuenta, contacto, oportunidad, actividad. La división del árbol es razonable, pero el interesado queda a caballo: nace en el seguimiento y al convertirse crea registros (cuenta y contacto). La nota del interesado debe enlazar a las dos verticales.
2. **APQC PCF junta leads y cuentas.** En la copia consultada, 3.5 «Develop and manage sales plans» contiene 3.5.1 «Manage leads/opportunities» y 3.5.2 «Manage customers and accounts» (con 3.5.2.5 «Manage customer master data» y 3.5.2.5.2 «De-duplicate customer data»). Trata el registro de cuentas como parte del proceso de vender. Nuestro árbol (registro aparte del método) es compatible, pero el PCF muestra que el campo los ve unidos. https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services
3. **«Relación con clientes» en Buttle y Maklan es más ancha que un registro** (estrategia, valor del cliente, tecnología); no se pudo leer el índice (ver huecos). El tema acá es la parte de modelo de datos.
4. **El presupuesto no es la oportunidad sino un documento ligado** (Dataverse y ERPNext lo modelan como objeto aparte).
5. **El límite de crédito y la condición de pago son dato del cliente; la decisión es de Tesorería.** Dataverse lo llama referencia; ERPNext lo vuelve regla que bloquea (ver componente 2).

---

## Componente 1. Cuenta y contacto (parte, roles, jerarquías, comprador/pagador/destinatario, duplicados)

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Lectura |
|---|---|---|---|---|---|
| 1.1 | Fowler, *Analysis Patterns* (1997), cap. «Organization Structures» (Party, Organization Hierarchy, Accountability) | https://martinfowler.com/apsupp/accountability.pdf | P | 3/3/2/3 | [L parcial] texto extraído con pdftotext; leído Party y Organization Hierarchy y la introducción de Accountability; no el detalle de Accountability Type ni Knowledge Level |
| 1.2 | Fowler, «Dealing with Roles» (borrador, 20 jul 1997) | https://martinfowler.com/apsupp/roles.pdf | P | 3/3/2/3 | [L parcial] introducción y tabla de patrones |
| 1.3 | Silverston, *The Data Model Resource Book* vol. 1, listado de figuras (Wiley) | https://books.wiley.com/authors/len-silverston/models | S | 3/1/1/3 | [M] |
| 1.4 | Salesforce Trailhead, «Understand Account and Contact Relationships» | https://trailhead.salesforce.com/content/learn/modules/accounts_contacts_lightning_experience/understand-account-and-contact-relationships-lightning | P | 2/2/2/1 | [L] |
| 1.5 | Microsoft Learn, tabla Account (Dynamics 365 Customer Engagement, on-premises) | https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account | P | 3/3/3/1 | [L parcial] 100.000 de 121.405 caracteres |
| 1.6 | Odoo 19.0, Contactos | https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html | P | 2/2/2/1 | [L parcial] 100.000 de 102.561 |
| 1.7 | ERPNext (Frappe), Customer | https://docs.frappe.io/erpnext/user/manual/en/customer | P | 2/2/3/1 | [L] |
| 1.8 | SAP Library 4.70, «Partner Functions» | https://help.sap.com/saphelp_470/helpdata/en/7f/f6341aac6111d2b44c006094b9ea37/content.htm | P | 3/2/2/3 | [L] |
| 1.9 | Resumen del buscador sobre partner functions SAP (foros y Q&A de SAP Community; páginas de SAP Library devueltas) | https://help.sap.com/saphelp_erp2005/helpdata/EN/7f/f63420ac6111d2b44c006094b9ea37/content.htm | S | 1/1/2/1 | [S] página no abierta |
| 1.10 | APQC PCF, copia de Cape Chamber (versión no declarada) | https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services | S | 2/3/1/2 | [L] |
| 1.11 | CIO.com, David Taber, «How to solve CRM data deduplication dilemmas» (1 oct 2013) | https://www.cio.com/article/2382113/how-to-solve-crm-data-deduplication-dilemmas.html | S (columna de práctica) | 1/2/2/2 | [L] |

Independencia: 1.4 a 1.7 son cuatro productos distintos que cuentan cosas parecidas porque el patrón es común, que es lo que se quiere mostrar. 1.8 y 1.9 son un mismo hecho; 1.9 pesa poco.

### Afirmaciones

**Parte y roles**
- Fowler: Party es «An abstraction of people and organizational units», con Person y Organization como subtipos. «A telephone utility's customers may be individuals or businesses. Many aspects of dealing with customers are the same, in which case they are treated as parties. Where they differ they are treated through their subtype.» https://martinfowler.com/apsupp/accountability.pdf
- El problema: «If I were to model an address book, I might choose to have people and companies, each of which have postal addresses and telephone numbers, but the resulting duplication is painful to the eye.» https://martinfowler.com/apsupp/accountability.pdf
- El nombre es convención: «I have seen it on countless data models on various names: person/org, player, legal entity…. The term I prefer is party, and I've been glad to see that over the last few years it's turned into a fairly standard name.» https://martinfowler.com/apsupp/accountability.pdf
- El patrón sirve aun sin distinguir persona y organización: «it's useful just to define a party class and not to provide the subtypes.» https://martinfowler.com/apsupp/accountability.pdf
- Roles: «You may have an agent who is also a customer, you have an accountant who becomes an engineer.» Por eso la herencia simple no alcanza. Los cinco patrones de la tabla: Single Role Type, Separate Role Type, Role Subtype, Role Object («put common features on a host object with a separate object for each role») y Role Relationship («make each role a relationship»). https://martinfowler.com/apsupp/roles.pdf
- Silverston vol. 1: el listado del editor trae las figuras «Party», «Party roles», «Specific party relationships», «Common party relationships» y «Party relationship information»; ninguna se llama «customer» (lo más cercano es «Sales order parties and contact mechanisms»). Es consistente con que cliente sea un rol de la parte, pero es inferencia desde un índice. [M] https://books.wiley.com/authors/len-silverston/models

**Cuenta frente a contacto; empresa frente a persona**
- Dataverse: la cuenta es «Business that represents a customer or potential customer. The company that is billed in business transactions.» Y «Choose the primary contact for the account to provide quick access to contact details.» https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account
- Salesforce: cada contacto tiene una cuenta principal; los roles son un campo de la relación contacto-cuenta; contactos a varias cuentas permite «track the relationships between people and businesses without creating duplicate records». https://trailhead.salesforce.com/content/learn/modules/accounts_contacts_lightning_experience/understand-account-and-contact-relationships-lightning
- Odoo usa un mismo registro para empresa y persona: «Odoo supports both Person and Company contacts.» y «Person contacts can be linked to a Company contact.» Es Party de Fowler hecho producto. https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html
- ERPNext distingue el tipo: «Distinguishes Company, Individual, and Partnership Customers and can affect naming and reporting.» y «Addresses and Contacts are independent records linked to the Customer.» https://docs.frappe.io/erpnext/user/manual/en/customer
- Discrepancia de modelo: Dataverse y Salesforce separan cuenta y contacto en dos tablas; Odoo los unifica. Para el cliente persona, Salesforce tiene la variante «cuenta personal» (solo por el buscador [S]; la página oficial devolvió 403, no verificado).

**Jerarquías**
- Dataverse: «Choose the parent account associated with this account to show parent and child businesses in reporting and analytics.» https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account
- Salesforce: con la cuenta matriz cargada se puede «generate a family tree for your account». https://trailhead.salesforce.com/content/learn/modules/accounts_contacts_lightning_experience/understand-account-and-contact-relationships-lightning
- Fowler: usar la jerarquía «when you have a hierarchic corporate structure that affects the software you are using»; y si no duele no tenerla, no vale el costo de mantenerla («If the consequences are not painful then it's not worth carrying the cost of the links»). Sin ciclos («your grandparent cannot be your grandchild»). Con varias jerarquías a la vez se justifica Accountability, que describe como «the most powerful, and also the most complex way of dealing with organizational structures»; hay un Knowledge Level que fija qué partes se pueden conectar. https://martinfowler.com/apsupp/accountability.pdf
- Discrepancia: los productos leídos dan una sola cuenta matriz; Fowler admite varias jerarquías o vínculos tipados. (Un blog de proveedor afirma que Salesforce soporta una sola estructura padre-hijo por cuenta [S]; dato débil.)

**Comprador, pagador, destinatario (partner functions)**
- SAP: los partner functions son roles que un interlocutor cumple en un proceso; uno puede tener varios; las funciones estándar del tipo cliente son sold-to party, ship-to party, bill-to party y payer, «absolutely necessary for sales and distribution processing», obligatorias por defecto; en el caso simple el cliente cumple las cuatro. https://help.sap.com/saphelp_470/helpdata/en/7f/f6341aac6111d2b44c006094b9ea37/content.htm
- Del buscador (foros, no documentación oficial) [S]: sold-to pide, ship-to recibe la mercadería, bill-to recibe la factura, payer paga; los otros interlocutores tienen registro propio enlazado al sold-to; caso común: pagador central distinto del que compra; códigos SP, SH, BP, PY. https://help.sap.com/saphelp_erp2005/helpdata/EN/7f/f63420ac6111d2b44c006094b9ea37/content.htm
- La página oficial leída no define cada función por separado (hueco). Se pueden sostener con Dataverse («The company that is billed») y Odoo: «Invoice: adds a specific invoice address to the existing contact form.» y «Delivery: adds a specific delivery address to the existing contact form.» https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html
- Dos niveles de detalle: SAP hace cuatro roles que pueden apuntar a registros distintos; Odoo y ERPNext resuelven con direcciones de factura y entrega dentro de la misma cuenta, sin pagador de primera clase. El modelo chico alcanza cuando el que paga es el que compra.

**Duplicados y fusión**
- PCF 3.5.2.5.1 «Collect and merge internal and third-party customer information», 3.5.2.5.2 «De-duplicate customer data». https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services
- Taber: «Get beyond 5 percent or so, though, and users will start to complain.» y «Systems with 25 percent duplicate records, moreover, can threaten careers.» Causas: no buscar antes de crear, importaciones que no detectan duplicados, integraciones (formularios, portales) que insertan sin chequear, errores de administración o de software. https://www.cio.com/article/2382113/how-to-solve-crm-data-deduplication-dilemmas.html
- Registro de oro: ya en `Datos/Gobierno-y-calidad/datos-maestros.md`; el cliente es su caso típico.

### Recurso canónico propuesto
Fowler, «Organization Structures» (accountability.pdf) y «Dealing with Roles» (roles.pdf) para la idea; Account de Dataverse y Contactos de Odoo como evidencia de práctica; SAP «Partner Functions» para comprador/pagador/destinatario. Silverston vol. 1 sería el complemento concreto, pero no se pudo leer.

---

## Componente 2. Condiciones comerciales del cliente

### Fuentes
Son las mismas 1.5, 1.6, 1.7 y 1.8 (Dataverse Account, Odoo Contactos, ERPNext Customer, SAP Partner Functions), más Dataverse Opportunity (5.1). No hay fuente fuera de productos (libro o norma): todo descansa en tres productos y se presenta como práctica común.

### Afirmaciones
- Lista de precios: ERPNext «Selects the default selling Price List used to retrieve Item prices.» https://docs.frappe.io/erpnext/user/manual/en/customer. Odoo: «Select the Pricelist drop-down menu to choose the appropriate Pricelist.» https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html. Dataverse la pone en la oportunidad («Choose the price list associated with this record to make sure the products ... are offered at the correct prices») y no apareció en la parte leída de la cuenta. https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/opportunity
- Condición de pago: Dataverse «Select the payment terms to indicate when the customer needs to pay the total amount.» (Net 30, 2% 10 Net 30, Net 45, Net 60). ERPNext: «The payment terms template controls when amounts are due; it does not increase the Customer's credit limit.» Odoo: en la sección Sales (clientes) y Purchase (proveedores) del mismo registro. https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account , https://docs.frappe.io/erpnext/user/manual/en/customer , https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html
- Límite de crédito: Dataverse «Type the credit limit of the account. This is a useful reference when you address invoice and accounting issues with the customer.» ERPNext: «Blocks applicable transactions when outstanding exposure exceeds the configured company limit.» Discrepancia: referencia frente a regla que bloquea. Quien decide el límite es Tesorería. https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account , https://docs.frappe.io/erpnext/user/manual/en/customer
- Moneda: ERPNext «Defaults the transaction currency on new sales documents for this Customer.» https://docs.frappe.io/erpnext/user/manual/en/customer
- Vendedor: ERPNext «Assign a Sales Person or sales team and ensure contribution percentages total 100%.» Odoo «a specific Salesperson can be assigned to a contact». Dataverse, propietario: «Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.» https://docs.frappe.io/erpnext/user/manual/en/customer , https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html , https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account
- Zona: Dataverse «Select a region or territory for the account for use in segmentation and analysis.» ERPNext: el territorio «Places the Customer in the sales territory hierarchy for analysis and assignment.» (mismas URLs)
- Impuestos (en general): ERPNext «a Tax Category or regional Tax Withholding Category when required by your tax configuration.» Odoo «Tax ID: the identification number used for tax and accounting purposes.» Lo argentino (CUIT, condición frente al IVA, percepciones) no se investigó: va aparte. https://docs.frappe.io/erpnext/user/manual/en/customer , https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html
- Condiciones por rol: en SAP se cargan por área de ventas y el pagador puede ser otro registro [S]; en Odoo y ERPNext quedan en el cliente. Quién paga determina de qué registro se lee la condición de pago y el límite.

### Recurso canónico propuesto
Dataverse Account (límite, condición de pago, propietario, territorio) más ERPNext Customer (lista de precios, moneda, impuestos, vendedor, separación entre condición de pago y límite). Ambos son evidencia de práctica, no norma.

---

## Componente 3. Cartera de clientes (asignación, territorios, clasificación, dueño)

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Lectura |
|---|---|---|---|---|---|
| 3.1 | Trailhead, tips de Enterprise Territory Management (más notas de admin y un libro de O'Reilly, vía buscador) | https://trailhead.salesforce.com/content/learn/modules/advanced-territory-management/get-tips-and-tricks-for-enterprise-territory-management | P | 2/2/2/2 | [S] no abierta |
| 3.2 | O'Reilly, *Mastering Salesforce CRM*, rol frente a territorio | https://oreilly.com/library/view/mastering-salesforce-crm/9781786463180/ch03s02.html | S | 1/1/1/1 | [S] no abierta |
| 3.3 | IMD, «Getting ABC classifications right» (sobre inventario) | https://www.imd.org/research-knowledge/supply-chain/articles/getting-abc-classifications-right/ | S | 2/2/1/2 | [S] no abierta |
| 3.4 | ERPNext Customer (1.7), Dataverse Account (1.5), PCF vía Cape Chamber (1.10) | ver 1.x | P/S | ver 1.x | ver 1.x |

### Afirmaciones
- Dueño: Dataverse tiene un solo propietario, usuario o equipo («Enter the user or team who is assigned to manage the record.»). El resumen del buscador dice, para Salesforce, «an account is owned by a single user. An account can be belonged to multiple territories.» [S] https://oreilly.com/library/view/mastering-salesforce-crm/9781786463180/ch03s02.html
- Un dueño frente a reparto: ERPNext reparte entre vendedores con porcentajes que suman 100%; Dataverse y Salesforce tienen un dueño más un territorio o equipo. Dos modelos que se muestran los dos. https://docs.frappe.io/erpnext/user/manual/en/customer
- Territorio: ERPNext lo ubica en una jerarquía de territorios; Dataverse lo usa para segmentar y analizar (la lista la carga la organización; en la página solo hay un valor por defecto). https://docs.frappe.io/erpnext/user/manual/en/customer , https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account
- Rol frente a territorio (Salesforce): la jerarquía de roles para líneas de reporte y la de territorios para extender acceso por asignación; con territorios no usar equipos de cuenta. [S, resumen del buscador; abrir antes de citar] https://trailhead.salesforce.com/content/learn/modules/advanced-territory-management/get-tips-and-tricks-for-enterprise-territory-management
- Clasificación: ERPNext, grupo de clientes: «Classify Customers for defaults, reporting, permissions, and pricing decisions.» Cumple a la vez segmentación y defaults: conviene advertirlo. https://docs.frappe.io/erpnext/user/manual/en/customer
- ABC: aplica Pareto; «20% of customers generate 80% of the revenue» es aproximación; los cortes se fijan sobre el porcentaje de ingreso, no la cantidad de clientes; la base (ingreso, unidades, margen) se discute y la clasificación envejece. Es técnica de inventario aplicada a clientes; sin fuente primaria de CRM. [S] https://www.imd.org/research-knowledge/supply-chain/articles/getting-abc-classifications-right/
- Activo/inactivo y potencial: sin definición en las fuentes leídas (hueco); «inactivo» (por tiempo sin compra) lo decide cada negocio.
- PCF: 3.5.2.1 «Select key customers/accounts», 3.5.2.2 «Develop sales/key account plan», 3.5.2.4 «Manage customer relationships»; y 3.3.5.1 «Determine customer lifetime value», 3.3.5.3 «Analyze customer attrition and retention rates», que respaldan enlazar valor del cliente y RFM a un análisis fuera del registro. https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services
- RFM: no se investigó (solo enlace).

### Recurso canónico propuesto
Ninguno único. ERPNext Customer como modelo más completo y legible (grupo, territorio, vendedor con porcentajes); Trailhead de territorios si se confirma leyéndolo.

---

## Componente 4. Interesado (lead)

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Lectura |
|---|---|---|---|---|---|
| 4.1 | Microsoft Learn, tabla Lead | https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/lead | P | 3/3/3/1 | [L parcial] 100.000 de 160.155 |
| 4.2 | SuiteCRM, Leads | https://docs.suitecrm.com/user/sales-relationships/leads/ | P | 2/2/2/1 | [L] |
| 4.3 | Odoo 18.0, «Convert leads into opportunities» | https://www.odoo.com/documentation/18.0/applications/sales/crm/acquire_leads/convert.html | P | 2/2/2/1 | [L] |
| 4.4 | ERPNext, Lead | https://docs.frappe.io/erpnext/user/manual/en/lead | P | 2/2/2/1 | [L] |
| 4.5 | Salesforce (mapeo de Lead en Data Cloud y guías de estudio, vía buscador) | https://developer.salesforce.com/docs/data/data-cloud-ref/guide/c360dm-crm-lead.html | S | 2/1/1/1 | [S] |
| 4.6 | PCF (1.10), Taber (1.11) | ver 1.x | S | ver 1.x | ver 1.x |

La página oficial de Salesforce para el objeto Lead devolvió 403.

### Afirmaciones
- Qué es: Dataverse «Prospect or potential sales opportunity. Leads are converted into accounts, contacts, or opportunities when they are qualified. Otherwise, they are deleted or archived.» https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/lead . SuiteCRM «an unqualified contact usually generated from some form of marketing related event». https://docs.suitecrm.com/user/sales-relationships/leads/ . ERPNext «A lead is a potential customer who might be interested in your products or services.» https://docs.frappe.io/erpnext/user/manual/en/lead
- Por qué se separa del cliente: Odoo «Leads act as a qualifying step before an opportunity is created.»; da tiempo para evaluar antes de pasarlo al vendedor y se puede apagar por equipo. https://www.odoo.com/documentation/18.0/applications/sales/crm/acquire_leads/convert.html . Dataverse admite borrarlo o archivarlo si no se califica. La razón de fondo (dato incierto que no compromete a nadie ni debe ensuciar la cartera) es interpretación nuestra; ninguna fuente la formula como principio.
- Origen: SuiteCRM «records how the lead was acquired» (Web Site, Trade Show, Word of Mouth, Cold Call, Campaign), para medir canales. https://docs.suitecrm.com/user/sales-relationships/leads/ . ERPNext tiene Source en el interesado y en la oportunidad. https://docs.frappe.io/erpnext/user/manual/en/lead
- Estados: Dataverse, Open / Qualified / Disqualified con motivos New, Contacted (abiertos) y Lost, Cannot Contact, No Longer Interested, Canceled (descalificados); «Qualified and disqualified leads are read-only and can't be edited unless they are reactivated.» https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/lead . SuiteCRM: New, Assigned, In Process, Converted, Recycled, Dead. Discrepancia: SuiteCRM tiene «Recycled» (volver a la cola); Dataverse reactiva. ERPNext mezcla estado del interesado con la suerte de la cotización: crear oportunidad lo marca calificado, «Converted» lo pone una orden de venta y una cotización perdida lo pasa a «Lost Quotation». https://docs.frappe.io/erpnext/user/manual/en/lead
- Conversión: SuiteCRM «Once a Lead is qualified and converted then it can be split into three parts»: contacto (quién), cuenta (dónde trabaja), oportunidad (qué podría comprar); avisa de duplicados. Dataverse: la empresa del interesado «becomes the account name when the lead is qualified and converted to a customer account». Odoo: al convertir se elige vendedor y equipo y se crea, vincula o no se vincula el cliente. ERPNext: desde el interesado se crea oportunidad, cliente o cotización con valores copiados. (URLs de 4.1 a 4.4)
- Rastro: Dataverse `QualifyingOpportunityId`, la oportunidad en la que se calificó. ERPNext: al convertir, el cliente «remains connected to the earlier sales activity» (https://docs.frappe.io/erpnext/user/manual/en/customer). Salesforce: IsConverted y campos de cuenta, contacto y oportunidad convertidos [S]. El interesado no se borra al convertirse.
- Deduplicación: Odoo muestra «Similar Leads»; al fusionar conserva el registro más antiguo y suma la información del otro; si se fusiona interesado con oportunidad queda oportunidad. https://www.odoo.com/documentation/18.0/applications/sales/crm/acquire_leads/convert.html . Causas generales: Taber (1.11).
- PCF 3.5.1.2 «Identify/receive leads/opportunities» y 3.5.1.3 «Validate and qualify leads/opportunities»: lo segundo es método (Ventas); el estado lo registra. https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services
- División: lead como objeto propio en Dataverse, SuiteCRM, Odoo (apagable) y ERPNext (donde la oportunidad es «a qualified lead»). La separación es decisión de diseño con costo; sin software, una planilla con una columna «estado» alcanza.

### Recurso canónico propuesto
Lead de Dataverse (estados, calificación, conversión, literal) más Leads de SuiteCRM (origen y conversión en tres partes). Para el «por qué se separa» no hay fuente única.

---

## Componente 5. Oportunidad

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Lectura |
|---|---|---|---|---|---|
| 5.1 | Microsoft Learn, tabla Opportunity | https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/opportunity | P | 3/3/3/1 | [L parcial] 100.000 de 139.478 |
| 5.2 | ERPNext, Opportunity | https://docs.frappe.io/erpnext/user/manual/en/opportunity | P | 2/2/2/1 | [L] |
| 5.3 | Odoo 19.0, «Lost opportunities» | https://www.odoo.com/documentation/19.0/applications/sales/crm/pipeline/lost_opportunities.html | P | 2/1/1/1 | [L parcial] 100.000 de 105.505 |
| 5.4 | PCF (1.10) | ver 1.10 | S | 2/3/1/2 | [L] |

### Afirmaciones
- Definición: Dataverse «Potential revenue-generating event, or sale to an account, which needs to be tracked through a sales process to completion.» ERPNext «Opportunity is a qualified lead.»; un interesado o cliente puede tener varias. (5.1, 5.2)
- Monto: Dataverse `estimatedvalue`: «Type the estimated revenue amount to indicate the potential sale or value of the opportunity for revenue forecasting.» ERPNext: Opportunity Amount y Currency.
- Probabilidad: Dataverse «Type a number from 0 to 100 that represents the likelihood of closing the opportunity.» ERPNext «Probability of conversion». Pregunta abierta: si la fija la etapa o la persona (en las fuentes leídas es un campo editable).
- Fecha estimada de cierre: Dataverse «Enter the expected closing date of the opportunity to help make accurate revenue forecasts.» ERPNext distingue «Next Contact Date» y «Next Contact By» (recordatorio de seguimiento que agrega un evento al calendario del asignado), otra fecha distinta de la de cierre.
- Etapa: Dataverse «Select the sales stage of this opportunity to aid the sales team in their efforts to win this opportunity.» Valores de fábrica 0 Qualify, 1 Develop, 2 Propose, 3 Close. Las etapas como método son de `Ventas/Medicion-comercial/medicion-comercial.md`; acá es un campo con valores configurables.
- Estado abierta, ganada, perdida: Dataverse «Shows whether the opportunity is open, won, or lost. Won and lost opportunities are read-only and can't be edited until they are reactivated.» Motivos In Progress, On Hold (abierta), Won, Canceled, Out-Sold (perdida). Hay dos ejes: etapa de avance y estado de cierre.
- Productos: Dataverse, total del detalle «the sum of all existing and write-in products included on the opportunity, based on the specified price list and quantities». ERPNext: casilla «With Items». Los productos son opcionales: puede bastar un monto estimado.
- Competidores: ERPNext, al perder se registran «the reasons, the competitors involved, and a detailed explanation»; Dataverse solo trae en la oportunidad un Sí/No («Select whether information about competitors is included») y un objeto Competidor aparte (no leído).
- Motivo de pérdida: Odoo «Specifying why an opportunity was lost helps identify recurring issues, reveal coaching opportunities»; es opcional pero se recomienda llenarlo; la lista es configurable. https://www.odoo.com/documentation/19.0/applications/sales/crm/pipeline/lost_opportunities.html
- Presupuesto: Dataverse, relación uno a muchos `opportunity_quotes` y acción WinQuote; ERPNext crea la cotización desde la oportunidad («Relevant field values will be copied over.»). Oportunidad = intención y pronóstico; presupuesto = documento con líneas, precio y vigencia; una oportunidad puede tener varios. PCF separa igual: 3.5.1.5 a 3.5.1.8.5 frente a 3.5.3 «Develop and manage sales proposals, bids, and quotes». https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services
- Historial de cambios de etapa: sin fuente (hueco). Sin él no se mide cuánto tarda cada etapa; esa medición es de `medicion-comercial.md`.

### Recurso canónico propuesto
Opportunity de Dataverse como referencia de campos; Opportunity de ERPNext para competidores, motivos y recordatorios; Odoo «Lost opportunities» para el motivo de pérdida.

---

## Componente 6. Actividad (línea de tiempo y por qué no se carga)

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Lectura |
|---|---|---|---|---|---|
| 6.1 | Microsoft Learn, tabla Activity (ActivityPointer), actualizada 2026-09-17 | https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/activitypointer | P | 3/3/2/1 | [L parcial] búsqueda de texto sobre la página guardada |
| 6.2 | ERPNext Opportunity (5.2) | https://docs.frappe.io/erpnext/user/manual/en/opportunity | P | 2/2/2/1 | [L] |
| 6.3 | Nutshell, «9 Reasons Why Sales Reps Quit Their CRMs» | https://www.nutshell.com/blog/reasons-why-sales-reps-quit-their-crms | S (blog de un proveedor de CRM; cita estudios sin enlazarlos) | 1/1/1/1 | [L] |
| 6.4 | HubSpot, «team not using CRM» | https://blog.hubspot.com/sales/team-not-using-crm | S (blog de proveedor) | 1/1/1/1 | [S] no abierta |
| 6.5 | Resultados sobre fallas de CRM (Forrester, DesignRush, Salesforce) | https://news.designrush.com/why-crm-implementations-fail-how-to-avoid-it | S | 1/1/1/1 | [S] |
| 6.6 | Taber, CIO (1.11) | ver 1.11 | S | 1/2/2/2 | [L] |

Los blogs 6.3 y 6.4 son de proveedores con interés en que el problema parezca de adopción y no de diseño. Sus cifras citan estudios de terceros que no se verificaron en el original. No se encontró estudio primario.

### Afirmaciones
- Qué es: Dataverse «Task performed, or to be performed, by a user. An activity is any action for which an entry can be made on a calendar.» Tiene un campo «Regarding» (`regardingobjectid`): «Unique identifier of the object with which the activity is associated.» La actividad cuelga de cualquier objeto (cuenta, contacto, oportunidad) y esa relación arma la línea de tiempo. Lo hecho y lo pendiente son una misma entidad. https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/activitypointer
- Tipos concretos (llamada, correo, reunión, tarea): no verificados en la página leída.
- Seguimiento programado: ERPNext, «Next Contact Date» y «Next Contact By». https://docs.frappe.io/erpnext/user/manual/en/opportunity
- Vista unificada: en Dataverse el interesado tiene `CustomerId`, «a quick link to additional customer details, such as account information, activities, and opportunities». https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/lead
- Por qué no se carga (secundario, de proveedor): Nutshell cita a MHI Global («only a third of CRM projects are adopted by 90% or more of their sales teams.»), a ESNA («79% of opportunity-related data gathered by sales reps is never entered into their CRMs.») y SuperOffice (menos de 40% de las empresas que implementan CRM lo usan a plena capacidad). Razones: valor poco claro («Reps see the CRM as a management monitoring tool»), complejidad, poca capacitación, no es móvil, no ahorra tiempo (registros «off the books»), datos malos que erosionan la confianza, mala integración, poca personalización. https://www.nutshell.com/blog/reasons-why-sales-reps-quit-their-crms
- HubSpot: la raíz es que el vendedor no ve beneficio personal; una capacitación única no alcanza. [S] https://blog.hubspot.com/sales/team-not-using-crm
- Datos malos: Taber, causas de duplicados y umbrales (5% queja, 25% «can threaten careers»); columna de práctica, no medición. https://www.cio.com/article/2382113/how-to-solve-crm-data-deduplication-dilemmas.html
- Débil y sin verificar: DesignRush afirma «roughly 70%» de implementaciones que no cumplen objetivos sin nombrar el estudio; otro artículo atribuye a Gartner que los datos malos son la causa número uno, sin enlace. [S] https://news.designrush.com/why-crm-implementations-fail-how-to-avoid-it
- Interpretación nuestra, no de fuente: «el vendedor no carga porque no le sirve» sugiere pedir pocos campos obligatorios y dar al vendedor algo a cambio; hipótesis hasta tener fuente primaria.

### Recurso canónico propuesto
Para el modelo, Activity de Dataverse (única primaria leída). Para el porqué de la falta de carga no hay canónico; el mejor disponible es Nutshell, avisando que cita cifras de terceros.

---

## Recursos canónicos, en una línea cada uno
1. Parte, roles, jerarquía: Fowler, https://martinfowler.com/apsupp/accountability.pdf y https://martinfowler.com/apsupp/roles.pdf
2. Cliente y condiciones: Dataverse Account https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account y ERPNext Customer https://docs.frappe.io/erpnext/user/manual/en/customer
3. Comprador / pagador / destinatario: SAP «Partner Functions» https://help.sap.com/saphelp_470/helpdata/en/7f/f6341aac6111d2b44c006094b9ea37/content.htm
4. Interesado: Dataverse Lead https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/lead y SuiteCRM https://docs.suitecrm.com/user/sales-relationships/leads/
5. Oportunidad: Dataverse Opportunity https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/opportunity
6. Actividad: Dataverse Activity https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/activitypointer
7. Mapa de procesos: APQC PCF 3.5.1 y 3.5.2 (fuente https://www.apqc.org/pcf; la copia leída es de un tercero).

## Huecos
- **Libros de texto no leídos.** Buttle y Maklan (*Customer Relationship Management: Concepts and Technologies*, 4.ª ed., Routledge, 2019) y Kumar y Reinartz: solo metadatos y buscador. La página de Taylor & Francis no devolvió contenido y la de Routledge dio 404. No se confirmó el índice ni se verificó ninguna afirmación contra ellos.
- **Silverston y Hay (*Data Model Patterns*) no leídos**: solo el listado de figuras del editor [M].
- **Salesforce**: las páginas primarias de objeto (Account, Contact, Lead, Opportunity) dieron 403; lo de Salesforce es Trailhead (leído) y resúmenes del buscador. Cuentas personales no verificadas en primaria.
- **SAP**: sin página oficial que defina cada una de las cuatro funciones; `learning.sap.com` dio 404.
- **Dataverse**: se leyeron las referencias de tablas (Account, Lead, Opportunity, Activity), no la documentación conceptual del modelo de datos común; las de Account, Lead y Opportunity son de Customer Engagement on-premises y pueden estar desactualizadas frente a Dataverse actual. Competitor, Contact y los tipos de actividad no leídos.
- **APQC PCF**: no se abrió la fuente oficial. La lista usada es una copia de Cape Chamber con versión no declarada. El encargo habla de «3.5 gestionar clientes y cuentas»: en la copia, 3.5 es «Develop and manage sales plans» y «Manage customers and accounts» es 3.5.2; la numeración cambia entre versiones (en la 6.1.1 «Manage Customer Service» es 5.0 y en las 7.x y 8.0 es 6.0, según el buscador). Los PDF oficiales de versiones 6 y 6.1.1 no se pudieron extraer.
- **SuiteCRM**: solo la página de interesados.
- **Sin fuente leída**: historial de cambios de etapa, probabilidad por etapa, tipos de actividad, estados activo/inactivo del cliente.
- **Evidencia primaria de por qué los vendedores no cargan datos**: solo blogs de proveedores con cifras de segunda mano (ESNA, MHI Global, SuperOffice sin enlace). Falta el original o literatura académica de adopción de CRM.
- **ABC de clientes**: solo resúmenes del buscador, con base en inventario.
- **RFM y lo argentino** (CUIT, condición frente al IVA, percepciones, factura electrónica): no investigados por pedido.
- **Presupuesto como documento**: solo dos productos y PCF; el método es de `Ventas/La-propuesta/`.
- **Rondas**: ningún componente pasó de tres (más fetches directos).
