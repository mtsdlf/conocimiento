---
resumen: >-
  Un sistema adaptativo es un programa de práctica que mantiene un mapa de qué temas domina cada alumno y elige con él el próximo ejercicio, el próximo prerrequisito o el próximo repaso. Su diseño se apoya en técnicas con evidencia, pero casi no hay estudios independientes de que un producto concreto enseñe más.
estado: vigente
estabilidad: estable
fuentes:
  - "Skycak, J. (2023, actualizado en 2026), Individualized Spaced Repetition in Hierarchical Knowledge Structures: https://justinmath.com/individualized-spaced-repetition-in-hierarchical-knowledge-structures/ (del autor y proveedor)"
  - "Escueta, Nickow, Oreopoulos y Quan (2020), Journal of Economic Literature 58(4):897-996: https://www.aeaweb.org/doi/10.1257/jel.20191507 (resumen)"
  - "J-PAL (2019), Will technology transform education for the better? (evidence review, resumen del artículo de Escueta et al.): https://www.povertyactionlab.org/sites/default/files/2020-03/education-technology-evidence-review.pdf (texto completo)"
  - "Quan, V. (2017-09-05), Exploring the promise of education technology, blog de J-PAL: https://www.povertyactionlab.org/node/4552 (texto completo)"
  - "Fang, Y., Ren, Z., Hu, X. y Graesser, A. (2019), A meta-analysis of the effectiveness of ALEKS on learning, Educational Psychology 39(10):1278-1292: https://doi.org/10.1080/01443410.2018.1495829 (abstract)"
  - "Sun, S., Else-Quest, N. M., Hodges, L. C., French, A. M. y Dowling, R. (2021), The Effects of ALEKS on Mathematics Learning in K-12 and Higher Education: A Meta-Analysis, Investigations in Mathematics Learning 13(3):182-196: https://doi.org/10.1080/19477503.2021.1926194 (abstract)"
  - "Oreopoulos y Low (2026), NBER w35620: https://www.nber.org/papers/w35620"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
  - "Tecnologia-educativa/.investigacion/fuentes-ia-y-practica-adaptativa-2026-11.md"
aliases: [adaptive learning system, aprendizaje adaptativo, grafo de conocimiento, knowledge graph, repaso jerárquico, hierarchical spaced repetition, aprendizaje para el dominio, mastery learning, aprendizaje asistido por computadora]
creado: 2026-11-27
revisado: 2026-11-27
---

# Sistemas adaptativos

Un sistema adaptativo es un programa de práctica que mantiene un mapa de qué temas domina cada alumno y elige con él el próximo ejercicio, el próximo prerrequisito o el próximo repaso. Su diseño se apoya en técnicas con evidencia, pero casi no hay estudios independientes de que un producto concreto enseñe más.

Como lectura de esta base, hace a escala de un curso lo que el [tutor inteligente](../Tutores-inteligentes/tutores-inteligentes.md) hace dentro de un problema: el trazado de conocimiento de la [arquitectura de un tutor](../Tutores-inteligentes/arquitectura-de-un-tutor-inteligente.md) estima qué habilidades se dominan para elegir el próximo problema, y un sistema adaptativo hace lo mismo con todo el temario. Se diferencia del [repaso espaciado con software](repaso-espaciado-con-software.md) en que no solo decide cuándo repasar, sino también qué aprender después.

## Cómo decide qué practicar

El sistema tiene un mapa del temario: qué temas hay y cuáles necesitan a cuáles. Suele arrancar con un diagnóstico que ubica al alumno en ese mapa; la lógica de esa medición está en [evaluación adaptativa](../../Evaluacion-educativa/Evaluacion-adaptativa/evaluacion-adaptativa.md) y [espacios de conocimiento](../../Evaluacion-educativa/Evaluacion-adaptativa/espacios-de-conocimiento.md). Después, con cada ejercicio, actualiza qué domina, y elige entre tres movidas: volver a un prerrequisito que falta, avanzar a un tema para el que ya tiene lo necesario o repasar algo que se está por olvidar.

La descripción es la que dan los proveedores y la lógica del trazado de conocimiento; no viene de una revisión independiente.

## El repaso jerárquico

Como lectura de esta base (la fuente no lo plantea así), el problema de combinar el mapa con el repaso espaciado es que, en matemática, los temas avanzados ejercitan los simples. Si cada tema tuviera su propio calendario de repaso, el alumno repasaría de más lo que ya practica al resolver lo avanzado.

La propuesta de Justin Skycak (2023, renombrada en 2026 como «Hierarchical Spaced Repetition») resuelve eso con repeticiones implícitas fraccionarias. Aprobar un tema avanzado cuenta como repaso parcial de los temas más simples que ejercita; fallar uno simple penaliza hacia arriba a los avanzados que dependen de él. Usa un grafo propio, distinto del de prerrequisitos, que dice qué tema «abarca» a cuál, con pesos puestos por un experto.

Es un diseño con respaldo teórico y sin evidencia de efecto. El propio autor dice que no hay estudios académicos del sistema; lo que ofrece son resultados de su escuela y reportes de usuarios. El producto que lo implementa está en la ficha de [herramientas de práctica adaptativa](herramientas-de-practica-adaptativa.md).

## Qué se sabe del efecto

Escueta et al. (2020) ubican estos sistemas dentro del aprendizaje asistido por computadora, una de sus cuatro categorías de tecnología educativa. El artículo no se pudo leer; sus conclusiones llegan por el resumen que publicó J-PAL en 2019, antes de la versión de la revista. Según J-PAL, de 30 estudios de aprendizaje asistido por computadora, 20 dieron efectos positivos significativos, y 15 de esos 20 eran de matemática. El mismo resumen dice que hay «some evidence» de que estos programas suben las notas tanto como una tutoría eficaz, y que falta entender por qué unos programas funcionan mejor que otros. Según un coautor, rindieron más usados en clase o como tarea obligatoria.

ALEKS, uno de los tutores en línea más usados en Estados Unidos según Fang et al., rinde como la clase tradicional. Fang et al. (2019) reunieron 15 estudios de 2005 a 2015 y, según su resumen, ALEKS fue «as good, but not better than, traditional classroom teaching»; el efecto fue mayor con usos más cortos. Sun et al. (2021) reunieron 33 estudios con 9.238 alumnos y, según su resumen, dieron g = 0,05 (IC 95 % −0,01 a 0,20, así en el resumen, aunque el intervalo no queda centrado en el valor) frente a la enseñanza tradicional y g = 0,43 (0,02 a 0,83) cuando ALEKS la complementa. Los dos discrepan en eso: Fang et al. no encontraron diferencia entre usarlo como enseñanza principal o de apoyo.

El único ensayo reciente leído en esta base es indirecto. En el ensayo de dos años de Oreopoulos y Low (2026, documento de trabajo del NBER, sin revisión por pares), el tutor de IA dio de 0,06 a 0,08 [desviaciones estándar](../../Didactica/Fundamentos/glosario-de-didactica.md#leer-la-evidencia) por año, que según su resumen es un efecto parecido al de la práctica de Khan Academy sin IA. La práctica adaptativa y la tutoría por chat dieron efectos parecidos y chicos, en escolares de matemática remedial.

> [!NOTE]
> Sin fuente todavía: un metaanálisis de varios sistemas adaptativos comerciales a la vez (Duolingo y otros, más allá de ALEKS) y el texto de Escueta et al. (2020), que dio 403; lo de arriba sale del resumen de J-PAL. Para los tutores inteligentes, que son una de las familias con más evidencia en esta base, está [evidencia de los tutores inteligentes](../Tutores-inteligentes/evidencia-de-los-tutores-inteligentes.md).

## Cómo leer la promesa de un producto

Como lectura de esta base: que un sistema cite técnicas con evidencia (práctica distribuida, intercalado, efecto de testeo, ejemplos resueltos) no prueba que el sistema enseñe más. La evidencia es de la técnica, no del producto. La pregunta para un proveedor es si hay un estudio con grupo de control y una prueba externa, como pide [fuentes de tecnología educativa](../Fundamentos/fuentes-de-tecnologia-educativa.md).
