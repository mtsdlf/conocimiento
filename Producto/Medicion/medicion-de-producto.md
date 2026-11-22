---
resumen: >-
  La medición es la parte de producto que dice si lo construido funciona: una métrica que resume el valor que reciben los usuarios, el momento en que un usuario nuevo llega a ese valor y los experimentos que separan lo que un cambio causa de lo que solo lo acompaña.
estado: vigente
estabilidad: estable
fuentes:
  - "Amplitude, What Makes a Good vs Bad North Star Metric: https://www.amplitude.com/blog/good-bad-north-star-metric"
  - "Rodden, Hutchinson y Fu, Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications, CHI 2010, pp. 2395-2398, DOI 10.1145/1753326.1753687 (solo abstract): https://research.google/pubs/pub36299/"
  - "Dave McClure, Startup Metrics for Pirates: AARRR!, Ignite Seattle 4 (solo la ficha): https://webarchive.library.unt.edu/dentonfracking/20141206040342/http://igniteshow.com/videos/startup-metrics-pirates-aarrr"
  - "Built In, AARRR (vía buscador): https://builtin.com/growth-hacking/aarrr; Shopify, AARRR metrics (vía buscador): https://www.shopify.com/blog/aarrr-metrics"
  - "Kohavi et al., Online Controlled Experiments at Large Scale, KDD 2013 (solo abstract): https://exp-platform.com/large-scale/"
  - "Producto/.investigacion/medicion-y-monetizacion.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmaciones 1 y 5)"
aliases: [métricas de producto, product metrics, product analytics, medir producto]
creado: 2026-11-22
revisado: 2026-11-22
---

# Medición

La medición es la parte de producto que dice si lo construido funciona: una métrica que resume el valor que reciben los usuarios, el momento en que un usuario nuevo llega a ese valor y los experimentos que separan lo que un cambio causa de lo que solo lo acompaña.

Cierra el ciclo del producto. [Planificación y entrega](../Planificacion-y-entrega/planificacion-y-entrega.md) pone algo en manos de la gente; la medición dice si movió algo, y lo que encuentra corrige la [estrategia](../Estrategia/estrategia.md). Mide los [resultados](../Estrategia/resultados-y-entregables.md) que la estrategia fijó, no los entregables. Una métrica que no se mueve vuelve al [descubrimiento](../Descubrimiento/descubrimiento.md) como una oportunidad para investigar.

## Por qué se mide después de lanzar

En los experimentos controlados de empresas con mucho tráfico, una parte grande de los cambios no mueve la métrica que buscaba mover, y el equipo no lo anticipa: según el abstract de Kohavi y otros (KDD 2013), "many ideas impact key metrics by 1% and are not well estimated a-priori". Si el equipo no puede predecir qué idea va a funcionar, tiene que comprobarlo (lectura de la base). Las cifras y sus límites están en [experimento A/B](experimento-ab.md); la idea, en la [entrada del tema](../producto.md#la-idea-que-cruza-todo-el-tema).

## Cuatro preguntas que contesta la medición

Cada pregunta tiene su herramienta. Las tres primeras viven en esta vertical; la cuarta usa la técnica de otro tema.

| Pregunta | Herramienta | Dónde |
|---|---|---|
| ¿El producto entrega valor, en conjunto? | Una métrica que lo resume y las métricas de entrada que el equipo mueve | [North Star](north-star.md) |
| ¿Los usuarios nuevos llegan al valor? | La acción o el umbral que marca la llegada | [Activación](activacion.md) |
| ¿Este cambio causó la diferencia? | Una prueba controlada con variantes al azar | [Experimento A/B](experimento-ab.md) |
| ¿Los usuarios siguen volviendo? | La retención por cohorte | [Retención](../../Datos/Retencion-y-churn/retencion.md), en Datos |

La North Star y la activación se miran juntas: la primera dice si el producto entrega valor y la segunda si los nuevos llegan a él. El experimento es la forma de saber si un cambio en cualquiera de las dos lo causó el equipo.

## HEART y AARRR, dos mapas para elegir métricas

Dos marcos se usan para no empezar de cero al elegir qué medir. Ambos son listas de categorías que ayudan a cubrir el producto entero.

HEART es de un equipo de Google: Rodden, Hutchinson y Fu lo publicaron en CHI 2010. Sus letras son Happiness, Engagement, Adoption, Retention y Task success. Según el abstract, el paper trae un proceso para pasar de metas a métricas y ejemplos de equipos de Google, y los autores esperan que otras organizaciones lo reusen. Mide la experiencia del usuario a escala, y por eso ya está en [métricas de UX](../../UX/Evaluacion/metricas-de-ux.md), donde se lee junto con las métricas de un test con personas.

AARRR es de Dave McClure: adquisición, activación, retención, referencia e ingresos. Es un embudo de crecimiento, del primer contacto al pago. Según una fuente se presentó en Ignite Seattle 4 en 2007; otra dice que el modelo es de principios de los 2000, así que la fecha está discutida. La adquisición y la referencia son de [Marketing](../../Marketing/Medicion/medicion.md); acá interesan la activación y la retención, que dependen del producto.

> [!NOTE]
> Sin fuente todavía: las definiciones literales de cada letra de HEART (solo se leyó el abstract) y las diapositivas de McClure (solo la ficha de la charla).

## Dónde termina la medición de producto

Cuatro vecinos miden cosas parecidas con otra pregunta. La medición de producto se queda con el valor que el producto entrega a quien ya llegó.

- La experiencia de uso, con test de usabilidad, SUS y NPS, la mide [UX](../../UX/Evaluacion/metricas-de-ux.md).
- Si un canal causa las ventas, si cada venta deja plata y qué métrica seguir según la etapa del negocio son de la [medición de Marketing](../../Marketing/Medicion/medicion.md): [incrementalidad](../../Marketing/Medicion/incrementalidad.md), [economía unitaria](../../Marketing/Medicion/economia-unitaria.md) y [una métrica que importa](../../Marketing/Medicion/metrica-que-importa.md).
- Cómo se arma una cohorte y cómo se calculan la retención y el churn es de [Datos](../../Datos/Retencion-y-churn/retencion-y-churn.md). Esta vertical usa esos números; no repite la técnica.
- Medir el avance de una empresa nueva, con métricas accionables y de vanidad, es la [contabilidad de la innovación](../../Emprender/Validacion/contabilidad-de-la-innovacion.md) de Emprender.

## Cómo falla una métrica de producto

Una métrica que se vuelve meta se desvía de lo que medía. Es la ley de Goodhart, cuyo origen y variantes están en [resultados y entregables](../Estrategia/resultados-y-entregables.md#goodhart-cuando-el-resultado-se-vuelve-meta).

La segunda falla es elegir un número que sube solo. Amplitude llama métricas de vanidad a las que "look great on the surface but don't translate to meaningful business outcomes". La tercera es querer un experimento donde no hay volumen: con poco tráfico, el método es otro (ver [experimento A/B](experimento-ab.md#cuando-un-experimento-no-sirve)).

> [!IMPORTANT]
> Medir resultados y no entregables es una recomendación de la escuela de Cagan, Perri y Torres, sin estudio que la compare con equipos que miden entregables. La versión prudente, según el informe de posición contraria: medir resultados además de entregables, con varias métricas (de resultado, de guarda y de calidad de datos) y revisarlas, sabiendo que cualquiera usada como meta se desvía.

## Lo que hay adentro de la medición

- [North Star](north-star.md): la métrica que resume el valor que los clientes reciben y sus métricas de entrada; qué la hace buena según Amplitude y dónde se discute.
- [Activación](activacion.md): cómo se encuentra el comportamiento temprano que separa a los usuarios que se quedan, y el mito de "7 amigos en 10 días".
- [Experimento A/B](experimento-ab.md): cuándo una prueba controlada dice qué causó un cambio, qué invalida un resultado y cuándo no sirve.

## Lo que falta de la medición

- Retención como métrica de producto: qué curva de retención indica que el producto entrega valor sostenido, a partir de la técnica de Datos.
