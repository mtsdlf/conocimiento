---
resumen: >-
  La fiscalización es cómo el fisco comprueba que lo declarado es cierto (cruces de información, selección por riesgo, requerimientos e inspecciones), y las sanciones son lo que cuesta no cumplir: intereses por el tiempo, multas por omitir o por defraudar, hasta que la deuda prescribe o se cancela, a veces con un plan de pagos.
estado: vigente
estabilidad: estable
fuentes:
  - "FMI, Tax Law Design and Drafting, vol. 1 (1996), cap. 4, secciones II.E (Audits and Investigations), II.H (Collection, Installment Payment Arrangements), II.J (Interest), II.K.10 (Limitations) y III (Taxpayer Compliance and Sanctions): https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch4.pdf"
  - "CIAT, Modelo de Código Tributario (2015), índice y tabla de cambios (la extracción del PDF perdió letras y cifras): https://www.ciat.org/Biblioteca/DocumentosTecnicos/Espanol/2015_Modelo_Codigo_Tributario_CIAT.pdf"
  - "World Bank Group y PwC, Paying Taxes 2020, secciones de tecnología y post-filing index (leído el 2026-11-27): https://archive.doingbusiness.org/content/dam/doingBusiness/pdf/db2020/PayingTaxes2020.pdf"
  - "Impuestos/.investigacion/cumplimiento.md (2026-11-27)"
aliases: [fiscalización, inspección, auditoría fiscal, tax audit, verificación, requerimiento, cruce de información, matching, gestión de riesgo de cumplimiento, compliance risk management, determinación de oficio, intereses resarcitorios, intereses moratorios, late payment interest, multa, sanción, penalty, omisión, defraudación, evasión, tax evasion, prescripción, statute of limitations, plan de pagos, plan de facilidades, installment agreement, moratoria, amnistía fiscal, tax amnesty, apropiación indebida de tributos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Fiscalización y sanciones

La fiscalización es cómo el fisco comprueba que lo declarado es cierto (cruces de información, selección por riesgo, requerimientos e inspecciones), y las sanciones son lo que cuesta no cumplir: intereses por el tiempo, multas por omitir o por defraudar, hasta que la deuda prescribe o se cancela, a veces con un plan de pagos.

Es la otra cara del [cumplimiento](cumplimiento.md). En un sistema de autoliquidación (ver [declaración y pago](declaracion-y-pago.md)) el contribuyente calcula y el fisco revisa después; lo que el fisco puede revisar depende de los [registros fiscales](registros-fiscales.md) y de cada [comprobante fiscal](comprobante-fiscal.md).

## Cómo elige el fisco a quién revisar

Ningún fisco puede revisar a todos, así que selecciona, cada vez más en forma automática.

- Cruces de información. El fisco compara lo declarado con lo que informan terceros (clientes, proveedores, bancos, agentes de recaudación). Una diferencia dispara un aviso o un requerimiento.
- Gestión de riesgo. El fisco concentra las inspecciones en los de mayor riesgo (descripción de la base; la guía de la OCDE no se pudo abrir). Según lo leído de *Paying Taxes 2020*, las administraciones usan los sistemas en línea para hacer «comprehensive and faster risk assessment and compliance checks on returns», y distingue entre «random audits versus risk-based audits».
- Señales propias. Un pedido de devolución, una rectificativa a favor o un saldo a favor que crece llaman la atención (inferencia de la base). Según el mismo informe, en Chipre el aumento de las inspecciones sobre pedidos de devolución llevó el tiempo para cobrarla de 7,5 semanas en 2014 a 43,8 en 2018.

> [!NOTE] Sin fuente todavía: la guía de gestión de riesgo de cumplimiento de la OCDE («Compliance Risk Management», 2004) y la serie *Tax Administration* de la OCDE, que no se pudieron abrir.

## De la carta al inspector

La fiscalización tiene grados, de menos a más intrusivos (orden de la base; cada país usa sus nombres):

1. Control masivo. El sistema del fisco detecta una diferencia y manda un aviso: una declaración no presentada, un crédito fiscal que el proveedor no declaró.
2. Requerimiento. El fisco pide por escrito información o documentación sobre algo puntual, con un plazo para contestar.
3. Inspección. Un inspector revisa los libros, los comprobantes y los sistemas de un período, en el fisco o en la empresa.
4. Determinación de oficio. Si el fisco concluye que se debía más, lo determina él y lo reclama. El contribuyente puede discutirlo en un recurso administrativo y después en la justicia.

El FMI incluye entre los derechos del contribuyente las inspecciones en tiempo y lugar razonables (las demás garantías, como audiencia y recursos, no se leyeron). Si los registros no están completos, el fisco puede determinar por métodos indirectos (presunciones a partir de otros datos). El derecho procesal tributario queda fuera de este tema.

## Intereses: el precio del tiempo

El interés se cobra por pagar tarde, haya culpa o no. El FMI separa con claridad interés y multa: «Interest must be assessed on every late payment of tax or penalty, as well as on every payment due from the treasury to the taxpayer. It should be stressed that interest is not the same as a penalty due for noncompliance. Interest reflects the time value of money and should therefore never be waived or subject to compromise.»

Del mismo texto salen tres criterios de diseño:

- La tasa se fija por referencia a una tasa pública (la del banco central o la de las letras del tesoro).
- Debería superar la tasa común del mercado, para que a nadie le convenga financiarse dejando de pagar impuestos («borrowing from the government»).
- El interés se aplica también a lo que el tesoro le debe al contribuyente.

Las tasas argentinas van en [impuestos en Argentina](../impuestos-en-argentina.md).

## Multas: omisión y defraudación

Las multas castigan el incumplimiento y se gradúan según la intención. Los códigos suelen separar tres familias (síntesis de la base a partir del FMI y del CIAT):

| Infracción | Qué es | Cómo se mide la multa |
|---|---|---|
| Formal | no presentar una declaración, no contestar un requerimiento, no llevar libros, no emitir factura | monto fijo |
| Omisión | pagar de menos por error o negligencia, sin intención de engañar | porcentaje del impuesto omitido |
| Defraudación | pagar de menos con engaño: facturas falsas, ventas ocultas, libros dobles | porcentaje mayor del impuesto evadido; si es grave, delito penal aparte |

El Modelo de Código Tributario del CIAT agrupa las infracciones materiales «por omisión, inexactitud, u obtención indebida de devoluciones», y trata el delito tributario, doloso, por separado.

El FMI da órdenes de magnitud para el diseño, no valores de un país: las multas «should probably not exceed 25 percent of the amount of underpayment for negligence or 50 percent for intentional underpayment», y «it is unlikely that a civil penalty for fraud should exceed 100 percent of the amount of underpayment». Cita la recomendación de un grupo de trabajo del fisco de Estados Unidos: 20 % por negligencia y 100 % por fraude.

Reparar a tiempo baja la multa. El modelo del CIAT prevé que quien corrige y paga espontáneamente, antes de que el fisco actúe, pague un recargo y evite la sanción; y, según su índice, que la sanción se reduzca si se repara. El FMI propone algo parecido: reducir la multa (por ejemplo, a la mitad) si se llega a un acuerdo temprano. Los porcentajes de cada país los fija su ley.

## Prescripción: cuándo el fisco ya no puede reclamar

La prescripción pone un límite al tiempo en que el fisco puede determinar y cobrar un impuesto. Según el FMI, «There should be a limitation on the period during which an assessment may be made. However, this limitation should be waived in the event of fraud». Sus ejemplos:

| País | Plazo general | Si hubo fraude |
|---|---|---|
| Reino Unido | seis años desde el período | veinte años (también por negligencia) |
| Estados Unidos | tres años desde la presentación de la declaración | sin límite (también si no se presentó) |

Ejemplos del manual del FMI de 1996; los plazos vigentes no se verificaron.

El Modelo del CIAT de 2015 incluye la prescripción como forma de extinguir la obligación, fija un plazo absoluto máximo (según su índice y su tabla de cambios). La consecuencia práctica es la de [registros fiscales](registros-fiscales.md): los comprobantes se guardan por lo menos mientras el período no prescribió.

## Planes de pago y moratorias

Quien no puede pagar una deuda de una vez puede pedir un plan de pagos. El FMI recomienda que la ley autorice al fisco a acordar con el contribuyente «to pay the tax over time, in cases where the taxpayer cannot pay the amount of assessed tax immediately», y aclara que la prórroga no frena los intereses. Como financiamiento (si conviene un plan o un préstamo) es del tema Tesorería y finanzas de la empresa en marcha (todavía no escrito).

Una moratoria es un régimen excepcional y temporal para regularizar deudas viejas en mejores condiciones; una amnistía perdona también lo no declarado (definiciones de la base, sin fuente leída). Si una moratoria condona intereses, contradice lo que dice el FMI de que el interés nunca debería condonarse (inferencia de la base).

> [!NOTE] Sin fuente todavía: un estudio sobre el efecto de las moratorias y amnistías fiscales en el cumplimiento posterior.

## El agente que no ingresó lo retenido

La plata que junta una empresa como [agente de recaudación](../Recaudacion-en-la-fuente/agente-de-recaudacion.md) no es suya. No depositarla es más grave que no pagar un impuesto propio: el tercero ya pagó y el agente se quedó con dinero del fisco. Por qué el agente responde con sus bienes, y el caso argentino, están en esa nota.

Las fuentes agregan dos piezas de diseño:

- Responden personas. El FMI propone una multa a la «responsible physical person», el directivo que debía retener y depositar; el porqué no quedó registrado en lo leído. En Estados Unidos existe solo para no retener o no depositar lo retenido, responde junto a la persona jurídica y por el monto no ingresado.
- Menos facilidades. El Modelo del CIAT admite el aplazamiento de deudas retenidas o percibidas solo en forma excepcional.

Para quien sufrió la retención, el certificado del agente prueba el pago aunque el agente no lo haya depositado (lectura de la base; depende de cada régimen). Ver [pagos a cuenta](../Recaudacion-en-la-fuente/pagos-a-cuenta.md).

Para leer más: FMI, *Tax Law Design and Drafting*, vol. 1, cap. 4, sección III, por cuánto debería costar cada incumplimiento y por qué multas muy altas son contraproducentes; y el Modelo de Código Tributario del CIAT (2015), título de infracciones y sanciones.
