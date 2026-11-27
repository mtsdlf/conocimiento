# Planificación de la producción, segunda ronda: huecos cerrados

Fecha: 2026-11-27. Continúa `planificacion.md` (ids P1 a P15, H1, G12 a G14 se citan igual). Marcas: [L] texto completo leído (PDF bajado y extraído a texto, no resumido por un lector), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes: autoridad / profundidad / ejemplos / unicidad (1 a 3).

Cómo se leyó: el lector de páginas devuelve resúmenes y corta las citas a unas 125 letras. Para evitarlo se bajaron los PDF y se extrajeron con `pdftotext`; las citas de abajo salen de ese texto. Lo que solo se vio por el lector va marcado [S] o [M].

## Fuentes nuevas

| Id | Fuente | URL | Tipo | Puntaje | Marca |
|---|---|---|---|---|---|
| Q1 | ASCM/APICS, *CPIM Version 6.1, 2019 Edition*, Módulo 1 (BSCM), sección F «Master Planning», pp. 1-207 a 1-211 (extracto público de muestra; cita el *APICS Dictionary*, 15.ª ed.) | https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf | primaria (material oficial de ASCM; el extracto es una muestra) | 3/3/3/2 | [L] 289 líneas. Las tablas de las figuras 1-79 a 1-81 son imágenes: no están en el texto, solo las cuentas |
| Q2 | ASCM, *CPIM LS 2020 Excerpt* (v6.2), muestra | https://learningsystem.ascm.org/wp-content/uploads/2019/11/CPIM_LS_2020_Excerpt.pdf | primaria | 3/1/1/1 | [L] 429 líneas. Solo trae la historia de MRP abierto, cerrado, MRP II y ERP; nada de barreras ni lotes |
| Q3 | IBM, *COPICS, Volume III: Chapter 3 Forecasting, Chapter 4 Master Production Schedule Planning*, 1.ª ed., marzo de 1972, form G320-1976-0 (128 págs.) | https://mirrorservice.org/sites/www.bitsavers.org/pdf/ibm/370/COPICS/G320-1976-0_COPICS_Volume_3_197203.pdf | primaria histórica (manual de un fabricante de computadoras de la época de Orlicky) | 2/3/2/3 | [L] 6.263 líneas con OCR; ver notas de abajo |
| Q4 | Gershwin, S. B., *MIT 2.853/2.854 Introduction to Manufacturing Systems, Material Requirements Planning* (diapositivas, © 2002-2006; copia 2016 de OCW). Es la misma serie que H1, releída en el PDF | https://ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/4eec617bb52d64f4ea1bed6d9905bc00_MIT2_854F16_MatrialRequire.pdf | secundaria (curso abierto; fuente declarada: Hopp y Spearman) | 3/2/3/1 | [L] 674 líneas |
| Q5 | Apuntes «Chapter 4 Material Requirements Planning» (Univ. de Houston, Bauer; hoja de cálculo MRP1 y POQ de Houston Oil Tools). Sin autor visible en el PDF | https://www.bauer.uh.edu/egardner/3301H%20Operations%20Management/OM%20Text/4MRP-1.pdf | secundaria (apuntes con ejemplo numérico) | 1/2/3/2 | [L] 282 líneas |
| Q6 | Petropoulos, F. et al. (2025), *Operations & Supply Chain Management: Principles and Practice*, arXiv:2503.05749v2 (CC BY 4.0) | https://arxiv.org/pdf/2503.05749 | primaria/secundaria (revisión colectiva abierta) | 2/1/1/3 | [L] 11.306 líneas; solo cuatro pasajes útiles (CODP, lotes, MRP-I y II) |
| Q7 | Harfeldt-Berg, M. (2024), tesis doctoral, Lund University (supervisor Olhager), ISBN 978-91-8104-164-4 | https://lup.lub.lu.se/search/files/194792365/e-spik_ex_Magnus.pdf | secundaria (tesis abierta que cita a Sharman y Hoekstra y Romme) | 2/2/1/2 | [L] 4.036 líneas, la introducción |
| Q8 | Documentación de un sistema comercial, «Forecast Consumption» (JD Edwards EnterpriseOne 9.1, Requirements Planning, cap. 10) | https://docs.oracle.com/cd/E16582_01/doc.91/e15139/forecast_consumption.htm | primaria (documentación de un sistema; comercial, no abierto) | 2/2/1/2 | [S] el lector devolvió citas literales; la página no se bajó entera |
| Q9 | Documentación de un sistema comercial, «Action Messages» (Infor M3) | https://docs.infor.com/m3udi/16.x/en-us/m3beud/scplanhs/rps001.html | primaria (documentación de un sistema) | 2/2/1/2 | [S] citas literales del lector |
| Q10 | Documentación de un sistema comercial, «Time Fences and the Time Series» (JD Edwards 9.2) | https://docs.oracle.com/en/applications/jd-edwards/supply-chain-manufacturing/9.2/eoarp/time-fences-and-the-time-series.html | primaria (documentación) | 2/1/1/1 | [S] |
| Q11 | Documentación de un sistema comercial, «Finite capacity planning and scheduling» (Microsoft Dynamics 365 SCM) | https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/finite-capacity | primaria (documentación) | 2/2/2/2 | [L] la página (vino como Markdown entero) |
| Q12 | ERP Information, «Frozen Zone in Supply Chain (Slushy, Liquid & Time Fences)» (blog de un sitio comercial; «Editorial Staff»; no cita a APICS) | https://www.erp-information.com/frozen-zone.html | secundaria débil | 1/1/1/1 | [S] citas del lector |
| Q13 | Open-exam-prep, «6.3 Using and Maintaining the Master Schedule» (guía comercial de estudio de CPIM) | https://open-exam-prep.com/study-guides/cpim/master-scheduling/using-maintaining-mps | secundaria débil | 1/1/1/1 | [S] |
| Q14 | Diapositivas «Master Production Schedule» en SlideShare (sin autor ni curso visibles) | https://www.slideshare.net/slideshow/master-production-schedule-mpspptx/261096678 | secundaria débil | 1/1/3/1 | [S] el lector devolvió las tablas; no verificadas contra el original |
| Q15 | Blackburn, J. D., Kropp, D. H. y Millen, R. A. (1986), «A Comparison of Strategies to Dampen Nervousness in MRP Systems», *Management Science* 32(4), 413-429. DOI 10.1287/mnsc.32.4.413 | https://ideas.repec.org/a/inm/ormnsc/v32y1986i4p413-429.html | primaria (paper; registro con abstract) | 3/2/1/3 | [M] abstract; el lector solo dio citas cortas |
| Q16 | Wagner, H. M. y Whitin, T. M. (1958), «Dynamic Version of the Economic Lot Size Model», *Management Science* 5(1), 89-96. DOI 10.1287/mnsc.5.1.89 | https://econpapers.repec.org/RePEc:inm:ormnsc:v:5:y:1958:i:1:p:89-96 | primaria (paper; registro con abstract) | 3/2/1/3 | [M] abstract |
| Q17 | Silver–Meal heuristic (Wikipedia) | https://en.wikipedia.org/wiki/Silver%E2%80%93Meal_heuristic | secundaria | 1/1/1/1 | [S] |
| Q18 | Wikipedia, «Final assembly schedule» | https://en.wikipedia.org/wiki/Final_assembly_schedule | secundaria | 1/1/1/1 | [S]; cita un solo libro (Sheikh 2003) |
| Q19 | Documentación de un sistema comercial, «Overview of Two-Level Master Scheduling» (Oracle MRP, versión antigua) | https://docs.oracle.com/cd/A60725_05/html/comnls/us/mrp/2levover.htm | primaria (documentación) | 2/1/1/1 | [S] |
| Q20 | Beasley, J. E. (Brunel), apuntes de MRP | https://people.brunel.ac.uk/~mastjjb/jeb/or/mrp.html | secundaria (apuntes) | 1/2/2/1 | [S] |
| Q21 | Open Library e Internet Archive, registros de Orlicky (1975) y de la 3.ª y 4.ª ediciones | https://openlibrary.org/search.json?q=orlicky+material+requirements+planning ; https://archive.org/metadata/materialrequirem00orli | primaria bibliográfica | 2/1/1/2 | [M] |

No abrieron: el PDF de apuntes de la EMU sobre planificación de la producción (devuelve 401 y es el que el buscador describía con barreras, ATP y un ejemplo de bombas; sin leer), la página de IFS (`ENOTFOUND`), las diapositivas de MIT 2.854 de 2010 en dspace (404), el capítulo de O'Reilly sobre «Stabilizing the MPS» (403), la página de CSUS (404), la de UNCG (conexión rechazada), Academia.edu (403), el libro de Proud *Master Scheduling* en un servidor con certificado inválido, la API de Google Books (429), el registro de la 3.ª edición de Texas A&M (403), el de la Univ. de Hertfordshire (bloqueo antibots) y el PDF del capítulo de Springer (redirección a login).

---

## 1. Barreras y zonas de tiempo del plan maestro (hueco 1)

### Lo que se encontró

- **Zona «slushy» y quién autoriza**, texto de ASCM [Q1, L], a propósito de un pedido que no entra en el ATP: «If the order was higher than this sum, it would require a new MPS entry and thus would be subject to master scheduler approval, since it is in the slushy zone and changing the schedule could impact production efficiency.» Es la única mención literal de la palabra «slushy» en una fuente primaria; el extracto no define la zona ni las barreras.
- **Barreras en lean**, de la misma fuente [Q1, L]: «For the portion of production in which lean uses demand pull signals, it will operate on orders rather than forecasts and so will not use time fences.» y «For these push elements, lean can benefit from using time fences, because schedule stability in turn promotes production stability.»
- **Congelado en 1972** [Q3, L], con la palabra «frozen» entre comillas ya entonces: «If desirable, the schedule can be defined as "frozen" over a given time span beyond the current date - say, for the next month (Figure 34).» El pie de la figura: «Changes to the schedule cannot normally be made over this period» y «A production schedule can be "frozen" over a given time span». Es el antecedente de la zona congelada, sin los términos «barrera de demanda» ni «de planificación».
- **Parte firme y parte tentativa**, misma fuente [Q3, L]: «This evokes the concept of tentative and firm portions of the master production schedule. Assuming that the schedule covers a period of 18 months ahead, everything that appears within the first six-month segment of that schedule represents the firm portion, that is, products in various stages of commitment and correspondingly difficult to change.» «The tentative portion represents merely a plan for the execution of which money has not yet been expended. The firm portion of the schedule is of the same length at any time. It moves along the time scale, with the passage of time, progressively covering what has formerly been the tentative area.» El criterio: «The consequences (cost) of a previous decision constitute the practical limits of changing that decision.» Y «If the total manufacturing lead time is six months, there is significant difference in impact and cost between changing something that is six months away from completion and changing something that is five months away from completion.» El ejemplo de 18 y 6 meses es de la fuente, no una norma.
- **Quién cambia el plan en 1972** [Q3, L]: los cambios al plan los decide un grupo de gestión con el sistema: «The management group thinks that these could probably be transferred from another underloaded department, and verifies this possibility...»; «Once the changes are agreed upon ... The system is accordingly "informed" that the changes to the schedule should be made firm.»
- **Definiciones de un sistema comercial** (ya en P3, [L]): barrera de demanda, barrera de planificación, barrera de liberación y orden firme; no se repiten.
- **Otro sistema comercial** [Q10, S]: «Freeze Fence (F): The number of days from the generation start date during which the system should not create or replan order messages.» «Imbalances of supply and demand within the freeze fence are planned outside the freeze fence.» «Planning Fence (P): The number of days that the system uses with the time fence rule to determine how demand is used.» Además, la página dice de sí misma que no usa «frozen», «firm» ni «open» como zonas ni nombra a quién cambia.
- **Zonas y autorizaciones, solo en fuentes débiles**:
  - [Q12, S], blog comercial sin fuente primaria: «The frozen zone is the near-term part of the master production schedule where changes are blocked»; «Demand time fence (DTF) is the nearer fence, and the edge of the frozen zone.»; «Planning time fence (PTF) is the farther fence, and the edge of the slushy zone.»; «Outside the fence, in the liquid zone, you can freely revise» las órdenes. Quién autoriza (tabla de la página): congelada, «Whoever the change policy names, usually senior management»; slushy, «Master scheduler with sales and manufacturing agreement»; líquida, «The planning system, within plan limits, with no cost penalty».
  - [Q13, S], guía comercial de CPIM: congelada, «Changes discouraged or barred without high-level approval»; slushy, «Changes allowed with trade-off analysis and planner negotiation»; líquida, «MPS can be regenerated or freely adjusted to forecast». «The demand time fence marks where actual demand takes priority over forecast for calculating requirements in the MPS grid.» «A human planner (sometimes with manager approval) must authorize changes.»
  - Otro texto, citado por el buscador sin abrir la página, atribuye al diccionario de APICS esta frase sobre la barrera de demanda: «the Demand Time Fence may correspond to that point in the future inside which changes to the Master Schedule must be approved by an authority other than the Master Scheduler.» Sin leer la fuente: no se puede atribuir al diccionario.

### Discrepancias

- Dos barreras (demanda y planificación; IFS, Q12, Q13) frente a tres (Oracle, con la de liberación; P3) frente a «congelar» y «planificar» con otro sentido (JD Edwards, Q10). Q12 y Q13 coinciden en que la zona congelada llega hasta la barrera de demanda y la líquida empieza después de la de planificación; el sistema de Q10 llama «planning fence» a otra cosa (la que decide cómo se usa la demanda).
- La frase «dentro de la barrera de demanda cuenta solo el pedido» está en P3 (Oracle) y en Q13; la zona «congelada» de Q12 y Q13 es la misma región. En ASCM (Q1) el pedido nuevo en la zona slushy va al master scheduler, no a la dirección.
- Los números (1-2, 3-5 semanas, etc.) varían entre fuentes: son ilustrativos.

### Hueco que queda

La definición literal de «demand time fence» y «planning time fence» en el *APICS Dictionary* o en un libro de texto (Vollmann, Proud): no se leyó. Lo más cercano a un texto fundacional es COPICS (Q3). La palabra «liquid» no aparece en ninguna fuente primaria leída. Para la nota: citar Q1 para «slushy» y quién aprueba, Q3 para el origen, P3 y Q10 como evidencia de cómo un sistema lo implementa, y decir que las tres zonas con esos nombres vienen de material de estudio.

---

## 2. Consumo del pronóstico y disponible para prometer (hueco 2)

### Disponible para prometer, método discreto (ASCM) [Q1, L]

Definición del diccionario, 15.ª ed., citada en Q1: «In operations, the uncommitted portion of a company's inventory and planned production maintained in the master schedule to support customer-order promising. The ATP quantity is the uncommitted inventory balance in the first period and is normally calculated for each period in which an MPS receipt is scheduled. In the first period, ATP includes on-hand inventory less customer orders that are due and overdue.»

Fórmulas literales:

- «First Period ATP = Beginning Inventory − Sum of Customer Orders Before Period Containing First Scheduled MPS Receipt»; ejemplo: «First Period ATP = 70 units − 48 units = 22 units».
- «ATP for Periods Containing MPS = Scheduled MPS Receipt − Sum of Customer Orders Before Next Period Containing Scheduled MPS Receipt»; ejemplo: «ATP for Period 2 = 100 units − 66 units = 34 units».
- Regla adicional, cuando los pedidos superan el MPS: «Reduce the prior ATP by the amount by which the next ATP would be negative, and then add this amount to the negative ATP field so it is no longer negative.»

Ejemplo numérico completo de Q1 (MPS de 100 por lote, existencia inicial 70):

- Semana 1: 70 − 48 = 22.
- Semana 2: 100 − 66 = 34.
- Semana 3: 100 − (57 + 62) = −19.
- Semana 5: 100 − (30 + 0) = 70.
- Corrección por la regla: «Week 2: 100 units MPS – 66 units of orders – 19 units = 15 units ATP»; «Week 3: 100 units MPS – (57 + 62 units of orders) + 19 units = 0 units ATP».
- Uso: «If the customer wants immediate shipping, the salesperson can promise up to 22 units of this inventory. Even though the beginning inventory is 70 units, 48 of these are committed to customers who already placed their orders.» «If the customer can wait a week, the salesperson can promise up to 15 additional units.» «As soon as an order is entered into the system, the system automatically adjusts the customer orders higher and reduces the ATP.»

La nota debe saber que los pedidos por período salen de la figura 1-80 (imagen), así que el reparto de pedidos entre semanas 4 y 5 no se leyó: solo las cuentas del texto.

Otras definiciones literales de Q1:

- «Order promising: The process of making a delivery commitment (i.e., answering the question, "When can you ship?"). For make-to-order products, this usually involves a check of uncommitted material and availability of capacity, often as represented by the master schedule available-to-promise.»
- «Order entry: The process of accepting and translating what a customer wants into terms used by the manufacturer or distributor. The commitment should be based on the available-to-promise (ATP) line in the master schedule.»
- «Available inventory: The on-hand inventory balance minus allocations, reservations, backorders, and (usually) quantities held for quality problems.»
- «the committed portion of the MPS, in the form of actual orders, leaves the uncommitted portion to be promised to customers who have not yet ordered, which is called available-to-promise (ATP).»
- «The closer one gets to the present, the more the cumulative actual orders displace forecasts or available capacity.»
- Q1 nombra otros dos métodos, «cumulative with look-ahead and cumulative without look-ahead», sin presentarlos.
- Capaz de prometer: «The process of committing orders against available capacity as well as inventory ... Employs a finite-scheduling model of the manufacturing system to determine when an item can be delivered.» (Ver sección 8.)
- Una respuesta de práctica del curso, en el mismo PDF (CPIM 6.0, 2018): con MPS de 100 y pedidos de 46 y 63, «100 units – (46 units + 63 units) = – 9 units», se corrige a 0 «because this would result in a negative value».

### ATP acumulado y regla del pronóstico [Q14, S: tablas no verificadas]

Ejemplo de SlideShare: lote 30, stock de seguridad 5, MPS 30 en los períodos 1 y 3, existencia inicial 20. Pronóstico 5, 5, 8, 10, 15; pedidos 5, 3, 2, 0, 0. Fórmula de la diapositiva: «Previous available + MPS – MAX(Forecast, Orders)». Saldo proyectado 15, 10, 32, 22, 7 (P3: 10 + 30 − máx(8; 2) = 32). ATP discreto: P1 = 20 − 8 = 12; P3 = 30 − 2 = 28. ATP acumulado: P1 = 12; P3 = 12 + 30 − 2 = 40. Frase: la demanda es el máximo entre pronóstico y pedidos, regla «conservadora». Las cuentas verifican entre sí, pero el original no se vio y la fuente no tiene autor; sirve como segunda opinión del acumulado, no como cita.

### Consumo del pronóstico

- Definición literal de un sistema comercial [Q8, S]: «Forecast consumption is based on the assumption that actual sales orders reduce, or consume, the forecasted quantities. This approach ensures that sales orders are not treated as additional demand to the forecast during a planning period. The plan begins with gross forecast. Actual sales orders are placed that consume the forecast. The result is an adjusted forecast-that is, the forecast balance not consumed by sales orders.» «Within an FCP, the system processes sales orders against the gross (unadjusted) forecast ... on a first-in, first-out (FIFO) basis.» Además: «The aggregate forecast will be reduced by the aggregate sale orders for a period.» Por cliente: el sistema «only reduces the forecast quantities for specific customers by the sales order quantities for the same customer.»
- Antecedente de 1972 [Q3, L]: «When not shipping from stock, orders from customers are normally received in advance of final assembly. Each order received is then allocated against the master production schedule. Provided the demand is covered by the schedule, no further action is necessary.» «When the order does not fit the schedule ... a decision must be made either to change the schedule or to postpone the delivery date of the order. The criterion again is, "What would be the effect on resource requirements?" Increasing the schedule is possible only if INVENTORY MANAGEMENT confirms that material will be available, and if the additional capacity can be provided.» Es la idea de que el pedido consume el plan, antes de la palabra.
- Regla del máximo y de la barrera: P3 (dentro de la barrera de demanda cuenta solo la demanda real) y Q14 [S] (máximo entre pronóstico y pedidos).

### Hueco que queda

No se encontró un apunte universitario legible con la tabla completa del MPS con «projected on-hand», pronóstico, pedidos y ATP (el de la EMU dio 401). La fuente más sólida es Q1 (ASCM): fórmulas y ejemplo literales, con las figuras como imagen. La fórmula del ATP acumulado y la del consumo hacia adelante y hacia atrás en una fuente académica: sin leer.

---

## 3. Plan maestro en dos niveles, lista de planificación y FAS (hueco 3)

- **Antecedente de 1972** [Q3, L], sobre la lista de opciones: «There may, however, be a number of options and accessories that are not specified until the firm customer order is received.» «Historically, A has been used on the average 40% of the time and B 60%. If the production schedule calls for a total of 100 units, we can estimate that 40 of option A and 60 of option B need to be available to make 100.» «One common approach in material requirements planning is to provide some sort of cushion, or protection, in addition to the average requirements of the options. For example, one could add "10% for protection" and cover 44 of option A and 66 of option B.» Otra: probabilidad de cada opción por pedido y buffer por la distribución binomial. Todo es la lógica de la lista de planificación con porcentajes, sin el nombre «planning bill».
- **Programa de ensamble final** [Q3, L]: «In some industries, the master production schedule and the final assembly schedule may be identical. This would be the case with relatively simple products that have few or no optional features ... This would also be the case with more complex products produced "to order".» «In industries that produce complex products to anticipated future demand (that is, where the manufacturing lead time exceeds customer delivery time), the final assembly schedule is created - usually on receipt of actual orders - later in time than the master production schedule.» «This means that the availability of components, including assemblies, that results from planning and activities set earlier in motion by the master production schedule, acts as a constraint within which the final assembly schedule must be accommodated. It is impossible, on short notice, to build more, or different, products than the quantities of available components allow.»
- **FAS en una enciclopedia** [Q18, S]: «a schedule of end items to finish the product for specific customer orders»; «Final assembly schedule (FAS) entries are needed when end products do not appear in the MPS.» Dos programas: el MPS para los componentes de los productos finales y el FAS para los productos que se despachan. No trae plan en dos niveles ni lista de planificación.
- **Plan en dos niveles en documentación de un sistema** [Q19, S]: «One solution to this problem is to master schedule and build key subassemblies only, based on anticipated demand, and to assemble specific configurations only after receiving customer orders.» «You can define multilevel planning and model bills to represent product families and products with options, and to maintain planning percents that represent estimates of anticipated product and option mixes.»
- Hasta ahora: ningún libro ni apunte leído da la definición del diccionario de «two-level master schedule» ni de «planning bill». Las citas de Q3 y Q19 cubren el mecanismo.
- Un resultado del buscador menciona el libro de John F. Proud, *Master Scheduling*, con capítulos sobre listas de planificación y programa de terminación; no se pudo abrir (certificado inválido en el servidor que lo aloja).

Lo que registra un sistema (de Q3 y Q19): una lista de planificación con porcentajes por opción, el MPS en el nivel de módulos y el FAS por pedido en el nivel final. Confirmación en un sistema abierto: no hecha en esta ronda.

---

## 4. Mensajes de acción y nerviosismo (hueco 4)

### Mensajes de acción

- **Un sistema comercial** [Q9, S]: «An action message suggests performing a certain planning action.» Categorías: A (liberar): «A messages can be regarded as natural messages for a planner.»; B (reprogramar): «B messages indicate that some sort of manual replanning or deletion has to be done for planned or released orders.»; C (demorada): «C messages are a planner's indication that an order is or might be delayed.» Códigos: A2, «a planned order must be released since the release date is before or equal to today's date»; A3, «a planned order must be firmed since the planning date is inside the planning time fence»; B1, «a released order should be replanned to an earlier date» (adelantar); B3, «re-planned to a later date due non-needed replenishment» (postergar); B7, «a replenishment order is not needed anymore» (anular). El sistema no tiene un mensaje llamado «cancelar»; su equivalente es B7, «Delete order».
- **Una guía de estudio** [S, vista solo por el buscador, no abierta]: «An existing open order's need date has moved earlier than its current due date. The planner should attempt to pull the order in to avoid a shortage.» / «moved later ... The planner may push the order out to avoid carrying unnecessary inventory.» No usar como cita.
- **Apuntes del MIT** [Q4, L]: salidas del MRP: «Planned order releases», «Change notices» y «Exception reports — discrepancies, consequences of unexpected events».
- **Apuntes de Brunel** [Q20, S]: la salida del MRP es una lista de acciones, «summary of all actions (planned order releases)». «The document says only the current period's actions need immediate attention» es una paráfrasis del lector.
- **Reglas de barrera sobre los mensajes** [P3]: dentro de la barrera de planificación el sistema no recomienda adelantar, pero puede recomendar postergar o cancelar.
- Orlicky (1975) es la fuente original de los mensajes de acción; el texto no es accesible (ver sección 5).

### Nerviosismo del sistema

- **Definición en los apuntes del MIT** [Q4, L]: «Nervousness — drastic changes in schedules due to small deviations from plans — (chaos?)» y «Nervousness results when a deterministic calculation is applied to a random system, and local perturbations lead to global changes.» Consecuencias: «Drastic changes in plans for the near future, which will confuse workers; Excessive setups, consuming excess expense or capacity.» Remedio: «Freeze the early part of the schedule (ie, the near future). Do not change the schedule even if there is a change in requirements; or do not accept changes in requirements.» con la advertencia «But: What price is paid for freezing?» Y: «nervousness amplifies inevitable variability.»
- **Paper académico** [Q15, M]: Blackburn, Kropp y Millen (1986), *Management Science* 32(4), 413-429, DOI 10.1287/mnsc.32.4.413. El abstract «examines the effectiveness of alternative strategies for dealing with the problem of order instability» en sistemas MRP. Evalúa por simulación cinco estrategias contra la nerviosidad que viene de la lotificación y del horizonte móvil: congelar el programa dentro del horizonte, lote por lote después de la primera etapa, stock de seguridad, pronóstico más allá del horizonte y un procedimiento de costo de cambio. Resultado: la de stock de seguridad y la de lote por lote no son efectivas en costo cuando la inestabilidad viene del horizonte móvil, y en la mayoría de las condiciones el costo de cambio o congelar el programa «appear to be dominant». El resumen vino por el lector, que no pudo dar el abstract entero con comillas; las frases entre comillas son literales.
- Un resultado del buscador cita otro artículo de los mismos autores, «MRP System Nervousness: Causes and Cures» (Engineering Costs and Production Economics, 1985); no se abrió.
- P1 [ronda 1]: órdenes planificadas firmes «stabilize the production schedule and serve to reduce system nervousness».

### Hueco que queda

Mensajes de acción en una fuente de fundamentos con el conjunto completo (liberar, adelantar, postergar, cancelar) y no solo en un sistema; Orlicky o Vollmann. El texto del abstract de Blackburn et al. entero, con comillas.

---

## 5. Orlicky: metadatos y fórmula del neteo (hueco 5)

### Metadatos verificados [Q21, M]

- 1975, 1.ª edición: Joseph Orlicky, *Material requirements planning: the new way of life in production and inventory management*, New York, McGraw-Hill, 1975. Internet Archive: id `materialrequirem00orli`, ISBN 0070477086 y 9780070477087, LCCN 74010904, «Includes bibliographies», 332 imágenes escaneadas (no es el número de páginas), `access-restricted-item: true` (solo préstamo). Un registro de catálogo agregado por el buscador da «xx, 292 p.» y clasificación LC TS155.8 .O74 (Univ. de Hertfordshire; no confirmado por mí porque la página está bloqueada). Discrepancia: Open Library tiene un registro de 1974 con el mismo ISBN 0070477086; el archivo de Internet Archive y los catálogos dicen 1975.
- 1994: *Orlicky's material requirements planning*, McGraw-Hill, ISBN 0070504598 / 9780070504592 (id de Internet Archive `orlickysmaterial00orli`; no se verificaron los coautores de esa edición).
- 3.ª edición, 2011: *Orlicky's Material Requirements Planning*, 3.ª ed., Carol A. Ptak y Chad Smith, McGraw-Hill, 2011. ISBN 0071755632 / 9780071755634 (impreso); libro electrónico 0071755640 / 9780071755641. LCCN 2011015842 y signatura TS155.8 .O74 2011 según un registro de biblioteca visto por el buscador. Open Library confirma año e ISBN; la editorial lista a veces «McGraw-Hill Education».
- 4.ª edición, 2023: Ptak y Smith, McGraw-Hill Education, ISBN 1264264577 / 9781264264575 [Open Library]. No estaba en el brief; es la más reciente.

### Cita literal del libro

Ninguna. El texto del libro de 1975 está en préstamo controlado (Internet Archive devuelve una página vacía de «Full text» en la vista de texto) y el intento por Google Books fue rechazado con 429. Se declara como hueco: no hay cita literal accesible.

### Fórmula del neteo, con texto abierto

- **Apuntes de Houston** [Q5, L], con stock de seguridad: «Net requirements in row 16 are: (gross requirements this week) + (safety stock) - (inventory on hand at the beginning of this week). Net requirements cannot be negative in MRP1. If this formula results in a negative value, the model resets net requirements to zero.» Saldo proyectado: «Projected inventory on hand at the beginning of each week is computed as follows: (inventory on hand last week) - (gross requirements last week) + (planned order receipts last week) + (scheduled receipts this week).» Existencia disponible inicial: «The beginning inventory is 50 units, with 20 units allocated to future production. Thus the initial inventory available is 50 - 20 = 30 units.» Redondeo al lote: «the net requirement of 215 units in week 3 rounds up to a planned order receipt of 300 units» (lote 100); plazo: «Planned order releases are offset by the length of the leadtime and adjusted by the yield percentage»: 300 / 0,98 da 306. Esa fuente suma el stock de seguridad al requerimiento y no las recepciones programadas en la misma fórmula; las recepciones entran al saldo.
- **Apuntes del MIT** [Q4, L], sin stock de seguridad: «It = It−1 − Dt, as long as It−1 − Dt ≥ 0; It = It−1 − Dt + St, if It−1 − Dt < 0» y, para las necesidades netas, N_t = 0 si t < t*, N_t = I_{t−1} − D_t < 0 si t = t*, N_t = D_t si t > t*, donde t* es el primer período con I_{t−1} − D_t < 0. Ejemplo: necesidades brutas de las semanas 1 a 8, 15 20 50 10 30 30 30 30; existencia 20; recibos programados ajustados 20 en la semana 2 y 100 en la 3; saldo proyectado 5 5 55 45 15 −15; necesidades netas 0 0 0 0 0 15 30 30. Otro ejemplo del mismo PDF, con lote de 75: recepciones planificadas 30, 0, 75, 0, 0, 75, 0, 75 y lanzamientos 75, 0, 0, 75, 0, 75, 0, 0 con plazo de una semana. Tarea: «Material requirements are determined by considering whether inventory would otherwise become negative.»
- La fórmula pedida, necesidad neta = bruta − disponible − recepciones programadas (+ stock de seguridad), queda cubierta por Q5 y Q4 combinadas: Q5 trae el seguridad y el stock disponible (en bruto menos asignado), Q4 la dinámica con recepciones. Q5 no la escribe en una sola línea.

---

## 6. Lotificación (hueco 6)

- **Reglas, literal** [Q4, L]: «Lot-for-lot: produce in a period the net requirements for that period. Maximum setups.» «Fixed order period: produce in a period the net requirements for P periods.» «Fixed order quantity: always produce the same quantity, whenever anything is produced. EOQ formula can be used to determine lot size.» Y una pregunta abierta: «Which satisfy the Wagner-Whitin property?»
- **EOQ y POQ, definición literal** [Q5, L]: «Production economics may dictate the use of lot-sizing in MRP systems but the EOQ rarely works very well. The problem is that the EOQ is based on the assumption that demand is continuous and uniform. In MRP systems, demand for component parts tends to be "lumpy," that is, discontinuous and nonuniform, with frequent periods of zero demand. When the EOQ is applied to lumpy demand, lot sizes usually don't cover whole periods of demand. The result is that unnecessary inventory is often carried during the periods following the receipt of a lot. This unnecessary inventory is called "remnants"...» «The period-order-quantity (POQ) model was designed to avoid remnants and give lower costs with lumpy demand.» Cálculo: «we order only in whole periods of demand. To determine the number of periods to order, the first step is to compute the EOQ quantity. Next, we determine the average number of periods of demand covered by the EOQ.» 194 / 103,1 = 1,9 semanas, que redondea a un período económico de 2 semanas.
- **Ejemplo comparativo de costos** [Q5, L]: costo de mantener 0,15 por unidad y semana, costo de preparación 27,50, existencia inicial 25, horizonte 8 semanas. Demanda 100, 0, 175, 50, 0, 125, 75, 300 (total 825; promedio 103,1; EOQ 194).
  - EOQ: recepciones en las semanas 1, 3, 6 y 8 de 194, 194, 194 y 218; saldos al final de semana 119, 119, 138, 88, 88, 157, 82, 0 (suma 791).
  - POQ (2 semanas): recepciones en las semanas 1, 3, 6 y 8 de 75, 225, 200 y 300; saldos finales 0, 0, 50, 0, 0, 75, 0, 0 (suma 125).
  - La hoja informa costo total EOQ 228,65 y costo total POQ 18,75. Verificación mía: EOQ = 4 pedidos × 27,50 + 0,15 × 791 = 110 + 118,65 = 228,65. POQ: 0,15 × 125 = 18,75 es solo el costo de mantener; con los mismos 4 pedidos se agregan 110 de preparación y el total es 128,75. La cifra de 18,75 que da la fuente no incluye la preparación y no es comparable con la de EOQ: la nota no debe copiarla como «costo total». Con la corrección, POQ (128,75) sigue siendo menor que EOQ (228,65). Es una discrepancia entre el texto de la fuente y sus propias cuentas.
- **Cantidad mínima de lote** [Q5, L]: «Some companies treat the lot size as a minimum and do not round up to the nearest even multiple.»
- **Wagner–Whitin (1958)** [Q16, M]: «A forward algorithm for a solution to the following dynamic version of the economic lot size model is given:» «allowing the possibility of demands for a single item, inventory holding charges, and setup costs to vary over N periods, we desire a minimum total cost inventory management scheme which satisfies known demand in every period.» «Disjoint planning horizons are shown to be possible which eliminate the necessity of having data for the full N periods.» Autores Harvey M. Wagner y Thomson M. Whitin, *Management Science* 5(1), 89-96, DOI 10.1287/mnsc.5.1.89; reeditado en 50(12 suplemento), 1770-1774 (2004).
- **Silver–Meal (1973)** [Q17, S]: el método «is a forward method that requires determining the average cost per period as a function of the number of periods the current order is to span»; regla de parada «The search for the optimal T continues until C(T) > C(T − 1)». Metadatos del paper: Silver, E. A. y Meal, H. C. (1973), *Production and Inventory Management* 14, desde p. 210 (según Crossref; el título varía entre «lot size quantities» y «lot size requirements»). El texto del paper no se leyó; no hay ejemplo numérico.
- **Contexto** [Q6, L]: «In the 1950s, time-varying deterministic demand models emerged, considering finite time horizons and applying dynamic programming, the most well-known one being Wagner and Whitin (1958). A considerable literature was then developed to propose near-optimal solutions for this problem, often referred to as the lot sizing problem (Silver and Meal, 1973, particularly).» y «The early EOQ model, assuming constant demand, was refined by Wilson (1934)». Q6 cita una reseña de Glock et al. (2014) sobre el tema.
- **Cuál elegir**: P13 (ronda 1) y la serie de Gershwin (H1, Q4). La advertencia de Blackburn et al. (Q15): lote por lote y stock de seguridad no sirven para reducir la inestabilidad que viene del horizonte móvil.
- Lote por lote y período fijo en una lista (Beasley): «Other rules are fixed order quantity (FOQ) and fixed period requirements (FPR)» [Q20, S]. Q20 trae un ejemplo de silla con lote por lote y un período fijo de 3 semanas que da un pedido de 225 sillas en la semana 3 y 60 en la 6 [S].

### Hueco que queda

Un ejemplo comparativo de Wagner-Whitin y Silver-Meal con números en apuntes abiertos: no hay. El texto original de Silver y Meal no se leyó.

---

## 7. Estrategias de respuesta y punto de desacople (hueco 7)

- **Definición literal de Sharman (1984)**, citada en Q6 [L, con página]: «the point at which product becomes earmarked for a particular customer. Downstream of this order penetration (OP) point, customer orders drive the systems that control materials flow; upstream, forecast and plans do the driving» (Sharman, 1984, p. 75). Referencia: Sharman, G. (1984), «The rediscovery of logistics», *Harvard Business Review* 62(5), 71-79. La cita viene de segunda mano (la reseña abierta, no el artículo).
- **Cinco posiciones** [Q6, L]: «Based on a balance between market characteristics (e.g., specificity of demand, delivery speed) and manufacturing characteristics (e.g., costs of goods, processing time) five distinct position of the CODP have been distinguished in the literature: make to stock (MTS), assemble to order (ATO), make to order (MTO), purchase and make to order (PMTO), and engineer to order (ETO).» «While the first one directly delivers a product form inventory upon arrival of an order, the last one starts engineering and purchasing once an order arrives. Hence there is a huge difference in delivery leadtime, but also in product specificity and the number of activities performed after ordering.» La reseña remite a Olhager y Van Donk (2024) como panorama.
- **Cuatro posiciones y qué hace el punto** [Q7, L], tesis abierta de Lund: «The four most common CODP positions, make-to-stock (MTS), assemble-to-order (ATO), make-to-order (MTO) and engineer-to-order (ETO)». «In short, the CODP is the point that separates the material flow and its associated operations into two parts: an upstream part which is driven by forecasts and a downstream part which is driven by actual customer orders.» Sharman, según la tesis, lo ve como variable clave porque «it is normally the point where product specifications get frozen, it is typically the last inventory point, and it separates forecast-driven activities in the value chain from order-driven activities.» (paráfrasis de la tesis, no cita de Sharman). Hoekstra y Romme (1992): el lugar del CODP importa para «the determination of organizational structure and the types of unavoidable risks» (paráfrasis de la tesis). Referencia: Hoekstra, S. y Romme, J. (1992), *Integrated Logistics Structures: Developing Customer Oriented Goods Flows*, McGraw-Hill, Cambridge, UK.
- **Efectos de la posición** [Q7, L, tabla 1.1]: aguas arriba, «Standardized products, produced according to forecast»; aguas abajo, «Customized products, produced based on actual customer orders»; «Demand is predictable and demand volumes are high» arriba frente a «Market demand is spiky and unpredictable, volumes vary but are typically lower (per product variant)» abajo; capacidades: «Cost-efficiency, lean, high throughput rate, and a level schedule» arriba, «Flexibility, agility, capacity to deal with demand spikes» abajo.
- **Olhager 2010**, *Computers in Industry* 61(9), 863-868: metadatos confirmados (volumen, número y páginas por el buscador). Del abstract solo se vio la primera frase, en el registro de una biblioteca: «The customer order decoupling point (CODP) is getting increasing attention as an important input to the design of manufacturing operations as well as supply chains.» [M, vía buscador; no se abrió el registro]. No hay copia abierta encontrada (Scribd tiene un documento llamado «Decoupling Point» que no se pudo confirmar como el mismo texto).
- **Comprar y fabricar contra pedido** (PMTO): solo el nombre en la lista de Q6 y Olhager y Van Donk (P5); ninguna definición literal.
- Sobre la ronda 1: la relación P:D y las cuatro definiciones de P7 siguen siendo [S] de Wikipedia.

### Hueco que queda

Definición de cada estrategia (cuatro o cinco) en una fuente primaria abierta (Olhager 2010 o Hoekstra y Romme): no hay. Lo mejor es Q6 y Q7 como textos abiertos con la cita de Sharman, y declarar que las definiciones de cada posición salen de Wikipedia [S, P7].

---

## 8. Carga finita frente a infinita (hueco 8)

- **Definición de una documentación de sistema** [Q11, L]: «Finite capacity is an approach that helps you understand how much work can be produced during a specific period when limitations on different resources are taken into consideration. The purpose of finite capacity scheduling is to ensure that work proceeds at an even and efficient pace throughout the plant.» «Finite capacity planning and scheduling creates a more realistic schedule for the production processes than the infinite loading approach creates. If there isn't enough capacity on the resources, the delivery date is pushed out, and the job is scheduled when there's enough capacity.» Mecánica: «Planned production orders are backward-scheduled from the requirement date. If capacity isn't available to meet the optimal schedule, the system tries to require component items on an earlier date.» «If your capacity can change as requirements change (for example, when you're working with shifts), you shouldn't use finite capacity functionality, because the calculated processing times won't be correct.» Ejemplo con números: una orden de 24 piezas, 8 horas diarias, dos operaciones; con capacidad infinita un pedido nuevo de 8 piezas carga la línea de soldadura de «Today at 8:00» a «Today at 12:00»; con capacidad finita y una barrera de un día, «Today + 1 at 8:00»; con barrera de dos días, «Today + 1 at 12:00» a «Today + 1 at 16:00» y el armado en «Today + 2 at 8:00». El sistema aclara: «a single-day time fence is probably too low for most manufacturers that use finite capacity planning.» Es documentación de un sistema comercial: evidencia de cómo se implementa, no de la definición.
- **Capacidad infinita en el MRP, textos abiertos**:
  - [Q6, L]: «While MRP-I assumes infinite capacities, MRP-II incorporates capacity constraints and integrates functions such as aggregate planning, capacity checks, and short-term scheduling (Harhen, 1988). MRP-II requires a step-by-step process to plan materials and capacities, and it is sometimes difficult to generate plans that consider volatility.»
  - [Q2, L], ASCM: «The first iteration of manufacturing planning and control systems involved open-loop MRP controlling the timing and release of materials into a production process. These early systems made a simplifying assumption that there was infinite capacity (thus the open loop).» «The next iteration was to add capacity checks at the master scheduling and MRP stages to ensure feasibility, and this feedback loop defined the major advancement of these systems, called closed-loop MRP.»
  - [Q4, L], MIT: «MRP is a solution to a problem whose formulation is based on an unrealistic model, one which is deterministic, infinite capacity»; «Capacity is actually finite.»
  - [Q20, S], Beasley: «MRP typically takes no account of capacity considerations».
- **Programación finita en el diccionario** [Q1, L], dentro de la definición de capable-to-promise del *APICS Dictionary* (15.ª ed.): «Employs a finite-scheduling model of the manufacturing system to determine when an item can be delivered. Includes any constraints that might restrict the production, such as availability of resources, lead times for raw materials or purchased parts, and requirements for lower-level components or subassemblies. The resulting delivery date takes into consideration production capacity, the current manufacturing environment, and future order commitments.»
- Para el CRP, las citas de la ronda 1 (P1) siguen siendo la definición de «infinite forward loading».

### Hueco que queda

La definición del diccionario de «finite loading» y «infinite loading» como términos: no se leyó. El caso de «carga infinita» como técnica de lectura de capacidad (qué hace el planificador con el exceso) está en P1.

---

## Recursos canónicos (actualizados)

- Barreras y quién autoriza: ASCM [Q1] para «slushy» y la aprobación del master scheduler; COPICS 1972 [Q3] para el origen del congelado y la parte firme; P3 y Q10 para cómo lo implementa un sistema. En qué fijarse: el criterio de costo de cambiar lo comprometido.
- ATP y consumo: ASCM [Q1] (fórmulas, regla de corrección y ejemplo con 70, 48, 100, 66, 57, 62), COPICS [Q3] para asignar el pedido al plan, un sistema comercial [Q8] para el consumo en software. En qué fijarse: el ATP no es un saldo acumulado en el método discreto; la corrección con el ATP previo.
- Plan en dos niveles y FAS: COPICS [Q3] (porcentajes de opciones y programa de ensamble final como restricción).
- Netea y lotes: Q4 para la dinámica, Q5 para la fórmula con seguridad y el ejemplo de POQ (con la corrección de costos de arriba).
- Nerviosismo: Q4 para la definición, Q15 para la evidencia académica.
- CODP: Q6 y Q7 para la cita de Sharman y las cinco posiciones; Olhager 2010 y Olhager y Van Donk 2024 solo como metadatos.
- Orlicky: citar solo con la edición y la ficha, no con texto.

## Qué registra un sistema (agregados de esta ronda)

- Barreras: cantidad de días por ítem desde la fecha de generación (P3, Q10); orden firme [P3]; mensaje A3 «transformar a orden planificada firme» cuando la fecha cae dentro de la barrera [Q9].
- Mensajes: por orden, un código y una categoría (liberar, reprogramar a una fecha anterior o posterior, borrar, demorada) [Q9].
- MPS: ATP por período con MPS programado, pedidos del cliente por período, saldo proyectado [Q1].
- Consumo: período de consumo del pronóstico, consumo por cliente, orden de procesamiento primero entrado primero salido [Q8].
- Capacidad finita: marca por plan y por recurso, y una barrera de capacidad finita en días [Q11].
- Evidencia de sistema abierto: no se encontró en esta ronda; todo lo anterior viene de documentación de sistemas comerciales.

## Huecos que quedan

1. Definiciones literales de «demand time fence» y «planning time fence» del *APICS Dictionary* o de un libro de texto; zona «liquid» en una fuente primaria.
2. El apunte de la EMU con tablas de MPS, ATP y pedidos (401) y las diapositivas de MIT 2010 (404): no leídas.
3. Fórmula del ATP acumulado en una fuente fiable: solo Q14 [S], sin autor.
4. Plan en dos niveles y lista de planificación con definición literal de diccionario: solo Q3 (1972) y Q19.
5. Orlicky: ninguna cita literal; Google Books y Hertfordshire inaccesibles.
6. Wagner-Whitin y Silver-Meal: solo abstract y descripción secundaria; sin ejemplo numérico.
7. Olhager (2010): solo la primera frase del abstract, vía un registro de biblioteca visto por el buscador; sin copia abierta. Hoekstra y Romme (1992): sin acceso; solo la paráfrasis de Q7. Definición propia de comprar y fabricar contra pedido: sin fuente.
8. Mensajes de acción en una fuente de fundamentos: solo documentación de un sistema [Q9] y los apuntes del MIT sin lista de mensajes.
9. Evidencia de un sistema abierto para barreras, consumo, mensajes y capacidad finita: no hecha en esta ronda (todo es de sistemas comerciales).
10. Este ángulo no toca ley ni dinero; no corresponde la regla de dos fuentes independientes.
