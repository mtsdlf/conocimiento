---
resumen: >-
  Cerrar una orden de trabajo es registrar lo que pasó: el trabajo hecho, la falla encontrada, las horas, los materiales y el costo. Es lo que convierte un trabajo en historia del equipo; un cierre vacío o mal codificado deja un historial que no sirve para medir ni para decidir.
estado: borrador
estabilidad: semi
fuentes:
  - "IBM, Maximo Manage, Work order statuses (terminada, cerrada, edición en historia): https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=orders-work-order-statuses"
  - "SAP Help, orden técnicamente concluida (TECO) y cerrada (CLSD), según el buscador: https://help.sap.com/doc/saphelp_sfin100/1.9/en-US/88/16295411158c24e10000000a4450e5/content.htm"
  - "ERPNext, Asset Repair: https://docs.frappe.io/erpnext/user/manual/en/asset-repair"
  - "ERPNext, Asset Maintenance: https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance"
  - "Odoo 17, Maintenance setup (MTBF y próxima falla estimada): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_setup.html"
  - "Microsoft Learn, Dynamics 365 Field Service, Work order lifecycle and system statuses (2026-08-10): https://learn.microsoft.com/en-us/dynamics365/field-service/work-order-status-booking-status"
  - "Microsoft Learn, Overview of Dynamics 365 Field Service (2026-11-23): https://learn.microsoft.com/en-us/dynamics365/field-service/overview"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.3.2.3 y 10.3.2.4: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Activos-y-mantenimiento/.investigacion/orden-de-trabajo.md, registro-y-desempeno.md, servicio-de-campo.md, tercera-ronda.md y apqc-10.md"
aliases: [cierre de la orden, cierre de orden de trabajo, work order close, work order completion, cierre técnico, cierre administrativo, technical completion, códigos de falla, failure codes, notificación de tiempos]
creado: 2026-11-27
revisado:
---

# Cierre de la orden

Cerrar una orden de trabajo es registrar lo que pasó: el trabajo hecho, la falla encontrada, las horas, los materiales y el costo. Es lo que convierte un trabajo en historia del equipo; un cierre vacío o mal codificado deja un historial que no sirve para medir ni para decidir.

Es el último paso del ciclo de la [orden de trabajo](orden-de-trabajo.md) y el que APQC 7.4 llama «Update work and asset records» (10.3.2.4); al lado pone «Undertake quality control» (10.3.2.3), revisar que el trabajo quedó bien. Lo que se registra acá alimenta el [historial del equipo](../Registro-de-activos/historial-del-equipo.md) y, desde él, los [indicadores de mantenimiento](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md).

## Qué se registra al cerrar

Un ERP abierto pide, para una reparación: el equipo, la fecha de la falla, una descripción de la falla, las facturas de proveedores y los repuestos consumidos (de donde sale el costo), las acciones realizadas y la fecha de finalización. Para el preventivo, el registro de cada ocurrencia anota las acciones hechas y se completa o se cancela. Con eso, y sumando lo que la base considera necesario, el cierre completo tiene cinco partes:

| Parte | Qué se anota | Para qué sirve después |
|---|---|---|
| Trabajo hecho | Qué se hizo, con palabras del técnico | Que el próximo técnico y el planificador sepan qué se tocó |
| Falla | Qué se encontró, por qué falló y qué se hizo, codificado | Contar fallas por modo y causa; analizar confiabilidad |
| Horas | Horas reales por persona u oficio, y cuánto estuvo parado el equipo | Costo de mano de obra; tiempo de reparación |
| Materiales | Repuestos e insumos consumidos | Costo; qué pieza se cambió en el equipo |
| Costo | La suma de lo anterior más servicios de terceros | Comparar contra lo estimado; pasarlo a Contabilidad |

Los materiales consumidos vienen de [repuestos y materiales](repuestos-y-materiales.md). Las horas cargadas son costo del trabajo acá; para liquidar el sueldo del técnico son del tema Administración de personal y nómina, todavía no armado.

## La falla codificada

Una falla en texto libre se lee, pero no se cuenta. Para saber cuántas veces falló un rodamiento por falta de lubricación hace falta que el cierre use una lista cerrada: qué se observó (el problema), por qué pasó (la causa) y qué se hizo (la acción). El ERP abierto que sirve de ejemplo no tiene códigos de falla estructurados: la descripción es texto libre. La división en problema, causa y acción es criterio de la base; ninguna fuente leída la describe.

> [!NOTE] Sin fuente todavía: las tablas de modo, causa y mecanismo de falla de ISO 14224 (anexo B), y cómo un sistema arma sus listas de códigos por clase de equipo.

## Terminada y cerrada

El trabajo físico termina antes que la orden. Un sistema de mantenimiento de referencia tiene dos estados: terminada, «The physical work is completed», y cerrada, que viene después y desde la que solo se puede pasar a una edición controlada del historial. Un ERP de gran empresa hace el mismo corte, según el buscador: técnicamente concluida, que todavía admite liquidar costos, y cerrada, final y bloqueada. Un sistema de servicio de campo lo hace con terminada y contabilizada: la segunda la pone administración después de revisar, y dispara la factura.

Para la base, el intervalo entre los dos estados existe porque hay cosas que llegan tarde: la factura de un taller externo, la devolución al depósito de un repuesto que no se usó, la revisión del supervisor de los códigos que cargó el técnico. Llamar a esto cierre técnico y cierre administrativo es lectura de la base; las fuentes no usan esos términos. Cerrar la orden en el mismo momento en que termina el trabajo deja el costo incompleto para siempre. Esta explicación es inferencia de la base.

En el servicio de campo hay una variante: el técnico puede marcar la orden como terminada o como que necesita seguimiento, y un cierre parcial la devuelve a sin programar. Está en [visita técnica](../Servicio-de-campo/visita-tecnica.md).

## Por qué los cierres malos arruinan el historial

El que cierra la orden es el técnico, al final del turno y con la próxima urgencia esperando; el que aprovecha el dato es quien analiza meses después. Esa asimetría explica la mayoría de los historiales inútiles: códigos genéricos («otro», «revisado»), horas redondeadas, repuestos que no se cargan. Esta explicación es criterio de la base.

El daño es concreto. Un sistema de gestión para pymes calcula el [tiempo medio entre fallas](../Desempeno-de-los-activos/indicadores-de-mantenimiento.md) sobre las órdenes correctivas terminadas, y estima la próxima falla así: «Latest Failure Date + MTBF». Si un correctivo se cargó como preventivo, o no se cerró, ese cálculo cuenta mal y la fecha estimada miente. Lo mismo pasa con cualquier análisis de [mantenimiento centrado en la confiabilidad](../Estrategia-de-mantenimiento/mantenimiento-centrado-en-confiabilidad.md), que exige identificar los modos de falla dominantes y sus causas.

Lo que ayuda, como criterio de la base: pocas opciones de código, elegidas según la clase del equipo; campos obligatorios solo donde el dato se usa; y una revisión del supervisor entre terminada y cerrada. Palmer, según los resúmenes de sus principios, pide la retroalimentación de los técnicos para que el planificador mejore el próximo paquete de trabajo (ver [planificación y programación](planificacion-y-programacion.md)).

## El costo pasa a Contabilidad

La orden junta el costo de una reparación; si ese costo va a resultados o se suma al valor del equipo lo decide Contabilidad. El ERP abierto lo muestra en la reparación con un interruptor, «Capitalize Repair Cost», y un campo para el aumento de vida útil, con la regla general «Routine repair is normally an expense». La regla misma, con la norma que la sostiene, está en [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md).

Lo que le toca al cierre es dejar el dato para que esa decisión se pueda tomar: qué se cambió, cuánto costó y si el trabajo alarga la vida del equipo o solo lo devuelve a su condición. Un cambio de motor que agrega años de uso y un cambio de correa de rutina se cierran igual en mantenimiento, pero se registran distinto en [Contabilidad](../../Contabilidad/contabilidad.md).
