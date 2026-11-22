---
resumen: >-
  La evaluación heurística es la revisión de una interfaz por varios evaluadores que, cada uno por su cuenta, la comparan con principios de usabilidad, las diez heurísticas de Nielsen. Detecta problemas sin participantes y encuentra otros distintos de los del test de usabilidad, al que no reemplaza.
estado: vigente
estabilidad: semi
fuentes:
  - "NN/g, 10 Usability Heuristics for User Interface Design (Nielsen, publicada el 24-4-1994; revisada por última vez el 30-1-2024): https://www.nngroup.com/articles/ten-usability-heuristics/ (leída a través del resumen de una herramienta; las glosas son de esta base)"
  - "NN/g, How to Conduct a Heuristic Evaluation: https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/ (leída a través del resumen de una herramienta)"
  - "NN/g, Usability Problems Found by Heuristic Evaluation (resume a Nielsen 1992): https://www.nngroup.com/articles/usability-problems-found-by-heuristic-evaluation/ (leída a través del resumen de una herramienta)"
  - "Nielsen y Molich (1990), Heuristic evaluation of user interfaces, CHI, doi 10.1145/97243.97281 (solo abstract vía buscador)"
  - "Jeffries, Miller, Wharton y Uyeda (1991), User interface evaluation in the real world, CHI (solo resumen): https://hci.stanford.edu/seminar/abstracts/90-91/910522-jeffries.html"
  - "UX/.investigacion/investigacion-y-evaluacion.md y UX/.investigacion/posicion-contraria.md"
aliases: [heurísticas de Nielsen, diez heurísticas, heuristic evaluation, revisión experta]
creado: 2026-11-22
revisado: 2026-11-22
---

# Evaluación heurística

La evaluación heurística es la revisión de una interfaz por varios evaluadores que, cada uno por su cuenta, la comparan con principios de usabilidad, las diez heurísticas de Nielsen. Detecta problemas sin participantes y encuentra otros distintos de los del test de usabilidad, al que no reemplaza.

Es uno de los tres caminos de la [evaluación](evaluacion.md). Según NN/g, nació con Nielsen y Molich en 1990 y Nielsen refinó la lista en 1994 con un análisis factorial de 249 problemas de usabilidad. Varias heurísticas, como el feedback y el control, tocan principios de [interacción](../Interaccion/principios-de-interaccion.md), y la técnica se complementa con el [test de usabilidad](test-de-usabilidad.md).

## Las diez heurísticas de Nielsen

NN/g publicó la lista el 24 de abril de 1994, la revisó en 2020 y por última vez el 30 de enero de 2024. Según la propia página, "the 10 heuristics themselves have remained relevant and unchanged since 1994". NN/g las llama "broad rules of thumb", no guías específicas. Los títulos salen del resumen de una herramienta y las glosas de la tabla son de esta base; si se va a citar el texto de NN/g, hay que leerlo en la página.

| # | Heurística | Qué pide |
|---|---|---|
| 1 | Visibility of System Status | Que el sistema informe en qué estado está, con feedback a tiempo |
| 2 | Match Between the System and the Real World | Que use el lenguaje y los conceptos de la persona, no los internos |
| 3 | User Control and Freedom | Que haya salida clara, deshacer y rehacer cuando la persona se equivoca |
| 4 | Consistency and Standards | Que lo igual se vea y funcione igual, y que siga las convenciones |
| 5 | Error Prevention | Que el diseño evite el error antes de que ocurra |
| 6 | Recognition Rather than Recall | Que lo necesario esté a la vista y no obligue a recordar |
| 7 | Flexibility and Efficiency of Use | Que sirva al novato y acelere al experto |
| 8 | Aesthetic and Minimalist Design | Que no muestre información de más |
| 9 | Help Users Recognize, Diagnose, and Recover from Errors | Que los mensajes de error digan qué pasó y cómo seguir |
| 10 | Help and Documentation | Que la ayuda, si hace falta, sea breve y buscable |

Esta base propone usar las heurísticas para detectar problemas durante una evaluación, y no como lista de requisitos ni como medida de calidad. Un resumen derivado de Wikipedia afirma que nunca hubo una validación basada en investigación; no se pudo verificar en fuente primaria.

## Cómo se hace una evaluación

NN/g pide que "three to five people should independently evaluate" la misma interfaz, porque cada evaluador, aun experto, se pierde problemas. El procedimiento tiene tres pasos:

1. Preparar: leer las heurísticas, hacer una ronda de práctica y acotar el alcance.
2. Evaluar de forma independiente, de una a dos horas y con dos pasadas por la interfaz.
3. Consolidar: agrupar los hallazgos, discutirlos y decidir cuáles pasan a un test de usabilidad.

Como los problemas menores abundan, cada hallazgo lleva una severidad para ordenar qué corregir primero.

## Qué encuentra y qué se pierde

Según Nielsen (1992), resumido por NN/g, un evaluador solo halló cerca de 42% de los problemas mayores y 32% de los menores. Nielsen y Molich (1990) corrieron cuatro experimentos: los evaluadores individuales encontraron entre 20 y 51% de los problemas, y los agregados de tres a cinco "do rather well" (abstract vía buscador, sin verificar). Por eso se agrega a varios evaluadores y no se confía en uno.

La heurística encuentra cosas distintas que el test con usuarios. Jeffries et al. (1991) compararon test, heurística, guías y recorridos cognitivos sobre la misma interfaz y, según el resumen, las técnicas hallaron tipos distintos de problemas. NN/g recomienda alternar, con la heurística primero.

> [!IMPORTANT]
> Cuánto vale la heurística frente al test está discutido. NN/g sostiene que no reemplaza la investigación con usuarios, y admite que una violación no siempre es un problema real y que es difícil cubrir productos grandes. Una crítica habitual atribuye a Jeffries et al. que la heurística produce falsos positivos y hallazgos de baja prioridad, pero no se pudo leer el paper y esa crítica no se afirma. Sin conteos por técnica, no hay una comparación verificada de costo y beneficio.

> [!NOTE]
> Sin fuente todavía: el porcentaje de problemas que encuentran cinco evaluadores (circula "cerca de 75%") no se leyó en el paper de 1990; y los conteos por técnica de Jeffries et al. Las cifras y citas de NN/g salen de un resumen que una herramienta hizo de cada página: conviene cotejarlas en el original antes de entrecomillarlas.

## Qué leer

Para la lista y las descripciones completas, NN/g, [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/). Para el procedimiento, [How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/); conviene fijarse en el aviso de NN/g de que no sustituye a los usuarios. La fuente primaria para citar es Nielsen y Molich (1990) y Nielsen (1992).
