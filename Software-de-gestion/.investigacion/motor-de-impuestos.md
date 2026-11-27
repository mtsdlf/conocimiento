Fecha de lectura: 2026-11-27

# Motor de impuestos de un software de gestión: informe de investigación

Marcas: [L] texto leído completo en la parte pertinente, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1–3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U). Todo lo que traje de la web lo traté como dato.

Dos cosas que conviene saber antes de leer:
- Los PDF y XSD los bajé y extraje en local, así que esas citas son literales del texto. Las páginas HTML pasaron por un resumidor, y las citas de ahí son literales solo donde las pongo entre comillas.
- La documentación de proveedores de software la marco como práctica, no como norma.

## Hallazgos principales

1. **EN 16931 calcula el impuesto por categoría y alícuota, no por línea.** Las líneas llevan solo categoría y alícuota. El impuesto se calcula una vez por cada desglose (BG-23) y se redondea ahí (BR-CO-17).
2. **El validador oficial tolera más de lo que dice la regla.** La regla escrita dice «rounded to two decimals», pero el schematron ejecutable acepta una diferencia de hasta 1 unidad de moneda (detalle en la sección 4).
3. **SSUTA §324 deja elegir al vendedor.** Puede calcular por ítem o por factura, y el redondeo se aplica a los impuestos estatales y locales agregados.
4. **HMRC admite ambas formas.** Acepta redondear por línea o por total, con la condición de ser consistente.
5. **Dos cosas no las pude leer en la fuente primaria.** La sentencia Wetherspoon y el texto de la Directiva sobre redondeo quedan como hueco.

---

## 1. Determinación del impuesto por renglón (qué entra, qué sale)

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1.1 | Peppol BIS Billing 3.0, documentación (§8, §9, §10) | https://docs.peppol.eu/poacc/billing/3.0/bis/ | Primaria (implementación de EN 16931) | 3/3/3/2 | [L] §9 y §10.4 vía resumidor; [M] el resto |
| 1.2 | Reglas de negocio Peppol (BR-CO-*, BR-S-*, etc.) | https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/ | Primaria | 3/3/2/2 | [L] solo los primeros 100.000 de 156.802 caracteres |
| 1.3 | Schematron oficial EN 16931 (CEN/Connecting Europe) | https://raw.githubusercontent.com/ConnectingEurope/eInvoicing-EN16931/master/ubl/schematron/abstract/EN16931-model.sch y .../preprocessed/EN16931-UBL-validation-preprocessed.sch | Primaria (código de validación; última release `validation-1.3.17`, 2026-10-12) | 3/3/1/3 | [L] las aserciones citadas |

- **Entradas y salida por línea.** Cada línea lleva categoría de IVA, y la alícuota de cada línea salvo en la categoría O. Texto de la fuente:
  - «Each Invoice line (BG-25) shall be categorized with an Invoiced item VAT category code (BT-151).» (BR-CO-04, https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/)
  - La BIS §8.1 dice que cada línea lleva el código de categoría (BT-151) y la alícuota para toda categoría salvo O (https://docs.peppol.eu/poacc/billing/3.0/bis/).
- **No hay importe de impuesto por línea.** En el modelo EN 16931 la línea tiene categoría y alícuota, pero el importe de impuesto solo existe en el desglose por categoría. La conclusión sale de que BT-117 solo existe en BG-23 y de BR-S-08/09. No encontré una frase literal que lo afirme.
- **Un desglose por combinación.** «One VAT Breakdown shall be provided for each distinct combination of VAT category code and VAT rate» (https://docs.peppol.eu/poacc/billing/3.0/bis/, §10.4).
- **Valores iguales con distinta escritura.** La §8.3 de la BIS dice que alícuotas que difieren solo en ceros finales (25 y 25.00) dan un único desglose.
- **Base por categoría (BR-S-08):** «the VAT category taxable amount (BT-116) in a VAT breakdown (BG-23) shall equal the sum of Invoice line net amounts (BT-131) plus the sum of document level charge amounts (BT-99) minus the sum of document level allowance amounts (BT-92) where the VAT category code (BT-151, BT-102, BT-95) is "Standard rated" and the VAT rate (BT-152, BT-103, BT-96) equals the VAT category rate (BT-119).» (https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/)
- **Descuentos y cargos de cabecera entran en la base.** Cada uno lleva su propia categoría (BT-95, BT-102), como muestra el texto anterior.

Fecha del hecho imponible y lugar de origen y destino: EN 16931 solo modela la fecha del punto impositivo (BT-7/BT-8, mutuamente excluyentes, BR-CO-03). No modela la determinación del lugar. Eso es del motor y no del estándar.

**Recurso canónico:** BIS 3.0, §8 (VAT) y §10.4 (cálculo del IVA), más BR-S-08/09 y BR-CO-04. Fijarse en que el estándar solo agrega y no determina: el «de dónde sale la categoría» queda fuera del estándar.

## 2. Códigos/categorías fiscales de artículo y de sujeto

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 2.1 | Code list UNCL5305 (subconjunto Peppol), D.16B, release mayo 2026 | https://docs.peppol.eu/poacc/billing/3.0/codelist/UNCL5305/ | Primaria | 3/2/2/2 | [L] (los nombres de los códigos son literales; las descripciones del resumidor son parafraseadas) |
| 2.2 | BIS 3.0 §12 y reglas BR-S-05, BR-O-05, BR-AE-10 | https://docs.peppol.eu/poacc/billing/3.0/bis/ (offset 100000) | Primaria | 3/2/2/1 | [L] parcial |

Lista de códigos y nombres, literal de https://docs.peppol.eu/poacc/billing/3.0/codelist/UNCL5305/:
- AE «Vat Reverse Charge»
- B «Transferred (VAT), In Italy» (solo Italia, desviación A de EN 16931)
- E «Exempt from Tax»
- G «Free export item, VAT not charged»
- K «VAT exempt for EEA intra-community supply of goods and services»
- L «Canary Islands general indirect tax»
- M «Tax for production, services and importation in Ceuta and Melilla»
- O «Services outside scope of tax»
- S «Standard rate»
- Z «Zero rated goods»

**Discrepancia entre las dos páginas de Peppol** (ambas literales):
- El codelist dice G «Free export item, VAT not charged».
- La tabla 14 de la BIS dice «G | Free export item, tax not charged».
- Y los nombres de las reglas BR-* usan «Standard rated» y «Exempt from VAT», mientras que el codelist usa «Standard rate» y «Exempt from Tax». Son nombres distintos del mismo código.

Reglas sobre la alícuota según la categoría (resumen de la fuente, https://docs.peppol.eu/poacc/billing/3.0/bis/):
- BR-S-05: en categoría S la alícuota del renglón es mayor que cero.
- En Z, E, G y K la alícuota es 0.
- BR-O-05: una línea O «shall not contain an Invoiced item VAT rate».
- Importes de impuesto en cero: Z BR-Z-09 «shall equal 0 (zero)», E BR-E-09, AE BR-AE-09 «shall be 0 (zero)», K/IC BR-IC-09, O BR-O-09 (https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/).

La categoría de sujeto (condición fiscal de la parte) y la «taxabilidad» de producto no tienen lista en el estándar. En EE. UU. el análogo es la Taxability Matrix de SSUTA (ver sección 5).

**Recurso canónico:** el codelist UNCL5305 en Peppol y, de la BIS, la tabla de reglas BR-S/Z/E/AE/IC/G/O. Fijarse en que la categoría combina cuatro cosas distintas: tasa estándar, tasa cero, exención y mecanismo (inversión, intracomunitaria).

## 3. Reglas por jurisdicción con vigencia, límites, certificados de exención

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 3.1 | SSUTA, amended through May 20, 2025 (PDF) | https://www.streamlinedsalestax.org/docs/default-source/agreement/ssuta/ssuta-as-amended-through-05-20-25-with-hyperlinks-and-compiler-notes-at-end.pdf | Primaria | 3/3/2/3 | [L] las secciones citadas (texto extraído con `pdftotext`) |

Citas literales (SSUTA, Section 305, subsecciones A.1 a A.7, C y D):
- **Vigencia de cambios locales:** «Provide that local rate changes will be effective only on the first day of a calendar quarter after a minimum of sixty days' notice to sellers.»
- **Cambios de límites:** «apply local jurisdiction boundary changes only on the first day of a calendar quarter after a minimum of sixty days' notice to sellers.»
- **Base de límites:** «Provide and maintain a database that describes boundary changes for all taxing jurisdictions. This database shall include a description of the change and the effective date of the change for sales and use tax purposes.»
- **Base de alícuotas:** «Provide and maintain a database of all sales and use tax rates for all of the jurisdictions levying taxes within the state.» Los códigos son FIPS para estados, condados, ciudades y parroquias.
- **Asignación por código postal:** «Provide and maintain a database that assigns the proper tax rates and jurisdictions to each five-digit and nine-digit zip code within a member state.»
- **Conflicto dentro de un código postal:**
  - Nueve dígitos con más de una alícuota: «the state must assign the lowest combined tax rate».
  - Cinco dígitos: el estado puede asignar la más alta, la más baja o una combinada.
- **Opción address-based (A.7)** y, en C, bases address-based de proveedores certificadas por el estado.
- **Plazo de publicación (D):** las bases deben estar «available to a seller or CSP by the first day of the month prior to the first day of a calendar quarter».
- **Efecto de las tasas en servicios facturados por período (§329):** «For a rate increase, the new rate shall apply to the first billing period starting on or after the effective date. For a rate decrease, the new rate shall apply to bills rendered on or after the effective date.»
- **Certificados de exención:** la §317 trata la administración de exenciones, en particular los certificados. Solo la ubiqué (línea 1334 del texto) y no la leí entera, así que no cito de ella.

Otras fuentes buscadas sin éxito para esta parte: no leí normativa de vigencia de alícuotas fuera de EE. UU. (ver huecos).

**Recurso canónico:** SSUTA §305 y §306 completas y §329. Fijarse en la regla de calendario trimestral con 60 días de aviso y en que la vigencia es una propiedad del dato (alícuota y límite) y no del cálculo.

## 4. Redondeo: por línea, por categoría o por total

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 4.1 | BIS 3.0 §9 «Rounding» y §10.2 y §10.4 | https://docs.peppol.eu/poacc/billing/3.0/bis/ | Primaria | 3/3/3/2 | [L] vía resumidor |
| 4.2 | BR-CO-13 a 17 | https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/ | Primaria | 3/3/2/2 | [L] |
| 4.3 | Schematron EN 16931 (aserciones BR-CO-14, BR-CO-15, BR-CO-17) | ver 1.3 | Primaria | 3/3/1/3 | [L] |
| 4.4 | HMRC VAT Notice 700, §17.5, §17.5.1, §17.5.2, §17.6 | https://www.gov.uk/guidance/vat-guide-notice-700 | Primaria (guía del fisco) | 3/2/2/3 | [L] §17.5 a §17.6 (HTML bajado y leído en local) |
| 4.5 | SSUTA §324 | ver 3.1 | Primaria | 3/2/1/3 | [L] |
| 4.6 | Directiva 2006/112/CE; sentencia C-302/07 | ver huecos | Primaria (no leída) | — | [S] |

### 4.1 Qué dice EN 16931 / Peppol

Sección «9 Rounding» de la BIS, literal (https://docs.peppol.eu/poacc/billing/3.0/bis/):
- «To minimize the risk of differences due to rounding, the following rules apply.»
- «All document level amounts shall be rounded to two decimals for accounting»
- «Invoice line net amount shall be rounded to two decimals»
- «Results from calculations involving already rounded amounts are not subject to rounding»
- Sobre el importe neto de línea (§10.2.2): «the different parts of the calculation must be rounded separately».

Reglas de totales, literales (https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/):
- BR-CO-10: «Sum of Invoice line net amount (BT-106) = Σ Invoice line net amount (BT-131).»
- BR-CO-14: «Invoice total VAT amount (BT-110) = Σ VAT category tax amount (BT-117).»
- BR-CO-15: «Invoice total amount with VAT (BT-112) = Invoice total amount without VAT (BT-109) + Invoice total VAT amount (BT-110).»
- BR-CO-16: «Amount due for payment (BT-115) = Invoice total amount with VAT (BT-112) -Paid amount (BT-113) +Rounding amount (BT-114).»
- BR-CO-17: «VAT category tax amount (BT-117) = VAT category taxable amount (BT-116) x (VAT category rate (BT-119) / 100), rounded to two decimals.»

Consecuencia de diseño: el impuesto se redondea **una vez por categoría y alícuota** (BR-CO-17), y el total es la suma de esos redondeos (BR-CO-14). No hay redondeo por línea del impuesto, porque la línea no tiene importe de impuesto. Si el ERP calcula impuesto por línea, la suma de las líneas puede no coincidir con BT-117. Esa conclusión es mía, sacada de las reglas.

**Hallazgo sobre el validador oficial.** En el schematron preprocesado, la aserción BR-CO-17 compara así: `abs(TaxAmount) - 1 < round(abs(TaxableAmount) * (Percent div 100) * 10 * 10) div 100` y `abs(TaxAmount) + 1 > ...` (https://raw.githubusercontent.com/ConnectingEurope/eInvoicing-EN16931/master/ubl/schematron/preprocessed/EN16931-UBL-validation-preprocessed.sch, línea 225 de mi copia). Leído literalmente, el validador acepta cualquier importe a menos de 1 unidad de moneda del valor teórico, no a menos de 1 centavo. La regla escrita («rounded to two decimals») es más estricta que su implementación. Lo leí en el código y no encontré documentación que lo explique. Vale la pena verificarlo con un caso de prueba antes de afirmarlo en la base.

### 4.2 Qué dicen las normas fiscales

- **Reino Unido, HMRC Notice 700** (https://www.gov.uk/guidance/vat-guide-notice-700):
  - §17.5: «You may round down the total VAT payable on all goods and services shown on a VAT invoice to a whole penny. You can ignore any fraction of a penny.» La concesión es «designed for invoice traders».
  - §17.5.1, redondeo por línea: se calcula el IVA de la línea redondeando «down to the nearest 0.1 pence» o «to the nearest 1 pence or 0.5 pence». Luego: «Whatever you decide, you must be consistent.» y «The final total amount of VAT payable may be rounded down to the nearest whole penny.»
  - §17.5.2, por unidad o artículo (listas de precios): 4 decimales y redondear a 3, o al 1 o 0,5 penique más cercano. En el segundo caso, «you must not round the VAT down to 'nil'» en artículos de tasa estándar o reducida.
  - §17.6, minoristas: «If you calculate VAT at line level or invoice level, you must not round the VAT figure down. But, you may round (up and down) each VAT calculation.»
  - Es decir, HMRC admite línea o factura, con consistencia. Hay una asimetría: el redondeo hacia abajo es una concesión para quien factura, y en el minorista no se puede.
- **EE. UU., SSUTA §324** (https://www.streamlinedsalestax.org/docs/default-source/agreement/ssuta/ssuta-as-amended-through-05-20-25-with-hyperlinks-and-compiler-notes-at-end.pdf), literal:
  - «A. After December 31, 2005, each member state shall adopt a rounding algorithm that meets the following criteria: 1. Tax computation must be carried to the third decimal place, and 2. The tax must be rounded to a whole cent using a method that rounds up to the next cent whenever the third decimal place is greater than four.»
  - «B. Each state shall allow sellers to elect to compute the tax due on a transaction on an item or an invoice basis, and shall allow the rounding rule to be applied to the aggregated state and local taxes. No member state shall require a seller to collect tax based on a bracket system.»
  - Consecuencia: el motor debe soportar por ítem y por factura, y aplicar el redondeo sobre el impuesto agregado estado más local.
- **UE, Directiva 2006/112/CE:** una búsqueda secundaria dice que la Directiva es silente sobre el redondeo y que lo deja al nivel nacional. Es [S] y no la verifiqué en el texto. Ver huecos.
- **Finlandia** (cita secundaria de un resultado de buscador): afirma que no se puede redondear línea por línea, sino sobre el total por alícuota. No la verifiqué y no es primaria. Si es cierta, discrepa de HMRC y SSUTA, y vale la pena confirmarla en la fuente de la autoridad fiscal finlandesa.

**Discrepancia entre fuentes (resumen):**
- EN 16931: redondeo por categoría y alícuota, con total como suma.
- HMRC: línea o factura, a elección y de forma consistente.
- SSUTA: ítem o factura, a elección del vendedor.
- Finlandia [S]: por total de alícuota, no por línea.

**Recurso canónico:** BIS §9 y BR-CO-14/17, junto con HMRC §17.5.1 y SSUTA §324B. Fijarse en la diferencia entre redondear el impuesto de cada línea y el de cada categoría, y en quién elige.

## 5. Cómo un estándar modela el impuesto en línea y documento

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 5.1 | OASIS UBL 2.1, esquema `UBL-CommonAggregateComponents-2.1.xsd` | http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd | Primaria (estándar) | 3/3/1/3 | [L] definiciones extraídas del XSD |
| 5.2 | OASIS UBL 2.1 spec principal (HTML) | https://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html | Primaria | 3/1/1/1 | [M] solo el frente (se cortó en §2.13) |
| 5.3 | Peppol, sintaxis `cac:TaxTotal` | https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-TaxTotal/ | Primaria | 3/2/2/2 | [L] parcial |
| 5.4 | Vertex, VRBL (guía de e-invoicing) | https://developer.vertexinc.com/einvoicing/docs/tax | Práctica de proveedor | 1/1/2/1 | [L] parcial |

Definiciones literales del XSD de UBL 2.1 (la extracción automática puede mezclar la definición con la del elemento vecino, y las de abajo son las que coinciden con el contexto):
- **TaxTotal/TaxAmount:** «The total tax amount for a particular taxation scheme, e.g., VAT; the sum of the tax subtotals for each tax category within the taxation scheme.»
- **TaxTotal/RoundingAmount:** «The rounding amount (positive or negative) added to the calculated tax total to produce the rounded TaxAmount.»
- **TaxTotal/TaxIncludedIndicator:** «An indicator that tax is included in the calculation (true) or not (false).» Es el bit que modela «impuesto incluido en el precio».
- **TaxSubtotal/TaxableAmount:** «The net amount to which the tax percent (rate) is applied to calculate the tax amount.»
- **TaxSubtotal/CalculationSequenceNumeric:** «The number of this tax subtotal in the sequence of subtotals corresponding to the order in which multiple taxes are applied. If all taxes are applied to the same taxable amount (i.e., their order of application is inconsequential), then CalculationSequenceNumeric is 1 for all tax subtotals applied to a given amount.» Es el mecanismo de UBL para **impuesto sobre impuesto**.
- **TaxSubtotal/Percent:** «The tax rate of the tax category applied to this tax subtotal, expressed as a percentage.»
- **TaxSubtotal/PerUnitAmount y BaseUnitMeasure:** soporte para impuestos por unidad.
- **TaxSubtotal/TierRange:** «Where a tax is tiered, the range of taxable amounts that determines the rate of tax applicable to this tax subtotal.» Es soporte para impuestos escalonados.
- **TaxCategory** lleva ID, Name, Percent, TaxExemptionReasonCode y TaxExemptionReason.

Cómo lo restringe EN 16931 (https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-TaxTotal/):
- `cac:TaxTotal` tiene cardinalidad 1..2. «When tax currency code is provided, two instances of the tax total must be present, but only one with tax subtotal.»
- `cac:TaxSubtotal` es 0..n y es el desglose de IVA (BG-23).
- Regla PEPPOL-EN16931-R054: «Only one tax total without tax subtotals MUST be provided when tax currency code is provided.»

En la línea, la categoría clasificada va en `Item/ClassifiedTaxCategory`. El resultado de búsqueda de OASIS indica que un ticket (UBL-403, https://issues.oasis-open.org/browse/UBL-403) pregunta si hay redundancia entre esa ruta y `TaxTotal/TaxSubtotal/TaxCategory` a nivel de línea. Solo vi el título y el resumen, no la discusión [S].

Vertex (práctica, no norma): modela la línea con `ClassifiedTaxCategory`, con el código de categoría como obligatorio y la alícuota (Percent) como opcional. Sobre cómo se pasa de líneas a subtotales: «The page does not explain how document-level TaxSubtotal values are calculated from invoice lines», según el resumidor. No sirve como fuente de la derivación.

Dónde queda lo que EN 16931 no modela (conclusión mía, no cita): impuesto sobre impuesto y escalonados existen en UBL pero EN 16931 solo usa el IVA con un único nivel. Para esa parte no hay fuente leída que lo afirme textualmente, y queda como hipótesis a verificar.

**Recurso canónico:** el XSD de UBL 2.1 (TaxTotal, TaxSubtotal, TaxCategory) para el vocabulario completo, y el ejemplo de la BIS §10.4 (líneas S/25% agrupadas en un TaxSubtotal y E/0% en otro) para el mapeo línea a documento.

## 6. Impuesto incluido frente a agregado; impuesto sobre impuesto

Lo que tengo con fuente:
- UBL modela explícitamente `TaxIncludedIndicator` y `CalculationSequenceNumeric` (ver sección 5, https://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd).
- HMRC §17.5.2 menciona el cálculo del impuesto «per unit or per article (for example, for use in price lists)», que es el caso de precios publicados (https://www.gov.uk/guidance/vat-guide-notice-700).
- EN 16931 usa precio neto de IVA en el renglón («Item net price»), y el importe de línea se redondea a dos decimales (BIS §9).

No encontré ninguna fuente primaria que defina la conversión de un precio con impuesto incluido a base más impuesto (la «cuenta hacia atrás»). Es hueco.

## 7. Motor interno frente a servicio externo

Lo que dice SSUTA (https://www.streamlinedsalestax.org/docs/default-source/agreement/ssuta/ssuta-as-amended-through-05-20-25-with-hyperlinks-and-compiler-notes-at-end.pdf), literal:
- **CAS (§202):** «Software certified under the Agreement to calculate the tax imposed by each jurisdiction on a transaction, determine the amount of tax to remit to the appropriate state, and maintain a record of the transaction.»
- **CSP (§203):** «An agent certified under the Agreement to perform the seller's sales and use tax functions as outlined in the contract between the Streamlined Sales Tax Governing Board and the Certified Service Provider, other than the seller's obligation to remit tax on its own purchases.»
- **Modelos:** §205 define el «Model 1 seller» como el que eligió un CSP como agente. Solo leí el comienzo de la definición.
- **Relación con la responsabilidad (§306 A):** el estado releva a vendedores y CSP «from liability to the member state and local jurisdictions for having charged and collected the incorrect amount of sales or use tax resulting from their reliance on erroneous data provided by a member state on tax rates, boundaries, or taxing jurisdiction assignments.»
- **Relevo por la matriz de taxabilidad (§328 C):** relevo equivalente cuando se confía en datos erróneos de la sección «Library of Definitions» de la matriz.
- **Reembolso al cliente (§325 D):** el vendedor se presume de práctica comercial razonable si usa «either a provider or a system, including a proprietary system, that is certified by the state».
- **Certificación de proveedores de bases address-based (§305 C):** «Certification by the Governing Board does not replace the requirement that the databases be certified by the states individually.»

Esto responde la pregunta del encargo: el estándar permite motor propio certificado, proveedor certificado (CSP) o base certificada de proveedor, y la liberación de responsabilidad depende de usar las bases oficiales.

Lo que no leí: la certificación de CAS/CSP en detalle (el Apéndice E, «CSP CAS certification process», figura en los resultados de búsqueda pero no lo abrí). Práctica de proveedores de software de gestión: no la investigué más allá de Vertex.

**Recurso canónico:** SSUTA §202, §203, §205, §305 a §307 y §325 D. Fijarse en que la responsabilidad pasa al estado solo por confiar en sus bases oficiales, y en que la elección entre motor interno y servicio externo es una decisión de quién carga con el error.

---

## Recursos canónicos por componente (resumen)

| Componente | Recurso | Parte | En qué fijarse |
|---|---|---|---|
| Determinación por renglón | Peppol BIS 3.0 | §8, §10.4, BR-CO-04, BR-S-08/09 | El estándar solo agrega, no determina |
| Códigos fiscales | UNCL5305 en Peppol | codelist completo | Cuatro cosas mezcladas en un código |
| Reglas por jurisdicción | SSUTA | §305, §306, §329 | Vigencia trimestral, 60 días, base de límites y alícuotas |
| Redondeo | BIS §9, HMRC 700, SSUTA §324 | BR-CO-14/17, §17.5.1, §324B | Quién elige y a qué nivel |
| Modelo en estándar | UBL 2.1 CAC XSD | TaxTotal, TaxSubtotal, TaxCategory | `TaxIncludedIndicator`, `CalculationSequenceNumeric` |
| Motor interno o externo | SSUTA | §202, §203, §306, §325 D | Liberación de responsabilidad |

## Huecos

- **Directiva 2006/112/CE y redondeo.** No pude leer el texto. Una búsqueda secundaria indica que la Directiva no regula el redondeo y lo deja a los Estados. Falta la cita literal de EUR-Lex. Mi intento de bajar el texto de EUR-Lex por `curl` devolvió un archivo vacío.
- **Sentencia C-302/07, J D Wetherspoon (5 marzo 2009).** Los dos sitios (BAILII) dieron 403. Solo tengo resúmenes secundarios: reafirma la discreción de los Estados sobre el sistema de redondeo y remite a Ahold. No tengo el texto del fallo ni su cita literal.
- **Finlandia.** La afirmación «no se puede redondear línea por línea» viene de un fragmento de buscador y no la verifiqué.
- **Guía OCDE International VAT/GST Guidelines.** No la busqué, por el tope de rondas y porque no vi indicio de que aporte al motor. Sigue sin cubrir.
- **Texto oficial de EN 16931-1.** La norma CEN es de pago. Usé como proxy las reglas y el schematron publicados, que son oficiales pero no son el texto de la norma.
- **Validador BR-CO-17 y su tolerancia de 1 unidad.** Es una lectura mía del schematron, sin documentación que la confirme. Hay que probarlo con un caso real.
- **Componentes que quedaron sin fuente primaria:**
  - Impuesto incluido en el precio, la fórmula de la cuenta hacia atrás.
  - Impuesto sobre impuesto en la práctica.
  - Certificados de exención: solo ubiqué SSUTA §317 sin leerla.
  - Códigos de taxabilidad de producto fuera de EE. UU.
  - Documentación técnica de ERP (solo una página de proveedor, sin información sobre redondeo).
  - Lugar de la operación: queda en el tema tributario existente, como indicaste.
- **Peppol, categorías.** La página de reglas se leyó solo hasta el carácter 100.000 de 156.802, así que quedan sin ver las reglas del último tercio (probablemente las BR-IC, BR-IG, BR-IP, BR-G y BR-O restantes). Las citas de BR-IC/G/O de arriba salieron de lo que sí leí.
- **UBL 2.1.** El HTML de la especificación principal quedó en [M]. Las definiciones vienen del XSD. No leí las reglas de cardinalidad de línea (`InvoiceLine/TaxTotal`).

## Archivos

Escribí en el scratchpad copias descargadas para extracción (no son entregables): `/tmp/claude-1000/-home-dela-repos-personal-conocimiento/cfb247c6-67ae-4161-949e-87e8ed3a86d4/scratchpad/ssuta/ssuta.txt` y archivos en `.../scratchpad/w/` (`cac.xsd`, `model.sch`, `ubl.sch`, `n700.html`). No se escribió nada en el repo.
