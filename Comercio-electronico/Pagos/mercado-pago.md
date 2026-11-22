---
resumen: >-
  Los datos públicos de Mercado Pago como medio de cobro de tiendas online en Argentina: sus tarifas por plazo y por cuotas, sus productos para cobrar online, lo que deja hacer a plataformas y desarrolladores, lo que se reserva en sus términos y su movida hacia la gestión del comercio con Cuenta Negocio, consultados el 2026-11-22.
estado: borrador
estabilidad: volatil
fuentes:
  - "Mercado Pago Developers, índice de la documentación: https://www.mercadopago.com.ar/developers/es/docs (leído con navegador, 2026-11-22; A2)"
  - "Mercado Pago, términos y condiciones para desarrolladores: https://www.mercadopago.com.ar/developers/es/docs/resources/legal/terms-and-conditions (leídos enteros, 2026-11-22; A1)"
  - "Mercado Pago, cómo integrar el checkout en marketplace: https://www.mercadopago.com.ar/developers/es/docs/checkout-pro-preferences/how-tos/integrate-marketplace (leído 2026-11-22; A2)"
  - "Mercado Pago, Checkout Pro, resumen: https://www.mercadopago.com.ar/developers/es/docs/checkout-pro/overview (leído 2026-11-22; A2)"
  - "Mercado Pago, reporte de liquidaciones, campos: https://www.mercadopago.com.ar/developers/es/docs/checkout-api-orders/resources/reports/released-money/report-fields (leído 2026-11-22; A2)"
  - "Mercado Pago, apps para plataformas: https://www.mercadopago.com.ar/developers/es/docs/shopify/introduction (leído 2026-11-22; A2)"
  - "SpomBridge, Comisiones de Mercado Pago 2026: https://app.spomsolutions.com/herramientas/comisiones-mercado-pago-2026 (leído con navegador, 2026-11-22; C3, vende un sistema de gestión; dice haber relevado la página oficial el 2-nov-2026)"
  - "Mercado Pago, link de pago: https://www.mercadopago.com.ar/herramientas-para-vender/link-de-pago (2026-11-22: una lectura dio los mismos valores que SpomBridge y otra devolvió 403)"
  - "Mercado Pago, sección de costos y ayuda de comisiones: https://www.mercadopago.com.ar/costs-section y https://www.mercadopago.com.ar/ayuda/26748 (403 el 2026-11-22; F6)"
  - "Mercado Pago, Partners Program: https://mercadopago.com.ar/partners/developers/en/details (403 el 2026-11-22; niveles según el buscador sobre las páginas de Brasil y Chile; B4)"
  - "iProUP, Mercado Pago lanza Pagos rápidos, tarjetas y seguros para comercios (10-sep-2026): https://www.iproup.com/finanzas/71416-mercado-pago-lanza-pagos-rapidos-tarjetas-y-seguros-para-comercios (leída con navegador; B3, las cifras son dichos de la empresa)"
  - "iProfesional, Mercado Pago relanza Mago con IA (30-sep-2026): https://www.iprofesional.com/finanzas/465587-mercado-pago-relanza-mago-con-ia-para-gestionar-las-finanzas (leída; B3)"
  - "El CEO, Cuenta Negocio en México (4-sep-2026): https://elceo.com/negocios/mercado-pago-acelera-su-apuesta-por-las-pymes-en-mexico-con-cuenta-negocio/ (leída; C3)"
  - "WordPress.org, plugin de Mercado Pago para WooCommerce: https://wordpress.org/plugins/wp-json/plugins/v1/plugin/woocommerce-mercadopago (leído 2026-11-22; A2)"
  - "iProfesional, comisiones de Mercado Pago (1-ago-2023): https://www.iprofesional.com/tecnologia/386153-mercado-pago-que-debes-saber-sobre-comisiones-plazos-y-montos (leída; B2, antecedente)"
  - "Experiencia propia, noviembre de 2026, una empresa de software de comercio electrónico: recorrido de dos checkouts de Shopify en pesos que cobran con Mercado Pago, hasta antes de pagar"
aliases: [Mercado Pago, MercadoPago, Checkout Pro, Checkout API, Bricks, link de pago, Cuenta Negocio, Mago, marketplace_fee, application_fee]
creado: 2026-11-22
revisado:
---

# Mercado Pago

Los datos públicos de Mercado Pago como medio de cobro de tiendas online en Argentina: sus tarifas por plazo y por cuotas, sus productos para cobrar online, lo que deja hacer a plataformas y desarrolladores, lo que se reserva en sus términos y su movida hacia la gestión del comercio con Cuenta Negocio, consultados el 2026-11-22.

Es un caso de agregador, en el sentido de [actores del pago](actores-del-pago.md): cobra por muchos comercios bajo su propia cuenta. Es una unidad de negocio de MercadoLibre S.R.L., la empresa del marketplace [Mercado Libre](../Plataforma-de-tiendas/mercado-libre.md), cuyo negocio fintech en Argentina fue de US$ 3.928 millones en 2025, casi el doble que el de comercio, según el 10-K. Consultado el 2026-11-22. Las páginas comerciales (costos, ayuda, partners) devolvieron 403 a la lectura automática; la documentación para desarrolladores abrió y se leyó directo. La escala de calificación de cada fuente está en [fuentes públicas](../../Estrategia-competitiva/Analisis-de-competidores/fuentes-publicas.md#quién-lo-dice-y-si-está-confirmado).

> [!WARNING]
> Ley y dinero: la ficha no reemplaza el consejo de un contador ni la tarifa que Mercado Pago le muestra a cada comercio en su cuenta.

## Tarifas por plazo y por cuotas

Copiado de SpomBridge, que dice haberlas relevado de la página oficial el 2-nov-2026, con tablas «vigentes desde el 6 de marzo de 2026» (C3: una sola fuente para los valores de 2026). Valen para Link de pago y Checkout Pro, con cualquier medio de pago, más IVA. La sección oficial de costos dio 403.

| Plata disponible | Ciudad de Buenos Aires y otras 8 provincias | Provincia de Buenos Aires y Córdoba |
|---|---|---|
| Al instante | 6,29% | 6,6% |
| A 10 días | 4,39% | 4,61% |
| A 18 días | 3,39% | 3,56% |
| A 35 días | 1,49% | 1,56% |
| Cuotas sin interés, se suma | 2: 7,79%; 3: 10,49%; 6: 18,69%; 9: 26,49%; 12: 32,29%; 18: 41,59% | ídem, «puede variar según los impuestos de tu provincia» |

Con tarjetas extranjeras se suman 3 puntos. Las retenciones de impuestos no son comisión. Las ventas hechas en el marketplace Mercado Libre no pagan comisión de Mercado Pago aparte: pagan los cargos de Mercado Libre. No hay abono mensual. La forma coincide con las fuentes de 2023 que reúne [costos de cobro en Argentina](costos-de-cobro-en-argentina.md): más barato cuanto más espera el comercio. Por qué el plazo tiene precio está en [costo de cobrar](costo-de-cobrar.md).

## Productos para cobrar online

| Producto | Qué hace, según su documentación |
|---|---|
| Checkout Pro | el comprador «es dirigido a una página de Mercado Pago para completar el pago»; decide si sigue con su cuenta o como invitado, elige un medio guardado o uno nuevo y vuelve al sitio |
| Checkout API y Bricks | el pago queda dentro del sitio del comercio |
| Link de pago | cobra un monto sin sitio web; según el buscador, no tiene catálogo en Argentina. «Tu link», un enlace único del negocio para cualquier monto, sale de un resumen del buscador, sin verificar |
| Suscripciones | cobro recurrente |
| Integraciones listas | Tiendanube, Shopify, WooCommerce, VTEX, PrestaShop, Adobe Commerce, BigCommerce y Salesforce Commerce Cloud |
| Para desarrolladores con IA | un servidor MCP oficial, un plugin para Claude Code y una CLI |

El plugin de WooCommerce tiene más de 100.000 instalaciones activas y 693 calificaciones: 451 de 5 estrellas y 148 de 1, una J con poco en el medio (versión 8.10.3 del 18-nov-2026). En dos tiendas de Shopify en pesos recorridas hasta antes de pagar, Mercado Pago aparecía debajo de la tarjeta con el aviso «Se te redirigirá a Mercado Pago para completar tu compra»; una ofrecía además 10% de descuento por transferencia. Cómo cambia el checkout según la plataforma está en [checkout por plataforma](../Checkout-y-conversion/checkout-por-plataforma.md).

## Lo que deja hacer a terceros

- **Cobrar una comisión de plataforma dentro del pago.** Con `marketplace_fee` en Checkout Pro y `application_fee` en Checkout API: «Ambos checkouts reparten automáticamente los importes entre el vendedor y el marketplace […] primero se descuenta la comisión de Mercado Pago, y la comisión del marketplace se descuenta del saldo restante». El vendedor autoriza con OAuth. Es la forma técnica de lo que [el negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md) llama cobrar por venta, sin pasarela propia.
- **Leer los costos de cada cobro.** El reporte de liquidaciones, que se genera por API, trae por operación `MP_FEE_AMOUNT` («Comisión de Mercado Pago y/o Mercado Libre. Incluye IVA»), `FINANCING_FEE_AMOUNT` (cuotas sin interés), `SHIPPING_FEE_AMOUNT`, `TAXES_AMOUNT` (impuestos retenidos por jurisdicción), contracargos y cupones. Que las ventas de Mercado Libre aparezcan ahí con sus cargos es inferencia por el nombre del campo, sin probar con una cuenta.
- **Ganar por integrar.** Su Partners Program promete «una comisión por cada integración realizada», descuentos a los clientes del integrador y atención prioritaria; los niveles van de Certified a Platinum según el volumen de los clientes, según el buscador. La página del programa dio 403.

Los términos para desarrolladores, leídos enteros, ponen el borde. La licencia es «limitada, no exclusiva, personal, revocable, y no transferible», para «facilitar, mejorar y/o potenciar el uso y las funcionalidades del Sitio y de los servicios prestados por Mercado Pago». Mercado Pago:

| Se reserva | Lo que dicen los términos |
|---|---|
| Competir con las apps | «podrá desarrollar productos, servicios o aplicaciones que puedan competir con las Aplicaciones» |
| Revocar el acceso | «sin expresión de causa y en cualquier momento, sin necesidad de notificarlo» |
| Cambiar la API | sin obligación de mantener compatibilidad, con cambios «sustanciales» a costo del desarrollador; puede limitar las llamadas y cobrar el exceso, y exigir certificación |
| Cambiar los términos | con 10 días de aviso |
| Prohibir | guardar datos de tarjetas, de forma «expresa e irrestricta» (7.2.I); revender la API con una app «que funcione sustancialmente de la misma manera que la API» (7.2.A); usar «mercado», «libre», «pago», «shops», «envíos» o «crédito» en el nombre de la app |

Los términos del marketplace dicen algo parecido, y están en [Mercado Libre para desarrolladores](../Plataforma-de-tiendas/mercado-libre-para-desarrolladores.md). Por qué una plataforma abre y se reserva competir lo explica [competencia con la plataforma](../../Producto/Plataformas/competencia-con-la-plataforma.md).

## Cuenta Negocio: del cobro a la gestión

En el evento Meli Experience, el 10-sep-2026, Mercado Pago lanzó Cuenta Negocio en Argentina, para «convertirse en la cuenta desde la que un negocio pueda cobrar, administrar su dinero, financiarse y gestionar su operación cotidiana», con herramientas de «cobro multicanal, de soluciones financieras y de software de gestión», según iProUP. La misma nota dice que «la compañía también trabaja en herramientas de inventario, stock, clientes, facturación y punto de venta». En México, Cuenta Negocio ya ofrece «software para administrar inventarios y facturación», según El CEO (4-sep-2026).

| Anuncio | Lo que dice la empresa, según iProUP |
|---|---|
| Mago, su asistente de IA | «uno de cada cinco vendedores interactúa con Mago»; el 60% de las consultas lo usa «como un socio del negocio» y le pide reportes de ventas, vencimientos y recomendaciones de productos |
| Pagos Rápidos | usa sus «90 millones de tarjetas […] guardadas y tokenizadas» para que el comprador no cargue datos en una tienda online; dice que podría dar «10 puntos porcentuales de mayor conversión» |
| Cuotas de su tarjeta de crédito | sin costo para el comercio, en QR y Point (presencial) |

Son dichos de la empresa, sin verificar. Una nota de iProfesional del 30-sep-2026 describe a Mago para finanzas personales y, para comercios, pagos programados a proveedores y transferencias múltiples, sin hablar de reportes de ventas. Qué reportes da hoy no se leyó.

> [!NOTE] Sin fuente todavía: la tarifa oficial vigente, leída en la sección de costos; qué incluye hoy Cuenta Negocio en Argentina y cuándo llegan inventario y facturación; las condiciones del Partners Program; si una tienda propia que cobra con Mercado Pago sufre retenciones de dinero como las que cuentan los vendedores del marketplace; y la página a la que redirige Checkout Pro.
