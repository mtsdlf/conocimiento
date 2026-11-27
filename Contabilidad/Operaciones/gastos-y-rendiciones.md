---
resumen: >-
  Los gastos de empleados son compras chicas que paga una persona de la empresa con plata propia, con un anticipo o con un fondo fijo, y que se registran recién cuando rinde los comprobantes.
estado: borrador
estabilidad: semi
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 8.4 caja chica: https://openstax.org/books/principles-financial-accounting/pages/8-4-define-the-purpose-and-use-of-a-petty-cash-fund-and-prepare-petty-cash-journal-entries"
  - "Washington State Auditor's Office, Best practices for travel and reimbursable expenses (enero de 2024): https://www.sao.wa.gov/sites/default/files/2024-01/Travel_and_Reimbursable_Expenses_1_11_24_updated.pdf"
  - "MNCPA, Employee expense reimbursements: legitimate or fraudulent? (2015, vía buscador): https://mncpa.org/publications/footnote/2015-02/employee-expense-reimbursements-legitimate-or-fraudulent"
  - "New York Office of the State Comptroller, auditoría de anticipos (vía buscador): https://www.osc.ny.gov/files/state-agencies/pdf/XII-4-B-1-att6.pdf"
  - "Contabilidad/.investigacion/operaciones.md (2026-11-27)"
aliases: [gastos de empleados, rendición de gastos, rendiciones, expense report, expense reimbursement, reintegro de gastos, anticipo a rendir, anticipo de viáticos, travel advance, fondo fijo, caja chica, petty cash, imprest]
creado: 2026-11-27
revisado:
---

# Gastos y rendiciones

Los gastos de empleados son compras chicas que paga una persona de la empresa con plata propia, con un anticipo o con un fondo fijo, y que se registran recién cuando rinde los comprobantes.

Contablemente es el ciclo de [compras y cuentas a pagar](compras-y-cuentas-a-pagar.md) con el empleado en el lugar del proveedor: hay un gasto, un comprobante y una deuda o un crédito que se cancela. Los libros de texto no lo tratan como ciclo propio; lo ponen dentro de la caja y el control interno. Se separa porque su recorrido es distinto (quien gasta no es quien compra, el comprobante llega después y la aprobación la da un jefe), y las guías de auditoría leídas lo revisan aparte.

## Las tres formas de pagar un gasto de empleado

| Forma | Quién pone la plata | Qué queda pendiente hasta la rendición |
|---|---|---|
| Reintegro | el empleado | una deuda de la empresa con el empleado |
| Anticipo a rendir | la empresa, antes del gasto | un crédito de la empresa contra el empleado |
| Fondo fijo | la empresa, en un fondo permanente | nada: el fondo se repone contra comprobantes |

En las tres el gasto se registra con el comprobante, en la cuenta que corresponde a su naturaleza (viáticos, combustible, papelería), y no al entregar la plata. Salvo en el fondo fijo (OpenStax), esto es construcción propia: ver la nota sobre anticipos más abajo.

## El fondo fijo y su reposición

El fondo fijo, o caja chica, es según OpenStax una suma predeterminada de efectivo que se tiene a mano para pagos chicos del día a día. Es una cuenta de importe fijo: lo que se gasta se repone, de modo que en todo momento el efectivo más los comprobantes suman el monto del fondo. El gasto se carga al reponer, con los comprobantes a la vista. Un faltante va a una cuenta de diferencias de caja; un sobrante invierte ese asiento.

El ejemplo de OpenStax 8.4 es una tienda de yogur que el 1 de julio crea un fondo de $75:

| Cuenta | Debe | Haber |
|---|---|---|
| Fondo fijo | 75 | |
| Caja | | 75 |

El 31 de julio repone el fondo contra los comprobantes del mes:

| Cuenta | Debe | Haber |
|---|---|---|
| Franqueo | 30 | |
| Inventario | 10 | |
| Gastos varios | 5 | |
| Caja | | 45 |

El 1 de agosto sube el fondo a $100 (Fondo fijo 25 contra Caja 25). Si al reponer faltan $5, se registra Diferencias de caja 5 al debe y Caja 5 al haber.

La cuenta Fondo fijo solo se mueve al crearlo, al cambiar su monto o al cerrarlo. Los gastos nunca van contra ella: van contra Caja (o el banco) al reponer. Quien construye un sistema puede leer de acá qué tiene que impedir: un asiento de gasto contra la cuenta del fondo rompe la regla de que su saldo es fijo. Esta lectura es inferencia a partir del mecanismo.

## Anticipos y rendiciones

Un anticipo es plata que la empresa le da al empleado antes de un gasto, por ejemplo un viaje. Mientras no rinde, la empresa tiene un crédito contra él. Al rendir, los comprobantes pasan a gasto y la diferencia se devuelve o se le paga.

El patrón del asiento es: al dar el anticipo, Anticipos a rendir al debe y Caja al haber; al rendir, cada gasto al debe y Anticipos a rendir al haber; si sobró, Caja al debe por lo que devuelve; si faltó, una deuda con el empleado al haber hasta reintegrarle. Este patrón es una construcción a partir del devengado y del fondo fijo: ninguna fuente leída lo trae con números.

> [!NOTE] Sin fuente todavía: los asientos de un anticipo a empleado y su rendición en un libro de texto, y una guía de gastos de empleados del sector privado (las encontradas son de organismos públicos de Estados Unidos).

Las guías de auditoría pública de Estados Unidos que se leyeron traen controles sobre los anticipos. La del Auditor del Estado de Washington (enero de 2024) recomienda limitar el anticipo a una parte del gasto estimado, no darlo con demasiada anticipación, asignar a alguien el seguimiento de los que están vencidos, no dar un anticipo nuevo a quien no rindió el anterior y resolver los pendientes antes de liquidarle el final a quien se va. Pide también una política escrita, revisada cada año y actualizada al menos cada tres.

## Cómo falla la rendición

La rendición falla (explicación propia, sin fuente) cuando nadie mira el comprobante o cuando quien lo aprueba es quien gasta. Según resúmenes de dos guías profesionales leídas por el buscador (un colegio de contadores de Minnesota y la contraloría del Estado de Nueva York), una rendición sana lleva el comprobante original, el propósito del gasto, la aprobación firmada y con fecha, y una revisión de segundo nivel sobre una muestra. La conciliación de los anticipos la tiene que hacer alguien que no registre cobros ni pagos, que es un caso de [separación de funciones](../Control-interno/separacion-de-funciones.md). Los niveles de aprobación según el monto están en [autorizaciones](../Control-interno/autorizaciones.md).

Para quien construye un sistema, estos controles se traducen (inferencia) en requisitos del registro: el gasto pide un comprobante adjunto y un aprobador distinto de quien lo carga, el anticipo tiene un saldo por empleado con fecha de vencimiento, y la baja de un empleado muestra sus anticipos abiertos. Cómo se liquida lo que se le debe a un empleado que se va es del tema Administración de personal y nómina, todavía no escrito.
