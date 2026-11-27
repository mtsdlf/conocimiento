# Taxonomías externas: ¿el árbol cubre cómo se divide este mundo?

Investigación para el issue #96 del mapa #94 (software de gestión). Fecha de todas las lecturas: 2026-11-27.

Marcas: [L] leído de la fuente (WebFetch, o el PDF bajado y pasado a texto), [S] solo el resumen del buscador o una copia de terceros, sin la fuente a mano. Varias fuentes del rubro están detrás de un muro (APQC devuelve 403 en casi todo, Gartner también, ASCM arma sus páginas con JavaScript): lo que salió de ahí va marcado [S] y conviene cotejarlo antes de citarlo en una nota.

El árbol contra el que se compara es el de «Forma del árbol» (#95): diez temas de dominio (Contabilidad; Tesorería y finanzas de la empresa en marcha; Impuestos; Compras y abastecimiento; Inventario y depósitos; Cadena de suministro y logística; Producción; Relación con clientes; Servicio al cliente y de campo; Gestión de personas y nómina), la vertical de inteligencia de negocio dentro de `Datos`, el tema «Procesos de negocio» y el tema «Software de gestión». El issue #96 habla de «11 dominios»: cuenta la vertical de BI como uno; el cierre de #95 dice diez temas más esa vertical.

## En corto

- **El árbol cubre lo administrativo y lo de la cadena física casi uno a uno**: la categoría 9 de APQC (finanzas) se reparte limpia entre Contabilidad, Tesorería e Impuestos, y la 4 (entregar productos físicos) entre Compras, Inventario, Cadena de suministro y Producción.
- **Faltan tres cosas que todas las taxonomías tienen y el árbol no**: entregar servicios y proyectos (APQC 5.0, la familia «Services» de Odoo, el módulo Projects de ERPNext, el ERP para empresas de servicios de Gartner), activos y mantenimiento (APQC 10.0, Maintenance y Assets en los dos ERP, la gestión de mantenimiento de ISA-95) y calidad (Quality en los dos ERP, ISA-95, un módulo de CPIM). Riesgo y cumplimiento (APQC 11.0) y desarrollo de producto físico (APQC 2.0, PLM) quedan como huecos menores.
- **Tres cortes del árbol no los hace nadie afuera**: separar Inventario y depósitos de Cadena de suministro y logística (las fuentes juntan depósito con logística, o inventario con planificación), tener Relación con clientes como dominio propio (APQC no tiene categoría de «relación con clientes», y los analistas parten el CRM en ventas, servicio y marketing) y poner la nómina en un solo tema (APQC la tiene en dos lugares a la vez).
- **Lo que el árbol puso como tema aparte sí tiene respaldo**: Procesos de negocio calca la separación de APQC entre su marco funcional y sus mapas de punta a punta, y Software de gestión calca la distinción de ISA-95 entre el nivel del negocio (ERP) y el de la planta (MES).
- **Dos solapes con temas que ya existen**: `Datos/Visualizacion-y-BI` ya está armada (la vertical de BI que pide #95 no es nueva, es ampliar esa) y `Liderazgo-y-direccion/Gestion-de-personas` ya trata contratar, evaluar, compensar y desvincular.

## 1. Las taxonomías, cómo dividen

### 1.1 APQC Process Classification Framework (cross-industry)

- **13 categorías** de nivel 1, en dos grupos: operativas (1.0 a 6.0) y de gestión y soporte (7.0 a 13.0). Debajo, cuatro niveles más: grupo de procesos, proceso, actividad y tarea. [L] https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Understanding%20the%20PCF%20Elements%20%20-%20FINAL.pdf
  1.0 Develop Vision and Strategy · 2.0 Develop and Manage Products and Services · 3.0 Market and Sell Products and Services · 4.0 Deliver Physical Products · 5.0 Deliver Services · 6.0 Manage Customer Service · 7.0 Develop and Manage Human Capital · 8.0 Manage Information Technology · 9.0 Manage Financial Resources · 10.0 Acquire, Construct, and Manage Assets · 11.0 Manage Enterprise Risk, Compliance, Remediation, and Resiliency · 12.0 Manage External Relationships · 13.0 Develop and Manage Business Capabilities.
- **El marco es funcional, no de punta a punta**, y lo dice: «The PCF reflects a functional view of an organization, rather than a cross-functional view», sigue el principio MECE y «does not imply order». [L] https://www.apqc.org/sites/default/files/files/PCF%20Collateral/PCF%20Business%20Rules.pdf
- **Los procesos de punta a punta van aparte**: APQC los define como «cross-functional processes that comprise all the steps to accomplish a specific outcome or goal», da de ejemplo order-to-cash, hire-to-retire e idea-to-market, y usa el PCF como «lista de ingredientes» (order-to-cash toma 3.5.4.1 «Accept and validate sales order» y 3.5.4.3 «Determine availability»). [L] https://www.apqc.org/blog/why-are-end-end-processes-important
- **Mapas de punta a punta que publica APQC** (para socios): procure-to-pay, record-to-report, order-to-cash, hire-to-retire, issue-to-resolution, lead-to-order; colección actualizada el 19-11-2025. [S] https://www.apqc.org/resource-library/resource-collection/end-end-process-maps-and-measures
- **Grupos de nivel 2 usados en la tabla** (versión 7.2.1, copia de terceros del PDF de APQC; la numeración cambia entre versiones): [S] https://www.slideshare.net/AsgharAghiliDehkordi/cross-industry-v721-final
  - 3.0: 3.1 entender mercados y clientes, 3.2 estrategia de marketing, 3.3 planes de marketing, 3.4 estrategia de ventas, 3.5 planes de ventas (adentro, 3.5.4 los pedidos).
  - 4.0: 4.1 Plan for and align supply chain resources, 4.2 Procure materials and services, 4.3 Produce/Assemble/Test product, 4.4 Manage logistics and warehousing.
  - 5.0: 5.1 gobierno y estrategia de la entrega de servicios, 5.2 recursos para entregarlos, 5.3 entregar el servicio al cliente.
  - 6.0: 6.1 estrategia de atención, 6.2 contactos de atención, 6.3 Service products after sales, 6.4 retiros de producto y auditorías regulatorias, 6.5 evaluar la atención y la satisfacción.
  - 7.0: 7.1 planificación y políticas de RR. HH. a 7.9, con 7.5 Reward and retain employees (adentro, 7.5.4 Administer payroll) y 7.7 información y analítica de empleados.
  - 9.0: 9.1 contabilidad de gestión, 9.2 contabilidad de ingresos, 9.3 contabilidad general y reportes, 9.4 activos fijos, 9.5 Process payroll, 9.6 cuentas a pagar y rendición de gastos, 9.7 Manage treasury operations, 9.8 controles internos, 9.9 Manage taxes, 9.10 fondos internacionales y consolidación, 9.11 comercio exterior.
- **Versión vigente**: APQC publicó la 7.4 (21-08-2024) y la 8.0 (27-02-2026). No se pudo leer ninguna de las dos (403); la tabla usa la 7.2.1 y cualquier número de nivel 2 hay que cotejarlo con la 8.0. [S] https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-cross-industry-pdf-12 · [S] https://www.apqc.org/pcf-pdf

### 1.2 Odoo (cómo corta un producto)

Las apps, agrupadas como las agrupa la documentación oficial: [L] https://www.odoo.com/documentation/18.0/applications.html (y la vitrina [L] https://www.odoo.com/page/all-apps)

- **Finance**: Accounting and Invoicing, Expenses, Online payments, Fiscal localizations.
- **Sales**: CRM, Sales, Point of Sale, Subscriptions, Rental, Members.
- **Supply Chain**: Inventory, Manufacturing, Purchase, Barcode, Quality, Maintenance, Product lifecycle management, Repairs.
- **Human resources**: Attendances, Employees, Appraisals, Frontdesk, Fleet, Payroll, Time off, Recruitment, Referrals, Lunch, Approvals.
- **Marketing**: Email, SMS y Social Marketing, Marketing Automation, Events, Marketing Card, Surveys.
- **Services**: Project, Timesheets, Planning, Field Service, Helpdesk.
- **Productivity**: Documents, Sign, Spreadsheet, Dashboards, Knowledge, Calendar, Appointments, Discuss y otras.
- **Websites** (sitio, tienda, cursos, foro, blog, chat), **Studio** y **General settings**; «Reporting» figura entre los «Odoo essentials», o sea, en todas las apps.

### 1.3 ERPNext

Los módulos salen del código: `erpnext/modules.txt` y, para personal, la app aparte `hrms`. [L] https://github.com/frappe/erpnext/blob/develop/erpnext/modules.txt · [L] https://github.com/frappe/hrms/blob/develop/hrms/modules.txt

- **ERPNext**: Accounts, CRM, Buying, Projects, Selling, Setup, Manufacturing, Stock, Support, Utilities, Assets, Portal, Maintenance, Regional, ERPNext Integrations, Quality Management, Communication, Telephony, Bulk Transaction, Subcontracting, EDI.
- **HRMS** (otra app): HR Setup, Tenure, Recruitment, Shift and Attendance, Leaves, Expenses, Performance, Payroll, Tax and Benefits, HR.

Dos cosas que muestra: separa CRM (antes del pedido) de Selling (el pedido en adelante), y saca personas y nómina a una aplicación propia.

### 1.4 Categorías de los analistas

Casi todo está detrás de un muro; lo que sigue sale de resúmenes de Gartner y de terceros que los citan.

- **ERP** se parte en dos cuadrantes por tipo de empresa: «Cloud ERP for Product-Centric Enterprises» (soporta y automatiza «operational activities across manufacturing, distribution, and supply chain») y «Cloud ERP for Service-Centric Enterprises», los dos de octubre de 2025. [S] https://www.gartner.com/en/documents/7058198 · [S] https://news.sap.com/2025/10/sap-a-leader-gartner-magic-quadrant-cloud-erp-product-centric-enterprises/
- **ERP como estrategia, no como suite**: Gartner habla de «postmodern ERP» (desde 2013-2014) y ahora de «composable ERP», «a technology strategy that automates and links administrative and operational business capabilities»; ERP «is neither defined as a single integrated suite, nor is it a specific set of modules». Distingue ERP administrativo (finanzas, RR. HH., compras) de operativo (producción, distribución). [S] https://www.netsuite.com/portal/resource/articles/erp/how-does-netsuite-fit-gartners-definition-of-postmodern-erp.shtml · [S] https://www.gartner.com/en/documents/6206787
- **IDC** divide las aplicaciones empresariales en enterprise resource management (ERM), CRM, engineering applications, supply chain management y production applications. [S] https://www.idc.com/resource-center/press-releases/worldwide-enterprise-applications-revenue-grew-12-0-in-2023-and-is-forecast-to-surpass-600-billion-in-2028-according-to-idc/
- **CRM** no es un cuadrante: Gartner lo parte en «Sales Force Automation Platforms» (julio de 2025) y «CRM Customer Engagement Center» (octubre de 2025, suites de atención al cliente), y marketing va por otro lado. [S] https://www.gartner.com/en/documents/6747034 · [S] https://www.cxtoday.com/crm/gartner-magic-quadrant-for-sales-force-automation-platforms-sfa-2025-the-rundown/
- **HCM**: «Cloud HCM Suites for 1,000+ Employee Enterprises», que evalúa Core HR/Benefits, talento antes y después de la contratación, y Payroll Administration. [S] https://www.gartner.com/reviews/market/cloud-hcm-suites-for-1000-employees · [S] https://www.gartner.com/en/documents/6933166
- **SCM**: hay cuadrante de Supply Chain Planning Solutions (abril de 2025); WMS y TMS existen como mercados aparte, pero no se confirmó su edición vigente. [S] https://www.gartner.com/en/documents/6356179
- **MES**: Market Guide de mayo de 2025; la definición citada de Gartner pone al MES a despachar trabajo según instrucciones del ERP o del programador de producción. [S] https://www.gartner.com/en/documents/6420807
- **Field service**: Market Guide de marzo de 2025 («the market is integrating adjacent technologies»); el último Magic Quadrant encontrado es de 2022. [S] https://www.gartner.com/en/documents/6311147
- **BI**: «Analytics and Business Intelligence Platforms» (2025): modelar, analizar y visualizar datos de varias fuentes, con capa semántica. [S] https://www.gartner.com/en/documents/6576602

**Dónde dicen que se pisan**: ERP con MES (el ERP planifica y registra, el MES ejecuta en planta; hay proveedores en los dos cuadrantes), ERP con SCM y con HCM (el ERP «administrativo» incluye RR. HH. y compras), CRM con field service (la atención y el servicio en campo comparten el caso y la orden de trabajo) y field service con gestión de activos (el mantenimiento del equipo del cliente).

### 1.5 Cuerpos de saber propios de cada dominio

- **Cadena de suministro, ASCM**:
  - SCOR Digital Standard, siete procesos: Orchestrate, Plan, Order, Source, Transform, Fulfill, Return (Deliver se partió en Order y Fulfill; Make pasó a Transform). [S] https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/ · [S] https://mhlnews.com/global-supply-chain/article/21251037/ascm-releases-new-scor-digital-standard
  - CSCP 2026, ocho módulos: Supply Chains, Demand Management, and Forecasting; Global Supply Chain Networks; Sourcing Products and Services; Internal Operations and Inventory; Forward and Reverse Logistics; Supply Chain Relationships; Supply Chain Risk; Optimization, Sustainability, and Technology. [L] https://www.ascm.org/globalassets/ascm_website_assets/docs/credentials/2026-cscp-module-content-outline.pdf
  - CLTD 2026, nueve módulos: Logistics Fundamentals and Strategy; Demand Management and Supply (Capacity Management); Customer and Order Management; Warehouse Distribution/Fulfillment Center Management; Inventory Management; Transportation Management; Global Logistics; Sustainability, Reverse Logistics, and Risk Management; Logistics Framework, Metrics, Network Design, Transformation, and Improvement. [L] https://www.ascm.org/globalassets/ascm_website_assets/docs/credentials/2026-cltd-module-content-outline.pdf
- **Producción y planificación, ASCM CPIM**: en la versión 8.0, ocho módulos (estrategia, S&OP, demanda, abastecimiento, programas detallados, inventario, distribución, calidad y mejora continua); la edición 2026 pasa a nueve, con el último «Quality, Business Investments, and Continuous Improvement». El PDF oficial no se pudo bajar. [S] https://www.ascm.org/globalassets/ascm_website_assets/docs/credentials/2026-cpim-module-content-outline.pdf · [S] https://www.coursera.org/articles/cpim
- **Producción en planta, ISA-95**: nivel 4 (planificación del negocio y logística, donde está el ERP) y nivel 3 (gestión de operaciones de manufactura, donde está el MES); la norma trata sobre todo la interfaz entre los dos. [L] https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard. Las categorías de la gestión de operaciones son producción, mantenimiento, calidad e inventario. [S] https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf (el preview nombra «inventory operations management»; la lista de cuatro sale de resúmenes)
- **Compras, CIPS Procurement & Supply Cycle**: 13 etapas, de «Define Business Needs and Develop Specification» y «Market Analysis and Make or Buy Decision» hasta «Contract Award and Implementation», «Warehouse, Logistics and Receipt», «Contract Performance and Improvement», «Supplier Relationship Management» y «Asset Management». [L] https://udntho.files.cmp.optimizely.com/download/assets/CIPS+Procurement+and+Supply+Cycle/b28fefe2aa9e11f0964012001de8781f
- **Personas, SHRM BASK** (antes BoCK): tres dominios, People, Organization y Workplace; en People están HR Strategy, Talent Acquisition, Employee Engagement & Retention, Learning & Development y Total Rewards. [S] https://shrm.org/topics-tools/news/shrm-certification-updates-shrm-body-competency-knowledge
- **Tesorería, AFP CTP**: examen de cinco dominios basado en *The Essentials of Treasury Management* (7.ª ed.); no se confirmaron los nombres vigentes de los dominios. [S] https://ctpcert.afponline.org/overview/ctp-test-specifications
- **Sin cuerpo propio encontrado**: Contabilidad (la ordenan las normas, NIIF/IFRS y las de cada país, no un cuerpo de saber del oficio; no se leyó en esta pasada), Impuestos (es de cada país), Relación con clientes, Servicio al cliente y de campo, y BI fuera de DAMA-DMBOK (que ya cita `Datos/.investigacion/vistazo.md`).

## 2. La tabla: dominio del árbol × cada taxonomía

| Dominio del árbol | APQC PCF (7.2.1) | Odoo | ERPNext | Analistas | Cuerpo propio |
|---|---|---|---|---|---|
| Contabilidad | 9.1 a 9.4, 9.6, 9.8, 9.10 | Accounting and Invoicing, Expenses | Accounts, Assets | Núcleo financiero del ERP «administrativo»; IDC: ERM | Normas contables (no leídas) |
| Tesorería y finanzas | 9.7 (y 9.10) | Dentro de Accounting; Online payments | Dentro de Accounts | Sin categoría propia en esta lista; dentro del ERP | AFP CTP |
| Impuestos | 9.9; 9.11 comercio exterior | Fiscal localizations | Regional; en HRMS, Tax and Benefits | Dentro del ERP | No hay (de cada país) |
| Compras y abastecimiento | 4.2; el pago en 9.6 | Purchase (familia Supply Chain) | Buying, Subcontracting | Parte de SCM | CIPS (13 etapas); SCOR Source; CSCP mód. 3 |
| Inventario y depósitos | 4.4 (junto con logística) | Inventory, Barcode | Stock | WMS (mercado aparte); inventario de planta en MES | CLTD mód. 4 y 5; CPIM inventario; ISA-95 inventario |
| Cadena de suministro y logística | 4.1, 4.4 | «Supply Chain» es la familia que agrupa también compras, producción, calidad y mantenimiento | No hay módulo: Stock + Buying + Selling | SCM; Supply Chain Planning; TMS | SCOR DS (7 procesos); CSCP; CLTD |
| Producción | 4.3; producto en 2.0; planta en 10.0 | Manufacturing, PLM, Quality, Maintenance | Manufacturing, Quality Management, Maintenance, Subcontracting | MES; ERP para empresas de producto; IDC: production apps | ISA-95 (nivel 3 y 4); CPIM; SCOR Transform |
| Relación con clientes | No hay categoría: 3.0 (vender, 3.5.4 pedidos) y 6.0 (atender) | CRM; además Sales, Subscriptions, Rental, Members | CRM (y Selling aparte) | CRM partido en SFA, Customer Engagement Center y marketing | No hay |
| Servicio al cliente y de campo | 6.0 (6.2, 6.3, 6.4); 5.0 si el servicio es el producto | Helpdesk, Field Service (familia Services); Repairs (familia Supply Chain) | Support; Maintenance (visitas) | CRM Customer Engagement Center; Field Service Management (aparte) | No hay |
| Gestión de personas y nómina | 7.0 (7.1 a 7.9); nómina en 9.5 y en 7.5.4 | Familia Human resources (con Fleet, Lunch, Frontdesk) | App aparte HRMS (nueve módulos con Payroll y Tax and Benefits) | HCM (Core HR, talento, Payroll Administration) | SHRM BASK |
| BI (vertical de Datos) | No hay: 9.3 reportes, 7.7 analítica de empleados, 6.5 evaluar la atención, 8.4 información | Reporting en cada app; Dashboards, Spreadsheet | Reportes en cada módulo; no hay módulo | Analytics and BI Platforms | DAMA-DMBOK, área Data Warehousing & BI |
| Procesos de negocio | Fuera del PCF: mapas de punta a punta (order-to-cash, procure-to-pay, record-to-report, hire-to-retire, issue-to-resolution, lead-to-order) | No hay: el proceso cruza apps | No hay: el proceso cruza módulos | No es categoría de mercado | SCOR es de procesos; los mapas de APQC |
| Software de gestión | 8.0 (gestionar TI) | Productivity, Studio, General settings | Setup, Utilities, Portal, Integrations, EDI, Bulk Transaction | ERP de producto y de servicios; composable ERP; IDC: ERM/CRM/SCM | ISA-95 (frontera ERP y MES) |

## 3. Huecos: lo que las taxonomías tienen y el árbol no

1. **Servicios y proyectos.** APQC tiene una categoría operativa entera (5.0 Deliver Services), Odoo una familia (Project, Timesheets, Planning), ERPNext el módulo Projects y Gartner un cuadrante de ERP para empresas de servicios. En el árbol, «Servicio al cliente y de campo» es la posventa (APQC 6.0), no la entrega del servicio que se vende. Es el hueco más grande: el lector principal (quien construye software de gestión) suele ser una empresa de servicios.
2. **Activos y mantenimiento.** APQC 10.0, Maintenance en los dos ERP, Assets en ERPNext, Fleet en Odoo, la etapa 13 del ciclo de CIPS y el mantenimiento de ISA-95. En el árbol queda repartido entre Contabilidad (el activo fijo, 9.4) y Producción (el mantenimiento de planta), y el mantenimiento del equipo del cliente cae en servicio de campo.
3. **Calidad.** Quality en Odoo, Quality Management en ERPNext, una de las cuatro categorías de ISA-95 y el último módulo de CPIM. No es tema: cabe como vertical de Producción, pero los retiros de producto (APQC 6.4) y la calidad de servicio quedan afuera.
4. **Riesgo, cumplimiento y control interno.** APQC 11.0 y 9.8. No aparece en el árbol; una parte va en Contabilidad (control interno) y otra en Impuestos.
5. **Desarrollo de producto físico.** APQC 2.0, PLM en Odoo, «engineering applications» en IDC. `Producto` trata productos digitales; la ingeniería del producto (lista de materiales, cambios de ingeniería) quedaría en Producción.
6. **Comercio exterior.** APQC 9.11 y el módulo de logística global de CLTD. Cae entre Impuestos y Cadena de suministro.
7. **Gastos y rendiciones.** Odoo los pone en Finance y ERPNext en HRMS: entre Contabilidad y Personas.
8. **Lo que no hace falta sumar**: marketing (APQC 3.1 a 3.4, la familia Marketing de Odoo) ya es el tema `Marketing`; punto de venta, sitio y tienda ya están en `Comercio-electronico`; documentos, firma, aprobaciones y personalización son columnas técnicas de Software de gestión.

## 4. Solapes y cortes que no hace nadie afuera

1. **Inventario y depósitos contra Cadena de suministro y logística.** Ninguna fuente los separa como el árbol. APQC junta depósito con logística (4.4); CLTD tiene depósito, inventario y transporte como módulos hermanos de un solo cuerpo; CPIM pone inventario con planificación; Odoo mete todo bajo «Supply Chain». Si quedan como dos temas, el límite lo pone la base y conviene escribirlo en los dos `ALCANCE.md`.
2. **Compras dentro o fuera de la cadena.** SCOR (Source), CSCP (módulo 3) y APQC (4.2, adentro de entregar productos físicos) ponen compras dentro de la cadena de suministro; CIPS lo trata como disciplina propia. El árbol lo separa: es defendible, pero el pago al proveedor (9.6) es contable.
3. **Relación con clientes.** Es el dominio con menos respaldo externo: APQC no tiene esa categoría (reparte entre 3.0 vender y 6.0 atender), los analistas parten el CRM en ventas, atención y marketing, y ERPNext separa CRM de Selling. Choca con tres temas que ya existen o están en el árbol: `Ventas` (el método), `Marketing` y Servicio al cliente. Lo que le queda propio es el registro del cliente y de la oportunidad, y la pregunta de quién es dueño del pedido (APQC 3.5.4 lo pone en vender, SCOR en Order, CLTD en Customer and Order Management).
4. **Nómina.** APQC la pone dos veces (9.5 Process payroll en finanzas y 7.5.4 Administer payroll en personas); ERPNext la trae con impuestos sobre sueldos (Tax and Benefits). El árbol la pone en Personas: hace falta enlazarla con Contabilidad e Impuestos.
5. **Servicio al cliente con servicio de campo.** Los analistas los tienen en mercados distintos (Customer Engagement Center contra Field Service Management) y Odoo los pone juntos en Services, pero las reparaciones en Supply Chain. Servicio de campo se pisa además con activos y mantenimiento (hueco 2). Responde en parte la pregunta abierta de #94 sobre su tamaño: solo no tiene cuerpo propio de saber, pero con mantenimiento y reparaciones sí arma un dominio.
6. **Producción con Cadena de suministro.** SCOR (Plan, Transform) y CPIM ponen la planificación de producción (S&OP, MRP, programas) dentro de la cadena; ISA-95 pone la planificación en el nivel 4 y la ejecución en el 3. Hay que decidir de qué lado queda la planificación.
7. **BI con `Datos/Visualizacion-y-BI`.** La vertical ya existe (capa semántica, tablero, herramientas de BI). Lo que piden las fuentes de gestión es otra cosa: los reportes de cada dominio (cierre contable, rotación de inventario, nivel de servicio). Eso va en cada dominio, y la vertical de Datos se amplía con lo común (el depósito de datos sobre el software de gestión).
8. **Personas con `Liderazgo-y-direccion/Gestion-de-personas`.** Esa vertical ya trata contratar, incorporar, evaluar, compensar y desvincular, o sea, buena parte de APQC 7.0 y del dominio People de SHRM. El tema nuevo tendría que quedarse con la administración (legajo, asistencia, licencias, nómina) y enlazar lo otro.
9. **Software de gestión.** Las fuentes respaldan que sea un tema aparte: Gartner dice que ERP no es un conjunto fijo de módulos, ISA-95 marca la frontera entre ERP y MES, y la comparación de Odoo con ERPNext muestra que cada producto agrupa distinto (Odoo pone Fleet en personas y Repairs en cadena; ERPNext saca personas a otra app).

## 5. Lo que no se pudo leer

- El PCF 7.4 y 8.0 de APQC (403): los números de nivel 2 son de la 7.2.1, por una copia de terceros.
- Las definiciones de mercado de Gartner (glosario y cuadrantes): solo resúmenes.
- El PDF oficial de CPIM 2026 (devuelve HTML), los dominios vigentes del CTP de AFP y el texto de ISA-95 con sus cuatro categorías.
- Un cuerpo de saber para Relación con clientes, Servicio al cliente y de campo, y Contabilidad como oficio; no se buscó a fondo para Contabilidad e Impuestos (normas de cada país).
