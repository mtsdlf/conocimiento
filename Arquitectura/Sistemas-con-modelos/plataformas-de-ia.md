---
resumen: >-
  Ejemplos de productos por categoría para armar un sistema con modelos (gateways, vector stores,
  orquestación, evals y observabilidad), los valores del prompt cache por proveedor y el estado del
  fine-tuning por proveedor, copiados el 2026-11-27.
estado: borrador
estabilidad: volatil
fuentes:
  - https://docs.litellm.ai/docs/simple_proxy
  - https://developers.cloudflare.com/ai-gateway/
  - https://openrouter.ai/docs/features/model-routing
  - https://dev.to/_6638a39c349d7e9c85ee20/vector-database-comparison-2026-pinecone-vs-weaviate-vs-qdrant-vs-milvus-vs-pgvector-2b0o
  - https://www.morphllm.com/ai-agent-framework
  - https://dev.to/gabrielanhaia/langfuse-vs-langsmith-vs-phoenix-vs-braintrust-the-honest-2026-comparison-253p
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://developers.openai.com/api/docs/guides/prompt-caching
  - https://aistudio.google.com/docs/caching
  - https://developers.openai.com/api/docs/guides/distillation
  - https://developers.openai.com/api/docs/guides/model-optimization
  - https://www.anthropic.com/news/fine-tune-claude-3-haiku-ga
creado: 2026-11-27
revisado:
---

# Plataformas de IA

Ejemplos de productos por categoría para armar un sistema con modelos (gateways, vector stores,
orquestación, evals y observabilidad), los valores del prompt cache por proveedor y el estado del
fine-tuning por proveedor, copiados el 2026-11-27.

Implementa las capas de [Sistemas con modelos](sistemas-con-modelos.md). Los productos son
ejemplos, no un ranking: la fuente viva de cada uno es su documentación y su registro de paquetes.
Las filas marcadas **[buscador]** salen de resúmenes de buscador o de blogs comparativos, sin abrir
la documentación del producto: hay que verificarlas antes de decidir.

## Productos por categoría

| Categoría | Implementa | Ejemplos | Fuente viva | Cómo se obtuvo |
|---|---|---|---|---|
| Gateways de modelos | [Router y gateway](router-y-gateway-de-modelos.md) | LiteLLM (MIT, autoalojable), Cloudflare AI Gateway, OpenRouter | [LiteLLM](https://docs.litellm.ai/docs/simple_proxy), [Cloudflare](https://developers.cloudflare.com/ai-gateway/), [OpenRouter](https://openrouter.ai/docs/features/model-routing) | documentación oficial leída |
| Vector stores | [Contexto y RAG](contexto-y-rag.md) | pgvector, Qdrant, Pinecone | docs de cada producto | **[buscador]** |
| Orquestación y SDK de agentes | [Agente](agente.md) | LangGraph, OpenAI Agents SDK, Claude Agent SDK | docs de cada producto | **[buscador]** |
| Evals y observabilidad | [Observabilidad](../Evaluacion-y-observabilidad/observabilidad-de-modelos.md) | Langfuse, LangSmith, Arize Phoenix | docs de cada producto | **[buscador]** |

Lo que dicen las fuentes de cada fila:

- **Gateways.** LiteLLM ofrece un endpoint compatible con la API de OpenAI para "100+ LLM
  providers", claves virtuales con presupuesto por usuario, equipo o proyecto, fallbacks y
  reintentos, y envío de logs a herramientas de observabilidad y a OpenTelemetry. Cloudflare AI
  Gateway suma cache, límites de tasa, fallback y analítica. OpenRouter tiene un modelo `auto` que
  elige modelo y esfuerzo de razonamiento por pedido, sin cargo extra, y mantiene la sesión estable
  para no perder el prompt cache. Otros nombres que aparecen en listados **[buscador]**: Portkey,
  Kong AI Gateway, Bifrost, Envoy AI Gateway; hay noticias de adquisiciones en el rubro que vienen de
  un solo listado y no se verificaron.
- **Vector stores [buscador].** Los blogs de 2026 coinciden en que pgvector alcanza para muchos
  casos de RAG y Milvus (otro de los que comparan) apunta a escala muy grande; discrepan sobre si Pinecone hace búsqueda
  híbrida.
- **Orquestación [buscador].** La clasificación común es SDK de un proveedor de modelos, framework
  agnóstico o herramienta especializada; varios soportan MCP. Las versiones que citan los roundups
  no sirven para fijar.
- **Evals y observabilidad [buscador].** Coinciden en que Langfuse y Phoenix se pueden autoalojar,
  LangSmith se integra con el ecosistema LangChain y Braintrust (otro de los comparados) es fuerte
  en evals. Uno de los
  comparativos es de Arize, parte interesada. Un criterio verificable al elegir: que nombre
  compatibilidad con OpenTelemetry.

## Prompt cache por proveedor

Implementa el prompt cache de [Cache de modelos](cache-de-modelos.md). Los multiplicadores son
sobre el precio de entrada normal. Copiado de las tres documentaciones el 2026-11-27.

| | Anthropic | OpenAI | Google |
|---|---|---|---|
| Activación | se marca con `cache_control`, hasta 4 puntos de corte | por defecto | implícito por defecto desde Gemini 2.5; explícito con objetos de cache |
| Duración | 5 minutos por defecto; 1 hora con `"ttl":"1h"` | modelos nuevos: 30 min por defecto o 12 h; anteriores: `in_memory` (unos 5-10 min, hasta 1 h) o `24h` | la página no lo dice |
| Escritura | 1,25x (5 min); 2x (1 h) | modelos nuevos: 1,25x (30 min) o 2,5x (12 h); anteriores: sin cargo | la página no lo dice |
| Lectura | 0,1x; 0,05x en Opus 5.5 y Sonnet 5.5; 0,025x en Fable/Mythos 5.1 y 5.2 | 0,1x; 0,05x en algunos modelos | la página no lo dice |
| Mínimo cacheable | de 512 a 4.096 tokens según modelo | 1.024 tokens (GPT-5.6 y posteriores) | de 2.048 a 4.096 tokens según modelo |
| Qué invalida | cualquier cambio en el prefijo (orden `tools`, `system`, `messages`); cambiar herramientas invalida todo; cambiar `tool_choice`, system y tools | contenido distinto al comienzo; guarda el estado KV, no el texto | — |

## Estado del fine-tuning por proveedor

| Proveedor | Estado al 2026-11-27 | Fuente |
|---|---|---|
| OpenAI | "OpenAI is winding down the fine-tuning platform": cerrada a usuarios nuevos; los clientes existentes elegibles pueden crear jobs hasta el 2026-12-15. Fechas de apagado de modelos afinables: `gpt-4.1-nano-2025-04-14` el 2026-10-23; `gpt-4.1` y `gpt-4.1-mini` el 2027-01-14. Métodos que documentaba: SFT, DPO y visión | [distillation](https://developers.openai.com/api/docs/guides/distillation), [model optimization](https://developers.openai.com/api/docs/guides/model-optimization) |
| Anthropic | Fine-tuning de Claude 3 Haiku en Amazon Bedrock, disponible desde el 2024-11-01 en us-west-2; según el buscador, ese modelo llegó a fin de vida el 2026-09-10. No se encontró una página oficial vigente | [anuncio](https://www.anthropic.com/news/fine-tune-claude-3-haiku-ga) **[buscador]** |
| Google | Sin dato: no se buscó una página oficial | — |

> [!NOTE]
> Sin fuente todavía: las alternativas de fine-tuning que quedan con la plataforma de OpenAI en
> retirada (pesos abiertos con LoRA, otros proveedores), y el TTL y el descuento del cache de Google
> en su página viva.
