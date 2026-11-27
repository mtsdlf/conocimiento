---
resumen: >-
  Planificar una orden de trabajo es decidir qué se hace, cómo y con qué (tareas, horas, oficios, repuestos, herramientas); programarla es decidir cuándo y quién. Son dos trabajos distintos: el primero deja la orden lista, el segundo la pone en la semana de una cuadrilla, en el momento en que producción puede parar el equipo.
estado: borrador
estabilidad: semi
fuentes:
  - "D. Palmer, «Do you know the purpose and principles of maintenance planning and scheduling?», Palmer's Planning Corner, Plant Services (según el resumen del buscador): https://www.plantservices.com/voices/palmers-planning-corner/article/55361071/do-you-know-the-purpose-and-principles-of-maintenance-planning-and-scheduling"
  - "D. Palmer, «Understanding the math of maintenance planning and scheduling», Plant Services (según el resumen del buscador): https://plantservices.com/planned-maintenance/planning-and-scheduling/article/11295301/understanding-the-math-of-maintenance-planning-and-scheduling"
  - "Reliable Plant, el pendiente planificado como requisito para programar (según el buscador): https://reliableplant.com/Articles/Print/7051?id=7051"
  - "IBM, Maximo Manage, Work order statuses: https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=orders-work-order-statuses"
  - "Odoo 17, Maintenance requests (fecha programada, duración, bloqueo del centro de trabajo): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html"
  - "SMRP, Best Practices Metrics (definiciones tras membresía, no leídas): https://www.smrp.org/learning-resources/smrp-library/best-practices-metrics-guidelines/"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.1.4, 10.3.1.6, 10.3.1.7 y 10.3.2.1: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/orden-de-trabajo.md, tercera-ronda.md y apqc-10.md"
aliases: [planificación del mantenimiento, programación del mantenimiento, maintenance planning, maintenance scheduling, planning and scheduling, pendiente, backlog, trabajo pendiente, tiempo de herramienta, wrench time, cumplimiento del programa, schedule compliance, trabajo listo, ready backlog]
creado: 2026-11-27
revisado:
---

# Planificación y programación

Planificar una orden de trabajo es decidir qué se hace, cómo y con qué (tareas, horas, oficios, repuestos, herramientas); programarla es decidir cuándo y quién. Son dos trabajos distintos: el primero deja la orden lista, el segundo la pone en la semana de una cuadrilla, en el momento en que producción puede parar el equipo.

Están entre la [solicitud de trabajo](solicitud-de-trabajo.md) aprobada y la ejecución de la [orden de trabajo](orden-de-trabajo.md). APQC 7.4 los pone en grupos distintos: «Conduct resource planning» (10.3.1.6) y «Create work plans» (10.3.1.7) dentro de planificar, y «Schedule maintenance work» (10.3.2.1) dentro de gestionar. Un sistema de gestión para pymes los junta en dos campos de la misma ficha, fecha programada y duración; según la base, alcanza mientras nadie se dedique solo a preparar trabajo.

## Qué hace el planificador y qué hace el programador

El planificador arma el paquete de trabajo de una orden: los pasos, las horas por oficio, los repuestos y las herramientas, los permisos y el procedimiento de bloqueo del equipo. Trabaja sobre lo que viene, no sobre la urgencia de hoy. El programador toma las órdenes ya preparadas, mira las horas disponibles de cada cuadrilla y las ventanas en que se puede parar cada equipo, y arma la semana. Esta división de tareas es criterio de la base. Los resúmenes de Palmer solo confirman que los planificadores se ocupan del trabajo futuro y que se programa trabajo ya planificado; ningún rol se leyó en una fuente primaria.

Para la base, la diferencia importa porque las dos funciones compiten por la misma persona: si el planificador también atiende las fallas del día, las fallas ganan y el trabajo futuro nunca se prepara. Es inferencia.

## Los principios de Palmer

D. Palmer, autor de un libro sobre el tema, resume la práctica en dos listas de principios. Lo que sigue sale de resúmenes de sus columnas, no del libro:

- De planificación: los planificadores están en un departamento separado de las cuadrillas; se ocupan del trabajo futuro; llevan archivos simples y seguros a nivel de equipo; reciben la retroalimentación de los técnicos; evitan las trampas que impiden planificar todo; y miden su desempeño con el tiempo de herramienta como medida principal de eficiencia.
- De programación: se programa trabajo planificado, con un sistema de prioridades creíble; el horizonte es de una semana; el programa se carga al 100 % de las horas disponibles; el supervisor reparte el trabajo día a día; y se mide el cumplimiento del programa. El resumen menciona un cumplimiento entre 40 y 90 %, sin aclarar si es lo observado o lo esperable.

La retroalimentación de los técnicos es lo que conecta este componente con el [cierre de la orden](cierre-de-la-orden.md): lo que el técnico anota al terminar es lo que el planificador usa la próxima vez.

## El tiempo de herramienta

El tiempo de herramienta es, en la definición de la base, la parte de la jornada de un técnico en que efectivamente trabaja sobre el equipo, sin contar traslados, búsqueda de repuestos, esperas ni permisos. Según los resúmenes de Palmer, ronda el 35 % en una planta típica, aun en una buena, y la planificación y la programación lo pueden llevar a cerca del 55 %. Según los mismos resúmenes, la cuenta es 55 / 35 = 1,57, o sea un 57 % más de trabajo con la misma gente. El argumento económico de tener planificadores sale de ahí.

> [!NOTE] Sin fuente todavía: la definición formal del tiempo de herramienta y del cumplimiento del programa de SMRP, cuyas fichas de métricas están detrás de una membresía.

## El pendiente y el trabajo listo

El pendiente es el conjunto de órdenes aprobadas que todavía no se hicieron. La base lo mide en horas o semanas de trabajo de la cuadrilla y no en cantidad de órdenes, porque una orden puede llevar una hora o una semana; ninguna fuente leída lo confirma. El pendiente planificado, el que ya tiene paquete de trabajo, es requisito para programar, según un artículo de práctica que lo dice en esos términos.

Para la base, una orden está lista cuando se la puede ejecutar sin preguntar nada: está planificada, los repuestos están reservados o en el depósito, y hay acuerdo para parar el equipo. Un sistema de mantenimiento de referencia lo hace visible con estados de espera con causa: esperando programación, esperando materiales («Materials must arrive before the work can be performed») y esperando condición de planta («can be performed only when the condition of the plant is suitable»). Separar el pendiente total del pendiente listo es criterio de la base: el primero mide cuánto falta, el segundo cuánto se puede programar la semana que viene.

> [!NOTE] Sin fuente todavía: un rango de referencia del pendiente en semanas de cuadrilla y la proporción de trabajo planificado sobre el total.

## Parar el equipo: el acuerdo con producción

Para la base, casi todo el mantenimiento de una planta exige parar algo, y la ventana la decide producción. APQC lo nombra como proceso propio, «Integrate preventive maintenance into operations schedule» (10.3.1.4). Un sistema para pymes tiene un campo en la orden que bloquea el centro de trabajo; la base lo lee como la forma de que producción no le cargue trabajo mientras dura el mantenimiento.

El programa semanal es, como criterio de la base, una negociación: mantenimiento propone qué equipos necesita parar y cuánto tiempo, y producción dice cuándo. Programar la planta es del tema Producción, todavía no armado; acá queda el lado de mantenimiento. Qué equipos se pueden esperar y cuáles no lo dice su [criticidad](../Registro-de-activos/criticidad.md).
