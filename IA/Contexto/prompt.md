---
resumen: >-
  El prompt es el texto con que se le pide algo al modelo: instrucciones, ejemplos y la consulta,
  repartidos en mensajes con roles. Es la forma más barata de adaptar un modelo a una tarea, porque
  no toca sus pesos, y se versiona y se prueba como código.
estado: borrador
estabilidad: semi
fuentes:
  - https://arxiv.org/abs/2005.14165
  - https://arxiv.org/abs/2201.11903
  - https://arxiv.org/abs/2406.06608
  - https://arxiv.org/abs/2506.07142
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
  - https://developers.openai.com/api/docs/guides/prompt-engineering
  - https://hamel.dev/blog/posts/evals/
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 5 «Prompt Engineering», pp. 211-251 (solo índice)"
aliases: [prompt engineering, ingeniería de prompts, prompting, system prompt, prompt de sistema, few-shot, in-context learning, aprendizaje en contexto]
creado: 2026-11-27
revisado:
---

# Prompt

El prompt es el texto con que se le pide algo al modelo: instrucciones, ejemplos y la consulta,
repartidos en mensajes con roles. Es la forma más barata de adaptar un modelo a una tarea, porque
no toca sus pesos, y se versiona y se prueba como código.

Es la primera pieza del [contexto](contexto.md) y la base sobre la que se suman las demás: los
fragmentos de un [RAG](contexto-y-rag.md), la [memoria](memoria.md) y los resultados de
herramientas entran en el mismo texto. Cuando el prompt no alcanza, la decisión de qué probar
después está en [Prompt, RAG o finetuning](../prompt-rag-o-finetuning.md).

## Aprender una tarea sin cambiar pesos

Que un modelo pueda hacer una tarea nueva solo porque se la describen en texto se llama aprendizaje
en contexto (*in-context learning*). Lo mostró GPT-3 en 2020: según el abstract de Brown et al., el
modelo, de 175.000 millones de parámetros, se evaluó sin actualizar pesos, con la tarea y los
ejemplos dados solo como texto, y los autores concluyen que "scaling up language models greatly
improves task-agnostic, few-shot performance". Dar ejemplos se llama *few-shot*; no darlos,
*zero-shot*.

El campo acumuló muchas técnicas desde entonces. The Prompt Report, según su abstract, ordena 58
técnicas para modelos de texto y 40 para otras modalidades. La mayoría son variantes de unas pocas
ideas que siguen en las guías de los proveedores.

## El prompt de sistema y el del usuario

Las APIs reparten el prompt en mensajes con roles. El de sistema (o de desarrollador) lo escribe
quien construye el producto y fija el comportamiento; el de usuario trae la consulta de cada vez.
OpenAI propone pensarlos "like a function and its arguments in a programming language", y los
mensajes de desarrollador tienen prioridad sobre los del usuario. Huyen abre su capítulo con esa
distinción (cap. 5, p. 215, según el índice).

Esa prioridad la aprende el modelo; no la garantiza nada. Un texto en el mensaje de usuario o en un
documento recuperado puede pasar por encima del prompt de sistema, y por eso el prompt de sistema no
sirve como control de seguridad: se explica en [Inyección de prompt](inyeccion-de-prompt.md).

## Lo que sigue funcionando

Las guías actuales de Anthropic y OpenAI coinciden en un núcleo que el índice de Huyen también
ordena como prácticas (cap. 5, pp. 220-229):

- **Instrucciones claras y explícitas**, con el contexto que la tarea necesita: para qué es la
  salida, quién la lee, qué formato lleva.
- **Ejemplos variados.** OpenAI: "try to show a diverse range of possible inputs with the desired
  outputs". Anthropic recomienda "3–5 examples for best results", envueltos en etiquetas.
- **Estructura con etiquetas** para separar instrucciones, documentos y ejemplos.
- **Documentos largos arriba y la consulta al final.** Según Anthropic, "Queries at the end can
  improve response quality by up to 30 percent in tests"; la cifra es de pruebas del propio
  laboratorio.
- **Partir una tarea compleja en pasos** encadenados, que es el patrón de cadena de
  [Patrones de flujo](../Agentes/patrones-de-flujo.md).

Si la salida tiene que tener una forma fija (un JSON con ciertos campos), pedirla en el prompt no
alcanza para garantizarla; las salidas estructuradas se explican en [Muestreo](../Modelos/muestreo.md).

## Lo que perdió peso con modelos más capaces

Varias técnicas de 2022 y 2023 compensaban limitaciones que los modelos fueron perdiendo:

- **Pedir que piense paso a paso.** Wei et al. (2022) mostraron, según su abstract, que con ocho
  ejemplos con pasos intermedios un modelo de 540.000 millones de parámetros alcanzaba el estado del
  arte en problemas de matemática escolar. En 2025, Meincke et al. (preprint sin revisión por pares,
  según su abstract) encontraron que en modelos sin razonamiento la mejora es "a small average
  improvement" con más variabilidad, y en los modelos que ya razonan por dentro, "often only marginal
  accuracy gains, if any", a cambio de más tokens y tiempo. Por qué pasa eso está en
  [Razonamiento](../Modelos/razonamiento.md).
- **El énfasis agresivo.** Anthropic dice que sus modelos recientes responden más al prompt de
  sistema, y que donde antes se escribía "CRITICAL: You MUST use this tool when..." ahora alcanza con
  "Use this tool when...".
- **Rellenar el comienzo de la respuesta** (*prefill*) para forzar un formato: Anthropic dejó de
  aceptarlo en sus modelos recientes y dice que "most use cases of prefill no longer require it".

> [!IMPORTANT]
> Los proveedores no coinciden en si el estilo depende del tipo de modelo. OpenAI separa: a un modelo
> de razonamiento se le da un objetivo, "like a senior co-worker", y a uno sin razonamiento,
> instrucciones explícitas, "like a junior coworker". Anthropic presenta un solo conjunto de técnicas
> para todos sus modelos vigentes. No hay un estudio independiente que lo arbitre: se prueba con el
> modelo propio y los [evals](../Evaluacion/evals.md) propios.

## Versionar el prompt como código

Un prompt de producción es código: cambia el comportamiento del sistema y se rompe como cualquier
cambio. OpenAI recomienda fijar la aplicación a una instantánea concreta del modelo, guardar los
prompts en el código de la aplicación con revisión y despliegue normales, y agregar casos de prueba
y evaluaciones antes de cambiarlos. Huyen cierra la parte de prácticas con "Organize and Version
Prompts" (p. 233, según el índice).

El riesgo de no hacerlo es el prompt que crece por acumulación. Husain cuenta un caso, un asistente
inmobiliario, en el que el prompt engineering se estancó y los prompts se volvieron largos y
difíciles de manejar a medida que se sumaban casos borde. Es un solo caso, de un practicante que
vende consultoría en evaluación, pero ilustra por qué cada cambio de prompt pasa por un
[eval](../Evaluacion/evals.md): sin él, arreglar un caso rompe otro sin que nadie lo vea.

Anthropic agrega un límite antes de empezar: "Not every success criterion or failing eval is best
solved by prompt engineering". A veces cambiar de modelo resuelve latencia o costo más fácil, y a
veces el problema es de conocimiento y lo resuelve el [RAG](contexto-y-rag.md).

## Qué leer sobre prompts

Para entender, Huyen, *AI Engineering*, cap. 5, de "Introduction to Prompting" (p. 212) a "Organize
and Version Prompts" (p. 233); fijarse en el prompt como comunicación y no como truco (leído solo
por su índice). Para hacerlo, la guía ["Prompting best practices"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
de Anthropic, la más actual y fechada contra modelos concretos, en paralelo con la
[guía de OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering) para ver qué
cambia entre proveedores. En las dos, fijarse en que cada consejo depende del modelo y en que la
regla común es medir antes de iterar.

> [!NOTE]
> Sin fuente todavía: la guía de prompts de otros proveedores y un estudio del costo de versionar y
> evaluar prompts más allá de un caso.
