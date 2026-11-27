# Investigación: Legajo y Tiempo y asistencia (Administración de personal y nómina)

Fecha de la investigación: 2026-11-27. Todo lo traído de la web es dato. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Las herramientas de lectura devuelven resúmenes de un modelo pequeño: las "citas literales" salen de ese resultado; donde la fuente primaria bloqueó (403/404) lo digo.

Advertencia general: no pude leer APQC, SHRM BASK, CIPD, Dessler ni Armstrong (ver Huecos). Los componentes se apoyan en normas de la OIT (leídas solo de forma indirecta), guías de organismos de país (EE. UU., Reino Unido) y documentación de software abierto.

---

## 0. Fuentes transversales

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| T1 | Fowler, Effectivity / Temporal Property / actual vs. record (timeNarrative) | https://martinfowler.com/eaaDev/timeNarrative.html | secundaria (patrón de diseño) | 3/2/2/3 | [L] |
| T2 | ERPNext/Frappe docs, Leave Application | https://docs.frappe.io/erpnext/user/manual/en/leave-application | primaria (doc de producto, evidencia de práctica) | 2/2/3/2 | [L] |
| T3 | Odoo docs, Attendances | https://www.odoo.com/documentation/18.0/applications/hr/attendances.html | primaria (doc de producto) | 2/2/3/2 | [L] |
| T4 | 29 CFR 516 (516.2, 516.5, 516.6), vía Cornell LII | https://www.law.cornell.edu/cfr/text/29/516.2 | primaria (norma de EE. UU., ejemplo de país) | 3/3/2/2 | [L] |

---

## A) Legajo

### A1. legajo (datos, historia con vigencias, acceso, retención)

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| 29 CFR 516.2 (datos por empleado) | https://www.law.cornell.edu/cfr/text/29/516.2 | primaria, EE. UU. | 3/3/2/2 | [L] |
| 29 CFR 516.5 (3 años) | https://www.law.cornell.edu/cfr/text/29/516.5 | primaria, EE. UU. | 3/2/1/2 | [L] |
| 29 CFR 516.6 (2 años) | https://www.law.cornell.edu/cfr/text/29/516.6 | primaria, EE. UU. | 3/2/1/2 | [L] |
| Fowler, timeNarrative | https://martinfowler.com/eaaDev/timeNarrative.html | secundaria | 3/2/2/3 | [L] |
| GOV.UK, employment records | https://www.gov.uk/employment-records | primaria, RU | - | no leída: 404 |
| GOV.UK, personnel records and data protection | https://www.gov.uk/personnel-records-and-data-protection | primaria, RU | - | no leída: 404 |

Afirmaciones:
- EE. UU. (ejemplo de país): por cada empleado cubierto por salario mínimo y horas extra se guardan, entre otros, nombre legal, domicilio, "Date of birth, if the employee is under 19", sexo y ocupación, base de pago, horas por día y por semana, ganancias, premio por horas extra, "additions to and deductions from wages", fecha de pago y período. https://www.law.cornell.edu/cfr/text/29/516.2
- Retención en EE. UU.: registros de nómina y de empleados "at least 3 years" desde la última entrada (516.5); tarjetas de tiempo, tablas de tarifas y registros de descuentos "at least 2 years" (516.6). https://www.law.cornell.edu/cfr/text/29/516.5 y https://www.law.cornell.edu/cfr/text/29/516.6. Una sola fuente por cada número; no hay segunda fuente independiente (la de GOV.UK falló). Los plazos varían por país: no es un dato agnóstico.
- Historia con vigencias: Fowler distingue tiempo actual ("the time something happened", valid time) de tiempo de registro ("the time we knew about it", transaction time) y dice "bi-temporal information always needs both dates". Un legajo que contesta "cuál era el sueldo el 25/2 y qué creíamos entonces" necesita las dos fechas. Una propiedad temporal es "an accessor that is parameterized by date". https://martinfowler.com/eaaDev/timeNarrative.html
- Evidencia de modelado (software abierto): la licencia es un registro con empleado, tipo, desde/hasta y estado, no un campo sobre el empleado (ver B3); se modela como evento con fechas, no como valor pisado. https://docs.frappe.io/erpnext/user/manual/en/leave-application
- Quién lo ve, datos sensibles, salud: la fuente prevista (ICO, employment practices) no la pude leer. Solo hay el resumen del buscador sobre monitoreo (ver B2). Hueco.

Recurso canónico: Fowler timeNarrative (parte: Effectivity, Temporal Property y la distinción actual/registro; fijarse en que el legajo necesita fecha desde y fecha de registro para corregir retroactivamente). Para el contenido mínimo, 29 CFR 516.2 como lista ejemplo (aclarando que es de EE. UU.).

Posición contraria: acumular datos "por si acaso". El resumen de la ICO sobre monitoreo exige que sea "necessary and proportionate" (ver B2) [S]; la misma lógica de minimización aplica al legajo, pero no pude verificarla en la guía de legajos de la ICO.

### A2. puesto-y-estructura

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| ERPNext Leave Application (aprobador del empleado o del departamento) | https://docs.frappe.io/erpnext/user/manual/en/leave-application | primaria | 2/1/2/2 | [L] |
| Odoo/ERPNext Employee, Department, Designation | no consultadas | - | - | hueco |

Afirmaciones:
- En software abierto el jefe/aprobador cuelga del empleado y, si falta, del departamento: "Leave Approver: taken from the employee or, if empty, from the department's approver table". https://docs.frappe.io/erpnext/user/manual/en/leave-application
- Puesto frente a persona, posición vacante y organigrama como registro: no encontré fuente leída. Hueco.

Recurso canónico: sin recurso verificado. Candidato: doc de Employee/Designation/Department de ERPNext HRMS y Odoo Employees.

### A3. modalidades-de-contratacion

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| OIT R198 párr. 13, citado en el helpdesk de la OIT | https://www.ilo.org/ilo-helpdesk-questions-and-answers-business-and-employment-security | primaria (OIT, cita del texto) | 3/2/1/3 | [L] de la cita; normlex dio 403 |
| R198 PDF (copia pública) | https://www.wecglobal.org/uploads/2019/07/2006_ILO_Recommendation-198.pdf | primaria (copia) | 3/3/1/3 | no extraíble (PDF binario) |
| US DOL, misclassification / economic reality | https://www.dol.gov/agencies/whd/flsa/misclassification | primaria, EE. UU. | 3/2/2/2 | [L] |
| Revisión jurídica lituana sobre R198 | https://www.journals.vu.lt/teise/en/article/view/42279/39581 | secundaria | 2/2/1/2 | [S] |

Afirmaciones:
- R198 párr. 13 da indicadores de relación de trabajo; entre ellos que el trabajo "is carried out according to the instructions and under the control of another party", "involves the integration of the worker in the organization of the enterprise", "is performed solely or mainly for the benefit of another person", "is carried out within specific working hours or at a workplace specified or agreed by the party requesting the work", "involves the provision of tools, materials and machinery by the party requesting the work"; y de remuneración: "periodic payment of remuneration", "sole or principal source of income", "recognition of entitlements such as weekly rest and annual holidays", "absence of financial risk for the worker". https://www.ilo.org/ilo-helpdesk-questions-and-answers-business-and-employment-security
- Es una lista no vinculante ("might include"); el buscador indica que la R198 prevé una presunción legal cuando hay uno o más indicadores y que no precisa cuántos bastan. https://www.journals.vu.lt/teise/en/article/view/42279/39581 [S]. Verificar contra el texto oficial antes de escribir.
- EE. UU.: prueba de "realidad económica" con cinco factores; los dos centrales son control ("the nature and degree of control over the work") y oportunidad de ganancia o pérdida; otros: habilidad, permanencia, si es "part of an integrated unit of production". Si es empleado y no hay exención, "must be paid not less than the federal minimum wage and overtime pay". https://www.dol.gov/agencies/whd/flsa/misclassification. Esa página no describe sanciones.
- Por qué importa (consecuencias, costos): sin fuente leída. Hueco.
- Tipos (plazo fijo, eventual, tiempo parcial, prueba): sin fuente, salvo que GOV.UK trata el tiempo parcial en vacaciones (5.6 semanas prorrateadas) https://www.gov.uk/holiday-entitlement-rights [L].
- Dos fuentes sobre clasificación: OIT (indicadores) y DOL (factores) son independientes entre sí y coinciden en control e integración.

Recurso canónico: R198 párr. 13 (lista de indicadores) como criterio agnóstico, más la página del DOL como ejemplo de test operativo. Ambos son un haz de indicios, no una regla única.

Posición contraria: "contratista independiente = más barato y sin riesgo". R198 y DOL ponen el peso en la realidad del vínculo (control, dependencia económica) y no en el nombre del contrato. Es lectura mía de las dos fuentes; no leí una cita de "primacía de la realidad".

### A4. ingreso-y-egreso

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| GOV.UK, right to work checks (guía del empleador) | https://www.gov.uk/government/publications/right-to-work-checks-employers-guide | primaria, RU | 3/1/1/2 | [M]: la página no trae plazos; la guía es un PDF de 83 págs. no leído |

Afirmaciones: la página indica que la guía cubre "when to carry out initial checks, follow-up checks, and what happens under TUPE". No obtuve retención de copias. Alta/baja, documentos, registro ante seguridad social, devolución de bienes, cierre de accesos: sin fuente leída. Hueco grande.

Recurso canónico: sin recurso verificado. Candidato: el PDF de right to work (RU) y I-9 (EE. UU.) como ejemplos de país.

### A5. busquedas-y-postulantes (solo registro)

Sin fuente leída. Candidatos no consultados: ICO "Recruitment and selection", EEOC recordkeeping. Hueco total.

---

## B) Tiempo y asistencia

### B1. jornada-y-turnos

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| GOV.UK, maximum weekly working hours | https://www.gov.uk/maximum-weekly-working-hours | primaria, RU | 3/2/1/2 | [L] |
| US DOL, overtime | https://www.dol.gov/agencies/whd/overtime | primaria, EE. UU. | 3/2/1/2 | [L] |
| OIT C001/C030 (horas) | https://normlex.ilo.org | primaria | - | no leída: 403 |
| Odoo Attendances (horas extra, tolerancias) | https://www.odoo.com/documentation/18.0/applications/hr/attendances.html | primaria | 2/2/3/2 | [L] |

Afirmaciones:
- RU: no más de 48 horas semanales de promedio, "normally averaged over 17 weeks"; se puede optar por exceder; menores de 18: 8 horas diarias y 40 semanales; hay excepciones (servicios de emergencia, seguridad, trabajos donde "working time isn't measured"). https://www.gov.uk/maximum-weekly-working-hours. La página no cubre descansos.
- EE. UU.: salvo exentos, horas "over 40 in a workweek" a 1.5 veces la tarifa regular; la semana de trabajo es un período fijo de 168 horas y no se promedia entre semanas; fines de semana y feriados no dan recargo por sí solos a nivel federal. https://www.dol.gov/agencies/whd/overtime
- Discrepancia ilustrativa: RU limita por promedio de 17 semanas; EE. UU. por semana fija de 40 horas con recargo y sin promedio. El concepto agnóstico es (límite, período de cómputo, recargo, exenciones); los valores son de país.
- Modelado: Odoo guarda horas trabajadas y horas extra con validación (automática o por el gerente), tolerancias a favor del empleado y de la empresa en minutos, y permite descontar horas extra aprobadas de la licencia (banco o compensación de horas en la práctica). https://www.odoo.com/documentation/18.0/applications/hr/attendances.html
- Convenios OIT C001/C030, turnos rotativos, descansos: sin lectura. Hueco.

Recurso canónico: C001/C030 en normlex para el piso (no leídos); como práctica, GOV.UK + DOL overtime para mostrar que el cómputo difiere; Odoo para el modelado.

### B2. registro-de-asistencia

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Odoo Attendances | https://www.odoo.com/documentation/18.0/applications/hr/attendances.html | primaria | 2/2/3/2 | [L] |
| ICO, Monitoring workers (guía oct. 2023) | https://ico.org.uk/media/for-organisations/uk-gdpr-guidance-and-resources/employment-information/employment-practices-and-data-protection-monitoring-workers-1-0.pdf | primaria, RU | 3/3/1/3 | [S]: PDF dio 403 |
| ICO, nota de prensa | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2023/10/ico-publishes-guidance-to-ensure-lawful-monitoring-in-the-workplace | primaria | 3/1/1/2 | [S] |
| ERPNext HRMS Shift Type / Attendance | https://docs.frappe.io/hrms/shift-type | primaria | - | no leída: 404 |
| Ravid, Behrend et al., Personnel Psychology 2023 (meta-análisis), vía APA Monitor | https://www.apa.org/monitor/2026/11-12/hidden-costs-workplace-surveillance.html | secundaria | 2/1/1/3 | [S] |
| JRC / Univ. St Andrews, vigilancia y confianza | https://news.st-andrews.ac.uk/?p=21134 | secundaria | 2/1/1/2 | [S] |

Afirmaciones:
- Modelado de marcación: cada registro tiene entrada y salida, tiempo trabajado como suma de pares, modo (quiosco, barra de sistema o manual), IP, navegador y GPS opcional. Entradas sin salida en 24 horas o con un período de más de 16 horas se marcan como error y alguien con permiso las corrige o borra. Salida automática según el horario más una tolerancia. https://www.odoo.com/documentation/18.0/applications/hr/attendances.html
- Licencia y asistencia se enlazan: al aprobar una licencia se crea un registro de asistencia "On Leave" por cada día. https://docs.frappe.io/erpnext/user/manual/en/leave-application
- Marco de privacidad (RU, ejemplo): el monitoreo debe ser "necessary and proportionate"; en general hay que avisar antes; el consentimiento rara vez es base válida por el desequilibrio de poder; hay secciones sobre fichaje biométrico; los datos del monitoreo están sujetos a pedido de acceso. https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2023/10/ico-publishes-guidance-to-ensure-lawful-monitoring-in-the-workplace [S]. Verificar contra el PDF antes de citar literal.
- Conciliación de marcaciones con el turno, tardanzas, trabajo remoto, timesheet: sin lectura. Hueco (el doc de Shift de ERPNext falló).

Posición contraria (mitos y errores):
- "El fichaje o la vigilancia miden y mejoran la productividad": el meta-análisis de monitoreo electrónico del desempeño (Ravid, Behrend y otros, 2023) no halló mejora del desempeño y sí más estrés, según el resumen. https://www.apa.org/monitor/2026/11-12/hidden-costs-workplace-surveillance.html [S]. St Andrews/JRC: sin propósito explícito, la recolección "for its own sake" genera actitudes negativas y menos confianza. https://news.st-andrews.ac.uk/?p=21134 [S]. Un informe del GAO de 2024 recoge opiniones divididas (algunas dicen que puede mejorar la productividad). Hay discrepancia, las fuentes son secundarias y no vi tamaños de efecto.
- Distinción útil: el fichaje registra presencia y horas (insumo de liquidación y de cumplimiento de límites), no resultado. Inferencia mía, apoyada en que Odoo lo usa para tiempo trabajado y extra, no para desempeño.

Recurso canónico: ICO monitoring workers (secciones sobre biometría y proporcionalidad) para el límite de qué se puede registrar; Odoo Attendances para el modelo del registro y sus correcciones. Verificar el PDF de la ICO a mano.

### B3. licencias-y-ausencias

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| GOV.UK, holiday entitlement | https://www.gov.uk/holiday-entitlement-rights | primaria, RU | 3/2/2/2 | [L] |
| OIT C132, copia pública | https://lankalaw.net/wp-content/uploads/2024/12/C132-Holidays-with-Pay-Convention-Revised-1970.pdf | primaria (copia) | 3/3/1/3 | [S]: no leída, solo resultado del buscador |
| OIT C132 en normlex | https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_INSTRUMENT_ID:312319 | primaria | - | no leída: 403 |
| ERPNext Leave Application | https://docs.frappe.io/erpnext/user/manual/en/leave-application | primaria | 2/2/3/2 | [L] |
| SHRM, 4 lessons about unlimited vacation | https://www.shrm.org/ResourcesAndTools/hr-topics/benefits/pages/4-lessons-about-unlimited-vacation.aspx | secundaria | 2/1/2/2 | [S] |
| Wharton, unlimited vacation | https://knowledge.wharton.upenn.edu/article/unlimited-vacation-time-sounds-great-policies-deliver/ | secundaria | 2/1/1/2 | [S] |

Afirmaciones:
- RU: casi todos los trabajadores tienen "5.6 weeks' paid holiday a year"; tope de 28 días; part-time prorrateado (3 días por semana = 16.8 días); irregulares y de temporada acumulan según horas trabajadas; los feriados pueden contarse dentro de las 5.6 semanas; el empleador puede dar más. Arrastre de días y pago al salir no figuran en la página. https://www.gov.uk/holiday-entitlement-rights
- OIT C132: mínimo de "three working weeks" por un año de servicio; adoptado el 24/6/1970, en vigor desde el 30/6/1973. Lo dan fuentes secundarias en el buscador (copia en base jurídica de Sri Lanka y Wikipedia); no leí el texto. Período mínimo de servicio y pago: hueco. https://lankalaw.net/wp-content/uploads/2024/12/C132-Holidays-with-Pay-Convention-Revised-1970.pdf [S]
- Discrepancia de pisos: OIT 3 semanas (mínimo internacional) frente a RU 5.6 semanas.
- Modelo de saldos (software abierto): un tipo de licencia define reglas (saldo negativo, sin goce, máximo de días consecutivos, si cuentan feriados); una asignación (allocation) es el derecho del período; la solicitud tiene estado Abierto/Aprobado/Rechazado; al aprobar se descuenta en un libro mayor (ledger) y al cancelar se revierte. El saldo se muestra como total asignado, vencido, usado, pendiente de aprobación y disponible. https://docs.frappe.io/erpnext/user/manual/en/leave-application. Sostiene el patrón devengamiento = asignación periódica + ledger.
- Aprobación: ajustes sobre aprobador obligatorio, bloqueo de autoaprobación y solicitudes con fecha pasada. Mismo enlace.
- Efecto en la liquidación (días sin goce, saldo de vacaciones al egreso): sin fuente leída. Hueco; el único dato es que "sin goce" no requiere asignación en el modelo.

Posición contraria: vacaciones ilimitadas. Un estudio de Namely (2018) citado por el buscador halló que quienes tenían plan "unlimited" tomaban dos días menos al año; Kickstarter abandonó la política en 2015 porque la gente tomaba menos; contraejemplo: carinsurance.net distribuyó mejor el tiempo. Evidencia mayormente anecdótica y de encuestas, no revisada por pares. https://www.shrm.org/ResourcesAndTools/hr-topics/benefits/pages/4-lessons-about-unlimited-vacation.aspx [S]. Consecuencia de sistema: sin saldo no hay devengamiento ni pasivo, pero tampoco señal de que alguien no descansa (inferencia mía).

Recurso canónico: GOV.UK holiday entitlement para el cálculo (prorrateo, irregulares) y el doc de Leave Application de ERPNext para el modelo (tipo, asignación, solicitud, ledger, saldo). C132 como piso internacional, cuando se lea el texto.

---

## ¿Coincide el árbol con cómo divide el campo?

- Parcialmente. En software (ERPNext, Odoo) licencias y asistencia son de la misma familia: la licencia aprobada genera asistencia "On Leave" y el saldo se descuenta en un ledger. licencias-y-ausencias y registro-de-asistencia son vecinas fuertes; enlazarlas, y evaluar si "ausencias" (en asistencia) y "licencias" se duplican.
- Horas extra y banco de horas aparecen en la práctica dentro de la asistencia (Odoo: horas extra aprobadas canjeables por licencia), no solo en jornada. El recargo es de país.
- La vigencia (Fowler) es transversal a legajo, puesto-y-estructura y modalidades: conviene una sección o nota común, no repetirla.
- busquedas-y-postulantes como registro es razonable, pero esta ronda no halló respaldo; riesgo de quedar sin evidencia.

---

## Huecos (no encontrado o no leído)

- APQC PCF 7.0/payroll, SHRM BASK, CIPD, Dessler, Armstrong: no consultados (prioricé normas y guías oficiales dentro del límite de rondas).
- normlex.ilo.org devolvió 403 en C132 y R198: C001, C030, C095, C183 no leídos; C132 y R198 solo por copias y citas de segunda mano.
- GOV.UK employment records y personnel records: 404. Retención de legajos: una sola fuente (EE. UU., 29 CFR 516), sin segunda fuente independiente.
- ICO monitoring workers: PDF 403, solo resumen del buscador [S]. ICO sobre datos sensibles/salud y sobre postulantes, y EEOC recordkeeping: no consultados.
- Right to work: sin plazo de retención de copias (la guía es un PDF de 83 págs.).
- ERPNext HRMS Employee/Shift/Attendance y Odoo Employees/Time Off: Shift 404; Employee y Time Off no pedidos. Posición vs. persona, organigrama y vacante sin evidencia.
- Ingreso/egreso (alta, baja, certificados, devolución de bienes, cierre de accesos), modalidades (plazo fijo, eventual, prueba), consecuencias de la clasificación errónea, efecto de licencias en la liquidación: sin fuente.
- Vigilancia y vacaciones ilimitadas: solo fuentes secundarias; verificar los originales (Ravid et al. 2023, Namely 2018).
- Todo lo de ley y dinero (plazos, recargos, días) viene de un solo país por cada dato; marcar como ejemplo en las notas.
