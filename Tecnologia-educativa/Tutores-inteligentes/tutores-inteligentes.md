---
resumen: >-
  Un tutor inteligente es un programa que guía a quien aprende paso a paso dentro de un problema: sigue cada acción, estima qué sabe y decide qué pista dar y qué problema poner después. Es la familia de tecnología educativa con más evidencia, y la base de los tutores con IA.
estado: borrador
estabilidad: estable
fuentes:
  - "Ma, Adesope, Nesbit y Liu (2014), Intelligent tutoring systems and learning outcomes: A meta-analysis, Journal of Educational Psychology 106(4):901-918: https://www.cs.uky.edu/~sgware/reading/papers/ma2014intelligent.pdf"
  - "VanLehn (2011), The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems, Educational Psychologist 46(4):197-221: https://eric.ed.gov/?id=EJ946764 (abstract)"
  - "Pane, Griffin, McCaffrey y Karam (2014), Effectiveness of Cognitive Tutor Algebra I at Scale, EEPA 36(2), vía RAND: https://www.rand.org/pubs/research_briefs/RB9746.html"
  - "Tecnologia-educativa/.investigacion/medios-en-linea-tutores.md"
aliases: [intelligent tutoring system, ITS, sistemas de tutoría inteligente, tutor cognitivo, cognitive tutor]
creado: 2026-11-27
revisado:
---

# Tutores inteligentes

Un tutor inteligente es un programa que guía a quien aprende paso a paso dentro de un problema: sigue cada acción, estima qué sabe y decide qué pista dar y qué problema poner después. Es la familia de tecnología educativa con más evidencia, y la base de los tutores con IA.

Dentro de [Tecnología educativa](../tecnologia-educativa.md) es la parte que intenta automatizar lo que hace un tutor humano. Le presta su arquitectura y su escalera de pistas a [IA en la educación](../IA-en-la-educacion/ia-en-la-educacion.md): un tutor con un modelo de lenguaje que no regala respuestas está haciendo, con otra tecnología, lo que estos sistemas hacen desde los años 80. Le presta su estimación de lo que sabe cada alumno a la [práctica adaptativa](../Practica-adaptativa/practica-adaptativa.md). La [tutoría](../../Didactica/Tutoria-y-mentoria/tutoria.md) humana, con la que se los compara, está en Didáctica.

## Cómo trabaja un tutor inteligente

El sistema se arma con cuatro piezas: un modelo de lo que hay que saber (el dominio), un modelo de lo que sabe este alumno, un modelo pedagógico que decide qué hacer y una interfaz. En los tutores cognitivos, el trazado de modelo compara cada paso del alumno con las rutas de solución posibles, y el trazado de conocimiento estima qué habilidades ya domina para elegir el próximo problema. Las piezas y su historia, desde SCHOLAR (1970), están en [arquitectura de un tutor inteligente](arquitectura-de-un-tutor-inteligente.md).

La pieza más visible del modelo pedagógico es la [escalera de pistas](pistas-de-un-tutor-inteligente.md): primero una pista general, después una más concreta y al final la que da el paso. Su riesgo conocido es que el alumno la baje hasta el fondo sin pensar; su matiz, que esa última pista puede funcionar como ejemplo resuelto si se la lee.

## Cuánto enseñan

Los metaanálisis dan efectos de medianos a grandes. Ma et al. (2014) encontraron una ventaja de g = 0,42 frente a la clase grupal dirigida por un docente y ninguna diferencia significativa frente a la tutoría humana individual. VanLehn (2011), según su resumen, estimó d = 0,76 para los tutores inteligentes y d = 0,79 para la tutoría humana.

El mejor ensayo a escala da menos. En el ensayo aleatorizado de Pane et al. (2014) con el Cognitive Tutor de Álgebra en 147 escuelas, el efecto en secundaria fue nulo el primer año y de unas 0,20 desviaciones estándar el segundo, según RAND. La distancia entre una cifra y otra es la lección de la vertical, y está en [evidencia de los tutores inteligentes](evidencia-de-los-tutores-inteligentes.md).

Todo lo medido es escolar o universitario, y el ensayo a escala es de álgebra. Que funcione igual para un adulto que aprende un oficio técnico es inferencia de esta base.

## Qué hay adentro de los tutores inteligentes

- [Arquitectura de un tutor inteligente](arquitectura-de-un-tutor-inteligente.md): las cuatro piezas, el trazado de modelo y de conocimiento, y la historia de SCHOLAR al Cognitive Tutor.
- [Pistas de un tutor inteligente](pistas-de-un-tutor-inteligente.md): cómo el modelo pedagógico gradúa la ayuda, cuándo bajar hasta la última pista es abuso y cuándo es estudiar un ejemplo.
- [Evidencia de los tutores inteligentes](evidencia-de-los-tutores-inteligentes.md): los metaanálisis de VanLehn, Ma y Kulik y Fletcher frente al ensayo a escala de Pane, con las discrepancias a la vista.
