---
resumen: >-
  Las pistas de un tutor inteligente son la forma en que su modelo pedagógico gradúa la ayuda: primero una pista general, después otras más concretas y al final una que da el paso. Bajar hasta la última sin pensar es abuso de la ayuda, pero leerla con cuidado puede funcionar como estudiar un ejemplo resuelto.
estado: borrador
estabilidad: estable
fuentes:
  - "Shih, B., Koedinger, K. R. y Scheines, R. (2008), A Response Time Model for Bottom-Out Hints as Worked Examples, Educational Data Mining 2008: https://www.cmu.edu/dietrich/philosophy/docs/scheines/Shih_Koedinger_Scheines_2008_EDM.pdf"
  - "Wikipedia, Cognitive tutor: https://en.wikipedia.org/wiki/Cognitive_tutor (terciaria)"
  - "Bastani et al. (2025), PNAS 122(26): https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html"
  - "Tecnologia-educativa/.investigacion/medios-en-linea-tutores.md"
aliases: [pistas de un tutor, bottom-out hint, última pista, help abuse, gaming the system, abuso de la ayuda, next-step hints]
creado: 2026-11-27
revisado:
---

# Pistas de un tutor inteligente

Las pistas de un tutor inteligente son la forma en que su modelo pedagógico gradúa la ayuda: primero una pista general, después otras más concretas y al final una que da el paso. Bajar hasta la última sin pensar es abuso de la ayuda, pero leerla con cuidado puede funcionar como estudiar un ejemplo resuelto.

Es una pieza del modelo pedagógico, una de las cuatro de la [arquitectura de un tutor inteligente](arquitectura-de-un-tutor-inteligente.md). Es la versión programada de la [escalera de pistas](../../Didactica/Retroalimentacion/escalera-de-pistas.md) que usan los tutores humanos expertos, explicada en Didáctica; esta nota cubre lo propio del programa: cómo se arma y cómo la usan los alumnos.

## Cómo se arma la escalera

Los tutores cognitivos dan pistas del siguiente paso cuando el alumno las pide. La escalera tiene tres tramos:

1. **Pista general**: recuerda qué principio o qué meta aplica, sin decir cómo («¿qué querés dejar sola en un lado?»).
2. **Pista más concreta**: señala la operación o el dato que falta («fijate en el coeficiente de la x»).
3. **Última pista** (*bottom-out hint*): da el paso entero («dividí los dos lados por 3»).

Los ejemplos entre paréntesis son ilustración de esta base. Según Wikipedia, el riesgo conocido de estas pistas es que el alumno llegue a la respuesta sin cumplir los objetivos de aprendizaje.

> [!NOTE]
> Sin fuente todavía: desde cuándo los tutores cognitivos usan escaleras de pistas, y el trabajo de Aleven et al. sobre enseñar a pedir ayuda. Ninguno se verificó.

## Abuso de la ayuda o ejemplo resuelto

Algunos alumnos saltean las pistas abstractas y van directo a la última. La literatura de tutores lo llamaba «gaming or help abuse». Shih, Koedinger y Scheines (2008) muestran que no siempre lo es: «some examples of this behavior are not abusive and … bottom-out hints can act as worked examples».

Lo que separa un caso del otro es el tiempo. Su modelo usa cuánto tarda el alumno después de recibir la última pista para distinguir a quien la copia y sigue de quien se detiene a entenderla. El buen uso, así detectado, predice aprendizaje y «captures behaviors related to self-explanation»: el alumno se explica a sí mismo por qué el paso es correcto. Un ejemplo resuelto enseña cuando se lo estudia, y la última pista es un ejemplo resuelto de un paso.

## Qué pasa cuando la última pista está siempre disponible

Un chat con un modelo de lenguaje sin instrucciones es una escalera que empieza en la última pista: da el paso, o la solución entera, al primer pedido. El experimento de Bastani et al. (2025) muestra el costo. Los alumnos que practicaron con un chat abierto rindieron 17 % menos que el grupo de control cuando les sacaron la IA, y en los registros la mayoría pedía la respuesta. Los que practicaron con un tutor con guardas, que no daba la respuesta, no rindieron peor que el control. El estudio está en [la IA como tutor](../IA-en-la-educacion/ia-como-tutor.md).

Como inferencia de esta base, al diseñar un tutor (con IA o sin ella) la escalera da tres decisiones: cuántos tramos hay antes de la última pista, si la última se puede pedir enseguida o exige intentar antes, y si se mira el tiempo después de darla para detectar a quien copia sin leer.
