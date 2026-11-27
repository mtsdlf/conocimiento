---
resumen: >-
  El finetuning es seguir entrenando un modelo ya entrenado con ejemplos de una tarea, para que
  cambie su comportamiento de forma estable; sirve para formato, estilo y criterio más que para
  meter hechos nuevos, pide mucha más memoria que inferir y puede hacerle olvidar lo que ya sabía.
estado: borrador
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://hamel.dev/blog/posts/evals/
  - https://huggingface.co/docs/transformers/model_memory_anatomy
  - https://arxiv.org/abs/1910.02054
  - https://arxiv.org/abs/2405.09673
  - https://arxiv.org/abs/2312.05934
  - https://developers.openai.com/api/docs/deprecations
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms
aliases: [fine-tuning, ajuste fino, afinar un modelo, SFT, supervised finetuning, ajuste supervisado, full finetuning]
creado: 2026-11-27
revisado:
---

# Finetuning

El finetuning es seguir entrenando un modelo ya entrenado con ejemplos de una tarea, para que
cambie su comportamiento de forma estable; sirve para formato, estilo y criterio más que para
meter hechos nuevos, pide mucha más memoria que inferir y puede hacerle olvidar lo que ya sabía.

La forma más común es el ajuste supervisado: pares de entrada y respuesta esperada, y el modelo
aprende a producir esa respuesta. Los laboratorios usan la misma familia de técnicas, más el ajuste
por preferencias, para convertir un modelo base en un asistente; eso está en
[Post-entrenamiento](../Modelos/post-entrenamiento.md). Acá se trata el finetuning que hace quien
construye un producto sobre un modelo ya entrenado.

## Lo que el finetuning enseña y lo que no

Husain lo resume: "Fine-tuning is best for learning syntax, style, and rules". Para hechos nuevos la
evidencia va en contra: según un resumen secundario de Ovadia et al. (EMNLP 2024), RAG "consistently
outperforms" al finetuning no supervisado tanto en conocimiento ya visto como en nuevo, y los
modelos "struggle to learn new factual information" por esa vía salvo que vean muchas variaciones
del mismo hecho. Lo que le falta saber al modelo se le da con [Contexto y RAG](../Contexto/contexto-y-rag.md).

Cuándo conviene ajustar y cuándo quedarse en el prompt o en RAG se decide con la falla que muestra
la evaluación, y está en [Prompt, RAG o finetuning](../prompt-rag-o-finetuning.md). El libro de
Huyen dedica a la decisión tres secciones del cap. 7: "Reasons to Finetune", "Reasons Not to
Finetune" y "Finetuning and RAG" (según el índice del libro; su texto no se leyó).

## Las razones para no ajustar

El resumen del cap. 7 dice que "The process of finetuning itself isn't hard" y cierra con
"finetuning is easy, but getting data for finetuning is hard". Lo caro está en los
[datos para ajustar](datos-para-ajustar.md), no en el entrenamiento. Huyen cuenta entre los errores
de empezar demasiado complejo "insist on finetuning when prompting works".

Un modelo ajustado sobre un modelo cerrado depende además de que el proveedor no retire la base. La
página de deprecaciones de un gran proveedor dice que los modelos ajustados "follow the same
shutdown schedule as their underlying base models": cuando se apaga la base, el ajuste se pierde y
hay que rehacerlo sobre otra. Es la razón práctica más fuerte para no ajustar un modelo cerrado
(lectura de esta base). Qué proveedores ofrecen ajuste hoy, y cuáles lo están cerrando, está en la
ficha [Plataformas de IA](../Produccion/plataformas-de-ia.md).

> [!IMPORTANT]
> **Si el finetuning todavía hace falta.** Una posición dice que, con modelos fuertes, el prompt y
> RAG alcanzan; Huyen critica insistir en ajustar "when prompting works". La evidencia acota esa
> posición en vez de confirmarla: para conocimiento nuevo gana RAG (Ovadia et al., según un resumen
> secundario), y para comportamiento y dominio el finetuning sigue aprendiendo cosas, el completo
> más que LoRA (Biderman et al., según su abstract). Los dos estudios usan modelos de 2023 y 2024.
> No se encontró un estudio reciente que compare ajustar contra un modelo de punta con buen prompt
> en una tarea de dominio, con costos: la pregunta sigue abierta.

## Por qué entrenar pide mucha más memoria que inferir

Para inferir alcanza con los pesos. Para entrenar hay que guardar además los gradientes (cuánto
mover cada peso) y los estados del optimizador (un historial por peso), y las activaciones de cada
capa. La documentación de Transformers desglosa la cuenta por parámetro, con precisión mixta y el
optimizador Adam:

| Qué se guarda | Bytes por parámetro |
|---|---|
| Pesos (una copia en 16 bits y otra en 32) | 6 |
| Estados de Adam (momento y varianza, en 32 bits) | 8 |
| Gradientes (en 32 bits) | 4 |
| Activaciones | varían "with batch size, sequence length, model depth, and hidden size" |

Sin las activaciones son 18 bytes por parámetro. Con esa cifra, un modelo de 7.000 millones de
parámetros pediría unos 126 GB para pesos, gradientes y optimizador, contra unos 14 GB para inferir
con los pesos en 16 bits, a 2 bytes por parámetro (cuenta de esta base, no cita). La misma página da
un caso medido: "Training a 4B parameter model in mixed precision on a batch size of 16 requires
roughly 85GB of GPU memory". Con un optimizador cuantizado, los estados de Adam bajan a 2 bytes por
parámetro.

> [!IMPORTANT]
> **Las dos cifras que circulan.** Otras cuentas usan 16 bytes por parámetro (2 de pesos, 2 de
> gradientes y 12 del optimizador con la copia en 32 bits), y se atribuyen al paper ZeRO de
> Rajbhandari et al. Con esa cifra, el mismo modelo de 7.000 millones pediría unos 112 GB. La de 18
> bytes sale de la documentación de Transformers, leída; la de 16 no se pudo verificar en el paper,
> del que solo se leyó el abstract. La diferencia está en si los gradientes se guardan en 16 o en 32
> bits. Las dos son estimaciones de orden: la memoria real depende de las activaciones, del tamaño
> de lote y de la implementación.

Lo que la cuenta enseña es que los pesos son la parte chica: el grueso son gradientes y optimizador,
uno por cada parámetro entrenable. Por eso entrenar menos parámetros, que es lo que hacen
[PEFT y LoRA](peft-y-lora.md), baja la memoria tanto, y guardar el modelo congelado en 4 bits
(QLoRA) la baja más. La cuantización para servir el modelo, que es otra cosa, está en
[Inferencia](../Produccion/inferencia.md).

> [!NOTE]
> Sin fuente todavía: las representaciones numéricas (FP32, BF16, FP16, INT8, 4 bits), con sus bits,
> su rango y cuándo desbordan. Huyen las trata en "Numerical Representations" y "Memory Math" del
> cap. 7 (según el índice del libro), que no se leyeron.

## Olvido catastrófico: lo que el modelo pierde al ajustarse

Ajustar un modelo en una tarea puede empeorar lo que hacía bien fuera de ella. Biderman et al.
(TMLR 2024) lo midieron comparando LoRA con el finetuning completo en programación y matemática.
Según su abstract, con configuraciones estándar LoRA "substantially underperforms full finetuning",
pero "forgets less": conserva mejor lo que el modelo hacía fuera del dominio y da salidas más
diversas. El finetuning completo aprende cambios de un rango de 10 a 100 veces mayor que los de una
LoRA típica.

La lectura práctica es que aprender y olvidar vienen juntos: la técnica que más cambia el modelo es
la que más aprende y la que más olvida (lectura de esta base). Por eso el modelo ajustado se mide
con los [evals](../Evaluacion/evals.md) de la tarea y también con casos generales que antes
resolvía.

> [!NOTE]
> Sin fuente todavía: la definición clásica del olvido catastrófico (McCloskey y Cohen, 1989;
> Kirkpatrick et al., 2017) y fuentes sobre cómo mitigarlo (mezclar datos generales, tasa de
> aprendizaje baja). La única fuente leída es Biderman et al., y solo su abstract.

## Lo que el finetuning hace con los datos repetidos

En el experimento de Raschka con LoRA, entrenar dos veces sobre el mismo conjunto empeoró el
resultado, tanto con 50.000 ejemplos como con 1.000; es un solo experimento con un modelo, y se
desarrolla en [Datos para ajustar](datos-para-ajustar.md). Otra variante que el campo usa, seguir
preentrenando el modelo con texto del dominio antes del ajuste supervisado, no tiene fuente en esta
base todavía.

## Qué leer sobre finetuning

Huyen, *AI Engineering*, cap. 7, desde "Memory Bottlenecks" (p. 319) hasta "Quantization" (p. 328)
para la cuenta de memoria, y "Reasons Not to Finetune" (p. 312) para la decisión. Como complemento
verificable, la página ["GPU memory usage"](https://huggingface.co/docs/transformers/model_memory_anatomy)
de la documentación de Transformers: fijarse en que lo que más memoria pide no son los pesos sino los
gradientes y el optimizador, y en que las activaciones crecen con el largo de secuencia y el lote.
