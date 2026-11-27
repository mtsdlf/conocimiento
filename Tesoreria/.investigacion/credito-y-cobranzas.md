# Investigación: Crédito y cobranzas

Fecha de lectura: 2026-11-27. Capa cruda del tema Tesorería. Marcas: [L] leído el texto completo o la parte citada; [M] metadatos o abstract; [S] resumen secundario o del buscador. Las páginas web se leyeron con un extractor que devuelve resúmenes y citas cortas, no el HTML completo; los PDF (Petersen y Rajan, guía de la Comisión, APQC) se bajaron y se leyeron como texto. Dos limitaciones: el texto literal de la Directiva en EUR-Lex y en legislation.gov.uk no se pudo bajar (respuesta vacía), y el presupuesto de búsquedas se agotó a mitad de la ronda, así que varios componentes quedan con una sola fuente o sin fuente (ver Huecos).

## Frontera con lo ya escrito

- No se repite: el registro del límite y de la condición de pago como datos del cliente ni su diseño como dato o regla (condiciones-comerciales.md), ni el ECHEQ en cifras del BCRA de septiembre de 2026, la Factura de Crédito Electrónica MiPyME, el dato del Observatorio PyME (62% de las industrias pyme vio alargarse los plazos de cobro) ni la ausencia de medición del reparto de plazos (cuenta-corriente-y-credito.md). Esas notas dicen que el límite «lo decide Tesorería» y dejan sin fuente las retenciones y la mora minorista; este informe aporta el método de decidir y de cobrar.
- Frontera con Contabilidad: asiento del cobro, auxiliar de clientes, antigüedad de saldos como informe, previsión de incobrables, conciliación bancaria. APQC las mezcla en el mismo proceso 9.2; el árbol de Tesorería las parte.

## Observación sobre la división del árbol

APQC no pone crédito y cobranzas dentro de tesorería (9.7): los pone en 9.2 «Perform revenue accounting», junto con la facturación, y en 9.2.3 y 9.2.4 mezcla lo que acá se reparte entre Contabilidad y Tesorería. La división de las tres partes del brief calza con 9.2.1 (crédito), 9.2.4 (cobranza) y 9.2.3.3 (aplicación). Las **deducciones y disputas** (9.2.5, «Manage and process adjustments/deductions») son un subproceso propio en APQC y en el árbol no tienen casa: conviene que caigan en aplicación de cobros (diferencias y retenciones) o en gestión de la cobranza (disputas).

## Tabla de fuentes

| # | Fuente | URL | Tipo | Aut. | Prof. | Ejem. | Uni. | Marca |
|---|---|---|---|---|---|---|---|---|
| 1 | Petersen y Rajan 1997, *Trade Credit: Theories and Evidence*, Review of Financial Studies 10(3), 661-691 (versión NBER WP 5602, junio de 1996) | https://www.nber.org/system/files/working_papers/w5602/w5602.pdf (resumen: https://www.nber.org/papers/w5602) | primaria | 3 | 3 | 2 | 3 | [L] el abstract y las partes citadas; no leí todo. El PDF se extrajo por OCR: los números se contrastaron donde se pudo |
| 2 | Comisión Europea, *Late Payment Directive 2011/7/EU: FAQs* (DG GROW) | https://ec.europa.eu/docsroom/documents/16222/attachments/1/translations/en/renditions/native | primaria (guía oficial de la norma) | 3 | 2 | 2 | 2 | [L] |
| 3 | Comisión Europea, página sobre la Directiva | https://single-market-economy.ec.europa.eu/smes/sme-strategy/late-payment-directive_en | primaria | 3 | 1 | 1 | 1 | [S] por el extractor; coincide con la 2 |
| 4 | Directiva 2011/7/UE, texto | https://eur-lex.europa.eu/eli/dir/2011/7/oj/eng | primaria (la ley) | 3 | 3 | 1 | 3 | no leída: la descarga devolvió vacío |
| 5 | APQC, Process Classification Framework, Cross Industry, versión 7.4 (agosto de 2024), 9.2.1 a 9.2.5 | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | primaria (marco) | 3 | 2 | 1 | 3 | [L] los títulos de 9.2; el marco no trae definiciones largas |
| 6 | ERPNext, Dunning | https://docs.frappe.io/erpnext/user/manual/en/dunning | primaria de práctica | 2 | 2 | 2 | 2 | [L] vía extractor |
| 7 | ERPNext, Payment Entry | https://docs.frappe.io/erpnext/user/manual/en/payment-entry | primaria de práctica | 2 | 2 | 3 | 2 | [L] vía extractor |
| 8 | Wikipedia, Days sales outstanding | https://en.wikipedia.org/wiki/Days_sales_outstanding | secundaria (cita a Houston y Brigham 2009, *Fundamentals of Financial Management*, p. 90) | 1 | 1 | 1 | 1 | [S] |
| 9 | Wikipedia, Trade credit insurance | https://en.wikipedia.org/wiki/Trade_credit_insurance | secundaria, con etiqueta de «faltan citas» | 1 | 1 | 1 | 1 | [S] |
| 10 | Wikipedia, Trade credit | https://en.wikipedia.org/wiki/Trade_credit | secundaria, con etiqueta de «faltan citas» | 1 | 1 | 1 | 1 | [S]; solo sirve de índice a Murfin y Njoroge 2012 y Chludek 2010 |
| 11 | APQC, páginas de benchmarks de cuentas a cobrar (definiciones de 9.2.2 a 9.2.5) | https://www.apqc.org/resource-library/resource-collection/accounts-receivable-and-collections-key-benchmarks | primaria | 3 | 1 | 1 | 1 | [S] por el buscador, sin abrir la página |

Las URL probadas de Odoo (follow-up), OpenStax (capítulos de cuentas a cobrar), y Wikipedia (Five Cs of credit, Cash application) devolvieron 404: se descartan, no se citan.

## 1. Crédito a clientes

### Por qué las empresas dan crédito comercial (evidencia con método)

Hay una sola fuente con método. Petersen y Rajan 1997 (fuente 1) usan la Encuesta Nacional de Pequeñas Empresas (NSSBF) de la Reserva Federal y la Small Business Administration, hecha en 1988-89 sobre empresas pequeñas no financieras ni agrícolas que operaban en diciembre de 1987. Hallazgos, con el abstract literal:

- Las pequeñas empresas usan más crédito comercial cuando no hay crédito financiero: «firms use trade credit relatively more when credit from financial institutions is not available». Luego: «while short term trade credit may be routinely used to minimize transactions costs, medium term borrowing against trade credit is a form of financing of last resort».
- Por qué el proveedor presta cuando nadie más lo hace: «they may have a comparative advantage in getting information about buyers cheaply, they have a better ability to liquidate goods, and they have a greater implicit equity stake in the firm's long term survival».
- «some evidence consistent with the use of trade credit as a means of price discrimination».
- «firms with better access to credit from financial institutions offer more trade credit»: las empresas con mejor acceso al banco intermedian hacia las que tienen menos.
- Cifra de la tabla 1: las cuentas a pagar son el 4,4% de las ventas en las empresas pequeñas de la muestra y el 11,6% en las grandes de Compustat (datos de 1987); las pequeñas «uniformly use less trade credit than the large firms».
- Costo implícito de un plazo con descuento, literal: en términos «2-10 net 30» el cliente recibe 2% de descuento si paga en 10 días o paga el total al día 30; quien paga el día 30 «is effectively borrowing over the next 20 days at an annual rate of 43.5 percent». Es el precio que el vendedor le pone a su propio plazo (el lado de quien paga está en Pagos a proveedores).

Límites: datos de Estados Unidos, empresas pequeñas, 1987; no mide pymes de América Latina ni inflación alta. No leí el texto completo.

Hueco: no hay segunda fuente con método. Candidatas citadas pero no leídas: Murfin y Njoroge 2012 («Small Lending Big», sobre el costo para un proveedor pequeño de financiar a clientes grandes) y Chludek 2010 (ambas aparecen en la fuente 10, secundaria); Ng, Smith y Smith 1999 y Smith 1987 (información asimétrica) están citadas en Petersen y Rajan.

### Política, las cinco C, límite, garantías, seguro de crédito

- **APQC 9.2.1 «Process customer credit»** (fuente 5, [L] los títulos), siete hijos literales: 9.2.1.1 Establish credit policies; 9.2.1.2 Analyze/Approve new account applications; 9.2.1.3 Analyze credit scoring history; 9.2.1.4 Forecast credit scoring requirement; 9.2.1.5 Review existing accounts; 9.2.1.6 Produce credit/collection reports; 9.2.1.7 Reinstate or suspend accounts based on credit policies. Es la mejor descomposición abierta del componente: política, alta, historial de puntaje, previsión del requerimiento, revisión periódica, reportes, y reactivar o suspender cuentas (el bloqueo al pasar del límite).
- **Las cinco C** (carácter, capacidad, capital, colateral, condiciones): sin fuente leída. Hueco.
- **Límite de crédito**: ninguna fuente leída dice cómo calcularlo. Hueco. Lo que sí sale de la práctica del seguro (fuente 9, [S]): el asegurado fija un límite por comprador y las ventas se aseguran solo cuando el límite está vigente.
- **Seguro de crédito comercial** (fuente 9, [S]): cubre pérdidas por impago, insolvencia o quiebra del cliente; lo contratan empresas, no individuos; puede incluir riesgo político en ventas al exterior; la aseguradora paga «an agreed percentage of an invoice or receivable that remains unpaid»; la prima se cobra mensualmente como porcentaje de las ventas del mes o de las cuentas a cobrar pendientes. La cifra de exposición de 3,5 billones de euros en 2024 es de tercera mano (Wikipedia cita una nota de Morningstar DBRS); no se usa. No hallé porcentaje típico de cobertura ni deducible.
- **Garantías** (pagaré, aval, carta de crédito, prenda): sin fuente leída. Hueco.

### Plazos de pago y ley: Directiva 2011/7/UE

La guía oficial de la Comisión (fuente 2, [L]) y la página de la Comisión (3, [S]) concuerdan; ambas son de la misma institución, así que cuentan como una sola línea de fuente oficial, y el texto de la ley (4) no se pudo leer. Literal, de la guía:

- «Public authorities have to pay for the goods and services that they procure within 30 days or, in very exceptional circumstances, within 60 days.»
- «Businesses have to pay their invoices within 60 days, but can choose a longer payment term as long as it is expressly agreed in the contract and provided that it is not grossly unfair to the creditor. In cases of delayed payment, creditors are automatically entitled to interest for late payment and €40 minimum as compensation for recovery costs.»
- Interés (artículo 2(6) según la guía): «the TOTAL of i) the reference rate of the European central bank [...] and ii) at least 8 percentage points».
- Los €40 son por factura: «the creditor will have a separate fixed amount of €40 per invoice», más otros costos razonables.
- El plazo se cuenta «from the date that an invoice is delivered»; si la fecha de recepción de la factura es incierta, desde la recepción de los bienes o servicios.
- Una cláusula que excluye intereses por mora «will be considered to be grossly unfair to the creditor»; la que excluye la compensación por costos de cobro se presume abusiva.
- Países que fueron más allá: Alemania, 30 días como máximo («likely to be considered unreasonable» un plazo mayor ante una disputa); Austria, 60 días como máximo.

Un plazo supletorio de 30 días cuando el contrato no fija fecha (artículo 3(3)) sale solo del buscador [S]: no se cita como literal. La propuesta de 2023 de la Comisión de reemplazar la Directiva por un reglamento con máximo de 30 días no se leyó: hueco, y su estado a noviembre de 2026 es desconocido para este informe.

Esto no rige en Argentina. Sirve de evidencia de que el plazo de pago entre empresas se regula en otros mercados. Lo argentino (Factura de Crédito Electrónica) ya está en cuenta-corriente-y-credito.md.

### Recurso canónico del componente

- Petersen y Rajan 1997, abstract y secciones de teoría. En qué fijarse: el crédito comercial es financiación con ventaja de información, no un favor, y la regla 2-10 net 30 equivale a 43,5% anual.
- APQC PCF 9.2.1, para la lista de tareas de la política.
- Comisión Europea, FAQs de la Directiva 2011/7/UE (preguntas 1, 3, 4, 7 y 16), para ver cómo se escribe una regla de plazos y mora.

## 2. Gestión de la cobranza

- **APQC 9.2.4 «Manage and process collections»** (fuente 5, [L]), hijos literales: 9.2.4.1 Establish policies for delinquent accounts; 9.2.4.2 Analyze delinquent account balances; 9.2.4.3 Correspond/Negotiate with delinquent accounts; 9.2.4.4 Discuss account resolution with internal parties; 9.2.4.5 Process adjustments/write off balances; 9.2.4.6 Perform recovery workout; 9.2.4.7 Manage default accounts. El ciclo: política de morosos, análisis, contacto y negociación, coordinación interna, ajuste o castigo, recuperación y gestión de cuentas en default. El asiento del castigo es de Contabilidad; el cuándo y quién lo autoriza, de Tesorería.
- **Secuencia de recordatorios (dunning)**, práctica en software, no norma (fuente 6, [L] vía extractor): un documento formal de reclamo reúne las cuotas vencidas de las facturas, calcula interés y cargos, guarda la carta enviada y vincula el pago posterior; no reemplaza la factura ni crea una venta. Un «tipo» es una plantilla de etapa (primer recordatorio, segundo, aviso final) con cargo fijo, tasa de interés anual, texto de la carta y cuenta de ingreso. Estados: Draft, Unresolved, Resolved, Cancelled. La fuente no menciona período de gracia. La práctica equivalente de Odoo (seguimiento) no se pudo leer.
- **Mora y acuerdos de pago**: sin fuente leída. En APQC corresponden a 9.2.4.3 y 9.2.4.6.
- **Paso a legales o dar por incobrable**: sin criterio en ninguna fuente (cuánto monto, cuántos días). APQC lo nombra (9.2.4.5, 9.2.4.7) pero no dice cuándo.
- **DSO** (fuente 8, [S], cita a Houston y Brigham 2009, p. 90): cuentas a cobrar / ventas diarias promedio, o cuentas a cobrar / (ventas anuales / 365). Lo que dice sobre sus límites: mide «not in units of currency, but in average sales days»; «can vary from month to month, and over the course of a year with a company's seasonal business cycle»; se lee mal como tiempo promedio de cobro, cuando es el número de días de venta promedio que siguen pendientes; una caída de ventas sola lo sube; un período corto distorsiona; qué es «bueno» depende del rubro. No discute por nombre el crecimiento ni la mezcla de clientes: esas críticas, que sí se repiten en la práctica, son inferencia y no tienen autor citado en este informe.
- **Best possible DSO**: la misma fuente lo define como cuentas a cobrar corrientes (no vencidas) / ventas diarias promedio, y llama DDSO («days delinquent sales outstanding») a las cuentas a cobrar vencidas / ventas diarias promedio, de modo que DDSO = DSO menos best possible DSO. De segunda mano, de una enciclopedia abierta: vale como definición, no como autoridad.
- **CEI (índice de eficacia de cobranza)**: la fuente consultada no lo cubre. Hueco; no se escribe la fórmula sin fuente.

Recurso canónico: APQC 9.2.4 para el ciclo y la documentación de ERPNext (Dunning) para ver cómo se modela. En métricas falta un recurso; el ideal es el capítulo de cuentas a cobrar de OpenStax *Principles of Finance*, cuya URL no pude confirmar.

## 3. Aplicación de cobros (cash application)

- **APQC 9.2.3 «Process accounts receivable (AR)»** (fuente 5, [L]), hijos literales: 9.2.3.1 Establish AR policies; 9.2.3.2 Receive/Deposit customer payments; 9.2.3.3 Apply cash remittances; 9.2.3.4 Prepare AR reports; 9.2.3.5 Post AR activity to the general ledger. Definición, de la página de benchmarks de APQC (fuente 11, [S]): «Processing payments due from customers. This includes all processing of funds received, whether by check or electronically. This does not include the generation of invoices.»
- **Cómo lo modela un sistema abierto** (fuente 7, [L] vía extractor, Payment Entry y Payment Reconciliation):
  - Pago parcial: el cobro menor a la factura deja saldo; el total aplicado puede ser menor o igual al cobro, no mayor.
  - Anticipo o cobro sin aplicar: «An advance or standalone payment can remain unallocated» hasta conciliarlo después; «Keep unallocated payments available for later reconciliation».
  - Diferencia: si no coinciden cobro y aplicación, se revisan importes, tipo de cambio y asignaciones; comisiones bancarias, retenciones, pequeños castigos o diferencias de cambio van a «Deductions or Losses» con cuenta explícita; las comisiones no se cargan como impuestos y cargos porque «it is not money paid to the party».
  - Castigo de deuda incobrable: no en el cobro, sino con un asiento manual.
  - Aplicación equivocada: se desaplica y se vuelve a conciliar.
  - Prueba que la práctica existe (parcial, anticipo, sin identificar, diferencia, retención); no dice cómo identificar un cobro sin referencia.
- **Cobro sin identificar, remesa y retenciones sufridas**: sin fuente profesional leída más que lo anterior. Es el hueco de fondo: falta una fuente que explique cómo se empareja un cobro (qué datos se usan), qué se hace con lo no emparejado y cuánto tiempo. AFP y ACT lo tratan según el mapa del brief, pero no se pudieron consultar.
- **Deducciones y disputas** (APQC 9.2.5, [L] los títulos): 9.2.5.1 Establish policies/procedures for adjustments; 9.2.5.2 Analyze adjustments; 9.2.5.3 Correspond/Negotiate with customer; 9.2.5.4 Discuss resolution with internal parties; 9.2.5.5 Prepare chargeback invoices; 9.2.5.6 Process related entries. Es lo que el cliente descuenta al pagar (devoluciones, diferencias de precio, retenciones).
- Frontera: el asiento del cobro y la conciliación bancaria son de Contabilidad; la aplicación a facturas, de Tesorería. APQC separa 9.2.3.3 (aplicar remesas) de 9.2.3.5 (contabilizar), lo que respalda la frontera.

## 4. Medios de cobro desde la empresa

Casi sin fuente propia: el cheque y el ECHEQ en Argentina están en cuenta-corriente-y-credito.md (BCRA, septiembre de 2026) y los medios online en Comercio electrónico/Pagos. Lo único leído que toca el tema es APQC 9.2.3.2 «Receive/Deposit customer payments» y la definición de 9.2.3 («whether by check or electronically»), que confirma que el marco trata el cheque y lo electrónico como dos formas de recibir. Sin fuente sobre tiempos de acreditación, costos por medio, débito directo ni efectivo: hueco entero.

## Recursos canónicos (resumen)

| Componente | Recurso | Qué parte | En qué fijarse |
|---|---|---|---|
| Crédito | Petersen y Rajan 1997 | abstract y teoría | financiación con ventaja de información; 2-10 net 30 = 43,5% anual |
| Crédito | APQC PCF 7.4, 9.2.1 | siete subprocesos | política, alta, revisión, suspensión |
| Plazos y mora | Comisión Europea, FAQs 2011/7/UE | preguntas 1, 3, 4, 7, 16 | 60 días como norma, interés más ocho puntos, €40 por factura |
| Cobranza | APQC 9.2.4 | siete subprocesos | de la mora al default |
| Cobranza | ERPNext, Dunning | tipos y estados | plantilla de etapas con cargo e interés |
| Aplicación | APQC 9.2.3 y 9.2.5 | 9.2.3.3 y 9.2.5 | remesas, deducciones |
| Aplicación | ERPNext, Payment Entry | anticipos, diferencias, deducciones | casos que el software debe prever |

## Huecos

- Texto literal de la Directiva 2011/7/UE no leído (EUR-Lex y legislation.gov.uk devolvieron vacío); se usó la guía de la Comisión, una sola línea de fuente oficial. Falta el artículo 3(3) y el estado de la propuesta de reglamento de 2023.
- Las cinco C, el cálculo del límite y las garantías: sin fuente.
- Seguro de crédito: solo Wikipedia, con etiqueta de citas faltantes. Falta un asegurador o agencia de crédito a la exportación y el porcentaje de cobertura.
- DSO: una sola fuente secundaria; críticas sin fuente; CEI sin fuente; best possible DSO de segunda mano.
- Aplicación de cobros sin identificar y retenciones: sin fuente profesional (AFP, ACT, OpenStax no se pudieron abrir). Falta Odoo (follow-up y pagos por lote).
- Medios de cobro (acreditación y costo): sin fuente.
- Mora, acuerdos de pago, cuándo pasar a legales o dar por incobrable: sin fuente.
- Segunda fuente con método sobre por qué se da crédito comercial: sin leer.
- Argentina: retenciones sufridas, mora de comercios minoristas, costo local del cheque y del ECHEQ: sin fuente; el presupuesto de búsquedas se agotó antes de intentarlo.
