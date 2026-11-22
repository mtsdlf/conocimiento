---
resumen: >-
  Un roadmap es el plan visible de hacia dónde va un producto y qué viene primero. Qué debe llevar adentro (funcionalidades con fecha, temas, resultados) es la disputa central de la planificación de producto, y ninguna posición tiene estudios que la respalden.
estado: vigente
estabilidad: semi
fuentes:
  - "Marty Cagan, Product Roadmaps (SVPG, 2009-01-07): https://www.svpg.com/product-roadmaps/"
  - "Marty Cagan, The Alternative to Roadmaps (SVPG, 2015-09-07): https://www.svpg.com/the-alternative-to-roadmaps/"
  - "C. Todd Lombardo, Bruce McCarthy, Evan Ryan y Michael Connors, Product Roadmaps Relaunched (O'Reilly, 2017), según resúmenes e índice: https://www.oreilly.com/library/view/product-roadmaps-relaunched/9781491971710"
  - "Janna Bastow, I invented the Now-Next-Later roadmap (ProdPad, 2022-10-18): https://www.prodpad.com/blog/invented-now-next-later-roadmap/"
  - "Pragmatic Institute Framework: https://www.pragmaticinstitute.com/framework/"
  - "Basecamp, Shape Up, introducción: https://basecamp.com/shapeup/0.3-chapter-01"
  - "Producto/.investigacion/planificacion-y-entrega.md"
  - "Producto/.investigacion/posicion-contraria.md"
aliases: [product roadmap, hoja de ruta, roadmap de producto, Now-Next-Later]
creado: 2026-11-22
revisado: 2026-11-22
---

# Roadmap

Un roadmap es el plan visible de hacia dónde va un producto y qué viene primero. Qué debe llevar adentro (funcionalidades con fecha, temas, resultados) es la disputa central de la planificación de producto, y ninguna posición tiene estudios que la respalden.

El Pragmatic Institute lo define así: "A product roadmap is a visual plan of the product's direction and priorities over time", y le asigna una pregunta: "Which outcomes come next, and in what order?". El roadmap toma la dirección de la [estrategia](../Estrategia/estrategia-de-producto.md) y la ubica en el tiempo. El orden fino dentro de cada tramo es trabajo de [priorización](priorizacion.md).

## Tres posiciones sobre qué lleva un roadmap

Según el informe, la escuela de Cagan y la de *Roadmaps Relaunched* y Pragmatic coinciden en que la peor forma de roadmap es una lista de funcionalidades con fechas. Difieren en qué la reemplaza.

| Posición | Qué propone | Qué hace con las fechas |
|---|---|---|
| Cagan (SVPG) | Visión de producto y objetivos de negocio por equipo, con OKRs, en lugar del roadmap | Las vuelve excepcionales ("high-integrity commitments") |
| *Product Roadmaps Relaunched* | Un roadmap que comunica la visión, atado a objetivos medibles, con temas como componente central | Los resúmenes leídos no lo dicen |
| Now-Next-Later (Bastow) | Tres columnas: ahora, después, más adelante | Las saca |

Cagan desconfía del roadmap. En 2009 escribió que "your job is not to prioritize and document feature requests" y que "To lock in specific features at the roadmap level is to effectively skip the most important part of your job": fijar la funcionalidad antes de descubrirla. Sobre las fechas, "these dates are essentially just your hopes and wishes". En 2015 describió el roadmap típico como una lista priorizada de funcionalidades que "tell the team what to do", y propuso darle a cada equipo un problema y un objetivo. Eso conecta con la diferencia entre [resultados y entregables](../Estrategia/resultados-y-entregables.md) y con el [equipo empoderado](../Organizacion/equipo-empoderado.md).

*Roadmaps Relaunched* lo conserva, reformado. El libro de Lombardo, McCarthy, Ryan y Connors (O'Reilly, 2017) lleva el subtítulo "How to Set Direction while Embracing Uncertainty". Según resúmenes, defiende roadmaps que comuniquen la visión y se organicen por temas atados a objetivos medibles. El texto no se pudo abrir; lo que se dice viene de resúmenes y del índice. Una página de terceros afirma que el libro trata Now-Next-Later y que Google y Spotify adoptaron el formato; no se pudo confirmar y no se usa.

Now-Next-Later saca las fechas. Janna Bastow (ProdPad) cuenta que "dropped the dates and drew three columns", porque "rather than focusing on deadline-based delivery, product teams should stay focused on discovery". El post es de 2022; en un comentario ubica el origen en 2012, en "the original version that Simon and I sketched out in 2012", con columnas llamadas Current, Near Term y Future.

> [!IMPORTANT]
> Ninguna de las tres posiciones tiene un estudio que compare roadmaps por resultados con roadmaps por fechas. Son tesis de practicantes.
>
> Hay una cuarta posición que no es un roadmap. Shape Up trabaja en apuestas de seis semanas y dice "We don't rethink our roadmap every two weeks"; el tiempo es fijo y el alcance variable: "If a project runs over, by default it doesn't get an extension". Compromete un ciclo, no un tema sin fecha. Está en [Shape Up](shape-up.md).
>
> En contra de sacar las fechas: ventas, marketing, regulaciones y clientes externos necesitan fechas para coordinar. Es un argumento lógico, sin fuente propia verificada.

## El roadmap cuando el cliente paga por fechas y alcance

Una consultora de software o una agencia de marketing digital vende un alcance y una fecha, firmados, y no resultados. Ahí el roadmap de resultados de la escuela choca con el contrato. Por qué el cliente compra entregables y no resultados está en [qué cambia en una consultora](../Fundamentos/que-es-producto.md#qué-cambia-en-una-consultora-que-vende-proyectos) (inferencia de esta base).

Los estudios de contratos no dan un ganador entre precio fijo y tiempo y materiales; el detalle está en [pricing y empaquetado](../Monetizacion/pricing-y-empaquetado.md#cómo-cobra-una-consultora-o-una-agencia).

La combinación que propone el informe de posición contraria de esta base, sin una fuente que la haya probado, es partir el roadmap: fechas para lo que está comprometido, resultados para el resto, o un apetito fijo al estilo de Shape Up. La distinción de Cagan entre roadmap y compromiso de fecha sirve de herramienta: un compromiso con fecha es una promesa cara y se hace después de descubrir lo suficiente, no antes. Elegir el tipo de contrato es también una decisión de precio; eso está en [Pricing y empaquetado](../Monetizacion/pricing-y-empaquetado.md).

> [!NOTE]
> Sin fuente todavía: cómo arma su roadmap una consultora que promete fechas a clientes. No se encontró ninguna fuente con método sobre el roadmap como promesa a un cliente.

## Cómo falla un roadmap

Falla cuando se vuelve una lista de pedidos con fecha: el equipo construye lo que dice la lista y nadie mira si movió algo. Falla también al revés, cuando "resultados" es la etiqueta de una lista que no cambió. Esas dos son lectura de esta base, sin fuente. Y falla cuando promete fechas que nadie estimó: para Cagan, esas fechas son deseos.

## Qué leer

"The Alternative to Roadmaps" de Cagan (2015) da la postura de la escuela en una página; la parte útil es la distinción entre roadmap y compromiso de fecha. Para la postura práctica, *Product Roadmaps Relaunched*, los capítulos de temas y de comunicación a clientes.
