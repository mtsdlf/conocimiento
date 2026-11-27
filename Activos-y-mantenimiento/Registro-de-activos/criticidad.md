---
resumen: >-
  La criticidad de un equipo es cuánto le importa a la empresa que falle, por la gravedad de lo que pasa cuando falla y por lo probable que es. Se calcula una vez por equipo, con un análisis que suele terminar en una matriz de consecuencia por probabilidad, y decide cuánto esfuerzo de mantenimiento merece cada uno.
estado: vigente
estabilidad: semi
fuentes:
  - "Wikipedia, Reliability-centered maintenance (resumen): https://en.wikipedia.org/wiki/Reliability-centered_maintenance"
  - "NASA, RCM Guide for Facilities and Collateral Equipment (copia de febrero de 2000), fig. 1-1: https://everyspec.com/NASA/NASA-General/download.php?spec=NASA_RCM_GUIDE_2000.030306.pdf"
  - "Wikipedia, Risk matrix (resumen): https://en.wikipedia.org/wiki/Risk_matrix"
  - "Cox, L. A., What's wrong with risk matrices?, Risk Analysis 28(2), 2008, resumen del autor (leído completo en Europe PMC; el artículo no): https://doi.org/10.1111/j.1539-6924.2008.01030.x"
  - "Wikipedia, Failure mode, effects, and criticality analysis (resumen): https://en.wikipedia.org/wiki/Failure_mode,_effects,_and_criticality_analysis"
  - "Activos-y-mantenimiento/.investigacion/registro-y-desempeno.md (2026-11-27), primera y segunda ronda"
  - "Activos-y-mantenimiento/.investigacion/estrategia-y-fundamentos.md (2026-11-27), componente A"
  - "Activos-y-mantenimiento/.investigacion/verificacion-registro-y-desempeno.md (2026-11-27)"
aliases: [análisis de criticidad, criticality analysis, criticidad del equipo, asset criticality, equipment criticality, matriz de riesgo, risk matrix, matriz de criticidad, criticality matrix, FMECA, ranking de criticidad]
creado: 2026-11-27
revisado: 2026-11-27
---

# Criticidad

La criticidad de un equipo es cuánto le importa a la empresa que falle, por la gravedad de lo que pasa cuando falla y por lo probable que es. Se calcula una vez por equipo, con un análisis que suele terminar en una matriz de consecuencia por probabilidad, y decide cuánto esfuerzo de mantenimiento merece cada uno.

Es un atributo del [registro de activos](registro-de-activos.md) que se calcula sobre la [jerarquía de activos](jerarquia-de-activos.md): se le da a cada equipo o a cada sistema. La usa la [estrategia de mantenimiento](../Estrategia-de-mantenimiento/estrategia-de-mantenimiento.md) para elegir qué tipo de mantenimiento recibe cada equipo, y la [solicitud de trabajo](../Orden-de-trabajo/solicitud-de-trabajo.md) para ordenar lo que llega.

## Qué consecuencias se miran

Una falla importa por lo que provoca, no por el equipo en sí. El mantenimiento centrado en la confiabilidad (RCM), según su resumen en Wikipedia, mira tres riesgos: la seguridad, la operación y el presupuesto de mantenimiento; las versiones más nuevas suman el ambiente. Un ejemplo de la base: una misma bomba puede ser crítica en una planta sin otra de reserva y menor en una que tiene dos en paralelo.

Como criterio de la base, la criticidad depende del contexto y no de la clase de equipo. Según la guía de RCM de la NASA, dejar fallar conviene para elementos chicos, no críticos, sin consecuencia, improbables de fallar o redundantes. Las preguntas cinco y seis del RCM («cuánto importa» y «qué tarea previene o reduce las consecuencias») son, como lectura de la base, un análisis de criticidad hecho por modo de falla. El método completo está en [mantenimiento centrado en la confiabilidad](../Estrategia-de-mantenimiento/mantenimiento-centrado-en-confiabilidad.md).

## La matriz de consecuencia por probabilidad

La forma más común de expresar la criticidad es una matriz de riesgo: en un eje, categorías de gravedad; en el otro, categorías de probabilidad; en cada celda, un nivel de riesgo. Según su resumen en Wikipedia, la matriz es «a simple mechanism to increase visibility of risks and assist management decision making», y el riesgo que representa es, en términos estadísticos, probabilidad por gravedad.

El ejemplo de esa página usa cuatro niveles de gravedad (Minor, Marginal, Critical, Catastrophic) y cinco de probabilidad, de Certain a Rare. Tres celdas como muestra:

| Probabilidad | Gravedad | Riesgo |
|---|---|---|
| Certain | Minor | High |
| Possible | Critical | High |
| Rare | Catastrophic | Medium |

En defensa y aeroespacial, la variante es el análisis de modos de falla, efectos y criticidad (FMECA). Según su resumen en Wikipedia, calcula un número de criticidad por modo de falla, Cm = λp × α × β × t, donde λp es la tasa de falla base, α la proporción de fallas de ese modo, β la probabilidad de que el efecto llegue a la gravedad dada y t el tiempo. La criticidad del ítem, Cr, es la suma de los Cm de sus modos. La gravedad sigue la MIL-STD-882 (I Catastrófica, II Crítica, III Marginal, IV Despreciable) y la probabilidad va de A Frecuente a E Improbable. Como inferencia, una planta rara vez tiene las tasas de falla que pide esa fórmula, y por eso suele usar categorías en lugar de números.

## Cómo la criticidad orienta la estrategia y la prioridad

Como criterio de la base, la criticidad se usa en dos momentos distintos:

1. Al armar el plan. Los equipos de criticidad alta reciben un análisis de modos de falla y tareas preventivas o [por condición](../Estrategia-de-mantenimiento/mantenimiento-por-condicion.md); los de criticidad baja pueden quedar en correctivo, como dice la guía de la NASA. Es la decisión de cuánto gastar antes de la falla.
2. Al ordenar el trabajo. Cuando llegan diez solicitudes juntas, la prioridad de cada orden combina la criticidad del equipo con la urgencia de la falla: una pérdida de aceite en el compresor sin reserva va antes que una lámpara quemada en el depósito. La prioridad es de la orden y cambia; la criticidad es del equipo y queda.

> [!NOTE] Sin fuente todavía: cómo se combina la criticidad del equipo con la urgencia en una matriz de prioridad de órdenes, y cuántas categorías de criticidad usan las plantas en la práctica. La guía de criticidad que trataba esto no se alcanzó a leer.

## Las críticas a la matriz de riesgo

La matriz es fácil de usar y por eso se usa mal. Cox (2008) examina sus propiedades matemáticas, parte de que «little research rigorously validates their performance in actually improving risk management decisions» y encuentra cuatro límites:

- Resolución pobre. Una matriz típica «can correctly and unambiguously compare only a small fraction (e.g., less than 10%) of randomly selected pairs of hazards», y puede asignar la misma calificación a riesgos cuantitativamente muy distintos («range compression»).
- Errores. Puede asignar una calificación más alta a un riesgo cuantitativamente menor. Si frecuencia y gravedad están correlacionadas de forma negativa, puede ser «worse than useless» y llevar a decisiones peores que al azar.
- Asignación subóptima. Los recursos contra los riesgos no pueden repartirse bien con las categorías de la matriz.
- Entradas y salidas ambiguas. Las categorías de gravedad no se pueden fijar de forma objetiva cuando la consecuencia es incierta, y distintos usuarios pueden obtener calificaciones opuestas para los mismos riesgos.

Cox concluye que las matrices deben usarse «with caution, and only with careful explanations of embedded judgments». Según el resumen de Wikipedia, que no se contrastó con la fuente, Thomas, Bratvold y Bickel muestran además que cambiar las escalas o los cortes cambia qué riesgo queda primero.

La consecuencia práctica, como criterio de la base, es que una matriz propia es una convención local. Conviene documentar qué quiere decir cada nivel con un ejemplo (cuántas horas de parada, qué tipo de lesión, cuánta plata) y no comparar criticidades entre plantas que usan matrices distintas.

Otro modo de falla, también criterio de la base: la criticidad se calcula una vez, al armar el registro, y nadie la revisa cuando se agrega un equipo de reserva o cambia el proceso. El equipo que era crítico deja de serlo y sigue recibiendo el plan caro.
