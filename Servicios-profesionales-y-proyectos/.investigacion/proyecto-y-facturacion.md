# Investigación: Proyecto del cliente y Facturación del proyecto

Alcance: dos verticales del tema Servicios profesionales y proyectos. Fecha de la investigación: 2026-11-27.

Condición de la investigación: el presupuesto de búsquedas web de la sesión se agotó antes de empezar (WebSearch devolvió «budget is used up»), así que no hubo descubrimiento por buscador. Solo se pudo leer por URL directa lo que ya se conocía o se podía adivinar. Resultado: **las normas (NIIF 15) y el marco APQC quedaron bien respaldados; las prácticas de estudios (lockup, realización), retención en contratos de servicios, anticipos y NIC 11 de primera mano quedaron como huecos**. Todo lo que no tiene URL en este informe no está verificado y figura solo en la sección de huecos.

Leyenda: [L] texto completo leído (o la parte indicada), [M] metadatos o abstract, [S] resumen secundario. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

## 0. Hallazgo estructural sobre el árbol (lo primero)

APQC no tiene una vertical de «proyecto del cliente» ni de «facturación del proyecto» dentro de 5.0. Lo que hay (texto local `pcf.txt`, PCF cross-industry 2024, © APQC):

- **5.3 Deliver service to customer** se divide en 5.3.1 Initiate service delivery, 5.3.2 Execute service delivery y 5.3.3 Complete service delivery.
  - 5.3.1: «5.3.1.1 Review contract and agreed terms (20060)», «5.3.1.3 Modify/revise and approve project plan (20062)», «5.3.1.6 Identify, select, and assign resources (20065)», «5.3.1.7 Plan for service delivery (20068)».
  - 5.3.2: «5.3.2.4 Identify changes (20073)», «5.3.2.5 Obtain approval to proceed (20074)».
  - 5.3.3: «5.3.3.2 Complete/finalize financial management activities (20079)», «5.3.3.3 Confirm delivery according to contract terms (20080)», «5.3.3.4 Release resources (20081)», «5.3.3.7 Archive records and update systems (20084)».
- **No hay en 5.x ningún proceso de facturar el servicio, de presupuesto del proyecto, ni de reconocer ingreso.** La facturación vive en 9.2.2 «Invoice customer (10743)» con «9.2.2.2 Generate customer billing data (10795)» y «9.2.2.3 Transmit billing data to customers (10796)», y 9.5.1.5 «Analyze and report employee utilization (10857)» está en la parte de personal de finanzas. La oferta (con «3.5.3.8 Identify staffing requirements» y «3.5.3.9 Develop pricing and scheduling estimates») está en 3.5.3.
- Consecuencia para el árbol: la división «proyecto del cliente / facturación del proyecto» **no coincide con APQC**; es la división que usan los productos PSA y los libros de firmas de servicios (que atraviesa 3.5, 5.3, 9.2 y 9.3 de APQC). Conviene decirlo en la nota raíz: el tema reúne lo que APQC reparte en cuatro categorías. El cierre financiero del proyecto (5.3.3.2) es la única pieza explícita y APQC solo da el nombre, no el contenido.
- 5.3.2.4 «Identify changes» + 5.3.2.5 «Obtain approval to proceed» es la sucesión cambio detectado, aprobación, y luego recién se ejecuta; sirve de base para la orden de cambio como registro.

Fuente: APQC, PCF cross-industry (texto local `/tmp/claude-1000/-home-dela-repos-personal-conocimiento/8f0c0cb6-2f82-41a4-8ebf-4fbe94e03c21/scratchpad/pcf.txt`, secciones 5.0 y 9.2; «© 2024 APQC. ALL RIGHTS RESERVED»). No se verificó la URL pública de apqc.org en esta sesión.

## 1. Tabla de fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| F1 | APQC PCF cross-industry 2024, 5.0 y 9.2 | (texto local pcf.txt; apqc.org no verificada) | primaria | 3/2/1/3 | [L] las secciones 5.x, 9.2.2 |
| F2 | IFRS Foundation, NIIF 15 texto oficial HTML 2026 | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html | primaria | 3/3/2/3 | [L] por tramos vía el lector de la herramienta (parágrafos 18-21, 35, 39-41, 56, 60-65, 105-109, B14-B19); no se leyó completo |
| F3 | IFRS Foundation, NIIF 15 Ejemplos ilustrativos HTML 2026 | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15-ie.html | primaria | 3/2/3/2 | [L] parcial (ejemplos 18, 19, 42) |
| F4 | IFRS Foundation, página de NIIF 15 (qué reemplaza) | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/ | primaria | 3/1/1/1 | [L] |
| F5 | Odoo 18, Time and materials invoicing | https://www.odoo.com/documentation/18.0/applications/sales/sales/invoicing/time_materials.html | doc de producto (práctica) | 2/2/2/1 | [L] casi toda (faltó la cola) |
| F6 | ERPNext/Frappe, Project Profitability | https://docs.frappe.io/erpnext/user/manual/en/project-profitability | doc de producto (práctica) | 2/1/1/1 | [L] |
| F7 | Wikipedia, Retainage | https://en.wikipedia.org/wiki/Retainage | secundaria | 1/2/1/1 | [S] |
| F8 | Wikipedia, Time and materials | https://en.wikipedia.org/wiki/Time_and_materials | secundaria | 1/1/1/1 | [S] |
| F9 | Wikipedia, Percentage-of-completion method (cita IAS 11.42-43) | https://en.wikipedia.org/wiki/Percentage-of-completion_method | secundaria | 1/1/2/1 | [S] |
| F10 | Wikipedia, Professional services automation | https://en.wikipedia.org/wiki/Professional_services_automation | secundaria | 1/1/1/1 | [S] |

No leídas (error 403/404 o sin acceso, no cuentan como fuentes): ifrs.org PDF de NIIF 15 e IAS 11 (suscripción o 404), iasplus.com (devuelve solo «IAS»), eur-lex (vacío), PwC Viewpoint (403), Microsoft Learn Project Operations (404 en las rutas probadas), Odoo prepaid hours, milestones y billing rates (404 en las rutas probadas), ABA Model Rule 1.15 (403), OpenStax job order (404 en la ruta probada).

## 2. Proyecto del cliente

### 2.1 De la venta al proyecto

- APQC pone la entrada del proyecto en 5.3.1 como una secuencia: revisar el contrato y los términos acordados (5.3.1.1), definir el enfoque, revisar y aprobar el plan del proyecto (5.3.1.3), identificar, seleccionar y asignar recursos (5.3.1.6, con «Establish engagement rules») y planificar la entrega (5.3.1.7). Fuente F1.
  - Lectura para el árbol: el proyecto nace de un contrato o presupuesto aceptado y su primer acto es **leer los términos de cobro**, que gobiernan después el registro (tipo de facturación). Conecta con los documentos de `Relacion-con-clientes/` y con `Desarrollo/Encargo/modelos-de-contrato-y-cobro.md`.
- Un sistema abierto crea el proyecto desde la venta: en Odoo, «Confirm the sales order, which creates the project and task» y las horas aparecen luego en la orden de venta en la columna «Delivered». F5. Dato de práctica: **la línea de venta de servicio es el ancla que une proyecto, horas y factura**; el producto servicio lleva una política de facturación («Based on Timesheets») y solo los productos de tipo servicio se facturan por tiempo. F5.
- ERPNext modela el proyecto como una etiqueta (dimensión) que cuelga de documentos de compra y venta: «Purchase Orders, Purchase Receipts, and Purchase Invoices can be linked to a project through the Project field» y lo mismo para Sales Order, Delivery Note, Sales Invoice y Payment; la rentabilidad se calcula con «the income and expense entries linked to the project». F6. Evidencia de que el proyecto como **dimensión de los asientos** es el mínimo viable (concuerda con `Contabilidad/.../centros-de-costo.md`, que ya existe en la base).
- PSA, según Wikipedia (secundaria): cubre «project management and resource management for client projects and utilization rate management for billable staff»; funciones típicas «project management and documentation, time recording, billing, reporting, and resource utilization»; da visibilidad de «mid-project profitability». F10. Sirve solo para delimitar el término.

Estados del proyecto (borrador, activo, en pausa, cerrado) y facturable frente a interno: **no encontré fuente primaria**. Lo único respaldado es el ciclo de APQC (iniciar, ejecutar, completar: 5.3.1 a 5.3.3) y el cierre con «Release resources (20081)» y «Archive records and update systems (20084)». F1. Los cuatro estados son una síntesis de práctica, no un estándar; declararlo así en la nota.

### 2.2 Cierre financiero del proyecto (5.3.3)

- 5.3.3.2 «Complete/finalize financial management activities» y 5.3.3.3 «Confirm delivery according to contract terms»: el cierre financiero es un paso separado de la entrega y apoyado en el contrato. F1. APQC no detalla qué contiene; **hueco**: lo que incluye (últimos tiempos, facturar el remanente, liberar retenciones, cancelar saldos de WIP, cerrar el proyecto a nuevos cargos) no tiene fuente leída.
- NIIF 15 trata la aceptación del cliente como evidencia en sus parágrafos B83-B86 (solo se leyó el rótulo de la sección, no el contenido). F2.

### 2.3 Presupuesto del proyecto: línea base y re-pronóstico

- ERPNext: se crea un Budget para el proyecto y «The expense limit defined in the Budget will be validated in the expense transactions». F6. Es evidencia de práctica de un presupuesto de **costo** con tope validado en los gastos, no de horas/precio por fase/rol.
- No encontré fuente leída para: presupuesto en horas, costo y precio por fase/tarea/rol, línea base, EAC/ETC como dato. **Hueco**. El método (valor ganado, EAC) ya está en `Gestion-de-proyectos/Seguimiento/medir-el-avance.md`; este tema solo necesita el esquema del registro. A buscar: PMI Practice Standard for Earned Value Management (pago) o guías abiertas de EVM, y las guías de productos PSA (Kantata, Certinia, Dynamics) para el esquema.

### 2.4 Hitos y entregables como registro

- NIIF 15 B14: los métodos de medición del avance son «output methods (see paragraphs B15–B17)» e «input methods (see paragraphs B18–B19)». B15 abre con «Output methods include methods such as surveys of performance completed to date, appraisals of results achieved» (el extracto leído está cortado; el texto completo del parágrafo incluye hitos alcanzados y tiempo transcurrido, a confirmar). F2.
- B17: «The disadvantages of output methods are that the outputs used to measure progress may not be directly observable». F2. Fundamenta por qué un hito es un evento de aceptación observable y no una estimación.
- Hito como disparador de factura: la única mención leída es indirecta, en Odoo: «The sales order only appears as an option if it includes a service billed by timesheets, milestones, or delivered quantities». F5.

### 2.5 Orden de cambio (registro y plata)

- NIIF 15 18: «A contract modification is a change in the scope or price (or both) of a contract that is approved by the parties.» F2. Es la definición más precisa leída: **el cambio tiene alcance y/o precio y está aprobado**.
- 19: puede existir modificación aunque haya disputa sobre alcance o precio; si el precio no está resuelto se estima con las reglas de contraprestación variable. F2.
- 20: contrato separado cuando se agregan bienes o servicios **distintos** y el precio sube por su precio de venta independiente; 21: si no, se trata como parte del contrato existente (ajuste acumulativo) o como contrato nuevo según el caso. F2. Dato de modelado: el registro de la orden de cambio debe distinguir «suma un servicio distinto a precio de lista» de «cambia el alcance del mismo servicio».
- 56: la contraprestación variable entra solo «to the extent that it is highly probable that a significant reversal in the amount of cumulative revenue recognised». F2. Aplica a cambios no aprobados con precio pendiente.
- Que APQC separe 5.3.2.4 «Identify changes» de 5.3.2.5 «Obtain approval to proceed» respalda el estado intermedio del cambio (identificado frente a aprobado). F1.
- Hueco: formularios de orden de cambio de práctica (AIA G701, FIDIC) y el impacto en calendario. Sin leer.

## 3. Facturación del proyecto

### 3.1 Tiempo y materiales

- Definición (secundaria): el cliente paga la mano de obra según el tiempo y los materiales, «no matter how much work is required», útil cuando el tamaño no puede estimarse con precisión o los requisitos cambiarán; el contraste es el precio fijo, donde el contratista absorbe el riesgo. F8; la misma idea en Odoo («size can't be estimated accurately or whose requirements may change», F5). Dos redacciones del mismo sentido, no cuentan como dos fuentes independientes.
- Tope: Wikipedia no usa «not-to-exceed» pero describe el precio máximo garantizado: «puts an upper limit on what the contractor may charge». F8. **Hueco**: no hay fuente leída para NTE o tope en servicios profesionales.
- Del tiempo a la factura (práctica): en Odoo se cargan líneas de hoja de horas por empleado, fecha y horas; vuelven a la orden de venta como «Delivered»; se crea un borrador de factura («Create Draft Invoice») y se revisa antes de confirmar. Los gastos reembolsables se reinvoican desde la orden de venta. F5. El documento fuente del cobro es la línea de la orden, no la hoja de horas.
- NIIF 15 B16: si el derecho a cobrar equivale directamente al valor entregado al cliente, se puede reconocer el ingreso por el monto facturable. El ejemplo oficial es «Example 42, Contract A (IE213–IE214)»: limpieza a «CU25 per hour»; la entidad «has a right to invoice the customer in the amount that corresponds directly with the value» de lo completado. F3. Es la forma contable de T&M: ingreso = horas aprobadas × tarifa, sin estimar el avance.
- Tarifas por rol/persona/cliente: Odoo remite a una página de tarifas que no se pudo leer. F5. **Hueco**.
- Ajustes y castigos antes de facturar (write-down/write-off): **sin fuente**. Hueco principal de esta vertical (es práctica de estudios, ver sección 4).

### 3.2 Por hito o precio cerrado; anticipos; retención

- Calendario por hito: ver 2.4. Un cobro que se adelanta al servicio genera pasivo del contrato (ver 3.4).
- Anticipos: NIIF 15 B44-B47 trata los prepagos y los derechos no ejercidos (breakage); solo se leyó el rótulo de la sección. F2. El contenido es **hueco**.
- Retención: definida como «a portion of the agreed upon contract price deliberately withheld until the work is complete»; típico 5 % en Reino Unido y 10 % en EE. UU., a veces bajando a 5 % al 50 % de avance; se libera al terminar y, en Reino Unido, al cierre del período de responsabilidad por defectos (aprox. 12 meses). F7 (secundaria y de **construcción**, no de servicios profesionales). Dinero: una sola fuente secundaria, hay que decirlo así. En servicios profesionales es poco común; lo más cercano es la retención de garantía en ingeniería y arquitectura. Fuente primaria faltante.
- Financiación: NIIF 15 60-65. Se ajusta la contraprestación por el valor tiempo del dinero, con la excepción del 63: «need not adjust» si el plazo esperado entre transferencia y pago es de un año o menos. F2. Para anticipos y retenciones de servicios cortos, lo normal es la excepción.

### 3.3 Abono y bolsa de horas prepaga

- Evidencia de práctica: ninguna leída.
- Marco conceptual: NIIF 15 Ejemplo 18 (club de salud): acceso por período como obligación satisfecha con medida de tiempo, a línea recta: «CU100 per month (CU1,200 over the year)»; el beneficio se reparte parejo «whether or not the customer uses the clubs». F3. Es la base contable de un **abono de disponibilidad** (se reconoce por tiempo transcurrido aunque no se use). La bolsa de horas consumibles es distinta: cada hora entregada es la medida y el saldo no consumido es pasivo hasta que se consume o vence. Esto último es inferencia mía desde B44-B47 y 106, **no verificado en texto**.
- Hueco: horas que vencen o se trasladan (breakage), drawdown y caducidad según la ley argentina.

### 3.4 WIP, ingreso a lo largo del tiempo, activo y pasivo del contrato

NIIF 15 (texto oficial, F2):

- 35: ingreso a lo largo del tiempo si se cumple alguno de tres criterios: (a) «the customer simultaneously receives and consumes the benefits provided by the entity's performance as the entity performs»; (b) «that the customer controls as the asset is created or enhanced»; (c) «the entity's performance does not create an asset with an alternative use to the entity», más derecho exigible al pago de lo completado a la fecha.
- 39: «an entity shall recognise revenue over time by measuring the progress towards complete satisfaction» de la obligación. 40: «An entity shall apply a single method of measuring progress for each performance obligation satisfied over time.» 41: «Appropriate methods of measuring progress include output methods and input methods.»
- Producto: B15-B17. Insumo: B18, «resources consumed, labour hours expended, costs incurred, time elapsed or machine hours used». B19: ajustar cuando un costo incurrido no es proporcional al avance.
- Ejemplo 19 (F3): contrato de CU5.000.000, costos esperados CU4.000.000, de los cuales CU1.500.000 son ascensores obtenidos antes de instalarse; se excluyen del avance. Al 31/12/20X2: «20% (CU500,000 ÷ CU2,500,000)»; ingreso «20% × CU3,500,000 + CU1,500,000 = CU2,200,000»; costo de ventas CU2.000.000; ganancia CU200.000. Es el ejemplo oficial de costo incurrido sobre costo total con ajuste. Viene de construcción; en servicios el insumo típico son las horas.
- 105: «When either party to a contract has performed, an entity shall present the contract in the statement of financial position as a contract asset or a contract liability...»; 106: pasivo del contrato = obligación de transferir bienes o servicios; 107: «A contract asset is an entity's right to consideration in exchange for goods or services that the entity has transferred...»; 108: «A receivable is an entity's right to consideration that is unconditional.»; 109: la norma «does not prohibit an entity from using alternative descriptions» (se puede decir «trabajo en curso sin facturar» o «ingreso diferido»).
- Mapeo a los términos del brief (mi lectura de 105-109, a confirmar en la nota): WIP sin facturar con derecho condicionado a algo más que el paso del tiempo = activo del contrato; incondicional = cuenta a cobrar; facturado por adelantado = pasivo del contrato (ingreso diferido).
- NIC 11: «IFRS 15 replaces IAS 11 (Construction Contracts) and IAS 18 (Revenue)», para períodos desde el 1 de enero de 2018 (F4). Del contenido de NIC 11 solo hay secundaria: presentaba «the gross amount due from customers for contract work as an asset» (IAS 11.42-43) y, esperada una pérdida, «the full amount of the loss must be recognized immediately» (F9, de segunda mano). Texto primario de NIC 11: no leído.
- ASC 606: **no leído**. No se afirma nada sobre ASC 606 en este informe.

Dos observaciones para el árbol:
1. La base ya tiene NIIF 15 en cinco pasos en `Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md`. La vertical de servicios debe enlazarlo y quedarse con lo propio: la medida del avance en horas, el WIP como activo del contrato y la factura como evento distinto del ingreso.
2. «Hito como método de producto» y «costo incurrido como método de insumo» son opciones de contabilidad, mientras que «facturar por hito» es una cláusula de cobro; pueden no coincidir, y de la diferencia nace el activo o el pasivo del contrato. Reconocer no es facturar: es la idea más útil de la vertical.

## 4. Lockup, realización y castigos (estudios)

Sin fuente leída. Ni ABA, ni Law Society, ni AICPA, ni Maister sobre lockup pudieron consultarse (ABA Rule 1.15 dio 403; sin buscador). **Hueco completo**: definición de lockup (WIP + cuentas a cobrar en días), cifras de referencia, realización, práctica de castigos y la regla de mantener separados los anticipos de honorarios hasta devengarse. El único puente es 9.5.1.5 de APQC «Analyze and report employee utilization» (F1) y la ecuación de Maister ya en `Emprender/Modelo-de-negocio/economia-de-una-firma-de-servicios.md`.

## 5. Recursos canónicos propuestos

| Componente | Recurso | Parte | En qué fijarse |
|---|---|---|---|
| Del contrato al proyecto | APQC PCF 5.3.1 y 5.3.3 (F1) | 5.3.1.1 a 5.3.1.7; 5.3.3.2 a 5.3.3.7 | El contrato se lee primero, el cierre financiero es un paso aparte; APQC no cubre la facturación |
| Orden de cambio | NIIF 15 parágrafos 18-21 y 56 (F2) | las cuatro definiciones | alcance y/o precio, aprobado; contrato separado o no; precio no resuelto = estimación |
| T&M y derecho a cobrar | NIIF 15 B16 + Ejemplo 42 (F2, F3) | IE213-IE214 | ingreso igual al monto facturable cuando equivale al valor entregado |
| Ingreso a lo largo del tiempo | NIIF 15 35, 39-41, B14-B19 y Ejemplo 19 (F2, F3) | métodos de producto e insumo | un solo método por obligación; excluir costos no proporcionales |
| WIP, anticipos | NIIF 15 105-109 (F2) | las cuatro definiciones | activo del contrato frente a cuenta a cobrar frente a pasivo del contrato; derecho incondicional |
| Práctica de sistemas | Odoo, T&M invoicing (F5) | pasos orden de venta, horas, borrador de factura | la línea de venta como ancla; reinvoicing de gastos |
| Abono | NIIF 15 Ejemplo 18 (F3) | health club | reconocimiento por tiempo, independiente del uso |

Por conseguir (no encontrados): texto de NIC 11, ASC 606-10-25-27 a 25-37 y 45, Maister (capítulos de finanzas y lockup), ABA o Law Society sobre cuentas de fideicomiso y lockup, AIA G702/G703 y G701 para retención y orden de cambio, documentación de Dynamics Project Operations y Kantata/Certinia para el esquema de presupuesto de proyecto.

## 6. Huecos

1. Estados del proyecto y proyecto facturable frente a interno: sin fuente; síntesis propia.
2. Presupuesto del proyecto por fase/tarea/rol (horas, costo, precio), línea base, EAC/ETC como esquema de datos: sin fuente.
3. Formularios de orden de cambio reales y su impacto en calendario: sin fuente.
4. Tarifas por rol/persona/cliente, topes NTE, castigos y ajustes antes de facturar: sin fuente primaria.
5. Retención en servicios: una sola fuente secundaria, de construcción.
6. Anticipos y breakage (NIIF 15 B44-B47): solo el rótulo.
7. Abono y bolsa de horas: sin fuente de práctica; la afirmación sobre saldo consumible es inferencia.
8. NIC 11 primaria y ASC 606: no leídos. Dinero y ley (alto riesgo) pide dos fuentes independientes: **hoy hay una sola (IFRS Foundation) para NIIF 15 y ninguna para ASC 606**.
9. Lockup, realización, WIP de estudios: sin fuente.
10. Lo de Argentina (facturación electrónica, normas contables locales): no investigado por este ángulo.
11. Método: sin buscador no se hicieron las tres rondas por componente. Reintentar cuando se renueve el presupuesto de WebSearch.
12. Las citas de NIIF 15 llegaron por el extractor de la herramienta, con recortes; lo entrecomillado es literal de ese extracto, pero 105-109 y B14-B19 conviene releerlos enteros en la fuente antes de citarlos como texto de la nota.
