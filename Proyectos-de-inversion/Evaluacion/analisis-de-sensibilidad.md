---
resumen: >-
  El análisis de sensibilidad prueba cuánto cambia el valor actual neto de una inversión cuando cambia un supuesto (el precio, el volumen, el costo, la tasa, la vida), y cuánto tiene que fallar cada uno para que la decisión se dé vuelta. Lo acompañan los escenarios, el punto de equilibrio, la simulación y la mirada sobre lo que el VAN no cuenta: la posibilidad de esperar, ampliar o abandonar.
estado: vigente
estabilidad: estable
fuentes:
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones del cap. 5 «Measuring Returns on Investments», sensibilidad y simulación (leído): https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/invretA.pdf"
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones del cap. 6 «Estimating Side Costs and Benefits» (leído): https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/invretB.pdf"
  - "OpenStax, Principles of Finance (2022), 16.6 Using Excel to Make Company Investment Decisions, perfil del VAN (leído por extractor): https://openstax.org/books/principles-finance/pages/16-6-using-excel-to-make-company-investment-decisions"
  - "Graham (2022), Presidential Address: Corporate Finance and Reality, versión NBER w29841, Tabla I y sección de escenarios (leído en esas partes): https://nber.org/system/files/working_papers/w29841/w29841.pdf"
  - "Graham y Harvey (2002), Journal of Applied Corporate Finance 15(1) (leído): https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf"
  - "GAO, Executive Guide: Leading Practices in Capital Decision-Making, GAO/AIMD-99-32 (diciembre de 1998), lista de las doce prácticas (leído): https://www.gao.gov/assets/aimd-99-32.pdf"
  - "Jagannathan, Meier y Tarhan (2011), NBER WP 16770, sobre la opción de esperar (leído en resumen e introducción): https://www.nber.org/papers/w16770.pdf"
  - "Proyectos-de-inversion/.investigacion/evaluacion.md (2026-11-27), componente 6"
aliases: [análisis de sensibilidad, sensitivity analysis, análisis de escenarios, scenario analysis, punto de equilibrio del VAN, break-even, simulación de Monte Carlo, Monte Carlo simulation, perfil del VAN, opciones reales, real options, opción de esperar, opción de abandonar, riesgo del proyecto, project risk]
creado: 2026-11-27
revisado: 2026-11-27
---

# Análisis de sensibilidad

El análisis de sensibilidad prueba cuánto cambia el valor actual neto de una inversión cuando cambia un supuesto (el precio, el volumen, el costo, la tasa, la vida), y cuánto tiene que fallar cada uno para que la decisión se dé vuelta. Lo acompañan los escenarios, el punto de equilibrio, la simulación y la mirada sobre lo que el VAN no cuenta: la posibilidad de esperar, ampliar o abandonar.

Cierra la [evaluación](evaluacion-de-la-inversion.md). El [valor actual neto](valor-actual-neto.md) da un número con decimales, pero sale de un [flujo de fondos](flujo-de-fondos-del-proyecto.md) hecho de estimaciones. Damodaran enumera lo que puede fallar: «Revenues may be over estimated», «Actual costs may be higher than estimated costs», «Tax rates may go up», «Interest rates may rise». Esta nota trata cómo se mide ese riesgo; la prima por riesgo en la tasa está en [tasa de corte](tasa-de-corte.md).

## Mover un supuesto por vez

La sensibilidad cambia una variable, deja las demás quietas y recalcula el VAN. Con la máquina de 30 del ejemplo de [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md#una-máquina-con-cifras-supuestas), que da un VAN de −4,55 al 12 %, esta base calcula:

| Si cambia | A | El VAN da |
|---|---|---|
| Nada (caso base) | ahorro 8, vida 5 años, tasa 12 % | −4,55 |
| El ahorro | 20 % menos (6,4 por año) | −8,30 |
| La vida | 4 años en lugar de 5 | −8,56 |
| La tasa | 6,3 % | 0 (es la tasa interna de retorno) |
| El ahorro | 9,9 por año | 0 (punto de equilibrio) |

La tabla dice algo que el VAN solo no dice: la máquina conviene si ahorra 9,9 por año en lugar de 8, o si la plata cuesta menos de 6,3 %. La conversación pasa de «el VAN da negativo» a «¿podemos estar seguros de que ahorra 10?», que es una pregunta que el área que pidió la máquina puede contestar.

Damodaran pone dos advertencias. La primera: «When analyzing the effects of changing a variable, we often hold all else constant. In the real world, variables move together» (si baja el volumen, también puede bajar el precio). La segunda: el objetivo es decidir mejor, «not churn out more tables and numbers»; no todo merece variarse.

## El punto de equilibrio y el perfil del VAN

El punto de equilibrio es el valor de un supuesto con el que el VAN da exactamente cero. En la tabla, 9,9 de ahorro anual. Es la forma más útil de presentar la sensibilidad a quien decide, porque traduce el riesgo a una cifra del negocio («hace falta ahorrar 10 por año»).

El perfil del VAN es el mismo cálculo para la tasa: el VAN con varias tasas, en un gráfico. Donde cruza el cero está la [tasa interna de retorno](tasa-interna-de-retorno.md). OpenStax lo propone para cuando la tasa es incierta: una empresa puede usarlo «to see how sensitive their decisions are to changes in financing costs». En su caso de paneles solares, el proyecto se rechaza solo si la plata cuesta más de unos 13,4 % (el texto dice 13,43 % y la figura, 13,41 %).

## Escenarios

Un escenario mueve varias variables a la vez de forma coherente: un caso malo con menos volumen, precio más bajo y costos más altos; un caso base; un caso bueno. Según Graham (2022), las empresas encuestadas trabajan en promedio con tres escenarios, «most scenarios are of a downside/base case/upside nature», casi siempre para la empresa entera y no para un proyecto. El caso base es «the "most likely" outcome (not necessarily the expected value)», y el malo se usa sobre todo para planear qué recortar si las cosas salen mal.

## Simulación

La simulación de Monte Carlo reemplaza cada supuesto por un rango con probabilidades y recalcula el VAN miles de veces. El resultado es una distribución. En el caso de Damodaran de un parque temático, el VAN va de −1.000 millones a +8.500 millones de dólares, con promedio de 3.400 millones, y es negativo el 12 % de las veces. Damodaran pregunta qué hace con eso quien decide, y entre las respuestas posibles pone, con ironía, imprimir los resultados «and file them away to show that I exercised due diligence». La simulación vale si cambia la decisión o el diseño del proyecto, no como respaldo.

## Cuánto se usa cada técnica

Graham (2022) compara el uso «siempre o casi siempre» en 2001 y 2022, separando empresas de más y de menos de mil millones de dólares de ventas:

| Técnica | Grandes 2001 | Grandes 2022 | Chicas 2001 | Chicas 2022 |
|---|---|---|---|---|
| Análisis de escenarios | 58,67 % | 68,67 % | 46,38 % | 51,78 % |
| Simulación | 16,08 % | 35,80 % | 11,94 % | 17,65 % |
| Opciones reales | 28,03 % | 37,50 % | 25,63 % | 40,28 % |

En la encuesta de 2001, Graham y Harvey notaban que las empresas muy endeudadas usaban más la sensibilidad y la simulación, «in part to assess (and limit to acceptable levels) the probability of financial distress». Sobre las opciones reales, que más de un cuarto decía usar, advertían que el uso dominante era probablemente cualitativo.

## Lo que el VAN no ve: poder esperar, ampliar o abandonar

Un VAN calculado hoy supone que la empresa hace el proyecto entero y no cambia nada después. En la realidad puede esperar a tener más datos, empezar chico y ampliar si anda, o abandonar si no. Damodaran cuenta entre los beneficios que el análisis tradicional no captura las «options embedded in projects (including the options to delay, expand or abandon a project)». Esas posibilidades tienen valor, y se las llama opciones reales.

La de esperar es la que más pesa en una empresa en marcha. Jagannathan, Meier y Tarhan proponen, siguiendo a McDonald y Siegel, que las empresas suben su tasa de corte justamente porque invertir hoy cierra la posibilidad de invertir mañana; está en [tasa de corte](tasa-de-corte.md#las-empresas-piden-más-que-su-costo-de-capital).

La lectura práctica de esta base: no hace falta valuar la opción con fórmulas para usarla. Alcanza con preguntar, antes de aprobar, si la inversión se puede partir en etapas, si hay una salida a mitad de camino y qué se aprendería esperando seis meses. Eso cambia el diseño del proyecto y se traslada a la [aprobación](../Aprobacion/aprobacion-de-la-inversion.md) por etapas; la guía de la GAO tiene una práctica para eso, «Budget for projects in useful segments».

> [!NOTE] Sin fuente todavía: un libro de texto leído sobre árboles de decisión y valuación de opciones reales (Dixit y Pindyck, 1994; Myers, 1977, no se leyeron).
