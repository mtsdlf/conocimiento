---
resumen: >-
  El registro de asistencia es la lista de marcaciones de entrada y salida de cada empleado, corregida y conciliada con su turno, de la que salen las horas trabajadas, las horas extra, las ausencias y las tardanzas del período. Registra presencia y horas, no rendimiento.
estado: borrador
estabilidad: semi
fuentes:
  - "Odoo 18.0, Attendances (documentación de producto, como evidencia de práctica): https://www.odoo.com/documentation/18.0/applications/hr/attendances.html"
  - "ERPNext, Leave Application (documentación de producto, como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/leave-application"
  - "ICO, nota de prensa sobre la guía Monitoring workers, octubre de 2023 (según resumen): https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2023/10/ico-publishes-guidance-to-ensure-lawful-monitoring-in-the-workplace"
  - "ICO, Employment practices and data protection: monitoring workers (PDF no leído; error 403): https://ico.org.uk/media/for-organisations/uk-gdpr-guidance-and-resources/employment-information/employment-practices-and-data-protection-monitoring-workers-1-0.pdf"
  - "APA Monitor, sobre el metaanálisis de Ravid, Behrend y otros, Personnel Psychology 2023 (según resumen): https://www.apa.org/monitor/2026/11-12/hidden-costs-workplace-surveillance.html"
  - "Universidad de St Andrews y JRC, vigilancia y confianza (según resumen): https://news.st-andrews.ac.uk/?p=21134"
  - "29 CFR 516.6, vía Cornell LII: https://www.law.cornell.edu/cfr/text/29/516.6"
  - "Administracion-de-personal-y-nomina/.investigacion/legajo-y-tiempo.md (2026-11-27)"
aliases: [marcación, fichaje, fichada, control horario, reloj de control, reloj biométrico, planilla de asistencia, ausentismo, tardanza, attendance, clock in, clock out, time clock, punch, timesheet]
creado: 2026-11-27
revisado:
---

# Registro de asistencia

El registro de asistencia es la lista de marcaciones de entrada y salida de cada empleado, corregida y conciliada con su turno, de la que salen las horas trabajadas, las horas extra, las ausencias y las tardanzas del período. Registra presencia y horas, no rendimiento.

El registro es la mitad «ocurrida» de [tiempo y asistencia](tiempo-y-asistencia.md). La otra mitad, lo esperado, es el turno de [jornada y turnos](jornada-y-turnos.md). Los días que el empleado pidió no venir y le aprobaron están en [licencias y ausencias](licencias-y-ausencias.md).

## Qué guarda una marcación

En un sistema abierto de gestión, cada registro de asistencia tiene una entrada y una salida, y el tiempo trabajado del día es la suma de esos pares. Cada marcación guarda además cómo se hizo: en un quiosco (una terminal compartida), desde una barra del sistema en la computadora del empleado o a mano. También puede guardar la dirección IP, el navegador y, si se activa, la ubicación GPS.

El modo cambia el control. Una marcación a mano la carga alguien, y conviene que quede registrado quién (criterio de esta base). Una de quiosco depende de que quien marca sea quien dice ser. Elegir qué datos de cada marcación se guardan es también una decisión de privacidad, porque la ubicación de un empleado es un dato personal (ver más abajo).

## Marcaciones rotas y cómo se corrigen

Las marcaciones fallan de formas conocidas: alguien entra y no marca la salida, o marca dos veces la entrada. El sistema abierto consultado marca como error una entrada sin salida después de 24 horas o un período abierto de más de 16 horas. Solo alguien con permiso la corrige o la borra. El sistema también puede cerrar por su cuenta la marcación abierta con la salida del horario asignado más una tolerancia.

Una corrección mal hecha le quita al registro su valor como prueba. Como criterio de la base, una marcación corregida debería guardar la original, quién la cambió y cuándo, igual que se corrige un [movimiento](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md): con otra fila, sin pisar la primera. Cada país fija qué se guarda y por cuánto tiempo. Por ejemplo, en Estados Unidos las tarjetas de tiempo se conservan «at least 2 years» (29 CFR 516.6), y no hay una segunda fuente para ese plazo.

## Conciliar con el turno: ausencias, tardanzas y extras

Conciliar es comparar, día por día, lo marcado con lo esperado. La comparación da cuatro resultados, que la conciliación separa para la aprobación:

| Lo marcado frente al turno | Resultado | Qué llega a la liquidación |
|---|---|---|
| Igual, dentro de la tolerancia | horas normales | nada aparte del sueldo |
| Entrada después del horario | tardanza | según la política, un descuento o solo el registro |
| Más horas que el turno | horas extra a validar | horas con recargo o al banco de horas |
| Ninguna marcación, sin licencia | ausencia | un día sin goce o una falta a justificar |

La tabla es una síntesis de esta base. Del sistema abierto consultado salen dos datos: las horas extra se validan antes de valer, y hay tolerancias en minutos a favor del empleado y de la empresa. De otro sistema sale que una licencia aprobada evita la falta: al aprobarla se crea un registro de asistencia con estado «en licencia» por cada día.

> [!NOTE] Sin fuente todavía: una fuente que describa la conciliación de marcaciones con turnos, el tratamiento de tardanzas y el paso de la ausencia injustificada al descuento (la documentación de turnos del sistema abierto consultado no se pudo abrir).

## Trabajo remoto

Sin reloj en la puerta, el empleado marca desde su computadora o su teléfono. Los modos del sistema abierto consultado que permiten marcar a distancia (barra del sistema, IP, navegador, GPS) son también los que más datos personales juntan. La política de trabajo remoto (quién puede, cuántos días) la decide [Gestión de personas](../../Liderazgo-y-direccion/Gestion-de-personas/gestion-de-personas.md); acá solo se registra.

> [!NOTE] Sin fuente todavía: cómo se registra la jornada en el trabajo remoto y qué pide la ley argentina para ese caso.

## Vigilancia y lo que dice la evidencia

Registrar horas es distinto de vigilar. El fichaje alimenta la liquidación y el cumplimiento de los límites de jornada, y no mide resultado. La distinción es inferencia del informe de investigación: el sistema consultado usa la marcación para tiempo trabajado y horas extra, y no para desempeño.

El regulador británico de datos personales (ICO) publicó en octubre de 2023 una guía sobre monitoreo de trabajadores. Según un resumen de la nota de prensa, el monitoreo tiene que ser «necessary and proportionate» y en general hay que avisar antes. El consentimiento rara vez sirve como base, porque el empleado no está en igualdad con el empleador. La guía tiene secciones sobre fichaje biométrico, y el empleado puede pedir los datos que se juntaron sobre él. El PDF de la guía no se pudo abrir. El marco argentino de datos personales está en [privacidad de datos personales](../../Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md).

> [!IMPORTANT]
> **¿La vigilancia mejora la productividad?** Según el resumen del APA Monitor, el metaanálisis de Ravid, Behrend y otros (Personnel Psychology, 2023) sobre monitoreo electrónico del desempeño no encontró mejora del desempeño y sí más estrés. Según un resumen de la Universidad de St Andrews con el JRC, juntar datos sin un propósito explícito, «for its own sake», genera actitudes negativas y menos confianza. Las dos fuentes son secundarias: no se leyeron los originales ni se vieron tamaños de efecto. Para un diseño, lo razonable es juntar lo que la liquidación y la ley necesitan y nada más (inferencia de esta base).

## Dónde termina el registro de asistencia

La asistencia dice cuántas horas trabajó alguien. La carga de horas por proyecto (en qué proyecto, para qué cliente, si se factura) es del tema Servicios profesionales y proyectos, todavía no escrito. Muchos sistemas piden las dos cosas en una sola hoja de horas. Aun así, la suma de horas por proyecto no reemplaza a la marcación como registro de jornada, porque responde a otra pregunta (inferencia de esta base).
