---
resumen: >-
  Quién le vende herramientas al comercio argentino que vende por chat, con su precio de lista al 2026-11-22: los proveedores de la API de WhatsApp, las bandejas, bots y CRM, los catálogos que mandan el pedido al chat, las apps de WhatsApp de las plataformas de tiendas y los links de pago.
estado: borrador
estabilidad: volatil
fuentes:
  - "Twilio https://www.twilio.com/en-us/whatsapp/pricing; 360dialog https://360dialog.com/pricing; Gupshup https://www.gupshup.ai/isv-partners/whatsapp-api/pricing (leídas; A2)"
  - "Wati https://www.wati.io/pricing/ (A3) y eesel https://www.eesel.ai/blog/wati-pricing (C3) (leídas)"
  - "Cliengo https://www.cliengo.com/pricing; Botmaker https://botmaker.com/es/precios/; Leadsales https://www.leadsales.io/precios; Kommo https://www.kommo.com/pricing/; Zenvia https://www.zenvia.com/es/precios/; B2Chat https://www.b2chat.io/precios/; Callbell https://www.callbell.eu/es/precios/; SleekFlow https://sleekflow.io/es/pricing; Respond.io https://respond.io/pricing (leídas el 2026-11-22; A2)"
  - "Waspy y Wames en la tienda de apps de Tiendanube: https://www.tiendanube.com/tienda-aplicaciones-nube/waspy (leídas; A2)"
  - "Pedix: https://info.pedix.app/ (sección de precios de Argentina, leída; A2)"
  - "Tiendanube, canal WhatsApp: https://tiendanube.com/canales/whatsapp (leída) y planes: https://www.tiendanube.com/planes-y-precios?c=AR"
  - "Mercado Pago, link de pago (costos): https://www.mercadopago.com.ar/herramientas-para-vender/link-de-pago (leída; A2)"
  - "Tiendanube, ayuda, Ualá Bis (leída; C3)"
  - "Comercio-electronico/.investigacion/conversacional-proveedores-y-precios.md"
creado: 2026-11-22
revisado:
---

# Proveedores de comercio conversacional en Argentina

Quién le vende herramientas al comercio argentino que vende por chat, con su precio de lista al 2026-11-22: los proveedores de la API de WhatsApp, las bandejas, bots y CRM, los catálogos que mandan el pedido al chat, las apps de WhatsApp de las plataformas de tiendas y los links de pago.

Implementa las piezas de [comercio conversacional](comercio-conversacional.md); qué es cada tipo de intermediario está en [WhatsApp Business y su API](whatsapp-business-y-su-api.md).

Copiado de la página de precios de cada proveedor el 2026-11-22; las URL están en `fuentes` y en el informe [`conversacional-proveedores-y-precios.md`](../../.investigacion/conversacional-proveedores-y-precios.md). Ninguna bandeja, bot ni proveedor de la API independiente publica precio en pesos en su web (Zenvia remite a una lista en pesos que no se abrió); sí lo hacen las apps y la IA por chat de las plataformas de tiendas.

## Proveedores de la API

| Proveedor | Cuota | Por mensaje, además de Meta | Recargo sobre Meta |
|---|---|---|---|
| Meta, Cloud API directa | no tiene | — | — (factura en pesos desde el 1/4/2026) |
| Twilio (EE. UU.) | no tiene | USD 0,005, enviado o recibido | dice pasar Meta al costo |
| Gupshup | no tiene | USD 0,001 | «at actuals» |
| 360dialog (Alemania) | €49 por número (USD 59 según su documentación); €99 con bandeja | — | +7% en marketing por el canal estándar |
| Infobip | la página dio 403 | — | — |

## Bandejas, bots y CRM

Precio de entrada por mes, sin la tarifa de Meta, que ninguno incluye.

| Herramienta | Entrada | Qué incluye | Recargo sobre Meta |
|---|---|---|---|
| Wati | USD 45 anual según su página; un tercero midió 59 anual y 69 mensual | 3 usuarios, 500 contactos activos | ≈1,2 a 1,8 veces, medido por un tercero; Wati no lo declara |
| Whaticket | USD 49, mínimo 3 usuarios | 1 conexión por QR, API o coexistencia | Meta aparte |
| SleekFlow | USD 49 anual | 3 usuarios, 500 contactos | «según la tarifa de SleekFlow» |
| Waspy (bandeja y carritos para Tiendanube) | USD 70 | 2 agentes, 1.000 conversaciones iniciadas | dice que no recarga |
| Respond.io | USD 79 anual / 99 mensual | 5 usuarios, 1.000 contactos activos | no dice |
| B2Chat | USD 84 | 2 usuarios, 1.000 contactos | no dice |
| Leadsales (México) | USD 106,40 anual / 133 mensual (Profesional; el Básico no trae WhatsApp) | 4 usuarios, 20.000 contactos, USD 10 de saldo de Meta | descuenta de saldo; no dice |
| Cliengo | USD 119 (Premium, por coexistencia); USD 259 (Business, con una línea de API) | 3 o 5 operadores; 2.000 o 4.000 conversaciones con IA | no dice |
| Botmaker | USD 149 + alta de USD 99 | 3.000 conversaciones, 10 agentes | +20% en notificaciones |
| Kommo | USD 25 por usuario, mínimo 6 meses | 1 número | no dice |
| Callbell | €14 por agente | — | no dice |
| ManyChat (Instagram, Messenger, WhatsApp) | gratis hasta 25 contactos; Pro USD 29 anual / 39 mensual | 500 contactos activos según un tercero, 2.500 según otro | no dice |
| Chatfuel | USD 18 anual | unos 330 chats | +10% en plantillas |
| Treble | sin precio publicado | — | — |

## Catálogos y apps de las plataformas de tiendas

| Producto | Qué hace | Precio por mes | Comisión por venta |
|---|---|---|---|
| Pedix (Argentina) | catálogo web que manda el pedido armado por WhatsApp | $ 19.000, $ 25.500 o $ 35.000; 14 días gratis | no |
| Kyte (Brasil) | punto de venta con catálogo y pedidos | plan gratis; pagos de USD 9,99 a 19,99 en una página suya y de 19,99 a 39,99 en otra | no dice |
| Take App | tienda para WhatsApp | plan gratis; Business de unos USD 37,50 a 50, según el buscador | «no commissions» |
| Continuar por WhatsApp (app de Tiendanube) | botón que manda el carrito armado al chat | $ 10.593,62 | no |
| Wames (app de Tiendanube) | carritos abandonados por WhatsApp, bandeja e IA | gratis con 9% de lo recuperado; USD 29 + 7%; USD 79 + 5% | sobre lo recuperado |
| Chat Nube (Tiendanube) | IA que atiende por WhatsApp e Instagram con la API oficial | por mensaje, de $ 69 a $ 149 según el plan (ver [Tiendanube](../../Plataforma-de-tiendas/tiendanube.md)), más un adicional de $ 45 por mensaje en WhatsApp, según la página del producto; no queda claro si ese adicional es el cobro de Meta | no |
| App oficial de WhatsApp en Shopify | conecta la tienda con la API | gratis; Meta cobra aparte en dólares | no |

## Cobrar por chat

En Argentina ningún medio cobra dentro de WhatsApp ni de Instagram: se manda un link de pago o se pide una transferencia. Meta tiene pagos dentro de WhatsApp en Brasil, India y Singapur, y en México desde el 12/5/2026 según un proveedor.

| Medio | Comisión | Fuente |
|---|---|---|
| Link de pago de Mercado Pago | 6,29% al instante; 4,39% a 10 días; 3,39% a 18 días; 1,49% a 35 días. En cuotas, por ejemplo 3 cuotas 10,49% y 12 cuotas 32,29%. La página no dice si incluye IVA | página oficial (A2) |
| Link de Ualá Bis | 4,9% + IVA al instante (ayuda de una plataforma de tiendas); 4,4% según la prensa de julio de 2026 | C3 |
| Naranja X, MODO | no publican tarifa de link; en MODO la pone el procesador | — |

> [!NOTE] Sin fuente todavía: precios de Infobip, Treble y Tiendup; país de origen verificado de varias bandejas; si a las cuotas en dólares se les suman IVA o percepciones; Wabi, Hilos y los menús digitales para gastronomía.
