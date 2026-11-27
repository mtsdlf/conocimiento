# Tesorería, segunda ronda: proyección de caja, posición, reserva, crédito, cobranza y aplicación de cobros

Fecha de lectura: 2026-11-27. Capa cruda. Complementa `caja-y-liquidez.md` y `credito-y-cobranzas.md` (no repite lo que ya tienen). Marcas: [L] leído lo citado; [M] metadatos o abstract; [S] resumen secundario o del buscador. Las páginas web pasan por un extractor que resume y devuelve citas cortas; el PDF de CRF se bajó y se leyó como texto con `pdftotext` (es la única lectura textual completa de esta ronda). El cupo de búsqueda web se agotó tras tres búsquedas: las cinco C, el límite de crédito, las garantías, los firmantes y el cash pooling quedan sin fuente.

## Resumen de lo que se logró

- Mejor hallazgo: la guía de medidas de la Credit Research Foundation (primaria, texto completo), con las fórmulas literales de CEI, DSO, DSO mejor posible, días de atraso promedio, porcentaje corriente y porcentaje a más de 91 días. Cierra el hueco 6 en lo central.
- Proyección de caja: solo fuentes de proveedores de software y una de Wikipedia que cita a AFP; el origen en reestructuraciones lo dice una sola fuente comercial. Sin fuente primaria.
- Reserva de liquidez: motivos de Keynes por Wikipedia (secundaria); motivo de precaución con evidencia en Bates, Kahle y Stulz [M]. Reglas de «meses de gastos»: no se encontró fuente; no se afirman.
- Sin fuente: cinco C, cálculo de límite, garantías, firmantes y poderes, cantidad de bancos, cash pooling, secuencia de recordatorios con plazos, cobros sin identificar, deducciones y disputas como práctica.

## Tabla de fuentes

| # | Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|---|
| 1 | Credit Research Foundation, *Performance Measures* (PDF, creado 2016-10-07) | https://www.crfonline.org/wp-content/uploads/2017/12/PerformanceMeasures.pdf | primaria (asociación profesional de gestores de crédito) | 3/2/1/3 | [L] |
| 2 | Wikipedia, Cash flow forecasting (cita a de Caux 2005, Bort 1990 y AFP 2006) | https://en.wikipedia.org/wiki/Cash_flow_forecasting | secundaria (último recurso) | 1/2/1/1 | [S] |
| 3 | Upflow, 13-Week Cash Flow Forecast (blog de un vendedor de software de cobranzas; cita a Wall Street Prep, Cherry Bekaert, AFP, PwC) | https://upflow.io/blog/cfo-reads/13-week-cash-flow-forecast | secundaria, comercial | 1/2/2/1 | [S] |
| 4 | Stampli, What is a 13-week cash flow forecast (vendedor de software) | https://www.stampli.com/resources/13-week-cash-flow-forecast/ | secundaria, comercial | 1/1/1/1 | [S] |
| 5 | Wikipedia, Float (money supply) (cita a Federal Reserve Bank of New York, *Fedpoints: Float*, abril de 2007) | https://en.wikipedia.org/wiki/Float_(money_supply) | secundaria | 1/1/1/1 | [S] |
| 6 | Wikipedia, Cash management | https://en.wikipedia.org/wiki/Cash_management | secundaria, con aviso de mantenimiento | 1/1/1/1 | [S] |
| 7 | Wikipedia, Treasury management | https://en.wikipedia.org/wiki/Treasury_management | secundaria | 1/1/1/1 | [S] |
| 8 | OpenStax *Principles of Finance 2e*, 19.3 Cash Management | https://openstax.org/books/principles-finance-2e/pages/19-3-cash-management | primaria (libro abierto) | 2/1/1/1 | [L] vía extractor |
| 9 | Wikipedia, Liquidity preference (cita a Dimand 2008 en *New Palgrave* y a Keynes 1936) | https://en.wikipedia.org/wiki/Liquidity_preference | secundaria | 1/1/1/1 | [S] |
| 10 | Bates, Kahle y Stulz (2009), NBER WP 12534 | https://www.nber.org/papers/w12534 | primaria (académica) | 3/3/1/3 | [M] |
| 11 | Wikipedia, Trade credit insurance (con aviso de citas faltantes) | https://en.wikipedia.org/wiki/Trade_credit_insurance | secundaria | 1/1/1/1 | [S] |
| 12 | Wikipedia, Credit control (cita a Allianz Trade 2021, Reckon, Accountancy Recruit) | https://en.wikipedia.org/wiki/Credit_control | secundaria | 1/1/1/1 | [S] |
| 13 | Wikipedia, Dunning (process) (stub, 2022) | https://en.wikipedia.org/wiki/Dunning_letter | secundaria | 1/1/1/1 | [S] |
| 14 | Wikipedia, Days sales outstanding | https://en.wikipedia.org/wiki/Days_sales_outstanding | secundaria | 1/1/1/1 | [S] |
| 15 | Wikipedia, Remittance advice | https://en.wikipedia.org/wiki/Remittance_advice | secundaria | 1/1/1/1 | [S] |
| 16 | ERPNext, Payment Reconciliation | https://docs.frappe.io/erpnext/user/manual/en/payment-reconciliation | primaria de práctica | 2/2/2/2 | [L] vía extractor |

URL probadas que dieron 404 o contenido retirado y no se citan: OpenStax Principles of Accounting (dos formas de la URL del capítulo 9), Wikipedia Cash pooling y Notional pooling, Odoo follow-up (versión 18.0), Allianz Trade (dos páginas), la página de Fedpoints del NY Fed («This content is no longer available»), treasurers.org sobre estructuras de cuentas. El CFPB no menciona las cinco C.

## 1. Proyección de caja: 13 semanas, método directo, rolling forecast, precisión

Método directo e indirecto (fuente 2):
- Directo: programa los cobros y pagos reales; los cobros vienen sobre todo de cuentas a cobrar y los pagos incluyen sueldos, proveedores, dividendos e intereses. El artículo lo dice «best suited to the short-term forecasting horizon of 30 days», porque hay datos reales y no proyectados.
- Indirectos (parten de estado de resultados y balance proyectados): ingreso neto ajustado, balance proforma y reversión de devengados. Los dos primeros sirven para mediano y largo plazo, con períodos mensuales o trimestrales; el tercero se presenta como mejor para el mediano plazo y evita los errores acumulados del directo en períodos largos, pero es más complejo.
- Precisión: «rare for cash receipts to match sales forecasts exactly»; los clientes rara vez pagan todos en fecha, por eso hace falta criterio con la experiencia. Los resultados de los métodos indirectos hay que ajustarlos por la diferencia entre la caja contable y los saldos del banco.
- El artículo no trata el rolling forecast. Atribuciones: de Caux (2005), Bort (1990), AFP (2006), no leídas.

Las 13 semanas (fuentes 3 y 4, ambas de vendedores: cuentan como una línea de práctica comercial, no como dos independientes):
- Trece semanas son un trimestre: «short enough that most inputs are already known» (facturas emitidas, sueldos programados) y «long enough to arrange financing or change spending before a shortfall» (fuente 3, resumen del extractor). La fuente 4 dice que «balances actionability and visibility».
- Origen: la fuente 3 dice que el formato salió de las reestructuraciones y cita a Wall Street Prep («in the context of corporate restructuring»); agrega que prestamistas y tribunales pidieron evidencia semanal de liquidez. La fuente 4 solo lo llama «the standard liquidity tool in turnarounds». Origen histórico sin fuente primaria (hueco).
- Estructura: una columna por semana; filas de caja inicial, cobros por origen (cuentas a cobrar abiertas, facturación futura, otros), sueldos, proveedores, obligaciones fijas, partidas únicas, flujo neto y caja final; caja final = caja inicial + flujo neto, comparada con un mínimo o un covenant. Método directo siempre: «cash in, cash out - no accrual adjustments» (fuente 4). Los cobros se modelan sobre la antigüedad de saldos.
- Rolling: cada semana se reemplaza la semana pasada por lo real y se agrega una semana 13; conviene guardar la versión previa, porque sin ella no se mide la desviación (fuente 3). La precisión decae con el horizonte: semanas 1 a 4 casi exactas, las siguientes direccionales (fuente 3).
- Medición de precisión: «receipts accuracy» = |previsto − real| ÷ real de cobros, por semana, seguida en las semanas 1 a 4 (fuente 3). Cobros y pagos se miden por separado porque fallan por razones distintas. Revisar el sesgo: si una semana yerra siempre para el mismo lado, el supuesto está mal (fuente 4). Revisión semanal de las diez mayores desviaciones de cobros, cada una con causa (pago tardío, disputa, promesa de pago incumplida, error de facturación, cobro sin aplicar) y responsable (fuente 3).
- Tolerancia: la fuente 3 dice que no hay referencia independiente aceptada de precisión a escala de empresa mediana y que cada empresa fija su banda. Nadie da un número; no inventarlo.
- Frontera con Emprender/Finanzas: ese plan es mensual a 12 meses y económico; las 13 semanas son de caja y semanales.

Recurso canónico propuesto: la guía de AFP sobre pronóstico (no leída); como ejemplo de estructura, la fuente 3, marcada como contenido comercial.

## 2. Posición de caja diaria, saldos y float

- OpenStax 19.3 (fuente 8) cubre los motivos de transacción y de precaución, la caja excedente que se invierte a corto plazo y el saldo compensatorio (USD 50.000 sobre un préstamo de USD 500.000). No trata float, lockbox, concentración ni saldo contable frente a disponible (lo confirmó el extractor).
- Float (fuente 5, que cita al NY Fed): es «money in the banking system that is counted twice, for a brief time, because of delays in processing checks». Float del banco: tiempo desde el depósito hasta que el banco depositante recibe los fondos. Float del cliente: desde el depósito hasta que el depositante puede usar los fondos; la diferencia se llama float negativo. Hasta que el cheque se compensa, el banco acredita provisoriamente. El artículo cuenta el «remote disbursement» de los años 70 y 80 (girar contra bancos lejanos para demorar la compensación). No usa «collection float» ni «disbursement float».
- Informe de saldos (fuente 6): los bancos informan, además del saldo, el float («checks in the process of collection»). Hay lockbox (el banco abre el correo y deposita los cheques) y concentración de caja (el banco principal junta los saldos de cuentas locales en una cuenta que paga interés). Fuente con aviso de mantenimiento.
- Posición diaria, saldo contable frente a disponible y valores al cobro: no se encontró texto que los defina. Puede explicarse como razonamiento propio (saldo contable = lo registrado; disponible = lo que se puede usar hoy, sin los cheques depositados aún sin acreditar; posición = disponible más lo en tránsito menos los compromisos del día), sin cita, o buscarlo en el *Essentials* de AFP. Hueco.
- Frontera: la conciliación entre libros y extracto es de Contabilidad.

## 3. Cuentas bancarias, firmantes, concentración

- Marco: APQC 9.7.2.7 y 9.7.2.8 y la ACT (en `caja-y-liquidez.md`). La fuente 7 dice que el tesorero cuida el contacto con bancos y que pooling, netting y banco interno son funciones de la caja, sin explicarlos.
- Cash pooling físico y nocional: sin fuente (Wikipedia dio 404). Cantidad de bancos, firmantes y poderes: sin fuente. Lo único aportable es la concentración de la fuente 6 (en una frase) y que APQC 9.7.3 la coloca en cuentas internas del grupo, o sea empresa grande. Hueco completo.

## 4. Reserva de liquidez

- Motivos de Keynes (fuente 9, secundaria): transacción («people prefer to have liquidity to assure basic transactions»), precaución (colchón contra gastos inesperados) y especulación (retener liquidez porque se espera que caiga el precio de los bonos). El artículo no da capítulo de la *Teoría general* (1936); lo atribuye a Dimand (2008). Las dos primeras motivan la reserva de una empresa; la especulativa es de inversión financiera y casi no aplica a una pyme operativa (juicio propio).
- OpenStax 19.3 (fuente 8) usa dos de los tres motivos (transacción y precaución) para la caja de la empresa, con ejemplos (nómina, proveedores; averías).
- Evidencia: Bates, Kahle y Stulz (fuente 10, [M]): la razón caja/activos promedio de las industriales de EE. UU. subió 129 % de 1980 a 2004; al final, la caja promedio cubría la deuda. Atribuyen la suba a flujos de caja más riesgosos, menos capital de trabajo (menos inventarios y cuentas a cobrar) y más I+D, y concluyen que el motivo de precaución es el que mejor la explica. Son empresas de EE. UU.; no se transfiere a una pyme.
- «Meses de gastos» como regla: no se encontró fuente. Si va a la nota, decir que es regla de practicantes sin respaldo leído, o no ponerla. Hueco.

## 5. Crédito a clientes

- Las cinco C, cálculo del límite, garantías: sin fuente. No afirmarlas con cita.
- Pasos del crédito (fuente 12, secundaria, que cita a Allianz Trade 2021): solicitud formal del cliente; evaluación por el responsable de crédito y el de riesgo; cotejo del plazo de cobro con el plazo de pago propio; calificadoras externas si corresponde; revisión interna del riesgo de incobrable frente a la ganancia esperada; aprobación de crédito, riesgo y dirección de finanzas; apertura de la cuenta con tope y duración del crédito. Es un proceso de empresa grande; en una pyme se reduce (quién aprueba lo fija la política de tesorería).
- Seguro de crédito (fuente 11, con aviso de citas faltantes): cubre insolvencia o incumplimiento prolongado del comprador; «usually covers a portfolio of buyers»; paga «an agreed percentage of an invoice or receivable that remains unpaid»; quien se asegura debe fijar un límite por comprador; la prima es mensual, como porcentaje de las ventas del mes o de las cuentas a cobrar pendientes, según el riesgo promedio de la cartera; algunas pólizas el asegurador puede cancelarlas o reducirlas. Plazo de espera de reclamo: no figura. Sin fuente primaria (Allianz Trade, Atradius, Berne Union: 404 o no abiertas). Hueco.

## 6. Cobranza: DSO, DSO mejor posible, CEI, secuencia

CRF (fuente 1, primaria, [L]), literal:
- CEI: «expresses the effectiveness of collection efforts over time. The closer to 100 percent, the more effective the collection effort is. It is a measure of the quality of the collection of receivables». Fórmula: (Beginning Receivables + (Credit Sales/N) − Ending Total Receivables) ÷ (Beginning Receivables + (Credit Sales/N) − Ending Current Receivables) × 100, con N = número de meses. «CEI can be used as a departmental or individual performance measure.» El denominador resta las cuentas a cobrar corrientes (aún no vencidas), no las vencidas; coincide con lo que dicen fuentes comerciales de los resultados de búsqueda (no abiertas). El «90 % es bueno» sale de una calculadora comercial vista en el buscador; no es de CRF.
- DSO: «the average time (aggregate), in days it takes a firm to convert its accounts receivables to cash. DSO is one of the most often misused and misunderstood performance measures». Fórmula: Ending Total Receivables × Number of Days in Period Analyzed ÷ Credit Sales for Period Analyzed. Su valor está en ayudar a determinar si un cambio en las cuentas a cobrar viene de las ventas o de otro factor «such as change in selling terms». Se compone de plazos (lo corriente y futuro), facturas atrasadas y errores operativos, problemas de servicio y calidad, y disputas (deducciones). Preguntas que propone al compararse con la industria: plazos en línea con competidores, plazos aplicados, procedimientos de cobranza adecuados, base de clientes riesgosa, facturas emitidas a tiempo, bien y claras, descuentos por pronto pago, calidad discutible, clientes insatisfechos.
- DSO mejor posible (best possible DSO): Current Receivables × Number of Days in Period Analyzed ÷ Credit Sales for Period Analyzed; «the best possible level of receivables under the most favorable condition – A/R with no delinquency». Debe usarse junto con el DSO; cuanto más cerca esté el DSO del mejor posible, más cerca están las cuentas a cobrar del nivel óptimo, y se relaciona con los plazos de venta.
- Días de atraso promedio (ADD): DSO − Best Possible DSO. Puede «deceive» al tapar a los atrasados cuando otros clientes pagan antes del vencimiento (literal: «can be deceiving by masking the performance of delinquent accounts if other accounts are discounting their bills»). Y: «Like the many measures, there are flaws and biases, however, used consistently and routinely, these DSO related measures can be indicators of performance and can be an early warning sign».
- Porcentaje corriente: Ending Current A/R ÷ Total Receivables. Porcentaje a más de 91 días: total de la categoría de más de 90 días ÷ total de cuentas a cobrar; «nothing special about the period of over 91 days»; es la metodología de CRF en su encuesta nacional de plazos (NSDTR) desde hace más de 45 años; se puede usar la categoría de antigüedad que convenga.
- Críticas del DSO de fuente secundaria (fuente 14, [S], que cita a Houston y Brigham 2009, p. 90): se lee mal como «días promedio para cobrar una venta», y es mejor leerlo como días de ventas promedio pendientes; cambia con el volumen de ventas, así que una variación no aísla la velocidad de cobro; un período demasiado corto genera artefactos; un DSO alto puede indicar mal filtro de crédito o mala cobranza y uno bajo, una política tan dura que frena ventas; lo bueno depende del modelo de negocio; varía con la estacionalidad, así que importa la tendencia. Discrepancia entre fuentes: la fuente 14 llama «DDSO» (days delinquent sales outstanding) a un «best possible DSO» y lo calcula como DSO menos DSO de lo corriente; CRF llama a esa resta «Average Days Delinquent» y define el mejor posible aparte. Seguir a CRF (primaria). Método countback: sin fuente.
- Secuencia de recordatorios: fuente 13 (stub): dunning es «the process of methodically communicating with customers»; va de recordatorios amables a cartas y llamadas amenazantes; las reglas varían por país y el hostigamiento a consumidores suele estar prohibido. Los plazos concretos (aviso previo, día 1, 15, 30) no tienen fuente. ERPNext Dunning (ronda anterior) es la evidencia de práctica. Odoo follow-up: 404.
- Deducciones y disputas: CRF las nombra dentro del DSO («disputes and customer dissatisfaction (deductions)») y APQC 9.2.5 las tiene como subproceso propio (ya anotado). Sin fuente sobre cómo se gestionan.

Recurso canónico propuesto: CRF, *Performance Measures*, para fórmulas y limitaciones (breve, de una asociación del oficio, la única primaria). Fijarse en que DSO, mejor posible y ADD se leen juntos.

## 7. Aplicación de cobros

- Datos de remesa (fuente 15): el aviso de pago es la carta del cliente que informa que pagó una factura; «should therefore specify the invoice numbers for which payment is tendered»; los avisos modernos pueden listar docenas o cientos de facturas. Sirve a cuentas a cobrar para cruzar facturas y pagos. Si el cliente no manda aviso, alguien lo arma. El artículo no trata cobros sin identificar ni pagos cortos.
- Herramienta de práctica (fuente 16, ERPNext Payment Reconciliation): lista los cobros y asientos con monto disponible para asignar; se elige factura y cobro y se asigna; sin selección asigna por primero entrado, primero salido (FIFO); para el cobro parcial propone el menor entre el saldo de la factura y el del cobro, se puede editar y el resto «stays unallocated and can be used later»; el monto asignado no puede superar ninguno de los dos; hay una cuenta de anticipos por defecto cuyos cobros entran en la lista; muestra un «Difference Amount» para revisar antes de conciliar. No trata el castigo (write-off). Es evidencia de que la práctica existe: asignar, parcial, resto sin aplicar, anticipo, diferencia.
- Cobros sin identificar, conciliación con el cliente, retenciones sufridas: sin fuente profesional. Si van a la nota, como razonamiento propio.

## Recursos canónicos (resumen)

| Componente | Recurso | Qué mirar |
|---|---|---|
| Medidas de cobranza | CRF, *Performance Measures* | fórmulas y limitaciones de DSO, mejor posible, ADD, CEI |
| Proyección de caja | AFP (guía de pronóstico, no leída); como ejemplo de estructura, Upflow (comercial) | semanas 1 a 4 frente al resto; cobros y pagos medidos por separado |
| Reserva de caja | Bates, Kahle y Stulz 2009 (abstract) y OpenStax 19.3 | motivo de precaución; transacción y precaución |
| Posición, float, firmantes, pooling | sin fuente adecuada | AFP *Essentials* (no leído) |
| Crédito y seguro | sin fuente adecuada | Allianz Trade, Atradius, NACM (no abiertos) |

## Huecos

- Origen de las 13 semanas en reestructuraciones: una sola fuente comercial (Upflow, que cita a Wall Street Prep, no abierto). Sin primaria.
- No hay un valor aceptado de precisión del pronóstico (la propia fuente lo dice); tampoco encuestas de AFP.
- Posición de caja diaria (saldo contable frente a disponible, fondos en tránsito, valores al cobro): sin fuente. Float: solo Wikipedia, que cita a un NY Fed ya retirado.
- Cuentas bancarias: firmantes y poderes, cantidad de bancos, cash pooling físico y nocional, netting: sin fuente.
- Reserva de liquidez: reglas de «meses de gastos» sin fuente; Keynes solo por Wikipedia (sin capítulo); no se leyó la *Teoría general*.
- Cinco C, límite de crédito, garantías: sin fuente. Seguro de crédito: solo Wikipedia con citas faltantes.
- Secuencia de recordatorios con plazos, mora, acuerdos y pase a legales, deducciones y disputas: sin fuente.
- Countback para DSO: sin fuente. CEI: fórmula de CRF leída; benchmarks sin fuente.
- Cobros sin identificar, anticipos y conciliación con el cliente: sin fuente profesional; solo ERPNext y Wikipedia sobre remesas.
- Argentina: nada de esta ronda toca lo local.
- Árbol: el aviso de pago y las deducciones no tienen casa clara; conviene ponerlos en aplicación de cobros (datos de remesa, diferencias) y en gestión de la cobranza (disputas). Sin otros cambios.
