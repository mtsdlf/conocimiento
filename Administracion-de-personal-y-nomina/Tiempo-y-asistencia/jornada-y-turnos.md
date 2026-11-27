---
resumen: >-
  La jornada es el tiempo que un empleado está a disposición del empleador, con un límite que fija cada país. El turno reparte esa jornada en días y horarios concretos. Lo que excede el límite son horas extra, que se pagan con un recargo o se compensan con tiempo libre en un banco de horas.
estado: borrador
estabilidad: estable
fuentes:
  - "GOV.UK, Maximum weekly working hours: https://www.gov.uk/maximum-weekly-working-hours"
  - "US Department of Labor, Overtime: https://www.dol.gov/agencies/whd/overtime"
  - "Odoo 18.0, Attendances (documentación de producto, como evidencia de práctica): https://www.odoo.com/documentation/18.0/applications/hr/attendances.html"
  - "Ley de Contrato de Trabajo 20.744, texto actualizado, InfoLEG, arts. 197 y 197 bis: https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm"
  - "Administracion-de-personal-y-nomina/.investigacion/legajo-y-tiempo.md (2026-11-27)"
aliases: [jornada de trabajo, jornada laboral, horario, turno, turnos rotativos, horas extra, horas extraordinarias, recargo, banco de horas, compensación de horas, francos compensatorios, working time, shift, overtime, time bank, time off in lieu, TOIL]
creado: 2026-11-27
revisado:
---

# Jornada y turnos

La jornada es el tiempo que un empleado está a disposición del empleador, con un límite que fija cada país. El turno reparte esa jornada en días y horarios concretos. Lo que excede el límite son horas extra, que se pagan con un recargo o se compensan con tiempo libre en un banco de horas.

Jornada y turnos es la mitad «esperada» de [tiempo y asistencia](tiempo-y-asistencia.md): el turno dice qué horas se esperaban, y el [registro de asistencia](registro-de-asistencia.md) compara contra él lo que el empleado marcó. La definición de jornada como tiempo «a disposición» viene de la ley argentina (art. 197 de la Ley de Contrato de Trabajo). Se usa porque deja claro que cuenta todo el tiempo disponible, además del productivo.

## Las cuatro piezas de una regla de jornada

Toda regla de jornada se describe con cuatro datos: el límite de horas, el período sobre el que se cuenta, el recargo de lo que lo excede y las excepciones. La síntesis sale del informe de investigación del tema, que compara dos normas que cortan distinto:

| Pieza | Reino Unido | Estados Unidos (federal) |
|---|---|---|
| Límite | 48 horas semanales de promedio | 40 horas por semana |
| Período de cómputo | «normally averaged over 17 weeks» | semana fija de 168 horas, sin promediar entre semanas |
| Exceso | se puede optar por superarlo | se paga a 1,5 veces la tarifa regular |
| Excepciones | servicios de emergencia, seguridad, trabajos donde «working time isn't measured»; menores de 18: 8 horas diarias y 40 semanales | los empleados exentos |

En Estados Unidos, además, trabajar un fin de semana o un feriado no da recargo por sí solo a nivel federal: el recargo aparece al pasar las 40 horas. En la Argentina el recargo depende también del día (sábado después de las 13, domingo y feriado), como muestra [jornada y licencias en la Argentina](jornada-y-licencias-en-argentina.md).

Quien diseña un sistema tiene que guardar esas cuatro piezas como parámetros del convenio o de la modalidad, no como constantes. La pieza que más se olvida es el período de cómputo. Con promedio sobre 17 semanas, una semana de 55 horas no es exceso si las otras compensan, y eso solo se sabe al cerrar el período (inferencia de esta base sobre la norma británica).

## El turno como dato del legajo

El turno es lo que el empleado tiene que cumplir: días, hora de entrada, hora de salida y pausas. Se asigna a cada empleado, o a un grupo, desde el [legajo](../Legajo/legajo.md), y cambia desde una fecha como cualquier otro dato con vigencia. Un turno rotativo cambia de horario según un ciclo; uno fijo repite el mismo cada semana.

Un sistema abierto usa el horario asignado para cerrar por su cuenta la marcación que quedó abierta: registra la salida según el horario más una tolerancia. También guarda tolerancias en minutos, a favor del empleado y a favor de la empresa. Así, llegar dos minutos tarde o salir dos minutos después no genera una tardanza ni una hora extra.

> [!NOTE] Sin fuente todavía: cómo se modelan los turnos rotativos y los ciclos de turnos (la documentación de turnos del sistema abierto consultado no se pudo abrir), y los convenios de la OIT sobre horas de trabajo (C001 y C030), que no se leyeron.

## Horas extra: recargo o tiempo libre

Una hora extra se devuelve de dos formas. Una es pagarla con un recargo sobre la tarifa normal: 1,5 veces en Estados Unidos, 50 % o 100 % según el día en la Argentina. La otra es guardarla en el banco de horas para devolverla en tiempo libre.

En el sistema abierto consultado, las horas extra pasan por una validación (automática o del gerente) antes de valer, y las aprobadas se pueden descontar del saldo de licencias. El banco de horas es un saldo de horas con entradas (horas extra aprobadas) y salidas (horas tomadas como franco), igual que el saldo de vacaciones de [licencias y ausencias](licencias-y-ausencias.md). Se modela con el mismo [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md): cada hora que entra o sale es una fila, y el saldo es la suma (inferencia de esta base sobre ese patrón).

La hora extra que se paga llega a la liquidación como una novedad en horas, y el recargo lo aplica un [concepto de liquidación](../Liquidacion-de-sueldos/conceptos-de-liquidacion.md) sobre el valor de la hora. La que va al banco llega al recibo recién cuando se toma o, si la regla lo prevé, cuando vence o termina la relación.

El tiempo parcial cambia la cuenta. En la Argentina, las horas que alguien con jornada reducida trabaja por encima de su jornada son «suplementarias» y voluntarias, no extraordinarias, mientras no pasen la jornada legal (art. 92 ter, detalle en [relación laboral en la Argentina](../Legajo/relacion-laboral-en-argentina.md)). Por eso la modalidad del contrato, descrita en [modalidades de contratación](../Legajo/modalidades-de-contratacion.md), decide qué es hora extra.

## Descansos entre jornadas y semanal

El descanso completa el límite: un mínimo de horas sin trabajar entre una jornada y la siguiente, y un descanso semanal. En la Argentina son 12 horas entre jornadas (art. 197) y el descanso desde el sábado a las 13 hasta el domingo a las 24, con descanso compensatorio si se trabaja (arts. 204 y 205). Un sistema que asigna turnos tiene que poder avisar cuando un cambio de turno deja menos de esas horas.

> [!NOTE] Sin fuente todavía: una regla de descanso agnóstica o de otro país para contrastar con la argentina; la página británica consultada no cubre descansos.
