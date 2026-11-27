---
resumen: >-
  La posición de caja es cuánta plata puede usar la empresa hoy: el saldo de cada cuenta, corregido por lo que está en camino de acreditarse o de debitarse y por lo que ya está comprometido para pagar.
estado: vigente
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 9.7.2.1 Manage and reconcile cash positions, p. 24 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "AFP, especificaciones del examen CTP, subtemas de posición y revisión de saldos (leído): http://ctpcert.financialprofessionals.org/overview/ctp-test-specifications"
  - "OpenStax, Principles of Finance (2022), 19.3 Cash Management (leído): https://openstax.org/books/principles-finance/pages/19-3-cash-management"
  - "Wikipedia, Float (money supply), que cita a Federal Reserve Bank of New York, Fedpoints: Float (2007) (según su resumen; es la única fuente de la definición de flotación, porque la página original del Banco de la Reserva Federal de Nueva York ya no está disponible): https://en.wikipedia.org/wiki/Float_(money_supply)"
  - "Reserva Federal de Estados Unidos, Regulation CC (12 CFR parte 229), página de presentación y sección 229.10 (leído, solo lo citado): https://www.federalreserve.gov/paymentsystems/regcc-about.htm"
  - "Wikipedia, Cash management (según su resumen; artículo con aviso de mantenimiento): https://en.wikipedia.org/wiki/Cash_management"
  - "Tesoreria/.investigacion/caja-y-liquidez.md, secciones 1 y 2 (2026-11-27)"
  - "Tesoreria/.investigacion/caja-y-cobranzas-segunda-ronda.md, sección 2 (2026-11-27)"
  - "Tesoreria/.investigacion/caja-y-liquidez-verificacion.md (2026-11-27)"
aliases: [posición de caja, posición diaria, posición de tesorería, cash position, daily cash position, saldo disponible, available balance, saldo contable, ledger balance, flotación, float]
creado: 2026-11-27
revisado: 2026-11-27
---

# Posición de caja

La posición de caja es cuánta plata puede usar la empresa hoy: el saldo de cada cuenta, corregido por lo que está en camino de acreditarse o de debitarse y por lo que ya está comprometido para pagar.

Es la primera de las dos preguntas de [Caja y liquidez](caja-y-liquidez.md); la segunda, cuánta va a haber, es de la [proyección de caja](proyeccion-de-caja.md). APQC la pone primera dentro de la gestión de caja, en 9.7.2.1, «Manage and reconcile cash positions». El examen de tesoreros de la AFP le da dos subtemas: «Manage optimal cash positioning through short-term investing and borrowing activities» y «Review cash balances and reconcile transaction activity to ensure accuracy». El primero dice para qué sirve la posición, por lectura de esta base: decidir cada día si se coloca lo que sobra o se cubre lo que falta.

## Los saldos que forman la posición

Una misma cuenta tiene varios saldos a la vez, y cada uno dice otra cosa. Ninguna fuente abierta leída los define; la tabla es lectura de esta base, armada sobre la flotación que se explica abajo.

| Saldo | Qué es | De dónde sale |
|---|---|---|
| Contable | Lo que la empresa registró en su cuenta Banco | Los libros de la empresa |
| Según el banco | Lo que el banco tiene registrado al cierre del último extracto o consulta | El extracto o el informe diario del banco |
| Disponible | Lo que se puede usar hoy sin que el banco rechace la operación | El banco, que descuenta los depósitos que todavía no acreditó |
| En tránsito | Cobros depositados o enviados que todavía no se acreditaron, y pagos emitidos que todavía no se debitaron | La diferencia entre los libros y el banco, documento por documento |
| Comprometido | Pagos aprobados o programados para hoy que todavía no salieron | La [corrida de pagos](../Pagos-a-proveedores/corrida-de-pagos.md) y los vencimientos del día |

La posición del día, en esta lectura, es el saldo disponible más lo que se acredita en el día menos lo comprometido para el día. Se calcula por cuenta y por moneda, y después se suma.

> [!NOTE] Sin fuente todavía: una definición con autoridad de saldo contable, saldo disponible, fondos en tránsito y valores al cobro. El candidato es *Essentials of Treasury Management* de la AFP, que no se leyó.

## La flotación: la misma plata contada dos veces

La diferencia entre el saldo contable y el disponible tiene nombre: flotación (float). Según el resumen de un artículo que cita al Banco de la Reserva Federal de Nueva York, la flotación es plata que el sistema bancario cuenta dos veces durante un rato, por la demora en procesar los cheques. Hasta que el cheque se compensa, el banco lo acredita en forma provisoria. Es una sola fuente, terciaria, y la página oficial que cita no se pudo leer.

En Estados Unidos la ley acota esa demora. La Ley de Disponibilidad Expedita de Fondos fija plazos máximos de retención de los depósitos, y la Regulation CC la desarrolla: por ejemplo, el banco debe poner a disposición no más tarde del día hábil siguiente al depósito los fondos de ciertos cheques (del Tesoro, giros postales, cheques de caja y certificados, entre otros). El plazo para el resto de los cheques no se leyó. Para la Argentina, los plazos de cada medio están en [tesorería en Argentina](../tesoreria-en-argentina.md).

El mismo artículo separa dos plazos. La flotación del banco va desde el depósito hasta que el banco del depositante recibe los fondos; la del cliente, desde el depósito hasta que el depositante los puede usar. Cuenta además una práctica de los años setenta y ochenta en Estados Unidos: girar cheques contra bancos lejanos para demorar la compensación y usar la plata unos días más.

Para la posición, la flotación corre en los dos sentidos (lectura de esta base). Un cheque recibido y depositado ya bajó la cuenta a cobrar del cliente y todavía no se puede usar. Un cheque emitido ya bajó el saldo contable y todavía está en la cuenta. Según el resumen de otro artículo, los bancos informan, además del saldo, los cheques en proceso de cobro.

Los medios electrónicos achican la flotación pero no la eliminan: el comercio que cobra con tarjeta ve el pago acreditado antes de poder usarlo, como explica [costo de cobrar](../../Comercio-electronico/Pagos/costo-de-cobrar.md). Cuándo se acredita cada medio está en [medios de cobro y pago](medios-de-cobro-y-pago.md).

## El saldo que está pero no se puede usar

Parte de la plata de una cuenta puede estar atada a un acuerdo con el banco. OpenStax define el saldo compensatorio como «typically a minimum amount to be maintained in the company's checking account», y da el caso de un grupo de restaurantes con un préstamo de 500.000 dólares que debía mantener 50.000 en su cuenta corriente. Esa plata aparece en el saldo y no sirve para pagar: la posición la resta.

Lo mismo vale, por lectura de esta base, para un depósito en garantía o un fondo retenido por una plataforma de cobro. El sistema tiene que saber que existe para no mostrarlo como disponible.

## Lo que es de la contabilidad y lo que es de la posición

La posición y la conciliación bancaria usan los mismos datos y contestan preguntas distintas. La [conciliación](../../Contabilidad/Control-interno/conciliaciones.md), que en esta base es de la contabilidad, explica después por qué el saldo del banco y el de los libros no coinciden y corrige los libros. La posición se arma antes, cada mañana, con los saldos que haya, y decide qué se hace hoy.

APQC las junta en un solo proceso. Por lectura de esta base, la razón es que se necesitan: una posición armada sobre libros sin conciliar arrastra los errores del mes. Las partidas en tránsito que la conciliación lista son las mismas que la posición tiene que tener en cuenta.

## La decisión de cada día

Con la posición armada, la tesorería decide tres cosas. Las dos primeras salen del subtema del examen de la AFP citado arriba y la tercera es lectura de esta base: si sobra plata para [colocar](colocacion-de-excedentes.md), si falta y hay que usar una línea de [financiamiento de corto plazo](../Financiamiento/financiamiento-de-corto-plazo.md), y si hay que mover fondos entre [cuentas bancarias](cuentas-bancarias.md) para que cada pago salga de una cuenta con saldo. En una pyme, por lectura de esta base, es una consulta a la banca electrónica por la mañana y una planilla; en una empresa grande, un informe que el banco manda cada día.

## Cómo se diseña en un sistema

Lo que sigue es lectura de esta base para quien construye la pantalla de posición:

- Cada saldo lleva su origen y su hora: el saldo del banco de ayer a la noche no es el de hoy al mediodía.
- El saldo según el banco sale del extracto importado o de la conexión con el banco; el contable, del registro; nunca se pisan.
- Lo en tránsito se arma con documentos concretos (el cheque n.º tal, la transferencia de tal cliente), con la fecha en que se espera la acreditación.
- Lo comprometido sale de los pagos aprobados que todavía no se enviaron, para que el mismo peso no se prometa dos veces.
- El límite de descubierto o de la línea de crédito que no se usó va en una línea aparte, sin sumarse al saldo: es plata a la que se puede llegar, con el costo que dice [financiamiento de corto plazo](../Financiamiento/financiamiento-de-corto-plazo.md).
- Las monedas no se suman sin un tipo de cambio explícito y fechado; el registro de la diferencia de cambio está en [moneda extranjera](../../Contabilidad/Operaciones/moneda-extranjera.md).
- La posición de cada día se guarda, porque contra ella se mide si la [proyección de caja](proyeccion-de-caja.md) acertó.

## Cómo falla

Las fallas habituales, por lectura de esta base: contar como disponible un cheque depositado que después se rechaza; olvidar un pago aprobado y prometer la misma plata a otro; mostrar el saldo compensatorio o retenido como libre; armar la posición sobre libros con semanas sin conciliar; y mirar una sola cuenta cuando la empresa tiene varias en distintos bancos. En la Argentina, el cheque de pago diferido agrega una cartera de cheques recibidos con fecha de cobro futura; cómo se trata está en [tesorería en Argentina](../tesoreria-en-argentina.md).
