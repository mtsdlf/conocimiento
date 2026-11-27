---
resumen: >-
  La teoría de los espacios de conocimiento (Doignon y Falmagne) describe lo que sabe alguien como el conjunto de tipos de problema que puede resolver, ordenados por prerrequisitos. El diagnóstico busca la frontera: lo que ya domina y lo que está listo para aprender.
estado: vigente
estabilidad: estable
fuentes:
  - "Cosyn, Doble, Falmagne et al. (2013), Assessing mathematical knowledge in a learning space, cap. 2 de Falmagne et al. (eds.), Knowledge Spaces: Applications in Education, Springer: https://www.mheducation.com/content/dam/mhe/research/prek-12/essa-tier-4/aleks-assessing-learning-space.pdf"
  - "Doignon y Falmagne (2015), Knowledge spaces and learning spaces, arXiv:1511.06757 (abstract): https://arxiv.org/abs/1511.06757"
  - "Falmagne, Koppen, Villano, Doignon y Johannesen (1990), Introduction to knowledge spaces: How to build, test, and search them, Psychological Review 97(2):201-224 (texto completo): https://stat.cmu.edu/~brian/nynke/726-2021/project%20HCI%20Prereqs%20(Elaine,%20Smeet%20&%20Zhou)/2021-02-23/Falmagne90.pdf"
  - "Stefanutti y Cristante (s. f., ponencia en la 54.ª sesión del ISI), Empirical validation of a knowledge structure for assessment and learning of psychometrics at university level (texto completo): https://fpce.uc.pt/iase-web/documents/papers/isi54/3440.pdf"
  - "Doignon y Falmagne (1985), Spaces for the assessment of knowledge, International Journal of Man-Machine Studies; y Knowledge Spaces (1999), Springer (citados por Wikipedia): https://en.wikipedia.org/wiki/Knowledge_space"
  - "Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md"
  - "Evaluacion-educativa/.investigacion/fuentes-adaptativa-2026-11.md"
aliases: [knowledge space theory, KST, teoría de los espacios de conocimiento, learning space, espacio de aprendizaje, frontera de conocimiento, knowledge frontier, Doignon y Falmagne]
creado: 2026-11-27
revisado: 2026-11-27
---

# Espacios de conocimiento

La teoría de los espacios de conocimiento (Doignon y Falmagne) describe lo que sabe alguien como el conjunto de tipos de problema que puede resolver, ordenados por prerrequisitos. El diagnóstico busca la frontera: lo que ya domina y lo que está listo para aprender.

Es la rama de la [evaluación adaptativa](evaluacion-adaptativa.md) que viene de la psicología matemática, y la de mejor fuente en esa vertical. Es también la que mejor se traslada a un grupo chico, porque su regla central es lógica y no estadística. La [evaluación diagnóstica](../Propositos/evaluacion-diagnostica.md) de esta base se apoya en ella. El grafo de prerrequisitos de un curso, como pieza de diseño, es la [jerarquía de aprendizaje](../../Diseno-instruccional/Secuencia-y-curriculo/jerarquia-de-aprendizaje.md), de Diseño instruccional.

## Estados, espacios y frontera

Doignon y Falmagne la presentaron en 1985 y en el libro *Knowledge Spaces* (1999). Falmagne, Koppen, Villano, Doignon y Johannesen (1990) resumieron la teoría en *Psychological Review*. Allí el estado de conocimiento es el subconjunto de problemas «that the subject is capable of solving», y el espacio de conocimiento es la familia de todos los estados. Si dos conjuntos son estados, su unión también lo es. Según los autores, eso es coherente con que una noción se pueda aprender desde distintos prerrequisitos.

El capítulo de Cosyn et al. (2013), leído entero, define el estado de conocimiento como «the set of 'problem types' that the student is capable of solving». Los estados posibles forman un espacio de aprendizaje con dos principios:

1. Un estudiante puede llegar al estado de otro «by learning the missing concepts one at a time».
2. Todo concepto que uno está listo para aprender, el otro, si sabe más, ya lo domina o también está listo para aprenderlo.

De ahí sale un resultado: un estado queda definido por sus dos fronteras. La interna es lo último que la persona domina; la externa es «the set of problems that the student is ready to learn». Para enseñar, la externa es la que importa: dice qué sigue.

## Diagnosticar por prerrequisitos

El diagnóstico no devuelve un número sino una estructura, el estado. Según el abstract de Doignon y Falmagne (2015), es adaptativo porque usa las respuestas previas, y se apoya en procesos probabilísticos de tipo Markov.

La regla, en su forma simple: si alguien resuelve un problema, probablemente sabe sus prerrequisitos; si falla, probablemente no sabe lo que depende de él. Cada respuesta descarta muchos estados posibles a la vez, y por eso alcanzarían pocas preguntas para un curso con muchos temas (inferencia de esta base). No hace falta calibrar con cientos de personas como en la [teoría de respuesta al ítem](teoria-de-respuesta-al-item.md); hace falta un buen grafo.

El artículo de 1990 describe cómo armarlo. El primer esbozo sale de consultar a docentes expertos, con preguntas como esta: si alguien falló el problema A, ¿es prácticamente seguro que falle el B? Después el espacio se pone a prueba con respuestas reales y se ajusta. Para eso los autores usan una versión probabilística que admite errores por descuido («careless errors») y aciertos por suerte («lucky guesses»). Su ejemplo es una prueba de matemática de secundaria con «several hundred students»: con esos datos, la cantidad de estados posibles se redujo.

## Dónde choca con la psicometría

Cosyn et al. contrastan los dos enfoques. El test psicométrico busca un puntaje y puede descartar preguntas que correlacionan poco con el total aunque sean parte del currículo. El espacio de conocimiento las conserva, porque lo que se quiere saber es si la persona domina ese tema, no ordenarla. Los mismos autores reconocen que algunas preguntas de su sistema rinden mal y que no las eliminan por esa razón.

## Cómo falla

Las dos primeras son inferencias de esta base.

- El grafo está mal. Si un prerrequisito no lo es, la inferencia da por sabido lo que no se sabe. El costo de la teoría está en construir el grafo y las preguntas.
- Se infiere y no se confirma. Math Academy marca lo inferido como provisorio y retrocede si la persona se traba; ver la [ficha de sistemas](sistemas-de-diagnostico-adaptativo.md).
- Se aplica a lo que no tiene prerrequisitos claros. La evidencia es de matemática, donde el orden de los temas es firme. Que valga para un oficio técnico, donde el orden es más discutible, es una inferencia.

Hay una aplicación fuera de la matemática escolar, en un curso universitario de análisis de datos en psicología (Stefanutti y Cristante, ponencia leída entera). Cinco expertos armaron el espacio de 10 problemas de probabilidad, tablas de contingencia y análisis log-lineal, y 400 estudiantes los resolvieron. El modelo se aceptó en las dos mitades del test. En una, un problema de opción múltiple con cinco opciones dio una probabilidad de acierto por suerte de 0,78. Los autores concluyen que «either the model is not correct or the data for this item are unreliable».

> [!NOTE] Sin fuente todavía: Doignon y Falmagne (1985 y 1999) leídos en el original (se leyó su resumen de 1990), y una aplicación validada lejos de la matemática y la estadística, por ejemplo en un oficio técnico.
