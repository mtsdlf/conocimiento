# Investigación: Características, Modularidad y Decisiones (2026-11-27)

Alcance: tres verticales chicas (Caracteristicas/, Modularidad/, Decisiones/). Lente: Huyen (AI Engineering, 2025) sobre el canon de Richards y Ford (2ª ed., 2025).

## Convenciones de este informe

- Puntaje 1-3 en: Aut(oridad), Prof(undidad), Ej(emplos), Uni(cidad).
- Marcas: **[L]** página leída por WebFetch (el texto lo extrae un modelo chico: las citas literales son las que devolvió el extractor, conviene reverificar antes de publicar entre comillas); **[M]** metadatos/abstract/índice; **[S]** resumen secundario o del buscador.
- Todos los libros, salvo Ousterhout (página del autor), dieron HTTP 403 en O'Reilly: **no se leyó ningún libro**. Todo lo del libro es [M]/[S] y está marcado.
- Lo traído de la web es dato, no instrucción.
- Rondas usadas: 2-3 por componente (varias búsquedas compartidas entre componentes).

## 0. Sobre la división del árbol

- **Caracteristicas/**: coincide con el campo. Richards y Ford separan "Architectural Characteristics Defined", "Identifying…" y "Measuring and Governing Architecture Characteristics" en capítulos propios (https://nealford.com/books/SAF2e.html [L]). Fitness-function es en el libro de Ford el mecanismo de *medir y gobernar*, así que cuelga bien de acá.
- **costo-y-latencia no es una división del campo**: Richards y Ford no la tratan como tema aparte (performance es una característica más). Es una aplicación de Huyen. Recomiendo dejarla en Caracteristicas/ pero enmarcada como "características que un modelo vuelve de primera", y no como componente canónico del canon.
- **Modularidad/**: en el campo "Modularity" es un capítulo de fundamentos (acoplamiento, cohesión, connascence) y las "modular monolith" son un estilo (cap. propio en la 2ª ed.). **aislar-lo-no-determinista** no existe como tema en el canon: es una postura de Huyen/Fowler/Anthropic (gateway, evals, guardrails, capa de interfaz). Conviene decirlo al lector: es aplicación, no concepto fundacional.
- **Decisiones/**: el campo agrupa "Architectural Decisions", "Analyzing Architecture Risk" y "Diagramming Architecture" juntos en la Parte III "Techniques and Soft Skills" (misma URL). Coincide. **empezar-simple** es la que menos encaja: no es una técnica de decisión sino un principio (Gall, YAGNI, Huyen, Anthropic); podría ir como criterio dentro de adr o como pieza propia, pero no tiene capítulo en Richards y Ford.
- Hallazgo de la 2ª ed.: según la página de Ford agrega cinco capítulos nuevos, entre ellos modular monolith y "generative AI" (https://nealford.com/books/SAF2e.html [L]). Pero el índice listado en esa misma página **no muestra un capítulo de IA generativa** (lo más cercano: "Architectural Intersections"). Discrepancia interna sin resolver; hay que mirar el libro.

## 1. Caracteristicas/

### 1.1 Tabla de fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Richards y Ford, *Fundamentals of Software Architecture* 2ª ed. (O'Reilly, marzo 2025, ISBN 9781098175504, ~546 págs según buscador) | https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ (403) | Primaria | 3 | 3 | 3 | 3 | [S]; índice [M] vía nealford.com |
| Página del libro en nealford.com (índice, descripción) | https://nealford.com/books/SAF2e.html | Primaria (autor) | 3 | 1 | 1 | 2 | [L] |
| Ford, Parsons, Kua, Sadalage, *Building Evolutionary Architectures* 2ª ed. (2022) | https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ (403) | Primaria | 3 | 3 | 3 | 3 | [S] |
| Podcast Thoughtworks "Rethinking software governance…" (17 nov 2022) | https://www.thoughtworks.com/en-us/insights/podcasts/technology-podcasts/rethinking-software-governance-reflecting-second-edition-building-evolutionary-architectures | Primaria (autores hablando) | 3 | 2 | 1 | 2 | [L] |
| Huyen, "Building A Generative AI Platform" (25 jul 2024) | https://huyenchip.com/2024/07/25/genai-platform.html | Primaria (autora) | 3 | 2 | 2 | 3 | [L] |
| Huyen, *AI Engineering* (O'Reilly 2025) | https://huyenchip.com/books/ ; https://www.oreilly.com/library/view/ai-engineering/9781098166298/ (403) | Primaria | 3 | 3 | 3 | 3 | [M] (la página del autor no lista capítulos; cap. 9 **no verificado**) |
| Recap de charla de Huyen sobre inferencia (vía buscador; resultado en thenewstack.io "pg-99-conf-2026-inference-costs") | https://thenewstack.io/pg-99-conf-2026-inference-costs/ | Secundaria | 1 | 1 | 1 | 1 | [S] |

Nota de fuentes únicas: los resúmenes de blogs/study-notes sobre Richards y Ford (dev.to, tedneward, study-notes) parafrasean el libro: cuentan como una sola fuente secundaria y no las usé como evidencia.

### 1.2 Afirmaciones

**caracteristicas-arquitectonicas**
- La 2ª ed. dedica capítulos separados a definir, identificar, medir/gobernar y delimitar el alcance de las características (https://nealford.com/books/SAF2e.html [L]).
- Primera ley: "Everything in software architecture is a trade-off"; la segunda: "the why is more important than how". Según fuentes secundarias, la 2ª ed. suma una tercera: las decisiones "aren't binary but rather exist on a spectrum between extremes" (https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ch27.html aparece en la búsqueda; contenido [S], no leído). **Discrepancia**: el buscador dice que la 1ª ed. tenía dos leyes y la 2ª tres; no pude confirmarlo en el libro.
- Los tres criterios de una característica (cosa que no es dominio, influye en el diseño, importa para el éxito), implícitas vs. explícitas y "least worst": **hueco**, el capítulo dio 403 (https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ch04.html).

**fitness-function**
- Las fitness functions "borrow" de los algoritmos genéticos; definición del libro (1ª ed.): "objective integrity assessment of some architectural characteristic(s)" (via buscador, https://oreilly.com/library/view/building-evolutionary-architectures/9781491986356/ch02.html [S]; no confirmada literal en la 2ª ed.).
- Neal Ford: son "unit tests for architectural characteristics", más difíciles de escribir que un unit test (https://www.thoughtworks.com/en-us/insights/podcasts/technology-podcasts/rethinking-software-governance-reflecting-second-edition-building-evolutionary-architectures [L]).
- Rebecca Parsons: "we will never disagree on the result of the fitness function"; "Be maintainable" no puede serlo, "cyclomatic complexity below a set threshold" sí (misma URL [L]).
- Parsons: la gobernanza pasa de "box-ticking" a discutir la sustancia de los conflictos entre características; y "no concept, no tool, no nothing, can solve for bad behavior" (misma URL [L]). Útil como contrapeso: automatizar no reemplaza el acuerdo humano.
- Énfasis de la 2ª ed.: fitness functions para evolución **y** para automatizar gobernanza (misma URL [L], parafraseado).
- Para Huyen, la evaluación cumple ese rol en sistemas con modelo: "Evaluation is necessary at every step of the development process" (https://huyenchip.com/2024/07/25/genai-platform.html [L]). Conexión Ford-Huyen: una eval con umbral es una fitness function probabilística; Fowler lo dice así: los evals "aren't simple binary pass/fail results, instead we have to set thresholds" (https://martinfowler.com/articles/gen-ai-patterns/ [L]). Esta equivalencia es **mi inferencia**, ninguna fuente la formula.

**costo-y-latencia**
- Latencia: TTFT = "The time it takes for the first token to be generated"; TPOT = "The time it takes to generate each output token" (https://huyenchip.com/2024/07/25/genai-platform.html, sección Observability [L]).
- Costo: "Cost-related metrics are the number of queries and the volume of input and output tokens"; "Length-related metrics are also important for tracking latency and costs" (misma URL [L]).
- El gateway sirve de control: "A model gateway is access control and cost management" (misma URL [L]); caching de prompt/exacto/semántico se agrega para latencia (Step 4, misma URL [L]).
- Charla de Huyen (secundaria): optimizar en tres ángulos (hardware, modelo, servicio); al evaluar un servicio mirar costo, latencia **y calidad**; "The first generated token might not be the same as the first visible token" en modelos de razonamiento (https://thenewstack.io/pg-99-conf-2026-inference-costs/ [S]).
- Cap. 9 de *AI Engineering*: **no verificado** (403 y la página del autor no lista capítulos). No cito afirmaciones del capítulo.

### 1.3 Recursos canónicos

- caracteristicas-arquitectonicas: Richards y Ford 2ª ed., caps. "Architectural Characteristics Defined" e "Identifying Architectural Characteristics" (cap. 4 y 5 según numeración del buscador; confirmar). Fijarse en: los criterios de qué es una característica, el límite de elegir pocas (se contradicen entre sí), y la primera ley. Pendiente de lectura.
- fitness-function: *Building Evolutionary Architectures* 2ª ed., cap. 2 "Fitness Functions" + el podcast de Thoughtworks como acceso gratuito. Fijarse en: objetividad del resultado, atómica vs. holística, disparada vs. continua.
- costo-y-latencia: Huyen, genai-platform post (sección Observability) como acceso verificable; cap. 9 del libro como canónico declarado pero sin leer.

## 2. Modularidad/

### 2.1 Tabla de fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Ousterhout, *A Philosophy of Software Design* 2ª ed. (jul 2021) | https://web.stanford.edu/~ouster/cgi-bin/book.php | Primaria | 3 | 3 | 2 | 3 | [M] (página del autor; no define deep modules) |
| Ousterhout, charla "A Philosophy of Software Design", Talks at Google | https://www.youtube.com/watch?v=bmSAYlu0NcY | Primaria | 3 | 2 | 2 | 2 | [M] (solo título; no se vio el video; fecha no confirmada) |
| connascence.io | https://connascence.io/ | Secundaria (sitio sin autor nombrado; la taxonomía es de Meilir Page-Jones, dato mío, no verificado en esta ronda) | 2 | 2 | 2 | 2 | [L] |
| Richards y Ford, cap. "Modularity" y "Component-Based Thinking" | https://nealford.com/books/SAF2e.html | Primaria | 3 | 3 | 3 | 3 | [M] (solo títulos) |
| Huyen, genai-platform (gateway, orquestación) | https://huyenchip.com/2024/07/25/genai-platform.html | Primaria | 3 | 2 | 2 | 3 | [L] |
| Subramaniam, "Emerging Patterns in Building GenAI Products", martinfowler.com (25 feb 2025) | https://martinfowler.com/articles/gen-ai-patterns/ | Primaria (Thoughtworks/Fowler) | 3 | 2 | 2 | 2 | [L] |
| Anthropic, "Building effective agents" (19 dic 2024) | https://www.anthropic.com/engineering/building-effective-agents | Secundaria (blog de laboratorio) | 2 | 2 | 3 | 2 | [L] |

### 2.2 Afirmaciones

**modularidad**
- Connascence: "a software quality metric & a taxonomy for different types of coupling". Estáticas: Name, Type, Meaning, Position, Algorithm. Dinámicas: Execution, Timing, Value, Identity (https://connascence.io/ [L]).
- Propiedades: Strength ("Stronger connascences are harder to discover, or harder to refactor"), Locality ("Connascent elements that are close together in a codebase are better than ones that are far apart"), Degree (https://connascence.io/ [L]).
- Deep modules: Ousterhout, cap. 4 "Modules Should Be Deep" y cap. 6 "General-Purpose Modules are Deeper" (el segundo reescrito en la 2ª ed.). La página del autor confirma el título del cap. 6 y la edición, no la definición (https://web.stanford.edu/~ouster/cgi-bin/book.php [L]). La definición "mucha funcionalidad detrás de una interfaz simple" viene de resúmenes secundarios (sive.rs, Pragmatic Engineer; todos parafrasean el libro = una fuente) [S]. **Discrepancia señalada**: un crítico dice que las clases profundas son difíciles de testear (Medium, "depth of module", https://medium.com/@nakabonne/depth-of-module-f62dac3c2fdb [S]); relevante para la tensión "profundo vs. aislable y testeable" de aislar-lo-no-determinista.
- 2ª ed. de Ousterhout: nuevo capítulo "Decide What Matters" y subsecciones que lo comparan con *Clean Code* sobre largo de métodos y comentarios (página del autor [L]).

**aislar-lo-no-determinista**
- Huyen: "A model gateway is an intermediate layer that allows your organization to interface with different models"; "If a model API changes, you only need to update the model gateway"; ante caída, el gateway "can route requests to alternative models" (fallback) (https://huyenchip.com/2024/07/25/genai-platform.html [L]).
- Fowler/Subramaniam: "With LLM-based systems, we encounter a system that no longer behaves deterministically"; "Such a system will provide different outputs to the same inputs on repeated requests"; evals se tratan "similarly to how we work with performance testing"; guardrails: "Guardrails act to shield the LLM…" y "guardrails don't come for free" (https://martinfowler.com/articles/gen-ai-patterns/ [L]). Ojo: el artículo trata de evals y guardrails; **no lo vi decir** "ponelo detrás de una interfaz reemplazable" (la página cubre pocos patrones; puede haber más texto que el extractor omitió).
- Anthropic: los frameworks "often create extra layers of abstraction that can obscure the underlying prompts and responses"; recomienda "Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing" y "Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts" (https://www.anthropic.com/engineering/building-effective-agents [L]).
- **Tensión entre fuentes (dar las dos)**: Huyen aconseja una capa (gateway) que oculte proveedores; Huyen y Anthropic advierten contra abstracciones que ocultan el comportamiento ("Abstract away critical details, making it hard to understand and debug your system", https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html [L]). Se concilia distinguiendo interfaz propia chica y transparente (gateway/adaptador) de framework opaco, pero eso es inferencia mía.
- Huyen sobre orquestadores: "start building your application without one first" (genai-platform [L]).

### 2.3 Recursos canónicos

- modularidad: Richards y Ford, cap. "Modularity" (acoplamiento, cohesión, connascence; pendiente de lectura) más Ousterhout cap. 4 para deep modules. Fijarse en: profundidad = funcionalidad / tamaño de interfaz; connascence por fuerza, localidad y grado.
- aislar-lo-no-determinista: Huyen, genai-platform, sección Gateway (único con cita verificada de la interfaz reemplazable), complementado por Fowler/Subramaniam (Evals) para "cómo se prueba". Fijarse en: qué logra el gateway (swap, fallback, costo) y en que evals tienen umbrales, no pass/fail. **No existe un recurso canónico que lo nombre como principio**: hueco real.

## 3. Decisiones/

### 3.1 Tabla de fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Nygard, "Documenting Architecture Decisions" (15 nov 2011) | https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions | Primaria | 3 | 2 | 2 | 3 | [L] |
| adr.github.io | https://adr.github.io/ | Primaria (comunidad ADR) | 3 | 2 | 1 | 2 | [L] |
| MADR 4.0.0 | https://adr.github.io/madr/ | Primaria | 3 | 2 | 2 | 3 | [L] |
| Richards y Ford, caps. "Architectural Decisions", "Analyzing Architecture Risk", "Diagramming Architecture" | https://nealford.com/books/SAF2e.html | Primaria | 3 | 3 | 3 | 3 | [M] (solo títulos) |
| Risk storming (Simon Brown; resumen en el cap. de R&F) | https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/ch20.html (1ª ed.) | Primaria | 3 | 3 | 2 | 3 | [S] (403; vía buscador y espejo) |
| Resúmenes de risk storming (icepanel.io, ensono.com, study-notes) | https://icepanel.io/blog/risk-storming | Secundaria (parafrasean la misma fuente = una) | 1 | 1 | 1 | 1 | [S] |
| c4model.com (Simon Brown) | https://c4model.com/ ; https://c4model.com/abstractions | Primaria | 3 | 2 | 2 | 3 | [L] |
| Huyen, "Common pitfalls when building generative AI applications" (16 ene 2025) | https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html | Primaria | 3 | 2 | 2 | 3 | [L] |
| Anthropic, "Building effective agents" | https://www.anthropic.com/engineering/building-effective-agents | Secundaria | 2 | 2 | 3 | 2 | [L] |
| Gall, *Systemantics* (1975 como *General Systemantics*; 1977 retitulado) | https://en.wikipedia.org/wiki/John_Gall_(author) | Libro; lo leído es secundaria (Wikipedia) | 2 | 1 | 1 | 2 | [S] |

### 3.2 Afirmaciones

**adr**
- Nygard (15 nov 2011): partes Title, Context, Decision, Status, Consequences; "The whole document should be one or two pages long"; "ADRs will be numbered sequentially and monotonically"; "An architecture decision record is a short text file" (https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions [L]).
- adr.github.io define una decisión arquitectónica como "a justified design choice that addresses a functional or non-functional requirement"; el conjunto de ADRs forma el "decision log"; atribuye a Nygard 2011 haber popularizado el concepto; menciona el formato Y-statement (Zdun et al.) y una comparación de siete plantillas en WICSA 2015 (https://adr.github.io/ [L]).
- MADR ("Markdown Architectural Decision Records", pronunciado "matter"), versión 4.0.0 del 2024-09-17. Secciones: Context and Problem Statement (obligatoria), Decision Drivers, Considered Options (obligatoria), Decision Outcome (obligatoria, con Consequences y Confirmation opcionales), Pros and Cons of the Options, More Information; front matter opcional con status, date, decision-makers, consulted, informed (https://adr.github.io/madr/ [L]).
- Diferencia a señalar al lector: Nygard no pide opciones consideradas; MADR sí. Mark Richards, según adr.github.io, también parte de la plantilla de Nygard (https://adr.github.io/ [L]).
- El cap. "Architectural Decisions" de R&F existe (nealford.com [L]); su contenido (p. ej. "anti-patterns" de decisión, ADRs) **no se leyó**: hueco.

**empezar-simple**
- Anthropic: "we recommend finding the simplest solution possible, and only increasing complexity when needed"; "Maintain simplicity in your agent's design" (https://www.anthropic.com/engineering/building-effective-agents [L]).
- Huyen, pitfalls: "Starting too complex" con ejemplos "Use an agentic framework when direct API calls work" e "Insist on finetuning when prompting works"; "Not everything is a nail"; "The journey from 0 to 60 is easy, whereas progressing from 60 to 100 becomes exceedingly challenging"; "It's easy to build a demo, but hard to build a product"; sobre evaluación: "While AI judges can be very useful, they aren't deterministic" y "staring at data for just 15 minutes usually gives me some insight…" (https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html [L]).
- Huyen en genai-platform: arrancar con "query, model, response" y "progressively add more components" con evaluación en cada paso (https://huyenchip.com/2024/07/25/genai-platform.html [L]). Esto es literalmente la regla "una pieza se suma cuando la medición la pide".
- Gall: "a complex system that works is invariably found to have evolved from a simple system that worked" y un sistema complejo hecho de cero "doesn't work and can't be patched into working" (parafraseado por https://en.wikipedia.org/wiki/John_Gall_(author) [S]; cita literal original **no verificada**).
- YAGNI: **no busqué fuente primaria** (Fowler tiene un artículo; hueco declarado).

**analisis-de-riesgo**
- Risk storming: la 1ª ed. lo cubre en el cap. 20 "Analyzing Architecture Risk", la 2ª en el cap. 22 (buscador: https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ch22.html [S]). Se atribuye a Simon Brown (*Software Architecture for Developers*) [S]. Fases: identificación individual (sin influir entre participantes), consenso, mitigación, sobre un diagrama de arquitectura [S, un espejo del cap. 20].
- Matriz de riesgo (impacto x probabilidad): confirmado solo que el capítulo la incluye junto con risk storming [S]; **escala, puntajes y colores del libro no verificados**.

**diagramas**
- C4: cuatro niveles (system context, containers, components, code) y diagramas suplementarios (system landscape, dynamic, deployment); "easy to learn, developer friendly approach to software architecture diagramming" (https://c4model.com/ [L]).
- Abstracciones: "A software system is made up of one or more containers (applications and data stores)"; cada container "contains one or more components"; los componentes se "implemented by one or more code elements". "Container" no es Docker (https://c4model.com/abstractions [L]).
- R&F tienen un capítulo propio "Diagramming Architecture" (nealford.com [L]); su relación con C4 **no verificada**.

### 3.3 Recursos canónicos

- adr: Nygard 2011 (corto, gratis, se lee en 5 minutos) + MADR 4.0.0 como plantilla actual. Fijarse en: Context/Decision/Consequences, "one or two pages", numeración, y que se guarda en el repo.
- empezar-simple: Huyen, "Common pitfalls" ("Starting too complex") + Anthropic, "Building effective agents" (sección sobre simplicidad). Fijarse en: casos concretos de cuándo no usar agente/framework/finetuning.
- analisis-de-riesgo: R&F cap. "Analyzing Architecture Risk" (2ª ed. cap. 22, **sin leer**). Fijarse en: matriz y risk storming. Sin acceso: usar la descripción de Simon Brown como alternativa.
- diagramas: c4model.com (abstractions y los cuatro niveles), más el cap. "Diagramming Architecture" de R&F.

## 4. Huecos declarados

1. **Ningún libro leído.** O'Reilly bloqueó (403) en 8 URLs. Faltan: criterios de característica, trade-offs, la matriz de riesgo, el texto de "Architectural Decisions", y todo el cap. 9 de *AI Engineering* (costo por token, latencia, optimización de inferencia).
2. Definición literal de fitness function en la 2ª ed.: solo la de la 1ª ed. vía buscador [S].
3. Definición de deep module en el libro de Ousterhout: solo secundarias; la charla de Google no se vio (solo título).
4. Fuente que formule "aislar el modelo detrás de una interfaz reemplazable" como principio: solo Huyen (gateway) y la advertencia de Anthropic contra frameworks; el artículo de Fowler no lo dice con esas palabras en lo extraído. Posible hueco del campo o del extractor: revisar el artículo completo a mano.
5. Origen y escalas de la matriz de riesgo y de risk storming: secundarias.
6. YAGNI y cita literal de Gall: sin fuente primaria.
7. Discrepancia interna: la página de Ford dice que la 2ª ed. suma un capítulo de IA generativa, pero su índice no lo lista.
8. Cuántas leyes tiene la 2ª ed. (dos vs. tres): solo secundarias.
9. Costo y latencia desde Anthropic/OpenAI (precios, caching): no se buscó; las cifras cambian y quedarían viejas. Sin números de costo por token en este informe a propósito.
10. El extractor de WebFetch es un modelo chico: las citas "literales" son lo que devolvió; reverificar en la página antes de poner entre comillas en el árbol.
