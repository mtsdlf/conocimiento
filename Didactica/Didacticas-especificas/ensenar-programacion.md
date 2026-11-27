---
resumen: >-
  Enseñar programación tiene una didáctica propia, la investigación en educación en computación, que propone leer y trazar código antes de escribirlo, nombrar los subobjetivos de cada procedimiento y hacer explícito cómo ejecuta la máquina. Casi toda su evidencia es de cursos introductorios universitarios y escolares.
estado: vigente
estabilidad: semi
fuentes:
  - "Fincher y Robins (eds.) (2019), The Cambridge Handbook of Computing Education Research, caps. 12 y 15: https://www.cambridge.org/core/product/F8CFAF7B81A8F6BF5C663412BA0A943D (según resumen)"
  - "Luxton-Reilly et al. (2018), Introductory programming: a systematic literature review, ITiCSE Companion, DOI 10.1145/3293881.3295779 (solo metadatos)"
  - "Lister et al. (2004), ITiCSE working group, DOI 10.1145/1044550.1041673 (solo metadatos)"
  - "Lopez, Whalley, Robbins y Lister (2008), Relationships between reading, tracing and writing skills in introductory programming, ICER '08:101-112, DOI 10.1145/1404520.1404531: https://opus.lib.uts.edu.au/bitstream/10453/10806/1/2008001530.pdf (texto completo, repositorio de la UTS)"
  - "Xie, Nelson y Ko (2018), An Explicit Strategy to Scaffold Novice Program Tracing, SIGCSE '18:344-349, DOI 10.1145/3159450.3159527: https://faculty.washington.edu/ajko/papers/Xie2018TracingStrategies.pdf (texto completo, sitio del autor)"
  - "Margulieux, Morrison y Decker (2020), International Journal of STEM Education 7, art. 19: https://link.springer.com/article/10.1186/s40594-020-00222-7 (abstract)"
  - "Sentance, Waite y Kallia (2019), PRIMM, Computer Science Education 29(2-3), DOI 10.1080/08993408.2019.1608781 (solo metadatos)"
  - "Ericson et al. (2022), Parsons Problems and Beyond, ITiCSE Working Group Reports, DOI 10.1145/3571785.3574127 (solo metadatos)"
  - "Sorva (2013), Notional Machines and Introductory Programming Education, ACM TOCE 13(2), DOI 10.1145/2483710.2483713 (abstract)"
  - "Selvaraj, Zhang, Porter y Soosai Raj (2021), Live Coding: A Review of the Literature, ITiCSE: https://par.nsf.gov/biblio/10313400-live-coding-review-literature (abstract)"
  - "Porter, Bailey Lee y Simon (2013), Halving fail rates using peer instruction: a study of four computer science courses, SIGCSE '13:177-182, DOI 10.1145/2445196.2445250: https://files.software-carpentry.org/training-course/2012/08/porter-halving-fail-peer-instruction-2013.pdf (texto completo, preimpresión)"
  - "Didactica/.investigacion/indagacion-tutoria-especificas.md"
  - "Didactica/.investigacion/explicita-practica-preguntas-feedback.md"
  - "Didactica/.investigacion/fuentes-didacticas-especificas-2026-11.md"
  - "Didactica/.investigacion/fuentes-explicar-y-practica-guiada-2026-11.md"
aliases: [didáctica de la programación, enseñanza de la programación, computing education, educación en computación, CS education, teaching programming]
creado: 2026-11-27
revisado: 2026-11-27
---

# Enseñar programación

Enseñar programación tiene una didáctica propia, la investigación en educación en computación, que propone leer y trazar código antes de escribirlo, nombrar los subobjetivos de cada procedimiento y hacer explícito cómo ejecuta la máquina. Casi toda su evidencia es de cursos introductorios universitarios y escolares.

Dentro de [Didácticas específicas](didacticas-especificas.md) es la materia con más literatura verificada. El problema que la motiva aparece en el abstract de Margulieux et al. (2020): las tasas de abandono y reprobación en los cursos introductorios de programación «are regularly as high as 50%». El mapa del campo es *The Cambridge Handbook of Computing Education Research* (Fincher y Robins, 2019): para quien enseña, los capítulos 12, sobre programadores novatos y la programación introductoria, y 15, sobre enfoques pedagógicos. La revisión sistemática de Luxton-Reilly et al. (2018) cubre la programación introductoria; no se leyó.

## Leer y trazar antes de escribir

Lister et al. (2004) y Lopez et al. (2008) se citan para la idea de que la habilidad de escribir código se apoya en la de leerlo y trazarlo: predecir qué hace un fragmento, paso a paso. De Lister et al. solo se verificaron título, lugar de publicación y autores.

Lopez et al. (2008) analizaron el examen final de un primer semestre de Java: 38 de los 78 alumnos dieron permiso para usar sus respuestas. Trazar código con bucles se correlacionó con escribir código (r = 0,6267) y explicó el 39 % de la variabilidad. Explicar un fragmento «in plain English» se correlacionó 0,5586 y explicó el 31 %. Juntas, las dos habilidades explican el 46 % de la varianza de escribir. Los autores aclaran que esas covarianzas «are not, alone, evidence of causality»: es una correlación en un examen, no un experimento.

Xie, Nelson y Ko (2018) sí hicieron un experimento. Enseñaron en 5 a 10 minutos una estrategia de trazado explícita: seguir el código línea por línea y anotar en una tabla de memoria el valor de cada variable. Participaron 24 novatos de un primer curso universitario, asignados por bloques al azar. Con la estrategia, sacaron en promedio un 15 % más en los problemas de trazado (p = 0,049) y con 46 % menos variabilidad. En el parcial del curso, los 8 del grupo con estrategia que informaron su nota sacaron un 7 % más, una diferencia que no llegó a ser significativa (p = 0,083). La muestra es chica.

La idea encaja con el resto del tema: leer un programa que funciona es estudiar un [ejemplo resuelto](../Explicar-y-modelar/modelado-y-ejemplos-resueltos.md), y pedir que se prediga la salida antes de ejecutarla es una [pregunta de proceso](../Preguntas-y-dialogo/preguntas-en-clase.md).

## Subobjetivos nombrados

Margulieux, Morrison y Decker (2020) hicieron un cuasiexperimento en un curso introductorio de un semestre con 265 estudiantes: la mitad recibió instrucción con subobjetivos nombrados (cada procedimiento partido en pasos con un nombre que dice para qué sirve; definición de esta base) y la otra mitad, la habitual. Según el abstract, el grupo con subobjetivos sacó mejores notas en los cuestionarios formativos, tomados dentro de la semana en que se aprendía cada procedimiento, pero no en los exámenes finales. Tuvo menor varianza de notas y menos abandonos y reprobados; según el resumen de un buscador, con un efecto mayor en los estudiantes en riesgo. No hay tamaños de efecto.

Junto con Xie et al. (2018), es uno de los pocos estudios de programación de esta base con un resultado medido contra un grupo de comparación. La técnica es una forma de [modelado](../Explicar-y-modelar/modelado-y-ejemplos-resueltos.md): hace visible la estructura que el experto ve y el novato no.

## Del código ajeno al propio: PRIMM y problemas de Parsons

- **PRIMM** (Sentance, Waite y Kallia, 2019) ordena la clase en los cinco pasos de su sigla en inglés (*predict, run, investigate, modify, make*): predecir, ejecutar, investigar, modificar y crear; el desglose de la sigla es ilustrativo, de esta base: no se leyó el artículo. Es la secuencia de [práctica guiada y andamiaje](../Practica-guiada-y-andamiaje/practica-guiada-y-andamiaje.md) aplicada al código: primero se lee y se predice, al final se escribe solo. Los detalles del estudio (escuelas, cantidad y edad de alumnos) no se verificaron; es evidencia escolar, no de adultos.
- **Problemas de Parsons**: en su forma habitual se dan las líneas de una solución desordenadas y hay que ordenarlas (descripción ilustrativa de esta base, sin fuente leída). Ericson et al. (2022) revisan esa literatura en un grupo de trabajo de ITiCSE; su contenido no se leyó.

## La máquina nocional

Sorva (2013) llama máquina nocional a la versión simplificada de la computadora que quien programa necesita para entender qué pasa al ejecutarse un programa en un lenguaje dado. Según el abstract, argumenta que las máquinas nocionales son un desafío mayor de la programación introductoria y que quien enseña debería convertirlas en un objetivo de aprendizaje explícito. Es una revisión con posición, no un experimento. Es un ejemplo de [conocimiento pedagógico del contenido](conocimiento-pedagogico-del-contenido.md): saber qué modelo de ejecución le falta al novato.

## Programar en vivo y aprender entre pares

- **Programar en vivo** (*live coding*): escribir código frente al grupo, con los errores y las correcciones a la vista. Selvaraj et al. (2021) revisaron la literatura y concluyen que «there is a lack of empirical evidence to support claims about the effectiveness of live coding on student learning», aunque se recomienda como una de las mejores prácticas. Lo que sí tiene respaldo general es el [modelado](../Explicar-y-modelar/modelado-y-ejemplos-resueltos.md) y el pensar en voz alta; programar en vivo es una forma de hacerlo. Las dos comparaciones con código ya escrito que se leyeron, por su abstract, lo encuentran igual o apenas mejor (Rubin 2013) o sin mejora (Shah et al. 2023); el detalle está en [modelado y ejemplos resueltos](../Explicar-y-modelar/modelado-y-ejemplos-resueltos.md).
- **[Instrucción entre pares](../../Ciencias-del-aprendizaje/Aprender-con-otros/instruccion-entre-pares.md)** (*peer instruction*): en su forma habitual, una pregunta conceptual, votación individual, discusión con un compañero y nueva votación (descripción ilustrativa de esta base, sin fuente leída). Porter, Bailey Lee y Simon (2013) compararon la instrucción entre pares con la clase expositiva en cuatro materias de computación universitaria, a lo largo de diez años: la reprobación (abandonar o terminar con D o F) bajó en promedio un 61 % por curso, de 20 % a 7 %, y un 67 % (de 23 % a 8 %) con el mismo docente dando la misma materia. Es un estudio en el aula, no un ensayo aleatorizado; el detalle está en la nota de instrucción entre pares. La evidencia general del aprendizaje activo está en [aprendizaje activo](../Aprendizaje-activo-e-indagacion/aprendizaje-activo.md).

## Lo que la evidencia no cubre

Ninguno de los estudios verificados es de adultos que aprenden programación en el trabajo o en cursos profesionales: son universitarios de cursos introductorios o escolares. Llevar estas técnicas a un adulto que se reconvierte a IT es una inferencia de esta base. Con un asistente de IA en la mano del alumno el problema cambia; eso está en [enseñar programación con IA](ensenar-programacion-con-ia.md).
