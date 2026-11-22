---
resumen: >-
  Un contracargo es la reversión de un pago con tarjeta que el titular desconoce o reclama ante su emisor: el dinero vuelve al titular y se le debita al comercio, salvo que este pruebe que la venta fue legítima o que la responsabilidad haya pasado al emisor. El fraude sin tarjeta presente, típico de la venta online, es su causa más estudiada.
estado: vigente
estabilidad: semi
fuentes:
  - "EBA y BCE, 2025 Report on Payment Fraud (EBA/REP/2025/40), diciembre de 2025: https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf (leído: resumen y capítulos 2 a 6)"
  - "Stripe, How disputes work, consultado 2026-11-22: https://docs.stripe.com/disputes/how-disputes-work (leído vía herramienta de resumen; empresa que vende pagos)"
  - "Stripe, Dispute categories, consultado 2026-11-22: https://docs.stripe.com/disputes/categories (leído vía herramienta de resumen: Visa completo, Mastercard solo el principio)"
  - "Stripe, 3D Secure authentication flow, consultado 2026-11-22: https://docs.stripe.com/payments/3d-secure/authentication-flow (leído completo vía herramienta de resumen)"
  - "EMVCo, 3-D Secure, consultado 2026-11-22: https://www.emvco.com/emv-technologies/3-d-secure/ (leído vía herramienta de resumen)"
  - "Clearsale, Understanding Visa chargeback time limits: https://www.clear.sale/blog/understanding-visa-chargeback-time-limits (según resumen del buscador; vende gestión de contracargos)"
  - "Chargebacks911, Visa chargeback time limit: https://chargebacks911.com/chargeback-rules/chargeback-time-limit/visa-chargeback-time-limit/ (según resumen del buscador; vende gestión de contracargos)"
  - "Ley 25.065, arts. 26 a 30, texto original de 1998: https://www.argentina.gob.ar/normativa/nacional/ley-25065-1998-55556/texto (leído vía herramienta de resumen)"
  - "Comercio-electronico/.investigacion/pagos.md (sección 3)"
  - "Comercio-electronico/.investigacion/huecos-pagos-y-operaciones.md (sección 2)"
aliases: [chargeback, contracargo, disputa, dispute, desconocimiento de compra, fraude con tarjeta, card fraud, card-not-present fraud, CNP, 3-D Secure, 3DS, liability shift, cambio de responsabilidad, representment]
creado: 2026-11-22
revisado: 2026-11-22
---

# Fraude y contracargos

Un contracargo es la reversión de un pago con tarjeta que el titular desconoce o reclama ante su emisor: el dinero vuelve al titular y se le debita al comercio, salvo que este pruebe que la venta fue legítima o que la responsabilidad haya pasado al emisor. El fraude sin tarjeta presente, típico de la venta online, es su causa más estudiada.

> [!WARNING]
> Ley y dinero: esta nota no reemplaza el consejo de un abogado o un contador. Los plazos salen de una empresa de pagos y de vendedores de gestión de contracargos, no del reglamento de las marcas, y la Ley 25.065 se leyó en su texto original, por un resumen.

Es el riesgo que queda después de que un pago se aprobó. Recorre hacia atrás la cadena de [actores del pago](actores-del-pago.md), y su costo se suma al [costo de cobrar](costo-de-cobrar.md).

## El fraude se concentra en el pago a distancia

En la venta online la tarjeta no está presente, y ahí se concentra el fraude. Según el informe de la EBA y el BCE de diciembre de 2025, en 2024 el fraude remoto fue alrededor del 83 % del fraude con tarjeta en Europa, aunque los pagos remotos eran solo ~28 % del valor de los pagos con tarjeta. Dentro del fraude remoto, el robo de los datos de la tarjeta explicó más del 56 % del valor.

Esas cifras miden desde el emisor y solo cubren tarjetas emitidas en la UE o el EEE; las demás están en [fraude de pagos en Europa](fraude-de-pagos-en-europa.md).

> [!NOTE]
> Sin fuente todavía: cifras de fraude y de contracargos en la venta online de Argentina o de América Latina de una fuente primaria (BCRA, bancos, Visa o Mastercard).

## Cómo corre un contracargo

Según la documentación de Stripe, una fuente de empresa y no el reglamento de las marcas, el recorrido es este:

1. El titular disputa el pago ante su emisor.
2. El emisor inicia el contracargo; la red debita al adquirente o agregador, y este debita al comercio el monto más una tarifa.
3. El comercio responde con evidencia, normalmente en 7 a 21 días según la red. Las guías de proveedores de gestión de contracargos llaman representment a esa respuesta.
4. El emisor decide, en 60 a 75 días. Si el comercio no queda conforme, siguen el precontracargo (pre-arbitration) y el arbitraje, según guías de proveedores de gestión de contracargos.

El ciclo completo toma de 2 a 3 meses. Las redes permiten iniciar la disputa normalmente dentro de los 120 días desde el pago, más en viajes o eventos. Stripe agrega que alrededor del 40 % de las alertas tempranas de fraude de Visa y Mastercard terminan en disputa por fraude; la cifra vale para esa plataforma.

> [!IMPORTANT]
> Los plazos no coinciden entre fuentes, y ninguna es el reglamento de Visa. Stripe da 7 a 21 días para que el comercio responda. Dos vendedores de gestión de contracargos, según resúmenes del buscador, dan 20 o 30 días, y dicen que el adquirente suele fijar plazos internos más cortos. Para iniciar la disputa, esos vendedores dan 120 días como base, hasta 540 para algunos motivos y 75 para otros. Los vendedores tienen interés comercial: venden recuperación de contracargos.

## Los motivos de un contracargo

Cada red clasifica las disputas con códigos de motivo. Estos son algunos de Visa, según la transcripción que publica Stripe:

| Motivo | Código de Visa |
|---|---|
| Fraude con tarjeta ausente, el típico de la venta online | 10.4 |
| Fraude con cambio de responsabilidad por chip (EMV) | 10.1 y 10.2 |
| Programa de monitoreo de fraude | 10.5 |
| Producto no recibido | 13.1 |
| Pago recurrente ya cancelado | 13.2 |
| Producto que no es como se describió o defectuoso | 13.3 |
| Crédito no procesado | 13.6 |
| Cobro duplicado | 12.6.1 |

Mastercard usa otros números, por ejemplo 4860 para crédito no procesado y 4834 para diferencias de monto o duplicados. No todo contracargo es fraude: varios motivos son fallas de la operación, como no entregar o no devolver el dinero, y se previenen en [operaciones del comercio](../Operaciones-del-comercio/operaciones-del-comercio.md).

## 3-D Secure traslada la responsabilidad, con excepciones

3-D Secure es un paso de autenticación del titular durante el pago. EMVCo, dueña de la especificación, dice que «EMV 3-D Secure (EMV 3DS) helps payment card issuers and merchants around the world prevent card-not-present (CNP) fraud» y recomienda la versión 2.2 o superior. Su página no habla de responsabilidad.

Según Stripe, si un pago autenticado con 3DS se disputa como fraude, «the liability typically shifts from you to the card issuer». La misma fuente lo limita: «Successful 3DS authentication doesn't guarantee liability shift». No corre si el comercio está en un programa de monitoreo de Visa por fraude excesivo, algunas industrias están exentas, y no cubre las disputas por producto no recibido. Es una sola fuente de empresa; las reglas de Visa y Mastercard sobre el cambio de responsabilidad no se obtuvieron.

El informe europeo también mide la autenticación fuerte del cliente (SCA), que según el mismo informe puede no ser exigible fuera del EEE. Según la EBA y el BCE, solo el 40 % de las operaciones de tarjeta iniciadas electrónicamente se autenticaron así en 2024, y «SCA-authenticated transactions showed lower fraud rates than non-SCA transactions, especially for card payments».

> [!NOTE]
> Sin fuente todavía: cuánto baja la conversión al pedir 3DS en el checkout, y los umbrales de contracargos que hacen entrar a un comercio en los programas de monitoreo de Visa y Mastercard. Lo que se sabe del checkout está en [Checkout y conversión](../Checkout-y-conversion/checkout-y-conversion.md).

## Quién pierde

La pérdida se reparte distinto según quién sea responsable. Según la EBA y el BCE, en 2024 los titulares cargaron con el 38 % de las pérdidas con tarjeta en Europa, con diferencias grandes entre países que el informe atribuye a regímenes de responsabilidad distintos. El informe no dice qué parte cae sobre los comercios.

Del lado del comercio, la cuenta de Stripe es directa: se le debita el monto y una tarifa de disputa, y recupera el monto solo si gana. Si además entregó el producto, pierde también la mercadería y el envío; esto último es una inferencia, no un dato de la fuente.

En Argentina, la Ley 25.065 en su texto original no usa la palabra contracargo. Regula cómo el titular «cuestiona» el resumen: tiene 30 días desde que lo recibe, por nota simple (art. 26); el emisor acusa recibo en 7 días y tiene 15 para corregir o explicar, 60 si la operación fue en el exterior (art. 27); y mientras dure el trámite no puede impedir el uso de la tarjeta dentro del límite (art. 28). Esa es la relación entre titular y emisor. La relación entre emisor y comercio, el contracargo propiamente dicho, se rige por contratos y por las reglas de las marcas. No se verificó si el DNU 70/2023 cambió esos artículos; el estado de la ley está en el [régimen argentino de tarjetas y cuotas](regimen-argentino-de-tarjetas-y-cuotas.md).

Los medios que no pasan por la red de tarjetas tienen otras reglas. Las transferencias de Argentina son irrevocables y Pix tiene un mecanismo de devolución propio para golpes y fraudes; los dos están en [medios de pago locales](medios-de-pago-locales.md).

## Cómo se usa al analizar una plataforma de tiendas

Frente a una plataforma de tiendas, la pregunta es cuánto de este riesgo absorbe por el comercio. Se mira si incluye una herramienta antifraude, si aplica 3DS y cuándo, si gestiona las disputas o deja al comercio solo frente al agregador, y cuánto cobra por disputa. Se responde con su documentación pública y sus condiciones, dos de las [fuentes públicas](../../Estrategia-competitiva/Analisis-de-competidores/fuentes-publicas.md) de un competidor.

Para las cifras, el recurso es el [informe de la EBA y el BCE de 2025](https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf): leer los capítulos 2 (niveles de fraude), 4 (efecto de la autenticación fuerte) y 5 (quién pierde), y fijarse en que mide desde el emisor, en que la tasa por valor y la tasa por cantidad difieren, y en que no cubre América Latina. Para el mecanismo, la [guía de disputas de Stripe](https://docs.stripe.com/disputes/how-disputes-work) es la mejor fuente abierta que se encontró, con sus límites; la fuente canónica serían las reglas de disputas de Visa (Visa Core Rules) y la guía de contracargos de Mastercard, que no se leyeron.
