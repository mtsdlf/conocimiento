---
resumen: >-
  WhatsApp le da a un comercio dos productos: la app WhatsApp Business, gratis para atender a mano desde un teléfono, y la API (WhatsApp Business Platform), que permite bots, varios agentes y envíos automáticos y se cobra por mensaje entregado según su categoría y el país del destinatario. Casi siempre la API se usa a través de un intermediario que suma su propia cuota.
estado: borrador
estabilidad: semi
fuentes:
  - "Meta, precios de WhatsApp Business Platform: https://developers.facebook.com/docs/whatsapp/pricing (leída; consultada el 2026-11-22; A1)"
  - "WhatsApp, ayuda, difusiones comerciales y sus precios: https://faq.whatsapp.com/1711086883148106/ y https://faq.whatsapp.com/1356785542323967/ (por extracto; A)"
  - "Meta, anuncio del 3/4/2025 sobre difusiones pagas y límites de marketing por usuario, about.fb.com (por extracto; A1)"
  - "Meta, Introducing Meta One, 15/9/2026: https://about.fb.com/news/2026/09/introducing-meta-one-subscription-service-more-features-ai/ (por extracto; A2)"
  - "Cliengo, precios: https://www.cliengo.com/pricing (leída; coexistencia)"
  - "360dialog, documentación de precios: https://docs.360dialog.com/docs/get-started/pricing.md (leída)"
  - "Comercio-electronico/.investigacion/conversacional-meta-precios-y-terminos.md"
  - "Comercio-electronico/.investigacion/conversacional-proveedores-y-precios.md"
aliases: [WhatsApp Business, WhatsApp Business API, WhatsApp Business Platform, Cloud API, BSP, Business Solution Provider, ventana de 24 horas, plantilla de WhatsApp, difusión comercial]
creado: 2026-11-22
revisado:
---

# WhatsApp Business y su API

WhatsApp le da a un comercio dos productos: la app WhatsApp Business, gratis para atender a mano desde un teléfono, y la API (WhatsApp Business Platform), que permite bots, varios agentes y envíos automáticos y se cobra por mensaje entregado según su categoría y el país del destinatario. Casi siempre la API se usa a través de un intermediario que suma su propia cuota.

Es la pieza central del [comercio conversacional](comercio-conversacional.md). Los valores de Argentina están en [precios de WhatsApp en Argentina](precios-de-whatsapp-en-argentina.md) y los intermediarios, en [proveedores de comercio conversacional en Argentina](proveedores-de-comercio-conversacional-en-argentina.md).

## La app gratis y sus límites

La app WhatsApp Business agrega a WhatsApp un perfil de empresa, un catálogo, etiquetas, respuestas rápidas y mensajes automáticos de bienvenida y ausencia. Responder es gratis. Sus límites aparecen cuando el comercio crece:

- **Un número, pocos dispositivos.** Un teléfono principal y hasta cuatro vinculados, según el blog de WhatsApp y la prensa; no hay bandeja con asignación de chats entre agentes.
- **Las difusiones comerciales se pagan.** Desde el anuncio de Meta del 3/4/2025, los envíos masivos de marketing desde la app se cobran por mensaje entregado, «solo en ciertos países», cuya lista no es pública. Reseñas argentinas de 2026 hablan de comprar «créditos» para difusiones, lo que indica que ya corre en Argentina; Meta no lo confirma por país.
- **Meta One.** Desde el 15/9/2026 Meta vende la suscripción Meta One: el plan Essential para empresas, con insignia de verificada, cuesta desde USD 14,99 por mes y el Advanced (USD 49,99) suma más dispositivos vinculados y créditos de difusión. El anuncio no dice si reemplaza a Meta Verified, y el precio en pesos no está publicado.
- **El bloqueo.** La app restringe números por señales de spam; en 2026 aparecen bloqueos por escribir a un número no agendado o mandar muchas fotos (ver [quejas](quejas-de-los-comercios-que-venden-por-chat.md#bloqueos-del-número)).

## Cómo cobra la API

Desde el 1/7/2025, Meta cobra la API por mensaje entregado, y no cobra los mensajes que el cliente le manda al comercio. Antes cobraba por conversación de 24 horas. El precio depende de dos cosas:

1. **La categoría del mensaje.** Marketing (promociones), utilidad (avisos de un pedido), autenticación (códigos) y servicio (respuestas libres). Las tres primeras son plantillas aprobadas que se pueden mandar en cualquier momento; el servicio solo se puede mandar dentro de la ventana de atención. Desde el 1/7/2026 se cobra una quinta, el agente de IA de Meta, por tokens; el agente ya se usaba antes de junio de 2026.
2. **El país del destinatario.** Cada país o región tiene su tarifa; Argentina tiene tarifa propia y, desde el 1/4/2026, se puede facturar en pesos.

**La ventana de atención** dura 24 horas desde el último mensaje del cliente y se renueva con cada mensaje suyo. Fuera de ella el comercio solo puede escribir con plantillas pagas. Si el cliente llega desde un anuncio «clic a WhatsApp» en la app del teléfono y el comercio responde dentro de las 24 horas, se abre una ventana gratuita en la que todo es gratis, salvo el agente de IA de Meta, «hasta 7 días» (antes eran 72 horas; la fecha del cambio no se encontró).

**Lo gratis cambió tres veces en dos años.** Meta dejó de cobrar el servicio el 1/11/2024 y la utilidad dentro de la ventana el 1/7/2025, y volvió a cobrar los dos el 1/10/2026, con un cupo de 1.000 mensajes de servicio gratis por mes por número de teléfono que no se acumula. Los descuentos por volumen existen solo para utilidad y autenticación, desde el mensaje 100.001 del mes. Meta cambia precios solo el 1/1, 1/4, 1/7 o 1/10, con un mes de aviso para una tarifa y seis para un cambio de modelo.

## Los intermediarios

La API de Meta (Cloud API) no trae pantalla: es una interfaz para programas. Para atender con ella un comercio necesita software encima, y lo compra a uno de dos tipos de intermediario:

| Tipo | Qué pone | Cómo cobra |
|---|---|---|
| Proveedor de la API (BSP, Business Solution Provider) | el alta del número, la facturación de Meta y a veces una bandeja simple | cuota por número o cargo por mensaje, más la tarifa de Meta al costo o con recargo |
| Bandeja, bot o CRM | la pantalla compartida para varios agentes, el bot, la IA, el catálogo, la conexión con la tienda | abono mensual por usuarios y contactos, más la tarifa de Meta, a veces con recargo |

Pocos declaran el recargo sobre Meta: en los precios leídos el 2026-11-22, uno suma 20% en notificaciones, otro 10% en plantillas y un BSP 7% en marketing; de otro, un tercero midió tarifas entre 1,2 y 1,8 veces las de Meta. Los demás no lo dicen. Las unidades tampoco coinciden: unos cuentan contactos activos, otros conversaciones de 24 horas y Meta, mensajes entregados.

Algunos proveedores ofrecen **coexistencia**: el mismo número sigue en la app del teléfono y además se conecta a la API, y los mensajes que pasan por la API los factura Meta. Un proveedor la vende como la forma barata de sumar una bandeja sin dejar la app.

## Cómo se decide el salto de la app a la API

La app alcanza mientras atiende una sola persona y los envíos masivos son pocos. El salto lo empujan tres cosas: varias personas atendiendo el mismo número, querer un bot o una IA que responda fuera de horario, y avisos automáticos del pedido. El costo del salto es la cuota del intermediario más los mensajes de Meta, que desde el 1/10/2026 incluyen las respuestas por encima de 1.000 al mes. La API también trae reglas propias: las plantillas se aprueban, hay límites de envío por portafolio y desde el 15/1/2026 no se puede usar para un asistente de IA de propósito general, del tipo de ChatGPT; los bots de atención de un comercio siguen permitidos ([dependencia de Meta](dependencia-de-meta.md)).

> [!NOTE] Sin fuente todavía: cuántas cuentas de la app y de la API hay en Argentina, y cuántos comercios dieron el salto.

Recurso canónico: la página de precios de Meta (developers.facebook.com/docs/whatsapp/pricing), entera, con las tablas por país enlazadas al pie; fijarse en la sección de mensajes gratis y en el calendario de cambios.
