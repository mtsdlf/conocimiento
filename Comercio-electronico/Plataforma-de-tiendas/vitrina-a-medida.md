---
resumen: >-
  Una vitrina a medida es el frente de una tienda que el comercio o su agencia programa y que habla por API con un motor de comercio, que sigue guardando catálogo, precios y pedidos. Es el modo headless en la práctica: qué se programa, cuánto cuesta sostenerlo, de qué se quejan quienes lo hacen y cuántas marcas lo tienen en Argentina.
estado: vigente
estabilidad: semi
fuentes:
  - "Shopify, Headless: https://shopify.dev/docs/storefronts/headless (leída, consultada el 2026-11-22)"
  - "Tiendanube Ayuda, qué es la Storefront API (actualizada el 26-oct-2026): https://ayuda.tiendanube.com/es_AR/socios-tecnologicos/que-es-la-storefront-api-de-tiendanube-y-para-que-sirve (leída entera, 2026-11-22)"
  - "VTEX, código de FastStore (redirectToCheckout.ts y pages/checkout.tsx): https://github.com/vtex/faststore (leído, 2026-11-22)"
  - "WooCommerce, Store API: https://developer.woocommerce.com/docs/apis/store-api/ (leída, 2026-11-22)"
  - "StoreLeads, Next.js, Nuxt y Shopify Hydrogen en Argentina (actualizadas el 13-nov-2026): https://storeleads.app/reports/technology/Next.js/country/AR , https://storeleads.app/reports/technology/Nuxt/country/AR , https://storeleads.app/reports/technology/Shopify%20Hydrogen/country/AR (leídas, 2026-11-22)"
  - "StoreLeads, VTEX, Magento, Salesforce Commerce Cloud, Shopify, WooCommerce y carrito propio en Argentina: https://storeleads.app/reports/vtex/AR/top-stores y páginas hermanas (leídas, 2026-11-22)"
  - "Tiendanube, clientes de Evolución: https://www.tiendanube.com/evolucion/clientes (leída, 2026-11-22; la empresa)"
  - "Mercado, Hot Sale 2026 (5-may-2026): https://mercado.com.ar/agenda/hot-sale-2026-mas-de-800-marcas-y-foco-en-financiacion (leída)"
  - "Sysarmy y openqube, encuesta de sueldos 2026.01 (4-mar-2026): https://sueldos.openqube.io/encuesta-sueldos-2026.01/ (leída, datos de la página)"
  - "dolarapi, dólar oficial y MEP: https://dolarapi.com/v1/dolares/oficial (leída, 20 y 22-nov-2026)"
  - "Clutch, e-commerce developers en Argentina: https://clutch.co/ar/developers/ecommerce (leída en parte, 33 de 151 perfiles)"
  - "VTEX, directorio de integradores, API: https://www.vtex.com/api/si-portal/v2/system-integrators?lang=en&page=1&limit=500 (leída entera)"
  - "Shopify, directorio de socios en Argentina: https://www.shopify.com/ar/partners/directory/services/store_building?location=AR (leída, con y sin el filtro headless)"
  - "Archivo de Reddit pullpush.io, GitHub issues, PeerSpot, Hacker News y la comunidad de VTEX, codificados en Comercio-electronico/.investigacion/vidrieras-resenas.json (255 filas codificadas a mano: de GitHub se leyeron 150 títulos y unos 15 cuerpos; de Magento, 120 de 215 comentarios)"
  - "Comercio-electronico/.investigacion/vidrieras-tamano.md (secciones 1 a 5 y fuerza de la cifra)"
  - "Comercio-electronico/.investigacion/vidrieras-agencias-y-costo.md (secciones 1, 2, 3 y 4)"
  - "Comercio-electronico/.investigacion/vidrieras-resenas.md (respuesta primero, temas, Latinoamérica y sesgos)"
  - "Comercio-electronico/.investigacion/vidrieras-motores-y-precios.md (secciones 2 y 3)"
  - "Comercio-electronico/.investigacion/vidrieras-contraria.md (tabla de veredictos, ítems 2 a 4, 7, 10, 13, 14, 23, 26, 33 a 37, 39, 45, 49 a 51), que manda sobre los otros cuatro"
aliases: [vitrina a medida, vidriera a medida, headless en la práctica, vitrina headless, headless storefront, custom storefront, frente desacoplado]
creado: 2026-11-27
revisado: 2026-11-27
---

# Vitrina a medida

Una vitrina a medida es el frente de una tienda que el comercio o su agencia programa y que habla por API con un motor de comercio, que sigue guardando catálogo, precios y pedidos. Es el modo headless en la práctica: qué se programa, cuánto cuesta sostenerlo, de qué se quejan quienes lo hacen y cuántas marcas lo tienen en Argentina.

Qué es headless y cuándo conviene está en [tipos de plataforma](tipos-de-plataforma.md#headless-y-composable-separar-la-vitrina-y-elegir-cada-pieza). Licencia, precio y lo local de cada motor, en la ficha [motores para vitrinas a medida](motores-para-vitrinas-a-medida.md).

## Dónde termina la vitrina y empieza el motor

El frente se programa siempre. Lo que cambia es si el motor se queda con el carrito y el checkout:

| Motor | Carrito | Checkout |
|---|---|---|
| Shopify con Hydrogen | sin dato | el de Shopify ("redirects customers through Shopify's web checkout"); personalización completa solo en Plus |
| VTEX con FastStore | sin dato | el de VTEX, al que redirige el código de FastStore |
| API de vitrina de Tiendanube | lo arma el frente: «La API no incluye un endpoint de carrito» | el alojado de Tiendanube |
| Medusa, Saleor, Vendure, commercetools | se arma sobre la API del motor | se arma sobre la API, con pagos, envíos e impuestos |
| WooCommerce | lo trae su Store API | lo trae su Store API; la pasarela, sin garantía |

Con la API de Tiendanube, según su ayuda, se pierden el editor visual, el SEO y parte de las estadísticas, y las apps «se validan caso a caso». Una cadena de electrodomésticos argentina muestra la división: en VTEX desde 2014, armó su frente en React y dejó carrito y checkout en VTEX porque no quería hacer el suyo, según un caso de VTEX leído por un resumen.

> [!IMPORTANT]
> Si hay un motor a medida con lo local resuelto depende de cómo se cuente. WooCommerce y Magento Open Source no cobran licencia, dejan armar el checkout y tienen [Mercado Pago](../Pagos/mercado-pago.md) oficial, y WooCommerce suma transportistas argentinos y factura de [ARCA](../Normativa/factura-electronica-de-arca.md). Pero nadie probó que anden sin la vitrina estándar. En Medusa hay solo un Mercado Pago de la comunidad, y en Saleor, Vendure y commercetools no hay nada de lo local.

## Cuánto cuesta construirla y sostenerla

Casi nadie publica precios en Argentina, y el único estudio que publica tablas se contradice: US$ 8.000 a 20.000 por una tienda a medida básica en marzo de 2026 y US$ 1.500 a 3.000 en junio. La cuenta se arma de abajo hacia arriba, con supuestos:

- Sueldos brutos de la encuesta de Sysarmy de marzo de 2026 (Senior $3.500.000 en pesos), por 1,354 de costo empresa, a $1.397,9 por dólar.
- Vitrina chica: 1,5 personas durante 3 meses; mediana: 4,75 personas durante 4 meses. Mantener: media persona o de 1,5 a 2.
- Sin la licencia del motor, y con un motor que ya resuelve carrito y checkout.

| | Propio, en pesos | Propio, dolarizado | Agencia a US$ 25-49 la hora | Agencia a US$ 50-99 la hora |
|---|---|---|---|---|
| Construir la chica | US$ 13.800 | US$ 20.100 | US$ 18.000-35.300 | US$ 36.000-71.300 |
| Construir la mediana | US$ 51.600-52.600 | US$ 74.900 | US$ 76.000-149.000 | US$ 152.000-301.000 |
| Mantener la chica, por mes | US$ 1.695 | US$ 2.583 | US$ 2.000-3.900 | US$ 4.000-7.900 |
| Mantener la mediana, por mes | US$ 4.602-5.814 | US$ 6.716-8.266 | US$ 6.000-15.700 | US$ 12.000-31.700 |

El primer año con equipo propio da US$ 29.000 a 43.000 la chica y US$ 89.000 a 141.000 la mediana. Las tarifas son las que cargan las agencias en Clutch: de 30 perfiles leídos entre 151, 16 cobran US$ 25-49 y 10 cobran US$ 50-99.

La cuenta vale para FastStore e Hydrogen. Con Tiendanube falta el carrito, y con los motores abiertos faltan el checkout y lo local: "the integration work for checkout alone it was going to eat 8-10 weeks", escribió un desarrollador.

El dólar oficial vendía a $1.600 a fines de noviembre de 2026. Si los sueldos en pesos no se hubieran movido desde marzo, las columnas en pesos saldrían un 13% menos en dólares; con la inflación del período, la diferencia es menor o nula.

Mantener es la fila más débil; Shopify, que vende ambas, escribe: "A headless storefront costs more to build and run than a theme".

> [!NOTE] Sin fuente todavía: horas o personas por mes para mantener una vitrina a medida, de una fuente que no venda headless; y el precio real de Medusa, Saleor o Vendure en la nube.

## De qué se quejan quienes la construyen

Se codificaron 255 filas: 204 opiniones (84 negativas, 120 mixtas) y 51 issues de GitHub, casi todas de quien construye.

| Tema | Opiniones | Negativas | Mixtas |
|---|---|---|---|
| Costo total, precio y licencia | 52 | 23 | 29 |
| Complejidad y tiempo de implementación | 46 | 18 | 28 |
| Funciones que faltan | 38 | 17 | 21 |
| Hace falta un equipo | 26 | 8 | 18 |
| Mantenimiento permanente | 25 | 11 | 14 |
| Pagos y checkout | 19 | 8 | 11 |

Costo, equipo o mantener aparecen en 85 de las 204, y algo más de la mitad son mixtas: sirve si hay con qué. Sobre commercetools: "you basically need a small agency just to maintain the frontend and integrations". En los issues, el checkout es lo que más aparece (22 de 51), en parte por cómo se buscó; rehacerlo es "almost always a trap", según quien lo hizo en WooCommerce.

Cada motor tiene su queja: en commercetools el costo (23 de 56 filas); en VTEX el costo (9), el rendimiento (7) y el talento (5), pero solo 6 de 27 filas tratan la vitrina; en los abiertos, funciones que faltan y complejidad; en Shopify headless, que el negocio pierde edición y medición (7 de 17).

De Latinoamérica son 29 de las 255: 20 de VTEX y 5 de Tiendanube, sobre temas y planes y ninguna sobre su API de vitrina. Una revisión de 30 filas al azar coincidió con la codificación en 21; G2 y Capterra bloquearon la lectura.

## Cuántas marcas la tienen en Argentina y cuántas podrían quererla

StoreLeads detectaba al 13-nov-2026 Next.js en 81 tiendas argentinas, Nuxt en 19 e Hydrogen en 5: 105 dominios, no marcas. De las 10 visibles de Next.js, 4 o 5 no son marcas de consumo (una telefónica, una inmobiliaria), y hay de todo tamaño, hasta una panadería.

| Cifra | Rango | Cómo sale | Fuerza |
|---|---|---|---|
| La tienen hoy | unas 70 a 220, centro unas 130 | 105, menos un ruido supuesto de 30% a 55%, por un supuesto de 1,5 a 3 por lo no detectado | débil a media |
| Podrían quererla | 1.200 a 1.900, centro unas 1.500 | tiendas de VTEX, Magento, Salesforce, Shopify Plus y Tiendanube Evolución, más las de WooCommerce y carrito propio con 50 o más empleados, ±20% supuesto | media |
| Les convendría | 120 a 475 | un supuesto de 10% a 25% de las anteriores | débil |

El Hot Sale 2026 tuvo «más de 800 marcas», 48% pymes: las unas 420 que no lo son quedan en el mismo orden, sin confirmarlo. En una muestra de portadas elegida a mano, de unas 38 legibles, 6 sirven un frente separado y 13 la vitrina estándar de VTEX.

De los 18 integradores de VTEX que atienden el país se leyeron 7, y 4 lo anuncian, lo hacen o lo declaran. Ninguno de los 11 [socios](socios-de-una-plataforma.md) de Shopify con sede en el país marca la especialidad headless, igual que en México, Brasil y Chile; uno ofrece "custom storefronts" en su perfil.

## Hacia dónde van las mudanzas públicas

Los casos publicados van hacia una plataforma. Una marca de indumentaria dejó Magento por Tiendanube Evolución por «costos mensuales que oscilaban entre 1,5 y 3 millones de pesos» (unos US$ 940 a 1.875) y «Alta dependencia técnica para cualquier cambio»; otra dejó VTEX por el mismo destino. Hacia lo a medida, el único caso es la cadena de electrodomésticos.

Es lo publicado y no el flujo: cada caso lo cuenta la plataforma que lo recibe. Cómo se hace el pase está en [mudar una tienda](mudar-una-tienda.md).

> [!NOTE] Sin fuente todavía: una marca argentina que haya dejado una vitrina a medida y cuente por qué.

## Cómo falla

Lectura propia sobre las quejas y los casos: falla cuando falta el equipo que la sostiene, cuando el checkout rehecho hereda impuestos, envíos y pagos, y cuando marketing ya no puede editar ni medir. También cuando el proyecto de abajo cambia: "PWA Studio is dead", se escribió sobre Magento en 2025, y Medusa pasó permisos y SSO a licencia comercial en agosto de 2026. Por eso [segmentos de comerciantes](segmentos-de-comerciantes.md) la pone arriba de la escalera.
