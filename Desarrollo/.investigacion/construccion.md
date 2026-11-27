# Investigación: vertical Construcción (2026-11-27)

Marcas: [L] texto completo, [M] metadatos o abstract, [S] resumen del buscador o secundario. Puntajes 1 a 3: Autoridad / Profundidad / Ejemplos / Unicidad. Todo lo de agentes es volátil y está fechado. Las páginas se leyeron con una herramienta que extrae por pregunta, no con lectura de texto completo; por eso casi todo es [M] y lo marco así cuando un detalle no pude verificarlo.

## 0. Corte propuesto de la vertical

El árbol de ALCANCE.md propone `contexto-del-repositorio`, `agente-de-codigo`, `plantilla-de-proyecto`, `Configuracion/`, `Git/`. El campo coincide en lo general, con ajustes:

1. `contexto-del-repositorio` y `agente-de-codigo` se solapan en una sola cosa: el bucle del agente es el que consume el contexto. Se mantienen separadas, pero `agente-de-codigo` debería cubrir también "darle una forma de verificar" (el hallazgo más fuerte de la doc oficial) y mandar a Verificacion/ el detalle.
2. Faltan dos notas de construcción vigentes: **entorno-reproducible** (dev containers, y su doble uso como sandbox del agente) y **dependencias** (actualización automática con espera y riesgo de paquetes inventados). Estilo y formateo automático no merece nota: se cubre con un párrafo en `contexto-del-repositorio` (lo determinista va a hooks/CI, no a instrucciones) y un enlace a Hook de Git. "Programación en pareja con IA" no es una nota aparte: es un modo de trabajo de `agente-de-codigo`; hay poca evidencia primaria (ver huecos).
3. `Configuracion/` (YAML, Spring Boot, Compose) y `Git/` se mantienen; ver sección 5.

## 1. contexto-del-repositorio

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | Recencia |
|---|---|---|---|---|
| Anthropic, Best practices for Claude Code https://code.claude.com/docs/en/best-practices (la URL vieja anthropic.com/engineering/claude-code-best-practices redirige acá con 308) | primaria | 3/3/3/2 | [M] (51 KB, leí las secciones de CLAUDE.md, verificación, hooks y worktrees) | volátil, leída 2026-11-27 |
| Anthropic, Effective context engineering for AI agents, 2025-09-29 https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | primaria | 3/2/2/2 | [M] | 2025-09-29 |
| agents.md https://agents.md | primaria | 2/1/2/3 | [M] | volátil |
| OpenAI, Codex: AGENTS.md https://learn.chatgpt.com/docs/agent-configuration/agents-md (redirige desde developers.openai.com/codex/guides/agents-md) | primaria | 3/2/3/2 | [M] | volátil |
| Gloaguen, Mündler, Müller, Raychev, Vechev, Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?, arXiv 2602.11988, 2026-02-12 https://arxiv.org/abs/2602.11988 (taller ICLR 2026 MemAgents; sin revisión por pares en la versión leída) | primaria, preprint | 2/2/2/3 | [M] abstract | 2026-02 |
| Thoughtworks Technology Radar vol. 35, "Agent instruction bloat" (Caution; entrada de abril 2026, actualizada 2026-11-04) https://www.thoughtworks.com/en-au/radar/techniques/agent-instruction-bloat | práctica (practicantes reconocidos) | 2/1/2/3 | [M] | 2026-11-04 |
| Claude Code, Skills https://code.claude.com/docs/en/skills | primaria | 3/3/3/2 | [M] (leí 100.000 de 121.124 caracteres) | volátil |

### Afirmaciones

- Qué poner: la doc de Claude Code dice que el archivo "works best when it only holds what Claude couldn't work out from the code itself" y lista cuatro cosas: cómo confirmar el trabajo (comandos exactos de test, typecheck y lint, y cómo correr un solo test), "places where the code is misleading", "decisions that aren't in the repo" y "anything you've had to correct twice already". Recomienda quedar bajo 200 líneas. https://code.claude.com/docs/en/best-practices
- Qué no poner: la tabla de la misma página desaconseja "Describe your architecture and file layout in CLAUDE.md" porque "Claude reads the repo itself". https://code.claude.com/docs/en/best-practices
- Determinista vs. sugerencia: "If something has to happen every time, make it a hook, a deny rule, or a managed setting. CLAUDE.md is for guidelines, and Claude is allowed to decide a guideline doesn't apply." Regla sin excepciones (no leer .env, no tocar migraciones, correr el formateador) va a un hook (`PreToolUse` que sale con código 2). https://code.claude.com/docs/en/best-practices
- Skills como carga bajo demanda: "a skill's body loads only when it's used, so long reference material costs almost nothing until you need it"; se sugiere `SKILL.md` bajo 500 líneas; siguen el estándar abierto Agent Skills (agentskills.io). https://code.claude.com/docs/en/skills
- Formato común: AGENTS.md es "A simple, open format for guiding coding agents", administrado por la Agentic AI Foundation bajo la Linux Foundation, "used by over 60k open-source projects", con más de 20 herramientas (Codex, Cursor, Copilot, Gemini CLI, Jules, Aider, Zed, Windsurf, entre otras). En monorepos "the closest one takes precedence" y "explicit user chat prompts override everything". https://agents.md
- Codex: junta los AGENTS.md desde la raíz del repo hasta el directorio actual, uno por directorio (`AGENTS.override.md` primero), y el límite combinado por defecto es 32 KiB (`project_doc_max_bytes`); lo que excede se descarta. https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Claude Code lee CLAUDE.md, no AGENTS.md (no lo verifiqué en la página leída; la doc de memoria lo aclara y conviene confirmarlo antes de escribir). Este repo ya usa CLAUDE.md.
- Evidencia: el estudio de ETH Zürich/Raychev (arXiv 2602.11988) halla que los archivos de contexto "do not generally improve task success rates" y suben el costo de inferencia "by over 20% on average"; los resúmenes de repositorio, "despite being popular and recommended by model providers, don't help"; son útiles "for specifying non-standard coding practices". Las dos versiones del preprint discrepan en el efecto de los archivos escritos por personas (la v1 dice que mejoran un poco; la posterior, que no mejoran de forma significativa). https://arxiv.org/abs/2602.11988 (la discrepancia viene de la búsqueda [S]; verificar en https://arxiv.org/html/2602.11988v1).
- Práctica: el Radar de Thoughtworks pone "agent instruction bloat" en Caution: los archivos "tend to grow long, contradictory, and stale"; recomienda convertir instrucciones en hooks o checks, reevaluarlas con cada modelo nuevo y borrar las que sobran, y revelar contexto de forma progresiva. La entrada de noviembre cita que Anthropic quitó más del 80% del system prompt de Claude Code sin pérdida medible (dato [S], no lo verifiqué en la fuente de Anthropic). https://www.thoughtworks.com/en-au/radar/techniques/agent-instruction-bloat
- Principio de fondo: context engineering es "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference"; guía: "the smallest possible set of high-signal tokens"; el contexto se degrada al llenarse (context rot); técnicas: recuperación just-in-time, compactación, notas fuera de la ventana, subagentes con contexto limpio. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

### Qué cambia con agentes y qué pierde peso

- Cambia: el repo pasa a tener un lector nuevo; el README para humanos no alcanza. Nace un archivo de instrucciones, skills, hooks y comandos de verificación como parte del código.
- Pierde peso: la documentación de arquitectura "para que se entienda el repo" copiada en el archivo de instrucciones; el archivo largo generado con `/init` sin podar (la evidencia dice que cuesta y no ayuda); los prompts con MAYÚSCULAS y "IMPORTANT" (la doc oficial dice que no arreglan nada y que la regla va a un hook).
- Tensión a nombrar: la doc de Anthropic y el Radar se alinean con el estudio (poco y solo lo no deducible); la práctica común de "archivo grande con resumen del repo" está en contra de las tres fuentes.

### Recurso canónico

La sección "Keep CLAUDE.md short" y "Enforce the rules that can't have exceptions" de https://code.claude.com/docs/en/best-practices, más el abstract de arXiv 2602.11988 como evidencia. Fijarse en: el test "qué no puede deducir el agente del código" y la frontera instrucción/hook.

## 2. agente-de-codigo

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | Recencia |
|---|---|---|---|---|
| METR, Early-2025 AI experienced OS dev study, 2025-07-10 https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | primaria (RCT; paper en arXiv, sin revisión por pares cuando se publicó) | 3/3/2/3 | [M] | 2025-07; la página dice que está desactualizada |
| METR, Uplift update, 2026-02-24 https://metr.org/blog/2026-02-24-uplift-update/ | primaria | 3/3/2/3 | [M] | 2026-02 |
| METR, Measuring AI ability to complete long tasks, 2025-03-19 https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ | primaria | 3/3/2/3 | [M] | 2025-03; el propio METR dice que los datos están reemplazados por Time Horizon 1.1 |
| Google/DORA, 2025 State of AI-assisted Software Development https://dora.dev/dora-report-2025/ ; PDF https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf | primaria | 3/3/2/3 | [M] la página; el PDF no lo leí | 2025 |
| DORA, catálogo de capacidades https://dora.dev/capabilities/ | primaria | 3/2/1/2 | [M] | volátil |
| OpenAI, Why we no longer evaluate SWE-bench Verified, 2026-02-23 https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ | primaria (parte interesada: es un proveedor de modelos) | 2/2/2/3 | [M] | 2026-02 |
| He et al. (CMU), Does AI-Assisted Coding Deliver? (retitulado "Speed at the Cost of Quality"), arXiv 2511.04427; aceptado en MSR '26 según el buscador https://arxiv.org/abs/2511.04427 | primaria, observacional | 2/2/2/3 | [S] | 2025-11 |
| GitClear, AI Copilot Code Quality 2025 (reportado por LeadDev https://leaddev.com/software-quality/how-ai-generated-code-accelerates-technical-debt y TechCrunch https://techcrunch.com/2025/02/21/report-ai-coding-assistants-arent-a-panacea) | primaria de un proveedor con interés (vende análisis de código); no leí el informe | 1/2/2/2 | [S] | 2025-02 |
| Anthropic, Claude Code best practices (ver sección 1) | primaria | 3/3/3/2 | [M] | volátil |
| Thoughtworks Radar vol. 34, abril 2026 https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2026/04/tr_technology_radar_vol_34_en.pdf y Spec Kit https://www.thoughtworks.com/en-au/radar/languages-and-frameworks/github-spec-kit | práctica | 2/2/2/2 | [S] (no abrí el PDF) | 2026-04 |
| Kent Beck, Augmented Coding: Beyond the Vibes https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes | practicante reconocido | 2/2/2/3 | [S] | 2025 |

### Afirmaciones

- RCT de METR (publicado 2025-07-10): 16 desarrolladores experimentales de código abierto, 246 issues reales asignados al azar a "IA permitida" o no, repos de más de 22k estrellas y más de 1M de líneas. Con IA tardaron 19% más; esperaban antes un 24% de aceleración y después seguían creyendo que habían ido un 20% más rápido. Limitaciones que enumeran los autores: muestra chica, no representa la mayoría del desarrollo, mejor uso (prompting, andamiaje) podría dar aceleración, efectos de aprendizaje con Cursor más allá de ~50 horas. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Actualización de METR (2026-02-24), 57 desarrolladores, 143 repos, más de 800 tareas: desarrolladores que volvían, -18% de tiempo (IC -38% a +9%); nuevos, -4% (IC -15% a +9%); referencia del estudio anterior +19% (IC +2% a +39%) (negativo = más rápido con IA). METR advierte efectos de selección (entre 30% y 50% omitió tareas porque no quería hacerlas sin IA; el pago bajó de 150 a 50 USD/hora), concluye que el estimado es "a poor proxy" y que el número real probablemente es mayor que el medido, y que está rediseñando el estudio. No hay un número vigente confiable. https://metr.org/blog/2026-02-24-uplift-update/ Ojo: blogs secundarios reportan cifras que discrepan en signo y sentido; usar solo la fuente de METR.
- Horizonte temporal: la duración de tareas que agentes de frontera completan con 50% de fiabilidad "doubling approximately every 7 months for the last 6 years" (2025-03-19); ajustando solo 2024-2025 la estimación se acelera; SWE-bench Verified muestra una duplicación en menos de 3 meses, que los autores atribuyen a cómo se estimó el tiempo humano. La página dice que estas cifras son las de la publicación original. https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
- DORA 2025: "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses"; el mayor retorno sale del sistema organizacional más que de la herramienta. https://dora.dev/dora-report-2025/ Según el buscador [S]: 90% usa IA, 30% confía poco o nada en el código generado, casi 5.000 profesionales, y la adopción ahora mejora el throughput pero también la inestabilidad (esto último viene de comentarios secundarios; confirmar en el PDF antes de escribirlo como cita). El catálogo de DORA marca con "AI" siete capacidades: AI-accessible internal data, Clear and communicated AI stance, Healthy data ecosystems, Platform engineering, User-centric focus, Version control, Working in small batches (lista inferida por mí a partir de las etiquetas del catálogo, no un modelo declarado). https://dora.dev/capabilities/
- SWE-bench: el 2026-02-23 OpenAI dejó de reportar SWE-bench Verified y recomienda a otros hacer lo mismo: de 138 problemas auditados (los que o3 no resolvía consistentemente, 27,6% de los 500), 59,4% tenían tests o descripciones con problemas materiales, y todos los modelos de frontera probados reprodujeron parches originales o detalles textuales de algunas tareas (contaminación). Recomienda SWE-bench Pro. https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ Un resultado del buscador [S] agrega que OpenAI estima ~30% de tareas rotas en SWE-bench Pro, sin fecha confirmada. Consecuencia para las notas: no citar puntajes de SWE-bench como medida de capacidad.
- Calidad del código generado: estudio de diferencias en diferencias de CMU sobre 806 repos que adoptaron Cursor: 3 a 5 veces más líneas agregadas el primer mes, que se disipan a los dos meses; advertencias de análisis estático +30% y complejidad +41% tras la adopción. Observacional, repos de código abierto, [S] vía buscador. https://arxiv.org/abs/2511.04427 Un preprint posterior sobre agentes autónomos (https://arxiv.org/html/2601.13597v1) reporta efectos parecidos (~18% y ~35%) [S]. GitClear (211 millones de líneas, 2020-2024): ocho veces más bloques duplicados de 5+ líneas en 2024 y por primera vez más líneas copiadas que movidas; es de un proveedor con interés comercial y lo leí solo en notas secundarias. https://leaddev.com/software-quality/how-ai-generated-code-accelerates-technical-debt DORA 2024 (secundario) reportó que la IA mejoraba levemente la calidad y bajaba la estabilidad de entrega un 7,2% estimado, según https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250 [S].
- Cómo trabaja: la doc oficial actual ya no se organiza en el viejo "explorar, planificar, codificar, commitear": dice que "your first plain prompt in a fresh session already does the right thing", con modo automático, delegación a subagentes y compactación automática; lo que pide a la persona es contar lo que el agente no ve, "give it a check to run" y "enforce the rules that can't have exceptions". La verificación va desde el prompt, un `/goal`, un hook `Stop` que impide terminar hasta que pase el typecheck, hasta una revisión por un subagente nuevo; y pide evidencia (el comando y su salida), no "pasan las pruebas". https://code.claude.com/docs/en/best-practices La secuencia explorar-planificar-codear-commitear sigue valiendo como descripción de un bucle, pero no hay que presentarla como receta oficial vigente.
- Paralelo: `claude -w nombre` abre una sesión en un git worktree nuevo; un worktree es un checkout nuevo sin archivos ignorados ni dependencias: se copian con `.worktreeinclude` y se usa `worktree.symlinkDirectories` o el comando de instalación en CLAUDE.md; `/batch` divide un cambio mecánico grande en 5 a 30 unidades, cada una con su worktree y su PR. https://code.claude.com/docs/en/best-practices
- Seguridad operativa del agente: el Radar vol. 34 advierte que los agentes "find creative exfiltration paths, push to branches they shouldn't touch and erode approve/deny chokepoints" sin mala intención [S] https://www.thoughtworks.com/en-cl/radar. Lo vigente es permisos, sandbox y una sola rama donde pueda empujar (la propia doc lo menciona en "What's it allowed to touch?").
- Práctica: Thoughtworks (abril 2026) ve valor en el desarrollo guiado por especificaciones (Spec Kit en Assess) y señala la "cognitive debt": con más código generado "it's easier to adopt solutions without developing the mental models needed to understand how they work" [S]. Beck distingue vibe coding (solo importa el comportamiento) de augmented coding (se sigue cuidando la complejidad y las pruebas, con TDD) [S] https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes

### Qué cambia con agentes y qué pierde peso

Esta nota es la que describe el cambio. Pierde peso: medir la productividad por líneas o commits (el estudio de Cursor muestra el pico de líneas que se disipa), citar SWE-bench como prueba de capacidad, y confiar en la autopercepción (los desarrolladores de METR creían ir 20% más rápido cuando iban 19% más lento). Gana peso: tener una verificación ejecutable, cambios chicos, el sistema de entrega sano (DORA: amplificador).

### Recurso canónico

Para la práctica: la página best-practices de Claude Code, partes "Give Claude a check to run" y "Run parallel sessions". Para la evidencia: el post de METR de 2026-02-24 (más honesto sobre lo que no se sabe que el de 2025) y el informe DORA 2025. Fijarse en los intervalos de confianza, no en la cifra central.

## 3. plantilla-de-proyecto

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | Recencia |
|---|---|---|---|---|
| Notas del repo: Desarrollo/Generacion-de-proyectos/ (arquetipo-de-maven.md, derivar-nombres-en-un-arquetipo-de-maven.md, generacion-de-proyectos.md) y Platform-Engineering/Plataforma-interna/golden-path.md | primaria interna (borrador) | n/a | [L] las cabeceras y el arquetipo | 2026 |
| Copier https://copier.readthedocs.io/en/stable/ | primaria | 2/2/2/3 | [M] | volátil |
| Backstage Software Templates https://backstage.io/docs/features/software-templates/ | primaria | 3/2/2/2 | [M] | volátil |
| Spotify, golden paths (citada en la nota golden-path, no la releí) https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/ | práctica | 2/2/2/2 | [S] vía la nota existente | 2020 |

### Afirmaciones

- Copier es "A library and CLI app for rendering project templates" y plantea dos objetivos: "Code scaffolding" y "Code lifecycle management" ("When the template evolves, let consumers update their projects. Not all templates allow updating."). https://copier.readthedocs.io/en/stable/ No pude verificar el contraste con cookiecutter en esa página; el punto relevante (la plantilla se puede volver a aplicar y no solo copiar una vez) queda como [M].
- Backstage Software Templates: una herramienta para "create Components inside Backstage": esqueleto de código, variables, publicación en GitHub o GitLab que crea el repo, formulario con revisión y tareas con logs. https://backstage.io/docs/features/software-templates/
- La nota existente de Maven ya dice que lo generado no se actualiza solo, a diferencia de un proyecto padre. Esa es la diferencia clave con Copier y con un padre/BOM.
- Hueco: no encontré evidencia empírica de que las plantillas reduzcan defectos o tiempo de arranque; es práctica reconocida (Spotify, Platform Engineering), no demostrada.

### Qué queda acá y qué pasa a ficha

- Queda como nota `plantilla-de-proyecto` (corta, agnóstica de lenguaje): por qué arrancar de una plantilla versionada y no copiando otro servicio; tres mecanismos (arquetipo/plantilla que se copia una vez, plantilla re-aplicable tipo Copier, repositorio plantilla de GitHub; el generador de un portal tipo Backstage); y la novedad de que la plantilla ahora incluye lo que lee el agente: AGENTS.md/CLAUDE.md inicial, comandos de verificación, hooks, dev container y CI. Es el mejor lugar para que lo de `contexto-del-repositorio` se vuelva repetible.
- `golden-path` se queda en Platform-Engineering (es concepto de organización) y se enlaza; no se duplica.
- `arquetipo-de-maven` y `derivar-nombres-en-un-arquetipo-de-maven` pasan a ficha (herramienta concreta de Java/Maven) bajo Construccion/plantilla-de-proyecto/ o similar; `generacion-de-proyectos.md` se funde en la nueva entrada, como ya dice ALCANCE.md. Pierden peso como lectura general: la nota no debe empezar por Maven.
- Qué cambia con agentes: un agente puede generar un proyecto desde cero sin plantilla, pero la plantilla fija las decisiones (estructura, seguridad, CI) que no se quiere que el agente reinvente cada vez; y un agente también puede aplicar una actualización de plantilla a proyectos ya generados (el caso `/batch`). Fuente de la parte del agente: https://code.claude.com/docs/en/best-practices (`/batch`). La conclusión sobre "la plantilla fija lo que el agente no debe reinventar" es mía, sin fuente directa.
- Recurso canónico: la nota golden-path existente más la doc de Copier (secciones sobre actualización de proyectos).

## 4. Componentes faltantes de construcción

### Entorno de desarrollo reproducible (dev containers) — falta, recomendada

- Dev Containers: "A development container, or 'dev container,' lets you use a container as a full-featured development environment"; especificación abierta con Features y Templates; funciona en local o remoto. https://containers.dev/ [M]. El mantenimiento y las herramientas que lo soportan no los pude verificar en esa página (pie: Microsoft).
- Con agentes: un contenedor sirve de sandbox para correr el agente sin permisos amplios y de arranque determinista para sesiones en la nube; la doc de Claude Code lista el sandbox y los worktrees entre los límites de lo que el agente puede tocar (https://code.claude.com/docs/en/best-practices, "What's it allowed to touch?"). No encontré una fuente primaria que describa devcontainer.json como práctica para agentes: hueco.
- Hoy en el repo solo existe `levantar-un-entorno-local-con-docker-compose.md`, que cubre el entorno de ejecución con Compose y no el entorno de desarrollo.

### Manejo de dependencias — falta, recomendada

- Actualización automática con espera: Renovate tiene `minimumReleaseAge` ("requires Renovate to wait for a specified amount of time before suggesting a dependency update") https://docs.renovatebot.com/key-concepts/minimum-release-age/; Dependabot ofrece una configuración de edad mínima de paquete https://github.blog/changelog/2025-07-01-dependabot-supports-configuration-of-a-minimum-package-age/ y explica el porqué en https://github.blog/security/supply-chain-security/the-case-for-a-cooldown-why-dependabot-now-waits-before-issuing-version-updates/ ; según el buscador [S], npm lo sumó en la 11.10.0 (febrero 2026), pnpm y Yarn en septiembre 2025, y Renovate 42 pone 3 días por defecto en su preset para npm. Todas estas son cifras del buscador sin verificar en la fuente.
- Paquetes inventados por modelos (slopsquatting): Spracklen et al., USENIX Security 2025, 16 modelos y 576.000 muestras de código https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen (confirmado en la página de USENIX [S]); cifras de la prensa y de Socket: 19,7% de paquetes recomendados no existían, 43% de los nombres inventados reaparecieron en las diez repeticiones. Esas cifras no las verifiqué en el paper, y la propia cobertura aclara que salen de preguntar directamente qué instalar, no de código de uso normal. https://www.theregister.com/2025/04/12/ai_code_suggestions_sabotage_supply_chain/
- Con agentes: la dependencia nueva es una decisión que se revisa (¿existe, está mantenida, hace falta?); el agente agrega dependencias con facilidad. Se solapa con DevOps/DevSecOps (cadena de suministro) y Evolucion/migraciones-y-actualizaciones: decidir en cuál vive. Propuesta: la nota vive en Construccion/ ("agregar y actualizar dependencias") y las actualizaciones masivas en Evolucion.

### Estilo y formateo automático

No hace falta nota. Es una consecuencia de lo dicho: formateadores y linters corren en hook o CI y no en el archivo de instrucciones (https://code.claude.com/docs/en/best-practices, ejemplo "Always run the formatter after editing" que pasa a hook). Hook de Git ya existe en Git/. Se menciona dentro de `contexto-del-repositorio`.

### Programación en pareja con IA

Fuente fuerte, ninguna primaria. Beck (augmented coding, [S]) y el Radar (cognitive debt, [S]) dan postura de practicantes. El estudio de METR es la evidencia del riesgo de autopercepción. No recomiendo nota aparte: va como sección "modos de trabajo" en `agente-de-codigo` (supervisado paso a paso vs. delegado con verificación) con enlace a Verificacion/.

## 5. Configuracion/ y Git/ (qué revisar)

- Git/: no hay nada en desuso a la vista (modelo de objetos, rebase, reflog, hooks, LFS son vigentes). Falta lo esencial para agentes: **git worktree para sesiones en paralelo**. La nota `git-en-repositorios-grandes.md` ya tiene una fila de worktree (la describe como "un segundo clon completo", que no es del todo correcto: comparte el mismo `.git`, la propia fila lo dice después) pero solo como revisar un branch sin guardar el trabajo. Propuesta: una nota o sección "worktrees para trabajo en paralelo" con lo que dice la doc de Claude Code (un checkout nuevo no trae `.env` ni dependencias; `.worktreeinclude`; limpieza; `git worktree remove` y `unlock`). También una sección sobre cómo un agente commitea y empuja (ramas propias, no empujar a la rama principal), enlazada con DevOps/Ramas-y-versiones. La memoria del usuario ya advierte de revisar `git worktree list` y de no tocar ramas ajenas, lo que confirma que el riesgo es real.
- Configuracion/: YAML, Spring Boot externalizada y Compose son vigentes pero específicos de un stack; son fichas. Falta lo esencial transversal: **secretos y archivos que el agente no debe leer** (el ejemplo de `Never read .env` y los deny rules de la doc de Claude Code) y la regla "el agente no recibe credenciales de producción". La nota de configuración ya enlaza Gestión de secretos en DevOps. Propuesta: agregar a `configuracion.md` un párrafo sobre qué puede ver un agente y enlazar a `contexto-del-repositorio`. La nota de Compose tiene estabilidad `semi` y hay que decidir si pasa a ficha de entorno local junto con dev containers.
- Las dos entradas llevan `fuentes: []` en la entrada y el enlace a `Especificacion-y-prueba/` en `generacion-de-proyectos.md` apunta a una carpeta que ALCANCE.md reordena; hay que actualizar enlaces al mover.

## 6. Lo que pierde peso en construcción (con quién lo dice)

- Archivo de instrucciones largo con resumen de arquitectura: ArXiv 2602.11988, Radar vol. 35, doc de Claude Code (sección 1).
- Lectura de puntajes de SWE-bench como capacidad: OpenAI 2026-02-23.
- Productividad como líneas o commits: estudio de Cursor [S] y METR.
- Autopercepción de velocidad como medida: METR 2025 (creían +20%, midieron -19%).
- Copiar otro servicio como plantilla (sección 3).

## 7. Huecos

1. No leí el PDF de DORA 2025: la afirmación "más throughput, más inestabilidad" y los resultados sobre calidad y confianza están sin verificar; hay que leerlo antes de escribir esa afirmación.
2. No verifiqué en el paper ni en la página de Anthropic: el dato del 80% del system prompt, las cifras de slopsquatting, las versiones de npm/pnpm/Renovate, el informe de GitClear y los números de CMU. Son [S].
3. Sin fuente primaria sobre dev containers como entorno para agentes.
4. Sin evidencia empírica de que las plantillas de proyecto reduzcan defectos o tiempo.
5. Sin estudio controlado sobre programación en pareja con IA (hay opiniones de practicantes y el RCT de METR, que no es de pareja).
6. No abrí el PDF del Radar vol. 34 ni el 35 completo; "cognitive debt" y la advertencia de seguridad de agentes los leí en el resumen del buscador.
7. La doc de Claude Code cambia rápido: la estructura "explorar-planificar-codear-commitear" desapareció de la página actual; los números de versión, modelos y comandos (`/goal`, `/batch`, `/verify`) hay que fecharlos y revisarlos en cada pasada.
8. No confirmé que Claude Code lea AGENTS.md (convive con CLAUDE.md); verificar en https://code.claude.com/docs/en/memory antes de recomendar un archivo común.
9. No busqué la doc de Cursor ni de GitHub Copilot sobre archivos de contexto propios (`.cursor/rules`, `copilot-instructions.md`); AGENTS.md los cubre en parte según agents.md.
