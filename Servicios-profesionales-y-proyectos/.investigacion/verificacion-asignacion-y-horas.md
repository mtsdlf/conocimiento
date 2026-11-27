# Verificación con fuentes: asignación de personas y registro de horas

Ángulo `asignacion-y-horas`. Notas: `Asignacion-de-personas/` (4) y `Registro-de-horas/` (4). Fecha de la pasada: 2026-11-27.

Método y límites. La búsqueda web (WebSearch) agotó su presupuesto en la sesión y no se pudo usar. Se leyó por URL directa: texto oficial de la FAR en acquisition.gov (HTML bajado completo y limpiado), 29 CFR 516.2 y 2 CFR 200.430 en la e-CFR de Cornell LII, el sitio de SFIA, páginas del autor Maister, la historia de WilmerHale, la documentación de Odoo y ERPNext (HTML completo), y el PDF de Jacobs (1998) del BLS (bajado y pasado a texto). Para artículos de revistas, la API de metadatos Crossref (solo resúmenes, marca [A]). Marcas: [L] texto leído entero o la parte citada; [A] solo el resumen que publica el editor; [S] resumen de un modelo; [F] no se pudo abrir.

Cerrados por acceso (no cuentan como fuente): ABA Formal Opinion 93-379 y Regla 1.5 (403 de Cloudflare, tres URL del sitio de la ABA); SSRN (403); ScienceDirect (403); OpenTextBC (403); BLS en HTML (403, sí abrió el PDF por WebFetch); PMBOK (de pago); Ross, *The Honest Hour* (libro); Lerman, trabajos sobre facturación (no se encontró una versión abierta).

## Casos resueltos

### 1. FAR 52.232-7, leída entera [L]
URL: https://www.acquisition.gov/far/52.232-7 (cláusula de nov. 2021).
- (a)(5): comprobantes «not more than once every two weeks»; se respaldan con prueba de pago real y «(i) Individual daily job timekeeping records; (ii) Records that verify the employees meet the qualifications for the labor categories specified in the contract; or (iii) Other substantiation approved by the Contracting Officer».
- (a)(4): la tarifa horaria incluye «wages, indirect costs, general and administrative expense, and profit».
- (b)(1)(ii): «Materials» incluye materiales directos, subcontratos de insumos y servicios incidentales sin categoría laboral, «Other direct costs (e.g., ..., travel, computer usage charges, etc.)» y «Applicable indirect costs». (b)(5): el contratista puede incluir costos indirectos y otros costos directos asignables si son solo costos claramente excluidos de la tarifa horaria, se asignan según sus prácticas contables y «Indirect costs are not applied to subcontracts that are paid at the hourly rates». (b)(7): «the Government will not pay profit or fee to the prime Contractor on materials» salvo 31.205-26(e) y (f). (b)(3): se reembolsan los materiales pagados o que el contratista suele pagar dentro de 30 días.
- Corrección en `hoja-de-horas` y `calidad-del-registro`: la nota decía que «cada factura se respalda con Individual daily job timekeeping records»; es una de tres alternativas. Corregido, y se sacó «según resumen».
- Agregado en `gastos-del-proyecto`: «materiales» incluye viajes y otros costos directos; sin ganancia pero con costos indirectos asignables; no se aplican indirectos a subcontratos pagados por hora.

### 2. FAR 31.205-26, leída entera [L]
URL: https://www.acquisition.gov/far/31.205-26 (FAC 2026-01, vigente 2026-03-13).
(b): ajustar el costo de los materiales por «trade discounts, refunds, rebates, allowances, and cash discounts, and credits for scrap, salvage, and material returned to vendors»; no hay que acreditar descuentos por pago al contado perdidos si no tomarlos fue razonable. (e) y (f) son las excepciones (transferencias entre divisiones bajo control común, productos comerciales a precio de catálogo). La nota decía que restar los descuentos era lo que decía el resumen: confirmado. Se aclaró qué son (e) y (f).

### 3. FAR 31.201-2, leída entera [L]
URL: https://www.acquisition.gov/far/31.201-2. (a): razonable, imputable, estándares CAS o PCGA, términos del contrato, límites de la subparte; (d): registros «adequate to demonstrate that costs claimed have been incurred, are allocable to the contract, and comply with applicable cost principles», y el funcionario «may disallow all or part of a claimed cost that is inadequately supported». La nota estaba bien; se citó el texto y se sacó «según resumen».

### 4. ABA Formal Opinion 93-379 [F]
Tres URL del sitio de la ABA devolvieron 403 (desafío de Cloudflare); la Regla 1.5 también. No se usaron espejos de terceros. Sigue sin fuente de ética profesional sobre gastos al cliente. La nota `gastos-del-proyecto` lo dice y deja el bloque de «es plata, una sola fuente».

### 5. Asistencia frente a hora imputada [L], dos fuentes independientes
- 29 CFR 516.2(a)(7) (https://www.law.cornell.edu/cfr/text/29/516.2): el empleador debe conservar, de cada empleado cubierto, «Hours worked each workday and total hours worked each workweek». 516.2(c): con horario fijo puede registrar el horario y marcar que se cumplió, y anotar horas exactas solo en las semanas distintas. 516.6: conservar al menos 2 años.
- 2 CFR 200.430(g)(1)(iii) y (vi) (https://www.law.cornell.edu/cfr/text/2/200.430): los registros deben «reasonably reflect the total activity for which the employee is compensated» y «support the distribution of the employee's salary or wages among specific activities or cost objectives»; (g)(3): para no exentos, además, registros del total de horas trabajadas cada día. (g)(1)(i): control interno; (g)(1)(vii): estimaciones previas solo para registro provisional, con revisiones posteriores y «all necessary adjustments».
- Cambio en `registro-de-horas`: se reemplazó la hoja del Departamento de Trabajo (403, según resumen) por el texto del reglamento y se agregó la norma de imputación a proyectos. Las dos son de EE. UU., y la nota lo dice.

### 6. WilmerHale, historia de la hora facturable [L]
URL de la nota. Confirmados: «a form on which you wrote the name of the client, the name of the case»; décima de hora por «add, subtract, and divide on the decimal system»; «they hate any system»; «Initially, the timesheet remained a purely internal metric, used for organizational planning and budgeting»; el tiempo entre «inception around 1920» y «1940» en que se convirtió en hora facturable. La página dice que la ABA publicó el libro de Smith en 1940. Se sacó «según resumen».

### 7. Odoo 19 Planning y Timesheets, ERPNext Timesheet y Activity Type [L], como evidencia de práctica
- Odoo Planning: turnos en borrador («Diagonal stripes: shifts that are planned but have yet to be published»), el empleado solo se entera al publicar; turnos abiertos (sin recurso) solo se asignan a quien tiene el rol. Confirmado.
- Odoo Timesheets: permiso «validate all employees' timesheets»; grilla con vista por semana, día o mes. Confirmado.
- ERPNext Timesheet: «Once a Timesheet is saved and submitted, the details like Billing Rate and Costing rate get locked»; «the actual cost of work done»; «The rate at which the customer needs to be billed». Corrección: la nota `registro-de-horas` citaba entre comillas «A Timesheet records the hours an employee spends on tasks. It can support billing, payroll, and tracking an employee's contribution to a Project or Task», que no está en la página (era una paráfrasis del resumen). El texto literal es «The Timesheet can also be used to calculate the billable towards an employee, to calculate their salaries, or to track an employee's contribution towards a Project or a Task». Corregido.
- Se sacó «según resumen» de las cuatro citas.

### 8. SFIA 9 [L]
URLs: https://sfia-online.org/en/sfia-9/responsibilities, .../skills/resourcing, .../skills/workforce-planning.
- Siete niveles de responsabilidad, iguales para todas las habilidades: 1 Follow, 2 Assist, 3 Apply, 4 Enable, 5 Ensure/advise, 6 Initiate/influence, 7 Set strategy/inspire/mobilise, cada uno con un «Essence of the level» genérico. El sitio dice que los niveles se pueden usar fuera de TI («Its universal applicability allows it to be extended into various knowledge-intensive or technical professions»).
- Cada habilidad se define en un subconjunto de niveles: Resourcing 2 a 6; Workforce planning 4 a 6.
- Workforce planning, notas de guía: «more strategic than tactical resource allocation to projects»; analiza datos «over extended time periods to discover multi-year trends»; planes para cerrar brechas con «external recruitment, internal development, re-skilling, sourcing external partners, organisational design or outplacement».
- Cambios: párrafo nuevo en `roles-y-habilidades` (escala con niveles; sigue abierto quién fija el nivel); párrafo en `demanda-y-capacidad` sobre contratar y subcontratar como salidas de un plan de dotación. No resuelve «cuándo conviene cada una» ni «cuánto banco».

### 9. Maister, «The Anatomy of a Consulting Firm» (2004) [L]
URL: https://davidmaister.com/articles/4/2/index.html. Capítulo 2 de *The Advice Business* (Pearson, 2004), adaptado de *Managing the Professional Service Firm* (1997) y *True Professionalism* (1993). La sección «Leverage Structure» calcula la dotación por nivel a partir de un proyecto típico (0,5 socio, 1 medio, 3 junior) y utilizaciones objetivo de 75 % (socios y medios) y 90 % (junior): 4 socios dan 6 proyectos, 8 medios, 20 junior; proporción 1:2:5. Dice que si el trabajo exige más junior que los que hay, «higher-priced people will end up performing lower-value tasks» y hay subutilización de seniors; si exige más seniors, falta gente calificada y riesgo de calidad. Agregado en `demanda-y-capacidad` ("De los proyectos a las personas por nivel") y en `roles-y-habilidades` (respaldo parcial al planificar por rol). Es un ejemplo numérico del autor, no una medición. El libro entero no se leyó. No dice nada de reserva tentativa y firme, de banco medido ni del horizonte del pronóstico.

### 10. Calidad del registro: estudios con método
- Reffett (2011), experimento [A]: https://doi.org/10.2139/ssrn.1873250. Con incentivo a declarar de menos, los errores de declaración fueron menores, pero sesgados a la baja «when they reported time one-week after task completion, but not when they reported time immediately after task completion».
- Margheim y Pany (1986), casos con auditores [A]: https://doi.org/10.2308/ajpt-4691861. Efectos del tamaño del estudio y de la necesidad percibida del paso; efectos limitados de la presión de tiempo y de la materialidad del exceso sobre el presupuesto; sin efecto de las normas de control de calidad.
- Parker y Ruschena (2011), encuesta a abogados de 25 estudios de Queensland [A]: https://doi.org/10.2139/ssrn.1790082. La presión de las horas facturables es «the "face" of more fundamental pressures»: pesan las percepciones de lo que hace «todo el mundo» y de que no hay otro camino.
- te Braak, van Tienoven, Minnen, Glorieux (2022), 8.535 docentes belgas, diarios de tiempo en línea [A]: https://doi.org/10.1177/00811750221126499. La calidad cae con la demora de recuerdo, que ya empieza «several hours after an activity has been completed».
- Jacobs (1998), Monthly Labor Review [L]: https://www.bls.gov/opub/mlr/1998/12/art3full.pdf. 3.059 trabajadores (Workforce Survey 1992), horas autoinformadas frente a calculadas con salida y regreso: r = 0,61, que sube a 0,77 al corregir errores de codificación (161 casos, 5,2 %). Media autoinformada 42,2 y calculada 44,8 (la calculada incluye almuerzo y pausas). La aparente exageración de quienes declaran 60 horas o más es en buena parte regresión a la media; los factores psicológicos probados casi no explican la diferencia (el texto dice que ninguna ecuación llega al 1 % de la varianza). Cita a Rodgers y otros (r = 0,614 entre horas de la semana pasada y registros de la empresa, 0,719 con horas anuales, sin exageración) y a Robinson y Bostrom (que sí ven exageración en quienes dicen 50 horas o más, comparando con diarios). Es disputa, y es sobre horas semanales de encuestas, no sobre hojas de horas de proyectos.
- Otros resultados de Crossref sin abstract o sin relevancia directa (no usados): Shapeero y Killough (1993), «Underreporting of Billable Hours by Entry-level Professionals» (sin resumen); Soobaroyen y Chengabroyan (2006, auditores de Mauritania); Evans, Kunda y Barley (2004).
- Cambios en `calidad-del-registro`: resumen y primera línea cambiados de «No hay fuente con método que la mida» a que hay pocos estudios y ninguno da cifra general; secciones «El incentivo mueve el dato» y «Cargar a diario o al final de la semana» reescritas con estas fuentes; se sacaron las citas a la página de Wikipedia de Billable hours; Goodhart queda como referencia secundaria con la nota de que no se leyó a Strathern. El bloque «Sin fuente todavía» queda, precisado (sin cifras de pérdida o inflado en firmas de servicios; sin comparación diario/semanal en hojas de horas; sin evidencia del registro automático). No se inventó ninguna cifra.
- No resuelto: Lerman («Blue-Chip Bilking», 1999; «Lying to Clients», 1990 es sobre franqueza con el cliente y no se usó) y Ross, *The Honest Hour*: sin acceso al texto.

### 11. Nesheim (2021), rol del responsable de recursos [A]
https://doi.org/10.1108/ijmpb-12-2020-0389. Estudio de caso con 12 entrevistas en un departamento de proyectos de una industria con estructura de matriz: el responsable de recursos es «a specific type of line manager, complementing a task (project) manager»; tareas de asignar recursos, desarrollar competencias y evaluar el desempeño; el desafío principal es la relación con el jefe de proyecto. Agregado en `asignacion-de-personas` y `reserva-de-personas`. No dice quién arbitra un choque entre proyectos ni con qué criterio.

## Casos que siguen abiertos

- Reserva tentativa y firme: una sola fuente (documentación de un sistema). Odoo usa borrador y publicado, no tentativa y firme. No apareció una fuente de literatura o guía. Marcado en `reserva-de-personas`.
- Quién arbitra un conflicto entre proyectos y con qué criterio: no resuelto. La guía del PMI (de pago) y Engwall y Jerbrant (2003, ScienceDirect 403, Crossref sin resumen) no se pudieron leer. Marcado en `asignacion-de-personas` y `reserva-de-personas`.
- Banco (*bench*), cuándo contratar o subcontratar, horizonte del pronóstico en firmas de servicios: SFIA y Maister aportan el marco (salidas y mezcla de niveles), no el criterio ni cifras. Marcado en `demanda-y-capacidad`.
- Rol genérico frente a persona con nombre: apoyo parcial (Maister planifica por nivel); el método de «pedir genérico y bajar a persona» sigue siendo de un sistema.
- Quién fija el nivel de habilidad de una persona: sin fuente. Marcado.
- Cierre del período de la hoja de horas: las normas leídas (29 CFR 516.2, 2 CFR 200.430, FAR 52.232-7) hablan de la semana de trabajo y del comprobante quincenal, no de una fecha de cierre de carga. Marcado.
- Aprobación y corrección después de aprobar o facturar: segunda fuente solo parcial (2 CFR 200.430(g): control interno y ajustes posteriores), que no dice cómo ni quién aprueba. El esquema de reversa y factura correctiva sigue siendo de un sistema.
- Gastos reembolsables en firmas privadas, recargo: ABA 93-379 no abrió. Alto riesgo (dinero) mantenido con aviso.

## Cosas vistas en otras notas (no tocadas)

- `Fundamentos/fundamentos-de-servicios-profesionales.md` repite datos de la hoja de horas; conviene revisar que diga «a purely internal metric» y las fechas como las de WilmerHale y que no cite el resumen de Wikipedia de Billable hours.
- Cualquier nota que cite la FAR 52.232-7 como «cada factura se respalda con registros diarios» tiene el mismo error de las dos corregidas acá.
