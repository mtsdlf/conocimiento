---
resumen: >-
  Dar forma a una solución es pasar de una oportunidad elegida a una solución acotada antes de diseñar pantallas: qué elementos tiene, qué recorrido sigue la persona, qué riesgos esconde y qué queda afuera.
estado: vigente
estabilidad: semi
fuentes:
  - "Ryan Singer, Shape Up (las citas de los caps. 2 a 6 se leyeron por extracto, conviene cotejarlas con el libro), cap. 2, Principles of Shaping: https://basecamp.com/shapeup/1.1-chapter-02"
  - "Ryan Singer, Shape Up, cap. 3, Set Boundaries: https://basecamp.com/shapeup/1.2-chapter-03"
  - "Ryan Singer, Shape Up, cap. 4, Find the Elements: https://basecamp.com/shapeup/1.3-chapter-04"
  - "Ryan Singer, Shape Up, cap. 5, Risks and Rabbit Holes: https://basecamp.com/shapeup/1.4-chapter-05"
  - "Ryan Singer, Shape Up, cap. 6, Write the Pitch: https://basecamp.com/shapeup/1.5-chapter-06"
  - "Marty Cagan, Revisiting the Product Spec (SVPG, 12-oct-2006): https://www.svpg.com/revisiting-the-product-spec/"
  - "Marty Cagan, Product Discovery (SVPG, 24-sep-2007): https://www.svpg.com/product-discovery/"
  - "Lenny Rachitsky, My favorite product management templates (Lenny's Newsletter, 4-ago-2020): https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37"
  - "Plantilla Lenny's Product Requirements, copia de Atlassian: https://www.atlassian.com/software/confluence/templates/lennys-product-requirements"
  - "Jeff Patton, The New User Story Backlog is a Map (2008, actualizado 2023): https://www.jpattonassociates.com/the-new-backlog/"
  - "Jeff Patton Associates, User Story Mapping: https://www.jpattonassociates.com/user-story-mapping/"
  - "Jeff Patton, User Story Mapping (O'Reilly, 2014) (no leído)"
  - "Molenaar y Dalpiaz, The Impact of Requirements Artifacts on Efficiency in Agile Development: A Case Study (solo primera página): https://webspace.science.uu.nl/~dalpi001/papers/mole-dalp-25-re.pdf"
  - "Mund, Femmer, Méndez Fernández y Eckhardt, Does Quality of Requirements Specifications matter? (2017, solo abstract): https://arxiv.org/abs/1702.07656"
  - "Producto/.investigacion/dar-forma-a-una-solucion.md"
aliases: [shaping, dar forma, pitch, breadboard, fat marker sketch, PRD, product requirements document, story mapping, user story map]
creado: 2026-11-22
revisado: 2026-11-22
---

# Dar forma a una solución

Dar forma a una solución es pasar de una oportunidad elegida a una solución acotada antes de diseñar pantallas: qué elementos tiene, qué recorrido sigue la persona, qué riesgos esconde y qué queda afuera.

Es el tramo entre el [árbol de oportunidades](arbol-de-oportunidades.md), que termina en tres soluciones candidatas, y la decisión de construir una. Singer lo llama *shaping*; Cagan lo resuelve con un prototipo y Patton con un mapa de historias. Lo que sale de acá se prueba con la [prueba de supuestos](prueba-de-supuestos.md) o se apuesta en [Shape Up](../Planificacion-y-entrega/shape-up.md).

## Rough, solved, bounded: el nivel justo de abstracción

Singer define el shaping como "Make an abstract project idea more concrete by defining key elements of the solution before betting on it." Hay que trabajar "not too vague and not too concrete".

El trabajo con forma es rough ("Work in the shaping stage is rough."), está solved ("shaped work has been thought through.") y está bounded ("It tells the team where to stop."). En el caso del libro, un calendario, el equipo podía construir "about a tenth of what people think of when they say "calendar."": eligió una vista de dos meses de solo lectura y dejó afuera arrastrar y soltar.

Para empezar hacen falta una idea cruda, un [apetito](../Planificacion-y-entrega/shape-up.md#apetito-en-lugar-de-estimacion) y un problema acotado. Acotar es pasar de "What could we build?" a "What's really going wrong?".

Singer sostiene que "Shaping is primarily design work" y que no hace falta programar, pero sí ser "technically literate". Es una posición de escuela: en Cagan y Torres el trío decide junto, como cuenta [equipo empoderado](../Organizacion/equipo-empoderado.md#shape-up-y-scrum-otras-formas-de-repartir-la-decision).

## Breadboard y fat marker sketch: dibujar sin pantallas

El breadboard, tomado de la electrónica, describe la solución con palabras: lugares ("screens, dialogs, or menus"), affordances ("things the user can act on, like buttons and fields") y líneas que muestran cómo cada affordance lleva de un lugar a otro. Sirve para juzgar si la secuencia de acciones sirve al caso de uso.

El fat marker sketch es "a sketch made with such broad strokes that adding detail is difficult or impossible". Se usa cuando el problema central es la disposición en el espacio, que el breadboard no muestra. Su costo, según el libro, es que el equipo se apega a detalles de layout.

Los dos se quedan antes de la [interacción](../../UX/Interaccion/interaccion.md), del tema UX, que decide cómo se usa y se ve cada control. Dar forma decide qué elementos y qué recorrido hay.

## Buscar los agujeros antes de apostar

Un agujero (*rabbit hole*) es "Part of a project that is too unknown, complex, or open-ended to bet on." Singer recorre el caso de uso en cámara lenta y pregunta, por ejemplo, "Does this require new technical work we've never done before?". Cada agujero se parchea con algo más simple o se declara fuera de límites.

A ingeniería no se le pregunta "Is this possible?", porque "everything is possible but nothing is free", sino "is X possible in 6-weeks?". Dar forma nombra los riesgos; la [prueba de supuestos](prueba-de-supuestos.md) los evalúa con actividades chicas (división de esta base).

## El pitch y el PRD corto

El pitch es "A document that presents a shaped project idea for consideration at the betting table." Se publica para leerlo sin reunión, y la decisión se toma en la [mesa de apuestas](../Planificacion-y-entrega/shape-up.md#las-tres-piezas-shaping-apuestas-y-cool-down).

| Ingrediente | Qué lleva, según Singer |
|---|---|
| Problem | "The raw idea, a use case, or something we've seen" que motiva el trabajo |
| Appetite | "How much time we want to spend" y cómo eso limita la solución |
| Solution | "The core elements we came up with" |
| Rabbit holes | Detalles "worth calling out to avoid problems" |
| No-gos | "Anything specifically excluded from the concept" |

El PRD corto es la práctica parecida fuera de Shape Up. La plantilla de Lenny Rachitsky, leída en la copia de Atlassian, tiene seis campos: Description, Problem, Why ("How do we know this is a real problem and worth solving?"), Success ("How do we know if we've solved this problem?"), Audience y What. Rachitsky elogia otras plantillas por "the "Non-Goals" section" y por caber "to one page, at least to start". Es práctica, no un estudio.

Comparación de esta base: los dos coinciden en problema, solución y lo que queda afuera. El PRD suma éxito y audiencia; el pitch, apetito y agujeros.

## El criterio de éxito, escrito antes

El pitch no tiene campo para la métrica: el apetito acota el costo, no el resultado esperado (lectura de esta base). Conviene escribir antes de construir qué métrica se espera mover y cuánto. Torres pide lo mismo antes de cada prueba, como dice [prueba de supuestos](prueba-de-supuestos.md); cómo elegir la métrica está en [medición de producto](../Medicion/medicion-de-producto.md).

> [!IMPORTANT]
> Cuánto detalle hace falta antes de construir es una disputa entre escuelas, sin estudio que la resuelva.
>
> Spec escrita: Cagan escribió en 2006 que "most specs take too long to write, they are seldom read" y que dan "a false indicator" de que todo va bien. El PRD corto responde achicando el documento (lectura de esta base).
>
> Prototipo de alta fidelidad: para Cagan, "there's only one form of spec that can deliver on these requirements, and that is the high-fidelity prototype", porque "can be tested". Afirma que acorta la salida al mercado, sin dato.
>
> Trazo grueso: Singer evita wireframes y maquetas porque "define too much detail too early".
>
> Según esta base, no se contradicen del todo: Singer acota antes de apostar, sin pruebas con usuarios en el libro; Cagan prueba antes de pasar a ingeniería. Sus artículos son de 2006 y 2007, y no se buscó su posición actual.
>
> La única evidencia es de requisitos de software. Un caso de Molenaar y Dalpiaz, con "1,345 USs from nineteen sprints", encontró que tener criterios de aceptación "may be a relevant factor" para terminar a tiempo; son correlaciones, leídas en la primera página. Mund y otros, según su abstract, dicen que importa según "particular project characteristics".

## Story mapping: el recorrido y los cortes de entrega

El mapa de historias de Patton ordena el trabajo según el recorrido de la persona. Una lista plana es, para él, "A bag of context-free mulch."

Arriba va la columna vertebral (*backbone*): "the essential capabilities the system needs to have". Primero va el walking skeleton, término de Alistair Cockburn: "the smallest possible system you could build that would give you end to end functionality". Las entregas se cortan con "horizontal swim lanes for each release", de lado a lado, para no sacar "a car without brakes". Patton lo une al [producto mínimo viable](../../Emprender/Validacion/producto-minimo-viable.md): "we'll need all of them to deliver a minimum viable product".

El mapa decide orden y cortes; cada pedazo se escribe después como [historia de usuario](../../Desarrollo/Especificacion-y-prueba/historia-de-usuario.md), con sus criterios de aceptación. El breadboard y el mapa buscan el sistema mínimo de punta a punta con notaciones distintas; ninguna fuente los compara.

## Lo que no se sabe

No hay estudio con método sobre shaping, pitches, PRD cortos ni story mapping: son prácticas de Basecamp y de Patton, sin eficacia demostrada.

> [!NOTE]
> Sin fuente todavía: cómo dan forma a una solución una consultora o una agencia, donde el alcance suele venir del contrato. Tampoco se leyeron el libro *User Story Mapping* (2014) ni la plantilla original de Rachitsky.

## Qué leer

La parte 1 de [Shape Up](https://basecamp.com/shapeup/1.1-chapter-02), capítulos 2 a 6: fijarse en las tres propiedades, en breadboard contra fat marker sketch y en los ingredientes del pitch. Como contrapeso, Cagan, [Revisiting the Product Spec](https://www.svpg.com/revisiting-the-product-spec/). Para el mapa, Patton, [The New User Story Backlog is a Map](https://www.jpattonassociates.com/the-new-backlog/): backbone, walking skeleton y el corte de lado a lado.
