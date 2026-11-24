---
resumen: >-
  Integrar un sistema de gestión con una tienda online o un marketplace es copiar productos, precios, stock y pedidos de un lado al otro por sus APIs, con un sistema que manda en cada dato y el otro que lo refleja. Falla cuando el aviso de una venta se pierde o llega dos veces, cuando el permiso de acceso vence o cuando dos canales venden la misma unidad entre una copia y la siguiente.
estado: vigente
estabilidad: semi
fuentes:
  - "Tiendanube, API, autenticación: https://tiendanube.github.io/api-documentation/authentication (consultada el 2026-11-22, por extracto)"
  - "Tiendanube, API, introducción y límites: https://tiendanube.github.io/api-documentation/intro (consultada el 2026-11-22, por extracto)"
  - "Shopify, webhooks: https://shopify.dev/docs/apps/build/webhooks (consultada el 2026-11-22, por extracto)"
  - "Shopify, límites de llamadas: https://shopify.dev/docs/api/usage/rate-limits (consultada el 2026-11-22, por extracto)"
  - "Mercado Libre, developers, gestión de identidades y accesos (OAuth y tokens): https://developers.mercadolibre.com.ar/gestion-de-identidades-y-accesos-oauth-y-tokens (dio 403; por resumen del buscador)"
  - "Dux Software, ayuda, integrar y usar Mercado Libre: https://intercom.help/duxsoftware/es/articles/8931932-integrar-y-usar-mercado-libre-con-dux (consultada el 2026-11-22)"
  - "Dux Software, precios: https://www.duxsoftware.com.ar/precios (leída el 2026-11-22)"
  - "Contabilium, planes Argentina: https://contabilium.com/ar/planes (consultada el 2026-11-22)"
  - "Tiendanube, blog, Tango Factura, actualizado el 26/01/2026: https://www.tiendanube.com/blog/tango-factura/ (por extracto)"
  - "Comercio-electronico/.investigacion/sistemas-de-gestion.md"
  - "Comercio-electronico/.investigacion/resenas-de-sistemas-de-gestion.md"
  - "Comercio-electronico/.investigacion/contraria-gestion-y-local.md"
aliases: [integración ERP ecommerce, sincronización de stock, conector, middleware, integración con Mercado Libre, sync de stock, webhook, token de acceso]
creado: 2026-11-22
revisado: 2026-11-24
---

# Integración con tiendas y marketplaces

Integrar un sistema de gestión con una tienda online o un marketplace es copiar productos, precios, stock y pedidos de un lado al otro por sus APIs, con un sistema que manda en cada dato y el otro que lo refleja. Falla cuando el aviso de una venta se pierde o llega dos veces, cuando el permiso de acceso vence o cuando dos canales venden la misma unidad entre una copia y la siguiente.

Es lo que une al [sistema de gestión](sistemas-de-gestion.md) con los canales de [Venta en varios canales](../../Venta-en-varios-canales/venta-en-varios-canales.md). Sin integración, cada canal descuenta su propio stock y aparece la sobreventa que describe [catálogo y stock](../catalogo-y-stock.md). La misma mecánica usan las [apps para vendedores de marketplace](../../Plataforma-de-tiendas/apps-para-vendedores-de-marketplace.md), que conectan una tienda con Mercado Libre sin pasar por un sistema de gestión.

## Qué viaja y en qué sentido

| Dato | Sentido habitual | Por qué |
|---|---|---|
| Productos y precios | del sistema de gestión a los canales | el catálogo y las listas de precios se cargan una vez |
| Stock | del sistema de gestión a los canales | un solo número que todos reflejan |
| Pedidos | de los canales al sistema de gestión | cada venta se factura y descuenta del registro central |
| Comprobante | del sistema de gestión al canal o al comprador | la factura se emite donde está el registro fiscal |

La tabla es una lectura de la base sobre la documentación de los fabricantes; ninguna fuente leída lo describe en general. Un ejemplo concreto: la ayuda de un sistema argentino dice que el stock y los precios van del sistema hacia los canales, en un solo sentido (citado abajo). Otro sistema describe su conexión con una plataforma de tiendas como facturar las ventas en lote, sincronizar precios y stock, y pausar o activar publicaciones según el stock.

Las dos partes se reconocen por el SKU de cada [variante](../catalogo-y-stock.md): si el código no coincide, la venta llega al sistema sin producto o el stock no se actualiza.

## Cómo se entera cada lado

Hay dos maneras, y las integraciones serias usan las dos:

- **Aviso (webhook)**: el canal llama al sistema cuando pasa algo, como una venta nueva. Shopify advierte que «Webhook delivery isn't always guaranteed» y recomienda descartar los avisos repetidos por su identificador.
- **Consulta periódica**: el sistema pregunta cada tanto qué cambió. Shopify recomienda «reconciliation jobs» que vuelvan a leer los datos para cubrir los avisos perdidos.

Cada canal limita cuántas consultas acepta. En la API de Tiendanube el límite es un balde de 40 llamadas que se vacía a 2 por segundo, por tienda y por app, multiplicado por 10 en sus planes más altos. Un catálogo grande que se resincroniza entero choca contra ese límite.

## El permiso de acceso vence

Para leer y escribir en la cuenta del comercio, el sistema usa un token que el comercio autoriza una vez. Las plataformas lo manejan distinto:

| Canal | Qué dice su documentación | Calidad de lo leído |
|---|---|---|
| Tiendanube | «Our access tokens don't expire»: el token deja de valer solo si se pide otro o se desinstala la app | documentación oficial, por extracto |
| Mercado Libre | el token de acceso dura 6 horas (`expires_in: 21600`); se renueva con un token de renovación que es de un solo uso y exige el permiso `offline_access` | documentación oficial que dio 403; por resumen del buscador |

Del lado del comercio se ve así, en la ayuda de un sistema argentino: «Cada cierto tiempo, Mercado Libre requiere renovar el token de la integración», y la misma ayuda aclara que la sincronización de stock y precios «va siempre desde [el sistema] hacia tu tienda online» y «no funciona al revés».

Con un token que vence cada 6 horas y un token de renovación que se gasta al usarlo, dos procesos que renuevan a la vez dejan a uno con un token inválido y la cuenta desconectada. En la lectura de la base, eso explica una parte de los cortes de sincronización con Mercado Libre; un proveedor también los atribuye a la «inestabilidad de la interfaz de Mercado Libre». Cuánto dura el token de renovación no quedó claro: un resumen dice 6 meses y otra redacción de la misma documentación es ambigua.

## Cómo falla

1. **Sobreventa**: dos canales venden la última unidad entre dos sincronizaciones, o un aviso de venta se pierde.
2. **Pedidos duplicados**: el mismo aviso llega dos veces y el sistema crea dos pedidos.
3. **Publicaciones pausadas o desconectadas**: el token venció o el stock llegó a cero por un error de mapeo.
4. **Productos sin vincular**: el SKU de un canal no coincide con el del sistema.

Las reseñas de los usuarios argentinos, con su conteo por tema, están en [sistemas de gestión en Argentina](sistemas-de-gestion-en-argentina.md#lo-que-dicen-las-reseñas).

## Cuánto cuesta conectar

Los sistemas argentinos cobran la integración por cuenta de canal. Uno incluye de 1 a 5 tiendas o marketplaces según el plan; otro incluye de 3 a 5 cuentas y cobra cada cuenta extra de Mercado Libre o Tiendanube a $42.000 + IVA por mes y la de Shopify a $55.000 + IVA (precios al 2026-11-22, en la [ficha](sistemas-de-gestion-en-argentina.md)).

> [!NOTE] Sin fuente todavía: la documentación oficial de Mercado Libre sobre tokens, notificaciones y límites (dio 403), los reintentos de avisos de Tiendanube y WooCommerce, y una medición de cada cuánto sincronizan los conectores y con qué frecuencia sobrevenden.

El recurso canónico es la documentación de webhooks de Shopify: fijarse en la parte de entregas no garantizadas, duplicados y reconciliación, que vale para cualquier integración por avisos.
