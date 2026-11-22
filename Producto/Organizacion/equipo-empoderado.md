---
resumen: >-
  Un equipo empoderado recibe un problema para resolver y elige cómo, y se lo juzga por los resultados que mueve; un equipo de funcionalidades recibe una lista priorizada y la entrega. Es la tesis central de la escuela de Cagan, sin estudios que la comparen, y la discuten Shape Up, Scrum y founder mode.
estado: vigente
estabilidad: semi
fuentes:
  - "Marty Cagan, Product vs. Feature Teams (SVPG, 29 de agosto de 2019): https://www.svpg.com/product-vs-feature-teams/"
  - "Marty Cagan, Transformed FAQ (SVPG), según el buscador: https://svpg.com/transformed-faq"
  - "Marty Cagan y Chris Jones, Empowered (Wiley, 2020); Marty Cagan, Transformed (2024), solo listado: https://www.oreilly.com/library/view/empowered/9781119691297/b02.xhtml"
  - "DORA, Team experimentation: https://dora.dev/capabilities/team-experimentation/"
  - "John Cutler, A Cagan Critique: https://cutlefish.substack.com/p/a-cagan-critique"
  - "Jeremiah Lee, Spotify vs Fitbit: Marty Cagan's false premise and false cause fallacy, según el buscador: https://www.jeremiahlee.com/posts/failed-squad-goals/comments/spotify-vs-fitbit/"
  - "Nielsen Norman Group, Teams aren't empowered: https://www.nngroup.com/articles/teams-arent-empowered/"
  - "Lenny's Newsletter, In defense of feature team product managers, según el buscador: https://www.lennysnewsletter.com/p/in-defense-of-feature-team-product"
  - "less.works, On product team and feature team (2019), según el buscador: https://less.works/blog/2019/09/05/on-product-team-and-feature-team"
  - "Paul Graham, Founder Mode (septiembre de 2024): https://paulgraham.com/foundermode.html"
  - "Marty Cagan, Coaching Founder Mode (SVPG): https://svpg.com/coaching-founder-mode"
  - "Skift, Airbnb CEO Brian Chesky: I Never Called it Founder Mode (2024-09-21), según el buscador: https://skift.com/2024/09/21/airbnb-ceo-brian-chesky-i-never-called-it-founder-mode/"
  - "Ryan Singer, Shape Up (Basecamp), cap. 1: https://basecamp.com/shapeup/0.3-chapter-01"
  - "Scrum.org, Product team empowerment anti-patterns, según el buscador: https://www.scrum.org/resources/blog/product-team-empowerment-anti-patterns"
  - "Producto/.investigacion/organizacion-y-fundamentos.md"
  - "Producto/.investigacion/estrategia.md"
  - "Producto/.investigacion/posicion-contraria.md"
aliases: [empowered team, empowered product team, equipo de producto, equipo de funcionalidades, feature team, delivery team, equipo de entrega]
creado: 2026-11-22
revisado: 2026-11-22
---

# Equipo empoderado

Un equipo empoderado recibe un problema para resolver y elige cómo, y se lo juzga por los resultados que mueve; un equipo de funcionalidades recibe una lista priorizada y la entrega. Es la tesis central de la escuela de Cagan, sin estudios que la comparen, y la discuten Shape Up, Scrum y founder mode.

Cagan lo llama product team, equipo de producto; esta base usa "equipo empoderado" para no confundirlo con cualquier equipo que trabaje en un producto. Es parte de la vertical [Organización](organizacion.md), y depende de que la [estrategia](../Estrategia/estrategia-de-producto.md) baje como problemas y no como funcionalidades.

## Tres tipos de equipo según Cagan

Cagan distingue tres tipos de "product teams" y dice que el más común no es uno de producto: "The most common in terms of sheer numbers are not really product teams at all, they are delivery teams" (cita vía buscador). El artículo (leído por extracto) desarrolla la diferencia entre los otros dos.

| Tipo | Qué recibe | Por qué se lo juzga | Qué hace el product manager |
|---|---|---|---|
| Equipo de entrega | Trabajo de ejecución | No quedó registrado | No quedó registrado (el equipo no decide sobre el valor, según el buscador) |
| Equipo de funcionalidades | "a prioritized list that is called the roadmap" | Por entregar la lista (con fechas) | "mainly project manager, and partly (unskilled) designer" |
| Equipo empoderado | Un problema para resolver | Por "outcomes (rather than output)" | "explicitly responsible for ensuring value and viability" |

El propósito del equipo empoderado, en palabras de Cagan, es "to solve problems in ways our customers love, yet work for our business". El equipo está "empowered to figure out the best way to solve the problems they've been asked to solve". De los equipos de funcionalidades dice: "Much more often than not, the teams are not empowered at all." La diferencia está en qué se le delega, y se ve en cómo se escriben los [resultados y entregables](../Estrategia/resultados-y-entregables.md).

Según la FAQ de *Transformed*, vista por el buscador, pasar de equipos de funcionalidades a empoderados "you are not adding responsibilities, you are changing responsibilities". Los [roles de producto](roles-de-producto.md) cambian de contenido con el tipo de equipo.

## Lo que mide DORA

La única evidencia con método cerca de esta tesis viene de DORA, el programa de investigación sobre entrega de software. DORA identifica tres componentes de la experimentación de equipo que impulsan el desempeño de entrega. Son la libertad para probar ideas sin aprobación externa, para escribir y revisar especificaciones durante el desarrollo, y para cambiar historias y especificaciones sin aprobación externa.

Eso apoya una parte de la tesis: los equipos con margen para decidir entregan mejor. Pero no dice nada sobre resultados de negocio, que es lo que Cagan afirma. Cómo mide DORA el desempeño de entrega está en [métricas DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md), del tema DevOps. Una cifra que circula, "95% de las empresas con PMs tienen equipos de funcionalidades", sale de un foro anónimo y no es una medición.

> [!IMPORTANT]
> No hay estudios con método que muestren que los equipos empoderados rindan más que los de funcionalidades. Las críticas también son opinión, pero apuntan a fallas concretas del argumento:
> - Causa falsa y casos ganadores: Jeremiah Lee acusa a Cagan de comparar casos exitosos con fracasos y atribuir la diferencia al modelo (según el buscador). Cutler dice que ignorar los contrafactuales es "like learning only from customers who succeed with a product while ignoring those who churn", y agrega que "the views of a small group of people in tech are having a massively disproportionate impact on our lives".
> - Escala y dependencias: NN/g sostiene que, en organizaciones grandes, los equipos "empoderados" suelen decidir cosas que "don't matter very much", por componentes compartidos y dependencias, y que "nobody was empowered to maintain coherence across the whole experience". La página no tiene datos: sus números son ejemplos hipotéticos.
> - La dicotomía: Lenny's Newsletter defiende que los product managers de equipos de funcionalidades también hacen producto, y less.works cuestiona que la división sea binaria (las dos según el buscador).

## Shape Up y Scrum: otras formas de repartir la decisión

Shape Up, el método de Basecamp, reparte la decisión de otra manera. Un grupo chico moldea el trabajo y lo apuesta en una "betting table"; el equipo recibe el trabajo moldeado y "full responsibility" para definir las tareas en un ciclo de seis semanas. El equipo tiene libertad de implementación pero no elige el problema. El método está en [Shape Up](../Planificacion-y-entrega/shape-up.md).

Scrum pone la decisión en una persona: el Product Owner ordena el backlog y responde por el valor. El equipo decide cómo construir lo que está arriba de la lista (lectura de la base: los informes no lo traen del Scrum Guide). Ninguno de los dos modelos tiene un estudio que lo compare con el de Cagan.

## Founder mode: el fundador en los detalles

La disputa más reciente viene del lado opuesto: la del fundador que decide los detalles. Paul Graham, en "Founder Mode" (septiembre de 2024), sostiene que "there are two different ways to run a company: founder mode and manager mode". El modo gerente trata las partes del organigrama como unidades selladas; el modo fundador rompe la regla de que el CEO solo trata con sus reportes directos. Graham advierte que el consejo "Hire good people and give them room to do their jobs" puede terminar en "hire professional fakers and let them drive the company into the ground". Cita a Brian Chesky y el retiro anual de Steve Jobs con las 100 personas más importantes de Apple.

> [!IMPORTANT]
> Founder mode y equipo empoderado tienen la misma calidad de evidencia, que es ninguna. Graham escribe un ensayo basado en una charla y en anécdotas, y admite que founder mode "is not yet well understood". Cagan respondió en "Coaching Founder Mode" que founder mode "does not mean hands-off delegation, but it also does not mean micro-managing", que "Many people confuse delegation with empowerment" y que "empowered organizations don't require less management, they require better management". Chesky, según la prensa, dijo que él no lo llamó así y que no hace falta ser fundador para tenerlo; en 2025 dijo que gestiona él mismo hasta unos 50 reportes directos. No se encontró ningún estudio que compare fundadores que deciden los detalles con equipos que reciben problemas.

## Cuándo la tesis aplica peor

Las críticas y los informes permiten armar tres condiciones (lectura de la base). Con muchas dependencias entre equipos, el margen real de cada uno se achica (NN/g). En una consultora de software, el equipo suele recibir un alcance contratado y no un problema; las fuentes del caso están en [qué cambia en una consultora](../Fundamentos/que-es-producto.md#que-cambia-en-una-consultora-que-vende-proyectos). Y cuando se adopta el vocabulario sin la capacidad, las decisiones no cambian: Scrum.org lo llama teatro (según el buscador).

La forma de los equipos dentro de una organización de software, alineados a un flujo de trabajo, está en [stream-aligned team](../../Platform-Engineering/Organizacion-de-equipos/stream-aligned-team.md), del tema Platform Engineering.

## Qué leer

Cagan, "Product vs. Feature Teams", por la comparación de responsabilidades y las dos citas sobre el rol del product manager. DORA, "Team experimentation", para la evidencia que existe. Como contraste, Graham, "Founder Mode", corto y para leer entero, aunque es una tesis sin datos. Y Cutler, "A Cagan Critique", por el argumento de los contrafactuales.
