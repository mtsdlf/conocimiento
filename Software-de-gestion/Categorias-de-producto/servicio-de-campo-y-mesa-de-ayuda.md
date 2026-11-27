---
resumen: >-
  La mesa de ayuda y la gestión del servicio de campo son dos categorías de software de la posventa: la primera registra y sigue los casos que abren los clientes; la segunda programa, despacha y sigue a los técnicos que van a casa del cliente. El mercado las vende por separado, y se tocan cuando un caso necesita una visita.
estado: vigente
estabilidad: estable
fuentes:
  - "Wikipedia, «Field service management» (leída; secundaria, con aviso de falta de citas): https://en.wikipedia.org/wiki/Field_service_management"
  - "Gartner, Market Guide for Field Service Management, marzo de 2025 (resumen): https://www.gartner.com/en/documents/6311147"
  - "Gartner, cuadrantes de CRM (automatización de ventas, julio de 2025, y centro de atención al cliente, octubre de 2025), según resúmenes: https://www.gartner.com/en/documents/6747034 y https://www.cxtoday.com/crm/gartner-magic-quadrant-for-sales-force-automation-platforms-sfa-2025-the-rundown/"
  - "Documentación de aplicaciones de un ERP de código abierto, versión 18.0 (leída): https://www.odoo.com/documentation/18.0/applications.html"
  - "Lista de módulos de otro ERP de código abierto (leída): https://github.com/frappe/erpnext/blob/develop/erpnext/modules.txt"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y taxonomias-externas-96.md (2026-11-27)"
aliases: [mesa de ayuda, help desk, helpdesk, service desk, mesa de servicio, software de atención al cliente, customer service software, ticketing, sistema de tickets, FSM, field service management, gestión del servicio de campo, software de servicio de campo, ITSM, IT service management, gestión de servicios de TI]
creado: 2026-11-27
revisado: 2026-11-27
---

# Servicio de campo y mesa de ayuda

La mesa de ayuda y la gestión del servicio de campo son dos categorías de software de la posventa: la primera registra y sigue los casos que abren los clientes; la segunda programa, despacha y sigue a los técnicos que van a casa del cliente. El mercado las vende por separado, y se tocan cuando un caso necesita una visita.

Son parte de las [categorías de producto](categorias-de-producto.md). Esta base las junta en una nota porque el recorrido [del reclamo a la resolución](../../Procesos-de-negocio/del-reclamo-a-la-resolucion.md) pasa por las dos. El campo no las junta: los analistas las tienen en mercados distintos.

## Dos mercados, dos dominios

| | Mesa de ayuda | Gestión del servicio de campo |
|---|---|---|
| Qué registra | El caso: lo que pidió el cliente, su prioridad, su dueño y su reloj | La orden de servicio: el técnico, la agenda, el viaje, los repuestos, la conformidad |
| Dominio de esta base | [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md) | [Servicio de campo](../../Activos-y-mantenimiento/Servicio-de-campo/servicio-de-campo.md), en Activos y mantenimiento |
| Cómo lo evalúa Gartner (según resúmenes) | Dentro del CRM, como suites de centro de atención al cliente (octubre de 2025) | Guía de mercado propia (marzo de 2025); el último cuadrante encontrado es de 2022 |

Los productos tampoco coinciden. La documentación de un ERP de código abierto pone mesa de ayuda y servicio de campo en una misma familia de servicios, junto con proyectos y horas, pero deja las reparaciones en la de cadena de suministro. Otro ERP de código abierto tiene un módulo de soporte y lleva las visitas dentro del de mantenimiento.

## La mesa de ayuda y su vecina, la de sistemas

La mesa de ayuda se vende de dos maneras. Una atiende a clientes: lleva el [caso](../../Servicio-al-cliente/Caso/caso.md), su [escalamiento](../../Servicio-al-cliente/Escalamiento/escalamiento.md) y sus [niveles de servicio](../../Servicio-al-cliente/Niveles-de-servicio/niveles-de-servicio.md). La otra atiende a los empleados de la propia empresa cuando falla un sistema, y es la gestión de servicios de TI (ITSM), ordenada por ITIL desde fines de los ochenta, como cuenta la [historia del servicio al cliente](../../Servicio-al-cliente/Fundamentos/historia-del-servicio-al-cliente.md). Las dos comparten el registro (el caso o el incidente, la prioridad, el reloj, el escalamiento por niveles); cambia quién pide y qué se le promete.

Esta base trata solo la primera. La gestión de servicios de TI no lleva un dominio de negocio de los que trata esta base, aunque los proveedores grandes la venden junto con el resto; queda con lo que [no es categoría en este tema](categorias-de-producto.md#lo-que-no-es-categoría-en-este-tema). La atención al cliente, además, se compra muchas veces dentro del [CRM](crm.md), y entonces el caso queda junto al historial comercial del cliente.

## El servicio de campo como software

Wikipedia define la gestión del servicio de campo como la de los recursos de una empresa «employed at or en route to the property of clients, rather than on company property»: ubicar vehículos, programar y despachar el trabajo, y enlazarlo con el inventario, la facturación y la contabilidad. El ciclo de la orden de servicio (crear, programar, despachar, ejecutar, aprobar, facturar) ya está en [servicio de campo](../../Activos-y-mantenimiento/Servicio-de-campo/servicio-de-campo.md); lo propio del software es el despacho con agenda y ruteo, que está en [despacho y agenda](../../Activos-y-mantenimiento/Servicio-de-campo/despacho-y-agenda.md), y la aplicación del técnico en la calle.

Gartner dice, según el resumen de su guía de 2025, que el mercado «is integrating adjacent technologies». En la lectura de esta base, eso lo acerca a dos vecinas: el [EAM y el CMMS](eam-y-cmms.md), porque el ciclo de la [orden de trabajo](../../Activos-y-mantenimiento/Orden-de-trabajo/orden-de-trabajo.md) es el mismo aunque el equipo sea del cliente, y el [PSA](psa.md), cuando el servicio en casa del cliente es lo que la empresa vende.

## Dónde se tocan las dos: la derivación al técnico

Las dos cajas se encuentran en un punto: el caso que no se resuelve a distancia y [se deriva al técnico](../../Servicio-al-cliente/Escalamiento/derivacion-al-tecnico.md). La mesa de ayuda crea la orden de servicio; la orden vuelve al caso cuando se cierra, para que la atención le conteste al cliente. Si las dos son productos distintos, ese ida y vuelta es una integración, y la pregunta es quién es dueño del estado que ve el cliente (lectura de esta base).

## Cómo se integran con el ERP

Según Wikipedia, el software de servicio de campo suele integrarse con «backend systems such as service management, billing, accounting, parts inventory, and other HR systems». Para esta base, las tres conexiones con el [ERP](erp.md) son los repuestos que salen del stock, la factura por mano de obra y repuestos que cubre o no el contrato, y las horas del técnico para la nómina. La mesa de ayuda necesita menos del ERP: el cliente, lo que compró y su garantía. Cómo se arma cada conexión está en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md).

> [!NOTE] Sin fuente todavía: una fuente específica sobre la mesa de ayuda como categoría de software (no se buscó; la fuente natural es ITIL, que no se leyó), y una definición primaria de la gestión del servicio de campo (la de Wikipedia es secundaria y su referencia a Gartner está rota).
