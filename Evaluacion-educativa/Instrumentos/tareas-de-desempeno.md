---
resumen: >-
  Una tarea de desempeño pide hacer algo parecido a lo que se hace fuera del curso (resolver un caso, construir un programa, presentar un proyecto) y juzga el producto o el proceso. Gana realismo y pierde confiabilidad: cada tarea y cada corrector agregan ruido.
estado: vigente
estabilidad: estable
fuentes:
  - "AERA, APA y NCME (2014), Standards for Educational and Psychological Testing, cap. 2 Reliability/precision: https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf"
  - "Villarroel et al. (2018), revisión sistemática de evaluación auténtica, citada por Vlachopoulos (2025): https://www.eur.nl/en/media/2025-09-literaturereview-report"
  - "Messer, Brown, Kölling y Shi (2023), Automated Grading and Feedback Tools for Programming Education: A Systematic Review (resumen): https://arxiv.org/abs/2306.11722"
  - "Shavelson, Gao y Baxter (1993), Sampling variability of performance assessments, CSE Technical Report 361, CRESST/UCLA (texto completo; versión en Journal of Educational Measurement 30(3):215-232): https://cresst.org/wp-content/uploads/TECH361.pdf"
  - "Shavelson, Wiley y Ruiz-Primo (1999), Note on sources of sampling variability in science performance assessments, Journal of Educational Measurement 36(1):61-71 (resumen): https://nepc.colorado.edu/publication/note-on-sources-sampling-variability-science-performance-assessments"
  - "Messer, Brown, Kölling y Shi (2024), How consistent are humans when grading programming assignments?, preprint arXiv 2409.12967v3, sin revisión por pares (texto completo): https://arxiv.org/abs/2409.12967"
  - "Indriasari, Luxton-Reilly y Denny (2020), A review of peer code review in higher education, ACM Transactions on Computing Education 20(3):1-25 (abstract): https://doi.org/10.1145/3403935"
  - "Evaluacion-educativa/.investigacion/propositos-instrumentos-validez.md"
  - "Evaluacion-educativa/.investigacion/fuentes-propositos-instrumentos-2026-11.md"
aliases: [evaluación auténtica, authentic assessment, performance assessment, tarea auténtica, proyecto, portfolio, portafolio, corrección automática de código, autograding]
creado: 2026-11-27
revisado: 2026-11-27
---

# Tareas de desempeño

Una tarea de desempeño pide hacer algo parecido a lo que se hace fuera del curso (resolver un caso, construir un programa, presentar un proyecto) y juzga el producto o el proceso. Gana realismo y pierde confiabilidad: cada tarea y cada corrector agregan ruido.

Es el extremo auténtico de los [instrumentos](instrumentos.md), opuesto a la [opción múltiple](opcion-multiple.md). Casi siempre se corrige con una [rúbrica](rubrica.md), y su confiabilidad depende de cómo se [calibran los correctores](../Validez-confiabilidad-y-equidad/confiabilidad.md).

## Qué la hace auténtica

El término se usa mucho y se define poco. Según una revisión de 2025 que la cita, la revisión sistemática de Villarroel et al. (2018), sobre literatura de 1988 a 2015, encontró 13 características agrupadas en tres: realismo (la tarea se parece a la del trabajo o la vida), desafío cognitivo (pide usar el conocimiento, no repetirlo) y juicio evaluativo (quien aprende aprende a juzgar la calidad). La misma revisión dice que el campo «still lacks conceptual clarity». No se leyó Villarroel et al. en el original.

Los proyectos y los portfolios son formas de tarea de desempeño: el proyecto junta varias habilidades en un producto; el portfolio junta varios productos a lo largo del tiempo. Esta base no encontró investigación específica sobre portfolios y los trata como un caso de tarea de desempeño.

## El costo en confiabilidad

Los Standards (2014) piden reportar la confiabilidad de las tareas abiertas «over tasks, contexts, raters»: el puntaje varía según qué tarea tocó, en qué contexto y quién corrigió. Con un único proyecto final, el resultado dice mucho de ese proyecto y poco de lo que la persona haría con otro. Tres maneras de bajar ese ruido, inferidas de los Standards:

1. Más de una tarea, aunque sean más chicas.
2. Una rúbrica con criterios explícitos y ejemplos de cada nivel.
3. Una parte corregida por dos personas, para ver si coinciden.

## Cuántas tareas hacen falta

Un estudio de generalizabilidad mide cuánto del puntaje depende de la tarea, del corrector y de la ocasión. Shavelson, Gao y Baxter (1993) lo hicieron con tareas de ciencias y matemática en primaria y con tareas de trabajo en la Marina y la Infantería de Marina de Estados Unidos. Los correctores entrenados casi no agregaron error: «raters (e.g., teachers, job incumbents) can be trained to consistently judge performance on complex tasks». La fuente principal de error fue qué tarea tocó.

Con un corrector y una tarea, el coeficiente de generalizabilidad fue de 0,15 a 0,32 en los estudios escolares y de 0,12 y 0,19 en los militares. Para llegar a 0,80 hacían falta unas 23 tareas en el estudio de ciencias, 15 en el de matemática, 8 en el CAP (una evaluación del estado de California), 17 en la Marina y 35 en la Infantería de Marina.

Shavelson, Wiley y Ruiz-Primo (1999) revisaron esa lectura. Cronbach et al. (1997) habían objetado que la tarea y la ocasión estaban confundidas, porque cada tarea suele tomarse una sola vez. Según el resumen, el reanálisis apoyó la objeción: parte de la variación es de la tarea y parte de cómo rinde la persona de una ocasión a otra. Inferencia de esta base: en los dos análisis, un único proyecto dice poco de lo que la persona haría con otro.

## Corregir código y proyectos técnicos

Corregir programas con tests automáticos es lo que más hacen las herramientas de evaluación de programación. La revisión sistemática de Messer, Brown, Kölling y Shi (2023) analizó 121 artículos de 2017 a 2021. Según el resumen:

- La mayoría de las herramientas evalúa si el programa es correcto.
- Pocas evalúan legibilidad, mantenibilidad o documentación.
- Los tests de unidad sirven mal para el diseño y para las tareas abiertas, que son «nearly impossible to automatically assess using unit test-based approaches».

La consecuencia, como inferencia: el test automático es un buen instrumento para la parte cerrada de una tarea de programación (¿hace lo que tiene que hacer?) y un mal instrumento para la parte de oficio (¿está bien hecho?). Esa segunda parte vuelve al juicio humano con rúbrica, o a la [revisión entre pares](autoevaluacion-y-evaluacion-entre-pares.md). Corregir y devolver con IA no tiene nota en esta base; lo más cercano es [la IA como ayuda del docente](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-ayuda-del-docente.md), de Tecnología educativa, donde el modelo redacta y una persona aprueba.

El juicio humano sobre la calidad del código tampoco es parejo. En el preprint de Messer, Brown, Kölling y Shi (2024), 28 correctores con la misma rúbrica acordaron poco: un alfa de Krippendorff promedio de 0,2 en corrección y menor a 0,1 en elegancia, legibilidad y documentación. De los 22 que no notaron un trabajo repetido, solo uno le puso las mismas notas las dos veces. Choca con el resultado de Shavelson para correctores entrenados. Acá eran estudiantes de grado y posgrado con el perfil típico de un ayudante, y los autores piden entrenar a los correctores en la rúbrica. El detalle está en [rúbrica](rubrica.md).

Sobre la revisión de código entre estudiantes, Indriasari, Luxton-Reilly y Denny (2020) analizaron 51 estudios empíricos de educación superior. Según el abstract, entre los beneficios más citados está el desarrollo de habilidades de programación y entre las barreras, la poca participación de los estudiantes; y los resultados de aprendizaje informados necesitan «more empirical work» para validarse.

> [!NOTE] Sin fuente todavía: un estudio con revisión por pares sobre el acuerdo entre correctores de calidad de código, la confiabilidad de la revisión de código entre estudiantes como nota, y estudios de generalizabilidad con tareas de programación o con adultos en capacitación.
