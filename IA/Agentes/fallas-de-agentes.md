---
resumen: >-
  Un agente falla de formas propias (planes inválidos, herramientas mal llamadas, tareas que da
  por terminadas sin terminar, pasos de más) y se evalúa midiendo cada modo de falla por separado,
  la trayectoria y no solo el resultado, y la fiabilidad en varios intentos; como actúa sobre el
  mundo, sus acciones se limitan con mínimo privilegio y aprobación humana.
estado: borrador
estabilidad: semi
fuentes:
  - https://huyenchip.com/2025/01/07/agents.html
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 6 «Agents», sección «Agent Failure Modes and Evaluation», p. 298 (según el índice)"
  - https://arxiv.org/abs/2503.13657
  - https://arxiv.org/abs/2406.12045
  - https://arxiv.org/abs/2407.01502
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
  - https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://modelcontextprotocol.io/specification/latest
aliases: [agent failure modes, modos de falla de agentes, evaluación de agentes, agent evaluation, excessive agency, agencia excesiva, pass^k, trifecta letal, lethal trifecta, MAST]
creado: 2026-11-27
revisado:
---

# Fallas de agentes

Un agente falla de formas propias (planes inválidos, herramientas mal llamadas, tareas que da
por terminadas sin terminar, pasos de más) y se evalúa midiendo cada modo de falla por separado,
la trayectoria y no solo el resultado, y la fiabilidad en varios intentos; como actúa sobre el
mundo, sus acciones se limitan con mínimo privilegio y aprobación humana.

Un [agente](agente.md) suma a las fallas de cualquier modelo (la
[alucinación](../Modelos/alucinacion.md), la sensibilidad al prompt) las de encadenar pasos y
actuar. Las tres literaturas que tratan esto (taxonomías de falla, benchmarks y seguridad) se
juntan acá porque se usan juntas: lo que falla define qué se mide, y lo que puede romper define
qué se limita.

## Cómo falla un agente

Huyen agrupa las fallas en tres familias, ya resumidas en
[Agente](agente.md#las-tres-fallas-de-un-agente). Las de planificación, en su post, empiezan por
el uso de herramientas: "Invalid tool", "Valid tool, invalid parameters." y "Valid tool, incorrect
parameter values". Les siguen el plan que no llega al objetivo, el que no respeta una restricción
(de presupuesto, de tiempo) y el agente que cree haber terminado cuando no. Las de herramienta son
la herramienta que devuelve algo erróneo o la traducción mala del plan a la llamada. Las de
eficiencia son llegar con más pasos, costo o tiempo que una línea de base.

Es una taxonomía de autora, sin método empírico explícito. La que tiene método es MAST (Cemri et
al., preprint de 2025), para sistemas multiagente. Según su abstract, se construyó con 150 trazas
"validated by high inter-annotator agreement (kappa = 0.88)" e identifica "14 unique modes,
clustered into 3 categories": "(i) system design issues, (ii) inter-agent misalignment, and (iii)
task verification". Después se aplicó con un modelo como juez sobre MAST-Data, "1600+ annotated
traces collected across 7 popular MAS frameworks". Es de sistemas multiagente y de modelos de
2024-2025, así que no se traslada sin más a un agente solo.

Dos fallas se repiten en los agentes de tareas largas. Anthropic (2025-11-26) observó que su agente
de código declaraba el proyecto terminado antes de tiempo y marcaba funciones como hechas sin
probarlas; lo corrigió con una lista de funciones explícita y pruebas de punta a punta con un
navegador automatizado. La otra es el error que se acumula: con 95 % de acierto por paso, diez
pasos dan 60 %, como se explica en
[Planificación](planificacion.md#por-qué-los-planes-largos-fallan-el-error-se-acumula).

## Cómo se evalúa un agente

"To evaluate an agent, identify its failure modes and measure how often each of these failure
modes happens", escribe Huyen. Los modos de falla no se inventan en abstracto: salen del
[análisis de errores](../Evaluacion/analisis-de-errores.md) sobre las trazas que guarda la
[observabilidad](../Produccion/observabilidad-de-modelos.md), y cada uno se vuelve un caso de las
[evals](../Evaluacion/evals.md). Huyen sugiere probar cada herramienta por separado, armar un
conjunto de pares (tarea, herramientas disponibles) y buscar qué tipo de tarea o qué herramienta
concentra los errores; si una herramienta es demasiado difícil para el agente, se cambia la
herramienta.

Un agente se mira por tres lados, que no compiten:

| Qué se mira | Qué pregunta | De dónde sale |
|---|---|---|
| El resultado | ¿Quedó el mundo como tenía que quedar? | τ-bench compara el estado final de la base de datos con el objetivo anotado |
| La trayectoria | ¿Las llamadas y el plan eran válidos? ¿Cuántos pasos dio? | Huyen: validez de llamadas y planes, y "How many steps does the agent need, on average, to complete a task?" |
| La fiabilidad | ¿Lo logra cada vez, o solo a veces? | τ-bench introduce pass^k |

La fiabilidad es lo que más se pasa por alto. pass@k cuenta como éxito que al menos uno de k
intentos salga bien; pass^k pide que salgan bien los k. Un agente que atiende clientes corre la
misma tarea miles de veces, y lo que importa es pass^k. En τ-bench, los mejores agentes de 2024
resolvían menos de la mitad de las tareas, y con ocho intentos el puntaje en comercio bajaba de
25 % (los valores están en la ficha [Benchmarks de agentes](benchmarks-de-agentes.md)).

El costo entra en la evaluación. Kapoor et al. (2024), según su resumen, advierten que medir solo
precisión lleva a agentes "needlessly complex and expensive"; por eso Huyen compara la eficiencia
contra una línea de base en pasos, costo y latencia. Los benchmarks públicos de agentes, con sus
problemas de validez, están en la ficha; cómo leer un benchmark en general, en
[Benchmarks y elección de modelo](../Evaluacion/benchmarks-y-eleccion-de-modelo.md).

## Qué puede romper un agente que actúa

Un agente con [acciones de escritura](uso-de-herramientas.md) puede hacer daño que no se deshace
con otra respuesta. Huyen lo compara con un pasante: "Just as you shouldn't give an intern the
authority to delete your production database", no se le da a un sistema poco confiable una
acción irreversible como una transferencia.

OWASP (LLM06:2025, *Excessive Agency*) pone la causa en tres excesos: funcionalidad (herramientas
que el agente no necesita), permisos (más acceso del que la tarea pide) y autonomía (acciones de
alto impacto sin control). Sus mitigaciones son concretas:

1. **Mínimo privilegio**: solo las herramientas y los permisos que la tarea necesita; una
   herramienta de lectura no tiene credenciales de escritura.
2. **Aprobación humana en lo que importa**: "Utilise human-in-the-loop control to require a human
   to approve high-impact actions before they are taken". La aprobación va en las acciones de
   escritura de alto impacto, no en cada paso (lectura de esta base).
3. **Autorización afuera del modelo**: "Implement authorization in downstream systems rather than
   relying on an LLM to decide if an action is allowed or not."

A esas tres se suman las de la arquitectura del agente: ejecutar en un entorno aislado (Anthropic
recomienda "extensive testing in sandboxed environments"), dar a cada acción repetible su
[clave de idempotencia](../../Arquitectura/Sistemas-distribuidos/clave-de-idempotencia.md) y, si
la acción cruza varios sistemas, compensarla con una [saga](../../Arquitectura/Sistemas-distribuidos/saga.md).
Los controles sobre lo que entra y sale del modelo son los [guardrails](../Produccion/guardrails.md).

La amenaza que vuelve peligroso a un agente aun con permisos razonables es el contenido hostil que
llega por una herramienta: la [inyección de prompt](../Contexto/inyeccion-de-prompt.md). Willison
(2025-06-16) la resume en la "trifecta letal": si un agente junta acceso a datos privados,
exposición a contenido no confiable y una forma de comunicarse hacia afuera, un atacante puede
hacer que le mande los datos. Es la tesis de un practicante, no un estudio, pero da una regla de
diseño: sacarle al agente al menos una de las tres. La especificación de MCP pide consentimiento
explícito antes de cada herramienta y admite que el protocolo no puede imponerlo.

## Qué leer sobre fallas

El post ["Agents"](https://huyenchip.com/2025/01/07/agents.html) de Huyen, secciones de modos de
falla y evaluación, para el vocabulario. El abstract y la tabla de modos de
[MAST](https://arxiv.org/abs/2503.13657), para una taxonomía con método. [τ-bench](https://arxiv.org/abs/2406.12045),
para entender pass^k. [OWASP LLM06](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
y la [trifecta letal](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), para la
seguridad: fijarse en que la autorización vive en el sistema de destino.

> [!NOTE]
> Sin fuente todavía: tasas de falla por modo en agentes de un solo hilo con modelos de 2026,
> incidentes reales documentados con fuente primaria (agentes que borraron datos o filtraron
> información) y estudios sobre la fatiga de aprobación cuando una persona tiene que confirmar
> muchas acciones.
