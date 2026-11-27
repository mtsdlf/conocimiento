---
resumen: >-
  Las operaciones son los hechos habituales de una empresa (vender, comprar, gastar, pagar sueldos, usar una máquina, operar en otra moneda) y cada una llega al registro con un documento que dispara un asiento de forma conocida.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 6.3 compras con inventario permanente: https://openstax.org/books/principles-financial-accounting/pages/6-3-analyze-and-record-transactions-for-merchandise-purchases-using-the-perpetual-inventory-system"
  - "OpenStax, Principles of Financial Accounting (2019), 6.4 ventas con inventario permanente: https://openstax.org/books/principles-financial-accounting/pages/6-4-analyze-and-record-transactions-for-the-sale-of-merchandise-using-the-perpetual-inventory-system"
  - "OpenStax, Principles of Financial Accounting (2019), 4.2 ajustes: https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries"
  - "OpenStax, Principles of Financial Accounting (2019), 12.5 sueldos: https://openstax.org/books/principles-financial-accounting/pages/12-5-record-transactions-incurred-in-preparing-payroll"
  - "IFRS Foundation, NIC 19 Beneficios a los empleados, texto oficial (edición HTML 2026): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias19.html"
  - "Contabilidad/.investigacion/operaciones.md (2026-11-27)"
aliases: [operaciones contables, ciclos contables, ciclos de transacciones, transaction cycles, sueldos, asiento de sueldos, payroll accounting]
creado: 2026-11-27
revisado: 2026-11-27
---

# Operaciones

Las operaciones son los hechos habituales de una empresa (vender, comprar, gastar, pagar sueldos, usar una máquina, operar en otra moneda) y cada una llega al registro con un documento que dispara un asiento de forma conocida.

Esta vertical aplica a cada caso el mecanismo de [Registro](../Registro/registro-contable.md): la [partida doble](../Registro/partida-doble.md) dice que cada hecho toca dos cuentas, y el [devengado](../Registro/devengado.md) dice cuándo se registra. Lo que sale de acá se resume en los [estados contables](../Estados-contables/estados-contables.md), le da costos a la [contabilidad de gestión](../Contabilidad-de-gestion/contabilidad-de-gestion.md) y lo vigila el [control interno](../Control-interno/control-interno.md), que decide quién puede aprobar cada documento.

## Los ciclos que llegan al registro

El campo agrupa las operaciones en ciclos: de la venta al cobro, de la compra al pago, el inventario y su costo, los activos fijos y los sueldos. Cada ciclo lo recorren otras áreas (ventas, compras, depósito, personal); la contabilidad entra cuando aparece un documento que cambia el patrimonio. Por eso (explicación propia, sin fuente leída) el pedido de un cliente o la orden de compra no generan asiento: todavía no pasó nada que la empresa deba o tenga derecho a cobrar.

La tabla resume qué documento dispara qué asiento. Los patrones salen de OpenStax y de la NIC 2; la tabla como síntesis es del informe de investigación.

| Ciclo | Documento o hecho | Asiento típico (debe / haber) | Dónde se explica |
|---|---|---|---|
| Ventas | Factura de venta con entrega | Cuentas a cobrar / Ventas, y Costo de lo vendido / Inventario | [ingresos](ingresos-y-cuentas-a-cobrar.md), [costo de lo vendido](costo-de-lo-vendido.md) |
| Ventas | Cobro | Caja / Cuentas a cobrar | [ingresos](ingresos-y-cuentas-a-cobrar.md) |
| Ventas | Nota de crédito por devolución | Devoluciones sobre ventas / Cuentas a cobrar, e Inventario / Costo de lo vendido | [ingresos](ingresos-y-cuentas-a-cobrar.md) |
| Compras | Recepción sin factura | Inventario / Recepciones no facturadas | [compras](compras-y-cuentas-a-pagar.md) |
| Compras | Factura del proveedor | Inventario o gasto / Cuentas a pagar | [compras](compras-y-cuentas-a-pagar.md) |
| Gastos | Rendición con comprobantes | Gasto / Caja o deuda con el empleado | [gastos y rendiciones](gastos-y-rendiciones.md) |
| Inventario | Rebaja a valor neto de realización | Resultado / Inventario | [costo de lo vendido](costo-de-lo-vendido.md) |
| Activos | Compra de un activo fijo | Activo / Caja o Cuentas a pagar | [activos fijos](activos-fijos-y-amortizacion.md) |
| Activos | Amortización del período | Amortización del período / Amortización acumulada | [activos fijos](activos-fijos-y-amortizacion.md) |
| Sueldos | Sueldos devengados | Sueldos / varios pasivos | la sección de abajo |

Una venta con stock lleva dos asientos, porque mueve dos cosas: el derecho a cobrar y la mercadería que sale. En el ejemplo de OpenStax 6.4, una empresa vende el 1 de octubre 55 impresoras a $350 que le habían costado $100 cada una:

| Cuenta | Debe | Haber |
|---|---|---|
| Cuentas a cobrar | 19.250 | |
| Ventas | | 19.250 |
| Costo de lo vendido | 5.500 | |
| Inventario | | 5.500 |

El primer par registra el ingreso; el segundo, el costo de lo que se entregó. El margen bruto aparece el día de la venta, aunque la plata llegue después.

Para quien construye un sistema, la tabla dice qué documentos tienen que existir para que el registro esté completo: si un hecho no tiene documento, no hay de dónde sacar el asiento. Que el saldo se calcule sumando movimientos que no se editan es la idea del [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).

## Moneda extranjera atraviesa todos los ciclos

La [moneda extranjera](moneda-extranjera.md) aparece en cualquier ciclo cuando una venta, una compra, un préstamo o una cuenta bancaria están en una moneda distinta de la funcional. El asiento de cada ciclo sigue igual y se le suma una conversión al registrar y otra cada vez que la partida se liquida o llega un cierre. La diferencia entre esos tipos de cambio va a resultados.

## Cómo se registran los sueldos

Los sueldos se registran cuando el empleado trabaja, aunque se paguen después. La NIC 19 pide reconocer los beneficios de corto plazo, cuando el empleado prestó el servicio, "as a liability (accrued expense), after deducting any amount already paid" y "as an expense", salvo que otra norma permita sumarlos al costo de un activo (como el inventario o una máquina en construcción).

El asiento tiene tres partes. El sueldo bruto es gasto. Lo que se le retiene al empleado (aportes, impuestos, cuotas) y el neto que se le va a pagar son pasivos, deudas con terceros y con el empleado. Las cargas que paga el empleador por su cuenta son un gasto aparte con su propio pasivo. El ejemplo de OpenStax 12.5 es de Estados Unidos, con sus porcentajes y organismos; lo que se lleva a cualquier país es la estructura. Un sueldo bruto de $2.000 al 31 de agosto:

| Cuenta | Debe | Haber |
|---|---|---|
| Sueldos | 2.000 | |
| Seguro social a pagar | | 124 |
| Medicare a pagar | | 29 |
| Retención de impuesto federal | | 102 |
| Retención de impuesto estatal | | 25 |
| Seguro de salud del empleado a pagar | | 200 |
| Plan de retiro a pagar | | 150 |
| Sueldos a pagar | | 1.370 |

El 1 de septiembre se paga el neto: Sueldos a pagar 1.370 al debe, Caja 1.370 al haber. Las cargas del empleador se registran aparte:

| Cuenta | Debe | Haber |
|---|---|---|
| Cargas sociales | 265 | |
| Desempleo federal a pagar | | 12 |
| Desempleo estatal a pagar | | 100 |
| Seguro social a pagar | | 124 |
| Medicare a pagar | | 29 |

Un beneficio que paga el empleador (en el ejemplo, $300 de seguro de salud) es otro gasto contra su pasivo. Si el cierre cae entre el trabajo y la liquidación, los sueldos se devengan con un [ajuste de cierre](../Estados-contables/ajustes-de-cierre.md); OpenStax 4.2 lo muestra con 5 empleados a $2.500: Sueldos 12.500 al debe, Sueldos a pagar 12.500 al haber.

Las vacaciones siguen la misma lógica. Según la NIC 19, las ausencias pagadas que se acumulan se reconocen mientras el empleado presta el servicio que le da derecho a ellas; las que no se acumulan, cuando ocurre la ausencia. OpenStax las trata como pasivos estimados, sin plazo ni importe ciertos.

> [!NOTE] Sin fuente todavía: un asiento con números del devengamiento de vacaciones.

Cómo se calcula cada concepto del recibo, el legajo y las licencias son del tema Administración de personal y nómina, todavía no escrito. Los porcentajes de aportes y contribuciones de cada país, también.

## Qué hay adentro de Operaciones

- [Ingresos y cuentas a cobrar](ingresos-y-cuentas-a-cobrar.md): cuándo se reconoce un ingreso (NIIF 15), la factura, el cobro, la nota de crédito, los anticipos, los ingresos diferidos y los incobrables.
- [Compras y cuentas a pagar](compras-y-cuentas-a-pagar.md): la factura del proveedor, el cruce de tres vías visto desde el registro, lo recibido sin facturar y el pago.
- [Gastos y rendiciones](gastos-y-rendiciones.md): los gastos que paga un empleado, los anticipos a rendir y el fondo fijo.
- [Costo de lo vendido](costo-de-lo-vendido.md): inventario permanente o periódico, PEPS, promedio ponderado y UEPS, y el valor neto de realización.
- [Activos fijos y amortización](activos-fijos-y-amortizacion.md): qué se capitaliza, cómo se amortiza, qué pasa al vender un activo, y por qué la amortización no guarda plata.
- [Moneda extranjera](moneda-extranjera.md): moneda funcional, conversión y diferencia de cambio.
