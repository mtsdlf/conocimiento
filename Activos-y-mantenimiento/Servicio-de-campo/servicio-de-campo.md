---
resumen: >-
  El servicio de campo es el mantenimiento que una empresa hace sobre equipos de sus clientes, en el lugar donde están: instalarlos, mantenerlos y repararlos. Usa el mismo ciclo de orden de trabajo que el mantenimiento interno y le suma lo que trae que el equipo sea de otro: el contrato, el viaje, la conformidad del cliente y el cobro.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 6.3 «Service products after sales», 5.0 «Deliver Service» y 10.3 «Maintain assets»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Microsoft Learn, Overview of Dynamics 365 Field Service, 2026-11-23: https://learn.microsoft.com/en-us/dynamics365/field-service/overview"
  - "Microsoft Learn, Work order lifecycle and system statuses, 2026-08-10: https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status"
  - "Microsoft Learn, Set up customer agreements to generate work orders, 2026-03-02: https://learn.microsoft.com/en-us/dynamics365/field-service/set-up-agreements-work-orders"
  - "Wikipedia, Field service management (secundaria, con «citation needed»): https://en.wikipedia.org/wiki/Field_service_management"
  - "Cohen, Agrawal y Agrawal, «Winning in the Aftermarket», Harvard Business Review, mayo de 2006 (solo el resumen público): https://hbr.org/2006/05/winning-in-the-aftermarket"
  - "Activos-y-mantenimiento/.investigacion/servicio-de-campo.md (rondas 1 y 2)"
  - "Activos-y-mantenimiento/.investigacion/apqc-10.md"
aliases: [servicio de campo, field service, field service management, FSM, gestión del servicio de campo, servicio técnico, servicio técnico a domicilio, servicio posventa, after-sales service, service products after sales]
creado: 2026-11-27
revisado:
---

# Servicio de campo

El servicio de campo es el mantenimiento que una empresa hace sobre equipos de sus clientes, en el lugar donde están: instalarlos, mantenerlos y repararlos. Usa el mismo ciclo de orden de trabajo que el mantenimiento interno y le suma lo que trae que el equipo sea de otro: el contrato, el viaje, la conformidad del cliente y el cobro.

Es una de las cinco partes de [Activos y mantenimiento](../activos-y-mantenimiento.md). Toma de [Orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) el documento y sus estados, y de [Registro de activos](../Registro-de-activos/registro-de-activos.md) la idea de un registro por equipo con su historial. Una enciclopedia la define como la gestión de los recursos de una empresa «employed at or en route to the property of clients, rather than on company property», propia de las firmas que instalan, mantienen o reparan equipos. La documentación de un sistema de referencia da como ejemplos de trabajo por contrato el mantenimiento trimestral de ascensores y el control de plagas semanal.

## Lo que cambia cuando el equipo es del cliente

El trabajo técnico es el mismo; cambian cinco cosas alrededor. Los sistemas de servicio de campo las muestran en su modelo de datos: el trabajo ocurre «at customer locations», el equipo del cliente y su historial se llevan aparte, y la orden carga la mano de obra «to bill to the customer».

| Qué cambia | En el mantenimiento interno | En el servicio de campo |
|---|---|---|
| De quién es el equipo | De la empresa, y suele estar también en su contabilidad | Del cliente: se registra en la [base instalada](base-instalada.md), sin contraparte contable |
| Qué dice qué hacer | El plan preventivo y la criticidad | El [contrato de servicio](contrato-de-servicio.md), que fija cobertura, precio y visitas |
| Cómo se llega | El técnico ya está en la planta | Hay un viaje, con tiempo, distancia y a veces un cargo propio |
| Quién da por bueno el trabajo | El supervisor o el área que pidió | El cliente, con su firma o su comentario al cierre de la [visita](visita-tecnica.md) |
| Qué pasa después del cierre | Se imputa el costo | Se factura al cliente según lo que cubra el contrato |

La columna del mantenimiento interno es criterio de la base, por contraste. La de servicio de campo sale de la documentación de un sistema de referencia: en ella el viaje se registra como estado («Traveling»), con distancia y duración, y se agrega a la orden como un producto cuando la cuenta del cliente tiene cargo de viaje.

## Del caso del cliente a la factura

El servicio de campo empieza cuando alguien decide que hace falta ir. La atención, el caso, el reclamo y el escalamiento son del tema [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md); este tema empieza cuando el caso [deriva a un técnico](../../Servicio-al-cliente/Escalamiento/derivacion-al-tecnico.md), y el cierre de la orden vuelve al caso. Allí los agentes, según un sistema de referencia, «triage incoming requests and determine when to create work orders for onsite visits». Que el cierre vuelva al caso para que la atención le conteste al cliente es decisión del mapa de la base.

El ciclo típico, según el mismo sistema, tiene estos pasos y estos responsables:

1. Crear la orden de servicio. La crea la atención si viene de un caso, el contrato si es una visita recurrente o ventas si viene de un pedido. También puede nacer de un mail, un llamado, un portal o un sensor.
2. Programar y despachar. El despachante, el propio técnico o un motor de ruteo le asignan técnico y horario; está en [despacho y agenda](despacho-y-agenda.md).
3. Hacer el servicio. El técnico viaja, trabaja y cierra su [visita](visita-tecnica.md).
4. Revisar y aprobar. Un supervisor o alguien de administración revisa la orden completada.
5. Facturar y ajustar el inventario. La orden pasa a un estado de contabilizada («Posted») que dispara la factura por repuestos y mano de obra.

El cobro es un paso aparte de la ejecución, hecho por otra persona. La factura y la cuenta a cobrar son de [Contabilidad](../../Contabilidad/contabilidad.md), en [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md); la venta del contrato, de [Relación con clientes](../../Relacion-con-clientes/relacion-con-clientes.md).

## Dónde lo pone APQC y por qué la base lo pone acá

APQC, en su marco de procesos 7.4 (2024), no pone el servicio técnico sobre productos vendidos junto al mantenimiento. Lo pone en 6.0 «Manage Customer Service», proceso 6.3 «Service products after sales», que incluye 6.3.1 «Register products», 6.3.2 «Process warranty claims» (con 6.3.2.3.2 «Schedule field service») y 6.3.4 «Service products». Dentro de este último están 6.3.4.1.3 «Generate service order», 6.3.4.2 «Identify and schedule resources to meet service requirements» y 6.3.4.3.2 «Execute product repair».

No está en 5.0 «Deliver Service». Por los títulos de sus procesos, como «Review contract and agreed terms», 5.0 trata la entrega de servicios por contrato o proyecto, no la reparación en casa del cliente; es una lectura de los títulos, sin las definiciones de APQC. El mantenimiento de los activos propios está en 10.3 «Maintain assets». Es lectura de la base, que el marco no declara, que 10.3 describe el lado de quien posee el equipo y 6.3.4 el lado de quien presta el servicio.

La base lo pone en este tema por criterio propio, no por APQC: el ciclo de la [orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) es el mismo aunque cambie el dueño del equipo, y separarlo obligaría a explicar dos veces la solicitud, la programación, los repuestos y el cierre. La atención y el reclamo, que APQC también tiene en 6.0, quedan en Servicio al cliente.

## Reactivo, por contrato o por condición

Un sistema de referencia distingue cuatro maneras de que nazca el trabajo de campo, que la base hace corresponder, por criterio propio, con las de la [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md):

- Reactivo («break-fix»): «a customer reports an issue, a customer service agent creates a work order, and a dispatcher schedules a technician».
- Preventivo por contrato: «scheduled maintenance happens on a recurring basis through agreements»; el [contrato de servicio](contrato-de-servicio.md) genera las órdenes como lo hace un plan de [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md).
- Predictivo, por datos de sensores (IoT): la estrategia está en [mantenimiento por condición](../Estrategia-de-mantenimiento/mantenimiento-por-condicion.md).
- Por proyecto: una instalación o un trabajo con principio y fin.

Por qué importa el negocio de posventa lo plantean Cohen, Agrawal y Agrawal en Harvard Business Review (2006). Según su resumen público, los ejecutivos temen que la mayoría de las empresas «either don't know how or don't care to provide after-sales services effectively», y la alta gerencia lo trata como «a mere afterthought». El cuerpo del artículo no se leyó.

> [!NOTE] Sin fuente todavía: cómo separan el mercado los analistas (gestión de servicio de campo frente a centro de atención al cliente) y la servitización como concepto.

## Qué hay en Servicio de campo

- [Base instalada](base-instalada.md): el registro de cada equipo del cliente, con su número de serie, su ubicación y la cobertura que se deriva de él.
- [Contrato de servicio](contrato-de-servicio.md): garantía frente a contrato, qué cubre, cómo genera las visitas preventivas y qué se factura.
- [Despacho y agenda](despacho-y-agenda.md): cómo se asigna cada orden a un técnico y a una ventana, la orden frente a la visita y el ruteo.
- [Visita técnica](visita-tecnica.md): la orden en la casa del cliente, el stock de la camioneta, la conformidad, el cierre parcial y resolver en la primera visita.
