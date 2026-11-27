---
resumen: >-
  Enseñar programación con IA es decidir cómo y cuándo dejar que quien aprende use un asistente que escribe código. Los primeros experimentos coinciden en que la IA sin guía sube el rendimiento mientras se practica pero no necesariamente lo aprendido, ayuda más a quien ya sabía (la brecha se ensancha), y rinde mejor cuando obliga a predecir o explicar antes de mostrar la solución.
estado: vigente
estabilidad: semi
fuentes:
  - "Kazemitabaar et al. (2023), Studying the effect of AI code generators on supporting novice learners in introductory programming, CHI: https://arxiv.org/abs/2302.07427 (abstract)"
  - "Prather et al. (2024), The Widening Gap, ICER: https://arxiv.org/abs/2405.17739 (abstract)"
  - "Kazemitabaar, Huang, Suh, Henley y Grossman (2025), Exploring the Design Space of Cognitive Engagement Techniques with AI-Generated Code for Enhanced Learning, IUI '25:695-714, DOI 10.1145/3708359.3712104 (preprint de octubre de 2024: https://arxiv.org/abs/2410.08922) (abstract)"
  - "Kazemitabaar, Ye, Wang, Henley, Denny, Craig y Grossman (2024), CodeAid: Evaluating a Classroom Deployment of an LLM-based Programming Assistant that Balances Student and Educator Needs, CHI '24, DOI 10.1145/3613904.3642773: https://arxiv.org/abs/2401.11314 (abstract)"
  - "Margulieux, Prather, Reeves, Becker, Cetin Uzun, Loksa, Leinonen y Denny (2024), Self-Regulation, Self-Efficacy, and Fear of Failure Interactions with How Novices Use LLMs to Solve Programming Problems, ITiCSE 2024:276-282, DOI 10.1145/3649217.3653621: https://par.nsf.gov/servlets/purl/10580378 (abstract y sección de método)"
  - "Bassner, Lenk-Ostendorf, Beinstingel, Wasner y Krusche (2025), Less stress, better scores, same learning: The dissociation of performance and learning in AI-supported programming education, Computers and Education: Artificial Intelligence 10, 100537, DOI 10.1016/j.caeai.2025.100537 (abstract)"
  - "Zi, Y. et al. (2025), FSE Companion 2025, arXiv 2504.19037: https://arxiv.org/abs/2504.19037"
  - "Bastani et al. (2025), PNAS 122(26), e2422633122 (abstract)"
  - "Kestin et al. (2025), Scientific Reports 15, 17458, DOI 10.1038/s41598-025-97652-6 (abstract parcial)"
  - "Chen, M. et al. (2021), Evaluating Large Language Models Trained on Code, arXiv 2107.03374: https://arxiv.org/abs/2107.03374 (texto completo; sin revisión por pares)"
  - "OpenAI (10/08/2021), OpenAI Codex: https://openai.com/index/openai-codex/ (leída 2026-11-27)"
  - "Denny et al. (2024), Communications of the ACM 67(2), DOI 10.1145/3624720 (solo metadatos)"
  - "Didactica/.investigacion/indagacion-tutoria-especificas.md"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
  - "Didactica/.investigacion/fuentes-didacticas-especificas-2026-11.md"
  - "Tecnologia-educativa/.investigacion/fuentes-tutores-y-plataformas-2026-11.md"
aliases: [enseñar a programar con IA, aprender a programar con IA, programar con IA, novatos y asistentes de código, CS1 con IA, IA en la enseñanza de la programación, asistentes de código en la educación, LLM en educación en computación, generative AI in computing education, ilusión de competencia, illusion of competence, widening gap]
creado: 2026-11-27
revisado: 2026-11-27
---

# Enseñar programación con IA

Enseñar programación con IA es decidir cómo y cuándo dejar que quien aprende use un asistente que escribe código. Los primeros experimentos coinciden en que la IA sin guía sube el rendimiento mientras se practica pero no necesariamente lo aprendido, ayuda más a quien ya sabía (la brecha se ensancha), y rinde mejor cuando obliga a predecir o explicar antes de mostrar la solución.

Dentro de [Didácticas específicas](didacticas-especificas.md) es una nota aparte de [enseñar programación](ensenar-programacion.md) porque su evidencia es de 2023 en adelante y cambia rápido: va con `estabilidad: semi` y conviene releerla contra estudios nuevos. Es también el caso donde se cruzan los roles que Tecnología educativa le ve a la IA: el asistente puede ser [tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md) si guía, o [atajo](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-atajo.md) si escribe el código que el alumno tenía que aprender a escribir (el panorama está en [IA en la educación](../../Tecnologia-educativa/IA-en-la-educacion/ia-en-la-educacion.md)). Cómo trabajan los asistentes de código en la práctica profesional está en [Desarrollo](../../Desarrollo/desarrollo.md).

## Lo que muestran los primeros estudios

Siete estudios son de novatos que programan con un asistente:

| Estudio | Diseño | Hallazgo | Estado |
|---|---|---|---|
| Kazemitabaar et al. (2023) | 69 novatos de 10 a 17 años, 45 tareas de Python, la mitad con Codex, el modelo de OpenAI de 2021, derivado de GPT-3 y entrenado con código público de GitHub, que genera código a partir de texto | Con Codex, 1,15 veces la tasa de finalización y 1,8 veces el puntaje en las tareas de escribir; modificar código a mano no empeoró; en el [postest](../Fundamentos/glosario-de-didactica.md#leer-la-evidencia) (la prueba final) a la semana, algo mejor con Codex pero sin diferencia significativa; quienes tenían mejor pretest (la prueba inicial) retuvieron significativamente más | Presentado en CHI 2023 (la revisión por pares se infiere por la sede) |
| Prather et al. (2024) | 21 sesiones de laboratorio con observación, entrevistas y seguimiento ocular | Quienes ya iban bien usaron la IA para construir lo que habían planeado e ignoraron las sugerencias malas; quienes tenían problemas metacognitivos los conservaron y sumaron otros, y muchos sobreestimaron su rendimiento | Aceptado en ICER 2024; cualitativo |
| Kazemitabaar et al. (2024), CodeAid | Un asistente que no muestra el código de la solución, usado por 700 alumnos de un curso de programación durante 12 semanas; análisis de 8000 usos, encuestas, 22 entrevistas a alumnos y 8 a docentes | Cuatro criterios de diseño para asistentes educativos, entre ellos evitar las respuestas directas y promover el compromiso cognitivo | CHI 2024; cualitativo |
| Kazemitabaar et al. (2025) | Siete técnicas para que el alumno se involucre con el código generado; 82 participantes entre grupos y 42 intrasujeto | La más eficaz fue guiar paso a paso: el alumno dice qué debe pasar en cada etapa antes de ver el código | IUI 2025 (preprint de octubre de 2024) |
| Margulieux et al. (2024) | Alumnos de un curso introductorio de una universidad pública de EE. UU. que usaban IA a su gusto durante un semestre; 54 participantes, 40 con datos completos; mediciones repetidas y método mixto | Quienes tenían más autoeficacia, menos miedo a fallar o mejores notas previas usaron menos la IA, o más tarde, y la juzgaron menos útil; no hubo relación entre estrategias de autorregulación y uso | ITiCSE 2024; correlacional, sin causalidad según los autores |
| Bassner et al. (2025) | Ensayo aleatorizado de tres brazos con 275 alumnos de un primer curso de la TUM: un tutor que da pistas sin la solución (Iris), ChatGPT sin restricciones y un control sin IA, en un ejercicio de 90 minutos | Los dos grupos con IA sacaron más puntaje en el ejercicio, pero ninguno ganó más conocimiento entre pre y postest ni comprendió mejor el código; solo el tutor con pistas subió la motivación intrínseca | *Computers and Education: AI*, vol. 10; según su resumen |
| Zi et al. (2025) | 32 alumnos de un primer curso de programación, 160 tareas | Entendieron la implementación generada en el 32,5 % de las tareas; los obstáculos fueron no ser hablante nativo de inglés, la sintaxis de Python y confiar demasiado en la salida | Aceptado en FSE Companion 2025 |

Dos más no son de programación pero miden lo mismo, aprender con un asistente de IA:

| Estudio | Quiénes y qué | Resultado según el abstract |
|---|---|---|
| Bastani et al. 2025 (PNAS) | Casi 1000 estudiantes secundarios de matemática, experimento de campo | Con GPT-4 en la práctica, +48 % (versión base) y +127 % (versión tutor); al quitar el acceso, los de la versión base quedaron 17 % por debajo del control y los de la versión tutor, casi sin daño según el abstract (sin diferencia con el control, según [la IA como tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md)) |
| Kestin et al. 2025 (Scientific Reports) | Universitarios de física, ensayo aleatorizado | «learn significantly more in less time» con un tutor de IA que con una clase de aprendizaje activo; el abstract no da cifras, y las del artículo están en [la IA como tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md) |

Denny et al. (2024), en *Communications of the ACM*, es un artículo de posición sobre la IA generativa en la educación en computación; no se leyó su contenido.

## El patrón: rendir no es aprender

Leídos juntos, los estudios dibujan tres regularidades:

1. La IA sin guía infla el rendimiento durante la práctica. En Bastani et al., quienes practicaron con la versión base rindieron más mientras la tenían y menos que el control cuando se la sacaron. En Bassner et al., el puntaje del ejercicio subió con IA y el aprendizaje medido no cambió; los autores lo llaman «a performance aid rather than a learning enhancer». Es el mismo problema que el tema ve en la [retroalimentación](../Retroalimentacion/retroalimentacion.md) que da la respuesta: resolver con ayuda no garantiza aprender a resolver.
2. Ayuda más a quien ya sabía. En Kazemitabaar et al. 2023 retuvieron más los de mayor pretest, y en Prather et al. quienes ya planeaban bien sacaron provecho. Encaja con la [inversión de la experticia](../Practica-guiada-y-andamiaje/inversion-de-la-experticia.md): la misma ayuda no sirve igual a un novato que a alguien con base.
3. Los diseños que obligan a pensar antes de mostrar funcionan mejor. La versión tutor de Bastani, que no entregaba la respuesta, casi no dañó; en Kazemitabaar et al. 2025, predecir cada etapa antes de ver el código fue lo más eficaz. Es la lógica de la [escalera de pistas](../Retroalimentacion/escalera-de-pistas.md) (y de las [pistas de un tutor inteligente](../../Tecnologia-educativa/Tutores-inteligentes/pistas-de-un-tutor-inteligente.md)) y de la [autoexplicación](../Preguntas-y-dialogo/autoexplicacion.md).

> [!IMPORTANT]
> Bassner et al. (2025) matizan la tercera regularidad. En su ensayo, el tutor que daba pistas sin la solución tampoco produjo más aprendizaje que el control: solo mejoró la motivación. La versión tutor de Bastani et al. evitó el daño, pero tampoco superó al control en lo aprendido. En física, Kestin et al. sí midieron más aprendizaje con un tutor de IA, contra una clase de aprendizaje activo. Lo que sí muestran los dos es que la IA que da la solución no enseña más que practicar sin ella.

## La brecha que se ensancha

Prather et al. llamaron a su artículo «The Widening Gap» por lo que observaron: la IA amplifica lo que el alumno ya trae. Quien sabe qué quiere construir usa la sugerencia como herramienta y descarta la que no sirve. Quien no sabe planificar ni controlar su propio entendimiento acepta la sugerencia y cree que entiende, lo que los autores llaman «illusion of competence» (ilusión de competencia). Lo que separa a unos de otros es la [metacognición](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/metacognicion-y-autorregulacion.md): creer que se entiende porque el código aparece sin esfuerzo es un caso de [ilusión de saber](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/ilusion-de-saber.md), y sobreestimar el propio rendimiento, uno de mala [calibración](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/calibracion.md).

Margulieux et al. (2024) miran otra cosa, cuánto se usa la IA, y encuentran un reparto distinto del de Prather et al.: los alumnos con más autoeficacia y mejores notas previas recurrieron menos a la IA, o más tarde. Que esos alumnos terminaran con mejores notas es, según los autores, «most likely due to prior characteristics», y sus datos no sugieren que sea causal. En Prather et al. quien ya sabía usaba la IA con provecho; en Margulieux et al., la usaba menos. Las dos cosas pueden ser ciertas a la vez, pero ningún estudio lo compara (lectura de esta base).

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
> Sin fuente todavía: un experimento con adultos que aprenden programación con asistentes de IA, una revisión sistemática del subcampo, y Geng et al. (2025) y Xiao et al. (2026), que se citan seguido y no se pudieron identificar: sin título ni sede, la búsqueda no da con un trabajo único.
