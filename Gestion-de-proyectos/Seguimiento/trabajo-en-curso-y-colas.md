---
resumen: >-
  El trabajo en curso es todo lo que se empezó y no se terminó; por la ley de Little, con el mismo ritmo de salida, más trabajo en curso significa más tiempo de entrega, y por eso se limita y se vigilan las colas.
estado: borrador
estabilidad: semi
fuentes:
  - "Little (2011), Little's Law as Viewed on Its 50th Anniversary, Operations Research 59(3): 536-549 (leído entero): https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf"
  - "Vacanti (2018), Little's Law for Professional Scrum with Kanban (según un resumen del buscador): https://scrumorg-website-prod.s3.amazonaws.com/drupal/2018-05/Little’s Law for Professional Scrum with Kanban.pdf"
  - "Reinertsen (2011), Understanding the Magic of Lean Product Development, diapositivas de QCon (según un resumen del buscador; el libro de 2009 no se leyó): https://qconsf.com/sf2011/dl/qcon-sanfran-2011/slides/DonReinertsen_UnderstandingTheMagicOfLeanProductDevelopment.pdf"
  - "Rubinstein, Meyer y Evans (2001), Executive control of cognitive processes in task switching, JEP: HPP 27(4) (solo el resultado del buscador): https://typeset.io/pdf/executive-control-of-cognitive-processes-in-task-switching-1k82y0gpz8.pdf"
  - "Estudio empírico de WIP en equipos kanban, ESEM 2018 (según un resumen del buscador): https://www.sintef.no/publikasjoner/publikasjon/1637884/"
  - "Tesis de maestría de la Universidad de Oslo sobre WIP y throughput (según un resumen del buscador): https://duo.uio.no/handle/10852/42080"
  - "dos Santos et al. (2018), síntesis sobre Kanban (según un resumen del buscador): https://rd.springer.com/content/pdf/10.1186/s40411-018-0057-1.pdf"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [WIP, work in progress, trabajo en proceso, límite de WIP, WIP limit, ley de Little, Little's law, colas, queues, tamaño de tanda, batch size]
creado: 2026-11-27
revisado:
---

# Trabajo en curso y colas

El trabajo en curso es todo lo que se empezó y no se terminó; por la ley de Little, con el mismo ritmo de salida, más trabajo en curso significa más tiempo de entrega, y por eso se limita y se vigilan las colas.

El trabajo en curso incluye lo que está esperando: una revisión pendiente, un permiso que no llegó, una tarea a medio hacer porque alguien pasó a otra. Esas esperas son colas, y en un proyecto suelen no aparecer en el cronograma (observación de la base, sin medición). Pensar el trabajo como [flujo continuo](../Enfoque/flujo-continuo.md) empieza por contarlas.

## La ley de Little es un balance de promedios

La ley de Little relaciona tres promedios: el trabajo en curso (L), la tasa de salida (λ) y el tiempo que cada pieza pasa adentro (W), con L = λW. Little la describe así: "Basically, it is a theorem in queuing theory". Según su artículo de 2011, vale "under remarkably general conditions", para una cola sola o para una red, y es "independent of queue discipline": no importa en qué orden se atiende. En su versión determinista vale exacta sobre una trayectoria observada, sin suponer estado estacionario ni distribuciones.

En gestión de operaciones se escribe como rendimiento = trabajo en curso / tiempo de ciclo. Little cita esa lectura: "any increase in output requires either an increase in work-in-process inventory or a reduction in cycle time or both, unless some change is made in the manufacturing process itself".

Un ejemplo con números redondos: si una persona revisa diez entregas por día y hay treinta esperando, cada entrega nueva espera en promedio unos tres días. Para bajar la espera a un día hay dos caminos: revisar más rápido o dejar entrar menos.

## Lo que la ley no dice

La ley no pronostica. Vacanti, practicante de Kanban, insiste en que no predice resultados por sí sola: si sube el trabajo en curso promedio, puede cambiar el tiempo de ciclo, el rendimiento o los dos (según un resumen). Exige además que el trabajo en curso no cambie mucho en el período y que todo lo que entra termine saliendo. Little recomienda usarla "in conjunction with other models and other measurements".

Por eso la lectura de gestión es condicional. Limitar el trabajo en curso acorta el tiempo de entrega solo si el rendimiento no cae al limitar. Si el equipo queda ocioso esperando, el límite no ayuda.

## Por qué las colas crecen antes de que se note

Reinertsen sostiene que la creencia en la eficiencia, sumada a no ver las colas, lleva a cargar los procesos con utilización alta. Según el modelo de colas más simple (M/M/1), la cola crece de forma no lineal cuando la utilización se acerca al 100 %, y el costo de demora crece con la cola. Esto sale de un resumen de sus diapositivas; el libro no se leyó.

En blogs circula que conviene no pasar del 80 % de utilización, atribuido a Reinertsen. No se encontró en su texto y no se usa en esta base.

Cambiar de tarea también cuesta. Rubinstein, Meyer y Evans (2001) son la fuente académica de los costos de cambio de tarea. No se tienen sus magnitudes, y hay debate sobre qué miden.

> [!NOTE] Sin fuente todavía: la magnitud del costo de la multitarea en trabajo de proyectos. La cifra popular de que cada tarea extra hace perder entre 20 y 40 % no se pudo verificar.

## Lo que muestran los equipos reales

> [!IMPORTANT]
> **A favor de limitar el trabajo en curso.** La ley de Little implica que, con el rendimiento constante, menos trabajo en curso es menos espera. En un estudio de ESEM 2018 sobre más de 8.000 ítems, cuatro años y cinco equipos de una empresa, menos trabajo en curso fue con tiempos de entrega más cortos (según un resumen). Una tesis de la Universidad de Oslo con datos de 2008 a 2013 concluye que los límites importan (según un resumen).
>
> **En contra, o al menos no tan simple.** El mismo estudio de ESEM halló que el trabajo en curso también correlaciona con la productividad, algo que los autores llaman "inconsistente" con lo que dice la literatura. Concluyen que es difícil indicar un límite óptimo y que no hay estudios publicados de casos reales sobre ese óptimo. En la tesis de Oslo, la correlación entre trabajo en curso y rendimiento fue de 0,4, y de 0,2 con errores y tiempo de entrega. dos Santos y otros señalan la "ausencia de resultados negativos" en la literatura sobre Kanban, una señal de sesgo de publicación.
>
> **Estado.** La matemática es firme; la evidencia de que limitar el trabajo en curso mejora proyectos es débil, de una empresa por estudio y sin experimentos controlados. No se encontraron críticas formales a Reinertsen. Todo es de software.

## Tanda chica y límite explícito

El tamaño de tanda es cuánto trabajo se pasa junto de un paso al siguiente: una revisión de cuarenta cambios o cuatro de diez. La recomendación de tandas chicas viene de la misma tradición de flujo.

> [!NOTE] Sin fuente todavía: evidencia sobre tamaño de tanda en proyectos, fuera de lo que el tema DevOps reúne sobre lotes en la entrega de software ([flujo de valor](../../DevOps/Cultura-y-medicion/flujo-de-valor.md)).

Práctica de la base, sin fuente: el límite se escribe por etapa ("no más de cinco cosas esperando revisión") y se respeta antes de empezar algo nuevo. Cuando una etapa llega al límite, quien está libre ayuda a vaciarla. Lo mismo vale entre proyectos: cuántos van en paralelo es una decisión de [portafolio](../Gobierno-y-cierre/portafolio.md).

## Con agentes, la cola que manda es la de revisión

La ley de Little vale igual para una cola de tareas que ejecutan agentes: es un balance de promedios y no le importa quién atiende. Lo que cambia es dónde queda la cola. Los agentes pueden producir muchas piezas en paralelo, y entonces el trabajo en curso se acumula frente a la persona que tiene que aceptarlas. Esa lectura es inferencia de esta base; el mecanismo está en [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md).

> [!NOTE] Sin fuente todavía: si un agente paga algún costo por cambiar de tarea comparable al humano. No se afirma.

El tiempo de entrega y el rendimiento que salen de esta cuenta se miden como dice [medir el avance](medir-el-avance.md), y la entrada de la vertical es [Seguimiento](seguimiento.md).
