---
resumen: >-
  Las cuentas corrientes son los libros auxiliares que llevan el saldo de cada cliente y de cada proveedor por separado, mientras el mayor guarda una sola cuenta de control cuyo saldo tiene que ser igual a la suma del auxiliar.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 7.4 Prepare a Subsidiary Ledger: https://openstax.org/books/principles-financial-accounting/pages/7-4-prepare-a-subsidiary-ledger"
  - "OpenStax, Principles of Financial Accounting (2019), 7.2 Describe and Explain the Purpose of Special Journals (según el resumen del capítulo): https://openstax.org/books/principles-financial-accounting/pages/7-2-describe-and-explain-the-purpose-of-special-journals-and-their-importance-to-stakeholders"
  - "OpenStax, Principles of Financial Accounting (2019), 9.2 Account for Uncollectible Accounts Using the Balance Sheet and Income Statement Approaches: https://openstax.org/books/principles-financial-accounting/pages/9-2-account-for-uncollectible-accounts-using-the-balance-sheet-and-income-statement-approaches"
  - "Contabilidad/.investigacion/registro-y-fundamentos.md (2026-11-27)"
aliases: [cuenta corriente, cuentas corrientes, libro auxiliar, auxiliar, subsidiary ledger, subledger, auxiliar de clientes, accounts receivable subsidiary ledger, auxiliar de proveedores, accounts payable subsidiary ledger, cuenta de control, controlling account, control account, antigüedad de saldos, aging, aging of receivables, deudores por ventas, proveedores]
creado: 2026-11-27
revisado: 2026-11-27
---

# Cuentas corrientes

Las cuentas corrientes son los libros auxiliares que llevan el saldo de cada cliente y de cada proveedor por separado, mientras el mayor guarda una sola cuenta de control cuyo saldo tiene que ser igual a la suma del auxiliar.

Resuelven un choque entre dos necesidades. El [plan de cuentas](plan-de-cuentas.md) tiene que ser corto para que los estados contables se lean; la empresa necesita saber cuánto le debe cada cliente y cuánto le debe a cada proveedor. El auxiliar guarda el detalle y el mayor, el total.

## Auxiliar y cuenta de control

Según OpenStax, el libro auxiliar registra el saldo de cada cliente, en el caso de las cuentas a cobrar, y de cada proveedor, en el de las cuentas a pagar. La cuenta del mayor (Cuentas a cobrar, Proveedores) funciona como cuenta de control: su saldo tiene que coincidir con la suma de los saldos del auxiliar, y si no coincide hay un error que buscar.

Las ventas a crédito se pasan al auxiliar cliente por cliente y al mayor en total, según el resumen del capítulo 7 de OpenStax. En los libros de texto eso pasa por diarios especiales, de los que solo se leyó el título y el resumen del capítulo 7.

Una cuenta corriente de cliente muestra, para cada comprobante, la fecha, el tipo (factura, nota de crédito, recibo), el importe al debe o al haber y el saldo que va quedando. Es el mismo formato del mayor aplicado a una persona en lugar de a una cuenta (inferencia de la base).

## Un auxiliar que coincide con su control

El ejemplo de OpenStax, una empresa llamada Store Inc. al 31 de enero (cifras en dólares):

| Cliente | Saldo |
|---|---|
| PB&J | 0 |
| Jones Co. | 328 |
| Black & White Inc. | 0 |
| Tiny Tim's Inc. | 2.661 |
| **Total del auxiliar** | **2.989** |
| Cuentas a cobrar en el mayor | 2.989 |

| Proveedor | Saldo |
|---|---|
| D & D Inc. | 5.646 |
| BSA | 0 |
| Dow John | 425 |
| **Total del auxiliar** | **6.071** |
| Cuentas a pagar en el mayor | 6.071 |

Los dos totales coinciden con su cuenta de control. Cuando no coinciden, lo habitual es un comprobante cargado en un lado y no en el otro, o imputado al cliente equivocado (inferencia de la base). Comparar los dos y explicar la diferencia es una conciliación, y su procedimiento está en [conciliaciones](../Control-interno/conciliaciones.md).

## La antigüedad de saldos

La antigüedad de saldos (aging) ordena lo que deben los clientes según cuánto tiempo lleva vencido. OpenStax la presenta como una forma de estimar incobrables: las cuentas a cobrar se agrupan en tramos por tiempo pendiente, y cuanto más tiempo pasa sin cobrar, menos probable es cobrar.

El ejemplo del libro, la empresa Billie's Watercraft Warehouse, aplica un porcentaje creciente a cada tramo:

| Tramo | Saldo | Porcentaje estimado incobrable | Estimación |
|---|---|---|---|
| 0 a 30 días | 145.740 | 10 % | 14.574 |
| 31 a 90 días | 102.100 | 20 % | 20.420 |
| Más de 90 días | 77.010 | 30 % | 23.103 |
| **Total** | **324.850** | | **58.097** |

Con esa estimación, el asiento de la previsión es:

| Cuenta | Debe | Haber |
|---|---|---|
| Deudores incobrables (gasto) | 58.097 | |
| Previsión para deudores incobrables | | 58.097 |

La previsión es una contracuenta que resta de Cuentas a cobrar sin tocar el auxiliar: no se sabe todavía qué cliente no va a pagar (explicación de la base). Cómo sigue el ciclo (dar de baja un crédito, recuperar uno dado de baja) está en [ingresos y cuentas a cobrar](../Operaciones/ingresos-y-cuentas-a-cobrar.md).

El mismo informe sirve para cobrar: dice a quién llamar primero. OpenStax lo trata solo como estimación de incobrables, y ninguna fuente leída lo trata como herramienta de cobranzas; ese uso es práctica habitual (inferencia de la base). La gestión del cobro en sí es de Tesorería, en [gestión de la cobranza](../../Tesoreria/Credito-y-cobranzas/gestion-de-la-cobranza.md), que usa este informe. Con proveedores se arma el mismo cuadro al revés, para ver qué vence y cuándo (inferencia de la base).

## Lo que un registro tiene que poder hacer

Las cuentas corrientes ponen tres requisitos en un sistema (inferencia de la base a partir de OpenStax 7.4):

1. Cada línea de asiento sobre Cuentas a cobrar o Cuentas a pagar lleva el cliente o el proveedor; sin él, el auxiliar no se puede armar.
2. La suma del auxiliar y el saldo del control salen del mismo registro, para que solo difieran si hay un error de carga.
3. Un cobro o un pago se puede aplicar a facturas concretas, porque la antigüedad se calcula por comprobante y no por saldo.

Si el auxiliar y el control se guardan en dos lugares que se actualizan por separado, se desincronizan: es el problema que describe [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) para cualquier saldo guardado aparte de sus movimientos.

Para leer más: OpenStax, sección 7.4, para el auxiliar y su control, y 9.2 para la antigüedad. En la 7.4 conviene fijarse en que la suma del auxiliar coincide con el control; en la 9.2, en la tabla de tres tramos con porcentajes crecientes.
