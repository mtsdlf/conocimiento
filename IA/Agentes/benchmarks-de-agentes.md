---
resumen: >-
  Los benchmarks públicos de agentes (SWE-bench, τ-bench, GAIA, TheAgentCompany y el horizonte de
  tiempo de METR), con qué mide cada uno, los resultados publicados con su fecha y lo que se sabe
  de su validez, copiado el 2026-11-27.
estado: borrador
estabilidad: volatil
fuentes:
  - https://arxiv.org/abs/2310.06770
  - https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
  - https://openai.com/index/separating-signal-from-noise-coding-evaluations
  - https://arxiv.org/abs/2406.12045
  - https://arxiv.org/abs/2311.12983
  - https://arxiv.org/abs/2412.14161
  - https://arxiv.org/abs/2503.14499
  - https://metr.org/time-horizons/
aliases: [agent benchmarks, benchmarks de agentes, SWE-bench, τ-bench, tau-bench, GAIA, TheAgentCompany]
creado: 2026-11-27
revisado:
---

# Benchmarks de agentes

Los benchmarks públicos de agentes (SWE-bench, τ-bench, GAIA, TheAgentCompany y el horizonte de
tiempo de METR), con qué mide cada uno, los resultados publicados con su fecha y lo que se sabe
de su validez, copiado el 2026-11-27.

Implementa la evaluación por resultado que se describe en
[Fallas de agentes](fallas-de-agentes.md#cómo-se-evalúa-un-agente). Los benchmarks de modelos en
general y por qué un ranking público dice menos de lo que su nombre promete están en
[Benchmarks y elección de modelo](../Evaluacion/benchmarks-y-eleccion-de-modelo.md). Cada fila
tiene su fuente viva; los resultados envejecen rápido y los de la tabla sirven como historia, no
como estado del arte.

## Qué mide cada benchmark

| Benchmark | Qué le pide al agente | Cómo puntúa | Resultado publicado (fecha) |
|---|---|---|---|
| SWE-bench (Jimenez et al., ICLR 2024) | resolver issues reales de repositorios de GitHub | las pruebas del repositorio pasan o no | el mejor modelo del paper, Claude 2, resolvió 1,96 % (2023) |
| τ-bench (Yao et al., Sierra, 2024-06-17) | atender a un usuario simulado por un modelo, con herramientas y reglas de negocio (comercio, aerolínea) | compara el estado final de la base de datos con el objetivo; introduce pass^k | "even state-of-the-art function calling agents (like gpt-4o) succeed on <50% of the tasks", y son "quite inconsistent (pass^8 <25% in retail)" (2024; cita recotejada contra el abstract el 2026-11-27) |
| GAIA (Mialon et al., 2023-11-21) | preguntas de asistente general que piden buscar, leer y usar herramientas | respuesta exacta | según su abstract, personas 92 % contra 15 % de GPT-4 con plugins (2023) |
| TheAgentCompany (Xu et al., v3 2025-09-10) | tareas de un trabajador digital en una empresa simulada | tareas completadas y parciales | "the most competitive agent can complete 30% of tasks autonomously" (2025); "more difficult long-horizon tasks are still beyond the reach of current systems" |
| Horizonte de tiempo (METR, Kwa et al., v1 2025-03-18) | tareas de software, ML y ciberseguridad de duración humana conocida | la duración humana de las tareas que el agente completa con 50 % de éxito | Claude 3.7 Sonnet, "around 50 minutes" (2025-03); un agente con GPT-5, "around 2 hours and 17 minutes", según la página |

## Lo que se sabe de su validez

- **SWE-bench Verified.** OpenAI dejó de reportarlo el 2026-02-23 porque, según el resumen del
  buscador, los avances reflejan cada vez más cuánto vio el modelo el benchmark durante el
  entrenamiento. Recomendó SWE-bench Pro y después se retractó: su auditoría estima que cerca de
  30 % de las tareas de Pro están rotas. Las dos cosas vienen de resúmenes de buscador y de una
  fuente interesada, que compite en esos rankings; ninguna fuente independiente lo confirmó.
- **Horizonte de tiempo de METR.** La página dice "This page is no longer actively updated" desde
  el 2026-09-08; el último modelo agregado fue Claude Mythos Preview, el 2026-05-08. Advierte que
  "Measurements above 16 hrs are unreliable with our current task suite" y que las duraciones
  humanas "likely overestimate how long a human expert takes". Los valores por modelo están solo en
  un gráfico interactivo.
- **τ-bench.** Existe una versión posterior (τ²-bench) que no se revisó.

> [!NOTE]
> Sin fuente todavía: una fuente independiente sobre qué benchmark de agentes de código es
> confiable en 2026, y puntajes vigentes de τ-bench y GAIA.
