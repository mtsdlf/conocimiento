---
resumen: >-
  Las escuelas de arquitectura son las formas de pensar el diseño de un sistema que conviven hoy:
  la clásica de estilos y características, la evolutiva, el diseño guiado por el dominio, el ML de
  producción, el AI engineering centrado en evaluación y la de agentes y harness; cada una pone en
  el centro una cosa distinta.
estado: borrador
estabilidad: semi
fuentes:
  - https://nealford.com/books/SAF2e.html
  - https://research.chalmers.se/publication/247094
  - https://oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch02.html
  - https://www.thoughtworks.com/insights/podcasts/technology-podcasts/rethinking-software-governance-reflecting-second-edition-building-evolutionary-architectures
  - https://pubs.opengroup.org/architecture/o-aa-standard/DDD-strategic-patterns.html
  - https://www.infoq.com/news/2019/09/evans-improve-language-ddd
  - https://arxiv.org/html/2310.01905v4
  - https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
  - https://github.com/chiphuyen/dmls-book
  - https://github.com/chiphuyen/aie-book
  - https://hamel.dev/blog/posts/evals/
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://openai.com/index/harness-engineering/
  - https://lilianweng.github.io/posts/2026-07-04-harness/
  - https://www.latent.space/p/ainews-is-harness-engineering-real
  - https://www.thoughtworks.com/en-us/radar/techniques/summary/
aliases: [escuelas de arquitectura de software, corrientes de arquitectura]
creado: 2026-11-27
revisado:
---

# Escuelas de arquitectura

Las escuelas de arquitectura son las formas de pensar el diseño de un sistema que conviven hoy: la
clásica de estilos y características, la evolutiva, el diseño guiado por el dominio, el ML de
producción, el AI engineering centrado en evaluación y la de agentes y harness; cada una pone en el
centro una cosa distinta.

No son excluyentes: el [tema](../arquitectura.md) combina la clásica con la de AI engineering. Lo que
las separa es qué preguntan primero y qué aceptan como evidencia.

## Las seis escuelas de un vistazo

| Escuela | Pone en el centro | Autores | Evidencia |
|---|---|---|---|
| Clásica de estilos y características | Elegir el estilo por las características que importan | Richards y Ford | Canon de práctica y consultoría |
| Evolutiva | Verificar características con chequeos automáticos | Ford, Parsons y Kua | Práctica, sin estudios |
| DDD | Partir el sistema por el modelo del dominio | Evans, Vernon | Revisión sistemática con estudios de poco rigor |
| ML de producción (MLOps) | El sistema entero alrededor del modelo y sus datos | Sculley et al., Huyen (2022) | Paper revisado por pares y práctica |
| AI engineering centrado en evaluación | Medir antes de sumar piezas | Huyen (2025), Husain | Práctica, sin dato cuantitativo |
| Agentes y harness | El entorno que rodea al modelo | Anthropic, OpenAI, Weng | Informes de los propios laboratorios |

## Clásica: el estilo sale de las características

Richards y Ford (*Fundamentals of Software Architecture*, 2ª ed., 2025) sostienen que el estilo se
elige por las [características](../Caracteristicas/caracteristicas.md) que el sistema tiene que
cumplir y no por moda, y que todo es un trade-off. La segunda edición, que Ford describe como
"basically a rewrite", suma el [monolito modular](../Estilos/monolito-modular.md), IA generativa,
nube y team topologies. Es la escuela de [Estilos](../Estilos/estilos.md) y de
[Decisiones](../Decisiones/decisiones.md). Su punto débil es la evidencia: el estudio de van der Ven y
Bosch encontró respaldo estadístico para pocas creencias de arquitectos.

## Evolutiva: chequear la arquitectura como un test

Ford, Parsons y Kua (*Building Evolutionary Architectures*) ponen en el centro la
[fitness function](../Caracteristicas/fitness-function.md): según resúmenes del capítulo 2 y de un
podcast, un chequeo objetivo de una característica, "somewhat like a unit test for architecture",
específico y automatizable ("ser mantenible" no sirve; "complejidad ciclomática menor a cinco", sí).
La segunda edición pone el énfasis en el gobierno automatizado. Es el antecedente directo de los
[evals](../Evaluacion-y-observabilidad/evaluacion.md) y de los chequeos que se le ponen a un agente.

## DDD: el límite lo pone el dominio

Evans (2003) y Vernon (2013) parten el sistema por el modelo del negocio. Su concepto central, el
*bounded context*, es según el Open Group la "operational definition of where a particular model is
well-defined and applicable", típicamente un subsistema o el trabajo de un equipo. Alimenta la
[modularidad](../Modularidad/modularidad.md) y el corte de
[microservicios](../Estilos/microservicios.md). La revisión sistemática de Özkan et al. reporta
mejoras, pero con estudios de poco rigor; no hay medición rigurosa de su costo-beneficio. Los libros
de Evans y Vernon no se leyeron: lo dicho viene de fuentes secundarias.

## ML de producción: el modelo es lo de menos

Sculley et al. (NIPS 2015) mostraron que el código del modelo es una parte chica de un sistema de ML y
que la velocidad inicial engaña: "it is dangerous to think of these quick wins as coming for free".
Nombraron la deuda propia de esos sistemas: erosión de límites, entrelazamiento, bucles de
retroalimentación ocultos, consumidores no declarados, dependencias de datos y configuración. Huyen
(*Designing Machine Learning Systems*, 2022) lleva eso a mirar el sistema entero, donde datos, features,
reentrenamiento y monitoreo se juzgan por cómo sirven al sistema entero.

## AI engineering centrado en evaluación

Huyen (*AI Engineering*, 2025) parte de modelos fundacionales ya entrenados y pone la evaluación
antes que las técnicas: los capítulos 3 y 4 vienen antes que prompting, RAG y fine-tuning. Según los
resúmenes de capítulo de su repositorio, "Not having a reliable evaluation pipeline is one of the
biggest blockers to AI adoption", y en arquitectura, "Each added component can improve capability,
safety, or speed, but also adds complexity and new failure modes". Husain la respalda desde la
práctica: según él, los productos que fracasan casi siempre comparten la misma causa, no haber armado
un sistema de evaluación sólido. Lo dice sin dato cuantitativo. Es la escuela de
[Sistemas con modelos](../Sistemas-con-modelos/sistemas-con-modelos.md) y de
[Evaluación y observabilidad](../Evaluacion-y-observabilidad/evaluacion-y-observabilidad.md).

## Agentes y harness: diseñar el entorno del modelo

Esta escuela no es de Huyen. Sale de los laboratorios y de investigadoras entre 2025 y 2026. Anthropic
(2025) separa *workflows*, donde el código fija el camino, de agentes que "dynamically direct their
own processes", y pide empezar con llamadas directas. Después vino el *harness*: según Weng
("Harness Engineering for Self-Improvement", 2026), "the system surrounding a base model that
orchestrates execution", es decir, cómo planifica, usa herramientas, administra contexto, guarda
artefactos y evalúa. OpenAI (2026) contó un producto interno de cerca de un millón de líneas sin
código escrito a mano, con un archivo de instrucciones de unas 100 líneas, "a map, not a 1,000-page
instruction manual". Anthropic agrega que cada pieza del harness codifica algo que el modelo no sabe
hacer solo, y que esas piezas envejecen.

Anthropic también define *context engineering* como "the set of strategies for curating and
maintaining the optimal set of tokens (information) during LLM inference", sucesor del prompt
engineering; el Thoughtworks Radar lo tenía en Adopt en abril de 2026. Se cuenta como parte de esta
escuela. Las cifras son de las propias empresas que venden el modelo, sin replicación independiente.
El detalle técnico está en [agente](../Sistemas-con-modelos/agente.md).

## Dónde chocan

> [!IMPORTANT]
> **Harness grande o modelo grande.** Dentro de la escuela de agentes, unos sostienen que el valor
> está en el harness y otros que los modelos de razonamiento lo van a reemplazar; Latent Space
> (marzo de 2026) junta las dos posiciones y advierte que cada bando tiene interés comercial. La
> propia Anthropic dice las dos cosas: diseñá el harness, y quitá lo que el modelo ya hace solo.

- **Clásica contra AI engineering, sobre qué cuenta como evidencia.** La clásica decide por
  trade-offs razonados; AI engineering, por mediciones sobre casos propios. Con un modelo adentro,
  el tema elige la medición, pero ninguna de las dos tiene estudios que la respalden como método.
- **DDD contra microservicios por defecto, sobre dónde va el límite.** Evans advierte que un servicio
  no es siempre un bounded context, y hasta Tilkov, que defiende arrancar con servicios, admite que
  eso funciona mejor si el dominio se entiende bien. La disputa completa está en
  [lo que pierde peso](lo-que-pierde-peso.md).
- **ML de producción contra AI engineering, sobre qué se construye.** La primera entrena y mantiene
  modelos propios; la segunda adapta modelos ajenos. Dónde sigue ganando el modelo propio (datos
  tabulares) también está en [lo que pierde peso](lo-que-pierde-peso.md).
- **Evolutiva y AI engineering coinciden** en verificar con chequeos automáticos; la diferencia es
  que una fitness function pasa o falla, y un eval da una proporción.

> [!NOTE]
> Sin fuente todavía: la arquitectura sociotécnica (team topologies) como escuela propia; solo se
> confirmó que Richards y Ford la incorporan en su segunda edición.

## Qué leer de cada escuela

Para la clásica, Richards y Ford, parte de Estilos y el capítulo de elegir estilo: fijarse en que cada
estilo se juzga por características. Para AI engineering, Huyen, capítulo 4, junto con Husain,
["Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/). Para agentes y harness,
Anthropic,
["Effective harnesses for long-running agents"](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents):
fijarse en la lista de features, una feature por sesión y el traspaso por git. El resto está en la
[bibliografía](bibliografia-de-arquitectura.md).
