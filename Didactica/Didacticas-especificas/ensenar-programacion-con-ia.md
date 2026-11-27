---
resumen: >-
  Enseñar programación con IA es decidir cómo y cuándo dejar que quien aprende use un asistente que escribe código. Los primeros experimentos coinciden en que la IA sin guía sube el rendimiento mientras se practica pero no necesariamente lo aprendido, ayuda más a quien ya sabía (la brecha se ensancha), y rinde mejor cuando obliga a predecir o explicar antes de mostrar la solución.
estado: borrador
estabilidad: semi
fuentes:
  - "Kazemitabaar et al. (2023), Studying the effect of AI code generators on supporting novice learners in introductory programming, CHI: https://arxiv.org/abs/2302.07427 (abstract)"
  - "Prather et al. (2024), The Widening Gap, ICER: https://arxiv.org/abs/2405.17739 (abstract)"
  - "Kazemitabaar et al. (2024), preprint: https://arxiv.org/abs/2410.08922 (abstract)"
  - "Zi, Y. et al. (2025), FSE Companion 2025, arXiv 2504.19037: https://arxiv.org/abs/2504.19037"
  - "Bastani et al. (2025), PNAS 122(26), e2422633122 (abstract)"
  - "Kestin et al. (2025), Scientific Reports 15, 17458, DOI 10.1038/s41598-025-97652-6 (abstract parcial)"
  - "Denny et al. (2024), Communications of the ACM 67(2), DOI 10.1145/3624720 (solo metadatos)"
  - "Didactica/.investigacion/indagacion-tutoria-especificas.md"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [enseñar a programar con IA, aprender a programar con IA, programar con IA, novatos y asistentes de código, CS1 con IA, IA en la enseñanza de la programación, asistentes de código en la educación, LLM en educación en computación, generative AI in computing education, ilusión de competencia, illusion of competence, widening gap]
creado: 2026-11-27
revisado:
---

# Enseñar programación con IA

Enseñar programación con IA es decidir cómo y cuándo dejar que quien aprende use un asistente que escribe código. Los primeros experimentos coinciden en que la IA sin guía sube el rendimiento mientras se practica pero no necesariamente lo aprendido, ayuda más a quien ya sabía (la brecha se ensancha), y rinde mejor cuando obliga a predecir o explicar antes de mostrar la solución.

Dentro de [Didácticas específicas](didacticas-especificas.md) es una nota aparte de [enseñar programación](ensenar-programacion.md) porque su evidencia es de 2023 en adelante y cambia rápido: va con `estabilidad: semi` y conviene releerla contra estudios nuevos. Es también el caso donde se cruzan los roles que Tecnología educativa le ve a la IA: el asistente puede ser [tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md) si guía, o [atajo](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-atajo.md) si escribe el código que el alumno tenía que aprender a escribir (el panorama está en [IA en la educación](../../Tecnologia-educativa/IA-en-la-educacion/ia-en-la-educacion.md)). Cómo trabajan los asistentes de código en la práctica profesional está en [Desarrollo](../../Desarrollo/desarrollo.md).

## Lo que muestran los primeros estudios

Cuatro estudios son de novatos que programan con un asistente:

| Estudio | Diseño | Hallazgo | Estado |
|---|---|---|---|
| Kazemitabaar et al. (2023) | 69 novatos de 10 a 17 años, 45 tareas de Python, la mitad con Codex, el modelo de OpenAI que genera código a partir de texto | Con Codex, 1,15 veces la tasa de finalización y 1,8 veces el puntaje en las tareas de escribir; modificar código a mano no empeoró; en el [postest](../Fundamentos/glosario-de-didactica.md#leer-la-evidencia) (la prueba final) a la semana, algo mejor con Codex pero sin diferencia significativa; quienes tenían mejor pretest (la prueba inicial) retuvieron significativamente más | Presentado en CHI 2023 (la revisión por pares se infiere por la sede) |
| Prather et al. (2024) | 21 sesiones de laboratorio con observación, entrevistas y seguimiento ocular | Quienes ya iban bien usaron la IA para construir lo que habían planeado e ignoraron las sugerencias malas; quienes tenían problemas metacognitivos los conservaron y sumaron otros, y muchos sobreestimaron su rendimiento | Aceptado en ICER 2024; cualitativo |
| Kazemitabaar et al. (2024) | Siete técnicas para que el alumno se involucre con el código generado; 82 participantes entre grupos y 42 intrasujeto | La más eficaz fue guiar paso a paso: el alumno dice qué debe pasar en cada etapa antes de ver el código | Preprint de octubre de 2024 en lo verificado; un material lo ubica en IUI 2025, sede sin verificar |
| Zi et al. (2025) | 32 alumnos de un primer curso de programación, 160 tareas | Entendieron la implementación generada en el 32,5 % de las tareas; los obstáculos fueron no ser hablante nativo de inglés, la sintaxis de Python y confiar demasiado en la salida | Aceptado en FSE Companion 2025 |

Dos más no son de programación pero miden lo mismo, aprender con un asistente de IA:

| Estudio | Quiénes y qué | Resultado según el abstract |
|---|---|---|
| Bastani et al. 2025 (PNAS) | Casi 1000 estudiantes secundarios de matemática, experimento de campo | Con GPT-4 en la práctica, +48 % (versión base) y +127 % (versión tutor); al quitar el acceso, los de la versión base quedaron 17 % por debajo del control y los de la versión tutor, casi sin daño según el abstract (sin diferencia con el control, según [la IA como tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md)) |
| Kestin et al. 2025 (Scientific Reports) | Universitarios de física, ensayo aleatorizado | «learn significantly more in less time» con un tutor de IA que con una clase de aprendizaje activo; el abstract no da cifras, y las del artículo están en [la IA como tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md) |

Denny et al. (2024), en *Communications of the ACM*, es un artículo de posición sobre la IA generativa en la educación en computación; no se leyó su contenido.

## El patrón: rendir no es aprender

Leídos juntos, los estudios dibujan tres regularidades:

1. La IA sin guía infla el rendimiento durante la práctica. En Bastani et al., quienes practicaron con la versión base rindieron más mientras la tenían y menos que el control cuando se la sacaron. Es el mismo problema que el tema ve en la [retroalimentación](../Retroalimentacion/retroalimentacion.md) que da la respuesta: resolver con ayuda no garantiza aprender a resolver.
2. Ayuda más a quien ya sabía. En Kazemitabaar et al. 2023 retuvieron más los de mayor pretest, y en Prather et al. quienes ya planeaban bien sacaron provecho. Encaja con la [inversión de la experticia](../Practica-guiada-y-andamiaje/inversion-de-la-experticia.md): la misma ayuda no sirve igual a un novato que a alguien con base.
3. Los diseños que obligan a pensar antes de mostrar funcionan mejor. La versión tutor de Bastani, que no entregaba la respuesta, casi no dañó; en Kazemitabaar et al. 2024, predecir cada etapa antes de ver el código fue lo más eficaz. Es la lógica de la [escalera de pistas](../Retroalimentacion/escalera-de-pistas.md) (y de las [pistas de un tutor inteligente](../../Tecnologia-educativa/Tutores-inteligentes/pistas-de-un-tutor-inteligente.md)) y de la [autoexplicación](../Preguntas-y-dialogo/autoexplicacion.md).

## La brecha que se ensancha

Prather et al. llamaron a su artículo «The Widening Gap» por lo que observaron: la IA amplifica lo que el alumno ya trae. Quien sabe qué quiere construir usa la sugerencia como herramienta y descarta la que no sirve. Quien no sabe planificar ni controlar su propio entendimiento acepta la sugerencia y cree que entiende, lo que los autores llaman «illusion of competence» (ilusión de competencia). Lo que separa a unos de otros es la [metacognición](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/metacognicion-y-autorregulacion.md): creer que se entiende porque el código aparece sin esfuerzo es un caso de [ilusión de saber](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/ilusion-de-saber.md), y sobreestimar el propio rendimiento, uno de mala [calibración](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/calibracion.md).

Zi et al. agrega un dato para quien enseña en castellano: no ser hablante nativo de inglés fue un obstáculo para entender el código generado. El estudio es de un curso en inglés; que valga igual para hispanohablantes es inferencia.

## Qué decisiones toma quien enseña

Lo que sigue es una inferencia de esta base a partir de los estudios de arriba, no una recomendación de ninguno de ellos:

- Pedir que quien aprende escriba o diga qué tiene que hacer el código antes de pedírselo a la IA, como en la secuencia predecir y luego ejecutar de [enseñar programación](ensenar-programacion.md).
- Comprobar lo aprendido sin el asistente de vez en cuando, porque el rendimiento con IA no dice cuánto queda sin ella. Cómo se arma esa comprobación está en [tareas de desempeño](../../Evaluacion-educativa/Instrumentos/tareas-de-desempeno.md), de Evaluación educativa.
- Graduar el acceso según el nivel: más restricción al principio, más libertad cuando hay base.
- Mirar a quien va peor: el beneficio cae sobre quien ya sabe más, y quien tiene problemas metacognitivos los conserva y puede creer que va bien.

## Lo que todavía no se sabe

Dos de los estudios son con menores (Kazemitabaar et al. 2023 y Bastani et al.), y Bastani es de matemática y Kestin de física, no de programación. Ninguno es de adultos que aprenden a programar en su trabajo. La base de esta nota es corta y el campo publica rápido; los estudios posteriores que no se verificaron no entran.

> [!NOTE]
> Sin fuente todavía: un experimento con adultos que aprenden programación con asistentes de IA, una revisión sistemática del subcampo, y Margulieux et al. (ITiCSE 2024), el ensayo de tres brazos de Bassner et al. (*Computers and Education: AI*, 2025, 275 participantes), Geng et al. (2025) y Xiao et al. (2026), que se citan seguido y no se pudieron verificar.
