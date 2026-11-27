---
resumen: >-
  Los rankings y agregadores públicos de modelos que se consultan hoy, con lo que mostraban el
  2026-11-27: qué evalúan, quién los opera y los primeros puestos, copiados con fecha.
estado: vigente
estabilidad: volatil
fuentes:
  - https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
  - https://arena.ai/leaderboard
  - https://arena.ai/leaderboard/methodology
  - https://epoch.ai/benchmarks
  - https://arxiv.org/abs/2211.09110
aliases: [leaderboards, rankings de modelos, leaderboards vigentes]
creado: 2026-11-27
revisado: 2026-11-27
---

# Benchmarks vigentes

Los rankings y agregadores públicos de modelos que se consultan hoy, con lo que mostraban el
2026-11-27: qué evalúan, quién los opera y los primeros puestos, copiados con fecha.

Implementa el paso de acotar candidatos de [benchmarks y elección de modelo](benchmarks-y-eleccion-de-modelo.md),
donde está por qué un puntaje no alcanza para elegir. Las familias de modelos están en
[modelos disponibles](../Modelos/modelos-disponibles.md).

Copiado de cada fuente el 2026-11-27. Los nombres de modelos y versiones están como los devolvió la
herramienta de lectura y hay que verificarlos en la fuente antes de usarlos. Artificial Analysis y
Arena son operadores con interés comercial; Epoch AI es un instituto de investigación.

| Fuente | Quién la opera y qué hace | Lo que mostraba el 2026-11-27 |
|---|---|---|
| [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | Agregador comercial; un índice sobre nueve evaluaciones | Índice v5.0.2 con AA-Briefcase v1.1, AutomationBench-AA, Terminal-Bench 4.1, FrontierCode-AA 2.0, AA-Omniscience v1.1, GDP.pdf, HLE-Diamond, CritPt v2 y Terminal-Bench-Science 0.1. Primeros: Claude Fable 5.2 (Max) 65; Claude Fable 5.2 (Xhigh) 62; GPT-6.2 Astra (Max) 62. La página no trae fecha. |
| [Arena](https://arena.ai/leaderboard) | Comparaciones por pares votadas por personas; Bradley-Terry con control de estilo ([metodología](https://arena.ai/leaderboard/methodology)) | La portada mostró solo el Agent Arena Index: Claude Fable 5.2 (Max) 1.449; Claude Opus 5.5 (Max) 1.342; Gemini 4 Neon (xHigh) 1.331. El ranking de texto no se leyó. lmarena.ai redirige a arena.ai. |
| [Epoch AI Benchmarking Hub](https://epoch.ai/benchmarks) | Instituto de investigación; corre evaluaciones propias y recoge las oficiales | Base con 100 benchmarks, actualizada el 2026-11-27. Incluye GPQA Diamond. |
| HELM ([paper](https://arxiv.org/abs/2211.09110)) | Batería amplia con varias métricas por escenario | En el paper de 2022-23: 42 escenarios, 7 métricas, 30 modelos. El leaderboard vivo no se leyó. |

> [!NOTE]
> Sin fuente todavía: el ranking de texto actual de Arena, el leaderboard vivo de HELM y los puntajes
> recientes de Humanity's Last Exam y GPQA.
