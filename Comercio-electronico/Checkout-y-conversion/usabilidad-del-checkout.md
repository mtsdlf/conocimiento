---
resumen: >-
  La usabilidad del checkout es qué tan fácil le resulta a un comprador completar los pasos de datos, envío y pago sin trabarse ni abandonar. Casi todo lo que se sabe viene del Baymard Institute, que tiene un método cualitativo sólido, vende su investigación y no tiene auditoría independiente; ningún estudio revisado por pares confirma ni contradice sus guías principales.
estado: borrador
estabilidad: semi
fuentes:
  - "Baymard Institute, Current state of checkout UX, publicado el 13 de noviembre de 2024 y actualizado el 3 de noviembre de 2026: https://baymard.com/blog/current-state-of-checkout-ux (leído)"
  - "Baymard Institute, Ecommerce checkout usability report and benchmark, publicado el 21 de septiembre de 2016 y actualizado el 2 de febrero de 2025: https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark (leído)"
  - "Baymard Institute, Make Guest Checkout the Most Prominent Option, 17 de enero de 2023: https://baymard.com/blog/make-guest-checkout-prominent (leído)"
  - "Holst, One page checkouts, Baymard Institute, 26 de abril de 2011: https://baymard.com/blog/one-page-checkout (leído)"
  - "Baymard Institute, página de metodología de checkout: https://baymard.com/checkout-usability/methodology (según el vistazo; no se releyó)"
  - "Baymard Institute, Cart Abandonment Rate Statistics, actualizada el 28 de octubre de 2026: https://baymard.com/lists/cart-abandonment-rate (leído)"
  - "Stripe, guía sobre checkout de una página contra varios pasos: https://stripe.com/en-es/resources/more/one-page-checkout-vs-multistep-checkout (según resultados del buscador)"
  - "Comercio-electronico/.investigacion/checkout-y-conversion.md (sección 3)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (B4)"
  - "Comercio-electronico/.investigacion/vistazo.md (sección 4)"
aliases: [checkout usability, usabilidad del checkout, checkout UX, UX del checkout, guest checkout, compra como invitado, one-page checkout, checkout de una página]
creado: 2026-11-22
revisado:
---

# Usabilidad del checkout

La usabilidad del checkout es qué tan fácil le resulta a un comprador completar los pasos de datos, envío y pago sin trabarse ni abandonar. Casi todo lo que se sabe viene del Baymard Institute, que tiene un método cualitativo sólido, vende su investigación y no tiene auditoría independiente; ningún estudio revisado por pares confirma ni contradice sus guías principales.

Es la mirada que explica las causas observadas del [carrito abandonado](carrito-abandonado.md), donde están las causas declaradas. Las reglas generales de un formulario (etiquetas, validación en línea, cantidad de campos) están en [Formularios](../../UX/Interaccion/formularios.md); acá está lo propio del checkout.

## Cómo investiga Baymard

Baymard combina tests de usabilidad con auditorías de sitios. Según su informe de checkout (actualizado en 2025), hizo tests moderados uno a uno con "think aloud", en 272 sesiones (cada una, un participante en un sitio), un estudio de seguimiento ocular, dos rondas de benchmark sobre más de 850 pasos de checkout y nueve estudios cuantitativos con 11.777 participantes. De ahí salieron más de 2.700 problemas, condensados en 134 guías dentro de un informe de 718 páginas.

Su página de metodología, según un resumen que no se releyó, da otras cifras: 25 rondas de pruebas moderadas, 244 sitios puntuados y más de 110 guías de carrito y checkout. Justifica la muestra así: con 20 participantes se descubre en promedio el 95% de los problemas que aparecen en el 14% o más de los casos. Es la misma lógica que la regla de los cinco usuarios del [test de usabilidad](../../UX/Evaluacion/test-de-usabilidad.md), con más gente para encontrar problemas menos frecuentes.

Un test moderado descubre qué hace tropezar a la gente. No estima cuánto sube la conversión si se corrige. El vínculo entre una guía y la conversión, en Baymard, sale de promedios de sitios y de encuestas, no de experimentos.

## Lo que sostiene la investigación

En lo leído, cinco guías de Baymard traen evidencia publicada. La tabla las ordena por tipo de evidencia; que el costo visible o el teléfono sean guías con ese nombre es la lectura de esta base sobre la encuesta. Las cifras de cada una, con su fecha y su muestra, están en la [ficha de cifras](cifras-de-checkout-y-conversion.md).

| Guía | Qué la apoya | Tipo de evidencia |
|---|---|---|
| Mostrar pocos campos por defecto | el conteo de elementos de formulario en checkouts reales contra un flujo ideal; sitios que tropiezan con campos mal marcados | auditoría de sitios y tests |
| Destacar la compra como invitado | la cuenta obligatoria entre las razones de abandono; la parte de sitios que no la destaca | encuesta y auditoría de sitios |
| Dejar la creación de cuenta para la confirmación | la parte de sitios que la pide antes | auditoría de sitios |
| Mostrar costos de envío, impuestos y total antes de pagar | los costos extra, primera razón declarada de abandono; no poder ver el total | encuesta |
| Pedir solo los datos necesarios, como el teléfono | la resistencia declarada a dar el teléfono | encuesta |

Marcar bien qué campo es obligatorio y cuál opcional también cuenta, según el artículo de Baymard de 2026. Cuando solo los opcionales estaban marcados, una parte de los participantes saltó al menos un campo obligatorio. Usar un tipo de campo equivocado para un dato opcional alargó el tiempo del paso.

El estado general, según el benchmark de Baymard de 2026, es malo: la mayoría de los sitios de escritorio y de celular quedan en "mediocre" o peor, y muy pocos llegan a "good". El propio artículo avisa que Baymard está "retesting and verifying all of our existing Checkout research" y que publicará la versión revisada en el segundo trimestre de 2027. Sus cifras actuales están, por su propia cuenta, en revisión.

## Los límites de Baymard

Los límites salen del propio texto de Baymard. El informe no tiene una sección de limitaciones. Sus páginas se contradicen en cifras que deberían coincidir: 68,8% y 70,19% de abandono en un mismo artículo, 50 y 60 sitios, 134 y más de 110 guías, 59% y 65% de sitios mediocres o peores. La mejora de conversión que promete el rediseño, de 35,26%, es para el sitio grande promedio y se calcula sobre sitios como Walmart y Amazon; el mismo artículo dice que es más difícil de lograr de lo que sugiere el número.

Baymard vende el acceso a su base de investigación, y su benchmark califica sitios. Cada problema que reporta es parte de lo que vende. Eso no prueba que esté mal; es un motivo para pedir el método antes de citar una cifra. No se encontró ninguna auditoría independiente.

Fuera de Baymard, la evidencia es débil. No se encontró ningún estudio revisado por pares sobre la cantidad de campos del checkout ni sobre compra como invitado contra registro obligatorio. Lo que aparece son comparaciones de vendedores entre poblaciones distintas, o tests anecdóticos sin tamaño de muestra. Los estudios académicos de abandono coinciden en la dirección (la inconveniencia percibida predice el abandono), pero miden percepción con encuestas, no el efecto de cambiar un checkout.

## Una página o varios pasos

> [!IMPORTANT]
> Si un checkout de una sola página convierte más que uno de varios pasos no está resuelto. Holst, en Baymard (2011), sostiene que una página "won't necessarily perform better" que un checkout de varios pasos bien optimizado. Según él, los A/B que dan ganador a la página única comparan un checkout viejo sin optimizar contra uno nuevo optimizado. Su texto no trae tests ni cifras: es una opinión de 2011.
>
> Del otro lado hay casos sueltos: un test citado de segunda mano, detenido a las 606 transacciones, y el caso de un solo comercio publicado por una plataforma, sin grupo de control descrito. Ninguno se pudo verificar. Stripe, que vende pagos, recomienda probar con la propia audiencia porque no hay un diseño mejor para todos.
>
> Lo que esta base sostiene: no hay un estudio independiente que compare a igual cantidad de campos. Lo disponible sugiere que pesa lo que pide cada paso más que la cantidad de páginas.

## Al analizar el checkout de un competidor

Las guías de Baymard sirven como lista para auditar el checkout de una plataforma rival en una [evaluación heurística](../../UX/Evaluacion/evaluacion-heuristica.md): se recorre el flujo y se anota qué guías cumple. Ver a personas reales trabarse en cada checkout, con las mismas tareas, es una [evaluación competitiva](../../UX/Evaluacion/evaluacion-competitiva.md). Las guías completas de Baymard son de pago; sin ellas, se arma una lista propia con las cinco guías de arriba.

En una plataforma de tiendas, la mayoría de esas guías caen en lo que fija la plataforma, no en lo que configura cada comercio. Por eso la auditoría compara plataformas y no tiendas; el reparto está en [Checkout y conversión](checkout-y-conversion.md#qué-fija-la-plataforma-y-qué-configura-el-comercio). Para saber si una mejora detectada sube la conversión hace falta un [experimento A/B](../../Producto/Medicion/experimento-ab.md), que las guías no reemplazan.

> [!NOTE]
> Sin fuente todavía: estudios de usabilidad del checkout con compradores de Argentina o América Latina, donde pesan datos que Baymard no estudia, como el documento de identidad, los datos de factura y la elección de cuotas.

## Qué leer

- Baymard, [Current state of checkout UX](https://baymard.com/blog/current-state-of-checkout-ux) (actualizado el 3 de noviembre de 2026): el estado del benchmark y el aviso de que todo se está re-testeando. Fijate en las fechas y en qué cifras no traen tamaño de muestra.
- Baymard, [Ecommerce checkout usability report and benchmark](https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark) (actualizado en 2025): el método, con las sesiones, los estudios y las guías. Fijate en de dónde sale la mejora de 35,26%.
- Holst, [One page checkouts](https://baymard.com/blog/one-page-checkout) (2011): para la distinción entre cantidad de páginas y contenido de cada paso, no como evidencia.
