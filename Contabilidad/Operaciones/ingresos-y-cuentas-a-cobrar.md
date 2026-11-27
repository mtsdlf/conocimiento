---
resumen: >-
  Un ingreso se reconoce cuando la empresa le transfiere al cliente el bien o el servicio prometido, y desde ahí nace una cuenta a cobrar que se cancela con el cobro, se reduce con una nota de crédito o se da de baja si el cliente no paga.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIIF 15 Ingresos de actividades ordinarias procedentes de contratos con clientes, resumen oficial: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/"
  - "IFRS Foundation, NIIF 15, texto oficial (edición HTML 2026): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "IFRS Foundation, NIIF 15, Ejemplos ilustrativos, Ejemplo 38: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15-ie.html"
  - "IFRS Foundation, NIIF 9 Instrumentos financieros, texto oficial (edición HTML 2026): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html"
  - "OpenStax, Principles of Financial Accounting (2019), 6.4 ventas: https://openstax.org/books/principles-financial-accounting/pages/6-4-analyze-and-record-transactions-for-the-sale-of-merchandise-using-the-perpetual-inventory-system"
  - "OpenStax, Principles of Financial Accounting (2019), 4.2 ajustes: https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries"
  - "OpenStax, Principles of Financial Accounting (2019), 9.2 incobrables: https://openstax.org/books/principles-financial-accounting/pages/9-2-account-for-uncollectible-accounts-using-the-balance-sheet-and-income-statement-approaches"
  - "Contabilidad/.investigacion/operaciones.md (2026-11-27)"
aliases: [ingresos, reconocimiento de ingresos, revenue recognition, cuentas a cobrar, cuentas por cobrar, accounts receivable, deudores por ventas, NIIF 15, IFRS 15, ingresos diferidos, deferred revenue, pasivo del contrato, contract liability, incobrables, previsión para incobrables, allowance for doubtful accounts]
creado: 2026-11-27
revisado:
---

# Ingresos y cuentas a cobrar

Un ingreso se reconoce cuando la empresa le transfiere al cliente el bien o el servicio prometido, y desde ahí nace una cuenta a cobrar que se cancela con el cobro, se reduce con una nota de crédito o se da de baja si el cliente no paga.

Es el ciclo de la venta al cobro visto desde el registro. El presupuesto y el pedido de venta son del tema Relación con clientes, todavía no escrito, y no generan asiento. Cobrar la plata es de Tesorería; registrar el cobro es de acá. Cada cliente tiene su saldo en las [cuentas corrientes](../Registro/cuentas-corrientes.md), cuyo total coincide con la cuenta Cuentas a cobrar del mayor.

## Cuándo hay un ingreso: los cinco pasos de la NIIF 15

La NIIF 15 ordena el reconocimiento de ingresos alrededor de un principio: "an entity recognises revenue to depict the transfer of promised goods or services to the customer". Lo aplica en cinco pasos:

1. Identificar el contrato con el cliente.
2. Identificar cada promesa separada que contiene (la norma las llama obligaciones de desempeño).
3. Determinar el precio de la transacción, estimando la parte variable si la hay.
4. Repartir ese precio entre las promesas según lo que valdría cada una vendida sola.
5. Reconocer el ingreso al cumplir cada promesa, en un momento o a lo largo del tiempo.

El momento lo marca el control: la norma dice que el bien se transfiere "when (or as) the customer obtains control of that asset". Una venta de mercadería se reconoce al entregar; un servicio de un año, mes a mes (ejemplos propios). Para que haya contrato, entre otras condiciones, tiene que ser "probable that the entity will collect the consideration".

La contraprestación variable, el derecho de devolución y las licencias tienen reglas propias en la norma, que la investigación no cubrió. La NIIF 15 rige para los ejercicios que empiezan desde el 1 de enero de 2018.

## La factura, la nota de crédito y el cobro

La factura con entrega registra el ingreso y la cuenta a cobrar, y si hay stock, también el costo (ver [costo de lo vendido](costo-de-lo-vendido.md)). El ejemplo de OpenStax 6.4 sigue a una empresa que vende el 1 de octubre 55 impresoras a $350 ($19.250) que le costaron $100 cada una. El 6 de octubre el cliente devuelve 10. La nota de crédito revierte las dos partes de la venta:

| Cuenta | Debe | Haber |
|---|---|---|
| Devoluciones sobre ventas | 3.500 | |
| Cuentas a cobrar | | 3.500 |
| Inventario | 1.000 | |
| Costo de lo vendido | | 1.000 |

Después la empresa concede una rebaja de $300 y el cliente paga el 15 de octubre dentro del plazo del descuento del 10 %, sobre un saldo de $15.450:

| Cuenta | Debe | Haber |
|---|---|---|
| Caja | 13.905 | |
| Descuentos sobre ventas | 1.545 | |
| Cuentas a cobrar | | 15.450 |

Las devoluciones, rebajas y descuentos van a cuentas propias que restan de las ventas en el estado de resultados. Así, por inferencia propia, la venta original no se toca y queda a la vista cuánto se devolvió y cuánto se descontó. Un registro que permite editar la factura en lugar de emitir una nota de crédito pierde esa información (también inferencia); corregir sin borrar está en [asiento y libros](../Registro/asiento-y-libros.md).

## Cobrar antes de entregar: anticipos e ingresos diferidos

Si el cliente paga antes de recibir, la empresa tiene una deuda: le debe el bien o el servicio. La NIIF 15 la llama pasivo del contrato, "an entity's obligation to transfer goods or services to a customer for which the entity has received consideration (or an amount of consideration is due)". La cuenta a cobrar, en cambio, es "an entity's right to consideration that is unconditional": solo falta que pase el tiempo.

El Ejemplo 38 de la NIIF 15 muestra la diferencia con un contrato de CU1.000 que no se puede cancelar, con vencimiento de pago el 31 de enero, cobro el 1 de marzo y entrega el 31 de marzo:

| Fecha | Cuenta | Debe | Haber |
|---|---|---|---|
| 31 de enero | Cuentas a cobrar | 1.000 | |
| | Pasivo del contrato | | 1.000 |
| 1 de marzo | Caja | 1.000 | |
| | Cuentas a cobrar | | 1.000 |
| 31 de marzo | Pasivo del contrato | 1.000 | |
| | Ingresos | | 1.000 |

Si el contrato se puede cancelar, el 31 de enero no hay derecho incondicional y no se registra nada: el 1 de marzo el cobro va directo contra el pasivo del contrato.

Una suscripción sigue el mismo patrón: se cobra por adelantado y el ingreso se devenga a medida que pasa el período. OpenStax 4.2 lo muestra con un estudio de abogados que cobra $48.000 de honorarios por adelantado (Caja contra Honorarios no devengados, un pasivo). Al cierre había prestado el 40 % del servicio:

| Cuenta | Debe | Haber |
|---|---|---|
| Honorarios no devengados | 19.200 | |
| Honorarios | | 19.200 |

Quedan $28.800 como pasivo hasta que se preste el resto. Ese ajuste es un [ajuste de cierre](../Estados-contables/ajustes-de-cierre.md) y la regla de fondo es el [devengado](../Registro/devengado.md).

> [!NOTE] Sin fuente todavía: un ejemplo de suscripción de software con sus asientos mes a mes; el de OpenStax es de honorarios y sigue el mismo patrón.

## Los clientes que no pagan: la previsión para incobrables

Una parte de las ventas a crédito no se va a cobrar, y el registro tiene que reflejarlo antes de saber qué cliente falla. El método de la previsión estima la pérdida al cierre y la carga contra una cuenta que resta de Cuentas a cobrar en el balance. Cuando un cliente concreto resulta incobrable, se lo da de baja contra la previsión, sin tocar resultados otra vez.

OpenStax 9.2 lo muestra con ventas a crédito de $458.230 y una estimación del 5 %:

| Cuenta | Debe | Haber |
|---|---|---|
| Incobrables | 22.911,50 | |
| Previsión para incobrables | | 22.911,50 |

La baja de un cliente por $5.000 es Previsión al debe y Cuentas a cobrar al haber. Si después paga $3.000, se repone la cuenta a cobrar contra la previsión y se registra el cobro. El libro también calcula la previsión por antigüedad de saldos: 10 %, 20 % y 30 % sobre tramos de $145.740, $102.100 y $77.010 dan $58.097. La antigüedad sale del auxiliar de [cuentas corrientes](../Registro/cuentas-corrientes.md).

El método de baja directa, que carga la pérdida recién cuando se identifica al cliente, no lo acepta el US GAAP según OpenStax, porque separa el gasto del período de la venta; el libro dice que se usa para impuestos.

La NIIF 9 pide otra base para la misma previsión. Para las cuentas a cobrar comerciales sin financiación significativa, la empresa "shall always measure the loss allowance at an amount equal to lifetime expected credit losses": la pérdida esperada en toda la vida del crédito, mirando hacia adelante. Como atajo práctico admite una matriz de provisiones con la experiencia histórica ajustada, que se parece al cálculo por antigüedad. Según la lectura del informe de investigación (no de las fuentes), las dos coinciden en la mecánica (previsión que resta del activo, baja contra la previsión) y difieren en la base de la estimación: OpenStax enseña porcentajes históricos del US GAAP clásico y la NIIF 9 exige pérdida esperada. Qué marco aplica a cada empresa está en [normas contables](../Estados-contables/normas-contables.md).

Para quien construye un sistema, esto se traduce (inferencia) en que la baja de un cliente tiene que poder registrarse contra la previsión y no contra un gasto, y en que el auxiliar tiene que dar la antigüedad de cada saldo a una fecha.
