---
resumen: >-
  La seguridad de los pagos son los controles que impiden que un pago legítimo termine en la cuenta de un tercero: el engaño por correo comprometido que cambia los datos bancarios de un proveedor, el cheque robado o alterado y el pago que sale dos veces.
estado: vigente
estabilidad: semi
fuentes:
  - "FBI IC3, 2025 Internet Crime Report (abril de 2026) (leído en las partes citadas, extraído a texto): https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf"
  - "FBI IC3, anuncio de servicio público PSA240911 sobre BEC (2024) (leído): https://www.ic3.gov/PSA/2024/PSA240911"
  - "AFP, 2026 Payments Fraud and Control Survey Report: Key Highlights (abril de 2026; 465 profesionales; datos de 2025; solo EE. UU.) (leído el resumen; el informe completo es para socios): https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf"
  - "Nacha, nota sobre BEC (mayo de 2026), que resume la misma encuesta de AFP (leído): https://www.nacha.org/news/business-email-compromise-attempts-rose-sharply-2025-report-finds"
  - "APQC, Process Classification Framework 7.4 (2024), 9.7.6 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Documentación de pagos por lotes de un sistema de gestión abierto, versión 18 (leído; como evidencia de práctica): https://www.odoo.com/documentation/18.0/applications/finance/accounting/payments/batch.html"
  - "Citi, What is Check Positive Pay? (leído): https://www.citi.com/banking/small-business-guide/business-services/positive-pay"
  - "Commerce Bank, Positive Pay (leído): https://www.commercebank.com/corporate/payments-treasury/fraud-prevention/positive-pay"
  - "Oracle, Understanding Positive Pay, JD Edwards 9.2 (leído; como evidencia de práctica): https://docs.oracle.com/en/applications/jd-edwards/financials/9.2/eoaap/understanding-positive-pay.html"
  - "Tesoreria/.investigacion/caja-y-liquidez-verificacion.md (2026-11-27)"
  - "Tesoreria/.investigacion/pagos-a-proveedores.md, secciones 3 y 4 (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 6 (2026-11-27)"
  - "Tesoreria/.investigacion/pagos-y-politica-verificacion.md (2026-11-27)"
aliases: [seguridad de los pagos, fraude de pagos, payments fraud, compromiso del correo empresarial, business email compromise, BEC, fraude del cambio de cuenta, vendor impersonation, fraude del CEO, pago duplicado, duplicate payment, positive pay, devolución de llamada, callback verification]
creado: 2026-11-27
revisado: 2026-11-27
---

# Seguridad de los pagos

La seguridad de los pagos son los controles que impiden que un pago legítimo termine en la cuenta de un tercero: el engaño por correo comprometido que cambia los datos bancarios de un proveedor, el cheque robado o alterado y el pago que sale dos veces.

El riesgo viene de afuera. El fraude de alguien de adentro, como el proveedor inventado o la factura inflada, está en [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md) y en [auditoría y fraude](../../Contabilidad/Control-interno/auditoria-y-fraude.md), con las cifras de la ACFE. El fraude con tarjeta en una venta online y sus contracargos, que es plata que entra, está en [fraude y contracargos](../../Comercio-electronico/Pagos/fraude-y-contracargos.md). Acá la factura es real, el proveedor existe y la deuda es cierta: lo que se ataca es a dónde va el pago. APQC tiene un proceso para esto dentro de la tesorería, 9.7.6 «Manage financial fraud/dispute cases».

## El correo comprometido que cambia la cuenta del proveedor

El FBI define el compromiso del correo empresarial (BEC, por *business email compromise*) como «a scam targeting businesses or individuals working with suppliers and/or businesses regularly performing wire transfer payments». El delincuente compromete o imita una cuenta de correo, un teléfono o una reunión virtual, por ingeniería social o por intrusión, «to conduct unauthorized transfer of funds» (*2025 Internet Crime Report*).

La forma típica, según la encuesta de AFP de 2026, es hacerse pasar por un proveedor o un directivo y pedir un cambio en las instrucciones de pago. El 39 % de las organizaciones que respondieron sigue recibiendo correos genuinos interceptados, es decir, mandados desde la casilla real del proveedor. Según el resumen de Nacha de la misma encuesta, el 85 % recibió correos falsificados y más de la mitad, dominios que difieren del verdadero en una o dos letras.

El informe de AFP cuenta un caso sin nombres. Un delincuente tomó la casilla de un proveedor clave, mandó facturas falsas que pasaron todas las aprobaciones y pidió cambiar la cuenta bancaria; el cambio se cargó en el sistema antes de que la tesorería lo confirmara. La falla, en la lectura de esta base, es que la aprobación de la factura y el alta de los datos bancarios corrieron por caminos que no se controlaban entre sí.

## Lo que dicen las cifras del FBI

Las cifras del FBI son denuncias recibidas por su centro de quejas (IC3) en Estados Unidos, no una medida de cuánto fraude hay: según la prensa que resume el informe, el propio FBI advierte que la cifra real puede ser mayor.

| Año | Denuncias por BEC | Pérdidas denunciadas por BEC (USD) |
|---|---|---|
| 2023 | 21.489 | 2.946.830.270 |
| 2024 | 21.442 | 2.770.151.146 |
| 2025 | 24.768 | 3.046.598.558 |

En 2025, el BEC fue el segundo delito por pérdidas, detrás del fraude de inversión (USD 8.648.617.756) y delante del falso soporte técnico (USD 2.134.675.818). El informe dice que en 2025 las empresas denunciaron pérdidas de más de USD 30 millones por BEC con inteligencia artificial, y aclara que no todas las tácticas de BEC la usan. En el período más largo, el anuncio PSA240911 del FBI suma USD 55.499.915.582 de pérdidas expuestas por BEC entre octubre de 2013 y diciembre de 2023, en 305.033 incidentes, nacionales e internacionales.

## Lo que dice la encuesta de AFP

La encuesta de AFP es la otra fuente, independiente del FBI: 465 profesionales de tesorería y finanzas de organizaciones de Estados Unidos, encuestados en enero de 2026 sobre lo que les pasó en 2025. No es una muestra aleatoria: respondieron socios de AFP que quisieron. Cada porcentaje se lee como «de las organizaciones que respondieron, EE. UU., 2025».

- El 76 % sufrió fraude de pagos, intentado o consumado: el 81 % de las que facturan al menos mil millones de dólares y el 67 % de las más chicas. La cifra cuenta intentos.
- El 74 % fue blanco de BEC, contra el 63 % en 2024 según Nacha. Entre las que sufrieron fraude, el 70 % nombró al BEC o al correo fraudulento como fuente.
- Por tipo de engaño, el informe da 33 % de instrucciones de transferencia manipuladas, 26 % de fraude de facturas y 7 % de *deepfake*.
- Los medios usados en el BEC fueron la transferencia (49 %; 63 % en 2024), el débito ACH (34 %), el cheque (33 %), el crédito ACH (31 %; 50 % en 2024) y los pagos en tiempo real (6 %). ACH es la red de pagos automáticos entre bancos de Estados Unidos.
- La tesorería es el área que más detecta: el 83 % de los intentos y el 55 % de los fraudes consumados.
- Según el informe, «For every 100 attempts by a fraudster, 20 are successful».

La pérdida cambia con el tamaño. Entre las organizaciones de menos de mil millones de ingresos que sufrieron fraude, el 48 % perdió plata y el 24 % no recuperó nada; entre las más grandes, el 66 % y el 19 %. En el total, el 30 % recuperó más del 75 % de lo perdido y el 20 % no recuperó nada.

## El cheque, el medio más atacado

En la misma encuesta, el 87 % de las organizaciones usó cheques en 2025, y el cheque fue el medio con más organizaciones afectadas por fraude: 58 %, contra 30 % del débito ACH y 25 % de la transferencia. Es el porcentaje de organizaciones, tal como rotula el informe sus gráficos (el 76 % sufrió algún fraude, real o intentado), no una tasa por operación; otros gráficos del informe dicen en cambio «Experiencing Payments Fraud» y este no. AFP lo atribuye al robo de correspondencia: «Mail-theft-enabled check fraud is a large persistent problem»; el cheque se intercepta, se altera y se deposita en una cuenta del delincuente. Qué medio conviene para cada pago, y quién lo puede revertir, está en [medios de cobro y pago](../Caja-y-liquidez/medios-de-cobro-y-pago.md); el cheque y el cheque electrónico en Argentina, en [tesorería en Argentina](../tesoreria-en-argentina.md).

El control específico del cheque es el *positive pay*. La empresa le manda al banco un archivo con los cheques que emitió, con número e importe. El banco compara con él cada cheque que se presenta y retiene los que difieren, y la empresa aprueba o rechaza esa excepción antes de que el banco pague. La versión *payee positive pay* agrega el nombre del beneficiario, que sirve contra el cheque alterado. En la variante inversa, el banco le manda a la empresa los cheques presentados y ella confirma cuáles se pagan. Lo describen dos bancos de Estados Unidos y la documentación de un sistema de gestión; no se encontró una guía de un regulador, y no se leyó cómo funciona en Argentina.

## Los controles y cuánto sirven según quien los usa

La encuesta de AFP preguntó qué controles contra el BEC tenían las organizaciones y si los consideraban muy efectivos:

| Control | Lo tiene | Lo considera muy efectivo |
|---|---|---|
| Verificar el pedido de transferencia llamando a un contacto autorizado, con un teléfono de los registros propios y no del correo | 94 % | 63 % |
| Políticas para verificar cambios en facturas, cuentas de depósito y datos de contacto | 96 % | 58 % |
| Prohibir iniciar pagos por correo u otros mensajes poco seguros | 91 % | 53 % |
| Firma de la gerencia por encima de un umbral | 94 % | 52 % |
| Contraseñas que solo conocen las dos partes de la transferencia | 42 % | 52 % |
| Capacitación | 96 % | 42 % |

El mejor valorado es la devolución de llamada a un número que la empresa ya tenía. El FBI recomienda lo mismo en su anuncio PSA240911: confirmar cada pedido de cambio de datos de cuenta por un canal distinto o con doble factor. El segundo caso del informe de AFP muestra el límite: cuentas a pagar llamó al número que venía en el correo, que era del delincuente. El sistema no había actualizado los datos y el pago fue a la cuenta correcta. El delincuente reclamó, se le mandó una transferencia a la cuenta falsa, la transferencia fue devuelta y no se perdió plata.

Las reglas de quién aprueba un cambio de cuenta bancaria y que el cambio vuelva a pedir aprobación están en [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md). El umbral de firma y la prohibición de pagar por pedidos de correo los fija la [política de tesorería](../politica-de-tesoreria.md).

## Lo que un sistema puede impedir

Uno de los sistemas de gestión abiertos documenta un control que une la [corrida de pagos](corrida-de-pagos.md) con esta nota: marca como no confiable cada cuenta bancaria de destino nueva hasta que alguien la verifica, y mientras tanto bloquea las transferencias salientes hacia ella. Por inferencia de esta base, con las fuentes de arriba, un sistema además puede:

- Guardar el teléfono y el contacto de verificación del proveedor en su ficha, separados del correo, y pedir que quien aprueba el cambio de cuenta registre a quién llamó.
- Avisar cuando una factura llega con datos bancarios distintos de los de la ficha.
- Mostrar en la aprobación de la corrida qué pagos van a una cuenta que cambió hace pocos días.

## Cuando el pago ya salió

El FBI es directo: «If you discover a fraudulent transfer, time is of the essence. Immediately, contact your financial institution and request a recall of the funds». Su equipo de recuperación de activos intervino en 3.900 incidentes en 2025, con USD 1.163.919.846 de robo intentado y USD 679.013.183 congelados, un 58 % de éxito. El informe dice que antes la mayoría de esos incidentes eran BEC y que en 2025 crecieron los de falso soporte técnico y toma de cuentas. El congelamiento separa lo nacional de lo internacional: 3.574 incidentes nacionales con USD 507.042.623 congelados, y 326 internacionales con USD 171.970.560. Que recuperar una transferencia al exterior sea más difícil es lectura de esta base sobre esos números.

## El pago duplicado

El pago duplicado es la misma deuda pagada dos veces: la misma factura cargada con otro número, el mismo proveedor y el mismo importe en fechas cercanas, o una factura que entra en dos corridas. Los dos sistemas abiertos leídos tienen defensas parciales: el lote validado no admite pagos nuevos, y un pago no puede aplicar más que el monto disponible. Eso no detecta una factura cargada dos veces.

> [!NOTE] Sin fuente todavía: cuántos pagos duplicados ocurren y cómo se detectan. Los controles que circulan como práctica, sin respaldo leído, son la unicidad de proveedor, número de factura e importe al registrar; marcar la factura como «en pago» al armar la corrida; revisar los pagos al mismo proveedor por igual importe en una ventana corta; y conciliar contra el extracto.
