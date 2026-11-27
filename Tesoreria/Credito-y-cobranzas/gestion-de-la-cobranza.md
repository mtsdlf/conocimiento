---
resumen: >-
  La gestión de la cobranza es el trabajo de convertir en plata las facturas vencidas: reclamarlas con una secuencia de recordatorios, resolver las disputas y deducciones, negociar acuerdos y decidir cuándo una deuda pasa a legales o se da por incobrable, midiendo el resultado con el DSO y el índice de eficacia de cobranza.
estado: borrador
estabilidad: semi
fuentes:
  - "Credit Research Foundation, Performance Measures (2016) (leído): https://www.crfonline.org/wp-content/uploads/2017/12/PerformanceMeasures.pdf"
  - "APQC, Process Classification Framework 7.4 (2024), 9.2.4 y 9.2.5 (leído, los títulos): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "OpenStax, Principles of Finance (2022), 19.4 Receivables Management (leído, la definición del DSO): https://openstax.org/books/principles-finance/pages/19-4-receivables-management"
  - "Wikipedia, Days sales outstanding, que cita a Houston y Brigham (2009), Fundamentals of Financial Management, p. 90 (según su resumen): https://en.wikipedia.org/wiki/Days_sales_outstanding"
  - "Wikipedia, Dunning (process) (según su resumen): https://en.wikipedia.org/wiki/Dunning_letter"
  - "ERPNext, Dunning (como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/dunning"
  - "Tesoreria/.investigacion/credito-y-cobranzas.md, sección 2 (2026-11-27)"
  - "Tesoreria/.investigacion/caja-y-cobranzas-segunda-ronda.md, sección 6 (2026-11-27)"
  - "Tesoreria/.investigacion/fundamentos-y-contraria.md, sección 4.2 (2026-11-27)"
aliases: [gestión de la cobranza, cobranza, collections, collections management, gestión de mora, recordatorios de pago, dunning, secuencia de cobranza, disputas, deducciones, deductions management, DSO, days sales outstanding, días de cobro, best possible DSO, DSO mejor posible, CEI, collection effectiveness index, índice de eficacia de cobranza, average days delinquent, días de atraso promedio]
creado: 2026-11-27
revisado:
---

# Gestión de la cobranza

La gestión de la cobranza es el trabajo de convertir en plata las facturas vencidas: reclamarlas con una secuencia de recordatorios, resolver las disputas y deducciones, negociar acuerdos y decidir cuándo una deuda pasa a legales o se da por incobrable, midiendo el resultado con el DSO y el índice de eficacia de cobranza.

Empieza donde termina el [crédito a clientes](credito-a-clientes.md): el cliente ya tiene un límite y una condición de pago, y la factura venció o está por vencer. Termina cuando el cobro llega y se [aplica](aplicacion-de-cobros.md) a las facturas. Lo que se mide acá son los días de cobro, uno de los tres términos del [capital de trabajo](../Caja-y-liquidez/capital-de-trabajo.md).

## El ciclo de la mora según APQC

APQC descompone el proceso 9.2.4 «Manage and process collections» en siete pasos, que ordenan el trabajo de la mora al default:

1. Establecer la política para cuentas morosas (9.2.4.1).
2. Analizar los saldos morosos (9.2.4.2).
3. Escribir y negociar con los morosos (9.2.4.3).
4. Discutir la resolución con las áreas internas (9.2.4.4), como ventas o logística.
5. Procesar ajustes o castigar saldos (9.2.4.5).
6. Hacer la recuperación (9.2.4.6, «Perform recovery workout»).
7. Administrar las cuentas en default (9.2.4.7).

El análisis del paso 2 parte de la antigüedad de saldos, que agrupa la deuda en tramos por días de vencida y dice a quién llamar primero. El informe lo arma la contabilidad desde las [cuentas corrientes](../../Contabilidad/Registro/cuentas-corrientes.md); la cobranza lo usa.

## La secuencia de recordatorios

La secuencia de recordatorios (en inglés, dunning) es la comunicación metódica con el cliente que debe. Según el resumen de una enciclopedia abierta, va de recordatorios amables a cartas y llamadas cada vez más firmes, y las reglas cambian por país: el hostigamiento a consumidores suele estar prohibido.

Un sistema abierto la modela así, como evidencia de práctica:

- Un documento de reclamo que junta las cuotas vencidas de una o varias facturas del cliente, calcula interés y cargos, guarda la carta enviada y queda vinculado al pago que llega después. No reemplaza la factura ni crea una venta.
- Un tipo de reclamo por etapa (primer recordatorio, segundo, aviso final), cada uno con su cargo fijo, su tasa de interés anual, el texto de la carta y la cuenta de ingreso donde va el cargo.
- Estados: borrador, sin resolver, resuelto y cancelado.

La documentación de ese sistema no menciona período de gracia. El interés que se le cobra al moroso puede tener piso legal: en la Unión Europea, la tasa del Banco Central Europeo más ocho puntos y un monto fijo por factura, contados en [crédito a clientes](credito-a-clientes.md#lo-que-dice-la-ley-europea-sobre-plazos-y-mora).

> [!NOTE] Sin fuente todavía: los plazos de la secuencia (cuántos días antes del vencimiento se avisa, cuándo va el segundo reclamo, cuándo el aviso final) y el criterio para pasar a legales o castigar una deuda (monto, días). APQC nombra los pasos 9.2.4.5 a 9.2.4.7 pero no dice cuándo se dan.

Para quien construye el sistema, una lectura de esta base: cada etapa tiene que saber si el cliente ya pagó, aunque el cobro no esté aplicado todavía. Reclamarle a quien pagó ayer es el error de cobranza más visible para el cliente, y nace casi siempre en un cobro sin [aplicar](aplicacion-de-cobros.md#el-cobro-sin-identificar).

## Acuerdos de pago, legales y castigo

Cuando el cliente no puede pagar todo, se negocia un acuerdo (APQC 9.2.4.3 y 9.2.4.6): un plan de cuotas, una quita o un cambio de condición. Si no hay acuerdo, la deuda pasa a legales o se castiga.

Castigar es dar la deuda por incobrable. La decisión y quién la autoriza son de tesorería, con niveles fijados en [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md); el asiento contra la previsión para incobrables, y qué pasa si el cliente paga después, están en [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md).

> [!NOTE] Sin fuente todavía: cómo se arma un acuerdo de pago (cuotas, intereses, qué pasa con el límite mientras dura) y el procedimiento de paso a legales.

## Disputas y deducciones

Una deducción es lo que el cliente descuenta por su cuenta al pagar: una devolución, una diferencia de precio, una retención. Una disputa es el desacuerdo sobre si debe lo que se le factura. Las dos frenan la cobranza, y la Credit Research Foundation las cuenta entre los componentes del DSO («disputes and customer dissatisfaction (deductions)»).

APQC les da un proceso propio, 9.2.5 «Manage and process adjustments/deductions», con seis pasos: fijar la política de ajustes, analizarlos, escribir y negociar con el cliente, discutir la resolución con las áreas internas, preparar facturas de «chargeback» y procesar los asientos. Por el nombre, el «chargeback» de 9.2.5.5 es volver a facturarle al cliente una deducción que no correspondía (lectura de esta base); no es el contracargo de una tarjeta, que está en [fraude y contracargos](../../Comercio-electronico/Pagos/fraude-y-contracargos.md).

Para el sistema, una deducción nace en la [aplicación de cobros](aplicacion-de-cobros.md): el cobro no alcanza para cancelar la factura y la diferencia tiene un motivo. Que esa diferencia quede como una partida abierta con motivo, responsable y estado, y no como un saldo suelto en la cuenta del cliente, es lectura de esta base.

> [!NOTE] Sin fuente todavía: cómo se gestionan las deducciones en la práctica (códigos de motivo, plazos para resolverlas, cuándo se aceptan sin discutir por monto chico).

## DSO, DSO mejor posible y días de atraso

La Credit Research Foundation, una asociación de gestores de crédito, publica las fórmulas de referencia. El DSO es «the average time (aggregate), in days it takes a firm to convert its accounts receivables to cash»:

- DSO = cuentas a cobrar totales al cierre × días del período ÷ ventas a crédito del período.
- DSO mejor posible (best possible DSO) = cuentas a cobrar corrientes (no vencidas) × días del período ÷ ventas a crédito del período. Es «the best possible level of receivables under the most favorable condition – A/R with no delinquency», y depende de los plazos que se dan.
- Días de atraso promedio (average days delinquent) = DSO − DSO mejor posible.
- Porcentaje corriente = cuentas a cobrar corrientes ÷ cuentas a cobrar totales.
- Porcentaje a más de 91 días = lo que tiene más de 90 días de antigüedad ÷ cuentas a cobrar totales. La CRF aclara que hay «nothing special about the period of over 91 days»: se puede usar el tramo de antigüedad que convenga.

La CRF pide usarlas juntas. El DSO solo no separa lo que viene de los plazos de lo que viene de la mora; el DSO mejor posible aísla la parte de los plazos y los días de atraso, la de la cobranza.

## El índice de eficacia de cobranza

El CEI (collection effectiveness index) «expresses the effectiveness of collection efforts over time. The closer to 100 percent, the more effective the collection effort is». Su fórmula, según la CRF, con N igual al número de meses:

CEI = (cuentas a cobrar al inicio + ventas a crédito ÷ N − cuentas a cobrar totales al cierre) ÷ (cuentas a cobrar al inicio + ventas a crédito ÷ N − cuentas a cobrar corrientes al cierre) × 100

Como lectura de esta base, el numerador es lo que se cobró y el denominador, lo que se podía cobrar: todo menos lo que todavía no venció. La CRF dice que sirve «as a departmental or individual performance measure».

Un ejemplo de esta base, para un mes de 30 días: cuentas a cobrar al inicio de 100.000, ventas a crédito de 60.000, cuentas a cobrar al cierre de 90.000, de las cuales 50.000 no vencieron.

| Medida | Cálculo | Resultado |
|---|---|---|
| CEI | (100.000 + 60.000 − 90.000) ÷ (100.000 + 60.000 − 50.000) | 63,6 % |
| DSO | 90.000 × 30 ÷ 60.000 | 45 días |
| DSO mejor posible | 50.000 × 30 ÷ 60.000 | 25 días |
| Días de atraso promedio | 45 − 25 | 20 días |

De los 110.000 que se podían cobrar se cobraron 70.000. Veinte de los 45 días de DSO son mora; los otros 25 son el plazo que se dio.

> [!NOTE] Sin fuente todavía: un valor de referencia del CEI. El «90 % es bueno» que circula sale de una calculadora comercial, no de la CRF.

## Por qué el DSO engaña

La CRF llama al DSO «one of the most often misused and misunderstood performance measures». Su valor está en ayudar a ver si un cambio en las cuentas a cobrar viene de las ventas o de otro factor, «such as change in selling terms». Advierte que los días de atraso promedio «can be deceiving by masking the performance of delinquent accounts if other accounts are discounting their bills»: los clientes que pagan antes tapan a los atrasados. Y cierra: «Like the many measures, there are flaws and biases, however, used consistently and routinely, these DSO related measures can be indicators of performance and can be an early warning sign».

Según el resumen de una enciclopedia abierta que cita a Houston y Brigham, el DSO cambia con el volumen de ventas aunque la cobranza no cambie, varía con la estacionalidad, un período demasiado corto genera saltos que no significan nada, y lo que es un buen valor depende del rubro. Un DSO alto puede venir de un mal filtro de crédito o de una mala cobranza, y uno muy bajo, de una política tan dura que frena ventas.

> [!IMPORTANT] Las fuentes no leen igual el DSO. La CRF lo define como el tiempo promedio en convertir las cuentas a cobrar en plata, y OpenStax como «the expected days it will take to convert accounts receivable into cash», a comparar con el plazo otorgado. La fuente que cita a Houston y Brigham dice que leerlo como días promedio para cobrar una venta es un error: son los días de venta promedio que siguen pendientes. Las dos lecturas coinciden cuando las ventas son estables (lectura de esta base). Hay además una diferencia de nombres: esa misma fuente llama DDSO a lo que la CRF llama días de atraso promedio; esta base sigue a la CRF, que es la fuente primaria.

Dos críticas más se repiten en la práctica y no tienen autor en las fuentes leídas: en una empresa que crece, el DSO sube aunque nadie pague más tarde, porque las ventas del período son menores que las que generaron el saldo; y un promedio mezcla clientes con plazos distintos. Las dos son lectura de esta base. El método de cálculo por meses hacia atrás (countback), que corrige la primera, queda sin fuente todavía.

Para leer más: la guía *Performance Measures* de la Credit Research Foundation, de pocas páginas, con las fórmulas y sus limitaciones. Conviene fijarse en que el DSO, el DSO mejor posible y los días de atraso se leen juntos, y en la lista de preguntas que propone para compararse con la industria (plazos, facturas emitidas a tiempo y sin errores, calidad, clientes insatisfechos).
