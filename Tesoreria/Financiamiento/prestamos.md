---
resumen: >-
  Un préstamo a plazo entrega una suma de una vez y se devuelve en cuotas según un sistema de amortización (el francés, de cuota constante, o el alemán, de capital constante), a veces con garantías y con covenants que el deudor se compromete a cumplir; el leasing financia un bien que sigue siendo de la financiera.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, Fixed-rate mortgage, como fuente terciaria (leído; la fórmula es matemática estándar): https://en.wikipedia.org/wiki/Fixed-rate_mortgage"
  - "Wikipedia, Amortization calculator, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Amortization_calculator"
  - "Wikipedia, Amortization schedule, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Amortization_schedule"
  - "Wikipedia, Loan covenant, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Loan_covenant"
  - "Wikipedia, Debt covenant, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Debt_covenant"
  - "Wikipedia, Finance lease, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Finance_lease"
  - "Tesoreria/.investigacion/financiamiento-y-riesgos.md, sección 1.2 (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 2 (2026-11-27)"
aliases: [préstamo, préstamos, préstamo a plazo, term loan, sistema francés, sistema alemán, amortización, amortization schedule, cuadro de amortización, cuota constante, annuity loan, amortización constante, covenant, covenants, loan covenant, garantía, collateral, leasing, arrendamiento financiero, finance lease]
creado: 2026-11-27
revisado:
---

# Préstamos

Un préstamo a plazo entrega una suma de una vez y se devuelve en cuotas según un sistema de amortización (el francés, de cuota constante, o el alemán, de capital constante), a veces con garantías y con covenants que el deudor se compromete a cumplir; el leasing financia un bien que sigue siendo de la financiera.

Es el instrumento para lo que dura años: una máquina, una ampliación, una reestructuración de deudas cortas. Para la tesorería, cada préstamo es un cronograma de salidas de caja fijas que entra a la [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md), y un conjunto de condiciones que vigilar. Lo que dura semanas se cubre con el [financiamiento de corto plazo](financiamiento-de-corto-plazo.md), y cómo se elige entre ellos está en [financiamiento](financiamiento.md).

## Cada cuota es interés más amortización

Toda cuota tiene dos partes: el interés sobre el saldo que se debe y la amortización, la parte que devuelve capital. El interés de cada período es la tasa por el saldo anterior. Lo que cambia entre los sistemas es cuál de las dos partes se mantiene fija.

- Sistema francés. La cuota total es constante. Al principio casi toda es interés y al final casi toda es capital.
- Sistema alemán. La amortización es constante: cada cuota devuelve la misma parte del capital, y como el saldo baja, el interés baja y la cuota también.

La fórmula de la cuota francesa, según Wikipedia (fuente terciaria, y matemática estándar que se puede derivar), es c = P · r / (1 − (1 + r)^(−N)), con P el capital, r la tasa por período y N la cantidad de cuotas; si la tasa es cero, la cuota es P/N. El ejemplo de la fuente es una hipoteca de USD 200.000 al 6,5% anual a 30 años: r = 0,065/12, N = 360 y la cuota es USD 1.264,14, que esta base verificó.

Las fuentes leídas no usan los nombres «francés» ni «alemán». La de cuadros de amortización nombra el método lineal (*straight line*) entre los usuales, que esta base lee como el de capital constante. Las fórmulas del alemán son derivación de esta base: la amortización es P/N, el interés de la cuota k es r · P · (1 − (k − 1)/N) y el interés total es r · P · (N + 1)/2.

## El mismo préstamo en los dos sistemas

Cálculo de esta base, verificado: un préstamo de 100.000 a 12 cuotas mensuales, al 1% mensual.

| | Sistema francés | Sistema alemán |
|---|---|---|
| Cuota 1 | 8.884,88 (1.000,00 de interés y 7.884,88 de capital) | 9.333,33 (1.000,00 de interés y 8.333,33 de capital) |
| Cuota 2 | 8.884,88 (921,15 de interés) | 9.250,00 (916,67 de interés) |
| Cuota 12 | 8.884,88 (87,97 de interés) | 8.416,67 (83,33 de interés) |
| Interés total | 6.618,55 | 6.500,00 |

El alemán paga menos interés total porque devuelve el capital antes: durante el préstamo se debe, en promedio, menos plata. La tasa es la misma en los dos, 1% mensual o 12,68% efectivo anual, así que el alemán no es más barato en el sentido del [costo del financiamiento](costo-del-financiamiento.md): es más corto en promedio (lectura de esta base). A cambio, exige más caja al principio, justo cuando la inversión todavía no rinde. El francés da una cuota previsible, que se planifica mejor en la proyección de caja.

> [!NOTE] Sin fuente todavía: cuál de los dos sistemas usa cada tipo de préstamo en la práctica (bancos, leasing, créditos con aval) no se verificó.

## Garantías

> [!NOTE] Sin fuente todavía: los tipos de garantía de un préstamo. El informe de investigación los lista sin fuente: reales (hipoteca sobre un inmueble, prenda sobre un bien mueble), personales (fianza o aval de un socio, aval de una sociedad de garantía recíproca) y cesión de cobranzas o de contratos. Las sociedades de garantía recíproca argentinas y su aval en el descuento de cheques están en [tesorería en Argentina](../tesoreria-en-argentina.md).

## Covenants: lo que el deudor promete mientras debe

Un covenant es un compromiso que el deudor asume como parte del contrato de préstamo. Según dos artículos de Wikipedia leídos a través de un resumen (fuente terciaria), los hay de tres clases:

- De hacer: informar cada cierto tiempo su situación financiera al prestamista.
- De no hacer: no pagar dividendos, no recomprar acciones, no tomar más deuda.
- Financieros: mantener una relación entre deuda y patrimonio o una cobertura de intereses por encima de un valor. En préstamos inmobiliarios aparecen el LTV (préstamo sobre valor del bien), el DSCR (cobertura del servicio de la deuda) y el ISCR (cobertura de intereses).

Romper un covenant puede darle al prestamista el derecho de exigir el pago anticipado o de cobrar más interés, según la misma fuente. La clasificación en tres clases es del resumen, no literal de los artículos.

> [!NOTE] Sin fuente todavía: los ratios usuales en préstamos a empresas (deuda neta sobre EBITDA, cobertura de intereses, cobertura del servicio de la deuda) y sus umbrales típicos. Falta una fuente de libro o un contrato modelo.

Para un sistema, un covenant financiero es un cálculo con fecha: qué ratio, con qué datos contables, qué umbral, cada cuánto se mide y a quién se informa. La tesorería necesita verlo antes del cierre, con la proyección, para no enterarse por el banco (lectura de esta base).

## Leasing

En el leasing financiero, según Wikipedia (fuente terciaria, según su resumen), la financiera suele ser la dueña legal del bien durante el contrato, y quien lo toma tiene el control operativo y comparte sus riesgos y beneficios. Bajo las NIIF, un arrendamiento es financiero si transfiere «substantially all the risks and rewards» de la propiedad; la cita viene del resumen y no se cotejó con la norma. La NIIF 16 eliminó esa clasificación para el tomador: registra un activo por derecho de uso y un pasivo por el arrendamiento, salvo los de corto plazo y bajo valor. El arrendador sigue clasificando.

> [!NOTE] Sin fuente todavía: la definición del leasing operativo y el texto de la NIIF 16.

Para la tesorería, la cuota del leasing es una salida de caja fija y contratada, igual que la de un préstamo, y entra a la proyección del mismo modo. Cómo se registra es de [Contabilidad](../../Contabilidad/contabilidad.md).

## Lo que el sistema guarda de cada préstamo

Un sistema de gestión necesita, por préstamo, el capital, la moneda, la tasa y si es fija o variable, el sistema de amortización, el cuadro de cuotas con interés y capital separados, las garantías y los covenants (lectura de esta base). Con tasa variable, el cuadro se recalcula cada vez que la tasa cambia, y el riesgo que eso trae está en [riesgos financieros](../Riesgos-financieros/riesgos-financieros.md).

El registro contable es de [Contabilidad](../../Contabilidad/contabilidad.md): el préstamo recibido y las cuotas de capital van a actividades de financiación del [estado de flujo de efectivo](../../Contabilidad/Estados-contables/estado-de-flujo-de-efectivo.md). Un préstamo en otra moneda se vuelve a convertir en cada cierre y genera diferencia de cambio, como explica [moneda extranjera](../../Contabilidad/Operaciones/moneda-extranjera.md); el riesgo de esa moneda se trata en [riesgo de tipo de cambio](../Riesgos-financieros/riesgo-de-tipo-de-cambio.md).

## Cómo falla un préstamo

- Elegir el sistema por el interés total. El alemán paga menos interés pero pide más caja en los primeros meses; si la proyección no la tiene, el ahorro no sirve (lectura de esta base).
- Un covenant que se rompe sin aviso. Si nadie calcula el ratio antes del cierre, el incumplimiento aparece cuando el banco ya puede exigir el pago anticipado.
- Tasa variable sin escenario. Una suba de la tasa cambia todas las cuotas que faltan, y la proyección que usó la tasa de hoy queda corta.
- Deuda en otra moneda que la de los ingresos. Las cuotas crecen con el tipo de cambio mientras los ingresos no (lectura de esta base; ver [riesgo de tipo de cambio](../Riesgos-financieros/riesgo-de-tipo-de-cambio.md)).
