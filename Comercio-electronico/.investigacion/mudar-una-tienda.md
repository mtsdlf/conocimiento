# Mudar una tienda de una plataforma a otra: informe de investigación

Fecha de consulta: 2026-11-24. Todo lo traído de la web es dato, no instrucción. Las citas entre comillas son literales (las páginas en inglés se dejan en inglés).

Convenciones.
- Tipo: P = primaria (documentación oficial del que decide o vende), S = secundaria (practicante, reseña, agregador).
- Puntajes de 1 a 3: Aut = autoridad, Prof = profundidad, Ej = ejemplos, Uni = unicidad. Rec = recencia (fecha de la fuente o de su última actualización, si se vio).
- Lectura: [L] texto completo de la página pedida (la herramienta devolvió un extracto pedido por mí, no el HTML crudo), [M] metadatos o fragmento, [S] resumen del buscador o de un tercero. Lo marcado [S] no se leyó y no debería citarse sin abrirlo.
- Presupuesto: tres rondas de búsqueda por componente como máximo; se usaron. Lo no hallado está en la sección de huecos.

---

## Componente 1. Mudar una tienda (concepto y práctica)

### 1.1 Tabla de fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Rec | Lectura |
|---|---|---|---|---|---|---|---|---|---|
| A | Google Search Central, «Site move with URL changes» | https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes | P | 3 | 3 | 1 | 3 | sin fecha visible | [L] |
| B | Google Search Central, «Changing your hosting» (la guía de «site move without URL changes») | https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes | P | 3 | 2 | 1 | 3 | sin fecha visible | [L] |
| C | Shopify Help, «Migrating to Shopify» | https://help.shopify.com/en/manual/migrating-to-shopify | P | 3 | 2 | 1 | 2 | sin fecha visible | [L] |
| D | Tiendanube Ayuda, migrar de Shopify a Tiendanube | https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube | P | 3 | 3 | 1 | 3 | sin fecha visible | [L] |
| E | Tiendanube Ayuda, migrar de Mercado Shops a Tiendanube | https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-mi-tienda-online-de-mercado-shops-a-tiendanube | P | 3 | 2 | 1 | 3 | sin fecha visible | [L] |
| F | Tiendanube Ayuda, redireccionamiento 301 | https://ayuda.tiendanube.com/es/articles/692035-que-es-el-redireccionamiento-301-y-como-lo-uso | P | 3 | 1 | 1 | 2 | sin fecha visible | [S] |
| G | Tiendanube Evolución, migración sin perder SEO (servicio comercial de Tiendanube) | https://www.tiendanube.com/mx/evolucion/seo | P (comercial, interesada) | 2 | 2 | 1 | 2 | 2026-06-26 (mod. 2026-06-29) | [L] |
| H | Ahrefs, guía de migración web (Patrick Stox; versión en español) | https://ahrefs.com/blog/es/migracion-web | S (practicante) | 3 | 3 | 1 | 2 | 2021-12-08 | [L] |
| I | SALT.agency, «Only 27% of domain migrations recover in 90 days» (Dan Taylor) | https://salt.agency/blog/27-of-domain-migrations-recover-in-90-days (URL canónica inferida de los enlaces para compartir; la leída fue https://salt.agency/?p=18880405) | S (estudio con método, con dataset propio y colaborativo) | 2 | 3 | 2 | 3 | 2026-06-26 | [L] |
| J | Search Engine Journal, «What is a migration hangover» (Sophie Brannon, StudioHawk) | https://www.searchenginejournal.com/what-is-a-migration-hangover-traffic-drop-how-do-you-avoid-it/ | S (practicante, agencia) | 2 | 2 | 2 | 1 | 2026-06-05 | [L] |
| K | Aleyda Solís, guías y checklists para migraciones web | https://aleydasolis.com/en/search-engine-optimization/seo-for-web-migrations | S (practicante reconocida) | 3 | s/d | s/d | s/d | s/d | [S] (la página devolvió 403) |
| L | Search Engine Land, caso de colapso por soft 404 tras mudanza de dominio (cripto, enero 2022) | https://searchengineland.com/soft-404s-indexing-issues-traffic-collapse-477116 | S (caso de practicante) | 2 | s/d | 2 | 2 | s/d | [S] (403) |
| M | Sitebulb, «When Website Migrations Go Wrong» | https://sitebulb.com/resources/guides/when-website-migrations-go-wrong-a-practical-guide-to-disaster-recovery/ | S | 2 | s/d | s/d | s/d | s/d | [S] |
| N | Shopify Help, crear y gestionar redirecciones de URL | https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect | P | 3 | s/d | 1 | 2 | s/d | [S] |
| O | Ahrefs/Dynadot y otros que repiten a Google (retención de 1 año, no redirigir a la home) | — | — | — | — | — | — | — | no contados: parafrasean A (una sola fuente) |

### 1.2 Qué datos pasan y cuáles no

- Shopify lista lo que «might want to migrate»: productos, clientes, pedidos históricos, tarjetas de regalo / certificados / crédito de tienda, blogs y páginas. Ofrece cinco métodos, del menos al más técnico: copiar y pegar, CSV, app de migración, un Shopify Partner, o una solución a medida con la API. Orden recomendado: «Import your products first, then your customers, and then any historical orders». https://help.shopify.com/en/manual/migrating-to-shopify
- Shopify, CSV de productos: «A product can have up to 3 options.»; «You can add up to 250 images to a product.»; las imágenes deben estar en una URL pública con https y sin contraseña; «Gift card details can be edited in bulk, but a gift card can't be created by importing a CSV»; las variantes con Option1 distinto a la tienda existente «deletes existing variant IDs and creates new ones, which can break third-party dependencies». Cada producto va a una sola colección por la columna Collection. https://help.shopify.com/en/manual/products/import-export/using-csv
- Contraseñas de clientes: no se migran. El plugin Shopify Data Migrator de WooCommerce.com dice: «User passwords will not be imported as Shopify APIs do not provide password data for security reasons.» Esa evidencia es de la dirección Shopify a WooCommerce; no encontré una fuente oficial que lo confirme en la dirección inversa ni hacia Tiendanube. https://woocommerce.com/document/shopify-data-migrator
- Pedidos históricos hacia Tiendanube: no se migran. «El historial de órdenes no se migrará a Tiendanube.» (aparece en la guía desde Shopify y en la guía desde Mercado Shops; en ambas queda visible solo en la app de email marketing elegida, p. ej. Perfit / Marketing Nube). https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube y https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-mi-tienda-online-de-mercado-shops-a-tiendanube
- Hacia Tiendanube desde Shopify, por tipo de dato (guía oficial): productos por CSV o apps (Automágico, AutoAzur, Astroselling, Ventiapp; «usar el SKU» para cruzar); clientes vía app de email marketing instalada en ambas tiendas (Marketing Nube, Mailchimp, Brevo, Doppler); descuentos exportados a CSV y luego «contactar a soporte» para importarlos; reseñas exportadas y enviadas al soporte de una app de reseñas (Revie, Lily Review, Trusty); envíos y medios de pago no migran, se configuran de nuevo (Pago Nube, Mercado Pago, Ualá Bis, MODO, Nave, GOCuotas, PayPal); el dominio no se transfiere solo, se cambian los DNS. Páginas y blog no se mencionan en esa guía. https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube
- Desde Mercado Shops, la app «Mercadoshops a Tiendanube» trae «productos con sus características: fotos, categorías, descripciones, precio, stock, variantes, etc.»; el tope de 20.000 líneas aplica a la carga manual por planilla. https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-el-catalogo-de-productos-de-mercado-shops-a-tiendanube [L]. El blog de Tiendanube agrega que el historial de ventas se respalda aparte con «Descargar Excel de ventas» de Mercado Libre. https://www.tiendanube.com/blog/como-migrar-de-mercado-shops-a-tiendanube/ [L]
- Discrepancia de fechas dentro de la propia Tiendanube: el cuerpo del blog dice que Mercado Shops «dejó de existir a finales de 2025», y su FAQ dice que se anunció en enero de 2025 y que «Estará activa hasta el 31 de diciembre de 2026». (El cierre como tal ya está documentado en la base y no se repite; solo se deja la discrepancia.) https://www.tiendanube.com/blog/como-migrar-de-mercado-shops-a-tiendanube/ (datePublished 2026-02-27; «Actualizado el 10/04/2026»)
- Tiendanube Evolución (servicio asistido) dice que migra el blog con una 301 por entrada y que exporta antes títulos SEO, meta descripciones y texto ALT. https://www.tiendanube.com/mx/evolucion/seo
- Suscripciones y tokens de pago (tarjetas guardadas): no encontré fuente primaria. Ver huecos.

### 1.3 Direcciones y redirecciones 301

- Google: usar redirecciones permanentes del lado del servidor («301 or 308»); «Permanent redirects don't cause a loss in PageRank»; no redirigir muchas URL viejas a una página irrelevante como la home, porque puede tomarse como soft 404; cadenas «ideally no more than 3 and fewer than 5» saltos; «Keep the redirects for as long as possible, generally at least 1 year.» https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- Pasos de Google para mudanza con cambio de URL: revisar buenas prácticas, preparar y probar el sitio nuevo, preparar el mapa de URL viejas a nuevas, redirigir, monitorear tráfico en ambas. Mismo enlace.
- Shopify: «You can set up redirects for all your important pages to help preserve your SEO ranking.» https://help.shopify.com/en/manual/migrating-to-shopify . Según el buscador (resumen, sin leer la página de ayuda): Shopify permite importar redirecciones por CSV (dos columnas, vieja y nueva) y no traduce solas las URL de otra plataforma; el mapa lo arma uno. https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect [S]
- Límites de redirecciones en Matrixify por trabajo: Basic 10.000, Big 100.000. https://matrixify.app/pricing/ [L]
- Tiendanube: «Configuración > Redireccionamientos 301»; campo «Nueva URL» sin dominio y con barra inicial; «Los redireccionamientos 301 son permanentes»; recomienda migrar todas las URL anteriores, incluidas categorías y productos; si el dominio está en un hosting externo, la redirección de dominio se hace allá. https://ayuda.tiendanube.com/es/articles/692035-que-es-el-redireccionamiento-301-y-como-lo-uso [S, texto vía buscador]. La app Redirect AI de Tiendanube cruza el sitemap público del sitio anterior con el nuevo y propone redirecciones que el comerciante aprueba. https://www.tiendanube.com/co/tienda-aplicaciones-nube/redirec-ai [S]
- La guía oficial Shopify a Tiendanube no trata las 301 en sus pasos («Redireccionamiento 301» solo aparece como ítem de menú). https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube . La guía de Mercado Shops tampoco dice nada de redirigir las URL viejas. https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-mi-tienda-online-de-mercado-shops-a-tiendanube

### 1.4 No perder el tráfico de los buscadores

- Herramienta de cambio de dirección de Search Console: solo para mover entre dominios o subdominios; «isn't needed» para HTTP a HTTPS, www a no-www ni rutas dentro del dominio; hay que enviarla por todas las variantes verificadas del dominio viejo. Sitemaps: guardar uno con las URL nuevas y otro con las viejas, enviar el nuevo, y las advertencias por redirección en el viejo «are expected». https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- Mudar sin cambio de URL (hosting o plataforma con las mismas URL): bajar el TTL del DNS «at least a week in advance» a un valor bajo (p. ej. «a few hours»); probar con un host temporal con `noindex`; sacar el `noindex` y el bloqueo de robots antes de mudar; mantener la verificación de Search Console; apagar el viejo cuando su tráfico llegue a cero. Tras el lanzamiento, caída temporal del rastreo y luego subida «over the next few days». https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes
- Ahrefs (Patrick Stox, 2021-12-08) distingue por tipo: mismas URL (hosting, plataforma, diseño) vs distintas (dominio, protocolo, ruta). Una mudanza de plataforma que conserva las URL cae en el primer grupo. Sus causas probables de caída: «redirects, uncrawlable pages, noindex, content changes or deletions, internal link changes, or technical SEO changes» (parafraseado del extracto). Recomienda plan de vuelta atrás, rastreo base, conjunto de páginas clave, y mantener un sitemap de URL viejas «durante algo de tiempo». https://ahrefs.com/blog/es/migracion-web
- Cuánto tarda en recuperarse, con tres fuentes que no coinciden.
  - Google (primaria): para un sitio mediano, «it can take a few weeks or more» hasta que Google muestra las URL nuevas; sitios grandes más. https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
  - SALT.agency (2026-06-26): 1.052 mudanzas de dominio, mediana 304 días, media 489 días; recuperación acumulada 22,8% al día 90, 59,5% al 365, 83,5% al 730, 86,1% al 1095; 13,9% sin recuperar a los tres años. Método: la mudanza se infiere por una caída de 60% o más con base de 50 visitas/mes; datos mensuales, margen ±30 días; muestra mezcla proyectos propios y colaborativos sin desglose; no analiza plataforma ni cambio de URL, solo mudanzas de dominio con 301. Además el titular («27%») no coincide con su propia tabla (22,8% al día 90). https://salt.agency/blog/27-of-domain-migrations-recover-in-90-days [L]
  - StudioHawk vía SEJ (2026-06-05): una caída temporal normal de 10-30% (otra sección dice 10-20%, recupera en 2 a 6 semanas); la «migration hangover» es 50% o más (o 30-50%+) sin estabilizarse tras 4 semanas, y en casos graves puede durar «12 to 18 months». Opinión de agencia, sin dataset. https://www.searchenginejournal.com/what-is-a-migration-hangover-traffic-drop-how-do-you-avoid-it/ [L]
  - Tiendanube Evolución (comercial): reindexación «usualmente 2 a 4 semanas» y caída temporal de 5% a 15% durante 2 a 4 semanas que «se recupera por completo». Fuente interesada y sin método. https://www.tiendanube.com/mx/evolucion/seo [L]
  - Lectura honesta: las cifras de agencias de plataforma son optimistas frente al único dataset grande; pero el dataset es de mudanzas de dominio con caídas grandes (detectadas por umbral), no de replatforming pyme con mismo dominio. No hay dato directo para el caso que nos importa.

### 1.5 Dominio y DNS

- Google: bajar TTL una semana antes; cambiar los DNS al nuevo destino; verificar con herramientas públicas de DNS que los ISP lo recogieron; revisar que firewall y protección DoS no bloqueen a Googlebot. https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes
- Tiendanube: el dominio no se transfiere automáticamente; se cambian los registros DNS. https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube . Dominio propio exige plan pago. https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-mi-tienda-online-de-mercado-shops-a-tiendanube
- Shopify: «Set up your domain» es el paso 9 de 11. https://help.shopify.com/en/manual/migrating-to-shopify
- Ahrefs: renovar el dominio viejo, mantener redirecciones a nivel DNS si se da de baja el hosting y mantener vigentes los certificados. https://ahrefs.com/blog/es/migracion-web

### 1.6 Orden de los pasos

Secuencia oficial de Shopify (11 pasos): importar contenido y datos; verificar y organizar productos; elegir y personalizar tema; envíos; impuestos; proveedor de pago y checkout; pedidos de prueba; cuentas de personal; dominio; POS (opcional); SEO con redirecciones y envío de sitemap (opcional). https://help.shopify.com/en/manual/migrating-to-shopify

Secuencia de Tiendanube desde Mercado Shops: crear cuenta de prueba; migrar catálogo; opcional sincronizar con Mercado Libre vía Astroselling, Ecomnube o Anymarket; plantilla; dominio; Mercado Pago y otros pagos; envíos; clientes. https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-mi-tienda-online-de-mercado-shops-a-tiendanube

Google (monitoreo): vigilar tráfico en ambas URL y mantener el sitio viejo hasta que Googlebot haya visitado cada URL vieja y nueva «at least once». https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes

Observación: ninguna de las fuentes leídas trae el encuadre «inventario, prueba, congelar cambios, corte, verificación» como tal. Lo más cercano es el flujo de Ahrefs (preparación, ejecución, prueba y monitoreo) y el de Google. «Congelar cambios» no aparece en ninguna fuente leída; queda como práctica propia a documentar sin cita.

### 1.7 Apps e integraciones a reemplazar

- Pagos, envíos y medios de cobro no migran: se vuelven a configurar (lista de Tiendanube en 1.2). https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube
- Mercado Libre y otros canales: Tiendanube nombra Astroselling, Ecomnube y Anymarket para mantener sincronizados catálogo, precios y stock con Mercado Libre. https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-mi-tienda-online-de-mercado-shops-a-tiendanube [L]
- Sistema de gestión: ninguna fuente leída lo trata. Hueco.

### 1.8 Qué suele salir mal (causas y casos)

- Causas listadas por StudioHawk: redirecciones faltantes, 302 en vez de 301, cadenas, redirecciones a páginas irrelevantes, `noindex` dejado desde staging, canonicals apuntando a URL viejas, cambios de contenido (títulos, metas, imágenes faltantes), regresión de velocidad, cambios innecesarios de URL, SEO convocado tarde. https://www.searchenginejournal.com/what-is-a-migration-hangover-traffic-drop-how-do-you-avoid-it/
- Caso fallido de ese artículo: un sitio SaaS cuya subdominio viejo quedó rastreable y generó canibalización; sin cifras. Caso exitoso: un distribuidor ecommerce de autopartes con SEO desde el inicio, «over $750,000 in organic revenue» en tres meses (cifra de la agencia, sin verificar). Mismo enlace.
- Caso con detalle (Search Engine Land): colapso tras una mudanza de dominio de enero de 2022 por soft 404 en 13 dominios de país; el dominio viejo siguió rastreándose. Solo se vio el resumen del buscador; no se pudo abrir (403). https://searchengineland.com/soft-404s-indexing-issues-traffic-collapse-477116 [S]
- Sitebulb recomienda primero verificar si la caída es real contra una proyección previa; sin esa línea base «every dip looks like a disaster» (parafraseado del resumen). https://sitebulb.com/resources/guides/when-website-migrations-go-wrong-a-practical-guide-to-disaster-recovery/ [S]
- Riesgos específicos de plataforma que sí están documentados: en Shopify, cambiar Option1/2/3 reasigna IDs de variantes y puede romper dependencias de terceros (ver 1.2); en Shopify las imágenes por CSV fallan si la URL no es pública o si se quitaron productos tras exportar. https://help.shopify.com/en/manual/products/import-export/using-csv
- No se encontraron fracasos documentados de pymes argentinas en replatforming (ni de Mercado Shops a Tiendanube). Hueco.

### 1.9 Recurso canónico del componente

Propuesta: dos piezas, en este orden.
1. Google Search Central, «Site move with URL changes» (https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) más «Changing your hosting» (https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes). Qué parte: los pasos, la retención de redirecciones de 1 año, la regla de no mandar todo a la home, y el TTL previo. En qué fijarse: separa mudanza con cambio de URL (dominio) de mudanza sin cambio; casi todo replatforming pyme con el mismo dominio cae en la segunda, pero si la plataforma nueva impone rutas distintas (p. ej. /products/) pasa a ser la primera aunque el dominio no cambie. Ninguna de las dos trae fecha visible.
2. Ahrefs, guía de migración web (https://ahrefs.com/blog/es/migracion-web): checklist previo/durante/posterior, en español, de un practicante reconocido. En qué fijarse: es de 2021 y su tabla de tipos ayuda a clasificar el caso; no trae datos propios de recuperación.
Para fijar expectativas de tiempo, citar el estudio de SALT.agency (https://salt.agency/blog/27-of-domain-migrations-recover-in-90-days) con sus límites (solo dominio, umbral de caída, titular inconsistente) y no las cifras optimistas de los servicios comerciales.
Para el lado Argentina, el canónico operativo es la guía oficial de Tiendanube desde Shopify (https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube), con la advertencia de que no cubre redirecciones.

---

## Componente 2. Ficha fechada de herramientas de migración (consulta 2026-11-24)

### 2.1 Tabla de fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Rec | Lectura |
|---|---|---|---|---|---|---|---|---|---|
| P | Shopify App Store, «Store Migration» (Shopify) | https://apps.shopify.com/store-migration | P | 3 | 2 | 1 | 3 | lanzada 2024-07-17 | [L] |
| Q | Matrixify, precios | https://matrixify.app/pricing/ | P | 3 | 3 | 1 | 3 | sin fecha | [L] |
| R | Shopify Help, importar por CSV | https://help.shopify.com/en/manual/products/import-export/using-csv | P | 3 | 3 | 2 | 3 | sin fecha | [L] |
| S | WooCommerce, importador CSV de productos | https://woocommerce.com/document/product-csv-importer-exporter/ | P | 3 | — | — | — | — | [L] pero el primer intento (otra URL) dio 404; esta sí abrió |
| T | WooCommerce, «Shopify Data Migrator» | https://woocommerce.com/document/shopify-data-migrator | P (de un plugin) | 2 | 2 | 1 | 2 | © 2026, sin versión | [L] |
| U | Tiendanube Ayuda, migrar catálogo / clientes (Mercado Shops, Shopify) | ver D y E en 1.1 | P | 3 | 2 | 1 | 3 | sin fecha | [L] |
| V | Tiendanube blog, Mercado Shops a Tiendanube | https://www.tiendanube.com/blog/como-migrar-de-mercado-shops-a-tiendanube/ | P (comercial) | 2 | 2 | 1 | 2 | 2026-02-27; act. 2026-04-10 | [L] |
| W | LitExtension, FAQ de precio | https://litextension.com/faq/docs/ordering-and-payment/payment/how-much-does-the-service-cost/ | P | 2 | 2 | 1 | 2 | sin fecha | el fetch de esta URL dio 404; el contenido de la tabla de abajo viene de https://litextension.com/pricing.html [L] |
| X | Cart2Cart, reseña de ecommerce-platforms.com (Bogdan Rancea) | https://ecommerce-platforms.com/ecommerce-resources/cart2cart-review | S (reseña de afiliado probable) | 2 | 2 | 2 | 2 | act. 2025-07-22 | [L] |
| Y | Cart2Cart, página de precios propia | https://www.cart2cart.com/pricing/ | P | — | — | — | — | — | no se pudo leer (página vacía para la herramienta) |
| Z | G2 / Capterra / SoftwareSuggest sobre LitExtension y Cart2Cart | https://www.g2.com/products/litextension/pricing | S (agregadores) | 1 | 1 | 1 | 1 | G2: precios actualizados 2025-03-20 | [S] |

### 2.2 Importadores oficiales

Shopify.
- App «Store Migration» (de Shopify, gratis, lanzada el 17 de julio de 2024): plataformas «Square, WooCommerce, Etsy, Wix, Amazon, eBay, Clover, and Lightspeed R/X (Vend)»; importa datos de producto y de cliente; por CSV para cualquier plataforma, y conexión automática en las compatibles. Limitaciones del listado: algunas plataformas no exportan todo; reseñas de usuarios dicen que puede no traer fotos de producto y que los errores en CSV de clientes son vagos. Valoración: 3,1 de 5 con 77 reseñas (23 de cinco estrellas, 21 de una). Los pedidos no figuran en el extracto leído; un resumen del buscador menciona «last 60 days» de pedidos, sin confirmar. https://apps.shopify.com/store-migration
- Nota sobre nombre: la app que antes se llamaba «Store Importer» no se verificó en esta ronda; hoy lo oficial leído es «Store Migration». Hueco de verificación.
- CSV nativo: ver 1.2 (límites de 3 opciones, 250 imágenes, UTF-8; las imágenes se bajan desde URL pública). https://help.shopify.com/en/manual/products/import-export/using-csv
- Matrixify (app de terceros, ampliamente usada, no es oficial de Shopify): planes por 30 días, Demo gratis (10 registros por tipo), Basic $20, Big $50, Enterprise $200. Límites por trabajo de importación, Basic / Big: productos 5.000 / 50.000, clientes 2.000 / 20.000, pedidos 1.000 / 10.000, redirecciones 10.000 / 100.000, páginas 50 / 500, entradas de blog 50 / 500, descuentos 300 / 3.000. Hasta 2.048 variantes por producto. Puede leer archivos desde FTP/SFTP, Google Drive, Google Sheets, Dropbox o enlaces. «Batch Import» solo en Enterprise. https://matrixify.app/pricing/
- La guía oficial de migración de Shopify no menciona a Matrixify (verificado en la página). https://help.shopify.com/en/manual/migrating-to-shopify

Tiendanube.
- Hacia Tiendanube hay tres vías oficiales: planilla CSV (Productos > Exportar e importar), app propia «Mercadoshops a Tiendanube» (que según el blog funciona también desde Mercado Libre) y app «Shopify a Tiendanube» (importa productos, colecciones y clientes). La carga masiva por CSV no borra productos. https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-el-catalogo-de-productos-de-mercado-shops-a-tiendanube ; https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube
- Para clientes y pedidos desde Mercado Shops la vía oficial es instalar Perfit / Marketing Nube en la cuenta de Mercado Shops, que sincroniza clientes y órdenes; las órdenes quedan solo en esa app. https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-mi-tienda-online-de-mercado-shops-a-tiendanube
- Servicios asistidos: «Tiendanube Evolución» ofrece migración asistida; la página no declara precio ni condiciones. https://www.tiendanube.com/mx/evolucion/seo
- Apps de terceros en la tienda de apps de Tiendanube: Automágico (migración por API desde WooCommerce y otras plataformas, resto por planilla), LitExtension, Migrashop. Solo vistas en listados del buscador; no se abrieron. https://www.tiendanube.com/tienda-aplicaciones-nube/litextension-store-migration [S]
- La reseña de un usuario citada en un resumen dice que una app no migró todo pese a pagar la suscripción; sin URL propia verificable, no se usa.

WooCommerce.
- Importador CSV nativo de productos: agrega y actualiza por ID o SKU (en WooCommerce 11.2 y posteriores, también por GTIN/UPC/EAN/ISBN); crea variaciones (11.1 y posteriores) con SKU único por variación; las imágenes se descargan desde URL externa si el host lo permite; «The core importer cannot add or update image alt text»; los límites dependen de memoria y de subida del servidor; recomienda lotes y pruebas en staging. La página solo trata productos; no dice nada de clientes ni pedidos. https://woocommerce.com/document/product-csv-importer-exporter/
- Hacia WooCommerce desde Shopify existen herramientas oficiales de la tienda de extensiones (Shopify Data Migrator: productos, categorías, clientes, pedidos, cupones, blogs, páginas y reseñas; reseñas solo con CSV; sin contraseñas; no se encontró precio en la página). https://woocommerce.com/document/shopify-data-migrator

### 2.3 Servicios de terceros

| Herramienta | Qué migra | Cómo cobra | Precio de entrada | Fuente | Lectura |
|---|---|---|---|---|---|
| Cart2Cart | productos, categorías y etiquetas, clientes, pedidos, URL y metadatos SEO, impuestos y cupones (según plataforma); reseñas, páginas, blog, contraseñas y lealtad / tarjetas de regalo como adicional o no incluidos | pago único por proyecto según cantidad de entidades y plataformas de origen y destino; sin suscripción | «From $69 and up»; ejemplo WooCommerce a Shopify: productos $99, clientes $79, pedidos $99, adicionales $59 + $49, total $286; adicional de 301 $59 | https://ecommerce-platforms.com/ecommerce-resources/cart2cart-review (act. 2025-07-22) | [L] reseña; precio propio sin leer |
| LitExtension, Automated Migration | productos, clientes, pedidos y otras entidades (según el destino) | por proyecto, según el total de entidades; hasta 6 opciones adicionales gratis; «Customer Password Migration» y «SEO URL Migration, or 301 Redirect» como «paid add-ons» | «starts from $19» por proyecto; gratis para tiendas con menos de 100 productos, 100 clientes y 100 pedidos | https://litextension.com/pricing.html | [L] |
| LitExtension, All-in-One (gestionado por expertos) | lo mismo, con ayuda | por entidades y complejidad; todas las opciones adicionales gratis | «starting from $129 per project» | https://litextension.com/pricing.html | [L] |
| Tiendanube Evolución | migración asistida (URL, 301, blog, metadatos) | no declarado | no declarado | https://www.tiendanube.com/mx/evolucion/seo | [L] |

Discrepancias a mostrar, no a resolver.
- Contraseñas en Cart2Cart: la reseña dice que no se migran y que se manda un mail de restablecimiento, y a la vez lista «password migration» como adicional «if supported». https://ecommerce-platforms.com/ecommerce-resources/cart2cart-review
- Precio de entrada de LitExtension: la página oficial dice «from $19»; G2 dice paquete automático desde $49 y premium desde $129; SoftwareSuggest «$19 per 100 entities»; Capterra Canadá «$29 for 100 products, customers and orders» (agregadores, sin abrir). Prima la página oficial. https://www.g2.com/products/litextension/pricing [S]
- Cart2Cart $69: la reseña dice «From $69»; no se pudo confirmar contra su página de precios.
- Presencia en LatAm: LitExtension aparece como app en la tienda de Tiendanube (listado del buscador); no se verificó para Cart2Cart ni la compatibilidad con Tiendanube como origen o destino. Hueco.

### 2.4 A dónde se mudaron los vendedores de Mercado Shops, y con qué

- Tiendanube publicó una app dedicada («Mercadoshops a Tiendanube»), guía en su centro de ayuda y blog (ver arriba). No se encontró un dato de cuántos se mudaron ni a qué plataforma fuera de Tiendanube (la fuente es del actor interesado). https://www.tiendanube.com/blog/como-migrar-de-mercado-shops-a-tiendanube/
- «Mi Página» (el destino que propone Mercado Libre) ya está cubierto en la base y no se repite.

### 2.5 Recurso canónico del componente

Propuesta: la guía oficial de la plataforma de destino, más la ficha de precios de la herramienta elegida.
- Para destino Shopify: https://help.shopify.com/en/manual/migrating-to-shopify (los 5 métodos y los 11 pasos) y https://help.shopify.com/en/manual/products/import-export/using-csv (límites de CSV). En qué fijarse: orden productos, clientes, pedidos; tarjetas de regalo no se crean por CSV; la app gratuita Store Migration tiene 3,1 de 5.
- Para destino Tiendanube: https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube . En qué fijarse: qué NO migra (pedidos, envíos, pagos) y el hecho de que descuentos y reseñas pasan por soporte.
- Para costear un trabajo con terceros: https://litextension.com/pricing.html (precio oficial y adicionales de 301 y contraseñas) y, mientras no se lea la página de Cart2Cart, la reseña https://ecommerce-platforms.com/ecommerce-resources/cart2cart-review marcada como secundaria.
- Fechar la ficha: los precios y planes de Matrixify, LitExtension y Cart2Cart cambian; anotar «consultado 2026-11-24» y revisar cada 6 meses.

---

## Huecos

- Suscripciones, tokens de pago (tarjetas guardadas) y qué pasa con las tarjetas de regalo hacia Tiendanube: no hallé fuente primaria. Solo consta lo de Shopify (tarjetas de regalo no se crean por CSV).
- Contraseñas: sin fuente oficial para WooCommerce a Shopify ni hacia Tiendanube; la evidencia leída es Shopify a WooCommerce.
- Páginas y blog hacia Tiendanube: la guía oficial desde Shopify no los menciona; solo el servicio asistido (Evolución) dice que migra el blog.
- Redirecciones 301 hacia Tiendanube: la ayuda de 301 se leyó solo vía buscador [S]; falta abrirla y ver si admite importación masiva y qué límite tiene.
- Límites del CSV de Tiendanube (excepto el tope de 20.000 líneas, citado en la guía de Mercado Shops) y de la app Shopify a Tiendanube: no leídos.
- Shopify «Store Importer» con ese nombre: no verificado si sigue vigente o fue reemplazada por «Store Migration». La página de redirecciones de Shopify se leyó solo por buscador.
- Página de precios propia de Cart2Cart: no cargó; solo reseña secundaria. Precio de LitExtension a Tiendanube específicamente: no hallado.
- Aleyda Solís (403) y el caso de Search Engine Land (403): no se pudieron leer; no se citan afirmaciones de su contenido. Glenn Gabe, Moz y Sistrix: no se encontraron estudios de replatforming suyos en las tres rondas.
- Dato de recuperación para replatforming pyme con el mismo dominio: no existe en lo hallado; SALT es solo de dominios. Hay un resumen de podcast que cita un «estudio de SEJ de enero 2025» con 523 días y 17% de fracaso; no se pudo verificar y no se usa.
- Casos documentados de fracaso para pymes argentinas o de Mercado Shops a Tiendanube: ninguno hallado.
- Sistemas de gestión (ERP / stock) e integración con Mercado Libre tras la mudanza: solo se nombran Astroselling, Ecomnube y Anymarket en la guía de Tiendanube; sin análisis de qué se rompe.
- DNS y dominios `.ar` (NIC Argentina, tiempos de propagación): no buscado en el presupuesto de rondas.
- «Congelar cambios» y el orden inventario, prueba, congelar, corte, verificación: no figura en ninguna fuente leída; queda como práctica propia sin cita.
- Hacia Tiendanube, la afirmación de que no se migran envíos y medios de pago es de la guía oficial; no se verificó con un caso real.
