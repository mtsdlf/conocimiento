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
  - "Jeffries, Miller, Wharton y Uyeda (1991), User interface evaluation in the real world: a comparison of four techniques, CHI, pp. 119-124, doi 10.1145/108844.108862; texto en https://www.miramontes.com/writing/uievaluation/ ; resumen del seminario: https://hci.stanford.edu/seminar/abstracts/90-91/910522-jeffries.html"
  - "Gray y Salzman (1998), Damaged Merchandise? A Review of Experiments That Compare Usability Evaluation Methods, Human-Computer Interaction 13(3), 203-261: https://rauterberg.employee.id.tue.nl/lecturenotes/JFS-lecture/Gray&Salzman98a_HCI.pdf"
  - "Hertzum y Jacobsen (2001), The evaluator effect: a chilling fact about usability evaluation methods, IJHCI 13(4): https://forskning.ruc.dk/da/publications/the-evaluator-effect-a-chilling-fact-about-usability-evaluation-m/"
  - "Producto/.investigacion/revision-del-producto-propio.md"
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

La heurística encuentra cosas distintas que el test con usuarios. NN/g recomienda alternar, con la heurística primero.

## La comparación de Jeffries: cuatro técnicas sobre el mismo producto

Jeffries, Miller, Wharton y Uyeda (1991) evaluaron el mismo producto con cuatro técnicas:

| Técnica | Problemas | Entre los más graves | Horas-persona |
|---|---|---|---|
| Heurística, por especialistas en interfaz | 105 | 28 | 35 |
| Test con usuarios | 31 | 18 | 199 |
| Guías de diseño | 35 | 12 | 86 |
| Recorrido cognitivo | 35 | 9 | 43 |

Los conteos son sin repetidos dentro de cada grupo, y «los más graves» es el tercio de mayor gravedad. La heurística encontró más problemas, también más graves, y más barato, pero necesitó varios especialistas en interfaz y muchos de sus hallazgos fueron menores y puntuales. El test fue el mejor para los problemas recurrentes y generales, pero según los autores dejó pasar muchos problemas serios; algunos, como uno que borraba sin querer la carpeta del usuario, los encontró el test y fueron difíciles de ver con guías o con recorrido cognitivo. Fue un solo producto, con seis usuarios, y la técnica se confunde con la experiencia de quien la aplicó: la heurística la hicieron especialistas en interfaz, y las guías y el recorrido, ingenieros de software. El recorrido cognitivo es una inspección en la que un evaluador recorre una tarea con los ojos de alguien nuevo y en cada paso se pregunta si sabría qué hacer y si entendería que avanzó; sirve para tareas que se hacen por primera vez.

> [!IMPORTANT]
> Cuánto vale la heurística frente al test está discutido. NN/g sostiene que no reemplaza la investigación con usuarios, y admite que una violación no siempre es un problema real y que es difícil cubrir productos grandes. Gray y Salzman (1998) revisaron cinco comparaciones influyentes y encontraron fallas de validez que ponen en duda lo que se creía saber sobre la eficacia de cada método (según un resumen; el texto no se pudo abrir y no se verificó que la de Jeffries esté entre las cinco). Olson y Moran les respondieron en el mismo número. Hertzum y Jacobsen (2001), en 11 estudios, encontraron según su abstract que dos evaluadores que miran lo mismo coinciden entre el 5 % y el 65 % de los problemas, con heurística, recorrido cognitivo o test con pensamiento en voz alta. Ningún método ni ningún evaluador solo da la lista completa: se combinan métodos y se hacen varias rondas.

> [!NOTE]
> Sin fuente todavía: el porcentaje de problemas que encuentran cinco evaluadores (circula "cerca de 75%") no se leyó en el paper de 1990. Las cifras y citas de NN/g salen de un resumen que una herramienta hizo de cada página: conviene cotejarlas en el original antes de entrecomillarlas.

## Qué leer

Para la lista y las descripciones completas, NN/g, [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/). Para el procedimiento, [How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/); conviene fijarse en el aviso de NN/g de que no sustituye a los usuarios. La fuente primaria para citar es Nielsen y Molich (1990) y Nielsen (1992).
