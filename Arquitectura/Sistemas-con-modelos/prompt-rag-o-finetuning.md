---
resumen: >-
  Elegir entre mejorar el prompt, sumar RAG o hacer fine-tuning es decidir cómo adaptar un modelo a
  una tarea: se empieza por el prompt, se suma contexto cuando al modelo le falta información y se
  entrena solo cuando lo que falla es su comportamiento y hay datos para corregirlo.
estado: vigente
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 5 «Prompt Engineering», pp. 211-251; cap. 7 «When to Finetune», pp. 311-318; cap. 8 «Model Distillation», p. 395"
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy
  - https://developers.openai.com/api/docs/guides/model-optimization
  - https://developers.openai.com/api/docs/guides/distillation
aliases: [fine-tuning, finetuning, ajuste fino, escalera de adaptación, prompt vs RAG vs fine-tuning, destilación, distillation]
creado: 2026-11-27
revisado: 2026-11-27
---

# Prompt, RAG o fine-tuning

Elegir entre mejorar el prompt, sumar RAG o hacer fine-tuning es decidir cómo adaptar un modelo a
una tarea: se empieza por el prompt, se suma contexto cuando al modelo le falta información y se
entrena solo cuando lo que falla es su comportamiento y hay datos para corregirlo.

Es una decisión de desarrollo, no una capa del sistema en ejecución: se toma antes de servir y
cambia qué prompt o qué modelo hay detrás del gateway, sin sumar un paso a las capas de
[Sistemas con modelos](sistemas-con-modelos.md). Los capítulos 5 a 8 de *AI Engineering* son, en
orden, prompt, RAG y agentes, fine-tuning e ingeniería de datos; ese orden coincide con la escalera (lectura de esta base).

## La escalera: del más barato al más caro de cambiar

| Escalón | Qué cambia | Qué cuesta |
|---|---|---|
| Prompt | las instrucciones y los ejemplos que recibe el modelo | horas; se prueba con la evaluación existente |
| RAG | la información que recibe en cada consulta | un índice, un recuperador y su mantenimiento ([Contexto y RAG](contexto-y-rag.md)) |
| Fine-tuning | los pesos del modelo | un conjunto de datos de entrenamiento, el entrenamiento y servir un modelo propio |

Los dos primeros no tocan el modelo; según el resumen del libro, RAG y agentes "are prompt-based".
OpenAI arranca igual: "Prompt engineering is typically the best place to start". Huyen cuenta entre
los errores de empezar demasiado complejo "insist on finetuning when prompting works". La columna de
costo es inferencia de esta base, ordenada como la ordenan las dos fuentes.

## El diagnóstico: falta conocimiento o falla el comportamiento

La guía de OpenAI "Optimizing LLM accuracy" da la pregunta que decide el escalón: qué tipo de falla
se ve en la [evaluación](../Evaluacion-y-observabilidad/evaluacion.md).

- **Le falta conocimiento**: el modelo no sabe algo (datos de la empresa, información reciente).
  Es un problema de contexto y se resuelve con RAG.
- **Su comportamiento es inconsistente**: sabe lo necesario pero no sigue el formato, el tono o el
  criterio de forma estable. Es un problema de aprendizaje y se resuelve con fine-tuning.
- **Las dos cosas**: se combinan.

El diagnóstico sale de mirar las fallas una por una, que es el
[análisis de errores](../Evaluacion-y-observabilidad/analisis-de-errores.md). Combinar no siempre
suma: la misma guía cuenta un caso de corrección de textos en islandés donde agregar RAG a un
modelo ya afinado bajó la métrica BLEU de 87 a 83.

## Cuándo el fine-tuning vale la pena

Según OpenAI, el fine-tuning ayuda cuando hay más ejemplos de los que entran en el prompt, cuando se
quieren prompts más cortos (menos tokens y menos latencia) y para "train a smaller, cheaper, faster
model to excel at a particular task". La guía pide empezar con 50 ejemplos o más de calidad, porque
"Quality of training data is more important than quantity".

Ese último caso tiene nombre, destilación: se ajusta el prompt en un modelo grande hasta que pasa
las evaluaciones, se guardan sus salidas como datos y se afina un modelo chico con ellas. Huyen la
trata en el cap. 8 (p. 395). En este caso el fine-tuning no sube la calidad sino que baja el
[costo y la latencia](../Caracteristicas/costo-y-latencia.md) (inferencia de esta base).

## El fine-tuning mueve el problema al dato

Según el resumen oficial del libro, lo difícil del cap. 7 no es la mecánica de entrenar sino saber
si hacerlo, y Huyen lo resume con una frase que escucha de practicantes: "finetuning is easy, but
getting data for finetuning is hard". Las técnicas de ajuste eficiente (como LoRA) bajaron el costo
de entrenar; no bajaron el de juntar, limpiar y etiquetar ejemplos buenos, que es el tema de su
cap. 8 (lectura de esta base). Por inferencia de esta base, un modelo afinado es además un modelo propio que hay que
versionar, evaluar y volver a afinar cuando sale uno base mejor: una decisión que conviene dejar
en un [ADR](../Decisiones/adr.md).

Las plataformas de fine-tuning de los proveedores también cambian: al menos una de las grandes
está cerrando la suya; el estado por proveedor está en [Plataformas de IA](plataformas-de-ia.md).

> [!NOTE]
> Sin fuente todavía: el texto de "When to Finetune" del libro (solo se leyeron el índice y el
> resumen) y una guía vigente de otros proveedores sobre cuándo afinar.

El recurso canónico es el cap. 7 de *AI Engineering*, "When to Finetune" (pp. 311-318), con
"Reasons Not to Finetune" (p. 312) y "Finetuning and RAG" (p. 316) para la decisión, y el cap. 8
sobre destilación (p. 395). Como complemento operativo, la guía
["Optimizing LLM accuracy"](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy) de
OpenAI, por el diagnóstico entre conocimiento y comportamiento. Conviene fijarse en que cada escalón
se justifica con una falla medida, no con una intuición.
