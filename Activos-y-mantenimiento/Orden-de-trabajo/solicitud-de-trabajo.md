---
resumen: >-
  La solicitud de trabajo es el aviso de que un equipo necesita atención: alguien ve una falla, un ruido o una pérdida y lo registra. Es un pedido, no una autorización; mantenimiento lo evalúa, decide si se convierte en orden de trabajo y con qué prioridad.
estado: borrador
estabilidad: semi
fuentes:
  - "Odoo 17, Maintenance requests (campos y prioridad): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html"
  - "SAP Help 4.6C, aviso pendiente y liberación de la orden, según el buscador: https://help.sap.com/saphelp_46c/helpdata/en/de/957177415611d1893d0000e8323c4f/content.htm"
  - "SAP Help, avisos asignados a una orden siguen su estado, según el buscador: https://help.sap.com/doc/b183ce53118d4308e10000000a174cb4/700_SFIN3E%20006/en-US/238bb6535fe6b74ce10000000a174cb4.html"
  - "IBM, Maximo Manage, Work order statuses: https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=orders-work-order-statuses"
  - "Microsoft Learn, Overview of Dynamics 365 Field Service (2026-11-23): https://learn.microsoft.com/en-us/dynamics365/field-service/overview"
  - "Wikipedia, Corrective maintenance (cita la NF EN 13306): https://en.wikipedia.org/wiki/Corrective_maintenance"
  - "Wikipedia, Work order: https://en.wikipedia.org/wiki/Work_order"
  - "D. Palmer, principios de programación, según resúmenes de Plant Services (Palmer's Planning Corner): https://www.plantservices.com/voices/palmers-planning-corner/article/55361071/do-you-know-the-purpose-and-principles-of-maintenance-planning-and-scheduling"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.1.5 y 10.3.3.4: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/orden-de-trabajo.md, tercera-ronda.md, apqc-10.md y servicio-de-campo.md"
aliases: [solicitud de trabajo, aviso, aviso de mantenimiento, pedido de trabajo, pedido de mantenimiento, solicitud de mantenimiento, work request, maintenance request, maintenance notification, notificación de avería]
creado: 2026-11-27
revisado:
---

# Solicitud de trabajo

La solicitud de trabajo es el aviso de que un equipo necesita atención: alguien ve una falla, un ruido o una pérdida y lo registra. Es un pedido, no una autorización; mantenimiento lo evalúa, decide si se convierte en orden de trabajo y con qué prioridad.

Es la puerta de entrada del trabajo no planificado a la [orden de trabajo](orden-de-trabajo.md). El trabajo planificado entra por otro lado: lo genera el plan de [mantenimiento preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) sin que nadie lo pida. APQC 7.4 tiene un proceso para cada mitad de esta nota: 10.3.3.4 «Identify unplanned maintenance requirements» (darse cuenta de que algo hace falta) y 10.3.1.5 «Identify work management tasks & priorities» (decidir qué se hace y en qué orden).

## Quién levanta el aviso

Lo levanta, en la práctica de la base, quien está cerca del equipo: el operador que lo usa, el técnico que hace una ronda de inspección, el supervisor de producción. En un sistema de servicio de campo el trabajo además llega desde casos de atención, pedidos de venta, correos, llamadas, contratos, portales web y datos de sensores; allí los agentes de atención «triage incoming requests and determine when to create work orders for onsite visits». Ese triage es la frontera con el tema [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md), y lo que pasa después está en [servicio de campo](../Servicio-de-campo/servicio-de-campo.md).

Un aviso útil dice tres cosas: qué equipo, qué se observó y desde cuándo. El equipo se elige del [registro de activos](../Registro-de-activos/registro-de-activos.md), no se escribe a mano; si no, el aviso no llega al [historial del equipo](../Registro-de-activos/historial-del-equipo.md). Lo observado es el síntoma con palabras de quien lo vio, no un diagnóstico. Estas tres condiciones son criterio de la base.

## Aviso y orden: dos documentos o uno

Separar el aviso de la orden permite que muchos pidan y pocos autoricen. Un ERP de gran empresa crea el aviso con estado «aviso pendiente» y la orden aparte; varios avisos pueden quedar asignados a una misma orden y seguir su estado. Un sistema de gestión para pymes, en cambio, usa un solo documento, la «solicitud de mantenimiento», para pedir y para hacer, con un campo que dice si es correctiva o preventiva. Las dos formas están en [orden de trabajo](orden-de-trabajo.md).

Cuando hay un solo documento, la evaluación queda dentro de la orden como un estado. Un sistema de mantenimiento de referencia abre la orden «waiting for approval» y la pasa a aprobada, «the work can begin», o a cancelada. Una enciclopedia lo dice en términos generales: las órdenes se suelen revisar y programar antes de ejecutarse.

## Evaluar y aprobar

Evaluar un aviso es contestar unas pocas preguntas antes de gastar horas en planificarlo. Las que siguen son criterio de la base:

1. ¿Ya hay un aviso o una orden abierta por lo mismo? Los duplicados son frecuentes cuando varios operadores ven la misma falla.
2. ¿Es mantenimiento? Un cambio de diseño, una mejora o una instalación nueva es un proyecto, no una reparación.
3. ¿Hay riesgo para las personas o el ambiente? Si lo hay, va antes que todo y puede exigir parar el equipo ya.
4. ¿Quién paga y quién aprueba? Un monto o un tipo de trabajo puede necesitar la firma de alguien fuera de mantenimiento.

Aprobar no es programar. La orden aprobada entra al pendiente y espera que la [planificación](planificacion-y-programacion.md) la deje lista.

## La prioridad

La prioridad dice qué se hace primero cuando no alcanza la gente para todo, que es el caso normal. La norma europea de terminología, según una enciclopedia que la cita, distingue el correctivo inmediato, que «starts immediately after a failure», del diferido, cuyo trabajo «is delayed in conformance to a given set of maintenance rules». Para la base, esa es la primera decisión de prioridad: ¿se para todo o entra al pendiente?

Dentro del pendiente, la prioridad tiene que ser creíble. Palmer, según los resúmenes de sus principios, pide «un sistema de prioridades creíble» como condición para programar. El riesgo, según la base, es la inflación: si todo aviso llega como urgente, la prioridad deja de ordenar. Un sistema para pymes muestra el otro extremo: su prioridad, de cero a tres estrellas, solo ordena el tablero («Requests assigned a higher priority appear above those with a lower priority»), sin regla de urgencia ni de impacto.

La base deriva la prioridad de dos datos: cuánto importa el equipo, que está en [criticidad](../Registro-de-activos/criticidad.md), y cuánto apura la falla. Esa combinación es criterio de la base.

> [!NOTE] Sin fuente todavía: matrices de prioridad de órdenes (urgencia por criticidad), sus niveles típicos y los tiempos de atención asociados a cada nivel.
