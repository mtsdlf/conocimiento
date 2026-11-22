---
resumen: >-
  Las apps para comerciantes son productos de terceros que un comercio instala en su tienda, desde la tienda de apps de su plataforma, para sumar lo que la plataforma no trae: analítica y rentabilidad, marketing, atribución de anuncios y otras funciones. Viven de la base de comercios de la plataforma, cobran casi siempre según el tamaño del comercio y dependen de reglas que la plataforma puede cambiar o de una función que puede copiar.
estado: borrador
estabilidad: estable
fuentes:
  - "Escalafy, sitio y precios: https://www.escalafy.com/en y https://www.escalafy.com/en/pricing (leídos, consultados el 2026-11-22; fuente propia de la empresa)"
  - "Escalafy en la tienda de apps de Shopify: https://apps.shopify.com/escalafy (leída, consultada el 2026-11-22)"
  - "Escalafy en la tienda de aplicaciones de Tiendanube: https://www.tiendanube.com/mx/tienda-aplicaciones-nube/escalafy (leída, consultada el 2026-11-22)"
  - "Fichas de la tienda de apps de Shopify de BeProfit, TrueProfit, Polar Analytics y Peel: https://apps.shopify.com/beprofit-profit-tracker, https://apps.shopify.com/trueprofit, https://apps.shopify.com/polar-analytics, https://apps.shopify.com/peel-insights (leídas, consultadas el 2026-11-22)"
  - "Northbeam, pricing: https://www.northbeam.io/pricing (leída, consultada el 2026-11-22)"
  - "Tiendanube, tienda de aplicaciones: https://www.tiendanube.com/tienda-aplicaciones-nube (leída; la categoría Estadísticas no listó apps)"
  - "Tiendanube, planes y precios: https://www.tiendanube.com/planes-y-precios (leída, consultada el 2026-11-22)"
  - "Tiendanube, API documentation, introducción: https://tiendanube.github.io/api-documentation/intro (leída)"
  - "Comercio-electronico/.investigacion/huecos-plataformas.md (sección 4)"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md (sección 6)"
aliases: [apps para tiendas online, apps de Shopify, aplicaciones de Tiendanube, merchant apps, app store, tienda de apps, extensiones, plugins, apps de rentabilidad, profit analytics]
creado: 2026-11-22
revisado:
---

# Apps para comerciantes

Las apps para comerciantes son productos de terceros que un comercio instala en su tienda, desde la tienda de apps de su plataforma, para sumar lo que la plataforma no trae: analítica y rentabilidad, marketing, atribución de anuncios y otras funciones. Viven de la base de comercios de la plataforma, cobran casi siempre según el tamaño del comercio y dependen de reglas que la plataforma puede cambiar o de una función que puede copiar.

Son el tercer lado de la plataforma: los desarrolladores vienen porque hay comercios, y los comercios se quedan porque las apps resuelven lo que falta. La teoría de ese lado (cuánto abre la plataforma, cuánto cobra y por qué) está en [ecosistema de terceros](../../Producto/Plataformas/ecosistema-de-terceros.md). Cómo se conecta técnicamente una app, con OAuth, APIs, webhooks y límites de uso, está en [arquitectura de una plataforma](arquitectura-de-plataforma.md#la-tienda-de-apps-y-la-instalacion-de-una-app).

## Qué resuelven las apps

Las apps llenan lo que la plataforma no trae o trae en un plan más caro. Los informes relevaron sobre todo la analítica de rentabilidad y atribución, la clase de [Escalafy](escalafy.md), el ejemplo de esta vertical.

| Tipo | Qué resuelve | Ejemplos en los informes |
|---|---|---|
| Analítica de rentabilidad | juntar ventas, costos y gasto en publicidad para ver la ganancia real por canal, producto y pedido | Escalafy, BeProfit, TrueProfit |
| Analítica de datos y de retención | tableros con los datos de la marca y con la retención de sus clientes | Polar Analytics, Peel |
| Atribución de marketing | saber qué anuncio originó cada venta y devolver ese dato a las redes de anuncios | Northbeam; el Pixel de Escalafy |
| Marketing y canales | conectar la tienda con redes, anuncios y email | Pinterest en Tiendanube; Klaviyo y Perfit, como integraciones de Escalafy |
| Envíos, facturación, atención | etiquetas, cálculo de envío, comprobantes, chat | sin relevar |

> [!NOTE] Sin fuente todavía: la tabla es una lectura de esta base. Faltan las categorías de las tiendas de apps de Shopify y de Tiendanube (la categoría "Estadísticas" de Tiendanube no listó apps) y ejemplos de apps de envíos, facturación y atención.

Una app puede vivir en varias plataformas a la vez. Escalafy se conecta a Shopify, a Tiendanube y a Mercado Libre, según su sitio. De las alternativas relevadas, los informes solo registraron su ficha en la tienda de Shopify; Northbeam, en sus planes más caros, funciona con cualquier plataforma. Estar en varias plataformas es lo que más protege a una app cuando la suya entra a su espacio (ver abajo).

## Cómo cobran: por pedidos, por GMV, por gasto en anuncios

Casi todas las apps relevadas cobran una suscripción mensual que escala con el tamaño del comercio. Lo que cambia es la unidad con que miden ese tamaño, que es la métrica de valor de [pricing y empaquetado](../../Producto/Monetizacion/pricing-y-empaquetado.md#la-metrica-de-valor-por-que-unidad-se-cobra).

| Unidad de cobro | Cómo funciona | Ejemplos |
|---|---|---|
| Pedidos del mes | el precio sigue la cantidad de pedidos: "The price follows your orders for the month. Sell less, pay less." | Escalafy |
| Plan con tope de pedidos y cargo por pedido extra | un plan incluye cierta cantidad; lo que pasa se cobra por pedido, con un máximo | BeProfit, TrueProfit |
| Tramo de pedidos mensuales | planes por bandas de pedidos | Peel |
| GMV | "Pricing based on online GMV" | Polar Analytics |
| Gasto en publicidad y volumen de datos | tramos por cuánto invierte el comercio en anuncios y cuántas páginas vistas procesa | Northbeam |

La mayoría tiene un plan gratis con tope bajo, una prueba gratis o las dos cosas. Los precios y los topes están en [la ficha de Escalafy](escalafy.md) y en [apps de rentabilidad](apps-de-rentabilidad.md).

Cobrar por pedidos o por GMV ata el precio de la app al tamaño del comercio, igual que la plataforma ata su ingreso al GMV (ver [el negocio de una plataforma](negocio-de-una-plataforma.md)). Esto es lectura de esta base. La unidad también separa segmentos: una app que cobra por pedidos puede empezar gratis con un emprendedor, y una que arranca con un piso alto atiende solo a comercios grandes.

## Qué parte se queda la plataforma

La plataforma cobra una comisión sobre lo que los desarrolladores facturan a los comercios por la tienda de apps. Las reglas de Shopify, con su umbral de ingresos sin comisión y su tasa, están en [ecosistema de terceros](../../Producto/Plataformas/ecosistema-de-terceros.md#el-reparto-de-ingresos-con-los-desarrolladores), y no se repiten acá.

> [!NOTE] Sin fuente todavía: la comisión que cobra Tiendanube a los desarrolladores de su tienda de aplicaciones. Los informes no la relevaron.

Las reglas técnicas también cuestan: las versiones de la API vencen y obligan a migrar, y si el comercio deja de pagar, la plataforma corta el acceso de la app (ver [arquitectura de una plataforma](arquitectura-de-plataforma.md#versionado-el-calendario-que-sigue-quien-construye-encima)).

## Cómo se mide la presencia de una app, y por qué cuesta

Las tiendas de apps muestran reseñas y puntaje, pero no instalaciones: ninguna ficha relevada de Shopify las mostró, y las apps no publican cuántos comercios pagan. Medir la presencia de una app es juntar señales débiles.

| Señal | Qué dice | Su límite |
|---|---|---|
| Cantidad de reseñas | cuántos comercios se tomaron el trabajo de opinar | no es la cantidad de instalaciones; se acumula con el tiempo, así que una app nueva tiene pocas aunque crezca rápido |
| Puntaje | si quienes opinan están conformes | se concentra cerca del máximo: las cinco apps relevadas con puntaje tienen entre 4,5 y 5,0 |
| Comercios que la app dice tener | el tamaño que la app declara | sin definición ni auditoría |
| Fecha de lanzamiento en la tienda | cuánto tiempo lleva acumulando reseñas | no es la edad de la empresa |

Escalafy muestra los límites. Su sitio declara marcas conectadas sin definir "conectada", y su ficha en Shopify daba una cifra mucho menor. Sus reseñas en Shopify y en Tiendanube no suman lo que dice su sitio, y en Tiendanube todas son de 5 estrellas. Las cifras están en [la ficha de Escalafy](escalafy.md).

La regla práctica, de esta base: comparar reseñas solo dentro de una misma tienda de apps, con la fecha de lanzamiento al lado, y tratar las cifras que publica la app como lo que dice de sí misma.

## El riesgo de que la plataforma absorba la función

El riesgo mayor de una app es que la plataforma lance la misma función como propia. Los estudios con datos de Amazon, Android y la App Store, y qué hacen los terceros cuando la plataforma entra, están en [competencia con la plataforma](../../Producto/Plataformas/competencia-con-la-plataforma.md). La teoría del envolvimiento está en [ecosistema de terceros](../../Producto/Plataformas/ecosistema-de-terceros.md#cuando-la-plataforma-absorbe-lo-que-hicieron-otros).

En analítica, la superposición ya existe. Tiendanube incluye "estadísticas avanzadas" en uno de sus planes altos, según su página de planes, y una app de rentabilidad compite con eso. Lo que esa función nativa cubre y lo que no, no se relevó. La plataforma, además, ve los datos de todas las tiendas, una ventaja que ya fue objeto de regulación en el caso de un marketplace.

La defensa que sugieren los estudios es tener otra plataforma adonde ir. Una app que cruza varias plataformas, como Escalafy con Shopify, Tiendanube y Mercado Libre, ofrece algo que ninguna plataforma da sola: ver juntos los canales del comercio. Esto es inferencia de esta base, no un dato medido.

## Cómo se usa al analizar una app o su mercado

Para un SaaS que piensa construir una app para comerciantes, el análisis tiene dos frentes de competidores. Uno son las otras apps de la misma función; el otro, la plataforma misma, que entra en la lista como competidor potencial, en el sentido de [identificación de competidores](../../Estrategia-competitiva/Analisis-de-competidores/identificacion-de-competidores.md).

1. Listá las apps de la función en cada tienda de apps, con plataformas que cubren, unidad de cobro, precio de entrada, reseñas y fecha de lanzamiento. [Apps de rentabilidad](apps-de-rentabilidad.md) es un ejemplo hecho.
2. Mirá qué trae la plataforma de esa función y en qué plan.
3. Leé la comisión de la tienda de apps y la política de versiones: son costos fijos de estar ahí.
4. Medí cuánto del mercado propio depende de una sola plataforma.

El recurso canónico es la ficha de cada app en la tienda de apps de Shopify (apps.shopify.com). Fijarse en los planes con su unidad de cobro, las reseñas con su distribución por estrellas, la fecha de lanzamiento y la dirección del desarrollador.
