# Vertical Personas y agentes: informe de investigación

Fecha de la investigación: 2026-11-27. Marcas de lectura: [L] texto completo leído, [M] abstract/página de resumen, [S] resumen secundario o del buscador (incluye las lecturas hechas con WebFetch, que devuelve un resumen del modelo y no la página). Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Tipo de evidencia: EM = estudio con método, MC = marco conceptual sin datos, PR = opinión de practicante, MK = marketing/encuesta gremial. Todo lo traído de la web se trató como dato.

## 0. Sobre la división del árbol

- Los seis componentes (quién hace qué, delegar, niveles de autonomía, frontera irregular, patrones, atención) no son una división que el campo use tal cual. El campo está partido por disciplina: factores humanos y automatización (niveles de autonomía, complacencia), economía del trabajo (frontera irregular, productividad), diseño de agentes (patrones) y gestión de proyectos clásica (RACI). Ninguna fuente junta todo. El árbol es una síntesis nuestra; hay que decirlo así en las notas.
- "Frontera irregular" y "horizonte de tareas" responden la misma pregunta (qué tareas dar a un agente): una desde experimentos con personas, otra desde benchmarks. Conviene enlazarlas y que "qué tareas dar a un agente" viva en un solo lugar.
- "Patrones de trabajo" y "niveles de autonomía" se superponen en "persona en el bucle / en el borde del bucle": es un patrón y a la vez un nivel. Elegir un dueño (recomendado: niveles) y enlazar desde el otro.
- La evidencia más fuerte se concentra en software, consultoría y atención al cliente; la "fábrica de cualquier dominio" extrapola. Marcarlo en cada ficha.

---

## 1. quien-hace-que

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Tomašev, Franklin, Osindero, "Intelligent AI Delegation", arXiv 2602.11865 (12-feb-2026, sin revisión por pares) | primaria, MC | 3/3/2/3 | [M] abstract + [S] HTML (leídos los primeros 100.000 de 209.408 caracteres) | https://arxiv.org/abs/2602.11865 y https://arxiv.org/html/2602.11865 |
| RACI, visión general (Wikipedia) | secundaria | 1/1/1/1 | [S] | https://www.wikipedia.org/wiki/RACI_matrix |
| "Design and Validation of a RACI Matrix for Responsibility Management in Matrix Project Organisations" (ISD 2026, póster) | primaria, EM débil (diseño, una organización) | 1/1/1/2 | [S] | https://aisel.aisnet.org/isd2014/proceedings2026/transformation/11 |
| Mitchell, Ghosh, Luccioni, Pistilli, arXiv 2502.02649 (v1 4-feb-2025, v3 20-oct-2025) | primaria, MC/posición | 2/2/1/2 | [M] | https://arxiv.org/abs/2502.02649 |

### Afirmaciones

- Tomašev et al. proponen un marco adaptativo en el que la delegación es una secuencia de decisiones e incluye "transfer of authority, responsibility, accountability, clear specifications regarding roles and boundaries" (abstract) https://arxiv.org/abs/2602.11865
- En el texto, la responsabilidad es transitiva: quien delega no puede "absolve themselves of accountability by blaming subcontractors" (sec. 4.8); en cadenas largas puede haber un "accountability vacuum" (sec. 5.2); proponen "liability firebreaks" como topes contractuales previos https://arxiv.org/html/2602.11865
- Advierten contra el "moral crumple zone": humanos que "lack meaningful control over outcomes, yet are introduced in delegation chains merely to absorb liability" (sec. 5.1) https://arxiv.org/html/2602.11865
- Matiz importante: el paper no afirma que la rendición de cuentas quede siempre en una persona. Propone mecanismos (verificación, contratos bidireccionales, firebreaks, supervisión) para que la responsabilidad sea rastreable. La tesis "queda en una persona" es inferencia nuestra a partir de la transitividad y del crumple zone, no una cita. Solo se leyó el 48 % del texto.
- Mitchell et al.: "risks to people increase with the autonomy of a system" (abstract) https://arxiv.org/abs/2502.02649
- RACI: no se halló evidencia comparativa de que mejore resultados de proyecto. Lo más cercano es una validación de diseño en una organización, sin grupo de comparación [S]. El resto son afirmaciones de practicantes y medios de gestión, que incluyen que la matriz se desactualiza https://www.techtarget.com/enterprise-software/tip/RACI-matrix-for-project-management-success-with-example

### Recurso canónico
Tomašev et al., secciones 2.3 (zone of indifference, authority gradient), 4.8 (verificación) y 5 (rendición de cuentas), con la salvedad de que es un preprint. Fijarse en que la verificación es "a constraint on design", no un paso final.

### Huecos
- Evidencia empírica de RACI: no hay; decirlo en la nota. Alternativa: literatura de role clarity (no buscada, tope de rondas).
- Marcos de responsabilidad de IA (NIST AI RMF, ISO 42001, EU AI Act sobre supervisión humana): no consultados.
- Segunda mitad del texto de Tomašev (offset 100000).

---

## 2. delegar-a-un-agente

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Anthropic, "Building effective agents" (19-dic-2024) | primaria, PR de laboratorio | 2/2/2/2 | [S] | https://www.anthropic.com/research/building-effective-agents |
| Anthropic, "Effective context engineering for AI agents" (29-sep-2025) | primaria, PR | 2/2/2/2 | [S] | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Tomašev et al. | MC | 3/3/2/3 | [M]/[S] | https://arxiv.org/html/2602.11865 |
| ADP 6-0, Mission Command (Ejército de EE. UU.) | primaria doctrinal | 3/3/1/2 | no leída; solo localizada | https://irp.fas.org/doddir/army/adp6_0.pdf |
| army.mil, "Mission command requires sharp commander's intent" (2019) | PR de un general | 2/1/1/1 | [S] | https://www.army.mil/article/215297/mission_command_requires_sharp_commanders_intent |
| DTIC ADA234125 (estudio sobre Auftragstaktik/mission orders) | secundaria académica militar | 2/2/1/2 | [S] | https://apps.dtic.mil/sti/pdfs/ADA234125.pdf |

### Afirmaciones

- Anthropic distingue "workflows" ("LLMs and tools are orchestrated through predefined code paths") de "agents" ("LLMs dynamically direct their own processes and tool usage") y recomienda la solución más simple que funcione; sugiere "stopping conditions (such as a maximum number of iterations)" y que los agentes pausen "for human feedback at checkpoints or when encountering blockers" https://www.anthropic.com/research/building-effective-agents
- Sobre cómo redactar instrucciones: apuntar al "right altitude", ni lógica rígida ni vaguedad que asume contexto compartido, y dar "the minimal set of information that fully outlines your expected behavior" https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Tomašev: la delegación es "contingent upon the outcome having precise verification" (contract-first decomposition, sec. 4.1) y los contratos deben ser bidireccionales (sec. 4.2) https://arxiv.org/html/2602.11865
- Intención del comandante: ADP 6-0 (versión 2019) lista siete principios, entre ellos intención clara, órdenes de misión e iniciativa disciplinada [S]. Los elementos (tarea, propósito, factores críticos, estado final) provienen de un artículo de un general, no de la definición doctrinal; leer el glosario de ADP 6-0 antes de citar la definición oficial. El estudio DTIC dice, en síntesis, que actuar dentro de la intención no suele dar problemas y alterarla sí [S].
- La lista "intención, límites, criterio de terminado, presupuesto" no es de una fuente única: es composición de intención (mission command), criterio de verificación (Tomašev) y condiciones de parada (Anthropic). "Presupuesto" como tope de iteraciones viene de Anthropic. Marcarlo como síntesis.

### Recurso canónico
"Building effective agents", solo la sección de cuándo usar agentes y checkpoints (lo técnico es tema IA); Tomašev sec. 4.1 y 4.8 para el criterio de terminado verificable.

### Huecos
- Guías de especificación de tareas de otros laboratorios (p. ej. OpenAI, "A practical guide to building agents"): no consultadas.
- Auftragstaktik en fuente histórica primaria: no consultada.
- Evidencia de que un encargo mejor especificado rinde más: no hallada.

---

## 3. niveles-de-autonomia

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Feng, McDonald, Zhang, "Levels of Autonomy for AI Agents", arXiv 2506.12469 (14-jun-2025, rev. 28-jul-2025; sin revisión por pares confirmada) | primaria, MC | 2/3/2/3 | [M] + [S] del HTML | https://arxiv.org/abs/2506.12469 |
| Parasuraman, Sheridan, Wickens (2000), IEEE Trans. SMC-A 30(3):286-297, DOI 10.1109/3468.844354 | primaria, MC (factores humanos) | 3/3/2/3 | [S] (sin acceso al texto) | https://dblp.uni-trier.de/rec/journals/tsmc/ParasuramanSW00.html |
| Parasuraman y Manzey (2010), Human Factors 52(3):381-410 | primaria, revisión de estudios empíricos | 3/3/2/3 | [M] | https://pubmed.ncbi.nlm.nih.gov/21077562/ |
| Mitchell et al., arXiv 2502.02649 | MC/posición | 2/2/1/2 | [M] | https://arxiv.org/abs/2502.02649 |
| Anthropic, "Measuring AI agent autonomy in practice" (18-feb-2026) | datos de uso de un laboratorio (observacional, solo modelos de Anthropic) | 2/2/2/3 | [S] | https://www.anthropic.com/research/measuring-agent-autonomy |

### Afirmaciones

- Feng et al. definen cinco niveles según el rol de la persona: Operator, Collaborator, Consultant, Approver ("only required to interact with the agent when the agent encounters a blocker") y Observer ("does not require, and comes with no means for, user involvement"). El nivel es decisión de diseño separada de la capacidad: "autonomy as a property that can also be designed independently of capability". Proponen "autonomy certificates" que fijan el nivel máximo https://arxiv.org/html/2506.12469
- Parasuraman, Sheridan y Wickens: cuatro etapas automatizables (adquisición de información, análisis, selección de decisión, implementación de acción), cada una con su grado; el criterio primario son las consecuencias en el desempeño humano. Refina la escala de diez niveles de Sheridan y Verplank (1978, no consultada) [S] https://dblp.uni-trier.de/rec/journals/tsmc/ParasuramanSW00.html
- Parasuraman y Manzey: complacencia y sesgo de automatización aparecen en novatos y expertos, la práctica sola no los elimina, el sesgo produce errores de omisión y de comisión y afecta también a equipos [M] https://pubmed.ncbi.nlm.nih.gov/21077562/
- Anthropic (datos Claude Code, 2025-26): usuarios nuevos (<50 sesiones) usan aprobación automática total ~20 % de las veces; hacia 750 sesiones, más de 40 %. Los nuevos interrumpen ~5 % de los turnos y los experimentados ~9 %. Cita: "effective oversight doesn't require approving every action but being in a position to intervene when it matters." Limitaciones: solo modelos de Anthropic, casi todo ingeniería de software, puntajes de riesgo generados por Claude https://www.anthropic.com/research/measuring-agent-autonomy
- Gestión por excepción: no se consultó fuente del concepto. Approver/Observer de Feng y la cita de Anthropic son su equivalente aplicado. Hueco.
- Mitchell et al.: tesis normativa (no desarrollar agentes totalmente autónomos); no es evidencia sobre cuánta autonomía conviene en una fábrica concreta.

### Recurso canónico
Feng et al., sección de los cinco niveles; Parasuraman y Manzey para el riesgo de pasar a Approver (la persona deja de mirar). Leer juntos.

### Huecos
- Parasuraman, Sheridan, Wickens 2000 y Sheridan y Verplank 1978 en texto completo.
- "Gestión por excepción": sin fuente.
- Si Feng et al. tuvo revisión por pares: no verificado.

---

## 4. frontera-irregular

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon, Lakhani, HBS Working Paper 24-013 (SSRN 4573321) | primaria, EM (experimento de campo preregistrado) | 3/3/3/3 | [L] parcial: texto extraído del PDF (abstract, resultados y sección Centaur/Cyborg leídos) | https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf |
| Misma investigación en Organization Science, doi 10.1287/orsc.2025.21838 | primaria | 3/-/-/- | no leída; las cifras podrían diferir | https://pubsonline.informs.org/doi/full/10.1287/orsc.2025.21838 |
| Brynjolfsson, Li, Raymond, "Generative AI at Work", QJE 140(2):889-942 (2025); NBER w31161 | primaria, EM (datos de campo, 5.172 agentes de soporte) | 3/3/2/3 | [M]/[S] | https://www.nber.org/papers/w31161 |
| METR, estudio de desarrolladores experimentados (10-jul-2025); arXiv 2507.09089 | primaria, EM (ECA) | 3/3/3/3 | [S] | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ |
| METR, "uplift update" (24-feb-2026) | primaria, EM con sesgo de selección declarado | 3/2/2/3 | [S] | https://metr.org/blog/2026-02-24-uplift-update/ |

### Afirmaciones (Dell'Acqua et al., cifras literales del PDF)

- Diseño: "pre-registered experiment involved 758 consultants comprising about 7% of the individual contributor-level consultants at the company"; tres condiciones al azar: sin IA, GPT-4, GPT-4 con resumen de prompt engineering.
- Dentro de la frontera (18 tareas): "completed 12.2% more tasks on average, and completed tasks 25.1% more quickly", y calidad "more than 40% higher quality compared to a control group".
- Quienes estaban por debajo del umbral medio mejoraron 43 %, los de arriba 17 %.
- Fuera de la frontera: "consultants using AI were 19 percentage points less likely to produce correct solutions". En el cuerpo: el control acertó ~84,5 % y las condiciones con IA 60 % y 70 %.
- Centauros: "dividing and delegating their solution-creation activities to the AI or to themselves". Cyborgs: "completely integrating their task flow with the AI and continually interacting with the technology". Todo en https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
- Discrepancia: una página de Harvard resume "about 32 %" de mejora en calidad y VentureBeat dice 40 % [S]; el working paper dice "more than 40 %": usar el paper. Límites del estudio: una empresa, tareas de consultoría, GPT-4 de 2023, una sola tarea fuera de la frontera.
- Brynjolfsson et al.: el abstract de QJE reporta 5.172 agentes; los menos experimentados ganan en velocidad y calidad, los más experimentados ganan poco en velocidad y pierden algo de calidad. Las cifras 14 % promedio y 34 % para novatos son del working paper NBER (2023, que lista 5.179 agentes), no confirmadas en la versión QJE; el preprint de arXiv decía 15 % [S] https://www.nber.org/papers/w31161
- METR (2025): ECA con 16 desarrolladores, 246 issues de ~2 h, repos grandes y conocidos; con IA permitida tardaron 19 % más (IC +2 % a +39 %); esperaban 24 % de aceleración y después creyeron haber ganado ~20 %. Solo software, Cursor con Claude 3.5/3.7 Sonnet https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR actualización, 24-feb-2026: 57 desarrolladores, 143 repos, más de 800 tareas. Los 10 que volvieron: -18 % de tiempo (IC -38 % a +9 %); los 47 nuevos: -4 % (IC -15 % a +9 %); el signo negativo es más rápido con IA. METR lo llama "an unreliable signal" por sesgo de selección (quienes no quieren trabajar sin IA no participan; retienen tareas). Dice que probablemente hoy hay más aceleración que en 2025, con evidencia "muy débil" https://metr.org/blog/2026-02-24-uplift-update/
- Discrepancia sin resolver: la búsqueda indicó que METR declaró "desactualizado" el resultado de 2025; la lectura de la página de actualización no lo dice literal.

### Recurso canónico
Dell'Acqua et al.: abstract, resultados de la tarea fuera de la frontera y la sección Centaur/Cyborg. Fijarse en que con IA el desempeño empeoró justo donde la persona no sabía que estaba fuera de la frontera.

### Huecos
- Versión de Organization Science: contrastar cifras.
- Experimentos de frontera en otros dominios (derecho, ingeniería, ciencia): no buscados.
- Cómo se desplaza la frontera con modelos nuevos: solo parcial (sección 7).

---

## 5. patrones-de-trabajo

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Anthropic, "Building effective agents" | PR de laboratorio | 2/2/2/2 | [S] | https://www.anthropic.com/research/building-effective-agents |
| Anthropic, "How we built our multi-agent research system" (13-jun-2025) | PR de laboratorio, con evaluación interna | 2/3/2/3 | [S] | https://www.anthropic.com/engineering/multi-agent-research-system |
| Feng et al. (persona en el bucle como nivel) | MC | 2/3/2/3 | [M] | https://arxiv.org/abs/2506.12469 |

### Afirmaciones

- Patrones: orquestador-trabajadores ("a central model splits up work on the fly, assigns pieces to worker models" en la paráfrasis), evaluador-optimizador (un modelo genera y otro critica en bucle), paralelización, encadenamiento, enrutamiento https://www.anthropic.com/research/building-effective-agents
- Sistema multiagente (Claude Opus 4 líder, Sonnet 4 subagentes): "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval"; "agents typically use about 4× more tokens than chat interactions" y los multiagente ~15× más que el chat; en BrowseComp tres factores explicaron 95 % de la varianza y el uso de tokens solo ~80 % https://www.anthropic.com/engineering/multi-agent-research-system
- Salvedades del propio post: solo conviene si el valor de la tarea justifica el costo; mal ajuste donde todos los agentes necesitan el mismo contexto o hay muchas dependencias; la mayoría de las tareas de código tienen menos partes paralelizables que la investigación. Evaluación interna del laboratorio que vende el modelo.
- Lectura como organización del trabajo (síntesis nuestra, no de la fuente): orquestador = jefe de equipo que descompone y sintetiza; evaluador-optimizador = hacer y revisar (maker-checker); persona "en el bucle" = aprueba antes de seguir, "en el borde" = vigila y puede intervenir (cerca de Approver/Observer de Feng).
- Ninguna fuente compara el patrón contra una organización humana equivalente.

### Recurso canónico
Post del sistema multiagente: arquitectura, costo en tokens y cuándo no sirve; "Building effective agents" solo por el catálogo.

### Huecos
- Estudios independientes de patrones multiagente en trabajo real: no hallados. Fallas multiagente: tema IA, no consultado.
- Persona en el bucle vs en el borde como literatura propia: sin fuente.

---

## 6. la-atencion-humana-como-restriccion

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Goldratt, *The Goal* (1984): cinco pasos de enfoque | primaria, MC/novela | 3/-/2/3 | [S] (libro no consultado; la redacción de los pasos varía entre fuentes) | https://www.ebsco.com/research-starters/business-and-management/theory-constraints-toc |
| Leroy (2009), OBHDP 109(2):168-181 | primaria, EM (dos experimentos) | 3/3/2/3 | [S] | https://econpapers.repec.org/RePEc:eee:jobhdp:v:109:y:2009:i:2:p:168-181 |
| Mark, Gudith, Klocke (2008), CHI '08, pp. 107-110 | primaria, EM de laboratorio | 3/2/2/3 | [S] | https://www.ics.uci.edu/~gmark/chi08-mark.pdf |
| Parasuraman y Manzey (2010) | EM (revisión) | 3/3/2/3 | [M] | https://pubmed.ncbi.nlm.nih.gov/21077562/ |
| Faros AI, "AI Productivity Paradox Report 2025" | telemetría de vendor | 1/2/2/2 | [S] | https://www.faros.ai/blog/ai-productivity-paradox-report-2025 |
| DORA 2025, "State of AI-assisted Software Development" | encuesta (~5.000 profesionales) | 2/2/1/2 | [S] (el PDF no se pudo leer) | https://dora.dev/dora-report-2025/ |
| AIDev (932.791 PRs de agentes) y estudios derivados | EM observacional (arXiv, sin revisión confirmada) | 2/2/2/2 | [S] | https://arxiv.org/html/2602.09185v1 ; https://arxiv.org/html/2601.00753v2 |
| Revisiones de alert fatigue (clínica), JMIR Med Inform 2020 y revisión de 2026 | EM (revisiones) | 2/2/1/1 | [S] | https://medinform.jmir.org/2020/7/e15653/ |

### Afirmaciones

- Teoría de Restricciones: identificar la restricción, explotarla, subordinar el resto, elevarla y repetir. Confirmar la redacción contra el libro antes de citar literal https://www.ebsco.com/research-starters/business-and-management/theory-constraints-toc
- Aplicación a la revisión humana (síntesis nuestra, lente de flujo): si los agentes producen más rápido de lo que una persona revisa, el rendimiento lo fija la revisión; explotar = no gastar su atención en lo que ya se verificó solo; subordinar = no producir más de lo que se puede revisar; elevar = recién después. No hallé una fuente que aplique TOC a la revisión de agentes.
- Leroy: la gente tiene dificultad para dejar una tarea inconclusa y su desempeño en la siguiente baja ("attention residue", dos experimentos); la presión de tiempo en la primera tarea ayudó a desengancharse [S] https://econpapers.repec.org/RePEc:eee:jobhdp:v:109:y:2009:i:2:p:168-181
- Mark et al.: los interrumpidos terminaron más rápido con calidad similar, pero con más estrés, frustración, esfuerzo y presión; laboratorio, tamaño de muestra no extraído [S] https://www.ics.uci.edu/~gmark/chi08-mark.pdf. El costo medido es en carga, no en tiempo.
- Faros (2025, 10.000+ desarrolladores, 1.255 equipos): con alta adopción de IA, 21 % más tareas y 98 % más PRs integrados, pero el tiempo de revisión subió 91 % y el tamaño medio del PR 154 %; las métricas DORA de organización no mejoraron [S]. Vendor, sin revisión por pares; algunas fuentes atribuyen las cifras al informe 2026, sin confirmar https://www.faros.ai/blog/ai-productivity-paradox-report-2025
- DORA 2025: adopción de IA 90 % (+14 % respecto del año previo), ~65 % depende mucho de IA; el vínculo con throughput es positivo pero aumenta la inestabilidad; ~30 % confía poco o nada en el código generado [S] https://blog.google/technology/developers/dora-report-2025/. No se obtuvieron cifras propias de tiempo de revisión.
- Estudios de PRs de agentes (AIDev, corte 1-ago-2025): tasa de aceptación entre 0,45 (Copilot) y 0,83 (Codex) en un subconjunto https://arxiv.org/pdf/2602.02345 ; 3,8 % de "ghosting" (sin respuesta humana tras más de 14 días) en 33.707 PRs, y un presupuesto de revisión del 20 % captura 69 % de los PRs de alto esfuerzo https://arxiv.org/html/2601.00753v2 ; los subconjuntos difieren, las cifras no son comparables.
- Fatiga de alertas: tasas medias de anulación de 46,2 % a 96,2 % (revisión de 23 artículos, 2020) https://medinform.jmir.org/2020/7/e15653/ ; una revisión de 2026 halló que casi ningún estudio define alert fatigue de modo operativo. Es analogía clínica, no estudio de revisión de agentes.
- Un estudio que junte TOC, cambio de contexto y revisión de agentes: no lo hallé. Las piezas existen por separado; la síntesis es nuestra.

### Recurso canónico
Goldratt, *The Goal* (los cinco pasos) leído junto con Faros/AIDev como caso; Leroy 2009 para el costo del cambio de tarea.

### Huecos
- Goldratt en texto original; Reinertsen (flujo, colas) sin consultar; literatura de vigilancia (Mackworth) sin consultar.
- DORA 2025 en texto completo.
- Carga de revisión fuera de software: sin evidencia.

---

## 7. horizonte-de-tareas (ficha, volátil)

Fecha de esta ficha: 2026-11-27. Las cifras envejecen en meses.

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|
| Kwa et al., "Measuring AI Ability to Complete Long Software Tasks", arXiv 2503.14499 (v1 18-mar-2025; v4 10-jul-2026; el título cambió, antes "Long Tasks") | primaria, EM de benchmark (sin revisión por pares confirmada) | 3/3/2/3 | [M] | https://arxiv.org/abs/2503.14499 |
| METR, Time Horizon 1.1 (29-ene-2026) | primaria | 3/3/2/3 | [S] | https://metr.org/blog/2026-1-29-time-horizon-1-1/ |
| METR, página de horizontes (última actualización 8-sep-2026; "no longer actively updated") | primaria | 3/1/1/3 | [S] | https://metr.org/time-horizons/ |
| METR, "How Does Time Horizon Vary Across Domains?" (14-jul-2025) | primaria | 3/3/2/3 | [S] | https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains |
| Prensa sobre Claude Mythos Preview (The Decoder, otras) | secundaria | 1/1/1/1 | [S] | https://the-decoder.com/metr-says-it-can-barely-measure-claude-mythos-palo-alto-networks-warns-of-autonomous-ai-attackers/ |

### Valores

- Original (Kwa et al.): horizonte al 50 % de Claude 3.7 Sonnet ≈ 50 minutos; duplicación cada ~7 meses desde 2019, quizá acelerada en 2024 https://arxiv.org/abs/2503.14499
- TH 1.1 (29-ene-2026): 228 tareas (de 170), 31 de 8 horas o más, solo 5 de esas con línea base humana. Mayor horizonte al 50 % en esa fecha: Claude Opus 4.5, 320 minutos, IC [170, 729]. Duplicación desde 2023: 130,8 días [107, 161]; desde 2024: 88,6 días. METR: "These confidence intervals are still very wide." https://metr.org/blog/2026-1-29-time-horizon-1-1/
- Modelos agregados después al tracker de METR: Claude Opus 4.6 y GPT-5.3-Codex (20-feb-2026), GPT-5.4 (10-abr-2026), Gemini 3.1 Pro (15-abr-2026), Claude Mythos Preview temprano (8-may-2026) https://metr.org/time-horizons/. No obtuve sus valores porque el archivo de datos no estaba accesible.
- Claude Mythos Preview: según la prensa, METR estimó un horizonte al 50 % de "at least 16 hours" con IC 95 % de 8,5 a 55 horas, evaluado en marzo de 2026, y advierte que por encima de 16 horas la suite actual no es fiable [S, no verificado contra METR]. Una lectura de terceros del archivo de datos da 1.044,8 min (~17,4 h) al 50 % y ~3,1 h al 80 %. Estimaciones de 34 a más de 40 horas circulan en LessWrong como imputaciones no oficiales. Las cifras no coinciden; tratar como "más de 16 horas, con incertidumbre grande".
- Por dominio (METR, 14-jul-2025): 9 benchmarks; en ninguno el progreso es claramente sub-exponencial. Software y razonamiento (GPQA, MATH, METR-HRS, LiveCodeBench): horizontes de 50 a 200+ minutos; uso agéntico de computadora (OSWorld, WebArena): ~40-100 veces más corto; conducción autónoma ~0,6 duplicaciones por año; en video la métrica no aplica. METR admite que trabajo valioso como gestión o enfermería casi no está representado y que los benchmarks probablemente sobre-representan dominios de avance rápido https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains
- Para la fábrica: el horizonte es el tiempo humano de las tareas que el modelo completa con 50 % de éxito, no cuánto trabaja solo con fiabilidad. Para encargos fiables importa el horizonte al 80 %, bastante menor (inferencia de la definición).

### Recurso canónico
Página de METR del TH 1.1, sección de caveats; el artículo original solo para la definición.

### Huecos
- Valores actuales al 50 % y 80 % de los modelos de 2026 (archivo de datos de METR no accedido).
- Horizontes en dominios no software con tareas largas reales: casi no hay.
- Verificar la nota de METR sobre Mythos directamente.

---

## Contradicciones y cautelas generales

- METR 2025 (19 % más lentos) vs METR 2026 (aceleración estimada, con sesgo de selección): las dos son de METR; la segunda se declara poco confiable. Citar ambas con fecha.
- Dell'Acqua: 40 % de calidad (paper) vs 32 % (resumen de Harvard): usar el paper.
- Brynjolfsson: 14 % (NBER), 15 % (arXiv), cifras de QJE sin confirmar.
- Mythos: de 16 h a más de 40 h según la fuente.
- Marketing/encuesta gremial: PMI publica encuestas de profesionales sobre IA (2023: solo 18 % con experiencia práctica amplia; 2025 Global AI in Project Management Survey, 870 profesionales en 97 países) [S]; son encuestas sin método causal, no usar como evidencia de efecto https://www.pmi.org/about/press-media/press-releases/demand-increases-for-project-professionals-with-ai-skills

## Huecos de la vertical en conjunto

1. Marcos de responsabilidad de IA (NIST, ISO 42001, EU AI Act) no consultados.
2. Textos originales de Goldratt, Sheridan y Verplank, Parasuraman et al. 2000 y Auftragstaktik: sin acceso.
3. Evidencia de RACI: inexistente en lo hallado.
4. Evidencia independiente de patrones multiagente y de carga de revisión fuera del software: casi nula; las cifras de revisión son de vendors y estudios observacionales de GitHub.
5. Fuera de software, atención al cliente y consultoría casi no hay experimentos con agentes; la extrapolación a "cualquier dominio" es inferencia.
6. Gestión por excepción: sin fuente primaria.
7. Casi todas las lecturas de páginas web fueron resúmenes de WebFetch [S]; antes de citar literal, abrir la fuente.
