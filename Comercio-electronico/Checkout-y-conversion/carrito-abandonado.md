---
resumen: >-
  Un carrito abandonado es el de un comprador que agregó productos y no terminó la compra en esa sesión. La tasa de abandono se calcula como (1 − compras ÷ carritos creados) × 100, y no equivale a ventas perdidas: una parte de esos carritos es gente mirando o que compra después, en otra sesión o en otro canal.
estado: borrador
estabilidad: estable
fuentes:
  - "Baymard Institute, Cart Abandonment Rate Statistics, actualizada el 28 de octubre de 2026: https://baymard.com/lists/cart-abandonment-rate (leído)"
  - "Baymard Institute, Cart abandonment rate (artículo): https://baymard.com/blog/cart-abandonment-rate (leído)"
  - "Baymard Institute, Current state of checkout UX, actualizado el 3 de noviembre de 2026: https://baymard.com/blog/current-state-of-checkout-ux (leído)"
  - "Baymard Institute, Ecommerce checkout usability report and benchmark, publicado el 21 de septiembre de 2016 y actualizado el 2 de febrero de 2025: https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark (leído)"
  - "Littledata, Benchmarks, generado el 18 de noviembre de 2026: https://www.littledata.io/benchmarks (leído)"
  - "Rajamma, Paswan y Hossain (2009), Journal of Product & Brand Management 18(3):188-197, DOI 10.1108/10610420910957816: https://digitalcommons.fairfield.edu/business-facultypubs/205 (según su abstract)"
  - "Kukar-Kinney y Close (2010), Journal of the Academy of Marketing Science 38:240-250, DOI 10.1007/s11747-009-0141-5: https://link.springer.com/article/10.1007/s11747-009-0141-5 (según su resumen; acceso restringido)"
  - "Close, Kukar-Kinney y Benusa (2012), capítulo sobre abandono de carrito: https://scholarship.richmond.edu/marketing-faculty-publications/17/ (según su abstract)"
  - "Li, Luo, Lu y Moriguchi (2021), Does Retargeting Too Early Backfire? (en la AMA, Does Too Early Retargeting Backfire?), Journal of Marketing 85(4):123-140, DOI 10.1177/0022242920959043: https://journals.sagepub.com/doi/10.1177/0022242920959043 (según resultados del buscador y comunicados de la AMA)"
  - "Marketing Science Institute, informe 21-133: https://www.msi.org/wp-content/uploads/2021/09/MSI_Report_21-133-1.pdf (según resultados del buscador)"
  - "Comercio-electronico/.investigacion/checkout-y-conversion.md (sección 2)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (B4)"
aliases: [cart abandonment, abandono de carrito, tasa de abandono, shopping cart abandonment, carrito abandonado, recuperación de carritos, cart recovery]
creado: 2026-11-22
revisado:
---

# Carrito abandonado

Un carrito abandonado es el de un comprador que agregó productos y no terminó la compra en esa sesión. La tasa de abandono se calcula como (1 − compras ÷ carritos creados) × 100, y no equivale a ventas perdidas: una parte de esos carritos es gente mirando o que compra después, en otra sesión o en otro canal.

Es la caída más visible del [embudo de conversión](embudo-de-conversion.md), entre el carrito y la compra. Lo que se puede corregir de esa caída desde el diseño está en [usabilidad del checkout](usabilidad-del-checkout.md); acá están la cifra, lo que significa y lo que se sabe de recuperar esos carritos.

## Alrededor de 70%, y qué es esa cifra

Alrededor de 70% de los carritos creados no termina en compra, según el promedio que publica el Baymard Institute. Es la media simple de 50 estudios publicados entre 2006 y 2025, con un rango de 55% a 84%. Baymard no la midió: junta estudios de otros, varios de ellos de proveedores de software de recuperación de carritos. La cifra exacta, y las dos que dan otras páginas de la misma empresa, están en la [ficha de cifras](cifras-de-checkout-y-conversion.md).

Una media sin ponderar hace pesar igual a un estudio de 2006 y a uno de 2025, y a un panel chico y a uno grande. Baymard da la fórmula de abandono, pero no dice si cada estudio la usó. Por eso la cifra no describe a ninguna tienda en particular: es un orden de magnitud.

Un benchmark con definición propia da otra cifra. Littledata, que mide tiendas de una sola plataforma con su app instalada, define el abandono como las sesiones con carrito que no compraron, y su mediana sale más alta que el promedio de Baymard. Las dos cifras miden cosas distintas, y por eso no se restan ni se promedian.

## Por qué un carrito abandonado no es una venta perdida

Muchos carritos se usan para otra cosa que comprar en el momento. Kukar-Kinney y Close (2010), según el resumen de su artículo, encontraron que "many customers use online carts for entertainment or as a shopping research and organizational tool, which may induce them to buy at a later session or via another channel". También que los factores de búsqueda y consideración "play a larger role in cart abandonment than factors at the purchase decision stage".

Un capítulo posterior del mismo grupo (2012), según su abstract, distingue tres resultados: la compra, el abandono sin compra y el abandono para comprar en otro lado. De esa distinción se sigue, como inferencia de esta base, que solo el segundo resultado es una venta perdida para el mercado, y que el tercero lo es solo para esa tienda.

La encuesta de Baymard apunta en la misma dirección. Un 42% de los compradores online de Estados Unidos dice haber abandonado un carrito porque "I was just browsing / not ready to buy", algo que Baymard llama "largely unavoidable". Ese 42% es la parte de compradores que alguna vez abandonó por ese motivo, no la parte de carritos abandonados. No se puede multiplicar por la tasa de abandono para sacar cuánto es irrecuperable.

> [!IMPORTANT]
> Cuánto del abandono es recuperable está en disputa. Baymard calcula US$ 260.000 millones recuperables en Estados Unidos y la Unión Europea, multiplicando una mejora de conversión de 35,26% por las ventas online de esas regiones. Esa mejora sale de los problemas que encontró en sus pruebas, no se presenta como resultado de experimentos medidos y no explica cómo pasa de los sitios analizados, entre ellos Walmart y Amazon, a todo el mercado. Es la estimación del proveedor que vende la base de datos de guías.
>
> Del otro lado, una parte del abandono tiene causas de diseño que se pueden corregir, según las razones que declaran los compradores (sección siguiente).
>
> Lo que esta base sostiene: alrededor de 70% de los carritos creados no termina en compra; no es una pérdida, porque una parte es navegación o compra posterior, y el potencial de mejora por checkout es una estimación del proveedor. Nunca "se pierde el 70% de las ventas".

## Lo que los compradores dicen y lo que se observa

Las razones de abandono vienen de encuestas: son lo que la gente declara, no lo que se midió que causó el abandono. En la encuesta de Baymard, excluido el "solo estaba mirando", la razón más citada son los costos extra demasiado altos (envío, impuestos, tarifas), con 40%. Le siguen la entrega lenta, la desconfianza para dar la tarjeta, la obligación de crear una cuenta, un proceso largo o complicado, errores del sitio, la política de devoluciones, no ver el total antes, la tarjeta rechazada y pocos medios de pago. Los porcentajes de cada una están en la [ficha de cifras](cifras-de-checkout-y-conversion.md).

La encuesta tiene límites que hay que nombrar al citarla. La página no da el tamaño de la muestra ni el año. Las opciones las arma Baymard, la respuesta admite varias (suman más de 100%) y pregunta por los últimos tres meses. Para la cuenta obligatoria, otra página de Baymard da 24% (4.384 adultos de Estados Unidos, 2022) contra el 18% actual, sin explicar si son encuestas o definiciones distintas.

La literatura académica coincide en la dirección. Rajamma, Paswan y Hossain (2009), según su abstract, encuestaron a personas que habían comprado online en el último año y hallaron que "perceived transaction inconvenience is the major predictor of shopping cart abandonment". El riesgo percibido también predice el abandono. Los dos estudios académicos son encuestas de 2009 y 2010 en Estados Unidos, que miden percepción y no el efecto de un cambio concreto en el checkout.

Lo observado, en cambio, sale de los tests de usabilidad: qué hace tropezar a la gente mientras completa un checkout. Eso está en [usabilidad del checkout](usabilidad-del-checkout.md).

## Recuperar carritos: qué midieron los experimentos

La evidencia más sólida sobre recuperación es sobre anuncios de retargeting, no sobre emails. Li, Luo, Lu y Moriguchi (2021), según resultados del buscador y comunicados de la American Marketing Association, hicieron experimentos de campo al azar con más de 40.500 clientes. Un anuncio temprano, de 30 a 60 minutos después del abandono, bajó la probabilidad de compra frente al grupo de control. Uno tardío, de 24 a 72 horas después, tuvo un efecto incremental positivo. Un segundo experimento con más de 23.900 clientes de otra empresa lo replicó en parte.

Un informe del Marketing Science Institute (21-133), según resúmenes, encontró en otro experimento con un retailer que el efecto fue mayor en quienes habían abandonado hace poco y con carritos de una sola categoría.

Las cifras de recuperación que publican las plataformas de tiendas y las herramientas de email no son experimentos controlados. Un email que "recupera" un carrito puede llevarse el crédito de una compra que iba a ocurrir igual; es un razonamiento de esta base, no una medición. Medir eso pide un grupo de control, que es la idea de la [incrementalidad](../../Marketing/Medicion/incrementalidad.md); la recuperación como acción de marketing es parte de los [canales](../../Marketing/Canales/canales.md).

> [!NOTE]
> Sin fuente todavía: un experimento al azar revisado por pares sobre emails de carrito abandonado, y cualquier estudio de abandono en Argentina o América Latina. Del artículo de Kukar-Kinney y Close no se leyó el texto, solo el resumen; del de Rajamma y colegas, solo el abstract, sin tamaño de muestra.

## Al analizar una plataforma de tiendas competidora

La tasa de abandono que muestre o prometa bajar una plataforma no sirve para compararla con otra. Lo comparable es qué ofrece contra las causas declaradas: si muestra el costo de envío y el total antes del checkout, si permite comprar sin cuenta, qué medios de pago trae. También, si su función de recuperación de carritos mide contra un grupo de control o cuenta como recuperada toda compra posterior a un aviso. Lo que la plataforma fija y lo que el comercio configura está en [Checkout y conversión](checkout-y-conversion.md#qué-fija-la-plataforma-y-qué-configura-el-comercio).

## Qué leer

- Baymard, [Cart Abandonment Rate Statistics](https://baymard.com/lists/cart-abandonment-rate): la lista de estudios y la sección de razones. Fijate en que el "just browsing" queda excluido de los porcentajes y en que la tasa es una media simple de 50 estudios.
- Kukar-Kinney y Close (2010) y Rajamma y colegas (2009): la lectura académica. Conviene leer el texto completo, con acceso institucional, antes de citar sus números.
- Li y colegas (2021), en el Journal of Marketing: para recuperación. Fijate en la ventana de tiempo entre el abandono y el anuncio.
