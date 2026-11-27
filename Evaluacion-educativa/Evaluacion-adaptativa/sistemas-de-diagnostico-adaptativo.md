---
resumen: >-
  Dos sistemas comerciales de diagnóstico adaptativo (ALEKS, basado en espacios de conocimiento, y Math Academy, con un grafo de prerrequisitos y una frontera de conocimiento), con lo que publican de su método y de su exactitud, copiado en 2026-11. Lo que dicen de sí mismos tiene conflicto de interés.
estado: vigente
estabilidad: volatil
fuentes:
  - "Cosyn, Doble, Falmagne et al. (2013), cap. 2 de Knowledge Spaces: Applications in Education, Springer, publicado por la editora de ALEKS: https://www.mheducation.com/content/dam/mhe/research/prek-12/essa-tier-4/aleks-assessing-learning-space.pdf"
  - "Doignon y Falmagne (2015), arXiv:1511.06757 (abstract): https://arxiv.org/abs/1511.06757"
  - "Math Academy, How our AI works (resumen de herramienta): https://mathacademy.com/how-our-ai-works"
  - "Math Academy, How it works: https://www.mathacademy.com/how-it-works (leída 2026-11-27)"
  - "Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md"
  - "Tecnologia-educativa/.investigacion/fuentes-ia-y-practica-adaptativa-2026-11.md"
creado: 2026-11-27
revisado: 2026-11-27
---

# Sistemas de diagnóstico adaptativo

Dos sistemas comerciales de diagnóstico adaptativo (ALEKS, basado en espacios de conocimiento, y Math Academy, con un grafo de prerrequisitos y una frontera de conocimiento), con lo que publican de su método y de su exactitud, copiado en 2026-11. Lo que dicen de sí mismos tiene conflicto de interés.

ALEKS implementa los [espacios de conocimiento](espacios-de-conocimiento.md); Math Academy usa una idea cercana, y sus fuentes no dicen que se base en esa teoría. Copiado de las fuentes de arriba el 2026-11-27.

| | ALEKS | Math Academy |
|---|---|---|
| Base teórica | Espacios de conocimiento; entre los autores del capítulo está Falmagne | Grafo de prerrequisitos y «knowledge frontier» |
| Qué devuelve el diagnóstico | El estado de conocimiento y sus dos fronteras | La frontera; lo apenas superado queda «conditionally completed» |
| Cómo infiere | Procesos probabilísticos tipo Markov sobre el espacio | Un acierto cuenta como evidencia del tema y sus prerrequisitos; un error, de que no se sabe el tema ni lo que depende de él; un acierto muy lento pesa menos |
| Escala | Millones de estudiantes, según Doignon y Falmagne (2015) | 500 a 1.000 temas por curso; dice reducir las preguntas «an order of magnitude» frente a un enfoque ingenuo |
| Datos de exactitud publicados | Sobre 1.940.473 experiencias de aprendizaje, «the median probability of learning success was .93» | No publica |
| Conflicto de interés | El capítulo lo escribieron empleados de la empresa que vende el sistema | Página de producto |

Según la página «How it works» de Math Academy, leída el 2026-11-27, el diagnóstico adaptativo «will take approximately 30 to 45 minutes». En la lectura de esta base, la página no dice cuántas preguntas tiene. El repaso que el sistema programa después del diagnóstico está en la ficha de [herramientas de práctica adaptativa](../../Tecnologia-educativa/Practica-adaptativa/herramientas-de-practica-adaptativa.md#math-academy).
