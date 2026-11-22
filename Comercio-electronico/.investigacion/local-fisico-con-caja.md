# El local físico con caja que también vende online (omnicanalidad práctica, Argentina)

Consulta: 2026-11-22. Ángulo: POS, stock compartido y retiro, ficha de POS y cobros en Argentina, reseñas.

## Cómo leer este informe

- Marcas de lectura: **[L]** texto completo abierto por mí; **[M]** metadatos, abstract o extracto devuelto por la herramienta de lectura (no vi la página cruda); **[S]** resumen secundario o del buscador. Las páginas que leí con `WebFetch` devuelven un extracto procesado, así que las marco [M] salvo que diga lo contrario. Solo marco [L] lo que leí entero en crudo (la nota de iProUP, la página de Google Play de Shopify POS, las diapositivas de Gallino y Moreno).
- Calificación de fuente A-F y de dato 1-6 (1 = verificado en primaria y vigente; 6 = no verificable). Puntajes de fuente 1-3 en autoridad (Aut), profundidad (Prof), ejemplos (Ej), unicidad (Uni).
- Límite del trabajo: el presupuesto de búsquedas web se agotó a mitad de la investigación, así que varios huecos son por eso y no porque no existan datos (ver «Huecos»). Varias páginas de Mercado Pago dan 403 con el lector.
- Todo es información pública; sin nombres de personas.

## Resumen en cinco líneas

1. El POS de Tiendanube viene en todos los planes (uno incluido: «Inicial» en el plan gratis, «Plus» en los pagos) y no cobra con tarjeta por sí mismo: registra el cobro hecho con un lector externo (Mercado Pago, Getnet, Nave). El único cobro integrado es QR con MODO.
2. Factura de ARCA en Tiendanube: no está en el POS; se resuelve con una app de terceros (facture.ar, desde gratis hasta 10 facturas por mes) que factura las ventas pagadas de la tienda.
3. Shopify POS funciona como app en casi cualquier país, pero Argentina no figura entre los países de Shopify Payments, así que el cobro integrado y el hardware oficial no aplican; POS Pro cuesta USD 89 por mes por sucursal (página argentina de Shopify).
4. Mercado Pago en Argentina vende lectores (Point Smart: lista $60.000, con 25% de descuento $44.999 el 2026-11-22) y una API para integrarlos a sistemas de terceros; el software de punto de venta propio de Mercado Pago lo encontré solo en México ($99 por mes), no en Argentina.
5. La evidencia empírica clave (Gallino y Moreno) muestra que el retiro en tienda con inventario confiable bajó las ventas online cerca de las tiendas y subió las ventas y el tránsito de las tiendas; el efecto neto fue positivo. No encontré estudios de América Latina.

---

## Componente 1. Punto de venta (POS)

### Fuentes

| # | Fuente | URL | Tipo | Lectura | Aut | Prof | Ej | Uni | Calif. |
|---|---|---|---|---|---|---|---|---|---|
| 1.1 | Ayuda Tiendanube, «Qué es Punto de venta» (AR) | https://ayuda.tiendanube.com/es_AR/pdv/que-es-punto-de-venta-de-tiendanube | primaria | [M] | 3 | 2 | 2 | 3 | A |
| 1.2 | Ayuda Tiendanube, «Cómo comenzar a usar Punto de venta» (AR) | https://ayuda.tiendanube.com/es_AR/pdv/como-comenzar-a-usar-punto-de-venta-en-mi-tiendanube | primaria | [M] | 3 | 2 | 2 | 3 | A (ver discrepancia) |
| 1.3 | Mercado Pago developers, Point, visión general | https://www.mercadopago.com.ar/developers/es/docs/mp-point/overview | primaria | [M] | 3 | 2 | 1 | 3 | A |
| 1.4 | Fudo (restaurantes), sitio | https://fu.do | primaria | [M] | 2 | 1 | 1 | 1 | C |
| 1.5 | Libro de retail de referencia (p. ej. Levy y Weitz, «Retailing Management») | no abierto | secundaria | — | — | — | — | — | hueco |

### Qué es y qué hace (afirmaciones)

- Un POS de pequeño comercio argentino cubre: buscar y cargar productos del catálogo viendo su stock, buscar o crear clientes, aplicar descuentos (monto fijo o porcentaje), agregar dirección y costo de envío y notas, y ver la venta en la lista de ventas de la tienda. Cita de la ayuda: «gestionar todo tu negocio en un solo lugar», incluye ventas por WhatsApp, teléfono o redes. https://ayuda.tiendanube.com/es_AR/pdv/que-es-punto-de-venta-de-tiendanube [M] — A-1.
- Caja: el plan «Plus» agrega «cash register management» (gestión de caja), permisos de usuario, soporte nativo de lectores de códigos de barras e impresoras de recibos. https://ayuda.tiendanube.com/es_AR/pdv/como-comenzar-a-usar-punto-de-venta-en-mi-tiendanube [M] — A-2 (ver discrepancia de nombres de plan).
- Diferencia con un lector de cobro: el lector (Point, Getnet, Nave) procesa la tarjeta y liquida el dinero; el POS de Tiendanube solo registra el cobro («terminal de pago externa (como Mercado Pago, Getnet o Nave)», con número de comprobante, cuotas, marca y banco opcionales). https://ayuda.tiendanube.com/es_AR/pdv/que-es-punto-de-venta-de-tiendanube [M] — A-1.
- Diferencia con un sistema de gestión: el POS vende y cobra en el mostrador; el sistema de gestión (compras, proveedores, contabilidad, múltiples depósitos) es más amplio. Un caso intermedio: Fudo describe «comandas, caja, cobros» y una «Terminal de pagos integrada», más facturación electrónica con ARCA y «tienda online propia» (https://fu.do [M]) — C-3.
- Mercado Pago Point integrado: la integración conecta un lector Point a un POS propio: «Creas la order de pago desde tu sistema a través de nuestra API unificada»; la terminal carga la orden, el comprador paga y el sistema recibe una notificación; modos PDV y SELF_SERVICE; terminales Point Smart 1 y 2; tarjetas (débito, crédito, prepaga; chip, NFC, banda) y QR. https://www.mercadopago.com.ar/developers/es/docs/mp-point/overview [M] — A-2.

### Recurso canónico propuesto

Un capítulo de manual de retail sobre el sistema de punto de venta (registro, caja, arqueo, inventario, informes). No abrí ninguno: queda como hueco. Mientras tanto, la documentación conceptual más a mano es la ayuda de Tiendanube (1.1, 1.2) para la parte funcional, y la doc de Point (1.3) para la integración lector-POS.

---

## Componente 2. Stock compartido y retiro en el local

### Fuentes

| # | Fuente | URL | Tipo | Lectura | Aut | Prof | Ej | Uni | Calif. |
|---|---|---|---|---|---|---|---|---|---|
| 2.1 | Gallino y Moreno (2014), Management Science 60(6):1434-1451, ficha en RePEc | https://econpapers.repec.org/RePEc:inm:ormnsc:v:60:y:2014:i:6:p:1434-1451 | primaria (ficha del paper) | [M] abstract | 3 | 2 | 1 | 3 | A |
| 2.2 | Gallino y Moreno, diapositivas de seminario (enero 2014, Universidad de Chile) | https://www.dii.uchile.cl/wp-content/uploads/2014/01/presentacion-Gallino-seminario-retail.pdf | primaria (de los autores) | [L] texto de las diapositivas; los números de los gráficos no salen en el texto | 3 | 2 | 2 | 3 | B |
| 2.3 | Tuck, «Rethinking Retail in a Multichannel World» | https://tuck.dartmouth.edu/news/articles/rethinking-retail-in-a-multichannel-world | secundaria (universidad) | [M] | 2 | 1 | 2 | 2 | B |
| 2.4 | Bell, Gallino y Moreno (2018), Management Science 64(4):1629-1651, «Offline Showrooms in Omni-channel Retail» | https://mackinstitute.wharton.upenn.edu/2018/offline-showrooms-and-customer-migration-in-omni-channel-retail/ | primaria (resumen institucional) | [M] abstract | 3 | 1 | 1 | 3 | A |
| 2.5 | Ayuda Tiendanube (stock, retiro en sucursal) | ver 1.1 | primaria | [M] | 3 | 2 | 2 | 3 | A |
| 2.6 | Shopify POS en Google Play (retiro y devoluciones) | https://play.google.com/store/apps/details?id=com.shopify.pos&hl=es_AR&gl=AR | primaria (descripción del proveedor) | [L] | 2 | 1 | 1 | 1 | B |
| 2.7 | Estudios de América Latina | — | — | no encontrado | — | — | — | — | hueco |

### Afirmaciones

- Qué estudiaron: un programa «buy-online, pick-up-in-store» (BOPS) en una cadena de más de 80 tiendas de Norteamérica, implementado en octubre de 2011, con seis meses de datos antes y seis después; unidades: DMA-día (online), tienda-día (tiendas). Diapositivas [L]: https://www.dii.uchile.cl/wp-content/uploads/2014/01/presentacion-Gallino-seminario-retail.pdf — B-2 (fuente de los autores, no el paper).
- Diseño: 48 áreas de mercado con una tienda a menos de 50 millas contra 162 sin tienda (control para online); Canadá, donde no había retiro, como control para las tiendas (diferencia en diferencias). Mismas diapositivas [L] — B-2.
- Resultado: tras el programa, las ventas online bajan en las áreas cercanas a tiendas aunque el tráfico online sube; las ventas y el tránsito de las tiendas suben más en EE.UU. que en Canadá. Mismas diapositivas [L] — B-2. El abstract en RePEc confirma: «ventas online más bajas y ventas y tránsito de tiendas más altos» y atribuye el efecto a dos fuerzas, venta cruzada en tienda y migración de canal, esta última explicada por más «research online, purchase offline» (ROPO); y cierra: «Our analysis illustrates the limitations of drawing conclusions about complex interventions using single-channel data.» https://econpapers.repec.org/RePEc:inm:ormnsc:v:60:y:2014:i:6:p:1434-1451 [M, extracto] — A-2.
- Mecanismo central: ofrecer BOPS obliga a compartir información de disponibilidad confiable, lo que baja el costo de ir a la tienda y reduce el riesgo de faltante para el cliente (diapositivas [L]); el autor lo resume en la nota de Tuck como la «percepción de confiabilidad del inventario». https://tuck.dartmouth.edu/news/articles/rethinking-retail-in-a-multichannel-world [M] — B-3.
- Balance por canal: las diapositivas muestran «-2%», «+6%» y «+4%» en un gráfico sin rótulos legibles en el texto; leo online -2%, tiendas +6%, total +4%, pero es lectura mía del orden de los números, no verificada contra el paper. Marcado como dato 5 (no confirmar antes de citarlo).
- Uso del retiro: según Tuck, más del 60% de quienes usaron BOPS retiró dos o más días después de la compra; el retiro estaba disponible en aproximadamente una hora; el estudio cubrió 83 tiendas y 210 DMA. https://tuck.dartmouth.edu/news/articles/rethinking-retail-in-a-multichannel-world [M] — B-3 (las diapositivas dicen «más de 80 tiendas»; Tuck dice 83).
- Desafíos que nombran los autores: compartir inventario en tiempo real, inexactitud del registro de inventario, mayor complejidad de ejecución en tienda ([L] diapositivas) — B-2.
- Showrooms (Bell, Gallino y Moreno 2018): con datos cuasi-experimentales de aperturas de showrooms de una marca online de anteojos, la demanda sube en total y en el canal online, la eficiencia operativa mejora (más conversión en el canal de prueba, menos devoluciones) y el beneficio crece con el tiempo («channel awareness»). https://mackinstitute.wharton.upenn.edu/2018/offline-showrooms-and-customer-migration-in-omni-channel-retail/ [M] — A-2. No dan números en el resumen que leí.
- Producto en Argentina, stock por ubicación: si hay más de un centro de distribución, se puede destinar el stock de uno solo a las ventas del Punto de venta, sin mostrarlo en la tienda online («destinar el stock de uno de ellos únicamente a las ventas de Punto de Venta»); el Punto de venta «no amplía el límite de centros de distribución de tu plan base». https://ayuda.tiendanube.com/es_AR/pdv/que-es-punto-de-venta-de-tiendanube [M] y https://www.tiendanube.com/tienda-aplicaciones-nube/facturear (resultado del buscador, [S]) — A-3 para lo primero, C-4 para el límite.
- Retiro: pestaña «Retiro en sucursal» con las ventas pendientes de retiro, que se marcan retiradas cuando el cliente llega; carrito compartido con link para que el cliente pague con los medios de la tienda online. https://ayuda.tiendanube.com/es_AR/pdv/que-es-punto-de-venta-de-tiendanube [M] — A-1.
- Shopify POS (descripción de Google Play, [L]): seguimiento de todos los pedidos de retiro con aviso al cliente cuando están listos, y cambios y devoluciones de artículos comprados online o en otras ubicaciones. https://play.google.com/store/apps/details?id=com.shopify.pos&hl=es_AR&gl=AR — B-3 (descripción del proveedor, sin saber si aplica en Argentina).
- Envío desde la tienda (ship from store) y reserva de stock del local: no encontré documentación de Tiendanube sobre ninguno de los dos; el POS permite ventas con envío. Hueco.

### Recurso canónico propuesto

Gallino y Moreno (2014), Management Science 60(6), https://doi.org/10.1287/mnsc.2014.1951 (no abrí el paper completo: lo canónico es leerlo en la fuente; mientras, las diapositivas de los autores sirven para el diseño y la conclusión).

---

## Componente 3. Ficha de POS y cobros en Argentina

### Fuentes

| # | Fuente | URL | Tipo | Lectura | Aut | Prof | Ej | Uni | Calif. |
|---|---|---|---|---|---|---|---|---|---|
| 3.1 | Tiendanube, planes y precios (AR) | https://www.tiendanube.com/planes-y-precios?c=AR | primaria | [M] | 3 | 2 | 1 | 3 | A |
| 3.2 | Tiendanube, app facture.ar | https://www.tiendanube.com/tienda-aplicaciones-nube/facturear | primaria | [M] | 3 | 2 | 2 | 2 | A |
| 3.3 | Shopify, POS (versión AR) | https://www.shopify.com/ar/pos | primaria | [M] | 3 | 1 | 1 | 2 | A |
| 3.4 | Shopify, precios de POS (AR) | https://www.shopify.com/ar/pos/precios | primaria | [M] | 3 | 1 | 1 | 2 | A |
| 3.5 | Shopify, países de Shopify Payments | https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries | primaria | [M] | 3 | 2 | 1 | 3 | A |
| 3.6 | Shopify, preguntas frecuentes de venta en persona | https://help.shopify.com/en/manual/sell-in-person/faq | primaria | [M] | 3 | 1 | 1 | 2 | A |
| 3.7 | Mercado Pago, Point Smart (AR) | https://www.mercadopago.com.ar/herramientas-para-vender/lectores-point/point-smart | primaria | [M] | 3 | 2 | 1 | 3 | A |
| 3.8 | Mercado Pago, costos de Point (AR) | https://www.mercadopago.com.ar/costs-section/point | primaria | 403 con lector y con WebFetch, no leída | — | — | — | — | hueco |
| 3.9 | Mercado Pago México, blog del sistema de punto de venta | https://www.mercadopago.com.mx/blog/todo-sobre-el-sistema-de-punto-de-venta | primaria | [S] (403 al abrirla; dato del buscador) | 3 | 1 | 1 | 2 | C |
| 3.10 | iProUP, «Mercado Pago, Ualá, MODO: cuál es más barato para cobrar», 16.01.2026 | https://www.iproup.com/finanzas/64002-mercado-pago-uala-modo-cual-es-mas-barato-para-cobrar-en-comercios-y-emprendimientos | secundaria | [L] | 2 | 2 | 2 | 2 | C |
| 3.11 | Tiendanube MX, planes y página del POS | https://www.tiendanube.com/mx/canales/punto-de-venta | primaria (otro país) | [M] | 3 | 2 | 1 | 2 | A (solo México) |

### Tabla de POS y cobros (consulta 2026-11-22)

| Producto | Qué es | Precio y condiciones | Cobro con tarjeta | Factura ARCA | Stock/retiro | Fuente, calif. |
|---|---|---|---|---|---|---|
| Tiendanube, Punto de venta | POS de la tienda, en todos los planes | Un POS incluido: «Inicial» en el plan gratis; «Plus» en los planes de pago; extras Plus «por un costo adicional, según tu plan». Precio del punto extra en AR: no encontrado. Planes AR (mensual, 3.1): Inicial gratis; Esencial $27.999; Impulso $79.999; Escala $244.999; Evolución a consultar (cifras de la página con descuento anual: $20.999, $59.999, $183.749 por mes). Crear productos en el POS: solo plan Plus | No procesa tarjeta: registra cobros en efectivo, transferencia o terminal externa (Mercado Pago, Getnet, Nave). QR con Pago Nube: solo MODO | No incluida; app facture.ar (gratis 10 facturas por mes; Básica USD 9,99 por mes con 1.000; Pro USD 59,99 por mes con 25 CUIT y 25.000) | Stock sincronizado con la tienda; stock de un centro reservable para el POS; retiro en sucursal | 3.1, 1.1, 3.2; A-2 (precio extra: hueco) |
| Shopify POS | App de venta en persona | POS Pro: USD 89 por mes por sucursal, facturación anual (página AR). La versión básica está en todos los planes pagos. «Casi en cualquier país» según la página AR | Shopify Payments y hardware «solo en algunas regiones»; Argentina no está en la lista de 41 países de Shopify Payments | No encontrado (hueco) | Retiro, cambios y devoluciones entre canales (descripción de Google Play) | 3.3-3.6; A-2 |
| Mercado Pago Point Smart | Lector con pantalla (Android 12), sin POS | Lista $60.000, 25% off = $44.999 (o 6 cuotas de $7.499,83); «sin costo de alquiler»; un blog de 2026-09-06 repite los mismos montos [S] | Ver tabla de comisiones | Página del producto no la menciona | Sin stock; API para integrarlo a POS propios (1.3) | 3.7; A-2 |
| Mercado Pago, software de gestión / POS propio | Sistema de punto de venta de Mercado Pago | México: $99 MXN por mes o $950 por año, prueba de 15 días [S]. Argentina: no encontré lanzamiento (búsqueda hecha antes de agotar el presupuesto; el resultado fue negativo) | — | — | — | 3.9; C-4 |
| Getnet (Santander) | Adquirente, terminales y app | Abono según plan | Según iProUP: 0,8% QR, 3,19% débito, 6,19% crédito, acreditación inmediata | — | Tiendanube lo cita como terminal externa | 3.10, 1.1; C-3 |
| Nave (Grupo Galicia) | Adquirente | Abono según plan | 0,8% QR, 1,2% débito, 4,5% crédito, acreditación inmediata | — | Tiendanube lo cita como terminal externa | 3.10, 1.1; C-3 |
| Payway (Prisma) | Adquirente | Abono mensual en algunos casos bonificado | 0,8% QR en el acto; 1% débito a 1 día hábil; 6,3% (1 día) y 2% (8 días) como figura en la nota | — | No relevado | 3.10; C-4 |
| Fiserv (PosNET/Clover) | Adquirente | Abono mensual en algunos casos bonificado | 0,8% QR; 0,8% débito a 1 día hábil; 1,8% a 8 días hábiles | — | No relevado | 3.10; C-4 |
| Ualá Bis | Cobro para emprendedores | — | La nota trae: 0,8% QR con saldo en el acto; 2,9% «débito en el acto»; 4,9% «débito en el acto» (repetido, probable error de la nota) | — | No relevado | 3.10; C-5 |
| MODO | Billetera de bancos; sin cobro propio, opera sobre adquirentes | Tasas reguladas con QR interoperable | Ver Fiserv y Payway | — | Integrado como QR en el POS de Tiendanube | 3.10, 1.1; C-3 |

### Comisiones de Mercado Pago Point, dos fuentes que discrepan

| Concepto | Página oficial de Point Smart AR (3.7) [M] | iProUP, 2026-01-16 (3.10) [L] |
|---|---|---|
| Débito | Titular de la página 2,99%; tabla: 2,75% a 2 días | 3,25% en el acto (Point); 1,35% con QR |
| Crédito | Titular 5,99%; tabla: 5,19% a 5 días; 4,19% a 10 días | 6,29% en el acto (Point/QR) |
| Prepaga | 3,75% al instante; 3,50% a 3 días | no figura |
| QR con saldo | no figura | 0,8% |

La página oficial no explica por qué el titular (2,99%/5,99%) no coincide con la tabla; la nota es de enero y la página se leyó en noviembre; las tasas dependen del plazo elegido y de impuestos provinciales. Usar la oficial para citar, y declarar la fecha. Plazos de liberación en la página oficial: al instante, 2, 3, 5 o 10 días según el medio. Funciones: wifi o chip 4G con datos gratis, batería de 3 días, QR impreso gratis, equipo de más de 100 miembros. Facturación electrónica e integraciones con terceros: no figuran en esa página (la integración está en la doc de developers, 1.3).

### Discrepancias a tener presentes

- Nombres de plan del POS de Tiendanube: la ayuda «Qué es» habla de «Inicial» y «Plus (antes Avanzado)»; la ayuda «Cómo comenzar» habla de «Lite (antes Básico)» y «Plus (antes Avanzado)», con costos por transacción de 1% (Lite) y 0,25% (Plus), y un plan «Emprendedor» heredado. Parece una página más vieja que la otra; no pude fecharlas. No uso los porcentajes de 1% y 0,25% como vigentes.
- Precio de los planes de Tiendanube AR: el buscador mostró Impulso $78.999 y Escala $234.999; la página de planes que abrí dice $79.999 y $244.999. Uso la página abierta.
- Tiendanube México (3.11): PDV Inicial gratis; PDV Plus en los planes de pago (de $149 MXN por mes); caja, escáner, división de pagos. Es México, no Argentina.

### Sistemas de gestión (una línea cada uno; otro agente hace la ficha)

- Fudo: funciona como POS de restaurante (comandas, caja, terminal de pagos integrada, ARCA, tienda online propia); no menciona Tiendanube ni Point. https://fu.do [M] — C-3.
- Dux, Bsale, Contabilium, Tango Punto de Venta: no verificados (la página de Dux solo redirige; Bsale no resolvió el dominio probado). Hueco.

### Recurso canónico propuesto

Para precios y funciones de POS: la ayuda oficial de cada proveedor, con fecha de consulta. Para comisiones: la página de costos de Mercado Pago (la que dio 403 con el lector, hay que verla en navegador) y las de cada adquirente; la nota de iProUP sirve como comparación fechada pero no como fuente de verdad.

---

## Componente 4. Reseñas de los POS

### Alcance real (declarado)

| App | Dónde | Qué leí | Observación |
|---|---|---|---|
| Mercado Pago: cuenta digital (id 925436649) | Feed de App Store AR | 500 reseñas, todas de 2026 (2026-05-22 a 2026-11-20); estrellas: 1 = 280, 2 = 57, 3 = 37, 4 = 24, 5 = 102 | Es la billetera del consumidor, no una app de negocios; el feed `.../customerreviews/id=925436649/sortby=mostrecent/json` |
| Nube, app de compras de Nuvemshop (id 1666924494) | Feed AR | 272 reseñas, 2024-11-23 a 2026-11-17 | App de comprador (seguimiento de pedidos), no de comercio |
| Tiendanube, app del comercio (id 1038913504) | Feed AR | 245 reseñas, 2016-07-09 a 2026-10-28 | App de administración; sin sección de POS visible |
| Shopify: administra tu negocio (id 371294472) | Feed AR | 25 reseñas, 2018 a 2026-10-14 | Ninguna menciona POS |
| Shopify Point of Sale (id 686830644) | Feed AR | 0 reseñas | Sin reseñas en AR |
| Shopify POS en Google Play | Página [L], 3,8 estrellas, 3,38 mil opiniones | Solo leí las 3 reseñas visibles, no el total | Reseñas de 2021, 2022 y 2026, no filtradas por país |
| Tiendanube/Nube en Google Play (4,7 y 4,5), Point | Solo vi la calificación en una búsqueda de la tienda | No leí reseñas | Hueco |
| App de Mercado Pago Point / «para negocios» | No encontré una app separada en la tienda AR de Apple (la búsqueda devolvió la de la billetera) | — | Hueco |

Resultado importante: **no hay una masa de reseñas públicas específica del POS de Tiendanube ni de Mercado Pago Point que se pueda codificar**; el POS de Tiendanube vive dentro de la app de administración y las reseñas de esa app casi no lo mencionan. Lo que sigue es la codificación de lo que sí hay, sin pretender que sea la voz del comercio con POS.

### Codificación por tema (conteos sobre lo que leí; citas cortas sin autor)

**Mercado Pago, billetera (2026, 500 reseñas leídas por filtro de palabras; 14 mencionan negocio, lector, posnet, cobro o vendedor; ninguna habla del lector Point en sí)**

| Tema | n (de 14) | Cita corta |
|---|---|---|
| Piden usar posnet o restringen anticipos al vendedor | 1 | «Me piden que use el posnet y yo vendo desde link virtual» |
| Posnet defectuoso (ambiguo, puede ser tarjeta) | 1 | «ya me dieron 3 y los 3 son malísimos» |
| Cobro/sistema de cobros en general, sin detalle | 2 | «Es una vergüenza el sistema de cobros» |
| Cuenta compartida entre dos vendedores | 1 | «DOS BILLETERAS EN UNA» (título) |
| Fallas de transferencia o QR (lado comprador) | 2 | «nunca aparece el comprobante ni le llega al vendedor» |
| Resto: consumo, estafas, cargos, crédito | 7 | — |

**Tiendanube, app del comercio (245 reseñas; 2024-2026: 0 sobre POS)**

| Tema | n | Cita |
|---|---|---|
| Stock desincronizado entre local y tienda (2020, fuera de rango) | 1 | «vendí en mi local algo que ya había vendido por la tienda y era el último que tenía en stock» |
| Pedido de más reportes (2017, fuera de rango) | 1 | «Muy básico vs sistemas similares» |

**Nube, app de compras (2024-2026; 4 de 272 hablan de sucursal)**

| Tema | n | Cita |
|---|---|---|
| Retiro en sucursal del correo: seguimiento mal informado | 3 | «Dice “en camino” cuando el producto ya estaba hace 5 días esperando» |
| Pedido no entregado, no es de POS | 1 | — |

**Shopify POS, Google Play (3 reseñas visibles)**

| Tema | n | Año | Cita |
|---|---|---|---|
| Lentitud de búsqueda y de la grilla de artículos | 2 | 2021, 2022 | «tardadisimo y muy tedioso hacer esperar al cliente» |
| Cada actualización empeora el flujo (caja, cierres, devoluciones) | 1 | 2026 | «Procesar ventas es una pesadilla de clics infinitos» |

**Separación 2024-2026 contra antes:** de lo que leí, solo 1 reseña de POS es de 2024-2026 (Shopify POS, mayo de 2026); las demás son anteriores. La base es demasiado chica para conclusiones; sirve para formular hipótesis: la fricción en el mostrador (velocidad de búsqueda, clics) y la sincronización del stock entre local y tienda.

Fuentes: feeds de App Store AR (https://itunes.apple.com/ar/rss/customerreviews/id=<ID>/sortby=mostrecent/json, el feed devuelve hasta 500 reseñas) [L]; https://play.google.com/store/apps/details?id=com.shopify.pos&hl=es_AR&gl=AR [L]. Calificación de fuente: C (reseñas anónimas, muestra parcial); de dato: 5.

---

## Huecos

1. Precio de un punto de venta Plus adicional en Argentina y en cada plan: no está en los extractos de las ayudas ni en la página de planes de Argentina; México lo tiene en una tabla ($399, $249, $149, $99 MXN según un resultado del buscador, sin saber qué columna es cuál [S]). Verificar en navegador.
2. Página de costos de Mercado Pago Point (3.8): 403. Se usó la página de Point Smart. Falta el precio del Point Pro y de otros modelos en Argentina.
3. Mercado Pago como software de gestión o POS propio en Argentina: no se encontró, pero la búsqueda fue acotada; sí existe en México ($99 MXN por mes, [S]). Falta mirar comunicados de 2025-2026.
4. Shopify en Argentina: factura de ARCA por apps, hardware soportado, y la lista oficial de países para POS. Solo está confirmado que Argentina no figura entre los países de Shopify Payments.
5. Getnet, Nave, Payway, Ualá Bis, MODO: sin fuente oficial; solo la nota de iProUP; integración con POS no confirmada (salvo MODO en Tiendanube).
6. Dux, Bsale, Contabilium, Tango y su sincronización con la tienda: sin verificar.
7. Ship from store, reserva de stock del local y devolución en el local de una compra online: sin documentación argentina; Shopify lo describe en genérico.
8. Estudios de América Latina sobre omnicanalidad o BOPS: no encontrados (búsqueda acotada por el presupuesto).
9. Manual de retail como recurso canónico del POS: no abierto.
10. Reseñas: faltan Google Play de Tiendanube/Nube y de las apps de Point; Shopify POS en App Store AR sin reseñas.
11. El paper completo de Gallino y Moreno y su gráfico de efectos por canal (+4%, -2%, +6%) no se verificaron.
