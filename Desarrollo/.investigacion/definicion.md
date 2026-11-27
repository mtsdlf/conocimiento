# Investigación: vertical Definición (Desarrollo de software)

Fecha de la investigación: 2026-11-27. Alcance: `Desarrollo/Definicion/` según `Desarrollo/ALCANCE.md` (especificación, historia de usuario, criterios de aceptación, descomposición en tareas, modelo de dominio).

Marcas de lectura: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U). Nota general sobre el método: las páginas se leyeron con una herramienta que devuelve un resumen del contenido (no el texto crudo), por lo que casi todo lo que figura como [L] es en rigor una lectura resumida de la página completa; donde una cita es literal, está entre comillas y viene de ese resumen. Los preprints de arXiv están sin revisión por pares salvo que se diga lo contrario. Los códigos de arXiv que empiezan con 26xx y las fechas de 2026 son las que devolvieron las páginas consultadas.

## 0. Hallazgos transversales (lo que cambia el árbol)

1. **El corte del árbol coincide en general con el campo**, con tres ajustes propuestos:
   - `criterios-de-aceptacion` se solapa con `historia-de-usuario` (la nota existente ya trae Dado/Cuando/Entonces). Corte propuesto: la historia queda como la unidad de valor (Cohn, INVEST, Patton) y los criterios pasan a ser "ejemplos como contrato" (Adzic, Wynne, Gherkin). La parte de Gherkin de la nota existente se muda a criterios.
   - `modelo-de-dominio` debe incluir los dos pasos que el campo separa: *descubrir* (Event Storming, entrevistas) y *fijar* (lenguaje ubicuo, contextos delimitados, glosario). Se propone mantenerlo un solo componente; si crece, partir en `lenguaje-ubicuo` y `descubrir-el-dominio`.
   - Falta un tema que el campo trata aparte y que con agentes pesa mucho: **detectar y cerrar la ambigüedad antes de construir** (preguntas de aclaración, entrevista al cliente o al agente). No es componente propio: va como sección de `especificacion` y de `criterios-de-aceptacion` (fuentes en 1.4 y 2.4).
2. **No hacen falta componentes propios para requisitos no funcionales ni prototipo** (sección 6): ya los cubren `Arquitectura/Caracteristicas/` y `Producto/Descubrimiento/`. Sí hace falta que `especificacion` los enlace y diga cómo entran en la spec.
3. **Spec-driven development (SDD) es práctica emergente con evidencia débil a favor**: un estudio de 88.052 PRs no encuentra efecto de la calidad de la especificación sobre defectos ni retrabajo (con la salvedad de que lo medido son sobre todo links a tickets, no salida de herramientas SDD); un estudio de Google sí encuentra mejora al generar tests desde pre y postcondiciones. El Radar de Thoughtworks lo tiene en "Assess" (Spec Kit, abril 2026) y OpenSpec subió a "Trial" (noviembre 2026). La nota debe presentar SDD con sus tres niveles y decir que la evidencia es mixta, no venderlo.
4. **Lo que sigue vigente casi sin cambio es la capa de ejemplos ejecutables**: el consejo de Anthropic ("Give Claude something it can run that comes back pass or fail") y el de OpenAI ("Done when") son, en la práctica, criterios de aceptación verificables. Eso une `criterios-de-aceptacion` con `Verificacion/`.
5. **La nota existente `historia-de-usuario.md` tiene un defecto de redacción** (la última sección, "Historia y tarea técnica", empieza con una oración sin verbo: "Una tarea técnica."), y la carpeta de origen es `Especificacion-y-prueba/` (hay que mudarla con `git mv`). Detalle en 2.5.

---

## 1. especificacion

### 1.1 Qué es una especificación hoy
Dos definiciones citadas por Böckeler: GitHub, "In this new world, maintaining software means evolving specifications."; Tessl, "A development approach where specs — not code — are the primary artifact." La misma autora avisa de la deriva del término: "spec" se está volviendo vago y a veces solo significa un prompt detallado (https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).

### 1.2 Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", martinfowler.com, 15-oct-2025 | secundaria (practicante, Thoughtworks) | 3/3/3/3 | [L] | https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html |
| Thoughtworks Radar, "Spec-driven development", Assess, nov-2025 (vol. 35); ya no está en la edición vigente | secundaria (práctica) | 2/1/1/2 | [L] | https://www.thoughtworks.com/radar/techniques/spec-driven-development |
| Thoughtworks Radar, "GitHub Spec Kit", Assess, abr-2026 | secundaria | 2/2/2/3 | [L] | https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit |
| Thoughtworks Radar, "OpenSpec", Trial, nov-2026 | secundaria | 2/2/1/3 | [L] | https://www.thoughtworks.com/radar/tools/openspec |
| GitHub Spec Kit (repo/README) | primaria, volátil (visto 2026-11-27) | 3/2/2/3 | [L] | https://github.com/github/spec-kit |
| Kiro, docs "Specs" | primaria, volátil | 3/2/2/3 | [L] | https://kiro.dev/docs/specs/ |
| Anthropic, Claude Code best practices | primaria, volátil | 3/3/3/3 | [L] | https://code.claude.com/docs/en/best-practices |
| OpenAI, Codex best practices (redirige a learn.chatgpt.com) | primaria, volátil | 3/2/2/2 | [L] | https://learn.chatgpt.com/guides/best-practices |
| Agarwal et al., "Spec-Driven Development as Prescribed and as Practiced" (CMU y Google), arXiv, v1 25-ago-2026, v5 16-nov-2026 | primaria, preprint sin revisión por pares | 2/3/2/3 | [M] | https://arxiv.org/abs/2608.25202 |
| Hill, "Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects", ESEM 2026 (LIPIcs 394) | primaria, con revisión (actas) | 3/3/2/3 | [M] | https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84 |
| Piskala, "Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants", arXiv 2602.00180, 30-ene-2026, enviado a AIWare 2026; sin revisión por pares confirmada | primaria, preprint | 1/2/2/2 | [M] | https://arxiv.org/abs/2602.00180 |
| "Grounding AI Agents in Contracts: An Empirical Evaluation of Spec-Driven Test Generation" (SpecOps '26; Google Research) | primaria | 2/2/1/3 | [S] | https://research.google/pubs/grounding-ai-agents-in-contracts-an-empirical-evaluation-of-spec-driven-test-generation/ |
| ISO/IEC/IEEE 29148:2018, página del IEEE | primaria (norma) | 3/1/1/3 | [M] | https://standards.ieee.org/ieee/29148/6937 |
| SWEBOK v4.0 (IEEE Computer Society, 2024, ed. Washizaki; v4.0a en sep-2025) | primaria | 3/3/1/3 | [S] | https://www.computer.org/education/bodies-of-knowledge/software-engineering (la página devolvió 403 al leerla; datos vía buscador) |
| Mavin, "EARS" | primaria | 3/2/3/3 | [L] | https://alistairmavin.com/ears/ |

### 1.3 Afirmaciones con fuente
- **Tres niveles de SDD.** Spec-first: "A carefully written spec comes before AI-assisted coding, and it guides the current task." Spec-anchored: la spec se conserva tras la tarea y sirve para evolucionar y mantener la funcionalidad. Spec-as-source: la spec es el artefacto principal a largo plazo y las personas solo editan la spec, nunca el código generado (resumen de Böckeler; https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html). Piskala nombra los mismos tres niveles ("levels of specification rigor") en su abstract (https://arxiv.org/abs/2602.00180). Son dos fuentes, pero Piskala es posterior y parece tomar la clasificación de Böckeler: cuenta como una sola para los niveles.
- **Qué hace cada herramienta.** Kiro: tres archivos, `requirements.md` (o `bugfix.md`), `design.md` y `tasks.md`, en tres fases; "Waves execute sequentially; tasks within a wave execute concurrently"; hay un "Quick Spec" sin puertas de aprobación (https://kiro.dev/docs/specs/). Spec Kit: constitución una vez por proyecto, y por funcionalidad Specify, Plan, Tasks, Implement y Converge, repetidos hasta que Converge devuelva `Converged`; la página no lista agentes soportados (https://github.com/github/spec-kit). Böckeler juzga a Kiro "mostly spec-first" y a Spec Kit spec-first en la práctica aunque aspira a spec-anchored; Tessl, en beta privada a la fecha del artículo, apunta a spec-anchored y explora spec-as-source con una relación 1 a 1 entre spec y archivo de código.
- **Críticas de Böckeler.** Kiro convirtió un bug chico en cuatro historias de usuario con 16 criterios de aceptación; Spec Kit le pareció excesivo para una funcionalidad mediana; los agentes a veces ignoraron instrucciones (duplicó clases que había investigado) y otras las aplicaron de más; en Tessl la misma spec produjo código distinto entre corridas; spec-as-source recuerda al desarrollo dirigido por modelos (MDD), que "never took off for business applications", y teme combinar su rigidez con la imprevisibilidad de los modelos (https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
- **Radar.** Nov-2025, Assess: flujos "elaborate and opinionated", resultados que varían con el tamaño y tipo de tarea, specs difíciles de revisar, y "unclear who the intended audience is" de los PRD o historias generados; los autores sugieren que puede repetir la "bitter lesson" (las reglas escritas a mano para IA no escalan) (https://www.thoughtworks.com/radar/techniques/spec-driven-development). Abr-2026, Spec Kit: equipos divididos entre confiar en agentes mejores con poca estructura y preferir flujos con specs detalladas; usos mayormente en código existente; la constitución sirve cuando cubre alcance, contexto de dominio, versiones, estándares y estructura del repo; "instruction bloat" y luego "context rot"; un equipo movió la guía reutilizable a skills; "Experienced engineers with strong clean coding and architectural practices get the most value" (https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit). Nov-2026, OpenSpec pasa a Trial: spec-anchored, con cambios registrados como deltas contra una spec persistente, "more predictable agent output and fewer unintended changes", y la advertencia de que los agentes generan mucho Markdown y mantener la spec exige disciplina (https://www.thoughtworks.com/radar/tools/openspec). Las tres entradas son del mismo emisor: peso de práctica, no de estudio.
- **Evidencia en contra (la más fuerte).** Hill, sobre 88.052 PRs, 119 repos y 25.209 artefactos de especificación: calidad de la spec vs defectos p = 0,164, vs retrabajo p = 0,860, restricción de alcance en cambios marcados como IA p = 0,997; ninguna de las cinco hipótesis se sostiene. Salvedades del propio autor: los "artefactos" son sobre todo links a tickets, ningún repo de la muestra versiona salida de herramientas SDD, y la adopción de herramientas SDD queda sin probar; "Developers write specs for their hardest work" confunde la comparación (https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84).
- **Evidencia a favor (acotada).** Estudio de generación de tests: documentar pre y postcondiciones antes de generar tests mejora la detección de bugs en 9,8 puntos porcentuales (p = 0,0352) y la cobertura de ramas en 2,5 (p = 0,0034) frente a un agente base (https://research.google/pubs/grounding-ai-agents-in-contracts-an-empirical-evaluation-of-spec-driven-test-generation/ , [S]; la lista de autores difiere entre el buscador y arXiv 2608.17177, verificar). Es sobre tests, no sobre construir funcionalidades.
- **Práctica real.** Entrevistas a 21 practicantes (ocho son creadores de herramientas) y minería de 266 repos activos, de un corpus de 470.795 archivos de spec en 73.030 repos: acuerdan en que la spec debe capturar la intención, pero muchos incluyen detalles de implementación; se usa de forma selectiva, sobre todo en funcionalidades nuevas; más fiabilidad del agente, pero más costo de planificar y revisar; los detalles de implementación hacen a las specs "prone to decay"; los chequeos spec-código se hacen al final del cambio, no de forma continua (https://arxiv.org/abs/2608.25202).
- **Lo que dicen los fabricantes de agentes.** Anthropic: ante algo no del todo pensado, pedirle a Claude "Interview me until you could write the spec, then write it to SPEC.md", y arrancar la construcción en sesión nueva "so the build begins with a clean context and a written definition of done"; también revisar contra la spec con un subagente (https://code.claude.com/docs/en/best-practices). OpenAI: estructurar el prompt con "Goal", "Context", "Constraints" y "Done when"; si la tarea es compleja o ambigua, planear antes de codear (https://learn.chatgpt.com/guides/best-practices).
- **Notación de requisitos.** EARS (Rolls-Royce, publicada en 2009; el nombre del congreso no se pudo confirmar): "When <trigger>, the <system name> shall <system response>", y cinco patrones más (ubicuo, estado, opcional, no deseado, complejo) (https://alistairmavin.com/ears/). La página de Kiro no menciona EARS: la afirmación frecuente de que Kiro usa EARS no se pudo verificar en la fuente primaria consultada.
- **Norma.** ISO/IEC/IEEE 29148:2018 (publicada 2018-11-30, sustituye a 29148-2011): "defines the construct of a good requirement, provides attributes and characteristics of requirements" (https://standards.ieee.org/ieee/29148/6937). Un paper secundario dice que define nueve características por requisito individual y que su antecesor IEEE 830 tenía ocho para el SRS (https://arxiv.org/pdf/2305.05800 , [S]); la lista no se verificó en la norma. SWEBOK v4.0: el capítulo 1 es Software Requirements, con ocho secciones (fundamentos, elicitación, análisis, especificación, validación, gestión, consideraciones prácticas, herramientas); un comentario de terceros sobre el borrador de enero de 2024 dice que fue reescrito y ampliado respecto de v3 (https://medium.com/analysts-corner/swebok-v3-and-v4-software-requirements-a598cf7ea485 , [S], solo sobre borrador).

### 1.4 Qué cambia con agentes
- La spec pasa de documento para personas a **insumo ejecutable por un agente**, con "definición de terminado" explícita (Anthropic, OpenAI, arriba).
- Los agentes **no detectan bien lo que falta**: en Ambig-SWE (Carnegie Mellon, ICLR 2026), los modelos tienen dificultad para distinguir tareas bien especificadas de subespecificadas, por defecto no preguntan, y la interacción mejora el rendimiento hasta un 74% sobre el caso no interactivo en entradas subespecificadas (https://arxiv.org/abs/2502.13069 , [S]); "Ask or Assume?" (EMNLP 2026, camera-ready) separa detectar subespecificación de ejecutar y llega a 69,40% de tareas resueltas en la variante subespecificada de SWE-bench Verified (https://arxiv.org/abs/2603.26233 , [M]). Implicancia para la nota: la spec incluye una lista de preguntas abiertas y suposiciones, y el agente se configura para preguntar.
- El costo de **revisar specs** crece (Böckeler, Radar, Agarwal): una spec larga que nadie lee no sirve. Regla práctica a sostener con esas fuentes: el tamaño de la spec debe seguir al tamaño y claridad del problema.
- La constitución o contexto del proyecto choca con **context rot** (Radar Spec Kit); la fuente "Codified Context" (Vasilopoulos, arXiv 2602.20478, feb-2026, un solo autor, preprint, caso único: sistema C# de 108.000 líneas, 34 documentos de spec bajo demanda y 283 sesiones) propone memoria caliente (constitución) y fría (specs a pedido) (https://arxiv.org/abs/2602.20478 , [M]); es evidencia de un caso, no un estudio.

### 1.5 Qué pierde peso de la práctica clásica
- El **documento de requisitos completo antes de empezar** (la forma ISO 29148 / IEEE 830 como entregable monolítico). Fuentes que sostienen el cambio: la crítica de Böckeler al peso de las specs largas y de pasos pequeños e iterativos; el estudio de Agarwal (uso selectivo, decae). Ninguna fuente consultada dice "29148 quedó obsoleta": el reemplazo es lectura de esta base. Lo que **sigue vigente** de 29148 y SWEBOK es el vocabulario de calidad de un requisito (necesario, no ambiguo, verificable, trazable) y la distinción entre requisito y diseño. Pendiente leer 5.2.5 de la norma para citar las características literales.
- La **trazabilidad por matrices** a mano: sin fuente propia en esta investigación; declararla como hueco, no como hallazgo.

### 1.6 Recurso canónico propuesto
Böckeler, "Understanding Spec-Driven-Development" (martinfowler.com), completo: da los tres niveles, el mapa de herramientas y las críticas, y es la fuente que citan las otras. Complementar con Hill (ESEM 2026) para la evidencia y con la sección "Tell Claude what it can't see" y "Give Claude a check to run" de la guía de Anthropic para el cómo.

---

## 2. historia-de-usuario y criterios-de-aceptacion

### 2.1 Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Mountain Goat Software, "User Stories" (Cohn) | secundaria; no muestra byline | 2/1/1/1 | [L] | https://www.mountaingoatsoftware.com/agile/user-stories |
| Cohn, *User Stories Applied* (2004) | primaria, libro | 3/3/3/3 | no leído | https://www.mountaingoatsoftware.com/books/user-stories-applied |
| Wake, "INVEST in Good Stories, and SMART Tasks" (2003) | primaria | 3/2/2/3 | no releído (citado en la nota existente) | https://xp123.com/invest-in-good-stories-and-smart-tasks/ |
| Patton, página de "User Story Mapping" (28-ene-2008) | primaria | 3/1/1/2 | [L] | https://www.jpattonassociates.com/user-story-mapping/ |
| Patton, *User Story Mapping* (O'Reilly, 2014) | primaria, libro | 3/3/3/3 | no leído | https://www.oreilly.com/library/view/user-story-mapping/9781491904893/ |
| Adzic, *Specification by Example* (Manning, 2011) | primaria, libro | 3/3/3/3 | [S] (índice y descripción) | https://www.manning.com/books/specification-by-example |
| Wynne, "Introducing Example Mapping", Cucumber (8-dic-2015) | primaria | 3/2/2/3 | [L] | https://cucumber.io/blog/bdd/example-mapping-introduction/ |
| Cucumber, Gherkin Reference | primaria | 3/3/3/3 | [L] | https://cucumber.io/docs/gherkin/reference/ |
| Fowler, "Given When Then" (21-ago-2013) | secundaria | 3/1/1/2 | [L] | https://martinfowler.com/bliki/GivenWhenThen.html |
| Agile Alliance, User Stories | secundaria | 2/1/1/1 | citada en la nota existente | https://www.agilealliance.org/glossary/user-stories/ |

### 2.2 Afirmaciones con fuente
- **Historia.** Cohn: "a short description of desired functionality", dicha desde quien la necesita; plantilla "As a [type of user], I [need/want/am required] to [do something], so that [reason or benefit]"; las tres C de Ron Jeffries (tarjeta, conversación, confirmación); "The conversation is where understanding grows." La página no menciona INVEST (https://www.mountaingoatsoftware.com/agile/user-stories). INVEST es de Wake (2003), no de Cohn: la nota existente lo atribuye bien a Wake.
- **Story mapping.** "A user story map arranges user stories into a useful model" del sistema, para ver huecos y planear entregas con valor; el método combina el Task Modeling de Constantine y Lockwood con talleres de escritura de historias, y su método de planificación se describió primero en el artículo "How You Slice It" (*Better Software*, enero 2005) (https://www.jpattonassociates.com/user-story-mapping/). La página consultada no habla de columna vertebral ni de "walking skeleton": eso hay que tomarlo del libro de 2014, no leído.
- **Ejemplos como especificación.** Adzic: método colaborativo con siete patrones; el ciclo va de derivar el alcance desde los objetivos, especificar en colaboración, ilustrar con ejemplos, refinar la especificación y automatizar la validación sin cambiar las especificaciones; el producto es documentación viva (https://www.manning.com/books/specification-by-example , [S]).
- **Given-When-Then.** Es "a style of representing tests", desarrollado por Daniel Terhorst-North y Chris Matts en BDD; los pasos `then` deben usar consultas sin efectos secundarios (https://martinfowler.com/bliki/GivenWhenThen.html).
- **Gherkin.** Given fija el estado inicial; When una acción o evento; Then "an observable outcome", y debe afirmar algo que el usuario o un sistema externo vea, no estado interno como registros en la base; guía: 3 a 5 pasos por ejemplo, Background corto (menos de unas cuatro líneas), "Describe behavior, not implementation"; `Rule` agrupa ejemplos de una regla de negocio (Gherkin 6 o posterior); Scenario Outline con tabla de Examples; traducido a más de 70 idiomas con encabezado `# language:` (no se verificó el español puntualmente) (https://cucumber.io/docs/gherkin/reference/).
- **Example Mapping.** Tarjetas amarillas (la historia), azules (reglas), verdes (ejemplos), rojas (preguntas sin respuesta en la sala); "about 25 minutes" para una historia bien entendida y de tamaño razonable, y votación rápida de si está lista; muchas rojas indican que falta aprender; muchas azules, que la historia es grande; una regla con muchos ejemplos puede ser varias reglas (https://cucumber.io/blog/bdd/example-mapping-introduction/).

### 2.3 Qué falta y qué sigue vigente en `historia-de-usuario.md`
- Sigue vigente: plantilla, tres C, INVEST, Dado/Cuando/Entonces, épica como agrupación. Todo está en las fuentes primarias de arriba.
- Falta: (a) Patton y el mapa de historias (cómo se descubre el conjunto y se corta el primer release), (b) la relación con la spec de un agente: la historia es la unidad de *valor*, no la unidad de *trabajo* del agente, (c) enlazar a descomposición (slicing vertical) y a `Producto/Planificacion-y-entrega/shape-up.md` y `Producto/Descubrimiento/dar-forma-a-una-solucion.md` (esa nota ya menciona a Patton), (d) la historia como detonante de la conversación y no como especificación completa (Cohn).
- A revisar: la nota afirma que el formato Connextra "nació en 2001 en esa empresa británica": no lo verifiqué en esta ronda; si no se encuentra fuente, quitar o marcar. La última sección está cortada ("Una tarea técnica." sin verbo). Los criterios "Dado/Cuando/Entonces" del ejemplo tienen "una lista vacía con un mensaje", correcto, pero no declaran el caso de error de forma explícita para un agente.
- `estado: borrador`, `revisado:` vacío: por convención no se pasa a vigente sin lectura de una persona.

### 2.4 Qué cambia con agentes
- Los criterios de aceptación pasan a ser **el contrato de "terminado"** del agente: Anthropic recomienda darle "something it can run that comes back pass or fail" (test, código de salida del build, linter, diff contra un fixture, captura contra el mockup) y pedir "evidence": el comando y su salida, porque "All tests pass" solo dice poco (https://code.claude.com/docs/en/best-practices). La lista de cinco preguntas antes de dejarlo correr solo empieza por "Does it know what done looks like? A goal condition, a spec file, or a failing test it has to turn green." (misma fuente).
- Un arnés de Anthropic para trabajos largos expande el pedido en una lista de funcionalidades en JSON, todas inicialmente "failing", donde el agente solo puede cambiar el estado; eligieron JSON porque los modelos lo alteran menos que Markdown; la prueba de punta a punta con automatización de navegador mejoró mucho el resultado frente a tests unitarios y `curl` (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents , [L], 26-nov-2025). Es la forma más clara de "criterios como contrato".
- Fallas documentadas: el agente "declare the job done" demasiado pronto y marca funcionalidades completas sin probarlas (misma fuente). Por eso el criterio debe poder ejecutarse, no solo leerse.
- Example Mapping sirve de **entrevista previa**: las tarjetas rojas son las preguntas que hay que llevar al cliente antes de lanzar al agente (conexión mía con Ambig-SWE, 1.4).

### 2.5 Qué pierde peso
- La **estimación en puntos de historia** como parte de la historia (solo declarado en ALCANCE; sin fuente propia acá, va a `Estimacion`).
- **Escribir criterios como prosa informal sin ejecución**: la fuente (Adzic, Anthropic) empuja al ejemplo ejecutable.
- **Gherkin como obligación**: el Gherkin Reference no lo impone; el valor está en los ejemplos concretos, no en la sintaxis. (Lectura de esta base; sin fuente que mida el costo de mantener Gherkin.)

### 2.6 Recurso canónico propuesto
Historia: Cohn, *User Stories Applied* (cap. de las tres C y de las buenas historias) y Patton, *User Story Mapping* (primeros capítulos); ninguno leído completo aquí. Criterios: Wynne, "Introducing Example Mapping" (se lee en 10 minutos y da el método) más el Gherkin Reference para la sintaxis; Adzic como libro de fondo.

---

## 3. descomposicion-en-tareas

### 3.1 Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Lawrence, Humanizing Work, "Guide to Splitting User Stories" | primaria | 3/3/3/3 | [L] | https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/ |
| Anthropic, "Effective harnesses for long-running agents", 26-nov-2025 | primaria, volátil | 3/3/3/3 | [L] | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |
| Anthropic, Claude Code best practices | primaria, volátil | 3/3/3/3 | [L] | https://code.claude.com/docs/en/best-practices |
| OpenAI, Codex best practices | primaria, volátil | 3/2/2/2 | [L] | https://learn.chatgpt.com/guides/best-practices |
| METR, "Time Horizon 1.1", 29-ene-2026 | primaria (organización de investigación; método publicado, sin revisión por pares conocida) | 2/3/2/3 | [L] | https://metr.org/blog/2026-1-29-time-horizon-1-1 |
| METR, "Measuring AI Ability to Complete Long Tasks", arXiv 2503.14499, mar-2025 | primaria, preprint | 2/3/2/3 | [S] | https://arxiv.org/abs/2503.14499 |
| METR, RCT de desarrolladores con experiencia, arXiv 2507.09089, jul-2025 | primaria, preprint | 2/3/2/3 | [S] | https://arxiv.org/abs/2507.09089 |
| Kiro docs (tareas por oleadas) | primaria, volátil | 3/2/2/3 | [L] | https://kiro.dev/docs/specs/ |

### 3.2 Afirmaciones con fuente
- **Rebanada vertical.** Lawrence: "a work item that delivers a valuable change in system behavior"; las horizontales cubren una sola capa; hay que "find thin vertical slices inside those wide ones". Nueve patrones: pasos del flujo (cuidado: "the most obvious split—one step at a time from beginning to end—is the wrong way to go"), operaciones (la palabra "manage" delata varias operaciones), variaciones de reglas de negocio, variaciones de datos, métodos de ingreso de datos, esfuerzo mayor, simple/complejo, postergar rendimiento y abrir un *spike* "should be your last resort"; un metapatrón: encontrar la complejidad central, identificar las variaciones y reducirlas a una rebanada completa. Advierte que "diferir rendimiento" acumula deuda si se da por hecha una historia antes de tiempo (https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/).
- **Una funcionalidad por sesión.** En el arnés de Anthropic cada sesión apunta a una sola funcionalidad, y lo llaman crítico por la tendencia a "try to do too much at once"; el intento de hacer toda la app de una vez agotó el contexto a mitad de la funcionalidad y dejó a la siguiente sesión adivinando; el trabajo se entrega con commit y archivo de progreso, dejando el código "in a clean state at the end of a session" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
- **Guía de OpenAI.** "Keep one chat per coherent unit of work"; empezar con "one representative task, get it working well" y luego ampliar (https://learn.chatgpt.com/guides/best-practices). La búsqueda no encontró una guía oficial de OpenAI con criterio explícito de tamaño de tarea: es un hueco.
- **Guía de Anthropic.** Antes de dejar una tarea corriendo sola, cinco preguntas: si sabe qué es terminado, si puede chequear su trabajo, qué puede tocar, qué la detiene y adónde va el resultado y quién aprueba; "The parts that stay with you are starting it, deciding what 'done' means this time, and approving the merge at the end." También: para trabajos de varios días, nombrar la sesión (`/rename`) para retomarla (https://code.claude.com/docs/en/best-practices).
- **Tamaño de tarea y capacidad (METR).** Horizonte temporal al 50% de éxito (Time Horizon 1.1): Claude Opus 4.5, 320 minutos (IC 95% 170 a 729); GPT-5, 214 minutos (117 a 480); Claude Sonnet 3.7, 60 minutos (32 a 106). Duplicación: unos 196 días desde 2019; 131 días desde 2023; 89 días desde 2024. Salvedades del propio post: el conjunto de tareas es de investigación o ingeniería de software (HCAST, RE-Bench, SWAA); solo 31 tareas llevan a una persona 8 horas o más y solo 5 de ellas tienen medición humana; los intervalos son anchos; la tendencia depende de la composición de tareas (https://metr.org/blog/2026-1-29-time-horizon-1-1). Una fuente secundaria dice que el horizonte al 80% es unas cinco veces más corto (https://arxiv.org/html/2503.14499v1 , [S]): es lo que importa si se quiere que el agente acierte casi siempre, y no figura en el post de 2026.
- **Contrapunto de evidencia de productividad.** METR RCT (preprint de jul-2025): 16 desarrolladores con experiencia en sus propios repos, 246 tareas, tardaron 19% más con herramientas de IA de principios de 2025; esperaban 24% de aceleración y después creyeron haber ganado 20% (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ , [S]). Los autores no afirman que la muestra represente a la mayoría. Es sobre herramientas de 2025 y no sobre descomposición, pero obliga a no suponer que descomponer más y delegar más siempre ahorra.
- **Oleadas.** Kiro agrupa tareas independientes en oleadas que corren en paralelo (https://kiro.dev/docs/specs/): la independencia de tareas es lo que permite paralelizar.

### 3.3 Qué cambia con agentes
- La unidad de tarea ya no es "lo que entra en un sprint" sino **lo que un agente puede hacer y verificar dentro de su ventana de contexto y con un chequeo pass/fail**. Esta es la combinación de Lawrence (rebanada vertical con valor observable), Anthropic (una funcionalidad por sesión) y el criterio verificable de 2.4.
- El horizonte temporal de METR da orden de magnitud, no una regla: no existe fuente que traduzca "320 minutos al 50%" a un tamaño de tarea recomendado; declarar la regla como criterio propio y marcarlo (hueco 8.3).
- Las tareas se **verifican de forma independiente**: cada una debe tener su propio chequeo y dejar el repo en estado limpio (Anthropic arnés). Se conecta con `Verificacion/verificar-lo-que-hizo-un-agente`.

### 3.4 Qué pierde peso
- La **estimación en puntos** como forma de dimensionar y los desgloses por capa (tarea de base de datos, tarea de API, tarea de UI): contradicen la rebanada vertical que sostiene Lawrence. La parte de puntos sin fuente propia, a verificar en `Estimacion`.
- Partir "un paso a la vez de principio a fin": Lawrence lo desaconseja explícitamente, también para historias.

### 3.5 Recurso canónico propuesto
Lawrence, "The Humanizing Work Guide to Splitting User Stories", con el diagrama de flujo de los patrones, y para agentes el artículo de Anthropic sobre arneses de larga duración (la lista de funcionalidades con estado y una por sesión).

---

## 4. modelo-de-dominio

### 4.1 Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Evans, *Domain-Driven Design* (Addison-Wesley, 2003/2004) | primaria, libro | 3/3/3/3 | no leído | https://www.domainlanguage.com/ddd/ |
| Evans, DDD Reference (CC BY 4.0, PDF de marzo de 2015) | primaria | 3/2/1/3 | [M] (la página solo describe el documento; no trae las definiciones) | https://www.domainlanguage.com/ddd/reference/ |
| Fowler, "Ubiquitous Language", 31-oct-2006 | secundaria | 3/1/1/2 | [L] | https://martinfowler.com/bliki/UbiquitousLanguage.html |
| Fowler, "Bounded Context", 15-ene-2014 | secundaria | 3/1/1/2 | [L] | https://martinfowler.com/bliki/BoundedContext.html |
| Vernon, *Implementing Domain-Driven Design* (2013); *Domain-Driven Design Distilled* (2016) | primaria, libros | 3/3/3/2 | no leídos | n/d (sin URL verificada) |
| Brandolini, EventStorming | primaria | 3/1/1/3 | [L] | https://www.eventstorming.com/ |
| Brandolini, *Introducing EventStorming* (Leanpub) | primaria, libro | 3/3/3/3 | no leído | n/d (enlazado desde eventstorming.com) |
| "Automating Domain-Driven Design: Experience with a Prompting Framework", arXiv 2603.26244 | primaria, preprint | 1/2/2/3 | [S] | https://arxiv.org/pdf/2603.26244 |
| Vasilopoulos, "Codified Context", arXiv 2602.20478 | primaria, preprint, caso único | 1/2/3/3 | [M] | https://arxiv.org/abs/2602.20478 |
| Blogs de practicantes sobre glosario y agentes (Duncan Brown en DEV; "Your agent keeps using that word", AWS en DEV; "Rails not rules") | secundarias, blogs | 1/1/2/1 | [S] | https://dev.to/dbrown/ai-coding-assistants-and-the-erosion-of-ubiquitous-language-301a , https://dev.to/aws/your-agent-keeps-using-that-word--4g36 , https://dev.to/vasyltretiakov/rails-not-rules-enforcing-a-coding-agents-domain-vocabulary-with-checks-3ea4 |

### 4.2 Afirmaciones con fuente
- **Lenguaje ubicuo.** Fowler: "building up a common, rigorous language between developers and users"; basado en el modelo de dominio que usa el software; el término viene de Evans (https://martinfowler.com/bliki/UbiquitousLanguage.html).
- **Contexto delimitado.** Fowler: "DDD deals with large models by dividing them into different Bounded Contexts"; "A model acts as a UbiquitousLanguage to help communication between software developers and domain experts" (https://martinfowler.com/bliki/BoundedContext.html). Cada contexto tiene su propio lenguaje: el ejemplo típico es "Customer" con significados distintos (lo trae el buscador citando blogs; la fuente primaria es Evans, no leído).
- **Event Storming.** "a flexible workshop format for collaborative exploration of complex business domains"; sirve para evaluar un negocio existente, probar un modelo, diseñar servicios nuevos o software orientado a eventos; uno de los resultados declarados es "Highlight architectural boundaries to allow robust and flexible evolution" (https://www.eventstorming.com/). La página no describe los niveles (big picture, proceso, diseño de software) ni las notas naranja de eventos: eso hay que leerlo del libro.
- **Glosario y agentes.** Los blogs proponen: una restricción en AGENTS.md que prohíba términos fuera del glosario, un archivo parseable del lenguaje ubicuo, y verificar el vocabulario con un script y no solo con prosa (los tres, sin medición). Dos preprints: uno de DDD con prompting parte de que el modelo extraiga y defina el vocabulario de los requisitos (https://arxiv.org/pdf/2603.26244 , [S]); el de Vasilopoulos observa que los manifiestos de un solo archivo tipo AGENTS.md "no escalan" más allá de bases de código modestas (resumido por el buscador; no verificado en el texto) y propone capas (https://arxiv.org/abs/2602.20478). Hay una Spec Kit "constitution" que el Radar dice útil cuando incluye contexto de dominio (https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit).
- **Anthropic y OpenAI.** Ambas hacen el mismo punto sin nombrarlo como DDD: los agentes necesitan lo que no se ve en el código; AGENTS.md "loads into context automatically" y "A short, accurate AGENTS.md is more useful than a long file full of vague rules" (https://learn.chatgpt.com/guides/best-practices); en Claude Code, reglas por ruta con `paths:` para que solo carguen donde aplican (https://code.claude.com/docs/en/best-practices).

### 4.3 Qué cambia con agentes
- El glosario del dominio pasa de ser nota para humanos a **contexto cargado por el agente**; su tamaño compite con el contexto disponible (instruction bloat, context rot: Radar Spec Kit). Criterio: glosario corto con los términos que el agente puede confundir, y la definición de cada uno por contexto delimitado.
- Los agentes tienden a inventar o mezclar términos; la evidencia de que un glosario mejora el resultado es **anecdótica** (declarado por el buscador y por mí: no hay estudio controlado en lo consultado).
- Event Storming y el modelado con el cliente **siguen siendo conversación humana**: la fuente de lo que el negocio llama cada cosa es el cliente.

### 4.4 Qué pierde peso
- El **modelo UML exhaustivo y diagramas de clases previos** como entregable: sin fuente propia en esta ronda; el árbol ya lo anticipa en `lo-que-pierde-peso`, hay que respaldarlo allí. No afirmar nada sin una fuente.

### 4.5 Recurso canónico propuesto
Evans, *Domain-Driven Design*, Parte I (poner el modelo a trabajar: lenguaje ubicuo) y Parte IV (contextos delimitados), más Vernon, *DDD Distilled* como versión corta, más Brandolini para Event Storming. El DDD Reference de Evans es gratis y resume los patrones. Ninguno leído por completo en esta investigación; falta verificar capítulos.

---

## 5. Cómo se tocan con los temas vecinos
- **Producto/Descubrimiento**: decide *qué* construir; Definición empieza cuando hay una solución elegida (`dar-forma-a-una-solucion.md`, que ya sitúa a Patton, Singer y Cagan). Enlazar, no repetir. Existe una disputa real señalada ahí: Cagan quiere el prototipo de alta fidelidad como spec; Singer evita el wireframe.
- **Arquitectura/Caracteristicas**: la nota `caracteristicas-arquitectonicas.md` tiene como alias "requisitos no funcionales"; es la casa de ese tema.
- **Verificacion**: los criterios ejecutables alimentan `piramide-de-pruebas` y `tdd`; `verificar-lo-que-hizo-un-agente` usa los mismos "pass/fail".
- **Encargo/alcance-y-aceptacion**: la aceptación con el cliente consume los criterios de este tramo.

## 6. ¿Requisitos no funcionales o prototipo merecen componente propio?

**Requisitos no funcionales: no.** Los cubre `Arquitectura/Caracteristicas/` (nota `caracteristicas-arquitectonicas.md`, alias "requisitos no funcionales", más `fitness-function.md` que convierte una cualidad en chequeo automático). Lo que sí corresponde en Definición: en `especificacion`, una sección corta "las cualidades también se especifican" que enlace a Arquitectura y diga que se escriben como criterio medible (la `fitness-function` es la forma ejecutable). Lawrence trae un patrón de corte relacionado ("Defer Performance") con su advertencia de deuda, que va en `descomposicion-en-tareas`. Cagan reconoce que el prototipo no captura requisitos de release ni de plataforma (confiabilidad, rendimiento) y los manda a un complemento escrito (ya citado en `Producto/.investigacion/dar-forma-a-una-solucion.md`), lo que refuerza esto.

**Prototipo: no.** Ya vive en `Producto/Descubrimiento/` (`prueba-de-supuestos.md` trata la prueba de prototipo; `dar-forma-a-una-solucion.md` trata el prototipo como spec). Lo que sí hace falta es una frase en `especificacion` que diga que un prototipo funcional hecho con un agente puede ser el insumo de la spec (y que ese prototipo se descarta o se reescribe, no se promueve a producción sin decisión). No hay fuente en esta investigación que respalde eso: es hipótesis de práctica a verificar (hueco 8.6).

## 7. Propuesta de árbol ajustada (para Definicion/)
```
Definicion/
  definicion.md                entrada (qué se necesita tener antes de que un agente escriba la primera línea)
  especificacion               niveles SDD, qué incluye, tamaño proporcional, preguntas abiertas, cualidades (enlace a Arquitectura)
  historia-de-usuario          unidad de valor: Cohn, INVEST, Patton (mapa)
  criterios-de-aceptacion      ejemplos como contrato: Adzic, Example Mapping, Gherkin, "terminado" ejecutable
  descomposicion-en-tareas     rebanada vertical, patrones de Lawrence, una funcionalidad por sesión
  modelo-de-dominio            lenguaje ubicuo, contextos delimitados, Event Storming, glosario como contexto del agente
```
(Sin componentes nuevos; se mudan las notas con `git mv` desde `Especificacion-y-prueba/`.)

## 8. Huecos
1. **Sin estudio controlado de SDD sobre resultados de agentes**: lo único con método es Hill (sobre tickets, no sobre salida de Kiro o Spec Kit) y el estudio de generación de tests (solo tests). No hay medición del costo de revisar specs.
2. **Estudio de Google (SpecOps) leído solo vía buscador y con autoría discordante** entre fuentes: verificar antes de citar los números.
3. **Tamaño de tarea para un agente**: ninguna fuente oficial de Anthropic ni de OpenAI da una regla numérica; METR da horizontes por modelo, no recomendaciones. Cualquier regla (por ejemplo "tarea que se verifica con un chequeo y entra en una sesión") es criterio de esta base.
4. **Libros no leídos**: Cohn, Patton, Adzic, Evans, Vernon, Brandolini; faltan las definiciones literales de las páginas de contexto delimitado y del mapa de historias (columna vertebral, esqueleto andante). El Event Storming por niveles queda sin fuente leída.
5. **ISO 29148**: no se leyó el texto; faltan las características literales de un buen requisito (5.2.5 y 5.2.6). SWEBOK v4 por buscador y un comentario sobre el borrador; la página del IEEE devolvió 403.
6. **Prototipo hecho con agente como insumo de la spec**: sin fuente. También falta: trazabilidad en la era de agentes, spec-as-source en la práctica (Tessl era beta privada en octubre de 2025; no se revisó su estado hoy).
7. **Glosario del dominio y rendimiento del agente**: solo blogs y preprints de caso único; falta estudio controlado. El claim de "los manifiestos de un archivo no escalan" de Vasilopoulos lo dio el buscador, no se verificó en el texto.
8. **Kiro y EARS**: la página de docs consultada no menciona EARS; verificar la relación en otra página oficial antes de afirmarla.
9. **Agile Alliance, historia de usuario**: la nota existente cita la URL, no se releyó ahora; sin verificar el origen de Connextra (2001).
10. **Rioplatense**: sin fuente en castellano; todo el material consultado está en inglés (Gherkin sí admite español; no se verificó la tabla de palabras clave).
