---
resumen: >-
  El software para vender entre empresas viene en seis formas: la capa mayorista sobre una tienda al público, el portal B2B propio, la app de toma de pedidos para el vendedor en la calle, el sistema de gestión con módulo comercial, el marketplace B2B y la app que el fabricante le da al comercio. Se diferencian por quién es dueño del catálogo y del cliente, si sirven al vendedor que visita y si publican su precio.
estado: borrador
estabilidad: semi
fuentes:
  - "Shopify Enterprise, guía de plataformas B2B: https://www.shopify.com/enterprise/blog/b2b-ecommerce-platforms (leído con extractor; proveedor)"
  - "Salesforce, nota sobre el Magic Quadrant for Digital Commerce 2025 de Gartner: https://www.salesforce.com/news/stories/gartner-magic-quadrant-digital-commerce-2025/ (según el buscador)"
  - "Yo Facturo, sistema de preventa y autoventa: https://yo-facturo.com/blog/sistema-preventa-autoventa/ (leído; proveedor de software)"
  - "Las fichas de esta vertical y sus fuentes: portales-b2b-globales.md, software-b2b-en-argentina.md y marketplaces-y-apps-b2b-de-la-region.md"
  - "Comercio-electronico/.investigacion/b2b-software-global.md, b2b-software-argentina.md, b2b-marketplaces-y-region.md y b2b-posicion-contraria.md"
aliases: [software B2B, plataforma B2B, portal B2B, B2B ecommerce platform, capa mayorista, app de preventa, sistema de preventa, SFA, ERP comercial, marketplace B2B, tipos de software mayorista]
creado: 2026-11-22
revisado:
---

# Modelos de software B2B

El software para vender entre empresas viene en seis formas: la capa mayorista sobre una tienda al público, el portal B2B propio, la app de toma de pedidos para el vendedor en la calle, el sistema de gestión con módulo comercial, el marketplace B2B y la app que el fabricante le da al comercio. Se diferencian por quién es dueño del catálogo y del cliente, si sirven al vendedor que visita y si publican su precio.

Cada modelo resuelve una parte distinta de los rasgos del [comercio entre empresas](comercio-b2b.md): el [precio por cliente](precio-por-cliente.md), la [cuenta corriente](cuenta-corriente-y-credito.md), el [pedido](pedido-b2b.md), la [preventa](preventa-y-autoventa.md) y la [factura](factura-entre-empresas.md). Ninguno los cubre todos de fábrica. La clasificación es de esta base: según la nota de un proveedor evaluado, Gartner no hace un cuadrante aparte para el B2B y lo trata como una capacidad más de la plataforma de comercio digital (el original no se pudo abrir), y Shopify, un proveedor, separa las plataformas B2B solo por arquitectura («composable» o «all-in-one»).

## Las seis formas

| Modelo | Quién lo usa | Qué resuelve bien | Qué deja afuera | Cómo cobra |
|---|---|---|---|---|
| Capa mayorista sobre una tienda | la marca o el fabricante chico que ya vende al público y suma revendedores | listas y mínimos sobre el catálogo que ya tiene | el vendedor en la calle, la cuenta corriente, la factura con percepciones | incluido en un plan más caro, o una app de abono mensual |
| Portal B2B propio | el fabricante o distribuidor que quiere que sus clientes pidan solos | catálogo por cliente, repetición de pedidos, a veces app del vendedor | la factura y el stock, que siguen en el sistema de gestión | abono mensual por topes de productos, usuarios o pedidos |
| App de toma de pedidos (preventa) | el distribuidor con vendedores en la calle | ruta, cartera, pedido sin señal, cobranza | la venta sin vendedor; a veces la factura | por vendedor, o cotizado |
| Sistema de gestión con módulo comercial | la empresa que ya factura con él | precio, stock, cuenta corriente y factura en un solo lugar | la experiencia del cliente que pide solo | licencia o abono, casi siempre cotizado |
| Marketplace B2B | el comercio que busca proveedores, y el proveedor que busca clientes | juntar oferta de muchos proveedores | la relación propia con el cliente, que es del marketplace | no se encontró publicado; se supone comisión o margen |
| App del fabricante | el almacén o kiosco cliente de una marca grande | pedir a cualquier hora, promociones, puntos | la entrega, que sigue a cargo del distribuidor de la zona | gratis para el comercio; la paga el fabricante |

La tabla resume las fichas; las columnas de qué resuelve y qué deja afuera cada modelo son lectura de esta base.

El EDI, el intercambio de pedidos entre sistemas de empresas grandes, es anterior a todos y sigue siendo la mayor parte del comercio electrónico entre empresas medido ([cifras del comercio B2B](cifras-del-comercio-b2b.md)). Aquí queda afuera porque no lo usa el comercio chico; su historia está en [historia del comercio electrónico](../Fundamentos/historia-del-comercio-electronico.md).

## Tres ejes para ubicar una opción

1. **De quién es el catálogo y el cliente.** En la capa mayorista y el portal, del que vende. En el marketplace, el cliente es del marketplace. En la app del fabricante, la relación es de la marca, aunque entregue otro.
2. **Si sirve al vendedor que visita.** La capa mayorista de las tiendas al público no trae app para el vendedor; los portales con fuerza de ventas y los sistemas de preventa, sí, y varios anuncian que funcionan sin señal (fichas en [portales B2B globales](portales-b2b-globales.md)).
3. **Si publica su precio.** Las capas mayoristas y algunos portales publican precio. Las plataformas para empresas medianas y grandes y la mayoría de los sistemas de gestión locales se cotizan ([software B2B en Argentina](software-b2b-en-argentina.md)).

## Cómo se combinan y dónde se cortan

En la práctica, una distribuidora usa varias formas a la vez: el sistema de gestión factura y lleva la cuenta corriente, una app de preventa toma los pedidos en la calle y, a veces, un portal o un catálogo recibe los pedidos de los clientes que piden solos. Cuando esas piezas no están conectadas, alguien pasa los pedidos a mano. Un proveedor local de sistemas de gestión lo usa como argumento de venta: cuando el pedido «nace en el mismo sistema que factura», dice, «no hay doble carga ni errores de transcripción», y la autoventa «seria es offline-first» (es parte interesada).

En las reseñas leídas para esta vertical, las quejas más repetidas son que la app falla y que el soporte no resuelve. Detrás vienen las que aparecen cuando una pieza tiene que hablar con otra: el precio mayorista que no se aplica al pagar, la app del vendedor que no sincroniza, el pedido digital que el distribuidor de la zona no entrega. Leerlas como un problema de conexión entre piezas es interpretación de esta base; el conteo está en cada ficha.

## Fichas

- [Portales B2B globales](portales-b2b-globales.md): capas mayoristas, portales y plataformas con su precio publicado, y las reseñas negativas de dos capas mayoristas.
- [Software B2B en Argentina](software-b2b-en-argentina.md): la capa mayorista de las tiendas locales, los portales regionales, las apps de preventa y los sistemas de gestión, con precios y reseñas.
- [Marketplaces y apps B2B de la región](marketplaces-y-apps-b2b-de-la-region.md): las apps de los fabricantes, los marketplaces B2B y los que cerraron.
