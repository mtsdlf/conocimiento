---
resumen: >-
  El devengado es la base contable que registra ingresos y gastos en el período en que ocurren, aunque se cobren o se paguen en otro; por eso el resultado de un período y la caja que entró en ese período son dos números distintos.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, Conceptual Framework for Financial Reporting (2018), párrs. 1.17 a 1.21: https://moodle2.units.it/pluginfile.php/493397/mod_resource/content/1/conceptual-framework-for-financial-reporting.pdf"
  - "IASB, NIC 1 Presentación de estados financieros, párrs. 27 y 28 (versión previa a la NIIF 18): https://moodle2.units.it/pluginfile.php/493402/mod_resource/content/1/ias-1-presentation-of-financial-statements.pdf"
  - "OpenStax, Principles of Financial Accounting (2019), 4.1 Explain the Concepts and Guidelines Affecting Adjusting Entries: https://openstax.org/books/principles-financial-accounting/pages/4-1-explain-the-concepts-and-guidelines-affecting-adjusting-entries"
  - "OpenStax, Principles of Financial Accounting (2019), 4.3 Record and Post the Common Types of Adjusting Entries: https://openstax.org/books/principles-financial-accounting/pages/4-3-record-and-post-the-common-types-of-adjusting-entries"
  - "OpenStax, Principles of Financial Accounting (2019), 3.5 Use Journal Entries to Record Transactions: https://openstax.org/books/principles-financial-accounting/pages/3-5-use-journal-entries-to-record-transactions-and-post-to-t-accounts"
  - "AccountingTools, How a profitable business can run out of cash: https://www.accountingtools.com/articles/how-a-profitable-business-can-run-out-of-cash"
  - "Curso de finanzas y contabilidad en lynda.com, Accrual accounting (según el buscador): https://www.lynda.com/Finance-Accounting-tutorials/Accrual-accounting/565365/637007-4.html"
  - "AccountingCoach, Net cash flow vs net income (según el buscador): https://www.accountingcoach.com/blog/net-cash-flow-net-income"
  - "Contabilidad/.investigacion/registro-y-fundamentos.md (2026-11-27)"
  - "Contabilidad/.investigacion/posicion-contraria.md (2026-11-27)"
aliases: [devengado, base de devengado, devengamiento, principio de lo devengado, accrual, accrual basis, accrual accounting, base caja, base de caja, percibido, cash basis, caja y resultado, ganancia y caja, matching, correlación de ingresos y gastos]
creado: 2026-11-27
revisado:
---

# Devengado

El devengado es la base contable que registra ingresos y gastos en el período en que ocurren, aunque se cobren o se paguen en otro; por eso el resultado de un período y la caja que entró en ese período son dos números distintos.

Es la idea que ordena todo el tema de [Contabilidad](../contabilidad.md). Explica por qué existen las cuentas a cobrar y a pagar, los [ajustes de cierre](../Estados-contables/ajustes-de-cierre.md) y un [estado de flujo de efectivo](../Estados-contables/estado-de-flujo-de-efectivo.md) separado del [estado de resultados](../Estados-contables/estado-de-resultados.md).

## Devengado y caja, las dos bases

Según OpenStax, la base de devengado exige registrar ingresos y gastos en el período contable en que se ganaron o se incurrieron. La base caja, en cambio, no registra una operación hasta que hay un intercambio de efectivo. Los principios de reconocimiento de ingresos y de correlación de gastos con ingresos (matching) salen del devengado.

El Marco Conceptual del IASB lo define así (1.17): «Accrual accounting depicts the effects of transactions and other events and circumstances on a reporting entity's economic resources and claims in the periods in which those effects occur, even if the resulting cash receipts and payments occur in a different period.» Y da la razón: esa información «provides a better basis for assessing the entity's past and future performance than information solely about cash receipts and payments during that period».

La NIC 1 lo vuelve obligatorio para los estados contables, con una excepción: «An entity shall prepare its financial statements, except for cash flow information, using the accrual basis of accounting» (párrafo 27). La NIIF 18 reemplaza a la NIC 1 desde el 1 de enero de 2027; el párrafo citado es de la versión anterior. Qué normas rigen en cada lugar está en [normas contables](../Estados-contables/normas-contables.md).

## La caja no desaparece

El mismo Marco Conceptual (1.20) dice que la información sobre flujos de caja también sirve: para evaluar la capacidad de la empresa de generar flujos netos, su liquidez y su solvencia. El resultado devengado mide el desempeño; la caja mide si la empresa puede pagar lo que vence. La excepción de la NIC 1 sigue esa lógica (lectura de la base): el estado de flujo de efectivo se arma sobre base caja y los demás sobre devengado.

## Un ingreso sin plata y una plata sin ingreso

Los asientos de enero de Printing Plus, el ejemplo de OpenStax, muestran las dos direcciones (cifras en dólares, cuentas traducidas):

| Fecha | Cuenta | Debe | Haber |
|---|---|---|---|
| 9 de enero | Caja | 4.000 | |
| | Ingresos cobrados por adelantado | | 4.000 |
| 10 de enero | Deudores por ventas | 5.500 | |
| | Ingresos por servicios | | 5.500 |

El 9 de enero entra plata y no hay ingreso: el cliente pagó un trabajo que todavía no se hizo, y la empresa le debe ese trabajo (un pasivo). El 10 de enero hay un ingreso de 5.500 y la caja no se mueve: el servicio se prestó y se facturó, y la plata llega con el cobro posterior. En base caja, el 9 habría un ingreso de 4.000 y el 10 nada.

## Los ajustes que llevan el devengado al cierre

Durante el mes se registran los hechos con comprobante. Al cierre faltan los que ocurrieron sin que nadie emitiera un papel: el material que se gastó, el equipo que se desgastó, los sueldos trabajados y no pagados. Los asientos de ajuste los agregan. Según OpenStax, cada ajuste toca una cuenta de resultado y una patrimonial, y nunca la caja.

Los ajustes de Printing Plus al 31 de enero de 2019:

| Qué se ajusta | Debe | Haber | Importe |
|---|---|---|---|
| Materiales usados en el mes | Gasto de materiales | Materiales | 100 |
| Amortización del equipo comprado el 5 de enero | Amortización de equipos | Amortización acumulada de equipos | 75 |
| Parte ganada del adelanto del 9 de enero | Ingresos cobrados por adelantado | Ingresos por servicios | 600 |
| Intereses ganados y no cobrados | Intereses a cobrar | Intereses ganados | 140 |
| Sueldos del 21 al 31 de enero, no pagados | Sueldos | Sueldos a pagar | 1.500 |

Después de los ajustes, Materiales baja de 500 a 400 y el pasivo por el adelanto baja de 4.000 a 3.400. Ninguna de las cinco líneas mueve la caja, y todas cambian el resultado del mes. El detalle de cada tipo de ajuste y el cierre de las cuentas de resultado están en [ajustes de cierre](../Estados-contables/ajustes-de-cierre.md).

## Por qué una empresa con ganancia se queda sin plata

Si el resultado y la caja se separan en cada venta, también se separan en el total. AccountingTools lista las causas habituales de que una empresa rentable se quede sin efectivo:

- el ingreso se registra mucho antes de cobrarlo;
- las inversiones grandes en activos fijos salen de la caja de una vez y pasan al resultado de a poco, con la amortización;
- el inventario inmoviliza plata que todavía no es costo;
- los clientes pagan a plazo largo mientras los proveedores exigen pago rápido;
- sueldos, cargas sociales, alquileres y seguros vencen antes de cobrar.

En todas, el devengado mueve el resultado en un momento y la caja en otro. Una empresa que crece vendiendo a plazo agranda sus cuentas a cobrar más rápido de lo que cobra, y puede mostrar ganancia mientras se le acaba la plata (inferencia de la base a partir de la lista).

> [!NOTE]
> Sin fuente todavía: un caso con cifras de una empresa con ganancia y sin caja, de un libro de texto o un caso documentado. La lista de causas tiene una sola fuente secundaria, sin números; el ejemplo de Printing Plus muestra el mecanismo, pero el libro no lo plantea como un caso de falta de caja.

## El mito de que la ganancia es caja

Quien no es contador suele leer la ganancia del estado de resultados como la plata que la empresa tiene o generó. Según un curso de finanzas y contabilidad citado por el buscador, los estudiantes confunden el resultado neto con el flujo de efectivo operativo, que rara vez son el mismo número. AccountingCoach lo muestra con una venta de diciembre, que sube la ganancia de diciembre y la caja de enero (según el buscador).

La respuesta corta para quien pregunta «si gané, ¿dónde está la plata?» está en la diferencia entre los dos estados: el [estado de flujo de efectivo](../Estados-contables/estado-de-flujo-de-efectivo.md) parte del resultado y le suma y resta lo que se devengó sin moverse la caja.

## A quién le toca cada pregunta

Para una empresa que empieza, la pregunta que decide si sigue viva es la de caja: cuántos meses le dura la plata (criterio de la base, no de las fuentes de esta nota). Esa pregunta, con la pista y el consumo mensual, vive en [Finanzas de Emprender](../../Emprender/Finanzas/finanzas.md), que usa la distinción entre caja y resultado y la tiene explicada acá. Cobrar, pagar y cuidar la posición de caja de una empresa en marcha va al tema Tesorería y finanzas de la empresa en marcha, todavía no escrito.

Para quien construye un sistema, el devengado pide registrar la factura y el cobro como dos hechos con fechas propias, y poder emitir los dos informes desde el mismo registro (inferencia de la base). Cómo se registra una venta a plazo de punta a punta está en [ingresos y cuentas a cobrar](../Operaciones/ingresos-y-cuentas-a-cobrar.md).

Para leer más: el Marco Conceptual, párrafos 1.17 a 1.21 (cinco párrafos), y OpenStax 4.1 y 4.3. Conviene fijarse en que el 1.17 dice por qué el devengado es mejor base para medir desempeño y en que el 1.20 suma la caja como complemento.
