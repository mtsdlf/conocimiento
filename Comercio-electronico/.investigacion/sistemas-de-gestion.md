# Sistemas de gestión (ERP para pymes) e integración con tiendas y marketplaces, Argentina

Fecha de consulta de todo: 2026-11-22. Investigación para la base pública de comercio electrónico.

## Cómo leer las marcas

- Marca de lectura: **[L]** leí el texto completo que devolvió el navegador (`leer-pagina.mjs`); **[M]** solo metadatos; **[S]** resumen: o bien un buscador, o bien un extractor automático (WebFetch, que lee la página y devuelve un resumen a una pregunta mía). Todo lo que pasó por WebFetch lo marco [S], porque no vi el texto crudo.
- Calificación de la fuente A-F y del dato 1-6, como en el encargo. Un dato con una sola fuente nunca pasa de 2-3 (el 1 exige otra fuente que lo confirme).
- Búsqueda: el presupuesto de WebSearch de la sesión se agotó a mitad del trabajo. Por eso quedaron sin cubrir el recurso conceptual (Laudon) y varias fichas. Está declarado en Huecos.
- Las páginas de developers.mercadolibre.* devolvieron 403 tanto con WebFetch como con el navegador real. **No pude abrir la documentación oficial de Mercado Libre.** Lo que sigue sobre sus tokens viene de resúmenes de buscador y va marcado así.

## Sobre la división del árbol

La división propuesta (qué es un ERP / cómo se integra / fichas) funciona, pero el campo mezcla dos cosas que conviene separar en la base:

1. **Facturador, sistema contable, ERP/gestión, POS y conector** no son categorías limpias. Los productos reales se montan sobre varias a la vez (Contabilium y Dux venden gestión + POS + conector a tiendas; Colppy y Xubio nacieron contables y se extienden a gestión; Tango Factura/TFactura y TusFacturasAPP son facturadores que crecen hacia stock y cobranzas; Alegra se autodefine "Software de Gestión", y dice que difiere del ERP por alcance). Propongo clasificar por **qué es la fuente de verdad de qué** (comprobantes, stock, contabilidad, cobranza) y no por la etiqueta comercial.
2. **Las fichas envejecen mucho más rápido** (los precios cambian por mes, hay promociones como CYBER) que los conceptos y la mecánica de integración. Conviene que las fichas vivan aparte, fechadas, y que el concepto no cite precios.
3. Los grandes en Argentina se organizan por **canal de venta indirecto** (Tango: "200 centros de servicio"): el precio público de Tango casi no existe y eso es un rasgo del mercado, no un hueco de la investigación.

---

## Componente 1. Qué es un sistema de gestión / ERP para pyme

### Fuentes

| # | Fuente | URL | Tipo | Aut. | Prof. | Ejem. | Unic. | Marca |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Alegra Argentina, home (FAQ "¿Qué diferencia hay entre ERP y Software de Gestión?", "¿Qué tipos existen?") | https://www.alegra.com/argentina/ | primaria (el fabricante hablando de sí y de la categoría) | 1 | 1 | 1 | 1 | [L] |
| 1.2 | Develop Argentina, "sistemas de gestión comercial Argentina 2026", 25-jun-2026 | https://www.developargentina.com/blog/sistemas-gestion-comercial-argentina-2026 | secundaria (el autor vende desarrollo a medida; lo dice el extractor, no yo) | 1 | 2 | 1 | 1 | [S] |
| 1.3 | SpomBridge, "Mejor ERP para pymes en Argentina (2026)", actualizado 15-oct-2026 | https://app.spomsolutions.com/blog/mejor-erp-pymes-argentina | secundaria con conflicto de interés (SpomBridge es una de las 8 opciones comparadas) | 1 | 2 | 1 | 1 | [S] |
| 1.4 | Laudon & Laudon, *Management Information Systems*, capítulo de aplicaciones/sistemas empresariales | no consultado | canónica propuesta | - | - | - | - | no leída |

### Afirmaciones

- Alegra define la diferencia así: "El ERP abarca todos los aspectos operativos y ofrecen una integración total, sin embargo, son más complejos, costosos y difíciles de escalar cuando la empresa crece. El Software de Gestión se centra en áreas específicas de la empresa, son más flexibles y fáciles de escalar". Es una definición de parte (vende lo segundo). https://www.alegra.com/argentina/ - fuente B, dato 3, [L].
- Tipos: "Los Software de Gestión pueden ser locales o basados en la nube. Los primeros, son tradicionales y requieren instalación en servidores internos"; los segundos "permiten gestionar operaciones desde cualquier lugar". https://www.alegra.com/argentina/ - fuente B, dato 3, [L].
- Axoft describe su oferta como un conjunto de productos por rol/rubro: Tango Gestión ("para PyMEs y grandes empresas"), Capital Humano, Punto de Venta ("para comercios minoristas, sucursales y/o franquicias"), Estudios Contables, Restô (gastronomía) y TFactura ("solución cloud para pequeñas empresas y emprendedores"). Es decir: generalista + verticales por rubro + facturador cloud en la misma casa. https://www.axoft.com/ - fuente B, dato 2, [L].
- Módulos típicos que un sistema nube para comercio declara (ejemplo Contabilium): facturación online, control de stock con listas de precios y depósitos, compras, tesorería (cajas, cheques, arqueos), y contabilidad en planes altos. https://www.contabilium.com/ar - fuente B, dato 2, [L]. Dux: "ventas, stock, facturación y cobranzas conectados en un solo lugar". https://www.duxsoftware.com.ar/ - fuente B, dato 2, [L].
- Cómo falla / cómo se elige: Develop Argentina señala como errores comunes "elegir solo por precio, decidir solo con el criterio del contador y subestimar la migración de datos" (paráfrasis del extractor; no tengo la cita literal). https://www.developargentina.com/blog/sistemas-gestion-comercial-argentina-2026 - fuente C (autor interesado), dato 4, [S]. Es la única fuente que encontré sobre fallas de implementación: **hueco fuerte**, no hay literatura independiente leída.
- Costo por unidad de uso: los planes se escalonan por comprobantes, usuarios y cuentas de canal (ver tabla de precios). Un modelo de cobro por volumen de comprobantes y por usuarios adicionales es verificable en las páginas de Dux, Contabilium, Xubio y Colppy. Fuente A para el precio de cada una, dato 2.
- Facturación electrónica: los sistemas se conectan a ARCA (ex AFIP) por web service. Contabilium publicó el 20-nov-2026 una nota "Facturá sin entrar a ARCA: cómo conectar tu sistema por web service". https://www.contabilium.com/ar - fuente B, dato 3, [L] (solo el título del blog).

### Recurso canónico propuesto

- **Laudon & Laudon, *Management Information Systems*, capítulo sobre aplicaciones empresariales** (sección "Enterprise systems"): qué es un sistema empresarial como base de datos única que integra funciones, y su costo de implementación y cambio organizacional. No pude abrirlo; lo propongo por conocimiento previo, y alguien debe verificar edición, capítulo y cita antes de escribirlo. Fijarse en: la idea de proceso de negocio de punta a punta, y el apartado de desafíos (costo, cambio de procesos, migración).
- Para el ámbito argentino: la página de Alegra como ejemplo de definición de parte, nunca como definición neutral.

---

## Componente 2. Integración con tiendas y marketplaces

### Fuentes

| # | Fuente | URL | Tipo | Aut. | Prof. | Ejem. | Unic. | Marca |
|---|---|---|---|---|---|---|---|---|
| 2.1 | Tiendanube API, autenticación | https://tiendanube.github.io/api-documentation/authentication | primaria | 3 | 2 | 2 | 3 | [S] |
| 2.2 | Tiendanube API, intro (rate limit) | https://tiendanube.github.io/api-documentation/intro | primaria | 3 | 2 | 2 | 3 | [S] |
| 2.3 | Shopify, rate limits | https://shopify.dev/docs/api/usage/rate-limits | primaria | 3 | 1 | 1 | 2 | [S] |
| 2.4 | Shopify, webhooks | https://shopify.dev/docs/apps/build/webhooks | primaria | 3 | 2 | 1 | 3 | [S] |
| 2.5 | WooCommerce REST API docs | https://woocommerce.github.io/woocommerce-rest-api-docs/ | primaria | 3 | 1 | 1 | 2 | [S] (leí solo el primer tercio; la sección de webhooks quedó sin leer) |
| 2.6 | Mercado Libre developers, autenticación y autorización | https://developers.mercadolibre.com.ar/es_ar/autenticacion-y-autorizacion | primaria, **inaccesible (403)** | - | - | - | - | no leída |
| 2.7 | Resúmenes de buscador sobre la doc de ML (varias páginas de developers.mercadolibre.* y global-selling) | https://developers.mercadolibre.com.ar/gestion-de-identidades-y-accesos-oauth-y-tokens | primaria, solo vista por resumen | 3 | 1 | 1 | 2 | [S] |
| 2.8 | Tiendanube, blog "Tango Factura" (actualizado 26-ene-2026) | https://www.tiendanube.com/blog/tango-factura/ | secundaria (la empresa de la tienda, no del ERP) | 2 | 2 | 2 | 2 | [S] |

### Afirmaciones

**Mercado Libre (todo [S], la doc oficial no se abrió).**
- El access token vale 6 horas: la respuesta de ejemplo trae `"expires_in": 21600`. Fuente B (primaria, vista por resumen), dato 2 (la misma cifra aparece en varias páginas del resumen, pero son copias de la misma doc: una fuente). https://developers.mercadolibre.com.ar/gestion-de-identidades-y-accesos-oauth-y-tokens
- El refresh token es de un solo uso: "We only allow using the last refresh token generated. Additionally, remember that the refresh token is single-use, and you will receive a new one with each token refresh process." (cita del resumen). Guardar el par nuevo en cada renovación; si dos procesos renuevan a la vez, uno queda con un token ya gastado. B, dato 2, [S].
- La doc recomienda renovar antes del vencimiento: "Before it expires (e.g.: at 5 hours), you refresh automatically. You save the new access_token and refresh_token" (cita del resumen). B, dato 2, [S].
- Duración del refresh token: **6 meses**, según el resumen de la búsqueda ("One Mercado Libre developer page says the refresh token expires after six months"). Un fragmento de la guía de Global Selling dice "get refresh token (new access_token which is valid for 6 months)", redactado de forma ambigua. Otra versión de la misma doc, en la respuesta de renovación, habla de "a new access token which is valid for 6 more hours". **Las dos redacciones conviven en los resultados; si el seis meses es fijo o se renueva con cada uso, no lo pude confirmar.** B, dato 4, [S].
- El refresh token solo se emite si la app tiene el permiso `offline_access`. B, dato 3, [S].
- Hay eventos que invalidan un access token antes de su vencimiento; la lista no apareció completa. B, dato 4, [S].
- Hay una nota de práctica (DEV Community, secundaria, 1 autor): "El refresh token de Mercado Libre es de un solo uso: cómo no desconectar a tus vendedores", https://dev.to/javiersivack/el-refresh-token-de-mercado-libre-es-de-un-solo-uso-como-no-desconectar-a-tus-vendedores-137g. Solo vi el título en la búsqueda. D, dato 5, [M].

**Tiendanube / Nuvemshop.**
- "Our access tokens don't expire. They become invalid only after you get a new one, or if the user uninstalls your app." No hay refresh token. https://tiendanube.github.io/api-documentation/authentication - A, dato 2, [S]. Contraste de diseño útil: Tiendanube no vence tokens, Mercado Libre sí.
- Límite: "the default bucket size is of 40 requests with a leaky rate of 2 requests per second"; "If the store is Next or Evolution (higher plans), the rate limit multiplies by 10"; "The rate limit works between each store and app." Cabeceras `x-rate-limit-limit`, `x-rate-limit-remaining`, `x-rate-limit-reset`. https://tiendanube.github.io/api-documentation/intro - A, dato 2, [S].
- Los webhooks "no se disparan" mientras el acceso a la API está suspendido por falta de pago; existen `app/suspended` y `app/resumed`. https://tiendanube.github.io/api-documentation/intro - A, dato 2, [S].
- Reintentos de webhooks de Tiendanube: no encontrado (la página de recurso webhook no se leyó). Hueco.

**Shopify.**
- "Most Shopify rate limits are enforced with a leaky bucket algorithm"; GraphQL Admin usa "Calculated query cost, by plan", REST Admin usa cubo por solicitudes. Backoff recomendado: "one second". https://shopify.dev/docs/api/usage/rate-limits - A, dato 2, [S]. Cifras por plan: no las obtuve.
- "Webhook delivery isn't always guaranteed"; recomienda "use reconciliation jobs to periodically fetch data from Shopify" e "ignore duplicate deliveries using `X-Shopify-Webhook-Id`". https://shopify.dev/docs/apps/build/webhooks - A, dato 2, [S]. Es la mejor base conceptual para explicar sobreventa y pedidos duplicados: el webhook puede perderse o repetirse, así que hace falta reconciliar y deduplicar.

**WooCommerce.**
- Autenticación REST: Basic Auth sobre HTTPS con Consumer Key y Consumer Secret; sin HTTPS, OAuth 1.0a de un solo paso con ventana de 15 minutos en el timestamp. https://woocommerce.github.io/woocommerce-rest-api-docs/ - A, dato 2, [S]. Webhooks, reintentos y desactivación tras fallos: no leídos.

**Conectores intermedios y quién manda.**
- Contabilium cobra por cuenta de canal integrada: Standard 3, Pro 4, Full 5; "MercadoLibre o Tiendanube adicional ($42.000)", WooCommerce $42.000, Shopify $55.000, todo + IVA. Dux limita por "tiendas online integradas" (1, 3, 4, 5) e incluye "Mercado Libre, Tienda Nube, WooCommerce, entre otras". https://contabilium.com/ar/planes [S]; https://www.duxsoftware.com.ar/precios [L]. A, dato 2.
- Tiendanube sobre Tango Factura: "permite facturar ventas de forma masiva, sincronizar precios y stock en la tienda, activar o pausar publicaciones según el stock, imprimir etiquetas de envío en lote y generar notas de crédito" (paráfrasis del extractor). Para conectar Tiendanube con "Tango Tiendas" remite a un tutorial; Tango Tiendas aparece como producto aparte que también conecta con PedidosYa. https://www.tiendanube.com/blog/tango-factura/ - B, dato 3, [S].
- Axoft ofrece "Tango Ecommerce": "Integrá tus plataformas de venta y mantené toda tu operación sincronizada". https://www.axoft.com/ - B, dato 3, [L] (solo el texto de portada; no abrí el detalle).
- Hay conectores independientes de los ERP (por ejemplo "Nexo Tiendas" en la tienda de apps de Tiendanube); la ficha no cargó. https://www.tiendanube.com/tienda-aplicaciones-nube/nexo-tiendas - [M]. Hueco.

**Quién es la fuente de verdad, sentido, SKU, frecuencia, fallas.** Ninguna fuente primaria que haya leído lo explica en general; la doc de Shopify sobre webhooks respalda el mecanismo (entrega no garantizada, duplicados, reconciliación). Lo siguiente es **conclusión mía, sin fuente propia**, a verificar: el stock suele tener un único dueño (el ERP o la tienda) y el otro lado lo refleja; la sincronización se mapea por SKU, y la sobreventa aparece cuando dos canales venden entre dos sincronizaciones o cuando un webhook se pierde. Está en Huecos.

### Recurso canónico propuesto
- **Documentación de webhooks de Shopify** (sección sobre entrega no garantizada, duplicados y reconciliación) como explicación general de por qué falla una sincronización por eventos.
- **Doc oficial de autenticación de Mercado Libre** (parte: access token 6 h, refresh token de un solo uso, `offline_access`). Hay que abrirla desde un navegador de una persona; desde acá devolvió 403. Fijarse en: si el refresh token de 6 meses se renueva en cada uso y qué eventos invalidan el access token.
- **Intro de la API de Tiendanube** (rate limit 40/2 por segundo y multiplicador 10 por plan) como ejemplo concreto de cubo con goteo.

---

## Componente 3. Fichas de sistemas en Argentina

### Fuentes

| # | Fuente | URL | Tipo | Aut. | Prof. | Ejem. | Unic. | Marca |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Axoft, home | https://www.axoft.com/ | primaria | 2 | 1 | 1 | 2 | [L] |
| 3.2 | Dux Software, home | https://www.duxsoftware.com.ar/ | primaria | 2 | 1 | 1 | 2 | [L] |
| 3.3 | Dux Software, precios | https://www.duxsoftware.com.ar/precios | primaria | 3 | 3 | 1 | 3 | [L] |
| 3.4 | Contabilium, home | https://www.contabilium.com/ar | primaria | 2 | 1 | 1 | 2 | [L] |
| 3.5 | Contabilium, planes | https://contabilium.com/ar/planes | primaria | 3 | 3 | 1 | 3 | [S] |
| 3.6 | Xubio, home con planes | https://www.xubio.com/ar | primaria | 3 | 3 | 1 | 3 | [L] |
| 3.7 | Colppy, precios | https://www.colppy.com/precios/ | primaria | 3 | 3 | 1 | 3 | [S] |
| 3.8 | Colppy, home | https://www.colppy.com/ | primaria | 2 | 1 | 1 | 2 | [L] |
| 3.9 | Alegra Argentina, home | https://www.alegra.com/argentina/ | primaria | 2 | 1 | 1 | 2 | [L] |
| 3.10 | Fudo, home | https://www.fu.do/ | primaria | 2 | 1 | 1 | 2 | [L] |
| 3.11 | TusFacturasAPP, home | https://www.tusfacturas.app/ | primaria | 2 | 2 | 1 | 2 | [L] |
| 3.12 | SpomBridge, comparativa (precios leídos por ellos el 15-oct-2026) | https://app.spomsolutions.com/blog/mejor-erp-pymes-argentina | secundaria con conflicto de interés | 1 | 2 | 1 | 2 | [S] |
| 3.13 | Develop Argentina | https://www.developargentina.com/blog/sistemas-gestion-comercial-argentina-2026 | secundaria con conflicto de interés | 1 | 2 | 1 | 1 | [S] |
| 3.14 | Tiendanube, blog Tango Factura | https://www.tiendanube.com/blog/tango-factura/ | secundaria | 2 | 2 | 2 | 2 | [S] |

### Tabla comparativa de precios (ARS, mensual, consultado 2026-11-22 salvo indicación)

| Sistema | Plan | Precio | IVA | Límites | Fuente / marca | Cal. |
|---|---|---|---|---|---|---|
| Dux Software | Inicial | $36.000 | + IVA | 250 comprobantes de venta/mes, 1 tienda online, 1 usuario admin | 3.3 [L] | A-1 |
| | Estándar | $75.300 | + IVA | 1.500 comprobantes, 3 tiendas | 3.3 [L]; coincide con 3.12 | A-1 |
| | Pro | $111.200 | + IVA | 5.000 comprobantes, 4 tiendas, API | 3.3 [L] | A-2 |
| | Full | $150.300 | + IVA | ilimitados, 5 tiendas, API | 3.3 [L] | A-2 |
| | Complementos | usuario extra $4.700; catálogo online $6.000; contabilidad avanzada $10.000; integración VTEX $30.000 | + IVA | | 3.3 [L] | A-2 |
| Contabilium | Standard | $122.000 ($109.800 anual) | + IVA | 1.500 comprobantes, 5.000 SKU, 1 CUIT, 2 usuarios, 2 puntos de venta ARCA, 3 cuentas integradas | 3.5 [S]; coincide con 3.12 | A-1 |
| | Pro | $179.000 ($161.100 anual) | + IVA | 5.000 comprobantes, 10.000 SKU, 2 CUIT, 10 usuarios, 3 PV, 4 cuentas | 3.5 [S] | A-2 |
| | Full | $245.000 ($220.500 anual) | + IVA | 10.000 comprobantes, 20.000 SKU, 3 CUIT, usuarios ilimitados, 5 cuentas, API | 3.5 [S] | A-2 |
| | Enterprise | a medida | | | 3.5 [S] | A-2 |
| Xubio | Empresa Gratis | $0 | | 10 facturas/mes, 1 usuario | 3.6 [L] | A-2 |
| | Empresa Básico | $128.000 con otros medios; $98.700 con débito bancario (promo CYBER 50% = $49.350 por 6 meses) | + IVA | 300 facturas/mes, 3 depósitos, 3 usuarios | 3.6 [L] | A-2 |
| | Empresa Estándar | $206.600 otros medios; $161.800 con débito (promo $80.900 por 6 meses) | + IVA | 1.000 facturas/mes, 5 depósitos, 5 usuarios | 3.6 [L] | A-2 |
| | "Emprendedor Ilimitado" | $124.600 ($93.600 con débito) | + IVA | facturas, usuarios y depósitos ilimitados | 3.12 [S] (15-oct-2026); **no lo vi en la home** | C-4 |
| Colppy | Essential | $128.500 (Estudios: $89.500) | + IVA | 300 comprobantes/mes, 2 usuarios | 3.7 [S] | A-2 |
| | Platinum | $189.500 | + IVA | 1.000 comprobantes | 3.7 [S] | A-2 |
| | Full | $261.500 | + IVA | 3.000 comprobantes, 1 punto de venta en app | 3.7 [S] | A-2 |
| | Enterprise | $310.900 | + IVA | 7.000 comprobantes, 3 puntos de venta | 3.7 [S] | A-2 |
| | Colppy Plus | $627.500 | + IVA | | 3.7 [S] | A-3 |
| Tango Factura / TFactura (Axoft) | Factura | $20.891 | + IVA | 50 comprobantes, 200 presupuestos | 3.14 [S], artículo actualizado 26-ene-2026 | B-4 |
| | Factura Pro | $48.207 | + IVA | 200 comprobantes, 400 presupuestos | 3.14 [S] | B-4 |
| | Negocios | $106.237 ($95.613 anual) | + IVA | comprobantes ilimitados, 2.000 presupuestos | 3.14 [S] | B-4 |
| | Negocios Pro | $171.906 ($137.524 anual) | + IVA | ilimitados | 3.14 [S] | B-4 |
| Tango Gestión | SaaS básico | "desde unos $180.000/mes" | no dice | | 3.13 [S] (autor vende software a medida) | D-5 |
| Tango Punto de Venta, Tiendas | | no publica | | licencia por módulos y puestos de trabajo (resumen de búsqueda sobre un documento de Axoft, sin abrir) | [S] | - |
| TusFacturasAPP | planes | desde $15.251,28 al mes | IVA incluido | | 3.11 [L] | A-2 |
| | planes con API | desde $38.128,20 al mes | IVA incluido | | 3.11 [L] | A-2 |
| Alegra | | no obtenido | | 15 días gratis, "Precio fijo por 6 meses" | 3.9 [L] | A-2 (solo la promo) |
| Fudo | | no obtenido | | | | - |
| Bsale | | no obtenido | | | | - |
| Odoo Argentina | Enterprise | desde USD 24,90 por usuario/mes; Community gratuita con módulos argentinos de la comunidad | no dice | | 3.13 [S] | D-5 |
| Otros citados por 3.12/3.13 (no investigados) | Tilo $49.000 con IVA, SpomBridge $49.999 con IVA, Contagram $58.900 + IVA, Gestión Nube $74.999, La Pyme $119.900 | | | | 3.12 [S] (3.12 es parte interesada) | C-4 |

Aclaraciones: (a) Los precios de Contabilium, Dux y Xubio coinciden entre la página del fabricante y la comparativa de octubre, y por eso reciben dato 1 en los de entrada; el resto, 2. (b) Xubio muestra su precio rebajado por la promoción CYBER hasta el 30-nov-2026; el precio de lista es el "otros medios". (c) Hay discrepancia que no pude resolver sobre la columna "Empresa Estándar" de Xubio, que no incluye el plan "Emprendedor Ilimitado" citado por la comparativa; puede estar en la pestaña "Emprendedores" que la home no abre. (d) Colppy: la página tiene dos grillas por perfil (Empresas/PyMEs y Estudios contables), y la extracción puede haber mezclado columnas; la grilla de Empresas es la primera. Hay que verificar a mano.

### Fichas

**Tango (Axoft).** Software de gestión argentino; productos: Tango Gestión (pymes y grandes), Punto de Venta (minoristas, sucursales, franquicias), Estudios Contables, Restô, Capital Humano, TFactura (nube, pequeñas empresas) y Tango Ecommerce. Cuenta que son "Más de 60.000 empresas, 200 centros de servicio y 110.000 personas capacitadas" y "el software #1 de Argentina" (dicho por la empresa). https://www.axoft.com/ - fuente B, dato 3, [L]. Origen: el artículo de Tiendanube dice "Axoft Argentina fundado en 1988" (B-3, [S]; https://www.tiendanube.com/blog/tango-factura/). Con Tiendanube: "Tango Tiendas" aparece en la tienda de apps como desarrollada por Axoft y, según el resumen de buscador, requiere ser usuario de Tango Gestión (D-5, [S]). Reseñas: no obtenidas.

**Dux Software.** Sistema de gestión comercial en nube para pymes, comercios y distribuidoras: stock, POS, facturación ARCA, ecommerce, informes. "+4.800 clientes nos eligen desde 2017" (dicho por la empresa) y "Soporte 24/7" (bot 24/7, agentes de lunes a viernes). Tiene POS; integra "Mercado Libre, Tienda Nube, WooCommerce, entre otras", más un complemento VTEX. https://www.duxsoftware.com.ar/ y /precios - A-2, [L]. Ojo de homonimia: www.dux.com.ar es un estudio de diseño, no el ERP. Dueño/origen: no obtenidos. Reseñas: Capterra (https://www.capterra.com/p/213765/Dux-Software/) devolvió 403, no leída.

**Contabilium.** ERP en la nube; módulos de facturación, compras, stock, tesorería, contabilidad, punto de venta, comprobantes con IA. "Más de 7.000 empresas de Argentina, Chile, Paraguay y Uruguay" (dicho por la empresa). Integra MercadoLibre, TiendaNube, WooCommerce, Shopify, PrestaShop y Mercado Pago (cuentas integradas por plan). Soluciones por tipo: mayoristas, ecommerce y marketplaces, tiendas físicas. Prueba de 10 días. https://www.contabilium.com/ar [L] y https://contabilium.com/ar/planes [S] - A-2. Dueño: no obtenido. Reseñas: no obtenidas.

**Xubio.** Software de gestión y facturación electrónica para empresas y estudios contables: facturación, stock, contabilidad, sueldos, ajuste por inflación, conciliación bancaria. "Más de 60.000 empresas confían en Xubio", "+240.000.000 comprobantes generados", "8 de cada 10 clientes que nos recomiendan" (dicho por la empresa). https://www.xubio.com/ar - A-2, [L]. Integra Mercado Libre, Mercado Pago, Tiendanube y WooCommerce según la comparativa de octubre (3.12, [S], C-3); la home habla de "Integraciones" sin detallar. Hay una página de socio en Tiendanube (https://www.tiendanube.com/partners/xubio-com) que no pude leer. POS: la comparativa dice "no figura". Dueño: no obtenido. Reseñas: no obtenidas.

**Colppy.** Sistema contable/administrativo online con facturación electrónica ARCA, bancos, sueldos, cobranzas; apuntado también a estudios contables. Declara "+3.000 empresas confían en Colppy" (precios, [S]) y "El 70% de los clientes afirman que Colppy les brinda una mejor visión de la salud financiera" (home, [L]). Integra Mercado Pago y, según la home, "Tiendanube, Mercado Libre y más" en su página de integraciones; la comparativa de octubre dice que no publica integración con ML ni Tiendanube en su página de planes (3.12, [S]). Dos fuentes discrepan: las doy las dos. POS: tiene "puntos de venta" como numeración de comprobantes, no un POS de local. https://www.colppy.com/ y /precios/ - A-3. Certificada "ISO 9001:2015". Dueño: no obtenido.

**Tango Factura / TFactura.** Facturador y gestión liviana de Axoft en nube; se integra con Tiendanube (ver Componente 2). Precios arriba. Capterra lista "Tango Factura" con "1290,00 ARS" como precio inicial (resumen de buscador, [S], D-5, discrepa con 20.891 de Tiendanube; no es explicable sin abrir Capterra).

**Alegra Argentina.** Plataforma de gestión, facturación y POS, de origen no argentino (la home tiene selector de países; origen no verificado). "Más de 40.000 pymes en Argentina usan Alegra" (dicho por la empresa). Conecta con Mercado Libre desde "Alegra Gestión". POS propio con múltiples terminales y turnos de caja. https://www.alegra.com/argentina/ - A-2, [L]. Precios: la página /precios no devolvió cifras.

**Fudo (gastronomía).** Plataforma para restaurantes, bares y cafés: gestión, cobros, delivery. "35.000+ negocios eligen Fudo" (dicho por la empresa). https://www.fu.do/ - A-2, [L]. Precios: /ar/precios dio 404; no obtenidos.

**TusFacturasAPP.** Facturador ARCA con stock, compras, cobros, cuentas corrientes, micrositio de cada cliente con pago por Mercado Pago, y una API REST de factura electrónica para integrar en otros sistemas. "11 años en el mercado". Precios arriba. https://www.tusfacturas.app/ - A-2, [L]. Integra Mercado Pago; Tiendanube/ML: no vi mención. Ejemplo de facturador que opera como conector de facturación para sistemas propios.

**Odoo en Argentina.** Edición Community con módulos argentinos de la comunidad; Enterprise desde USD 24,90 por usuario/mes. https://www.developargentina.com/blog/sistemas-gestion-comercial-argentina-2026 - D-5, [S]. Localización argentina oficial: no verificada.

**Bsale, Finnegans, Holistor, Flexxus, Facturante.** No investigados: bsale.com.ar no resolvió el nombre de dominio; el resto, por el presupuesto de búsqueda. Hueco.

### Cantidad de clientes que declara cada uno (dicho por la empresa)

| Sistema | Cifra | Fuente | Cal. |
|---|---|---|---|
| Axoft/Tango | más de 60.000 empresas | https://www.axoft.com/ [L] | B-3 |
| Xubio | +60.000 empresas gestionadas en Argentina | https://www.xubio.com/ar [L] | B-3 |
| Dux | +4.800 clientes | https://www.duxsoftware.com.ar/ [L] | B-3 |
| Contabilium | más de 7.000 empresas (4 países) | https://www.contabilium.com/ar [L] | B-3 |
| Colppy | +3.000 empresas | https://www.colppy.com/precios/ [S] | B-4 |
| Alegra | más de 40.000 pymes en Argentina | https://www.alegra.com/argentina/ [L] | B-3 |
| Fudo | 35.000+ negocios | https://www.fu.do/ [L] | B-3 |
| TusFacturasAPP | no declara cifra de clientes | | |

Axoft y Xubio declaran la misma cifra, "60.000". Lo anoto sin interpretarlo; son dos páginas distintas de dos empresas distintas.

### Calificaciones y cantidad de reseñas
No obtenidas para ninguna. Capterra (Dux, Xubio) devolvió 403, y la tienda de apps de Tiendanube no mostró el listado en la lectura. Hueco total.

### Recurso canónico propuesto
- Para "qué incluye y cuánto cuesta": la página de precios de cada fabricante, fechada, nunca la comparativa de un competidor. En Argentina la mejor de leer es **https://www.duxsoftware.com.ar/precios** por su tabla de herramientas por plan (la fila "Límite de comprobantes" y "Límite de ecommerce para integrar" explica el modelo de cobro).
- Para "cómo se ve la competencia": la comparativa de SpomBridge (3.12) sirve como mapa de actores, con la advertencia de que es parte interesada y de que sus montos "con IVA" son cálculos suyos del 21%.

---

## Huecos

1. **Documentación oficial de Mercado Libre no leída (403 con WebFetch y con el navegador).** Faltan: texto literal de duración del refresh token (6 meses según resúmenes; si se renueva con cada uso, no confirmado), lista de eventos que invalidan el token, límites de llamadas, notificaciones/webhooks de ML (tópicos, reintentos), manejo de stock en publicaciones y causas de pausas.
2. **Recurso conceptual (Laudon & Laudon) no abierto.** El presupuesto de búsqueda se agotó. Falta una definición canónica de ERP, y literatura independiente sobre cómo falla una implementación (migración, dependencia del contador, costos). Lo que hay sobre fallas es de un autor interesado.
3. **Tango**: sin precio público de Tango Gestión, Punto de Venta ni Tango Tiendas (solo un "desde unos $180.000" de un tercero); sin páginas de producto abiertas.
4. **Bsale, Finnegans, Holistor, Flexxus, Facturante, Odoo oficial**: no investigados.
5. **Precios de Alegra y Fudo**: no obtenidos. Colppy y Contabilium Planes pasaron por extractor, no por texto crudo; verificar.
6. **Reseñas y calificaciones**: ninguna cifra (Capterra 403; app store de Tiendanube sin listados; Contabilium lista "opiniones" en su sitio, no abierta).
7. **Dueño y origen** de Dux, Contabilium, Xubio, Colppy y Alegra: no obtenidos (salvo "desde 2017" de Dux y 1988 de Axoft).
8. **Reintentos de webhooks de Tiendanube, WooCommerce y ML**; cifras por plan de Shopify; frecuencia típica de sincronización de los conectores; qué sistema es dueño del stock por defecto. Lo que está dicho sobre sobreventa, pausadas y pedidos duplicados es el mecanismo de Shopify más mis conclusiones, no una fuente que mida esas fallas.
9. **Integraciones por sistema**: salvo Contabilium y Dux (primaria), las de Xubio y Colppy dependen de una comparativa interesada y de menciones de home; Point (Mercado Pago) no apareció en ningún lado.
10. Los precios son de noviembre de 2026 y hay promociones vigentes (CYBER Xubio hasta 30-nov, CYBER15 en Contabilium); dentro de un mes pueden no valer.
