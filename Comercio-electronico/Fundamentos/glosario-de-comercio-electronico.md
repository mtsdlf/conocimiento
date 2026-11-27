---
resumen: >-
  Los términos y siglas que usan las notas de comercio electrónico, cada uno con su forma en inglés, una definición corta y la nota que lo desarrolla, más las marcas con que los informes dicen cuánto se leyó de cada fuente.
estado: vigente
estabilidad: semi
fuentes:
  - "Las notas del tema que enlaza cada término, con sus propias fuentes"
  - "OECD, The 2025 OECD definition of e-commerce and guidelines for interpretation, copia en UNCTAD: https://unctad.org/system/files/information-document/2025oecddefinitionofecommerce_guidelinesforinterpretation.pdf (leído)"
  - "Shopify, 10-K FY2025, Item 1 y Item 7: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm (leído en parte)"
  - "BCRA, Comunicación A 6885: https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6885.pdf (leído)"
  - "BCRA, Transferencias 3.0: https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ (leído, resumen de herramienta)"
  - "Stripe, cómo funcionan las disputas: https://docs.stripe.com/disputes/how-disputes-work y 3D Secure: https://docs.stripe.com/payments/3d-secure/authentication-flow (leídos)"
  - "EMVCo, 3-D Secure: https://www.emvco.com/emv-technologies/3-d-secure/ (leído)"
  - "Littledata, Benchmarks: https://www.littledata.io/benchmarks (leído)"
  - "Baymard Institute, Cart abandonment rate: https://baymard.com/blog/cart-abandonment-rate (leído)"
  - "Shopify, ProductVariant: https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant (leído)"
  - "Disposición 954/2025: https://www.boletinoficial.gob.ar/detalleAviso/primera/330827/20250904 (leído)"
  - "Código Civil y Comercial, art. 1110: https://www.argentina.gob.ar/normativa/nacional/ley-26994-235975/texto (leído)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md, sección A7; Comercio-electronico/.investigacion/plataforma-de-tiendas.md; Comercio-electronico/.investigacion/pagos.md; Comercio-electronico/.investigacion/checkout-y-conversion.md; Comercio-electronico/.investigacion/operaciones-canales-y-normativa.md; Comercio-electronico/.investigacion/huecos-pagos-y-operaciones.md"
aliases: [glosario de e-commerce, términos de comercio electrónico, e-commerce glossary, siglas de comercio electrónico]
creado: 2026-11-22
revisado: 2026-11-24
---

# Glosario de comercio electrónico

Los términos y siglas que usan las notas de comercio electrónico, cada uno con su forma en inglés, una definición corta y la nota que lo desarrolla, más las marcas con que los informes dicen cuánto se leyó de cada fuente.

Las definiciones son síntesis del campo hechas por el informe de fundamentos, sin fuente propia, salvo donde se nombra una. Las citas, las cifras y los desacuerdos viven en la nota de cada término. Antes de pasar a vigente, cada término de dinero (GMV, take rate, contracargo) tiene que quedar con su fuente en su nota.

## Marcas de lectura

Los informes del tema marcan cuánto se leyó de cada fuente; las notas lo dicen en prosa ("según su abstract", "según un resumen").

| Marca | Qué significa |
|---|---|
| [L] | Se leyó la página o el pasaje relevante. En casi todos los informes la lectura pasó por una herramienta que devuelve un extracto; el de pagos la marca [L*] y reserva [L] para los PDF convertidos a texto y leídos enteros. |
| [M] | Se leyeron solo los metadatos, el índice, la ficha o el abstract. En la historia, también las páginas de Wikipedia sin abrir sus fuentes. |
| [S] | Se leyó un resumen del buscador o una fuente secundaria, o es síntesis propia del informe; hay que verificarlo antes de afirmarlo. |

## El comercio y sus modelos

| Término | En inglés | Qué es | Dónde se desarrolla |
|---|---|---|---|
| Comercio electrónico | e-commerce | Venta o compra en la que el pedido se hace por un método diseñado para eso, aunque el pago y la entrega sean fuera de línea (OCDE) | [Comercio electrónico](../comercio-electronico.md) |
| B2C, B2B y C2C | business-to-consumer, business-to-business, consumer-to-consumer | Una empresa vende a consumidores; una empresa a otra (incluye el EDI); personas a personas, con una plataforma en el medio | [Comercio electrónico](../comercio-electronico.md) |
| D2C | direct-to-consumer (D2C o DTC) | La marca que fabrica vende directo, sin minorista; es un canal, y una D2C también es B2C | [Comercio electrónico](../comercio-electronico.md) |
| Marketplace | marketplace | Sitio donde muchos vendedores publican y la plataforma cobra una comisión; la OCDE las llama plataformas de intermediación digital | [Venta en varios canales](../Venta-en-varios-canales/venta-en-varios-canales.md) |
| Comercio social | social commerce | Pedido hecho dentro de una red o una app de mensajería; para la OCDE cuenta solo con un catálogo estructurado | [Venta en varios canales](../Venta-en-varios-canales/venta-en-varios-canales.md) |
| Comercio conversacional | conversational commerce | Venta que se cierra atendiendo por chat (WhatsApp, Instagram), con o sin catálogo, y se cobra con un link | [Comercio conversacional](../Venta-en-varios-canales/Comercio-conversacional/comercio-conversacional.md) |
| EDI | electronic data interchange | Intercambio de pedidos y documentos entre sistemas de empresas, anterior a la web | [Historia del comercio electrónico](historia-del-comercio-electronico.md) |

## La plataforma de tiendas

| Término | En inglés | Qué es | Dónde se desarrolla |
|---|---|---|---|
| Plataforma alojada | hosted platform, SaaS commerce | Software de tienda que el comercio alquila y que el proveedor aloja y opera | [Tipos de plataforma](../Plataforma-de-tiendas/tipos-de-plataforma.md) |
| Código abierto autoalojado | self-hosted open source | Software de tienda que el comercio o su agencia instala, actualiza y asegura | [Tipos de plataforma](../Plataforma-de-tiendas/tipos-de-plataforma.md) |
| Headless | headless commerce | La vitrina se separa del motor de comercio y se comunica con él por API | [Tipos de plataforma](../Plataforma-de-tiendas/tipos-de-plataforma.md) |
| Vitrina a medida | headless storefront, custom storefront | El frente de una tienda que el comercio o su agencia programa y que habla por API con un motor de comercio | [Vitrina a medida](../Plataforma-de-tiendas/vitrina-a-medida.md) |
| Composable | composable commerce | La tienda se arma con servicios independientes elegidos uno por uno | [Tipos de plataforma](../Plataforma-de-tiendas/tipos-de-plataforma.md) |
| MACH | microservices, API-first, cloud-native, headless | Principios de arquitectura que promueve la MACH Alliance, formada por proveedores de esos componentes | [Tipos de plataforma](../Plataforma-de-tiendas/tipos-de-plataforma.md) |
| Multi-tenant | multi-tenancy | Una instalación sirve a muchas tiendas con los datos aislados; el concepto general está en [Multi-tenancy](../../Arquitectura/Sistemas-distribuidos/multi-tenancy.md) | [Arquitectura de plataforma](../Plataforma-de-tiendas/arquitectura-de-plataforma.md) |
| Tema | theme | Diseño intercambiable de la vitrina | [Arquitectura de plataforma](../Plataforma-de-tiendas/arquitectura-de-plataforma.md) |
| API y webhook | API, webhook | Interfaz para que otros sistemas lean y escriban datos; aviso automático que un sistema manda a otro ante un evento | [Arquitectura de plataforma](../Plataforma-de-tiendas/arquitectura-de-plataforma.md) |
| Tienda de apps | app store | Catálogo de extensiones de terceros dentro de la plataforma | [Apps para comerciantes](../Plataforma-de-tiendas/apps-para-comerciantes.md); cómo se instalan, en [Arquitectura de plataforma](../Plataforma-de-tiendas/arquitectura-de-plataforma.md) |
| GMV | gross merchandise value | Valor bruto de lo vendido a través de la plataforma. Shopify: "the total dollar value of orders facilitated through our platform", que "does not represent revenue" | [El negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md) |
| Take rate | take rate | Parte del GMV que se queda la plataforma; Shopify no la publica con ese nombre y se calcula dividiendo ingresos por GMV | [El negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md) |
| MRR | monthly recurring revenue | Ingreso mensual recurrente. Shopify: "the aggregate value of all subscription plans, excluding variable platform fees" | [El negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md) |
| Penetración de pagos | payments penetration rate | Parte del GMV que pasa por la pasarela propia de la plataforma; es proporción del GMV, no de comerciantes | [El negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md) |
| Churn | churn | Parte de los comerciantes que se da de baja en un período; el concepto general está en [Churn](../../Datos/Analitica-de-producto/Retencion-y-churn/churn.md) | [El negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md) |
| Segmento de comerciantes | merchant segment (SMB, mid-market, enterprise) | Emprendedor, pyme, mediana o grande; las plataformas no publican la clasificación, se deduce de sus planes | [Segmentos de comerciantes](../Plataforma-de-tiendas/segmentos-de-comerciantes.md) |

## Pagos

| Término | En inglés | Qué es | Dónde se desarrolla |
|---|---|---|---|
| Pasarela de pagos | payment gateway | Servicio que transmite los datos del pago desde la tienda al procesador | [Actores del pago](../Pagos/actores-del-pago.md) |
| Adquirente | acquirer | Entidad que procesa los cobros con tarjeta del comercio y le paga | [Actores del pago](../Pagos/actores-del-pago.md) |
| Procesador | processor | Empresa que ejecuta técnicamente la autorización | [Actores del pago](../Pagos/actores-del-pago.md) |
| Agregador de pagos | payment facilitator (payfac), aggregator | Cobra por muchos comercios bajo una sola cuenta propia | [Actores del pago](../Pagos/actores-del-pago.md) |
| Proveedor de servicios de pago (PSP) | payment service provider | Para el BCRA, persona jurídica que, "sin ser entidades financieras", cumple al menos una función en un esquema de pago minorista | [Actores del pago](../Pagos/actores-del-pago.md) |
| Emisor | issuer | Banco o entidad que emitió la tarjeta del comprador | [Actores del pago](../Pagos/actores-del-pago.md) |
| Red de tarjetas, esquema de pago | card network, card scheme | Quien fija las reglas entre emisor y adquirente. El BCRA define el esquema como "sistemas de reglas comerciales, técnicas y/o operativas" con un administrador | [Actores del pago](../Pagos/actores-del-pago.md) |
| Autorización | authorization | Aprobación del emisor para un pago | [Actores del pago](../Pagos/actores-del-pago.md) |
| Tasa de intercambio | interchange fee | Lo que el adquirente paga al emisor por cada operación; en la Unión Europea tiene tope | [Costo de cobrar](../Pagos/costo-de-cobrar.md) |
| Tasa de descuento | merchant discount rate (MDR) | Lo que el comercio paga por cada cobro, que suma intercambio, red y margen del adquirente | [Costo de cobrar](../Pagos/costo-de-cobrar.md) |
| Acreditación y conciliación | settlement, reconciliation | El paso del dinero al comercio, y el cruce entre ventas, cobros y movimientos bancarios. En una plataforma argentina, acreditar (que aparezca el pago) no es tener el dinero disponible | [Costo de cobrar](../Pagos/costo-de-cobrar.md) |
| Contracargo | chargeback | El titular desconoce un pago ante su emisor, la red debita al adquirente o agregador y este al comercio, más una tarifa (Stripe) | [Fraude y contracargos](../Pagos/fraude-y-contracargos.md) |
| Representment | representment | La respuesta del comercio a un contracargo, con evidencia, a través de su adquirente (según guías de proveedores) | [Fraude y contracargos](../Pagos/fraude-y-contracargos.md) |
| 3-D Secure (3DS) | 3-D Secure | Autenticación extra del titular. EMVCo: ayuda a "prevent card-not-present (CNP) fraud" | [Fraude y contracargos](../Pagos/fraude-y-contracargos.md) |
| Cambio de responsabilidad | liability shift | Con 3DS, el fraude disputado suele pasar del comercio al emisor; Stripe advierte que la autenticación exitosa "doesn't guarantee liability shift" | [Fraude y contracargos](../Pagos/fraude-y-contracargos.md) |
| Cuotas y cuotas sin interés | installments, interest-free installments | Pago dividido en pagos mensuales. "Sin interés" significa que el comprador no ve la tasa; el costo lo paga el comercio, el que compra al contado o el Estado | [Cuotas](../Pagos/cuotas.md) |
| CFT | costo financiero total | Costo total de un crédito, con la tasa y los cargos | [Cuotas](../Pagos/cuotas.md) |
| BNPL | buy now, pay later | Compra ahora, pago diferido | [Cuotas](../Pagos/cuotas.md) |
| Billetera virtual | digital wallet | App que guarda medios de pago o saldo; si guarda saldo, en Argentina es un PSP con cuenta de pago | [Medios de pago locales](../Pagos/medios-de-pago-locales.md) |
| Pago con transferencia | instant payment, account-to-account payment | Transferencia inmediata entre cuentas usada para pagar. En Argentina (Transferencias 3.0) se acredita "en un máximo de 15 segundos" y es irrevocable; en Brasil es Pix | [Medios de pago locales](../Pagos/medios-de-pago-locales.md) |
| QR interoperable | interoperable QR | Código QR que cualquier billetera puede pagar: "no importa la marca del código QR" (BCRA) | [Medios de pago locales](../Pagos/medios-de-pago-locales.md) |

## Checkout y conversión

| Término | En inglés | Qué es | Dónde se desarrolla |
|---|---|---|---|
| Embudo de conversión | conversion funnel | Las etapas de la visita a la compra; en GA4 son eventos como `add_to_cart`, `begin_checkout` y `purchase` | [Embudo de conversión](../Checkout-y-conversion/embudo-de-conversion.md) |
| Tasa de conversión | conversion rate | Compras sobre sesiones o sobre visitantes, según la fuente. Littledata: "The share of sessions that included at least one purchase" | [Embudo de conversión](../Checkout-y-conversion/embudo-de-conversion.md) |
| Finalización del checkout | checkout completion | De las sesiones que empezaron el checkout, las que compraron (Littledata) | [Embudo de conversión](../Checkout-y-conversion/embudo-de-conversion.md) |
| Ticket promedio | average order value (AOV) | Facturación dividida por pedidos | [Embudo de conversión](../Checkout-y-conversion/embudo-de-conversion.md) |
| Abandono de carrito | cart abandonment | El carrito es la selección de productos antes de pagar; el abandono, los carritos creados que no terminan en compra; Baymard lo calcula como (1 − compras ÷ carritos creados) × 100 | [Carrito abandonado](../Checkout-y-conversion/carrito-abandonado.md) |
| Retargeting | retargeting | Anuncios para quien abandonó; el momento cambia el efecto | [Carrito abandonado](../Checkout-y-conversion/carrito-abandonado.md) |
| Checkout | checkout | Los pasos de datos, envío y pago | [Usabilidad del checkout](../Checkout-y-conversion/usabilidad-del-checkout.md) |
| Checkout de invitado | guest checkout | Comprar sin crear una cuenta | [Usabilidad del checkout](../Checkout-y-conversion/usabilidad-del-checkout.md) |

## Buscadores

| Término | En inglés | Qué es | Dónde se desarrolla |
|---|---|---|---|
| SEO | search engine optimization | El trabajo para aparecer en los resultados orgánicos (no pagos) de los buscadores | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Rastrear e indexar | crawl, index | El buscador recorre las páginas siguiendo enlaces (rastrea) y guarda las que decide mostrar (indexa); indexar no está garantizado | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Canónica | canonical URL, rel=canonical | La dirección que se declara como la versión principal entre varias casi iguales; para Google es una señal, no una orden | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Sitemap y robots.txt | sitemap, robots.txt | El archivo que lista las páginas para que el buscador las descubra, y el que le dice qué direcciones no rastrear | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Noindex y soft 404 | noindex, soft 404 | La marca que pide no mostrar una página; y una página que dice «no encontrado» o queda vacía pero responde como si existiera | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Slug | slug, handle | El texto final de la dirección de un producto o categoría, que el comercio suele poder editar | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Navegación por facetas | faceted navigation | Los filtros de un listado (color, talle, precio), que crean una dirección por combinación | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Datos estructurados | structured data, JSON-LD, schema.org | Marcas en el código de la página que le dicen al buscador el precio, la disponibilidad y otros datos del producto | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Merchant Center y feed | Google Merchant Center, product feed | La cuenta de Google donde la tienda carga su catálogo (el feed) para aparecer en Shopping y en los listados gratuitos | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Search Console | Google Search Console | La herramienta gratuita de Google para ver qué páginas indexó, por qué consultas aparece la tienda y con cuántos clics | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Impresiones, CTR y posición promedio | impressions, click-through rate, average position | Cuántas veces apareció la tienda en los resultados, qué parte de esas veces recibió un clic y en qué lugar apareció, en promedio | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| Core Web Vitals | Core Web Vitals (LCP, INP, CLS) | Tres métricas de Google sobre la experiencia de carga: cuánto tarda en verse lo principal, cuánto en responder y cuánto se mueve la página | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |
| CDN | content delivery network | Una red de servidores repartidos que entrega la tienda desde el lugar más cercano al comprador | [SEO de una tienda](../Plataforma-de-tiendas/seo-de-una-tienda.md) |

## Operaciones, canales y normativa

| Término | En inglés | Qué es | Dónde se desarrolla |
|---|---|---|---|
| Variante y SKU | variant, stock keeping unit | La versión vendible de un producto (talla, color) y su código; en Shopify el stock cuelga de la variante | [Catálogo y stock](../Operaciones-del-comercio/catalogo-y-stock.md) |
| Sobreventa | overselling | Vender más de lo disponible; el riesgo crece con cada canal que descuenta stock por su cuenta | [Catálogo y stock](../Operaciones-del-comercio/catalogo-y-stock.md) |
| Fulfillment | fulfillment | Preparar y despachar los pedidos | [Operaciones del comercio](../Operaciones-del-comercio/operaciones-del-comercio.md) |
| Última milla | last mile | El tramo final de la entrega al comprador | [Operaciones del comercio](../Operaciones-del-comercio/operaciones-del-comercio.md) |
| Logística inversa | reverse logistics | El circuito de las devoluciones | [Devoluciones](../Operaciones-del-comercio/devoluciones.md) |
| Multicanal y omnicanal | multichannel, omnichannel | Vender en varios canales gestionados por separado; o con los canales integrados, con stock y cliente compartidos | [Venta en varios canales](../Venta-en-varios-canales/venta-en-varios-canales.md) |
| POS | point of sale | El punto de venta físico conectado a la tienda online | [Venta en varios canales](../Venta-en-varios-canales/venta-en-varios-canales.md) |
| Derecho de revocación | right of withdrawal | En Argentina, el consumidor puede revocar una compra a distancia "dentro de los diez días" (CCyC, art. 1110) | [Normativa](../Normativa/normativa.md) |
| Botón de arrepentimiento | withdrawal button | El enlace para revocar la compra, a simple vista y sin registro previo; hoy lo regula la Disposición 954/2025, que derogó la Resolución 424/2020 | [Normativa](../Normativa/normativa.md) |
| CAC y LTV | customer acquisition cost, customer lifetime value | Lo que cuesta conseguir un cliente y lo que deja a lo largo del tiempo | [Economía unitaria](../../Marketing/Medicion/economia-unitaria.md) |
