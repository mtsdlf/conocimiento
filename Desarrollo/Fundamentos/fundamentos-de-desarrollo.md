---
resumen: >-
  Los fundamentos de desarrollo son lo que cruza todo el tema sin ser una etapa del proceso: cómo
  se divide el campo, de dónde viene la forma actual de trabajar, las escuelas que compiten, lo que
  pierde peso, la bibliografía y el glosario.
estado: borrador
estabilidad: estable
fuentes:
  - https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge
  - https://www.computer.org/education/bodies-of-knowledge/software-engineering
  - https://en.wikipedia.org/wiki/Software_crisis
  - https://en.wikipedia.org/wiki/Waterfall_model
  - https://arxiv.org/html/2510.03894v3
  - https://en.wikipedia.org/wiki/Extreme_programming
  - https://agilemanifesto.org/
  - https://en.wikipedia.org/wiki/Accelerate_(book)
  - https://scrumguides.org/scrum-guide.html
  - https://dora.dev/research/2025/dora-report/
  - https://en.wikipedia.org/wiki/Vibe_coding
  - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  - https://metr.org/blog/2026-02-24-uplift-update/
  - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
  - https://standards.ieee.org/standard/12207-2017
aliases: [fundamentos de desarrollo de software, historia del desarrollo de software, fundamentos]
creado: 2026-11-27
revisado:
---

# Fundamentos de desarrollo

Los fundamentos de desarrollo son lo que cruza todo el tema sin ser una etapa del proceso: cómo se divide el campo, de dónde viene la forma actual de trabajar, las escuelas que compiten, lo que pierde peso, la bibliografía y el glosario.

El [tema](../desarrollo.md) se escribe desde una escuela elegida, la ingeniería de software moderna de Farley con la evidencia de DORA. Esta carpeta dice qué otras escuelas hay, qué se dejó fuera y con qué evidencia, para que la elección se pueda revisar.

## Cómo se divide el campo a sí mismo

La referencia del campo es SWEBOK, la guía del cuerpo de conocimiento de la IEEE Computer Society. Su versión 4, de octubre de 2024, tiene 18 áreas de conocimiento: suma arquitectura, operaciones y seguridad a las 15 de la versión anterior y no quita ninguna. La página oficial no se pudo abrir; la lista sale de Wikipedia.

El árbol del tema cubre las áreas del proceso: requisitos ([Encargo](../Encargo/encargo.md) y [Definición](../Definicion/definicion.md)), construcción ([Construcción](../Construccion/construccion.md)), pruebas ([Verificación](../Verificacion/verificacion.md)) y mantenimiento ([Evolución](../Evolucion/evolucion.md)). Arquitectura y diseño viven en [Arquitectura](../../Arquitectura/arquitectura.md), y operaciones, en [DevOps](../../DevOps/devops.md). La seguridad del software, área nueva de la v4, todavía no tiene nota en este tema; lo más cercano es [DevSecOps](../../DevOps/DevSecOps/devsecops.md). El corte en dos ciclos, con el cliente y técnico, no sale de SWEBOK: es de esta base.

## De la crisis de 1968 a los agentes

La historia del proceso se puede contar en cuatro etapas. Solo van los hitos que se verificaron con una fuente; los años de varios libros clásicos quedan afuera hasta confirmarlos.

| Año | Hito |
|---|---|
| 1968 | Conferencia de la OTAN en Garmisch, del 7 al 11 de octubre; la expresión "software crisis" se atribuye a sus asistentes |
| 1970 | Royce publica "Managing the Development of Large Software Systems", que criticaba la pasada única y después se leyó como origen de la cascada |
| 1972 | Dijkstra, en su conferencia del Premio Turing: "The major cause of the software crisis is that the machines have become several orders of magnitude more powerful!" |
| 1999 | Beck publica *Extreme Programming Explained*, después del proyecto C3 de Chrysler, que lideraba desde 1996 |
| 2001 | El Manifiesto Ágil, con 17 firmantes |
| 2004 | Segunda edición de *Extreme Programming Explained*, con Cynthia Andres |
| 2018 | Forsgren, Humble y Kim publican *Accelerate*, con métricas y capacidades medidas en encuestas |
| 2020 | Nueva versión de la Scrum Guide |
| 2024 | SWEBOK v4, con 18 áreas |
| 2025 | Karpathy nombra el vibe coding (febrero); METR publica su ensayo controlado con desarrolladores experimentados (julio); DORA describe la IA como amplificador (septiembre); Böckeler analiza el desarrollo guiado por especificaciones (octubre) |
| 2026 | METR advierte que el diseño de su estudio de 2025 ya no mide bien y lo rediseña (febrero) |

La primera etapa, de 1968 a fines de los ochenta, es la de la crisis del software y la planificación predictiva. La segunda, hasta 2010 más o menos, es la del desarrollo iterativo y ágil: XP, Scrum y el Manifiesto. La tercera agrega la entrega continua, DevOps y la evidencia de *Accelerate*. La cuarta empieza con los asistentes y sigue con los agentes de código, con la medición de su efecto todavía en disputa. El corte en etapas es de esta base.

La IEEE marca la edición 2017 de la norma de ciclo de vida ISO/IEC/IEEE 12207 como reemplazada por una de 2026. No se verificó en la ISO.

> [!NOTE] Sin fuente todavía: los años de Parnas sobre módulos, Brooks (*The Mythical Man-Month*), Boehm y el modelo espiral, la presentación de Scrum, Beck sobre TDD, Humble y Farley (*Continuous Delivery*) y el origen del movimiento DevOps, para sumarlos a la tabla.

## Qué hay en los fundamentos

- [Escuelas de desarrollo](escuelas-de-desarrollo.md): ágil, XP, Scrum, Kanban, Shape Up, ingeniería moderna con DORA, cascada, desarrollo guiado por especificaciones y las posturas sobre la IA, y por qué el tema elige la ingeniería moderna.
- [Lo que pierde peso en desarrollo](lo-que-pierde-peso-en-desarrollo.md): las prácticas que el tema dejó en segundo plano, con quién lo dice, la evidencia en contra y un veredicto, más las creencias que no conviene repetir.
- [Bibliografía de desarrollo](bibliografia-de-desarrollo.md): qué leer según lo que se necesite hacer, qué parte y en qué fijarse.
- [Glosario de desarrollo](glosario-de-desarrollo.md): los términos del tema en una línea, con la nota donde se explica cada uno.
