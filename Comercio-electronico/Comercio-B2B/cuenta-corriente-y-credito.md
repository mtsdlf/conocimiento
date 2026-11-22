---
resumen: >-
  La cuenta corriente es el registro de lo que cada cliente debe y paga a lo largo del tiempo, y el crédito comercial es el plazo que el vendedor le da para pagar. En la venta entre empresas es común vender a plazo, así que vender incluye decidir a quién fiar, cuánto, y cobrar: en Argentina, el cheque electrónico es el cheque más usado.
estado: borrador
estabilidad: semi
fuentes:
  - "BCRA, Informe mensual de pagos minoristas, septiembre de 2026: https://www.bcra.gob.ar/archivos/Pdfs/PublicacionesEstadisticas/Informes/informe-mensual-pagos-minoristas-2026-09.pdf (leído)"
  - "Infobae, Crecieron los cheques rechazados por falta de fondos (1/5/2026): https://www.infobae.com/economia/2026/05/01/crecieron-los-cheques-rechazados-por-falta-de-fondos-y-duplican-el-nivel-de-hace-un-ano/ (leído)"
  - "Argentina.gob.ar, Emitir una Factura de Crédito Electrónica MiPyME: https://www.argentina.gob.ar/servicio/emitir-una-factura-de-credito-electronica-mipyme (leído)"
  - "Perfil, El problema no es vender sino cobrar (Observatorio PyME, 2.º trimestre de 2026): https://noticias.perfil.com/noticias/amp/empresas/el-problema-no-es-vender-sino-cobrar.phtml (leído)"
  - "INDEC, Encuesta de autoservicios mayoristas, agosto de 2026: https://www.indec.gob.ar/uploads/informesdeprensa/autoservicios_mayoristas_10_26AFB69B25A5.pdf (leído)"
  - "Comercio-electronico/.investigacion/b2b-rasgos-y-factura.md y b2b-marketplaces-y-region.md"
aliases: [cuenta corriente, crédito comercial, trade credit, net terms, términos de pago, condiciones de pago, venta a plazo, fiado, echeq, cheque electrónico, cobranza]
creado: 2026-11-22
revisado:
---

# Cuenta corriente y crédito

La cuenta corriente es el registro de lo que cada cliente debe y paga a lo largo del tiempo, y el crédito comercial es el plazo que el vendedor le da para pagar. En la venta entre empresas es común vender a plazo, así que vender incluye decidir a quién fiar, cuánto, y cobrar: en Argentina, el cheque electrónico es el cheque más usado.

Es el rasgo del [comercio entre empresas](comercio-b2b.md) que más lo aleja de una tienda al público, donde el cobro es en el momento y lo resuelve un tercero (ver [Pagos](../Pagos/pagos.md)). Aquí el que financia es el vendedor. Se cruza con el [precio por cliente](precio-por-cliente.md), porque la lista puede cambiar con el plazo, y con la [factura entre empresas](factura-entre-empresas.md), porque una factura puede convertirse en un título de cobro.

## Qué decide quien vende a plazo

1. **El plazo**: contado o a una cantidad de días; 30, 60 y 90 son los ejemplos que da la prensa. Una nota sobre el Observatorio PyME dice que una operación puede cobrarse «a 60, 90 o más días». No hay medición pública del reparto de plazos en el comercio mayorista.
2. **El límite de crédito**: cuánto puede deber cada cliente antes de que se le corte la venta.
3. **El medio de cobro**: efectivo al repartidor, transferencia, cheque o cheque electrónico (ECHEQ) a fecha.
4. **La cobranza**: quién va a cobrar, que puede ser el mismo vendedor que toma el pedido (ver [preventa y autoventa](preventa-y-autoventa.md)), y qué pasa con la mora.

El software tiene que llevar el saldo de cada cliente, avisar cuando se pasa del límite al tomar un pedido nuevo y registrar los cobros parciales. En las capas mayoristas de las tiendas al público, cuando aparece, se llama «net terms»: una app mayorista de Shopify ofrece plazos de 15, 30 y 60 días desde su plan de US$ 44,99 por mes ([portales B2B globales](portales-b2b-globales.md)).

## El cheque electrónico manda en Argentina

En septiembre de 2026 se compensaron 5,1 millones de cheques por $ 26,9 billones, según el BCRA. El ECHEQ fue el 66% de la cantidad (3,4 millones) y el 86,2% del monto ($ 23,2 billones), 7,1 y 4,4 puntos más que un año antes. Los cheques rechazados por falta de fondos fueron el 1,7% de la cantidad y el 1,1% del monto ese mes. En marzo de 2026, según Infobae citando al BCRA, la tasa había llegado a 2,2% en cantidad, contra apenas más de 1% un año antes.

El plazo también aprieta a quien vende. En el segundo trimestre de 2026, el 62% de las industrias pyme vio alargarse los plazos de cobro de sus clientes y el 24% se atrasó en sus propios vencimientos, según el Observatorio PyME citado por Perfil. Es un dato de industria, no de comercio mayorista.

## La factura que se vuelve título

La Factura de Crédito Electrónica MiPyME convierte una venta a plazo en un documento que se puede negociar. Es obligatoria cuando una MiPyME le factura a una empresa grande por $ 5.549.862 o más (monto vigente desde el 14 de abril de 2026). El comprador tiene 21 días corridos para aceptarla o rechazarla, un plazo excepcional prorrogado hasta el 31 de octubre de 2027; si no hace nada, queda aceptada y pasa a ser un título ejecutivo que se puede descontar en un banco o en el mercado de capitales. Los detalles están en [factura entre empresas](factura-entre-empresas.md).

## Dónde se ve y dónde no

En el autoservicio mayorista, INDEC mide los medios de pago: en agosto de 2026, el 24,8% de las ventas del panel se pagó en efectivo, el 26,8% con tarjeta de crédito y el resto con débito y otros medios. No mide la venta en cuenta corriente. Que el crédito comercial largo esté sobre todo en el distribuidor que visita es inferencia.

En las reseñas de las apps con que los fabricantes y los marketplaces toman pedidos de almacenes, ninguna de 75 reseñas negativas leídas menciona el crédito ni el pago (codificación en [marketplaces y apps B2B de la región](marketplaces-y-apps-b2b-de-la-region.md)). Puede querer decir que la cuenta corriente se maneja fuera de la app, con el distribuidor, o que no es motivo de queja pública: no prueba ninguna de las dos.

> [!NOTE]
> Sin fuente todavía: el reparto de plazos y medios de cobro en el comercio mayorista, la mora de los comercios minoristas con sus proveedores, y las percepciones y retenciones que se descuentan de cada cobro.
