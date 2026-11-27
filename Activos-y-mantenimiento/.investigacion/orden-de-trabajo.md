# Activos y mantenimiento: vertical Orden de trabajo (informe de investigación)

Fecha: 2026-11-27. Estado: **parcial**. El presupuesto de búsqueda web de la sesión se agotó antes de la primera consulta y varias URL de documentación (IBM Maximo, SAP Help, DOE FEMP) devolvieron 404 o páginas vacías. Solo tres fuentes se leyeron con contenido útil (OSHA, Odoo, ERPNext). Todo lo demás figura como hueco o como conocimiento previo **no verificado** y no debe citarse como hecho en las notas sin una segunda ronda.

Marcas: [L] contenido de la página recuperado, [M] metadatos, [S] resumen secundario. WebFetch devuelve un resumen hecho por un modelo chico sobre la página, así que "L" no equivale a lectura literal íntegra.
Puntajes: A autoridad, P profundidad, E ejemplos, U unicidad (1 a 3).

## Cómo divide el campo esta vertical (aviso sobre el árbol)

El árbol propuesto (orden de trabajo, solicitud, planificación y programación, repuestos, cierre) es razonable, pero:
- En la práctica la **solicitud** y la **orden** a veces son un solo documento con estados (Odoo: una "maintenance request" con etapas New Request, Repaired, Scrap) y a veces dos documentos (aviso y orden, patrón SAP PM; **no verificado** en esta ronda).
- **Planificar** y **programar** son dos funciones distintas en Palmer y SMRP (no verificado acá), pero los sistemas chicos las colapsan en "Scheduled Date / Duration" en la misma ficha (Odoo).
- La **seguridad** (LOTO, permisos) es una disciplina propia (OSHA) que la orden solo referencia; conviene tratarla como dato de la orden, enlazando al estándar.
- El **mantenimiento preventivo** (plan que genera órdenes) queda fuera de esta vertical pero origina buena parte de las órdenes; ERPNext lo modela como plan + log por ocurrencia. Hay que decidir si va en otra vertical.

## Componente: orden de trabajo y solicitud

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Odoo, Maintenance requests (17.0) https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html | primaria (producto) | 2 | 2 | 3 | 2 | [L] |
| ERPNext, Asset Maintenance https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance | primaria (producto) | 2 | 1 | 2 | 3 | [L] |

Afirmaciones:
- En Odoo, una solicitud de mantenimiento sirve para "preventivo" (evitar roturas) y "correctivo" (arreglar equipo roto), sobre un equipo o un centro de trabajo. Fuente: https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html
- Datos de la solicitud en Odoo: título, equipo o centro de trabajo, fecha de solicitud (no editable), tipo (correctivo o preventivo), orden de fabricación u orden de trabajo vinculada, equipo responsable y persona, fecha programada y duración, bloqueo del centro de trabajo, prioridad de cero a tres estrellas, notas e instrucciones (PDF, enlace o texto). Misma URL.
- Estados en Odoo: New Request, Repaired, Scrap (para lo irreparable). Un solo documento cubre pedido y ejecución; no hay estados de aprobación, planificación ni cierre administrativo. Misma URL.
- La prioridad en Odoo es solo orden visual en el tablero ("Requests assigned a higher priority appear above those with a lower priority"); no es una matriz de urgencia e impacto. Misma URL.
- En ERPNext, el preventivo es un **plan** (Asset Maintenance) con filas de tarea (tipo, fecha de inicio, periodicidad, responsable, descripción, certificado requerido) que al guardar genera **logs** por ocurrencia; el log registra las acciones hechas y se completa o se cancela; lo vencido se resuelve completando o cancelando el log. Fuente: https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance
- En ERPNext, lo no planificado va por otro documento, **Asset Repair**, que registra "a failure, downtime, repair cost, and possible capitalization"; los costos de reparación que califican pueden capitalizarse, el mantenimiento rutinario normalmente no. Misma URL.
- Discrepancia de modelado: Odoo junta preventivo y correctivo en un documento con campo tipo; ERPNext los separa en plan/log y Repair. Ambas son prácticas reales.

Recurso canónico propuesto: la página de Odoo para ver el mínimo viable de un documento único; la de ERPNext para ver la separación plan/ocurrencia/reparación y el gancho a capitalización. Falta el canónico fuerte (SAP PM aviso+orden o Maximo): ver huecos.

## Componente: planificación y programación

Sin fuentes leídas. Conocimiento previo **no verificado** (para guiar una segunda ronda, no para citar): Palmer distingue planificador (qué, cómo, con qué, cuántas horas; paquete de trabajo) de programador (cuándo, quién); se programa trabajo "listo"; el pendiente se mide en semanas-técnico; SMRP define wrench time y schedule compliance. No se afirma ningún porcentaje ni rango.

## Componente: repuestos y materiales

Sin fuentes leídas. Solo se observa que la ficha de solicitud de Odoo no lista materiales (misma URL de Odoo).

## Componente: cierre de la orden

Afirmación leída: la frontera gasto frente a capitalización aparece en Asset Repair de ERPNext (https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance). Cierre técnico frente a administrativo, códigos de falla y horas reales: sin fuente; hueco.

## Componente: seguridad en la orden (LOTO)

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| OSHA 29 CFR 1910.147 https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147 | primaria (norma) | 3 | 3 | 1 | 3 | [L] |

Afirmaciones (URL de OSHA):
- El empleador debe establecer un programa de control de energía que consiste en "energy control procedures, employee training and periodic inspections" (1910.147(c)(1)).
- Pasos de aplicación (1910.147(d)): conocer la energía y sus peligros; apagar con el procedimiento establecido; ubicar y operar los dispositivos de aislamiento; aplicar bloqueo o etiquetado; liberar o contener la energía almacenada o residual; verificar el aislamiento antes de empezar.
- Inspección periódica del procedimiento "at least annually", por un empleado autorizado distinto de quienes usan el procedimiento (1910.147(c)(6)(i)).
- Inferencia mía, no de la fuente: la orden debería referenciar el procedimiento de bloqueo del equipo y registrar la verificación; el procedimiento es dato del equipo.
- OSHA es norma de EE. UU.; el marco argentino no se investigó.

Recurso canónico: 1910.147(c) y (d); fijarse en los seis pasos y en la auditoría anual.

## Huecos

- **404 o página vacía**: IBM Maximo (estados WAPPR, APPR, INPRG, COMP, CLOSE), SAP PM (CRTD, REL, TECO, CLSD; help.sap.com solo devolvió el título), DOE FEMP O&M Best Practices. Hay que encontrar la URL vigente.
- **Búsqueda web no disponible** (cupo agotado): no se consultaron Palmer (libro de pago, solo reseñas secundarias), SMRP BoK y Best Practices Metrics, EN 13306 (de pago), APQC PCF, NASA.
- **Sin datos numéricos**: wrench time, rangos de backlog, % planificado.
- **Sin cobertura**: matrices de prioridad y emergencia, trabajo listo vs no listo, coordinación con producción, repuestos críticos y kits, reserva y retiro contra la orden, códigos de falla, cierre técnico vs administrativo, aviso+orden vs documento único en SAP.
- Los resúmenes de WebFetch son de un modelo chico: antes de citar literal, reabrir las tres páginas leídas.
- Próximo paso: otra sesión con cupo de búsqueda, empezando por Maximo y SAP (estados) y por los documentos públicos de SMRP.

## Segunda ronda

Fecha: 2026-11-27. Solo WebFetch (búsqueda agotada). Marca [L] = resumen de WebFetch con cita pedida; son resúmenes de un modelo chico, reabrir antes de citar literal en notas. Puntajes A/P/E/U.

### Estados de la orden: IBM Maximo (hueco 1, parcial)

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| IBM Maximo Manage, Work order statuses https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=orders-work-order-statuses | primaria (producto) | 3 | 2 | 1 | 3 | [L] |

Estado, significado literal y transiciones permitidas según la página:
- WAPPR: "The work order is waiting for approval." Va a INPRG, CAN, WMATL, COMP, WPCOND, APPR, CLOSE.
- APPR: "The work order is approved and the work can begin." Va a INPRG, WMATL, COMP, WPCOND, WAPPR, CAN, CLOSE.
- WSCH: "The work order is waiting to be scheduled." Mismas salidas que APPR.
- WMATL: "Materials must arrive before the work can be performed."
- WPCOND: "The work can be performed only when the condition of the plant is suitable."
- INPRG: "The work is in progress." Va a WMATL, COMP, WAPPR, CLOSE.
- COMP: "The physical work is completed." Solo va a CLOSE.
- CLOSE: "The work order is closed." Solo va a HISTEDIT.
- CAN: "The work order is canceled." Sin transiciones.
- HISTEDIT: "The work order was edited in history."
Todo de la misma URL. Observaciones: (a) COMP (trabajo físico terminado) y CLOSE son pasos separados: base del cierre técnico frente al administrativo, pero la página no usa esos términos (inferencia mía). (b) Hay estados de espera por causa (materiales, condición de planta) además de aprobación y programación. (c) Una orden cerrada solo se corrige por un estado especial de edición en historia. (d) El resumen mostró "APP" en una fila: probable errata del resumen.

### SAP PM (hueco 1, sigue abierto)
help.sap.com devuelve solo el título «SAP Help Portal»; CRTD, REL, TECO, CLSD y aviso frente a orden: sin fuente leída.

### Preventivo por calendario o por uso, generación de órdenes (hueco 8)
- ERPNext: "ERPNext creates planned Asset Maintenance Logs for the schedule" al guardar el plan; no explica cómo la periodicidad se traduce en fechas y no hay disparador por uso (horas, contador, producción): los ejemplos son por calendario (inspección mensual, correa cada seis meses). https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance [L]
- Odoo 17, Maintenance requests: preventivo "intended to prevent equipment from breaking down"; campos Maintenance Type, Scheduled Date, Duration; no describe recurrencia. https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_requests.html [L]. maintenance_calendar solo menciona "Repeat Every" como medida de una vista pivote, sin explicarla. https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_calendar.html [L]
- Odoo 17, Maintenance setup (útil para el modelo de datos): MTBF "the amount of time (in days) between reported failures", calculado sobre correctivos completados; Expected MTBF editable; Estimated Next Failure: "This date is computed as the Latest Failure Date + MTBF"; MTTR "the amount of time (in days) it takes to repair this equipment upon failure". https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/maintenance/maintenance_setup.html [L]
- Wikipedia, Preventive maintenance [S]: planificado "can be date-based, based on equipment running hours, or on distance travelled"; ítems de cambio por intervalo fijo (TCI). https://en.wikipedia.org/wiki/Preventive_maintenance
- IBM Maximo PM y medidores: el índice de docs muestra una tarea cron "PMWoGen" (generación de órdenes de PM), pero el texto de los temas de PM y medidores no se leyó. https://www.ibm.com/docs/en/maximo-manage/continuous-delivery?topic=records-preventive-maintenance [M]. Hueco: frecuencia por tiempo y por medidor, anticipación, pronóstico.

### Tipos de mantenimiento, EN 13306 (hueco 5, parcial)
- Wikipedia sobre correctivo, que cita la NF EN 13306: "maintenance which is carried out after failure detection"; inmediato "starts immediately after a failure"; diferido "work is delayed in conformance to a given set of maintenance rules". https://en.wikipedia.org/wiki/Corrective_maintenance [S; A1 P1 E1 U1]. La norma no se leyó.
- Wikipedia, Predictive maintenance: lo distingue del preventivo porque "does take into account the current condition"; no menciona curva P-F ni EN 13306. https://en.wikipedia.org/wiki/Predictive_maintenance [S]
- Wikipedia, RCM: no trae patrones A a F ni P-F. https://en.wikipedia.org/wiki/Reliability-centered_maintenance [S]

### Huecos que siguen abiertos
- Planificación y programación, backlog, wrench time, cumplimiento del programa: SMRP (https://www.smrp.org/learning-resources/smrp-library/best-practices-metrics-guidelines/) lista "70+ metrics" pero las definiciones están tras membresía (Best Practices 7th Edition). DOE: la página del artículo y el PDF completo dan 404. Palmer: sin fuente pública hallada. Wikipedia CMMS no trata órdenes, medidores ni backlog; Wikipedia «Work order» no trata estados ni prioridades (solo: "often dispatched (reviewed and scheduled) before being executed"; https://en.wikipedia.org/wiki/Work_order).
- Matrices de prioridad, códigos de falla (Maximo: la página probada devolvió solo el índice; no se leyeron los 315 mil caracteres restantes) y cierre administrativo: sin fuente.
