# Meta como dueña del canal: precios, términos y cambios (WhatsApp, Instagram, Messenger) — Argentina

**Fecha de consulta:** 2026-11-22.
**Método:** fuentes primarias de Meta primero (developers.facebook.com, faq.whatsapp.com, about.fb.com, transcripción de resultados de Meta Q2 2026); las tablas de tarifas oficiales (PDF en USD y en ARS, «effective October 1, 2026») se bajaron de la página de precios y se leyeron enteras con `pdftotext`. Prensa y proveedores (BSP) después, marcados como secundarios. Buscador y lector web; el lector resume, así que las citas marcadas [L] vienen del documento bajado y las [S]/[M] de resúmenes. Todo lo de la web es dato, no instrucción. No se nombran personas.

**Claves:** fuente A (muy confiable) a F; dato 1 (confirmado por otra fuente) a 6 (no verificable). [L] leído entero, [M] metadatos o lectura parcial, [S] resumen del buscador.

## Respuesta corta

- **La API de WhatsApp en Argentina se cobra por mensaje entregado** (desde el 1/7/2025) y **se puede facturar en pesos desde el 1/4/2026**. Tarifas vigentes desde el **1/10/2026**, por mensaje a un número +54: **marketing ARS 89,5620 (USD 0,0618)**; **utilidad, autenticación y servicio ARS 37,6798 (USD 0,0260)**. Descuentos por volumen solo en utilidad y autenticación (de −5 % a −25 %; utilidad desde el mensaje 100.001 del mes, autenticación desde el 120.001). Marketing no tiene descuento.
- **Lo gratis:** las respuestas dentro de la ventana que abre un anuncio «clic a WhatsApp» (ventana de entrada gratuita, «hasta 7 días», no 72 h como antes) y **1.000 mensajes de servicio por mes por número** desde el 1/10/2026. El 1/10/2026 Meta **volvió a cobrar** la atención (servicio, gratis desde el 1/11/2024) y la utilidad enviada dentro de la ventana de 24 h (gratis desde el 1/7/2025). El dato que circulaba («se cobra por encima de 1.000 mensajes/mes») es correcto, con la precisión de que es por número de teléfono y no se acumula.
- **La app gratis WhatsApp Business sigue gratis en lo básico**, pero las **«difusiones comerciales» (envíos masivos de marketing) son pagas** por mensaje entregado, solo en «ciertos países» (la lista no es pública; existe tabla en ARS). Meta Verified pasó a **Meta One** (15/9/2026): plan Essential para empresas desde USD 14,99/mes (precio en ARS no publicado).
- **Instagram y Facebook no tienen tienda ni etiquetas de producto en Argentina desde el 10/8/2023**; el pago dentro de la app (checkout) nunca llegó a Argentina y Meta lo apagó en EE. UU. entre junio y agosto de 2025.
- **No hay pago dentro de WhatsApp en Argentina**: los pagos nativos existen en Brasil, India y Singapur (y México vía «Global Payments API», según un BSP). El camino local es el link de pago (Mercado Pago u otro).
- **La dependencia es real y fechada:** en 18 meses Meta cambió el modelo de cobro (7/2025), apagó la API On-Premises (23/10/2025), pasó los límites de envío al portafolio (7/10/2025), prohibió los asistentes de IA de propósito general (15/1/2026, salvo donde un regulador la obligó), volvió a cobrar la atención (1/10/2026) y lanzó su propio agente de IA pago que compite con los terceros (1/7/2026). Hubo bloqueos masivos de cuentas (3/8/2026) que Meta reconoció como error.

## 1. Precios de la API de WhatsApp (WhatsApp Business Platform) para Argentina

### Cómo cobra Meta
- «Effective July 1, 2025 – Meta charges on a **per-message basis** … Meta does **not** charge for messages from users to businesses.» «Businesses are only charged when a message is _delivered_.» [L, pricing.md] (A1)
- Cinco categorías: marketing, utilidad, autenticación (plantillas, se pueden mandar en cualquier momento) y servicio y «Meta Business Agent» (no plantillas, solo dentro de la ventana de 24 h). Meta Business Agent existe desde el 1/7/2026. [L] (A1)
- Ventana de atención (CSW): «a 24-hour timer called a _customer service window_ starts … If the user messages or calls you again before the timer expires, the timer resets to 24 hours.» Fuera de la ventana solo se pueden mandar plantillas. [L] (A1)
- Calendario de precios (publicado en septiembre de 2025): Meta solo cambia precios el 1/1, 1/4, 1/7 o 1/10, con aviso mínimo de 1 mes (cambio de tarifa), 3 meses (agregado al modelo) o 6 meses (cambio de modelo). [L] (A1)

### Tarifas vigentes para un destinatario argentino (+54), desde el 1/10/2026

| Categoría | ARS por mensaje (tabla ARS) | USD por mensaje (tabla USD) |
|---|---|---|
| Marketing | 89,5620 | 0,0618 |
| Utilidad | 37,6798 | 0,0260 |
| Autenticación | 37,6798 | 0,0260 |
| Autenticación internacional | n/a | n/a |
| Servicio (después de los 1.000 gratis) | 37,6798 | 0,0260 |
| Meta Business Agent | USD 2,00 por millón de tokens (≈ 4–5 centavos de dólar por mensaje según Meta) | ídem |

Fuente: «Cost per message in ARS on the WhatsApp Business Platform, effective October 1, 2026» y su par en USD [L, PDF oficiales enlazados desde la página de precios] (A1: las dos tablas son consistentes entre sí; el cociente implícito es 1.449,2 ARS por USD en ambas categorías). Para comparar: Brasil marketing USD 0,0625 y utilidad 0,0068; México 0,0397 y 0,0085; Chile 0,0889 y 0,0200; Colombia 0,0125 y 0,0008; Resto de América Latina 0,0740 y 0,0113. **Argentina tiene la utilidad más cara de la región** entre los mercados con tarifa propia (solo detrás de Perú, ARS 43,4768). [L]

**Escalones por volumen (tabla ARS, Argentina):**

| Utilidad: mensajes/mes | Tarifa ARS | vs. lista | Autenticación: mensajes/mes | Tarifa ARS |
|---|---|---|---|---|
| 0 – 100.000 | 37,6798 | 0 % | 0 – 120.000 | 37,6798 |
| 100.001 – 1.000.000 | 35,7958 | −5 % | 120.001 – 400.000 | 35,7958 |
| 1.000.001 – 4.500.000 | 33,9118 | −10 % | 400.001 – 1.000.000 | 33,9118 |
| 4.500.001 – 15.000.000 | 32,0278 | −15 % | 1.000.001 – 5.000.000 | 32,0278 |
| 15.000.001 – 30.000.000 | 30,1438 | −20 % | 5.000.001 – 10.000.000 | 30,1438 |
| 30.000.001 en adelante | 28,2599 | −25 % | 10.000.001 en adelante | 28,2599 |

Los escalones se suman a nivel portafolio de negocio, se reinician cada mes y no cuentan los mensajes gratis de la ventana de anuncios. Servicio: «Service message rates will match utility and authentication rates, with no volume tiers» [M, página de cambios]. (A1)

**Discrepancias secundarias:** Sleekflow publica Argentina marketing USD 0,07107 y Chattigo ≈ USD 0,0265 (probablemente utilidad o con recargo del proveedor) [S] (C5). La tabla de Meta manda.

### Facturación en pesos
- Tabla de monedas de la página de precios: «ARS | April 1, 2026 | ARS list rates | ARS volume tiers | ARS rates and volume tiers». «Currency selection is part of the Messaging account creation process; once selected, a currency cannot be changed.» Hay una «Currency Migration API» (disponible desde el 1/6/2026). [L] (A1, confirmado por Chattigo y Cliengo [S])
- Ocho monedas nuevas el 1/4/2026: AED, ARS, CLP, COP, MYR, PEN, SAR, SGD. A diferencia de Brasil e India, **para Argentina no se publicó obligación de migrar** a ARS ni entidad local que facture (Brasil factura Facebook Brasil y obliga a migrar antes del 30/6/2027; India antes del 31/12/2026). [L] (A1)
- Hueco: IVA y percepciones (impuesto PAIS ya no rige; RG de servicios digitales) sobre la factura en pesos no encontrados.

### Lo gratis
- «There are two instances where Meta does _not_ charge»: (1) la ventana de entrada gratuita y (2) «For each business phone number, Meta provides 1,000 free service messages per month, which do not roll over but reset monthly. Thus, Meta only charges as of the 1,001st service message for each business phone number.» [L] (A1)
- Ventana de entrada gratuita (FEP): se abre si el usuario escribe desde un anuncio «clic a WhatsApp» (solo apps Android/iOS) y la empresa responde dentro de las 24 h; «The FEP window may remain open for up to 7 days»; dentro, marketing, utilidad, autenticación y servicio son gratis; Meta Business Agent se cobra igual. [L] (A1). **Discrepancia con el dato que circulaba:** la ventana histórica era de 72 h; la página actual dice «hasta 7 días». No encontré la fecha del cambio (hueco).
- Sin medio de pago cargado al 30/9/2026, Meta entrega los 1.000 gratis y después **deja de entregar** los mensajes de servicio. [L] (A1)
- Gobierno y ONG elegibles: servicio gratis sin tope hasta el 31/12/2027. [L] (A1)
- **Discrepancia interna de Meta:** la página «Upcoming pricing updates… non-template messages» (anunciada con la guía del 1/7/2026) no menciona el cupo de 1.000 gratis; la página principal de precios sí. Lectura probable: el cupo se agregó después del primer anuncio. [M] (A2)

### Qué cambió el 1/10/2026 (literal)
«Meta resumed charging, on a per-message basis, for messages that were previously free: Service messages, which became free as of Nov. 1, 2024 … Utility messages sent in response to users (thus in an open customer service window), which became free as of July 1, 2025.» Razón dada por Meta: «ensure pricing reflects the value these messages deliver to businesses». [L/M] (A1)

### Historia del modelo de cobro
| Fecha | Cambio | Fuente |
|---|---|---|
| Hasta 30/6/2025 | Cobro por conversación de 24 h (marketing, utilidad, autenticación, servicio) | pricing.md, sección conversation-based [L] A1 |
| 1/8/2024 | Baja de tarifas de conversación de utilidad | pricing.md [L] A1 |
| 1/11/2024 | Conversaciones de servicio gratis para todos | pricing.md [L] A1 |
| 1/4/2025 | Meta deja de entregar plantillas de marketing a números de EE. UU. (+1); sigue vigente: «WhatsApp does not currently deliver marketing template messages to WhatsApp users with United States phone numbers» | per-user-limits [M] A1 (la fecha 1/4/2025 viene de 360dialog [S] C2) |
| 1/7/2025 | Cobro por mensaje entregado; utilidad dentro de la ventana de 24 h gratis; escalones por volumen para utilidad y autenticación; baja de utilidad y autenticación en varios mercados | pricing.md [L] A1 |
| 1/10/2025 | Argentina: baja de utilidad y autenticación («Lower») | pricing.md [L] A1 |
| 1/1/2026 | MXN; cambios en Egipto, Francia, India, Norteamérica | [L] A1 |
| 1/4/2026 | ARS y otras 7 monedas | [L] A1 |
| 1/7/2026 | Categoría Meta Business Agent (USD 2/millón de tokens) | [L] A1 |
| 1/10/2026 | Vuelve el cobro de servicio (1.000 gratis por número) y de utilidad en ventana | [L] A1 |

Hueco: la tarifa argentina en USD antes del 1/10/2025 (utilidad) no quedó verificada en fuente primaria.

## 2. La app gratis WhatsApp Business

- **Lo básico sigue gratis.** Meta, al lanzar Meta One: «The core experience across our apps and Meta AI has always been free, and that's not changing.» [M, about.fb.com 15/9/2026] (A2)
- **Difusiones comerciales pagas.** Meta, 3/4/2025: las «business broadcasts» «will now be a paid feature to ensure businesses are thoughtful about what they send»; y «introduced limits to the number of marketing messages that people can receive». [M, about.fb.com] (A1, confirmado por TechCrunch 18/3/2025, que habló de «250 customized messages for free» en la prueba [M] B).
- Ayuda de WhatsApp (vigente): «Puedes enviar difusiones comerciales por un cargo.» «Luego de que hayas usado los mensajes gratuitos, tendrás que añadir un método de pago.» «Solo pagas por cada mensaje que se entrega a un contacto dentro de los cinco días posteriores al envío.» «Los precios … se basan en el código de país de cada destinatario.» «Actualmente, las difusiones comerciales solo están disponibles en ciertos países.» Hay tablas en 16 monedas, **ARS incluida**; Argentina no está nombrada y no hay lista de países. [M, faq.whatsapp.com 1711086883148106 y 1356785542323967] (A1 en el mecanismo; A6 en si ya está activo en Argentina).
- Cupo y límites reportados por terceros (no confirmados por Meta para cada mercado): prueba de 6 meses con 250 mensajes gratis/mes, hasta 500 destinatarios por envío, 1.000 en 30 días; la lista de difusión vieja (gratis) llegaba a 256 contactos guardados. [M, ChakraHQ 17/11/2026] (C4)
- **Meta Verified → Meta One (15/9/2026).** Planes para empresas y creadores: Essential USD 14,99/mes, Advanced 49,99, Expert 149, Max 499. Essential incluye en WhatsApp Business «Meta Business Agent», insignia verificada, canal verificado y protección contra suplantación (sujeto a verificación); Advanced suma «more linked devices and business broadcast credits». Disponibilidad «rolling out gradually», varía por región. **Precio en ARS no publicado.** [M, about.fb.com] (A2; precios confirmados por TechCrunch/The Next Web [S]). Antecedente: en 2023 Meta Verified (Facebook/Instagram) llegó a Argentina a USD 7,99 web / 9,99 móvil [S, La Nación 27/6/2023] (B2).
- **Dispositivos vinculados:** el estándar es 1 teléfono principal + hasta 4 dispositivos vinculados (blog de WhatsApp y prensa) [S] (B3); el plan Advanced de Meta One promete «más». Hueco: número exacto en 2026 para Business.
- Catálogo, etiquetas, mensajes automáticos y anuncios desde la app: no se verificaron cambios de precio en 2026 (hueco; se asume gratis salvo los anuncios, que se pagan como cualquier anuncio de Meta).

## 3. Instagram y Facebook

- **Tiendas (Shops) y etiquetas de producto apagadas en Argentina desde el 10/8/2023.** «Por decisión de Meta, Facebook e Instagram Shopping no están disponibles en Argentina, Colombia y Chile desde el 10 de agosto de 2023.» Se perdió el etiquetado de productos en publicaciones, reels e historias, la pestaña de tienda y las audiencias de visitantes; México quedó afuera del corte. [M, ayuda.tiendanube.com, dos páginas] (B2: es Tiendanube relatando una decisión de Meta; no encontré el aviso de Meta).
- **Checkout dentro de Instagram/Facebook:** nunca estuvo en Argentina. En 2023 Meta planeaba forzar el checkout propio (TechCrunch 27/4/2023); en 2025 lo revirtió: «Starting in June 2025, Shops will gradually begin using website checkout instead of checkout on Facebook or Instagram», con fin del procesamiento de pedidos de Meta hacia fines de agosto de 2025 (afectaba a tiendas de EE. UU.). [S, ppc.land, BigCommerce, Value Added Resource] (B2)
- **Instagram Basic Display API:** cerrada el 4/12/2024 («the API will no longer be available 90 days from now, starting December 4th, 2024»). [S, developers.facebook.com/blog 4/9/2024] (A1, con TechCrunch 6/12/2024)
- **Mensajería de Instagram y Messenger (API):** responder no se cobra; ventana estándar de 24 h («For most user actions, it lasts 24 hours»), que llega a 7 días tras un anuncio «clic a Messenger/Direct»; etiqueta «Human Agent» para responder a mano dentro de 7 días; algunas etiquetas son solo de Messenger. [M, Messenger Platform policy overview] (A1). La página de políticas no menciona tarifas.
- **Mensajes de marketing en Messenger:** pagos por mensaje entregado vía la cuenta publicitaria, fuera de la ventana de 24 h, uno cada 12 h por suscriptor; solo para proveedores con App Review aprobado. Las «Recurring Notifications» gratis se apagan desde enero de 2026 (ManyChat dice 12/1/2026, SaleSmartly 7/1/2026: discrepan). [S] (A2 el producto, C4 las fechas)
- **Agente de Meta en Instagram:** «We're rolling business agents out on Instagram now too» (Meta, resultados Q2 2026, 29/7/2026) [L] (A1).
- Herramientas de automatización de DMs permitidas: las que usan la API oficial (Instagram API con login de Facebook/Instagram) y pasan App Review; no se verificó una lista. Hueco.

## 4. Dependencia de un solo tercero: cambios de Meta que golpearon a quienes construyen encima

| Fecha | Cambio | A quién golpeó | Fuente |
|---|---|---|---|
| 10/8/2023 | Fin de Facebook e Instagram Shopping (tiendas y etiquetas) en Argentina, Chile y Colombia | Comercios y plataformas con integración de catálogo (Tiendanube perdió el canal en esos países) | ayuda.tiendanube.com [M] B2 |
| Enero 2024 (v2.53) | Todas las funciones nuevas solo en Cloud API | Quien corría On-Premises | developers.facebook.com sunset [S] A1 |
| 4/12/2024 | Cierre de Instagram Basic Display API | Widgets de feed, apps de terceros | developers.facebook.com/blog [S] A1 |
| 1/4/2025 | Pausa de plantillas de marketing a números de EE. UU. (sigue) | Marcas y BSP con clientes en EE. UU. | per-user-limits [M] A1; fecha 360dialog [S] C2 |
| 3/4/2025 | Difusiones de la app Business pasan a pagas; límites de marketing por usuario | Comercios que usaban la app gratis para promociones | about.fb.com [M] A1 |
| Jun–ago 2025 | Fin del checkout nativo en Shops (EE. UU.) | Tiendas y plataformas integradas | ppc.land / BigCommerce [S] B2 |
| 1/7/2025 | Cambio de cobro por conversación a cobro por mensaje (aviso de 6 meses) | Todo BSP: rehacer facturación y presupuestos | pricing.md [L] A1 |
| Sin fecha publicada | Límite de marketing por usuario (código de error 131049): «WhatsApp may limit the number of marketing template messages a WhatsApp user receives from any business» | Campañas masivas | per-user-limits [M] A1 |
| 7/10/2025 | Límites de envío pasan del número al portafolio de negocio | BSP que repartían números | messaging-limits / 8x8 [S] A2 |
| 15/10/2025 (nuevos) y 15/1/2026 (todos) | Prohibición de asistentes de IA de propósito general en la API («AI Providers»); OpenAI, Copilot y Perplexity salieron de WhatsApp | Startups de IA sobre WhatsApp | TechCrunch 18/10/2025 [S], respond.io [S] B1 |
| 23/10/2025 | Fin de la On-Premises API: no se puede registrar ni enviar | Quien no migró a Cloud API | developers.facebook.com sunset [S] A1 |
| 24/12/2025 – 3/2026 | Reguladores obligan a Meta a excluir Italia (AGCM, 24/12/2025) y Brasil (CADE, ene-2026); la Comisión Europea abre caso y emite pliego de cargos (feb-2026). Meta habilita a los «AI Providers» solo donde «is legally required» y **les cobra** cada mensaje de servicio (Italia desde 16/2/2026, Brasil y Europa desde 11/3/2026; Italia y Europa sin cobro desde 13/5/2026) | Argentina **no** está en la lista: la prohibición rige acá | developers…/pricing/ai-providers [M] A1; TechCrunch 13/1 y 15/1/2026 [S] B1 |
| 1/7/2026 | Meta lanza su propio agente de IA pago (Meta Business Agent) y lo compara en su documentación contra «3rd-party AI» (~9–10 ¢ vs ~4–5 ¢ por mensaje) | Proveedores de bots e IA conversacional: Meta compite con ellos en su propio canal | pricing.md [L] A1 |
| 3/8/2026 | Bloqueos masivos de cuentas (personales y Business); Meta: «A veces nos equivocamos» | Pymes que atienden por WhatsApp | La Nación 3/8/2026 [M] B2; iProfesional 3/8/2026 [S] (impacto en comercios) C3 |
| 15/9/2026 | Meta Verified absorbido por Meta One (suscripción con créditos de difusión y agente) | Quien pagaba Meta Verified | about.fb.com [M] A2 |
| 1/10/2026 | Vuelve el cobro de servicio y utilidad en ventana; sin medio de pago, se cortan los mensajes de servicio | BSP y comercios con mucha atención | pricing.md [L] A1 |

- **Apelaciones:** se piden desde el portafolio de negocio; resultado no garantizado [S, Wati/Klaviyo] (C3). Hubo fallos judiciales argentinos contra Meta por cuentas bloqueadas (iProUP) que no pude leer (hueco).
- **Casos de empresas que perdieron su negocio:** el más documentado es el de los asistentes de IA generalistas (OpenAI anunció que su contacto en WhatsApp dejaba de funcionar el 15/1/2026 [S, 9to5Mac]). No encontré un caso argentino con cifras.
- **Requisitos BSP / Tech Provider:** no verificados (hueco).

## 5. Pagos dentro de WhatsApp

- **Existen en Brasil** (Pix, boleto, links de pago, «One-Click Payments»; moneda BRL), **India** (UPI, pasarelas como Razorpay, PayU; solo INR) y **Singapur** (solo empresas y usuarios de Singapur). [S, developers.facebook.com payments-br / payments-in; 360dialog para Singapur] (A2)
- **México:** pago nativo vía «Global Payments API» desde el 12/5/2026 según Cliengo [M] (C5, sin fuente de Meta leída).
- **Argentina: no hay pago nativo.** Cliengo (guía actualizada 11/10/2026) lo marca como «planned / a confirmar» y recomienda «Catálogo + link Mercado Pago» [M] (C4). Meta anunció «in-chat checkout» en Conversations 2026 (junio de 2026, about.fb.com/news/2026/06/meta-business-agent/, no leído) sin que eso implique pago nativo por país.
- **Mercado Pago:** no hay integración oficial dentro del chat de WhatsApp; el camino oficial es el link de pago compartible por WhatsApp (mercadopago.com.ar/herramientas-para-vender/link-de-pago). Su asistente de IA (2026) vive en la app de Mercado Pago, no en WhatsApp. [S] (B3)

## 6. Cifras oficiales

- WhatsApp: «more than 3 billion monthly users» (Meta, Q1 2025) [S] (A2). «Over two billion people use WhatsApp every day» (about.fb.com, 3/4/2025) [M] (A1).
- Meta Business Agent: «more than 1 million businesses using them to talk to their customers or complete sales every week» (resultados Q2 2026, 29/7/2026) [L] (A1).
- Ingresos: «quarterly Family of Apps other revenue reached $1 billion and grew 73% year-over-year, driven primarily by WhatsApp paid messaging and subscriptions revenue» (Q2 2026) [L] (A1). La mensajería paga habría superado USD 2.000 millones anualizados a fines de 2025 [S] (C4).
- App WhatsApp Business: último dato oficial encontrado, más de 200 millones de usuarios activos mensuales (junio de 2023) [S] (B4). Sin cifra oficial 2026.
- Argentina: ~36 millones de usuarios y 90–93 % de penetración (nota regional sin fecha) [S] (D5); 74 % de los usuarios argentinos ya interactúa con empresas por WhatsApp (informe Infobip vía Mercado) [S] (C5). **Meta no publica cifras por país** (hueco).

## Tabla de fuentes

| # | Fuente | URL | Tipo | Lectura | Calif. |
|---|---|---|---|---|---|
| 1 | Pricing on the WhatsApp Business Platform (Markdown oficial) | https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing.md | Primaria | [L] | A |
| 2 | Tabla oficial ARS, efectiva 1/10/2026 (PDF enlazado desde #1) | enlace «ARS rates and volume tiers» en https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing | Primaria | [L] | A |
| 3 | Tabla oficial USD, efectiva 1/10/2026 (PDF enlazado desde #1) | enlace «USD rates and volume tiers», misma página | Primaria | [L] | A |
| 4 | Upcoming pricing updates (non-template messages) | https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages/ | Primaria | [M] | A |
| 5 | AI Providers pricing policy | https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers | Primaria | [M] | A |
| 6 | Per-user marketing limits | https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits/ | Primaria | [M] | A |
| 7 | Messaging limits | https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits | Primaria | [M] | A |
| 8 | On-Premises API sunset | https://developers.facebook.com/docs/whatsapp/on-premises/sunset | Primaria | [S] | A |
| 9 | Messenger Platform policy overview | https://developers.facebook.com/docs/messenger-platform/policy/policy-overview | Primaria | [M] | A |
| 10 | Marketing Messages on Messenger | https://developers.facebook.com/documentation/business-messaging/messenger-platform/marketing-messages-on-messenger | Primaria | [S] | A |
| 11 | Update on Instagram Basic Display API (4/9/2024) | https://developers.facebook.com/blog/post/2024/09/04/update-on-instagram-basic-display-api | Primaria | [S] | A |
| 12 | WhatsApp FAQ: Cómo crear y enviar una difusión comercial | https://faq.whatsapp.com/1711086883148106/?cms_platform=web | Primaria | [M] | A |
| 13 | WhatsApp FAQ: Precios de las difusiones comerciales | https://faq.whatsapp.com/1356785542323967/?cms_platform=web | Primaria | [M] | A |
| 14 | Meta: ways to manage your business chats (3/4/2025) | https://about.fb.com/news/2025/04/ways-to-manage-your-businesses-chats-on-whatsapp/ | Primaria | [M] | A |
| 15 | Meta: Introducing Meta One (15/9/2026) | https://about.fb.com/news/2026/09/introducing-meta-one-subscription-service-more-features-ai/ | Primaria | [M] | A |
| 16 | Meta Q2 2026 Earnings Call Transcript (29/7/2026) | https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf | Primaria | [L] | A |
| 17 | WhatsApp payments Brasil / India (docs) | https://developers.facebook.com/documentation/business-messaging/whatsapp/payments/payments-br/overview ; …/payments-in/pg | Primaria | [S] | A |
| 18 | TechCrunch: límites a difusiones (18/3/2025) | https://techcrunch.com/2025/03/18/whatsapp-will-soon-limit-number-of-broadcast-messages-users-and-businesses-can-send/ | Secundaria | [M] | B |
| 19 | TechCrunch: prohibición de chatbots generalistas (18/10/2025) | https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform | Secundaria | [S] | B |
| 20 | TechCrunch: Brasil/Italia excluidos (13 y 15/1/2026); Italia (24/12/2025) | https://techcrunch.com/2026/01/15/after-italy-whatsapp-excludes-brazil-from-rival-chatbot-ban ; https://techcrunch.com/2025/12/24/italy-tells-meta-to-suspend-its-policy-that-bans-rival-ai-chatbots-from-whatsapp/ | Secundaria | [S] | B |
| 21 | respond.io: fechas de la prohibición | https://respond.io/blog/whatsapp-general-purpose-chatbots-ban | Secundaria (BSP) | [S] | C |
| 22 | Tiendanube ayuda: desactivación de Meta Shops | https://ayuda.tiendanube.com/es_AR/facebook-e-instagram-shopping/acerca-de-la-desactivacion-de-meta-shops ; https://ayuda.tiendanube.com/como-activar-facebook-e-instagram-shopping | Secundaria (afectada) | [M] | B |
| 23 | ppc.land: fin del checkout en Shops | https://ppc.land/meta-phases-out-facebook-and-instagram-shops-checkout-by-august-2025/ | Secundaria | [S] | C |
| 24 | ChakraHQ: difusión paga en la app (17/11/2026) | https://chakrahq.com/article/whatsapp-business-app-paid-broadcast | Secundaria (proveedor) | [M] | C |
| 25 | Cliengo: In-chat checkout y pagos por país (act. 11/10/2026) | https://guiawabusiness.cliengo.com/in-chat-checkout-whatsapp | Secundaria (proveedor) | [M] | C |
| 26 | La Nación: bloqueos masivos (3/8/2026) | https://www.lanacion.com.ar/tecnologia/usuarios-en-todo-el-mundo-reportan-que-su-cuenta-de-whatsapp-fue-bloqueada-sin-previo-aviso-nid03082026/ | Secundaria | [M] | B |
| 27 | iProfesional: suspensión de cuentas (3/8/2026) | https://www.iprofesional.com/tecnologia/461427-whatsapp-suspendio-miles-cuentas-genero-caos-usuarios-dependen-app | Secundaria | [S] | C |
| 28 | Mercado Pago: link de pago | https://www.mercadopago.com.ar/herramientas-para-vender/link-de-pago | Primaria (MP) | [S] | A |
| 29 | Sleekflow / Chattigo (tarifas de terceros, discrepan) | https://help.sleekflow.io/es_/whatsapp/pricing ; https://blog.chattigo.com/whatsapp-business/cuanto-cobra-whatsapp-business-por-mensaje | Secundaria | [S] | D |
| 30 | La Nación: Meta Verified en Argentina (27/6/2023) | https://www.lanacion.com.ar/tecnologia/meta-verified-llega-a-la-argentina-el-servicio-de-verificacion-paga-de-cuentas-para-facebook-e-nid27062023/ | Secundaria | [S] | B |

## Huecos

1. **Precio en ARS de las difusiones comerciales de la app** (existe tabla ARS pero no la abrí) y **si la función está activa en Argentina**: Meta no publica la lista de países.
2. **Precio de Meta One / Meta Verified en pesos** y disponibilidad en Argentina.
3. **Fecha en que la ventana gratis de anuncios pasó de 72 h a «hasta 7 días».**
4. **Tarifas argentinas históricas en USD** (antes del 1/10/2025 y bajo el modelo por conversación): no verificadas en fuente primaria. Tampoco si la tabla ARS cambió entre el 1/4 y el 1/10/2026.
5. **Impuestos** sobre la factura de Meta en pesos (IVA, percepciones).
6. **Requisitos para ser BSP o Tech Provider** y sus cambios recientes.
7. **Fallos judiciales argentinos** por cuentas bloqueadas (la nota de iProUP no cargó) y **casos de comercios argentinos con pérdidas medidas** por un cambio de Meta.
8. **Cifras oficiales de Meta por país** (usuarios de WhatsApp en Argentina, empresas que usan WhatsApp Business en Argentina o Latam) y cifra oficial 2026 de empresas en la app.
9. **Fecha de inicio del límite de marketing por usuario** (Meta no la publica) y si se eliminaron los escalones de 2K y 10K en 2026 (un solo proveedor lo dice; la página de Meta todavía los lista).
10. **Cantidad exacta de dispositivos vinculados** en WhatsApp Business en 2026.
11. **Pago nativo en México** (dato de un proveedor, sin fuente de Meta leída) y el anuncio de «in-chat checkout» de junio de 2026 (no leído).
