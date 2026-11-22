---
resumen: >-
  El embudo de conversión es la secuencia de etapas entre ver un producto y comprarlo, medida como la proporción de compradores que pasa de cada etapa a la siguiente. Las etapas son eventos que la tienda decide registrar y las tasas dependen de qué se pone en el denominador, así que dos tiendas pueden llamar igual a cifras distintas.
estado: vigente
estabilidad: estable
fuentes:
  - "Google, Measure ecommerce (GA4, guía para desarrolladores): https://developers.google.com/analytics/devguides/collection/ga4/ecommerce (leído)"
  - "Littledata, Benchmarks, generado el 18 de noviembre de 2026: https://www.littledata.io/benchmarks (leído)"
  - "eMarketer, ficha de Dynamic Yield y página de KPI de conversión: https://www.emarketer.com/data-providers/dynamic-yield y https://www.emarketer.com/industry-kpis/conversion-rate (según resultados del buscador)"
  - "The Good, Ecommerce benchmarks: https://thegood.com/insights/ecommerce-benchmarks/ (leído)"
  - "Growth Suite, artículo sobre compararse con los promedios de la industria, 21 de mayo de 2026: https://www.growthsuite.net/blog/the-problem-with-benchmarking-your-store-against-industry-averages (leído)"
  - "Comercio-electronico/.investigacion/checkout-y-conversion.md (sección 1)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (B3)"
aliases: [conversion funnel, embudo de compra, purchase funnel, tasa de conversión, conversion rate, checkout completion, tasa de finalización del checkout]
creado: 2026-11-22
revisado: 2026-11-22
---

# Embudo de conversión

El embudo de conversión es la secuencia de etapas entre ver un producto y comprarlo, medida como la proporción de compradores que pasa de cada etapa a la siguiente. Las etapas son eventos que la tienda decide registrar y las tasas dependen de qué se pone en el denominador, así que dos tiendas pueden llamar igual a cifras distintas.

Es la mirada que mide dentro de [Checkout y conversión](checkout-y-conversion.md). La caída entre el carrito y la compra es el [carrito abandonado](carrito-abandonado.md), y las causas de diseño de esa caída están en [usabilidad del checkout](usabilidad-del-checkout.md). Este embudo es el del comprador en una tienda. El embudo AARRR de crecimiento de un producto es otro, y su etapa de [activación](../../Producto/Medicion/activacion.md) mide si un usuario nuevo llega al valor, no si compra.

## Las etapas son eventos que la tienda registra

La guía de comercio electrónico de Google Analytics 4 (GA4) es la referencia más usada para nombrar las etapas. Recomienda esta secuencia de eventos: `view_item_list`, `select_item`, `view_item`, `add_to_cart`, `view_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info` y `purchase`.

| Evento | Qué marca, según Google |
|---|---|
| `view_item` | "whenever a user views an item's details screen" |
| `add_to_cart` | "an item being added to a shopping cart" |
| `begin_checkout` | "the first step in a checkout process" |
| `purchase` | una compra con uno o más productos; lleva un `transaction_id`, y los reembolsos van en un evento `refund` aparte |

Los eventos son recomendados, no obligatorios. Cada tienda, o la plataforma sobre la que está, decide cuáles envía y en qué momento. Qué cuenta como "el primer paso" del checkout depende de esa implementación, así que dos tiendas pueden medir la misma etapa con eventos distintos. Esto es inferencia de esta base; Google no lo dice.

## Las tasas que se calculan entre etapas

Entre las etapas se calculan varias tasas que en la conversación se mezclan. Littledata, un vendedor de analítica para tiendas, publica las definiciones por escrito, y son las que usa esta base:

| Tasa | Numerador sobre denominador |
|---|---|
| Conversión | sesiones con al menos una compra sobre sesiones totales |
| Agregado al carrito | la parte de las sesiones que agrega un producto al carrito (la definición literal no se copió) |
| Finalización del checkout | sesiones que compraron sobre sesiones que empezaron el checkout |
| Abandono de carrito | sesiones con carrito que no compraron sobre sesiones con carrito |

Los valores de cada tasa, con su muestra y su fecha, están en la [ficha de cifras](cifras-de-checkout-y-conversion.md).

La conversión mezcla tres cosas: la calidad del tráfico, el catálogo y el checkout. Una tienda con tráfico pago frío convierte menos que otra con clientes que vuelven, aunque tengan el mismo checkout. Para aislar el checkout sirve más la finalización del checkout, de checkout iniciado a compra, siempre que se sepa cómo se definió "iniciado".

## El denominador decide la cifra

La misma tienda da tasas distintas según divida por sesiones o por visitantes únicos. Si cada visitante tiene varias sesiones antes de comprar, la tasa por visitante sale más alta que la tasa por sesión. Una misma fuente puede usar las dos: según resúmenes de eMarketer, Dynamic Yield define la conversión como sesiones con compra sobre sesiones en una página, y como compras sobre visitantes en 12 meses en otra.

Las muestras tampoco se parecen. Cada benchmark mide a los clientes de quien lo publica: tiendas de una plataforma con una app instalada y un mínimo de tráfico, retailers grandes que compran personalización, o pymes de un país. Ninguna representa al mercado argentino. A eso se suman los sesgos de supervivencia (solo se miden tiendas activas), de rubro y de estacionalidad.

> [!IMPORTANT]
> Si los benchmarks de conversión sirven para compararse está en discusión. En contra: según The Good, una consultora de optimización, los competidores no tienen incentivos para publicar cifras precisas y no se sabe si calculan igual; por ejemplo, sumar ventas mayoristas a la conversión de la venta directa la infla. Growth Suite (21 de mayo de 2026) da el ejemplo de joyería con 0,8% y compra impulsiva con 6%, cuyo promedio de 3,4% "no describe a ninguna de las dos"; su autor vende una app de analítica y sus cifras no tienen fuente.
>
> A favor: The Good dice que el benchmark sirve para ubicar un orden de magnitud y para desconfiar de una cifra de dos dígitos. No hay evidencia de que los rangos publicados estén corridos en una dirección; el problema es la comparabilidad.
>
> Lo que esta base sostiene: una tasa de conversión sirve de orden de magnitud, no de vara de medir. Cada cifra lleva su denominador, su fuente, su tipo de tiendas y su fecha, y la comparación útil es contra la propia historia y el propio segmento.

## Qué causa un cambio en el embudo

El embudo muestra dónde cae la gente, no por qué. Una caída en la finalización del checkout puede venir de un cambio de diseño, de una campaña que trajo otro tráfico o de un medio de pago que dejó de andar. Para saber si un cambio del checkout causó una mejora hace falta un [experimento A/B](../../Producto/Medicion/experimento-ab.md) con grupos al azar, y eso exige un volumen de compras que una tienda chica no tiene.

## Al comparar plataformas de tiendas

Al analizar una plataforma de tiendas competidora, el embudo sirve para comparar qué mide cada una, no cuánto convierten sus tiendas. Se puede ver qué eventos envía la plataforma de fábrica a la herramienta de analítica, si distingue el inicio del checkout del agregado de envío y de pago, y qué tasas le muestra al comerciante en su panel. Una plataforma que solo muestra la conversión total deja al comerciante sin ver dónde se corta su checkout. La tasa de conversión publicada por la propia plataforma es una afirmación de vendedor; cómo se lee está en [Checkout y conversión](checkout-y-conversion.md#cómo-se-compara-el-checkout-de-plataformas-competidoras).

## Qué leer

- Google, [Measure ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce): la definición de cada evento y la secuencia recomendada. Fijate en qué eventos son recomendados y no obligatorios, y en qué campos lleva `purchase`.
- Littledata, [Benchmarks](https://www.littledata.io/benchmarks): el único benchmark leído que publica la definición de cada etapa y su muestra. Fijate en las definiciones por etapa y en el umbral mínimo de sesiones y compras, que deja afuera a las tiendas chicas.
