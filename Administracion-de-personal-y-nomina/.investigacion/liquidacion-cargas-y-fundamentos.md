# Administración de personal y nómina: liquidación, cargas y fundamentos

Investigación del ángulo "dos verticales y los fundamentos" (liquidación de sueldos; cargas y declaraciones; fundamentos). Hecha el 2026-11-27. Todo lo traído de la web es dato. Contenido agnóstico: los ejemplos de país (Reino Unido, EE. UU.) van marcados como ejemplos.

Leyenda de marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U).

Límites de esta ronda (decirlos antes de usar el informe):
- El presupuesto de búsquedas web de la sesión se agotó a mitad de la investigación. Quedaron sin leer: APQC, SHRM BASK, Payroll.org CPP/FPC, CIPP, Dessler, Bieg y Toland, C102, C121, y los textos primarios de los informes de auditoría de Phoenix y Queensland Health.
- WebFetch resume con un modelo pequeño: las "citas literales" de abajo vienen de esos extractos (fragmentos de hasta 125 caracteres), no de lectura directa. Para el texto de leyes y cifras, antes de escribir la nota hay que reverificar contra el original.
- Cuando algo de ley o dinero tiene una sola fuente, está dicho.

---

## 0. Sobre el árbol propuesto

El árbol (ciclo; conceptos; recibo; retroactivos; liquidación final; pago | aportes; retención; libro | fundamentos) coincide en lo grueso con cómo lo divide la fuente más cercana a un corpus de práctica: el modelo de datos de un software abierto de nómina separa estructura salarial / componente / recibo / entrada de nómina (lote) / pago adicional (ver sección 6). Observaciones:

1. **Cierre y contabilización no tienen hogar propio.** El ciclo termina en "pago, contabilización e informes", pero lo contable ya está en otro tema; conviene que el ciclo lo mencione solo como frontera. La fuente de software abierto contabiliza en dos movimientos: devengamiento al confirmar los recibos y asiento de pago aparte (sección 6), lo que apoya la frontera.
2. **Embargos y adelantos** quedan en "el pago de sueldos" como sección. La OIT los trata como dos asuntos distintos: deducciones (Art. 8) y embargo/cesión (Art. 10) y privilegio en quiebra (Art. 11). Si el árbol los junta, que el texto distinga "descuento permitido" de "retención por orden de un tercero".
3. **"Retención de impuestos" y "aportes" comparten el mismo hecho generador** (el pago de sueldo) y los mismos organismos de reporte; en práctica del Reino Unido y EE. UU. se declaran en un solo informe. Conviene una nota que los una (el "informe periódico") en lugar de repetirlo en libro-de-sueldos y retención.
4. **Los marcos profesionales (APQC, SHRM, Payroll.org) no pude leerlos**, así que no puedo afirmar si dividen el dominio igual que el árbol. Es un hueco, no un hallazgo.

---

## A. Liquidación de sueldos

### A1. Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1 | OIT C095, Convenio sobre la protección del salario, 1949 (copia en Univ. de Minnesota; normlex.ilo.org dio 403) | https://hrlibrary.umn.edu/instree/ilo95.html | Primaria (norma), copia alojada por terceros | 3/3/1/3 | [L] vía extracto |
| 2 | GOV.UK, Running payroll | https://www.gov.uk/running-payroll | Primaria (guía oficial, ejemplo de país) | 3/2/2/2 | [L] vía extracto |
| 3 | GOV.UK, Pay your employees | https://www.gov.uk/running-payroll/pay-your-employees | Primaria (ejemplo de país) | 3/1/2/1 | [L] |
| 4 | GOV.UK, Payslips | https://www.gov.uk/payslips | Primaria (ejemplo de país) | 3/2/2/2 | [L] |
| 5 | Fowler, Temporal Patterns / Time Narrative | https://martinfowler.com/eaaDev/timeNarrative.html | Secundaria (autor de referencia en software) | 3/3/3/3 | [L] vía extracto |
| 6 | Frappe HR docs, Salary Structure | https://docs.frappe.io/hr/salary-structure | Primaria del producto (evidencia de modelado; la nota no debe nombrarlo) | 2/2/2/2 | [L] vía extracto |
| 7 | Frappe HR docs, Payroll Entry | https://docs.frappe.io/hr/payroll-entry | ídem | 2/2/2/2 | [L] vía extracto |
| 8 | Frappe HR docs, Additional Salary | https://docs.frappe.io/hr/additional-salary | ídem | 2/2/2/2 | [L] vía extracto |

No leí Odoo Payroll, ni Bieg y Toland, ni Dessler.

### A2. Afirmaciones

**Ciclo de liquidación**
- En el ejemplo de país del Reino Unido, en cada día de pago el empleador registra la paga, calcula impuesto y aportes, calcula el aporte patronal sobre ganancias por encima de £242 semanales, produce recibos e informa al fisco; el mes fiscal siguiente (que empieza el día 6) se ve lo adeudado desde el día 10, se envía el resumen mensual hasta el 19 si se reclaman reducciones y se paga hasta el 22 (19 si es por correo). https://www.gov.uk/running-payroll [extracto]
- La declaración de pagos y retenciones de cada día de pago se llama Full Payment Submission (FPS) y debe enviarse "on or before" el día de pago, aunque el pago al fisco sea trimestral; si cambian datos (alta, baja, cambio de código impositivo) hay que mandar un FPS corregido. https://www.gov.uk/running-payroll/reporting-to-hmrc (extracto de la página; no consta en la tabla por haberla abierto una sola vez)
- Si en un mes fiscal no se pagó a ningún empleado hay que enviar igualmente un Employer Payment Summary (EPS). https://www.gov.uk/running-payroll/pay-your-employees
- Frecuencia: la OIT dice "Wages shall be paid regularly" y que los intervalos los fija la ley, el convenio colectivo o laudo (Art. 12). https://hrlibrary.umn.edu/instree/ilo95.html La OIT no impone mensual, quincenal ni semanal; eso lo define cada país o convenio. En el Reino Unido el ejemplo muestra el período de pago como parámetro: "Select the Payroll Frequency" al crear un lote en el software abierto. https://docs.frappe.io/hr/payroll-entry
- Modelo de lote: una "entrada de nómina" procesa a muchos empleados a la vez, filtrable por sucursal, departamento o cargo, y genera un recibo por empleado sin duplicar los ya creados. https://docs.frappe.io/hr/payroll-entry ("If the Salary Slips are already created, the system will not create any more Salary Slips.")
- Fuera de ciclo: el software abierto lo resuelve con un "pago adicional" a un empleado, con una fecha de pago única o recurrente entre fechas, que se incorpora si la fecha cae dentro del período procesado. https://docs.frappe.io/hr/additional-salary El Reino Unido admite un pago extra con su propio FPS, que debe llegar antes del siguiente informe regular. https://www.gov.uk/running-payroll/reporting-to-hmrc

**Conceptos de liquidación**
- El modelo del software abierto separa Earnings y Deductions en tablas distintas; cada línea sale de un componente que puede tener monto fijo o "amount based on formula", con fórmula o condición en el componente o en la fila de la estructura. https://docs.frappe.io/hr/salary-structure
- La misma estructura puede ser "basada en hoja de horas" (pago por hora). https://docs.frappe.io/hr/salary-structure
- El pago adicional puede reemplazar el monto de un componente de la estructura ("Overwrite Salary Structure Amount"). https://docs.frappe.io/hr/additional-salary
- No encontré en esa documentación el orden de evaluación de componentes, el proporcional por días ni el bruto a neto inverso. Son hueco para la fuente de software; ver huecos.

**Recibo**
- OIT Art. 14: los trabajadores deben ser informados "in an appropriate and easily understandable manner", antes de ingresar y cuando haya cambios, de las condiciones salariales, y "at the time of each payment of wages, of the particulars of their wages for the pay period concerned, in so far as such particulars may be subject to change." https://hrlibrary.umn.edu/instree/ilo95.html
- Ejemplo de país (Reino Unido): el recibo debe mostrar ganancias antes y después de deducciones, las deducciones que cambian cada vez (impuesto, aportes) y las horas trabajadas si el pago depende de ellas; las deducciones fijas (por ejemplo, un préstamo) deben explicarse en el recibo o en una declaración aparte enviada antes del primer recibo y actualizada cada año. https://www.gov.uk/payslips
- "Employers can choose whether they provide printed or electronic (online) payslips"; debe darse en o antes del día de pago. No se exige a contratistas o freelancers. https://www.gov.uk/payslips
- Firma o conformidad: no encontré fuente agnóstica; la OIT no la exige en el Art. 14. Hueco.

**Retroactivos y reliquidaciones**
- Fowler abre su ejemplo con un sistema de nómina: "Imagine we have a payroll system that knows that en employee has a rate of $100/day starting on January 1", y muestra un cambio retroactivo. Distingue tiempo real (cuándo ocurrió) y tiempo de registro (cuándo lo supimos). https://martinfowler.com/eaaDev/timeNarrative.html
- Las correcciones no son ediciones: son entradas nuevas con nuevas fechas de registro; los cambios retroactivos sobre el tiempo de registro "break the integrity of the record". Dice que "no situation that requires a retroactive change that can't be handled by the actual-time dimension (unless fraud is one of your requirements)". https://martinfowler.com/eaaDev/timeNarrative.html
- Para explicar salidas pasadas (como facturas) sugiere que una traza detallada del cálculo puede sustituir al modelo bitemporal completo. https://martinfowler.com/eaaDev/timeNarrative.html
- Ejemplo de país: un FPS erróneo se corrige con un FPS corregido ("send a corrected FPS as soon as possible"). https://www.gov.uk/running-payroll/reporting-to-hmrc
- El software abierto trata los atrasos (arrears) como un tipo de pago adicional ("such as a bonus, allowance, arrears, or incentive"). https://docs.frappe.io/hr/additional-salary (leído solo en extracto; otros modelos podrían usar recibo complementario).

**Liquidación final**
- OIT Art. 12: "Upon the termination of a contract of employment, a final settlement of all wages due shall be effected within a reasonable period of time having regard to the terms of the contract." https://hrlibrary.umn.edu/instree/ilo95.html (fuente única en lo de plazo)
- Vacaciones no gozadas, proporcionales e indemnización como concepto: sin fuente agnóstica leída. El software abierto tiene "Leave Encashment Amount Per Day" en la estructura, para pagar licencias como un componente. https://docs.frappe.io/hr/salary-structure

**El pago de sueldos**
- Medio: "Wages payable in money shall be paid only in legal tender"; vales o cupones prohibidos; la autoridad puede permitir cheque bancario, postal o giro "in cases in which payment in this manner is customary or is necessary" (Art. 3). https://hrlibrary.umn.edu/instree/ilo95.html La OIT no menciona la transferencia electrónica; hueco para el medio moderno.
- Pago directo al trabajador salvo lo que disponga la ley o el acuerdo del trabajador (Art. 5); el empleador no puede limitar la libertad del trabajador de disponer de su salario (Art. 6); alcohol de alta graduación o drogas nocivas nunca como pago (Art. 4). https://hrlibrary.umn.edu/instree/ilo95.html
- Deducciones: "permitted only under conditions and to the extent prescribed by national laws or regulations or fixed by collective agreement or arbitration award" y se informa al trabajador (Art. 8). https://hrlibrary.umn.edu/instree/ilo95.html
- Embargos: "Wages may be attached or assigned only in a manner and within limits prescribed by national laws or regulations", y se protegen "to the extent deemed necessary for the maintenance of the worker and his family" (Art. 10). https://hrlibrary.umn.edu/instree/ilo95.html
- Quiebra: los trabajadores son "privileged creditors" y el salario privilegiado se paga en su totalidad antes que a los acreedores ordinarios; la prioridad relativa frente a otras deudas privilegiadas la determina la ley nacional (Art. 11). https://hrlibrary.umn.edu/instree/ilo95.html
- Pago en efectivo: solo en días laborables y en o cerca del lugar de trabajo (Art. 13). https://hrlibrary.umn.edu/instree/ilo95.html
- Registros: la ley debe prever "the maintenance, in all appropriate cases, of adequate records in an approved form and manner" (Art. 15). https://hrlibrary.umn.edu/instree/ilo95.html
- Contabilización en el software abierto: al confirmar los recibos se registra el devengamiento contra "Payroll Payable" y el pago se asienta aparte como un único asiento. https://docs.frappe.io/hr/payroll-entry
- Archivo al banco y adelantos: sin fuente leída. Hueco.
- Prioridad entre varios embargos: la OIT solo remite a la ley nacional. Sin fuente de ejemplo leída.

### A3. Recursos canónicos propuestos

- Ciclo: GOV.UK Running payroll (ejemplo de país, claro y corto) para el orden pago-informe; falta uno agnóstico (el Body of Knowledge de Payroll.org sería candidato, sin leer).
- Conceptos: la documentación de estructura salarial del software abierto como evidencia de modelado.
- Recibo: OIT C095 Art. 14 como norma; GOV.UK Payslips como ejemplo.
- Retroactivos: Fowler, Time Narrative.
- Pago: OIT C095 Arts. 3-13.
- Liquidación final: OIT C095 Art. 12.

---

## B. Cargas y declaraciones

### B1. Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 9 | IRS Publication 15 (Circular E), 2026, ejemplo de país | https://www.irs.gov/publications/p15 | Primaria (ejemplo de país) | 3/3/3/2 | [L] parcial: solo los primeros 100.000 de 357.528 caracteres |
| 10 | GOV.UK, Running payroll y Reporting to HMRC | https://www.gov.uk/running-payroll/reporting-to-hmrc | Primaria (ejemplo de país) | 3/2/2/2 | [L] vía extracto |
| 11 | OIT C095 (Art. 15, registros) | https://hrlibrary.umn.edu/instree/ilo95.html | Primaria | 3/1/1/2 | [L] |

No pude leer: C102 y C121 de la OIT (seguro de accidentes), la guía de retención del Reino Unido, la guía de registros del Reino Unido (la URL probada dio 404; la página de "Pay your employees" y la de "Running payroll" no dicen cuánto se guardan).

### B2. Afirmaciones

**Aportes y contribuciones (ejemplo EE. UU.)**
- El empleador retiene la parte del empleado de seguridad social y Medicare. Seguridad social: 6,2% cada uno (empleado y empleador), con base máxima 2026 de $184,500. Medicare: 1,45% cada uno, "no wage base limit". https://www.irs.gov/publications/p15 (dato de una sola fuente en esta ronda; para dinero habría que contrastar con la página del SSA)
- Los impuestos retenidos y la parte del empleado de FICA son "trust fund taxes"; si no se retienen o depositan puede aplicar la "trust fund recovery penalty". https://www.irs.gov/publications/p15
- Ejemplo Reino Unido: aporte patronal sobre ganancias por encima de £242 semanales. https://www.gov.uk/running-payroll
- Seguro de accidentes de trabajo y beneficios: sin fuente leída. Hueco.

**Retención de impuestos sobre sueldos**
- EE. UU.: "Withhold federal income tax from each wage payment" según el Form W-4 de cada empleado y las tablas de la Pub. 15-T; "Ask each new employee to complete the 2026 Form W-4". https://www.irs.gov/publications/p15
- Retención sobre pagos suplementarios (bonos): 22%, y 37% sobre lo que supere $1 millón en el año. https://www.irs.gov/publications/p15
- Ajuste anual: se concilia el Form 941 (trimestral) con los Forms W-2/W-3; se entrega a cada empleado un W-2 y se presenta la copia A a la administración. https://www.irs.gov/publications/p15 (fecha de vencimiento no leída por truncamiento)
- Reino Unido: el empleador calcula impuesto y aportes en cada pago y lo informa en el FPS; llama a esto sistema de información en tiempo real (la sigla RTI no apareció en los extractos leídos). https://www.gov.uk/running-payroll
- Deducciones declaradas por el empleado: en EE. UU., el W-4. En Reino Unido, código impositivo (se menciona en el FPS corregido por "cambia el código impositivo"). https://www.gov.uk/running-payroll/reporting-to-hmrc

**Libro de sueldos y declaraciones**
- Depósitos federales: calendario mensual o semisemanal según un período de referencia, por vía electrónica ("You must use EFT to make all federal tax deposits"). https://www.irs.gov/publications/p15
- Form 941 trimestral: vencimientos 30 abr., 31 jul., 31 oct., 31 ene. https://www.irs.gov/publications/p15
- Conservación de registros: "Keep all records of employment taxes for at least 4 years." https://www.irs.gov/publications/p15 (EE. UU.). Para Reino Unido no encontré plazo en las páginas leídas; hueco.
- Frecuencia de la declaración: en tiempo real por pago (Reino Unido, FPS), trimestral con conciliación anual (EE. UU.). Dos fuentes de ejemplo que difieren en la cadencia; no son contradictorias, son modelos distintos. https://www.gov.uk/running-payroll/reporting-to-hmrc y https://www.irs.gov/publications/p15
- Registros según la OIT: debe existir un registro adecuado "in an approved form and manner". https://hrlibrary.umn.edu/instree/ilo95.html
- Sanciones por tarde: "Missing or late FPSs can lead to a late filing notice and penalties" y pueden afectar beneficios de los empleados. https://www.gov.uk/running-payroll

### B3. Recursos canónicos propuestos

- Aportes y retención como ejemplo EE. UU.: IRS Publication 15.
- Ejemplo de declaración en tiempo real: GOV.UK, Reporting to HMRC / FPS.
- Registros: OIT C095 Art. 15 como principio; plazo concreto de ejemplo EE. UU. (4 años) en la Pub. 15.
- Aportes patronales y accidentes de trabajo: sin canónico todavía (C102/C121 de la OIT son los candidatos).

---

## C. Fundamentos

### C1. Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 12 | Wikipedia, LEO (computer) | https://en.wikipedia.org/wiki/LEO_(computer) | Secundaria | 1/2/2/1 | [L] vía extracto |
| 13 | Resultados del buscador sobre LEO (Warwick, BCS, THE, Register) | https://warwick.ac.uk/services/library/mrc/explorefurther/digital/leo/story/ (404 al abrirla) | Secundaria / archivo | 2/2/2/2 | [S] |
| 14 | Wikipedia, Phoenix pay system | https://en.wikipedia.org/wiki/Phoenix_pay_system | Secundaria (cita al OAG) | 1/2/2/1 | [L] vía extracto |
| 15 | Resultados del buscador, Phoenix: OAG Fall 2017 Report 1 "Phoenix Pay Problems" | https://www.publications.gc.ca/collections/collection_2017/bvg-oag/FA1-23-2017-2-1-eng.pdf (página de archivo; PDF no abierto) | Primaria | 3/3/3/3 | [S] (no pude leerlo) |
| 16 | OAG Spring 2018 Report 1, "Building and Implementing the Phoenix Pay System" | https://www.oag-bvg.gc.ca/internet/English/parl_oag_201805_01_e_43033.html (404 al abrirla) | Primaria | 3/3/3/3 | [S] |
| 17 | Wikipedia, 2010 Queensland Health payroll system implementation | https://en.wikipedia.org/wiki/2010_Queensland_Health_payroll_system_implementation | Secundaria | 1/2/2/1 | [L] vía extracto |
| 18 | Queensland Health Payroll System Commission of Inquiry, Report, 31 julio 2013 (papel tabulado 5413T2967) | https://documents.parliament.qld.gov.au/tableOffice/TabledPapers/2013/5413T2967.pdf (403 al abrirla) | Primaria | 3/3/3/3 | [S] |
| 19 | iTnews, "IBM should never have been appointed, finds Qld payroll inquiry" | https://www.itnews.com.au/news/ibm-should-never-have-been-appointed-finds-qld-payroll-inquiry-352362 | Secundaria (prensa especializada) | 2/2/2/1 | [S] |

APQC PCF 7.0 y 9.5, SHRM BASK, Payroll.org CPP/FPC y su Body of Knowledge, CIPP, ERP/HRIS/HCM (historia): no leídos. Dessler y Bieg y Toland: no leídos.

### C2. Afirmaciones

**Historia: LEO y la nómina**
- LEO I, de J. Lyons and Co.: la primera aplicación de negocios fue la valuación de la panadería ("Bakery Valuations"), que corrió con éxito el 5 de septiembre de 1951 y LEO tomó el cálculo completo el 29-30 de noviembre de 1951. https://en.wikipedia.org/wiki/LEO_(computer)
- Las fuentes **discrepan** sobre la fecha de la nómina en LEO: una dice que en noviembre de 1951 se usó por primera vez en nómina, con 40 recibos por minuto; otra, que la primera nómina computarizada fue en 1953; otra, que la nómina de 10.000 empleados pasó a LEO II en febrero de 1954. Todas vía resumen del buscador [S]; Wikipedia no da fecha de la nómina. https://en.wikipedia.org/wiki/LEO_(computer) y resultados de búsqueda arriba citados (warwick.ac.uk, theregister.com, bcs.org). No afirmar "1951 nómina" sin verificar en el archivo de Warwick. Sí es seguro: "En 1956 Lyons empezó a calcular nóminas para Ford UK y otros en LEO I", un caso temprano de tercerización. https://en.wikipedia.org/wiki/LEO_(computer)
- Por qué la nómina fue de las primeras tareas: no tengo fuente leída que lo diga; la explicación habitual (volumen, repetición, reglas fijas) es inferencia, no hallazgo.
- Historia de la planilla de jornales, ERP y HRIS/HCM: sin fuente leída. Hueco.

**Incidentes y errores documentados**
- Phoenix (Canadá). Según la página secundaria, la primera ola salió en febrero de 2016 (más de 34 departamentos, cerca de 120.000 empleados) y la segunda el 21 de abril de 2016; el presupuesto original de 2009 era de $309 millones; en noviembre de 2017 el costo estimado de arreglarlo era de $540 millones. https://en.wikipedia.org/wiki/Phoenix_pay_system (secundaria, cifras sin verificar contra el OAG)
- Qué dijo el auditor: la página secundaria cita al OAG de mayo de 2018 llamándolo "an incomprehensible failure of project management and oversight", dice que se canceló un piloto de junio de 2015 en un solo departamento, y que en septiembre de 2017 se habían analizado "6 of the 200 custom programs". https://en.wikipedia.org/wiki/Phoenix_pay_system (secundaria: reverificar en el informe del OAG)
- Resumen del buscador sobre el informe de otoño de 2017: tabulado el 21 de noviembre de 2017; trabajo terminado el 25 de septiembre de 2017; migración desde 2009 de unos 290.000 empleados; 494.500 solicitudes de pago pendientes en junio de 2017; errores de $520 millones en sobrepagos o subpagos (el seguimiento de 2018), y $615 millones según una nota de prensa atribuida al auditor. Las dos cifras **discrepan** ($520 millones y $615 millones); no está resuelto cuál corresponde a qué fecha. https://www.publications.gc.ca/collections/collection_2017/bvg-oag/FA1-23-2017-2-1-eng.pdf [S]
- El mismo resultado atribuye el volumen de errores en parte a la complejidad de procesar nóminas con reglas distintas, y la página secundaria agrega que unos 200 programas a medida. https://en.wikipedia.org/wiki/Phoenix_pay_system
- Queensland Health. Puesta en marcha el 14 de marzo de 2010; cerca de 78.000 empleados pagados mal o no pagados; contrato original de $98 millones (IBM, diciembre de 2007); costo de $181 millones al fin del proyecto y unos $1.200 millones estimados para repararlo y operarlo ocho años. https://en.wikipedia.org/wiki/2010_Queensland_Health_payroll_system_implementation (secundaria)
- La Comisión (Richard Chesterman) le da "a place in the front rank of failures in public administration in this country". https://en.wikipedia.org/wiki/2010_Queensland_Health_payroll_system_implementation Informe fechado 31 de julio de 2013, 36 días de audiencias y 60 testigos (resumen del buscador). https://documents.parliament.qld.gov.au/tableOffice/TabledPapers/2013/5413T2967.pdf [S]
- Pruebas de aceptación: más de 2.000 defectos, unos 14 críticos; el lanzamiento siguió con problemas conocidos después de postergarse más de diez veces. https://en.wikipedia.org/wiki/2010_Queensland_Health_payroll_system_implementation
- Cifras de costo **discrepan** según la fuente: precio original citado como $98 millones (Wikipedia) o 6,194 millones (resumen de búsqueda con la cita del premier, de un resultado de prensa); el total "cerca de $1.200 millones" y "$1.250 millones" (KPMG) también difieren de los $181 millones al cierre del proyecto. Se miden bases distintas (costo del proyecto contra costo de recuperación). Reverificar contra el informe y la auditoría general.
- Posiciones contrarias y mitos (la nómina es "simple"): ambas catástrofes se asocian a reglas especiales de pago muy numerosas y a pruebas insuficientes (puntos de arriba); los textos primarios no los leí. Para "errores de nómina y su costo" en empresas privadas: sin fuente. Hueco.

**Marcos que dividen el dominio**
- APQC PCF 7.0 y 9.5, SHRM BASK, Payroll.org CPP y su Body of Knowledge, CIPP: no leídos. Sin afirmaciones.

**Dónde se produce el saber confiable**
- Normas internacionales (OIT) para los principios; organismos fiscales (GOV.UK, IRS) para la práctica de país; informes de auditoría pública (OAG, comisiones) para fallas documentadas; software abierto para modelado. Esta clasificación es mía, apoyada en lo leído arriba. Sin fuente de cuerpo profesional leída.

### C3. Recursos canónicos propuestos

- Historia: archivo LEO Computers Society / Warwick (a localizar; el enlace probado dio 404).
- Fallas: informes del OAG de Canadá (otoño de 2017, primavera de 2018) y el informe de la Comisión de Queensland (2013), leídos de primera mano antes de citar cifras.
- Marcos: Payroll.org Body of Knowledge y APQC PCF, pendientes.

---

## Huecos (qué no se encontró)

1. **Textos primarios de auditoría**: Phoenix (OAG 2017 y 2018) y Queensland (Comisión 2013) no se abrieron (404, 403, redirección). Todas las cifras de la sección C son secundarias o de buscador; deben verificarse. Hay discrepancias abiertas: $520 millones frente a $615 millones de errores en Phoenix; costos de Queensland según la base.
2. **Marcos profesionales**: APQC 7.0 y 9.5, SHRM BASK, Payroll.org (CPP/FPC y Body of Knowledge), CIPP. No sé cómo dividen el dominio.
3. **Fecha de la primera nómina en LEO**: 1951, 1953 y 1954 según las fuentes; sin primaria leída.
4. **Historia de la planilla de jornales, ERP, HRIS/HCM** y por qué la nómina se automatizó pronto: sin fuente.
5. **Conceptos**: orden de cálculo de componentes que dependen de otros, proporcional por días, bruto a neto inverso (grossing up), remunerativo frente a no remunerativo como idea general (qué entra en la base de cargas). Ninguna fuente leída los cubre; la documentación del software abierto leída no los describe (probar la página Salary Component de Frappe y Odoo Payroll).
6. **Recibo**: firma o conformidad no tienen fuente.
7. **Liquidación final**: vacaciones no gozadas e indemnización como concepto; solo el plazo de la OIT.
8. **Pago**: archivo al banco, adelantos y préstamos, prioridad entre varios embargos. La OIT remite a la ley nacional. Sin ejemplo de país leído.
9. **Cargas**: seguro de accidentes de trabajo y beneficios (C102/C121 no abiertos). Topes y bases: solo el ejemplo EE. UU. (una fuente; falta contraste para dinero).
10. **Retención**: PAYE y el ajuste anual del Reino Unido (no abrí la guía específica); fecha de vencimiento del W-2 no leída (truncamiento de la Pub. 15).
11. **Libro de sueldos**: plazo de conservación en Reino Unido no encontrado (la URL guess dio 404). Contenido obligatorio de los registros: solo la mención genérica de la OIT.
12. **Odoo Payroll** y los libros (Dessler, Bieg y Toland): no leídos.
13. Normlex (normlex.ilo.org) devolvió 403; la copia de la OIT es de la Univ. de Minnesota. Confirmar en la fuente oficial.
14. Ley y dinero con una sola fuente leída: las cifras de IRS Pub. 15 (tasas, topes, 4 años) y el texto del C095 (una sola copia). No hay segunda fuente independiente en esta ronda.
