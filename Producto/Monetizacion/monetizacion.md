---
resumen: >-
  La monetización es la parte de producto que decide cómo cobra el producto: por qué unidad se cobra, qué entra en cada plan y qué se regala para vender el resto. La escuela que más se cita sostiene que el precio se diseña junto con el producto y no al final, una tesis de practicantes sin estudio independiente.
estado: vigente
estabilidad: estable
fuentes:
  - "Madhavan Ramanujam y Georg Tacke, Monetizing Innovation (Wiley, 2016), índice: https://ebooks.mpdl.mpg.de/ebooks/Record/EB001935873/TOC"
  - "First Round Review, It's price before product, period (entrevista a Ramanujam): https://review.firstround.com/its-price-before-product-period"
  - "Yevgeniy Brikman, reseña de Monetizing Innovation (vía buscador): https://www.ybrikman.com/blog/2023/04/01/monetizing-innovation/"
  - "TechCrunch sobre la encuesta de OpenView de 2023 (vía buscador): https://techcrunch.com/2023/02/02/usage-based-pricing-is-rising-but-not-replacing-other-models/"
  - "Lenny Rachitsky y Kyle Poyar, What is a good free-to-paid conversion rate? (parte pública): https://lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion"
  - "Producto/.investigacion/medicion-y-monetizacion.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmación 7)"
aliases: [monetization, monetizar, modelo de precios, pricing de producto]
creado: 2026-11-22
revisado: 2026-11-22
---

# Monetización

La monetización es la parte de producto que decide cómo cobra el producto: por qué unidad se cobra, qué entra en cada plan y qué se regala para vender el resto. La escuela que más se cita sostiene que el precio se diseña junto con el producto y no al final, una tesis de practicantes sin estudio independiente.

La monetización cruza todo el ciclo y no es una etapa. Lo que el producto puede cobrar condiciona qué conviene construir en el [descubrimiento](../Descubrimiento/descubrimiento.md): una idea que nadie pagaría falla en el riesgo de viabilidad de los [cuatro riesgos](../Descubrimiento/cuatro-riesgos.md). Si el precio funciona se ve en la [medición](../Medicion/medicion-de-producto.md), en cuántos usuarios llegan a pagar y cuántos siguen.

## El precio antes que el producto

La tesis que domina la vertical es de *Monetizing Innovation* (Ramanujam y Tacke, 2016): "Most companies postpone pricing decisions until after the product is developed". El libro propone lo contrario: preguntar la disposición a pagar al principio y diseñar el producto alrededor del precio. Como argumento usa una cifra de su consultora, según la cual, en la versión de la entrevista, el 72% de las innovaciones no cumplió sus metas de ingresos o de ganancia, o fracasó del todo; la cita exacta y sus variantes están en [pricing y empaquetado](pricing-y-empaquetado.md).

> [!IMPORTANT]
> Que el precio se diseñe junto con el producto es opinión de practicantes: el libro y la consultora de precios que lo promueve, con interés comercial en la tesis. No se encontró un estudio independiente ni una crítica publicada. La reseña de Brikman señala el límite más claro: el método supone que el cliente puede expresar cuánto valora algo que todavía no tiene. La lectura prudente, según el informe de posición contraria: pensar el precio y el empaquetado desde el diseño es una recomendación razonable de una escuela, no un hallazgo.

## Tres decisiones de monetización

Cobrar un producto de software se reduce a tres decisiones, cada una con su nota:

| Decisión | Qué se elige | Dónde |
|---|---|---|
| La unidad de cobro | Por asiento, por uso o por resultado: la métrica de valor | [Pricing y empaquetado](pricing-y-empaquetado.md) |
| Los planes | Qué funciones y límites entran en cada uno, y para qué segmento | [Pricing y empaquetado](pricing-y-empaquetado.md) |
| Lo que se regala | Una versión gratis para siempre, una prueba por tiempo, o nada | [Freemium y prueba gratuita](freemium-y-prueba-gratuita.md) |

Las tres se tocan. Wes Bush sostiene, según resúmenes de su blog, que importa menos elegir entre freemium y prueba que decidir qué se incluye gratis y si el usuario llega al valor, que es la [activación](../Medicion/activacion.md). La forma de saber si un cambio de precio funcionó es la misma que para cualquier cambio: medirlo, con un [experimento](../Medicion/experimento-ab.md) si hay volumen.

## Cuando no hay producto empaquetado: servicios y plataformas

La tesis cambia de sentido fuera del SaaS. En una consultora o una agencia, el precio lo fija el contrato: precio fijo o tiempo y materiales, y lo que se decide es quién carga con el riesgo. Lo que dicen los estudios de contratos está en [pricing y empaquetado](pricing-y-empaquetado.md#como-cobra-una-consultora-o-una-agencia).

En una plataforma de dos lados, el precio es además una palanca para equilibrar los lados: a cuál se le cobra comisión y a cuál se subsidia. Eso es de [mercado de dos lados](../Plataformas/mercado-de-dos-lados.md), en Plataformas.

## Dónde termina la monetización

Tres vecinos tratan el dinero con otra pregunta.

- Qué modelo de ingreso tiene una empresa nueva (suscripción, freemium, hoja y afeitadora) y el precio como hipótesis a validar son del [modelo de negocio](../../Emprender/Modelo-de-negocio/modelo-de-negocio.md), en Emprender. Acá se decide cómo cobra un producto que ya existe.
- Si cada cliente deja plata después de lo que costó conseguirlo, con el LTV, el CAC y el payback, es la [economía unitaria](../../Marketing/Medicion/economia-unitaria.md), en Marketing. El precio entra en esas cuentas; las cuentas no se repiten acá.
- El product-led growth como canal de adquisición es de [Marketing](../../Marketing/Canales/growth-y-product-led-growth.md). Acá solo se decide qué se regala.

## De dónde salen los datos de precios

Casi toda la evidencia de esta vertical es de SaaS B2B financiado por capital de riesgo. La encuesta de precio por uso es de un fondo de inversión, OpenView, a empresas SaaS. Los benchmarks de conversión de Rachitsky y Poyar declaran estar "focused on B2B SaaS". Una pyme, una agencia o una tienda online no están en esas muestras.

> [!NOTE]
> Sin fuente todavía: evidencia sobre precios en pymes, agencias y consultoras, y estudios de freemium en comercio electrónico o en ecosistemas de apps.

## Lo que hay adentro de la monetización

- [Pricing y empaquetado](pricing-y-empaquetado.md): la tesis de *Monetizing Innovation* y su cifra, la métrica de valor, el precio por uso con los datos de OpenView y cómo cobra una consultora o una agencia.
- [Freemium y prueba gratuita](freemium-y-prueba-gratuita.md): qué convierte cada modelo según Rachitsky y Poyar, la discrepancia entre fuentes y cuánto regalar.
- [Precios de la competencia](precios-de-la-competencia.md): el precio del rival como alternativa más cercana en el método de valor económico, cómo se comparan planes, el precio de referencia y las guerras de precios.

## Lo que falta de la monetización

- Van Westendorp y cómo medir la disposición a pagar: las cuatro preguntas, la extensión de Newton, Miller y Smith y sus críticas, con fuente primaria.
- El precio de las apps en un ecosistema: cómo cobran los desarrolladores de terceros dentro de una plataforma y qué parte se queda la plataforma.
