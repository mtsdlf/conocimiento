---
resumen: >-
  La visita técnica es la cita concreta de un técnico en el lugar del cliente para trabajar sobre una orden de servicio: viaja, llega, trabaja, usa repuestos y la cierra con la conformidad del cliente, completa o con seguimiento. Cada paso deja la hora en que pasó, y de esos registros salen la factura y el historial del equipo.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Overview of Dynamics 365 Field Service, 2026-11-23: https://learn.microsoft.com/en-us/dynamics365/field-service/overview"
  - "Microsoft Learn, Work order lifecycle and system statuses, 2026-08-10: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status"
  - "ERPNext (Frappe), Maintenance Visit: https://docs.frappe.io/erpnext/user/manual/en/maintenance-visit"
  - "Odoo 17.0, Field Service: Product management: https://www.odoo.com/documentation/17.0/applications/services/field_service/product_management.html"
  - "Odoo 17.0, Field Service: Worksheets: https://www.odoo.com/documentation/17.0/applications/services/field_service/worksheets.html"
  - "Wikipedia, Field service management (secundaria, con «citation needed»): https://en.wikipedia.org/wiki/Field_service_management"
  - "IBM, What is first-time fix rate? (página del proveedor, leída): https://ibm.com/think/topics/first-time-fix-rate"
  - "PTC, What is first-time fix rate? (blog de proveedor; cifras atribuidas a Aberdeen, según el buscador): https://www.ptc.com/en/blogs/service/what-is-first-time-fix-rate"
  - "AEX, How to increase first-time fix rates (blog de proveedor; cifra atribuida a Aberdeen, según el buscador): https://aexinc.com/blog/how-to-increase-first-time-fix-rates"
  - "CustomerThink, sobre el informe de Aquant de 2026 (según el buscador): https://customerthink.com/?p=1080461"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 6.3.4.3.2 y 6.3.4.4: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/servicio-de-campo.md (rondas 1 y 2) y tercera-ronda.md"
aliases: [visita técnica, visita, visita de servicio, visita de mantenimiento, maintenance visit, service visit, reserva, booking, servicio en sitio, on-site service, stock de la camioneta, truck stock, van stock, firma del cliente, customer signature, conformidad del cliente, resolver en la primera visita, first-time fix, first-time fix rate, FTFR, visita de seguimiento, follow-up]
creado: 2026-11-27
revisado:
---

# Visita técnica

La visita técnica es la cita concreta de un técnico en el lugar del cliente para trabajar sobre una orden de servicio: viaja, llega, trabaja, usa repuestos y la cierra con la conformidad del cliente, completa o con seguimiento. Cada paso deja la hora en que pasó, y de esos registros salen la factura y el historial del equipo.

Es donde termina el recorrido de [Servicio de campo](servicio-de-campo.md): la arma el [despacho](despacho-y-agenda.md), que le pone técnico y horario, y la orden que atiende sigue el ciclo de la [orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md). Un sistema abierto la define como «a visit made by an engineer to a Customer's premise for maintenance work of an Item». APQC tiene, como lo más cercano, 6.3.4.3.2 «Execute product repair».

## Cada estado deja su hora

La visita avanza por estados, y cada cambio queda sellado con la hora. En un sistema de servicio de campo de referencia, la visita pasa por programada, en viaje, en curso, en descanso y terminada; según su documentación, cada cambio de estado crea una marca de tiempo. Pasar a en curso indica que el técnico llegó, y completa en la orden la hora real de llegada y la primera llegada.

Al cerrar, el sistema calcula con esas marcas la duración total, el descanso, la duración facturable y el costo. Que las horas salgan de tocar el estado en el momento, y no de cargarlas a mano, es criterio de la base: si el técnico toca todo al final del día, las horas no sirven, y es el mismo problema de calidad que describe [cierre de la orden](../Orden-de-trabajo/cierre-de-la-orden.md).

## El viaje: un dato y un cargo

El viaje es lo que el mantenimiento interno no tiene, y el sistema lo trata dos veces. Como dato, registra el estado en viaje, las millas recorridas y la duración real del viaje. Como cargo, agrega a la orden un ítem de viaje, si la cuenta del cliente tiene un cargo de viaje configurado y la visita tuvo duración de viaje distinta de cero.

Si el viaje se cobra o lo absorbe el contrato depende de la cobertura que defina el [contrato de servicio](contrato-de-servicio.md#qué-se-factura-y-la-doble-factura). El dato sirve igual en los dos casos: el tiempo de viaje medido es lo que el [despacho](despacho-y-agenda.md#el-ruteo-es-un-problema-de-ruteo-de-vehículos) intenta bajar.

## Lo que lleva el técnico

Según el sistema de referencia, en el teléfono o la tableta ve la ubicación, las instrucciones de la orden, el equipo y su historial, y puede sacar fotos y videos. El equipo sale de la [base instalada](base-instalada.md), y el historial se arma como el [historial del equipo](../Registro-de-activos/historial-del-equipo.md) propio: con lo que dejó cada orden al cerrarse. Otro sistema le da formularios que se completan en sitio.

El trabajo tiene que poder hacerse sin señal: el mismo sistema deja descargar los datos «for offline work when internet isn't available». En un sótano o una sala de máquinas, una aplicación que exige conexión deja al técnico sin el historial; esto es criterio de la base.

## El stock de la camioneta

El técnico lleva repuestos con él, y esa camioneta es un depósito más. El sistema de referencia lo llama «truck stock»: los encargados de inventario aseguran que el técnico tenga lo necesario, y al instalar una pieza se registra una baja «from the related warehouse or truck». En otro sistema, los productos de los pedidos creados en la intervención salen siempre del depósito por defecto, y el stock se actualiza cuando la tarea se marca terminada.

Qué repuesto pide la orden y cuándo se registra el consumo está en [repuestos y materiales](../Orden-de-trabajo/repuestos-y-materiales.md). Cuánto stock lleva cada camioneta, cómo se repone y cómo se cuenta es del tema [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md). La pieza instalada puede pasar a ser un equipo del cliente, como se explica en [base instalada](base-instalada.md#cómo-nace-un-equipo-en-la-base).

## La conformidad del cliente

La visita termina con el cliente dando por bueno el trabajo. En el sistema de referencia, el técnico puede «record a digital customer signature»; en el sistema abierto, el comentario del cliente es un campo opcional de la visita. La firma sirve después: si el cliente discute la factura, es la prueba de que el técnico fue, cuánto estuvo y qué hizo. Esa lectura es criterio de la base; ninguna fuente leída la describe así.

> [!NOTE] Sin fuente todavía: el informe de servicio como documento que se le deja al cliente (qué dice, si es obligatorio) y la validez de la firma digital como conformidad en la Argentina.

## Cerrar la visita sin terminar la orden

Una visita puede cerrarse sin que el trabajo esté terminado. El técnico marca la orden «as complete or as requiring a follow-up», según el sistema de referencia; una visita cerrada como parcialmente completa devuelve la orden a sin programar, para que el despacho arme la siguiente. El sistema abierto tiene los dos estados de cierre de la visita: parcialmente completa y completa.

Funciona porque la orden y la visita tienen ciclos independientes, como explica [despacho y agenda](despacho-y-agenda.md#la-orden-de-servicio-y-la-visita-son-dos-objetos). Una orden con tres visitas necesitó tres viajes.

## De la visita a la factura

La factura no sale de la visita sino de la orden, y la emite otra persona. Cuando el trabajo termina, la orden pasa a terminada; un supervisor o alguien de administración la revisa y la pasa a contabilizada, y ese paso dispara la factura por repuestos y mano de obra. El tiempo de trabajo es facturable por defecto, el descanso solo si la lista de precios lo dice, y el viaje entra como un ítem más.

Qué cubre el contrato y qué se cobra está en [contrato de servicio](contrato-de-servicio.md); la factura y la cuenta a cobrar son de [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md).

## Resolver en la primera visita

Resolver en la primera visita («first-time fix») es terminar el trabajo en la primera cita, sin visita de seguimiento, sin repuestos adicionales y sin ayuda externa, y se mide, según una página de IBM, como el porcentaje de trabajos completados en la primera visita sin visitas de seguimiento: los resueltos en la primera visita sobre el total de trabajos completados, por cien. El sistema de referencia lo pone como objetivo («Improve first-time fix rate») y una enciclopedia lo cita como beneficio, los dos sin cifra.

Las cifras que circulan se atribuyen a Aberdeen Group, pero llegan por blogs de proveedores que no coinciden entre sí. Uno da 88 % para los mejores, 80 % para el promedio y 63 % para los rezagados; otro, un promedio de cerca de 75 %. El informe original de Aberdeen no se encontró. Un informe de otro proveedor, de 2026 y con unos 30 millones de eventos de servicio, da 77 % según un tercero que lo comenta. Ninguna se leyó en la fuente original: no sirven para compararse. La página de IBM también cita un estudio de Aberdeen Group (por debajo de 70 % perjudicaría la retención, la satisfacción y el cumplimiento de los SLA) y no describe su método. No se encontró una fuente con método publicado: lo que hay son páginas de proveedores y su definición sale de ellas, no de un estudio.

> [!NOTE] Sin fuente todavía: por qué falla la primera visita (falta el repuesto en la camioneta, el técnico no tiene la habilidad, el diagnóstico del caso fue malo) y en qué proporción. Las tres causas son el saber del sector, y cada una apunta a otra pieza: la [camioneta](#el-stock-de-la-camioneta), el [despacho](despacho-y-agenda.md#con-qué-criterios-se-elige-al-técnico) y la atención al cliente.

## El cierre vuelve al caso

Si la visita nació de un reclamo, su cierre no le contesta al cliente: lo hace la atención. La atención, el caso, el reclamo y el escalamiento son del tema [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md); este tema empieza cuando el caso deriva a un técnico, y el cierre de la orden vuelve al caso para que la atención le conteste al cliente. Ese límite está en [servicio de campo](servicio-de-campo.md#del-caso-del-cliente-a-la-factura).

Lo que queda en este tema es el registro: la orden cerrada se suma al historial del equipo de la base instalada, y contar las visitas de cada orden da el dato para resolver en la primera visita y para los [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md); esto último es inferencia de la base.
