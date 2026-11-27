# Vidrieras a medida en Argentina: quién las construye y cuánto cuestan

Fecha de consulta de todo: 2026-11-22. Calificación: fuente A a F (A = primaria, oficial o medición propia; D = quien vende el servicio hablando de sí; E-F = opinión suelta), dato 1 a 6 (1 = confirmado por varias vías; 6 = no se puede juzgar). Marcas: [L] leído entero o medido (WebFetch devuelve un resumen del modelo sobre la página; el navegador real y curl devuelven el texto o el HTML crudo), [S] resumen del buscador o fuente secundaria.

Método: directorios de socios leídos con navegador real (Playwright, script `leer-pagina.mjs`) o por su API pública cuando la página la usa (VTEX); perfiles de Clutch con WebFetch; detección de tecnología con **una sola** petición GET a la portada de cada sitio (curl), leyendo encabezados y HTML: `x-powered-by: Next.js`, `__NEXT_DATA__`, `x-vtex-*`, `faststore`, `mitiendanube`, `demandware`, etc. Unas 9 búsquedas web, cupo no agotado. No se cargó ningún sitio ni se pidió presupuesto. No se recomienda nada.

El barrido liviano anterior (`lind-negocio`, `el-taller/analisis/2026-11-22-el-bosque/motor-para-vidrieras-a-medida.md`) ya trae los precios de los motores (Medusa, Saleor, Vendure, commercetools), IURCO, Kudos, Valtech y Devups. Acá no se repiten; se citan.

## Respuesta primero

- **Quién construye.** En Argentina hay dos ofertas de agencia bien distintas. Arriba, 18 integradores de VTEX con operación en el país (3 Diamond, 2 Gold, 13 Silver, según la API del directorio de VTEX) y 11 socios de Shopify con sede en Argentina (3 Plus, 1 Premier, 7 Select). Abajo, 22 especialistas en desarrollo de Tiendanube y unas 151 empresas que Clutch lista para comercio electrónico en el país, casi todas de software general. [A/2, L]
- **Headless declarado es raro.** Ningún socio argentino de Shopify marca "Headless development" (el filtro da 0 sobre 11). Entre los integradores de VTEX, solo IURCO e Innew lo nombran en su sitio. Lo que sí aparece es headless *hecho*, no anunciado: POW arma vitrinas en Next.js con API propia para Cheeky y Paula Cahen d'Anvers, y Cetrogar corre sobre FastStore de VTEX. [A/2, L para la detección; D/4 para lo que dicen las agencias]
- **Marcas con vitrina a medida detectada:** de 51 portadas revisadas, 6 sirven Next.js (Frávega, Cetrogar, Sodimac, Cheeky, Paula Cahen d'Anvers y Tienda BNA, esta sobre la plataforma de Avenida+ para bancos) y 5 más tienen un frente propio sin plataforma reconocible (Coto, Megatone, Grimoldi, Havanna, Kevingston). El resto de las grandes está en VTEX con su vitrina estándar (IO). [A/3, L]
- **Cuánto cobran:** casi nadie publica precio. Clutch da tarifas por hora: de 30 empresas argentinas leídas, 16 cobran US$ 25 a 49 y 10 cobran US$ 50 a 99. La única tabla publicada es de un solo proveedor (Develop Argentina) que se contradice: US$ 1.500 a 3.000 por una tienda a medida básica en junio de 2026 y US$ 8.000 a 20.000 en marzo. [C/3 y D/5]
- **Costo de abajo hacia arriba (supuestos marcados):** una vitrina chica (1,5 personas, 3 meses) cuesta unos **US$ 14.000 a 20.000** con equipo propio o **US$ 18.000 a 36.000** con agencia a tarifa Clutch; una mediana (4,75 personas, 4 meses), **US$ 53.000 a 75.000** propia o **US$ 76.000 a 150.000** con agencia. Mantenerla cuesta **US$ 1.700 a 2.600 por mes** (media persona) en el caso chico y **US$ 4.600 a 8.300 por mes** (1,5 a 2 personas) en el mediano, sin contar la licencia del motor.
- **Mantener:** la única fuente que no vende headless y lo cuantifica en algo es Shopify, que vende las dos cosas: "A headless storefront costs more to build and run than a theme" y pide que el comercio "has developers to maintain the storefront after launch". Horas por mes: no hay ninguna fuente independiente. [A/2, L]
- **Migraciones:** los casos públicos van **hacia plataforma** más que hacia afuera: Bensimon (Magento, con costo de $1,5 a 3 millones por mes) y Selú (VTEX) pasaron a Tiendanube Evolución; Oggi figura como caso Shopify de POW y hoy corre en Tiendanube. Hacia lo a medida, el caso documentado es Frávega, que en VTEX desde 2014 armó su propio frente en React y dejó el carrito y el checkout en VTEX. Una agencia (LOP) ofrece hasta 6 meses sin licencia a quien deje VTEX por Shopify Plus antes del 31-dic-2026.

## 1. Agencias y estudios

### 1.1 Directorios oficiales: cuántos son

| Directorio | Qué cuenta | Cifra | Fuente | Calif. |
|---|---|---|---|---|
| VTEX, System Integrators | integradores con "ar" entre sus países | 18 de 244 en el mundo: Diamond 3, Gold 2, Silver 13 | API pública que usa la página: `https://www.vtex.com/api/si-portal/v2/system-integrators?lang=en&page=1&limit=500` | A/2 [L] |
| VTEX, niveles del programa | lo que paga la agencia | Silver US$ 500 por mes "or earn it", Gold US$ 2.000 por mes "or earn it", Diamond "Earn it" (no se compra); el directorio con logo es desde Silver | https://vtex.com/en-us/system-integrators/ | A/2 [L] |
| Shopify Partner Directory, "Creación de tiendas", ubicación principal Argentina | socios con sede en el país | 11: Plus 3, Premier 1, Select 7 | https://www.shopify.com/ar/partners/directory/services/store_building?location=AR | A/2 [L] |
| Idem, filtro "Headless development" | socios argentinos con esa especialidad | 0 (sin el filtro de país, la misma consulta devuelve una página llena) | `...store_building?location=AR&service=headless_development` | A/3 [L]; el filtro se leyó en el HTML, no en la interfaz |
| Tiendanube, Especialistas, servicio "Desarrollo" | especialistas que ofrecen desarrollo | 22, todos los de la primera página en Buenos Aires | https://www.tiendanube.com/especialistas/servicios/desarrollo | A/2 [L] |
| Clutch, "E-commerce developers", Argentina | empresas listadas | 151 (las primeras posiciones son pagas y no todas tienen sede acá) | https://clutch.co/ar/developers/ecommerce | C/3 [L] |

Lectura: el directorio de VTEX tiene una API abierta y se puede contar entero; los otros se cuentan por página. Ninguno mide cuántas vitrinas headless hicieron.

### 1.2 Quiénes son (lo que dicen de sí mismos)

Todo lo de esta tabla es **lo que la agencia dice de sí** (D/4) salvo el nivel de socio, que lo da la plataforma (A/2), y la tarifa de Clutch, que la carga la agencia en Clutch (C/3).

| Agencia | Ciudad | Plataformas | Headless o vitrina propia | Clientes públicos | Tamaño | Fuente |
|---|---|---|---|---|---|---|
| Known Online | Buenos Aires; oficinas en Chile, Ecuador, Uruguay y EE. UU. | VTEX (Diamond), Shopify, Magento, AEM; Next.js en Clutch | no lo dice en el sitio | AB InBev, Levi's Argentina, Carter's, Cummins, Komatsu, Falabella, Mercado Libre (logos y casos) | Clutch: 50-249, fundada 2011, US$ 25-49/h | knownonline.com; clutch.co/profile/known-online |
| Pierce Commerce | Buenos Aires, Lima, EE. UU. | solo VTEX (Diamond) | no | Frávega, Motorola, LG, Provincia Compras, Carrefour, Farmacity, Rutini, Newsan | sin dato | piercecommerce.com |
| Infracommerce | Brasil y Argentina | VTEX (Diamond) | no leído | no leído | sin dato | API de VTEX |
| Innew | CABA, Resistencia, Ciudad de México, Asunción | "especialización 100% en VTEX, con más de 12 años como Partner Certificado"; nombra headless | sí, lo nombra | Crocs, Stanley, Personal, New Balance, Tommy Hilfiger, Guess (logos) | sin dato | innew.net |
| We Are | Argentina | VTEX (Gold) | no leído | no leído | sin dato | API de VTEX |
| IURCO | Buenos Aires | Magento, VTEX, Shopify, Tiendanube | "headless ecommerce on Magento + Next.js, live in ~4 weeks" (Pampa Commerce); FastStore y Shopify "~2 weeks" (Ceibo Commerce) | no nombra | "130+ projects", 15 años | iurco.com/llms.txt (ya en el barrido) |
| POW | 5 países de LATAM (sin ciudad) | VTEX (Silver), Shopify | vitrinas en Next.js con API propia (detectado en Cheeky y Paula Cahen d'Anvers, ver sección 2) | Cheeky, Paula Cahen d'Anvers, 47 Street, Markova, Oggi | "+50" personas, "+10 años", "+25" marcas | pow.la |
| Fulljaus | Buenos Aires | VTEX (Silver), Shopify, Tiendanube; integra Magento, WooCommerce, PrestaShop | no | Pardo, Megatone, Cetrogar, Hisense, LG, Tienda Macro, Tienda Galicia | "+8 años"; implementación "30–60 días" | fulljaus.com |
| Kudos Commerce | Córdoba y Mar del Plata | VTEX (Silver), Magento | no | sin reseñas en Clutch | Clutch: 10-49, fundada 2002, US$ 25-49/h, mínimo US$ 5.000 | clutch.co/profile/kudos-commerce |
| Otros Silver de VTEX en AR | sin leer | Arbusta, Cruce, Goldben, Inbound Digital, Lindo Software, MADE OF, Nomada Digital, Red Clover, Solucionet | | | | API de VTEX |
| LOP Multimedia | CABA | Shopify Plus | no lo menciona | Crocs, Columbia, Sodastream, Kappa, Salomon, Kinderland (verificados por Shopify) | 11-50 personas, socio desde 2017 | perfil de Shopify; lop.global |
| Wualá | Córdoba | Shopify Plus, Tiendanube, PrestaShop | no | Bardahl, TotalEnergies, Repuestos Samsung | 11-50, "+500 proyectos" | perfil de Shopify; wuala.net |
| Innovate Group | Capital Federal | Shopify Plus; también especialista de Tiendanube | no en Shopify | migró Selú de VTEX a Tiendanube Evolución (ver sección 4) | 11-50, socio desde 2017 | perfil de Shopify; tiendanube.com/especialistas/innovate-group2 |
| VN Studios | CABA | Shopify (Premier) | ofrece "Custom app and API development" | Stanley 1913 Argentina, Vaja, Ruti, Vondom Argentina | 11-50, socio desde 2016 | perfil de Shopify |
| Combinatoria | CABA | Shopify (Select) | no | bodegas: Susana Balbo, Norton, Trivento, Colomé | 11-50 | perfil de Shopify; combinatoria.wine |
| Tikun Olam Media | Buenos Aires | Shopify (Select) | "Custom storefronts, checkout extensions, B2B" | sin dato | 1-10; "No acepta nuevos clientes" | perfil de Shopify |
| Otros Select de Shopify | CABA, Campana, Tucumán | Bue Studio, Lirogo Digital, Romolabs, HOTY, un consultor independiente | no | | 1-10 cada uno | perfiles de Shopify |
| Estudio Volando | Buenos Aires | Tiendanube (Titanium) | no | "613 Clientes", "Más de 550 reseñas" | sin dato | tiendanube.com/especialistas/estudiovolando |
| Guanaco Studio, Zurbrand, Software Studio, L2Consultores, MANADA | Buenos Aires | Tiendanube | no leído | Zurbrand hizo el diseño y desarrollo de Bensimon (sección 4) | | directorio de Tiendanube |
| Valtech, IT Globers, Apply Digital, Vinneren, Kpi Digital | regionales ("LATAM") | VTEX Diamond | Valtech busca líder VTEX remoto desde AR (barrido) | | | API de VTEX |
| Avenida (Avenida+) | sin ciudad | plataforma propia para tiendas de bancos | vitrina en Next.js detectada en Tienda BNA | Banco Nación, Macro, Supervielle, Comafi, Ciudad, Brubank | sin dato | avenidamas.com |

Huecos de la tabla: tamaño en LinkedIn (no se leyó: pide sesión); GoodFirms y el directorio de socios de Adobe (no se leyeron); los Silver de VTEX y la segunda página de Tiendanube (no se abrieron uno por uno).

### 1.3 Clutch: tarifas por hora de las empresas con sede en Argentina

Se leyeron 33 perfiles de la lista de 151 (las primeras posiciones de las dos mitades de la página). Se descartan 3 pagos sin sede en Argentina (Blue Badger, Techgropse, Chop-Chop). Quedan 30.

| Tarifa por hora | Empresas | Ejemplos (ciudad, mínimo de proyecto) |
|---|---|---|
| US$ 25-49 | 16 | Serfe (Santo Tomé, US$ 10.000+), eCloud Agency (Rosario, 25.000+), Fuzzy Fish (Córdoba, 10.000+), Outside the Box (Córdoba, 10.000+), Ibisdev (Buenos Aires, 5.000+) |
| US$ 50-99 | 10 | GM2 (Buenos Aires, 50.000+), Revolt (Buenos Aires, 25.000+), onGlobal (Tandil, 10.000+), Loop3 (Olivos, 10.000+), Odiseo (Villa Crespo, 1.000+, trabaja Sylius) |
| US$ 150-199 | 1 | Mira Commerce (Santa Fe, 75.000+; BigCommerce y Shopify) |
| no publica | 3 | United Virtualities, Portinos, Agencia Buffalo |

Más Kudos y Known Online, ambas en US$ 25-49 (sus perfiles). Fuente: https://clutch.co/ar/developers/ecommerce, C/3 [L]. La tarifa la carga la agencia; Clutch no la verifica (inferencia: no dice que lo haga). Casi ninguna es especialista en comercio: el comercio pesa entre 10% y 50% de su mezcla de servicios.

## 2. Marcas argentinas: qué vitrina tienen

Una petición a la portada, 2026-11-22. "Next.js" = encabezado `x-powered-by: Next.js` o rutas `/_next/`. "VTEX IO" = encabezados `x-vtex-*` con `vstore`. "FastStore" = encabezado `x-vtex-janus-router-backend-app: faststore-...`. A/3 [L] para lo detectado; lo que hay detrás se marca aparte.

### 2.1 Vitrina a medida o desacoplada

| Marca | Rubro | Lo detectado | Lo que hay detrás | Quién la hizo |
|---|---|---|---|---|
| Frávega | electro | Next.js (`buildId` en `__NEXT_DATA__`), CloudFront; `apiShopping: https://www.fravega.com/api/v2` y `checkoutApiEndpoint: https://www.fravega.com/chk-api/api/v1`; Contentful mencionado | según VTEX, usa VTEX "since 2014"; frente propio en React con "proprietary React-based CMS", carrito, checkout y backend en VTEX. En el HTML no aparece ninguna marca de VTEX: el checkout pasa por un dominio propio. [C/3, S: caso de VTEX leído en casestudies.com] | equipo propio ("Frávega Tech" figura como unidad de negocio en su sitio corporativo, según el buscador [S]); Pierce Commerce la lista como cliente |
| Cetrogar | electro | Next.js + `x-vtex-janus-router-backend-app: faststore-prod-...` | VTEX FastStore (la vitrina headless oficial de VTEX) | Fulljaus la lista como cliente (sin decir qué hizo) |
| Cheeky | indumentaria infantil | Next.js (app router), `api-cheeky-prod.pow.la`, `cheeky.powcdn.com`, `mdl-cheeky.azurewebsites.net` | API de POW; motor detrás no visible | POW (caso en su sitio) |
| Paula Cahen d'Anvers | indumentaria | Next.js (app router), `paula.powcdn.com` | idem | POW ("PCDA": separó sus dos sitios) |
| Tienda BNA | tienda de banco | Next.js, Cloudflare, `statics.avenida.com` | plataforma de Avenida+ | Avenida+ |
| Sodimac Argentina | hogar | Next.js, Cloudflare | plataforma del grupo dueño (inferencia, no verificada) | sin dato |
| Coto Digital | supermercado | SPA (`<base href="/">`), nginx, buscador Constructor | desarrollo propio (inferencia: ninguna plataforma reconocible) | sin dato |
| Megatone | electro | Vue y jQuery servidos desde `/next/files/`, servidor "GenericServerI" | desarrollo propio (inferencia) | Fulljaus la lista como cliente |
| Grimoldi | calzado | `x-powered-by: ASP.NET` | desarrollo propio (inferencia) | sin dato |
| Havanna | alimentos | jQuery y Bootstrap propios, nginx | desarrollo propio (inferencia) | sin dato |
| Kevingston | indumentaria | estáticos en `kvnstatic.com`, Cloudflare | desarrollo propio (inferencia) | sin dato |

### 2.2 En una plataforma con su vitrina estándar (para comparar)

| Plataforma | Marcas detectadas |
|---|---|
| VTEX IO (vitrina estándar) | Carrefour, Jumbo, Farmacity, On City, Easy, Arredo, Levi's, Naldo, Sportline, Mimo, Fila, 47 Street, Provincia Compras |
| Salesforce Commerce Cloud (`demandware`) | Dexter, Stock Center, Moov |
| Magento | Rapsodia, Prüne, Solo Deportes |
| Tiendanube | Selú, Bensimon, Oggi |
| WordPress | Compumundo |
| Fuera de comparación | Mercado Libre (plataforma propia de marketplace), Newsan (sitio institucional), Naranja X (financiera), Samsung (no se leyó) |
| Sin lectura | Tienda Naranja, Garbarino, Lacoste, Changomás, Tramando, Personal (sin respuesta); Adidas, Nike, Despegar, Hot Sale, María Cher (403); Musimundo ("Sitio en mantenimiento") |

Lectura: de 51 sitios, 11 tienen vitrina a medida o desacoplada, y de esos solo 2 dejan ver un motor de terceros detrás (VTEX en Cetrogar; VTEX en Frávega según VTEX, no según el HTML). La muestra la eligió esta investigación entre marcas conocidas: no es representativa. Inferencia: la vitrina a medida se ve en electro, supermercados, bancos y en la cartera de una agencia (POW), no como oferta general.

## 3. Cuánto cuesta

### 3.1 Lo publicado

| Quién | Qué | Precio | Plazo | Calif. |
|---|---|---|---|---|
| Develop Argentina, catálogo | "Tienda online" | "desde AR$ 890.000" o "desde US$ 640"; se paga con seña; pesos al dólar MEP | no dice | D/4 [L], developargentina.com/precios |
| Develop Argentina, blog 25-jun-2026 | tienda a medida básica / con ERP y facturación / marketplace / "enterprise con API propia" | US$ 1.500-3.000 / 3.000-6.000 / 6.000-15.000 / 15.000+ | 4-8 / 8-16 / 16-32 semanas / 6+ meses | D/5 [L], sin método |
| Develop Argentina, blog 28-mar-2026 | a medida básica / intermedia (con ARCA, logística) / avanzada (marketplace) | US$ 8.000-20.000 / 20.000-45.000 / 45.000-120.000 | 2-3 / 3-5 / 5-10 meses | D/5 [L], sin método. **Contradice** al de junio del mismo proveedor por 5 a 7 veces |
| Develop Argentina, mantenimiento | tienda a medida | US$ 145-450 por mes (hosting 30-100, mantenimiento técnico 100-300, email 15-50); en marzo usó US$ 1.000 por mes como supuesto | | D/5 [L] |
| IURCO | Pampa (Magento + Next.js) / Ceibo (FastStore, Shopify) | sin precio | "~4 weeks" / "~2 weeks" | D/4 [L] |
| Fulljaus | implementación | sin precio | "30–60 días" | D/4 [L] |
| Bloque comparativo de un blog de terceros | implementar VTEX | "decenas de miles a cientos de miles de dólares", más de US$ 30.000 en proyectos grandes, 6 a 12 meses | | E/5 [S], andreybusiness.com |
| Barrido anterior | headless, primer año | US$ 40.000-200.000, agencias que venden headless | | D/5 |

Huecos: ninguna agencia de VTEX ni de Shopify Plus en Argentina publica un precio. Workana bloqueó la lectura (Cloudflare, 403) y en los avisos que mostró el buscador no figura ningún presupuesto en dólares. Tampoco se leyó Freelancer.

### 3.2 Sueldos: la base para el cálculo

Encuesta de sueldos de Sysarmy, edición 2026.01 (publicada el 2026-03-04; 4.939 respuestas válidas), leída de los datos que trae la propia página (`sueldos.openqube.io/encuesta-sueldos-2026.01`). Sueldo **bruto mensual** en pesos. Junior: 0 a 2 años; Semi-Senior: 2 a 5; Senior: 5 o más. B/2 [L]: es una encuesta voluntaria, con sesgo de autoselección, pero publica método e intervalos de confianza.

| Rol | Pesos (no dolarizado) | Dolarizado (al menos en parte) |
|---|---|---|
| Developer Junior | $1.538.500 | $1.600.000 |
| Developer Semi-Senior | $2.501.629 | $3.200.000 |
| Developer Senior | $3.500.000 | $5.332.500 |
| Technical Leader Senior | sin dato confiable | $6.743.000 |
| QA Semi-Senior | $1.879.574 | $2.600.000 |
| Diseño | la encuesta marca sus medianas como no confiables | |
| Mediana general | $3.253.581 = US$ 2.327,5 al oficial de la fecha | |

De la mediana general en pesos y en dólares sale el tipo de cambio que usó la encuesta: **$1.397,9 por dólar** (cálculo propio). Hoy el oficial vende a $1.600 y el MEP a $1.743,10 (dolarapi.com, 20 y 22-nov-2026). Los sueldos de marzo ajustados por la inflación posterior no se calcularon: **supuesto** de que en dólares se mantienen parecidos.

Por tecnología (la encuesta no tiene VTEX, Shopify ni Next.js como fila de sueldo): TypeScript Senior dolarizado $6.345.000; JavaScript Senior dolarizado $5.685.799. Next.js lo usa el 10,5% de quienes respondieron; React, el 19,2%.

Avisos con sueldo: Devups, front-end VTEX IO semi senior, US$ 1.000 a 1.400 brutos por mes (barrido, B/3). En Get on Board, el 22-nov-2026, la búsqueda "vtex" da un solo aviso (Chile, US$ 1.300-1.800) y "nextjs", ninguno (API pública `getonbrd.com/api/v0/search/jobs`, A/3 [L]). Hueco: no hay serie de avisos argentinos con sueldo para VTEX o Shopify.

### 3.3 Cuenta de abajo hacia arriba

**Supuestos**, todos de esta investigación y ninguno medido:
- S1. Costo empresa = bruto × 13/12 (aguinaldo) × 1,25 (contribuciones patronales) = **1,354 × bruto**. No incluye vacaciones, equipo ni oficina.
- S2. Tipo de cambio de la encuesta, $1.397,9 por dólar.
- S3. Diseño y gestión se pagan como un desarrollador Semi-Senior y Senior, porque la encuesta no da su sueldo confiable.
- S4. 160 horas por persona por mes.
- S5. Una **vitrina chica**: 1 desarrollador Senior + 0,5 Semi-Senior (diseño), 3 meses. Una **vitrina mediana**: 0,5 líder técnico, 1 Senior, 2 Semi-Senior, 0,5 QA, 0,5 diseño, 0,25 gestión (4,75 personas), 4 meses. Ambas sobre un motor que ya resuelve catálogo, carrito y checkout (FastStore, Hydrogen o la Storefront API de Tiendanube); no incluyen la licencia del motor.
- S6. Mantener: 0,5 Senior (chica) y 1 Senior + 0,5 a 1 Semi-Senior (mediana). Es el supuesto más débil: no hay fuente de horas (sección 3.4).

| Concepto | Equipo propio, sueldos en pesos | Equipo propio, sueldos dolarizados | Agencia a US$ 25-49/h | Agencia a US$ 50-99/h |
|---|---|---|---|---|
| Vitrina chica: costo mensual del equipo | US$ 4.602 | US$ 6.716 | | |
| Vitrina chica: construir (3 meses, 720 h) | **US$ 13.800** | **US$ 20.100** | **US$ 18.000-35.300** | US$ 36.000-71.300 |
| Vitrina mediana: costo mensual del equipo | US$ 13.157 | US$ 18.732 | | |
| Vitrina mediana: construir (4 meses, 3.040 h) | **US$ 52.600** | **US$ 74.900** | **US$ 76.000-149.000** | US$ 152.000-301.000 |
| Mantener chica (0,5 persona, 80 h por mes) | US$ 1.695 por mes; US$ 20.300 por año | US$ 2.583 por mes; US$ 31.000 por año | US$ 2.000-3.900 por mes | US$ 4.000-7.900 por mes |
| Mantener mediana (1,5 a 2 personas, 240-320 h por mes) | US$ 4.602-5.814 por mes | US$ 6.716-8.266 por mes | US$ 6.000-15.700 por mes | US$ 12.000-31.700 por mes |

Cuentas: por ejemplo, Developer Senior en pesos $3.500.000 / 1.397,9 = US$ 2.504; × 1,354 = US$ 3.390 por mes de costo empresa. El resto, igual con las cifras de la tabla 3.2.

Contraste con lo publicado: la vitrina chica propia (US$ 14.000-20.000) cae dentro del rango de marzo de Develop Argentina (US$ 8.000-20.000) y muy por encima del de junio (US$ 1.500-3.000). El mantenimiento de US$ 100-300 por mes que publica Develop Argentina alcanza, a sus propias tarifas implícitas, para unas pocas horas por mes (inferencia): es soporte, no un desarrollador dedicado como pide Shopify.

### 3.4 Lo que cuesta mantener: fuentes

| Fuente | Qué dice | ¿Vende headless? | Calif. |
|---|---|---|---|
| Shopify, documentación de headless | "A headless storefront costs more to build and run than a theme"; que el comercio "has developers to maintain the storefront after launch"; que "accepts the added cost and complexity" | vende las dos cosas; su producto principal son los temas | A/2 [L], https://shopify.dev/docs/storefronts/headless |
| Tiendanube, Storefront API | el frontend "queda a cargo del equipo o la agencia"; se pierden editor visual, SEO y parte de las estadísticas | vende las dos cosas | A/1 (barrido) |
| Tiendanube, comparación con VTEX | marca en VTEX como "Costo adicional" el "Equipo técnico para consultorías de personalizaciones y soluciones a medida"; dice de sí "no requiere desarrolladores" | competidor de VTEX | D/5 [L], tiendanube.com/evolucion/compara-vtex |
| Bensimon, caso de Tiendanube | en Magento, "costos mensuales que oscilaban entre 1,5 y 3 millones de pesos" y "Alta dependencia técnica para cualquier cambio" | lo publica la plataforma a la que migró | D/4 [L]; a $1.600 son unos US$ 940-1.875 por mes (cálculo propio) |
| Salesforce y Netguru | el costo se corre 6 a 24 meses después del lanzamiento; con headless propio "your IT team is responsible for ongoing maintenance" | sí | D/5 [S] |

Hueco central: **ninguna fuente independiente da horas o personas por mes** para mantener una vitrina headless. Lo más cerca de un número es lo que una marca dice que pagaba (Bensimon, en Magento, no headless).

## 4. Migraciones: por qué se va a medida o se vuelve a una plataforma

| Marca | De | A | Por qué, según la fuente | Fuente | Calif. |
|---|---|---|---|---|---|
| Frávega | VTEX completo (desde 2014) | frente propio en React con CMS propio; VTEX queda para carrito, checkout y backend | más velocidad, flexibilidad y control sobre la experiencia; no quería hacer su propio checkout | caso de VTEX (casestudies.com y el PDF en cdn.featuredcustomers.com); detección propia del Next.js | C/3 [S] para el porqué; A/3 [L] para la vitrina |
| Cetrogar | sin dato | VTEX FastStore | sin dato | detección propia | A/3 [L] para el estado actual |
| Bensimon | Magento | Tiendanube Evolución, a inicios de 2026, en 31 días | costo ($1,5 a 3 millones por mes), "dependencia técnica", plataforma "rígida"; quería "operar con autonomía" | tiendanube.com/blog/ejemplos/bensimon; detección: hoy en Tiendanube | D/4 [L] |
| Selú | VTEX | Tiendanube Evolución, con rediseño | hecho para su aniversario número 50 (paráfrasis); el porqué no se dice | perfil de Innovate Group en Tiendanube; detección: hoy en Tiendanube | D/4 [L] |
| Oggi | Shopify (caso de POW: "rediseño en Shopify + integraciones") | hoy en Tiendanube | sin dato; el caso de POW no tiene fecha | pow.la; detección propia | A/3 para el estado actual; el pasaje es inferencia |
| 47 Street | sin dato | VTEX IO | "Migramos a VTEX IO" | pow.la; detección: VTEX IO | D/4 |
| Etiqueta Negra | Magento | Tiendanube Evolución | rediseño de una marca con historia | buscador y perfil de Innovate Group | D/5; el dominio hoy redirige a pctechnical.com.ar |
| Samsonite Latinoamérica (no argentina) | VTEX | Shopify Plus | pasar de lo físico a lo digital en 9 meses; 12 sitios en 6 a 9 meses | caso de Shopify | B/3 [S] |
| (oferta) LOP Multimedia | VTEX o Magento | Shopify Plus | "Up to 6 months with no license fees: just 0.2% of your sales", para migraciones desde VTEX en LATAM firmadas antes del 31-dic-2026 | lop.global/en | D/4 [L]; muestra que hay un flujo que la agencia quiere captar, no su tamaño |

Lo que se repite en los casos que dan motivo (todos contados por quien recibió la migración): costo mensual, depender de un técnico para cada cambio y querer autonomía. El único caso hacia lo a medida (Frávega) lo cuenta el motor que se quedó con el checkout. Contexto ya en la base: Magento cayó de 568 tiendas en Argentina en el tercer trimestre de 2023 a 332 (StoreLeads, `presencia-en-argentina.md`). Hueco: no apareció ninguna marca argentina que haya dejado una vitrina headless y lo cuente.

## 5. Huecos

1. **Precios de agencia.** Ninguna agencia de VTEX, Shopify Plus o headless publica precio en Argentina. Lo publicado es de un solo proveedor, que se contradice.
2. **Horas de mantenimiento.** Ninguna fuente independiente. El supuesto S6 sostiene toda la fila de mantener.
3. **Workana y Freelancer.** Workana dio 403 (Cloudflare) con navegador real; Freelancer no se intentó.
4. **LinkedIn, GoodFirms y Adobe.** No se leyeron: tamaño real de las agencias y socios de Adobe Commerce en el país, sin dato.
5. **Sueldo por tecnología de comercio.** La encuesta de Sysarmy no abre VTEX, Shopify ni Next.js como fila de sueldo; hay un solo aviso VTEX con sueldo en Argentina (Devups, barrido).
6. **Qué hay detrás de las vitrinas a medida.** En Cheeky, Paula Cahen d'Anvers, Sodimac y los desarrollos propios no se ve el motor. No se abrió el carrito ni el checkout (habría que cargar el sitio).
7. **Representatividad.** Las 51 marcas las eligió esta investigación. No hay un conteo de vitrinas headless en el país; los rastreadores detectan la plataforma por la vitrina (barrido).
8. **Inflación entre marzo y noviembre de 2026.** Los sueldos son de la encuesta de marzo; no se ajustaron.

## 6. Fuentes

Todas consultadas el 2026-11-22.

- VTEX, System Integrator Program y directorio: https://vtex.com/en-us/system-integrators/ ; API: https://www.vtex.com/api/si-portal/v2/system-integrators?lang=en&page=1&limit=500 [A/2, L]
- Shopify Partner Directory, Argentina: https://www.shopify.com/ar/partners/directory/services/store_building?location=AR y perfiles `https://www.shopify.com/ar/partners/directory/partner/<slug>` (lop-global, wuala, innovate-group, vn-studios, combinatoria, hamanut-design1, bue-studio, lirogo-digital, romolabs, e-chile, cristian-varela) [A/2, L]
- Shopify, headless: https://shopify.dev/docs/storefronts/headless [A/2, L]
- Tiendanube, Especialistas: https://www.tiendanube.com/especialistas/servicios/desarrollo ; https://www.tiendanube.com/especialistas/estudiovolando ; https://www.tiendanube.com/especialistas/innovate-group2 [A/2 y D/4, L]
- Tiendanube, compara VTEX: https://www.tiendanube.com/evolucion/compara-vtex [D/5, L]; caso Bensimon: https://www.tiendanube.com/blog/ejemplos/bensimon/ [D/4, L]
- Clutch: https://clutch.co/ar/developers/ecommerce ; https://clutch.co/profile/kudos-commerce ; https://clutch.co/profile/known-online [C/3, L]
- Agencias, sitios propios: https://knownonline.com ; https://piercecommerce.com/ ; https://www.fulljaus.com ; https://innew.net/ ; https://www.pow.la/ ; https://www.wuala.net/ ; https://lop.global/en ; https://www.combinatoria.wine/ ; http://avenidamas.com/ ; https://iurco.com/llms.txt [D/4, L]
- Develop Argentina: https://developargentina.com/precios ; https://developargentina.com/blog/cuanto-cuesta-ecommerce-argentina-2026 ; https://developargentina.com/blog/cuanto-cuesta-tienda-online-argentina-2026 [D/5, L]
- Sysarmy y openqube, encuesta 2026.01: https://sueldos.openqube.io/encuesta-sueldos-2026.01/ (datos leídos del archivo `static/js/main.d30099da.js` que sirve la página) [B/2, L]
- Tipo de cambio: https://dolarapi.com/v1/dolares/oficial y https://dolarapi.com/v1/dolares/bolsa [B/2, L]
- Get on Board, API pública: https://www.getonbrd.com/api/v0/search/jobs?query=vtex (y shopify, nextjs, ecommerce) [A/3, L]
- Frávega y VTEX: https://www.casestudies.com/company/vtex/case-study/protecting-fravegas-legacy-with-headless-technology ; PDF: https://cdn.featuredcustomers.com/CustomerCaseStudy.document/protecting-fravegas-legacy-with-headless-technology_hkPsOXF.pdf ; las URLs originales en vtex.com dieron 404 [C/3, S]
- Samsonite: https://www.shopify.com/case-studies/samsonite (según el buscador) [B/3, S]
- Blog sobre VTEX: https://www.andreybusiness.com/argentina/blog/shopify-vs-vtex-ecommerce-latam-2026 (según el buscador) [E/5, S]
- Salesforce: https://www.salesforce.com/resources/articles/minimize-headless-commerce-cost/ ; Netguru: https://www.netguru.com/blog/the-real-price-of-headless-commerce (según el buscador) [D/5, S]
- Workana: https://www.workana.com/jobs (403) [sin lectura]
- Detección propia, una GET por portada: fravega.com, cetrogar.com.ar, cheeky.com.ar, paulacahendanvers.com.ar, tiendabna.com.ar, sodimac.com.ar, coto.com.ar, megatone.net, grimoldi.com, havanna.com.ar, kevingston.com, carrefour.com.ar, jumbo.com.ar, farmacity.com, oncity.com, easy.com.ar, arredo.com.ar, levi.com.ar, naldo.com.ar, sportline.com.ar, mimo.com.ar, fila.com.ar, 47street.com.ar, provinciacompras.com.ar, dexter.com.ar, stockcenter.com.ar, moov.com.ar, rapsodia.com.ar, prune.com.ar, solodeportes.com.ar, selu.com.ar, bensimon.com.ar, oggi.com.ar, compumundo.com.ar y los que no respondieron [A/3, L]
- Base: `Comercio-electronico/Plataforma-de-tiendas/presencia-en-argentina.md`, `vtex.md`; barrido: `lind-negocio/el-taller/analisis/2026-11-22-el-bosque/motor-para-vidrieras-a-medida.md`
