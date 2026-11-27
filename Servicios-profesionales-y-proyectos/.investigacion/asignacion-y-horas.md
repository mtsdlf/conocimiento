# Asignación de recursos y registro de horas: informe de investigación

Alcance: dos verticales del tema Servicios profesionales y proyectos. Fecha: 2026-11-27.

Aviso de método. El presupuesto de búsqueda web de la sesión estaba agotado (WebSearch rechazó todas las consultas). Trabajé solo con fuentes que pude abrir por URL directa: el texto del APQC PCF ya extraído en el scratchpad, la FAR (normas federales de EE.UU. sobre costos de contratos), la hoja del Departamento de Trabajo de EE.UU., y documentación de ERPNext, Odoo y Microsoft Dynamics Project Operations. No entraron libros (Maister, Løwendahl), ni estudios sobre calidad del dato, ni guías de colegios profesionales (ABA devolvió 403). Todo eso queda como hueco. La sección de calidad del dato no tiene ninguna fuente: no inventé cifras.

Marcas: [L] texto leído, [M] metadatos, [S] resumen secundario. Con WebFetch lo que recibí es un resumen hecho por un modelo chico sobre la página, así que las citas de páginas web van marcadas [S]. El PCF lo leí directo desde el archivo local [L].

## Tabla de fuentes

Puntajes 1 a 3: Autoridad / Profundidad / Ejemplos / Unicidad.

| Id | Fuente | Tipo | Marca | A/P/E/U |
|---|---|---|---|---|
| F1 | APQC PCF cross-industry 2024, categorías 5.0, 7.7, 9.2, 9.5, 9.6 (texto local: /tmp/claude-1000/-home-dela-repos-personal-conocimiento/8f0c0cb6-2f82-41a4-8ebf-4fbe94e03c21/scratchpad/pcf.txt) | primaria (marco) | [L] | 3/1/1/3 |
| F2 | FAR 31.201-1, https://www.acquisition.gov/far/31.201-1 | primaria (norma, EE.UU.) | [S] | 3/2/1/3 |
| F3 | FAR 31.201-2, https://www.acquisition.gov/far/31.201-2 | primaria (norma) | [S] | 3/2/1/3 |
| F4 | FAR 52.232-7 (pagos por tiempo y materiales), https://www.acquisition.gov/far/52.232-7 | primaria (cláusula contractual) | [S] | 3/2/2/3 |
| F5 | FAR 31.205-26 (materiales), https://www.acquisition.gov/far/31.205-26 | primaria (norma) | [S] | 3/1/1/2 |
| F6 | US DOL, hoja 21 sobre registros FLSA, https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping | primaria (regulador) | [S] | 3/1/1/2 |
| F7 | Documentación de ERPNext, Timesheet, https://docs.frappe.io/erpnext/user/manual/en/timesheet | práctica de producto | [S] | 2/2/2/2 |
| F8 | Documentación de Odoo, Timesheets, https://www.odoo.com/documentation/19.0/applications/services/timesheets.html | práctica de producto | [S] | 2/1/1/1 |
| F9 | Microsoft Learn, Project Operations, Resource management key concepts, https://learn.microsoft.com/en-us/dynamics365/project-operations/resource-management/resource-management-key-concepts | práctica de producto | [S] | 2/1/2/2 |

Intentadas sin éxito (no cuentan como fuente): eCFR (redirigió a un bloqueo), ABA Formal Opinion 93-379 y ABA Regla 1.5 (403), DCAA Contract Audit Manual (403), Microsoft time-entry y resource-booking (404 en las URL que probé), OpenStax (404), Odoo Planning (error).

## 1. Asignación de recursos

### 1.1 Cómo divide el campo esta parte

- APQC no tiene «asignación» como vertical propia. La ubica dentro de 5.2 «Manage service delivery resources (20040)», con tres ramas: 5.2.1 demanda, 5.2.2 plan de recursos, 5.2.3 habilitación (capacitación). La asignación concreta a un proyecto cae en otro lado: 5.3.1.6 «Identify, select, and assign resources (20065)», con 5.3.1.6.1 «Establish people objectives» y 5.3.1.6.2 «Establish engagement rules», y la liberación en 5.3.3.4 «Release resources (20081)». [F1] [L]
- Consecuencia para el árbol: la vertical abarca dos momentos que APQC mantiene separados, el plan de la firma (5.2, antes de tener proyecto) y la reserva sobre un proyecto (5.3.1.6), más la liberación (5.3.3.4). Conviene decirlo en la nota. La capacitación (5.2.3) queda fuera.
- Microsoft agrupa todo bajo «Resource management» y lo describe como encontrar «the right resources at the right time», reservarlos y mantenerlos ocupados. [F9] [S]

### 1.2 Demanda y capacidad

- APQC 5.2.1 desglosa el pronóstico de demanda en ocho pasos: 5.2.1.1 «Monitor pipeline», 5.2.1.2 «Develop baseline forecasts», 5.2.1.3 «Collaborate with customers», 5.2.1.4 «Develop consensus forecast», 5.2.1.5 «Determine availability of skills to deliver on current and forecast customer orders», 5.2.1.6 «Monitor activity against forecast and revise forecast», 5.2.1.7 «Evaluate and revise forecasting approach», 5.2.1.8 «Measure forecast accuracy». [F1] [L]
- Lectura: el marco parte del embudo y de los pedidos vigentes, pasa por un pronóstico de consenso y cierra midiendo la exactitud. Es un ciclo, no un cálculo único. APQC no dice cómo ponderar el embudo (por probabilidad de cierre); no lo encontré en fuente.
- 5.2.2 plan de recursos: 5.2.2.2 «Create resource plan», 5.2.2.3 «Match resource demand with capacity, skills, and capabilities», 5.2.2.4 «Collaborate with suppliers and partners to supplement skills and capabilities» (subcontratar), 5.2.2.5 «Identify critical resources and supplier capacity», 5.2.2.6 «Monitor and manage resource capacity and availability». [F1] [L]
- Contratar frente a subcontratar: APQC solo tiene el nodo de proveedores y socios (5.2.2.4) y, del lado de personas, la categoría 7. La decisión no está explícita en 5.x. Hueco.
- Banco de personas libres (bench): APQC no usa el término; 5.2.2.6 lo cubre sin nombrarlo. Hueco de fuente.
- Ya escrito en la base: la capacidad dentro de un proyecto está en `Gestion-de-proyectos/` y en `Emprender/Modelo-de-negocio/capacidad-de-un-equipo-de-servicio.md`; el tema nuevo debe enlazarlas.

### 1.3 Habilidades y roles

- APQC 5.2.2.1 «Define and manage skills taxonomy (20051)»; también 5.2.3.6 «Perform skill and capability testing (20057)». [F1] [L]
- Microsoft: «Match skills by identifying the skills defined on the resource demand against available resource skills» y «Maintain a skills and proficiency repository». [F9] [S] Es práctica de un producto: dice que el pedido se compara contra habilidades con nivel, no que sea la forma correcta.
- Rol genérico frente a persona con nombre: Microsoft separa «generic team member records» (con rol y unidad organizativa) de recursos con nombre: «Staff your project with a team of generic or named resources». También «Substitute resources». [F9] [S] Evidencia de práctica de planificar primero por rol y bajar a persona después. Falta fuente primaria que lo justifique.
- Tarifa y costo por rol: ERPNext separa costo y tarifa de venta (ver 2.5) [F7] [S]. No encontré fuente primaria de la tarifa por rol.

### 1.4 Reserva de personas

- Microsoft distingue reservas (bookings) de asignaciones del cronograma (assignments): «Align project schedule assignments and resource bookings» y «Reconcile differences in bookings and assignments»; también «Change resource bookings in response to out-of-office status» y «Collaborate between project managers and resource managers». [F9] [S]
- Respalda dos distinciones: (a) reserva sobre la firma (quién estará dónde) frente a asignación de tarea dentro del proyecto (quién hace qué); (b) hay dos roles, gerente de proyecto y gerente de recursos, que colaboran. La fuente no dice quién decide en un conflicto.
- Reserva tentativa y firme (soft/hard), pedido de recurso, conflictos entre proyectos y matriz de decisión: no los pude leer en fuente (la página de Microsoft sobre estados de reserva dio 404). Hueco.

## 2. Registro de horas

### 2.1 Cómo divide el campo esta parte

- APQC 5.0 no tiene un nodo de registro de horas ni de facturación del proyecto. Hay 5.3.3.2 «Complete/finalize financial management activities (20079)» y 5.3.3.3 «Confirm delivery according to contract terms (20080)». [F1] [L] La hora imputada aparece en otras categorías:
  - 9.2.2.2 «Generate customer billing data (10795)» y 9.2.2.3 «Transmit billing data to customers (10796)».
  - 9.5.1.5 «Analyze and report employee utilization (10857)» y 9.5.2.1 «Enter employee time worked into payroll system (10858)».
  - 7.7.6 «Develop and manage time and attendance systems (10527)».
  - 9.6.2.3 «Approve reimbursements and advances (10882)», 9.6.2.4 «Process reimbursements and advances (10883)», 9.6.3 «Manage corporate credit cards (20929)».
- Sostiene la distinción pedida: la asistencia (horas trabajadas por una persona, de nómina) vive en 7.7.6 y 9.5.2.1, y la hora imputada a un proyecto no tiene casa propia en el marco. Es una discrepancia entre el árbol propuesto y el campo, y conviene decirlo.

### 2.2 La hora imputada y la diferencia con asistencia

- El Departamento de Trabajo de EE.UU. exige registrar por cada trabajador no exento: «Time and day of week when employee's workweek begins», «Hours worked each day», «Total hours worked each workweek». No habla de imputar a proyectos. [F6] [S] Es una obligación legal distinta (solo EE.UU.; lo de Argentina va en la nota aparte).
- ERPNext: «A Timesheet records the hours an employee spends on tasks. It can support billing, payroll, and tracking an employee's contribution to a Project or Task». Cada fila tiene el casillero «Bill» («This box needs to be checked if this particular Time Sheet is a billable»), se etiqueta a un proyecto y, opcionalmente, a una tarea. [F7] [S] Un mismo registro sirve a tres usos y «facturable» es un atributo de la línea.
- Odoo: se puede registrar tiempo solo si «the project itself allows it»; en un proyecto facturable se incluye una línea del pedido de venta para poder facturar el tiempo. Quien tiene «User: all timesheets» puede «view, edit, and validate all employees' timesheets»; la página no describe un flujo de aprobación de varios pasos. [F8] [S] Aquí el proyecto, vinculado al pedido de venta, decide si una hora es facturable.
- ERPNext: la hoja se guarda y luego se presenta (submit); de la hoja presentada se puede crear una factura, y tras presentar las tarifas ya no se editan («Submission locks the rates»). [F7] [S]
- No encontré fuente sobre período de hoja, cierre del período, correcciones después de aprobar, ni la jerarquía proyecto, tarea y actividad. Hueco.

### 2.3 Cómo se respalda una hora ante un tercero

- FAR 52.232-7(a)(5): cada factura se respalda con «Individual daily job timekeeping records», o «Records that verify the employees meet the qualifications», u «Other substantiation approved by the Contracting Officer»; facturas generalmente una cada dos semanas. [F4] [S] Es el único dato firme que hallé sobre frecuencia: un cliente (el Estado de EE.UU.) exige registros diarios como condición de pago por tiempo y materiales. Contrato público estadounidense, no práctica general.
- FAR 31.201-2(d): «A contractor is responsible for accounting for costs appropriately and for maintaining records», «including supporting documentation, adequate to demonstrate that costs claimed have been incurred»; «The contracting officer may disallow all or part of a claimed cost that is inadequately supported». [F3] [S]
- Para una firma privada estas normas no obligan; valen como ejemplo del extremo exigente.

### 2.4 Gastos del proyecto

- FAR 31.201-2(a): un costo es admisible solo si cumple «Reasonableness», «Allocability», estándares CAS «if applicable» (o principios contables generalmente aceptados), «Terms of the contract» y «Any limitations set forth in this subpart». [F3] [S] Da un esquema para decidir si un gasto se traslada al cliente: razonable, imputable a ese proyecto, conforme al contrato.
- FAR 52.232-7(b)(7): «the Government will not pay profit or fee to the prime Contractor on materials», con excepciones en FAR 31.205-26(e) y (f). [F4] [S] Caso de regla expresa sobre recargo (markup). Los recargos de otros clientes los fija el contrato; no encontré fuente general.
- FAR 31.205-26(b): al costo de materiales se le restan «income and other credits, including available trade discounts, refunds, rebates, allowances, and cash discounts». [F5] [S] Se pasa al cliente el costo neto.
- Gastos reembolsables y rendiciones: APQC solo tiene reembolsos en 9.6.2, sin vínculo con proyectos. [F1] [L] `Contabilidad/Operaciones/gastos-y-rendiciones.md` ya cubre la rendición; falta fuente sobre imputarla a proyecto y trasladarla al cliente. La ABA Formal Opinion 93-379 es la fuente canónica probable (cargos al cliente por gastos), pero dio 403 y no la leí. Hueco, y alto riesgo (dinero): hoy no hay dos fuentes independientes.

### 2.5 El costo de la hora: costo cargado frente a tarifa

- FAR 31.201-1: «The total cost ... of a contract is the sum of the direct and indirect costs allocable to the contract, incurred or to be incurred, plus any allocable cost of money ... less any allocable credits.» [F2] [S]
- FAR 52.232-7(a)(4): «The hourly rates shall include wages, indirect costs, general and administrative expense, and profit.» [F4] [S] Composición literal de una tarifa horaria de venta; es la contracara del costo cargado: tarifa = costo cargado + ganancia.
- ERPNext: costo y tarifa son campos separados: «This is the actual cost of work done» frente a «The rate at which the customer needs to be billed for this work»; cada uno se multiplica por las horas. [F7] [S]
- Cómo se calcula el costo cargado (sueldo, cargas sociales, parte de indirectos, dividido por horas facturables o por horas pagadas): no encontré fuente. Hueco. Se puede apoyar en `Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md`.

### 2.6 Calidad del dato

Sin fuentes: subregistro, carga tardía, diario frente a semanal y registro automático quedan vacíos. La única señal indirecta es la regla de registros diarios de FAR 52.232-7(a)(5) [F4] [S], que es una exigencia y no dice nada sobre exactitud. No afirmo cifras. Si se retoma: estudios sobre precisión de tiempo autoinformado primero, blogs de proveedores después y marcados como tales.

## 3. Recursos canónicos propuestos

| Componente | Recurso | Parte | En qué fijarse |
|---|---|---|---|
| Demanda y plan | APQC PCF 5.2.1 y 5.2.2 (F1) | los ocho pasos de 5.2.1 | Es un ciclo con pronóstico de consenso y medida de exactitud; 5.2.1.5 une demanda y habilidades |
| Habilidades | APQC 5.2.2.1 (F1) y Microsoft key concepts (F9) | taxonomía y repositorio con nivel | Comparar la habilidad pedida con la disponible |
| Reserva y roles | Microsoft key concepts (F9) | genéricos frente a con nombre, reserva frente a asignación | Dos roles: gerente de proyecto y de recursos |
| Hora imputada | ERPNext Timesheet (F7) | Bill, Project, Task, costo y tarifa, Submit | Un registro sirve a facturación, nómina y seguimiento |
| Hora como respaldo | FAR 52.232-7(a)(5) y 31.201-2(d) (F4, F3) | registros diarios, respaldo adecuado | Extremo exigente, solo contratos públicos de EE.UU. |
| Costo y tarifa | FAR 52.232-7(a)(4) y 31.201-1 (F4, F2) | composición de la tarifa y costo total | Directos más indirectos; la tarifa incluye ganancia |
| Asistencia frente a hora de proyecto | APQC 7.7.6, 9.5.2.1, 9.5.1.5 (F1) y DOL (F6) | los nodos citados | Tres lugares distintos en el marco |

## 4. Huecos

1. Libros de práctica (Maister, Løwendahl, Oxford Handbook of PSFs): no leídos; faltan bench, contratar o subcontratar y la fórmula de costo cargado con su base de horas.
2. Reserva tentativa y firme, pedido de recurso, conflictos entre proyectos, quién decide, matriz: sin fuente leída.
3. Período de hoja, cierre, correcciones después de aprobar, imputación a proyecto, tarea y actividad: sin fuente (más allá de submit en ERPNext y la validación de Odoo).
4. Gastos reembolsables y recargo: solo reglas de un contrato público de EE.UU.; ABA 93-379 y Regla 1.5 dieron 403; nada de Argentina. Alto riesgo.
5. Calidad del dato: cero fuentes.
6. Costo cargado: solo la composición de la tarifa; falta el cálculo.
7. Casi todo lo web está en [S] (resumen de un modelo sobre la página). Releer la fuente completa antes de citar literal en una nota.
8. No consulté SPI Research ni TSIA.
9. Lo de Argentina (cargas sociales, registro de jornada, facturación de gastos reembolsados) no se tocó; va en la nota aparte.
