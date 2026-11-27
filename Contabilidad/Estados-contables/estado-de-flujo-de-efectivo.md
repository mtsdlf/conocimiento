---
resumen: >-
  El estado de flujo de efectivo explica cómo cambió la caja de la empresa en un período, separando lo que entró y salió por operar, por invertir en activos de largo plazo y por financiarse.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIC 7 Statement of Cash Flows (página de la norma, según su resumen): https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/"
  - "OpenStax, Principles of Financial Accounting (2019), 16.1 Explain the Purpose of the Statement of Cash Flows: https://openstax.org/books/principles-financial-accounting/pages/16-1-explain-the-purpose-of-the-statement-of-cash-flows"
  - "OpenStax, Principles of Financial Accounting (2019), 16.3 Prepare the Statement of Cash Flows Using the Indirect Method: https://openstax.org/books/principles-financial-accounting/pages/16-3-prepare-the-statement-of-cash-flows-using-the-indirect-method"
  - "Contabilidad/.investigacion/estados-contables.md (2026-11-27)"
aliases: [estado de flujo de efectivo, estado de flujos de efectivo, flujo de caja, estado de origen y aplicación de fondos, cash flow statement, statement of cash flows, método indirecto, indirect method, método directo, direct method, flujo operativo, operating cash flow]
creado: 2026-11-27
revisado:
---

# Estado de flujo de efectivo

El estado de flujo de efectivo explica cómo cambió la caja de la empresa en un período, separando lo que entró y salió por operar, por invertir en activos de largo plazo y por financiarse.

Existe aparte del [estado de resultados](estado-de-resultados.md) porque los dos miden cosas distintas. El resultado se arma por [devengado](../Registro/devengado.md): registra la venta cuando se hace y el gasto cuando se consume. La caja se mueve cuando se cobra y se paga. Según OpenStax, los flujos de caja suelen diferir bastante del resultado devengado. Una empresa puede ganar y quedarse sin plata, o perder y juntar caja (OpenStax trae un caso del segundo tipo; del primero no hay un caso documentado en las fuentes leídas); para quien empieza, esa pregunta es la de la pista, en [finanzas de Emprender](../../Emprender/Finanzas/finanzas.md).

## Las tres actividades

La NIC 7 pide mostrar cómo cambiaron el efectivo y sus equivalentes durante el período, y divide los movimientos en tres actividades. Según el resumen de su página:

| Actividad | Qué incluye | Ejemplos |
|---|---|---|
| De operación | las actividades principales que generan los ingresos de la empresa | cobros a clientes, pagos a proveedores y a empleados |
| De inversión | la compra y la venta de activos de largo plazo y de otras inversiones que no son equivalentes de efectivo | comprar una máquina, vender un terreno |
| De financiación | lo que cambia el tamaño y la composición del capital aportado y de los préstamos | tomar un préstamo, emitir acciones, pagar dividendos |

Las tres suman la variación de la caja, que tiene que coincidir con la diferencia entre la caja del [balance](balance.md) de cierre y la del anterior.

Las operaciones de inversión o financiación que no mueven caja quedan afuera del estado y se revelan aparte. OpenStax da el caso de un terreno comprado con un pagaré de $20.000: hay un activo nuevo y una deuda nueva, y la caja no se movió (el asiento de abajo es armado a partir de ese caso).

| Cuenta | Debe | Haber |
|---|---|---|
| Terrenos | 20.000 | |
| Documentos a pagar | | 20.000 |

## Método directo y método indirecto

Los dos métodos solo cambian la sección de operación; inversión y financiación se arman igual en los dos. Que den el mismo flujo operativo por caminos distintos es lo esperable, pero ninguna fuente leída lo dice.

- El directo muestra las grandes clases de cobros y pagos brutos (cuánto se cobró a clientes, cuánto se pagó a proveedores).
- El indirecto parte del resultado del período y lo corrige por lo que no movió caja (como la amortización) y por las variaciones del capital de trabajo.

El indirecto es una conciliación entre el resultado y la caja, y por eso enseña la diferencia entre los dos. La regla de los signos sale de pensar qué pasó con la plata. Si las cuentas a cobrar bajaron, se cobró más de lo que se vendió, y se suma. Si el inventario subió, se pagó mercadería que todavía no se vendió, y se resta. Con los pasivos es al revés: si las deudas con proveedores bajaron, se pagó más de lo que se compró, y se resta.

## La conciliación de Propensity Company, 2018

OpenStax arma el estado de 2018 de Propensity Company por el método indirecto. Estas son las cifras del estado (en dólares):

| Concepto | Importe |
|---|---|
| Resultado neto | 4.340 |
| Amortización | +14.400 |
| Ganancia por venta de activos | −4.800 |
| Disminución de cuentas a cobrar | +4.500 |
| Aumento de seguros pagados por adelantado | −700 |
| Aumento de inventario | −2.500 |
| Disminución de cuentas a pagar | −1.800 |
| Aumento de sueldos a pagar | +400 |
| Total de ajustes | 9.500 |
| **Flujo de las actividades de operación** | **13.840** |
| Venta de terreno | +14.800 |
| Compra de activos | −60.000 |
| **Flujo de las actividades de inversión** | **−45.200** |
| Pagarés emitidos | +10.000 |
| Acciones emitidas | +45.000 |
| Dividendos pagados | −440 |
| **Flujo de las actividades de financiación** | **+54.560** |
| **Variación neta de la caja** | **+23.200** |

La caja pasó de $24.300 al 31 de diciembre de 2017 a $47.500 al 31 de diciembre de 2018: 13.840 − 45.200 + 54.560 = 23.200. El texto narrativo del libro da $25.200 de inversión y $34.560 de financiación, que no coinciden con el estado; la aritmética respalda las cifras del estado.

Dos líneas muestran cómo piensa el método. La amortización de $14.400 se restó como gasto para llegar al resultado, pero no salió de la caja, así que se suma de vuelta; la amortización no es plata que se guarda, como explica [activos fijos y amortización](../Operaciones/activos-fijos-y-amortizacion.md). La ganancia por la venta de activos ($4.800) se resta porque el cobro entero de esa venta ya aparece en inversión; dejarla en operación lo contaría dos veces (explicación propia, no del libro).

El resultado fue de $4.340 y la operación generó $13.840. La empresa compró activos por $60.000 y en el mismo año emitió acciones y pagarés por $55.000. Esa lectura no surge del estado de resultados.

## Lo que cambia con la NIIF 18

Según el resumen de la página de la NIC 7, una enmienda de 2024, emitida junto con la NIIF 18, cambia dos cosas: el método indirecto pasa a partir del resultado operativo y no del resultado del período, y cambia la clasificación de los intereses y los dividendos entre las tres actividades.

> [!NOTE]
> Sin fuente todavía: el texto de la NIC 7 y de su enmienda de 2024 (en qué actividad van los intereses y los dividendos cobrados y pagados, antes y después del cambio). Se leyó solo el resumen de la página.

Para quien construye un sistema, el método directo necesita saber, para cada movimiento de caja, de qué tipo de operación vino; el indirecto se puede armar con los saldos del balance y el resultado. Es una inferencia sobre el diseño: si los asientos de caja no llevan esa clasificación, el directo hay que reconstruirlo a mano.
