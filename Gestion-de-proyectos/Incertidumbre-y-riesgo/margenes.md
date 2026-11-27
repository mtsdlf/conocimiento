---
resumen: >-
  Un margen es tiempo o plata que se reserva para absorber lo que salga distinto del plan; importa tanto su tamaño como dónde se ubica y quién lo controla, porque, según la explicación habitual de la cadena crítica, el margen repartido en cada tarea tiende a gastarse aunque no haga falta (con evidencia débil).
estado: vigente
estabilidad: semi
fuentes:
  - "Gutierrez y Kouvelis (1991), Parkinson's law and its implications for project management, Management Science 37(8):990-1001 (según resumen): https://econpapers.repec.org/RePEc:inm:ormnsc:v:37:y:1991:i:8:p:990-1001"
  - "Brannon, Hershberger y Brock (1999), Psychonomic Bulletin & Review (según resumen del buscador): https://link.springer.com/article/10.3758/BF03210823"
  - "Simulación del síndrome del estudiante en proyectos (según resumen): https://dlib.si/stream/URN:NBN:SI:DOC-28JY2A81/d0c0e633-e141-448f-aa1b-db656cc989df/PDF"
  - "Raz, Barnes y Dvir (2003), A critical look at critical chain project management, Project Management Journal 34(4):24-32 (solo el registro): https://cris.bgu.ac.il/en/publications/a-critical-look-at-critical-chain-project-management-2/"
  - "Goldratt, Critical Chain (1997) (no se leyó)"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
aliases: [margen, reserva, buffer, colchón, reserva de contingencia, contingency reserve, reserva de gestión, management reserve, ley de Parkinson, Parkinson's law, síndrome del estudiante, student syndrome]
creado: 2026-11-27
revisado: 2026-11-27
---

# Márgenes

Un margen es tiempo o plata que se reserva para absorber lo que salga distinto del plan; importa tanto su tamaño como dónde se ubica y quién lo controla, porque, según la explicación habitual de la cadena crítica, el margen repartido en cada tarea tiende a gastarse aunque no haga falta (con evidencia débil).

El margen es la distancia entre el [pronóstico](../Planificacion/pronostico.md) y lo que se compromete. Cubre los [riesgos](riesgo.md) que se aceptan y los [supuestos](supuestos.md) que pueden fallar. Cuando un desvío se come el margen y sale de la tolerancia, deja de ser un tema del equipo y pasa a [problemas y escalamiento](problemas-y-escalamiento.md). Es parte de [Incertidumbre y riesgo](incertidumbre-y-riesgo.md).

## Por qué el margen escondido se gasta

Si cada persona agrega su propio colchón a cada tarea, el proyecto se atrasa aunque tenga mucho margen: es la tesis habitual de la cadena crítica, que esta base no verificó. La explicación son dos efectos de conducta, y la evidencia de los dos es débil.

La ley de Parkinson dice que el trabajo se expande hasta llenar el tiempo disponible. Gutierrez y Kouvelis (1991) la modelaron para proyectos y señalaron que PERT y el camino crítico no incorporan esos efectos de conducta sobre la duración, según un resumen; es un modelo teórico, no un experimento. Según el resumen del buscador, Brannon, Hershberger y Brock (1999) afirman que la ley "has survived without an artifact-free demonstration at the individual level". Esta base no confirmó qué encontraron.

El síndrome del estudiante es dejar el trabajo para el final del plazo, cuando ya no queda margen para un imprevisto. Lo que hay es una simulación: según su resumen, eliminarlo acorta el proyecto hasta 35 % frente a cuando ocurre. No es un dato de campo.

> [!NOTE] Sin fuente todavía: evidencia de campo o experimental firme de la ley de Parkinson y del síndrome del estudiante en proyectos.

## Dónde va el margen

Hay dos lugares donde poner el margen, y cambian quién lo gasta:

| Dónde | Quién lo controla | Qué pasa |
|---|---|---|
| En cada tarea, escondido en la estimación | Quien hace la tarea | Si los efectos de arriba existen, se consume aunque la tarea no lo necesite, y lo que sobra en una tarea no pasa a otra |
| Juntado en una reserva visible | Quien gestiona el proyecto, o quien lo gobierna | Se gasta solo en lo que se desvía, y cuánto queda es un dato de seguimiento |

La cadena crítica de Goldratt, practicante, hace lo segundo: saca el margen de cada tarea y lo junta en reservas compartidas ([dependencias y camino crítico](../Planificacion/dependencias-y-camino-critico.md)). Su evidencia es la del método entero: propuesta de practicante, con validaciones empíricas escasas según las revisiones, y criticada por Raz, Barnes y Dvir (2003). Ver cuánta reserva se consumió frente a cuánto avance hubo es una forma de [medir el avance](../Seguimiento/medir-el-avance.md).

En el vocabulario habitual de los marcos, que esta base no cotejó con sus textos, se distingue además una reserva de contingencia, para los riesgos identificados, de una reserva de gestión, para lo que nadie previó, que controla un nivel más arriba. Lectura de esta base, sin fuente: el margen que cubre lo desconocido no lo administra quien ejecuta.

> [!NOTE] Sin fuente todavía: el tratamiento de las reservas de contingencia y de gestión en los estándares; esta base no leyó sus textos.

## Cuánto margen

El tamaño sale del pronóstico, no de un porcentaje fijo. Si se pronostica con una distribución, el margen es la distancia entre la mediana y el percentil con que se quiere cumplir. Como los desvíos tienen [cola gruesa](por-que-fallan-los-proyectos.md), ese percentil queda bastante más lejos de lo que sugiere el desvío promedio. Es la lectura de esta base a partir del pronóstico por clase de referencia, que sí se describe en [pronóstico](../Planificacion/pronostico.md).

En un proyecto con precio cerrado, quién paga el margen es una decisión comercial, y cómo se reparte el riesgo con el cliente está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md).

## El margen que importa con agentes

Es una inferencia de esta base, sin fuente, que un agente no posterga su tarea ni la estira porque sobra tiempo, y que los efectos de conducta de arriba no le aplican. También lo es que el margen que importa cuando ejecutan agentes es el de verificación y retrabajo humano. Si una de cada tres entregas vuelve de la revisión, lo que alarga el plazo es la cola de quien revisa.

Del lado del costo, el margen se vuelve un tope de gasto por tarea y por período: lo que el agente puede consumir en reintentos antes de que alguien decida. Está en [capacidad y costo](../Planificacion/capacidad-y-costo.md).

> [!NOTE] Sin fuente todavía: no se encontró un recurso canónico verificado sobre márgenes en proyectos. El candidato es Raz, Barnes y Dvir (2003) para el balance crítico de las reservas, completado con Goldratt como fuente de practicante.
