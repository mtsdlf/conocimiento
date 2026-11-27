# Marcos de procesos: informe de investigación

Para la nota `Procesos-de-negocio/Fundamentos/marcos-de-procesos.md`. Fecha de todas las lecturas: 2026-11-27. Marcas: [L] texto completo leído, [M] metadatos, índice o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U).

Insumos previos: la investigación de la rama `research/taxonomias-externas` (`.investigacion-software-de-gestion/taxonomias-externas.md`, que usó la 7.2.1 por una copia de terceros) y los issues #96 y #99. La decisión de #99: los marcos se citan, sin vertical; una nota de Fundamentos explica marco frente a proceso de punta a punta y a qué dominio va cada marco; cada nota de proceso cita sus códigos APQC en una línea.

## Tabla de fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| APQC, Process Classification Framework, Cross-Industry, PDF versión 7.4 (agosto de 2024), copia de la IFRC | primaria | 3/3/2/3 | [L] entero, pasado a texto (`pdftotext -layout`) | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf |
| APQC, PCF Business Rules (sin fecha; la imagen embebida es de 2016) | primaria | 3/2/1/3 | [L] | https://www.apqc.org/sites/default/files/files/PCF%20Collateral/PCF%20Business%20Rules.pdf |
| APQC, Understanding the Elements of APQC's Process Classification Framework | primaria | 3/2/2/2 | [L] | https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Understanding%20the%20PCF%20Elements%20%20-%20FINAL.pdf |
| Madison Lundquist (APQC), Why are end-to-end processes important?, 15 de enero de 2024 | primaria | 3/1/2/3 | [L] (por WebFetch) | https://www.apqc.org/blog/why-are-end-end-processes-important |
| APQC, página del PCF 8.0 (PDF y Excel, 27 de febrero de 2026) y colección de definiciones 8.0 (24 de marzo de 2026) | primaria | 3/1/1/2 | [S] (buscador; la página da 403) | https://www.apqc.org/pcf-pdf |
| APQC, colección End-to-End Process Maps and Measures (procure-to-pay, S&OP; actualizada en noviembre de 2025) | primaria | 3/1/1/2 | [S] (403) | https://www.apqc.org/resource-library/resource-collection/end-end-process-maps-and-measures |
| ITU-T, Recomendación M.3050.1 (03/2007), resumen y tabla de contenidos | primaria | 3/1/1/3 | [L] resumen e índice | https://www.itu.int/dms_pubrec/itu-t/rec/m/T-REC-M.3050.1-200703-I!!SUM-HTM-E.htm |
| Wikipedia, Business Process Framework (eTOM) | secundaria | 1/2/1/2 | [L] | https://en.wikipedia.org/wiki/Business_Process_Framework_(eTOM) |
| TM Forum, páginas de eTOM (ODA, MODA) | primaria | — | no leídas: 403 | https://www.tmforum.org/oda/business/process-framework-etom/ |
| Notas de la base: marcos de la cadena, marcos de la producción, fundamentos de compras, de administración de personal, de tesorería, de servicio al cliente, de activos | base | — | [L] | rutas en la sección 6 |

## 1. Marco funcional frente a proceso de punta a punta

- El PCF se declara funcional: «The PCF reflects a functional view of an organization, rather than a cross-functional view. It serves many purposes for organizations including: facilitating benchmarking, aiding in process definition and governance, and forming the structure of a content management or knowledge management taxonomy for the organization.» [L] Business Rules.
- Descomposición funcional y MECE: «The PCF begins by identifying the major functional categories of an organization. Following the MECE principle [...] these categories should collectively describe all of the work done at an organization and should not overlap each other.» [L] Business Rules, regla 3.
- No dice el orden: «The PCF is intended to identify the complete collection of what happens at each part of the organization, not the order in which these things happen or the dependency between these elements. Exception flows should also be included.» (regla 3) y «The order of process elements within a hierarchy does not imply execution order; merely the scope of the parent process element.» (regla 4). [L] Business Rules.
- Mismo punto en el documento de elementos, con título propio: «Key Concept: The PCF Does Not Imply Order». [L] Understanding the Elements.
- Formato verbo-sustantivo: «All items in the PCF begin with a verb describing the process, activity, etc.» [L] Business Rules, regla 1.
- Versiones de industria: «There are also industry specific "offspring" of the PCF. Industry-specific frameworks generally address functions or processes that are materially different or absent from the cross-industry framework.» [L] Business Rules.
- **Contradicción a declarar**: la portada del PCF 7.4 dice que el PCF «is a taxonomy of cross-functional business processes intended to allow the objective comparison of organizational performance within and among organizations» [L] PCF 7.4, p. 1. Las Business Rules dicen lo contrario («functional view [...] rather than a cross-functional view»). Lectura de la base: la estructura (categorías por función, regla MECE, sin orden) es funcional; «cross-functional» en la portada parece describir el alcance (toda la empresa), no un orden de punta a punta. Es inferencia.
- Proceso de punta a punta según APQC: «cross-functional processes that comprise all the steps to accomplish a specific outcome or goal». Ejemplos: order-to-cash, hire-to-retire, idea-to-market (y un ejemplo de restaurante, «Arrive-to-Leave»). El PCF funciona como «ingredient list»; para order-to-cash marca las categorías 3.0, 4.0 y 9.0 y cita 3.5.4.1 «Accept and validate sales order (Take orders)» y 3.5.4.3 «Determine availability (Check availability)». [L] Lundquist 2024. (Ojo: en el blog el nombre de 3.5.4.1 está en singular, «sales order»; en el PCF 7.4 es «Accept and validate sales orders».)
- Mapas de punta a punta que publica APQC: procure-to-pay (Visio y Excel), S&OP; la investigación previa lista además record-to-report, order-to-cash, hire-to-retire, issue-to-resolution y lead-to-order. [S] buscador y taxonomias-externas.md. No se encontraron mapas de APQC de project-to-cash, plan-to-produce ni acquire-to-retire (búsqueda en apqc.org, 2026-11-27, [S]). La nota de del-proyecto-al-cobro (otra sesión) dice lo mismo para proyectos.
- El PCF mismo tiene un proceso para identificar los recorridos: 13.1.2.2 «Identify cross-functional processes» (16386), dentro de 13.1 «Manage business processes» (16378); y 13.1.1.3 «Assign and support process ownership» (16382). [L] PCF 7.4, p. 31.

## 2. Las 13 categorías del PCF 7.4 (literal)

Del índice y de los títulos del cuerpo [L] PCF 7.4, pp. 1-2 y 4-31:

| Código | Nombre en el índice | Grupo |
|---|---|---|
| 1.0 | Develop Vision and Strategy | Operating processes |
| 2.0 | Develop and Manage Products and Services | Operating processes |
| 3.0 | Market and Sell Products and Services | Operating processes |
| 4.0 | Manage Supply Chain for Physical Products | Operating processes |
| 5.0 | Deliver Services (en el título del cuerpo: «Deliver Service (20025)») | Operating processes |
| 6.0 | Manage Customer Service | Operating processes |
| 7.0 | Develop and Manage Human Capital | Management and support services |
| 8.0 | Manage Information Technology (IT) | Management and support services |
| 9.0 | Manage Financial Resources | Management and support services |
| 10.0 | Acquire, Construct, and Manage Assets | Management and support services |
| 11.0 | Manage Enterprise Risk, Compliance, Remediation, and Resiliency | Management and support services |
| 12.0 | Manage External Relationships | Management and support services |
| 13.0 | Develop and Manage Business Capabilities | Management and support services |

- Los nombres cambian entre versiones: el documento «Understanding the Elements» (sin versión) llama a 4.0 «Deliver Physical Products», igual que la 7.2.1 de la investigación previa; la 7.4 dice «Manage Supply Chain for Physical Products». [L]
- Portada: «The PCF organizes operating and management processes into 13 enterprise-level categories, including process groups and more than 1,000 processes and associated activities.» Historia: «Since its inception in 1992». [L] PCF 7.4, p. 1.

## 3. Niveles y numeración

- «These 13 Categories break down into increasingly granular levels: Level 2—Process group [...], Level 3—Process: a single process, Level 4—Activity: a key step performed to execute a process, and Level 5—Task: an element of work that goes into executing an activity.» Ejemplos: grupo 1.1, proceso 1.1.1, actividad 1.1.1.1. [L] Understanding the Elements.
- «Categories are parent to process groups, process groups are parent to processes, processes are parent to activities, and activities are parent to tasks.» [L] Business Rules.
- Dos números por elemento. El jerárquico: «The numbers are specific to a particular release and are not comparable across version numbers of the PCF. [...] These numbers will change across releases.» El de cinco dígitos: «a machine readable index number that is used to maintain control of the definition of the element»; APQC reserva 95000-99999 para que cada usuario agregue los suyos. [L] Business Rules, regla 6. En el PCF 7.4: «This number will always refer to the conceptual definition of the process element [...] A new 5-digit number will be assigned to a process element if its definition substantially changes.» [L] PCF 7.4, p. 3.
- Versiones: «major, minor, release»; «Major releases typically occur when category-level changes are made. Minor releases typically occur when process-level changes are made.» [L] Business Rules.
- Consecuencia (inferencia de la base): un sistema que guarde códigos APQC tiene que guardar la versión y el identificador de cinco dígitos, porque el número jerárquico no sobrevive a una versión nueva.

## 4. Versión

- 7.4: «Version 7.4 • August 2024» [L] PCF 7.4, p. 1.
- 8.0: PDF y Excel publicados el 27 de febrero de 2026; definiciones y medidas 8.0 actualizadas el 24 de marzo de 2026. [S] buscador sobre apqc.org (403). No se pudo leer: los códigos de la nota son de la 7.4 y pueden cambiar en la 8.0.
- Otros temas de la base usan la 7.2.1 (Administración de personal, Contabilidad) y dicen que la 7.4 no se pudo leer. La 7.4 sí se leyó (copia de la IFRC). Ver sección 7.

## 5. Códigos de cada recorrido (PCF 7.4, literal)

Todos [L] PCF 7.4. Entre paréntesis, el identificador de cinco dígitos cuando se usó. La elección de qué piezas entran en cada recorrido es de la base.

### Del pedido al cobro (order-to-cash)
- 3.5.4 Manage sales orders (10185): 3.5.4.1 Accept and validate sales orders (10194); 3.5.4.3 Determine availability (10196); 3.5.4.4 Determine fulfillment process (10197); 3.5.4.5 Process back orders and updates (10199). p. 10.
- 4.1.2.4 Determine available to promise (10238). p. 11.
- 4.4.3.4 Pick, pack, and ship product for delivery (10356). p. 12.
- 4.4.4.1 Plan, transport, and deliver outbound product (10360). p. 12.
- 9.2 Perform revenue accounting (10729): 9.2.1 Process customer credit (10742); 9.2.2 Invoice customer (10743); 9.2.3 Process accounts receivable (AR) (10744), con 9.2.3.3 Apply cash remittances (10801); 9.2.4 Manage and process collections (10745); 9.2.5 Manage and process adjustments/deductions (10746). p. 23.
- 9.7.2 Manage cash (10759), 9.7.2.1 Manage and reconcile cash positions (10893). p. 25.
- Observación: el crédito, la factura, la cuenta a cobrar y la cobranza están en 9.2 (contabilidad de ingresos), no en 9.7 (tesorería). Lo mismo dice `Tesoreria/Fundamentos/fundamentos-de-tesoreria.md`.

### De la compra al pago (procure-to-pay)
- 4.2.3 Order materials and services (10279): 4.2.3.1 Process/Review requisitions; .2 Approve requisitions; .3 Solicit supplier quotes; .4 Create/Distribute purchase orders; .5 Expedite orders and satisfy inquiries; .6 Reconcile purchase orders; .7 Research/Resolve order exceptions. p. 11.
- 4.2.4.4 Monitor quality of product delivered (10302). p. 12. (La calidad como paso, decisión de #99.)
- 4.4.2.1 Plan inbound material receipts (10349); 4.4.3.2 Receive, inspect, and store inbound deliveries (10354). p. 12.
- 9.6.1 Process accounts payable (AP) (10756): 9.6.1.1 Verify AP pay file with purchase order vendor master file; 9.6.1.3 Audit invoices and key data in AP system; 9.6.1.4 Approve payments; 9.6.1.7 Research/Resolve payable exceptions; 9.6.1.8 Process payments. p. 24.
- 9.7.2.3 Process and oversee electronic fund transfers (EFTs) (10895). p. 25.
- Observación: el PCF no nombra el cruce de tres vías; lo más cercano es 9.6.1.3 y 4.2.3.6.

### Del registro al balance (record-to-report)
- 9.3 Perform general accounting and reporting (10730): 9.3.1 Manage financial policies and procedures (10747); 9.3.2 Perform general accounting (10748), con 9.3.2.2 Process journal entries, 9.3.2.4 Process period end adjustments, 9.3.2.5 Post and reconcile intercompany transactions, 9.3.2.6 Reconcile general ledger accounts, 9.3.2.7 Perform consolidations and process eliminations, 9.3.2.8 Prepare trial balance; 9.3.4 Perform financial reporting (10750). pp. 23-24.
- 9.1.2.1 Perform inventory accounting (10774). p. 23.
- 9.7.2.1 Manage and reconcile cash positions (10893). p. 25.
- 9.8 Manage internal controls (10735). p. 26.
- 9.9.2 Process taxes (10766). p. 26.
- 9.10 Manage international funds/consolidation (10737). p. 26.
- Observación: los ajustes de cierre están repartidos: 9.3.2.4, 9.5.2.7 Process period-end adjustments (nómina) y 9.6.1.5 Process financial accruals and reversals (cuentas a pagar).

### De la planificación a la producción (plan-to-produce)
- 4.1.2 Manage demand for products (10222); 4.1.3 Create materials plan (10223); 4.1.4 Create and manage master production schedule (10224). p. 11.
- 4.2.3 Order materials and services (10279). p. 11.
- 4.3 Produce/Assemble/Test product (10217): 4.3.1 Schedule production; 4.3.2 Produce/Assemble product; 4.3.3 Perform quality testing; 4.3.4 Maintain production records and manage lot traceability. p. 12.
- 4.4.3.7 Manage physical finished goods inventory (10359). p. 12.
- 9.1.2.4 Perform product costing (10776); 9.1.2.5 Perform variance analysis (10777). p. 23.
- Detalle por subproceso en `Produccion/Fundamentos/marcos-de-la-produccion.md`.

### De la contratación a la baja (hire-to-retire)
- 7.2 Recruit, source, and select employees (10410): 7.2.1 Manage employee requisitions (10439); 7.2.4 Manage new hire/re-hire (10443), con 7.2.4.3 Hire candidate. p. 16.
- 7.3.1 Manage employee orientation and deployment (10469). p. 16.
- 7.5.2 Manage and administer benefits (10495); 7.5.4 Administer payroll (10497). p. 17.
- 7.6 Redeploy and retire employees (10413): 7.6.2 Manage separation (10513); 7.6.3 Manage retirement (10514); 7.6.4 Manage leave of absence (10515). p. 17.
- 7.7.3 Manage and maintain employee data (10524). p. 17.
- 9.5 Process payroll (10732): 9.5.1 Report time (10753); 9.5.2 Manage pay (10754); 9.5.3 Manage and process payroll taxes (10755). p. 24.
- Observación: la nómina aparece dos veces (7.5.4 y 9.5), como ya dice `Administracion-de-personal-y-nomina/Fundamentos/fundamentos-de-administracion-de-personal.md` con la 7.2.1; en la 7.4 sigue igual.

### Del reclamo a la resolución (issue-to-resolution)
- 6.2.2 Manage customer service problems, requests, and inquiries (10388); 6.2.3 Manage customer complaints (10389); 6.2.4 Process returns (20094), con 6.2.4.1 Authorize return y 6.2.4.2 Process return and record reason. p. 14.
- 6.3.2 Process warranty claims (12669), con 6.3.2.3.4 Investigate issue/perform root cause analysis; 6.3.4 Service products (10218), con 6.3.4.3.2 Execute product repair. p. 14.
- 6.5.2 Measure customer satisfaction with customer-complaint handling and resolution (10402). p. 15.
- 4.4.2.4 Manage flow of returned products (10352); 4.4.2.5 Manage disposition of returned products (20109). p. 12.
- 4.3.3.5 Track and analyze non-conformance trends; 4.3.3.6 Perform root cause analysis. p. 12.
- 9.2.2.5 Resolve customer billing inquiries (10798); 9.2.5 Manage and process adjustments/deductions (10746). p. 23.
- Observación: el PCF no nombra la nota de crédito.

### Del proyecto al cobro (project-to-cash)
- 5.2.2 Create and manage resource plan (20050), con 5.2.2.3 Match resource demand with capacity, skills, and capabilities. p. 13.
- 5.3 Deliver service to customer (20058): 5.3.1 Initiate service delivery (20059); 5.3.2 Execute service delivery (20069), con 5.3.2.4 Identify changes; 5.3.3 Complete service delivery (20077), con 5.3.3.2 Complete/finalize financial management activities. p. 13.
- 9.5.1 Report time (10753), con 9.5.1.2 Collect and record employee time worked y 9.5.1.5 Analyze and report employee utilization. p. 24.
- 9.6.2 Process expense reimbursements (10757). p. 24.
- 9.2.2 Invoice customer; 9.2.3 Process accounts receivable (AR); 9.2.4 Manage and process collections. p. 23.
- 9.1.4.1 Assess customer and product profitability (10782). p. 23.
- Observación: el PCF no tiene un paso de facturar horas o hitos dentro de 5.0; la hora está en nómina (9.5.1).

### De la compra a la baja del activo (acquire-to-retire)
- 9.4.1 Perform capital planning and project approval (10751), con 9.4.1.3 Review and approve capital projects and fixed-asset acquisitions (10846); 9.4.2 Perform capital project accounting (10752). p. 24.
- 10.1.1.3 Determine build, buy, or lease decision (10957). p. 27.
- 4.2.3 Order materials and services (10279). p. 11.
- 9.3.3 Perform fixed-asset accounting (10749): 9.3.3.3 Process and record fixed-asset additions and retires; 9.3.3.5 Process and record fixed-asset maintenance and repair expenses; 9.3.3.6 Calculate and record depreciation expense; 9.3.3.8 Track fixed-assets including physical inventory. pp. 23-24.
- 10.3 Maintain assets (19238): 10.3.1 Plan asset maintenance; 10.3.2 Manage asset maintenance; 10.3.3 Perform asset maintenance. p. 27.
- 10.4 Manage asset end-of-life (21576): 10.4.1 Develop exit strategy; 10.4.2 «Decomission productive assets» (así, con una m, en el original); 10.4.3 Perform sale or trade. p. 27.

## 6. Marcos de un solo dominio y dónde ya están en la base

| Marco | Dónde se explica | Anclas comprobadas |
|---|---|---|
| SCOR (ASCM), v13 leída; versión de siete procesos solo por secundaria | `Cadena-de-suministro-y-logistica/Fundamentos/marcos-de-la-cadena-de-suministro.md` | `#scor-qué-versión-se-leyó` |
| ISA-95 / IEC 62264 | `Produccion/Fundamentos/marcos-de-la-produccion.md` | `#isa-95-cinco-niveles-y-la-frontera-entre-erp-y-mes` |
| CIPS, ciclo de 13 pasos | `Compras-y-abastecimiento/Fundamentos/fundamentos-de-compras-y-abastecimiento.md` | `#cómo-dividen-el-dominio-cips-apqc-y-esta-base` |
| SHRM BASK 2026 | `Administracion-de-personal-y-nomina/Fundamentos/fundamentos-de-administracion-de-personal.md` | `#cómo-dividen-el-dominio-los-marcos-y-los-productos` |
| ISO 10002, ISO 18295-1, ITIL 4 | `Servicio-al-cliente/Fundamentos/fundamentos-de-servicio-al-cliente.md` | `#cómo-se-divide-el-campo-a-sí-mismo` |
| ISO 55000 (gestión de activos; no es un marco de procesos) | `Activos-y-mantenimiento/Fundamentos/fundamentos-de-activos-y-mantenimiento.md` | `#tres-enfoques-en-tres-planos-distintos` |
| APQC 9.7 frente a 9.2 y 9.6 (tesorería) | `Tesoreria/Fundamentos/fundamentos-de-tesoreria.md` | `#cómo-se-divide-el-campo` |

### eTOM

- ITU-T M.3050.1 (03/2007), resumen: el eTOM «describes the enterprise processes required by a service provider», es «a reference framework for categorizing the business activities that a service provider will use» y los «analyses [...] to different levels of detail according to their significance and priority for the business». Está «built on the concepts of management services and functions». Lo desarrolló el TeleManagement Forum y la UIT lo publica como serie M.3050.x. [L] resumen.
- Índice de M.3050.1: capítulos «The eTOM business process framework» (6.1 «Core eTOM single enterprise viewpoint»), «The emergence of e-business within the ICT market» y anexo A.3 «End-to-end process flow concepts». [L] índice.
- Wikipedia: «an operating model framework for telecom service providers in the telecommunications industry»; mantenido por TM Forum, «an association for service providers and their suppliers in the telecommunications and entertainment industries». Tres áreas: «Strategy, Infrastructure & Product», «Operations» y «Enterprise Management». En Operations, columnas «Operations Support & Readiness, Fulfillment, Assurance and Billing» y filas «Relationship Management, Service Management & Operations, Resource Management & Operations and Supplier/Partner Relationship Management». Última versión citada: R23. [L] Wikipedia (secundaria).
- Las páginas de TM Forum dan 403; la estructura en filas y columnas queda por secundaria.
- Lectura de la base: eTOM cruza filas (por qué se gestiona: cliente, servicio, recurso, proveedor) con columnas (qué se logra: cumplir, asegurar, facturar), así que sus columnas se parecen más a recorridos que las categorías del PCF. Es inferencia; no se leyó el texto de TM Forum.

## 7. Problemas encontrados en los temas de dominio (sin editar)

- `Administracion-de-personal-y-nomina/Fundamentos/fundamentos-de-administracion-de-personal.md:62` y `:67` citan el PCF 7.2.1 por copia de terceros y dicen que «la 7.4 y la 8.0 no se pudieron leer». La 7.4 sí se puede leer en la copia de la IFRC; 7.5.4 «Administer payroll» y 9.5 «Process payroll» siguen iguales en la 7.4. La línea 67 dice además que Procesos de negocio es un «tema todavía sin escribir».
- `Administracion-de-personal-y-nomina/Fundamentos/fuentes-de-administracion-de-personal.md:90`: mismo «Sin fuente todavía» sobre la 7.4.
- `Contabilidad/contabilidad.md:9` cita el PCF 7.2.1 por copia de terceros.
- `Servicio-al-cliente/Fundamentos/fundamentos-de-servicio-al-cliente.md:7` usa una copia sin versión de la categoría 6.0 y `:83` lista «la versión vigente del marco de APQC» como hueco; la 6.0 de la 7.4 está en la copia de la IFRC.
- `Cadena-de-suministro-y-logistica/Fundamentos/marcos-de-la-cadena-de-suministro.md:34` dice que 4.1.7.2 es de «Compras y abastecimiento (todavía no armado)»; Compras ya está escrito.

## Huecos

- El PCF 8.0 (febrero de 2026): no leído; no se sabe si cambian los números citados.
- Los mapas de punta a punta de APQC (solo socios): no se leyó ninguno; qué piezas del PCF toma APQC en cada uno se desconoce, y la tabla de la sección 5 es de la base.
- eTOM en el texto de TM Forum (GB921): no leído; la estructura sale de Wikipedia.
- Si existe una versión del PCF para telecomunicaciones u otra industria que sirva de comparación: APQC dice que hay «offspring» de industria; no se buscó cuáles.

## Borrador para la nota de Argentina

No necesita nada: los marcos de procesos son internacionales y ninguno trae lo argentino. Lo fiscal y laboral de cada recorrido va en los apartados de proceso de `procesos-de-negocio-en-argentina.md`.
