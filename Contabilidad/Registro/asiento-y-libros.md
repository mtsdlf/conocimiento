---
resumen: >-
  El asiento es la anotación de un hecho con sus cuentas, sus importes al debe y al haber, su fecha y su explicación; se anota primero en el diario, se pasa al mayor de cada cuenta y se controla con el balance de sumas y saldos, y si está mal se corrige con otro asiento, nunca borrándolo.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 3.5 Use Journal Entries to Record Transactions and Post to T-Accounts: https://openstax.org/books/principles-financial-accounting/pages/3-5-use-journal-entries-to-record-transactions-and-post-to-t-accounts"
  - "OpenStax, Principles of Financial Accounting (2019), 3.6 Prepare a Trial Balance: https://openstax.org/books/principles-financial-accounting/pages/3-6-prepare-a-trial-balance"
  - "OpenStax, Principles of Financial Accounting (2019), 5.4 Appendix: Complete a Comprehensive Accounting Cycle for a Business (según el buscador): https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business"
  - "Contabilidad/.investigacion/registro-y-fundamentos.md (2026-11-27)"
aliases: [asiento, asiento contable, journal entry, libro diario, diario, journal, libro mayor, mayor, general ledger, pase al mayor, posting, cuenta T, T-account, balance de sumas y saldos, balance de comprobación, trial balance, contraasiento, asiento de corrección, correcting entry, asiento de reversión, reversing entry]
creado: 2026-11-27
revisado: 2026-11-27
---

# Asiento y libros

El asiento es la anotación de un hecho con sus cuentas, sus importes al debe y al haber, su fecha y su explicación; se anota primero en el diario, se pasa al mayor de cada cuenta y se controla con el balance de sumas y saldos, y si está mal se corrige con otro asiento, nunca borrándolo.

Por qué cada asiento toca dos cuentas y qué lado aumenta cada una está en [partida doble](partida-doble.md). Esta nota trata la forma: qué tiene un asiento, en qué libros queda y cómo se controla.

## Qué tiene un asiento

Según OpenStax, un asiento lleva la fecha, las cuentas debitadas primero, las acreditadas debajo y corridas a la derecha, los importes y una explicación breve. El total del debe tiene que ser igual al total del haber. Un asiento con una sola cuenta de cada lado es simple; uno con más de una cuenta en alguna columna es compuesto.

Cada asiento nace de un comprobante: una factura, un recibo, un extracto. Qué documento dispara cada asiento habitual está en [operaciones](../Operaciones/operaciones.md).

## Del diario al mayor

El diario es, según OpenStax, el primer lugar donde la información entra al sistema contable; por eso se lo llama libro de registro original. Ahí los asientos quedan en orden cronológico, uno detrás de otro.

El mayor (libro mayor o general ledger) tiene una hoja por cuenta con todos sus movimientos y su saldo. Pasar los importes del diario a cada cuenta del mayor se llama pase o posting. Las dos vistas tienen los mismos datos ordenados de otra manera: el diario responde «qué pasó el 5 de enero» y el mayor, «cuánto hay en caja y por qué».

El saldo de una cuenta se calcula sumando los movimientos de un lado, restando los del otro, y queda del lado que pesa más. En el ejemplo de OpenStax, la caja de Printing Plus con 20.000 al debe y 300 al haber tiene un saldo deudor de 19.700.

Un sistema guarda los asientos una sola vez y calcula el mayor sumando: es el patrón de [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) (inferencia de la base sobre cómo se traduce el diario a una base de datos).

## El balance de sumas y saldos

El balance de sumas y saldos (trial balance) lista todas las cuentas del mayor que tienen saldo distinto de cero, con los deudores en una columna y los acreedores en otra. Si la partida doble se respetó, las dos columnas suman lo mismo. OpenStax lo ubica como el cuarto paso del ciclo contable; en ese momento todavía es un balance sin ajustar, antes de los [ajustes de cierre](../Estados-contables/ajustes-de-cierre.md).

El de Printing Plus al 31 de enero de 2019, con las cuentas traducidas (cifras en dólares):

| Cuenta | Debe | Haber |
|---|---|---|
| Caja | 24.800 | |
| Cuentas a cobrar | 1.200 | |
| Materiales | 500 | |
| Equipos | 3.500 | |
| Cuentas a pagar | | 500 |
| Ingresos cobrados por adelantado | | 4.000 |
| Capital | | 20.000 |
| Dividendos | 100 | |
| Ingresos por servicios | | 9.500 |
| Sueldos | 3.600 | |
| Gasto de luz | 300 | |
| **Total** | **34.000** | **34.000** |

## Qué errores encuentra y cuáles no

Cuando las columnas no suman lo mismo, hay al menos un error. OpenStax da dos pistas para encontrarlo con aritmética:

- Un saldo del lado equivocado. Con 33.900 al debe y 34.100 al haber, la diferencia es 200 y la mitad, 100: el saldo de Dividendos se había puesto en el haber.
- Dos cifras invertidas. Con 35.800 al debe y 34.000 al haber, la diferencia es 1.800, y 1.800 dividido 9 da 200, la distancia típica de una transposición: Equipos figuraba 5.300 en lugar de 3.500.

El libro avisa también lo contrario: puede haber errores y que el balance cuadre. Un asiento con la cuenta equivocada, uno omitido o uno cargado dos veces no descuadra nada (ejemplos de la base, no del libro). Esos errores los encuentran las [conciliaciones](../Control-interno/conciliaciones.md), que comparan el registro con algo de afuera (el banco, el auxiliar, el conteo) (inferencia de la base).

## Corregir con un asiento nuevo

Un asiento registrado no se borra ni se edita. Si estaba mal, se registra otro que lo compensa o lo completa, con la fecha en que se descubrió el error. Así el diario conserva qué se registró, cuándo y cómo se arregló, y un auditor puede seguir el rastro. Algunas leyes la hacen obligatoria; el caso argentino está en [libros contables en Argentina](libros-contables-en-argentina.md).

> [!NOTE]
> Sin fuente todavía: un pasaje de libro de texto o de norma internacional que formule la regla general de corregir con un asiento nuevo. OpenStax distingue el asiento de corrección del de ajuste, según el buscador, pero no se encontró cómo trata la corrección; la regla se sostiene acá en la práctica y en la ley de algunos países.

Un ejemplo armado sobre las cifras de Printing Plus (no está en la fuente): un cobro de 5.500 de un cliente se registra con crédito a Ingresos por servicios en lugar de a Cuentas a cobrar. El balance cuadra, pero el ingreso quedó duplicado y el cliente sigue debiendo. La corrección, fechada el día que se advierte:

| Cuenta | Debe | Haber |
|---|---|---|
| Ingresos por servicios | 5.500 | |
| Cuentas a cobrar | | 5.500 |

Para quien construye un sistema, la regla se traduce en tres cosas: un asiento confirmado no admite edición ni borrado, la corrección es un asiento nuevo que puede referir al original, y el período cerrado no admite asientos con fecha anterior al cierre (inferencia de la base; los permisos sobre esas acciones están en [controles sobre los sistemas](../Control-interno/controles-sobre-sistemas.md)).

## Los dos sentidos de contraasiento

«Contraasiento» y «reversión» se usan para dos cosas distintas, y conviene no mezclarlas:

1. Corregir un error: un asiento que anula otro mal hecho, total o parcialmente, invirtiendo sus débitos y créditos. Es lo de la sección anterior.
2. Revertir un ajuste: los reversing entries de OpenStax, que el libro presenta como un paso optativo al comenzar el período siguiente, después del balance posterior al cierre (según el buscador). Invierten un ajuste de devengamiento del cierre, por ejemplo unos sueldos devengados y no pagados, para que el pago del mes siguiente se registre sin tener que recordar el ajuste. No corrigen nada: el ajuste estaba bien.

Un sistema que ofrece «revertir» tiene que dejar claro cuál de los dos hace y con qué fecha (inferencia de la base).

Para leer más: OpenStax, secciones 3.5 y 3.6 juntas. En la 3.6 conviene fijarse en la parte de errores, con las reglas de dividir por 2 y por 9, y en que el libro admite que un balance que cuadra no prueba que esté bien.
