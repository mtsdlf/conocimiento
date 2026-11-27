---
resumen: >-
  La proyección de caja es el pronóstico de cuánta plata va a entrar y salir en las próximas semanas, cobro por cobro y pago por pago, para ver con tiempo en qué semana falta o sobra.
estado: borrador
estabilidad: semi
fuentes:
  - "OpenStax, Principles of Finance (2022), 19.6 Using Excel to Create the Short-Term Plan (leído): https://openstax.org/books/principles-finance/pages/19-6-using-excel-to-create-the-short-term-plan"
  - "APQC, Process Classification Framework 7.4 (2024), 9.7.2.4 Develop cash flow forecasts (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Wikipedia, Cash flow forecasting, que cita a de Caux (2005), Bort (1990) y AFP (2006) (según su resumen): https://en.wikipedia.org/wiki/Cash_flow_forecasting"
  - "Upflow, 13-Week Cash Flow Forecast (blog de un proveedor de software de cobranzas; según su resumen, como evidencia de práctica): https://upflow.io/blog/cfo-reads/13-week-cash-flow-forecast"
  - "Stampli, What is a 13-week cash flow forecast (proveedor de software; según su resumen, como evidencia de práctica): https://www.stampli.com/resources/13-week-cash-flow-forecast/"
  - "Tesoreria/.investigacion/caja-y-liquidez.md, sección 3 (2026-11-27)"
  - "Tesoreria/.investigacion/caja-y-cobranzas-segunda-ronda.md, sección 1 (2026-11-27)"
  - "Tesoreria/.investigacion/fundamentos-y-contraria.md, sección 4.2 (2026-11-27)"
aliases: [proyección de caja, pronóstico de caja, flujo de fondos proyectado, presupuesto de caja, cash flow forecast, cash forecast, cash budget, 13-week cash flow forecast, pronóstico de 13 semanas, rolling forecast, proyección móvil]
creado: 2026-11-27
revisado:
---

# Proyección de caja

La proyección de caja es el pronóstico de cuánta plata va a entrar y salir en las próximas semanas, cobro por cobro y pago por pago, para ver con tiempo en qué semana falta o sobra.

Es la segunda pregunta de [Caja y liquidez](caja-y-liquidez.md): la [posición de caja](posicion-de-caja.md) dice cuánta plata hay hoy y la proyección parte de ese número. APQC la tiene como subproceso propio, 9.7.2.4, «Develop cash flow forecasts». Se diferencia de dos vecinos. El [plan financiero mínimo de Emprender](../../Emprender/Finanzas/plan-financiero-minimo.md) es mensual, a doce meses, y sirve para ver la pista de una empresa que empieza. El [presupuesto](../../Contabilidad/Contabilidad-de-gestion/presupuesto.md) de la contabilidad de gestión planea ingresos y gastos devengados. La proyección de caja es semanal, de corto plazo y solo mira plata.

## Las filas de un presupuesto de caja

OpenStax llama al presupuesto de caja un «forward-looking document» y lo arma con estas filas, período por período:

1. Saldo inicial de caja.
2. Más los cobros.
3. Menos los pagos.
4. Igual al flujo neto, y saldo final preliminar.
5. Menos el saldo mínimo, que es «a target cash balance that management sets».
6. Igual al superávit o déficit del período.

El saldo final de un período es el inicial del siguiente. Del déficit, el libro dice: «A cash deficiency means that some type of financing, such as a line of credit or bank loan, will be needed.» Ese déficit es lo que lleva la pregunta a [Financiamiento](../Financiamiento/financiamiento.md); el superávit, a la [colocación de excedentes](colocacion-de-excedentes.md).

El período lo elige quien lo arma: el presupuesto «could be prepared using any useful time elements: weekly, monthly, or quarterly». El ejemplo del libro es mensual a doce meses.

## Método directo y método indirecto

Hay dos formas de llegar a los cobros y pagos futuros. Según el resumen de un artículo de referencia que cita a la AFP, el método directo programa los cobros y pagos reales, uno por uno: los cobros salen sobre todo de las cuentas a cobrar, y los pagos incluyen sueldos, proveedores, dividendos e intereses. Ese artículo lo presenta como el más adecuado para un horizonte corto, de unos 30 días, porque trabaja con datos reales y no proyectados.

Los métodos indirectos parten de un estado de resultados y un balance proyectados y los convierten en caja. Según el mismo resumen, sirven para el mediano y el largo plazo, con períodos mensuales o trimestrales. La misma distinción existe en el [estado de flujo de efectivo](../../Contabilidad/Estados-contables/estado-de-flujo-de-efectivo.md), que mira para atrás; la proyección de corto plazo usa el directo.

## Por qué trece semanas

La proyección de 13 semanas es la forma de la proyección de corto plazo que describen dos proveedores de software, igual los dos, que cuentan como una sola línea de práctica comercial. Según sus resúmenes, trece semanas son un trimestre: es un plazo en el que la mayoría de los datos ya se conocen (facturas emitidas, sueldos programados) y que a la vez deja tiempo para conseguir financiamiento o recortar gastos antes del pozo.

> [!NOTE] Una sola fuente, y comercial: que el formato de 13 semanas nació en las reestructuraciones de empresas en crisis, donde prestamistas y tribunales pedían ver la liquidez semana por semana. Falta una fuente primaria sobre su origen.

La forma, según esas fuentes: una columna por semana y filas de caja inicial, cobros por origen (cuentas a cobrar abiertas, facturación futura, otros), sueldos, proveedores, obligaciones fijas, partidas únicas, flujo neto y caja final, comparada con un mínimo o con lo que exige un préstamo. Es siempre de método directo, sin ajustes de devengado.

## De dónde sale cada fila

Por lectura de esta base, cada fila de la proyección sale de un registro distinto, y el registro dice qué tan firme es:

- Cobros de facturas emitidas: de la [antigüedad de saldos](../../Contabilidad/Registro/cuentas-corrientes.md) de los clientes, corrida por lo que cada cliente suele tardar después del vencimiento. Cómo se mide ese atraso está en [gestión de la cobranza](../Credito-y-cobranzas/gestion-de-la-cobranza.md).
- Cobros de lo que todavía no se facturó: de los [pedidos de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) abiertos y, más lejos, de una estimación de ventas.
- Pagos a proveedores: de las facturas aprobadas y su [programación de pagos](../Pagos-a-proveedores/programacion-de-pagos.md).
- Sueldos y cargas: del calendario de liquidación, que es del tema Administración de personal y nómina, todavía no escrito.
- Impuestos: de los vencimientos, que son del tema Impuestos, todavía no escrito; acá pesan solo como salida de caja.
- Deuda: de las cuotas e intereses de los [préstamos](../Financiamiento/prestamos.md).

Las primeras semanas se llenan casi solo con documentos que ya existen; las últimas, con estimaciones. Según una de las fuentes comerciales, la precisión baja con el horizonte: las semanas 1 a 4 salen casi exactas y las siguientes solo marcan la dirección.

## La proyección móvil

La proyección de 13 semanas se rehace cada semana. Según la misma fuente comercial, la semana que pasó se reemplaza por lo real y se agrega una semana 13 nueva, y conviene guardar la versión anterior, porque sin ella no se puede medir el desvío. OpenStax describe lo mismo para el presupuesto mensual: el presupuesto móvil «is continually updated to add a new budget period».

## Cómo se mide si acierta

Según el resumen del artículo de referencia, es raro que los cobros coincidan con lo proyectado, porque los clientes rara vez pagan todos en fecha. Una de las fuentes comerciales propone medir cada semana la precisión de los cobros como el valor absoluto de lo proyectado menos lo real, dividido por lo real, y seguirla en las semanas 1 a 4. Cobros y pagos se miden por separado, porque fallan por razones distintas.

Además del tamaño del error importa su sentido. Si una fila yerra siempre para el mismo lado, el supuesto está mal y no es mala suerte. Una de las fuentes propone revisar cada semana las diez mayores desviaciones de cobros, cada una con su causa (pago tardío, disputa, promesa de pago incumplida, error de facturación, cobro sin aplicar) y su responsable.

> [!NOTE] Sin fuente todavía: cuánto yerran las proyecciones de las empresas reales y qué margen de error se acepta. La propia fuente comercial dice que no hay una referencia independiente aceptada para una empresa mediana y que cada empresa fija la suya; la base no da un número.

## Cómo se diseña en un sistema

Por lectura de esta base, para quien construye la proyección en un sistema de gestión:

- Cada línea guarda su origen (la factura, el pedido, la cuota del préstamo o una estimación manual) para poder separar lo firme de lo supuesto.
- La fecha de cada cobro no es el vencimiento de la factura sino el vencimiento más el atraso habitual de ese cliente, y el usuario la puede corregir.
- Cada versión semanal se congela y se guarda, para comparar lo proyectado con lo real.
- La caja inicial sale de la posición del día, no del saldo contable.
- Las monedas se proyectan por separado.

Para una empresa chica, la misma estructura entra en una planilla; cómo armarla bien está en [Planillas de cálculo](../../Planillas-de-calculo/planillas-de-calculo.md).

## Cómo falla

Por lectura de esta base, las fallas más comunes son:

- proyectar ventas en lugar de cobros, que repite el resultado y no la caja;
- proyectar por mes cuando el pozo es de una semana;
- tomar el vencimiento como fecha de cobro, cuando los clientes pagan tarde;
- olvidar las salidas que no son a proveedores: impuestos, sueldos, cuotas, aguinaldos;
- no guardar las versiones, y no saber nunca qué supuesto falló.

Los clientes que no pagan en fecha son la fuente de error que nombra el artículo de referencia. Por eso la proyección mejora cuando mejora la [gestión de la cobranza](../Credito-y-cobranzas/gestion-de-la-cobranza.md), y por eso los datos de la [aplicación de cobros](../Credito-y-cobranzas/aplicacion-de-cobros.md) importan: un cobro sin aplicar deja la factura como pendiente y la proyección la vuelve a esperar.
