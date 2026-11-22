---
resumen: >-
  El modelo mental es lo que una persona cree que hace un sistema y cómo lo hace. Cuando difiere del funcionamiento real o de lo que el diseñador supone, la persona se equivoca o no entiende qué pasó.
estado: borrador
estabilidad: estable
fuentes:
  - "NN/g, Megan Chan, Mental Models (26 de enero de 2024; actualiza un texto de Nielsen de 2010): https://www.nngroup.com/articles/mental-models/"
  - "NN/g, Kathryn Whitenton, The Two UX Gulfs: Evaluation and Execution (11 de marzo de 2018): https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/"
  - "NN/g, Raluca Budiu, Recognition vs. Recall (15 de enero de 2024): https://www.nngroup.com/articles/recognition-and-recall/"
  - "Diapositivas del curso CSE 440 (Univ. de Washington, 2017) sobre The Design of Everyday Things: https://courses.cs.washington.edu/courses/cse440/17au/slides/lecture/l06-doet.pdf (resumen secundario; el libro de Norman, 2013, no se leyó)"
  - "UX/.investigacion/percepcion-y-decision.md"
aliases: [mental model, modelo conceptual, imagen del sistema, golfo de ejecución, golfo de evaluación]
creado: 2026-11-22
revisado:
---

# Modelo mental

El modelo mental es lo que una persona cree que hace un sistema y cómo lo hace. Cuando difiere del funcionamiento real o de lo que el diseñador supone, la persona se equivoca o no entiende qué pasó.

NN/g lo define como "what the user believes about the system (web, application, or other kind of product) at hand". Es una creencia de la persona, y NN/g señala que a menudo es menos desarrollada que la del diseñador y lleva a errores. Aparece en toda la vertical [Percepción y decisión](percepcion-y-decision.md).

## Por qué el diseñador no ve el problema

Según NN/g, quienes diseñan arman modelos mentales detallados de lo que crean, y por eso creen que cada función es fácil de entender. Los modelos de los usuarios suelen estar menos desarrollados y los llevan a errores. Esta base lo lee como una razón para no confiar en la propia lectura de la pantalla (inferencia). Para ver dónde se pierde otra persona sirven [métodos de investigación](../Investigacion/metodos-de-investigacion.md) como la [entrevista de usuario](../Investigacion/entrevista-de-usuario.md) y el [test de usabilidad](../Evaluacion/test-de-usabilidad.md).

## Los dos golfos de Norman

Hutchins, Hollan y Norman acuñaron en 1986 dos "golfos" entre la persona y el sistema, que Norman explicó después en *The Design of Everyday Things*. Según NN/g:

| Golfo | Qué cuesta | Pregunta de la persona |
|---|---|---|
| De ejecución | Decidir y hacer la acción que lleva a la meta | ¿Qué hago para conseguir esto? |
| De evaluación | Entender el estado del sistema después de actuar | ¿Qué pasó y sirvió? |

NN/g recomienda cerrar ambos con un "transparent conceptual model". Las diapositivas de curso consultadas resumen el ciclo de acción de Norman en siete etapas: establecer la meta, formar la intención, especificar la secuencia de acciones, ejecutar, percibir el estado, interpretarlo y evaluarlo. Las cuatro primeras etapas corresponden al golfo de ejecución y las tres últimas al de evaluación (lectura propia de esa descripción, no una cita). Los significantes y la respuesta del sistema que cierran cada golfo están en [Principios de interacción](../Interaccion/principios-de-interaccion.md).

## Tres vocabularios para lo mismo

Conviven tres. Las diapositivas, que atribuyen la terminología a Cooper y no a Norman, distinguen el modelo de implementación (cómo está construido), el modelo manifiesto o imagen del sistema (lo que la interfaz deja ver) y el modelo mental (lo que cree la persona). NN/g contrapone el modelo mental del usuario al del diseñador que conoce el producto, y no usa "modelo conceptual". En esta base, "modelo mental" nombra solo la creencia de la persona. Lo que el diseñador controla es la imagen del sistema, no el modelo del usuario.

> [!NOTE] Sin fuente todavía: la atribución exacta de cada término a Norman (2013) no se verificó contra el libro; solo hay diapositivas de curso y NN/g.

## Reconocer es más barato que recordar

Cuando el modelo mental es incompleto, ayuda que la interfaz muestre las opciones en lugar de pedir que se las recuerde. Según NN/g, "recognition is easier than recall because it involves more cues". El menú es el ejemplo clásico de reconocimiento; ingresar una contraseña, el de recuerdo. Es la heurística 6 de Nielsen, que se aplica en la [evaluación heurística](../Evaluacion/evaluacion-heuristica.md). El costo de recordar es una forma de [carga cognitiva](carga-cognitiva.md).

## Dónde leer más

El recurso canónico es Norman, *The Design of Everyday Things* (edición revisada de 2013): el capítulo 1 trae los golfos y el ciclo de acción, y el capítulo 2, los modelos conceptuales y la imagen del sistema. Conviene fijarse en que el diseñador solo controla la imagen del sistema. Como puerta de entrada corta y pública, el artículo de NN/g sobre los dos golfos.
