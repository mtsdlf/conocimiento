---
resumen: >-
  Cuando los agentes producen más rápido de lo que las personas revisan, la atención de quien revisa pasa a ser la restricción del sistema: fija cuánto trabajo termina de verdad. Es una síntesis de esta base (Teoría de Restricciones, costo del cambio de tarea y datos de revisión de agentes) sin un estudio que la junte.
estado: vigente
estabilidad: semi
fuentes:
  - "Goldratt (1984), The Goal, los cinco pasos de enfoque (según un resumen; libro no consultado): https://www.ebsco.com/research-starters/business-and-management/theory-constraints-toc"
  - "Leroy (2009), Why is it so hard to do my work?, OBHDP 109(2):168-181 (resumen): https://econpapers.repec.org/RePEc:eee:jobhdp:v:109:y:2009:i:2:p:168-181"
  - "Mark, Gudith y Klocke (2008), The cost of interrupted work, CHI '08, pp. 107-110 (resumen): https://www.ics.uci.edu/~gmark/chi08-mark.pdf"
  - "Parasuraman y Manzey (2010), Human Factors 52(3) (abstract): https://pubmed.ncbi.nlm.nih.gov/21077562/"
  - "Faros AI, AI Productivity Paradox Report 2025, informe de un vendedor (resumen): https://www.faros.ai/blog/ai-productivity-paradox-report-2025"
  - "DORA (2025), State of AI-assisted Software Development (resumen; el PDF no se leyó): https://dora.dev/dora-report-2025/"
  - "Estudios sobre el conjunto AIDev de PRs de agentes, arXiv, sin revisión confirmada (resumen): https://arxiv.org/html/2601.00753v2"
  - "Revisión sobre fatiga de alertas clínicas, JMIR Med Inform (2020) (resumen): https://medinform.jmir.org/2020/7/e15653/"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
aliases: [cuello de botella de la revisión, review bottleneck, capacidad de revisión, atención como restricción, fatiga de revisión]
creado: 2026-11-27
revisado: 2026-11-27
---

# La atención humana como restricción

Cuando los agentes producen más rápido de lo que las personas revisan, la atención de quien revisa pasa a ser la restricción del sistema: fija cuánto trabajo termina de verdad. Es una síntesis de esta base (Teoría de Restricciones, costo del cambio de tarea y datos de revisión de agentes) sin un estudio que la junte.

Las piezas existen por separado. La Teoría de Restricciones explica qué hacer con un cuello de botella. La psicología del trabajo mide lo que cuesta saltar de una tarea a otra. Y hay datos, sobre todo de software, de que la revisión crece cuando entran agentes. Juntarlas es lectura de esta base.

## Por qué el cuello de botella se corre a la revisión

En un sistema, lo que sale por unidad de tiempo lo fija el paso más lento. Si un agente produce en minutos lo que una persona tarda una hora en revisar, agregar agentes no hace terminar más trabajo: hace crecer la cola frente a quien revisa. El trabajo producido y no revisado no está hecho; es [trabajo en curso](../Seguimiento/trabajo-en-curso-y-colas.md) que espera.

Los datos que hay van en esa dirección, todos de software. Un informe de Faros AI, que vende herramientas de medición, dice según un resumen que con alta adopción de IA los equipos hicieron 21 % más tareas e integraron 98 % más cambios, pero el tiempo de revisión subió 91 % y el tamaño medio de cada cambio, 154 %. Según el mismo resumen, las métricas de entrega de la organización no mejoraron. Es telemetría de un vendedor, sin revisión por pares.

DORA 2025, una encuesta a unos 5.000 profesionales, asocia la adopción de IA con más rendimiento y también con más inestabilidad en la entrega, según un resumen; alrededor de 30 % confía poco o nada en el código generado. Las [métricas DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md) se explican en su tema.

## Lo que cuesta revisar a saltos

Revisar trabajo de agentes suele ser revisar a saltos: llega un resultado, se interrumpe otra cosa, se vuelve. Eso tiene costo medido.

- **Residuo de atención (Leroy, 2009).** Según un resumen, en dos experimentos la gente tuvo dificultad para dejar una tarea sin terminar, y su desempeño en la siguiente bajó.
- **Interrupciones (Mark, Gudith y Klocke, 2008).** En laboratorio, quienes fueron interrumpidos terminaron más rápido y con calidad similar, pero con más estrés, frustración y esfuerzo. El costo medido es carga, no tiempo.
- **Confianza de más.** Quien revisa automatización tiende a aprobar lo que no ve mal, según Parasuraman y Manzey; está en [niveles de autonomía](niveles-de-autonomia.md).
- **Fatiga de alertas, como analogía.** En medicina, una revisión de 23 artículos encontró tasas medias de alertas descartadas de 46,2 % a 96,2 %. Es una analogía clínica, no un estudio de revisión de agentes; la lectura de que muestra lo que pasa cuando llegan más avisos de los que una persona puede atender es de esta base.

Una cola de revisión larga demora el trabajo y, según esta base, también bajaría la calidad de cada revisión. Ese segundo efecto es inferencia de esta base: ningún estudio consultado lo midió en revisión de agentes.

## Los cinco pasos de Goldratt aplicados a la revisión

Goldratt propone, según un resumen de *The Goal*, cinco pasos: identificar la restricción, explotarla, subordinar el resto a ella, elevarla y volver a empezar. Aplicados a la revisión humana son una lectura de esta base:

1. **Identificar.** Medí dónde espera el trabajo. Si la cola más larga está frente a una persona que revisa, esa es la restricción.
2. **Explotar.** Que la atención de quien revisa no se gaste en lo que una máquina puede comprobar. Pruebas automáticas, otro agente que revisa y un [criterio de terminado](delegar-a-un-agente.md) comprobable filtran antes. La persona mira lo que solo una persona puede juzgar.
3. **Subordinar.** No produzcas más de lo que se puede revisar. Limitá cuántas piezas de agentes esperan revisión, como en [flujo continuo](../Enfoque/flujo-continuo.md), y achicá cada pieza (supuesto de esta base: un cambio chico se revisa mejor que uno grande; lo que midió Faros es que el tamaño del cambio creció junto con el tiempo de revisión).
4. **Elevar.** Recién después, sumá capacidad de revisión: otra persona, o subir el [nivel de autonomía](niveles-de-autonomia.md) en las piezas que ya mostraron ser confiables.
5. **Volver a empezar.** Cuando la revisión deja de ser el cuello, otro paso lo es; cuál, esta base lo supone (por ejemplo, especificar el trabajo) y no está medido.

## Revisar por riesgo y no todo igual

No todo lo que produce un agente merece la misma atención. En los estudios sobre el conjunto AIDev de cambios propuestos por agentes en repositorios públicos, según un resumen, un presupuesto de revisión de 20 % alcanzó para capturar 69 % de los cambios de alto esfuerzo. El mismo trabajo encontró 3,8 % de cambios sin respuesta humana tras más de 14 días, sobre 33.707. Las cifras de esos estudios salen de subconjuntos distintos y no se comparan entre sí.

La lectura para un proyecto: ordenar la revisión por consecuencia (lo que no se puede deshacer primero), revisar en bloques fijos del día en lugar de a cada aviso, y medir la cola de revisión como se mide cualquier otra. La capacidad de revisión se planifica junto con la de producción en [capacidad y costo](../Planificacion/capacidad-y-costo.md).

> [!NOTE] Sin fuente todavía: un estudio que junte Teoría de Restricciones, cambio de contexto y revisión de agentes; datos de carga de revisión fuera del software; el texto original de Goldratt.

Ver también: [Personas y agentes](personas-y-agentes.md), [patrones de trabajo](patrones-de-trabajo.md), [portafolio](../Gobierno-y-cierre/portafolio.md).
