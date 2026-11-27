---
resumen: >-
  Una licencia es una ausencia autorizada, con o sin goce de sueldo, que el empleado pide y alguien aprueba; las vacaciones son la licencia que se gana con el tiempo trabajado. Cada tipo de licencia tiene sus reglas, un saldo que se asigna por período y se descuenta al aprobar, y un efecto en la liquidación.
estado: borrador
estabilidad: semi
fuentes:
  - "ERPNext, Leave Application (documentación de producto, como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/leave-application"
  - "GOV.UK, Holiday entitlement: https://www.gov.uk/holiday-entitlement-rights"
  - "OIT, Convenio 132 sobre las vacaciones pagadas (revisado), 1970, copia pública (según resumen; no leído): https://lankalaw.net/wp-content/uploads/2024/12/C132-Holidays-with-Pay-Convention-Revised-1970.pdf"
  - "SHRM, 4 lessons about unlimited vacation (según resumen): https://www.shrm.org/ResourcesAndTools/hr-topics/benefits/pages/4-lessons-about-unlimited-vacation.aspx"
  - "Wharton, Unlimited vacation time sounds great (según resumen): https://knowledge.wharton.upenn.edu/article/unlimited-vacation-time-sounds-great-policies-deliver/"
  - "Administracion-de-personal-y-nomina/.investigacion/legajo-y-tiempo.md (2026-11-27)"
aliases: [licencia, licencias, ausencias, vacaciones, licencia paga, licencia sin goce, saldo de vacaciones, devengamiento de vacaciones, leave, time off, absence management, paid time off, PTO, annual leave, leave balance, leave accrual, vacaciones ilimitadas, unlimited PTO]
creado: 2026-11-27
revisado:
---

# Licencias y ausencias

Una licencia es una ausencia autorizada, con o sin goce de sueldo, que el empleado pide y alguien aprueba; las vacaciones son la licencia que se gana con el tiempo trabajado. Cada tipo de licencia tiene sus reglas, un saldo que se asigna por período y se descuenta al aprobar, y un efecto en la liquidación.

Dentro de [tiempo y asistencia](tiempo-y-asistencia.md), la licencia es la ausencia que se sabe de antemano o que se justifica después; la que nadie autorizó aparece como falta en el [registro de asistencia](registro-de-asistencia.md). Las dos se cruzan: al aprobar una licencia, un sistema abierto crea un registro de asistencia con estado «en licencia» por cada día, y ese día deja de contar como falta.

## Tipo, asignación, solicitud y saldo

El modelo que usa un sistema abierto de gestión tiene cuatro piezas, y sirve para cualquier licencia:

1. **El tipo de licencia** define las reglas: si admite saldo negativo, si es sin goce, el máximo de días consecutivos y si los feriados dentro del período cuentan.
2. **La asignación** es el derecho del período: tantos días de vacaciones para este año. Una licencia sin goce no necesita asignación.
3. **La solicitud** es el pedido de unos días concretos, con estado abierto, aprobado o rechazado.
4. **El saldo** se lleva en un libro de movimientos: al aprobar, se descuenta; al cancelar, se revierte.

El saldo se muestra desagregado en total asignado, vencido, usado, pendiente de aprobación y disponible. Es el mismo patrón del [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md): cada asignación, uso o reversión es una fila que no se edita, y el saldo sale de sumarlas. El banco de horas de [jornada y turnos](jornada-y-turnos.md) funciona igual, con horas en lugar de días.

## Cómo se gana el derecho a vacaciones

Las vacaciones se devengan: el derecho crece con el tiempo trabajado. Cuánto, lo fija cada país, y los pisos difieren mucho. Según resúmenes del buscador, el Convenio 132 de la OIT pide un mínimo de «three working weeks» por un año de servicio; el texto no se leyó. En el Reino Unido casi todos los trabajadores tienen «5.6 weeks' paid holiday a year», con un tope de 28 días.

El Reino Unido muestra también las tres formas de calcular el derecho que un sistema tiene que soportar:

| Situación | Cómo se calcula (ejemplo británico) |
|---|---|
| Jornada completa | 5,6 semanas, hasta 28 días |
| Tiempo parcial | prorrateado: quien trabaja 3 días por semana tiene 16,8 días |
| Horas irregulares o de temporada | se acumula según las horas trabajadas |

Los feriados pueden contarse dentro de esas 5,6 semanas, y el empleador puede dar más. En la Argentina la escala del art. 150 depende de la antigüedad, de 14 a 35 días corridos: está en [jornada y licencias en la Argentina](jornada-y-licencias-en-argentina.md). La antigüedad y la jornada salen del [legajo](../Legajo/legajo.md) y de la [modalidad de contratación](../Legajo/modalidades-de-contratacion.md).

> [!NOTE] Sin fuente todavía: el arrastre de días no gozados de un año al otro en una fuente agnóstica (la página británica no lo trata; la regla argentina está en la nota del país).

## Quién pide y quién aprueba

La solicitud la hace el empleado y la aprueba otra persona. En el sistema abierto consultado, el aprobador se toma del empleado y, si no tiene uno cargado, de la tabla de aprobadores de su departamento, que viene de [puesto y estructura](../Legajo/puesto-y-estructura.md). Hay tres ajustes que cambian el control: hacer obligatorio el aprobador, impedir que alguien apruebe su propia licencia y permitir o no solicitudes con fecha pasada.

La solicitud con fecha pasada es la forma normal de registrar una ausencia imprevista: alguien faltó por enfermedad el lunes y el martes carga la licencia con el certificado. Permitirla evita faltas falsas en la conciliación; no permitirla obliga a corregirlas a mano (inferencia de esta base).

## Qué le llega a la liquidación

Lo que sigue es criterio de esta base, porque no se leyó una fuente sobre el efecto de cada licencia en la liquidación. Cada licencia aprobada llega a la [liquidación de sueldos](../Liquidacion-de-sueldos/liquidacion-de-sueldos.md) como una novedad en días, y el tipo decide qué [concepto de liquidación](../Liquidacion-de-sueldos/conceptos-de-liquidacion.md) se usa. La licencia con goce se paga, la sin goce descuenta días y algunas las paga otro (en la Argentina, la seguridad social paga la licencia por maternidad). Al terminar la relación, el saldo de vacaciones no gozadas se paga en la [liquidación final](../Liquidacion-de-sueldos/liquidacion-final.md).

> [!NOTE] Sin fuente todavía: una fuente agnóstica sobre cómo se valúa el día de licencia paga y cómo se descuenta el día sin goce. La valuación argentina (art. 155 de la Ley de Contrato de Trabajo) no se leyó.

## Vacaciones ilimitadas

> [!IMPORTANT]
> **Las vacaciones ilimitadas como posición contraria.** Algunas empresas eliminan el saldo: el empleado toma los días que necesita, con aprobación. Según un resumen de SHRM, un estudio de Namely de 2018 encontró que quienes tenían ese plan tomaban dos días menos al año, y Kickstarter abandonó la política en 2015 porque la gente tomaba menos; el mismo resumen trae un contraejemplo de una empresa donde el tiempo libre se repartió mejor. La evidencia es de encuestas y casos, no revisada por pares, y no se leyeron los originales.

Para el sistema, sacar el saldo saca también el devengamiento y el monto pendiente de pagar, pero se pierde la señal de que alguien no descansa (inferencia del informe de investigación). Donde la ley fija un mínimo, como en la Argentina, el saldo legal sigue existiendo aunque la política diga «ilimitadas» (inferencia de esta base). Si conviene o no una política así es una decisión de [Gestión de personas](../../Liderazgo-y-direccion/Gestion-de-personas/gestion-de-personas.md).
