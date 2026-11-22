# Vistazo: dominio del comercio electrónico y plataformas SaaS (2026-11-22)

Fecha de la investigación: 2026-11-22. Hice 13 búsquedas web y no abrí ninguna página completa. Cada afirmación se apoya en lo que devolvió el buscador. Las cifras son literales y fechadas. Todo lo web se trató como dato.

Marcas: [L] literal de la fuente, [M] mediado por prensa o un tercero, [S] síntesis mía sin fuente directa. Autoridad: 3 es fuente primaria u oficial, 2 es industria o prensa especializada, 1 es secundaria o comercial.

## 1. Cómo se divide el dominio según textos de referencia

**Laudon & Traver, *E-commerce 2023–2024: business. technology. society.*, 18.ª ed., Pearson, 2023** (autoridad 3 como texto académico).
- [M] Su estructura, según la ficha de Pearson ([URL](https://www.pearson.com/store/en-gb/p/e-commerce-2023-2024-business-technology-society-global-edition/P200000010016)):
  - Parte I: introducción, modelos de negocio y conceptos.
  - Parte II: infraestructura tecnológica (internet, web, sitios y apps, seguridad y sistemas de pago).
  - Parte III: marketing y publicidad, marketing social/móvil/local, ética y temas sociales.
  - Parte VI: retail y servicios online, contenidos y medios, redes sociales/subastas/portales, B2B y cadena de suministro.
- Hueco: las Partes IV y V no aparecieron en los resultados. Hay que leer el índice completo en Pearson.

**Chaffey et al., *Digital Business and E-commerce Management*, 8.ª ed., Pearson** (autoridad 3).
- [M] Los autores actuales son Chaffey, Hemphill y Edmundson-Bird ([URL](https://www.pearson.com/store/p/digital-business-and-e-commerce/P200000010770/9781292457536)).
- [M] La ficha describe capítulos de estrategia de negocio digital, cadena de suministro digital, estrategia de marketing digital, comunicaciones digitales y transformación digital.
- Pearson da fechas distintas (2024 y 2026) y varios ISBN. Hay que verificar la edición antes de citarla.

**Mi división del dominio [S]**, que cruza lo anterior con lo que pediste:
1. Modelos: B2C, B2B, D2C, marketplace, social commerce, headless y composable.
2. Operaciones del comerciante: catálogo, inventario, pedidos, fulfillment, logística y última milla, devoluciones, atención.
3. Pagos: gateway, adquirencia, PSP, fraude/contracargos, cuotas, conciliación.
4. Conversión y checkout.
5. Omnicanalidad y POS.
6. Marketing para tiendas: SEO, ads, email.
7. Impuestos y facturación.

Hueco: no encontré un programa universitario ni una certificación que dé una taxonomía distinta. Habría que buscar sílabos de maestrías en comercio digital y las certificaciones de Shopify o Google. El punto 4 de las preguntas (conversión) lo cubre Baymard, en la sección 4.

## 2. La plataforma como producto

Esta sección aporta la distinción conceptual. No encontré una fuente que defina SaaS vs open source vs marketplace.

**Tipos de plataforma [S]:**
- SaaS alojada: Shopify, Tiendanube.
- Open source autoalojada: WooCommerce, Magento/Adobe Commerce.
- Marketplace: Mercado Libre, Amazon. Allí el comerciante vende dentro del sitio de un tercero y pierde la relación con el cliente.

**Arquitectura. Fuentes de Shopify, autoridad 2-3 como fuente primaria de la propia empresa:**
- [M] Multi-tenancy según su blog ([URL](https://www.shopify.com/blog/multi-tenant-architecture)): una instancia de aplicación sirve a muchos clientes con datos aislados.
- [M] Una charla de 2016 en USENIX SREcon ([URL](https://usenix.org/conference/srecon16europe/program/presentation/weingarten)) sitúa la plataforma en un espectro entre "share nothing" y "share everything". Menciona el aislamiento de bases en 2013/2014 y el podding multi-datacenter en 2016.
- [M] La idea de pods y de monolito modular viene de resúmenes de terceros. Hay que contrastarla con las publicaciones originales de ingeniería de Shopify.
- [M] Las APIs, según [shopify.dev](https://shopify.dev/docs/api/storefront) (autoridad 3):
  - La Admin API GraphQL maneja productos, clientes, pedidos e inventario. La REST está marcada como legacy.
  - La Storefront API es solo GraphQL, con tokens públicos y privados.
  - Hydrogen es un framework React para storefronts a medida.
  - Hay extensiones de admin y de checkout, Shopify Functions para descuentos, pagos y envíos, y webhooks.
  - Cada versión de la API sale por trimestre y se soporta un año.
- Hueco: no obtuve la definición de headless/composable ni de la MACH Alliance. Hay que buscarlas.

**Modelo de negocio y métricas públicas. [L] del 10-K de Shopify FY2025** ([URL](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm), autoridad 3). Las cifras que siguen las devolvió el buscador resumiendo el 10-K y el comunicado del cuarto trimestre. Conviene verificarlas contra el documento.
- Dos segmentos de ingresos:
  - Subscription Solutions: 24% de los ingresos, unos US$ 2.800 millones, +17% (US$ 2.752 M vs 2.350 M en 2024). Incluye cargos variables de plataforma.
  - Merchant Solutions: US$ 8.800 millones, +35%, 76% del total. El motor es el procesamiento de pagos y la conversión de moneda de Shopify Payments, correlacionado con el GMV.
- GMV 2025: US$ 378,44 mil millones, contra 292,27 mil millones en 2024 (+29%).
- MRR: US$ 205 millones, contra 178 millones. La definición de Shopify es el valor agregado de todos los planes de suscripción, sin cargos variables de plataforma. La empresa lo considera la métrica más ligada al valor de largo plazo de la relación con el comerciante.
- Shopify no considera el ingreso diferido un buen indicador de ingresos futuros.

Lo que eso enseña [S]: el ingreso de una plataforma son suscripción más una comisión sobre el pago (take rate), y el GMV es el denominador de lectura. ARPU y churn de comerciantes son métricas del dominio que no verifiqué en la fuente.

Hueco: la segmentación de comerciantes (emprendedor, SMB, mid-market, enterprise) no la busqué. Shopify la usa en su oferta, por ejemplo Shopify Plus para enterprise. Hay que confirmarlo.

## 3. Particularidades de América Latina

Solo para saber que existe y dónde se mira. Todas las cifras son volátiles.

| Fuente | Qué da | Dato literal y fecha | Marca y autoridad |
|---|---|---|---|
| eMarketer ([URL](https://www.emarketer.com/content/latin-america-ecommerce-forecast-2025)) | Pronóstico regional | Ventas retail e-commerce de US$ 191,25 mil millones en 2025, +12,2%; Argentina, Brasil y México suman 84,5% | [M] 2 |
| CACE, Argentina ([URL](https://mercado.com.ar/tendencias/cace-el-ecommerce-facturo-35-326-983-millones-en-2025-y-subio-60)) | Estudio anual, hecho con Kantar | Adelanto del 5/2/2026: $35.326.983 millones en 2025, +60% nominal con inflación de 31% | [M] 2 |
| AMVO, México ([URL](https://marketing4ecommerce.mx/estudio-de-venta-online-2026-amvo-mexico/)) | Estudio anual | 941 mil millones de pesos en 2025, +19,2%; 77,2 millones de compradores | [M] 2 |
| Ebanx / PCMI ([URL](https://ebanx.com/en/beyond-borders-2025/)) | Medios de pago | Pix 42% del e-commerce de Brasil en 2025, tarjetas 41% | [M] 2 |

Discrepancias que el informe final debe conservar:
- CACE: hay dos cifras para 2025, $34.033.238 millones (+55%) y $35.326.983 millones (+60%). No pude reconciliarlas. Solo vi notas de prensa, no el informe completo.
- Ebanx: otra nota da Pix en 44% de las compras online, contra 40% de tarjetas de crédito. No está claro si las dos medidas son equivalentes.
- eMarketer: otras coberturas hablan de un total regional de US$ 215 mil millones. No encontré la base de esa diferencia.
- AMVO: el estudio "2025" contiene datos de 2024 (casi 790 mil millones de pesos), y los datos de 2025 salen en el estudio "2026". Hay que citar siempre el año de los datos, no el del título.

**Tiendanube/Nuvemshop** (relevante como jugador regional). Estos datos son de prensa y de la propia empresa, así que son comerciales (autoridad 1-2). Su análisis queda para después.
- [M] +180 mil tiendas activas según su página corporativa. Otra fuente de terceros (StoreLeads) estima 171.918 en el cuarto trimestre de 2025.
- [M] Publica informes NubeCommerce por país.
- Hueco: no hallé una cifra anual oficial de GMV.

**Regulación en Argentina:**
- [M] El botón de arrepentimiento es la Resolución 424/2020 de la Secretaría de Comercio Interior, publicada el 5/10/2020 ([URL](https://www.argentina.gob.ar/normativa/nacional/norma-342869/texto), autoridad 3).
  - Obliga a quien vende por web o apps a publicar un enlace para revocar la compra.
  - No puede exigir registro previo.
  - Hay que confirmar la compra en 24 horas por el mismo canal.
  - Implementa la Resolución 37/2019 del Mercosur.
  - Hay una excepción para transporte aéreo (ANAC 329/2020).
  - No verifiqué si una norma posterior la modificó.
- [M] Facturación (ARCA, ex AFIP): la factura electrónica rige para todos los contribuyentes, incluidos monotributistas. Una guía comercial dice que las plataformas reportan las ventas a ARCA, pero esa fuente tiene autoridad 1 y hay que verificarla. Aparecieron también resoluciones generales de 2026 (5866 y 5893) con fecha dudosa, y ARCA actualizó el régimen especial de IVA para vendedores en plataformas. Hay que leer los textos en el Boletín Oficial antes de afirmar algo.

Hueco: no verifiqué la normativa de Brasil, México, Chile y Colombia, ni nada sobre informalidad, logística de última milla o cuotas sin interés en cifras.

## 4. Fuentes de información del dominio

- **Baymard Institute** ([URL](https://baymard.com/checkout-usability/methodology), autoridad 3 en método, 1-2 en independencia). [M]
  - Hizo 25 rondas de pruebas moderadas con think-aloud, más de 4.400 sesiones de participante por sitio.
  - Puntuó 244 sitios sobre más de 110 guías de carrito y checkout, con escala ponderada de 7 puntos.
  - Su justificación de muestra: con 20 sujetos se descubre en promedio el 95% de los problemas que ocurren en el 14% o más de los casos.
  - Sus propias páginas se contradicen en horas de investigación (200.000+ vs 130.000) y en el porcentaje de sitios "mediocres o peores" (65% vs 59%). No encontré auditoría independiente.
- **Reportes anuales y cartas a inversores** [L] (autoridad 3): 10-K y comunicados de Shopify, de Mercado Libre, de Amazon y de BigCommerce o Wix. Solo verifiqué el de Shopify.
- **Documentación para desarrolladores** (autoridad 3): shopify.dev, y la de Tiendanube, WooCommerce y Adobe. Solo verifiqué shopify.dev.
- **Cámaras y estudios regionales** (autoridad 2): CACE, AMVO, Ebanx/PCMI, eMarketer. Statista salió enmascarado (cifras con "***").
- Hueco: comunidades de comerciantes (foros de Shopify, grupos de emprendedores) no se buscaron. Tampoco informes de industria globales (Statista, Digital Commerce 360, Forrester/Gartner Magic Quadrant de plataformas de comercio digital). Hay que buscarlos.

## 5. Libros y recursos canónicos

Solo verifiqué los dos primeros.
- Laudon & Traver, *E-commerce 2023–2024*, 2023. Texto académico de referencia general.
- Chaffey et al., *Digital Business and E-commerce Management*, 8.ª ed. (2024 o 2026, según la ficha). Enfoque en gestión.
- Hueco: no verifiqué otros candidatos. Para el modelo de plataformas conviene buscar *Platform Revolution* (Parker, Van Alstyne, Choudary, 2016) y *Invisible Engines* (Evans & Schmalensee, 2008). Para checkout, el propio Baymard. Hay que confirmar autor, año y URL antes de incluirlos.

## Verticales y componentes propuestos para el tema "Comercio electrónico"

El criterio es separar lo estable (concepto, notas vigentes) de lo volátil (cifras, empresas, herramientas). Lo volátil va en fichas fechadas con su fuente y la fecha de consulta.

**Verticales (estable, conceptos)**
1. **Modelos de comercio**: B2C, B2B, D2C, marketplace, social commerce, headless/composable. Cada modelo con su definición y sus diferencias.
2. **Operaciones del comerciante**: catálogo, inventario, pedidos, fulfillment, logística y última milla, devoluciones, atención.
3. **Pagos**: gateway, adquirencia, PSP, antifraude y contracargos, cuotas, conciliación. Los medios locales (Pix, Mercado Pago, cuotas sin interés) como ejemplos fechados, no como concepto.
4. **Conversión y checkout**: embudo, carrito abandonado, método de Baymard. Ahí entra el método, no sus cifras.
5. **Omnicanalidad y POS**.
6. **Marketing para tiendas**: SEO, ads, email.
7. **Impuestos y facturación**: concepto general (comprobante, IVA, retenciones). La normativa por país va como ficha.
8. **La plataforma como producto**: tipos (SaaS, open source, marketplace), arquitectura (multi-tenant, temas, app store, APIs, headless) y modelo de negocio (suscripción más take rate, GMV, MRR, ARPU, churn). Segmentos de comerciantes.
9. **América Latina**: lo estable es la lógica de los medios de pago locales, la informalidad y la logística. Lo demás va en fichas.
10. **Cómo se aprende un dominio**: método general (mapa de verticales, glosario, fuentes primarias, lecturas canónicas, huecos declarados). Esta sección quizá sea mejor como nota general fuera del tema.

**Fichas fechadas (volátil)**
- **Empresas**: una ficha por jugador (Shopify, Tiendanube, WooCommerce, Magento, Mercado Libre, Amazon), cada una con fecha de consulta y fuente primaria. Su análisis competitivo queda fuera de esta base de dominio.
- **Cifras de mercado**: eMarketer, CACE, AMVO, Ebanx/PCMI. En cada ficha, el año de los datos distinto del año de publicación, y las discrepancias entre fuentes declaradas.
- **Métricas públicas de plataformas**: el 10-K de Shopify como ficha modelo (segmentos, GMV, MRR, definiciones).
- **Regulación**: botón de arrepentimiento (Res. 424/2020), facturación ARCA e IVA de plataformas, y las equivalentes de otros países, con su estado de vigencia.
- **Herramientas y APIs**: versiones de las APIs de Shopify y similares.
- **Fuentes**: una ficha por fuente con su método, autoridad y límites. Baymard es la primera.

**Componentes sugeridos por nota [S]**: definición, para qué sirve, cómo se mide o evalúa, qué decisiones de producto toca, fuentes con marca [L]/[M]/[S] y autoridad, y huecos.

**Orden de trabajo sugerido**: primero cerrar los huecos grandes (headless/MACH, segmentos de comerciantes, otras regulaciones, informes globales). Después escribir las verticales conceptuales. Por último, las fichas fechadas.
