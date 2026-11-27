---
resumen: >-
  La IA generativa actual sale de una línea que va de los modelos de lenguaje estadísticos y las
  redes recurrentes al Transformer de 2017, y de ahí al escalado (GPT-3, 2020), al ajuste por
  preferencias humanas (ChatGPT, 2022), a los modelos base que manejan varios tipos de dato y a
  los modelos de razonamiento (2024-2025).
estado: borrador
estabilidad: estable
fuentes:
  - https://web.stanford.edu/~jurafsky/slp3/
  - https://arxiv.org/abs/1508.07909
  - https://arxiv.org/abs/1706.03762
  - https://arxiv.org/abs/1810.04805
  - https://arxiv.org/abs/2001.08361
  - https://arxiv.org/abs/2005.14165
  - https://arxiv.org/abs/2108.07258
  - https://arxiv.org/abs/2201.11903
  - https://arxiv.org/abs/2203.02155
  - https://arxiv.org/abs/2203.15556
  - https://openai.com/index/chatgpt/
  - https://arxiv.org/abs/2212.08073
  - https://arxiv.org/abs/2407.21783
  - https://arxiv.org/abs/2408.03314
  - https://openai.com/index/learning-to-reason-with-llms/
  - https://arxiv.org/abs/2501.12948
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
aliases: [historia de los LLM, historia de la IA generativa, history of generative AI, de los modelos de lenguaje a los modelos base]
creado: 2026-11-27
revisado:
---

# Historia de la IA generativa

La IA generativa actual sale de una línea que va de los modelos de lenguaje estadísticos y las
redes recurrentes al Transformer de 2017, y de ahí al escalado (GPT-3, 2020), al ajuste por
preferencias humanas (ChatGPT, 2022), a los modelos base que manejan varios tipos de dato y a
los modelos de razonamiento (2024-2025).

Explica por qué cambió el oficio: cada paso volvió más conveniente adaptar un modelo que ya
existe que entrenar uno propio (lectura de esta base). Huyen, según el resumen de su capítulo 1,
cuenta la misma historia en dos escalones: de modelos de lenguaje a LLM, "enabled by
self-supervision", y de LLM a modelos base que manejan otros tipos de dato. Las fechas de abajo son
las de envío o publicación de cada paper; casi todos se leyeron solo por su abstract.

## Los hitos con fecha

| Fecha | Hito | Qué cambió |
|---|---|---|
| 2015 | BPE para subpalabras (Sennrich y otros) | El texto se parte en piezas de palabra, la base del [token](../Modelos/token-y-embedding.md) actual |
| 12 jun 2017 | Transformer (Vaswani y otros) | Atención sin recurrencia: se entrena en paralelo |
| 11 oct 2018 | BERT (Devlin y otros) | Un codificador preentrenado que se adapta con una capa |
| 23 ene 2020 | Leyes de escala (Kaplan y otros) | La pérdida baja como ley de potencia con modelo, datos y cómputo |
| 28 may 2020 | GPT-3 (Brown y otros) | 175 mil millones de parámetros; la tarea se pide con texto |
| 16 ago 2021 | "Foundation models" (Bommasani y otros) | Nombre y marco para el modelo base |
| 28 ene 2022 | Cadena de pensamiento (Wei y otros) | Pedir pasos intermedios mejora el razonamiento en modelos grandes |
| 4 mar 2022 | InstructGPT (Ouyang y otros) | Ajuste con demostraciones y preferencias humanas |
| 29 mar 2022 | Chinchilla (Hoffmann y otros) | Modelo y datos deben crecer en igual proporción |
| 30 nov 2022 | ChatGPT | El método de InstructGPT llevado a una conversación pública |
| 15 dic 2022 | Constitutional AI (Bai y otros) | Preferencias generadas por un modelo a partir de principios escritos |
| 31 jul 2024 | Llama 3 (Meta) | Imagen, video y voz agregados a un modelo de lenguaje |
| 12 sep 2024 | o1 (OpenAI) | Un modelo entrenado para pensar antes de responder |
| 22 ene 2025 | DeepSeek-R1 | Razonamiento obtenido con aprendizaje por refuerzo, con pesos abiertos |

## Antes del Transformer: contar palabras y recorrer secuencias

Los modelos de lenguaje existían mucho antes de la IA generativa. Un modelo de lenguaje asigna
probabilidad a la próxima palabra dadas las anteriores; los primeros lo hacían contando secuencias de
n palabras (n-gramas), y después llegaron las redes recurrentes (RNN y LSTM), que leen el texto
palabra por palabra y arrastran un estado. Jurafsky y Martin les dedican capítulos propios en
*Speech and Language Processing* (cap. 3, "N-gram Language Models", y cap. 14, "RNNs and LSTMs").

En 2015, Sennrich y otros propusieron partir las palabras raras en subpalabras con BPE, que es el
origen de la tokenización que usan los modelos de hoy.

> [!NOTE]
> Sin fuente todavía: el paso de los n-gramas a las redes neuronales (Bengio y otros, 2003) y el de
> los embeddings de palabras (word2vec), con fechas y cifras de una fuente primaria leída. Del libro
> de Jurafsky y Martin solo se confirmó el índice.

## 2017: la atención reemplaza a la recurrencia

En junio de 2017, Vaswani y otros presentaron el [Transformer](../Modelos/transformer.md), una
arquitectura "based solely on attention mechanisms, dispensing with recurrence and convolutions
entirely". En traducción inglés-alemán (WMT 2014) obtuvo 28,4 de BLEU, y entrenaba mucho más rápido
que los modelos anteriores, porque la atención procesa la secuencia en paralelo en lugar de
recorrerla. El paper original era un modelo de traducción con codificador y decodificador.

A partir de ahí la historia se abre en ramas. BERT (octubre de 2018) usa el codificador: aprende
representaciones bidireccionales con texto sin etiquetar, se adapta a una tarea con "a single
output layer" y reporta 80,5 % en GLUE. No genera texto. La rama que lleva a la IA generativa es
la de los modelos que solo predicen el próximo token, que es la de GPT. Contarla como una línea
recta esconde que codificadores y decodificadores son ramas distintas del mismo Transformer.

## 2020: escalar alcanza para cambiar la forma de usar el modelo

En enero de 2020, Kaplan y otros midieron que "the loss scales as a power-law with model size,
dataset size, and the amount of compute used for training", con tendencias de "more than seven
orders of magnitude".

En mayo de 2020 llegó GPT-3: 175 mil millones de parámetros, "10 times larger than any previous
non-sparse language model". Lo nuevo no fue solo el tamaño sino la forma de usarlo: se evaluó en
few-shot "with no gradient updates or fine-tuning", pidiéndole la tarea solo con texto y unos
ejemplos. El abstract lo resume en "scaling up language models greatly improves task-agnostic,
few-shot performance". Ese es el momento en que un modelo se empieza a programar con un
[prompt](../Contexto/prompt.md) en lugar de reentrenarlo.

> [!IMPORTANT]
> **Cuánto escalar el modelo y cuánto los datos.** Kaplan (2020) concluía que el entrenamiento
> óptimo "involves training very large models on a relatively modest amount of data". Chinchilla
> (Hoffmann y otros, marzo de 2022), con más de 400 modelos, encontró lo contrario: modelo y datos
> deben crecer en igual proporción, y "current large language models are significantly
> undertrained". Chinchilla, de 70 mil millones de parámetros, superó con el mismo cómputo a Gopher,
> de 280 mil millones. El detalle está en [preentrenamiento](../Modelos/preentrenamiento.md).

## 2021: el modelo base como categoría

En agosto de 2021, un informe de 114 autores de Stanford (Bommasani y otros) llamó *foundation
models* a los modelos "trained on broad data at scale" que se adaptan a muchas tareas, con BERT,
DALL-E y GPT-3 como ejemplos. Según su abstract, señalan dos rasgos: la homogeneización (los
defectos del modelo base pasan a todo lo que se construye encima) y las capacidades emergentes. El
nombre en castellano en esta base es [modelo base](../Modelos/modelo-base.md).

## 2022: de completar texto a seguir instrucciones

Un modelo preentrenado completa texto; no necesariamente hace lo que se le pide. InstructGPT
(marzo de 2022) ajustó GPT-3 primero con demostraciones escritas por personas y después con
aprendizaje por refuerzo sobre rankings humanos de sus salidas. Su abstract dice que "outputs from
the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having
100x fewer parameters", sobre la distribución de prompts de los autores. Es el origen del
[post-entrenamiento](../Modelos/post-entrenamiento.md) como etapa.

ChatGPT, anunciado el 30 de noviembre de 2022, aplicó "the same methods as InstructGPT" a un modelo
de la serie GPT-3.5, con conversaciones escritas y rankeadas por entrenadores humanos. Según el
resumen de su anuncio, la limitación declarada ya era la que hoy se llama
[alucinación](../Modelos/alucinacion.md): "sometimes writes plausible-sounding but incorrect or
nonsensical answers". En diciembre de 2022, Constitutional AI (Bai y otros) reemplazó parte de las
preferencias humanas por las de un modelo que juzga respuestas contra una lista corta de principios
escrita por personas.

Ese mismo año, Wei y otros mostraron que pedir pasos intermedios en los ejemplos (cadena de
pensamiento) llevaba a un modelo de 540 mil millones de parámetros, con ocho ejemplos, al estado
del arte en el conjunto de problemas matemáticos GSM8K.

## 2024: modelos base que manejan más que texto

El segundo escalón de Huyen es el paso de LLM a modelos base que procesan otros tipos de dato.
El paper de Llama 3 (julio de 2024) es un ejemplo documentado: su modelo más grande es "a dense
Transformer with 405B parameters and a context window of up to 128K tokens", y las capacidades de
imagen, video y voz se agregan con un enfoque composicional, sobre el modelo de lenguaje.

> [!NOTE]
> Sin fuente todavía: una fuente histórica que cuente el paso a modelos nativamente multimodales
> (entrenados con varios tipos de dato desde el principio), con fechas.

## 2024-2025: gastar cómputo al pensar

La última rama es la de los modelos de razonamiento: en lugar de responder de una vez, el modelo
genera una cadena de pensamiento antes de la respuesta, y se lo entrena para que esa cadena sirva.
En agosto de 2024, Snell y otros (preprint) mostraron que asignar cómputo de inferencia de forma
adaptativa para cada prompt es más de cuatro veces más eficiente que generar N respuestas y quedarse con la mejor (paráfrasis de su abstract).
El 12 de septiembre de 2024, OpenAI presentó o1: según el resumen de su anuncio, un algoritmo de
aprendizaje por refuerzo "teaches the model how to think productively using its chain of thought",
y los resultados mejoran con más entrenamiento y con más tiempo de pensamiento.

DeepSeek-R1, enviado el 22 de enero de 2025 y publicado en *Nature* (vol. 645), mostró con pesos
abiertos que el razonamiento puede incentivarse con aprendizaje por refuerzo puro, sin ejemplos de
razonamiento escritos por personas, y que rinde en tareas cuya respuesta se puede verificar
(matemática, programación). El mecanismo y la discusión sobre si estos modelos razonan de verdad
están en [razonamiento](../Modelos/razonamiento.md).

## Qué leer para la historia

No hay una fuente única. Para lo anterior a 2017, Jurafsky y Martin,
[*Speech and Language Processing*](https://web.stanford.edu/~jurafsky/slp3/) (3ª ed., PDF gratuito),
capítulos 3, 14 y 7, en ese orden: n-gramas, redes recurrentes y Transformer. Para lo posterior,
los abstracts de los papers de la tabla, en orden; fijarse en qué se adapta en cada paso (los
pesos, el prompt o la cadena de pensamiento). Más lectura en la [bibliografía de IA](bibliografia-de-ia.md);
cómo cambió el oficio, en [AI engineering y ML engineering](ai-engineering-y-ml-engineering.md).
