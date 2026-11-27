---
resumen: >-
  La IA generativa actual sale de una línea que va de los modelos de lenguaje estadísticos y las
  redes recurrentes al Transformer de 2017, y de ahí al escalado (GPT-3, 2020), al ajuste por
  preferencias humanas (ChatGPT, 2022), a los modelos base que manejan varios tipos de dato y a
  los modelos de razonamiento (2024-2025).
estado: vigente
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
  - https://github.com/deepseek-ai/DeepSeek-R1
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
aliases: [historia de los LLM, historia de la IA generativa, history of generative AI, de los modelos de lenguaje a los modelos base]
creado: 2026-11-27
revisado: 2026-11-27
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
| 2015 | BPE para subpalabras (Sennrich et al.) | Las palabras raras se parten en piezas más chicas |
| 12 jun 2017 | Transformer (Vaswani et al.) | Una arquitectura solo de atención, sin recurrencia |
| 11 oct 2018 | BERT (Devlin et al.) | Un codificador preentrenado que se adapta con una capa |
| 23 ene 2020 | Leyes de escala (Kaplan et al.) | La pérdida baja como ley de potencia con modelo, datos y cómputo |
| 28 may 2020 | GPT-3 (Brown et al.) | 175.000 millones de parámetros; la tarea se pide con texto |
| 16 ago 2021 | "Foundation models" (Bommasani et al.) | Nombre y marco para el modelo base |
| 28 ene 2022 | Cadena de pensamiento (Wei et al.) | Pedir pasos intermedios mejora el razonamiento en modelos grandes |
| 4 mar 2022 | InstructGPT (Ouyang et al.) | Ajuste con demostraciones y preferencias humanas |
| 29 mar 2022 | Chinchilla (Hoffmann et al.) | Otra receta para repartir el cómputo entre modelo y datos |
| 30 nov 2022 | ChatGPT | El método de InstructGPT llevado a una conversación pública |
| 15 dic 2022 | IA constitucional (Constitutional AI; Bai et al.) | Preferencias generadas por un modelo a partir de principios escritos |
| 31 jul 2024 | Llama 3 (Meta) | Imagen, video y voz agregados a un modelo de lenguaje |
| 12 sep 2024 | o1 (OpenAI) | Un modelo entrenado para pensar antes de responder |
| 22 ene 2025 | DeepSeek-R1 | Razonamiento obtenido con aprendizaje por refuerzo, con pesos publicados |

## Antes del Transformer: n-gramas y redes recurrentes

Los modelos de lenguaje existían mucho antes de la IA generativa. Jurafsky y Martin les dedican
capítulos propios en *Speech and Language Processing* (cap. 3, "N-gram Language Models", y cap.
14, "RNNs and LSTMs"); de ese libro solo se confirmó el índice. Contado en una línea, y como
lectura de esta base: los n-gramas estiman la próxima palabra contando secuencias de n palabras, y
las redes recurrentes leen el texto paso a paso arrastrando un estado.

En 2015, Sennrich et al. propusieron partir las palabras raras en subpalabras con BPE (leído por su
abstract). Cómo se usa hoy esa idea está en [token y embedding](../Modelos/token-y-embedding.md).

> [!NOTE]
> Sin fuente todavía: el paso de los n-gramas a las redes neuronales (Bengio et al., 2003) y el de
> los embeddings de palabras (word2vec), con fechas y cifras de una fuente primaria leída.

## 2017: la atención reemplaza a la recurrencia

En junio de 2017, Vaswani et al. presentaron el [Transformer](../Modelos/transformer.md), una
arquitectura "based solely on attention mechanisms, dispensing with recurrence and convolutions
entirely". Según su abstract, en traducción inglés-alemán (WMT 2014) obtuvo 28,4 de BLEU y requirió
mucho menos tiempo de entrenamiento que los modelos anteriores. El paper original era un modelo de
traducción con codificador y decodificador.

BERT (octubre de 2018) usa el codificador: aprende representaciones bidireccionales con texto sin
etiquetar, se adapta a una tarea con "a single output layer" y reporta 80,5 % en GLUE. No genera
texto. Codificadores y decodificadores se explican en [modelo base](../Modelos/modelo-base.md#codificadores-y-decodificadores).

## 2020: escalar cambia la forma de usar el modelo

En enero de 2020, Kaplan et al. midieron que "the loss scales as a power-law with model size,
dataset size, and the amount of compute used for training", con tendencias de "more than seven
orders of magnitude". Chinchilla (2022) dio otra receta; la disputa está en
[preentrenamiento](../Modelos/preentrenamiento.md#leyes-de-escala-cuánto-modelo-y-cuántos-datos).

En mayo de 2020 llegó GPT-3: 175.000 millones de parámetros, "10 times larger than any previous
non-sparse language model", evaluado en few-shot "with no gradient updates or fine-tuning". Desde
ahí la tarea se pide con texto y unos ejemplos; el paso está contado en
[modelo base](../Modelos/modelo-base.md#una-pieza-general-que-se-programa-con-texto).

## 2021: el modelo base como categoría

En agosto de 2021, un informe de 114 autores de Stanford (Bommasani et al.) llamó *foundation
models* a los modelos "trained on broad data at scale" que se adaptan a muchas tareas, con BERT,
DALL-E y GPT-3 como ejemplos. Según su abstract, señalan la homogeneización (los defectos del
modelo base pasan a todo lo que se construye encima) y las capacidades emergentes. En esta base se
llama [modelo base](../Modelos/modelo-base.md).

## 2022: de completar texto a seguir instrucciones

Un modelo preentrenado completa texto; no necesariamente hace lo que se le pide. InstructGPT
(marzo de 2022) ajustó GPT-3 primero con demostraciones escritas por personas y después con
aprendizaje por refuerzo sobre rankings humanos de sus salidas. Su abstract dice que "outputs from
the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having
100x fewer parameters", sobre la distribución de prompts de los autores. La etapa se explica en
[post-entrenamiento](../Modelos/post-entrenamiento.md).

ChatGPT, anunciado el 30 de noviembre de 2022, aplicó "the same methods as InstructGPT" a un modelo
de la serie GPT-3.5. Según el resumen de su anuncio, la limitación declarada ya era la que hoy se
llama [alucinación](../Modelos/alucinacion.md): "sometimes writes plausible-sounding but incorrect
or nonsensical answers". En diciembre, la IA constitucional (Constitutional AI; Bai et al.)
reemplazó parte de las preferencias humanas por las de un modelo que juzga respuestas contra una
lista corta de principios. Ese año, Wei et al. mostraron el efecto de pedir pasos intermedios
(cadena de pensamiento), contado en [razonamiento](../Modelos/razonamiento.md#de-pedir-los-pasos-a-entrenarlos).

## 2024: modelos base que manejan más que texto

El segundo escalón de Huyen es el paso de LLM a modelos base que procesan otros tipos de dato.
El paper de Llama 3 (julio de 2024) es un ejemplo documentado: su modelo más grande es "a dense
Transformer with 405B parameters and a context window of up to 128K tokens", y las capacidades de
imagen, video y voz se agregan con un enfoque composicional, según su abstract.

> [!NOTE]
> Sin fuente todavía: una fuente histórica que cuente el paso a modelos nativamente multimodales
> (entrenados con varios tipos de dato desde el principio), con fechas.

## 2024-2025: gastar cómputo al pensar

En los modelos de razonamiento, el modelo genera una cadena de pensamiento antes de la respuesta.
En agosto de 2024, Snell et al. (preprint) mostraron que asignar cómputo de inferencia de forma
adaptativa para cada prompt es más de cuatro veces más eficiente que generar N respuestas y
quedarse con la mejor (paráfrasis de su abstract). El 12 de septiembre de 2024, OpenAI presentó o1:
según el resumen de su anuncio, un algoritmo de aprendizaje por refuerzo "teaches the model how to
think productively using its chain of thought".

DeepSeek-R1, enviado el 22 de enero de 2025 y publicado en *Nature* (vol. 645), mostró que el
razonamiento puede incentivarse con aprendizaje por refuerzo puro, sin ejemplos de razonamiento
escritos por personas, en tareas cuya respuesta se puede verificar (según su abstract). Su
repositorio dice "we have open-sourced DeepSeek-R1-Zero, DeepSeek-R1, and six dense models", con
pesos bajo licencia MIT. El mecanismo y la discusión sobre si estos modelos razonan están en
[razonamiento](../Modelos/razonamiento.md).

## Qué leer para la historia

No hay una fuente única. Para lo anterior a 2017, Jurafsky y Martin,
[*Speech and Language Processing*](https://web.stanford.edu/~jurafsky/slp3/), capítulos 3, 14 y 7,
en ese orden: n-gramas, redes recurrentes y Transformer. Para lo posterior, los abstracts de los
papers de la tabla, en orden; fijarse en qué se adapta en cada paso (los pesos, el prompt o la
cadena de pensamiento). Más lectura en la [bibliografía de IA](bibliografia-de-ia.md); cómo cambió
el oficio, en [AI engineering y ML engineering](ai-engineering-y-ml-engineering.md).
