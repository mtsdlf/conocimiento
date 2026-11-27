---
resumen: >-
  Las condiciones del proveedor son los términos con que vende: precio, plazo de entrega, cantidad mínima y condición de pago, casi siempre distintos para cada artículo. Se guardan en el registro artículo-proveedor, que dice qué artículo se le compra a quién, con qué código y en qué condiciones, y que la orden de compra trae sola.
estado: vigente
estabilidad: semi
fuentes:
  - "Odoo 17, Requests for quotation y Lead times (según su resumen; como evidencia de práctica): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/purchase/manage_deals/rfq.html ; https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/lead_times.html"
  - "ERPNext, Supplier y Supplier Group (según su resumen; como evidencia de práctica): https://docs.frappe.io/erpnext/supplier ; https://docs.frappe.io/erpnext/supplier-group"
  - "SAP, Underdeliveries, Overdeliveries, and Final Deliveries (4.6C) y SAP Learning, Applying Tolerances (según su resumen; como evidencia de práctica): https://help.sap.com/saphelp_46c/helpdata/en/a5/63343943a211d189410000e829fbbd/content.htm ; https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/applying-tolerances-and-the-delivery-completed-indicator"
  - "ERPNext, Purchase Order y Purchase Receipt (según su resumen; como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/purchase-order ; https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt"
  - "International Trade Administration, Know your Incoterms (describe el texto de la ICC; leído): https://trade.gov/know-your-incoterms"
  - "ICC, Incoterms 2020 (leído por extracto; no dice qué excluyen): https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/"
  - "Compras-y-abastecimiento/.investigacion/proveedores.md (2026-11-27), sección 3"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), sección 7"
aliases: [condiciones de compra, lista de precios del proveedor, precio de compra, registro artículo-proveedor, artículo-proveedor, info record, purchasing info record, supplier price list, vendor price list, plazo de entrega, lead time, cantidad mínima, mínimo de compra, minimum order quantity, MOQ, condición de pago, payment terms, Incoterms]
creado: 2026-11-27
revisado: 2026-11-27
---

# Condiciones del proveedor

Las condiciones del proveedor son los términos con que vende: precio, plazo de entrega, cantidad mínima y condición de pago, casi siempre distintos para cada artículo. Se guardan en el registro artículo-proveedor, que dice qué artículo se le compra a quién, con qué código y en qué condiciones, y que la orden de compra trae sola.

Son la parte del registro de [Proveedores](proveedores.md) que lee cada compra. Las fija una negociación o un acuerdo de [Abastecimiento estratégico](../Abastecimiento-estrategico/abastecimiento-estrategico.md), y las lee cada [orden de compra](../Orden-de-compra/orden-de-compra.md) para no volver a escribirlas. Es el espejo de las [condiciones comerciales](../../Relacion-con-clientes/Registro-del-cliente/condiciones-comerciales.md) del cliente.

## El registro artículo-proveedor

Un mismo artículo se le puede comprar a varios proveedores, y cada uno lo vende a su precio, con su código y en su plazo. Por eso, como lectura de esta base, las condiciones no caben ni en la ficha del artículo ni en la del proveedor: van en un registro que cruza los dos. Como evidencia de práctica, la documentación de un sistema abierto permite fijar el proveedor y su precio en la ficha del artículo, para que se rellenen solos en cada pedido de cotización, y cargar listas de precios enteras de una vez.

Las columnas que ese sistema trae por defecto en un renglón de pedido de cotización dicen qué hay en el registro: cantidad, precio unitario y plazo de entrega. Se pueden sumar el código que el proveedor le da al artículo y el descuento. Las tolerancias de recepción también pueden fijarse en este registro; de dónde manda cada una está en [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md).

| Condición | Qué dice | Quién la usa |
|---|---|---|
| Precio | Cuánto cuesta cada unidad, a veces por tramo de cantidad o con descuento | La orden de compra y el cruce de la factura |
| Código del proveedor | Cómo llama el proveedor al artículo | La orden que se le manda, para que la entienda |
| Plazo de entrega | Cuántos días pasan entre la orden y la entrega | La [fecha esperada](../Seguimiento-de-la-orden/confirmacion-y-seguimiento.md) y el [punto de pedido](../../Inventario-y-depositos/Reposicion/punto-de-pedido.md) |
| Cantidad mínima | Lo mínimo que acepta vender | La cantidad de la orden |
| Tolerancia | Cuánto de más o de menos se acepta al recibir | La [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md) |
| Condición de pago | Cuándo se le paga | La cuenta a pagar |

## Plazo de entrega: de él sale la fecha esperada

Como criterio de la base, el plazo de entrega es la condición que más se usa fuera de Compras. En el sistema abierto citado, la fecha esperada de una orden es la fecha en que se confirma más el plazo del proveedor. Es una de las tres fechas de la orden, junto con la fecha requerida (la que pide quien compra) y la fecha confirmada (la que promete el proveedor); las define la [confirmación y el seguimiento](../Seguimiento-de-la-orden/confirmacion-y-seguimiento.md), y contra ellas se mide al proveedor en la [evaluación](evaluacion-de-proveedores.md).

Inventario usa el mismo número para otra cosa: el [punto de pedido](../../Inventario-y-depositos/Reposicion/punto-de-pedido.md) es la demanda esperada durante el plazo de entrega más un stock de seguridad. Como criterio de la base, si el plazo cargado es más corto que el real, el punto de pedido queda bajo y la empresa se queda sin stock aunque la política esté bien calculada.

## Cantidad mínima, unidad de compra y precio por cantidad

El proveedor suele vender con un mínimo, en un múltiplo o en una unidad distinta de la que usa el depósito. Un hilo de un foro de usuarios de un sistema abierto, sin fuente oficial, dice que la lista de precios se elige según si la cantidad pedida alcanza el mínimo y si la lista sigue vigente. El sobrepedido, que deja a la orden superar a la solicitud por embalaje o por mínimos del proveedor, está en [solicitud de compra](../Orden-de-compra/solicitud-de-compra.md).

La unidad de compra se define acá y importa al recibir: la documentación de recepciones de ese sistema, según su resumen, aconseja revisar la unidad de compra y su conversión antes de tocar la tolerancia cuando lo recibido supera lo pedido.

> [!NOTE] Sin fuente todavía: cómo se modelan la unidad de compra y su conversión, el múltiplo de compra y el descuento por pronto pago; la única fuente sobre el mínimo es un foro de usuarios.

## Condición de pago: se negocia acá y se paga en Tesorería

La condición de pago dice cuántos días después de la factura, o en qué cuotas, se le paga al proveedor. En el sistema abierto citado es una plantilla que se asigna al proveedor, y sigue la misma prioridad que el resto del registro: la del proveedor gana sobre la de su grupo, y la del grupo sobre la de la empresa. Se negocia en Compras; la deuda la registra Contabilidad: al recibir, como recibido sin facturar, y se confirma con la factura ([compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md)). El pago es de Tesorería, en [pagos a proveedores](../../Tesoreria/Pagos-a-proveedores/pagos-a-proveedores.md).

En la Argentina, la factura de crédito electrónica le pone un plazo legal a la aceptación de la factura; está en [Compras y abastecimiento en la Argentina](../compras-y-abastecimiento-en-argentina.md).

## Incoterms: quién paga el flete y quién corre el riesgo

Cuando la compra viaja, el registro guarda también la regla de entrega. Según una página del gobierno de Estados Unidos que describe el texto de la Cámara de Comercio Internacional, los Incoterms (11 reglas, edición 2020) definen las tareas, los costos y el traspaso del riesgo de pérdida o daño entre vendedor y comprador. No dicen el método ni el momento del pago, ni cuándo pasa la propiedad de la mercadería. Esas exclusiones salen de esa página; la de la ICC las deja sin decir. Las reglas una por una están en [Incoterms](../../Cadena-de-suministro-y-logistica/Comercio-exterior/incoterms.md), y la importación como operación (aduana, despachante, flete internacional), en [Comercio exterior](../../Cadena-de-suministro-y-logistica/Comercio-exterior/comercio-exterior.md), de Cadena de suministro y logística.

## Dónde vive cada condición

Una misma condición puede estar en varios lugares, y hace falta una regla de cuál gana. El sistema abierto citado usa proveedor, grupo y empresa para la condición de pago, y la tolerancia tiene su propia regla en [recepción contra lo pedido](../Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md). Como criterio de la base, la regla general es que lo más particular gana: la orden sobre el [contrato marco](../Abastecimiento-estrategico/contrato-marco.md), el contrato sobre el registro artículo-proveedor, y este sobre el proveedor y su grupo. También como criterio de la base, lo que se trae al documento es un valor inicial que el comprador puede cambiar, y el cambio queda en la orden, no en el registro.
