---
resumen: >-
  Las escuelas de desarrollo son las formas de organizar el proceso de hacer software que conviven
  hoy: la ágil y sus marcos (XP, Scrum, Kanban, Lean), Shape Up, la ingeniería de software moderna
  con DORA como evidencia, la planificación predictiva, el desarrollo guiado por especificaciones y
  las posturas sobre cómo programar con IA.
estado: vigente
estabilidad: semi
fuentes:
  - https://agilemanifesto.org/
  - https://scrumguides.org/scrum-guide.html
  - https://en.wikipedia.org/wiki/Extreme_programming
  - https://basecamp.com/shapeup/0.3-chapter-01
  - "Dave Farley, Modern Software Engineering (Addison-Wesley, 2021; copyright 2022), índice: https://www.informit.com/store/modern-software-engineering-doing-what-works-to-build-9780137314911"
  - https://en.wikipedia.org/wiki/Accelerate_(book)
  - https://dora.dev/research/2025/dora-report/
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
  - https://en.wikipedia.org/wiki/Waterfall_model
  - https://arxiv.org/html/2510.03894v3
  - https://leanpub.com/read/leprechauns/leanpub-auto-chapter-7-whos-afraid-of-the-big-bad-waterfall
  - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
  - https://www.thoughtworks.com/radar/techniques/spec-driven-development
  - https://en.wikipedia.org/wiki/Vibe_coding
  - https://simonwillison.net/2025/Mar/19/vibe-coding/
  - https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
  - https://code.claude.com/docs/en/best-practices
  - https://unpaywall.org/10.1007%2F978-3-031-78386-9_21
aliases: [escuelas de desarrollo de software, metodologías de desarrollo, corrientes del proceso de desarrollo, ágil vs cascada]
creado: 2026-11-27
revisado: 2026-11-27
---

# Escuelas de desarrollo

Las escuelas de desarrollo son las formas de organizar el proceso de hacer software que conviven hoy: la ágil y sus marcos (XP, Scrum, Kanban, Lean), Shape Up, la ingeniería de software moderna con DORA como evidencia, la planificación predictiva, el desarrollo guiado por especificaciones y las posturas sobre cómo programar con IA.

No son excluyentes ni del mismo tamaño: el Manifiesto Ágil es una declaración de valores, Scrum un marco de trabajo y DORA un programa de investigación. Las separa qué ponen en el centro y qué aceptan como evidencia.

## La escuela de este tema

El [tema](../desarrollo.md) se escribe desde la ingeniería de software moderna de Farley, con las prácticas de XP y la evidencia de DORA: pasos chicos, retroalimentación rápida y la prueba como especificación ejecutable. Se eligió, por criterio de esta base, porque cuenta con datos más allá de la práctica de sus autores (las encuestas de DORA). Además, DORA 2025 encuentra que, sin pruebas automáticas, control de versiones maduro y retroalimentación rápida, más volumen de cambio con IA lleva a inestabilidad. El desarrollo guiado por especificaciones entra como práctica emergente, con su crítica a la vista; la planificación predictiva y el Scrum ceremonial quedan como contraste.

## Las escuelas de un vistazo

| Escuela | Pone en el centro | Autores o fuente | Evidencia |
|---|---|---|---|
| Ágil | Software andando y responder al cambio | Manifiesto, 2001 | Poca, en relación con su popularidad |
| XP | Prácticas técnicas: TDD, integración, refactorización | Beck, 1999 | DORA respalda la entrega en lotes chicos |
| Scrum | Eventos y responsabilidades en ciclos fijos | Scrum Guide 2020 | Escasa en las dos direcciones |
| Kanban y flujo | Limitar el trabajo en curso | DORA (capacidades) | Correlaciones de encuesta |
| Shape Up | Apetito en lugar de estimación, ciclos de seis semanas | Singer, Basecamp | Práctica de una empresa; no se hallaron estudios |
| Ingeniería moderna | Optimizar para aprender y para gestionar la complejidad | Farley, 2021 | Se apoya en DORA |
| DORA como evidencia | Medir entrega y estabilidad | Forsgren, Humble y Kim, 2018 | Encuestas grandes, correlaciones |
| Predictiva o cascada | Un plan completo por fases | Atribuida a Royce, 1970 | Contraste |
| Guiado por especificaciones | La especificación antes del código | Böckeler; Radar | Pocos estudios, ninguno que la respalde |
| Posturas sobre IA | Cuánto se revisa lo que escribe el modelo | Karpathy, Willison, Beck | Textos de practicantes |

## Ágil, XP y Scrum: los valores y los marcos que salieron de ellos

El Manifiesto Ágil (2001, 17 firmantes) prefiere, entre otros valores, "Working software over comprehensive documentation" y "Responding to change over following a plan". Según el resumen de Rytkönen et al. (2024), hay "far less empirical evidence on agile benefits than the method's popularity would suggest". DORA respalda prácticas concretas, como entregar en lotes chicos, más que la etiqueta.

XP nació en el proyecto C3 de Chrysler, que Beck lideró desde 1996; *Extreme Programming Explained* salió en 1999 y su segunda edición, con Cynthia Andres, en 2004. Sus prácticas técnicas ([TDD](../Verificacion/tdd.md), de evidencia nula o mixta; integración continua; [refactorización](../Evolucion/refactorizar.md); entregas chicas) son la base de la escuela de este tema y viven en [Verificación](../Verificacion/verificacion.md), [Evolución](../Evolucion/evolucion.md) e [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md).

La Scrum Guide 2020 define Scrum como "a lightweight framework", con cinco eventos (Sprint, Sprint Planning, Daily Scrum, Sprint Review y Sprint Retrospective) y tres responsabilidades (Developers, Product Owner y Scrum Master), y se declara "purposefully incomplete". Por qué el Scrum con todas sus ceremonias es acá contraste está en [lo que pierde peso](lo-que-pierde-peso-en-desarrollo.md).

## Kanban, flujo y Lean: limitar lo que está en curso

Entre las capacidades que *Accelerate* asocia con mejor desempeño están el flujo de trabajo visible y los límites al trabajo en curso; el mecanismo está en [flujo de valor](../../DevOps/Cultura-y-medicion/flujo-de-valor.md). Con agentes, si el código sale rápido el cuello pasa a la revisión, y limitar los cambios que esperan revisión es limitar el trabajo en curso (inferencia de esta base).

> [!NOTE] Sin fuente todavía: Anderson sobre Kanban y los Poppendieck sobre Lean, leídos y fechados.

## Shape Up: apetito en lugar de estimación

Shape Up (Singer, Basecamp) trabaja en ciclos de seis semanas, le da forma al trabajo antes de dárselo al equipo y fija el apetito, "The amount of time we want to spend on a project, as opposed to an estimate". El *circuit breaker* cancela por defecto lo que no sale en un ciclo. Al tema le sirve para el ciclo con el cliente: el apetito alimenta la [estimación](../Encargo/estimacion.md) y el corte por defecto, los [cambios de alcance](../Encargo/cambios-de-alcance.md). La escuela entera está en [Shape Up](../../Producto/Planificacion-y-entrega/shape-up.md).

## Ingeniería moderna y DORA: aprender rápido, medido

Farley (*Modern Software Engineering*) organiza el oficio en dos ejes: optimizar para aprender (iterar, buscar retroalimentación, avanzar por incrementos, decidir con evidencia (empirismo) y experimentar) y optimizar para gestionar la complejidad (modularidad, cohesión, separación de responsabilidades, ocultamiento de información, acoplamiento). El primero ordena este tema; el segundo vive en [modularidad](../../Arquitectura/Modularidad/modularidad.md).

*Accelerate* (Forsgren, Humble y Kim, 2018) le dio su evidencia: cuatro métricas de entrega y 24 capacidades, sobre unos 23.000 datos de encuestas. En octubre de 2023 DORA advirtió contra usar las métricas para evaluar equipos individuales; las actuales están en [métricas DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md).

DORA 2025 (casi 5.000 profesionales) encontró una relación positiva entre la adopción de IA y el volumen de entrega (throughput) y el desempeño del producto, y una que "does continue to have a negative relationship with software delivery stability". Su lectura: "AI doesn't fix a team; it amplifies what's already there". Son correlaciones de encuesta.

## La cascada y el malentendido de Royce

La planificación predictiva hace un plan completo por fases y lo ejecuta en una pasada. Se la atribuye a Royce (1970), pero, según una historia de 2025 (arXiv 2510.03894), su artículo criticaba la pasada única para sistemas grandes y recomendaba recorrer el ciclo al menos dos veces, con una primera pasada que "provides an early simulation of the final product". La palabra "waterfall" no aparece en el original; según Wikipedia, su primer uso "may have been" el de Bell y Thayer en 1976, un dato que la misma Wikipedia pide respaldar mejor.

> [!IMPORTANT]
> Qué criticó Royce. Para Wikipedia y una historia de 2025 (arXiv 2510.03894), Royce describió el modelo secuencial para mostrar sus riesgos. Bossavit (*The Leprechauns of Software Engineering*, cap. 7) sostiene que la crítica apunta a la figura sin lazos de retroalimentación, no a la idea de etapas. Según esta base, las dos lecturas coinciden en que no propuso la cascada pura (Bossavit se leyó solo por un resumen). La cita más conocida del artículo no se verificó contra el PDF original.

Planificar la intención por adelantado sigue siendo necesario, y este tema lo hace en el [acuerdo inicial](../Encargo/acuerdo-inicial.md).

## Guiado por especificaciones: la especificación vuelve, con dudas

El desarrollo guiado por especificaciones (spec-driven development) le da al agente, antes del código, una especificación escrita como fuente de verdad. Böckeler (octubre de 2025) lo ordena en tres niveles, y en la práctica casi todas las herramientas son spec-first. Su crítica es de practicante: especificaciones desproporcionadas, tediosas de revisar, y agentes que no siguen todas las instrucciones. El Radar de Thoughtworks lo puso en Assess en noviembre de 2025, y los pocos estudios que hay no la respaldan (Hill, ESEM 2026; Agarwal y otros, preprint). Los niveles, el detalle por herramienta y la evidencia están en [especificación](../Definicion/especificacion.md); el tema toma de ahí la especificación con ejemplos verificables y un flujo proporcional al tamaño del cambio.

## Cuánto se revisa lo que escribe el modelo: las posturas sobre IA

- Vibe coding. Karpathy lo propuso el 2 de febrero de 2025: "fully give in to the vibes, embrace exponentials, and forget that the code even exists" (cita vía Wikipedia). Collins lo eligió palabra del año 2025.
- La definición de Willison. Para Willison (marzo de 2025), vibe coding es "building software with an LLM without reviewing the code it writes", distinto de programar con ayuda de un LLM; él no commitea código que no pueda explicar.
- Augmented coding. Beck (junio de 2025) sigue cuidando el código ("tidy code that works") aunque no lo tipee, y avisa de bucles, funcionalidad no pedida y pruebas borradas o desactivadas.
- Ingeniería con agentes. La documentación de Anthropic pide decirle al agente lo que no puede ver y darle una verificación para correr.

La postura de este tema es la de Beck y Willison: el agente escribe y lo que entrega se acepta con evidencia, como dice [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md). Cuánto acelera un agente está en disputa, como cuenta [agente de código](../Construccion/agente-de-codigo.md).

> [!NOTE] Sin fuente todavía: una comparación con método entre Scrum, Kanban y Shape Up.
