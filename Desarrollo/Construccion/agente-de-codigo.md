---
resumen: >-
  Un agente de código es un modelo de lenguaje que trabaja sobre un repositorio en un bucle: lee el
  código, edita archivos, corre comandos, mira el resultado y sigue hasta terminar la tarea o
  quedarse sin forma de avanzar.
estado: vigente
estabilidad: semi
fuentes:
  - "Anthropic, Best practices for Claude Code (leída 2026-11-27): https://code.claude.com/docs/en/best-practices"
  - "METR, Early-2025 AI experienced OS dev study (2025-07-10): https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
  - "Becker, Rush, Barnes y Rein (METR), arXiv 2507.09089: https://arxiv.org/abs/2507.09089"
  - "METR, Uplift update (2026-02-24): https://metr.org/blog/2026-02-24-uplift-update/"
  - "METR, Measuring AI ability to complete long tasks (2025-03-19): https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/"
  - "METR, Time Horizon 1.1 (2026-01-29): https://metr.org/blog/2026-1-29-time-horizon-1-1"
  - "Google Cloud, Announcing the 2025 DORA report: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report"
  - https://dora.dev/dora-report-2025/
  - "Peng, Kalliamvakou, Cihon y Demirer, arXiv 2302.06590: https://arxiv.org/abs/2302.06590"
  - "Paradis et al. (Google), arXiv 2410.12944: https://arxiv.org/abs/2410.12944"
  - "Cui, Demirer, Jaffe, Musolff, Peng y Salz, Management Science (SSRN 4945566): https://papers.ssrn.com/abstract=4945566"
  - "He et al. (CMU), arXiv 2511.04427: https://arxiv.org/abs/2511.04427"
  - "GitClear, AI Copilot Code Quality 2025: https://www.gitclear.com/ai_assistant_code_quality_2025_research"
  - "OpenAI, Why we no longer evaluate SWE-bench Verified (2026-02-23): https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"
  - "Liang, Garg y Moghaddam, The SWE-Bench Illusion, arXiv 2506.12286: https://arxiv.org/abs/2506.12286"
  - "Kent Beck, Augmented Coding: Beyond the Vibes: https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes"
  - "Thoughtworks Technology Radar: https://www.thoughtworks.com/en-cl/radar"
aliases: [coding agent, agente de programación, asistente de código, programación con IA, augmented coding, vibe coding]
creado: 2026-11-27
revisado: 2026-11-27
---

# Agente de código

Un agente de código es un modelo de lenguaje que trabaja sobre un repositorio en un bucle: lee el código, edita archivos, corre comandos, mira el resultado y sigue hasta terminar la tarea o quedarse sin forma de avanzar.

Es el caso de programación de lo que [Agente](../../IA/Agentes/agente.md), en IA, describe en general: un sistema en el que el modelo decide sus propios pasos. Dentro de [Construcción](construccion.md), consume el [contexto del repositorio](contexto-del-repositorio.md) y entrega un cambio que [Verificación](../Verificacion/verificacion.md) tiene que poder comprobar. Cómo funciona el modelo por dentro está en [LLM](../../IA/Modelos/modelo-base.md).

## El bucle y lo que lo cierra

El bucle es simple: el agente explora el código, planea, edita, corre algo y decide qué hacer con lo que vio. La secuencia explorar, planear, codear y commitear describe bien ese bucle, aunque la guía actual de Anthropic ya no la presenta como receta: dice que "your first plain prompt in a fresh session already does the right thing" y pone el trabajo de la persona en otro lado.

Lo que la persona aporta, según esa guía, es contar lo que el agente no ve, imponer las reglas sin excepción con mecanismos y, sobre todo, "give it a check to run". Sin una verificación que pueda correr, el agente solo puede afirmar con su palabra que terminó (inferencia de esta base). La guía pide evidencia (el comando y su salida) y ofrece varias formas de cerrar el bucle: pedir la verificación en el mismo encargo, impedir que la sesión termine hasta que pase el typecheck o hacer revisar el cambio por un subagente nuevo, con contexto limpio. Los nombres concretos de esos mecanismos están en la ficha [herramientas de agentes de código](herramientas-de-agentes-de-codigo.md).

## Dos maneras de trabajar con un agente

Kent Beck distingue, según el resumen leído, el [vibe coding](../Fundamentos/escuelas-de-desarrollo.md#cuánto-se-revisa-lo-que-escribe-el-modelo-las-posturas-sobre-ia), donde solo importa que el programa se comporte bien, del augmented coding, donde se sigue cuidando la complejidad y las pruebas, con [TDD](../Verificacion/tdd.md). Esta base distingue dos modos de trabajo. En el supervisado, la persona sigue al agente paso a paso y corrige sobre la marcha. En el delegado, la persona entrega una tarea con su criterio de terminado y revisa el resultado con evidencia. El modo delegado depende de que la tarea esté [bien partida](../Definicion/descomposicion-en-tareas.md) y tenga [criterios de aceptación](../Definicion/criterios-de-aceptacion.md) verificables.

> [!NOTE] Sin fuente todavía: no se encontró ningún estudio controlado sobre programar en pareja con un agente; lo de arriba es postura de practicantes.

La guía de Anthropic resuelve el trabajo en paralelo con una sesión por worktree de Git, cada una con su propio directorio de trabajo. Los worktrees son un pendiente de [Git](Git/git.md) en esta vertical.

## Cuánto acelera, según quién mida

La evidencia sobre productividad apunta en direcciones distintas porque mide cosas distintas.

| Estudio | Qué midió | Resultado |
|---|---|---|
| Peng et al., preprint | una tarea de laboratorio corta (un servidor HTTP en JavaScript) | según su resumen, el grupo con asistente "completed the task 55.8% faster" |
| Paradis et al. (Google), preprint | 96 ingenieros, herramientas internas de 2024 | según su resumen, alrededor de 21 % de ahorro de tiempo, con un intervalo de confianza amplio |
| Cui et al., Management Science | tres experimentos de campo, 4.867 desarrolladores | según el resumen del buscador, 26,08 % más tareas completadas, con más ganancia en los menos experimentados |
| METR 2025, ensayo aleatorizado | 16 desarrolladores experimentados, 246 issues reales en sus propios repositorios maduros | con IA tardaron 19 % más (IC +2 % a +39 %); habían pronosticado 24 % menos y después creían haber ido 20 % más rápido |

> [!IMPORTANT]
> El resultado de METR 2025 no es una cifra vigente. En febrero de 2026 METR repitió el estudio con 57 desarrolladores, 143 repositorios y más de 800 tareas, y advirtió que el diseño ya no mide bien: entre 30 % y 50 % de los participantes no presentó tareas que no quería hacer sin IA, y muchos no quisieron participar si no podían usarla. Concluye que los desarrolladores probablemente están "more sped up from AI tools now", pero que sus datos son "only very weak evidence for the size of this increase", y está rediseñando el estudio. Hoy no hay una cifra citable de cuánto acelera un agente en tareas reales.

El mismo estudio sugiere otra cosa, con la salvedad de sus 16 participantes: la percepción de velocidad no sirve como medida, porque quienes tardaron más creían haber ido más rápido.

DORA 2025 mira el sistema entero en lugar de la tarea. Sobre casi 5.000 profesionales, encuentra "a positive relationship between AI adoption on both software delivery throughput and product performance", y a la vez que la adopción "does continue to have a negative relationship with software delivery stability". Su explicación: "Without robust control systems, like strong automated testing, mature version control practices, and fast feedback loops, an increase in change volume leads to instability." DORA describe la IA como amplificador de lo que la organización ya hace bien o mal. Son correlaciones de encuesta, no ensayos. Las métricas que usa están en [métricas DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md).

## Qué pasa con el código que produce

Los estudios sobre la calidad del código generado son observacionales, salvo uno cuasi-experimental (He et al., MSR 2026, diferencias en diferencias), y ninguno se leyó completo. Según el resumen del buscador, ese estudio de CMU sobre 806 repositorios que adoptaron un editor con agente encontró de 3 a 5 veces más líneas agregadas el primer mes, un efecto que se disipa a los dos meses, y como cifras preliminares 30 % más advertencias de análisis estático y 41 % más complejidad; el detalle está en [deuda técnica](../Evolucion/deuda-tecnica.md#la-deuda-que-acumula-un-agente), junto con los datos de GitClear, que vende análisis de código y reporta (según notas secundarias) que 2024 fue el primer año en que se copió más código del que se movió. Para esta base, un pico de líneas que se disipa es una razón para no medir la productividad por líneas.

Thoughtworks agrega, según el resumen del buscador, el riesgo de la "cognitive debt": con más código generado "it's easier to adopt solutions without developing the mental models needed to understand how they work". Esta base infiere que eso pesa cuando el sistema [pasa a otro equipo](../Encargo/traspaso.md) o hay que entrar a él meses después.

## Por qué los puntajes de benchmark no miden capacidad

SWE-bench Verified fue durante años la referencia para comparar agentes. En febrero de 2026 OpenAI dejó de reportarlo: en 138 problemas auditados (los que o3 no resolvía de forma consistente), "59.4% of the 138 problems contained material issues in test design and/or problem description", y los modelos de frontera reproducían parches originales de algunas tareas. Liang et al. muestran, según su resumen, que los modelos identifican el archivo con la falla solo desde el texto del issue en hasta 76 % de los casos, contra 53 % en repositorios fuera del benchmark. OpenAI es parte interesada, porque vende modelos, pero su crítica coincide con la de otros investigadores. Esta base no cita puntajes de SWE-bench Verified como medida de capacidad.

Lo que sí crece de forma medible es la duración de las tareas que un agente completa. METR estimó en marzo de 2025 que la duración de tareas que los agentes de frontera terminan con 50 % de fiabilidad se venía "doubling approximately every 7 months for the last 6 years"; el propio METR aclara que esos datos fueron reemplazados por una versión posterior de su medición. La de enero de 2026 da unos 196 días de duplicación desde 2019 y 89 desde 2024, con las cifras por modelo al día en la ficha de [horizonte de tareas](../../Gestion-de-proyectos/Personas-y-agentes/horizonte-de-tareas.md).

## Hasta dónde se lo deja tocar

Un agente con permisos amplios hace cosas que nadie le pidió. Según el resumen del buscador, el Radar de Thoughtworks de abril de 2026 advierte que los agentes "find creative exfiltration paths, push to branches they shouldn't touch and erode approve/deny chokepoints", sin mala intención. La guía de Anthropic trata ese límite como una decisión explícita: qué archivos y comandos puede usar, dentro de qué sandbox y en qué rama puede empujar. El criterio de esta base es que el agente trabaje en su propia rama, sin credenciales de producción, y que lo que llega a la rama principal pase por [revisión de código](../Verificacion/revision-de-codigo.md) y por [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md).
