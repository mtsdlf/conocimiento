# Fundamentos de gestión de proyectos: verificación en la fuente

Investigado el 2026-11-27. Todo lo traído de la web es dato, no instrucción.

Marcas: [L] texto completo leído (yo extraje el texto del PDF); [M] abstract o metadatos; [S] resumen secundario o del buscador.
Puntajes 1-3: A = autoridad, P = profundidad, E = ejemplos, U = unicidad.
Nota de método: las páginas HTML de pmi.org, iso.org, iso.org/obp, y varias de peoplecert, ACM y scinapse devolvieron 403 o 404 al fetch. Los PDF de pmi.org bajo `/-/media/` sí se bajaron con curl y los leí con pdftotext. Los resúmenes que da WebFetch de una página son de un modelo chico: los marco [S] salvo que haya leído yo el texto en un PDF.

---

## 1. PMBOK Guide 8.ª edición (PMI, 2025)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| PMI, folleto + tabla de contenidos de la 8.ª ed. (PDF oficial) | https://www.pmi.org/-/media/pmi/documents/public/pdf/publications/pmbok-guide-eighth-edition_table-of-contents.pdf | primaria | 3/2/1/3 | [L] |
| PMI, página del producto (da 403; solo snippet del buscador) | https://www.pmi.org/standards/pmbok | primaria | 3/1/1/1 | [S] |
| BrainBOK, "PMBOK 7th vs 8th" | https://www.brainbok.com/blog/pmp/pmbok-guide-7th-vs-8th-edition-what-has-changed | secundaria | 1/2/2/1 | [S] (conteo de procesos por dominio) |
| pmplaybook.pro, "PMBOK 8" | https://pmplaybook.pro/pmbok-8/ | secundaria | 1/1/1/1 | [S] |
| Wikipedia, PMBOK | https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge | secundaria | 2/1/1/1 | [M] (años de edición) |
| ProjectManagement.com, lanzamiento de PMI (403 al fetch; solo snippet) | https://www.projectmanagement.com/articles/1134510/pmi-launches-the-pmbok--guide---eighth-edition | secundaria | 2/1/1/1 | [S] |

### Listas literales (verificadas, [L], PDF de PMI)

Principios (títulos de capítulo 3 de *The Standard for Project Management*, 8.ª ed.): 3.3 Adopt a Holistic View; 3.4 Focus on Value; 3.5 Embed Quality Into Processes and Deliverables; 3.6 Be an Accountable Leader; 3.7 Integrate Sustainability Within All Project Areas; 3.8 Build an Empowered Culture.

Dominios (capítulo 2 de la *Guide*, "Project Management Performance Domains"): 2.1 Governance, 2.2 Scope, 2.3 Schedule, 2.4 Finance, 2.5 Stakeholders, 2.6 Resources, 2.7 Risk (cada uno "Performance Domain").

Todo del mismo PDF de PMI. Resultado: la lista de 6 principios y 7 dominios que se había dicho de memoria queda confirmada (los nombres en inglés son los de arriba; "Be an Accountable Leader" y "Build an Empowered Culture" son los literales para "liderazgo responsable" y "equipos empoderados").

Cita literal del folleto de PMI (mismo PDF): "Simplified to six actionable principles guiding effective project management"; "Reintroduction of Process Groups as Focus Areas to accommodate diverse project delivery approaches"; "Integration of technical ways of working and other core concepts into seven comprehensive project management performance domains, including 40 newly evolved processes".

Los cinco Focus Areas (sección 4.5 del Standard, índice del PDF): Initiating, Planning, Executing, Monitoring and Controlling, Closing. Cada dominio tiene subsecciones "Processes" y "Tailoring Considerations" (2.1.6/2.1.7, 2.2.2/2.2.3, etc.).

### ¿Vuelven los procesos?

Sí. PMI lo dice literal ("40 newly evolved processes"; "Reintroduction of Process Groups as Focus Areas") en el PDF [L]. La 7.ª los había sacado (ver ítem 2).
Conteo por dominio (Governance 9, Scope 6, Schedule 3, Finance 4, Stakeholders 7, Resources 5, Risk 6 = 40): solo [S] en https://www.brainbok.com/blog/pmp/pmbok-guide-7th-vs-8th-edition-what-has-changed ; suma 40 y coincide con el total de PMI. Los nombres de cada proceso no los verifiqué (el PDF es solo índice parcial).
Discrepancia de interpretación: PMI (snippet) dice que la 8.ª "retains the principles and performance domains foundation of the Seventh Edition, but simplifies and clarifies them"; un resumen de buscador la presenta como cambio de dominios "de resultado" a dominios "de función con procesos". Es lectura de terceros [S].

### Fecha de publicación

- Noviembre de 2025: snippet de la página de PMI [S] y https://pmplaybook.pro/pmbok-8/ [S]. Wikipedia da "2025" y cita un artículo del 13-nov-2025 [M].
- Metadatos del PDF oficial [L]: ISBN 978-1-62825-829-5; incluye "ANSI/PMI 99-001-2025"; composición fechada 9/6/25 (no es fecha de publicación).
- PMI dice (snippet) que la 7.ª queda disponible hasta el 8-jul-2026 [S].
- Hueco: sin fecha exacta en fuente primaria legible.

### Huecos

Solo leí el folleto y el índice: no puedo citar la declaración de cada principio ni los nombres de los 40 procesos.

---

## 2. PMBOK Guide 7.ª edición (2021)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| PMBOK Guide 7th Edition, PDF completo (copia alojada por un tercero, con sello de licencia de miembro de PMI a nombre de otra persona) | (URL omitida: copia no autorizada) | primaria (copia no autorizada: sirve para verificar listas, no para citar largo) | 3/3/2/2 | [L] |
| PMI, "The PMBOK Guide: Seven Facts About the Pending Seventh Edition" (20-ene-2021) | https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-seven-facts.pdf?v=8dc5f84d-76f6-4405-8b1b-999dd3d4beef | primaria | 3/1/1/2 | [L] |

### Los 12 principios (literal, índice del Standard, cap. 3) [L]

3.1 Be a Diligent, Respectful, and Caring Steward; 3.2 Create a Collaborative Project Team Environment; 3.3 Effectively Engage with Stakeholders; 3.4 Focus on Value; 3.5 Recognize, Evaluate, and Respond to System Interactions; 3.6 Demonstrate Leadership Behaviors; 3.7 Tailor Based on Context; 3.8 Build Quality into Processes and Deliverables; 3.9 Navigate Complexity; 3.10 Optimize Risk Responses; 3.11 Embrace Adaptability and Resiliency; 3.12 Enable Change to Achieve the Envisioned Future State.
Fuente: PDF de la 7.ª (arriba).

### Los 8 dominios de desempeño (literal, cap. 2 de la Guide) [L]

2.1 Stakeholder; 2.2 Team; 2.3 Development Approach and Life Cycle; 2.4 Planning; 2.5 Project Work; 2.6 Delivery; 2.7 Measurement; 2.8 Uncertainty (todos "Performance Domain"). Cap. 3 de la Guide: "Tailoring"; cap. 4: "Models, Methods, and Artifacts". Mismo PDF.

### Cita de PMI sobre el giro [L]

"A move from processes to principles: The 12 project management principles in the draft of The Standard for Project Management are built around a set of statements that guide the actions and behaviors of project management practitioners regardless of development approach."
"A move from Knowledge Areas to project performance domains: The PMBOK Guide is organized around eight project performance domains defined as a group of related activities that are critical for the effective delivery of project outcomes."
Fuente: PDF de PMI "Seven Facts" (arriba). La hoja dice "expected to be available in 2021".

### Fecha

2021: página de derechos del PDF ("Seventh edition", LCCN 2021011107) [L]. Mes exacto no verificado. Ediciones según Wikipedia [M]: 1996, 2000, 2004, 2008, 2013, 2017, 2021, 2025.

### Huecos

Texto de cada principio (está en el PDF; no lo transcribí por ser copia no autorizada).

---

## 3. PRINCE2 7.ª edición (2023)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| "Unveiling PRINCE2 7" (PDF de 5 págs., texto de Axelos según su contenido, alojado por un centro de formación) | https://www.innovativelearning.eu/images/PDF/prince2_7_whats_new.pdf | primaria espejada | 2/2/1/2 | [L] |
| Wikipedia, PRINCE2 | https://en.wikipedia.org/wiki/PRINCE2 | secundaria | 2/1/1/1 | [S] |
| KnowledgeTrain, PRINCE2 7th edition | https://knowledgetrain.co.uk/project-management/prince2/prince2-course/prince2-7th-edition | secundaria (proveedor de cursos) | 1/1/1/1 | [S] |
| PeopleCert, "PRINCE2 7: a new chapter in a well-told story" | https://peoplecert.org/news-and-announcements/Prince2-7-new-chapter | primaria | 3/1/1/1 | [S] (no lista elementos ni fecha) |
| Manual oficial *Managing Successful Projects with PRINCE2 7* | no accesible | primaria | 3/3/3/3 | no leído |

### Confirmado en el texto de Axelos [L]

- Estructura: "the five integrated elements of people, principles, practice, processes, and project context".
- "PRINCE2 remains a principle-centred method and the previous seven principles still apply, albeit with some changes to the way they are described and minor changes to the titles."
- "the seven themes from the previous edition are still addressed and are renamed Practices."
- Procesos: "As before, it consists of the seven processes that support the three layers of management"; "All process chapters retain the same names and relationships between them".
- People: "The new people chapter is the largest single addition to PRINCE2"; tres actividades: "Leading successful changes; Leading successful teams; Communication".
- "Sustainability has been added as a seventh aspect of project performance"; se agrega gestión de datos y digital.
- La edición anterior fue 2017 y PRINCE2 nació en 1996 (mismo texto).
- Títulos de los capítulos de prácticas (tabla de cambios): Business Case, Organizing, Plans, Quality, Risk, Issues, Progress.

### Listas con nombres literales ([S], Wikipedia; el manual no se pudo leer)

Principios: Ensure continued business justification; Learn from experience; Define roles, responsibilities, and relationships; Manage by stages; Manage by exception; Focus on products; Tailor to suit the project. https://en.wikipedia.org/wiki/PRINCE2 [S]. Corroboración parcial: KnowledgeTrain dice que cambiaron de título "ensure continued business justification" y "define roles, responsibilities, and relationships" [S].

Prácticas: Business case, Organizing, Quality, Plans, Risk, Issues, Progress. Wikipedia [S] + KnowledgeTrain [S] + títulos de capítulo de Axelos [L]: lista bien corroborada.

Procesos (Wikipedia [S]): Starting up a project; Initiating a project; Directing a project; Controlling a stage; Managing product delivery; Managing stage boundaries; Closing a project. Axelos [L] confirma que son siete y que los nombres no cambiaron. Un buscador citó una tarjeta de referencia v7 con "Manage a stage boundary": el título exacto de cada proceso exige el manual.

### Discrepancia sobre "people"

- Axelos (what's new) [L]: Leading successful changes; Leading successful teams; Communication.
- KnowledgeTrain [S]: Organizational and project ecosystems; Change management; Culture; Leadership.
Dicen cosas distintas. La de Axelos es la más directa; falta cotejar con el manual.

### Fecha

7.ª ed.: septiembre de 2023 (KnowledgeTrain [S]); "2023" (Wikipedia [S]). PRINCE 1989 (derivado de PROMPT II, CCTA) y PRINCE2 1996: Wikipedia [S]; 1996 también en Axelos [L].

### Huecos

Manual y tarjeta de referencia sin acceso. Lista de principios y nombres exactos de procesos: solo [S].

---

## 4. ISO 21502:2020

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| DIN/Beuth, índice del texto ISO 21502:2020 (PDF de 3 págs.) | https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download | primaria (índice publicado por el distribuidor) | 3/3/1/3 | [L] (solo índice) |
| ISO 21500:2021, muestra con el prólogo (iTeh) | https://cdn.standards.iteh.ai/samples/75704/66d8037f5925439480f7ccce8a86a5bf/ISO-21500-2021.pdf | primaria (muestra del estándar) | 3/1/1/3 | [L] |
| AFNOR, ficha ISO 21502:2020 | https://www.boutique.afnor.org/en-gb/standard/iso-215022020/project-programme-and-portfolio-management-guidance-on-project-management/xs137197/338025 | secundaria oficial | 2/1/1/1 | [S] |
| BSI, ficha ISO 21500:2021 | https://knowledge.bsigroup.com/products/project-programme-and-portfolio-management-context-and-concepts | secundaria oficial | 2/1/1/1 | [S] |
| iso.org/standard/74947.html | no accesible (403) | primaria | | no leído |

### Estructura literal (índice) [L]

"Project, programme and portfolio management — Guidance on project management", 52 páginas.
1 Scope; 2 Normative references; 3 Terms and definitions.
4 Project management concepts: 4.1 Overview; 4.2 Context; 4.3 Project governance (4.3.1 Governance framework, 4.3.2 Business case); 4.4 Project life cycle; 4.5 Project organization and roles (4.5.1 organization, sponsoring organization, project board, sponsor, assurance, manager, project office, work package leader, team members, stakeholders, other roles); 4.6 Competencies of project personnel.
5 Prerequisites for formalizing project management: 5.1 Overview; 5.2 Considerations for implementing project management; 5.3 Continuous improvement of the project management environment; 5.4 Alignment with organizational processes and systems.
6 Integrated project management practices: 6.1 Overview; 6.2 Pre-project activities; 6.3 Overseeing a project; 6.4 Directing a project; 6.5 Initiating a project (project team mobilization; governance and management approach; initial project justification; initial project planning); 6.6 Controlling a project (progressive justification; managing project performance; managing the start and close of each project phase; managing the start, progress and close of each work package); 6.7 Managing delivery; 6.8 Closing or terminating a project; 6.9 Post-project activities.
7 Management practices for a project (17): 7.2 Planning; 7.3 Benefit management; 7.4 Scope management; 7.5 Resources management; 7.6 Schedule management; 7.7 Cost management; 7.8 Risk management; 7.9 Issues management; 7.10 Change control; 7.11 Quality management; 7.12 Stakeholder engagement; 7.13 Communication management; 7.14 Managing organizational and societal change; 7.15 Reporting; 7.16 Information and documentation management; 7.17 Procurement; 7.18 Lessons learned.
Annex A (informative): Project management processes based on practices.
Fuente: DIN/Beuth (arriba). Un resumen del buscador mostraba una numeración distinta (un borrador DIN sin 6.6); el índice final sí tiene 6.6.

### Qué reemplazó

Prólogo de ISO 21500:2021, literal: "This second edition, together with ISO 21502:2020, cancels and replaces the first edition (ISO 21500:2012), which has been technically revised." [L] (muestra iTeh). AFNOR: ISO 21500:2012 figura "Cancelled", reemplazada [S].
Discrepancia: BSI dice que BS ISO 21500:2021 no es revisión de la de 2012 y que la guía de 2012 fue revisada y redesignada como ISO 21502 [S, snippet]. Prevalece el prólogo ISO. Reparto de alcance según ANSI: 21500:2021 = visión general; 21502:2020 = guía de gestión de proyectos [S] https://blog.ansi.org/ansi/iso-21502-2020-project-management-guidance/ (403, snippet).

### Huecos

Texto de las cláusulas (solo índice); prólogo propio de 21502:2020 no leído.

---

## 5. IPMA ICB4 (2015)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| GPM, "Individual Competence Baseline für Projektmanagement", Version 4.0, edición alemana (1.ª ed. actualizada feb 2017; copyright IPMA 2015); traducción autorizada con nombres ingleses entre paréntesis | https://www.gpm-ipma.de/fileadmin/user_upload/ICB4_Projektmanagement.pdf | primaria | 3/3/2/3 | [L] |
| BCS, evento IPMA "28 competencies" | https://www.bcs.org/events-calendar/2026/november/ipma-international-project-management-association-and-the-28-competencies/ | secundaria | 1/1/1/1 | [S] (solo título) |

### Estructura literal [L]

"Kompetenz im Projektumfeld wird in 29 Kompetenzelemente unterteilt": Perspective (5), People (10), Practice (14). Mismo PDF. El PDF cita la definición en inglés: "People CEs define the personal and interpersonal competences…; Practice CEs define the technical aspects of managing…; Perspective CEs define the contextual competences…".

Perspective: 1 Strategy; 2 Governance, structures and processes; 3 Compliance, standards and regulations; 4 Power and interest; 5 Culture and values.
People: 1 Self-reflection and self-management; 2 Personal integrity and reliability; 3 Personal communication; 4 Relationships and engagement; 5 Leadership; 6 Teamwork; 7 Conflicts and crisis; 8 Resourcefulness; 9 Negotiation; 10 Results orientation.
Practice: 1 Design; 2 Requirements, objectives and benefits; 3 Scope; 4 Time; 5 Organisation and information; 6 Quality; 7 Finance; 8 Resources; 9 Procurement and partnership; 10 Plan and control; 11 Risk and opportunity; 12 Stakeholders; 13 Change and transformation; 14 Select and balance.
Aplicabilidad: en la tabla de la edición de proyectos, "Practice 14: Select and balance" figura "n/a" (aplica a portafolios y programas), así que para proyectos aplican 13 de Practice.

### Discrepancia

Algunas fuentes hablan de "28 competencias"; el ICB4 en la edición GPM dice 29 [L]. No pude rastrear el origen del 28.

### Huecos

No leí el PDF original en inglés (la copia de pma-india da 403); los nombres ingleses vienen de la tabla de la edición GPM (traducción autorizada).

---

## 6. escuelas-de-gestion-de-proyectos

### Escuelas de práctica

| Escuela | Qué sostiene | Autores / año | Evidencia verificada |
|---|---|---|---|
| Predictiva / por plan | Definir alcance, plan y cronograma al inicio y controlar contra el plan | Gantt (1910s), CPM (paper de Kelley y Walker 1959), PERT (1958), PMBOK/PRINCE2 | Fechas en el ítem 7. Evidencia empírica de su eficacia: no verificada |
| Ágil | "Individuals and interactions over processes and tools; Working software over comprehensive documentation; Customer collaboration over contract negotiation; Responding to change over following a plan" | Manifiesto ágil, 2001 | Texto literal [L]: https://agilemanifesto.org/ (copyright 2001) |
| Lean / flujo | Gestionar el flujo, limitar el trabajo en curso; economía del desarrollo de producto | Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business* (2010); Reinertsen, *The Principles of Product Development Flow* (2009) | Anderson: Goodreads dice 7-abr-2010 [S] https://www.goodreads.com/book/show/8086552 ; Agile Alliance lo llama el primer relato del método Kanban [S] https://www.agilealliance.org/?p=8027291 . Reinertsen: sin verificar |
| Cadena crítica | Proteger el plazo con buffers en la cadena de recursos | Goldratt, *Critical Chain* (1997) | Sin verificar |
| Shape Up | Ciclos fijos de seis semanas, "appetite" en vez de estimación, "shaping", "betting table" | Ryan Singer, Basecamp | Glosario literal [L] https://basecamp.com/shapeup : cycle = "A six week period of time where teams work uninterruptedly on shaped projects." El año 2019 no figura en la página: sin verificar |
| Adaptativa / híbrida | Elegir el enfoque (predictivo, adaptativo, híbrido) según el trabajo | PMBOK 7 y 8 (cap. 4 de la 8.ª: 4.2.1 Predictive, 4.2.2 Adaptive, 4.2.3 Hybrid Approaches) | [L] índice PMBOK 8 (URL en ítem 1) y "predictive, adaptive or hybrid" en PMI Seven Facts (URL en ítem 2) |
| Megaproyectos | Los grandes proyectos se desvían sistemáticamente; planear con realismo | Flyvbjerg: "iron law" | [S] La frase "Over budget, over time, over and over again" aparece en https://cmr.berkeley.edu/2009/02/51-2-delusion-and-deception-in-large-infrastructure-projects-two-models-for-explaining-and-preventing-executive-disaster/ ; la versión con "under benefits" en la introducción del Oxford Handbook of Megaproject Management (2017), https://papers.ssrn.com/abstract=2742088 ; en el Parlamento británico: "one out of 10 major projects, for instance, is on budget", https://committees.parliament.uk/oralevidence/8678/html . Tres antídotos (planeamiento realista, equipos de alta calidad, gobernanza con incentivos): https://www.wikipedia.com/wiki/Bent_Flyvbjerg [S] |

### Escuelas académicas de investigación

- Söderlund (2011), "Pluralism in Project Management: Navigating the Crossroads of Specialization and Fragmentation", *International Journal of Management Reviews* 13(2): 153-176 (en línea oct-2010) [M] https://api.crossref.org/works/10.1111/j.1468-2370.2010.00290.x .
  Número de escuelas: un espejo bibliográfico reproduce el abstract: "seven schools of thought" (Optimization, Factor, Contingency, Behaviour, Governance, Relationship, Decision) [S] https://search.isc.ac/inventory/10/707675.htm . Un paper de conferencia dice que en 2002 propuso 5 y en 2011 extendió a 9 [S] https://opus.lib.uts.edu.au/bitstream/10453/74226/1/BAM%202016_Knowledge_revised.pdf . Las dos discrepan (7 vs 9) y no pude leer el abstract en la revista; probablemente 9 se confunde con las de Turner. Queda abierto.
- Turner, Anbari, Bredillet (2013), "Perspectives on research in project management: the nine schools", *Global Business Perspectives* 1(1): 3-28. Nueve escuelas: optimization, modelling, governance, behaviour, success, decision, process, contingency, marketing [S] https://researchinnovation.kingston.ac.uk/en/publications/perspectives-on-research-in-project-management-the-nine-schools-2/ . Libro base: Turner, Huemann, Anbari, Bredillet (2010), *Perspectives on Projects*, Routledge [S].
- Winter, Smith, Morris, Cicmil: no aparecieron en la búsqueda.

### Huecos

Reinertsen y Goldratt (libros y años); año de Shape Up; abstract original de Söderlund; evidencia empírica por escuela (ninguna verificada).

---

## 7. historia

| Hito | Dato | Fuente | Marca |
|---|---|---|---|
| Gantt | Henry Laurence Gantt (1861-1919), gráfico de los años 1910 | https://en.wikipedia.org/wiki/Timeline_of_project_management | [S], sin cita inline |
| CPM | Morgan R. Walker (DuPont) y James E. Kelley Jr. (Remington Rand), "late 1950s". Paper: Kelley y Walker (1959), "Critical-path planning and scheduling", Eastern Joint Computer Conference, pp. 160-173, doi:10.1145/1460299.1460318. El año 1957 no figura en lo que leí | https://en.wikipedia.org/wiki/Critical_path_method | [S] |
| PERT | Navy Special Projects Office, Lockheed, Booz Allen Hamilton; hecho público en 1958 en dos informes de la Marina (Polaris) | https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique | [S] |
| PMI | Fundado en 1969 en Georgia Tech (Atlanta), incorporado en Pensilvania; primer examen PMP en 1984 | https://en.wikipedia.org/wiki/Project_Management_Institute | [S] |
| PMBOK | Timeline de Wikipedia: 1987, "white paper"; página de PMI en Wikipedia: primer PMBOK en 1996; lista de ediciones de la Guide desde 1996 | https://en.wikipedia.org/wiki/Timeline_of_project_management ; https://en.wikipedia.org/wiki/Project_Management_Institute ; https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge | [S]/[M]. Las fechas 1987 y 1996 son compatibles si 1987 fue el documento previo, pero no lo verifiqué |
| PRINCE | 1989, CCTA (UK), derivado de PROMPT II (PROMPT 1975); PRINCE2 1996 | https://en.wikipedia.org/wiki/PRINCE2 ; https://en.wikipedia.org/wiki/Timeline_of_project_management | [S] |
| Manifiesto ágil | 2001 | https://agilemanifesto.org/ | [L] |
| PMBOK 7 | 2021, "A move from processes to principles" | PDF PMI Seven Facts (ítem 2) | [L] |
| PMBOK 8 | nov-2025, vuelven los procesos (Focus Areas) | ítem 1 | [L] / [S] |
| PRINCE2 7 | sept-2023 / 2023 | ítem 3 | [S] |

Sin verificar: 1957 como año de CPM. Wikipedia cita a Kwak (2005), "A brief history of Project Management", como fuente de la historia de Polaris: candidata a leer.

---

## 8. mitos-de-gestion-de-proyectos

### CHAOS report (Standish Group)

- Cifras 1994: éxito 16,2 %, "challenged" 52,7 %, "impaired" (cancelados) 31,1 %; muestra de 365 respuestas y 8.380 aplicaciones [S] (copia del reporte en https://www.math.unipd.it/~tullio/IS-1/2004/Approfondimenti/CHAOS.html , visto solo vía buscador).
- Glass (2006), "The Standish Report: Does It Really Describe a Software Crisis?", *Communications of the ACM* 49(8): 15-16 [M]. Texto en https://cacmb4.acm.org/magazines/2006/8/5855-the-standish-report/fulltext (403). Según fragmentos: Standish "could be considered fundamental to most claims of crisis"; se pregunta si los hallazgos están sesgados hacia el fracaso [S].
- Eveleens y Verhoef (2010), "The Rise and Fall of the Chaos Report Figures", *IEEE Software* 27(1): 30-36, doi:10.1109/MS.2009.154 [M] https://research.vu.nl/en/publications/the-rise-and-fall-of-the-chaos-report-figures/ . La definición de éxito de Standish tiene cuatro problemas (mide solo la exactitud de la estimación de costo, tiempo y funcionalidad; es unilateral; distorsiona la estimación; promedia números de sesgo desconocido). Probada con 5.457 pronósticos de 1.211 proyectos reales. Cita: "The Standish figures didn't reflect the reality of the case studies at all."
- Jørgensen y Moløkken-Østvold (2006), "How large are software cost overruns? A review of the 1994 CHAOS report", *Information and Software Technology* 48(4): 297-301, doi:10.1016/j.infsof.2005.07.002 [M] https://ebse.webspace.durham.ac.uk/ebse-bibliography/how-large-are-software-cost-overruns-a-review-of-the-1994-chaos-report/ . El sobrecosto medio "as high as 189%" es muy superior al de otras encuestas; la muestra puede estar "strongly biased towards 'failure projects'"; probablemente "much too high" para proyectos típicos de los 90.
- Standish 2015 cambió la definición de éxito (valor percibido por el cliente) [S] https://www.infoq.com/articles/standish-chaos-2015 . La cifra 29/52/19 que circula no la pude confirmar.

### "El 70 % de los cambios organizacionales fracasa"

Hughes (2011), "Do 70 Per Cent of All Organizational Change Initiatives Really Fail?", *Journal of Change Management* 11(4): 451-464, doi:10.1080/14697017.2011.630506 [M] https://research.brighton.ac.uk/en/publications/do-70-per-cent-of-all-organizational-change-initiatives-really-fa/ y Crossref https://api.crossref.org/works/10.1080/14697017.2011.630506 . Revisa cinco fuentes de la cifra (Hammer y Champy; Beer y Nohria; un artículo de Bain; uno de McKinsey; Kotter) y no halla evidencia empírica válida y confiable [S] https://www.projectmanagement.com/blog-post/7112/time-to-kill-the-phantom-70--failure-rate- .

### "El 90 % del tiempo del gerente de proyecto es comunicación"

Atribución más antigua hallada: Mulcahy (2002), "90% of the project manager's time is spent communicating" (p. 211), citada en la biblioteca de PMI [S] https://www.pmi.org/learning/library/basic-knowledge-useful-project-managers-communication-5784 . En foros de PMI nadie halla la investigación original; también se atribuye a Andy Crowe (*Alpha Project Managers*) y a un paréntesis del PMBOK [S] https://www.projectmanagement.com/discussion-topic/90042/ . Veredicto: sin fuente primaria verificada; a veces aparece como 75-90 %.

### Otros números sin fuente

Sin investigar en esta ronda (hueco): "x % de los proyectos fracasa" de otras consultoras, "el costo de un defecto crece 100 veces", etc. El "one out of 10 major projects is on budget" de Flyvbjerg tiene fuente (testimonio ante el Parlamento, ítem 6) pero es dicho oral.

### Huecos

Texto completo de Glass, IEEE e IST (solo metadatos/abstract); cifras 2015 de Standish; Mulcahy no leído.

---

## 9. bibliografia (candidatas y qué parte leer)

Verificadas (existencia y datos) en esta ronda:

1. PMI (2025), *The Standard for Project Management and A Guide to the PMBOK (8.ª ed.)*, ISBN 978-1-62825-829-5: cap. 3 del Standard (principios) y 4.5 (Focus Areas); el dominio que se necesite. [L índice]
2. PMI (2021), *PMBOK Guide 7.ª ed.*: cap. 3 del Standard (principios) y cap. 3 de la Guide, "Tailoring". [L]
3. Axelos (2023), *Managing Successful Projects with PRINCE2 7*: principios, people, práctica Progress (tolerancias, excepciones). Manual no leído; solo el "what's new". [L parcial]
4. ISO 21502:2020: cláusulas 6 y 7, el mapa de prácticas. [L índice]
5. IPMA (2015), *Individual Competence Baseline 4.0*: sección 3 (estructura) y los tres bloques de competencias. [L]
6. Flyvbjerg (2014), "What You Should Know About Megaprojects and Why: An Overview", *Project Management Journal* 45(2), https://www.pmi.org/learning/library/what-you-should-know-megaprojects-11656 [S]: leer completo.
7. Söderlund (2011), IJMR: abstract y tabla de escuelas. [M]
8. Turner, Anbari, Bredillet (2013): tabla de las nueve escuelas. [S]
9. Anderson (2010), *Kanban*: principios y prácticas centrales. [S]
10. Singer, *Shape Up* (Basecamp, online y gratis): partes de shaping y betting, https://basecamp.com/shapeup [L parcial].
11. Kelley y Walker (1959), "Critical-path planning and scheduling": primer paper de CPM. [M vía Wikipedia]

Sin verificar (de memoria): Goldratt (1997), *Critical Chain*; Reinertsen (2009), *The Principles of Product Development Flow*; Flyvbjerg y Gardner (2023), *How Big Things Get Done*; Kwak (2005), "A brief history of Project Management".

---

## 10. glosario (castellano / inglés)

| Castellano | Inglés | Fuente / nota |
|---|---|---|
| Dominio de desempeño | Performance domain | PMBOK 7: "a group of related activities that are critical for the effective delivery of project outcomes" [L] |
| Principio | Principle | PMBOK 7: 12; PMBOK 8: 6; PRINCE2: 7 |
| Área de enfoque (antes grupo de procesos) | Focus area (process group) | PMBOK 8 [L] |
| Área de conocimiento | Knowledge area | PMBOK 6 y anteriores; la 7.ª las reemplazó por dominios [L] |
| Adaptación a medida | Tailoring | PMBOK 7: "deliberate adaptation of the project management approach, governance, and processes" [L] |
| Enfoque de desarrollo (predictivo, adaptativo, híbrido) | Development approach (predictive, adaptive, hybrid) | PMBOK 8 cap. 4 [L] |
| Práctica (antes tema) | Practice (formerly theme) | PRINCE2 7 [L] |
| Gestión por excepción / por etapas | Manage by exception / by stages | PRINCE2 [S] |
| Caso de negocio | Business case | PRINCE2; ISO 21502 4.3.2 [L] |
| Junta del proyecto, patrocinador, aseguramiento | Project board, sponsor, assurance | ISO 21502 4.5 [L] |
| Competencias de contexto, personales y técnicas | Perspective, People, Practice | ICB4 [L] |
| Ruta crítica | Critical path (CPM) | Kelley y Walker 1959 [M] |
| Cadena crítica | Critical chain | Goldratt (sin verificar) |
| Flujo | Flow | Reinertsen (sin verificar) |
| Apetito, ciclo, moldeado, mesa de apuestas | Appetite, cycle, shaping, betting table | Shape Up, glosario [L] |
| Ley de hierro de los megaproyectos | Iron law of megaprojects | Flyvbjerg [S] |
| Gestión de beneficios | Benefit management | ISO 21502 7.3 [L] |

---

## Huecos globales

- No se pudieron abrir: HTML de pmi.org, iso.org, páginas de producto de PeopleCert, manual PRINCE2 7, Wikipedia de IPMA, scinapse, ACM, tandfonline.
- Sin investigar: otros números repetidos distintos de Standish, 70 % y 90 %; evidencia empírica de cada escuela; Reinertsen y Goldratt; año de Shape Up.
- La copia del PMBOK 7 y la de "what's new" de PRINCE2 son espejos de terceros: valen para verificar listas, no como cita pública.
