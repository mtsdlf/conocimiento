---
resumen: >-
  Mudar una tienda es pasarla de una plataforma de tiendas a otra: llevar los datos que se pueden llevar, configurar de nuevo lo que no pasa, conservar las direcciones o redirigirlas, y cambiar el dominio de lugar sin perder los pedidos ni el tráfico de los buscadores.
estado: vigente
estabilidad: semi
fuentes:
  - "Google Search Central, Site move with URL changes (sin fecha visible): https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes (leída entera, 2026-11-24)"
  - "Google Search Central, Changing your hosting (sin fecha visible): https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes (leída entera, 2026-11-24)"
  - "Shopify Help, Migrating to Shopify: https://help.shopify.com/en/manual/migrating-to-shopify (leída, 2026-11-24)"
  - "Shopify Help, Using CSV files to import and export products: https://help.shopify.com/en/manual/products/import-export/using-csv (leída, 2026-11-24)"
  - "Tiendanube Ayuda, cómo migrar mi tienda online de Shopify a Tiendanube: https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube (leída, 2026-11-24)"
  - "Tiendanube Ayuda, cómo migrar mi tienda online de Mercado Shops a Tiendanube: https://ayuda.tiendanube.com/es_AR/migrar-desde-mercado-shops/como-migrar-mi-tienda-online-de-mercado-shops-a-tiendanube (leída, 2026-11-24)"
  - "WooCommerce, Shopify Data Migrator: https://woocommerce.com/document/shopify-data-migrator (leída, 2026-11-24)"
  - "Patrick Stox, Migración web, Ahrefs (2021-12-08): https://ahrefs.com/blog/es/migracion-web (leída, 2026-11-24; practicante)"
  - "Dan Taylor, Only 27% of domain migrations recover in 90 days, SALT.agency (2026-06-26): https://salt.agency/blog/27-of-domain-migrations-recover-in-90-days (leída, 2026-11-24; estudio de una agencia con datos propios)"
  - "Dan Taylor, How long should an SEO migration take, Search Engine Journal (2025-01-08): https://www.searchenginejournal.com/how-long-should-seo-migration-take/492050/ (leída, 2026-11-24; estudio de una agencia con datos propios)"
  - "Search Engine Journal, Google says why site migrations can exceed 4 months (2026-10-13): https://searchenginejournal.com/google-says-why-site-migrations-can-exceed-4-months/592757 (leída, 2026-11-24)"
  - "LitExtension, Ecommerce migration issues: https://litextension.com/blog/ecommerce-migration-issues/ (leída, 2026-11-24; vende migraciones)"
  - "Red Stag Fulfillment, How many BigCommerce stores are there (2025-07, con datos de Store Leads): https://redstagfulfillment.com/how-many-bigcommerce-stores-are-there/ (leída, 2026-11-24; secundaria)"
  - "Sitebulb, When website migrations go wrong: https://sitebulb.com/resources/guides/when-website-migrations-go-wrong-a-practical-guide-to-disaster-recovery/ (según resumen del buscador)"
  - "Sophie Brannon (StudioHawk), What is a migration hangover, Search Engine Journal (2026-06-05): https://www.searchenginejournal.com/what-is-a-migration-hangover-traffic-drop-how-do-you-avoid-it/ (leída, 2026-11-24; opinión de agencia)"
  - "Tiendanube Evolución, migración sin perder SEO (2026-06-26): https://www.tiendanube.com/mx/evolucion/seo (leída, 2026-11-24; servicio comercial de la plataforma)"
  - "Comercio-electronico/.investigacion/mudar-una-tienda.md"
  - "Comercio-electronico/.investigacion/socios-y-mudanza-contraria.md"
aliases: [migrar una tienda, migración de tienda, migración de plataforma, replatforming, re-platforming, store migration, mudanza de tienda]
creado: 2026-11-24
revisado: 2026-11-24
---

# Mudar una tienda

Mudar una tienda es pasarla de una plataforma de tiendas a otra: llevar los datos que se pueden llevar, configurar de nuevo lo que no pasa, conservar las direcciones o redirigirlas, y cambiar el dominio de lugar sin perder los pedidos ni el tráfico de los buscadores.

Lo que se paga al mudarse es un [costo de cambio](../../Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md): datos que no pasan, integraciones que hay que rehacer, tráfico que se pierde por un tiempo. Las plataformas lo bajan para el comercio que llega y no para el que se va. Shopify y Tiendanube publican guías y apps para importar; ninguna guía leída explica cómo irse. Cada plataforma tiene su ficha con lo propio ([Shopify](shopify.md), [Tiendanube](tiendanube.md), [WooCommerce](woocommerce.md)). Las herramientas, con sus precios, están en la ficha [herramientas para mudar una tienda](herramientas-para-mudar-una-tienda.md).

## Qué pasa y qué no

Los productos pasan casi siempre, y lo demás depende de la plataforma de destino. Shopify recomienda un orden: "Import your products first, then your customers, and then any historical orders". Las guías oficiales leídas dejan afuera varias cosas:

| Dato | Pasa | Lo que dicen las fuentes |
|---|---|---|
| Productos, variantes, fotos, categorías | sí, por planilla CSV o por app | Shopify admite hasta 3 opciones y 250 imágenes por producto; las imágenes se bajan desde una URL pública |
| Clientes | sí, sin contraseñas | El migrador de WooCommerce: "User passwords will not be imported as Shopify APIs do not provide password data for security reasons." Hacia Tiendanube, los clientes pasan por una app de email marketing instalada en las dos tiendas |
| Pedidos históricos | depende del destino | Hacia Tiendanube: «El historial de órdenes no se migrará». Queda visible solo en la app de email marketing |
| Descuentos y reseñas | a mano o por soporte | Hacia Tiendanube, los descuentos se exportan y los importa soporte; las reseñas, el soporte de una app de reseñas |
| Tarjetas de regalo | no por planilla | Shopify: "a gift card can't be created by importing a CSV" |
| Medios de pago y de envío | no | Se configuran de nuevo en el destino (los medios de cobro están en [Pagos](../Pagos/pagos.md)) |
| Suscripciones y tarjetas guardadas | sin fuente | Ninguna guía leída lo trata |

Sin contraseña, cada cliente tiene que crear una nueva la primera vez que vuelve. La evidencia oficial viene de la dirección Shopify a WooCommerce: la plataforma de origen no entrega las contraseñas por su API. Para las otras direcciones, y hacia Tiendanube, no se encontró una fuente oficial. Hacia una plataforma de código abierto hay una salida: según LitExtension, que lo vende, un complemento instalado en la tienda nueva deja a los clientes seguir con su contraseña.

Lo que vive dentro de apps tampoco pasa con el importador de la plataforma: reseñas, puntos de fidelidad y suscripciones se mudan app por app. LitExtension dice que cambiar los números de pedido es "a frequent source of support tickets" y recomienda conservar los originales donde la plataforma lo permita. Son opiniones de quien vende migraciones; no hay una medición de cuánto se rompe.

Cambiar los identificadores también rompe cosas. En Shopify, importar variantes con opciones distintas a las de la tienda "deletes existing variant IDs and creates new ones, which can break third-party dependencies". Lo mismo pasa con lo que vive afuera de la tienda y apunta a sus productos: la integración con el [sistema de gestión](../Operaciones-del-comercio/Sistemas-de-gestion-en-el-comercio/integracion-con-tiendas-y-marketplaces.md), y las publicaciones sincronizadas con Mercado Libre (inferencia propia: ninguna fuente midió cuánto se rompe).

## Las direcciones: conservarlas o redirigirlas

El tráfico de los buscadores depende de que cada dirección vieja siga llevando a algún lado. Google separa dos casos. Si las URL no cambian (el mismo dominio y las mismas rutas en otra plataforma), es un cambio de alojamiento. Si cambian, hay que redirigir cada URL vieja a la nueva. Una mudanza entre plataformas con el mismo dominio cae en el primer caso solo si la plataforma nueva deja conservar las rutas. Si impone las suyas, pasa al segundo aunque el dominio no cambie: según guías de terceros, Shopify pone los productos bajo `/products/` sin que se pueda cambiar.

Las reglas de Google para redirigir:

- Redirecciones permanentes del lado del servidor, "301 or 308". "Permanent redirects don't cause a loss in PageRank."
- Una URL vieja va a su equivalente, no todas a la portada: mandar muchas a una página irrelevante puede tomarse como una página inexistente (un soft 404).
- Cadenas cortas: "ideally no more than 3 and fewer than 5" saltos.
- "Keep the redirects for as long as possible, generally at least 1 year."

El mapa de URL viejas a nuevas lo arma quien muda. Shopify y Tiendanube permiten cargar redirecciones, y según los resúmenes de su ayuda no traducen solas las rutas de otra plataforma (las páginas no se abrieron). Las guías de Tiendanube para venir desde Shopify o desde Mercado Shops no mencionan las redirecciones entre sus pasos; su servicio asistido, sí.

## El dominio

El dominio no viaja con la tienda: se apuntan sus registros DNS a la plataforma nueva. Para que el corte sea rápido, Google pide bajar el TTL del DNS (cuánto tiempo guardan los proveedores la dirección vieja) "at least a week in advance" a un valor de pocas horas, y confirmar después que los proveedores de internet ya ven el destino nuevo. El dominio viejo, si lo hay, se renueva y se mantiene con sus certificados mientras haya redirecciones que dependan de él (Ahrefs). En Tiendanube, el dominio propio pide un plan pago.

## El orden de los pasos

Las secuencias oficiales coinciden en lo grueso. La de Shopify tiene once pasos: importar, revisar productos, tema, envíos, impuestos, pagos, pedidos de prueba, cuentas del personal, dominio, punto de venta y redirecciones con el sitemap. Juntando a Google, Shopify, Tiendanube y Ahrefs:

1. Hacé un inventario: todas las URL que reciben tráfico, las apps y las integraciones, y un rastreo del sitio viejo como base.
2. Armá la tienda nueva aparte, sin indexar, e importá productos, clientes y lo que se pueda de pedidos.
3. Configurá de nuevo pagos, envíos e integraciones, y hacé pedidos de prueba.
4. Cargá el mapa de redirecciones y probalo.
5. Cambiá el dominio, sacá el bloqueo de indexación y mandá el sitemap nuevo a Search Console. Guardá también el viejo: sus avisos por redirección "are expected".
6. Seguí el tráfico de las dos versiones y dejá vivo lo viejo hasta que Google haya visitado cada URL al menos una vez.

> [!NOTE] Sin fuente todavía: congelar los cambios en la tienda vieja entre la importación y el corte (para que no queden pedidos o productos de un solo lado) es práctica corriente, pero ninguna fuente leída lo trata.

## Cuánto tráfico se pierde y por cuánto tiempo

Una caída después de mudar es normal; cuánto dura no tiene una respuesta con buen método para el caso de una tienda pyme. Las fuentes no coinciden:

| Fuente | Qué dice | Cuánto vale |
|---|---|---|
| Google | Para un sitio mediano, "it can take a few weeks or more" hasta mostrar las URL nuevas | Primaria, sin cifras de tráfico |
| Search Engine Journal (2025) | 892 mudanzas de dominio: 523 días en promedio para igualar el tráfico anterior; "17% of migrations did not return to the same traffic levels after 1,000 days" | Mismo autor que el de SALT, con muestras que se solapan: los dos estudios cuentan como uno |
| SALT.agency (2026) | 1.052 mudanzas de dominio: mediana de 304 días para recuperarse; 22,8% recuperadas al día 90 y 59,5% al año; 13,9% sin recuperar a los tres años | El único conjunto grande. Solo mudanzas de dominio, detectadas por una caída de 60% o más, y el titular («27%») no coincide con su tabla |
| StudioHawk, en Search Engine Journal (2026) | Caída temporal normal de 10% a 30%; si pasa de 50% y no se estabiliza en cuatro semanas, puede durar "12 to 18 months" | Opinión de una agencia, sin datos |
| Tiendanube Evolución (el plan de Tiendanube que incluye migración asistida) | Caída de 5% a 15% durante 2 a 4 semanas, que «se recupera por completo» | La vende la plataforma de destino, sin método |

Las cifras de quien vende la mudanza son las más optimistas, y los únicos estudios con datos tratan otro caso, el cambio de dominio. Según ellos, alrededor de 14% a 17% de los sitios no vuelve a su tráfico a unos tres años. Para una tienda que cambia de plataforma y conserva el dominio no se encontró un dato. Google tampoco promete plazos: John Mueller dijo en 2026 que "sometimes things just take a particularly long time to be fully processed".

Que las redirecciones conserven el posicionamiento es una creencia más fuerte que lo que dice Google: los 301 no pierden PageRank, pero Google no dice que se conserven las posiciones, y las causas de caída que listan los practicantes incluyen los cambios de contenido, de títulos y de enlaces internos.

## Qué suele salir mal

Las causas que listan StudioHawk y Ahrefs se repiten:

- redirecciones que faltan, temporales (302) en vez de permanentes, en cadena o hacia páginas que no corresponden;
- el bloqueo de indexación de la tienda de prueba que queda puesto en la tienda nueva;
- etiquetas canónicas que siguen apuntando a las URL viejas;
- contenido que se pierde en el camino: títulos, descripciones, textos de las imágenes, el blog;
- la tienda nueva, más lenta;
- direcciones cambiadas sin necesidad, y el SEO consultado tarde.

Antes de declarar un desastre, Sitebulb recomienda comparar la caída contra lo que se esperaba sin mudanza: sin esa línea de base, cualquier baja parece la mudanza (según el resumen de su guía). Las caídas por temporada no son de la mudanza.

> [!NOTE] Sin fuente todavía: casos documentados de mudanzas fallidas de tiendas pyme argentinas, incluidas las que salieron de Mercado Shops; qué pasa con suscripciones y tarjetas guardadas; cuánto cobra por una mudanza quien presta el servicio en Argentina.

## Dónde entra en un servicio

Mudar es la puerta de entrada de un servicio de implementación: el comercio llega con una tienda que ya existe, y el trabajo es pasarla sin cortar las ventas. Productos y clientes los puede pasar el comercio solo, con las apps de la plataforma de destino (la de Shopify es gratis). Lo que se vende es lo que no pasa solo: pedidos, contraseñas, redirecciones, integraciones.

No se encontró una tasa de mudanzas para comercios pyme ni para Argentina. El único dato medido es de BigCommerce: 551 tiendas perdidas en 90 días (hasta julio de 2025) sobre 41.221, alrededor de 1,3% por trimestre (cálculo propio sobre datos de Store Leads). Un cierre sí produce una ola de mudanzas, como el de Mercado Shops (ver [Mercado Libre](mercado-libre.md#cierre-de-mercado-shops)); Tiendanube se contradice sobre la fecha: en el mismo artículo dice que cerró a fines de 2025 y que sigue activo hasta el 31-dic-2026.

Para medir el antes y el después en ventas, el [embudo de conversión](../Checkout-y-conversion/embudo-de-conversion.md). Si se cobra a precio cerrado, el inventario del paso 1 es lo que permite estimar: ver [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md). Después de la mudanza, lo que sigue es el [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md), y el posicionamiento se sigue cada mes como dice [SEO de una tienda](seo-de-una-tienda.md#qué-se-revisa-cada-mes). Shopify manda las mudanzas complejas a sus socios (según el resumen de su página) y les prohíbe salir a buscar a sus comercios para llevárselos: cómo funciona eso está en [socios de una plataforma](socios-de-una-plataforma.md).

El recurso canónico para el proceso es la guía de Google [Site move with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes): fijate en el mapa de URL, en el año de redirecciones y en la regla de no mandar todo a la portada. Para el caso argentino, la [guía de Tiendanube para venir desde Shopify](https://ayuda.tiendanube.com/es_AR/primeros-pasos/como-migrar-mi-tienda-online-de-shopify-a-tiendanube) dice qué no pasa, pero no trata las redirecciones.
