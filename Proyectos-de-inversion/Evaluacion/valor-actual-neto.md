---
resumen: >-
  El valor actual neto (VAN) de una inversión es la suma de todos sus flujos de fondos, cada uno traído a hoy con la tasa de corte: si da positivo, la inversión deja más de lo que cuesta la plata que usa y se acepta; si da negativo, se rechaza. Es el criterio que recomiendan los libros, porque mide en plata el valor que agrega.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance (2022), 16.2 Net Present Value (NPV) Method (leído por extractor): https://openstax.org/books/principles-finance/pages/16-2-net-present-value-npv-method"
  - "OpenStax, Principles of Finance (2022), 16.4 Alternative Methods (leído por extractor): https://openstax.org/books/principles-finance/pages/16-4-alternative-methods"
  - "OpenStax, Principles of Finance (2022), 16.5 Choosing between Projects (leído por extractor): https://openstax.org/books/principles-finance/pages/16-5-choosing-between-projects"
  - "OpenStax, Principles of Finance (2022), 16.6 Using Excel to Make Company Investment Decisions (leído por extractor): https://openstax.org/books/principles-finance/pages/16-6-using-excel-to-make-company-investment-decisions"
  - "Proyectos-de-inversion/.investigacion/evaluacion.md (2026-11-27), componente 2"
aliases: [VAN, valor actual neto, valor presente neto, VPN, net present value, NPV, perfil del VAN, NPV profile, índice de rentabilidad, profitability index, PI, anualidad equivalente, equivalent annuity, cadena de reemplazo, replacement chain]
creado: 2026-11-27
revisado:
---

# Valor actual neto

El valor actual neto (VAN) de una inversión es la suma de todos sus flujos de fondos, cada uno traído a hoy con la tasa de corte: si da positivo, la inversión deja más de lo que cuesta la plata que usa y se acepta; si da negativo, se rechaza. Es el criterio que recomiendan los libros, porque mide en plata el valor que agrega.

Lee el [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md) con una [tasa de corte](tasa-de-corte.md). Sus dos compañeros en la [evaluación](evaluacion-de-la-inversion.md) son la [tasa interna de retorno](tasa-interna-de-retorno.md), que busca la tasa con la que el VAN da cero, y el [periodo de repago](periodo-de-repago.md), que no descuenta.

## Traer cada flujo a hoy y sumar

Un peso dentro de tres años vale menos que un peso hoy, porque el de hoy se puede poner a rendir. Descontar es hacer la cuenta al revés: un flujo F del año t vale hoy F / (1 + r)^t, con r la tasa de corte. OpenStax define el VAN como «the difference between the present value of the cash inflows and the present value of cash outflows», y la regla: «If the cash inflows exceed the cash outflows in present value terms, the project will add value and should be accepted».

Con la máquina de bordar del ejemplo de OpenStax (16.000 dólares de inversión, 2.000 y 4.000 los dos primeros años, 5.000 en cada uno de los cuatro siguientes, al 9 %):

| Año | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Flujo | −16.000 | 2.000 | 4.000 | 5.000 | 5.000 | 5.000 | 5.000 |
| Valor actual al 9 % | −16.000 | 1.834,86 | 3.366,72 | 3.860,92 | 3.542,13 | 3.249,66 | 2.981,34 |

Los valores actuales de las entradas suman 18.835,63; menos los 16.000 de la inversión, el VAN es 2.835,63. OpenStax concluye: «Because the NPV is positive, Sam's Sporting Goods should purchase the embroidery machine». Las cuentas se rehicieron y cierran, con diferencias de un centavo por redondeo.

El VAN positivo no es la ganancia de la máquina. Es lo que deja por encima de lo que la plata habría rendido en otro uso al 9 %: después de devolver la inversión y ese rendimiento, quedan 2.835,63 de hoy.

## Qué tasa y cuánto importa

OpenStax dice que se debería usar «the firm's cost to attract capital» y reconoce que es difícil de estimar. Por eso propone, en su sección 16.6, el perfil del VAN: calcular el VAN con varias tasas y ver dónde cruza el cero. La empresa puede usarlo «to see how sensitive their decisions are to changes in financing costs». Qué tasa poner y por qué las empresas usan tasas más altas que su costo de capital está en [tasa de corte](tasa-de-corte.md); el perfil y las otras pruebas, en [análisis de sensibilidad](analisis-de-sensibilidad.md).

## El índice de rentabilidad

El índice de rentabilidad divide el valor actual de las entradas por el de las salidas. Para la máquina de bordar, 18.836 / 16.000 = 1,18. Si es mayor que 1, el VAN es positivo: los dos criterios aceptan y rechazan lo mismo. Sirve para otra cosa, ordenar proyectos cuando la plata no alcanza para todos, que es el caso del [presupuesto de capital](../Aprobacion/presupuesto-de-capital.md#cuando-la-plata-no-alcanza).

## Elegir entre alternativas

Cuando dos proyectos son excluyentes (comprar una máquina o la otra, no las dos), OpenStax da la regla: «take the project with the highest NPV». En su caso, la máquina de bordar común cuesta 16.000, tiene VAN de 2.835,62 y tasa interna de retorno de 14,10 %; una de uso intensivo cuesta 25.000, tiene VAN de 3.970,67 y tasa interna de 13,20 %. Se elige la de uso intensivo, aunque su tasa interna sea menor, porque agrega más valor. Por qué la tasa interna engaña acá está en [tasa interna de retorno](tasa-interna-de-retorno.md#cuándo-la-tir-elige-mal).

Si las alternativas duran distinto, comparar sus VAN no alcanza: la que dura más suma más años. OpenStax compara dos camiones de 50.000 dólares al 10 %: uno usado que dura 3 años y deja 40.000 por año (VAN 49.474) y uno nuevo que dura 6 y deja 30.000 (VAN 80.658). Hay dos maneras de emparejarlos:

- **Cadena de reemplazo**: repetir el corto hasta igualar la duración del largo. Dos camiones usados seguidos dan un VAN de 86.644,69, más que el nuevo.
- **Anualidad equivalente**: convertir cada VAN en una cuota anual. El usado da 19.894 por año y el nuevo 18.520.

Por los dos caminos gana el camión usado. Los dos suponen que al terminar el corto habrá otro igual, y OpenStax advierte que «this is not always a reasonable assumption». La anualidad equivalente es la misma herramienta que usa el mantenimiento para decidir si [reparar o reemplazar](../../Activos-y-mantenimiento/Desempeno-de-los-activos/reparar-o-reemplazar.md#el-costo-anual-equivalente) un equipo, con costos en lugar de ingresos.

## Cómo falla

- **Un VAN es tan bueno como su flujo.** Un error en el [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md) pasa entero al VAN; la precisión de los decimales no lo arregla.
- **Es difícil de explicar.** OpenStax lo admite: «The NPV method can be difficult for someone without a finance background to understand». Por eso se presenta junto con el repago y la tasa interna, que se entienden más rápido.
- **No ordena bien con plata limitada.** Ordenar proyectos de mayor a menor VAN puede dejar afuera combinaciones que suman más. Está en [presupuesto de capital](../Aprobacion/presupuesto-de-capital.md#cuando-la-plata-no-alcanza).
- **No ve la flexibilidad.** Un VAN calculado una vez supone que la empresa no va a reaccionar si las cosas salen mal o bien. El valor de poder esperar, ampliar o abandonar está en [análisis de sensibilidad](analisis-de-sensibilidad.md#lo-que-el-van-no-ve-poder-esperar-ampliar-o-abandonar).
