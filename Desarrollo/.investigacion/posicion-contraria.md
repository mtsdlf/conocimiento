# Posición contraria: evidencia en contra de lo que la base va a afirmar

Informe de investigación para el tema Desarrollo de software. Ángulo: buscar la mejor evidencia en contra de lo que la base afirmaría (que lo clásico pierde peso, que los agentes aceleran, que conviene spec-driven y TDD). Fecha de la búsqueda: 2026-11-27. Marcas de lectura: [L] texto completo (en realidad, la página o el abstract leído con WebFetch, que resume con un modelo chico: las citas literales salen de ahí), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U).

Aviso de método: WebFetch devuelve un resumen hecho por un modelo, no el texto crudo; lo que dice "literal" son frases que el resumen entrecomilló. Los PDF de Royce (1970) y del informe DORA 2024 no se pudieron leer (escaneado y 403 / demasiado grande). Eso marca varios huecos.

## Resumen de lo que más cambia el árbol

1. La tesis "los agentes aceleran el desarrollo" no se puede afirmar sin matices en ninguna de las dos direcciones. Hay RCT a favor (Peng 55,8 %; Google ~21 %; Cui et al. +26,08 % de tareas) y en contra (METR 2025: +19 % de tiempo), y METR misma dijo en 2026 que su diseño ya no mide bien. DORA 2025 dice que el rendimiento mejora pero la estabilidad sigue empeorando.
2. Lo único robusto en contra: más cambio por unidad de tiempo sin controles (pruebas, lotes chicos, feedback rápido) produce inestabilidad (DORA 2025). Esto refuerza la escuela del tema (pasos chicos y prueba como especificación) y es el mejor argumento para `verificar-lo-que-hizo-un-agente`.
3. Spec-driven development no tiene evidencia empírica; tiene una crítica fundada (Böckeler) y está en Assess en el Radar de noviembre de 2025. El ALCANCE lo trata como "práctica emergente con su evidencia": la evidencia hoy es de práctica, no de estudios.
4. Varios ítems de "lo que pierde peso" del ALCANCE tienen respaldo desigual: story points como productividad (Radar Hold, 2015) y cobertura como objetivo (estudio ICSE 2014) están bien respaldados; Scrum ceremonial y estimación en horas, no (no encontré estudio ni entrada del Radar). Hay que decirlo así en la nota.
5. Mitos documentados que la base no debe repetir: "Royce propuso la cascada", "el CHAOS report prueba que el 84 % falla", "el 10x programador está probado", "la ley de Brooks es una ley".
6. TDD: la evidencia causal es nula o mixta (familia de 12 experimentos). La base debe presentarlo como práctica de diseño y feedback, no como mejora probada de calidad. Con agentes, el Radar lo pone como refuerzo (Complacency with AI-generated code, Hold/Caution).

---

## Componente 1. Lo que pierde peso

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Radar: "Velocity as productivity" (Hold, ed. de Jan 2015) | primaria (práctica) | 2/1/1/2 | [L] | https://www.thoughtworks.com/radar/techniques/velocity-as-productivity |
| Radar: "Four key metrics" (Adopt) | primaria (práctica) | 2/1/1/2 | [S] | https://www.thoughtworks.com/en-us/radar/techniques/four-key-metrics |
| Inozemtseva y Holmes, ICSE 2014, "Coverage is not strongly correlated with test suite effectiveness" | primaria (estudio) | 3/3/2/3 | [S] | https://cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf |
| Ivanković et al., "Code coverage at Google", FSE 2019 | primaria (estudio) | 3/2/2/3 | [S] | https://research.google/pubs/code-coverage-at-google/ |
| Tawosi, Moussa y Sarro, ESEM 2022, story points | primaria (estudio) | 2/2/1/2 | [S] | https://solar.cs.ucl.ac.uk/pdf/tawosi2022esem.pdf |
| Vetro et al. (Politecnico di Torino), estimación en Scrum | primaria (estudio) | 2/1/1/2 | [S] | https://iris.polito.it/retrieve/handle/11583/2722515/224876 |
| Menzies, Nichols, Shull y Layman, EMSE 2017, "Are delayed issues harder to resolve?" | primaria (estudio) | 3/3/2/3 | [M] | https://arxiv.org/abs/1609.04886 |
| Bacchelli y Bird, ICSE 2013, code review en Microsoft | primaria (estudio) | 3/3/2/3 | [S] | https://microsoft.com/en-us/research/?p=164195 |
| Sadowski et al., ICSE-SEIP 2018, code review en Google | primaria (estudio) | 3/2/2/3 | [S] | https://research.google/pubs/modern-code-review-a-case-study-at-google/ |
| Dybå y Dingsøyr 2008; Rytkönen et al. PROFES 2024; Verwijs y Russo 2021 (revisiones de evidencia ágil) | primarias (revisiones) | 3/2/1/3 | [S] | https://jyx.jyu.fi/jyx/Record/jyx_123456789_99071/Description y https://unpaywall.org/10.1007%2F978-3-031-78386-9_21 |
| Jørgensen, "A review of studies on expert estimation of software development effort" (JSS 2004) | primaria (revisión) | 3/3/2/3 | [S] | https://www.simula.no/research/review-studies-expert-estimation-software-development-effort |
| Radar: "Complacency with AI-generated code" (Hold, ed. Nov 2025) | primaria (práctica) | 2/1/1/2 | [L] | https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code |
| Radar vol. 35 (nov 2026), sobre review como cuello de botella | secundaria (buscador) | 2/1/1/1 | [S] | https://thoughtworks.com/radar |
| Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl" | primaria (práctica) | 2/2/2/3 | [L] | https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html |

Nota sobre el anillo: en el Radar actual el anillo exterior se llama Caution y ya no hay Hold (según el buscador sobre el Radar; https://www.thoughtworks.com/en-ec/radar). Las entradas viejas (2015) aparecen todavía como Hold en su página. Coincide con lo que dice `Arquitectura/Fundamentos/lo-que-pierde-peso.md`. Recencia: las páginas del Radar dicen que lo que no está en las últimas ediciones puede ya no reflejar la opinión actual.

### Ítem (a). El documento de requisitos gigante al principio (BRUF)

- **A favor de que pierde peso.**
  - Böckeler, sobre spec-kit: "I'm very skeptical that lots of up-front spec design is a good idea" y "The past has shown that the best way for us to stay in control of what we're building are small, iterative steps" (https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) [L]. Sobre sus salidas: "very verbose and tedious to review".
  - Menzies et al. analizaron 171 proyectos (2006-2014) y no encontraron evidencia consistente de que arreglar un defecto más tarde cueste mucho más; sugieren que el efecto puede ser "a historical relic" (resumen del buscador, https://arxiv.org/abs/1609.04886) [M]. Esto debilita el argumento económico que sostiene gastar mucho en especificar antes (la "curva de costo del cambio"), pero no es un estudio sobre BRUF.
  - Royce no defendió la pasada única (ver componente 4).
- **En contra de que pierde peso.** No encontré un estudio que compare BRUF con requisitos iterativos. Las normas (ISO/IEC/IEEE 29148) siguen describiendo documentos de requisitos, y spec-driven development vuelve a poner la especificación escrita antes del código: el Radar lo tiene en Assess (nov 2025) y lo describe como "an emerging approach to AI-assisted coding workflows" con flujos que "remain elaborate and opinionated" (https://www.thoughtworks.com/radar/techniques/spec-driven-development) [L]. Hay una tensión que la base tiene que mostrar: se dice que el documento gigante pierde peso y a la vez se recomienda la especificación como insumo principal.
- **Veredicto.** Pierde peso el documento único, completo y congelado antes de empezar; no pierde peso la especificación por tramos chicos. Quién lo dice: Böckeler (practicante), Menzies (estudio, indirecto). Sin estudio directo: marcar como criterio de la base.

### Ítem (b). Story points y velocity como medida de productividad

- **A favor.** El Radar puso "Velocity as productivity" en Hold (edición Jan 2015; https://www.thoughtworks.com/radar/techniques/velocity-as-productivity) [L]: avisa que se usa para jugar la métrica en vez de entregar software andando. La misma página dice que la velocity sirve como estimación de capacidad interna del equipo. "Four key metrics" (DORA) está en Adopt [S] como alternativa. Tawosi et al. (ESEM 2022) encontraron que la estimación en story points "is often not consistent throughout the project" [S]; Pasuksmit et al. (EMSE 2022, 19.349 ítems, seis proyectos) estudian cómo cambian los puntos después de entrar al sprint [S].
- **En contra.** Un blog de Scrum.org dice que los story points son precisos (https://www.scrum.org/resources/blog/why-do-we-use-story-points-estimating): es opinión de la organización que vende Scrum, no estudio. Vetro et al. reportan que al cambiar el proceso de estimación (escala corta no numérica, analogías, retrospectivas de exactitud) la precisión pasó de 10 % a 45 % en un proyecto nuevo [S]: la estimación relativa puede mejorar, pero es un estudio chico.
- **Veredicto.** Sólido: pierde peso como medida de productividad (Radar Hold 2015, estudios). No pierde peso como ayuda de planificación interna. Con agentes: no encontré ninguna fuente sobre si los story points sirven cuando el código lo escribe un agente (hueco); la base no debería afirmarlo.

### Ítem (c). Scrum con todas sus ceremonias

- **A favor de que pierde peso.** Hay poca evidencia empírica sobre beneficios ágiles en relación con su popularidad: Rytkönen et al. (PROFES 2024) concluyen que hay "far less empirical evidence on agile benefits than the method's popularity would suggest" (resumen del buscador, https://unpaywall.org/10.1007%2F978-3-031-78386-9_21) [S]. Dybå y Dingsøyr (2008) ya pedían más estudios.
- **En contra.** No es evidencia de que dañe: Verwijs y Russo (ACM TOSEM 2021) construyeron una teoría de efectividad de equipos Scrum con trece estudios de campo y la validaron con ecuaciones estructurales [S]. No encontré (a) ninguna entrada del Radar en Hold/Caution contra Scrum, (b) ningún meta-análisis que aísle el daily, la retro o la planning. 
- **Veredicto.** Es criterio de la base, no un hallazgo: la evidencia es escasa en las dos direcciones. Recomiendo escribirlo así ("sin evidencia sólida ni a favor ni en contra; se contrasta como proceso predefinido frente a la entrega continua con medidas DORA") y no con un "Scrum pierde peso" a secas.

### Ítem (d). Gitflow

Ya tiene nota en DevOps (`/home/dela/repos/personal/conocimiento-desarrollo/DevOps/Ramas-y-versiones/gitflow.md`), que cita a Driessen: en su nota de 2020 recomienda algo más simple para quien hace entrega continua. No busqué más. Hueco: no verifiqué en esta ronda si DORA mide trunk-based como capacidad (la base de DevOps probablemente lo cubre); si se cita, que se cite a DevOps y no se repita acá. Veredicto: se nombra y se enlaza.

### Ítem (e). La cobertura de pruebas como objetivo

- **A favor.** Inozemtseva y Holmes (ICSE 2014, premio Distinguished Paper de ACM SIGSOFT) observaron correlación de baja a moderada entre cobertura y efectividad al controlar por el número de casos; concluyen que la cobertura sirve para encontrar código poco probado pero no como objetivo de calidad (resumen del buscador; https://cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf) [S].
- **En contra.** Ivanković et al. (FSE 2019) describen la cobertura en Google calculada para mil millones de líneas por día en siete lenguajes, con 512 respuestas de una encuesta (https://research.google/pubs/code-coverage-at-google/) [S]: se usa como señal en cada cambio. No leí qué opinaron los desarrolladores. Hay también trabajos posteriores con otras conclusiones (un resumen del buscador dice que un trabajo posterior discrepa con el de 2014; no lo identifiqué).
- **Con agentes.** Un agente puede inflar la cobertura escribiendo pruebas triviales; no encontré estudio sobre eso (hueco). El Radar recomienda reforzar "TDD and static analysis" frente a la complacencia (https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code) [L].
- **Veredicto.** Sólido como objetivo; la cobertura sigue valiendo como señal de lo que no se probó.

### Ítem (f). Estimación detallada en horas de cada tarea

- **A favor de que pierde peso.** Jørgensen (2004) concluye que la estimación por juicio experto es la más usada y que no hay evidencia sustancial a favor de los modelos formales (https://www.simula.no/research/review-studies-expert-estimation-software-development-effort) [S]. En su revisión de 2007, citando a Moløkken-Østvold y Jørgensen (2003), los proyectos gastan "roughly 30–40% more effort than estimated" y la exactitud no mejoró con los años (https://web-backend.simula.no/sites/default/files/publications/Jorgensen.2007.2.pdf, resumen del buscador) [S]. Es evidencia de que la estimación detallada sistemáticamente se queda corta, no de que haya que abandonarla.
- **En contra.** La misma literatura trae doce prácticas de estimación experta con evidencia a favor (combinar estimaciones de varios, usar datos históricos). Nada de lo hallado compara estimar tarea por tarea en horas contra estimar en grueso.
- **Veredicto.** Sin estudio que lo zanje. Se puede afirmar que el desvío de 30-40 % es sistemático; no que estimar en horas "pierde peso". Con agentes: no encontré datos sobre estimar tareas hechas por un agente (hueco grande, y es la pregunta central de `estimacion`).

### Ítem (g). Code review línea por línea como único control

- **A favor de que pierde peso.** Bacchelli y Bird (ICSE 2013, Microsoft) hallaron que la revisión es "less about defects than expected" y rinde conocimiento compartido, conciencia de equipo y soluciones alternativas; los comentarios sobre defectos son una proporción chica [S] (https://microsoft.com/en-us/research/?p=164195). Sadowski et al. (Google, 2018; 12 entrevistas, 44 respuestas, 9 millones de cambios revisados) la sostienen como herramienta educativa y de claridad [S]. O sea: ni siquiera antes de los agentes servía como único control de defectos. Radar vol. 35 (nov 2026): cuando la revisión no da abasto, la supervisión "puede volverse una formalidad" (secundaria, resumen del buscador de https://thoughtworks.com/radar) [S]; vol. 34 pone controles deterministas y sensores antes de la revisión humana.
- **En contra.** La revisión no se descarta: cumple funciones que las pruebas no cumplen (conocimiento compartido, claridad). Perry et al. (ver componente 2) muestran que los usuarios de asistentes escribían código menos seguro y creían lo contrario: eso pide más control humano, no menos.
- **Veredicto.** Pierde peso como único control; no pierde peso como práctica. Hay estudios de antes de los agentes; no encontré uno sobre revisar código de agentes (hueco).

### Otros ítems propuestos (con fuente)

| Ítem | Fuente | Veredicto |
|---|---|---|
| "Complacency with AI-generated code": confiar sin verificar | Radar, Hold, nov 2025: "increasingly highlighting concerns about complacency with AI-generated code" (https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code) [L] | Entra: no es una práctica clásica en declive, es un riesgo nuevo; va a `verificar-lo-que-hizo-un-agente` |
| Especificaciones largas y elaboradas por defecto con agentes | Radar, SDD en Assess (nov 2025); Böckeler | Se sostiene como cautela, no como declive |
| Curva de costo del cambio exponencial como justificación de la planificación previa | Menzies et al. 2017 [M] | Se sostiene con reservas: 171 proyectos de un grupo (TSP), no es evidencia universal |
| La documentación completa antes de codificar como "calidad" | sin fuente propia | Descartado: no hay evidencia |
| Pair programming "porque sí" | no investigado | Descartado por falta de fuente |

---

## Componente 2. Evidencia contra "los agentes aceleran el desarrollo", y a favor para balancear

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Becker, Rush, Barnes y Rein (METR), arXiv 2507.09089, jul 2025 | primaria, preprint sin revisión por pares (a confirmar) | 3/3/3/3 | [M] | https://arxiv.org/abs/2507.09089 |
| METR, "uplift update", 24 feb 2026 | primaria | 3/3/2/3 | [L] | https://metr.org/blog/2026-02-24-uplift-update/ |
| DORA 2024 (resumen en dora.dev) | primaria | 3/1/1/3 | [M] | https://dora.dev/research/2024/dora-report/ |
| DORA 2024, cifras 1,5 % y 7,2 % (Google Cloud, TechTarget, The New Stack) | secundaria | 2/1/1/1 | [S] | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report |
| DORA 2025, anuncio de Google Cloud | primaria | 3/2/1/3 | [L] | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report |
| GitClear, "AI Copilot Code Quality 2025" | primaria de un proveedor | 1/2/2/2 | [S] | https://www.gitclear.com/ai_assistant_code_quality_2025_research |
| Pearce et al., "Asleep at the Keyboard?", arXiv 2108.09293 | primaria (estudio; publicado en IEEE S&P 2022) | 3/3/2/3 | [M] | https://arxiv.org/abs/2108.09293 |
| Perry, Srivastava, Kumar y Boneh, CCS 2023, arXiv 2211.03622 | primaria (estudio con usuarios) | 3/3/2/3 | [M] | https://arxiv.org/abs/2211.03622 |
| Veracode, GenAI Code Security Report 2025 | primaria de un proveedor | 1/2/2/2 | [S] | https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/ |
| Liang, Garg y Moghaddam, "The SWE-Bench Illusion", arXiv 2506.12286 | primaria, preprint | 2/2/2/3 | [M] | https://arxiv.org/abs/2506.12286 |
| OpenAI, "Why we no longer evaluate SWE-bench Verified", 23 feb 2026 | primaria | 2/2/2/3 | [L] | https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ |
| Anthropic, "AI assistance and coding skills", 29 ene 2026 (arXiv 2601.20245) | primaria | 2/2/2/3 | [S] | https://www.anthropic.com/research/AI-assistance-coding-skills |
| Peng, Kalliamvakou, Cihon y Demirer, arXiv 2302.06590 | primaria, preprint | 3/2/2/3 | [M] | https://arxiv.org/abs/2302.06590 |
| Paradis et al. (Google), arXiv 2410.12944 | primaria, preprint | 3/2/2/3 | [M] | https://arxiv.org/abs/2410.12944 |
| Cui, Demirer, Jaffe, Musolff, Peng y Salz, Management Science (SSRN 4945566) | primaria | 3/3/2/3 | [S] | https://papers.ssrn.com/abstract=4945566 |

### En contra

- **METR (RCT, 2025).** 16 desarrolladores con unos 5 años de experiencia en repositorios maduros de código abierto, 246 tareas asignadas al azar para permitir o prohibir IA de comienzos de 2025: "Allowing AI increased task completion time by 19%". Los desarrolladores habían pronosticado una reducción de 24 % y después estimaron una de 20 % (https://arxiv.org/abs/2507.09089) [M]. Intervalo de confianza del 95 %: +2 % a +39 % (https://metr.org/blog/2026-02-24-uplift-update/) [L]. Límites: 16 personas, proyectos propios maduros, herramientas de 2025.
- **METR actualiza en 2026, lo que matiza el anterior.** Nuevo experimento desde agosto de 2025: 57 desarrolladores, 143 repositorios, más de 800 tareas. Reportó -18 % (IC -38 % a +9 %) para los 10 desarrolladores originales y -4 % (IC -15 % a +9 %) para los nuevos, en la convención de la página, que habla de "speedup" negativo. Pero METR dice que la señal es poco fiable: muchos desarrolladores no quisieron participar si no podían usar IA, y entre 30 % y 50 % retuvo tareas que no quería hacer sin IA. Cita literal: los desarrolladores probablemente están "more sped up from AI tools now", aunque los datos son "only very weak evidence for the size of this increase" [L]. Hoy no hay una cifra nueva citable.
- **DORA 2024.** El resumen de dora.dev dice que la IA "significantly increases individual productivity, flow, and job satisfaction" pero "negatively impacts software delivery stability and throughput" (https://dora.dev/research/2024/dora-report/) [M]. Las cifras (-1,5 % en rendimiento y -7,2 % en estabilidad por cada 25 % más de adopción) aparecen solo en fuentes secundarias (Google Cloud, TechTarget, The New Stack); no pude abrir el PDF para confirmar el método [S]. Dos fuentes secundarias no valen como independientes si repiten a Google.
- **DORA 2025 (casi 5.000 profesionales; encuesta del 13 de junio al 21 de julio de 2025).** Citas literales: "Unlike last year, we observe a positive relationship between AI adoption on both software delivery throughput and product performance." y "However, AI adoption does continue to have a negative relationship with software delivery stability." También: "Without robust control systems, like strong automated testing, mature version control practices, and fast feedback loops, an increase in change volume leads to instability." y "AI doesn't fix a team; it amplifies what's already there." 90 % usa IA en el trabajo; 30 % desconfía poco o nada del código generado (https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) [L]. Son correlaciones de encuesta, no ensayos.
- **Calidad y duplicación (GitClear).** 211 millones de líneas cambiadas de 2020 a 2024. Las líneas copiadas y pegadas pasaron de 8,3 % a 12,3 %, y las movidas (señal de refactor) bajaron de 24,1 % a 9,5 %; 2024 fue el primer año en que se copió más de lo que se movió. Un 8x en bloques duplicados circula en la prensa. Cuidado: GitClear vende análisis de código, la cifra de 8x es de cobertura secundaria y el estudio es observacional, sin control de causa [S] (https://www.gitclear.com/ai_assistant_code_quality_2025_research).
- **Seguridad.** Pearce et al.: 1.689 programas en 89 escenarios, "approximately 40% to be vulnerable" (Copilot de 2021) [M]. Perry et al. (Codex-davinci-002): quienes usaron el asistente escribieron "significantly less secure code" y creyeron más que su código era seguro; confiar menos en la IA y reformular los prompts iba con menos vulnerabilidades [M]. Veracode (2025): 80 tareas, más de 100 modelos, "introduces security vulnerabilities in 45 percent of cases"; Java con más de 70 %; modelos más grandes y nuevos no mejoran la seguridad [S]. Los tres miden modelos viejos o benchmarks propios: la cifra no es "el porcentaje del código real con IA".
- **Críticas a SWE-bench.** Liang et al.: hasta 76 % de acierto al identificar el archivo con falla solo desde el texto del issue, y 53 % en repositorios fuera de SWE-bench; reproducción verbatim (5-gramas) hasta 35 % en SWE-bench Verified contra 18 % en otros benchmarks [M]. OpenAI (23 feb 2026) dejó de reportar SWE-bench Verified: lo llama "increasingly contaminated" y, en 138 problemas que o3 no resolvía de forma consistente, "59.4% of the 138 problems contained material issues in test design and/or problem description" (35,5 % con pruebas demasiado estrechas, 18,8 % demasiado anchas, 5,1 % otros) [L]. Recomienda SWE-bench Pro. Un estudio citado de segunda mano (Wang et al.) dice que correr todas las pruebas baja el rendimiento 4,5 % y que 28,6 % de las muestras evidentemente incorrectas pasa igual [S, sin verificar]. Implicación para la base: no citar puntajes de SWE-bench Verified como prueba de capacidad.
- **Habilidad.** Anthropic (29 ene 2026): 52 ingenieros mayormente junior aprendiendo la librería Trio; el grupo con IA sacó 17 % menos en un cuestionario posterior, sin ser significativamente más rápido (unos 23 contra 25 minutos, p = 0,391); lo más débil, depurar. Quienes hicieron preguntas conceptuales a la IA rindieron mejor [S]. Es un laboratorio con una librería nueva.
- **"Productivity paradox".** No encontré un estudio primario con ese nombre; las notas de prensa (TechCrunch, TheNextWeb) lo usan para la brecha entre percepción y medición de METR. No lo uso como fuente.

### A favor (para balancear)

- **Peng et al. (Copilot, preprint).** El grupo con Copilot "completed the task 55.8% faster" implementando un servidor HTTP en JavaScript "as quickly as possible" (https://arxiv.org/abs/2302.06590) [M]. Tarea de laboratorio, aislada y corta; el abstract no traía el tamaño de muestra en lo que leí.
- **Google (Paradis et al.).** RCT empresarial con 96 ingenieros de Google; mejor estimación de aproximadamente 21 % de ahorro de tiempo, con "our confidence interval is large", en un estudio de laboratorio con herramientas internas del verano de 2024 (https://arxiv.org/abs/2410.12944) [M].
- **Cui et al. (Management Science).** Tres experimentos de campo en Microsoft, Accenture y un fabricante Fortune 100; análisis agrupado de 4.867 desarrolladores: aumento de 26,08 % en tareas completadas (error estándar 10,3 %), con resultados que varían entre experimentos; los menos experimentados adoptaron y ganaron más (https://papers.ssrn.com/abstract=4945566) [S].
- **DORA 2025.** El rendimiento de entrega y el desempeño del producto correlacionan positivamente con la adopción (primera cita arriba).

### Lectura equilibrada
Las tres señales discrepan porque miden cosas distintas: el tiempo de una tarea de laboratorio (Peng, Google), tareas reales en un repositorio conocido (METR 2025, -19 % de velocidad), tareas completadas en equipos (Cui) y la estabilidad del sistema entregado (DORA). Lo que se puede afirmar con respaldo: la IA acelera la escritura y el cambio, y la estabilidad depende de los controles alrededor (DORA 2025). Lo que no se puede: "los agentes aceleran el desarrollo" sin decir en qué medida, con qué herramienta de qué fecha y con qué controles. Todo esto es volátil y debe llevar fecha.

### Qué cambia con agentes y qué pierde peso
Pierde peso el argumento "escribir código es el cuello de botella" (DORA 2025: la aceleración "can expose weaknesses downstream") y la revisión humana línea por línea como control suficiente (Radar vol. 35). Gana peso lo que ya dice el tema: lotes chicos, pruebas automáticas y retroalimentación rápida.

### Recurso canónico
DORA 2025 (https://dora.dev/dora-report-2025/): el capítulo sobre las siete capacidades que magnifican el efecto de la IA; fijarse en que son correlaciones de encuesta. Segundo: METR (2025) y su actualización de 2026 juntas, para ver por qué un RCT sobre IA se vuelve difícil de repetir.

---

## Componente 3. Evidencia contra spec-driven, TDD, #NoEstimates y contratos ágiles de precio fijo

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl" (martinfowler.com) | primaria (práctica, probó herramientas) | 2/2/3/3 | [L] | https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html |
| Radar: "Spec-driven development" (Assess, nov 2025) | primaria (práctica) | 2/1/1/2 | [L] | https://www.thoughtworks.com/radar/techniques/spec-driven-development |
| Santos, Vegas, Dieste et al., "A Family of Experiments on Test-Driven Development" (arXiv 2011.11942) | primaria (meta-análisis) | 3/3/2/3 | [M] | https://arxiv.org/abs/2011.11942 |
| Fucci et al., "A Dissection of the TDD Process" (arXiv 1611.05994) | primaria | 3/2/2/2 | [S] | https://ar5iv.arxiv.org/html/1611.05994 |
| Reseña de InfoQ del libro #NoEstimates | secundaria | 1/1/1/2 | [S] | https://www.infoq.com/articles/book-review-noestimates |
| Ron Jeffries, "The NoEstimates movement" | primaria (practicante) | 2/2/1/2 | [S] | https://ronjeffries.com/xprog/articles/the-noestimates-movement/ |
| McConnell, respuesta a Jeffries | primaria (practicante) | 2/2/1/2 | [S] | https://stevemcconnell.com/?p=234 |
| Gaebert, estudios sobre contratos de precio fijo (Springer) | primaria (estudio) | 2/2/1/2 | [S] | https://link.springer.com/chapter/10.1007/978-3-319-21915-8_2 |
| Wikipedia "Agile contracts" (para ubicar a Opelt et al.) | secundaria, solo para ubicar | 1/1/1/1 | [S] | https://en.wikipedia.org/wiki/Agile_contracts |

### Spec-driven development
- **Böckeler** probó Kiro, spec-kit y Tessl. Citas literales: sobre el flujo de Kiro, "like using a sledgehammer to crack a nut"; sobre spec-kit, "overkill for the size of the problem", "very verbose and tedious to review", y "To be honest, I'd rather review code than all these markdown files"; "I frequently saw the agent ultimately not follow all the instructions"; con Tessl, la misma especificación regenerada produjo código distinto y se pregunta si se combinan "Inflexibility and non-determinism" [L]. El artículo no usa la palabra "waterfall" (verificado en la lectura); la frase "waterfall con otro nombre" que circula no es suya y no debe atribuírsele. Lo más cercano es su escepticismo hacia el diseño de especificaciones extensas por adelantado.
- **Radar.** Assess, noviembre de 2025: "We may be relearning a bitter lesson" (escrito como observación tentativa) y que escribir a mano reglas detalladas para la IA "ultimately doesn't scale"; advierte que algunas herramientas generan archivos largos y difíciles de revisar, y que no está claro quién es el usuario de sus PRD o historias [L]. Esa entrada ya no está en la edición actual, con la advertencia de la página de que su evaluación puede haber cambiado.
- **Lo que no hay.** Ni un estudio controlado ni uno observacional sobre spec-driven. Las fuentes a favor que busqué son documentación de herramientas (GitHub Spec Kit, Kiro) que corresponden a otro componente.
- **Qué hacer.** Afirmar spec-driven como práctica emergente sin evidencia empírica; dejar la crítica de Böckeler visible: el tamaño de la tarea decide si la especificación formal se justifica. Recurso canónico: el artículo de Böckeler completo, fijándose en los casos donde el agente ignora la especificación.

### TDD
- **Evidencia en contra.** La familia de 12 experimentos (Santos et al., con meta-análisis) halló que los novatos lograron "slightly higher code quality" con test-last iterativo que con TDD; que el orden de aplicación y el efecto de aprendizaje no parecen afectar la calidad; que la tarea tuvo la mayor influencia y que los profesionales con TDD mostraron una caída de calidad mayor que los estudiantes [M]. El abstract leído no informa sobre productividad. Fucci et al. (82 puntos de dato de 39 profesionales): lo que importa no es probar primero ni después sino la granularidad y la uniformidad de los pasos, según el resumen del buscador [S]. Una réplica no halló evidencia de mejora de calidad externa ni productividad (resumen del buscador, sin URL propia verificada). Todo viene del grupo de Oulu/Turhan/Fucci y de estudios con estudiantes, y los autores hacen notar que el efecto depende de las características del estudio.
- **En contra de la crítica.** Los mismos estudios hallan suites de pruebas más grandes con mayor capacidad de detección de fallas (según resumen del buscador) [S]. Y el Radar recomienda "reinforcing established practices such as TDD and static analysis" frente a la complacencia con el código de IA [L]: aquí TDD vale como control, no como método de diseño probado.
- **Qué hacer.** Escribir TDD como práctica con evidencia causal nula o mixta en calidad y de valor como contrato y retroalimentación (criterio de la escuela Beck/Farley). No prometer menos defectos.

### #NoEstimates
- **Contra.** Un crítico señala que "neither wing" puede mostrar casos reales y que el relato del libro de Duarte es ficticio (reseña de InfoQ) [S]. Zuill propone dejar de estimar; Duarte, empezar y pronosticar tras unos sprints [S]. McConnell publicó una respuesta punto por punto a Jeffries [S]; no leí el detalle.
- **A favor.** Duarte sostiene que planificar no exige estimar. Jørgensen (componente 1) documenta que las estimaciones se pasan 30-40 % en esfuerzo: es un argumento de fondo para cuestionar la estimación, aunque no valida #NoEstimates.
- **Hueco.** Ningún estudio empírico de proyectos sin estimaciones. La base debería describir el pronóstico por flujo (conteo de ítems y tiempo de ciclo) como técnica sin evidencia comparativa, con la crítica visible.

### Contratos ágiles con precio fijo
- **Una sola línea de evidencia, delgada.** Aviso: dinero y ley piden dos fuentes independientes; solo tengo una de estudio y una que ubica el libro. Opelt et al. (*Agile Contracts*, libro) proponen un precio indicativo que se vuelve vinculante después de una fase de verificación de dos a cinco sprints (resumen de Wikipedia, que es secundaria) [S]. Gaebert: los clientes confiables permiten contratos de precio fijo creíbles y las cláusulas sofisticadas no tienen ese efecto [S]. Una tesis de Portsmouth dice que "still no substantial academic research" había sobre Scrum bajo precio fijo cerrado, y una tesis de práctica (Fuller) dice que su aplicación exitosa con alcance y plazo predeterminados "has not been proven" [S]. Hay muchos hallazgos de práctica, pero no estudios con muestra grande.
- **Qué hacer.** En `estimacion` y `cambios-de-alcance` decir que el precio fijo con alcance variable es práctica de consultores sin respaldo empírico, y que lo que sí tiene respaldo (Jørgensen) es que las estimaciones se pasan, por lo que un precio fijo transfiere ese riesgo al proveedor. Legal y comercial va con Ventas.

### Con agentes
Böckeler y el Radar son de 2025; ambos tratan de agentes. Para estimar y cobrar cuando el código sale casi gratis no encontré estudio ni fuente con método (hueco grande: pregunta 4 del ALCANCE).

---

## Componente 4. Concepciones erróneas documentadas

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Royce, "Managing the Development of Large Software Systems" (1970) | primaria | 3/3/3/3 | no leída (PDF escaneado) | https://www.praxisframework.org/files/royce1970.pdf |
| "A Brief History of the Waterfall Model: Past, Present, and Future" (arXiv 2510.03894) | primaria/secundaria (historia), preprint | 2/2/2/2 | [L] | https://arxiv.org/html/2510.03894v3 |
| Eveleens y Verhoef, "The Rise and Fall of the Chaos Report Figures", IEEE Software 27(1), 2010 | primaria (estudio) | 3/3/2/3 | [S] | https://ieeexplore.ieee.org/document/5232804 |
| Sackman, Erickson y Grant (1968) y Bossavit, *The Leprechauns of Software Engineering* | primaria y secundaria | 2/3/2/3 | [S] | https://leanpub.com/read/leprechauns/leanpub-auto-chapter-7-whos-afraid-of-the-big-bad-waterfall |
| SEI, "Programmer Moneyball" | primaria (blog institucional) | 2/1/1/2 | [S] | https://www.sei.cmu.edu/blog/programmer-moneyball-challenging-the-myth-of-individual-programmer-productivity |
| McConnell, "Brooks' Law Repealed" (IEEE Software 1999), vía CACM; Capiluppi y Adams 2009 | primarias, vistas por secundaria | 2/1/1/2 | [S] | https://cacm.acm.org/blogcacm/in-search-of-the-shortest-possible-schedule y https://link.springer.com/content/pdf/10.1007/978-3-642-02032-2_24.pdf |

- **Royce y la cascada.** La historia de 2025 dice que el artículo de Royce criticaba el enfoque rígido de pasada única para sistemas grandes; recomendaba ejecutar el ciclo al menos dos veces ("provides an early simulation of the final product" en la primera pasada); la palabra "waterfall" no aparece en el original y la popularizaron Bell y Thayer en 1976 [L]. Otro crítico argumenta que los primeros trabajos que describen un modelo secuencial son anteriores (al menos 1956) [S]; la historia leída da 1987 para el artículo de Benington que cita, así que ese año queda sin resolver. La frase "I believe in this concept, but the implementation described above is risky and invites failure" solo la vi en una publicación de LinkedIn (no usable); hay que verificarla en el PDF original antes de entrecomillarla. Veredicto: se puede decir que Royce no propuso la cascada pura y que su figura 3 es una descripción para criticarla; hay que contrastar con el PDF.
- **CHAOS report.** Eveleens y Verhoef: las cifras agregadas de Standish no tienen sentido porque combinan estimaciones hechas con procesos distintos y sesgos desconocidos, y no coincidían con los casos reales que examinaron [S]. El informe de 1994 daba 16 % de éxito. Los datos no son públicos y los hallazgos no fueron replicados (CACM; Glass 2006) [S]. Veredicto: no citar "x % de los proyectos fracasan" del CHAOS como dato. Una cifra citada en un blog (sobrecostos de 45 % y 56 % menos de valor) no tiene estudio identificado; la descarto.
- **El 10x developer.** Origen: Sackman, Erickson y Grant (1968), 12 programadores en dos grupos; la crítica de Bossavit es que compara el mejor caso de uno con el peor de otro con tareas distintas; Dickey reanalizó y concluyó que "only a range of 5:1 can be attributed to programmer variability" [S]. En el otro lado, McConnell (*Making Software*) sostiene que hay evidencia empírica de una diferencia de 10:1 entre el mejor y el promedio [S]; el SEI ve evidencia contra la idea de que algunos programadores sean inherentemente mucho más productivos [S]. Veredicto: hay variabilidad grande entre personas, pero la cifra 10x no está bien sostenida; las dos posturas van con su fuente. No encontré Plat_Forms (Prechelt), hueco.
- **Ley de Brooks.** Su alcance es acotado: aplica a agregar gente a un proyecto que ya está atrasado [S]. McConnell (1999) la "repeal" y argumenta con curvas de costo-tiempo; estudios con grandes datos de GitHub dan resultados discrepantes entre sí (Gote et al. 2022; una réplica de 2025 explica la discrepancia por problemas de método) [S]; Capiluppi y Adams (KDE, 2009) hallan que se cumple entre los desarrolladores centrales [S]. Veredicto: dar las dos posturas; llamarla "ley" es una exageración. Con agentes: sumar agentes a un trabajo no es lo mismo que sumar personas (costo de comunicación y de contexto distinto), pero no hay estudio que lo compare (hueco).

### Qué cambia con agentes
Estos mitos se vuelven a repetir con la IA (el "10x" reaparece como "un solo desarrollador con un agente rinde 10x"). Ninguna de las fuentes leídas prueba eso; el RCT de Cui sugiere que ganan más los menos experimentados, lo contrario de lo que sugeriría el mito.

---

## Huecos

1. Royce 1970 en el original: PDF escaneado, sin OCR. Hay que verificar las citas y los cinco pasos que agrega.
2. DORA 2024 y 2025 completos: no se leyeron los PDF; las cifras de -1,5 % y -7,2 % salen de fuentes secundarias, y los nombres de las siete capacidades de 2025 no se obtuvieron.
3. GitClear: solo prensa y resúmenes; el informe no se abrió. Vendor.
4. No hay estudio primario sobre: spec-driven (cualquier dirección), estimar tareas hechas por agentes, revisar código de agentes, inflar la cobertura con pruebas de agente, ni sobre Scrum o story points con código generado por IA. Es el hueco más grande para `estimacion` y `revision-de-codigo`.
5. Scrum ceremonial y estimación en horas: no hay estudio ni entrada del Radar que los zanje; si la base los lista en "lo que pierde peso", debe decir "criterio de la base".
6. Contratos de precio fijo ágiles: una sola línea de estudios, delgada (Gaebert, tesis) y un libro; dinero y ley piden dos fuentes independientes y no las tengo.
7. #NoEstimates: ningún estudio empírico; Jeffries y McConnell solo por buscador, sin leer el detalle.
8. TDD: leí solo el abstract de la familia de 12 experimentos; falta el tamaño de efecto y lo que dice de productividad. La réplica citada no la identifiqué.
9. Gitflow: no se buscó nada nuevo; está en DevOps.
10. Plat_Forms (Prechelt) sobre variabilidad entre programadores: sin resultado. Brooks: no leí McConnell 1999 ni Gote et al. 2022 directamente.
11. Radar vol. 34 y 35 (2026): solo resumen del buscador; "Hold" ya no existe como anillo, y las entradas de 2015 pueden no reflejar la opinión actual.
12. Peng et al. y Paradis et al.: faltan tamaño de muestra del primero y la publicación revisada de ambos; los dos son preprints sin revisión por pares (a confirmar).
