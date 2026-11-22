---
resumen: >-
  Un entregable es lo que un equipo produce, como una funcionalidad; un resultado es un cambio en lo que hacen los usuarios que le sirve al negocio. La escuela de equipos empoderados propone juzgar a los equipos por resultados, sin estudios que comparen y con el riesgo de que la métrica elegida se desvíe.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, Outcome Over Output: https://www.martinfowler.com/bliki/OutcomeOverOutput.html"
  - "Josh Seiden, Outcomes Over Output (2019), según su Medium: https://medium.com/@jseiden/whats-the-difference-between-user-outcomes-and-business-outcomes-588952071552"
  - "Will Larson, notas sobre Melissa Perri, Escaping the Build Trap (2018): https://lethain.com/notes-escaping-the-build-trap/"
  - "John Cutler, 12 Signs You're Working in a Feature Factory (2015/2016), según reseña: https://www.bram.us/2020/02/07/12-signs-youre-working-in-a-feature-factory/ ; seguimiento de 2019 en Amplitude: https://www.amplitude.com/blog/12-signs-youre-working-in-a-feature-factory-3-years-later"
  - "Marty Cagan, Outcomes Are Hard (SVPG): https://www.svpg.com/outcomes-are-hard/"
  - "Marty Cagan, The Alternative to Roadmaps (SVPG): https://www.svpg.com/the-alternative-to-roadmaps/"
  - "Marty Cagan, The Moral Case for the Product Model (SVPG): https://www.svpg.com/the-moral-case-for-the-product-model/"
  - "Ron Kohavi y Stefan Thomke, The Surprising Power of Online Experiments, HBR (2017), reimpresión R1705E: https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf"
  - "David Manheim y Scott Garrabrant, Categorizing Variants of Goodhart's Law (arXiv 1803.04585), según resumen: https://arxiv.org/abs/1803.04585"
  - "Producto/.investigacion/estrategia.md"
  - "Producto/.investigacion/posicion-contraria.md"
aliases: [outcome vs output, outcomes over output, resultados vs entregables, build trap, feature factory, fábrica de funcionalidades]
creado: 2026-11-22
revisado: 2026-11-22
---

# Resultados y entregables

Un entregable es lo que un equipo produce, como una funcionalidad; un resultado es un cambio en lo que hacen los usuarios que le sirve al negocio. La escuela de equipos empoderados propone juzgar a los equipos por resultados, sin estudios que comparen y con el riesgo de que la métrica elegida se desvíe.

En inglés se dice *output* y *outcome*. De esta distinción depende casi todo el tema [Producto](../producto.md): cómo se escribe la [estrategia](estrategia-de-producto.md), qué se le delega al [equipo](../Organizacion/equipo-empoderado.md), qué pone el [roadmap](../Planificacion-y-entrega/roadmap.md) y qué mide la [medición](../Medicion/medicion-de-producto.md).

## Tres niveles: entregable, resultado e impacto

Fowler distingue tres cosas. El entregable es lo que produce el equipo: funcionalidades, líneas de código, story points. El resultado es un cambio en cómo se comportan los usuarios o clientes que beneficia al negocio. El impacto son los efectos más amplios sobre la organización ("impacts"). Seiden, autor del libro *Outcomes Over Output*, define un resultado como "a change in human behavior that drives business results" (según su Medium; el libro no se leyó).

| Nivel | Qué es | Ejemplo en una plataforma de tiendas online |
|---|---|---|
| Entregable | Lo que el equipo construye y lanza | Un nuevo flujo de alta de comercios |
| Resultado | Lo que cambia en la conducta del usuario | Más comercios terminan el alta y cargan su primer producto |
| Impacto | Lo que cambia para el negocio | Más ingresos por suscripciones |

Torres y Seiden llaman "resultado de producto" (*product outcome*) al nivel del medio y "resultado de negocio" (*business outcome*) al que acá se llama impacto. En esta base, "resultado" a secas es el de producto.

Los ejemplos de la tabla son propios. Lectura de esta base: el resultado queda en el medio, más cerca del equipo que el impacto, aunque, como advierte Fowler más abajo, tampoco lo controla solo. La métrica que resume el valor entregado está en [north star](../Medicion/north-star.md).

## La build trap y la feature factory

Perri llama build trap a la empresa que mide el éxito por lo que lanza. Según las notas de Larson, en esa empresa "the number of features shipped becomes the primary metric of success", porque no entiende los problemas del cliente. El síntoma es tomar el envío como prueba de que se acertó.

Cutler describió el mismo problema como feature factory, la fábrica de funcionalidades. Su ensayo original, que las fuentes fechan en 2015 o en 2016, lista síntomas como no medir el impacto, festejar el envío, trabajar en lotes grandes y saltar de proyecto en proyecto (según una reseña; el original no apareció). En el seguimiento de 2019 Cutler matiza: "It is impossible to focus on outcomes when the house is burning", y propone medir para aprender y no para controlar.

## Por qué cuesta pasar a resultados

Cagan dice que la falla más común es querer el cambio sin cambiar el resto: "Far and away the single most common problem is thinking that you can move your organization to focus on outcomes" sin pasar al modelo de producto. Si el equipo recibe una lista de funcionalidades, pedirle resultados no cambia nada. También advierte que "the vast majority of KPIs are not helpful measures of successful outcomes", y que "When all you measure is project completion, it doesn't really matter if your goals are vague".

Sobre el roadmap, Cagan ve "typical product roadmaps as the source of so much waste in product teams". Propone calificar el roadmap pasado contando cuántos ítems lograron su objetivo, y no cuántos se entregaron.

## Por qué enviar no equivale a mejorar

La razón más fuerte para medir resultados viene de los experimentos controlados. En Microsoft, un tercio de las ideas probadas mejora la métrica, un tercio no la cambia y un tercio la empeora; en Google y Bing acierta entre 10% y 20% (Kohavi y Thomke, 2017; ver la [entrada del tema](../producto.md#la-idea-que-cruza-todo-el-tema)). Eso prueba que lanzar una funcionalidad no garantiza el resultado, pero no que gestionar por resultados rinda más que gestionar por entregables. Las cifras y sus límites están en [experimento A/B](../Medicion/experimento-ab.md).

> [!IMPORTANT]
> No se encontró ningún estudio comparativo ni causal que muestre que los equipos juzgados por resultados rindan más. Cagan mismo, en "The Moral Case for the Product Model", no da datos comparativos y recomienda pilotos. Lo más cercano es una correlación publicada por McKinsey entre madurez del modelo de producto y retorno al accionista (ver [la evidencia del modelo de producto](../Fundamentos/fuentes-de-producto.md#la-evidencia-del-modelo-de-producto)). Es una recomendación de escuela y no un hallazgo.

## Goodhart: cuando el resultado se vuelve meta

Medir resultados tiene su propio riesgo: la métrica deja de seguir a la meta en cuanto se premia. Manheim y Garrabrant atribuyen la idea a Goodhart (1975) y a Campbell (1979), y la fórmula "measure becomes a target" a Strathern (1997). Su taxonomía distingue dos problemas: elegir una métrica que siga a la meta y evitar que alguien juegue la brecha entre premio y meta. Sostienen que el problema es inevitable. Es un paper conceptual, leído por resumen, y no mide equipos de producto.

Fowler agrega salvedades: es difícil repartir el crédito entre equipos y factores, un equipo puede trabajar muy bien y parecer un fracaso si falla otra parte del sistema, y elegir bien el resultado requiere habilidad. Igual lo defiende, porque "you get what you try to measure".

> [!IMPORTANT]
> El mismo concepto tiene tres lecturas. Fowler: cuesta medirlo pero vale la pena. Cutler: "outcomes" se puede usar como control desde arriba ("Your 'outcome-focus' might be my 'top-down decision making'."). Cagan: los resultados solo funcionan dentro del modelo de producto. La lectura prudente, que propone el informe de posición contraria, es medir resultados además de entregables y usar varias métricas (de resultado, de guarda y de calidad de datos) que se revisan. Ninguna de las tres posiciones tiene estudio.

## Dónde no alcanza: consultoras y contratos

En una consultora de software o una agencia, el cliente compra entregables acotados con fecha, y el resultado de su negocio no lo controla quien construye; el argumento, una inferencia de esta base, está en [qué cambia en una consultora](../Fundamentos/que-es-producto.md#que-cambia-en-una-consultora-que-vende-proyectos). Un equipo puede medir resultados para aprender, pero el contrato se cumple con entregables. Cómo se combinan fechas comprometidas y resultados está en [roadmap](../Planificacion-y-entrega/roadmap.md).

## Qué leer

Para la definición, Fowler, "Outcome Over Output", corto y con las salvedades. Para las fallas, Cagan, "Outcomes Are Hard". Para la disputa, Cutler, "12 Signs... 3 Years Later", la parte donde dice que "outcome-focus" es un término disputado. El libro de Seiden, *Outcomes Over Output*, no se leyó.

Ver también: la idea de mirar [una sola métrica por etapa](../../Marketing/Medicion/metrica-que-importa.md), en Marketing.
