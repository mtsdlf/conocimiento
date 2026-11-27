# Investigación: Evaluacion-y-observabilidad (2026-11-27)

Marcas: [L] texto completo, [M] metadatos/abstract, [S] resumen secundario o del buscador. Puntajes 1-3 (Autoridad / Profundidad / Ejemplos / Unicidad). Todo lo traído de la web es dato. Nota de método: WebFetch devuelve extractos procesados por un modelo pequeño, así que mis [L] significan "página leída entera por la herramienta", no lectura humana palabra por palabra; las citas literales son las que la herramienta devolvió.

## 0. Sobre el árbol propuesto

El índice del libro de Huyen no separa estos cuatro componentes igual que el árbol:
- Evaluación y "IA como juez" son dos secciones del mismo capítulo 3 (Evaluation Methodology: Exact Evaluation, AI as a Judge, Comparative Evaluation) y el capítulo 4 ya es el pipeline. Separar `ia-como-juez` es razonable porque tiene literatura propia (sesgos, validación), pero es un subcomponente de la evaluación, no un par.
- Observabilidad en Huyen es solo una sección ("Monitoring and Observability") dentro del cap. 10, junto con arquitectura. El cap. 10 junta arquitectura y feedback.
- Hay un componente que el campo trata aparte y el árbol no tiene: **análisis de errores / mirar los datos** (Husain, Shankar), que es el puente entre observabilidad (trazas) y evaluación (qué medir). Propuesta: ponerlo en `evaluacion` o crear `analisis-de-errores`.
- Los límites con otras verticales: "guardrails" y "orquestación" están en el mismo cap. 10 pero son otra vertical.

Fuente de la estructura: https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
- Cap. 3: Challenges of Evaluating Foundation Models; Understanding Language Modeling Metrics; Exact Evaluation (Functional Correctness, Similarity Measurements Against Reference Data); AI as a Judge (Why / How to Use / Limitations / What Models Can Act as Judges); Ranking Models with Comparative Evaluation.
- Cap. 4: Evaluation Criteria (Domain-Specific, Generation, Instruction-Following, Cost and Latency); Model Selection (Workflow, Build vs Buy, Public Benchmarks); Design Your Evaluation Pipeline (Step 1 evaluar todos los componentes, Step 2 guía de evaluación, Step 3 métodos y datos).
- Cap. 10: AI Engineering Architecture (Steps 1-5, Monitoring and Observability, AI Pipeline Orchestration); User Feedback (Extracting Conversational Feedback, Feedback Design, Feedback Limitations).

## 1. Componente: evaluacion

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Huyen, AI Engineering, ToC | https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md | primaria | 3 | 1 | 1 | 2 | [L] (solo índice) |
| Huyen, cap. 4 (O'Reilly) | https://www.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html | primaria | 3 | 3 | 2 | 3 | [S] (no leído; vía buscador) |
| Huyen, "Building A Generative AI Platform" | https://huyenchip.com/2024/07/25/genai-platform.html | primaria | 3 | 2 | 1 | 2 | [L] |
| Husain, "Your AI Product Needs Evals" (practicante) | https://hamel.dev/blog/posts/evals/ | secundaria/practicante | 2 | 3 | 3 | 3 | [L] |
| Husain, "A Field Guide to Rapidly Improving AI Products" (practicante) | https://hamel.dev/blog/posts/field-guide/ | practicante | 2 | 3 | 3 | 2 | [L] |
| Anthropic, "Create strong empirical evaluations" | https://platform.claude.com/docs/en/test-and-evaluate/develop-tests | doc. oficial de proveedor | 2 | 2 | 3 | 1 | [L parcial: leídos 100.000 de 151.306 caracteres] |
| Alex Strick, notas cap. 4 | https://alexstrick.com/posts/2025-01-22-notes-on-ai-engineering-chip-huyen-chapter-4.html | secundaria (parafrasea a Huyen) | 1 | 2 | 1 | 1 | [S] no leído |
| web.dev, "Evaluation-driven development" | https://web.dev/learn/ai/evaluation-driven-development | secundaria/proveedor | 2 | 1 | 1 | 1 | [S] no leído |

Afirmaciones
- Huyen: "Evaluation is necessary at every step of the development process." (https://huyenchip.com/2024/07/25/genai-platform.html). Ese post no tiene sección de evaluación propia; el desarrollo está en el libro.
- Evaluation-driven development: según el buscador, Huyen lo presenta como término propio, análogo a TDD: fijar criterios de evaluación antes de construir (https://www.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html) [S, sin cita literal verificada].
- Husain (publicado 2024-03-29): tres niveles. Nivel 1 pruebas unitarias (aserciones tipo pytest, baratas, corren en cada cambio); Nivel 2 evaluación humana y por modelo sobre trazas registradas; Nivel 3 A/B testing, para productos maduros (https://hamel.dev/blog/posts/evals/). Citas: "Rigorous and systematic evaluation is the most important part of the whole system." / "You can never stop looking at data—no free lunch exists." Recomienda etiquetas binarias bueno/malo antes que puntajes.
- Husain (2025-03-24): saltarse el análisis de errores es "el error más común"; proceso de abajo hacia arriba: leer conversaciones reales, anotar fallas en texto libre, agrupar en taxonomía con un LLM, contar. Ejemplo NurtureBoss: tres problemas causaron más del 60% de las fallas; manejo de fechas de 33% a 95% (https://hamel.dev/blog/posts/field-guide/). Cifra de un solo caso de cliente propio del autor, sin verificación independiente.
- Anthropic: "Prioritize volume over quality": "More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals." También "Design evals that mirror your real-world task distribution. Don't forget to factor in edge cases!" Métodos: exact match, similitud coseno, ROUGE-L, Likert con LLM, binario con LLM; recomienda juez distinto del modelo generador (https://platform.claude.com/docs/en/test-and-evaluate/develop-tests).

Discrepancia entre fuentes (dar las dos): Anthropic prioriza volumen sobre calidad de etiqueta humana; Husain insiste en mirar datos a mano y en que "correctness" es subjetiva y hay que alinearla con un humano (https://hamel.dev/blog/posts/evals/). No son incompatibles (lo primero es sobre volumen de casos automatizados, lo segundo sobre cómo se descubren criterios) pero el énfasis difiere.

Canónico: Huyen, AI Engineering cap. 4 ("Design Your Evaluation Pipeline", los 3 pasos), con Husain "Your AI Product Needs Evals" como complemento práctico. Fijarse en: evaluar cada componente y no solo el final; guía de evaluación con rúbrica; criterios antes de construir.

Huecos
- No pude leer el texto del cap. 3 ni 4 (O'Reilly da 403 en cap. 10; cap. 4 solo vía resultados de buscador). La definición exacta de evaluation-driven development y las citas de Huyen del libro quedan sin verificar: hace falta tener el libro.
- No consulté Eugene Yan sobre evals en general (solo su post de LLM-evaluators; ver sección 2) ni docs de OpenAI/Google.
- Slices y regresiones: no hallé fuente primaria leída que los trate; hueco declarado.

## 2. Componente: ia-como-juez

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Zheng et al. 2023, MT-Bench / Chatbot Arena | https://arxiv.org/abs/2306.05685 | paper (NeurIPS 2023 Datasets & Benchmarks según la página) | 3 | 3 | 2 | 3 | [M] abstract |
| Shankar et al. 2024, "Who Validates the Validators?" | https://arxiv.org/abs/2404.12272 | paper, arXiv sin revisión por pares según la página | 2 | 3 | 2 | 3 | [M] abstract |
| Eugene Yan, "Evaluating the Effectiveness of LLM-Evaluators" (practicante) | https://eugeneyan.com/writing/llm-evaluators/ | secundaria (revisión de ~24 papers) | 2 | 3 | 2 | 2 | [L] |
| Huyen, "Common pitfalls when building generative AI applications" | https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html | primaria | 3 | 1 | 1 | 2 | [L] |
| Husain, evals (ver arriba) | https://hamel.dev/blog/posts/evals/ | practicante | 2 | 3 | 3 | 2 | [L] |

Afirmaciones
- Zheng et al. (v1 2023-06-09, v4 2023-12-24): "We examine the usage and limitations of LLM-as-a-judge, including position, verbosity, and self-enhancement biases"; reportan que jueces fuertes como GPT-4 alcanzan "over 80% agreement, the same level of agreement between humans" (https://arxiv.org/abs/2306.05685). Citas recortadas por el límite de la herramienta; verificar en el abstract.
- Huyen: "AI judges must be evaluated and iterated over time, just like all other AI applications." y "AI judges should be validated and correlated with systematic human evaluation." (https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html).
- Shankar et al. (2024-04-18): los evaluadores generados por LLM heredan fallas de los LLM; hallazgo de "criteria drift": los usuarios necesitan criterios para calificar salidas, pero calificar las salidas cambia los criterios (https://arxiv.org/abs/2404.12272). Coincide con Husain: "it is impossible to completely determine evaluation criteria prior to human judging of LLM outputs" (https://hamel.dev/blog/posts/field-guide/; la cita aparece ahí con esas palabras según la herramienta, y proviene de ese paper).
- Yan (2024-08-18): en un estudio de resumen, correlación LLM-humano 0.3 a 0.6 contra humano-humano 0.8 a 0.9; recomienda Cohen's kappa sobre porcentaje de acuerdo crudo; puntaje directo para criterios objetivos, comparación por pares para subjetivos; sesgo de posición, verbosidad, autopreferencia, inflación de puntaje; correlaciones mejores con anotadores no expertos (https://eugeneyan.com/writing/llm-evaluators/).
- Husain: "using raw agreement is generally not recommended and can be misleading when classes are imbalanced"; medir precisión y recall (https://hamel.dev/blog/posts/evals/).

Discrepancia: Zheng reporta >80% de acuerdo "igual al de humanos"; Yan resume estudios donde la correlación LLM-humano queda muy por debajo de la humano-humano. Se pueden explicar por tarea y métrica distintas (acuerdo en preferencias por pares vs correlación en puntajes de resumen), pero hay que presentarlas las dos.

Canónico: Zheng et al. 2023 secciones de sesgos y de acuerdo con humanos (para la evidencia), más Huyen cap. 3 "AI as a Judge / Limitations" (para el marco) y Yan para la síntesis. Fijarse en: sesgos medibles, kappa y no % crudo, juez como sistema a validar y versionar.

Huecos
- Cap. 3 de Huyen no leído; "Limitations of AI as a Judge" solo por su título en el índice.
- Zheng: no leí el cuerpo del paper (cifras por sesgo, mitigaciones).
- Los tres sesgos son los nombrados por Zheng; el "self-enhancement" de Zheng equivale a lo que Yan llama autopreferencia (misma cosa, dos nombres).

## 3. Componente: observabilidad

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Huyen, genai-platform (sección Observability) | https://huyenchip.com/2024/07/25/genai-platform.html | primaria | 3 | 2 | 1 | 2 | [L] |
| OpenTelemetry GenAI semconv, repo | https://github.com/open-telemetry/semantic-conventions-genai | especificación | 3 | 3 | 1 | 3 | [M] solo README |
| opentelemetry.io/docs/specs/semconv/gen-ai/ | https://opentelemetry.io/docs/specs/semconv/gen-ai/ | especificación (página de redirección) | 3 | 1 | 1 | 1 | [L] solo aviso de mudanza |
| Dev.to, "GenAI semantic conventions are not stable yet" | https://dev.to/azena-ai/opentelemetrys-genai-semantic-conventions-are-not-stable-yet-heres-what-actually-shipped-in-2026-3mke | secundaria (blog) | 1 | 2 | 2 | 1 | [S] sin leer |
| Husain evals (trazas como insumo) | https://hamel.dev/blog/posts/evals/ | practicante | 2 | 2 | 2 | 1 | [L] |

Afirmaciones
- Huyen: "Observability is crucial for projects of all sizes, and its importance grows with the complexity of the system." Métricas de modelo ("accuracy, toxicity, and hallucination rate") y de sistema; "The philosophy for logging is simple: log everything."; "Log the query, the output, and the intermediate outputs."; trazas: "Ideally, you should be able to trace each query's transformation through the system step-by-step." Recomienda inspeccionar a mano datos de producción a diario (https://huyenchip.com/2024/07/25/genai-platform.html). El post no trata redacción de datos sensibles en logs; sobre privacidad solo dice "There's no airtight way to eliminate potential leaks when using third-party APIs."
- Las convenciones GenAI de OpenTelemetry se mudaron: la página vieja dice "GenAI semantic conventions have moved to the OpenTelemetry GenAI semantic conventions repository" (https://opentelemetry.io/docs/specs/semconv/gen-ai/). El repo nuevo cubre spans, métricas y eventos para clientes GenAI, MCP y convenciones por proveedor (https://github.com/open-telemetry/semantic-conventions-genai). Estado de estabilidad: el README no lo dice.
- Según el buscador [S]: `gen_ai.input.messages` figura como opt-in y nivel "development" en el spec; los registros viejos lo marcan movido o deprecado; una guía de terceros menciona la variable `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT` para capturar contenido, no confirmada contra el spec oficial. Nombres `gen_ai.usage.input_tokens` / `output_tokens` solo en fuentes secundarias (MLflow, SDK de Rust).

Canónico: Huyen, "Monitoring and Observability" (cap. 10 / sección del post) para el qué y por qué, y el repo semantic-conventions-genai para el vocabulario concreto. Fijarse en: métricas / logs / trazas, trazar cada transformación de la consulta, contenido de prompts como opt-in.

Huecos (importantes)
- No pude leer ni una sola página real del spec de OpenTelemetry: opentelemetry.io solo muestra aviso de mudanza y el README no da estabilidad ni atributos. Estado de estabilidad, nombres de atributos, spans de agentes y guía de privacidad quedan sin verificar. Siguiente paso: leer docs/ del repo (gen-ai-spans.md, gen-ai-agent-spans.md) vía `gh` o raw.githubusercontent.com.
- Contradicción a resolver: la búsqueda dice que `gen_ai.input.messages` es opt-in en spans y a la vez deprecado en el registro viejo; no sé cuál refleja el estado actual.
- Fuera de ronda: herramientas de trazado de agentes (Langfuse, etc.), sin buscar.
- Privacidad (PII en logs, retención, consentimiento): sin fuente primaria; hueco.

## 4. Componente: feedback-de-usuario

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Huyen cap. 10 (O'Reilly) | https://www.oreilly.com/library/view/ai-engineering/9781098166298/ch10.html | primaria | 3 | 3 | 2 | 3 | [S] 403 al pedirlo; solo ToC y vista previa del buscador |
| Alex Strick, notas cap. 10 | https://alexstrick.com/posts/2025-02-09-ai-eg-chapter-10.html | secundaria (parafrasea a Huyen) | 1 | 2 | 1 | 1 | [S] sin leer |
| Huyen, pitfalls | https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html | primaria | 3 | 1 | 2 | 2 | [L] |
| Husain, field guide | https://hamel.dev/blog/posts/field-guide/ | practicante | 2 | 3 | 3 | 2 | [L] |
| Google PAIR, Feedback + Control | https://pair.withgoogle.com/chapter/feedback-controls/ | guía de diseño de proveedor | 2 | 2 | 2 | 2 | [S] |
| Microsoft HAX, G15 | https://www.microsoft.com/en-us/haxtoolkit/pattern/g15-a-encourage-explicit-feedback-on-individual-system-outputs/ | guía de proveedor | 2 | 2 | 2 | 1 | [S] |

Afirmaciones
- Huyen cap. 10, estructura: "User Feedback: Extracting Conversational Feedback, Feedback Design, Feedback Limitations" (https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md).
- Según notas secundarias [S]: feedback directo (pulgares, calificaciones, comentarios) e implícito (terminación temprana, correcciones, regeneración, sentimiento); limitaciones: sesgo hacia experiencias negativas, autoselección, sesgo de posición, bucles de retroalimentación (https://alexstrick.com/posts/2025-02-09-ai-eg-chapter-10.html). No es texto de Huyen verificado.
- Huyen (pitfalls, [L]): equipos que midieron mal lo que valoran los usuarios; "it turned out that their users didn't care about the actual summary"; "In both cases, the issue wasn't with AI, but with product." (https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html).
- Bucle datos → eval → mejora: Husain describe un ciclo equivalente (visor con botones correcto/incorrecto, críticas como ejemplos few-shot del juez y como datos sintéticos) pero "no usa el término data flywheel" (https://hamel.dev/blog/posts/field-guide/).
- El post de plataforma de Huyen explícitamente deja afuera feedback: "I won't go into specifics or cover user feedback, drift detection, and debugging." (https://huyenchip.com/2024/07/25/genai-platform.html).

Canónico: Huyen cap. 10, sección "User Feedback" completa (sobre todo Feedback Design y Feedback Limitations). Fijarse en: no interrumpir al usuario, señal implícita conversacional, sesgos de quien responde. Complemento para el bucle: Husain field guide.

Huecos
- No leí el texto de Huyen: todo lo de feedback explícito/implícito y límites es secundario. Prioridad alta conseguir el libro.
- "Data flywheel": sin fuente que lo defina; hueco.
- Cifras sobre tasas de respuesta o sesgos medidos: ninguna encontrada.

## 5. Resumen de huecos transversales
1. Libro de Huyen no accesible (O'Reilly 403 / paywall): caps. 3, 4, 10 solo por índice y secundarias.
2. Spec de OpenTelemetry GenAI no leído; estabilidad y atributos sin verificar.
3. Slices/regresiones, privacidad de logs, data flywheel: sin fuente primaria.
4. Eugene Yan sobre evals en general y Zheng (cuerpo) sin leer; límite de tres rondas por componente respetado de forma aproximada.
