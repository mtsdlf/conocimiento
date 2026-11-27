# Informe: inglés profesional escrito para software (escritura técnica, code review, incidentes)

Fecha de la investigación: 2026-11-27.

**Qué significan las marcas.** Todas las páginas se leyeron con la herramienta de fetch, que devuelve un extracto filtrado por un modelo pequeño, no el texto crudo. Por eso:
- Marco **[L\*]** a lo que se recuperó y extrajo de la página real. Solo cito literal lo que aparece entre comillas en el extracto.
- Marco **[M]** a lo que solo vi por metadatos o abstract.
- Marco **[S]** a lo que solo vi en el resumen del buscador.

**Puntajes.** Van de 1 a 3, en el orden Aut / Prof / Ej / Uni (autoridad, profundidad, ejemplos, unicidad).

## 0. Sobre la división del árbol

La división en tres componentes (escritura-tecnica, code-review, incidentes) coincide con cómo divide el campo, con tres ajustes:

1. **Las fuentes tratan el commit message como parte de la descripción del cambio.** Google eng-practices lo llama "CL description" y lo pone en la guía de code review, no en la de escritura. Conviene un subtema "describir un cambio" (commit, PR) dentro de escritura-tecnica, con enlace desde code-review.
2. **"Escribir para lectores no nativos" no es un componente aparte.** Lo tratan las guías de estilo (Google y Microsoft) como una sección transversal. Dentro de escritura-tecnica va como capa transversal, y los incidentes la necesitan aún más (se lee bajo estrés y en un segundo idioma).
3. **El campo no separa "incidentes en vivo" de "postmortem" como lo hace el árbol.** El ciclo es único (roles, avisos, postmortem). Si hay que dividir, mejor por momento: durante (voz y chat), hacia afuera (status page) y después (postmortem escrito).

## 1. escritura-tecnica

### Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| Google developer documentation style guide, "Write for a global audience" | https://developers.google.com/style/translation | Primaria (guía oficial) | 3/3/3/3 | [L\*] |
| Microsoft Writing Style Guide, "Global communications" | https://learn.microsoft.com/en-us/style-guide/global-communications/ | Primaria | 3/2/1/2 | [L\*] |
| Microsoft Writing Style Guide, Welcome | https://learn.microsoft.com/en-us/style-guide/welcome/ | Primaria | 3/1/1/1 | [L\*] |
| Google Technical Writing One | https://developers.google.com/tech-writing/one | Primaria (curso) | 3/2/1/2 | [M], solo la intro |
| Plain language (Digital.gov, adaptado de PlainLanguage.gov) | https://digital.gov/guides/plain-language | Primaria (gobierno de EE. UU.) | 3/1/1/1 | [L\*] |
| Google eng-practices, "CL descriptions" | https://google.github.io/eng-practices/review/developer/cl-descriptions.html | Primaria | 3/2/3/3 | [L\*] |
| Chris Beams, "How to Write a Git Commit Message" | https://cbea.ms/git-commit/ | Practicante reconocido | 2/3/3/3 | [L\*] |
| Conventional Commits 1.0.0 | https://www.conventionalcommits.org/en/v1.0.0/ | Primaria (especificación) | 2/2/3/2 | [L\*] |
| Google design docs (Malte Ubl, "Design Docs at Google") | https://www.industrialempathy.com/posts/design-docs-at-google/ | Practicante reconocido, sobre práctica de Google | 2/3/2/3 | [L\*] |
| Rust RFC template | https://github.com/rust-lang/rfcs/blob/master/0000-template.md | Primaria | 3/2/3/2 | [L\*] |
| Oxide RFD 1, "Requests for Discussion" | https://rfd.shared.oxide.computer/rfd/0001 | Primaria | 2/3/2/3 | [L\*] |
| Mozilla, "Bug writing guidelines" | https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html | Primaria | 3/2/3/3 | [L\*] |
| Chromium, "Bug reporting guidelines" | https://www.chromium.org/for-testers/bug-reporting-guidelines/ | Primaria | 3/1/2/1 | [L\*] |

### Afirmaciones

**Escribir para lectores no nativos**
- La guía de Google dice que se escribe "in US English with localization, translation, and internationalization in mind" (parafraseo del buscador). Pide oraciones cortas, voz activa y dirigidas a "you". Fuentes: https://developers.google.com/style/translation y el resumen en el buscador.
- La misma página:
  - Pide evitar modismos, jerga y humor. Sus ejemplos: "ballpark figure", "back burner", "hang in there". https://developers.google.com/style/translation
  - Pide evitar referencias estacionales ("August isn't summer in the southern hemisphere"). Para un hispanohablante de LatAm es un buen ejemplo propio. https://developers.google.com/style/translation
  - Pide reemplazar verbos frasales por uno simple, con excepciones como "set up", "log in", "sign in". https://developers.google.com/style/translation
  - Recomienda "start" o "begin" en vez de "commence", "use" en vez de "utilize" o "leverage", "so" en vez de "consequently". https://developers.google.com/style/translation
  - Pide no omitir los pronombres relativos: "the rules that you previously defined" mejor que "the rules you previously defined". https://developers.google.com/style/translation
  - Pide poner la condición antes de la instrucción, usar un solo término por concepto y no más de dos sustantivos como modificadores. https://developers.google.com/style/translation
- Microsoft: "It's usually safe to assume your content will be read in many countries and by readers whose primary language isn't English." https://learn.microsoft.com/en-us/style-guide/global-communications/
- Microsoft define "voice": "warm and relaxed, crisp and clear, and ready to lend a hand." https://learn.microsoft.com/en-us/style-guide/welcome/
- Microsoft recomienda dos libros: Kohl, *The Global English Style Guide* (2008), y Weiss, *The Elements of International English Style* (2005). https://learn.microsoft.com/en-us/style-guide/global-communications/
- Plain language: la Plain Writing Act of 2010 exige contenido público claro, y la guía se divide en "Principles of plain language", "Writing for understanding", "Design for understanding" y "Test for understanding". https://digital.gov/guides/plain-language

**Descripciones de cambios (commit y PR)**
- Google, primera línea: "a short summary of what the CL does", como oración imperativa completa, seguida de una línea en blanco. Ejemplo: "Delete the FizzBuzz RPC and replace it with the new system." https://google.github.io/eng-practices/review/developer/cl-descriptions.html
- Malos ejemplos de Google: "Fix bug", "Fix build", "Add patch", "Phase 1". El cuerpo explica el porqué: el problema, por qué este enfoque, limitaciones conocidas y contexto que no se ve en el código. Pide poner contexto suficiente porque los enlaces externos pueden dejar de funcionar. https://google.github.io/eng-practices/review/developer/cl-descriptions.html
- Beams, siete reglas: separar asunto de cuerpo con línea en blanco; asunto de 50 caracteres como máximo; empezar con mayúscula; sin punto final; modo imperativo; cuerpo cortado a 72 caracteres; el cuerpo explica "what and why vs. how". https://cbea.ms/git-commit/
- Prueba del imperativo de Beams: el asunto debe completar "If applied, this commit will *your subject line here*". https://cbea.ms/git-commit/
- Matiz sobre Beams: la regla de 50 es una pauta y 72 es el límite duro, porque "GitHub truncates longer subjects" según el extracto. Conviene contrastar con GitHub. https://cbea.ms/git-commit/
- Conventional Commits: estructura `<type>[optional scope]: <description>`, cuerpo y pies opcionales. https://www.conventionalcommits.org/en/v1.0.0/
  - `fix` corrige un bug y `feat` agrega una funcionalidad.
  - Un cambio incompatible se marca con "BREAKING CHANGE: " o con `!` antes de los dos puntos.
  - Ejemplos: `feat(lang): add Polish language`, `docs: correct spelling of CHANGELOG`, `feat!: drop support for Node 6`.
- Discrepancia a dar en la nota: Beams pide mayúscula inicial y Conventional Commits usa minúscula tras el tipo (`feat: allow ...`). Son convenciones distintas; manda la del equipo. Fuentes: ambas URL anteriores.

**Bug reports**
- Mozilla: los pasos para reproducir son "the most important part of any bug report". Hay que separar resultado real y esperado, y no mezclar hechos con especulación. https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html
- Mozilla, resumen: "should explain the problem, not your suggested solution". Mal: "Software crashes". Bien: "Cancelling a File Copy dialog crashes File Manager". Un bug por reporte. https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html
- Frase modelo de Mozilla: "**Actual results**: My inbox displays the message 'Your browser does not support cookies (error -91)'." https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html
- Chromium: verificar con la última build, dar una descripción de alto nivel, pasos detallados, comportamiento esperado, comprobar otros navegadores y adjuntar un caso de prueba reducido. https://www.chromium.org/for-testers/bug-reporting-guidelines/

**Design docs y RFCs**
- Google design docs: contexto y alcance; goals y non-goals; el diseño en sí; alternativas consideradas (el autor las llama una de las secciones más importantes); preocupaciones transversales. Tamaño sugerido: 10 a 20 páginas para proyectos grandes y 1 a 3 para un "mini design doc". https://www.industrialempathy.com/posts/design-docs-at-google/
- Rust RFC template, secciones en orden: Summary, Motivation, Guide-level explanation, Reference-level explanation, Drawbacks, Rationale and alternatives, Prior art, Unresolved questions, Future possibilities. Frases modelo literales: "Why should we _not_ do this?" y "Why is this design the best in the space of possible designs?". https://github.com/rust-lang/rfcs/blob/master/0000-template.md
- Oxide RFD: estados prediscussion, ideation, discussion, published, committed y abandoned. Como guía, "3-5 business days to comment on your RFD before merging seems reasonable". https://rfd.shared.oxide.computer/rfd/0001

### Recursos canónicos
- **Lectores no nativos:** Google style guide, "Write for a global audience". Leer entera: es corta. Fijarse en la lista de modismos, los verbos frasales y el "that" obligatorio. Es lo más útil para un B2 que quiere pasar a C1, porque le da un criterio de simplicidad, no de elegancia.
- **Commit y PR:** Beams, más Google "CL descriptions". Fijarse en la prueba del imperativo, la primera línea que se sostiene sola y el porqué en el cuerpo.
- **Bug report:** Mozilla, en la parte de "steps to reproduce" y "expected vs actual".
- **Design doc:** Ubl para el criterio, y el template de Rust RFC como plantilla con preguntas incorporadas.

## 2. code-review

### Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| Google eng-practices, "How to write code review comments" | https://google.github.io/eng-practices/review/reviewer/comments.html | Primaria | 3/2/2/3 | [L\*] |
| Google eng-practices, "Handling pushback / How to handle reviewer comments" | https://google.github.io/eng-practices/review/developer/handling-comments.html | Primaria | 3/2/1/3 | [L\*] |
| Conventional Comments | https://conventionalcomments.org/ | Practicantes (comunidad), estándar de facto | 2/2/3/3 | [L\*] |
| Gunawardena et al., CSCW 2022, "Destructive Criticism in Software Code Review Impacts Inclusion" | https://research.google/pubs/destructive-criticism-in-software-code-review-impacts-inclusion/ | Primaria (investigación) | 3/2/1/3 | [S], solo el resumen del buscador |
| Egelman et al., ICSE 2020, "Predicting Developers' Negative Feelings about Code Review" | https://research.google/pubs/predicting-developers-negative-feelings-about-code-review/ | Primaria (investigación) | 3/2/1/3 | [S] |

### Afirmaciones

**Cómo comentar**
- Google pide ser "courteous and respectful" y a la vez muy claro. Hay que comentar el código y no a la persona. Mal ejemplo literal: "Why did you use threads here when there's obviously no benefit to be gained from concurrency?". La versión mejor habla del diseño: la concurrencia suma complejidad sin ganancia medible. https://google.github.io/eng-practices/review/reviewer/comments.html
- Explicar el porqué del comentario. Etiquetas de severidad literales: "Nit: This is a minor thing. Technically you should do it, but it won't hugely impact things." / "Optional (or Consider): I think this may be a good idea, but it's not strictly required." / "FYI: I don't expect you to do this in this CL, but you may find this interesting to think about for the future." https://google.github.io/eng-practices/review/reviewer/comments.html
- Cuidado: el extracto de la página sobre preguntas contra órdenes no encontró una regla explícita de Google. Las frases del tipo "Could you simplify this loop...?" son ilustraciones mías, no de la fuente. Hay que buscarlas en otra parte o declararlas como invención propia en la nota.
- Conventional Comments usa el formato `<label> [decorations]: <subject>`. Etiquetas: praise, nitpick, suggestion, issue, todo, question, thought, chore, note. Decoraciones: (non-blocking), (blocking), (if-minor). https://conventionalcomments.org/
- Ejemplos literales de Conventional Comments: "**question (non-blocking):** At this point, does it matter which thread has won?", "**suggestion:** Let's avoid using this specific function…", "**praise:** Beautiful test!", "**issue (ux,non-blocking):** These buttons should be red, but let's handle this in a follow-up." https://conventionalcomments.org/
- Conventional Comments dice que dejar al menos un praise por review, y que no hay que dar elogios falsos. https://conventionalcomments.org/

**Cómo responder y manejar el desacuerdo**
- Google, para el autor: "Never respond in anger to code review comments." Si estás demasiado molesto, "walk away from your computer for a while". Pregunta guía: "What is the constructive thing that the reviewer is trying to communicate to me?". Si no entendés: pedir aclaración. https://google.github.io/eng-practices/review/developer/handling-comments.html
- Pushback: "it's important to think collaboratively, not combatively or defensively". "Your first step in resolving conflicts should always be to try to come to consensus with your reviewer." Plantilla de respuesta: explicar los tradeoffs y preguntar "Are you suggesting that Y better serves the original tradeoffs". https://google.github.io/eng-practices/review/developer/handling-comments.html
- Cuidado: la cita de esa última frase está truncada en el extracto. Verificar la redacción completa antes de usarla como frase modelo.

**Investigación**
- Gunawardena et al., CSCW 2022 (Proc. ACM HCI vol. 6, CSCW2; DOI 10.1145/3555183): encuesta con viñetas a 93 profesionales. Más de la mitad dijo haber recibido feedback negativo no específico en el último año. Las mujeres consideraron la crítica destructiva menos apropiada y quedaron menos motivadas para seguir trabajando con esa persona. La crítica destructiva se percibe menos válida y con menos probabilidad de mejorar el código. Estos datos vienen del resumen del buscador; no leí el paper. https://research.google/pubs/destructive-criticism-in-software-code-review-impacts-inclusion/ y DOI vía https://api.crossref.org/works/10.1145%2F3555183
- Egelman et al., ICSE 2020, pp. 174 a 185, DOI 10.1145/3377811.3380414: 1.317 desarrolladores de una empresa; se define pushback como la percepción de conflicto interpersonal innecesario mientras un revisor bloquea un cambio. Métricas basadas en logs lo predicen con recall alto y precisión baja. Es [S]: no vi el paper. https://research.google/pubs/predicting-developers-negative-feelings-about-code-review/

### Recursos canónicos
- **Para comentar:** Google "How to write code review comments", más el vocabulario de Conventional Comments. Fijarse en las etiquetas de severidad y en el "comentar el código, no a la persona". Lo más útil para un hispanohablante, porque el español tolera órdenes directas que en inglés suenan secas.
- **Para recibir y responder:** Google "Handling pushback / handling reviewer comments".
- **Como lectura de fondo:** Gunawardena 2022. Hay que leer el paper completo antes de citarlo con números en una nota.

## 3. incidentes

### Fuentes

| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| Google SRE Book, "Managing Incidents" | https://sre.google/sre-book/managing-incidents/ | Primaria (libro) | 3/3/2/3 | [L\*] |
| Google SRE Book, "Postmortem Culture" | https://sre.google/sre-book/postmortem-culture/ | Primaria | 3/3/2/3 | [L\*] |
| Google SRE Book, Apéndice D, "Example Postmortem" | https://sre.google/sre-book/example-postmortem/ | Primaria | 3/2/3/3 | [L\*] |
| PagerDuty, Incident Response, "Incident Commander" | https://docs.pagerduty.com/ops-guides/incident-response-guide/incident-commander | Primaria (guía oficial) | 3/3/3/3 | [L\*] |
| PagerDuty, "During an incident" | https://docs.pagerduty.com/ops-guides/incident-response-guide/during-an-incident | Primaria | 3/2/2/2 | [L\*] |
| PagerDuty, "External Communication Guidelines" | https://docs.pagerduty.com/ops-guides/incident-response-guide/external-comms | Primaria | 3/2/1/3 | [L\*] |
| Atlassian, Incident communication templates | https://www.atlassian.com/incident-management/incident-communication/templates | Primaria | 3/2/3/2 | [S] (la página falló, ver huecos) |
| Etsy, Allspaw, "Blameless PostMortems and a Just Culture" (2012) | https://www.etsy.com/codeascraft/blameless-postmortems/ | Practicante reconocido | 3/3/2/3 | [S], el sitio dio 403 |

### Afirmaciones

**Roles y comunicación en vivo**
- SRE Book, cuatro roles: Incident Command ("holds the high-level state about the incident"), Operational Work ("The operations team should be the only group modifying the system during an incident"), Communication ("the public face of the incident response task force") y Planning. https://sre.google/sre-book/managing-incidents/
- Documento vivo de incidente: debe ser editable por varias personas a la vez, con lo más importante arriba. Traspaso con la frase literal "You're now the incident commander, okay?", esperando una confirmación firme. https://sre.google/sre-book/managing-incidents/
- Cuándo declarar un incidente (SRE Book): hay que involucrar a un segundo equipo; la caída es visible para clientes; o el problema sigue sin resolverse tras una hora de análisis concentrado. Prioridad: "Stop the bleeding, restore service, and preserve the evidence for root-causing." https://sre.google/sre-book/managing-incidents/
- PagerDuty, frases literales del IC (muy útiles como plantilla): https://docs.pagerduty.com/ops-guides/incident-response-guide/incident-commander
  - Presentación: "This is [NAME], I am the Incident Commander for this call." Si no hay IC: "Is there an IC on the call?".
  - Nunca "Can someone..." por el efecto espectador. Se asigna a una persona con plazo: "Bob, please investigate the high latency on web app boxes. I'll come back to you for an answer in 3 minutes." Respuesta: "Understood."
  - Decisión: "Are there any strong objections to this plan?" y, si no hay, "Hearing no objects, we are proceeding with this proposal." (así aparece escrito en la fuente, con el error). No preguntar "Does everyone agree?".
  - "Clear is better than concise." y "Making the 'wrong' decision is better than making no decision."
  - Cierre: "Ok everyone, we're ending the call at this time. Please continue any follow-up discussion on Slack. Thanks everyone."
  - Orden en la llamada: "Ok everyone, can we all speak one at a time please." y "We do not discuss incident severity during the call. We're treating this as a SEV-1."
  - Traspaso: "Everyone on the call, be advised, at this time I am handing over command to [X]."
- PagerDuty, roles de comunicación: el customer liaison publica avisos externos, incluida la status page; el internal liaison da resúmenes cortos a ejecutivos "about every 30 minutes". Regla de publicación: "If in doubt, post it out". https://docs.pagerduty.com/ops-guides/incident-response-guide/during-an-incident
- Nota para el árbol: los roles se llaman distinto en cada fuente. Google usa "communication lead", PagerDuty usa "customer liaison" y "internal liaison". Hay que dar ambos nombres.

**Comunicación externa (status page)**
- PagerDuty: el aviso inicial se decide y publica "within 5 minutes of kicking off the incident call". El segundo mensaje, dentro de 5 minutos del primero, da impacto, componentes y regiones afectadas. En las primeras dos horas, actualizar al menos cada 20 minutos. Cada actualización dice qué cambió, si empezó la recuperación y cuándo es la próxima. Para incidentes largos: evitar actualizaciones sin contenido. La actualización final confirma recuperación y si hay pérdida de datos. https://docs.pagerduty.com/ops-guides/incident-response-guide/external-comms
- Atlassian (resultado del buscador, [S]): plantillas con títulos "Investigating service disruption", "Identified service disruption", "Monitoring service disruption", y la de "monitoring" incluye un campo para el tiempo hasta la próxima actualización. https://www.atlassian.com/incident-management/tutorials/incident-communication
- Discrepancia a registrar: PagerDuty fija 20 minutos como cadencia en las primeras dos horas. La guía de Atlassian que vi no fija un número (no pude leer su página de plantillas). Una nota debería citar PagerDuty como ejemplo de política y no como regla general.

**Postmortem sin culpables**
- SRE Book: para ser blameless, un postmortem "must focus on identifying the contributing causes of the incident without indicting any individual or team." Supone que todos actuaron con buenas intenciones. "You can't 'fix' people, but you can fix systems and processes." https://sre.google/sre-book/postmortem-culture/
- Prácticas culturales: "postmortem of the month", clubes de lectura de postmortems y "Wheel of Misfortune". https://sre.google/sre-book/postmortem-culture/
- Estructura del postmortem de ejemplo (Apéndice D): título, metadatos, Summary, Impact, Root Causes, Trigger, Resolution, Detection, Action Items, Lessons Learned ("What went well", "What went wrong", "Where we got lucky"), Timeline en UTC, Supporting Information. https://sre.google/sre-book/example-postmortem/
- Frases modelo literales del ejemplo: "Shakespeare Search down for 66 minutes during period of very high interest", "Estimated 1.21B queries lost, no revenue impact", "Cascading failure due to combination of exceptionally high load and a resource leak". https://sre.google/sre-book/example-postmortem/
- Etsy/Allspaw: publicado en mayo 2012 en Code as Craft; plantea "Just Culture" (equilibrio entre seguridad y responsabilidad). Seguimiento: Etsy's Debriefing Facilitation Guide (2016). Todo esto es del buscador, no leí el artículo. https://www.etsy.com/codeascraft/blameless-postmortems/

### Recursos canónicos
- **Voz en vivo:** PagerDuty, página del Incident Commander. Fijarse en las frases literales; es el mejor material para practicar inglés oral y de chat bajo presión.
- **Roles y conceptos:** SRE Book, "Managing Incidents". Leer los cuatro roles y el traspaso.
- **Status page:** PagerDuty "External Communication Guidelines" para la cadencia, y las plantillas de Atlassian para el texto, una vez que se pueda leer la página.
- **Postmortem:** SRE Book "Postmortem Culture" para la idea y su Apéndice D para la estructura y el tono de las frases.

## 4. Huecos

- **Atlassian incident handbook**: la URL del handbook (`.../incident-management/handbook/incident-communication`) dio 404, y la página de plantillas devolvió solo la navegación. No tengo el texto literal de sus plantillas de status page; solo los títulos del buscador. Falta leerlas.
- **Etsy/Allspaw**: el sitio devolvió 403. No tengo citas literales del artículo original, solo el resumen del buscador. Falta una copia accesible (por ejemplo, kitchensoap.com, que apareció en la búsqueda pero no leí).
- **Gunawardena 2022 y Egelman 2020**: solo vi resúmenes secundarios. Antes de citar números o conclusiones en una nota hay que leer los PDF (https://storage.googleapis.com/gweb-research2023-media/pubtools/6564.pdf aparece como el del paper de CSCW; no lo abrí).
- **Preguntas en vez de órdenes** en code review: no encontré una regla explícita en Google eng-practices. Falta una fuente primaria para ese consejo (posibles: guías de Conventional Comments más largas, o Egelman y otros papers de MSR).
- **Papers de MSR/ICSE sobre toxicidad**: no hice la búsqueda más allá de dos papers. Quedan sin cubrir los trabajos sobre toxicidad detectada automáticamente en comentarios de code review y sobre confusión en reviews.
- **Google SRE Book sobre status pages**: no hay un capítulo propio. El libro no cubre texto de avisos externos con detalle; eso viene de PagerDuty y Atlassian.
- **PagerDuty postmortems**: no leí https://postmortems.pagerduty.com/culture/blameless/ ni https://docs.pagerduty.com/ops-guides/postmortem-best-practices, que aparecieron en los resultados.
- **Google "Technical Writing One/Two"**: solo la intro; no tengo la lista de módulos ni la duración. Falta leer los módulos en sí.
- **Plain language (plainlanguage.gov)**: el sitio redirige a Digital.gov, y de ahí solo tengo los títulos de las cuatro guías, no los principios concretos.
- **Google style guide**: la URL que usé fue `.../style/translation` (`.../translations` da 404). El buscador menciona que la página fue reestructurada en julio de 2026; no verifiqué si cambió el contenido.
- **Documentación**: no revisé las secciones de Google sobre documentación (por ejemplo "Highlights" o "Procedures") ni las de Microsoft sobre "Top 10 tips". Faltan para cubrir la parte "documentación" del componente 1.
- **Conventional Commits y Beams** no los comparé con la práctica real de GitHub (por ejemplo, límites de truncado de asunto). Solo Beams los menciona.
