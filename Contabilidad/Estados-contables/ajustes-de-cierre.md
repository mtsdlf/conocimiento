---
resumen: >-
  Los ajustes de cierre son los asientos que se registran al final de un período para que los saldos reflejen lo devengado aunque no haya un documento que lo dispare, y los asientos de cierre son los que después vuelcan las cuentas de resultado al patrimonio y las dejan en cero.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 4.2 Discuss the Adjustment Process and Illustrate Common Types of Adjusting Entries (según extractos del buscador): https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries"
  - "OpenStax, Principles of Financial Accounting (2019), 4.3 Record and Post the Common Types of Adjusting Entries: https://openstax.org/books/principles-financial-accounting/pages/4-3-record-and-post-the-common-types-of-adjusting-entries"
  - "OpenStax, Principles of Financial Accounting (2019), 5.1 Describe and Prepare Closing Entries for a Business (según extractos del buscador): https://openstax.org/books/principles-financial-accounting/pages/5-1-describe-and-prepare-closing-entries-for-a-business"
  - "OpenStax, Principles of Financial Accounting (2019), 5.4 Appendix: Complete a Comprehensive Accounting Cycle for a Business: https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business"
  - "OpenStax, Principles of Financial Accounting (2019), 9.2 Account for Uncollectible Accounts: https://openstax.org/books/principles-financial-accounting/pages/9-2-account-for-uncollectible-accounts-using-the-balance-sheet-and-income-statement-approaches"
  - "Contabilidad/.investigacion/estados-contables.md (2026-11-27)"
  - "Contabilidad/.investigacion/operaciones.md (2026-11-27), previsión para incobrables"
aliases: [ajustes de cierre, asientos de ajuste, adjusting entries, asientos de cierre, closing entries, refundición de cuentas de resultado, resumen de resultados, income summary, balance de sumas y saldos ajustado, balance de comprobación ajustado, adjusted trial balance, devengamientos, accruals, diferimientos, deferrals, previsión, allowance, provisión, provision]
creado: 2026-11-27
revisado: 2026-11-27
---

# Ajustes de cierre

Los ajustes de cierre son los asientos que se registran al final de un período para que los saldos reflejen lo devengado aunque no haya un documento que lo dispare, y los asientos de cierre son los que después vuelcan las cuentas de resultado al patrimonio y las dejan en cero.

Son el puente entre el [registro](../Registro/registro-contable.md) del día a día y los [estados contables](estados-contables.md). Durante el mes, cada asiento nace de un documento: una factura, un recibo, un extracto. Pero el [devengado](../Registro/devengado.md) pide registrar cosas que no tienen documento: el interés que se ganó y no se cobró, el sueldo de la última semana que se paga el mes siguiente, el desgaste de una máquina. Según OpenStax, un ajuste no significa que hubo un error: existe porque no todo hecho genera un comprobante. El recorrido completo del cierre entre áreas (quién concilia, quién aprueba, en qué orden) es del tema Procesos de negocio, en [del registro al balance](../../Procesos-de-negocio/del-registro-al-balance.md); acá queda cómo se registra cada ajuste.

## La regla que valida un ajuste

Según OpenStax, todo asiento de ajuste toca al menos una cuenta de resultado y una del balance, y nunca toca la caja. La razón, según una explicación propia que el libro no da, es que la caja, cuando se mueve, deja un documento y se registró en su momento. Lo que falta al cierre es repartir entre períodos lo que ya se registró, o registrar lo que pasó sin documento.

Para quien construye un sistema, esa regla es validable: un asiento marcado como ajuste que toca la caja, o que no toca ninguna cuenta de resultado, está mal clasificado. Es una inferencia a partir de la regla del libro; cómo se modela el asiento está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).

## Los cinco ajustes de Printing Plus, enero de 2019

OpenStax sigue a Printing Plus, una empresa de ejemplo, y al 31 de enero registra estos ajustes (cifras en dólares):

| Ajuste | Cuenta | Debe | Haber |
|---|---|---|---|
| 1. Ingreso devengado: intereses ganados y no cobrados | Intereses a cobrar | 140 | |
| | Ingresos por intereses | | 140 |
| 2. Gasto pagado por adelantado: de $500 de insumos se usaron $100 | Gasto de insumos | 100 | |
| | Insumos | | 100 |
| 3. Amortización del equipo | Amortización del período | 75 | |
| | Amortización acumulada de equipos | | 75 |
| 4. Ingreso diferido: de $4.000 cobrados por adelantado el 9 de enero, se prestaron servicios por $600 | Ingresos cobrados por adelantado | 600 | |
| | Ingresos por servicios | | 600 |
| 5. Gasto devengado: sueldos del 21 al 31 de enero sin pagar | Sueldos | 1.500 | |
| | Sueldos a pagar | | 1.500 |

Después de los ajustes quedan $400 de insumos y $3.400 de ingresos cobrados por adelantado. Ningún asiento toca la caja.

Los cinco caen en tres familias, y al cierre se suma una cuarta:

- Los devengamientos (1 y 5): algo ya pasó y todavía no se cobró o pagó. Se registra el ingreso o el gasto contra una cuenta a cobrar o a pagar.
- Los diferimientos (2 y 4): la plata se movió antes y el hecho se va cumpliendo con el tiempo. Se pasa a resultado la parte que corresponde al período.
- La amortización del período (3): el costo de un bien de uso se reparte a lo largo de su vida útil. El cálculo y los métodos están en [activos fijos y amortización](../Operaciones/activos-fijos-y-amortizacion.md).
- Las estimaciones, como la previsión para incobrables, que se explica abajo.

## Previsiones y provisiones

Al cierre también se registran estimaciones. El caso de libro es la previsión para incobrables: se estima qué parte de lo que deben los clientes no se va a cobrar y se registra el gasto en el período de la venta, aunque todavía no se sepa qué cliente no va a pagar. OpenStax da un ejemplo con ventas a crédito de $458.230 y una estimación del 5%:

| Cuenta | Debe | Haber |
|---|---|---|
| Gasto por incobrables | 22.911,50 | |
| Previsión para incobrables | | 22.911,50 |

La previsión es una contracuenta: resta de las cuentas a cobrar en el balance sin tocar la cuenta de ningún cliente. Cuando un cliente concreto resulta incobrable, se da de baja contra la previsión y el resultado no se toca de nuevo. El ciclo completo, y cómo la NIIF 9 cambia la base de la estimación, está en [ingresos y cuentas a cobrar](../Operaciones/ingresos-y-cuentas-a-cobrar.md).

> [!NOTE]
> Sin fuente todavía: la distinción de vocabulario entre previsión (una corrección del valor de un activo, como la de incobrables) y provisión (un pasivo de monto o fecha inciertos, como un juicio) que usan los contadores de habla hispana. Falta leer la NIC 37 y la norma local que la fije.

## El balance de sumas y saldos ajustado

Después de registrar los ajustes se arma el balance de sumas y saldos ajustado (adjusted trial balance; también se lo llama balance de comprobación ajustado). Es el mismo [balance de sumas y saldos](../Registro/asiento-y-libros.md#el-balance-de-sumas-y-saldos) del registro, armado otra vez con los saldos que dejaron los ajustes: la lista de las cuentas con saldo distinto de cero, con sus débitos y créditos. Según OpenStax, sirve para encontrar errores de cálculo de los pasos anteriores antes de armar los estados. En el ejemplo de Clip'em Cliff de agosto de 2019, el balance sin ajustar sumaba $87.900 y el ajustado, $94.150. Los estados se arman con los saldos ajustados.

## El cierre de las cuentas de resultado

Las cuentas de ingresos, gastos y dividendos son temporales: miden un período y empiezan el siguiente en cero. OpenStax las cierra con cuatro asientos, a través de una cuenta puente, el resumen de resultados:

1. Los ingresos se cancelan contra el resumen de resultados.
2. Los gastos se cancelan contra el resumen de resultados.
3. El saldo del resumen, que es el resultado del período, pasa a resultados acumulados.
4. Los dividendos se cancelan contra resultados acumulados.

Con los totales del ciclo de Clip'em Cliff de agosto de 2019 (ingresos por servicios $10.300, por intereses $350, gastos $10.625, dividendos $150), los asientos quedan así. La fuente da los totales; el armado de los asientos con ellos es propio, y los gastos van en una línea aunque en el registro son varias cuentas.

| Asiento | Cuenta | Debe | Haber |
|---|---|---|---|
| 1 | Ingresos por servicios | 10.300 | |
| | Ingresos por intereses | 350 | |
| | Resumen de resultados | | 10.650 |
| 2 | Resumen de resultados | 10.625 | |
| | Gastos (todas las cuentas) | | 10.625 |
| 3 | Resumen de resultados | 25 | |
| | Resultados acumulados | | 25 |
| 4 | Resultados acumulados | 150 | |
| | Dividendos | | 150 |

El resumen de resultados queda en cero, y su saldo antes del asiento 3 ($25 acreedor) es el resultado neto del [estado de resultados](estado-de-resultados.md). En el ejemplo de Printing Plus pasa lo mismo: el resumen de enero queda en $4.665 acreedor, que según OpenStax es la misma cifra que informa su estado de resultados. Resultados acumulados termina en −$125, el saldo que muestra el patrimonio del [balance](balance.md).

Después del cierre, el balance de sumas y saldos solo tiene cuentas permanentes: activo, pasivo y patrimonio. Que una cuenta de resultado tenga saldo después del cierre es un error.

## Cómo fallan los ajustes

El ajuste que falta no da error: el balance de sumas y saldos cuadra igual, porque un asiento que no se hizo no deja débitos sin créditos. Si Printing Plus no registra los $1.500 de sueldos, el gasto de enero queda corto y el de febrero, inflado. Esto es una inferencia a partir del mecanismo, y de ella sale que el cierre necesita una lista de los ajustes que se repiten cada período y la [conciliación](../Control-interno/conciliaciones.md) de cada cuenta con su respaldo, que muestra lo que se olvidó.
