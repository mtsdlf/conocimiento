---
resumen: >-
  La evaluación adaptativa elige cada pregunta según las respuestas anteriores, para estimar lo que sabe una persona con menos preguntas. La reúnen tres comunidades que casi no se citan: la psicometría (teoría de respuesta al ítem y tests adaptativos), los tutores inteligentes (seguimiento del conocimiento) y la psicología matemática (espacios de conocimiento).
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, Computerized adaptive testing: https://en.wikipedia.org/wiki/Computerized_adaptive_testing"
  - "Cosyn, Doble, Falmagne et al. (2013), cap. 2 de Knowledge Spaces: Applications in Education, Springer: https://www.mheducation.com/content/dam/mhe/research/prek-12/essa-tier-4/aleks-assessing-learning-space.pdf"
  - "Corbett y Anderson (1994), Knowledge tracing, User Modeling and User-Adapted Interaction 4, 253-278: https://doi.org/10.1007/BF01099821"
  - "Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md"
aliases: [adaptive assessment, evaluación adaptativa, modelado del estudiante, student modeling, diagnóstico adaptativo]
creado: 2026-11-27
revisado:
---

# Evaluación adaptativa

La evaluación adaptativa elige cada pregunta según las respuestas anteriores, para estimar lo que sabe una persona con menos preguntas. La reúnen tres comunidades que casi no se citan: la psicometría (teoría de respuesta al ítem y tests adaptativos), los tutores inteligentes (seguimiento del conocimiento) y la psicología matemática (espacios de conocimiento).

Dentro de la [evaluación educativa](../evaluacion-educativa.md), es la parte que modela a cada persona en lugar de comparar a todas con la misma prueba. Sirve sobre todo al [diagnóstico](../Propositos/evaluacion-diagnostica.md) y a la práctica, y hereda los problemas de [confiabilidad](../Validez-confiabilidad-y-equidad/confiabilidad.md) de cualquier medida. El software que practica y repasa adaptándose a cada uno, y los tutores que guían paso a paso, son [tecnología educativa](../../Tecnologia-educativa/tecnologia-educativa.md); acá está la lógica de la medición.

## Tres comunidades, tres preguntas

| Comunidad | Qué estima | Con qué | Nota |
|---|---|---|---|
| Psicometría | Un número: la habilidad de la persona en una escala | Teoría de respuesta al ítem; test adaptativo computarizado | [Teoría de respuesta al ítem](teoria-de-respuesta-al-item.md) |
| Tutores inteligentes y minería de datos educativos | La probabilidad de que domine cada habilidad, y cómo cambia al practicar | Bayesian Knowledge Tracing; redes neuronales | [Seguimiento del conocimiento](seguimiento-del-conocimiento.md) |
| Psicología matemática | El conjunto de temas que domina y los que está listo para aprender | Grafo de prerrequisitos | [Espacios de conocimiento](espacios-de-conocimiento.md) |

La diferencia de fondo es qué devuelve el diagnóstico. La psicometría devuelve un puntaje y puede descartar una pregunta que correlaciona mal con el total aunque sea parte del currículo; los espacios de conocimiento devuelven una lista de temas y no la descartan (Cosyn et al., 2013). El seguimiento del conocimiento no mide una vez: actualiza la estimación con cada respuesta mientras la persona practica.

## Qué sobrevive con un grupo chico

Casi todo lo que se estudió de evaluación adaptativa es de matemática escolar y universitaria, con miles de personas. Las dos primeras comunidades necesitan datos: muchas respuestas para calibrar las preguntas o ajustar los parámetros. Con un curso de unas decenas de personas no se llega.

Lo que sí se lleva a un grupo chico es una idea por comunidad (inferencias del informe de esta base, no resultados medidos):

- De la psicometría, no gastar preguntas demasiado fáciles ni demasiado difíciles para esa persona: se puede hacer a mano con preguntas ordenadas por dificultad.
- Del seguimiento del conocimiento, que acertar no es saber: hace falta más de una evidencia antes de dar por dominada una habilidad.
- De los espacios de conocimiento, inferir por prerrequisitos: es lógica sobre un grafo y no necesita muestra.

Las tres juntas, con la pregunta por el primer paso de Kalyuga y Sweller, son el método de [evaluación diagnóstica](../Propositos/evaluacion-diagnostica.md) que propone esta base.

## Qué hay adentro

- [Teoría de respuesta al ítem](teoria-de-respuesta-al-item.md): en qué se diferencia de la teoría clásica, cuánta gente hace falta para calibrar y cómo funciona un test adaptativo computarizado.
- [Seguimiento del conocimiento](seguimiento-del-conocimiento.md): Bayesian Knowledge Tracing, su versión con redes neuronales y la disputa sobre cuál predice mejor.
- [Espacios de conocimiento](espacios-de-conocimiento.md): la teoría de Doignon y Falmagne, la frontera de lo que alguien está listo para aprender y la inferencia por prerrequisitos.
- [Sistemas de diagnóstico adaptativo](sistemas-de-diagnostico-adaptativo.md): dos sistemas comerciales basados en espacios de conocimiento y lo que publican de sí mismos (ficha, 2026-11).
