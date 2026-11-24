---
resumen: >-
  Las herramientas para pasar los datos de una tienda a otra plataforma: los importadores de Shopify, Tiendanube y WooCommerce, y los servicios de terceros, con lo que migran, cómo cobran y su precio de entrada, consultados el 2026-11-24.
estado: borrador
estabilidad: volatil
fuentes:
  - "Shopify App Store, Store Migration: https://apps.shopify.com/store-migration (leída, 2026-11-24)"
  - "Shopify Help, Migrating to Shopify: https://help.shopify.com/en/manual/migrating-to-shopify (leída, 2026-11-24)"
  - "Shopify Help, Using CSV files to import and export products: https://help.shopify.com/en/manual/products/import-export/using-csv (leída, 2026-11-24)"
  - "Matrixify, Pricing: https://matrixify.app/pricing/ (leída, 2026-11-24)"
  - "Tiendanube Ayuda, cómo migrar mi tienda online de Shopify a Tiendanube: https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube (leída, 2026-11-24)"
  - "Tiendanube Ayuda, cómo migrar el catálogo de Mercado Shops a Tiendanube: https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-el-catalogo-de-productos-de-mercado-shops-a-tiendanube (leída, 2026-11-24)"
  - "Tiendanube, blog, cómo migrar de Mercado Shops a Tiendanube (2026-02-27, actualizada el 10/04/2026): https://www.tiendanube.com/blog/como-migrar-de-mercado-shops-a-tiendanube/ (leída, 2026-11-24)"
  - "WooCommerce, Product CSV Importer and Exporter: https://woocommerce.com/document/product-csv-importer-exporter/ (leída, 2026-11-24)"
  - "WooCommerce, Shopify Data Migrator: https://woocommerce.com/document/shopify-data-migrator (leída, 2026-11-24)"
  - "LitExtension, Pricing: https://litextension.com/pricing.html (leída, 2026-11-24)"
  - "Bogdan Rancea, Cart2Cart review, ecommerce-platforms.com (actualizada el 2025-07-22): https://ecommerce-platforms.com/ecommerce-resources/cart2cart-review (leída, 2026-11-24; reseña, probable afiliado)"
  - "Comercio-electronico/.investigacion/mudar-una-tienda.md (componente 2)"
aliases: [migradores de tiendas, importadores, Cart2Cart, LitExtension, Matrixify, Store Migration]
creado: 2026-11-24
revisado:
---

# Herramientas para mudar una tienda

Las herramientas para pasar los datos de una tienda a otra plataforma: los importadores de Shopify, Tiendanube y WooCommerce, y los servicios de terceros, con lo que migran, cómo cobran y su precio de entrada, consultados el 2026-11-24.

Implementa [mudar una tienda](mudar-una-tienda.md), que explica qué pasa y qué no, y por qué. Las fuentes vivas son las páginas enlazadas en cada tabla. Los precios están en dólares y cambian seguido.

## Los importadores de cada plataforma

| Destino | Herramienta | De dónde trae | Qué trae | Precio |
|---|---|---|---|---|
| Shopify | [Store Migration](https://apps.shopify.com/store-migration), de Shopify (lanzada el 17-jul-2024) | "Square, WooCommerce, Etsy, Wix, Amazon, eBay, Clover, and Lightspeed R/X (Vend)", y cualquiera por CSV | productos y clientes | gratis; 3,1 de 5 con 77 reseñas |
| Shopify | CSV propio | cualquiera | productos (hasta 3 opciones y 250 imágenes por producto) | gratis; las tarjetas de regalo no se crean por CSV |
| Shopify | [Matrixify](https://matrixify.app/pricing/), de un tercero | archivos propios, de FTP, Google Drive, Dropbox o enlaces | productos, clientes, pedidos, redirecciones, páginas, blog, descuentos | US$ 20, 50 o 200 cada 30 días, según volumen |
| Tiendanube | Planilla CSV | cualquiera | productos; la carga por planilla no borra productos | gratis; hasta 20.000 líneas |
| Tiendanube | App «Shopify a Tiendanube» | Shopify | productos, colecciones y clientes | sin dato |
| Tiendanube | App «Mercadoshops a Tiendanube» | Mercado Shops y Mercado Libre | productos con fotos, categorías, descripciones, precio, stock y variantes | sin dato |
| WooCommerce | Importador CSV propio | cualquiera | productos, por ID o SKU (por GTIN desde la versión 11.2); variaciones desde la 11.1; no importa el texto alternativo de las imágenes | viene con WooCommerce |
| WooCommerce | [Shopify Data Migrator](https://woocommerce.com/document/shopify-data-migrator) | Shopify | productos, categorías, clientes, pedidos, cupones, blog, páginas y reseñas (estas, por CSV); no las contraseñas | sin dato |

Matrixify, por trabajo de importación, en los planes Basic y Big: productos 5.000 y 50.000, clientes 2.000 y 20.000, pedidos 1.000 y 10.000, redirecciones 10.000 y 100.000.

Hacia Tiendanube, la guía oficial pasa los clientes por una app de email marketing instalada en las dos tiendas; la app «Shopify a Tiendanube» también dice traerlos. Los pedidos no se migran a la tienda: desde Mercado Shops, esa app de email marketing los sincroniza y quedan visibles solo ahí. Los descuentos y las reseñas pasan por soporte. Tiendanube también ofrece migración asistida en su plan Evolución, sin precio publicado.

## Los servicios de terceros

Mudan entre muchas plataformas y cobran por proyecto, según cuántos productos, clientes y pedidos se pasan.

| Servicio | Cómo cobra | Precio de entrada | Lo que se paga aparte |
|---|---|---|---|
| [LitExtension](https://litextension.com/pricing.html), automático | por proyecto, según la cantidad de datos | «starts from $19»; gratis con menos de 100 productos, 100 clientes y 100 pedidos | las contraseñas de clientes y las redirecciones 301 |
| LitExtension, hecho por su equipo | por proyecto, según datos y complejidad | «starting from $129 per project» | nada: los adicionales van incluidos |
| Cart2Cart | por proyecto, sin suscripción | «From $69 and up», según una reseña | redirecciones 301, US$ 59; en un caso de WooCommerce a Shopify, la reseña declara US$ 286 en total, pero sus líneas suman US$ 385 |

LitExtension también figura en la tienda de aplicaciones de Tiendanube, según el buscador (la página no se abrió). Los agregadores de reseñas dan otros precios de entrada para LitExtension (US$ 29 o US$ 49); acá se toma su página. El precio de Cart2Cart sale de una reseña, porque su página de precios no cargó; la misma reseña dice que no migra contraseñas y a la vez las lista como adicional.

> [!NOTE] Sin fuente todavía: los límites de las apps de Tiendanube para importar desde Shopify y desde Mercado Shops; si la app Store Migration de Shopify trae pedidos; el precio de LitExtension o Cart2Cart con Tiendanube como destino; qué herramientas usan las agencias argentinas.
