---
resumen: >-
  Una plataforma de tiendas alojada corre una sola instalación que sirve a muchas tiendas, y se abre a terceros por cuatro puertas: los temas, la tienda de apps, las APIs y los webhooks. Quien construye encima trabaja dentro de límites de uso por tienda y tiene que seguir el calendario de versiones de la API.
estado: vigente
estabilidad: estable
fuentes:
  - "Shopify Engineering, MySQL database shard balancing at terabyte scale: https://shopify.engineering/mysql-database-shard-balancing-terabyte-scale (leída a través de un resumen de la página)"
  - "Weingarten, charla en SREcon16 Europe: https://usenix.org/conference/srecon16europe/program/presentation/weingarten (solo abstract)"
  - "Shopify, API versioning: https://shopify.dev/docs/api/usage/versioning (leída, consultada el 2026-11-22)"
  - "Shopify, Liquid: https://shopify.dev/docs/api/liquid (leída)"
  - "Shopify, documentación de APIs: https://shopify.dev/docs/api/storefront (según resumen del buscador)"
  - "Tiendanube, API documentation, introducción: https://tiendanube.github.io/api-documentation/intro (leída, consultada el 2026-11-22)"
  - "Adobe, Commerce developer: https://developer.adobe.com/commerce/ (leída)"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md (sección 2)"
  - "Comercio-electronico/.investigacion/huecos-plataformas.md (sección 3)"
  - "Comercio-electronico/.investigacion/vistazo.md (sección 2)"
aliases: [arquitectura de una plataforma de e-commerce, pods, pod, temas, themes, Liquid, tienda de apps, app store, API, webhooks, rate limit, límite de tasa, versionado de API]
creado: 2026-11-22
revisado: 2026-11-22
---

# Arquitectura de una plataforma de tiendas

Una plataforma de tiendas alojada corre una sola instalación que sirve a muchas tiendas, y se abre a terceros por cuatro puertas: los temas, la tienda de apps, las APIs y los webhooks. Quien construye encima trabaja dentro de límites de uso por tienda y tiene que seguir el calendario de versiones de la API.

La arquitectura explica por qué una plataforma alojada puede cobrar poco por tienda: el costo de operar se reparte entre todas. También fija qué puede hacer un tercero, y por eso es la base de las [apps para comerciantes](apps-para-comerciantes.md). Vale para el tipo alojado de [tipos de plataforma](tipos-de-plataforma.md); en una autoalojada, cada comercio corre su propia instalación.

## Una instalación para muchas tiendas: los pods de Shopify

Servir a muchos clientes desde una misma instancia, con los datos de cada uno aislados, es [multi-tenancy](../../Arquitectura/Sistemas-distribuidos/multi-tenancy.md). Esa nota explica cuánto se comparte entre clientes y los modelos de aislamiento. El caso de una plataforma de tiendas lo documenta Shopify en su blog de ingeniería.

Shopify reparte las tiendas en pods. Su definición: "A pod is an isolated instance of Shopify consisting of an individual MySQL database shard". Y agrega: "Every pod houses a unique subset of shops on the platform." Según un resumen de la misma página, cada pod es un stack completo, con su shard de MySQL más Redis y Memcached.

El ruteo funciona así, según ese resumen:

1. Llega una request para una tienda.
2. Una capa de entrada consulta una tabla de ruteo y averigua en qué pod están los datos de esa tienda. La clave que reparte las tiendas entre shards es `shop_id`.
3. La request va a ese pod, que la atiende sin tocar a los demás.

El aislamiento protege a las tiendas entre sí: "two high-traffic merchants are isolated at the pod level". Si una tienda recibe un pico de tráfico, el daño queda dentro de su pod. Mover una tienda de pod es copiar todas sus filas a otro shard, y Shopify rebalancea las tiendas entre pods para equilibrar la carga de las bases.

En los términos de multi-tenancy, el pod es un punto intermedio: adentro, muchas tiendas comparten la base; entre pods, están separadas. Esto es lectura de esta base, no de Shopify. La historia viene de antes: una charla de Weingarten en SREcon 2016, según su abstract, ubica a la plataforma entre "share nothing" y "share everything", con el aislamiento de bases en 2013 y 2014 y los pods en varios centros de datos en 2016.

## Temas: el diseño de la vitrina

Un tema es un diseño intercambiable de la vitrina. El comercio elige uno, lo ajusta y puede cambiarlo sin tocar catálogo ni pedidos. En Shopify, los temas se escriben en Liquid: "Liquid is a template language created by Shopify". Los temas usan una variante que "extends the open-source version of Liquid for use with Shopify themes".

Cuánto del tema puede tocar el comercio depende de la plataforma y a veces del plan. En [Tiendanube](tiendanube.md), el acceso al código del tema aparece en la lista de lo que suma un plan intermedio.

> [!NOTE] Sin fuente todavía: cómo funcionan los temas de Tiendanube (lenguaje y estructura); la documentación leída no los cubre.

## La tienda de apps y la instalación de una app

La tienda de apps es el catálogo de extensiones de terceros que el comercio instala en su tienda. La documentación de Tiendanube muestra el circuito que recorre un desarrollador:

1. Se registra como partner y crea la app en el panel de partners.
2. El comercio instala la app. La plataforma sigue OAuth 2 ("We follow the OAuth 2 framework") y le entrega a la app un token para esa tienda.
3. La app manda el token en cada request, más un encabezado `User-Agent` con su nombre y un contacto. Sin ese encabezado, la API responde 400.

El token es por tienda: cada comercio que instala la app le abre solo sus propios datos. Qué tipos de apps hay, cómo cobran y qué parte se queda la plataforma está en [apps para comerciantes](apps-para-comerciantes.md).

## APIs y webhooks: leer, escribir y enterarse

Una API deja que otro sistema lea y escriba datos de la tienda; un webhook es el aviso que la plataforma manda a otro sistema cuando pasa algo, como un pedido nuevo. Con la API, la app pregunta; con el webhook, la plataforma avisa sin que nadie pregunte.

Las plataformas grandes separan las APIs por uso. Según un resumen de la documentación de Shopify, la Admin API, en GraphQL, maneja productos, clientes, pedidos e inventario, y su versión REST figura como legacy. La Storefront API es solo GraphQL, y Hydrogen, un framework de React, la usa para armar vitrinas a medida: es la puerta del modo headless. Adobe presenta su producto como "API-first Commerce".

En Tiendanube, toda URL lleva la versión y la tienda en la ruta: "All URLs start with `https://api.tiendanube.com/2025-03/{store_id}`". Una app puede suscribirse a los webhooks `app/suspended` y `app/resumed`, que avisan cuando la plataforma le corta o le devuelve el acceso por falta de pago. Mientras está suspendida no recibe webhooks, y esos eventos no se disparan al terminar una prueba gratis. La lista completa de eventos no se leyó.

## Límites de uso: el balde de Tiendanube

Una plataforma limita cuántas requests puede hacer una app, para que ninguna sature la instalación compartida. Tiendanube usa un balde con goteo (leaky bucket): "the default bucket size is of 40 requests with a leaky rate of 2 requests per second". Consultado el 2026-11-22.

En la práctica, una app puede hacer una ráfaga de hasta 40 requests, y después el balde se vacía a 2 por segundo. Si se pasa, la API responde 429. El límite es por tienda y por app, y las tiendas de los planes más altos tienen un límite diez veces mayor. Así, la plataforma segmenta también por capacidad técnica, no solo por funciones (ver [segmentos de comerciantes](segmentos-de-comerciantes.md)).

## Versionado: el calendario que sigue quien construye encima

Las APIs cambian, y la plataforma fija cada cuánto y con cuánto aviso. Shopify: "Shopify releases a new API version every three months at 5pm UTC on the first day of the quarter." Las versiones llevan el nombre de su fecha, como 2026-04. "Each stable version is supported for a minimum of 12 months", con "at least nine months of overlap" entre versiones.

La consecuencia, en lectura de esta base: un desarrollador de apps tiene que migrar al menos una vez por año, o su app deja de funcionar cuando su versión sale de soporte. Tiendanube también pone la versión en la ruta, pero la política de soporte no se leyó.

## Cómo se usa al analizar plataformas de tiendas

La documentación para desarrolladores es pública y dice cuánto deja hacer una plataforma, algo que el sitio comercial no cuenta. Al comparar dos con el método de [desarme de producto](../../Estrategia-competitiva/Analisis-de-competidores/desarme-de-producto.md), conviene mirar:

1. Qué APIs ofrece y en qué estado (GraphQL, REST, legacy), y si hay una API de vitrina para headless.
2. Los límites de uso y si cambian por plan: dicen qué tamaño de comercio espera.
3. La cadencia de versiones y cuánto dura cada una: es el costo de mantenimiento que la plataforma le pone a sus desarrolladores.
4. Qué eventos manda por webhook: sin ellos, una app tiene que consultar una y otra vez.

Para un SaaS que piensa vivir dentro de una plataforma, esto es parte del costo de entrada, junto con el riesgo de que la plataforma copie la función, que está en [competencia con la plataforma](../../Producto/Plataformas/competencia-con-la-plataforma.md).

Los recursos canónicos son las fuentes primarias:

- La entrada de shard balancing del blog de ingeniería de Shopify: fijarse en la definición de pod, la clave `shop_id` y la tabla de ruteo.
- La página de versionado de shopify.dev: la tabla de versiones y la política de deprecación, para ver cuántos meses hay para migrar.
- La introducción de la API de Tiendanube: OAuth por tienda, el balde de 40 requests y el límite diez veces mayor en los planes altos.
- La charla de Weingarten en SREcon16 es la fuente más temprana del aislamiento; vale el video o las diapositivas, no solo el abstract.
