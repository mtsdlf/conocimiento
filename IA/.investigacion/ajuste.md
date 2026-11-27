# Investigación: vertical Ajuste (cambiar los pesos del modelo)

Fecha de la investigación: 2026-11-27. Lector objetivo: programa y conoce APIs, no sabe cómo funciona un modelo por dentro. Perspectiva: Huyen, *AI Engineering* (O'Reilly 2025), cap. 7 y 8, como inspiración.

Convenciones. Marcas de lectura: [L] leído completo, [M] metadatos o abstract, [S] resumen secundario. Puntajes 1 a 3: A = autoridad, P = profundidad, E = ejemplos, U = unicidad; R = recencia (solo en lo volátil). Tipo: P = primaria, S = secundaria. Advertencia de método: las páginas se leyeron con una herramienta que devuelve un resumen del contenido, no el HTML crudo; por eso casi todos los abstracts de arXiv llegaron parafraseados y las únicas citas literales son las que van entre comillas (todas salen de esa herramienta). Lo que quede sin comillas es paráfrasis mía y hay que cotejarlo con la fuente antes de publicarlo como cita.

## Sobre la división de componentes

La división propuesta (finetuning, peft-y-lora, destilacion, datos-para-ajustar, datos-sinteticos) sirve, pero no coincide del todo con cómo parte el campo y el libro:

1. **Huyen no tiene un capítulo de destilación.** "Model Distillation" es una subsección (p. 395) dentro de "Data Augmentation and Synthesis" del cap. 8, es decir, para ella destilar es una forma de sintetizar datos (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md). Pero la destilación original de Hinton (2015) es otra cosa: el alumno aprende de las probabilidades del maestro, no de textos generados. Conviene una nota que distinga las dos y las vincule con `datos-sinteticos`.
2. **Falta un componente: el ajuste de preferencias y por refuerzo (RLHF, DPO, GRPO) y el post-entrenamiento en general.** El campo divide el ajuste en SFT (supervisado), preferencias y refuerzo; TRL lo muestra en su taxonomía de entrenadores: SFT, DPO, KTO, GRPO, RLOO, Reward, y también Knowledge distillation (https://huggingface.co/docs/trl/index). Huyen lo trata solo de pasada (formato de preferencias en cap. 8). Se propone al menos una sección "SFT, preferencias y refuerzo: qué es cada uno" dentro de `finetuning`.
3. **Fusión de modelos y multitarea** en el libro están en "Finetuning Techniques" (pp. 347-357), junto a PEFT; la ubicación en `peft-y-lora` es razonable.
4. **Costo en memoria y representaciones numéricas** son en el libro la sección "Memory Bottlenecks" (pp. 319-332), anterior a las técnicas. Va bien en `finetuning`, pero PEFT y QLoRA no se entienden sin ella: orden de lectura sugerido finetuning, peft-y-lora.
5. **Datos**: el libro agrupa curación, síntesis y procesamiento en un solo capítulo; separar `datos-para-ajustar` y `datos-sinteticos` está bien si el segundo se cuida de no repetir la verificación de calidad.
6. Un hueco de alcance: el pre-entrenamiento continuado (seguir entrenando con texto del dominio) no figura en los componentes y es una alternativa entre prompt y SFT.

Estructura del libro, literal (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md [L, vía resumen de la herramienta]): cap. 7 "Finetuning Overview (308), When to Finetune (311) [Reasons to Finetune (311), Reasons Not to Finetune (312), Finetuning and RAG (316)], Memory Bottlenecks (319) [Backpropagation and Trainable Parameters (320), Memory Math (322), Numerical Representations (325), Quantization (328)], Finetuning Techniques (332) [Parameter-Efficient Finetuning (333), Model Merging and Multi-Task Finetuning (347), Finetuning Tactics (357)]". Cap. 8: "Data Curation (365) [Data Quality (368), Data Coverage (370), Data Quantity (372), Data Acquisition and Annotation (377)], Data Augmentation and Synthesis (380) [Why Data Synthesis (381), Traditional Data Synthesis Techniques (383), AI-Powered Data Synthesis (386), Model Distillation (395)], Data Processing (396) [Inspect Data (397), Deduplicate Data (399), Clean and Filter Data (401), Format Data (401)]".

## Lo que ya existe en la base y no se repite

La nota `IA/prompt-rag-o-finetuning.md` ya cubre: la escalera prompt, RAG, fine-tuning; el diagnóstico "falta conocimiento o falla el comportamiento" (guía de OpenAI "Optimizing LLM accuracy"); cuándo vale la pena según OpenAI (más ejemplos que los que entran en el prompt, prompts más cortos, modelo chico y barato); la destilación en una frase (prompt en modelo grande, guardar salidas, afinar uno chico); "finetuning is easy, but getting data for finetuning is hard"; y avisa que al menos un proveedor está cerrando su plataforma. Su propio aviso de hueco: nunca se leyó el texto del cap. 7 ni una guía vigente de otros proveedores. Esa nota remite a `Produccion/plataformas-de-ia.md` para el estado por proveedor; esta investigación trae el estado fechado y se cruzará con esa nota al escribir. Lo que sigue trae lo que falta.

---

## Componente 1: finetuning

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| Huyen, resúmenes de capítulos | https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | S | 2 | 1 | 1 | 1 | - | [L] |
| Huyen, índice | https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md | S | 2 | 1 | 1 | 1 | - | [L] |
| Hugging Face, "GPU memory usage" (docs de Transformers) | https://huggingface.co/docs/transformers/model_memory_anatomy | P | 3 | 2 | 2 | 3 | 3 | [L] |
| Biderman et al. 2024, "LoRA Learns Less and Forgets Less" (TMLR) | https://arxiv.org/abs/2405.09673 | P | 3 | 2 | 2 | 3 | - | [M] |
| OpenAI, guía de optimización de modelos | https://developers.openai.com/api/docs/guides/model-optimization | P | 3 | 2 | 1 | 3 | 3 | [L] |
| OpenAI, deprecaciones | https://developers.openai.com/api/docs/deprecations | P | 3 | 2 | 1 | 3 | 3 | [L] |
| OpenAI, destilación | https://developers.openai.com/api/docs/guides/distillation | P | 3 | 2 | 1 | 2 | 3 | [L] |
| Google, ajuste en Vertex AI | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models | P | 3 | 2 | 1 | 3 | 3 | [L] |
| Google, guía de ajuste de la Gemini API | https://ai.google.dev/docs/model_tuning_guidance | P | 3 | 1 | 1 | 3 | 2 | [S] (solo vista en resultados de búsqueda) |
| AWS/Anthropic, ajuste de Claude 3 Haiku en Bedrock | https://www.anthropic.com/news/fine-tune-claude-3-haiku-ga | P | 3 | 1 | 1 | 3 | 1 | [S] (solo vista en resultados de búsqueda) |
| Hugging Face TRL, inicio | https://huggingface.co/docs/trl/index | P | 3 | 1 | 1 | 2 | 3 | [L] |
| Husain, "Your AI product needs evals" | https://hamel.dev/blog/posts/evals/ | S | 2 | 2 | 2 | 2 | 2 | [L] |
| Raschka, "Practical tips for finetuning LLMs using LoRA" | https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms | S | 2 | 3 | 3 | 2 | 1 | [L] |

### Afirmaciones

**Qué es y cómo es el reparto del trabajo.**
- El resumen del cap. 7 dice: "The process of finetuning itself isn't hard." Y cierra: "finetuning is easy, but getting data for finetuning is hard." (https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md)
- Husain, en la misma línea: "99% of the labor involved with fine-tuning is assembling high-quality data that covers your AI product's surface area." Y: "Fine-tuning is best for learning syntax, style, and rules." (https://hamel.dev/blog/posts/evals/)

**Razones para no hacerlo (lo que falta respecto de la nota existente).**
- El cap. 7 separa "Reasons to Finetune" (p. 311), "Reasons Not to Finetune" (p. 312) y "Finetuning and RAG" (p. 316) (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md). El texto de esas secciones NO se leyó: hueco declarado más abajo.
- Dato nuevo para el costo de oportunidad: el proveedor puede retirar el modelo base. Los modelos afinados en OpenAI "follow the same shutdown schedule as their underlying base models" (https://developers.openai.com/api/docs/deprecations). Es la razón práctica más fuerte hoy para no afinar un modelo cerrado.

**Costo en memoria: por qué entrenar pide mucho más que inferir.**
- Según la documentación de Transformers: "Training a 4B parameter model in mixed precision on a batch size of 16 requires roughly 85GB of GPU memory." (https://huggingface.co/docs/transformers/model_memory_anatomy)
- Desglose por parámetro, de la misma página: pesos en precisión mixta, "This equates to 6 bytes per parameter" (una copia fp16 de 2 bytes y una fp32 de 4); estados de Adam (momento y varianza, fp32), "an additional 8 bytes per parameter"; gradientes en fp32, "4 bytes per parameter"; y las activaciones "vary in size with batch size, sequence length, model depth, and hidden size". Con Adam cuantizado de bitsandbytes los estados bajan a 2 bytes por parámetro. (https://huggingface.co/docs/transformers/model_memory_anatomy)
- Cuenta aproximada (aritmética mía sobre esas cifras, no cita): 6 + 8 + 4 = 18 bytes por parámetro sin contar activaciones; un modelo de 7.000 millones de parámetros serían unos 126 GB solo de pesos, gradientes y optimizador, contra unos 14 GB para inferir en 16 bits (2 bytes por parámetro, dato de las representaciones numéricas, ver abajo). Otras cuentas usan 16 bytes por parámetro (2 de pesos, 2 de gradientes, 12 de optimizador y copia fp32); esa cifra viene del paper ZeRO (https://arxiv.org/abs/1910.02054) pero NO se pudo verificar: la página de arXiv es solo el abstract y el PDF no se pudo leer. Discrepancia a presentar como rango y marcar la cuenta como estimación.
- El libro tiene "Memory Math (322)" y "Backpropagation and Trainable Parameters (320)" (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md); texto no leído.

**Representaciones numéricas y cuantización, solo lo del ajuste.**
- El libro las trata en "Numerical Representations (325)" y "Quantization (328)" (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md); texto no leído.
- Lo verificado: la precisión mixta guarda dos copias de los pesos (fp16 y fp32) (https://huggingface.co/docs/transformers/model_memory_anatomy); y QLoRA usa un tipo de 4 bits llamado NF4 (ver componente 2). Las definiciones de FP32, BF16, FP16, INT8 (bits, rango, cuándo desborda) quedan como hueco: no hay fuente leída para ellas.

**Olvido catastrófico.**
- Biderman et al. comparan LoRA y ajuste completo en código y matemática; en configuración estándar LoRA "substantially underperforms full finetuning", pero "forgets less", preserva mejor lo que el modelo hacía fuera del dominio y da salidas más diversas. El ajuste completo aprende perturbaciones de rango 10 a 100 veces mayor que las configuraciones típicas de LoRA. (https://arxiv.org/abs/2405.09673; resumen de la herramienta, citas cortas.)
- Sobre el olvido hay una sola fuente leída (esta). Falta una primaria sobre la definición clásica (McCloskey y Cohen, 1989; Kirkpatrick 2017): hueco.

**Servicios de finetuning de los proveedores (estado al 2026-11-27).**
- OpenAI. La página de deprecaciones fija tres etapas: 7 de mayo de 2026, "Organizations that have never run a fine-tuning job can no longer create one."; 2 de julio de 2026, "Organizations that haven't run inference on a fine-tuned model in the past 60 days can no longer create training jobs."; 15 de diciembre de 2026, "Starting on this date, no organization can create new self-serve fine-tuning jobs." La página aclara que el corte se adelantó: "We're moving that cutoff up to December 15, 2026". Y: "You can continue to run inference on each existing fine-tuned model until OpenAI retires its underlying base model." (https://developers.openai.com/api/docs/deprecations)
- Discrepancia: resultados de búsqueda y notas de prensa (https://ypyl.github.io/news/2026/05/12/openai-winds-down-fine-tuning-platform.html, [S], no leída) daban como fecha final el 6 de enero de 2027, que es el corte anterior a la corrección. Vale la fecha de la página oficial: 15 de diciembre de 2026. La guía de OpenAI dice también que "The platform is no longer accessible to new users." (https://developers.openai.com/api/docs/guides/model-optimization)
- Modelos y métodos que OpenAI aún lista: SFT y DPO con gpt-4.1, gpt-4.1-mini y gpt-4.1-nano (versiones 2025-04-14); visión con gpt-4o-2024-08-06 (https://developers.openai.com/api/docs/guides/model-optimization). Cierres de base: gpt-4.1-nano el 23 de octubre de 2026; gpt-4.1 y gpt-4.1-mini el 14 de enero de 2027, con sus versiones afinadas (https://developers.openai.com/api/docs/guides/distillation). Una respuesta de personal de OpenAI en el foro (no verificada contra página oficial, [S]) dice que no se quita el ajuste como tal y que la familia GPT-5 no figura como base afinable (https://community.openai.com/t/deprecation-of-fine-tuned-models-but-still-cant-access-newer-ones/1379550).
- Google. La página de Vertex AI lista SFT para Gemini 3.5 Flash-Lite, 3.5 Flash, 3.1 Flash-Lite, 2.5 Pro, 2.5 Flash-Lite y 2.5 Flash; ajuste por preferencias solo en 2.5 Flash-Lite y 2.5 Flash; ajuste por refuerzo solo en 3.5 Flash y 3.1 Flash-Lite. Describe el ajuste eficiente como uno que "updates a relatively small subset of the model's parameters". (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models) En la Gemini API (la de desarrolladores), la guía oficial dice que el ajuste se perdió al deprecarse Gemini 1.5 Flash-001 en mayo de 2025 y recomienda Vertex AI (https://ai.google.dev/docs/model_tuning_guidance, vista solo en el resultado de búsqueda [S]). Discrepancia: un hilo de foro de mayo de 2026 decía que ningún Gemini 3.x admitía SFT (https://discuss.google.dev/t/when-will-supervised-fine-tuning-be-available-for-gemini-3-x-models-on-vertex-ai/346487, [S]); la página oficial leída hoy ya lista 3.x. Vale la página oficial. Hay también fechas de cierre contradictorias en foros para gemini-2.5-pro (17 de junio o 17 de octubre de 2026); la tabla oficial de deprecaciones (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations) no se leyó: hueco.
- Anthropic. El ajuste de Claude 3 Haiku en Amazon Bedrock pasó de vista previa (julio de 2024) a disponibilidad general el 1 de noviembre de 2024 (https://aws.amazon.com/about-aws/whats-new/2024/11/fine-tuning-anthropics-claude-3-haiku-amazon-bedrock, [S] por resultado de búsqueda). Un aviso en el blog de AWS dice que Claude 3 Haiku llegó al fin de vida el 10 de septiembre de 2026 (https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality, [S]). No se encontró ajuste vigente para modelos Claude posteriores en la API de Anthropic: hueco, no afirmar que no existe.
- Hugging Face TRL, la herramienta para quien ajusta por su cuenta: SFT, DPO, GRPO, reward modeling y destilación en la misma librería, con un v1.0 anunciado el 31 de marzo de 2026 (https://huggingface.co/docs/trl/index).

**Ajustes prácticos (Raschka, secundaria, un solo experimento con un modelo y un conjunto de datos).**
- QLoRA redujo la memoria de 21,33 GB a 14,18 GB (cerca de 33 %) y subió el tiempo de entrenamiento de 1,85 h a 2,79 h (cerca de 39 %), con poco efecto en el rendimiento. Duplicar las iteraciones sobre Alpaca de 50.000 ejemplos (unas 2 épocas) bajó el rendimiento, y lo mismo con LIMA de 1.000 ejemplos. (https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms)

### Recurso canónico
Huyen, cap. 7, desde "Memory Bottlenecks" (p. 319) hasta "Quantization" (p. 328) para la cuenta de memoria, y "Reasons Not to Finetune" (p. 312). Complemento operativo y verificable: la página "GPU memory usage" de Transformers, por el desglose bytes por parámetro. Fijarse en que lo que más memoria pide no son los pesos sino los gradientes y los estados del optimizador, y en que las activaciones dependen del largo de secuencia y del lote. Para el estado de los proveedores, la página de deprecaciones de OpenAI, que es la que trae fechas.

---

## Componente 2: peft-y-lora

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| Hu et al. 2021, LoRA | https://arxiv.org/abs/2106.09685 | P | 3 | 3 | 2 | 3 | - | [M] |
| Dettmers et al. 2023, QLoRA | https://arxiv.org/abs/2305.14314 | P | 3 | 3 | 2 | 3 | - | [M] |
| Houlsby et al. 2019, adapters | https://arxiv.org/abs/1902.00751 | P | 3 | 2 | 1 | 3 | - | [M] |
| Lester et al. 2021, prompt tuning | https://arxiv.org/abs/2104.08691 | P | 3 | 2 | 1 | 3 | - | [M] |
| Sheng et al. 2023, S-LoRA | https://arxiv.org/abs/2311.03285 | P | 3 | 2 | 1 | 3 | - | [M] |
| Chen et al. 2023, Punica | https://arxiv.org/abs/2310.18547 | P | 3 | 2 | 1 | 2 | - | [M] |
| Ilharco et al. 2022, task arithmetic | https://arxiv.org/abs/2212.04089 | P | 3 | 2 | 1 | 3 | - | [M] |
| Yang et al., survey de fusión de modelos | https://arxiv.org/abs/2408.07666 | P (survey) | 2 | 2 | 1 | 3 | 2 | [M] |
| Hugging Face PEFT, inicio | https://huggingface.co/docs/peft/index | P | 3 | 1 | 1 | 2 | 3 | [L] |
| Hugging Face PEFT, guía conceptual de LoRA | https://huggingface.co/docs/peft/main/en/conceptual_guides/lora | P | 3 | 2 | 3 | 2 | 3 | [L] |
| Biderman et al. 2024 | https://arxiv.org/abs/2405.09673 | P | 3 | 2 | 2 | 3 | - | [M] |

### Afirmaciones

**Idea general de PEFT.**
- La documentación de PEFT: los métodos "only fine-tune a small number of (extra) model parameters - significantly decreasing computational and storage costs - while yielding performance comparable to a fully fine-tuned model." (https://huggingface.co/docs/peft/index) El resumen del libro: "PEFT reduces finetuning's memory requirements by reducing the number of trainable parameters." (https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md)
- La familia, con fechas: adapters (Houlsby et al., 2 de febrero de 2019): módulos chicos entrenables con los pesos originales congelados; en BERT sobre GLUE quedan a 0,4 % del ajuste completo con "3.6% parameters per task" (https://arxiv.org/abs/1902.00751). Prompt tuning o soft prompts (Lester et al., 18 de abril de 2021): vectores aprendidos por retropropagación con el modelo congelado; "se vuelve más competitivo con el tamaño" y pasado el mil millones de parámetros casi iguala al ajuste completo (https://arxiv.org/abs/2104.08691, paráfrasis de la herramienta). Un soft prompt no es un prompt en texto: es una secuencia de números que no se puede leer ni editar; aclararlo a quien viene de las APIs. Prefix tuning aparece solo como "a simplified version" citada por Lester; el paper original de Li y Liang 2021 no se leyó.

**LoRA.**
- Hu et al., 17 de junio de 2021: frente a GPT-3 175B ajustado con Adam, LoRA reduce los parámetros entrenables "10,000 times" y la memoria de GPU "3 times". (https://arxiv.org/abs/2106.09685, herramienta; el abstract completo no se pudo citar.)
- Cómo funciona, según la guía de PEFT: representa la actualización con dos matrices chicas por descomposición de bajo rango; "The original weight matrix remains frozen and doesn't receive any further adjustments." El parámetro `r` es el rango; "Lower rank results in smaller update matrices with fewer trainable parameters"; la escala es `lora_alpha/r` (con rsLoRA, `lora_alpha/math.sqrt(r)`). Después del entrenamiento los pesos se pueden fusionar: "the weights can actually be merged into a new weight matrix that is identical", con `merge_and_unload()`, lo que quita la latencia extra al servir. (https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)
- Servir varios: como los pesos base se comparten, "you can have multiple lightweight and portable LoRA models for various downstream tasks built on top of them"; `add_weighted_adapter()` combina varios LoRA. (https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)
- Costo real de LoRA frente al completo: "LoRA Learns Less and Forgets Less" (ver componente 1): con rangos estándar rinde menos que el ajuste completo en código y matemática, y olvida menos. (https://arxiv.org/abs/2405.09673)
- Consejos de Raschka (un solo experimento): no halló una regla para el rango; su mejor resultado fue con r=256; alpha igual a 2 veces el rango es un "sweet spot" con r=8 (alpha=16); aplicar LoRA a todas las capas subió los parámetros entrenables de 4.194.304 a 20.277.248 y la memoria de 14,18 GB a 16,62 GB. El propio artículo es inconsistente sobre el mejor alpha (128 en un experimento, 512 en la lista de mejores); presentar las dos cifras si se cita. (https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms)

**QLoRA.**
- Dettmers et al., 23 de mayo de 2023: ajustar un modelo de 65.000 millones de parámetros en una sola GPU de 48 GB sin perder rendimiento frente al ajuste en 16 bits, retropropagando a través de un modelo congelado en 4 bits hacia adaptadores de bajo rango; trucos: NF4 (4-bit NormalFloat), doble cuantización y optimizadores paginados; sus modelos Guanaco llegan al "99.3%" de ChatGPT en el benchmark de Vicuna tras 24 horas de ajuste en una GPU. (https://arxiv.org/abs/2305.14314, paráfrasis de la herramienta.) Aclarar al lector que 4 bits describe cómo se guardan los pesos congelados; los adaptadores se entrenan en mayor precisión (inferencia mía a partir de "backpropagates through a frozen, 4-bit quantized model into low-rank adapters", falta cotejar en el texto).

**Servir varios LoRA.**
- S-LoRA (Sheng et al., 6 de noviembre de 2023): guarda todos los adaptadores en memoria principal y pasa a la GPU solo los de las consultas en curso; "Unified Paging"; puede servir miles de adaptadores con hasta 4 veces más rendimiento que PEFT de Hugging Face y el soporte básico de LoRA de vLLM (https://arxiv.org/abs/2311.03285). Punica (28 de octubre de 2023): un kernel que agrupa operaciones de distintos LoRA para guardar una sola copia del modelo base, hasta 12 veces más rendimiento y unos 2 ms de latencia extra por token (https://arxiv.org/abs/2310.18547). Cifras de los autores, no replicadas.

**Fusión de modelos y multitarea.**
- Objetivo según el libro: combinar varios modelos "into one model that works better than these models separately" (https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md).
- Task arithmetic (Ilharco et al., 8 de diciembre de 2022): un "vector de tarea" es la diferencia entre los pesos preentrenados y los ajustados; sumarlos o negarlos cambia el comportamiento; "a simple, efficient and effective way of editing models" (https://arxiv.org/abs/2212.04089). Survey con taxonomía de métodos y aplicaciones en LLM, revisado hasta el 31 de diciembre de 2025 (https://arxiv.org/abs/2408.07666). Los métodos concretos (promedio de pesos o "model soups", TIES, DARE, SLERP) no se leyeron: hueco.

### Recurso canónico
Hu et al. 2021, secciones de introducción y del método (dónde se inserta la actualización de bajo rango y por qué no agrega latencia), emparejado con la guía conceptual de LoRA de PEFT (la parte de fusionar y de adaptadores múltiples) y con el abstract de QLoRA para el truco de memoria. Fijarse en que LoRA no entrena menos "inteligencia" sino menos parámetros, y que paga con menos capacidad de aprender y de olvidar (Biderman et al.).

---

## Componente 3: destilacion

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| Hinton, Vinyals y Dean 2015 | https://arxiv.org/abs/1503.02531 | P | 3 | 3 | 2 | 3 | - | [M] |
| Stanford CRFM, Alpaca | https://crfm.stanford.edu/2023/03/13/alpaca.html | P | 3 | 2 | 3 | 3 | - | [M] (resumen de la herramienta) |
| DeepSeek-AI, DeepSeek-R1 (arXiv, Nature 645) | https://arxiv.org/abs/2501.12948 | P | 3 | 2 | 2 | 3 | 3 | [M] |
| DeepSeek-R1, repositorio y licencias | https://github.com/deepseek-ai/DeepSeek-R1 | P | 3 | 1 | 3 | 2 | 3 | [M] |
| OpenAI, destilación | https://developers.openai.com/api/docs/guides/distillation | P | 3 | 2 | 1 | 2 | 3 | [L] |
| OpenAI, términos de uso | https://openai.com/policies/terms-of-use/ | P | 3 | 1 | 1 | 3 | 3 | [M] (cita de una cláusula) |
| TRL, entrenadores de destilación | https://huggingface.co/docs/trl/index | P | 3 | 1 | 1 | 2 | 3 | [L] |
| Huyen, índice (p. 395) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md | S | 2 | 1 | 1 | 1 | - | [L] |

### Afirmaciones

- Origen (Hinton, Vinyals y Dean, 9 de marzo de 2015): un conjunto de modelos es incómodo de desplegar; se puede comprimir su conocimiento en un solo modelo, y los autores muestran que destilar un conjunto mejora un modelo acústico comercial. (https://arxiv.org/abs/1503.02531, paráfrasis de la herramienta.) El mecanismo que da nombre al paper (entrenar al alumno con las probabilidades suaves del maestro, con temperatura) NO figura en el abstract y no se leyó el texto: hueco, y es justo lo que más importa para no confundirlo con "entrenar con textos del modelo grande".
- Lo que se llama destilar hoy en el ajuste de LLM suele ser lo segundo: generar datos con el modelo grande y entrenar al chico. El flujo oficial de OpenAI: afinar el prompt en un modelo mayor (gpt-4.1) hasta pasar las evaluaciones, capturar las respuestas ("Responses API stores model responses for 30 days by default"), filtrar las que cumplen, y afinar un modelo menor (gpt-4.1-mini). (https://developers.openai.com/api/docs/distillation) Esa misma plataforma está en retirada (ver componente 1: cierre el 15 de diciembre de 2026).
- Alpaca (Stanford, 13 de marzo de 2023): LLaMA 7B afinado con 52.000 demostraciones generadas por text-davinci-003 a partir de 175 pares escritos a mano, con el método Self-Instruct; la generación costó menos de 500 dólares y el ajuste unas 3 horas en 8 GPU A100 de 80 GB (menos de 100 dólares). (https://crfm.stanford.edu/2023/03/13/alpaca.html, resumen de la herramienta.) Ejemplo canónico también de la restricción: "Alpaca is intended only for academic research" y "any commercial use is prohibited", con tres razones: licencia no comercial de LLaMA, los términos de OpenAI, y falta de medidas de seguridad. (mismo URL)
- Restricción de términos de uso, literal: entre lo que no se puede hacer figura "Use Output to develop models that compete with OpenAI." (https://openai.com/policies/terms-of-use/) Las cláusulas equivalentes de Anthropic, Google y las licencias de los modelos abiertos (Llama) no se leyeron: hueco. No dar consejo legal; decir que hay que leer los términos vigentes de cada proveedor.
- DeepSeek-R1: el paper (22 de enero de 2025; publicado en Nature 645, pp. 633-638, 2025) dice que los patrones de razonamiento de los modelos grandes se pueden transferir a modelos chicos (https://arxiv.org/abs/2501.12948). El repositorio lista seis modelos destilados (Qwen 1.5B, 7B, 14B, 32B; Llama 8B y 70B), los Qwen "now finetuned with 800k samples curated with DeepSeek-R1", con el código y pesos bajo MIT pero cada base conserva su licencia (Apache 2.0 para Qwen 2.5; licencias Llama 3.1 y Llama 3.3). (https://github.com/deepseek-ai/DeepSeek-R1) Buen ejemplo de que la licencia de la destilación hereda la de la base. Que sea SFT sobre muestras y no destilación de probabilidades es lo que dice el repositorio ("finetuned with 800k samples"), y vale aclararlo.
- Herramientas: TRL incluye en su taxonomía un `DistillationTrainer` estable y varios experimentales (GKD, GOLD, entre otros), y publicó "Distilling 100B+ Models 40x Faster with TRL" (12 de abril de 2026) (https://huggingface.co/docs/trl/index; el post no se leyó).
- En el libro, la destilación está en p. 395, dentro de síntesis de datos (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md); el resumen del cap. 8 no la menciona y aparece en el resumen del cap. 9 como técnica de optimización (https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md, según la herramienta).

### Recurso canónico
Hinton, Vinyals y Dean 2015 (secciones sobre probabilidades suaves y temperatura) para el qué es; la guía de destilación de OpenAI para el flujo práctico (con la salvedad de la fecha de cierre); y la página de Alpaca como caso con costo y restricción de licencia. Fijarse en dos cosas: qué se le enseña al alumno (probabilidades o solo textos) y de quién son los términos que limitan el uso de las salidas.

---

## Componente 4: datos-para-ajustar

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| Zhou et al. 2023, LIMA | https://arxiv.org/abs/2305.11206 | P | 3 | 3 | 2 | 3 | - | [M] |
| Lee et al. 2021, deduplicación | https://arxiv.org/abs/2107.06499 | P | 3 | 2 | 2 | 3 | - | [M] |
| Li y Flanigan 2023, contaminación de tareas | https://arxiv.org/abs/2312.16337 | P | 3 | 2 | 2 | 3 | - | [M] |
| Huyen, resúmenes (cap. 8) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | S | 2 | 1 | 1 | 1 | - | [L] |
| Huyen, índice (cap. 8) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md | S | 2 | 1 | 1 | 1 | - | [L] |
| Husain, evals | https://hamel.dev/blog/posts/evals/ | S | 2 | 2 | 2 | 2 | 2 | [L] |
| TRL, formatos de datos (guía conceptual) | https://huggingface.co/docs/trl/index | P | 3 | 1 | 1 | 2 | 3 | [S] (solo el índice) |
| OpenAI, guía de optimización (formato, cantidad) | https://developers.openai.com/api/docs/guides/model-optimization | P | 3 | 2 | 1 | 2 | 3 | [L] |

### Afirmaciones

- Tres criterios para cualquier fase: "dataset design across training phases shares the same three core criteria: quality, coverage, and quantity." Y: "A small amount of high-quality data can outperform a large amount of noisy data." Se empieza pensando "the behaviors you want your model to learn". (https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md)
- LIMA (Zhou et al., 18 de mayo de 2023): LLaMA de 65.000 millones de parámetros, SFT estándar con solo 1.000 pares prompt-respuesta curados, sin refuerzo ni modelo de preferencias; sus respuestas fueron iguales o preferidas a las de GPT-4 en 43 % de los casos en un estudio humano; la conclusión citada: "almost all knowledge in large language models is learned during pretraining". (https://arxiv.org/abs/2305.11206, herramienta.) El término "Superficial Alignment Hypothesis" no aparece en el abstract, sí en el cuerpo del paper según mi conocimiento previo: no verificado. Advertencia para el lector: el resultado es sobre estilo y formato en modelos grandes y ya preentrenados, no autoriza a esperar que mil ejemplos enseñen conocimiento nuevo.
- Cantidad, con contrapunto: OpenAI pide empezar con 50 ejemplos o más y dice "Quality of training data is more important than quantity" (citado en la nota existente; https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy); Raschka vio que más épocas sobre 1.000 y 50.000 ejemplos empeoraban (https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms). Dos fuentes que no discrepan sino que acotan: poca cantidad si es buena, y no repetirla de más.
- Inspección: "You must remove all friction from the process of looking at data." y "You can never stop looking at data—no free lunch exists." (https://hamel.dev/blog/posts/evals/)
- Deduplicación (Lee et al., 14 de julio de 2021, ACL 2022): los conjuntos populares tienen muchos casi-duplicados; más de 1 % de la salida sin guía de los modelos entrenados con ellos se copia del entrenamiento; una oración aparecía más de 60.000 veces en C4; deduplicar reduce la memorización y necesita menos pasos; encontraron solapamiento entre entrenamiento y prueba en más de 4 % de los conjuntos de validación estándar. (https://arxiv.org/abs/2107.06499, herramienta.) Es sobre preentrenamiento; extenderlo al ajuste es inferencia razonable, no hallazgo del paper.
- Contaminación con datos de evaluación: Li y Flanigan (26 de diciembre de 2023, AAAI 2024) encuentran que los modelos rinden mejor en conjuntos publicados antes de la recolección de sus datos de entrenamiento y lo llaman "task contamination"; en tareas que no pudieron estar contaminadas, los LLM rara vez superan significativamente al baseline de la clase mayoritaria. (https://arxiv.org/abs/2312.16337, herramienta.) Para el lector: separar el conjunto de evaluación antes de armar los datos y buscar solapamiento con los datos de ajuste.
- Formatos: el libro tiene "Format Data (401)" (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md), no leído. El catálogo de formatos de TRL (instrucción-respuesta, conversación, preferencias) está solo anunciado como "dataset formats" en su sección de guías conceptuales (https://huggingface.co/docs/trl/index): sin lectura de la página de formatos. Hueco.
- Anotación y guías ("Data Acquisition and Annotation", p. 377): sin lectura. Hueco.
- Costo oculto: el resumen del cap. 7 insiste en que juntar los datos es lo difícil, y Husain cuenta que el sistema de evaluación puede reutilizarse como filtro de datos sintéticos: "Tests and assertions" descartan ejemplos y las críticas del evaluador ayudan a curar (https://hamel.dev/blog/posts/evals/, paráfrasis de la herramienta salvo la cita de arriba).

### Recurso canónico
Huyen, cap. 8, "Data Curation" (pp. 365-380) para los tres criterios y "Data Processing" (pp. 396-401) para inspección, deduplicación y filtrado; LIMA completo (secciones de construcción del conjunto de 1.000 ejemplos y de análisis) como el caso que cambia la intuición sobre cantidad. Fijarse en qué hizo el equipo de LIMA para asegurar diversidad con tan pocos ejemplos, y en que el resultado se refiere a estilo, no a conocimiento.

---

## Componente 5: datos-sinteticos

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| Wang et al. 2022, Self-Instruct | https://arxiv.org/abs/2212.10560 | P | 3 | 3 | 2 | 3 | - | [M] |
| Xu et al. 2023, WizardLM / Evol-Instruct (ICLR 2024) | https://arxiv.org/abs/2304.12244 | P | 3 | 2 | 2 | 3 | - | [M] |
| Bai et al. 2022, Constitutional AI | https://arxiv.org/abs/2212.08073 | P | 3 | 3 | 2 | 3 | - | [M] |
| Gunasekar et al. 2023, phi-1 | https://arxiv.org/abs/2306.11644 | P | 3 | 2 | 2 | 3 | - | [M] |
| Shumailov et al., Nature 631 (2024) | https://www.nature.com/articles/s41586-024-07566-y | P | 3 | 3 | 2 | 3 | - | [S] (no cargó: acceso por redirección; abstract vía resultados de búsqueda) |
| Shumailov et al., versión arXiv | https://arxiv.org/abs/2305.17493 | P | 3 | 2 | 2 | 2 | - | [M] |
| Gerstgrasser et al. 2024 | https://arxiv.org/abs/2404.01413 | P | 3 | 3 | 2 | 3 | - | [M] |
| Huyen, resúmenes (cap. 8) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | S | 2 | 1 | 1 | 1 | - | [L] |
| Husain, evals | https://hamel.dev/blog/posts/evals/ | S | 2 | 2 | 2 | 2 | 2 | [L] |

### Afirmaciones

- Por qué y cuándo: el libro sostiene que la síntesis se volvió práctica cuando la IA pudo generar datos realistas y complejos; "Just like real data, synthetic data must be evaluated to ensure its quality before being used to train models." Y: "It's hard to automate data generation, but it's even harder to automate verifying it." (https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md) El índice divide en "Why Data Synthesis (381)", técnicas tradicionales (383) y con IA (386).
- Self-Instruct (Wang et al., 20 de diciembre de 2022): el modelo genera sus propias instrucciones, entradas y salidas; se filtran las inválidas o parecidas; se ajusta con ellas. Con GPT-3 base dio "a 33% absolute improvement" en Super-NaturalInstructions, comparable a InstructGPT-001, y queda "a 5% absolute gap" por detrás de InstructGPT-001 en evaluación humana. (https://arxiv.org/abs/2212.10560)
- Evol-Instruct (Xu et al., 24 de abril de 2023): partir de instrucciones semilla y reescribirlas "step by step into more complex instructions" con un LLM; ajustar LLaMA con la mezcla (WizardLM); evaluadores humanos prefirieron las instrucciones evolucionadas a las escritas por humanos; GPT-4 como juez: más de 90 % de la capacidad de ChatGPT en 17 de 29 habilidades. (https://arxiv.org/abs/2304.12244)
- Constitutional AI (Bai et al., 15 de diciembre de 2022): una fase supervisada en que el modelo critica y revisa sus respuestas y se ajusta con las revisiones, y una fase de refuerzo con preferencias generadas por IA (RLAIF); resultado: un asistente inofensivo pero "non-evasive" con muchas menos etiquetas humanas. (https://arxiv.org/abs/2212.08073) Es síntesis de datos para alineación, no solo para capacidades.
- Síntesis para capacidades: phi-1 (20 de junio de 2023), 1.300 millones de parámetros, entrenado 4 días en 8 A100 con unos 6.000 millones de tokens de web "de calidad de libro de texto" y unos 1.000 millones de tokens de libros y ejercicios sintéticos generados con GPT-3.5; 50,6 % pass@1 en HumanEval y 55,5 % en MBPP. (https://arxiv.org/abs/2306.11644)
- Verificación: la verificación no es un componente aparte en ninguno de los papers leídos; el libro la pone como el punto difícil. Ejemplos concretos de verificadores que no se leyeron en fuente propia: ejecución de código y tests unitarios, resultado comprobable en matemática, juez de IA. Es un hueco para el informe de la nota: fuente primaria sobre verificación y filtrado de sintéticos. Husain sugiere reutilizar tests y aserciones del sistema de evaluación (https://hamel.dev/blog/posts/evals/). DeepSeek-R1 usa recompensas verificables (matemática, código) según su abstract: "performs strongly on verifiable tasks in mathematics, coding competitions, and STEM fields" (https://arxiv.org/abs/2501.12948, paráfrasis de la herramienta).
- Colapso de modelos: Shumailov et al., *Nature* 631, 755-759 (2024), DOI 10.1038/s41586-024-07566-y: el entrenamiento con contenido generado por modelos produce un proceso degenerativo en que los modelos "forget the true underlying data distribution"; se pierden primero las colas raras de la distribución y después las salidas convergen a una varianza muy chica; se observa en mezclas gaussianas, autoencoders variacionales y LLM. (https://www.nature.com/articles/s41586-024-07566-y; la página no cargó, la cita viene del texto recuperado por búsqueda, y existe una corrección de autor: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11981929/, no leída.) La versión de arXiv se titulaba "The Curse of Recursion: Training on Generated Data Makes Models Forget", 27 de mayo de 2023 (https://arxiv.org/abs/2305.17493).
- Discusión sobre si se evita mezclando: Gerstgrasser et al. (1 de abril de 2024) encuentran que reemplazar los datos reales por los sintéticos de cada generación lleva al colapso, mientras que acumular los sintéticos junto con los reales lo evita, con distintos tamaños, arquitecturas e hiperparámetros; en un marco lineal simplificado demuestran que el error de prueba queda acotado al acumular y crece al reemplazar. (https://arxiv.org/abs/2404.01413) Lectura honesta: no es contradicción sino dos supuestos (reemplazar contra acumular). Una nota crítica de terceros sobre Shumailov se anuncia en https://arxiv.org/pdf/2410.12954, que apareció solo como resultado de búsqueda y no se leyó: hueco. Todas las lecturas de este punto son de abstract; la fuerza de la conclusión en LLM grandes es discutible y sin revisión adicional de mi parte.
- Estado del arte sin revisión por pares: no se buscó un preprint reciente específico sobre datos sintéticos a gran escala (2025-2026); declarado como hueco.

### Recurso canónico
Huyen, cap. 8, "Data Augmentation and Synthesis" (pp. 380-396) como mapa, con Self-Instruct (secciones del proceso de generación y filtrado) como el mecanismo mínimo, y Gerstgrasser et al. junto con Shumailov et al. leídos como par. Fijarse en qué se mide como "colapso" (pérdida de las colas de la distribución) y bajo qué supuesto (reemplazar o acumular), y en que el filtrado entre generaciones es lo que el flujo de Self-Instruct hace de forma explícita.

---

## Huecos

1. Texto del cap. 7 y 8 de Huyen: solo se leyeron el índice y los resúmenes. No hay lectura de "Reasons Not to Finetune", "Memory Math", "Numerical Representations", "Finetuning Tactics", "Data Acquisition and Annotation" ni "Format Data".
2. Representaciones numéricas (FP32, BF16, FP16, INT8, 4 bits): sin fuente primaria leída; solo la mención de fp16/fp32 en la página de memoria de Hugging Face y NF4 en QLoRA. Hay que sumar una fuente (por ejemplo la documentación de cuantización de Transformers o bitsandbytes) antes de explicarlas.
3. Cuenta de memoria: la cifra de 16 bytes por parámetro (ZeRO) no se pudo verificar; la de 18 bytes (6+8+4) sale de Hugging Face. Presentar como rango y como estimación.
4. Olvido catastrófico: solo Biderman et al. (sobre LoRA); falta el trabajo clásico y una fuente sobre mitigación (mezclar datos generales, tasa de aprendizaje baja).
5. Proveedores: Anthropic sin estado verificado fuera de Bedrock y Claude 3 Haiku; Google sin la tabla oficial de deprecaciones ni cierre de Gemini 2.5 Pro verificado; Mistral, Meta, Cohere y proveedores de modelos abiertos (Together, Fireworks) sin cubrir. Al ser volátil, todo con fecha 2026-11-27 y a revisar.
6. Destilación: el mecanismo de Hinton (probabilidades suaves, temperatura) no se leyó; términos de Anthropic, Google y licencias de Llama sin leer.
7. Fusión de modelos: métodos concretos (model soups, TIES, DARE, SLERP) y el finetuning multitarea sin fuente primaria leída.
8. Formatos de datos (instrucción-respuesta, conversación, preferencias) y anotación con guías: sin fuente. Ajuste por preferencias (RLHF, DPO) y refuerzo (GRPO): sin fuente primaria (Rafailov et al. para DPO, el paper de InstructGPT). Es además el componente que falta en la división.
9. Verificación de datos sintéticos: sin fuente primaria específica; y sin preprint reciente (2025-2026) sobre síntesis a escala.
10. Shumailov et al. en Nature no cargó; la cita viene de texto recuperado por búsqueda. Las notas de terceros sobre el colapso (https://arxiv.org/pdf/2410.12954) y la corrección de autor no se leyeron.
11. Todos los abstracts se leyeron con una herramienta que resume; las citas literales cortas son las únicas confiables al carácter, y todo lo demás (cifras incluidas) debe cotejarse con el PDF antes de publicarse en la base. Los puntajes de "ejemplos" y "unicidad" son juicio mío.
