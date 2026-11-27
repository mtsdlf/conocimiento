---
resumen: >-
  Una conciliación compara dos registros independientes del mismo saldo (los libros y el extracto del banco, el auxiliar de clientes y su cuenta de control) y explica cada diferencia, para corregir lo que está mal y detectar lo que no debería haber pasado.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 8.6 Define the Purpose of a Bank Reconciliation: https://openstax.org/books/principles-financial-accounting/pages/8-6-define-the-purpose-of-a-bank-reconciliation-and-prepare-a-bank-reconciliation-and-its-associated-journal-entries"
  - "OpenStax, Principles of Financial Accounting (2019), 7.4 Prepare a Subsidiary Ledger: https://openstax.org/books/principles-financial-accounting/pages/7-4-prepare-a-subsidiary-ledger"
  - "ACFE, Occupational Fraud 2024: A Report to the Nations, fig. 13, p. 24: https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf"
  - "UNC School of Government, The Bank Reconciliation: A Key Internal Control (Badgett, 2024), según su resumen: https://canons.sog.unc.edu/2024/04/the-bank-reconciliation-a-key-internal-control-in-financial-management"
  - "Washington State Auditor, BARS, Bank reconciliations, según su resumen: https://sao.wa.gov/bars-annual-filing/bars-gaap-manual/accounting/accounting-principles-and-internal-control/bank-reconciliations"
  - "Contabilidad/.investigacion/control-interno.md (2026-11-27)"
  - "Contabilidad/.investigacion/posicion-contraria.md, sección 5, mito 6 (2026-11-27)"
aliases: [conciliación bancaria, bank reconciliation, conciliación de cuentas, account reconciliation, conciliación del auxiliar, conciliación intercompañía, intercompany reconciliation]
creado: 2026-11-27
revisado:
---

# Conciliaciones

Una conciliación compara dos registros independientes del mismo saldo (los libros y el extracto del banco, el auxiliar de clientes y su cuenta de control) y explica cada diferencia, para corregir lo que está mal y detectar lo que no debería haber pasado.

Es una actividad de control detectiva del componente 3 de COSO, que la nombra entre las típicas ("reconciliations"); el marco está en [control interno](control-interno.md). Funciona porque los dos registros los lleva gente distinta: el banco no sabe lo que anotó la empresa, y el auxiliar se arma documento por documento mientras la cuenta de control recibe totales. Por eso una conciliación hecha por quien custodia la plata pierde casi todo su valor ([separación de funciones](separacion-de-funciones.md)).

## Para qué sirve la conciliación bancaria

La conciliación bancaria explica, en un informe interno, por qué el saldo del extracto del banco y el saldo de la cuenta Banco en los libros de la empresa no coinciden. Se suele creer que sirve para encontrar errores del banco. Los manuales de los organismos de control del sector público de Estados Unidos la presentan de otra forma, según el resumen de esas fuentes: es un control para proteger el efectivo contra fraudes y pérdidas y para asegurar que los registros contables sean exactos. La mayoría de las diferencias son de tiempo (un depósito que el banco todavía no acreditó, un cheque que el proveedor todavía no cobró) o movimientos del banco que la empresa no registró (intereses, comisiones, cheques rechazados). Que el propósito principal sea encontrar los errores y fraudes propios es una inferencia: ninguna fuente nombra el malentendido con esas palabras.

Como detector de fraude, su peso es chico. En los 1,921 casos del informe de la ACFE de 2024, la conciliación de cuentas fue la vía por la que se descubrió el 5% de los fraudes, contra el 43% de las denuncias y el 14% de la auditoría interna (más en [auditoría y fraude](auditoria-y-fraude.md)).

## La conciliación bancaria paso a paso

OpenStax, en su capítulo 8.6, la arma en dos columnas que terminan en el mismo número:

1. Partí del saldo según el extracto del banco.
2. Sumale los depósitos en tránsito y los errores del banco que redujeron el saldo; restale los cheques emitidos que el banco todavía no pagó.
3. Eso da el saldo bancario ajustado.
4. Partí del saldo según los libros de la empresa.
5. Sumale lo que el banco cobró por cuenta de la empresa y los intereses ganados; restale los cheques rechazados, los cargos del banco y los errores de registro de la empresa.
6. Eso da el saldo contable ajustado, que tiene que ser igual al bancario.
7. Registrá un asiento solo por las partidas del lado de los libros. Los errores del banco se reclaman al banco, y las partidas en tránsito se acomodan solas el mes siguiente.

## El ejemplo de Feeter Plumbing

OpenStax concilia la cuenta de Feeter Plumbing Company al 31 de julio. Las cifras están en dólares.

| Lado del banco | USD | Lado de los libros | USD |
|---|---|---|---|
| Saldo del extracto | 77,040 | Saldo en libros | 32,760 |
| + Depósito en tránsito (la noche del 31) | 34,300 | + Pagaré cobrado por el banco | 60,000 |
| + Error del banco (cheque de 320 debitado por error) | 320 | + Intereses ganados | 1,800 |
| Subtotal | 111,660 | Subtotal | 94,560 |
| − Cheques pendientes (n.º 5523 por 9,620 y n.º 6547 por 10,000) | (19,620) | − Cheque rechazado de un cliente (Berson) | (2,200) |
| | | − Error de registro del cheque n.º 5386 (anotado 1,760 en lugar de 2,000) | (240) |
| | | − Cargos del banco | (80) |
| Saldo ajustado | 92,040 | Saldo ajustado | 92,040 |

Del lado del banco no sale ningún asiento: el depósito y los cheques en tránsito ya están en los libros, y los 320 se le reclaman al banco. Del lado de los libros salen cuatro:

| Cuenta | Debe | Haber |
|---|---|---|
| Banco | 61,800 | |
| Pagarés a cobrar | | 60,000 |
| Ingresos por intereses | | 1,800 |

| Cuenta | Debe | Haber |
|---|---|---|
| Cuentas a cobrar (Berson) | 2,200 | |
| Banco | | 2,200 |

| Cuenta | Debe | Haber |
|---|---|---|
| Gasto por cuotas | 240 | |
| Banco | | 240 |

| Cuenta | Debe | Haber |
|---|---|---|
| Gastos bancarios | 80 | |
| Banco | | 80 |

El cheque rechazado vuelve a la cuenta del cliente porque la deuda de Berson renace: el cobro que se había registrado no existió. El error de 240 se corrige con un asiento nuevo por la diferencia y no editando el original, que es la regla de [asiento y libros](../Registro/asiento-y-libros.md). Después de los cuatro asientos, la cuenta Banco en los libros queda en 92,040.

## El auxiliar contra su cuenta de control

La segunda conciliación habitual compara un auxiliar con su cuenta de control en el mayor. Cómo funcionan los auxiliares de clientes y proveedores está en [cuentas corrientes](../Registro/cuentas-corrientes.md); acá importa que el total de las cuentas individuales tiene que igualar el saldo de la cuenta de control, y si no iguala hay un error que encontrar.

OpenStax lo muestra al 31 de enero en su capítulo 7.4:

| Auxiliar de clientes | Saldo |
|---|---|
| PB&J | 0 |
| Jones Co. | 328 |
| Black & White | 0 |
| Tiny Tim's | 2,661 |
| Total del auxiliar | 2,989 |
| Cuenta de control Cuentas a cobrar | 2,989 |

Del lado de los proveedores, los tres saldos individuales (5,646, 0 y 425) suman 6,071, igual que la cuenta de control Cuentas a pagar.

Cuando un sistema registra la factura en el auxiliar y en el mayor con el mismo asiento, las dos cifras no pueden diferir por un error de suma. La conciliación sigue sirviendo para encontrar asientos manuales hechos directo contra la cuenta de control, sin pasar por el auxiliar. Esto último es inferencia, no viene de la fuente; quien construye el sistema puede impedirlo marcando la cuenta de control como no imputable a mano.

## Entre empresas del mismo grupo

Cuando un grupo tiene varias empresas que se venden o se prestan entre sí, cada una registra su lado: la que vende, una cuenta a cobrar; la que compra, una cuenta a pagar por el mismo monto. Antes de consolidar los estados contables del grupo se concilian los dos lados, y después los saldos entre empresas se eliminan. Según guías que no tienen autoridad normativa, la base es la NIIF 10, párrafo B86, que pide eliminar esos saldos por completo. La consolidación está en [normas contables](../Estados-contables/normas-contables.md).

> [!NOTE] Sin fuente todavía: el texto de la NIIF 10, B86, leído en la norma, y una guía neutral (de una firma grande o un texto académico) sobre cómo se concilia entre empresas del grupo.

## Quién la usa después

La tesorería, que maneja la posición de caja, se apoya en la conciliación bancaria para saber cuánta plata hay de verdad; el tema Tesorería y finanzas de la empresa en marcha, todavía no escrito, la va a enlazar. En el cierre de mes, las conciliaciones van junto con los [ajustes de cierre](../Estados-contables/ajustes-de-cierre.md): los asientos que salen de ellas tienen que estar antes de emitir los estados.
