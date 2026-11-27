# Investigación: Pagos a proveedores (Tesorería)

Fecha de lectura: 2026-11-27. Marcas: [L] texto leído (completo o la parte citada), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U).

Límites de esta capa: la factura del proveedor, su asiento, el cruce de tres vías y la autorización por tramos ya están en `Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md` y `Contabilidad/Control-interno/autorizaciones.md`. Ese material ya usa el ejemplo 5/10 n/30 de OpenStax (Principles of Financial Accounting 6.3) solo como asiento; acá va el costo financiero de ese descuento. La nota de autorizaciones ya cita la facturación ficticia de ACFE 2024 (22 %, mediana USD 100,000) y dice que las guías de separación de funciones salen de empresas de software; no se repite. Lo nuevo de esta capa: cuándo pagar, cómo se arma y se manda el lote, con qué medio, y cómo se protege la salida de plata de un engaño externo (no de un fraude interno).

Nota de método: se agotó el presupuesto de búsquedas web de la sesión tras la primera ronda (tres búsquedas). El resto se hizo con lecturas directas de URLs conocidas. Lo que no se pudo cubrir está en «Huecos».

## Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 1 | OpenStax, *Principles of Finance* (1.ª ed.), 19.2 «What Is Trade Credit?» | Primaria (libro de texto abierto) | 3/2/3/2 | [L] | https://openstax.org/books/principles-finance/pages/19-2-what-is-trade-credit |
| 2 | OpenStax, *Principles of Finance 2e*, mismo capítulo (Dahlquist y Knight, publicado 24 jun 2026) | Primaria; es la misma obra que la 1 | 3/1/2/1 | [L] (solo citas) | https://openstax.org/books/principles-of-finance-2e/pages/19-2-what-is-trade-credit |
| 3 | FBI IC3, *2025 Internet Crime Report* (PDF de 3,2 MB) | Primaria | 3/3/2/3 | [L] las partes citadas, con `pdftotext` | https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf |
| 4 | FBI IC3, alerta pública sobre BEC (código PSA240911; el título no se verificó) | Primaria | 3/2/2/2 | [L] | https://www.ic3.gov/PSA/2024/PSA240911 |
| 5 | AFP, *2026 Payments Fraud and Control Survey Report: Key Highlights* (abril 2026; 465 profesionales; datos de 2025), alojado por quien lo auspicia | Primaria (encuesta con método y n declarado, solo de EE. UU.) | 3/3/3/3 | [L] el PDF de resumen; el informe completo es solo para socios | https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf |
| 6 | AFP, comunicado de prensa sobre la misma encuesta | Secundaria (la misma obra que la 5) | 2/1/1/1 | [L] | https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags |
| 7 | Nacha, nota sobre BEC (mayo 2026), que cita la misma encuesta de AFP | Secundaria (misma obra que la 5) | 2/1/1/1 | [L] | https://www.nacha.org/news/business-email-compromise-attempts-rose-sharply-2025-report-finds |
| 8 | APQC, *Process Classification Framework* Cross Industry v7.4 (2024), categoría 9.6 y 9.7 | Primaria (marco) | 3/1/1/2 | [L] las secciones 9.6 y 9.7 | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf |
| 9 | Odoo 18, documentación de pagos por lotes (Batch Payments) | Primaria de práctica (documentación de un software) | 2/2/2/2 | [L] | https://www.odoo.com/documentation/18.0/applications/finance/accounting/payments/batch.html |
| 10 | ERPNext (Frappe), documentación de Payment Entry | Primaria de práctica | 2/2/2/2 | [L] | https://docs.frappe.io/erpnext/user/manual/en/payment-entry |
| 11 | Wikipedia, «Positive pay» | Secundaria, con aviso propio de exceso de fuentes primarias | 1/1/1/1 | [L] | https://en.wikipedia.org/wiki/Positive_pay |

Independencia: 1 y 2 son la misma obra, cuentan como una. 5, 6 y 7 son la misma encuesta, cuentan como una. 9 y 10 son prácticas de dos productos, cuentan como evidencia de que la práctica existe, no como norma. 3 y 4 son del mismo organismo pero informes distintos (anual y alerta pública); para cifras de fraude de pagos en EE. UU. las dos fuentes independientes entre sí son el FBI (denuncias recibidas) y AFP (encuesta a tesoreros).

Aviso de licencia: la página de OpenStax 2e dice que su contenido no puede usarse para entrenar modelos de lenguaje ni incorporarse a ofertas de IA generativa sin permiso escrito de OpenStax. Se leyó para citar una fórmula; si el equipo quiere evitar el roce, que cite la fórmula con la 1.ª edición o con otro libro, y que no copie texto.

## 1. Programación de pagos: vencimientos y descuento por pronto pago

Afirmaciones:

- Los términos de pago son un dato de la factura. «A common net term is Net 30, with payment due in full within 30 days of the invoice»; «2/10 n/30» da 2 % de descuento si el saldo se paga dentro de los 10 días de la fecha de factura (fuente 2, [L]).
- El libro llama al crédito comercial «often referred to as a no-cost type of financing» y a la vez dice que quien no toma el descuento por pronto pago «will pay more» (fuente 2, [L]). La contradicción es solo aparente: es gratis dentro del plazo neto, y costoso si se renuncia al descuento.
- Fórmula del libro: costo anual = [360 / (plazo total - plazo del descuento)] x [descuento % / (100 - descuento %)] (fuente 1, [L]). Con 2/10 neto 30: 360/20 x 2/98 = **36,73 %**; el libro dice textualmente «The annual cost to NAI of not taking advantage of the discount for quick payment is 36.73 percent». El libro llama a esto una tasa anual (APR) o costo de oportunidad anualizado; no da una tasa efectiva anual (fuente 1, [L]).
- Cálculo propio (no es cita; verificado con una corrida): mismas condiciones, mismo descuento y tasa simple con 365 días: 37,24 %; capitalizando, (1 + 2/98)^(365/20) - 1 = 44,59 %. Otras condiciones, tasa simple con 360 días: 1/10 neto 30 = 18,18 %; 2/10 neto 60 = 14,69 %; 5/10 neto 30 = 94,74 %. La conclusión es que el descuento solo conviene si la empresa no tiene dinero más barato que ese costo (descubierto, línea de crédito) o si la caja le sobra; para el tesorero es una comparación con el costo de su financiamiento marginal. Esa comparación es una lectura propia, no está en las fuentes.
- La fuente 1 sí habla de pagar tarde: «Some accounts payable arrangements specify an interest penalty or a late fee when the account goes delinquent», y que pagar a tiempo «helps create a credit history for the purchasing firm» (fuente 1, [L]). No dice nada de estirar plazos como práctica ni de su costo con el proveedor.
- Alcance de APQC: 9.6.1.4 «Approve payments» y 9.6.1.8 «Process payments» están dentro de 9.6.1 «Process accounts payable (AP)», no en tesorería (fuente 8, [L]). Tesorería (9.7.2) aparece con «Manage and reconcile cash positions», «Process and oversee electronic fund transfers (EFTs)» (9.7.2.3), «Develop cash flow forecasts» y «Manage cash flows» (9.7.2.5); y 9.7.3.3 «Manage centralized outgoing payments on behalf of subsidiaries» (fuente 8, [L]). Es decir: en APQC el pago de la factura es de cuentas a pagar, y a tesorería le tocan el movimiento de fondos y los pagos centralizados.

Qué decir sobre la fórmula: el libro usa 360 días (convención comercial); otras bases dan cifras algo distintas, y conviene declarar la base.

Prioridades cuando la caja no alcanza: no se encontró una fuente abierta con método. Es un hueco (ver abajo). Lo que se puede afirmar con respaldo es solo el costo de pagar tarde según el libro (intereses y cargos pactados, y efecto en la historia crediticia).

Recurso canónico: OpenStax *Principles of Finance*, cap. 19 sección 19.2, el ejemplo de 36,73 %. Fijarse en que el costo se compara con el de otras fuentes de dinero; no en el descuento en sí.

## 2. La corrida de pagos

Afirmaciones (todas de práctica de software, que cuenta como evidencia de que la práctica existe):

- Odoo: «Instead of processing supplier invoices manually, select multiple bills and generate a single outgoing payment file» (fuente 9, [L]). El lote exige registrar antes cada pago, tiene un tipo (saliente), un diario bancario y un método de pago; «All payments in a batch must use the same payment method» (fuente 9, [L]). Una vez validado, «no additional payments can be added to a batch»; antes de validar se puede borrar (fuente 9, [L]).
- El archivo depende de la región: SEPA en Europa, NACHA en EE. UU., ISO 20022 en el mundo; se sube a mano al portal del banco (fuente 9, [L]).
- Odoo marca las cuentas bancarias de destino como no confiables hasta que se verifican, y eso bloquea las transferencias salientes hacia ellas (fuente 9, [L]). Es un control que une la corrida con la seguridad.
- Al conciliar, el extracto trae un solo débito por el total del lote y el sistema lo reparte entre los pagos; si el banco rechazó una línea, se saca antes de cerrar la conciliación (fuente 9, [L]). La conciliación bancaria es de Contabilidad.
- ERPNext: el Payment Entry «Pay» debita la cuenta del proveedor, acredita el banco o la caja y baja el saldo de la factura; una entrada puede cubrir varias facturas de un mismo proveedor, pero no varios proveedores; el monto aplicado no puede superar lo disponible (fuente 10, [L]). El anticipo a un proveedor se registra antes que la factura y queda sin aplicar hasta que se concilia; las retenciones, comisiones bancarias y diferencias de cambio van en un campo de deducciones, cada una a su cuenta (fuente 10, [L]).
- La página de ERPNext no trata descuentos por pronto pago ni términos de pago (fuente 10, [L]); no se debe inferir que no los tenga.

Pasos de la corrida (síntesis propia sobre las fuentes 8 a 10, a validar con una guía profesional; no hay fuente que la defina así): elegir qué facturas aprobadas se pagan (propuesta), aprobar, armar el lote, generar el archivo, enviarlo al banco, que el banco ejecute, y conciliar. Las firmas conjuntas y la orden de pago como documento no tienen fuente leída. APQC separa 9.6.1.4 «Approve payments» de 9.6.1.8 «Process payments» y de 9.7.2.3 «Process and oversee EFTs» (fuente 8, [L]), lo que respalda que aprobación, proceso y envío son tres actos distintos.

Recurso canónico: la documentación de pagos por lotes (fuente 9) para ver los pasos y los estados; APQC 9.6.1 y 9.7.2 para el vocabulario de procesos. Fijarse en qué se bloquea después de validar y en cómo el sistema trata las cuentas nuevas.

## 3. Medios de pago

Afirmaciones:

- En la encuesta AFP 2026, «87% of organizations report using checks in 2025»; «68% of companies use checks for vendor payments because vendors require payment via checks», un aumento de 16 % respecto de 2024 (según el propio documento); «72% of organizations plan to continue using checks for the foreseeable future» (fuente 5, [L]). Entre quienes usan cheques, el 72 % dice que son el 25 % o menos de sus pagos (fuente 5, [L]).
- El mismo informe dice que entre las empresas de más de mil millones de ingresos, con hasta 25 cuentas de pago el 95 % usa cheques y con más de 100 cuentas el 77 %; lo lee como que, al complicarse las operaciones de pago, se abandonan los cheques (fuente 5, [L]).
- Los métodos más afectados por fraude en 2025: cheques 58 %, débitos ACH 30 %, transferencias 25 %, tarjetas corporativas 21 %, créditos ACH 18 %, pagos rápidos 1 %, criptomonedas 1 %, billeteras móviles 2 % (fuente 5, [L]). Es el porcentaje de organizaciones que sufrieron fraude por ese medio, no una tasa por operación.
- Del cheque: «Mail-theft-enabled check fraud is a large persistent problem» (fuente 5, [L]); los delincuentes interceptan y alteran cheques y desvían los fondos a cuentas fraudulentas (fuente 5, [L]).
- Positive pay: según Wikipedia (fuente secundaria, con aviso propio), la empresa comparte con el banco el registro de los cheques emitidos y el banco solo paga los que figuran, con el mismo importe, beneficiario y número de serie; la variante inversa (reverse positive pay) funciona al revés, y el banco manda a la empresa la lista de lo presentado para que ella diga qué paga (fuente 11, [L]). Hueco: falta una fuente primaria (un banco central o una guía de AFP).
- Tarjeta corporativa: APQC 9.6.3 «Manage corporate credit cards» con sus pasos: políticas y límites, solicitud, emisión, manejo de cuentas, aprobar o cambiar límites, cancelar (fuente 8, [L]). En la encuesta AFP, las tarjetas corporativas o comerciales aparecieron en el 21 % de las organizaciones con fraude (fuente 5, [L]).
- Pagos al exterior: sin fuente leída. Lo que sí hay es el costo de la rapidez: en el informe de IC3 2025, el proceso de congelamiento de fondos separa los incidentes nacionales (3.574) de los internacionales (326), con USD 507.042.623 y USD 171.970.560 congelados respectivamente (fuente 3, [L]), lo que indica que recuperar fondos enviados al exterior es un proceso aparte.

Recurso canónico: el informe AFP 2026 (resumen), páginas 5 y 11, para la mezcla de medios y su exposición; mirar la diferencia entre uso (87 %) y fraude (58 %) por medio.

## 4. Seguridad de los pagos

Cifras del FBI (fuente 3, [L], informe de 2025, publicado en abril de 2026):

- Pérdidas por BEC en 2025: **USD 3.046.598.558**; 2024: USD 2.770.151.146; 2023: USD 2.946.830.270. Denuncias por BEC: 24.768 en 2025, 21.442 en 2024 y 21.489 en 2023.
- En el ranking de pérdidas por tipo de delito, BEC es el segundo, detrás de inversión (USD 8.648.617.756), y delante de soporte técnico falso (USD 2.134.675.818).
- Definición del informe: «BEC is a scam targeting businesses or individuals working with suppliers and/or businesses regularly performing wire transfer payments», con cuentas de correo y otros medios (teléfonos, reuniones virtuales) comprometidos mediante ingeniería social o intrusión «to conduct unauthorized transfer of funds».
- IA: «In 2025, businesses reported losses over $30 million to BEC scams involving AI»; el informe también dice que no todas las tácticas de BEC usan IA.
- Equipo de recuperación de activos (RAT, Financial Fraud Kill Chain): 3.900 incidentes, USD 1.163.919.846 de robo intentado, USD 679.013.183 congelados, 58 % de éxito. Consejo literal: «If you discover a fraudulent transfer, time is of the essence. Immediately, contact your financial institution and request a recall of the funds». Una aclaración: el informe dice que antes la mayoría de los incidentes eran BEC, pero que en 2025 subieron los de soporte técnico y toma de cuentas.
- El total de pérdidas de todos los delitos en 2025 supera los USD 20 mil millones («surpassing the $20 billion mark», literal); el desglose exacto no se verificó en el PDF.
- Alerta anterior (fuente 4, [L]): de octubre de 2013 a diciembre de 2023, BEC causó USD 55.499.915.582 de pérdidas expuestas, nacionales e internacionales, en 305.033 incidentes. Medida recomendada textual en el alerta: confirmar los pedidos de cambio de datos de cuenta por un canal distinto o con doble factor.
- Advertencia del FBI sobre su propio dato: son denuncias recibidas, y el FBI dice que la cifra puede ser mayor (visto en la prensa; el texto leído no lo repite literalmente, por eso va como [S]). No usar como incidencia.

Cifras de AFP (fuente 5, [L]; encuesta de enero de 2026, 465 profesionales, datos de 2025; solo organizaciones de EE. UU., autoseleccionadas entre socios de AFP):

- 76 % sufrió fraude de pagos intentado o real en 2025 (81 % de las de al menos mil millones de ingresos; 67 % de las más chicas). Cuidado: 76 % cuenta intentos.
- BEC: 74 % de las organizaciones fue afectada en 2025 (63 % en 2024, según la fuente 7, [L]); y como fuente de fraude, el 70 % citó «Business email compromise (BEC)/Fraudulent email». Son dos medidas distintas: el 74 % es prevalencia entre todas; el 70 % es el porcentaje entre las que sufrieron fraude.
- Los delincuentes se hacen pasar por proveedores o directivos y piden cambios en las instrucciones de pago; el 39 % sigue recibiendo correos genuinos interceptados (fuente 5, [L]); el 85 % recibió correos falseados (spoofed) y más de la mitad, dominios parecidos con una o dos letras de diferencia (fuente 7, [L]).
- Fraude de facturas: 26 %; instrucciones de ACH o transferencia manipuladas: 33 %; deepfake: 7 % (fuente 5, [L]).
- Medio usado en BEC: transferencia 49 % (63 % en 2024), débito ACH 34 %, cheque 33 %, crédito ACH 31 % (50 % en 2024), pagos en tiempo real 6 % (fuente 5, [L]).
- Pérdidas: entre las organizaciones con menos de mil millones de ingresos y fraude, el 48 % tuvo pérdida y el 24 % no recuperó nada; entre las grandes, 66 % y 19 % (fuente 5, [L]). Recuperación en general: 30 % recuperó más del 75 %; 20 % nada (fuente 5, [L]). «For every 100 attempts by a fraudster, 20 are successful».
- Quién lo detecta: Tesorería es el área que más descubre el intento (83 %) y el fraude real (55 %) (fuente 5, [L]).
- Controles y su eficacia (porcentaje de organizaciones que lo implementó; entre paréntesis, «muy efectivo»): políticas para verificar cambios en facturas, depósitos y datos de contacto, 96 % (58 %); verificar el pedido de transferencia llamando a un contacto autorizado del beneficiario con un teléfono de los registros oficiales, no del correo, 94 % (63 %); firma de la gerencia por encima de un umbral, 94 % (52 %); prohibir iniciar pagos por correo u otros mensajes poco seguros, 91 % (53 %); contraseñas conocidas solo por las dos partes en una transferencia, 42 % (52 %); capacitación, 96 % (42 %) (fuente 5, [L]). El control mejor valorado es la devolución de llamada con un teléfono de los registros, que es el «canal independiente» de las guías.
- Un caso anónimo del propio informe: un delincuente tomó la casilla de un proveedor clave, mandó facturas falsas que pasaron todas las aprobaciones y pidió cambiar la cuenta bancaria; el cambio se cargó antes de que Tesorería lo confirmara (fuente 5, [L]). Otro: AP llamó al número del correo, que era del delincuente; el sistema no actualizó los datos, el pago fue a la cuenta correcta, el delincuente reclamó, se mandó una transferencia a la cuenta falsa, fue devuelta, y no se perdió plata (fuente 5, [L]). La primera ilustra la falla que une aprobación y alta de datos; la segunda, el límite de «llamar al número que viene en el correo».
- Dos puntos de método: la encuesta no es muestra aleatoria; y cuando la nota diga «74 %» tiene que decir «de organizaciones que respondieron, EE. UU., 2025».

Pagos duplicados y su detección: **no se encontró fuente primaria**. Sin cifra. Lo que ofrecen las fuentes leídas sobre prevención es parcial: un pago por lote queda bloqueado después de validado (fuente 9), y la aplicación del pago contra la factura impide asignar más del monto disponible (fuente 10). Eso no equivale a detectar duplicados (misma factura cargada dos veces con otro número, mismo proveedor y mismo importe en fechas cercanas); esa idea es explicación propia, sin respaldo, y no debe presentarse como práctica comprobada.

Frontera: el fraude interno con proveedores ficticios (ACFE) ya está en `autorizaciones.md`; acá importa el engaño externo que cambia dónde va un pago legítimo. El fraude con tarjeta cobrada en un sitio (contracargos) es de Comercio electrónico/Pagos, no de esta vertical.

Recurso canónico: AFP *Payments Fraud and Control Survey* (la edición más nueva), la página 12 de BEC, con la tabla de controles y su eficacia; y el informe IC3 2025, la tabla de pérdidas y la sección de la Financial Fraud Kill Chain para el tiempo de reacción. Para la verificación: PSA240911.

## 5. APQC

- 9.6 «Process accounts payable and expense reimbursements» (10733): 9.6.1 AP (verificar el archivo de pagos contra el maestro de proveedores de compras, 9.6.1.1; auditar facturas y datos clave, 9.6.1.3; aprobar pagos, 9.6.1.4; investigar excepciones, 9.6.1.7; procesar pagos, 9.6.1.8; conservar registros, 9.6.1.10); 9.6.2 reintegros de gastos; 9.6.3 tarjetas corporativas (fuente 8, [L]).
- 9.7 «Manage treasury operations» (10734): 9.7.1 políticas y procedimientos; 9.7.2 caja (posición, equivalentes, EFT, pronóstico, flujos, relaciones bancarias, comisiones); 9.7.3 bancos internos; 9.7.4 deuda e inversión; 9.7.5 riesgo y cobertura (fuente 8, [L]).
- Observación útil: APQC deja la corrida en cuentas a pagar (9.6.1.1: «Verify AP pay file with purchase order vendor master file»). Dónde termina cuentas a pagar y empieza tesorería depende de la organización; el campo no la parte igual que el árbol propuesto.

## Cómo divide el campo esta vertical (si el árbol debería cambiar)

El árbol propuesto separa bien los cuatro componentes, con dos observaciones:

1. Las fuentes de práctica y de marco tratan la corrida de pagos como parte de cuentas a pagar (APQC 9.6.1, documentación de software de lotes), no como tesorería. En el árbol del tema conviene decir en una línea que es el punto de encuentro de cuentas a pagar y tesorería, y que en una empresa chica la hace la misma persona.
2. El libro de texto (OpenStax) trata el descuento por pronto pago dentro del crédito comercial como financiamiento (capítulo 19, capital de trabajo), no como programación de pagos. Se sugiere que la nota de programación enlace con la de financiamiento de corto plazo (crédito de proveedores) y que la fórmula viva en una sola de las dos.

## Huecos

- Prioridades de pago cuando la caja no alcanza, y estirar plazos (costo con el proveedor): sin fuente abierta con método leída. Candidatos no leídos: Petersen y Rajan (1997) sobre crédito comercial; EU Directive 2011/7 sobre morosidad (intentada con dos URLs de EUR-Lex y una descarga directa; las páginas llegaron vacías, ley sin leer); guías de AFP o de ACT.
- Firmas conjuntas, orden de pago como documento, aprobación por niveles en la corrida: sin fuente.
- Pagos al exterior (SWIFT, comisiones, gastos compartidos, tipo de cambio): sin fuente leída.
- Pagos duplicados: ni cifra ni método de detección con fuente.
- Positive pay y filtros de débito: solo Wikipedia; falta fuente primaria (banco, Federal Reserve, AFP).
- ISO 20022 como formato de archivo al banco: citado solo desde la documentación de Odoo; falta el estándar.
- IC3: el PDF se leyó con extracción de texto; una lectura de los gráficos (por ejemplo el tipo de transacción de BEC) no fue segura y no se usa. El comunicado y la nota de Nacha repiten la encuesta de AFP y no aportan fuente nueva.
- AFP: el informe completo es solo para socios; no se leyó el capítulo de recuperación de fondos ni el detalle de por qué los cambios de cuenta fallan. Solo EE. UU.
- Fuente local: no se buscó nada de Argentina (CBU, transferencias inmediatas, cheques; eso es de la nota de Argentina).
- Presupuesto de búsquedas web de la sesión agotado: tras la primera ronda no hubo más búsquedas.
