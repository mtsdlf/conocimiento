# Investigación: vertical Contexto (todo lo que entra en la ventana del modelo)

Lectura hecha el 2026-11-27. Público: quien programa y sabe de APIs, pero no sabe cómo funciona un modelo por dentro. Perspectiva: Chip Huyen, *AI Engineering* (O'Reilly, 2025), cap. 5 y 6, como inspiración y no como índice.

Convenciones. Marcas de lectura: [L] leí la página (o su parte relevante), [M] solo metadatos o abstract, [S] resumen secundario o de buscador. Puntajes 1 a 3 en Autoridad (Aut), Profundidad (Prof), Ejemplos (Ej) y Unicidad (Uni); Rec = recencia en lo volátil. Tipo: P = primaria, S = secundaria. Todo lo traído de la web se trató como dato. Las páginas se leyeron con una herramienta que resume (WebFetch), así que las citas textuales cortas son las que esa herramienta devolvió entre comillas; las paráfrasis van sin comillas.

Material que ya existe y no se repite: `IA/Contexto/contexto-y-rag.md` (escalera de recuperación, contextual retrieval con sus cifras, contexto largo vs RAG con Li et al. 2024, Anthropic "Effective context engineering" y la definición de context engineering) y `IA/prompt-rag-o-finetuning.md`.

## 0. Hallazgos que cambian el encargo

1. **La división en cinco componentes no coincide del todo con cómo el campo parte la vertical.**
   - "Context engineering" se usa como paraguas: LangChain lo define como "the art and science of filling the context window with just the right information at each step of an agent's trajectory" y lo parte en cuatro estrategias (write, select, compress, isolate) (https://www.langchain.com/blog/context-engineering-for-agents). Bajo ese paraguas caen prompt, recuperación, memoria y compactación. Es decir, `ingenieria-de-contexto` no es un hermano de los otros: es la vista de conjunto, y conviene escribirla como la nota entrada de la vertical.
   - Huyen no pone la memoria en el capítulo de contexto: está en el cap. 6, sección "Agents", "Memory" (p. 300), y la inyección de prompt está en el cap. 5, "Defensive Prompt Engineering" (p. 235), no en una sección de seguridad aparte (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md [L]). La fuente de Anthropic también ubica la memoria como herramienta de agente (https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool [L]). Propuesta: mantener `memoria` en esta vertical (es contexto persistido) pero enlazarla a Agentes.
   - `inyeccion-de-prompt` es seguridad más que contexto. Entra acá porque el vector de ataque es el propio contexto (datos no confiables dentro de la ventana). Conviene que se enlace a la vertical de seguridad o producción si existe.
   - `contexto-y-rag` y `recuperacion` se solapan. Lo ya escrito cubre la escalera léxica, embeddings, híbrida y reranking a nivel de idea. `recuperacion` debería ser la nota de profundidad (métricas, partición en fragmentos, fusión de rankings, búsqueda agentiva) y `contexto-y-rag` quedar como la visión de conjunto.
2. **Discrepancia a verificar con el libro.** El resumen del cap. 6 en el repo, según la herramienta de lectura, dice que "Chunking and hybrid search aren't discussed in this chapter" y que la búsqueda híbrida aparece solo en un pie de figura del cap. 7 (https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md [L, paráfrasis de la herramienta]). Pero el índice sí lista "Retrieval Optimization" en p. 268 (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md [L]), y la nota existente cita de Huyen una definición de búsqueda híbrida. Lo más probable es que el resumen del repo omita lo que el libro sí trata, pero no se pudo comprobar: el texto del libro no está disponible. No atribuirle a Huyen cifras ni técnicas de partición sin leer esas páginas.
3. **El término "context engineering" tiene una fecha de nacimiento ajustada pero sin fuente primaria leída.** Ver el componente 2.

---

## 1. prompt

### Tabla de fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Rec | Marca |
|---|---|---|---|---|---|---|---|---|
| Anthropic, "Prompting best practices" (referencia viva para los modelos actuales) | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | P | 3 | 3 | 3 | 2 | leída 2026-11-27 | [L] (guardada completa, leída por secciones) |
| Anthropic, "Prompt engineering overview" | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview | P | 3 | 1 | 1 | 1 | leída 2026-11-27 | [L] |
| OpenAI, guía de prompt engineering | https://developers.openai.com/api/docs/guides/prompt-engineering | P | 3 | 2 | 2 | 2 | leída 2026-11-27 | [L] |
| Brown et al., "Language Models are Few-Shot Learners" (arXiv 2005.14165, 2020-05-28) | https://arxiv.org/abs/2005.14165 | P | 3 | 3 | 2 | 3 | 2020 | [M] |
| Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (arXiv 2201.11903, 2022-01-28) | https://arxiv.org/abs/2201.11903 | P | 3 | 3 | 2 | 3 | 2022 | [M] |
| Schulhoff et al., "The Prompt Report" (arXiv 2406.06608, v6 2025-02-26) | https://arxiv.org/abs/2406.06608 | P (survey) | 2 | 3 | 2 | 2 | 2025 | [M] |
| Meincke, Mollick, Mollick, Shapiro, "The Decreasing Value of Chain of Thought in Prompting" (arXiv 2506.07142, 2025-06-08, sin revisión por pares) | https://arxiv.org/abs/2506.07142 | P (preprint) | 2 | 2 | 1 | 3 | 2025 | [M] |
| Huyen, *AI Engineering*, cap. 5, índice y resumen del repo | https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md y .../chapter-summaries.md | P (libro; solo índice y resumen) | 3 | 1 | 1 | 2 | 2025 | [L] del índice y del resumen; el libro no se leyó |
| Hamel Husain, "Your AI Product Needs Evals" (2024-03-29) | https://hamel.dev/blog/posts/evals/ | S (practicante) | 2 | 2 | 2 | 2 | 2024 | [L] |

### Afirmaciones

- **Aprendizaje en contexto.** GPT-3 (175.000 millones de parámetros) se evaluó sin actualizar pesos, con tareas y ejemplos dados solo como texto; los autores afirman que "scaling up language models greatly improves task-agnostic, few-shot performance". https://arxiv.org/abs/2005.14165
- **Cadena de pensamiento.** Con ocho ejemplos que incluyen pasos intermedios, un modelo de 540.000 millones de parámetros alcanzó el estado del arte en GSM8K. https://arxiv.org/abs/2201.11903
- **Catálogo.** The Prompt Report ordena 58 técnicas para modelos de texto, 33 términos de vocabulario y 40 técnicas para otras modalidades. https://arxiv.org/abs/2406.06608
- **Estructura del capítulo de Huyen** (útil como esqueleto de la nota): prompt de sistema y de usuario (p. 215), "Write Clear and Explicit Instructions" (p. 220), "Provide Sufficient Context" (p. 223), "Break Complex Tasks into Simpler Subtasks" (p. 224), "Give the Model Time to Think" (p. 227), "Iterate on Your Prompts" (p. 229), "Organize and Version Prompts" (p. 233). https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
- **Roles de mensaje.** OpenAI: "You could think about `developer` and `user` messages like a function and its arguments in a programming language"; los mensajes de desarrollador tienen prioridad sobre los del usuario. https://developers.openai.com/api/docs/guides/prompt-engineering
- **Ejemplos.** OpenAI: "When providing examples, try to show a diverse range of possible inputs with the desired outputs." Anthropic recomienda "Include 3–5 examples for best results" y envolverlos en etiquetas `<example>`. https://developers.openai.com/api/docs/guides/prompt-engineering y https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **Contexto largo en el prompt.** Anthropic: poner los documentos largos arriba, antes de la consulta, y "Queries at the end can improve response quality by up to 30 percent in tests". Cifra del propio laboratorio. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **Versionar.** OpenAI: fijar la aplicación de producción a una instantánea concreta del modelo; guardar los prompts de producción en el código de la aplicación (no en objetos de prompt reutilizables, que OpenAI está dejando de lado), con revisión y despliegue normales; agregar fixtures y evaluaciones antes de cambiar un prompt. https://developers.openai.com/api/docs/guides/prompt-engineering
- **Antes de tocar el prompt.** Anthropic supone que ya hay criterios de éxito y una forma empírica de probarlos, y avisa que "Not every success criterion or failing eval is best solved by prompt engineering": a veces cambiar de modelo mejora latencia y costo más fácil. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- **Qué perdió peso con modelos más capaces** (cada punto con su fuente):
  - La cadena de pensamiento pedida explícitamente: para modelos sin razonamiento da "a small average improvement" y puede sumar variabilidad; muchos modelos recientes ya razonan sin que se les pida y el efecto es poco; para los que razonan por dentro "often only marginal accuracy gains, if any" con más tokens y tiempo. Es una paráfrasis del abstract. https://arxiv.org/abs/2506.07142
  - El énfasis agresivo: Anthropic dice que los modelos recientes responden más al prompt de sistema y que "Where you might have said 'CRITICAL: You MUST use this tool when...,' you can use more normal prompting such as 'Use this tool when...' instead". https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  - El relleno de la respuesta (*prefill*): desde Claude 4.6 y Mythos Preview los mensajes de asistente prellenados en el último turno devuelven error 400, "most use cases of prefill no longer require it". https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  - Los pasos explícitos según el tipo de modelo: OpenAI dice que a los modelos de razonamiento se les da un objetivo ("like a senior co-worker") y a los GPT instrucciones explícitas ("like a junior coworker"). https://developers.openai.com/api/docs/guides/prompt-engineering
  - Lo que sigue vigente: claridad, contexto, ejemplos, estructura con etiquetas y encadenar tareas complejas siguen en la guía actual de Anthropic. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **Prompts que crecen sin control.** Husain cuenta que en el asistente Lucy de Rechat el prompt engineering "se estancó" y los prompts se volvieron largos y difíciles de manejar a medida que se acumulaban casos borde. https://hamel.dev/blog/posts/evals/ (un solo caso, de un practicante que vende consultoría).

### Discrepancias

- Anthropic y OpenAI no coinciden en el estilo según el modelo: OpenAI separa "modelo de razonamiento = objetivo" de "GPT = pasos explícitos" mientras que Anthropic habla de un solo conjunto de técnicas para todos sus modelos vigentes y migraciones entre versiones. Se presentan las dos; no hay estudio que arbitre.

### Recurso canónico

Para entender: Huyen, cap. 5, de "Introduction to Prompting" (p. 212) a "Organize and Version Prompts" (p. 233), por la estructura de prácticas y por situar el prompt como comunicación y no como truco. Para hacerlo: "Prompting best practices" de Anthropic, por ser la referencia más actual y fechada contra modelos concretos; leer en paralelo la guía de OpenAI para ver qué cambia de proveedor. En qué fijarse: que cada recomendación depende del modelo, y que la regla de ambas es medir antes de iterar.

---

## 2. ingenieria-de-contexto

### Tabla de fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Rec | Marca |
|---|---|---|---|---|---|---|---|---|
| Anthropic, "Effective context engineering for AI agents" (2025-09-29) | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | P | 3 | 3 | 2 | 3 | 2025 | [L] |
| LangChain, "Context Engineering for Agents" (2025-07-02) | https://www.langchain.com/blog/context-engineering-for-agents | S (vendor, practicante) | 2 | 2 | 2 | 2 | 2025 | [L] |
| Simon Willison, "Context engineering" (2025-06-27) | https://simonwillison.net/2025/Jun/27/context-engineering/ | S | 2 | 1 | 1 | 2 | 2025 | [L] |
| Karpathy, post en X del 2025-06-25 | https://x.com/karpathy/status/1937902205765607626 | P (no se pudo abrir: HTTP 402) | 3 | 1 | 1 | 3 | 2025 | [S] vía búsqueda |
| Liu et al., "Lost in the Middle" (arXiv 2307.03172, v3 2023-11-20; TACL) | https://arxiv.org/abs/2307.03172 | P (paper) | 3 | 3 | 2 | 3 | 2023 | [M] |
| Hsieh et al., "RULER" (arXiv 2404.06654, COLM 2024) | https://arxiv.org/abs/2404.06654 | P (paper) | 3 | 3 | 2 | 3 | 2024 | [M] |
| Modarressi et al., "NoLiMa" (arXiv 2502.05167, ICML 2025) | https://arxiv.org/abs/2502.05167 | P (paper) | 3 | 2 | 2 | 3 | 2025 | [M] |
| Hong, Troynikov, Huber (Chroma), "Context Rot" (2025-07-14, informe técnico, sin revisión por pares) | https://www.trychroma.com/research/context-rot | P (reporte de vendor) | 2 | 3 | 2 | 3 | 2025 | [L] |
| Anthropic, docs de compactación | https://platform.claude.com/docs/en/build-with-claude/compaction | P | 3 | 2 | 2 | 3 | leída 2026-11-27 | [L] |

### Afirmaciones

- **Origen del término.** Karpathy respondió el 2025-06-25 a un post de Tobi Lütke (2025-06-18) con "+1 for 'context engineering' over 'prompt engineering'"; la frase "delicate art and science of filling the context window with just the right information for the next step" se le atribuye. No se abrió el post original: las fechas y el texto vienen de reportes secundarios que difieren levemente. https://x.com/karpathy/status/1937902205765607626 [S]; la atribución aparece también en https://www.langchain.com/blog/context-engineering-for-agents
- Willison lo defiende como mejor término: "The term **context engineering** has recently started to gain traction as a better alternative to prompt engineering", porque el significado inferido de "prompt engineering" es "a laughably pretentious term for typing things into a chatbot!". https://simonwillison.net/2025/Jun/27/context-engineering/
- **Cuatro estrategias de LangChain:** write, select, compress, isolate; y Cognition lo llama "effectively the #1 job of engineers building AI agents". https://www.langchain.com/blog/context-engineering-for-agents
- **Anthropic** (lo ya volcado en la base no se repite): el contexto es un recurso finito y los LLM tienen un "attention budget"; "Studies on needle-in-a-haystack style benchmarking have uncovered the concept of context rot"; el prompt de sistema debe estar en "the right altitude" (entre lógica rígida y guía vaga); limpiar resultados de herramientas es "One of the safest lightest touch forms of compaction"; el resumen de compactación en Claude Code conserva "architectural decisions, unresolved bugs, and implementation details"; Claude Code usa un modelo híbrido (CLAUDE.md cargado de entrada; glob y grep en el momento); y "do the simplest thing that works". https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Lost in the middle** (Liu et al., 2023): el rendimiento "is often highest when relevant information occurs at the beginning or end" del contexto y "significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models". Tareas: preguntas sobre varios documentos y recuperación de pares clave-valor. https://arxiv.org/abs/2307.03172
- **RULER** (Hsieh et al., 2024): 17 modelos, 13 tareas; aunque casi todos resuelven la aguja en el pajar simple, casi todos se degradan mucho al crecer el contexto; todos declaran 32K tokens o más, pero solo cerca de la mitad mantiene rendimiento satisfactorio a 32K (paráfrasis del abstract). https://arxiv.org/abs/2404.06654
- **NoLiMa** (ICML 2025): con agujas sin coincidencia literal con la pregunta, a 32K tokens 11 de 13 modelos caen por debajo del 50% de su rendimiento en contexto corto; GPT-4o baja de 99,3% a 69,7%; razonamiento y cadena de pensamiento no evitan del todo la caída (paráfrasis del abstract). https://arxiv.org/abs/2502.05167
- **Context rot** (Chroma, julio de 2025): 18 modelos; "performance grows increasingly unreliable as input length grows"; un solo distractor ya baja el resultado respecto de la base y cuatro lo agravan; los pajares barajados rinden mejor que los coherentes en los 18 modelos ("surprising finding" según los autores); en LongMemEval los prompts enfocados de ~300 tokens rinden mucho más que los de ~113.000 tokens, con la mayor brecha en modelos Claude, en buena parte por abstenciones. Límites que declaran: tareas deliberadamente simples, no explican el mecanismo, solo dos temas de pajar, juez LLM (GPT-4.1). El término "context rot" lo usa la propia Anthropic. https://www.trychroma.com/research/context-rot
- **Compactación como API:** reemplaza los turnos viejos por un resumen escrito en el servidor, "because response quality degrades as a conversation grows"; hay compactación a pedido y por umbral de tokens (ambas en beta en las páginas leídas), y limpieza de resultados o de bloques de pensamiento por regla ("context editing"). https://platform.claude.com/docs/en/build-with-claude/compaction

### Discrepancias

- Todos los estudios de degradación son sobre modelos de 2023 a mediados de 2025. Chroma incluye modelos de 2025 (Claude 4, Gemini 2.5, GPT-4.1) y aun así ve degradación; pero no hay una fuente leída sobre los modelos de contexto largo de 2026 (hueco). Y Chroma es de un vendor de bases vectoriales, con interés en que la recuperación importe.
- Los benchmarks (Lost in the middle, RULER, NoLiMa, Chroma) miden recuperación sintética; Chroma dice que la degradación real en tareas de varios pasos probablemente sea mayor pero no lo probó.

### Recurso canónico

"Effective context engineering for AI agents" (Anthropic): leer completo, y fijarse en la tríada compactación, notas fuera de la ventana y subagentes, y en el consejo final de simplicidad. Para la evidencia de degradación, leer el abstract de Lost in the Middle y el informe de Context Rot (es el más legible y trae modelos actuales). Para entender la etiqueta, el post de LangChain por la taxonomía write, select, compress, isolate.

---

## 3. contexto-y-rag

Ya existe. Lo que falta o contradice, tras revisar las fuentes de esta vertical:

- **Falta:** la evidencia de degradación (sección 2) como argumento para recuperar poco y bueno en vez de meter todo. La nota existente cita la regla de los 200.000 tokens de Anthropic (2024-09) y el debate Li et al., pero no dice que los estudios de degradación dan una razón para preferir contexto enfocado incluso si la base cabe.
- **Falta:** la búsqueda agentiva como alternativa real al índice vectorial (sección 4). La nota solo menciona *agentic RAG* con un survey.
- **Matiz posible:** la nota atribuye a Huyen la definición de RAG con "chunks" y de búsqueda híbrida; ver hallazgo 2 sobre la discrepancia con el resumen del repo.
- **Nada contradice** las cifras de contextual retrieval (35%, 49%, 67%). Se releyó la fuente: la prueba usó los 20 mejores fragmentos y concluyó "We tried delivering 5, 10, and 20 chunks, and found using 20 to be the most performant of these options"; los fragmentos suelen ser de "no more than a few hundred tokens"; el costo único de contextualizar es "$1.02 per million document tokens"; y recomiendan embeddings de Gemini y Voyage. https://www.anthropic.com/news/contextual-retrieval [L, 2024-09-19]

---

## 4. recuperacion

### Tabla de fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Rec | Marca |
|---|---|---|---|---|---|---|---|---|
| Karpukhin et al., "Dense Passage Retrieval" (arXiv 2004.04906, EMNLP 2020) | https://arxiv.org/abs/2004.04906 | P | 3 | 3 | 2 | 3 | 2020 | [M] |
| Thakur et al., "BEIR" (arXiv 2104.08663, NeurIPS 2021 Datasets) | https://arxiv.org/abs/2104.08663 | P | 3 | 3 | 2 | 3 | 2021 | [M] |
| Nogueira y Cho, "Passage Re-ranking with BERT" (arXiv 1901.04085) | https://arxiv.org/abs/1901.04085 | P | 3 | 2 | 1 | 3 | 2019 | [M] |
| Sentence-Transformers, "Retrieve & Re-Rank" | https://www.sbert.net/examples/applications/retrieve_rerank/README.html | P (docs de librería) | 2 | 2 | 2 | 2 | leída 2026-11-27 | [L] |
| Cormack, Clarke, Büttcher, "Reciprocal rank fusion..." (SIGIR 2009) | https://research.google/pubs/pub36196/ | P | 3 | 2 | 1 | 3 | 2009 | [S] (solo la ficha, vía buscador) |
| Elastic, docs de Reciprocal Rank Fusion | https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion | P (producto) | 2 | 2 | 2 | 1 | leída 2026-11-27 | [L] |
| Anthropic, "Introducing Contextual Retrieval" (2024-09-19) | https://www.anthropic.com/news/contextual-retrieval | P | 3 | 2 | 3 | 3 | 2024 | [L] |
| Smith y Troynikov (Chroma), "Evaluating Chunking Strategies for Retrieval" (2024-07-03) | https://www.trychroma.com/research/evaluating-chunking | P (reporte de vendor) | 2 | 2 | 3 | 3 | 2024 | [L] |
| Wikipedia, "Discounted cumulative gain" | https://en.wikipedia.org/wiki/Discounted_cumulative_gain | S | 1 | 2 | 1 | 1 | leída 2026-11-27 | [L] |
| Informes sobre el cambio de Claude Code a búsqueda agentiva (Pragmatic Engineer, OfficeChai, otros) | https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny y https://officechai.com/ai/claude-researcher-explains-how-agentic-search-performed-better-than-rag-for-code-generation/ | S (varias notas sobre el mismo podcast y charla: cuentan como una fuente) | 1 | 1 | 1 | 2 | 2025 | [S] vía buscador |
| Anthropic, "Effective context engineering..." (sección just-in-time) | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | P | 3 | 2 | 2 | 3 | 2025 | [L] |

### Afirmaciones

- **Densa vs léxica.** DPR: un recuperador denso de doble codificador supera a un BM25 de Lucene "by 9%–19% absolute" en precisión de recuperación en los 20 primeros, en varios datasets de QA abierta (paráfrasis del abstract). https://arxiv.org/abs/2004.04906
- **Pero en cero disparos BM25 aguanta.** BEIR: BM25 es "a robust baseline"; los rerankers y los modelos de interacción tardía logran el mejor promedio en cero disparos con alto costo de cómputo; los densos y dispersos son más baratos pero "often underperform" y dejan espacio para mejorar la generalización (paráfrasis). https://arxiv.org/abs/2104.08663. Las dos fuentes (2020 y 2021) se leen juntas: un denso entrenado en el dominio le gana a BM25, uno que se usa en otro dominio no necesariamente.
- **Reranking.** Un cross-encoder pasa la consulta y el documento juntos por el modelo y da un puntaje, con más precisión pero con costo proporcional a la cantidad de candidatos; por eso se aplica a unos ~100 candidatos que trajo un recuperador barato. https://www.sbert.net/examples/applications/retrieve_rerank/README.html. Origen: Nogueira y Cho superan al mejor anterior "by 27% (relative) in MRR@10" en MS MARCO. https://arxiv.org/abs/1901.04085
- **Fusión híbrida.** RRF suma, para cada documento, 1/(k + posición) por cada lista donde aparece; k por defecto en Elastic es 60; usa solo posiciones, así que no hay que normalizar puntajes de BM25 contra similitud de vectores y "requires no tuning". https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion. El método es de Cormack et al., SIGIR 2009. https://research.google/pubs/pub36196/ [S]. Anthropic combina BM25 y embeddings con "rank fusion techniques" (sin nombrar RRF). https://www.anthropic.com/news/contextual-retrieval
- **Partición en fragmentos.** En el estudio de Chroma, con 472 consultas sintéticas sobre cinco corpus (328.208 tokens), unas estrategias superan a otras "by up to 9% in recall"; la partición recursiva de 200 tokens sin solapamiento tuvo recall de 88,1 con buen desempeño parejo; la configuración por defecto de OpenAI Assistants (800 tokens, 400 de solapamiento) tuvo el peor puntaje en las otras métricas (precisión 1,4); bajar el solapamiento mejora IoU. Límites declarados: consultas generadas por LLM ("tend to generate a specific style of question"), dataset chico, no se midió tiempo. https://www.trychroma.com/research/evaluating-chunking. Anthropic dice que el tamaño, el borde y el solapamiento "can affect retrieval performance". https://www.anthropic.com/news/contextual-retrieval
- **Métricas.** nDCG: DCG suma la relevancia de cada resultado dividida por log2(posición + 1); nDCG divide por el DCG ideal y queda entre 0 y 1; y "Normalized DCG does not penalize missing documents in the result" salvo que se fije el tamaño del conjunto. https://en.wikipedia.org/wiki/Discounted_cumulative_gain (fuente secundaria). Las cifras de recall aparecen en las fuentes de Chroma y Anthropic ("failure rate" de los 20 primeros). **No hay fuente primaria leída que defina recall@k y precision@k:** hueco.
- **Búsqueda agentiva vs vector store.** Anthropic describe el modelo en que el agente guarda "lightweight identifiers (file paths, stored queries, web links, etc.)" y carga los datos al ejecutar, con glob y grep en Claude Code, junto con carga previa (CLAUDE.md). https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents. Boris Cherny, creador de Claude Code, habría dicho que probaron RAG con base vectorial local y pasaron a búsqueda agentiva, con resultado "mostly vibes" más algo de benchmarks internos, y que el paso de indexar y la desactualización del índice fueron razones; costo: más latencia y tokens. Todo esto es secundario (no se pudo abrir el original) y de un solo origen, tratado como una fuente. https://officechai.com/ai/claude-researcher-explains-how-agentic-search-performed-better-than-rag-for-code-generation/ [S]. Contra: un ingeniero de turbopuffer comenta que no prueba que la recuperación semántica no sirva para todo agente de código (https://ai.engineer/talks/UM6sFg_jdlE-rag-is-dead-right-kuba-rogut [S]). Se presentan las dos; es caso de código, no se generaliza a documentos de empresa.

### Discrepancias

- DPR (densa gana) vs BEIR (BM25 robusta, densa generaliza peor): se explican por si hay entrenamiento en el dominio, pero se dan las dos.
- Búsqueda agentiva vs vector store: sin estudio controlado; solo relatos y un contra-comentario.

### Recurso canónico

Para entender y decidir: Huyen, cap. 6 "Retrieval Algorithms" (p. 257) y "Retrieval Optimization" (p. 268), con la salvedad del hallazgo 2. Para hacerlo: el post de Contextual Retrieval de Anthropic (mejor ejemplo de medir cada escalón) y los docs de Sentence-Transformers "Retrieve & Re-Rank". Para decidir con números propios: el informe de partición de Chroma, leído como ejemplo de método (consultas sintéticas, métricas por token) y no como receta. En qué fijarse: separar si falló el recuperador o el modelo, y medir recall en los primeros k antes de tocar el generador.

---

## 5. memoria

### Tabla de fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Rec | Marca |
|---|---|---|---|---|---|---|---|---|
| Packer et al., "MemGPT: Towards LLMs as Operating Systems" (arXiv 2310.08560, v2 2024-02-12) | https://arxiv.org/abs/2310.08560 | P | 2 | 3 | 2 | 3 | 2023 | [M] |
| Chhikara et al., "Mem0" (arXiv 2504.19413, 2025-04-28, sin revisión por pares; los autores son los del producto) | https://arxiv.org/abs/2504.19413 | P (preprint, vendor) | 1 | 2 | 2 | 2 | 2025 | [M] |
| Anthropic, docs de la herramienta de memoria | https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | P | 3 | 3 | 3 | 3 | leída 2026-11-27 | [L] |
| Anthropic, docs de compactación | https://platform.claude.com/docs/en/build-with-claude/compaction | P | 3 | 2 | 2 | 2 | leída 2026-11-27 | [L] |
| OpenAI, "Memory FAQ" (ChatGPT) | https://help.openai.com/en/articles/8590148-memory-faq | P | 3 | 2 | 1 | 3 | leída 2026-11-27 | [L] |
| Anthropic, ayuda: chat search y memoria de Claude | https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-conversations | P | 3 | 2 | 1 | 3 | leída 2026-11-27 | [L] |
| Huyen, *AI Engineering*, cap. 6, "Memory" (p. 300) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md | P (libro; solo índice) | 3 | 1 | 1 | 2 | 2025 | [L] solo el índice |

### Afirmaciones

- **Idea de MemGPT.** "Virtual context management", tomada de la memoria jerárquica de los sistemas operativos: mover datos entre niveles de memoria rápida y lenta, con interrupciones para el control entre modelo y usuario; evaluado en análisis de documentos grandes y chat de varias sesiones (paráfrasis del abstract). https://arxiv.org/abs/2310.08560
- **Memoria como herramienta (API).** La herramienta de memoria de Anthropic corre del lado del cliente: Claude pide operaciones de archivo (view, create, str_replace, insert, delete, rename) sobre un directorio `/memories` y la aplicación las ejecuta con su propio almacenamiento; "Rather than loading all relevant information up front, an agent records what it learns in memory files and reads them back on demand". El sistema agrega la instrucción "ASSUME INTERRUPTION: Your context window might be reset at any moment". https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- **Riesgos que la propia doc nombra:** validar rutas contra el recorrido de directorios ("`/memories/../../secrets.env`"), limitar el tamaño de los archivos, vencer memorias viejas, y que Claude "usually refuses" a guardar datos sensibles pero para garantías hay que validar en el código. https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- **Memoria y compactación son piezas distintas:** la compactación resume el historial en el servidor; la memoria "preserves the information that must survive summarization". Recomiendan usar las dos en agentes largos. https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- **Patrón para varias sesiones:** una sesión inicial arma el registro de progreso y la lista de funciones; las siguientes los leen al arrancar y los actualizan al cerrar; "Mark a feature complete only after end-to-end verification". https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- **Resumen y recuperación (Mem0).** Los autores reportan en LOCOMO "26% relative improvements in the LLM-as-a-Judge metric over OpenAI", 91% menos de latencia p95 y más del 90% de ahorro de tokens frente a pasar todo el contexto. Son autores del producto y el estudio no pasó revisión por pares. https://arxiv.org/abs/2504.19413
- **Memoria de ChatGPT:** dos mecanismos, "saved memories" (detalles que se piden guardar o que se guardan; viven aparte: borrar el chat original no las borra) y "reference chat history" (usa chats pasados relevantes); los chats temporales "do not create or update memories". Apagar la referencia de memorias guardadas apaga también la de historial. https://help.openai.com/en/articles/8590148-memory-faq
- **Memoria de Claude:** guarda "individual topics as you chat"; cada proyecto tiene su memoria separada; temas sensibles (salud, política, religión) no se guardan por defecto; hay pausa, reinicio, modo incógnito, y borrar una conversación no borra las memorias generadas de ella; en planes de equipo y empresa depende de quien administra, y las organizaciones creadas desde el 2026-10-31 arrancan con memoria activada. https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-conversations (volátil: leída 2026-11-27).
- Los resultados de memoria son "contexto no confiable" en términos de seguridad: lo que se guarda lo escribió el modelo a partir de entradas que pueden estar envenenadas (inferencia de esta base; no se encontró un estudio leído sobre envenenamiento de memorias: hueco).

### Discrepancias

- ChatGPT mezcla guardado explícito más referencia al historial; Claude guarda por temas y separa por proyecto. No hay una taxonomía común ni un estudio comparativo (hueco). La división corto plazo / largo plazo del encargo es de Huyen y de la literatura de agentes, y las páginas de producto no usan esos términos.

### Recurso canónico

Huyen, cap. 6 "Memory" (p. 300, solo índice leído: decir que no se leyó). Para entender el mecanismo, el abstract de MemGPT, que fundó la idea de memoria jerárquica. Para hacerlo, la doc de la herramienta de memoria de Anthropic, por ser la única fuente con API, errores y seguridad. En qué fijarse: que la memoria es un archivo o una base que la aplicación controla, no algo que el modelo "tiene", y que hay que decidir qué se escribe, quién lo puede borrar y cuándo vence.

---

## 6. inyeccion-de-prompt

Seguridad es alto riesgo: la afirmación central ("no hay defensa completa") se apoya en cinco fuentes independientes (OWASP, NCSC, Willison, Nasr et al., Anthropic). Los detalles de cada defensa tienen una o dos fuentes y se marca.

### Tabla de fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Rec | Marca |
|---|---|---|---|---|---|---|---|---|
| OWASP, Top 10 for LLM Applications 2025 (lista) | https://genai.owasp.org/llm-top-10/ | P (estándar) | 3 | 2 | 2 | 3 | 2025 | [L] |
| OWASP, LLM01:2025 Prompt Injection | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | P | 3 | 2 | 2 | 3 | 2025 | [L] |
| OWASP, LLM07:2025 System Prompt Leakage | https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/ | P | 3 | 2 | 1 | 3 | 2025 | [L] |
| Greshake et al., "Not what you've signed up for" (arXiv 2302.12173, 2023-02-23) | https://arxiv.org/abs/2302.12173 | P | 3 | 3 | 3 | 3 | 2023 | [M] |
| Perez y Ribeiro, "Ignore Previous Prompt" (arXiv 2211.09527, 2022-11-17) | https://arxiv.org/abs/2211.09527 | P | 2 | 2 | 2 | 3 | 2022 | [M] |
| Willison, "Prompt injection attacks against GPT-3" (2022-09-12) | https://simonwillison.net/2022/Sep/12/prompt-injection/ | S (practicante; acuñó el término) | 2 | 1 | 2 | 3 | 2022 | [L] |
| Willison, "The Dual LLM pattern" (2023-04-25) | https://simonwillison.net/2023/Apr/25/dual-llm-pattern/ | S | 2 | 2 | 2 | 3 | 2023 | [L] |
| Willison, "The lethal trifecta" (2025-06-16) | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | S | 2 | 2 | 2 | 3 | 2025 | [L] |
| Willison, "CaMeL offers a promising new direction" (2025-04-11) | https://simonwillison.net/2025/Apr/11/camel/ | S | 2 | 2 | 2 | 1 | 2025 | [L] |
| Debenedetti et al., "Defeating Prompt Injections by Design" (CaMeL; arXiv 2503.18813, v2 2025-06-24, DeepMind y ETH) | https://arxiv.org/abs/2503.18813 | P (preprint) | 3 | 3 | 2 | 3 | 2025 | [M] |
| 14 autores (entre ellos Tramèr), "Design Patterns for Securing LLM Agents against Prompt Injections" (arXiv 2506.08837, 2025-06-10) | https://arxiv.org/abs/2506.08837 | P (preprint) | 3 | 3 | 3 | 3 | 2025 | [S] (el abstract no se abrió; seis patrones vía Willison) |
| Willison, "Design Patterns for Securing LLM Agents" (2025-06-13) | https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/ | S | 2 | 2 | 2 | 1 | 2025 | [L] |
| Wallace et al., "The Instruction Hierarchy" (OpenAI, arXiv 2404.13208, 2024-04-19) | https://arxiv.org/abs/2404.13208 | P (preprint de laboratorio) | 3 | 2 | 2 | 3 | 2024 | [M] |
| Nasr et al., "The Attacker Moves Second" (arXiv 2510.09023, 2025-10-10, sin revisión por pares) | https://arxiv.org/abs/2510.09023 | P (preprint) | 3 | 2 | 2 | 3 | 2025 | [M] |
| NCSC (Reino Unido), "Prompt injection is not SQL injection (it may be worse)" (2025-12-08) | https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection | P (agencia gubernamental) | 3 | 2 | 1 | 3 | 2025 | [L] |
| Anthropic, defensas contra inyección en uso de navegador (2025-11-24) | https://www.anthropic.com/research/prompt-injection-defenses | P (lab) | 3 | 2 | 2 | 3 | 2025 | [L] |
| Huyen, cap. 5: "Defensive Prompt Engineering" (p. 235) a "Defenses Against Prompt Attacks" (p. 248) | https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md | P (libro; solo índice y resumen) | 3 | 1 | 1 | 2 | 2025 | [L] solo índice y resumen |

### Afirmaciones

**Qué es y cómo se llama**
- **Origen del término:** Willison lo propuso el 2022-09-12 ("I propose that the obvious name for this should be prompt injection") y lo comparó con la inyección SQL: la analogía es construir prompts concatenando entrada no confiable. https://simonwillison.net/2022/Sep/12/prompt-injection/. Perez y Ribeiro, dos meses después, estudian "goal hijacking" y "prompt leaking" con el marco PromptInject sobre GPT-3. https://arxiv.org/abs/2211.09527
- **Directa e indirecta:** OWASP: directa, "A user's prompt alters the model's behavior"; indirecta, el modelo procesa contenido externo (páginas, archivos) con instrucciones; y el texto malicioso no tiene que ser visible para humanos mientras el modelo lo parsee. https://genai.owasp.org/llmrisk/llm01-prompt-injection/. La indirecta la formalizaron Greshake et al.: los atacantes plantan instrucciones en datos que el modelo probablemente recupere; la taxonomía incluye robo de datos, "worming" y contaminación del ecosistema de información, demostrada contra Bing Chat con GPT-4 y apps sintéticas (paráfrasis del abstract). https://arxiv.org/abs/2302.12173
- **Versión vigente de OWASP:** la página lista la edición 2025: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption. La página enlaza además una "LLM Top 10 for 2026" cuyo contenido no se pudo confirmar. https://genai.owasp.org/llm-top-10/ (volátil: verificar si salió la edición 2026 antes de publicar la nota).
- **Extracción de prompt:** OWASP LLM07: el prompt de sistema "should not be treated as a secret or as a security control"; no poner credenciales, conexiones ni roles adentro, y hacer los controles de seguridad fuera del modelo. https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/. En Huyen el tema es "Proprietary Prompts and Reverse Prompt Engineering" (p. 236) e "Information Extraction" (p. 243). https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
- **Jailbreak vs inyección:** el mismo resumen y el índice de Huyen los juntan (sección "Jailbreaking and Prompt Injection", p. 238). Es un hueco de definición: no se leyó una fuente que los separe con precisión (ver huecos). https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md

**Por qué no hay defensa completa (cinco fuentes independientes)**
1. OWASP: "it is unclear if there are fool-proof methods of prevention for prompt injection", y RAG y fine-tuning no lo mitigan del todo. https://genai.owasp.org/llmrisk/llm01-prompt-injection/
2. NCSC: "Current large language models (LLMs) simply do not enforce a security boundary between instructions and data inside a prompt"; "there's a good chance prompt injection will never be properly mitigated"; el modelo es un "inherently confusable deputy"; si el sistema no tolera el riesgo residual, quizá un LLM no sea la opción adecuada. https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
3. Willison: "we still don't know how to 100% reliably prevent this from happening", y un 95% de ataques detectados es "very much a failing grade". https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
4. Nasr et al. (14 autores): con ataques adaptativos (descenso de gradiente, aprendizaje por refuerzo, búsqueda aleatoria, exploración guiada por humanos) pasaron 12 defensas recientes con tasa de éxito "above 90% for most", y la mayoría de ellas había reportado casi cero (paráfrasis del abstract). Es preprint sin revisión por pares. https://arxiv.org/abs/2510.09023
5. Anthropic: tras sus mejoras, el ataque interno Best-of-N (100 intentos por entorno) tuvo éxito 1,4% en Claude Opus 4.5 (8,0% sin salvaguardas), 2,0% en Sonnet 4, 1,9% en Sonnet 4.5 y 2,4% en Haiku 4.5; dicen que es "far from a solved problem", que 1% "still represents meaningful risk" y que "no browser agent is immune". Cifras del laboratorio, sobre su propio atacante. https://www.anthropic.com/research/prompt-injection-defenses
   Huyen coincide en el resumen del cap. 5: "no defense is foolproof" (paráfrasis de la herramienta de lectura). https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md

**Defensas, con su fuente**
- **Lista de OWASP:** limitar el comportamiento con el prompt de sistema; definir formatos de salida y validarlos con código determinista; filtrar entradas y salidas; mínimo privilegio con las funciones privilegiadas en el código y no en el modelo; aprobación humana para acciones de alto riesgo; separar y etiquetar el contenido externo; pruebas adversarias tratando al modelo como usuario no confiable. https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- **NCSC** coincide en diseño seguro (asumir que el modelo se puede manipular, salvaguardas determinísticas en herramientas y APIs, "an LLM handling a party's content should hold no more privilege than that party"), pide marcar el contenido no confiable como datos (por ejemplo con etiquetas XML), no depender de listas de frases prohibidas, desconfiar de productos que prometen "detener" la inyección y registrar entradas, salidas y llamadas a herramientas. https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
- **Jerarquía de instrucciones** (OpenAI, 2024): entrenar al modelo para que priorice las instrucciones privilegiadas sobre las de usuarios y terceros; mejora la robustez en GPT-3.5 "with minimal loss in standard capabilities" (paráfrasis del abstract). Es una defensa a nivel de modelo, no reemplaza el diseño del sistema. https://arxiv.org/abs/2404.13208
- **Doble LLM** (Willison, 2023): un LLM privilegiado recibe entrada confiable y tiene herramientas; uno en cuarentena procesa contenido no confiable, sin herramientas, y su salida sin filtrar nunca llega al privilegiado. Willison mismo escribe que "This solution is pretty bad", que "isn't a 100% reliable solution" por la ingeniería social, y en la actualización de 2025 que CaMeL "highlights a potential flaw" en su propuesta. https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
- **CaMeL** (DeepMind y ETH, 2025): el modelo privilegiado escribe código en un subconjunto de Python que un intérprete propio ejecuta; el modelo en cuarentena solo parsea datos; las "capabilities" son etiquetas sobre las variables que registran origen y permisos, y las políticas autorizan o bloquean acciones. Resultado en AgentDojo: resuelve 77% de las tareas con seguridad demostrable, frente a 84% de un sistema sin defensa (paráfrasis del abstract). https://arxiv.org/abs/2503.18813. Willison lo llama "the first credible prompt injection mitigation I've seen that doesn't just throw more AI at the problem", y anota los costos: fatiga de aprobaciones y tener que escribir y mantener políticas de seguridad. https://simonwillison.net/2025/Apr/11/camel/
- **Seis patrones de diseño** (Willison resume el paper de junio de 2025): Action-Selector, Plan-Then-Execute, LLM Map-Reduce, Dual LLM, Code-Then-Execute y Context-Minimization; la idea común, cita del paper vía Willison: "once an LLM agent has ingested untrusted input, it must be constrained so that it is impossible for that input to trigger any consequential actions". https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/ y https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ (el abstract del paper original no se abrió: [S]).
- **Lethal trifecta** (Willison, 2025-06-16): tres capacidades que combinadas en un agente permiten robar datos: "Access to your private data", "Exposure to untrusted content" y "The ability to externally communicate"; "The only way to stay safe there is to avoid that lethal trifecta combination entirely." Es un marco de un solo autor, no un estándar; sirve como regla de diseño mnemotécnica. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Huyen lista "Defenses Against Prompt Attacks" (p. 248) y la sección de riesgos del cap. 6 vincula el uso de herramientas con ellos; el detalle de sus defensas no se leyó. https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md

### Discrepancias

- **Filtros y detectores.** OWASP los incluye entre las mitigaciones ("semantic filters"); Willison y el NCSC son escépticos con los productos de guardrails y con las listas de frases. Nasr et al. (preprint) muestra que defensas reportadas como casi perfectas fallan con atacantes adaptativos. Se presentan las dos posturas: sirven como capa que sube el costo del ataque, no como garantía.
- **Cuánto baja el riesgo la capacitación del modelo.** Anthropic reporta 1,4% a 2,4% contra su propio atacante; Nasr et al. muestran más de 90% contra otras defensas con atacantes adaptativos. No son comparables: distinto atacante, distinto entorno, uno del vendor.
- **CaMeL:** el paper afirma "provable security" y Willison lo valora, pero el propio abstract cuenta un costo de utilidad (77% vs 84%), y Willison nota fatiga de usuario.

### Recurso canónico

Para decidir: la nota del NCSC (la mejor explicación corta de por qué no es inyección SQL) más el post de la lethal trifecta de Willison. Para clasificar y auditar: OWASP LLM01 y LLM07 (la lista 2025). Para la historia: Greshake et al. (2023) por la inyección indirecta. Para diseñar: el artículo de patrones de diseño (leer el original en arXiv, solo se leyó el resumen de Willison) y CaMeL. Libro: Huyen, cap. 5, desde "Defensive Prompt Engineering" (p. 235) hasta "Summary" (p. 251). En qué fijarse: la defensa que sirve es limitar lo que el modelo puede hacer una vez que leyó algo no confiable (privilegios, acciones, canales de salida), no mejorar el prompt de sistema.

---

## Huecos

1. **Karpathy, post original.** El enlace devolvió HTTP 402. Fecha y frase salen de reportes secundarios que discrepan en la redacción. Si la nota va a citar la frase, verificarla en el original.
2. **Huyen, texto de los capítulos 5 y 6.** Solo se leyeron el índice y el resumen del repo. No se puede afirmar qué dice sobre partición, búsqueda híbrida, memoria ni defensas, y hay una discrepancia sin resolver con el resumen (hallazgo 2).
3. **Degradación en modelos de contexto largo de 2026.** Todo lo leído llega hasta mediados de 2025. No hay fuente leída sobre si "lost in the middle" persiste en los modelos de 2026. Las recomendaciones de colocación en Anthropic (documentos arriba, consulta al final) están vigentes en su guía actual, pero con la cifra de 30% de pruebas propias.
4. **Métricas de recuperación.** No hay fuente primaria o de manual leída que defina recall@k, precision@k y MRR; nDCG solo viene de Wikipedia (secundaria). El manual de Manning, Raghavan y Schütze (nlp.stanford.edu/IR-book) falló por conexión rechazada; reintentar.
5. **BM25.** No se leyó una fuente primaria sobre BM25 (Robertson y Zaragoza) ni la ficha del paper de RRF más allá del resumen del buscador.
6. **Búsqueda agentiva vs índice vectorial.** Solo hay relatos secundarios sobre Claude Code, de un solo origen, y no hay estudio controlado. Una fuente primaria sería la charla o el podcast original.
7. **Recuperación en castellano.** Ya era hueco en la nota existente: no se buscó nada sobre embeddings o partición para textos en castellano.
8. **Memoria.** No hay fuente leída que compare estrategias (ventana deslizante, resumen, recuperación) en una aplicación común, ni sobre envenenamiento de memorias. La memoria de producto (ChatGPT, Claude) se apoya solo en sus páginas de ayuda; MemGPT y Mem0 solo en el abstract (Mem0 es del vendor, sin revisión por pares).
9. **Jailbreak vs inyección.** No se leyó una fuente que los distinga con precisión (el consenso habitual es: el jailbreak apunta a saltarse las reglas del modelo; la inyección, a que el modelo siga instrucciones ajenas a la aplicación). Falta una fuente primaria; Wallace et al. y Perez y Ribeiro tratan los dos pero sin definición leída.
10. **Seguridad con una sola fuente.** El abstract del paper de seis patrones de diseño no se abrió (solo la reseña de Willison, una fuente). La lethal trifecta es de un solo autor. La OWASP 2026 se menciona sin contenido.
11. **Prompt: otros proveedores.** No se leyó la guía de Google (Gemini) y no hay estudio leído sobre el costo de versionar y evaluar prompts más allá de OpenAI y Husain (un caso).
12. **Eugene Yan** no se consultó (la regla de tres rondas por componente se agotó con otros temas).
