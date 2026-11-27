---
resumen: >-
  Los evals de un sistema con un modelo son un conjunto de casos que imita el uso real y mide qué
  proporción de las salidas cumple los criterios del producto; reemplazan a la prueba de resultado
  exacto cuando la misma entrada puede dar salidas distintas.
estado: vigente
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://www.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://huyenchip.com/2025/01/07/agents.html
  - https://hamel.dev/blog/posts/evals/
  - https://hamel.dev/blog/posts/field-guide/
  - https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
  - https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
  - https://arxiv.org/abs/2407.01502
  - https://arxiv.org/abs/2502.14318
aliases: [evals, eval, evaluation, evaluación de LLM]
creado: 2026-11-27
revisado: 2026-11-27
---

# Evals

Los evals de un sistema con un modelo son un conjunto de casos que imita el uso real y mide qué
proporción de las salidas cumple los criterios del producto; reemplazan a la prueba de resultado
exacto cuando la misma entrada puede dar salidas distintas.

Cada caso de ese conjunto se llama, en la jerga, un *eval*. Los evals son la pieza central del
[bucle de la evaluación](evaluacion.md): reciben del
[análisis de errores](analisis-de-errores.md) qué medir, corren sobre las trazas que guarda la
[observabilidad](../Produccion/observabilidad-de-modelos.md) y deciden si una mejora se queda. Cada
caso se califica con código, con una [métrica](metricas-de-evaluacion.md), con un
[juez](ia-como-juez.md) o con una persona.

## Por qué la prueba unitaria no alcanza

Una prueba unitaria fija qué devuelve una función ante una entrada. Con un modelo eso falla por dos
lados. La salida varía entre corridas, así que una sola corrida no prueba nada. Y "correcto" muchas
veces no es una cadena exacta sino un juicio: si la respuesta es fiel al documento, si el tono sirve,
si resolvió lo que el usuario pedía. Husain agrega que esa corrección es subjetiva y hay que alinearla
con el criterio de una persona.

Parte del no determinismo se puede evitar. He (Thinking Machines, 2025) mostró que la causa principal
no es la concurrencia sino que los kernels de inferencia no son invariantes al tamaño del batch: con
1.000 completions de Qwen3-235B a temperatura 0 obtuvo 80 salidas distintas, y con kernels
invariantes, las 1.000 iguales. El costo, en una prueba con Qwen3-8B, fue de 42 s frente a 26 s de vLLM por defecto. Aun con salidas
reproducibles, un cambio chico de prompt o de modelo cambia el comportamiento, así que la evaluación
sobre muchos casos sigue haciendo falta. Cómo se aísla esa pieza incierta en el diseño está en
[aislar lo no determinista](../../Arquitectura/Modularidad/aislar-lo-no-determinista.md).

## Los tres niveles de Husain

Husain (2024) ordena la evaluación en tres niveles, de lo barato a lo caro:

| Nivel | Qué es | Cuándo corre |
|---|---|---|
| 1. Pruebas unitarias | Aserciones de código sobre la salida | En cada cambio |
| 2. Evaluación humana y por modelo | Personas o un [juez](ia-como-juez.md) califican trazas registradas | Sobre las trazas ya guardadas |
| 3. A/B testing | Dos versiones frente a usuarios reales, como en un [experimento A/B](../../Producto/Medicion/experimento-ab.md) | Cuando el producto ya es maduro |

El nivel 1 conserva lo que la prueba unitaria sí puede fijar. Husain recomienda etiquetas binarias
(bueno o malo) antes que puntajes en escala. Y advierte: "You can never stop
looking at data—no free lunch exists."

## Criterios antes de construir y en cada componente

Según el resumen del buscador del capítulo 4, Huyen propone *evaluation-driven development*: fijar
los criterios de evaluación antes de construir, como en TDD. La cita literal no se verificó. El índice
del capítulo sí muestra los tres pasos del pipeline: evaluar todos los componentes del sistema, no solo
la salida final; escribir una guía de evaluación con rúbrica; y elegir métodos y datos. Evaluar cada
componente es, por inferencia de esta base, lo que permite saber si una falla viene de la recuperación de
[contexto](../Contexto/contexto-y-rag.md), del prompt o del modelo.

Según los resúmenes de capítulo del repositorio del libro, Huyen sostiene que los
[benchmarks públicos](benchmarks-y-eleccion-de-modelo.md) sirven para descartar modelos malos pero no para elegir el mejor para una aplicación, y que para eso
se arma un "private leaderboard" propio. También que ningún método es perfecto y que se combinan:
comparación exacta, juez, personas.

## Volumen de casos o calidad de etiqueta

> [!IMPORTANT]
> Anthropic, en su guía de evaluaciones, pide "Prioritize volume over quality": "More questions with
> slightly lower signal automated grading is better than fewer questions with high-quality human
> hand-graded evals." Husain insiste en lo contrario en el énfasis: mirar los datos a mano, porque,
> según una frase que toma de Shankar et al., "it is impossible to completely determine evaluation
> criteria prior to human judging of LLM outputs". Las dos posiciones no se excluyen: la de Anthropic habla de cuántos casos automatizados
> correr; la de Husain, de cómo se descubren los criterios. Una lectura que las junta, inferencia de
> esta base: primero pocos casos mirados a mano para saber qué medir, después muchos casos
> automatizados para medirlo.

Anthropic agrega que los casos deben imitar la distribución real de tareas ("Don't forget to factor
in edge cases!") y que el juez sea un modelo distinto del que genera.

## Dónde la evaluación no alcanza

Las críticas más fuertes apuntan a los benchmarks públicos, no a los evals de una aplicación. Fodor
(2025, según el resumen del buscador) sostiene que los benchmarks se volvieron objetivo y no medida,
un caso de la ley de Goodhart. Kapoor et al. (2024) muestran que los benchmarks de agentes, con
holdouts débiles, producen agentes que "take shortcuts and overfit" y diseños "needlessly complex and
expensive". El mismo riesgo vale para un conjunto propio que nunca se renueva: si el sistema se ajusta
a esos casos, deja de medir el uso real. La fórmula de Huyen para agentes es medir fallas, no
aciertos: "identify its failure modes and measure how often each of these failure modes happens".

> [!NOTE]
> Sin fuente todavía: cómo se cortan los resultados por segmento (*slices*) y cómo se arma una
> suite de regresión para un sistema con modelos. Tampoco se leyó el texto de los capítulos 3 y 4 de
> Huyen, solo su índice y resúmenes.

## Qué leer para armar la primera evaluación

Huyen, *AI Engineering*, capítulo 4, sección "Design Your Evaluation Pipeline": fijarse en los tres
pasos y en evaluar cada componente. Como complemento práctico, Husain,
["Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/): fijarse en los tres niveles y
en las etiquetas binarias. La [fitness function](../../Arquitectura/Caracteristicas/fitness-function.md) del canon
es el antecedente directo: un chequeo automático de una característica, que acá pasa a ser una
proporción.
