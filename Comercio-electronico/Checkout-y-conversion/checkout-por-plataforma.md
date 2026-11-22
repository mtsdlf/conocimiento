---
resumen: >-
  Lo que dos plataformas de tiendas alojadas, Shopify y Tiendanube, dejan configurar del checkout al comercio y lo que fijan ellas, según su documentación pública. Consultado el 2026-11-22.
estado: borrador
estabilidad: volatil
fuentes:
  - "Shopify, Checkout (documentación para desarrolladores): https://shopify.dev/docs/apps/build/checkout (leído)"
  - "Tiendanube, centro de ayuda, cómo agregar códigos personalizados en el checkout: https://ayuda.tiendanube.com/es_AR/123367-opciones-del-checkout/como-agregar-codigos-personalizados-en-el-checkout-de-mi-tiendanube (según resultados del buscador, no se abrió)"
  - "Tiendanube, centro de ayuda, cómo agregar campos personalizados: https://ayuda.tiendanube.com/es_AR/123522-recursos-extra/como-agregar-campos-personalizados-para-que-mis-clientes-los-completen-en-mi-tiendanube (según resultados del buscador, no se abrió)"
  - "Comercio-electronico/.investigacion/checkout-y-conversion.md (sección 4)"
aliases: [personalización del checkout, checkout extensibility, opciones del checkout]
creado: 2026-11-22
revisado:
---

# Checkout por plataforma

Lo que dos plataformas de tiendas alojadas, Shopify y Tiendanube, dejan configurar del checkout al comercio y lo que fijan ellas, según su documentación pública. Consultado el 2026-11-22.

Es el dato detrás del reparto entre lo fijo y lo configurable que explica [Checkout y conversión](checkout-y-conversion.md#qué-fija-la-plataforma-y-qué-configura-el-comercio). El resto de los datos de cada plataforma está en sus fichas: [Shopify](../Plataforma-de-tiendas/shopify.md) y [Tiendanube](../Plataforma-de-tiendas/tiendanube.md). WooCommerce no se revisó.

| | Shopify | Tiendanube |
|---|---|---|
| Fuente y cuánto se leyó | [documentación para desarrolladores](https://shopify.dev/docs/apps/build/checkout), leída | centro de ayuda, solo resultados del buscador |
| Lo que configura el comercio sin código | marca (branding) por la Admin API | en "Configuración > Opciones del checkout": nota del cliente, pedir teléfono y documento, Factura A con CUIT y razón social, colores de marca, mensaje de confirmación |
| Lo que se extiende con código o apps | extensiones de interfaz: bloques en el editor de checkout, campos propios, validación del lado del cliente, autocompletar dirección, encabezado y pie. Functions: descuentos, ocultar medios de pago, renombrar opciones de entrega, bloquear el checkout si falla una regla | códigos personalizados, solo en el plan Evolución, que no permiten cambiar libremente campos, botones ni estructura; para más de dos campos propios, apps |
| Lo que fija la plataforma | `checkout.liquid` ya no se admite en los pasos de Información, Envío y Pago; la página no lista qué más queda bloqueado | no se personaliza con CSS ni HTML "porque es un proceso seguro"; la dirección de envío no se quita salvo en productos digitales |
| Diferencias por plan | lo único dicho son las fechas de retiro de los script tags: 28 de agosto de 2025 en Plus y 26 de agosto de 2026 en los otros planes | los códigos personalizados, solo en el plan Evolución |

Las páginas de ayuda de Tiendanube no coinciden entre sí sobre si hay campos propios nativos. De Shopify no se pudo confirmar la lista completa de lo que queda fijo.

En los dos casos, la cantidad de campos, el orden de los pasos y el diseño del checkout los fija la plataforma; el comercio ajusta campos extra, textos, marca y reglas. Es la lectura de estas dos fuentes, no una regla documentada para todas las plataformas.
