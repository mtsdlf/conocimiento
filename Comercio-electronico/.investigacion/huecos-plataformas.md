# Huecos de plataformas: segunda pasada (2026-11-22)

Cierra parte de los huecos de `plataforma-de-tiendas.md`. Fecha de consulta de todo lo volátil: 2026-11-22. Marcas: [L] página leída vía WebFetch (devuelve un resumen del modelo sobre la página; las citas vienen de ahí), [S] resumen del buscador. Puntajes omitidos salvo donde importa: todas son primarias de la empresa (autoridad 3 para sus propios datos, con interés comercial en precios y métricas) salvo que se indique. El presupuesto de búsquedas web se agotó a mitad de la pasada; el resto se hizo con WebFetch a URLs conocidas, y muchas dieron 403/404/ECONNRESET.

## 1. Mercado Libre como marketplace y Mercado Shops

### Fuentes
| Fuente | URL | Tipo | Marca |
|---|---|---|---|
| 10-K FY2025 de MercadoLibre Inc. (cierre 31-dic-2025) | https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm | primaria | [L] parcial: caracteres 0-100.000 y 200.000-341.712 (faltan 100.000-200.000 en lo que dio resultado útil) |
| Resultados 4T 2025 | https://news.mercadolibre.com/en/financial-results-fourth-quarter-2025 | primaria | [S] (403 al abrirla; cifra de GMV viene del buscador) |

### Cifras del 10-K FY2025 (US$ millones, 2025 vs 2024)
- Ingresos netos e ingresos financieros: 28.893 (+39,1% desde 20.777). Comercio: 16.294 (+34,0% desde 12.159). Fintech: 12.599 (+46,2% desde 8.618). https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm
- Argentina (segmento): 5.962 (+56,2% desde 3.818). Comercio 2.034 (+44,6% desde 1.407). Fintech 3.928 (+62,9% desde 2.411). Fintech pesa casi el doble que comercio en Argentina.
- Crecimiento 2025 del GMV: "a 26.4% increase in gross merchandise volume"; del volumen total de pagos (TPV): 41,3%. El 10-K en lo leído no da el GMV absoluto.
- GMV total 2025: US$ 65 mil millones (+26% interanual) según el buscador que resumió el comunicado de 4T 2025 [S]; Argentina: GMV +42% interanual en moneda neutral (mismo origen, [S]). Falta verificar contra el comunicado.
- Concentración: Brasil, Argentina y México suman 95,6% (2025) y 95,7% (2024) de los ingresos netos. En 2025, 52,6% de los ingresos estaban en reales, 22,4% en pesos mexicanos y 20,6% en pesos argentinos.
- Inflación anual de Argentina que cita el 10-K: 31,5% (2025), 117,8% (2024), 211,4% (2023).
- Cambio de método (según el buscador, citando un proxy posterior, [S]): los ingresos 2025 se presentan en dólares constantes y ya no incluyen ajustes por deflación de Argentina; cuidado al comparar con 2024.

### Take rate
No lo calculo como dato. 16.294 / 65.000 = 25%, pero "Comercio" incluye ventas propias (1P), envíos, publicidad y otros, no solo comisiones de marketplace, y el GMV 65 mil M viene de un resumen [S]. Un 10-K antiguo (2014) define take rate como ingresos de marketplace sobre GMV, según el buscador [S]; no lo abrí. Hueco: take rate publicado y comisiones por venta (la página de tarifas dio 403 en la pasada anterior).

### Mercado Shops (cierre)
- Cita literal del 10-K: "Mercado Shops was discontinued as of December 31, 2025." Y en enero de 2025 la empresa anunció la migración de Mercado Shops a "Mi Página", "fully embedded within the Marketplace". https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm [L] (fuente primaria, una sola).
- No encontré el comunicado de ayuda original (fecha exacta del anuncio de enero 2025 y condiciones de migración): búsqueda agotada. Hueco.

### Recurso canónico
10-K de MercadoLibre, Item 7 (MD&A): tabla de ingresos por segmento y país; fijarse en que comercio y fintech son líneas distintas y que en Argentina fintech es más grande.

## 2. Planes y precios públicos (consulta 2026-11-22)

| Plataforma | Resultado |
|---|---|
| Tiendanube (Argentina) | Ya relevado en `plataforma-de-tiendas.md` §4. Esta pasada confirmó que la página tiene 5 planes (Inicial, Esencial, Impulso, Escala, Evolución) y fecha de última modificación 28-ago-2026 (https://www.tiendanube.com/planes-y-precios, [L]). Comisión por venta propia: 2% / 1% / 0,7% con pasarela externa; ver tabla previa. |
| Empretienda | HUECO. https://www.empretienda.com.ar y /precios: ECONNRESET en dos intentos. |
| Jumpseller (Argentina) | HUECO. https://jumpseller.com/pricing y /ar/pricing: 404. Datos previos: 64 tiendas en Argentina según StoreLeads, prueba de 7 días. |
| Wix eCommerce (Argentina) | HUECO. https://es.wix.com/ecommerce/pricing y https://www.wix.com/ecommerce/pricing: 404. Datos previos: planes Core, Business y Business Elite, sin precios en la página. |

## 3. Documentación técnica

### Shopify: pods
- Fuente: https://shopify.engineering/mysql-database-shard-balancing-terabyte-scale [L] (primaria, blog de ingeniería de Shopify; esta URL abrió, la anterior no). Autoridad 3, profundidad 2.
- Cita: "A pod is an isolated instance of Shopify consisting of an individual MySQL database shard". "Every pod houses a unique subset of shops on the platform." "two high-traffic merchants are isolated at the pod level."
- Resumen de la página: cada pod es un stack autocontenido con su shard de MySQL más Redis y Memcached; una capa de ingress consulta una tabla de ruteo para mandar cada request al pod que tiene los datos de la tienda; la clave de sharding es `shop_id`; mover una tienda es copiar todas sus filas a otro shard; las tiendas se rebalancean entre pods para equilibrar la carga de la base. Cierra el hueco "pod sin fuente primaria leída" de la pasada anterior.

### Tiendanube / Nuvemshop
- Fuente: https://tiendanube.github.io/api-documentation/intro [L] (primaria). https://developers.tiendanube.com/docs/ dio error.
- URL base: "All URLs start with `https://api.tiendanube.com/2025-03/{store_id}`" (también vale el dominio de Nuvemshop .com.br); solo SSL; la versión de API va en la ruta.
- Autenticación: "We follow the OAuth 2 framework"; tras instalar la app el comerciante, se recibe un token que va en cada request.
- Apps: hay que registrarse como partner y crear la app en la sección Apps del panel de partners; cada request lleva un encabezado `User-Agent` con el nombre de la app y un contacto, si no devuelve 400.
- Webhooks: se puede registrar a `app/suspended` y `app/resumed` (acceso cortado o restituido por falta de pago); no se envían webhooks mientras el acceso está suspendido; esos eventos no se disparan al terminar una prueba gratis. La lista completa de eventos no la leí.
- Límite de tasa: "the default bucket size is of 40 requests with a leaky rate of 2 requests per second"; excedido, 429; límite por tienda y app; las tiendas de los planes Next o Evolución tienen un límite diez veces mayor.
- Temas: la página leída no los cubre. Hueco.

### WooCommerce
- Licencia: "GPL-2.0 license" (https://github.com/woocommerce/woocommerce [L]; descripción: "A customizable, open-source ecommerce platform built on WordPress"; 10,6 mil estrellas). https://wordpress.org/plugins/woocommerce/ [L] dice solo "WooCommerce is open source software", "Active installations 7+ million", versión 11.3.1. Es el máximo que muestra el directorio de plugins ("7+ millones"), no un conteo exacto.
- Costos de hosting y extensiones: HUECO, no medidos (no se abrió woocommerce.com/products ni precios de hosting).

### Adobe Commerce
- https://developer.adobe.com/commerce/ [L]: "Adobe provides developers with software, tools, and services to customize and extend Adobe Commerce"; ofertas nuevas "Commerce as a Cloud Service" y "Commerce Optimizer"; "API-first Commerce"; App Builder; Edge Delivery Services y dropins para storefronts; kit de integración con sistemas empresariales.
- https://developer.adobe.com/commerce/docs/ [L]: enlaza guías de Cloud (Commerce Cloud Service), Commerce Services y Services Connector; no menciona ediciones ni licencia.
- Licencia y ediciones (Open Source vs comercial): HUECO. La página de producto de Adobe no abrió (timeout/404).

## 4. Escalafy y sus alternativas

Confirmado por quien consulta: es Escalafy. Solo datos. En la pasada anterior no se halló ninguna plataforma de tiendas llamada "Scalafy" (ver `plataforma-de-tiendas.md` §6); no hubo búsquedas para otras grafías (Scalefast, etc.): hueco menor, ya resuelto por la confirmación.

### 4a. Escalafy en detalle

Fuentes (todas primarias, propias de la empresa, con interés comercial):
| Fuente | URL | Marca |
|---|---|---|
| Sitio (inglés) | https://www.escalafy.com/en | [L] |
| Sitio (español) | https://www.escalafy.com/ | [L] |
| Precios | https://www.escalafy.com/en/pricing | [L] |
| Ficha en Shopify | https://apps.shopify.com/escalafy | [L] |
| Ficha en Tiendanube (México) | https://www.tiendanube.com/mx/tienda-aplicaciones-nube/escalafy | [L] |

- Qué es: "Data intelligence for e-commerce brands" / "la plataforma de inteligencia de datos para marcas de e-commerce que quieren escalar". Combina datos de ventas, costos y publicidad para mostrar la ganancia real por canal, producto y pedido, y rastrea qué anuncio origina cada venta. Dos productos: Analytics (ventas, gasto publicitario y costos en un panel en tiempo real) y Pixel (recupera datos de clientes que pierden las plataformas de anuncios y los reenvía a Meta, TikTok y Klaviyo). Módulos listados en el sitio inglés: Analytics, Pixel, Ads, Products, Inventory, Lifetime Value y MCP/API.
- Plataformas donde se conecta: Shopify, Tiendanube y Mercado Libre (sitio y fichas). Hay una página de producto "Mercado Libre fees".
- Integraciones nombradas: Meta, Google, TikTok, Klaviyo y Perfit (email). Pagos: no hay lista de pasarelas; solo aparecen "Comisiones de pago" y el dato de ejemplo "shopify_payments". Envíos: sin proveedores nombrados (solo el campo "Costo de envío"). Costos: sin integración nombrada; una reseña sugiere carga manual de costos ("cargar todos los costos del negocio"). Cualquier otra afirmación sobre integraciones queda como no confirmada.
- Para quién (tamaño): no declara un segmento. Lo que muestran los precios: el plan base cubre hasta 300 pedidos/mes, el plan gratis hasta 50, y para más de 100.000 pedidos o varias tiendas hay plan a medida por WhatsApp.
- Modelo de cobro: suscripción mensual que escala por cantidad de pedidos del mes ("The price follows your orders for the month. Sell less, pay less."). No cobra por GMV (no lo dice). Sin contrato anual, sin cargo de alta (US$ 0).
- Precios (consulta 2026-11-22), USD, cobro cada 30 días:
  - Sitio (/en/pricing): Base US$ 19/mes y Advanced US$ 30/mes, ambos hasta 300 pedidos/mes; deslizador de 300 a "100k+" pedidos sin precios por encima de 300; Pixel con precio propio según pedidos; prueba "7 days free, with every feature".
  - Ficha de Shopify: Free (hasta 50 pedidos), Pro Analytics US$ 19/mes (prueba de 7 días), Pro Pixel US$ 99/mes (prueba de 14 días).
  - Ficha de Tiendanube (preguntas frecuentes): Analítica gratis hasta 50 órdenes/mes, Base US$ 19, Advanced US$ 30; Pixel desde US$ 99/mes.
  - Discrepancia: la ficha de Shopify no muestra el plan Advanced de US$ 30; el sitio no muestra el plan gratis ni el precio de US$ 99 del Pixel en lo leído. Se conservan los tres.
- Lanzamiento en la tienda de apps de Shopify: 6-oct-2025. Idiomas: español, portugués (Brasil) e inglés.
- País de origen: no declarado en el sitio. Pie de página: "Escalafy LLC, 5830 E 2nd St, Casper, WY 82604" (Wyoming, EE.UU.); la ficha de Shopify da una dirección en Casper, WY, y dice que la app está basada en Argentina [L, resumen del modelo; contradice o complementa la dirección]. Esas dos cosas conviven sin contradicción si la LLC es el vehículo legal; no está confirmado. El desarrollador figura en Tiendanube como "be-flowing". Una reseña menciona a "Mateo, uno de los founders" (sin apellido).
- Métricas públicas:
  - Marcas conectadas: 9.260 (sitio, 2026-11-22), sin definición de "conectada"; la ficha de Shopify decía "+3.000 marcas en LatAm" según la pasada anterior [S]. Discrepancia que se conserva.
  - Reseñas: Shopify 5,0 con 102 reseñas; Tiendanube 5,0 con 163 reseñas, las 163 de 5 estrellas (ambas 2026-11-22). El sitio español dice "318 reseñas verificadas" con 5,0 en tiendas de apps (102 + 163 = 265, no 318; falta explicar, puede incluir otra tienda de apps). Instalaciones: no se muestran.
  - Rondas de inversión, empleados, ingresos: no hallados; el sitio no tiene página de equipo ni de financiamiento. Hueco.

### 4b. Alternativas (apps de analítica de rentabilidad y atribución)

Todas las fichas de Shopify son primarias de la tienda de apps (datos de la ficha, 2026-11-22); las reseñas son un indicador de presencia, no de instalaciones (Shopify no las muestra en lo leído).

| App | Qué hace | Plataformas | Cobro y precio de entrada | Presencia | Origen |
|---|---|---|---|---|---|
| BeProfit | Seguimiento de ganancias | Shopify (ficha) | Plan por mes con tope de pedidos: Free (1 tienda, 150 pedidos/mes); Basic US$ 29/mes (US$ 249/año); Pro US$ 99 (US$ 948/año); Scale US$ 149 (US$ 1.428/año); extra US$ 0,30 por pedido, máx. US$ 500/mes; prueba de 14 días. https://apps.shopify.com/beprofit-profit-tracker | 4,5 con 203 reseñas | Coral Springs, FL, EE.UU. (dirección de la ficha) |
| TrueProfit | Ganancia y LTV en tiempo real | Shopify (ficha) | Plan por mes con pedidos incluidos: Basic US$ 35 (300 pedidos), Advanced US$ 60 (600), Ultimate US$ 100 (1.500), Enterprise US$ 200 (3.500); extra desde US$ 0,07 a US$ 0,30 por pedido con tope; prueba 14 días. https://apps.shopify.com/trueprofit | 4,9 con 930 reseñas | no leído |
| Polar Analytics | Analítica de datos para marcas | Shopify (ficha) | "Pricing based on online GMV": Core desde US$ 750/mes; descuentos por plazo anual; sin prueba propia declarada. https://apps.shopify.com/polar-analytics | 4,9 con 116 reseñas; lanzada 28-oct-2020 | París, Francia |
| Peel | Analítica de retención | Shopify (ficha) | Por tramo de pedidos mensuales: Core US$ 199/mes (6 mil pedidos), Essentials US$ 499 (16 mil), Accelerate US$ 899 (29 mil); prueba 30 días. https://apps.shopify.com/peel-insights | 5,0 con 38 reseñas | no leído |
| Northbeam | Atribución de marketing | Starter: solo Shopify; Professional y Enterprise: cualquier plataforma | Tramos por gasto en publicidad y volumen de datos (páginas vistas): Starter "$1,500" (sin período indicado), Professional US$ 3.500/mes, Growth y Enterprise a medida; Starter mensual, los demás anuales. https://www.northbeam.io/pricing | no medida (no está en tienda de apps leída) | no leído |
| Triple Whale | Analítica y atribución | no leído | HUECO: https://www.triplewhale.com/pricing dio 403; la ficha de Shopify (slugs `triple-whale`, `triplewhale`) dio 404 | sin dato | sin dato |
| Lifetimely | LTV y ganancia | no leído | HUECO: slugs probados dieron 404 | sin dato | sin dato |

- Tiendanube/Nuvemshop: en la tienda de apps (https://www.tiendanube.com/tienda-aplicaciones-nube) existe la categoría "Estadísticas", pero la página no listó apps dentro de ella en lo leído. Las que aparecieron cerca: Launch Tools (5,0, 5 reseñas; "analizá fuentes de tráfico", proyección de metas, análisis de competidores) y Pinterest (4,9, 332 reseñas; sigue conversiones). No hallé una app de rentabilidad o atribución además de Escalafy en esa tienda. La página de categoría https://www.tiendanube.com/mx/tienda-aplicaciones-nube/estadisticas no devolvió apps (solo metadatos). Hueco: no se verificó la categoría con navegador.
- Alternativas de América Latina fuera de las tiendas de apps: no hay búsquedas disponibles; no hallé ninguna con datos. Hueco.

### 4c. Tabla resumen (datos, sin opinión; consulta 2026-11-22)

| Nombre | Plataformas | Unidad de cobro | Precio de entrada (USD) | Presencia |
|---|---|---|---|---|
| Escalafy | Shopify, Tiendanube, Mercado Libre | pedidos del mes (suscripción) | gratis hasta 50 pedidos; US$ 19/mes hasta 300 | 9.260 marcas (sitio); 5,0 con 102 (Shopify) y 163 (Tiendanube) reseñas |
| BeProfit | Shopify | plan con tope de pedidos + extra por pedido | gratis (150 pedidos); US$ 29/mes | 4,5 con 203 reseñas |
| TrueProfit | Shopify | plan con pedidos incluidos + extra por pedido | US$ 35/mes (300 pedidos) | 4,9 con 930 reseñas |
| Polar Analytics | Shopify | GMV online | US$ 750/mes | 4,9 con 116 reseñas |
| Peel | Shopify | tramo de pedidos mensuales | US$ 199/mes (6 mil pedidos) | 5,0 con 38 reseñas |
| Northbeam | Shopify (Starter); cualquiera (Professional y Enterprise) | gasto en publicidad / páginas vistas | US$ 1.500 (Starter, período sin indicar); US$ 3.500/mes (Professional) | sin dato |
| Triple Whale, Lifetimely | sin dato | sin dato | sin dato | sin dato |

## 5. Recursos canónicos propuestos
- Shopify pods: la entrada de ingeniería de shard balancing (URL arriba); fijarse en la definición de pod, la clave `shop_id` y la tabla de ruteo.
- Tiendanube desarrolladores: introducción de la API (URL arriba); fijarse en OAuth por tienda, el límite de 40 requests con goteo de 2 por segundo, y el límite diez veces mayor en Next y Evolución.
- Mercado Libre: 10-K FY2025, ingresos por segmento y la nota de Mercado Shops.

## 6. Huecos que quedan
1. Planes de Empretienda, Jumpseller y Wix (las tres páginas fallaron; plan pendiente con otra URL o navegador).
2. Mercado Libre: GMV absoluto y take rate publicados; comisiones por venta; comunicado original del cierre de Mercado Shops y fecha del anuncio (el 10-K dice que cerró el 31-dic-2025 y que el anuncio de migración fue en enero de 2025). El tramo 100.000-200.000 del 10-K devolvió un resultado sin las cifras; no se leyó el MD&A completo.
3. WooCommerce: costos de hosting y extensiones; Adobe Commerce: licencia y ediciones; Tiendanube: eventos de webhook completos y temas.
4. Escalafy: rondas, empleados, país real de operación (LLC en Wyoming vs "basada en Argentina"), cuenta de "318 reseñas" y de "3.000 marcas" vs 9.260; integraciones con pagos y envíos no confirmadas.
5. Triple Whale, Lifetimely: sin ficha ni precio; origen de TrueProfit, Peel y Northbeam sin leer; apps latinoamericanas de analítica: sin búsqueda.
6. Presupuesto de búsquedas agotado: dos cifras de Mercado Libre (GMV de US$ 65 mil M y +42% de Argentina) y el cambio de método de ingresos quedan solo como [S].
