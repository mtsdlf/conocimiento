---
resumen: >-
  Los patrones de flujo son las formas de encadenar llamadas a un modelo y a herramientas, desde un
  workflow con el camino fijado en el código hasta un agente que decide sus pasos, pasando por
  cinco patrones intermedios; los sistemas multiagente son el extremo, y su conveniencia está en
  disputa.
estado: borrador
estabilidad: semi
fuentes:
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://huyenchip.com/2025/01/07/agents.html
  - https://arxiv.org/abs/2210.03629
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://cognition.com/blog/dont-build-multi-agents
  - https://arxiv.org/abs/2503.13657
aliases: [workflow, flujo fijo, agentic workflow, patrones agénticos, agent patterns, multiagente, multi-agent system, sistema multiagente, ReAct, orchestrator-workers, evaluator-optimizer, prompt chaining]
creado: 2026-11-27
revisado:
---

# Patrones de flujo

Los patrones de flujo son las formas de encadenar llamadas a un modelo y a herramientas, desde un
workflow con el camino fijado en el código hasta un agente que decide sus pasos, pasando por
cinco patrones intermedios; los sistemas multiagente son el extremo, y su conveniencia está en
disputa.

## Workflow o agente: quién decide el camino

Anthropic ("Building effective agents", 2024-12-19) separa dos sistemas que suelen llamarse igual.
Un workflow son "systems where LLMs and tools are orchestrated through predefined code paths"; un
agente, "systems where LLMs dynamically direct their own processes and tool usage, maintaining
control over how they accomplish tasks". La diferencia es quién decide el próximo paso: el código o
el modelo.

Las dos puntas cuestan distinto. Un workflow es predecible, se prueba como cualquier programa y
falla en los lugares que se previeron. Un [agente](agente.md) resuelve tareas cuyos pasos no se
conocen de antemano, pero "Agentic systems often trade latency and cost for better task
performance", y Anthropic recomienda "extensive testing in sandboxed environments, along with the
appropriate guardrails". El consejo de fondo es buscar "the simplest solution possible, and only
increasing complexity when needed": muchas veces alcanza con una sola llamada bien armada, con
[recuperación](../Contexto/recuperacion.md) y ejemplos en el prompt. Es el mismo principio que
[empezar simple](../../Arquitectura/Decisiones/empezar-simple.md) en arquitectura.

## Los cinco patrones de workflow

Entre la llamada única y el agente, Anthropic describe cinco patrones. Cada uno agrega una pieza de
control, y se elige por la forma de la tarea:

| Patrón | Qué hace | Cuándo conviene |
|---|---|---|
| Encadenamiento (*prompt chaining*) | cada llamada trabaja sobre la salida de la anterior, con controles entre pasos | la tarea se parte limpio en pasos fijos y conocidos |
| Ruteo (*routing*) | clasifica la entrada y la manda a un camino especializado | hay categorías distintas que conviene tratar aparte; incluye mandar lo simple a un modelo más barato, como hace un [router](../Produccion/router-y-gateway-de-modelos.md) |
| Paralelización (*parallelization*) | corre partes independientes a la vez (*sectioning*) o la misma tarea varias veces y vota (*voting*) | las partes no dependen entre sí, o hace falta más confianza en una respuesta |
| Orquestador-trabajadores (*orchestrator-workers*) | un modelo reparte subtareas a otros y junta los resultados | "complex tasks where you can't predict the subtasks needed", como un cambio de código cuyo número de archivos depende de la tarea |
| Evaluador-optimizador (*evaluator-optimizer*) | un modelo genera y otro evalúa, en un bucle | "when we have clear evaluation criteria, and when iterative refinement provides measurable value" |

El evaluador del último patrón es un uso de [IA como juez](../Evaluacion/ia-como-juez.md) dentro del
sistema, no solo en la evaluación, y hereda sus sesgos (lectura de esta base). La diferencia entre
el orquestador y un agente es de grado: el orquestador decide qué subtareas hay, pero el resto del
camino sigue escrito en el código (lectura de esta base).

Los cinco patrones son la taxonomía de un laboratorio, no un estándar del campo. Huyen no los usa:
organiza el tema por herramientas, planificación y fallas, y los patrones aparecen en su libro
como un paso de la arquitectura ("Add Agent Patterns", cap. 10), según el índice.

## El bucle del agente: razonar y actuar

Cuando el camino lo decide el modelo, el patrón más común es el de ReAct (Yao et al., 2022): el
modelo intercala un paso de razonamiento ("qué sé y qué me falta"), una acción (una llamada a una
[herramienta](uso-de-herramientas.md)) y la observación del resultado, y repite. Según su
abstract, ReAct "outperforms imitation and reinforcement learning methods by an absolute success
rate of 34% and 10% respectively" en dos entornos de prueba (ALFWorld y WebShop), y en preguntas
con búsqueda "overcomes issues of hallucination and error propagation prevalent in
chain-of-thought reasoning". Huyen lo confirma como práctica: "interleaving reasoning and action has
become a common pattern for agents".

Cómo el agente arma y corrige el plan dentro de ese bucle está en
[Planificación](planificacion.md); cómo se sostiene una tarea que dura más que una
[ventana de contexto](../Modelos/transformer.md#la-ventana-de-contexto), en
[Ingeniería de contexto](../Contexto/ingenieria-de-contexto.md), en
[Memoria](../Contexto/memoria.md) y en la sección de harness de [Agente](agente.md).

## Multiagente: varios agentes que se reparten la tarea

Un sistema multiagente reparte una tarea entre varios agentes, cada uno con su propia ventana de
contexto, coordinados por un agente principal o entre sí. Puede leerse como el patrón
orquestador-trabajadores llevado al extremo, en el que los trabajadores también deciden sus pasos
(lectura de esta base). Si conviene es la
disputa más visible de la vertical, y las dos posiciones vienen de empresas que venden agentes.

> [!IMPORTANT]
> **A favor, para investigar en paralelo (Anthropic, 2025-06-13).** Su sistema de investigación,
> con un agente principal y subagentes de un modelo más chico, superó en 90,2 % a un agente solo
> del modelo principal "on our internal research eval". El costo: "agents typically use about 4× more
> tokens than chat interactions", y "multi-agent systems use about 15× more tokens than chats". En
> un benchmark de búsqueda web, el uso de tokens "by itself explains 80% of the variance". El mismo
> texto marca dónde no sirve: "domains that require all agents to share the same context", la
> coordinación en tiempo real ("LLM agents are not yet great at coordinating and delegating to
> other agents in real time") y el código, porque "most coding tasks involve fewer truly
> parallelizable tasks than research".
>
> **En contra, para escribir código (Cognition, Walden Yan, 2025-06-12).** Sus dos principios:
> "Share context, and share full agent traces, not just individual messages" y "Actions carry
> implicit decisions, and conflicting decisions carry bad results". Dos subagentes que construyen
> partes de lo mismo sin ver lo que decidió el otro producen piezas que no encajan. Recomienda por
> defecto un agente lineal de un solo hilo y, para tareas largas, un modelo aparte que comprima el
> historial en "key details, events, and decisions".
>
> **La evidencia independiente.** Cemri et al. (UC Berkeley y otros, preprint de 2025) estudian por
> qué fallan los sistemas multiagente y parten de que "their performance gains on popular
> benchmarks are often minimal". Su taxonomía de fallas está en
> [Fallas de agentes](fallas-de-agentes.md#cómo-falla-un-agente).
>
> **Lectura de esta base.** Las dos posiciones no chocan de frente: Anthropic recomienda multiagente
> para tareas de lectura que se paralelizan, y Cognition lo descarta para tareas de escritura cuyas
> decisiones dependen unas de otras. Si el uso de tokens explica el 80 % de la varianza, parte de la
> mejora de Anthropic puede ser más cómputo y no mejor arquitectura. Ningún estudio independiente
> con modelos actuales arbitra entre las dos.

El criterio que sale de las dos fuentes: repartir entre agentes lo que se puede hacer sin
compartir decisiones (buscar, leer, resumir fuentes distintas) y mantener en un solo hilo lo que
tiene que quedar coherente (un cambio de código, un documento). La pregunta de si usar un framework
de agentes o llamar a la API directo está en [Agente](agente.md#frameworks-de-agentes-llamar-directo-primero).

## Qué leer sobre patrones

["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents),
para la definición y los cinco patrones: fijarse en los ejemplos de cuándo cada patrón no hace
falta. Después, juntos y en tensión,
["How we built our multi-agent research system"](https://www.anthropic.com/engineering/multi-agent-research-system)
y ["Don't Build Multi-Agents"](https://cognition.com/blog/dont-build-multi-agents): anotar en qué
difiere la tarea de cada uno.

> [!NOTE]
> Sin fuente todavía: un estudio revisado por pares sobre cuándo un workflow supera a un agente, y
> el contenido del capítulo de Huyen sobre patrones (cap. 10, p. 463).
