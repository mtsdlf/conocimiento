# Planificación de la producción: informe de investigación

Ángulo: estrategias de respuesta (MTS, ATO, MTO, ETO; CODP), plan maestro de producción (MPS), MRP, planificación de capacidad. Fecha: 2026-11-27. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes: autoridad / profundidad / ejemplos / unicidad (1 a 3).

Parte de, y no repite, `Cadena-de-suministro-y-logistica/.investigacion/planificacion-3.md` (sección H1: diapositivas MIT 2.854 de Gershwin, MRP literal: neteo, lote, desfase, reglas de lote, explosión, nerviosismo, jerarquía de planes) y `planificacion-2.md` (G12 documentación del MPS de un sistema abierto, G13 pronóstico y plan maestro de otro, G14 `MrpEvent` de un tercero). Se citan por su id (H1, G12, G13, G14); G12 se volvió a leer para sacar citas nuevas.

## Fuentes de esta ronda

| Id | Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|---|
| P1 | Lymperopoulos, G., *Σχεδιασμός και Προγραμματισμός Παραγωγής: Προγραμματισμός Απαιτήσεων σε Υλικά* (diapositivas, Univ. de Tesalia, Depto. de Ingeniería Mecánica, 25/11/2015). Declara como guía el cap. 3 «The MRP Crusade» de Hopp y Spearman, *Factory Physics*, 2.ª ed. (2000). Está en griego: las citas de abajo son traducción mía, con los números literales | https://opencourses.uth.gr/modules/document/file.php/MHXB125/MRP.pdf | secundaria (curso abierto que sigue a Hopp y Spearman) | 2/3/3/1 | [L] texto extraído (755 líneas): MRP, regenerativo y cambio neto, pegging, lote, stock y plazo de seguridad, RCCP, CRP |
| P2 | Diapositivas «Material Requirements Planning (MRP) for Dependent Demand Systems» (SMU, curso 5362, 2004; sin autor visible) | https://s2.smu.edu/~barr/5362/2004/04p20MRP.pdf | secundaria (curso) | 1/2/3/1 | [L] 444 líneas extraídas; las columnas de las tablas salen desalineadas |
| P3 | Documentación oficial de un sistema comercial (Oracle E-Business Suite 12.1, «Time Fence Control») | https://docs.oracle.com/cd/E18727_01/doc.121/e15188/T478564T479135.htm | primaria (documentación de un sistema; comercial, no abierto) | 2/2/1/2 | [L] la página |
| P4 | Documentación de «Lead times» de un sistema abierto (Odoo 17.0) | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/lead_times.html | primaria (documentación oficial de un sistema abierto) | 2/2/3/2 | [L] la página (resumen del lector con citas) |
| P5 | Olhager, J. y Van Donk, D. P. (2024), «Managing customer order decoupling points in supply chains», en *The Palgrave Handbook of Supply Chain Management*, Springer, pp. 1115-1137. DOI 10.1007/978-3-031-19884-7_103 | https://lup.lub.lu.se/record/2f6f2a70-d314-4ea2-b252-140f6d5396c3 | primaria (capítulo; registro del repositorio) | 3/2/1/3 | [M] abstract, solo recortes literales cortos |
| P6 | Olhager, J. (2003), «Strategic positioning of the order penetration point», International Journal of Production Economics 85(3), 319-329 | https://ideas.repec.org/a/eee/proeco/v85y2003i3p319-329.html | primaria (paper; RePEc dice «No abstract is available for this item») | 3/1/1/3 | [M] metadatos; el abstract salió de un catálogo de biblioteca vía buscador [S] |
| P7 | Wikipedia, «Order fulfillment» (MTS, MTO, ATO, ETO, punto de desacople) | https://en.wikipedia.org/wiki/Order_fulfillment | secundaria | 1/1/1/1 | [S] resumen del lector con citas |
| P8 | Wikiversity, «Master Production Schedule» (tipos de barrera, ATP, PAB, ejemplo con stock de seguridad 20) | https://en.wikiversity.org/wiki/Master_Production_Schedule | secundaria (wiki) | 1/1/2/1 | [S] resumen del lector; solo las filas PAB y ATP |
| P9 | Wikipedia, «Material requirements planning» (hitos históricos) | https://en.wikipedia.org/wiki/Material_requirements_planning | secundaria | 1/1/1/1 | [S] |
| P10 | Wikipedia, «Master production schedule» | https://en.wikipedia.org/wiki/Master_production_schedule | secundaria | 1/1/1/1 | [S]: no trae barreras ni fórmula del ATP |
| P11 | Documentación de «Production Plan» de un sistema abierto (ERPNext) | https://docs.frappe.io/erpnext/user/manual/en/production-plan | primaria (documentación oficial) | 2/1/1/2 | [L] la página (resumen del lector con citas) |
| P12 | Documentación de «Manufacturing Settings» del mismo sistema abierto | https://docs.frappe.io/erpnext/user/manual/en/manufacturing-settings | primaria | 2/1/1/2 | [L] la página (resumen del lector con citas) |
| P13 | Solucionario de preguntas de discusión de un manual de operaciones (curso IE 314, KSU) | https://faculty.ksu.edu.sa/sites/default/files/mrp.pdf | secundaria (apuntes sobre un libro) | 1/1/1/1 | [L] solo las primeras 100 líneas del texto extraído |
| P14 | Resultados del buscador sobre barreras de tiempo en la documentación de tres sistemas comerciales (NetSuite, IFS, Infor) | https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/bridgehead_3848105396.html y https://ifshelp.instron.com/ifsdoc/documentation/en/MasterScheduling/AboutTimeFenceDemandAndPlanning.htm | primaria (documentación) pero leída solo en resumen | 2/1/1/1 | [S]; la página de IFS no se pudo abrir (`ENOTFOUND`) |
| P15 | Hopp y Spearman, *Factory Physics* (3.ª ed.), índice: cap. 3 «The MRP Crusade», p. 114; 3.1.7 «safety stock and safety lead times», p. 133 | https://sisis.rz.htw-berlin.de/inh2012/12423613.pdf | primaria (índice) | 3/1/1/1 | [S] solo lo que devolvió el buscador; el capítulo no se leyó |

No se pudieron abrir: las diapositivas MIT 2.854 de 2010 (dspace, 404), las de ESD.260 lect15 (conexión rechazada), el paper de Cardiff sobre ETO y CODP en dos dimensiones (403).

---

## 1. Estrategias de respuesta y punto de desacople del pedido (CODP)

### Afirmaciones

- El CODP: «The CODP refers to the point in the supply chain at which a product is linked to a specific customer.» [P5, M]. El concepto se discute desde 1984. El abstract lista las posiciones «make to stock, assemble to order, make to order, purchase and make to order, and engineer to order» (es decir, hay una quinta, comprar y fabricar contra pedido, que el árbol no nombra) y distingue las operaciones aguas arriba, guiadas por pronóstico, de las aguas abajo, guiadas por pedido [P5, M, resumen del lector, no literal].
- Olhager (2003) lo llama «order penetration point»: «Market, product, and production factors are identified that affect the OPP positioning and the shifting of the OPP upstream or downstream in the manufacturing value chain» y «Guidelines are provided for this strategic choice» [P6, texto de un catálogo vía buscador, S]. La lista de factores (plazo que tolera el cliente frente al plazo de producción, variedad, estabilidad de la demanda): sin leer.
- Definiciones de las cuatro estrategias, con la relación P:D (plazo de producción frente a plazo de entrega que acepta el cliente) [P7, S]:
  - ETO, D≫P: «the product is designed and built to customer specifications».
  - Fabricar contra pedido (también «build-to-order»), D>P: «the product is based on a standard design».
  - ATO, D<P: «the product is built to customer specifications from a stock of existing components».
  - MTS, D=0: «the product is built against a sales forecast, and sold to the customer from finished goods stock».
  - Punto de desacople: «The decoupling point always is an inventory buffer» [P7, S], donde se encuentran los tramos empujados por pronóstico y los tirados por la demanda.
- Qué cambia en el plan: «The master schedule is expressed in terms of: (1) End items in a continuous (make-to-stock) company; (2) Customer orders in a job shop (make-to-order) company; and (3) Modules in a repetitive (assemble-to-stock) company.» [P13, L; es un solucionario, no el libro]. El mismo solucionario, sobre la lista de materiales: «A planning bill of material may be used to issue a mixture of parts that only makes sense to reduce material handling» y «A phantom bill of material is a subassembly that exists only on the production line» [P13, L]. Sobre lista modular de opciones con porcentajes para ATO: sin fuente.

### Discrepancias

- «Make-to-order» y «build-to-order» se igualan en P7, pero P5 lista «make to order» y «purchase and make to order» como posiciones distintas. P13 usa «assemble-to-stock» para la repetitiva, que no coincide con el ATO de P7.

### Recurso canónico

Olhager y Van Donk (2024) [P5] para la idea y la bibliografía; Olhager (2003) [P6] para los factores de ubicación. El texto completo de ninguno se leyó: la nota debe marcar que solo se vio el abstract.

### Qué registra un sistema

- En un sistema abierto, la fecha de la orden contra pedido se calcula hacia atrás: la fecha límite de la orden de fabricación «is calculated as the expected delivery date subtracted by the manufacturing lead time» [P4, L]. El plan de producción del sistema abierto de P11 se arma desde pedidos de venta («Select option as Sales Order from the 'Get Items From' drop-down list») o solicitudes de material, y «Click on 'Get Items for Work Order' to fetch the items from the above Sales Orders» trae los ítems con lista de materiales [P11, L].
- El plan maestro por reposición con pronóstico es el otro camino [G12]. Que el producto tenga una estrategia (a stock o contra pedido) como dato no se confirmó como campo en un sistema abierto.

---

## 2. Plan maestro de producción (MPS)

### Afirmaciones

- Definición mínima: «a plan for individual commodities to be produced in each time period» [P10, S]; «The Master Production Schedule is a detailed Plan of Production.» [P8, S]. Ambas flojas; falta la definición del diccionario de ASCM.
- Frontera con el plan agregado (S&OP es de otro tema): el plan agregado da «Outputs, inventories by time period / In standard units» y se desagrega en «MASTER PRODUCTION SCHEDULE / Individual product production, by period / Capacity requirements» [P2, L]. En la jerarquía de MIT: «Demand management — converts long range forecast and actual orders into detailed forecast», con el plan maestro en el plazo intermedio [H1].
- El MPS como entrada del MRP: «Master production scheduling: produces the MPS, a fundamental input of MRP. This function works with rough-cut capacity planning to ensure the MPS is capacity-feasible» [P1, L, traducción]. En P2 el MPS es una tabla por ítem y período, junto con la lista de materiales y el registro de stock («MRP Inputs: Master schedule, Bill of materials, Inventory records») [P2, L].
- Cubetas: «In some MRP systems, time is divided into time buckets — days, weeks, or whatever is convenient.» [H1, diap. 6]. En un sistema abierto, «Default Time Range» anual, mensual, semanal o diario y «Number of Periods» [G12].
- Mecánica de reposición del MPS de un sistema abierto, literal [G12, releído en https://raw.githubusercontent.com/odoo/documentation/19.0/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst, L]: «Forecasted Stock = Starting Stock - Forecasted Demand - Indirect Demand Forecast + Replenishment»; «Replenishment = Safety Stock Target - Starting Stock + Forecasted Demand + Indirect Demand Forecast»; «Indirect Demand Forecast»: «The forecasted demand for the component from existing MOs». «Adding a product to the MPS does not automatically create a purchase or manufacturing order»; «The MPS only suggests the amount of product to be replenished». Disparador: «Manually replenish the product from the MPS», «Automatically schedule a replenishment order for the product» o «Never replenish the product from the MPS». «Safety Stock Target: Specify the minimum quantity of the product to be available across all time periods»; «Minimum to Replenish: ... for each period».
- Barreras de tiempo, tres versiones:
  - Sistema comercial, documentación oficial [P3, L]: «The demand time fence is bordered by the current date and a date within which the planning process does not consider forecast demand when calculating actual demand. Within the demand time fence, Oracle MRP only considers actual demand. Outside the demand time fence, the planning process considers forecast demand.» «The planning time fence is bordered by the current date and a date within which the planning process does not alter the current material plan or master schedule.» Dentro de ella, en ítems discretos, el proceso «does not reschedule in (create earlier) order due dates or create new planned orders for the item to satisfy net demand requirements. However, the planning process can reschedule out or cancel an order when it determines that such orders create excess supply.» Afuera, «can generate suggestions to create, change, and reduce entries on the master schedule or the material requirements plan.» Una tercera: «The release time fence is bordered by the current date and a date within which the planning process automatically releases planned orders to Oracle Work in Process as discrete jobs or to Oracle Purchasing as purchase requisitions.» Y «A firm order is an order that is frozen in quantity and time (unavailable for rescheduling).», que crea una barrera implícita porque «resources committed to meeting the firm order would be unavailable for orders scheduled earlier.»
  - Resumen del buscador sobre documentación de otros sistemas comerciales [P14, S]: «Demand Time Fences are a point in time, or boundary, within the master schedule when the forecast is no longer included in total demand and projected available inventory calculations. Within this point, only customer orders are considered.» Para la de planificación: «A point in time, or boundary, within the master schedule when changes to the schedule may adversely affect component schedules, capacity plans, customer deliveries, and cost.» Y sobre IFS: «The demand time fence is the shorter of the two periods.»; «During the time period beyond the demand time fence but within the planning time fence, changes to the master production schedule require consideration of management trade-offs. Beyond the planning time fence, the master production scheduler is free to change the schedule.»
  - Wiki [P8, S]: «The first week or two can be frozen - no changes are allowed during this time - this is called time fence.», con cuatro barreras de otros nombres (pronóstico, reserva, MPS, disponible para prometer). No coincide con las dos de arriba.
  - Los nombres de zona «congelada, firme, abierta» (frozen, slushy, liquid) no aparecen en ninguna fuente leída. MIT dice solo «Freeze the early part of the schedule (ie, the near future)» [H1, diap. 31].
- Consumo del pronóstico por pedidos: dentro de la barrera de demanda cuenta solo el pedido [P3]. El consumo hacia adelante o atrás como mecanismo: sin fuente.
- Disponible para prometer (ATP) y saldo proyectado (PAB): «Available To Promise (ATP) - Number of MPS items that can be promised to new customer orders.» «Projected Available Balance (PAB) - Projected number of available items.» Ejemplo, stock de seguridad 20, producto A [P8, S, solo estas dos filas]:

| Semana | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PAB | 55 | 30 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 |
| ATP | | 20 | 0 | 20 | 10 | 20 | 15 | 0 | 30 | 25 | 30 |

  La fórmula del ATP y las filas de pedidos no se leyeron: no sirve para la nota sin la tabla entera.
- Plan maestro en dos niveles: sin fuente.
- Otro sistema abierto guarda por partida `planned_qty`, `order_release_date` y `cumulative_lead_time`, y por cabecera el vínculo al pronóstico y a los pedidos de venta [G13].

### Recurso canónico

*APICS Dictionary* (ASCM) y Vollmann et al., *Manufacturing Planning and Control* (capítulo de planificación maestra): no leídos, no hay copia abierta encontrada. Mientras tanto, la documentación de un sistema para las barreras [P3] (es evidencia de cómo un sistema las implementa, no un texto de fundamentos) y un sistema abierto para la reposición [G12].

### Qué registra un sistema

- Por producto, almacén y período: existencia inicial, demanda pronosticada, demanda indirecta, reposición sugerida, existencia pronosticada [G12]. Por producto: stock de seguridad objetivo, mínimo a reponer, disparador (manual, automático, nunca) [G12].
- Barreras: en P3, tres (demanda, planificación, liberación), cada una una cantidad de días desde hoy, más una marca de «orden firme» por orden. En ningún sistema abierto se encontró un campo de barrera.

---

## 3. MRP

H1 ya trae neteo, explosión, lote, desfase, reglas de lote, incertidumbre, nerviosismo y jerarquía. Acá lo nuevo.

### Afirmaciones

- Entradas y salidas: «MRP Inputs: Master schedule, Bill of materials, Inventory records»; salidas «Changes / Order releases / Planned-order schedules» y «Inventory transaction» que realimenta [P2, L]. «An MRP System: Is a management information system. Uses little mathematics, primarily bookkeeping» [P2, L]. Requisitos: «A good schedule of what is to be made / An accurate BOM / Accurate inventory records / Accurate purchases data / Lead times that will be met» [P13, L].
- Registro por ítem de un ejemplo: plazo («Lead time 3 weeks»), costo estándar, costo de preparación («Setup cost»), cantidad de pedido («Order quant 15 units»), «Safety stock», «Where used», «On hand», «On order» [P2, L].
- Ejemplo numérico de un curso abierto [P2, L]. Ítem «Treadle subassembly #0820000», lote 15, plazo 3 semanas, stock 10, necesidades brutas 3 en el período 2, 8 en el 7 y 10 en el 10. Su fila de saldo es «10 10 7 7 7 7 7 -1 -1 -1 -11 -11 -11» (empieza en el período 0, y no aplica la recepción planificada) y la «Planned release» es 15. Derivación mía con sus entradas: 10-3 = 7 (período 2); 7-8 = -1 (período 7), así que hace falta una recepción de 15 en el 7 y, con plazo 3, el lanzamiento va en el período 4; el saldo queda 14 y 14-10 = 4 en el 10. La explosión sigue: el lanzamiento de 15 es necesidad bruta de 15 del componente «Treadle pivot #0270018» (lote 15, plazo 3), que lanza en el período 1 [P2, L]. Para el nivel siguiente («Casting #0278818», lote 25, plazo 6): stock 11, necesidad de 15 y recepción programada de 25 en el período 2; saldo «-4» y luego «21» (11-15 = -4; -4+25 = 21), sin lanzamiento [P2, L].
- Neteo con varios padres [P1, L]: «Ακαθάριστες απαιτήσεις» (necesidades brutas) «125, 90, 15», que suman las que vienen del ítem B (35, 30, 15) y del ítem 100 (90, 60); recepción programada «100»; saldo proyectado «50 50 25 25 -65»; necesidades netas «65, 15»; recepciones y lanzamientos planificados «65, 15». La posición exacta de cada cifra por período se perdió en la extracción.
- Órdenes planificadas frente a firmes: «Firm planned orders: planned orders that are held fixed and scheduled to start whatever the changes in the system. They stabilize the production schedule and serve to reduce system nervousness.» [P1, L, traducción]. «A firm order is an order that is frozen in quantity and time (unavailable for rescheduling).» [P3]. La salida del MRP es la «job pool», hecha de lanzamientos planificados, que pasan al piso con la función de liberación de trabajos [P1, L].
- Regenerativo frente a cambio neto (Hopp y Spearman vía P1, [L, traducción]): «Regenerative: all planned order releases that have not yet been converted into real jobs (scheduled receipts) are discarded, and the process is repeated from the start, beginning with the MPS at level zero.» «Net-change: only those items whose demand has changed are affected. This gives faster updating, but is less effective because lot size selection does not benefit fully from all the net requirements.» «Most modern MRP systems use the regenerative method.» Frecuencia: «Too frequent updating: the factory will receive a storm of exception reports and planned order releases will keep changing. Too infrequent: we end up with old schedules that are often obsolete.»
- Pegging: «allows the planner to see the demand from which a planned order release arises, by providing a link from the gross requirements of an item to all its sources of demand.» «One use of pegging is bottom-up replanning.» [P1, L, traducción].
- Mensajes de acción (adelantar, postergar, cancelar): P1 habla de «exception reports» sin detalle. Un sistema comercial dice que el proceso no recomienda adelantar dentro de la barrera de planificación, pero «can recommend that you reschedule out or cancel existing orders, even if they fall within the planning time fence» [P3, L]. No hay fuente que defina el conjunto de mensajes. En un sistema abierto, el estado de la reposición del MPS se muestra por color: verde lista, gris igual a lo sugerido, amarillo menor, rojo mayor [planificacion-2.md, G12].
- Reglas de lote [P1, L, traducción; la regla ya está en H1]: lote por lote «Minimizes (zeroes) inventory. Maximizes total setup cost.», atractivo porque «it is simple, consistent with the just-in-time philosophy, and tends to produce a smoother production schedule, since it does not pile up requirements from many periods», «probably the best policy when setup costs are minimal». Cantidad fija: se usa «when the means used to move jobs inside the factory have a specific size» y «because fixing the lot size affects the number of setups»; EOQ con la demanda promedio `Q = sqrt(2AD/h)`. El curso trae una comparación de costo por período fijo con una tabla (se queda con 60 unidades, que cubren los períodos 6, 7 y 8 y dejan 15 para el 9), pero la tabla salió incompleta. Sobre la elección: «There is no one 'ideal' lot sizing technique ... Lot-for-lot is the goal to be sought. However, where setup costs are significant and demand is not particularly lumpy, EOQ is a simple method ... Too much concern with lot sizing yields spurious results because of MRP dynamics.» [P13, L, solucionario].
- Seguridad: «Safety stock: often used to protect against uncertainty in production and demand quantities. Safety lead time: often used to protect against uncertainty in production and demand times.» [P1, L, traducción]. En un sistema abierto, el plazo de seguridad: «moves the scheduled date of the MO forward by a specified number of days»; plazo de fabricación: «number of days needed to complete a manufacturing order (MO) from the date of confirmation», en días corridos. Ejemplo literal: entrega el 15 de agosto, plazo de fabricación 7, plazo de seguridad 3, orden planificada el 5 de agosto (15 - 7 - 3); sin plazo de seguridad, el 8 [P4, L].
- Capacidad infinita: «The basic assumption of MRP is that lead times are fixed and do not depend on the workload of the production system. This implicitly assumes the system will always have sufficient capacity» [P1, L, traducción]. Coincide con H1, diap. 34.
- Historia (frontera con Fundamentos): primera empresa en 1964, Black & Decker, con Dick Alban; unas 700 empresas en 1975 y 8.000 en 1981; «In 1983, Oliver Wight developed MRP into manufacturing resource planning (MRP II)» [P9, S]. Hopp y Spearman vinculan la adopción masiva de los setenta con la «MRP Crusade» de APICS [P15 y un resumen del buscador sobre https://pubsonline.informs.org/doi/pdf/10.1287/msom.1030.0028, S].

### Discrepancias

- Regenerativo frente a cambio neto: una sola fuente (P1, sobre Hopp y Spearman) dice que predomina el regenerativo; ninguna lo contradice ni lo confirma en un sistema.
- Dónde van el RCCP y el CRP en la jerarquía: H1 los pone en el plazo intermedio; P1 pone el RCCP con el MPS y el CRP con el MRP.

### Recurso canónico

Hopp y Spearman, *Factory Physics*, cap. 3 «The MRP Crusade» [P15 da la ubicación; no se leyó]. Mientras tanto: diapositivas MIT 2.854 [H1] para la lógica y las de la Univ. de Tesalia [P1] para regenerativo, cambio neto, pegging y capacidad. Ejemplo numérico propuesto para la nota: el de P2 (cuatro cuentas verificables) o la tabla de H1; no armar uno propio sin marcarlo.

### Qué registra un sistema

- Por ítem: plazo, lote o regla de lote, stock de seguridad, stock disponible, pedido pendiente, «where used» [P2]; plazo de seguridad [P4].
- Por período: necesidades brutas, recepciones programadas, saldo proyectado, necesidades netas, recepciones y lanzamientos planificados [H1, P1, P2].
- Por orden: estado planificada o firme [P1, P3]; en otro sistema abierto, eventos con fecha, tipo, cantidad e indicador de atraso [G14].
- Pegging: vínculo de cada necesidad con su origen [P1].
- En un sistema abierto, el plan de producción calcula con la cantidad proyectada del almacén: «the system will consider the Projected Qty which is available in the bin to calculate the required quantity»; sub-ensambles: «Get Sub Assembly Items will fetch Sub Assembly Items from the BOM of the Finished Good Items» [P11, L]. No menciona stock de seguridad.

---

## 4. Planificación de capacidad

### Afirmaciones

- RCCP: «Rough-cut capacity planning: used to provide a quick check of the capacity of a few critical resources, in order to ensure the MPS is feasible.» «Bill of resources: gives the number of hours required at each critical resource to make one end item.» [P1, L, traducción].
- Ejemplo de RCCP [P1, L; las cuentas verifican]: el ítem A necesita en el centro 21 1 hora, y sus componentes A1 y A2 media hora y 1 hora (total 2,5 horas); el ítem B, 2,0 horas. MPS semanas 1 a 8: A 10, 10, 10, 20, 20, 20, 20, 10; B 5, 25, 5, 15, 10, 25, 15, 10. Horas de A: 25, 25, 25, 50, 50, 50, 50, 25; de B: 10, 50, 10, 30, 20, 50, 30, 10; total 35, 75, 35, 80, 70, 100, 80, 35; disponibles 65 por semana; diferencia +30, -10, +30, -15, -5, -35, -15, +30. Salidas del texto: cambiar las fechas del MPS, o ajustar la capacidad con horas extra o subcontratación. Casi igual en [P13, L]: ante un exceso de una semana, partir una orden hacia antes o después, horas extra, proceso alternativo o subcontratación; ante falta crónica, «a capital investment to increase capacity, add a shift, or develop an outside source».
- CRP: «provides a more detailed check of the MRP-generated schedules than RCCP. CRP performs so-called infinite forward loading. CRP predicts completion times for each work center using fixed lead times and then calculates a forecast workload over time. The loads are compared with available capacity, but no correction is made for overload situations.» [P1, L, traducción]. Ejemplo: un centro con plazo de 3 días y capacidad de 400 piezas por día; recién lanzadas 400, con un día de antigüedad 500, con dos 300; lanzamientos planificados de los días 1 a 5: 300, 350, 400, 350, 300; si se prevén más de 400 en un día, el centro está sobrecargado [P1, L]. Críticas del mismo texto: aun sobrecargado, el CRP supone que el tiempo de paso no cambia, por lo que sirve solo en el horizonte muy cercano; «only finds where the problem is» sin decir causa ni remedio; «due to the serious drawbacks of CRP, fewer and fewer companies use it» [P1, L, traducción].
- Carga infinita frente a finita: P1 y H1 dicen que MRP y CRP son de carga infinita. La carga finita como técnica: sin fuente leída.
- MRP II: «MRP II includes or integrates functions within the firm in addition to the management of dependent demand inventories. Examples of these additional functions include: Order entry, invoicing, billing, purchasing, production scheduling, capacity planning, and warehouse management.» [P13, L]. Fecha y autor: Wight, 1983 [P9, S].
- Planificación de recursos (nivel agregado): «Aggregate planning — determines rough estimates of production, staffing, etc.» [H1, diap. 40-42]. Es frontera con S&OP.
- Un sistema abierto registra: «Disable Capacity Planning: If checked, capacity planning won't be done»; «Allow Overtime: If enabled it'll allow creating work orders, job cards etc. outside workstation working hours»; «Capacity Planning For (Days)»: «the number of days in advance when the capacity planning activities will be initiated»; «Time Between Operations (Mins)» [P12, L]. Es evidencia de datos de capacidad y calendario, no de que haga RCCP ni CRP.

### Recurso canónico

Hopp y Spearman cap. 3 (por intermedio de P1) para RCCP, CRP y la crítica de la capacidad infinita; la tabla del RCCP de P1 como ejemplo literal. Vollmann et al., capítulo de planificación de capacidad: sin leer.

### Qué registra un sistema

- Por centro de trabajo: capacidad por período y calendario [P12].
- Por producto: horas por recurso crítico (lista de recursos) [P1], o tiempos por operación (ruta, otro ángulo).
- Por orden: horas cargadas contra un centro y una fecha, con indicador de sobrecarga [P1].

---

## Sobre la división del árbol

- Las estrategias de respuesta y el CODP son un marco de estrategia de operaciones que atraviesa pronóstico, inventario, diseño y entrega. En el árbol caben en Planificación, pero la nota debe enlazar a Cadena de suministro por el lado de la demanda.
- Los cursos enseñan MPS, RCCP, MRP y CRP como una cascada (plan agregado, MPS con RCCP, MRP con CRP, control de planta) [P1, H1]. El árbol los separa en componentes, lo que coincide con el campo; conviene un esquema de la cascada en la nota de entrada.
- La lista de planificación, la fantasma y la modular de ATO son de Producto-y-proceso; marcar el enlace.
- La carga finita es más de Ejecución en planta (programación) que de Planificación.

## Huecos

1. Barreras de tiempo con zonas congelada, firme y abierta, y las definiciones de «demand time fence» y «planning time fence» del diccionario ASCM: solo documentación de sistemas comerciales [P3, P14] y un wiki [P8].
2. Consumo del pronóstico por pedidos, fórmula del ATP, plan maestro en dos niveles: sin fuente leída.
3. Mensajes de acción (adelantar, postergar, cancelar, liberar): solo una mención en un sistema [P3] y «exception reports» en P1. Falta Orlicky o Vollmann.
4. Qué cambia en la lista de materiales según la estrategia (lista de planificación, módulos con porcentajes): sin fuente.
5. Orlicky (1975), Vollmann et al. y Hopp y Spearman cap. 3: ninguno se leyó (solo el índice y las diapositivas que los siguen). MIT 2.854 de 2010 y ESD.260 no abrieron.
6. Olhager y Van Donk (2024) y Olhager (2003): solo abstract y catálogo; el paper de Cardiff dio 403.
7. Carga finita frente a infinita como técnica: sin fuente.
8. Un campo de «estrategia de respuesta» por producto, un estado «planificada» o «firme» y una barrera de tiempo en el modelo de datos de un sistema abierto: no confirmados.
9. RCCP y CRP en un sistema abierto: solo la página de ajustes [P12].
10. Este ángulo no toca ley ni dinero; no corresponde la regla de dos fuentes independientes.
