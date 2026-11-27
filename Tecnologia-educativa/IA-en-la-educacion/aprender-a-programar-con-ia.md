---
resumen: >-
  Aprender a programar con IA es el caso en que un novato escribe código con un asistente que genera código. Los estudios muestran que sube lo que se termina durante la tarea, no siempre lo que se aprende, y que el beneficio se concentra en quien ya iba bien: la brecha se ensancha.
estado: borrador
estabilidad: semi
fuentes:
  - "Kazemitabaar, M. et al. (2023), CHI 2023, arXiv 2302.07427: https://arxiv.org/abs/2302.07427"
  - "Prather, J. et al. (2024), The Widening Gap, ICER 2024, arXiv 2405.17739: https://arxiv.org/abs/2405.17739"
  - "Kazemitabaar, M. et al. (2024), arXiv 2410.08922: https://arxiv.org/abs/2410.08922"
  - "Zi, Y. et al. (2025), FSE Companion 2025, arXiv 2504.19037: https://arxiv.org/abs/2504.19037"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [novatos y asistentes de código, programar con IA, CS1 con IA, enseñar programación con IA, ilusión de competencia, illusion of competence, widening gap]
creado: 2026-11-27
revisado:
---

# Aprender a programar con IA

Aprender a programar con IA es el caso en que un novato escribe código con un asistente que genera código. Los estudios muestran que sube lo que se termina durante la tarea, no siempre lo que se aprende, y que el beneficio se concentra en quien ya iba bien: la brecha se ensancha.

Es el cruce de los tres roles de la vertical en una sola tarea: el asistente puede ser [tutor](ia-como-tutor.md) si guía, o [atajo](ia-como-atajo.md) si escribe el código que el alumno tenía que aprender a escribir. Es también el caso más cercano a enseñar IT, aunque todos los estudios son de estudiantes y no de adultos que aprenden en su trabajo. Cómo trabajan los asistentes de código en la práctica profesional está en [Desarrollo](../../Desarrollo/desarrollo.md).

## Cuatro estudios de novatos

| Estudio | Diseño | Hallazgo | Estado |
|---|---|---|---|
| Kazemitabaar et al. (2023) | 69 novatos de 10 a 17 años, 45 tareas de Python, la mitad con Codex | Con Codex, 1,15 veces la tasa de finalización y 1,8 veces el puntaje en las tareas de escribir; modificar código a mano no empeoró; en el postest a la semana, algo mejor con Codex pero sin diferencia significativa; quienes tenían mejor pretest retuvieron más | Presentado en CHI 2023 (la revisión por pares se infiere por la sede) |
| Prather et al. (2024) | 21 sesiones de laboratorio con observación, entrevistas y seguimiento ocular | Quienes ya iban bien usaron la IA para construir lo que habían planeado e ignoraron las sugerencias malas; quienes tenían problemas metacognitivos los conservaron y sumaron otros, y muchos sobreestimaron su rendimiento | Aceptado en ICER 2024; cualitativo |
| Kazemitabaar et al. (2024) | Siete técnicas para que el alumno se involucre con el código generado; 82 participantes entre grupos y 42 intrasujeto | La más eficaz fue guiar paso a paso: el alumno dice qué hacer en cada etapa antes de ver el código | Preprint de octubre de 2024 en lo verificado; un material lo ubica en IUI 2025, sede sin verificar |
| Zi et al. (2025) | 32 alumnos de un primer curso de programación, 160 tareas | Entendieron la implementación generada en el 32,5 % de las tareas; los obstáculos fueron no ser hablante nativo de inglés, la sintaxis de Python y confiar demasiado en la salida | Aceptado en FSE Companion 2025 |

## La brecha que se ensancha

Prather et al. llamaron a su artículo «The Widening Gap» por lo que observaron: la IA amplifica lo que el alumno ya trae. Quien sabe qué quiere construir usa la sugerencia como herramienta y descarta la que no sirve. Quien no sabe planificar ni controlar su propio entendimiento acepta la sugerencia y cree que entiende, lo que los autores llaman «illusion of competence». Lo que separa a unos de otros es la [metacognición](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/metacognicion-y-autorregulacion.md): creer que se entiende porque el código aparece sin esfuerzo es un caso de [ilusión de saber](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/ilusion-de-saber.md), y sobreestimar el propio rendimiento, uno de mala [calibración](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/calibracion.md).

Kazemitabaar et al. (2023) muestra lo mismo con números: quienes tenían mejor pretest retuvieron más. Y Bastani et al., en matemática, coincide en que el rendimiento durante la tarea sube sin que suba lo aprendido. Tres estudios con métodos distintos apuntan a lo mismo.

Zi et al. agrega un dato para quien enseña en castellano: no ser hablante nativo de inglés fue un obstáculo para entender el código generado. El estudio es de un curso en inglés; que valga igual para hispanohablantes es inferencia.

## Qué cambia al enseñar programación

Lo que sostienen estos estudios, como lectura de esta base:

1. Que el alumno decida antes de ver el código. Es la técnica que mejor funcionó en Kazemitabaar et al. (2024), y es la misma lógica de la [escalera de pistas](../Tutores-inteligentes/pistas-de-un-tutor-inteligente.md): el alumno intenta antes de recibir el paso.
2. Medir sin la herramienta. Lo que se termina con el asistente no dice lo que se aprendió; el postest sin asistente sí.
3. Mirar a quien va peor. El beneficio cae sobre quien ya sabe más; quien tiene problemas metacognitivos los conserva y puede creer que va bien.

> [!NOTE]
> Sin fuente todavía: Margulieux et al. (ITiCSE 2024), el ensayo de tres brazos de Bassner et al. (*Computers and Education: AI*, 2025, 275 participantes), Geng et al. (2025) y Xiao et al. (2026). Se citan seguido y no se pudieron verificar. Tampoco hay estudios de adultos que aprenden a programar en su trabajo.
