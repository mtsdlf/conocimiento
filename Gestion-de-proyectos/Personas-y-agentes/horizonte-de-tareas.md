---
resumen: >-
  Los horizontes de tarea que METR midió para cada modelo: el largo de las tareas, en tiempo de una persona, que un agente completa con 50 % y con 80 % de éxito, copiados del archivo de datos de METR el 2026-11-27.
estado: vigente
estabilidad: volatil
fuentes:
  - "METR, página de horizontes de tiempo (última actualización 2026-09-08; ya no se actualiza): https://metr.org/time-horizons/"
  - "METR, archivo de datos METR-Horizon-v1.1, copiado el 2026-11-27: https://metr.org/assets/benchmark_results_1_1.yaml"
  - "METR (2026-01-29), Time Horizon 1.1 (resumen): https://metr.org/blog/2026-1-29-time-horizon-1-1/"
  - "Kwa et al., Measuring AI Ability to Complete Long Software Tasks, arXiv 2503.14499 (abstract): https://arxiv.org/abs/2503.14499"
  - "METR (2025-07-14), How Does Time Horizon Vary Across Domains? (resumen): https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains"
  - "The Decoder, sobre la evaluación de METR de Claude Mythos Preview (prensa, no verificado contra METR): https://the-decoder.com/metr-says-it-can-barely-measure-claude-mythos-palo-alto-networks-warns-of-autonomous-ai-attackers/"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
aliases: [time horizon, horizonte temporal, 50% time horizon, largo de tarea de un agente, METR]
creado: 2026-11-27
revisado: 2026-11-27
---

# Horizonte de tareas

Los horizontes de tarea que METR midió para cada modelo: el largo de las tareas, en tiempo de una persona, que un agente completa con 50 % y con 80 % de éxito, copiados del archivo de datos de METR el 2026-11-27.

Da una cota para decidir qué darle a un agente; el criterio para decidirlo está en [frontera irregular](frontera-irregular.md) y en [delegar a un agente](delegar-a-un-agente.md). La medición como benchmark, con su validez, está en [benchmarks de agentes](../../IA/Agentes/benchmarks-de-agentes.md).

## Qué mide y qué no

El horizonte al 50 % es el tiempo que le lleva a una persona una tarea que el modelo completa la mitad de las veces. No es cuánto trabaja el agente solo ni con qué fiabilidad. Para un encargo que tiene que salir bien casi siempre importa el horizonte al 80 %, que en la tabla es entre 4 y 10 veces más corto (inferencia de la base a partir de la definición y de los valores).

Las tareas son de ingeniería de software, investigación en aprendizaje automático y ciberseguridad. Según METR, en su estudio por dominios de 2025, el uso agéntico de una computadora (navegar, operar programas) tiene horizontes de 40 a 100 veces más cortos que el software. METR admite que trabajos como la gestión o la enfermería casi no están representados. Para un proyecto fuera del software, estos valores son, por inferencia de esta base, una cota de arriba y no una estimación.

## Valores por modelo

Fuente viva: [metr.org/time-horizons](https://metr.org/time-horizons/), que se actualizó por última vez el 2026-09-08 y dice "This page is no longer actively updated". Copiado del archivo [benchmark_results_1_1.yaml](https://metr.org/assets/benchmark_results_1_1.yaml) el 2026-11-27. Los valores están en minutos de trabajo humano, redondeados a un decimal desde el archivo, con su intervalo de confianza entre paréntesis.

| Modelo | Fecha de salida | Horizonte al 50 % | Horizonte al 80 % |
|---|---|---|---|
| Claude 3.7 Sonnet | 2025-02-24 | 60,4 (33,0 a 104,2) | 12,1 (4,6 a 28,9) |
| o3 | 2025-04-16 | 119,7 (74,6 a 190,9) | 30,0 (15,1 a 57,8) |
| GPT-5 | 2025-08-07 | 203,0 (112,6 a 405,6) | 38,3 (19,2 a 70,1) |
| Gemini 3 Pro | 2025-11-18 | 224,3 (139,6 a 379,2) | 54,1 (25,7 a 103,3) |
| Claude Opus 4.5 | 2025-11-24 | 293,0 (161,7 a 623,7) | 49,4 (20,7 a 104,6) |
| GPT-5.2 | 2025-12-11 | 352,2 (198,1 a 815,2) | 66,0 (31,7 a 131,7) |
| GPT-5.3 Codex | 2026-02-05 | 349,5 (194,9 a 816,4) | 54,7 (22,4 a 122,1) |
| Claude Opus 4.6 | 2026-02-05 | 718,8 (316,7 a 3.633,8) | 69,9 (27,0 a 170,4) |
| Gemini 3.1 Pro | 2026-02-19 | 384,1 (233,5 a 694,8) | 89,8 (52,0 a 158,6) |
| GPT-5.4 | 2026-03-05 | 341,7 (186,6 a 768,8) | 53,9 (24,0 a 108,7) |
| Claude Mythos Preview (versión temprana) | 2026-04-07 | 1.044,8 (508,9 a 3.304,3) | 185,9 (97,3 a 398,5) |

El tiempo de duplicación del horizonte al 50 %, en el mismo archivo, es de 128,7 días desde 2023 (de 104,4 a 158,0) y de 187,8 días tomando toda la serie. El cálculo excluye los modelos con horizonte central de más de 16 horas.

## Cautelas para leer la tabla

- **Arriba de 16 horas no se puede medir bien.** La página de METR dice: "Measurements above 16 hrs are unreliable with our current task suite". El valor de Claude Mythos Preview cae ahí. Según la prensa, METR estimó para ese modelo "at least 16 hours", con un intervalo de 8,5 a 55 horas; eso no se verificó contra METR.
- **Los intervalos son muy anchos.** En el post de enero de 2026, METR advierte: "These confidence intervals are still very wide". Solo 31 de sus 228 tareas le llevan a una persona 8 horas o más, y solo 5 de esas tienen medición humana.
- **Los valores cambian entre publicaciones.** El post de enero de 2026 daba 320 minutos para Claude Opus 4.5 (de 170 a 729) y una duplicación de 130,8 días desde 2023. El archivo copiado da 293,0 minutos y 128,7 días. La tabla usa el archivo.
- **El archivo no dice la unidad.** Se leyó como minutos porque así reporta METR los mismos modelos en sus posts.

## La tendencia en el tiempo

El artículo original de METR (Kwa et al., 2025) dio unos 50 minutos para Claude 3.7 Sonnet y una duplicación de alrededor de 7 meses desde 2019, quizá acelerada en 2024. Con la versión 1.1 de las tareas, el mismo modelo da 60,4 minutos. La lectura de esta base: cualquier cifra de esta ficha envejece en meses; re-verificarla cada tres es una regla de esta base, no de METR.

Ver también: [Personas y agentes](personas-y-agentes.md), [capacidad y costo](../Planificacion/capacidad-y-costo.md), [descomposición en tareas](../../Desarrollo/Definicion/descomposicion-en-tareas.md).
