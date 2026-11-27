# Investigación cruda, segunda ronda: financiamiento, costo, riesgos, política y pagos

Fecha de lectura: 2026-11-27. Complementa `financiamiento-y-riesgos.md` y `pagos-a-proveedores.md` (no repite lo que tienen).

**Advertencia de alcance.** El presupuesto de búsquedas web de la sesión seguía agotado (las tres búsquedas intentadas fueron rechazadas). Con fetch directo, **todas las URLs primarias que probé dieron 404**: OpenStax (`…/pages/19-introduction`, `…/1-introduction`, `…/16-introduction`), IFRS (resumen del proyecto en PDF, PDF de la enmienda, noticia de mayo de 2023), BCRA (`t-proteccion-usuarios.pdf`, `t-protusu.pdf`) y ACT (`/hub/treasurypedia/treasury-policy`). Solo respondieron páginas de Wikipedia en inglés, que son **fuente terciaria, último recurso**. Por eso casi todo lo de abajo es [S] terciario o derivación matemática propia. Lo que no tiene URL se marca **[sin verificar]** y no debe pasar a una nota vigente sin fuente primaria. No hay ningún resultado de las normas del IASB ni del BCRA: los puntos 1 (la enmienda) y 3 (costo financiero total) de la prioridad siguen abiertos.

Marcas: [S] resumen secundario. El fetch devuelve un resumen hecho por un modelo sobre la página, así que cuento todo como [S] aunque haya abierto la página; las citas entre comillas vienen de ese resumen y hay que cotejarlas con la página antes de usarlas. Puntajes 1 a 3: A autoridad, P profundidad, E ejemplos, U unicidad.

## Fuentes

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Wikipedia, *Factoring (finance)*: https://en.wikipedia.org/wiki/Factoring_(finance) | terciaria | 1 | 2 | 2 | 1 | [S] |
| Wikipedia, *Invoice discounting*: https://en.wikipedia.org/wiki/Invoice_discounting | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Overdraft*: https://en.wikipedia.org/wiki/Overdraft | terciaria (centrada en el Reino Unido) | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Revolving credit*: https://en.wikipedia.org/wiki/Revolving_credit | terciaria | 1 | 2 | 2 | 1 | [S] |
| Wikipedia, *Amortization calculator*: https://en.wikipedia.org/wiki/Amortization_calculator | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Amortization schedule*: https://en.wikipedia.org/wiki/Amortization_schedule | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Debt covenant*: https://en.wikipedia.org/wiki/Debt_covenant | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Loan covenant*: https://en.wikipedia.org/wiki/Loan_covenant | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Finance lease*: https://en.wikipedia.org/wiki/Finance_lease | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Effective interest rate*: https://en.wikipedia.org/wiki/Effective_interest_rate | terciaria | 1 | 1 | 2 | 1 | [S] |
| Wikipedia, *Fisher equation*: https://en.wikipedia.org/wiki/Fisher_equation | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Interest rate risk*: https://en.wikipedia.org/wiki/Interest_rate_risk | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Liquidity risk*: https://en.wikipedia.org/wiki/Liquidity_risk | terciaria (sesgo a bancos y seguros) | 1 | 2 | 1 | 1 | [S] |
| Wikipedia, *Forward contract*: https://en.wikipedia.org/wiki/Forward_contract | terciaria | 1 | 2 | 1 | 1 | [S] |
| Wikipedia, *Natural hedge*: https://en.wikipedia.org/wiki/Natural_hedge | terciaria | 1 | 1 | 2 | 1 | [S] |
| Wikipedia, *Positive pay*: https://en.wikipedia.org/wiki/Positive_pay | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Two-person rule* (redirige desde *Four-eyes principle*): https://en.wikipedia.org/wiki/Four-eyes_principle | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *ISO 20022*: https://en.wikipedia.org/wiki/ISO_20022 | terciaria | 1 | 1 | 1 | 1 | [S] |
| Wikipedia, *Supplier finance*: https://en.wikipedia.org/wiki/Supplier_finance | terciaria | 1 | 1 | 1 | 1 | [S]; no dice nada de la enmienda del IASB |

Páginas que dieron 404 o no tenían lo pedido, sin aporte: Covenant (finance), Financial covenant, Foreign exchange exposure, Lease, Covenant (law).

## 1. Financiamiento de corto plazo

**Descubierto.** «An overdraft occurs when something is withdrawn in excess of what is in a current account.» Se distingue el *arranged* (cubierto por un límite pactado) del *unarranged* (excede el límite; el banco puede rechazar o tratarlo como pedido informal de más límite); el no pactado «typically» cuesta más que el pactado; con interés, comisiones o ambos. https://en.wikipedia.org/wiki/Overdraft [S, Reino Unido; los términos y la reforma del FCA de abril de 2020 son locales]. Para la nota: un descubierto es un límite de crédito atado a la cuenta corriente, pactado de antemano o no, y la diferencia de costo entre pactado y no pactado enseña a pactarlo antes de necesitarlo. Cómo funciona en Argentina (acuerdo en cuenta corriente) va a Notas de Argentina **[sin verificar]**.

**Línea de crédito rotativa (revolving).** Un tope disponible durante un plazo, con retiro, devolución y nuevo retiro dentro del tope; cada retiro suele tomarse por uno, tres o seis meses; algunos prestamistas cobran una comisión sobre lo no usado: ejemplo de la fuente, comisión de 40% de un margen de 2,0%, o sea 0,8% efectivo, que sobre USD 600.000 sin usar da USD 4.800 por año. https://en.wikipedia.org/wiki/Revolving_credit [S]. **Comprometida vs. no comprometida: la fuente no lo trata.** Definición para sostener con fuente profesional **[sin verificar]**: en la comprometida el banco se obliga a prestar hasta el tope mientras no haya incumplimiento, y por eso cobra la comisión por no uso; en la no comprometida puede negarse a desembolsar cuando se la usa, justo cuando más se la necesita. La página de riesgo de liquidez coincide en el espíritu: una empresa sana debería «establish durable, ever green (i.e., always available) liquidity lines of credit» con un prestamista de buena calificación y repartir entre varios (cita un informe de la American Academy of Actuaries, pensado para aseguradoras). https://en.wikipedia.org/wiki/Liquidity_risk [S].

**Factoring.** Sin recurso (*non-recourse*): venta de un activo financiero; el factor absorbe la pérdida si el deudor no paga (puede quedar una «quality recourse» por devoluciones de mercadería). Con recurso: el factor puede reclamar al vendedor lo impago. Con notificación el deudor sabe de la cesión (aviso de cesión) y paga al factor; sin notificación el vendedor cobra como agente del factor. Adelanto típico de 80% a 85% del valor de la factura; el resto se devuelve menos comisiones al cobrarse. Costo: comisión como porcentaje de la factura (ejemplo 5% por una factura a 45 días), a veces cargo de administración más interés devengado; algunos factores retienen una reserva de 10% a 15% de la línea. https://en.wikipedia.org/wiki/Factoring_(finance) [S]. Observación: el costo anualizado de «5% por 45 días» no es 5%; es 0,05 × 365/45 ≈ 40,6% nominal anual simple (derivación propia; el valor exacto depende de si el 5% se aplica sobre la factura o sobre lo adelantado).

**Descuento de facturas (invoice discounting).** En el factoring el factor cobra y el deudor suele saberlo; en el descuento (uso británico) el vendedor cobra por cuenta del factor y es confidencial: «the main difference between factoring and invoice discounting is confidentiality». En EE. UU. el factoring es una venta y el descuento es un préstamo con la cuenta a cobrar como garantía. https://en.wikipedia.org/wiki/Invoice_discounting [S]. **Descuento de documentos (cheques, pagarés, letras): la fuente no lo trata.** Definición a sostener con fuente **[sin verificar]**: el banco o un inversor compra el documento a su valor nominal menos un descuento que depende de la tasa y de los días hasta el vencimiento; con endoso la empresa responde si el librador no paga. La nota debe advertir que «descuento» significa cosas distintas en inglés (financiar facturas) y en el uso local (descontar cheques).

**Reverse factoring / supplier finance.** Definición y casos Carillion y Greensill están en la ronda anterior. Sin aporte nuevo: la página *Supplier finance* repite la definición («a suite of financial solutions that aim to manage working capital and liquidity for businesses within a supply chain») y no menciona la enmienda del IASB.

**Enmienda del IASB de mayo de 2023 a NIC 7 y NIIF 7: NO SE PUDO LEER (hueco abierto).** Las tres URLs primarias probadas dieron 404. Lo único con fuente sigue siendo lo de la ronda anterior (emisión en mayo de 2023, modifica IAS 7 e IFRS 7; https://www.ifrs.org/projects/completed-projects/2023/supplier-finance-arrangements/). Lo siguiente es **[sin verificar: conocimiento previo]** y hay que cotejarlo con el texto antes de escribirlo: IAS 7 (párrafos 44F a 44H) pide revelar términos y condiciones de los acuerdos, el importe en libros de los pasivos que forman parte del acuerdo y cuántos ya pagó el financiador al proveedor, el rango de fechas de vencimiento frente a las cuentas a pagar comparables, y los cambios no monetarios; IFRS 7 agrega estos acuerdos como ejemplo en el riesgo de liquidez; vigencia: períodos anuales que comienzan el 1 de enero de 2024 o después, con alivios en el primer año. En Argentina las NIIF las adopta la FACPCE; no se investigó.

## 2. Préstamos

**Sistema francés (cuota constante).** A = P·i(1+i)ⁿ / ((1+i)ⁿ − 1), con A cuota, P capital, i tasa por período y n cantidad de cuotas; si i = 0, A = P/n. https://en.wikipedia.org/wiki/Amortization_calculator [S]. Coincide con la ronda anterior. En el modelo estándar «the total amount of each payment is the same»; la página no nombra «sistema francés» ni «alemán» y no trata la amortización constante.

**Sistema alemán (capital constante).** Sin fuente leída que use ese nombre (https://en.wikipedia.org/wiki/Amortization_schedule solo lista «Straight line (linear)» y «Declining balance» como métodos). Derivación propia: amortización por cuota = P/N; interés de la cuota k = i·P·(1 − (k−1)/N); cuota k = P/N + i·P·(1 − (k−1)/N); interés total = i·P·(N+1)/2.

**Ejemplo con la cuenta hecha (propio, verificable en una planilla):** P = 100.000, N = 12 cuotas mensuales, i = 1% mensual.
- Francés: cuota 8.884,88 constante; interés total ≈ 6.618,6.
- Alemán: amortización 8.333,33 por mes; primera cuota 9.333,33, última 8.416,67; interés total 6.500,00.
- Lectura: con la misma tasa el alemán paga menos interés total porque amortiza antes, pero exige más caja al principio; el francés cuesta más intereses y da una cuota previsible. El uso típico de cada uno no se verificó.

**Garantías.** Sin fuente leída. **[sin verificar]** Tipos: real (hipoteca, prenda), personal (fianza, aval de un socio, aval de una sociedad de garantía recíproca), cesión de cobranzas o de contratos. Punto para Notas de Argentina (SGR ya está en el árbol).

**Covenants.** Fuentes leídas, ambas débiles. «Covenants are undertakings given by a borrower as part of a term loan agreement»; los hay financieros, de información, de propiedad, afirmativos, negativos o positivos; típicos en préstamos inmobiliarios: LTV, DSCR e ISCR; romperlos puede dar al prestamista el derecho de exigir el pago anticipado o cobrar más interés (https://en.wikipedia.org/wiki/Loan_covenant) [S]. «Lenders may write stipulations on the borrower, called covenants»; ejemplos: informar periódicamente su situación financiera (de hacer), abstenerse de pagar dividendos, recomprar acciones o endeudarse más (de no hacer), y cláusulas ligadas a la relación deuda/patrimonio o a la cobertura de intereses (financieras) (https://en.wikipedia.org/wiki/Debt_covenant) [S]; las categorías «afirmativo», «negativo» y «financiero» son un mapeo del resumen, no figuran literales. Falta una fuente primaria o de libro con los ratios usuales (deuda neta/EBITDA, cobertura de intereses, cobertura del servicio de la deuda) y umbrales típicos.

**Leasing.** Finance lease: la financiera suele ser la dueña legal durante el contrato, el tomador tiene control operativo y comparte riesgos y beneficios; bajo IFRS es financiero el arrendamiento que transfiere «substantially all the risks and rewards» de la propiedad. IFRS 16 eliminó para el tomador la clasificación y exige registrar «a right-of-use asset and a lease liability», salvo arrendamientos de corto plazo y de bajo valor; el arrendador sigue clasificando (https://en.wikipedia.org/wiki/Finance_lease) [S]. La fuente no define el leasing operativo; hay que ir a IFRS 16 o a un libro de contabilidad. Frontera: cómo se registra es de Contabilidad; Tesorería necesita que la cuota es una salida de caja fija y contratada.

## 3. Costo del financiamiento

- **Tasa efectiva desde la nominal:** EAR = (1 + i/m)^m − 1, con i nominal anual y m períodos de capitalización por año; ejemplo de la fuente: 6% nominal con capitalización mensual da 0,5% por mes, (1,005)^12 ≈ 1,0617, o sea 6,17% efectiva anual. https://en.wikipedia.org/wiki/Effective_interest_rate [S].
- **Ecuación de Fisher:** «(1+i)=(1+r)(1+π)», con r real, i nominal y π inflación; aproximación r = i − π «since the rπ is negligible»; forma equivalente r = (1+i)/(1+π) − 1. https://en.wikipedia.org/wiki/Fisher_equation [S]. Ejemplo propio: nominal anual 60% con inflación 50% da r = 1,60/1,50 − 1 = 6,67%, no 10%: con inflación alta la aproximación engaña. La tasa real es *ex post* con la inflación observada y *ex ante* con la esperada; la fuente no lo aclara.
- **Costo de renunciar al descuento por pronto pago (2/10 neto 30):** derivación propia: 2/98 = 2,04% por 20 días, o sea 2,04% × 365/20 ≈ 37,2% nominal anual simple y (1,0204)^(365/20) − 1 ≈ 44,6% efectivo anual. Ya tiene sección en `pagos-a-proveedores.md`.
- **Costo financiero total (CFT) en Argentina: HUECO.** Las dos URLs del BCRA dieron 404 y no hubo búsqueda. **[sin verificar]** Lo que recuerdo: el BCRA lo define en las normas de «Protección de los usuarios de servicios financieros» y lo expresa como tasa efectiva anual, con y sin impuestos, incluyendo intereses, comisiones, seguros y gastos a cargo del cliente. Hay que traer el texto ordenado vigente. Va a la nota de Argentina. Para el modelo general: la comisión por no uso de una línea y los gastos de apertura entran al costo real.

**Recurso canónico.** OpenStax *Principles of Finance* 2e: no pude abrirlo (404 en tres URLs); el índice vigente se busca en https://openstax.org/details/books/principles-finance-2e. No pude confirmar de qué tratan los capítulos 19 y 20 que pedía el encargo, así que no los cito.

## 4. Riesgos

- **Riesgo de liquidez.** *Funding liquidity risk*: los pasivos «Cannot be met when they fall due» o «Can only be met at an uneconomic price». *Market liquidity risk*: un activo no se puede vender por falta de liquidez del mercado. Mitigaciones listadas: líneas de crédito siempre disponibles, reservas explícitas de liquidez, plan de contingencia de fondeo y probar el flujo de caja día a día con un escenario de incumplimiento de una contraparte clave. https://en.wikipedia.org/wiki/Liquidity_risk [S; apunta a bancos y aseguradoras, no a empresas no financieras].
- **Riesgo de tasa.** «The potential for financial loss due to fluctuations in interest rates.» La página trata bonos y bancos; no aborda préstamos a tasa fija o variable de una empresa. https://en.wikipedia.org/wiki/Interest_rate_risk [S]. **Hueco:** lo central de la nota (con deuda a tasa variable se pierde si la tasa sube; con tasa fija se pierde si baja; cobertura con tope, canje o fijando la tasa) no tiene fuente leída **[sin verificar]**.
- **Riesgo de contraparte.** Sin fuente específica. La de forwards dice «forward contracts have a significant counterparty risk» (https://en.wikipedia.org/wiki/Forward_contract) [S]. Los otros frentes (cliente que no paga, banco o emisor del excedente, financiador de la cadena) están en `credito-y-cobranzas.md`, `caja-y-liquidez.md` y en Greensill.
- **Exposición de transacción, traslación y económica.** La página específica dio 404. **[sin verificar]** Transacción: el flujo contratado en otra moneda entre que se pacta y se cobra o paga; traslación: lo que cambia al convertir estados de una filial a la moneda de presentación; económica u operativa: el efecto del tipo de cambio sobre la competitividad y los flujos futuros no contratados. Para una pyme importa la de transacción. Con fuente, solo lo de la ronda anterior (Duke FinReg Blog, *Currency risk*).
- **Forward y futuros.** Forward: «a non-standardized contract between two parties to buy or sell an asset at a specified future time»; precio fijado al inicio; fuera de bolsa; sin pagos intermedios típicos (aunque puede incluir márgenes), sin pago inicial; salir exige negociar con la contraparte original. Los futuros son estandarizados, de bolsa, con liquidación diaria (la página lo da por contraste, no lo desarrolla). https://en.wikipedia.org/wiki/Forward_contract [S].
- **Cobertura natural.** «An investment that reduces the undesired risk by matching cash flows (i.e. revenues and expenses)»; ejemplos: un exportador que abre una planta en el país de sus ventas, endeudarse en la moneda de los ingresos de una filial, pagar bonos en la moneda de los ingresos. https://en.wikipedia.org/wiki/Natural_hedge [S]. Ejemplo propio sin fuente: un comercio que vende y compra en dólares compensa sus flujos y solo cubre la diferencia neta.
- **Recurso canónico.** AFP *Essentials of Treasury Management* (de pago, no leído) y materiales de ACT.

## 5. Política de tesorería

Sin fuente leída: la página de ACT probada dio 404 (https://www.treasurers.org/hub/treasurypedia/treasury-policy). Lo que sigue es propuesta de contenidos, **[sin verificar]**, apoyada solo en los códigos APQC 9.7.1, 9.7.4 y 9.7.5 de la ronda anterior (política de inversión, exposición a emisores, cobertura «in accordance with risk policy»): objetivos y alcance; roles y quién autoriza qué (límites por monto); estructura de cuentas y bancos permitidos; liquidez (colchón mínimo); endeudamiento (instrumentos, límites, covenants a vigilar); inversión (instrumentos permitidos, plazo máximo, límite por contraparte); riesgo cambiario y de tasa (qué se cubre, con qué, quién decide); controles y reportes; revisión periódica. En una empresa chica cabe en una o dos páginas y sirve sobre todo para fijar quién puede firmar y mover plata.

**Recurso canónico propuesto:** guía de política de tesorería de ACT (encontrar la URL vigente) y APQC 9.7.1.

## 6. Pagos

- **Firmas conjuntas y doble control.** *Two-person rule*: «access and actions require the presence of two or more authorized people at all times»; en pagos, algunos sistemas exigen que dos usuarios autorizados aprueben una transferencia antes de procesarla, y algunas empresas y entidades sin fines de lucro exigen dos firmas en los cheques. https://en.wikipedia.org/wiki/Four-eyes_principle [S]. Frontera: la separación de funciones es de Contabilidad; acá se agrega quién firma qué monto.
- **Positive pay.** «The client company electronically shares its check register of all written checks with the bank.» «The bank therefore will only pay checks listed in that register», contrastando monto, beneficiario y número de serie; «This system dramatically reduces check fraud». https://en.wikipedia.org/wiki/Positive_pay [S]. No trata el *payee positive pay* por separado. Sigue faltando fuente primaria (banco, Reserva Federal, AFP). El equivalente local no se investigó.
- **ISO 20022.** «An ISO standard for electronic data interchange between financial institutions»; alcance: pagos, valores, tarjetas; primera sintaxis soportada: XML; adopción inicial de SWIFT en marzo de 2023 con hoja de ruta publicada por SWIFT. https://en.wikipedia.org/wiki/ISO_20022 [S]. No menciona el mensaje de instrucción de pago de cliente a banco (`pain.001`, que conozco por la documentación de Odoo de la ronda anterior; **[sin verificar]**) ni las fechas de migración de los pagos transfronterizos. Frase de una línea: es el estándar de mensajes que reemplaza a los formatos propios de archivo de pagos, y el archivo de un lote de transferencias al banco suele ir en ese formato.
- **Pagos al exterior (SWIFT).** Sin fuente nueva. **[sin verificar]** SWIFT es la red de mensajes entre bancos, no mueve plata; el pago pasa por bancos corresponsales que cobran comisiones, y la opción de gastos (ordenante, beneficiario o compartidos) cambia cuánto recibe el proveedor.
- **Pagos duplicados: HUECO.** Sin fuente ni cifra. **[sin verificar]** Controles habituales: unicidad de proveedor + número de factura + importe; marcar la factura como en pago al armar la corrida; revisar pagos al mismo proveedor por igual importe en una ventana corta; conciliar contra el extracto.
- **Prioridades de pago cuando la caja no alcanza: HUECO.** Sin fuente. **[sin verificar]** Criterio de práctica: primero lo que tiene consecuencia legal o frena la operación (sueldos y cargas, impuestos, servicios básicos), luego proveedores críticos o sin sustituto y los que dan un descuento mayor que el costo del dinero, y al final el resto, negociando por escrito un plan con quien se estira. Decirlo como práctica, no como norma; la prelación legal en un concurso es de abogados y de Argentina.

## Recursos canónicos (qué parte y en qué fijarse)

| Componente | Recurso | Parte | Estado |
|---|---|---|---|
| Descubierto, línea, factoring | OpenStax *Principles of Finance* 2e | capítulo de financiamiento de corto plazo (sin confirmar cuál) | URL no verificada |
| Revelación de supplier finance | IASB, enmienda a IAS 7 e IFRS 7 (mayo de 2023) | IAS 7 pár. 44F a 44H; IFRS 7 (sin verificar el párrafo) | sin leer |
| Tasa efectiva y real | OpenStax (valor del dinero en el tiempo); Brealey, Myers y Allen | EAR y Fisher | sin leer |
| CFT | BCRA, texto ordenado de protección de usuarios de servicios financieros | definición de CFT | sin leer |
| Leasing | IFRS 16 | definición y modelo del tomador | sin leer |
| Política y riesgos | ACT; AFP *Essentials of Treasury Management* | política y riesgo | sin leer |
| Pagos | norma ISO 20022; guías de bancos | `pain.001`; filtros de débito | sin leer |

## ¿Cambiaría el árbol?

Dos ajustes menores. (1) Factoring, descuento de documentos y descuento de facturas, en una nota comparativa («vender o dar en garantía lo que me deben»): la diferencia entre venta y préstamo, con o sin recurso, con o sin aviso, es lo que importa a quien modela, y los nombres cambian entre inglés y uso local. (2) El costo financiero (tasa efectiva, Fisher, CFT, costo de renunciar al descuento) es una misma cuenta aplicada a todas las fuentes: sirve una nota «cómo comparar» aparte de cada instrumento.

## Huecos

1. Texto de la enmienda del IASB a IAS 7 e IFRS 7: sin leer (3 URLs 404). Contenido y vigencia sin verificar.
2. Costo financiero total del BCRA: sin leer (2 URLs 404).
3. OpenStax *Principles of Finance* 2e: ninguna página abrió (404), no confirmo los capítulos 19 y 20.
4. ACT y AFP: política de tesorería, financiamiento y riesgo sin fuente abierta leída.
5. Línea comprometida vs. no comprometida, descuento de documentos, garantías, leasing operativo y ratios usuales de covenants: sin fuente.
6. Riesgo de tasa para quien debe (fija vs. variable, tope, canje) y las tres exposiciones cambiarias: sin fuente.
7. Pagos: duplicados, prioridades, SWIFT y pagos al exterior, `pain.001`, positive pay: sin fuente primaria.
8. Todo lo [S] de Wikipedia hay que reemplazarlo o confirmarlo con fuente primaria antes de pasar a una nota vigente; lo derivado (cuotas, 2/10 neto 30, factoring a 45 días) es verificable en planilla pero se pone como cuenta propia.
9. Argentina: no se investigó nada nuevo.
