# Rubro autopartes, repuestos y accesorios para vehículos (Argentina): investigación severa (consulta 2026-11-22)

Alcance: repuesteros minoristas, casas de cubiertas y baterías, accesorios, repuestos de motos. Mide, no propone. Fuentes leídas el 2026-11-22 salvo que se diga otra fecha.

Marcas de lectura: **[L]** página abierta y leída con WebFetch; **[Lc]** página descargada con `curl` y leída en sus pasajes relevantes (se usó cuando WebFetch no podía verificar el dominio); **[S]** solo resumen del buscador. Calificación: fuente A (confiable) a F; dato 1 (confirmado por otra fuente independiente) a 6.

## 0. Respuesta primero

- **Cupo:** no se agotó el cupo de búsquedas. Hubo bloqueos: Google Play y App Store (no se pudieron abrir), la ayuda de costos de Mercado Libre (403 o contenido cargado por JavaScript), la comunidad de vendedores de Mercado Libre (sin respuesta), Reddit (403), `catalogosuap.com.ar` y `specparts.shop` (Cloudflare), `motor.com`, `wynges.com` y `preciosok.com.ar` (WebFetch no verificó el dominio). Por eso no hay reseñas de apps argentinas ni de la comunidad de Mercado Libre.
- **El dolor propio del rubro es la compatibilidad pieza–vehículo** (marca, modelo, año, motor, posición). Mercado Libre la resuelve con su propio catálogo de compatibilidades, la exige en las publicaciones marcadas con el tag `incomplete_compatibilities` «para evitar que las publicaciones de autopartes sean pausadas», y desde el 15/07/2026 deja de permitir por API editar o copiar las compatibilidades que gestiona su catálogo (fuente 1, [Lc]).
- **Para una tienda propia, las plataformas generales no traen filtro por vehículo.** Tiendanube filtra solo por categorías, variantes, marca y precio, y «no es posible agregar filtros adicionales de forma manual» (fuente 9, [L]). Shopify permite filtros por metacampos, con un tope de 25 filtros, 100 valores por filtro y sin filtros en colecciones de más de 5.000 productos, y su ayuda no menciona filtros dependientes ni búsqueda por vehículo (fuente 10, [L]). Lo resuelven apps de terceros.
- **Las apps traen el buscador, pero no los datos.** En Shopify, las 11 apps de «Year Make Model» revisadas dependen de que el comercio cargue las compatibilidades por CSV o a mano, o de proveedores de datos de EE. UU. (ACES/PIES, Turn 14, ShowMeTheParts). En Tiendanube hay una sola app (Peça Certa, ARS 10.593,62 por mes, 0 reseñas), que dice explícitamente que no trae base de vehículos (fuente 8, [L]).
- **Sí hay datos del parque argentino, pero se venden a la industria.** Promotive (la empresa que hace el informe del parque de AFAC) ofrece «TablaSpec + VIO» con el parque de «más de 19 países de Latinoamérica» y un «Catálogo 360 B2B / B2C», sin precio publicado (fuente 13, [Lc]). AFAC lanzó en 2020 el SUAP («Sistema Único de Autopartes»), un catálogo unificado de sus fabricantes asociados (fuente 14, [Lc]). Su estado actual y si alguien puede licenciarlo no se pudieron verificar. TecDoc no menciona Argentina (fuente 15, [L]).
- **Tamaño (fuerza media-baja):** entre 8.400 y 16.800 comercios minoristas de autopartes, con un centro de unos 11.000. Son 6.541 locales de empresas empleadoras más un tramo supuesto de monotributistas. La federación de cámaras del rubro dice representar a «más de 10.000 comercios» entre mayoristas y minoristas ([S]). Los que tienen tienda propia en Tiendanube son unos 1.111 en «Autos & Vehicles» en Argentina, según un rastreador de terceros (fuente 17, [Lc]).
- **Quejas: 77 reseñas de apps de compatibilidad en Shopify leídas una por una** (2017–2026, 17 negativas o mixtas), más 63 mensajes de 4 hilos de la comunidad de eBay. Entre las 17 negativas o mixtas, el tema principal es cargar los datos de compatibilidad (6), seguido de cobros (6) y fallas o resultados erróneos (5). Entre las positivas, casi todo es elogio al soporte. **Ninguna de las 77 es de Argentina**, solo una de Chile: no hay voz local de vendedores en lo leído.
- **Corrección al barrido previo:** el rubro no es 5.º. En el adelanto del Estudio Anual 2025 de CACE es **9.º por facturación y 6.º por unidades** (fuentes 2 y 3, [L]/[Lc], mismo comunicado).

## 1. Tamaño de abajo hacia arriba

| Paso | Cuenta | Resultado | Pieza que la sostiene |
|---|---|---|---|
| 1 | Locales de empresas empleadoras, autopartes al por menor (4532xx), 2022 | 6.541 (6.263 en 2021): repuestos nuevos 4.665; cubiertas 1.462; baterías 309; usados 105. 23.835 puestos, unos 3,6 por local | Dato de base, CEP XXI (A2, [L], suma de quien coordina) |
| 2 | Aparte: motos y sus partes (454010) | 1.325 locales (incluye la venta de motos, no solo de partes) | Dato de base |
| 3 | Aparte: mayoristas de autopartes (453100) | 2.146 locales | Dato de base |
| 4 | Locales por empresa | Las empresas empleadoras del CLAE 453 (mayor y menor) son 7.414 (oct. 2023), contra 8.687 locales (paso 1 + paso 3): **unos 1,17 locales por empresa** (inferencia, años distintos) | Dato de base |
| 5 | Empresas empleadoras minoristas | 6.541 / 1,17 ≈ **5.600** (inferencia) | Pasos 1 y 4 |
| 6 | Monotributistas sin empleados que venden repuestos | **No hay corte por actividad** (ARCA dio 404 en la ronda general). **Supuesto:** de 0,5 a 2 por cada empresa empleadora minorista, es decir entre 2.800 y 11.200. En el total de la economía, el censo da 1.138.346 monotributistas contra 273.176 empresas con fines de lucro (unos 4 a 1), pero un repuestero necesita stock y capital, así que se toma un tramo más bajo (supuesto) | INDEC CNE 2020/21 citado en `tamano-local-y-gestion.md` (A, [L] en esa nota) |
| 7 | Comercios minoristas de autopartes | 5.600 + (2.800 a 11.200) ≈ **8.400 a 16.800**, centro de unos 11.000 (cuenta por CUIT y no por local; inferencia) | Pasos 5 y 6 |
| 8 | Con tienda propia en Tiendanube | 1.111 tiendas en vivo de Argentina en la categoría «Autos & Vehicles» (13/11/2026). En el total de la categoría, que suma todos los países, el 53,8% son «Parts & Services» y el 15,5% «Motor Vehicles». Aplicando el 53,8%, **unas 600 tiendas de repuestos y servicios en Argentina** (inferencia: la proporción es del total, no de Argentina) | StoreLeads (fuente 17, C3, [Lc]) |
| 9 | Con sistema de gestión del rubro | Boxer Gestión dice tener «+600 Clientes», «Repuesteros activos en todo el país» (lo dice quien vende) | Fuente 18 (C, [L]) |
| 10 | Venden en Mercado Libre | **Sin dato.** La API pública de categorías y de costos respondió 403 («PolicyAgent») y la página de la categoría también dio 403 | Hueco |

**Cruce con vías independientes:**

- **La cámara.** FACCERA (Federación Argentina de Cámaras de Comerciantes en Repuestos del Automotor; 14 cámaras, fundada en 1978) «representa a más de 10.000 comercios de venta de repuestos instalados en toda la Argentina, incluyendo mayoristas y minoristas» (Taller Actual, edición Automechanika 2024, C4, [S]; el PDF pesa más de 10 MB y no se pudo abrir). Otra nota local le atribuye «más de 500 empresas» (diariolaopinion.com.ar, D4, [S]). Las dos cifras discrepan; la segunda probablemente cuenta las socias directas (**inferencia**). Los 10.000 cuadran con el rango del paso 7 sumado a unos 2.000 mayoristas.
- **El parque automotor.** 15.784.385 vehículos a fin de 2025, sin contar motos (82% autos, 15% comerciales livianos, 3% pesados), con una antigüedad promedio de 14,8 años, según AFAC (El Economista, 07/04/2026, B2, [L]; la cifra de 2024, 15.552.418, también la publica Infobae, [S]). Siete marcas suman el 86% del parque y 28 modelos el 50%. Sobre la antigüedad hay una discrepancia: El Economista dice que el 27,41% es anterior a 2006, y otro resumen dice que el 37,3% tiene más de 20 años ([S]). Orden de magnitud: entre 940 y 1.880 vehículos por comercio minorista (**inferencia**, sin comparación con otros países).

**Fuerza de la cifra: media-baja.** El piso (6.541 locales empleadores) es firme (A2). Los monotributistas son un supuesto de rango ancho. El cruce con la cámara cuadra en orden de magnitud, pero viene de una sola fuente gremial leída por resumen. Lo que vende online es un piso parcial (solo Tiendanube, con una proporción tomada del total de la categoría).

**La venta online del rubro:** «Accesorios para motos, autos y otros vehículos» es la 9.ª categoría por facturación y la 6.ª por unidades del comercio electrónico argentino en 2025. El total fue de $35.326.983 millones y 645 millones de unidades (CACE con Kantar, encuesta a unas 200 empresas socias; iProUP 05/02/2026 [Lc] y Mercado 06/02/2026 [L]: mismo comunicado, B3). El monto de la categoría no está publicado en lo leído.

**Cuánto pasa por Mercado Libre:** no hay dato argentino firme. Un resumen de una nota de DF Sud (probablemente de 2024) dice que autopartes es «la segunda categoría en ventas» de Mercado Libre, con más de 12 millones de visitas al mes, y que en Argentina las ventas subieron 61% después de una herramienta de compatibilidad (D5, [S]; la página dio 404). Hueco.

## 2. Cuánto pagan hoy

| Qué | Precio | Con o sin IVA | Fecha | Fuente |
|---|---|---|---|---|
| Mercado Libre, comisión de Accesorios para Vehículos | Clásica **13,0%**, Premium **18,5%**, «valores aproximados 2026» | Sin IVA (el IVA va aparte según las guías) | 2026 | Mellium10, calculadora de terceros (C4, [Lc]). Otro blog dice 14,5% y otra guía da un rango de 12% a 16% en Clásica ([S]). La página oficial no se pudo leer (403 o JavaScript): **hueco en fuente primaria** |
| Mercado Libre, costo fijo por unidad | Se cobra por debajo de un umbral de unos $33.000 (un blog dice $1.800) | — | 2026 | [S], D5 |
| Tiendanube, app Peça Certa (buscador por vehículo) | **ARS 10.593,62 por mes** (equivale a R$ 39,9), 3 días gratis | No dice | 22/11/2026 | Fuente 8 (B, [L]) |
| Tiendanube, filtros nativos | Incluidos, pero sin vehículo | — | — | Fuente 9 |
| Shopify, EasySearch (NexusMedia, Polonia) | US$ 19 y US$ 75 por mes | Sin impuestos locales | 22/11/2026 | Fuente 11 ([L] y [Lc]) |
| Shopify, C: Year Make Model Search (India) | Gratis solo en tienda de desarrollo; US$ 10, 50 y 75 por mes (anual: 96, 480 y 720) | Ídem | Ídem | Ídem |
| Shopify, PartFinder (GoVedia) | US$ 49 por mes | Ídem | Ídem | Ídem [Lc] |
| Shopify, Convermax | US$ 250, 450 y 850 por mes | Ídem | Ídem | Ídem [Lc] |
| Shopify, Standard Parts Toolkit (con datos ACES/PIES de EE. UU.) | US$ 300 por mes | Ídem | Ídem | Ídem [Lc] |
| Shopify, otras (Instant Fit, MSPL, WTS, Friends2a, Fitscar) | De US$ 2 a US$ 99,99 por mes | Ídem | Ídem | Ídem [Lc] |
| Boxer Gestión (gestión para repuesteros) | **No publica precio** («Consultar»; mensual, trimestral, semestral o anual) | — | 2026 | Fuente 18 ([L]) |
| Promotive, TecDoc (datos de compatibilidad) | **No publican precio** | — | — | Fuentes 13 y 15 |

**Ejemplo de cuenta (inferencia, con supuestos):** un repuestero que vende 100 piezas al mes de $60.000 en Mercado Libre Clásica paga 13% × $6.000.000 = $780.000, más IVA 21% = **unos $944.000 por mes**. El mismo volumen en una tienda propia de Tiendanube con Peça Certa paga $10.594 por mes de la app, además del plan de la tienda y del cobro del medio de pago (no medidos acá). Lo que la cuenta no ve es el trabajo de cargar a mano las compatibilidades, que en Mercado Libre se apoya en su catálogo.

## 3. De qué se quejan (reseñas leídas una por una)

**Qué se leyó:**

- **77 reseñas** de 10 apps de compatibilidad por vehículo en la Shopify App Store, sin duplicados. Por cada app se leyó la primera página de reseñas y la página filtrada a 1–3 estrellas, descargadas con curl y leídas una por una. Las apps: EasySearch (173 reseñas en total), C: Year Make Model Search (104), PartFinder (16), Convermax (15), Standard Parts Toolkit (7), MSPL (7), Instant Fit (6), WTS (4), Friends2a (4) y Fitscar (1). En la Channelmotive Parts Finder no aparecieron reseñas.
- Por estrellas: 60 de 5, 3 de 4, 2 de 3 y 12 de 1. Son **17 negativas o mixtas (1 a 4 estrellas con queja)**. Años: de 2017 a 2026, la mayoría de 2024 a 2026. Países: EE. UU., Canadá, Australia, Reino Unido y otros, con **una sola de Latinoamérica (Chile)**.
- **63 mensajes de 4 hilos de la comunidad de vendedores de eBay** (2022–2025) sobre piezas que «no entran». No son reseñas; se leyó cada mensaje en sus primeras líneas.
- **No se pudo leer:** Google Play y App Store (apps de catálogo argentinas como Wega o Mahle Argentina, que solo aparecieron en el buscador, del lado de iOS), la comunidad de Mercado Libre, Reddit (403) y la tienda de apps de Tiendanube (Peça Certa no tiene reseñas). **No hay quejas de vendedores argentinos en lo leído.**

**Las 17 negativas o mixtas, recodificadas a mano** (una reseña puede caer en más de un tema):

| Tema | n | Ejemplos |
|---|---|---|
| Datos de compatibilidad: la app no los trae, hay que cargar todo, el CSV sobrescribe lo que había, no se puede editar en lote | 6 | EasySearch 2026 (base vacía), EasySearch 2025 (CSV), WTS 2024 (no deja cargar datos; no hay borrado en lote), PartFinder 2017 (no trae modelos ni referencias cruzadas), Friends2a 2025 (mucha carga manual) |
| Cobros: caro, prueba gratis que no es tal, cobran sin funcionar | 6 | EasySearch 2021, 2025 y 2026; C: YMM 2025 (dos); MSPL 2023 |
| Falla o resultados erróneos | 5 | EasySearch 2024 (vehículos no relacionados) y 2025 (dejó de andar); Instant Fit 2024; MSPL 2025; WTS 2024 |
| Soporte que no responde | 2 | MSPL 2023 (dos meses), Fitscar 2023 (Chile) |
| No se adapta al tema de la tienda | 1 | Fitscar 2023 (Chile) |

**Las 60 positivas:** casi todas elogian el soporte o la rapidez de respuesta (56 de las 77 reseñas lo mencionan, contadas por palabra clave y revisadas). Aparecen también la personalización del buscador al diseño de la tienda y, en 5 casos (Standard Parts Toolkit y Convermax), el valor de tener **datos de compatibilidad precisos** de los fabricantes (ACES/PIES). **Inferencia:** en las reseñas, el soporte cubre a mano lo que el producto no resuelve solo (configurar, cargar datos, ajustar el tema).

**Temas de los hilos de eBay (63 mensajes):**

- El comprador no sabe qué vehículo tiene o carga mal su «Garage».
- Quién paga el envío de vuelta: «doesn't fit» cuenta como arrepentimiento y «doesn't fit my vehicle» entra en la garantía.
- El vendedor arma la compatibilidad por su cuenta y teme que se la cuenten como defecto.

**Citas textuales** (sin nombres; las de Shopify, de la reseña; las de eBay, del mensaje):

1. «doesnt work data base is empty and it cost way to much for this trash» (EasySearch, 1 estrella, 2026).
2. «Did I understood correctly, here is no models, no cross-references, this is clean windows where I need to build every think by myself?» (PartFinder, 3 estrellas, 2017; menciona que con TecDoc sí cruza su número con el modelo de vehículo).
3. «The inability to upload new CSVs without overwriting existing data severely limits scalability.» (EasySearch, 1 estrella, 2025).
4. «Year make model will show 15 different vehicles and products that are not related to your search.» (EasySearch, 1 estrella, 2024).
5. «The year-make-model search is only as good as your store's fitment data.» (Convermax, 5 estrellas, 2023).
6. «Before Standard Parts Toolkit, we struggled to find a turn key solution that could take ACES & PIES from the hundreds of brands that we sell» (5 estrellas, 2025).
7. «Fitment is built by the seller; ebay doesnt provide fitment» (comunidad de eBay, 2023).
8. «They don't know what vehicle they have...They don't know their options...They don't enter their vehicle in their "Garage".» (comunidad de eBay, 2024).

**Devoluciones por pieza equivocada:** **no hay dato argentino.**

- Lo que aparece es de EE. UU. y de proveedores: tasas de devolución de autopartes online del 18% al 20% como «promedio de la industria», según PARTS iD (que dice tener 5%), y «hasta 20%» según otro proveedor. También que «casi la mitad» de las devoluciones son por compatibilidad. Todo es D4/D5 y [S]; la nota de MOTOR (2023) no se pudo abrir.
- Una encuesta a compradores de AUTODOC (Europa): el 37% pidió la pieza equivocada y el 34% recibió una que no entraba ([S], C5).
- Mercado Libre México se propuso en 2021 «reducir hasta en un 40% las devoluciones de productos y los reclamos» con las compatibilidades. Es una meta, no un resultado (PortalAutomotriz 03/06/2021, C, [L]).

## 4. Quién atiende

| Quién | Qué cubre | Qué no cubre | Precio | Fuente |
|---|---|---|---|---|
| Mercado Libre (compatibilidades) | Catálogo de vehículos propio en AR, MX, BR, UY, CL y CO. Compatibilidad por producto o por dominio (marca, modelo, año, motor), posición y notas. Sugerencias automáticas («pending_compatibilities»). Gestor de Compatibilidades en el sitio. Obligatoria en ítems con el tag `incomplete_compatibilities`, bajo riesgo de pausa | Desde el 15/07/2026, la API solo da un resumen (marca y total) de las compatibilidades del catálogo: se aceptan todas las sugeridas o ninguna. Esas compatibilidades no se copian con copiar y pegar (solo las del vendedor) y el buscador de vehículos por API dejó de estar disponible. **Inferencia:** los datos de compatibilidad que pone Mercado Libre no se pueden llevar a otro canal | Incluido en la comisión (13% a 18,5%, terceros) | Fuente 1 [Lc], fuente 6 [L] |
| Tiendanube (nativo) | Filtros por categoría, variante, marca y precio | Filtro por vehículo; «no es posible agregar filtros adicionales» | Incluido | Fuente 9 [L]. El blog de Tiendanube promete «filtrado avanzado por modelo, marca o año» (14/05/2026), sin un artículo de ayuda que lo respalde (fuente 19, [L]) |
| Tiendanube, app Peça Certa (ElunaLab, origen brasileño según el dominio y la moneda) | Búsqueda por marca, modelo, año y motor; vincular aplicaciones a SKU; CSV; búsquedas sin resultado | Base de vehículos («no incluye una base precargada»); búsqueda por patente; 0 reseñas | ARS 10.593,62 por mes | Fuente 8 [L] |
| Shopify (nativo, Search & Discovery) | Filtros por metacampo o metaobjeto y por la taxonomía de categorías | No hay filtros dependientes en lo leído; máximo 25 filtros y 100 valores por filtro; sin filtros en colecciones de más de 5.000 productos | Incluido | Fuente 10 [L] |
| Shopify, 11 apps de «Year Make Model» | Buscador por vehículo, «My Garage», tabla de compatibilidad | Datos de compatibilidad (los carga el comercio), salvo las que conectan con proveedores de EE. UU. (Turn 14, Slingshot, ShowMeTheParts, ACES/PIES). Ninguna menciona Argentina | De US$ 2 a US$ 850 por mes | Fuente 11 |
| Promotive Group (Argentina y LATAM) | TablaSpec + VIO («parque vehicular de más de 19 países de Latinoamérica»), PartsMapping, Catálogo 360 B2B/B2C; hace el informe del parque de AFAC. Dice tener «+300 Clientes B2B» (lo dice quien vende) | Está pensado para fabricantes y distribuidores; no hay conector a una tienda del repuestero en lo leído | No publicado | Fuente 13 [Lc] |
| AFAC, SUAP (Sistema Único de Autopartes) | Catálogo unificado de fabricantes asociados (AG, Corven, DRiV, DZE, Ferrazzi, Fram, GEA, Juntas Illinois, Kessel, RM, Serrat, Taranto, Tiper, ZF): vehículos, piezas, equivalencias con OE e imágenes. Según un resumen, el sitio busca por patente | Estado actual, acceso y licencia sin verificar (el sitio respondió con Cloudflare). La nota es de 02/07/2020 | No publicado | Fuente 14 [Lc]; `catalogosuap.com.ar` [S] |
| TecAlliance (TecDoc) | Base mundial de piezas y vehículos (web service, catálogo y VIO en más de 75 países, «incluido Brasil» y «los principales mercados de Sudamérica» sin nombrarlos). Expuso en Automechanika Buenos Aires 2026 desde su filial de Brasil | Argentina no aparece nombrada; sin datos del parque argentino confirmados | No publicado | Fuente 15 [L], fuente 16 [S] |
| Catálogos de fabricantes | Wega (filtros por modelo de vehículo, web y app de iOS), Bosch (catálogo digital argentino con búsqueda por vehículo, 2023), Mahle Argentina (app de iOS con referencias cruzadas y modelos), Ferrazzi (catálogo descargable) | Solo su marca; para consultar, no para alimentar una tienda (lo leído no ofrece API) | Gratis para consultar | Wega y Ferrazzi [Lc]; Bosch y Mahle [S] |
| Boxer Gestión (sistema para repuesteros) | Stock, ventas, «automatización» de 5, 20 o 60 listas de precios de proveedores, equivalencias, factura ARCA. El plan Premium se integra con «MELI, WooCommerce, Tienda Nube y Más Pedidos». Dice tener «+600» repuesteros (lo dice quien vende) | No menciona catálogo por vehículo | No publicado | Fuente 18 [L] |
| Otros sistemas de gestión (Líder Gestión/Wynges, PreciosOK, Vehix) | Listas de precios por proveedor (PreciosOK descarga y procesa las listas); facturación | Compatibilidad, sin verificar | Wynges: «US$ 810» según Capterra, con datos discrepantes ([S]) | [S] |
| Tiendas multimarca con buscador propio (CotizaPartes; AutoCentral, que busca por patente) | Buscador por marca, modelo y año sobre su propio catálogo (CotizaPartes: 36.539 repuestos al 16/11/2026, 112 marcas de auto) | Son vendedores o comparadores, no proveedores de datos | — | CotizaPartes [Lc]; AutoCentral [Lc] (solo el título) |

## 5. Huecos con fuerza

1. **Datos de compatibilidad del parque argentino para la tienda propia del repuestero. Fuerza: media.** Lo que hay: las apps de las plataformas generales traen el buscador pero no los datos; Peça Certa lo dice explícitamente y las 11 apps de Shopify dependen del comercio o de datos de EE. UU. Los datos locales existen (Promotive, el SUAP de AFAC y los catálogos de cada marca), pero están pensados para fabricantes y distribuidores, sin precio publicado y sin conector a una tienda en lo leído. El tema que más se repite en las negativas de Shopify es la carga de datos (6 de 17). Por qué no es fuerte: no se leyó ninguna queja de un repuestero argentino, y no se sabe si Promotive o AFAC le venden datos a un comercio chico.
2. **No hay filtro por vehículo nativo en las plataformas generales. Fuerza: fuerte en el hecho, débil en la queja.** Lo dicen las ayudas oficiales: Tiendanube no permite filtros adicionales y Shopify no tiene filtros dependientes, con topes de valores y de productos. Que los comercios argentinos lo reclamen no aparece en lo leído.
3. **Encierro en Mercado Libre de los datos de compatibilidad. Fuerza: media.** Las compatibilidades del catálogo de Mercado Libre no se pueden leer en detalle ni copiar por API desde el 15/07/2026, y son obligatorias para no pausar publicaciones. **Inferencia:** el trabajo de compatibilidad que se hace en Mercado Libre no se puede llevar a una tienda propia. No hay quejas leídas que lo confirmen (la comunidad de Mercado Libre no se pudo abrir).
4. **Devoluciones por pieza equivocada. Fuerza: débil.** No hay dato argentino. El problema existe afuera (eBay creó «Guaranteed Fit» para autopartes, y en sus foros los vendedores discuten quién paga el envío de vuelta), pero las cifras son de proveedores.
5. **Listas de precios de muchos proveedores, con aumentos frecuentes. Atendido**, no es un hueco: Boxer, PreciosOK y Líder Gestión lo cubren. Se anota porque es el otro dolor operativo del rubro que aparece en lo leído.

## 6. Lo que puede cerrar un hueco desde arriba

- **Mercado Libre:** ya cierra la compatibilidad dentro de su marketplace (catálogo propio, sugerencias automáticas, obligación con pausa). Las restricciones de API de julio de 2026 refuerzan que los datos queden adentro.
- **Tiendanube:** su blog del 14/05/2026 promete «filtrado avanzado por modelo, marca o año», pero su ayuda dice que no se pueden agregar filtros. Hoy hay una sola app del rubro en su tienda. Señal débil.
- **Shopify:** en septiembre de 2024 sumó filtros por metacampos de categoría con su taxonomía estándar ([S], changelog). Su ecosistema de apps del rubro es grande (78.297 tiendas «Autos & Vehicles» en el mundo, según StoreLeads [Lc]), pero de datos de EE. UU.
- **Promotive o AFAC:** tienen los datos del parque argentino y un «Catálogo 360 B2C». Si abrieran un conector a tiendas, cerrarían el hueco 1. No hay señal leída de que lo hagan para comercios chicos.
- **TecAlliance:** está presente en la feria argentina desde Brasil; su VIO cubre «los principales mercados de Sudamérica». Señal débil para Argentina.
- **Sistemas de gestión (Boxer):** ya se integran con Tiendanube y Mercado Libre. Si sumaran equivalencias por vehículo, llevarían datos a la tienda. Sin señal leída.

## 7. Evidencia para criterios (sin puntuar)

- **¿Pagan hoy y se quejan?** Pagan comisiones en Mercado Libre (13% a 18,5% según terceros) y suscripciones de gestión (sin precio publicado). En Tiendanube, la única app de vehículo no tiene reseñas ni, por lo tanto, quejas. En Shopify pagan de US$ 10 a US$ 850 por mes y se quejan sobre todo de cargar datos y de los cobros. Queja local: no encontrada.
- **¿Quién decide y cómo se llega?** Decide el dueño del repuestero. Lo que los junta:
  - FACCERA: 14 cámaras, «más de 10.000 comercios» según ella misma.
  - AFAC, la cámara de fabricantes, con su SUAP.
  - Medios del rubro (Taller Actual) y la feria Automechanika Buenos Aires.
  - Distribuidores y mayoristas: 2.146 locales.
  - Los sistemas de gestión: Boxer dice tener 600 repuesteros.
- **¿Depende de un solo tercero?** En Mercado Libre, de su API y su catálogo (las reglas cambiaron el 15/07/2026). Para datos del parque argentino, de muy pocos actores (Promotive, los fabricantes de AFAC); en lo leído no hay alternativa abierta.
- **¿Hay una opción gratis que hace lo central?** Dentro de Mercado Libre, sí: las compatibilidades están incluidas y el catálogo pone los datos. Para la tienda propia, no: los filtros nativos no filtran por vehículo, y la única app gratis de Shopify sirve solo en tiendas de desarrollo. Para consultar una pieza, los catálogos de marca (Wega, Bosch) son gratis, pero de a una marca.

## 8. Lo que no se sabe

1. La comisión oficial de Mercado Libre para Accesorios para Vehículos: la página de costos no se pudo leer (403 o JavaScript) y la API pública respondió 403.
2. Cuántos vendedores o publicaciones hay en la categoría en Mercado Libre Argentina, y qué parte de la venta online de autopartes pasa por ahí.
3. Los monotributistas por actividad (ARCA): todo el tramo sin empleados es un supuesto.
4. Si el SUAP de AFAC sigue activo y si se licencia; el precio de Promotive y de TecDoc; si TecDoc cubre el parque argentino.
5. Las reseñas de apps de catálogo argentinas (Google Play y App Store no se abrieron) y las quejas de la comunidad de Mercado Libre sobre compatibilidades.
6. Una tasa de devolución por pieza equivocada en Argentina.
7. El monto facturado por la categoría en el estudio de CACE 2025 (solo se publicó el puesto).
8. El parque de motos (el informe de AFAC las excluye) y los datos para repuestos de motos.
9. Cuántas de las 1.111 tiendas de Tiendanube de «Autos & Vehicles» en Argentina son repuesteros con local.

## 9. Fuentes

1. Mercado Libre Developers, «Compatibilidades entre ítems y productos de Autopartes», última actualización 12/11/2026. https://developers.mercadolibre.com.ar/compatibilidades-entre-items-y-productos (WebFetch dio 403; se leyó con curl la versión `/es_ar/`) — A1 (el resumen del buscador coincide), [Lc]. Versión en inglés: https://developers.mercadolibre.com.ar/en_us/compatibility-between-items-and-vehicle-accessories (403).
2. iProUP, «Por qué el ecommerce creció por encima de la inflación en la Argentina en 2025», 05/02/2026. https://www.iproup.com/economia-digital/64641-por-que-el-ecommerce-crecio-por-encima-de-la-inflacion-en-la-argentina-en-2025 — B3, [Lc] (WebFetch trajo solo el título). La nota dice «unidades en 2021», un error evidente de la nota.
3. Mercado, «CACE: el eCommerce facturó $35.326.983 millones en 2025 y subió 60%», 06/02/2026. https://mercado.com.ar/tendencias/cace-el-ecommerce-facturo-35-326-983-millones-en-2025-y-subio-60 — B3, [L]. Es el mismo comunicado que la fuente 2: una sola fuente.
4. UpSeller, «Mercado Libre – Compatibilidad de autopartes». https://www.upseller.com/es/doc-article/1906-Mercado-Libre-Compatibilidad-de-autopartes — C3, [L].
5. PortalAutomotriz, «Mercado Libre ayuda a los vendedores con nuevas herramientas de compatibilidades» (México), 03/06/2021. https://www.portalautomotriz.com/print/noticias/automotriz/mercado-libre-ayuda-a-los-vendedores-con-nuevas-herramientas-de-compatibilidades — C4, [L].
6. Mellium10, «Ganancia Neta MercadoLibre Argentina — Accesorios para Vehículos 2026». https://melium10.com/herramientas/calculadora-ganancia-neta-mercadolibre/argentina/accesorios-para-vehiculos — C4, [Lc]. Otros sin primaria: https://digitalsellers.com.ar/blog/comisiones-mercado-libre/ ([L], sin cifras), https://gestodo.net/blog/comisiones-mercado-libre-argentina-2026-guia-completa-para-vendedores ([S], 14,5%).
7. API de Mercado Libre `sites/MLA/listing_prices` y `categories`: respondió 403 «PolicyAgent» (22/11/2026). Ayuda de costos https://www.mercadolibre.com.ar/ayuda/Costos-de-vender-un-producto_870: 403 con WebFetch; con curl, contenido cargado por JavaScript.
8. Tiendanube, tienda de aplicaciones, «Peça Certa». https://www.tiendanube.com/tienda-aplicaciones-nube/peca-certa — B (dato de la propia ficha), [L].
9. Centro de Atención Nube, «Qué son los filtros y cómo habilitarlos en mi tienda». https://ayuda.tiendanube.com/es_MX/que-son-los-filtros-y-como-habilitarlos-en-mi-tienda — A2, [L] (versión de México de la misma plataforma).
10. Shopify Help Center, «Adding filters». https://help.shopify.com/en/manual/online-store/search-and-discovery/filters — A2, [L]. Changelog de los metacampos de categoría: https://changelog.shopify.com/posts/storefront-filters-now-support-category-metafields — [S].
11. Shopify App Store, fichas y reseñas (descargadas el 22/11/2026): https://apps.shopify.com/easysearch ([L] la ficha; reseñas [L] y [Lc]), https://apps.shopify.com/year-make-model-advance-search ([L] y [Lc]), https://apps.shopify.com/automotive-part-search ([L] y [Lc]), https://apps.shopify.com/year-make-model-fitment-search ([L] y [Lc]), https://apps.shopify.com/year-make-model-app, https://apps.shopify.com/fitment-tool, https://apps.shopify.com/standard-parts-toolkit, https://apps.shopify.com/make-model-year, https://apps.shopify.com/fitscar, https://apps.shopify.com/friends2a-ymm-partfinder, https://apps.shopify.com/channelmotive-part-finder (todas [Lc]). Reseñas: B para el texto (cada una es la voz de un comercio) y C para los totales.
12. Comunidad de eBay, 4 hilos: https://community.ebay.com/forum/selling-57920/topic/buyers-claim-part-doesnt-fit-128858/ (2024), https://community.ebay.com/t5/Selling/New-Return-Policy-Seller-Protections-For-Parts-amp-Accessories/td-p/33154160 (2022–2023), https://community.ebay.com/t5/Buying/Guaranteed-Fit-program-challenges-with-seller/m-p/35010382 (2025), https://community.ebay.com/t5/Returns/Doesn-t-fit/td-p/33476363 (2023) — C (foro), [Lc]. Programa: https://www.ebay.com/sellercenter/protections/ebay-guaranteed-fit — [Lc] (solo el menú; el contenido no se leyó).
13. Promotive Group, página de inicio. https://promotive.com.ar (redirige a promotive.la) — C (habla de sí misma), [Lc].
14. Taller Actual, «SUAP – Sistema Único de Autopartes», fuente AFAC, 02/07/2020. https://talleractual.com/suap-sistema-unico-de-autopartes/ — B4 (comunicado de la cámara), [Lc]. Sitio: https://catalogosuap.com.ar/ — 403 (Cloudflare); su descripción solo por el buscador [S].
15. German Pavilion, Automechanika Buenos Aires 2026, ficha de TecAlliance do Brasil. https://automechanika-argentina.german-pavilion.com/en/sites/exhibitors/135771 — B4, [L].
16. Comunicados de TecAlliance (VIO en 77 países; México; 9,8 millones de artículos de más de 1.000 marcas) — [S], C5.
17. StoreLeads, «Autos & Vehicles stores on Tiendanube», actualizado el 13/11/2026. https://storeleads.app/reports/tiendanube/category/Autos%20&%20Vehicles — C3 (rastreador de terceros, método no leído), [Lc]. Shopify mundial: https://storeleads.app/reports/shopify/category/Autos%20&%20Vehicles — [Lc].
18. Boxer Gestión, «Software para Casas de Repuestos en Argentina». https://boxergestion.com/sistema-gestion-casas-de-repuestos y https://boxergestion.com/planes — C (habla de sí misma), [L].
19. Tiendanube Blog, «Cómo iniciar un negocio de autopartes online», actualizado el 14/05/2026. https://www.tiendanube.com/blog/como-iniciar-negocio-de-autopartes/ — C (marketing), [L].
20. El Economista, «En Argentina hay 15,8 millones de vehículos y su edad promedio es 14,8 años», 07/04/2026, sobre un informe de AFAC. https://eleconomista.com.ar/autos/en-argentina-hay-158-millones-vehiculos-su-edad-promedio-148-anos-n93924 — B2, [L]. Cifra de 2024: https://www.infobae.com/economia/2025/06/05/un-informe-privado-revela-cuantos-vehiculos-circulan-por-el-pais-y-preocupa-el-envejecimiento-del-parque-automotor/ — [S].
21. FACCERA: Taller Actual, edición Automechanika 2024 (PDF de más de 10 MB, no se abrió). https://talleractual.com/media/revista/taller-actual-periodico/taller-actual-automechanika-2024.pdf — C4, [S]. Diario La Opinión (Rafaela), «El mercado de repuestos automotor muestra una mayor competencia». https://diariolaopinion.com.ar/locales/el-mercado-de-repuestos-automotor-muestra-una-mayor-competencia.htm — D4, [S].
22. Dato de base CEP XXI, «Distribución geográfica de los establecimientos productivos» y empleadoras por CLAE3. https://cdn.produccion.gob.ar/cdn-cep/establecimientos-productivos/Datos_por_departamento_y_actividad.csv — A2, [L] (suma de quien coordina; ver `rubros-conteo-propio.md`).
23. Wega, sitio con catálogo por modelo de vehículo. https://www.wega.com.ar/ — B, [Lc]. Ferrazzi, catálogo descargable: https://www.ferrazzi.com.ar/ — B, [Lc]. Bosch, catálogo digital en Argentina (Autoweb, 2023): https://www.autoweb.com.ar/?p=41543 — [S]. Mahle Argentina, app de catálogo en iOS: https://apps.apple.com/us/app/-/id1544271375 — [S] (App Store bloqueada).
24. CotizaPartes, inicio (36.539 repuestos, actualizado el 16/11/2026). https://cotizapartes.com/ — C (habla de sí misma), [Lc]. AutoCentral: https://www.autocentral.ar/ — [Lc], solo el título («Buscá autopartes por patente en Argentina»).
25. Devoluciones: X-Cart, PARTS iD, AUTODOC y otros, citados por el buscador (sin metodología). https://www.motor.com/2023/11/auto-parts-return-rates-rank-as-the-highest-in-retail-how-e-commerce-options-aim-to-drop-that-number/ (no se pudo abrir) — D5, [S].
26. DF Sud, nota sobre la herramienta de autopartes de Mercado Libre (probablemente de 2024). https://dfsud.com/america/mercado-libre-lanza-nueva-herramienta-para-impulsar-la-compra-de (404 al abrir) — D5, [S].
