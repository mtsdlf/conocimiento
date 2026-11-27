---
resumen: >-
  La planificación de un agente es cómo descompone una tarea en pasos, elige el orden y se corrige
  cuando un paso sale mal; Huyen recomienda validar el plan antes de ejecutarlo, y Kambhampati et
  al. sostienen, en una tesis disputada, que un modelo de lenguaje no planifica de forma confiable
  sin un verificador externo.
estado: borrador
estabilidad: estable
fuentes:
  - https://huyenchip.com/2025/01/07/agents.html
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 6 «Agents», sección «Planning», p. 281 (según el índice)"
  - https://arxiv.org/abs/2402.01817
  - https://arxiv.org/abs/2303.11366
  - https://arxiv.org/abs/2210.03629
  - https://arxiv.org/abs/2503.14499
  - https://metr.org/time-horizons/
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
aliases: [planning, planificación de agentes, agent planning, reflexión, reflection, Reflexion, LLM-Modulo, horizonte de tiempo, time horizon]
creado: 2026-11-27
revisado:
---

# Planificación

La planificación de un agente es cómo descompone una tarea en pasos, elige el orden y se corrige
cuando un paso sale mal; Huyen recomienda validar el plan antes de ejecutarlo, y Kambhampati et
al. sostienen, en una tesis disputada, que un modelo de lenguaje no planifica de forma confiable
sin un verificador externo.

Es lo que distingue a un [agente](agente.md) de un [workflow](patrones-de-flujo.md): en el
workflow el plan lo escribió una persona en el código; en el agente lo genera el modelo en cada
tarea.

## Planificar es buscar

"Planning, at its core, is a search problem", escribe Huyen: entre todos los caminos posibles
hacia el objetivo, encontrar uno que llegue. Un plan, según su post, puede ser una secuencia, tener
ramas condicionales, pasos en paralelo, bucles o niveles (un plan de alto nivel cuyos pasos se
vuelven planes más chicos). Y tiene granularidad: un plan detallado es difícil de generar y fácil
de ejecutar; uno de alto nivel, al revés.

Un modelo genera texto de izquierda a derecha y no vuelve sobre lo que ya emitió. Huyen discute si
eso le impide planificar: un modelo "can revise the path using action B instead, effectively
backtracking". Es decir, no retrocede borrando, pero puede corregir el rumbo en el paso siguiente.
Los [modelos de razonamiento](../Modelos/razonamiento.md), que gastan tokens pensando antes de
responder, llevan parte de esa búsqueda adentro de la inferencia (lectura de esta base).

## Separar el plan de la ejecución

"To avoid fruitless execution, planning should be decoupled from execution", recomienda Huyen. El
agente queda partido en tres pasos:

1. **Generar el plan**: el modelo propone la secuencia de pasos y herramientas.
2. **Validarlo**: "The plan can be validated using heuristics" (que solo use herramientas que
   existen, que no pase de cierto número de pasos) o con un modelo como
   [juez](../Evaluacion/ia-como-juez.md); una persona puede aprobarlo si la tarea lo pide.
3. **Ejecutarlo**: recién entonces se llaman las [herramientas](uso-de-herramientas.md).

Validar antes de ejecutar es barato: un plan rechazado cuesta unos tokens, mientras que un plan
malo ejecutado puede costar acciones de escritura que no se deshacen (lectura de esta base). Los
[guardrails](../Produccion/guardrails.md) son otro lugar donde poner esa validación, y si el plan
pasa por varios sistemas, cada acción que se puede repetir necesita su
[clave de idempotencia](../../Arquitectura/Sistemas-distribuidos/clave-de-idempotencia.md)
(lectura de esta base).

## Por qué los planes largos fallan: el error se acumula

Cada paso de un agente puede fallar, y un error temprano contamina todo lo que sigue. Huyen lo
cuantifica: "If the model's accuracy is 95% per step, over 10 steps, the accuracy will drop to
60%". La cuenta es 0,95 elevado a 10, que da 0,60, y supone que los pasos fallan de forma
independiente. Con 20 pasos, la misma cuenta da 0,36 (cálculo de esta base).

La consecuencia de diseño: acortar los planes, partir las tareas largas en tramos que se verifican
por separado y poner un control después de cada paso que cambia algo. Es la razón por la que
[evaluar un agente](fallas-de-agentes.md) mira la trayectoria y no solo el resultado final.

## ¿Puede planificar un modelo de lenguaje?

> [!IMPORTANT]
> **No por sí solo (Kambhampati et al., ICML 2024).** "We argue that auto-regressive LLMs cannot,
> by themselves, do planning or self-verification." Proponen los marcos LLM-Modulo, que "combine
> the strengths of LLMs with external model-based verifiers": el modelo genera candidatos y un
> verificador externo, basado en un modelo del dominio, los critica en un ciclo. Critican por
> igual a quienes dicen que los modelos ya planifican ("over-optimistic claims") y a quienes los
> subestiman ("perhaps over-pessimistic claims"): "both these extremes are misguided". Del paper
> se leyó solo el abstract. Huyen cita a LeCun en la misma línea: "autoregressive LLMs can't plan".
>
> **Pregunta abierta (Huyen, 2025).** Huyen deja sin cerrar si el límite es del modelo o de cómo se
> lo usa, y muestra que el modelo puede corregir el rumbo dentro del bucle.
>
> **Lo que cambió después.** El paper es de 2024, anterior a los modelos de razonamiento; no se
> encontró una actualización de la tesis. La disputa sobre si esos modelos razonan (el estudio de
> Apple sobre puzzles y sus réplicas) está en [Razonamiento](../Modelos/razonamiento.md). Lectura
> de esta base: las dos posiciones llevan a la misma práctica, poner un verificador externo donde
> se pueda, lo pueda o no hacer el modelo solo.

## Reflexión: el agente revisa lo que hizo

La reflexión es pedirle al agente que evalúe un paso o un resultado y, si salió mal, explique por
qué antes de reintentar. Puede hacerla el mismo modelo o un componente aparte que evalúa, como en
el patrón [evaluador-optimizador](patrones-de-flujo.md#los-cinco-patrones-de-workflow). Huyen
la recomienda con su precio: "reflection is relatively easy to implement and can bring surprisingly
good performance improvement", pero "The downside of this approach is latency and cost".

Reflexion (Shinn et al., 2023) la lleva entre intentos: el agente mejora "not by updating weights,
but instead through linguistic feedback", y guarda sus reflexiones "in an episodic memory buffer"
para el intento siguiente. Según su abstract, "Reflexion achieves a 91% pass@1 accuracy on the
HumanEval coding benchmark". Es un resultado de los autores en un benchmark de código que hoy está
saturado. Guardar lo aprendido entre intentos es un caso de [memoria](../Contexto/memoria.md).

La reflexión hereda el límite de la sección anterior: un modelo que no verifica bien su propio
plan tampoco verifica bien su propio resultado. Donde hay un verificador externo (las pruebas que
pasan o no, el compilador, el estado de una base de datos), la reflexión tiene contra qué
corregirse (lectura de esta base).

## Tareas largas: el horizonte de tiempo

METR mide cuán larga es la tarea que un agente puede completar con su "50%-task-completion time
horizon": "the time humans typically take to complete tasks that AI models can complete with 50%
success rate". La medida es el tiempo que le lleva la tarea a una persona experta, no el tiempo del
agente. En su preprint de 2025, METR encontró que ese horizonte "has been doubling approximately
every seven months since 2019" y que "the trend may have accelerated in 2024". Las tareas son de
ingeniería de software, ML y ciberseguridad, y la página de METR advierte que los tiempos humanos
probablemente sobreestiman lo que tarda un experto que ya conoce el contexto. Los valores por
modelo y el estado de la página están en la ficha
[Benchmarks de agentes](benchmarks-de-agentes.md).

En la práctica, una tarea más larga que una sesión se sostiene con artefactos fuera del modelo:
Anthropic (2025-11-26) usa una lista de funciones por hacer y un archivo de progreso, y un agente
que hace una función por sesión. Ese andamiaje es parte del harness descrito en
[Agente](agente.md#harness-engineering-2026-el-sistema-alrededor-del-modelo), y lo que se guarda
entre sesiones, de la [memoria](../Contexto/memoria.md).

## Qué leer sobre planificación

El post ["Agents"](https://huyenchip.com/2025/01/07/agents.html) de Huyen, secciones "Planning" y
"Reflection": fijarse en por qué conviene separar el plan de la ejecución. El abstract de
[Kambhampati et al.](https://arxiv.org/abs/2402.01817), para la postura de que el modelo necesita
un verificador externo. El [paper de METR](https://arxiv.org/abs/2503.14499), para la definición
del horizonte de tiempo, leído con las advertencias de su página.

> [!NOTE]
> Sin fuente todavía: planificación con búsqueda en árbol (Tree of Thoughts y sucesores) y una
> medición de cómo cambia la planificación de un agente con los modelos de razonamiento.
