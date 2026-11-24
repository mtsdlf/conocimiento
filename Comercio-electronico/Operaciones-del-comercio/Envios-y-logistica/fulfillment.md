---
resumen: >-
  El fulfillment (guarda de stock tercerizada) es el servicio en el que un operador guarda el stock del comercio en su depósito, prepara cada pedido cuando entra la venta y lo despacha. Se cobra por almacenar, por preparar cada pedido y por despachar, y suele pedir un volumen mínimo; el de un marketplace solo sirve para lo que se vende en ese marketplace.
estado: borrador
estabilidad: estable
fuentes:
  - "Comercio-electronico/.investigacion/envios-agregadores-y-fulfillment.md"
  - "Comercio-electronico/.investigacion/envios-transportistas-y-tarifas.md"
  - "Zipnova, fulfillment: https://www.zipnova.com/servicios-zipnova/fulfillment/ (leída el 2026-11-22)"
  - "Shipnow, fulfillment: https://shipnow.com.ar/fulfillment (leída el 2026-11-22)"
  - "Develop Argentina, logística y fulfillment para e-commerce en Argentina, 11/11/2025: https://developargentina.com/blog/logistica-fulfillment-ecommerce-argentina-2025 (por resumen de una herramienta; consultora, no operador)"
aliases: [fulfillment, guarda de stock, almacenamiento tercerizado, 3PL, third-party logistics, operador logístico, pick and pack, preparación de pedidos, Full]
creado: 2026-11-22
revisado:
---

# Fulfillment

El fulfillment (guarda de stock tercerizada) es el servicio en el que un operador guarda el stock del comercio en su depósito, prepara cada pedido cuando entra la venta y lo despacha. Se cobra por almacenar, por preparar cada pedido y por despachar, y suele pedir un volumen mínimo; el de un marketplace solo sirve para lo que se vende en ese marketplace.

Es la capa de [envíos y logística](envios-y-logistica.md) que está antes del transportista. El nombre se confunde con el cumplimiento del pedido en general, que en [operaciones del comercio](../operaciones-del-comercio.md#el-pedido-y-su-cumplimiento) es el registro de lo que salió; acá es el servicio de un tercero que hace ese trabajo físico.

## Qué se cobra

Los operadores leídos describen el mismo esquema en tres partes, sin publicar montos:

| Parte | Qué cubre | Cómo se mide |
|---|---|---|
| Almacenaje | el espacio que ocupa el stock | por posición de pallet, por metro cúbico o por unidad, por día o por mes; algunos cobran más por el stock que no rota |
| Preparación (pick and pack) | sacar las unidades, embalarlas y etiquetarlas | por pedido preparado, con un extra por unidad o por embalaje especial |
| Despacho | entregar el pedido al transportista o a la última milla | el envío, aparte |

La única cifra pública leída para Argentina es de una guía de una consultora, no de un operador: el centro de un transportista grande cobraría de 0,80 a 1,50 USD por metro cúbico por mes y de 2,50 a 4 USD por pedido preparado, y otros tres operadores, rangos parecidos (noviembre de 2025, sin método). El fulfillment de un marketplace cobra almacenamiento por unidad y por día y un cargo por unidad vendida, con un recargo por el stock que pasa cierto tiempo sin venderse (detalle en [envíos en Argentina](envios-en-argentina.md#mercado-libre)).

## Desde qué volumen

El fulfillment tercerizado reemplaza un costo fijo (depósito, gente, tiempo del dueño) por uno variable, y conviene cuando el volumen alcanza para que el operador lo tome. Uno de los operadores argentinos se orienta, según la ayuda de una plataforma, a comercios «con más de 100 envíos al mes»; la guía citada pone el umbral para un depósito propio con software de almacén en 50 a 100 pedidos por día. En la lectura de la base, un comercio que manda unas pocas decenas de envíos por mes queda debajo de esos mínimos y prepara él, en su casa o en su local. Lo que no hay es una oferta publicada para ese tramo.

## El fulfillment del marketplace y el independiente

El marketplace ofrece su propio fulfillment: el comercio manda el stock a su depósito y el marketplace vende, prepara y entrega con su red, con mejor posición en los resultados. Sirve solo para lo que se vende ahí: la venta de la tienda propia sale de otro stock. Por eso un comercio que vende en varios canales parte el stock o contrata un operador independiente que despache para todos, y vuelve el problema de la [sobreventa entre canales](../catalogo-y-stock.md).

> [!NOTE] Sin fuente todavía: precios publicados de fulfillment independiente en Argentina, y las tarifas oficiales de almacenamiento y stock viejo del fulfillment del marketplace (la ayuda oficial no se pudo leer).
