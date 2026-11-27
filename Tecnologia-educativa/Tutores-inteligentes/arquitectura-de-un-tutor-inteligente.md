---
resumen: >-
  Un tutor inteligente se arma con cuatro piezas: un modelo del dominio (lo que hay que saber), un modelo del estudiante (lo que este alumno sabe), un modelo pedagógico (qué hacer ahora) y una interfaz. La historia que sigue arranca con SCHOLAR (1970) y los tutores cognitivos de Carnegie Mellon (principios de los 80).
estado: borrador
estabilidad: estable
fuentes:
  - "Ma, Adesope, Nesbit y Liu (2014), Journal of Educational Psychology 106(4):901-918, DOI 10.1037/a0037123: https://www.cs.uky.edu/~sgware/reading/papers/ma2014intelligent.pdf"
  - "Wikipedia, Cognitive tutor: https://en.wikipedia.org/wiki/Cognitive_tutor (terciaria; cita a Anderson, Corbett, Koedinger y Pelletier 1995, Journal of the Learning Sciences 4(2):167-207, no leído)"
  - "Tecnologia-educativa/.investigacion/medios-en-linea-tutores.md"
aliases: [ITS architecture, arquitectura ITS, modelo del estudiante, student model, modelo del dominio, modelo pedagógico, model tracing, knowledge tracing, trazado de modelo, trazado de conocimiento, Cognitive Tutor, SCHOLAR, ACT-R]
creado: 2026-11-27
revisado:
---

# Arquitectura de un tutor inteligente

Un tutor inteligente se arma con cuatro piezas: un modelo del dominio (lo que hay que saber), un modelo del estudiante (lo que este alumno sabe), un modelo pedagógico (qué hacer ahora) y una interfaz. La historia que sigue arranca con SCHOLAR (1970) y los tutores cognitivos de Carnegie Mellon (principios de los 80).

> [!NOTE]
> La división en cuatro piezas y el detalle de los tutores cognitivos salen de Wikipedia, que cita a Wenger (1987), Self (1990) y Koedinger y Corbett (2006). Falta verificarlo en una fuente primaria, como Wenger o Nkambou et al. (2010), y en Anderson et al. (1995).

## Las cuatro piezas

| Pieza | Qué guarda o decide | Ejemplo en un problema de álgebra |
|---|---|---|
| Modelo del dominio | Las reglas y las rutas de solución correctas, y los errores típicos | Los pasos válidos para despejar una incógnita |
| Modelo del estudiante | Qué habilidades domina este alumno, estimado a partir de sus pasos | «Domina pasar términos, no domina dividir por un coeficiente» |
| Modelo pedagógico (o del tutor) | Qué hacer ahora: dejar seguir, marcar un error, dar una pista, elegir el próximo problema | Dar la primera pista de la [escalera](pistas-de-un-tutor-inteligente.md) |
| Interfaz | Por dónde entran los pasos del alumno y salen las respuestas del tutor | El editor donde se escribe cada paso |

La columna de ejemplos es ilustración de esta base, no sale de las fuentes.

## Seguir cada paso: trazado de modelo y de conocimiento

Un tutor inteligente se distingue de un ejercicio con corrección automática porque mira cada paso y no solo la respuesta final. En los tutores cognitivos, el trazado de modelo (*model tracing*) compara cada acción del alumno con las rutas de solución del modelo del dominio: si el paso está en una ruta válida, el tutor lo deja seguir; si coincide con un error conocido, puede marcarlo en ese momento.

El trazado de conocimiento (*knowledge tracing*) actualiza el modelo del estudiante. Con un modelo bayesiano estima, después de cada paso, la probabilidad de que el alumno ya haya aprendido cada habilidad, y con esa estimación elige el próximo problema. Como lectura de esta base, es el mismo principio que usa la [práctica adaptativa](../Practica-adaptativa/sistemas-adaptativos.md) para decidir qué practicar.

Ma et al. (2014) compararon formas de modelar al estudiante: los tutores con trazado de modelo dieron un efecto de 0,35, y los basados en modelos de restricciones, de 0,24.

## De SCHOLAR al Cognitive Tutor

Ma et al. abren la historia con SCHOLAR, de Carbonell (1970), «often regarded as the first ITS». Lo destacan porque su arquitectura ya separaba la representación del dominio de la interfaz en lenguaje natural: la idea de piezas separadas está desde el principio.

Los tutores cognitivos nacieron a principios de los 80 en Carnegie Mellon para poner a prueba la teoría ACT-R de John Anderson. Los primeros fueron un tutor de demostraciones de geometría y uno de programación en LISP. El curso de Álgebra se creó a principios de los 90 y hacia 1999 estaba en 75 escuelas de Estados Unidos; Carnegie Learning es la empresa que salió de ese trabajo. Es el tutor del ensayo a escala de Pane et al., en [evidencia de los tutores inteligentes](evidencia-de-los-tutores-inteligentes.md).

## Qué heredan los tutores con IA

Un tutor con un modelo de lenguaje no tiene, de fábrica, un modelo del dominio verificado ni un modelo del estudiante: genera texto probable a partir de lo que tiene en su ventana, como explica [Modelos](../../IA/Modelos/modelos.md) en el tema IA. Lo que los ensayos con IA que funcionaron agregaron se parece a estas piezas, como lectura de esta base: Kestin et al. (2025) le dieron al tutor soluciones escritas por docentes, que hacen de modelo del dominio, y Khan Academy encontró que lo que mejora su tutor es darle el historial del alumno, que hace de modelo del estudiante. Los dos casos están en [la IA como tutor](../IA-en-la-educacion/ia-como-tutor.md) y en [modos de estudio de la IA](../IA-en-la-educacion/modos-de-estudio-de-la-ia.md).
