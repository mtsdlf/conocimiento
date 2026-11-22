---
resumen: >-
  Los principios de interacción son el criterio con que se juzga si una interfaz se entiende y se controla: el concepto de significante de Norman (con su corrección sobre affordance), los siete principios de la norma ISO 9241-110 y los tres umbrales de tiempo de respuesta de 0,1, 1 y 10 segundos.
estado: vigente
estabilidad: estable
fuentes:
  - "ISO 9241-110:2020, Ergonomics of human-system interaction, Part 110: Interaction principles, cláusula 4.1 (muestra pública: https://cdn.standards.iteh.ai/samples/75258/83c8cf072187487686645aad04eff40e/ISO-9241-110-2020.pdf; ficha: https://www.iso.org/standard/75258.html)"
  - "Donald Norman, Signifiers, not affordances, Interactions 15(6), 2008: https://jnd.org/signifiers-not-affordances/"
  - "Donald Norman, The Design of Everyday Things, ed. revisada, 2013 (solo fichas: https://jnd.org/the-design-of-everyday-things-revised-and-expanded/)"
  - "Jakob Nielsen, Response Times: The 3 Important Limits (extracto del cap. 5 de Usability Engineering, 1993): https://www.nngroup.com/articles/response-times-3-important-limits/"
  - "UX/.investigacion/arquitectura-e-interaccion.md"
aliases: [principios de diálogo, ISO 9241-110, affordance, significante, signifier, tiempos de respuesta]
creado: 2026-11-22
revisado: 2026-11-22
---

# Principios de interacción

Los principios de interacción son el criterio con que se juzga si una interfaz se entiende y se controla: el concepto de significante de Norman (con su corrección sobre affordance), los siete principios de la norma ISO 9241-110 y los tres umbrales de tiempo de respuesta de 0,1, 1 y 10 segundos.

Son tres cosas de naturaleza distinta que se usan juntas: conceptos de diseño, una norma y límites de tiempo. Sirven de criterio general para la [interacción](interaccion.md). Las diez heurísticas de Nielsen, que cumplen un papel parecido, se tratan en [Evaluación heurística](../Evaluacion/evaluacion-heuristica.md).

## Affordance y significante, según Norman

Norman corrigió en 2008 su propio uso de "affordance". Dice que al introducir el término al diseño, en 1988, se refería a "perceivable affordances", y concluye: "Forget affordances: what people need, and what design must provide, are signifiers". Define el significante como "some sort of indicator, some signal in the physical or social world that can be interpreted meaningfully", y agrega: "I call any physically perceivable cue a signifier, whether it is incidental or deliberate". La parte perceptible de una affordance es un significante. Gibson usaba "affordance" para nombrar una relación entre un agente y su entorno.

Un ejemplo de esta base, sin fuente propia: un botón con aspecto de botón es un significante de que se puede pulsar, y que se pueda pulsar es la affordance. Si falta el significante, la acción existe pero es difícil de descubrir. Según un resumen de buscador sobre Wikipedia, la edición revisada de 2013 del libro suma el significante para aclarar la definición de affordance.

> [!NOTE]
> Sin fuente todavía: las definiciones literales de Norman (2013) de restricciones, mapeo, feedback y modelo conceptual. Solo hay resúmenes de buscador, que no sirven como cita. Según la ficha del libro, las trata el capítulo 1 (principios fundamentales) y el 4 (restricciones, descubribilidad y feedback). Por eso esta nota no define el modelo conceptual ni lo distingue del [modelo mental](../Percepcion-y-decision/modelo-mental.md).

## Los siete principios de ISO 9241-110

La edición de 2020 reemplazó los "principios de diálogo" de 2006 por "principios de interacción" y agregó el compromiso del usuario. Según la cláusula 4.1, el orden de presentación "does not imply any priority". Los nombres en castellano son de esta base; no se leyó una versión oficial en castellano. La [usabilidad](../Fundamentos/glosario-de-ux.md) que mide ISO 9241-11 (eficacia, eficiencia y satisfacción) es otra norma de la misma serie.

| Principio | Qué pide la norma (cláusula 4.1, literal) |
|---|---|
| Adecuación a la tarea (suitability for the user's tasks) | Las funciones y las interacciones "are based on the task characteristics (rather than the technology chosen to perform the task)" |
| Autodescriptividad (self-descriptiveness) | Presenta "appropriate information, where needed by the user, to make its capabilities and use immediately obvious" |
| Conformidad con las expectativas (conformity with user expectations) | Su comportamiento es "predictable based on the context of use and commonly accepted conventions" |
| Aprendizaje (learnability) | "Supports discovery of its capabilities", permite explorar y "minimizes the need for learning" |
| Controlabilidad (controllability) | Deja al usuario "maintain control of the user interface and the interactions", incluida la velocidad y la secuencia |
| Robustez ante errores de uso (use error robustness) | Ayuda a evitar errores y, ante los identificables, los trata "tolerantly" y asiste en la recuperación |
| Compromiso del usuario (user engagement) | Presenta funciones e información "in an inviting and motivating manner supporting continued interaction" |

La cláusula 5 trae recomendaciones por principio; en la muestra solo se leyó el índice, que lista, por ejemplo, la "clear indication of processing status" bajo autodescriptividad y la "trustworthiness of the system" bajo compromiso. Para profundizar, leer la cláusula 4 y las recomendaciones de la 5 en la norma completa, y el capítulo 1 de *The Design of Everyday Things*.

## Los tres umbrales de tiempo de respuesta

Nielsen (1993, capítulo 5 de *Usability Engineering*) fija tres límites, que citan trabajos de Miller (1968) y de Card, Robertson y Mackinlay (1991):

| Umbral | Qué marca (literal) |
|---|---|
| 0,1 segundo | "about the limit for having the user feel that the system is reacting instantaneously" |
| 1 segundo | "about the limit for the user's flow of thought to stay uninterrupted" |
| 10 segundos | "about the limit for keeping the user's attention focused on the dialogue" |

Nielsen dice que la guía "has been about the same for thirty years". Son una guía de practicante de 1993; los trabajos originales de 1968 y 1991 no se leyeron. Los umbrales se definen una sola vez, acá: [Carga cognitiva](../Percepcion-y-decision/carga-cognitiva.md) y [Métricas de UX](../Evaluacion/metricas-de-ux.md) los enlazan sin repetirlos.

## Dónde tocan otras notas

Los principios aparecen aplicados en [Formularios](formularios.md), donde el feedback y la prevención de errores definen la validación. Un formulario que fuerza una cuenta, o una interfaz que oculta una salida, cruza con el [patrón oscuro](../Percepcion-y-decision/patron-oscuro.md). Los requisitos que la [accesibilidad](../Accesibilidad/accesibilidad.md) pone al feedback y a la operación por teclado complementan estos principios.
