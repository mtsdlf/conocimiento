---
resumen: >-
  Una especificación es el texto que fija, antes de construir un cambio, qué tiene que hacer, con
  qué restricciones, qué queda abierto y cómo se sabe que está terminado; con agentes de código es el
  insumo principal que el agente lee.
estado: vigente
estabilidad: semi
fuentes:
  - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
  - https://www.thoughtworks.com/radar/techniques/spec-driven-development
  - https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit
  - https://www.thoughtworks.com/radar/tools/openspec
  - https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
  - https://arxiv.org/abs/2608.25202
  - https://research.google/pubs/grounding-ai-agents-in-contracts-an-empirical-evaluation-of-spec-driven-test-generation/
  - https://code.claude.com/docs/en/best-practices
  - https://learn.chatgpt.com/guides/best-practices
  - https://alistairmavin.com/ears/
  - https://standards.ieee.org/ieee/29148/6937
  - https://arxiv.org/abs/2502.13069
  - https://github.com/github/spec-kit
  - https://kiro.dev/docs/specs/
aliases: [spec, especificación, spec-driven development, SDD, desarrollo guiado por especificaciones, requisito, SPEC.md]
creado: 2026-11-27
revisado: 2026-11-27
---

# Especificación

Una especificación es el texto que fija, antes de construir un cambio, qué tiene que hacer, con qué restricciones, qué queda abierto y cómo se sabe que está terminado; con agentes de código es el insumo principal que el agente lee.

Es la pieza central de [Definición](definicion.md). Toma el alcance que se acordó en [Encargo](../Encargo/alcance-y-aceptacion.md), usa las palabras del [modelo de dominio](modelo-de-dominio.md), se cierra con [criterios de aceptación](criterios-de-aceptacion.md) y se parte en [tareas](descomposicion-en-tareas.md). La [historia de usuario](historia-de-usuario.md) dice para quién y para qué; la especificación dice qué, con el detalle que necesita quien construye.

## Las partes de una especificación de un cambio

Las guías de los fabricantes de agentes piden casi lo mismo. OpenAI propone cuatro bloques: "Goal", "Context", "Constraints" y "Done when". Anthropic insiste en contarle al agente lo que no puede ver en el código y en darle un chequeo que ejecute. Con eso y lo que dice la investigación sobre ambigüedad, esta base propone que una especificación de un cambio lleve estas partes; las cuatro primeras siguen a las guías y la quinta al estudio de ambigüedad:

| Parte | Qué dice | Qué se arriesga si falta (criterio de esta base) |
|---|---|---|
| Objetivo | el resultado que se busca, en una o dos oraciones | el agente optimiza otra cosa |
| Contexto | lo que no está en el código: reglas del negocio, decisiones previas, quién lo usa | el agente lo inventa |
| Restricciones | lo que no se toca, las dependencias permitidas, las cualidades que se tienen que mantener | cambios no pedidos |
| Terminado | los ejemplos que se comprueban, idealmente ejecutables | el agente declara terminado antes de tiempo |
| Preguntas abiertas y supuestos | lo que no se sabe y lo que se dio por hecho | la ambigüedad se resuelve en silencio |

La fila de preguntas abiertas importa más con agentes que con personas. Según el resumen del estudio Ambig-SWE (ICLR 2026), los modelos tienen dificultad para distinguir una tarea bien especificada de una subespecificada y por defecto no preguntan; dejarlos interactuar mejoró el rendimiento hasta un 74 % en las subespecificadas.

## Qué hace bueno a un requisito

La norma ISO/IEC/IEEE 29148:2018 "defines the construct of a good requirement, provides attributes and characteristics of requirements". De esa tradición sigue sirviendo, para una especificación chica, la idea de que cada requisito sea necesario, no ambiguo, verificable y trazable, y que diga qué hace el sistema sin decidir cómo.

> [!NOTE]
> Sin fuente todavía: la lista literal de características de un buen requisito de ISO/IEC/IEEE 29148 (secciones 5.2.5 y 5.2.6). La enumeración de arriba es un resumen de la tradición, no una cita de la norma.

Una forma de escribir requisitos sin ambigüedad es EARS, de Alistair Mavin (Rolls-Royce, publicada en 2009). Su patrón para un evento es "When <trigger>, the <system name> shall <system response>", y tiene cinco patrones más: ubicuo, por estado, opcional, no deseado y complejo. Ejemplo de esta base: "Cuando el carrito supera el stock disponible, el sistema rechaza el pedido e informa qué producto falta".

## Una especificación del tamaño del problema

Böckeler, al probar las herramientas de especificación, vio una que convirtió un bug chico en cuatro historias de usuario con 16 criterios de aceptación; de otra dijo que era "overkill for the size of the problem" y que sus salidas eran "very verbose and tedious to review". El Radar de Thoughtworks marcó lo mismo: especificaciones difíciles de revisar y resultados que varían con el tamaño y el tipo de tarea. Según su resumen, el estudio de Agarwal y otros (preprint; 21 entrevistas y 266 repositorios) encontró un uso selectivo de las especificaciones, sobre todo en funcionalidades nuevas, y más fiabilidad del agente a cambio de más costo de planificar y revisar.

El criterio de esta base: la especificación crece con el tamaño y la oscuridad del problema. Un arreglo de una línea con una prueba que falla no necesita más texto que la prueba. Una funcionalidad nueva con reglas de negocio necesita objetivo, contexto, ejemplos y preguntas abiertas. Si una especificación ya tiene detalles de implementación, es probable que quede vieja: según su resumen, Agarwal y otros encontraron que esos detalles hacen a las especificaciones "prone to decay".

## Escribirla con el agente y construir con otro contexto

La guía de Anthropic propone que, cuando el pedido no está pensado del todo, el agente entreviste a la persona: "Interview me until you could write the spec, then write it to SPEC.md". Después, la construcción arranca en una sesión nueva "so the build begins with a clean context and a written definition of done", y un subagente revisa el resultado contra la especificación. Las preguntas que la persona no puede contestar son las que se llevan al cliente.

## Los tres niveles del desarrollo guiado por especificaciones

El desarrollo guiado por especificaciones (spec-driven development) propone que la especificación, y no el código, sea el artefacto principal. Böckeler describe tres niveles:

| Nivel | Qué pasa con la especificación |
|---|---|
| Spec-first | "A carefully written spec comes before AI-assisted coding, and it guides the current task." |
| Spec-anchored | se conserva después de la tarea y se usa para evolucionar y mantener la funcionalidad |
| Spec-as-source | es el artefacto principal a largo plazo; las personas editan solo la especificación y nunca el código generado |

Un preprint de Piskala (2026) nombra los mismos tres niveles, pero es posterior y parece tomarlos de Böckeler: cuentan como una sola fuente. Böckeler compara el último nivel con el desarrollo dirigido por modelos, que "never took off for business applications", y teme que junte la rigidez de aquel con la imprevisibilidad de los modelos. En sus pruebas con Tessl, la misma especificación produjo código distinto entre corridas, y con otras herramientas los agentes a veces ignoraron instrucciones y otras las aplicaron de más.

> [!IMPORTANT]
> Es una práctica emergente sin estudio empírico que la respalde; la evidencia que hay es mixta.
>
> - En contra: Hill (ESEM 2026), sobre 88.052 pull requests, 119 repositorios y 25.209 artefactos de especificación, no encontró efecto de la calidad de la especificación sobre defectos (p = 0,164) ni sobre retrabajo (p = 0,860), ni sobre el alcance de los cambios hechos con IA (p = 0,997). Sus salvedades: los artefactos son sobre todo enlaces a tickets, ningún repositorio versiona la salida de herramientas de especificación, y "Developers write specs for their hardest work".
> - A favor, acotado: un estudio de Google Research sobre generación de pruebas encontró que documentar pre y postcondiciones antes de generar las pruebas mejora la detección de bugs en 9,8 puntos porcentuales (p = 0,0352) y la cobertura de ramas en 2,5 (p = 0,0034), según su resumen y con autoría que difiere entre fuentes. Es sobre pruebas, no sobre construir funcionalidades.
> - De práctica: Thoughtworks lo puso en "Assess" (noviembre de 2025), con flujos "elaborate and opinionated" y la duda de si repite la "bitter lesson" de que las reglas escritas a mano para IA no escalan.

## Las cualidades y el prototipo entran por otro lado

Las cualidades que el sistema tiene que mantener, que se suelen llamar requisitos no funcionales, son [características arquitectónicas](../../Arquitectura/Caracteristicas/caracteristicas-arquitectonicas.md). La especificación las nombra en las restricciones como criterio medible (ejemplo de esta base: "la búsqueda responde en menos de 300 ms con 10.000 productos", no "tiene que ser rápida"), y su forma ejecutable es una [fitness function](../../Arquitectura/Caracteristicas/fitness-function.md).

El prototipo como forma de decidir qué construir está en Producto, en [prueba de supuestos](../../Producto/Descubrimiento/prueba-de-supuestos.md) y en [dar forma a una solución](../../Producto/Descubrimiento/dar-forma-a-una-solucion.md), donde está la disputa sobre si un prototipo puede ser la especificación.

> [!NOTE]
> Sin fuente todavía: si un prototipo funcional hecho con un agente sirve como insumo de la especificación, y si ese prototipo se descarta o se reescribe antes de producción.

## Herramientas de especificación a noviembre de 2026

Copiado de las fuentes el 2026-11-27; cambia seguido.

| Herramienta | Qué hace | Nivel, según Böckeler o el Radar |
|---|---|---|
| Kiro | tres archivos por funcionalidad (requisitos, diseño, tareas) en tres fases; las tareas independientes corren en oleadas paralelas; un modo rápido sin puertas de aprobación | "mostly spec-first" |
| GitHub Spec Kit | una constitución por proyecto y, por funcionalidad, Specify, Plan, Tasks, Implement y Converge hasta que Converge devuelve `Converged` | spec-first en la práctica; aspira a spec-anchored. Radar: Assess (abril de 2026), con "instruction bloat" y "context rot" |
| OpenSpec | registra cada cambio como delta contra una especificación persistente | spec-anchored. Radar: Trial (noviembre de 2026), "more predictable agent output and fewer unintended changes" |
| Tessl | relación uno a uno entre especificación y archivo de código | apunta a spec-anchored y explora spec-as-source; en beta privada en octubre de 2025 |

Que Kiro use EARS se repite seguido, pero la página de documentación consultada no lo menciona.
