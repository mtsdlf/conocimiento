---
resumen: >-
  Los datos para ajustar son los ejemplos de entrada y respuesta con los que se entrena un modelo;
  se juzgan por calidad, cobertura y cantidad, y pocos ejemplos buenos, revisados a mano, sin
  duplicados y separados de los casos de evaluación rinden más que muchos con ruido.
estado: borrador
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://arxiv.org/abs/2305.11206
  - https://arxiv.org/abs/2107.06499
  - https://arxiv.org/abs/2312.16337
  - https://hamel.dev/blog/posts/evals/
  - https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy
  - https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms
aliases: [datos de entrenamiento, dataset de ajuste, training data, finetuning data, curación de datos, data curation]
creado: 2026-11-27
revisado:
---

# Datos para ajustar

Los datos para ajustar son los ejemplos de entrada y respuesta con los que se entrena un modelo;
se juzgan por calidad, cobertura y cantidad, y pocos ejemplos buenos, revisados a mano, sin
duplicados y separados de los casos de evaluación rinden más que muchos con ruido.

Son la parte cara del [finetuning](finetuning.md), por lo que explica
[Ajuste](ajuste.md#por-qué-el-ajuste-mueve-el-problema-al-dato). Cuando los ejemplos reales no alcanzan se generan con modelos, que es lo que trata
[Datos sintéticos](datos-sinteticos.md); lo de esta nota vale para los dos.

## Calidad, cobertura y cantidad

El resumen del cap. 8 de Huyen da tres criterios para cualquier fase del entrenamiento: "quality,
coverage, and quantity". Se arranca por "the behaviors you want your model to learn", no por los
datos que hay a mano.

- **Calidad**: cada ejemplo muestra la respuesta que se quiere, en el formato que se quiere. "A
  small amount of high-quality data can outperform a large amount of noisy data".
- **Cobertura**: los ejemplos abarcan los casos que el producto va a ver, incluidos los raros. Los
  casos los da el [análisis de errores](../Evaluacion/analisis-de-errores.md), que es donde aparecen
  las fallas que el ajuste tiene que corregir.
- **Cantidad**: la que alcance con calidad y cobertura; LIMA, abajo, muestra un caso en que alcanzó con mil.

## Cuántos ejemplos hacen falta

LIMA (Zhou et al., 2023) es el caso que cambió la intuición. Según su abstract, un LLaMA de 65.000
millones de parámetros ajustado con solo 1.000 pares curados, sin refuerzo ni modelo de
preferencias, dio respuestas iguales o preferidas a las de GPT-4 en el 43 % de los casos de un
estudio con personas. Su conclusión: "almost all knowledge in large language models is learned
during pretraining".

El resultado habla de estilo y formato en un modelo grande ya preentrenado: no autoriza a esperar
que mil ejemplos enseñen conocimiento nuevo, que es justo lo que el ajuste hace mal (ver
[Finetuning](finetuning.md#lo-que-el-finetuning-enseña-y-lo-que-no)). El piso que pide un gran
proveedor para empezar está en [Prompt, RAG o finetuning](../prompt-rag-o-finetuning.md#cuándo-el-finetuning-vale-la-pena),
con su regla de que la calidad importa más que la cantidad.

Repetir los datos tampoco ayuda: en el experimento de Raschka con LoRA, entrenar unas dos épocas
sobre un conjunto de 50.000 ejemplos empeoró el resultado, y lo mismo con uno de 1.000. Es un solo
experimento con un modelo; junto con lo anterior, acota en vez de contradecir: pocos ejemplos si son
buenos, y no pasarlos de más.

## Mirar los datos antes de entrenar

Husain lo pone como regla de trabajo: "You must remove all friction from the process of looking at
data", y "You can never stop looking at data—no free lunch exists". Es el mismo hábito que el
[análisis de errores](../Evaluacion/analisis-de-errores.md), aplicado a la entrada del ajuste en vez
de a la salida del sistema. Husain también reutiliza el sistema de evaluación para filtrar
ejemplos: los tests y las aserciones descartan los que fallan.

El índice del libro de Huyen ordena el procesamiento en cuatro pasos: inspeccionar, deduplicar,
limpiar y filtrar, y dar formato (según el índice del libro, cap. 8, pp. 396-401).

## Duplicados y contaminación con los casos de evaluación

Los duplicados aumentan la memorización: que el modelo reproduzca textos del entrenamiento. Lee et
al. (2021) la midieron en
conjuntos de preentrenamiento; según su abstract, más del 1 % de lo que generaban los modelos
entrenados con ellos sin guía era copia del entrenamiento, una misma oración aparecía más de 60.000
veces en un conjunto popular, y deduplicar redujo la memorización y pidió menos pasos de
entrenamiento. Encontraron además solapamiento entre entrenamiento y prueba en más del 4 % de los
conjuntos de validación estándar. El paper es sobre preentrenamiento; que valga para el ajuste es
lectura de esta base.

El solapamiento con la evaluación tiene nombre propio. Li y Flanigan (AAAI 2024) encontraron que los
modelos rinden mejor en conjuntos publicados antes de que se juntaran sus datos de entrenamiento, y
lo llamaron "task contamination"; según su abstract, en tareas que no pudieron estar contaminadas
los modelos rara vez superan por mucho a la clase mayoritaria. Lo mismo le pasa a un equipo que
arma los datos de ajuste con los mismos casos que usa para medir.

Pasos para no contaminar, armados por esta base a partir de esas fuentes:

1. Separá el conjunto de [evals](../Evaluacion/evals.md) antes de juntar datos de ajuste, y no lo
   toques después.
2. Deduplicá los datos de ajuste, también los casi iguales.
3. Buscá solapamiento entre los datos de ajuste y los evals, y sacá de los datos lo que coincida.
4. Si usás un [benchmark público](../Evaluacion/benchmarks-y-eleccion-de-modelo.md) para comparar,
   asumí que el modelo de partida pudo haberlo visto.

> [!NOTE]
> Sin fuente todavía: los formatos de datos (instrucción y respuesta, conversación, pares de
> preferencias), la anotación con guías para quien etiqueta y cómo se mide el acuerdo entre
> anotadores. Huyen los trata en "Data Acquisition and Annotation" y "Format Data" del cap. 8
> (según el índice del libro), que no se leyeron.

## Qué leer sobre datos para ajustar

Huyen, *AI Engineering*, cap. 8, "Data Curation" (pp. 365-380) para los tres criterios y "Data
Processing" (pp. 396-401) para inspección, deduplicación y filtrado. El paper de
[LIMA](https://arxiv.org/abs/2305.11206) completo, en la construcción del conjunto de 1.000 ejemplos:
fijarse en qué hicieron para lograr diversidad con tan pocos ejemplos, y en que el resultado habla
de estilo, no de conocimiento.
