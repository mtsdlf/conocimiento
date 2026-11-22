---
resumen: >-
  Shape Up es el método de Basecamp para decidir y construir: en lugar de un backlog, se apuesta cada seis semanas a proyectos ya acotados, con el tiempo fijo y el alcance variable. Es una alternativa al backlog y al roadmap, y sus propios autores dicen que depende de la escala.
estado: vigente
estabilidad: semi
fuentes:
  - "Ryan Singer, Shape Up (Basecamp), introducción: https://basecamp.com/shapeup/0.3-chapter-01"
  - "Ryan Singer, Shape Up, cap. 2 y glosario: https://basecamp.com/shapeup/1.1-chapter-02"
  - "Ryan Singer, Shape Up, cap. 7 (Bets, Not Backlogs) y cap. 8 (The Betting Table): https://basecamp.com/shapeup/2.2-chapter-08"
  - "Ryan Singer, Shape Up, apéndice 2: https://basecamp.com/shapeup/4.1-appendix-02"
  - "Mind the Product, 7 lessons from trialling Basecamp's Shape Up (según resumen del buscador): https://www.mindtheproduct.com/7-lessons-from-trialling-basecamps-shape-up-methodology/"
  - "Trustpair, Why the ShapeUp method just wasn't for us (según resumen del buscador): https://jobs.trustpair.com/posts/why-the-shapeup-method-just-wasn-t-for-us"
  - "Reseñas de John Cutler y Alex De Becker (según resumen del buscador): https://medium.com/@johnpcutler/review-notes-shape-up-2c2bde31fc8a ; https://alexdebecker.substack.com/p/concerns-before-implementing-shape"
  - "Producto/.investigacion/planificacion-y-entrega.md"
  - "Producto/.investigacion/posicion-contraria.md"
aliases: [Shape Up, apuestas de seis semanas, betting table]
creado: 2026-11-22
revisado: 2026-11-22
---

# Shape Up

Shape Up es el método de Basecamp para decidir y construir: en lugar de un backlog, se apuesta cada seis semanas a proyectos ya acotados, con el tiempo fijo y el alcance variable. Es una alternativa al backlog y al roadmap, y sus propios autores dicen que depende de la escala.

Ryan Singer lo escribió y Basecamp lo publica libre en su sitio. Contesta la misma pregunta que la [priorización](priorizacion.md) y el [roadmap](roadmap.md), "qué hacemos y en qué orden", pero sin puntajes ni horizonte largo. Las tres respuestas están comparadas en [Planificación y entrega](planificacion-y-entrega.md).

## Apetito en lugar de estimación

La idea que sostiene el método es el apetito: "The amount of time we want to spend on a project, as opposed to an estimate." Una estimación pregunta cuánto va a tardar algo ya definido. El apetito invierte la pregunta: primero se decide cuánto tiempo vale el problema, y después se diseña una solución que entre en ese tiempo (lectura de esta base de la definición).

El ciclo dura seis semanas: "Six weeks is long enough to finish something meaningful and short enough to feel the deadline from the beginning." Si un proyecto no termina, no se estira: "If a project runs over, by default it doesn't get an extension". El alcance se recorta para que entre; el tiempo no se mueve.

## Las tres piezas: shaping, apuestas y cool-down

| Pieza | Qué es | Cuándo |
|---|---|---|
| Shaping | Acotar un problema antes de apostar a él; según el informe de esta base, lo hacen una o dos personas. La técnica (breadboard, agujeros, pitch) está en [dar forma a una solución](../Descubrimiento/dar-forma-a-una-solucion.md) | Antes de la apuesta |
| Mesa de apuestas (*betting table*) | "a meeting held during cool-down where stakeholders decide what to do in the next cycle" | Durante el cool-down |
| Cool-down | La pausa entre ciclos: "after each six-week cycle, we schedule two weeks for cool-down" | Dos semanas después de cada ciclo |

El capítulo 7 se titula "Bets, Not Backlogs". Basecamp no mantiene una cola de pedidos: "there's no "grooming" or backlog to organize."

La consecuencia para el roadmap es directa. Shape Up dice "We don't rethink our roadmap every two weeks": compromete un ciclo por vez, no una lista de temas a meses. Es una tercera posición frente al roadmap por fechas y al roadmap por resultados.

## Qué decide y qué deja afuera

Shape Up decide cómo se acota un trabajo y cuándo se apuesta a él. No dice cómo se descubre qué problema vale la pena. El shaping lo hacen una o dos personas antes de la apuesta, no el equipo completo en contacto semanal con clientes. Por eso contrasta con el [descubrimiento continuo](../Descubrimiento/descubrimiento-continuo.md) de la escuela de este tema. Esta lectura es del informe de investigación de esta base, no de una fuente que lo compare.

El contraste también es organizacional: Basecamp funciona sin un product manager dedicado, un caso que está en [empresas sin product manager](../Organizacion/roles-de-producto.md#empresas-sin-product-manager). Cómo se compara Shape Up con el [equipo empoderado](../Organizacion/equipo-empoderado.md#shape-up-y-scrum-otras-formas-de-repartir-la-decision) está en esa nota: el equipo tiene libertad de implementación pero no elige el problema.

## De qué escala depende

El apéndice 2 lo dice así: "The specific practices ... are scale-dependent." Con dos o tres personas, "a tiny team can throw out most of the structure". Al crecer, "all of this fluidity flips from an asset to a liability", y ahí convienen "six-week cycles, cool-downs, and a formal betting table". Basecamp tenía unas 50 personas, una docena de ellas en producto.

> [!IMPORTANT]
> Las críticas a Shape Up son anecdóticas y se leyeron solo en resúmenes del buscador, no en los textos.
>
> En contra: nació en una empresa chica con un solo producto; con equipos tan chicos, una baja cuesta cerca del 20% del tiempo; en una prueba contada por Mind the Product, el equipo se sintió "a tad aimless" después del ciclo y se acumularon pedidos de otras áreas; presta poca atención a investigación y descubrimiento con todo el equipo; una empresa lo dejó al crecer.
>
> A favor: Basecamp lo usa y lo documenta, y el propio libro acota dónde sirve. Ninguna de las dos posiciones tiene un estudio con método.

## Shape Up en una consultora

El apetito es el inverso del presupuesto fijo de un proyecto: en vez de estimar cuánto cuesta un alcance, se fija cuánto se gasta y se ajusta el alcance. Para una consultora que vende proyectos a precio cerrado, eso sugiere vender ciclos con apetito en lugar de alcances con fecha. Es una idea a explorar del informe de investigación, sin fuente que la haya probado. El contexto de los contratos está en [Roadmap](roadmap.md#el-roadmap-cuando-el-cliente-paga-por-fechas-y-alcance).

> [!NOTE]
> Sin fuente todavía: Shape Up usado en equipos de consultora o de agencia, y quién lo usa hoy fuera de Basecamp.

## Qué leer

El libro está libre en basecamp.com/shapeup. Conviene leer primero las partes de apetito, shaping y mesa de apuestas, y después el apéndice 2, sobre adopción. Allí el punto central es que las prácticas dependen de la escala: para un equipo de dos o tres personas, el libro mismo dice que se puede tirar casi toda la estructura.
