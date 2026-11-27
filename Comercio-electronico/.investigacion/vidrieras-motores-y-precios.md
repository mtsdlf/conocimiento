# Vidrieras a medida: los motores, cuánto cuestan de verdad y qué traen de lo local

Fecha de consulta: 2026-11-22 (todo lo de abajo, salvo que diga otra fecha). Método: páginas de precios oficiales leídas con WebFetch (marca [L] cuando se leyó la página; [S] cuando el dato viene de un resumen del buscador o de una herramienta de resumen sobre una página que no se pudo abrir); datos de GitHub por la API (`gh api`), de npm por su registro público y de WordPress.org por su API de plugins; el código de FastStore leído en su repositorio. No se recomienda nada: se mide.

Calificación: fuente A (primaria, confiable) a F; dato 1 (confirmado) a 6 (sin poder juzgar). Lo que cada empresa dice de sí misma va como C para cifras de escala o de éxito.

Parte de un barrido previo: `lind-negocio/el-taller/analisis/2026-11-22-el-bosque/motor-para-vidrieras-a-medida.md` (lo que ya está ahí se cita y no se repite). Fichas de la base usadas: `Plataforma-de-tiendas/shopify.md`, `vtex.md`, `adobe-commerce.md`, `woocommerce.md`, `tiendanube.md`, `tipos-de-plataforma.md` y `Pagos/mercado-pago.md`.

**Cupo de búsquedas:** se usaron unas 13 búsquedas web propias; no se agotó. Vendr (vendr.com) devolvió 403 a la lectura directa y al navegador real; sus cifras van por resumen del buscador y por CostBench, que las agrega. La página de precios de Adobe y su descripción legal del producto tampoco abrieron (timeout, error HTTP/2 y 403).

## Respuesta corta

1. **Hay tres formas de cobrar.** (a) Gratis el núcleo y se paga la nube o las funciones extra: Medusa, Saleor, Vendure, WooCommerce, Magento Open Source. (b) Plan mensual de la plataforma alojada, con la vitrina propia sin cargo extra: Shopify (Hydrogen y Oxygen "at no extra charge on paid Shopify plans") y Tiendanube (Storefront API sin precio publicado). (c) Contrato anual por contacto: commercetools, VTEX, Adobe Commerce [L, A].
2. **Precio real declarado (Vendr, vía agregadores):** commercetools, mediana de US$ 151.200 por año con 5 compras; Adobe Commerce, mediana de US$ 286.000 por año con 5 compras (otra página da US$ 22.000 con 23; no coinciden); VTEX "no está en el flujo de Vendr" [S, C, dato 5: muestras de 5].
3. **El checkout propio, quién lo deja.** Medusa, Saleor, Vendure, commercetools, Adobe Commerce y WooCommerce dejan armarlo, sin cargo de licencia en los abiertos. Shopify manda la compra a "Shopify's web checkout" y la personalización completa solo está en Plus, "Starts at $2,300 USD/mo". Tiendanube manda la compra a su checkout alojado. FastStore redirige al checkout de VTEX (está en su código) [L, A].
4. **Mercado Pago oficial existe para** Shopify, WooCommerce, VTEX, PrestaShop, Salesforce Commerce Cloud, Wix, Tiendanube, Adobe Commerce y BigCommerce (menú "Apps para plataformas" de Mercado Pago) [L, A]. **No hay oficial** para Medusa, Saleor, Vendure ni commercetools.
5. **Mercado Pago de la comunidad:** Medusa tiene uno mantenido (v0.4.0 del 14-sep-2026, para Medusa ≥ 2.21, 2.425 descargas en el último mes; su autor dice en su perfil de GitHub que trabaja en MedusaJS, pero el repo es personal). Saleor y Vendure, nada usable; commercetools, nada [L, A].
6. **Transportistas argentinos (Andreani, OCA, Correo Argentino) y factura de ARCA:** ninguno de los cuatro motores abiertos o composable tiene plugin, ni en GitHub, ni en npm, ni en su directorio. Donde sí hay es en WooCommerce (Andreani, OCA, Correo Argentino y ARCA, actualizados en noviembre de 2026), en Shopify (apps de terceros con pocas reseñas) y en Tiendanube [L, A].
7. **Lo que sí hay para cualquier motor en JavaScript:** SDKs de ARCA en npm, mantenidos en 2026 (`@afipsdk/afip.js` 1.3.0 del 2-nov; `@ramiidv/arca-facturacion` 7.1.0 del 19-nov; `facturas` 0.28.0 del 17-nov; `@arcasdk/core` 2.0.2 del 4-sep) y el SDK oficial de Mercado Pago (`mercadopago` 3.6.2, 1,43 millones de descargas en el último mes). Son bibliotecas, no plugins: la integración con el motor la escribe alguien [L, A].

## 1. Tabla por motor

| Motor | Quién lo hizo y licencia | Cómo cobra | Precio de lista (página oficial) | Precio real declarado | Escala |
|---|---|---|---|---|---|
| **Medusa** | MedusaJS, Inc.; fundada por Nicklas Gellner, Sebastian Rindom y Oliver Juhl (TechCrunch 2022). Licencia MIT, salvo RBAC y SSO, que desde el 11-ago-2026 son "Enterprise Edition materials" con licencia comercial (archivo `ENTERPRISE-LICENSE.md`) | Nube por plan mensual; "0% GMV platform fee"; el autoalojado no paga licencia (salvo lo Enterprise) | Develop US$ 29, Launch US$ 99, Scale US$ 299 por mes; Enterprise "Custom". Entornos extra US$ 60, asientos extra US$ 30, horas de cómputo US$ 0,16 sobre lo incluido [L, A1] | Hueco | 37.372 estrellas, 745 commits en 90 días, versión v2.23.0 del 20-nov-2026 [L, A1]; 1,43 millones de descargas de `@medusajs/medusa` en el último mes (incluye integración continua) [L, A2]; ronda semilla de US$ 8 millones en jul-2022 (blog propio) [S, A2]; una Serie A de US$ 6,5 millones aparece solo en un agregador sin fecha [S, E6] |
| **Saleor** | Saleor Commerce; nació en la agencia Mirumee (proyecto desde 2013, empresa desde 2020), fundadores Mirek Mencel y Patryk Zawadzki. BSD-3-Clause | Nube con tope de GMV y porcentaje sobre el excedente; autoalojado sin licencia | Sandboxes gratis; Select US$ 1.599 por mes hasta US$ 200.000 de GMV mensual y 0,8% sobre el excedente; Volume US$ 3.999 hasta US$ 1 millón y 0,4%; Enterprise "Negotiable"; extras: Accelerator US$ 6.000 y Forward Deployed Engineering US$ 12.000, acreditados en 12 meses [L, A1] | Hueco | 23.594 estrellas, 99 commits en 90 días en la rama principal, versión 3.23.50 del 17-nov-2026 [L, A1]; semilla de US$ 2,5 millones (2021) y extensión de US$ 8 millones (feb-2024, Target Global y Zalando); clientes nombrados: Lush y Breitling (TechCrunch) [L, B2] |
| **Vendure** | Vendure GmbH (Viena según CB Insights; sociedad de mayo de 2022). Su blog de feb-2026 cuenta que lo financió la agencia Elevantiq, dueña mayoritaria, y que cierra esa agencia para enfocarse en Vendure. GPLv3 con excepción para plugins, o licencia comercial con los planes pagos | Suscripción por plan, "no fee on revenue, gross merchandise value, orders, or users"; planes lanzados en oct-2026 | Framework gratis; Starter €199, Growth €599, Scale €2.499 por mes (anual, sin IVA); Enterprise desde €60.000 por año. Lo pago son funciones B2B y soporte; Vendure Cloud en beta cerrada, disponible en el primer trimestre de 2027 [L, A1] | Hueco | 8.612 estrellas, 786 commits en 90 días, v3.8.2 del 12-nov-2026 [L, A1]; 238.482 descargas de `@vendure/core` en el último mes [L, A2]; la agencia que lo financiaba facturaba "nearly €3M" [L, C] |
| **commercetools** | commercetools GmbH, Múnich; nació de REWE. Propietario, SaaS | Licencia anual por contacto; la página dice "order-based approach" y no GMV; se compra también por Google Cloud o AWS Marketplace | Sin cifras; "Contact us for more information on pricing plans"; prueba gratis sin plazo publicado; add-ons (Checkout, regiones, B2B) aparte [L, A] | Mediana de US$ 151.200 por año, n = 5 (Vendr, vía buscador y CostBench) [S, C5]. Costos ocultos según CostBench: integrador 25–50% de la licencia, desarrolladores 15–40% [S, D5] | US$ 145 millones en 2019 (Insight Partners, valuación ~US$ 300 millones) y US$ 140 millones en 2021 (Accel, valuación US$ 1.900 millones) [L, B2]; en feb-2025 despidió ~10% del personal y su CEO escribió que no alcanzaron "aggressive revenue growth targets"; ARR "far beyond" US$ 100 millones a jul-2024 [L, B2]; ~650 empleados según Built In (abr-2026) [S, C4]. El SDK en TypeScript tiene 657.374 descargas en el último mes [L, A2] |
| **Shopify headless** (Hydrogen, Oxygen, Storefront API, Plus) | Shopify Inc. Hydrogen es MIT; la plataforma es propietaria | Plan mensual; tarifa por usar un proveedor de pago externo (2%, 1%, 0,6% y 0,2% según plan; ver `shopify.md`). Oxygen "available at no extra charge on paid Shopify plans", menos los planes Agentic | Planes de `shopify.md`; Plus "Starts at $2,300 USD/mo", con contrato de 1 o 3 años [L, A1] | Plus: tarifa variable sobre el GMV de ~0,35% (3 años) o ~0,40% (1 año), con tope de ~US$ 40.000 por mes, según guías de agencias; G2 todavía muestra 0,25% sobre US$ 800.000 al mes. Shopify no lo publica [S, D5] | Hydrogen: 2.183 estrellas, último lanzamiento del 10-nov-2026; `@shopify/hydrogen`, 583.447 descargas en el último mes [L, A1]. Escala de la empresa en `shopify.md` |
| **VTEX FastStore** | VTEX; FastStore es MIT | Cargo fijo más % del GMV, contratos de 12 a 36 meses (`vtex.md`) | La página de precios no publica nada; formulario de ventas [L, A] | VTEX "Not in Vendr's deal flow"; CostBench cita cargos de 0,5% a 2,5% del ingreso por mes con una sola fuente [S, D6] | FastStore: 219 estrellas, v4.10.2 del 3-nov-2026; `@faststore/core`, 65.790 descargas en el último mes [L, A1]. Escala de la empresa en `vtex.md` |
| **Tiendanube Storefront API** | Tiendanube; propietaria | El plan de la tienda (planes en `tiendanube.md`); el frontend lo paga quien lo construye | Sin precio publicado para la API; habilitación manual por tienda, pidiéndola con link, contacto técnico y descripción del proyecto [S, A2] | Hueco | Sin repos ni paquetes públicos de la API de vitrina en GitHub (búsqueda: 0 resultados propios) [L, A] |
| **WooCommerce headless** | Automattic; GPL-2.0 | Núcleo gratis; alojamiento y extensiones aparte (`woocommerce.md`) | Gratis. La Store API es pública, sin autenticación para leer, con carrito y checkout [L, A1] | Hueco | 10.609 estrellas, 11.3.1 del 19-nov-2026 [L, A1] |
| **Adobe Commerce** (Magento) | Adobe; Magento Open Source sigue en GitHub con licencia OSL-3.0 (2.4.10-alpha1 del 13-oct-2026). La edición comercial es propietaria | Por contacto; las descripciones legales de Adobe definen el "Pricing Level" por tramos de GMV y valor medio de pedido ("AOV") o por tope de pedidos [S, A3] | Sin precio público [S, A3] | Mediana de US$ 286.000 por año, n = 5 (Vendr vía CostBench); otra página de CostBench da ~US$ 22.000 con n = 23. No coinciden [S, C5] | magento2: 12.242 estrellas, 2.638 temas abiertos [L, A1]. Tiendas en Argentina en `adobe-commerce.md` |

Notas sobre la tabla:

- **El cambio de licencia de Medusa** es de este año. El commit "chore: update license" del 11-ago-2026 agregó `ENTERPRISE-LICENSE.md`, que dice: "Possession of or access to the source code does not grant a license" para los archivos de RBAC y SSO. El resto sigue siendo MIT [L, A1].
- **Vendure, cambio de modelo:** las funciones pagas son B2B (cuentas de empresa, cotizaciones, aprobaciones, precios por contrato). Su blog promete "Nothing that's open source today will be moved behind a paywall" [L, A, C para la promesa].
- **Vendure sacó sus plugins de pago del núcleo** el 30-mar-2026 ("Remove community plugins from monorepo"). Hoy viven en `vendurehq/community-plugins`: Braintree, Mollie y Stripe [L, A1].
- **Las descargas de npm** cuentan instalaciones automáticas (integración continua, despliegues). Sirven para comparar entre sí, no para contar tiendas [inferencia].

## 2. Quién deja controlar el checkout y a qué precio

| Motor | ¿El checkout es propio? | Lo que dice la fuente | Precio para tenerlo |
|---|---|---|---|
| Medusa, Saleor, Vendure | Sí: el carrito y el pago se arman sobre la API del motor | Medusa y Vendure no traen vitrina obligatoria; Saleor ofrece su "Checkout API" [L, A] | US$ 0 de licencia autoalojado (Medusa sin RBAC ni SSO); en la nube, desde US$ 29 (Medusa), €199 (Vendure, con funciones B2B) o US$ 1.599 (Saleor) por mes |
| commercetools | Sí, por API; o el add-on "Checkout" | El Checkout de commercetools trae conectores para Adyen y PayPal; para otro proveedor hay que crear un "Organization Connector" [L, A1] | Por contacto (add-on aparte de la licencia) |
| Adobe Commerce y Magento Open Source | Sí | Mercado Pago ofrece Checkout Pro y Checkout API en su módulo [L, A] | Open Source sin licencia; comercial por contacto |
| WooCommerce headless | Sí, con la Store API (`POST /wc/store/v1/checkout`) | La documentación no garantiza que cada pasarela funcione: "cannot comprehensively list all expected requests for all payment gateways" y manda a consultar al autor del plugin [L, A1] | US$ 0 de licencia |
| Shopify (Hydrogen) | No: la vitrina es propia y la compra va al checkout de Shopify | "The response includes a URL that redirects customers through Shopify's web checkout" [L, A1]. Personalización del checkout "Limited" en Basic, Grow y Advanced, "Full" en Plus [L, A1] | Checkout completo: Plus, desde US$ 2.300 por mes con contrato de 1 o 3 años |
| VTEX FastStore | No: redirige al checkout de VTEX | El código de FastStore (`redirectToCheckout.ts` y `pages/checkout.tsx`) hace `window.location.href` a `storeConfig.checkoutUrl` [L, A1] | Lo que cobre VTEX por contrato |
| Tiendanube Storefront API | No: "entrega la compra al checkout alojado de Tiendanube" | El endpoint de checkout devuelve una URL; el pago se completa en el navegador [S, A2] | El plan de la tienda; no se publica una opción de checkout propio |

**Un costo que aparece en Argentina con Shopify:** Shopify Payments no está disponible en Argentina (la lista oficial de países incluye solo a México en América Latina) [L, A1]. En lo leído, una tienda argentina que cobra con Mercado Pago paga la tarifa por proveedor externo de su plan (2% en Basic y 0,2% en Plus, según `shopify.md`). Que esa tarifa se aplique a la app oficial de Mercado Pago es inferencia por la regla general; no se leyó un caso.

## 3. Matriz de lo local

Estado: **oficial** (de la marca, o del motor), **comunidad mantenida** (cambio en los últimos 12 meses), **comunidad abandonada** (más de 12 meses sin cambio), **no hay** (búsqueda hecha sin resultado), **hueco** (no se pudo verificar). Fecha: último cambio visible (versión, commit o actualización del directorio).

| Motor | Mercado Pago | Transportistas argentinos | Factura de ARCA |
|---|---|---|---|
| **Medusa** | **Comunidad mantenida.** `@nicogorga/medusa-payment-mercadopago` 0.4.0, **14-sep-2026**; Medusa ≥ 2.21; Payment Brick y suscripciones; 30 estrellas; 2.425 descargas en el último mes. Figura en la página de integraciones de Medusa en dos entradas ("Mercadopago" y "MercadoPago") sin marca de oficial. **Abandonadas:** `minskylab/medusa-payment-mercadopago` (último commit **3-oct-2023**, Medusa v1, Checkout Pro); `marcosgomesneto/...` (**12-nov-2024**, PIX de Brasil, "soon" para Medusa 2.0); `medusa-payment-mercadopago` en npm (**13-ago-2022**) [L, A1] | **No hay.** GitHub: 0 repos para Andreani, OCA o Correo Argentino con Medusa. La página de integraciones lista 18 de logística, ninguna latinoamericana. El único paquete regional, `medusa-latam`, empieza por Brasil (Correios, PIX), creado el **2-nov-2026** con 0 estrellas [L, A1] | **No hay** plugin. Las integraciones de facturación listadas son de Polonia y Alemania [L, A1] |
| **Saleor** | **No hay usable.** Apps oficiales (`saleor/apps`): Stripe, Adyen ("available only on Saleor Cloud"), NP Atobarai (Japón) y de prueba. En la comunidad, `fedexin40/saleor-app-mercadopago`, creado el **21-nov-2026**, 0 estrellas; su README es la plantilla de Saleor App, sin rastro de funciones [L, A1] | **No hay.** Hay un monorepo comunitario para Colombia (Servientrega), actualizado el **22-nov-2026** [L, A1] | **No hay** [L, A1] |
| **Vendure** | **No hay.** GitHub: 0 repos. Directorio de plugins: 49 en total, el único de pagos visible es HULO Payments. Plugins de pago mantenidos por Vendure: Braintree, Mollie y Stripe [L, A1] | **No hay.** GitHub y npm: 0 [L, A1] | **No hay** plugin argentino. Existe un plugin de facturas genérico (`@pinelab/pinelab-invoice-plugin`), sin país [L, A1] |
| **commercetools** | **No hay.** Conectores del Checkout: Adyen y PayPal; el menú de Mercado Pago no nombra a commercetools; GitHub: 0 [L, A1] | **Hueco.** El buscador de socios (marketplace.commercetools.com redirige a commercetools.com/partners) no se pudo leer; GitHub: 0 | **No hay** en GitHub; socios sin leer (hueco) |
| **Shopify** (también con Hydrogen, porque el checkout es de Shopify) | **Oficial** (app de Mercado Pago: Checkout Pro y Checkout API con tarjetas, "en el checkout de Shopify"). Fecha del último cambio: hueco. La documentación no menciona Hydrogen; que funcione igual en headless es inferencia porque el checkout es el mismo [L, A2] | **Terceros:** Escala Envíos (Andreani y Correo Argentino; 5,0 con 4 reseñas), Shipy 2 (Andreani y Correo Argentino con puntos de retiro; 4,1 con 13), Correo Argentino Integración y Zipnova. La cotización de un transportista externo en el checkout está "available on Shopify Advanced and Shopify Plus"; Grow lo suma con un cargo mensual o con pago anual [L, A1]. Fechas de cada app: hueco | **Terceros:** Profitar (5,0 con 2 reseñas), Emitio (5,0 con 6) y FacturAR (sin reseñas), las tres con CAE de ARCA [L, B2]. Fechas: hueco |
| **VTEX FastStore** | **Oficial** (Mercado Pago para VTEX: Checkout Pro y Checkout API, Argentina incluida). Funciona sobre el checkout de VTEX, al que FastStore redirige. Fecha: hueco [L, A2] | **Hueco.** No se pudo buscar en la VTEX App Store (la búsqueda por URL da 404). Zipnova dice integrarse con VTEX (informe de envíos, [L, A, C para su dicho]); una app de Andreani para VTEX no apareció [S] | **Hueco.** No apareció una app de ARCA para VTEX [S, dato 6] |
| **Tiendanube Storefront API** | En la tienda, Mercado Pago tiene integración nativa (`mercado-pago.md`). En headless, la ayuda confirma solo Pago Nube y Envío Nube; el resto de las apps "se validan caso a caso" [S, A2] | Igual: Envío Nube confirmado; Andreani tiene app en la tienda de Tiendanube, en headless "caso a caso" [S, A2] | Las apps de factura de la tienda trabajan sobre pedidos; en headless no está confirmado [inferencia, dato 6] |
| **WooCommerce** | **Oficial:** `woocommerce-mercadopago` 8.10.3, **18-nov-2026**, 100.000+ instalaciones, 693 calificaciones (repo `mercadopago/cart-woocommerce`). En headless depende de que la pasarela soporte la Store API: hueco [L, A1] | **Andreani:** `andreani-shipping` 1.8.9, **6-nov-2026**, 1.000+, autor "integracionandreani" (que sea de Andreani no está verificado); `wanderlust-andreani-shipping` 2.0.205, **11-dic-2024** (abandonado). **OCA:** `oca-for-woocommerce` 4.1.7, **5-nov-2026**, 100+ (CRPlugins). **Correo Argentino:** `correo-argentino-for-woocommerce` 3.0.8.1, **2-nov-2026**, 1.000+, autor "Correo Argentino". **Agregador:** `enviopack-argentina` 1.0.19, **30-jun-2026**, autor Enviopack. Zipnova: sin plugin en el directorio [L, A1] | **Comunidad mantenida:** `integracion-afip` 4.1.0, **6-nov-2026**, 100+ (CRPlugins); `contabilium-oficial-para-woo` 3.0.2, **29-sep-2026** (del sistema de gestión Contabilium); `facturante` 1.24.0, **24-oct-2025**. En GitHub: `fedealvz/Woo-iFactura` (**27-ago-2026**, 11 estrellas) y `sarthouse/open-facturarca` (**6-nov-2026**) [L, A1] |
| **Adobe Commerce** (Magento) | **Oficial:** `mercadopago/adb-payment` v1.15.7, **27-oct-2026**; `adb-payment-23` para Magento 2.3 (**2-jul-2026**); el viejo `cart-magento2` está archivado [L, A1] | **Andreani, publicado por Andreani:** organización `andreani-publico` en GitHub, `magento-2.3` (último cambio **29-abr-2025**) y `magento-2.2` (**27-ene-2025**). En el Marketplace de Adobe, "andreani" da 0 resultados. **OCA y Correo Argentino:** GitHub, 0 [L, A1] | **Abandonado:** `25Watts/magento2-afip`, **26-nov-2020**, 1 estrella. Nada más [L, A1] |

Para todos los motores en JavaScript (Medusa, Vendure, el frontend de Hydrogen o FastStore, las apps de Saleor) hay piezas sueltas en npm: SDKs de ARCA mantenidos (los de la respuesta corta) y clientes de transportistas, casi todos viejos: `node-andreani-api` 1.2.0 (**28-oct-2022**), `@nchsala/andreani` (**24-oct-2020**), `enviopack-node` (**2-jul-2020**), `ylazzari-correoargentino` 0.1.0 (**14-may-2026**), y `@ar-agents/shipping` 0.4.2 (**13-jul-2026**, "Argentine shipping carriers (Andreani, OCA, Correo Argentino) as drop-in tools" para agentes de IA) [L, A1, dato 6 para su calidad: no se probaron].

## 4. Fuentes

| Fuente | Tipo | Calificación | Marca |
|---|---|---|---|
| https://medusajs.com/pricing/ | precios oficiales | A1 | [L] |
| https://github.com/medusajs/medusa (API; `LICENSE`, `ENTERPRISE-LICENSE.md`, commits) | repositorio | A1 | [L] |
| https://medusajs.com/integrations/ | directorio de integraciones | A1 | [L] |
| https://docs.medusajs.com/resources/integrations | documentación | A1 | [L] |
| https://medusajs.com/blog/announcement-8m-usd-seed-round-to-build-the-leading-ecom-platform-for-devs/ | blog propio | A2 | [S] |
| https://saleor.io/pricing | precios oficiales | A1 | [L] |
| https://github.com/saleor/saleor y https://github.com/saleor/apps | repositorios | A1 | [L] |
| https://techcrunch.com/2024/02/06/open-source-headless-commerce-builder-saleor-pulls-in-8m-round-led-by-target-global-and-zalando | prensa | B2 | [L] |
| https://vendure.io/pricing | precios oficiales | A1 | [L] |
| https://vendure.io/letter (blog del 4-feb-2026, nota de oct-2026) | blog propio | A para hechos de la empresa, C para cifras | [L] |
| https://docs.vendure.io/plugins | directorio de plugins (49) | A1 | [L], solo la primera página de 12 |
| https://github.com/vendurehq/vendure y https://github.com/vendurehq/community-plugins | repositorios | A1 | [L] |
| https://www.cbinsights.com/company/vendure | agregador | C4 | [S] |
| https://commercetools.com/pricing | precios oficiales (sin cifras) | A1 | [L] |
| https://docs.commercetools.com/checkout/payment-connectors-applications | documentación | A1 | [L] |
| https://techcrunch.com/2021/09/13/commercetools-raises-140m-at-a-1-9b-valuation-as-headless-commerce-continues-to-boom | prensa | B2 | [L] |
| https://techcrunch.com/2025/02/26/commercetools-a-pioneer-in-headless-commerce-lays-off-dozens-of-staff | prensa | B2 | [L] |
| https://builtin.com/company/commercetools/faq/stability-growth | agregador | C4 | [S] |
| https://vendr.com/marketplace/commercetools | datos de compras | C5 (n = 5) | [S], 403 al abrir |
| https://www.costbench.com/compare/commercetools-vs-vtex/ y https://www.costbench.com/compare/adobe-commerce-vs-commercetools/ | agregador de Vendr y otras | C5 / D5 para costos ocultos | [L] |
| https://shopify.dev/docs/storefronts/headless/hydrogen/fundamentals | documentación | A1 | [L] |
| https://shopify.dev/docs/api/storefront | documentación | A1 | [L] |
| https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/cart/manage | documentación | A1 | [L] |
| https://www.shopify.com/plus/pricing | precios oficiales | A1 | [L] |
| https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries | ayuda oficial | A1 | [L] |
| https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/third-party-carrier-calculated-shipping | ayuda oficial | A1 | [L] |
| https://apps.shopify.com/search?q=andreani y ?q=afip | tienda de apps | B2 | [L] con navegador |
| https://elogic.co/blog/shopify-plus-pricing-2026/ , https://g2.com/products/shopify-plus/pricing , https://beancount.io/ca/blog/2026/09/12/shopify-plus-platform-fee-increase-variable-fee-merchant-guide | agencias y reseñas sobre la tarifa variable de Plus | D5 | [S] |
| https://github.com/Shopify/hydrogen | repositorio | A1 | [L] |
| https://www.vtex.com/en-us/pricing/ | precios oficiales (sin cifras) | A1 | [L] |
| https://github.com/vtex/faststore (README, `packages/core/src/sdk/cart/redirectToCheckout.ts`, `packages/core/src/pages/checkout.tsx`) | código | A1 | [L] |
| https://apps.vtex.com/ | tienda de apps | — | no se pudo buscar |
| https://ayuda.tiendanube.com/es_AR/socios-tecnologicos/que-es-la-storefront-api-de-tiendanube-y-para-que-sirve | ayuda oficial, sin fecha | A2 | [S] (la herramienta resumió, no copió) |
| https://developer.woocommerce.com/docs/apis/store-api/ y .../resources-endpoints/checkout/ | documentación | A1 | [L] |
| https://api.wordpress.org/plugins/info/1.2/ (búsquedas: andreani, oca, correo argentino, enviopack, zipnova, afip, arca, mercado pago) | directorio de plugins | A1 | [L] |
| https://github.com/mercadopago (lista de repos, `cart-woocommerce`, `adb-payment`) | repositorios oficiales | A1 | [L] |
| https://www.mercadopago.com.ar/developers/es/docs/shopify/introduction | documentación oficial | A2 | [L] |
| https://www.mercadopago.com.ar/developers/es/docs/vtex/introduction | documentación oficial | A2 | [L] |
| https://commercemarketplace.adobe.com/catalogsearch/result/?q=andreani | marketplace | A1 | [L] |
| https://github.com/andreani-publico | repositorios de Andreani | A1 | [L] |
| https://github.com/magento/magento2 | repositorio | A1 | [L] |
| https://helpx.adobe.com/legal/product-descriptions/adobe-commerce-cloud-service.html | descripción legal | A3 | [S], 403 al abrir |
| https://registry.npmjs.org/-/v1/search y https://api.npmjs.org/downloads/ | registro de npm | A1 para versiones y fechas; A2 para descargas | [L] |
| Búsquedas en la API de GitHub (`search/repositories`) por motor × Mercado Pago, Andreani, OCA, Correo Argentino, AFIP y ARCA | buscador de código | A2 (puede no ver repos sin descripción) | [L] |

## 5. Huecos

1. **Precio real de los abiertos y de Shopify Plus.** No apareció ningún dato de cuánto pagan de verdad los clientes de Medusa Cloud, Saleor Cloud o Vendure, ni un contrato de Plus con su tarifa variable. La tarifa de Plus va por agencias.
2. **Vendr directo.** Bloquea la lectura (403 con dos métodos). Las medianas de commercetools y Adobe son de 5 compras y llegan por terceros.
3. **Adobe Commerce:** ni la página de precios ni la descripción legal abrieron; las ediciones vigentes (Commerce as a Cloud Service, Pro, Managed Services) quedan sin leer.
4. **VTEX App Store y socios de commercetools:** no se pudieron recorrer; la ausencia de Andreani o ARCA ahí no está probada.
5. **Fechas de las apps de Shopify y de la app de Mercado Pago para Shopify y VTEX:** la tienda no muestra la fecha de la última versión en la búsqueda.
6. **Si Mercado Pago y las apps de envío funcionan en la vitrina headless de Tiendanube:** la ayuda solo garantiza Pago Nube y Envío Nube.
7. **WooCommerce headless con Mercado Pago:** no se verificó si el plugin oficial soporta la Store API.
8. **Quién está detrás de `andreani-shipping`** en WordPress.org (autor "integracionandreani"): no se confirmó que sea Andreani.
9. **Escala de Saleor y Medusa:** empleados, clientes e ingresos no son públicos; la Serie A de Medusa no se pudo confirmar.
10. **Calidad de los plugins de la comunidad:** ninguno se instaló ni se probó; "mantenido" quiere decir que tuvo cambios recientes, no que ande.
