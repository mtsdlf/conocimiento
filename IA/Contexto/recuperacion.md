---
resumen: >-
  La recuperación es el paso de un RAG que busca los fragmentos que van a entrar en el contexto. Se
  hace de forma léxica (por términos), por embeddings (densa) o combinando las dos, se afina con
  reranking y con la partición en fragmentos, y se mide antes de tocar el modelo que genera.
estado: borrador
estabilidad: semi
fuentes:
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://arxiv.org/abs/2004.04906
  - https://arxiv.org/abs/2104.08663
  - https://arxiv.org/abs/1901.04085
  - https://www.sbert.net/examples/applications/retrieve_rerank/README.html
  - https://research.google/pubs/pub36196/
  - https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion
  - https://www.anthropic.com/news/contextual-retrieval
  - https://www.trychroma.com/research/evaluating-chunking
  - https://en.wikipedia.org/wiki/Discounted_cumulative_gain
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://officechai.com/ai/claude-researcher-explains-how-agentic-search-performed-better-than-rag-for-code-generation/
  - https://ai.engineer/talks/UM6sFg_jdlE-rag-is-dead-right-kuba-rogut
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 6 «Retrieval Algorithms» p. 257 y «Retrieval Optimization» p. 268 (solo índice)"
aliases: [retrieval, recuperador, retriever, búsqueda híbrida, hybrid search, reranking, chunking, partición en fragmentos, BM25, búsqueda agentiva, agentic search, RRF]
creado: 2026-11-27
revisado:
---

# Recuperación

La recuperación es el paso de un RAG que busca los fragmentos que van a entrar en el contexto. Se
hace de forma léxica (por términos), por embeddings (densa) o combinando las dos, se afina con
reranking y con la partición en fragmentos, y se mide antes de tocar el modelo que genera.

[Contexto y RAG](contexto-y-rag.md) da la visión de conjunto y la escalera de técnicas, de la más
barata a la más precisa. Acá se detalla cada escalón: qué dice la evidencia, cómo se combinan los
resultados y cómo se mide si el recuperador trajo lo que hacía falta. Qué es un embedding como
representación se explica en [Token y embedding](../Modelos/token-y-embedding.md).

## Léxica o densa: depende de si hay datos del dominio

La búsqueda léxica (por términos, como BM25) compara palabras; la búsqueda por embeddings (densa)
compara vectores, que capturan
significado. Dos estudios parecen contradecirse:

- **DPR** (Karpukhin et al., EMNLP 2020): un recuperador denso entrenado para la tarea supera a BM25
  "by 9%–19% absolute" en precisión en los 20 primeros resultados, en varios conjuntos de preguntas
  abiertas (según su abstract).
- **BEIR** (Thakur et al., NeurIPS 2021): probando en dominios para los que los modelos no se
  entrenaron, BM25 resiste como línea de base, y los recuperadores densos "often underperform" (según su
  abstract).

En lectura de esta base, leídos juntos dicen lo mismo: un recuperador denso entrenado en el dominio le
gana a BM25; uno que se usa en un dominio que no vio, no necesariamente. Por eso, también en lectura
de esta base, BM25 es la línea de base que conviene medir primero; el resumen del cap. 6 de Huyen
dice que da líneas de base fuertes.

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre BM25 (Robertson y Zaragoza) y sobre recuperación y
> partición para textos en castellano.

## Fusionar dos rankings sin comparar puntajes

La búsqueda híbrida corre las dos búsquedas y junta los resultados. El problema es que el puntaje de
BM25 y la similitud entre vectores no están en la misma escala. La fusión por posición recíproca
(*reciprocal rank fusion*, RRF) lo esquiva; el método se atribuye a Cormack et al. (SIGIR 2009),
según la ficha del paper vista solo por buscador. A cada documento le suma
1/(k + posición) por cada lista en la que aparece. Usa solo posiciones, así que no hay que
normalizar nada, y según la documentación de Elastic "requires no tuning"; ahí k vale 60 por
defecto. Anthropic combina BM25 y embeddings con "rank fusion techniques", sin decir cuál.

## Reranking: un modelo caro sobre pocos candidatos

El reranking reordena lo que trajo un recuperador barato. Un *cross-encoder* recibe la consulta y el
documento juntos y devuelve un puntaje: es más preciso que comparar embeddings por separado, pero su
costo crece con cada candidato. Por eso, según la documentación de Sentence-Transformers, se aplica
a unos 100 candidatos y no a todo el índice. El método viene de Nogueira y Cho (2019), que superaron
al mejor anterior "by 27% (relative) in MRR@10" en MS MARCO.

En la medición de Anthropic sobre sus propios datos, sumar reranking bajó la tasa de fallas de 2,9%
a 1,9%; el salto mayor fue el primero, los embeddings contextuales (de 5,7% a 3,7%). Las cifras
completas están en [Contexto y RAG](contexto-y-rag.md).

## Partición en fragmentos

La partición en fragmentos (*chunking*) decide qué unidad puede recuperarse. Anthropic dice que el tamaño,
el borde y el solapamiento "can affect retrieval performance", y que en su prueba, con fragmentos de
"no more than a few hundred tokens", traer 20 rindió mejor que traer 5 o 10.

El estudio con números entre estrategias que se encontró es de Chroma (2024), con 472 consultas sobre cinco
corpus. Unas estrategias superaron a otras "by up to 9% in recall"; partir de forma recursiva en
fragmentos de 200 tokens sin solapamiento dio 88,1 de recall con buen desempeño parejo, y la
configuración por defecto de una API conocida (800 tokens con 400 de solapamiento) fue la peor en
precisión. Los propios autores avisan que las consultas las generó un modelo y "tend to generate a
specific style of question", que el conjunto es chico y que no midieron tiempo. Sirve como ejemplo de
método para medir con datos propios, no como receta.

## Cómo se mide la recuperación

La recuperación se mide aparte de la respuesta: si el fragmento correcto no llegó, ningún prompt lo
arregla. Las fuentes leídas usan dos medidas:

- **Tasa de fallas o recall en los primeros k**: si el fragmento que hacía falta estaba entre los k
  que se trajeron (definición en lectura de esta base, a falta de una fuente primaria). Anthropic
  reporta la tasa de fallas en los 20 primeros, y Chroma, recall.
- **nDCG**: suma la relevancia de cada resultado dividida por el logaritmo de su posición, y la
  normaliza contra el orden ideal para que quede entre 0 y 1. Premia que lo relevante aparezca
  arriba. Según Wikipedia, "Normalized DCG does not penalize missing documents in the result" si no se
  fija el tamaño del conjunto.

Cómo se arma un conjunto de casos para medir está en [Evals](../Evaluacion/evals.md), y las
métricas en general, en [Métricas de evaluación](../Evaluacion/metricas-de-evaluacion.md).

> [!NOTE]
> Sin fuente todavía: una definición primaria de recall@k, precision@k y MRR (un manual de
> recuperación de información); nDCG sale de una fuente secundaria.

## Búsqueda agentiva en lugar de un índice

Un [agente](../Agentes/agente.md) puede buscar por su cuenta en lugar de consultar un índice armado
de antemano. Anthropic describe ese modelo: el agente guarda "lightweight identifiers (file paths,
stored queries, web links, etc.)" y carga el contenido cuando lo necesita, con herramientas como
`glob` y `grep`.

> [!IMPORTANT]
> Si la búsqueda agentiva reemplaza al índice vectorial es una discusión sin estudio controlado.
> Según notas secundarias sobre una charla y un podcast (un solo origen), el equipo del agente de
> código de Anthropic probó RAG con una base vectorial local y pasó a búsqueda agentiva por
> resultados "mostly vibes" más algunos benchmarks internos, y porque indexar suma un paso y el
> índice se desactualiza; el costo es más latencia y más tokens. En contra, un ingeniero de una
> empresa de búsqueda vectorial sostiene que eso no prueba que la recuperación semántica no sirva para
> todo agente de código (también secundario). Las dos posiciones hablan de código y no se generalizan a documentos de
> una empresa; que en código pesen más los nombres exactos es lectura de esta base.

## Qué leer sobre recuperación

Para entender, Huyen, cap. 6, "Retrieval Algorithms" (p. 257) y "Retrieval Optimization" (p. 268),
leído solo por su índice; el resumen de capítulos del repo del libro no nombra la partición ni la
búsqueda híbrida, pero el [post de plataforma](https://huyenchip.com/2024/07/25/genai-platform.html)
de Huyen sí las trata. Para hacerlo,
["Introducing Contextual Retrieval"](https://www.anthropic.com/news/contextual-retrieval), el mejor
ejemplo de medir cada escalón por separado, y la página
["Retrieve & Re-Rank"](https://www.sbert.net/examples/applications/retrieve_rerank/README.html). Para
decidir con números propios, el [informe de partición de Chroma](https://www.trychroma.com/research/evaluating-chunking),
leído como método. En todos, fijarse en separar si falló el recuperador o el modelo, y en medir el
recall en los primeros k antes de tocar el prompt.
