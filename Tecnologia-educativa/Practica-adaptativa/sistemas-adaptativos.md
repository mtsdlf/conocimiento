---
resumen: >-
  Un sistema adaptativo es un programa de práctica que mantiene un mapa de qué temas domina cada alumno y elige con él el próximo ejercicio, el próximo prerrequisito o el próximo repaso. Su diseño se apoya en técnicas con evidencia, pero casi no hay estudios independientes de que un producto concreto enseñe más.
estado: borrador
estabilidad: estable
fuentes:
  - "Skycak, J. (2023, actualizado en 2026), Individualized Spaced Repetition in Hierarchical Knowledge Structures: https://justinmath.com/individualized-spaced-repetition-in-hierarchical-knowledge-structures/ (del autor y proveedor)"
  - "Escueta, Nickow, Oreopoulos y Quan (2020), Journal of Economic Literature 58(4):897-996: https://www.aeaweb.org/doi/10.1257/jel.20191507 (resumen)"
  - "Oreopoulos y Low (2026), NBER w35620: https://www.nber.org/papers/w35620"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [adaptive learning system, aprendizaje adaptativo, grafo de conocimiento, knowledge graph, repaso jerárquico, hierarchical spaced repetition, aprendizaje para el dominio, mastery learning, aprendizaje asistido por computadora]
creado: 2026-11-27
revisado:
---

# Sistemas adaptativos

Un sistema adaptativo es un programa de práctica que mantiene un mapa de qué temas domina cada alumno y elige con él el próximo ejercicio, el próximo prerrequisito o el próximo repaso. Su diseño se apoya en técnicas con evidencia, pero casi no hay estudios independientes de que un producto concreto enseñe más.

Hace a escala de un curso lo que el [tutor inteligente](../Tutores-inteligentes/tutores-inteligentes.md) hace dentro de un problema: el trazado de conocimiento de la [arquitectura de un tutor](../Tutores-inteligentes/arquitectura-de-un-tutor-inteligente.md) estima qué habilidades se dominan para elegir el próximo problema, y un sistema adaptativo hace lo mismo con todo el temario. Se diferencia del [repaso espaciado con software](repaso-espaciado-con-software.md) en que no solo decide cuándo repasar, sino también qué aprender después.

## Cómo decide qué practicar

El sistema tiene un mapa del temario: qué temas hay y cuáles necesitan a cuáles. Suele arrancar con un diagnóstico que ubica al alumno en ese mapa. Después, con cada ejercicio, actualiza qué domina, y elige entre tres movidas: volver a un prerrequisito que falta, avanzar a un tema para el que ya tiene lo necesario o repasar algo que se está por olvidar.

La descripción es la que dan los proveedores y la lógica del trazado de conocimiento; no viene de una revisión independiente.

## El repaso jerárquico

Un problema de combinar el mapa con el repaso espaciado es que, en matemática, los temas avanzados ejercitan los simples. Si cada tema tuviera su propio calendario de repaso, el alumno repasaría de más lo que ya practica al resolver lo avanzado.

La propuesta de Justin Skycak (2023, renombrada en 2026 como «Hierarchical Spaced Repetition») resuelve eso con repeticiones implícitas fraccionarias. Aprobar un tema avanzado cuenta como repaso parcial de los temas más simples que ejercita; fallar uno simple penaliza hacia arriba a los avanzados que dependen de él. Usa un grafo propio, distinto del de prerrequisitos, que dice qué tema «abarca» a cuál, con pesos puestos por un experto.

Es un diseño con respaldo teórico y sin evidencia de efecto. El propio autor dice que no hay estudios académicos del sistema; lo que ofrece son resultados de su escuela y reportes de usuarios. El producto que lo implementa está en la ficha de [herramientas de práctica adaptativa](herramientas-de-practica-adaptativa.md).

## Qué se sabe del efecto

Escueta et al. (2020) ubican estos sistemas dentro del aprendizaje asistido por computadora, una de sus cuatro categorías de tecnología educativa. Esta base no leyó sus conclusiones por categoría.

El único ensayo adaptativo verificado en esta base es indirecto. En el ensayo de dos años de Oreopoulos y Low (2026, documento de trabajo del NBER, sin revisión por pares), el tutor de IA dio, según su resumen, un efecto parecido al de la práctica de Khan Academy sin IA: de 0,06 a 0,08 desvíos por año. La práctica adaptativa y la tutoría por chat dieron efectos parecidos y chicos, en escolares de matemática remedial.

> [!NOTE]
> Sin fuente todavía: un metaanálisis de sistemas adaptativos comerciales (ALEKS, Duolingo y otros) y las conclusiones de Escueta et al. sobre el aprendizaje asistido por computadora. Para los tutores inteligentes, que son la familia más estudiada, está [evidencia de los tutores inteligentes](../Tutores-inteligentes/evidencia-de-los-tutores-inteligentes.md).

## Cómo leer la promesa de un producto

Como lectura de esta base: que un sistema cite técnicas con evidencia (práctica distribuida, intercalado, efecto del testeo, ejemplos resueltos) no prueba que el sistema enseñe más. La evidencia es de la técnica, no del producto. La pregunta para un proveedor es si hay un estudio con grupo de control y una prueba externa, como pide [fuentes de tecnología educativa](../Fundamentos/fuentes-de-tecnologia-educativa.md).
