---
resumen: >-
  Agentes es la parte de un sistema con un modelo adentro en la que el modelo actúa: llama
  herramientas, encadena pasos y, en el extremo, decide él mismo qué hacer hasta terminar la
  tarea. Abarca el mecanismo de las herramientas, los patrones para encadenar pasos, la
  planificación y cómo fallan y se evalúan los agentes.
estado: vigente
estabilidad: semi
fuentes:
  - https://huyenchip.com/2025/01/07/agents.html
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 6 «Agents», pp. 275-305 (según el índice)"
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://arxiv.org/abs/2507.09089
  - https://metr.org/blog/2026-02-24-uplift-update/
  - https://papers.ssrn.com/abstract=4945566
  - https://arxiv.org/abs/2412.14161
  - https://arxiv.org/abs/2402.01817
  - https://cognition.com/blog/dont-build-multi-agents
aliases: [agentes de IA, AI agents, agentic AI, IA agéntica]
creado: 2026-11-27
revisado: 2026-11-27
---

# Agentes

Agentes es la parte de un sistema con un modelo adentro en la que el modelo actúa: llama
herramientas, encadena pasos y, en el extremo, decide él mismo qué hacer hasta terminar la
tarea. Abarca el mecanismo de las herramientas, los patrones para encadenar pasos, la
planificación y cómo fallan y se evalúan los agentes.

Es una de las tres formas de adaptar un modelo a una tarea, junto con cambiar lo que entra en su
ventana ([Contexto](../Contexto/contexto.md)) y cambiar sus pesos ([Ajuste](../Ajuste/ajuste.md)).
Recibe de [Modelos](../Modelos/modelos.md) un modelo que genera texto probable, también cuando
genera la llamada a una herramienta, y por eso hereda la [alucinación](../Modelos/alucinacion.md).
Se cruza con Contexto en dos lugares: lo que devuelve cada herramienta entra a la ventana, con su
riesgo de [inyección de prompt](../Contexto/inyeccion-de-prompt.md), y lo que el agente recuerda
entre pasos y sesiones es su [memoria](../Contexto/memoria.md). Le entrega a
[Evaluación](../Evaluacion/evaluacion.md) trayectorias que medir y a
[Producción](../Produccion/produccion.md) acciones que operar y vigilar.

## De la llamada única al agente

Un sistema con un modelo puede ubicarse en una escala, según quién decide el próximo paso:

| Escalón | Quién decide el camino | Ejemplo |
|---|---|---|
| Llamada única | nadie: una entrada, una salida | resumir un documento |
| Workflow | el código, con pasos fijos o ramas previstas | clasificar un ticket y mandarlo a la cola que corresponde |
| Agente | el modelo, paso a paso | investigar un bug, leer archivos, probar un arreglo y abrir el PR |
| Multiagente | varios modelos que se reparten la tarea | un agente principal que manda subagentes a investigar fuentes distintas |

El mecanismo es el mismo en todos los escalones: el modelo no ejecuta nada, emite una llamada
estructurada a una herramienta que la aplicación declaró, la aplicación la ejecuta y le devuelve
el resultado. Un agente es ese circuito repetido hasta que el modelo deja de pedir herramientas.
Cada escalón suma capacidad y también latencia, costo y formas de fallar. Anthropic aconseja
buscar "the simplest solution possible, and only increasing complexity when needed".

## Lo que se decide al construir un agente

Cuatro decisiones arman un agente, y cada una tiene su nota:

- **Qué herramientas tiene y cómo están escritas.** Pocas, de alto impacto, con descripciones
  pensadas como un prompt; las de escritura cambian el riesgo del sistema.
- **Cuánto decide el modelo.** Un workflow con un patrón conocido (encadenamiento, ruteo,
  paralelización, orquestador-trabajadores, evaluador-optimizador) es más predecible que un agente
  libre; un sistema multiagente conviene cuando las partes no comparten decisiones (lectura de esta
  base, a partir de la disputa entre Anthropic y Cognition).
- **Cómo planifica y se corrige.** Kambhampati et al. sostienen que un modelo no planifica de
  forma confiable por sí solo, una tesis disputada; Huyen recomienda separar el plan de la
  ejecución y validarlo antes de ejecutarlo.
- **Qué puede romper y cómo se mide.** Cada acción de escritura lleva mínimo privilegio y, si es de
  alto impacto, aprobación humana; la evaluación mide cada modo de falla y la fiabilidad en varios
  intentos (pass^k, explicada en [Fallas de agentes](fallas-de-agentes.md#cómo-se-evalúa-un-agente)).

El sistema alrededor del modelo que sostiene todo eso (el bucle, las herramientas, el manejo del
contexto, los artefactos entre sesiones) se llama harness, y se explica en
[Agente](agente.md#harness-engineering-2026-el-sistema-alrededor-del-modelo).

## Cuánto acelera un agente: lo que se midió

La afirmación de que los agentes y la IA para programar aceleran el trabajo es de las más
repetidas del campo y de las menos medidas. Los estudios con método que hay se contradicen o
tienen límites que sus propios autores declaran.

> [!IMPORTANT]
> **Más lento, en el único ensayo controlado con desarrolladores experimentados (METR, 2025).**
> Becker et al. asignaron al azar 246 tareas de proyectos maduros de código abierto a "permitir IA"
> o "no permitir IA", con 16 desarrolladores que tenían "an average of 5 years of prior experience"
> en esos proyectos. Con la IA permitida, el tiempo para completar las tareas subió 19 %, con un
> intervalo de confianza de +2 % a +39 %. Antes de empezar, los desarrolladores esperaban que la IA
> lo redujera 24 %; al terminar, creían que lo había reducido 20 %. Economistas y expertos en ML
> habían predicho reducciones de 39 % y 38 %.
>
> **Más rápido, con intervalos que incluyen cero (METR, 2026-02-24).** El segundo estudio, con "57
> developers, across 143 repos, and 800+ tasks", estimó un cambio de -18 % en el tiempo por tarea
> para los desarrolladores del primer estudio (intervalo de -38 % a +9 %) y de -4 % para los nuevos
> (de -15 % a +9 %). METR advierte un sesgo de selección: entre "30% to 50% of developers" dijeron
> que no presentaban algunas tareas porque no querían hacerlas sin IA, lo que "likely biases
> downwards our estimate of AI-assisted speedup". El pago bajó de 150 a 50 dólares por hora entre
> estudios. Su conclusión: cree que la aceleración de 2026 es mayor que la de 2025, pero sus datos
> son "only very weak evidence for the size of this increase" y dan "an unreliable signal of the
> current productivity effect of AI tools". Rediseña el estudio.
>
> **Más tareas completadas, en empresas (Cui et al., Management Science).** Tres experimentos de
> campo con un asistente de código en tres empresas grandes, con 4.867 desarrolladores, dieron
> 26,08 % más tareas completadas (error estándar de 10,3 %), con más ganancia en juniors (27 % a
> 39 %) que en seniors (8 % a 13 %). Estas cifras vienen de un resumen del buscador; el paper no se
> abrió. No contradice a METR: mide otra población (empresas, muchos juniors) y otra variable
> (tareas completadas en un período, no tiempo por tarea).
>
> **Agentes solos, en una empresa simulada (TheAgentCompany, 2025).** Según su abstract, "the most
> competitive agent can complete 30% of tasks autonomously", y "more difficult long-horizon tasks
> are still beyond the reach of current systems".
>
> **Lectura de esta base.** Ni "los agentes aceleran" ni "los agentes frenan" se sostienen con estos
> estudios. Lo firme es la brecha entre lo que la gente cree y lo que se mide: en el estudio de
> 2025, quienes iban 19 % más lentos creían ir 20 % más rápido, aunque con n = 16. Para un equipo,
> la consecuencia práctica es medir el efecto en su propio trabajo en lugar de confiar en la
> percepción, con el mismo criterio que la [evaluación](../Evaluacion/evaluacion.md) aplica a un
> modelo.

Las herramientas concretas para programar con agentes están fuera de este tema, en
[Desarrollo](../../Desarrollo/desarrollo.md).

## Lo que hay adentro de Agentes

En orden de lectura:

- [Agente](agente.md) — qué es, las tres clases de herramientas de Huyen, frameworks y harness
  engineering, con enlaces a las notas que desarrollan workflows, MCP y fallas; la nota de partida.
- [Uso de herramientas](uso-de-herramientas.md) — cómo el modelo pide ejecutar una función, cómo
  se diseña una herramienta y qué es MCP.
- [Versiones de MCP](versiones-de-mcp.md) — ficha con la historia de la especificación, su
  gobierno y la adopción, copiada el 2026-11-27.
- [Patrones de flujo](patrones-de-flujo.md) — workflow o agente, los cinco patrones, el bucle
  ReAct (razonar, actuar y observar, intercalados) y la disputa sobre multiagente.
- [Planificación](planificacion.md) — cómo el agente arma un plan, por qué el error se acumula,
  si un modelo puede planificar y el horizonte de tiempo de las tareas largas.
- [Fallas de agentes](fallas-de-agentes.md) — modos de falla, cómo se evalúa un agente (resultado,
  trayectoria y pass^k, que pide que salgan bien todos los intentos) y cómo se limitan sus acciones.
- [Benchmarks de agentes](benchmarks-de-agentes.md) — ficha con qué mide cada benchmark público de
  agentes y sus resultados fechados.

La memoria de los agentes vive en [Memoria](../Contexto/memoria.md) y el manejo de lo que entra en
la ventana a lo largo de una tarea, en [Ingeniería de contexto](../Contexto/ingenieria-de-contexto.md).
