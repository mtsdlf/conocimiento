---
resumen: >-
  La bibliografía de desarrollo ordena los libros y las fuentes vivas del tema por lo que se
  necesita hacer (entender el proceso, especificar, probar, mantener código heredado, trabajar con
  agentes y tratar con el cliente) y dice qué parte leer de cada uno y en qué fijarse.
estado: vigente
estabilidad: semi
fuentes:
  - "Dave Farley, Modern Software Engineering (Addison-Wesley, 2021; copyright 2022), índice: https://www.informit.com/store/modern-software-engineering-doing-what-works-to-build-9780137314911"
  - https://en.wikipedia.org/wiki/Accelerate_(book)
  - https://dora.dev/research/2025/dora-report/
  - https://scrumguides.org/scrum-guide.html
  - https://basecamp.com/shapeup/0.3-chapter-01
  - https://basecamp.com/shapeup/1.1-chapter-02
  - https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge
  - https://www.manning.com/books/specification-by-example
  - https://www.mountaingoatsoftware.com/books/user-stories-applied
  - https://cucumber.io/docs/gherkin/reference/
  - https://www.domainlanguage.com/ddd/reference/
  - https://standards.ieee.org/ieee/29148/6937
  - https://martinfowler.com/books/refactoring.html
  - https://martinfowler.com/articles/practical-test-pyramid.html
  - https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
  - https://archive.org/details/working-effectively-with-legacy-code
  - https://code.claude.com/docs/en/best-practices
  - https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
  - https://simonwillison.net/2025/Mar/19/vibe-coding/
  - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
  - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  - https://metr.org/blog/2026-02-24-uplift-update/
  - https://www.martinfowler.com/articles/lean-inception
  - https://www.simula.no/research/review-studies-expert-estimation-software-development-effort
  - https://ieeexplore.ieee.org/document/5232804
aliases: [libros de desarrollo de software, qué leer sobre el proceso de desarrollo, bibliografía de ingeniería de software]
creado: 2026-11-27
revisado: 2026-11-27
---

# Bibliografía de desarrollo

La bibliografía de desarrollo ordena los libros y las fuentes vivas del tema por lo que se necesita hacer (entender el proceso, especificar, probar, mantener código heredado, trabajar con agentes y tratar con el cliente) y dice qué parte leer de cada uno y en qué fijarse.

Casi ningún libro se leyó entero para escribir el tema: de varios se usaron el índice, la página del autor o resúmenes secundarios. Donde no se pudo confirmar el año o la edición, la tabla dice "edición sin verificar". Las fuentes de 2025 y 2026 sobre agentes envejecen rápido y van con fecha.

## Para entender el proceso

| Recurso | Qué leer | En qué fijarse |
|---|---|---|
| Farley, *Modern Software Engineering* (Addison-Wesley, 2021; copyright 2022) | Parte II, "Optimize for Learning" (caps. 4 a 8); la Parte III va con [Arquitectura](../../Arquitectura/arquitectura.md) | Los cinco principios de aprender rápido (iterar, buscar retroalimentación, avanzar por incrementos, decidir con evidencia y experimentar), que ordenan este tema |
| Forsgren, Humble y Kim, *Accelerate* (2018) | Las métricas de entrega y las capacidades | Qué es evidencia y qué es correlación; el aviso de DORA de 2023 contra evaluar equipos con las métricas |
| DORA, informe 2025 | Lo que dice sobre la IA como amplificador y los controles que la acompañan | Que son correlaciones de encuesta |
| Scrum Guide 2020 (gratis) | Entera, es corta | Que se define como marco "purposefully incomplete" |
| Singer, *Shape Up* (gratis, en línea) | Los capítulos de apetito, dar forma y circuit breaker | Cómo se acota el trabajo sin estimarlo |
| SWEBOK v4 (IEEE Computer Society, octubre de 2024) | La lista de las 18 áreas de conocimiento | El vocabulario común del campo; la página oficial no se pudo abrir |

Las escuelas que salen de estas lecturas están en [escuelas de desarrollo](escuelas-de-desarrollo.md).

## Para especificar

| Recurso | Qué leer | En qué fijarse |
|---|---|---|
| Adzic, *Specification by Example* (Manning, 2011) | El ciclo: derivar el alcance de los objetivos, especificar en colaboración, ilustrar con ejemplos, automatizar la validación | Ejemplos concretos como especificación y documentación viva |
| Cohn, *User Stories Applied* (Addison-Wesley, 2004; no leído) | Qué es una buena historia | La historia como inicio de una conversación, no como especificación completa |
| Referencia de Gherkin (Cucumber) | Given, When, Then y `Rule` | Que Then afirme algo observable y que el ejemplo describa comportamiento, no implementación |
| Evans, *Domain-Driven Design* (Addison-Wesley, 2003; no leído) y su DDD Reference (gratis, marzo de 2015) | La parte de lenguaje ubicuo y la de contextos delimitados | El vocabulario del negocio igual en el código |
| ISO/IEC/IEEE 29148:2018 (de pago) | Solo los atributos de un buen requisito | Necesario, no ambiguo, verificable, trazable (lista sin verificar en la norma); no el documento entero como entregable |

Se usan en [especificación](../Definicion/especificacion.md), [criterios de aceptación](../Definicion/criterios-de-aceptacion.md), [historia de usuario](../Definicion/historia-de-usuario.md) y [modelo de dominio](../Definicion/modelo-de-dominio.md).

## Para probar

| Recurso | Qué leer | En qué fijarse |
|---|---|---|
| Beck, *Test-Driven Development by Example* (2002; no leído) | Las primeras dos partes (sin verificar) | El ritmo rojo, verde, refactorizar; la evidencia sobre calidad es mixta |
| "The Practical Test Pyramid" (martinfowler.com) | Entero | Que el propio artículo llama simplista al modelo de la pirámide |
| Böckeler, sobre TDD en el bucle de un agente (martinfowler.com) | Los hallazgos | Agentes que se saltan el paso rojo y pruebas tautológicas |

Se usan en [pirámide de pruebas](../Verificacion/piramide-de-pruebas.md) y [TDD](../Verificacion/tdd.md).

## Para mantener código heredado

| Recurso | Qué leer | En qué fijarse |
|---|---|---|
| Feathers, *Working Effectively with Legacy Code* (2004; no leído) | Las partes de seams y de pruebas de caracterización (capítulos sin verificar) | Su definición: código heredado es código sin pruebas |
| Fowler, *Refactoring*, 2ª ed. (2018) | El capítulo 1 y el de pruebas; el catálogo como vocabulario | Pasos chicos sostenidos por pruebas |
| Ousterhout, *A Philosophy of Software Design* (edición sin verificar) | Lo que indica la [bibliografía de Arquitectura](../../Arquitectura/Fundamentos/bibliografia-de-arquitectura.md) | Módulos profundos como contrapeso a partir el código por reflejo |

Se usan en [sistema heredado](../Evolucion/sistema-heredado.md), [refactorizar](../Evolucion/refactorizar.md) y [deuda técnica](../Evolucion/deuda-tecnica.md).

## Para trabajar con agentes

| Recurso | Qué leer | En qué fijarse |
|---|---|---|
| Documentación de buenas prácticas de un agente de código (Anthropic) | Decirle lo que no puede ver y darle una verificación para correr | Es volátil: fechar lo que se copie |
| Beck, "Augmented Coding: Beyond the Vibes" (junio de 2025) | Entero, es corto | Las señales de que el agente se desvía: bucles, funcionalidad no pedida, pruebas borradas |
| Willison, sobre qué es vibe coding (19 de marzo de 2025) | Entero | La regla de no commitear lo que no se puede explicar |
| Böckeler, "Understanding Spec-Driven-Development" (octubre de 2025) | Los tres niveles y las críticas | Los casos en que el agente ignora la especificación |
| METR, estudio de julio de 2025 y actualización de febrero de 2026 | Las dos juntas, sobre todo las limitaciones | Por qué el 19 % de 2025 ya no se puede citar solo |

Se usan en [agente de código](../Construccion/agente-de-codigo.md), [contexto del repositorio](../Construccion/contexto-del-repositorio.md) y [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md).

## Para tratar con el cliente

| Recurso | Qué leer | En qué fijarse |
|---|---|---|
| Caroli, "Lean Inception" (martinfowler.com) | La agenda de la semana | Que termina en un MVP entendido por todos, no en un documento de requisitos |
| Singer, *Shape Up*, cap. 2, "Principles of Shaping" | Entero | El trabajo moldeado como "rough", "solved" y "bounded": le dice al equipo dónde parar |
| Jørgensen, revisión de estudios sobre estimación experta (2004) | El resumen y las prácticas recomendadas | Que las estimaciones se quedan cortas de forma sistemática |
| Eveleens y Verhoef, "The Rise and Fall of the Chaos Report Figures" (IEEE Software, 2010) | El resumen | Por qué no citar el CHAOS como dato |
| McConnell, *Software Estimation* (2006); Vacanti, *When Will It Be Done?* (edición sin verificar); Opelt y otros, *Agile Contracts* (Wiley, 2013) | No se leyeron | Pendientes para estimación por rangos, previsión por flujo y contratos |

Se usan en [acuerdo inicial](../Encargo/acuerdo-inicial.md), [estimación](../Encargo/estimacion.md) y [modelos de contrato y cobro](../Encargo/modelos-de-contrato-y-cobro.md); el caso del precio cerrado tiene su propia bibliografía en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md).
