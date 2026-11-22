---
resumen: >-
  Percepción y decisión reúne lo que se sabe de cómo la gente entiende, recuerda y elige frente a una pantalla. Dice qué es fácil y qué es caro para una mente, y dónde termina la persuasión legítima.
estado: vigente
estabilidad: estable
fuentes:
  - "Norman, The Design of Everyday Things (ed. revisada, 2013), a través de NN/g: https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/"
  - "Cowan (2001), The magical number 4 in short-term memory, Behavioral and Brain Sciences 24(1): https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf"
  - "Liu et al. (2020), How Relevant is Hick's Law for HCI?, CHI 2020: https://researchportal.ip-paris.fr/en/publications/how-relevant-is-hicks-law-for-hci/"
  - "Mathur, Mayer y Kshirsagar (2021), What Makes a Dark Pattern... Dark?, CHI 2021: https://arxiv.org/abs/2101.04843"
  - "NN/g, Proximity Principle (Gestalt): https://www.nngroup.com/articles/gestalt-proximity/"
  - "UX/.investigacion/percepcion-y-decision.md"
aliases: [psicología del usuario, factores humanos, cognición y diseño]
creado: 2026-11-22
revisado: 2026-11-22
---

# Percepción y decisión

Percepción y decisión reúne lo que se sabe de cómo la gente entiende, recuerda y elige frente a una pantalla. Dice qué es fácil y qué es caro para una mente, y dónde termina la persuasión legítima.

Es la base científica del tema [UX](../ux.md): pone los límites con que trabajan las demás partes. La [Arquitectura de información](../Arquitectura-de-informacion/arquitectura-de-informacion.md) se organiza para que la gente encuentre sin esfuerzo, la [Interacción](../Interaccion/interaccion.md) se diseña para que las acciones se entiendan, y el [Diseño visual](../Diseno-visual/diseno-visual.md) decide qué se ve primero. Cada una se apoya en lo que acá se describe como costoso o barato para una persona.

La vertical trata la parte cognitiva: qué cree la persona, cuánto esfuerzo mental gasta, cuánto tarda en apuntar y en elegir, y cuánto se la puede empujar. La percepción visual propiamente dicha va en otro lado. Las fuentes de UX ubican la Gestalt (proximidad, agrupamiento) en diseño visual, por ejemplo NN/g, que llama a la proximidad "a foundational principle in visual design"; su teoría está en [Diseño visual](../Diseno-visual/diseno-visual.md).

## Lo que la persona cree, lo que esfuerza y lo que tarda

Tres ideas se encadenan. Primero, la persona actúa según lo que cree que hace el sistema, que es su [modelo mental](modelo-mental.md); si difiere del real, se equivoca aunque la interfaz sea correcta. Segundo, entender y recordar gastan recursos mentales limitados, que la [carga cognitiva](carga-cognitiva.md) mide: se reduce el procesamiento que no ayuda a la tarea, sin contar elementos por pantalla. Tercero, apuntar a un blanco y elegir entre alternativas tienen costos de tiempo que describen las [leyes de Fitts y Hick](leyes-de-fitts-y-hick.md), y solo la primera tiene respaldo en diseño de interfaces; sobre la segunda, Liu et al. (2020) dudan.

Esta vertical corrige dos reglas populares. La de 7±2 elementos nace de un trabajo sobre memoria que Cowan revisó a la baja (unos cuatro chunks). Esa memoria retiene ítems; que un menú visible no la use es inferencia de esta base. Según Liu et al. (2020), la ley de Hick no prueba que menos opciones acelere la decisión. Las notas de abajo desarrollan las dos con su evidencia.

## Dónde la persuasión pasa a ser engaño

Lo que la gente hace fácil o difícil también se puede explotar. El [patrón oscuro](patron-oscuro.md) es el diseño que lleva a decidir lo que no se habría decidido. La definición es disputada: según Mathur, Mayer y Kshirsagar (2021) hay 19 definiciones que difieren en si exigen engaño, intención del diseñador o daño. Hay evidencia de que estos patrones funcionan, y hay regulación en EE. UU. y la UE, que la nota resume con fecha. La [economía del comportamiento aplicada al mensaje](../../Marketing/Comunicacion/economia-del-comportamiento-en-marketing.md), que cubre el tema Marketing, estudia los mismos sesgos desde el lado de la comunicación.

## Qué hay adentro

- [Modelo mental](modelo-mental.md): lo que la persona cree que hace el sistema, los dos golfos de Norman y por qué reconocer pesa menos que recordar.
- [Carga cognitiva](carga-cognitiva.md): el esfuerzo mental de una interfaz, la distinción entre intrínseca y extrínseca, y el debate de Miller contra Cowan sobre cuánto retiene la memoria.
- [Leyes de Fitts y Hick](leyes-de-fitts-y-hick.md): el tiempo de apuntar y el de elegir, con las fórmulas y los límites de cada una.
- [Patrón oscuro](patron-oscuro.md): los tipos, la evidencia de que funcionan, las posiciones sobre dónde termina la persuasión y la normativa con fecha.

## Qué falta

Dos componentes que esta vertical va a sumar y todavía no existen:

- Percepción visual y atención: cómo se explora una pantalla, la búsqueda visual y la ceguera a los banners. La nota de Hick remite a la búsqueda visual como el modelo más pertinente que la ley.
- Memoria y aprendizaje: la memoria de largo plazo y cómo la gente construye esquemas con el uso. Completa lo que [Carga cognitiva](carga-cognitiva.md) solo toca en la memoria de trabajo.

Los umbrales de tiempo de respuesta del sistema (0,1 s, 1 s y 10 s) no se tratan acá: están en [Principios de interacción](../Interaccion/principios-de-interaccion.md).
