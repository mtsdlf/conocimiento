---
resumen: >-
  El MRP (planificación de los requerimientos de materiales) calcula, período por período, cuánto hace falta de cada componente y cuándo lanzar su orden de fabricación o de compra. Parte del plan maestro, resta lo que hay y lo que ya viene, explota la lista de materiales nivel por nivel y corre cada orden hacia atrás por su plazo; es contabilidad, no optimización, y por eso depende de que los datos sean exactos.
estado: borrador
estabilidad: estable
fuentes:
  - "Gershwin, S. B., Material Requirements Planning, diapositivas de MIT 2.853/2.854 (© 2002-2006; MIT OCW, otoño de 2016), diapositivas 3, 19, 23, 25 a 27, 31 a 34: https://ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/4eec617bb52d64f4ea1bed6d9905bc00_MIT2_854F16_MatrialRequire.pdf"
  - "Lymperopoulos, G., Σχεδιασμός και Προγραμματισμός Παραγωγής: MRP (diapositivas, Univ. de Tesalia, 25/11/2015, sobre Hopp y Spearman, Factory Physics, cap. 3; traducción de la base): https://opencourses.uth.gr/modules/document/file.php/MHXB125/MRP.pdf"
  - "Diapositivas «Material Requirements Planning (MRP) for Dependent Demand Systems», SMU, curso 5362 (2004): https://s2.smu.edu/~barr/5362/2004/04p20MRP.pdf"
  - "Apuntes «Chapter 4 Material Requirements Planning», Univ. de Houston, Bauer (hojas MRP1 y POQ): https://www.bauer.uh.edu/egardner/3301H%20Operations%20Management/OM%20Text/4MRP-1.pdf"
  - "Solucionario de preguntas de discusión sobre MRP, curso IE 314, KSU: https://faculty.ksu.edu.sa/sites/default/files/mrp.pdf"
  - "Documentación de «Lead times» de un sistema abierto (v17.0): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/lead_times.html"
  - "Documentación de un sistema comercial, «Time Fence Control»: https://docs.oracle.com/cd/E18727_01/doc.121/e15188/T478564T479135.htm"
  - "Documentación de un sistema comercial, «Action Messages» (según el resumen): https://docs.infor.com/m3udi/16.x/en-us/m3beud/scplanhs/rps001.html"
  - "Blackburn, J. D., Kropp, D. H. y Millen, R. A. (1986), «A Comparison of Strategies to Dampen Nervousness in MRP Systems», Management Science 32(4), 413-429, DOI 10.1287/mnsc.32.4.413 (según el resumen): https://ideas.repec.org/a/inm/ormnsc/v32y1986i4p413-429.html"
  - "Wagner, H. M. y Whitin, T. M. (1958), «Dynamic Version of the Economic Lot Size Model», Management Science 5(1), 89-96, DOI 10.1287/mnsc.5.1.89 (según el resumen): https://econpapers.repec.org/RePEc:inm:ormnsc:v:5:y:1958:i:1:p:89-96"
  - "Wikipedia, Silver–Meal heuristic (secundaria; Silver y Meal, 1973, Production and Inventory Management 14): https://en.wikipedia.org/wiki/Silver%E2%80%93Meal_heuristic"
  - "Orlicky, J. (1975), Material Requirements Planning: The New Way of Life in Production and Inventory Management, McGraw-Hill, ISBN 0070477086 (registro, préstamo controlado; no leído): https://archive.org/metadata/materialrequirem00orli"
  - "Ptak, C. A. y Smith, C. (2011), Orlicky's Material Requirements Planning, 3.ª ed., McGraw-Hill, ISBN 9780071755634, y 4.ª ed. (2023), McGraw-Hill Education, ISBN 9781264264575 (registros; no leídos): https://openlibrary.org/search.json?q=orlicky+material+requirements+planning"
  - "Produccion/.investigacion/planificacion.md (sección 3) y planificacion-2.md (secciones 4 a 6), 2026-11-27; Cadena-de-suministro-y-logistica/.investigacion/planificacion-3.md (H1)"
aliases: [MRP, planificación de los requerimientos de materiales, planificación de necesidades de materiales, material requirements planning, MRP I, plan de materiales, materials plan, necesidades brutas, gross requirements, necesidades netas, net requirements, neteo, netting, explosión, explosion, desfase, offsetting, lotificación, lot sizing, lote por lote, lot for lot, L4L, cantidad fija de pedido, fixed order quantity, FOQ, período fijo, fixed order period, cantidad por período, period order quantity, POQ, Wagner-Whitin, Silver-Meal, recepción programada, scheduled receipt, orden planificada, planned order, orden planificada firme, firm planned order, mensaje de acción, action message, mensaje de excepción, exception message, rastreo de la demanda, pegging, regenerativo, regenerative MRP, cambio neto, net change, nerviosismo, nervousness, plazo de seguridad, safety lead time, demanda dependiente, dependent demand]
creado: 2026-11-27
revisado:
---

# MRP

El MRP (planificación de los requerimientos de materiales) calcula, período por período, cuánto hace falta de cada componente y cuándo lanzar su orden de fabricación o de compra. Parte del plan maestro, resta lo que hay y lo que ya viene, explota la lista de materiales nivel por nivel y corre cada orden hacia atrás por su plazo; es contabilidad, no optimización, y por eso depende de que los datos sean exactos.

Es el tercer escalón de [Planificación de la producción](planificacion-de-la-produccion.md). Las diapositivas de SMU lo dicen sin vueltas: un MRP «Uses little mathematics, primarily bookkeeping». Sus entradas son «Master schedule, Bill of materials, Inventory records»: el [plan maestro de producción](plan-maestro-de-produccion.md), la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) y el stock de [Inventario](../../Inventario-y-depositos/inventario-y-depositos.md). Sus salidas son las órdenes planificadas, los avisos de cambio y los informes de excepción.

## Demanda dependiente: por qué no alcanza el punto de pedido

El MIT separa la demanda que viene «from outside the system», independiente, de la de «components or raw material», dependiente. La segunda no se pronostica: se calcula desde el plan del producto que la usa. El [punto de pedido](../../Inventario-y-depositos/Reposicion/punto-de-pedido.md) de Inventario repone mirando el consumo; el MRP mira el plan hacia adelante.

## El neteo: lo que falta después de usar lo que hay

Para cada artículo y período, el MRP resta de las necesidades brutas el stock proyectado, que ya incluye las recepciones programadas (órdenes abiertas que todavía no llegaron). Unos apuntes de Houston dan la fórmula con stock de seguridad: «(gross requirements this week) + (safety stock) - (inventory on hand at the beginning of this week)», y si da negativo, cero. El stock inicial es el disponible, no el físico: «The beginning inventory is 50 units, with 20 units allocated to future production. Thus the initial inventory available is 50 - 20 = 30 units».

Juntando esa fuente y el MIT, la cuenta de la base es:

> necesidad neta = máx(0; necesidad bruta + stock de seguridad − stock proyectado al empezar el período − recepciones programadas del período)

Un ejemplo del MIT, con 20 unidades en stock y dos recepciones programadas (20 en la semana 2 y 100 en la 3):

| Semana | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Necesidades brutas | 15 | 20 | 50 | 10 | 30 | 30 | 30 | 30 |
| Recepciones programadas | | 20 | 100 | | | | | |
| Stock proyectado | 5 | 5 | 55 | 45 | 15 | −15 | | |
| Necesidades netas | 0 | 0 | 0 | 0 | 0 | 15 | 30 | 30 |

Las cuentas verifican (20 − 15 = 5; 5 − 20 + 20 = 5; 5 − 50 + 100 = 55; hasta 15 − 30 = −15), y desde la semana 6 falta todo lo que se pide. Con lote por lote, las recepciones planificadas son 15, 30 y 30 en las semanas 6, 7 y 8; con un plazo de una semana se lanzan en la 5, 6 y 7 (cuenta de la base: la fuente no da el plazo para este ejemplo). El caso con lotes de 75 está resuelto en [planificación de la distribución](../../Cadena-de-suministro-y-logistica/Planificacion/planificacion-de-la-distribucion.md#la-tabla-por-período-con-el-ejemplo-de-mit), de Cadena, que usa la misma cuenta entre depósitos.

## Explosión y desfase: de un nivel al de abajo

Cada orden se corre hacia atrás por su plazo: con «Lead times are 1 week», el lanzamiento «must occur one week before delivery is required» (MIT). Los lanzamientos del padre son las necesidades del hijo: «The planned order releases for Level 0 are the gross requirements for Level 1», y así en cada nivel. El MRP procesa por [código de nivel más bajo](../Producto-y-proceso/lista-de-materiales.md#código-de-nivel-más-bajo), para netear una sola vez un componente que aparece en varias ramas. Los apuntes de Houston agregan el rendimiento: el lanzamiento se ajusta «by the yield percentage», y 300 unidades con 98 % piden 306.

El plazo es un dato fijo de cada artículo: el cálculo no lo alarga cuando la planta está cargada, ni mira si las horas alcanzan. El MIT lo formula como un modelo «deterministic» y de «infinite capacity». Qué pasa cuando el plan no entra está en [planificación de capacidad](planificacion-de-capacidad.md#carga-infinita-y-carga-finita), y lo que la evidencia dice de planificar con plazos fijos, en [fundamentos de producción](../Fundamentos/fundamentos-de-produccion.md#lo-que-la-evidencia-discute-de-las-ideas-más-repetidas).

Las diapositivas de SMU encadenan tres niveles. Un subconjunto con lote de 15, plazo de 3 semanas y 10 en stock necesita 3 en el período 2, 8 en el 7 y 10 en el 10. El saldo baja a 7 y en el 7 daría −1: hace falta recibir 15 en el período 7, que se lanzan en el 4, y el saldo queda en 14 y después en 4. Ese lanzamiento es una necesidad de 15 del componente de abajo, con su propio plazo de 3 semanas, que lanza en el período 1. En el tercer nivel, una pieza con 11 en stock pasa por −4 antes de que una recepción programada de 25 la lleve a 21. Las cuentas son de la base sobre las filas de la fuente, que salen desalineadas. Un saldo negativo con una recepción ya en camino no pide una orden nueva: pide adelantar la que existe, que es un mensaje de acción (lectura de la base).

## Lotificación: cuánto pedir de una vez

La necesidad neta casi nunca es lo que conviene fabricar o comprar. El MIT da tres reglas:

- **Lote por lote**: «produce in a period the net requirements for that period. Maximum setups.» Según Tesalia, es simple, coherente con el justo a tiempo y «probably the best policy when setup costs are minimal».
- **Cantidad fija**: «always produce the same quantity, whenever anything is produced. EOQ formula can be used to determine lot size.» Tesalia la justifica cuando los medios de transporte internos tienen un tamaño fijo. Hay empresas que la usan como mínimo: «Some companies treat the lot size as a minimum and do not round up to the nearest even multiple» (Houston).
- **Período fijo**: «produce in a period the net requirements for P periods.»

El [lote económico](../../Inventario-y-depositos/Reposicion/lote-economico.md), de Inventario, supone demanda constante, y en el MRP no lo es. Los apuntes de Houston lo explican: la demanda de componentes es «"lumpy," that is, discontinuous and nonuniform», y con un EOQ quedan restos que se guardan sin necesidad. La cantidad por período (POQ) pide solo períodos enteros: se calcula el EOQ, se ve cuántos períodos promedio cubre y se redondea. En su ejemplo, 194 / 103,1 = 1,9, que da 2 semanas.

El ejemplo compara las dos reglas con 25 en stock, preparación de 27,50 y costo de mantener de 0,15 por unidad y semana:

| Semana | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Demanda | 100 | 0 | 175 | 50 | 0 | 125 | 75 | 300 |
| EOQ: recepción | 194 | | 194 | | | 194 | | 218 |
| EOQ: stock al cierre | 119 | 119 | 138 | 88 | 88 | 157 | 82 | 0 |
| POQ: recepción | 75 | | 225 | | | 200 | | 300 |
| POQ: stock al cierre | 0 | 0 | 50 | 0 | 0 | 75 | 0 | 0 |

La fuente da 228,65 de costo total con EOQ y 18,75 con POQ, y ese segundo número está mal. Con EOQ: 4 × 27,50 + 0,15 × 791 = 228,65, que verifica. Con POQ, 0,15 × 125 = 18,75 es solo el costo de mantener; con las mismas 4 preparaciones, el total es 110 + 18,75 = 128,75 (cuenta de la base). POQ sigue ganando, pero por unos 100 y no por unos 210.

Hay métodos que buscan el lote de menor costo con demanda variable. Wagner y Whitin (1958) dieron un algoritmo exacto que, según su resumen, busca «a minimum total cost inventory management scheme which satisfies known demand in every period». Silver y Meal (1973) propusieron una heurística que extiende el pedido mientras baja el costo promedio por período («until C(T) > C(T − 1)», según Wikipedia). Ninguno se leyó en el texto original. Un solucionario de un curso pone el límite: «There is no one 'ideal' lot sizing technique ... Too much concern with lot sizing yields spurious results because of MRP dynamics».

## Stock y plazo de seguridad dentro del plan

El MIT dice: «MRP is deterministic but reality is not. Therefore, the system needs safety stock and safety lead times». En el plan, el stock de seguridad cambia el piso: «Instead of having a minimal planned inventory of zero, the (positive) safety stock is the planned minimal inventory level». Tesalia los separa por lo que cubren: el stock, la incertidumbre en las cantidades; el plazo, la incertidumbre en los tiempos. Cómo se dimensiona el stock de seguridad es de [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md), de Inventario.

El plazo de seguridad adelanta la orden. Un sistema abierto lo define como el que «moves the scheduled date of the MO forward by a specified number of days». Su ejemplo: entrega el 15 de agosto, plazo de fabricación de 7 días y de seguridad de 3; la orden se planifica el 5 de agosto, y sin plazo de seguridad, el 8.

## Órdenes planificadas, firmes y mensajes de acción

La orden planificada es una propuesta que el MRP recalcula en cada corrida; la orden planificada firme no la toca. Tesalia las define como órdenes «held fixed and scheduled to start whatever the changes in the system», que «stabilize the production schedule and serve to reduce system nervousness». Una vez liberada, la orden de fabricación pasa a [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md), y la de compra, a [solicitud de compra](../../Compras-y-abastecimiento/Orden-de-compra/solicitud-de-compra.md).

Sobre las órdenes que ya existen, el MRP no cambia nada: sugiere. La documentación de un sistema comercial lo llama mensaje de acción, que «suggests performing a certain planning action», en tres categorías:

| Categoría | Ejemplos de ese sistema |
|---|---|
| Liberar | lanzar una orden planificada cuya fecha llegó; volverla firme porque entró en la barrera de planificación |
| Reprogramar | adelantar una orden liberada; postergarla porque ya no hace falta tan pronto; borrarla porque no hace falta |
| Demorada | avisar que una orden está o puede estar atrasada |

Las barreras del [plan maestro](plan-maestro-de-produccion.md#barreras-y-zonas-de-tiempo) filtran los mensajes: otro sistema comercial no recomienda adelantar dentro de la barrera de planificación, pero sí postergar o cancelar.

> [!NOTE] Sin fuente todavía: el conjunto de mensajes de acción en una fuente de fundamentos (Orlicky o Vollmann); los leídos son de un sistema.

## Rastreo de la demanda

El rastreo («pegging»), según Tesalia, «allows the planner to see the demand from which a planned order release arises, by providing a link from the gross requirements of an item to all its sources of demand». Sirve para replanificar desde abajo: si falta un componente, el planificador ve qué pedido de cliente se atrasa. Cuando se [fabrica contra pedido](fabricar-para-stock-o-contra-pedido.md), el vínculo llega al pedido de venta.

## Regenerativo o de cambio neto

Según Tesalia, el regenerativo descarta los lanzamientos planificados que no se volvieron órdenes y rehace todo desde el plan maestro; el de cambio neto recalcula solo los artículos cuya demanda cambió, más rápido pero con peores lotes. Dice que «Most modern MRP systems use the regenerative method» (una sola fuente). Recalcular muy seguido manda a la planta «a storm of exception reports»; muy espaciado, deja el plan viejo.

## Por qué el MRP es nervioso

El MIT llama nerviosismo a los «drastic changes in schedules due to small deviations from plans», que aparecen cuando «a deterministic calculation is applied to a random system». Cuesta cambios que confunden a la planta y preparaciones de más. El remedio que propone es congelar el tramo cercano, con una advertencia: «But: What price is paid for freezing?».

Blackburn, Kropp y Millen (1986) compararon por simulación cinco estrategias contra el nerviosismo que viene de la lotificación y del horizonte móvil. Según su resumen, el stock de seguridad y el lote por lote no son efectivos en costo contra el horizonte móvil, y cobrar un costo por cambiar o congelar el programa «appear to be dominant». Lo que la evidencia discute del MRP sigue en [fundamentos de producción](../Fundamentos/fundamentos-de-produccion.md).

## El libro de origen

El texto fundacional es Joseph Orlicky, *Material Requirements Planning: The New Way of Life in Production and Inventory Management*, McGraw-Hill, 1975, ISBN 0070477086 (un registro lo fecha en 1974 con el mismo ISBN). La 3.ª edición, *Orlicky's Material Requirements Planning*, es de Carol A. Ptak y Chad Smith (McGraw-Hill, 2011, ISBN 9780071755634); la 4.ª, de los mismos autores, de 2023 (ISBN 9781264264575). Ninguna se leyó: la nota no las cita.

## Qué guarda un MRP

- Por artículo: plazo, plazo de seguridad, regla y tamaño de lote, stock de seguridad, rendimiento, código de nivel más bajo y dónde se usa.
- Por artículo y período: necesidades brutas, recepciones programadas, stock proyectado, necesidades netas, recepciones y lanzamientos planificados.
- Por orden: estado (planificada, firme, liberada), fechas, cantidad y el rastreo hacia su demanda.
- Por corrida: los mensajes de acción, con código y orden, y la versión del plan, para medir cuánto cambió.
