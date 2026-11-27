---
resumen: >-
  Las pistas de un tutor inteligente son la forma en que su modelo pedagógico gradúa la ayuda: primero una pista general, después otras más concretas y al final una que da el paso. Bajar hasta la última sin pensar es abuso de la ayuda, pero leerla con cuidado puede funcionar como estudiar un ejemplo resuelto.
estado: vigente
estabilidad: estable
fuentes:
  - "Shih, B., Koedinger, K. R. y Scheines, R. (2008), A Response Time Model for Bottom-Out Hints as Worked Examples, Educational Data Mining 2008: https://www.cmu.edu/dietrich/philosophy/docs/scheines/Shih_Koedinger_Scheines_2008_EDM.pdf"
  - "Wikipedia, Cognitive tutor: https://en.wikipedia.org/wiki/Cognitive_tutor (terciaria)"
  - "Bastani et al. (2025), PNAS 122(26): https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html"
  - "Tecnologia-educativa/.investigacion/medios-en-linea-tutores.md"
  - "Anderson, J. R., Corbett, A. T., Koedinger, K. R. y Pelletier, R. (1995), Cognitive Tutors: Lessons Learned, Journal of the Learning Sciences 4(2):167-207, DOI 10.1207/s15327809jls0402_2: https://kilthub.cmu.edu/articles/journal_contribution/Cognitive_Tutors_Lessons_Learned/6469901 (texto completo escaneado; leídas págs. 168-176 y 196)"
  - "Aleven, V., McLaren, B., Roll, I. y Koedinger, K. (2006), Toward Meta-cognitive Tutoring: A Model of Help Seeking with a Cognitive Tutor, International Journal of Artificial Intelligence in Education 16:101-130: https://kilthub.cmu.edu/articles/journal_contribution/Toward_Meta-Cognitive_Tutoring_A_Model_of_Help-Seeking_with_a_Cognitive_Tutor/6470573 (texto completo)"
  - "Roll, I., Aleven, V., McLaren, B. M. y Koedinger, K. R. (2011), Improving students' help-seeking skills using metacognitive feedback in an intelligent tutoring system, Learning and Instruction 21(2):267-280, DOI 10.1016/j.learninstruc.2010.07.004: https://www.cs.cmu.edu/~bmclaren/pubs/RollEtAl-ImprovingMetacogSkillsWithITS-LandI2010.pdf (texto completo, versión de autor)"
  - "Tecnologia-educativa/.investigacion/fuentes-tutores-y-plataformas-2026-11.md"
aliases: [pistas de un tutor, bottom-out hint, última pista, help abuse, gaming the system, abuso de la ayuda, next-step hints]
creado: 2026-11-27
revisado: 2026-11-27
---

# Pistas de un tutor inteligente

Las pistas de un tutor inteligente son la forma en que su modelo pedagógico gradúa la ayuda: primero una pista general, después otras más concretas y al final una que da el paso. Bajar hasta la última sin pensar es abuso de la ayuda, pero leerla con cuidado puede funcionar como estudiar un ejemplo resuelto.

Es una pieza del modelo pedagógico, una de las cuatro de la [arquitectura de un tutor inteligente](arquitectura-de-un-tutor-inteligente.md). Es la versión programada de la [escalera de pistas](../../Didactica/Retroalimentacion/escalera-de-pistas.md) que usan los tutores humanos expertos en la [tutoría](../../Didactica/Tutoria-y-mentoria/tutoria.md), explicada en Didáctica; esta nota cubre lo propio del programa: cómo se arma y cómo la usan los alumnos.

## Cómo se arma la escalera

Los tutores cognitivos dan pistas del siguiente paso cuando el alumno las pide. La escalera tiene tres tramos:

1. Pista general: recuerda qué principio o qué meta aplica, sin decir cómo («¿qué querés dejar sola en un lado?»).
2. Pista más concreta: señala la operación o el dato que falta («fijate en el coeficiente de la x»).
3. Última pista (*bottom-out hint*): da el paso entero («dividí los dos lados por 3»).

Los ejemplos entre paréntesis son ilustración de esta base. Según Wikipedia, el riesgo conocido de estas pistas es que el alumno llegue a la respuesta sin cumplir los objetivos de aprendizaje.

La ayuda a pedido ya estaba en el tutor de LISP de mediados de los 80. Según Anderson, Corbett, Koedinger y Pelletier (1995), si el alumno pide una explicación o parece trabado, ese tutor «will also provide a correct next step in a solution, along with an explanation». En esa descripción (se leyeron las págs. 168 a 176 y 196) la ayuda es un solo mensaje, no una escalera.

En el tutor cognitivo de geometría que describen Aleven, McLaren, Roll y Koedinger (2006), la ayuda ya es una secuencia, «with each hint providing increasingly more specific advice». Su ejemplo tiene siete niveles, que caen en los tres tramos: del 1 al 3 señalan un rasgo del problema y mandan al glosario, del 4 al 6 nombran el teorema y cómo se aplica, y el 7 da la expresión que resuelve el paso. Ninguna secuencia de ese tutor pasaba de ocho niveles.

> [!NOTE]
> Sin fuente todavía: desde cuándo exactamente la ayuda de los tutores cognitivos es una secuencia por niveles. Lo leído la ubica entre el tutor de LISP de los 80, que daba el paso siguiente en un mensaje, y el tutor de geometría descripto en 2006.

## Abuso de la ayuda o ejemplo resuelto

Algunos alumnos saltean las pistas abstractas y van directo a la última. La literatura de tutores lo llamaba «gaming or help abuse». Shih, Koedinger y Scheines (2008) muestran que no siempre lo es: «some examples of this behavior are not abusive and … bottom-out hints can act as worked examples».

El abuso es frecuente. En los registros del tutor de geometría que analizaron Aleven et al. (2006), el 73 % de las acciones de los alumnos no seguía su modelo de buen uso de la ayuda. El error metacognitivo más frecuente fue el abuso de la ayuda (36 %), casi todo pasar las pistas sin leerlas (33 %). Cuantos más errores de este tipo, menos aprendía el alumno (correlación parcial de –0,65, descontado el puntaje previo).

Lo que separa un caso del otro es el tiempo. Su modelo usa cuánto tarda el alumno después de recibir la última pista para distinguir a quien la copia y sigue de quien se detiene a entenderla. El buen uso, así detectado, predice aprendizaje y «captures behaviors related to self-explanation»: el alumno se explica a sí mismo por qué el paso es correcto. Un [ejemplo resuelto](../../Didactica/Explicar-y-modelar/modelado-y-ejemplos-resueltos.md) enseña cuando se lo estudia, y explicarse cada paso es la [autoexplicación](../../Didactica/Preguntas-y-dialogo/autoexplicacion.md), y la última pista es un ejemplo resuelto de un paso.

## Qué pasa cuando la última pista está siempre disponible

Como lectura de esta base, un chat con un modelo de lenguaje sin instrucciones es una escalera que empieza en la última pista: da el paso, o la solución entera, al primer pedido. El experimento de Bastani et al. (2025) muestra el costo. Los alumnos que practicaron con un chat abierto rindieron 17 % menos que el grupo de control cuando les sacaron la IA, y en los registros de esos alumnos la mayoría pedía la respuesta. Los que practicaron con un tutor con [guardas](../IA-en-la-educacion/ia-como-tutor.md#el-diseño-decide-si-suma-o-resta), que no daba la respuesta, no rindieron peor que el control. El estudio está en [la IA como tutor](../IA-en-la-educacion/ia-como-tutor.md).

Como inferencia de esta base, al diseñar un tutor (con IA o sin ella) la escalera da tres decisiones: cuántos tramos hay antes de la última pista, si la última se puede pedir enseguida o exige intentar antes, y si se mira el tiempo después de darla para detectar a quien copia sin leer.

## Enseñar a pedir ayuda

Enseñar a pedir ayuda mejoró cómo los alumnos pedían ayuda, pero no lo que aprendieron de la materia. Roll, Aleven, McLaren y Koedinger (2011) sumaron al tutor de geometría el Help Tutor, que corrige al momento los errores al pedir ayuda. En el primer estudio, con 58 alumnos, el Help Tutor mejoró la forma de pedir ayuda; en el segundo, con 67, se agregó instrucción y autoevaluación, y los alumnos pasaron más tiempo antes de pedir el nivel siguiente y pidieron menos últimas pistas.

En el segundo estudio, la mejora siguió en unidades nuevas, sin el apoyo, en el cuarto mes y no en el segundo. En ninguno de los dos estudios cambió lo aprendido de geometría: el primero no encontró «effect of the Help Tutor on students' learning gains», y el segundo, ningún efecto «on domain learning» en los meses en que se midió. Los autores proponen dos explicaciones sin probar: que la mejora fue chica para mover las notas, o que los mensajes del Help Tutor sumaron carga cognitiva.

Como inferencia de esta base, enseñar a usar la escalera no reemplaza diseñarla bien.
