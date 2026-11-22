---
resumen: >-
  Pagos es la parte del comercio electrónico que convierte una compra en dinero disponible para el comercio: quién interviene en el cobro, cuánto cuesta y cuándo llega el dinero, quién pierde si el pago se desconoce, y cómo cambian todo eso las cuotas y los medios locales de América Latina.
estado: vigente
estabilidad: estable
fuentes:
  - "Comercio-electronico/.investigacion/pagos.md"
  - "Comercio-electronico/.investigacion/huecos-pagos-y-operaciones.md"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (A7 y B6)"
  - "Comercio-electronico/.investigacion/vistazo.md"
  - "Las fuentes primarias de cada componente y ficha, citadas en cada nota"
aliases: [payments, pagos online, cobros, medios de pago, procesamiento de pagos, payment processing]
creado: 2026-11-22
revisado: 2026-11-22
---

# Pagos

Pagos es la parte del comercio electrónico que convierte una compra en dinero disponible para el comercio: quién interviene en el cobro, cuánto cuesta y cuándo llega el dinero, quién pierde si el pago se desconoce, y cómo cambian todo eso las cuotas y los medios locales de América Latina.

> [!WARNING]
> Ley y dinero: nada de esta vertical reemplaza el consejo de un abogado o un contador. Varias cifras y normas tienen una sola fuente, algunas solo de prensa; antes de decidir, se leen la norma o la tarifa en la fuente viva.

Recibe la orden de cobro de [Checkout y conversión](../Checkout-y-conversion/checkout-y-conversion.md) y, cuando el pago se aprueba, libera el pedido a [Operaciones del comercio](../Operaciones-del-comercio/operaciones-del-comercio.md). [Normativa](../Normativa/normativa.md) fija reglas a quien cobra y a cuánto se puede cobrar. Y la [plataforma de tiendas](../Plataforma-de-tiendas/plataforma-de-tiendas.md) puede quedarse con una parte de cada cobro, que llega a pesar más en su ingreso que la suscripción, como cuenta [el negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md).

## Un cobro pasa por varias manos

Un pago con tarjeta en una tienda online sale del titular, pasa por la tienda, una pasarela, un adquirente o agregador y la red de la tarjeta, y llega al banco emisor, que lo aprueba o lo rechaza. La respuesta vuelve por el mismo camino, y más tarde el dinero llega al comercio por el adquirente o el agregador. Cada mano cumple una función y cobra por ella.

El agregador cambia la relación del comercio con el resto: cobra por muchos comercios bajo una sola cuenta propia, así que el comercio no necesita contrato con un adquirente. A cambio, el agregador fija la tarifa y es quien le debita al comercio cuando un pago se disputa. En Argentina, quien cumple una función en un esquema de pago sin ser entidad financiera es un proveedor de servicios de pago, con reglas del BCRA.

## Lo que cuesta cobrar y cuándo llega el dinero

El comercio paga un porcentaje de cada venta, la tasa de descuento, que suma tres precios: la tasa de intercambio para el emisor, la tarifa de la red y el margen del adquirente o agregador. En la Unión Europea y en el débito de EE. UU. la parte del emisor tiene un tope legal; en Argentina el tope existió y, según dos notas de prensa y un estudio jurídico, el DNU 70/2023 lo eliminó. No se leyó el texto del decreto en el Boletín Oficial ni se confirmó que esa parte siga vigente.

El plazo también tiene precio. Que un pago aparezca acreditado no quiere decir que el dinero esté disponible: el comercio elige cuándo dispone de él, y cuanto antes lo quiere, más paga. Sobre la tasa se suman el cargo de la plataforma, el costo de ofrecer cuotas y los cargos por disputa. Conciliar todo eso contra lo vendido es trabajo propio de la tienda.

## Un pago aprobado todavía se puede perder

La aprobación no cierra el riesgo. Durante meses, el titular puede desconocer el pago ante su emisor, y el contracargo le saca el dinero al comercio y le cobra una tarifa. En Europa, el fraude se concentra en los pagos sin tarjeta presente, que son los de la venta online. Según Stripe, la autenticación 3-D Secure puede pasar la responsabilidad al emisor, pero con excepciones. Y varios motivos de contracargo vienen de la operación, como un producto que no llegó.

## Lo que cambia en América Latina

Dos cosas separan a la región del modelo de la tarjeta. La primera son las cuotas: las fuentes describen compras en pagos mensuales «sin interés» en Argentina, Brasil y México, y su costo lo pagan el comercio, los compradores al contado o, en programas oficiales, el Estado. Que las cuotas aumenten las ventas lo dicen sobre todo los procesadores que las cobran, sin método publicado.

La segunda son los rieles de los bancos centrales. Pix, en Brasil, compite con la tarjeta de crédito en la venta online, y en Argentina las Transferencias 3.0 y el QR interoperable cobran con acreditación en segundos y sin posibilidad de revertir. Cambian el costo, el plazo y el riesgo de cobrar, y no tienen cuotas propias: Pix Parcelado no está confirmado.

Lo argentino es lo más inestable de la vertical. Los topes a los aranceles, los programas de cuotas y las tarifas cambiaron entre 2023 y 2026, y varias de esas normas se conocen solo por prensa. Por eso viven en fichas con fecha y no en los componentes.

## Pagos como sistema distribuido

Un cobro es una conversación entre sistemas de varias empresas, y cualquiera puede no contestar. Dos patrones de [Arquitectura](../../Arquitectura/arquitectura.md) resuelven los problemas que eso trae a una tienda: la [clave de idempotencia](../../Arquitectura/clave-de-idempotencia.md) evita cobrar dos veces cuando se reintenta, y la [saga](../../Arquitectura/saga.md) deshace los pasos de un checkout cuando el pago falla a mitad de camino.

## Cómo se mira Pagos en una plataforma de tiendas

Al analizar una plataforma de tiendas, pagos es la parte del precio que no aparece en la lista de planes. Las preguntas que salen de esta vertical:

| Pregunta | Componente que la explica |
|---|---|
| ¿La plataforma es agregador propio, integra terceros o las dos cosas? | [actores del pago](actores-del-pago.md) |
| ¿Cuánto paga el comercio por venta, sumando tasa, plazo y cargo de la plataforma? | [costo de cobrar](costo-de-cobrar.md) |
| ¿Quién gestiona las disputas y cuánto riesgo absorbe la plataforma? | [fraude y contracargos](fraude-y-contracargos.md) |
| ¿Deja ofrecer cuotas sin interés y quién paga su costo? | [cuotas](cuotas.md) |
| ¿Qué medios locales ofrece en el checkout, además de la tarjeta? | [medios de pago locales](medios-de-pago-locales.md) |

Se responden con la documentación pública de la plataforma y abriendo una tienda de prueba, como cuenta el [desarme de producto](../../Estrategia-competitiva/Analisis-de-competidores/desarme-de-producto.md), siempre con la fecha de la consulta.

## Qué hay en Pagos

Los términos de la vertical (pasarela, tasa de descuento, proveedor de servicios de pago, contracargo, 3-D Secure) están definidos en el [glosario del tema](../Fundamentos/glosario-de-comercio-electronico.md).

Para entender la vertical, leer los componentes en este orden:

- [Actores del pago](actores-del-pago.md): quién es quién en un cobro con tarjeta (emisor, red, adquirente, procesador, pasarela, agregador) y qué es un proveedor de servicios de pago para el BCRA.
- [Costo de cobrar](costo-de-cobrar.md): de qué se compone la tasa de descuento, por qué el plazo tiene precio y qué es conciliar.
- [Fraude y contracargos](fraude-y-contracargos.md): cómo corre un contracargo, sus motivos, qué hace 3-D Secure y quién pierde.
- [Cuotas](cuotas.md): quién paga el «sin interés» y qué se sabe de su efecto en ventas.
- [Medios de pago locales](medios-de-pago-locales.md): transferencias instantáneas, QR, billeteras y Pix, y qué cambian frente a la tarjeta.

Las fichas, con datos fechados al 2026-11-22:

- [Régimen argentino de tarjetas y cuotas](regimen-argentino-de-tarjetas-y-cuotas.md): los topes a los aranceles, el DNU 70/2023, Ahora 12 y Cuota Simple, con lo que no está verificado.
- [Costos de cobro en Argentina](costos-de-cobro-en-argentina.md): la tarifa de la transferencia, las tasas de un agregador por plazo (de 2023 y discrepantes) y el cargo de una plataforma.
- [Tasas de intercambio reguladas](tasas-de-intercambio-reguladas.md): los topes de la UE y de EE. UU. y el promedio de EE. UU. en 2024.
- [Fraude de pagos en Europa](fraude-de-pagos-en-europa.md): las cifras de 2024 del informe de la EBA y el BCE.
- [Pix en cifras](pix-en-cifras.md): el uso de Pix según su banco central y su participación en la venta online de Brasil según procesadores.
