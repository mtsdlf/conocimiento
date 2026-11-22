---
resumen: >-
  Cobrar una venta con tarjeta le cuesta al comercio un porcentaje del monto, la tasa de descuento, que se reparte entre el emisor, la red y el adquirente o agregador, y que sube cuanto antes quiera disponer del dinero. Conciliar es comprobar que lo acreditado, menos lo descontado, coincide con lo vendido.
estado: vigente
estabilidad: semi
fuentes:
  - "Reglamento (UE) 2015/751, EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R0751 (leído vía herramienta de resumen: arts. 3, 4, 5, 7, 9 y 18)"
  - "Federal Reserve, Regulation II Average Interchange Fee, datos 2024: https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm (leído vía herramienta de resumen)"
  - "BCRA, Transferencias 3.0, sin fecha: https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ (leído vía herramienta de resumen)"
  - "Stripe, How disputes work, consultado 2026-11-22: https://docs.stripe.com/disputes/how-disputes-work (leído vía herramienta de resumen; empresa que vende pagos)"
  - "Tiendanube, ayuda, preguntas frecuentes sobre Mercado Pago, sin fecha: https://ayuda.tiendanube.com/es_ES/122921-mercado-pago/preguntas-frecuentes-sobre-mercado-pago (leído vía herramienta de resumen; plataforma con interés comercial)"
  - "La Nación, 21/12/2023, y Ámbito, sobre el DNU 70/2023 y las tarjetas (ver la ficha del régimen argentino)"
  - "Comercio-electronico/.investigacion/pagos.md (sección 2)"
  - "Comercio-electronico/.investigacion/huecos-pagos-y-operaciones.md (sección 1)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (A7, glosario)"
aliases: [merchant discount rate, MDR, tasa de descuento, arancel, comisión por cobro, interchange, tasa de intercambio, scheme fee, plazo de acreditación, settlement time, conciliación, reconciliation]
creado: 2026-11-22
revisado: 2026-11-22
---

# Costo de cobrar

Cobrar una venta con tarjeta le cuesta al comercio un porcentaje del monto, la tasa de descuento, que se reparte entre el emisor, la red y el adquirente o agregador, y que sube cuanto antes quiera disponer del dinero. Conciliar es comprobar que lo acreditado, menos lo descontado, coincide con lo vendido.

> [!WARNING]
> Ley y dinero: esta nota no reemplaza el consejo de un abogado o un contador. Las normas se leyeron por resúmenes y las cifras argentinas tienen una sola fuente o solo prensa; antes de decidir, se leen en la fuente viva.

Quién es cada uno de esos actores está en [actores del pago](actores-del-pago.md). Este costo es una línea fija del margen de cada venta, y por eso entra en la [economía unitaria](../../Marketing/Medicion/economia-unitaria.md) de una tienda.

## Tres precios dentro de la tasa de descuento

La tasa que ve el comercio suma tres precios, tal como los separa el Reglamento europeo que se cita abajo. La tasa de intercambio (interchange) va al emisor; la tarifa de la red (scheme fee) va a la marca de la tarjeta; y el margen queda para el adquirente o el agregador que le cobra al comercio.

El Reglamento (UE) 2015/751 es la norma corta que mejor muestra esa separación. Pone topes a la tasa de intercambio (arts. 3 y 4), cuenta como intercambio cualquier remuneración con efecto equivalente (art. 5), exige separar el esquema del procesamiento (art. 7) y obliga al adquirente a ofrecer los cargos desglosados por categoría y marca, salvo que el comercio pida por escrito otra cosa (art. 9). Los valores de los topes de la UE y de EE. UU. están en [tasas de intercambio reguladas](tasas-de-intercambio-reguladas.md).

> [!NOTE]
> Sin fuente todavía: cómo arma un agregador su tarifa única, que mezcla los tres precios en un solo porcentaje, en una fuente primaria. El art. 9 del Reglamento europeo, que distingue cargos desglosados de cargos mezclados, es la mejor referencia conceptual que se encontró, y no habla de América Latina.

## Lo que se regula y lo que se negocia

Donde un Estado topea la tasa de intercambio, la parte del emisor queda acotada; se infiere que la competencia entre adquirentes se da en su margen. La UE topea crédito y débito de consumo desde 2015; EE. UU. topea solo el débito de los emisores grandes.

En Argentina la Ley 25.065 topeaba lo que el emisor podía descontarle al comercio. Según dos notas de prensa y un estudio jurídico (este último, por un resumen del buscador), el DNU 70/2023 eliminó ese tope; no se leyó el texto del decreto en el Boletín Oficial ni se confirmó que esa parte siga vigente. Según La Nación, desde entonces el arancel queda librado a la negociación entre comercios y tarjeteras. El detalle, las cifras de los topes anteriores, una contradicción sin resolver sobre qué artículos cambió el DNU y lo que no está verificado están en el [régimen argentino de tarjetas y cuotas](regimen-argentino-de-tarjetas-y-cuotas.md); el marco legal general, en [Normativa](../Normativa/normativa.md).

## El plazo también tiene precio

Un comercio puede cobrar antes o más barato, pero no las dos cosas. Un agregador adelanta el dinero que el adquirente todavía no le liquidó, y cobra por ese adelanto: la tasa baja a medida que el comercio acepta esperar más días. La forma de esa tarifa, con un ejemplo argentino de 2023 cuyas cifras no coinciden entre fuentes, está en [costos de cobro en Argentina](costos-de-cobro-en-argentina.md).

Que el agregador adelanta fondos es una inferencia de esa forma de tarifa, no una afirmación de una fuente. Lo que sí dice una fuente es la diferencia entre dos momentos. Según la ayuda de una plataforma de tiendas, los pagos con tarjeta se acreditan «de forma instantánea», pero la disponibilidad del dinero «depende del plazo configurado en tu cuenta», y cada plazo «tiene un costo diferente». Acreditado no es disponible: el pago aparece en la cuenta enseguida, y el dinero se puede usar en la fecha que el comercio eligió y pagó.

## Lo que se suma a la tasa

| Costo | Qué es | Dónde está el dato |
|---|---|---|
| Cargo por disputa | Un agregador debita el monto disputado más una tarifa de disputa, no reembolsable salvo en México según Stripe; si el comercio contesta, se suma una tarifa por contestar, que se devuelve si gana | [fraude y contracargos](fraude-y-contracargos.md) |
| Costo de las cuotas | Lo que el comercio paga para ofrecer cuotas sin interés | [cuotas](cuotas.md) |
| Cargo de la plataforma | Lo que la plataforma de tiendas cobra por cada venta, a veces solo si el comercio usa un medio de cobro de terceros | [costos de cobro en Argentina](costos-de-cobro-en-argentina.md) |
| Otro medio de pago | La transferencia tiene su propia tarifa y no pasa por la red de tarjetas | [medios de pago locales](medios-de-pago-locales.md) |

## Conciliar: lo acreditado contra lo vendido

Conciliar es cruzar las ventas con los cobros y con el banco. Cada venta llega con un descuento distinto según el medio, el plazo y las cuotas; algunas vuelven meses después como contracargo; y las liquidaciones juntan muchas ventas en un solo depósito. Esa lista de causas es una inferencia de cómo funciona el cobro, no un dato de una fuente.

> [!NOTE]
> Sin fuente todavía: cómo se concilia en la práctica y qué formato tienen las liquidaciones de adquirentes y agregadores en Argentina.

Una causa más de diferencia entre lo cobrado y lo acreditado son los impuestos que quien procesa el pago retiene del cobro; cómo funcionan está en [Normativa](../Normativa/normativa.md), y los impuestos de una empresa en general, en [Legal e impuestos](../../Emprender/Legal-e-impuestos/legal-e-impuestos.md).

## Cómo comparar el costo de cobrar entre plataformas

Comparar plataformas de tiendas por el precio del plan deja afuera la parte del costo que crece con las ventas. Para un comercio que vende un monto dado por mes, el costo total suma el plan, el cargo de la plataforma por venta, la tasa del medio de cobro según el plazo elegido, el costo de las cuotas y los cargos por disputa. Por ejemplo, una plataforma con plan más caro y sin cargo por venta puede salir más barata que otra con plan barato y cargo por venta, a partir de cierto volumen. El punto de cruce se calcula con las tarifas del día.

Esa cuenta se hace con la misma fecha para todas las plataformas, porque las tarifas cambian seguido. Cómo se lee la lista de precios de un competidor está en [precios de la competencia](../../Producto/Monetizacion/precios-de-la-competencia.md), y por qué los pagos pesan tanto en el ingreso de una plataforma, en [el negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md).

El recurso para entender el mecanismo es el [Reglamento (UE) 2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R0751): leer los arts. 3, 4, 5, 7 y 9, y fijarse en la diferencia entre poner un tope y obligar a desglosar el cargo. Para Argentina, el DNU 70/2023 en sus arts. 14, 19 y 23, junto con la historia del art. 15 en la [página de actualización de la Ley 25.065](https://www.argentina.gob.ar/normativa/nacional/ley-25065-1998-55556/actualizacion).
