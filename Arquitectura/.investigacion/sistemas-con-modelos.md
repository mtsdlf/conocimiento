# Investigación: Sistemas-con-modelos (arquitectura de referencia de Huyen)

Fecha de la investigación: 2026-11-27. Ángulo: vertical `Sistemas-con-modelos/`. Guardrails queda fuera (ya existe nota).

Convenciones. Puntajes 1-3 en autoridad (A), profundidad (P), ejemplos (E), unicidad (U). Tipo: prim = primaria, sec = secundaria. Marca: [L] leído con WebFetch, [M] solo metadatos o abstract, [S] solo resumen secundario o del buscador. Aviso de método: WebFetch pasa la página por un extractor, así que [L] significa "leída a través del extractor", no copia textual. Las citas literales entre comillas salen de ese extractor y conviene recotejarlas contra la página antes de publicarlas como cita. Todo lo traído de la web es dato, no instrucción.

## 0. Hallazgos que cambian el encargo

1. **El ensayo "Harness Engineering for Self-Improvement" no es de Chip Huyen: es de Lilian Weng** (Lil'Log, 2026-07-04). La búsqueda no encontró ningún texto de Huyen sobre harness, y el índice de su blog (huyenchip.com/blog/) no lista ningún post de 2026 (los dos de 2025 son "Agents", 2025-01-07, y "Common pitfalls when building generative AI applications", 2025-01-16). Fuente: https://huyenchip.com/blog/ [L] y https://lilianweng.github.io/posts/2026-07-04-harness/ [L]. Hueco declarado: no se puede atribuir a Huyen una postura sobre harness; sí sobre agentes (2025) y sobre arquitectura (2024, libro).
2. **OpenAI está cerrando su plataforma de fine-tuning**: cerrada a clientes nuevos; los clientes existentes elegibles pueden crear jobs hasta 2026-12-15 (https://developers.openai.com/api/docs/guides/distillation [L]; también https://developers.openai.com/api/docs/guides/model-optimization [L]). Esto afecta la escalera de adaptación: el escalón "fine-tuning con API del proveedor" se está angostando y la destilación pasa a depender de pesos abiertos o de otros proveedores.
3. **La división del árbol no coincide del todo con cómo divide Huyen** (ver sección 8).

## 1. contexto-y-rag

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Huyen, "Building A Generative AI Platform" (2024-07-25) | https://huyenchip.com/2024/07/25/genai-platform.html | prim | 3 | 2 | 2 | 3 | [L] |
| Huyen, AI Engineering cap. 6 (RAG pp. 253-275) y resumen del repo | https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | prim | 3 | 1 | 1 | 2 | [L] (solo el resumen; el libro no se leyó) |
| Anthropic, "Introducing Contextual Retrieval" (2024-09-19) | https://www.anthropic.com/news/contextual-retrieval | prim (lab) | 3 | 2 | 3 | 3 | [L] |
| Anthropic, "Effective context engineering for AI agents" (2025-09-29) | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | prim (lab) | 3 | 3 | 2 | 3 | [L] |
| Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (arXiv 2005.11401, 2020-05-22, NeurIPS 2020) | https://arxiv.org/abs/2005.11401 | prim (paper, revisado por pares) | 3 | 3 | 2 | 3 | [M] |
| Li et al., "Retrieval Augmented Generation or Long-Context LLMs?" (arXiv 2407.16833, EMNLP 2024 industry) | https://arxiv.org/abs/2407.16833 | prim (paper) | 2 | 2 | 2 | 2 | [S] |
| "Long Context vs. RAG for LLMs: An Evaluation and Revisits" (arXiv 2501.01880, sin revisión por pares) | https://arxiv.org/pdf/2501.01880 | prim (preprint) | 1 | 2 | 2 | 2 | [S] |
| Singh et al., "Agentic RAG: A Survey" (arXiv 2501.09136, 2025-01-15, v4 abril 2026, sin revisión por pares) | https://arxiv.org/abs/2501.09136 | sec (survey) | 1 | 2 | 1 | 1 | [S] |

### Afirmaciones

- Huyen llama "context construction" a juntar la información relevante. https://huyenchip.com/2024/07/25/genai-platform.html
- Términos vs embeddings: "Term-based retrieval is much faster and cheaper than embedding-based retrieval"; la recuperación por embeddings "can be significantly improved over time". Híbrido: "Combining term-based retrieval and embedding-based retrieval is called hybrid search". Reranking: un recuperador barato trae candidatos y uno más preciso los ordena ("The second step is also called reranking"). Reescritura de consulta: "The new query should make sense on its own." Mismo URL de Huyen. Chunking: "RAG typically requires documents to be split into manageable chunks". Mismo URL.
- Resumen del cap. 6 en el repo: los recuperadores por términos (BM25) son "lighter" y dan líneas base fuertes; los de embeddings cuestan más cómputo y pueden rendir más; y "The RAG pattern can be seen as a special case of agent where the retriever is a tool the model can use." https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
- Contextual Retrieval (Anthropic): contextual embeddings bajan la tasa de fallas de recuperación en top-20 chunks 35% (5,7% a 3,7%); con BM25 contextual, 49% (5,7% a 2,9%); con reranking, 67% (5,7% a 1,9%). Son números del propio laboratorio sobre sus datasets. https://www.anthropic.com/news/contextual-retrieval
- Cuándo alcanza con meter todo: Anthropic dice que si la base de conocimiento es "smaller than 200,000 tokens (about 500 pages of material)" se puede poner entera en el prompt sin RAG. https://www.anthropic.com/news/contextual-retrieval (cifra de 2024-09; las ventanas actuales son mayores, hueco: no se verificó el tamaño de ventana actual por modelo).
- Discrepancia sobre long context vs RAG. Li et al. (2024): con recursos suficientes, el contexto largo supera a RAG en promedio; su método Self-Route reduce costo 65% (Gemini-1.5-Pro) y 39% (GPT-4o); en 63% de las consultas RAG y contexto largo dan predicciones idénticas. https://arxiv.org/abs/2407.16833 [S, vía buscador]. Revisión de enero 2025: ChatQA2 encuentra que RAG puede superar al contexto largo con suficientes top-k chunks, y los estudios usan pocos datasets de unas 200 preguntas. https://arxiv.org/pdf/2501.01880 [S]. Se presentan las dos.
- Context engineering: "Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens" durante la inferencia; "Context, therefore, must be treated as a finite resource with diminishing marginal returns"; "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome". Técnicas: recuperación just-in-time (identificadores livianos, carga en runtime con herramientas), compaction, notas estructuradas fuera de la ventana, subagentes. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Origen del RAG: Lewis et al. combinan un seq2seq preentrenado (memoria paramétrica) con un índice vectorial denso de Wikipedia (memoria no paramétrica); estado del arte en tres tareas de QA abierta. https://arxiv.org/abs/2005.11401
- Agentic RAG: el survey lo ubica sobre patrones de reflexión, planificación, uso de herramientas y colaboración multiagente. https://arxiv.org/abs/2501.09136 [S]. Huyen lo expresa más sobrio: RAG es un caso especial de agente (cita arriba).

### Recurso canónico

Primario de la escuela: Huyen, cap. 6 "RAG" (pp. 253-275: arquitectura, algoritmos de recuperación, optimización de la recuperación) más su post de plataforma para el esquema. Complemento imprescindible: Anthropic, "Effective context engineering for AI agents", porque cubre el término 2025 y la parte de agentes que el libro (de principios de 2025) no tiene. Fijarse en: la secuencia término, embedding, híbrido, reranking como escalera de costo; la cifra de Contextual Retrieval como orden de magnitud, no como garantía; y el criterio "tamaño de la base vs ventana".

### Huecos

- El texto del cap. 6 del libro no se leyó (solo índice y resumen del repo). Páginas de "Retrieval Optimization" (pp. 268-273, chunking, reranking, query rewriting) sin verificar en el original.
- Sin fuente primaria sobre embeddings multilingües/castellano para chunking ni sobre evaluación de recuperación (precision/recall@k): eso cruza con la nota de evaluación.
- Sin fuente de "agentic RAG" que no sea un survey de arXiv.

## 2. router-y-gateway-de-modelos

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Huyen, post de plataforma (2024-07-25), sección Router and Gateway | https://huyenchip.com/2024/07/25/genai-platform.html | prim | 3 | 2 | 1 | 3 | [L] |
| Ong et al., "RouteLLM" (arXiv 2406.18665, 2024-06-26, v4 2025-02-23, sin revisión por pares en la página) | https://arxiv.org/abs/2406.18665 | prim (preprint) | 2 | 2 | 2 | 3 | [M] |
| LiteLLM, docs del AI Gateway (MIT) | https://docs.litellm.ai/docs/simple_proxy | prim (producto) | 2 | 2 | 2 | 1 | [L] |
| Cloudflare AI Gateway, docs | https://developers.cloudflare.com/ai-gateway/ | prim (producto) | 2 | 1 | 1 | 1 | [L] |
| OpenRouter, docs de model routing | https://openrouter.ai/docs/features/model-routing | prim (producto) | 2 | 2 | 1 | 1 | [L] |

### Afirmaciones

- Router: usa un clasificador de intención; "Instead of routing all queries to an expensive model, you can route simpler queries to cheaper models." Gateway: "A model gateway is access control and cost management", con "fallback policies to overcome rate limits or API failures". https://huyenchip.com/2024/07/25/genai-platform.html
- RouteLLM reporta que sus routers bajan el costo "more than 2x in some cases" sin comprometer la calidad, entrenando con datos de preferencia. https://arxiv.org/abs/2406.18665 (afirmación de los autores; preprint).
- LiteLLM: un endpoint compatible con OpenAI para "100+ LLM providers", claves virtuales por usuario/equipo/proyecto con presupuestos y límites, seguimiento de gasto, fallbacks y reintentos, logs a Langfuse/Datadog/OpenTelemetry, guardrails (filtros y PII). https://docs.litellm.ai/docs/simple_proxy
- Cloudflare AI Gateway: caché, límites de tasa, reintentos y fallback con alias de modelo, rutas dinámicas, analítica y logs. https://developers.cloudflare.com/ai-gateway/
- OpenRouter: `openrouter/auto` elige modelo y esfuerzo de razonamiento por pedido, con `cost_tier` (low/medium/high), sin cargo extra; mantiene sesiones estables para no rehacer el prompt cache. https://openrouter.ai/docs/features/model-routing
- Debate sobre routers (discrepancia). Latent Space (2026-03-04) recoge a Noam Brown (OpenAI): los scaffolds "will also just be replaced by the reasoning models" y los routers de modelos deberían desaparecer. https://www.latent.space/p/ainews-is-harness-engineering-real [L]. Contra: OpenRouter y LiteLLM los ofrecen como producto. No hay un estudio que arbitre; se presenta como tensión abierta.

### Recurso canónico

Huyen, post de plataforma, sección "Router and gateway" (cap. 10 pp. 456-460). Fijarse en que separa dos funciones: router (decide qué modelo) y gateway (acceso, claves, costo, fallback). Para el mecanismo concreto, la doc de LiteLLM como ejemplo auditable.

### Huecos

- No hay fuente primaria sobre cuánto ahorra un router en producción más allá del paper de RouteLLM. Sin datos de la comunidad que no sean de vendors.
- Las páginas de OpenRouter y Cloudflare son de producto (autoridad sobre su propio producto, interés comercial).

## 3. cache-de-modelos

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Recencia | Marca |
|---|---|---|---|---|---|---|---|---|
| Anthropic, docs de prompt caching | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | prim | 3 | 3 | 3 | 3 | leída 2026-11-27 | [L] (primeros 100.000 de ~155.000 caracteres) |
| OpenAI, guía de prompt caching | https://developers.openai.com/api/docs/guides/prompt-caching | prim | 3 | 2 | 2 | 2 | leída 2026-11-27 | [L] |
| Google, docs de context caching (redirige a aistudio.google.com/docs/caching) | https://aistudio.google.com/docs/caching | prim | 3 | 1 | 1 | 2 | leída 2026-11-27 | [L] |
| Huyen, post de plataforma, sección Cache | https://huyenchip.com/2024/07/25/genai-platform.html | prim | 3 | 2 | 1 | 3 | 2024 | [L] |
| vCache (arXiv 2502.03771, sin revisión por pares) | https://arxiv.org/abs/2502.03771 | prim (preprint) | 1 | 2 | 2 | 3 | v5 | [S] |
| InfoQ, caso de falsos positivos en un FAQ bancario | https://www.infoq.com/articles/reducing-false-positives-retrieval-augmented-generation | sec | 1 | 2 | 2 | 2 | s/f | [S] |
| DZone, "LLM semantic caching" | https://dzone.com/articles/llm-semantic-caching | sec | 1 | 1 | 2 | 1 | s/f | [S] |

### Afirmaciones

- Prompt cache de Anthropic: marca `cache_control: {"type":"ephemeral"}`; hasta 4 puntos de corte; TTL por defecto 5 minutos, 1 hora con `"ttl":"1h"`; orden del prefijo `tools`, `system`, `messages`; los hits exigen prefijo 100% idéntico. Escritura 5 min = 1,25x del precio de entrada; escritura 1 h = 2x; lectura = 0,1x (0,05x en Opus 5.5 y Sonnet 5.5; 0,025x en Fable/Mythos 5.1 y 5.2). Mínimo cacheable entre 512 y 4.096 tokens según modelo. Cambiar definiciones de herramientas invalida todo; cambiar `tool_choice` invalida system y tools. Aislado por organización o workspace. https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Prompt cache de OpenAI: activado por defecto; guarda el estado KV, no el texto; mínimo 1.024 tokens (GPT-5.6 y posteriores); lectura 0,1x (0,05x en algunos modelos); escritura 1,25x con vida de 30 min por defecto o 2,5x con 12 h; modelos anteriores: sin cargo de escritura y retención `in_memory` (unos 5-10 minutos, hasta 1 h) o `24h`. Consejo: contenido estático primero, dinámico al final. https://developers.openai.com/api/docs/guides/prompt-caching
- Google: caché implícito activado por defecto desde Gemini 2.5; explícito con objetos de caché manuales; mínimos de 2.048 a 4.096 tokens según modelo. La página no da TTL, descuento ni costo de almacenamiento. https://aistudio.google.com/docs/caching
- Diferencia de diseño entre proveedores (dato, no discrepancia): Anthropic cobra escritura y lectura con multiplicadores y exige marcar; OpenAI en modelos nuevos también cobra escritura; Google ofrece implícito sin marca. Los números cambian por modelo y por mes: no ponerlos en la nota estable.
- Huyen distingue tres cachés. Prompt cache: reutiliza segmentos compartidos; "Like KV cache, prompt cache size can be quite large and require significant engineering effort". Exact cache: mismas entradas, mismo resultado; "Having an eviction policy is crucial"; malo para consultas específicas de usuario o sensibles al tiempo. Semantic cache: reutiliza para consultas parecidas; "If the system mistakes the incoming query as being similar to another query" la respuesta cacheada es errónea; depende de "high-quality embeddings, functional vector search, and a trustworthy similarity metric". https://huyenchip.com/2024/07/25/genai-platform.html
- Riesgo del semantic cache, evidencia: vCache dice que los hits correctos e incorrectos tienen puntajes de similitud muy superpuestos, así que un umbral global no separa bien; propone un umbral por entrada aprendido online. https://arxiv.org/abs/2502.03771 [S]. Un caso de FAQ bancario (un solo caso, estilo vendor) reporta respuestas seguras pero erróneas, con falsos positivos de hasta 99% en algunos modelos a umbral 0,7. https://www.infoq.com/articles/reducing-false-positives-retrieval-augmented-generation [S]. Mitigaciones sugeridas: umbral más estricto, embedding del dominio, verificación posterior, claves mixtas exacta+semántica, y que la distancia vectorial no decae con el tiempo (entradas viejas). https://dzone.com/articles/llm-semantic-caching [S]
- Anthropic recomienda diseñar el harness para aciertos de caché: contenido estable primero y no cambiar de modelo a mitad de sesión. https://claude.com/resources/articles/harnessing-claudes-intelligence [L]

### Recurso canónico

Para el mecanismo: la doc de prompt caching del proveedor que use el lector (Anthropic es la más completa de las tres: orden del prefijo, qué invalida, campos de uso `cache_read_input_tokens` y `cache_creation_input_tokens`). Para el marco conceptual (tres cachés y sus riesgos): Huyen, post de plataforma, sección Cache (libro cap. 10 pp. 460-463). Fijarse en: el prompt cache es del proveedor y casi no tiene riesgo de corrección; el semantic cache es el que puede devolver una respuesta equivocada.

### Huecos

- Sin fuente primaria rigurosa sobre semantic cache en producción: solo un preprint y blogs. Hueco declarado.
- Google: TTL y descuento no figuran en lo extraído; verificar en la página viva.
- Sin sección propia en el libro del exact cache más allá de lo que dice el post.

## 4. agente

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Recencia | Marca |
|---|---|---|---|---|---|---|---|---|
| Huyen, "Agents" (2025-01-07) | https://huyenchip.com/2025/01/07/agents.html | prim | 3 | 3 | 2 | 3 | 2025-01 | [L] |
| Anthropic, "Building effective agents" (2024-12-19) | https://www.anthropic.com/engineering/building-effective-agents | prim (lab) | 3 | 2 | 2 | 3 | 2024-12 | [L] |
| Yao et al., ReAct (arXiv 2210.03629, 2022-10-06; ICLR 2023 camera-ready) | https://arxiv.org/abs/2210.03629 | prim (paper) | 3 | 3 | 2 | 3 | 2022 | [M] |
| Anthropic, anuncio de MCP (2024-11-25) | https://www.anthropic.com/news/model-context-protocol | prim | 3 | 1 | 1 | 3 | 2024-11 | [L] |
| Especificación MCP (versión 2026-07-28) | https://modelcontextprotocol.io/specification/latest | prim | 3 | 3 | 1 | 3 | 2026-07 | [L] |
| Anthropic, "Effective harnesses for long-running agents" (2025-11-26, Justin Young) | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | prim (lab) | 3 | 2 | 3 | 2 | 2025-11 | [L] |
| Anthropic, "Harness design for long-running application development" (2026-03-24, Prithvi Rajasekaran) | https://www.anthropic.com/engineering/harness-design-long-running-apps | prim (lab) | 3 | 2 | 3 | 2 | 2026-03 | [L] |
| Anthropic/Claude, "Agent Harness Design: 3 Patterns..." (2026-04-02, Lance Martin) | https://claude.com/resources/articles/harnessing-claudes-intelligence | prim (lab) | 3 | 2 | 2 | 2 | 2026-04 | [L] |
| OpenAI, "Harness engineering: leveraging Codex in an agent-first world" (2026-02-11, Ryan Lopopolo) | https://openai.com/index/harness-engineering/ | prim (lab) | 3 | 3 | 3 | 3 | 2026-02 | [L] |
| Weng, "Harness Engineering for Self-Improvement" (2026-07-04) | https://lilianweng.github.io/posts/2026-07-04-harness/ | prim (survey de investigadora, ex OpenAI) | 3 | 3 | 2 | 3 | 2026-07 | [L] |
| Latent Space, "Is Harness Engineering real?" (AINews, 2026-03-04) | https://www.latent.space/p/ainews-is-harness-engineering-real | sec (curaduría) | 2 | 2 | 2 | 2 | 2026-03 | [L] |
| Osmani, "Agent harness engineering" (2026-05-15, republicado en O'Reilly Radar) | https://www.oreilly.com/radar/agent-harness-engineering/ | sec (síntesis) | 2 | 2 | 2 | 1 | 2026-05 | [L] |
| Huyen, AI Engineering cap. 6, "Agents" (pp. 275-305) | libro (ToC: https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md) | prim | 3 | 3 | 2 | 3 | 2025 | [M] (solo índice) |

### Afirmaciones: definición y planificación

- Huyen define agente como "anything that can perceive its environment and act upon that environment". Herramientas en tres tipos: aumento de conocimiento (retrievers, SQL, web), extensión de capacidad (calculadora, intérprete de código) y acciones de escritura (enviar emails, transferir). "Planning, at its core, is a search problem." Recomienda separar planificación de ejecución y validar el plan antes de correrlo. Reflexión y corrección de errores son "two different mechanisms that go hand in hand". https://huyenchip.com/2025/01/07/agents.html
- Tres tipos de falla (Huyen): de planificación (herramienta inválida, parámetros erróneos, no llegar al objetivo, creer que terminó), de herramienta (salida errónea, error al traducir el plan a comandos) y de eficiencia (pasos de más, costo, tiempo frente a una línea base). Mismo URL.
- Anthropic: workflow = "systems where LLMs and tools are orchestrated through predefined code paths"; agent = "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks". Cinco patrones: prompt chaining, routing, parallelization (sectioning y voting), orchestrator-workers, evaluator-optimizer. Consejo: "the simplest solution possible, and only increasing complexity when needed"; los frameworks pueden "create extra layers of abstraction that can obscure the underlying prompts". https://www.anthropic.com/engineering/building-effective-agents
- Huyen y Anthropic coinciden en que RAG es un caso del patrón agente con retriever como herramienta (ver sección 1) y en la sobriedad ante la autonomía. Diferencia de énfasis, no discrepancia: Huyen pone el foco en planificación y fallas; Anthropic en el espectro workflow a agente.
- ReAct intercala trazas de razonamiento con acciones; en HotpotQA y FEVER reduce alucinación frente a chain-of-thought; en ALFWorld y WebShop supera a imitación y RL por 34% y 10% de éxito absoluto con uno o dos ejemplos. https://arxiv.org/abs/2210.03629

### Afirmaciones: MCP

- MCP, anunciado el 2024-11-25 como estándar abierto para conectar asistentes con sistemas donde viven los datos; la motivación: "Every new data source requires its own custom implementation". https://www.anthropic.com/news/model-context-protocol
- Especificación (versión 2026-07-28): JSON-RPC 2.0; hosts, clientes y servidores; el servidor ofrece resources, prompts y tools; el cliente puede ofrecer elicitation; peticiones sin estado y con negociación de capacidades por petición; extensiones opcionales (Tasks, Skills over MCP, MCP Apps). Seguridad: las herramientas "represent arbitrary code execution", las descripciones de herramientas son no confiables salvo servidor de confianza. https://modelcontextprotocol.io/specification/latest
- Inspiración declarada: Language Server Protocol. Mismo URL.

### Afirmaciones: harness engineering (qué cambia)

- Autoría: Weng, no Huyen (sección 0). Definición de Weng: el harness es "the system surrounding a base model that orchestrates execution": cómo planifica, llama herramientas, administra contexto, guarda artefactos y evalúa resultados. Tesis: el camino cercano a la automejora recursiva "is unlikely to start as a model directly rewriting its weights", sino con el harness como objetivo de optimización; requiere un modelo base "capable enough". Retos: evaluadores débiles ("Current self-improvement loops work best for tasks when evaluation metrics are measurable and objective"), ciclo de vida de la memoria, resultados negativos, colapso de diversidad, reward hacking, éxito de largo plazo (mantenibilidad), rol humano. https://lilianweng.github.io/posts/2026-07-04-harness/
- OpenAI (Lopopolo, 2026-02-11): equipo construyó una beta interna de aproximadamente un millón de líneas en cinco meses sin escribir código a mano, unos 1.500 PR fusionados, de 3 a 7 ingenieros; estimación de un décimo del tiempo. El trabajo pasa de escribir código a "designing environments, specifying intent, and building feedback loops". Cuando el agente falla, se agrega la herramienta, la guarda o la documentación faltante, no se reintenta el prompt. AGENTS.md de unas 100 líneas como mapa y un directorio `docs/` como sistema de registro: "give Codex a map, not a 1,000-page instruction manual". Restricciones de arquitectura impuestas por linters y tests estructurales, con mensajes de error que incluyen la remediación. El cuerpo del artículo no define "harness"; el término está solo en el título. Cifras autodeclaradas por el equipo. https://openai.com/index/harness-engineering/
- Anthropic, tareas largas (Young, 2025-11-26): los agentes trabajan en sesiones sin memoria de las anteriores; solución en dos partes: un agente inicializador (script `init.sh`, `claude-progress.txt`, commit inicial, lista de features en JSON todas marcadas como fallando) y un agente de código que trabaja una feature por sesión, la prueba de punta a punta y deja el repo limpio. Fallas y arreglos: declarar el proyecto terminado antes de tiempo (lista de features), marcar features hechas sin probar (pruebas con automatización de navegador). https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic (Rajasekaran, 2026-03-24): triple planner, generator, evaluator (con Playwright y umbrales duros); "context anxiety" en Sonnet 4.5 (cerrar el trabajo antes por creer que se acaba el contexto); reset vs compaction ("While compaction preserves continuity, it doesn't give the agent a clean slate"); con Opus 4.5 el reset sobraba. Principio: "every component in a harness encodes an assumption about what the model can't do on its own" y esas asunciones envejecen. https://www.anthropic.com/engineering/harness-design-long-running-apps
- Anthropic (Martin, 2026-04-02): harness = "the software scaffolding around a model" (bucle, herramientas, contexto, guardas). Tres patrones: apoyarse en el modelo y no en el harness, preguntar qué se puede dejar de hacer, y fijar bien los límites (diseñar para aciertos de caché; herramientas dedicadas para acciones que requieren control de seguridad, UX u observabilidad). Los resets de contexto pasaron a "dead weight" con Opus 4.5. https://claude.com/resources/articles/harnessing-claudes-intelligence
- Osmani (2026-05-15), síntesis: "Agent = Model + Harness" (fórmula atribuida a Viv Trivedy); componentes: prompts e instrucciones (AGENTS.md, CLAUDE.md, skills), herramientas y servidores MCP, infraestructura (filesystem, sandbox, navegador), orquestación (subagentes, handoffs, routing), hooks y middleware, observabilidad. Cada error del agente debería volverse una restricción durable; "Success is silent; failures are verbose." Afirma que un modelo decente con buen harness puede superar a uno fuerte con harness débil (dato citado de segunda mano: un agente de código pasó del Top 30 al Top 5 en Terminal Bench 2.0 cambiando solo el harness). https://www.oreilly.com/radar/agent-harness-engineering/ . Esta nota es síntesis de las anteriores, cuenta como casi la misma fuente que OpenAI y Anthropic.
- Discrepancia viva: ¿harness grande o modelo grande? Latent Space (2026-03-04) ordena el debate. Modelo grande: Boris Cherny (Claude Code es "the thinnest possible wrapper over the model"), Noam Brown (los scaffolds serán reemplazados por modelos de razonamiento), METR (Claude Code y Codex no superan a un scaffold básico), y Scale AI SWE-Atlas (Opus 4.6 apenas +2,5 puntos en Claude Code frente a SWE-Agent, y GPT-5.2 al revés). Harness grande: Jerry Liu (LlamaIndex, "The Model Harness is Everything"), y una prueba de que cambiando solo el harness (Pi) mejoraron 15 LLM en código. Conclusión de Latent Space: "real value" en harness engineering, con la advertencia de que cada bando tiene interés comercial. https://www.latent.space/p/ainews-is-harness-engineering-real . Además un guest post (Dan McAteer, vía buscador [S]) cita Harness-Bench: un mismo modelo en 106 tareas con distintos harness rindió entre 52,4 y 76,2 (https://daily.dev/posts/the-evolution-of-the-agent-harness-1z25xrcos, sin leer). Las dos posturas conviven en Anthropic: su propia guía dice "quitá lo que el modelo ya hace solo".
- Qué cambia en resumen, tomando lo leído: (a) el foco pasa de "el prompt" a "el entorno" (documentación en el repo, linters, pruebas, herramientas); (b) el harness es perecedero: cada pieza codifica una limitación del modelo y hay que podarlas; (c) el harness es lo que hace posible la tarea larga (memoria en archivos, feature list, evaluador separado); (d) empieza a ser objeto de optimización automática (Weng). El término es de 2026 y su definición no está fijada: OpenAI no lo define, Anthropic y Weng sí, con matices.

### Recurso canónico

Para la definición y fallas: Huyen, "Agents" (post 2025-01-07) y cap. 6 pp. 275-305, en especial "Planning" y "Agent Failure Modes and Evaluation" (pp. 281-300). Para el criterio de diseño: Anthropic, "Building effective agents" (workflow vs agent, simplicidad). Para harness engineering: OpenAI, "Harness engineering" (el caso más concreto y con cifras) más Anthropic, "Harness design for long-running application development" (el principio de que las asunciones envejecen). Weng como mapa de la investigación y para el límite (evaluadores débiles). Fijarse en: dónde viven el conocimiento y las restricciones (en el repo, no en el chat), y qué piezas del harness se pueden quitar.

### Huecos

- No existe ensayo de Huyen sobre harness (sección 0).
- El texto del cap. 6 "Agents" no se leyó.
- Sin fuente independiente (no de un laboratorio con producto) que mida el efecto del harness con método reproducible: Harness-Bench y Terminal Bench llegan de segunda mano.
- El artículo de OpenAI no define "harness"; la definición estable sigue en discusión.
- Latent Space: el post completo está parcialmente tras paywall, se leyó lo que mostró el extractor.

## 5. prompt-rag-o-finetuning

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Recencia | Marca |
|---|---|---|---|---|---|---|---|---|
| Huyen, AI Engineering cap. 7 "Finetuning", "When to Finetune" (pp. 311-319) y cap. 8 "Model Distillation" (p. 395) | ToC: https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md ; resumen: https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md | prim | 3 | 3 | 2 | 3 | 2025 | [M] (índice) y [L] (resumen de capítulo) |
| OpenAI, "Optimizing LLM accuracy" | https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy | prim | 3 | 3 | 3 | 3 | leída 2026-11-27 | [L] |
| OpenAI, "Model optimization" | https://developers.openai.com/api/docs/guides/model-optimization | prim | 3 | 2 | 2 | 2 | leída 2026-11-27 | [L] |
| OpenAI, "Distillation" | https://developers.openai.com/api/docs/guides/distillation | prim | 3 | 2 | 2 | 2 | leída 2026-11-27 | [L] |
| Anthropic, "intro to prompting" (docs) | https://docs.claude.com/en/docs/intro-to-prompting | prim | 3 | 1 | 1 | 2 | s/f | [S] (solo lo citó el buscador) |
| Anthropic y AWS, fine-tuning de Claude 3 Haiku en Bedrock (GA 2024-11-01) | https://www.anthropic.com/news/fine-tune-claude-3-haiku-ga | prim | 3 | 1 | 1 | 2 | 2024-11 | [S] |

### Afirmaciones

- Resumen oficial del repo del libro, cap. 7: lo difícil de fine-tunear no es la mecánica sino saber si hacerlo y cuándo usar RAG; el fine-tuning completo no escala; PEFT y LoRA bajan el costo; "A comment I often hear from practitioners is that finetuning is easy, but getting data for finetuning is hard". Cap. 6: tanto RAG como agentes "are prompt-based", no cambian el modelo. https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
- Estructura del cap. 7: "Reasons to Finetune" (p. 311), "Reasons Not to Finetune" (p. 312), "Finetuning and RAG" (p. 316); cap. 8: "Model Distillation" (p. 395). https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md . El contenido de esas secciones no se leyó. Nota: el resumen del repo no menciona distilación en el cap. 8 (el extractor la ubicó en el cap. 9); el índice la pone en el cap. 8 p. 395. Discrepancia entre el resumen y el índice: manda el índice.
- Escalera de OpenAI: "Prompt engineering is typically the best place to start"; diagnosticar la falla: falta de conocimiento (problema de contexto, se resuelve con RAG) vs comportamiento inconsistente (problema de aprendizaje, se resuelve con fine-tuning); se combinan si hay ambos; empezar con 50+ ejemplos de calidad; "Quality of training data is more important than quantity". Caso de advertencia: en una corrección de islandés, agregar RAG a un GPT-4 afinado bajó el BLEU de 87 a 83. https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy
- Cuándo ayuda el fine-tuning según OpenAI: más ejemplos de los que caben en una ventana, prompts más cortos (menos tokens y latencia), y "train a smaller, cheaper, faster model to excel at a particular task". Métodos: SFT, DPO (con par respuesta correcta/incorrecta), fine-tuning de visión. https://developers.openai.com/api/docs/guides/model-optimization
- Destilación (OpenAI): afinar un prompt en un modelo grande hasta cumplir los evals, guardar las salidas (el Responses API las guarda 30 días por defecto), armar el dataset y afinar uno chico. https://developers.openai.com/api/docs/guides/distillation
- Estado de la plataforma: "OpenAI is winding down the fine-tuning platform"; cerrada a nuevos usuarios; jobs hasta 2026-12-15 para clientes elegibles; `gpt-4.1-nano-2025-04-14` se apaga el 2026-10-23, y `gpt-4.1` y `gpt-4.1-mini` el 2027-01-14. Mismo URL de destilación. Es lo más volátil de esta sección.
- Anthropic: la guía de prompting dice que la ingeniería de prompts es mucho más rápida que el fine-tuning, que este exige muchos datos etiquetados y arriesga olvido catastrófico (citado por el buscador, sin abrir la página) [S]. Fine-tuning de Claude 3 Haiku en Bedrock fue GA el 2024-11-01 en us-west-2; el buscador indicó que Claude 3 Haiku llega a fin de vida el 2026-09-10 [S]. Hueco: no se encontró una página oficial vigente de Anthropic sobre cuándo fine-tunear; hay blogs de terceros que se contradicen (uno dice que Anthropic no ofrece fine-tuning público a abril 2026), sin verificar.

### Recurso canónico

Huyen, cap. 7, sección "When to Finetune" (pp. 311-319), con "Finetuning and RAG" (p. 316) para la decisión; el cap. 8 sobre distilación (p. 395). Como complemento con criterio operativo, la guía de OpenAI "Optimizing LLM accuracy" (el diagnóstico conocimiento vs comportamiento es lo más útil para un ingeniero). Fijarse en: separar falta de conocimiento (contexto) de falta de consistencia (comportamiento), la regla de empezar por prompt y evals, y que el fine-tuning mueve el problema al dato.

### Huecos

- El texto de "When to Finetune" del libro no se leyó (solo índice y resumen general).
- Sin doc oficial vigente de Anthropic; sin doc oficial de Google sobre fine-tuning.
- Con la plataforma de OpenAI en retirada, falta fuente sobre la alternativa actual (pesos abiertos con LoRA, otros proveedores): no se investigó (fuera de las tres rondas por componente).

## 6. plataformas-de-ia (ficha volátil, fechada 2026-11-27)

Recomendación: ficha corta, con la categoría estable y los productos como ejemplos con fecha de consulta. La fuente viva de cada categoría es la documentación del producto, no los rankings. La mayoría de los rankings hallados son blogs de vendors o de DEV Community (autoridad 1).

| Categoría | Ejemplos (no exhaustivo) | Fuente viva leída | Marca | Nota de recencia |
|---|---|---|---|---|
| Gateways de modelos | LiteLLM (MIT), Cloudflare AI Gateway, OpenRouter; también aparecen Portkey, Kong AI Gateway, Bifrost, Envoy AI Gateway | https://docs.litellm.ai/docs/simple_proxy ; https://developers.cloudflare.com/ai-gateway/ ; https://openrouter.ai/docs/features/model-routing | [L] | consultadas 2026-11-27. Un listado afirma que Portkey fue adquirida (2026-05-29) y otro que Helicone tuvo una adquisición; ambos [S] de un solo origen, no usar sin verificar: https://geekflare.com/open-source/llm-gateway/ |
| Vector stores | pgvector, Qdrant, Weaviate, Pinecone, Milvus | ninguna leída en el sitio del producto | [S] | Los blogs de 2026 discrepan en hybrid search de Pinecone (uno lo lista solo denso, otro con vectores sparse). Coinciden en que pgvector alcanza para muchos casos de RAG y Milvus para escala muy grande. https://dev.to/_6638a39c349d7e9c85ee20/vector-database-comparison-2026-pinecone-vs-weaviate-vs-qdrant-vs-milvus-vs-pgvector-2b0o . Hueco: ver docs oficiales. |
| Frameworks de orquestación y SDK de agentes | LangGraph, OpenAI Agents SDK, Claude Agent SDK, Google ADK, Pydantic AI, Microsoft Agent Framework, CrewAI | ninguna leída en el sitio del producto | [S] | Clasificación común: SDK de proveedor, frameworks agnósticos, herramientas especializadas. MCP ya viene soportado en varios (un solo origen). Versiones citadas por un roundup del 2026-10-12 no sirven para fijar: https://www.morphllm.com/ai-agent-framework |
| Evals y observabilidad | Langfuse, LangSmith, Braintrust, Arize Phoenix (ELv2) | ninguna leída en el sitio del producto | [S] | Coinciden en: Langfuse y Phoenix autoalojables, LangSmith para el ecosistema LangChain, Braintrust fuerte en evals. Un comparativo es de Arize, parte interesada. https://dev.to/gabrielanhaia/langfuse-vs-langsmith-vs-phoenix-vs-braintrust-the-honest-2026-comparison-253p |

Fuente viva sugerida por categoría: las docs de cada producto y los registros de paquetes (versiones). Para gateways y observabilidad, que los proyectos nombren compatibilidad con OpenTelemetry es un criterio verificable (LiteLLM la nombra; Phoenix se describe OpenTelemetry-native según blogs [S]).

Huecos: no se leyeron las páginas oficiales de vector stores, frameworks y herramientas de evals/observabilidad; solo resúmenes del buscador. Para la ficha hay que abrir esas páginas antes de escribir. La nota de evaluación y observabilidad ya tiene su propia investigación en la misma carpeta (`evaluacion-y-observabilidad.md`), no solapar.

## 7. Capítulos de AI Engineering por componente

Índice leído en https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md [L]. Resúmenes de capítulo en https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md [L].

| Componente del árbol | Capítulo y secciones (páginas del libro) |
|---|---|
| contexto-y-rag | Cap. 6 "RAG" pp. 253-275 (RAG Architecture 256, Retrieval Algorithms 257, Retrieval Optimization 268, RAG Beyond Texts 273); cap. 5 "Context Length and Context Efficiency" p. 218 y "Provide Sufficient Context" p. 223; cap. 10 "Step 1. Enhance Context" p. 450; memoria cap. 6 p. 300 |
| router-y-gateway | Cap. 10 "Step 3. Add Model Router and Gateway" p. 456; cap. 4 "Model Selection" p. 179 (build vs buy p. 181) |
| cache | Cap. 10 "Step 4. Reduce Latency with Caches" p. 460; cap. 9 "Inference Service Optimization" p. 440 (aquí vive el KV cache y el prompt caching del lado servidor) |
| agente | Cap. 6 "Agents" pp. 275-305 (Tools 278, Planning 281, Failure Modes and Evaluation 298, Memory 300); cap. 10 "Step 5. Add Agent Patterns" p. 463 |
| prompt-rag-o-finetuning | Cap. 5 (prompt) pp. 211-251; cap. 6 (RAG); cap. 7 "When to Finetune" pp. 311-319; cap. 8 "Model Distillation" p. 395 |
| (no previsto en el árbol) observabilidad y orquestación | Cap. 10 "Monitoring and Observability" p. 465 y "AI Pipeline Orchestration" p. 472; evaluación cap. 3-4; feedback p. 474 |

Otras piezas del repo: `case-studies.md`, `resources.md`, `study-notes.md` (solo enlaces a notas de terceros, p. ej. notas por capítulo de Alex Strick van Linschoten; no un resumen propio de Huyen), `prompt-examples.md`, `misalignment.md`. https://github.com/chiphuyen/aie-book [L]

## 8. ¿Coincide el árbol propuesto con cómo el campo divide esta vertical?

Coincide en lo central, con cuatro diferencias que conviene decidir:

1. **El árbol mezcla dos ejes.** Huyen ordena la arquitectura de referencia (cap. 10 y su post) como capas de runtime: contexto, guardrails, router y gateway, caché, lógica compleja y acciones de escritura, observabilidad, orquestación. `prompt-rag-o-finetuning` no es una capa de runtime: es una decisión de desarrollo (la escalera de adaptación, cap. 5-8) y comparte RAG con `contexto-y-rag`. Dos notas distintas que hablan de RAG hay que enlazarlas, no duplicarlas: `contexto-y-rag` explica el mecanismo; `prompt-rag-o-finetuning` decide cuándo subir de escalón.
2. **Router y gateway van juntos en Huyen** (un solo paso 3), pero hacen cosas distintas (decidir modelo vs controlar acceso y costo). El árbol los junta en un componente: es consistente con Huyen y razonable.
3. **Faltan observabilidad y orquestación** como componentes de la vertical, aunque Huyen los incluye (pasos 6 y 7). Hay una investigación de evaluación y observabilidad en la misma carpeta, así que alcanza con enlazar. Orquestación (frameworks) cae en `plataformas-de-ia` y en el post de Huyen, que recomienda empezar sin orquestador ("Any external tool brings added complexity"). Decidir si `agente` absorbe "Complex Logic and Write Actions" (Huyen lo trata como paso aparte; el libro lo llama "Add Agent Patterns").
4. **Harness engineering desborda a `agente`.** Según Osmani, el harness incluye prompts, herramientas, infraestructura, orquestación, hooks y observabilidad; es decir, cruza varios componentes. Dos opciones: una sección de `agente` o una nota propia sobre harness, con enlaces a contexto, observabilidad y guardrails. Dado que el término es de 2026 y su definición no está fijada, lo prudente es sección dentro de `agente`, fechada, con la discrepancia modelo grande vs harness grande.

Memoria (cap. 6 p. 300) y feedback del usuario (cap. 10 p. 474) tampoco tienen casa en el árbol; son candidatos a ampliación.

## 9. Resumen de huecos

- Sin ensayo de Huyen sobre harness (el ensayo es de Weng).
- El libro (texto) no se leyó: solo índice, resúmenes del repo y los posts de Huyen.
- Sin doc oficial vigente de Anthropic ni de Google sobre cuándo fine-tunear; OpenAI está retirando su plataforma de fine-tuning (jobs hasta 2026-12-15).
- Plataformas: vector stores, frameworks y observabilidad solo por resúmenes del buscador y blogs; gateways leídos en sitio oficial.
- Semantic cache: evidencia de preprint y blogs; ningún estudio primario revisado por pares.
- Long context vs RAG: dos preprints/papers que discrepan; la cifra de 200.000 tokens de Anthropic es de 2024.
- Evidencia independiente del impacto del harness: solo de segunda mano (Terminal Bench, Harness-Bench, SWE-Atlas).
- Google context caching: TTL y descuento no figuran en lo extraído.
- Límites de método: citas literales vía extractor; la doc de prompt caching de Anthropic se leyó hasta el caracter 100.000 de 155.417.
