---
resumen: >-
  El seguimiento del conocimiento (knowledge tracing) estima, respuesta a respuesta, la probabilidad de que alguien domine cada habilidad mientras practica. Su versión clásica, Bayesian Knowledge Tracing, separa saber de acertar; las redes neuronales no la superan con claridad.
estado: vigente
estabilidad: estable
fuentes:
  - "Corbett y Anderson (1995), Knowledge tracing: Modeling the acquisition of procedural knowledge, User Modeling and User-Adapted Interaction 4:253-278, doi 10.1007/BF01099821 (texto completo, PDF escaneado; se leyeron las págs. 253-262): http://act-r.psy.cmu.edu/wordpress/wp-content/uploads/2012/12/893CorbettAnderson1995.pdf"
  - "Wikipedia, Bayesian knowledge tracing: https://en.wikipedia.org/wiki/Bayesian_knowledge_tracing"
  - "Piech et al. (2015), Deep Knowledge Tracing, NeurIPS (abstract): https://arxiv.org/abs/1506.05908"
  - "Khajah, Lindsey y Mozer (2016), How deep is knowledge tracing?, arXiv:1604.02416v2 (texto completo): https://arxiv.org/abs/1604.02416"
  - "Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md"
  - "Evaluacion-educativa/.investigacion/fuentes-adaptativa-2026-11.md"
aliases: [knowledge tracing, Bayesian Knowledge Tracing, BKT, deep knowledge tracing, DKT, modelo del estudiante]
creado: 2026-11-27
revisado: 2026-11-27
---

# Seguimiento del conocimiento

El seguimiento del conocimiento (knowledge tracing) estima, respuesta a respuesta, la probabilidad de que alguien domine cada habilidad mientras practica. Su versión clásica, Bayesian Knowledge Tracing, separa saber de acertar; las redes neuronales no la superan con claridad.

Es la rama de la [evaluación adaptativa](evaluacion-adaptativa.md) que viene de los [tutores inteligentes](../../Tecnologia-educativa/Tutores-inteligentes/tutores-inteligentes.md), donde es el modelo del alumno de su [arquitectura](../../Tecnologia-educativa/Tutores-inteligentes/arquitectura-de-un-tutor-inteligente.md). A diferencia de la [teoría de respuesta al ítem](teoria-de-respuesta-al-item.md), que mide una vez, el seguimiento actualiza la estimación durante la práctica: supone que la persona aprende mientras responde.

## Saber no es acertar

Corbett y Anderson (1995) propusieron el modelo para el ACT Programming Tutor, donde se aprende a escribir programas cortos en Lisp. El tutor mantiene, para cada regla, la probabilidad de que el estudiante la haya aprendido.

> [!WARNING] Obsoleto desde 2026-11: esta base databa el artículo en 1994, el año que asignaba al volumen 4. El artículo impreso dice «User Modeling and User-Adapted Interaction 4: 253-278, 1995» y «Received 1 December 1994; in final form 13 March 1995», así que se cita como 1995.

Bayesian Knowledge Tracing (BKT) usa cuatro parámetros por regla. Los nombres en inglés son los del artículo:

| Parámetro | Qué es |
|---|---|
| Conocimiento previo (*initial learning*, p(L0)) | Probabilidad de que la regla ya esté aprendida antes de la primera oportunidad de aplicarla, por ejemplo por haber leído el texto |
| Aprendizaje (*acquisition*, p(T)) | Probabilidad de pasar a aprendida después de cada oportunidad de aplicarla |
| Adivinanza (*guess*, p(G)) | Probabilidad de acertar sin haberla aprendido |
| Desliz (*slip*, p(S)) | Probabilidad de equivocarse habiéndola aprendido |

La adivinanza y el desliz son la idea que sirve fuera del modelo: un acierto puede ser suerte y un error puede ser un descuido, así que una respuesta sola no decide.

El modelo tiene dos estados: «Each coding rule is either in the learned state or in the unlearned state». Además, «There is no forgetting»: una regla aprendida no vuelve atrás. El criterio de dominio del tutor es una probabilidad de conocimiento de 0,95.

## La versión con redes neuronales

Piech et al. (2015) propusieron Deep Knowledge Tracing (DKT): una red neuronal recurrente que no necesita que alguien codifique a mano qué habilidad mide cada pregunta y que, según el abstract, predijo mejor en varios conjuntos de datos.

> [!IMPORTANT]
> **Las redes predicen mejor (Piech et al., 2015).** DKT superó a BKT en los conjuntos de datos que probaron.
>
> **La ventaja venía de lo que le faltaba a BKT (Khajah, Lindsey y Mozer, 2016).** Con extensiones de BKT (olvido, descubrimiento de habilidades, habilidades de cada estudiante) el rendimiento queda «indistinguishable» del de DKT. En Assistments, BKT clásico dio un AUC de 0,73 (0,67 en el trabajo de Piech), BKT con olvido 0,83 y DKT 0,86 según Piech. En Statics, BKT con las tres extensiones dio 0,75 y DKT 0,76; en Spanish, 0,846 contra 0,836. Según los autores, el 31,6 % de la diferencia que informó Piech viene de un cálculo del AUC sesgado contra BKT, y otro 50,6 % desaparece al sumar el olvido. Según el buscador, Xiong et al. (2016) encontraron duplicados en Assistments que inflaban los resultados de DKT, y Wilson et al. (2016) sostienen que el seguimiento no se beneficia de la «profundidad».

## Qué sirve con pocos alumnos

Ajustar los parámetros pide muchas respuestas de muchas personas; con un grupo chico habría que inventarlos. Lo que se lleva es conceptual, y es inferencia del informe de esta base: pedir más de una evidencia, en momentos distintos, antes de dar por dominada una habilidad. Es la misma lógica que justifica no ponerle nota a una sola [prueba de práctica](../Propositos/evaluacion-como-aprendizaje.md) y que pide la [calificación por dominio](../Calificacion-y-acreditacion/calificacion-por-dominio.md).

> [!NOTE] Sin fuente todavía: Xiong et al. (2016) y Wilson et al. (2016) leídos en su fuente, y las págs. 263-278 de Corbett y Anderson (1995), con sus cuatro estudios empíricos.
