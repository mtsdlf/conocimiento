---
resumen: >-
  IA como juez es usar un modelo de lenguaje para calificar o comparar las salidas de otro, de modo
  que la evaluación escale sin personas; es otro sistema con sesgos propios, que se valida contra
  juicio humano antes de confiar en él.
estado: vigente
estabilidad: semi
fuentes:
  - https://arxiv.org/abs/2306.05685
  - https://eugeneyan.com/writing/llm-evaluators/
  - https://hamel.dev/blog/posts/evals/
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://arxiv.org/abs/2404.12272
  - https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
  - https://www.thoughtworks.com/en-us/radar/techniques/llm-as-a-judge
aliases: [LLM-as-a-judge, LLM as judge, AI as a judge, juez LLM, LLM-evaluator]
creado: 2026-11-27
revisado: 2026-11-27
---

# IA como juez

IA como juez es usar un modelo de lenguaje para calificar o comparar las salidas de otro, de modo
que la evaluación escale sin personas; es otro sistema con sesgos propios, que se valida contra
juicio humano antes de confiar en él.

Es una forma de calificar [evals](evals.md), no una alternativa a ellos: Huyen lo trata como una
sección del capítulo de metodología de evaluación, junto a la evaluación exacta (ver
[métricas de evaluación](metricas-de-evaluacion.md)) y la evaluación comparativa (ver
[benchmarks y elección de modelo](benchmarks-y-eleccion-de-modelo.md)). Los criterios que aplica el juez salen del [análisis de errores](analisis-de-errores.md).

## Puntaje directo o comparación por pares

Hay dos formas de usar un juez. En el puntaje directo, el modelo califica una salida contra una
rúbrica (bien o mal, o una escala). En la comparación por pares, elige la mejor de dos salidas. Según
la revisión de Yan (2024), el puntaje directo sirve para criterios objetivos (si cita la fuente, si
respeta el formato) y la comparación por pares para criterios subjetivos (cuál es más clara). Husain
recomienda etiquetas binarias antes que escalas, y Anthropic, que el juez sea un modelo distinto del
que genera.

## Los sesgos que midió Zheng

Zheng et al. (2023) examinan "the usage and limitations of
LLM-as-a-judge, including position, verbosity, and self-enhancement biases":

| Sesgo | Qué hace el juez |
|---|---|
| Posición | Prefiere la respuesta según el lugar en que aparece en la comparación |
| Verbosidad | Prefiere la respuesta más larga |
| Autopreferencia (*self-enhancement*) | Prefiere las respuestas de su propio modelo |

Yan suma la inflación de puntajes y llama autopreferencia a lo mismo que Zheng llama
*self-enhancement*. Las cifras por sesgo y las mitigaciones están en el cuerpo del paper, que no se
leyó.

## Cuánto se parece a una persona

> [!IMPORTANT]
> Zheng et al. reportan que jueces fuertes como GPT-4 alcanzan "over 80% agreement, the same level
> of agreement between humans" con preferencias humanas controladas y de plataforma colaborativa. Yan, que
> revisó unos 24 papers, cita un estudio de resumen donde la correlación entre juez y humano fue de
> 0,3 a 0,6, contra 0,8 a 0,9 entre humanos. La diferencia puede venir de la tarea y la métrica
> (acuerdo en preferencias contra correlación en puntajes), pero ninguna fuente la resuelve: el
> acuerdo de un juez depende de la tarea y hay que medirlo en la propia.

El Thoughtworks Technology Radar movió LLM-as-a-judge de Trial (octubre de 2024) a Assess (noviembre
de 2025), con el argumento de que "often fails as a reliable proxy for human judgment" y es "less
mature than once believed". Yan agrega que las correlaciones mejoran con anotadores no expertos, y advierte que los resultados
pueden inflarse si quienes anotaron no eran expertos.

## Validar al juez como cualquier sistema

Huyen lo pone como regla: "AI judges must be evaluated and iterated over time, just like all other
AI applications", y "AI judges should be validated and correlated with systematic human evaluation".
Según los resúmenes de capítulo de su libro, los puntajes de jueces distintos no son comparables
entre sí. Pasos armados por esta base a partir de esas fuentes:

1. Etiquetá a mano un conjunto de salidas con el criterio del producto.
2. Corré el juez sobre el mismo conjunto y compará.
3. Medí con Cohen's kappa (según Yan, mide el acuerdo entre dos calificadores descontando el que se daría por azar), o con precisión y recall por separado, no con el porcentaje de acuerdo
   crudo: según Husain, "using raw agreement is generally not recommended and can be misleading when
   classes are imbalanced".
4. Versioná el prompt y el modelo del juez; si cambia cualquiera, repetí la validación.

Shankar et al. describen el [*criteria drift*](analisis-de-errores.md#criteria-drift-los-criterios-cambian-al-mirar), que los criterios cambian al calificar salidas; de ahí se deduce, como inferencia de esta base, que el conjunto
etiquetado envejece y que el juez se revalida cuando cambian los criterios. Registrar qué modelo y qué umbral se eligió para el juez es
una decisión que va a un [ADR](../../Arquitectura/Decisiones/adr.md).

> [!NOTE]
> Sin fuente todavía: cifras confiables de cuánto bajan los sesgos con mitigaciones (invertir el
> orden, pedir justificación). Un paper de 2026 con cifras de acuerdo y de sesgo de verbosidad fue retirado por arXiv y no se usa.

## Qué leer sobre jueces

Yan, ["Evaluating the Effectiveness of LLM-Evaluators"](https://eugeneyan.com/writing/llm-evaluators/),
para la síntesis: fijarse en kappa y en cuándo usar pares. Zheng et al.,
["Judging LLM-as-a-Judge"](https://arxiv.org/abs/2306.05685), para la evidencia de sesgos y acuerdo.
Huyen, *AI Engineering*, capítulo 3, "Limitations of AI as a Judge", para el marco (leído solo por su
título en el índice).
