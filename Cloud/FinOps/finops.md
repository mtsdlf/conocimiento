---
resumen: >-
  FinOps es la parte de Cloud que hace dueños del gasto a ingeniería, finanzas y negocio: cómo se
  organiza la práctica según la FinOps Foundation, cómo se asigna y se mide el costo, y cómo se baja
  en Azure.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-10-03
revisado:
---

# FinOps

FinOps es la parte de Cloud que hace dueños del gasto a ingeniería, finanzas y negocio: cómo se
organiza la práctica según la FinOps Foundation, cómo se asigna y se mide el costo, y cómo se baja
en Azure.

Dentro de [Cloud](../cloud.md), FinOps mira lo que cuestan todas las demás partes. Depende de
[Gobernanza e identidad](../Gobernanza-e-identidad/gobernanza-e-identidad.md), porque la
jerarquía de suscripciones y las etiquetas que obliga [Azure Policy](../Gobernanza-e-identidad/azure-policy.md)
son lo que permite repartir la factura. Sus palancas caen sobre el [cómputo](../Computo/computo.md)
(tamaño, reservas, Spot), los [datos operacionales](../Datos-operacionales/datos-operacionales.md)
(tiers de blob), las [redes](../Redes/redes.md) (egreso, private endpoints) y la
[operación](../Operacion/operacion.md) (retención de logs).

## Una práctica que se recorre en ciclos

En la nube, cualquier ingeniero crea gasto con un `apply` y la factura llega un mes después a
finanzas. FinOps junta a quien gasta con quien paga, con un equipo central que negocia descuentos
y publica los datos, y cada equipo dueño de su uso. El trabajo avanza en tres fases que se repiten
(Inform, Optimize, Operate), y cada capacidad madura por separado de Crawl a Walk y a Run.

## Asignar, medir y recién después optimizar

No se optimiza lo que no se ve. Primero se asigna el gasto a cada equipo (showback, y chargeback
si las políticas contables lo piden); con eso se calcula el costo unitario, que dice si un servicio
se vuelve más eficiente aunque el total crezca. Recién después se optimiza, y en orden: primero el
uso, después la tarifa, porque comprometer una reserva antes de ajustar el tamaño congela por años
un gasto que sobraba. FinOps no es recortar: gastar más puede estar bien si el ingreso crece más
rápido.

## Las cinco notas de FinOps

- [FinOps](que-es-finops.md) — la definición, los seis principios oficiales y las personas. Leerla primero.
- [Ciclo de vida de FinOps](ciclo-de-vida-finops.md) — las fases Inform, Optimize y Operate, y la madurez Crawl, Walk, Run.
- [Showback y chargeback](showback-y-chargeback.md) — cómo se reparte la factura entre equipos y en qué se diferencian mostrar y cobrar.
- [Costo unitario](costo-unitario.md) — la métrica que relaciona el costo con lo que produce un servicio.
- [Optimización de costos en Azure](optimizacion-de-costos-en-azure.md) — rightsizing, reservas, savings plans, Spot, egreso y logs para bajar el costo sin romper los SLO.
