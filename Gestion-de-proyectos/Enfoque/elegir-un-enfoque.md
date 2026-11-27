---
resumen: >-
  Elegir un enfoque es decidir qué queda fijo y qué varía en un proyecto (alcance, tiempo o trabajo en curso) mirando cuánto se sabe del resultado y del camino, y mezclar enfoques por partes cuando conviene. Es el criterio en el que, según resúmenes secundarios, pone el foco el PMBOK 8 (el estándar no se pudo leer), aunque la evidencia de que elegir así mejore los resultados es débil.
estado: borrador
estabilidad: semi
fuentes:
  - "Serrador y Pinto (2015), Does Agile work? A quantitative analysis of agile project success, IJPM 33(5):1040-1051 (abstract): https://pure.psu.edu/en/publications/does-agile-work-a-quantitative-analysis-of-agile-project-success/"
  - "Ficha de APM sobre Serrador y Pinto (2015) (leída entera): https://apm.org.uk/media/r01fph3t/does-agile-work-a-quantitative-analysis-of-agile-project-success.pdf"
  - "Gemino, Horner Reich y Serrador (2021), Agile, traditional, and hybrid approaches to project success: is hybrid a poor second choice?, Project Management Journal 52(2):161-175 (según el resumen de los autores): https://www.socialsciencespace.com/2023/03/agile-traditional-and-hybrid-approaches-to-project-success-is-hybrid-a-poor-second-choice/"
  - "Klünder et al. (2019), Catching up with Method and Process Practice (HELENA), ICSE-SEIP (texto completo): https://arxiv.org/pdf/2101.12383"
  - "Snowden y Boone (2007), A Leader's Framework for Decision Making, HBR (según resúmenes secundarios): https://en.wikipedia.org/wiki/Cynefin_framework"
  - "Matriz de Stacey (según resúmenes secundarios): https://plexusinstitute.org/edgeware/archive/think/main_aides3.html ; https://umbrex.com/resources/change-management-frameworks/what-is-stacey-matrix/"
  - "PMI, A Guide to the PMBOK, tailoring (vista previa, según resumen): https://www.oreilly.com/library/view/a-guide-to/9781628258301/p2section03.xhtml"
  - "Khoza y Marnewick (2020), South African Computer Journal (según resumen del buscador): https://sacj.cs.uct.ac.za/index.php/sacj/article/download/683/388"
  - "Ahimbisibwe, Cavana y Daellenbach (2015), J. Enterprise Information Management (según resumen del buscador): https://emerald.com/insight/content/doi/10.1108/JEIM-08-2013-0060/full/html"
  - "Garousi et al. (2018), Software Quality Journal (según resumen del buscador): https://link.springer.com/article/10.1007/s11219-018-9419-5"
  - "Gestion-de-proyectos/.investigacion/enfoque.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [elección del enfoque, adaptar el enfoque, tailoring, enfoque híbrido, hybrid approach, ajuste por contingencia]
creado: 2026-11-27
revisado:
---

# Elegir un enfoque

Elegir un enfoque es decidir qué queda fijo y qué varía en un proyecto (alcance, tiempo o trabajo en curso) mirando cuánto se sabe del resultado y del camino, y mezclar enfoques por partes cuando conviene. Es el criterio en el que, según resúmenes secundarios, pone el foco el PMBOK 8 (el estándar no se pudo leer), aunque la evidencia de que elegir así mejore los resultados es débil.

Los enfoques entre los que se elige están descritos en la entrada de [Enfoque](enfoque.md). Esta decisión se toma al arrancar, después del [encuadre](../Encuadre/encuadre.md), y se revisa en cada [punto de control](etapas-y-puntos-de-control.md).

## Qué mirar para decidir

La pregunta central es cuánto se sabe antes de empezar y cuánto cuesta equivocarse. Cuatro señales ayudan a responderla (criterio de la base, sin estudio que lo respalde):

| Señal | Empuja hacia |
|---|---|
| El resultado está definido y el camino se conoce (una mudanza de oficina ya hecha otras veces) | [predictivo](enfoque-predictivo.md) |
| Lo que se quiere se descubre mostrando algo (un servicio nuevo, una plataforma con usuarios) | [iterativo](enfoque-iterativo.md) |
| El trabajo llega sin parar, en pedidos chicos y sin fecha de fin (soporte, mantenimiento, un equipo de operaciones) | [flujo continuo](flujo-continuo.md) |
| Algo vale una cantidad de tiempo y no más, y quien pide acepta recortar | [apuesta con tiempo fijo](apuesta-con-tiempo-fijo.md) |

Un mismo proyecto suele tener partes de cada fila. En un evento, la logística del lugar se planifica entera, el programa se itera con los oradores y los pedidos de los asistentes entran como flujo. Mezclar así es lo que el PMBOK llama adaptar (tailoring): según una vista previa del estándar, se adaptan el enfoque, los procesos, el ciclo de vida, los entregables y el involucramiento de interesados.

## Lentes para medir la incertidumbre

Cynefin (Snowden y Boone, 2007) distingue contextos con respuestas distintas, según resúmenes secundarios. En lo simple se categoriza y se responde; en lo complicado se analiza antes; en lo complejo se sondea con experimentos seguros; en lo caótico se actúa primero. Inferencia de la base: el enfoque predictivo encajaría con lo complicado, y el iterativo y la apuesta, con lo complejo.

La matriz de Stacey cruza el acuerdo entre las personas con la certeza sobre el camino. Su origen es confuso y cada fuente la dibuja distinto: discrepan en qué cuadrante va "complicado" y en cuál "complejo". Conviene usarla con cautela.

Las dos son marcos para pensar, no estudios. No hay evidencia de que elegir el enfoque con ellas mejore los resultados.

## Lo que dicen los estudios que comparan enfoques

El estudio cuantitativo más citado es el de Serrador y Pinto (2015), sobre 1.002 proyectos de varias industrias y países. Según su abstract, el uso de ágil tuvo efecto positivo sobre la eficiencia y sobre la satisfacción de los interesados. La calidad de la visión y de los objetivos fue un moderador solo marginalmente significativo. Según la ficha de APM, no hubo diferencia significativa en la planificación inicial entre proyectos ágiles y no ágiles, y la planificación continua ayudó: el resultado favorece planificar, no un enfoque en particular.

Gemino, Horner Reich y Serrador (2021) compararon los tres tipos, según el resumen de los autores. Los proyectos híbridos igualaron a los tradicionales y a los ágiles en presupuesto, plazo, alcance y calidad. Ágil e híbrido tuvieron la misma satisfacción de interesados, y ambos superaron a los tradicionales, controlando complejidad y experiencia del equipo. Los autores concluyen que el híbrido no es una segunda opción pobre.

El híbrido además es lo que la gente hace. En la encuesta HELENA, el 76,8 % (562 de 732 casos) declara usar métodos híbridos, en empresas de todos los tamaños (Klünder et al., 2019). Scrum lo usa el 84,7 % de los participantes, pero solo el 69,3 % de ellos "a menudo o siempre", y PRINCE2 aparece en el 9,7 %. La muestra es de software y sistemas, y no se traslada tal cual a otros dominios.

## La incertidumbre como criterio, en disputa

> [!IMPORTANT]
> **El enfoque se elige según la incertidumbre.** Es la postura que los resúmenes secundarios atribuyen al PMBOK 8 (no leído) y la de la escuela de este tema. Se apoya en un razonamiento de la base, no en un estudio: si el resultado se descubre en el camino, comprometer el alcance antes no tiene sentido.
>
> **El efecto no depende de la incertidumbre.** Según la ficha de APM, en Serrador y Pinto (2015) el éxito con ágil no dependió de la experiencia del equipo ni de la complejidad del proyecto: ágil ayudó parejo, no más donde había más incertidumbre. Khoza y Marnewick (2020) ven poca evidencia de que ágil sea más exitoso como metodología, según un resumen.
>
> **La evidencia del ajuste es mixta.** Ahimbisibwe, Cavana y Daellenbach (2015) describen la evidencia del modelo de contingencia como mixta y piden probarlo con datos. Garousi et al. (2018) encontraron asociaciones positivas entre factores y resultados, "pero mayormente en niveles no significativos" (los dos, según resúmenes del buscador).
>
> El estudio de Serrador y Pinto es correlacional y de autorreporte: cada persona describía de memoria un proyecto más exitoso y uno menos exitoso. De los demás solo se vio el resumen, sin su método. No hay metaanálisis del ajuste entre enfoque y contexto. La base sostiene el criterio como razonable, no como probado.

## Cómo falla la elección

Lo que sigue son inferencias de la base, sin fuente.

- **Elegir el enfoque por identidad.** Un equipo que "es ágil" itera también la logística de un evento con fecha y lugar cerrados, y paga en retrabajo lo que un plan resolvía.
- **Planificar entero lo que nadie sabe.** El riesgo opuesto, con el caso del Departamento de Defensa de EE. UU., está en [enfoque predictivo](enfoque-predictivo.md).
- **Tomar el híbrido como fracaso.** La evidencia de Gemino y otros no lo pone por debajo de los enfoques puros.
- **No revisar la elección.** La incertidumbre baja a medida que el proyecto avanza; lo que empezó como apuesta puede terminar como plan. El momento natural de revisarla es cada [punto de control](etapas-y-puntos-de-control.md).

## Elegir cuando ejecutan agentes

Inferencia de esta base: cuando un agente ejecuta, el costo de probar una versión baja, y eso empuja hacia enfoques que aprenden mostrando algo. Lo que no baja es el costo de especificar bien y de revisar. La elección pasa a depender menos de cuánto cuesta construir y más de cuánta atención humana hay para decidir qué vale y aceptar lo hecho, que es lo que trata [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md).

> [!NOTE]
> Sin fuente todavía: estudios que comparen enfoques en proyectos donde ejecutan agentes, y cualquier estudio con método de ágil o flujo fuera del software.
