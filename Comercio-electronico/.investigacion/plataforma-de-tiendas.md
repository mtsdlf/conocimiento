# Investigación: Plataforma-de-tiendas (2026-11-22)

Fecha de consulta de todo lo volátil: 2026-11-22. Marcas: [L] texto completo leído (vía WebFetch, que devuelve un resumen del modelo sobre la página; las citas literales vienen de ahí), [M] metadatos o abstract, [S] resumen del buscador o secundario. Puntajes 1-3 (autoridad / profundidad / ejemplos / unicidad).

Límites de esta pasada: se agotó el presupuesto de búsquedas web de la sesión (200). Varias páginas dieron 403/404/ECONNRESET. Lo que no se pudo leer figura en "Huecos". El 10-K de Shopify y el 20-F de VTEX se leyeron por tramos (WebFetch solo cubre 100.000 caracteres por llamada); del 10-K quedaron sin leer los primeros 100.000 en parte y el último tramo.

## 0. Divergencias con el árbol del ALCANCE

- "Scalafy" no se encontró como plataforma de tiendas (ver sección 6). Lo que existe con nombre casi igual es **Escalafy**, una herramienta de analítica de ganancias, no una plataforma. Se declara abajo y no se inventa ficha de plataforma.
- Las "fichas" quedaron en dos grupos: las que tienen presencia medida en Argentina (sección 5) y las globales del pedido original.
- GPV y "attach rate de pagos": el 10-K de Shopify FY2025 no usa "GPV" en lo leído; usa "penetration rate" de Shopify Payments (65,6%). Eso es lo más cercano al attach rate.

## 1. tipos-de-plataforma

### Fuentes
| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| MACH Alliance (nota de prensa de commercetools, 2020) | https://commercetools.com/press-releases/mach-alliance-forms-to-empower-enterprises-taking-advantage-of-modern-saas-technology | primaria (de un fundador, con interés) | 2/2/1/2 | [S] solo el resultado del buscador, no abrí la página |
| MACH Alliance (Wikipedia) | https://en.wikipedia.org/wiki/MACH_Alliance | secundaria | 1/2/1/1 | [S] |
| Sitio MACH Alliance | https://machalliance.org/the-alliance | primaria | 2/1/1/2 | [S] |
| WooCommerce, About | https://woocommerce.com/about/ | primaria | 3/2/1/3 | [L] |
| Shopify, Liquid | https://shopify.dev/docs/api/liquid | primaria | 3/2/2/3 | [L] |

### Afirmaciones
- Alojada (SaaS) vs código abierto autoalojada: WooCommerce se define como "the flexible, Open Source commerce solution built on WordPress", núcleo gratuito (https://woocommerce.com/about/). VTEX se describe como SaaS (20-F, sección 5). En SaaS el proveedor aloja y opera; en autoalojada el comercio (o su agencia) aloja, actualiza y asegura. Esta distinción es de definición común; no hay una fuente primaria única que la fije [S, mía].
- Marketplace: el comercio vende dentro del sitio de un tercero (Mercado Libre; ficha en sección 5). Definición [S, mía]; falta fuente académica (Laudon & Traver, ver Huecos).
- MACH = microservices, API-first, cloud-native, headless. Es una organización sin fines de lucro (501(c)(3)) lanzada en junio de 2020; su propia nota de prensa nombra como fundadores a commercetools, Contentstack, EPAM Systems y Valtech; otras fuentes listan diez miembros iniciales (Algolia, Amplience, Cloudinary, Constructor.io, Contentful, E2X, Fluent Commerce, Frontastic, Mobify, Vue Storefront). 111 miembros a septiembre de 2025 (https://en.wikipedia.org/wiki/MACH_Alliance, [S]). Quienes la impulsan son proveedores que venden componentes de ese tipo: conflicto de interés evidente.
- Crítica: la única que traje es del lado de un proveedor de otro modelo, Shopify Enterprise ("disadvantages microservices", https://www.shopify.com/enterprise/disadvantages-microservices, apareció en una búsqueda, [S], no la abrí). No encontré crítica independiente (académica o de consultora neutral). Hueco.
- Costos y ventajas por tipo: no hay una fuente primaria neutral que los compare; se pueden armar de las fichas (cobro, quién opera). No lo redacto como hecho.

### Recurso canónico
No hay uno confiable aún. Candidato provisional: sitio de la MACH Alliance para la definición literal (fijarse en los principios de certificación), leído con la salvedad de que es un lobby de proveedores. Para el concepto de plataforma alojada vs abierta, Laudon & Traver (parte de infraestructura) sin verificar.

## 2. arquitectura-de-plataforma

### Fuentes
| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| Shopify, versionado de API | https://shopify.dev/docs/api/usage/versioning | primaria | 3/2/2/3 | [L] |
| Shopify, Liquid | https://shopify.dev/docs/api/liquid | primaria | 3/2/2/3 | [L] |
| Shopify, blog multi-tenant | https://www.shopify.com/blog/multi-tenant-architecture | primaria (marketing) | 2/1/1/2 | [S] del vistazo |
| SREcon16 Europe, Weingarten | https://usenix.org/conference/srecon16europe/program/presentation/weingarten | primaria (charla) | 3/2/2/3 | [M] del vistazo |
| Blog de ingeniería de Shopify (pods) | https://shopify.engineering/blogs/engineering/shard-balancing-moving-shops-confidently-with-zero-downtime-at-terabyte-scale | primaria | ?/?/?/? | NO leído: 404 en engineering.shopify.com; la redirección a shopify.engineering no devolvió contenido. Hueco |
| Docs de desarrolladores Tiendanube | https://developers.tiendanube.com/docs/ | primaria | ?/?/?/? | NO leído (error de red) |
| Adobe Commerce developer | https://developer.adobe.com/commerce/ | primaria | 3/1/1/3 | [L] |

### Afirmaciones
- Versionado: "Shopify releases a new API version every three months at 5pm UTC on the first day of the quarter." Versiones con nombre de fecha (2026-04). "Each stable version is supported for a minimum of 12 months", con "at least nine months of overlap". Última estable al 2026-11-22: 2026-10 (https://shopify.dev/docs/api/usage/versioning). Esto cierra y precisa la frase del vistazo ("soporta un año"): es un mínimo de 12 meses.
- Liquid: "Liquid is a template language created by Shopify." Los temas usan una variante: "The variation of Liquid in this reference extends the open-source version of Liquid for use with Shopify themes." Notificaciones y Shopify Flow usan otras versiones (https://shopify.dev/docs/api/liquid).
- Multi-tenant, pods, SREcon 2016: solo en lo que dijo el vistazo (una instancia sirve a muchos clientes; espectro "share nothing"/"share everything"; podding multi-datacenter 2016). No pude leer el blog de ingeniería, así que "pod" como unidad de aislamiento queda sin fuente primaria leída. Hueco.
- Admin API (GraphQL, REST legacy), Storefront API, Hydrogen, Functions, webhooks: solo del vistazo ([M]). Verificar en https://shopify.dev/docs/api.
- Adobe Commerce: la página dice dar "software, tools, and services to customize and extend Adobe Commerce", "API-first Commerce", y menciona "Commerce as a Cloud Service" (https://developer.adobe.com/commerce/). No nombra REST/GraphQL ni marketplace en esa página.
- Equivalente Tiendanube: no verificado (docs no abrieron). Por el plan Impulso se sabe que da "acceso al código fuente" del tema (https://www.tiendanube.com/planes-y-precios). Hueco para API, webhooks, lenguaje de temas.

### Recurso canónico
- shopify.dev/docs/api/usage/versioning: leer la tabla de versiones y la política de deprecación (fijarse en cuántos meses hay para migrar).
- Charla SREcon16 de Weingarten: la fuente primaria más temprana de la arquitectura de aislamiento; mirar el video/diapositivas, no solo el abstract.

## 3. negocio-de-una-plataforma

### Fuentes
| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| Shopify 10-K FY2025 | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm | primaria | 3/3/2/3 | [L] parcial (tres tramos; ver abajo) |
| VTEX 20-F FY2025 (presentado 2026-02-26) | https://www.sec.gov/Archives/edgar/data/1793663/000119312526076504/ck0001793663-20251231.htm | primaria | 3/3/2/3 | [L] parcial |
| Tiendanube, Quiénes somos | https://www.tiendanube.com/compania | primaria (empresa) | 2/1/1/3 | [L] |
| Yespress / empresa (ventas 2025 de Nuvemshop) | https://yespress.io/nuvemshop | secundaria | 1/1/1/1 | [S] |
| Ámbito, 20-oct-2025 | https://www.ambito.com/negocios/tiendanube-acelera-inteligencia-artificial-y-apunta-al-millon-marcas-latinoamerica-n6198958 | secundaria | 2/1/1/1 | [S] |
| Bloomberg Línea, Nuvemshop y marcas medianas | https://www.bloomberglinea.com.br/startups/nuvemshop-cresceu-com-foco-nos-pequenos-negocios-marcas-medias-entraram-na-mira/ | secundaria | 2/2/2/1 | [S], sin fecha visible |
| StoreLeads Tiendanube | https://storeleads.app/reports/tiendanube | terciaria (estimación) | 1/1/1/2 | [L] |

### Cifras literales del 10-K de Shopify FY2025 (cierre 31-dic-2025), US$ millones
(Los números de la tabla y del GMV/MRR/penetración salieron de una lectura del tramo MD&A; las definiciones de GMV y de ingresos, del Item 1.)

| | 2025 | 2024 | 2023 |
|---|---|---|---|
| Subscription solutions | 2.752 (+17%, 24% del total) | 2.350 (+28%, 26%) | 1.837 (26%) |
| Merchant solutions | 8.804 (+35%, 76%) | 6.530 (+25%, 74%) | 5.223 (74%) |
| Total ingresos | 11.556 (+30%) | 8.880 (+26%) | 7.060 |
| GMV | 378.441 (+29%) | 292.275 (+24%) | |
| MRR al 31-dic | 205 (+15%) | 178 | 144 |
| GMV vía Shopify Payments | 248,1 mil M (+37%, +67,2 mil M) | 181,0 mil M | |
| Penetración de Shopify Payments | 65,6% | 61,9% | |

- Verificado contra el vistazo: todas sus cifras (2.752/2.350; GMV 378,44/292,27; MRR 205/178) coinciden. Merchant Solutions "US$ 8.800 millones" del vistazo era 8.804 (+35%, 76%): coincide. Nuevo respecto del vistazo: la penetración de pagos y el GMV vía Payments.
- Definiciones literales: "GMV is the total dollar value of orders facilitated through our platform"; "GMV does not represent revenue earned by us." "MRR is the aggregate value of all subscription plans, excluding variable platform fees". "Our merchant solutions revenues are directionally correlated with the level of GMV". Merchant solutions viene sobre todo de "payment processing fees and currency conversion fees" de Shopify Payments, más préstamos, comisiones de referidos y "the sale of shipping labels". Subscription incluye suscripciones, cargos variables de plataforma, POS Pro, apps, dominios y temas.
- Alcance: "millions of merchants from more than 175 countries"; base de comerciantes 44% EE.UU., 31% EMEA, 16% APAC/Australia/China, 5% Canadá, 5% América Latina (todo al 31-dic-2025). "No single merchant has ever represented more than five percent of our total revenues".
- Plus: "offered at a starting rate that is several times that of our standard Shopify plans"; parte del crecimiento de suscripciones viene de "higher priced plans, such as Plus".
- Shopify Capital: aparece en riesgos como "loans and merchant cash advances"; no obtuve el monto de originación. Hueco.

### Cómo se calcula (cálculo mío sobre las cifras de arriba)
- Take rate de merchant solutions = 8.804 / 378.441 = 2,33% del GMV (2025). Con 2024: 6.530 / 292.275 = 2,23%.
- Take rate total (todos los ingresos) = 11.556 / 378.441 = 3,05%.
- Aclaración: Shopify no publica "take rate" con ese nombre en lo leído; es una razón derivada. El numerador incluye cosas que no son comisión por pago (préstamos, etiquetas), así que no es el costo que paga un comercio.
- Attach rate de pagos: lo más cercano publicado es la "penetration rate" de Shopify Payments, 65,6% del GMV (no es la proporción de comerciantes, es proporción del GMV). Por región al 31-dic-2025: Norteamérica 88%, APAC 89%, EMEA 83%.

### VTEX 20-F FY2025 (US$)
- Ingresos 2025: US$ 240,5 millones (+6,1% desde 226,7). Ingresos por suscripción: 97,7% del total en 2025 y 96,0% en 2024. GMV de clientes en la plataforma: US$ 20,5 mil millones (2025) y 18,2 mil millones (2024). "approximately 2,200 customers with 3,100 active online stores across 44 countries". Fundada en 2000 por Geraldo do Carmo Thomaz Júnior y Mariano Gomide de Faria; la holding se constituyó en Islas Caimán el 25-jul-2018.
- Modelo de cobro: planes con "a fixed fee component and a revenue-sharing component based on a percentage of our customers' GMV", contratos de 12 a 36 meses.
- Razón derivada mía: 0,977 x 240,5 / 20.500 = 1,15% del GMV. Aproximada (usa el 97,7% redondeado) y mezcla cargos fijos.

### Tiendanube / Nuvemshop (datos de la propia empresa y de prensa)
- Empresa (https://www.tiendanube.com/compania, consultado 2026-11-22): "180,000+" tiendas activas, más de US$ 2.000 millones de ventas anuales en LatAm (sin año explícito), más de 1.500 empleados. Rondas que lista: 2011 US$ 300 mil (ángeles); 2013 US$ 600 mil (Trindade); 2017 US$ 7 M (Elevar Equity); 2020 US$ 30 M (Qualcomm Ventures y Kaszek); 2021 US$ 89 M (Accel); 2021 US$ 500 M serie E (Insight Partners y Tiger Global), con valuación escrita "USD 3,1 billones" (probable US$ 3.100 millones; es la redacción de la página).
- Prensa/empresa: ventas de las tiendas superiores a R$ 6.500 millones en 2025 (+35%) y 12 millones de compradores únicos (https://yespress.io/nuvemshop, [S], 1 fuente comercial); la fecha y base no están confirmadas.
- Bloomberg Línea (fecha no visible): el nivel Nuvemshop Next (~2.000 clientes) = 35% del GMV y Nuvem Pago procesa 60% del GMV. Puede estar desactualizado, [S].
- Discrepancia de conteo de tiendas: empresa 180.000+ activas; StoreLeads 204.631 tiendas vivas en 3T 2026 y 155.499 en 3T 2025 (según el buscador, [S]). Métodos distintos (activas según la empresa, vivas detectadas por rastreo).
- No hay GMV oficial publicado por Tiendanube en lo hallado. Hueco.

### Recurso canónico
- 10-K de Shopify, Item 7 (MD&A, "Key Performance Indicators") e Item 1 (definiciones): leer las definiciones de GMV, MRR y la nota de penetración de pagos; fijarse en que "GMV does not represent revenue".
- 20-F de VTEX: para ver un modelo de cobro por suscripción con porcentaje del GMV, distinto del de Shopify.

## 4. segmentos-de-comerciantes

### Fuentes
| Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|
| Shopify pricing | https://www.shopify.com/pricing | primaria | 3/2/2/3 | [L] |
| Tiendanube planes (ARS) | https://www.tiendanube.com/planes-y-precios | primaria | 3/2/2/3 | [L] |
| Shopify 10-K (Plus) | ver sección 3 | primaria | 3/2/1/3 | [L] parcial |

### Planes públicos (consultados 2026-11-22)
**Shopify (USD, página de EE.UU.)**: Basic US$ 25/mes (US$ 19/mes anual), tarifa de proveedor de pago externo 2%; Grow US$ 65 (US$ 49), 1%; Advanced US$ 399 (US$ 299), 0,6%; Plus "starts at $2,300/mo" (sin precio anual en la página), 0,2%. POS Pro US$ 89/mes por local; Plus "includes 20 locations". Promoción de entrada: prueba de 3 días y luego US$ 1/mes por 3 meses. "Pricing and payment options can differ depending on where your business is based". La página no mostró las tarifas de tarjeta. https://www.shopify.com/pricing

**Tiendanube (ARS, página es-AR)**: Inicial gratis; Esencial $27.999/mes ($20.999/mes anual, $251.991/año), 2% por otros medios de pago, Pago Nube desde 2,97% + IVA; Impulso $79.999 ($59.999; $719.991/año), 1%, Pago Nube desde 2,85% + IVA; Escala $244.999 ($183.749; $2.204.991/año), 0,7%, desde 2,65% + IVA; Evolución a consultar (negociable). Inicial: Pago Nube desde 2,99% + IVA. Descuento anual 25%. "Sin límites de productos, ventas y visitas". Impulso suma WhatsApp y "acceso al código fuente"; Escala suma estadísticas avanzadas y hasta 3 centros de distribución; Evolución suma soporte prioritario, especialista dedicado y migración asistida. La página tiene un dato estructurado que da Evolución a "0", contradice el texto visible. https://www.tiendanube.com/planes-y-precios

### Cómo se mapea (lectura de la estructura de planes, no clasificación oficial)
- Emprendedor: planes de entrada (Shopify Basic, Tiendanube Inicial/Esencial).
- Pyme: planes medios (Grow, Impulso).
- Mediana: planes altos (Advanced, Escala) y "Next" de Nuvemshop (Bloomberg Línea, [S]).
- Grande: Shopify Plus (US$ 2.300+/mes), Tiendanube Evolución (a consultar), VTEX (sólo por contacto).
- Ninguna plataforma lee oficialmente "emprendedor/pyme/mediana": son los nombres de planes. La clasificación por facturación o empleados no la hallé en una fuente. Hueco.

### Recurso canónico
Las dos páginas de planes, tomadas el mismo día: fijarse en la tarifa de transacción por usar pasarela propia vs externa, que es donde se ve el incentivo de la plataforma.

## 5. Presencia en Argentina (cuotas y conteos)

El pedido de la coordinación: establecer con datos quiénes están en Argentina antes de las fichas. No hay un informe de cámara (CACE) ni consultora con cuota por plataforma que haya podido abrir; solo rastreadores técnicos, que miden sitios detectados, no ventas. Todos con método distinto.

### Tabla A: StoreLeads, tiendas vivas en Argentina, página actualizada 2026-11-13 [L]
Método: StoreLeads no describe cómo cuenta por país en lo leído; sí dice que las fechas de creación son estimadas con una heurística que incluye DNS histórico. Terciaria, 1/1/1/2.

| Plataforma | Tiendas vivas en Argentina | URL |
|---|---|---|
| Tiendanube | 59.214 (28,3% de sus tiendas globales) | https://storeleads.app/reports/tiendanube/AR/top-stores |
| WooCommerce | 24.711 | https://storeleads.app/reports/woocommerce/AR/top-stores |
| Shopify | 9.059 (el total global mostrado es 3.298.869) | https://storeleads.app/reports/shopify/AR/top-stores |
| Empretienda | 5.802 (86,9% de 6.675) | https://storeleads.app/reports/empretienda |
| Wix | 2.803 | https://storeleads.app/reports/wix/AR/top-stores |
| PrestaShop | 658 (707 en 3T) | https://storeleads.app/reports/prestashop/AR/top-stores |
| VTEX | 438 | https://storeleads.app/reports/vtex/AR/top-stores |
| Ecwid | 363 | https://storeleads.app/reports/ecwid/AR/top-stores |
| Magento | 332 (pico 568 en 3T 2023; 346 en 3T 2026 vs 474 un año antes) | https://storeleads.app/reports/magento/AR/top-stores |
| BigCommerce | 13 | https://storeleads.app/reports/bigcommerce/AR/top-stores |
| Squarespace | 12 | https://storeleads.app/reports/squarespace/AR/top-stores |
| Jumpseller | 64 (0,8% de 8.248 globales; cálculo mío) | https://storeleads.app/reports/jumpseller |
| Fenicio | 1 (probablemente subdetección: no es creíble que sea todo lo que hay; no verificado) | https://storeleads.app/reports/fenicio/AR/top-stores |
| Mercado Shops, Tiendup | sin dato: la URL devolvió 404 | |

Con esas cifras (suma mía de las 12 con dato, sin Fenicio: 59.214+24.711+9.059+5.802+2.803+658+438+363+332+64+13+12 = 103.469), Tiendanube sería 57%, WooCommerce 24%, Shopify 9%. Es una suma de las plataformas que consulté, no el total de tiendas en Argentina: faltan Mercado Shops, Tiendup, desarrollos a medida y otras.

### Tabla B: otros rastreadores [S], del buscador, no abrí las páginas (403)
| Fuente | Medida | Dato | Fecha |
|---|---|---|---|
| WMTips https://www.wmtips.com/technologies/e-commerce/country/ar/ | cuota de sitios detectados | WooCommerce 42,5%, Tiendanube 25,5%, VTEX 5,1% | 2026 (sin día) |
| AfterShip https://www.aftership.com/ecommerce/statistics/regions/ar | cuota por cantidad de tiendas | Tiendanube 29,36 mil tiendas (35,08%), WooCommerce 24,05 mil (28,75%) | 2026 (sin día) |
| StoreLeads, WooCommerce AR (versión vieja) | tiendas vivas | 25.900 (-2% interanual en 1T 2025) | jun-2025 |
| StoreLeads, usuarios de Klaviyo en AR | proporción entre quienes usan Klaviyo | Shopify ~74%, Tiendanube 16,5%, WooCommerce 7,9% | mar-2026 |

### Discrepancias que conservar
- Líder: WMTips pone a WooCommerce primero (42,5% vs 25,5% de Tiendanube); AfterShip y StoreLeads (59.214 vs 24.711) ponen a Tiendanube primero. Medidas y métodos distintos (sitios detectados vs tiendas vivas).
- Tiendanube Argentina: AfterShip 29,36 mil vs StoreLeads 59.214. Diferencia de ~2x sin explicación hallada; StoreLeads global de Tiendanube 204.631 (3T 2026) vs la empresa "180.000+".
- Shopify entre quienes usan Klaviyo domina (74%), pero en tiendas vivas totales es la tercera: la muestra de una herramienta de email marketing sesga hacia tiendas más grandes.
- BuiltWith (julio 2025): unas 1.183 detecciones de temas de Shopify en Argentina, valor distinto de los 9.059 de StoreLeads (mide temas, no tiendas) [S].

### Dónde presencia confirmada
Con presencia real en Argentina: Tiendanube, WooCommerce, Shopify, Empretienda, Wix, VTEX (tiene filial en Argentina, 20-F). Presencia marginal (cientos de tiendas): PrestaShop, Ecwid, Magento. Prácticamente nula en datos: BigCommerce, Squarespace, Jumpseller, Fenicio (dato dudoso). Mercado Libre: marketplace, fuera de esta medición.

## 6. Scalafy y análogas

- **Scalafy**: ninguna búsqueda devolvió una plataforma de tiendas con ese nombre. Búsqueda "Scalafy ecommerce": 0 resultados con el nombre. `https://scalafy.com` redirige (302) a una página de venta de dominios (grandname.com), que devolvió 403; es decir, el dominio parece estar a la venta, pero no pude abrir la página para confirmarlo. Conclusión: no hay información confiable sobre un producto llamado Scalafy. Hay que pedirle a quien lo mencionó el enlace o el país.
- **Escalafy** (¿posible error de tipeo?): según el buscador [S]: aplicación de analítica de rentabilidad y flujo de caja para e-commerce de LatAm, lanzada en la tienda de apps de Shopify el 6-oct-2025 (https://apps.shopify.com/escalafy), con integraciones a Tiendanube, Shopify, Mercado Libre y a gasto en Meta/Google/TikTok; planes de US$ 19 (Growth), US$ 49 (Scale), US$ 99 (Pro) más uno gratis según Capterra (https://www.capterra.com/p/10034658/Escalafy/); la ficha de Shopify dice "+3.000 marcas en LatAm" y su sitio inglés 9.099 marcas conectadas (https://www.escalafy.com/en): discrepancia. No es una plataforma de tiendas: es una app del ecosistema de Tiendanube/Shopify (https://www.tiendanube.com/mx/tienda-aplicaciones-nube/escalafy).
- Si el producto buscado es una plataforma de tiendas, las análogas por función con presencia medida en Argentina son Empretienda, Wix, PrestaShop, Ecwid y Jumpseller. Si es una herramienta que se apoya en las plataformas, son las apps de la tienda de aplicaciones de Tiendanube y Shopify. No puedo decidir cuál es "Scalafy" sin el dato; las fichas abajo están marcadas por esa distinción.

## 7. Fichas (datos públicos fechados, consulta 2026-11-22; sin opinión ni comparación)

### Shopify
- Qué es / tipo: plataforma alojada (SaaS). Origen: Canadá [no verificado en esta pasada, solo conocimiento general; fuente pendiente].
- Mercados: "millones de comerciantes en más de 175 países"; 5% de los comerciantes en América Latina (10-K, 31-dic-2025).
- Cobro: suscripción mensual + soluciones para comerciantes (pagos, conversión de moneda, préstamos, etiquetas de envío); ver tabla de planes en sección 4 (página EE.UU., 2026-11-22). https://www.shopify.com/pricing
- Métricas (10-K FY2025): ingresos US$ 11.556 M; GMV US$ 378.441 M; MRR US$ 205 M; penetración de Payments 65,6%. https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm
- Ecosistema: APIs versionadas cada trimestre, soporte mínimo 12 meses (https://shopify.dev/docs/api/usage/versioning); Liquid (https://shopify.dev/docs/api/liquid). Tienda de apps: https://apps.shopify.com (existencia vista; no medida).
- Argentina: 9.059 tiendas vivas (StoreLeads, 2026-11-13). No verifiqué si Shopify Payments opera en Argentina: el 10-K leído no lo dice.

### Tiendanube / Nuvemshop
- Qué es / tipo: plataforma alojada (SaaS) con pasarela propia (Pago Nube). Origen: Buenos Aires, Argentina, fundada en 2011 (aceptada en la incubadora Baitec de la Ciudad por 12 meses en 2011).
- Mercados: Argentina, Brasil (2012, como Nuvemshop), México (2020), Colombia y Chile (2023). Fuente: https://www.tiendanube.com/compania
- Cobro y planes: ver sección 4 (ARS, 2026-11-22).
- Métricas: 180.000+ tiendas activas, más de US$ 2.000 M de ventas anuales, 1.500+ empleados (página de la empresa, 2026-11-22); R$ 6.500 M en 2025 y 12 millones de compradores (Yespress, [S]); valuación US$ 3.100 M en 2021 (página de la empresa). StoreLeads: 59.214 tiendas en Argentina y 28,3% del total (2026-11-13).
- Ecosistema: tienda de aplicaciones (https://www.tiendanube.com/mx/tienda-aplicaciones-nube); API en https://developers.tiendanube.com/docs/ (no leída).

### WooCommerce
- Qué es / tipo: plugin de código abierto sobre WordPress, autoalojado. Origen: WooThemes (2008), plugin WooCommerce lanzado en 2011, adquirido por Automattic en 2015. https://woocommerce.com/about/
- Cobro: el núcleo es gratis (la misma página); costos de hosting, extensiones y pasarela no se midieron.
- Métricas: "seven million downloads" en 2014 (dato viejo). StoreLeads: 24.711 tiendas vivas en Argentina (2026-11-13). No hay conteo global actual leído.
- Ecosistema: extensiones; no verificado en esta pasada.

### Adobe Commerce (Magento)
- Qué es: plataforma de comercio de Adobe, "API-first", con "Commerce as a Cloud Service" (https://developer.adobe.com/commerce/, [L]). Magento Open Source: no mencionado en esa página. Origen, licencias, precios: no verificado.
- Argentina: 332 tiendas (StoreLeads 2026-11-13), en baja (pico 568 en 3T 2023).

### VTEX
- Qué es / tipo: plataforma de comercio SaaS, Cayman, cotiza en NYSE; fundada en 2000 (Brasil implícito por los fundadores; el 20-F lo describe con subsidiarias "mostly located in Brazil, Argentina and Colombia"). Mercados: 44 países, 2.200 clientes, 3.100 tiendas activas.
- Cobro: cargo fijo + porcentaje del GMV, contratos de 12 a 36 meses; precios por contacto (https://www.vtex.com/en-us/pricing/ no publica planes).
- Métricas FY2025: ingresos US$ 240,5 M; GMV de clientes US$ 20,5 mil M. https://www.sec.gov/Archives/edgar/data/1793663/000119312526076504/ck0001793663-20251231.htm
- Argentina: filial local; 438 tiendas (StoreLeads), 5,1% de los sitios detectados según WMTips ([S]).

### Mercado Libre (marketplace) y Mercado Shops
- Mercado Libre como marketplace: no se pudo leer la página de tarifas (403) ni su 10-K. Ficha vacía por ahora.
- Qué pasó con Mercado Shops: no verificado. Las páginas de ayuda y de desarrolladores devolvieron 403 y no tengo búsquedas disponibles. Hueco declarado; no afirmo si fue cerrado.

### Empretienda
- Qué es: plataforma de tiendas, concentrada en Argentina (86,9% de sus 6.675 tiendas vivas están en el país, StoreLeads 2026-11-13). Planes y origen: no leídos (error de conexión al sitio). Análoga a Tiendanube por función.

### Wix eCommerce
- Qué es: constructor de sitios con tienda. Wix describe su oferta como "launch a professional eCommerce store powered by AI". Planes Core, Business y Business Elite con límites (50 GB/100 GB/ilimitado; 25/250/50.000 productos de dropshipping; 5/10/100 colaboradores); "you need a paid plan to accept payments"; precios no mostrados en la página (https://www.wix.com/ecommerce/online-store, 2026-11-22). Argentina: 2.803 tiendas (StoreLeads).

### PrestaShop, Ecwid, Jumpseller, Squarespace, Fenicio, Tiendup
- Solo el conteo de StoreLeads de la tabla A. Jumpseller: "all-in-one platform", copyright 2010-2026, prueba de 7 días sin tarjeta, planes no listados en su home (https://jumpseller.com). Nada más verificado: sin origen, precios ni métricas. Tiendup no tiene dato.

## 8. Huecos
1. Mercado Libre y Mercado Shops: sin dato leído; falta qué pasó con Mercado Shops, tarifas y métricas del 10-K.
2. Origen de Shopify, WooCommerce licencia (GPL), precios de WooCommerce y Adobe Commerce, Magento Open Source: sin fuente primaria leída.
3. Blog de ingeniería de Shopify (pods): sin leer. Crítica independiente a MACH: no hallada. Documentación para desarrolladores de Tiendanube: no leída.
4. Shopify Capital: monto no obtenido; disponibilidad de Shopify Payments en Argentina: no verificada.
5. Planes públicos de Empretienda, Jumpseller, PrestaShop, Ecwid, Fenicio, Tiendup, Wix (precios): sin leer. WMTips y AfterShip dieron 403: se citan por el buscador.
6. Cuota de mercado en Argentina por una cámara (CACE) o consultora: no hallada; solo rastreadores técnicos con métodos distintos.
7. Scalafy: ver sección 6; falta el enlace o país de origen de quien lo mencionó.
8. 10-K de Shopify: leí por tramos y no el documento completo (los primeros 100.000 caracteres solo para el Item 1; el último tramo no). 20-F de VTEX: tramos 100.000-300.000.
9. Presupuesto de búsquedas web agotado en la sesión; el resto de rondas por componente no se hizo.
