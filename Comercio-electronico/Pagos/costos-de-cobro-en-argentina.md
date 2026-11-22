---
resumen: >-
  Las cifras públicas de lo que le cuesta a un comercio argentino cobrar con transferencia, con un agregador de pagos y a través de una plataforma de tiendas, con su fecha y sus discrepancias, a noviembre de 2026.
estado: vigente
estabilidad: volatil
fuentes:
  - "BCRA, Transferencias 3.0, sin fecha visible: https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ (leído vía herramienta de resumen, consultado 2026-11-22)"
  - "iProfesional, comisiones de Mercado Pago, 1/8/2023: https://www.iprofesional.com/tecnologia/386153-mercado-pago-que-debes-saber-sobre-comisiones-plazos-y-montos (leído vía herramienta de resumen)"
  - "Tiendanube, ayuda, preguntas frecuentes sobre Mercado Pago, sin fecha: https://ayuda.tiendanube.com/es_ES/122921-mercado-pago/preguntas-frecuentes-sobre-mercado-pago (leído vía herramienta de resumen; fuente de una plataforma con interés comercial)"
  - "iProfesional, Los secretos detrás de las cuotas sin interés, 19/02/2020: https://www.iprofesional.com/finanzas/309622-los-secretos-detras-de-las-cuotas-sin-interes (leído)"
  - "Mercado Pago, sección de costos: https://www.mercadopago.com.ar/costs-section/ (no se pudo abrir: 403, también el 2026-11-22)"
  - "SpomBridge, Comisiones de Mercado Pago 2026: https://app.spomsolutions.com/herramientas/comisiones-mercado-pago-2026 (leído 2026-11-22; C3, dice haber relevado la página oficial el 2-nov-2026)"
  - "Tiendanube, Pago Nube: https://www.tiendanube.com/soluciones/pago-nube (leída 2026-11-22; B1)"
  - "Comercio-electronico/.investigacion/pagos.md (sección 2)"
  - "Comercio-electronico/.investigacion/huecos-pagos-y-operaciones.md (sección 1)"
  - "Comercio-electronico/.investigacion/fundamentos-y-contraria.md (B6)"
aliases: [tasa de descuento en Argentina, comisiones de cobro, MDR Argentina]
creado: 2026-11-22
revisado: 2026-11-22
---

# Costos de cobro en Argentina

Las cifras públicas de lo que le cuesta a un comercio argentino cobrar con transferencia, con un agregador de pagos y a través de una plataforma de tiendas, con su fecha y sus discrepancias, a noviembre de 2026.

Implementa [el costo de cobrar](costo-de-cobrar.md). Consultado el 2026-11-22.

> [!WARNING]
> Ley y dinero: la ficha no reemplaza el consejo de un abogado o un contador, ni la tarifa que el proveedor muestra al comercio.

Ninguna fila es una tarifa vigente leída en la página oficial del proveedor: la de Mercado Pago devolvió 403 en 2023 y otra vez en noviembre de 2026, y Payway, Getnet y MODO no se pudieron abrir. La fuente viva para la tarifa de un agregador es su propia sección de costos, abierta desde un navegador y con fecha de captura.

## Transferencia: la única cifra de fuente primaria

El BCRA dice que en los pagos con transferencia el comprador no paga comisión y los comercios pagan «entre 6 y 8 por mil más IVA». La página no tiene fecha, y es una sola fuente, la del regulador. Es la única cifra argentina de costo por medio de pago que sale de una fuente primaria; el medio se explica en [medios de pago locales](medios-de-pago-locales.md).

## Agregador: la tasa cambia con el plazo, y las fuentes no coinciden

La tabla de una nota de prensa de iProfesional del 1/8/2023, sin fuente oficial, da para cobrar con Mercado Pago (más IVA):

| Medio | Disponible | Tasa |
|---|---|---|
| Crédito | al instante | 6,49 % |
| Crédito | a 10 días | 4,29 % |
| Crédito | a 18 días | 3,39 % |
| Crédito | a 35 días | 1,79 % |
| Débito | al instante | 1,24 % |
| Débito | a 1 día | 0,85 % |
| Saldo en cuenta | al instante | 0,8 % |

> [!IMPORTANT]
> Para los mismos tramos de crédito, un blog de Tiendanube de fecha no verificada da 6,49 %, 4,39 %, 3,39 % y 1,49 %, según un resumen del buscador; y Cronista da 6,39 % al instante, también según resumen. Las tres fuentes discrepan en los tramos de 10 y 35 días. Ninguna sirve como tarifa vigente: muestran la forma de la tarifa (más barata cuanto más espera el comercio), no su valor de hoy.

## Mercado Pago en 2026, según un tercero

SpomBridge, que vende un sistema de gestión, dice haber relevado la página oficial de Mercado Pago el 2-nov-2026. Para Link de pago y Checkout Pro en la Ciudad de Buenos Aires, más IVA: 6,29 % al instante, 4,39 % a 10 días, 3,39 % a 18 días y 1,49 % a 35 días; las cuotas sin interés suman de 7,79 % (2 cuotas) a 41,59 % (18). Es una sola fuente, de terceros (C3); la tabla completa, por provincia, está en la ficha de [Mercado Pago](mercado-pago.md). Los tramos de 10, 18 y 35 días coinciden con los del blog de Tiendanube citado arriba; el tramo al instante, no (6,29 % contra 6,49 %).

Pago Nube, la pasarela de Tiendanube, publica sus tarifas «a partir de» por plazo y por plan: en el plan gratis, 6,40 % a 1 día, 4,45 % a 7, 3,50 % a 14 y 2,99 % a 30 días, más IVA, y 1,50 % por transferencia. La tabla por plan está en la ficha de [Tiendanube](../Plataforma-de-tiendas/tiendanube.md#planes-públicos-en-pesos-argentinos).

## Plataforma de tiendas: acreditación, disponibilidad y cargo propio

La ayuda de Tiendanube, fuente de una plataforma con interés comercial, separa dos momentos. Los pagos con crédito y débito se acreditan «de forma instantánea», pero la disponibilidad del dinero «depende del plazo configurado en tu cuenta», y cada plazo «tiene un costo diferente». La misma página dice que la plataforma cobra un cargo por usar una plataforma de pagos de terceros, del 0,7 % al 2 % según el plan; el valor de cada plan está en la ficha de [Tiendanube](../Plataforma-de-tiendas/tiendanube.md), y por qué las plataformas cobran ese cargo, en [el negocio de una plataforma](../Plataforma-de-tiendas/negocio-de-una-plataforma.md).

## Cifras viejas que todavía circulan

Una nota de iProfesional de 2020 decía que el comercio pagaba un 3 % de comisión por el posnet y esperaba hasta 18 días hábiles para cobrar una venta en cuotas. Son datos de entonces, anteriores a la desregulación de los topes que cuenta el [régimen argentino de tarjetas y cuotas](regimen-argentino-de-tarjetas-y-cuotas.md): no son vigentes.
