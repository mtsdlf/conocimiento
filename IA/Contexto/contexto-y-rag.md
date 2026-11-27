---
resumen: >-
  El contexto es la información que se le pone al modelo junto con la consulta para que pueda
  responder lo que no sabe; RAG (generación aumentada por recuperación) es la forma de armarlo
  buscando en una base de documentos solo los fragmentos relevantes para cada consulta.
estado: vigente
estabilidad: estable
fuentes:
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 6 «RAG», pp. 253-275; cap. 5 «Context Length and Context Efficiency», p. 218"
  - https://www.anthropic.com/news/contextual-retrieval
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://arxiv.org/abs/2005.11401
  - https://arxiv.org/abs/2407.16833
  - https://arxiv.org/pdf/2501.01880
aliases: [RAG, retrieval-augmented generation, generación aumentada por recuperación, context construction, construcción de contexto, context engineering]
creado: 2026-11-27
revisado: 2026-11-27
---

# Contexto y RAG

El contexto es la información que se le pone al modelo junto con la consulta para que pueda
responder lo que no sabe; RAG (generación aumentada por recuperación) es la forma de armarlo
buscando en una base de documentos solo los fragmentos relevantes para cada consulta.

Es la primera capa que Huyen suma a un sistema con modelos ("Step 1. Enhance Context"), y la
llama *context construction*. Un modelo sabe lo que vio al entrenarse: no conoce los documentos de
una empresa, el pedido de un cliente ni lo que pasó ayer. RAG no cambia el modelo, cambia lo que
recibe; según el resumen del libro, RAG y agentes "are prompt-based". La idea viene de Lewis et
al. (2020), que según su resumen combinaron la memoria paramétrica de un modelo con un índice de
documentos como memoria no paramétrica.

## De qué está hecho un RAG

Un RAG tiene dos tiempos. Al indexar, los documentos se parten en fragmentos ("RAG typically
requires documents to be split into manageable chunks", según Huyen) y cada fragmento se guarda en
un índice. Al consultar, un recuperador busca los fragmentos más parecidos a la consulta y se los
pone al modelo en el prompt. Dónde se guardan los vectores (un *vector store*) es una pieza
operativa; hay ejemplos en [Plataformas de IA](../Produccion/plataformas-de-ia.md).

## La escalera de recuperación

Huyen presenta estas técnicas en este orden, con la de términos como opción atractiva para empezar.
Ordenarlas como escalera de la más barata a la más precisa, y subir un escalón solo si la evaluación
de la recuperación lo pide, es lectura de esta base.

1. **Por términos** (como BM25): busca palabras. "Term-based retrieval is much faster and cheaper
   than embedding-based retrieval", y según el resumen del cap. 6 da líneas de base fuertes.
2. **Por embeddings**: busca por significado, con vectores. Cuesta más cómputo y "can be
   significantly improved over time".
3. **Híbrida**: "Combining term-based retrieval and embedding-based retrieval is called hybrid
   search".
4. **Reranking**: un recuperador barato trae muchos candidatos y uno más preciso los ordena. Huyen:
   "The second step is also called reranking".
5. **Reescritura de consulta**: en una conversación, "¿y el otro?" no se puede buscar; se reescribe
   con la regla de Huyen: "The new query should make sense on its own."

Anthropic midió una variante, *contextual retrieval*: antes de indexar, se le agrega a cada
fragmento una explicación corta de dónde está dentro del documento. Sobre sus propios datasets, la
tasa de fallas de recuperación en los 20 primeros fragmentos bajó 35% con embeddings contextuales
(de 5,7% a 3,7%), 49% sumando BM25 contextual (a 2,9%) y 67% sumando reranking (a 1,9%). Son
números del laboratorio que vende el modelo, sobre sus datos: sirven como orden de magnitud de cuánto
rinde cada escalón, no como garantía.

## Contexto largo o RAG

Cuando la ventana del modelo crece, la pregunta es si hace falta recuperar o alcanza con poner todo.
Anthropic escribió en 2024 que si la base de conocimiento es "smaller than 200,000 tokens (about 500
pages of material)" se puede poner entera en el prompt, sin RAG. La cifra es de septiembre de 2024 y
las ventanas cambiaron desde entonces; el criterio que queda es comparar el tamaño de la base con la
ventana y con el costo de mandarla en cada consulta (que el
[prompt cache](../Produccion/cache-de-modelos.md) abarata).

> [!IMPORTANT]
> La evidencia sobre contexto largo frente a RAG no coincide. Li et al. (EMNLP 2024) encontraron,
> según el resumen que dio el buscador, que con recursos suficientes el contexto largo rinde más en
> promedio, que en 63% de las consultas los dos dan la misma respuesta, y que mandar a cada consulta
> por el camino que le conviene (su método Self-Route) baja el costo. Una revisión de enero de 2025,
> sin revisión por pares y también según su resumen, recoge que RAG puede superar al contexto largo
> con suficientes fragmentos recuperados, y advierte que los estudios usan pocos datasets de unas
> 200 preguntas. Ninguno de los dos cierra la discusión: se decide midiendo con los datos propios.

Huyen trata el largo de contexto en el cap. 5 ("Context Length and Context Efficiency", p. 218), y
el resumen del cap. 6 agrega una forma de verlo que une esta capa con la de [agente](../Agentes/agente.md):
"The RAG pattern can be seen as a special case of agent where the retriever is a tool the model can
use". Cuando el modelo decide qué buscar y cuándo, se habla de *agentic RAG*; la única fuente
encontrada que lo sistematiza es un survey de arXiv sin revisión por pares.

## Context engineering: el contexto como recurso finito

En 2025 Anthropic propuso *context engineering* como el paso siguiente al prompt engineering:
"the set of strategies for curating and maintaining the optimal set of tokens" durante la
inferencia. El argumento es que "context, therefore, must be treated as a finite resource with
diminishing marginal returns", y el objetivo, "find the smallest set of high-signal tokens that
maximize the likelihood of your desired outcome". Las técnicas que nombra son de agente más que de
RAG clásico: recuperación *just-in-time* (el modelo tiene identificadores livianos y carga el
contenido con herramientas cuando lo necesita), compactar la conversación, notas fuera de la
ventana y subagentes con contexto propio.

La diferencia con el RAG de Huyen es de momento (lectura de esta base): el RAG arma el contexto una vez, antes de llamar
al modelo; el context engineering lo administra durante toda una tarea larga. Que pase a ser parte
del harness de un agente es lo que se cuenta en [Agente](../Agentes/agente.md).

## Cómo falla y cómo se mide

Un RAG puede fallar en dos lugares distintos (lectura de esta base), y la [evaluación](../Evaluacion/evals.md)
tiene que separarlos: el recuperador no trajo el fragmento correcto, o lo trajo y el modelo no lo
usó bien. El primero se arregla subiendo la escalera; el segundo, con el prompt o con el modelo.
Cuándo la falla no es de contexto sino de comportamiento, y conviene otra cosa que RAG, está en
[Prompt, RAG o fine-tuning](../prompt-rag-o-finetuning.md).

> [!NOTE]
> Sin fuente todavía: métricas de recuperación (precision y recall en los primeros k) y fragmentación
> y embeddings para textos en castellano.

El recurso canónico es el cap. 6 de *AI Engineering*, sección "RAG" (pp. 253-275), con "Retrieval
Optimization" (p. 268) para fragmentación, reranking y reescritura; la versión libre es la sección
de contexto del [post de plataforma](https://huyenchip.com/2024/07/25/genai-platform.html). Conviene
fijarse en la escalera como escalera de costo. Para el tramo que el libro no cubre, Anthropic,
["Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents),
por la idea del contexto como recurso finito.
