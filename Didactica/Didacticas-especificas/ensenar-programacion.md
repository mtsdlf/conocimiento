---
resumen: >-
  Enseñar programación tiene una didáctica propia, la investigación en educación en computación, que propone leer y trazar código antes de escribirlo, nombrar los subobjetivos de cada procedimiento y hacer explícito cómo ejecuta la máquina. Casi toda su evidencia es de cursos introductorios universitarios y escolares.
estado: vigente
estabilidad: semi
fuentes:
  - "Fincher y Robins (eds.) (2019), The Cambridge Handbook of Computing Education Research, caps. 12 y 15: https://www.cambridge.org/core/product/F8CFAF7B81A8F6BF5C663412BA0A943D (según resumen)"
  - "Luxton-Reilly et al. (2018), Introductory programming: a systematic literature review, ITiCSE Companion, DOI 10.1145/3293881.3295779 (solo metadatos)"
  - "Lister et al. (2004), ITiCSE working group, DOI 10.1145/1044550.1041673 (solo metadatos)"
  - "Lopez, Whalley, Robbins y Lister (2008), DOI 10.1145/1404520.1404531 (solo metadatos)"
  - "Xie, Nelson y Ko (2018), An Explicit Strategy to Scaffold Novice Program Tracing, SIGCSE, DOI 10.1145/3159450.3159527 (solo metadatos)"
  - "Margulieux, Morrison y Decker (2020), International Journal of STEM Education 7, art. 19: https://link.springer.com/article/10.1186/s40594-020-00222-7 (abstract)"
  - "Sentance, Waite y Kallia (2019), PRIMM, Computer Science Education 29(2-3), DOI 10.1080/08993408.2019.1608781 (solo metadatos)"
  - "Ericson et al. (2022), Parsons Problems and Beyond, ITiCSE Working Group Reports, DOI 10.1145/3571785.3574127 (solo metadatos)"
  - "Sorva (2013), Notional Machines and Introductory Programming Education, ACM TOCE 13(2), DOI 10.1145/2483710.2483713 (abstract)"
  - "Selvaraj, Zhang, Porter y Soosai Raj (2021), Live Coding: A Review of the Literature, ITiCSE: https://par.nsf.gov/biblio/10313400-live-coding-review-literature (abstract)"
  - "Porter, Bailey Lee y Simon (2013), Halving fail rates using peer instruction, SIGCSE, DOI 10.1145/2445196.2445250 (solo metadatos)"
  - "Didactica/.investigacion/indagacion-tutoria-especificas.md"
  - "Didactica/.investigacion/explicita-practica-preguntas-feedback.md"
aliases: [didáctica de la programación, enseñanza de la programación, computing education, educación en computación, CS education, teaching programming]
creado: 2026-11-27
revisado: 2026-11-27
---

# Enseñar programación

Enseñar programación tiene una didáctica propia, la investigación en educación en computación, que propone leer y trazar código antes de escribirlo, nombrar los subobjetivos de cada procedimiento y hacer explícito cómo ejecuta la máquina. Casi toda su evidencia es de cursos introductorios universitarios y escolares.

Dentro de [Didácticas específicas](didacticas-especificas.md) es la materia con más literatura verificada. El problema que la motiva aparece en el abstract de Margulieux et al. (2020): las tasas de abandono y reprobación en los cursos introductorios de programación «are regularly as high as 50%». El mapa del campo es *The Cambridge Handbook of Computing Education Research* (Fincher y Robins, 2019): para quien enseña, los capítulos 12, sobre programadores novatos y la programación introductoria, y 15, sobre enfoques pedagógicos. La revisión sistemática de Luxton-Reilly et al. (2018) cubre la programación introductoria; no se leyó.

## Leer y trazar antes de escribir

Lister et al. (2004) y Lopez et al. (2008) se citan para la idea de que la habilidad de escribir código se apoya en la de leerlo y trazarlo: predecir qué hace un fragmento, paso a paso. De ambos solo se verificaron título, lugar de publicación y autores; las cifras que circulan sobre esa relación no se verificaron, y según la pista de la que parte esta base son correlaciones y no experimentos. Xie, Nelson y Ko (2018) propusieron enseñar una estrategia explícita de trazado como andamiaje para novatos; su resultado tampoco se verificó.

> [!NOTE] Sin fuente todavía: cuánto de la habilidad de escribir código explican el trazado y la explicación (Lopez et al. 2008) y el efecto de la estrategia de trazado de Xie et al. (2018), leídos en el artículo.

La idea encaja con el resto del tema: leer un programa que funciona es estudiar un [ejemplo resuelto](../Explicar-y-modelar/modelado-y-ejemplos-resueltos.md), y pedir que se prediga la salida antes de ejecutarla es una [pregunta de proceso](../Preguntas-y-dialogo/preguntas-en-clase.md).

## Subobjetivos nombrados

Margulieux, Morrison y Decker (2020) hicieron un cuasiexperimento en un curso introductorio de un semestre con 265 estudiantes: la mitad recibió instrucción con subobjetivos nombrados (cada procedimiento partido en pasos con un nombre que dice para qué sirve; definición de esta base) y la otra mitad, la habitual. Según el abstract, el grupo con subobjetivos sacó mejores notas en los cuestionarios formativos, tomados dentro de la semana en que se aprendía cada procedimiento, pero no en los exámenes finales. Tuvo menor varianza de notas y menos abandonos y reprobados; según el resumen de un buscador, con un efecto mayor en los estudiantes en riesgo. No hay tamaños de efecto.

Es el estudio de programación con resultado concreto mejor verificado de esta base. La técnica es una forma de [modelado](../Explicar-y-modelar/modelado-y-ejemplos-resueltos.md): hace visible la estructura que el experto ve y el novato no.

## Del código ajeno al propio: PRIMM y problemas de Parsons

- **PRIMM** (Sentance, Waite y Kallia, 2019) ordena la clase en los cinco pasos de su sigla en inglés (*predict, run, investigate, modify, make*): predecir, ejecutar, investigar, modificar y crear; el desglose de la sigla es ilustrativo, de esta base: no se leyó el artículo. Es la secuencia de [práctica guiada y andamiaje](../Practica-guiada-y-andamiaje/practica-guiada-y-andamiaje.md) aplicada al código: primero se lee y se predice, al final se escribe solo. Los detalles del estudio (escuelas, cantidad y edad de alumnos) no se verificaron; es evidencia escolar, no de adultos.
- **Problemas de Parsons**: en su forma habitual se dan las líneas de una solución desordenadas y hay que ordenarlas (descripción ilustrativa de esta base, sin fuente leída). Ericson et al. (2022) revisan esa literatura en un grupo de trabajo de ITiCSE; su contenido no se leyó.

## La máquina nocional

Sorva (2013) llama máquina nocional a la versión simplificada de la computadora que quien programa necesita para entender qué pasa al ejecutarse un programa en un lenguaje dado. Según el abstract, argumenta que las máquinas nocionales son un desafío mayor de la programación introductoria y que quien enseña debería convertirlas en un objetivo de aprendizaje explícito. Es una revisión con posición, no un experimento. Es un ejemplo de [conocimiento pedagógico del contenido](conocimiento-pedagogico-del-contenido.md): saber qué modelo de ejecución le falta al novato.

## Programar en vivo y aprender entre pares

- **Programar en vivo** (*live coding*): escribir código frente al grupo, con los errores y las correcciones a la vista. Selvaraj et al. (2021) revisaron la literatura y concluyen que «there is a lack of empirical evidence to support claims about the effectiveness of live coding on student learning», aunque se recomienda como una de las mejores prácticas. Lo que sí tiene respaldo general es el [modelado](../Explicar-y-modelar/modelado-y-ejemplos-resueltos.md) y el pensar en voz alta; programar en vivo es una forma de hacerlo.
- **[Instrucción entre pares](../../Ciencias-del-aprendizaje/Aprender-con-otros/instruccion-entre-pares.md)** (*peer instruction*): en su forma habitual, una pregunta conceptual, votación individual, discusión con un compañero y nueva votación (descripción ilustrativa de esta base, sin fuente leída). El título de Porter, Bailey Lee y Simon (2013) habla de reducir a la mitad las tasas de reprobación; la cifra exacta no se verificó. La evidencia general del aprendizaje activo está en [aprendizaje activo](../Aprendizaje-activo-e-indagacion/aprendizaje-activo.md).

## Lo que la evidencia no cubre

Ninguno de los estudios verificados es de adultos que aprenden programación en el trabajo o en cursos profesionales: son universitarios de cursos introductorios o escolares. Llevar estas técnicas a un adulto que se reconvierte a IT es una inferencia de esta base. Con un asistente de IA en la mano del alumno el problema cambia; eso está en [enseñar programación con IA](ensenar-programacion-con-ia.md).
