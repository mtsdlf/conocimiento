---
resumen: >-
  El enfoque predictivo fija el alcance antes de ejecutar y ordena el trabajo en fases que se recorren una vez: requisitos, diseño, construcción, prueba y entrega. Sirve cuando el resultado y el camino se conocen; engaña cuando el plan detallado se toma como conocimiento de algo que nadie sabe todavía.
estado: vigente
estabilidad: estable
fuentes:
  - "Larman y Basili (2003), Iterative and Incremental Development: A Brief History, IEEE Computer 36(6):47-56 (texto completo): https://mosaicprojects.com.au/PDF-Gen/History_of_Iterative_and_Incremental_Development.pdf"
  - "Royce (1970), Managing the Development of Large Software Systems, IEEE WESCON (no leído; frase citada según el buscador): https://faculty.washington.edu/hazeline/misc/reserve/royce_waterfall.pdf"
  - "Saravanos (2025), A Brief History of the Waterfall Model, arXiv 2510.03894, sin revisión por pares (abstract): https://arxiv.org/html/2510.03894v3"
  - "BCS, sobre la adopción de la cascada (según resumen del buscador): https://www.bcs.org/content/conWebDoc/22547"
  - "Flyvbjerg (2014), What You Should Know About Megaprojects and Why, PMJ 45(2) (texto completo): https://arxiv.org/pdf/1409.0003.pdf"
  - "Flyvbjerg y Gardner (2023), How Big Things Get Done (según una reseña): https://www.independent.org/tir/2023-fall/how-big-things-get-done/"
  - "Gestion-de-proyectos/.investigacion/enfoque.md"
aliases: [cascada, waterfall, enfoque tradicional, plan-driven, predictive approach]
creado: 2026-11-27
revisado: 2026-11-27
---

# Enfoque predictivo

El enfoque predictivo fija el alcance antes de ejecutar y ordena el trabajo en fases que se recorren una vez: requisitos, diseño, construcción, prueba y entrega. Sirve cuando el resultado y el camino se conocen; engaña cuando el plan detallado se toma como conocimiento de algo que nadie sabe todavía.

Es uno de los [enfoques](enfoque.md) entre los que se [elige](elegir-un-enfoque.md). Lo fijo es el alcance; si el plan falla, lo que se mueve es el plazo y el costo. Por eso depende de una [línea base de alcance](../Encuadre/alcance.md) firme y de un [control de cambios](../Seguimiento/control-de-cambios.md) que la proteja.

## Dónde rinde un plan completo

Criterio de la base, sin fuente: rinde cuando el trabajo ya se hizo antes y lo que falla en el medio es caro de deshacer. Mudar un centro de datos con ventana de corte fija, levantar una obra con permisos o armar un evento con lugar y fecha cerrados son casos así. Ahí las dependencias son conocidas, el [camino crítico](../Planificacion/dependencias-y-camino-critico.md) se puede calcular y un error descubierto tarde cuesta más que planificar de más al principio.

Flyvbjerg y Gardner (2023) defienden planificar mucho por otra razón, según una reseña: "pensar lento, actuar rápido". La reseña no permite más detalle y el libro no se leyó; que la planificación sea la fase barata y la ejecución la cara es la lectura habitual de esa tesis, sin cotejar.

## Royce no recomendó la cascada

Según Larman y Basili (2003), el texto que se cita como origen de la cascada se lee mal: "muchos, incorrectamente, ven el artículo de Royce como el paradigma de la cascada de una sola pasada". Royce (1970), según esos autores, recomendó hacerlo dos veces: que la versión entregada fuera, en lo crítico, la segunda. Sugirió que un proyecto de 30 meses tuviera un piloto de 10 meses cuando hay elementos nuevos e incógnitas.

La frase más citada del artículo, "I believe in this concept, but the implementation described above is risky and invites failure", figura en la copia de la Universidad de Washington según el buscador; no se cotejó con el original. Royce tampoco usó la palabra "waterfall": según un artículo sin revisión por pares, la popularizaron Bell y Thayer en 1976. El BCS atribuye parte de la adopción a los grandes contratos de gobierno, que prefieren estructuras rígidas, según un resumen.

## Dónde engaña

El plan detallado engaña cuando lo que se quiere se descubre haciendo. Larman y Basili parafrasean a Parnas y Clements con cuatro razones por las que especificar todo antes es impracticable:

1. Quienes usan el resultado rara vez saben exactamente qué quieren.
2. Muchos detalles aparecen solo al implementar.
3. Una persona maneja poca complejidad a la vez.
4. Los cambios externos invalidan decisiones ya tomadas.

Larman y Basili citan el caso del Departamento de Defensa de EE. UU. A fines de los 80 tenía fallas importantes con la cascada que exigía su estándar DoD-Std-2167. Una revisión de 1999 de proyectos anteriores concluyó: "Of a total $37 billion for the sample set, 75% of the projects failed or were never used, and only 2% were used without extensive modification". A fines de 1987 el DoD cambió sus estándares para permitir desarrollo iterativo. El dato es de segunda mano (Larman y Basili citan la revisión) y es de software militar.

Planificar a fondo tampoco garantiza cumplir. Según Flyvbjerg (2014), los megaproyectos se pasan de costo y plazo una y otra vez; las cifras y la disputa sobre sus causas están en [por qué fallan los proyectos](../Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md). El remedio que propone esa línea no es planificar menos sino [pronosticar](../Planificacion/pronostico.md) mirando proyectos parecidos ya terminados.

## Iterar y planificar a fondo no se oponen

Las dos fuentes empujan para lados distintos: Larman y Basili, a iterar para aprender; Flyvbjerg, a planificar más antes de ejecutar. Se pueden conciliar, por lectura de la base, si la iteración barata (un prototipo, un piloto, el "hacerlo dos veces" de Royce) se cuenta como parte de pensar lento. Lo que Flyvbjerg condena es aprobar sin haber explorado alternativas (según una reseña). Criterio de la base: un proyecto predictivo sano tiene una [etapa](etapas-y-puntos-de-control.md) de exploración antes de comprometer la línea base.

Tesis de la base, sin estudio que la pruebe: lo que pierde peso es el cronograma detallado a meses vista tomado como compromiso, no el plan. Está en [lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md).

## Planificar cuando ejecutan agentes

Inferencia de esta base: si un agente construye una versión en horas, equivocarse en la especificación cuesta horas y no meses. El piloto de Royce se abarata, y en vez de planificar todo se pueden probar versiones. El valor de planificar se corre a decidir qué vale la pena construir, que es el "pensar lento" de Flyvbjerg aplicado a la decisión y no a la ejecución. Lo que sigue siendo caro de deshacer (un corte de servicio, un contrato, una obra física) conserva el plan completo.
