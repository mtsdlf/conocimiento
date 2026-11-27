---
resumen: >-
  El registro de horas es el trabajo hecho, imputado a un proyecto: cada hora imputada dice quién trabajó, en qué proyecto y tarea, qué día, cuánto tiempo y si se cobra. Una vez aprobada se trata como un movimiento: no se edita, se revierte y se vuelve a cargar.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework cross-industry (copia de 2024 en texto), 5.3.3.2, 7.7.6 «Develop and manage time and attendance systems», 9.2.2.2 «Generate customer billing data», 9.5.1.5 «Analyze and report employee utilization» y 9.5.2.1 «Enter employee time worked into payroll system»"
  - "ERPNext, Timesheet (según resumen): https://docs.frappe.io/erpnext/user/manual/en/timesheet"
  - "Odoo 19, Timesheets (según resumen): https://www.odoo.com/documentation/19.0/applications/services/timesheets.html"
  - "Microsoft Learn, Project Operations, Time entry overview (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/time/time-entry-overview"
  - "Microsoft Learn, Project Operations, Recall and cancel approvals (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/approvals/recall-cancel"
  - "U.S. Department of Labor, Fact Sheet #21: Recordkeeping Requirements under the FLSA (según resumen): https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping"
  - "WilmerHale (2010), Slice of History: Reginald Heber Smith and the Birth of the Billable Hour (según resumen): https://www.wilmerhale.com/en/insights/publications/slice-of-history-reginald-heber-smith-and-the-birth-of-the-billable-hour-august-9-2010"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md (secciones 2.1 y 2.2)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 3)"
aliases: [registro de horas, carga de horas, time tracking, timekeeping, hora imputada, time entry, horas imputadas, parte de horas, imputación de horas]
creado: 2026-11-27
revisado:
---

# Registro de horas

El registro de horas es el trabajo hecho, imputado a un proyecto: cada hora imputada dice quién trabajó, en qué proyecto y tarea, qué día, cuánto tiempo y si se cobra. Una vez aprobada se trata como un movimiento: no se edita, se revierte y se vuelve a cargar.

Dentro de [Servicios profesionales y proyectos](../servicios-profesionales-y-proyectos.md) es la vertical que convierte el tiempo de las personas en un dato. Recibe de la [asignación de personas](../Asignacion-de-personas/asignacion-de-personas.md) el equipo de cada proyecto. Le da a la [facturación del proyecto](../Facturacion-del-proyecto/facturacion-del-proyecto.md) las horas y los gastos aprobados, y a la [rentabilidad de la firma](../Rentabilidad-de-la-firma/rentabilidad-de-la-firma.md) el costo del trabajo y la base de la [utilización](../Rentabilidad-de-la-firma/utilizacion.md).

## Una hora, tres usos

La misma hora imputada sirve para facturar, para costear y para medir. Uno de los sistemas abiertos leídos lo dice en la definición de su hoja de horas: «A Timesheet records the hours an employee spends on tasks. It can support billing, payroll, and tracking an employee's contribution to a Project or Task». En un proyecto por [tiempo y materiales](../Facturacion-del-proyecto/facturacion-por-hora.md) la hora aprobada se vuelve una línea de factura. En uno a precio cerrado no se factura, pero es el costo con que se calcula el [margen del proyecto](../Rentabilidad-de-la-firma/costo-y-margen-del-proyecto.md). En los dos, es el numerador de la utilización.

Por eso cada hora lleva dos valores separados: el costo de la hora y la tarifa con que se cobra. Ese sistema los guarda como campos distintos, uno «the actual cost of work done» y otro «the rate at which the customer needs to be billed», y cada uno se multiplica por las horas. Cómo se calcula el costo de la hora es de [costo y margen del proyecto](../Rentabilidad-de-la-firma/costo-y-margen-del-proyecto.md).

La hoja de horas nació así, como herramienta interna. Según la historia que publica el estudio donde se inventó, Reginald Heber Smith la creó hacia 1920 para planificar y presupuestar el estudio, y recién antes de 1940 empezó a usarse para facturar. La historia y la crítica a la hora como unidad de precio están en [Fundamentos](../Fundamentos/fundamentos-de-servicios-profesionales.md).

## La hora imputada no es la asistencia

Cuántas horas trabajó una persona, para pagarle, y a qué proyecto se imputan esas horas, para cobrarlas o costearlas, son dos registros distintos. APQC los pone en lugares distintos: la asistencia en recursos humanos (7.7.6 «Develop and manage time and attendance systems») y en la liquidación (9.5.2.1 «Enter employee time worked into payroll system»). La hora imputada a un proyecto no tiene un proceso propio en el marco; aparece de costado, como dato para facturar (9.2.2.2 «Generate customer billing data») y para medir la utilización (9.5.1.5).

La asistencia tiene obligaciones legales propias. En los Estados Unidos, por ejemplo, el empleador registra de cada trabajador no exento las horas de cada día y el total de cada semana, según el resumen de la hoja del regulador; la norma no habla de proyectos. Lo de la Argentina, y la asistencia como registro, son del tema Administración de personal y nómina, que todavía no está escrito.

Como criterio de esta base, los dos registros se pueden cargar en un solo paso (la persona carga sus horas por proyecto y el total del día sale de la suma), pero no se confunden: una persona puede trabajar ocho horas y que solo cinco vayan a proyectos de clientes, y una hora de proyecto corregida después de facturada no cambia lo que se le pagó.

## La hora como movimiento

Una hora aprobada se comporta como un [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md#un-error-se-corrige-con-otro-movimiento): no se edita ni se borra, y un error se corrige con otro movimiento que lo compensa. Un sistema de gestión de servicios lo hace literalmente. Al retirar la aprobación de una hora, marca el costo y la venta originales como ajustados y crea asientos de reversa que copian todo salvo la cantidad, que se invierte. Después la persona corrige y vuelve a enviar, y la aprobación genera los valores nuevos.

Lo que cambia con el estado es cuánto cuesta corregir. En borrador, la persona edita o borra. Enviada, la retira. Aprobada, se revierte. Facturada, no se puede retirar sin una factura correctiva que acredite la original entera. El detalle está en [hoja de horas](hoja-de-horas.md).

En la contabilidad, el proyecto es una dimensión de cada movimiento de costo e ingreso, como explica [centros de costo](../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md#por-qué-los-centros-de-costo-van-en-dimensiones-y-no-en-el-plan-de-cuentas); acumular el costo por proyecto es el costeo por órdenes de [sistemas de costeo](../../Contabilidad/Contabilidad-de-gestion/sistemas-de-costeo.md#por-órdenes-o-por-procesos-qué-se-acumula).

## Quién decide si una hora se cobra

Los sistemas leídos ponen la decisión en lugares distintos, y es una decisión de diseño:

| Dónde vive «facturable» | Cómo funciona |
|---|---|
| En cada línea de la hoja | Quien carga marca si la hora se cobra |
| En el proyecto y su línea de venta | Solo se cobra si el proyecto es facturable y la hora cuelga de una línea del pedido de venta |
| En la aprobación | Quien aprueba puede cambiar la cantidad facturable y el tipo (cobrable, no cobrable, de cortesía) |

Como criterio de esta base, el modelo de cobro del [proyecto del cliente](../Proyecto-del-cliente/proyecto-del-cliente.md) da el valor por defecto y la aprobación lo puede corregir; dejarlo solo en manos de quien carga mezcla el registro con la decisión comercial.

## Qué hay en el registro de horas

- [Hoja de horas](hoja-de-horas.md): qué datos lleva cada línea, el período, los estados, quién aprueba y cómo se corrige una hora aprobada o facturada.
- [Gastos del proyecto](gastos-del-proyecto.md): viajes, materiales y otros gastos imputados a un proyecto, y cómo se trasladan al cliente: a costo, con recargo o por tarifa.
- [Calidad del registro](calidad-del-registro.md): por qué la hora cargada se aleja de la trabajada, qué se puede razonar y lo que falta medir.
