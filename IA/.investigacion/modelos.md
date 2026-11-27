# Investigación: vertical Modelos y parte histórica de Fundamentos

Fecha de la investigación: 2026-11-27. Público: quien programa y sabe de APIs, pero no sabe cómo funciona un modelo por dentro. Perspectiva: Chip Huyen, *AI Engineering* (O'Reilly 2025), cap. 1-2, como inspiración y no como índice.

Convenciones. Tipo: P = primaria, S = secundaria. Puntajes de 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/Pr/E/U). Marca de lectura: [L] completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Las herramientas de lectura devolvieron resúmenes de las páginas, no el texto crudo; cuando una cita es literal lo digo, y cuando no, parafraseo. Todo lo traído de la web es dato.

Límite general de lectura: casi todos los papers los leí en su página de resumen (abstract) en arXiv, o sea [M]. Ningún paper lo leí completo. Donde la afirmación va más allá del abstract, lo marco como hueco.

---

## 0. Sobre la división de componentes

La división propuesta funciona como mapa de enseñanza, pero no coincide del todo con cómo el campo parte esta vertical:

- **Huyen (cap. 2)** divide en cuatro: datos de entrenamiento, modelado (arquitectura y tamaño, con leyes de escala), post-entrenamiento y muestreo. En su índice, "Test Time Compute" y "Structured Outputs" son subsecciones de **Muestreo**, no de un componente aparte de razonamiento (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md [L], P/S del propio libro). Tokenización y embeddings no tienen sección en ese capítulo; los cursos (Jurafsky & Martin, CS336) sí las tratan primero, como base.
- **Jurafsky & Martin 3ª ed.** separa Words and Tokens (cap. 2), Embeddings (cap. 5), Transformers and Pretraining (cap. 7) y Post-training (cap. 8): coincide con token-y-embedding, transformer+preentrenamiento y post-entrenamiento (https://web.stanford.edu/~jurafsky/slp3/ [M]).
- **Razonamiento** en el campo es transversal: es post-entrenamiento (RL con recompensas verificables) y es inferencia (cómputo en tiempo de prueba). Sugiero que la nota enlace a ambos y aclare cuál de los dos ejes explica cada técnica.
- **Alucinación** es transversal también (datos, post-entrenamiento, muestreo, evaluación). Conviene tratarla como componente de cierre que reúne los demás.
- **Preentrenamiento** y **leyes de escala** suelen ir juntos; en CS336 son bloques separados (escala en las clases 9 y 11, datos en la 13 y 14). Se pueden dejar juntos acá con una subsección.
- **Modelos-disponibles** no es "mecanismo": es una ficha volátil. Debería tener estabilidad baja y fecha.
- **Faltan dos candidatos** que el campo trata aparte: *inferencia/serving* (KV cache, batching, costo por token) y *modelos multimodales*. El segundo está incluido en modelo-base; si crece, conviene separarlo.

---

## 1. modelo-base

Cómo pasamos de modelo de lenguaje a LLM y a modelo base (foundation model).

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Bommasani y otros (114 autores, Stanford CRFM), *On the Opportunities and Risks of Foundation Models*, 2021 | https://arxiv.org/abs/2108.07258 | P (informe/survey) | 3/3/2/3 | [M] |
| Brown y otros, *Language Models are Few-Shot Learners* (GPT-3), 2020 | https://arxiv.org/abs/2005.14165 | P | 3/3/2/3 | [M] |
| Devlin y otros, *BERT*, 2018 | https://arxiv.org/abs/1810.04805 | P | 3/2/1/2 | [M] |
| Huyen, cap. 1: resumen y ToC ("From Language Models to Large Language Models", "From Large Language Models to Foundation Models") | https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | S | 2/1/1/2 | [L] del resumen público |
| Jurafsky & Martin, *Speech and Language Processing* 3ª ed., cap. 1-2, 7 | https://web.stanford.edu/~jurafsky/slp3/ | P (libro abierto) | 3/3/2/2 | [M] solo índice |
| Meta, *The Llama 3 Herd of Models* (para el caso multimodal) | https://arxiv.org/abs/2407.21783 | P | 3/2/1/1 | [M] |

Afirmaciones:
- Foundation models: modelos "trained on broad data at scale" y adaptables a muchas tareas, con ejemplos BERT, DALL-E y GPT-3; los autores señalan homogeneización (los defectos del modelo base pasan a todo lo que se construye encima) y capacidades emergentes. Resumen del abstract, https://arxiv.org/abs/2108.07258 (Bommasani y otros, 16 ago 2021, v3 12 jul 2022).
- GPT-3 tiene 175 mil millones de parámetros, "10 times larger than any previous non-sparse language model"; se evalúa en few-shot "with no gradient updates or fine-tuning", y la tarea se especifica solo con texto. Cita literal del abstract: "scaling up language models greatly improves task-agnostic, few-shot performance". https://arxiv.org/abs/2005.14165 (28 may 2020).
- BERT aprende representaciones bidireccionales profundas con texto sin etiquetar y se adapta con "a single output layer"; reporta GLUE 80.5 %. Es un modelo codificador, no generativo, y sirve para contrastar con los decodificadores. https://arxiv.org/abs/1810.04805 (11 oct 2018).
- Huyen: el cap. 1 traza el paso de modelos de lenguaje a LLM "enabled by self-supervision" y a modelos base que manejan otros tipos de dato. https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
- Llama 3: "Our largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens"; las capacidades de imagen, video y voz se agregan con un enfoque composicional. https://arxiv.org/abs/2407.21783 (31 jul 2024).
- Jurafsky & Martin: borrador de la 3ª edición publicado el 19 de agosto de 2026, con PDF completo gratuito; no declara una licencia de reutilización. https://web.stanford.edu/~jurafsky/slp3/

**Recurso canónico:** Bommasani y otros, secciones 1 y 2 (introducción y capacidades), para la definición y la idea de homogeneización; combinar con Brown y otros para el salto a "se programa con texto". Fijarse en: la distinción entre el modelo (artefacto adaptable) y la aplicación (lo que se construye encima), y en la nota de que los autores admiten no entender del todo cuándo fallan.

**Contraste con el material previo (`Archivo/IA/llm.md`)**: ya cubre GPT-3, Transformer y alucinación en una sola nota. Lo que no tiene: la tercera escalera (LLM a modelo base) ni multimodal. Esa es la ampliación.

---

## 2. token-y-embedding

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Sennrich, Haddow, Birch, *Neural Machine Translation of Rare Words with Subword Units* (BPE), ACL 2016 | https://arxiv.org/abs/1508.07909 | P | 3/3/1/3 | [M] |
| Petrov y otros, *Language Model Tokenizers Introduce Unfairness Between Languages*, NeurIPS 2023 | https://arxiv.org/abs/2305.15425 | P (con revisión) | 3/2/2/3 | [M] |
| Karpathy, `minbpe` (código) y video "Let's build the GPT Tokenizer" | https://github.com/karpathy/minbpe | S (práctica) | 2/3/3/3 | [M] del README; el video no pude abrirlo (YouTube redirigió a un bloqueo) |
| Jurafsky & Martin, cap. 2 *Words and Tokens* y cap. 5 *Embeddings* | https://web.stanford.edu/~jurafsky/slp3/ | P | 3/3/2/2 | [M] solo índice |
| CS336 Stanford (clase 1: overview y tokenización, Percy Liang) | http://cs336.stanford.edu/spring2025/ | P (curso) | 3/3/3/2 | [M] |

Afirmaciones:
- BPE para traducción: codificar palabras raras o desconocidas "as sequences of smaller subword units" evita el diccionario de respaldo; mejora de 1,1 BLEU (inglés-alemán) y 1,3 (inglés-ruso) sobre el respaldo por diccionario. https://arxiv.org/abs/1508.07909 (31 ago 2015; ACL 2016). Nota: el paper es de traducción neuronal; que los LLM adoptaran BPE (y variantes a nivel de byte) es una extensión que no verifiqué en esta fuente.
- Costo e idiomas: el mismo texto en idiomas distintos puede producir hasta 15 veces más tokens; los modelos a nivel de caracter o byte muestran diferencias de más de 4 veces entre algunos pares. Quien habla esos idiomas paga más, espera más y le cabe menos en la ventana de contexto. https://arxiv.org/abs/2305.15425 (17 may 2023).
- La nota sobre la ventana de Claude lo ilustra con un dato fechado: "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7); models before it fit about 750k words in 1M tokens". Es decir, un cambio de tokenizador cambia cuánto texto entra y cuánto cuesta. https://platform.claude.com/docs/en/models/overview (leído 2026-11-27).
- `minbpe` implementa BasicTokenizer, RegexTokenizer (la expresión regular evita que las fusiones crucen categorías como letras, números y puntuación) y un GPT4Tokenizer que reproduce el de tiktoken. https://github.com/karpathy/minbpe

Hueco en este componente: no leí una fuente primaria sobre aritmética y tokenización (por qué los números se parten en tokens y eso daña la cuenta), ni sobre embeddings como representación (word2vec, Bengio 2003). Declarado en la sección de huecos.

**Recurso canónico:** el video de Karpathy "Let's build the GPT Tokenizer" (en la descripción de `minbpe`), para ver BPE funcionando, junto con Petrov y otros para el costo por idioma. Para la parte de embeddings, el cap. 5 de Jurafsky & Martin. Fijarse en: cuántos tokens da una frase en castellano frente a inglés, y que el vocabulario es una decisión de diseño fija antes del entrenamiento. (No pude verificar el video.)

---

## 3. transformer

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Vaswani y otros, *Attention Is All You Need*, 2017 | https://arxiv.org/abs/1706.03762 | P | 3/3/1/3 | [M] |
| Alammar, *The Illustrated Transformer* | https://jalammar.github.io/illustrated-transformer/ | S (didáctica) | 2/2/3/3 | [M] |
| Kwon y otros, *PagedAttention / vLLM* (para KV cache) | https://arxiv.org/abs/2309.06180 | P | 3/2/1/2 | [M] |
| Shazeer y otros, *Outrageously Large Neural Networks* (MoE) | https://arxiv.org/abs/1701.06538 | P | 3/3/1/3 | no leído acá; ya figura en el material previo |
| Fedus y otros, *Switch Transformers* | https://arxiv.org/abs/2101.03961 | P | 3/3/1/2 | [M] |
| Jiang y otros, *Mixtral of Experts* | https://arxiv.org/abs/2401.04088 | P | 3/2/2/2 | [M] |
| Jurafsky & Martin, cap. 7 *Transformers and Pretraining* | https://web.stanford.edu/~jurafsky/slp3/ | P | 3/3/2/2 | [M] solo índice |

Afirmaciones:
- Transformer: arquitectura "based solely on attention mechanisms, dispensing with recurrence and convolutions entirely" (cita literal). 28,4 BLEU en WMT 2014 inglés-alemán y 41,8 en inglés-francés, entrenando mucho más rápido. Es un modelo codificador-decodificador; los LLM de hoy usan solo la parte decodificadora (esto último es práctica del campo que no verifiqué en una fuente puntual, ver huecos). https://arxiv.org/abs/1706.03762 (12 jun 2017).
- Atención, según Alammar: cada token genera vectores de consulta, clave y valor; los puntajes son productos punto, escalados y pasados por softmax, y ponderan los valores. Varias cabezas (ocho en el paper original) corren en paralelo, y como la atención no capta el orden se suman vectores de posición. https://jalammar.github.io/illustrated-transformer/ (escrito en 2018, con actualización 2025).
- KV cache: "the key-value cache (KV cache) memory for each request is huge and grows and shrinks dynamically"; mal manejado, limita el tamaño del lote. PagedAttention reduce el desperdicio a casi cero. Es la razón por la que servir contextos largos cuesta memoria. https://arxiv.org/abs/2309.06180 (12 sep 2023). Esto explica el concepto en servicio; el origen de la idea de cachear K y V no lo leí.
- Ventana de contexto vigente, fechada: Claude, 1M tokens en toda la línea 5.x (https://platform.claude.com/docs/en/models/overview); OpenAI GPT-6.x, 1,05 M (https://developers.openai.com/api/docs/models); Gemini 4, 1 M de entrada (https://aistudio.google.com/docs/models). Los tres a 2026-11-27.
- MoE: Switch Transformer simplifica el router y reporta hasta 7 veces menos tiempo de preentrenamiento a igual cómputo sobre T5-Base y T5-Large, y modelos de un billón de parámetros con 4 veces de aceleración sobre T5-XXL. https://arxiv.org/abs/2101.03961 (11 ene 2021). Mixtral 8x7B: ocho expertos por capa, el router elige dos por token; 47 B de parámetros totales y 13 B activos; Apache 2.0; "matches or outperforms Llama 2 70B and GPT-3.5" en los benchmarks evaluados. https://arxiv.org/abs/2401.04088 (8 ene 2024).
- MoE hoy: DeepSeek-V4-Pro 1,6 T totales y 49 B activos; V4-Flash 284 B y 13 B activos; contexto 1 M (https://api-docs.deepseek.com/news/news260424). Qwen3.5-397B-A17B (17 B activos de 397 B) según prensa (ver sección 9). MoE es hoy la forma común de los modelos abiertos grandes.

**Recurso canónico:** Vaswani y otros, secciones 3.1 a 3.3 (arquitectura, atención y atención multi-cabeza), leídas junto a Alammar para tener el dibujo. Para MoE, el resumen de Switch Transformers más Mixtral. Fijarse en: que el costo de la atención crece con el cuadrado del largo del contexto (afirmación del campo que no pude verificar en estas fuentes de resumen) y que el KV cache es lo que hace que un prompt largo repetido sea barato con *prompt caching*.

**Contraste con material previo:** `mixture-of-experts.md` ya cubre Shazeer 2017, Switch y Mixtral con cifras (47 B / 13 B, 7 veces). Coinciden con lo leído acá. No repetir; enlazar. Lo que sí falta: el decodificador, la atención y el KV cache.

---

## 4. preentrenamiento

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Kaplan y otros, *Scaling Laws for Neural Language Models*, 2020 | https://arxiv.org/abs/2001.08361 | P | 3/3/2/3 | [M] (citas literales del abstract) |
| Hoffmann y otros, *Training Compute-Optimal Large Language Models* (Chinchilla), 2022 | https://arxiv.org/abs/2203.15556 | P | 3/3/2/3 | [M] |
| Villalobos y otros, *Will we run out of data?*, 2022 (rev. 2024) | https://arxiv.org/abs/2211.04325 | P | 3/3/2/3 | [M] |
| Muennighoff y otros, *Scaling Data-Constrained Language Models*, 2023 | https://arxiv.org/abs/2305.16264 | P | 3/3/2/3 | [M] |
| Huyen cap. 2 (Training Data: Multilingual / Domain-Specific; Model Size) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | S | 2/1/1/2 | [L] del resumen |
| CS336 (datos: clases 13 y 14; escala: clases 9 y 11) | http://cs336.stanford.edu/spring2025/ | P (curso) | 3/3/3/2 | [M] |

Afirmaciones:
- Kaplan: "The loss scales as a power-law with model size, dataset size, and the amount of compute used for training", con tendencias de "more than seven orders of magnitude"; arquitectura fina como ancho o profundidad tiene "minimal effects within a wide range"; el entrenamiento compute-óptimo "involves training very large models on a relatively modest amount of data and stopping significantly before convergence". https://arxiv.org/abs/2001.08361 (23 ene 2020).
- Chinchilla: "We find that current large language models are significantly undertrained" (cita literal). Más de 400 modelos de 70 M a más de 16 B de parámetros; tamaño del modelo y tokens deben escalar en igual proporción. Chinchilla (70 B, unas 4 veces más datos que Gopher de 280 B con el mismo cómputo) supera a Gopher, GPT-3, Jurassic-1 y Megatron-Turing NLG, con 67,5 % de promedio en MMLU. https://arxiv.org/abs/2203.15556 (29 mar 2022).
- **Discrepancia entre las dos:** Kaplan recomienda más modelo y relativamente pocos datos; Chinchilla recomienda crecer ambos en igual proporción y concluye que los modelos de la época estaban "significativamente subentrenados". Hay que dar las dos y la fecha de cada una; la nota no debe presentar Kaplan como "la" ley. Lo que no leí: las razones metodológicas de la diferencia (se discuten en la literatura, no en estos abstracts).
- Cuello de botella de datos: el stock de texto humano público podría ser alcanzado por los datasets de entrenamiento "between 2026 and 2032" si la tendencia sigue, y antes si hay sobreentrenamiento; mitigaciones propuestas: datos sintéticos, transferencia desde dominios con más datos, mayor eficiencia de datos. https://arxiv.org/abs/2211.04325. Es una proyección de 2022 (revisada en 2024), no una medición; conviene fecharla.
- Repetir datos: hasta unas 4 épocas casi no cambia la pérdida frente a datos únicos; más allá, el cómputo extra rinde cada vez menos; sumar código o quitar filtros de calidad son formas de aliviar la escasez. 400 corridas, modelos de hasta 9 B con hasta 900 B de tokens. https://arxiv.org/abs/2305.16264
- Huyen: la calidad del modelo depende mucho de los datos; los proveedores suelen usar "whatever data is available"; para idiomas de pocos recursos y para dominios hace falta curar. Escala medida en parámetros, tokens de entrenamiento y FLOPs de entrenamiento. https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
- Un dato de cuánto: Llama 3 405B, 128 K de contexto (ver arriba). La cifra de 15 T de tokens la conozco de otras fuentes pero no se confirmó en la lectura: no usar sin verificar.

**Recurso canónico:** Hoffmann y otros (Chinchilla), con Kaplan al lado: leer los dos abstracts y el gráfico de asignación óptima. Fijarse en que "óptimo" es para minimizar la pérdida con un presupuesto de entrenamiento dado, no para minimizar el costo de servir el modelo (si se va a servir mucho, conviene un modelo más chico entrenado con más datos; esto último es práctica del campo, no lo verifiqué en estas fuentes). Complemento: CS336, clases 9 y 11 (escala) y 13 y 14 (datos).

---

## 5. post-entrenamiento

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Ouyang y otros, *Training language models to follow instructions with human feedback* (InstructGPT), 2022 | https://arxiv.org/abs/2203.02155 | P | 3/3/2/3 | [M] |
| Rafailov y otros, *Direct Preference Optimization*, 2023 | https://arxiv.org/abs/2305.18290 | P | 3/3/1/3 | [M] |
| Bai y otros, *Constitutional AI: Harmlessness from AI Feedback*, 2022 | https://arxiv.org/abs/2212.08073 | P | 3/3/2/3 | [M] |
| Lambert y otros, *Tulu 3*, 2024 | https://arxiv.org/abs/2411.15124 | P (receta abierta) | 3/3/2/3 | [M] |
| OpenAI, anuncio de ChatGPT, 30 nov 2022 | https://openai.com/index/chatgpt/ | P | 3/1/2/2 | [S] resumen del fetch |
| Jurafsky & Martin, cap. 8 *Post-training* | https://web.stanford.edu/~jurafsky/slp3/ | P | 3/3/2/2 | [M] solo índice |
| Huyen cap. 2, Post-Training (SFT y preference finetuning) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | S | 2/1/1/2 | [L] del resumen |

Afirmaciones:
- Por qué existe: el preentrenamiento sobre datos imperfectos puede dar salidas que no coinciden con lo que espera el usuario; el post-entrenamiento se hace con ajuste supervisado y ajuste por preferencias. Las preferencias humanas son diversas, así que los métodos actuales son imperfectos (Huyen, resumen del cap. 2).
- InstructGPT: ajustan GPT-3 con demostraciones escritas por etiquetadores (supervisado) y después con aprendizaje por refuerzo con feedback humano sobre rankings de salidas. Cita literal del abstract: "outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters". Ojo: es preferencia humana sobre la distribución de prompts de los autores, no superioridad en todos los benchmarks; "still makes simple mistakes". https://arxiv.org/abs/2203.02155 (4 mar 2022).
- ChatGPT: se afinó desde un modelo de la serie GPT-3.5 con RLHF, "the same methods as InstructGPT" con diferencias en la recolección de datos; entrenadores humanos escribieron conversaciones y rankearon respuestas para entrenar un modelo de recompensa, y luego PPO. Limitación declarada: "sometimes writes plausible-sounding but incorrect or nonsensical answers". https://openai.com/index/chatgpt/ (30 nov 2022).
- DPO: reparametriza el modelo de recompensa para que la política óptima salga en forma cerrada; reduce el problema a una pérdida de clasificación "with no sampling from the language model during fine-tuning" (paráfrasis del abstract: sin muestrear del modelo ni casi afinar hiperparámetros). Los autores afirman que iguala o mejora los métodos previos. https://arxiv.org/abs/2305.18290 (29 may 2023, v3 29 jul 2024).
- RLAIF / constitucional: dos fases. Supervisada: el modelo critica y revisa sus respuestas con una lista corta de principios escrita por personas (la "constitución"), y se afina con las revisiones. RL: un modelo juzga cuál de dos respuestas es mejor y esas preferencias entrenan el modelo de recompensa (RLAIF). Resultado: asistente inofensivo "but not evasive". https://arxiv.org/abs/2212.08073 (15 dic 2022).
- Receta abierta reciente: Tulu 3 combina SFT, DPO y un método nuevo "Reinforcement Learning with Verifiable Rewards" (RLVR); publica datos, código y recetas; reporta superar a los instruct de Llama 3.1, Qwen 2.5 y Mistral y a GPT-4o-mini y Claude 3.5 Haiku. https://arxiv.org/abs/2411.15124 (22 nov 2024, v5 14 abr 2025). Es un resultado de los autores, preprint.

**Recurso canónico:** InstructGPT (Ouyang y otros), secciones de método (SFT, modelo de recompensa, PPO) y la sección de resultados sobre preferencias; es el puente histórico a ChatGPT. Para el estado actual, Tulu 3 (receta abierta completa). Fijarse en: el modelo de recompensa es un modelo entrenado con rankings humanos, no la verdad, y por eso el modelo puede aprender a agradar. El resumen de DPO sirve para la pregunta "¿hace falta RL?".

---

## 6. muestreo

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Holtzman y otros, *The Curious Case of Neural Text Degeneration* (top-p), ICLR 2020 | https://arxiv.org/abs/1904.09751 | P | 3/3/2/3 | [M] |
| Willard & Louf, *Efficient Guided Generation for LLMs* (Outlines), 2023 | https://arxiv.org/abs/2307.09702 | P (preprint) | 2/3/2/3 | [M] |
| Anthropic, documentación de *Structured outputs* | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | P (doc oficial) | 3/3/3/2 | [L] hasta los 100 000 caracteres de 112 853; falta el final |
| OpenAI, guía de *Structured Outputs* | https://developers.openai.com/api/docs/guides/structured-outputs | P (doc oficial) | 3/3/3/2 | [L] parcial (100 000 de 152 792 caracteres) |
| Huyen cap. 2, Sampling (fundamentals, strategies, test-time compute, structured outputs, probabilistic nature) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md y chapter-summaries.md | S | 2/1/1/2 | [L] |

Afirmaciones:
- Top-p: muestrear del "smallest set of top-probability words" cuya probabilidad acumulada supera un umbral recorta la cola poco confiable y mantiene la diversidad; el texto generado eligiendo siempre lo más probable es "dull and repetitive"; "decoding strategy alone can greatly change the quality of generated text, even with the same model" (paráfrasis del abstract). https://arxiv.org/abs/1904.09751 (22 abr 2019; ICLR 2020).
- Huyen: el muestreo hace a los modelos probabilísticos; eso permite salidas creativas, pero también inconsistencia y alucinación; hay que diseñar el flujo alrededor de ese comportamiento, empezando por una buena evaluación. https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
- Salidas estructuradas, Anthropic: se manda el esquema en `output_config.format` con `type: "json_schema"`; la página lo describe como "constrained decoding" y "constrained sampling with compiled grammar artifacts", y garantiza "No JSON parsing errors", tipos y campos obligatorios correctos. La primera vez con un esquema hay latencia extra por compilar la gramática; las gramáticas se cachean 24 horas desde el último uso. No soporta esquemas recursivos, `oneOf`, `minimum`/`maximum`, `minLength`/`maxLength`. https://platform.claude.com/docs/en/build-with-claude/structured-outputs (leído 2026-11-27).
- Salidas estructuradas, OpenAI: "Structured Outputs constrains completed, non-refusal model output to your supplied JSON Schema"; "only Structured Outputs ensure schema adherence", y el modo JSON solo asegura JSON válido. Hay que manejar rechazos (`refusal`), respuestas incompletas y reglas de negocio que el esquema no expresa. La página no describe el mecanismo ni usa "constrained decoding". https://developers.openai.com/api/docs/guides/structured-outputs
- Mecanismo de la técnica: recasting de la generación como transiciones de una máquina de estados finita, con un índice sobre el vocabulario para guiar con expresiones regulares y gramáticas libres de contexto; implementación en Outlines. https://arxiv.org/abs/2307.09702 (19 jul 2023). Lo que dice cada fuente sobre el mecanismo es compatible; la de OpenAI no lo nombra.
- Garantía y calidad no son lo mismo: el esquema asegura la forma, no que el valor sea correcto. (Inferencia mía, consistente con el aviso de OpenAI sobre reglas de negocio; no es cita.)

No pude verificar: la definición literal de logits, temperatura y top-k en una fuente primaria, ni los rangos y valores por defecto actuales de `temperature`/`top_p` en las APIs (la página de la API de mensajes de Anthropic tiene 1,3 M de caracteres y el fetch no llegó a esos parámetros). Tampoco una fuente primaria sobre por qué `temperature = 0` no garantiza determinismo. Quedan como hueco.

**Recurso canónico:** Huyen, sección Sampling (en el libro completo, no disponible; el resumen no alcanza) más Holtzman y otros para la intuición; y la documentación de salidas estructuradas del proveedor que use la persona, porque es donde está la garantía concreta y sus límites. Fijarse en: qué restricciones del esquema no se soportan (se descubren con un 400), y que la primera llamada con un esquema nuevo cuesta latencia.

---

## 7. razonamiento

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Wei y otros, *Chain-of-Thought Prompting*, 2022 | https://arxiv.org/abs/2201.11903 | P | 3/3/2/3 | [M] |
| Snell y otros, *Scaling LLM Test-Time Compute Optimally...*, 2024 | https://arxiv.org/abs/2408.03314 | P (preprint, sin revisión por pares) | 3/3/2/3 | [M] |
| OpenAI, *Learning to reason with LLMs* (o1), 12 sep 2024 | https://openai.com/index/learning-to-reason-with-llms/ | P | 3/2/2/3 | [S] resumen del fetch |
| DeepSeek-AI, *DeepSeek-R1*, 2025 (Nature 645, 633-638) | https://arxiv.org/abs/2501.12948 | P | 3/3/2/3 | [M] |
| Shao y otros, *DeepSeekMath* (GRPO), 2024 | https://arxiv.org/abs/2402.03300 | P | 3/2/1/3 | [M] |
| Raschka, *Understanding Reasoning LLMs*, 5 feb 2025 | https://magazine.sebastianraschka.com/p/understanding-reasoning-llms | S (práctica) | 2/2/2/2 | [S] resumen del fetch |
| Anthropic, *Extended thinking* (marcado como legado) y modelos | https://platform.claude.com/docs/en/build-with-claude/extended-thinking | P (doc oficial) | 3/3/3/3 | [L] |

Afirmaciones:
- Cadena de pensamiento: con pocos ejemplos que incluyen pasos intermedios, un modelo de 540 B con ocho ejemplos alcanzó el estado del arte en GSM8K, por encima de un GPT-3 afinado con verificador. Funciona en modelos suficientemente grandes. https://arxiv.org/abs/2201.11903 (28 ene 2022).
- Cómputo en inferencia: con presupuesto fijo, asignar cómputo de forma adaptativa por prompt es "over 4x more efficient than a best-of-N baseline" (paráfrasis del abstract); en una comparación a FLOPs iguales, un modelo base más chico superó a uno 14 veces mayor cuando se le dio más cómputo en inferencia, en problemas donde el chico tenía tasas de éxito no triviales. https://arxiv.org/abs/2408.03314 (6 ago 2024). Es un preprint y el resultado depende de la dificultad del problema.
- o1: la página, fechada 12 sep 2024, dice que un algoritmo de RL a gran escala "teaches the model how to think productively using its chain of thought", que los resultados mejoran con más entrenamiento RL y con más tiempo de razonamiento (test-time compute). Al leerla, la misma página avisa que o1-preview y o1-mini están retirados de la API y o1 deprecado. https://openai.com/index/learning-to-reason-with-llms/
- DeepSeek-R1: el razonamiento puede incentivarse con RL puro, sin ejemplos de razonamiento etiquetados por humanos (R1-Zero), con conductas como autorreflexión, verificación y adaptación de estrategia; rinde bien en tareas verificables (matemática, programación, STEM). Enviado 22 ene 2025, revisión 4 ene 2026, publicado en Nature vol. 645. https://arxiv.org/abs/2501.12948
- GRPO: variante de PPO que reduce el uso de memoria; DeepSeekMath 7B llega a 51,7 % en MATH sin herramientas. https://arxiv.org/abs/2402.03300 (5 feb 2024).
- RL con recompensas verificables (RLVR): nombre de la técnica en Tulu 3; la recompensa sale de una verificación automática (la respuesta correcta) en vez de preferencia humana. El abstract de Tulu 3 no explica el mecanismo; la definición de "verificable" como respuesta comprobable la tomo de R1, "verifiable tasks". https://arxiv.org/abs/2411.15124
- Raschka, cuatro vías para construir o mejorar modelos de razonamiento: escalado en inferencia, RL puro, SFT más RL (la receta de R1) y SFT puro con destilación. Define razonamiento como "the process of answering questions that require complex, multi-step generation with intermediate steps". https://magazine.sebastianraschka.com/p/understanding-reasoning-llms
- **Presupuesto de pensamiento, estado de API a 2026-11 (volátil):** la API de Claude pasó de un presupuesto fijo (`thinking: {type: "enabled", budget_tokens: N}`, mínimo 1 024 tokens, menor que `max_tokens`) a pensamiento adaptativo controlado por `effort`. La doc dice: "Extended thinking is a legacy feature", "Claude 4.7 and later models do not support it and reject requests that use it, returning a 400 error". Para migrar: `thinking: {type: "adaptive"}` y `output_config: {effort: ...}`. Los tokens de pensamiento se facturan como salida y se reportan en `usage.output_tokens_details.thinking_tokens`. https://platform.claude.com/docs/en/build-with-claude/extended-thinking (leído 2026-11-27). En la tabla de modelos, Fable 5.2 y Opus 5.5 tienen "Adaptive (always on)" y Sonnet 5.5 y Haiku 5.5 "Adaptive". https://platform.claude.com/docs/en/models/overview

**Recurso canónico:** DeepSeek-R1 (Nature, 2025), con la parte de R1-Zero y las secciones de recompensas y conductas emergentes; es el primer caso abierto y bien documentado del paradigma. Contexto: o1 como anuncio, Snell y otros para la lógica de "gastar cómputo al pensar". Para el desarrollador: la página de *thinking* y *effort* del proveedor. Fijarse en: la recompensa solo funciona donde se puede verificar la respuesta, y las "cadenas de pensamiento" visibles pueden ser resúmenes (la doc de Anthropic habla de bloques de pensamiento resumidos); no son un registro fiel del cálculo (la fidelidad de la cadena de pensamiento no la verifiqué acá).

**Discrepancia de terminología:** Huyen ubica "test time compute" bajo Muestreo; Raschka lo pone como una de cuatro vías de razonamiento; OpenAI lo liga a RL. No son contradicciones, son cortes distintos del mismo tema.

---

## 8. alucinacion

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Kalai, Nachum, Vempala, Zhang, *Why Language Models Hallucinate*, 4 sep 2025 | https://arxiv.org/abs/2509.04664 | P (preprint, sin revisión por pares verificada) | 3/3/2/3 | [M] |
| Zhang y otros, *How Language Model Hallucinations Can Snowball*, 2023 | https://arxiv.org/abs/2305.13534 | P | 3/2/3/3 | [M] |
| Gekhman y otros, *Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?*, EMNLP 2024 | https://arxiv.org/abs/2405.05904 | P | 3/3/2/3 | [M] |
| Kadavath y otros, *Language Models (Mostly) Know What They Know*, 2022 | https://arxiv.org/abs/2207.05221 | P | 3/3/2/3 | [M] |
| Weng, *Extrinsic Hallucinations in LLMs*, 7 jul 2024 | https://lilianweng.github.io/posts/2024-07-07-hallucination/ | S (survey de práctica) | 2/3/2/2 | [S] resumen del fetch |
| Anthropic, *Reduce hallucinations* (ya citada en el material previo) | https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations | P (doc oficial) | 3/2/2/1 | no releída acá |

Afirmaciones:
- OpenAI 2025 (Kalai y otros): los modelos alucinan, o sea producen afirmaciones plausibles pero falsas con seguridad, porque el entrenamiento y la evaluación premian adivinar en lugar de admitir incertidumbre. Las alucinaciones pueden surgir como errores de clasificación binaria cuando las afirmaciones falsas son difíciles de distinguir de los hechos. Conclusión de los autores: el arreglo es sociotécnico, cambiar cómo los benchmarks existentes puntúan las respuestas inciertas, en lugar de agregar nuevas pruebas de alucinación. (Paráfrasis del abstract, que el fetch no devolvió textual.) https://arxiv.org/abs/2509.04664
- Snowballing: los modelos se comprometen con un error inicial y después generan afirmaciones falsas que ellos mismos reconocerían como erróneas; ChatGPT y GPT-4 identificaron como erróneas el 67 % y el 87 % de sus propias afirmaciones falsas. Apoya la hipótesis de que no todo se debe a falta de conocimiento. https://arxiv.org/abs/2305.13534 (22 may 2023).
- Conocimiento del modelo frente al del etiquetador: afinar con datos que traen hechos nuevos se aprende "much more slowly" que lo que el modelo ya sabe, y una vez aprendido aumenta la tendencia a alucinar; los autores concluyen que el modelo adquiere el conocimiento factual sobre todo en el preentrenamiento y el afinado mejora cómo lo usa. https://arxiv.org/abs/2405.05904 (9 may 2024, EMNLP 2024). Esta es la evidencia concreta de la hipótesis de desalineación entre conocimiento del modelo y del etiquetador; el paper no lo nombra así, la conexión es la que propuso la consigna.
- Weng: datos de preentrenamiento de internet (desactualizados, faltantes o incorrectos y memorizados) y conocimiento nuevo en afinado como causas; detección por recuperación (FActScore, SAFE) o por consistencia entre muestras (SelfCheckGPT); retrieval reduce la alucinación de forma consistente. https://lilianweng.github.io/posts/2024-07-07-hallucination/
- Calibración: Kadavath y otros encuentran modelos grandes bien calibrados en preguntas de opción múltiple y verdadero/falso con buen formato, y entrenan un predictor P(IK) de "yo sé la respuesta" que generaliza solo en parte a tareas nuevas. https://arxiv.org/abs/2207.05221 (11 jul 2022).
- **Discrepancia a presentar:** Weng, citando a Kadavath, dice que "RLHF fine-tuning makes the model poorly calibrated" y que mayor temperatura mejora la calibración. Kalai y otros apuntan a que la evaluación premia adivinar. Los dos apuntan a que el post-entrenamiento puede empeorar la calibración, pero por distinto mecanismo: uno empírico sobre RLHF, otro por incentivos de los benchmarks. No es contradicción, pero no hay que tratarlos como la misma explicación. También: la hipótesis de snowballing (autoregresión) y la de Kalai (incentivos de evaluación) no se excluyen.
- OpenAI en ChatGPT (2022) ya advertía: "sometimes writes plausible-sounding but incorrect or nonsensical answers". https://openai.com/index/chatgpt/

**Recurso canónico:** Kalai y otros, 2025: la introducción y la sección sobre pos-entrenamiento y evaluación. Es el texto más reciente y trae una explicación estadística unificada. Complemento: Weng para el panorama de detección y mitigación, y Zhang para el efecto bola de nieve. Fijarse en: qué parte es causa estadística (hechos arbitrarios raros que no se pueden aprender) y qué parte es incentivo de evaluación.

---

## 9. modelos-disponibles (ficha fechada a 2026-11-27)

Regla: solo lo verificado en una fuente viva. Los precios, contextos e IDs cambian; por eso cada fila trae su fuente.

| Fuente (viva) | URL | Tipo | A/Pr/E/U | Marca | Recencia |
|---|---|---|---|---|---|
| Anthropic, *Models overview* | https://platform.claude.com/docs/en/models/overview | P | 3/3/3/3 | [L] | leída 2026-11-27 |
| OpenAI, página de modelos | https://developers.openai.com/api/docs/models | P | 3/2/1/3 | [L] resumen del fetch | leída 2026-11-27 |
| Google, página de modelos de Gemini | https://aistudio.google.com/docs/models | P | 3/2/1/3 | [L] resumen del fetch | leída 2026-11-27 |
| DeepSeek, anuncio V4 | https://api-docs.deepseek.com/news/news260424 | P | 3/2/1/3 | [L] resumen del fetch | 2026-04-24 |
| Alibaba Cloud/NYU/The Decoder sobre Qwen 3.8 | https://www.alibabacloud.com/blog/603463 ; https://the-decoder.com/alibabas-qwen-team-releases-qwen-3-8-models-with-open-weights-under-the-apache-2-0-license/ | S | 2/1/1/1 | [S] del buscador, no abiertas | ago 2026 |
| Prensa sobre Meta (Muse Spark, fin de Llama) | https://9to5mac.com/2026/04/08/goodbye-llama-meta-unveils-muse-spark-ai-with-new-contemplating-mode/ | S | 1/1/1/1 | [S] del buscador | abr 2026 |

**Cerrados (fuente primaria, leída):**
- Anthropic, a 2026-11-27: Claude Fable 5.2 (`claude-fable-5-2`, 8 USD entrada / 40 USD salida por millón de tokens), Opus 5.5 (`claude-opus-5-5`, 4/20), Sonnet 5.5 (`claude-sonnet-5-5`, 2/10), Haiku 5.5 (`claude-haiku-5-5`, desde 0,10/0,50). Todos 1 M de contexto y 128 K de salida máxima, corte de conocimiento confiable jun 2026, todos con pensamiento adaptativo. Claude Mythos 5.2 es de disponibilidad limitada. Retiro "Not sooner than" nov 2027 (Fable), sep 2027 (Opus), sep 2027 (Sonnet), oct 2027 (Haiku). https://platform.claude.com/docs/en/models/overview
- OpenAI: GPT-6.2 Astra (`gpt-6.2-astra`), GPT-6.2 Sol (`gpt-6.2-sol`), GPT-6.1 Terra (`gpt-6.1-terra`), GPT-6 Luna (`gpt-6-luna`); contexto 1,05 M, salida hasta 128 K, cortes de conocimiento de 18 may y 1 jun 2026. La página no trae precios en lo que recuperé. https://developers.openai.com/api/docs/models
- Google: Gemini 4 (Carbon, Neon, Hydrogen, Argon; IDs `gemini-4-carbon` etc.; entrada de 1 M de tokens; estado no indicado) y la línea 3.x con Gemini 3.8 Flash y 3.6 Flash estables, 3.1 Pro en preview. https://aistudio.google.com/docs/models

**Abiertos (con salvedad):**
- DeepSeek-V4, 24 abr 2026, "Preview Release": V4-Pro 1,6 T de parámetros totales y 49 B activos; V4-Flash 284 B y 13 B activos; contexto 1 M; pesos abiertos en Hugging Face; nombres de API `deepseek-v4-pro` y `deepseek-v4-flash`; los nombres viejos `deepseek-chat` y `deepseek-reasoner` se retiran después del 24 jul 2026 (ya vencido a la fecha). La página oficial no nombra licencia; una fuente de prensa dice MIT, sin confirmar en el original. https://api-docs.deepseek.com/news/news260424 (primaria); licencia: https://rits.shanghai.nyu.edu/ai/deepseek-releases-v4-open-source-1-6t-moe-with-1m-context [S].
- Qwen (Alibaba): según resultados del buscador, Qwen3.5-397B-A17B (feb 2026), Qwen3.8-27B bajo Apache 2.0, Qwen3.8-2.4T-A95B (13 ago 2026, descrito como el mayor modelo de pesos abiertos publicado) y Qwen3.8-Flash-Next (26 ago 2026). Todo [S]; no abrí la fuente primaria (Hugging Face / blog de Qwen). Marcar como "a verificar".
- Meta: la serie Llama termina en Llama 4 (abr 2025) según Wikipedia; la prensa de abril 2026 habla de Muse Spark como sucesor, con pesos "en fases". Todo [S]; no verifiqué en llama.com ni en el blog de Meta si hay pesos abiertos. Marcar como "a verificar".
- Mistral: no investigado (sin dato propio más allá de Mixtral 8x7B de 2024, que ya es histórico).

**Discrepancia a notar:** el buscador describe a DeepSeek V4 como "preview" por prensa de abril; la página oficial lo titula "Preview Release". Si ya salió una versión final después, no la encontré (búsqueda de una sola ronda), y la fecha de la fuente es de siete meses antes de hoy.

**Recurso canónico:** no hay uno estable; la propuesta es que la nota sea una tabla corta con fecha y enlace a la página viva de cada proveedor, más una regla de mantenimiento: cada fila se revalida cada tanto contra su fuente. Fijarse en: contexto máximo frente a salida máxima, corte de conocimiento, fecha de retiro (dice cuánto durará el ID) y si el modelo "piensa" por defecto.

---

## 10. Fundamentos/historia-de-la-ia-generativa

| Fuente | URL | Tipo | A/Pr/E/U | Marca |
|---|---|---|---|---|
| Jurafsky & Martin 3ª ed. (cap. 3 N-gram, 14 RNN/LSTM, 7 Transformers) | https://web.stanford.edu/~jurafsky/slp3/ | P | 3/3/2/3 | [M] solo índice |
| Vaswani y otros 2017 | https://arxiv.org/abs/1706.03762 | P | 3/3/1/3 | [M] |
| Devlin y otros (BERT) 2018 | https://arxiv.org/abs/1810.04805 | P | 3/2/1/2 | [M] |
| Brown y otros (GPT-3) 2020 | https://arxiv.org/abs/2005.14165 | P | 3/3/2/3 | [M] |
| Kaplan 2020; Hoffmann 2022 | ver sección 4 | P | 3/3/2/3 | [M] |
| Ouyang 2022 y anuncio de ChatGPT, 30 nov 2022 | https://arxiv.org/abs/2203.02155 ; https://openai.com/index/chatgpt/ | P | 3/3/2/3 | [M]/[S] |
| Bommasani 2021 | https://arxiv.org/abs/2108.07258 | P | 3/3/2/3 | [M] |
| OpenAI o1 (12 sep 2024); DeepSeek-R1 (22 ene 2025) | ver sección 7 | P | 3/3/2/3 | [S]/[M] |

Línea de tiempo con fuente (fechas de envío o publicación):
- Modelos de n-gramas y de RNN/LSTM: están como capítulos de Jurafsky & Martin (cap. 3 "N-gram Language Models", cap. 14 "RNNs and LSTMs"). https://web.stanford.edu/~jurafsky/slp3/ Solo confirmé el índice; no hay nota fechada de n-gramas ni de RNN acá.
- 2015 a 2016, BPE subword: Sennrich y otros. https://arxiv.org/abs/1508.07909
- jun 2017, Transformer. https://arxiv.org/abs/1706.03762
- oct 2018, BERT. https://arxiv.org/abs/1810.04805
- ene 2020, leyes de escala (Kaplan). https://arxiv.org/abs/2001.08361
- may 2020, GPT-3 (175 B, few-shot). https://arxiv.org/abs/2005.14165
- ago 2021, "foundation models". https://arxiv.org/abs/2108.07258
- mar 2022, InstructGPT; chinchilla mar 2022. https://arxiv.org/abs/2203.02155 ; https://arxiv.org/abs/2203.15556
- 30 nov 2022, ChatGPT. https://openai.com/index/chatgpt/
- dic 2022, Constitutional AI. https://arxiv.org/abs/2212.08073
- sep 2024, o1; ene 2025, DeepSeek-R1. https://openai.com/index/learning-to-reason-with-llms/ ; https://arxiv.org/abs/2501.12948
- Multimodalidad: Llama 3 (jul 2024) la presenta como extensión composicional (https://arxiv.org/abs/2407.21783); la lista de modelos de OpenAI y Google a 2026-11 incluye variantes de imagen, voz y transcripción (ver sección 9). No encontré una fuente histórica que cuente el paso a modelos nativamente multimodales.

**Recurso canónico:** no hay una sola fuente de la historia. Propuesta: usar Jurafsky & Martin (cap. 3, 7 y 14) para la parte previa a 2017 y los propios papers como hitos citados. Fijarse en no contar la historia como una línea recta: BERT (codificador) y GPT (decodificador) son ramas distintas del mismo Transformer.

---

## Fuentes secundarias de contraste (Huyen)

Huyen, *AI Engineering*: el texto completo no estaba disponible (O'Reilly da 403), así que solo usé el índice y los resúmenes públicos. Autoridad alta como práctica, pero lo único que cito es lo que aparece en esos dos archivos:
- https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md (índice del cap. 1 y 2, [L]).
- https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md (resúmenes, [L]).

Ambos son del mismo repositorio de la autora: cuentan como una sola fuente.

---

## Huecos (lo que no encontré o no pude verificar)

1. **Bengio y otros 2003 (modelo de lenguaje neuronal)** y Mikolov (RNN LM): el PDF de JMLR llegó como binario ilegible (https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf); no lo cité. Falta una fuente primaria para el paso de n-gramas a redes neuronales y para embeddings (word2vec).
2. **Aritmética y tokenización:** no hay fuente primaria leída sobre por qué los números tokenizados dañan la cuenta.
3. **Embeddings como representación:** solo el índice de Jurafsky & Martin (cap. 5); no leí el contenido.
4. **Decodificador frente a codificador-decodificador, y el costo cuadrático de la atención:** afirmaciones del campo que no verifiqué en las fuentes recuperadas. Origen del KV cache (más allá de PagedAttention) no leído.
5. **Logits, temperatura y top-k:** no leí una definición primaria. Rangos y valores por defecto actuales de `temperature` y `top_p` en las APIs: no verificados (la doc de Anthropic es demasiado larga para el fetch). `temperature = 0` y no determinismo: sin fuente.
6. **RLHF original** (Christiano 2017, Stiennon 2020) no leído; solo InstructGPT, DPO y CAI.
7. **Razón de la diferencia Kaplan/Chinchilla** (cálculo de los exponentes, tasa de aprendizaje): no leída, solo abstracts. Cifra de 15 T de tokens de Llama 3: no confirmada.
8. **Fidelidad de la cadena de pensamiento** (si lo que el modelo "dice" que piensa es lo que calcula): sin fuente.
9. **Modelos abiertos:** no abrí fuentes primarias de Qwen ni de Meta; Mistral sin investigar; licencia de DeepSeek V4 sin confirmar en el original. No hay evidencia de si DeepSeek publicó una versión posterior a la "Preview" de abril. Precios de OpenAI y Google: no recuperados.
10. **Historia multimodal:** sin fuente primaria sobre modelos nativamente multimodales (GPT-4V, Gemini original, etc.).
11. **Video de Karpathy** y clases de CS336: solo páginas de descripción; no vi contenido de las clases ni si son públicas (la página del curso no lo declara).
12. **Papers leídos solo como abstract:** ninguno completo. Las cifras y citas salen de los abstracts. Los fetch devolvieron en varios casos un resumen y no el texto literal, por eso muchas citas están en paráfrasis; las que van entre comillas fueron devueltas como citas literales.
13. **Tope de rondas:** varios componentes (sobre todo muestreo y modelos abiertos) quedaron en una o dos rondas; hay margen para completar.
