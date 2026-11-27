---
resumen: >-
  Un modelo base es un modelo grande, entrenado por otros sobre datos amplios y a escala, que se
  adapta a muchas tareas sin reentrenarlo; un LLM es el caso en que los datos son texto, y los
  modelos multimodales suman imagen, audio o video.
estado: vigente
estabilidad: estable
fuentes:
  - https://arxiv.org/abs/2108.07258
  - https://arxiv.org/abs/2005.14165
  - https://arxiv.org/abs/1810.04805
  - https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
  - https://arxiv.org/abs/2407.21783
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://web.stanford.edu/~jurafsky/slp3/
aliases: [foundation model, modelo fundacional, LLM, large language model, modelo de lenguaje grande, modelo de lenguaje, modelo multimodal]
creado: 2026-11-27
revisado: 2026-11-27
---

# Modelo base

Un modelo base es un modelo grande, entrenado por otros sobre datos amplios y a escala, que se
adapta a muchas tareas sin reentrenarlo; un LLM es el caso en que los datos son texto, y los
modelos multimodales suman imagen, audio o video.

Es la pieza que hace posible el oficio: como el modelo ya existe, quien construye un producto
arranca por el producto y adapta el modelo con [contexto](../Contexto/contexto.md),
[herramientas](../Agentes/agentes.md) o, si hace falta, [ajuste](../Ajuste/ajuste.md). Cómo se
llegó hasta acá (n-gramas, redes recurrentes, el salto de 2020 a 2022) está en
[Historia de la IA generativa](../Fundamentos/historia-de-la-ia-generativa.md); esta nota se queda
con lo que hace falta para entender qué es el modelo.

## De modelo de lenguaje a modelo base

Huyen, según el resumen público del capítulo 1 de *AI Engineering*, cuenta el paso en dos escalones:
de modelos de lenguaje a LLM, "enabled by self-supervision", y de LLM a modelos base que manejan
otros tipos de dato.

1. **Modelo de lenguaje.** Un modelo que, dado un texto, calcula la probabilidad de cada
   [token](token-y-embedding.md) posible como continuación. Genera encadenando esas predicciones:
   elige un token, lo agrega al texto y vuelve a predecir. Por eso se dice autorregresivo, y por eso
   la forma de elegir cada token ([muestreo](muestreo.md)) cambia lo que sale.
2. **LLM.** El mismo objetivo, con una red mucho más grande (un [Transformer](transformer.md)) y
   entrenada sobre un corpus enorme sin etiquetas: la etiqueta de cada posición es el token que
   sigue en el propio texto. Eso es la autosupervisión; lectura de esta base: como no hace falta
   etiquetar, sirve casi cualquier texto disponible ([preentrenamiento](preentrenamiento.md)).
3. **Modelo base.** Bommasani et al. (Stanford, 2021) acuñaron *foundation model* para los modelos
   "trained on broad data at scale" que se adaptan a muchas tareas, con BERT, DALL-E y GPT-3 como
   ejemplos (según su abstract). El nombre dice el rol: es la base sobre la que se construyen muchas
   aplicaciones.

## Una pieza general que se programa con texto

Lo que cambió la forma de trabajar fue que la tarea se describe en el texto de entrada. GPT-3 (Brown
et al., 2020), con 175.000 millones de parámetros, se evaluó en tareas nuevas "with no gradient
updates or fine-tuning", dándole solo instrucciones y algunos ejemplos en el prompt. Su abstract lo
resume así: "scaling up language models greatly improves task-agnostic, few-shot performance". De
ahí sale todo lo que vive en [Contexto](../Contexto/contexto.md): el [prompt](../Contexto/prompt.md)
es la forma de programar un modelo base.

Según el resumen del capítulo 2 de Huyen, el preentrenamiento sobre datos imperfectos da salidas que
no coinciden con lo que espera el usuario, y el [post-entrenamiento](post-entrenamiento.md) lo corrige
para que el modelo siga instrucciones y converse. En este tema, el modelo antes de esa etapa se llama
**modelo preentrenado**, y "modelo base" queda para el sentido de *foundation model* (convención de
esta base).

## Codificadores y decodificadores

No todo modelo base genera texto. BERT (Devlin et al., 2018) aprende representaciones de un texto
leyéndolo en las dos direcciones y se adapta a una tarea agregando "a single output layer": sirve para
clasificar o para representar, no para escribir. La rama generativa empezó con GPT (Radford et al.,
2018), que según su paper usa "a multi-layer Transformer decoder" como modelo de lenguaje: predice de
izquierda a derecha. Las dos ramas salen del mismo [Transformer](transformer.md). Lectura de esta base: lo que hace BERT, convertir un texto en
una representación, es lo que piden los [embeddings](token-y-embedding.md) que usa la
[recuperación](../Contexto/recuperacion.md).

> [!NOTE]
> Sin fuente todavía: una fuente primaria que muestre que los modelos generativos actuales siguen
> usando solo la parte decodificadora, como GPT en 2018.

## Modelos multimodales

Un modelo multimodal recibe o produce más de un tipo de dato. El informe de Llama 3 (Meta, 2024)
describe su modelo mayor como "a dense Transformer with 405B parameters and a context window of up to
128K tokens", y agrega imagen, video y voz con un enfoque composicional (según su abstract).

> [!NOTE]
> Sin fuente todavía: cómo se pasó a modelos nativamente multimodales, entrenados con varios tipos de
> dato desde el principio, y qué tipos de dato acepta cada modelo actual (la ficha de
> [Modelos disponibles](modelos-disponibles.md) no lo trae).

## Los defectos del modelo base se heredan

Bommasani et al. señalan la homogeneización: como muchas aplicaciones se construyen sobre el mismo
modelo, sus defectos pasan a todas. La [alucinación](alucinacion.md), los sesgos de los datos y el
corte de conocimiento llegan a cada producto que lo usa. Por eso la [evaluación](../Evaluacion/evaluacion.md)
mide el sistema en la tarea propia y no confía en lo que el modelo hace en general.

Lectura de esta base: un asistente o chatbot no es el modelo, sino el modelo más instrucciones de
sistema, herramientas y controles alrededor ([Sistemas con modelos](../Produccion/sistemas-con-modelos.md)).
Tampoco es una base de datos: no recupera hechos guardados, los regenera desde lo que aprendió. Si se
le pide el monto de una factura y devuelve `"total": 1520`, el número tiene la forma correcta, pero
nada en el modelo garantiza que sea el de la factura.

## Qué leer sobre modelos base

Bommasani et al., [*On the Opportunities and Risks of Foundation Models*](https://arxiv.org/abs/2108.07258),
secciones 1 y 2: fijarse en la diferencia entre el modelo (un artefacto que se adapta) y la aplicación
que se construye encima. Junto con el abstract de [GPT-3](https://arxiv.org/abs/2005.14165), para el
salto a "se programa con texto". Para el panorama técnico, Jurafsky y Martin,
[*Speech and Language Processing*](https://web.stanford.edu/~jurafsky/slp3/) (3.ª ed., PDF
gratuito), capítulos 1, 2 y 7; de ese libro se leyó solo el índice.
