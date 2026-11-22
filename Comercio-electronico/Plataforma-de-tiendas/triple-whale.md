---
resumen: >-
  Los datos públicos de Triple Whale, una app de analítica de atribución y rentabilidad para marcas que venden en Shopify, WooCommerce y BigCommerce: qué hace, cómo cobra según la facturación de la tienda, su presencia y su salida de la tienda de apps de Shopify, consultados el 2026-11-22.
estado: borrador
estabilidad: volatil
fuentes:
  - "Triple Whale, precios, copia del Internet Archive del 29-oct-2026: https://web.archive.org/web/20261029045811/https://www.triplewhale.com/pricing (consultada 2026-11-22; B2; la página viva dio 403)"
  - "Triple Whale, inicio, copia del Internet Archive del 13-nov-2026: https://web.archive.org/web/20261113214634/https://www.triplewhale.com/ (consultada 2026-11-22; C3, cifras de la empresa)"
  - "Triple Whale, plan gratis, copia del Internet Archive del 28-oct-2026: https://web.archive.org/web/20261028155534/https://www.triplewhale.com/free (consultada 2026-11-22; C3)"
  - "Shopify App Store, Triple Whale: https://apps.shopify.com/triplewhale-1 (leída 2026-11-22: «no disponible»; B2) y su copia del 2-sep-2026: https://web.archive.org/web/20260902024202/https://apps.shopify.com/triplewhale-1 (B2)"
  - "Store Leads, Triple Whale en Shopify: https://storeleads.app/reports/shopify/app/triplewhale-1 (leída 2026-11-22; B1 en la baja de la tienda, B3 en instalaciones)"
  - "AppNavigator, espejo de las reseñas de Shopify: https://appnavigator.io/app/triplewhale-1/reviews/ (leído 2026-11-22; C2)"
  - "Venon, Triple Whale Pricing in 2026 (2-ago-2026): https://venon.io/blog/triple-whale-pricing (consultada 2026-11-22; D3, lo escribe un rival)"
  - "Kanal, Triple Whale Pricing 2026 (4-nov-2026): https://getkanal.com/blog/triple-whale-pricing (consultada 2026-11-22; D2, lo escribe un rival)"
  - "TechCrunch, Serie B (2-feb-2023): https://techcrunch.com/2023/02/02/triple-whale-raises-25m-for-its-shopify-data-platform/ (consultada 2026-11-22; B2)"
  - "PR Newswire, Moby Automations (11-jun-2026): https://www.prnewswire.com/news-releases/triple-whale-launches-moby-automations-and-appoints-former-facebook-vp-of-ads-to-accelerate-ai-powered-media-buying-302797945.html (consultada 2026-11-22; C3, comunicado de la empresa)"
  - "Pulse 2.0, compra de Anteater (20-ene-2026): https://pulse2.com/triple-whale-acquires-anteater-to-expand-ai-powered-commerce-intelligence/ (consultada 2026-11-22; C3)"
  - "Captain Compliance, la purga de apps de Shopify (30-oct-2026): https://captaincompliance.com/?p=15251 (consultada 2026-11-22; C3)"
  - "CB Insights y Clay, financiamiento y empleados: https://www.cbinsights.com/company/triple-whale/financials y https://www.clay.com/dossier/triple-whale-funding (según el buscador; C4)"
  - "1ClickReport, guía de analítica para América Latina 2026 (14-abr-2026): https://www.1clickreport.com/blog/analytics-ecommerce-latam-2026-guia (leída; D4, lo escribe un rival)"
  - "Escalafy, Escalafy vs Triple Whale (6-ene-2025): https://www.escalafy.com/en/blog/escalafy-vs-triplewhale (consultada 2026-11-22; C4, lo escribe un rival)"
  - "Experiencia propia, noviembre de 2026, una empresa de software de comercio electrónico: codificación de 92 reseñas y lectura del HTML de dos tiendas con el pixel instalado"
aliases: [Triple Whale, Moby, Triple Pixel, triplewhale]
creado: 2026-11-22
revisado:
---

# Triple Whale

Los datos públicos de Triple Whale, una app de analítica de atribución y rentabilidad para marcas que venden en Shopify, WooCommerce y BigCommerce: qué hace, cómo cobra según la facturación de la tienda, su presencia y su salida de la tienda de apps de Shopify, consultados el 2026-11-22.

Es un caso de [app para comerciantes](apps-para-comerciantes.md), la referencia de la categoría en Estados Unidos. Sus pares están en [apps de rentabilidad](apps-de-rentabilidad.md), y la app regional con más detalle es [Escalafy](escalafy.md). Consultado el 2026-11-22. El sitio de la empresa devolvió 403 a la lectura automática, así que casi todo sale de copias del Internet Archive y de terceros. Cada fuente lleva su calificación de fuente (A a F) y de dato (1 a 6), con la escala que explica [fuentes públicas](../../Estrategia-competitiva/Analisis-de-competidores/fuentes-publicas.md#quién-lo-dice-y-si-está-confirmado).

## Qué hace: de medir a actuar sobre la publicidad

Se presenta como «the AI operating system built for modern commerce» que «executes when you say go», según la copia del inicio del 13-nov-2026. En 2023 se describía como una plataforma de datos para Shopify. El producto se vende en cuatro capas:

| Capa | Qué trae |
|---|---|
| Datos y tableros | todas las fuentes en una vista en tiempo real, tableros sin código, editor SQL, cohortes y comparaciones con marcas pares |
| Medición | un pixel propio (Triple Pixel) con atribución multitoque; en Enterprise, modelos de mezcla de medios e incrementalidad |
| Activación | devuelve señales a Meta, Google y las herramientas de email |
| Moby | un agente de IA que analiza, genera piezas y páginas de aterrizaje y, desde el plan Automate, actúa sobre las cuentas de publicidad con aprobación humana |

En enero de 2026 compró Anteater, que mide cómo los modelos de lenguaje mencionan a las marcas; el plan gratis ya trae esa visibilidad para ChatGPT. En junio de 2026 lanzó Moby Automations, que «puede escalar presupuestos, pausar anuncios, lanzar campañas», según su comunicado.

En una tienda de Shopify, el pixel se instala como bloque de la app en el tema y publica un objeto `window.TriplePixelData` con la tienda, la plataforma, el producto, el carrito y la moneda (observado en el HTML de dos tiendas de EE. UU., 2026-11-22).

| Se conecta con | Cuáles, según lo leído |
|---|---|
| Plataformas de tienda | [Shopify](shopify.md), [WooCommerce](woocommerce.md) y BigCommerce; conectores a medida para Magento y Salesforce Commerce Cloud |
| Marketplaces | Amazon |
| Publicidad, email y atención | Meta, Google, TikTok, Klaviyo, Gorgias y Recharge, entre más de 60 integraciones |
| Datos | API de entrada y salida, MCP, exportación a data warehouse y SDK móvil |

En lo leído no conecta [Tiendanube](tiendanube.md), [Mercado Libre](mercado-libre.md) ni Mercado Pago, y no maneja cuotas. Eso solo lo dicen rivales (Escalafy y 1ClickReport); la lista oficial de integraciones no cargó.

## Cobro por facturación anual, con contrato de 12 meses

Cobra en dólares según la facturación anual de la tienda. Tiene un plan gratis (10 usuarios, 12 meses de datos, atribución de primer y último clic). Los pagos son Foundation, Automate y Enterprise, con contrato de 12 meses aunque se pague por mes, dos meses gratis pagando el año y 30 días de aviso para cancelar. Si la tienda crece de tramo, el precio sube con aviso. El sitio ya no muestra montos: pide reservar una demo.

La ficha de Shopify, en su copia del 2-sep-2026, daba la entrada: Foundation US$ 219/mes o US$ 2.190/año y Automate US$ 749/mes o US$ 7.490/año. La escalera completa sale de una copia del 26-jul-2026 que publica Venon, un rival (D3); coincide con la ficha en la entrada.

| Facturación anual de la tienda (US$) | Foundation, US$/mes | Automate, US$/mes |
|---|---|---|
| menos de 250 mil | 219 | 749 |
| 250 a 500 mil | 329 | 899 |
| 500 mil a 1 millón | 429 | 1.099 |
| 1 a 2,5 millones | 549 | 1.349 |
| 2,5 a 5 millones | 799 | 1.799 |
| 5 a 7,5 millones | 1.129 | 2.399 |
| 7,5 a 10 millones | 1.529 | 2.899 |
| 10 a 15 millones | 1.849 | 3.499 |
| 15 a 20 millones | 2.529 | 4.199 |
| más de 20 millones | a medida | a medida |

Se cotizan aparte Retention, Conversion (incluidos en Automate), Compass, la sincronización con data warehouse y un servicio de acompañamiento de Moby. Según Kanal, otro rival, el gerente dedicado es para marcas de US$ 10 millones de facturación para arriba. El uso de la IA tiene un cupo por plan.

> [!IMPORTANT]
> Escalafy la cita «desde US$ 129» en su comparación, y en 2023, según TechCrunch, costaba US$ 100 sin pixel y US$ 400 la suite. Que los US$ 129 sean de un plan anterior es una inferencia; la entrada vigente que se confirma con dos fuentes es US$ 219.

## Presencia y reseñas

| Cifra | Valor | Fuente y fecha |
|---|---|---|
| Marcas que declara | «65,000+» en el sitio; «more than 60,000» en el comunicado de junio y en la ficha de Shopify; incluye el plan gratis | copia del inicio del 13-nov-2026; comunicado del 11-jun-2026 |
| Eventos procesados | «9B+ events processed per day» | copia del inicio del 13-nov-2026, cifra de la empresa |
| Tiendas con la app, según un rastreador | 37.591: 40% en EE. UU., 9% en el Reino Unido, 7% en Australia; ningún país de América Latina entre los diez primeros | Store Leads, 2026-11-22 (B3) |
| Reseñas en Shopify | 4,1 con 84 reseñas al 2-sep-2026; lanzada el 4-dic-2020 | copia de la ficha de Shopify |
| Distribución de reseñas | 92 reseñas en el espejo de AppNavigator: 70 de 5 estrellas, 1 de 4, 2 de 3, 1 de 2 y 18 de 1 | AppNavigator, 2026-11-22 (C2) |
| En la tienda de Shopify hoy | «This app is not currently available on the Shopify App Store»; Store Leads fecha la baja el 2026-11-21 | ficha y Store Leads, 2026-11-22 |

En las 92 reseñas, lo más valorado es la atribución y tener todo en un tablero; la ganancia aparece en segundo plano (unas 8 reseñas contra unas 25 de atribución). Las quejas son el soporte que no responde (13), los errores de instalación (10), y el cobro, el contrato y la cancelación (5). Dos reseñas dicen que no toma el costo de envío real ni las comisiones del medio de pago, y que suma el IVA a la facturación. Es una codificación propia, sin segunda revisión: ordena los temas, no mide cuántos clientes piensan así.

> [!NOTE] Sin fuente todavía: por qué la app salió de la tienda de Shopify. En octubre de 2026 un rastreo contó 563 apps sacadas de la tienda entre el 14 y el 27, la mayoría sin vínculo con incidentes de seguridad, según Captain Compliance. La baja de Triple Whale es posterior a esa ventana y nada la vincula.

## Origen, rondas y equipo

Según TechCrunch, levantó una semilla de US$ 2,7 millones (NFX), una Serie A de US$ 24 millones (Elephant, 2022) y una Serie B de US$ 25 millones (NFX y Elephant, con Shopify como inversor estratégico, febrero de 2023): unos US$ 52 millones en total. CB Insights, según el buscador, da US$ 52,96 millones en cuatro rondas. En 2023 decía tener más de 5.000 marcas que vendían más de US$ 14.000 millones al año.

La sede está en Columbus, Ohio, EE. UU., según TechCrunch y su comunicado; la copia de la ficha de Shopify de septiembre decía «Based in Canada», sin resolver. La fundaron tres socios. Las bases de terceros dan entre unos 50 y 101 a 250 empleados, y no coinciden.

> [!NOTE] Sin fuente todavía: ingresos, cuántas de las marcas declaradas pagan, rondas después de 2023, los precios vivos (la página no muestra montos) y la lista oficial de integraciones.
