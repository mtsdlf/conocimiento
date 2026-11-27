---
resumen: >-
  La bibliografía de arquitectura junta los libros y fuentes vivas que sostienen este tema, con qué
  parte leer de cada uno, en qué fijarse y cuánto se verificó de cada uno.
estado: borrador
estabilidad: semi
fuentes:
  - https://nealford.com/books/SAF2e.html
  - https://oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch02.html
  - https://github.com/chiphuyen/dmls-book
  - https://github.com/chiphuyen/aie-book
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
  - https://github.com/johnousterhout/aposd-vs-clean-code
  - https://www.infoq.com/news/2020/05/monolith-decomposition-newman/
  - https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html
  - https://www.thoughtworks.com/en-us/radar/techniques/summary/
  - https://www.thoughtworks.com/radar/archive
  - https://hamel.dev/blog/posts/evals/
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://martinfowler.com/articles/microservices.html
aliases: [bibliografía, qué leer de arquitectura, lecturas de arquitectura]
creado: 2026-11-27
revisado:
---

# Bibliografía de arquitectura

La bibliografía de arquitectura junta los libros y fuentes vivas que sostienen este tema, con qué
parte leer de cada uno, en qué fijarse y cuánto se verificó de cada uno.

La columna de confianza importa: varios libros se conocen solo por su índice o por resúmenes, porque
las fichas de la editorial no se pudieron abrir. Lo que un libro dice y se usa en una nota está
atribuido en esa nota.

## Los libros que ordenan el tema

| Libro | Qué leer | En qué fijarse | Qué se verificó |
|---|---|---|---|
| Richards y Ford, *Fundamentals of Software Architecture*, 2ª ed. (2025) | Foundations, el capítulo de características, la parte de estilos y el capítulo de elegir estilo | Que cada estilo se juzga por características, no por moda; el monolito modular, nuevo en esta edición | El índice en la página del autor |
| Huyen, *AI Engineering* (2025) | Capítulos 3 y 4 (evaluación), 6 (RAG y agentes), 7 (fine-tuning) y 10 (arquitectura y feedback) | El "private leaderboard" propio; cuándo no hacer fine-tuning | El índice y los resúmenes de capítulo del repositorio |
| Ford, Parsons y Kua, *Building Evolutionary Architectures*, 2ª ed. | Capítulo 2, "Fitness Functions" | Que una fitness function sea específica y automatizable | Resúmenes; la fecha de la 2ª edición no se confirmó |
| Huyen, *Designing Machine Learning Systems* (2022) | Capítulos 1, 2 y 11 si no se viene de ML, según el repositorio | El sistema entero por encima del modelo | El repositorio, sin el índice completo |
| Ousterhout, *A Philosophy of Software Design* | Los módulos profundos y el debate con Robert Martin | Interfaz simple sobre implementación rica | El debate, no el libro |
| Newman, *Building Microservices* 2ª ed. y *Monolith to Microservices* | Las charlas que resumen su posición | "Microservices should not be the default choice" (de una charla, no del libro) | Una nota de InfoQ sobre su charla |
| Kleppmann y Riccomini, *Designing Data-Intensive Applications*, 2ª ed. | El libro de referencia para datos y sistemas distribuidos | Ver la discrepancia de fecha abajo | Una nota del autor con poco detalle |

Según Ford, la segunda edición de *Fundamentals* es "basically a rewrite" y pasa de unas 450 a casi
600 páginas; el listado de la editorial que vio el buscador dice 546. Lo que cada libro aporta al tema
se reparte en [Estilos](../Estilos/estilos.md),
[Características](../Caracteristicas/caracteristicas.md),
[Sistemas con modelos](../Sistemas-con-modelos/sistemas-con-modelos.md) y
[Evaluación y observabilidad](../Evaluacion-y-observabilidad/evaluacion-y-observabilidad.md).

> [!IMPORTANT]
> La fecha de la 2ª edición de *Designing Data-Intensive Applications* discrepa entre fuentes: la
> editorial la lista en febrero de 2026, una librería el 27 de febrero, otra el 3 de marzo, y la nota
> del propio Kleppmann (24 de marzo de 2026) habla de marzo. Todas las fechas salvo la de la nota
> vienen del buscador. La nota no lista capítulos ni menciona modelos de lenguaje, así que no se sabe
> qué cambió respecto de la primera edición.

## Papers y ensayos que se leen enteros

| Fuente | Qué leer | En qué fijarse |
|---|---|---|
| Sculley et al., "Hidden Technical Debt in Machine Learning Systems" (NIPS 2015) | Todo, es corto | Las categorías de deuda propia de los sistemas con modelos |
| Lewis y Fowler, "Microservices" | La sección "smart endpoints and dumb pipes" | Por qué la lógica no va en el bus |
| Husain, ["Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/) | Todo | Los tres niveles de [evaluación](../Evaluacion-y-observabilidad/evaluacion.md) |
| Anthropic, ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents) | Todo | Workflow contra agente; sumar complejidad solo si mejora el resultado |

Las fuentes de cada disputa (Tilkov contra Fowler, Grinsztajn contra TabPFN, Zheng contra Yan) se
citan donde se discute cada una: en [lo que pierde peso](lo-que-pierde-peso.md) y en
[IA como juez](../Evaluacion-y-observabilidad/ia-como-juez.md).

## La fuente viva: el Technology Radar

El Thoughtworks Technology Radar se publica dos veces por año: el volumen 30 en abril de 2024 y el 35
en noviembre de 2026. Qué leer: el volumen vigente, sección técnicas, y el historial de anillos de cada
entrada. En qué fijarse: que el anillo exterior hoy se llama Caution (antes Hold), y que el propio
Radar avisa que no revisa sus entradas viejas de forma continua, así que una entrada antigua puede no
reflejar lo que piensan hoy. Cómo se usó en este tema está en
[lo que pierde peso](lo-que-pierde-peso.md).

> [!NOTE]
> Sin fuente todavía: los índices de *Designing Data-Intensive Applications* 2ª ed. y de *Designing
> Machine Learning Systems*; las fechas de edición de Evans (2003), Vernon (2013) y GoF (1994), que no
> se verificaron contra la editorial.
