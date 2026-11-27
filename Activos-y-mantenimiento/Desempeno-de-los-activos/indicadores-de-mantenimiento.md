---
resumen: >-
  Los indicadores de mantenimiento son las cuentas que se hacen sobre el historial de los equipos y de las órdenes de trabajo para saber cuánto andan los equipos (MTBF, MTTR, disponibilidad), si el trabajo se hace como se planeó (cumplimiento del preventivo, pendiente, trabajo planificado) y cuánto cuesta (costo sobre valor de reposición). Cada uno tiene más de una fórmula en circulación, y ninguno vale sin decir cuál se usó.
estado: borrador
estabilidad: semi
fuentes:
  - "Reliable Media (Reliamag), Maintenance and Reliability KPI Reference (resumen): https://reliamag.com/topics/guides/maintenance-reliability-kpi-reference"
  - "Wikipedia, Availability (resumen): https://en.wikipedia.org/wiki/Availability"
  - "NASA KSC, Availability: what is it (solo metadatos y resumen del buscador): https://extapps.ksc.nasa.gov/Reliability/Documents/160727.1_Availability_What_is_it.pdf"
  - "Wikipedia, Mean time between failures y Failure rate (remiten a Lienig y Bruemmer 2017 y Birolini 2013, no leídos): https://en.wikipedia.org/wiki/Mean_time_between_failures ; https://en.wikipedia.org/wiki/Failure_rate"
  - "Fiix, Maintenance cost as a percent of replacement asset value (resumen del buscador): https://fiixsoftware.com/maintenance-metrics/mcrav/"
  - "Odoo 17, Maintenance setup (MTBF, MTTR y próxima falla estimada, como evidencia de práctica): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_setup.html"
  - "Wikipedia, Overall equipment effectiveness: https://en.wikipedia.org/wiki/Overall_equipment_effectiveness"
  - "SMRP, Best Practices Metrics (definiciones tras membresía, no leídas): https://www.smrp.org/learning-resources/smrp-library/best-practices-metrics-guidelines/"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.2.6 y 10.3.2.7: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/registro-y-desempeno.md (2026-11-27), componente 2"
  - "Activos-y-mantenimiento/.investigacion/posicion-contraria.md (2026-11-27), sección 4"
  - "Activos-y-mantenimiento/.investigacion/orden-de-trabajo.md (2026-11-27), práctica de sistemas"
aliases: [KPI de mantenimiento, maintenance KPI, métricas de mantenimiento, maintenance metrics, MTBF, tiempo medio entre fallas, mean time between failures, MTTR, tiempo medio de reparación, mean time to repair, MTTF, tiempo medio hasta la falla, MTBM, disponibilidad, availability, disponibilidad inherente, disponibilidad operacional, cumplimiento del preventivo, PM compliance, pendiente en semanas, backlog, trabajo planificado, planned work, costo sobre valor de reposición, RAV, replacement asset value]
creado: 2026-11-27
revisado:
---

# Indicadores de mantenimiento

Los indicadores de mantenimiento son las cuentas que se hacen sobre el historial de los equipos y de las órdenes de trabajo para saber cuánto andan los equipos (MTBF, MTTR, disponibilidad), si el trabajo se hace como se planeó (cumplimiento del preventivo, pendiente, trabajo planificado) y cuánto cuesta (costo sobre valor de reposición). Cada uno tiene más de una fórmula en circulación, y ninguno vale sin decir cuál se usó.

Son la herramienta de la vertical [Desempeño de los activos](desempeno-de-los-activos.md), que explica para qué decisión sirve cada uno. Todos se calculan con lo que deja el [cierre de la orden](../Orden-de-trabajo/cierre-de-la-orden.md) en el [historial del equipo](../Registro-de-activos/historial-del-equipo.md). APQC 7.4 los pone en dos procesos seguidos, 10.3.2.6 «Define maintenance performance targets» y 10.3.2.7 «Monitor maintenance performance against targets/contracts».

## Las fórmulas

Las fórmulas que siguen son las de una guía de indicadores que remite a las definiciones de SMRP y de la norma europea EN 15341; ninguna de las dos se leyó, y la guía misma se leyó por un resumen. Se copian literales, salvo la última, que la guía y un resumen de un proveedor dan sin comillas:

| Indicador | Fórmula |
|---|---|
| Tiempo medio entre fallas (MTBF) | «Total operating time / number of failures (repairable assets)» |
| Tiempo medio de reparación (MTTR) | «Total repair time / number of repairs» |
| Disponibilidad | «Uptime / (uptime + downtime), or MTBF / (MTBF + MTTR)» |
| Cumplimiento del preventivo | «PM work orders completed on time / PM work orders scheduled» |
| Pendiente en semanas | «Total outstanding estimated work hours / weekly craft capacity hours (expressed in crew-weeks)» |
| Trabajo planificado | «Planned maintenance hours / total maintenance hours» |
| Costo sobre valor de reposición | costo anual de mantenimiento / valor de reposición × 100 |

El valor de reposición es, según la misma guía, «Cost to replace the asset base with equivalent new assets». El MTBF es para equipos que se reparan; para los que se tiran se usa el tiempo medio hasta la falla (MTTF). La guía advierte que confundir los dos es «one of the most common errors in maintenance reporting».

El tiempo de herramienta, la parte de la jornada en que el técnico trabaja de verdad sobre el equipo, mide la planificación y está en [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md), junto con el pendiente listo y el cumplimiento del programa semanal.

## Qué tiempo cuenta en el MTBF

El MTBF divide un tiempo por una cantidad de fallas, y las fuentes no coinciden en qué tiempo. La guía de indicadores pone «operating time» en el numerador, lo que sugiere sacar el tiempo en reparación, pero no lo dice y remite a SMRP o a la EN 15341. Un sistema de gestión empresarial abierto, según su documentación, lo calcula como «the amount of time (in days) between reported failures» sobre las órdenes correctivas terminadas: días de calendario entre fallas, con la reparación y las paradas adentro.

Las dos versiones dan números distintos para el mismo equipo. Una máquina que trabaja un turno de 8 horas cuenta 8 horas por día en la primera y 24 en la segunda (cuenta propia, ilustrativa). Como criterio de la base, el tablero dice cuál usa y no compara un MTBF de horas de marcha con uno de días de calendario.

## Inherente, lograda y operacional: tres disponibilidades

La disponibilidad es la fracción del tiempo en que el equipo puede cumplir su función. Hay al menos tres versiones, según qué paradas se restan:

| Disponibilidad | Fórmula | Qué paradas cuenta |
|---|---|---|
| Inherente (Ai) | MTBF / (MTBF + MTTR); para no reparables, MTTF / (MTTF + MTTR) | solo la reparación; excluye «logistics time, waiting or administrative downtime, and preventive maintenance downtime» |
| Lograda | (sin fórmula en la fuente leída) | incluye «active preventive and corrective maintenance downtime», pero no la logística ni la espera |
| Operacional (Ao) | MTBF / (MTBF + MDT), según Wikipedia; MTBM / (MTBM + MDT), según el resumen de la NASA | todo: el tiempo medio de parada (MDT) incluye «logistics time, ready time, and waiting or administrative downtime» |

La discrepancia en la operacional es de fondo. Con MTBF arriba, solo cuentan las fallas; con el tiempo medio entre mantenimientos (MTBM), cuentan también las paradas por preventivo. La versión con MTBM viene del resumen del buscador sobre el documento de la NASA, que no se pudo leer entero.

Como criterio de la base, la inherente sirve para comparar diseños y la operacional para saber qué ve producción. Wikipedia trae un ejemplo de equipo informático: con un MTTF de 713.940 horas (81,5 años) y un MTTR de 1 hora, Ai = 713.940 / 713.941 = 99,999860 %. El número es real y a la vez engaña: un equipo que espera tres días el repuesto sigue mostrando la misma Ai, porque la espera no entra. Esa lectura es inferencia de la base sobre la definición.

La disponibilidad es el primer factor de la eficiencia global del equipo (OEE), que la multiplica por el rendimiento y la calidad. La OEE mide la línea y se explica en el tema Producción, todavía no armado.

## El MTBF no es la vida del equipo

El MTBF solo describe bien a un equipo si su tasa de falla es constante. Wikipedia lo dice así: «this is only valid if the failure rate λ(t) is actually constant over time». Con tasa constante, la probabilidad de que el equipo siga andando al llegar al MTBF es 1/e, cerca del 37 %: el 63 % falla antes. Leer el MTBF como vida media, donde la mitad ya falló, «can lead to bad design decisions».

Un MTBF de 100.000 horas no quiere decir que el equipo dure 11 años, aunque 100.000 horas sean 11,4 años de marcha continua. Con tasa constante, la probabilidad de que falle en el primer año es 1 − e^(−8.760/100.000), cerca del 8,4 %, y a las 100.000 horas ya falló el 63 %. La frase es de manual y no se encontró en una fuente primaria; la cuenta es de la investigación de la base, y se verificó.

El caso se ve en la práctica. El sistema abierto de arriba estima la próxima falla como «Latest Failure Date + MTBF». Con tasa constante esa fecha es un promedio, no un aviso: según la cuenta anterior, el 63 % de las veces la falla llega antes (inferencia de la base). Y si el equipo se desgasta con la edad, la tasa no es constante y el promedio dice todavía menos; los patrones de falla están en [mantenimiento centrado en la confiabilidad](../Estrategia-de-mantenimiento/mantenimiento-centrado-en-confiabilidad.md).

Dos errores más, según Wikipedia: si solo se cuentan las fallas observadas, el MTBF se subestima por censura, y qué cuenta como falla depende del contexto. Lo segundo se decide al definir la falla en el [historial del equipo](../Registro-de-activos/historial-del-equipo.md).

## Cómo se engaña cada indicador

Un indicador se engaña sin mentir: alcanza con elegir qué entra. La guía de indicadores advierte que los objetivos de referencia «frequently circulate without a traceable primary source», y que la misma métrica en un tablero de un proveedor y en la EN 15341 «may be calculated slightly differently». Los casos que siguen son, salvo donde se dice, criterio de la base:

- Cumplimiento del preventivo. La fórmula cuenta las órdenes hechas a tiempo sobre las programadas. Si se reprograma una orden atrasada, deja de estar atrasada; si se cierra sin hacer la tarea, cuenta como hecha. Que el indicador dependa de qué se llama «a tiempo» lo marca la propia guía como inferencia.
- Pendiente en semanas. El número depende de la capacidad que se pone abajo. Con la capacidad nominal de la cuadrilla, sin restar vacaciones ni urgencias, el pendiente parece más corto; la guía también lo marca como inferencia.
- Trabajo planificado. Si cualquier orden con una línea de descripción cuenta como planificada, la proporción sube sin que nadie haya armado un paquete de trabajo.
- MTTR y MTBF. Dependen de que el técnico cargue la hora real de inicio y fin y el tipo de orden correcto. Un correctivo cargado como preventivo desaparece del MTBF; las causas están en [cierre de la orden](../Orden-de-trabajo/cierre-de-la-orden.md).
- Costo sobre valor de reposición. Numerador y denominador tienen que cubrir los mismos activos, y hay que declarar qué entra en el valor de reposición (ingeniería, instalación, edificios), según un resumen de un proveedor de software de mantenimiento. Un valor de reposición inflado baja el porcentaje.

La defensa es la misma en todos los casos: publicar la fórmula al lado del número y compararlo primero contra sí mismo en el tiempo, como pide la [entrada de la vertical](desempeno-de-los-activos.md).

> [!NOTE] Sin fuente todavía: las definiciones literales de SMRP (Best Practices Metrics, tras membresía) y de la EN 15341, que dirían si el MTBF incluye el tiempo de reparación; valores de referencia trazables para cualquiera de estos indicadores.
