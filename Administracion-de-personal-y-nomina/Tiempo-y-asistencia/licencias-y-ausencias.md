---
resumen: >-
  Una licencia es una ausencia autorizada, con o sin goce de sueldo, que el empleado pide y alguien aprueba. Las vacaciones son la licencia que se gana con el tiempo trabajado. Cada tipo de licencia tiene sus reglas, un saldo que se asigna por período y se descuenta al aprobar, y un efecto en la liquidación.
estado: borrador
estabilidad: semi
fuentes:
  - "ERPNext, Leave Application (documentación de producto, como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/leave-application"
  - "GOV.UK, Holiday entitlement: https://www.gov.uk/holiday-entitlement-rights"
  - "OIT, Convenio 132 sobre las vacaciones pagadas (revisado), 1970, arts. 3, 8 y 9, copia de terceros de la ficha de NORMLEX: https://lankalaw.net/wp-content/uploads/2024/12/C132-Holidays-with-Pay-Convention-Revised-1970.pdf"
  - "SHRM, 4 lessons about unlimited vacation, Joanne Sammer, 6 de enero de 2020: https://www.shrm.org/ResourcesAndTools/hr-topics/benefits/pages/4-lessons-about-unlimited-vacation.aspx"
  - "Knowledge at Wharton, Unlimited vacation time sounds great, 7 de marzo de 2017: https://knowledge.wharton.upenn.edu/article/unlimited-vacation-time-sounds-great-policies-deliver/"
  - "Administracion-de-personal-y-nomina/.investigacion/legajo-y-tiempo.md (2026-11-27)"
aliases: [licencia, licencias, ausencias, vacaciones, licencia paga, licencia sin goce, saldo de vacaciones, devengamiento de vacaciones, leave, time off, absence management, paid time off, PTO, annual leave, leave balance, leave accrual, vacaciones ilimitadas, unlimited PTO]
creado: 2026-11-27
revisado:
---

# Licencias y ausencias

Una licencia es una ausencia autorizada, con o sin goce de sueldo, que el empleado pide y alguien aprueba. Las vacaciones son la licencia que se gana con el tiempo trabajado. Cada tipo de licencia tiene sus reglas, un saldo que se asigna por período y se descuenta al aprobar, y un efecto en la liquidación.

Dentro de [tiempo y asistencia](tiempo-y-asistencia.md), la licencia es la ausencia que se sabe de antemano o que se justifica después. La que nadie autorizó aparece como falta en el [registro de asistencia](registro-de-asistencia.md). Los dos registros se cruzan: al aprobar una licencia, un sistema abierto crea un registro de asistencia con estado «en licencia» por cada día, y ese día deja de contar como falta.

## Tipo, asignación, solicitud y saldo

Un sistema abierto de gestión modela cualquier licencia con cuatro piezas:

1. **El tipo de licencia** define las reglas: si admite saldo negativo, si es sin goce, el máximo de días consecutivos y si los feriados dentro del período cuentan.
2. **La asignación** es el derecho del período: tantos días de vacaciones para este año. Una licencia sin goce no necesita asignación.
3. **La solicitud** es el pedido de unos días concretos, con estado abierto, aprobado o rechazado.
4. **El saldo** se lleva en un libro de movimientos: al aprobar, se descuenta; al cancelar, se revierte.

El saldo se muestra desagregado en total asignado, vencido, usado, pendiente de aprobación y disponible. Sigue el patrón del [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md): cada asignación, uso o reversión es una fila que no se edita, y el saldo sale de sumarlas. El banco de horas de [jornada y turnos](jornada-y-turnos.md) funciona igual, con horas en lugar de días.

## Cómo se gana el derecho a vacaciones

Las vacaciones se devengan: el derecho crece con el tiempo trabajado. Cada país fija cuánto, y los pisos difieren mucho. El Convenio 132 de la OIT dice que las vacaciones no pueden ser «less than three working weeks for one year of service» (art. 3.3). En el Reino Unido casi todos los trabajadores tienen «5.6 weeks' paid holiday a year», con un tope de 28 días.

El caso británico muestra también las tres formas de calcular el derecho que un sistema tiene que soportar:

| Situación | Cómo se calcula (ejemplo británico) |
|---|---|
| Jornada completa | 5,6 semanas, hasta 28 días |
| Tiempo parcial | prorrateado: quien trabaja 3 días por semana tiene 16,8 días |
| Horas irregulares o de temporada | se acumula según las horas trabajadas |

Los feriados pueden contarse dentro de esas 5,6 semanas, y el empleador puede dar más. En la Argentina, la escala del art. 150 depende de la antigüedad y va de 14 a 35 días corridos; el detalle está en [jornada y licencias en la Argentina](jornada-y-licencias-en-argentina.md). La antigüedad y la jornada salen del [legajo](../Legajo/legajo.md) y de la [modalidad de contratación](../Legajo/modalidades-de-contratacion.md).

Los días no gozados tienen un plazo para tomarse. El Convenio 132 permite dividir las vacaciones, pero una parte debe ser de «at least two uninterrupted working weeks» (art. 8.2). Esa parte se toma a más tardar un año después del año en que se ganó, y el resto, a más tardar a los dieciocho meses (art. 9.1). Lo que exceda un mínimo puede postergarse más allá, con acuerdo del empleado, hasta un límite que fija cada país (art. 9.2 y 9.3). Para un sistema, el saldo arrastrado necesita su fecha de vencimiento (inferencia de esta base). La regla argentina está en la nota del país.

## Quién pide y quién aprueba

La solicitud la hace el empleado y la aprueba otra persona. En el sistema abierto consultado, el aprobador se toma del empleado y, si no tiene uno cargado, de la tabla de aprobadores de su departamento, que viene de [puesto y estructura](../Legajo/puesto-y-estructura.md). Tres ajustes cambian el control: hacer obligatorio el aprobador, impedir que alguien apruebe su propia licencia y permitir o no solicitudes con fecha pasada.

La solicitud con fecha pasada es la forma normal de registrar una ausencia imprevista: alguien faltó por enfermedad el lunes y el martes carga la licencia con el certificado. Si el sistema la permite, no aparecen faltas falsas en la conciliación; si no, hay que corregirlas a mano (inferencia de esta base).

## Qué le llega a la liquidación

Esta sección es criterio de esta base, porque no se leyó una fuente sobre el efecto de cada licencia en la liquidación. Cada licencia aprobada llega a la [liquidación de sueldos](../Liquidacion-de-sueldos/liquidacion-de-sueldos.md) como una novedad en días, y el tipo decide qué [concepto de liquidación](../Liquidacion-de-sueldos/conceptos-de-liquidacion.md) se usa. La licencia con goce se paga, la sin goce descuenta días y algunas las paga un tercero (en la Argentina, la seguridad social paga la licencia por maternidad). Al terminar la relación, el saldo de vacaciones no gozadas se paga en la [liquidación final](../Liquidacion-de-sueldos/liquidacion-final.md).

> [!NOTE] Sin fuente todavía: una fuente agnóstica sobre cómo se valúa el día de licencia paga y cómo se descuenta el día sin goce. La valuación argentina (art. 155 de la Ley de Contrato de Trabajo) no se leyó.

## Vacaciones ilimitadas

> [!IMPORTANT]
> **Las vacaciones ilimitadas como posición contraria.** Algunas empresas eliminan el saldo: el empleado toma los días que necesita, con aprobación. Según Knowledge at Wharton (2017), una encuesta de SHRM daba esa política en el 1 % a 2 % de las empresas. Un profesor de Wharton dice que ninguna de las que la adoptaron «have reported that vacation time exploded», y que «If anything, we see they take less vacation», por lo que algunas la abandonaron. Una empresa de software temía que se tomara menos y pagaba 1.000 dólares a quien se tomara una semana. Según SHRM (2020), una firma con ese plan exige a sus empleados un mínimo de 120 horas libres por año. El estudio de 2018 según el cual quienes tienen el plan toman menos días, y el abandono de la política por una empresa en 2015, aparecieron en resúmenes del buscador y no en las páginas leídas. La evidencia viene de encuestas y casos sin revisión por pares.

Sin saldo, el sistema se ahorra el devengamiento y el monto pendiente de pagar, pero pierde la señal de que alguien no descansa (inferencia del informe de investigación). Donde la ley fija un mínimo, como en la Argentina, el saldo legal sigue existiendo aunque la política diga «ilimitadas» (inferencia de esta base). Adoptar o no una política así lo decide [Gestión de personas](../../Liderazgo-y-direccion/Gestion-de-personas/gestion-de-personas.md).
