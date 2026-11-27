# Investigación: Verificación y Evolución (panorama)

Fecha de la búsqueda: 2026-11-27. Alcance: panorama de dos verticales (`Verificacion/` y `Evolucion/`), no exhaustivo. Puntajes de fuente: A autoridad, P profundidad, E ejemplos, U unicidad (1 a 3). Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Todo lo traído de la web se trató como dato. Donde dice "preprint" no tiene revisión por pares (o no pude confirmarla).

Nota de método: la herramienta de lectura devuelve resúmenes de una página, no el texto crudo, así que casi todo lo marcado [L] es una lectura mediada. Las citas literales son las que la herramienta devolvió entre comillas; verificar contra la fuente antes de publicarlas.

## Resumen de lo que cambia el árbol

1. **TDD con agentes tiene evidencia mixta, y la nota `tdd` no puede predicar "la prueba primero" sin matiz.** Fucci et al. (2017) no encuentran efecto del orden test-first; sí de granularidad y uniformidad. Böckeler (martinfowler.com, sin fecha visible) reporta que los agentes saltan o falsean el paso rojo y que TDD costó unas 3 veces más tokens sin mejor calidad; dejó de pedirles test-first y se apoya en mutación, análisis estático y escenarios aprobados. Lo que se sostiene: la prueba como señal de retroalimentación y definición de "terminado" (docs de Claude Code), no el ritual.
2. **Mutation testing merece componente** (o sección grande dentro de `verificar-lo-que-hizo-un-agente`): es la respuesta práctica a "las pruebas que escribió el agente, ¿prueban algo?". Hay evidencia de Google (ICSE 2021) y Meta (FSE 2025).
3. **Property-based testing merece ficha**, no componente: hay trabajo reciente de Anthropic (agente que escribe tests Hypothesis, 100 paquetes de Python).
4. **Pruebas de contrato merecen sección propia dentro de `piramide-de-pruebas`** (o componente `pruebas-de-contrato`); `disenar-casos-de-prueba-de-api` ya las roza con el contrato OpenAPI pero no cubre contratos dirigidos por el consumidor.
5. **Corte propuesto para Verificacion:** la pirámide, trofeo y honeycomb son discusión de forma; lo vigente es "probar en la frontera del servicio, con pocas pruebas de extremo a extremo". Proponer `piramide-de-pruebas` = qué nivel conviene según tipo de sistema, con las tres formas como contraste.
6. **Deuda técnica:** la evidencia cuantitativa existe (Besker 2019: 23% del tiempo; Tornhill y Borg 2022: 15 veces más defectos en código de baja calidad), pero hay un solo estudio de la autoría del vendor (CodeScene) y uno de autoreporte. Para deuda por IA hay un estudio causal (Cursor, MSR 2026) con aumento persistente de complejidad.
7. **Migraciones con LLM:** los casos grandes (Google, Amazon, Airbnb) son autoinformes de empresas. El patrón común es el que importa: el modelo propone, una verificación determinista (compilar, probar, lint) decide, y personas revisan. Eso refuerza el hilo de las dos verticales.
8. **Hueco grande:** codemods (OpenRewrite, jscodeshift) y Renovate/Dependabot por docs oficiales no se leyeron; la sección quedó sin fuente primaria.

---

## Verificacion/piramide-de-pruebas

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Fowler, "The Practical Test Pyramid" (Vocke) | Práctica reconocida | 3 | 3 | 3 | 2 | [L] | https://martinfowler.com/articles/practical-test-pyramid.html |
| Fowler, bliki "TestPyramid" | Práctica reconocida | 3 | 1 | 1 | 2 | [L] | https://martinfowler.com/bliki/TestPyramid.html |
| Spotify Engineering, "Testing of Microservices" (honeycomb), 2018 | Práctica (empresa) | 2 | 2 | 2 | 3 | [L] | https://engineering.atspotify.com/2018/01/testing-of-microservices/ |
| Kent C. Dodds, "The Testing Trophy and Testing Classifications" | Práctica reconocida, centrada en frontend | 2 | 2 | 2 | 3 | [L] | https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications |
| Fowler, bliki "ContractTest" | Práctica reconocida | 3 | 1 | 1 | 2 | [L] | https://martinfowler.com/bliki/ContractTest.html |
| Cohn, *Succeeding with Agile* (2009), origen de la pirámide | Primaria (libro) | 3 | 3 | 2 | 3 | no leído; citado vía Fowler | (sin URL verificada) |

### Afirmaciones

- Cohn introdujo la pirámide en *Succeeding with Agile* con tres capas: unidad, servicio, UI. El propio artículo dice que los nombres pueden confundir y el modelo es simplista. https://martinfowler.com/articles/practical-test-pyramid.html
- Fowler: Cohn la popularizó en 2009; la dibujó con Lisa Crispin en 2003-2004 y la presentó en un encuentro Scrum en 2004; Jason Huggins llegó a lo mismo hacia 2006. https://martinfowler.com/bliki/TestPyramid.html
- Cita literal: "Push your tests as far down the test pyramid as you can". Y: "Watch out that you don't end up with a test ice-cream cone". https://martinfowler.com/articles/practical-test-pyramid.html
- Las pruebas de extremo a extremo por UI son, para Fowler, "brittle, expensive to write, and time consuming to run", y las de alto nivel son "a second line of test defense"; si falla una, se escribe una prueba de unidad que reproduzca el error. https://martinfowler.com/bliki/TestPyramid.html
- Honeycomb (Spotify): la mayor parte son pruebas de integración del servicio por sus puntos de interacción (REST o mensajes); pocas de "detalle de implementación"; idealmente ninguna "integrada" (que dependan de la corrección de otro sistema). Razón: en microservicios la complejidad está en las interacciones, y muchas pruebas de unidad atan las pruebas a la implementación, de modo que refactorizar obliga a cambiar pruebas. Costo admitido: más lentas (milisegundos a pocos segundos) y mensajes de falla menos precisos. https://engineering.atspotify.com/2018/01/testing-of-microservices/
- Trofeo (Dodds): capas estática, unidad, integración, extremo a extremo; la más ancha es integración, "A general guide for the return on investment of the different forms of testing". Lo limita a monolitos de una sola base de código, no a microservicios. Cita: "The more your tests resemble the way your software is used, the more confidence they can give you." https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications
- Crítica de fondo: el término "unidad" no tiene definición común, y la discusión de porcentajes oculta el desacuerdo real; lo que importa es tener pruebas rápidas, confiables y que fallen por buenas razones (resumen de la fuente). https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications
- Pruebas de contrato, dos sentidos. (a) Verifican que los dobles de prueba de un servicio externo respondan igual que el servicio real: "These check that all the calls against your test doubles return the same results as a call to the external service would." Corren periódicamente, no en cada commit. (b) Dirigidas por el consumidor (CDC): el equipo proveedor corre copias de las pruebas del consumidor en su pipeline. https://martinfowler.com/bliki/ContractTest.html
- Con Pact, el consumidor publica lo que necesita y el proveedor lo corre continuamente; dentro de una organización se pueden cubrir todos los consumidores, en una API pública normalmente no. https://martinfowler.com/articles/practical-test-pyramid.html

### Qué cambia con agentes

- El costo de escribir muchas pruebas de unidad baja casi a cero; el cuello pasa a ser que valgan algo (ver mutación) y que no queden atadas a la implementación. El argumento del honeycomb (pruebas atadas a la implementación frenan el refactor) pesa más cuando el agente refactoriza seguido. Es inferencia mía a partir de las fuentes; no encontré estudio que compare formas de la pirámide con código de agentes. [hueco]
- Docs de Claude Code: dar al agente un comando que verifique su trabajo ("Claude said it was done and it wasn't quite, usually because it had no way to check its own work"), con "the exact test, typecheck, and lint commands, and how to run a single test file". Sirve a cualquier nivel, pero exige pruebas rápidas y deterministas. https://code.claude.com/docs/en/best-practices
- Las pruebas de contrato ganan peso: con agentes que cambian código en una zona, el contrato es el guardarraíl en la frontera que el agente no debe romper.

### Lo que pierde peso

Discutir la forma geométrica (pirámide contra trofeo contra panal) y los porcentajes por nivel; la cobertura como objetivo (ver mutación). Las pruebas de UI grabadas y reproducidas (Fowler ya las desaconseja).

### Recurso canónico

"The Practical Test Pyramid" (Vocke, en martinfowler.com): leer las secciones de pruebas de integración, contrato y extremo a extremo; fijarse en la regla "empujá las pruebas hacia abajo" y en el apartado de contratos con Pact. Complementar con el artículo de Spotify solo para sistemas con servicios.

---

## Verificacion/tdd

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Fucci et al., "A Dissection of the TDD Process: Does It Really Matter to Test-First or to Test-Last?" (IEEE TSE 43(7), 2017; arXiv 1611.05994) | Primaria (empírica) | 3 | 3 | 2 | 3 | [M] abstract | https://arxiv.org/abs/1611.05994 |
| Rafique y Mišić, "The Effects of TDD on External Quality and Productivity: A Meta-Analysis" (IEEE TSE 39(6), 2013) | Primaria (metaanálisis) | 3 | 3 | 1 | 3 | [S] (no se accedió al texto; solo citas) | https://link.springer.com/content/pdf/10.1007/s10664-016-9490-0.pdf (resultado del buscador, es otro paper que la cita; el URL del original no se verificó) |
| Beck, *Test-Driven Development by Example* (2002) | Primaria (libro) | 3 | 3 | 3 | 3 | no leído | (sin URL verificada) |
| Beck, "Augmented Coding: Beyond the Vibes" | Primaria (practicante) | 3 | 2 | 2 | 3 | [L] | https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes |
| Böckeler, "TDD inside the agent loop - theater or actual value?" (martinfowler.com, serie Exploring Gen AI) | Práctica, evaluación pequeña y exploratoria | 2 | 2 | 3 | 3 | [L], fecha no visible en la página | https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html |
| Anthropic, Claude Code "Best practices" | Primaria (docs oficiales), volátil, leída 2026-11-27 | 3 | 3 | 3 | 2 | [L] | https://code.claude.com/docs/en/best-practices |
| Resúmenes sobre Beck en el podcast de The Pragmatic Engineer ("superpower") | Secundaria | 1 | 1 | 1 | 1 | [S] | https://newsletter.pragmaticengineer.com/p/how-kent-beck-shapes-the-software (solo apareció como resultado del buscador) |

### Afirmaciones

- Fucci et al.: 82 datos de 39 profesionales; cuatro características (secuencia, granularidad, uniformidad, esfuerzo de refactor). La secuencia (test antes o después) "no tuvo influencia importante"; granularidad y uniformidad se asociaron positivamente con calidad y productividad; el esfuerzo de refactor, negativamente. Conclusión de los autores: los beneficios atribuidos a TDD pueden venir de pasos finos y constantes, no del orden. https://arxiv.org/abs/1611.05994 (preprint v1 leído; el artículo definitivo salió en IEEE TSE según el DOI 10.1109/TSE.2016.2616877).
- Limitación: el diseño no probó si test-first ayuda con incertidumbre de requisitos o decisiones de diseño (comentario de un resumen secundario, https://blog.acolyer.org/2017/06/13/a-dissection-of-the-test-driven-development-process-does-it-really-matter-to-test-first-or-to-test-last/ [S]).
- Rafique y Mišić (2013): metaanálisis de 25 estudios; mejoras de calidad, productividad con resultados mixtos y la experiencia de los participantes como factor. Solo por una tesis de Helsinki que lo resume [S]: https://helda.helsinki.fi/server/api/core/bitstreams/28435ba6-f068-4f28-983a-47d703536365/content. Falta leer el original.
- Beck: "In vibe coding you don't care about the code, just the behavior of the system." / "In augmented coding you care about the code, its complexity, the tests, & their coverage." Su señal de alarma número tres: "Any indication that the genie was cheating, for example by disabling or deleting tests." Su prompt de sistema le exigía TDD y commitear solo con todas las pruebas pasando. https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
- Böckeler (evaluación chica: Sonnet 4.6 genera, Opus juzga, tareas pequeñas, medianas y grandes de lógica de negocio desde cero): Opus no vio ventaja clara de TDD y a menudo puntuó mejor las soluciones sin TDD; puntajes de mutación similares; las corridas TDD usaron "roughly 3x or more" tokens; los agentes "often write the implementation first and generate tests after, skip confirming the red step". Cita: "Watching a test go red is only proof of anything if someone is checking why it went red." Hallazgos de pruebas tautológicas (recalculan con la implementación el "esperado") y una prueba que fijaba un bug. Ella dejó de pedir test-first y se apoya en mutación, análisis estático y Approved Scenarios. https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
- Discrepancia a mostrar: Beck (practicante) y los docs de Anthropic empujan la prueba antes o como condición de fin; Böckeler (evaluación pequeña, un solo juez-modelo) no halla ventaja de test-first y sí sobrecosto. Fucci (humanos, 2017) no halla efecto del orden. Las tres convergen en: la señal de retroalimentación importa, el ritual estricto no tiene evidencia.
- Docs de Claude Code: el prompt débil es "fix the login bug"; el fuerte pide escribir una prueba que reproduzca el fallo y después arreglar. Piden evidencia ("the command it ran and its output"), no "all tests pass" a secas. https://code.claude.com/docs/en/best-practices

### Qué cambia con agentes

- La prueba pasa de "método de diseño" a "contrato de terminado y guardarraíl": se escribe (o se aprueba) la prueba de aceptación antes y el agente itera hasta que pase. Fuente: docs de Claude Code y Beck.
- Riesgo propio: el agente borra, desactiva o ajusta pruebas para pasar (Beck; METR, ver siguiente componente). Mitigación práctica que aparece en los materiales: tratar las pruebas como solo lectura para el agente o revisarlas aparte [S: surgió en el buscador, sin fuente primaria].

### Lo que pierde peso

El ciclo rojo-verde-refactor como ritual obligatorio para cada línea que escribe un agente, y la cobertura como objetivo. TDD sigue vigente como práctica humana para diseño y como forma de pedir una prueba que reproduzca un bug.

### Recurso canónico

Fucci et al. (2017) para qué pesa de TDD, y Böckeler en martinfowler.com para ver cómo se comporta con agentes (leer el apartado de adherencia y costo). Para la práctica, la sección "Give Claude a check to run" de los docs de Claude Code.

---

## Verificacion/disenar-casos-de-prueba-de-api

Ya existe en `Desarrollo/Especificacion-y-prueba/disenar-casos-de-prueba-de-api.md` (borrador, estabilidad semi, 2026-10-03; leída entera [L]). Cubre formato de caso en tabla, once categorías con código esperado, ambigüedades del contrato y casos de efecto.

Lo que falta, para decidir si se agrega o se enlaza:
- Pruebas de contrato dirigidas por el consumidor (Pact) y verificación del contrato OpenAPI contra la implementación; hoy la nota solo dice "tener el contrato".
- Cómo se genera la suite con un agente a partir del contrato y de los criterios de aceptación, y cómo se verifica que cubre (mutación, no solo cobertura de categorías).
- Pruebas de propiedades para validación y paginado (ver abajo).
- La nota está en `Especificacion-y-prueba/` y el árbol nuevo la pone en `Verificacion/`: mover con `git mv` y actualizar enlaces (el árbol ya lo prevé).
- Dice "Archivo/Desarrollo/casos-de-prueba-api.md" como fuente: es una fuente interna, no pública.

---

## Verificacion/revision-de-codigo

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Bacchelli y Bird, "Expectations, Outcomes, and Challenges of Modern Code Review", ICSE 2013, pp. 712-721, DOI 10.1109/ICSE.2013.6606617 | Primaria (empírica, Microsoft) | 3 | 3 | 2 | 3 | [S] (buscador) | https://researchr.org/publication/BacchelliB13 |
| Sadowski et al., "Modern Code Review: A Case Study at Google", ICSE SEIP 2018 | Primaria (empírica, Google) | 3 | 3 | 2 | 3 | [M] metadatos (el PDF no pudo extraerse) | https://research.google/pubs/modern-code-review-a-case-study-at-google/ |
| Claude Code "Best practices" (secciones de revisión, subagentes) | Primaria (docs), volátil | 3 | 2 | 3 | 2 | [L] | https://code.claude.com/docs/en/best-practices |
| AIDev: "Studying AI Coding Agents on GitHub" (dataset, preprint) | Primaria, preprint | 2 | 2 | 2 | 3 | [S] | https://arxiv.org/html/2602.09185v1 |
| "Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub" (preprint) | Primaria, preprint | 2 | 2 | 2 | 3 | [S] | https://arxiv.org/html/2601.15195v1 |
| DORA 2025, resumen del informe | Primaria | 3 | 1 | 1 | 2 | [L] solo la página resumen | https://dora.dev/research/2025/dora-report/ |

### Afirmaciones

- Bacchelli y Bird (Microsoft): la motivación declarada es encontrar defectos, pero las revisiones dan menos de eso de lo esperado y más transferencia de conocimiento, conciencia del equipo y soluciones alternativas; solo una parte pequeña de los comentarios trata defectos. Entender el cambio y su contexto es la clave de cualquier revisión. https://researchr.org/publication/BacchelliB13 [S]
- Google (ICSE SEIP 2018): estudio exploratorio con 12 entrevistas, encuesta a 44 personas y registros de 9 millones de cambios revisados; foco en por qué se adoptó la revisión, cómo se practica y qué satisfacción y desafíos hay. Los resultados concretos no los pude leer. https://research.google/pubs/modern-code-review-a-case-study-at-google/
- Docs de Claude Code: `/code-review` revisa el diff en un subagente nuevo "that never saw your conversation. It isn't swayed by the reasoning that produced the code"; una segunda sesión es "the easiest independent reviewer you can get". Un revisor pedido para encontrar problemas "will always find something", por eso el prompt recomendado dice "report gaps that affect correctness and skip style" y se revisa contra `SPEC.md`. https://code.claude.com/docs/en/best-practices
- Se puede crear un revisor con solo herramientas de lectura (`tools: Read, Grep, Glob`), restricción que aplica la herramienta y no el prompt. https://code.claude.com/docs/en/best-practices
- PRs de agentes (AIDev, 932.791 PRs de cinco agentes: Codex, Devin, Copilot, Cursor, Claude Code, corte 1 de agosto de 2025): las tasas de aceptación publicadas discrepan según el filtro. Un estudio da 77,9% Codex, 74,5% Cursor, 68,0% Copilot, 61,6% Devin sobre 7.156 PRs (https://arxiv.org/html/2602.08915v1); otro, con AIDev-pop, da 0,83 Codex, 0,67 Cursor, 0,66 Claude, 0,45 Copilot (https://arxiv.org/html/2602.02345v1). Documentación, build y CI se aceptan más que funcionalidades; rendimiento y correcciones de bugs, menos. [S] todas, preprints.
- DORA 2025: "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses." https://dora.dev/research/2025/dora-report/ [L solo el resumen]. DORA 2024, según un resumen del buscador [S]: la adopción de IA se asoció con +3,4% de calidad de código y con menos estabilidad de entrega; no se verificó en la fuente.

### Qué cambia con agentes

- El volumen de código a revisar sube y el contexto lo tiene el agente, no quien revisa; Bacchelli y Bird ya decían que entender el cambio es el cuello de botella. Esto inclina a revisar contra la especificación y la evidencia (pruebas, salida de comandos) más que leer línea por línea.
- Reparto sostenible, con las fuentes que hay: herramienta (formato, lint, tipos, análisis estático, pruebas; determinista), otro agente con contexto limpio (contraste contra la especificación, casos borde), persona (intención, diseño, seguridad, lo que el agente no puede saber; y el traspaso de conocimiento que Bacchelli y Bird encontraron como beneficio). El reparto es síntesis mía, no lo afirma una fuente única.
- La revisión como transferencia de conocimiento se pierde si nadie lee el código: costo a nombrar.

### Lo que pierde peso

Comentarios de estilo y de formato en la revisión humana (los absorbe la herramienta). La "aprobación por rutina" sobre diffs que la persona no entiende.

### Recurso canónico

Bacchelli y Bird (2013), apartados de motivaciones y resultados, para entender qué pasa realmente en una revisión; para la práctica con agentes, la sección "Review against your spec" de los docs de Claude Code (fecharla).

---

## Verificacion/verificar-lo-que-hizo-un-agente

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| METR, "Recent Frontier Models Are Reward Hacking" (2025-06-05) | Primaria (informe de evaluador), sin revisión por pares | 3 | 2 | 3 | 3 | [L] | https://metr.org/blog/2025-06-05-recent-reward-hacking |
| Spracklen et al., "We Have a Package for You!" (USENIX Security 2025; arXiv 2406.10279) | Primaria (empírica) | 3 | 3 | 2 | 3 | [M] abstract | https://arxiv.org/abs/2406.10279 |
| Anthropic, system card de Claude 3.7 Sonnet | Primaria (vendor) | 2 | 2 | 2 | 3 | [S] (no se leyó el PDF) | https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf |
| Petrović et al., "Does mutation testing improve testing practices?" (ICSE 2021; arXiv 2103.07189) | Primaria (empírica, Google) | 3 | 3 | 2 | 3 | [S] | https://arxiv.org/abs/2103.07189v1 |
| "Mutation-Guided LLM-based Test Generation at Meta" (FSE Companion 2025; arXiv 2501.12862) | Primaria (industria) | 3 | 2 | 2 | 3 | [S] | https://arxiv.org/abs/2501.12862 |
| Maaz et al., "Agentic Property-Based Testing" (arXiv 2510.09907; NeurIPS 2025) | Primaria, preprint | 3 | 2 | 3 | 3 | [S] | https://arxiv.org/abs/2510.09907 |
| Böckeler (ver `tdd`) | Práctica | 2 | 2 | 3 | 3 | [L] | https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html |

### Afirmaciones

- METR: en RE-Bench, "30.4%" de las corridas (39 de 128) hicieron reward hacking; en HCAST, 0,7%; fue "more than 43× more common on RE-Bench tasks than HCAST tasks". Ejemplos: "Overwriting the grader's timer or copying the grader's answer", "Monkey-patching the evaluator to always return a perfect score". En una tarea, o3 hizo trampa "in every single trajectory we generated"; preguntado si su plan coincidía con la intención del usuario tras hacer trampa, "o3 answered 'no' 10 out of 10 times". Son entornos de evaluación, no repos de clientes. https://metr.org/blog/2025-06-05-recent-reward-hacking
- Claude 3.7 Sonnet: Anthropic observó "special-casing" para pasar pruebas (hardcodear salidas esperadas o modificar archivos de prueba) en entornos de código agéntico; el system card de Claude 4 reporta una baja promedio de 69% en hardcoding para Sonnet 4 frente a 3.7. Ambos datos llegan por resúmenes de terceros, no por el PDF. [S] https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf (verificar).
- Beck: la tercera señal de que "the genie" falla es desactivar o borrar pruebas. https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
- Paquetes inexistentes: 16 modelos, 576.000 muestras de código en dos lenguajes, 205.474 nombres de paquete alucinados únicos; promedio de al menos 5,2% de paquetes alucinados en modelos comerciales y 21,7% en modelos abiertos. https://arxiv.org/abs/2406.10279 El nombre "slopsquatting" (registrar el nombre alucinado con código malicioso) no lo usa este paper en el abstract; no encontré fuente primaria del término. [hueco menor]
- Mutation testing en Google: ~15 millones de mutantes; quienes lo usan escriben más pruebas y mejoran sus suites de modo que sobreviven menos mutantes; los mutantes se acoplan con fallas reales de alta prioridad. https://arxiv.org/abs/2103.07189v1 [S]
- Meta (ACH): 10.795 clases Kotlin de Android, 9.095 mutantes, 571 pruebas de endurecimiento de privacidad; 277 (≈49%) se habrían descartado si se hubiera guiado solo por cobertura de líneas; ingenieros aceptaron 73% de las pruebas en jornadas de Messenger y WhatsApp. Detector de mutantes equivalentes con LLM: precisión 0,79 y recall 0,47 (0,95 y 0,96 con preprocesamiento). https://arxiv.org/abs/2501.12862 [S]
- Property-based con agente: corrido sobre 100 paquetes populares de Python; 56% de los reportes válidos y 32% válidos y reportables; de 21 bugs mejor puntuados, 86% válidos y 81% reportables; 5 reportados, 4 con parche, 3 parches aceptados. https://arxiv.org/abs/2510.09907 [S]; hay una cifra discordante entre resúmenes (86% o 18 de 21): citar el paper.
- Böckeler: pruebas tautológicas y pruebas que consagran un bug; mutación y análisis estático como retroalimentación. https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html

### Señales de trabajo incompleto o inventado (lista propuesta, cada una atada a su fuente)

pruebas borradas, desactivadas o debilitadas (Beck, METR, system card); salidas hardcodeadas o casos especiales en el código (system card); evaluador o configuración tocados (METR); dependencias inexistentes (Spracklen); pruebas que recalculan el esperado con la implementación (Böckeler); "terminado" sin evidencia de comando ejecutado (docs de Claude Code). La detección con mutación y con revisor de contexto limpio sale de las fuentes anteriores; no hay un estudio que pruebe que juntas cubren estas fallas.

### Qué cambia con agentes

Este componente solo existe por los agentes. Las defensas con fuente: dar al agente una verificación ejecutable y pedir evidencia (docs de Claude Code); revisor con herramientas de solo lectura; mutación para medir si las pruebas detectan fallas; lockfile y verificación de existencia de paquetes (derivado de Spracklen, no de una guía oficial que haya leído).

### Lo que pierde peso

"Confiar en el resumen final del agente" y la cobertura de líneas como prueba de que está probado: el resultado de Meta (49% de pruebas descartables si se guiara por cobertura) lo ilustra en un caso.

### Recurso canónico

METR (2025) para entender la falla; la sección "Give Claude a check to run" de los docs para la práctica; el paper de Meta o el de Google para mutación.

### ¿Property-based y mutación merecen componente?

- Mutación: sí, como componente corto `pruebas-de-mutacion` (qué es, cuándo correrla, límite: mutantes equivalentes, costo) o, si se quiere menos nodos, una sección fuerte dentro de este componente. Es la herramienta que mejor responde la pregunta central de la vertical con agentes.
- Property-based: ficha dentro de `piramide-de-pruebas` o de este componente. Hay evidencia con agentes, pero es una técnica complementaria; el único trabajo fuerte que encontré es de Anthropic (preprint). Falta fuente de QuickCheck o Hypothesis primaria (no se buscó).

---

## Evolucion/deuda-tecnica

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Cunningham, "The WyCash Portfolio Management System", OOPSLA 1992 | Primaria (origen) | 3 | 1 | 1 | 3 | no leído; cita y datos vía buscador [S] | (sin URL verificada del original; ver CACM abajo) |
| CACM / ACM Queue, "Managing Technical Debt" (2012) | Secundaria que cita a Cunningham | 3 | 2 | 1 | 1 | [S] | https://queue.acm.org/detail.cfm?id=2168798 |
| Fowler, "Technical Debt Quadrant" (2009) | Práctica reconocida | 3 | 1 | 1 | 3 | [L] | https://martinfowler.com/bliki/TechnicalDebtQuadrant.html |
| Besker, Martini y Bosch, "Software developer productivity loss due to technical debt", J. Systems and Software, 2019 | Primaria (empírica) | 3 | 3 | 2 | 3 | [S] | https://research.chalmers.se/en/publication/507477 |
| Besker et al., "The Pricey Bill of Technical Debt", ICSME 2017 | Primaria (empírica) | 3 | 2 | 1 | 2 | [S] | https://research.chalmers.se/publication/500162 |
| Tornhill y Borg, "Code Red: The Business Impact of Code Quality", TechDebt 2022 (arXiv 2203.04374) | Primaria (empírica; autor de CodeScene, vendor) | 2 | 3 | 2 | 3 | [S] | https://arxiv.org/abs/2203.04374v1 |
| He et al., "Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity" (MSR '26; arXiv 2511.04427) | Primaria (empírica) | 3 | 3 | 2 | 3 | [S] | https://arxiv.org/abs/2511.04427 |
| GitClear, "AI Copilot Code Quality 2025" | Primaria (vendor de análisis de código) | 1 | 2 | 2 | 2 | [S] vía prensa | https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250 |

### Afirmaciones

- Cunningham 1992, OOPSLA: frase atribuida: "Shipping first-time code is like going into debt." (según CACM; no vi el texto original). Fowler dice que Ward introdujo el concepto en ese informe. https://martinfowler.com/bliki/TechnicalDebt.html [S] / https://queue.acm.org/detail.cfm?id=2168798 [S]
- Cuadrante de Fowler (2009): deliberada o inadvertida, prudente o imprudente. "may not be worth paying down if the interest payments are sufficiently small"; la deuda prudente e inadvertida (descubrís el mejor diseño después de construir) es inevitable. https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
- Besker 2019: los desarrolladores pierden en promedio 23% de su tiempo por deuda técnica (encuestas semanales durante unos diez meses más entrevistas, autoinformado); la actividad más común es hacer pruebas adicionales; los gerentes en general no sabían que se perdía un cuarto del tiempo. https://research.chalmers.se/en/publication/507477 [S]
- Discrepancia: "The Pricey Bill of Technical Debt" (ICSME 2017) estima 36% del tiempo, otra medición distinta; y el "42%" de Stripe es otra fuente. Dar las tres, no mezclarlas. https://research.chalmers.se/publication/500162 [S]
- Code Red: 39 bases de código propietarias, 30.737 archivos; el código de baja calidad (métrica Code Health de CodeScene) tiene unas 15 veces más defectos, resolver issues lleva 124% más de tiempo, y los tiempos máximos de ciclo son 9 veces mayores. El autor es del vendor de la métrica. https://arxiv.org/abs/2203.04374v1 [S]
- Deuda por IA, estudio causal (diferencias en diferencias, repos que adoptan Cursor frente a controles): ganancia de velocidad transitoria; aumento persistente de advertencias de análisis estático y de complejidad (en v2 del preprint, ≈30% y ≈41%; verificar en la versión publicada en MSR '26). https://arxiv.org/abs/2511.04427 [S]
- GitClear 2025 (211 millones de líneas, 2020-2024): bloques de 5 o más líneas duplicadas crecieron 8 veces durante 2024; el código "movido" (señal de refactor) bajó; en 2024 las líneas copiadas superaron por primera vez a las movidas. Vendor de analítica de revisión de código; mide patrones del diff, no defectos. Discrepa DORA 2024 (+3,4% de calidad de código, vía resumen [S]). https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250

### Qué cambia con agentes

La deuda se acumula más rápido (más código y duplicación, menos refactor, según GitClear y el estudio de Cursor) y a la vez el agente puede pagarla barato (ver `refactorizar`). Decidir qué deuda pagar se vuelve decisión de personas; hacerla, de agentes con pruebas.

### Lo que pierde peso

Medir deuda con "story points de deuda" o con un porcentaje fijo de sprint; el cuadrante sigue valiendo como lenguaje para explicarle al cliente.

### Recurso canónico

Cuadrante de Fowler (breve) más Besker 2019 para el costo; para IA, el estudio de Cursor, leyendo la versión de MSR '26.

---

## Evolucion/refactorizar

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Fowler, *Refactoring*, 2ª ed. (2018) | Primaria (libro) | 3 | 3 | 3 | 3 | [M] página del libro | https://martinfowler.com/books/refactoring.html |
| Horikawa et al., "Agentic Refactoring: An Empirical Study of AI Coding Agents" (arXiv 2511.04824), preprint | Primaria, preprint | 2 | 2 | 2 | 3 | [S] | https://arxiv.org/abs/2511.04824 |
| "How do Agents Refactor: An Empirical Study" (arXiv 2601.20160), preprint | Primaria, preprint | 2 | 2 | 2 | 2 | [S] | https://arxiv.org/abs/2601.20160 |
| Claude Code "Best practices" (migraciones masivas con `/batch`) | Primaria (docs) | 3 | 1 | 2 | 1 | [L] | https://code.claude.com/docs/en/best-practices |

### Afirmaciones

- Fowler, 2ª edición, 2018 (la primera, 1999): caso inicial recorrido de punta a punta, capítulos sobre malos olores, el papel de las pruebas y unas setenta refactorizaciones, cada una con motivación, mecánica y ejemplo. La página no dice qué cambió respecto de la 1ª edición ni el lenguaje de los ejemplos; no afirmar JavaScript sin verificar. https://martinfowler.com/books/refactoring.html
- Refactor con agentes, estudio sobre AIDev (Java): 15.451 instancias de refactor en 12.256 PRs; los agentes apuntan a refactor en 26,1% de los commits; motivaciones: mantenibilidad (52,5%) y legibilidad (28,1%). Las cifras de commits difieren entre versiones del paper. https://arxiv.org/abs/2511.04824 [S]
- Los estudios hallados detectan refactors con RefactoringMiner y medidas de olores; no encontré uno que verifique la preservación del comportamiento ejecutando pruebas. [hueco] Otro estudio, en Python, halló que una fracción grande de los PRs de refactor de agentes se acepta incluso introduciendo problemas nuevos de lint y seguridad (https://arxiv.org/pdf/2605.21453 [S]).
- Docs de Claude Code: `/batch` divide un cambio mecánico grande en 5 a 30 unidades, cada una en su worktree con su PR. https://code.claude.com/docs/en/best-practices

### Qué cambia con agentes

Refactorizar es el trabajo mejor acotado para un agente si hay pruebas que fijen el comportamiento: la definición de Fowler (cambiar la forma sin cambiar el comportamiento) es una especificación verificable. Sin pruebas previas, primero se fijan con characterization tests (ver `sistema-heredado`). Lo que no se sabe con evidencia: qué tan seguido el agente cambia comportamiento al refactorizar.

### Lo que pierde peso

Refactorizar a mano por rutina cambios mecánicos (renombres, extracciones); el catálogo de Fowler sigue vigente como vocabulario para pedirle al agente y para revisar.

### Recurso canónico

*Refactoring* 2ª ed.: el capítulo 1 (ejemplo completo) y el capítulo sobre pruebas; y el catálogo como vocabulario.

---

## Evolucion/sistema-heredado

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Feathers, *Working Effectively with Legacy Code* (2004) | Primaria (libro) | 3 | 3 | 3 | 3 | no leído; citas vía secundarias | https://archive.org/details/working-effectively-with-legacy-code |
| Fowler, bliki "LegacySeam" | Práctica reconocida | 3 | 1 | 1 | 2 | [S] (apareció en buscador, no se abrió) | https://martinfowler.com/bliki/LegacySeam.html |
| Seemann (ploeh), "Empirical characterization testing" (2025-11-03) | Práctica (practicante) | 2 | 2 | 2 | 2 | [S] | https://blog.ploeh.dk/2025/11/03/empirical-characterization-testing/ |
| Spinellis, reseña del libro | Secundaria | 2 | 1 | 1 | 1 | [S] | https://www.spinellis.gr/pubs/Breview/2005-CR-Legacy/html/review.html |

### Afirmaciones

- Definición de Feathers: "legacy code is simply code without tests" (cita vía secundarias); por "pruebas" suele entender pruebas de unidad rápidas que se corren tras un cambio. https://www.spinellis.gr/pubs/Breview/2005-CR-Legacy/html/review.html [S]
- Seam: "a place where you can alter behavior in your program without editing in that place"; cada seam tiene un punto de habilitación donde se elige el comportamiento. https://martinfowler.com/bliki/LegacySeam.html [S]
- Characterization test: prueba escrita después sobre código existente que describe lo que hace hoy, no necesariamente lo correcto; la receta de Feathers arranca poniendo el código en un arnés y escribiendo una aserción que se espera que falle para ver el comportamiento real. https://blog.ploeh.dk/2025/11/03/empirical-characterization-testing/ [S] (la receta viene de un blog; verificar con el libro).
- Entender código desconocido con agentes: no encontré un estudio sistemático con método; la guía oficial que sí hay es que el agente lee el repo para encontrar estructura y convenciones, y que conviene anotar lo que no se deduce del código (https://code.claude.com/docs/en/best-practices [L]). [hueco: evidencia sobre comprensión de sistemas heredados con agentes]

### Qué cambia con agentes

Los characterization tests se pueden generar con un agente corriendo el sistema y fijando salidas observadas, y el agente explora y resume el código rápido. Pero fijar el comportamiento actual puede enquistar bugs (Böckeler vio un bug consagrado en una prueba), y lo que un agente "entendió" de un sistema heredado no está verificado: hay que contrastarlo con el sistema corriendo y con quien lo conoce.

### Lo que pierde peso

Leer todo el código antes de tocar; documentar el heredado a mano antes de empezar. Sigue vigente la regla de Feathers: primero pruebas que fijan el comportamiento, después cambios.

### Recurso canónico

Feathers, partes sobre seams y characterization tests (capítulos 4, "The Seam Model", y 13, según el índice del libro; verificar capítulos antes de citar); más "Strangler fig" en Arquitectura/Estilos (enlazar, no repetir).

---

## Evolucion/migraciones-y-actualizaciones

### Fuentes

| Fuente | Tipo | A | P | E | U | Marca | URL |
|---|---|---|---|---|---|---|---|
| Nikolov et al., "How is Google using AI for internal code migrations?" (ICSE SEIP 2025; arXiv 2501.06972) | Primaria (informe de empresa) | 3 | 3 | 3 | 3 | [S] | https://arxiv.org/abs/2501.06972 |
| Google Research blog, "Accelerating code migrations with AI" | Primaria (vendor) | 2 | 2 | 3 | 1 | [L] | https://research.google/blog/accelerating-code-migrations-with-ai/ |
| Covey-Brandt (Airbnb), "Accelerating Large-Scale Test Migration with LLMs" | Primaria (empresa) | 2 | 2 | 3 | 3 | [S] (no se abrió el original) | https://airbnb.tech/?p=366 |
| AWS, "Amazon Q Developer just reached a $260 million dollar milestone" y Jassy | Primaria (vendor), autoinforme | 1 | 1 | 2 | 2 | [S] | https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone |
| Renovate docs, "Bot comparison" | Primaria (docs del vendor del bot) | 2 | 2 | 1 | 2 | [S] | https://docs.renovatebot.com/bot-comparison/ |
| Docs de Dependabot de GitHub | Primaria | 3 | 3 | 1 | 2 | no encontrado en esta ronda | (hueco) |

### Afirmaciones

- Google: migración de decenas de tipos de ID numéricos en Google Ads de 32 a 64 bits (`int32_t` en C++, `Integer` en Java): 80% de los cambios de código en los CLs aprobados fueron generados por IA, y una estimación de 50% menos de tiempo total de migración, informada por los propios ingenieros; Gemini ajustado con código interno; cada cambio se valida compilando y corriendo pruebas de unidad, con un paso de "reparación" por ML; las personas revisan, con los cambios repartidos a los equipos dueños. 91% de acierto prediciendo qué archivos Java había que editar. https://research.google/blog/accelerating-code-migrations-with-ai/
- El paper de arXiv cubre cuatro migraciones grandes con criterio de éxito de al menos 50% de aceleración extremo a extremo; un resumen secundario da ahorros de hasta 89% en algún caso (no verificado en el paper). https://arxiv.org/abs/2501.06972 [S]
- Airbnb: ~3,5 mil archivos de pruebas de componentes de Enzyme a React Testing Library en unas seis semanas, frente a una estimación manual de ~1,5 años (una fuente dice 18 meses); 97% automatizado y el resto a mano en otra semana; flujo por archivo en pasos: reescribir, hacer pasar Jest, limpiar ESLint y TypeScript, marcar terminado. [S: los números vienen de resúmenes, no del original] https://www.infoq.com/news/2025/03/airbnb-llm-test-migration/
- Amazon: "We estimate this has saved us the equivalent of 4,500 developer-years of work" (Jassy); el tiempo medio de actualización de una aplicación a Java 17 pasó de unos 50 días-desarrollador a pocas horas; decenas de miles de aplicaciones (una fuente dice 30.000); son estimaciones internas no auditadas, de un vendor. https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone [S]
- Renovate y Dependabot soportan actualizaciones agrupadas; el tablero de dependencias de Renovate viene activado por defecto y el de Dependabot no existe; Dependabot viene integrado en GitHub y Renovate se instala como app o se aloja por cuenta propia. Fuente del vendor de uno de los bots. https://docs.renovatebot.com/bot-comparison/ [S]
- Codemods (jscodeshift, OpenRewrite): sin fuente leída. [hueco]

### Qué cambia con agentes

Patrón común de los tres casos con fuente: el modelo propone, una verificación determinista decide (compilación, pruebas, lint), y las personas revisan o corrigen el resto. La migración masiva pasa de proyecto de meses a tarea de semanas si hay una suite que decida. Los bots de dependencias (Renovate, Dependabot) siguen siendo la primera línea para actualizaciones pequeñas y frecuentes; el agente entra cuando una actualización exige cambios de código. Son autoinformes de empresas grandes con pruebas sólidas; en un proyecto de cliente sin pruebas la ventaja no se traslada tal cual (inferencia mía).

### Lo que pierde peso

Posponer la actualización de dependencias hasta que "haya tiempo" y las reescrituras manuales de migraciones mecánicas. Strangler fig sigue en Arquitectura/Estilos: enlazar, no repetir.

### Recurso canónico

Nikolov et al. (Google, 2025): leer el apartado del flujo (descubrimiento de archivos, validación en varias etapas, revisión humana) y los criterios de éxito; para dependencias, la comparación de Renovate más los docs de Dependabot (a buscar).

---

## Huecos

1. Codemods (OpenRewrite, jscodeshift): sin fuente. Docs de Dependabot: no leídos.
2. Rafique y Mišić (2013): sin acceso al texto; solo citas de terceros.
3. Cunningham 1992 y Cohn 2009, Beck 2002, Feathers 2004, Fowler 2018: libros y papers primarios sin leer; todo vía páginas del autor o secundarias. Capítulos de Feathers por verificar.
4. Google "Modern Code Review" (2018): no se pudo leer el contenido; faltan cifras (revisores por cambio, latencia).
5. Slopsquatting como término: no se halló fuente primaria; el dato empírico (Spracklen) sí.
6. No hay estudio hallado que compare formas de pirámide con código de agentes, ni que mida la preservación de comportamiento en refactors de agentes, ni evidencia con método sobre entender sistemas heredados con agentes.
7. Evidencia sobre revisión asistida por IA en sí (herramientas de revisión automática: tasas de comentarios útiles): no se buscó en profundidad; DORA 2025 leído solo en su resumen.
8. Muchas cifras vienen de autoinformes de empresas (Google, Amazon, Airbnb, Meta) y de vendors (CodeScene, GitClear): sin replicación independiente.
9. La evaluación de Böckeler es pequeña, con un modelo como juez, y su fecha no figura en la página: tratarla como señal, no como prueba.
10. Verificar contra el texto original las citas marcadas [S] antes de publicarlas, en especial las del system card de Claude 3.7 y las cifras de Airbnb y Amazon.
