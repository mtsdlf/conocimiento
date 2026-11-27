---
resumen: >-
  Un agente es un sistema en el que el modelo decide sus propios pasos: planifica, llama
  herramientas, mira el resultado y sigue hasta terminar la tarea, en lugar de recorrer un camino
  fijado en el código.
estado: vigente
estabilidad: semi
fuentes:
  - https://huyenchip.com/2025/01/07/agents.html
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 6 «Agents», pp. 275-305; cap. 10 «Step 5. Add Agent Patterns», p. 463"
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://cognition.com/blog/dont-build-multi-agents
  - https://arxiv.org/abs/2407.01502
  - https://www.anthropic.com/news/model-context-protocol
  - https://modelcontextprotocol.io/specification/latest
  - https://lilianweng.github.io/posts/2026-07-04-harness/
  - https://openai.com/index/harness-engineering/
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://claude.com/resources/articles/harnessing-claudes-intelligence
  - https://www.latent.space/p/ainews-is-harness-engineering-real
aliases: [agent, agente de IA, AI agent, agentic system, sistema agéntico, harness, harness engineering]
creado: 2026-11-27
revisado: 2026-11-27
---

# Agente

Un agente es un sistema en el que el modelo decide sus propios pasos: planifica, llama
herramientas, mira el resultado y sigue hasta terminar la tarea, en lugar de recorrer un camino
fijado en el código.

Es el paso 5 de la arquitectura de Huyen, "Add Complex Logic and Write Actions" (en el libro, "Add
Agent Patterns"), para tareas de varios pasos o que cambian algo afuera del sistema. Huyen lo
define en sentido amplio: "anything that can perceive its environment and act upon that environment".

## Herramientas, planificación y las acciones de escritura

Huyen separa las herramientas en tres clases, y la tercera cambia el riesgo del sistema:

| Clase | Ejemplos | Qué agrega |
|---|---|---|
| Aumento de conocimiento | recuperadores, consultas SQL, búsqueda web | lo que el modelo no sabe; un [RAG](../Contexto/contexto-y-rag.md) es un agente con una sola de estas |
| Extensión de capacidad | calculadora, intérprete de código | lo que el modelo hace mal solo |
| Acciones de escritura | mandar un email, hacer una transferencia | efectos en el mundo, que no se deshacen con otra respuesta |

"Planning, at its core, is a search problem", escribe Huyen, y recomienda validar el plan antes de
ejecutarlo: Huyen propone validarlo con heurísticas o con un modelo juez, y admite que una persona intervenga en cualquier etapa; los [guardrails](../Produccion/guardrails.md) también pueden validarlo (lectura de esta base). Una
acción que el agente puede repetir necesita una
[clave de idempotencia](../../Arquitectura/Sistemas-distribuidos/clave-de-idempotencia.md), y una que toca varios
sistemas, una [saga](../../Arquitectura/Sistemas-distribuidos/saga.md) (lectura de esta base).
El plan se desarrolla en [Planificación](planificacion.md).

## Las tres fallas de un agente

Huyen evalúa un agente por sus modos de falla: "To evaluate an agent, identify its failure modes
and measure how often each of these failure modes happens." Los agrupa en tres:

1. **De planificación**: elige una herramienta que no existe o con parámetros erróneos, no llega
   al objetivo, o cree que terminó cuando no.
2. **De herramienta**: la herramienta devuelve algo erróneo, o el plan se traduce mal a la llamada.
3. **De eficiencia**: llega, pero con pasos de más, más costo o más tiempo que una línea de base.

Cada una se mide aparte en la [evaluación](../Evaluacion/evals.md), y las
trazas de la [observabilidad](../Produccion/observabilidad-de-modelos.md) son la materia
prima del [análisis de errores](../Evaluacion/analisis-de-errores.md) que las
encuentra. Según su resumen, Kapoor et al. (2024) advierten sobre la tercera: medir solo
precisión lleva a agentes "needlessly complex and expensive". Se desarrolla en
[Fallas de agentes](fallas-de-agentes.md).

## Workflow o agente: los cinco patrones de Anthropic

Anthropic ("Building effective agents", 2024) separa dos cosas que suelen llamarse igual. Un
*workflow* son "systems where LLMs and tools are orchestrated through predefined code paths"; un
agente, "systems where LLMs dynamically direct their own processes and tool usage". La diferencia
es quién decide el camino: el código o el modelo. Su consejo es buscar "the simplest solution
possible, and only increasing complexity when needed", y la mayoría cabe en
uno de cinco patrones de workflow:

| Patrón | Qué hace |
|---|---|
| Prompt chaining | encadena llamadas, cada una sobre la salida de la anterior, con controles entre medio |
| Routing | clasifica la entrada y la manda a un camino especializado (como el [router](../Produccion/router-y-gateway-de-modelos.md)) |
| Parallelization | corre partes en paralelo (*sectioning*) o la misma tarea varias veces y vota (*voting*) |
| Orchestrator-workers | un modelo reparte subtareas a otros y junta los resultados |
| Evaluator-optimizer | un modelo genera y otro evalúa, en un bucle |

Los sistemas multiagente son el caso extremo. Anthropic reporta que el suyo de investigación
rindió 90,2% más que un agente solo en su evaluación interna, con unas 15 veces los tokens de un
chat, y que no sirve cuando hay mucho contexto compartido o muchas dependencias, como en la mayoría
del código. Cognition ("Don't Build Multi-Agents", 2025) pide compartir contexto y trazas completas,
porque "actions carry implicit decisions, and conflicting decisions carry bad results". Los dos son
informes de proveedores, no estudios independientes. Se desarrolla en
[Patrones de flujo](patrones-de-flujo.md).

## Frameworks de agentes: llamar directo primero

Huyen cuenta entre los errores comunes "use an agentic framework when direct API calls work", y
Anthropic advierte que los frameworks pueden "create extra layers of abstraction that can obscure
the underlying prompts". Se critica el framework opaco, no la orquestación ([Sistemas con modelos](../Produccion/sistemas-con-modelos.md)). No hay un estudio independiente que compare
framework y llamada directa.

## MCP: un protocolo para conectar herramientas

MCP (Model Context Protocol) es un estándar abierto para conectar un modelo con las herramientas y
los datos que usa, de modo que cada herramienta se escriba una vez y sirva a cualquier aplicación.
Anthropic lo anunció en noviembre de 2024 con el problema que resuelve: "Every new data source
requires its own custom implementation". Se inspira en el Language Server Protocol.

La especificación define tres roles: la aplicación que aloja al modelo (*host*), los clientes y los
servidores (herramientas, recursos y prompts). Los mensajes viajan en JSON-RPC 2.0.
Su advertencia de seguridad importa para la arquitectura: las herramientas "represent
arbitrary code execution", y sus descripciones no son confiables salvo que el servidor lo sea.
Conectar un servidor MCP pide el cuidado de una acción de escritura (lectura de esta base). La especificación se versiona por fecha, y la vigente se lee en
[la fuente](https://modelcontextprotocol.io/specification/latest). Se desarrolla en
[Uso de herramientas](uso-de-herramientas.md) y en [Versiones de MCP](versiones-de-mcp.md).

## Harness engineering (2026): el sistema alrededor del modelo

*Al 2026-11-27, término nuevo sin definición fijada.*

El harness es lo que rodea al modelo en un agente: el bucle, las herramientas, cómo se
administra el contexto, dónde se guardan los artefactos y cómo se evalúa el resultado. Lilian
Weng lo define como "the system surrounding a base model that orchestrates execution"; Anthropic,
como "the software scaffolding around a model". El término no es de Huyen: no se encontró ningún texto suyo sobre harness;
el ensayo de 2026 que lo pone en el centro es de Weng ("Harness Engineering for Self-Improvement").

Tres textos de 2025-2026 dicen qué cambia:

- **OpenAI** (Lopopolo, 2026-02-11) cuenta un producto interno de alrededor de un millón de líneas,
  hecho en cinco meses sin escribir código a mano, con unos 1.500 PR. El trabajo pasa a ser
  "designing environments, specifying intent, and building feedback loops": cuando el agente falla,
  se agrega la herramienta, el control o la documentación que faltaba, en lugar de reintentar el
  prompt. Las reglas de arquitectura se imponen con linters y pruebas. Las cifras son del propio
  equipo y el artículo no define "harness".
- **Anthropic** (2025-11 y 2026-03) muestra que el harness hace posible una tarea larga (una lista
  de funciones y un archivo de progreso sostienen el trabajo entre sesiones sin memoria). Su principio es que "every component in a harness encodes an assumption about what the model
  can't do on its own", y esas suposiciones envejecen: piezas que hacían falta con un modelo
  sobraron con el siguiente.
- **Weng** (2026-07-04) propone que el camino hacia sistemas que se mejoran solos "is unlikely to
  start as a model directly rewriting its weights", sino optimizando el harness, y marca el límite:
  "Current self-improvement loops work best for tasks when evaluation metrics are measurable and
  objective". Sin un buen evaluador, el harness no tiene contra qué mejorar.

Lo que esta base saca en limpio: el foco pasa del prompt al entorno, con el
[contexto](../Contexto/contexto-y-rag.md) como pieza; el harness se poda cuando el modelo mejora; y
la [evaluación](../Evaluacion/evals.md) vuelve al centro, como lo que el
harness optimiza.

> [!IMPORTANT]
> ¿Modelo grande o harness grande? Latent Space (2026-03-04) ordena la disputa. Del lado del
> modelo, Boris Cherny (Anthropic) describe el agente de código de su empresa como "the thinnest
> possible wrapper over the model", Noam Brown (OpenAI) espera que los modelos de razonamiento
> reemplacen los andamiajes, y METR y Scale AI encuentran poca diferencia entre los harness de los
> proveedores y uno básico. Del lado del harness, Jerry Liu (LlamaIndex) sostiene que "the Model
> Harness is Everything", y una prueba mejoró a 15 modelos en código cambiando solo el harness.
> Latent Space ve "real value" en el harness y advierte que cada bando tiene interés comercial; las
> mediciones independientes llegan de segunda mano.

## Qué leer sobre agentes

Para la definición y las fallas, el post ["Agents"](https://huyenchip.com/2025/01/07/agents.html)
de Huyen y, en el cap. 6 del libro, "Planning" (p. 281) y "Agent Failure Modes and Evaluation"
(p. 298). Para el criterio de diseño, ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents).
Para harness engineering, el caso de [OpenAI](https://openai.com/index/harness-engineering/) y
["Harness design for long-running application development"](https://www.anthropic.com/engineering/harness-design-long-running-apps);
conviene fijarse en qué piezas del harness se pueden quitar.

> [!NOTE]
> Sin fuente todavía: una medición independiente y reproducible del efecto del harness. La memoria
> de agentes (Huyen, cap. 6, p. 300) se trata en [Memoria](../Contexto/memoria.md).
