---
resumen: >-
  Checkout y conversión es el tramo de una venta online que va desde que el comprador pone un producto en el carrito hasta que paga, y la medida de cuántos compradores lo completan. Se estudia con tres miradas: el embudo que lo mide, el abandono que muestra dónde se corta y la usabilidad que explica qué del diseño lo traba.
estado: borrador
estabilidad: estable
fuentes:
  - "Google, Measure ecommerce (GA4, guía para desarrolladores): https://developers.google.com/analytics/devguides/collection/ga4/ecommerce (leído)"
  - "Baymard Institute, Cart Abandonment Rate Statistics, actualizada el 28 de octubre de 2026: https://baymard.com/lists/cart-abandonment-rate (leído)"
  - "Baymard Institute, Current state of checkout UX, publicado el 13 de noviembre de 2024 y actualizado el 3 de noviembre de 2026: https://baymard.com/blog/current-state-of-checkout-ux (leído)"
  - "Shopify, Checkout (documentación para desarrolladores): https://shopify.dev/docs/apps/build/checkout (leído)"
  - "Tiendanube, centro de ayuda, opciones y códigos personalizados del checkout: https://ayuda.tiendanube.com/es_AR/123367-opciones-del-checkout/como-agregar-codigos-personalizados-en-el-checkout-de-mi-tiendanube (según resultados del buscador, no se abrió)"
  - "The Good, Ecommerce benchmarks: https://thegood.com/insights/ecommerce-benchmarks/ (leído)"
  - "Comercio-electronico/.investigacion/checkout-y-conversion.md"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (B3 y B4)"
  - "Comercio-electronico/.investigacion/vistazo.md"
aliases: [checkout, conversión, conversion, checkout and conversion, optimización de la conversión, CRO]
creado: 2026-11-22
revisado:
---

# Checkout y conversión

Checkout y conversión es el tramo de una venta online que va desde que el comprador pone un producto en el carrito hasta que paga, y la medida de cuántos compradores lo completan. Se estudia con tres miradas: el embudo que lo mide, el abandono que muestra dónde se corta y la usabilidad que explica qué del diseño lo traba.

El checkout son los pasos de datos, envío y pago. Este tramo recibe la tienda armada sobre una [plataforma de tiendas](../Plataforma-de-tiendas/plataforma-de-tiendas.md), que casi siempre trae el checkout hecho, y entrega una orden de cobro a [Pagos](../Pagos/pagos.md). Los medios de pago que ofrece, los datos fiscales que pide y lo que muestra antes de pagar salen también de la [Normativa](../Normativa/normativa.md) de cada país. Cómo se diseña un formulario en general está en [Formularios](../../UX/Interaccion/formularios.md); acá interesa el formulario que termina en una compra.

## Tres miradas sobre el mismo tramo

Las tres notas de la vertical miran el mismo recorrido desde lugares distintos. El campo no las separa así: el Baymard Institute, la fuente principal sobre checkout, cita su encuesta de razones de abandono y sus tests de usabilidad como un solo cuerpo de investigación.

| Mirada | Pregunta | Con qué evidencia |
|---|---|---|
| [Embudo de conversión](embudo-de-conversion.md) | ¿Cuántos pasan de cada etapa a la siguiente? | eventos de analítica que la tienda registra |
| [Carrito abandonado](carrito-abandonado.md) | ¿Cuántos se van con el carrito lleno, y por qué dicen que se van? | promedios de estudios de terceros y encuestas a compradores |
| [Usabilidad del checkout](usabilidad-del-checkout.md) | ¿Qué del diseño los hace tropezar? | tests de usabilidad moderados y auditorías de sitios |

El orden de lectura es ese. El embudo define las tasas, el abandono explica por qué una tasa alta no es toda pérdida, y la usabilidad dice qué se puede cambiar.

## Por qué las cifras de este tramo no se comparan entre fuentes

Una tasa de conversión sirve de orden de magnitud, no de vara de medir. Cada fuente divide por algo distinto (sesiones o visitantes), mide a sus propios clientes y elige su período. Según The Good, una consultora de optimización, las tasas reales suelen estar en "a low, single digit", y las cifras que publican los competidores son una versión pulida de las reales.

Por eso toda cifra de la vertical lleva su definición del denominador, su fuente, su tipo de tiendas y su fecha, y vive en una sola ficha: [cifras de checkout y conversión](cifras-de-checkout-y-conversion.md). Lo útil para un comercio es compararse con su propia historia y con su segmento. Ninguna cifra pública es "el promedio de la industria", porque ninguna fuente primaria publica método y muestra representativos del mercado.

El abandono tiene el mismo problema y uno más. La cifra de alrededor de 70% que más se repite es una media simple de 50 estudios de terceros, y una parte de esos carritos son compradores mirando o que compran después. Leerla como ventas perdidas es un error; el detalle está en [carrito abandonado](carrito-abandonado.md).

## Qué fija la plataforma y qué configura el comercio

En una plataforma alojada, la estructura del checkout la fija la plataforma. Decide la cantidad de pasos, su orden, los campos por defecto y el diseño. El comercio ajusta lo que la plataforma le abre: campos extra, textos, colores de marca y reglas como descuentos u ocultar un medio de pago.

Esa división sale de leer la documentación de dos plataformas de tiendas, una completa y otra por resultados del buscador; el detalle fechado está en [checkout por plataforma](checkout-por-plataforma.md). Que la regla valga para todas las plataformas alojadas es inferencia. En una de las dos, la ayuda dice que el checkout no se personaliza con CSS ni HTML "porque es un proceso seguro".

La consecuencia pesa al analizar el mercado. Las mejoras que la investigación de usabilidad señala (menos campos, compra como invitado, costos visibles antes de pagar) caen casi todas en la parte que fija la plataforma. Un comerciante individual no puede optimizarlas; la plataforma sí, para todas sus tiendas a la vez. Esto también es inferencia de esta base, no un hallazgo de una fuente.

## Cómo se compara el checkout de plataformas competidoras

Al analizar una plataforma de tiendas rival se compara la estructura del checkout y el reparto entre lo fijo y lo configurable. Las tasas de conversión que publica cada plataforma no sirven para eso: miden tiendas, tráfico y catálogos distintos.

1. Armá una tienda de prueba en cada plataforma y recorré el checkout como comprador, en escritorio y en celular. Es un [desarme de producto](../../Estrategia-competitiva/Analisis-de-competidores/desarme-de-producto.md) acotado a un flujo.
2. Contá los pasos y los elementos de formulario que aparecen por defecto, con el mismo criterio que usa Baymard (los valores de referencia están en la [ficha de cifras](cifras-de-checkout-y-conversion.md)).
3. Anotá si hay compra como invitado y cuán visible está, si el costo de envío y el total se ven antes de pagar, qué medios de pago y billeteras aparecen y qué datos locales pide (documento, datos de factura).
4. Separá qué es fijo y qué configurable, con la documentación para desarrolladores y el centro de ayuda de cada plataforma. Fijate qué cambia según el plan.
5. Si querés ver dónde se traban las personas, hacé una [evaluación competitiva](../../UX/Evaluacion/evaluacion-competitiva.md) con las mismas tareas en cada checkout, o una [evaluación heurística](../../UX/Evaluacion/evaluacion-heuristica.md) contra las guías de Baymard.
6. Leé las promesas de conversión ("hasta X% más") como afirmaciones de vendedor: pedí el método, contra qué se compara, el período y quién lo midió. Lo que no trae método no entra a la comparación.

> [!NOTE]
> Sin fuente todavía: evidencia sobre abandono y usabilidad del checkout en Argentina o América Latina. Todo lo que hay en la vertical se midió en Estados Unidos, Europa o el Reino Unido. Lo local (cuotas, billeteras, datos de factura) sale de [Pagos](../Pagos/pagos.md) y [Normativa](../Normativa/normativa.md), no de estudios de checkout.

## Lo que hay en la vertical

- [Embudo de conversión](embudo-de-conversion.md): las etapas del carrito al pago como eventos de analítica, las tasas que se calculan entre ellas y por qué el denominador cambia la cifra.
- [Carrito abandonado](carrito-abandonado.md): cuántos carritos no terminan en compra, por qué un carrito abandonado no es una venta perdida, qué dicen los compradores y qué se sabe de recuperarlos.
- [Usabilidad del checkout](usabilidad-del-checkout.md): lo que sostiene la investigación de Baymard (campos, compra como invitado, costos a la vista), cómo lo midió y sus límites.
- [Cifras de checkout y conversión](cifras-de-checkout-y-conversion.md): ficha con las tasas de conversión, de abandono y del benchmark de Baymard, cada una con fecha, muestra y quién la publica; consultada el 2026-11-22.
- [Checkout por plataforma](checkout-por-plataforma.md): ficha con lo que dos plataformas de tiendas dejan configurar del checkout y lo que fijan; consultada el 2026-11-22.
