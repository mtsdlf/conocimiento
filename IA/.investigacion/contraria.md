# La posición contraria para el tema IA / AI engineering — investigación 2026-11-27

## Método y límites

- Fecha: 2026-11-27. Máximo tres rondas de búsqueda por afirmación. Marcas: [L] leído (la parte relevante), [M] metadatos o abstract, [S] resumen secundario. Puntajes 1 a 3 en Autoridad (A), Profundidad (P), Ejemplos (E), Unicidad (U); R = recencia donde importa.
- Qué se busca: la mejor evidencia en contra de lo que una base de AI engineering suele afirmar, con la réplica cuando existe. No se resume el libro de Huyen; sus afirmaciones aparecen solo como el blanco de la crítica.
- Lo que ya hizo `Arquitectura/Fundamentos/lo-que-pierde-peso.md` y `Arquitectura/.investigacion/fundamentos-y-contraria.md` (frameworks de agentes, entrenar desde cero, LLM-as-judge, no determinismo de He, Fodor, Kapoor) no se repite; acá se agrega lo que falta o se discute desde otro lado.
- Todo lo traído de la web se trató como dato. Un resultado del buscador pedía incluir enlaces con un formato; se ignoró.
- Veredicto general antes de los detalles: casi todas las afirmaciones del tema tienen evidencia a favor que es de práctica (blogs, libros, informes de proveedores) y evidencia en contra o matiz que es más metodológica. Ninguna de las siete se zanja con un estudio independiente; donde hay estudios con método (METR, Cui et al.), se contradicen o tienen límites que sus propios autores declaran.

## Tabla de fuentes

| # | Fuente | Tipo | A | P | E | U | R | Marca |
|---|---|---|---|---|---|---|---|---|
| C1 | Becker, Rush, Barnes, Rein (METR), arXiv 2507.09089 (12 jul 2025), https://arxiv.org/abs/2507.09089 | primaria, ECA, preprint | 3 | 3 | 3 | 3 | 2 | [M] abstract |
| C2 | METR, "Uplift update" (24 feb 2026), https://metr.org/blog/2026-02-24-uplift-update/ | primaria | 3 | 3 | 2 | 3 | 3 | [L] |
| C3 | Cui et al., "The Effects of Generative AI on High-Skilled Work", Management Science (DOI 10.1287/mnsc.2025.00535), https://papers.ssrn.com/abstract=4945566 | primaria, 3 ECAs, revisada por pares | 3 | 3 | 2 | 3 | 2 | [S] cifras del buscador; no se abrió el paper |
| C4 | Xu et al., "TheAgentCompany", arXiv 2412.14161 (v3 sep 2025; NeurIPS 2025), https://arxiv.org/abs/2412.14161 | primaria | 3 | 2 | 2 | 2 | 2 | [S] la cifra de 30 % es del v2 y no se confirmó en el v3 |
| C5 | Challapally et al., MIT NANDA, "The GenAI Divide: State of AI in Business 2025", PDF en https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf | primaria; informe no revisado por pares, "Preliminary Findings", del proyecto NANDA | 1 | 2 | 2 | 3 | 2 | [L] texto extraído del PDF, partes relevantes |
| C6 | 80,000 Hours (Rob Wiblin), análisis del estudio del MIT (grabado 13 feb 2026, publicado 28 abr 2026), https://80000hours.org/podcast/episodes/ai-workplace-mit-study/ | secundaria (crítica) | 2 | 2 | 2 | 3 | 3 | [L] por extractor; es un podcast con transcripción |
| C7 | HPCwire, "MIT report flags 95% GenAI failure rate but critics say it oversimplifies" (4 sep 2025), https://www.hpcwire.com/bigdatawire/2025/09/04/mit-report-flags-95-genai-failure-rate-but-critics-say-it-oversimplifies/ | secundaria | 1 | 1 | 1 | 1 | 2 | [S] vía buscador |
| C8 | Shojaee et al. (Apple), "The Illusion of Thinking", arXiv 2506.06941 (v1 7 jun 2025; v3 20 nov 2025, NeurIPS 2025), https://arxiv.org/abs/2506.06941 | primaria | 3 | 3 | 3 | 3 | 2 | [M] |
| C9 | Lawsen, "Comment on The Illusion of Thinking", arXiv 2506.09250 (10 jun 2025), https://arxiv.org/abs/2506.09250 | primaria, comentario | 2 | 2 | 2 | 3 | 2 | [M] |
| C10 | Dellibarda Varela et al., "Rethinking the Illusion of Thinking", arXiv 2507.01231 (1 jul 2025), https://arxiv.org/abs/2507.01231 | primaria, réplica | 2 | 2 | 2 | 3 | 2 | [M] |
| C11 | Li et al. (Google), "Retrieval Augmented Generation or Long-Context LLMs?", arXiv 2407.16833, EMNLP 2024 Industry, https://arxiv.org/abs/2407.16833 | primaria | 3 | 3 | 2 | 3 | 1 | [M] |
| C12 | Xu et al. (NVIDIA), "Retrieval meets Long Context Large Language Models", arXiv 2310.03025, ICLR 2024, https://arxiv.org/abs/2310.03025 | primaria | 3 | 2 | 2 | 3 | 1 | [S] cifras del buscador |
| C13 | Liu et al., "Lost in the Middle", arXiv 2307.03172 (TACL 2023), https://arxiv.org/abs/2307.03172 | primaria | 3 | 2 | 2 | 3 | 1 | [M] |
| C14 | Chroma, "Context Rot" (14 jul 2025), https://research.trychroma.com/context-rot | primaria; técnica de un proveedor de vector store, sin revisión por pares | 2 | 2 | 2 | 3 | 2 | [S] por buscador |
| C15 | Ovadia et al., "Fine-Tuning or Retrieval?", arXiv 2312.05934 (EMNLP 2024), https://arxiv.org/abs/2312.05934 | primaria | 3 | 2 | 2 | 3 | 1 | [S] |
| C16 | Biderman et al., "LoRA Learns Less and Forgets Less", arXiv 2405.09673 (TMLR 2024), https://arxiv.org/abs/2405.09673 | primaria | 3 | 3 | 2 | 3 | 1 | [S] |
| C17 | Bean et al., "Measuring what Matters: Construct Validity in LLM Benchmarks", arXiv 2511.04703 (3 nov 2025; NeurIPS 2025 D&B), https://arxiv.org/abs/2511.04703 | primaria | 3 | 3 | 2 | 3 | 3 | [M] |
| C18 | van der Maden et al., "Results-Actionability Gap", arXiv 2604.16304 (25 ene 2026), https://arxiv.org/abs/2604.16304 | primaria, 19 entrevistas, preprint | 2 | 2 | 2 | 3 | 3 | [M] |
| C19 | Husain, "Your AI Product Needs Evals" (29 mar 2024), https://hamel.dev/blog/posts/evals/ | secundaria (práctica) | 2 | 2 | 3 | 2 | 2 | [L] por extractor |
| C20 | Huyen, "Common pitfalls when building generative AI applications" (16 ene 2025), https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html | secundaria (práctica) | 2 | 2 | 2 | 2 | 2 | [L] titulares |

---

## 1. "La evaluación va primero; quien itera por intuición fracasa"

**Lo que se afirma.** Husain: "unsuccessful products almost always share a common root cause: a failure to create robust evaluation systems" y "Like software engineering, success with AI hinges on how fast you can iterate" (C19). Huyen suma como error "Forgo human evaluation" (C20) y, en el libro, la ausencia de un pipeline confiable de evaluación como uno de los mayores obstáculos (ver `fundamentos-y-contraria.md`, 2.5).

**Evidencia en contra o matiz.**
- Una búsqueda dirigida no encontró ningún estudio controlado que compare equipos que evalúan primero con equipos que iteran por "vibes". La literatura hallada es cualitativa. La mejor es una entrevista a 19 practicantes (van der Maden et al., enero de 2026): identifican diez prácticas de evaluación, "ranging from informal 'vibe checks' to organizational meta-work", y describen un "results-actionability gap": los equipos juntan datos de evaluación y no logran convertirlos en mejoras concretas. Su interpretación: las prácticas informales "appear to be reasonable adaptations to LLM characteristics, not simply methodological failures" (C18). Es una muestra de 19, sin medir resultados.
- La afirmación de Husain es una causalidad sin datos: es retrospectiva ("almost always"), sin denominador (cuántos productos que fallaron sí evaluaban) y sin grupo de comparación (C19). Sobre su estructura: sus tres niveles (pruebas unitarias, evaluación humana y de modelos, A/B) son de práctica, y él mismo dice que el Nivel 3 "suits more mature products" (C19, por extractor).
- Huyen dice lo contrario del dogma en otra dirección: advierte de "Over-index on early success" y de "Start too complex" (C20): la evaluación pesada antes de saber qué se construye es un riesgo reconocido.

**Réplica a la crítica.** No se halló una réplica empírica. Lo que sí existe es el argumento de fondo: sin una medida no se sabe si un cambio mejora, y la propia C18 propone formalizar lo que los practicantes ya hacen, no abandonarlo.

**Veredicto.** Evaluación-primero es una norma de práctica sin respaldo causal. Se puede enseñar como criterio razonado, no como hecho. Conviene decirlo así en la nota.

**Fuentes independientes.** Husain y Huyen (y Yan y los demás de Applied LLMs) son una comunidad que se cita entre sí; cuentan como una corriente de opinión.

## 2. "Los agentes y la IA para programar aumentan la productividad"

**Lo que se afirma.** En el tema, que agentes y asistentes aceleran el trabajo de programar (afirmación general; los informes de OpenAI y Anthropic sobre sus propios sistemas están en `fundamentos-y-contraria.md`, 2.6, sin replicación independiente).

**Evidencia en contra (con método).** METR, ensayo controlado aleatorizado: 16 desarrolladores con unos cinco años de experiencia en sus proyectos de código abierto, 246 tareas asignadas al azar a permitir o no la IA (principalmente Cursor Pro y Claude 3.5/3.7 Sonnet). Resultado: "Allowing AI increased task completion time by 19%". Los desarrolladores esperaban antes una reducción de 24 %, y después creían haber ahorrado 20 %, aunque el tiempo medido subió. Los expertos en economía predijeron una reducción de 39 % y los de ML una de 38 % (C1). En el segundo estudio, el intervalo del primero es +2 % a +39 % (C2).

**Evidencia a favor.** Cui et al., tres experimentos de campo con GitHub Copilot en Microsoft, Accenture y una empresa Fortune 100: con 4.867 desarrolladores, 26,08 % más tareas completadas (error estándar 10,3 %); el resultado es ruidoso y varía entre experimentos; más ganancia en juniors (27 % a 39 %) que en seniors (8 % a 13 %) (C3) [S]. No contradice a METR: miden otra población (empresas, juniors, tareas por período) y otra variable (tareas completadas, no tiempo por tarea).

**Réplica y actualización de METR (24 feb 2026).** Un segundo estudio con 57 desarrolladores, 143 repositorios y más de 800 tareas dio -18 % de tiempo en los desarrolladores originales (IC -38 % a +9 %) y -4 % en los nuevos (IC -15 % a +9 %); es decir, el signo se invierte pero los intervalos incluyen cero. METR advierte efectos de selección graves: los desarrolladores no quieren trabajar sin IA, lo que "likely biases downwards our estimate of AI-assisted speedup", y entre 30 % y 50 % reportó saltear tareas que no querían hacer sin IA. Su conclusión: cree que los desarrolladores probablemente ganan más velocidad en 2026 que en 2025, pero llama a la evidencia "very weak", dice que el nuevo dato da "an unreliable signal of the current productivity effect" y rediseña el estudio (C2). El pago bajó de $150 a $50 por hora entre estudios (C2).

**Agentes autónomos.** TheAgentCompany (empresa simulada): según el buscador, el agente más competitivo completa 30 % de las tareas en el v2; el v3 no se confirmó (C4) [S]. Lo que dicen los autores, también del buscador: una buena parte de las tareas simples se resuelve, las de horizonte largo todavía no.

**Veredicto.** No se puede afirmar "los agentes mejoran la productividad" ni lo contrario con un estudio con método: el único ensayo controlado de experimentados halló lentitud en 2025 con herramientas de 2025, y su propio autor lo declara histórico y de interpretación difícil en 2026 (C2). Lo robusto es la brecha de percepción: la gente cree ir más rápido de lo que mide (C1). Es la evidencia de método más fuerte de todo el informe y sigue siendo n = 16.

## 3. "RAG supera al contexto largo" o "el contexto largo reemplaza a RAG"

**Lo que se afirma.** Las dos cosas se afirman en la comunidad.

**Evidencia.**
- A favor de RAG en 2023: NVIDIA (Xu et al., ICLR 2024): un modelo de contexto de 4K con recuperación rinde casi igual que uno de 16K extendido por interpolación, con mucho menos cómputo; el mejor, Llama2-70B-32k con recuperación, promedia 43,6 contra 42,8 de GPT-3.5-turbo-16k; con modelos de 43B y 70B (C12) [S, cifras del buscador].
- A favor del contexto largo en 2024: Li et al. (Google, EMNLP 2024 Industry): con recursos suficientes, el contexto largo "consistently outperforms RAG in terms of average performance"; RAG sigue siendo "much cheaper"; el método Self-Route manda la consulta a RAG y, si el modelo dice que no puede responder, al contexto largo, y baja el costo manteniendo un rendimiento comparable (C11) [M]. Las cifras de ahorro (65 % con Gemini-1.5-Pro, 39 % con GPT-4o) salen del buscador y no del abstract [S].
- Matices que desinflan el contexto largo: "Lost in the Middle": el rendimiento cae cuando la información relevante está en el medio de la entrada, incluso en modelos de contexto largo (C13) [M]; Chroma, en un reporte técnico de julio de 2025: con 18 LLM, el rendimiento se degrada al crecer la entrada incluso en una tarea simple (C14) [S].
- Discrepancia entre fuentes: C12 (2023, modelos más débiles) y C11 (2024, modelos más fuertes) llegan a conclusiones distintas. Los autores de C11 atribuyen la diferencia a modelos más fuertes y contextos más largos [S, vía buscador]. No es un conflicto: es una medida que cambia con el modelo.

**Veredicto.** No hay ganador general; la respuesta depende del modelo, el largo del contexto y el costo. Para la nota: afirmar "depende" con las dos fuentes y la fecha, no una regla. Hueco: no hay comparación posterior a 2024 con modelos actuales ni con precios actuales.

**Sesgo de la fuente.** C14 es de una empresa que vende un vector store (interés en que RAG pese); C11 es de Google, que vende contexto largo (Gemini). Cada lado tiene su interés.

## 4. "El finetuning ya no hace falta"

**Lo que se afirma.** Que, con modelos fuertes, prompting y RAG alcanzan. Huyen critica insistir en el finetuning "when prompting works" (ver `lo-que-pierde-peso.md`).

**Evidencia en contra de que no haga falta, y a favor del cambio.**
- Ovadia et al. (EMNLP 2024): para inyectar conocimiento, el finetuning no supervisado mejora algo, pero RAG "consistently outperforms it" tanto en conocimiento ya visto como en conocimiento nuevo, y los LLM "struggle to learn new factual information" por finetuning no supervisado, salvo exponiéndolos a muchas variaciones del mismo hecho (C15) [S]. Es evidencia a favor de no ajustar para meter hechos.
- Biderman et al. (TMLR 2024): LoRA "substantially underperforms" el finetuning completo en programación y matemática en configuraciones estándar, pero conserva mejor el rendimiento fuera del dominio; el finetuning completo aprende cambios de un rango 10 a 100 veces mayor (C16) [S]. Es decir: el finetuning sirve para comportamiento y dominio, y la versión barata (LoRA) aprende menos.
- Los dos estudios son de 2023 y 2024 con modelos de esa época; el estado de los proveedores hoy está en `plataformas-de-ia.md`.

**Veredicto.** "Ya no hace falta" es una simplificación. Lo sostenido por estudios es más acotado: para conocimiento nuevo, RAG gana; para comportamiento y estilo, el finetuning completo aprende más que LoRA a cambio de olvidar más. No se halló un estudio reciente que compare finetuning contra modelos de punta con prompting en una tarea de dominio con costos: hueco.

## 5. "Los benchmarks miden algo"

**Evidencia en contra.** Bean et al. (NeurIPS 2025 Datasets and Benchmarks): 29 revisores expertos analizaron 445 benchmarks de congresos de PLN y ML; encontraron patrones en los fenómenos medidos, las tareas y las métricas que "weaken the validity of the resulting claims", y dan ocho recomendaciones. "Reliably measuring abstract and complex phenomena such as 'safety' and 'robustness' requires strong construct validity" (C17) [M]. El buscador agrega que menos de 10 % de los benchmarks usaban tareas reales completas; no está en el abstract [S]. Complementos ya en la base: Fodor y Kapoor et al. (ver `fundamentos-y-contraria.md`, sección 5).

**Réplica.** No es una réplica sino un límite del argumento: Huyen y Husain no defienden benchmarks públicos como medida final, sino un "private leaderboard" propio y evaluaciones de aplicación (ver `fundamentos-y-contraria.md`, 2.5). La crítica de validez de constructo se aplica a los benchmarks públicos; las evaluaciones propias quedan sin crítica rigurosa encontrada (hueco ya declarado en esa investigación).

**Veredicto.** Los benchmarks miden algo, pero menos que lo que sus nombres dicen. Es un resultado de una revisión sistemática con 42 autores y es fuerte para lo que cubre.

## 6. "Los modelos razonan" (Apple y sus réplicas)

**Lo que se afirma en contra.** Shojaee et al. (Apple, NeurIPS 2025): con puzzles de complejidad controlable, los modelos de razonamiento muestran un "complete accuracy collapse beyond certain complexities", reducen el esfuerzo de razonamiento al subir la complejidad aunque les quede presupuesto de tokens, y hay tres regímenes: en baja complejidad los modelos estándar superan a los de razonamiento, en media ganan los de razonamiento y en alta ambos colapsan (C8) [M].

**Réplica 1.** Lawsen (10 jun 2025): los resultados "mostly reflect flawed experiments": en la Torre de Hanoi las salidas exceden el límite de tokens y los modelos lo reconocen; el corrector automático no distingue errores de razonamiento de restricciones prácticas; y las instancias de River Crossing con N > 5 son imposibles dada la capacidad del bote, pero se puntuaron como fallas. Pidiendo una función generadora en vez de la lista de movimientos, la precisión en Hanoi es alta; los experimentos son preliminares (C9) [M]. La versión más reciente de C9 dice que quitó a Claude como coautor, por política de arXiv; la atribución a "Opus" no se pudo confirmar en la página.

**Réplica 2.** Dellibarda Varela et al. (1 jul 2025): confirman parte de cada lado. En Hanoi los modelos "stumble when complexity rises moderately (around 8 disks)", así que las fallas no son solo de límite de salida; en River Crossing, con solo configuraciones resolubles, los modelos manejan "instances with over 100 agent pairs" (C10) [M]. Su conclusión: los modelos son "stochastic, RL-tuned searchers in a discrete state space we barely understand".

**Estado.** No hay consenso en lo que se encontró; un blog de opinión defiende que la réplica de Lawsen es débil (https://msukhareva.substack.com/p/on-illusion-of-thinking-do-llms-reason) [S]. No se halló trabajo posterior a 2025 con una segunda ronda.

**Veredicto.** Parte del "colapso" fue un defecto de diseño del experimento (puzzles irresolubles, límites de salida), según dos fuentes independientes (C9, C10); parte persiste (límite en Hanoi cerca de 8 discos, C10). "Razonan" y "no razonan" son ambos demasiado fuertes para sostener con estas pruebas. Para la nota: dato, réplica y qué sigue abierto.

## 7. Tasas de fracaso de proyectos de IA (MIT NANDA, "95 %")

**Lo que dice el informe (primaria).** "95% of organizations are getting zero return" y "Just 5% of integrated AI pilots are extracting millions in value" (C5). Es un informe "Preliminary Findings", periodo enero a junio de 2025, con una "systematic review of over 300 publicly disclosed AI initiatives, structured interviews with representatives from 52 organizations, and survey responses from 153 senior leaders collected across four major industry conferences" (C5). El éxito se define como un impacto "marked and sustained productivity and/or P&L impact", medido seis meses después del piloto (C5). Sus propias limitaciones, textuales: las cifras son "directionally accurate based on individual interviews rather than official company reporting", los tamaños de muestra "vary by category", y la ventana de seis meses puede ser "insufficient to fully assess 'successful deployment'... potentially understating success rates" (C5, sección 8.2).

**Críticas al método (secundarias, concordantes entre sí y con el texto del informe).**
- El número de la muestra: la prensa dijo "150 interviews with leaders and a survey of 350 employees" (Fortune, según C6); el informe dice 52 entrevistas y 153 encuestados (C5). Con tan pocas organizaciones, la cifra del 5 % podría estar errada por un factor de unas tres veces en cualquier dirección (C6).
- Qué cuenta como fracaso: del total de organizaciones, alrededor de 60 % investigó herramientas empresariales a medida, 20 % hizo un piloto y 5 % llegó a producción; el 95 % cuenta como falla a quien no llegó (C6, y consistente con el exhibit del informe, C5). Entre las que pilotearon, según C6, alrededor de un cuarto tuvo éxito. Cabe mirar con cuidado: la cifra de "un cuarto" es una cuenta del crítico.
- La definición de éxito pide un efecto "marked and sustained" que el informe no define y proyectos que empatan o van a ser rentables después cuentan como fracasos (C6).
- No fue revisado por pares y el informe completo no estaba disponible cuando se volvió viral: el enlace pedía un formulario (C6); en 2026 el PDF se pudo bajar de un alojamiento de terceros.
- Conflicto de interés: los autores desarrollan los marcos de IA agéntica que el informe recomienda y nombra a NANDA como solución, sin declarar el conflicto (C6). Una afirmación del mismo tipo hay en C7 [S].
- Modelos de 2024 en los proyectos, lo que según C6 podría hacer los resultados más favorables, no menos, para las herramientas actuales (C6).

**Réplica y corroboración.** El informe y la crítica coinciden en los números base; discrepan en qué significan. Corroboración débil, citada por un artículo secundario: Capgemini habría hallado que 88 % de los pilotos de IA no llegaba a producción en 2023 (C7) [S, no verificado]. No se halló otro estudio con muestra grande y método transparente sobre tasas de fracaso de IA en empresas: hueco.

**Veredicto.** "El 95 % fracasa" no se sostiene como lectura del informe; sí se sostiene "casi ningún piloto de herramientas a medida llegó a impacto sostenido en seis meses, según 52 entrevistas". Para la nota, citar el número con su definición y su muestra, nunca "95 % de los proyectos de IA fracasan".

## 8. Concepciones erróneas y sesgos del propio campo (documentadas)

1. **"La gente que usa IA sabe cuánto ayuda".** METR: esperaban -24 % de tiempo y creyeron haber logrado -20 %, y midieron +19 % (C1). Brecha de percepción, con n = 16.
2. **"Los expertos predicen bien la productividad".** Economistas (-39 %) y expertos en ML (-38 %) predijeron una reducción grande (C1).
3. **"Una cifra de un informe es un hecho".** El caso NANDA (sección 7): la cifra circuló sin muestra ni método a la vista.
4. **"Un colapso en un puzzle es un colapso del razonamiento".** Puzzles irresolubles y límites de salida (sección 6).
5. **"Las voces centrales del campo se confirman entre sí".** Huyen, Husain, Yan y Applied LLMs son una misma comunidad que se cita (ver `fundamentos-y-contraria.md` sección 5 y la sección 1 de este informe). Un tema construido con ellos hereda su sesgo: pro-evaluación y pro-aplicación. Se declara.
6. **Proveedores como fuente.** Los informes de OpenAI y Anthropic sobre sus propios sistemas (ver `fundamentos-y-contraria.md`) y los estudios de Chroma y Google en la sección 3 vienen de quien vende. Declarado.

## 9. Recurso canónico por afirmación

| Afirmación | Recurso | Parte y en qué fijarse |
|---|---|---|
| Evaluación primero | C18 con C19 | C18: las diez prácticas y el "results-actionability gap"; C19: los tres niveles y que no hay datos de comparación |
| Productividad | C1 con C2 | C1: la brecha entre -24 %, -20 % y +19 %; C2: los efectos de selección y el "very weak" |
| RAG o contexto largo | C11 con C12 | Fecha y modelo de cada uno; Self-Route como compromiso |
| Finetuning | C15 con C16 | Para qué sirve cada uno: conocimiento nuevo contra comportamiento |
| Benchmarks | C17 | Las ocho recomendaciones y el checklist |
| Razonamiento | C8, C9 y C10 juntos | Qué instancias eran irresolubles y qué sigue fallando cerca de 8 discos |
| Fracaso de proyectos | C5 sección 8.2 y C6 | Definición de éxito, tamaño de muestra, sus limitaciones propias |

## Huecos

1. **Evals primero contra vibes:** no hay estudio controlado; solo C18 (19 entrevistas). Hueco de fondo, no de búsqueda.
2. **Cui et al. (C3):** las cifras vienen del buscador, no se abrió el paper ni se verificó el 26,08 %.
3. **TheAgentCompany (C4):** el 30 % es del v2 y no se confirmó en el v3 (septiembre de 2025).
4. **Otros ensayos controlados de productividad con agentes** (2026): no se buscaron más allá de METR y Cui; podría haber estudios posteriores.
5. **RAG contra contexto largo:** nada posterior a 2024 con modelos y precios actuales; las cifras de ahorro de Self-Route son del buscador. C12 y C14 vistos solo por buscador.
6. **Finetuning:** no se leyó C15 ni C16 más allá del buscador; no hay estudio reciente con modelos de punta y costos.
7. **Benchmarks:** la cifra "menos de 10 %" no está en el abstract y no se verificó en el paper (C17).
8. **Razonamiento:** no se encontró trabajo de 2026; no se leyeron los PDF completos de C8, C9 y C10; la atribución a "Opus" en C9 no se pudo confirmar.
9. **NANDA:** el informe se leyó por texto extraído del PDF alojado por un tercero (mlq.ai), no desde el sitio de NANDA; no se encontró una respuesta oficial de los autores a las críticas; la crítica de C6 es un podcast, no un estudio; C7 y la cifra de Capgemini son [S]. No hay una segunda fuente primaria sobre tasas de fracaso con muestra grande.
10. **Predicción de empleo de Swyx (2023):** sin datos posteriores sobre el ratio de empleos de AI engineer y ML engineer.
11. **No se investigaron** las afirmaciones del tema sobre seguridad como mito (ver `produccion-y-fundamentos.md`, parte A1) ni sobre el costo de los modelos de razonamiento.
