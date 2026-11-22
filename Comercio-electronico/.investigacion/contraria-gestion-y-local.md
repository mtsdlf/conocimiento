# Posición contraria: sistemas de gestión, local físico con venta online y factura electrónica en Argentina

Consulta: 2026-11-22. Rol: buscar la mejor evidencia en contra del barrido previo. Solo fuentes públicas.

Escala. Fuente: A oficial/primaria, B prensa fechada, C proveedor o blog comercial (con interés), E foro. Puntaje de fuente 1-3 (3 = pesa más). Dato 1-6 (1 = confirmado por dos fuentes independientes, 2 = probable, 3 = posible, 4 = dudoso, 5 = improbable, 6 = no evaluable). Marcas: [L] texto completo abierto (las abiertas con WebFetch pasaron por un resumidor: las citas literales vienen de él), [M] metadatos, [S] resumen del buscador. Máximo tres rondas por afirmación; lo no decidido va como hueco.

## Resumen de veredictos

| # | Afirmación | Veredicto |
|---|---|---|
| 1 | PDV de Tiendanube sin factura ARCA, cobro manual con lector externo, QR solo MODO | Se sostiene, con una corrección: la factura sí se emite en apps oficiales de la tienda; integración con Point no encontrada |
| 2 | Shopify POS no disponible en Argentina con precio local ni factura ARCA | Se corrige: la app POS no está bloqueada por país; lo que falta es Shopify Payments/hardware propio, precio en pesos y factura nativa |
| 3 | Precios Dux y Contabilium | Se sostiene (verificados hoy, con los planes intermedios de Dux) |
| 4 | Quejas concentradas en sincronización con Mercado Libre y tiendas | No se puede decidir: no hay evidencia independiente de ninguna queja principal |
| 5 | Point sin integración directa con facturación | Se corrige: hay API oficial de Point para sistemas de punto de venta; lo que no cubre es la factura ARCA |
| 6 | Mercado Pago anunció software de gestión | Se sostiene para México; no hay evidencia de que exista en Argentina |
| 7 | Medio vacío entre PDV sin factura y gestión de $36.000 a $245.000 | Se cae como está escrita: hay oferta intermedia y gratuita |
| 8 | Supuestos de fondo | Parcialmente respaldados o sin respaldo; ver sección |

## 1. Punto de venta de Tiendanube

Veredicto: **se sostiene en lo central; se corrige en que "no emite factura" no equivale a "no hay factura en la tienda"**.

Evidencia:
- Ayuda de Tiendanube, "Qué es Punto de Venta" (A, 3, [L], 2026-11-22): el cobro es manual (efectivo, transferencia, "terminal de pago externa (como Mercado Pago, Getnet, Nave, entre otras)"), o QR de Pago Nube: "Por el momento, esta forma de pago está disponible para abonar a través de MODO." También permite "Pago pendiente" y link de carrito. La página no dice nada de facturación ni de lectores de tarjeta integrados. Dato 1 (confirma la afirmación 1). https://ayuda.tiendanube.com/es_AR/pdv/que-es-punto-de-venta-de-tiendanube
- Ayuda de Tiendanube, "Cómo facturar las ventas" (A, 3, [L]): "El proceso de facturación para las ventas que hacés en tu tienda online o con la funcionalidad 'Punto de Venta' debe realizarse externamente, ya que no se realiza a través de la plataforma de Tiendanube." Apps integradas listadas: Facturante, iFactura, Contagram, Contabilium, Xubio, Ecomm-App, Netegia, Nymeria, Tango Factura, Ecomgestión. "Si usás Pago Nube, la facturación automática solo está disponible con Facturante." Dato 1. https://ayuda.tiendanube.com/es_AR/123288-mis-ventas/como-facturar-las-ventas-de-mi-tiendanube
- Búsqueda sobre la ayuda del PDV (A, [S]): 7 días de prueba y después plan Punto de Venta Lite (gratuito) o Plus; Lite con "integración nativa con hardware" (lector de código de barras, impresión de tickets). Página actualizada, según el resumen, el 30/09/2026. Dato 2.
- Marketplace de apps de Tiendanube (C, 2, [S] y un [L]): Factuok, "$ 15.999/mes", "30 días gratis", factura A/B/C con CAE y mail al comprador, "cuando te pagan" (Dato 2; la ficha no dice que funcione con ventas del PDV físico, solo con ventas de la tienda). Lannis: US$ 6 a US$ 70 por mes. También Facture.ar, Factureo, S360, Facturante, Contabilium, Tilo.ar. https://www.tiendanube.com/tienda-aplicaciones-nube/factuok

Corrección propuesta: decir "Tiendanube no factura por sí misma ni en la tienda ni en el PDV; remite a apps de terceros, algunas desde US$ 6 o $15.999 por mes". No hay app oficial propia de Tiendanube: las apps son de terceros publicadas en su marketplace (hueco: no se vio si alguna está "certificada" por Tiendanube).

Integración con Point: no se encontró. La documentación de Point (API de integración con puntos de venta) existe y Tiendanube no figura en lo abierto. Hueco declarado (la búsqueda no lo prueba, solo no lo encontró).

## 2. Shopify POS

Veredicto: **se corrige**.

- Ayuda de Shopify, requisitos del POS (A, 3, [L]): no lista países ni nombra Argentina. Dato 6.
- Búsqueda (A, [S]): Shopify dice que se puede usar POS "in nearly every country", pero Shopify Payments y el hardware integrado están "available only in select regions". Argentina no aparece en la lista de Shopify Payments para POS (Australia, Bélgica, Canadá, Dinamarca, Finlandia, Alemania, Irlanda, Italia, Países Bajos, Nueva Zelanda, Singapur, España, Reino Unido, Estados Unidos). Dato 2. https://help.shopify.com/en/manual/sell-in-person/getting-started/setup-payment-method/compliance
- Precio: no se encontró precio en pesos para Argentina; las páginas de planes vistas (México, Colombia) muestran USD (p. ej. Basic USD 19 por mes en México; USD 25 en Colombia, [S]). Un hilo de la comunidad de Shopify (E) menciona "19$/mes" para Argentina. Dato 3. Un comparador (hacecuentas, C) convierte a unos $34.000 por mes; dato 4.
- Factura: respuesta en la comunidad de Shopify (A/E, [S]): Shopify "no puede confirmar cumplimiento AFIP ni conexión directa de esas apps". Apps de terceros: Emitio (desde US$ 15 por mes), Profitar (US$ 24 por mes). Dato 2.

Lo que se cae: "no está disponible". Lo que se sostiene: sin precio en pesos, sin factura nativa, sin cobro integrado presencial con tarjeta. Hueco: no se confirmó si Shopify cobra en ARS a Argentina.

## 3. Precios

Veredicto: **se sostiene**.

- Dux (A, 3, [L] por el lector de páginas; la fetch normal dio 403): título "Planes desde $36.000 +IVA por mes". Inicial $36.000 (hasta 250 comprobantes, 1 tienda online), Estándar $75.300 (1.500 comprobantes, 3 tiendas), Pro $111.200 (5.000, 4 tiendas, API), Full $150.300 (ilimitados, 5 tiendas, API), todos "+ IVA por mes". Complementos: usuario adicional $4.700 + IVA, catálogo online $6.000, contabilidad avanzada $10.000, integración VTEX $30.000. "Soporte 24/7", "Sin límite de permanencia". Importante: "no se pueden cargar datos históricos como ventas o cuentas corrientes" al migrar. Dato 1. https://www.duxsoftware.com.ar/precios
  Matiz: el límite de 250 cuenta "tanto facturadas como no facturadas".
- Contabilium (A, 3, [L]): Standard $122.000 + IVA, Pro $179.000 + IVA, Full $245.000 + IVA por mes; anual con 10% de descuento (Standard $109.800, Pro $161.100, Full $220.500); Enterprise a cotizar; "punto de venta extra" $28.000 + IVA (la página no aclara si es mensual o único). Dato 1. https://contabilium.com/ar/planes
- Comparador de un competidor (C, [S]): Xubio Estándar ~$162.503 con IVA, Contabilium PyME ~$118.580, Tango ~$638.880 o más. Discrepa con Contabilium (que el competidor muestra desactualizado o con otro plan). Dato 4.

## 4. Quejas principales de los sistemas de gestión

Veredicto: **no se puede decidir**.

- No se hallaron hilos de Reddit ni de foros de contadores con búsquedas generales; los resultados fueron blogs de proveedores competidores (YoFacturo, SpomBridge, Tiendanube). Sesgo declarado.
- Reseñas independientes de Dux (Capterra, GetApp, G2, [S], C/E): 3,7/5, "70%" recomiendan sobre 10 respuestas; G2 solo 5 reseñas. Muestra ínfima. Las reseñas citadas en el sitio de Dux (propias) elogian el soporte.
- Evidencia de que parte de las fallas de sincronización vienen del lado de Mercado Libre: un proveedor (UpSeller, C, [S]) reconoce que falla la sincronización "debido a la inestabilidad de la interfaz de Mercado Libre"; y las causas más citadas de desfase son datos mal vinculados (productos duplicados, publicaciones no enlazadas). Dato 3.
- Ningún dato mide qué queja es la principal. La afirmación 4 queda sin respaldo ni refutación. Falta: un barrido de reseñas por tema (Capterra/G2/Trustpilot/Play Store) con conteo.

## 5. Mercado Pago Point y la facturación

Veredicto: **se corrige**.

- Documentación de Mercado Pago Argentina, API de Point para punto de venta (A, 3, [L]): conecta terminales Point con un POS "para recibir pagos en las terminals que tengas configuradas"; "soporta dispositivos Point Plus (POS) y Point Smart"; "sólo permite tarjetas, contactless y SWIFT"; aviso: una nueva API (Orders) "descontinuará la actual", migración sin fecha. Dato 1. https://www.mercadopago.com.ar/developers/es/docs/mp-point-legacy/integration-configuration/integrate-with-pdv/introduction
- Búsqueda (A, [S]): la integración permite "procesar pagos presenciales con tarjetas y realizar una conciliación automática"; terminales compatibles Point Smart 1 y 2. No documenta factura ARCA.
- Sistemas que la usan (C, [S]): YoFacturo (plan Emprendedor $20.000 por mes) factura automáticamente cobros de Mercado Pago, con el Point "en modo PDV"; Tributo Simple conecta Mercado Pago, Mercado Libre y Point Smart. Dato 2 (páginas de proveedores). https://yo-facturo.com/mercado-pago-point-y-qr/

Corrección: Point sí se integra directamente con sistemas de punto de venta por API oficial; lo que no hace Mercado Pago es emitir la factura ARCA. "En paralelo, sin integración" vale solo para quien usa el Point suelto (como el PDV de Tiendanube, que remite a "terminal externa").

## 6. Mercado Pago y el software de gestión

Veredicto: **se sostiene para México; sin evidencia para Argentina**.

- DPL News (B, 2, [L], 2025-07-04): "nuevo software de Punto de Venta" de Mercado Pago en México, "Disponible para todos los comercios que aceptan pagos con tarjeta a través de la terminal Point Smart", más de 1.000 comercios "a tan solo semanas de su lanzamiento", $99 pesos mexicanos por mes o $950 por año; no menciona otros países. Dato 2. https://dplnews.com/?p=280390
- Excélsior y LatamFintech (B, [S]): controla ventas, inventario, colaboradores y facturación; surgió de una encuesta a más de 3.000 comercios, "88%" necesitaba software de gestión. Un título de LatamFintech habla de "para pymes en LATAM" ([M]/[S], sin abrir): hueco, podría haber plan regional. Las páginas oficiales halladas son todas de mercadopago.com.mx.
- Argentina: solo se halló la presentación de Point Smart (febrero de 2021, Android "permitirá sumar funcionalidades para la gestión", [S]). Ninguna página argentina de software de gestión de Mercado Pago. Hueco: confirmar en mercadopago.com.ar/herramientas-para-vender.

## 7. El "medio vacío"

Veredicto: **se cae como está escrita** (hay oferta; lo que queda por probar es si cubre el PDV físico más tienda online).

- Facturadores baratos en la tienda de Tiendanube: Factuok $15.999 por mes, Lannis US$ 6 por mes, Facture.ar (free con 10 facturas por mes; US$ 9,99 por mes con 1.000, [S]). Dato 2.
- Facturadores con POS: YoFacturo kioscos $20.000 por mes, con POS integrado, ARCA, 1 usuario, 500 productos y 1 punto de venta (C, [S]). Dato 3. Tilo.ar: gestión con factura y integración con Tiendanube, sin comisión por venta (C, [S]).
- Dux Inicial $36.000 y Contabilium arrancan arriba del tramo anterior, pero el vacío de $15.999 a $36.000 está poblado.
- Gratis: ARCA, "Comprobantes en línea" (A, [S]): servicio con clave fiscal; "¿Cuál es el costo? Gratuito". Y el "Facturador" (app/web) para monotributistas, que ARCA aclaró que "no es obligatorio", pensado para ventas simples a consumidor final (tiques C). Tope de $500.000 por operación según un blog (C): no verificado en fuente oficial. Dato 2. https://www.arca.gob.ar/facturacion/monotributo/modalidades.asp
- Kyte y Fudo: no se encontró evidencia de precios ni de factura ARCA en Argentina (la ficha vista de Kyte es la de México). Hueco, no refutación.
- Lo que sí sigue "vacío" (no refutado): un producto que junte PDV físico, tienda online, stock compartido y factura en un precio de $15.000-$36.000; no se buscó ni se halló.

## 8. Supuestos de fondo

- **Los comercios quieren integrar canales.** No se halló encuesta que lo respalde ni que lo refute (hueco). Contrapunto: la propia ARCA ofrece gratis Comprobantes en línea y el Facturador, y el PDV de Tiendanube admite "Pago pendiente" y cobro manual, lo que muestra que el flujo mínimo (cobrar y facturar aparte) es el normal hoy. Dato 3.
- **La omnicanalidad conviene.** Evidencia mixta, no negativa en general. Gallino y Moreno (Management Science, [S]; texto completo no abierto): en un retailer grande, ofrecer retiro en tienda (BOPS) bajó las ventas online, pero subió el tráfico y las ventas en tienda, por la percepción de confiabilidad del stock. Showrooms sin inventario de marcas digitales: más ventas y menos devoluciones (Bell, Gallino, Moreno, [S]). Un estudio de 2023 en Journal of Marketing (B/A, [S]) halló canibalización de las ventas online propias al abrir una tienda de marca en supermercados, con efecto positivo en el canal supermercado. Todos son retailers grandes de otros países; nada sobre pymes argentinas. No se halló un Gallino-Moreno que mida canibalización pyme. Dato 3.
- **Informalidad.** CAME (B, [S]): "seis de cada diez comercios operan por fuera de las regulaciones legales" (informe "Soberanía Informal", Comisión de Fronteras e Ilegalidad); la nota tiene un titular que dice 60% del PBI y que el cuerpo no respalda. Mide estar fuera de la regulación, no solo no facturar. No hay cifra oficial de comercios que no facturan. Dato 4. Ventas minoristas pyme CAME: mayo de 2026 -1,2% interanual, -3,1% acumulado en el año. Esto sí achica el mercado de pago por software, pero no con cifra propia.
- **Costos de cambio.** Dux declara que al migrar no se cargan ventas ni cuentas corrientes históricas (A, [L]); solo clientes, proveedores, productos, precios y stock por planilla. Un cliente citado en su web dice haber dudado en migrar (testimonio propio, C). Dato 2. Contabilium cobra el punto de venta extra aparte. No hay estudio de abandono.
- **Controlador fiscal vs factura electrónica.** ARCA (A, [S]): los monotributistas deben emitir comprobantes electrónicos tipo C a consumidores finales; las modalidades incluyen Comprobantes en línea, Facturador, Facturador móvil y controlador fiscal de "nueva tecnología". Un blog (C) dice que un kiosco monotributista "No necesitás comprar controlador fiscal"; no se encontró frase oficial que lo diga expresamente. Concepción errónea documentada: confundir "obligación de facturar" con "obligación de comprar un controlador fiscal" (el controlador es una modalidad entre varias). Dato 3.

## Concepciones erróneas documentadas

1. "Si uso Tiendanube, factura sola": la ayuda oficial dice que la facturación se hace externamente (A).
2. "El Punto de Venta de Tiendanube cobra con tarjeta": cobra con QR (hoy solo MODO) o registra un cobro hecho en una terminal externa (A).
3. "Facturador de ARCA sirve para todo": es solo para monotributistas, tiques C a consumidor final, y no es obligatorio (A).
4. "Hace falta controlador fiscal": no es obligatorio para el monotributista, que puede usar Comprobantes en línea o el Facturador (A parcial).
5. "Shopify POS no existe en Argentina": la app no tiene bloqueo por país; faltan pagos y hardware integrados (A).
6. "Mercado Pago ya tiene software de gestión en todos los países": solo México confirmado (B).
7. "Los precios de internet de sistemas de gestión": un comparador advierte de cifras bajas obsoletas que circulan (p. ej. "Xubio $3.500") (C).
8. "Más canales siempre suman": la evidencia es contingente al canal y al retailer (ver 8).

## Huecos

- App oficial o certificada de facturación propia de Tiendanube; integración Tiendanube-Point.
- Precio en ARS de Shopify para Argentina.
- Existencia del software de gestión de Mercado Pago en Argentina; lo "LATAM" de LatamFintech sin abrir.
- Precios y facturación de Kyte, Fudo, TusFacturas y Alegra en Argentina (no hallados en fuente oficial).
- Queja principal de los usuarios de sistemas de gestión: sin datos independientes; falta barrido de reseñas.
- Cifra oficial de comercios sin factura; informe CAME original no abierto.
- Texto completo y tamaños de efecto de Gallino y Moreno; nada sobre pymes argentinas.
- Tope de $500.000 del Facturador sin fuente oficial.
- Sin hilos de Reddit ni foros de contadores: la búsqueda web no los devolvió.
