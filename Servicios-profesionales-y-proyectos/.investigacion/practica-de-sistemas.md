# Práctica de sistemas: reserva, hoja de horas, facturación y presupuesto

Fecha: 2026-11-27. Complementa `asignacion-y-horas.md`, `proyecto-y-facturacion.md` y `metricas-fundamentos-y-contraria.md` (no repite lo que dicen).

Método. WebSearch no estaba disponible; todo se abrió por URL directa con WebFetch, partiendo del índice (`toc.json`) de Microsoft Learn y del índice de servicios de Odoo 19. Las páginas de Microsoft Learn llegaron casi enteras como texto de la página: [L]. Las de Odoo, ERPNext y FAR llegaron como resumen de un modelo chico sobre la página: [S] (las citas literales de esas son cortas y hay que releerlas antes de citarlas en una nota). Todo esto es documentación de producto: vale como «un sistema hace X», no como norma ni como recomendación. Los productos no se nombran en el árbol del tema; acá sí, porque es evidencia.

Marcas: [L] texto leído, [M] metadatos, [S] resumen secundario. Puntajes 1 a 3: Autoridad / Profundidad / Ejemplos / Unicidad.

## Tabla de fuentes

Raíz MS = https://learn.microsoft.com/en-us/dynamics365/project-operations/

| Id | Fuente (URL) | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| M1 | MS `resource-management/resource-management-key-concepts` | doc de producto | [L] | 2/1/1/2 |
| M2 | MS `resource-management/booking-status` | doc de producto | [L] | 2/3/2/3 |
| M3 | MS `resource-management/resource-management-mode-overview` | doc de producto | [L] | 2/2/1/3 |
| M4 | MS `resource-management/submit-resource-request-po` y `generic-resource-requirement-fulfillment` | doc de producto | [L] | 2/2/2/3 |
| M5 | MS `resource-management/booking-vs-assignment` | doc de producto | [L] | 2/2/1/3 |
| M6 | MS `resource-management/define-roles` y `define-skills-proficiencies` | doc de producto | [L] | 2/1/1/2 |
| M7 | MS `pricing-costing/price-list-setup` (solo la cabecera; no abrí la parte de «Role price») | doc de producto | [L] parcial | 2/2/2/3 |
| M8 | MS `pro/pricing-costing/sales-price-resolution-sales` | doc de producto | [L] | 2/3/2/3 |
| M9 | MS `pricing-costing/set-up-cost-sales-rates-expenses` | doc de producto | [L] | 2/3/3/3 |
| M10 | MS `time/time-entry-overview`, `time/ui-behavior-time`, `time/time-entry-configurations` | doc de producto | [L] | 2/2/2/2 |
| M11 | MS `approvals/approvals-overview`, `approvals/recall-cancel`, `approvals/cancelapproval` | doc de producto | [L] | 2/3/3/3 |
| M12 | MS `pro/sales/manage-contract-values-project-based-sales` | doc de producto | [L] | 2/3/3/3 |
| M13 | MS `pro/proforma-invoicing/manage-nte-status-validations-sales` | doc de producto | [L] | 2/3/2/3 |
| M14 | MS `pro/sales/invoice-schedules-contract-line-sales` | doc de producto | [L] | 2/3/3/3 |
| M15 | MS `pro/sales/set-up-advances-retainer-based-contracts-sales` y `pro/proforma-invoicing/invoice-retainer-advance-sales` | doc de producto | [L] | 2/3/3/3 |
| M16 | MS `proforma-invoicing/manage-billing-backlog` | doc de producto | [L] | 2/3/2/3 |
| M17 | MS `proforma-invoicing/manage-proforma-invoice` y `update-ild-on-an-invoice` | doc de producto | [L] | 2/3/3/3 |
| M18 | MS `proforma-invoicing/revise-project-invoices` | doc de producto | [L] | 2/3/3/3 |
| M19 | MS `pro/budget/keyconcepts-projectbudget` y `pro/budget/revise-project-cost-budget` | doc de producto | [L] | 2/2/2/3 |
| M20 | MS `project-management/estimating-projects-overview` y `sales/sales-overview` | doc de producto | [L] | 2/2/2/2 |
| O1 | Odoo 19 `applications/services/timesheets.html` y `timesheets/billing_rates.html` | doc de producto | [S] | 2/1/1/1 |
| O2 | Odoo 19 `applications/services/planning.html` | doc de producto | [S] | 2/2/1/2 |
| O3 | Odoo 19 `applications/sales/sales/invoicing/milestone.html`, `down_payment.html`, `invoicing_policy.html`, `time_materials.html` | doc de producto | [S] | 2/2/2/1 |
| O4 | Odoo 19 `applications/services/project/project_management/project_profitability.html` | doc de producto | [S] | 2/1/1/1 |
| E1 | ERPNext/Frappe `timesheet`, `activity-type`, `project-costing`, `project` en https://docs.frappe.io/erpnext/user/manual/en/ | doc de producto | [S] | 2/1/1/1 |
| F1 | FAR 52.232-7, https://www.acquisition.gov/far/52.232-7 | primaria (cláusula contractual de EE.UU.) | [S] | 3/2/2/3 |

## 1. Reserva tentativa y firme, pedido de recurso, quién aprueba

Hallazgos (todo de un sistema, Project Operations; no hay segunda fuente independiente: Odoo Planning tiene un esquema distinto, abajo).

- Cuatro estados de reserva: «Project Operations provides four booking statuses: Hard, Soft, Proposed, and Canceled» (M2, [L]).
  - Firme: «a resource manager or project manager wants to firmly allocate and reserve a resource»; el recurso entra al equipo y «the resource's capacity is consumed».
  - Tentativa: sirve para reservar a alguien para un proyecto «but you want that resource to remain allocable to other projects until you make a final decision»; el recurso entra al equipo pero «the resource's capacity isn't consumed». Es decir, una reserva tentativa no bloquea capacidad: dos proyectos pueden tener tentativa sobre la misma persona.
  - Propuesta: es el estado que usa el gerente de recursos para ofrecer a alguien ante un pedido; no consume capacidad ni agrega a la persona al equipo hasta que se decide.
  - Cancelada: libera la capacidad pero «you don't remove those resources from the project's Team member grid» (la persona sigue en el equipo).
- Transiciones y su efecto (M2, tabla): propuesta a firme consume capacidad; propuesta a cancelada no tiene efecto; tentativa a firme consume capacidad (caso típico: «A project that was waiting to be started is confirmed»); firme a cancelada libera (caso: «A task was suspended»).
- Quién reserva depende del modo (M3, [L]):
  - Modo central: «A resource manager handles the fulfillment of the resource requirements. Project managers can accept or reject resources that the resource manager proposes.» El jefe de proyecto define el requerimiento; el gerente de recursos propone; el jefe de proyecto acepta o rechaza.
  - Modo híbrido: «enables both project managers and resource managers to book resources»; el jefe de proyecto puede reservar directo.
  - El modo es un parámetro del proyecto y se puede cambiar.
- Pedido de recurso (M4, [L]): el recurso genérico con requerimiento se envía con «Submit Request»; el estado pasa a «Submitted»; si el gerente de recursos propone una persona con nombre el estado pasa a «Needs Review»; si la reserva, «the generic resource is replaced by the named resource». Si no se cumple, el genérico queda en el equipo.
- Todo se reserva contra un requerimiento: «you must always make bookings against a resource requirement»; si no hay pedido específico, se reserva contra el «primary requirement», creado con el proyecto (M2, [L]).
- Un requerimiento genérico puede cubrirse con varias personas con nombre (ejemplo del documento: 120 horas de ingeniería en cinco días, que no puede hacer una sola persona); el genérico queda en la tarea y es el jefe de proyecto quien asigna el trabajo (M4).
- Reserva versus asignación (M5, [L]): la reserva es un concepto de proyecto («hard or soft allocation of resources to a project»); la asignación es el compromiso con tareas del cronograma. «Typically, the sum of the bookings for a resource equals the sum of the resource's assignments [...] However, Project Operations doesn't enforce this agreement.» Una vista de conciliación muestra los desacuerdos al jefe de proyecto.
- Sobreasignación: la fuente solo dice que la reserva firme consume capacidad y la tentativa no (M2). Lo que sigue es un hueco: ninguna de las páginas abiertas describe un bloqueo por sobreasignación ni cómo se resuelve un conflicto entre proyectos.
- El mismo documento junta lo que el cronograma llama «ausencia»: los pendientes de vacaciones o ausencias aparecen en el tablero como «Out» para que el gerente de recursos planifique (M10, [L]).

Odoo Planning (O2, [S]): un turno sin persona es un «open shift»; los turnos son borrador hasta «Publish & Save» (los borradores se ven con rayas diagonales; publicar manda el horario por correo a la persona); los roles filtran quién ve qué turno abierto y habilitan el auto-planificado. No es un esquema de reserva firme/tentativa sobre proyectos: es borrador/publicado sobre turnos. La parte de sobreasignación no apareció en el texto leído.

Lectura para la base: el patrón común es (a) pedido del proyecto, (b) propuesta de quien administra a las personas, (c) aceptación, y dos intensidades de reserva, una que consume capacidad y otra que no. La nota agnóstica puede decir eso sin nombrar productos; la planilla equivalente es una columna «firme / tentativa» y una suma de horas firmes por persona y semana.

## 2. Rol genérico, persona con nombre, habilidades, precio y costo por rol

- Equipo con recursos genéricos o con nombre: «Staff your project with a team of generic or named resources» (M1, [L]). Un recurso genérico se define por rol y unidad organizativa; sirve para estimar y pedir antes de saber quién (M1, M20).
- Rol (M6, [L]): «roles or categories that you use to group the resources» (ejemplos: Consultant, Developer, Project manager, «Consulting Lead 1», «Senior Project manager»), para «define their pricing based on their roles». Un rol puede llevar utilización objetivo y tipo de facturación que pasan por defecto a cada persona que lo juega, y habilidades asignadas.
- Habilidades con nivel (M6, [L]): un modelo de competencia («proficiency model») tiene un valor mínimo y uno máximo y los valores intermedios con nombre; el sistema muestra esos valores en los filtros de requerimientos y del tablero de planificación. Es decir, la habilidad tiene escala configurable y se usa para emparejar el pedido con la persona.
- Una persona con varios roles en un proyecto tiene su propia página (`sales/br-playing-multiple-roles`, aparece en el índice; no la abrí).
- Listas de precios (M7, [L] parcial): una lista es «a catalog of rates» y tiene contexto Costo, Venta o Compra. «Cost price lists and Purchase price lists resolve the price for the cost type on estimate and actuals records. Sales price lists resolve the price on estimated and actual records of unbilled and billed sales types.» Solo las de venta pueden pegarse a la lista de precios de un cliente, una cotización o un contrato. Tienen vigencia (inicio y fin) y moneda; en las de venta la moneda de las líneas es la de la cabecera, en las de costo la línea puede tener otra moneda. Hay listas generales o específicas de una cotización o contrato.
- Cómo se resuelve la tarifa de venta de una hora (M8, [L]): primero la lista, por fecha de la transacción y moneda; después se busca la línea por rol + unidad que presta el recurso («Resourcing Unit»); si no hay, «retrieves role price lines that have matching values for the Role field but null values for the Resource Unit field». Si se configuran otras dimensiones, se prueban en orden de prioridad y las filas con nulo van últimas. Es decir: tarifa por rol, con excepción por unidad, no por persona.
- Estimaciones y costo (M20, [L]): para vender una hora el sistema crea dos líneas, una de venta y otra de costo, con los mismos campos no monetarios; rol y unidad organizativa son las dimensiones de precio de ambas.
- Odoo y ERPNext, el esquema por persona (E1, [S]; O1, [S]): en ERPNext el tipo de actividad tiene costo y tarifa de venta por defecto, y el «Activity Cost» por empleado los pisa («Rates can be set for individual employees through Activity Cost, which overrides the Activity Type defaults»). Odoo 19: la página de tarifas de facturación solo trata de objetivos de horas facturables por empleado (un indicador contra una meta mensual), no de tarifas; el costo horario del empleado sale de la ficha de RR. HH. (O4, [S], «based on each employee's HR settings»).

Discrepancia entre sistemas: Project Operations precia por rol (con excepción por unidad); ERPNext precia por tipo de actividad, con excepción por persona. Dos ejes distintos de precio. No hay una fuente que diga cuál es más usual en firmas reales.

## 3. Hoja de horas

- Estados (M10, [L]): «Draft» (nacen así; solo en borrador se pueden borrar), «Submitted», «Approved», «Returned» (el aprobador rechazó; vuelve a corregir y reenviar, con comentario de rechazo visible).
- Enviada = bloqueada: «After you submit time entries, you can't edit them.» La persona puede retirar («recall») lo enviado y editarlo (M10).
- Quién aprueba: cada proyecto tiene miembros del equipo marcados como aprobadores del proyecto («Project Approver» = Sí); además el gerente de la persona se configura en su ficha (M11, [L]). La aprobación crea los «actuals» (costo y venta sin facturar): «If the entry is related to a project, the actuals are created when you approve it.»
- Unidad de registro (M10): contra proyecto, tarea o resumen; en una grilla semanal con dimensiones proyecto, tarea, rol, tipo y estado. Duración máxima por día configurable de 0 a 1440 minutos (por defecto 24 horas), y un intervalo mínimo configurable de 1 a 60 minutos: una duración que no es múltiplo se redondea al múltiplo mayor (por ejemplo a 15 minutos).
- Facturable o no: no es un campo del que escribe la hora; el aprobador puede cambiar «Billable quantity» y «Billing type» al volver a aprobar (M11, cancelapproval). En la factura borrador, el tipo de facturación es Cobrable, No cobrable o De cortesía («Complimentary»); solo lo cobrable suma al total de la línea (M17, [L]). En el tope de importe, las horas no cobrables quedan «Not Applicable» (M13).
- Corrección de horas ya aprobadas (M11, [L]), tres caminos:
  1. Retiro de aprobación por el aprobador («Cancel Approval»): la entrada vuelve a «Submitted»; el aprobador puede cambiar cantidad facturable y tipo y aprobar de nuevo.
  2. Pedido de retiro por quien cargó la hora («Recall»), con motivo obligatorio y aprobación del aprobador; si se aprueba, el aprobación queda «Rejected» y la hora «Returned» (tiempo) o «Rejected» (gasto/material), y la persona puede editarla, reenviarla o borrarla.
  3. Si ya se facturó: «You can't create a recall request for an approved time, expense, or material usage entry that the system already invoiced to the customer». Solo se puede si una factura correctiva da crédito total o devolución de la factura original; lo mismo si la hora está en una factura borrador.
- Efecto financiero de retirar una aprobación: el costo y la venta sin facturar originales pasan a «Adjusted» con estado de facturación «Canceled», y el sistema crea asientos de reversa copiando todo salvo la cantidad, que se invierte; «the recorded spending and the revenue backlog on the project no longer account for the amounts» (M11). Esto sirve de patrón: una hora aprobada no se edita, se revierte y se vuelve a registrar.
- ERPNext (E1, [S]): al enviar la hoja, «Billing Rate and Costing rate get locked, and cannot be changed»; hay casilla «Bill» por fila; se factura desde la hoja enviada, y las horas facturadas se completan cuando se envía la factura; la casilla «Completed» es por fila (tarea terminada), no un estado de la hoja. Cancelación no documentada en lo leído.
- Odoo 19 (O1, [S]): la grilla va por semana (día o mes también); totales por día coloreados contra la jornada del empleado y por período contra lo esperado (verde si coincide, naranja si excede, rojo si falta). No hay casilla «facturable» aparte: la facturabilidad viene del proyecto y la hora facturable necesita un ítem del pedido de venta. La validación de hojas existe como permiso («validate all employees' timesheets») pero la página no describe el flujo; bloqueo de períodos: no cubierto.

Hueco: un período de cierre (fecha límite para cargar horas, cierre mensual que bloquea) no aparece en ninguna de las páginas leídas de Project Operations ni de Odoo; la única restricción temporal es la duración diaria.

## 4. Facturación

### 4.1 Métodos por línea de contrato

- El contrato tiene líneas; cada una guarda el acuerdo de estimación y facturación de un componente de trabajo, con «Billing method»: «Fixed Price» o «Time and Material» (M12, [L]). Cada línea apunta a un proyecto, a todas las tareas o solo a algunas, y a qué clases de transacción incluye (tiempo, gasto, material, honorario). Reglas de no superposición: un proyecto y una clase de transacción pueden estar incluidos en una sola línea del contrato, salvo que cada línea tome tareas distintas.
- Efecto del método sobre lo que se registra al aprobar una hora: tiempo y materiales crea costo y venta sin facturar; precio fijo crea solo costo (M12). Es decir, en precio fijo no hay venta devengada por la hora: el ingreso viene por hito o avance.
- En precio fijo el «Contracted Amount» es el valor pactado; en tiempo y materiales es «an estimated value» (M12).
- Odoo (O3, [S]): la facturación de servicios por hora exige un producto de tipo servicio con política «Based on Timesheets» y «Create on Order = Project & Task»; las políticas generales del módulo de ventas son «ordered» y «delivered» (cantidades).

### 4.2 Tope («not-to-exceed»)

- Solo en líneas de tiempo y materiales (M12). Se evalúa en cuatro niveles: límite de la línea para el cliente, de la línea, del cliente y del contrato (M13, [L]).
- Se evalúa dos veces: al enviar la entrada (estado «Success» o «Failed») y al aprobar, sobre la venta sin facturar («Committed» o «Failed»), restando lo ya comprometido y lo ya facturado.
- Las horas no cobrables o de cortesía, o sin tope definido, quedan «Not Applicable».
- Una venta sin facturar que falló el tope no se puede marcar «Ready to Invoice» (M16, [L]). El jefe de proyecto puede «Reset Not-to-Exceed Status» sobre otras horas ya comprometidas para dar prioridad a un trabajo y reevaluar, y reevaluar en masa cuando renegocia el tope (M13). Es la práctica de «priorizar qué se factura dentro del tope».
- La fuente de la norma (F1, [S]): en la cláusula de pago por tiempo y materiales del gobierno de EE.UU., la tarifa horaria «shall include wages, indirect costs, general and administrative expense, and profit»; los materiales se reembolsan a costo permitido y no pagan ganancia sobre los materiales; el contratista debe avisar con una estimación revisada cuando los costos se acercan al tope, «specifically at 85 percent of the ceiling»; «The Government will not be obligated to pay the Contractor any amount in excess of the ceiling price»; el contratista no tiene que seguir trabajando pasado el tope sin aumento escrito; los comprobantes se presentan como máximo cada dos semanas y se respaldan con «Individual daily job timekeeping records». Es un caso de práctica pública de EE.UU.: una sola fuente, marca [S]. Dinero y ley: requiere segunda fuente antes de afirmarlo en una nota.

### 4.3 Calendario de facturación e hitos

- En tiempo y materiales, la programación es por fecha: frecuencia de facturación, fecha de corrida, y «Transaction Cut-off Date» = el día anterior a la fecha de corrida; la corrida queda «Run Successful» o «Run Failed» (M14, [L]).
- En precio fijo hay dos tipos de programación: «Completed Milestones» (se factura el hito solo si está completo; es el valor por defecto) y «Progress-based» (se factura un porcentaje de avance del hito) (M12, [L]). Los hitos periódicos se generan dividiendo el monto por la cantidad de períodos; «Billing milestones should equal the contracted value of the project-based contract line» o hay error (M14). También hay hitos manuales (nombre, fecha, monto, impuesto, estado «Not ready for invoicing»).
- Un hito pasa a «Ready to invoice» (a mano, o por la corrida automática en la fecha) y, cuando está en borrador de factura, «Customer Invoice Created»; confirmada, «Customer Invoice Posted» (M16).
- Odoo (O3, [S]): el hito se marca «Reached» en el pedido; «Reaching a milestone does not automatically create an invoice»: se crea la factura aparte, con la columna «Delivered» como porcentaje del pedido que ya es facturable.
- Si el hito facturado se corrige, la corrección es siempre crédito total; el crédito parcial de un hito no está soportado, y el hito vuelve de «Customer Invoice Posted» a «Ready to Invoice» (M18, [L]).

### 4.4 Anticipos y retainer

- Retainer: «a negotiated set of equally distributed payments that the customer pays throughout the duration of a project», típico para tiempo y materiales cuando se quiere una factura y un cobro predecibles (M15, [L]). Mecanismo: cada período se factura el monto del retainer y, al cierre del período, se concilia lo devengado (horas a tarifa) contra lo cobrado: si lo devengado excede, se factura solo el exceso o se posterga la conciliación a una factura final. Anticipo (advance): un pago único que se concilia contra los costos del proyecto.
- Un retainer o anticipo no está disponible hasta que se factura: el monto disponible es cero hasta entonces; al confirmar esa factura, queda disponible (M15). El monto usado y el disponible se llevan por registro; una factura posterior lo aplica solo (grilla «Applied Retainers and Advances», con monto, usado, extendido y saldo); el cliente ve su factura reducida (M15).
- Retainer no consumido: una función permite devolver el saldo desde una factura o desde el contrato al cerrar el proyecto, sin facturas correctivas (M15, [L]; es un flag de función).
- Diferencia con precio fijo según la fuente: en precio fijo «the invoice amount isn't linked or tied to costs incurred»; en retainer lo facturable depende del costo del período y la conciliación lo sigue (M15).
- Odoo (O3, [S]): anticipo como porcentaje o monto fijo sobre el pedido confirmado; aparece como línea en la factura y queda en una sección de anticipos del pedido; un anticipo del 100 % igual exige otra factura para completar el pedido. Cómo se descuenta de la factura final: no lo pude leer.
- Ruptura/«breakage»: no documentada en estas fuentes (hueco anterior sigue abierto).

### 4.5 Ventas no facturadas (unbilled) y backlog

- Al aprobar una hora de una línea de tiempo y materiales, el sistema genera dos «actuals»: costo y «venta sin facturar» (M12). Hay un tablero «Time and Material Billing Backlog» con todas las ventas sin facturar de todos los contratos, y los hitos de precio fijo van en otra vista; desde ahí se marca cada una «Ready to Invoice» o no (M16). Las de estado «Adjusted» o «Unadjustable» no son facturables y se excluyen del tablero.
- Dato útil para el modelo conceptual: la venta sin facturar es la «cuenta de trabajo en curso a precio de venta» de los estudios; el sistema la guarda por transacción, no como saldo.
- Odoo (O4, [S]): el tablero de rentabilidad separa ingresos en Vendido, Entregado y Facturado, y costos en Esperado, Por facturar/pagar, Facturado/Pagado.

### 4.6 Ajustes antes de facturar, castigos

- En el borrador de factura (M17, [L]), cada línea del contrato tiene su línea de factura aunque no haya actuals, y cada línea tiene detalles que vienen de las ventas sin facturar y los hitos. En una línea de tiempo y materiales, en borrador se pueden editar: tipo de facturación, cantidad, precio, impuesto, descripción y descripción externa (la que va impresa). En una línea de precio fijo, solo tipo, impuesto y descripciones.
- Tipos de facturación: Cobrable, No cobrable, De cortesía; los dos últimos «don't add up to the invoice line total». Es la forma de «castigar» una hora en el borrador: se cambia a no cobrable o cortesía (o se baja cantidad o precio), y la hora sigue costando al proyecto. La palabra «write-off» no aparece en el índice; descuento y flete en la cabecera figuran como «unsupported» (M17).
- No se debe cambiar la «Transaction Classification» de un detalle de factura (rompe la correspondencia con el sin facturar) (M17).
- Se pueden refrescar las transacciones: horas que llegaron después de crear el borrador y marcadas «Ready to Invoice» se agregan (M17).
- Factura confirmada: no se edita; se «revisa»: se genera un borrador nuevo con cantidades en cero (se asume crédito total); si el crédito es parcial se carga la cantidad que sigue facturándose. Al confirmar, el sistema crea una reversa de venta facturada y una nueva venta sin facturar cobrable por lo que sigue pendiente (M18, [L]). Crédito parcial de hito: no soportado.
- Hueco: castigo contable propiamente dicho (baja de WIP a resultado, provisión) no aparece; solo la reclasificación de tipo y el crédito por factura correctiva.

### 4.7 Gastos reembolsables y recargo

- Precio de venta de una categoría de gasto (M9, [L]; M8, [L]): tres métodos, «Price per unit» (tarifa fija por unidad, p. ej. por milla), «At cost» (el precio de venta en el sin facturar es el precio del costo real) y «Markup over cost» (costo más un porcentaje; ejemplo del documento: «the airfare sales rate should be marked up 10 percent over the cost of the incurred airfare expense»).
- En la estimación, «At cost» y «Markup» dan cero por defecto (solo aplican al gasto real) (M8). Si no hay línea de precio para categoría y unidad, el precio de venta es 0.
- Los gastos entran al contrato solo si la línea los incluye («Include Expense») (M12), y solo se facturan si son cobrables.
- FAR (F1, [S]): los materiales se reembolsan a costo permitido y «the Government will not pay profit or fee [...] on materials»: contraste con el recargo de los sistemas comerciales; es regla de un tipo de contrato público de EE.UU.
- Reglas profesionales (ABA 93-379, Regla 1.5) siguen sin leerse (403 en la ronda anterior) y lo de Argentina no se tocó.

## 5. Presupuesto del proyecto y estimación al terminar

- Presupuesto de costo y de ingreso (M19, [L]): un presupuesto es «a point-in-time snapshot of the estimated spend across the project phases and its associated tasks»; aunque cambien los precios luego, la foto no cambia. Hay presupuesto de costo (se compara el costo real de tiempo, material y gasto) y de ingreso (se comparan ventas sin facturar y facturadas). Las líneas de presupuesto tienen dimensiones únicas (categoría, tarea, tipo de costo, proveedor) y cada «actual» se empareja con la línea de más dimensiones coincidentes, y si no hay, se relaja la dimensión de menor prioridad.
- Pronóstico por línea: «The forecast equals the budgeted value when the budget is approved.» Y la regla de piso: «If actual costs are more than the forecasted cost for a budget line, the forecast cost will be made equal to the actual cost.» Es decir, el pronóstico nunca baja del real.
- Desvío: en costo, 0 si el real es menor que el pronóstico, y real menos pronóstico si es mayor; en ingreso, el espejo (M19).
- Revisión: solo se revisa una versión en estado aprobado; la revisión crea una versión nueva en borrador y permite usar los pronósticos como base del presupuesto revisado: «When you must formalize forecasts as a budget, a budget revision is required» (M19, [L]). Hay entonces tres capas: presupuesto aprobado (línea base), pronóstico (actualizable en modo seguimiento) y presupuesto revisado (formaliza el pronóstico).
- Hay una página de «transferir presupuestos a pronósticos» y una de pronóstico por período (en el índice de la versión integrada; no las abrí).
- Estimación de venta y de proyecto (M20, [L]): se estima en dos etapas, preventa (líneas de cotización con detalles de tiempo, gasto, material y honorario) y ejecución (líneas de contrato o plan del proyecto). Se recomienda la estimación de abajo hacia arriba desde las tareas con roles genéricos; al importarla a la cotización se importan valores de venta y de costo y se ven rentabilidad y margen.
- ERPNext (E1, [S]): el proyecto tiene un campo «Estimated Cost»; costo total y monto facturable total salen de las hojas de horas (hora por tarifa de costo y de venta); margen bruto = costo total contra monto facturado, con gastos, compras y materiales consumidos en la fórmula. Porcentaje de avance con cuatro métodos: Manual, Task Completion, Task Progress, Task Weight («sums each task's weight multiplied by its progress»). No hay presupuesto por fase ni EAC.
- Odoo (O4, [S]): rentabilidad con tres etapas por monto (esperado, por facturar, facturado); el presupuesto como tal en proyecto no figura en lo leído.
- Estimación al terminar (EAC) y estimación para terminar (ETC): ninguna de las páginas abiertas usa esas siglas ni esa fórmula; lo más cercano es el «forecast» por línea de Project Operations (real + lo que falta, nunca menos que el real). El método de valor ganado está ya en `Gestion-de-proyectos/Seguimiento/medir-el-avance.md`. Declarado como hueco de práctica de sistemas.

## 6. Recursos canónicos propuestos (para las notas del tema)

1. Reserva: MS `resource-management/booking-status` (M2). Fijarse en la tabla de cambios de estado y en cuál consume capacidad; sirve para la nota de reserva (tentativa y firme). Acompañar con `resource-management-mode-overview` (M3) para quién propone y quién acepta.
2. Rol, habilidad y tarifa: MS `pro/pricing-costing/sales-price-resolution-sales` (M8): el orden de resolución de la tarifa es una descripción compacta de «precio por rol con excepción».
3. Hoja de horas y corrección de lo aprobado: MS `approvals/recall-cancel` (M11): la sección «Impact of a recall request» (reversa, nunca edición) y la regla de lo ya facturado.
4. Tope y backlog: MS `pro/proforma-invoicing/manage-nte-status-validations-sales` (M13) y `proforma-invoicing/manage-billing-backlog` (M16).
5. Hitos y avance: MS `pro/sales/manage-contract-values-project-based-sales` (M12), fila «Invoice Schedule Type».
6. Anticipo y retainer: MS `pro/sales/set-up-advances-retainer-based-contracts-sales` (M15): la sección que contrasta retainer con precio fijo.
7. Borrador de factura y castigos: MS `proforma-invoicing/manage-proforma-invoice` (M17) y `revise-project-invoices` (M18).
8. Gasto con recargo: MS `pricing-costing/set-up-cost-sales-rates-expenses` (M9).
9. Presupuesto y pronóstico: MS `pro/budget/keyconcepts-projectbudget` (M19): la regla de piso del pronóstico.
10. Tope y registro de horas como norma de un tipo de contrato: FAR 52.232-7 (F1), releerla completa antes de citar literal.

## 7. Huecos

1. Sobreasignación y conflicto de reservas entre proyectos: ninguna página abierta lo explica (solo que firme consume capacidad). Falta cómo se detecta, quién arbitra y la matriz.
2. Período de cierre de la hoja de horas (bloqueo después de una fecha): no hay fuente; solo duración diaria máxima e intervalo mínimo.
3. Página de «Role price» de la lista de precios (campos de la línea de rol, precio por unidad de tiempo): no la abrí; la tabla de cabecera sí.
4. Odoo: validación de hojas, tarifas por empleado, anticipo en la factura final, reinvoice de gastos y planificación de sobreasignación: los textos llegaron truncados o resumidos, sin esas partes. ERPNext: estados exactos de la hoja y cancelación.
5. Castigo («write-off») propiamente dicho, provisión y WIP de estudios: los sistemas solo ofrecen reclasificar el tipo de facturación, corregir cantidad o precio, o crédito por factura correctiva. Sin fuente de estudios.
6. EAC y ETC con sus fórmulas en un sistema de servicios: ninguna fuente; solo el pronóstico por línea con piso en el real.
7. Anticipos, «breakage» y no devolución (NIIF 15 B44-B47): sin fuente de práctica.
8. Dinero y ley: lo único normativo es FAR 52.232-7 y es una sola fuente en [S]; todo lo demás es documentación de un producto. Segunda fuente independiente: pendiente (y nada de Argentina).
9. Una sola implementación documentada con detalle (Project Operations) cubre casi todo; no hay segunda fuente de práctica independiente para reserva firme/tentativa, tope ni recall. Marcarlo en las notas como «un sistema hace X».
10. Si el árbol del tema divide Recursos, Horas, Facturación y Presupuesto: coincide con cómo se parte el producto de Microsoft (Resource management, Time, Invoicing, Budget), y no con APQC (ver `proyecto-y-facturacion.md`, sección 0).
