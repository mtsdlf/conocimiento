# Investigación: Fundamentos del tema y vistazo del todo

Fecha de la ronda: 2026-11-27. Alcance: cómo el campo se divide a sí mismo, escuelas, historia, bibliografía, glosario.

Convenciones. Marcas de lectura: [L] texto completo de la fuente, [M] metadatos o abstract, [S] resumen secundario o del buscador, [W] lo leí a través de un resumen de la página (la herramienta de lectura devuelve un resumen, no el texto literal), [MEM] dato de memoria, NO verificado en esta ronda (hay que verificarlo antes de escribir la nota). Puntajes 1 a 3: Autoridad / Profundidad / Ejemplos / Unicidad.

## 0. Hallazgos que más cambian el árbol (resumen)

1. El árbol del ALCANCE cubre bien los procesos técnicos de 12207 y las áreas de requisitos, diseño, construcción, pruebas, mantenimiento. Quedan sin lugar: **seguridad del software** (área nueva en SWEBOK v4), **gestión de configuración y de dependencias como práctica propia**, **calidad como disciplina transversal**, **economía de la ingeniería** (decidir qué vale la pena, deuda, costo de cambio), **gestión de riesgos y de proyecto técnico**, **validación** (distinta de verificación), **medición y evidencia** (DORA), **práctica profesional** (ética, responsabilidad, licencias y propiedad del código generado).
2. Farley divide el oficio en dos pegamentos, "optimizar para aprender" (iterar, feedback, incrementalismo, empirismo, experimentar) y "optimizar para gestionar la complejidad" (modularidad, cohesión, separación de responsabilidades, abstracción, acoplamiento). Lo segundo ya vive en Arquitectura; lo primero no tiene nota en Desarrollo y es el corazón de la escuela elegida. Propuesta: una nota `Fundamentos/aprender-rapido` (o `ingenieria-moderna`) con esos cinco principios y la evidencia (DORA).
3. La evidencia sobre agentes se movió dentro del propio año: METR 2025 midió 19% más lento; la actualización de febrero 2026 dice que ese número ya es mal proxy y rediseña el estudio (sin cifra firme nueva). Las notas no deben citar "19% más lento" sin esa corrección.
4. DORA 2025 (23-sep-2025): la IA es "amplificador"; hay más throughput pero también más inestabilidad. Respalda la escuela (pasos chicos, prueba automática) como condición para que la IA rinda.
5. Spec-driven development está en Assess en el Radar de Thoughtworks (nov 2025) y Böckeler/Fowler lo critica (tamaño del flujo, revisión de specs, "false sense of control"). El tema debe presentarlo como práctica emergente con tres niveles (spec-first, spec-anchored, spec-as-source), no como estándar.
6. Royce 1970 no dijo "cascada" ni la recomendó: la figura secuencial es la que llama "risky and invites failure". Es un malentendido citable con fuente primaria.
7. ISO/IEC/IEEE 12207 tiene edición 2026 (abril 2026, según Wikipedia vía buscador [S]); la 2017 figura como reemplazada. Verificar antes de citar edición.

## 1. Cómo se divide el dominio a sí mismo

### 1.1 Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| SWEBOK v4, IEEE Computer Society (oct 2024) vía Wikipedia | https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge | secundaria | 2/2/1/1 | [W] |
| SWEBOK v4, página oficial | https://www.computer.org/education/bodies-of-knowledge/software-engineering | primaria | 3/3/1/3 | no accesible (HTTP 403) |
| Farley, Modern Software Engineering (Addison-Wesley, 10-dic-2021) índice vía InformIT | https://www.informit.com/store/modern-software-engineering-doing-what-works-to-build-9780137314911 | primaria (editorial) | 3/2/1/2 | [W] |
| ISO/IEC/IEEE 12207:2017 vía arc42 y Wikipedia | https://quality.arc42.org/standards/iso12207 ; https://en.wikipedia.org/wiki/ISO/IEC_12207 | secundaria | 2/1/1/1 | [S] |
| IEEE, estado de 12207-2017 ("Superseded") | https://standards.ieee.org/standard/12207-2017 | primaria | 3/1/1/2 | [S] (solo el título del resultado) |

### 1.2 Afirmaciones

SWEBOK v4 tiene 18 áreas de conocimiento y se publicó en octubre de 2024 (https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge). Las 18, literales: Software requirements; Software architecture; Software design; Software construction; Software testing; Software engineering operations; Software maintenance; Software configuration management; Software engineering management; Software engineering process; Software engineering models and methods; Software quality; Software security; Software engineering professional practice; Software engineering economics; Computing foundations; Mathematical foundations; Engineering foundations. La v3 tenía 15; la v4 agrega Software architecture, Software engineering operations y Software security y no quita ninguna (misma URL). Esa página dice que la v4 suma como disciplinas relacionadas business analysis, cybersecurity, data science e information systems/IT.

Farley, índice literal (https://www.informit.com/store/modern-software-engineering-doing-what-works-to-build-9780137314911): Parte I What Is Software Engineering? (1 Introduction; 2 What Is Engineering?; 3 Fundamentals of an Engineering Approach). Parte II Optimize for Learning (4 Working Iteratively; 5 Feedback; 6 Incrementalism; 7 Empiricism; 8 Being Experimental). Parte III Optimize for Managing Complexity (9 Modularity; 10 Cohesion; 11 Separation of Concerns; 12 Information Hiding and Abstraction; 13 Managing Coupling). Parte IV Tools to Support Engineering in Software (14 The Tools of an Engineering Discipline; 15 The Modern Software Engineer). Fecha: la página dice "Dec 10, 2021", con copyright 2022 (el brief y el ALCANCE dicen 2021; citar 2021/2022 con esa aclaración).

12207: la edición 2017 agrupa los procesos en cuatro: acuerdo (adquisición y suministro), habilitación organizacional del proyecto (modelo de ciclo de vida, infraestructura, portafolio, recursos humanos, calidad, conocimiento), gestión técnica (planificación, evaluación y control, decisiones, riesgos, configuración, medición, gestión de información) y procesos técnicos (definición de requisitos de interesados, análisis de requisitos, diseño de arquitectura, implementación, integración, verificación, transición, validación, operación, mantenimiento, disposición) (https://quality.arc42.org/standards/iso12207 y https://en.wikipedia.org/wiki/ISO/IEC_12207; las dos coinciden en los cuatro grupos, discrepan en la cantidad exacta de procesos de gestión técnica: no usar el número). La página de IEEE marca la 2017 como "Superseded" por 12207-2026; Wikipedia dice abril 2026 (https://standards.ieee.org/standard/12207-2017). [S]: verificar en iso.org.

### 1.3 Comparación con el árbol del ALCANCE

| Área del campo | Dónde cae en el ALCANCE | Veredicto |
|---|---|---|
| Requisitos (SWEBOK), definición de requisitos y análisis (12207) | Encargo/acuerdo-inicial, alcance-y-aceptacion; Definicion/ | Cubierta. Ojo: 29148 (norma de requisitos) conviene nombrarla en `especificacion` |
| Arquitectura y diseño | Se enlaza a Arquitectura | Cubierta afuera. Farley Parte III también va ahí |
| Construcción | Construccion/ | Cubierta |
| Pruebas | Verificacion/ | Cubierta. Falta distinguir verificación (¿lo construí bien?) de validación (¿construí lo correcto?): hoy `alcance-y-aceptacion` y `seguimiento-con-el-cliente` hacen de validación sin nombrarla |
| Operaciones | DevOps | Cubierta afuera |
| Mantenimiento | Evolucion/ | Cubierta |
| Gestión de configuración | Git/ y Configuracion/ (parcial) | Parcial: falta versionado de dependencias, ramas/entornos, reproducibilidad. Se toca con migraciones-y-actualizaciones |
| Gestión (planificar, riesgos, medir) | Encargo/estimacion, plan-de-entregas | Parcial: falta **gestión de riesgos** y **medición/evidencia** (métricas DORA, tiempo de ciclo, tasa de defectos escapados) |
| Proceso e ingeniería de procesos, modelos y métodos | Fundamentos/escuelas-de-desarrollo | Cubierta |
| Calidad | Verificacion/ (parcial) | Parcial: calidad como atributos (rendimiento, accesibilidad, mantenibilidad) y no solo pruebas |
| **Seguridad del software** | Sin lugar | Hueco. Es área nueva en v4. Con agentes se agrava (dependencias inventadas, secretos, código generado inseguro; ver 2.x, Veracode, CodeRabbit). Propuesta: `Verificacion/seguridad-en-el-desarrollo` o tema propio enlazado |
| **Economía de la ingeniería** | Encargo/estimacion (parcial) | Parcial: falta costo de cambio, deuda como decisión económica, comprar vs construir. Encaja en `Evolucion/deuda-tecnica` y `Encargo/estimacion` |
| **Práctica profesional** (ética, responsabilidad, propiedad intelectual y licencias del código generado) | Sin lugar | Hueco. Lo legal exige dos fuentes independientes; esta ronda no las buscó |
| Fundamentos de computación, matemática, ingeniería | Fuera por el nivel declarado | Correcto que queden afuera |
| Habilitación organizacional (RR. HH., portafolio, conocimiento) | Fuera | Correcto; "gestión del conocimiento" ya es el tema `documentar` |

Corte propuesto: no agregar vertical. Agregar tres notas: `Fundamentos/ingenieria-moderna` (Farley Parte II como método: aprender rápido), `Verificacion/seguridad-en-el-desarrollo` y `Fundamentos/evidencia-y-medicion` (DORA, qué medir y qué no). El ciclo doble del ALCANCE (cliente / técnico) no está en ninguna de las tres fuentes: es un corte propio, razonable, y cercano al grupo "acuerdo" de 12207 frente a los "técnicos". Conviene decirlo en `desarrollo.md`.

### 1.4 Qué cambia con agentes

SWEBOK v4 no lo trata como cambio de áreas: las áreas siguen. Lo que cambia es dónde está el cuello: el código sale barato, así que pesan más requisitos, verificación, seguridad y mantenimiento. Fuente: DORA 2025, que dice que la IA es "amplificador" de fortalezas y disfunciones (https://dora.dev/research/2025/dora-report/ [W]). Pierde peso: la gestión de configuración manual y la documentación de diseño larga como entregable.

### 1.5 Recurso canónico

SWEBOK v4: leer el capítulo de Requirements y el de Testing, y la tabla de áreas; en qué fijarse: el vocabulario (verificación vs validación). Farley: Partes II y III. 12207: solo el esquema de grupos de procesos, no la norma entera (es de pago).

## 2. Escuelas de desarrollo (mapa para `escuelas-de-desarrollo`)

### 2.1 Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| Manifiesto Ágil (2001) | https://agilemanifesto.org/ | primaria | 3/1/1/3 | [W] |
| Scrum Guide 2020 | https://scrumguides.org/scrum-guide.html | primaria | 3/3/2/3 | [W] |
| XP, Wikipedia (Beck 1999, 2004) | https://en.wikipedia.org/wiki/Extreme_programming | secundaria | 2/2/1/1 | [W] |
| Shape Up (Singer, Basecamp) | https://basecamp.com/shapeup/0.3-chapter-01 | primaria | 2/2/2/3 | [W] |
| Accelerate (Wikipedia, 2018) | https://en.wikipedia.org/wiki/Accelerate_(book) | secundaria | 2/2/1/1 | [W] |
| DORA 2025 | https://dora.dev/research/2025/dora-report/ ; https://blog.google/technology/developers/dora-report-2025/ | primaria / secundaria | 3/2/1/2 | [W] / [S] |
| Waterfall, Royce 1970 (Wikipedia, buscador) | https://en.wikipedia.org/wiki/Waterfall_model ; https://faculty.washington.edu/hazeline/misc/reserve/royce_waterfall.pdf | secundaria / primaria (reimpresión) | 2/2/1/2 | [W] / [S] (el PDF no se abrió) |
| Böckeler, Understanding SDD (martinfowler.com, 15-oct-2025) | https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html | primaria (practicante, marcado) | 2/3/3/3 | [W] |
| Thoughtworks Radar, Spec-driven development (5-nov-2025, Assess) | https://www.thoughtworks.com/radar/techniques/spec-driven-development | primaria (practicante) | 2/2/1/2 | [W] |
| GitHub Spec Kit | https://github.com/github/spec-kit | primaria (herramienta) | 2/2/2/3 | [W] |
| Karpathy, post del 2-feb-2025, vía Wikipedia | https://en.wikipedia.org/wiki/Vibe_coding | secundaria | 2/2/2/1 | [W] |
| Willison, 19-mar-2025 | https://simonwillison.net/2025/Mar/19/vibe-coding/ | primaria (practicante) | 2/2/2/3 | [W] |
| Beck, Augmented Coding: Beyond the Vibes (25-jun-2025) | https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes | primaria (autor) | 3/2/3/3 | [W] |
| METR RCT (10-jul-2025) | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | primaria (informe técnico, sin revisión por pares: no verificado si pasó a venue) | 2/3/2/3 | [W] |
| METR, actualización 24-feb-2026 | https://metr.org/blog/2026-02-24-uplift-update/ | primaria | 2/3/2/3 | [W] |
| Anthropic, Best practices for Claude Code | https://code.claude.com/docs/en/best-practices | primaria (docs oficiales, volátil) | 3/3/3/3 | [W] (guardado el texto; solo leí el inicio) |
| AGENTS.md | https://agents.md/ | primaria | 2/1/1/3 | [W] |

### 2.2 Mapa (una línea cada una + autor + texto + evidencia + estado)

**Ágil (Manifiesto, 2001).** Sostiene cuatro valores: "Individuals and interactions over processes and tools", "Working software over comprehensive documentation", "Customer collaboration over contract negotiation", "Responding to change over following a plan" (https://agilemanifesto.org/ [W]; 17 firmantes, año 2001 por el copyright; la página no da fecha ni lugar). Evidencia: los estudios de DORA apoyan las prácticas (entrega en lotes chicos) más que la etiqueta. Estado hoy: vigente como actitud; la marca "Agile" como industria de certificaciones pierde peso (criterio propio, sin fuente).

**Extreme Programming (Beck).** Nace en el proyecto C3 de Chrysler (Beck líder desde marzo 1996, proyecto cancelado en febrero 2000); *Extreme Programming Explained*, octubre 1999; 2ª edición con Cynthia Andres, 2004, agrega "respect" a los valores (https://en.wikipedia.org/wiki/Extreme_programming [W]). Prácticas: pair programming, planning game, TDD, whole team, integración continua, refactoring, small releases, estándares de código, propiedad colectiva, diseño simple, metáfora, ritmo sostenible. Estado: sus prácticas técnicas (TDD, CI, refactor, releases chicos) son la base de la escuela moderna; vigente.

**Scrum.** Scrum Guide 2020: "a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems"; cinco eventos (Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective), tres accountabilities (Developers, Product Owner, Scrum Master); dice que el framework es "purposefully incomplete" (https://scrumguides.org/scrum-guide.html [W]). Autores: Schwaber y Sutherland [MEM]. Estado: el más difundido [MEM, sin dato]; la versión ceremonial es el contraste del tema. Evidencia comparativa de Scrum vs. otras: no la busqué (hueco).

**Kanban / flujo.** Gestión del flujo con límites de trabajo en curso; en DORA aparecen "visual workflow" y "WIP limits" como capacidades (https://en.wikipedia.org/wiki/Accelerate_(book) [W]). Texto de referencia: Anderson, *Kanban* (2010) [MEM]. Estado: vigente, y encaja bien con agentes (el cuello pasa a la revisión; limitar WIP de PRs). Fuente directa de Anderson: hueco.

**Lean software development (Poppendieck).** Mary y Tom Poppendieck, *Lean Software Development* (2003) [MEM]: eliminar desperdicio, amplificar aprendizaje, decidir tarde, entregar rápido, empoderar al equipo, integridad, ver el todo. Estado: vigente como fundamento de DORA/Accelerate ("Lean and DevOps"). Sin lectura en esta ronda: hueco para citar.

**Shape Up (Singer, Basecamp).** Ciclos de seis semanas ("Six weeks is long enough to build something meaningful start-to-finish"); se "da forma" al trabajo antes de dárselo al equipo; *appetite* = "The amount of time we want to spend on a project, as opposed to an estimate"; *betting table*; *circuit breaker* = "Cancel projects that don't ship in one cycle by default instead of extending them by default" (https://basecamp.com/shapeup/0.3-chapter-01 [W]). Evidencia: práctica de una empresa, sin estudio controlado [MEM]. Interesa para Encargo: apetito en vez de estimación, y circuit breaker como regla de cambios de alcance. Estado: vigente en nicho.

**Ingeniería de software moderna (Farley).** Dos ejes: optimizar para aprender (iterar, feedback, incrementalismo, empirismo, experimentar) y para gestionar complejidad (modularidad, cohesión, separación, abstracción, acoplamiento) (índice en 1.2). Apoyo empírico: DORA. Estado: vigente y es la escuela de este tema.

**DevOps / DORA como evidencia.** *Accelerate* (Forsgren, Humble, Kim, 2018): cuatro métricas (Change Lead Time, Deployment Frequency, Change Failure Rate, Mean Time to Recovery) y 24 capacidades en cinco categorías, sobre unos 23.000 datos de las State of DevOps (https://en.wikipedia.org/wiki/Accelerate_(book) [W]). Aviso: en octubre 2023 el equipo DORA advirtió contra usar las métricas para evaluar equipos individuales (misma fuente). DORA 2025 (23-sep-2025, ~5.000 profesionales, encuesta 13-jun a 21-jul-2025): IA como "amplificador", más throughput y también más inestabilidad, ganancias donde hay arquitecturas desacopladas y feedback rápido; ~90% usa IA (https://blog.google/technology/developers/dora-report-2025/ [S], vía buscador; el informe en https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf no se leyó). Estado: la evidencia más sólida del tema.

**Predictivo / cascada.** Plan completo por fases. Malentendido de Royce 1970: su artículo "Managing the Development of Large Software Systems" presenta el esquema secuencial y dice "I believe in this concept, but the implementation described above is risky and invites failure"; propone volver a iterar y "Do the job twice if possible"; no usó la palabra "waterfall" (según Wikipedia, el uso más temprano "may have been" Bell y Thayer 1976, dato marcado por Wikipedia como necesitado de mejor fuente) (https://en.wikipedia.org/wiki/Waterfall_model [W] y https://faculty.washington.edu/hazeline/misc/reserve/royce_waterfall.pdf [S]). Lectura contraria: la frase refiere a la Figura 2 sin lazos de retroalimentación, no condena la idea de etapas (Leanpub, Leprechauns, cap. 7, https://leanpub.com/read/leprechauns/leanpub-auto-chapter-7-whos-afraid-of-the-big-bad-waterfall [S]). Estado: como contraste; planificar por adelantado a nivel de intención sigue siendo necesario (ver Shape Up).

**Spec-driven development (SDD) con agentes.** Böckeler (martinfowler.com, 15-oct-2025): escribir la especificación antes del código con IA como fuente de verdad; tres niveles: spec-first, spec-anchored, spec-as-source; todas las herramientas revisadas son spec-first (https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html [W]). Herramientas: Kiro (Requirements → Design → Tasks), spec-kit (constitution, specify, plan, tasks, implement; MIT; https://github.com/github/spec-kit [W]), Tessl (spec-as-source, "GENERATED FROM SPEC - DO NOT EDIT"). Críticas, literales de resumen: Kiro convirtió un bug chico en cuatro historias con 16 criterios de aceptación; spec-kit genera muchos archivos repetitivos; los agentes a veces ignoran instrucciones; riesgo de repetir las lecciones de la ingeniería dirigida por modelos; "spec" se vuelve sinónimo de "prompt detallado". Thoughtworks Radar (5-nov-2025): ring Assess, "interesting but elaborate and opinionated", y duda de que escribir reglas detalladas a mano escale ("bitter lesson") (https://www.thoughtworks.com/radar/techniques/spec-driven-development [W]). Estado: emergente, sin evidencia controlada que haya encontrado (hueco). Postura recomendable para las notas: especificar con ejemplos verificables y mantener el flujo proporcional al tamaño del cambio.

**Posturas sobre IA en el desarrollo.**
- *Vibe coding* (Karpathy, post del 2-feb-2025): "fully give in to the vibes, embrace exponentials, and forget that the code even exists"; Collins lo eligió palabra del año 2025 (anuncio 6-nov-2025) (https://en.wikipedia.org/wiki/Vibe_coding [W]; el post original no se abrió).
- Willison (19-mar-2025): vibe coding es "building software with an LLM without reviewing the code it writes"; no confundirlo con programar con ayuda de LLM; su regla personal: no commitear código que no pueda explicar (https://simonwillison.net/2025/Mar/19/vibe-coding/ [W]).
- Beck, *augmented coding* (25-jun-2025): se sigue cuidando el código ("tidy code that works"), no se tipea la mayor parte; avisos: bucles, funcionalidad no pedida, trampas como borrar o desactivar tests; usó un plan file y una prueba a la vez con TDD y Tidy First (https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes [W]).
- Ingeniería con agentes (docs de Anthropic): "tell Claude what it can't see, give it a check to run" y fallas típicas: construyó otra cosa, o dijo estar listo sin poder verificarse (https://code.claude.com/docs/en/best-practices [W]).
- Evidencia: GitClear (211 millones de líneas 2020-2024; refactor de 25% a menos de 10%, duplicación x4), CodeRabbit (17-dic-2025; 470 PRs; 1,7 veces más issues "major", 2,74 veces más vulnerabilidades), Veracode (oct 2025: mejor funcionalidad, seguridad sin mejora general) vía Wikipedia (https://en.wikipedia.org/wiki/Vibe_coding [W], terceros no leídos; los tres son estudios de industria, sin revisión por pares: marcar). METR RCT 2025: 16 desarrolladores experimentados, 246 tareas, 19% más lentos con IA; esperaban 24% más rápidos y después creían 20% (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ [W]). METR 24-feb-2026: el estudio nuevo (57 desarrolladores, 143 repos, 800+ tareas) dio -18% de tiempo (IC -38% a +9%) en los que volvían y -4% (IC -15% a +9%) en los nuevos, pero METR lo califica de proxy poco fiable por efectos de selección (muchos se negaron a trabajar sin IA) y rediseña el experimento; cree que el aumento es probablemente mayor en 2026 que en 2025 (https://metr.org/blog/2026-02-24-uplift-update/ [W]). Las dos fuentes de METR son del mismo grupo: una sola autoridad.
- Contexto para agentes: AGENTS.md, formato abierto "README for agents", custodiado por la Agentic AI Foundation (Linux Foundation), con "over 60k" proyectos y la lista de agentes compatibles (Codex, Cursor, Copilot, Gemini CLI, Jules, Devin, Windsurf, Zed, entre otros) (https://agents.md/ [W]).

### 2.3 Qué cambia con agentes / qué pierde peso (para esta sección)

Ganan peso: especificación con ejemplos, pruebas automáticas como contrato, revisión, ciclo de feedback corto (DORA: ganancias solo con feedback rápido y arquitectura desacoplada). Pierden peso (criterio propio, a verificar): estimación en story points, ceremonias de Scrum como valor en sí, documento de requisitos grande por adelantado (Thoughtworks y Böckeler apuntan igual contra specs voluminosas). Dudoso: SDD completo para cambios chicos.

### 2.4 Recurso canónico

Para la escuela: Farley caps. 4 a 8, luego DORA capabilities (dora.dev). Para posturas de IA: Beck (junio 2025) + Willison (marzo 2025) + Böckeler (octubre 2025). Para contraste: Scrum Guide 2020 (13 páginas) y Royce 1970 (el artículo, 11 páginas [MEM]).

## 3. Historia corta del proceso

Verificado en esta ronda: Garmisch 7 al 11 de octubre de 1968, NATO Science Committee ("software crisis" se atribuye a asistentes; Wikipedia no dice quién acuñó "software engineering") (https://en.wikipedia.org/wiki/Software_crisis [W]); Dijkstra en su Turing Lecture de 1972: "The major cause of the software crisis is that the machines have become several orders of magnitude more powerful!" (misma URL); Royce 1970 (sección 2); Manifiesto 2001; XP 1999 y 2004; Accelerate 2018; Karpathy 2-feb-2025; METR 10-jul-2025; Fowler/Böckeler 15-oct-2025; SWEBOK v4 octubre 2024; 12207-2026 abril 2026 [S]. El informe de la NATO (PDF de Randell en ncl.ac.uk) no se pudo abrir: el certificado del sitio venció.

Hitos de memoria, [MEM], sin verificar en esta ronda: Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules" (1972); Brooks, *The Mythical Man-Month* (1975); Boehm, *Software Engineering Economics* (1981) y modelo espiral (1986/88); Scrum presentado en 1995; Beck, *TDD by Example* (2002); Fowler, *Refactoring* (1999; 2ª ed. 2018); Humble y Farley, *Continuous Delivery* (2010); DevOps como movimiento ~2009; GitHub Copilot en vista previa 2021; ChatGPT nov 2022; agentes de código en terminal desde 2025 (Claude Code, Codex CLI). Para la nota, verificar cada una con su fuente primaria antes de fecharla.

Cuatro etapas sugeridas para el relato: (1) 1968-1990, crisis y planificación predictiva; (2) 1990-2010, iterativo y ágil (XP, Scrum, Manifiesto); (3) 2010-2020, entrega continua, DevOps y la evidencia (Accelerate); (4) 2021-hoy, asistentes y agentes, con medición todavía en disputa.

## 4. Bibliografía por necesidad (borrador para `bibliografia-de-desarrollo`)

Todos [MEM] salvo donde se indica; verificar edición y año antes de escribir. Farley verificado.

| Necesidad | Recurso | Qué leer | En qué fijarse |
|---|---|---|---|
| Entender el proceso | Farley, *Modern Software Engineering* (2021/22) [L índice] | Partes II y III | Los cinco principios de aprender; qué dice de estimar |
| Entender el proceso | Forsgren, Humble, Kim, *Accelerate* (2018) | Caps. de métricas y capacidades | Qué es evidencia y qué es correlación |
| Entender el proceso | Scrum Guide 2020 (gratis) [W] | Entera, es corta | Que dice "framework" incompleto |
| Entender el proceso | Singer, *Shape Up* (gratis) [W] | Apetito, formar el trabajo, circuit breaker | Cómo se acota sin estimar |
| Especificar | Adzic, *Specification by Example* | Ejemplos como especificación, "living documentation" | Ejemplos concretos y no abstractos |
| Especificar | Cohn, *User Stories Applied* | Qué es una buena historia, criterios | Divide historias; INVEST |
| Especificar | Evans, *Domain-Driven Design* | Lenguaje ubicuo, contexto delimitado (primeras partes) | El vocabulario común con el código |
| Especificar | ISO/IEC/IEEE 29148 | Solo el índice de atributos de un buen requisito | Norma de pago |
| Probar | Beck, *Test-Driven Development by Example* | Parte I y II | El ritmo rojo-verde-refactor |
| Probar | Fowler, *Refactoring* 2ª ed. | Cap. 1 y catálogo como referencia | Pasos chicos con pruebas |
| Mantener legado | Feathers, *Working Effectively with Legacy Code* | "Seams" y pruebas de caracterización | Definición: legado = código sin pruebas |
| Mantener / diseñar | Ousterhout, *A Philosophy of Software Design* | Módulos profundos, complejidad | Contrapeso a "clean code" mecánico |
| Trabajar con agentes | Anthropic, Best practices for Claude Code [W] | Tell Claude what it can't see; give it a check to run | Volátil: fechar |
| Trabajar con agentes | Beck (jun 2025) y Willison (mar 2025) [W] | Enteros, cortos | Qué señales de trabajo incompleto |
| Trabajar con agentes | Böckeler (oct 2025) [W]; Thoughtworks Radar | Niveles de SDD y críticas | Qué se dice sin evidencia |
| Trabajar con agentes | METR (jul 2025 y feb 2026) [W] | Limitaciones | Qué se midió y qué no |
| Marco del campo | SWEBOK v4 (IEEE, 2024) | Tabla de áreas | Vocabulario común |

## 5. Glosario (34 términos, definición de una línea y fuente)

Las fuentes marcadas "lit." son las citadas arriba (leídas); "[MEM]" no verificada.

1. **Agente de código**: programa que, con un modelo de lenguaje, lee el repo, edita archivos, corre comandos y pruebas en bucle. Fuente: docs de Anthropic, https://code.claude.com/docs/en/best-practices.
2. **AGENTS.md**: archivo Markdown con instrucciones del proyecto para agentes, "README for agents". https://agents.md/.
3. **Amplificador (DORA 2025)**: la IA magnifica fortalezas y disfunciones de la organización. https://dora.dev/research/2025/dora-report/.
4. **Apetito (appetite)**: tiempo que se quiere gastar en un proyecto, no una estimación. https://basecamp.com/shapeup/0.3-chapter-01.
5. **Augmented coding**: programar con IA cuidando el código, las pruebas y la complejidad. Beck, https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes.
6. **Betting table**: reunión donde se decide en qué pitches apostar el próximo ciclo. Shape Up (misma URL que 4).
7. **Circuit breaker**: por defecto se cancela lo que no sale en un ciclo, en vez de extenderlo. Shape Up.
8. **Change failure rate**: proporción de cambios que fallan; una de las cuatro métricas DORA. https://en.wikipedia.org/wiki/Accelerate_(book).
9. **Change lead time**: tiempo del primer commit al despliegue. Misma fuente.
10. **Cohesión**: grado en que las partes de un módulo pertenecen juntas. Farley, parte III.
11. **Criterio de aceptación**: condición verificable con la que se decide que algo está terminado. Adzic [MEM].
12. **Cascada (waterfall)**: secuencia de fases sin retorno; término posterior a Royce 1970. https://en.wikipedia.org/wiki/Waterfall_model.
13. **Deuda técnica**: costo futuro de atajos de diseño; término de Cunningham [MEM].
14. **Deployment frequency**: con qué frecuencia se despliega. https://en.wikipedia.org/wiki/Accelerate_(book).
15. **Empirismo (Farley)**: decidir con evidencia observada, no con opinión. Farley, cap. 7.
16. **Especificación (spec)**: descripción de lo que el software debe hacer, insumo del desarrollo con agentes. Böckeler, https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html.
17. **Spec-first / spec-anchored / spec-as-source**: tres niveles: la spec se usa y se descarta, se mantiene, o es el único archivo que se edita. Böckeler.
18. **Spec-driven development (SDD)**: escribir la especificación antes del código con IA, como fuente de verdad. Böckeler; Thoughtworks Radar.
19. **Historia de usuario**: descripción breve de una necesidad desde quien la tiene. Cohn [MEM]; ver nota existente.
20. **Increment / incrementalismo**: entregar valor en pasos pequeños utilizables. Farley, cap. 6; Scrum Guide.
21. **Integración continua (CI)**: integrar y verificar cambios con frecuencia en un tronco común. XP, https://en.wikipedia.org/wiki/Extreme_programming.
22. **Kanban / límite de WIP**: visualizar el trabajo y limitar lo en curso. DORA capabilities (Accelerate).
23. **MTTR**: tiempo medio de restablecer el servicio tras una falla. Accelerate.
24. **Refactorizar**: cambiar la estructura interna sin cambiar el comportamiento observable. Fowler [MEM].
25. **Retroalimentación (feedback)**: información rápida sobre si lo hecho funciona; Farley, cap. 5.
26. **Shaping**: darle forma al trabajo (límites, riesgos, solución a grandes rasgos) antes de dárselo al equipo. Shape Up.
27. **Sprint**: contenedor de tiempo fijo de Scrum. Scrum Guide, https://scrumguides.org/scrum-guide.html.
28. **SWEBOK**: Guía del cuerpo de conocimiento de la ingeniería de software de IEEE Computer Society; v4 de oct 2024 con 18 áreas. https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge.
29. **TDD**: escribir una prueba que falla, hacerla pasar, refactorizar. Beck [MEM]; práctica de XP.
30. **Validación vs. verificación**: validar es si se construyó lo correcto; verificar es si se construyó bien lo especificado. SWEBOK / 12207 (criterio de las normas) [MEM].
31. **Vibe coding**: construir software con un LLM sin revisar el código que escribe. Willison, https://simonwillison.net/2025/Mar/19/vibe-coding/.
32. **Acoplamiento**: dependencia entre módulos; cuánto cambia uno cuando cambia otro. Farley, cap. 13.
33. **Prueba de caracterización**: prueba que fija el comportamiento actual de código heredado antes de tocarlo. Feathers [MEM].
34. **Contexto del repositorio**: lo que un agente debe saber del proyecto que no se ve en el código (reglas, comandos, convenciones). Docs de Anthropic ("tell Claude what it can't see").

## 6. Huecos

- SWEBOK oficial (403): solo la lista de áreas vía Wikipedia; no leí el contenido de ningún capítulo.
- 12207:2026 no verificada en iso.org; la lista de procesos es de resúmenes secundarios.
- Informe de la NATO 1968 (certificado vencido) y artículo de Royce 1970 (PDF no abierto): citas de Royce vía secundarias; la frase literal aparece en el buscador.
- Sin lectura directa de Poppendieck, Anderson, Beck TDD, Fowler, Feathers, Evans, Adzic, Cohn, Ousterhout: bibliografía y glosario con [MEM] a confirmar (ediciones y años).
- Sin evidencia empírica controlada de SDD, ni comparación Scrum vs. Kanban vs. Shape Up; Shape Up solo con la práctica del propio Basecamp.
- DORA 2025: el informe completo (PDF) no se leyó; cifras de la encuesta vienen del blog de Google y de buscador. Falta su modelo de capacidades de IA.
- Estudios de GitClear, CodeRabbit, Veracode: leídos solo vía Wikipedia, sin revisión por pares; marcar como evidencia débil.
- Karpathy: post original no abierto; la cita viene de Wikipedia.
- Lo legal del código generado (autoría, licencias): no buscado; pide dos fuentes independientes.
- No cubrí DevOps, Arquitectura, Producto, IA ni Ventas (vecinos).
