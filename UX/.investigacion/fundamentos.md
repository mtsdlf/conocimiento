# Fundamentos y el todo del tema UX: informe de investigación

Fecha de la investigación: 2026-11-22. Marcas: [L] leído completo o la sección; [M] metadatos o abstract; [S] resumen secundario o del buscador. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

## 0. Hallazgos que cambian el encargo

1. **"Jen Vinh" no existe.** "Design Thinking is Bullshit" es una charla de **Natasha Jen** (Pentagram) en la conferencia 99U de Adobe, en 2017. **Khoi Vinh** (Adobe) es otra persona y la defendió. No encontré un artículo de Medium con ese título. Citar como "Jen, 99U, 2017" y no como "Vinh, Medium". Fuente: https://www.fastcompany.com/90166804/design-thinking-is-b-s [S: el buscador la mostró, la página dio 403].
2. **"Norman acuña UX en Apple en 1993": la fecha no se confirma en fuente primaria.** Hay fuentes que dicen 1993, otras 1995 y otras "mediados de los 90". La cita primaria verificable es de Norman: "I invented the term because I thought human interface and usability were too narrow." (entrevista de Adaptive Path, citada en https://blog.adobe.com/en/publish/2017/08/28/where-did-the-term-user-experience-come-from [L]). El cargo fue "user experience architect" en Apple. Escribir "principios de los 90" y no "1993", salvo que se consiga la fuente primaria.
3. **El árbol y el campo.** La división del árbol (ux.md → capas) coincide con el campo, con tres matices. (a) ISO 9241-210 llama al proceso "diseño centrado en el ser humano" (human-centred design) y no "centrado en el usuario"; la propia norma dice que los términos "are often used synonymously" (nota 1 de 3.7). (b) "Fundamentos/mitos" tiene poca base en estas fuentes. Un mito bien documentado que apareció es "usabilidad = solo facilidad de uso": ISO 9241-210 §5.6 lo llama "a common misconception". (c) JTBD no es escuela de UX sino de producto; conviene tratarlo como contraste breve (ver hueco).
4. **Contradicción interna de ediciones:** el tema que pide "Preece/Rogers/Sharp 6.ª ed." tiene como autores, en esa edición, **Rogers, Sharp y Preece** (ese orden). Ver §6.

---

## 1. El todo: cómo se divide el sujeto

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| ISO 9241-210:2019, vista previa (portada a §5.7, índice completo) | Norma, primaria | [L] hasta p. 7; el texto de §7 es de pago | 3/3/2/3 | copia de vista previa: https://cdn.standards.iteh.ai/samples/77520/8cac787a9e1549e1a7ffa0171dfa33e0/ISO-9241-210-2019.pdf ; ficha oficial: https://www.iso.org/standard/77520.html (403 al leerla) |
| Garrett, "The Elements of User Experience" (diagrama), 30 marzo 2000 | Primaria, del autor | [L] | 3/2/2/3 | copia: https://www2.bui.haw-hamburg.de/pers/ulrike.spree/ws0910/elements_user_experience.pdf (original citado: jjg.net/ia/elements.pdf, no accesible) |
| Garrett, libro 2.ª ed., New Riders, 16 dic 2010 (copyright 2011) | Libro canónico | [S] (ficha de Pearson; el texto dio 403) | 3/3/3/3 | https://pearson.com/store/p/elements-of-user-experience-the-user-centered-design-for-the-web-and-beyond/P200000000272 |
| Preece/Rogers/Sharp, 6.ª ed. | Libro de texto | [S] (índice parcial en O'Reilly) | 3/3/3/2 | https://oreilly.com/library/view/interaction-design-6th/9781119901099 |
| Norman y Nielsen, "The Definition of User Experience (UX)" | Instituto de practicantes | [S] (resumen de WebFetch de la página) | 2/2/2/3 | https://www.nngroup.com/articles/definition-user-experience/ |

### Afirmaciones

**ISO 9241-210:2019 (todas [L], literal, de la vista previa)**
- Es la "Second edition 2019-07"; "cancels and replaces the first edition (ISO 9241-210:2010), of which it constitutes a minor revision" con tres cambios: Figure 1 actualizada, más información sobre accesibilidad en 7.1 y cambios editoriales. Que está vigente (confirmada en 2025) viene de la página de ISO vía buscador [S]: https://www.iso.org/standard/77520.html
- Definición 3.7: "human-centred design: approach to systems design and development that aims to make interactive systems more usable by focusing on the use of the system and applying human factors/ergonomics and usability knowledge and techniques". Nota 1: se usa "human-centred" y no "user-centred" "in order to emphasize that this document also addresses impacts on a number of stakeholders"; "in practice, these terms are often used synonymously".
- Definición 3.15: "**user experience**: user's perceptions and responses that result from the use and/or anticipated use of a system, product or service". Nota 1: "Users' perceptions and responses include the users' emotions, beliefs, preferences, perceptions, comfort, behaviours, and accomplishments that occur before, during and after use." Nota 2: "User experience is a consequence of brand image, presentation, functionality, system performance, interactive behaviour, and assistive capabilities of a system, product or service. It also results from the user's internal and physical state resulting from prior experiences, attitudes, skills, abilities and personality; and from the context of use." La fuente declarada es ISO 9241-11:2018, 3.2.3.
- Definición 3.13: "usability: extent to which a system, product or service can be used by specified users to achieve specified goals with effectiveness, efficiency and satisfaction in a specified context of use". Efectividad: "accuracy and completeness with which users achieve specified goals"; eficiencia: "resources used in relation to the results achieved" (3.3, 3.4). Satisfacción (3.10) incluye "physical, cognitive and emotional responses".
- Definición 3.16: "user interface: all components of an interactive system (software or hardware) that provide information and controls for the user to accomplish specific tasks with the interactive system".
- **Los seis principios (§5.1, literal):** "a) the design is based upon an explicit understanding of users, tasks and environments; b) users are involved throughout design and development; c) the design is driven and refined by user-centred evaluation; d) the process is iterative; e) the design addresses the whole user experience; f) the design team includes multidisciplinary skills and perspectives".
- **Las cuatro actividades** (Tabla 1 de §4, literal): "Understand and specify the context of use" (salida: descripción del contexto de uso); "Specify the user requirements"; "Produce design solutions to meet these requirements"; "Evaluate the designs against requirements". El cuerpo de §7 (7.2 a 7.5) no estaba en la vista previa; los títulos del índice coinciden con estas cuatro.
- **Cómo se conectan las partes (ciclo):** §5.1 dice que la norma "does not assume any particular design process" y que "All the human-centred design activities identified in Clause 7 are applicable (to a greater or lesser extent) at any stage". §5.5: "Iteration should be used to progressively eliminate uncertainty" y "it is impossible to specify completely and accurately every detail of every aspect of the interaction at the beginning of development". El Example 1 de §5.5 cierra el lazo: la retroalimentación "is used to update the intended context of use, to revise the requirements and to refine proposed design solutions". Es decir, la evaluación alimenta a las otras tres actividades. **No pude ver la Figure 1** (el diagrama del ciclo) en texto; hueco menor. Cuidado: la norma dice que sirve para "any particular design process" y que es "complementary" a los métodos ágiles o en cascada (Introducción).
- §5.6: "There is a common misconception that usability refers solely to making products easy to use." §5.2: "Constructing systems based on an inappropriate or incomplete understanding of user needs is one of the major sources of systems failure."
- Alcance (§1): "It does not provide detailed coverage of the methods and techniques required for human-centred design". La norma da el marco; los métodos están en otras partes de ISO 9241 y en el resto del tema.
- Beneficios económicos (§4): menciona costos de soporte menores y "increasing the productivity of users and the operational efficiency of organizations". Es afirmación de la norma, sin cifras.

**Garrett (diagrama 2000, [L], literal)**
- Fecha: "30 March 2000", "© 2000 Jesse James Garrett". Título: "The Elements of User Experience".
- La dualidad básica: "The Web was originally conceived as a hypertextual information space; but the development of increasingly sophisticated front- and back-end technologies has fostered its use as a remote software interface."
- El modelo tiene dos columnas: "Web as software interface" (orientada a tareas, "task-oriented") y "Web as hypertext system" ("information-oriented"), con cinco niveles de abstracto a concreto: "Site Objectives" y "User Needs"; "Functional Specifications" / "Content Requirements"; "Interaction Design" / "Information Architecture"; "Interface Design", "Information Design" / "Navigation Design"; "Visual Design". Es la versión de 2000, con nombres distintos de los del libro.
- Aviso del propio autor: "this model does not describe a development process, nor does it define roles within a user experience development team". Esto importa: los planos ordenan consideraciones, no son un proceso.
- **Los cinco planos con los nombres del libro (strategy, scope, structure, skeleton, surface)** y la distinción "producto como funcionalidad / producto como información" la sostienen solo resúmenes secundarios [S]: https://mason.gmu.edu/~bluceroc/507/module5/elements.html (resumen universitario que no cita a Garrett literalmente) y https://ccnmtl.columbia.edu/enhanced/noted/how_to_design_an_educational_user_experience.html. **No obtuve el texto literal del libro.** Los términos del diagrama de 2000 ("Web as software interface" / "Web as hypertext system", "task-oriented" / "information-oriented") son la base literal verificada de esa distinción. El libro, según los resúmenes, orden de abstracto a concreto: estrategia, alcance, estructura, esqueleto, superficie, cada plano apoyado en el de abajo.
- La 2.ª edición "is no longer just about Web sites" (ficha de la edición en Pearson [S]).

**Preece/Rogers/Sharp**
- 6.ª ed., Wiley, abril 2023, 720 páginas; autores en la portada: Rogers, Sharp, Preece [S] https://www.oreilly.com/library/view/interaction-design-6th/9781119901099/. Capítulos confirmados: 1 "What is Interaction Design?"; 2 proceso del diseño de interacción; 4 aspectos cognitivos; 5 interacción social; 6 emoción; 7 interfaces; 8 recolección de datos; 13 "Interaction Design in Practice" (incluye AgileUX). **No obtuve el índice completo**: el resto de los capítulos (3, 9 a 12, 14 a 16) es hueco.

**Dónde está cada parte y cómo se conectan (propuesta para ux.md, con base en lo anterior)**
- ISO 9241-210 pone el proceso (cuatro actividades alrededor de la evaluación); Garrett pone el contenido que se decide en cada capa. La unión es mía: los planos son lo que se decide; las actividades, cómo se decide y se corrige. Marcar como síntesis propia, no de la fuente.

### Recurso canónico del todo
ISO 9241-210:2019 §3 (definiciones), §5 (principios) y Tabla 1 (actividades y salidas) para el proceso; el diagrama de Garrett de 2000 y el capítulo 1 del libro para las capas. En qué fijarse: que ISO no prescribe un proceso, y que Garrett no define roles ni proceso. Un lector no diseñador recibe primero Tabla 1 y los seis principios.

---

## 2. Qué es UX (y dónde termina cada concepto)

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| ISO 9241-210:2019 §3 | Norma | [L] | 3/3/2/3 | (ver §1) |
| Norman y Nielsen, "The Definition of User Experience (UX)" (8 ago 1998 según la página) | Instituto | [S] | 2/2/2/3 | https://www.nngroup.com/articles/definition-user-experience/ |
| Flaherty (NN/g), "UX vs. CX", 6 jul 2023 | Instituto | [S] | 2/2/2/2 | https://www.nngroup.com/articles/ux-vs-cx/ |
| Gibbons (NN/g), "Service Design 101", 9 jul 2017 | Instituto | [S] | 2/2/2/2 | https://www.nngroup.com/articles/service-design-101/ |
| Nielsen, "10 Usability Heuristics", 24 abr 1994, revisada 2024 | Instituto | [S] | 2/2/3/2 | https://www.nngroup.com/articles/ten-usability-heuristics/ |

### Afirmaciones
- ISO: UX = percepciones y respuestas del usuario por el uso o uso previsto; **incluye antes, durante y después del uso** y la marca, el rendimiento del sistema y el estado del usuario (§1, [L]). Usabilidad = efectividad, eficiencia y satisfacción para usuarios, objetivos y contexto específicos. UI = los componentes que dan información y controles. Es decir: UI es una parte de lo que produce la experiencia; usabilidad es una calidad medible de un uso específico; UX es la respuesta total.
- Norman y Nielsen (1998): UX "encompasses all aspects of the end-user's interaction with the company, its services, and its products" [S, resumen de la página]. Aclaran: "It's important to distinguish the total user experience from the user interface (UI)". Usabilidad es "a quality attribute of the UI, covering whether the system is easy to learn, efficient to use". Ejemplo del artículo: un sitio de reseñas de películas con buena búsqueda sigue teniendo mala UX si su base no incluye películas independientes pequeñas. Nota: el artículo es de 1998, anterior a ISO 9241-210:2010; las dos definiciones son compatibles en lo esencial y la de ISO es más acotada al usuario.
- UX vs CX (NN/g 2023, [S]): UX "all aspects of a person's interaction with a company, its services, and its products"; CX es la totalidad de las interacciones con la organización en el tiempo. El autor sostiene que "basically mean the same thing when interpreted correctly" y que lo importante es diseñar en tres niveles: interacción, recorrido y relación. **Otras fuentes pueden separar CX (marketing, relación comercial) de UX (producto)**: no busqué una segunda definición de CX; hueco.
- Diseño de servicios (NN/g 2017, [S]): "the activity of planning and organizing a business's resources", personas, objetos y procesos; mejora la experiencia del empleado de forma directa y la del cliente de forma indirecta. Termina el diseño de producto/UX donde empiezan los procesos de atrás ("backstage") que el usuario no ve pero sufre.
- HCI, diseño de interacción y diseño de producto: no obtuve una fuente que los delimite con definiciones literales. Preece/Rogers/Sharp cap. 1 (el libro se titula "Interaction Design: Beyond Human-Computer Interaction"): el diseño de interacción es el término más amplio que HCI [S; solo por el título y el preámbulo; hueco para leer el cap. 1].

### Recurso canónico
ISO 9241-210:2019 §3.7, 3.13, 3.15, 3.16 como definiciones que mandan; para las fronteras, la nota 2 de 3.15 (qué entra en UX). Complementos: Norman y Nielsen 1998 para "UX no es UI"; Flaherty 2023 para CX.

---

## 3. Historia

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| ISO 9241-210:2019 §3.5 (definición de ergonomía) | Norma | [L] | 3/1/1/2 | (ver §1) |
| Card, Moran, Newell 1983 (referencias en material de curso y en Kieras) | Libro, referenciado | [S] | 3/2/2/2 | https://www.cosc.brocku.ca/~bockusd/3p94/kieras96guide.pdf ; https://www.cs.umd.edu/class/fall2002/cmsc838s/tichi/goms.html |
| Johnson et al., "The Xerox Star: A Retrospective", Computer, 1989 | Primaria, del equipo | [S] (solo aparecieron en búsqueda) | 3/2/2/2 | https://worrydream.com/refs/Johnson_1989_-_The_Xerox_Star,_a_Retrospective.pdf |
| Adobe, "Where Did the Term User Experience Come From?", 28 ago 2017 | Secundaria | [L] | 1/1/2/1 | https://blog.adobe.com/en/publish/2017/08/28/where-did-the-term-user-experience-come-from |
| Nielsen, heuristics (ver §2) | Instituto | [S] | 2/2/3/2 | https://www.nngroup.com/articles/ten-usability-heuristics/ |
| Garrett diagrama 2000 | Primaria | [L] | 3/2/2/3 | (ver §1) |
| Frost, Atomic Design | Libro, del autor | [S] | 2/2/2/3 | https://atomicdesign.bradfrost.com/ |

### Fechas con fuente
- **Ergonomía / factores humanos:** definición de la norma: "scientific discipline concerned with the understanding of interactions among human and other elements of a system, and the profession that applies theory, principles, data and methods to design in order to optimize human well-being and overall system performance" (ISO 6385:2016, 2.3, citada en ISO 9241-210 §3.5, [L]). La historia de posguerra (militar, aviación) **no se investigó**: hueco.
- **Fitts 1954, Hick 1952:** los trae el brief como papers; no los verifiqué (son de otro ángulo).
- **1983:** Card, Moran y Newell, *The Psychology of Human-Computer Interaction*, Hillsdale, NJ: Erlbaum; GOMS = "a set of Goals, a set of Operators, a set of Methods for achieving the goals, and a set of Selections rules" [S] https://www.cs.umd.edu/class/fall2002/cmsc838s/tichi/goms.html . Una reseña lo llama "the seminal" libro de HCI [S, en la búsqueda; no abrí la reseña].
- **1973, Alto; 1981, Star:** "Xerox introduced the 8010 Star in April 1981" [S]; fue un fracaso comercial ("only about 25 thousand were sold") pero el equipo de Lisa lo vio en su presentación y convirtió su interfaz de texto en GUI. El Alto "was never meant for sale", con casi 1.000 unidades en uso en Xerox [S, resultados de búsqueda sobre IEEE Spectrum y Wikipedia: https://en.wikipedia.org/wiki/Xerox_Star ]. **La fecha del Alto (1973) no la confirmé.**
- **1985:** Gould y Lewis, "Designing for Usability: Key Principles and What Designers Think", *Communications of the ACM* 28(3), pp. 300-311 [M, vía buscador sobre ACM y CU Boulder: https://experts.colorado.edu/display/pubid_27159 ]. Principios literales del abstract: "early and continual focus on users; empirical measurement of usage; and iterative design whereby the system (simulated, prototype, and real) is modified, tested, modified again, tested again, and the cycle is repeated again and again". Es el antecedente directo de los principios a), c) y d) de ISO 9241-210.
- **1988:** el término "user-centered design" aparece en *The Design of Everyday Things* de Norman (que entonces se llamaba *The Psychology of Everyday Things*) [S] https://blog.adobe.com/en/publish/2017/08/28/where-did-the-term-user-experience-come-from y https://jnd.org/preface-design-of-everyday-things-revised-edition/ . La ed. revisada es de 5 de noviembre de 2013 (ISBN 9780465050659).
- **Principios de los 90 ("1993" no confirmado):** Norman en Apple, "user experience architect" (ver §0).
- **1990 / 1994:** Nielsen y Molich desarrollaron las heurísticas en 1990; Nielsen las refinó en 1994 con un análisis factorial de 249 problemas de usabilidad. Literal: "originally developed the heuristics for heuristic evaluation in collaboration with Rolf Molich in 1990" [S, página de NN/g]. Página publicada 24 abr 1994.
- **1998:** Norman y Nielsen, "The Definition of User Experience" (8 ago 1998 según la página [S]).
- **2000:** Garrett publica el diagrama el 30 de marzo [L]. Una reseña del libro dice que se publicó en la primavera de 2000 en jjg.net [S]. **El libro de 2002 (1.ª ed.) no lo verifiqué en fuente**; la 2.ª es de 2010 (ver §6).
- **Era móvil y sistemas de diseño:** solo hay un dato: *Atomic Design* de Frost (2016), gratis en línea en https://atomicdesign.bradfrost.com/ [S], y la ed. de papel dejó de venderse. El resto (iPhone 2007, Material 2014, etc.) **no investigado**: hueco.

### Recurso canónico
Gould y Lewis 1985 (el paper original, vía ACM Digital Library, de pago o por la copia del autor) para el origen de los principios del diseño centrado en el usuario; el capítulo 1 de Preece/Rogers/Sharp para una historia escrita por el campo (no leído); Grudin, *From Tool to Partner: The Evolution of Human-Computer Interaction* (2017) quedó sin verificar y es el candidato a recurso de historia.

---

## 4. Escuelas

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| ISO 9241-210:2019 | Norma | [L] | 3/3/2/3 | (ver §1) |
| Gould y Lewis 1985, CACM 28(3):300-311 | Paper | [M] | 3/2/1/3 | https://experts.colorado.edu/display/pubid_27159 |
| Norman, "Design Thinking: A Useful Myth", 28 jun 2010 (Core77; copia jnd.org) | Ensayo del autor | [S] (resumen de WebFetch con citas) | 2/2/2/3 | https://jnd.org/design-thinking-a-useful-myth/ |
| Norman, "Human-Centered Design Considered Harmful", *interactions* 12(4), jul-ago 2005, pp. 14-19 (copia jnd.org 2008) | Ensayo del autor | [S] | 2/2/2/3 | https://jnd.org/human-centered-design-considered-harmful/ |
| Gibbons (NN/g), "Design Thinking 101", 31 jul 2016 (revisada 2026) | Instituto | [S] | 2/2/2/2 | https://www.nngroup.com/articles/design-thinking/ |
| Natasha Jen, "Design Thinking is Bullshit", 99U 2017 | Charla; cobertura | [S] | 1/1/1/2 | https://www.fastcompany.com/90166804/design-thinking-is-b-s ; https://designweek.co.uk/issues/5-11-march-2018/pentagrams-natasha-jen-design-monster-unleash-fix-world |
| McKinsey, "The business value of design", oct 2018 | Estudio de consultora | [S] (la página dio timeout; cifras por buscador y prensa) | 1/2/1/2 | https://www.mckinsey.com/capabilities/mckinsey-design/our-insights/the-business-value-of-design |
| Gothelf y Seiden, *Lean UX* 3.ª ed., O'Reilly, 2021 | Libro | [M] | 2/3/2/2 | https://oreilly.com/library/view/lean-ux-3rd/9781098116293 |
| Kohavi, Tang, Xu, *Trustworthy Online Controlled Experiments*, CUP, 2020 | Libro | [M] | 3/3/3/3 | https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59 |

### Afirmaciones por escuela

**Diseño centrado en el usuario / HCD (columna).** Sostiene que el diseño se basa en conocer usuarios, tareas y entorno, con evaluación e iteración (ISO 9241-210 §5.1, [L]). Antecedente: Gould y Lewis (1985): "early and continual focus on users; empirical measurement of usage; and iterative design" [M]. Evidencia: la norma afirma beneficios pero **sin cifras**; un estudio del propio Gould y Lewis aparece en su abstract como "an example of the principles being applied successfully" y "survey data suggesting these principles are not really all that obvious" [M]. Es decir, la evidencia primaria es de caso y encuesta, no experimento controlado. Cockton (CHI 2008) dice que el artículo de 1985 sigue sustentando estándares con los que se juzga el trabajo en HCI [S, en el resultado de búsqueda].

**Design thinking.** Gibbons (NN/g): "Design thinking is an ideology supported by an accompanying process." Seis fases: empatizar, definir, idear, prototipar, probar, implementar. "The specific term 'design thinking' was coined in the 1990's by David Kelley and Tim Brown of IDEO, with Roger Martin" [S]. **No pude confirmar el papel de la d.school**: la página no la menciona.
- Críticas, con sus fuentes: Norman 2010: "Design thinking is a public relations term for good, old-fashioned creative thinking." y "Act as if you believe it. Just don't actually do so." [S]. Norman lo ve útil porque contrarresta la idea de que diseño es decoración y señala que el método sirve para problemas organizacionales. Un detalle: la página de jnd.org nota que Norman "later reversed his position in a second essay" [S, resumen del propio sitio]; no leí ese segundo ensayo. Natasha Jen (99U, 2017): "design thinking was little more than a buzzword and lacked rigorous critique" [S, parafraseado por el buscador, no literal]; Khoi Vinh la defendió como "a crucial tool for democratizing design" [S].
- Evidencia a favor: McKinsey Design Index (MDI), 300 empresas cotizadas durante cinco años, 2013-18, encuesta de julio de 2018 [S]. Cifra del Exhibit 3: **32 y 56 "percentage points" (ingresos y retorno total al accionista) de diferencia entre el cuartil superior y los pares** según el exhibit; la prensa lo reporta como "32% higher revenue growth" y "56% higher" retorno (AMA, Dezeen). **Discrepancia a dar con ambas lecturas** (puntos porcentuales vs. por ciento): https://www.ama.org/marketing-news/the-business-value-of-good-design/ ; https://www.dezeen.com/2018/10/25/good-design-good-for-business-mckinsey-company-report/ . El informe dice "strong correlation" entre MDI alto y desempeño, es decir **correlación, no causalidad**. No obtuve la metodología completa ni críticas específicas del MDI (la búsqueda no las devolvió): hueco. Además McKinsey vende servicios de diseño (lanzó una división de diseño con el informe, según Dezeen), conflicto de interés a declarar.

**Lean UX (Gothelf y Seiden).** 3.ª ed. O'Reilly, ~septiembre 2021 (Apple Books dice 29 jul 2021; discrepancia), 256 pp. [M]. Se centra en el Lean UX Canvas y en el producto como experiencia y no en entregables. **No pude leer el capítulo 1** (403) para citar su definición ni sus tres raíces. Hueco.

**Diseño centrado en la actividad (Norman 2005).** Tesis, [S]: "Activity-Centered Design is superior." Argumenta que los objetos exitosos (automóvil, reloj, escritura, instrumentos musicales) no se hicieron con estudios de usuarios; que HCD se concentra en pantallas estáticas y no en secuencias; que "the best way to satisfy users is sometimes to ignore them". Aclara que no rechaza HCD de plano. **Cuidado:** el resumen devolvió la frase "Human-Centered Design does guarantee good products" que probablemente omite un "not"; no usar esa cita sin leer el original. Evidencia: argumentos y ejemplos, no datos.

**CRO / experimentación.** Kohavi, Tang y Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*, Cambridge University Press; en línea 13 mar 2020, tapa blanda 2 abr 2020; 288 páginas; ISBN 9781108724265 (tapa blanda), 9781108653985 (digital); **no es acceso abierto**, digital 45 USD; autores de Microsoft, Google y LinkedIn, empresas que ejecutan más de 20.000 experimentos al año cada una [M, ficha de Cambridge]. Sostiene que la decisión se toma con experimentos controlados y no con opinión. Límite: requiere tráfico suficiente; para una agencia con landings de poco tráfico y para sistemas internos con pocos usuarios, la aplicabilidad es acotada (inferencia mía, no de la fuente).

**Jobs to be done en UX.** Intenté NN/g (404). **Hueco completo.**

### Recurso canónico
Columna: ISO 9241-210 §5 (principios). Contraste: Norman 2005 (el único ensayo que ataca la columna desde dentro) y Norman 2010; evidencia comparativa: leer el informe de McKinsey con sus caveats (correlación). Para experimentación: Kohavi et al., caps. introductorios (en línea, de pago).

---

## 5. Fuentes: el peso de cada tipo

### Fuentes verificadas para el mapa

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Baymard Institute, "About" | Instituto | [S] | 2/3/3/2 | https://baymard.com/about |
| NN/g, "Data Tables" (Laubheimer, 3 abr 2022) | Instituto | [S] | 2/2/2/2 | https://www.nngroup.com/articles/data-tables/ |
| Cambridge, Kohavi et al. | Libro | [M] | 3/3/3/3 | (ver §4) |

### Afirmaciones
- **Normas** mandan en definiciones: ISO 9241-210 §3 [L]. La norma completa es de pago (la vista previa gratuita cubre hasta §5.7 y el índice): https://www.iso.org/standard/77520.html . WCAG 2.2 y 9241-110/11 no se verificaron en este ángulo.
- **Baymard** (propio sitio, [S]): "An independent web UX research institute"; "Over 200,000 hours of UX research, with 37,000+ new hours added each year"; benchmark de "344 leading ecommerce sites" con "275,000+ UX performance scores"; "Over 700 UX best-practice guidelines". **Gratis:** unos 470 artículos (la página dice también 450+: cifra inconsistente), que cubren "about 5%" de los hallazgos según la página; casos del benchmark; más de 18.000 ejemplos anotados. **De pago:** Premium Research (la biblioteca completa), UX Auditing, UX Training; precios no publicados en esa página. Son cifras de autodescripción, no verificadas por terceros. La página no da el número de sesiones de prueba (hay una página de metodología aparte, no leída).
- **NN/g**: método declarado por artículo; es fuente secundaria fuerte pero con opinión. Ejemplo: sus recomendaciones sobre tablas empresariales (Laubheimer 2022, [S]): cuatro tareas centrales (encontrar registros, comparar, ver o editar una fila, actuar sobre registros); "Freeze header rows and header columns (if the table is larger than the screen)"; editar una fila fuera de la tabla con panel lateral no modal; acciones por lote con casillas y "Select All" cuando hay más de una o dos acciones. Marcar como "guía de instituto".
- **Guías de plataforma:** no se investigaron (Material, HIG, GOV.UK): hueco, el brief ya fija su peso como ejemplo de práctica.
- **Pago vs. gratis, resumen verificado:** ISO 9241 (pago, vista previa gratis), Baymard (parcialmente gratis), Kohavi (de pago, 45 USD digital), *Atomic Design* (gratis en línea, ebook ~10 USD), NN/g (artículos gratis; informes y cursos de pago, no verificado).

---

## 6. Bibliografía por necesidad (datos verificados)

| Libro | Dato verificado | Marca | URL |
|---|---|---|---|
| Norman, *The Design of Everyday Things: Revised and Expanded Edition* | Basic Books, 5 nov 2013, 368 pp., ISBN 9780465050659; la 1.ª ed. de 1988 se llamaba *The Psychology of Everyday Things*; ed. UK: MIT Press | [S] | https://www.hachettebookgroup.com/titles/don-norman/the-design-of-everyday-things/9780465050659/ ; https://jnd.org/preface-design-of-everyday-things-revised-edition/ |
| Krug, *Don't Make Me Think, Revisited* | New Riders; **3.ª ed.**; publicado 24 dic 2013, copyright 2014; 216 pp.; ISBN-13 978-0-321-96551-6; añade un capítulo sobre usabilidad móvil | [L] ficha del editor | https://www.peachpit.com/store/dont-make-me-think-revisited-a-common-sense-approach-to-9780321965516 |
| Garrett, *The Elements of User Experience*, 2.ª ed. | New Riders, 16 dic 2010 (©2011), 192 pp.; los ISBN varían según el vendedor (9780321683687 impreso; 9780321624642 eText) | [S] | https://pearson.com/store/p/elements-of-user-experience-the-user-centered-design-for-the-web-and-beyond/P200000000272 |
| Rogers, Sharp, Preece, *Interaction Design: Beyond Human-Computer Interaction*, **6.ª ed.** | Wiley, abril 2023, 720 pp. (el orden de autores cambió) | [S] | https://oreilly.com/library/view/interaction-design-6th/9781119901099 |
| Cooper, Reimann, Cronin, Noessel, *About Face: The Essentials of Interaction Design*, 4.ª ed. | Wiley, 2014 (con Csizmadi y LeMoine) | [S] | https://lib.ecu.edu/catalog-preview/catalog/3813293 |
| Rosenfeld, Morville, Arango, *Information Architecture: For the Web and Beyond*, 4.ª ed. | O'Reilly, **octubre 2015** | [S] | https://oreilly.com/library/view/information-architecture-4th/9781491913529 |
| Sauro y Lewis, *Quantifying the User Experience*, 2.ª ed. | Morgan Kaufmann (Elsevier), julio 2016 (12 o 27 según la página) | [S] | https://shop.elsevier.com/books/quantifying-the-user-experience/sauro/978-0-12-802308-2 |
| Portigal, *Interviewing Users*, **2.ª ed.** | Rosenfeld Media, 17 oct 2023, 276 pp., ISBN 9781959029786; 1.ª ed. 2013; prólogo de Jamika D. Burge | [S] | https://rosenfeldmedia.com/books/interviewing-users-second-edition/ |
| Kohavi, Tang, Xu | Ver §4 (CUP, 2020) | [M] | https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59 |
| Cialdini, *Influence, New and Expanded: The Psychology of Persuasion* | Harper Business, 4 mayo 2021, 592 pp. | [S] | https://bookshop.org/book/9780062937650 |
| Wroblewski, *Web Form Design: Filling in the Blanks* | Rosenfeld Media, 2008 (mayo); reseña en *interactions* jul-ago 2008 | [S] | https://rosenfeldmedia.com/Themen/web-form-design/ ; https://interactions.acm.org/archive/view/july-august-2008/previewweb-form-design1 |
| Few, *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring*, 2.ª ed. | Analytics Press, agosto 2013, ISBN 978-1938377006, 40 USD. **El subtítulo "The Effective Visual Communication of Data" es de la 1.ª ed./Goodreads**, no el del editor. Páginas: 246 o 260 según el catálogo | [S] | https://analyticspress.com/idd.php |
| Frost, *Atomic Design* | 2016; gratis en línea; paperback discontinuado; ebook de pago | [S] | https://atomicdesign.bradfrost.com/ ; https://bradfrost.com/blog/post/ceasing-sales-of-atomic-design-paperback-version/ |
| Gothelf y Seiden, *Lean UX*, 3.ª ed. | O'Reilly, sept 2021 (Apple: 29 jul 2021), 256 pp. **El subtítulo "Designing Great Products with Agile Teams" no se pudo confirmar** | [M] | https://oreilly.com/library/view/lean-ux-3rd/9781098116293 |
| Wathan y Schoger, *Refactoring UI* | Libro más screencasts y recursos, ~250 pp., dirigido a desarrolladores; **la fecha 2018 no está confirmada** en fuente | [S] | https://refactoringui.com/ |
| Lidwell, Holden, Butler, *Universal Principles of Design* | **No verificado** (la búsqueda no devolvió nada) | — | — |

### Agrupación propuesta por necesidad
- **General (base común):** Norman 2013 (el vocabulario: affordances, modelos conceptuales), Garrett 2010 (las capas), Preece/Rogers/Sharp 6.ª ed. (texto de referencia), Krug 2013/14 (lectura corta), Lidwell (por verificar).
- **Conversión y marketing digital (agencia):** Kohavi/Tang/Xu 2020 (experimentación), Cialdini 2021 (persuasión: pertenece también al tema Marketing, avisar de la frontera), Wroblewski 2008 (formularios, núcleo de una landing), Portigal 2023 (entrevistas) y Sauro y Lewis 2016 (medir).
- **E-commerce (plataforma de tiendas):** Baymard Institute (benchmark y guías de checkout y catálogo; ver §5 para lo gratis y lo pago). **No encontré un libro de e-commerce**; el activo principal es Baymard.
- **Software de negocio (sistemas internos, tablas, dashboards):** Few 2013 (dashboards), Cooper et al. *About Face* 4.ª ed. (patrones de software de escritorio y de negocio), Frost 2016 y Wathan/Schoger (diseño visual y sistemas), NN/g "Data Tables" (tablas). 
- **Aporte propio para tablas y aplicaciones empresariales:** NN/g, Laubheimer, "Data Tables" (3 abr 2022), https://www.nngroup.com/articles/data-tables/ [S]. Falta un libro; candidatos sin verificar que sugiero buscar: Tidwell, Brewer y Valencia, *Designing Interfaces* (3.ª ed.), y Few, *Show Me the Numbers*. No los verifiqué.

### Aviso de calidad
Varias fichas son de tienda o de catálogo y no del libro; sirven para autor, año y edición, no para el contenido. Ninguno de los libros se leyó.

---

## 7. Huecos

1. **Garrett, libro:** no se obtuvo el texto literal de los cinco planos con los nombres del libro ni de "producto como funcionalidad / información" (403 en O'Reilly y Pearson; jjg.net con certificado erróneo). Solo se leyó el diagrama de 2000. Pendiente: capítulo 1 del libro (en biblioteca o en copia del autor).
2. **ISO 9241-210:** no se vio §7 ni la Figure 1 (el ciclo) por ser de pago; el cuerpo de las cuatro actividades se infiere de la Tabla 1 y del índice.
3. **ISO 9241-11:2018** (definición de usabilidad y de UX en su fuente) no se leyó directamente; los textos son citas dentro de 9241-210.
4. **Preece/Rogers/Sharp:** índice completo de la 6.ª ed. y cap. 1 (definiciones de diseño de interacción vs. HCI vs. UX) sin leer.
5. **Historia:** ergonomía de posguerra; fecha del Alto (1973); 1993 de Norman; Nielsen y la web de los 90; libro de Garrett de 2002; era móvil; sistemas de diseño (solo Frost 2016). Grudin 2017 sin verificar.
6. **Escuelas:** la metodología del Design Index de McKinsey y sus críticas; IDEO y d.school como fuente primaria; Lean UX cap. 1; JTBD en UX; el segundo ensayo de Norman sobre design thinking; el texto original de Norman 2005 (la cita del resumen puede estar incompleta). Natasha Jen: solo cobertura periodística.
7. **Fuentes del mapa:** guías de plataforma, WCAG, MeasuringU y revistas de papers sin explorar en este ángulo.
8. **Bibliografía:** Lidwell sin verificar; fecha 2018 de *Refactoring UI*; subtítulo de *Lean UX* 3.ª ed.; Krug aparece con año 2013 (publicación) y 2014 (copyright), citar "2014 (publicado dic. 2013)"; no hay libro de e-commerce ni de tablas empresariales verificado.
9. **Fuentes que no se pudieron leer:** iso.org (403), O'Reilly (403), Fast Company (403), McKinsey (timeout en tres intentos), web.archive.org (bloqueado), jjg.net (certificado).
