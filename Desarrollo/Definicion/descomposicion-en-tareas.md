---
resumen: >-
  Descomponer es partir un trabajo en tareas que entregan cada una un cambio de comportamiento
  observable y se verifican por separado; con agentes de código, una tarea es lo que un agente puede
  hacer y comprobar con un chequeo de pasa o falla dentro de una sesión.
estado: vigente
estabilidad: semi
fuentes:
  - https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://code.claude.com/docs/en/best-practices
  - https://learn.chatgpt.com/guides/best-practices
  - https://metr.org/blog/2026-1-29-time-horizon-1-1
  - https://arxiv.org/abs/2503.14499
  - https://kiro.dev/docs/specs/
  - "Bain, Designing Agile Missions (según resumen): https://www.bain.com/insights/designing-agile-missions/"
  - "User stories and vertical slicing, dev.to (según resumen): https://dev.to/jan/user-stories-and-vertical-slicing-1dpo"
aliases: [descomponer, partir historias, splitting user stories, rebanada vertical, vertical slice, slicing, tarea, desglose de tareas, tamaño de tarea]
creado: 2026-11-27
revisado: 2026-11-27
---

# Descomposición en tareas

Descomponer es partir un trabajo en tareas que entregan cada una un cambio de comportamiento observable y se verifican por separado; con agentes de código, una tarea es lo que un agente puede hacer y comprobar con un chequeo de pasa o falla dentro de una sesión.

Es el último paso de [Definición](definicion.md) antes de [Construcción](../Construccion/construccion.md). Parte una [especificación](especificacion.md) o una [historia de usuario](historia-de-usuario.md) en pedazos, y a cada pedazo le asigna sus [criterios de aceptación](criterios-de-aceptacion.md). La historia es la unidad de valor para el cliente; la tarea es la unidad de trabajo para quien construye. A veces coinciden y a veces una historia se hace en varias tareas.

## Rebanadas verticales y no capas

Richard Lawrence (Humanizing Work) define una buena porción como "a work item that delivers a valuable change in system behavior". Una porción horizontal cubre una sola capa (la tabla, el endpoint, la pantalla) y no cambia nada que se pueda ver hasta que llegan las otras. La vertical atraviesa todas las capas con poco ancho: la consigna es "find thin vertical slices inside those wide ones".

El desglose clásico por capa (una tarea de base de datos, otra de API, otra de interfaz) va contra esa idea. Según materiales secundarios que coinciden entre sí, las rebanadas horizontales no entregan valor solas. Hay voces en contra: un equipo que corta en horizontal a propósito y entrega un grupo de historias como una función, y la idea de *dicing*, rebanadas que no valen hasta que se juntan. Todo esto viene de blogs y se toma como práctica aceptada, no como resultado medido. En un encargo, cada incremento del [plan de entregas](../Encargo/plan-de-entregas.md) se arma con una o más de estas rebanadas.

Lectura de esta base: con agentes el corte vertical pesa más, porque una tarea horizontal no tiene un comportamiento que se pueda comprobar y por eso no tiene un criterio de pasa o falla propio.

## Los patrones para partir

Lawrence da nueve patrones y un metapatrón: encontrar la complejidad central, identificar sus variaciones y reducirlas a una sola rebanada completa.

| Patrón | Se parte por | Ejemplo |
|---|---|---|
| Pasos del flujo | etapas de un recorrido que ya entregan algo | comprar un solo producto antes que el carrito completo |
| Operaciones | cada operación de un "gestionar" | crear, después editar, después borrar |
| Variaciones de reglas de negocio | una regla por vez | descuento fijo antes que descuento por volumen |
| Variaciones de datos | un tipo de dato por vez | un solo país, después los demás |
| Métodos de ingreso de datos | la forma simple primero | un campo de texto antes que un selector con búsqueda |
| Esfuerzo mayor | el primer caso, que trae la infraestructura | el primer medio de pago, después el resto |
| Simple y complejo | el caso simple primero | búsqueda exacta antes que búsqueda difusa |
| Postergar rendimiento | que ande primero, que ande rápido después | búsqueda sin índice, después con índice |
| Spike | una investigación corta cuando no se sabe por dónde | probar si el proveedor de pagos admite cuotas |

Los ejemplos de la tabla son de esta base. Lawrence hace tres advertencias. Partir "one step at a time from beginning to end" es lo más obvio y está mal. Abrir un spike "should be your last resort". Postergar el rendimiento acumula deuda si la historia se da por terminada antes de tiempo, y eso conecta con [deuda técnica](../Evolucion/deuda-tecnica.md).

La palabra "gestionar" en una historia delata varias operaciones. Según Wynne, muchas tarjetas azules en un [Example Mapping](criterios-de-aceptacion.md) indican que la historia es grande; esta base propone que cada regla puede ser una rebanada, como en el patrón de variaciones de reglas de negocio.

## Una funcionalidad por sesión

En el arnés para trabajos largos de Anthropic, cada sesión del agente apunta a una sola funcionalidad, y lo llaman crítico por la tendencia del agente a "try to do too much at once". Cuando intentó hacer la aplicación entera de una vez, se quedó sin contexto a mitad de una funcionalidad y la sesión siguiente tuvo que adivinar dónde estaba. Cada sesión termina con un commit y un archivo de progreso, dejando el código "in a clean state at the end of a session". OpenAI da un consejo parecido: "Keep one chat per coherent unit of work", y empezar con "one representative task, get it working well" antes de ampliar.

Que cada tarea deje el repositorio en un estado limpio y verificable es lo que permite revisarla sola, en [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md), y lo que permite correr tareas en paralelo. Algunas herramientas agrupan las tareas independientes en oleadas que corren a la vez; las que dependen de otra esperan.

## Antes de soltar una tarea a un agente

La guía de Anthropic propone cinco preguntas antes de dejar una tarea corriendo sola. En voseo, como lista de chequeo:

1. ¿Sabe qué es estar terminado? Una condición, un archivo de especificación o una prueba que falla y tiene que pasar.
2. ¿Puede comprobar su propio trabajo?
3. ¿Qué puede tocar y qué no?
4. ¿Qué lo detiene?
5. ¿Adónde va el resultado y quién lo aprueba?

La misma guía dice qué le queda a la persona: "starting it, deciding what 'done' means this time, and approving the merge at the end."

## Cuánto puede durar una tarea para un agente

METR mide el horizonte temporal de los modelos: la duración de las tareas, medida en lo que tardaría una persona, que un modelo completa con un 50 % de éxito. Ese horizonte se viene duplicando en meses y no en años (unos 89 días desde 2024, según su medición de enero de 2026), así que cualquier número envejece rápido. El conjunto de tareas es de investigación e ingeniería de software, y los intervalos de confianza son anchos. Según el resumen de una fuente secundaria, el horizonte con 80 % de éxito es unas cinco veces más corto que el de 50 %, y es el que importa si se quiere que el agente acierte casi siempre.

> [!IMPORTANT]
> Ni METR ni las guías de los fabricantes dan una regla de tamaño de tarea: METR mide horizontes por modelo, no recomendaciones, y la búsqueda no encontró una guía oficial con un criterio numérico. Cualquier regla es criterio de esta base. La de esta base: una tarea es una rebanada vertical que se comprueba con un chequeo de pasa o falla y entra en una sesión del agente sin agotar su contexto. Si no se puede escribir su criterio, todavía no es una tarea.

Descomponer más y delegar más no siempre ahorra tiempo: en el ensayo de METR de 2025, quienes usaron IA tardaron 19 % más, aunque ese resultado ya no es una cifra vigente. La evidencia sobre cuánto acelera un agente es mixta y está en [agente de código](../Construccion/agente-de-codigo.md).

## Horizontes medidos por METR en enero de 2026

Copiado de METR, "Time Horizon 1.1" (29 de enero de 2026), el 2026-11-27. Horizonte al 50 % de éxito, con intervalo de confianza del 95 %: Claude Opus 4.5, 320 minutos (170 a 729); GPT-5, 214 minutos (117 a 480); Claude Sonnet 3.7, 60 minutos (32 a 106). Tiempo de duplicación: unos 196 días desde 2019, 131 desde 2023 y 89 desde 2024. Solo 31 tareas le llevan a una persona 8 horas o más, y solo 5 de ellas tienen medición humana.
