---
resumen: >-
  El aprendizaje activo es cualquier clase en la que quien aprende hace algo con el contenido (resolver, discutir, responder) en lugar de solo escuchar una exposición. En ciencias, ingeniería y matemática universitarias baja la reprobación de 33,8 % a 21,8 % y sube los exámenes en 0,47 desviaciones estándar.
estado: vigente
estabilidad: estable
fuentes:
  - "Freeman et al. (2014), Active learning increases student performance in science, engineering, and mathematics, PNAS 111(23): https://www.bu.edu/eng/files/2025/01/Active-learning-increases-student-performance-in-science-engineering-and-mathematics.pdf (texto leído)"
  - "Chi y Wylie (2014), The ICAP Framework: Linking Cognitive Engagement to Active Learning Outcomes, Educational Psychologist 49(4):219-243, DOI 10.1080/00461520.2014.965823: https://chilab.asu.edu/sites/default/files/lcl/chiwylie2014icap_2.pdf (texto completo, copia del laboratorio de la autora)"
  - "Porter, Bailey Lee y Simon (2013), Halving fail rates using peer instruction: a study of four computer science courses, SIGCSE '13:177-182, DOI 10.1145/2445196.2445250: https://files.software-carpentry.org/training-course/2012/08/porter-halving-fail-peer-instruction-2013.pdf (texto completo, preimpresión)"
  - "EEF Teaching and Learning Toolkit, Collaborative learning approaches, vía Evidence for Learning: https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/collaborative-learning-approaches/"
  - "Didactica/.investigacion/indagacion-tutoria-especificas.md"
  - "Didactica/.investigacion/fuentes-activo-y-preguntas-2026-11.md"
aliases: [active learning, clase activa, aprendizaje colaborativo, collaborative learning, peer instruction, instrucción entre pares, ICAP]
creado: 2026-11-27
revisado: 2026-11-27
---

# Aprendizaje activo

El aprendizaje activo es cualquier clase en la que quien aprende hace algo con el contenido (resolver, discutir, responder) en lugar de solo escuchar una exposición. En ciencias, ingeniería y matemática universitarias baja la reprobación de 33,8 % a 21,8 % y sube los exámenes en 0,47 desviaciones estándar.

No es lo mismo que descubrir. Una clase activa puede ser muy guiada: una explicación corta, un problema para resolver en parejas, una votación y la corrección. Por eso queda fuera de la disputa de [guía o descubrimiento](guia-o-descubrimiento.md) y es compatible con la secuencia de [explicar y modelar](../Explicar-y-modelar/explicar-y-modelar.md): lo que discute es cuánto tiempo pasa quien aprende escuchando sin hacer nada.

## Lo que midió Freeman

Freeman et al. (2014) reunieron 225 estudios que comparaban clases con algo de aprendizaje activo contra exposición magistral continua en ciencias, ingeniería y matemática universitarias.

| Medida | Resultado |
|---|---|
| Exámenes e inventarios conceptuales (158 estudios) | +0,47 desviaciones estándar |
| Reprobación | 21,8 % con aprendizaje activo, 33,8 % con clase magistral |
| Probabilidad de reprobar con clase magistral | [odds ratio](../Fundamentos/glosario-de-didactica.md#leer-la-evidencia) 1,95 |
| Solo estudios con asignación aleatoria (16) | 0,514, similar al resto |

Los autores calcularon cuántos estudios nulos sin publicar harían falta para anular el resultado (114 para exámenes, 438 para reprobación) y lo consideraron improbable. El "55 % más de reprobados" que circula es la diferencia relativa entre 21,8 % y 33,8 %, no el odds ratio. El beneficio fue mayor en clases chicas y en inventarios conceptuales. El propio artículo advierte que "aprendizaje activo" cubre intervenciones muy distintas, así que el promedio no dice cuál conviene.

## Qué cuenta como activo

Chi y Wylie (2014) propusieron el marco ICAP para ordenar esa variedad. Clasifica lo que quien aprende hace a la vista en cuatro modos:

| Modo | Qué hace quien aprende | Ejemplos de Chi y Wylie |
|---|---|---|
| Pasivo | Recibe | Escuchar una clase sin hacer otra cosa; leer en silencio |
| Activo | Manipula el material | Subrayar, copiar los pasos de una solución, tomar notas literales |
| Constructivo | Genera algo que no estaba en el material | Autoexplicarse, hacer un mapa conceptual, comparar y contrastar |
| Interactivo | Dialoga | Defender una posición en pareja o en grupo; preguntar y responder |

La hipótesis ICAP predice que se aprende más en el orden inverso de la tabla: interactivo, constructivo, activo, pasivo. Para que un diálogo cuente como interactivo, las dos partes tienen que aportar ideas propias y turnarse. Mover las manos no alcanza: lo que sube de nivel es producir algo nuevo con el contenido, como en la [autoexplicación](../Preguntas-y-dialogo/autoexplicacion.md).

La evidencia que presentan es sobre todo una relectura de estudios sobre tres actividades: tomar notas, hacer mapas conceptuales y autoexplicar. Muchos son de otros autores, como Coleman, Brown y Rivkin (1997), que ellos reinterpretan con el marco. El estudio con los cuatro modos que citan es de su laboratorio (Menekse et al. 2013, ciencia de materiales), donde el aprendizaje sube «around 8% to 10%» de un modo al siguiente. Los estudios de aula que citan no se diseñaron con ICAP: los autores los reclasifican.

Los propios autores hacen tres advertencias. Con preguntas superficiales, de puro recuerdo, el rendimiento es poco sensible a cómo se estudió, y eso vale también para los modos ICAP. Alguien puede procesar a fondo mientras parece pasivo, porque el marco mira la conducta visible. Y una discusión con toda la clase es constructiva solo para los pocos que hablan: para el resto, que escucha, es pasiva.

> [!NOTE] Sin fuente todavía: estudios independientes, diseñados para probar la jerarquía ICAP fuera del laboratorio de Chi.

## Pares y grupos

La [instrucción entre pares](../../Ciencias-del-aprendizaje/Aprender-con-otros/instruccion-entre-pares.md) (*peer instruction*) alterna preguntas conceptuales, votación individual, discusión con un compañero y nueva votación. En enseñanza de programación, Porter, Bailey Lee y Simon (2013) compararon la instrucción entre pares con la clase expositiva en cuatro materias de computación universitaria, a lo largo de diez años: la reprobación (abandonar o terminar con D o F) bajó en promedio un 61 % por curso, de 20 % a 7 %, y un 67 % (de 23 % a 8 %) con el mismo docente dando la misma materia. Es un estudio en el aula, no un ensayo aleatorizado; el detalle está en la nota de instrucción entre pares. El caso de programación está en [enseñar programación](../Didacticas-especificas/ensenar-programacion.md).

El Toolkit de la [EEF](../Fundamentos/evidencia-en-educacion.md#los-resúmenes-de-evidencia-y-cómo-leer-cada-uno) (Education Endowment Foundation, Inglaterra), leído por su espejo australiano, da al aprendizaje colaborativo +5 [meses de progreso](../Fundamentos/evidencia-en-educacion.md#los-resúmenes-de-evidencia-y-cómo-leer-cada-uno) con costo muy bajo, sobre 212 estudios, en grupos de tres a cinco con una meta compartida. La condición que pone es que los de menor rendimiento participen activamente. La solidez de la evidencia discrepa entre versiones: el espejo la califica de baja y el Toolkit de 2018 hablaba de "extensive evidence". Cómo leer esos meses y candados está en [evidencia en educación](../Fundamentos/evidencia-en-educacion.md); lo social del aprendizaje, en [aprender con otros](../../Ciencias-del-aprendizaje/Aprender-con-otros/aprender-con-otros.md), de Ciencias del aprendizaje.

## Hasta dónde llega la evidencia

Freeman es evidencia de grado universitario en ciencias; el Toolkit, de escuelas. Ninguna fuente leída trata a adultos en cursos de oficio o de tecnología, así que trasladar las cifras a ese público es una inferencia. Lo que sí se traslada sin forzar es la dirección: una exposición continua de una hora rinde menos que la misma hora cortada por problemas y preguntas.
