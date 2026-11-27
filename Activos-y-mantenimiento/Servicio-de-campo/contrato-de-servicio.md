---
resumen: >-
  El contrato de servicio es el acuerdo por el que una empresa se obliga a mantener o reparar equipos de un cliente durante un período, a un precio negociado: dice qué equipos cubre, dónde, cada cuánto se visitan y qué se cobra aparte. A diferencia de la garantía, que es una promesa del vendedor, el contrato es un servicio que se vende, y es lo que genera las visitas preventivas.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft Learn, Set up customer agreements to generate work orders, 2026-03-02: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-agreements-work-orders"
  - "Microsoft Learn, Customer agreements overview, 2026-08-28: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-customer-agreements"
  - "Microsoft Learn, Entitlements for work orders overview, 2026-09-16: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-entitlements-overview"
  - "Microsoft Learn, Create entitlements for work orders, 2026-08-07: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-entitlements"
  - "Microsoft Learn, Work order lifecycle and system statuses, 2026-08-10: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status"
  - "Microsoft Learn, Configure SLAs in Customer Service, 2026-11-06: https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/define-service-level-agreements"
  - "Microsoft Learn, Overview of Dynamics 365 Field Service, 2026-11-23: https://learn.microsoft.com/en-us/dynamics365/field-service/overview"
  - "ERPNext (Frappe), Warranty Claim: https://docs.frappe.io/erpnext/user/manual/en/warranty-claim"
  - "Odoo 17.0, Field Service: Product management: https://www.odoo.com/documentation/17.0/applications/services/field_service/product_management.html"
  - "Wikipedia, Warranty: https://en.wikipedia.org/wiki/Warranty"
  - "Wikipedia, Service-level agreement: https://en.wikipedia.org/wiki/Service-level_agreement"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 6.1.6 «Define warranty claims» y 10.3.2.7: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/servicio-de-campo.md (rondas 1 y 2)"
aliases: [contrato de servicio, contrato de mantenimiento, service contract, service agreement, maintenance contract, acuerdo de servicio, abono de mantenimiento, AMC, annual maintenance contract, garantía, warranty, garantía extendida, extended warranty, cobertura, entitlement, derecho de servicio, SLA, acuerdo de nivel de servicio]
creado: 2026-11-27
revisado: 2026-11-27
---

# Contrato de servicio

El contrato de servicio es el acuerdo por el que una empresa se obliga a mantener o reparar equipos de un cliente durante un período, a un precio negociado: dice qué equipos cubre, dónde, cada cuánto se visitan y qué se cobra aparte. A diferencia de la garantía, que es una promesa del vendedor, el contrato es un servicio que se vende, y es lo que genera las visitas preventivas.

Dentro de [Servicio de campo](servicio-de-campo.md), el contrato se apoya en la [base instalada](base-instalada.md), porque cubre equipos con número de serie, y alimenta al [despacho](despacho-y-agenda.md) con las órdenes que genera. Venderlo es de [Relación con clientes](../../Relacion-con-clientes/relacion-con-clientes.md): sale de un [presupuesto](../../Relacion-con-clientes/Presupuesto/presupuesto.md) y se confirma con un [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md), que puede ser del tipo recurrente que describe [tipos de pedido](../../Relacion-con-clientes/Pedido-de-venta/tipos-de-pedido.md). Acá interesa qué cubre y qué promete una vez firmado. La atención, el caso, el reclamo y el escalamiento son del tema [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md); este tema empieza cuando el caso deriva a un técnico, y el cierre de la orden vuelve al caso.

## Garantía y contrato: una promesa y un producto

La garantía y el contrato son dos fuentes de cobertura que el técnico ve en el mismo lugar, pero nacen distinto. Según una enciclopedia, la garantía es «an expressed or implied promise or assurance of some kind» del vendedor al comprador, y puede ser implícita: promesas no escritas que surgen de la naturaleza de la venta, según la ley de cada lugar. La garantía extendida o «service contract», en cambio, la venden el fabricante o un tercero para «extend the warranty for a further length of time», con sus propios términos y exclusiones (uso comercial, abuso, piezas de desgaste). Revisar si un reclamo está cubierto y autorizarlo es una decisión del caso, que está en [garantía y reparación](../../Servicio-al-cliente/Caso/garantia-y-reparacion.md); acá queda qué promete el contrato.

Esa descripción es del derecho de los Estados Unidos. En la Argentina, la Ley 24.240 de Defensa del Consumidor (art. 21) exige que el presupuesto de una reparación diga si se otorga garantía y con qué alcance; está en [Relación con clientes en la Argentina](../../Relacion-con-clientes/relacion-con-clientes-en-argentina.md).

> [!NOTE] Sin fuente todavía: la garantía legal de los productos en la Argentina (plazos y qué cubre), leída en la norma.

En los sistemas, las dos terminan en el mismo reclamo. Un sistema abierto define el reclamo de garantía como el pedido de un cliente de reparación gratuita sobre algo «still covered by warranty or an Annual Maintenance Contract (AMC)», y el estado de cobertura sale del número de serie, como se explica en [base instalada](base-instalada.md#la-cobertura-se-lee-del-número-de-serie). APQC tiene 6.1.6 «Define warranty claims», con 6.1.6.1 «Determine and document warranty policies», y 6.3.2 «Process warranty claims»: la política por un lado y cada reclamo por otro.

## El contrato genera las visitas preventivas

El contrato no es solo una cláusula de cobertura: es lo que dispara el trabajo recurrente. Un sistema de referencia lo dice así: los acuerdos «let organizations automatically generate work orders and invoices with predefined details, frequencies, and date ranges», con ejemplos como el mantenimiento trimestral de ascensores o el control de plagas semanal. Cumple el papel del plan de [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) cuando el equipo es del cliente.

Armar un contrato en ese sistema tiene cuatro pasos: crear el acuerdo con cliente, fechas y lista de precios; agregar la programación de visitas, con su recurrencia; cargar el detalle (tipos de problema, productos, servicios, tareas); y activarlo. La recurrencia tiene tres parámetros:

| Parámetro | Ejemplo de la documentación |
|---|---|
| Patrón | Mensual durante un año, sobre un equipo instalado |
| Anticipación | Las órdenes se generan días antes de la fecha; por defecto, siete |
| Flexibilidad | Día 8 con ±7 días: la ventana va del 1 al 15 |

La ventana de fechas y la franja horaria (por ejemplo, de 8 a 12) pasan del contrato a cada orden, y el despacho las recibe como restricción.

Cómo se arman las órdenes es una decisión con costo. En el mismo sistema, varios tipos de problema en una recurrencia dan una sola orden, y varias recurrencias dan varias órdenes y más viajes; quien quiere atar el tiempo a cada equipo elige una orden por equipo. Un acuerdo se ejecuta en un solo lugar, y el trabajo en varias sucursales pide varios acuerdos.

## Quién recibe el servicio y quién paga

El contrato separa dos cuentas que en una venta común suelen coincidir. Según el mismo sistema, la cuenta de servicio «defines where the agreement work orders take place, while the billing account defines who the invoice should be sent to». Un ejemplo de la base: una cadena de locales con administración central, donde el técnico va a la sucursal y la factura va a la casa matriz. La relación entre cuentas y contactos está en [cuenta y contacto](../../Relacion-con-clientes/Registro-del-cliente/cuenta-y-contacto.md).

## Precio negociado y cobertura

El contrato fija precios propios. Según el sistema de referencia, los acuerdos «usually contain a negotiated price for goods and services that are reflected in an entirely new price list». La cobertura se modela aparte, como derechos («entitlements») que cambian el precio y no el costo: «Entitlements can't change the cost of a product or service, only the price».

Un derecho se aplica por cuenta de facturación, cuenta de servicio, producto o servicio, equipo, categoría de equipo o tipo de problema. Los ejemplos de la documentación son un 10 % de descuento sobre todo durante dos años y un 100 % durante dos años para los equipos de la categoría «Heating, Venting, and Air Conditioning». El descuento se aplica cuando el renglón de la orden pasa de estimado a usado; si dos derechos chocan, gana el de prioridad más alta y, si empatan, el más específico.

El mismo modelo tiene un límite que vale como advertencia de diseño: no admite cupos. «It's not possible to create an entitlement for 10 work orders or free service for the first hour.» Un contrato que promete «cuatro visitas incluidas» o «la primera hora sin cargo» necesita otro mecanismo.

## Qué se factura y la doble factura

Por criterio de la base, lo que el contrato no cubre se factura con la orden. En el sistema de referencia, el tiempo de trabajo es facturable por defecto, el descanso solo si la lista de precios lo dice, y el viaje entra como un producto más. En otro sistema, con facturación por tiempo y materiales, los productos cargados en la tarea pasan solos a la factura.

El riesgo propio del contrato es cobrar dos veces. Un acuerdo puede emitir su factura periódica y, además, cada orden que genera factura al cerrarse: «Even if an agreement generates invoices, agreement work orders create invoices upon completion [...]». Si solo vale la cuota, hay que apagar la factura de la orden o llevarla a cero con la lista de precios y los derechos. La factura y la cuenta a cobrar son de [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md).

## El tiempo de respuesta prometido

Un contrato puede prometer tiempos, y esa promesa tiene nombre: el acuerdo de nivel de servicio (SLA). Según una enciclopedia, es «an agreement, typically a binding contract, between a service provider and a customer», que fija el tiempo de respuesta («the period by which the service provider will start the investigation of the issue»), el plazo de resolución, la disponibilidad y a veces el MTTR y el MTBF, que se definen en [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md). Si se incumple, el cliente puede pedir compensación o terminar; en tercerización, con «financial penalties».

En el sistema de referencia leído, el SLA como objeto vive en la atención, sobre el caso y no sobre la orden de campo: mide la primera respuesta o la resolución, con horario hábil opcional, pausa mientras el caso espera y estados como «Nearing noncompliance» o «Noncompliant». Del lado del dueño del equipo, APQC tiene 10.3.2.7 «Monitor maintenance performance against targets/contracts».

> [!NOTE] Sin fuente todavía: el tiempo de respuesta y de resolución en sitio como cláusula del contrato de campo (por ejemplo, «técnico en 4 horas»), y la cobertura por tipo de costo (repuestos, mano de obra, viaje) que diferencia un contrato completo de uno solo de mano de obra. Ninguna fuente leída los describe.
