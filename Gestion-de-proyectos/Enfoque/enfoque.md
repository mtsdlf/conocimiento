---
resumen: >-
  El enfoque es la forma en que se organiza el trabajo de un proyecto según cuánto se sabe del resultado y del camino: planificar todo antes, entregar por partes, hacer fluir un trabajo que no para o fijar el tiempo y recortar el alcance. Sobre cualquiera de esas formas se monta una capa de etapas con una decisión de seguir o parar.
estado: borrador
estabilidad: estable
fuentes:
  - "Klünder et al. (2019), Catching up with Method and Process Practice (HELENA), ICSE-SEIP (texto completo): https://arxiv.org/pdf/2101.12383"
  - "Serrador y Pinto (2015), Does Agile work?, IJPM 33(5) (abstract y ficha de APM): https://apm.org.uk/media/r01fph3t/does-agile-work-a-quantitative-analysis-of-agile-project-success.pdf"
  - "Larman y Basili (2003), Iterative and Incremental Development: A Brief History, IEEE Computer 36(6) (texto completo): https://mosaicprojects.com.au/PDF-Gen/History_of_Iterative_and_Incremental_Development.pdf"
  - "Cooper y Sommer (2016), The Agile-Stage-Gate Hybrid Model, JPIM 33(5) (ficha): https://experts.mcmaster.ca/display/publication319920"
  - "Gestion-de-proyectos/.investigacion/enfoque.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [enfoque de desarrollo, ciclo de vida del proyecto, development approach, project life cycle, metodología]
creado: 2026-11-27
revisado:
---

# Enfoque

El enfoque es la forma en que se organiza el trabajo de un proyecto según cuánto se sabe del resultado y del camino: planificar todo antes, entregar por partes, hacer fluir un trabajo que no para o fijar el tiempo y recortar el alcance. Sobre cualquiera de esas formas se monta una capa de etapas con una decisión de seguir o parar.

Recibe del [Encuadre](../Encuadre/encuadre.md) qué resultado se busca y qué alcance queda fijo, y le da a la [Planificación](../Planificacion/planificacion.md) la forma del plan: un cronograma completo, una secuencia de entregas, una cola con límites o una caja de tiempo. El [Seguimiento](../Seguimiento/seguimiento.md) mide distinto según el enfoque elegido, y el [Gobierno](../Gobierno-y-cierre/gobierno-y-cierre.md) decide en los puntos de control que el enfoque deja marcados.

## Cómo parte el campo los enfoques

Según un resumen secundario, el PMI parte el campo en tres: predictivo, adaptativo e híbrido. Las notas de esta vertical abren "adaptativo" en tres formas que funcionan distinto: [iterar](enfoque-iterativo.md), hacer [fluir](flujo-continuo.md) el trabajo y [apostar con tiempo fijo](apuesta-con-tiempo-fijo.md). Flujo y tiempo fijo no son categorías del estándar: vienen de practicantes (Reinertsen, Anderson, Basecamp) y de la teoría de colas.

| Enfoque | Qué queda fijo | Qué varía | Sirve cuando |
|---|---|---|---|
| [Predictivo](enfoque-predictivo.md) | el alcance, decidido antes | el plazo y el costo, si el plan falla | el resultado y el camino se conocen y equivocarse sale caro |
| [Iterativo](enfoque-iterativo.md) | el largo de cada vuelta | el alcance, vuelta a vuelta | lo que se quiere se descubre usando lo que se entrega |
| [Flujo continuo](flujo-continuo.md) | el límite de trabajo en curso | qué entra y cuándo | el trabajo llega sin parar y no tiene fin |
| [Apuesta con tiempo fijo](apuesta-con-tiempo-fijo.md) | el tiempo que se está dispuesto a gastar | el alcance, recortado antes de empezar | algo vale una cantidad de tiempo y no más |

El híbrido es lo normal. En la encuesta HELENA la mayoría de los casos declara mezclar métodos; las cifras, y lo poco que dicen los estudios sobre qué enfoque rinde mejor, están en [elegir un enfoque](elegir-un-enfoque.md).

## Las etapas son una capa de gobierno, no un quinto enfoque

[Etapas y puntos de control](etapas-y-puntos-de-control.md) no compite con los cuatro de la tabla. Es una capa que se monta sobre cualquiera: corta el proyecto en tramos y al final de cada uno alguien decide seguir, cambiar o parar. PRINCE2 la exige (al menos dos etapas, según resúmenes secundarios), y Cooper y Sommer (2016) la combinaron con sprints en el modelo Agile-Stage-Gate. Un proyecto puede ser iterativo adentro de cada etapa y tener tres puertas con decisión real. Quién decide en cada puerta está en [gobierno del proyecto](../Gobierno-y-cierre/gobierno-del-proyecto.md).

## Iterar no exige ceremonias

Lo que define a un enfoque es qué queda fijo y cuándo se aprende, no sus reuniones ni sus roles. Según Larman y Basili (2003), se desarrolla de forma iterativa desde mediados de los años 50, mucho antes de cualquier marco con nombre. Los marcos de software, como Scrum, se tratan en [Desarrollo](../../Desarrollo/Fundamentos/escuelas-de-desarrollo.md#ágil-xp-y-scrum-los-valores-y-los-marcos-que-salieron-de-ellos); qué de esas ceremonias pierde peso está en [lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md).

## Lo que cambia cuando ejecutan agentes

Inferencia de esta base, sin estudio que la pruebe: si ejecutar se abarata, cada enfoque se corre hacia especificar y verificar. Equivocarse en un plan cuesta horas en vez de meses, así que el predictivo puede probar versiones antes de comprometerse. Las vueltas del iterativo se acortan, pero el límite pasa a ser la retroalimentación. En el flujo, el cuello de botella se mueve a la revisión, que es lo que trata [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md). La evidencia de que ejecutar se abarate es mixta: depende de si la tarea cae dentro de la [frontera irregular](../Personas-y-agentes/frontera-irregular.md).

## Qué hay adentro del enfoque

- [Elegir un enfoque](elegir-un-enfoque.md) — cómo se elige y se mezcla según la incertidumbre, y qué tan débil es la evidencia para hacerlo; se lee primero.
- [Enfoque predictivo](enfoque-predictivo.md) — planificar todo antes: el malentendido de Royce, cuándo sirve y cuándo engaña.
- [Enfoque iterativo](enfoque-iterativo.md) — entregar por partes y aprender de cada una, sin depender de un marco.
- [Flujo continuo](flujo-continuo.md) — el trabajo como colas: límite de trabajo en curso, tamaño de lote y costo de demora.
- [Apuesta con tiempo fijo](apuesta-con-tiempo-fijo.md) — fijar cuánto tiempo vale algo y recortar el alcance para que entre.
- [Etapas y puntos de control](etapas-y-puntos-de-control.md) — la capa de tramos con decisión de seguir o parar, que va sobre cualquier enfoque.
