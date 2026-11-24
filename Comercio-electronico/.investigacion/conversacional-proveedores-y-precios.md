# Comercio conversacional en Argentina: quién atiende al comercio que vende por chat y cuánto cobra

**Fecha:** 2026-11-22. **Método:** páginas de precios propias de cada proveedor leídas con un lector web (WebFetch) y búsquedas (WebSearch) para lo que la página propia no dio. [L] = página leída (el lector devuelve un extracto fiel, no el HTML crudo); [S] = resumen del buscador, sin abrir la página. Calificación de fuente A (oficial del proveedor) a F (no confiable); calificación del dato 1 (confirmado por más de una fuente) a 6 (no se puede juzgar). Todo lo de la web se tomó como dato. Precios literales en su moneda; «IVA» solo cuando la página lo dice. No se agotó el cupo de búsquedas, pero se cortó a las ~50 consultas: lo que falta está en «Huecos».

## Respuesta corta

- **Casi todos cobran en dólares (o euros), no en pesos.** De las bandejas, bots y BSP, ninguno mostró precio en ARS. En pesos solo aparecen los catálogos argentinos (Pedix, desde $19.000/mes) y las apps de la tienda de Tiendanube (que cobra el plan en ARS y convierte las apps).
- **La entrada a una bandeja con WhatsApp oficial va de ~USD 45 a ~USD 150 por mes** (Wati Growth USD 45 anual, Waspy USD 70, Whaticket USD 49, Leadsales Profesional USD 106-133, Cliengo Premium USD 119, Botmaker USD 149), siempre **más la tarifa de Meta por mensaje**, que nadie incluye.
- **Quién recarga a Meta:** Wati (≈1,2× a 1,8× según categoría, medido por un tercero), Botmaker (+20 % en notificaciones), Chatfuel (+10 % en plantillas), 360dialog (+7 % en marketing por el endpoint estándar). **Al costo** dicen Gupshup (y cobra USD 0,001 por mensaje propio), Twilio (pasa Meta y cobra USD 0,005 por mensaje entrante o saliente), Zenvia, Waspy y Wassenger. Los demás no lo dicen.
- **Meta directo (Cloud API) no cobra cuota**, solo por mensaje entregado; da 1.000 mensajes de servicio gratis por número por mes, y **desde el 1/10/2026 los de servicio por encima de ese tope se cobran**. Argentina factura en ARS desde el 1/4/2026. Pero Cloud API no trae bandeja: hay que ponerle software encima.
- **Cobrar por chat:** el link de pago de Mercado Pago cuesta **6,29 % al instante, 4,39 % a 10 días, 3,39 % a 18 días y 1,49 % a 35 días** (la página no dice si es con o sin IVA); cuotas aparte (2x 7,79 % … 12x 32,29 %). Ualá Bis: 4,9 % + IVA al instante (Tiendanube) o 4,4 % (prensa, 7/2026). Ninguno cobra *dentro* de WhatsApp: se manda el link.
- **Instagram:** las etiquetas de producto (Instagram Shopping) **no están disponibles en Argentina desde el 10/8/2023**. La venta por Instagram es por DM, y la automatización típica es ManyChat (Pro desde USD 29 anual / USD 39 mensual con 500 contactos activos).

## Tabla de proveedores

| Proveedor | Qué hace | Origen | ¿Factura en AR / ARS? | Entrada (precio de lista/mes) | Incluye | Recargo sobre Meta | Prueba / plan gratis | Fuente |
|---|---|---|---|---|---|---|---|---|
| Meta Cloud API | API oficial directa | EE. UU. | Sí, ARS desde 1/4/2026 | Sin cuota | 1.000 msj de servicio gratis por número/mes | — (es Meta) | — | F1 [L] |
| Twilio | BSP / API | EE. UU. | USD; no vi página AR | Sin cuota | — | Pasa Meta al costo + **USD 0,005 por mensaje** entrante o saliente | No dice | F2 [L] |
| 360dialog | BSP / API | Alemania | EUR | **€49 por número** (Regular); €99 Premium; €500 Scale | Soporte; Premium suma bandeja | Metadatos: «no markup»; doc: **+7 %** en marketing por endpoint estándar | No dice | F3, F4 [L] |
| Gupshup | BSP / API | India/EE. UU. | USD | Sin cuota (autoservicio) | — | Meta «at actuals» + **USD 0,001 por mensaje** | No dice | F5 [L] |
| Infobip | BSP / API + plataforma | Croacia | No se pudo leer | Página de precios dio **403** | — | Sin dato (pasa Meta según terceros) | — | F6 [L], F7 [S] |
| Wati | Bandeja + bot + IA | Hong Kong/Singapur (sin verificar) | USD | **USD 45/mes anual** (Growth) en su página; un tercero midió USD 59 anual / USD 69 mensual | 3 usuarios, 500 contactos activos/mes | **Sí**: ≈1,6× marketing, ≈1,8× utilidad, ≈1,2× servicio (tercero, oct-2026) | 7 días / no | F8 [L], F9 [L] |
| Cliengo | Bot IA + bandeja + WhatsApp | Argentina (la página no lo dice) | USD | **USD 119** Premium; USD 259 Business | Premium: 3 operadores, 2.000 conversaciones IA (24 h), WhatsApp por *coexistencia* (API aparte); Business: 5 op., 4.000 conv., 1 línea API | No dice (su guía estima ~20 % para un BSP genérico) | 14 días / no | F10 [L], F11 [L] |
| Botmaker | Bot + bandeja | Argentina (sin verificar) | USD | **USD 149** Standard | 3.000 conversaciones, 10 agentes; excedente USD 0,07 | **+20 %** en notificaciones; alta de cuenta USD 99 única vez | 300 conversaciones iniciales gratis | F12 [L] |
| Leadsales | CRM + bandeja | México | USD / MXN, no ARS | **USD 97 mensual / 77,60 anual** (Básico, **sin** API WhatsApp); **USD 133 / 106,40** Profesional (con API) | Prof.: 4 usuarios, 20.000 contactos, 1 número, **USD 10 de saldo Meta** incluido | Descuenta de saldo; no dice recargo | 14 días (Básico) / no | F13 [L] |
| Kommo | CRM + WhatsApp | EE. UU. (ex amoCRM) | USD | **USD 25 por usuario/mes**, mínimo 6 meses, sin pago mensual | 1 número WhatsApp | No dice | 14 días / no | F14 [L] |
| Zenvia | Plataforma de atención | Brasil | Página MX; «WhatsApp: No aplicable para Argentina»; ARS por PDF aparte | **USD 20** Starter (software 0 + paquete de canal); USD 150 Specialist | Starter 1 usuario, 100 interacciones; setup USD 137 si habilita WhatsApp | **Al costo** («sin margen añadido») | No / Starter USD 0 + canal | F15 [L] |
| B2Chat | Bandeja | Colombia (sin verificar) | USD (referenciales) | **USD 84** Básico con WhatsApp | 2 usuarios, 1.000 contactos únicos entrantes; excedente USD 0,05 | Meta aparte; no dice recargo | No dice | F16 [L] |
| Callbell | Bandeja | Italia/Suiza (sin verificar) | EUR, sin impuestos | **€14 por agente/mes** | — ; bot avanzado €59/mes; cuenta WhatsApp €20 | «sigue las tarifas de Meta»; no dice | 7 días / no | F17 [L] |
| SleekFlow | Bandeja + IA | Hong Kong | USD | **USD 49** Essential (anual) | 3 usuarios, desde 500 contactos | «Según la tarifa de SleekFlow» (sugiere tarifa propia) | 7 días Pro | F18 [L] |
| Respond.io | Bandeja + IA | Malasia | USD | **USD 79 anual / 99 mensual** (Starter) | 5 usuarios, 1.000 contactos activos | Meta no incluido; no dice recargo | 7 días / no | F19 [L] |
| Whaticket | Bandeja (QR, API o coexistencia) | Sin verificar | USD | **USD 49** (mín. 3 usuarios; −20 % anual) | 1 conexión; extra desde USD 20 | Meta aparte desde 1/10/2026 | 14 días | F20 [L] |
| Waspy | Bandeja + carritos para Tiendanube | EE. UU. (LLC en Delaware) | USD | **USD 70** Starter | 2 agentes, 1 número, 1.000 conversaciones iniciadas | **No** («no agrega markups») | 10 días | F21 [L], F22 [L] |
| Treble | Campañas + bot WhatsApp | Colombia (sin verificar) | — | **Sin precio publicado** (demo) | — | — | No | F23 [S] |
| ManyChat | Automatización Instagram/Messenger/WhatsApp | EE. UU. | USD | Pro **USD 29 anual / 39 mensual** con 500 contactos activos (otro tercero: Pro 29 con 2.500) | Gratis 25 contactos | Meta aparte por su billetera; no dice recargo | Plan gratis 25 contactos | F24 [L] 403, F25 [L], F26 [L] |
| Chatfuel | Bot IA WhatsApp/IG/FB | EE. UU. | USD | **USD 18** Business S (anual) | ~330 chats en su ejemplo | **+10 %** en plantillas | Sí, con saldo inicial | F27 [L] |
| Aivo | Bot IA | Argentina (Córdoba) | — | Hoy redirige a Engageware (comprada); un buscador cita USD 75 anual / 149 mensual + USD 0,18 por conversación | — | — | 30 días | F28 [S] |
| Wassenger | Bandeja/API | — | USD | USD 39,90 Professional | — | Plantillas al costo | — | F29 [S] |

## Proveedores de la API (BSP) y Meta directo

- **Meta Cloud API** [L, F1]: cobra por mensaje entregado, por categoría (marketing, utilidad, autenticación, servicio) y país del destinatario; los mensajes del cliente al comercio no se cobran. **1.000 mensajes de servicio gratis por número por mes; desde el 1/10/2026 los de servicio por encima se cobran.** La ventana de entrada gratis (anuncio «clic a WhatsApp») deja responder gratis hasta 7 días. No menciona ninguna cuota de plataforma. Argentina tiene tarifa propia y **ARS como moneda de facturación desde el 1/4/2026**. Mensajes del «Meta Business Agent» (IA de Meta): USD 2 por millón de tokens.
- **Twilio** [L, F2]: «Twilio's per-message fee for WhatsApp is $0.005, inbound or outbound», más la tarifa de Meta, que «Twilio passes through». Sin cuota mensual. Ojo: Twilio cobra también los **entrantes**, que Meta no cobra. La calculadora mostró «No charge» para marketing de Meta, probablemente por el país por defecto; no es dato de Argentina.
- **360dialog** [L, F3, F4]: cuota fija por número (canal): €49 Regular, €99 Premium (suma bandeja, envíos y automatización), €500 Scale; plataforma para socios desde €250/mes + €49 por canal. Los metadatos de la página dicen «no markup on Meta fees», pero su documentación agrega **«a 7% surcharge to Meta's standard rate»** para contenido de marketing por el endpoint estándar. Las dos fuentes son del mismo proveedor y no se contradicen del todo: sin recargo en general, +7 % en ese caso.
- **Gupshup** [L, F5]: USD 0,001 por mensaje (plantilla o sesión, también entrantes de texto), sin cuota; Meta «billed at actuals». La URL vieja (gupshup.io/whatsapp-api-pricing) da 404.
- **Infobip** [F6 L 403; F7 S]: la página de precios de WhatsApp dio **403**; su índice de precios solo dice que cobra por mensaje y que los paquetes los arma ventas. Un blog de terceros cita un Starter de USD 49,99 que no pude confirmar.

## Bandejas, bots y CRM

Ver tabla. Lo que no entra en la tabla:

- **Wati, dos fuentes:** su página [L, F8] muestra Growth USD 45, Pro USD 95, Business USD 239 (facturación anual), 500/1.000/2.500 contactos activos; un tercero [L, F9, revisado 26/10/2026] midió Growth USD 59 anual / 69 mensual y Pro 119 / 149, y comparó su tarifa por mensaje con la de Meta en EE. UU.: marketing USD 0,0400 vs 0,0250 (≈1,6×), utilidad 0,0061 vs 0,0034 (≈1,8×), servicio 0,0041 vs 0,0034 (≈1,2×). Wati no lo llama recargo. Otro competidor (YCloud) [S] estima +2,8 % marketing y +21 % utilidad: el dato de recargo es **3** (real, magnitud discutida). Usuario extra: USD 39 (Pro), USD 89 (Business); Growth no admite más de 3.
- **Cliengo** [L, F10]: el plan Premium conecta WhatsApp por *coexistencia* (el número sigue en la app y los mensajes los factura Meta directo); la API es costo adicional; Business trae una línea API. Pagos en USD. La guía de Cliengo [L, F11] dice que lo que se paga en Cliengo depende de plan, moneda local e impuestos y remite a un asesor.
- **Leadsales** [L, F13]: el plan más barato (Básico) **no tiene API de WhatsApp** (Messenger/web); para WhatsApp hay que ir a Profesional (USD 133 mensual / 106,40 anual), que incluye USD 10/mes de saldo para Meta.
- **Botmaker** [L, F12]: el único que pone el recargo en número: «costo transparente de WhatsApp + 20% de servicio» para notificaciones; respuestas dentro de las 24 h «sin costo» según su página (esto ya no es así en Meta desde 1/10/2026 por encima de 1.000 de servicio: discrepancia a vigilar).
- **Zenvia** [L, F15]: página de México en USD/MXN; dice que la tarifa de WhatsApp Business es «No aplicable para Argentina» y remite a un PDF para convertir a pesos. No lo abrí: hueco.
- **Whaticket** [L, F20]: no tiene planes fijos; arma desde USD 49 con mínimo 3 usuarios; permite conexión por QR (no oficial), API o coexistencia.
- **Waspy** [L, F21, F22]: sobre API oficial (Tech Provider de Meta); Starter USD 70 (2 agentes, 1.000 conversaciones iniciadas), Growth USD 100 (4 agentes, 5.000), Scale USD 150 (ilimitado). «No agrega markups». En la ficha de Tiendanube los datos estructurados dicen «0 ARS», que contradice el texto.
- **Treble** [S, F23]: sin precios públicos, todo por demo.
- **Aivo** [S, F28]: aivo.co redirige a engageware.com (adquirida); precio no confirmado.
- **Hilos**: no apareció en búsquedas; hueco.

## Catálogos que mandan el pedido por WhatsApp

| Catálogo | Moneda | Planes y precio/mes | Comisión por venta | Prueba / gratis | Fuente |
|---|---|---|---|---|---|
| Pedix (AR) | $ (pesos, sección Argentina; no dice IVA) | Principiante **$19.000**, Especialista $25.500, Pro $35.000; anual con 2 meses gratis | **No** («no cobra comisiones por venta ni por pedido») | 14 días | F30 [L]; un artículo viejo sin fecha citaba $2.900 / $4.700 / $6.600 [S, F31] |
| Kyte (BR) | «$» sin código (global) | PRO 9,99, GROW 13,99, PRIME 19,99; plan gratis 1 usuario. Otra página: PRO 19,99 / GROW 29,99 / PRIME 39,99 [S] | No dice | 7 días GROW, luego gratis | F32 [L], F33 [S] |
| Take App (Singapur/Malasia, sin verificar) | USD | Basic gratis (50 pedidos/mes o ilimitados según la página), Business ~USD 37,50-50 | «No commissions» | Plan gratis | F34 [S]; página /pricing **404** |
| Tiendup | — | Página /precios **404** y el buscador no la encontró | — | — | Hueco |
| Tiendanube (plataforma, AR) | ARS | Inicial gratis; Esencial $27.999 o $20.999; Impulso $79.999 o $59.999; Escala $244.999 o $183.749 (dos cifras por plan, la página no dice cuál rige) | — (no es tema de este informe) | — | F35 [L] |
| Menú/pedidos (Pedisy, MenuDigital, Wabi) | — | No buscados por falta de cupo | — | — | Hueco |

**Tiendanube, lo propio:** su página de canal WhatsApp [L, F35] lista Chat Nube (asistente IA que arma el carrito en WhatsApp), Botón WhatsApp, Teclado Nube (buscar catálogo y mandar link en el chat), Marketing Nube (carritos abandonados por WhatsApp) y Pago Nube. Solo menciona la **app gratis** de WhatsApp Business, no la API. No dice precio por función.

**Apps de WhatsApp en la tienda de Tiendanube** (la página de la categoría devolvió solo metadatos; se leyeron fichas sueltas):

| App | Qué hace | Precio | Fuente |
|---|---|---|---|
| Waspy | Bandeja + carritos, API oficial | Desde USD 70/mes, 10 días | F22 [L] |
| Wames | Carritos abandonados + bandeja + IA, API oficial | Gratis con **9 % sobre lo recuperado**; Starter USD 29 + 7 %; Growth USD 79 + 5 %; Meta aparte | F36 [L] |
| Continuar por WhatsApp | Botón en producto y carrito con el pedido armado | **ARS 10.593,62/mes (R$ 39,9)**, 5 días de prueba. El buscador decía ARS 5.000 y 15 días: discrepancia, gana la ficha leída | F37 [L] |
| WhatsApp by Kampana/Klinko | Avisos de pedido y carritos, conexión por QR (posiblemente no oficial) | «Tarifa única» sin monto; 7 días | F38 [L] |
| Chat Center Network, Recupera Já, SAK | Carritos / bandeja | Sin precio en lo encontrado | F39 [S] |

**Shopify:** la app oficial de Meta «WhatsApp» es **gratis**, Meta cobra aparte en USD [L, F40]. Abundan apps con plan gratis de ~50 mensajes/mes y pagos de USD 1 a 15/mes (Beacon, Magebytes USD 14,99, Whatomation USD 5, WAlert USD 9) [S, F41].

## Cobro por chat

| Medio | Comisión | IVA | Fuente |
|---|---|---|---|
| Mercado Pago, link de pago | Al instante **6,29 %**; 10 días **4,39 %**; 18 días **3,39 %**; 35 días **1,49 %**. Cuotas, sumadas: 2x 7,79 %, 3x 10,49 %, 6x 18,69 %, 9x 26,49 %, 12x 32,29 %, 18x 41,59 %. Sin cargo fijo. | La página no lo dice; aclara «no incluyen retenciones o impuestos ajenos a Mercado Pago» y que varía por impuestos provinciales | F42 [L] (A, dato 2). La sección general de costos y la ayuda dieron **403** |
| Ualá Bis, link de pago | **4,9 % + IVA**, acreditación al instante, cualquier medio | + IVA | F43 [L] (ayuda Tiendanube, sin fecha visible) |
| Ualá Bis (otra fuente) | 4,4 % crédito, débito y prepaga con link | No dice | F44 [S] (prensa 7/7/2026) |
| Naranja X, link de pago | Sin tarifa de link publicada; plazos en el día, 2, 14 o 60 días; QR con dinero en cuenta 0,8 % + IVA; crédito 1 cuota 4,40 % a 24 h | + IVA | F45 [S] |
| MODO | El arancel lo pone el adquirente (Payway, Getnet, Nave), no MODO | + IVA | F46 [L] |

Ninguno cobra **dentro** de WhatsApp en Argentina en lo encontrado: el flujo es mandar el link en el chat. (WhatsApp Pay no apareció para Argentina: hueco declarado, no se buscó a fondo.)

## Ventas por Instagram

- **Instagram Shopping / etiquetas de producto: no en Argentina.** La ayuda de Tiendanube [L, F47] dice que «no está disponible en Argentina, Colombia y Chile desde el 10 de agosto de 2023» por decisión de Meta; sigue solo para México. Un artículo de Shopify en español [S] incluye a Argentina, pero es anterior al corte. No encontré la página de Meta: dato 2.
- **Respuesta automática de DMs:** ManyChat (gratis hasta 25 contactos; Essential USD 14 anual con 250; Pro USD 29 anual / 39 mensual con 500 contactos activos según un tercero del 2/11/2026 [L, F26]; otro tercero del 28/9/2026 da Pro USD 29 anual con 2.500 [L, F25]; excedente USD 0,05 por contacto en Pro). Su página propia dio **403** dos veces. Chatfuel cubre Instagram en todos sus planes desde USD 18 [L, F27].

## Insumos para el cálculo (500 y 3.000 conversaciones por mes)

Sin tarifa de Meta (la trae otro agente). Lo que cada opción suma **encima** de Meta:

| Opción | Costo fijo/mes | Variable propio | Sobre la tarifa de Meta | Límite que obliga a subir de plan |
|---|---|---|---|---|
| (a) App gratis WhatsApp Business | **0** | 0 | Meta no cobra en la app | 1 número; sin bandeja multiagente real (límite de dispositivos: hueco) |
| (b) Cloud API directa | **0** | 0 | Al costo; 1.000 de servicio gratis por número; ARS desde 4/2026 | Sin interfaz: hace falta software propio o una bandeja |
| (c) 360dialog | **€49** por número | 0 | Al costo, +7 % en marketing por endpoint estándar | Sin bandeja en Regular (Premium €99 la trae) |
| (c') Gupshup / Twilio | 0 | USD 0,001 (Gupshup) o USD 0,005 (Twilio) **por mensaje, incluidos entrantes** | Al costo | — |
| (d1) Wati | USD 45 anual (su página) o 59-69 (tercero) | — | ≈1,2× servicio, 1,6× marketing, 1,8× utilidad | Growth: 500 contactos activos y 3 usuarios → con 3.000 hace falta Business (USD 239, 2.500 contactos) + excedente o plan a medida |
| (d2) Cliengo | USD 119 (Premium, coexistencia) / **USD 259** (Business, 1 línea API) | — | No dice | Premium 2.000 conversaciones IA; Business 4.000 → 3.000 entra en Business |
| (d3) Leadsales | USD 133 mensual / 106,40 anual (Profesional) | — | Descuenta de saldo; trae USD 10 de Meta | 20.000 contactos, 4 usuarios: 500 y 3.000 entran |

Ojo para el cálculo: las unidades no coinciden entre proveedores (Wati y ManyChat cuentan **contactos activos**, Cliengo y Botmaker **conversaciones de 24 h**, Meta **mensajes entregados**, Twilio y Gupshup **mensajes enviados y recibidos**). Hay que fijar cuántos mensajes por conversación y qué parte es marketing para pasar de uno a otro.

Dato cruzado (no es de este ángulo, se anota por si discrepa con el otro agente): la guía de Cliengo [L, F11] da para Argentina USD 0,0618 por mensaje de marketing y USD 0,0260 utilidad, autenticación y servicio, «vigente desde 1/10/2026», y dice que Argentina factura en ARS desde 1/4/2026.

## Fuentes

| # | URL | Tipo | Fuente | Dato | Lectura |
|---|---|---|---|---|---|
| F1 | https://developers.facebook.com/docs/whatsapp/pricing | Meta, doc oficial | A | 1 | [L] |
| F2 | https://www.twilio.com/en-us/whatsapp/pricing | Precios propios | A | 2 | [L] |
| F3 | https://360dialog.com/pricing | Precios propios | A | 2 | [L] |
| F4 | https://docs.360dialog.com/docs/get-started/pricing.md | Doc propia | A | 2 | [L] |
| F5 | https://www.gupshup.ai/isv-partners/whatsapp-api/pricing | Precios propios | A | 2 | [L] |
| F6 | https://www.infobip.com/pricing/whatsapp | Precios propios | A | 6 | **403** |
| F7 | https://cdn-web.infobip.com/uploads/markdown-exports/www.infobip.com/pricing.md | Índice propio | A | 5 | [L] |
| F8 | https://www.wati.io/pricing/ | Precios propios | A | 3 (discrepa con F9) | [L] |
| F9 | https://www.eesel.ai/blog/wati-pricing | Tercero, revisado 26/10/2026 | C | 3 | [L] |
| F10 | https://www.cliengo.com/pricing | Precios propios | A | 2 | [L] (cliengo.com/precios da **404**) |
| F11 | https://guiawabusiness.cliengo.com/precios | Guía propia | B | 3 | [L] |
| F12 | https://botmaker.com/es/precios/ | Precios propios | A | 2 | [L] |
| F13 | https://www.leadsales.io/precios | Precios propios | A | 2 | [L] |
| F14 | https://www.kommo.com/pricing/ | Precios propios | A | 2 | [L] (truncada al final) |
| F15 | https://www.zenvia.com/es/precios/ | Precios propios (MX) | A | 2 | [L] |
| F16 | https://www.b2chat.io/precios/ | Precios propios («referenciales») | A | 3 | [L] |
| F17 | https://www.callbell.eu/es/precios/ | Precios propios | A | 2 | [L] |
| F18 | https://sleekflow.io/es/pricing | Precios propios | A | 2 | [L] |
| F19 | https://respond.io/pricing | Precios propios | A | 3 (tabla mal alineada) | [L] |
| F20 | https://whaticket.com/precios/ | Precios propios | A | 3 (datos estructurados no coinciden) | [L] |
| F21 | https://waspytech.com/planes | Precios propios | A | 2 | [L] |
| F22 | https://www.tiendanube.com/tienda-aplicaciones-nube/waspy | Ficha en tienda de apps | A | 2 | [L] |
| F23 | https://hackceleration.com/labs/treble-pricing | Tercero | D | 4 | [S] (treble.ai/precios **404**) |
| F24 | https://www.manychat.com/pricing | Precios propios | A | 6 | **403** (dos URL) |
| F25 | https://www.eesel.ai/blog/manychat-pricing | Tercero, 28/9/2026 | C | 3 | [L] |
| F26 | https://www.activepieces.com/blog/manychat-pricing-2026-plans-and-contact-tier-costs | Tercero, 6/11/2026 | C | 3 | [L] |
| F27 | https://chatfuel.com/pricing | Precios propios | A | 2 | [L] |
| F28 | https://www.aivo.co/product-tour-agentbot | Propia, redirige a engageware.com | C | 5 | [S] |
| F29 | https://wassenger.com/pricing?lang=es | Precios propios | A | 4 | [S] |
| F30 | https://info.pedix.app/ (sección pedix.app/ar/#precios) | Precios propios | A | 2 | [L] (pedix.app/precios **404**) |
| F31 | https://infonegocios.info/default/vender-por-whatsapp-es-mas-facil-pedix-acelera-el-proceso-catalogo-virtual-y-ventas-centralizadas | Prensa sin fecha | D | 5 (viejo) | [S] |
| F32 | https://www.kyteapp.com/subscription/global | Precios propios | A | 3 (discrepa con F33) | [L] |
| F33 | https://www.kyteapp.com/pro-plan | Propia | A | 4 | [S] (kyte.site **403**) |
| F34 | https://www.take.app/help/subscription-plans-and-features | Ayuda propia | B | 4 (internamente contradictoria) | [S] (take.app/pricing **404**) |
| F35 | https://tiendanube.com/canales/whatsapp | Propia | A | 3 (dos precios por plan) | [L] |
| F36 | https://www.tiendanube.com/tienda-aplicaciones-nube/wames | Ficha tienda de apps | A | 2 | [L] |
| F37 | https://www.tiendanube.com/tienda-aplicaciones-nube/continuar-pelo-whatsapp | Ficha tienda de apps | A | 3 (discrepa con buscador) | [L] |
| F38 | https://www.tiendanube.com/tienda-aplicaciones-nube/whatsapp-by-kampana-hub | Ficha tienda de apps | A | 4 | [L] |
| F39 | https://www.tiendanube.com/tienda-aplicaciones-nube/chat-center-network | Ficha tienda de apps | A | 5 | [S] |
| F40 | https://apps.shopify.com/whatsapp | Tienda de apps Shopify | A | 2 | [L] |
| F41 | https://apps.shopify.com/beacon-messenger (y otras de la búsqueda) | Tienda de apps Shopify | B | 4 | [S] |
| F42 | https://www.mercadopago.com.ar/herramientas-para-vender/link-de-pago | Precios propios | A | 2 | [L] (costs-section y ayuda **403**) |
| F43 | https://ayuda.tiendanube.com/es_AR/uala-bis/preguntas-frecuentes-sobre-uala-bis | Ayuda de plataforma | B | 3 | [L] |
| F44 | https://www.iprofesional.com/finanzas/347660-boom-de-pagos-electronicos-entre-emprendedores-y-comercios-chicos | Prensa 7/7/2026 | C | 4 | [S] |
| F45 | https://www.naranjax.com/comercios | Propia | A | 5 | [S] |
| F46 | https://yo-facturo.com/blog/link-de-pago-comparativa-argentina/ | Tercero, 16/11/2026 | C | 3 | [L] |
| F47 | https://ayuda.tiendanube.com/como-etiquetar-mis-productos-de-tiendanube-en-instagram-shopping | Ayuda de plataforma | B | 2 | [L] |

## Huecos

- **Páginas que dieron error:** Infobip (403), ManyChat (403 ×2), Mercado Pago sección de costos y ayuda (403), Kyte .site (403), Cliengo /precios, Treble /precios, Pedix /precios, Take App /pricing, Tiendup /precios, Gupshup URL vieja (404), categoría de la tienda de apps de Tiendanube (sin contenido).
- **Precios en pesos de los proveedores de bandeja:** ninguno publica ARS; Zenvia remite a un PDF que no abrí. Si el IVA y la percepción por servicios digitales del exterior se suman al cobro en USD: no buscado.
- **Recargo sobre Meta sin declarar:** Wati (solo medido por terceros), Cliengo, Leadsales, Kommo, B2Chat, Callbell, SleekFlow, Respond.io, ManyChat.
- **IVA del link de Mercado Pago:** la página no dice si 6,29 % etc. es con o sin IVA (históricamente se publicaba «+ IVA»: no confirmado hoy).
- **Naranja X y MODO:** sin tarifa de link de pago publicada.
- **Sin dato:** Tiendup, Hilos, Wabi, Pedisy, MenuDigital, precio de Treble, precio vigente de Aivo/Boti (Boti es el bot del Gobierno de la Ciudad, no un proveedor para comercios: no buscado), Kampana, Chat Center Network.
- **App gratis de WhatsApp Business:** límites (dispositivos vinculados, catálogo, difusiones) no verificados en esta pasada.
- **País de origen** marcado «sin verificar» en Wati, Botmaker, B2Chat, Callbell, Whaticket, Treble, Take App; Cliengo argentino por conocimiento previo, la página no lo dice.
- **WhatsApp Pay / cobro dentro del chat en Argentina:** no buscado a fondo.
