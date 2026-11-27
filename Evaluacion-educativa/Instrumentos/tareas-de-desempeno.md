---
resumen: >-
  Una tarea de desempeño pide hacer algo parecido a lo que se hace fuera del curso (resolver un caso, construir un programa, presentar un proyecto) y juzga el producto o el proceso. Gana realismo y pierde confiabilidad: cada tarea y cada corrector agregan ruido.
estado: borrador
estabilidad: estable
fuentes:
  - "AERA, APA y NCME (2014), Standards for Educational and Psychological Testing, cap. 2 Reliability/precision: https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf"
  - "Villarroel et al. (2018), revisión sistemática de evaluación auténtica, citada por Vlachopoulos (2025): https://www.eur.nl/en/media/2025-09-literaturereview-report"
  - "Messer, Brown, Kölling y Shi (2023), Automated Grading and Feedback Tools for Programming Education: A Systematic Review (resumen): https://arxiv.org/abs/2306.11722"
  - "Evaluacion-educativa/.investigacion/propositos-instrumentos-validez.md"
aliases: [evaluación auténtica, authentic assessment, performance assessment, tarea auténtica, proyecto, portfolio, portafolio, corrección automática de código, autograding]
creado: 2026-11-27
revisado:
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

## Corregir código y proyectos técnicos

Corregir programas con tests automáticos es la forma más común de evaluar programación a escala. La revisión sistemática de Messer, Brown, Kölling y Shi (2023) analizó 121 artículos de 2017 a 2021. Según el resumen:

- La mayoría de las herramientas evalúa si el programa es correcto.
- Pocas evalúan legibilidad, mantenibilidad o documentación.
- Los tests de unidad sirven mal para el diseño y para las tareas abiertas, que son «nearly impossible to automatically assess using unit test-based approaches».

La consecuencia, como inferencia: el test automático es un buen instrumento para la parte cerrada de una tarea de programación (¿hace lo que tiene que hacer?) y un mal instrumento para la parte de oficio (¿está bien hecho?). Esa segunda parte vuelve al juicio humano con rúbrica, o a la [revisión entre pares](autoevaluacion-y-evaluacion-entre-pares.md). Corregir y devolver con IA no tiene nota en esta base; lo más cercano es [la IA como ayuda del docente](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-ayuda-del-docente.md), de Tecnología educativa, donde el modelo redacta y una persona aprueba.

> [!NOTE] Sin fuente todavía: la confiabilidad entre correctores de rúbricas de calidad de código, la revisión de código como instrumento de evaluación, y cuántas tareas hacen falta para generalizar (estudios de generalizabilidad).
