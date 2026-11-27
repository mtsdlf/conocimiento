---
resumen: >-
  El pedido de venta es el compromiso de una empresa de entregarle a un cliente ciertos productos o servicios, en cierta cantidad, a cierto precio y para cierta fecha. Es un documento con estados que siguen dos ejes a la vez, cuánto se entregó y cuánto se facturó, y es el punto donde la venta pasa a los dominios que reservan, despachan, facturan y cobran.
estado: vigente
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 3.5.4 «Manage sales orders»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "SCOR 6.0 Quick Reference, D1 y D2: https://www2.isye.gatech.edu/~lfm/8851/Sources/SCOR/SCORv6quickref.pdf"
  - "ERPNext, Sales Order (estados, fecha prometida, entrega y facturación parciales): https://docs.frappe.io/erpnext/user/manual/en/sales-order"
  - "Odoo 17, Receipts and deliveries in one step (confirmar el pedido crea la entrega): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.html"
  - "Odoo 17, Invoicing policy: https://www.odoo.com/documentation/17.0/applications/sales/sales/invoicing/invoicing_policy.html"
  - "Magal y Word (2011), Integrated Business Processes with ERP Systems, cap. 5 «The Fulfillment Process» (no leído; solo el título): https://www.oreilly.com/library/view/integrated-business-processes/9780470478448/14_chap05.html"
  - "Relacion-con-clientes/.investigacion/presupuesto-y-pedido.md (sección E)"
aliases: [pedido de venta, sales order, orden de venta, nota de pedido, pedido del cliente, customer order, toma de pedido, order entry, entrada de pedidos, gestión de pedidos, order management]
creado: 2026-11-27
revisado: 2026-11-27
---

# Pedido de venta

El pedido de venta es el compromiso de una empresa de entregarle a un cliente ciertos productos o servicios, en cierta cantidad, a cierto precio y para cierta fecha. Es un documento con estados que siguen dos ejes a la vez, cuánto se entregó y cuánto se facturó, y es el punto donde la venta pasa a los dominios que reservan, despachan, facturan y cobran.

Es el último de los cuatro objetos de [Relación con clientes](../relacion-con-clientes.md). Sale de un [presupuesto](../Presupuesto/presupuesto.md) aceptado o se carga directo, sin presupuesto, cuando el cliente pide algo de lista: un comercio que repone mercadería, una venta de mostrador. Toma del [registro del cliente](../Registro-del-cliente/registro-del-cliente.md) quién compra, quién paga y a dónde se entrega (ver [cuenta y contacto](../Registro-del-cliente/cuenta-y-contacto.md)), y las [condiciones comerciales](../Registro-del-cliente/condiciones-comerciales.md). Es también el comienzo del recorrido del pedido al cobro, que se va a contar en el tema Procesos de negocio.

## Qué compromete un pedido

Un pedido tiene la misma forma que un presupuesto (cabecera y renglones con producto, cantidad, precio, descuento e impuesto) y agrega lo que hace falta para cumplirlo: la [fecha prometida](fecha-prometida.md) y, si lo hay, el número de la orden de compra del cliente; la dirección de entrega y el depósito desde donde sale son criterio de la base. En un sistema abierto, la fecha de entrega de la cabecera es la fecha prometida por defecto, y cada renglón puede tener la suya para entregas escalonadas.

La diferencia con el presupuesto es el compromiso. El presupuesto ofrece; el pedido obliga a la empresa a entregar y, en la mayoría de los casos, al cliente a pagar. Un sistema abierto lo dice así: el pedido registra el pedido confirmado del cliente y, al presentarlo, confirma el compromiso y lo deja disponible para los pasos siguientes.

## Dónde está en los marcos de procesos

APQC 7.4 tiene un proceso propio, 3.5.4 «Manage sales orders», con seis pasos:

| Código | Paso |
|---|---|
| 3.5.4.1 | «Accept and validate sales orders» |
| 3.5.4.2 | «Collect and maintain account information» |
| 3.5.4.3 | «Determine availability» |
| 3.5.4.4 | «Determine fulfillment process» |
| 3.5.4.5 | «Process back orders and updates» |
| 3.5.4.6 | «Handle sales order inquiries including post-order fulfillment transactions» |

SCOR 6.0 lo pone dentro del proceso de entrega. Para producto en stock: D1.2 «Receive, Enter, & Validate Order» y D1.3 «Reserve Inventory and Determine Delivery Date»; para producto hecho contra pedido, D2.2 «Receive, Configure, Enter and Validate Order» y D2.3 «Reserve Resources and Determine Delivery Date». SCOR pone en un mismo paso (D1.3) reservar el stock y fijar la fecha de entrega. Este tema se queda con la promesa al cliente y deja el cálculo y la reserva a Inventario; el reparto está en [fecha prometida](fecha-prometida.md).

## Los estados: dos ejes cruzados

Los estados de un pedido no forman una línea. Los seis primeros de la tabla son los de un sistema abierto; «completado» y «anulado» los suma la base para cerrar el ciclo (el mismo sistema permite anular un pedido confirmado entero):

| Estado | Qué significa |
|---|---|
| Borrador | Guardado, sin confirmar |
| A entregar y facturar | Confirmado; falta entregar y falta facturar |
| A entregar | Falta entregar (lectura de la base: ya se facturó, por ejemplo por adelantado) |
| A facturar | Falta facturar (lectura de la base: ya se entregó) |
| En espera | Se pausó el cumplimiento |
| Cerrado | Se decidió no entregar lo que faltaba |
| Completado | Todo entregado y facturado |
| Anulado | Se deshizo el pedido entero |

Lo que se ve es el cruce de dos ejes: cuánto se entregó (nada, una parte, todo) y cuánto se facturó (nada, una parte, todo). Por eso el mismo sistema lleva el porcentaje entregado y el porcentaje facturado de cada pedido, que se actualizan con cada entrega y cada factura parcial. Qué se factura primero depende de la política: facturar lo pedido permite facturar apenas se confirma; facturar lo entregado exige validar la entrega antes. Modelar el estado como una sola lista de valores, sin los dos ejes, es la manera más común de que el pedido mienta: dice «entregado» cuando faltan renglones. Esto último es criterio de la base.

## Qué dispara aguas abajo

Confirmar el pedido pone en marcha a los vecinos:

- **[Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md)** [reserva](../../Inventario-y-depositos/Operacion-del-deposito/reserva.md) la mercadería y la [prepara](../../Inventario-y-depositos/Operacion-del-deposito/preparacion-de-pedidos.md). En un sistema abierto, confirmar el pedido crea la orden de entrega.
- **[Cadena de suministro y logística](../../Cadena-de-suministro-y-logistica/Despacho-y-entrega/despacho-y-entrega.md)** la despacha y la transporta; para una tienda, el caso está en [fulfillment](../../Comercio-electronico/Operaciones-del-comercio/Envios-y-logistica/fulfillment.md).
- **[Contabilidad](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md) e [Impuestos](../../Impuestos/Cumplimiento/comprobante-fiscal.md)** emiten la factura y registran la deuda del cliente; en la Argentina, con [la factura electrónica de ARCA](../../Comercio-electronico/Normativa/factura-electronica-de-arca.md) y, entre empresas, con lo de [factura entre empresas](../../Comercio-electronico/Comercio-B2B/factura-entre-empresas.md).
- **[Tesorería](../../Tesoreria/Credito-y-cobranzas/credito-y-cobranzas.md)** cobra; si el cliente compra a plazo, la deuda va a su [cuenta corriente](../../Comercio-electronico/Comercio-B2B/cuenta-corriente-y-credito.md).

Cada uno de esos pasos produce su propio documento (entrega, factura, cobro) que apunta al pedido; el recorrido entero está en [del pedido al cobro](../../Procesos-de-negocio/del-pedido-al-cobro.md). Esa cadena de documentos es la que permite responder a consultas del tipo «dónde está mi pedido», que APQC pone en 3.5.4.6. Que el pedido en sí no mueva stock ni plata, y que los movimientos los registren los documentos de cada dominio con el patrón de [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md), es criterio de la base.

Cómo llega un pedido (un vendedor que visita, el teléfono, el chat, un portal, la tienda) no cambia el objeto: todos tienen que terminar en el mismo registro. En la venta entre empresas, ese problema está en [pedido B2B](../../Comercio-electronico/Comercio-B2B/pedido-b2b.md) y en [preventa y autoventa](../../Comercio-electronico/Comercio-B2B/preventa-y-autoventa.md).

En la Argentina, una nota de pedido no es un comprobante fiscal y lleva una leyenda que lo dice; está en [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md).

## Qué hay en Pedido de venta

- [Fecha prometida](fecha-prometida.md): cómo se decide qué fecha prometerle al cliente (available-to-promise, capable-to-promise) y quién calcula y quién promete.
- [Tipos de pedido](tipos-de-pedido.md): de contado, a plazo, abierto o marco, recurrente, de muestra; y dónde terminan las devoluciones y la consignación.
- [Cambios y cancelaciones](cambios-y-cancelaciones.md): entregar en partes, lo pendiente de entrega, pausar, cerrar, anular y bloquear un pedido.
