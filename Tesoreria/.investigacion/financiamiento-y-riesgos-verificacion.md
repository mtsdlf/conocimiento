# Verificación de Financiamiento y Riesgos financieros (segunda pasada, 2026-11-27)

Marcas: [L] leído en el texto; [M] leído en un resumen o en una reseña; [S] solo en el resultado de un buscador. La búsqueda web se agotó a mitad de la pasada (límite de la sesión), así que lo que sigue sin fuente puede deberse a eso.

## Resuelto

### Costo financiero total (BCRA)
- [L] BCRA, texto ordenado Tasas de interés en las operaciones de crédito, al 01/07/2024 (última comunicación incorporada A 8057): https://www.bcra.gob.ar/Pdfs/Texord/t-tasint.pdf
  - 3.2: en todas las operaciones, los documentos dejan constancia de la tasa nominal anual pactada, la efectiva anual, si es fija o variable y el CFT (3.2.4).
  - 3.4.1: el CFT se expresa como tasa efectiva anual, «agregando a la tasa de interés el efecto de las comisiones y cargos asociados a la operación, cualquiera sea su concepto».
  - 3.4.2 computan: cuotas sociales de cooperativas, comisiones de intermediación inmobiliaria sobre el valor de plaza, seguros exigidos como condición, gastos de apertura y mantenimiento de cuentas y tarjetas asociadas, tasación, envío postal, IVA sobre intereses si el prestatario es consumidor final.
  - 3.4.3 no computan: comisiones por acuerdos de utilización de fondos como adelantos en cuenta corriente, si responden estrictamente a la asignación y no al capital usado (3.4.3.1); impuestos sobre préstamos prendarios y personales y otros; tasas de reparticiones públicas; honorarios de escribanía dentro del valor de plaza; impuesto sobre los intereses y el costo financiero del endeudamiento empresario (3.4.3.5).
- [L] BCRA, texto ordenado Protección de los usuarios de servicios financieros, al 06/05/2026 (A 8433), 2.3.3: si falta la tasa o el CFT en los documentos, el máximo es la tasa promedio de plazo fijo de 30 a 59 días; el CFT considera tasa, comisiones y cargos vigentes al contratar. https://www.bcra.gob.ar/Pdfs/Texord/t-pusf.pdf
- Corrección: la nota no decía que la comisión de acuerdo de adelanto en cuenta corriente queda fuera del CFT. Ahora lo dice. El «con y sin impuestos» de la nota anterior no está en la norma leída; el IVA entra solo para consumidor final.
- Ambos documentos son del BCRA: una sola fuente institucional en dos textos.

### Enmienda del IASB de 2023 a la NIC 7 y la NIIF 7
- [L] Anexo de la Comisión Europea que reproduce el texto del IASB (Council doc. 5621/24 ADD 1, 16/01/2024): https://data.consilium.europa.eu/doc/document/ST-5621-2024-ADD-1/en/pdf
  - NIC 7 44F: revelar información que permita evaluar los efectos en pasivos, flujos de efectivo y riesgo de liquidez.
  - 44G: definición; se llama también supply chain finance, payables finance o reverse factoring; las garantías y las tarjetas de crédito quedan afuera.
  - 44H: (a) términos y condiciones; (b) al inicio y cierre, valor en libros de los pasivos del acuerdo y de los ya cobrados por proveedores, y rango de vencimientos frente a cuentas a pagar comparables; (c) cambios que no mueven caja.
  - 62: vigente para ejercicios anuales desde el 1 de enero de 2024, aplicación anticipada permitida. 63: el primer año no exige comparativos, 44H(b)(ii)-(iii) al inicio del ejercicio, ni períodos intermedios.
  - NIIF 7, 44JJ y B11F(j): tener acceso a estos acuerdos es un factor al revelar el riesgo de liquidez.
- [M] EY, misma enmienda: fecha de vigencia 1 de enero de 2024 y el objetivo. https://www.ey.com/en_gl/technical/ifrs-technical-resources/iasb-amendments-to-ias-7-and-ifrs-7-for-supplier-finance-arrangements
- Corrección: la nota decía que la enmienda rige «desde 2023» en dos lugares; la emisión fue en mayo de 2023 y rige desde los ejercicios de 2024. «Pide revelar, no reclasificar» queda confirmado en el sentido de que los párrafos agregados son solo de revelación.
- No se pudo abrir el texto del IASB (suscripción). No se leyó el FASB ASU 2022-04.

### Carillion, informe parlamentario
- [L solo el resumen, págs. 3-4] Informe conjunto HC 769, publicado el 16/05/2018, copia en https://mcguinnessinstitute.org/wp-content/uploads/2020/04/Business-Energy-and-Industrial-Strategy-and-Work-and-Pensions-Committees-2018.pdf
  - Cita literal confirmada: «The mystery is not that it collapsed, but that it lasted so long.»
  - Liquidación en enero de 2018 con pasivos de casi £7.000 millones y £29 millones en caja; debía unos £2.000 millones a 30.000 proveedores, subcontratistas y otros acreedores de corto plazo, «a notorious late payer»; pasivo de pensiones de unos £2.600 millones.
- Sigue abierto: el capítulo sobre las cuentas (reverse factoring, £498 millones, 4 meses). publications.parliament.uk devolvió 403 por curl y WebFetch. Esas cifras siguen en Moody's vía CFO.com.

### Fórmula de la tasa efectiva y cuota fija
- [L] OpenStax, Principles of Finance, 8.4 https://openstax.org/books/principles-finance/pages/8-4-stated-versus-effective-rates: EAR = (1 + i)^n − 1; tarjeta 1,5% mensual da 19,56% contra 18% (recalculado: 1,015^12 − 1 = 19,5618%).
- [L] OpenStax 8.3 https://openstax.org/books/principles-finance/pages/8-3-loan-amortization: PMT = PV ÷ ([1 − 1/(1+r)^n]/r); préstamo de USD 32.000 al 6% a 3 años: cuota 973,50, interés del mes 1 de 160,00, interés total 3.046,08 (recalculado: 973,5020; 160,00; 3.046,07; diferencia de redondeo). No trata cuota de capital constante.
- Reemplazan a Wikipedia (Effective interest rate, Fixed-rate mortgage).

### Forward, futuros, cobertura natural, exposiciones
- [L] OpenStax 20.3 https://openstax.org/books/principles-finance/pages/20-3-exchange-rates-and-risk: transaction, translation y economic risk; forward «a contractual agreement between two parties to exchange a specified amount of currencies», contrato individualizado, «only as good as the promise of the counterparty»; futuros «standardized contracts» con tamaños y vencimientos fijos; cobertura natural «offset its risk simply through its own operations». No dice «over the counter» ni liquidación diaria; eso sigue en Wikipedia.

### Riesgo de tasa y de liquidez
- [L] OpenStax 20.4 https://openstax.org/books/principles-finance/pages/20-4-interest-rate-risk: el riesgo de tasa se define sobre bonos; con un canje de tasas, el que paga variable enfrenta tasas que fluctúan y el que fija gana previsibilidad. No cubre topes (caps) ni la cuota que sube con la tasa. Resuelve en parte la nota «sin fuente».
- [L] NIIF 7 B11F (anexo europeo, arriba): líneas comprometidas, fondeo diverso, concentraciones, controles internos y planes de contingencia, como factores de riesgo de liquidez. Segunda fuente para las mitigaciones que lista Wikipedia.

### Préstamo con garantía de activos: línea rotativa y covenants
- [L en las secciones de línea rotativa, covenants y glosario] OCC, Comptroller's Handbook, Asset-Based Lending v1.1 (2017) https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/pub-ch-asset-based-lending.pdf
  - Línea rotativa: retirar, devolver y volver a retirar; tope = el menor entre la base de garantía y el monto comprometido; plazo típicamente corto, en algunos casos hasta cinco años. No habla de comisión por no uso ni de línea comprometida o no comprometida.
  - Covenants: ratios «as an ongoing condition of credit», «default triggers»; mantenimiento (se mide cada período, por lo general trimestral) e incurrencia (se prueba al pagar dividendos, comprar o endeudarse más). En préstamos con garantía de activos el covenant financiero típico es la cobertura mínima de cargos fijos; el límite de 5 veces el flujo de caja es solo un ejemplo del glosario.
  - Es un manual de supervisión de Estados Unidos y de préstamos con garantía de activos, no de préstamos a plazo en general.

### Leasing (NIIF 16)
- [M] IASB, página de la NIIF 16 https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/: el tomador reconoce un activo por derecho de uso y un pasivo por arrendamiento en los arrendamientos de más de 12 meses, salvo bien de bajo valor; vigente desde el 01/01/2019; reemplaza a la NIC 17, la CINIIF 4 y las SIC 15 y 27. El texto de la norma exige suscripción.

### Calce de plazos
- [L] OpenStax 19.1 https://openstax.org/books/principles-finance/pages/19-1-what-is-working-capital: lista líneas de crédito, préstamos bancarios de corto plazo y préstamos sobre inventario como financiamiento externo, y dice que una base permanente de capital de trabajo «may need to be financed with longer-term sources of capital». Apoyo parcial, la regla no está enunciada. 19.2: el costo anual de renunciar al descuento 2/10 neto 30 es 36,73%. 19.4 no trata factoring ni recurso.

## Sigue abierto
- Greensill (fecha de insolvencia, USD 140 millones de Credit Suisse, aseguradoras, USD 4.600 millones, USD 10.000 millones congelados): solo Wikipedia. Se intentó Reuters, Bloomberg, The Guardian, The New York Times, The Wall Street Journal (WebFetch no puede abrirlos o devuelven 401 o 403) y el Comité del Tesoro (403). URLs que remite Wikipedia, p. ej. https://www.reuters.com/article/us-britain-greensill-idUSKBN2B01WB.
- S&P Global (noviembre de 2021) devolvió 403; la nota de la Manchester Metropolitan University sobre Prem Sikka, 404.
- Descubierto, factoring con y sin recurso y con y sin notificación, descuento de facturas, comisión por no uso, línea comprometida contra no comprometida: sin fuente buena. OpenStax 19.2 y 19.4 no los tratan. Páginas de la ACT y de FCI probadas dieron 404. Falta, por ejemplo, un manual de asociación de factoring o una guía de la ACT o de la AFP.
- Ecuación de Fisher: OpenStax no la trata (1.6, 17.2 y 10.4 no la incluyen). Sigue con Wikipedia; es matemática estándar.
- Covenants: OpenStax 10.1 y 17.2 no los tratan. Sigue la clasificación de tres clases (de hacer, de no hacer, financieros) solo en Wikipedia.
- Jin y Jorion (2006): solo el abstract; el artículo está en una revista con suscripción.
- Cobertura cambiaria en pymes: la reseña de Duke remite a un documento de SSRN que devolvió 403; no se pudieron buscar los estudios originales por el límite de búsquedas.
- FASB ASU 2022-04 no leída.
- Descuento de documentos como mecanismo general: sin fuente.
