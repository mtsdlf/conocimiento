---
resumen: >-
  El desempeño de los activos es cómo una empresa sabe si su mantenimiento alcanza: cuánto andan los equipos entre fallas, cuánto tardan en volver, cuánto del plan se cumple y cuánto cuesta. Cada indicador sirve para una decisión concreta, y la más grande es cuándo dejar de reparar un equipo y reemplazarlo.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.2 y 10.4.1, pp. 27-28: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Reliable Media (Reliamag), Maintenance and Reliability KPI Reference (página leída, sin fecha de publicación): https://reliamag.com/topics/guides/maintenance-reliability-kpi-reference"
  - "Activos-y-mantenimiento/.investigacion/registro-y-desempeno.md (2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/apqc-10.md (2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/verificacion-registro-y-desempeno.md (2026-11-27)"
aliases: [desempeño del mantenimiento, maintenance performance, asset performance, gestión del desempeño de activos, asset performance management, APM, indicadores de mantenimiento, KPI de mantenimiento]
creado: 2026-11-27
revisado:
---

# Desempeño de los activos

El desempeño de los activos es cómo una empresa sabe si su mantenimiento alcanza: cuánto andan los equipos entre fallas, cuánto tardan en volver, cuánto del plan se cumple y cuánto cuesta. Cada indicador sirve para una decisión concreta, y la más grande es cuándo dejar de reparar un equipo y reemplazarlo.

Dentro de [Activos y mantenimiento](../activos-y-mantenimiento.md) es la vertical que cierra el ciclo. Lee el [historial del equipo](../Registro-de-activos/historial-del-equipo.md) que dejan las [órdenes de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) al cerrarse, y devuelve a la [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) qué corregir. Sin historial con datos no hay nada que medir; como inferencia de la base, por eso es lo último que se arma.

APQC, en su marco de procesos 7.4 (2024), pone la medición dentro de la gestión del mantenimiento, con dos procesos: 10.3.2.6 «Define maintenance performance targets» y 10.3.2.7 «Monitor maintenance performance against targets/contracts». El segundo prevé medir contra contratos, que es lo que pasa en el [servicio de campo](../Servicio-de-campo/contrato-de-servicio.md). El fin de vida, en 10.4.1, suma «Monitor useful life of assets» y «Perform cost vs. benefit analysis for replacement».

## Qué se mide y para qué decisión

Un indicador que no cambia ninguna decisión es un número en un tablero. Como criterio de la base, los indicadores del dominio se ordenan por la pregunta que contestan:

| Pregunta | Indicador | Decisión que mueve |
|---|---|---|
| ¿El equipo falla seguido? | tiempo medio entre fallas (MTBF) | cambiar la estrategia del equipo, analizar la causa |
| ¿Cuánto tarda en volver? | tiempo medio de reparación (MTTR) | repuestos en stock, habilidades del técnico, diseño para mantener |
| ¿Está cuando se lo necesita? | disponibilidad | comprar un equipo de reserva, comprometer un plazo |
| ¿Se hace lo que se planeó? | cumplimiento del preventivo | recursos del plan, plan sobredimensionado |
| ¿Cuánto trabajo espera? | pendiente en semanas | contratar, tercerizar, priorizar |
| ¿Se trabaja con plan? | proporción de trabajo planificado | invertir en planificación |
| ¿Cuánto cuesta mantener? | costo sobre valor de reposición | presupuesto, comparar plantas |
| ¿Conviene seguir? | costo del ciclo de vida, costo anual equivalente | reparar o reemplazar |

Los primeros tres miden al equipo; los tres del medio, al trabajo; los dos últimos, la plata. Las fórmulas, sus versiones en conflicto y cómo se engaña cada uno están en [indicadores de mantenimiento](indicadores-de-mantenimiento.md).

## Por qué los números de referencia no se trasladan

Los objetivos de clase mundial circulan mucho y se rastrean poco. Una guía de indicadores lo advierte: muchos objetivos de clase mundial «circulate widely without a traceable primary source», y «a metric labeled the same way in a vendor dashboard and in EN 15341 may be calculated slightly differently». Como criterio de la base, un indicador se compara primero contra sí mismo en el tiempo y después, con su fórmula a la vista, contra otra planta.

> [!NOTE] Sin fuente todavía: valores de referencia trazables para cualquier indicador de esta vertical (la página pública de SMRP no trae las definiciones, que están en un compendio para miembros, y no se leyeron).

## Lo que esta vertical no mide

La eficiencia global del equipo (OEE) nació en el mantenimiento productivo total, pero mide la línea (disponibilidad por rendimiento por calidad) y se explica en el tema Producción, todavía no armado. Lo que interesa acá es su primer factor, la disponibilidad, que está en [indicadores de mantenimiento](indicadores-de-mantenimiento.md). El tiempo de herramienta de los técnicos mide la planificación y vive en [planificación y programación](../Orden-de-trabajo/planificacion-y-programacion.md).

## Qué hay en el desempeño de los activos

- [Indicadores de mantenimiento](indicadores-de-mantenimiento.md) — MTBF, MTTR, disponibilidad, cumplimiento del preventivo, pendiente, trabajo planificado y costo sobre valor de reposición: fórmulas, discrepancias entre fuentes y cómo se engañan.
- [Reparar o reemplazar](reparar-o-reemplazar.md) — costo del ciclo de vida, costo anual equivalente y vida económica, con un ejemplo numérico, y dónde empieza el lado contable.
