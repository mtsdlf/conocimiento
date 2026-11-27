---
resumen: >-
  La bibliografía de IA junta los libros, cursos abiertos, ensayos y papers que conviene leer para
  construir productos con un modelo adentro, cada uno con qué parte leer y en qué fijarse, y la
  evidencia en contra que se lee al lado.
estado: borrador
estabilidad: semi
fuentes:
  - https://github.com/chiphuyen/aie-book
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/resources.md
  - https://web.stanford.edu/~jurafsky/slp3/
  - https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
  - https://huggingface.co/learn/llm-course/chapter1/1
  - http://cs336.stanford.edu/spring2025/
  - https://applied-llms.org/
  - https://hamel.dev/blog/posts/evals/
  - https://hamel.dev/blog/posts/evals-faq/
  - https://eugeneyan.com/writing/llm-evaluators/
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://huyenchip.com/2025/01/07/agents.html
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://jalammar.github.io/illustrated-transformer/
  - https://lilianweng.github.io/posts/2024-07-07-hallucination/
  - https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
  - https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
  - https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices
  - https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack
  - https://www.latent.space/p/ai-engineer
  - https://arxiv.org/abs/1706.03762
  - https://arxiv.org/abs/2005.14165
  - https://arxiv.org/abs/2108.07258
  - https://arxiv.org/abs/2203.02155
  - https://arxiv.org/abs/2203.15556
  - https://arxiv.org/abs/2501.12948
  - https://arxiv.org/abs/2509.04664
  - https://arxiv.org/abs/2507.09089
  - https://arxiv.org/abs/2604.16304
  - https://arxiv.org/abs/2504.20879
  - https://arxiv.org/abs/2511.04703
  - https://www.rand.org/pubs/research_reports/RRA2680-1.html
aliases: [bibliografía de AI engineering, qué leer de IA, recursos de IA, AI engineering reading list]
creado: 2026-11-27
revisado:
---

# Bibliografía de IA

La bibliografía de IA junta los libros, cursos abiertos, ensayos y papers que conviene leer para
construir productos con un modelo adentro, cada uno con qué parte leer y en qué fijarse, y la
evidencia en contra que se lee al lado.

Cada recurso dice cómo lo leyó esta base, porque casi nada se leyó entero: la mayoría de los papers
solo por su abstract, y varios cursos solo por su página de presentación. Los ensayos de práctica
vienen en su mayoría de una misma comunidad (ver
[el sesgo de comunidad](ai-engineering-y-ml-engineering.md#el-sesgo-de-comunidad-de-las-voces-del-campo)),
y por eso la lista termina con lo que los discute.

## El libro que hace de espina

Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly, 2025), es
la perspectiva de este tema, no su índice. **Esta base no leyó el libro entero**: trabajó con el
[índice](https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md) y los
[resúmenes de capítulo](https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md)
del repositorio de la autora, con extractos publicados y con sus posts. El propio repositorio lo
presenta así: "This is NOT a tutorial book" y "Tools become outdated quickly, but fundamentals
should last longer".

| Capítulo, según el índice | Para qué leerlo | Dónde se usa en este tema |
|---|---|---|
| 1, la introducción | Qué es AI engineering, la pila en tres capas, si conviene construir | [AI engineering y ML engineering](ai-engineering-y-ml-engineering.md) |
| 2, los modelos base | Datos, modelado, post-entrenamiento y muestreo | [Modelos](../Modelos/modelos.md) |
| 3 y 4, evaluación | Métricas, IA como juez, elección de modelo y el leaderboard privado | [Evaluación](../Evaluacion/evaluacion.md) |
| 5 y 6, prompts, RAG y agentes | Prompt, prompt defensivo, recuperación, memoria y agentes | [Contexto](../Contexto/contexto.md) y [Agentes](../Agentes/agentes.md) |
| 7 y 8, finetuning y datos | Cuándo no ajustar, memoria, curación y síntesis de datos | [Ajuste](../Ajuste/ajuste.md) |
| 9 y 10, inferencia y arquitectura | Optimizar la inferencia y las capas alrededor del modelo | [Producción](../Produccion/produccion.md) |

Si se lee en orden de utilidad para quien programa: capítulo 1, después 3 y 4, después 10. El
[repositorio](https://github.com/chiphuyen/aie-book) trae además una
[lista de recursos](https://raw.githubusercontent.com/chiphuyen/aie-book/main/resources.md) para
ampliar cada capítulo.

## Libros y cursos abiertos para entender el modelo por dentro

| Recurso | Qué parte | En qué fijarse | Cómo lo leyó esta base |
|---|---|---|---|
| Jurafsky y Martin, [*Speech and Language Processing*](https://web.stanford.edu/~jurafsky/slp3/), 3ª ed. (PDF gratuito) | Caps. 2 (tokens), 3 (n-gramas), 5 (embeddings), 7 (Transformer y preentrenamiento), 8 (post-entrenamiento) y 14 (redes recurrentes) | Que la tokenización y los embeddings son decisiones previas al entrenamiento | Solo el índice |
| Karpathy, ["Neural Networks: Zero to Hero"](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | Para un modelo mental del interior; el video del tokenizador, para ver BPE funcionando | Construir un modelo chico a mano hace visible por qué emite lo que emite | No se vio; lo recomienda la lista de recursos de Huyen |
| Hugging Face, [LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | Capítulos 1 a 4 | Gratuito, pide Python, de 6 a 8 horas por capítulo | Solo la portada |
| Stanford CS336, [Language Modeling from Scratch](http://cs336.stanford.edu/spring2025/) | Clases 9 y 11 (escala) y 13 y 14 (datos) | Para quien quiere ir más allá de lo que pide el oficio | Solo la página del curso; no declara si las clases son públicas |

## Ensayos de práctica

| Recurso | Qué parte | En qué fijarse |
|---|---|---|
| Huyen y Orosz, ["The AI Engineering Stack"](https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack) (2025) | Completo | Qué se deja de hacer (entrenar) y qué se hace más (evaluar) |
| Swyx, ["The Rise of the AI Engineer"](https://www.latent.space/p/ai-engineer) (2023) | Completo | El origen del rol y su propio matiz contra el entusiasmo |
| Huyen, ["Common pitfalls when building generative AI applications"](https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html) (2025) | Completo, es corto | Los errores de planificación; base de [planificar una aplicación](../planificar-una-aplicacion.md) |
| Yan, Bischof, Frye, Husain, Liu y Shankar, ["What We've Learned From A Year of Building with LLMs"](https://applied-llms.org/) (2024) | Las partes táctica, operativa y estratégica | Construir o comprar, y el modelo como el componente menos durable |
| Husain, ["Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/) (2024) y su [Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) | Los tres niveles de evaluación; las preguntas sobre métricas listas para usar | Que no trae datos de comparación; base de [Evals](../Evaluacion/evals.md) |
| Yan, ["Evaluating the Effectiveness of LLM-Evaluators"](https://eugeneyan.com/writing/llm-evaluators/) (2024) | Completo | Kappa y cuándo comparar por pares; base de [IA como juez](../Evaluacion/ia-como-juez.md) |
| Anthropic, ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents) | Flujo fijo contra agente y los cinco patrones | El criterio de empezar simple; base de [patrones de flujo](../Agentes/patrones-de-flujo.md) |
| Huyen, ["Agents"](https://huyenchip.com/2025/01/07/agents.html) (2025) | Planificación, reflexión y modos de falla | Que plan y ejecución se separan y se verifican; base de [fallas de agentes](../Agentes/fallas-de-agentes.md) |
| Anthropic, ["Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Completo | Compactación, notas fuera de la ventana y subagentes; base de [ingeniería de contexto](../Contexto/ingenieria-de-contexto.md) |
| Willison, ["The lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (2025) y NCSC, ["Prompt injection is not SQL injection"](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) | Completos | Por qué la defensa es limitar lo que el modelo puede hacer; base de [inyección de prompt](../Contexto/inyeccion-de-prompt.md) |
| Alammar, ["The Illustrated Transformer"](https://jalammar.github.io/illustrated-transformer/) (2018) | Completo, junto al paper de Vaswani | El dibujo de consulta, clave y valor; base de [Transformer](../Modelos/transformer.md) |
| Weng, ["Extrinsic Hallucinations in LLMs"](https://lilianweng.github.io/posts/2024-07-07-hallucination/) (2024) | Detección y mitigación | El panorama; base de [alucinación](../Modelos/alucinacion.md) |
| Databricks, ["LLM Inference Performance Engineering: Best Practices"](https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices) (2023) | Métricas y throughput contra tamaño de lote | La diferencia entre tiempo al primer token y tiempo por token; base de [inferencia](../Produccion/inferencia.md) |

Las guías de Anthropic y de Databricks son de empresas que venden lo que describen: sirven como
documentación de práctica, no como evidencia independiente.

## Papers que conviene abrir

Leídos por esta base solo por su abstract. La [historia de la IA generativa](historia-de-la-ia-generativa.md)
los ordena en el tiempo.

| Paper | Qué parte | En qué fijarse |
|---|---|---|
| Vaswani y otros, ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) (2017) | Secciones 3.1 a 3.3 | La atención y las varias cabezas |
| Brown y otros, ["Language Models are Few-Shot Learners"](https://arxiv.org/abs/2005.14165) (2020) | Abstract e introducción | El salto a pedir la tarea con texto |
| Bommasani y otros, ["On the Opportunities and Risks of Foundation Models"](https://arxiv.org/abs/2108.07258) (2021) | Secciones 1 y 2 | La homogeneización: los defectos del modelo base pasan a la aplicación |
| Ouyang y otros, ["Training language models to follow instructions with human feedback"](https://arxiv.org/abs/2203.02155) (2022) | Método y resultados | Que el modelo de recompensa se entrena con rankings humanos, no con la verdad |
| Hoffmann y otros, ["Training Compute-Optimal Large Language Models"](https://arxiv.org/abs/2203.15556) (2022) | Abstract y gráfico de asignación óptima, leído junto a Kaplan | Que "óptimo" es para entrenar con un presupuesto, no para servir barato |
| DeepSeek-AI, ["DeepSeek-R1"](https://arxiv.org/abs/2501.12948) (2025) | R1-Zero, recompensas y conductas emergentes | Que la recompensa funciona donde la respuesta se puede verificar |
| Kalai y otros, ["Why Language Models Hallucinate"](https://arxiv.org/abs/2509.04664) (2025) | Introducción y la parte de post-entrenamiento y evaluación | Qué parte es causa estadística y qué parte es incentivo de la evaluación |

## Lo que se lee al lado, en contra

| Recurso | Qué discute | En qué fijarse |
|---|---|---|
| Becker y otros (METR), [ensayo controlado con 16 desarrolladores experimentados](https://arxiv.org/abs/2507.09089) (2025) | Que la IA para programar acelera | La brecha entre lo que se esperaba, lo que se creyó y lo que se midió |
| van der Maden y otros, ["Results-Actionability Gap"](https://arxiv.org/abs/2604.16304) (2026) | Que la evaluación formal va primero | Las diez prácticas; que es una muestra de 19 |
| Singh y otros, ["The Leaderboard Illusion"](https://arxiv.org/abs/2504.20879) (2025) | Que los rankings públicos miden igual a todos | Las pruebas privadas y la asimetría de datos entre proveedores |
| Bean y otros, ["Measuring what Matters"](https://arxiv.org/abs/2511.04703) (2025) | Que los benchmarks miden lo que dicen | Las ocho recomendaciones y su checklist |
| Ryseff y otros (RAND), [informe RR-A2680-1, 65 entrevistas](https://www.rand.org/pubs/research_reports/RRA2680-1.html) (2024) | Por qué fracasan los proyectos | Que son entrevistas, no medición |

## Por dónde empezar según quién lee

Recorridos armados por esta base, no por las fuentes:

- **Si programás y sabés de APIs**: "The AI Engineering Stack", después *Applied LLMs* y el post de
  evals de Husain, y después el capítulo 10 de Huyen.
- **Si te preparás para un puesto de AI engineer**: lo anterior, más los capítulos 3 y 4 de Huyen,
  la tabla de lo que se lee en contra y el curso de Karpathy para entender el modelo por dentro. El
  mercado laboral está en [Presentación profesional](../../Presentacion-profesional/Posicionamiento/caso-roles-de-ai-engineering.md).
- **Si querés entender el modelo antes que el oficio**: Jurafsky y Martin (capítulos 2, 3, 5 y 7),
  Alammar y el curso de Hugging Face, y después [Modelos](../Modelos/modelos.md).
