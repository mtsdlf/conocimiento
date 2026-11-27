---
resumen: >-
  La base instalada es el registro de cada equipo que la empresa vendió o instaló y que está en manos de un cliente: qué es, su número de serie, dónde está, cuándo se instaló y qué cobertura tiene. Cumple para los equipos ajenos el papel que el registro de activos cumple para los propios, y no tiene contraparte contable en la empresa que lo lleva.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, Overview of Dynamics 365 Field Service, 2026-11-23: https://learn.microsoft.com/en-us/dynamics365/field-service/overview"
  - "Microsoft Learn, Work order lifecycle and system statuses, 2026-08-10: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status"
  - "Microsoft Learn, Set up customer agreements to generate work orders, 2026-03-02: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-agreements-work-orders"
  - "Microsoft Learn, Customer agreements overview, 2026-08-28: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-customer-agreements"
  - "ERPNext (Frappe), Serial No: https://docs.frappe.io/erpnext/user/manual/en/serial-no"
  - "ERPNext (Frappe), Warranty Claim: https://docs.frappe.io/erpnext/user/manual/en/warranty-claim"
  - "Wikipedia, Installed base: https://en.wikipedia.org/wiki/Installed_base"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 6.3.1 «Register products»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/servicio-de-campo.md (rondas 1 y 2)"
aliases: [base instalada, installed base, parque instalado, equipo del cliente, activo del cliente, customer asset, customer equipment, número de serie, serial number, registro de productos, product registration]
creado: 2026-11-27
revisado:
---

# Base instalada

La base instalada es el registro de cada equipo que la empresa vendió o instaló y que está en manos de un cliente: qué es, su número de serie, dónde está, cuándo se instaló y qué cobertura tiene. Cumple para los equipos ajenos el papel que el registro de activos cumple para los propios, y no tiene contraparte contable en la empresa que lo lleva.

Es el punto de partida de [Servicio de campo](servicio-de-campo.md): la orden de servicio, la visita y el reclamo de garantía se abren sobre un equipo de la base instalada. Sin ese registro, el técnico no tiene a mano el modelo ni lo que se le hizo antes; es criterio de la base. La atención, el caso, el reclamo y el escalamiento son del tema [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md); este tema empieza cuando el caso deriva a un técnico, y el cierre de la orden vuelve al caso.

## Dos sentidos de la expresión

La expresión tiene dos sentidos, y conviene decir cuál se usa. En el sentido de mercado, según una enciclopedia, la base instalada de un producto es «the number of units that are currently in use by customers»: un conteo, que se distingue de la cuota de mercado y sirve para decidir el nivel de soporte y la disponibilidad de repuestos. En el sentido de servicio, que es el de este tema, es la lista de esas unidades una por una, cada una con su cliente, su lugar y su historia.

El segundo sentido contiene al primero: contar los equipos de la lista da el número de unidades en uso. APQC tiene 6.3.1 «Register products» dentro del servicio posventa; el marco da el título y no lo define.

## Qué se guarda de cada equipo

Cada equipo de la base instalada es un registro con estos datos. El número de serie es la clave, por criterio de la base: distingue dos equipos del mismo modelo. La lista de datos también es criterio de la base, armada con lo que registran los sistemas de referencia.

| Dato | Para qué sirve |
|---|---|
| Producto y número de serie | Qué es, y cuál de todos los iguales |
| Cliente | Quién lo tiene; sale del [registro del cliente](../../Relacion-con-clientes/Registro-del-cliente/registro-del-cliente.md) |
| Lugar | Dónde va el técnico; en un sistema de referencia, el contrato se ejecuta en «a single location represented by the service account» |
| Instalación | Con qué detalles quedó funcionando; la fecha, por criterio de la base |
| Cobertura | Garantía o contrato vigente, con sus fechas de vencimiento |
| Historial | Las órdenes y visitas que tuvo |

Un sistema de referencia ofrece «asset management capabilities to keep track of customer equipment and service history», y el contrato permite definir trabajo recurrente sobre un equipo puntual para «build service history». El historial se arma igual que el del [historial del equipo](../Registro-de-activos/historial-del-equipo.md) propio: con lo que registra cada orden al cerrarse.

> [!NOTE] Sin fuente todavía: el lugar del equipo como registro propio, separado del cliente (un cliente con varias sucursales); la estructura de componentes de un equipo del cliente, como la que tiene la [jerarquía de activos](../Registro-de-activos/jerarquia-de-activos.md) propia; y la fecha de instalación como dato del modelo. Ninguna fuente leída los describe.

## Cómo nace un equipo en la base

Por criterio de la base, un equipo entra a la base instalada en el momento en que deja de ser stock de la empresa. Las fuentes leídas muestran dos caminos:

- **Desde la entrega.** En un sistema abierto, cuando el número de serie sale con un pedido de venta, «the Customer will be linked here», y solo se entregan números de serie en estado disponible. El [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) deja así al cliente atado al equipo.
- **Desde la instalación.** En un sistema de servicio de campo, instalar una pieza en el domicilio registra una baja del depósito o de la camioneta y da de alta la pieza «as a new customer asset along with installation and repair details». Al completar la orden, los productos marcados para eso pasan a ser equipos del cliente.

Que el alta salga sola de la entrega o de la instalación, y no de una carga a mano posterior, es criterio de la base. Una base cargada a mano se desactualiza con cada venta que nadie registra, y ese problema de [calidad de datos](../../Datos/Gobierno-y-calidad/calidad-de-datos.md), por inferencia de la base, aparece recién cuando un técnico va a un equipo que no existe o no encuentra uno que sí. La base instalada es un dato maestro del servicio, en el sentido de [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md).

## La cobertura se lee del número de serie

La cobertura de un equipo se deriva de su número de serie. En un sistema abierto, al elegir el número de serie en un reclamo, el sistema trae el producto y uno de cuatro estados, con su fecha de vencimiento: «Under Warranty», «Out of Warranty», «Under AMC» y «Out of AMC», donde AMC es el contrato anual de mantenimiento. El estado se puede cambiar a mano, por ejemplo si el equipo fue manipulado por terceros.

Por inferencia de la base, con el número de serie la atención puede saber en el primer llamado si el equipo tiene garantía o contrato y hasta cuándo. Qué cubre cada uno está en [contrato de servicio](contrato-de-servicio.md).

## Un activo que no está en el balance

El equipo de la base instalada es del cliente. La empresa que presta el servicio lleva su registro, su historial y su plan, pero no lo tiene entre sus bienes de uso: no se amortiza ni se da de baja en su contabilidad, que trata [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md) solo para lo propio. Es el caso más claro de lo que la entrada del tema llama registro operativo sin registro contable.

El repuesto que se instala sí pasa por los libros de quien presta el servicio: sale de su stock; quién lo paga, el cliente o el contrato, depende de la cobertura, que ninguna fuente leída detalla. Ese movimiento de stock es del tema [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md).
