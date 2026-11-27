---
resumen: >-
  La programación de pagos decide qué factura aprobada se paga en qué fecha: respeta el vencimiento que fija la condición de pago, toma el descuento por pronto pago solo cuando cuesta menos que la plata que hay que usar para tomarlo, y ordena las prioridades cuando la caja no alcanza.
estado: vigente
estabilidad: semi
fuentes:
  - "OpenStax, Principles of Finance (2022), 19.2 What Is Trade Credit? (leído): https://openstax.org/books/principles-finance/pages/19-2-what-is-trade-credit"
  - "OpenStax, Principles of Finance 2e (2026), 19.2 What Is Trade Credit? (leído, solo para las definiciones de Net 30 y 2/10 n/30): https://openstax.org/books/principles-of-finance-2e/pages/19-2-what-is-trade-credit"
  - "APQC, Process Classification Framework 7.4 (2024), 9.6.1 y 9.7.2 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "IRS, Employment taxes and the Trust Fund Recovery Penalty (leído): https://www.irs.gov/TFRP"
  - "Petersen y Rajan, Trade Credit: Theories and Evidence, Review of Financial Studies (1997) (abstract): https://ideas.repec.org/a/oup/rfinst/v10y1997i3p661-91.html"
  - "Deloof, Does Working Capital Management Affect Profitability of Belgian Firms?, Journal of Business Finance & Accounting (2003) (abstract): https://ideas.repec.org/a/bla/jbfnac/v30y2003i3-4p573-588.html"
  - "Tesoreria/.investigacion/pagos-a-proveedores.md, sección 1 (2026-11-27)"
  - "Tesoreria/.investigacion/pagos-y-politica-verificacion.md (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, secciones 3 y 6 (2026-11-27)"
  - "Tesoreria/.investigacion/fundamentos-y-contraria.md, secciones 4.1 y 5 (2026-11-27)"
aliases: [programación de pagos, payment scheduling, calendario de pagos, descuento por pronto pago, early-payment discount, cash discount, costo de no tomar el descuento, cost of forgoing a discount, crédito comercial, trade credit, prioridades de pago]
creado: 2026-11-27
revisado: 2026-11-27
---

# Programación de pagos

La programación de pagos decide qué factura aprobada se paga en qué fecha: respeta el vencimiento que fija la condición de pago, toma el descuento por pronto pago solo cuando cuesta menos que la plata que hay que usar para tomarlo, y ordena las prioridades cuando la caja no alcanza.

Es el primer paso de los [pagos a proveedores](pagos-a-proveedores.md). Recibe facturas que ya se deben: el cruce con el pedido y la recepción, y el asiento de la deuda, están en [compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md). Entrega una lista de qué pagar y cuándo a la [corrida de pagos](corrida-de-pagos.md), que la aprueba y la manda al banco. Cada fecha que se elige acá mueve la [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md) y los días de pago del [capital de trabajo](../Caja-y-liquidez/capital-de-trabajo.md).

## La condición de pago fija dos fechas

La condición de pago es un dato de la factura, pactado con el proveedor. OpenStax define el plazo neto: con «Net 30», la factura se paga entera dentro de los 30 días de su fecha. La condición «2/10 neto 30» suma un descuento: 2 % si se paga dentro de los 10 días, y el total a los 30 (*Principles of Finance*, 19.2).

Para programar, cada factura lleva dos fechas calculadas desde su fecha de emisión: el límite del descuento, si lo hay, y el vencimiento. Entre una y otra, la empresa usa plata del proveedor. OpenStax llama al crédito comercial una forma de financiamiento que suele verse como sin costo, y en la misma sección dice que quien no toma el descuento paga más. Las dos cosas son ciertas a la vez: el crédito es gratis hasta el límite del descuento, y desde ahí hasta el vencimiento tiene un costo.

En un sistema, por inferencia de esta base, las dos fechas se calculan al registrar la factura y quedan guardadas, para que la lista de pagos se pueda filtrar por «vence antes del viernes» o «pierde el descuento antes del viernes». La condición de pago del proveedor vive en su ficha, como la del cliente vive en las [condiciones comerciales](../../Relacion-con-clientes/Registro-del-cliente/condiciones-comerciales.md).

## El costo de no tomar un descuento por pronto pago

No tomar el descuento equivale a pedirle prestado al proveedor el monto de la factura durante los días que van del límite del descuento al vencimiento, y pagar el descuento perdido como interés. OpenStax lo anualiza así:

> costo anual = [360 / (plazo total − plazo del descuento)] × [descuento % / (100 − descuento %)]

Con 2/10 neto 30: 360/20 × 2/98 = 36,73 %. El libro lo dice con su ejemplo: «The annual cost to NAI of not taking advantage of the discount for quick payment is 36.73 percent» (19.2). Es una tasa anual simple, con año comercial de 360 días; el libro no da una tasa efectiva.

La misma condición da otros números según la base de cálculo. Estas cuentas son de esta base, hechas con la fórmula de arriba y comprobadas en una planilla:

| Condición | Año de 360 días, simple | Año de 365 días, simple | Año de 365 días, capitalizada |
|---|---|---|---|
| 2/10 neto 30 | 36,73 % | 37,24 % | 44,59 % |
| 1/10 neto 30 | 18,18 % | | |
| 2/10 neto 60 | 14,69 % | | |
| 5/10 neto 30 | 94,74 % | | |

La versión capitalizada es (1 + 2/98)^(365/20) − 1: supone que la empresa repite el préstamo cada 20 días durante el año. Es la que se compara con una tasa efectiva anual, como la de un préstamo o un descubierto. Cómo pasar de tasa nominal a efectiva, y cómo comparar fuentes de plata entre sí, está en [costo del financiamiento](../Financiamiento/costo-del-financiamiento.md). Esta nota es la dueña de la fórmula del descuento y aquella la enlaza. El 5/10 neto 30 es la condición del ejemplo con que [compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md) muestra el asiento del descuento: renunciar a él cuesta 94,74 % anual.

Al escribir una de estas cifras hay que decir la base: 36,73 % y 44,59 % describen la misma condición.

## Cuándo conviene tomar el descuento

La regla que sale de la cuenta, como lectura de esta base y no de una fuente, es comparar el costo de no tomar el descuento con el costo de la plata que la empresa usaría para tomarlo. Si sobra caja que rinde menos que ese costo, conviene pagar antes. Si hay que tomar un descubierto o una línea de crédito para pagar antes, conviene solo si su tasa efectiva es menor. En un país con inflación alta las tasas se mueven seguido, y la comparación se hace con la del momento ([tesorería en Argentina](../tesoreria-en-argentina.md)).

Si no se toma el descuento, la regla que sigue es pagar el último día del plazo y no antes: pagar el día 15 un 2/10 neto 30 pierde el descuento y además adelanta la salida de caja (lectura de esta base). Un sistema que propone pagos ayuda si muestra, para cada factura, cuánto cuesta en tasa anual dejar pasar el descuento, al lado del costo de la plata de la empresa que fija la [política de tesorería](../politica-de-tesoreria.md).

## Pagar tarde y estirar los plazos

Pagar después del vencimiento tiene costos explícitos y otros que no se ven. OpenStax nombra los primeros: algunos acuerdos de pago «specify an interest penalty or a late fee when the account goes delinquent». Y nombra uno de los segundos: pagar a tiempo «helps create a credit history for the purchasing firm» (19.2). El libro no trata el estirar plazos como práctica ni mide su costo en la relación con el proveedor.

La evidencia sobre quién estira es de abstracts, leídos solo en su resumen. Petersen y Rajan (1997) encontraron que las empresas chicas usan más crédito comercial cuando las instituciones financieras no les prestan. Deloof (2003), con 1.009 grandes empresas belgas entre 1992 y 1996, encontró que las empresas menos rentables tardan más en pagar sus facturas. Que estirar el pago sea financiamiento con costo, y no un ahorro gratis, es la lectura que hace esta base de esos dos trabajos. El financiamiento de la cadena, en el que un financista le paga antes al proveedor mientras el comprador estira el plazo, tiene su nota en [financiamiento de la cadena](../Financiamiento/financiamiento-de-la-cadena.md).

## Las prioridades cuando la caja no alcanza

Cuando la proyección muestra que la plata de la semana no cubre todo lo que vence, alguien decide qué se paga primero y qué se renegocia. Esa decisión, y quién la toma, la fija la [política de tesorería](../politica-de-tesoreria.md). Los sueldos y los impuestos entran acá como salidas de caja con fecha fija; los sueldos se pagan como dice [pago de sueldos](../Pago-de-sueldos/pago-de-sueldos.md), y qué impuesto vence cuándo es del tema [Impuestos](../../Impuestos/impuestos.md).

Una regla de este orden tiene fuente. En Estados Unidos, el IRS llama impuestos «trust fund» a los que la empresa retiene a sus empleados, porque «you actually hold the employee's money in trust». Dice que usar fondos disponibles para pagar a otros acreedores cuando el negocio no puede pagar esos impuestos indica intención, y la sanción puede cobrarse a la persona responsable. Es una sola fuente y de otro país.

> [!NOTE] Sin fuente todavía: la norma argentina equivalente y un orden de prioridades de pago con método para el resto. El criterio de práctica que circula, sin respaldo leído, pone después de sueldos, cargas sociales, impuestos y servicios básicos a los proveedores críticos o sin reemplazo y a los que dan un descuento mayor que el costo de la plata, y al final el resto, con un plan de pagos acordado por escrito con quien se estira. La prelación legal en un concurso de acreedores es materia de abogados y de cada país.

## Dónde la pone APQC

APQC ubica la aprobación y el proceso de pagos dentro de cuentas a pagar (9.6.1.4 «Approve payments» y 9.6.1.8 «Process payments»), y a la tesorería le deja el pronóstico y el manejo de los flujos de caja (9.7.2.4 y 9.7.2.5). La programación queda en el medio: es una decisión de caja tomada sobre documentos de cuentas a pagar. En una empresa chica la toma la misma persona que paga; en una grande, según cómo esté organizada (lectura de esta base).
