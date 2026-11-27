---
resumen: >-
  La fecha prometida es la fecha de entrega que la empresa le compromete al cliente en el pedido. Se decide consultando cuánto hay sin comprometer en el stock y en lo que se va a recibir o fabricar (available-to-promise) o, si hay que producir, cuánta capacidad queda (capable-to-promise); el cálculo es de Inventario y de la planificación, y la promesa, de este tema.
estado: borrador
estabilidad: estable
fuentes:
  - "ASCM/APICS, CPIM 6.1 (2019) Excerpt, sección F, con definiciones del APICS Dictionary, 15.ª ed.: https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "Microsoft Learn, Order promising concepts (Dynamics 365 SCM): https://learn.microsoft.com/en-us/training/modules/set-up-order-cash-supply-chain-management/order-promising"
  - "APQC, Process Classification Framework 7.4, 3.5.4.3 «Determine availability»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "SCOR 6.0 Quick Reference, D1.3 y D2.3: https://www2.isye.gatech.edu/~lfm/8851/Sources/SCOR/SCORv6quickref.pdf"
  - "ERPNext, Sales Order (fecha de entrega por cabecera y por renglón): https://docs.frappe.io/erpnext/user/manual/en/sales-order"
  - "Wikipedia, Available-to-promise: https://en.wikipedia.org/wiki/Available-to-promise"
  - "Relacion-con-clientes/.investigacion/presupuesto-y-pedido.md (sección F)"
aliases: [fecha prometida, fecha de entrega comprometida, promised date, order promising, promesa de entrega, ATP, available-to-promise, disponible para prometer, CTP, capable-to-promise, capaz de prometer, disponibilidad]
creado: 2026-11-27
revisado:
---

# Fecha prometida

La fecha prometida es la fecha de entrega que la empresa le compromete al cliente en el pedido. Se decide consultando cuánto hay sin comprometer en el stock y en lo que se va a recibir o fabricar (available-to-promise) o, si hay que producir, cuánta capacidad queda (capable-to-promise); el cálculo es de Inventario y de la planificación, y la promesa, de este tema.

Es un campo del [pedido de venta](pedido-de-venta.md): en un sistema abierto, la fecha de entrega de la cabecera es la fecha prometida por defecto y cada renglón puede tener otra. Si se incumple, el problema llega a la [gestión de las promesas](../../Marketing/Servicio-y-relacion/gestion-de-las-promesas.md).

## Quién calcula y quién promete

SCOR 6.0 pone juntas la reserva y la fecha en un solo paso, D1.3 «Reserve Inventory and Determine Delivery Date», y para lo hecho contra pedido, D2.3 «Reserve Resources and Determine Delivery Date». APQC 7.4 tiene, dentro de la gestión de pedidos, un paso titulado «Determine availability» (3.5.4.3); de él solo se leyó el título.

La base las separa, y el reparto (criterio de la base) es este:

| Qué | De quién |
|---|---|
| Cuánto stock hay, cuánto está comprometido y qué entra cuándo | Inventario y depósitos, y la planificación (Cadena de suministro y Producción) |
| La reserva física de la mercadería para el pedido | Inventario y depósitos |
| Cuánto tarda el transporte hasta el cliente | Cadena de suministro y logística |
| Qué fecha se le dice al cliente y queda escrita en el pedido | Relación con clientes |

ASCM define el disponible para prometer sobre el plan maestro de producción, y el excerpt del CPIM dice que «sales professionals will be able to view available-to-promise information in the organization's master schedule». De ahí la base infiere el reparto: el vendedor consulta, no calcula, y el pedido consume y compromete la cifra.

## Available-to-promise: lo que no está comprometido

El APICS Dictionary (15.ª edición, citado en parte por el CPIM) define el ATP como «the uncommitted portion of a company's inventory and planned production maintained in the master schedule to support customer-order promising». Agrega que se calcula para cada período en que hay una entrada programada en el plan maestro y que, en el primer período, incluye el stock disponible menos los pedidos de clientes vencidos y por vencer.

El ejemplo del CPIM, con el método discreto:

- Primer período: «Beginning Inventory − Sum of Customer Orders Before Period Containing First Scheduled MPS Receipt», «70 units − 48 units = 22 units».
- Períodos con una entrada del plan maestro: «Scheduled MPS Receipt − Sum of Customer Orders Before Next Period Containing Scheduled MPS Receipt», «100 units − 66 units = 34 units».

Es decir: si hay 70 en stock y 48 ya prometidas antes de la próxima entrada, se pueden prometer 22 para ya; y de las 100 que entran, como 66 ya están prometidas, quedan 34 para esa fecha. El texto aclara que hay otros dos métodos (acumulados, con y sin mirada hacia adelante) que no presenta.

## Capable-to-promise: cuando hay que producir

Si lo que se vende se fabrica o se arma contra pedido, el stock no alcanza para prometer. El APICS Dictionary define el CTP como «The process of committing orders against available capacity as well as inventory», que puede abarcar varias plantas o centros de distribución, que usa un modelo de programación finita de la producción para saber cuándo se puede entregar, y cuyo objetivo es «to reduce the time spent by production planners in expediting orders and adjusting plans because of inaccurate delivery-date promises». Que sea el caso de los [productos configurables](../Presupuesto/productos-configurables.md) es inferencia de la base.

## Cinco maneras de prometer en un sistema

Un ERP de un proveedor grande ofrece cinco métodos para controlar la fecha de entrega, que sirven como escalera de complejidad:

1. **Ninguno**: supone que siempre hay stock.
2. **Plazo de venta**: suma un plazo fijo a la fecha del pedido, sin mirar el stock ni lo que entra.
3. **ATP**: mira el stock sin comprometer, los plazos, las entradas y las salidas planificadas.
4. **ATP más margen de salida**: suma el tiempo de preparar el envío.
5. **CTP**: explota el pedido contra la lista de materiales y las rutas de fabricación para ver cuándo se puede producir.

El mismo sistema distingue la fecha de despacho pedida y la fecha de recepción pedida, y ofrece alternativas de entrega (parcial, desde otro depósito, con otro transporte). La diferencia entre las dos fechas es el transporte, que es de Cadena de suministro.

Un comercio chico usa, sin saberlo, el método 1 o el 2: «lo tenemos» o «llega en una semana». Pasar al 3 pide que el stock esté bien registrado y que los pedidos reserven; sin eso, el ATP da números falsos con apariencia de precisión. Esto es criterio de la base.

## Dónde discrepan las fuentes

ASCM define el ATP sobre el plan maestro, descontando los pedidos de clientes vencidos y por vencer. Un sistema presenta el ATP como algo que reduce o elimina la necesidad de reservar, porque ya cuenta los pedidos cargados. No se contradicen: uno es el cálculo y el otro su implementación. Pero quien diseña tiene que decir qué cuenta como comprometido: los pedidos confirmados, los reservados o también los presupuestos aceptados sin pedido.

> [!NOTE] Sin fuente todavía: la definición literal de APQC 3.5.4.3 y el contenido del módulo «Customer and Order Management» de la certificación CLTD de ASCM; los dos solo se vieron por su título.
