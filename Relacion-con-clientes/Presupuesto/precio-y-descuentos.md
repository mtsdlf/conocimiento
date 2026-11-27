---
resumen: >-
  El precio de cada renglón de un presupuesto sale de una lista de precios que el sistema elige según el cliente, la cantidad y la fecha, y que el vendedor puede corregir con un descuento por renglón o sobre el total. Cuando el descuento o el monto pasan un umbral, el documento necesita la aprobación de alguien con más autoridad.
estado: borrador
estabilidad: estable
fuentes:
  - "Odoo 17, Pricing (listas de precios, cantidad mínima, descuentos por renglón y globales): https://www.odoo.com/documentation/17.0/applications/sales/sales/products_prices/prices/pricing.html"
  - "ERPNext, Authorization Rule (aprobación por total o por porcentaje de descuento): https://docs.frappe.io/erpnext/user/manual/en/authorization-rule"
  - "Microsoft Dynamics 365 SCM, Sales agreements overview (precio de contrato que pisa la lista): https://learn.microsoft.com/en-au/dynamics365/supply-chain/sales-marketing/sales-agreements"
  - "APQC, Process Classification Framework 7.4, 3.5.3.9, 3.5.3.10 y 3.5.3.12: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Relacion-con-clientes/.investigacion/presupuesto-y-pedido.md (sección B)"
aliases: [lista de precios, pricelist, price list, descuento, discount, aprobación de descuento, discount approval, precio de venta]
creado: 2026-11-27
revisado:
---

# Precio y descuentos

El precio de cada renglón de un presupuesto sale de una lista de precios que el sistema elige según el cliente, la cantidad y la fecha, y que el vendedor puede corregir con un descuento por renglón o sobre el total. Cuando el descuento o el monto pasan un umbral, el documento necesita la aprobación de alguien con más autoridad.

Esta nota trata cómo se registra y se calcula el precio dentro del [presupuesto](presupuesto.md). Cuánto cobrar y cómo armar los planes es una decisión de [monetización](../../Producto/Monetizacion/monetizacion.md); cómo mostrarle el precio al cliente para que no sea lo único que mire está en [presentar el precio](../../Ventas/La-propuesta/presentar-el-precio.md); cuánto ceder cuando el cliente regatea, en [objeciones y negociación](../../Ventas/Objeciones-y-negociacion/objeciones-y-negociacion.md).

## De dónde sale el precio de un renglón

El precio no se escribe a mano en cada presupuesto: se busca. La empresa mantiene una o varias listas de precios, y cada lista puede tener reglas por período y por cantidad mínima. Un sistema abierto lo resuelve así: el cliente tiene asignada una lista en sus [condiciones comerciales](../Registro-del-cliente/condiciones-comerciales.md); al cargar el renglón, el sistema busca en esa lista la regla que coincide con el producto, la cantidad y la fecha; si ninguna coincide, usa la lista por defecto. Una regla puede decir, por ejemplo, que desde dos unidades rige otro precio.

La lista sugiere un precio, y el vendedor puede pisarlo en el renglón. Esa libertad es necesaria (hay casos que ninguna lista prevé) y es la puerta por la que el margen se escapa, por eso las aprobaciones de más abajo.

Un contrato con el cliente puede fijar precios propios que mandan sobre la lista. En un ERP de un proveedor grande, el acuerdo de venta con un cliente (ver [tipos de pedido](../Pedido-de-venta/tipos-de-pedido.md)) tiene precios y descuentos que pisan los de los acuerdos comerciales generales. Que el orden de búsqueda (contrato, lista del cliente, lista general) sea una decisión de diseño que el sistema tiene que dejar escrita es criterio de la base.

En la venta entre empresas, el precio es de la relación más que del producto: cada cliente, zona o canal tiene su lista, con descuentos por volumen y bultos cerrados. Ese caso está contado en [precio por cliente](../../Comercio-electronico/Comercio-B2B/precio-por-cliente.md).

## Descuentos por renglón y sobre el total

El descuento se registra por renglón, con un campo de porcentaje en el que un valor negativo sube el precio. Sobre eso, un sistema abierto ofrece tres maneras de aplicarlo al documento entero:

| Forma | Cómo se registra |
|---|---|
| En todos los renglones | El mismo porcentaje se carga en cada renglón |
| Descuento global | Se agrega al pedido un renglón con un producto de descuento |
| Monto fijo | Se descuenta un importe fijo |

Cuándo sirve cada una es criterio de la base: el porcentaje por renglón, para descuentos que dependen del producto; el aplicado a todos, para un descuento comercial al cliente; el global o el fijo, cuando no se quiere repartir.

La elección importa para lo que viene después. Un descuento repartido en los renglones deja cada renglón con su precio neto, y la factura y el margen por producto salen bien. Un renglón de descuento global es más fácil de leer para el cliente, pero obliga a prorratearlo si después se quiere saber cuánto dejó cada producto. Esto es criterio de la base.

También se decide qué ve el cliente: el precio ya descontado o el precio de lista con el descuento a la vista. Un sistema abierto deja elegir entre las dos políticas. Mostrar el descuento tiene sentido cuando es parte de lo que se ofrece; ocultarlo, cuando el precio de lista no le dice nada al cliente.

## Quién aprueba un descuento

APQC pone tres pasos antes de presentar un presupuesto: «Develop pricing and scheduling estimates» (3.5.3.9), «Conduct profitability analysis» (3.5.3.10) y «Manage internal approvals» (3.5.3.12). En un sistema abierto, la aprobación se arma con reglas que miran un dato del documento (el total neto, el total general con impuestos o el porcentaje de descuento) y, si pasa un umbral, exigen que lo confirme un rol determinado. Su ejemplo es sobre el pedido: un pedido de venta cuyo total general supera 1.000 lo tiene que confirmar el gerente de ventas.

Atar la misma regla al presupuesto es criterio de la base, y también lo que sigue. Atarla al presupuesto evita mandarle al cliente una oferta que después no se puede cumplir; atarla al pedido deja vender rápido y controla al final. La elección depende de cuánto cuesta retirar una oferta ya enviada.

> [!NOTE] Sin fuente todavía: el margen mínimo como regla del sistema (un piso de precio sobre el costo que bloquea el renglón). APQC nombra el análisis de rentabilidad, pero no se encontró cómo lo modelan los sistemas.

## Cómo falla

Los tres modos de falla son criterio de la base, sin una fuente que los mida.

- **El precio a mano se vuelve la regla.** Si cada vendedor pisa la lista, la lista deja de decir cuánto se cobra y el margen se pierde de a poco.
- **El precio cambia entre el presupuesto y el pedido.** Si la lista se actualiza mientras el presupuesto está vigente, hay que decidir cuál rige; está en [vigencia y aceptación](vigencia-y-aceptacion.md).
- **El impuesto se calcula sobre el precio equivocado.** El descuento tiene que restarse antes de calcular el impuesto del renglón. En la Argentina, además, la condición del cliente frente al IVA decide la clase de comprobante que se le va a emitir (ver [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md)).
