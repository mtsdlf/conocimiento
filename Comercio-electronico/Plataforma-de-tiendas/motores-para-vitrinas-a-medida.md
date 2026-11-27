---
resumen: >-
  Los motores sobre los que se arma una vitrina a medida, con su licencia, cómo cobran, su precio de lista y el declarado, si dejan armar el checkout y si tienen Mercado Pago, transportistas argentinos y factura de ARCA, consultados el 2026-11-22.
estado: vigente
estabilidad: volatil
fuentes:
  - "Medusa, precios: https://medusajs.com/pricing/ (leída, 2026-11-22); repositorio y ENTERPRISE-LICENSE.md: https://github.com/medusajs/medusa (leído por la API de GitHub); integraciones: https://medusajs.com/integrations/ (leída)"
  - "Saleor, precios: https://saleor.io/pricing (leída); apps: https://github.com/saleor/apps (leído)"
  - "Vendure, precios: https://vendure.io/pricing (leída, 2026-11-22); plugins: https://docs.vendure.io/plugins (leída solo la primera página de 12)"
  - "commercetools, precios: https://commercetools.com/pricing (leída, sin cifras); conectores del Checkout: https://docs.commercetools.com/checkout/payment-connectors-applications (leída)"
  - "Vendr, commercetools: https://vendr.com/marketplace/commercetools (403; según un resumen del buscador y CostBench)"
  - "CostBench: https://www.costbench.com/compare/commercetools-vs-vtex/ y https://www.costbench.com/compare/adobe-commerce-vs-commercetools/ (leídas; agregador)"
  - "Shopify, Plus: https://www.shopify.com/plus/pricing ; precios: https://www.shopify.com/pricing ; Hydrogen: https://shopify.dev/docs/storefronts/headless/hydrogen/fundamentals ; Storefront API: https://shopify.dev/docs/api/storefront ; países de Shopify Payments: https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries ; transportista externo: https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/third-party-carrier-calculated-shipping (leídas, 2026-11-22)"
  - "Shopify, tienda de apps, búsquedas andreani y afip: https://apps.shopify.com/search?q=andreani (leída con navegador)"
  - "G2, precios de Shopify Plus: https://g2.com/products/shopify-plus/pricing (según un resumen del buscador; una de las guías sobre la tarifa variable de Plus)"
  - "VTEX, precios: https://www.vtex.com/en-us/pricing/ (leída, sin cifras); código de FastStore: https://github.com/vtex/faststore (leído)"
  - "Tiendanube Ayuda, qué es la Storefront API (actualizada el 26-oct-2026): https://ayuda.tiendanube.com/es_AR/socios-tecnologicos/que-es-la-storefront-api-de-tiendanube-y-para-que-sirve (leída entera)"
  - "WooCommerce, Store API: https://developer.woocommerce.com/docs/apis/store-api/ (leída); directorio de plugins: https://api.wordpress.org/plugins/info/1.2/ (leído por su API)"
  - "Magento Open Source: https://github.com/magento/magento2 (leído); Adobe, descripción legal de Commerce: https://helpx.adobe.com/legal/product-descriptions/adobe-commerce-cloud-service.html (403; según un resumen)"
  - "Mercado Pago, repositorios oficiales: https://github.com/mercadopago (leído); documentación para Shopify y VTEX: https://www.mercadopago.com.ar/developers/es/docs/shopify/introduction (leídas)"
  - "Andreani, repositorios: https://github.com/andreani-publico (leído); Adobe Marketplace: https://commercemarketplace.adobe.com/catalogsearch/result/?q=andreani (leído)"
  - "Registro de npm: https://registry.npmjs.org/-/v1/search y https://api.npmjs.org/downloads/ (leídos)"
  - "Comercio-electronico/.investigacion/vidrieras-motores-y-precios.md (respuesta corta y secciones 1, 2, 3 y 5)"
  - "Comercio-electronico/.investigacion/vidrieras-contraria.md (ítems 16 a 20, 40 a 45 y 47), que corrige al anterior"
aliases: [motores headless, motores de comercio headless, headless commerce engines, Medusa, Saleor, Vendure, commercetools, Hydrogen, Oxygen, FastStore, Storefront API de Tiendanube]
creado: 2026-11-27
revisado: 2026-11-27
---

# Motores para vitrinas a medida

Los motores sobre los que se arma una vitrina a medida, con su licencia, cómo cobran, su precio de lista y el declarado, si dejan armar el checkout y si tienen Mercado Pago, transportistas argentinos y factura de ARCA, consultados el 2026-11-22.

Implementa la [vitrina a medida](vitrina-a-medida.md): qué se programa, cuánto cuesta y cómo falla está allá. Las plataformas que ya tienen ficha propia son [Shopify](shopify.md), [VTEX](vtex.md), [Tiendanube](tiendanube.md), [WooCommerce](woocommerce.md) y [Adobe Commerce](adobe-commerce.md). Copiado de las páginas de precios, la documentación y los repositorios el 2026-11-22; las fuentes vivas van al final.

## Licencia, cobro y checkout

| Motor | Licencia | Cómo cobra | Precio de lista | Precio real declarado | ¿Deja armar el checkout? |
|---|---|---|---|---|---|
| Medusa | MIT, salvo permisos (RBAC) y SSO, con licencia comercial desde el 11-ago-2026 | nube por plan mensual, "0% GMV platform fee"; autoalojado sin licencia | "From $29": Develop US$ 29, Launch US$ 99, Scale US$ 299 por mes, más uso extra; Enterprise "Custom" | sin dato | sí, sobre su API |
| Saleor | BSD-3-Clause | nube con tope de GMV y porcentaje sobre el excedente; autoalojado sin licencia | Select US$ 1.599 por mes hasta US$ 200.000 de GMV mensual y 0,8% sobre el excedente; Volume US$ 3.999 hasta US$ 1 millón y 0,4% | sin dato | sí, con su "Checkout API" |
| Vendure | GPLv3 con excepción para plugins, o comercial con los planes pagos | plan por funciones de venta entre empresas y soporte, "no fee on revenue"; "Self-hosting doesn't change the plan price" | Starter €199 (12 meses), Growth €599, Scale €2.499 por mes; Enterprise desde €60.000 por año | sin dato | sí, sobre su API |
| commercetools | propietaria, SaaS | contrato anual por contacto, "order-based approach" y no GMV; Checkout como agregado aparte | sin cifras | mediana de US$ 151.200 por año con 5 compras, según un resumen de Vendr | sí, por API o con su Checkout (conectores de Adyen y PayPal) |
| Shopify Hydrogen y Oxygen | Hydrogen MIT; la plataforma, propietaria | plan mensual; Oxygen "at no extra charge on paid Shopify plans"; tarifa por pasarela externa de 2%, 1%, 0,6% y 0,2% según plan | planes de [Shopify](shopify.md); Plus "Starts at $2,300 USD/mo", contrato de 1 o 3 años; 1 vitrina a medida en los planes comunes y 25 en Plus | Plus: tarifa variable de alrededor de 0,35% a 0,40% del GMV con tope cercano a US$ 40.000 por mes, según guías de agencias leídas por un resumen; Shopify no la publica | no: la compra va al checkout de Shopify, con personalización "Limited" hasta Advanced y "Full" en Plus |
| VTEX FastStore | FastStore MIT; la plataforma, propietaria | cargo fijo más un porcentaje del GMV, contratos de 12 a 36 meses ([VTEX](vtex.md)) | no publicado | "Not in Vendr's deal flow"; un agregador cita 0,5% a 2,5% del ingreso con una sola fuente, según un resumen | no: el código redirige al checkout de VTEX |
| WooCommerce como motor | GPL-2.0 | núcleo gratis; alojamiento y extensiones aparte | gratis | sin dato | sí, con la Store API (`POST /wc/store/v1/checkout`) |
| Magento Open Source y Adobe Commerce como motor | Open Source OSL-3.0 (2.4.10-alpha1 del 13-oct-2026); Adobe Commerce propietaria | Adobe por contacto, con un "Pricing Level" por tramos de GMV y valor medio del pedido, según un resumen de su descripción legal | Open Source gratis; Adobe sin precio público | ver el aviso de abajo | sí |
| API de vitrina de Tiendanube | propietaria | el plan de la tienda ([Tiendanube](tiendanube.md)); habilitación manual por tienda | sin precio publicado para la API | sin dato | no: no tiene carrito («el frontend construye el suyo») y la compra va al checkout alojado |

> [!IMPORTANT]
> El precio real de Adobe Commerce no coincide entre dos fuentes, según un resumen. Vendr, a través del agregador CostBench, da una mediana de US$ 286.000 por año con 5 compras; otra página de CostBench da unos US$ 22.000 con 23, sin confirmar que vengan de Vendr. Vendr no se pudo abrir.

Shopify Payments no está disponible en Argentina: su lista oficial de países incluye solo a México en América Latina. Que la tarifa por pasarela externa se aplique a la app oficial de Mercado Pago es inferencia por la regla general.

## Mercado Pago, transportistas y factura de ARCA

Fecha de cada pieza: su último cambio visible. «Comunidad mantenida» quiere decir que cambió en los últimos 12 meses, no que se probó.

| Motor | [Mercado Pago](../Pagos/mercado-pago.md) | Andreani, OCA, Correo Argentino | [Factura de ARCA](../Normativa/factura-electronica-de-arca.md) |
|---|---|---|---|
| Medusa | de la comunidad: un paquete de npm, 0.4.0 del 14-sep-2026, 2.425 descargas en un mes; otros abandonados | no hay | no hay |
| Saleor | no hay usable: un repo de la comunidad del 21-nov-2026, vacío | no hay | no hay |
| Vendure | no hay | no hay | no hay plugin argentino |
| commercetools | no hay | sin verificar: su directorio de socios no se pudo leer | no hay en GitHub; socios sin leer |
| Shopify con Hydrogen | oficial, en el checkout de Shopify; la documentación no nombra Hydrogen | apps de terceros con pocas reseñas (Andreani y Correo Argentino); la cotización externa en el checkout es de Advanced y Plus | apps de terceros con CAE, de 0 a 6 reseñas |
| VTEX FastStore | oficial, sobre el checkout de VTEX | sin verificar: la tienda de apps no se pudo buscar | sin verificar |
| WooCommerce como motor | oficial: 8.10.3 del 18-nov-2026, 100.000+ instalaciones; sin verificar que ande por la Store API | Andreani 1.8.9 (6-nov-2026, autor sin confirmar), OCA 4.1.7 (5-nov-2026), Correo Argentino 3.0.8.1 (2-nov-2026, autor «Correo Argentino») | de la comunidad mantenidos, como `integracion-afip` 4.1.0 (6-nov-2026) |
| Magento Open Source y Adobe Commerce | oficial: `adb-payment` 1.15.7 del 27-oct-2026 | Andreani publica módulos para Magento 2.2 y 2.3 (último cambio 29-abr-2025); OCA y Correo Argentino, no hay | abandonado (26-nov-2020) |
| API de vitrina de Tiendanube | la ayuda confirma solo Pago Nube; el resto de las apps, «caso a caso» | confirma solo Envío Nube | sin confirmar en este modo |

Para cualquier motor en JavaScript hay piezas sueltas en npm: el SDK oficial `mercadopago` 3.6.2 y SDKs de ARCA mantenidos en 2026, como `@afipsdk/afip.js` 1.3.0 del 2-nov. Son bibliotecas y no plugins: la integración con el motor la escribe alguien. Ninguna oferta argentina de motor a medida con Mercado Pago, transportistas y ARCA ya resueltos apareció fuera de WooCommerce y Magento.

> [!NOTE] Sin fuente todavía: el precio real de Medusa, Saleor y Vendure en la nube; las fechas de las apps de Shopify y de Mercado Pago para Shopify y VTEX; si la VTEX App Store y los socios de commercetools tienen Andreani o ARCA; y si alguna de estas piezas anda de verdad en modo a medida.

## Fuentes vivas por motor

- **Medusa**: [precios](https://medusajs.com/pricing/), [repositorio](https://github.com/medusajs/medusa), [integraciones](https://medusajs.com/integrations/).
- **Saleor**: [precios](https://saleor.io/pricing), [apps oficiales](https://github.com/saleor/apps).
- **Vendure**: [precios](https://vendure.io/pricing), [plugins](https://docs.vendure.io/plugins).
- **commercetools**: [precios](https://commercetools.com/pricing), [conectores del Checkout](https://docs.commercetools.com/checkout/payment-connectors-applications).
- **Shopify**: [Plus](https://www.shopify.com/plus/pricing), [Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/fundamentals), [países de Shopify Payments](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries).
- **VTEX FastStore**: [precios](https://www.vtex.com/en-us/pricing/), [código](https://github.com/vtex/faststore).
- **WooCommerce**: [Store API](https://developer.woocommerce.com/docs/apis/store-api/), [plugin de Mercado Pago](https://github.com/mercadopago/cart-woocommerce).
- **Magento y Adobe Commerce**: [magento2](https://github.com/magento/magento2), [Mercado Pago para Adobe](https://github.com/mercadopago/adb-payment), [Andreani](https://github.com/andreani-publico).
- **API de vitrina de Tiendanube**: [ayuda](https://ayuda.tiendanube.com/es_AR/socios-tecnologicos/que-es-la-storefront-api-de-tiendanube-y-para-que-sirve).
