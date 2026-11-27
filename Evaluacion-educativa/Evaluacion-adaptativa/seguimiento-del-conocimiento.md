---
resumen: >-
  El seguimiento del conocimiento (knowledge tracing) estima, respuesta a respuesta, la probabilidad de que alguien domine cada habilidad mientras practica. Su versión clásica, Bayesian Knowledge Tracing, separa saber de acertar; las redes neuronales no la superan con claridad.
estado: borrador
estabilidad: estable
fuentes:
  - "Corbett y Anderson (1994), Knowledge tracing: Modeling the acquisition of procedural knowledge, User Modeling and User-Adapted Interaction 4, 253-278 (resumen del buscador): https://doi.org/10.1007/BF01099821"
  - "Wikipedia, Bayesian knowledge tracing: https://en.wikipedia.org/wiki/Bayesian_knowledge_tracing"
  - "Piech et al. (2015), Deep Knowledge Tracing, NeurIPS (abstract): https://arxiv.org/abs/1506.05908"
  - "Khajah, Lindsey y Mozer (2016), How deep is knowledge tracing? (resumen de herramienta): https://ar5iv.arxiv.org/html/1604.02416"
  - "Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md"
aliases: [knowledge tracing, Bayesian Knowledge Tracing, BKT, deep knowledge tracing, DKT, modelo del estudiante]
creado: 2026-11-27
revisado:
---

# Seguimiento del conocimiento

El seguimiento del conocimiento (knowledge tracing) estima, respuesta a respuesta, la probabilidad de que alguien domine cada habilidad mientras practica. Su versión clásica, Bayesian Knowledge Tracing, separa saber de acertar; las redes neuronales no la superan con claridad.

Es la rama de la [evaluación adaptativa](evaluacion-adaptativa.md) que viene de los tutores inteligentes, que son [tecnología educativa](../../Tecnologia-educativa/tecnologia-educativa.md). A diferencia de la [teoría de respuesta al ítem](teoria-de-respuesta-al-item.md), que mide una vez, el seguimiento actualiza la estimación durante la práctica: supone que la persona aprende mientras responde.

## Saber no es acertar

Corbett y Anderson propusieron el modelo para un tutor que mantenía, para cada regla, la probabilidad de que el estudiante la hubiera aprendido. La fecha discrepa entre fuentes: el volumen 4 de la revista corresponde a 1994, y Wikipedia y Semantic Scholar dan 1995; esta base usa 1994.

Bayesian Knowledge Tracing (BKT) usa cuatro parámetros por habilidad, según Wikipedia:

| Parámetro | Qué es |
|---|---|
| Conocimiento previo | Probabilidad de que ya la sepa antes de practicar |
| Aprendizaje | Probabilidad de aprenderla en cada oportunidad de práctica |
| Desliz (*slip*) | Probabilidad de fallar sabiéndola |
| Adivinanza (*guess*) | Probabilidad de acertar sin saberla |

Supone que cada habilidad se sabe o no se sabe, y que cada respuesta es correcta o incorrecta. Los dos últimos parámetros son la idea que sirve fuera del modelo: un acierto puede ser suerte y un error puede ser un descuido, así que una respuesta sola no decide.

## La versión con redes neuronales

Piech et al. (2015) propusieron Deep Knowledge Tracing (DKT): una red neuronal recurrente que no necesita que alguien codifique a mano qué habilidad mide cada pregunta y que, según el abstract, predijo mejor en varios conjuntos de datos.

> [!IMPORTANT]
> **Las redes predicen mejor (Piech et al., 2015).** DKT superó a BKT en los conjuntos de datos que probaron.
>
> **La ventaja venía de lo que le faltaba a BKT (Khajah, Lindsey y Mozer, 2016).** Con extensiones de BKT (olvido, diferencias entre preguntas, habilidades latentes) el rendimiento queda «indistinguishable» del de DKT. En Assistments, BKT clásico dio un AUC de 0,73 (0,67 en el trabajo de Piech), BKT con olvido 0,83 y DKT 0,86; en Statics, 0,75 contra 0,76; en Spanish, 0,846 contra 0,836. Las cifras vienen de un resumen de herramienta y hay que verificarlas. Según el buscador, Xiong et al. (2016) encontraron duplicados en Assistments que inflaban los resultados de DKT, y Wilson et al. (2016) sostienen que el seguimiento no se beneficia de la «profundidad».

## Qué sirve con pocos alumnos

Ajustar los parámetros pide muchas respuestas de muchas personas; con un grupo chico habría que inventarlos. Lo que se lleva es conceptual, y es inferencia del informe de esta base: pedir más de una evidencia, en momentos distintos, antes de dar por dominada una habilidad. Es la misma lógica que justifica no ponerle nota a una sola [prueba de práctica](../Propositos/evaluacion-como-aprendizaje.md) y que pide la [calificación por dominio](../Calificacion-y-acreditacion/calificacion-por-dominio.md).

> [!NOTE] Sin fuente todavía: Corbett y Anderson (1994) leído en el original, y las cifras de AUC de Khajah et al. (2016) verificadas en el artículo.
