---
resumen: >-
  En la venta entre empresas el precio no es del producto sino de la relación: cada cliente, zona o canal tiene su lista, con descuentos por volumen, mínimos de compra y bultos cerrados. Es la primera cosa que el software de una tienda al público no resuelve y la que separa una capa mayorista de una tienda común.
estado: borrador
estabilidad: estable
fuentes:
  - "Shopify Help Center, B2B: https://help.shopify.com/en/manual/b2b (leído; proveedor con interés comercial)"
  - "Shopify Help Center, Quantity rules: https://help.shopify.com/en/manual/b2b/catalogs/quantity-rules (leído; proveedor)"
  - "Shopify App Store, Wholesale Pricing Discount, ficha y reseñas de 1 a 3 estrellas: https://apps.shopify.com/wholesale-pricing-discount (leído)"
  - "Compre Ahora, sitio: https://www.compreahora.com.ar (leído)"
  - "Comercio-electronico/.investigacion/b2b-rasgos-y-factura.md, b2b-software-global.md, b2b-software-argentina.md y b2b-marketplaces-y-region.md"
aliases: [lista de precios, listas de precios, precio mayorista, precios por cliente, customer-specific pricing, price lists, tiered pricing, precio por volumen, pedido mínimo, compra mínima]
creado: 2026-11-22
revisado:
---

# Precio por cliente

En la venta entre empresas el precio no es del producto sino de la relación: cada cliente, zona o canal tiene su lista, con descuentos por volumen, mínimos de compra y bultos cerrados. Es la primera cosa que el software de una tienda al público no resuelve y la que separa una capa mayorista de una tienda común.

Es uno de los rasgos del [comercio entre empresas](comercio-b2b.md). Va junto con la [cuenta corriente](cuenta-corriente-y-credito.md), porque el precio de una lista suele depender también del plazo de pago, y con el [pedido B2B](pedido-b2b.md), que es donde el precio se aplica.

## Las cuatro piezas del precio entre empresas

| Pieza | Qué es | Ejemplo |
|---|---|---|
| Lista de precios | Un juego de precios para un grupo de clientes: por canal (almacén, supermercado, revendedora), por zona o negociado con un cliente | la lista «mayorista zona sur» |
| Escala por volumen | El precio unitario baja al comprar más unidades en el mismo pedido | 10 cajas a un precio, 50 a otro |
| Mínimo de compra | Un monto o una cantidad debajo de la cual no se toma el pedido | pedido mínimo de un monto en pesos |
| Bulto cerrado o múltiplo | Se vende por caja, pack o pallet, no por unidad | de a 12 unidades |

La documentación de B2B de Shopify, un proveedor que vende esta función, da un vocabulario útil para cualquier software. El cliente B2B se carga como una empresa con sus sucursales, y a cada una se le personalizan «pricing, currency, products, payment and shipping methods». Las escalas dan «price breaks» al comprar cierta cantidad en el mismo pedido; las reglas de cantidad sirven para «restrict the number of items» por pedido. Lo central es que el precio cuelga del cliente: un mismo artículo tiene tantos precios como listas.

## Por qué el precio queda detrás del login

Si el precio depende de quién compra, el catálogo no puede mostrarlo hasta saber quién es. Por eso los portales y las capas mayoristas piden iniciar sesión, y un marketplace B2B argentino muestra los precios solo después del alta y «específicos de la zona de tu negocio» (su sitio, leído el 2026-11-22). Esto tiene un costo: el comercio que todavía no es cliente no puede comparar, y en las reseñas de esa app aparecen quejas de quienes no pudieron darse de alta porque su zona no tiene proveedor (detalle en [marketplaces y apps B2B de la región](marketplaces-y-apps-b2b-de-la-region.md)).

## Cómo falla

- **Las reglas reales son más complejas que las del software.** En las reseñas negativas de una app mayorista de Shopify, un comercio pide un descuento por volumen sobre productos distintos: «10 of a, 10 of b, 10 of c = lowered price because you got 30 total». La app no lo resolvía.
- **El precio mal aplicado en el checkout cuesta plata.** En la misma app, 5 de las 28 reseñas de 1 a 3 estrellas cuentan precios que no se aplicaron al pagar, con pérdidas; 9 hablan de fallas de precio o de clientes no reconocidos (codificación propia, detalle en [portales B2B globales](portales-b2b-globales.md)).
- **Los planes bajos limitan las listas.** Las plataformas de tienda que suman una capa mayorista ponen tope de listas o de catálogos en los planes chicos y lo liberan en los caros (valores en [portales B2B globales](portales-b2b-globales.md) y [software B2B en Argentina](software-b2b-en-argentina.md)).
- **Con inflación, la lista envejece rápido.** Que en Argentina las listas se actualicen seguido y que eso pese en la operación es inferencia: no se encontró una fuente que lo mida.

> [!NOTE]
> Sin fuente todavía: cuántas listas maneja en promedio un distribuidor pyme, cada cuánto las actualiza y cuánto pesa el descuento por pago al contado.
