---
resumen: >-
  Las tarifas de Meta por mensaje de la API de WhatsApp para destinatarios argentinos, en pesos y en dólares, vigentes desde el 1/10/2026, y el costo mensual con precios de lista de un comercio que atiende 500 o 3.000 conversaciones por mes, con la app gratis, con la API directa y con un intermediario.
estado: borrador
estabilidad: volatil
fuentes:
  - "Meta, precios de WhatsApp Business Platform y tablas «Cost per message in ARS / USD on the WhatsApp Business Platform, effective October 1, 2026»: https://developers.facebook.com/docs/whatsapp/pricing (PDF leídos enteros; consultada el 2026-11-22; A1)"
  - "Cliengo, guía de precios de WhatsApp Business: https://guiawabusiness.cliengo.com/precios (leída; confirma las tarifas; B3)"
  - "360dialog: https://360dialog.com/pricing y https://docs.360dialog.com/docs/get-started/pricing.md (leídas; A2)"
  - "Twilio, WhatsApp pricing: https://www.twilio.com/en-us/whatsapp/pricing (leída; A2)"
  - "Wati, pricing: https://www.wati.io/pricing/ (leída; A3) y eesel, Wati pricing, revisado el 26/10/2026: https://www.eesel.ai/blog/wati-pricing (leída; C3)"
  - "Cliengo, pricing: https://www.cliengo.com/pricing (leída; A2)"
  - "Leadsales, precios: https://www.leadsales.io/precios (leída; A2)"
  - "Botmaker, precios: https://botmaker.com/es/precios/ (leída; A2)"
  - "Comercio-electronico/.investigacion/conversacional-meta-precios-y-terminos.md"
  - "Comercio-electronico/.investigacion/conversacional-proveedores-y-precios.md"
creado: 2026-11-22
revisado:
---

# Precios de WhatsApp en Argentina

Las tarifas de Meta por mensaje de la API de WhatsApp para destinatarios argentinos, en pesos y en dólares, vigentes desde el 1/10/2026, y el costo mensual con precios de lista de un comercio que atiende 500 o 3.000 conversaciones por mes, con la app gratis, con la API directa y con un intermediario.

Cómo cobra la API está en [WhatsApp Business y su API](whatsapp-business-y-su-api.md).

Copiado de las tablas oficiales de Meta (https://developers.facebook.com/docs/whatsapp/pricing) el 2026-11-22. Meta solo cambia tarifas el 1/1, 1/4, 1/7 o 1/10: esta ficha vence con la próxima de esas fechas.

## Tarifa por mensaje entregado a un número argentino (+54)

| Categoría | Pesos | Dólares |
|---|---|---|
| Marketing | 89,5620 | 0,0618 |
| Utilidad | 37,6798 | 0,0260 |
| Autenticación | 37,6798 | 0,0260 |
| Servicio, después de los 1.000 gratis por número y por mes | 37,6798 | 0,0260 |
| Agente de IA de Meta | USD 2 por millón de tokens | ídem |

Para Argentina la tarifa no cambia desde el 1/10/2025, cuando bajaron utilidad y autenticación; la fecha 1/10/2026 es la de la tabla. Las dos tablas implican 1.449,2 pesos por dólar. Utilidad y autenticación bajan entre 5% y 25% por volumen, desde el mensaje 100.001 (utilidad) o 120.001 (autenticación) del mes; marketing y servicio no tienen descuento. Para comparar, en dólares: Brasil cobra 0,0625 el marketing y 0,0068 la utilidad; México, 0,0397 y 0,0085; Chile, 0,0889 y 0,0200. Argentina tiene la utilidad más cara de América Latina entre los países con tarifa propia, después de Perú.

Lo gratis: los mensajes del cliente; lo que se manda dentro de la ventana de un anuncio «clic a WhatsApp» (hasta 7 días, si el cliente entró desde la app del teléfono y se le respondió dentro de las 24 horas, salvo el agente de IA de Meta), y los primeros 1.000 mensajes de servicio del mes de cada número. Hasta el 30/9/2026 todo el servicio era gratis; los avisos de utilidad dentro de la ventana de 24 horas se cobran desde el primero.

Otras fuentes dan valores distintos (un proveedor publicaba 0,07107 para marketing); manda la tabla de Meta. La factura en pesos no muestra IVA ni percepciones en la tabla: no se encontró cómo se tratan.

## Cuánto le cuesta por mes a un comercio tipo

Cuenta propia con precios de lista del 2026-11-22. Supuestos, ninguno medido:

- El 80% de las conversaciones las empieza el cliente; el 20%, el comercio con una plantilla de marketing.
- El comercio manda 4 mensajes por conversación (se prueba con 2 y con 6); en las que empieza él, uno es la plantilla y el resto son servicio.
- Un solo número, sin anuncios «clic a WhatsApp» (con anuncios, parte de esos mensajes sería gratis).
- La cuota en euros, al valor en dólares que da el propio proveedor (€49 = USD 59).

**Lo que se le paga a Meta**, por mes:

| Conversaciones por mes | 2 mensajes por conversación | 4 mensajes | 6 mensajes |
|---|---|---|---|
| 500 | USD 6 ($ 9.000) | USD 30 ($ 43.000) | USD 56 ($ 81.000) |
| 3.000 | USD 152 ($ 220.000) | USD 308 ($ 446.000) | USD 464 ($ 672.000) |

Con 4 mensajes por conversación y las reglas anteriores al 1/10/2026 (servicio gratis), la cuenta de Meta habría sido solo el marketing: USD 6 y USD 37. El cambio multiplicó el costo de Meta entre 4,8 y 8,3 veces en este escenario.

**Con la herramienta**, 4 mensajes por conversación, USD por mes:

| Opción | 500 conversaciones | 3.000 conversaciones | Qué se tomó |
|---|---|---|---|
| App WhatsApp Business | 0 | 0, si una persona da abasto | las difusiones de marketing se pagan aparte; su precio en pesos no se encontró |
| API directa de Meta | 30 | 308 | sin cuota, pero sin pantalla: hace falta software propio |
| 360dialog (proveedor de la API) | 89 | 370 | €49 por número (USD 59 según su documentación) + 7% sobre marketing |
| Twilio (proveedor de la API) | 50 | 428 | USD 0,005 por mensaje enviado o recibido; se supone que el cliente manda tantos como el comercio |
| Wati (bandeja) | 83 | 623 y más | Growth USD 45 (500 contactos activos); Business USD 239 (2.500 contactos) para 3.000; tarifas ≈1,2 veces Meta en servicio y 1,6 en marketing, medidas por un tercero sobre EE. UU. |
| Leadsales (CRM) | 153 | 431 | Profesional USD 133 mensual, con USD 10 de saldo de Meta incluido |
| Botmaker (bot y bandeja) | 180 | 464 | Standard USD 149 (3.000 conversaciones) + 20% sobre marketing; alta de USD 99 una vez |
| Cliengo (bot y bandeja) | 149 | 567 | Premium USD 119 por coexistencia (2.000 conversaciones) para 500; Business USD 259, con una línea de API, para 3.000; no dice si recarga a Meta |

Lectura: con 500 conversaciones la cuota del intermediario pesa más que Meta; con 3.000, Meta ya es la mitad o más de la cuenta. Ninguna bandeja independiente publica precio en pesos en su web; Meta sí factura en pesos. Los precios de las herramientas están en [proveedores de comercio conversacional en Argentina](proveedores-de-comercio-conversacional-en-argentina.md).

> [!NOTE] Sin fuente todavía: cuántos mensajes manda de verdad un comercio por conversación, qué parte de sus conversaciones llega por anuncios y el precio en pesos de las difusiones de la app.
