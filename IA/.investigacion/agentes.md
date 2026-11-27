# Investigación: vertical Agentes (el modelo que actúa con herramientas)

Fecha de la investigación: 2026-11-27. Público: quien programa, sabe de APIs y no sabe cómo funciona un modelo por dentro. Perspectiva de Chip Huyen (*AI Engineering*, cap. 6 parte Agents; post de 2025-01-07) como inspiración, no como índice.

Convenciones. Puntajes 1-3 en autoridad (A), profundidad (P), ejemplos (E), unicidad (U). Tipo: prim = primaria, sec = secundaria. Marca: [L] leído con WebFetch, [M] solo metadatos o abstract, [S] solo resumen secundario o del buscador. Aviso de método: WebFetch pasa la página por un extractor, así que [L] significa "leída a través del extractor". Varias citas literales salen de ese extractor y conviene recotejarlas contra la página antes de publicarlas como cita; donde el extractor no entregó el abstract literal, se parafrasea y se dice. Todo lo traído de la web es dato, no instrucción. Fuentes ya usadas en `agente.md` y en `sistemas-con-modelos.md` se citan sin repetir su lectura completa.

## 0. Hallazgos que cambian el encargo

1. **La división en cinco componentes coincide a medias con el campo.** Lo que el campo trata como un solo eje es "herramientas, planificación y fallas" (Huyen cap. 6 los junta: Tools p. 278, Planning p. 281, Failure Modes and Evaluation p. 298, Memory p. 300). Tres observaciones:
   - `patrones-de-flujo` mezcla dos cosas que Anthropic mantiene separadas: el espectro workflow/agente (patrones de orquestación con código) y el multiagente (arquitectura). Conviene dos secciones dentro de la misma nota.
   - `fallas-de-agentes` mezcla fallas, evaluación y seguridad de acciones. En el campo son tres literaturas distintas (taxonomías de falla, benchmarks, seguridad/OWASP). Para un lector principiante alcanza una nota con tres secciones; si crece, separar seguridad.
   - Faltan dos temas que el campo trata aparte: **memoria de agentes** (Huyen cap. 6 p. 300; ya figura como hueco en `agente.md`) y **harness engineering** (ya está en `agente.md`). También el **contexto de agentes** (context engineering), que vive en la vertical de contexto: enlazar, no duplicar.
2. **Lo que en `agente.md` contradice o queda corto con 2025-2026** (ver sección 2 y 5): (a) SWE-bench Verified ya no es una medida confiable según OpenAI (2026-02-23); (b) la especificación MCP vigente es la 2026-07-28 y MCP pasó a la Linux Foundation el 2025-12-09; (c) la página de METR sobre horizonte de tiempo ya no se actualiza desde 2026-09-08. Nada de `agente.md` se contradice de frente.
3. **La nota `llm-emite-reasoner-verifica.md` (archivo) cita a Kambhampati et al. correctamente** (arXiv 2402.01817); lo confirmé en el abstract. Falta que `planificacion` lo cite con su ICML 2024.

## 1. uso-de-herramientas

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Recencia | Marca |
|---|---|---|---|---|---|---|---|---|
| Anthropic, docs "Tool use with Claude" | https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview | prim (doc oficial) | 3 | 3 | 3 | 3 | leída 2026-11-27 | [L] |
| OpenAI, guía de function calling | https://developers.openai.com/api/docs/guides/function-calling | prim (doc oficial) | 3 | 2 | 2 | 2 | leída 2026-11-27 | [L] |
| Anthropic, "Writing effective tools for agents" (Aizawa, 2025-09-11) | https://www.anthropic.com/engineering/writing-tools-for-agents | prim (lab) | 3 | 3 | 3 | 3 | 2025-09 | [L] |
| Anthropic, "Building effective agents" (2024-12-19), sección de herramientas (ACI) | https://www.anthropic.com/engineering/building-effective-agents | prim (lab) | 3 | 2 | 2 | 3 | 2024-12 | [L] |
| Especificación MCP 2026-07-28 | https://modelcontextprotocol.io/specification/latest | prim | 3 | 3 | 1 | 3 | 2026-07 | [L] |
| Anthropic, "Donating the Model Context Protocol..." (2025-12-09) | https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation | prim (lab, con interés) | 2 | 1 | 1 | 2 | 2025-12 | [L] |
| Anthropic, anuncio de MCP (2024-11-25) | https://www.anthropic.com/news/model-context-protocol | prim | 3 | 1 | 1 | 3 | 2024-11 | [L] (en `agente.md`) |
| Linux Foundation, comunicado de la Agentic AI Foundation | https://linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation | prim | 3 | 1 | 1 | 2 | 2025-12 | [S] (solo apareció en el buscador) |
| Willison, "The lethal trifecta for AI agents" (2025-06-16) | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | sec (practicante reconocido) | 2 | 2 | 2 | 3 | 2025-06 | [L] |
| OWASP, LLM06:2025 Excessive Agency | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | prim (marco de seguridad) | 3 | 2 | 2 | 3 | 2025 | [L] |

### Afirmaciones

- Qué es el uso de herramientas: "Tool use (also called function calling) lets Claude call functions that you define or that Anthropic provides." El modelo devuelve una llamada estructurada que ejecuta tu aplicación (client tools) o Anthropic (server tools). https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- Mecánica en Anthropic: se pasa una herramienta con `name`, `description` e `input_schema`; el modelo responde con `stop_reason: "tool_use"` y bloques `tool_use`; tu código ejecuta y devuelve un `tool_result`. Mismo URL. El modelo no ejecuta nada: solo emite la llamada. Esto es lo que un programador necesita entender primero.
- Mecánica en OpenAI: cada función se declara en `tools` con `type`, `name`, `description`, `parameters` (esquema JSON) y `strict`; el flujo es de cinco pasos con `function_call`, `call_id` y `function_call_output`. `tool_choice` admite `auto`, `required`, función forzada, `allowed_tools` y `none`. https://developers.openai.com/api/docs/guides/function-calling
- Modo estricto: Anthropic: "Add `strict: true` to your custom tool definitions to ensure Claude's tool calls always match your schema exactly." OpenAI exige `additionalProperties: false` y todas las propiedades en `required`. En OpenAI Chat Completions el valor por defecto es no estricto. Mismos URL.
- Cantidad de herramientas: OpenAI sugiere "Aim for fewer than 20 functions available at the start of a turn" (orientativa); con muchas, usar tool search. Anthropic ofrece `tool_search` como herramienta de servidor "to work with thousands of tools". Mismos URL. Número de OpenAI: de la guía actual, puede cambiar.
- Los modelos pueden inventar argumentos faltantes: la doc de Anthropic dice que ante un parámetro requerido ausente, "Claude Sonnet might ask... But it might also infer a reasonable value", y que no está garantizado. Mismo URL de Anthropic.
- Costo oculto: los tokens de `tools` (nombres, descripciones y esquemas) se cobran como entrada, más un system prompt de uso de herramientas de 286 a 675 tokens según el modelo (tabla de la doc). Mismo URL.
- Diseño de herramientas (Anthropic, 2025-09-11): "Tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents." Principios: elegir pocas herramientas de alto impacto, "More tools don't always lead to better outcomes", y no envolver cada endpoint de API; usar namespacing; devolver contexto significativo (nombres legibles antes que identificadores) con un `response_format` conciso o detallado; eficiencia de tokens con paginación, filtrado y truncamiento (Claude Code limita las respuestas de herramientas a 25.000 tokens por defecto); errores accionables; descripciones escritas como prompt ("`user_id` en lugar de `user`"). https://www.anthropic.com/engineering/writing-tools-for-agents
- ACI y poka-yoke (Anthropic, 2024-12): las definiciones de herramientas merecen tanta ingeniería de prompts como los prompts principales; en SWE-bench, exigir rutas absolutas eliminó los errores con rutas relativas. https://www.anthropic.com/engineering/building-effective-agents (la nota editorial de la página advierte que parte del tooling descrito cambió desde 2024-12).
- Huyen clasifica las herramientas en tres tipos (conocimiento, capacidad, acciones de escritura): ya en `agente.md`. https://huyenchip.com/2025/01/07/agents.html
- MCP, origen: anunciado 2024-11-25 por Anthropic. https://www.anthropic.com/news/model-context-protocol
- MCP, gobierno y adopción: el 2025-12-09 Anthropic donó MCP a la Agentic AI Foundation, un fondo dirigido de la Linux Foundation cofundado por Anthropic, Block y OpenAI. Cifras de Anthropic (parte interesada): "Más de 10.000 servidores MCP públicos activos" y más de 97 millones de descargas mensuales de los SDK de Python y TypeScript; clientes como ChatGPT, Cursor, Gemini, Microsoft Copilot y VS Code. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation . El buscador atribuye "más de 10.000" también a la Linux Foundation (https://linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation [S]); es la misma cifra, no una fuente independiente. Hubo críticas en Hacker News sobre si un protocolo de un año estaba maduro para una fundación (vía buscador [S], sin enlace verificado).
- MCP, especificación vigente al 2026-11-27: versión 2026-07-28. JSON-RPC 2.0; hosts, clientes y servidores; el servidor ofrece resources, prompts y tools; el cliente ofrece elicitation; "Stateless, self-contained requests" y "Per-request capability negotiation"; extensiones opcionales Tasks, Skills over MCP y MCP Apps. https://modelcontextprotocol.io/specification/latest . Esto actualiza la descripción de `agente.md`, que ya cita la versión pero no el cambio a peticiones sin estado ni la fecha de la donación.
- MCP, seguridad en la especificación: "Tools represent arbitrary code execution and must be treated with appropriate caution"; las descripciones de herramientas "should be considered untrusted, unless obtained from a trusted server"; "Hosts must obtain explicit user consent before invoking any tool". También: "While MCP itself cannot enforce these security principles at the protocol level". Mismo URL.
- Riesgo central, la "trifecta letal" (Willison, 2025-06-16): acceso a datos privados, exposición a contenido no confiable y capacidad de comunicarse hacia afuera; si un agente junta las tres, un atacante puede inducirlo a mandarle los datos. Sobre MCP: "it encourages users to mix and match tools from different sources". https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ . Es la tesis de un practicante, no un estudio; el buscador menciona textos posteriores suyos ("Agents Rule of Two", "The Attacker Moves Second", "Lockdown Mode") que no abrí [S].
- OWASP LLM06:2025 Excessive Agency: causas raíz "funcionalidad excesiva, permisos excesivos y autonomía excesiva"; mitigaciones: mínimo privilegio, "Utilise human-in-the-loop control to require a human to approve high-impact actions before they are taken", y "Implement authorization in downstream systems rather than relying on an LLM to decide if an action is allowed or not." https://genai.owasp.org/llmrisk/llm062025-excessive-agency/

### Recurso canónico

Para el mecanismo: la doc "Tool use with Claude" (round trip completo con `tool_use` y `tool_result`; sirve aunque el lector use otro proveedor porque la forma es la misma que en OpenAI). Para el diseño: Anthropic, "Writing effective tools for agents" completo. Para MCP: la página de la especificación (resumen y sección de seguridad), no el anuncio. En qué fijarse: que el modelo solo emite la llamada y la aplicación ejecuta; que las descripciones de herramientas cuentan como prompt y como superficie de ataque; que menos herramientas mejores gana a un wrapper de cada endpoint.

### Huecos

- No se leyó el historial de versiones de la especificación de MCP (2025-03-26, 2025-06-18, 2025-11-25); solo la vigente. No verifiqué cuándo se introdujo cada cambio (autorización OAuth, elicitation, peticiones sin estado).
- Sin estudio independiente que mida adopción de MCP más allá de las cifras de Anthropic y la Linux Foundation (son la misma cifra).
- Sin estudio con método sobre incidentes reales de seguridad en servidores MCP (envenenamiento de herramientas): no se investigó en las tres rondas.
- La guía de OpenAI de function calling se leyó vía extractor sin ver el código; de Google (Gemini function calling) no se leyó nada: hueco.
- No se leyó el capítulo de Huyen sobre herramientas (cap. 6 p. 278).

## 2. patrones-de-flujo

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Recencia | Marca |
|---|---|---|---|---|---|---|---|---|
| Anthropic, "Building effective agents" (Erik S. y Barry Zhang, 2024-12-19) | https://www.anthropic.com/engineering/building-effective-agents | prim (lab) | 3 | 2 | 2 | 3 | 2024-12 | [L] |
| Yao et al., ReAct (arXiv 2210.03629, v1 2022-10-06, ICLR 2023) | https://arxiv.org/abs/2210.03629 | prim (paper) | 3 | 3 | 2 | 3 | 2022 | [M] |
| Anthropic, "How we built our multi-agent research system" (2025-06-13) | https://www.anthropic.com/engineering/multi-agent-research-system | prim (lab, con interés) | 3 | 3 | 3 | 3 | 2025-06 | [L] |
| Cognition, "Don't Build Multi-Agents" (Walden Yan, 2025-06-12) | https://cognition.com/blog/dont-build-multi-agents | prim (empresa, con interés) | 2 | 2 | 2 | 3 | 2025-06 | [L] |
| Huyen, "Agents" (2025-01-07) | https://huyenchip.com/2025/01/07/agents.html | prim | 3 | 3 | 2 | 3 | 2025-01 | [L] |
| Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (arXiv 2503.13657) | https://arxiv.org/abs/2503.13657 | prim (preprint, sin revisión por pares en la página) | 2 | 3 | 2 | 3 | v3 2025-10-26 | [M] |

### Afirmaciones

- Definiciones: un workflow es "systems where LLMs and tools are orchestrated through predefined code paths"; un agente, "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks". Consejo: la solución más simple posible; muchas veces basta con optimizar una sola llamada. https://www.anthropic.com/engineering/building-effective-agents
- Los cinco patrones y cuándo usarlos (misma fuente): prompt chaining, cuando la tarea se descompone limpio en pasos fijos; routing, cuando hay categorías distintas (incluye mandar preguntas simples a modelos más baratos); parallelization en dos variantes, sectioning y voting; orchestrator-workers, cuando las subtareas no se pueden predecir (ejemplo: cambios en varios archivos); evaluator-optimizer, cuando hay criterio de evaluación claro y mejora medible por iteración. Los agentes "suelen intercambiar latencia y costo por mejor rendimiento" y piden sandbox (parafraseado por el extractor, recotejar).
- Los patrones son una taxonomía de un solo laboratorio, no un estándar del campo. Huyen, por ejemplo, no los usa y organiza el capítulo por herramientas, planificación y fallas. Dato de contraste, no discrepancia sobre hechos. https://huyenchip.com/2025/01/07/agents.html
- ReAct: intercala trazas de razonamiento y acciones; en ALFWorld y WebShop supera a imitación y RL por 34% y 10% de éxito absoluto con uno o dos ejemplos en contexto. https://arxiv.org/abs/2210.03629 . Huyen: "interleaving reasoning and action has become a common pattern for agents". https://huyenchip.com/2025/01/07/agents.html
- Multiagente a favor (Anthropic, 2025-06-13): un sistema con Claude Opus 4 como agente principal y subagentes Claude Sonnet 4 superó en 90,2% a un Claude Opus 4 individual en su evaluación interna de investigación; usa unas 15 veces más tokens que un chat ("multi-agent systems use about 15× more tokens than chats", contra unas 4 veces de un agente normal); en BrowseComp el uso de tokens explicó el 80% de la varianza. https://www.anthropic.com/engineering/multi-agent-research-system . Observación mía: si los tokens explican el rendimiento, parte de la mejora es más cómputo y no mejor arquitectura.
- Cuándo no conviene (misma fuente): poca paralelización real, como muchas tareas de código; tareas de valor bajo frente al gasto; dominios donde todos los agentes comparten el mismo contexto o hay muchas dependencias; coordinación o delegación en tiempo real, que los LLM todavía no hacen bien.
- Multiagente en contra (Cognition, 2025-06-12): "Share context, and share full agent traces, not just individual messages"; "Actions carry implicit decisions, and conflicting decisions carry bad results"; recomienda por defecto un agente lineal de un solo hilo y, para tareas largas, un modelo que comprima el historial en decisiones y eventos clave. https://cognition.com/blog/dont-build-multi-agents
- Las dos posturas no se contradicen de frente: Anthropic recomienda multiagente para investigación en paralelo (lecturas), Cognition lo descarta para escribir código con decisiones que chocan (escrituras). Las dos son de empresas que venden productos, sin estudio independiente que las arbitre. Se presentan las dos.
- Evidencia independiente sobre multiagente: Cemri et al. (UC Berkeley y otros) señalan que los sistemas multiagente suelen mejorar poco frente a un agente solo en benchmarks populares (parafraseado desde el abstract por el extractor; recotejar). https://arxiv.org/abs/2503.13657 (detalle de su taxonomía en la sección 5).

### Recurso canónico

Anthropic, "Building effective agents": leer la definición workflow vs agente y los cinco patrones; fijarse en el criterio "empezar simple" y en los ejemplos de cuándo cada patrón no hace falta. Complemento obligatorio y en tensión: leer juntos el post de Anthropic sobre multiagente y el de Cognition, y anotar en qué difiere la tarea (leer en paralelo vs escribir código coherente).

### Huecos

- El contenido del capítulo de Huyen sobre patrones (cap. 10 p. 463) no se leyó.
- Sin estudio revisado por pares sobre cuándo un workflow supera a un agente; solo posturas de laboratorios y un preprint.
- ReAct se leyó solo por abstract: no verifiqué el diseño experimental.
- No se investigó el estado actual de los SDK de agentes (OpenAI Agents SDK, Claude Agent SDK, etc.); está como hueco en `sistemas-con-modelos.md`.

## 3. planificacion

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Recencia | Marca |
|---|---|---|---|---|---|---|---|---|
| Huyen, "Agents" (2025-01-07), secciones Planning y Reflection | https://huyenchip.com/2025/01/07/agents.html | prim | 3 | 3 | 2 | 3 | 2025-01 | [L] |
| Shinn et al., Reflexion (arXiv 2303.11366, 2023-03-20, v4 2023-10-10) | https://arxiv.org/abs/2303.11366 | prim (paper) | 3 | 3 | 2 | 3 | 2023 | [M] |
| Kambhampati et al., "LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks" (arXiv 2402.01817, ICML 2024) | https://arxiv.org/abs/2402.01817 | prim (paper, revisado) | 3 | 3 | 2 | 3 | 2024 | [M] |
| Kwa et al., METR, "Measuring AI Ability to Complete Long Software Tasks" (arXiv 2503.14499, v1 2025-03-18, v4 2026-07-10) | https://arxiv.org/abs/2503.14499 | prim (METR, org. de evaluación; NeurIPS 2025 según la página) | 3 | 3 | 2 | 3 | v4 2026-07 | [M] |
| METR, página "time horizons" | https://metr.org/time-horizons/ | prim | 3 | 2 | 1 | 3 | última actualización 2026-09-08 (ya no se actualiza) | [L] |
| Jimenez et al., SWE-bench (arXiv 2310.06770, ICLR 2024) | https://arxiv.org/abs/2310.06770 | prim (paper) | 3 | 3 | 2 | 3 | 2023 | [M] |
| OpenAI, "Why we no longer evaluate SWE-bench Verified" (2026-02-23) | https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ | prim (lab, con interés) | 2 | 2 | 1 | 3 | 2026-02 | [S] (solo resumen del buscador) |
| Anthropic, "Effective harnesses for long-running agents" (2025-11-26) | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | prim (lab) | 3 | 2 | 3 | 2 | 2025-11 | [L] (en `sistemas-con-modelos.md`) |

### Afirmaciones

- Planificar es búsqueda: "Planning, at its core, is a search problem" (cita ya en `agente.md`). Huyen recomienda separar planificación de ejecución: generar el plan, validarlo con heurísticas o con un juez de IA y recién después ejecutarlo; los planes tienen granularidad (detallado difícil de generar y fácil de ejecutar, de alto nivel al revés) y pueden ser jerárquicos, paralelos, condicionales o con bucles. https://huyenchip.com/2025/01/07/agents.html
- Reflexión: puede hacerla el mismo agente por autocrítica o un componente separado que evalúa; "mejora el rendimiento, pero aumenta la latencia y el costo por los tokens adicionales". Mismo URL (parafraseado por el extractor).
- Reflexion (Shinn et al., 2023): mejora a un agente sin actualizar pesos, con retroalimentación verbal guardada en memoria episódica entre intentos; reporta "91% pass@1 accuracy on the HumanEval coding benchmark" frente a 80% de GPT-4. https://arxiv.org/abs/2303.11366 . Es autorreporte de los autores, en un benchmark de código hoy saturado.
- Límites de planificación de los LLM: Huyen cita a LeCun (los LLM autorregresivos no pueden planificar) y deja abierto si el problema es el modelo o cómo se usa; un modelo autorregresivo "puede corregir su trayectoria, pero no retroceder de forma nativa"; y los errores se acumulan: "con 95% de precisión por paso, la precisión baja a unos 60% en 10 pasos" (0,95^10 ≈ 0,60; el cálculo asume pasos independientes). https://huyenchip.com/2025/01/07/agents.html
- Kambhampati et al. sostienen que "auto-regressive LLMs cannot, by themselves, do planning or self-verification", y proponen LLM-Modulo: el LLM genera candidatos y verificadores externos los critican, en un ciclo. Critican por igual a quienes dicen que el prompt adecuado basta y a quienes los reducen a traductores hacia solvers simbólicos. https://arxiv.org/abs/2402.01817 . Discrepancia a presentar: el post de Huyen deja abierta la cuestión; Kambhampati la da por cerrada en su tesis (a falta de verificador externo). El abstract es de 2024: no cubre los modelos de razonamiento posteriores y no verifiqué si el grupo actualizó su tesis (hueco).
- Agentes de larga duración: METR define el horizonte de tiempo al 50%: la duración de las tareas (medida en tiempo de expertos humanos) que un modelo completa con 50% de éxito. En el preprint original (2025-03), Claude 3.7 Sonnet alcanzó unos 50 minutos y el horizonte se duplicaba aproximadamente cada siete meses desde 2019 (puede haberse acelerado en 2024). https://arxiv.org/abs/2503.14499 (datos del abstract parafraseados por el extractor; el autor del extractor no pudo dar el abstract literal). La página de METR indica que un agente GPT-5 tiene un horizonte de unas 2 h 17 min; advierte que las mediciones por encima de 16 horas son poco fiables con la suite actual, que las tareas son de ingeniería de software, ML y ciberseguridad, que los tiempos humanos probablemente sobreestiman el tiempo de un experto con contexto, y que "no se actualiza activamente" desde 2026-09-08 (última incorporación: Claude Mythos Preview, 2026-05-08). https://metr.org/time-horizons/ . No obtuve una tabla de valores actuales ni un tiempo de duplicación actualizado: hueco.
- SWE-bench: agentes que resuelven issues reales de GitHub; en el paper original el mejor modelo, Claude 2, resolvió el 1,96% de los problemas. https://arxiv.org/abs/2310.06770 . Estado 2026: OpenAI dejó de reportar SWE-bench Verified el 2026-02-23 porque los avances "reflejan cada vez más cuánto estuvo expuesto el modelo al benchmark en el entrenamiento" (parafraseado por el buscador), recomendó SWE-bench Pro y después retractó esa recomendación: su auditoría estima que ~30% de las tareas de Pro están rotas. https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ [S] y https://openai.com/index/separating-signal-from-noise-coding-evaluations [S]; la fecha del segundo post no la obtuve. Fuente interesada (OpenAI compite en estos rankings); ninguna fuente independiente lo confirmó.
- Cómo se sostiene una tarea larga en la práctica: lista de features, archivo de progreso y un agente de código que hace una feature por sesión (Anthropic 2025-11-26). https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents . Ver `agente.md` para el resto del harness.

### Recurso canónico

Para el mecanismo y los límites: Huyen, "Agents", secciones Planning y Reflection, más el abstract de Kambhampati et al. (ICML 2024) para la postura teórica. Para larga duración: el paper de METR (la definición de horizonte al 50%) leído con las advertencias de su página. En qué fijarse: que "plan" y "ejecución" son pasos separables y verificables; que el cálculo 0,95^10 explica por qué los agentes largos fallan; que el horizonte de tiempo mide dificultad humana de la tarea, no tiempo del agente.

### Huecos

- No se leyó el texto completo de Reflexion, LLM-Modulo ni METR: solo abstracts por extractor.
- No hay fuente propia sobre árboles de búsqueda (Tree of Thoughts, planificación con búsqueda) ni sobre modelos de razonamiento y planificación (2025-2026): fuera de las tres rondas.
- No hay tabla actual de horizonte de tiempo por modelo; la página de METR no la expone en texto.
- La cifra de SWE-bench Verified actual por modelo no se obtuvo, a propósito: OpenAI la desaconseja. Falta una fuente independiente sobre qué benchmark de código vale hoy.

## 4. (reservado) memoria y contexto de agentes

No es componente del encargo, pero es el hueco más claro de la vertical: Huyen lo trata en cap. 6 p. 300 y `agente.md` ya lo declara sin fuente. Esta ronda no lo investigó. Candidato: enlazar `contexto-y-rag` (Anthropic, "Effective context engineering for AI agents", 2025-09-29, ya leída en `sistemas-con-modelos.md`) y la herramienta de memoria de Anthropic (https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool, vista solo como enlace en la doc de tool use [S]).

## 5. fallas-de-agentes

### Tabla de fuentes

| Fuente | URL | Tipo | A | P | E | U | Recencia | Marca |
|---|---|---|---|---|---|---|---|---|
| Cemri et al., MAST (arXiv 2503.13657) | https://arxiv.org/abs/2503.13657 | prim (preprint) | 2 | 3 | 2 | 3 | v3 2025-10-26 | [M] |
| Huyen, "Agents", sección Failure modes y Evaluation | https://huyenchip.com/2025/01/07/agents.html | prim | 3 | 3 | 2 | 3 | 2025-01 | [L] |
| Yao et al., τ-bench (arXiv 2406.12045, 2024-06-17) | https://arxiv.org/abs/2406.12045 | prim (paper, Sierra) | 3 | 3 | 2 | 3 | 2024 | [M] |
| Mialon et al., GAIA (arXiv 2311.12983, 2023-11-21) | https://arxiv.org/abs/2311.12983 | prim (paper, Meta/HF) | 3 | 2 | 2 | 3 | 2023 | [M] |
| Jimenez et al., SWE-bench | https://arxiv.org/abs/2310.06770 | prim | 3 | 3 | 2 | 3 | 2023 | [M] |
| OWASP LLM06:2025 Excessive Agency | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | prim | 3 | 2 | 2 | 3 | 2025 | [L] |
| Willison, trifecta letal | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | sec | 2 | 2 | 2 | 3 | 2025-06 | [L] |
| Anthropic, "Effective harnesses for long-running agents" (fallas observadas) | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | prim (lab) | 3 | 2 | 3 | 2 | 2025-11 | [L] |

### Afirmaciones

- Taxonomía de Huyen (ya en `agente.md`): fallas de planificación (herramienta inválida, parámetros erróneos, no llegar al objetivo, incumplir restricciones de presupuesto o tiempo, creer que terminó cuando no), de herramienta (resultado erróneo o fallo del traductor de acciones) y de eficiencia. Recomienda probar cada herramienta por separado, armar un dataset de pares (tarea, inventario de herramientas) y buscar patrones de error por tipo de tarea o herramienta; si una herramienta es demasiado difícil para el agente, reemplazarla. https://huyenchip.com/2025/01/07/agents.html . Es una taxonomía de autora, sin método empírico explícito en el post.
- Taxonomía con método: MAST (Cemri et al.) se construyó con 150 trazas y anotadores humanos expertos (acuerdo kappa = 0,88), tiene 14 modos de falla en 3 categorías (problemas de diseño del sistema, desalineación entre agentes y verificación de la tarea) y se aplicó con un LLM como juez sobre MAST-Data, de más de 1.600 trazas de 7 frameworks multiagente, con GPT-4, Claude 3, Qwen2.5 y CodeLlama. https://arxiv.org/abs/2503.13657 . Es sobre sistemas multiagente y sobre modelos de 2024-2025; no se generaliza sin más a un agente solo con modelos de 2026. Preprint, sin revisión por pares en la página que leí.
- Error acumulado: ver cálculo de Huyen en la sección 3 (95% por paso = ~60% en 10 pasos). https://huyenchip.com/2025/01/07/agents.html
- Fallas observadas en agentes de código de larga duración (Anthropic): declarar el proyecto terminado antes de tiempo y marcar features hechas sin probarlas; remedios: lista de features y pruebas de punta a punta con automatización de navegador. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Evaluar trayectoria vs resultado: τ-bench compara el estado final de la base de datos con el estado objetivo anotado (resultado), con un usuario simulado por LLM; introduce pass^k (fiabilidad en k intentos del mismo caso); "even state-of-the-art function calling agents (like gpt-4o) succeed on <50% of the tasks", y con pass^8 en retail el rendimiento baja de 25% (datos de 2024). https://arxiv.org/abs/2406.12045 (la frase literal sale del extractor; recotejar). Huyen evalúa la trayectoria: validez de llamadas y de planes, y eficiencia contra una línea base (pasos, costo, latencia). https://huyenchip.com/2025/01/07/agents.html . Complementarios, no contrarios: resultado dice si llegó, trayectoria dice cómo y a qué costo.
- GAIA: preguntas de asistente general con herramientas; "los respondentes humanos obtienen un 92%, frente a un 15% de GPT-4 con plugins" (2023; muy desactualizado como estado del arte). https://arxiv.org/abs/2311.12983
- SWE-bench: ver sección 3 sobre su pérdida de validez como medida (contaminación, según OpenAI 2026-02-23, fuente interesada).
- Seguridad de acciones: Huyen compara dar poder de escritura a un agente con darle a un becario permiso de borrar la base de producción ("Just as you shouldn't give an intern the authority to delete your production database"); la ejecución automática de código implica riesgo de inyección; las acciones de alto riesgo pueden requerir aprobación humana explícita. https://huyenchip.com/2025/01/07/agents.html . OWASP LLM06 formaliza lo mismo: funcionalidad, permisos y autonomía excesivos, y mitigaciones de mínimo privilegio, aprobación humana y autorización en los sistemas de destino, no en el modelo. https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- La trifecta letal y la inyección de prompt son la causa que vuelve peligroso al agente aun con permisos "razonables": contenido no confiable más datos privados más salida al exterior. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

### Recurso canónico

Para el vocabulario y la evaluación: Huyen, "Agents", secciones Failure modes y Evaluation. Para una taxonomía con método: Cemri et al. (abstract y la tabla de los 14 modos). Para la confiabilidad: τ-bench y su métrica pass^k. Para seguridad: OWASP LLM06 (mitigaciones concretas) y Willison (el modelo mental de la trifecta). En qué fijarse: que se mida cada modo de falla por separado, que pass^k castiga lo que pass@k oculta, y que la aprobación humana va en las acciones de escritura, no en cada paso.

### Huecos

- No hay estudio independiente y reciente (2026) sobre tasas de falla por modo en agentes de un solo agente; MAST es multiagente y de 2024-2025.
- No se leyó el texto completo de MAST, τ-bench ni GAIA, solo abstracts; no tengo la lista de los 14 modos.
- τ-bench: no verifiqué las versiones posteriores (τ²-bench) ni los puntajes vigentes 2026.
- Sin incidentes documentados (casos reales de agentes que borraron datos o filtraron información) con fuente primaria; no se investigó en las tres rondas. Este es el tipo "cómo falla: incidentes" que pide el mapa de fuentes.
- Sin fuente sobre aprobación humana en la práctica (fatiga de aprobación, modos "auto" de agentes de código): el buscador mencionó un post de Willison de 2026 sobre el modo auto de Claude Code, sin abrirlo [S].
- Sin evaluación de agentes de largo plazo con costo (benchmarks que midan costo por tarea): solo la mención de eficiencia en Huyen.

## 6. Resumen de huecos

- Sin lectura de los capítulos del libro de Huyen (solo el post y los resúmenes previos).
- Memoria de agentes: sin investigar.
- Historial de versiones de MCP y seguridad real de servidores MCP: sin verificar.
- Papers leídos solo por abstract (Reflexion, LLM-Modulo, METR, SWE-bench, τ-bench, GAIA, MAST, ReAct); varias cifras vienen del extractor y piden recoteje.
- Estado 2026 de benchmarks de agentes: SWE-bench Verified desacreditado por una fuente interesada; METR sin actualizar; sin fuente independiente sobre qué medir hoy.
- Sin incidentes con fuente primaria; sin estudio independiente sobre multiagente vs agente solo con modelos actuales (Anthropic y Cognition son partes interesadas).
- Sin documentación de Google (function calling de Gemini) ni de SDK de agentes.
- Límite de método: citas por extractor; tres rondas por componente se usaron para lo anterior, y lo no encontrado queda declarado aquí.
