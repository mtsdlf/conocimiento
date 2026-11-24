---
resumen: >-
  El plan financiero mínimo es una planilla de caja de doce meses, mes por mes: cuánta plata hay, cuánta entra, cuánta sale y con cuánto se termina cada mes. Sirve para saber cuántos meses se puede probar con la plata que hay y en qué mes habría que actuar, y vale lo que valen sus supuestos.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance 2e, 19.6 Using Excel to Create the Short-Term Plan (libro de texto abierto; leído vía resumen con citas): https://openstax.org/books/principles-finance-2e/pages/19-6-using-excel-to-create-the-short-term-plan"
  - "Duquesne University SBDC, Dollars and Sense (guía; leída en parte, hasta el ejemplo estacional): https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf"
  - "Ehmke y Miller, Estimating Breakeven Sales for Your Small Business, Purdue Extension EC-725 (págs. 1 a 3 leídas): https://www.extension.purdue.edu/extmedia/EC/EC-725.pdf"
  - "Dalton Caldwell, Advice for Companies With Less Than 1 Year of Runway, Y Combinator (2015-01-22): https://www.ycombinator.com/blog/advice-startups-running-out-of-money"
  - "JPMorgan Chase Institute, Cash is King: Flows, Balances, and Buffer Days (2016-09; página de resumen leída): https://www.jpmorganchase.com/institute/all-topics/business-growth-and-entrepreneurship/report-cash-flows-balances-and-buffer-days"
  - "SCORE, How much cash should a small business keep in reserve? (según el buscador): https://www.score.org/blog/how-much-cash-should-small-business-keep-reserve"
  - "SCORE, plantilla 12 Month Cash Flow Statement (no abierta): https://www.score.org/resource/template/12-month-cash-flow-statement"
  - "ACCA, Inflation and investment appraisal (material de examen de Financial Management): https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/inflation-investment-appraisal.html"
  - "Forbes Argentina (2022-08-23), cómo las pymes pueden mantener el flujo de caja en época de inflación: https://www.forbesargentina.com/money/como-pymes-pueden-mantener-flujo-caja-epoca-inflacion-n21013"
  - "Cassar (2010), Are Individuals Entering Self-Employment Overly Optimistic?, Strategic Management Journal 31(8): 822-840 (según el abstract, visto por el buscador): https://econpapers.repec.org/RePEc:bla:stratm:v:31:y:2010:i:8:p:822-840"
  - "Lange, Mollov, Pearlmutter, Singh y Bygrave (2007), Pre-start-up formal business plans and post-start-up performance, Venture Capital 9(4): 237-256 (abstract): https://ideas.repec.org/a/taf/veecee/v9y2007i4p237-256.html"
  - "Hopp, Greene, Honig, Karlsson y Samuelsson (2018), réplica de Honig y Karlsson (2004), Management Review Quarterly 68(4) (abstract): https://ideas.repec.org/a/spr/manrev/v68y2018i4d10.1007_s11301-018-0143-9.html"
  - "Emprender/.investigacion/plan-financiero-minimo.md"
  - "Emprender/.investigacion/plata-de-un-servicio-contraria.md"
aliases: [flujo de caja proyectado, presupuesto de caja, cash flow forecast, cash budget, proyección de caja, planilla de caja, plan financiero]
creado: 2026-11-24
revisado:
---

# Plan financiero mínimo

El plan financiero mínimo es una planilla de caja de doce meses, mes por mes: cuánta plata hay, cuánta entra, cuánta sale y con cuánto se termina cada mes. Sirve para saber cuántos meses se puede probar con la plata que hay y en qué mes habría que actuar, y vale lo que valen sus supuestos.

Es la herramienta que pone en números lo que explica [Finanzas](finanzas.md): la diferencia entre caja y resultado, el consumo mensual, la pista, *default alive* y el punto de equilibrio. Acá no se redefinen; se ve cómo se leen en la planilla. Los ingresos salen del [modelo de negocio](../Modelo-de-negocio/modelo-de-negocio.md), y en un servicio no pueden pasar lo que el equipo puede entregar, que es la [capacidad de un equipo de servicio](../Modelo-de-negocio/capacidad-de-un-equipo-de-servicio.md).

## Las filas de la planilla

Una proyección de caja encadena los meses: la caja con que termina uno es la caja con que empieza el siguiente. El libro de texto de OpenStax arma el presupuesto de caja con saldo inicial, cobranzas, desembolsos, flujo neto, saldo final y un saldo mínimo que fija la dirección: «The formula for net cash flow is cash collections less cash disbursements». Para una empresa chica de servicios, las filas son estas:

| Fila | Qué va | Cuidado |
|---|---|---|
| Caja al empezar el mes | Lo que hay en la cuenta | El primer mes, la plata real disponible |
| Cobros de abonos | Clientes activos por precio mensual | Lo cobrado, no lo facturado |
| Cobros de proyectos | Adelantos y cuotas según los hitos | Cada cuota en el mes en que se cobra |
| Pagos fijos | Herramientas, servicios, contador, alquiler | Los anuales, en el mes en que se pagan |
| Retiros de los socios | Lo que cada socio necesita para vivir | Siempre, aunque la empresa no gane |
| Impuestos | Lo que se paga sobre lo que se factura o se gana | Con su calendario de vencimientos |
| Flujo neto | Cobros menos pagos | |
| Caja al terminar el mes | Caja al empezar más flujo neto | Pasa al mes siguiente |

Facturar no es cobrar. OpenStax lo dice así: «projected monthly sales amounts are not equal to cash collected from sales». La guía del centro de pequeñas empresas de Duquesne pide que la planilla refleje el ciclo de cobro real, «cash coming in over 30 to 90+ days», y que incluya siempre el retiro propio: «Always include your own draw or salary». Las filas de retiros e impuestos como filas propias son una adaptación de esta base. Qué impuestos van y cuándo vencen depende del régimen, que está en [normativa para empezar en Argentina](../Legal-e-impuestos/normativa-para-empezar-en-argentina.md).

## Los ingresos, de abajo hacia arriba

Los ingresos se proyectan contando clientes y multiplicando por el precio, no suponiendo un porcentaje de crecimiento. La guía de Duquesne lo ejemplifica para un servicio: 30 clientes por mes por US$ 65 da US$ 1950, y advierte que «The number of successful clients is the variable number that needs to be justified». Cada supuesto va escrito al lado de la planilla, con de dónde sale.

Para un abono, la cuenta de clientes de cada mes es: los del mes anterior, más las altas, menos las bajas. Esa cuenta aparece en guías de practicantes, no en un libro de texto ni en una guía oficial. Las altas no pueden pasar lo que se puede vender y atender, y las bajas se miden como explica [retención y churn](../../Datos/Retencion-y-churn/retencion-y-churn.md). Para los proyectos, cada uno entra con su calendario de cobro: adelanto, hitos y saldo, como en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#formas-de-repartir-el-riesgo).

## Un ejemplo de doce meses

Los números son inventados para mostrar cómo se lee la planilla; no son referencias. Supuestos:

- Caja inicial de 6000. Pagos fijos de 300 por mes y retiros de los socios de 1600.
- Impuestos del 10 % de lo cobrado. Es un supuesto redondo para el ejemplo, no una tasa real.
- Desde el mes 2 entran 2 abonos por mes, de 120 cada uno, y se da de baja 1 cada tres meses.
- Siete proyectos en el año, de 1600 cada uno, cobrados mitad al vender y mitad al mes siguiente.

| Mes | Abonos activos | Cobro abonos | Cobro proyectos | Pagos | Flujo neto | Caja al terminar |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 1900 | −1900 | 4100 |
| 2 | 2 | 240 | 800 | 2004 | −964 | 3136 |
| 3 | 3 | 360 | 800 | 2016 | −856 | 2280 |
| 4 | 5 | 600 | 800 | 2040 | −640 | 1640 |
| 5 | 7 | 840 | 800 | 2064 | −424 | 1216 |
| 6 | 8 | 960 | 800 | 2076 | −316 | 900 |
| 7 | 10 | 1200 | 1600 | 2180 | 620 | 1520 |
| 8 | 12 | 1440 | 800 | 2124 | 116 | 1636 |
| 9 | 13 | 1560 | 800 | 2136 | 224 | 1860 |
| 10 | 15 | 1800 | 800 | 2160 | 440 | 2300 |
| 11 | 17 | 2040 | 800 | 2184 | 656 | 2956 |
| 12 | 18 | 2160 | 1600 | 2276 | 1484 | 4440 |

Leída de arriba abajo, la planilla dice tres cosas. El peor mes es el 6, con 900 de caja, menos de la mitad de lo que sale en un mes. El flujo neto se vuelve positivo en el mes 7, cuando los abonos acumulados más un proyecto cubren los pagos: ahí la empresa está, con estos supuestos, *default alive*. Y la plata no se acaba en el año, pero el margen en el mes 6 es chico.

El escenario pesimista cambia un solo supuesto: entra 1 abono por mes en lugar de 2. Con todo lo demás igual, la caja se vuelve negativa en el mes 6 y no se recupera en el año. La diferencia entre los dos escenarios dice cuál es el supuesto que hay que probar primero: el ritmo de altas.

## Cómo se lee la pista en la planilla

La pista es el mes en que la caja al terminar cruza el mínimo que se fijó, no una división. La fórmula de Finanzas (caja dividida por consumo mensual) supone un consumo constante. En una planilla con ingresos que crecen, el consumo cambia cada mes y la pista se lee directamente: es la fila de caja al terminar mirada contra el saldo mínimo, que es lo que hace OpenStax con su fila de déficit. Es lectura de esta base sobre la mecánica del libro.

Y Combinator da umbrales para actuar, pensados para startups que levantaron capital: con menos de tres meses de caja hay que enfrentar las deudas y la posibilidad de cerrar, y «<2 months is the point of no return» (Caldwell, 2015). Su consejo es no esperar: «Delaying taking action to reduce burn is a bad strategy». Según Caldwell, en el consumo pesan sobre todo los sueldos. En una empresa sin empleados, eso son los retiros de los socios.

El punto de equilibrio también se lee en la planilla: es el mes en que el flujo neto pasa a ser positivo. La guía de Duquesne lo calcula para un servicio sumando el sueldo propio a los gastos. Con US$ 3000 de ingreso personal y un margen del 55 %, las ventas de equilibrio suben de US$ 9091 a US$ 14.545. Purdue suma el margen de seguridad, que es cuánto se puede vender por debajo de lo esperado antes de perder: si es chico, «may put the business's ability to cash flow at risk». Las dos guías calculan el equilibrio contable de un mes típico, no el de caja con los desfases de cobro; la planilla da el segundo.

## Cuánta caja mínima tener

No hay una cifra con respaldo de cuántos meses de gastos tener de colchón. Las que circulan no coinciden y no traen evidencia:

| Fuente | Qué dice | Cómo se vio |
|---|---|---|
| SCORE | De tres a seis meses de gastos, y que usar la regla para todo negocio «is misleading» | Solo por el buscador |
| SBDC de Wyoming | Un piso de dos meses de gastos operativos | Solo por el buscador |
| Wells Fargo | De nueve a doce meses si el negocio es estacional | Solo por el buscador; contenido comercial de un banco |

Lo que sí está medido es cuánto tienen las empresas chicas. En 600.000 pymes de Estados Unidos, el JPMorgan Chase Institute encontró que «The median small business holds 27 cash buffer days in reserve» y que la mitad tiene menos de un mes. Describe lo que hay, no lo que conviene. La lectura de esta base es fijar el saldo mínimo de la planilla en meses de pagos fijos más retiros, y elegir el número mirando cuánto se tarda en cobrar un proyecto.

## Inflación y moneda

La regla que sostienen los textos de finanzas es de coherencia: toda la planilla en una sola unidad. ACCA lo explica para valuar proyectos: los flujos nominales («current price terms cash flows that have been inflated into future values») van con tasas nominales, y los reales, con tasas reales. Las partidas no suben todas igual: precios, costos variables y costos fijos tienen su propia inflación, y «if a real terms approach is adopted, the specific inflation rates cannot be ignored». Trasladado a la planilla, que es lectura de esta base, cada fila se actualiza con su propio índice y no con uno general.

La lectura de esta base es que, con inflación, el plazo de cobro es un costo. La única recomendación práctica que se encontró para Argentina es de prensa y viene de un proveedor de software contable (Forbes Argentina, 2022): que los días que se tarda en cobrar sean menos que los días que se tarda en pagar, y armar escenarios. Si conviene proyectar en pesos o en dólares, y cómo actualizar el precio de un abono, no tiene una fuente seria; lo que se sabe de cómo se cobra un abono está en [abono de cuidado](../Modelo-de-negocio/abono-de-cuidado.md#cómo-se-cobra).

> [!NOTE]
> Sin fuente todavía: una guía seria para proyectar caja de una pyme argentina con inflación (precios en dólares o en pesos, actualización del abono, plazos de cobro). Los trabajos de universidades argentinas que aparecieron (UNCOMA, UCCOR) no se pudieron abrir, y la normativa contable (FACPCE, RT 6), vista solo por el buscador, parece tratar los estados históricos y no las proyecciones.

## Para qué sirve y cómo falla

Que escribir un plan ayude a una empresa que empieza está en discusión, y la evidencia está en [escuelas de emprender](../Fundamentos/escuelas-de-emprender.md). Lo que suma para este caso: Lange y otros (2007), con 116 empresas de egresados de Babson, no encontraron diferencia de desempeño entre las que arrancaron con un plan escrito y las que no, y concluyen que solo vale un plan detallado si hay que levantar capital (según el abstract). Una réplica de 2018 sobre otro estudio encontró que el plan formal afecta la supervivencia pero no la rentabilidad. Ningún estudio evalúa la planilla de caja sola, que es mucho menos que un plan de negocios.

La planilla falla de maneras conocidas:

- Optimismo. Cassar (2010) encontró que preparar estados financieros proyectados vuelve más optimistas los pronósticos de ventas (según el abstract, visto por el buscador). Duquesne aconseja «when in doubt use worse-case projections».
- Cobrar en el mes en que se factura. Es confundir resultado con caja, el error que la planilla existe para evitar.
- Olvidar los retiros o los impuestos. La empresa parece viva porque los socios no están cobrando.
- Más ingresos de los que el equipo puede atender. En un servicio, las altas tienen un techo de [capacidad](../Modelo-de-negocio/capacidad-de-un-equipo-de-servicio.md).
- Hacerla una vez. La planilla sirve si cada mes se reemplaza lo proyectado por lo real y se mira qué supuesto falló.

Una cifra que circula y no se usa acá: que el 82 % de las pequeñas empresas quiebra por problemas de caja. No se encontró el estudio original, y SCORE, según el buscador, dice que la caja es «a symptom» de otras causas.

Para armar la planilla, la sección 19.6 de *Principles of Finance* de OpenStax, que es libre, tiene la mecánica fila por fila. La guía «Dollars and Sense» de Duquesne la baja a un negocio chico, con un ejemplo de servicios. SCORE y la British Business Bank publican plantillas de doce meses que no se pudieron abrir: conviene bajarlas y comparar sus filas con la tabla de arriba antes de usarlas.
