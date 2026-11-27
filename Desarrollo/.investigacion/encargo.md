# Investigación: Desarrollo / Encargo (el ciclo con el cliente en un proyecto a medida)

Fecha: 2026-11-27. Ángulo: la vertical `Encargo/` de `Desarrollo/ALCANCE.md`, con agentes de código como parte normal del oficio.

Marcas: [L] leí el texto completo o el pasaje que cito (páginas por extractor de WebFetch, PDF con pdftotext: tratar los literales de páginas web como fragmentos); [M] metadatos o abstract; [S] resumen secundario o del buscador. Puntajes 1 a 3: A autoridad, P profundidad, E ejemplos, U unicidad. Tipo: P primaria, S secundaria.

Tope de rondas: hubo tres rondas de búsqueda en total para toda la vertical, repartidas entre componentes; varios componentes quedaron con una sola ronda y eso se declara en Huecos.

## Qué ya hay en `conocimiento-desarrollo` y qué falta

Leí `Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md` y su informe `Producto/.investigacion/proyecto-a-precio-cerrado.md`. Ahí ya está, con fuentes y URL, y no hay que repetir (alcanza con enlazar):

- Sobrecostos y su cola: Moløkken y Jørgensen (60-80 % con sobrecosto, 30-40 % promedio), Flyvbjerg y Budzier (1471 proyectos, 27 %, uno de cada seis con 200 %; muestra de proyectos enormes), la crítica de CHAOS (Eveleens y Verhoef 2010: 5457 pronósticos de 1211 proyectos).
- Jørgensen: estimar de arriba hacia abajo y de abajo hacia arriba por separado, justificar, combinar, dar intervalo; no mezclar oferta con estimación; el optimismo del ganador (35 proveedores, 130-174 % de sobrecosto en los elegidos por precio).
- Cono de incertidumbre (McConnell 2010) con su crítica (Bossavit, Little 2006); descubrimiento pago de alrededor del 10 % (Boag 2024); reserva de contingencia vs de gestión (solo [S]).
- Control de cambios por escrito contra una línea base (PMBOK 6 vía resúmenes), art. 1264 del Código Civil y Comercial, intercambio a igual esfuerzo (Primer), Fowler "Fixed Scope Mirage".
- Aceptación formal (Validate Scope), garantía atada a la aceptación incremental (Primer), Money for Nothing / Change for Free (Sutherland 2008; Kelly 2014 lo evalúa), Fink y otros (270 contratos de un banco), hitos y adelantos de agencias.
- Sus huecos declarados, que acá siguen abiertos salvo donde digo lo contrario: porcentaje medido de contingencia para software chico, McConnell 2006 sin leer, PMBOK sin abrir, acta de entrega, aceptación por correo o silencio en Argentina, Opelt y otros 2013 sin texto.

Lo que falta y este informe agrega: (1) todo lo de antes del contrato (kickoff, inception, charter, discovery) y lo de después (traspaso, soporte); (2) el plan de entregas (walking skeleton, slicing vertical, release planning); (3) seguimiento con el cliente (demos, evidencia, riesgos); (4) estimación sin números por punto: previsión probabilística, apetito de Shape Up, #NoEstimates, reference class forecasting; (5) qué cambia estimar y cobrar cuando el código lo escribe un agente. El caso del proyecto a precio cerrado está escrito desde la tienda online de una pyme; lo de acá es el ciclo general.

## Hallazgo sobre el árbol

1. **`estimacion` carga dos temas distintos.** Estimar (técnicas, incertidumbre, previsión) y contratar/cobrar (modelos de contrato, quién carga el riesgo, cobro por horas o por valor) los junta el ALCANCE.md en una sola nota. La literatura los separa: Jørgensen, McConnell, Vacanti hablan de estimar; Larman/Vodde, Sutherland, Fink y Brynjolfsson/Petropoulos hablan de contratos y precios. Propuesta: `estimacion` (cómo se sabe cuánto lleva y cuánta incertidumbre hay) y `modelos-de-contrato-y-cobro` (precio cerrado, tiempo y materiales, alcance variable, por resultado, abono, y el efecto de los agentes). La nota existente `proyecto-a-precio-cerrado` de Producto queda como el caso profundo del precio cerrado, y la nota nueva la enlaza. El precio de lista y la propuesta son de Ventas.
2. **`alcance-y-aceptacion` y `cambios-de-alcance` son una cadena** (línea base, cambio contra la línea base, aceptación), igual que el PMBOK 6 la ubica en un solo capítulo (según resúmenes). Dejar dos notas es razonable porque la pregunta del lector es distinta ("qué entra" vs "me piden otra cosa"), pero conviene que se enlacen en los dos sentidos, y que `criterios-de-aceptacion` de `Definicion/` sea el puente técnico.
3. **`acuerdo-inicial` toca `Definicion/especificacion` en el medio.** Corte propuesto: `acuerdo-inicial` termina en un acuerdo entre personas (problema, resultado buscado, qué es éxito, quién decide, restricciones); `especificacion` empieza ahí y es insumo del agente. El charter o MVP canvas es lo último de uno y el primero del otro.
4. **`seguimiento-con-el-cliente` y `plan-de-entregas`** comparten el incremento usable. Sugiero que el plan hable de qué se corta y en qué orden, y el seguimiento de cómo se muestra y se mide el avance.
5. **`traspaso` tiene dos tiempos** que las fuentes mezclan: el cierre del proyecto (entregar el código, los accesos y la documentación) y lo que sigue (garantía, soporte, mantenimiento). Conviene una sección por cada uno, y el segundo se enlaza con `Evolucion/` y con el abono de cuidado de Emprender.
6. **Falta una nota que no está en el árbol**: la **gestión de riesgos del encargo** (qué riesgos se miran con el cliente y cuándo). Hoy las fuentes la reparten entre seguimiento, estimación y cambios. Propongo que quede dentro de `seguimiento-con-el-cliente` salvo que crezca.

## Hallazgo transversal sobre agentes

La evidencia sobre qué hace un agente con el esfuerzo de un proyecto es todavía débil y cambia rápido. Lo medido hasta ahora: un ensayo controlado de 2025 (METR) donde permitir IA a desarrolladores experimentados aumentó el tiempo de tarea un 19 %, y su seguimiento de 2026 con resultado poco claro y un sesgo de selección declarado; DORA 2025 que dice que la IA mejora el rendimiento de entrega pero que lo amplifica todo, también lo malo; y preprints que muestran que los modelos de lenguaje estiman puntos de historia con resultados dispares. Lo robusto para el encargo es indirecto: el costo de escribir el código baja, y el costo de definir, verificar, integrar, desplegar y conversar con el cliente no. La implicancia para el cobro la desarrolla el working paper de Brynjolfsson y Petropoulos (2026), y el consenso de analistas es que el cobro por resultado sigue siendo minoritario.

---

## 1. acuerdo-inicial

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Martin Fowler / Paulo Caroli, "Lean Inception" | https://www.martinfowler.com/articles/lean-inception | P (autor del método, en el sitio de Fowler) | 2 | 2 | 2 | 2 | [L] |
| Caroli, *Lean Inception: How to Align People and Build the Right Product* | https://leanpub.com/leaninception (no abrí) | P (libro) | 3 | 3 | 3 | 3 | [S] solo índice vía buscador, copias de Scribd no consultadas |
| Miro, plantilla de Lean Inception (agenda por día) | https://miro.com/miroverse/lean-inception-workshop/ | S | 1 | 1 | 1 | 1 | [S] |
| Basecamp, *Shape Up*, cap. 2 "Principles of Shaping" y glosario | https://basecamp.com/shapeup/1.1-chapter-02 | P | 3 | 3 | 3 | 3 | [L] |
| Boag, "Pricing Projects As A Freelancer Or Agency Owner" (descubrimiento pago, 10 %) | https://smashingmagazine.com/2024/08/pricing-projects-freelancer-agency-owner/ | P (practicante) | 1 | 1 | 1 | 2 | [L] (en el informe de Producto) |
| PMI, *PMBOK Guide* 7ª ed. (project charter como artefacto del enfoque) | https://www.pmi.org/pmbok-guide-standards/foundational/PMBOK | P (ficha) | 3 | 1 | 1 | 2 | [S] |
| Standish Group / Eveleens y Verhoef (el CHAOS como contexto de por qué se hace descubrimiento) | https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/ | P (crítica) | 3 | 2 | 2 | 3 | [L] abstract |

### Afirmaciones

- Lean Inception: «The lean inception is a focused form of inception, which can be done in a single week.» «consists of a series of activities, typically scheduled over the course of a week.» El lunes define la visión del producto y el «Is – Is not – Does – Does not»; martes personas y funciones; miércoles revisión técnica, de experiencia de usuario y de negocio, y recorridos de usuario; jueves funciones en recorridos y secuenciación; viernes el MVP canvas y una muestra a los interesados. El resultado es «the understanding the MVP». Sirve «when the team needs to iteratively develop an MVP» y las grandes lo usan «to start quickly». https://www.martinfowler.com/articles/lean-inception
- Origen: el buscador, citando el sitio de Fowler y Miro, da a Caroli como autor y dice que busca reducir las inceptions «tradicionales» de dos a cuatro semanas a una [S]. El libro no lo leí. https://www.martinfowler.com/articles/lean-inception
- Shape Up describe el trabajo moldeado como «rough», «solved» y «bounded»: «It tells the team where to stop». El pitch «summarizes the problem, constraints, solution, rabbit holes, and limitations». Es un acuerdo inicial de otro tipo: el equipo no recibe una lista de requisitos sino un problema acotado con un apetito (tiempo que se está dispuesto a gastar). https://basecamp.com/shapeup/1.1-chapter-02
- Descubrimiento pago antes de cotizar la construcción: Boag propone ~10 % del presupuesto, luego prototipo, y lo que aparece entra en la cotización de la fase siguiente (ya en la nota de Producto). https://smashingmagazine.com/2024/08/pricing-projects-freelancer-agency-owner/
- Qué es un project charter: de la ficha del PMBOK solo confirmé que el 7 tiene principios y dominios y una sección de adaptación del enfoque; no pude abrir qué dice del charter. Lo que sé del charter (documento corto que autoriza el proyecto, nombra al responsable y fija objetivos y restricciones) es de la práctica general y no lo pude citar. https://www.pmi.org/pmbok-guide-standards/foundational/PMBOK [S]
- Kickoff: no encontré en esta ronda una fuente primaria de calidad sobre la reunión de arranque con el cliente. Hueco.

### Qué cambia con agentes

- El acuerdo inicial es donde más pesa el cuello de botella nuevo: el agente construye rápido lo que se le dice, así que si el problema o el resultado están mal entendidos, se entrega rápido lo equivocado. Es inferencia de esta base apoyada en la tesis de DORA 2025 de que la IA amplifica lo que ya hay en la organización, buenas o malas prácticas: https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/ [S].
- Un prototipo funcionando cuesta hoy mucho menos que antes; eso empuja a reemplazar parte del discovery por prototipos para que el cliente reaccione a algo andando. No encontré una fuente que lo mida; es práctica emergente, a marcar como tal.
- Pierde peso: la inception de semanas con talleres largos como paso obligatorio, y el documento de requisitos gigante como entregable del arranque. Lean Inception de una semana ya es el formato condensado; para un encargo chico puede alcanzar con una o dos sesiones.

### Recurso canónico

El artículo de Fowler sobre Lean Inception (corto, con la agenda por día) para el formato, y *Shape Up* cap. 2 (rough, solved, bounded) para entender qué es un problema acotado. En qué fijarse: el «Is – Is not – Does – Does not» (qué es y qué no es el producto) y que lo que sale del acuerdo sea una decisión sobre qué entra en la primera versión, no una lista de deseos.

---

## 2. alcance-y-aceptacion

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Arbogast, Larman y Vodde, *Agile Contracts Primer* v5 (2012): Acceptance, Warranty, Deliverables | http://www.agilecontracts.org/agile_contracts_primer.pdf | P | 2 | 3 | 2 | 3 | [L] secciones (PDF bajado y pasado por pdftotext) |
| *Scrum Guide* (2020), Increment, Definition of Done | https://scrumguides.org/scrum-guide.html | P | 3 | 2 | 1 | 2 | [L] pasajes |
| ISTQB Glossary (acceptance testing; acceptance criteria) | https://api.glossary.istqb.org/storage/help/R0uz58NqLzUz48LVUuyGSF76NFj4LHQazSs0GlNS.pdf | P (glosario) | 3 | 1 | 1 | 2 | [S] vía buscador |
| PMBOK 6 cap. 5, Validate Scope y Control Scope | https://www.projectmanagement.com/blog-post/58284/project-scope-management-part-6--control-scope | S | 1 | 1 | 1 | 1 | [S] (en la nota de Producto) |
| Adzic, *Specification by Example* (2011), para criterios como ejemplos | no abierto | P (libro) | 3 | 3 | 3 | 3 | [S] solo citado en ALCANCE.md |

### Afirmaciones

- Qué es «terminado»: el *Scrum Guide* dice «The Definition of Done is a formal description of the state of the Increment» y «In order to provide value, the Increment must be usable.» https://scrumguides.org/scrum-guide.html
- Aceptación en contrato: el Primer pregunta «Is it done?» y «What to do if not done?», y en entrega iterativa la aceptación final es la suma de aceptaciones por iteración, basadas en «conformance to a prior agreed-on acceptance-test» (frase en el texto, línea ~1069 de la extracción). Recomienda no fijar en el contrato una lista detallada de entregables: «Avoid such specificity and rigidity—avoid including a detailed deliverables list in the contract», y da el motivo (se pasa a producir documentos en vez de software andando). Con una salvedad que cita: «we have seen custom software for which the source code was never provided by the supplier—somebody forgot». http://www.agilecontracts.org/agile_contracts_primer.pdf
- Documentación técnica: el Primer dice que su entrega se especifica a menudo en contratos tradicionales, pero «could be wasteful to require it as an early deliverable»; si el cliente toma el mantenimiento, puede crearse al final, «perhaps in a joint agile-documentation workshop». http://www.agilecontracts.org/agile_contracts_primer.pdf
- Garantía: con aceptación incremental el riesgo de la garantía final es menor, «especially enhanced if automated acceptance testing is employed», y la garantía se ata a cada entregable. http://www.agilecontracts.org/agile_contracts_primer.pdf
- Acceptance criteria según ISTQB (ref. a ISO 24765): «The criteria that a component or system must satisfy in order to be accepted by a user, customer, or other authorized entity.» «Acceptance testing: A test level that focuses on determining whether to accept the system.» No hay entrada separada de UAT en el glosario; las fuentes secundarias la tratan como una forma de aceptación (usuarios) junto a la operativa y la contractual. [S] https://api.glossary.istqb.org/storage/help/R0uz58NqLzUz48LVUuyGSF76NFj4LHQazSs0GlNS.pdf
- Línea base de alcance y separación entre validar y controlar calidad: ya en la nota de Producto ([S], PMBOK 6 por resúmenes).
- Qué entra y qué no en un acuerdo de alcance como práctica (una lista de «fuera de alcance» explícita): lo recomiendan blogs de agencia (en el informe de Producto); no encontré un estudio. Lean Inception lo cubre con el «Is not / Does not».

### Qué cambia con agentes

- Los criterios de aceptación escritos como ejemplos verificables son lo que un agente usa para saber cuándo terminó y lo que una persona usa para no leer cada línea. Eso los vuelve más valiosos que antes; se desarrolla en `Definicion/criterios-de-aceptacion`. La idea de que las pruebas automatizadas refuerzan la aceptación ya está en el Primer (cita arriba).
- Lo que sigue siendo de personas: que el cliente confirme que el criterio expresa lo que quiere. El agente verifica contra el criterio escrito, no contra la intención.
- Pierde peso: el UAT como una fase única al final con planillas de casos manuales; la aceptación incremental con demos y criterios automatizados la reemplaza. No encontré una fuente que mida ese cambio; es la lectura de esta base a partir del Primer.

### Recurso canónico

*Agile Contracts Primer*, secciones Acceptance, Warranty y Deliverables (libre, unas pocas páginas por tema). En qué fijarse: que la aceptación sea de conformidad con pruebas acordadas antes, que el contrato no fije una lista de documentos, y que el código fuente y los accesos figuren como entregables explícitos (el ejemplo del Primer de lo que alguien olvidó).

---

## 3. estimacion

### Fuentes: estimar

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Jørgensen (2004), A Review of Studies on Expert Estimation of Software Development Effort | https://cms.simula.no/sites/default/files/publications/SE.4.Joergensen.2004.c.pdf | P (revisión) | 3 | 3 | 2 | 3 | [L] en el informe de Producto (abstract y sobreoptimismo) |
| McConnell (2010), Software Development's Cone of Uncertainty | https://www.construx.com/wp-content/uploads/2019/02/CxWhitePaper_ConeOfUncertainty.pdf | P | 2 | 2 | 1 | 2 | [L] en el informe de Producto |
| McConnell, *Software Estimation* (2006) | https://www.oreilly.com/library/view/software-estimation-demystifying/0735605351/ | P (libro) | 3 | 3 | 3 | 3 | [S] no leído |
| Flyvbjerg y Budzier (2011) HBR | https://arxiv.org/abs/1304.0265 | P | 3 | 2 | 3 | 3 | [L] en el informe de Producto |
| Flyvbjerg, "From Nobel Prize to Project Management: Getting Risks Right" (reference class forecasting) | https://arxiv.org/pdf/1302.3642 | P | 3 | 2 | 2 | 3 | [M] solo vía buscador |
| Informe del Edinburgh Tram Inquiry (Flyvbjerg), pasos del RCF | https://arxiv.org/pdf/1805.12106 | P | 2 | 2 | 2 | 2 | [S] |
| Basecamp, *Shape Up*, cap. 3 "Set Boundaries" | https://basecamp.com/shapeup/1.2-chapter-03 | P | 3 | 3 | 3 | 3 | [L] |
| Fowler, "The Purpose of Estimation" | https://martinfowler.com/bliki/PurposeOfEstimation.html | P (practicante marcado) | 2 | 1 | 1 | 2 | [L] |
| Duarte, *NoEstimates* (libro), vía entrevista de InfoQ | https://www.infoq.com/articles/book-review-noestimates | P (autor) / entrevista promocional | 1 | 1 | 1 | 2 | [L] |
| Ron Jeffries, "The #NoEstimates Movement" | https://ronjeffries.com/xprog/articles/the-noestimates-movement/ | S (crítico moderado) | 2 | 2 | 1 | 2 | [S] solo en resultados |
| Vacanti, *Actionable Agile Metrics* / *When Will It Be Done?* | https://actionableagile.com (no abierto) | P (libro) | 2 | 3 | 2 | 3 | [S] solo vía buscador, ninguna fuente primaria leída |
| Reaktor, Expedia, etc. sobre Monte Carlo en entrega | https://www.reaktor.com/insights-and-events/forecasting-method ; https://medium.com/expedia-group-tech/monte-carlo-forecasting-in-software-delivery-474bb49cb3f9 | S (blogs de empresas) | 1 | 1 | 2 | 1 | [S] |
| Conferencia 2021 sobre pronóstico Monte Carlo con takt time (MMRE 32 %) | https://core.ac.uk/download/334528317.pdf | P | 2 | 2 | 2 | 3 | [S] solo vía buscador |
| METR (2025) RCT con desarrolladores experimentados | https://arxiv.org/pdf/2507.09089 | P, sin revisión por pares hasta donde vi | 3 | 3 | 3 | 3 | [M] |
| METR (2026-02-24) actualización de uplift | https://metr.org/blog/2026-02-24-uplift-update/ | P (blog de METR) | 3 | 2 | 2 | 3 | [M] |
| METR, "Measuring AI Ability to Complete Long Tasks" | https://arxiv.org/abs/2503.14499 | P, preprint | 3 | 3 | 2 | 3 | [M] |
| Preprints sobre LLM estimando puntos de historia | https://arxiv.org/pdf/2603.06276 ; https://arxiv.org/pdf/2604.03443 ; https://arxiv.org/pdf/2403.08430 | P, preprints | 2 | 2 | 2 | 2 | [S] |

### Afirmaciones: estimar

**Lo que sigue vigente (y está en la nota de Producto).** Rangos, el optimismo ante la propia tarea, no mezclar oferta con estimación, y el cono de incertidumbre con su discusión. No se repite acá.

**Reference class forecasting (previsión por clase de referencia).**
- El método consiste en tomar el «outside view»: «The outside view does not try to forecast the specific uncertain events that will affect the particular project, but instead places the project in a statistical distribution of outcomes from this class of reference projects.» El paso final es un ajuste («uplift») según si el proyecto es más o menos riesgoso que su clase. Vino de Kahneman y Tversky (1979) y lo probó Flyvbjerg en infraestructura de transporte. https://arxiv.org/pdf/1805.12106 [S, vía buscador]
- IT es una clase de referencia reconocida en los datos del Reino Unido, pero no encontré valores de uplift para IT. https://arxiv.org/pdf/1805.12106 [S]. La guía de ajuste por sesgo de optimismo del Green Book (HM Treasury) es donde buscarlos; no la abrí.
- Para un equipo chico, el equivalente práctico es el registro propio de proyectos terminados: un artículo informal propone que equipos chicos «grow proprietary reference classes» cuya capacidad predictiva crece con el tiempo (TechCrunch 2017, informal, no estudio): https://techcrunch.com/2017/01/03/how-to-fix-agile-teams-that-are-notoriously-bad-at-hitting-release-dates/ [S]. Misma conclusión que la nota de Producto («el registro de cuánto llevaron los anteriores vale más que una lista de tareas más fina»).

**Apetito en lugar de estimación (Shape Up).**
- «An appetite is completely different from an estimate.» «Estimates start with a design and end with a number. Appetites start with a number and end with a design.» «This principle, called "fixed time, variable scope," is key to successfully defining and shipping projects.» https://basecamp.com/shapeup/1.2-chapter-03
- Glosario: ciclo de seis semanas; «Circuit breaker: Cancel projects that don't ship in one cycle by default instead of extending them by default»; *scope hammering* («Forcefully questioning a design, implementation, or use case to cut scope and finish inside the fixed time box»); lote grande (un proyecto ocupa un equipo todo el ciclo) o lote chico (varios de 1-2 semanas). https://basecamp.com/shapeup/4.5-appendix-06
- Límite que el libro no resuelve en lo que leí: Shape Up describe un equipo con producto propio y no un proveedor con cliente externo y contrato. Cómo se traduce a un encargo (apetito fijado con el cliente, alcance que se acuerda recortar) es lectura de esta base; ya la insinúa la nota de Producto «Shape Up resuelve el mismo problema al revés, con el tiempo fijo y el alcance variable».

**#NoEstimates.**
- Empezó en Twitter en 2012 (Zuill, 10 dic 2012; Duarte con #EstWaste); Ron Jeffries lo llamó «movimiento» [S]. Zuill recomienda dejar de estimar y entregar lo más importante en unas dos semanas; Duarte, más matizado: empezar y después de unos sprints dar pronósticos. https://ronjeffries.com/xprog/articles/the-noestimates-movement/ [S]
- Propuesta del libro (en entrevista con el autor): decidir por valor, planificar por objetivo y presupuesto («a budget, not an estimate»), contar ítems entregados contra el backlog restante, proyectar el ritmo histórico, y tratar el momento en que lo que queda excede la capacidad como disparador de decisiones («I never assume that scope is fixed, or the backlog is complete»). https://www.infoq.com/articles/book-review-noestimates
- La evidencia que aporta es anecdótica: la misma entrevista cita «accuracy levels near 100%» y un proyecto de 18 meses reducido a menos de dos semanas, sin datos; es promocional y por eso la marca es 1/1/1. https://www.infoq.com/articles/book-review-noestimates
- Postura moderada de práctica: Fowler dice que la estimación vale «when it helps you make a significant decision» (asignar recursos, coordinar, seguir contra un plan) y que equipos sin estimar funcionan cuando cliente y equipo acuerdan que las estimaciones no manejan decisiones importantes y trabajan por prioridad en unidades chicas. https://martinfowler.com/bliki/PurposeOfEstimation.html
- Para un encargo con precio acordado, lo que queda en pie de #NoEstimates es la parte de pronóstico por ritmo (siguiente punto); la parte de «no estimar» choca con que el cliente necesita saber cuánto y cuándo antes de firmar.

**Previsión probabilística (Monte Carlo sobre el rendimiento histórico).**
- Método: tomar el rendimiento histórico (ítems terminados por semana), simular miles de veces y mostrar la distribución de fechas o de ítems por fecha. Responde «cuántos ítems llegan a tal fecha» y «cuándo termino N ítems». Una guía sugiere usar 12 a 16 semanas de datos; otra, más de 10.000 simulaciones. Supone un tablero que se usa con rigor: límite de trabajo en curso, todos los ítems entran y salen, actualización frecuente [S, blogs de empresas]. https://www.reaktor.com/insights-and-events/forecasting-method ; https://medium.com/expedia-group-tech/monte-carlo-forecasting-in-software-delivery-474bb49cb3f9
- Evidencia: una conferencia de 2021 reportó que los pronósticos de fecha con Monte Carlo basados en takt time tuvieron un MMRE (error relativo medio) del 32 % en una serie de 10 corridas y concluyó que pueden usarse en la práctica después de unos pocos sprints iniciales [S, solo abstract vía buscador]. https://core.ac.uk/download/334528317.pdf
- Crítica a PERT (de la nota de Producto): PERT subestima el riesgo donde convergen caminos y se recomienda Monte Carlo (Hulett, PMI, 2000, [S]).
- Lo que no hallé: una fuente primaria de Vacanti (libro o documentación de ActionableAgile) ni un estudio con proyectos a medida chicos. Hueco.

### Fuentes: contratos y cobro

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| *Agile Contracts Primer* v5, Part 3 | http://www.agilecontracts.org/agile_contracts_primer.pdf | P | 2 | 3 | 2 | 3 | [L] |
| Sutherland (2008), Money for Nothing | http://jeffsutherland.com/scrum/2008/10/agile-contracts-money-for-nothing-and.html | P (autor) | 3 | 2 | 2 | 3 | [L] en el informe de Producto |
| Kelly (2014), Agile Contracts: Truth & Options | https://www.allankelly.net/static/presentations/AgileContracts2014.pdf | P (practicante) | 2 | 1 | 2 | 2 | [L] en el informe de Producto |
| Fowler (2004), Fixed Scope Mirage | https://martinfowler.com/bliki/FixedScopeMirage.html | P (practicante) | 2 | 1 | 1 | 2 | [L] |
| Fink, Lichtenstein y Wyss (2013) | https://openaccess.city.ac.uk/id/eprint/18016/ | P | 3 | 3 | 2 | 3 | [L] abstract e intro (en el informe de Producto) |
| Opelt, Gloger, Pfarl y Mittermayr, *Agile Contracts* (Wiley 2013) | https://www.wiley-vch.de/de/fachgebiete/computer-und-informatik/agile-contracts-978-1-118-63094-5 | P (libro) | 3 | 3 | 3 | 3 | [M] solo catálogo |
| Brynjolfsson y Petropoulos, "Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives" (23 ago 2026) | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | P, working paper (no vi indicación de revisión por pares) | 3 | 3 | 2 | 3 | [L] abstract, secciones 1 y partes; no todo |
| Gartner, "services buyers 19 % / seller agreements 13 %" y IDC, vía síntesis del buscador | https://www.gartner.com/en/documents/8201129 ; https://www.idc.com/?p=123073 | P, de pago | 2 | 1 | 1 | 2 | [S] (no abrí los informes) |
| CIO.com, "Your service vendors are being rebuilt around AI" | https://www.cio.com/article/4196348/your-service-vendors-are-being-rebuilt-around-ai.html | S (nota periodística) | 1 | 1 | 1 | 1 | [L] |
| AlixPartners, *Enterprise software outcome-based pricing* | https://www.alixpartners.com/media/javp02x3/enterprise-software-outcome-based-pricing-pdf-final.pdf | S (consultora) | 2 | 1 | 1 | 2 | [S] |
| TechTarget, "Outcomes-based AI pricing works in theory but in practice..." | https://www.techtarget.com/it-strategy/news/366651390/Outcomes-based-AI-pricing-works-in-theory-but-in-practice | S | 1 | 1 | 1 | 1 | [S] |
| Ailoitte en dev.to (varios posts a favor del cobro por resultado) | https://dev.to/ailoitte_sk/the-hourly-billing-trap-why-outcome-based-software-development-wins-in-2026-3h9b | S (marketing de una agencia) | 1 | 1 | 1 | 1 | [S] no usar como evidencia |

### Afirmaciones: contratos y cobro

**Lo que ya está en Producto** (precio cerrado, tiempo y materiales con tope, intercambio a igual esfuerzo, salida pagada, adelantos): no se repite. Dos fuentes independientes que coinciden en que el precio y el alcance fijos son problemáticos para el cliente y el proveedor: el Primer («tend toward lose-lose situations for both the customer and supplier» y «Fixed-price bids have added a large risk contingency (a percentage of estimated cost as high as 50%)», sin cita) y Fowler (2004: «I always advised clients to avoid this mirage»; los proveedores «deliberately low-bid the fixed price, with the explicit plan of making a profit on change requests»; «It is possible to do a FixedPrice contract in an agile manner, but it's not wise to fix the scope»). Son dos practicantes distintos (Larman/Vodde y Fowler), no estudios. http://www.agilecontracts.org/agile_contracts_primer.pdf ; https://martinfowler.com/bliki/FixedScopeMirage.html

**Mapa de modelos y quién carga qué** (las filas con una sola fuente se marcan):

| Modelo | Qué se fija | Riesgo principal | Fuente |
|---|---|---|---|
| Precio cerrado, alcance cerrado | precio y alcance | proveedor (calidad se degrada, según el Primer) | Primer; Fowler |
| Precio cerrado por fase | precio de la fase | proveedor, fase por fase | Boag (una sola fuente) |
| Tiempo y materiales | tarifa | cliente | Primer; Fink |
| Tiempo y materiales con tope | tarifa y presupuesto máximo | cliente hasta el tope | Fink (un banco); Torchbox (una agencia); Primer |
| Precio fijo por iteración / por unidad de trabajo | precio por iteración o por punto | compartido; el proveedor suma una prima a la tarifa | Primer (una sola fuente) |
| Target-cost con ganancia y pérdida compartidas | costo objetivo | compartido | Primer |
| Alcance variable con precio fijo (ej.: Money for Nothing) | total y tamaño del alcance; lo nuevo reemplaza algo del mismo tamaño | compartido | Sutherland; evaluación escéptica de Kelly |
| Por resultado | un resultado medible | proveedor | Brynjolfsson/Petropoulos; Gartner/IDC [S] |
| Abono / retainer | pago periódico por disponibilidad o mantenimiento | proveedor si el alcance crece; cliente si no usa | ver Emprender (abono de cuidado); Primer, fase de soporte |

- Primer, fase de soporte en un caso que describe: «Progressive, capped T&M»; el presupuesto de soporte «fixed (per annum), and the scope of work variable»; «capped (per month) T&M was acceptable—simple to administer, and a high level of trust had been established.» http://www.agilecontracts.org/agile_contracts_primer.pdf
- Pagos: el Primer dice que el sistema «más popular» es pagar cada iteración al aceptarse el entregable. http://www.agilecontracts.org/agile_contracts_primer.pdf
- Agile Fixed Price: el modelo como tal no lo leí en una fuente primaria. El Primer lo trata como FPFS con Scrum (recomendaciones: sin cambios o intercambio a igual esfuerzo, más margen). El capítulo de Opelt y otros (sobre un «sistema adaptable de alcance») no lo pude leer. Hueco: «Agile Fixed Price» como método con nombre.

**Cobro por valor vs por horas cuando el código lo escribe un agente.** Esta es la parte más nueva y más débil en evidencia.
- Marco teórico: Brynjolfsson y Petropoulos (working paper del 23 de agosto de 2026) parten de la teoría principal-agente y de dos dimensiones, la observabilidad del resultado y la observabilidad del costo de los insumos. Dicen que la IA usada internamente para aumentar la productividad «lowers input cost observability: identical deliverables can now be produced with widely varying combinations of human time, computational spend, and unobservable orchestration effort», y que la IA desplegada en el entorno del cliente «raises outcome observability». La tesis: «AI tends to push consulting firms toward hybrid and asset-based structures». Además: «Attribution risk therefore sets a floor on outcome-signal informativeness that no amount of instrumentation can lower», lo que limita cuánto se puede ir a un contrato por resultado cuando el aporte del proveedor se confunde con todo lo que hace el cliente. Es un marco de predicción, no una medición con datos de agencias de software. https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
- Adopción real (todas las cifras de síntesis del buscador, sin abrir los informes): según Gartner, solo el 19 % de los compradores de servicios y el 13 % de los acuerdos de servicios de los vendedores usan acuerdos por resultado; IDC pone en 21 % la proporción de contratos de servicios de IA por resultado, con 23 % de compradores que lo prefieren; un repaso de Orb de 80 empresas de agentes de IA encontró cobro por resultado puro en el 3,8 % de la muestra; Gartner (Coshow) lo llama «more buzz than reality». [S] https://www.gartner.com/en/documents/8201129 ; https://www.idc.com/?p=123073
- Contra el cobro por horas: el argumento es que cuando la IA comprime las horas detrás de un entregable, cobrar por hora «castiga a quien es eficiente y premia al lento» (esto es paráfrasis del buscador sobre varias fuentes, no cita). Aparece sobre todo en blogs de una agencia que vende su propio modelo por resultado, que no cuentan como evidencia. [S] https://dev.to/ailoitte_sk/the-hourly-billing-trap-why-outcome-based-software-development-wins-in-2026-3h9b
- Dificultad específica del software: AlixPartners nota que el código generado por un agente es más difícil de atar a un resultado limpio que los tickets resueltos o los leads calificados [S]. https://www.alixpartners.com/media/javp02x3/enterprise-software-outcome-based-pricing-pdf-final.pdf
- Riesgo de transferirlo: CIO.com advierte que «pay for outcomes» puede ser «a risk transfer unless you can govern it»; no da números de desarrollo de software. https://www.cio.com/article/4196348/your-service-vendors-are-being-rebuilt-around-ai.html
- Consejo de IDC por la síntesis: costo por resultado resuelto para trabajo contable, y retainer o estructuras por valor para trabajo de juicio [S].
- Qué dicen dos fuentes independientes sobre «híbrido»: Brynjolfsson/Petropoulos (marco teórico) y Gartner/IDC por síntesis (hábito de mercado) coinciden en que los híbridos dominan. Con la salvedad de que la segunda es [S] y de pago. Para Fink y otros (2013) los híbridos ya existían antes de la IA (precio fijo con tope al cambio; tiempo y materiales con máximo).
- Lo que **no** encontré: una medición de cuánto bajó el costo de entregar un proyecto de software a medida por el uso de agentes, ni un estudio de cómo cambian los precios de las agencias. El ensayo de METR de 2025 (16 desarrolladores experimentados, 246 tareas, febrero a junio de 2025) encontró que permitir IA «increases completion time by 19 %», con una previsión de los desarrolladores de que reduciría el tiempo en 24 %; el seguimiento de 2026 estima -4 % (intervalo de -15 % a +9 %) en desarrolladores recién reclutados y dice que los desarrolladores se aceleran más en 2026 que en 2025, pero que entre el 30 % y el 50 % no enviaron algunas tareas porque no querían hacerlas sin IA, de modo que la estimación es un piso. Hay ambigüedad de signo en la síntesis que leí: tomarlo de la fuente antes de citarlo. [S] https://arxiv.org/pdf/2507.09089 ; https://metr.org/blog/2026-02-24-uplift-update/
- Tamaño de tarea que un agente puede cerrar: METR mide el «50 % time horizon» (la duración de tarea, medida por lo que tarda un experto humano, que el modelo completa la mitad de las veces) y encontró un crecimiento exponencial con duplicación cada aproximadamente siete meses desde 2019; para o3, unos 110 minutos, y el horizonte al 80 % es unas cinco veces más corto. Las tareas son sobre todo de ingeniería de software, aprendizaje automático y ciberseguridad, y METR advierte que no se lee como «la IA hace todo el trabajo intelectual de esa duración». [S] https://arxiv.org/abs/2503.14499 ; https://metr.org/time-horizons/ . Relevante para el encargo: sirve para estimar qué porción se le puede dar a un agente, no cuánto lleva el proyecto.
- Estimación con modelos de lenguaje: los resultados son dispares. Un estudio de 2024 halló que el modelo en cero ejemplos rinde peor que los promedios y medianas de base; un preprint de marzo de 2026 dice que con pocos ejemplos mejora; un trabajo de ICPC 2026 evalúa recuperación aumentada; todos miden puntos de historia, no tiempo transcurrido, y los autores piden evaluación rigurosa antes de reemplazar Planning Poker [S]. https://arxiv.org/pdf/2403.08430 ; https://arxiv.org/pdf/2603.06276 ; https://arxiv.org/pdf/2604.03443. No encontré una fuente que compare tiempos de agente con tiempos humanos. Hueco.
- Qué mide DORA 2025: la IA mejora la entrega (throughput) y es un amplificador: «AI's primary role is to magnify an organization's existing strengths and weaknesses» y «localized pockets of productivity that are often lost to downstream chaos» (palabras del buscador sobre el resumen); la inestabilidad aparece como problema sin cifras que yo haya visto [S]. https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/ . La lectura para un encargo: el costo se mueve de programar a todo lo demás (definir, verificar, integrar, mantener), y es ahí donde el precio tiene que apoyarse.

### Qué cambia con agentes (resumen del componente)

- Cambia: el insumo (horas de programación) pierde relación con el valor y con el costo, y se vuelve menos observable para el cliente; el cobro por hora se hace más difícil de defender y el precio cerrado más viable si el alcance está bien acotado, pero el riesgo de cola que describe Flyvbjerg sigue estando en lo que el agente no hace (definir mal, integrar, requisitos que cambian). Es una inferencia de esta base apoyada en Brynjolfsson/Petropoulos y en DORA; no hay medición propia.
- Sigue igual: nadie mide bien cuánto lleva un proyecto antes de tener un diseño, y el sesgo de optimismo no desaparece porque estime un agente (no encontré evidencia ni a favor ni en contra).
- Pierde peso: estimar en horas por tarea técnica y sumar, los story points como medida de productividad (ya en la lista de ALCANCE.md; Fowler y Duarte lo tratan como un fin en sí mismo, pero no encontré un estudio que lo refute directamente), y el cobro por hora como modelo por defecto.

### Recurso canónico

Para estimar: McConnell, el artículo del cono (8 páginas) más Jørgensen (2004), guías 3, 7, 9 y 10; para el apetito, Shape Up cap. 3 («Set Boundaries»), que es corto y se lee en media hora. Para contratos: Primer, Part 3 (libre) y Fowler, «Fixed Scope Mirage» (una página); para el cobro con agentes, el working paper de Brynjolfsson y Petropoulos, leído con la advertencia de que es de agosto de 2026 y sin revisión por pares a la vista. En qué fijarse: el eje que decide el modelo es qué tan observable es el resultado y qué tan atribuible a vos; la prima de riesgo del precio cerrado sigue sin medición.

---

## 4. plan-de-entregas

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| *Scrum Guide* (2020), Increment, Product Goal | https://scrumguides.org/scrum-guide.html | P | 3 | 2 | 1 | 2 | [L] pasajes |
| Cockburn, "Walking skeleton" (autor del término) | https://alistaircockburn.com/ (la URL que probé, alistair.cockburn.us/walking-skeleton/, dio 404) | P | 3 | 2 | 2 | 3 | no leído |
| Basecamp, *Shape Up*, cap. 2 (shaping) y glosario (ciclo, lote chico) | https://basecamp.com/shapeup/1.1-chapter-02 | P | 3 | 3 | 3 | 3 | [L] |
| Fowler/Caroli, Lean Inception (sequencer, MVP canvas) | https://www.martinfowler.com/articles/lean-inception | P | 2 | 2 | 2 | 2 | [L] |
| Bain, "Ask the Authors" y blogs de slicing (vertical vs horizontal) | https://www.bain.com/insights/designing-agile-missions/ ; https://dev.to/jan/user-stories-and-vertical-slicing-1dpo | S | 1 | 1 | 1 | 1 | [S] |
| Cohn, *User Stories Applied* (2004) y Wake, INVEST/story splitting | no abiertos | P (libros) | 3 | 3 | 3 | 2 | [S] solo citado en ALCANCE.md |
| Primer, aceptación e hitos por iteración | http://www.agilecontracts.org/agile_contracts_primer.pdf | P | 2 | 3 | 2 | 3 | [L] |

### Afirmaciones

- Incremento: «In order to provide value, the Increment must be usable.» https://scrumguides.org/scrum-guide.html
- Slicing vertical: el slicing «vertical» parte una historia en historias más chicas que cruzan todas las capas; el «horizontal» la parte por capas técnicas (interfaz, lógica, datos). Los materiales secundarios coinciden en que las horizontales no entregan valor solas. Hay una voz en contra (un foro de Scrum.org: un equipo que corta horizontal a propósito y entrega un conjunto de historias como funcionalidad, argumentando que cortar vertical no es obligatorio) y la noción de «dicing»: rebanadas que no dan valor hasta que se juntan. Todo [S] de blogs: marcar como práctica aceptada, no como resultado medido. https://www.bain.com/insights/designing-agile-missions/ ; https://dev.to/jan/user-stories-and-vertical-slicing-1dpo
- Walking skeleton (Cockburn): no pude abrir la fuente primaria; la URL probada dio 404. No cito la definición. Hueco para el término con nombre; el concepto (una implementación mínima que cruza todas las capas y despliega) aparece en los blogs de slicing como «thin vertical slices» [S].
- Release planning por secuencia, no por fechas: Lean Inception tiene un paso «Sequence the Features» (el output exacto no lo describe el artículo) y deriva de ahí el MVP canvas. https://www.martinfowler.com/articles/lean-inception
- Plan por lotes (Shape Up): ciclos de seis semanas, y la alternativa de lotes chicos de una a dos semanas; los proyectos que no terminan en un ciclo se cancelan por defecto («circuit breaker»), no se extienden. https://basecamp.com/shapeup/4.5-appendix-06
- Entrega por partes en el contrato: aceptación e hitos por iteración (Primer); ver `alcance-y-aceptacion`.
- Hueco: release planning como técnica con nombre (mapeo de historias, Jeff Patton; roadmap de entregas) sin fuente primaria leída en esta ronda.

### Qué cambia con agentes

- El corte vertical gana importancia: una rebanada fina que cruza todas las capas es una unidad que un agente puede construir y que una persona puede verificar corriéndola, mientras que una tarea por capa no se puede ver andando. Ya es una tesis de `Definicion/descomposicion-en-tareas`. No encontré un estudio sobre tamaño de tarea y éxito del agente que no sea el de METR sobre horizonte temporal (ver estimacion), que sugiere que las tareas largas fallan mucho más; esa es evidencia de apoyo, no de método.
- El walking skeleton ahora es barato de armar (el scaffolding lo hace el agente), y lo caro sigue siendo que cruce un despliegue real. Se enlaza con DevOps.
- Pierde peso: el plan por fases por capas (primero la base de datos, después la interfaz) y los plazos de varios meses sin nada visible entre medio.

### Recurso canónico

Cockburn sobre el walking skeleton (cuando se consiga abrir) y el *Scrum Guide* en lo que dice del incremento. Para el corte: el material de Cohn/Wake o Humanizing Work (no leído). En qué fijarse: que cada rebanada sea usable por el cliente y esté desplegada, no solo pasada por pruebas.

---

## 5. cambios-de-alcance

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| *Agile Contracts Primer* v5, sección Change Management y Part 3 | http://www.agilecontracts.org/agile_contracts_primer.pdf | P | 2 | 3 | 2 | 3 | [L] (la sección y el consejo «Avoid mandating change-management boards…», línea ~1004 de la extracción) |
| Sutherland (2008), change for free | http://jeffsutherland.com/scrum/2008/10/agile-contracts-money-for-nothing-and.html | P | 3 | 2 | 2 | 3 | [L] (en Producto) |
| Fowler (2004), Fixed Scope Mirage | https://martinfowler.com/bliki/FixedScopeMirage.html | P | 2 | 1 | 1 | 2 | [L] |
| Shape Up, circuit breaker y scope hammering | https://basecamp.com/shapeup/4.5-appendix-06 | P | 3 | 3 | 3 | 3 | [L] |
| Capers Jones (1-3 % por mes), Kulk y Verhoef (2008) | https://www.ppi-int.com/wp-content/uploads/2021/01/Software-Requirements-and-the-Ethics-of-Software-Engineering.pdf | S / P | 2 | 1 | 1 | 2 | [S] (en Producto) |
| Blogs de agencia sobre change orders | https://www.wix.com/studio/blog/avoid-scope-creep | S | 1 | 1 | 1 | 1 | [S] (en Producto) |
| PMBOK 6, Control Scope / change control | https://www.projectmanagement.com/blog-post/58284/project-scope-management-part-6--control-scope | S | 1 | 1 | 1 | 1 | [S] (en Producto) |

### Afirmaciones

La mayor parte está en `proyecto-a-precio-cerrado.md` (cambio cotizado por escrito, art. 1264 CCyC, intercambio a igual esfuerzo, Capers Jones, scope creep de las agencias). Lo que suma:

- El Primer toma una postura clara: contra el control de cambios formal en el modelo ágil. «Avoid mandating change-management boards, change requests, or special change processes», con la lógica de que el cambio tiene que ser fácil y frecuente. Admite grados: baja flexibilidad en precio fijo, media en target-cost. http://www.agilecontracts.org/agile_contracts_primer.pdf
- Presupuesto de cambios como práctica: una bolsa de horas o de puntos acordada de antemano, que se gasta sin trámite mientras dura, es la forma en que los contratos ágiles evitan el change request caso por caso. No lo vi explícito en el Primer en lo que leí; Sutherland lo hace con «change for free» mientras el alcance total no crezca. http://jeffsutherland.com/scrum/2008/10/agile-contracts-money-for-nothing-and.html . Hueco: una fuente que describa el presupuesto de cambios como técnica con nombre y su efecto medido.
- La respuesta de Shape Up a un cambio es recortar o cancelar, no agregar tiempo: *scope hammering* y *circuit breaker* (ver estimacion). https://basecamp.com/shapeup/4.5-appendix-06
- Fowler da la causa del juego perverso: la oferta baja intencional para ganar con los cambios. https://martinfowler.com/bliki/FixedScopeMirage.html
- Qué parte del cambio es inevitable: Capers Jones, 1 % a más de 3 % por mes durante análisis, diseño y programación, y un resumen que dice que a 1 % mensual un proyecto de 12 meses deja más de 10 % del alcance final sin definir cuando se terminan los requisitos [S, ver Producto]. Dos fuentes que miden: ninguna leída, así que es débil.

### Qué cambia con agentes

- Menos costo de rehacer: si el agente reconstruye una pieza en horas, el costo de un cambio de alcance cae más para el proveedor que para la planificación. Esto es lectura de esta base; no encontré medición. Lo que no cae: el costo de decidir, de verificar y de tocar partes ya aceptadas (regresiones).
- Que el cambio sea barato de programar empuja a aceptar más cambios y a que el alcance crezca sin que nadie lo decida (*gold-plating* automático). La regla de intercambio a igual esfuerzo (Primer) sigue siendo la defensa y pasa a expresarse en tamaño de resultado, no en horas.
- Pierde peso: el formulario de change request con aprobación por comité, y la estimación por hora de cada cambio como forma de cobrarlo.

### Recurso canónico

El Primer, sección Change Management, junto con el artículo de Fowler (una página) como contraste, y Shape Up (apéndice y cap. 3) para el enfoque del tiempo fijo. En qué fijarse: qué regla existe antes del primer pedido de cambio (intercambio, presupuesto, o cotización), y que los cambios se comparen contra lo aceptado y no contra la memoria.

---

## 6. seguimiento-con-el-cliente

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| *Scrum Guide* (2020), Sprint Review, Product Goal | https://scrumguides.org/scrum-guide.html | P | 3 | 2 | 1 | 2 | [L] pasajes |
| *Agile Contracts Primer* v5 | http://www.agilecontracts.org/agile_contracts_primer.pdf | P | 2 | 3 | 2 | 3 | [L] |
| PMI, *PMBOK Guide* 7ª ed., principios y dominios (stakeholders, riesgo, medición) | https://www.pmi.org/pmbok-guide-standards/foundational/PMBOK | P (ficha) | 3 | 1 | 1 | 2 | [S] |
| Basecamp, *Shape Up*, apéndice (hill charts) | https://basecamp.com/shapeup | P | 3 | 3 | 3 | 3 | no leído en esta ronda |
| DORA 2025 (medición de entrega) | https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/ | P | 3 | 3 | 2 | 3 | [S] |
| Fowler, "The Purpose of Estimation" (seguir contra un plan) | https://martinfowler.com/bliki/PurposeOfEstimation.html | P (practicante) | 2 | 1 | 1 | 2 | [L] |

### Afirmaciones

- Demo: «The purpose of the Sprint Review is to inspect the outcome of the Sprint and determine future adaptations.» «The Scrum Team presents the results of their work to key stakeholders and progress toward the Product Goal is discussed.» https://scrumguides.org/scrum-guide.html . El *Scrum Guide* da el qué (inspeccionar el resultado y adaptar), no la cadencia ni el formato para un cliente externo.
- Software andando como medida de avance: el principio del Manifiesto Ágil de que el software que funciona es la medida principal de progreso es ampliamente citado; no lo pude abrir esta ronda. Lo que sí está en el Primer: cada iteración con aceptación contra pruebas acordadas, y el pago por iteración aceptada (líneas ~1069 y ~1212 de la extracción), lo que convierte la evidencia de avance en algo contractual. http://www.agilecontracts.org/agile_contracts_primer.pdf
- Pronóstico como reporte: la previsión por ritmo de Monte Carlo (ver estimacion) y el «contar ítems terminados contra el restante» de Duarte son la forma de mostrar el avance sin story points. https://www.infoq.com/articles/book-review-noestimates
- Seguir contra un plan: Fowler dice que «a plan acts as a baseline to help assess changes». https://martinfowler.com/bliki/PurposeOfEstimation.html
- Gestión de expectativas y de riesgos con el cliente: el PMBOK 7 tiene dominios de interesados y de incertidumbre/riesgo; no pude abrir su contenido [S]. Una fuente primaria sobre cadencia y formato de reportes a un cliente de proyecto a medida: no encontré. Hueco grande.
- Evidencia empírica sobre demos y participación del cliente: no encontré estudios. Jørgensen identifica el sobreoptimismo como el problema central (nota de Producto), y eso apoya mostrar software andando temprano, pero es una lectura de esta base.

### Qué cambia con agentes

- Con el agente que construye rápido, el riesgo de seguimiento es el de cantidad sin dirección: muchas rebanadas pequeñas que nadie del cliente revisa. La demo frecuente es la forma de que el cliente corrija el rumbo antes de que se acumule código; se enlaza con `Verificacion/` (qué verificó una persona y qué no) y debe decirle al cliente qué fue generado y verificado cómo. Sin fuente específica para el cliente; es lectura de esta base.
- DORA 2025 señala que los beneficios de la IA se pierden en el caos de lo que viene después (integrar, desplegar, operar), así que lo que se muestra al cliente tiene que estar desplegado, no solo en una rama. [S]
- Pierde peso: el informe de estado semanal con porcentaje de avance, y el burndown con story points como evidencia. La evidencia es software corriendo y ritmo medido en ítems entregados.

### Recurso canónico

*Scrum Guide* (Sprint Review) para el propósito de la demo, y el Primer (Acceptance y Payment) para volver esa evidencia contractual. En qué fijarse: que la demo la hagan con el cliente decidiendo sobre algo corriendo, y que los reportes se apoyen en ítems terminados y en riesgos con dueño, no en porcentajes. Esta vertical es la de menor evidencia; conviene marcarla en la nota como práctica de la escuela y no como hallazgo.

---

## 7. traspaso

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| *Agile Contracts Primer* v5 (Deliverables, Warranty, caso de fase de soporte) | http://www.agilecontracts.org/agile_contracts_primer.pdf | P | 2 | 3 | 2 | 3 | [L] |
| Miquido, "Software Project Handover Checklist" | https://miquido.com/blog/software-project-handover-checklist | S (agencia) | 1 | 1 | 1 | 1 | [S] |
| Axonbuild, "software project handover checklist" | https://axonbuild.com/blog/software-project-handover-checklist/ | S (agencia) | 1 | 1 | 1 | 1 | [S] |
| Simplethread, "Checklist for Handing Off a Software Project" | https://www.simplethread.com/handing-off-a-software-project/ | S (agencia) | 1 | 1 | 1 | 1 | [S] |
| Wavect, "When a build ends" | https://wavect.io/software-development-guide/software-handover-checklist/ | S (agencia) | 1 | 1 | 1 | 1 | [S] |
| Manifestly, "Project Closure Checklist" | https://app.manifest.ly/public/checklists/project-closure-checklist | S | 1 | 1 | 1 | 1 | [S] |
| Sprintlaw (blog legal UK), cláusulas de aceptación y garantía | https://sprintlaw.co.uk/articles/software-acceptance-criteria-contracts/ | S | 1 | 1 | 1 | 1 | [S] (en Producto) |
| PMBOK 6, Close Project or Phase | no abierto | P | 3 | 1 | 1 | 2 | sin contenido; hueco (también en Producto) |

Nota de independencia: las guías de traspaso de agencias son todas secundarias y varias se parecen mucho entre sí; cuentan como **una** fuente sobre qué suele incluirse, no como confirmación mutua.

### Afirmaciones

- Qué se entrega según las guías de agencias (sin estudio, práctica común): repositorio en la cuenta del cliente o transferido a ella, con una lista de quién tiene acceso y la fecha de fin del acceso de la agencia; después de transferir un repositorio de GitHub quedan webhooks, secretos y deploy keys atados que hay que revisar; rotar claves y pasar hosting, dominio y cuentas de terceros a nombre del cliente (las cuentas atadas al correo de un ingeniero son una fuente común de problemas); documentación (arquitectura, runbooks, changelog, guía de contribución en el repositorio, y activos que viven fuera del control de versiones); sesiones de capacitación grabadas antes de cerrar el contrato. [S] https://miquido.com/blog/software-project-handover-checklist ; https://axonbuild.com/blog/software-project-handover-checklist/ ; https://www.simplethread.com/handing-off-a-software-project/
- Garantía: una ventana típica de 30 días para defectos del código entregado, y la recomendación de firmar el soporte continuo antes de que venza para que no haya un hueco [S, una guía]. Es dato de práctica de una agencia; no es estándar. El informe de Producto ya anotó la cifra de 12 meses de un blog legal del Reino Unido: las dos discrepan, y ninguna sirve como norma. https://app.manifest.ly/public/checklists/project-closure-checklist
- Propiedad intelectual: las guías piden confirmar la transferencia de la propiedad del código entregado, el pago final, el inicio de la garantía y un eventual depósito del código (escrow); dicen que la división entre el código entregado y las herramientas reutilizables que se queda la agencia es una cuestión de contrato, sin regla fija [S]. Dinero y ley: hay una sola familia de fuentes (blogs de agencia) y ninguna jurisdicción argentina; el tema legal de Argentina queda fuera de este informe, igual que en el de Producto.
- Postura del Primer: con entrega incremental, el cliente recibe código desplegado continuamente; documentar al final solo si el cliente toma el mantenimiento («perhaps in a joint agile-documentation workshop»), y la fase de soporte se puede pasar a tiempo y materiales con tope mensual cuando hay confianza. http://www.agilecontracts.org/agile_contracts_primer.pdf
- Mantenimiento posterior como producto: el abono de cuidado (Emprender) ya cubre su modelo de negocio; no se repite.
- Close Project or Phase del PMBOK y un acta de entrega modelo: sin fuente (hueco, ya declarado en Producto).

### Qué cambia con agentes

- El traspaso incluye ahora el contexto para agentes: el archivo de instrucciones del repositorio (AGENTS.md o equivalente), los comandos, las pruebas y las convenciones, de modo que el cliente (o su siguiente proveedor) pueda seguir trabajando con un agente desde el primer día. Es inferencia de esta base sobre `Construccion/contexto-del-repositorio`; sin fuente que lo mida ni que lo recomiende para un traspaso.
- La documentación de arquitectura, runbooks y onboarding se generan hoy a bajo costo; lo caro es que sean verdaderas y se mantengan. Es lectura de esta base.
- Un riesgo nuevo para el cliente: código que él no puede revisar, hecho por un agente y verificado solo por pruebas. Eso hace más importante entregar las pruebas y la forma de correrlas (ver `Verificacion/`).
- Pierde peso: el documento de diseño de cien páginas como entregable de cierre y la capacitación presencial larga como único medio de transferir conocimiento.

### Recurso canónico

No hay uno que pueda recomendar con fuente fuerte. Lo más cercano: el Primer (Deliverables, Warranty y el caso de la fase de soporte) para el criterio, y una checklist de agencia como lista de verificación práctica (la de Simplethread o la de Miquido, leídas como práctica de un practicante marcada). En qué fijarse: accesos y propiedad de las cuentas, que el cliente corra solo el build y las pruebas, que la garantía y el soporte posterior se acuerden antes de que termine la garantía.

---

## Huecos

- **Fuentes primarias no abiertas:** McConnell, *Software Estimation* (2006); PMBOK 6/7/8 (solo resúmenes); Vacanti (*Actionable Agile Metrics*, *When Will It Be Done?*); Caroli, *Lean Inception* (libro); Opelt y otros, *Agile Contracts* (2013); Cohn, *User Stories Applied*; Cockburn sobre walking skeleton (la URL probada dio 404; no probé otra). Larman y Vodde aparecen solo por el Primer; no leí su libro *Practices for Scaling Lean & Agile Development* donde está el capítulo de contratos.
- **Guía de ajuste por optimismo del Green Book** (HM Treasury) y los valores de uplift para IT en reference class forecasting: no encontrados.
- **Porcentaje medido de contingencia para software**: sigue sin fuente (ya era hueco en Producto). Se siguen sin cruzar las dos cifras débiles (hasta 50 %; 15 a 25 %).
- **Kickoff y project charter**: sin fuente primaria de calidad. **Agile Fixed Price** como modelo con nombre: sin fuente primaria. **Presupuesto de cambios** como técnica: sin fuente que lo describa.
- **Seguimiento con el cliente (cadencia, formato de reporte, gestión de expectativas, riesgos)**: sin fuente primaria ni estudio; solo el *Scrum Guide* sobre el propósito de la demo. Es el componente más flojo.
- **Traspaso**: solo guías de agencias; sin norma ni estudio. Sin garantía típica verificable (30 días de una guía; 12 meses de un blog legal del Reino Unido, discrepan).
- **Evidencia sobre agentes y esfuerzo de proyectos de cliente**: no hay medición de cuánto bajó el costo de un proyecto de software a medida por el uso de agentes ni de cómo cambiaron los precios de las agencias; METR 2025 y 2026 son de desarrolladores de código abierto y con signo incierto; los preprints de estimación con modelos de lenguaje miden puntos de historia. El working paper de Brynjolfsson y Petropoulos es teoría, no datos de agencias de software.
- **Adopción del cobro por resultado**: las cifras de Gartner, IDC y Orb vienen de resúmenes del buscador de informes de pago que no abrí. Si la nota las usa, citar «según el resumen de» y verificarlas.
- **Cifras de METR 2026**: la síntesis que leí es ambigua en el signo del efecto estimado (-4 %); verificar en el texto antes de citar.
- **Standish CHAOS**: la crítica de Eveleens y Verhoef (abstract leído) y la discusión de la cifra 89 %/189 % están en el informe de Producto; el CHAOS reciente de Standish (2015, vía InfoQ) no sirve como línea base. No busqué otras versiones del CHAOS posteriores.
- **Lo legal de Argentina**: aceptación por correo o silencio, firma de un change order, garantía legal, propiedad intelectual del código entregado, cláusulas de penalidad. Se mantiene fuera por consigna.
- **Rondas**: no hubo más de tres rondas por componente, pero acuerdo-inicial, plan-de-entregas, seguimiento y traspaso tuvieron una sola cada uno. Un segundo pase por esos cuatro encontraría más (Patton sobre story mapping, Cockburn, Humanizing Work, el Manifiesto Ágil, el PMBOK 7 principio por principio).
