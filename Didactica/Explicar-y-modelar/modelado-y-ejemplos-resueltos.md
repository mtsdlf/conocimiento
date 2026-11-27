---
resumen: >-
  Modelar es mostrar cómo se resuelve algo haciendo visible el razonamiento que un experto lleva oculto, pensando en voz alta o con ejemplos resueltos paso a paso. El ejemplo resuelto es de las técnicas con mejor respaldo experimental, y sirve sobre todo a quien recién empieza.
estado: vigente
estabilidad: estable
fuentes:
  - "Rosenshine (2012), Principles of Instruction, American Educator (principios 4 y 8): https://www.aft.org/sites/default/files/Rosenshine.pdf (lectura completa)"
  - "Atkinson, Derry, Renkl y Wortham (2000), Learning from Examples: Instructional Principles from the Worked Examples Research, Review of Educational Research 70(2):181-214: https://assess.ucr.edu/media/741/download (resumen y comienzo)"
  - "Pashler et al. (2007), guía del What Works Clearinghouse, recomendación 2: https://ies.ed.gov/ncee/wwc/PracticeGuide/1 (resumen de recomendaciones)"
  - "Margulieux, Morrison y Decker (2020), Reducing withdrawal and failure rates in introductory programming with subgoal labeled worked examples, International Journal of STEM Education 7, art. 19: https://link.springer.com/article/10.1186/s40594-020-00222-7 (según abstract)"
  - "Selvaraj, Zhang, Porter y Soosai Raj (2021), Live Coding: A Review of the Literature, ITiCSE: https://par.nsf.gov/biblio/10313400-live-coding-review-literature (según abstract)"
  - "Kalyuga (2007), Expertise Reversal Effect and Its Implications for Learner-Tailored Instruction, Educational Psychology Review 19:509-539: https://www.uky.edu/~gmswan3/EDC608/Kalyuga2007_Article_ExpertiseReversalEffectAndItsI.pdf (lectura parcial)"
  - "Didactica/.investigacion/explicita-practica-preguntas-feedback.md"
aliases: [modelado, modeling, pensar en voz alta, think-aloud, ejemplo resuelto, worked example, worked examples, subobjetivos, subgoal labels, live coding, programar en vivo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Modelado y ejemplos resueltos

Modelar es mostrar cómo se resuelve algo haciendo visible el razonamiento que un experto lleva oculto, pensando en voz alta o con ejemplos resueltos paso a paso. El ejemplo resuelto es de las técnicas con mejor respaldo experimental, y sirve sobre todo a quien recién empieza.

Es el cuarto de los [principios de Rosenshine](principios-de-rosenshine.md) y el primer paso de la secuencia que sigue con el [andamiaje](../Practica-guiada-y-andamiaje/andamiaje.md): primero se muestra, después se hace con ayuda, al final se hace solo. El [aprendizaje cognitivo](../Practica-guiada-y-andamiaje/aprendizaje-cognitivo.md) pone el modelado como el primero de sus seis métodos.

## Pensar en voz alta: mostrar lo que no se ve

Para Rosenshine, el modelado muestra «expert thinking that is usually hidden from the student». El docente verbaliza lo que hace al resolver: por ejemplo, cómo identifica el tema de un párrafo y de ahí arma la frase que lo resume. El mismo artículo sugiere el camino inverso, pedirle al alumno que piense en voz alta para ver su razonamiento, que es lo que desarrolla [autoexplicación](../Preguntas-y-dialogo/autoexplicacion.md).

La evidencia que reúne Rosenshine sobre modelado viene de comprensión lectora, escritura y matemática. No hay en su artículo un estudio de programación.

## Cómo se arma un buen ejemplo resuelto

Atkinson, Derry, Renkl y Wortham (2000) definen el ejemplo resuelto como «instructional devices that provide an expert's problem solution for a learner to study». De su revisión salen principios de diseño:

1. Integrar las partes: combinar modalidades y marcar la estructura conceptual con etiquetas o separando el ejemplo en segmentos.
2. Varios ejemplos por tipo de problema, con formatos variados dentro del tipo y rasgos superficiales que señalen la estructura profunda.
3. Ponerlos cerca de problemas de práctica equivalentes, no todos los ejemplos primero y todos los problemas después.
4. Hacer que el alumno se explique el ejemplo, entrenándolo o con la estructura misma del ejemplo.

Los autores aclaran que los ejemplos resueltos corresponden a las «early stages of skill development». La guía del [What Works Clearinghouse](../Fundamentos/evidencia-en-educacion.md#los-resúmenes-de-evidencia-y-cómo-leer-cada-uno) (Pashler et al. 2007) lo resume en su recomendación 2, «Interleave worked example solutions with problem-solving exercises», con evidencia moderada.

Rosenshine cuenta un problema práctico: en una investigación en Australia que alternaba ejemplos y problemas, no todos estudiaban el ejemplo. Agregaron problemas parcialmente completados para obligar a prestarle atención. Ese paso, de ejemplo completo a problema a medio resolver, es el comienzo del retiro de la guía que trata [andamiaje](../Practica-guiada-y-andamiaje/andamiaje.md).

## Subobjetivos: ponerle nombre a cada tramo

Un ejemplo con subobjetivos etiqueta los tramos de la solución con lo que cada uno logra (ilustrativo, no tomado de los estudios: «leer la entrada», «acumular el total»), para que quien aprende vea la estructura que se repite entre problemas. Margulieux, Morrison y Decker (2020) lo probaron en un curso introductorio de programación de un semestre, con 265 estudiantes: mitad con instrucción con subobjetivos y mitad con la habitual. Según el abstract, los del grupo con subobjetivos sacaron mejores notas en los cuestionarios de la semana y no se diferenciaron en los exámenes finales; tuvieron menos varianza y menos abandono y desaprobación, con un efecto mayor en los estudiantes en riesgo. El informe no tuvo acceso al texto, así que no hay tamaños de efecto. El caso de programación sigue en [enseñar programación](../Didacticas-especificas/ensenar-programacion.md).

## Cuándo el ejemplo deja de ayudar

El ejemplo resuelto ayuda a quien sabe poco y deja de ayudar, o estorba, a quien ya sabe: es la [inversión de la experticia](../Practica-guiada-y-andamiaje/inversion-de-la-experticia.md). Kalyuga (2007) cita a Tuovinen y Sweller (1999), donde los novatos que aprendían una base de datos se beneficiaron más con ejemplos que con exploración, sin diferencias entre los que ya sabían. Con un grupo mixto, quien enseña tiene que averiguar primero cuánto sabe cada uno.

## Live coding: modelado con poca evidencia propia

En programación, modelar suele tomar la forma de *live coding*, programar en vivo frente al grupo. Selvaraj et al. (2021) revisaron la literatura y, según su abstract, concluyen que «there is a lack of empirical evidence to support claims about the effectiveness of live coding on student learning», aunque se lo presente como «one of the best practices for teaching programming». El abstract no dice cuántos trabajos revisaron.

Leído junto con Rosenshine, el *live coding* se sostiene como una forma de pensar en voz alta, con sus errores incluidos, más que como técnica con evidencia propia. Esa lectura es inferencia de esta base.

> [!NOTE] Sin fuente todavía: si programar en vivo rinde distinto que mostrar código ya escrito, y qué dice *Teaching Tech Together* en su capítulo sobre el tema.
