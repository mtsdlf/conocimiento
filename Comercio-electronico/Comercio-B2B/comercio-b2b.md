---
resumen: >-
  El comercio B2B es la venta entre empresas: el fabricante, el distribuidor o el mayorista que le vende a otros comercios. Se distingue de la tienda al público en que el precio depende del cliente, se vende a plazo, los pedidos se repiten sobre catálogos grandes, un vendedor suele visitar al cliente y, en Argentina, la factura discrimina impuestos y puede volverse un título de cobro.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Introduction to Business 2e, 12.2 Wholesaling: https://openstax.org/books/introduction-business-2e/pages/12-2-wholesaling (leído)"
  - "Shopify Help Center, B2B: https://help.shopify.com/en/manual/b2b (leído; proveedor)"
  - "UNCTAD, Global e-commerce hits $25.6 trillion: https://unctad.org/news/global-e-commerce-hits-256-trillion-latest-unctad-estimates (leído)"
  - "CEP XXI, empleadores del sector privado por CLAE: https://cdn.produccion.gob.ar/cdn-cep/datos-por-actividad/empleadoras/empleadoras_privadas_por_clae3.csv (descargado y sumado)"
  - "Comercio-electronico/.investigacion/b2b-rasgos-y-factura.md, b2b-cadena-y-preventa.md, b2b-cifras.md, b2b-conteo-propio.md, b2b-software-global.md, b2b-software-argentina.md, b2b-marketplaces-y-region.md y b2b-posicion-contraria.md (2026-11-22)"
aliases: [B2B, comercio entre empresas, business to business, venta mayorista, comercio mayorista, distribución, wholesale, B2B e-commerce, comercio electrónico B2B]
creado: 2026-11-22
revisado:
---

# Comercio B2B

El comercio B2B es la venta entre empresas: el fabricante, el distribuidor o el mayorista que le vende a otros comercios. Se distingue de la tienda al público en que el precio depende del cliente, se vende a plazo, los pedidos se repiten sobre catálogos grandes, un vendedor suele visitar al cliente y, en Argentina, la factura discrimina impuestos y puede volverse un título de cobro.

Es una de las partes de [comercio electrónico](../comercio-electronico.md), aunque buena parte del comercio entre empresas todavía no pasa por un medio digital. Esta vertical trata la operación de venderle a otro comercio. Cómo se le hace publicidad a una empresa está en [marketing B2B](../../Marketing/Canales/marketing-b2b.md), y cómo se cierra una venta compleja con varios decisores, en [Ventas](../../Ventas/ventas.md). La compra de reposición de un almacén no se parece a esa venta compleja: el grupo de compra que describen las encuestas de Gartner es de compras grandes y no hay fuente sobre quién decide en un comercio chico.

## Qué la separa de una tienda al público

Cinco rasgos aparecen en todas las fuentes de esta vertical, y cada uno tiene su nota:

| Rasgo | En una tienda al público | Entre empresas | Nota |
|---|---|---|---|
| Precio | uno para todos | una lista por cliente, zona o canal, con escalas y mínimos | [precio por cliente](precio-por-cliente.md) |
| Pago | al confirmar, por un tercero | a plazo, con saldo, límite y cobranza | [cuenta corriente y crédito](cuenta-corriente-y-credito.md) |
| Pedido | ocasional, pocos productos | reposición repetida, muchos renglones, por varios caminos | [pedido B2B](pedido-b2b.md) |
| Quién vende | la tienda, sola | muchas veces un vendedor que visita con una ruta | [preventa y autoventa](preventa-y-autoventa.md) |
| Comprobante | factura al consumidor | factura con IVA discriminado, percepciones y, a veces, factura de crédito | [factura entre empresas](factura-entre-empresas.md) |

Los cinco se cruzan: el precio de la lista puede cambiar con el plazo; el vendedor que toma el pedido puede ser también quien cobra; la factura decide el precio final. Por eso el software de una tienda al público, que resuelve uno a la vez, se queda corto (ver más abajo).

## La cadena en la que vive

El comercio B2B ocurre a lo largo de la [cadena de distribución](cadena-de-distribucion.md): el fabricante le vende al distribuidor o al mayorista, y estos al comercio que vende al público. Cada eslabón vive de funciones como fraccionar, transportar y fiar, y cuando uno se saltea, otro las absorbe.

En Argentina, en octubre de 2023 había 34.525 empresas mayoristas con empleados registrados, 53.284 industriales y 109.418 minoristas, según los datos del CEP XXI sumados por esta base. Quedan afuera los mayoristas sin empleados registrados y los fabricantes que venden directo, que cuentan como industria. El canal tradicional de consumo masivo (almacenes, kioscos y autoservicios independientes) pesa alrededor de un tercio de las ventas, según NielsenIQ. Todas las cifras, con su fuente y su calificación, están en [cifras del comercio B2B](cifras-del-comercio-b2b.md).

## El software, por partes

Seis formas de software se reparten estos rasgos, y ninguna los cubre todos de fábrica: la capa mayorista sobre una tienda, el portal B2B propio, la app de toma de pedidos para el vendedor, el sistema de gestión con módulo comercial, el marketplace B2B y la app que el fabricante le da al comercio ([modelos de software B2B](modelos-de-software-b2b.md)). En la práctica, una distribuidora combina varias. En las reseñas leídas para esta vertical, las quejas más repetidas son que la app falla y que el soporte no resuelve; detrás vienen el precio mayorista que no se aplica al pagar, la app del vendedor que no sincroniza y el pedido digital que el distribuidor de la zona no entrega.

Las que publican precio son las capas mayoristas, algunos portales y los sistemas de gestión locales; lo que trabaja con empresas medianas y grandes se cotiza. Los datos de cada uno, fechados, están en tres fichas:

- [Portales B2B globales](portales-b2b-globales.md): capas mayoristas, portales y plataformas con precio y límites, y las reseñas de dos capas mayoristas.
- [Software B2B en Argentina](software-b2b-en-argentina.md): la capa mayorista de las tiendas locales, los sistemas de gestión con su precio en pesos y las apps de preventa, con 94 reseñas codificadas.
- [Marketplaces y apps B2B de la región](marketplaces-y-apps-b2b-de-la-region.md): las apps de los fabricantes para el almacén, los marketplaces B2B y los que cerraron, con las reseñas de tres apps.

## Lo que se suele afirmar y no está probado

- **«El B2B online es mucho más grande que el B2C.»** Es cierto con las cifras de UNCTAD (83% del comercio electrónico de 2018), pero esas cifras incluyen el EDI entre sistemas de empresas grandes. No dicen cuánto vende una pyme por una web. Una columna que dice «seis veces» no cita fuente.
- **«Los comercios quieren pedir por app.»** El único estudio con muestra de la región (Perú, 2026) dice que solo el 12% de los bodegueros tiene a las apps de los fabricantes como destino principal, y que las usan por las promociones más que por comodidad. Las plataformas de abastecimiento que compraban y repartían por su cuenta se achicaron o cerraron.
- **«El vendedor en la calle desaparece.»** Ninguna fuente lo muestra. Los fabricantes presentan sus apps como complemento del vendedor, y el comercio de cercanía creció en 2025.

Estas tres disputas se desarrollan en [pedido B2B](pedido-b2b.md), [preventa y autoventa](preventa-y-autoventa.md) y [cifras del comercio B2B](cifras-del-comercio-b2b.md).

## Por dónde empezar a analizar un mercado mayorista

Si tenés que analizar un mercado de distribuidoras, mayoristas o fabricantes que venden a comercios:

1. [Cifras del comercio B2B](cifras-del-comercio-b2b.md), para el tamaño en Argentina por rubro y por tamaño de empresa.
2. [Cadena de distribución](cadena-de-distribucion.md), para ubicar el eslabón y el canal.
3. Los rasgos que importan en ese eslabón: [preventa y autoventa](preventa-y-autoventa.md) y [cuenta corriente y crédito](cuenta-corriente-y-credito.md) para una distribuidora; [precio por cliente](precio-por-cliente.md) y [pedido B2B](pedido-b2b.md) para quien suma clientes que piden solos.
4. [Modelos de software B2B](modelos-de-software-b2b.md) y sus fichas, para saber quién lo atiende, cuánto cobra y de qué se quejan sus usuarios.
5. [Factura entre empresas](factura-entre-empresas.md), para lo que cambia el precio final en Argentina.

Cómo se arma el análisis en sí está en el [recorrido de un análisis de competencia](../../Estrategia-competitiva/Fundamentos/recorrido-analisis-de-competencia.md).

## Lo que falta medir

Varias preguntas no tienen todavía respuesta pública: cómo piden los comercios argentinos a sus proveedores, cuánto del pedido pasa por chat o planilla, cuánto paga una distribuidora pyme por su software y cuánto pagaría, cuánto cuesta una visita del vendedor y cuántas distribuidoras hay en cada rubro. Cada nota declara las suyas al final.
