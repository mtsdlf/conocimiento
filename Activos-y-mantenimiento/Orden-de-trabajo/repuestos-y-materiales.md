---
resumen: >-
  Los repuestos y materiales de una orden de trabajo son lo que el trabajo consume además de horas: piezas del equipo, insumos y consumibles. La orden los pide, los reserva contra el stock y registra lo que de verdad se usó, que pasa al costo de la orden y al historial del equipo.
estado: vigente
estabilidad: semi
fuentes:
  - "IBM, Maximo Manage, Work order statuses (estado esperando materiales): https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=orders-work-order-statuses"
  - "ERPNext, Asset Repair (repuestos consumidos y costo): https://docs.frappe.io/erpnext/user/manual/en/asset-repair"
  - "Microsoft Learn, Overview of Dynamics 365 Field Service (2026-11-23): https://learn.microsoft.com/en-us/dynamics365/field-service/overview"
  - "Microsoft Learn, Dynamics 365 Field Service, Work order lifecycle and system statuses (2026-08-10): https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status"
  - "Odoo 17, Field Service, Product management: https://www.odoo.com/documentation/17.0/applications/services/field_service/product_management.html"
  - "Odoo 17, Maintenance requests (la solicitud no lista materiales): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.2.2 «Obtain required resources»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/orden-de-trabajo.md, registro-y-desempeno.md, servicio-de-campo.md y apqc-10.md"
aliases: [repuestos, materiales de mantenimiento, spare parts, MRO, repuestos críticos, critical spares, reserva de materiales, material reservation, consumo de materiales, esperando materiales, waiting for materials]
creado: 2026-11-27
revisado: 2026-11-27
---

# Repuestos y materiales

Los repuestos y materiales de una orden de trabajo son lo que el trabajo consume además de horas: piezas del equipo, insumos y consumibles. La orden los pide, los reserva contra el stock y registra lo que de verdad se usó, que pasa al costo de la orden y al historial del equipo.

APQC 7.4 lo ubica en «Obtain required resources» (10.3.2.2), un proceso de recursos en general, dentro de gestionar el mantenimiento. Lo prepara la [planificación](planificacion-y-programacion.md) al armar el paquete de trabajo y lo cierra el [cierre de la orden](cierre-de-la-orden.md) al registrar el consumo. Un sistema de gestión para pymes muestra el mínimo posible: su ficha de solicitud de mantenimiento no lista materiales.

## Dónde termina este componente

Este tema decide qué repuestos lleva un equipo, cuáles son críticos y cuáles reserva una orden. Cuántos hay, dónde están y cuánto valen es del tema [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md); comprarlos, del tema [Compras y abastecimiento](../../Compras-y-abastecimiento/compras-y-abastecimiento.md), que arranca con la [solicitud de compra](../../Compras-y-abastecimiento/Orden-de-compra/solicitud-de-compra.md). Cómo el depósito aparta mercadería para un pedido está en [reserva](../../Inventario-y-depositos/Operacion-del-deposito/reserva.md). La orden es cliente de los dos: pide al depósito lo que hay y, por medio del depósito o directo, a compras lo que falta.

## Qué pide la orden

Una orden pide dos clases de cosas, y la distinción es criterio de la base. Los repuestos son piezas identificadas del equipo (un rodamiento, un sello, una placa) que se instalan y quedan en él. Los materiales e insumos se gastan en el trabajo (lubricante, trapos, tornillería) y no se rastrean pieza por pieza. Los primeros importan para el historial del equipo; los segundos, casi solo para el costo.

El punto de partida es la lista de repuestos del equipo, que dice de qué piezas está hecho y cuáles se cambian. Vive en el registro, junto con la estructura del equipo, en [jerarquía de activos](../Registro-de-activos/jerarquia-de-activos.md). Con esa lista, el planificador no tiene que adivinar el código de la pieza: elige de lo que el equipo lleva. Para trabajos que se repiten, el preventivo puede traer la lista de materiales ya cargada en la tarea; eso está en [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md).

> [!NOTE] Sin fuente todavía: cómo modela un sistema la lista de repuestos del equipo (maintenance BOM) y su relación con la lista de materiales de fabricación.

## Repuestos críticos

Un repuesto crítico es, en la definición de la base, el que, si falta cuando el equipo falla, deja el equipo parado más tiempo del que el negocio aguanta. Se decide por el equipo y no por el repuesto: la misma pieza puede ser crítica para la bomba principal y no para la de respaldo. Por eso se apoya en la [criticidad](../Registro-de-activos/criticidad.md) del equipo y en cuánto tarda en llegar la pieza. Un repuesto crítico se guarda aunque rote poco, y eso choca con el criterio de un depósito que busca bajar stock inmovilizado; esta tensión es criterio de la base.

> [!NOTE] Sin fuente todavía: métodos para clasificar repuestos críticos y para fijar cuántos guardar de cada uno.

## Reservar y consumir

Reservar es apartar en el depósito, a nombre de una orden, las piezas que va a usar; consumir es registrar que salieron y se usaron. Son dos momentos, y la diferencia entre los dos es la información útil: lo reservado y no usado vuelve al stock, lo usado y no reservado es un trabajo mal planificado. Esta lectura es criterio de la base.

Las fuentes de práctica muestran el consumo como el momento que mueve el stock. En un sistema de servicio de campo, instalar una pieza en casa del cliente registra «a reduction in inventory from the related warehouse or truck»; el ajuste de inventario es el último paso del ciclo de la orden, y el técnico puede llevar stock en la camioneta. En otro sistema, los productos de los pedidos creados desde la tarea salen del depósito por defecto, y el stock se actualiza solo cuando la tarea se marca terminada. Lo propio del técnico que viaja está en [visita técnica](../Servicio-de-campo/visita-tecnica.md).

Lo que se consume tiene que quedar en la orden, porque de ahí sale su costo. Un ERP abierto calcula el costo de una reparación con las facturas de proveedores y los repuestos consumidos.

## Esperando materiales

Cuando falta un repuesto, la orden no puede avanzar y lo tiene que decir. Un sistema de mantenimiento de referencia tiene un estado propio para eso, esperando materiales: «Materials must arrive before the work can be performed». Se puede entrar a él antes de empezar o desde una orden en curso, cuando al abrir el equipo aparece una pieza que no se previó.

El estado sirve para dos cosas. Saca la orden del pendiente listo, para que no se programe trabajo que no se puede hacer (ver [planificación y programación](planificacion-y-programacion.md)). Y mide cuánto trabajo frena el abastecimiento: muchas órdenes esperando la misma pieza señalan un repuesto que debería ser crítico. Las dos son inferencias de la base.
