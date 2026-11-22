---
resumen: >-
  El catálogo y el stock son lo que hace posible una venta: la unidad que se vende es la variante de un producto, identificada por su SKU, y su stock se lleva por ubicación y repartido en estados (disponible, apartado, dañado). Sin esos estados, cada canal vende contra una copia del número y aparece la sobreventa.
estado: vigente
estabilidad: estable
fuentes:
  - "Shopify, guía de apps de gestión de inventario: https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps (leída a través de un resumen de una herramienta)"
  - "Shopify, objeto ProductVariant de la Admin GraphQL API: https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant (leída a través de un resumen)"
  - "Comercio-electronico/.investigacion/operaciones-canales-y-normativa.md"
aliases: [catálogo, stock, inventario, variante, SKU, stock keeping unit, sobreventa, overselling, stock por ubicación, stock de seguridad]
creado: 2026-11-22
revisado: 2026-11-22
---

# Catálogo y stock

El catálogo y el stock son lo que hace posible una venta: la unidad que se vende es la variante de un producto, identificada por su SKU, y su stock se lleva por ubicación y repartido en estados (disponible, apartado, dañado). Sin esos estados, cada canal vende contra una copia del número y aparece la sobreventa.

Es el primer eslabón de la cadena que describe [Operaciones del comercio](operaciones-del-comercio.md): el pedido aparta stock de una variante y la [devolución](devoluciones.md) lo repone. Cuando el stock lo lleva un [sistema de gestión](Sistemas-de-gestion/sistemas-de-gestion.md) y no la plataforma de tiendas, la pregunta pasa a ser cuál de los dos manda.

## La unidad que se vende es la variante

La unidad que se vende no es el producto, es la variante. En la documentación de Shopify, que describe el modelo de esa empresa y no el del campo, una variante es "una versión de un producto que tiene más de una opción, como talla o color". Cada variante pertenece a un producto y tiene su `sku`, el código que la identifica dentro de la tienda (distingue mayúsculas). Ese código hace falta para conectar un servicio externo de preparación de pedidos.

El stock cuelga de la variante. En el mismo modelo, cada variante tiene un ítem de inventario, y ese ítem tiene cantidades en cada ubicación (un depósito, un local). Una remera en tres talles y dos colores son seis variantes con seis stocks.

## El stock se reparte en estados

Una cantidad de stock sola no alcanza para vender sin errores. Shopify la parte en estados por ubicación:

| Estado | Qué cuenta |
|---|---|
| `incoming` | lo que está por llegar |
| `on_hand` | lo que está físicamente: la suma de los seis estados siguientes |
| `available` | lo que se puede vender |
| `committed` | lo apartado para pedidos que todavía no se cumplieron |
| `reserved` | lo reservado |
| `damaged` | lo dañado |
| `safety_stock` | un colchón contra la sobreventa, según el resumen leído |
| `quality_control` | lo que está en control de calidad |

`committed` no se puede ajustar por la API y sus cambios no disparan webhooks.

## La sobreventa crece con cada canal

Sobreventa es vender más unidades de las que hay disponibles. En la lectura de la base, el riesgo crece con cada canal que descuenta stock por su cuenta, porque cada uno vende contra una copia del número que puede estar atrasada; el stock de seguridad es una de las defensas. Cómo se reparte el stock entre la tienda online y un local está en [retiro en el local y stock compartido](../Venta-en-varios-canales/Local-fisico-con-caja/retiro-en-el-local-y-stock-compartido.md), y cómo lo sincroniza un sistema externo, en [integración con tiendas y marketplaces](Sistemas-de-gestion/integracion-con-tiendas-y-marketplaces.md).

> [!NOTE] Sin fuente todavía: cuánto tarda en sincronizarse el stock entre una tienda propia, un marketplace y las redes, y con qué frecuencia se sobrevende. No se encontró fuente primaria.

El recurso canónico del modelo de datos es la guía de inventario de Shopify y su objeto `ProductVariant`: fijarse en los estados del stock y en que lo apartado no se ajusta por la API. Es el modelo de una empresa, no un estándar.
