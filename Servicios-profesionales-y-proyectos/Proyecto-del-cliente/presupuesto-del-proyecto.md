---
resumen: >-
  El presupuesto del proyecto es la foto aprobada de cuántas horas, cuánto costo y cuánto ingreso se esperan en un proyecto, repartidos por fase, tarea o rol; contra esa foto se comparan los reales, se mueve un pronóstico y, cuando el pronóstico se aleja, se aprueba una versión revisada.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Dynamics 365 Project Operations, Project budget key concepts: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/budget/keyconcepts-projectbudget"
  - "Microsoft Learn, Dynamics 365 Project Operations, Revise a project cost budget: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/budget/revise-project-cost-budget"
  - "Microsoft Learn, Dynamics 365 Project Operations, Estimating projects overview: https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/estimating-projects-overview"
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage contract values for project-based sales: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-contract-values-project-based-sales"
  - "ERPNext, Project Profitability (presupuesto con tope de gasto): https://docs.frappe.io/erpnext/user/manual/en/project-profitability"
  - "ERPNext, Project y Project Costing (costo estimado, avance por tareas): https://docs.frappe.io/erpnext/user/manual/en/project"
  - "GAO, Cost Estimating and Assessment Guide, GAO-20-195G (2020), glosario y capítulo de valor ganado, estimate at completion: https://www.gao.gov/assets/gao-20-195g.pdf"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 5)"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 2.3)"
aliases: [presupuesto del proyecto, project budget, línea base de costo, cost baseline, budget at completion, presupuesto de costo, presupuesto de ingreso, pronóstico del proyecto, project forecast]
creado: 2026-11-27
revisado:
---

# Presupuesto del proyecto

El presupuesto del proyecto es la foto aprobada de cuántas horas, cuánto costo y cuánto ingreso se esperan en un proyecto, repartidos por fase, tarea o rol; contra esa foto se comparan los reales, se mueve un pronóstico y, cuando el pronóstico se aleja, se aprueba una versión revisada.

Comparte el nombre con el [presupuesto](../../Relacion-con-clientes/Presupuesto/presupuesto.md) de Relación con clientes, que es otra cosa: aquel es la oferta que se le manda al cliente; este es el plan económico interno del [proyecto del cliente](proyecto-del-cliente.md) una vez vendido. Uno puede salir del otro, porque la estimación de la oferta suele ser la base del primer presupuesto del proyecto, pero desde que el cliente acepta viven por separado.

## Una foto que no se mueve

Un sistema de gestión de servicios define el presupuesto como «a point-in-time snapshot of the estimated spend across the project phases and its associated tasks». Que sea una foto es lo central: si después cambian los precios o las tarifas, el presupuesto aprobado sigue diciendo lo que decía. Es la línea base contra la que se mide el desvío, y por eso no se edita.

El mismo sistema lleva dos presupuestos: uno de costo, contra el que se compara el costo real de tiempo, materiales y gastos, y otro de ingreso, contra el que se comparan las ventas sin facturar y las facturadas. En un proyecto a [precio cerrado](../Facturacion-del-proyecto/facturacion-por-hito.md) el ingreso está fijado y lo que se vigila es el costo; en uno por [tiempo y materiales](../Facturacion-del-proyecto/facturacion-por-hora.md) el monto del contrato es, en palabras del sistema, «an estimated value», y, por criterio de esta base, los dos presupuestos se mueven juntos.

## De qué está hecha una línea del presupuesto

Cada línea tiene sus dimensiones: en el sistema leído, la categoría, la tarea, el tipo de costo y el proveedor, sin repetir combinaciones. Cada movimiento real (una hora aprobada, un gasto) se empareja con la línea que tiene más dimensiones coincidentes; si no hay una exacta, el sistema afloja primero la dimensión de menor prioridad. Lectura de esta base: por ejemplo, una hora cargada a una tarea sin línea propia cae en la línea de su fase.

Para un servicio profesional, las dimensiones que importan son la fase o la tarea y el rol, y cada línea tiene tres cantidades: horas, costo (horas por el [costo de la hora](../Rentabilidad-de-la-firma/costo-y-margen-del-proyecto.md)) y precio (horas por la tarifa del rol). El mismo sistema, al estimar una hora, crea dos líneas gemelas, una de venta y otra de costo, con los mismos datos no monetarios; el rol y la unidad organizativa (la parte de la firma, como un área o una oficina, con su propia lista de precios) son la dimensión de precio de las dos.

> [!NOTE] Sin fuente todavía: un esquema de presupuesto por fase, tarea y rol (horas, costo y precio) que no salga de la documentación de un solo producto. Lo de arriba es lo que hace un sistema; el reparto por rol es criterio de esta base.

Otro sistema abierto es más simple: el proyecto tiene un costo estimado y un presupuesto de gasto cuyo límite «will be validated in the expense transactions». Es un tope que frena gastos, no un plan por fase. Criterio de esta base: alcanza para una firma chica que solo quiere saber si un proyecto se pasó.

## Se estima en dos momentos

El sistema leído estima dos veces. En la preventa, la estimación vive en las líneas de la cotización, con detalles de tiempo, gastos, materiales y honorarios. En la ejecución, pasa a las líneas del contrato o al plan del proyecto. Recomienda estimar de abajo hacia arriba, desde las tareas y con roles genéricos (un «consultor senior» sin nombre), y al importar la estimación a la cotización se ven el costo, el precio y el margen.

Cómo se estima bien (con rangos, comparando con proyectos parecidos) está en [estimación](../../Desarrollo/Encargo/estimacion.md) y en [pronóstico](../../Gestion-de-proyectos/Planificacion/pronostico.md); cuánto se agrega por riesgo en un precio cerrado, en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#cuánto-agregar-por-el-riesgo). Los roles genéricos se vuelven personas con nombre en [Asignación de personas](../Asignacion-de-personas/asignacion-de-personas.md).

## Aprobado, pronóstico y revisado

El sistema leído separa tres capas:

| Capa | Qué es | Cuándo cambia |
|---|---|---|
| Presupuesto aprobado | La foto, línea base | Nunca; se reemplaza con una revisión |
| Pronóstico | Lo que hoy se espera gastar o facturar por línea | Cada vez que alguien lo actualiza |
| Presupuesto revisado | Una versión nueva que formaliza el pronóstico | Cuando se aprueba la revisión |

Dos reglas del sistema sirven para cualquier diseño. Al aprobarse, «The forecast equals the budgeted value». Y el pronóstico nunca baja del real: «If actual costs are more than the forecasted cost for a budget line, the forecast cost will be made equal to the actual cost». El desvío de costo es cero mientras el real esté debajo del pronóstico, y real menos pronóstico cuando lo pasa; el de ingreso es el espejo.

La revisión parte siempre de una versión aprobada y crea una nueva en borrador, que puede tomar los pronósticos como base: «When you must formalize forecasts as a budget, a budget revision is required». Lo que suele forzar una revisión es una [orden de cambio](orden-de-cambio.md) aprobada.

## Pronóstico y estimación al terminar

El valor ganado, el índice de costo y la estimación al terminar (*estimate at completion*) son método de seguimiento y están en [medir el avance](../../Gestion-de-proyectos/Seguimiento/medir-el-avance.md#el-valor-ganado-y-la-estabilidad-del-cpi). Lo que este tema necesita de ellos es dónde se guardan: el presupuesto aprobado es el total presupuestado, y el pronóstico por línea hace el papel de la estimación al terminar.

La guía de costos de la Oficina de Rendición de Cuentas del gobierno de los Estados Unidos (GAO-20-195G) da las definiciones que sostienen esa correspondencia. El presupuesto al terminar (*budget at completion*) es «the sum of the estimated budgets for all cost elements», y vale también para un elemento de nivel más bajo. La estimación al terminar es «an assessment of the cost to complete authorized work based on a contractor's historical EVM performance», con un segundo método, la estimación de abajo hacia arriba, que evalúa en detalle el trabajo que queda. La fórmula general que trae es «EAC = ACWP (cumulative) + (BAC – BCWP (cumulative)) / efficiency index»: el costo real acumulado más lo que falta del presupuesto, ajustado por un índice de eficiencia. La guía recomienda calcular más de una estimación al terminar. Es una guía de programas públicos de gran escala, no de servicios profesionales; sirve para la definición de los datos y no dice cómo se guardan en un sistema.

> [!NOTE] Sin fuente todavía: un sistema de servicios que guarde la estimación al terminar o la estimación para terminar con su fórmula. Ninguna página de sistemas leída usa esas siglas; lo más cercano es el pronóstico por línea con piso en el real.

## Cómo falla

Lectura de esta base sobre lo anterior. El presupuesto falla cuando se edita en lugar de revisarse: el desvío desaparece y nadie sabe cuánto se había prometido. Falla también cuando se lleva solo en plata y no en horas, porque las horas son lo que el equipo puede controlar y lo que la [hoja de horas](../Registro-de-horas/hoja-de-horas.md) registra. Y falla cuando las horas se cargan al proyecto pero no a una tarea o a un rol que tenga línea, porque todo cae en una bolsa y el pronóstico por fase deja de decir algo.
