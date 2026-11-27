---
resumen: >-
  Medir el avance es saber cuánto falta con datos de lo que ya se terminó. Hay dos familias de medidas que no se mezclan: las de flujo (tiempo de entrega, rendimiento, flujo acumulado), que no necesitan un plan fijo, y el valor ganado, que compara contra una línea base de alcance.
estado: borrador
estabilidad: semi
fuentes:
  - "Christensen y Templin (2002), EAC Evaluation Methods: Do They Still Work?, Acquisition Review Quarterly, primavera 2002, pp. 105-116 (leído entero): https://webharvest.gov/peth04/20041015060742/http:/www.dau.mil/pubs/arq/2002arq/ChrisSP2.pdf"
  - "Estudio de estabilidad de CPI y SPI(t) en 9 proyectos, Journal of Modern Project Management (2016) (leído en parte; autoría no verificada): https://discovery.ucl.ac.uk/1506314/1/De-Koning_Stability_earned_value_management_VoR.pdf"
  - "Earned schedule de Lipke (según un resumen secundario; los originales no se leyeron): https://wikipedia.com/wiki/Earned_Schedule"
  - "ANSI/EIA-748, estándar de sistemas de valor ganado (ficha de venta; texto no leído): https://saemobilus.sae.org/standards/eia748e-earned-value-management-systems"
  - "Vacanti, Actionable Agile Metrics for Predictability (según una reseña): https://www.thoughtworks.com/en-au/insights/blog/book-review-actionable-agile-metrics-predictability"
  - "Vacanti, The Kanban Guide (2020) (según un resumen del buscador): https://kanbanguides.org/the-kanban-guide/2020.7"
  - "Scrum.org, flujo acumulado (según un resumen del buscador): https://www.scrum.org/resources/blog/getting-85-agile-metrics-actionableagile-part-2"
  - "Ley de Campbell y ley de Goodhart (según un resumen secundario): https://en.wikipedia.org/wiki/Campbell%27s_law"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md"
aliases: [medición del avance, progress measurement, métricas de flujo, flow metrics, valor ganado, earned value, EVM, CPI, SPI, lead time, tiempo de entrega, throughput, rendimiento, flujo acumulado, cumulative flow diagram, CFD]
creado: 2026-11-27
revisado:
---

# Medir el avance

Medir el avance es saber cuánto falta con datos de lo que ya se terminó. Hay dos familias de medidas que no se mezclan: las de flujo (tiempo de entrega, rendimiento, flujo acumulado), que no necesitan un plan fijo, y el valor ganado, que compara contra una línea base de alcance.

La pregunta que se contesta es siempre la misma: si seguimos así, ¿cuándo y a qué costo terminamos? La respuesta alimenta el [pronóstico](../Planificacion/pronostico.md). Lo que cambia entre familias es contra qué se compara.

## Dos familias que presuponen proyectos distintos

| | Medidas de flujo | Valor ganado |
|---|---|---|
| Compara contra | lo que salió en el pasado reciente | una línea base de alcance, plazo y costo |
| Medidas típicas | tiempo de entrega, rendimiento, edad del trabajo en curso, flujo acumulado | valor planificado, valor ganado, costo real, CPI y SPI |
| Supone | que el trabajo entra y sale, aunque el alcance cambie | que el alcance quedó fijo y se puede valuar por partes |
| Sirve en | [flujo continuo](../Enfoque/flujo-continuo.md) y [enfoque iterativo](../Enfoque/enfoque-iterativo.md) | [enfoque predictivo](../Enfoque/enfoque-predictivo.md) con contratos grandes |
| Tradición | teoría de colas y Kanban | defensa y construcción en Estados Unidos |

En lo que se leyó, las dos tradiciones no se citan entre sí (observación de la investigación, no de una fuente). Inferencia de la base: un proyecto puede usar las dos: valor ganado para el contrato con alcance fijo y medidas de flujo para el trabajo que entra por pedidos. Lo que no tiene sentido es calcular un CPI sobre un alcance que se reprioriza cada semana, porque no hay línea base contra la cual ganar valor.

## Las medidas de flujo

Las medidas de flujo salen de contar piezas. El tiempo de entrega es cuánto tarda una pieza desde que se acepta hasta que se termina. El rendimiento es cuántas piezas se terminan por semana. La edad del trabajo en curso es cuánto lleva abierta cada pieza que todavía no salió. La guía de Kanban de Vacanti lista como medidas básicas el trabajo en curso, el rendimiento, el tiempo de ciclo y la edad del trabajo en curso, según un resumen; el listado exacto no se verificó, y ahí se habla de tiempo de ciclo y no de tiempo de entrega. Se relacionan por la ley de Little, explicada en [trabajo en curso y colas](trabajo-en-curso-y-colas.md).

El diagrama de flujo acumulado apila, en el tiempo, cuántas piezas hay en cada etapa. Según un resumen de un practicante, la distancia horizontal entre la banda de llegada y la de salida aproxima el tiempo de entrega, y una banda que se ensancha indica trabajo en curso que crece. Un libro de esta familia es el de Vacanti, también practicante, y aquí se conoce solo por una reseña.

> [!NOTE] Sin fuente todavía: evidencia primaria sobre curvas de quemado (burn-up y burn-down) y sobre si las medidas de flujo pronostican mejor que otras en proyectos reales.

## El valor ganado y la estabilidad del CPI

El valor ganado compara tres montos en una misma fecha: lo que se planeó gastar en lo planeado (valor planificado), el presupuesto de lo que efectivamente se terminó (valor ganado) y lo que se gastó (costo real). De ahí salen el índice de costo (CPI, valor ganado sobre costo real) y el de plazo (SPI, valor ganado sobre valor planificado). Un estándar estadounidense, ANSI/EIA-748, define 32 guías para estos sistemas (según su ficha de venta).

Una regla clásica es que el CPI se estabiliza temprano. Christensen y Templin (2002) la pusieron a prueba sobre 240 contratos de adquisición de defensa. La regla del Departamento de Defensa decía que las varianzas de costo "tienden a empeorar a partir del 20 por ciento de avance", con tres corolarios: la varianza final será peor que la del 20 %; el CPI acumulado no cambiará más de 0,10 respecto del valor al 20 % y casi siempre empeora; y el costo final calculado con ese CPI es una cota inferior razonable.

En los 147 contratos anteriores a la cancelación del avión A-12 (enero de 1991), las reglas se confirmaron: CPI medio de 0,996 al 20 % y una diferencia de -0,045 entre el final y el 20 %, significativa. En los contratos de los años noventa, según el abstract, "the mean cost performance... did not worsen significantly from the 20 percent completion point", y los autores especulan que las reformas de adquisición lo mejoraron. Pero la tabla en dólares del mismo artículo sí muestra empeoramiento significativo en varios subgrupos posteriores (p = 0,008 para el total posterior al A-12). El resultado depende de la métrica, y una regla de oficio puede dejar de valer.

Un estudio de nueve proyectos, en una revista de menor rango, agrega dos matices: el CPI se estabiliza antes cuanto más seguido se lo mide, y en proyectos chicos rara vez se estabiliza (citando a Lipke, 2009). La muestra es chica y el propio texto lo dice.

## El SPI siempre termina en uno

El SPI tiene un defecto conocido: al terminar el proyecto, el valor ganado iguala al planificado, así que el SPI vale 1 aunque se haya entregado tarde. Lipke propuso el "earned schedule", que mide el desvío en unidades de tiempo (según un resumen; los originales no se leyeron). No se encontró una validación independiente: lo publicado es de Lipke y sus colaboradores.

> [!NOTE] Sin fuente todavía: valor ganado fuera de defensa y construcción, en trabajo de conocimiento o con agentes.

## Lo que se mide se deforma

Según la síntesis de la ley de Campbell (no verificada contra el original), una medida que se usa para premiar o castigar deja de medir bien. Campbell lo formuló para indicadores sociales y Goodhart para regularidades estadísticas usadas como objetivo de control (según un resumen secundario; las citas literales que circulan están deformadas). Ejemplos de la base, sin fuente: contar tareas cerradas invita a partirlas en tareas más chicas; medir horas cargadas invita a cargar horas.

> [!NOTE] Sin fuente todavía: estudios de proyectos que comparen medir resultados contra medir actividad. La recomendación de medir piezas terminadas y aceptadas, y no esfuerzo, es inferencia de esta base.

Por eso una pieza cuenta como terminada solo cuando pasa la [aceptación con evidencia](aceptar-con-evidencia.md). Las horas-persona como medida de avance están entre lo que, por tesis de la base y sin estudios que lo midan, [pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md).

## Qué cambia cuando ejecutan agentes

Las medidas de flujo funcionan igual con agentes: cuentan piezas, no personas. Lo nuevo es que cada tarea de un agente puede dejar registro de sus pasos y de los tokens que consumió. El costo por tarea se podría armar sumando el consumo de todos sus pasos (no verificado en la especificación), pero no hay una definición estándar (según la especificación en desarrollo que lista la [ficha de herramientas](herramientas-de-seguimiento.md)).

Dos cuidados, como inferencia de esta base. El tiempo de entrega tiene que incluir la espera de revisión humana, que podría ser la parte más larga (hipótesis, [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md)). Y la velocidad percibida no sirve como medida: los estudios de METR sobre desarrolladores que se creían más rápidos están en [frontera irregular](../Personas-y-agentes/frontera-irregular.md).

Para la entrega de software, las métricas de throughput e inestabilidad son las de [DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md). Cómo se le muestra el avance a un cliente está en [seguimiento con el cliente](../../Desarrollo/Encargo/seguimiento-con-el-cliente.md). La entrada de la vertical es [Seguimiento](seguimiento.md).
