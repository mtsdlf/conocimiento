---
resumen: >-
  Planificar una orden de trabajo es decidir qué se hace, cómo y con qué (tareas, horas, oficios, repuestos, herramientas); programarla es decidir cuándo y quién. Son dos trabajos distintos: el primero deja la orden lista, el segundo la pone en la semana de una cuadrilla, en el momento en que producción puede parar el equipo.
estado: vigente
estabilidad: semi
fuentes:
  - "D. Palmer, «Do you know the purpose and principles of maintenance planning and scheduling?», Palmer's Planning Corner, Plant Services, 3 de marzo de 2026 [M]: https://www.plantservices.com/voices/palmers-planning-corner/article/55361071/do-you-know-the-purpose-and-principles-of-maintenance-planning-and-scheduling"
  - "D. Palmer, «Understanding the math of maintenance planning and scheduling», Plant Services, 4 de marzo de 2019 [M]: https://plantservices.com/planned-maintenance/planning-and-scheduling/article/11295301/understanding-the-math-of-maintenance-planning-and-scheduling"
  - "D. Palmer, «Maintenance Scheduling Needs a Planned Backlog», Reliable Plant [M]: https://reliableplant.com/Articles/Print/7051?id=7051"
  - "IBM, Maximo Manage, Work order statuses: https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=orders-work-order-statuses"
  - "Odoo 17, Maintenance requests (fecha programada, duración, bloqueo del centro de trabajo): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html"
  - "SMRP, Best Practices, Metrics & Guidelines (la página pública dice que las definiciones y fórmulas son para socios; no leídas): https://www.smrp.org/learning-resources/smrp-library/best-practices-metrics-guidelines/"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.1.4, 10.3.1.6, 10.3.1.7 y 10.3.2.1: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/verificacion-orden-de-trabajo.md, orden-de-trabajo.md, tercera-ronda.md y apqc-10.md"
aliases: [planificación del mantenimiento, programación del mantenimiento, maintenance planning, maintenance scheduling, planning and scheduling, pendiente, backlog, trabajo pendiente, tiempo de herramienta, wrench time, cumplimiento del programa, schedule compliance, trabajo listo, ready backlog]
creado: 2026-11-27
revisado: 2026-11-27
---

# Planificación y programación

Planificar una orden de trabajo es decidir qué se hace, cómo y con qué (tareas, horas, oficios, repuestos, herramientas); programarla es decidir cuándo y quién. Son dos trabajos distintos: el primero deja la orden lista, el segundo la pone en la semana de una cuadrilla, en el momento en que producción puede parar el equipo.

Están entre la [solicitud de trabajo](solicitud-de-trabajo.md) aprobada y la ejecución de la [orden de trabajo](orden-de-trabajo.md). APQC 7.4 los pone en grupos distintos: «Conduct resource planning» (10.3.1.6) y «Create work plans» (10.3.1.7) dentro de planificar, y «Schedule maintenance work» (10.3.2.1) dentro de gestionar. Un sistema de gestión para pymes los junta en dos campos de la misma ficha, fecha programada y duración; según la base, alcanza mientras nadie se dedique solo a preparar trabajo.

## Qué hace el planificador y qué hace el programador

El planificador arma el paquete de trabajo de una orden: los pasos, las horas por oficio, los repuestos y las herramientas, los permisos y el procedimiento de bloqueo del equipo. Trabaja sobre lo que viene, no sobre la urgencia de hoy. El programador toma las órdenes ya preparadas, mira las horas disponibles de cada cuadrilla y las ventanas en que se puede parar cada equipo, y arma la semana. Esta división de tareas es criterio de la base. Palmer confirma parte de este reparto: los planificadores atienden el trabajo futuro, y «field supervisors take care of daily scheduling», con el control del bloqueo de energía. Una definición formal de los dos roles no se encontró en una fuente abierta.

Para la base, la diferencia importa porque las dos funciones compiten por la misma persona: si el planificador también atiende las fallas del día, las fallas ganan y el trabajo futuro nunca se prepara. Es inferencia.

## Los principios de Palmer

D. Palmer, autor del «Maintenance Planning and Scheduling Handbook», resume la práctica en una columna con doce principios, seis de planificación y seis de programación. Lo que sigue sale de esa columna, no del libro:

- De planificación: se protege a los planificadores de las tareas administrativas; se atiende el trabajo futuro; se guarda la retroalimentación de los técnicos, que cierra el ciclo de mejora; la estimación de tiempo es la de un técnico que sabe lo que hace en un trabajo sin problemas inusuales, sin tiempo de más «just in case»; el detalle del plan es el mayor posible sin impedir que se planifique todo el trabajo; y el tiempo de herramienta explica por qué se puede hacer más trabajo.
- De programación: planes con oficio y horas estimadas; un sistema de prioridades creíble, con más de tres niveles; la semana siguiente como horizonte; el programa cargado al 100 % de la mano de obra prevista; la programación diaria a cargo de los supervisores de campo; y el cumplimiento del programa. Palmer dice que la gerencia debe esperar entre 40 y 90 %: por debajo de 40 % suele ser que se ignoró el programa o era irreal, y por encima de 90 % suele ser que no se cargó al 100 %.

La retroalimentación de los técnicos es lo que conecta este componente con el [cierre de la orden](cierre-de-la-orden.md): lo que el técnico anota al terminar es lo que el planificador usa la próxima vez.

## El tiempo de herramienta

El tiempo de herramienta es, en la definición de la base, la parte de la jornada de un técnico en que efectivamente trabaja sobre el equipo, sin contar traslados, búsqueda de repuestos, esperas ni permisos. Según Palmer, en la mayoría de las plantas, aun en las buenas, es de solo 35 %, y una buena planificación y programación lo lleva a 55 %. La cuenta es «55/35 = 1.57», o sea un 57 % más de productividad con la misma gente: una fuerza que completa 1.000 órdenes por mes pasaría a completar 1.570. Palmer atribuye el salto a la programación más que a mejores planes de trabajo, y es una cifra de su experiencia, no un estudio. El argumento económico de tener planificadores sale de ahí.

> [!NOTE] Sin fuente todavía: la definición formal del tiempo de herramienta y del cumplimiento del programa de SMRP. Su página pública dice que cada métrica trae definición y fórmula, pero el texto es solo para socios.

## El pendiente y el trabajo listo

El pendiente es el conjunto de órdenes aprobadas que todavía no se hicieron. La base lo mide en horas o semanas de trabajo de la cuadrilla y no en cantidad de órdenes, porque una orden puede llevar una hora o una semana; ninguna fuente leída lo confirma. El pendiente planificado, el que ya tiene paquete de trabajo, es requisito para programar: Palmer lo llama «the first scheduling principle» y pide que los planificadores se mantengan por delante de las cuadrillas con al menos una semana de trabajo planificado.

Para la base, una orden está lista cuando se la puede ejecutar sin preguntar nada: está planificada, los repuestos están reservados o en el depósito, y hay acuerdo para parar el equipo. Un sistema de mantenimiento de referencia lo hace visible con estados de espera con causa: esperando programación, esperando materiales («Materials must arrive before the work can be performed») y esperando condición de planta («can be performed only when the condition of the plant is suitable»). Separar el pendiente total del pendiente listo es criterio de la base: el primero mide cuánto falta, el segundo cuánto se puede programar la semana que viene.

> [!NOTE] Sin fuente todavía: un rango de referencia del pendiente en semanas de cuadrilla y la proporción de trabajo planificado sobre el total.

## Parar el equipo: el acuerdo con producción

Para la base, casi todo el mantenimiento de una planta exige parar algo, y la ventana la decide producción. APQC lo nombra como proceso propio, «Integrate preventive maintenance into operations schedule» (10.3.1.4). Un sistema para pymes tiene un campo en la orden que bloquea el centro de trabajo; la base lo lee como la forma de que producción no le cargue trabajo mientras dura el mantenimiento.

El programa semanal es, como criterio de la base, una negociación: mantenimiento propone qué equipos necesita parar y cuánto tiempo, y producción dice cuándo. Programar la planta es del tema Producción, todavía no armado; acá queda el lado de mantenimiento. Qué equipos se pueden esperar y cuáles no lo dice su [criticidad](../Registro-de-activos/criticidad.md).
