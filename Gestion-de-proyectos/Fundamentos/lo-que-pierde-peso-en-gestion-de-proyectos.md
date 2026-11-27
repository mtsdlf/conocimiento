---
resumen: >-
  Lo que pierde peso en gestión de proyectos son las prácticas que este tema deja para aprender después o pone en segundo plano, cada una con quién lo dice, la evidencia en contra y un veredicto.
estado: borrador
estabilidad: semi
fuentes:
  - "Jørgensen, estimación por juicio experto y modelos formales (según un resumen): https://simula.no/research/estimation-software-development-work-effortevidence-expert-judgment-and-formal-models"
  - "Jørgensen (2007), revisión de estudios de estimación (según un resumen): https://web-backend.simula.no/sites/default/files/publications/Jorgensen.2007.2.pdf"
  - "Serrador y Pinto (2015), Does Agile work?, IJPM 33(5) (ficha de APM): https://apm.org.uk/media/r01fph3t/does-agile-work-a-quantitative-analysis-of-agile-project-success.pdf"
  - "Joseph y Marnewick (2018), Investing in project management certification, Information Technology and Management 19(1) (abstract): https://ideas.repec.org/a/spr/infotm/v19y2018i1d10.1007_s10799-017-0275-y.html"
  - "Aslam y Bilal (2021), certificación y desempeño (según un resumen; sin URL verificada)"
  - "Hobbs y Aubry, PMO (según un resumen): https://www.pmi.org/learning/library/project-management-offices-types-functions-2376"
  - "Estudio de dos años en 200 grandes organizaciones sobre uso de PMO (según un resumen): https://www.pmi.org/learning/library/project-management-office-strategic-goals-4122"
  - "PMI, The role of the PMO in achieving project success (según un resumen): https://www.pmi.org/learning/library/role-pmo-achieving-project-success-1002"
  - "Cox (2008), What's wrong with risk matrices?, Risk Analysis 28(2) (abstract): https://econpapers.repec.org/RePEc:wly:riskan:v:28:y:2008:i:2:p:497-512"
  - "RACI, visión general (según un resumen): https://www.wikipedia.org/wiki/RACI_matrix"
  - "Validación de diseño de una matriz RACI en una organización (póster, según un resumen): https://aisel.aisnet.org/isd2014/proceedings2026/transformation/11"
  - "TechTarget, RACI matrix for project management (practicante, según un resumen): https://www.techtarget.com/enterprise-software/tip/RACI-matrix-for-project-management-success-with-example"
  - "Parasuraman y Manzey (2010), Complacency and bias in human use of automation, Human Factors 52(3) (abstract): https://pubmed.ncbi.nlm.nih.gov/21077562/"
  - "Green (2022), The flaws of policies requiring human oversight of government algorithms (según un resumen): https://arxiv.org/abs/2109.05067"
  - "Earned schedule, crítica de Lipke al SPI (según un resumen): https://wikipedia.com/wiki/Earned_Schedule"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md, tesis 4 y 6"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md, sección 1"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md, sección B1"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md, sección 2"
aliases: [posición contraria en gestión de proyectos, qué dejar del PMBOK y de Scrum, prácticas de gestión en desuso, what to unlearn in project management]
creado: 2026-11-27
revisado:
---

# Lo que pierde peso en gestión de proyectos

Lo que pierde peso en gestión de proyectos son las prácticas que este tema deja para aprender después o pone en segundo plano, cada una con quién lo dice, la evidencia en contra y un veredicto.

"Pierde peso" quiere decir que conviene aprenderlo después, no que esté muerto: casi todo sigue sirviendo en algún contexto, y varias prácticas tienen estudios que dicen "sirven, con condiciones". Casi todo es criterio de esta base, sin un estudio que lo mida. No hay ninguno que pruebe que estas prácticas pierdan peso cuando ejecutan agentes de IA: es una proyección del tema. Lo propio del software (story points, Gitflow, cobertura, revisión línea por línea) está en [lo que pierde peso en desarrollo](../../Desarrollo/Fundamentos/lo-que-pierde-peso-en-desarrollo.md).

## Resumen por ítem

| Ítem | Quién lo dice | Evidencia en contra | Veredicto |
|---|---|---|---|
| Ceremonias ágiles completas | Criterio de la base | Las reuniones diarias sirven para coordinar | Pierde peso el rito; la coordinación queda |
| Reuniones de estado | Criterio de la base | Ningún estudio las mide como tales | Pierde peso; el estado se lee sin reunirse |
| Estimar en horas-persona | Criterio de la base | El juicio experto fue más exacto que los modelos en 10 de 16 estudios (según un resumen) | Pierde peso como unidad del plan |
| Gantt detallado y congelado | Criterio de la base | Planificar ayuda; nada mide el Gantt | Pierde peso el detalle fino a largo plazo |
| Certificación como garantía | Joseph y Marnewick (2018) | Aslam y Bilal (2021) encuentran un vínculo | No garantiza; sirve como vocabulario común |
| PMO como garantía | Estudio en 200 organizaciones; revisión de PMI | No se halló estudio causal en ninguna dirección | No garantiza; depende de qué hace |
| Matriz de probabilidad e impacto como única herramienta | Cox (2008) | Se usa mucho y es fácil de leer | Se usa con cuidado, explicando los juicios |
| RACI como garantía de roles claros | Criterio de la base | No hay estudio comparativo a favor ni en contra | Pierde peso como documento; queda la pregunta |
| SPI del valor ganado al final del proyecto | Lipke | El valor ganado sí sirve para costo | Pierde peso el SPI en el tramo final |
| Persona en el bucle como garantía de control | Parasuraman y Manzey; Green | Nada refuta que la responsabilidad quede en una persona | Designar a alguien no alcanza como control |

## Las ceremonias ágiles completas

Lo que pierde peso es la ceremonia como rito, no la coordinación. Los estudios sobre reuniones diarias las respaldan como coordinación y las contradicen como reporte de estado al jefe; las cifras y las fuentes están en [enfoque iterativo](../Enfoque/enfoque-iterativo.md).

## Las reuniones de estado

No hay estudio sobre reuniones de estado como tales: es un hueco. Lo más cercano son los estudios de reuniones diarias, donde el reporte al jefe es lo que más pesa en contra. Como criterio de esta base, el estado se publica para que lo lea quien decide, y la reunión se guarda para decidir algo. Está en [informar el estado](../Seguimiento/informar-el-estado.md); las reuniones en general, en [reuniones](../../Liderazgo-y-direccion/Ejecucion/reuniones.md).

## Estimar en horas-persona

Pierde peso la hora-persona como unidad del plan. Jørgensen encontró que el juicio experto fue más exacto que los modelos formales en 10 de 16 estudios, según un resumen, y que se mejora con datos históricos, listas de verificación y combinando estimaciones independientes. Eso no defiende ni ataca la unidad. Lo que la debilita es una inferencia de esta base: cuando parte del trabajo lo hace un agente, la hora de una persona deja de medir el esfuerzo, y el costo pasa a ser de revisión y de cómputo. La alternativa, por rangos y clase de referencia, está en [pronóstico](../Planificacion/pronostico.md) y [capacidad y costo](../Planificacion/capacidad-y-costo.md).

## El Gantt detallado y congelado

Serrador y Pinto (2015) no hallaron diferencia significativa en la planificación inicial entre proyectos ágiles y no ágiles, y sí que la planificación continua ayuda, según la ficha de APM. Eso apoya planificar, no detallar un cronograma a meses vista. No se encontró nada sobre el Gantt como tal. Lo que queda es saber qué espera a qué y cuál es la cadena que manda, en [dependencias y camino crítico](../Planificacion/dependencias-y-camino-critico.md).

## La certificación como garantía

Según su abstract, Joseph y Marnewick (2018) concluyen que "el desempeño de proyectos de TI sudafricanos no está influido por la certificación en gestión de proyectos". Aslam y Bilal (2021) hallan, según un resumen, un vínculo entre certificación y desempeño mediado por el profesionalismo, y su texto no se verificó. Casi todo lo publicado sale de PMI o de revistas cercanas, que vende las certificaciones. La certificación da un vocabulario común; no garantiza un resultado. Preparar certificaciones queda fuera del tema.

## La PMO como garantía

Un estudio de dos años en 200 grandes organizaciones halló que las de mucho uso de PMO tenían más costos de TI y no entregaban proyectos de mayor retorno, según un resumen. Una revisión de PMI dice que la literatura sobre el efecto de la PMO en el éxito "es en gran parte anecdótica". Hobbs y Aubry encuestaron 500 PMO y documentaron una gran variedad de formas, y la ficha no dice que prueben un efecto (el texto no se leyó). Qué gobierna un proyecto está en [gobierno del proyecto](../Gobierno-y-cierre/gobierno-del-proyecto.md) y [portafolio](../Gobierno-y-cierre/portafolio.md).

## La matriz de probabilidad e impacto

Cox (2008) dice en su abstract que hay poca investigación que muestre que las matrices de riesgo mejoren las decisiones, y les marca cuatro límites, entre ellos que pueden calificar más alto un riesgo cuantitativamente menor. Concluye que se usen con cuidado y explicando los juicios que contienen. La crítica ataca las escalas ordinales, no la idea de gestionar riesgos; está en [riesgo](../Incertidumbre-y-riesgo/riesgo.md).

## RACI como garantía de roles claros

No se halló evidencia comparativa de que una matriz RACI mejore los resultados: lo más cercano es una validación de diseño en una sola organización, sin grupo de comparación. Los practicantes advierten que la matriz se desactualiza. La pregunta que contesta (quién decide, quién ejecuta, quién verifica, quién responde) sigue siendo central, y más con agentes; está en [quién hace qué](../Personas-y-agentes/quien-hace-que.md).

## El SPI del valor ganado al final del proyecto

Al terminar un proyecto, el índice de desempeño del cronograma (SPI) vale 1 aunque se haya entregado tarde, porque el valor ganado converge al planificado. Lipke propuso medir en unidades de tiempo ("earned schedule"), según un resumen; no se encontró crítica independiente de su propuesta. El valor ganado para costo tiene evidencia propia, en [medir el avance](../Seguimiento/medir-el-avance.md).

## Una persona en el bucle como garantía de control

Pierde peso la idea de que alcanza con poner a una persona a aprobar lo que hace la automatización. La evidencia sobre el sesgo de automatización y sobre las políticas de supervisión humana está en [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md). Nada de eso refuta que la responsabilidad por el resultado quede en una persona con nombre: dice que nombrarla no alcanza como control, y que hace falta [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md).
