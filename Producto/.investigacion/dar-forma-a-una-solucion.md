# Dar forma a una solución (componente nuevo de Descubrimiento)

Investigación para ampliar `Producto/Descubrimiento/`. Fecha de lectura: 2026-11-22. Marcas: [L] texto completo abierto, [M] metadatos o abstract, [S] resumen secundario o del buscador. Nota: WebFetch devuelve el texto de la página pasado por un modelo chico; lo que sigue son las citas que devolvió, no una lectura propia línea por línea. Las páginas de Shape Up se marcan [L] porque se abrió el capítulo entero, pero las citas literales provienen de esa extracción.

## Dónde cae en el árbol y qué dice el campo

- El campo no tiene un nombre único para este paso. Singer lo llama *shaping*; Cagan lo trata como parte de "product discovery" (diseño del prototipo y la spec); Torres lo resuelve dentro del árbol (elegir y refinar una solución, pasos 5 a 9; ver `arbol-de-oportunidades.md`); Patton lo llama story mapping y lo ubica antes de la entrega. La división del árbol (descubrimiento = oportunidad + prueba de supuestos) deja un tramo sin cubrir entre "oportunidad elegida" y "solución que se puede apostar": ese tramo es el componente nuevo. Propuesta de nombre: `dar-forma-a-una-solucion.md`, en `Descubrimiento/`.
- Límite con `shape-up.md` (ya escrito): esa nota explica apetito, ciclo de seis semanas, mesa de apuestas y cool-down, y dice que "el shaping lo hacen una o dos personas". La nota nueva toma el shaping como técnica general (límites, elementos, agujeros, documento de una página) que sirve también sin ciclos de seis semanas. Debe enlazar a `shape-up.md` para apetito y apuestas y no volver a explicarlos más que en una línea.
- Límite con `prueba-de-supuestos.md`: esa nota desarma una solución en supuestos y los prueba. Dar forma es lo anterior: producir la solución acotada que se va a probar o apostar. Un buen shaping lista los riesgos ("rabbit holes"); la prueba de supuestos los evalúa con actividades chicas.
- Límite con `arbol-de-oportunidades.md`: el árbol termina en "soluciones" candidatas (tres por oportunidad); dar forma toma una de ellas y la deja acotada.
- Límite con UX (`UX/Interaccion/interaccion.md`): la nota de interacción trata de cómo se usa y se ve (controles, respuesta del sistema, errores). Dar forma decide qué elementos y qué recorrido tiene la solución a nivel producto, antes de pantallas; Singer mismo pone la frontera: el shaping evita "wireframes or high-fidelity mockups" (ver abajo) y deja el diseño visual para después. Cagan, en cambio, quiere un prototipo de alta fidelidad como spec: ahí hay una disputa real (sección 2).
- Límite con `Desarrollo/Especificacion-y-prueba/historia-de-usuario.md`: esa nota ya cubre la plantilla "Como… quiero… para…", las tres C, Gherkin, INVEST, la épica y los criterios de aceptación. La nota nueva no repite eso: story mapping decide el orden y el corte de entregas antes de escribir historias; la historia es el formato en que cada pedazo se escribe después. La nota de historia define una épica como historia grande que se parte; el mapa de Patton es otra manera de ver el mismo material (ver sección 3).

## 1. Shaping (Ryan Singer, Shape Up)

### Fuentes

| Fuente | Tipo | Marca | Autoridad | Profundidad | Ejemplos | Unicidad |
|---|---|---|---|---|---|---|
| Singer, Shape Up cap. 2, "Principles of Shaping": https://basecamp.com/shapeup/1.1-chapter-02 | primaria | [L] | 3 | 3 | 3 | 3 |
| Singer, cap. 3, "Set Boundaries": https://basecamp.com/shapeup/1.2-chapter-03 | primaria | [L] | 3 | 3 | 2 | 3 |
| Singer, cap. 4, "Find the Elements": https://basecamp.com/shapeup/1.3-chapter-04 | primaria | [L] | 3 | 3 | 3 | 3 |
| Singer, cap. 5, "Risks and Rabbit Holes": https://basecamp.com/shapeup/1.4-chapter-05 | primaria | [L] | 3 | 3 | 3 | 3 |
| Singer, cap. 6, "Write the Pitch": https://basecamp.com/shapeup/1.5-chapter-06 | primaria | [L] | 3 | 3 | 2 | 3 |

Nota: es un solo libro de una sola escuela; cuenta como una fuente con cinco capítulos, no como cinco coincidencias independientes.

### Afirmaciones

- Qué es. Glosario: "Make an abstract project idea more concrete by defining key elements of the solution before betting on it." https://basecamp.com/shapeup/1.1-chapter-02
- Nivel de abstracción. "When we shape the work, we need to do it at the right level of abstraction: not too vague and not too concrete." Demasiado concreto: "When design leaders go straight to wireframes or high-fidelity mockups, they define too much detail too early." Demasiado abstracto: "When a project is defined in a few words, nobody knows what it means." https://basecamp.com/shapeup/1.1-chapter-02
- Tres propiedades del trabajo "con forma": rough ("Work in the shaping stage is rough."), solved ("Despite being rough and unfinished, shaped work has been thought through.") y bounded ("Lastly, shaped work indicates what not to do. It tells the team where to stop."). https://basecamp.com/shapeup/1.1-chapter-02
- Quién: "Shaping is primarily design work." y "You don't need to be a programmer to shape, but you need to be technically literate." https://basecamp.com/shapeup/1.1-chapter-02 (Esto es una posición de escuela: en Cagan y Torres el trío decide junto; ver `equipo-empoderado.md`.)
- Caso del libro, "Dot Grid Calendar": "With only six weeks to work with, we could only build about a tenth of what people think of when they say "calendar."" La pregunta pasó a ser "which tenth?"; se eligió una vista de dos meses de solo lectura y se dejó afuera arrastrar y soltar y colores. https://basecamp.com/shapeup/1.1-chapter-02
- Apetito: "You can think of the appetite as a time budget for a standard team size." Principio de "fixed time, variable scope". "Estimates start with a design and end with a number. Appetites start with a number and end with a design." https://basecamp.com/shapeup/1.2-chapter-03
- Acotar el problema: "we flip from asking "What could we build?" to "What's really going wrong?"" https://basecamp.com/shapeup/1.2-chapter-03
- Bolsas de gatos (*grab-bags*): "When someone proposes something like "redesign the Files section," that's a grab-bag, not a project." Señal: la etiqueta "2.0". https://basecamp.com/shapeup/1.2-chapter-03
- Listo para dar forma cuando hay tres cosas: una idea cruda, un apetito y un problema acotado ("we're ready", sección "Boundaries in place"). https://basecamp.com/shapeup/1.2-chapter-03
- Breadboarding (tomado de la electrónica, para diseñar "at the right level of abstraction"): lugares ("things you can navigate to, like screens, dialogs, or menus"), affordances ("things the user can act on, like buttons and fields") y líneas de conexión ("show how the affordances take the user from place to place"). Todo en palabras: "We'll use words for everything instead of pictures." Sirve para "play out an idea and judge if the sequence of actions serves the use case". https://basecamp.com/shapeup/1.3-chapter-04
- Fat marker sketch: "a sketch made with such broad strokes that adding detail is difficult or impossible." Se usa cuando el problema central es la disposición 2D, que el breadboard no ve. Desventaja que admite el libro: la notación restringe menos y el equipo puede apegarse a elementos de layout (por ejemplo una barra lateral) que no son el núcleo. https://basecamp.com/shapeup/1.3-chapter-04
- Agujeros (*rabbit holes*): "Part of a project that is too unknown, complex, or open-ended to bet on." Cómo buscarlos: recorrer el caso de uso en cámara lenta y preguntar "Does this require new technical work we've never done before?" y "Are we assuming a design solution exists that we couldn't come up with ourselves?". Se parchean con una solución más simple o se declaran fuera de límites. https://basecamp.com/shapeup/1.4-chapter-05
- Consulta técnica: "Beware the simple question: "Is this possible?" In software, everything is possible but nothing is free." Reformular: "is X possible in 6-weeks?". "we're really hunting for time bombs that might blow up the project once it's committed to a team." https://basecamp.com/shapeup/1.4-chapter-05
- El pitch: "A document that presents a shaped project idea for consideration at the betting table." Cinco ingredientes: Problem ("The raw idea, a use case, or something we've seen that motivates us to work on this"), Appetite ("How much time we want to spend and how that constrains the solution"), Solution ("The core elements we came up with, presented in a form that's easy for people to immediately understand"), Rabbit holes ("Details about the solution worth calling out to avoid problems") y No-gos ("Anything specifically excluded from the concept"). Se publica para lectura asincrónica y comentarios; la decisión se toma después en la mesa de apuestas. https://basecamp.com/shapeup/1.5-chapter-06
- Aclaración de vocabulario: el capítulo 5 no usa el término "no-gos" (usa "out of bounds"); el término aparece como ingrediente del pitch en el capítulo 6.

### Qué falta en la evidencia
No hay estudio con método sobre shaping. Las críticas y adopciones están en `shape-up.md` y son anecdóticas. El libro describe cómo trabaja Basecamp; no compara con otro método.

### Recurso canónico
Singer, Shape Up, parte 1 completa (caps. 2 a 6), unas 40 páginas. Fijarse en: las tres propiedades (rough, solved, bounded), la diferencia entre breadboard y fat marker sketch, el cap. 5 sobre cómo buscar agujeros y la lista de ingredientes del pitch. Contraponerlo a Cagan (abajo).

## 2. El spec o PRD como alternativa

### Fuentes

| Fuente | Tipo | Marca | Autoridad | Profundidad | Ejemplos | Unicidad |
|---|---|---|---|---|---|---|
| Cagan, "Revisiting the Product Spec", SVPG, 12-oct-2006: https://www.svpg.com/revisiting-the-product-spec/ | primaria (blog del autor, escuela) | [L] | 3 | 3 | 1 | 3 |
| Cagan, "Product Discovery", SVPG, 24-sep-2007: https://www.svpg.com/product-discovery/ | primaria (blog) | [L] | 3 | 2 | 1 | 2 |
| Rachitsky, "My favorite product management templates", Lenny's Newsletter, 4-ago-2020: https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37 | secundaria (newsletter; lista de plantillas ajenas) | [L] | 2 | 1 | 2 | 2 |
| Plantilla "Lenny's Product Requirements" en Atlassian: https://www.atlassian.com/software/confluence/templates/lennys-product-requirements | secundaria (plantilla de un proveedor) | [L] | 1 | 1 | 1 | 2 |
| Lenny's, "How to write a good PRD" y "Examples and templates of 1-pagers and PRDs": https://www.lennysnewsletter.com/p/how-to-write-a-good-prd , https://www.lennysnewsletter.com/p/prds-1-pagers-examples | secundaria | [S] (de pago; no se pudo leer) | | | | |

### Afirmaciones

- Cagan, 2006: el spec está "long overdue for a renovation"; "most specs take too long to write, they are seldom read"; un riesgo es "the mere existence of the spec to serve as a false indicator to management and the product team" de que el proyecto va bien. https://www.svpg.com/revisiting-the-product-spec/
- Cagan pide que la spec describa la experiencia completa, represente con exactitud el comportamiento del software, sirva a ingeniería, QA y marketing, y cambie con las decisiones con una sola versión maestra. Su conclusión: "there's only one form of spec that can deliver on these requirements, and that is the high-fidelity prototype", y rechaza el prototipo en papel "for most products". Ventaja que destaca: "unlike a paper document, a high-fidelity prototype can be tested"; la spec no está lista para ingeniería hasta que el prototipo pasa pruebas de usabilidad y deseabilidad. https://www.svpg.com/revisiting-the-product-spec/
- Cagan afirma que el prototipo "will typically significantly reduce time to market"; es una afirmación sin dato en el artículo. Admite que el prototipo no captura requisitos de release (confiabilidad, rendimiento) ni de plataforma (navegadores soportados), que van en un complemento (wiki o intranet). https://www.svpg.com/revisiting-the-product-spec/
- Cagan, 2007: critica pensar "requirements and design as a sequential, predictable and scheduled phase", y que construir software en lugar de un prototipo es usar a la ingeniería para hacer "a very, very expensive prototype" con clientes reales "as unwitting test subjects". https://www.svpg.com/product-discovery/
- Fechas: ambos artículos son de 2006 y 2007; SVPG puede haber matizado después. No se buscó una posición más reciente (ver huecos).
- Disputa para escribir: Singer (shaping) pide una solución deliberadamente gruesa, en palabras y trazos, y evita wireframes y maquetas de alta fidelidad porque "they define too much detail too early" (https://basecamp.com/shapeup/1.1-chapter-02). Cagan pide el prototipo de más fidelidad posible para poder probarlo con usuarios (https://www.svpg.com/revisiting-the-product-spec/). No se contradicen del todo: Singer acota antes de decidir apostar (sin pruebas con usuarios en el libro), Cagan prueba antes de pasar a ingeniería. Es lectura de esta base de dos fuentes que no se citan entre sí.
- Práctica documentada de PRD corto (marcada como práctica, no como estudio): la plantilla de Lenny Rachitsky, tal como la publica Atlassian, tiene seis campos: Description ("What is it?"), Problem ("What problem is this solving?"), Why ("How do we know this is a real problem and worth solving?"), Success ("How do we know if we've solved this problem?"), Audience ("Who are we building for?") y What ("What does this look like in the product?"). Su guía: "Keep coming back to the problem" y "In every design review, make sure the designers start by reviewing the problem statement." https://www.atlassian.com/software/confluence/templates/lennys-product-requirements
- Rachitsky (2020) recomienda otras plantillas con su razón: la de Kevin Yien (Square) por "the "Non-Goals" section and the step-by-step flow"; la de Asana por "the problem statement framework"; la de Steve Morin "the focus on success criteria and risks"; la de Adam Thomas "how valuable it is to keep these to one page, at least to start". https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37 La plantilla de Yien en sí no se encontró (solo la mención); no describir sus secciones.
- Observación de esta base: las plantillas cortas coinciden con el pitch de Singer en tres ingredientes (problema, solución, qué queda afuera: "Non-Goals" y no-gos) y difieren en que ponen "éxito" y "audiencia" explícitos y no tienen apetito ni agujeros. Es comparación propia, no de una fuente.

### Evidencia sobre especificación liviana vs pesada
No se encontró un estudio que compare especificación liviana y pesada contra el éxito del producto con diseño controlado (búsqueda del buscador; no hay una fuente que lo diga más allá de esa búsqueda). Lo más cercano, a nivel de requisitos de software y no de producto:

| Fuente | Tipo | Marca | Autoridad | Profundidad | Ejemplos | Unicidad |
|---|---|---|---|---|---|---|
| Molenaar y Dalpiaz, "The Impact of Requirements Artifacts on Efficiency in Agile Development: A Case Study" (Utrecht University; el archivo se llama mole-dalp-25-re, año y sede no confirmados): https://webspace.science.uu.nl/~dalpi001/papers/mole-dalp-25-re.pdf | primaria (paper) | [L] solo primera página: abstract e introducción; el resto no se leyó | 2 | 2 | 1 | 3 |
| Mund, Femmer, Méndez Fernández y Eckhardt, "Does Quality of Requirements Specifications matter? Combined Results of Two Empirical Studies", 2017: https://arxiv.org/abs/1702.07656 | primaria (preprint) | [M] | 2 | 2 | 1 | 2 |

- Molenaar y Dalpiaz: caso mixto en una organización grande neerlandesa; "eight agile teams: 1,345 USs from nineteen sprints". Hallazgo: los indicadores de calidad de la historia "do not seem to have an effect on on-time completion", mientras que "the existence of acceptance criteria may be a relevant factor for on-time completion". Y declaran que "empirical evidence on the impact of requirements artifacts on team efficiency is scarce". Es un caso, correlaciones, y mide historias y criterios, no el spec previo a construir. https://webspace.science.uu.nl/~dalpi001/papers/mole-dalp-25-re.pdf
- Mund y otros: la relevancia de la calidad de la especificación "depends both on particular project characteristics" y los dominios críticos para la seguridad dependen más de ella. Se leyó solo el abstract resumido. https://arxiv.org/abs/1702.07656

Declaración: no hay evidencia buena sobre cuánta especificación conviene antes de construir en producto digital; la disputa entre Cagan, Singer y las plantillas es de escuelas.

### Recurso canónico
Cagan, "Revisiting the Product Spec" (corto, una lectura): fijarse en la lista de requisitos de una spec y por qué solo el prototipo los cumple. Para práctica: la plantilla de seis campos de Rachitsky como ejemplo de PRD corto (marcado como práctica).

## 3. Story mapping (Jeff Patton)

### Fuentes

| Fuente | Tipo | Marca | Autoridad | Profundidad | Ejemplos | Unicidad |
|---|---|---|---|---|---|---|
| Patton, "The New User Story Backlog is a Map", 8-oct-2008 (actualizado 12-abr-2023): https://www.jpattonassociates.com/the-new-backlog/ | primaria | [L] | 3 | 2 | 2 | 3 |
| Patton Associates, resumen de presentación de 2008 sobre story mapping: https://www.jpattonassociates.com/user-story-mapping/ | primaria | [L] | 3 | 1 | 1 | 1 |
| Patton, *User Story Mapping*, O'Reilly, 2014 (libro) | primaria | no abierta; solo mencionada en resultados del buscador [S] | 3 | 3 | 3 | 3 |

### Afirmaciones

- Por qué un mapa y no una lista: "Arranging user stories in the order you'll build them doesn't help me explain to others what the system does."; una lista plana es "A bag of context-free mulch."; "I need that context in order for me to really tell a story about the system." https://www.jpattonassociates.com/the-new-backlog/
- Backbone ("columna vertebral"): "I find that the big things on the top of the story map look a little like vertebrae." y "Those big things on the top are often the essential capabilities the system needs to have." Se llama "backbone". https://www.jpattonassociates.com/the-new-backlog/
- Walking skeleton: "describe the smallest possible system you could build that would give you end to end functionality." Patton dice: "This is what Alistair Cockburn refers to as the "walking skeleton"." y "I always try to build this first." https://www.jpattonassociates.com/the-new-backlog/
- Cortes de entrega (release slices): "creating horizontal swim lanes for each release." Los ítems del backbone son esenciales: "These items are essential – and we'll need all of them to deliver a minimum viable product"; "That way we never release a car without brakes." https://www.jpattonassociates.com/the-new-backlog/ (El término "release slices" lo usan fuentes secundarias del buscador; Patton en este texto dice "swim lanes".)
- Origen: Patton Associates dice que el método de planificación se describió por primera vez en el artículo de enero de 2005 de *Better Software* "How you slice it", y que el mapa "arranges user stories into a useful model to help understand the functionality of the system". https://www.jpattonassociates.com/user-story-mapping/
- Lo que no se leyó: el libro de 2014 (estructura de "gran idea", discovery, framing con historias de usuario y personas). Solo hay resúmenes de buscadores (secundarios, no usar como fuente).
- Límite con `historia-de-usuario.md` (leída): esa nota define la historia (Connextra, tres C, Gherkin, INVEST) y la épica como historia "que no es pequeña" y se parte. El mapa suma una dimensión: ordena las historias según el recorrido de la persona (de izquierda a derecha) y por necesidad (de arriba abajo), y decide qué entra en cada entrega. Un criterio de aceptación se escribe después, historia por historia; el mapa no lo reemplaza.
- Límite con shaping: Singer arma el recorrido con breadboards (lugares y affordances); Patton con un mapa de actividades y pasos de la persona. Los dos buscan "el sistema mínimo de punta a punta"; no hay fuente que los compare (comparación de esta base).

### Evidencia sobre story mapping
Casi nula. La búsqueda mostró estudios empíricos sobre Example Mapping (primos de la técnica de refinamiento de historias), con conclusión de que funciona bajo ciertas condiciones, y un experimento de la KU Leuven sobre árbol de justificación vs story mapping cuyo resultado no se leyó; un estudio de 2022 señala que hay poca evidencia de la efectividad de las historias de usuario (todo [S], del buscador, sin URL abierta). Declaración: no hay estudio con método leído sobre story mapping. Sirve como práctica de una autoridad reconocida, no como técnica con eficacia demostrada.

### Recurso canónico
Patton, "The New User Story Backlog is a Map" (artículo corto y libre) como entrada; el libro *User Story Mapping* (2014) para el método completo, que no se leyó. Fijarse en: backbone, walking skeleton y la regla de que se corta de lado a lado y no por pieza.

## 4. Criterio de éxito antes de construir

- Esta base ya lo tiene en dos lados: `prueba-de-supuestos.md` dice que Torres recomienda definir qué resultado cuenta como bueno antes de correr una prueba, y que la lectura es de esta base ("sin ese criterio previo, cualquier resultado se puede leer como éxito"). Aquí solo hay que enlazar.
- Las plantillas cortas lo ponen como campo: "Success: How do we know if we've solved this problem?" (https://www.atlassian.com/software/confluence/templates/lennys-product-requirements) y Rachitsky elogia la plantilla de Steve Morin por "the focus on success criteria and risks" (https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37). El pitch de Singer no tiene un ingrediente de éxito: el apetito acota el costo, pero no hay campo para la métrica. Hueco de Shape Up señalado con el texto de los cinco ingredientes (https://basecamp.com/shapeup/1.5-chapter-06); es lectura de esta base.
- Cagan 2007: antes de comprometer ingeniería hay que "validate the opportunity with your customers" (https://www.svpg.com/product-discovery/).
- Recomendación: la nota nueva solo dice "el criterio de éxito va escrito antes de construir, qué métrica y cuánto se mueve" y enlaza a `Medicion/` (`north-star.md`, `experimento-ab.md`) y a `resultados-y-entregables.md`. No se investigó a fondo, como se pidió.

## Propuesta de estructura de la nota nueva

1. Qué es dar forma: pasar de una oportunidad elegida a una solución acotada (rough, solved, bounded).
2. Tres maneras de hacerlo, comparadas: pitch (Singer), spec corto (plantillas), prototipo (Cagan), mapa (Patton). Con la disputa gruesa/fina y sin fuente que las compare.
3. Los elementos de un pitch y cómo buscar agujeros.
4. Límites: apetito y apuestas en `shape-up.md`; supuestos en `prueba-de-supuestos.md`; historia y criterios en `historia-de-usuario.md`; pantallas en `interaccion.md`; éxito en `Medicion/`.
5. Qué no se sabe (sin estudios).

## Huecos

- No hay estudio con método sobre shaping, pitches, PRDs breves o story mapping; tampoco sobre especificación liviana vs pesada en producto (sí algo de requisitos de software, con correlaciones y casos, ver arriba).
- El libro *User Story Mapping* (2014) y *Inspired* no se abrieron; solo el artículo de 2008 y la nota de Patton Associates. Agile Alliance (glosario de story map) devolvió 404.
- Cagan 2006 y 2007 son viejos; no se buscó su posición actual (p. ej. *Inspired* 2.ª ed., *Empowered*, "Product Requirements"-tipo en SVPG).
- No se encontró la plantilla de Kevin Yien ni los posts de pago de Lenny's; la plantilla de seis campos se leyó en la copia de Atlassian, un proveedor, no en el original.
- El año y el congreso del paper de Molenaar y Dalpiaz no se confirmaron; solo se leyó la primera página.
- Sin fuente sobre shaping o story mapping en consultoras o agencias (los casos de orientación).
- Sin fuente que compare shaping con Torres o con Patton: las comparaciones son de esta base.
- Criterio de éxito previo: sin estudio, no investigado a fondo por pedido.
