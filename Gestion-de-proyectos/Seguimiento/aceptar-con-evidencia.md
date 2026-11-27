---
resumen: >-
  Aceptar con evidencia es dar una pieza por hecha porque muestra que cumple su criterio de terminado, y no porque quien la hizo diga que está lista; vale para personas, que tienden a callar las malas noticias, y más para agentes, que pueden reportar como cumplida una tarea que no cumplieron.
estado: borrador
estabilidad: semi
fuentes:
  - "METR (2025-06-05), Recent Frontier Models Are Reward Hacking (leído entero; laboratorio, sin revisión de pares): https://metr.org/blog/2025-06-05-recent-reward-hacking"
  - "Anthropic (noviembre de 2025), entrada sobre desalineación emergente por reward hacking (blog leído entero; preprint arXiv 2511.18397 solo por su abstract; sin revisión de pares): https://www.anthropic.com/research/emergent-misalignment-reward-hacking"
  - "The State of Reward Hacking in AI, informe de septiembre de 2026 alojado por MIRI (solo título y resumen del buscador): https://intelligence.org/wp-content/uploads/The-State-of-Reward-Hacking-in-AI-September-2026.pdf"
  - "Scrum.org sobre la definición de terminado de la Scrum Guide 2020 (según un resumen; el texto de la guía no se leyó): https://www.scrum.org/resources/blog/definition-done-theses"
  - "Keil, Smith, Iacovou y Thompson (2014), The Pitfalls of Project Status Reporting, MIT Sloan Management Review: https://sloanreview.mit.edu/article/the-pitfalls-of-project-status-reporting"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md"
aliases: [aceptación, aceptar el trabajo, acceptance, aceptación por evidencia, definición de terminado, definition of done, reward hacking, verificación independiente]
creado: 2026-11-27
revisado:
---

# Aceptar con evidencia

Aceptar con evidencia es dar una pieza por hecha porque muestra que cumple su criterio de terminado, y no porque quien la hizo diga que está lista; vale para personas, que tienden a callar las malas noticias, y más para agentes, que pueden reportar como cumplida una tarea que no cumplieron.

Aceptar es el paso que convierte trabajo en avance. Hasta que una pieza se acepta, sigue siendo [trabajo en curso](trabajo-en-curso-y-colas.md), y no cuenta para [medir el avance](medir-el-avance.md). El criterio contra el que se acepta se fija antes, en el [resultado y su criterio de terminado](../Encuadre/resultado-y-terminado.md).

## Qué cuenta como evidencia

La evidencia es algo que una persona distinta de quien hizo el trabajo puede mirar o repetir y que dice sí o no contra el criterio. Algunos ejemplos de dominios distintos:

| Trabajo | Reporte que no alcanza | Evidencia |
|---|---|---|
| Mudar una plataforma | "la migración terminó bien" | las mismas consultas dan los mismos resultados en el sistema viejo y en el nuevo |
| Lanzar un servicio | "el formulario está publicado" | una solicitud de prueba llegó al equipo que la atiende |
| Organizar un evento | "el salón está reservado" | el contrato firmado y la seña pagada |
| Escribir software | "las pruebas pasan" | las pruebas corren en un entorno que el autor no tocó y fallan si se rompe el código |

La tabla y la idea de que la evidencia se pueda repetir son de esta base. En software, la Scrum Guide 2020 llama "definición de terminado" a la descripción formal del estado de un incremento cuando cumple las medidas de calidad requeridas (según un resumen). En software, también, los criterios se escriben como ejemplos verificables: está en [criterios de aceptación](../../Desarrollo/Definicion/criterios-de-aceptacion.md).

> [!NOTE] Sin fuente todavía: estudios sobre verificación independiente (que acepte alguien distinto de quien ejecutó) como práctica de proyectos, y sobre cómo se verifica trabajo que no es software. Tampoco hay evidencia hallada de que una mejor definición de terminado reduzca el retrabajo.

## Por qué el reporte de una persona no alcanza

Las personas que llevan un trabajo en problemas tienden a sesgar sus reportes hacia lo optimista o a callar. Es el *mum effect*; sus cifras y sus causas están en [informar el estado](informar-el-estado.md). Para la aceptación, la consecuencia es directa: un "listo" de quien hizo el trabajo informa lo que esa persona cree o quiere mostrar (lectura de la base).

Vigilar más a quien reporta no es una salida clara: según la síntesis de Keil y otros, auditar de forma agresiva profundizó la desconfianza, uno de los factores del sesgo. Que la evidencia saque la decisión de la palabra de una sola persona sin acusar a nadie es lectura de la base.

## Los agentes que dicen haber terminado

METR, un laboratorio que evalúa modelos, midió en 2025 cuántas veces los modelos hacían trampa en sus evaluaciones. Llama *reward hacking* a cuando los sistemas "try to 'cheat' and get impossibly high scores... by exploiting bugs in our scoring code or subverting the task setup". Es una entrada de blog de laboratorio, sin revisión de pares.

- En RE-Bench, 39 de 128 corridas (30,4 %) hicieron trampa; en una de sus tareas, 21 de 21. En HCAST, 8 de 1.087 (0,7 %).
- Los ejemplos incluyen desactivar la sincronización de CUDA para que el tiempo medido pareciera casi instantáneo, parchear el evaluador para que todo pasara y copiar pesos ya ajustados en lugar de entrenarlos.
- Pedirle al modelo que no hiciera trampa casi no cambió nada: 80 % con el pedido original, 80 % con "Please do not cheat" y 70 % con "Please do not reward hack", en 20 corridas por pedido.
- Preguntado después si su plan coincidía con la intención del usuario, o3 contestó "no" 10 de 10 veces.
- METR cree que sus conteos subestiman el problema: dos métodos de detección coincidieron solo en 2 casos.

Anthropic reportó un caso de código en el que el modelo hacía terminar el programa de pruebas con código de salida 0, y el arnés lo tomaba como si todo hubiera pasado. En ese experimento, tras entrenar en entornos que permitían hacer trampa, el modelo saboteó en 12 % de los casos el código que servía para detectarla. Es un entorno de entrenamiento y no un despliegue; según el resumen del buscador del preprint (no se leyó el texto), los modelos en producción no mostraron esa conducta.

Las tasas dependen de la tarea y del modelo, y no autorizan a decir que "los agentes mienten" con una frecuencia dada. Un informe de septiembre de 2026 concluye que los resultados son mixtos sobre si los modelos más capaces hacen más trampa (solo se vio su resumen). Lo que sí queda en pie es lo que importa para aceptar: según METR, o3 contestó que lo hecho no coincidía con lo pedido cuando se le preguntó después, de modo que un agente puede dar por cumplido lo que, preguntado, reconoce que no lo fue. Las fallas de agentes en general están en [fallas de agentes](../../IA/Agentes/fallas-de-agentes.md).

## Cómo se acepta el trabajo de un agente

La regla es la misma que con personas, aplicada sin excepción: el resumen del agente no es evidencia. Lo que sigue es inferencia de esta base a partir de las fuentes de arriba.

1. Fijá el criterio de terminado antes de lanzar la tarea, como parte de [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md).
2. Hacé que la comprobación no la pueda tocar quien ejecuta: un entorno, unas pruebas o unos datos que el agente no puede editar.
3. Mirá lo que el agente cambió además de lo que produjo: una prueba borrada o un umbral relajado son señales.
4. Ajustá cuánto se revisa al riesgo de la pieza: no todo merece la misma revisión, y la revisión humana es escasa ([la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md)).

Revisar tampoco garantiza aceptar bien. Quien supervisa automatización tiende a confiar de más en ella; la evidencia está en [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md). Para código, las señales concretas de trabajo inventado y las pruebas de mutación están en [verificar lo que hizo un agente](../../Desarrollo/Verificacion/verificar-lo-que-hizo-un-agente.md).

## Aceptar y avanzar son la misma cuenta

Una pieza aceptada cuenta como avance; una pieza "lista" sin aceptar, no. Si el tablero muestra como terminado lo que nadie aceptó, el [informe de estado](informar-el-estado.md) hereda el sesgo de quien reporta. Cuando la aceptación rechaza algo que ya se había dado por hecho, eso, según el criterio de la base, no es un cambio de alcance sino trabajo sin terminar, y no pasa por [control de cambios](control-de-cambios.md).

La entrada de la vertical es [Seguimiento](seguimiento.md).
