---
resumen: >-
  El feedback de usuario es la señal que deja el uso real sobre si una salida sirvió, sea pedida
  (un pulgar, una calificación) o inferida de lo que la persona hace (corregir, regenerar,
  abandonar); vuelve al sistema como traza y como etiqueta para la evaluación.
estado: vigente
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://alexstrick.com/posts/2025-02-09-ai-eg-chapter-10.html
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://hamel.dev/blog/posts/field-guide/
  - https://www.thoughtworks.com/en-us/radar/techniques/summary/
aliases: [user feedback, retroalimentación de usuario, feedback explícito, feedback implícito]
creado: 2026-11-27
revisado: 2026-11-27
---

# Feedback de usuario

El feedback de usuario es la señal que deja el uso real sobre si una salida sirvió, sea pedida (un
pulgar, una calificación) o inferida de lo que la persona hace (corregir, regenerar, abandonar);
vuelve al sistema como traza y como etiqueta para la evaluación.

Cierra el [bucle de la evaluación](evaluacion.md): entra por la
[observabilidad](../Produccion/observabilidad-de-modelos.md) como un evento más de la traza y llega a los
[evals](evals.md) como juicio de alguien que usó el producto. Huyen le dedica la última
parte del capítulo 10, con tres secciones según el índice: "Extracting Conversational Feedback",
"Feedback Design" y "Feedback Limitations". Su post de arquitectura lo deja afuera a propósito: "I
won't go into specifics or cover user feedback, drift detection, and debugging."

## Explícito o implícito

> [!NOTE]
> Lo que sigue sale de notas de lectura de un tercero sobre el capítulo 10 (Alex Strick), no del
> texto de Huyen, que no se leyó.

Según esas notas, el feedback se divide en dos clases:

| Clase | Ejemplos | Qué cuesta (inferencia de esta base) |
|---|---|---|
| Explícito | Pulgar arriba o abajo, calificaciones, comentarios | Interrumpe al usuario; pocos lo dan |
| Implícito | Terminar la conversación temprano, corregir la respuesta, pedir que la regenere, el tono del mensaje siguiente | Hay que inferirlo y puede leerse mal |

En una interfaz conversacional, gran parte de la señal ya está en la conversación: si la persona
repite la pregunta con otras palabras, la respuesta anterior no le sirvió. Según las mismas notas,
los límites del feedback son el sesgo hacia las experiencias negativas, la autoselección de quien
responde, el sesgo de posición (se califica más lo que está a la vista) y los bucles de
retroalimentación, en los que el sistema aprende de datos que él mismo moldeó.

## Medir lo que le importa al usuario

El feedback corrige un error que la evaluación sola no ve: medir la calidad equivocada. Huyen cuenta
el caso de una amiga cuyo equipo cuidaba el largo de los resúmenes de reuniones y descubrió que "their
users didn't care about the actual summary": querían las tareas que les tocaban. En otro pasaje, sobre
dos equipos que habían descartado la IA, concluye que "the issue wasn't with AI, but with product". Un criterio de evaluación
que ningún usuario valora mejora un número y no el producto.

## Del feedback al bucle de mejora

Husain describe cómo el juicio humano vuelve al sistema: un visor de trazas con botones de correcto
e incorrecto, y las críticas escritas que se usan como ejemplos para el [juez](ia-como-juez.md) y
como base de datos sintéticos. Ese juicio es de quienes construyen el producto, no de los usuarios
finales, pero el mecanismo es el mismo: una etiqueta humana entra al conjunto de evaluación.

El término *data flywheel* se usa para este ciclo (el uso genera datos, los datos mejoran el modelo,
el modelo atrae más uso), pero esa descripción es la corriente y ninguna fuente leída lo define. Husain describe el ciclo sin usar el
término. El Thoughtworks Technology Radar puso "feedback flywheel" en Trial en noviembre de 2026; la
entrada no se leyó, solo su nombre y su anillo.

> [!NOTE]
> Sin fuente todavía: una definición citable de *data flywheel*; el texto de Huyen sobre diseño y
> límites del feedback; y cifras de tasas de respuesta o de sesgos medidos en feedback explícito.

## Qué leer sobre feedback

Huyen, *AI Engineering*, capítulo 10, sección "User Feedback", sobre todo "Feedback Design" y
"Feedback Limitations": fijarse en no interrumpir al usuario, en la señal implícita de la
conversación y en los sesgos de quien responde. Para el bucle, Husain,
["A Field Guide to Rapidly Improving AI Products"](https://hamel.dev/blog/posts/field-guide/).
