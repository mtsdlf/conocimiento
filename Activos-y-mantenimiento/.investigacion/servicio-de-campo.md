# Servicio de campo (field service): informe de investigación

Fecha de la investigación: 2026-11-27. Alcance: vertical Servicio de campo del tema Activos y mantenimiento.

## Advertencia sobre la cobertura de esta investigación

Esta investigación quedó **incompleta**. El presupuesto de búsquedas web de la sesión estaba agotado (las 4 búsquedas intentadas fueron rechazadas, 0 resultados), así que solo pude hacer lecturas directas (WebFetch) de URLs que ya conocía o que adiviné. Varias dieron 404, 403 o 429. Consecuencias:

- Solo las fuentes de la tabla "Verificadas" tienen URL leída en esta sesión. Todo lo demás está en "No verificadas" y **no debe citarse en la nota hasta confirmarlo**.
- No hay ninguna cifra de first-time fix, tiempo de respuesta o utilización con fuente verificada. Es un hueco, no una omisión.
- Las referencias académicas de la sección "No verificadas" salen de mi memoria, sin consulta. Pueden tener errores de año, título o volumen.
- Nota de lectura: WebFetch pasa la página por un modelo pequeño que responde a un prompt. Las marcas [L] de abajo son "la página se recuperó y se la interrogó", no lectura humana palabra por palabra. Las citas literales son las que el recuperador devolvió entre comillas.

## Fuentes verificadas

Puntajes de 1 a 3: A = autoridad, P = profundidad, E = ejemplos, U = unicidad. Todas son documentación de sistemas (salvo 7 y 9): sirven como **evidencia de práctica** sobre cómo se modelan los objetos, no como definición del negocio.

| # | Fuente | Tipo | Marca | A | P | E | U | URL |
|---|---|---|---|---|---|---|---|---|
| 1 | Microsoft Learn, Overview of Dynamics 365 Field Service (actualizada 2026-11-23) | primaria (de sistema) | [L] | 2 | 2 | 3 | 2 | https://learn.microsoft.com/en-us/dynamics365/field-service/overview |
| 2 | Microsoft Learn, Work order lifecycle and system statuses (2026-08-10) | primaria (de sistema) | [L] | 2 | 3 | 3 | 3 | https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status |
| 3 | Microsoft Learn, Set up customer agreements to generate work orders (2026-03-02) | primaria (de sistema) | [L] | 2 | 3 | 3 | 3 | https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-agreements-work-orders |
| 4 | ERPNext (Frappe) manual, Warranty Claim | primaria (de sistema) | [L] | 2 | 2 | 2 | 3 | https://docs.frappe.io/erpnext/user/manual/en/warranty-claim |
| 5 | ERPNext (Frappe) manual, Maintenance Visit | primaria (de sistema) | [L] | 2 | 2 | 2 | 3 | https://docs.frappe.io/erpnext/user/manual/en/maintenance-visit |
| 6 | ERPNext (Frappe) manual, Serial No | primaria (de sistema) | [L] | 2 | 1 | 1 | 2 | https://docs.frappe.io/erpnext/user/manual/en/serial-no |
| 7 | Wikipedia, Field service management | secundaria (enciclopedia; la propia página marca "citation needed") | [L] | 1 | 1 | 1 | 1 | https://en.wikipedia.org/wiki/Field_service_management |
| 8 | Odoo documentación, índice de Field Service | primaria (de sistema) | [M] solo índice de subpáginas | 2 | 1 | 1 | 1 | https://www.odoo.com/documentation/18.0/applications/services/field_service.html |
| 9 | Wikipedia, Vehicle routing problem | secundaria | [L] | 1 | 2 | 1 | 1 | https://en.wikipedia.org/wiki/Vehicle_routing_problem |

Intentadas sin éxito (no cuentan como fuente): Salesforce Field Service help (página dinámica sin contenido), SAP (no intentada), APQC PCF (403), ScienceDirect (403), HBR (404 en las dos URL probadas), subpáginas de Odoo (404), Field Service News (404), Crossref (429), customer assets e inventario de Dynamics (404).

## Componente 1: servicio de campo (entrada)

### Afirmaciones respaldadas

- **Definición.** El field service management es la gestión de recursos de una empresa "employed at or en route to the property of clients, rather than on company property"; aplica sobre todo a firmas que instalan, mantienen o reparan sistemas o equipos. Fuente 7 (secundaria débil): https://en.wikipedia.org/wiki/Field_service_management
- **Qué lo distingue del mantenimiento interno (visible en el modelo de datos).** El trabajo ocurre "at customer locations" y el sistema mantiene "customer equipment and service history" aparte (fuente 1). La orden lleva "labor to bill to the customer" y "parts to use" (fuente 1), y cerrar la orden genera factura por repuestos y mano de obra (fuente 2). O sea: el equipo es del cliente, el trabajo se factura y el viaje es un costo del servicio. Fuente 1: https://learn.microsoft.com/en-us/dynamics365/field-service/overview ; fuente 2: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status
- **Viaje como concepto propio.** Si la cuenta de servicio tiene un cargo de viaje configurado y la reserva tiene duración de viaje distinta de cero, el sistema agrega el "travel charge item" como producto de la orden. Los estados de la reserva incluyen "Traveling" y se registran "Miles Traveled" y "Actual Travel Duration". Fuente 2.
- **Cuenta de servicio y cuenta de facturación son distintas.** "Service Account & Billing Account: Defines where the agreement work orders take place, while the billing account defines who the invoice should be sent to." Fuente 3: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-agreements-work-orders
- **Secuencia caso → orden → visita → cierre → factura.** Las órdenes "generate from service cases, sales orders, emails, phone calls, service agreements, web portals, or Internet of Things (IoT) data" (fuente 1). El ciclo típico es: creación, programación (schedule), despacho (dispatch), servicio, revisión/aprobación, factura y ajuste de inventario (fuente 2). Quién hace cada paso: la creación, soporte (si viene de un caso), el contrato (si es recurrente) o ventas; la programación, el despachante, el técnico o un motor de ruteo; la revisión, un supervisor o administración. Fuente 2.
- **La orden y la visita tienen ciclos de vida independientes.** Estados de la orden: Unscheduled, Scheduled, In Progress, Completed, Posted, Canceled. Estados de la reserva (visita): Scheduled, Traveling, In Progress, On Break, Completed, Canceled. Cita literal: "Work orders and bookings have independent lifecycles." Una orden puede tener varias reservas, y se puede completar una reserva sin completar la orden para dejar seguimiento. Fuente 2. Relevante para el modelo: orden de servicio y visita son dos objetos.
- **Cobro como paso final y separado de la ejecución.** El estado "Posted" lo pone alguien de administración tras revisar, y dispara la factura. Fuente 2.
- **Roles.** Agentes de atención que "triage incoming requests and determine when to create work orders for onsite visits"; despachantes; técnicos; gerentes de servicio; encargados de inventario. Fuente 1. Marca el límite con Servicio al cliente: la atención hace el triage y decide si hay que ir.
- **Cuatro modelos de entrega.** Reactivo (break-fix), preventivo (por acuerdo), predictivo (por IoT) y por proyecto. Fuente 1.

### Cómo divide el campo esta vertical (APQC y analistas): SIN VERIFICAR

No pude leer el PCF de APQC (403) ni informes de analistas. **El encargo da 6.0 = servicio al cliente y 5.0 = entregar servicios; no pude confirmarlo ni refutarlo.** Hay que leer el PCF cross-industry en la versión vigente antes de escribirlo en la nota. Tampoco verifiqué la separación de mercado "field service management" frente a "customer engagement center". Pendiente.

### Dónde el campo corta distinto que el árbol propuesto

- El campo trata **contrato/acuerdo, activo del cliente y orden de servicio como un solo modelo**, y el contrato es lo que genera las órdenes preventivas (fuente 3). El árbol propone contrato y base instalada como componentes separados; sirve como capas de lectura, pero la nota de contrato tiene que explicar que el contrato es el generador del trabajo preventivo, no solo una cláusula de cobertura.
- El campo no separa "despacho y agenda" de "visita técnica" por actividad sino por objeto: **orden (el trabajo pedido)** frente a **reserva/visita (la cita concreta de un recurso)**, y el despacho es lo que las une (fuente 2). Las notas de despacho y de visita deberían nombrar esos dos objetos.
- Repuestos y stock en camioneta aparecen como **inventario** ("truck stock", fuente 1), un área que cruza con otros temas.

## Componente 2: base instalada

### Afirmaciones respaldadas

- **Registro del equipo del cliente.** Dynamics ofrece "asset management capabilities to keep track of customer equipment and service history" (fuente 1).
- **Se alimenta desde la entrega o la instalación.** Cuando se instala una pieza en el domicilio, el sistema "documents a reduction in inventory from the related warehouse or truck and document the part as a new customer asset along with installation and repair details" (fuente 1). Al completar la orden, los productos con "Convert to Customer Asset" = Yes pasan a ser activos del cliente (fuente 2). En ERPNext, cuando el número de serie viene de una orden de venta, "the Customer will be linked here", y solo se entregan seriales con estado "Available" (fuente 6): https://docs.frappe.io/erpnext/user/manual/en/serial-no
- **La orden apunta a un activo y construye historial.** En un contrato recurrente se especifica el activo en el incidente: "you can define recurring work that should be performed on specific equipment and build service history" (fuente 3).
- **El estado de cobertura se deriva del activo.** Al elegir el número de serie en un reclamo, ERPNext trae el artículo y el estado ("Under Warranty", "Out of Warranty", "Under AMC", "Out of AMC") con fechas de vencimiento, editable a mano (por ejemplo, si el equipo fue manipulado). Fuente 4: https://docs.frappe.io/erpnext/user/manual/en/warranty-claim

### Qué no encontré

Ubicación del equipo como entidad separada del cliente, jerarquía/configuración de componentes, fecha de instalación como campo. Hueco.

## Componente 3: contrato de servicio

### Afirmaciones respaldadas

- **Garantía y contrato de mantenimiento son dos fuentes de cobertura en el mismo reclamo.** El Warranty Claim "records a Customer's request for free repairs on an item or service still covered by warranty or an Annual Maintenance Contract (AMC)". Fuente 4.
- **Un contrato concentra cliente, vigencia, lista de precios y recurrencia.** Pasos: crear el acuerdo (cliente, fechas, lista de precios), agregar la programación de reservas (recurrencia, valores por defecto), agregar detalles (incidentes, productos, servicios, tareas) y activar. Fuente 3.
- **Precio negociado.** "Agreements usually contain a negotiated price for goods and services that are reflected in an entirely new price list." Fuente 3.
- **Visitas preventivas incluidas = órdenes generadas por recurrencia.** Ejemplo: mantenimiento mensual durante un año sobre un equipo instalado, generado a mitad de mes "with some flexibility". Hay patrón de recurrencia, días de anticipación (por defecto siete) y flexibilidad antes y después (ejemplo: día 8, ±7 días, ventana del 1 al 15). Fuente 3: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-agreements-work-orders
- **Break-fix frente a contrato.** Reactivo: "a customer reports an issue, a customer service agent creates a work order, and a dispatcher schedules a technician". Preventivo: "scheduled maintenance happens on a recurring basis through agreements". Fuente 1.
- **Tipo de visita.** ERPNext clasifica la visita como Scheduled, Unscheduled o Breakdown. Fuente 5: https://docs.frappe.io/erpnext/user/manual/en/maintenance-visit
- **Qué se factura.** En Dynamics el tiempo de trabajo es facturable por defecto y el descanso solo si la lista de precios lo indica ("Total Billable Duration"); el viaje se agrega como producto (fuente 2). Lo cubierto o no se resuelve por el estado de cobertura (fuente 4), pero **ninguna fuente leída describe la regla de cobertura (piezas, mano de obra, viaje) por contrato**.

### Qué no encontré

SLA de respuesta y resolución como objeto del contrato. Diferencia garantía (obligación del vendedor) frente a contrato (producto pagado) en una fuente conceptual. Hueco.

## Componente 4: despacho y agenda

### Afirmaciones respaldadas

- **Criterios de asignación.** "An interactive schedule board helps dispatchers assign work orders to the best resources based on location, availability, skill set, priority, and more", en tres modos: arrastrar a mano, asistente semiautomático o automático con un motor de optimización. Fuente 1: https://learn.microsoft.com/en-us/dynamics365/field-service/overview
- **Ventanas.** El contrato pasa a la orden "Date Window Start/End" y "Time Window Start/End" (ejemplo: entre 8:00 y 12:00). Fuente 3.
- **Recursos no son solo personas.** El tablero muestra "each resource - whether an employee, contractor, or equipment". Fuente 1.
- **Contraejemplo de modelado.** "Agreements create bookings according to recurrence without considering any other factors, including if the resource is active or their working hours." Fuente 3.
- **Despacho con notificación y aceptación.** El técnico recibe aviso y "may review and accept/decline the work order". Fuente 2.
- **Centralizado frente a autoasignación.** La fuente 2 indica para órdenes no planificadas "By field agent or centralized scheduling", es decir, ambas existen en el modelo. Ninguna fuente leída las compara.
- **Optimización.** Wikipedia sobre ruteo de vehículos menciona ventanas horarias ("The delivery locations have time windows within which the deliveries (or visits) must be made") pero **no menciona técnicos ni habilidades**. Fuente 9: https://en.wikipedia.org/wiki/Vehicle_routing_problem

### No verificado: survey académico

De memoria, sin consulta: Castillo-Salazar, Landa-Silva y Qu, "Workforce scheduling and routing problems: literature survey and computational study", Annals of Operations Research, 2016; Paraskevopoulos et al. (2008) sobre technician routing and scheduling, Computers & Operations Research. **El encargo pide un survey en EJOR o C&OR; no lo verifiqué.** Buscar y leer el abstract antes de citar.

## Componente 5: visita técnica

### Afirmaciones respaldadas

- **Llegada y cierre con sello de tiempo.** Pasar a "In Progress" indica la llegada y completa "Actual Arrival Time" y "First Arrived On" en la orden; cada cambio de estado crea una marca de tiempo; el cierre calcula duración total, descanso, duración facturable y costo. Fuente 2: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status
- **Información, offline y firma.** El técnico ve ubicación, instrucciones, activos e historial; puede "take pictures and videos or record a digital customer signature" y descargar datos "for offline work when internet isn't available". Fuente 1.
- **Conformidad.** Dynamics: firma digital (fuente 1). ERPNext: "Customer Feedback" opcional y estado "Partially Completed" o "Fully Completed" (fuente 5).
- **Repuestos y stock en camioneta.** Los encargados de inventario aseguran que el técnico tenga lo necesario; el sistema cubre "truck stock" y descuenta del almacén "or truck" al instalar. Fuente 1.
- **Cierre con seguimiento.** El técnico marca la orden "as complete or as requiring a follow-up" (fuente 1); la tabla de mapeo con "Partially Completed" devuelve la orden a Unscheduled (fuente 2).
- **Definición ERPNext.** "A Maintenance Visit is a visit made by an engineer to a Customer's premise for maintenance work of an Item." Registra cliente, artículo, serie, descripción, trabajo realizado y feedback; la página no lista repuestos consumidos. Fuente 5.
- **First-time fix.** Dynamics lo lista como objetivo ("Improve first-time fix rate") sin cifra ni definición (fuente 1); Wikipedia lo menciona como beneficio sin cifra (fuente 7). **No hay definición, cifra ni causas de falla leídas.**

### Qué no encontré

Causas de falla de first-time fix (falta de repuesto, de habilidad, mal diagnóstico): es saber de sector sin fuente leída. Informe de servicio como documento. Hueco.

## Métricas del servicio de campo

Sin fuente verificada y sin cifras: no leí TSIA, Aberdeen, Field Service News ni encuestas. Cuando se consigan, marcarlas como **cifra de encuesta de un proveedor o practicante**, con muestra y año. Lo único respaldado: el sistema registra los datos para calcularlas (hora de llegada, duración de viaje, duración en curso y facturable; fuente 2) y los proveedores las presentan como objetivo (fuente 1).

## No verificadas (no citar sin confirmar)

| Referencia | Estado |
|---|---|
| Cohen, Agrawal y Agrawal, "Winning in the Aftermarket", HBR, 2006 | Dado por el encargo. Dos URL de hbr.org probadas (404). Falta URL y abstract. Natural para por qué importa el posventa |
| Castillo-Salazar, Landa-Silva y Qu (2016), Annals of OR | De memoria |
| Paraskevopoulos et al. (2008), Computers & Operations Research | De memoria |
| APQC PCF categorías 5.0 y 6.0 | 403 |
| Gartner (FSM frente a customer engagement center), TSIA, Aberdeen, Field Service News | No consultadas |
| Salesforce Field Service, SAP Service | Página sin contenido / no consultada |

## Recursos canónicos propuestos (provisorios, solo de lo leído)

| Componente | Recurso | Qué parte | En qué fijarse |
|---|---|---|---|
| Servicio de campo | Microsoft Learn, "Work order lifecycle and system statuses" (fuente 2) | Tabla "Typical work order lifecycle" y tabla de estados | Orden y reserva con ciclos independientes; quién hace cada paso; factura como paso final aparte |
| Base instalada | ERPNext, Serial No + Warranty Claim (fuentes 6 y 4) | Garantía/AMC y estados de cobertura | Cobertura derivada del serial; vencimientos |
| Contrato de servicio | Microsoft Learn, "Set up customer agreements to generate work orders" (fuente 3) | Pasos 1 a 5 | Recurrencia, flexibilidad de fechas, precio negociado, advertencia sobre reservas automáticas |
| Despacho y agenda | Microsoft Learn, Overview, paso 2 (fuente 1) + survey académico por confirmar | Tablero de programación | Criterios de asignación; manual, asistido, automático |
| Visita técnica | Microsoft Learn, Overview, pasos 3 y 4 (fuente 1) + ERPNext Maintenance Visit (fuente 5) | Offline, firma, seguimiento, ajuste de inventario | Cierre parcial con seguimiento; llegada y viaje con sello de tiempo |

Falta el recurso canónico conceptual (no de producto) de cada componente.

## Huecos

1. Mapa de fuentes no-producto: APQC PCF, Gartner y analistas, TSIA, Aberdeen, Field Service News. Sin ellos no se afirma cómo divide el campo la vertical (5.0 frente a 6.0; FSM frente a customer engagement center).
2. Cohen, Agrawal y Agrawal (HBR 2006): sin URL ni abstract.
3. Survey académico de ruteo y programación de técnicos: citas de memoria.
4. Métricas con fuente: first-time fix, tiempo medio de respuesta, utilización. Cero cifras y definiciones.
5. SLA y cobertura de contrato (piezas, mano de obra, viaje; tiempos).
6. Causas de falla de first-time fix.
7. Salesforce y SAP no leídas; Odoo solo el índice.
8. Despacho centralizado frente a autoasignación: sin fuente comparativa.
9. Fecha de instalación, ubicación y configuración del activo.
10. Informe de servicio como documento.

Siguiente paso: repetir cuando se renueve el presupuesto de búsquedas (o se suba `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`), empezando por los huecos 1 a 4.

## Segunda ronda

Fecha: 2026-11-27. Solo WebFetch sobre URLs directas (WebSearch agotado). Misma nota de lectura que arriba: [L] = la página se recuperó e interrogó; las citas son las que devolvió el recuperador. Excepción: el PCF de APQC (fuente 10) se leyó con pdftotext sobre el PDF descargado. Puntajes A/P/E/U de 1 a 3.

### Fuentes nuevas verificadas

| # | Fuente | Tipo | Marca | A | P | E | U | URL |
|---|---|---|---|---|---|---|---|---|
| 10 | APQC PCF cross-industry v7.4 (agosto 2024), copia en solutions.ifrc.org | primaria (marco de referencia) | [L] | 3 | 3 | 2 | 3 | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf |
| 11 | Microsoft Learn, Customer agreements overview (2026-08-28) | primaria (de sistema) | [L] | 2 | 2 | 3 | 3 | https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-customer-agreements (redirige a agreements-overview) |
| 12 | Microsoft Learn, Entitlements for work orders overview (2026-09-16) | primaria (de sistema) | [L] | 2 | 3 | 3 | 3 | https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-entitlements-overview |
| 13 | Microsoft Learn, Create entitlements for work orders (2026-08-07) | primaria (de sistema) | [L] | 2 | 3 | 3 | 3 | https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-entitlements |
| 14 | Microsoft Learn, Configure SLAs in Customer Service (2026-11-06) | primaria (de sistema) | [L] | 2 | 3 | 2 | 3 | https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/define-service-level-agreements |
| 15 | Microsoft Learn, Resource Scheduling Optimization overview (2026-10-29) | primaria (de sistema) | [L] | 2 | 2 | 3 | 3 | https://learn.microsoft.com/en-us/dynamics365/field-service/rso-overview |
| 16 | Microsoft Learn, Schedule assistant overview | primaria (de sistema) | [L] | 2 | 2 | 2 | 2 | https://learn.microsoft.com/en-us/dynamics365/field-service/schedule-assistant |
| 17 | Microsoft Learn, Manually schedule from the schedule board | primaria (de sistema) | [L] | 2 | 1 | 2 | 2 | https://learn.microsoft.com/en-us/dynamics365/field-service/schedule-board-manual-scheduling |
| 18 | Odoo 17.0 Field Service: Product management y Worksheets | primaria (de sistema) | [L] | 2 | 1 | 1 | 2 | https://www.odoo.com/documentation/17.0/applications/services/field_service/product_management.html ; https://www.odoo.com/documentation/17.0/applications/services/field_service/worksheets.html |
| 19 | Wikipedia, Installed base | secundaria | [L] | 1 | 1 | 1 | 1 | https://en.wikipedia.org/wiki/Installed_base |
| 20 | Wikipedia, Service-level agreement | secundaria | [L] | 1 | 2 | 1 | 1 | https://en.wikipedia.org/wiki/Service-level_agreement |
| 21 | Wikipedia, Warranty | secundaria | [L] | 1 | 2 | 1 | 2 | https://en.wikipedia.org/wiki/Warranty |
| 22 | HBR, Cohen, Agrawal y Agrawal, "Winning in the Aftermarket" (mayo 2006, reprint R0605H). Solo el resumen público | primaria (artículo), leída solo la portada | [M] | 3 | 1 | 1 | 3 | https://hbr.org/2006/05/winning-in-the-aftermarket |

La URL de HBR funcionó esta vez (en la ronda 1 dio 404 en otras dos).

Fallaron (no cuentan): Wikipedia Servitization, Servitisation, First-time fix y Technician routing and scheduling problem (404); ScienceDirect Paraskevopoulos et al. (403); Springer Castillo-Salazar (redirige a login); Salesforce help (página de error); Dynamics define-entitlements, entitlement-overview, inventory-and-warehouses-overview, inventory-overview e inventory-management (404); Odoo create_tasks y plan_itinerary (404). Un identificador arXiv probado a ciegas devolvió un artículo de matemática sin relación: no usar identificadores que no se vean escritos en una página.

### 1. Definición y alcance

- Wikipedia: field service management "refers to the management of a company's resources employed at or en route to the property of clients". Funciones: localizar vehículos, gestionar la actividad del trabajador, programar y despachar, e "integrating these activities with inventory, billing, accounting, and other back-office systems". Nombra el "first-time-fix rate" sin cifra ni definición. No menciona contratos ni SLA. https://en.wikipedia.org/wiki/Field_service_management (secundaria, 1)
- Base instalada: "Installed base of a product is the number of units that are currently in use by customers." La distingue de la cuota de mercado. "Service providers use the installed base information to determine the level of support" y para asignar recursos; afecta la "availability of replacement parts and accessories". No menciona mantenimiento ni posventa. Es un conteo de unidades de un producto, no un registro de activos por cliente: son dos sentidos distintos y la nota debe decir cuál usa. https://en.wikipedia.org/wiki/Installed_base
- Garantía: "an expressed or implied promise or assurance of some kind"; en contratos, promesa del vendedor al comprador. Implícita: "unwritten promises that arise from the nature of the transaction", según la jurisdicción (en EE.UU., el UCC implica comerciabilidad y aptitud para un fin salvo exclusión). Garantía extendida o "service contract": la venden terceros o fabricantes y "extend the warranty for a further length of time", con términos que pueden diferir y exclusiones (uso comercial, abuso, piezas de desgaste). Cubre en parte el hueco 5 de la ronda 1 (garantía como promesa del vendedor frente a contrato como producto vendido), pero es derecho de EE.UU.: no verificado para Argentina. https://en.wikipedia.org/wiki/Warranty
- SLA: "an agreement, typically a binding contract, between a service provider and a customer". Contenidos: tiempo de respuesta ("the period by which the service provider will start the investigation of the issue"), plazo de resolución ("Issue resolution time frame"), disponibilidad, MTTR, MTBF, reportes. Si se incumple, el cliente puede terminar o pedir compensación; en tercerización, "financial penalties and the right to terminate if any of the SLA metrics are consistently missed". https://en.wikipedia.org/wiki/Service-level_agreement
- Servitización como concepto: sin fuente leída (Wikipedia 404). Solo el resumen de HBR (sección 6).

### 2. Contrato, cobertura, SLA, qué se factura

- El acuerdo genera trabajo y facturas: "Field Service agreements let organizations automatically generate work orders and invoices with predefined details, frequencies, and date ranges." Ejemplos: mantenimiento trimestral de ascensores, control de plagas semanal. Variantes: órdenes que programa el despachante, órdenes que programa el motor de optimización, el mismo recurso cada vez, una orden mensual para varios activos de un cliente, y "quarterly invoices to bill customers for predefined products and services". Fuente 11.
- Una ubicación por acuerdo: "An agreement is intended to be executed at a single location represented by the service account. Configure work at different locations with multiple agreements." Fuente 11.
- Decisión de modelado: varias incidencias en una recurrencia dan una orden; varias recurrencias dan varias órdenes y más viajes. Quien quiera atar tiempo a un activo elige una orden por activo. Fuente 11. Evidencia de práctica: el viaje es criterio de diseño del contrato.
- Doble facturación: "Even if an agreement generates invoices, agreement work orders create invoices upon completion and Close-Posted status." Si solo vale la factura del acuerdo, hay que desactivar la de la orden o dejarla en $0 con listas de precio y derechos. Fuente 11. La cuota del contrato y la factura por visita se pueden duplicar.
- Cobertura como derecho (entitlement) que cambia el precio, no el costo: "Entitlements can't change the cost of a product or service, only the price." Se aplican por cuenta de facturación, cuenta de servicio, producto o servicio, activo, categoría de activo o tipo de incidencia. Fuente 12.
- Ejemplos de la doc: 10% de descuento por dos años sobre todo, y 100% de descuento por dos años para activos de la categoría "Heating, Venting, and Air Conditioning". Las condiciones de una "aplicación" se combinan con AND. El descuento se aplica cuando la línea pasa de "Estimated" a "Used". Fuentes 12 y 13.
- Prioridad entre derechos: gana el de prioridad más alta (1 es la mayor); si empatan, "the most specific entitlement"; se puede anular a mano. Fuente 12.
- Límite explícito: "Entitlements for work orders don't support quantity-based and limit-based entitlements. For example, it's not possible to create an entitlement for 10 work orders or free service for the first hour." No hay "X visitas incluidas" ni "primera hora gratis" en este modelo. Fuente 12.
- SLA como objeto (Customer Service, sobre casos, no sobre la orden de campo): KPIs como "First Response or Resolve by"; ítems con condiciones "Applicable When", condiciones de éxito, duración de aviso y de falla, horario hábil opcional ("If you don't set the business hours record (customer service schedule), the work hours are considered to be all day, every day") y pausa/reanudación cuando el caso queda en espera. Estados: "Nearing noncompliance", "Succeeded", "Noncompliant". Fuente 14. El motor de optimización "helps avoid service level agreement penalties" dando preferencia a lo prioritario (fuente 15), sin describir el SLA de la orden.
- Odoo: con "Time and Material Invoicing" activo, los productos del catálogo cargados en la tarea se agregan solos a la factura; los productos de pedidos creados en la intervención "are always pulled from the default warehouse" y "Once the Field Service task is marked as done, the stock of the default warehouse is automatically updated". Worksheets: formularios que el técnico completa en sitio; la página no menciona firma ni facturación. Fuente 18.
- Sigue abierto: regla de cobertura por tipo de costo (piezas, mano de obra, viaje) por contrato; tiempos contractuales de respuesta y resolución en sitio (por ejemplo "4 horas"); Salesforce.

### 3. Despacho, agenda y ruteo

- Tres niveles en Dynamics: manual (tablero), semiautomático (asistente) y automático (optimización). Fuentes 15 a 17.
- Manual: "Manual bookings don't validate constraints like availability, characteristics, or location." Sirve para urgencias, casos simples y excepciones. Fuente 17.
- Asistente: "recommends resources that match criteria like availability, skills, and location" y "estimates travel time for the recommended resources"; filtra por ubicación, características, territorio y tipo de recurso. "If you book outside the schedule assistant's recommended slots, constraints such as capacity, work hours, and time windows aren't verified or enforced." Fuente 16.
- Optimización (complemento pago, precio por recurso optimizado): programa varios trabajos a la vez, "maximizes resource use and minimizes travel time", considera "characteristics, territory, promised time windows". Dice que ataca una variante del problema del viajante. Modos: nocturno, de un recurso, simulación, intradía (cada 30 minutos), emergencia. Objetivos rankeados porque hay compensaciones. Vocabulario: trabajo, recurso (persona, equipo o instalación), requerimiento, reserva, alcance. Fuente 15.
- Los acuerdos pueden dejar la reserva al motor o bloquear recurso y horario. Fuente 11.
- Survey académico: NO verificado. Ni Paraskevopoulos et al. (EJOR 2017) ni Castillo-Salazar et al. (Ann. Oper. Res. 2016) abrieron; las citas siguen de memoria y no deben ir a la nota.

### 4. Visita, stock en camioneta y first-time fix

- Las páginas de inventario de Dynamics dieron 404 y Salesforce no cargó. Solo hay lo de la ronda 1 (fuentes 1 y 2) y Odoo (almacén por defecto; el stock baja al marcar la tarea como hecha). Fuente 18.
- First-time fix: sin definición ni cifra. Hueco que sigue.

### 5. APQC PCF v7.4 (detalle de 10.0 en `apqc-10.md`)

- Nombres literales: "5.0 Deliver Service" (el índice dice "Deliver Services"), "6.0 Manage Customer Service", "10.0 Acquire, Construct, and Manage Assets". Resuelve el hueco 1 de la ronda 1: 5.0 y 6.0 son lo que dijo el encargo. Fuente 10.
- El servicio técnico en campo está en 6.3 "Service products after sales" (12658), no en 5.0. Dentro: 6.3.1 "Register products"; 6.3.2 "Process warranty claims" (con 6.3.2.3.2 "Schedule field service"); 6.3.3 "Manage supplier recovery"; 6.3.4 "Service products" con 6.3.4.1.3 "Generate service order", 6.3.4.2 "Identify and schedule resources to meet service requirements", 6.3.4.3 "Provide service to specific customers" (6.3.4.3.1 "Organize daily service order fulfillment schedule", 6.3.4.3.2 "Execute product repair", 6.3.4.3.3 "Manage service order fulfillment") y 6.3.4.4 "Ensure quality of service". Fuente 10.
- Lo más parecido a cobertura y SLA: 6.1.5 "Establish target service level for each customer segment", 6.1.6 "Define warranty claims" (6.1.6.1 "Determine and document warranty policies", 6.1.6.4 "Define warranty related offerings for customers") y 6.5.4 "Evaluate and manage warranty performance". Fuente 10.
- 5.0 es entrega de servicios por contrato y proyecto (5.3.1.1 "Review contract and agreed terms", 5.2.2.3 "Match resource demand with capacity, skills, and capabilities", 5.3.3.3 "Confirm delivery according to contract terms"). Lectura mía a partir de los títulos: sirve para contrato, capacidad y habilidades, no para reparación en casa.
- 10.0 es mantenimiento de los activos propios: 10.3 "Maintain assets" (10.3.1 Plan, 10.3.2 Manage, 10.3.3 Perform asset maintenance). Lectura mía: 10.3 es el espejo del lado de quien posee el activo (el cliente de un contrato) y 6.3.4 el del lado de quien presta el servicio. El PCF no lo dice.

### 6. Servitización y posventa [M]

- HBR, resumen visible: las empresas que venden soluciones "have long recognized the value of selling spare parts and after-sales services"; los autores hablan de "the golden age of services"; los ejecutivos temen en privado que la mayoría de las compañías "either don't know how or don't care to provide after-sales services effectively"; la alta gerencia trata el servicio posventa como "a mere afterthought". Cuerpo no leído: sin recomendaciones ni cifras. Fuente 22.

### Huecos que siguen abiertos

1. Survey académico de ruteo y programación de técnicos (abstract no leído).
2. First-time fix y tiempo de respuesta: definición, cifras, causas.
3. Contrato de campo: cobertura por tipo de costo, visitas incluidas, tiempos contractuales de respuesta y resolución en sitio.
4. Salesforce y SAP; inventario y camioneta de Dynamics.
5. Servitización como concepto.
6. Despacho centralizado frente a autoasignación; informe de servicio como documento.
7. Normativa argentina de garantías.
