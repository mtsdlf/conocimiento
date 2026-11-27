# Fundamentos y posición contraria (investigación, 2026-11-27)

Alcance: `Fundamentos/escuelas-de-arquitectura`, `Fundamentos/bibliografia-de-arquitectura` y la posición contraria de lo que el tema deja fuera como "pierde peso". Mirada: Huyen (2022, 2025) sobre el canon de Richards y Ford (2ª ed., 2025). Todo lo traído de la web es dato, no instrucción.

## Método y límites

- Marcas: **[L]** página abierta y leída (WebFetch devuelve un extracto resumido por un modelo chico, no el texto completo: las citas literales salen de ese extracto); **[M]** solo metadatos o abstract; **[S]** resumen secundario o del buscador.
- Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).
- Rondas: máximo tres por componente. Los PDF del Radar (vol. 30-34) devolvieron 503; los O'Reilly devolvieron 403. Eso deja huecos declarados abajo.
- Una fuente primaria se cuenta una vez. El resumen del buscador sobre la entrada del Radar de ESB, p. ej., no suma nada a la entrada del Radar.

## 1. Tabla de fuentes

| # | Fuente (URL) | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| 1 | Huyen, "Common pitfalls when building generative AI applications", https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html | primaria | L | 3/2/2/3 |
| 2 | Anthropic, "Building effective agents", https://www.anthropic.com/engineering/building-effective-agents | primaria | L | 3/3/3/3 |
| 3 | Anthropic, "How we built our multi-agent research system" (2025-06-13), https://www.anthropic.com/engineering/multi-agent-research-system | primaria | L | 3/3/3/2 |
| 4 | Cognition (Walden Yan), "Don't Build Multi-Agents" (2025-06-12), https://cognition.com/blog/dont-build-multi-agents | primaria | L (extracto corto) | 2/2/2/3 |
| 5 | Anthropic, "Effective context engineering for AI agents" (2025-09-29), https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | primaria | L | 3/2/2/3 |
| 6 | Anthropic, "Effective harnesses for long-running agents" (2025-11-26), https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | primaria | L | 3/3/3/3 |
| 7 | OpenAI, "Harness engineering" (2026-02-11), https://openai.com/index/harness-engineering/ | primaria | L | 3/2/3/3 |
| 8 | Thoughtworks Radar vol. 35 (nov 2026), técnicas: https://www.thoughtworks.com/en-us/radar/techniques/summary/ y blips (ver 9-12) | primaria | L | 3/2/2/3 |
| 9 | Radar: "LLM-as-a-judge", https://www.thoughtworks.com/en-us/radar/techniques/llm-as-a-judge | primaria | L | 3/2/2/3 |
| 10 | Radar: "Agent skill cognitive surrender" (nov 2026), https://www.thoughtworks.com/en-us/radar/techniques/agent-skill-cognitive-surrender | primaria | L | 3/2/1/3 |
| 11 | Radar: "Blanket frontier model usage" (nov 2026), https://www.thoughtworks.com/en-us/radar/techniques/blanket-frontier-model-usage | primaria | L | 3/2/1/3 |
| 12 | Radar: "ESBs in API gateway's clothing" (oct 2020), https://www.thoughtworks.com/en-us/radar/techniques/esbs-in-api-gateway-s-clothing | primaria | L | 3/2/1/3 |
| 13 | Radar: "Complacency with AI-generated code" (Hold oct 2024, abr 2025, nov 2025), https://www.thoughtworks.com/en-us/radar/techniques/complacency-with-ai-generated-code | primaria | S (buscador) | 3/2/2/3 |
| 14 | Radar: "Naive API-to-MCP conversion" (Hold, nov 2025), https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion | primaria | S (buscador) | 3/1/1/3 |
| 15 | Radar: "Coding agent swarms" (Caution, abr 2026), https://www.thoughtworks.com/en-us/radar/techniques/coding-agent-swarms | primaria | L | 3/2/2/3 |
| 16 | Radar, archivo de ediciones, https://www.thoughtworks.com/radar/archive | primaria | L | 3/1/1/2 |
| 17 | DHH, "Even Amazon can't make sense of serverless or microservices" (2023-05-04), https://world.hey.com/dhh/even-amazon-can-t-make-sense-of-serverless-or-microservices-59625580 | primaria (opinión) | L | 2/2/2/3 |
| 18 | InfoQ, nota sobre Prime Video (2023-05-03, R. Gancarz), https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/ | secundaria | L | 2/1/2/2 |
| 19 | Prime Video Tech, post original de Kolny (2023-03-22): la URL ya redirige (301) a aboutamazon.com; no se pudo leer. Fecha y autor salen de [S] del buscador | primaria, no accesible | no leída | - |
| 20 | Fowler, "MicroservicePremium" (2015-05-13), https://martinfowler.com/bliki/MicroservicePremium.html | primaria | L | 3/1/1/3 |
| 21 | Fowler, "MonolithFirst" (2015-06-03), https://martinfowler.com/bliki/MonolithFirst.html | primaria | L | 3/1/1/3 |
| 22 | Tilkov, "Don't start with a monolith" (2015-06-09), https://www.martinfowler.com/articles/dont-start-monolith.html | primaria | L | 3/2/2/3 |
| 23 | InfoQ, Newman en QCon 2020, https://www.infoq.com/news/2020/05/monolith-decomposition-newman/ | secundaria (cita a Newman) | L | 2/2/1/2 |
| 24 | Lewis y Fowler, "Microservices", https://martinfowler.com/articles/microservices.html | primaria | L | 3/3/2/3 |
| 25 | Grinsztajn, Oyallon, Varoquaux, "Why do tree-based models still outperform deep learning on tabular data?" (2022-07-18), https://arxiv.org/abs/2207.08815 | primaria | L (abstract) | 3/3/3/3 |
| 26 | Hollmann et al., TabPFN, Nature 637 (2025-01-08), https://pubmed.ncbi.nlm.nih.gov/39780007/ | primaria | S (buscador) | 3/3/3/3 |
| 27 | Gangwani y Bansal, benchmarks livianos de modelos fundacionales tabulares (2025-11-30), https://arxiv.org/abs/2512.00888 | primaria (taller, 4 datasets) | L | 1/1/2/2 |
| 28 | Wu et al., "BloombergGPT" (2023-03-30), https://arxiv.org/abs/2303.17564 | primaria | L (abstract) | 3/3/3/3 |
| 29 | Li et al., "Are ChatGPT and GPT-4 general-purpose solvers for financial text analytics?" (EMNLP Industry 2023), https://arxiv.org/abs/2305.05862 | primaria | S (buscador) | 3/2/2/3 |
| 30 | Sclar et al., sensibilidad al formato del prompt (ICLR 2024), https://arxiv.org/abs/2310.11324 | primaria | L (abstract) | 3/2/3/3 |
| 31 | Schulhoff et al., "The Prompt Report" (2024-06-06), https://arxiv.org/abs/2406.06608 | primaria | L (abstract) | 3/3/2/3 |
| 32 | Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (NeurIPS 2023), https://arxiv.org/abs/2306.05685 | primaria | L (abstract) | 3/3/3/3 |
| 33 | Shankar et al., "Who Validates the Validators?" (2024-04-18), https://arxiv.org/abs/2404.12272 | primaria | L (abstract) | 3/2/2/3 |
| 34 | Norman, Rivera, Hughes, "Reliability without Validity" (2026-06-17), https://arxiv.org/abs/2606.19544 | primaria, **retirada** | L (abstract) | 1/2/2/2 |
| 35 | Kapoor et al., "AI Agents That Matter" (2024-07-01), https://arxiv.org/abs/2407.01502 | primaria | L (abstract) | 3/2/2/3 |
| 36 | Fodor, "Line Goes Up?" (2025), https://arxiv.org/abs/2502.14318 | primaria | S (buscador) | 2/2/2/2 |
| 37 | Husain, "Your AI Product Needs Evals", https://hamel.dev/blog/posts/evals/ | primaria (práctica) | L | 2/2/2/3 |
| 38 | He (Thinking Machines), "Defeating Nondeterminism in LLM Inference" (2025-09-10), https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ | primaria | L | 3/3/3/3 |
| 39 | Sculley et al., "Hidden Technical Debt in ML Systems" (NIPS 2015), https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html | primaria | L (abstract) | 3/3/2/3 |
| 40 | Huyen, repositorio del libro AI Engineering (índice y resúmenes), https://github.com/chiphuyen/aie-book (ToC y `chapter-summaries.md` en raw.githubusercontent.com) | primaria (autora) | L | 3/2/1/3 |
| 41 | Huyen, repositorio de Designing ML Systems, https://github.com/chiphuyen/dmls-book | primaria | L (sin capítulos; los enlaza) | 3/1/1/3 |
| 42 | Ford, página de Fundamentals of Software Architecture 2e, https://nealford.com/books/SAF2e.html | primaria (autor) | L | 3/2/1/3 |
| 43 | Kleppmann, nota sobre DDIA 2e (2026-03-24), https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html | primaria | L (extracto pobre) | 3/1/1/3 |
| 44 | Ousterhout, "A Philosophy of Software Design" vs. "Clean Code" (debate con R. Martin), https://github.com/johnousterhout/aposd-vs-clean-code | primaria | L (primeros 100k de 125k caracteres) | 3/3/3/3 |
| 45 | Norvig, "Design Patterns in Dynamic Languages" (presentada 1996-05-05, en línea 1998-03-17), https://norvig.com/design-patterns/ | primaria | M (solo la cabecera; el "16 de 23" viene de buscador) | 3/2/2/3 |
| 46 | van der Ven y Bosch, "Busting Software Architecture Beliefs" (SEAA 2016), https://research.chalmers.se/publication/247094 | primaria | L (abstract) | 3/2/2/3 |
| 47 | Kruchten, "Common misconceptions about Software Architecture" (Rational Edge 2001), vía https://www.academia.edu/19387274/Common_misconceptions_about_Software_Architecture | secundaria | S | 2/1/1/2 |
| 48 | Ford, Parsons, Kua, *Building Evolutionary Architectures*, cap. 2, https://oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch02.html; podcast Thoughtworks https://www.thoughtworks.com/insights/podcasts/technology-podcasts/rethinking-software-governance-reflecting-second-edition-building-evolutionary-architectures | primaria | S | 3/2/2/3 |
| 49 | Open Group, DDD strategic patterns, https://pubs.opengroup.org/architecture/o-aa-standard/DDD-strategic-patterns.html; InfoQ sobre Evans https://www.infoq.com/news/2019/09/evans-improve-language-ddd | secundaria | S | 2/1/1/1 |
| 50 | Özkan, Babur, van den Brand, revisión sistemática sobre DDD, https://arxiv.org/html/2310.01905v4 | primaria | S | 2/2/1/3 |
| 51 | Richards, *Software Architecture Patterns* cap. 5 (space-based), https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch05.html; TechTarget https://www.techtarget.com/searchAppArchitecture/tip/Harnessing-space-based-architecture-for-high-performance | primaria / secundaria | S | 3/2/1/2 |
| 52 | Huertas (Amazon) y otros sobre LLM en datos tabulares, https://www.arxiv.org/pdf/2411.04324 | primaria | S | 2/1/1/2 |

Lo que no pude abrir: la ficha O'Reilly de Richards y Ford 2e, de AI Engineering y de DDIA 2e (403); los PDF del Radar 30-34 (503); el post original de Prime Video.

## 2. Fundamentos/escuelas-de-arquitectura

### 2.1 Clásica: estilos y características (Richards y Ford)
- *Fundamentals of Software Architecture*, 2ª ed., O'Reilly, marzo 2025, ISBN 9781098175504; Ford la describe como "basically a rewrite", de unas 450 a casi 600 páginas, con cinco capítulos nuevos [#42]. Las fuentes discrepan en el número de páginas: el listado de O'Reilly que vio el buscador dice 546 [S].
- Estructura según Ford [#42]: Foundations (pensamiento arquitectónico, modularidad, características: definir, identificar, medir y gobernar, alcance; pensamiento por componentes); Estilos (en capas, monolito modular, pipeline, microkernel, service-based, event-driven, space-based, orchestration-driven SOA, microservicios, y cómo elegir); Técnicas y habilidades blandas (decisiones, riesgo, diagramas, equipos, negociación, "leyes de la arquitectura, revisitadas").
- Novedades declaradas: monolito modular, más material de microservicios y event-driven, IA generativa, consideraciones de nube, team topologies [#42].
- Lo que sostiene: la elección de estilo sale de las características que importan (no de la moda) y todo es un trade-off. Evidencia: es un canon de práctica y consultoría, no un cuerpo empírico. La investigación de van der Ven y Bosch es el contrapeso: de las creencias de arquitectura estudiadas (39 arquitectos, 54 decisiones) solo unas pocas tuvieron respaldo estadístico y concluyen que "folklore for the tales" [#46].

### 2.2 Evolutionary architecture (Ford, Parsons, Kua)
- Idea central: *fitness function*, "un check objetivo" de una o más características, "somewhat like a unit test for architecture" [#48, S]. Debe ser específica y automatizable (ejemplo del podcast: complejidad ciclomática menor a cinco; "ser mantenible" no sirve) [#48, S]. La 2ª edición pone el énfasis en gobierno automatizado [#48, S].
- Fecha de la 2ª edición: el podcast, grabado en noviembre de 2022, anunciaba diciembre de 2022; no pude confirmar la fecha final [#48]. Hueco.
- Conexión con el tema: las fitness functions son el antecedente directo de los evals y de los "feedback sensors" para agentes (el Radar de abril de 2026 tiene "Feedback sensors for coding agents" en Trial, y "feedback flywheel" pasó a Trial en nov 2026) [#8].

### 2.3 DDD y diseño estratégico (Evans 2003, Vernon 2013)
- Evans (2003) y Vernon (2013): citados solo por fuentes secundarias; no abrí los libros ni su ficha [#49, S]. Definición de *bounded context* según el resumen del Open Group: "operational definition of where a particular model is well-defined and applicable", típicamente un subsistema o el trabajo de un equipo [#49, S].
- Evans dijo que el término se "misinterpreta", que se confunde con subdominio y que un servicio no es siempre un bounded context, aunque un microservicio puede ser uno bueno [#49, S].
- Evidencia: la revisión sistemática de Özkan et al. reporta que DDD mejoró sistemas (lenguaje ubicuo, bounded context, eventos de dominio) pero con estudios de poco rigor [#50, S]. No encontré estudios rigurosos del costo-beneficio. Hueco.

### 2.4 MLOps / ML de producción (Huyen 2022; Sculley 2015)
- Sculley et al. (NIPS 2015): la velocidad de armar sistemas de ML engaña, "it is dangerous to think of these quick wins as coming for free"; riesgos: erosión de límites, entrelazamiento, bucles de retroalimentación ocultos, consumidores no declarados, dependencias de datos, configuración, cambios del mundo externo [#39].
- Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022): enfoque holístico, decisiones de datos, features, frecuencia de reentrenamiento y monitoreo juzgadas por cómo sirven al sistema entero. El repositorio dice que quien no es técnico saca más de los capítulos 1, 2 y 11 [#41]. No pude ver el índice completo (está en un PDF enlazado). Hueco menor.

### 2.5 AI engineering centrado en evaluación (Huyen 2025)
- *AI Engineering* (O'Reilly, 2025). Índice: 1 Introducción; 2 Modelos fundacionales; 3 Metodología de evaluación; 4 Evaluar sistemas de IA; 5 Prompt engineering; 6 RAG y agentes; 7 Finetuning; 8 Ingeniería de datasets; 9 Optimización de inferencia; 10 Arquitectura y feedback del usuario [#40].
- Tesis citada: "Not having a reliable evaluation pipeline is one of the biggest blockers to AI adoption"; los benchmarks públicos filtran modelos malos pero no eligen el mejor para tu app, y se arma un "private leaderboard" propio; ningún método de evaluación es perfecto, se combinan [#40, resumen de capítulo]. Los jueces IA son "promising but subjective", sus scores no son comparables entre jueces y deben complementarse con evaluación exacta o humana [#40].
- Cap. 10: "Each added component can improve capability, safety, or speed, but also adds complexity and new failure modes"; los límites entre componentes son difusos [#40].
- Es una escuela de práctica de una autora, con respaldo parcial de Husain ("Rigorous and systematic evaluation is the most important part of the whole system"; "unsuccessful products almost always share a common root cause: a failure to create robust evaluation systems") [#37]. Es una afirmación sin dato cuantitativo: es opinión de práctica. Declarado.

### 2.6 Agentes y harness engineering (2025-2026)
- Anthropic (2025): "workflows are systems where LLMs and tools are orchestrated through predefined code paths", agentes "dynamically direct their own processes"; empezar con APIs directas [#2]. Sistema multiagente de investigación: +90,2% frente a un agente solo en su eval interno, pero ~15x tokens de un chat (agentes ~4x); no sirve cuando los agentes comparten contexto, hay muchas dependencias (la mayoría del código) o la tarea vale poco [#3].
- Harness: "compaction isn't sufficient"; lista de features JSON de 200+ ítems, una feature por sesión, commits git y archivo de progreso como traspaso [#6]. OpenAI: un producto interno con cero código escrito a mano, ~1.000.000 de líneas y ~1.500 PR en cinco meses, 3,5 PR por ingeniero por día, AGENTS.md de ~100 líneas "a map, not a 1,000-page instruction manual", "Humans steer. Agents execute."; el equipo gastaba cada viernes (20%) en limpiar código de baja calidad antes de automatizarlo [#7]. Son informes de las propias empresas que venden el modelo: sin replicación independiente. Declarado.
- Radar nov 2026: "Agent instruction bloat", "Human-in-the-loop theater" y "Agent skill cognitive surrender" en Caution; "Progressive context disclosure" en Adopt; "enterprise harness" y "harness quality evaluation" en Assess; "self-improving harness" y "coding harness for general-purpose agents" en Trial [#8]. "Context engineering" estaba en Adopt en abril de 2026 [#8, lista de blips relacionados].
- Anthropic define context engineering como "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference" y lo presenta como sucesor del prompt engineering [#5]. Es una candidata a escuela propia o a subcapítulo de harness: la propongo como parte de la 6.

### 2.7 Otras escuelas vivas (candidatas)
- Context engineering (arriba). Candidata sólida por el Adopt del Radar y por Anthropic.
- Arquitectura sociotécnica / team topologies: solo confirmé que Richards y Ford 2e la incorporan [#42]. No investigué la fuente primaria. Hueco.
- Gobierno por fitness functions (2.2) ya está cubierto.

## 3. Fundamentos/bibliografia-de-arquitectura

| Recurso | Qué leer | En qué fijarse | Confianza |
|---|---|---|---|
| Richards y Ford, *Fundamentals of Software Architecture* 2e (2025) | Foundations; capítulo de características; capítulo "choosing" estilo; técnicas [#42] | Que todo estilo se juzga por características, no por moda; los capítulos nuevos | índice de [#42], sin abrir el libro |
| Ford, Parsons, Kua, *Building Evolutionary Architectures* 2e | Cap. 2 "Fitness Functions" [#48] | Fitness function = específica y automatizable | S |
| Huyen, *Designing ML Systems* (2022) | Caps. 1, 2 y 11 si no sos de ML [#41] | Sistema entero sobre modelo | M |
| Huyen, *AI Engineering* (2025) | Caps. 3-4 (evaluación), 6 (RAG y agentes), 10 (arquitectura) [#40] | "Private leaderboard"; cuándo no hacer finetuning (cap. 7) | resúmenes de capítulo, no el libro |
| Sculley et al. 2015 | Todo, es corto [#39] | Las categorías de deuda técnica de ML | L abstract |
| Ousterhout, *A Philosophy of Software Design* | Módulos profundos y la discusión con Martin [#44] | Interfaz simple sobre implementación rica; métodos diminutos generan "shallow interfaces and entanglement" | L del debate; el libro no |
| Newman, *Building Microservices* 2e / *Monolith to Microservices* | Las charlas citadas [#23]; el libro no lo abrí | "Microservices should not be the default choice" (charla, no libro) | S |
| Kleppmann y Riccomini, *Designing Data-Intensive Applications* 2e | Sale en febrero-marzo de 2026 (O'Reilly lista febrero; The Nile 27 feb; B&N 3 mar; la nota de Kleppmann dice marzo de 2026) [#43, S] | Fecha exacta discrepa entre fuentes; la nota no lista capítulos ni menciona LLM | S |
| Thoughtworks Technology Radar | Vol. 35 (nov 2026), técnicas; entradas individuales con historial de anillos [#8] | El historial de cada blip y que "no revisan blips viejos de forma continua" | L |

Radar: ediciones 30 (abr 2024), 31 (oct 2024, publicada el 23 de octubre [S]), 32 (abr 2025), 33 (nov 2025), 34 (abr 2026), 35 (nov 2026) [#16]. Detalle clave: en el Radar actual el anillo exterior se llama **Caution**; el 35 lo lista así [#8]. Las fuentes del buscador confirman que "Hold" fue renombrado a "Caution" pero ninguna dice en qué volumen; los volúmenes 24 (2021) y 29 (2023) todavía dicen "Hold" [S]. Hueco: edición exacta del cambio.

## 4. Posición contraria

Estructura por tema: **a favor** de dejarlo fuera, **en contra**, **quién lo dice** (tipo de voz).

### a) Entrenar modelos propios desde cero
- A favor de dejarlo fuera: BloombergGPT, 50.000 millones de parámetros, ~363.000 millones de tokens financieros + ~345.000 millones generales (~708.000 millones en total) [#28]. Li et al. (EMNLP Industry 2023): ChatGPT y GPT-4 en zero/few-shot superan al modelo preentrenado de dominio y a modelos finetuneados en muchas tareas; fallan en NER y sentimiento financiero donde hace falta conocimiento de dominio [#29, S]. Un número del buscador (BloombergGPT 0,51 frente a GPT-4 0,86 y 0,97) no tenía columnas etiquetadas: no lo uso.
- En contra: el propio BloombergGPT reportó ganar "por amplios márgenes" en tareas financieras manteniendo desempeño general [#28]; y los resultados de Li et al. muestran que GPT-4 falla en tareas con conocimiento de dominio [#29]. Huyen no dice "nunca": dedica el cap. 7 a cuándo sí y cuándo no hacer finetuning y compara hospedar vs. API en siete ejes (privacidad, linaje de datos, desempeño, funcionalidad, control, costo, etc.) [#40]. Radar nov 2026: modelos de pesos abiertos y lenguaje chico en Trial; "Local coding models" salió de Caution a Assess porque los modelos abiertos maduraron [#8].
- Quién: papers (primaria, con autores de Bloomberg interesados en su propio modelo) frente a estudio externo. Hueco: no busqué evidencia 2025-2026 de preentrenamientos de dominio exitosos.

### b) Prompt engineering como conjunto de trucos
- A favor de dejar los trucos fuera: Anthropic presenta el prompt engineering como "methods for writing and organizing LLM instructions" y a context engineering como su sucesor [#5]. Radar: "Agent instruction bloat" (instrucciones largas, contradictorias, viejas) en Caution [#8].
- En contra: Sclar et al. midieron "performance differences of up to 76 accuracy points" en LLaMA-2-13B por cambios de formato que preservan el significado, y persiste con más tamaño, más ejemplos y tuning de instrucciones [#30]. Schulhoff et al. sistematizaron 58 técnicas de prompting y 33 términos [#31]: hay un cuerpo de técnicas, no solo trucos. Huyen le dedica un capítulo entero [#40].
- Quién: Anthropic (proveedor), dos grupos académicos. Hueco: el Sclar es de 2023 con modelos viejos; no verifiqué si la sensibilidad bajó con modelos de 2026.

### c) Frameworks de agentes pesados vs. llamadas directas
- A favor: Huyen, "Use an agentic framework when direct API calls work" y "Insist on finetuning when prompting works" figuran como errores de "start too complex"; los frameworks "abstract away critical details, making it hard to understand and debug your system" [#1]. Anthropic: "start by using LLM APIs directly: many patterns can be implemented in a few lines of code"; los frameworks "often create extra layers of abstraction that can obscure the underlying prompts"; añadir complejidad "only when it demonstrably improves outcomes" [#2]. Radar nov 2026: "Agent skill cognitive surrender" en Caution: equipos que adoptan "large, community-curated skill libraries or heavyweight AI agent frameworks" sin entenderlos; "generic community skills may become unnecessary" con mejores modelos [#10]. Kapoor et al.: los benchmarks centrados en precisión llevan a agentes "needlessly complex and expensive" [#35]. Cognition (12 jun 2025): compartir contexto y trazas completas, porque "actions carry implicit decisions, and conflicting decisions carry bad results" [#4].
- En contra: Anthropic reporta +90,2% de su sistema multiagente frente a un agente solo [#3], con 15x de tokens; el Radar pone "coding harness for general-purpose agents", "managed agents runtime" y "enterprise harness" en Trial o Assess [#8]. OpenAI muestra un repositorio de ~1 millón de líneas hecho con agentes y un harness elaborado [#7]. Es decir: lo que se critica es el framework opaco, no la orquestación; el harness sí gana peso.
- Quién: **todos son vendedores o autores de práctica**; no hay estudio independiente comparando framework vs. llamada directa. Hueco declarado. Matiz: Anthropic y OpenAI son los que fabrican el modelo y también venden el SDK de agentes.

### d) SOA con ESB
- A favor de dejarla fuera: Lewis y Fowler: "smart endpoints and dumb pipes"; critican "the tendency to hide complexity away in ESB's" y citan "Erroneous Spaghetti Box" (Jim Webber) [#24]. Radar 2020, en Hold: poner orquestación y transformación en una herramienta centralizada "adds architectural coupling, reduces transparency, and increases vendor lock-in"; las ESB se reempaquetan como API gateways [#12]. El buscador también vio una entrada de 2012 de ESB en Hold [S].
- En contra: los mismos autores admiten que "the microservice style is very similar to what some advocates of SOA have been in favor of" y que "others consider microservices to be one form of SOA"; "SOA means too many different things" [#24]. Richards y Ford 2e mantienen "orchestration-driven service-oriented architecture" como estilo en su índice [#42]. Mi lectura del conflicto: lo que cae es la ESB como lugar de la lógica, no el servicio como unidad.
- Quién: Thoughtworks, que tiene una postura histórica; los vendedores de ESB no aparecen. Hueco: no hay defensa reciente de ESB en mis fuentes.

### e) Space-based architecture
- Qué hay: Richards la presenta para escalabilidad: en el informe "Software Architecture Patterns" nombra a event-driven, microservicios y space-based como candidatas si la preocupación es la escalabilidad; el cuello de botella migra de web a aplicación a base de datos [#51, S]. Descripciones secundarias: nodos de procesamiento con grilla de datos en memoria replicada; mala para consistencia fuerte, joins complejos o escrituras intensas; costo de almacenamiento, riesgo de pérdida si falla la sincronización, complejidad operativa subestimada, pruebas de volumen a menudo en producción, dependencia de productos de grilla [#51, S].
- **Hueco principal**: no encontré evidencia de adopción ni un caso ni una crítica primaria independiente. Las fuentes vistas son de Richards, TechTarget y blogs informales. No puedo afirmar que "pierde peso": solo que figura en el índice de Richards y Ford 2e [#42] y que no apareció en el Radar. Si el tema la deja fuera, que se diga "evidencia de uso pública escasa", no "obsoleta".

### f) ML clásico a medida para tareas que un LLM resuelve (contraevidencia)
- A favor de usar el LLM: en pocos datos o few-shot, TabLLM le ganó a LightGBM por amplio margen en un dataset (Credit-g) [#52, S].
- En contra (el ML clásico sigue ganando en tabular): Grinsztajn et al.: los árboles "remain state-of-the-art on medium-sized data" (~10.000 muestras), en 45 datasets, con 20.000 horas de cómputo de búsqueda de hiperparámetros [#25]. Con muchos datos XGBoost ganó en seis de nueve datasets en un estudio few-shot [#52, S]. Gangwani y Bansal (taller, 4 datasets, una T4): árboles igualaron o superaron a los modelos fundacionales tabulares en 3 de 4; los árboles terminan en 0,40 s o menos y ~150 MB, TabICL tardó 960 s y 9 GB de VRAM, TabPFN no procesó las 100.000 filas de Higgs [#27]. Es evidencia chica.
- La contraevidencia a la contraevidencia: TabPFN, Nature 637 (8 ene 2025), supera a los métodos previos en datasets de hasta 10.000 muestras "by a wide margin", con mucho menos tiempo de entrenamiento [#26, S]; el Radar nov 2026 puso "Foundation models for structured data" en Assess [#8]. O sea: la frontera se mueve, pero en tabular mediano y grande los árboles siguen sin ser desplazados por un LLM generalista.
- Costo: "Blanket frontier model usage" en Caution: delegar toda tarea de LLM al modelo más grande es más caro y lento; tareas rutinarias a modelos chicos [#11].
- Hueco declarado: no encontré un estudio que mida el costo de inferencia de un LLM contra el entrenamiento y serving de XGBoost sobre las mismas tareas de clasificación (el buscador lo confirmó) [#52].

### g) Microservicios por defecto
- A favor de dejarlos como default: DHH (4 mayo 2023): microservicios son "perhaps the biggest siren song for needlessly complicating your system"; reemplazar llamadas a método por llamadas de red dentro de la aplicación de un equipo es "madness in almost all cases" [#17]. Prime Video: según InfoQ, el diseño distribuido con Step Functions tenía "a large number of step function state transitions" y muchas lecturas y escrituras a S3 para los ítems intermedios; el equipo llegó al límite de transiciones de la cuenta; "a 90% reduction in operational costs"; Kolny: "distributed approach wasn't bringing a lot of benefits in our specific use case" y "packed all of the components into a single process" [#18]. DHH agrega que el límite llegó cerca del 5% de la carga esperada [#17]. Fowler 2015: no considerarlos "unless you have a system that's too complex to manage as a monolith" [#20]; "you shouldn't start a new project with microservices" [#21]. Newman (QCon 2020, vía InfoQ): "Microservices should not be the default choice"; "not a good choice for most startups" [#23].
- En contra (y matices): (1) El caso Prime Video no es un monolito clásico ni microservicios de equipos: el post original ya no se puede leer (301 a aboutamazon.com) y varios comentaristas, vistos solo vía buscador, discuten la etiqueta ("they were simply refactoring"; es monolito "only at the service level") [S]. Que sea un componente de un servicio y no el sistema entero es el matiz que DHH ignora. (2) Tilkov (9 jun 2015, en martinfowler.com): "starting with a monolith is usually exactly the wrong thing to do" para sistemas que van a ser microservicios; partir el monolito después es muy difícil por acoplamiento (modelos de dominio, persistencia, transacciones compartidas); funciona mejor si el dominio se entiende bien; su beneficio principal es forzar límites para el desarrollo en paralelo [#22]. Fowler mismo dice que monolith-first es "by no means unanimous" [#21]. (3) Escala organizacional: Newman dice que los microservicios sirven en gran escala de equipos; la nota de InfoQ cita solo paráfrasis sobre eso, no una cita directa [#23]. (4) Lewis y Fowler: "not enough time has passed for us to make a full judgement"; "the true consequences of your architectural decisions are only evident several years after" [#24].
- Quién: DHH y Fowler/Newman son voces de práctica; Tilkov, de consultoría (innoQ); no hay estudio empírico. Richards y Ford 2e agregan el monolito modular como estilo [#42].

### h) Patrones GoF como lo primero que se estudia
- A favor de bajarlos: Norvig (presentado en 1996, en línea 1998): 16 de 23 patrones son "invisible or simpler" en Lisp o Dylan [#45 cabecera; cifra vía buscador, S]. Ousterhout prefiere módulos profundos y discute con Martin que la descomposición extrema produce "teeny-tiny methods that suffer from both shallow interfaces and entanglement" y que "the fundamental goal of software design is to make it easy to understand and modify the system" [#44]. (Eso no es una crítica a GoF sino a otra ortodoxia de diseño: lo uso como ejemplo de que la ortodoxia está disputada.)
- En contra: un comentarista (buscador) dice que lo de Norvig "es muy distinto de decir que los patrones son innecesarios" [S]; en los lenguajes mainstream los patrones siguen siendo vocabulario común. No encontré estudio empírico del orden pedagógico. Hueco.
- Quién: Norvig y Ousterhout, autores de renombre; Martin discute con Ousterhout en los puntos de comentarios y TDD [#44].

## 5. Crítica a la mirada de Huyen y del "AI engineering"

1. **"Los evals no alcanzan."** Fodor (2025): los benchmarks se volvieron objetivo y no medida, un problema de ley de Goodhart; "benchmark performance should not be used as a reliable indicator of general LLM cognitive capabilities" [#36, S]. Matiz: eso apunta a benchmarks públicos, no a los evals propios de una app que Huyen y Husain defienden [#40, #37]; no encontré una crítica rigurosa a los evals de aplicación. Hueco. Kapoor et al. (2024): los benchmarks de agentes tienen holdouts débiles o ausentes y generan agentes frágiles que "take shortcuts and overfit" [#35].
2. **LLM-as-judge.** A favor: Zheng et al. (2023): jueces fuertes como GPT-4 alcanzan "over 80% agreement" con preferencias humanas, similar a la que humanos tienen entre sí; sesgos de posición, verbosidad, autopreferencia [#32]. En contra: Radar lo movió de Trial (oct 2024) a Assess (nov 2025): "often fails as a reliable proxy for human judgment"; "less mature than once believed" [#9]. Shankar et al.: *criteria drift*, los criterios dependen de las salidas que se ven [#33]. Husain: seguir la correlación con humanos, medir precisión y recall por separado [#37]. Huyen: "AI judges must be evaluated and iterated over time" [#1]. Norman et al. (jun 2026) dicen que kappa es 33-41 puntos menor que el acuerdo exacto y que el sesgo de verbosidad es chico (<0,011), pero **su versión revisada del 3 nov 2026 fue retirada por arXiv por no cumplir estándares de calidad**: dato no confiable [#34]. Quién: la crítica más fuerte es del propio Radar (anillo Assess) y de académicos; Huyen coincide con la cautela, así que aquí la crítica es interna al campo, no externa.
3. **"El no determinismo se exagera."** He (Thinking Machines, 10 sep 2025): la explicación habitual (concurrencia y no asociatividad de punto flotante) "is incomplete"; la causa principal es que los kernels no son invariantes al tamaño del batch, y la carga del servidor lo hace variar. Qwen3-235B, 1.000 completions a temperatura 0: 80 salidas distintas, divergencia en el token 103; con kernels invariantes, las 1.000 idénticas; costo: 42 s frente a 26 s de vLLM por defecto en Qwen3-8B (1.000 secuencias) [#38]. Es evidencia primaria y fuerte de que parte del no determinismo es evitable, a un costo de rendimiento. No contradice que el comportamiento siga siendo difícil de predecir ante cambios de prompt (#30).
4. **"La arquitectura clásica alcanza."** Anthropic: "find the simplest solution possible"; workflows con caminos de código predefinidos antes que agentes [#2]. Huyen: "Use generative AI when you don't need generative AI" y "the differentiation is product" [#1]. Radar: "Blanket frontier model usage", "AI-driven documentation sprawl" [#8]. Es decir, las voces centrales del propio campo piden menos IA, no más. Mi lectura: la crítica externa más fuerte no existe como tal; está dentro.
5. **Reseñas del libro**: una reseña de 2 estrellas (Ross A. Baker) dice que pierde credibilidad pronto; Goodreads lo llama amplio pero a veces disperso [S, buscador]. Opiniones aisladas, no las uso como evidencia.
6. **Otros pitfalls de Huyen** [#1]: "getting from 0 to 80% took as long as from 80% to 90%"; "staring at data for just 15 minutes usually gives me some insight that could save me hours of headaches"; el aprendizaje de "crowdsourcing use cases" produce "a million text-to-SQL models, a million Slack bots, and a billion code plugins". Son observaciones de práctica sin cuantificación.

## 6. Concepciones erróneas documentadas
- van der Ven y Bosch (2016): de las creencias sobre esfuerzo de documentación, tamaño de equipo y quién decide, solo unas pocas tuvieron respaldo estadístico; "folklore for the tales" [#46]. 39 arquitectos, 54 decisiones: muestra chica y autorreporte.
- Kruchten (2001), vía resumen secundario: arquitectura es más que infraestructura; no es solo la visión de un arquitecto [#47, S]. Lo abriría en el original antes de citarlo.
- Evans: bounded context confundido con subdominio; no todo servicio es un bounded context [#49, S].
- Newman: "monolith" se usa como sinónimo de legacy, pero se refiere a la unidad de despliegue; el peor caso es el monolito distribuido [#23, S].
- Prime Video leído como "microservicios fracasaron": la etiqueta está disputada [#18, S].
- Radar (nov 2026, "Coding throughput as a measure of productivity"): métricas como proporción de código generado por IA o uso de tokens son malos sustitutos de productividad [#8].
- Mejor corpus que no encontré: un catálogo empírico de mitos de arquitectura. Hueco.

## 7. Radar "Hold"/"Caution" como señal de qué pierde peso (ediciones 2024-2026)

Lo que verifiqué, con fecha:
- Nov 2026 (vol. 35), Caution: Agent instruction bloat; Agent skill cognitive surrender; AI-accelerated shadow IT; AI-driven documentation sprawl; Blanket frontier model usage; Coding throughput as a measure of productivity; Human-in-the-loop theater; Meat proxy; Naive context compression; Stacked pull requests [#8].
- Abr 2026 (vol. 34), Caution: Coding agent swarms ("costly and still far from mature"); Codebase cognitive debt (solo vi el nombre en la lista de blips relacionados) [#15, #8].
- Nov 2025 (vol. 33), Hold: Naive API-to-MCP conversion [#14, S]; Complacency with AI-generated code (Hold en oct 2024, abr 2025 y nov 2025) [#13, S]. LLM-as-a-judge pasó de Trial a Assess [#9].
- Histórico: ESBs in API gateway's clothing, Hold, oct 2020 [#12]. Para 2024-2025 (vol. 30-32) no pude leer los PDF; **no puedo afirmar qué más estuvo en Hold**.
- **Ninguna de las cosas que el tema deja fuera (microservicios por defecto, SOA con ESB, space-based, GoF, entrenar desde cero) aparece como Hold en lo que pude verificar para 2024-2026.** Lo único con ring "contra" que toca las ocho es indirecto: frameworks pesados de agentes (#10), modelos más grandes de lo necesario (#11) y el ESB (2020, #12). No uso el Radar como evidencia de que microservicios o GoF "pierden peso": no lo dice.
- El nombre del anillo cambió de "Hold" a "Caution"; en el contenido, el informe usa Caution para 2026 y Hold para lo anterior.

## 8. Recursos canónicos por componente

- **escuelas-de-arquitectura**: Richards y Ford 2e, parte de Estilos y el capítulo de elegir estilo [#42]; fijarse en que cada estilo se juzga por características. Para la escuela 6, Anthropic "Effective harnesses…" [#6]; fijarse en la lista de features en JSON, un feature por sesión y el traspaso por git. Para la 5, el cap. 4 de Huyen [#40] junto con Husain [#37].
- **bibliografia-de-arquitectura**: la tabla de la sección 3; el recurso vivo es el Radar vol. 35, con el historial de anillos de cada blip [#8].
- **posición contraria, (c)**: Anthropic "Building effective agents" [#2] con Huyen "pitfalls" [#1]; fijarse en "demonstrably improves outcomes" y en que ambos son proveedores, no estudios.
- **(g)**: Tilkov [#22] contra Fowler [#21] y Newman [#23]; fijarse en que la disputa es sobre dominio entendido y escala de equipos, no sobre rendimiento.
- **(f)**: Grinsztajn et al. [#25] y TabPFN [#26] en conjunto; fijarse en que ambos son sobre tabular, el segundo con tamaño de datos limitado.
- **(d)**: Lewis y Fowler [#24], sección "smart endpoints and dumb pipes".
- **crítica a LLM-as-judge**: Radar [#9] y Shankar et al. [#33]; no usar [#34].
- **no determinismo**: He [#38].

## 9. Huecos declarados
1. PDF del Radar vol. 30-34 y fichas O'Reilly: no se pudieron abrir (503, 403). Falta el listado completo de Hold de 2024-2025.
2. En qué volumen el Radar renombró Hold a Caution.
3. Post original de Prime Video (redirige): números y cita literal vienen de InfoQ y del buscador.
4. Space-based: sin evidencia independiente de uso ni crítica primaria.
5. Estudio independiente de framework de agentes vs. llamada directa: no existe en lo que encontré.
6. Costo LLM frente a ML clásico en las mismas tareas: sin estudio directo.
7. Evans 2003, Vernon 2013, GoF 1994, Newman (libros), Ousterhout (libro), Ford 2e de Evolutionary Architectures: solo fuentes secundarias o charlas; las fechas de edición no se verificaron.
8. Tabla de contenidos de DDIA 2e y de Designing ML Systems: no obtenida.
9. Crítica rigurosa a los evals de aplicación (no benchmarks públicos): no encontrada.
10. Evidencia empírica del orden pedagógico (GoF primero): no encontrada.
11. Nada sobre la escuela sociotécnica (team topologies) más allá de que Richards y Ford 2e la incluyen.
