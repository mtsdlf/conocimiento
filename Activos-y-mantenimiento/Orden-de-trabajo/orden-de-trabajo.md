---
resumen: >-
  La orden de trabajo es el documento que autoriza y lleva un trabajo de mantenimiento sobre un equipo, desde que alguien lo pide hasta que se cierra con lo que se hizo, lo que se usó y lo que costó. Pasa por estados que separan pedir, aprobar, preparar, ejecutar, terminar el trabajo físico y cerrar el registro.
estado: borrador
estabilidad: estable
fuentes:
  - "IBM, Maximo Manage, Work order statuses (estados y transiciones): https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=orders-work-order-statuses"
  - "SAP Help, System Status for Orders (estados de la orden y sus efectos) [M]: https://help.sap.com/doc/saphelp_sfin100/1.9/en-US/29/cab65334e6b54ce10000000a174cb4/content.htm"
  - "SAP Help, Changing the System Status in the Order (técnicamente concluida, cerrada, avisos asignados) [M]: https://help.sap.com/doc/saphelp_sfin100/1.9/en-US/88/16295411158c24e10000000a4450e5/content.htm"
  - "SAP Help, Notifications and Task Lists in Maintenance Orders (avisos asignados a la orden) [M]: https://help.sap.com/doc/saphelp_sfin100/1.9/en-US/91/d92354f6f28c24e10000000a4450e5/content.htm"
  - "Activos-y-mantenimiento/.investigacion/verificacion-orden-de-trabajo.md"
  - "Odoo 17, Maintenance requests: https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html"
  - "ERPNext, Asset Maintenance: https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance"
  - "OSHA, 29 CFR 1910.147, The control of hazardous energy (lockout/tagout): https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147"
  - "Microsoft Learn, Dynamics 365 Field Service, Work order lifecycle and system statuses (2026-08-10): https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.1 y 10.3.2: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/orden-de-trabajo.md, tercera-ronda.md, apqc-10.md y servicio-de-campo.md"
aliases: [orden de trabajo, OT, orden de mantenimiento, work order, WO, maintenance work order, ciclo de la orden de trabajo, work order lifecycle, gestión del trabajo, work management]
creado: 2026-11-27
revisado:
---

# Orden de trabajo

La orden de trabajo es el documento que autoriza y lleva un trabajo de mantenimiento sobre un equipo, desde que alguien lo pide hasta que se cierra con lo que se hizo, lo que se usó y lo que costó. Pasa por estados que separan pedir, aprobar, preparar, ejecutar, terminar el trabajo físico y cerrar el registro.

Es el centro de [Activos y mantenimiento](../activos-y-mantenimiento.md). Se abre siempre sobre un equipo o una ubicación técnica del [registro de activos](../Registro-de-activos/registro-de-activos.md); la genera un plan de [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) o la pide una [solicitud de trabajo](solicitud-de-trabajo.md); y al cerrarse escribe el [historial del equipo](../Registro-de-activos/historial-del-equipo.md), de donde salen los [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md). Es la misma orden cuando el equipo es de un cliente: [servicio de campo](../Servicio-de-campo/servicio-de-campo.md) usa este ciclo y explica solo lo que cambia.

## Qué dice una orden

Una orden dice sobre qué equipo se trabaja, qué tipo de trabajo es, quién lo hace, cuándo y con qué prioridad. Un sistema de gestión para pymes guarda, en su forma mínima: título, equipo o centro de trabajo, fecha del pedido (que no se edita), tipo (correctivo o preventivo), equipo responsable y persona, fecha programada y duración, si bloquea el centro de trabajo, prioridad e instrucciones. Una orden completa suma lo que agregan la [planificación](planificacion-y-programacion.md) (tareas, horas estimadas, oficios), los [repuestos y materiales](repuestos-y-materiales.md) y el [cierre](cierre-de-la-orden.md) (horas reales, consumos, falla, costo); esa lista ampliada es criterio de la base.

El marco de procesos de APQC (versión 7.4, 2024) reparte el ciclo en dos grupos: planificar (10.3.1, con «Identify work management tasks & priorities» y «Create work plans») y gestionar (10.3.2, con «Schedule maintenance work», «Obtain required resources», «Update work and asset records» y «Manage maintenance work safety»). La base los lee como los pasos que recorre la orden.

## Los estados de la orden

Un sistema de mantenimiento de referencia tiene esta tabla de estados. Lo que más enseña es que separa el trabajo físico terminado (terminada) de la orden cerrada, y que tiene estados de espera con causa:

| Estado | Qué significa según la fuente | Puede pasar a |
|---|---|---|
| Esperando aprobación | «waiting for approval» | aprobada, en curso, esperando materiales, esperando condición, terminada, cerrada, cancelada |
| Aprobada | «approved and the work can begin» | esperando aprobación, en curso, esperando materiales, esperando condición, terminada, cerrada, cancelada |
| Esperando programación | «waiting to be scheduled» | las mismas que aprobada |
| Esperando materiales | «Materials must arrive before the work can be performed» | en curso, terminada, esperando condición, esperando aprobación, cerrada, cancelada |
| Esperando condición de planta | «The work can be performed only when the condition of the plant is suitable» | en curso, terminada, esperando aprobación, cerrada, cancelada |
| En curso | «The work is in progress» | esperando materiales, terminada, esperando aprobación, cerrada |
| Terminada | «The physical work is completed» | solo cerrada |
| Cerrada | «The work order is closed» | solo editada en historia |
| Cancelada | «The work order is canceled» | ninguno |

Una orden cerrada solo se corrige pasando por un estado especial de edición en el historial. Esta fuente no usa las palabras «cierre técnico» y «cierre administrativo»; la del ERP de más abajo sí distingue completar «técnicamente» y completar «para el negocio».

Un ERP de gran empresa hace el mismo corte con otros nombres. La orden se crea y, «after all the required information has been entered», se libera; al liberarla el sistema revisa la disponibilidad de materiales y herramientas y los permisos pendientes, y recién entonces se pueden retirar las reservas y cargar las horas. Después puede quedar parcialmente confirmada y finalmente confirmada. Técnicamente concluida es «complete for Plant Maintenance»: se borran las reservas y las capacidades pendientes, pero todavía se pueden imputar costos (por ejemplo, facturas de materiales entregados y usados) y liquidar. Concluida para el negocio es el estado final: ya no recibe ninguna imputación y queda bloqueada, y solo se puede liquidar si no se completó antes para el negocio. Además tiene estados de bloqueo y de «no ejecutada», que deja a la vista que el trabajo planificado no se hizo.

## Un documento o varios

Hay dos formas de modelar el pedido y el trabajo, y las dos se usan:

- Un solo documento que va del pedido al cierre. El sistema para pymes tiene una «solicitud de mantenimiento» con tres etapas: nueva, reparada y desechada (para lo irreparable). No tiene estados de aprobación, planificación ni cierre administrativo. Alcanza cuando quien pide y quien hace son casi la misma gente.
- Aviso y orden separados. El ERP de gran empresa crea primero un aviso, que tiene sus propios estados, y después una orden que lo atiende; los avisos asignados a la orden pueden seguir su estado: al concluir la orden, el sistema ofrece completar también los avisos asignados. Sirve cuando muchos piden, pocos aprueban y no todo aviso merece una orden. El aviso está en [solicitud de trabajo](solicitud-de-trabajo.md).

Un ERP abierto muestra una tercera división, por origen del trabajo: el preventivo es un plan con tareas y periodicidad que genera un registro por ocurrencia, que se completa o se cancela; lo no planificado va por otro documento, la reparación, que registra la falla, la parada, el costo y si el costo se capitaliza. Elegir entre las tres formas depende de cuántas personas intervienen y de si hace falta aprobar; es criterio de la base.

## La seguridad viaja en la orden

Trabajar sobre un equipo con energía exige aislarlo antes. En los Estados Unidos lo regula la norma OSHA 29 CFR 1910.147 (bloqueo y etiquetado): el empleador tiene que tener un programa de «energy control procedures, employee training and periodic inspections», con seis pasos antes de empezar (conocer la energía, apagar, aislar, bloquear o etiquetar, liberar la energía residual y verificar el aislamiento) y una inspección del procedimiento «at least annually». Que la orden referencie el procedimiento de bloqueo del equipo y registre la verificación es inferencia de la base, no de la norma.

> [!NOTE] Sin fuente todavía: el marco argentino de bloqueo y etiquetado y de permisos de trabajo. Lo obligatorio en la Argentina va en [mantenimiento obligatorio en la Argentina](../mantenimiento-obligatorio-en-argentina.md).

## La misma orden en casa del cliente

En el servicio de campo la orden es la misma y cambia el entorno. Un sistema de servicio de campo usa los estados sin programar, programada, en curso, terminada, contabilizada y cancelada, y separa la orden de la [visita](../Servicio-de-campo/visita-tecnica.md): «Work orders and bookings have independent lifecycles». El paso de terminada a contabilizada lo hace administración después de revisar, y dispara la factura: es el mismo corte entre trabajo hecho y orden cerrada.

## Las piezas del ciclo

- [Solicitud de trabajo](solicitud-de-trabajo.md) — el aviso: quién lo levanta, cómo se evalúa, se aprueba y se le pone prioridad.
- [Planificación y programación](planificacion-y-programacion.md) — preparar el trabajo (qué, cómo, con qué) y ponerle fecha y gente; el pendiente y el tiempo de herramienta.
- [Repuestos y materiales](repuestos-y-materiales.md) — qué pide la orden, los repuestos críticos, la reserva, el consumo y la espera por materiales.
- [Cierre de la orden](cierre-de-la-orden.md) — qué se registra al terminar, por qué un cierre malo arruina el historial y cómo pasa el costo a Contabilidad.
