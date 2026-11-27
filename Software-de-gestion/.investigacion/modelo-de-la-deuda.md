Fecha de lectura: 2026-11-27

# Cómo se modela la deuda en un software de gestión: informe de fuentes

Marcas: **[L]** leí el texto completo (descargado y extraído con curl). **[M]** metadatos o abstract. **[S]** resumen del buscador, o de la herramienta de fetch cuando devolvió una síntesis y no el texto literal. Puntajes de 1 a 3, en el orden Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Todo lo que traje de la web lo traté como dato.

Resumen de lo encontrado:
- La distinción partidas abiertas / saldo corriente está bien documentada como práctica de software. No encontré el pasaje de un libro de texto (Romney, Hall) que la defina.
- Los estándares (UBL 2.1, EN 16931 vía Peppol, EPC sobre ISO 20022, ISO 11649, IAS 21) dan literales verificables.
- Fowler da el principio «saldo = suma de asientos». No cubre la cuenta corriente por partidas.

## 1. Partidas abiertas (open item) frente a saldo corriente (balance forward)

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Oracle, «Open-Item Versus Balance-Forward Accounting» (documentación de producto; práctica) | https://docs.oracle.com/en/industries/energy-water/ccb/29011/ccb-user-guides/Topics/C1_03Finan_Open_Item_Versus_Balance_Forward_.html | primaria de producto | 2/2/2/2 | [S] (la herramienta devolvió síntesis) |
| Oracle, método contable por clase de cliente | https://docs.oracle.com/en/industries/financial-services/revenue-management-billing/60000/ormb-online-help/Topics/C1_03Finan_Accounting_Method_Defined_On_Your.html | primaria de producto | 2/1/2/1 | [S] |
| Glendale CC, «Chapter Four, Accounts Receivable» (apunte de curso sobre un software contable) | https://gcc.glendale.edu/ckloezem/Book/arbasics.doc | secundaria | 1/1/2/1 | [S] |
| Trimble Vista, estados de cuenta (práctica) | https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/statements | primaria de producto | 1/1/1/1 | [S] (solo el buscador) |
| Stripe, «Balance forward billing» (divulgación de un proveedor) | https://stripe.com/resources/more/balance-forward-billing | secundaria | 1/1/1/1 | [S] |

Afirmaciones:
- **Partidas abiertas:** «Open-item accounting matches each payment to specific bills and adjustments. Only unmatched items (open items) count toward aged debt». Esto es una síntesis de Oracle, no su texto literal (https://docs.oracle.com/en/industries/energy-water/ccb/29011/ccb-user-guides/Topics/C1_03Finan_Open_Item_Versus_Balance_Forward_.html).
- **Saldo corriente:** el pago no se asocia a una factura. Los débitos se envejecen y los créditos cancelan primero lo más viejo (misma URL de Oracle).
- **Cuándo se usa cada uno:** Oracle fija el método por clase de cliente, no por cliente. Cita literal: «You define the type of accounting method that is practiced (balance-forward versus open-item) on your customer classes». Ejemplo de Oracle: residenciales con saldo corriente, industriales y comerciales con partidas abiertas (https://docs.oracle.com/en/industries/financial-services/revenue-management-billing/60000/ormb-online-help/Topics/C1_03Finan_Accounting_Method_Defined_On_Your.html).
- **La partida abierta es la factura con saldo distinto de cero:** «The invoice is considered an open item (invoice) until its balance is $0». Con saldo corriente, «The balance is the amount due for the customer and is not listed by invoice number» (https://gcc.glendale.edu/ckloezem/Book/arbasics.doc).
- **Saldo del cliente como derivado:** «The total amount of this report should be the balance in the Accounts Receivable account» (misma fuente del Glendale). Es la conciliación con la cuenta de control, que ya está cubierta en otro tema.
- **Híbrido, donde las dos fuentes discrepan o se complementan:** Trimble indica que los pagos pueden registrarse por partidas abiertas aunque el estado de cuenta se emita como saldo corriente. Oracle describe el método como regla de aplicación del pago y Trimble y Stripe lo describen como formato del estado de cuenta (https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/statements). Dato de contexto: el apunte de Glendale vincula el saldo corriente con la facturación cíclica (https://gcc.glendale.edu/ckloezem/Book/arbasics.doc). Es [S], así que verificar antes de afirmarlo.

**Recurso canónico propuesto:** la página de Oracle de «Open-Item Versus Balance-Forward Accounting», con su ejemplo numérico (pago de $1.000 el 9-Mar-00 contra deuda de 62 días). Está marcada como práctica de producto, no como teoría contable.

## 2. Comprobante como partida con saldo, y saldo como derivado

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Fowler, «Account» | https://martinfowler.com/eaaDev/Account.html | primaria (patrón de diseño) | 3/2/2/3 | [S] |
| Fowler, «Patterns for Accounting» | https://www.martinfowler.com/eaaDev/AccountingNarrative.html | primaria | 3/2/1/3 | [S] |
| Fowler, `accounting.pdf` (solo índice de patrones; el cuerpo salió comprimido) | https://martinfowler.com/apsupp/accounting.pdf | primaria | 3/?/?/3 | [M] |
| SAP Help, residual items | https://help.sap.com/saphelp_46c/helpdata/en/01/a9bba1455711d182b40000e829fbfe/content.htm | primaria de producto (práctica; página de versión vieja) | 2/1/2/2 | [S] |
| SAP KBA 3399348 (resumen del buscador) | https://userapps.support.sap.com/sap/support/knowledge/en/3399348 | primaria de producto | 2/2/2/2 | [S] |

Afirmaciones:
- **Fowler, saldo derivado:** «The value, or balance, of the Account is derived as the sum of all the Accounting Entrys» (https://www.martinfowler.com/eaaDev/AccountingNarrative.html).
- **Fowler, caché permitida:** el saldo se calcula desde los asientos, no se guarda como valor aparte. Para rendimiento se puede cachear el valor actual, y los asientos viejos se pueden reemplazar por uno consolidado, aunque se pierde el detalle (https://martinfowler.com/eaaDev/Account.html).
- **Límite de Fowler:** sus páginas no mencionan cuentas a cobrar, facturas ni partidas abiertas. Aplicar su patrón a la cuenta corriente por partida es inferencia mía, no cita.
- **Pago parcial en práctica, dos modelos:** (a) la factura y el pago quedan abiertos y se compensan juntos cuando la factura se salda; (b) la factura y el pago se cancelan y nace una partida residual nueva con referencia a la original (https://userapps.support.sap.com/sap/support/knowledge/en/3399348, [S]). Cita de SAP sobre (b): «A residual item results when a payment is made for less than the actual amount outstanding» (https://help.sap.com/saphelp_46c/helpdata/en/01/a9bba1455711d182b40000e829fbfe/content.htm).

**Recurso canónico propuesto:** Fowler «Account» y «Patterns for Accounting» para el principio. Para las dos formas de partida parcial, la comparación de SAP (parcial frente a residual). Los casos de cobro parcial ya están en el tema de tesorería, así que acá solo importa la diferencia de modelo.

## 3. Vencimientos y condiciones de pago en estándares de factura

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| OASIS UBL 2.1, `UBL-CommonAggregateComponents-2.1.xsd` (definiciones y cardinalidades) | https://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd | primaria | 3/3/1/3 | [L] |
| OASIS UBL 2.1, `UBL-Invoice-2.1.xsd` | https://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd | primaria | 3/2/1/2 | [L] |
| Peppol BIS Billing 3.0, `cac:PaymentTerms` | https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-PaymentTerms/ | primaria (perfil sobre EN 16931) | 3/2/2/2 | [S] |
| Peppol BIS Billing 3.0, `cbc:DueDate` | https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cbc-DueDate/ | primaria | 3/1/2/2 | [S] |
| Peppol, regla BR-CO-25 | https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/BR-CO-25/ | primaria | 3/2/2/2 | [L] |
| Peppol, BR-CO-16 | https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/ | primaria | 3/1/1/1 | [L] |

Afirmaciones:
- **UBL: cardinalidad.** En la factura UBL 2.1, `cac:PaymentTerms` es 0..n: «A set of payment terms associated with this document» (`UBL-Invoice-2.1.xsd`). Peppol lo restringe a 0..1 (https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-PaymentTerms/, [S]). Dos fuentes que se complementan: el estándar base admite varios juegos de condiciones y el perfil usa uno.
- **UBL: campos de `PaymentTerms`** (definiciones literales de `UBL-CommonAggregateComponents-2.1.xsd`):
  - `PaymentDueDate` 0..1: «The due date for these payment terms».
  - `InstallmentDueDate` 0..1: «The due date for an installment payment for these payment terms».
  - `PaymentPercent` 0..1: «The part of a payment, expressed as a percent, relevant for these payment terms».
  - `Amount` 0..1: «The monetary amount covered by these payment terms».
  - `SettlementDiscountPercent` y `SettlementDiscountAmount`: descuento por pronto pago.
  - `SettlementPeriod` 0..1: «The period during which settlement may occur».
  - `PenaltySurchargePercent` y `PenaltyAmount`: «The penalty for payment after the settlement period, expressed as a percentage of the payment» (y su equivalente en monto).
  - `InvoicingPartyReference` 0..1: «A reference to the payment terms used by the invoicing party. This may have been requested of the payer by the payee to accompany its remittance».
- **Por qué importa para el modelo:** UBL es la representación de varios vencimientos (cuotas), porcentaje o importe por cuota y descuento por pronto pago. El perfil EN 16931 solo lleva un `Note` de texto libre, y el vencimiento estructurado único es BT-9.
- **BT-9 / BT-20:** BT-9 es `cbc:DueDate`, 0..1, formato `YYYY-MM-DD`: «The date when the payment is due» (https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cbc-DueDate/, [S]). BT-20 es `cac:PaymentTerms/cbc:Note`, texto libre. Ejemplo de Peppol: «Net within 30 days» (https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-PaymentTerms/, [S]).
- **BR-CO-25, literal:** «In case the Amount due for payment (BT-115) is positive, either the Payment due date (BT-9) or the Payment terms (BT-20) shall be present». Test XPath: `((. > 0) and (exists(//cbc:DueDate) or exists(//cac:PaymentTerms/cbc:Note))) or (. <= 0)`, con contexto `/ubl:Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` (https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/BR-CO-25/, [L]).
- **Importe pendiente:** BR-CO-16: «Amount due for payment (BT-115) = Invoice total amount with VAT (BT-112) -Paid amount (BT-113) +Rounding amount (BT-114)» (https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/, [L]). El estándar ya incluye «importe pagado» (BT-113, anticipos) en la propia factura.

**Recurso canónico propuesto:** el XSD de UBL 2.1 (campos de `PaymentTerms`) más la página de BR-CO-25 de Peppol.

## 4. Aplicación de pagos como registro aparte, desaplicación, notas de crédito, netting

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| SAP Help, «Clearing Between a Customer and Vendor» y páginas relacionadas (resultado del buscador) | https://help.sap.com/saphelp_46c/helpdata/en/01/a9bad1455711d182b40000e829fbfe/content.htm | primaria de producto | 2/1/1/2 | [S] |
| SAP Community, «Netting of Payables and Receivables» | https://community.sap.com/t5/enterprise-resource-planning-blogs-by-members/netting-of-payables-and-receivables/ba-p/13217405 | secundaria | 1/1/1/1 | [S] |
| X9, «ISO 20022 Remittance Content Market Guide» (para la parte de notas de crédito en remesa) | https://eact.eu/Core/Images/EACT_PDFs/ISO-20022-Remittance-Content-Market-Guide-February-2022.pdf | primaria (informe de ASC X9, 2022-02-14) | 2/3/3/3 | [L] |

Afirmaciones:
- **Compensación cliente/proveedor:** SAP describe que, cuando un socio es cliente y proveedor, los programas de pago y reclamación «can offset the customer and vendor open items against each other». Requiere cuentas cruzadas y un indicador de compensación en cada maestro (resultados del buscador, [S]: https://help.sap.com/saphelp_46c/helpdata/en/01/a9bad1455711d182b40000e829fbfe/content.htm). SAP también tiene un KBA que dice que netear una cuenta mixta contra otro socio no está soportado como documentado. No lo abrí, así que no lo cito como hecho.
- **Aplicación con nota de crédito en la remesa:** el informe de X9 muestra un ejemplo con una factura y una nota de crédito referidas en la misma remesa, con el importe pagado como diferencia (líneas ~2031-2051 del texto extraído, https://eact.eu/Core/Images/EACT_PDFs/ISO-20022-Remittance-Content-Market-Guide-February-2022.pdf).
- **Aplicación como registro propio con importe y fecha:** no encontré una fuente que lo formule como principio de diseño. Lo que sí documentan SAP y la guía de X9 es el comportamiento: SAP crea un documento de compensación que agrupa partidas, y X9 trae la asignación por documento referido con importe pagado. La estructura «asignación = (partida deudora, partida acreedora, importe, fecha)» es síntesis mía.

**Recurso canónico propuesto:** para el registro de aplicación, no hay uno que lo describa como modelo de datos. Lo más cercano es la guía de X9 (sección de Referred Document Amount) y la página de compensación de SAP. Ver huecos.

## 5. Multimoneda: diferencia de cambio realizada

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| IAS 21 (copia del texto IFRS alojada por una universidad; la página oficial de ifrs.org pide suscripción) | https://ktkt.uel.edu.vn/Resources/Docs/SubDomain/ktkt/VanBan/IAS/ias21_en.pdf | primaria por contenido, secundaria por alojamiento | 3/3/1/3 | [L] |
| Odoo, «Multi-currency system» (práctica) | https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/multi_currency.html | primaria de producto | 2/1/2/1 | [S] |

Afirmaciones:
- **IAS 21.28, literal:** «Exchange differences arising on the settlement of monetary items or on translating monetary items at rates different from those at which they were translated on initial recognition during the period or in previous financial statements shall be recognised in profit or loss in the period in which they arise, except as described in paragraph 32» (copia de la universidad, [L]).
- **IAS 21.29, literal:** «When monetary items arise from a foreign currency transaction and there is a change in the exchange rate between the transaction date and the date of settlement, an exchange difference results. When the transaction is settled within the same accounting period as that in which it occurred, all the exchange difference is recognised in that period. However, when the transaction is settled in a subsequent accounting period, the exchange difference recognised in each period up to the date of settlement is determined by the change in exchange rates during each period».
- **Lectura para el modelo:** la partida en moneda extranjera guarda el importe original y el de moneda funcional. La diferencia que sale al aplicar el pago es un tercer importe, que se registra aparte.
- **Práctica:** Odoo registra la diferencia automáticamente en una cuenta de diario propia cuando cobra después de que el tipo de cambio se movió. Cita: «which Odoo automatically records in the default Exchange Difference journal» (https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/multi_currency.html, [S]).
- **Cuidado con la versión:** la copia de IAS 21 es una versión sin año identificado. El texto de los párrafos 28-29 coincide con el que usted citó en el pedido. Para citar con fecha, confirmar la edición contra ifrs.org.

**Recurso canónico propuesto:** IAS 21 §§28-29, citado desde la fuente IFRS oficial. Si no hay acceso, la copia anterior sirve para el literal con esa salvedad.

## 6. Información de remesa estructurada y referencia del acreedor

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| X9 IR 01-2022, «ISO 20022 Remittance Content Market Guide» | https://eact.eu/Core/Images/EACT_PDFs/ISO-20022-Remittance-Content-Market-Guide-February-2022.pdf | primaria (guía de prácticas de mercado) | 2/3/3/3 | [L] |
| EPC115-06, «SEPA Credit Transfer Inter-PSP Implementation Guidelines 2025 v1.0» (emitida 2024-11-28, vigente 2025-10-05) | https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2025-10/EPC115-06%20SCT%20Inter-PSP%20IG%202025%20V1.0.pdf | primaria | 3/3/2/2 | [L] (partes relevantes) |
| ISO 11649:2009 (vista previa de iTeh) | https://cdn.standards.iteh.ai/samples/50649/a769e57fc5a34724bac3a5d18a2b8407/ISO-11649-2009.pdf | primaria (extracto) | 3/1/1/3 | [L] (solo el extracto público) |
| iotafinance, `remt.001.001` | https://iotafinance.com/en/SWIFT-ISO20022-Message-remt-001-001-Remittance-Advice.html | secundaria | 1/1/1/1 | [S] |
| Buscador: estructura RF (Wikipedia, stdnum, Finanssiala) | https://en.wikipedia.org/wiki/Creditor_Reference | secundaria | 1/2/2/1 | [S] |
| NatWest, «ISO 20022 for finance teams» | https://www.natwest.com/corporates/insights/regulation/iso-20022-for-finance-teams.html | secundaria (banco) | 1/1/1/1 | [S] |

Afirmaciones:
- **Remesa estructurada y automatización:** «Structured data is strongly preferred to allow automation». Solo puede venir estructurada o no estructurada, no ambas (https://eact.eu/Core/Images/EACT_PDFs/ISO-20022-Remittance-Content-Market-Guide-February-2022.pdf).
- **Documento referido:** «Referred Document Information should always be provided. In most cases, this would be the invoice number and date».
- **Importes del documento referido:** incluyen importe debido (`DuePyblAmt`), descuento aplicado (`DscntApldAmt`), nota de crédito (`CdtNoteAmt`), impuestos (`TaxAmt`) y importe remitido (`RmtdAmt`). Mejor práctica: «the total of the amounts in the referred document amount group should add up to the total amount remitted to fully explain the payment». Aclaración de la misma guía sobre `RmtdAmt`: «Although there is no arithmetic check, the other amounts in the “Document Amount” group should support the remitted amount».
- **Aplicación automática:** esa guía define cash application así: «Cash application refers to the process of posting a payment to the AR system and reconciling the amount paid to the amount due».
- **Remesa separada del pago:** cuando va aparte, hace falta un identificador de enlace: «A linking identifier is a single pre-determined (known) piece of data that brings two transactions together for reconciliation».
- **`RmtInf/Strd/CdtrRefInf`, literal (EPC):** la referencia es «Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction». Uso indicado: «If available, the initiating party should provide this reference in the structured remittance information, to enable reconciliation by the creditor upon receipt of the amount of money». Si el emisor (`Issr`) es «ISO», «RF Creditor Reference must be used (ISO 11649)».
- **ISO 11649, literal:** «The RF Creditor Reference is designed for use in an automated processing environment» y «a means to convey customer payment details in a machine-readable form. It also makes provision for validation of the RF Creditor Reference by making use of a computational check digit» (extracto de iTeh, [L]).
- **Formato RF** (solo [S], verificar contra la norma): `RF` + 2 dígitos de control + hasta 21 caracteres alfanuméricos, 25 en total (`2!a2!n21c`), con control MOD 97-10 según ISO/IEC 7064 (https://en.wikipedia.org/wiki/Creditor_Reference).
- **Validación en SEPA:** el banco receptor no está obligado a validar el dígito de control, y si lo valida y falla puede seguir procesando (EPC, `Reference`, #2.148).
- **`remt.001`:** «allows the originator to provide remittance details that can be associated with a payment», con etiqueta XML `RmtAdvc`. Fuente única y secundaria, y no habla de documentos referidos ni de importes (https://iotafinance.com/en/SWIFT-ISO20022-Message-remt-001-001-Remittance-Advice.html, [S]). La parte de documentos e importes la cubre la guía X9 sobre `RmtInf/Strd`.
- **camt.054:** solo [S]. Es el aviso de débito/crédito que el banco manda al titular y sirve para reconciliar. No leí su definición oficial (resultados de la búsqueda sobre BNY y Swift).
- **Cifra de un banco, dato de un solo proveedor:** NatWest dice que pasar a remesa estructurada y códigos de propósito lleva el auto-match a 88%, con 12% de excepciones ([S], https://www.natwest.com/corporates/insights/regulation/iso-20022-for-finance-teams.html). No es independiente.
- **Truncamiento:** Swift advierte que la información de remesa a menudo se trunca al pasar por las entidades financieras (resultado de la búsqueda, [S], https://swift.com/swift_resource/251967). Hay que diseñar para el caso en que la referencia llegue incompleta.

**Recurso canónico propuesto:** la guía X9 IR 01-2022 (elementos de `Strd`, ejemplos con factura, nota de crédito y descuento) más el extracto de ISO 11649 y las páginas de EPC sobre `CdtrRefInf`.

## 7. Intereses por mora

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Directiva 2011/7/UE (EUR-Lex; texto leído vía fetch con salida resumida) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32011L0007 | primaria | 3/2/1/3 | [S] (la herramienta devolvió síntesis; el HTML directo falló) |
| Comisión Europea, página sobre morosidad | https://single-market-economy.ec.europa.eu/smes/challenges-and-resilience/late-payment_en | primaria | 3/1/1/2 | [S] |
| SAP Help, cálculo de intereses sobre partidas (resultado del buscador) | https://help.sap.com/saphelp_globext607_10/helpdata/en/01/a9c652455711d182b40000e829fbfe/content.htm | primaria de producto | 2/2/2/2 | [S] |

Afirmaciones:
- **Derecho al interés:** «the creditor is entitled to interest for late payment without the necessity of a reminder» (art. 3(1), https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32011L0007, [S]). Condiciones: que el acreedor haya cumplido sus obligaciones y que no haya recibido el importe a tiempo, salvo que el deudor no sea responsable.
- **Desde cuándo corre:** art. 3(3)(a), desde «the day following the date or the end of the period for payment fixed in the contract». Si el contrato no fija plazo, art. 3(3)(b): «30 calendar days following the date of receipt by the debtor of the invoice or an equivalent request for payment».
- **Tope contractual:** art. 3(5), el plazo pactado no debe superar «60 calendar days», salvo pacto expreso y no abusivo para el acreedor.
- **Tasa legal:** «simple interest for late payment ... at a rate which is equal to the sum of the reference rate and at least eight percentage points» (artículo 2, definiciones). La herramienta numeró estos puntos como 2(5) a 2(7). No confío en esa numeración, citar «artículo 2, definiciones».
- **Costo de cobro:** art. 6(1), «a fixed sum of EUR 40».
- **Revisión pendiente:** la Comisión indica que prepara una revisión de la directiva (https://single-market-economy.ec.europa.eu/smes/challenges-and-resilience/late-payment_en, [S]). No verifiqué si hay un texto nuevo adoptado, así que confirmar antes de citar cifras como vigentes.
- **Qué implica para el modelo:** el interés se calcula sobre la partida y su vencimiento. En la práctica de SAP corre sobre partidas abiertas «always calculated as of the due date for net payment without taking into account any tolerance days», y se puede elegir calcular sobre partidas abiertas o sobre compensadas. Con partidas partidas, el tratamiento por defecto es una sola unidad (resultados del buscador, [S]). El interés entonces es una partida nueva, derivada de la original.

**Recurso canónico propuesto:** la Directiva 2011/7/UE leída en EUR-Lex (no pude obtener el literal con mis herramientas) y, como práctica, la página de cálculo de intereses de SAP.

## 8. Cómo falla el modelo

Esta sección salió de un solo bloque de búsquedas y no encontré una fuente que enumere los fallos. Lo que sigue combina lo citado arriba, con la inferencia marcada.

- **Saldo guardado aparte:** lo contradice Fowler, que lo deriva de los asientos y solo admite un caché. Si el saldo es un campo independiente se desincroniza de las partidas (https://martinfowler.com/eaaDev/Account.html). La conciliación contra la cuenta de control, que ya está documentada en otro tema, es la defensa.
- **Aplicar a cuenta (sin partida de destino):** es el comportamiento del saldo corriente. Oracle dice que los pagos «relieve the oldest debit first». Con partidas abiertas, el pago sin asignar queda como partida acreedora abierta, como el pago que SAP deja abierto en el modelo (a). Esto es lectura mía de las dos fuentes.
- **Diferencia de cambio sin registrar al aplicar:** no encontré una fuente que lo describa como falla. El foro de Odoo reporta un caso donde una conciliación parcial deja un residual que, al cerrarlo, genera dos asientos (ajuste manual más diferencia de cambio). Es el relato de un usuario, sin respuesta oficial (https://www.odoo.com/forum/help-1/reconciling-multi-currency-payments-cant-fully-log-exchange-difference-when-using-misc-type-journal-286697, [S]).
- **Remesa truncada o sin referencia:** Swift advierte que la información de remesa se trunca al pasar por entidades. EPC admite que el banco receptor no valide el dígito de control, así que la aplicación automática necesita una regla de reserva.
- **Notas de crédito:** el estándar de remesa de X9 las trata como un documento más en la misma remesa. Un modelo que solo asigna pagos a facturas queda sin dónde ponerlas.

## Recursos canónicos por componente

1. **Partidas abiertas / saldo corriente:** Oracle, «Open-Item Versus Balance-Forward Accounting», más la página de método por clase de cliente. Es práctica de producto, no teoría.
2. **Saldo derivado:** Fowler, «Account» y «Patterns for Accounting».
3. **Vencimientos y cuotas:** UBL 2.1 `PaymentTerms` (XSD) y Peppol BR-CO-25.
4. **Aplicación, desaplicación y netting:** sin un recurso canónico único. Mejor aproximación, SAP (compensación y residual) y la guía X9 (remesa con factura, nota de crédito y descuento).
5. **Multimoneda:** IAS 21 §§28-29.
6. **Remesa estructurada:** X9 IR 01-2022, EPC115-06 e ISO 11649.
7. **Mora:** Directiva 2011/7/UE (EUR-Lex), con SAP como práctica.

## Huecos

- **Libro de texto sobre open-item frente a balance-forward:** no encontré el pasaje de Romney y Steinbart ni de Hall. Lo más parecido fue un apunte de curso (Glendale) y documentación de producto. Hace falta el libro físico o un extracto verificable. Con la misma búsqueda apareció otra pista, un apunte de diapositivas sin autor verificado: el método de saldo corriente se asocia con cuenta por ciclo. Solo [S], no lo use sin verificar.
- **Cuándo conviene cada método:** solo tengo ejemplos de Oracle (residencial frente a industrial) y la asociación con la facturación cíclica. No hay criterio general en una fuente primaria.
- **Registro de aplicación como entidad (importe, fecha, desaplicación):** no hay fuente que lo formule como patrón. Lo que cito sale del comportamiento de SAP y la guía X9. Fowler no cubre la cuenta corriente: sus páginas no tratan facturas, cobros ni partidas abiertas. El cuerpo de `accounting.pdf` no se pudo leer.
- **Desaplicación (reversión de una aplicación):** no encontré documentación que la describa. Fowler tiene patrones de ajuste por reversión que podrían aplicarse (`Reversal Adjustment`, visibles en el índice de su PDF), pero no lo leí.
- **camt.054:** solo [S], sin definición oficial. `remt.001`: una sola fuente secundaria. El catálogo oficial de ISO 20022 devolvió 403.
- **ISO 11649 y la norma EN 16931:** el texto completo de ISO 11649 es de pago (leí el extracto público). EN 16931 no la leí, solo la rama de reglas publicada por Peppol (BR-CO-25 y BR-CO-16 son de Peppol sobre esa base).
- **IAS 21:** copia alojada en una universidad, sin año identificado. La página oficial de IFRS pide suscripción.
- **Directiva 2011/7/UE:** no pude leer el HTML literal de EUR-Lex. Las citas son síntesis de la herramienta y la numeración de los puntos del artículo 2 no es confiable. Hay una revisión de la directiva en trámite cuyo estado no verifiqué.
- **Netting entre cliente y proveedor:** solo resultados del buscador sobre SAP, sin lectura de página completa. Falta el tratamiento legal y contable de la compensación (por ejemplo, IAS 32 sobre compensación de activos y pasivos financieros). No lo busqué.
- **Fallos del modelo:** no hay fuente que los enumere. Es la sección más débil del informe.
- **Dos de tres rondas por componente se gastaron en casi todos.** El componente de aplicación y desaplicación tuvo una sola ronda de búsqueda, así que queda margen para una segunda antes de darlo por agotado.
