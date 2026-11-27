---
resumen: >-
  Pronosticar es decir cuándo termina un trabajo y cuánto cuesta como un rango con su probabilidad; se hace mirando cuánto llevaron trabajos parecidos ya terminados, porque mirar solo el plan propio produce un optimismo sistemático.
estado: borrador
estabilidad: semi
fuentes:
  - "Buehler, Griffin y Ross (1994), Exploring the planning fallacy, JPSP 67(3):366-381: https://bear.warrington.ufl.edu/brenner/mar7588/Papers/buehler-et-al-1994.pdf"
  - "Kahneman y Lovallo (1993), Timid choices and bold forecasts, Management Science 39(1):17-31 (según el abstract): https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.39.1.17"
  - "Lovallo, How to take the outside view, McKinsey (según resumen): https://www.mckinsey.com/business-functions/strategy-and-corporate-finance/our-insights/how-to-take-the-outside-view"
  - "Flyvbjerg (2008), Curbing optimism bias and strategic misrepresentation in planning, European Planning Studies 16(1):3-21 (abstract parcial): https://ideas.repec.org/a/taf/eurpls/v16y2008i1p3-21.html"
  - "Flyvbjerg, informe para el Edinburgh Tram Inquiry, pasos de la previsión por clase de referencia (según resumen del buscador): https://arxiv.org/pdf/1805.12106"
  - "Flyvbjerg (2014), What You Should Know About Megaprojects and Why, Project Management Journal 45(2): https://arxiv.org/pdf/1409.0003"
  - "Cantarelli, Davis, Pinto y Turner (2025), Reference class forecasting: promises, problems, and a research agenda (según la ficha y resúmenes del buscador): https://dspace.lib.cranfield.ac.uk/server/api/core/bitstreams/076d9c29-659d-4bfd-9b1b-e0019ea9ad20/content"
  - "Themsen (2019), proyecto ferroviario danés (según resumen): https://law-journals-books.vlex.com/vid/the-processes-of-public-855605613"
  - "Vacanti, When Will It Be Done? (2018) (descripción y títulos de capítulos): https://leanpub.com/whenwillitbedone"
  - "Scrum Alliance, Achieving predictable delivery (según resumen): https://resources.scrumalliance.org/Article/achieving-predictable-delivery"
  - "Nationwide Technology, Story pointless, parte 2 (según resumen): https://medium.com/nationwide-technology/story-pointless-part-2-of-3-57db27a48a58"
  - "Jørgensen, estimación de esfuerzo por juicio experto y modelos formales (según resumen): https://simula.no/research/estimation-software-development-work-effortevidence-expert-judgment-and-formal-models"
  - "Becker et al. (METR) (2025), ensayo aleatorizado con desarrolladores, arXiv 2507.09089 (según el abstract): https://arxiv.org/abs/2507.09089"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [forecast, forecasting, previsión, falacia de la planificación, planning fallacy, clase de referencia, reference class forecasting, visión externa, outside view, pronóstico probabilístico, probabilistic forecasting]
creado: 2026-11-27
revisado:
---

# Pronóstico

Pronosticar es decir cuándo termina un trabajo y cuánto cuesta como un rango con su probabilidad; se hace mirando cuánto llevaron trabajos parecidos ya terminados, porque mirar solo el plan propio produce un optimismo sistemático.

El pronóstico toma las piezas de la [descomposición del trabajo](descomposicion-del-trabajo.md), el orden de las [dependencias](dependencias-y-camino-critico.md) y el ritmo que da la [capacidad](capacidad-y-costo.md). Se actualiza con lo que mide el [seguimiento](../Seguimiento/medir-el-avance.md), y la distancia entre el pronóstico y el compromiso es lo que cubren los [márgenes](../Incertidumbre-y-riesgo/margenes.md). Ningún estándar lo trata como un tema propio: la literatura sale de la psicología de la decisión y de los megaproyectos.

## La falacia de la planificación

La gente subestima cuánto le van a llevar sus propias tareas. En el estudio 1 de Buehler, Griffin y Ross (1994), estudiantes que preparaban su tesis de grado pronosticaron en promedio 33,9 días y tardaron 55,5. "Fewer than one third of the respondents (29.7%) finished in the time they reported as their most accurate prediction." Con su propio escenario pesimista, solo el 48,7 % terminó a tiempo; con el optimista, de 21,4 días en promedio, el 10,8 %.

El mecanismo, según el mismo trabajo, es que quien planifica se concentra en escenarios futuros y no en cuánto le llevó lo parecido. En el estudio 4, "the optimistic bias was eliminated for Ss instructed to connect relevant past experiences with their predictions". En el estudio 5, los observadores sobrestimaron los tiempos de los demás: lo que sugiere, según esta base, que el sesgo es de quien pronostica su propio trabajo. Los autores citan la Ópera de Sídney, que en 1957 se estimó en US$ 7 millones, con la obra terminada a principios de 1963, y se inauguró en 1973 a un costo de US$ 102 millones.

La falacia es un caso de [sobreconfianza](../../Psicologia/Juicio-y-decision/sobreconfianza.md), y ahí está su lugar entre los sesgos de juicio. Una lectura de esta base, sin fuente: en un proyecto el error se acumula, porque cada pieza optimista suma al plazo total.

## La visión externa y la clase de referencia

La corrección es mirar el proyecto desde afuera. Kahneman y Lovallo (1993) atribuyen el optimismo, según el abstract, a tratar cada decisión como un caso único y desatender las estadísticas del pasado. Según Lovallo (McKinsey, en un resumen), él acuñó hacia 1993 los términos visión interna, para mirar el plan propio, y visión externa, para mirar la distribución de casos parecidos.

El pronóstico por clase de referencia lleva la visión externa a un método. Estos pasos los ordena esta base a partir de la descripción de Flyvbjerg; el ajuste del tercero aparece en el resumen de su informe para el tranvía de Edimburgo:

1. Elegí una clase de proyectos terminados parecidos al tuyo.
2. Armá la distribución de lo que pasó en esa clase: cuánto se desviaron del plazo o del costo previstos.
3. Ubicá tu proyecto en esa distribución y ajustalo si es más o menos riesgoso que la clase.
4. Decidí con qué probabilidad querés cumplir y tomá el percentil que corresponde.

Según el abstract de Flyvbjerg (2008), la primera aplicación práctica fue a costos de transporte en el Reino Unido, con casos como el tranvía de Edimburgo y Crossrail, de £ 15.000 millones. Flyvbjerg (2014) la menciona como remedio institucional. Los datos de desvío que la justifican están en [por qué fallan los proyectos](../Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md).

> [!IMPORTANT]
> Que la clase de referencia mejore el pronóstico está en disputa.
> - **A favor**: según resúmenes del buscador, en un trabajo de Park sobre 107 proyectos el sobrecosto medio bajó de 38 % a 5 % al introducirla, y en Batselier y Vanhoucke (Project Management Journal) fue el mejor método con datos reales.
> - **En contra**: en un megaproyecto ferroviario danés no llevó a estimaciones de costo más exactas (Themsen 2019, según un resumen). El mismo resumen sobre Park agrega que Estados Unidos quedó 17 % por debajo de su probabilidad objetivo de terminar en presupuesto. Elegir la clase es en sí un problema: dos partes pueden elegir clases distintas y llegar a números distintos.
> - **Estado**: Cantarelli, Davis, Pinto y Turner (2025) dejan abiertas, según su ficha, preguntas de validez, aplicabilidad y límites del método. Lo verificado es la propuesta y su aplicación, no una comparación con grupo de control. Los datos de base son de infraestructura grande; usarla en proyectos chicos es una extrapolación.

## Rangos, percentiles y el ritmo medido

Un pronóstico útil es un rango con probabilidades, no un promedio. Vacanti, practicante, lo resume en dos títulos de capítulo de su libro: "Never Communicate a Forecast in Terms of an Average" y "Percentiles Are Forecasts!". Decir "con 85 % de probabilidad termina antes del 20 de marzo" deja a quien decide elegir cuánto riesgo toma.

Cuando el trabajo ya está en marcha, la postura de Vacanti es pronosticar con el rendimiento propio: cuántas piezas se terminan por semana. Una simulación de Monte Carlo sobre ese rendimiento da la distribución de fechas. Según una guía de practicantes, alcanzan 10 a 20 mediciones para empezar; otra advierte que la simulación se degrada si el rendimiento es casi siempre cero. Ningún estudio con revisión por pares verificado valida el método frente a otros: es postura de practicantes. Los detalles para software, incluido el debate de no estimar, están en [estimación](../../Desarrollo/Encargo/estimacion.md).

Estimar pieza por pieza en horas-persona es lo que [pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md), con evidencia débil. Según un resumen de los trabajos de Jørgensen, en 10 de 16 estudios el juicio experto fue más exacto que los modelos formales, y mejora con datos históricos, listas de verificación y la combinación de estimaciones independientes. La lectura de esta base es que el juicio funciona mejor cuando incorpora la visión externa; ninguna de las fuentes lo dice así.

## Pronosticar cuando ejecutan agentes

Con agentes, la intuición de cuánto rinde el trabajo también falla, y falla hacia el optimismo. En el ensayo aleatorizado de METR de 2025, con 16 desarrolladores y 246 tareas, permitir IA "increased task completion time by 19%", según el abstract. Los desarrolladores esperaban una reducción de 24 % antes y estimaron 20 % después; economistas predijeron 39 % y expertos en aprendizaje automático, 38 %. El estudio, su actualización de 2026 y lo que dicen sobre cuánto rinde un agente están en [frontera irregular](../Personas-y-agentes/frontera-irregular.md).

La lectura de esta base es que se pronostica con datos del propio sistema y no con la intuición: rendimiento histórico de piezas aceptadas, tasa de retrabajo y tiempo de espera en la revisión. No hay base humana en horas-persona para lo que hace un agente. Lo más cercano es el largo de tarea que completan los agentes hoy, en la ficha de [horizonte de tareas](../Personas-y-agentes/horizonte-de-tareas.md), medido en software y con validez externa limitada según sus autores. Cuando la revisión humana es la restricción, el pronóstico depende más de esa cola que de la velocidad del agente ([trabajo en curso y colas](../Seguimiento/trabajo-en-curso-y-colas.md)).

Al arrancar, todavía no hay rendimiento propio. La salida que propone esta base, sin fuente que la haya medido, es correr primero una tanda chica de piezas reales, como la muestra que describe [frontera irregular](../Personas-y-agentes/frontera-irregular.md), y dar el primer pronóstico como un rango ancho que se angosta cuando entran las semanas medidas. Ese primer rango se informa como provisorio, con la fecha en que se va a rehacer.

El recurso canónico es Buehler, Griffin y Ross (1994): leer el estudio 1, con su tabla 1, y el estudio 4. Fijarse en que la mejora viene de forzar la conexión con experiencias pasadas, es decir, de la visión externa.
