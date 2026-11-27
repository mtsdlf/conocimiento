---
resumen: >-
  Enseñar programación con IA es decidir cómo y cuándo dejar que quien aprende use un asistente que escribe código. Los primeros experimentos coinciden en que la IA sin guía sube el rendimiento mientras se practica pero no necesariamente lo aprendido, ayuda más a quien ya sabía, y rinde mejor cuando obliga a predecir o explicar antes de mostrar la solución.
estado: borrador
estabilidad: semi
fuentes:
  - "Kazemitabaar et al. (2023), Studying the effect of AI code generators on supporting novice learners in introductory programming, CHI: https://arxiv.org/abs/2302.07427 (abstract)"
  - "Prather et al. (2024), ICER: https://arxiv.org/abs/2405.17739 (abstract)"
  - "Kazemitabaar et al. (2024), preprint: https://arxiv.org/abs/2410.08922 (abstract)"
  - "Bastani et al. (2025), PNAS 122(26), e2422633122 (abstract)"
  - "Kestin et al. (2025), Scientific Reports 15, 17458, DOI 10.1038/s41598-025-97652-6 (abstract parcial)"
  - "Denny et al. (2024), Communications of the ACM 67(2), DOI 10.1145/3624720 (solo metadatos)"
  - "Didactica/.investigacion/indagacion-tutoria-especificas.md"
aliases: [enseñar a programar con IA, IA en la enseñanza de la programación, asistentes de código en la educación, LLM en educación en computación, generative AI in computing education]
creado: 2026-11-27
revisado:
---

# Enseñar programación con IA

Enseñar programación con IA es decidir cómo y cuándo dejar que quien aprende use un asistente que escribe código. Los primeros experimentos coinciden en que la IA sin guía sube el rendimiento mientras se practica pero no necesariamente lo aprendido, ayuda más a quien ya sabía, y rinde mejor cuando obliga a predecir o explicar antes de mostrar la solución.

Dentro de [Didácticas específicas](didacticas-especificas.md) es una nota aparte de [enseñar programación](ensenar-programacion.md) porque su evidencia es de 2023 en adelante y cambia rápido: va con `estabilidad: semi` y conviene releerla contra estudios nuevos. Los tutores con modelos de lenguaje como tecnología están en [la IA como tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md), y lo que le pasa a quien aprende a programar con un asistente, en [aprender a programar con IA](../../Tecnologia-educativa/IA-en-la-educacion/aprender-a-programar-con-ia.md), las dos de Tecnología educativa; acá queda la decisión didáctica de quien enseña a programar.

## Lo que muestran los primeros estudios

| Estudio | Quiénes y qué | Resultado según el abstract |
|---|---|---|
| Kazemitabaar et al. 2023 (CHI) | 69 novatos de 10 a 17 años, 45 tareas, con Codex | Completaron 1,15 veces más tareas y puntuaron 1,8 veces más en las de autoría; modificar a mano no empeoró; a una semana, mejor pero no significativo; los de mayor puntaje previo retuvieron significativamente más |
| Prather et al. 2024 (ICER) | 21 sesiones de laboratorio con observación, entrevistas y seguimiento ocular | Quien usa bien la IA produce el código que ya planeaba; quien tiene dificultades termina con «an illusion of competence» y sus dificultades metacognitivas pueden empeorar |
| Kazemitabaar et al. 2024 (preprint) | 82 participantes entre sujetos, luego 42 intra sujetos | La técnica más eficaz hace que quien aprende diga qué debe pasar en cada etapa antes de ver el código |
| Bastani et al. 2025 (PNAS) | Casi 1000 estudiantes secundarios de matemática, experimento de campo | Con GPT-4 en la práctica, +48 % (versión base) y +127 % (versión tutor); al quitar el acceso, los de la versión base quedaron 17 % por debajo del control y los de la versión tutor, casi sin daño según el abstract (sin diferencia con el control, según [la IA como tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md)) |
| Kestin et al. 2025 (Scientific Reports) | Universitarios de física, ensayo aleatorizado | «learn significantly more in less time» con un tutor de IA que con una clase de aprendizaje activo; el abstract no da cifras, y las del artículo están en [la IA como tutor](../../Tecnologia-educativa/IA-en-la-educacion/ia-como-tutor.md) |

Denny et al. (2024), en *Communications of the ACM*, es un artículo de posición sobre la IA generativa en la educación en computación; no se leyó su contenido.

## El patrón: rendir no es aprender

Los cinco estudios, leídos juntos, dibujan tres regularidades:

1. **La IA sin guía infla el rendimiento durante la práctica.** En Bastani et al., quienes practicaron con la versión base rindieron más mientras la tenían y menos que el control cuando se la sacaron. Es el mismo problema que el tema ve en la [retroalimentación](../Retroalimentacion/retroalimentacion.md) que da la respuesta: resolver no es lo mismo que aprender a resolver.
2. **Ayuda más a quien ya sabía.** En Kazemitabaar et al. 2023 retuvieron más los de mayor puntaje previo, y en Prather et al. quienes ya planeaban bien sacaron provecho. Encaja con la [inversión de la experticia](../Practica-guiada-y-andamiaje/inversion-de-la-experticia.md): la misma ayuda no sirve igual a un novato que a alguien con base.
3. **Los diseños que obligan a pensar antes de mostrar funcionan mejor.** La versión tutor de Bastani, que no entregaba la respuesta, casi no dañó; en Kazemitabaar et al. 2024, predecir cada etapa antes de ver el código fue lo más eficaz. Es la lógica de la [escalera de pistas](../Retroalimentacion/escalera-de-pistas.md) y de la [autoexplicación](../Preguntas-y-dialogo/autoexplicacion.md).

## Qué decisiones toma quien enseña

Lo que sigue es una inferencia de esta base a partir de los estudios de arriba, no una recomendación de ninguno de ellos:

- Pedir que quien aprende escriba o diga qué tiene que hacer el código antes de pedírselo a la IA, como en la secuencia predecir y luego ejecutar de [enseñar programación](ensenar-programacion.md).
- Comprobar lo aprendido sin el asistente de vez en cuando, porque el rendimiento con IA no dice cuánto queda sin ella. Cómo se arma esa comprobación está en [tareas de desempeño](../../Evaluacion-educativa/Instrumentos/tareas-de-desempeno.md), de Evaluación educativa.
- Graduar el acceso según el nivel: más restricción al principio, más libertad cuando hay base.

## Lo que todavía no se sabe

Dos de los cinco estudios son con menores, uno es de matemática y otro de física, no de programación. Ninguno es de adultos que aprenden a programar. Bastani y Kestin miden dominios cercanos y no el código. La base de esta nota es corta y el campo publica rápido; los estudios posteriores que no se verificaron no entran.

> [!NOTE] Sin fuente todavía: un experimento con adultos que aprenden programación con asistentes de IA, y una revisión sistemática del subcampo.
