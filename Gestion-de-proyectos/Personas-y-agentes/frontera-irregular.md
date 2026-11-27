---
resumen: >-
  La frontera irregular es el borde, desparejo e invisible de antemano, entre las tareas que la IA hace bien y las que hace mal. Dentro de ella mejora el trabajo; fuera, lo empeora sin que la persona lo note, así que qué darle a un agente se decide probando y midiendo, no por intuición.
estado: vigente
estabilidad: estable
fuentes:
  - "Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon y Lakhani (2023), Navigating the Jagged Technological Frontier, HBS Working Paper 24-013 (texto del PDF: abstract, resultados y sección Centaur/Cyborg): https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf"
  - "Misma investigación en Organization Science, doi 10.1287/orsc.2025.21838 (no leída): https://pubsonline.informs.org/doi/full/10.1287/orsc.2025.21838"
  - "Brynjolfsson, Li y Raymond (2025), Generative AI at Work, QJE 140(2):889-942 (abstract): https://www.nber.org/papers/w31161"
  - "METR (2025-07-10), Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity, arXiv 2507.09089 (resumen): https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
  - "METR (2026-02-24), uplift update (leído entero según el informe de posición contraria): https://metr.org/blog/2026-02-24-uplift-update/"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [jagged frontier, frontera tecnológica irregular, qué tareas dar a un agente, centauros y cyborgs, uplift]
creado: 2026-11-27
revisado: 2026-11-27
---

# Frontera irregular

La frontera irregular es el borde, desparejo e invisible de antemano, entre las tareas que la IA hace bien y las que hace mal. Dentro de ella mejora el trabajo; fuera, lo empeora sin que la persona lo note, así que qué darle a un agente se decide probando y midiendo, no por intuición.

"Irregular" quiere decir que dos tareas que a una persona le parecen igual de difíciles pueden caer de lados distintos. No hay una regla del tipo "lo fácil adentro, lo difícil afuera".

## El experimento con 758 consultores

El término viene de Dell'Acqua y otros (2023). Su experimento preregistrado "involved 758 consultants comprising about 7% of the individual contributor-level consultants at the company". Los repartieron al azar en tres grupos: sin IA, con GPT-4 y con GPT-4 más un resumen de cómo escribirle.

**Dentro de la frontera** (18 tareas de consultoría), los consultores con IA "completed 12.2% more tasks on average, and completed tasks 25.1% more quickly", con "more than 40% higher quality compared to a control group". Los que estaban por debajo de la media mejoraron 43 % y los de arriba, 17 %.

**Fuera de la frontera** (una tarea que, según un resumen, se diseñó para que la IA fallara), los consultores con IA "were 19 percentage points less likely to produce correct solutions". El grupo sin IA acertó alrededor de 84,5 %, y los grupos con IA, 60 % y 70 %. La IA empeoró el resultado justo donde la persona no sabía que estaba afuera.

Hay una discrepancia en los resúmenes: una página de Harvard habla de "about 32 %" de mejora en calidad. El working paper dice "more than 40 %", y esa es la cifra que usa esta base. Los límites del estudio: una sola empresa, tareas de consultoría, un modelo de 2023 y una sola tarea fuera de la frontera. La versión publicada en Organization Science no se leyó y sus cifras podrían diferir.

## Centauros y cyborgs: dos formas de trabajar junto a la IA

El mismo estudio describe dos formas de trabajar con la IA. Los centauros reparten el trabajo: van "dividing and delegating their solution-creation activities to the AI or to themselves". Los cyborgs lo mezclan: van "completely integrating their task flow with the AI and continually interacting with the technology".

Para un proyecto, el centauro es el modelo de encargos separados de [delegar a un agente](delegar-a-un-agente.md). El cyborg se parece más al nivel de colaborador de los [niveles de autonomía](niveles-de-autonomia.md). La correspondencia es una lectura de esta base.

## Lo que midieron otros estudios: el signo depende de la tarea

> [!IMPORTANT]
> **Más rápido en atención al cliente (Brynjolfsson, Li y Raymond, 2025).** Según el abstract de la versión publicada, con 5.172 agentes de soporte, los menos experimentados ganaron en velocidad y calidad, y los más experimentados ganaron poco en velocidad y perdieron algo de calidad. Las cifras de 14 % promedio y 34 % para novatos son del working paper de 2023 y no se confirmaron en la versión publicada.
>
> **Más lento en código conocido (METR, 2025).** En un ensayo aleatorizado con 16 desarrolladores experimentados y 246 tareas de unas 2 horas en repositorios grandes que conocían, con IA tardaron 19 % más (intervalo de confianza de +2 % a +39 %). Esperaban ir 24 % más rápido y, al terminar, creían haber ganado alrededor de 20 %.
>
> **Quizá más rápido, con una señal que METR no da por buena (METR, 2026).** La actualización del 2026-02-24, con 57 desarrolladores, 143 repositorios y más de 800 tareas, estimó -18 % de tiempo para los 10 que repitieron (de -38 % a +9 %) y -4 % para los 47 nuevos (de -15 % a +9 %); negativo es más rápido. METR la llama "an unreliable signal": entre 30 % y 50 % de los desarrolladores no presentó tareas que no quería hacer sin IA, y el pago bajó de 150 a 50 dólares por hora. Los dos intervalos cruzan cero.
>
> **Lectura de esta base.** Los estudios no se contradicen si se lee la frontera: el efecto cambia de signo según la tarea, la persona y el modelo. Lo que más se sostiene es la brecha entre percepción y medición, aunque con una muestra chica: en el ensayo de 2025 (16 desarrolladores), quienes iban 19 % más lentos creían ir 20 % más rápido.

La misma disputa, contada desde el lado técnico y con otros estudios, está en [agentes](../../IA/Agentes/agentes.md).

## Cómo se encuentra la frontera en un trabajo propio

Si la frontera no se ve de antemano y la percepción engaña, solo queda medirla. Lo que sigue es criterio de esta base:

1. **Probá con una muestra chica.** Antes de dar una clase de tareas a un agente, hacé unas pocas con y sin agente y compará tiempo y resultado contra el criterio de terminado.
2. **Medí, no preguntes.** La impresión de quien trabajó con el agente no sirve como medida.
3. **Revisá más donde el error no se ve.** El estudio de Dell'Acqua muestra que fuera de la frontera los consultores con IA acertaron menos sin notarlo; que las respuestas "sigan pareciendo buenas" lo dice un resumen secundario, no el texto leído. Ahí va la [aceptación con evidencia](../Seguimiento/aceptar-con-evidencia.md) más estricta.
4. **Volvé a medir con cada modelo nuevo.** La frontera se mueve. El largo de tarea que completan los agentes se duplica en meses, según la ficha de [horizonte de tareas](horizonte-de-tareas.md).

El horizonte de tareas da una cota gruesa (qué largo de tarea es razonable intentar). La frontera irregular dice que, aun dentro de esa cota, hay tareas que fallan. Las dos se leen juntas.

## Fuera del software y la consultoría, casi no hay datos

Los experimentos con método son de consultoría, atención al cliente y programación. Para mudar una plataforma, organizar un evento o llevar una obra no se encontraron experimentos. Aplicar estos resultados a esos dominios es extrapolación.

Ver también: [Personas y agentes](personas-y-agentes.md), [capacidad y costo](../Planificacion/capacidad-y-costo.md).
