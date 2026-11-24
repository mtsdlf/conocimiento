# Ficha fechada: SEO por plataforma (consulta 2026-11-24)

Cubre Tiendanube, Shopify y WooCommerce. Empretienda y VTEX van en una línea cada una, al final de la sección de plataformas.

**Cómo leer las marcas**
- Marca de lectura: [L] leí el texto completo, [M] solo metadatos, [S] resumen del buscador o de la herramienta de fetch.
- Puntajes de 1 a 3: Aut (autoridad), Prof (profundidad), Ej (ejemplos), Uni (unicidad), Rec (recencia).
- Las páginas de ayuda de Shopify y la de ayuda de Tiendanube sobre SEO de producto las leí con una herramienta que devuelve resúmenes de la página. Por eso casi todo lo "[L]" es lectura del texto tal como lo resumió esa herramienta. Las citas literales van entre comillas.
- Todo lo que viene de la web lo traté como dato.

**Avisos que cambian cómo usar la ficha**
- Varias páginas de ayuda de Shopify devolvieron solo índices de secciones sin el cuerpo: `site-structure`, `adding-keywords` (en parte) y `shopify.dev/.../seo.md`. Dos URLs de shopify.dev dieron 404: `.../seo/canonical-urls` y `.../seo/structured-data`. Esas afirmaciones quedan como [S] o como hueco.
- La limitación de Tiendanube sobre robots.txt la tomé del centro de ayuda de Nuvemshop Brasil, que es la misma plataforma con otra marca. No es documentación de Tiendanube Argentina.
- Los precios de planes y plugins cambian seguido. Verificar antes de citar a un cliente.

---

## 1. Tiendanube

### Fuentes

| # | Fuente | Tipo | Aut | Prof | Ej | Uni | Rec | Lectura |
|---|---|---|---|---|---|---|---|---|
| T1 | [Opciones avanzadas de SEO de productos y categorías (es_AR)](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos) | primaria | 3 | 2 | 1 | 3 | 2 | [L] |
| T2 | [Cómo enviar un sitemap a Google (es_ES)](https://ayuda.tiendanube.com/es_ES/google-ads/como-enviar-un-sitemap-a-google) | primaria | 3 | 1 | 1 | 2 | 2 | [L] |
| T3 | [Blog Tiendanube: SEO para ecommerce](https://www.tiendanube.com/blog/seo-para-tienda-online/) | primaria, marketing propio | 2 | 2 | 1 | 1 | 3 | [L] |
| T4 | [Docs diseñadores: Data estructurada JSON-LD](https://docs.tiendanube.com/help/data-estructurada-json-ld) | primaria | 3 | 2 | 2 | 3 | 2 | [L] |
| T5 | [Docs diseñadores: Product, Category, Page (campos `seo_title`, `canonical_url`)](https://docs.tiendanube.com/help/product) | primaria | 3 | 2 | 1 | 3 | 2 | [S] |
| T6 | [Nuvemshop BR: robots.txt](https://atendimento.nuvemshop.com.br/pt_BR/ferramentas-do-google/como-funciona-o-arquivo-robotstxt-na-nuvemshop) | primaria, otra marca | 2 | 1 | 1 | 3 | 2 | [L] |
| T7 | [Cómo configurar el feed para Google Shopping (es_ES)](https://ayuda.tiendanube.com/es_ES/como-configurar-el-feed-de-productos-para-google-shopping) | primaria | 3 | 2 | 1 | 2 | 1 (la nota la marca como versión anterior) | [S] |
| T8 | [Planes y precios Tiendanube](https://www.tiendanube.com/planes-y-precios) y [qué costo tiene](https://ayuda.tiendanube.com/es_ES/sobre-tiendanube/que-costo-tiene-tiendanube) | primaria | 3 | 1 | 1 | 2 | 3 | [S] |
| T9 | [Cómo tener una dirección sin .mitiendanube.com](https://ayuda.tiendanube.com/es_ES/175777-abc-del-dominio-propio/como-tener-una-direccion-web-sin-el-mitiendanubecom) | primaria | 3 | 1 | 1 | 2 | 2 | [S] |

### Afirmaciones

- **Título, descripción y URL editables.**
  - Se editan por producto y por categoría. En producto, en la sección "SEO y búsqueda en la tienda"; en categoría, en "SEO". [T1](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos)
  - Límites: "Para el título, el máximo es de 70 caracteres. Para la descripción, el máximo es de 160 caracteres." [T1](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos)
  - Si la URL no se define, o ya existe una igual, "se genera una nueva". La carga masiva no permite cambiar la URL de un producto. [T1](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos)
  - Por defecto, "el sistema toma la información que configuraste en tus títulos y descripciones". [T1](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos)
  - Tiendanube lista "edición de meta title y meta description en productos y categorías" como función integrada. [T3](https://www.tiendanube.com/blog/seo-para-tienda-online/)
- **Estructura de URL.**
  - La FAQ lista "URLs amigables" como función integrada. [T3](https://www.tiendanube.com/blog/seo-para-tienda-online/)
  - No pude confirmar si las rutas fijas (`/productos/`, `/categorias/`) se pueden cambiar: ninguna fuente leída las nombra. Es hueco.
  - Un resumen del buscador dice que cambiar el nombre del producto cambia su URL, y que conviene una 301. Es [S] sobre la versión es_CO, así que dejo esto como sin confirmar con la fuente en mano.
- **Sitemap.**
  - Es automático, está en `/sitemap.xml` y "se actualiza diariamente". Google "puede demorar entre pocos días y 3 semanas". [T2](https://ayuda.tiendanube.com/es_ES/google-ads/como-enviar-un-sitemap-a-google)
- **robots.txt.**
  - La FAQ del blog dice que la plataforma genera sitemap.xml y robots.txt automáticamente. [T3](https://www.tiendanube.com/blog/seo-para-tienda-online/)
  - En Nuvemshop: "não é possível editar o arquivo Robots.txt manualmente". El archivo bloquea pantallas como login, panel de administración y finalización de compra. [T6](https://atendimento.nuvemshop.com.br/pt_BR/ferramentas-do-google/como-funciona-o-arquivo-robotstxt-na-nuvemshop)
  - No encontré la afirmación equivalente en el centro de ayuda de Tiendanube Argentina.
- **Canónicas.**
  - La FAQ del blog las lista como función integrada: "etiquetas canónicas para evitar contenido duplicado". [T3](https://www.tiendanube.com/blog/seo-para-tienda-online/)
  - En el cuerpo del mismo artículo la canonical aparece como acción manual para variantes de producto. No dice si la plataforma la aplica sola. [T3](https://www.tiendanube.com/blog/seo-para-tienda-online/)
  - El objeto Product de los temas expone `canonical_url`. Category y Page exponen `seo_title` y `seo_description`; no vi canonical en esos dos. [T5](https://docs.tiendanube.com/help/product)
  - El trato de variantes con parámetros y de filtros es hueco.
- **Datos estructurados.**
  - Los temas usan JSON-LD: "Ahora, utilizamos el formato JSON-LD". El snippet `item-structured-data.tpl` define `@type: Product` con nombre, imagen, descripción (SEO), SKU, marca, peso y `offers` (URL, moneda, precio, disponibilidad, nivel de inventario, vendedor). [T4](https://docs.tiendanube.com/help/data-estructurada-json-ld)
  - Si un tema ya lo trae depende de "cuan actualizado esté tu código": el desarrollador tiene que agregar los snippets a temas viejos. [T4](https://docs.tiendanube.com/help/data-estructurada-json-ld)
- **Google Shopping.**
  - Hay una integración directa que se activa en Canales de ventas. El feed XML manual es la versión anterior. Tiendanube envía solo el precio original, así que los descuentos por medio de pago pueden causar rechazos por diferencia de precio. No se puede vincular una cuenta Multi Client Account (MCA). [T7](https://ayuda.tiendanube.com/es_ES/como-configurar-el-feed-de-productos-para-google-shopping) [S]
- **Blog, alt text, velocidad.**
  - Blog: "se puede integrar un blog dentro de la misma plataforma" y se puede "conectar tu blog directamente desde el panel". [T3](https://www.tiendanube.com/blog/seo-para-tienda-online/)
  - Velocidad: "En Tiendanube ya viene integrada por defecto" la CDN. [T3](https://www.tiendanube.com/blog/seo-para-tienda-online/)
  - El mismo blog afirma que las tiendas de Tiendanube son más rápidas y estables que las de Shopify en Latinoamérica, citando un informe de CrUX. Es afirmación propia, no la verifiqué.
  - Alt text: el blog solo da recomendaciones; no dice que la plataforma tenga un campo por defecto. Es hueco.
- **Plan.**
  - El artículo de ayuda de SEO de producto no menciona dependencia de plan; solo pide permisos sobre productos. [T1](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos)
  - El dominio propio no está en el plan gratuito (Inicial en Argentina). Requiere plan pago. [T9](https://ayuda.tiendanube.com/es_ES/175777-abc-del-dominio-propio/como-tener-una-direccion-web-sin-el-mitiendanubecom) [S]
  - Precios en Argentina según el buscador: Esencial $27.999/mes, Impulso $79.999, Escala $244.999. [T8](https://www.tiendanube.com/planes-y-precios) [S]
  - No pude confirmar la tabla de qué plan incluye Google Shopping.
- **Redirecciones 301.** Existen: "Redireccionamiento 301" figura en Configuraciones avanzadas. [T1](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos)
- **Discrepancia entre fuentes.** El blog de Tiendanube recomienda títulos de hasta 60 caracteres y meta descripciones de hasta 105. El administrador admite 70 y 160. [T3](https://www.tiendanube.com/blog/seo-para-tienda-online/) vs. [T1](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos). El blog es recomendación general y el límite del administrador es lo que se puede escribir.
- **Quejas documentadas.** No encontré foros de la comunidad oficial de Tiendanube sobre SEO. Es hueco.

---

## 2. Shopify

### Fuentes

| # | Fuente | Tipo | Aut | Prof | Ej | Uni | Rec | Lectura |
|---|---|---|---|---|---|---|---|---|
| S1 | [Help: Redirecciones de URL](https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect) | primaria | 3 | 3 | 2 | 3 | 2 | [L] |
| S2 | [Help: SEO overview](https://help.shopify.com/en/manual/promoting-marketing/seo/seo-overview) | primaria | 3 | 2 | 2 | 2 | 3 | [L] |
| S3 | [Help: Agregar palabras clave (títulos, meta, alt)](https://help.shopify.com/en/manual/promoting-marketing/seo/adding-keywords) | primaria | 3 | 2 | 1 | 2 | 2 | [L] |
| S4 | [shopify.dev: Customize robots.txt](https://shopify.dev/docs/storefronts/themes/seo/robots-txt) y [robots.txt.liquid](https://shopify.dev/docs/storefronts/themes/architecture/templates/robots-txt-liquid) | primaria | 3 | 3 | 3 | 3 | 3 | [L] |
| S5 | [Help: Google & YouTube, sincronizar](https://help.shopify.com/en/manual/online-sales-channels/marketplaces/google/getting-setup/syncing-products) y [free listings](https://help.shopify.com/en/manual/online-sales-channels/marketplaces/google/shopping-on-google/google-listings) | primaria | 3 | 2 | 2 | 2 | 3 | [S] |
| S6 | [Help: Web performance](https://help.shopify.com/en/manual/online-store/web-performance/overview) y [shopify.dev: performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance) | primaria | 3 | 2 | 2 | 2 | 3 | [S] |
| S7 | [shopify.dev: Theme store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) | primaria | 3 | 2 | 1 | 2 | 3 | [S] |
| S8 | [shopify.dev: Liquid object `variant`](https://shopify.dev/docs/api/liquid/objects/variant) y [`product`](https://shopify.dev/docs/api/liquid/objects/product) | primaria | 3 | 3 | 2 | 3 | 3 | [S] |
| S9 | [Shopify Blog: set canonical url](https://www.shopify.com/blog/set-canonical-url-shopify) | primaria, blog | 2 | 2 | 2 | 2 | 2 | [S] |
| S10 | [Community: cambiar prefijos de URL](https://community.shopify.com/t/changing-default-word-products-in-the-url/263056) y otros hilos | secundaria, comunidad oficial | 1 | 1 | 2 | 2 | 2 | [S] |
| S11 | [Community: duplicado /collections/](https://community.shopify.com/t/collections-duplicate-content-products-urls/186571/1) | secundaria | 1 | 1 | 1 | 2 | 1 (enero 2023) | [L] |
| S12 | [Community: robots.txt](https://community.shopify.com/t/robots-txt-is-disallowing-multiple-pages-how-to-fix-this/299276) | secundaria | 1 | 1 | 1 | 2 | 2 | [S] |

### Afirmaciones

- **Estructura de URL.**
  - No hay fuente primaria que diga si se pueden cambiar los prefijos. Lo que sí es primario: no se pueden redirigir. "You can't redirect URLs that use fixed Shopify paths: `/products`, `/collections`, `/collections/all`." [S1](https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect)
  - Los hilos de la comunidad (secundaria) coinciden en que solo se edita el handle, es decir, el texto después de la última barra. [S10](https://community.shopify.com/t/changing-default-word-products-in-the-url/263056) [S]
  - Soluciones de terceros mencionadas en la comunidad: Cloudflare Worker o storefront headless. Ambas con costo de mantenimiento. Un ayudante advierte que el proxy exige reescribir links, canonicals y checkout. [S10]
  - Shopify dev recomienda no servir la tienda por un reverse proxy: "masks real problems, distorts metrics, and adds latency". [S6](https://shopify.dev/docs/storefronts/themes/best-practices/performance) [S]
- **Título y meta descripción.**
  - "You can enter up to 70 characters in the title." Recomienda 60 para evitar que se acorte. Para la descripción: "It's recommended that 160 characters is used". [S3](https://help.shopify.com/en/manual/promoting-marketing/seo/adding-keywords)
  - La etiqueta title sale de `{{ page_title }}` en `theme.liquid`. Si queda en blanco, el tema la arma con el nombre de la tienda y el título del contenido. [S3]
  - Los títulos se editan en Online Store > Preferences y el tema suma el nombre de la tienda. [S2](https://help.shopify.com/en/manual/promoting-marketing/seo/seo-overview)
  - Las plantillas por defecto de título por producto o colección quedan como hueco: la página no las describe.
- **Sitemap y robots.txt.**
  - "Your website's sitemap.xml and robots.txt files are automatically generated." [S2](https://help.shopify.com/en/manual/promoting-marketing/seo/seo-overview)
  - El sitemap raíz enlaza a sitemaps separados de productos, colecciones, blogs y páginas. Esto lo tomo del resumen del buscador sobre la guía de migración. [S]
  - robots.txt es editable mediante `robots.txt.liquid`. "Adding this template replaces Shopify's generated `robots.txt` output." Se pueden agregar reglas a un grupo, quitar reglas del default (con `unless`), agregar reglas propias y líneas `Sitemap:`. [S4](https://shopify.dev/docs/storefronts/themes/architecture/templates/robots-txt-liquid)
  - Antes de publicar hay que guardar una copia de la salida actual de `/robots.txt` y compararla. La plantilla "can't be a JSON template". [S4]
- **Canónicas y URLs duplicadas.**
  - "Auto-generated canonical tags are added to pages to prevent duplicate content from appearing in search results." [S2](https://help.shopify.com/en/manual/promoting-marketing/seo/seo-overview)
  - Según el blog de Shopify, los temas de la Theme Store traen canonicals. [S9] [S]
  - Según la comunidad (secundaria), la URL por colección (`/collections/x/products/y`) se canonicaliza a `/products/y`. Esto es [S] y no encontré una fuente primaria que lo diga.
  - Las páginas `/collections/all/{tag}` se generan automáticamente y no hay forma nativa de ponerles una canonical propia desde el admin, según un hilo de la comunidad. [S10]
  - La paginación (`?page=2`) puede indexarse con canonicals autorreferentes. [S10] [S]
  - Variantes: la URL es `/products/[handle]?variant=[id]` y el parámetro solo rige en páginas de producto. En listados o colecciones filtradas, la URL del producto puede traer el parámetro de la variante más relevante. [S8](https://shopify.dev/docs/api/liquid/objects/variant) [S]
- **Datos estructurados.**
  - "Structured data implementation is built into Shopify themes to help search engines better understand your content." [S2]
  - La Theme Store exige rich snippets de producto y canonical en el SEO del tema. [S7](https://shopify.dev/docs/storefronts/themes/store/requirements) [S]
  - Una queja de desarrolladores (secundaria): el `structured_data` de variante omite la descripción y Merchant Center avisa por descripción faltante. [community.shopify.dev](https://community.shopify.dev/t/structured-data-for-variant-does-not-include-description/37858) [S]
- **Google y YouTube.**
  - Los productos sincronizados al Merchant Center con la app pueden mostrarse gratis en la pestaña Shopping. Primera sincronización hasta 24 horas, después cambios en pocas horas. Cada cuenta de Merchant Center se conecta a una sola tienda. [S5](https://help.shopify.com/en/manual/online-sales-channels/marketplaces/google/getting-setup/syncing-products) [S]
  - Los listados gratuitos amplios (Search, Images, Maps, Lens) se describen para tiendas elegibles de Estados Unidos. Si el resto de países se comporta igual, no lo confirmé: hueco para Argentina. [S5]
- **Redirecciones 301.** Existen y se crean en Content > Menus > URL redirects, con importación CSV. Tope de 100.000, y 20.000.000 en Plus. [S1](https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect) Shopify recomienda "Set up 301 redirects when moving or discontinuing products". [S2]
- **Blog, alt text, velocidad.**
  - Blog incorporado, con SEO por entrada. [S2]
  - Alt text editable en la biblioteca de medios, y en imagen de producto, de colección o de entrada del blog. [S2] [S3]
  - Velocidad: CDN operada por Cloudflare "at no additional charge". La ayuda dice HTTP/2 y shopify.dev dice HTTP/3 y TLS 1.3. Discrepan, y la ayuda es más vieja. Core Web Vitals en el panel: LCP bueno <= 2500 ms, CLS bueno <= 0,1. La Theme Store exige un Lighthouse promedio mínimo de 60. [S6] [S]
- **Apps de SEO y plan.**
  - Shopify sugiere analizar el SEO con apps de la App Store o contratar un Partner. [S2] No relevé nombres, precios ni cuáles son las más usadas: hueco.
  - Las funciones de SEO de las páginas leídas no mencionan dependencia de plan. Lo único que depende del plan es el tope de redirecciones. [S1]
- **Quejas documentadas.**
  - El 25/01/2023 un comerciante con 15.000 URLs de productos preguntó por el contenido duplicado porque Google "is starting to index all of the additional Pages". La página leída no muestra respuestas. [S11](https://community.shopify.com/t/collections-duplicate-content-products-urls/186571/1)
  - Dueños de tiendas marcan como error de SEO las reglas de robots.txt por defecto. Según el resumen del buscador, el soporte dice que funciona como está pensado. [S12] [S]

---

## 3. WooCommerce (sobre WordPress)

### Fuentes

| # | Fuente | Tipo | Aut | Prof | Ej | Uni | Rec | Lectura |
|---|---|---|---|---|---|---|---|---|
| W1 | [woocommerce.com: Permalinks](https://woocommerce.com/document/permalinks/) | primaria | 3 | 2 | 2 | 3 | 2 | [L] |
| W2 | [developer.woocommerce.com: cambios de permalink en 10.5](https://developer.woocommerce.com/2026/01/13/product-permalink-changes-coming-in-woocommerce-10-5/) | primaria | 3 | 3 | 2 | 3 | 3 (2026-01-13) | [L] |
| W3 | [GitHub wiki: Structured data for products](https://github.com/woocommerce/woocommerce/wiki/Structured-data-for-products) | primaria | 3 | 2 | 2 | 3 | 1 (unos 7,5 años según el buscador) | [L] |
| W4 | [woocommerce.com: Google for WooCommerce, feed y listados gratuitos](https://woocommerce.com/document/google-for-woocommerce/get-started/product-feed-information-and-free-listings/) | primaria | 3 | 2 | 2 | 2 | 2 | [L] |
| W5 | [make.wordpress.org: sitemaps nativos de WP 5.5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/) y [WP_Sitemaps](https://developer.wordpress.org/reference/classes/wp_sitemaps/) | primaria | 3 | 2 | 1 | 3 | 1 (2020) | [S] |
| W6 | [developer.wordpress.org: hook `robots_txt`](https://developer.wordpress.org/reference/hooks/robots_txt/) | primaria | 3 | 1 | 1 | 2 | 2 | [S] |
| W7 | [Rank Math: duplicados en WooCommerce](https://rankmath.com/kb/woocommerce-duplicate-content-issues/) y [precios](https://rankmath.com/pricing/) | secundaria, vendor | 2 | 2 | 2 | 2 | 3 | [S] |
| W8 | [Yoast vs Rank Math](https://yoast.com/choosing-the-right-wordpress-seo-plugin-for-your-business-yoast-vs-rank-math/) | secundaria, vendor | 2 | 1 | 1 | 1 | 3 | [S] |
| W9 | [woocommerce.com: Smart Filter Noindex](https://woocommerce.com/document/smart-filter-noindex/) | primaria, extensión paga | 2 | 2 | 1 | 2 | 3 | [S] |

### Afirmaciones

- **Estructura de URL.** Es la plataforma con más libertad.
  - Opciones de base de producto: Default, Shop base, "Shop base with category" y Custom base. La base de categoría por defecto es `product-category`. [W1](https://woocommerce.com/document/permalinks/)
  - Consejo oficial: "Keep permalink structures as short as possible and include keywords that relate to the content they categorize." [W1]
  - Atributos: la base por defecto está vacía y produce `example.com/size/medium`, solo si "Enable archives" está activo. [W1]
  - Desde WooCommerce 10.5, con "Shop base with category" o bases con `%product_cat%`, se elige la categoría más profunda "rather than sorting by parent term ID". Cambia la URL de algunos productos y WooCommerce "will automatically 301 redirect old URLs". El filtro `wc_product_post_type_link_product_cat` restaura el comportamiento anterior. [W2](https://developer.woocommerce.com/2026/01/13/product-permalink-changes-coming-in-woocommerce-10-5/)
  - No se puede elegir una categoría principal por producto desde el núcleo: el desarrollador respondió que "no está en desarrollo". [W2]
- **Título y meta.** El núcleo de WooCommerce no trae un panel de SEO. Esto lo infiero de que todas las fuentes de títulos y metas son plugins. Las leídas no lo dicen expresamente, así que lo marco como sin confirmar.
- **Sitemap.**
  - WordPress trae sitemap nativo desde 5.5 en `/wp-sitemap.xml`, con máximo de 2.000 URLs por archivo, y agrega la línea `Sitemap:` a robots.txt solo si el sitio es público. [W5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/) [S]
  - Cambiar la ruta no es trivial. Un colaborador del núcleo dijo que un filtro para el prefijo "is not really doable as rewrite rules are persisted in the database". [W5]
  - Los plugins Yoast y Rank Math generan su propio sitemap y reemplazan al nativo.
- **robots.txt.**
  - WordPress sirve un robots.txt virtual solo si no existe un archivo físico en la raíz; se puede filtrar con el hook `robots_txt`. [W6](https://developer.wordpress.org/reference/hooks/robots_txt/) [S] (la parte del archivo físico viene de fichas de plugins, no del núcleo)
  - La afirmación de que el ajuste "Discourage search engines" agrega noindex y no un Disallow viene de un plugin de terceros. No la confirmé con documentación del núcleo.
- **Canónicas y variantes.**
  - Las canonicals de producto, categoría y atributos las agrega el plugin de SEO. Rank Math dice que apunta las páginas filtradas a la página principal. [W7] [S]
  - Se documentan casos límite: la canonical deja de mostrarse al combinar dos filtros en una página de atributos. Es un hilo de wordpress.org. [S]
  - La extensión oficial Smart Filter Noindex pone noindex a URLs de filtro y "does not modify robots.txt". [W9] [S]
  - Variantes: no encontré fuente oficial sobre cómo se comportan las URLs `?attribute_pa_...`. Es hueco.
- **Datos estructurados.**
  - "WooCommerce outputs structured data to the page in `JSON+LD` format." En páginas de producto: nombre, imagen, descripción, SKU, `offers`. [W3](https://github.com/woocommerce/woocommerce/wiki/Structured-data-for-products)
  - Filtros: `woocommerce_structured_data_product` y `woocommerce_structured_data_product_offer`. [W3]
  - Desde 3.5.6 no genera datos estructurados en archivos o categorías. [W3] El wiki es viejo; puede haber cambiado.
  - Los plugins de terceros dicen llenar huecos del markup nativo, como reseñas y envío/devoluciones. Dato secundario.
- **Google Merchant Center.**
  - Google for WooCommerce sincroniza los datos generales del producto. Los activos pueden aparecer en free listings en la pestaña Shopping "within the next 3-5 days". Los productos sin título, descripción, ID, enlace e imagen no se sincronizan. [W4](https://woocommerce.com/document/google-for-woocommerce/get-started/product-feed-information-and-free-listings/)
  - Un producto sale del feed si "hasn't been updated in 30 days". Los atributos globales personalizados no se sincronizan sin la herramienta de mapeo. [W4]
- **Redirecciones 301.** Existen mediante plugins o configuración del servidor, salvo el caso de 10.5, que las hace automáticas. [W2]
- **Blog, alt text, velocidad.**
  - Blog: WordPress es un CMS, con entradas nativas. Esto es conocimiento general, no lo verifiqué en fuente leída.
  - Alt text: campo nativo de la biblioteca de medios. Tampoco lo verifiqué en fuente leída.
  - Velocidad: depende del hosting, el tema y los plugins; no hay CDN incluida. Es hueco documental.
- **Plugins y precios.**
  - Rank Math: versión gratuita y PRO desde unos €95,88 al año, y €107,88 más impuestos en la renovación según su página de precios. [W7](https://rankmath.com/pricing/) [S]
  - Yoast: Premium en $118,80 al año sin IVA, según la comparación de Yoast. [W8](https://yoast.com/choosing-the-right-wordpress-seo-plugin-for-your-business-yoast-vs-rank-math/) [S]
  - Queja documentada: en un hilo de wordpress.org un usuario dice que Rank Math "heavily push" la versión paga para WooCommerce. Rank Math responde que el análisis de contenido específico de ecommerce está en PRO. [S]
  - Hay variaciones de moneda y descuentos entre páginas, así que los precios son orientativos.
- **Plan.** No aplica un plan de plataforma: las funciones dependen del hosting y los plugins.

---

## 4. Empretienda y VTEX (una línea cada una)

- **Empretienda:** en la búsqueda solo apareció su guía de [Google Shopping](https://empretienda.helpjuice.com/google-shopping) (en el panel: "Potenciar mi tienda > Canales de venta > Google shopping"), que no leí en profundidad [S]. No encontré su documentación de títulos, URLs ni sitemap. Es hueco.
- **VTEX:** tiene editor nativo de robots.txt (Store Settings > Storefront > Settings > SEO > Robots.txt) y genera canonicals automáticas en producto, categoría, marca y páginas custom. La URL de producto sale del campo `textLink`. Fuentes: [developers.vtex.com SEO](https://developers.vtex.com/docs/guides/storefront-seo) y [help.vtex.com](https://help.vtex.com/en/docs/tutorials/google-search-console-tracking-robots-txt?locale=en) [S].

---

## 5. Lo que pide Google (contraste)

Fuentes primarias: [Ecommerce URL structure](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites) [L] y [Product variants](https://developers.google.com/search/docs/appearance/structured-data/product-variants) [S].

- Cada variante debe tener una URL propia, como segmento de ruta (`/t-shirt/green`) o parámetro (`/t-shirt?color=green`). Con parámetros opcionales, usar "the URL with the query parameter omitted as the canonical URL". [L]
- Para productos con URL propia por variante, "include the canonical product URL on all variant pages". [L]
- Recomienda palabras descriptivas en la ruta (`/product/black-t-shirt-with-a-white-collar`) antes que `/product/3243`. [L]
- El markup `ProductGroup` con `variesBy` y `hasVariant` existe desde febrero de 2024. [S]
- Implicancia para la ficha: lo que Shopify hace con `?variant=` y lo que WooCommerce hace con plugins se puede contrastar con esta regla. La regla de Google sobre el canonical sin parámetro y la práctica de cada plataforma no la verifiqué en vivo.

---

## 6. Tabla comparativa

Todo sale de las fuentes anteriores. "Hueco" significa que no lo encontré. [S] marca resumen secundario.

| Aspecto | Tiendanube | Shopify | WooCommerce |
|---|---|---|---|
| Rutas de URL (prefijos) | Hueco | Fijos (`/products/`, `/collections/`); no se pueden redirigir [S1]. Solo se edita el handle (comunidad [S]) | Editables: base de producto, de categoría y de atributo [W1] |
| Slug editable | Sí, por producto y categoría [T1]; no en carga masiva | Sí (handle) | Sí (slug nativo de WordPress) |
| Título y meta por ítem | Sí, 70 y 160 caracteres [T1] | Sí, 70 recomendado 60; 160 [S3] | Con plugin de SEO; el núcleo no lo documenta |
| Sitemap | Automático `/sitemap.xml`, diario [T2] | Automático [S2] | `/wp-sitemap.xml` nativo (límite 2.000 URLs por archivo) o el del plugin [S] |
| robots.txt editable | No en Nuvemshop [T6]; Tiendanube AR hueco | Sí, `robots.txt.liquid` [S4] | Sí (virtual, filtro o archivo físico) [S] |
| Canónicas | Anunciadas como función [T3]; `canonical_url` en Product [T5] | Automáticas [S2]; colección a producto (comunidad [S]) | Las pone el plugin de SEO [S] |
| Variantes | Hueco | Parámetro `?variant=` [S8] [S] | Hueco documental |
| Datos estructurados | JSON-LD, depende del tema [T4] | Incluido en temas [S2] | JSON-LD en producto [W3] |
| Google Merchant Center | Integración propia; precio sin descuentos [T7] [S] | App Google & YouTube [S5] [S] | Google for WooCommerce [W4] |
| 301 | Sí [T1] | Sí, hasta 100.000 (Plus 20.000.000) [S1] | Por plugin o servidor; automático en 10.5 [W2] |
| Blog | Integrado o conectado [T3] | Incorporado [S2] | Nativo de WordPress (sin verificar) |
| Alt text | Hueco | Sí [S3] | Nativo de WordPress (sin verificar) |
| Velocidad | CDN incluida [T3] | CDN Cloudflare sin costo [S6] [S] | Depende del hosting; hueco |
| Plugins de SEO | Hueco | Apps de App Store, sin nombres relevados | Yoast (~$119/año), Rank Math (gratis o ~€96-108/año) [S] |
| Depende del plan | Dominio propio requiere plan pago [T9] [S] | Solo el tope de redirecciones [S1] | No hay plan; hosting y plugins |

---

## 7. Huecos

1. **Tiendanube:**
   - Rutas fijas, estructura real de URL, trato de variantes y de filtros con parámetros.
   - robots.txt en Argentina: solo tengo la fuente de Nuvemshop Brasil.
   - Alt text y qué plan incluye Google Shopping, SEO o dominio propio. La tabla de planes no se extrajo completa.
   - Qué hace la plataforma con noindex.
   - Quejas de la comunidad oficial.
2. **Shopify:**
   - La fuente primaria de que la canonical de `/collections/x/products/y` apunta a `/products/y`. Las páginas `site-structure` y `adding-keywords` no mostraron esa parte, y dos URLs de shopify.dev dieron 404.
   - Plantillas por defecto de título y meta.
   - Qué estructura de datos estructurados trae el tema por defecto hoy (Dawn u Horizon).
   - Apps de SEO más usadas y sus precios.
   - Si los listados gratuitos de Google y YouTube funcionan en Argentina.
3. **WooCommerce:**
   - Docs oficiales de título y meta del núcleo.
   - Comportamiento de variantes por URL.
   - Qué canonical emite el núcleo de WordPress sin plugin. No encontré fuente.
   - Si Yoast cobra algo específico para WooCommerce.
   - La versión del wiki de datos estructurados es vieja.
4. **Empretienda:** sin documentación de SEO encontrada. **VTEX:** solo dos puntos en [S]; falta sitemap editable.
5. **Pendiente de verificar en vivo:** la regla de Google (canonical sin parámetro) contra una tienda real de cada plataforma. Recomiendo mirar `view-source` de una tienda real de cada plataforma, no solo la documentación.
6. **Ronda de búsqueda:** usé hasta tres rondas por plataforma, más Google, y no hice una ronda dedicada a comunidades de Tiendanube ni a apps de SEO de Shopify.