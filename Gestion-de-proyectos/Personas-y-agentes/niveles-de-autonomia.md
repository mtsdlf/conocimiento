---
resumen: >-
  El nivel de autonomía de un agente es cuánto decide solo antes de que intervenga una persona, desde que la persona opera cada paso hasta que solo observa. Se elige por pieza de trabajo, separado de lo capaz que sea el agente, y choca con un límite humano: quien supervisa automatización tiende a confiar de más.
estado: borrador
estabilidad: semi
fuentes:
  - "Feng, McDonald y Zhang (2025), Levels of Autonomy for AI Agents, arXiv 2506.12469 (abstract y resumen del HTML): https://arxiv.org/abs/2506.12469 y https://arxiv.org/html/2506.12469"
  - "Parasuraman, Sheridan y Wickens (2000), A model for types and levels of human interaction with automation, IEEE Trans. SMC-A 30(3):286-297 (resumen, sin acceso al texto): https://dblp.uni-trier.de/rec/journals/tsmc/ParasuramanSW00.html"
  - "Parasuraman y Manzey (2010), Complacency and bias in human use of automation, Human Factors 52(3):381-410 (abstract): https://pubmed.ncbi.nlm.nih.gov/21077562/"
  - "Green (2022), The flaws of policies requiring human oversight of government algorithms, Computer Law & Security Review 45 (resumen): https://arxiv.org/abs/2109.05067"
  - "Anthropic (2026-02-18), Measuring AI agent autonomy in practice (resumen): https://www.anthropic.com/research/measuring-agent-autonomy"
  - "Mitchell, Ghosh, Luccioni y Pistilli (2025), arXiv 2502.02649 (abstract): https://arxiv.org/abs/2502.02649"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [autonomía de un agente, levels of autonomy, persona en el bucle, human in the loop, human on the loop, gestión por excepción, management by exception, sesgo de automatización, automation bias, complacencia]
creado: 2026-11-27
revisado:
---

# Niveles de autonomía

El nivel de autonomía de un agente es cuánto decide solo antes de que intervenga una persona, desde que la persona opera cada paso hasta que solo observa. Se elige por pieza de trabajo, separado de lo capaz que sea el agente, y choca con un límite humano: quien supervisa automatización tiende a confiar de más.

## Los cinco niveles según el papel de la persona

Feng, McDonald y Zhang (2025) definen cinco niveles por lo que hace la persona, no por lo que hace el agente:

| Nivel | Papel de la persona |
|---|---|
| Operador | Dirige cada paso; el agente ejecuta lo que se le pide |
| Colaborador | Trabaja junto al agente y se reparten el trabajo |
| Consultor | El agente lleva el trabajo y le consulta a la persona |
| Aprobador | La persona interviene solo cuando el agente "encounters a blocker" o pide aprobación |
| Observador | La persona mira; el nivel "does not require, and comes with no means for, user involvement" |

La idea central es que el nivel se diseña: tratan la autonomía como "a property that can also be designed independently of capability". Según esta base (inferencia de esa idea), un agente muy capaz puede trabajar como colaborador si la tarea es riesgosa. Proponen "autonomy certificates" que fijan el nivel máximo de cada agente. Es un marco conceptual, sin datos, y no se confirmó si tuvo revisión por pares.

Parasuraman, Sheridan y Wickens (2000) dieron la versión clásica desde los factores humanos. Según un resumen, separan cuatro etapas que se pueden automatizar (juntar información, analizarla, elegir qué hacer y hacerlo) y cada una tiene su propio grado. En un proyecto, eso permite que un agente analice y proponga con mucha autonomía y que ejecutar quede para una persona.

## Persona en el bucle y persona en el borde

Las dos expresiones más usadas son dos de esos niveles. Una persona "en el bucle" aprueba antes de que el trabajo siga: es el aprobador, con un punto de control obligado. Una persona "en el borde del bucle" vigila y puede intervenir, pero el trabajo no la espera: está entre aprobador y observador. La correspondencia es una lectura de esta base. Los [patrones de trabajo](patrones-de-trabajo.md) enlazan acá para esta parte.

La gestión por excepción de la gestión de proyectos equivale, según esta base, a lo mismo visto desde arriba: la persona se entera solo de lo que se sale de la tolerancia. Cómo se fijan esas tolerancias está en [problemas y escalamiento](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md).

> [!NOTE] Sin fuente todavía: una fuente primaria de la gestión por excepción; la equivalencia con el nivel de aprobador es de esta base.

## Quien supervisa confía de más

Subir de nivel tiene un costo humano medido. Parasuraman y Manzey (2010) revisaron estudios sobre personas que supervisan automatización. Según su abstract, la complacencia y el sesgo de automatización aparecen en novatos y en expertos, la práctica sola no los elimina y afectan también a equipos. El sesgo produce dos errores: no ver lo que la automatización no avisó (omisión) y seguir una recomendación equivocada (comisión).

Green (2022) lleva el argumento a las políticas. Según un resumen, revisó 41 políticas que exigen supervisión humana de algoritmos de gobierno. Concluye que "la gran mayoría de la investigación sugiere que las personas no pueden supervisar algoritmos de forma confiable" y que exigir supervisión da falsa seguridad. Su contexto son algoritmos que deciden sobre personas, no agentes en proyectos.

> [!IMPORTANT]
> **Supervisar sí cambia algo, según los datos de uso de Anthropic (2026).** En su agente de código, según un resumen, los usuarios nuevos (menos de 50 sesiones) dejan que el agente actúe sin aprobación alrededor del 20 % de las veces, y hacia las 750 sesiones, más de 40 %. Pero los experimentados interrumpen más: alrededor de 9 % de los turnos contra 5 % de los nuevos. Su lectura: "effective oversight doesn't require approving every action but being in a position to intervene when it matters". Son datos de un laboratorio sobre sus propios modelos, casi todo software, con puntajes de riesgo que generó el mismo modelo.
>
> **Supervisar no alcanza, según Parasuraman y Manzey y Green.** La persona que aprueba tiende a confiar de más y, según el abstract de Parasuraman y Manzey, la práctica sola no lo corrige. Designarla no prueba que controle.
>
> Lectura de esta base: las dos cosas pueden ser ciertas a la vez: la persona experimentada interviene más a menudo y aun así deja pasar errores que no espera. Para esta base, el nivel de aprobador se sostiene solo con una [aceptación con evidencia](../Seguimiento/aceptar-con-evidencia.md) que no dependa de la atención de la persona.

## Cómo se elige el nivel de cada pieza

No hay un estudio que diga qué nivel conviene en qué caso. Lo que sigue es criterio de esta base, armado con las fuentes de arriba:

- **Por consecuencia.** Mitchell y colegas sostienen, según su abstract, que "risks to people increase with the autonomy of a system". Lo que no se puede deshacer (pagar, publicar, borrar, comprometerse con un tercero) va con aprobador o menos. Lo reversible admite más, como en [decisiones reversibles](../../Liderazgo-y-direccion/Decidir/decisiones-reversibles.md).
- **Por verificabilidad.** Si el resultado se comprueba de forma automática, el agente puede llegar a observador en esa pieza. Si solo lo juzga una persona, no.
- **Por frontera.** Una tarea nueva, de la que no se sabe si cae dentro de la [frontera irregular](frontera-irregular.md), empieza en colaborador y sube cuando hay historia.
- **Por atención disponible.** Cada nivel bajo consume revisión. Si la [atención humana](la-atencion-humana-como-restriccion.md) ya es la restricción, bajar el nivel de todo frena el sistema entero.

El nivel también se baja. Un agente que falla en una pieza vuelve a colaborador en esa clase de piezas hasta que haya evidencia nueva. Cómo falla un agente que actúa solo y qué puede romper está en [fallas de agentes](../../IA/Agentes/fallas-de-agentes.md).

Ver también: [Personas y agentes](personas-y-agentes.md), [quién hace qué](quien-hace-que.md), [delegar a un agente](delegar-a-un-agente.md).
