---
resumen: >-
  Las cifras de referencia de checkout y conversión (tasa de abandono, razones de abandono, tasas de conversión y benchmark de usabilidad del checkout), cada una con qué mide, su muestra, su fecha y quién la publica. Consultadas el 2026-11-22.
estado: borrador
estabilidad: volatil
fuentes:
  - "Baymard Institute, Cart Abandonment Rate Statistics, actualizada el 28 de octubre de 2026: https://baymard.com/lists/cart-abandonment-rate (leído)"
  - "Baymard Institute, Cart abandonment rate (artículo): https://baymard.com/blog/cart-abandonment-rate (leído)"
  - "Baymard Institute, Ecommerce checkout usability report and benchmark, publicado el 21 de septiembre de 2016 y actualizado el 2 de febrero de 2025: https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark (leído)"
  - "Baymard Institute, Current state of checkout UX, actualizado el 3 de noviembre de 2026: https://baymard.com/blog/current-state-of-checkout-ux (leído)"
  - "Baymard Institute, Make Guest Checkout the Most Prominent Option, 17 de enero de 2023: https://baymard.com/blog/make-guest-checkout-prominent (leído)"
  - "Baymard Institute, página de metodología de checkout: https://baymard.com/checkout-usability/methodology (según el vistazo; no se releyó)"
  - "Littledata, Benchmarks, generado el 18 de noviembre de 2026: https://www.littledata.io/benchmarks (leído)"
  - "eMarketer, ficha de Dynamic Yield: https://www.emarketer.com/data-providers/dynamic-yield (según resultados del buscador)"
  - "IRP Commerce: https://www.irpcommerce.com/en/ (sitio leído; cifras según notas de terceros)"
  - "Shopify, blog sobre checkout de una página: https://www.shopify.com/pk/enterprise/blog/one-page-checkout (según resultados del buscador)"
  - "Comercio-electronico/.investigacion/checkout-y-conversion.md"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (B3 y B4)"
  - "Comercio-electronico/.investigacion/vistazo.md (sección 4)"
aliases: [benchmarks de conversión, conversion benchmarks, cifras de abandono de carrito, cart abandonment statistics]
creado: 2026-11-22
revisado:
---

# Cifras de checkout y conversión

Las cifras de referencia de checkout y conversión (tasa de abandono, razones de abandono, tasas de conversión y benchmark de usabilidad del checkout), cada una con qué mide, su muestra, su fecha y quién la publica. Consultadas el 2026-11-22.

Sirven a las notas de [embudo de conversión](embudo-de-conversion.md), [carrito abandonado](carrito-abandonado.md) y [usabilidad del checkout](usabilidad-del-checkout.md). Ninguna es "el promedio de la industria": cada fuente mide a sus propios clientes, y todas las de esta ficha tienen interés comercial. Las páginas de Baymard, Littledata e IRP se actualizan seguido; las fechas son las que decía cada página el 2026-11-22.

## Tasa de abandono de carrito

| Cifra | Qué mide | Muestra y fecha de los datos | Quién la publica |
|---|---|---|---|
| 70,22% | media simple, sin ponderar, de las tasas de abandono de otros estudios; fórmula (1 − compras ÷ carritos creados) × 100, sin saber si cada estudio la usó | 50 estudios publicados entre 2006 y 2025, con rango de 55% a 84%; página actualizada el 28 de octubre de 2026 | Baymard Institute, que vende investigación de usabilidad; entre los estudios promediados hay proveedores de software de recuperación de carritos |
| 70,19% y 68,8% | la misma tasa, en otro artículo de la misma empresa | artículo de 2016 actualizado el 2 de febrero de 2025 | Baymard Institute |
| 79% (mediana) | sesiones con carrito que no compraron, sobre sesiones con carrito; el 10% mejor, 56%; el 10% peor, 94% | 449 tiendas de una sola plataforma que usan la app de Littledata, con 1.000 sesiones y 90 compras como mínimo; 17 de agosto al 14 de noviembre de 2026 | Littledata, vendedor de analítica |
| 77,81% | abandono de carrito | clientes de Dynamic Yield (retailers medianos y grandes); visto solo en notas de terceros | Dynamic Yield, que vende personalización y es de Mastercard, según eMarketer |

Las tres de Baymard no coinciden entre sí y la empresa no explica por qué.

## Razones de abandono declaradas

Encuesta de Baymard a compradores online de Estados Unidos, publicada en su [lista de abandono](https://baymard.com/lists/cart-abandonment-rate). La página no da el tamaño de la muestra ni el año ("our latest quantitative study"); las URL citan "GC049/GC050" con "March 2026" como parámetro, sin explicarlo. La respuesta admite varias opciones y pregunta por los últimos tres meses.

Un 42% abandonó alguna vez porque "I was just browsing / not ready to buy". Los porcentajes de la tabla dejan afuera a ese grupo.

| Razón (literal) | % |
|---|---|
| Extra costs too high (shipping, tax, fees) | 40 |
| Delivery was too slow | 20 |
| I didn't trust the site with my credit card information | 19 |
| The site wanted me to create an account | 18 |
| Too long / complicated checkout process | 17 |
| Website had errors / crashed | 17 |
| Returns policy wasn't satisfactory | 13 |
| I couldn't see / calculate total order cost up-front | 12 |
| The credit card was declined | 10 |
| There weren't enough payment methods | 9 |
| I don't know | 7 |

Otras cifras de Baymard para razones parecidas, que no coinciden con la tabla:

| Cifra | Qué mide | Muestra y fecha |
|---|---|---|
| 24% | abandonó en el último trimestre solo por tener que crear una cuenta | 4.384 adultos de Estados Unidos, 2022 |
| 17% | abandonó por un checkout largo o complicado en los últimos tres meses | "1,000+" encuestados, artículo actualizado en 2026; es el único tamaño de muestra que aparece |
| 26% y 22% | abandono por complejidad, en otras páginas de Baymard | según el buscador; recogidas en [Formularios](../../UX/Interaccion/formularios.md) |

## Tasa de conversión

| Cifra | Qué mide | Muestra y fecha de los datos | Quién la publica |
|---|---|---|---|
| 1,4% (mediana) | sesiones con al menos una compra sobre sesiones totales; el 20% mejor, sobre 2,8%; el 10% mejor, 3,8% o más; el 20% peor, bajo 0,5% | las 449 tiendas de Littledata, 17 de agosto al 14 de noviembre de 2026; generado el 18 de noviembre de 2026 | Littledata, vendedor de analítica |
| 7,1% (mediana) | agregado al carrito; el 10% mejor, 18% | ídem | Littledata |
| 46% (mediana) | finalización del checkout: de las sesiones que empezaron el checkout, las que compraron; el 10% peor, 14%; el 10% mejor, 73% | ídem | Littledata |
| 66% (mediana) | parte del tráfico que llega desde el celular | ídem | Littledata |
| 2,72% y 2,66% | conversión global, 12 meses móviles; la segunda, en una actualización de junio de 2026 | panel de "200+ million unique users across 300 million anonymized sessions" de clientes de Dynamic Yield; vistas solo en notas de terceros | Dynamic Yield; eMarketer avisa que "broader industry metrics may vary" |
| 1,70% a 2,26% | transacciones sobre sesiones, según las notas que lo citan: 1,70% en abril de 2026; para junio de 2026, 2,03% en una nota y 1,70% en otras; 2,26% en julio; 1,97% en septiembre (1,68% un año antes); 1,8% para 2025 | comercios en su mayoría del Reino Unido e Irlanda, pymes y medianos; el sitio no publica muestra ni definición | IRP Commerce, que vende servicios a comercios; sin método verificable |
| "hasta 36%" mejor conversión | conversión del checkout de la plataforma, sin decir contra qué | estudio de una consultora sin nombre, sin método publicado | Shopify, sobre su propio producto; el mismo blog atribuye al estudio que Shop Pay sube la conversión 5% y hasta 50% frente a la compra como invitado |

Otras bandas que circulan, todas vistas solo en resúmenes del buscador: 1,4% a 3,0% (una guía de 2026), 1% a 4% (Adobe, guía antigua), 2,2% en el primer trimestre de 2023 (Monetate) y una mediana de tienda Shopify de 1,5% atribuida a Littledata, que no coincide con el 1,4% de su página.

## Benchmark de usabilidad del checkout

| Cifra | Qué mide | Fecha | Fuente |
|---|---|---|---|
| 23,48 elementos (14,88 si se cuentan solo campos) | elementos de formulario que muestra por defecto el checkout promedio de Estados Unidos | artículo actualizado en 2025; la página de 2026 no repite el promedio | Baymard, informe y benchmark |
| unos 12 elementos | los que tiene un flujo ideal; muchos checkouts podrían bajar entre 20% y 60% | ídem | ídem |
| 11,3 campos; 8 alcanzan | campos promedio en 2024 y los que necesita la mayoría de los sitios | 26 de junio de 2024 | Baymard, según [Formularios](../../UX/Interaccion/formularios.md) |
| 59% mediocre o peor | sitios de escritorio y celular; 2% de los de escritorio y 1% de los de celular son "good"; 15% "poor" o peor; en apps, 60% mediocre o peor | actualizado el 3 de noviembre de 2026; base de "44,000+ checkout usability scores", sin cantidad de sitios | Baymard, estado actual |
| 65% mediocre o peor | la misma calificación en otra página | sin releer | Baymard, según el vistazo |
| 47% | sitios que no destacan la compra como invitado | 17 de enero de 2023, sin muestra | Baymard |
| 62% | la misma tasa en una versión más nueva | según el buscador, sin leer | Baymard |
| 56% | sitios que piden crear la cuenta antes del paso de confirmación | 2026 | Baymard, estado actual |
| 68% | compradores que se resisten a dar el teléfono | encuesta GC049, marzo de 2026 | ídem |
| 32% | participantes que saltaron un campo obligatorio cuando solo los opcionales estaban marcados | 2026 | ídem |
| 5% a 30% | tiempo extra de un paso por usar un tipo de campo equivocado en datos opcionales | 2026 | ídem |
| 35,26% | mejora de conversión posible para el sitio grande promedio con un rediseño del checkout; estimación sobre sitios como Walmart y Amazon, no medida en experimentos | artículo actualizado en 2025 | Baymard |
| US$ 260.000 millones | ventas recuperables en Estados Unidos y la Unión Europea: el 35,26% por US$ 738.000 millones de ventas online | ídem | Baymard |

Los dos conteos de campos no se pueden conciliar con lo leído: 14,88 campos en el artículo actualizado en 2025 y 11,3 en el de 2024. Puede que cuenten cosas distintas (por defecto o en total); es una hipótesis sin verificar. Baymard declara que re-testea toda su investigación de checkout y publicará la versión revisada en el segundo trimestre de 2027.

El método detrás de estas cifras, con sus propias discrepancias (272 sesiones y 134 guías en un artículo; 25 rondas, 244 sitios y más de 110 guías en la página de metodología), está en [usabilidad del checkout](usabilidad-del-checkout.md#cómo-investiga-baymard).
