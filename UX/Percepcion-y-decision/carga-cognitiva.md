---
resumen: >-
  La carga cognitiva de una interfaz es el esfuerzo mental que exige usarla. Se reduce quitando el procesamiento que no ayuda a la tarea, y no depende de un número mágico de elementos por pantalla.
estado: vigente
estabilidad: estable
fuentes:
  - "George A. Miller (1956), The Magical Number Seven, Plus or Minus Two, Psychological Review 63, 81-97: https://psychclassics.yorku.ca/Miller/"
  - "Nelson Cowan (2001), The magical number 4 in short-term memory, Behavioral and Brain Sciences 24(1), 87-114: https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf (abstract e introducción)"
  - "John Sweller (1988), Cognitive load during problem solving, Cognitive Science 12(2), 257-285: https://dc2.philarchive.org/rec/SWECLD (solo abstract y resúmenes)"
  - "Sweller, van Merriënboer y Paas (2019), Cognitive Architecture and Instructional Design: 20 Years Later, Educational Psychology Review 31, 261-292: https://link.springer.com/article/10.1007/s10648-019-09465-5 (solo metadatos)"
  - "NN/g, Kathryn Whitenton, Minimize Cognitive Load to Maximize Usability (22 de diciembre de 2013): https://www.nngroup.com/articles/minimize-cognitive-load/"
  - "NN/g, Raluca Budiu, Recognition vs. Recall (2024): https://www.nngroup.com/articles/recognition-and-recall/"
  - "UX/.investigacion/percepcion-y-decision.md y UX/.investigacion/posicion-contraria.md"
aliases: [cognitive load, carga mental, memoria de trabajo, regla de 7±2, número mágico siete]
creado: 2026-11-22
revisado: 2026-11-22
---

# Carga cognitiva

La carga cognitiva de una interfaz es el esfuerzo mental que exige usarla. Se reduce quitando el procesamiento que no ayuda a la tarea, y no depende de un número mágico de elementos por pantalla.

NN/g la define así: "the cognitive load imposed by a user interface is the amount of mental resources that is required to operate the system". La idea viene de la teoría de la carga cognitiva de Sweller, nacida en la educación (aprendizaje con resolución de problemas); la teoría en su terreno de origen está en [carga cognitiva en el aprendizaje](../../Diseno-instruccional/Materiales-y-carga-cognitiva/carga-cognitiva-en-el-aprendizaje.md), de Diseño instruccional. Su aplicación a interfaces es una extrapolación de practicantes: no se encontró evidencia empírica de carga cognitiva específica en interfaces web.

## Carga intrínseca y carga extrínseca

NN/g distingue dos clases:

- Intrínseca: el esfuerzo de absorber información nueva y de seguir la propia meta. No se elimina, porque es la tarea misma.
- Extrínseca: el procesamiento que consume recursos sin ayudar a entender el contenido. El ejemplo de NN/g son los estilos de fuente decorativos.

Bajar la carga es atacar la extrínseca, la que no se justifica por la tarea. Esta base lee que un [modelo mental](modelo-mental.md) correcto la baja, y que reconocer en vez de recordar (heurística 6 de Nielsen) también; es inferencia de las notas de investigación.

> [!IMPORTANT] La carga pertinente (germane) parece haber cambiado de definición dentro de la escuela de Sweller; la fuente es solo una reseña de 2020 vista por el buscador. El marco de tres cargas (intrínseca, extrínseca y pertinente) es de Sweller, van Merriënboer y Paas (1998), y el texto de 2019 de los mismos autores lo revisa. NN/g omite la pertinente y no cita a Sweller. Sweller (1988), según su abstract, atribuye la carga extrínseca a buscar diferencias entre el estado actual y la meta, y recomienda ejemplos resueltos. En UX se usa casi solo la oposición intrínseca/extrínseca; cómo define exactamente la pertinente la versión de 2019 no se leyó.

## Cuántos elementos retiene la memoria

La regla "7±2" sale de Miller (1956), y la evidencia posterior la corrige. Miller aclara que el siete vale para juicios unidimensionales ("this magical number seven applies to one-dimensional judgments") y resume: "Absolute judgment is limited by the amount of information. Immediate memory is limited by the number of items". Lo constante en la memoria inmediata es el número de chunks, y el recodificado agrupa en menos chunks con más información cada uno.

> [!IMPORTANT] Miller dice 7±2 (1956); Cowan dice cerca de 4 (2001). Las dos son fuentes de primera mano y Cowan revisa a Miller. Según su abstract, el número de Miller "was meant more as a rough estimate and a rhetorical device than as a real capacity limit", el límite real es "only three to five chunks" y hay "a single, central capacity limit averaging about four chunks". Cowan agrega que lo central en Miller era el agrupamiento y no el número, y que el límite se observa bajo cuatro condiciones, entre ellas impedir el recodificado. La cifra depende de qué cuente como chunk. Esta base usa "unos cuatro".

## Por qué 7±2 no manda sobre los menús

El límite de la memoria de trabajo, con la disputa sobre si es uno solo o varios, está en [memoria](../../Psicologia/Aprendizaje-y-memoria/memoria.md), en Psicología.

Es frecuente limitar un menú a siete ítems por la memoria a corto plazo. Lo medido por Miller y Cowan es cuántos ítems se retienen y se recuerdan, y un menú visible se reconoce: no hay que retenerlo. Esta es una inferencia a partir de las definiciones de Miller y de NN/g sobre reconocimiento. La idea de que NN/g mismo llama error a ese uso solo llegó por una cita en un blog; el artículo de NN/g no se encontró. Su texto sobre la regla de los tres clics sí presenta "no más de 7 categorías de navegación principal" como un mito. Un artículo de 2002 de Dr. Dobb's (secundario) dice que el número óptimo de ítems no se reduce a una regla general. Cómo se organiza un menú es asunto de [Navegación](../Arquitectura-de-informacion/navegacion.md); para el tiempo de elegir entre opciones, [las leyes de Fitts y Hick](leyes-de-fitts-y-hick.md).

## Dónde leer más

Cowan (2001), abstract y sección 1, para el límite de capacidad. Miller (1956), la parte sobre chunking y recoding, para lo que dijo. NN/g, "Minimize Cognitive Load", como puente a diseño. Conviene fijarse en que lo medido es la memoria de trabajo para ítems retenidos, y no cuántos elementos puede mostrar una pantalla.

## Qué falta

La memoria de largo plazo y el aprendizaje (cómo una persona construye esquemas con el uso) son un componente aún no escrito, nombrado en [Percepción y decisión](percepcion-y-decision.md).
