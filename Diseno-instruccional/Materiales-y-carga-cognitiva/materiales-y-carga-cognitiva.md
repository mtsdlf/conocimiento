---
resumen: >-
  Los materiales son lo que quien aprende lee, mira o usa: textos, diagramas, videos, ejemplos. Se diseñan para no gastar la memoria de trabajo en lo que no enseña, según la teoría de la carga cognitiva y los principios multimedia de Mayer, la parte del diseño instruccional con más evidencia experimental, casi toda de laboratorio.
estado: vigente
estabilidad: estable
fuentes:
  - "Mayer (2023), Research-Based Principles for Designing Multimedia Instruction, en In Their Own Words, APA Division 2: https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-research-based-principles-for-designing-multimedia-instruction-mayer.pdf"
  - "de Jong (2010), Cognitive load theory, educational research, and instructional design: some food for thought, Instructional Science 38(2), 105-134, doi 10.1007/s11251-009-9110-0: https://ris.utwente.nl/ws/files/6597420/Jong10cognitive.pdf"
  - "Sweller, van Merriënboer y Paas (2019), Cognitive Architecture and Instructional Design: 20 Years Later, Educational Psychology Review 31, 261-292 (no leído)"
  - "Schroeder y Cenkci (2018), Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis, Educational Psychology Review, doi 10.1007/s10648-018-9435-9: https://eric.ed.gov/?id=EJ1186641 (abstract)"
  - "Chandler y Sweller (1992), The split-attention effect as a factor in the design of instruction, British Journal of Educational Psychology 62, 233-246, doi 10.1111/j.2044-8279.1992.tb01017.x (solo la ficha)"
  - "Catrambone (1995), Aiding subgoal learning: Effects on transfer, Journal of Educational Psychology: https://eric.ed.gov/?id=EJ505854 (abstract)"
  - "Margulieux, Catrambone y Guzdial (2016), Employing subgoals in computer programming education, Computer Science Education, doi 10.1080/08993408.2016.1144429: https://eric.ed.gov/?id=EJ1096330 (abstract)"
  - "Guo, Kim y Rubin (2014), How Video Production Affects Student Engagement: An Empirical Study of MOOC Videos, Learning at Scale 2014, doi 10.1145/2556325.2566239: https://www.cs.rochester.edu/hci/pubs/pdfs/edX-MOOC-video-production-and-engagement_LAS-2014.pdf (texto completo)"
  - "Diseno-instruccional/.investigacion/modelos-materiales-formatos.md"
  - "Diseno-instruccional/.investigacion/fuentes-modelos-y-materiales-2026-11.md"
aliases: [materiales didácticos, materiales instruccionales, diseño de materiales, instructional materials, diseño multimedia]
creado: 2026-11-27
revisado: 2026-11-27
---

# Materiales y carga cognitiva

Los materiales son lo que quien aprende lee, mira o usa: textos, diagramas, videos, ejemplos. Se diseñan para no gastar la memoria de trabajo en lo que no enseña, según la teoría de la carga cognitiva y los principios multimedia de Mayer, la parte del diseño instruccional con más evidencia experimental, casi toda de laboratorio.

Es la D de desarrollo en [ADDIE](../Modelos-de-diseno/addie-y-sam.md). Recibe de la [secuencia](../Secuencia-y-curriculo/secuencia-y-curriculo.md) qué va en cada paso y del [análisis de quien aprende](../Analisis-previo/analisis-de-quien-aprende.md) cuánto sabe ya, que cambia qué material le sirve. El soporte en que se entregan (plataformas, video, herramientas) está en [plataformas de aprendizaje](../../Tecnologia-educativa/Aprendizaje-en-linea/plataformas-de-aprendizaje.md) y [video educativo](../../Tecnologia-educativa/Aprendizaje-en-linea/video-educativo.md), de Tecnología educativa.

## Una idea con dos niveles

La vertical se apoya en una sola idea: la memoria de trabajo es chica, y lo que la ocupa sin enseñar le quita lugar a lo que enseña. La [carga cognitiva en el aprendizaje](carga-cognitiva-en-el-aprendizaje.md) es la teoría que lo explica y sus críticas; los [principios multimedia](principios-multimedia.md) son las reglas concretas que salen de ella, con sus tamaños de efecto y sus condiciones de borde. El mecanismo general de la memoria de trabajo está en [memoria](../../Psicologia/Aprendizaje-y-memoria/memoria.md), y la misma idea aplicada a pantallas, en [carga cognitiva](../../UX/Percepcion-y-decision/carga-cognitiva.md) del tema UX.

## Qué tan lejos llega la evidencia

Es la parte del tema con más experimentos, pero con tres límites que cambian cómo se aplica:

- **Laboratorio y lecciones cortas.** La mayoría de los estudios usan lecciones de minutos sobre mecanismos físicos (una bomba de aire, la formación de rayos, los frenos) y pruebas de [transferencia](../../Ciencias-del-aprendizaje/Transferencia/transferencia.md) inmediatas (resolver problemas nuevos con lo aprendido). Llevar eso a un curso de semanas es un salto que las fuentes no prueban.
- **Medianas del mismo grupo.** Los tamaños de efecto que da Mayer son medianas de estudios de su propio grupo.
- **La carga casi no se mide.** de Jong (2010) muestra que en muchos estudios la carga se infiere del resultado, y que atribuir la mejora a menos carga extrínseca es una explicación a posteriori.

Que todo esto valga para adultos que aprenden IT es una extrapolación: ninguno de los estudios verificados es de capacitación en IT.

## Qué hay adentro de los materiales

- [Carga cognitiva en el aprendizaje](carga-cognitiva-en-el-aprendizaje.md): las cargas intrínseca, extrínseca y pertinente aplicadas al material didáctico, el efecto de inversión de la experticia y la crítica de de Jong.
- [Principios multimedia](principios-multimedia.md): los nueve principios de Mayer con cuántos tests los apoyan, sus medianas y cuándo dejan de valer.

## Tres pautas sin nota propia todavía

- **Atención dividida.** Si el texto y el gráfico que se explican entre sí están separados, quien aprende tiene que juntarlos en la cabeza. Un metaanálisis de 58 comparaciones (n = 2426) encontró g = 0,63 a favor de integrarlos, según su resumen (Schroeder y Cenkci 2018); es pariente de la contigüidad espacial de los [principios multimedia](principios-multimedia.md).
- **Ejemplos resueltos con subobjetivos.** Catrambone (1995), según su resumen, mostró con 218 universitarios que etiquetar y aislar los pasos de un ejemplo ayuda a resolver problemas nuevos que usan ese subobjetivo. En programación, según su resumen, Margulieux, Catrambone y Guzdial (2016) sugieren mejoras en el laboratorio y efectos parecidos en un entorno de aprendizaje en línea con docentes en ejercicio que querían enseñar computación; el detalle está en [modelado y ejemplos resueltos](../../Didactica/Explicar-y-modelar/modelado-y-ejemplos-resueltos.md).
- **Videos cortos.** Guo, Kim y Rubin (2014) encontraron en 6,9 millones de sesiones de edX que la mediana de lo que se mira es «at most 6 minutes», y recomiendan tramos más cortos. Midieron cuánto se mira, no cuánto se aprende; el análisis está en [video educativo](../../Tecnologia-educativa/Aprendizaje-en-linea/video-educativo.md).

> [!NOTE] Sin fuente todavía: el texto de Chandler y Sweller (1991, 1992) y un estudio de estas tres pautas en capacitación de adultos en IT. Son candidatos a una nota propia.
