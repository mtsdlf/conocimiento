---
resumen: >-
  La teoría de la carga cognitiva, de Sweller, explica por qué un material enseña más o menos según cuánto ocupa la memoria de trabajo en lo que no construye conocimiento. Es la base de las reglas de diseño de materiales, y su crítica más seria, de de Jong (2010), es que la carga casi nunca se mide directamente.
estado: borrador
estabilidad: estable
fuentes:
  - "Sweller (1988), Cognitive load during problem solving: effects on learning, Cognitive Science 12(2), 257-285: https://escholarship.org/content/qt2dp9867s/qt2dp9867s.pdf (resumen del buscador)"
  - "Sweller, van Merriënboer y Paas (2019), Cognitive Architecture and Instructional Design: 20 Years Later, Educational Psychology Review 31, 261-292, doi 10.1007/s10648-019-09465-5: https://link.springer.com/article/10.1007/s10648-019-09465-5 (resumen del buscador; no leído)"
  - "de Jong (2010), Cognitive load theory, educational research, and instructional design: some food for thought, Instructional Science 38(2), 105-134, doi 10.1007/s11251-009-9110-0: https://ris.utwente.nl/ws/files/6597420/Jong10cognitive.pdf"
  - "Mayer, respuesta a de Jong en el mismo número: https://link.springer.com/article/10.1007/s11251-009-9113-x (resumen del buscador)"
  - "Kalyuga, Ayres, Chandler y Sweller (2003), The expertise reversal effect, Educational Psychologist 38(1), 23-31: https://ro.uow.edu.au/edupapers/136 (resumen del buscador)"
  - "Diseno-instruccional/.investigacion/modelos-materiales-formatos.md"
  - "Didactica/.investigacion/posicion-contraria-y-mitos.md"
aliases: [cognitive load theory, CLT, teoría de la carga cognitiva, carga intrínseca, carga extrínseca, carga pertinente, germane load, Sweller, efecto del ejemplo resuelto]
creado: 2026-11-27
revisado:
---

# Carga cognitiva en el aprendizaje

La teoría de la carga cognitiva, de Sweller, explica por qué un material enseña más o menos según cuánto ocupa la memoria de trabajo en lo que no construye conocimiento. Es la base de las reglas de diseño de materiales, y su crítica más seria, de de Jong (2010), es que la carga casi nunca se mide directamente.

La definición, la distinción intrínseca y extrínseca vista desde una interfaz y la discusión sobre el «siete más o menos dos» están en [carga cognitiva](../../UX/Percepcion-y-decision/carga-cognitiva.md), del tema UX; no se repiten. Esta nota mira lo mismo desde el material didáctico: qué cambia cuando el objetivo no es usar una pantalla sino aprender. Dentro de [materiales y carga cognitiva](materiales-y-carga-cognitiva.md) es la teoría; las reglas concretas que salen de ella están en [principios multimedia](principios-multimedia.md).

## Las tres cargas en un material didáctico

El marco de tres cargas es de Sweller, van Merriënboer y Paas (1998), y la revisión de los mismos autores en 2019 lo mantiene, según el resumen del buscador:

| Carga | De dónde sale | Qué hace el diseño |
|---|---|---|
| Intrínseca | La dificultad del contenido: cuántos elementos hay que tener en mente a la vez porque interactúan | No se elimina; se dosifica con la [secuencia](../Secuencia-y-curriculo/secuencia-y-curriculo.md) y con conocimientos previos |
| Extrínseca | La forma del material: buscar, cruzar, descartar lo que no enseña | Se minimiza |
| Pertinente | El esfuerzo de construir esquemas, lo que de verdad enseña | Se optimiza dentro de la capacidad que queda |

La diferencia con la mirada de interfaz es la tercera fila. En una interfaz el ideal es que la tarea cueste poco; en un material didáctico, que cueste lo que tiene que costar. Un material que no exige nada tampoco enseña. Cómo redefine la revisión de 2019 la carga pertinente no se leyó.

## El primer hallazgo: ejemplos resueltos y metas abiertas

Sweller (1988) estudió la resolución de problemas. Para un novato, un problema con meta específica induce un análisis de medios y fines (buscar diferencias entre dónde está y adónde tiene que llegar) que ocupa la memoria de trabajo y deja poco para aprender el esquema. Quienes estudiaron ejemplos resueltos rindieron mejor después resolviendo problemas. Con una meta no específica también se aprende mejor, aunque ese efecto no aparece siempre y se puede revertir.

## Lo que sirve al novato estorba al que sabe

El efecto de inversión de la experticia (Kalyuga et al. 2003) fue, en parte, la respuesta de la escuela de Sweller a sus críticos: técnicas muy eficaces con novatos pierden eficacia, o la empeoran, con quien tiene más experiencia. El ejemplo resuelto es el caso típico. La consecuencia para los materiales es que no hay un material bueno en abstracto: hay un material bueno para un nivel de conocimiento previo, y por eso importa el [análisis de quien aprende](../Analisis-previo/analisis-de-quien-aprende.md).

## La crítica de de Jong

de Jong (2010) hace el inventario más citado de problemas de la teoría, en un artículo de acceso abierto:

- **La carga pertinente es circular.** La define como «quite tautological»: la carga buena es la que ayuda a aprender y la mala, la que no.
- **La carga casi no se mide.** En muchos estudios «there is no direct measurement of cognitive load»; se usa el resultado en una prueba de transferencia como medida indirecta. Cuando se mide, es con un cuestionario de esfuerzo mental de 9 puntos (la escala de Paas), con medidas fisiológicas como la variabilidad del ritmo cardíaco o con una doble tarea.
- **Las medidas no separan las cargas.** Son siempre relativas, un puntaje único no distingue intrínseca de extrínseca ni de pertinente, y los instrumentos más usados no captan cambios en el tiempo.
- **La explicación llega después.** «Attributing better performance on a post-test to a reduction of extraneous load, as most of these studies do, is a post-hoc explanation without direct evidence». Y como las medidas solo comparan condiciones, «all conditions in a study could show overload».

Otra objeción, según un resumen: que la carga intrínseca no se pueda cambiar con la instrucción es una premisa dudosa.

> [!IMPORTANT]
> **La teoría tiene problemas conceptuales y de medición serios (de Jong 2010).** La carga pertinente es tautológica y la carga casi no se mide.
>
> **La crítica es útil pero no cambia las reglas (Mayer, en el mismo número).** Según el resumen del buscador, Mayer la calificó de «detailed, comprehensive, and systematic» y coincidió en mejorar definiciones y medidas. Otro resumen le atribuye haberla llamado «mainly a catalogue of criticisms» sin dirección; esa cita no se verificó. La discusión es sobre el balance entre críticas y propuestas, no sobre si los problemas existen.

Las respuestas posteriores a de Jong, como instrumentos que intentan medir las tres cargas por separado, no se buscaron.

## Qué queda en pie para diseñar

Las reglas que la teoría inspiró, quitar lo que no enseña, poner juntas las cosas que hay que mirar juntas, dar ejemplos resueltos a quien empieza, tienen su propia evidencia experimental en [principios multimedia](principios-multimedia.md), independiente de que la explicación de por qué funcionan esté bien medida. Esa separación entre regla y explicación es una lectura de esta base.
