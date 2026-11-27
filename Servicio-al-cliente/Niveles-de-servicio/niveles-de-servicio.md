---
resumen: >-
  El acuerdo de nivel de servicio es la promesa documentada de una empresa a su cliente sobre qué servicio le da y con qué nivel; en la atención, en cuánto tiempo se responde y se resuelve cada caso según su prioridad. La vertical cubre qué se promete, cómo corre el reloj, qué pasa cuando se vence y qué acuerdos internos lo sostienen.
estado: borrador
estabilidad: estable
fuentes:
  - "ITIL 4, definición de service level agreement, citada por BMC: https://www.bmc.com/blogs/ola/ (según resumen; el glosario oficial es pago y no se leyó)"
  - "InvGate, «Service level management in an ITIL 4 world»: https://blog.invgate.com/service-level-management-in-an-itil-4-world (según su resumen)"
  - "Advisera, «SLAs, OLAs and UCs in ITIL and ISO 20000»: https://advisera.com/20000academy/knowledgebase/slas-olas-ucs-itil-iso-20000 (según su resumen)"
  - "APQC, Process Classification Framework, categoría «Manage Customer Service» (6.0), 6.1.5, copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/6-manage-customer-service"
  - "ISO 18295-1:2017, índice (cláusula 9 y Anexo B): https://www.din.de/de/mitwirken/normenausschuesse/nadl/veroeffentlichungen/wdc-beuth:din21:276760944/toc-2704082/download (solo el índice)"
  - "ERPNext, Service Level Agreement: https://docs.frappe.io/erpnext/user/manual/en/service-level-agreement (como evidencia de práctica)"
  - "Odoo 19.0, Helpdesk, SLA: https://www.odoo.com/documentation/19.0/applications/services/helpdesk/overview/sla.html (como evidencia de práctica, según resumen del buscador)"
  - "Servicio-al-cliente/.investigacion/canales-y-niveles-de-servicio.md, secciones 4 a 6"
  - "Servicio-al-cliente/.investigacion/fundamentos-y-contraria.md, secciones 1 y 5"
aliases: [acuerdo de nivel de servicio, SLA, service level agreement, niveles de servicio, gestión de niveles de servicio, service level management, SLM, política de nivel de servicio]
creado: 2026-11-27
revisado:
---

# Niveles de servicio

El acuerdo de nivel de servicio es la promesa documentada de una empresa a su cliente sobre qué servicio le da y con qué nivel; en la atención, en cuánto tiempo se responde y se resuelve cada caso según su prioridad. La vertical cubre qué se promete, cómo corre el reloj, qué pasa cuando se vence y qué acuerdos internos lo sostienen.

Dentro de [Servicio al cliente](../servicio-al-cliente.md), los niveles de servicio le ponen el reloj al [caso](../Caso/caso.md). La prioridad que sale de la [clasificación y prioridad](../Caso/clasificacion-y-prioridad.md) elige qué objetivo de tiempo le toca; el [escalamiento](../Escalamiento/escalamiento.md) es lo que se hace cuando el caso no avanza dentro de ese tiempo; y [Calidad del servicio](../Calidad-del-servicio/calidad-del-servicio.md) mide si cumplir el acuerdo dejó conforme al cliente. Qué conviene prometer, visto desde el cliente, está en [gestión de las promesas](../../Marketing/Servicio-y-relacion/gestion-de-las-promesas.md) y en [expectativas y zona de tolerancia](../../Marketing/Servicio-y-relacion/expectativas-y-zona-de-tolerancia.md); acá está cómo se escribe la promesa y cómo se cronometra.

## Qué es el acuerdo de nivel de servicio

ITIL 4, según la cita que hace un proveedor de su glosario, define el acuerdo de nivel de servicio (SLA) como «A documented agreement between a service provider and a customer that identifies both services required and the expected level of service». La práctica que lo administra, la gestión de niveles de servicio, tiene como propósito, según el mismo tipo de resumen, «to set clear business-based targets for service levels, and to ensure that delivery of services is properly assessed, monitored, and managed against these targets». El texto oficial de ITIL es pago y no se leyó.

El acuerdo no es exclusivo de la mesa de ayuda de sistemas. La copia consultada del marco de APQC pone dentro de la estrategia de servicio al cliente el paso 6.1.5 «Establish target service level for each customer segment»: un objetivo por segmento de clientes, no uno solo para todos. ISO 18295-1, la norma de centros de contacto, dedica la cláusula 9 y el Anexo B a la relación entre el centro y la empresa que lo contrata, que es donde un acuerdo así se escribe cuando la atención está tercerizada.

## Tres cosas que se llaman nivel

En el tema, «nivel» tiene tres sentidos, y la vertical usa solo uno:

- El **acuerdo de nivel de servicio** promete al cliente tiempos por caso: es el de esta vertical.
- El **nivel de servicio del centro de contacto** es el porcentaje de contactos atendidos antes de un tiempo (por ejemplo, 80% en 20 segundos). Es un objetivo de espera en la cola y vive en [dimensionamiento del equipo](../Canales-de-atencion/dimensionamiento-del-equipo.md).
- Los **niveles de soporte** (primer, segundo y tercer nivel) dicen quién atiende, y están en [niveles de soporte](../Escalamiento/niveles-de-soporte.md).

Un centro puede atender el 80% de las llamadas en 20 segundos y vencer los casos de su acuerdo, y al revés. El [glosario](../Fundamentos/glosario-de-servicio-al-cliente.md) los separa con su nombre en inglés.

## Qué lleva un acuerdo

Las guías secundarias coinciden en una lista: los servicios que cubre, los objetivos, el horario en que rige, las responsabilidades de cada parte y cómo y cuándo se revisa. Son todas de una misma familia de blogs que resumen ITIL.

> [!NOTE] Sin fuente todavía: una fuente primaria sobre qué lleva un acuerdo de nivel de servicio.

En la atención, el núcleo del acuerdo son dos tiempos por prioridad: el de **primera respuesta** y el de **resolución**. Cómo se cuentan, con el horario de atención, los feriados y las pausas, está en [tiempos de respuesta y resolución](tiempos-de-respuesta-y-resolucion.md).

## Cómo lo modela un sistema

Dos sistemas de gestión independientes modelan el acuerdo con las mismas piezas: una política con objetivos de respuesta y resolución por prioridad, un calendario de atención, una lista de feriados y unos estados del caso que pausan el reloj. Uno de ellos admite que varias políticas apliquen al mismo caso y muestra el vencimiento más próximo. La lectura de esta base es que esas piezas son del dominio y no de un producto, porque aparecen en los dos sin relación entre ellos.

El modelo mínimo, entonces, es este: el acuerdo (a quién aplica: un cliente, un segmento, un tipo de caso), sus objetivos por prioridad, el calendario que usa y los estados que pausan. Cada caso guarda qué acuerdo le tocó y sus vencimientos calculados, para que un cambio posterior del acuerdo no reescriba la historia (lectura de esta base).

## Cómo falla un acuerdo

Falla de dos maneras opuestas. La primera es el vencimiento: el caso supera el tiempo prometido, y lo que se hace entonces (alertas, escalamiento, compensaciones) está en [incumplimiento del acuerdo](incumplimiento-del-acuerdo.md). La segunda es más difícil de ver: el acuerdo se cumple y el cliente igual está disconforme, porque se midió el manejo del caso y no el resultado. Es el llamado efecto «watermelon», verde por fuera y rojo por dentro, también en [incumplimiento del acuerdo](incumplimiento-del-acuerdo.md).

Falla también cuando se promete al cliente un tiempo que los equipos de atrás no se comprometieron a cumplir: el segundo nivel, otra área o un proveedor. Eso lo resuelven los [acuerdos internos](acuerdos-internos.md).

Los plazos de respuesta que fija la ley argentina están en [Servicio al cliente en la Argentina](../servicio-al-cliente-en-argentina.md).

## Qué hay en los niveles de servicio

- [Tiempos de respuesta y resolución](tiempos-de-respuesta-y-resolucion.md) — la primera respuesta, la resolución y el reloj: horario de atención, feriados y pausas por estados de espera.
- [Incumplimiento del acuerdo](incumplimiento-del-acuerdo.md) — el vencimiento, las alertas, los créditos y penalidades (sin fuente todavía) y el tablero verde con el cliente enojado.
- [Acuerdos internos](acuerdos-internos.md) — el acuerdo de nivel operativo entre equipos y el contrato de respaldo con un proveedor, que sostienen el que se le da al cliente.
