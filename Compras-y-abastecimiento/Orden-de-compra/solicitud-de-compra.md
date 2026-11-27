---
resumen: >-
  La solicitud de compra es el pedido interno con el que un área dice qué necesita, cuánto y para cuándo, antes de que alguien le pida precios a un proveedor. Sirve de autorización previa: la compra sale con el consentimiento de quien responde por el gasto y con presupuesto disponible, y lo que se compra sin pasar por ella es compra fuera del circuito.
estado: vigente
estabilidad: semi
fuentes:
  - "Wikipedia, Purchase requisition (según su resumen): https://en.wikipedia.org/wiki/Purchase_requisition"
  - "ERPNext, Material Request (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/material-request"
  - "ERPNext, Purchase Order, porcentaje de sobrepedido (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/purchase-order"
  - "Microsoft, Dynamics 365 Supply Chain Management, Purchase agreements: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements"
  - "GAO, Governmentwide Purchase Cards, GAO-08-333 (marzo de 2008; leído por extracto del texto): https://www.gao.gov/assets/gao-08-333.pdf"
  - "APQC, Maverick purchasing means slower, more costly purchases (según su resumen): https://www.apqc.org/blog/maverick-purchasing-means-slower-more-costly-purchases"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3.1 y 4.2.3.2: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Wikipedia, Purchase order, sección Legal («no PO, no pay», según su resumen): https://en.wikipedia.org/wiki/Purchase_order"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (sección 2) y apqc-4-2.md"
aliases: [solicitud de compra, sobrepedido, porcentaje de sobrepedido, requisición, requisición de compra, pedido interno, pedido de materiales, purchase requisition, PR, material request, compra fuera del circuito, maverick spending, maverick spend, maverick buying, compra fuera de contrato, off-contract spend, no PO no pay]
creado: 2026-11-27
revisado: 2026-11-27
---

# Solicitud de compra

La solicitud de compra es el pedido interno con el que un área dice qué necesita, cuánto y para cuándo, antes de que alguien le pida precios a un proveedor. Sirve de autorización previa: la compra sale con el consentimiento de quien responde por el gasto y con presupuesto disponible, y lo que se compra sin pasar por ella es compra fuera del circuito.

Es el primer documento de [Orden de compra](orden-de-compra.md) y el único que no sale de la empresa. APQC 7.4 le dedica los dos primeros pasos de 4.2.3: «Process/Review requisitions» (4.2.3.1) y «Approve requisitions» (4.2.3.2).

## Qué registra y qué no mueve

Según el resumen del artículo de Wikipedia, la solicitud dice qué se necesita, cuánto, de qué fuente y a qué costo, y garantiza que la compra se haga con el consentimiento del jefe del área y con presupuesto suficiente. Es la definición más débil de las leídas, porque la sección no cita fuentes.

Un sistema abierto la modela como el registro de una necesidad interna antes de pedir precios. No genera asiento ni movimiento de stock. El mismo documento sirve para cinco propósitos: comprar, transferir entre depósitos, consumir, fabricar o subcontratar. Solo el primero termina en una orden de compra (lectura de esta base); la transferencia es de Inventario y la fabricación y la subcontratación, de Producción, todavía no armado.

Los estados del mismo sistema muestran que la solicitud también tiene avance:

| Estado | Qué significa |
|---|---|
| Borrador | Cargada, sin presentar |
| Pendiente | Presentada, sin orden todavía |
| Parcialmente ordenada / Ordenada | Una parte o todo ya está en órdenes de compra |
| Parcialmente recibida / Recibida | Llegó una parte o todo lo pedido |
| Detenida | Se frenó, sin anularla |
| Cancelada | Se anuló |

## De la solicitud a la orden

Una solicitud aprobada sigue por uno de dos caminos. Si hace falta comparar precios, pasa a un [pedido de cotización](../Abastecimiento-estrategico/cotizacion-y-licitacion.md); si el proveedor y el precio ya están fijados, pasa directo a la orden, tome el precio de las [condiciones](../Proveedores/condiciones-del-proveedor.md) del proveedor o de un [contrato marco](../Abastecimiento-estrategico/contrato-marco.md) (el reparto en dos caminos es lectura de esta base). En los dos casos la orden guarda la referencia a la solicitud, para saber cuánto de lo pedido ya se ordenó.

Una solicitud no siempre la escribe una persona. En el sistema abierto se crea sola cuando el stock proyectado de un artículo baja de su nivel de reposición; la regla que fija ese nivel está en [punto de pedido](../../Inventario-y-depositos/Reposicion/punto-de-pedido.md), de Inventario. Cuando la necesidad sale del plan de producción, la propondría el MRP (la planificación de los requerimientos de materiales, que calcula qué comprar a partir de lo que se va a fabricar), que es de Producción, todavía no armado; ninguna fuente leída lo describe.

La orden puede pedir más que la solicitud. El sistema abierto tiene un porcentaje de sobrepedido para cubrir el embalaje o el mínimo del proveedor, y su documentación advierte, según su resumen, que no se use para tapar un aumento que nadie aprobó. Tampoco conviene descontar de un contrato marco en la solicitud: un ERP grande controla el máximo del acuerdo en la orden y no en la solicitud, porque las solicitudes no siempre se aprueban.

## Quién pide y quién aprueba

Pide el área que necesita; aprueba quien responde por ese gasto. Cuántos niveles hay y hasta qué monto aprueba cada uno no es de este tema: lo fija la matriz de [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md), de Contabilidad. Lo que sí es de acá es en qué paso se aplica. La base lo lee así, como inferencia: la solicitud la aprueba quien responde por el presupuesto del área, y la orden se aprueba según su monto contra la matriz.

La regla que no depende del monto es la [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md): quien pide la compra no debería ser quien la recibe, porque podría comprar para sí y declarar que llegó (criterio de la base). Ninguna fuente leída describe un flujo de aprobación formal dentro de la solicitud; el sistema abierto no lo trae.

> [!NOTE] Sin fuente todavía: un libro de texto o una guía de práctica que describa quién pide y quién aprueba una solicitud, y cómo se combina esa aprobación con la de la orden.

## La compra fuera del circuito

La compra fuera del circuito es la que alguien hace por su cuenta, salteando la solicitud, la orden o el contrato marco vigente; en inglés, maverick spending. APQC la define como comprar fuera del proceso estándar y la explica porque el proceso se ve «too complicated or a waste of time», y la mide en su base de comparación (según el resumen de su artículo). En las organizaciones de peor desempeño, con ingresos de al menos USD 500 millones, representa «2.5 percent or more of their total purchases».

APQC concluye que no hace la compra más rápida ni más barata, aunque se crea lo contrario. Las organizaciones que más la practican necesitan, en la mediana, «16 hours more to issue a purchase order to a vendor» y gastan USD 2,58 más de costo de compras por cada USD 1.000 comprados. Son diferencias de mediana entre grupos, no una causa demostrada; que un proceso lento empuje a saltearlo, y no al revés, es lectura de esta base.

Algunas organizaciones responden con una regla dura, «no PO, no pay»: devuelven las facturas sin número de orden. La única fuente leída es la sección legal del artículo de Wikipedia. Una consecuencia posible es la orden cargada después de la factura, para regularizar una compra ya hecha; ninguna fuente leída la define ni la mide.

La tarjeta de compra es una salida legítima para la compra chica, con sus propios controles. El informe GAO-08-333 (2008) sobre las tarjetas del gobierno federal de Estados Unidos dice que sirven para compras de «paper and pencils» a computadoras; que las compras menores al límite de 2.500 dólares fueron el 97 % de las transacciones y casi el 57 % de los dólares; que la agencia de compras del Estado atribuía a la tarjeta unos 1.800 millones de dólares de ahorro anual frente al proceso en papel; y que el mismo informe encontró debilidades de control que expusieron al gobierno a fraude y abuso. Es una sola fuente, del sector público de un país.

> [!NOTE] Sin fuente todavía: la orden cargada después de la factura (after-the-fact PO) y los catálogos internos como salidas legítimas para la compra chica.

El costo de que el circuito se saltee no es solo de precio. Lo que se compra por afuera no descuenta del [contrato marco](../Abastecimiento-estrategico/contrato-marco.md), aparece en el [análisis del gasto](../Abastecimiento-estrategico/analisis-del-gasto.md) como gasto sin acuerdo y no tiene una orden contra la cual cruzar la factura en [compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md). Esta lectura es criterio de la base.
