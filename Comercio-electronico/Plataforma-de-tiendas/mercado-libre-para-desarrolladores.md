---
resumen: >-
  Lo que la API de Mercado Libre deja hacer a una app de terceros sobre la cuenta de un vendedor, y lo que sus términos para desarrolladores reservan: el uso permitido, la prohibición de competir, la definición de contenido, el rol sobre los datos personales y el programa de partners, consultado el 2026-11-22.
estado: borrador
estabilidad: volatil
fuentes:
  - "Mercado Libre, términos y condiciones para desarrolladores, copia de la Wayback Machine del 2025-06-17 de https://developers.mercadolibre.com.ar/es_ar/terminos-y-condiciones (la página viva dio 403 el 2026-11-22; B2)"
  - "Mercado Libre, documentación para desarrolladores: mensajes de posventa, motivos para comunicarse, User Products, notificaciones, límite de pedidos y preguntas: https://developers.mercadolibre.com.ar/es_ar/mensajes-post-venta, https://developers.mercadolibre.com.ar/motivos-para-comunicarse, https://developers.mercadolibre.com.ar/user-products, https://developers.mercadolibre.com.ar/productos-recibe-notificaciones/, https://developers.mercadolibre.com.ar/rate-limit-error-429 y https://developers.mercadolibre.com.ar/preguntas-y-respuestas (leídas a través de resúmenes del buscador, 2026-11-22; B3)"
  - "Mercado Libre, Developer Partner Program: https://developers.mercadolibre.com.ar/developer-partner-program (según el buscador; B4)"
  - "Mercado Libre, centro de partners, ficha de una app certificada: https://centrodepartners.mercadolibre.com.ar/apps/real-trends (lectura directa, 2026-11-22; A2)"
  - "Tiendanube, tienda de aplicaciones, Astroselling: https://www.tiendanube.com/tienda-aplicaciones-nube/astroselling (leída 2026-11-22; C3)"
aliases: [API de Mercado Libre, términos para desarrolladores de Mercado Libre, Developer Partner Program, User Products, mensajes de posventa]
creado: 2026-11-22
revisado:
---

# Mercado Libre para desarrolladores

Lo que la API de Mercado Libre deja hacer a una app de terceros sobre la cuenta de un vendedor, y lo que sus términos para desarrolladores reservan: el uso permitido, la prohibición de competir, la definición de contenido, el rol sobre los datos personales y el programa de partners, consultado el 2026-11-22.

Es la puerta de la que viven las [apps para vendedores de marketplace](apps-para-vendedores-de-marketplace.md), y el caso concreto de lo que [competencia con la plataforma](../../Producto/Plataformas/competencia-con-la-plataforma.md) explica en general: el dueño de la plataforma abre y se reserva el derecho de competir. El marketplace está en [Mercado Libre](mercado-libre.md), y los términos de su servicio de cobro, que dicen algo parecido, en [Mercado Pago](../Pagos/mercado-pago.md#lo-que-deja-hacer-a-terceros). El 2026-11-22 la documentación devolvió 403 a la lectura automática; la escala de calificación de cada fuente está en [fuentes públicas](../../Estrategia-competitiva/Analisis-de-competidores/fuentes-publicas.md#quién-lo-dice-y-si-está-confirmado).


## Lo que deja hacer la API

Una app de terceros puede operar la cuenta de un vendedor por la API: publicar y cambiar precio y stock, recibir las ventas, contestar preguntas y mandar mensajes de posventa. Lo prueban las apps que ya lo hacen: una multicanal publica el catálogo de una tienda en Mercado Libre y aplica «reglas de mark-up o mark-down» por canal, según su ficha. La documentación, leída por resúmenes del buscador (B3), pone estos límites:

| Qué hace una app | Lo que dice la documentación |
|---|---|
| Publicar y cambiar precio y stock | recurso `/items` y avisos cuando cambia una publicación o su precio. Con el modelo User Products, cada variación puede tener su precio: el integrador agrupa por «user product» y atiende los avisos de migración (página argentina actualizada el 28-jul-2026) |
| Recibir las ventas | aviso `orders_v2`; la app contesta en 20 segundos o se reintenta |
| Contestar preguntas | `/questions/search` y `/answers`; las preguntas sin contestar de más de 7 meses se borran |
| Mensajes de posventa | hasta 350 caracteres; para iniciar la conversación hay motivos fijos (pedir variante, datos de facturación, mandar la factura, promesa de entrega), algunos con plantillas que el vendedor no edita y con topes por motivo |
| Volumen | límites por recurso, con error 429; la búsqueda de órdenes, 100 pedidos por minuto |

## El programa de partners

Mercado Libre tiene un programa de partners con medallas Silver, Gold y Platinum y plazos de entrega exigidos a las apps, que se pierden si no se cumplen, según el buscador (B4). Si es obligatorio para publicar por la API no se leyó. Al menos una app de gestión figura en su centro de partners con `certification_level: platinum`; lo que exige ese nivel tampoco se leyó.

## Lo que reservan los términos

Los términos para desarrolladores se leyeron en una copia de la Wayback Machine del 2025-06-17 (B2: oficial, pero de 17 meses antes; puede haber cambiado). Citas literales:

| Cláusula | Qué dice |
|---|---|
| 1, definición | «El Contenido de Mercado Libre no incluye la información obtenida por los Desarrolladores con independencia de Mercado Libre y de la API.» |
| 2.2.1, licencia | «limitada, no exclusiva, personal, revocable…», «únicamente a los fines enumerados»; el primero, «Facilitar, mejorar y/o potenciar el uso y las funcionalidades del Sitio y de los servicios prestados por Mercado Libre» |
| Competencia | «Mercado Libre podrá desarrollar productos, servicios o aplicaciones que puedan competir con las Aplicaciones» |
| Llamadas y certificación | puede «limitar discrecionalmente la cantidad de llamadas» y cobrar o cortar el acceso por exceso; puede exigir certificación y revocarla «a su exclusivo criterio» |
| 6, datos personales | el desarrollador es «Encargado de Tratamiento» y trata los datos «exclusivamente para cumplir con las finalidades» de los términos |
| 7.2, 7.4 y 7.9 | no publicar el Contenido de Mercado Libre fuera de la aplicación, ni usarlo, ni usar la aplicación, para «desarrollar productos y/o servicios que compitan con los de Mercado Libre» |
| Cambios | puede modificar en cualquier momento la API, las llamadas permitidas y los beneficios |

## De dónde sale el dato

La lectura de esta base, que no está en los términos: lo que decide qué se puede hacer con un dato es de dónde sale. Un catálogo que el comercio carga en otro sistema y publica en Mercado Libre es suyo y puede ir a cualquier canal. Un catálogo importado desde Mercado Libre para llevarlo a otro canal es contenido de Mercado Libre usado fuera de él, una zona gris que hoy toleran las apps multicanal y que el marketplace decide. Los compradores del marketplace no se pueden usar para vender afuera.

> [!NOTE] Sin fuente todavía: la versión vigente de los términos para desarrolladores; los Términos y Condiciones Generales para vendedores, donde suele estar la regla sobre desviar compradores fuera del sitio; la guía oficial para publicar por `/items`; y si los mensajes restringen datos de contacto o enlaces externos.

