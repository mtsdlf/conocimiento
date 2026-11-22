---
resumen: >-
  La medición comercial cuenta cuántas oportunidades entran a la venta, cuántas avanzan y se cierran, por cuánto y en cuánto tiempo. Sirve para ver dónde se traba la venta y para prever cuánto va a entrar.
estado: borrador
estabilidad: semi
fuentes:
  - "Outreach, Pipeline velocity: https://outreach.io/resources/blog/pipeline-velocity (según resumen)"
  - "Pipedrive, Sales velocity: https://pipedrive.com/en/blog/sales-velocity (según resumen; de ahí el ejemplo)"
  - "G2, Sales velocity: https://learn.g2.com/sales-velocity (según resumen)"
  - "Livespace, definición de tasa de cierre: https://www.livespace.io/en//94EWN (según resumen)"
  - "Ebsta, B2B Sales Benchmark Report 2021: https://www.ebsta.com/wp-content/uploads/2021/08/Ebsta-B2B-Sales-Benchmark-Report-2021.pdf (según resumen; el PDF no se pudo leer)"
  - "Norwest, 2024 B2B sales & marketing benchmark report: https://www.norwest.com/blog/2024-norwest-b2b-sales-marketing-benchmark-report (según resumen)"
  - "Databox, B2B sales cycle length: https://databox.com/b2b-sales-cycle-length (según resumen)"
  - "Xactly, 2024 Sales Forecasting Benchmark Report: https://www.xactlycorp.com/sites/default/files/file/2024-07/2024_sales_forecasting_benchmark_report.pdf (según resumen del buscador; el PDF no se pudo leer)"
  - "Gartner (2020), State of Sales Operations Survey: https://www.gartner.com/en/newsroom/press-releases/2020-02-12-gartner-says-less-than-50--of-sales-leaders-and-selle (según resumen)"
  - "Clari, estudio de Forrester sobre previsión de ventas: https://clari.com/blog/forrester-study-sales-forecasting (según resumen)"
  - "Ventas/.investigacion/objeciones-formas-y-medicion.md (sección C)"
aliases: [sales metrics, métricas de ventas, sales funnel, embudo de ventas, pipeline, win rate, tasa de cierre, sales cycle, ciclo de venta, pipeline velocity, sales velocity, velocidad del pipeline, sales forecast, previsión de ventas, forecast]
creado: 2026-11-22
revisado:
---

# Medición comercial

La medición comercial cuenta cuántas oportunidades entran a la venta, cuántas avanzan y se cierran, por cuánto y en cuánto tiempo. Sirve para ver dónde se traba la venta y para prever cuánto va a entrar.

Mide a las otras partes de [Ventas](../ventas.md). Cuenta cuántas oportunidades pasan la [calificación](../Descubrimiento-y-calificacion/calificacion.md) y cuántas terminan en acuerdo después de [objeciones y negociación](../Objeciones-y-negociacion/objeciones-y-negociacion.md). Dice cuánto y dónde, pero no por qué: el porqué de cada venta ganada o perdida lo recoge el [análisis de ventas ganadas y perdidas](../../Estrategia-competitiva/Analisis-de-competidores/analisis-de-ventas-ganadas-y-perdidas.md). Si la venta deja plata después de lo que costó conseguirla lo responde la [economía unitaria](../../Marketing/Medicion/economia-unitaria.md).

## El embudo comercial y sus cuatro números

El embudo comercial (pipeline) es la lista de oportunidades abiertas, ordenadas por la etapa en que están: contacto, descubrimiento, propuesta, negociación, cerrada. Cada empresa define sus etapas; lo que importa es que cada etapa tenga un criterio de entrada claro, como «el cliente recibió la propuesta». Cuatro números lo describen:

| Número | Qué mide | Cómo falla |
|---|---|---|
| Oportunidades calificadas | Cuántas posibles ventas pasaron el filtro de calificación | Si el filtro es laxo, el embudo se infla con oportunidades que nunca iban a cerrar |
| Tasa de cierre | Qué parte de las oportunidades termina en venta | El número cambia según qué se cuente abajo de la fracción |
| Tamaño promedio | Cuánto vale en promedio una venta cerrada | Un par de ventas grandes lo mueven mucho en un equipo chico |
| Ciclo de venta | Cuánto tarda una oportunidad desde que entra hasta que se cierra | Se mide distinto si se empieza a contar en el primer contacto o en la calificación |

La tasa de cierre depende del denominador. Livespace la calcula sobre los negocios cerrados, ganados y perdidos; otros benchmarks cuentan todas las oportunidades o solo las calificadas. Con los mismos negocios, cada definición da un número distinto. Quien mide tiene que declarar la suya, y quien compara con un benchmark, mirar cuál usó.

> [!NOTE] Sin fuente todavía: una definición canónica de las etapas del embudo comercial; las de arriba son criterio de la base.

## La velocidad del pipeline es una convención de proveedores

La velocidad del pipeline junta los cuatro números en uno: cuánto ingreso genera el embudo por unidad de tiempo. La fórmula aparece igual en varios proveedores de software de ventas, como Outreach, Pipedrive y G2. Es una convención de la industria, no un resultado de investigación.

```
velocidad = oportunidades calificadas × tamaño promedio × tasa de cierre ÷ ciclo de venta
```

El ejemplo de Pipedrive usa 40 oportunidades, un tamaño promedio de 8.000, una tasa de cierre de 0,25 y un ciclo de 45 días: 40 × 8.000 × 0,25 ÷ 45 = 1.777,78 por día. La unidad del resultado es la del ciclo, por día, por semana o por mes.

G2 advierte que hay que usar definiciones y períodos consistentes. Además, los cuatro factores no son independientes, y esto es inferencia de la base: apurar el ciclo para subir la velocidad puede bajar la tasa de cierre, y aflojar la calificación para sumar oportunidades, también. La fórmula sirve para ver qué palanca mover, no para mover una sola y suponer que las otras quedan quietas.

## Los benchmarks son de proveedores y de SaaS

Todos los benchmarks encontrados vienen de empresas que venden software o invierten en él, y miden a sus propios clientes. Sirven como orden de magnitud, dicho con su año, su muestra y su sesgo.

| Fuente | Qué dice | Sesgo |
|---|---|---|
| Ebsta, informe 2021 y posteriores | 19% de cierre en clientes nuevos, sobre un conjunto de 655.000 oportunidades; el de 2021 cubre unos USD 100 mil millones en valor de negocios | Empresas que usan Ebsta y su CRM |
| Norwest, 2024 | Cerrar un negocio de USD 50 a 100 mil de valor anual tarda casi lo mismo que uno de más de USD 100 mil | Empresas SaaS de la cartera de un fondo de inversión |
| Databox | Un ciclo de venta B2B suele pasar de dos meses | Sin metodología publicada |

Ningún benchmark encontrado es de la Argentina, de venta a comercios chicos ni de servicios profesionales. Los números son de SaaS y B2B de Estados Unidos, y no se trasladan a una plataforma que le vende a comercios ni a una consultora sin decirlo. Para un equipo chico, el benchmark útil es el propio: la tasa de cierre y el ciclo de los últimos trimestres, medidos siempre igual.

## La previsión de ventas falla seguido, según quienes venden herramientas para preverla

La previsión de ventas (forecast) estima cuánto se va a cerrar en un período, a partir del embudo. Las cifras sobre su precisión son de proveedores, con definiciones distintas, y no se comparan entre sí:

- Xactly (2024), que vende software de comisiones y previsión: 4 de cada 5 líderes de ventas y finanzas dicen haber fallado un pronóstico trimestral en el último año, y más de la mitad, dos o más veces. La cifra viene del buscador; el PDF no se pudo leer.
- Gartner (2020): solo 45% de los líderes y vendedores tiene alta confianza en la precisión de su previsión. Mide confianza, no error.
- Forrester, en un estudio encargado por Clari, otro proveedor de previsión: 51% falla el pronóstico mensual por más de 10%, y 85% por más de 5%.

Una cifra muy citada, atribuida a SiriusDecisions, sobre cuántas organizaciones se pasan del pronóstico no se pudo verificar en la página de Forrester que la menciona, y no se usa en esta base.

> [!NOTE] Sin fuente todavía: un estudio académico independiente sobre la precisión de la previsión de ventas.

## Qué hacer con los números al analizar la competencia

Un equipo que registra contra quién compitió en cada oportunidad puede calcular su tasa de cierre frente a cada rival. Ese número dice contra quién se pierde más, y el análisis de ventas ganadas y perdidas dice por qué. Para un SaaS que analiza competidores antes de diseñar una función, la combinación muestra si el rival gana por producto, por precio o por cómo vende. Esto es criterio de la base.

## Recursos para leer

No hay un recurso canónico recomendable. Para la fórmula, la página de Pipedrive o de Outreach, sabiendo que es convención. Para benchmarks, Ebsta o Norwest, citando año, muestra y sesgo. Para la previsión, ninguno independiente.

## Lo que falta de Medición comercial

Esta vertical tiene solo su entrada. Faltan estas notas y se van a sumar:

- Embudo comercial: cómo se definen las etapas y sus criterios de entrada.
- Tasa de cierre y ciclo de venta, con definiciones y benchmarks leídos en origen.
- Previsión de ventas: métodos y cómo se mide su error.

> [!NOTE] Sin fuente todavía: benchmarks de embudo, cierre y ciclo para comercios chicos, servicios profesionales y la Argentina; los informes de Ebsta 2024 y Xactly 2024 leídos completos.
