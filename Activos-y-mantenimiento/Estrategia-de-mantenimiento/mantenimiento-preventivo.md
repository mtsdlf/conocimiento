---
resumen: >-
  El mantenimiento preventivo es el que se hace a intervalos fijados de antemano, por calendario o por uso, sin esperar a que el equipo falle ni a que muestre síntomas. Se organiza como un plan de tareas con su frecuencia, y el plan genera una orden de trabajo cada vez que una tarea vence.
estado: borrador
estabilidad: semi
fuentes:
  - "DOE/FEMP, O&M Best Practices Guide, Release 3.0, cap. 5, sec. 5.3 «Preventive Maintenance» y 5.4: https://www1.eere.energy.gov/femp/pdfs/OM_5.pdf"
  - "Nowlan y Heap, Reliability-Centered Maintenance, 1978, DTIC ADA066579 (copia de la Wayback Machine del PDF de DTIC; la URL original da 403): https://web.archive.org/web/2020/https://apps.dtic.mil/sti/pdfs/ADA066579.pdf"
  - "NASA, Reliability Centered Maintenance Guide for Facilities and Collateral Equipment, copia de febrero de 2000, fig. 1-1 y sec. 2.4.5: https://everyspec.com/NASA/NASA-General/download.php?spec=NASA_RCM_GUIDE_2000.030306.pdf"
  - "Wikipedia, Preventive maintenance (según su resumen): https://en.wikipedia.org/wiki/Preventive_maintenance"
  - "ERPNext, Asset Maintenance (plan, tareas con periodicidad, registros por ocurrencia): https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance"
  - "Odoo 17, Maintenance requests: https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html"
  - "IBM Maximo Manage, Preventive maintenance records (solo el índice: tarea programada PMWoGen): https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=records-preventive-maintenance"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.1.4, 10.3.1.7 y 10.3.3.1: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/estrategia-y-fundamentos.md (componentes A y B, 2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/orden-de-trabajo.md (preventivo por calendario o por uso, 2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/verificacion-estrategia.md (2026-11-27)"
aliases: [mantenimiento preventivo, preventive maintenance, PM, mantenimiento planificado, planned maintenance, mantenimiento programado, scheduled maintenance, mantenimiento predeterminado, predetermined maintenance, plan de mantenimiento, maintenance plan, preventivo por calendario, time-based maintenance, preventivo por uso, usage-based maintenance, meter-based maintenance]
creado: 2026-11-27
revisado:
---

# Mantenimiento preventivo

El mantenimiento preventivo es el que se hace a intervalos fijados de antemano, por calendario o por uso, sin esperar a que el equipo falle ni a que muestre síntomas. Se organiza como un plan de tareas con su frecuencia, y el plan genera una orden de trabajo cada vez que una tarea vence.

El DOE lo define como acciones hechas «on a time- or machine-run-based schedule» para detectar, evitar o mitigar la degradación de un componente y así sostener o alargar su vida útil. Es uno de los tipos de la [estrategia de mantenimiento](estrategia-de-mantenimiento.md), junto al correctivo, el [mantenimiento por condición](mantenimiento-por-condicion.md) y dejar fallar. APQC 7.4 lo ejecuta en 10.3.3.1 «Perform preventative asset maintenance» y pide integrarlo al programa de operación en 10.3.1.4 «Integrate preventive maintenance into operations schedule».

## De qué está hecho un plan preventivo

Un plan dice qué hacerle a qué equipo y cada cuánto. En un sistema abierto de referencia, el plan tiene una fila por tarea, con su tipo, su fecha de inicio, su periodicidad, un responsable, una descripción y, si hace falta, un certificado exigido. Los ejemplos de esa documentación son una inspección mensual y un cambio de correa cada seis meses.

Una tarea bien escrita dice además cuánto dura, qué oficio la hace, qué repuestos y herramientas lleva y qué valores tiene que anotar el técnico. Eso es lo que necesita la [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md) para cargar la semana, y los [repuestos y materiales](../Orden-de-trabajo/repuestos-y-materiales.md) para reservar. Que esos datos vivan en la tarea y no se tipeen en cada orden es criterio de la base.

Una **ruta** agrupa tareas cortas de muchos equipos en un solo recorrido: una ronda de lubricación o una inspección semanal de todas las bombas de una sala. Es la definición de la base; ninguna fuente leída trata las rutas.

> [!NOTE] Sin fuente todavía: cómo se modelan las rutas (una orden con muchos equipos, o una orden por equipo agrupada) y cómo se cierran los puntos de una ronda. Ninguna fuente leída lo trata; es el hueco más relevante para quien construye el software.

## Por calendario o por uso

El preventivo tiene dos disparadores. Wikipedia, según su resumen, dice que el planificado puede ser «date-based, based on equipment running hours, or on distance travelled». El DOE da el ejemplo del aceite: cambiarlo cada 3.000 a 5.000 millas es preventivo por uso.

- **Por calendario**, la tarea vence en una fecha. Conviene cuando el desgaste avanza con el tiempo aunque el equipo no ande (corrosión, vencimiento de un matafuegos) o cuando una norma fija la frecuencia, como en el [mantenimiento obligatorio en la Argentina](../mantenimiento-obligatorio-en-argentina.md).
- **Por uso**, la tarea vence cuando un contador llega a un valor: horas de marcha en un horómetro, kilómetros, ciclos, piezas producidas. Conviene cuando el equipo trabaja a ritmos que cambian; una autoelevadora que anda dos turnos se desgasta el doble que una que anda uno. Esta comparación es criterio de la base.

El preventivo por uso depende de un dato que el calendario no necesita: alguien tiene que cargar las lecturas del contador, a mano o desde el equipo. Esas lecturas van al [historial del equipo](../Registro-de-activos/historial-del-equipo.md). Si no se cargan, el plan no vence nunca y el equipo puede pasar meses sin servicio sin que nadie lo vea (inferencia de la base).

De los dos sistemas abiertos leídos, uno solo ejemplifica el disparo por calendario y el otro no describe recurrencia; ninguno menciona medidores ni contadores. De un sistema de mantenimiento de referencia solo se vio el nombre de la tarea que genera órdenes, sin su texto sobre frecuencias por tiempo o por medidor.

## Cómo el plan genera órdenes

El plan no es una orden: es la regla que produce órdenes. En el sistema abierto de referencia, al guardar el plan se crean registros planificados, uno por ocurrencia, y cada uno se completa o se cancela; lo vencido se resuelve completando o cancelando. En un sistema de mantenimiento de referencia, el índice de la documentación muestra una tarea programada de generación de órdenes preventivas; no se leyó cómo funciona.

Hay tres decisiones de diseño que cualquier implementación tiene que tomar. Las tres son criterio de la base, porque ninguna fuente leída las trata:

1. **Con cuánta anticipación se genera la orden.** Una orden que aparece el día que vence no da tiempo a pedir repuestos ni a programarla; una que aparece con un mes de anticipación llena el pendiente de trabajo que todavía no corre.
2. **Desde dónde se cuenta el próximo vencimiento.** Si se cuenta desde la fecha planeada, el plan mantiene su ritmo aunque una orden se haga tarde. Si se cuenta desde la fecha en que se hizo, el intervalo real entre servicios se respeta, pero el plan se corre con cada atraso.
3. **Qué pasa si la orden anterior sigue abierta.** Generar otra encima duplica el trabajo; no generarla esconde que el plan está atrasado.

La orden que sale del plan sigue el mismo ciclo que cualquier otra, del alta al [cierre](../Orden-de-trabajo/cierre-de-la-orden.md), y se mide con el cumplimiento del preventivo de los [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md).

## Cuándo sirve el intervalo fijo y cuándo sobra

El preventivo por intervalo funciona cuando la falla depende de la edad. La NASA lo reserva para lo sujeto a desgaste, los consumibles y lo que tiene un patrón de falla conocido. Agrega que los elementos simples, de una sola pieza, muestran con frecuencia una relación directa entre confiabilidad y edad, y que para ellos un límite de edad por tiempo de marcha o por ciclos de esfuerzo puede ser efectivo.

Para los equipos complejos, según la NASA, la mayoría no falla por edad, y cambiarlos a una edad fija no los hace más confiables; la NASA lo toma de Nowlan y Heap (1978), que lo dicen así en el original: «unless there is a dominant failure mode, an age limit does little or nothing to improve the overall reliability of a complex item». Está en [mantenimiento centrado en la confiabilidad](mantenimiento-centrado-en-confiabilidad.md).

Sobremantener tiene costo y tiene riesgo. El DOE pone entre las desventajas del preventivo que «Includes performance of unneeded maintenance» y el «Potential for incidental damage to components in conducting unneeded maintenance». La NASA va más lejos: «In many cases scheduled overhaul increases the overall failure rate by introducing a high infant mortality rate into an otherwise stable system». Un tornillo flojo o una junta mal puesta al reabrir un equipo que andaba bien serían ejemplos de ese daño incidental (ejemplo de la base).

El DOE estima que el preventivo ahorra entre 12 y 18 por ciento sobre el reactivo, sin dar la fuente de la cifra; la advertencia sobre estas cifras está en [estrategia de mantenimiento](estrategia-de-mantenimiento.md#las-cifras-de-ahorro-que-circulan-y-por-qué-no-sirven-de-dato).

> [!NOTE] Sin fuente todavía: cuánto preventivo sobra en una planta típica (medido, no estimado) y cómo se depura un plan heredado. Ninguna fuente leída lo mide.
