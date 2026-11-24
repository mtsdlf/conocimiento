---
resumen: >-
  Lo que Tiendanube, Shopify y WooCommerce fijan y dejan cambiar para el posicionamiento en buscadores (direcciones, títulos, sitemap, robots.txt, canónicas, variantes, datos estructurados, Merchant Center, redirecciones y velocidad), según su documentación pública. Consultado el 2026-11-24.
estado: vigente
estabilidad: volatil
fuentes:
  - "Ayuda de Tiendanube, opciones avanzadas de SEO de productos: https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos (leída a través de un extracto, 2026-11-24)"
  - "Ayuda de Tiendanube, cómo enviar un sitemap a Google: https://ayuda.tiendanube.com/es_ES/google-ads/como-enviar-un-sitemap-a-google (leída a través de un extracto, 2026-11-24)"
  - "Blog de Tiendanube, SEO para tienda online: https://www.tiendanube.com/blog/seo-para-tienda-online/ (leída; marketing propio)"
  - "Documentación de temas de Tiendanube, datos estructurados JSON-LD: https://docs.tiendanube.com/help/data-estructurada-json-ld (leída a través de un extracto, 2026-11-24)"
  - "Ayuda de Nuvemshop (Brasil), robots.txt: https://atendimento.nuvemshop.com.br/pt_BR/ferramentas-do-google/como-funciona-o-arquivo-robotstxt-na-nuvemshop (leída; es la misma plataforma con otra marca)"
  - "Ayuda de Tiendanube, feed para Google Shopping: https://ayuda.tiendanube.com/es_ES/como-configurar-el-feed-de-productos-para-google-shopping (según resumen)"
  - "Ayuda de Tiendanube, dirección sin .mitiendanube.com: https://ayuda.tiendanube.com/es_ES/175777-abc-del-dominio-propio/como-tener-una-direccion-web-sin-el-mitiendanubecom (según resumen)"
  - "Shopify Help, URL redirects: https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect (leída a través de un extracto, 2026-11-24)"
  - "Shopify Help, SEO overview: https://help.shopify.com/en/manual/promoting-marketing/seo/seo-overview (leída a través de un extracto, 2026-11-24)"
  - "Shopify Help, Adding keywords: https://help.shopify.com/en/manual/promoting-marketing/seo/adding-keywords (leída en parte, 2026-11-24)"
  - "shopify.dev, robots.txt.liquid: https://shopify.dev/docs/storefronts/themes/architecture/templates/robots-txt-liquid (leída a través de un extracto, 2026-11-24)"
  - "shopify.dev, objeto variant de Liquid: https://shopify.dev/docs/api/liquid/objects/variant (según resumen)"
  - "Shopify Help, sincronizar productos con Google & YouTube: https://help.shopify.com/en/manual/online-sales-channels/marketplaces/google/getting-setup/syncing-products (según resumen)"
  - "Shopify Help, Web performance: https://help.shopify.com/en/manual/online-store/web-performance/overview (según resumen)"
  - "Shopify Community, prefijos de URL: https://community.shopify.com/t/changing-default-word-products-in-the-url/263056 (según resumen; comunidad)"
  - "WooCommerce, Permalinks: https://woocommerce.com/document/permalinks/ (leída a través de un extracto, 2026-11-24)"
  - "WooCommerce Developer Blog, Product permalink changes coming in WooCommerce 10.5 (2026-01-13): https://developer.woocommerce.com/2026/01/13/product-permalink-changes-coming-in-woocommerce-10-5/ (leída a través de un extracto)"
  - "WooCommerce wiki, Structured data for products: https://github.com/woocommerce/woocommerce/wiki/Structured-data-for-products (leída; página vieja)"
  - "WooCommerce, Google for WooCommerce, feed y listados gratuitos: https://woocommerce.com/document/google-for-woocommerce/get-started/product-feed-information-and-free-listings/ (leída a través de un extracto, 2026-11-24)"
  - "WordPress, sitemaps nativos de WordPress 5.5: https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/ (según resumen)"
  - "Rank Math, precios: https://rankmath.com/pricing/ y Yoast vs Rank Math: https://yoast.com/choosing-the-right-wordpress-seo-plugin-for-your-business-yoast-vs-rank-math/ (según resumen; los dos venden plugins)"
  - "Comercio-electronico/.investigacion/seo-por-plataforma.md"
aliases: [SEO en Tiendanube, SEO en Shopify, SEO en WooCommerce]
creado: 2026-11-24
revisado: 2026-11-24
---

# SEO por plataforma

Lo que Tiendanube, Shopify y WooCommerce fijan y dejan cambiar para el posicionamiento en buscadores (direcciones, títulos, sitemap, robots.txt, canónicas, variantes, datos estructurados, Merchant Center, redirecciones y velocidad), según su documentación pública. Consultado el 2026-11-24.

Es el dato detrás del reparto entre plataforma y comercio que explica [SEO de una tienda](seo-de-una-tienda.md#lo-que-resuelve-la-plataforma-y-lo-que-queda-en-el-comercio). El resto de los datos de cada plataforma está en sus fichas: [Tiendanube](tiendanube.md), [Shopify](shopify.md) y [WooCommerce](woocommerce.md). Varias páginas de ayuda se leyeron a través de un extracto y no enteras, y lo marcado «según resumen» no se abrió: conviene confirmarlo en una tienda real (el código fuente de una página de producto) antes de afirmarlo a un cliente.

| | Tiendanube | Shopify | WooCommerce |
|---|---|---|---|
| Prefijo de las direcciones | sin fuente | esas rutas (`/products/`, `/collections/`) no se pueden redirigir; que tampoco se puedan cambiar lo dice la comunidad | editable: base de producto, de categoría y de atributo |
| Texto de la dirección (slug) | editable por producto y categoría; no en la carga masiva | editable (el *handle*, según la comunidad) | editable (el slug de WordPress; sin fuente leída) |
| Título y descripción por producto y categoría | sí, hasta 70 y 160 caracteres | sí, hasta 70 caracteres en el título (recomienda 60); para la descripción recomienda 160 | sin panel propio documentado; se infiere que depende de un plugin |
| Sitemap | automático en `/sitemap.xml`, se actualiza cada día | automático | nativo de WordPress en `/wp-sitemap.xml` (2.000 direcciones por archivo, según resumen) o el del plugin |
| robots.txt | no editable a mano (dato de Nuvemshop Brasil; sin fuente para Argentina) | editable con la plantilla `robots.txt.liquid`, que reemplaza al generado | editable (filtro de WordPress o archivo propio, según resumen) |
| Canónicas | anunciadas como función integrada; los temas exponen `canonical_url` en el producto | automáticas; la dirección del producto dentro de una colección apunta a la del producto (según la comunidad) | las pone el plugin de SEO, según Rank Math; sin dato del núcleo |
| Variantes | sin fuente | parámetro `?variant=` en la dirección del producto (según resumen) | sin fuente |
| Datos estructurados del producto | JSON-LD en los temas; los temas viejos hay que actualizarlos | incluidos en los temas, y la tienda de temas los exige (según resumen) | JSON-LD en la página de producto; no en categorías (desde la versión 3.5.6, según una página vieja) |
| Google Merchant Center | integración propia; manda solo el precio original, y un descuento por medio de pago puede causar rechazos (según resumen) | app Google & YouTube; cada cuenta de Merchant Center, una tienda (según resumen) | extensión Google for WooCommerce; los productos pueden aparecer en los listados gratuitos en 3 a 5 días (sin confirmar para Argentina) |
| Redirecciones 301 | sí | sí, hasta 100.000 (20 millones en Plus) | con plugin o en el servidor; automáticas en el cambio de la versión 10.5 |
| Velocidad | CDN incluida | CDN de Cloudflare sin costo extra (según resumen) | sin fuente; en la práctica depende del alojamiento y los plugins |
| Plugins o apps de SEO | sin fuente | apps de la tienda de apps; no se relevaron nombres ni precios | Yoast Premium, USD 118,80 por año; Rank Math, gratis o PRO desde € 95,88 por año y € 107,88 en la renovación, más impuestos (según resumen) |
| Lo que depende del plan | el dominio propio pide un plan pago (según resumen) | las páginas leídas solo mencionan el tope de redirecciones | no hay planes: depende del alojamiento |

Lo que hay que saber de cada una al cuidar una tienda:

- **Tiendanube.** Su blog recomienda títulos de hasta 60 caracteres y descripciones de hasta 105, más cortos que lo que admite el panel (70 y 160): uno es una recomendación y el otro, el límite. Google tarda «entre pocos días y 3 semanas» en leer el sitemap, según su ayuda.
- **Shopify.** Si `/products/` y `/collections/` son fijos, como dice la comunidad, una tienda que llega de otra plataforma con otras rutas las cambia aunque conserve el dominio. Redirige las viejas hacia las nuevas (inferencia; ver [mudar una tienda](mudar-una-tienda.md)). Las soluciones de terceros para cambiar los prefijos, como un proxy delante de la tienda, tienen costo de mantenimiento, y Shopify desaconseja el proxy porque "masks real problems, distorts metrics, and adds latency" (según resumen).
- **WooCommerce.** Es la que más deja cambiar en las direcciones y la que menos trae resuelto: WordPress da el sitemap, y los títulos y las canónicas, según lo que se encontró, quedan en manos de un plugin. Desde la versión 10.5, una tienda con la categoría en la dirección del producto puede ver cambiar algunas direcciones; WooCommerce "will automatically 301 redirect old URLs".

Empretienda y VTEX no se relevaron: de Empretienda solo se encontró su guía de Google Shopping, y de VTEX, que tiene un editor de robots.txt y canónicas automáticas (según resumen de su documentación).
