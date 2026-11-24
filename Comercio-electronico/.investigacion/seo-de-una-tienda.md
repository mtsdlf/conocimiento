# Informe: SEO de una tienda online (para pymes argentinas en Tiendanube, Shopify y WooCommerce)

**Cómo leer las marcas.** Las páginas de Google, Semrush, Ahrefs y Tiendanube las traje con WebFetch, que devuelve un extracto procesado por un modelo chico, no el HTML crudo. Por eso uso **[L~]**: leí la página, pero a través de ese extracto. Las citas literales salen de esos extractos y conviene reverificarlas contra la página antes de citarlas en una nota. **[S]** es resumen del buscador. Ninguna fuente quedó como [L] pleno. Los puntajes (autoridad, profundidad, ejemplos, unicidad; 1 a 3) son juicio mío. Ninguna página de Google trajo fecha de actualización en el extracto, así que la recencia queda como hueco.

## Parte 1. Cómo encuentra, indexa y ordena Google una tienda

| Fuente | Tipo | Aut / Prof / Ej / Uni | Marca |
|---|---|---|---|
| [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | Primaria | 3 / 2 / 2 / 3 | [L~] |
| [Canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization) | Primaria | 3 / 3 / 2 / 3 | [L~] |
| [Informe de indexación de páginas](https://support.google.com/webmasters/answer/7440203) | Primaria | 3 / 3 / 2 / 3 | [L~] |
| [Cómo lanzar una tienda](https://developers.google.com/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website) | Primaria | 3 / 2 / 1 / 3 | [L~] |

**Afirmaciones**
- **Rastreo y descubrimiento.** Google usa programas automáticos ("crawlers") y encuentra las páginas sobre todo por enlaces: "Google primarily finds pages through links from other pages it already crawled." ([Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide))
- **Indexar no está garantizado.** Seguir las pautas solo vuelve más probable aparecer. Para ver una página como la ve Google se usa la Inspección de URL de Search Console. ([Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide))
- **Cuánto tarda.** "Some changes might take effect in a few hours, others could take several months." La guía pide evaluar después de semanas, no de días. ([Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide))
- **Mitos que la propia guía descarta.** Google no usa la meta keywords. No hay un largo de texto mágico: "there's no magical word count target, minimum or maximum." El contenido duplicado "es ineficiente, pero no causa una acción manual". ([Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide))
- **Estados de no indexación.** El informe de indexación distingue varios casos. "Crawled - currently not indexed" no siempre es un problema. "Discovered - currently not indexed" significa que Google la encontró pero todavía no la rastreó. "Soft 404" es una página que muestra "no encontrado" pero responde con código de éxito. ([Informe de indexación](https://support.google.com/webmasters/answer/7440203))
- **Lanzamiento.** Hay que verificar la propiedad en Search Console, pedir indexación y seguir el avance con el informe de indexación. ([Lanzar tienda](https://developers.google.com/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website))

**Recurso canónico:** la SEO Starter Guide, completa pero salteando lo que no aplica a tiendas. Fijarse en las secciones de rastreo e indexación, títulos y snippets, imágenes, y la lista de mitos.

## Parte 2. Lo propio de una tienda

| Fuente | Tipo | Aut / Prof / Ej / Uni | Marca |
|---|---|---|---|
| [Faceted navigation](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation) | Primaria | 3 / 3 / 3 / 3 | [L~] |
| [URL structure para ecommerce](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites) | Primaria | 3 / 2 / 2 / 3 | [L~] |
| [Paginación](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading) | Primaria | 3 / 2 / 2 / 3 | [L~] |
| [Product structured data](https://developers.google.com/search/docs/appearance/structured-data/product) | Primaria | 3 / 3 / 2 / 3 | [L~] (el extracto no trajo la lista de propiedades) |
| [Dónde puede aparecer el contenido de ecommerce](https://developers.google.com/search/docs/specialty/ecommerce/where-ecommerce-data-can-appear-on-google) | Primaria | 3 / 2 / 1 / 3 | [L~] |
| [Listados gratuitos, Merchant Center](https://support.google.com/merchants/answer/9199328) | Primaria | 3 / 2 / 2 / 3 | [L~] |
| [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) | Primaria | 3 / 2 / 1 / 3 | [L~] |
| Mueller sobre agotados, en [seroundtable](https://www.seroundtable.com/google-out-of-stock-seo-18268.html) y [SEJ](https://www.searchenginejournal.com/google-out-of-stock-products-may-impact-search-visibility/444500/) | Declaración de un Googler, vía prensa del rubro | 2 / 1 / 1 / 2 | [S] |

**Afirmaciones**
- **Facetas y filtros.** "If you don't need the faceted navigation URLs potentially indexed, prevent crawling of these URLs." Lo que se recomienda mantener rastreable son las fichas de producto y el listado sin filtrar. ([Faceted navigation](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation))
  - Para bloquear se usa robots.txt, por ejemplo `/*?*color=`.
  - Canonical hacia la versión sin filtro sirve, pero es "generally less effective in the long term".
  - nofollow solo funciona si todos los enlaces a esa URL lo llevan.
  - Los filtros después de `#` Google los ignora.
  - Una combinación sin resultados debe devolver 404.
- **Variantes.** "Make sure that each variant can be identified by a separate URL", ya sea como ruta (`/t-shirt/green`) o como parámetro (`/t-shirt?color=green`). Se pone "the canonical product URL on all variant pages". ([URL structure](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites))
  - La documentación de datos estructurados dice que el marcado de variantes ayuda a entender qué productos son variaciones del mismo producto padre. ([Product](https://developers.google.com/search/docs/appearance/structured-data/product))
  - Esas dos páginas hablan de URL propia por variante con canónica al producto base. No pude confirmar la pregunta "una URL o varias" en una página que la trate de frente. Los enlaces directos a `/ecommerce/variants` y a `crawlable-faceted-navigation` dieron 404.
- **Paginación.** Cada página lleva su URL única y enlaces `<a href>` a la siguiente. No se usa `#` para el número de página. No se usa la primera página como canónica de toda la secuencia. Google ya no usa rel=next/prev: "Google no longer uses these tags". Con scroll infinito el contenido necesita enlaces rastreables, porque los crawlers no hacen clic ni disparan el scroll de forma confiable. ([Paginación](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading))
- **Canónicas y duplicados.** Las canónicas son "a hint, not a rule". El duplicado por filtros y orden es normal y no es spam por sí mismo. ([Canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization))
  - Sobre las descripciones del fabricante no encontré una afirmación directa de Google. Es un hueco.
- **Datos estructurados.** Product snippets sirven para páginas donde no se puede comprar. Merchant listings son para páginas donde sí, con envío, devoluciones y talles. ([Product](https://developers.google.com/search/docs/appearance/structured-data/product))
  - Se puede dar la información con marcado, con feed a Merchant Center o con ambos, y hacer las dos cosas "maximizes your eligibility".
  - El Shopping tab requiere Merchant Center. ([Dónde aparece](https://developers.google.com/search/docs/specialty/ecommerce/where-ecommerce-data-can-appear-on-google))
- **Listados gratuitos.** Generan "organic traffic" sin costo. Los atributos obligatorios son id, título, link, imagen, precio, descripción y disponibilidad. Argentina no está entre los países donde el envío es obligatorio. La página nombra a Argentina solo para el Shopping Knowledge Panel, y no dice nada sobre los demás espacios. ([Merchant Center](https://support.google.com/merchants/answer/9199328))
- **Agotados y discontinuados.** No encontré documentación vigente de Google, solo declaraciones de Mueller (2016 a 2018) reportadas por prensa del rubro [S]. Temporalmente agotado: dejar la página y marcar la disponibilidad en el marcado. Discontinuado para siempre: 404 es aceptable, y si hay reemplazo conviene redirigir. Mueller advirtió que Google a veces trata "agotado" como soft 404, aunque no tiene por qué pasar. ([seroundtable](https://www.seroundtable.com/google-out-of-stock-seo-18268.html), [SEJ](https://www.searchenginejournal.com/google-out-of-stock-products-may-impact-search-visibility/444500/))
  - La guía de lanzamiento de Google advierte que no hay que deshabilitar "agregar al carrito" para bloquear compras, porque Google lo puede usar para verificar precios. ([Lanzar tienda](https://developers.google.com/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website))
- **Velocidad.** Umbrales "buenos": LCP en menos de 2,5 s, INP en menos de 200 ms, CLS en menos de 0,1. Google dice que esto "aligns with what our core ranking systems seek to reward", junto con otros aspectos de la experiencia de página. ([Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals))
- **Imágenes.** Nítidas, cerca del texto relevante, con alt descriptivo. ([Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide))

**Recursos canónicos.**
- Facetas y parámetros: la página de faceted navigation, en las reglas de bloqueo y en el 404 para combinaciones vacías.
- Variantes y URLs: la página de URL structure para ecommerce.
- Marcado de producto: la página Product, mirando cuál experiencia (snippet o merchant listing) aplica.
- Feed y gratuitos: la ayuda de listados gratuitos, para los atributos obligatorios.

## Parte 3. Qué resuelve una plataforma alojada y qué queda en el comercio

| Fuente | Tipo | Aut / Prof / Ej / Uni | Marca |
|---|---|---|---|
| [Ayuda de Tiendanube (AR)](https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-lograr-que-mi-tienda-aparezca-en-los-resultados-de-buscadores) y [SEO del producto](https://ayuda.tiendanube.com/es_AR/160351-seo-del-producto/que-son-las-opciones-avanzadas-de-seo-de-mis-productos) | Primaria del proveedor, con interés comercial | 2 / 2 / 2 / 2 | [S] |
| [Shopify: sitemap](https://help.shopify.com/manual/using-themes/find-site-map) | Primaria del proveedor | 2 / 1 / 1 / 2 | [S] |
| [Search Engine Land sobre Shopify](https://searchengineland.com/common-shopify-seo-pitfalls-and-how-to-avoid-them-338197) | Secundaria | 2 / 2 / 2 / 2 | [S] |

**Afirmaciones** (todas de resúmenes del buscador, sin leer las páginas)
- **Tiendanube.** Los títulos SEO tienen un máximo de 70 caracteres y las descripciones de 160, para productos y categorías, y pueden escribirse a mano o con IA. Recomienda no usar títulos tipo "Art 1143". Dice que enviar un sitemap ayuda a indexar y que las tiendas nuevas pueden tardar "entre 4 y 12 semanas" en posicionarse. ([ayuda Tiendanube](https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-lograr-que-mi-tienda-aparezca-en-los-resultados-de-buscadores))
- **Shopify.** Genera sitemap.xml automático con productos, colecciones, páginas y blog. ([Shopify](https://help.shopify.com/manual/using-themes/find-site-map)) Search Engine Land señala que crea URLs duplicadas de producto bajo cada colección, con canónica al producto, y que eso divide los enlaces. ([SEL](https://searchengineland.com/common-shopify-seo-pitfalls-and-how-to-avoid-them-338197))
  - Hay discrepancia sobre cuánto se puede editar robots.txt: una guía dice que desde junio de 2021 se puede, otra que los cambios a las directivas por defecto se revierten.
- **Discrepancia con Google.** Tiendanube dice que copiar textos hace que "los buscadores penalicen esas páginas". Google dice que el duplicado no causa acción manual y que es solo ineficiente. Las dos posturas van en la nota.

**Hueco: WooCommerce.** No busqué su documentación. No hay fuente sobre qué da por defecto y qué depende de plugins.

**Recurso canónico:** la ayuda de SEO de cada plataforma, leída con la lista de la Parte 2 al lado para contrastar qué hace sola y qué no.

## Parte 4. Evidencia

| Fuente | Tipo | Aut / Prof / Ej / Uni | Marca |
|---|---|---|---|
| [Ahrefs, cuánto tarda en rankear](https://ahrefs.com/blog/how-long-does-it-take-to-rank/) (15/5/2025) | Secundaria, con interés comercial | 2 / 2 / 1 / 3 | [L~] |
| [Semrush, mix de canales](https://semrush.com/blog/traffic-channel-mix-study) (27/4/2026) | Secundaria, con interés comercial | 2 / 2 / 1 / 3 | [L~] |
| Baye, De los Santos y Wildenbeest (2016), [J. Econ. & Mgmt Strategy 25(1)](https://econpapers.repec.org/RePEc:bla:jemstr:v:25:y:2016:i:1:p:6-31) | Académica | 3 / 3 / 2 / 3 | [S] |
| Weinberg y Mares, *Traction* (2015), cap. de SEO | Libro de práctica | 2 / 2 / 2 / 2 | [S] (no leí el texto) |
| Estudio Anual 2024 de CACE (Kantar, 1.102 encuestados) | Primaria local | 2 / 1 / 1 / 3 | [S] |
| Otros agregadores de estadísticas, como [Opensend](https://opensend.com/post/organic-traffic-ecommerce) y [Charle](https://www.charle.co.uk/articles/ecommerce-seo-statistics/) | Terciarias | 1 / 1 / 1 / 1 | [S] |

**Afirmaciones**
- **Cuánto pesa el orgánico.** La cifra depende de la fuente y del universo.
  - Semrush, con más de 50.000 sitios en 17 industrias y datos de 2025, dice que el orgánico "represents 16.04% of total traffic", con tendencia a bajar y +2,38% de crecimiento en 2025. Para retail solo da el crecimiento (+0,52%). El nivel por industria está en gráficos que el extracto no trajo. ([Semrush](https://semrush.com/blog/traffic-channel-mix-study))
  - Los agregadores citan 43% (BrightEdge 2024, vía intermediarios) y casi 47% (SE Ranking 2025). Son terciarias y no verifiqué las primarias. ([Opensend](https://opensend.com/post/organic-traffic-ecommerce), [Charle](https://www.charle.co.uk/articles/ecommerce-seo-statistics/))
  - Las dos cifras no se pueden comparar porque cambian la medición y el universo. No encontré un número de pymes ni de Argentina.
- **Qué dice CACE.** Los buscadores están entre las fuentes más consultadas antes de comprar, junto con marketplaces, redes y sitios de marca. Eso mide dónde se informa el consumidor, no de dónde llega el tráfico a una tienda. ([CACE 2024](https://cace.org.ar/wp-content/uploads/2025/03/2024_anual_informe_Tendencias-en-eCommerce.pdf), vía resumen del buscador; el PDF dio 404 al abrirlo directo)
- **Cuánto tarda.** Ahrefs: solo el 1,74% de las URLs nuevas llega al top 10 en un año, contra 5,7% en 2017. Con un filtro (contenido no vacío en inglés) sube a 6,11%, que el autor llama "a more fair number to use". El 40,82% de las que llegan lo logra en el primer mes. Para keywords de alto volumen tardan más: el 94% nunca rankeó. ([Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/))
  - Salvedades del propio autor: la edad se mide desde que el crawler de Ahrefs vio la URL, y puede haber diferencias de muestreo. Esto es correlación, no causa.
  - Google dice "horas a varios meses" y Tiendanube "4 a 12 semanas". Las tres cifras no se contradicen del todo, pero miden cosas distintas.
- **Posición e impacto.** Baye et al. (2016) usaron datos de 759 grandes retailers norteamericanos de un mes de 2012. Hallaron que la posición entre resultados orgánicos influye fuerte en los clics, y que la marca suma clics extra. La cifra de "1% de mejora de posición da +1,3% de tráfico" viene solo de un resumen secundario. Ojo: son grandes retailers, un mes y datos de 2012. ([EconPapers](https://econpapers.repec.org/RePEc:bla:jemstr:v:25:y:2016:i:1:p:6-31))
- **Traction, long tail vs. fat head.** Desde resúmenes: el capítulo plantea dos estrategias, "fat head" (pocos términos de mucho volumen) y "long tail" (muchas frases específicas con contenido rico). Dice que todo se reduce a contenido y enlaces, y que la clave es conseguir enlaces con una forma escalable. Cuenta el caso de un fundador cuya búsqueda tenía poco volumen y por eso SEO no alcanzaba a sus metas de tracción. El texto exacto no lo leí. ([Goodreads notes](https://www.goodreads.com/notes/26619894-traction/86569892-tahereh-falahatgar-etminani/c813eeef-1a89-45ff-aff3-548f12b279e7), [vectree](https://vectree.io/c/search-engine-algorithms-keyword-intent-targeting-and-balancing-paid-sem-with-long-tail-seo))
- **Factores con evidencia y mitos.** La mejor evidencia de factores es la propia lista de Google, que desmiente meta keywords, largo de texto mágico y penalización por duplicado. No encontré en esta ronda un estudio con método que sostenga o refute otros factores, como los enlaces o los Core Web Vitals en tiendas chicas.

**Recursos canónicos.** Para cuánto tarda, el estudio de Ahrefs, leyendo método y salvedades antes que el titular, siempre marcado como fuente con interés comercial. Para cuándo sirve el SEO como canal, el capítulo de Traction (hay que leerlo directo, la fuente que vi es indirecta). Para la evidencia académica, Baye et al. con la salvedad de los años y del tamaño de los retailers.

## Parte 5. Cómo se cuida mes a mes: Search Console

| Fuente | Tipo | Aut / Prof / Ej / Uni | Marca |
|---|---|---|---|
| [Informe de rendimiento](https://support.google.com/webmasters/answer/7576553) | Primaria | 3 / 2 / 1 / 3 | [L~] |
| [Informe de indexación de páginas](https://support.google.com/webmasters/answer/7440203) | Primaria | 3 / 3 / 2 / 3 | [L~] |
| [Listados gratuitos, Performance en Merchant Center](https://support.google.com/merchants/answer/9199328) | Primaria | 3 / 1 / 1 / 3 | [L~] |

**Afirmaciones**
- **Rendimiento.** Métricas: clics, impresiones, CTR (clics sobre impresiones) y posición promedio ("the topmost result from your site"). Dimensiones: consultas, páginas, países, dispositivos, apariencia en búsqueda y fechas. Dos resultados del mismo sitio para una consulta cuentan como una impresión en el total del gráfico. ([Rendimiento](https://support.google.com/webmasters/answer/7576553))
- **Indexación.** Lo que se revisa es el recuento de páginas indexadas y no indexadas, y la razón de las no indexadas (noindex, robots.txt, 404, 5xx, soft 404, duplicadas). "Alternate page with proper canonical tag" es normal y no requiere acción. ([Indexación](https://support.google.com/webmasters/answer/7440203))
- **Merchant Center.** El rendimiento de los listados gratuitos se ve en la página Performance de Merchant Center, filtrando por listados gratuitos. ([Merchant Center](https://support.google.com/merchants/answer/9199328))
- **Mejoras de producto.** No leí la documentación de los informes de mejoras de producto y de comerciante.
- **Retención de datos.** No la encontré en esta ronda.

**Recurso canónico:** el informe de indexación de páginas, leído estado por estado.

## Parte 6. Cómo falla

Salvo lo marcado, es inferencia mía a partir de las partes anteriores, no una fuente aparte.

- **Facetas sin control.** Muchas URLs con parámetros que se rastrean y duplican. Google lo trata en la guía de faceted navigation.
- **Variantes sin canónica.** Cada variante compite con las demás, o Google elige otra canónica distinta de la declarada. Es el estado "Duplicate, Google chose different canonical than user" del informe de indexación.
- **Páginas de producto que no se indexan.** Aparecen como "Crawled" o "Discovered - currently not indexed". Google dice que no siempre es un problema.
- **Agotados mal manejados.** Soft 404 o páginas vacías. Hay solo declaraciones de 2016 a 2018.
- **Contenido pobre.** Títulos como "Art 1143" y descripciones del fabricante sin trabajar. Tiendanube lo desaconseja explícitamente. ([ayuda Tiendanube](https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-lograr-que-mi-tienda-aparezca-en-los-resultados-de-buscadores))
- **Scroll infinito sin enlaces rastreables.** El contenido no se descubre. ([Paginación](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading))
- **Medir mal.** Esperar resultados en días, o confundir cifras de orgánico entre estudios con distinto universo (Partes 1 y 4).
- **Hueco de fuentes.** No busqué fallos documentados, como casos de postmortem o foros de Google. Es un hueco.

## Huecos

- **Weinberg y Mares, Traction:** no leí el capítulo. Falta la cita literal y la parte de cuándo SEO sirve como canal.
- **CACE:** no hay dato de fuentes de tráfico de tiendas argentinas. El PDF 2024 dio 404 al abrirlo directo, y el estudio 2025 no lo busqué.
- **Peso del orgánico en pymes y en Argentina:** sin dato. Las cifras de BrightEdge y SE Ranking son indirectas y sin verificar en la primaria.
- **Factores con evidencia:** sin estudio con método sobre enlaces, Core Web Vitals o contenido en tiendas.
- **Contenido duplicado del fabricante:** sin declaración de Google sobre el caso.
- **Agotados y discontinuados:** sin documentación vigente de Google, solo declaraciones viejas de Mueller. Tampoco hay fecha de ninguna página de Google.
- **Variantes:** no encontré la página de Google que trate "una URL o varias" de frente.
- **Product structured data:** el extracto no trajo propiedades requeridas y recomendadas, ni ProductGroup. Hay que leerla directo.
- **Merchant Center:** no verifiqué disponibilidad en Argentina de listados gratuitos más allá del Shopping Knowledge Panel.
- **WooCommerce y Shopify:** WooCommerce sin fuente. De Shopify no leí la documentación de robots.txt, y las fuentes discrepan.
- **Search Console:** sin retención de datos, ni informes de mejoras de producto y de comerciante.
- **Papers:** solo Baye et al. 2016, que además tiene ya diez años. Los demás estudios que aparecieron (Bosnia, Indonesia, tesis) no los verifiqué.
- **Sin ronda extra:** no usé la tercera ronda de búsquedas en ninguna parte, así que ningún hueco es por agotar las tres.