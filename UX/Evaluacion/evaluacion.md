---
resumen: >-
  La evaluación comprueba si un diseño funciona, con tres tipos de evidencia: observar a personas usándolo, revisarlo contra principios de usabilidad y medir su rendimiento. Cada una encuentra problemas distintos, así que se combinan.
estado: vigente
estabilidad: estable
fuentes:
  - "NN/g, Usability Problems Found by Heuristic Evaluation (resume a Nielsen 1992): https://www.nngroup.com/articles/usability-problems-found-by-heuristic-evaluation/ (leída a través del resumen de una herramienta)"
  - "NN/g, When to Use Which User-Experience Research Methods: https://www.nngroup.com/articles/which-ux-research-methods/ (leída a través del resumen de una herramienta)"
  - "Jeffries, Miller, Wharton y Uyeda (1991), User interface evaluation in the real world, CHI (solo resumen): https://hci.stanford.edu/seminar/abstracts/90-91/910522-jeffries.html"
  - "ISO 9241-210:2019: https://www.iso.org/standard/77520.html"
  - "UX/.investigacion/investigacion-y-evaluacion.md"
aliases: [evaluar UX, evaluación de usabilidad, usability evaluation]
creado: 2026-11-22
revisado: 2026-11-22
---

# Evaluación

La evaluación comprueba si un diseño funciona, con tres tipos de evidencia: observar a personas usándolo, revisarlo contra principios de usabilidad y medir su rendimiento. Cada una encuentra problemas distintos, así que se combinan.

Es la última actividad del ciclo de [diseño centrado en el usuario](../ux.md) (el orden de las actividades de ISO 9241-210 no se verificó contra la norma), y lo que sale de acá corrige lo que se creía en la [investigación](../Investigacion/investigacion.md). Evalúa lo que se decidió en [interacción](../Interaccion/interaccion.md), [diseño visual](../Diseno-visual/diseno-visual.md) y [accesibilidad](../Accesibilidad/accesibilidad.md). En términos del [mapa de métodos](../Investigacion/metodos-de-investigacion.md), es la investigación evaluativa.

## Tres formas de evaluar y qué encuentra cada una

Observar a personas es el [test de usabilidad](test-de-usabilidad.md): un facilitador pide tareas realistas a un participante parecido al usuario real y registra dónde se traba. Muestra dónde se traba alguien con una tarea realista. Revisar contra principios es la [evaluación heurística](evaluacion-heuristica.md): varios evaluadores recorren la interfaz solos con las diez heurísticas de Nielsen, sin participantes, y encuentran otros problemas. Medir es el trabajo de [métricas de UX](metricas-de-ux.md): puntajes de tarea y cuestionario con personas, y métricas de comportamiento a escala.

Según el resumen de Jeffries et al. (1991), que compararon test, heurística, guías y recorridos cognitivos sobre la misma interfaz, las técnicas encontraron tipos distintos de problemas. NN/g recomienda alternar y empezar por la heurística. La heurística, advierte NN/g, no reemplaza la investigación con usuarios.

## Lo que ninguna evaluación contesta sola

Una evaluación con pocas personas dice dónde se traba la gente, pero no cuántos se traban. Un experimento a escala dice qué variante rinde más, pero no por qué. Según MeasuringU, el NPS es un síntoma de lealtad y no dice qué arreglar. Por eso la nota de [métricas](metricas-de-ux.md) separa las que salen de un test con personas de las que salen del comportamiento a escala.

El número de participantes también está discutido. El debate de los cinco usuarios, con la fórmula de Nielsen y Landauer y las críticas de Spool, Faulkner y otros, está en el [test de usabilidad](test-de-usabilidad.md).

## Lo que hay adentro

- [Test de usabilidad](test-de-usabilidad.md): observar a participantes haciendo tareas, con el debate de cuántos hacen falta.
- [Evaluación heurística](evaluacion-heuristica.md): las diez heurísticas de Nielsen en tabla y cómo se organiza una revisión con evaluadores.
- [Métricas de UX](metricas-de-ux.md): SUS, tiempo y éxito de tarea, HEART, NPS y su crítica, y dónde entra el experimento A/B.
- Para una medición de causa a escala fuera de UX, [incrementalidad](../../Marketing/Medicion/incrementalidad.md), del tema Marketing.

## Qué falta

Faltan estas notas y se van a sumar:

- Experimento A/B como componente propio, con diseño, tamaño de muestra y fallas comunes. Hoy se trata dentro de [métricas de UX](metricas-de-ux.md#donde-entra-el-experimento-ab).
- Árbol de prueba (tree testing): cómo se evalúa una estructura de navegación sin diseño visual.
- Test de primer clic: si la persona empieza una tarea por el lugar correcto.
