# Motor para vidrieras a medida: de qué se quejan, con reseñas leídas una por una

Fecha de consulta: 2026-11-22. Zona: el motor de comercio que usan agencias y marcas para armar su propia vitrina (headless, composable o de código abierto). Ángulo: quejas de quienes usan o construyen con VTEX (FastStore e IO), commercetools, Medusa, Saleor, Vendure, Shopify headless (Hydrogen, Oxygen y Storefront API), Adobe Commerce o Magento headless, la Storefront API de Tiendanube y WooCommerce headless. No se recomienda nada. La tabla codificada, para recontar, está en `vidrieras-resenas.json` (255 filas, una por opinión o issue).

## Respuesta primero

1. **La queja que más se repite es el costo total y no la licencia.** En las 204 opiniones codificadas (sin contar los issues de GitHub), el costo aparece 52 veces y la complejidad o el tiempo de implementación 46. Casi siempre viene junto con otras dos: hace falta un equipo de desarrollo permanente (talento, 26) y la vitrina hay que mantenerla para siempre (mantenimiento, 25). La frase tipo: *"the total cost of ownership ends up way higher than anyone budgeted for … you basically need a small agency just to maintain the frontend and integrations"* (r/ecommerce, 7 de abril de 2026, sobre commercetools). Dato C/3: muchas opiniones y de varias fuentes, pero casi todas de Reddit, donde el contexto es el de cada hilo.
2. **El checkout es el punto donde se rompe.** En los motores abiertos, 22 de los 51 issues de GitHub leídos son de pagos y checkout (Stripe que cobra dos veces, PaymentIntent que se recrea con cada cambio, sobreventa con dos compras al mismo tiempo) y 12 de envíos e impuestos. En las opiniones, quien hizo WooCommerce o commercetools headless dice que rearmar el checkout es "una trampa" o que "solo el checkout" lleva de 8 a 10 semanas. Dato C/3. Ojo: los issues se buscaron por esas palabras, así que la proporción de pagos dentro de GitHub la armó la búsqueda y no se puede leer como frecuencia.
3. **Cada motor tiene su queja propia.** En commercetools pesa el costo (23 de 56 filas). En VTEX, la calidad técnica y la carrera de quien la programa: "nichado", "datado", documentación "básico do básico" (20 de sus 27 filas vienen de foros de Brasil, Argentina y Chile). En Medusa, Saleor y Vendure lo que falta (marketplace, permisos, facturas en lote, OMS) y si el proyecto va a durar (cambios de licencia, deprecaciones). En Shopify headless, que el negocio pierde la edición y la medición: píxeles que no disparan y marketing que no puede cambiar nada (7 de 17 opiniones). En Magento headless, que PWA Studio "está muerto" y que hay proyectos "migrando de vuelta" al Magento común. Dato C/3.
4. **De Argentina y Latinoamérica hay poco, y casi nada de la vitrina a medida.** De las 29 filas con contexto latinoamericano, 20 son de VTEX (sobre todo desarrolladores en r/brdev y r/devsarg). Las 5 de Tiendanube son de desarrolladores argentinos que se quejan de los límites de los temas y del plan, no de la Storefront API: sobre esa API no apareció ninguna queja pública. Lo local aparece de costado: un issue de Saleor de 2018 que rechaza códigos postales argentinos y no acepta la Ciudad de Buenos Aires en el campo provincia, una tienda con Medusa y el SDK de Mercado Pago que no puede reembolsar por un problema de decimales (2025), y un desarrollador argentino al que un correo no le abre su API. Dato D/4.
5. **Las fuentes de reseñas formales estaban cerradas.** G2, Capterra (también la de Brasil y la de México), GetApp, Software Advice, TrustRadius, Gartner Peer Insights, Trustpilot y SourceForge devolvieron 403 o bloqueo de Cloudflare, tanto con lectura directa como con navegador. PeerSpot sí abrió: 10 reseñas de commercetools (todas del 16 al 24 de junio de 2026, lo que parece una campaña de reseñas pedidas) y 10 de Adobe Commerce. Las "unas 35 de VTEX en G2" del barrido liviano no se pudieron releer.

## Método

- **Reddit:** el sitio bloquea la lectura automatizada (403 directo y con navegador), así que usé el archivo público pullpush.io (API de búsqueda de comentarios; trae hasta el 9 de octubre de 2026). Por motor, bajé los últimos 100 a 300 comentarios que lo nombran, filtré por subforos de comercio, desarrollo y emprendimiento (se fueron los de juegos, bolsa y el resto) y por largo mínimo, y **leí uno por uno** el fragmento alrededor de la mención. Codifiqué solo los que dicen algo del motor como producto: se descartaron las listas sin opinión, los avisos de trabajo, las charlas sobre VTEX como empleador (sueldos, oficina) y los elogios. En Magento leí los 120 más recientes de 215 (los otros 95 no los leí). El cupo de pullpush se agotó varias veces (error 429): los subforos r/headlesscommerce, r/shopify y r/Magento no se pudieron filtrar por subforo y se cubrieron con búsquedas por término.
- **GitHub:** con `gh api`, en medusajs/medusa, saleor/saleor, vendurehq/vendure, Shopify/hydrogen y vtex/faststore busqué issues con payment, checkout, tax, shipping, migration y performance en el título, ordenados por reacciones (6 por palabra y repo), y en Hydrogen además headless, storefront api, checkout y performance. Leí los 150 títulos y abrí el cuerpo de unos 15. Codifiqué 51: los que describen un problema que afecta a una tienda. Se descartaron las tareas internas, las propuestas sin dolor detrás y los PR. Busqué también mercadopago, "mercado pago", afip, argentina, brazil, pix, boleto, installments, cuotas y parcelas en esos repos.
- **Hacker News:** API de Algolia, 30 comentarios por término (commercetools, medusajs, saleor, vendure, "shopify hydrogen", vtex, "headless commerce"). Leí 131 fragmentos; casi todos son avisos de trabajo o anuncios y codifiqué 8.
- **PeerSpot:** las páginas de reseñas de commercetools y Adobe Commerce (VTEX no está). Leí las 20 secciones "What needs improvement?". Hablan del producto entero, no solo del modo headless.
- **Foros oficiales:** comunidad de VTEX (Discourse, búsqueda JSON con faststore, headless, checkout y performance: unos 30 posts leídos, 4 codificados) y community.shopify.dev (4 posts, ninguno codificado). La comunidad vieja de Shopify devuelve 410.
- **Búsqueda web:** 2 búsquedas para agencias argentinas y para quejas de la Storefront API de Tiendanube. No trajeron opiniones, solo documentación oficial.
- **Codificación:** a mano, con 14 temas. Una fila puede tener varios temas y nombrar varios motores (por ejemplo, "Saleor o Medusa"). La polaridad es **negativa** si la opinión es una queja o un rechazo y **mixta** si reconoce algo bueno y pone un límite o una condición ("sirve si tenés equipo"). Los elogios se leyeron pero no se codificaron. Las citas van sin autor. En Reddit la cita sale del texto original por coincidencia literal (el script corta si no la encuentra).

## Cuántas se leyeron

| Fuente | Leídas | Codificadas | Calificación |
|---|---|---|---|
| Reddit (archivo pullpush) | 967 comentarios únicos | 173 | D/4 [L] |
| GitHub issues | 150 títulos, unos 15 cuerpos | 51 | B/3 [L] |
| PeerSpot | 20 secciones de mejora | 19 | C/3 [L] |
| Hacker News | 131 fragmentos | 8 | D/5 [L] |
| Comunidad VTEX | unos 30 posts | 4 | C/4 [L] |
| community.shopify.dev | 4 posts | 0 | C/4 [L] |
| G2, Capterra, GetApp, Software Advice, TrustRadius, Gartner, Trustpilot, SourceForge | 0 (bloqueados) | 0 | sin dato |

Leídas en Reddit por motor (antes de codificar): VTEX 121 (95 de la búsqueda "vtex" y 29 de "vtex io", con 3 repetidas), commercetools 218, Saleor 140, Vendure 109, Medusa 102, Shopify headless 107, Magento headless 120 de 215, WooCommerce headless 60 y Tiendanube o Nuvemshop 81.

Filas codificadas por motor (una fila con dos motores cuenta para los dos):

| Motor | Opiniones neg. | Opiniones mixtas | Issues GitHub | Total |
|---|---|---|---|---|
| commercetools | 16 | 40 | 0 | 56 |
| Medusa | 12 | 21 | 16 | 49 |
| Vendure | 11 | 12 | 12 | 35 |
| Saleor | 9 | 10 | 10 | 29 |
| Shopify headless | 5 | 12 | 12 | 29 |
| VTEX | 18 | 8 | 1 | 27 |
| Adobe Commerce / Magento headless | 11 | 14 | 0 | 25 |
| WooCommerce headless | 8 | 11 | 0 | 19 |
| Tiendanube | 4 | 1 | 0 | 5 |

Por fecha: 147 filas son de 2026, 58 de 2025, 21 de 2024 y 29 de 2023 o antes (marcadas como viejas en la tabla).

## Temas

### Opiniones (204 filas: Reddit, PeerSpot, HN y comunidad VTEX)

| Tema | Total | Neg. | Mixtas | Motores donde más aparece |
|---|---|---|---|---|
| Costo total, precio y licencia | 52 | 23 | 29 | commercetools 23, VTEX 9, Adobe/Magento 8, Saleor 5 |
| Complejidad, curva y tiempo de implementación | 46 | 18 | 28 | commercetools 16, Medusa 8, Adobe/Magento 7, Woo 6, Vendure 6 |
| Funciones que faltan o ecosistema chico | 38 | 17 | 21 | commercetools 9, Medusa 7, Saleor 6, Vendure 6 |
| Talento (hace falta equipo; carrera de quien programa) | 26 | 8 | 18 | commercetools 10, VTEX 5, Medusa 5 |
| Mantenimiento permanente | 25 | 11 | 14 | commercetools 10, Medusa 6, Woo 4, Shopify 4 |
| Rendimiento, estabilidad y calidad técnica | 19 | 11 | 8 | VTEX 7, commercetools 3, Adobe/Magento 3 |
| Pagos y checkout | 19 | 8 | 11 | Woo 6, commercetools 5, Medusa 3 |
| Dependencia del proveedor o de la agencia, abandono, licencia | 19 | 8 | 11 | Medusa 6, Adobe/Magento 5, Vendure 3 |
| Edición por el negocio y medición (editor, vista previa, píxeles) | 17 | 6 | 11 | Shopify 7 |
| Soporte y documentación | 9 | 5 | 4 | commercetools 5, VTEX 2, Vendure 2 |
| Migración y actualizaciones | 9 | 4 | 5 | Adobe/Magento 5 |
| Queja general sin motivo | 6 | 4 | 2 | Medusa 3 |
| Envíos e impuestos | 4 | 3 | 1 | Woo 2 |
| Lo local (medios de pago, direcciones, correos del país) | 3 | 1 | 2 | — |

### Issues de GitHub (51 filas, motores abiertos y Hydrogen)

| Tema | Total | Motores |
|---|---|---|
| Pagos y checkout | 22 | Medusa 9, Saleor 4, Vendure 4, Hydrogen 4, FastStore 1 |
| Migración y actualizaciones (algo se rompe al actualizar) | 14 | Medusa 5, Hydrogen 5, Vendure 3, Saleor 1 |
| Envíos e impuestos | 12 | Medusa 4, Saleor 4, Vendure 4 |
| Rendimiento | 10 | Medusa 3, Saleor 3, Vendure 3, Hydrogen 1 |
| Lo local | 6 | Saleor 4, Medusa 1, Vendure 1 |
| Medición (eventos de analítica) | 3 | Hydrogen 3 |

Los issues se buscaron por esas palabras: sirven para ver **qué tipo** de problema aparece en cada tema, no cuánto pesa cada tema.

## Citas por tema (sin autor; la tabla JSON tiene la URL de cada una)

**Costo total**
- commercetools, r/ecommerce, 20 de abril de 2026: "The maintenance cost far outweighs the customization you end up being able to get. Most people who are composable regret it after a couple years."
- VTEX, r/empreendedorismo, 9 de septiembre de 2025: "os planos deles são por volta de R$5000/mês (preço oferecido por eles quando eu consultei) e isso, para o porte do negócio que temos, é muito alto".
- Saleor y Medusa, r/ecommerce, 22 de julio de 2026: "moving to Saleor or Medusa to save $250 a month is almost certainly trading a software bill for an engineering bill."

**Complejidad y tiempo**
- commercetools, r/nextjs, 9 de mayo de 2026: "We use Commercetools at my work. It’s a beast. Unless you have very custom needs I wouldn't recommend it."
- commercetools, r/nextjs, 8 de mayo de 2026: "the 6 month implementation timeline is real, and in my experience the complexity never really goes away after launch either."
- Medusa, r/devsarg, 14 de agosto de 2026: "La curva inicial no es trivial porque tenes que entender el concepto de modulos, workflows y el sistema de eventos. No es como WooCommerce que instalas y listo."

**Talento y mantenimiento**
- commercetools y similares, r/shopify, 7 de abril de 2026: "the hidden cost is talent. You need a strong, permanent dev team (either in-house or agency) who understand the architecture."
- Shopify headless, r/nextjs, 1 de octubre de 2026: "headless Shopify is less a framework choice and more a 'congrats you now own every piece of the plumbing' situation."
- WooCommerce headless, r/Wordpress, 4 de agosto de 2026 (escribe alguien que vende un producto propio): "We’ve built around 10 headless woo stores … Have now moved most of those projects back to native wp/woo."

**Pagos y checkout**
- WooCommerce headless, r/woocommerce, 30 de junio de 2026: "Rebuilding the checkout layer from scratch is almost always a trap because you instantly inherit the responsibility of maintaining complex tax, shipping, and payment gateway logic".
- commercetools, r/ExperiencedDevs, 9 de abril de 2026: "when we actually scoped the integration work for checkout alone it was going to eat 8-10 weeks because you're basically building a checkout service from their primitives."
- Medusa, GitHub #15589, 3 de junio de 2026: "Each cart total change during checkout creates a new Stripe PaymentIntent".

**Funciones que faltan**
- Medusa, r/PHP, 27 de abril de 2026: "there were basic functionalities (like batch print invoices) missing and needed my developer to hardcoded."
- Vendure, r/ecommerce, 9 de junio de 2026: "I have to write a lot of code as the OSS had very limited features."
- Saleor, r/django, 25 de marzo de 2026: "Sadly it was too hard to modify to be a marketplace BUT from a single store viewpoint it seemed pretty good."

**Rendimiento y calidad técnica**
- VTEX, r/chile, 23 de mayo de 2026: "vtex? esa se cae solo pegándole a unos GET desde un resultado de búsqueda."
- VTEX, r/brdev, 15 de septiembre de 2026: "Vtex é um buraco. É extremamente nichado, tecnologia de lá é bem datada e CHEIO de gambiarra."
- commercetools, Hacker News, 12 de diciembre de 2022: "the requests take more than 3 seconds in some cases".

**Dependencia, abandono y licencia**
- Magento, r/Magento, 24 de diciembre de 2025: "PWA Studio is dead. Adobe stopped investing. Too complex, low adoption."
- Vendure, r/PaymentProcessing, 29 de junio de 2026: "moving the core from MIT to GPLv3 was a strategic mistake because it adds adoption friction and weakens ecosystem trust."
- Hydrogen, GitHub #3321, 26 de noviembre de 2025: "Has Shopify abandoned Hydrogen?" (después, el 14 de octubre de 2026, Shopify anunció una Hydrogen reconstruida en community.shopify.dev).

**Edición por el negocio y medición**
- Shopify headless, r/shopifyDev, 20 de septiembre de 2026: "if the marketing team can’t add their tracking pixels and the content team can’t make basic updates then it’s not going to work".
- Shopify headless, r/ShopifyeCommerce, 28 de agosto de 2026: "Having the pixel fire right is the biggest headache with headless shopify".
- Magento headless, r/Magento, 25 de septiembre de 2025 (lo escribe quien maneja el comercio electrónico de una empresa): "it's so complex and time consuming to manage as a marketeer. It's also extra complex and expensive to integrate features or plugins."

**Soporte y documentación**
- VTEX, r/brdev, 10 de noviembre de 2023: "a documentação da vtex é básico do básico, então vão bater a cabeça quando quiserem fazer algo mais bolado".
- Vendure, r/programming, 10 de agosto de 2025: "I wasn't quite convinced about documentation and due to lack of NextJS starter."
- commercetools, PeerSpot, 21 de junio de 2026: "They have payments, but you have to integrate third-party systems or there are certain limitations to it." (la misma reseña pide tutoriales en video).

**Migración y actualizaciones**
- Magento headless, r/Magento, 18 de marzo de 2026: "More magento headless builds migrating back to vanilla magento for sure, for flexibility reasons".
- Medusa, GitHub #13891, 29 de octubre de 2025: "Checkout page not loading due to shipping options error after updating to 2.11.1".

## Lo que aparece de Argentina y Latinoamérica

- **VTEX (20 filas).** Casi todo es de desarrolladores en r/brdev, r/devsarg y r/chile. Se repiten tres cosas: el costo para un comercio mediano (R$ 5.000 por mes cotizados, "o preço acompanha o porte"), la calidad técnica ("se cae solo pegándole a unos GET", "carrinho bugado no Carrefour") y la carrera de quien programa ("no aprendías nada", "nichado", "termine perdiendo un año como dev"). Un comentario en r/devsarg (septiembre de 2025) cuenta que en un retail argentino grande la carga de productos, precios y stock "nada era automático". Ninguna de estas filas viene de una agencia que se presente como tal.
- **Tiendanube (5 filas, todas de r/devsarg en 2026).** Son quejas de personalización sobre temas y planes, no sobre la Storefront API: "estás al horno con los plancitos normales" (20 de abril), "para poder hacer cosas boludas tenés que subir de plan" (3 de abril), "editor horrible de código que a veces ni funciona" (13 de mayo). Sobre la Storefront API no encontré quejas públicas, ni en foros ni con búsqueda web. La página oficial confirma que el pago pasa por el checkout de Tiendanube y que la API se activa a mano por tienda [A/1]. Eso no es una queja, es lo que la plataforma declara.
- **Lo local en los motores abiertos.** Saleor #1646 y #1647 (2018): el checkout pide una provincia que la Ciudad de Buenos Aires no tiene y rechaza códigos postales argentinos válidos. Medusa #13091 (2025): una tienda cuyo package.json incluye el SDK de Mercado Pago no puede reembolsar por una diferencia de decimales. No hay ningún issue con "mercadopago", "cuotas" o "afip" en el título en los cuatro repos. Lo que aparece con esas palabras es código de usuarios, no pedidos.
- **Promoción disfrazada.** En r/ecommercebr y r/empreendedorismo hay varios comentarios de 2026 que empujan Nuvemshop Next contra VTEX y Shopify Plus con el mismo argumento y el mismo vocabulario ("Redução de custos (TCO)", "API bem mais liberada"). No los codifiqué como opinión, salvo uno que marqué como posible promoción.
- **Agencias argentinas:** no apareció ninguna queja pública de una agencia argentina sobre un motor headless (hueco).

## Sesgos de cada fuente

- **Reddit:** quien escribe es casi siempre desarrollador, agencia o consultor, rara vez el dueño de la marca. En 2026 hay mucha promoción encubierta: en r/bigcommerce y r/ecommerce los propios usuarios denuncian una red de cuentas que inventa historias a favor de SCAYLE y en contra de sus rivales, y empleados de commercetools, Medusa, Vendure, Saleor, Elastic Path y Uniform responden en los hilos. Marqué en la columna `nota` las filas con señales de eso (3 de commercetools con SCAYLE, varias de vendedores) y no codifiqué las respuestas de empleados que solo defienden su producto. Además, buena parte de las quejas sobre commercetools son consejos generales ("si no tenés equipo, no") y no experiencia propia, y por eso tiene tantas mixtas.
- **GitHub:** quien abre un issue es desarrollador y ya eligió el motor. Un issue mide qué se rompe, no cuánto molesta. La búsqueda por palabra clave infla los temas buscados.
- **PeerSpot:** las 10 reseñas de commercetools son de una sola semana de junio de 2026 y la mayoría las escriben socios implementadores (tercerizadoras y consultoras), lo que sugiere reseñas pedidas. Las de Adobe hablan del producto entero.
- **Hacker News:** pocas opiniones, viejas (2015 a 2025) y de perfil técnico.
- **G2 y Capterra** (no leídos): por lo que dice el barrido liviano, quien reseña ahí suele ser cliente grande o socio. Ese sesgo no se pudo medir esta vez.

## Huecos

1. **Las reseñas formales (G2, Capterra, TrustRadius, Gartner) no se pudieron leer:** todas bloquean la lectura automatizada. Para VTEX no hay ninguna reseña formal leída en esta tanda.
2. **La Storefront API de Tiendanube no tiene quejas públicas:** ni a favor ni en contra. Puede ser que se use poco o que la discusión pase en canales privados de socios.
3. **Agencias argentinas y latinoamericanas:** no se encontraron publicaciones públicas (LinkedIn, Medium, blogs) con quejas concretas. LinkedIn no se leyó: pide iniciar sesión.
4. **Magento:** quedaron 95 comentarios sin leer (de 215).
5. **Subforos puntuales:** r/headlesscommerce, r/shopify (filtrado por subforo) y r/Magento (idem) no se pudieron bajar por el límite de pullpush; se cubrieron en parte con búsquedas por término.
6. **Precisión de la codificación:** la hizo una sola persona y no se midió el acuerdo con otra. La separación entre negativa y mixta es lo más discutible.
7. **El que paga no habla:** casi no hay opiniones del dueño o del gerente de comercio electrónico de la marca (hay 2 o 3). Lo que se ve es la mirada de quien construye.

## Fuentes

Todas consultadas el 2026-11-22.

- Archivo de Reddit, pullpush.io: `https://api.pullpush.io/reddit/search/comment/?q=<término>` (términos: vtex, "vtex io", commercetools, saleor, vendure, medusajs, "hydrogen oxygen", "shopify headless", "magento headless", "magento graphql", "headless woocommerce", "woocommerce headless", tiendanube, "nuvemshop api"). La URL de cada comentario está en el JSON. [D/4] [L]
- GitHub, búsqueda de issues en medusajs/medusa, saleor/saleor, vendurehq/vendure, Shopify/hydrogen y vtex/faststore, por ejemplo https://github.com/medusajs/medusa/issues/15589, https://github.com/saleor/saleor/issues/1647, https://github.com/vendurehq/vendure/issues/3508, https://github.com/Shopify/hydrogen/issues/3321. [B/3] [L]
- PeerSpot, commercetools: https://www.peerspot.com/products/commercetools-reviews ; Adobe Commerce: https://www.peerspot.com/products/adobe-commerce-reviews [C/3] [L]
- Hacker News, API de Algolia: https://hn.algolia.com/api/v1/search?query=<término>&tags=comment ; comentarios citados: https://news.ycombinator.com/item?id=33958129 , https://news.ycombinator.com/item?id=39073302 , https://news.ycombinator.com/item?id=42355339 , https://news.ycombinator.com/item?id=35339936 [D/5] [L]
- Comunidad VTEX: https://community.vtex.com/t/add-products-to-orderform-with-prices-from-other-pricetable/43329 , https://community.vtex.com/t/lista-de-desejos-para-faststore/43926 , https://community.vtex.com/t/pre-visualizacao-faststore-nao-funciona/43542 , https://community.vtex.com/t/produtos-associados-compre-junto/40673 , https://community.vtex.com/t/duvidas-frequentes-tenho-um-front-headless-como-faco-para-integrar-e-usar-o-checkout-e-o-my-account-nativos-da-vtex-corretamente/40280 [C/4] [L]
- Shopify, comunidad de desarrolladores, Hydrogen 2026-10: https://community.shopify.dev/t/hydrogen-2026-10-now-available/38602 [A/2] [S] (leído el resumen del buscador del foro)
- Tiendanube, ¿Qué es la Storefront API?: https://ayuda.tiendanube.com/es_AR/socios-tecnologicos/que-es-la-storefront-api-de-tiendanube-y-para-que-sirve [A/1] [S] (según resumen del buscador; leída en el barrido liviano)
- Bloqueadas (403 o Cloudflare): https://www.g2.com/products/vtex-commerce-platform/reviews , https://www.g2.com/products/commercetools/reviews , https://www.capterra.com/p/159471/VTEX/reviews/ , https://www.trustradius.com/products/vtex/reviews , https://www.gartner.com/reviews/market/digital-commerce/vendor/vtex , https://www.getapp.com/retail-consumer-services-software/a/vtex/reviews/ , https://www.softwareadvice.com/ecommerce/vtex-profile/reviews/ , https://www.trustpilot.com/review/vtex.com , https://sourceforge.net/software/product/VTEX/ , https://www.reddit.com (lectura directa).
