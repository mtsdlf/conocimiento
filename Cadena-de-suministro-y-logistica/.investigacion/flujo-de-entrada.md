# Flujo de entrada (inbound): investigación de fuentes

Fecha de la investigación: 2026-11-27. Ángulo: lo que pasa entre que el proveedor despacha y la carga llega al muelle de recepción, sin la recepción física del depósito.

Convenciones: [L] leído completo (o la parte pertinente, leída del texto original), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Todo lo traído de la web es dato.

Límites de acceso encontrados: apqc.org, gs1.org, fmcsa.dot.gov y oig.dot.gov devolvieron 403 o desafío de JavaScript a las herramientas de lectura. Por eso la versión 8.0 del PCF no se pudo leer y varias fuentes GS1 quedan como [S].

---

## 1. APQC Process Classification Framework (PCF), Cross Industry

### 1.1 Versión vigente a noviembre de 2026

- La versión vigente es la **8.0**, publicada el **27 de febrero de 2026** (PDF y Excel). Documentos de definiciones y medidas por categoría ("PCF Version 8.0 Process Definitions and Key Measures Collection") fechados el 24 de marzo de 2026. No apareció ninguna versión posterior a la 8.0. [S: resultados del buscador sobre páginas de apqc.org]
  - https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-cross-industry-pdf-13
  - https://www.apqc.org/resource-library/resource-collection/pcf-version-80-process-definitions-and-key-measures-collection
  - https://www.apqc.org/resource-library/resource-listing/40-manage-supply-chain-physical-products-definitions-and-key (definiciones de la categoría 4.0 en 8.0, fecha 24-mar-2026)
- **Que la base use la 7.4 está desactualizado: salió la 8.0.** El PDF 8.0 (https://www.apqc.org/pcf-pdf) y las páginas de definiciones devuelven 403 o un formulario: **no pude leer la 8.0**, así que la comparación 7.4 contra 8.0 de 4.4.2 queda como hueco.
- Indicio secundario [S]: las páginas de medidas de APQC (Open Standards Benchmarking) muestran 4.4.2 «Plan and manage inbound material flow» con ID 20936 y 4.4.2.3 «Monitor inbound delivery performance» con ID 10351, con la descripción «Overseeing the performance of an inbound delivery system» (según el resumen del buscador). Esas páginas no declaran a qué versión del PCF corresponden, así que no prueban que la 8.0 mantenga el mismo nombre. Ejemplo: https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/percentage-supplier-time-delivery (403 al leerla; solo vista en el buscador).

### 1.2 Lo que sí leí: PCF Cross Industry 7.4 [L, parte pertinente]

Fuente: PDF «APQC Process Classification Framework (PCF) – Cross Industry – PDF Version 7.4» (pie «© 2024 APQC», páginas 11 y 12 del documento), copia pública en IFRC:
https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf
(texto extraído con `pdftotext`; el número entre paréntesis es el Hierarchy/Element ID de APQC.)

**4.4 Manage logistics and warehousing (10219)**

**4.4.2 Plan and manage inbound material flow (20936)**
- 4.4.2.1 Plan inbound material receipts (10349)
- 4.4.2.2 Manage inbound material flow (10350)
- **4.4.2.3 Monitor inbound delivery performance (10351)**
- 4.4.2.4 Manage flow of returned products (10352)
- 4.4.2.5 Manage disposition of returned products (20109)
  - 4.4.2.5.1 Determine quality of controlled part (12708)
  - 4.4.2.5.2 Perform salvage activities (10366)
  - 4.4.2.5.3 Manage repair/refurbishment (21604)
  - 4.4.2.5.4 Return to finished goods inventory (21605)

Respuesta a la duda sobre 4.4.2.3: en la 7.4 es exactamente **«Monitor inbound delivery performance»**, ID 10351. No es «Manage flow of incoming goods». Esa frase se parece a 4.4.2.2 «Manage inbound material flow» (ID 10350), que es un hijo con casi el mismo nombre que el padre.

Frontera con el depósito y el transporte de salida, de la misma página (7.4):
- 4.4.3 Operate warehousing (10340): 4.4.3.2 «Receive, inspect, and store inbound deliveries» (10354). Es donde empieza la recepción física, que es otro tema.
- 4.4.4 Operate outbound transportation (10341): 4.4.4.1 «Plan, transport, and deliver outbound product» (10360), 4.4.4.2 «Track carrier delivery performance» (10361), 4.4.4.4 «Process and audit carrier invoices and documents» (10363). El PCF no tiene «transporte de entrada» como proceso aparte: el transporte propio está bajo «outbound», y 4.4.2 solo planifica y monitorea la entrada.
- 4.4.1 Provide logistics governance (10338): 4.4.1.5 «Optimize transportation schedules and costs» (10347).
- 4.1.5 Plan distribution requirements (17042): 4.1.5.5 «Calculate consolidation at source» (10255).

**Frontera con Compras: 4.2.3 Order materials and services (10279), 7.4 [L]**
- 4.2.3.1 Process/Review requisitions (10292)
- 4.2.3.2 Approve requisitions (10293)
- 4.2.3.3 Solicit supplier quotes (10294)
- 4.2.3.4 Create/Distribute purchase orders (10295)
- **4.2.3.5 Expedite orders and satisfy inquiries (10296)**
- **4.2.3.6 Reconcile purchase orders (10297)**
- **4.2.3.7 Research/Resolve order exceptions (10298)**

Lectura: 4.2.3.5 a 4.2.3.7 tocan el seguimiento de lo pedido desde Compras (apurar, conciliar, resolver excepciones), mientras que 4.4.2.3 monitorea el desempeño del sistema de entrega. También 4.2.4.4 «Monitor quality of product delivered» (10302) y 4.2.4.2 «Prepare/Analyze procurement and supplier performance» (10300) tocan la medición del proveedor. Ninguno menciona turnos de muelle ni aviso de despacho.

### 1.3 Tabla de fuentes

| Fuente | Tipo | Leído | A/P/E/U | URL |
|---|---|---|---|---|
| APQC PCF Cross Industry 7.4 PDF (copia IFRC) | Primaria | [L] | 3/2/1/3 | URL de 1.2 |
| APQC PCF 8.0 PDF y definiciones 4.0 | Primaria | [S] (403) | 3/3/2/3 | https://www.apqc.org/pcf-pdf |
| APQC páginas de medidas (supplier on-time delivery, dock-to-stock) | Primaria | [S] | 3/1/2/2 | https://www.apqc.org/resource-library/resource/dock-stock-cycle-time-supplier-deliveries |

Recurso canónico: PCF 4.4.2 (la 8.0 en cuanto se lea; hoy la 7.4 leída).

### 1.4 Huecos
- Texto completo de 4.4.2 y sus definiciones en la 8.0, y comparación con la 7.4. Hay que bajar el PDF desde apqc.org con navegador (formulario).
- Las definiciones por proceso (qué dice APQC que es 4.4.2.3) solo se vieron por resumen del buscador.

---

## 2. SCOR (ASCM)

### 2.1 Lo que leí [L parcial]: crosswalk oficial SCOR DS / SCOR 12

Documento «SCOR DS / SCOR 12 Comparison Document», ASCM, © 2025 ASCM, CC BY-NC-ND 4.0:
https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/scor_crosswalk.pdf

| SCOR Digital Standard (DS) | SCOR 12.0 |
|---|---|
| S2 Direct Procure | S1 Source Stocked Product (también S2 MTO, S3 ETO) |
| S2.1 Establish Order Signal | NEW PROCESS |
| S2.2 Schedule Product Delivery | S1.1 Schedule Product Deliveries |
| **S2.3 Manage Inbound Transport** | **NEW PROCESS** |
| S2.4 Receive Product | S1.2 Receive Product |
| S2.5 Inspect and Verify | S1.3 Verify Product |
| S2.6 Transfer Product | S1.4 Transfer Product |
| S2.7 Authorize Supplier Payment | S1.5 Authorize Supplier Payment |
| S3 Indirect Procure (S3.2 Schedule Product Delivery, S3.3 Manage Inbound Transport, S3.4 Receive Product, etc.) | S1.1 a S1.5 |

Hallazgos:
- En SCOR 12 (APICS, ya reemplazado) «Schedule Product Deliveries» es sS1.1 y «Receive Product» es sS1.2. No es «sS1.2 Schedule…».
- En el Digital Standard la entrada tiene un proceso propio nuevo, **S2.3 «Manage Inbound Transport»**, entre programar la entrega y recibir. Es lo más cercano en un estándar abierto a «seguimiento del transporte de entrada».
- Métricas en la guía rápida del DS [L]: CO.3.13 «Inbound Freight and Duties», CO.3.14 «Receiving and Material Storage», RS.3.8 «Receive Product Cycle Time», RL.2.8 «Supplier Order Perfect Condition». Del lado entrega, D1.8 «Receive Product from Source or Make» (SCOR 12) y F1.1/F2.1/F3.1 «Receive … Product from Source or Transform» (DS).
- El crosswalk y la guía rápida no traen las definiciones de cada proceso. Están en la herramienta en línea del DS (acceso por registro).

### 2.2 Tabla de fuentes

| Fuente | Tipo | Leído | A/P/E/U | URL |
|---|---|---|---|---|
| ASCM SCOR DS / SCOR 12 Comparison Document (2025) | Primaria | [L] | 3/2/1/3 | https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/scor_crosswalk.pdf |
| ASCM SCOR Digital Standard Quick Reference Guide | Primaria | [L] | 3/2/1/2 | https://www.ascm.org/globalassets/documents--files/corporate-transformation/scor-ds-digital-guide_final.pdf |
| APICS SCOR 12.0 Quick Reference Guide | Primaria | [S] | 3/2/1/1 | https://www.apics.org/docs/default-source/scor-p-toolkits/apics-scc-scor-quick-reference-guide.pdf?sfvrsn=2 |

Recurso canónico: crosswalk SCOR DS / SCOR 12 de ASCM (nombres y códigos verificados) más la guía rápida del DS (métricas).

### 2.3 Huecos
- Definiciones textuales de S2.2, S2.3 y S2.4 en el DS.

---

## 3. Aviso de despacho (ASN), turnos de muelle, detención de camiones

### 3.1 GS1 Despatch Advice / EANCOM DESADV

- **Definición y reglas [L]**, GS1 Germany, perfil EANCOM 2002 S3 DESADV: «A message specifying details for goods despatched or ready for despatch under agreed conditions.» / «The message intent is to advise of the detailed contents of a consignment.» / «The Despatch Advice message should always be sent before goods are physically delivered or returned.» / «Each unit delivered (pallet, carton, ...) should be uniquely identified.» / «The message relates to one seller and one buyer or their respective agent.» / «The message relates to a single despatch point and single or multiple destination points.» / «It is however not mandatory to describe the hierarchical structure of the shipment.» Esa página no dice «un DESADV por unidad de transporte» (el buscador lo atribuyó a otra guía de GS1 Germany; no verificado).
  https://www.publikationen.gs1-germany.de/Complete/eancom_v9.3/profiles/s3/desadv/en/html/in1.htm
- **Guía ASN de GS1 UK [L]**, «ASN Message Implementation Guideline», versión 1.3, marzo 2012 (estado Draft; copia alojada en una universidad portuguesa): «The Advanced Shipping Notice (ASN) is a document that provides detailed information about a pending delivery, and is sent prior to that delivery. It is usually sent in electronic format. In the GS1 EANCOM standard, this is the DESDAV, despatch advice message.» Beneficios que enumera: «Improves the goods receipt process», «Increases efficiency of receiving process through selective checking», «Provides accurate and timely information of expected goods before delivery through early notification of any delivery shortfalls», pago más rápido por cotejo con la factura. Con SSCC: al llegar la carga se escanea la etiqueta y el SSCC de cada pallet se cruza con lo informado antes. Deja el cross-docking fuera de su alcance («This document does not refer to cross dock operations»). Un segmento puede indicar «a dock number or delivery bay».
  https://disciplinas.tecnico.ulisboa.pt/meic-sei/2013-2014/labs/proj/gs1uk/ASN%20Guidelines.pdf
- **Versión vigente [S]**: EANCOM 2002 Syntax 3, directorio D.01B, subset 008 (Edition 2016, Upd. 2021); GS1 lista DESADV como equivalente EANCOM del X12 856 y lo empareja con RECADV (aviso de recepción). Las páginas de gs1.org dieron 403.
  https://gs1.org/sites/default/files/docs/eancom/s3/desadv.pdf
  https://gs1.org/docs/tl/GS1Standards_DeliveryManagement.pdf

### 3.2 ANSI X12 856 [S]
- «Ship Notice/Manifest»: lo envía el proveedor al comprador sobre una orden de compra; trae jerarquía (segmento HL), SSCC (MAN), seguimiento (REF), embalaje, transportista. El equivalente EDIFACT es DESADV. Cada comprador fija su versión (3M usa 004010; DLA, 3050), así que el mapeo depende del socio. No leí el estándar X12 (es de pago). Guías públicas de ejemplo: https://www.stedi.com/edi/x12-004040/856 y https://www.dla.mil/Portals/104/Documents/TroopSupport/ConstructionandEquipment/EDI/PopsGuides/856_305_v11.pdf (ambas [S]).

### 3.3 Programación de turnos de muelle (dock appointment scheduling)
- Académico [M]: Boysen & Fliedner, «Cross dock scheduling: Classification, literature review and research agenda», Omega 38(6):413-422, 2010. Propone una clasificación del problema de asignación de camiones a puertas y revisa la literatura. https://ideas.repec.org/a/eee/jomega/v38y2010i6p413-422.html
- Estudio empírico [S]: TU Delft sobre un sistema de reservas en Royal FloraHolland Aalsmeer (subasta de flores, no un depósito comercial): las reservas dispersan las llegadas, con mejoras visibles con tasas de reserva cercanas al 70 %. https://repository.tudelft.nl/file/File_d8134aa2-adf5-4e98-a006-a6cbe48f1291?preview=1
- Vendors [S]: Transporeon declara reducciones de espera «de hasta 40 %» sin metodología (https://www.transporeon.com/en/products/management/time-slot-management/); SAP e Infios explican el concepto (https://www.sap.com/blogs/why-dock-appointment-scheduling-and-freight-collaboration-matter-for-warehouse-execution, https://www.infios.com/en/knowledge-center/glossary/wms-dock-appointment-scheduling). No encontré estudio independiente y controlado de turnos de muelle en un centro de distribución.

### 3.4 Tiempos de espera de camiones en muelles (con cifras)
- **DOT OIG (inspector general), informe ST2018019, 31 de enero de 2018 [L]**, «Estimates Show Commercial Driver Detention Increases Crash Risks and Costs, but Current Data Limit Further Analysis» (exigido por la FAST Act 2015). Copia leída: https://www.3plcentral.com/hubfs/FMCSA%20Driver%20Detention%20Final%20Report.pdf (el original está en oig.dot.gov, que no me dejó entrar).
  - «Accurate industrywide data on driver detention do not currently exist because most industry stakeholders measure only time spent at a shipper or receiver's facility beyond the limit established in shipping contracts.»
  - «a 15-minute increase in average dwell time—the total time spent by a truck at a facility—increases the average expected crash rate by 6.2 percent».
  - La detención se asocia con pérdidas anuales de ingresos de «$1.1 billion to $1.3 billion» para conductores de carga completa y de «$250.6 million to $302.9 million» de ingreso neto para transportistas; entre 3,0 % y 3,6 % del ingreso medio anual del conductor.
  - Dwell time medio en la base usada: 113 minutos en 2013; paradas: 46 % de una hora o menos y cerca de 21 % de más de 2 horas (mismo 21 % que C.H. Robinson 2015).
  - Datos de 2013 y del estudio FMCSA 2014, no actuales. Seis de ocho transportistas entrevistados dicen que los cargadores a veces no pagan la detención, por ejemplo por llegar un minuto tarde a la cita.
- **GAO-11-198, 26 de enero de 2011 (público 18-feb-2011) [S]**, «Commercial Motor Carriers: More Could Be Done to Determine Impact of Excessive Loading and Unloading Wait Times»: más de 300 conductores entrevistados (muestra no generalizable); 59 % reportó detención en las dos semanas previas; cerca de 80 % de los afectados dijo que perjudicó el cumplimiento de las horas de servicio; en el primer estudio de FMCSA «about 10 percent of the stops experienced detention time». https://www.gao.gov/products/gao-11-198
- FMCSA «Impact of Driver Detention Time on Safety and Operations» (estudio con Virginia Tech Transportation Institute): https://www.fmcsa.dot.gov/research-and-analysis/impact-driver-detention-time-safety-and-operations (403, solo [S]).
- Discrepancia a señalar: «detención» (tiempo más allá del plazo contractual) y «dwell time» (tiempo total en la instalación) no son lo mismo, y el OIG dice que casi nadie mide el segundo. El 10 % (FMCSA vía GAO) y el 21 % (más de 2 horas, OIG) miden cosas distintas.
- Es evidencia de EE. UU.; no encontré equivalente argentino.

### 3.5 Quién contrata el flete según el Incoterm
- ICC Incoterms 2020, EXW [L]: A4 «The seller has no obligation to the buyer to make a contract of carriage.»; B4 «It is up to the buyer to contract or arrange at its own cost for the carriage of the goods from the named place of delivery.» https://library.iccwbo.org/content/tfb/BOOKS/BK_0049/BK_0049_04_RulesAny.htm
- ICC, página de Incoterms 2020 [L]: «a set of eleven three-letter trade terms» y «Used globally in trade contracts since 1936 (updated 2020)». https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/
- DAP y DDP [S]: el vendedor entrega en destino (DDP, despachada a importación, «ready for unloading»); bajo DAP el vendedor debe poder organizar la descarga. No leí A4 de FCA, CPT, CIF, etc.: **hueco**. Las reglas son de comercio exterior; en compras locales manda el contrato de compra.

### 3.6 Consolidación, milk run, cross-docking de entrada
- Milk run [S]: la literatura lo define como «regularly scheduled pick up tours serving a producing plant» (tesis KIT, https://publikationen.bibliothek.kit.edu/1000051064/3768326); INFORMS Transportation Science 2025 trata rutas de milk run fijas con fechas exactas que dependen de la secuencia de producción (https://pubsonline.informs.org/doi/fpi/10.1287/trsc.2025.0189); tesis UFSCar distingue milk run entrante, saliente e interno (https://repositorio.ufscar.br/bitstreams/f42548c6-93fc-4ed3-9e34-d1f52fd5b92c/download). Los explicadores de vendors coinciden: un vehículo, varios proveedores, ruta fija, un destino.
- Cross-docking: Boysen & Fliedner (arriba). La guía ASN de GS1 UK lo deja fuera.

### 3.7 Libros de texto (Chopra & Meindl, Ballou, CLTD)
- **Hueco.** No encontré texto leíble de Chopra & Meindl, Ballou ni del temario CLTD (ASCM) sobre flujo de entrada. Solo la tabla de contenidos de la 6.ª edición de Chopra (secciones de costo total y offshoring) [S].

### 3.8 Tabla de fuentes

| Fuente | Tipo | Leído | A/P/E/U | URL |
|---|---|---|---|---|
| GS1 Germany, EANCOM 2002 S3 DESADV (intro) | Primaria | [L] | 3/2/2/3 | https://www.publikationen.gs1-germany.de/Complete/eancom_v9.3/profiles/s3/desadv/en/html/in1.htm |
| GS1 UK ASN Message Implementation Guideline v1.3 (2012) | Primaria | [L] | 3/3/3/3 | https://disciplinas.tecnico.ulisboa.pt/meic-sei/2013-2014/labs/proj/gs1uk/ASN%20Guidelines.pdf |
| GS1 EANCOM DESADV S3 y Delivery Management | Primaria | [S] | 3/3/2/2 | https://gs1.org/sites/default/files/docs/eancom/s3/desadv.pdf |
| ANSI X12 856 (guías de Stedi, DLA) | Secundaria | [S] | 2/2/3/1 | https://www.stedi.com/edi/x12-004040/856 |
| DOT OIG ST2018019 (2018) | Primaria | [L] | 3/3/2/3 | https://www.3plcentral.com/hubfs/FMCSA%20Driver%20Detention%20Final%20Report.pdf |
| GAO-11-198 (2011) | Primaria | [S] | 3/2/2/2 | https://www.gao.gov/products/gao-11-198 |
| Boysen & Fliedner, Omega 2010 | Primaria | [M] | 3/3/1/3 | https://ideas.repec.org/a/eee/jomega/v38y2010i6p413-422.html |
| ICC Incoterms 2020 (EXW) | Primaria | [L] | 3/2/2/3 | https://library.iccwbo.org/content/tfb/BOOKS/BK_0049/BK_0049_04_RulesAny.htm |
| Milk run: KIT, INFORMS 2025, UFSCar | Primaria | [S] | 2/2/2/2 | enlaces de 3.6 |
| Vendors de turnos (Transporeon, SAP, Infios) | Secundaria | [S] | 1/1/2/1 | enlaces de 3.3 |

Recursos canónicos: ASN, guía GS1 UK más la ficha DESADV de GS1 Germany; detención, OIG ST2018019; Incoterms, texto ICC (reglas A4/B4).

### 3.9 Huecos
- Texto de X12 856 (estándar de pago) y de GS1 EANCOM leído desde gs1.org.
- Estudio independiente sobre turnos de muelle en depósitos; todo lo disponible es de vendors.
- Cifras de detención posteriores a 2018.
- Cifras de Argentina.
- Libros de texto.
- A4 de las demás reglas Incoterms.

---

## 4. Costo de llegada (landed cost)

- **Definición contable en fuente primaria [L]**: IAS 2 Inventarios, párrafo 11 (IFRS Foundation, edición 2026 en HTML): «The costs of purchase of inventories comprise the purchase price, import duties and other taxes (other than those subsequently recoverable by the entity from the taxing authorities), and transport, handling and other costs directly attributable to the acquisition of finished goods, materials and services. Trade discounts, rebates and other similar items are deducted in determining the costs of purchase.» No usa la expresión «landed cost»: habla de costo de compra. https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html
- **Definición de logística [L]**, DP World: «Landed cost is the total cost of a shipment delivered to a specified location» (incluye el costo de la mercadería y todos los gastos para llevarla del proveedor al destino final). Componentes: precio de la mercadería; flete marítimo o aéreo; seguro; derechos y tasas aduaneras; costos de destino (manipuleo en terminal, descarga, depósito); gastos de despacho y trucking al punto final. https://www.dpworld.com/en/glossary/landed-cost
- **Otras definiciones [S]**: DHL, costo total que asume el vendedor para producir, transportar y entregar al cliente (https://lot.dhl.com/glossary/landed-cost); UPS, «the total expense of shipping a product», con derechos, impuestos y tasas en lo internacional (https://www.ups.com/us/en/shipping/international-shipping/international-shipping-costs). DHL mira el costo del vendedor; IAS 2 y DP World, el del comprador.
- SCOR DS: métricas CO.3.13 «Inbound Freight and Duties» y CO.3.14 «Receiving and Material Storage» (ver 2.1).
- No hallé definición de «landed cost» en un glosario de la OMA, de CBP ni de la ICC.

| Fuente | Tipo | Leído | A/P/E/U | URL |
|---|---|---|---|---|
| IFRS, IAS 2 par. 11 | Primaria | [L] | 3/2/1/3 | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html |
| DP World glosario | Secundaria | [L] | 2/1/2/1 | https://www.dpworld.com/en/glossary/landed-cost |
| DHL glosario | Secundaria | [S] | 2/1/1/1 | https://lot.dhl.com/glossary/landed-cost |
| UPS | Secundaria | [S] | 2/1/1/1 | https://www.ups.com/us/en/shipping/international-shipping/international-shipping-costs |

Recurso canónico: IAS 2 párrafo 11 para qué entra al costo de compra; DP World para la lista operativa de componentes.

Huecos: definición de una autoridad aduanera o de la ICC; tratamiento argentino (NIC 2 vía normas contables locales, no verificado); cómo se prorratean los costos de llegada a cada ítem (IAS 2 no lo detalla en el párrafo 11).
