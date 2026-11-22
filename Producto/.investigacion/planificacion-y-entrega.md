# Investigación: Planificación y entrega (priorización, roadmap, Shape Up, lanzamiento)

Fecha: 2026-11-22. Ángulo: planificación y entrega.

Marcas: [L] abrí la página y obtuve pasajes literales (la lectura pasó por un extractor de WebFetch, no vi el texto completo de la página: tratar los "literales" como fragmentos); [M] metadatos o abstract; [S] resumen secundario o del buscador. Puntajes 1 a 3: A autoridad, P profundidad, E ejemplos, U unicidad.

## Hallazgo sobre el árbol

La división del árbol (priorización, roadmap, shape-up, lanzamiento) coincide con cómo lo divide la práctica, con dos ajustes:
- Priorización, roadmap y Shape Up no son tres temas paralelos. Son tres respuestas a la misma pregunta ("qué hacemos y en qué orden"): scoring (RICE/WSJF), lista o tema en el tiempo (roadmap), y apuesta con tiempo fijo (Shape Up). Conviene que `priorizacion` diga qué método sirve para qué y `shape-up` se presente como alternativa a las otras dos.
- `lanzamiento` mezcla dos cosas: la práctica de producto (feature flags, lanzamiento gradual: ingeniería y producto) y el go-to-market (product marketing). En el Pragmatic Framework el lanzamiento vive en la categoría "Go-to-Market", separada de "Focus" (roadmap). Sugerencia: en la nota, solo la parte de producto y el límite.
- Dual-track y Scrum (PO vs PM) no tienen nota propia en el árbol; van como un apartado de límite en `roadmap` o `shape-up`, o en `Organizacion/roles-de-producto`.

## 1. Priorización

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Sean McBride, "RICE: Simple prioritization for product managers" (Intercom, 5-ene-2018) | https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/ | primaria (autor del método) | 3 | 2 | 2 | 3 | [L] |
| SAFe, "Weighted Shortest Job First" | https://framework.scaledagile.com/wsjf/ | primaria (marco) | 2 | 2 | 1 | 2 | [L] |
| Reinertsen, The Principles of Product Development Flow (Celeritas, 2009) vía Scrum.org y Wikipedia | https://www.scrum.org/node/106834 ; https://wikipedia.com/wiki/Cost_of_delay | secundaria | 1 | 1 | 1 | 1 | [S] |
| Kano, Seraku, Takahashi, Tsuji (1984), J. Japanese Society for Quality Control 14(2) | https://www.jstage.jst.go.jp/article/quality/14/2/14_KJ00002952366/_article/-char/en | primaria (abstract) | 3 | 1 | 1 | 3 | [M] |
| Críticas a RICE (DZone, Goitein en Substack) | https://dzone.com/articles/rice-score ; https://michaelgoitein.substack.com/p/why-prioritization-frameworks-are?open=false | secundaria, opinión | 1 | 1 | 1 | 1 | [S] |

### Afirmaciones

- RICE: 5-ene-2018, autor Sean McBride. Alcance se mide en "number of people/events per time period"; impacto: massive 3, high 2, medium 1, low 0.5, minimal 0.25; confianza: high 100%, medium 80%, low 50%, debajo de 50% "total moonshot"; esfuerzo en "person-months". La fórmula aparece solo como imagen, no en texto. https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
- Fecha: el brief dice 2016 para RICE (Sean McBride); la página que abrí está fechada 5-ene-2018. Discrepancia no resuelta: puede ser la fecha de republicación o del uso interno anterior. Citar 2018 para la publicación.
- WSJF: SAFe lo describe como "the relative cost of delay divided by the relative job duration"; insumos: valor para usuario y negocio, criticidad temporal, reducción de riesgo/habilitación de oportunidad, y tamaño del trabajo. Abre con la cita de Reinertsen: "If you only quantify one thing, quantify the Cost of Delay." https://framework.scaledagile.com/wsjf/
- Origen: Reinertsen, 2009; la regla se llama también CD3 (Cost of Delay Divided by Duration) y SAFe la popularizó como WSJF. Fuentes secundarias; no leí el texto del libro. https://www.scrum.org/node/106834 ; https://wikipedia.com/wiki/Cost_of_delay
- Cifra circulante: "~85% de los product managers no conocen su costo de demora" (Wikipedia) o "15% lo conoce" (resumen en SlideShare). Es una cifra de Reinertsen citada de segunda mano, sin método verificado; no usar como dato.
- Kano (1984): el abstract propone reemplazar el reconocimiento unidimensional de la calidad por uno bidimensional y clasifica elementos en atractivos, imprescindibles (must-be) y unidimensionales; probado con encuesta a consumidores sobre televisores y relojes de mesa. Un seguimiento de Koo y Nakajo (2001) halló que la categoría depende del tipo de producto. Wikipedia cita páginas 39-48; J-STAGE dice 147-156 (vale J-STAGE). https://www.jstage.jst.go.jp/article/quality/14/2/14_KJ00002952366/_article/-char/en
- Kano clasifica por efecto en la satisfacción, no es una fórmula de orden; sirve para saber qué fideliza, no qué construir primero. Secundaria. (buscador) https://en.wikipedia.org/wiki/Kano_model
- Críticas: RICE es útil si apoya el juicio y peligroso si lo reemplaza; "scoring theater"; el puntaje convierte desacuerdo en aritmética; el factor Confianza es el reconocimiento de la falsa precisión. Todo opinión de blogs, sin estudio con método. https://dzone.com/articles/rice-score ; https://michaelgoitein.substack.com/p/why-prioritization-frameworks-are?open=false
- Por qué sirve para qué (síntesis mía, a marcar como tal en la nota): RICE ordena ideas de crecimiento o mejora comparables entre sí (mismo producto, métricas de alcance); WSJF/costo de demora sirve cuando el valor depende del tiempo (ventanas de mercado, fechas contractuales, riesgo) y hay trabajo en cola; Kano sirve para clasificar atributos, no para secuenciar.
- ICE y MoSCoW: no los abrí (ver huecos).

### Recurso canónico
McBride, artículo de Intercom: leer la escala de impacto y confianza, y el aviso de que el número es una ayuda. Para costo de demora, Reinertsen cap. 3 (no leído): el recurso primario sigue pendiente.

## 2. Roadmap

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Cagan, "Product Roadmaps" (SVPG, 7-ene-2009) | https://www.svpg.com/product-roadmaps/ | primaria (practicante, escuela) | 2 | 1 | 1 | 2 | [L] |
| Cagan, "The Alternative to Roadmaps" (SVPG, 7-sep-2015) | https://www.svpg.com/the-alternative-to-roadmaps/ | primaria | 2 | 2 | 1 | 3 | [L] |
| Lombardo, McCarthy, Ryan, Connors, Product Roadmaps Relaunched (O'Reilly, oct-2017) | https://www.oreilly.com/library/view/product-roadmaps-relaunched/9781491971710 | primaria (libro; el cap. 1 dio 403) | 2 | 3 | 2 | 3 | [S] |
| Janna Bastow, "I invented the Now-Next-Later roadmap" (ProdPad, 18-oct-2022) | https://www.prodpad.com/blog/invented-now-next-later-roadmap/ | primaria (autora) | 2 | 1 | 1 | 3 | [L] |
| Pragmatic Institute Framework | https://www.pragmaticinstitute.com/framework/ | primaria (marco) | 2 | 1 | 1 | 2 | [L] |

### Afirmaciones

- Cagan 2009: "your job is not to prioritize and document feature requests"; "To lock in specific features at the roadmap level is to effectively skip the most important part of your job"; "these dates are essentially just your hopes and wishes". https://www.svpg.com/product-roadmaps/
- Cagan 2015: los roadmaps típicos son lista priorizada de funcionalidades y "tell the team what to do"; propone visión de producto más objetivos de negocio por equipo, con OKRs; los compromisos de fecha deben ser excepcionales ("high-integrity commitments"). https://www.svpg.com/the-alternative-to-roadmaps/
- Roadmaps Relaunched: subtítulo "How to Set Direction while Embracing Uncertainty"; los autores defienden roadmaps que comuniquen visión, atados a objetivos medibles, con temas como componente central. Solo por resúmenes y el índice. https://www.oreilly.com/library/view/product-roadmaps-relaunched/9781491971710
- Aviso: una página de terceros afirma que el libro cubre Now/Next/Later y que Google y Spotify adoptaron el formato; no lo pude confirmar. No usar. https://harshitsingh.pages.dev/books/product-roadmaps-relaunched/
- Now-Next-Later: Bastow dice "rather than focusing on deadline-based delivery, product teams should stay focused on discovery" y "dropped the dates and drew three columns". Fecha del post: 18-oct-2022; en un comentario ubica el origen en 2012 ("the original version that Simon and I sketched out in 2012", titulado Current/Near Term/Future). https://www.prodpad.com/blog/invented-now-next-later-roadmap/
- Pragmatic: el roadmap es "A product roadmap is a visual plan of the product's direction and priorities over time", con la pregunta "Which outcomes come next, and in what order?". https://www.pragmaticinstitute.com/framework/
- Disputa (a escribir): la escuela de Cagan desconfía del roadmap por los compromisos de fecha; Roadmaps Relaunched y el Pragmatic Framework lo mantienen como herramienta de comunicación orientada a resultados o temas. Las dos coinciden en que una lista de funcionalidades con fechas es la peor forma.
- Roadmap como promesa a clientes (consultora que vende fechas): no encontré fuente con método. Lo que hay es la distinción de Cagan entre roadmap y compromiso de fecha. Hueco para el caso de consultora.

### Recurso canónico
Cagan, "The Alternative to Roadmaps" (2015) para la postura de escuela; Roadmaps Relaunched, caps. de temas y de comunicación a clientes, para la postura práctica. Fijarse en la distinción roadmap vs compromiso.

## 3. Shape Up

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Ryan Singer, Shape Up, cap. 8 (betting table) | https://basecamp.com/shapeup/2.2-chapter-08 | primaria | 3 | 3 | 2 | 3 | [L] |
| Shape Up, glosario/cap. 2 (apetito, ciclos) | https://basecamp.com/shapeup/1.1-chapter-02 | primaria | 3 | 2 | 2 | 3 | [L] |
| Shape Up, apéndice 2 (adopción por tamaño) | https://basecamp.com/shapeup/4.1-appendix-02 | primaria | 3 | 2 | 2 | 3 | [L] |
| Mind the Product, "7 lessons from trialling Basecamp's Shape Up" | https://www.mindtheproduct.com/7-lessons-from-trialling-basecamps-shape-up-methodology/ | secundaria, caso | 1 | 1 | 2 | 2 | [S] |
| Trustpair, "Why the ShapeUp method just wasn't for us" | https://jobs.trustpair.com/posts/why-the-shapeup-method-just-wasn-t-for-us | secundaria, caso | 1 | 1 | 2 | 2 | [S] |
| Reseñas (J. Cutler; A. De Becker) | https://medium.com/@johnpcutler/review-notes-shape-up-2c2bde31fc8a ; https://alexdebecker.substack.com/p/concerns-before-implementing-shape | secundaria | 1 | 1 | 1 | 1 | [S] |

### Afirmaciones

- Cap. 8: "The betting table is a meeting held during cool-down where stakeholders decide what to do in the next cycle."; "after each six-week cycle, we schedule two weeks for cool-down."; "there's no "grooming" or backlog to organize." Cap. 7 se titula "Bets, Not Backlogs." https://basecamp.com/shapeup/2.2-chapter-08
- Seis semanas: "Six weeks is long enough to finish something meaningful and short enough to feel the deadline from the beginning." Apetito: "The amount of time we want to spend on a project, as opposed to an estimate." https://basecamp.com/shapeup/1.1-chapter-02
- Escala: con dos o tres personas "a tiny team can throw out most of the structure"; al crecer, "all of this fluidity flips from an asset to a liability" y ahí conviene "six-week cycles, cool-downs, and a formal betting table". Basecamp: unas 50 personas, una docena en producto. "The specific practices ... are scale-dependent." https://basecamp.com/shapeup/4.1-appendix-02
- Críticas (secundarias, solo buscador): nace en una empresa chica con un solo producto; equipos tan chicos que una baja cuesta cerca de 20% del tiempo; en una prueba, el equipo se sintió "a tad aimless" tras el ciclo y se acumularon pedidos de otras áreas; poca atención a investigación y descubrimiento con todo el equipo; una empresa lo dejó al crecer. Es evidencia anecdótica, no estudios. https://www.mindtheproduct.com/7-lessons-from-trialling-basecamps-shape-up-methodology/ ; https://jobs.trustpair.com/posts/why-the-shapeup-method-just-wasn-t-for-us
- Qué cubre y qué no (síntesis): Shape Up decide cómo acotar y cuándo apostar; no dice cómo descubrir qué problema vale la pena. Por eso contrasta con descubrimiento continuo: el "shaping" lo hace una o dos personas antes de la apuesta. Marcar como lectura mía.
- Encaje con consultora que vende proyectos a precio cerrado: el apetito es la inversa del presupuesto fijo; idea a explorar, sin fuente.

### Recurso canónico
Shape Up (libre en basecamp.com/shapeup): partes sobre apetito, shaping y betting table; después el apéndice 2 sobre adopción. Fijarse en que las prácticas dependen de la escala.

## 4. Lanzamiento

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Pete Hodgson, "Feature Toggles" (martinfowler.com, 9-oct-2017) | https://martinfowler.com/articles/feature-toggles.html | primaria (practicante) | 3 | 3 | 3 | 3 | [L] |
| Pragmatic Institute Framework (Go-to-Market) | https://www.pragmaticinstitute.com/framework/ | primaria | 2 | 1 | 1 | 2 | [L] |
| SVPG, página de product marketing | https://www.svpg.com/product-marketing/ | primaria | 1 | 0 | 0 | 0 | [L], vacía para este tema |

### Afirmaciones

- Feature toggle: "a powerful technique, allowing teams to modify system behavior without changing code". Cuatro tipos: release ("allow incomplete and un-tested codepaths to be shipped to production as latent code"), experiment (A/B), ops, permissioning. https://martinfowler.com/articles/feature-toggles.html
- Canary: encender la funcionalidad para un porcentaje chico (el ejemplo usa cerca del 1% de los usuarios), mirar métricas y ampliar. Se distingue del "Champagne Brunch", que apunta a un grupo específico. https://martinfowler.com/articles/feature-toggles.html
- Pragmatic: "A launch introduces a product or release to the market", en la categoría Go-to-Market (junto con plan de marketing, crecimiento, retención, concientización); "teams, systems, content, support, and measures" deben estar listos. El marco no asigna roles (PM vs PMM). https://www.pragmaticinstitute.com/framework/
- Límite producto/marketing (síntesis): producto decide qué sale, a quién y cómo se despliega y se mide (flags, gradual); marketing, el mensaje, los canales y el posicionamiento. El marco no fija el reparto; la fuente de roles (Organizacion/roles-de-producto) debería sostenerlo. Sin fuente primaria para el reparto.

### Recurso canónico
Hodgson, "Feature Toggles": secciones de categorías de toggles y de canary; fijarse en el costo de mantenerlos (qué toggles son de vida corta).

## 5. Límite: dual-track y Scrum

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| Cagan, "Dual-Track Agile" (SVPG, 17-sep-2012) | https://www.svpg.com/dual-track-agile/ | primaria | 2 | 2 | 1 | 3 | [L] |
| Scrum Guide | https://scrumguides.org/scrum-guide.html | primaria | 3 | 2 | 1 | 3 | [L] |

### Afirmaciones

- Cagan 2012: "The Discovery track is all about quickly generating validated product backlog items" y "the Delivery track is all about generating releasable software". Atribuye el término "Dual-Track Scrum" a Jeff Patton. Cagan después dejó de usar "Dual-track Agile" porque "the phrase made people focus far too much on process, and not enough on the principles" y pasó a decir "Continuous Discovery" y "Continuous Delivery". https://www.svpg.com/dual-track-agile/
- Scrum: "The Product Owner is accountable for maximizing the value of the product resulting from the work of the Scrum Team"; responde por la gestión del Product Backlog y por el Product Goal; los Sprints duran "one month or less". https://scrumguides.org/scrum-guide.html
- Límite (síntesis): Scrum define un rol de dueño del backlog y la entrega; no dice cómo se descubre qué poner. Dual-track agrega el descubrimiento sin cambiar Scrum. Sin fuente que compare PO y PM con método; hueco.

## Huecos

- Reinertsen: no leí el libro; costo de demora, CD3 y la cifra del 85% vienen de resúmenes. Falta fuente primaria.
- ICE (Sean Ellis) y MoSCoW (Dai Clegg, DSDM): no investigados.
- Evidencia con método sobre si los métodos de scoring mejoran decisiones: no encontré estudios, solo opiniones de blogs.
- Kano: solo el abstract; falta cómo se aplica (cuestionario funcional/disfuncional) y críticas con método.
- Roadmaps Relaunched: el texto abrió 403; solo resúmenes. Falta leer los capítulos de temas y de comunicación.
- Roadmap como promesa de fecha a clientes (consultora): sin fuente.
- Shape Up: críticas solo anecdóticas, y no abrí los casos (solo resúmenes del buscador); falta Shape Up en equipos de consultora o agencia, quién lo usa hoy fuera de Basecamp.
- Lanzamiento y product marketing: sin fuente primaria sobre el límite PM/PMM (la página de SVPG no tenía nada; Pragmatic no asigna roles). Candidatos: libro de Lauchengco (no verificado), SVPG sobre product marketing.
- Feature flags como práctica de producto (no solo de ingeniería): solo Hodgson; faltan fuentes de producto sobre lanzamiento gradual con métricas.
- PO vs PM: sin comparación con método.
- Nota: la página de SVPG de product marketing mostró fechas posteriores a 2026-11; son datos de la página, no verificados.
