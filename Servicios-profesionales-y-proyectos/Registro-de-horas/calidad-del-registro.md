---
resumen: >-
  La calidad del registro es cuánto se parecen las horas imputadas a las que de verdad se trabajaron en cada proyecto. No hay fuente con método que la mida; lo que se puede razonar es que depende de para qué se usa la hora y de qué premia la firma, y que cargar tarde obliga a reconstruir de memoria.
estado: borrador
estabilidad: semi
fuentes:
  - "WilmerHale (2010), Slice of History: Reginald Heber Smith and the Birth of the Billable Hour (según resumen): https://www.wilmerhale.com/en/insights/publications/slice-of-history-reginald-heber-smith-and-the-birth-of-the-billable-hour-august-9-2010"
  - "Wikipedia, Billable hours (según resumen): https://en.wikipedia.org/wiki/Billable_hours"
  - "Wikipedia, Goodhart's law (según resumen): https://en.wikipedia.org/wiki/Goodhart%27s_law"
  - "FAR 52.232-7 Payments under Time-and-Materials and Labor-Hour Contracts (según resumen): https://www.acquisition.gov/far/52.232-7"
  - "Odoo 19, Timesheets (según resumen): https://www.odoo.com/documentation/19.0/applications/services/timesheets.html"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md (sección 2.6)"
  - "Servicios-profesionales-y-proyectos/.investigacion/metricas-fundamentos-y-contraria.md (origen de la hoja de horas y posición contraria)"
aliases: [calidad del registro de horas, timesheet accuracy, subregistro, horas no registradas, carga tardía, sobrerregistro, padding, registro automático de tiempo]
creado: 2026-11-27
revisado:
---

# Calidad del registro

La calidad del registro es cuánto se parecen las horas imputadas a las que de verdad se trabajaron en cada proyecto. No hay fuente con método que la mida; lo que se puede razonar es que depende de para qué se usa la hora y de qué premia la firma, y que cargar tarde obliga a reconstruir de memoria.

Es el límite de todo lo que se calcula con la [hoja de horas](hoja-de-horas.md): la factura por hora, el costo y el margen del proyecto, la [utilización](../Rentabilidad-de-la-firma/utilizacion.md). Si la hora cargada no se parece a la trabajada, esos números heredan el error.

> [!NOTE]
> Sin fuente todavía: ningún estudio con método sobre cuántas horas se dejan de cargar, cuánto se infla la carga, qué cambia entre cargar a diario o por semana, ni si el registro automático mejora el dato. Circulan cifras de horas perdidas sin origen identificable; esta base no las repite. Lo que sigue es razonamiento de esta base sobre las pocas fuentes que hay.

## Para qué se inventó la hoja y para qué se usa

La hoja de horas nació hacia 1920 en un estudio jurídico como herramienta interna, para planificar y presupuestar, y recién antes de 1940 empezó a usarse para facturar; la historia está en [Fundamentos](../Fundamentos/fundamentos-de-servicios-profesionales.md#la-hora-facturable-nació-para-costear). Su inventor dijo que los abogados «hate any system» y que con el tiempo cargar la hoja fue «as much a matter of habit as getting dressed in the morning».

Como lectura de esta base, ese cambio de uso es el origen del problema. Mientras la hora sirve para planificar, nadie gana nada cargándola mal. Cuando sirve para cobrarle al cliente, para medir a la persona o para decidir su bono, cada uso empuja el dato en una dirección.

## El incentivo mueve el dato

Según el resumen de la entrada de enciclopedia sobre la hora facturable, los estudios jurídicos suelen exigir un número de horas por mes o por año, con bonos y ascensos atados a él, y la crítica de los libros de gestión de estudios es que la medida cuenta cantidad y no calidad. La ley de Goodhart lo dice en general: «When a measure becomes a target, it ceases to be a good measure», en la formulación de Strathern. Aplicarla a la hoja de horas es inferencia de esta base, y la crítica completa a la hora como meta está en [Fundamentos](../Fundamentos/fundamentos-de-servicios-profesionales.md).

Como criterio de esta base, el incentivo empuja en dos direcciones según qué se premie:

| Si la firma premia | El dato tiende a |
|---|---|
| Muchas horas facturables por persona | Inflarse en los proyectos que se cobran por hora y vaciarse en lo interno |
| No pasarse del presupuesto del proyecto | Quedarse corto en los proyectos ajustados, o irse a otro proyecto con margen |
| Nada, porque nadie mira la hoja | Cargarse tarde, redondeado y con descripciones vacías |

Que el incentivo financiero sube la cantidad de trabajo y no su calidad está en [compensación e incentivos](../../Liderazgo-y-direccion/Gestion-de-personas/compensacion-e-incentivos.md); vale también para la cantidad de horas que se cargan.

## Cargar a diario o al final de la semana

Ninguna fuente leída mide la diferencia. La única señal es una exigencia: en los contratos por tiempo y materiales del Estado de los Estados Unidos, la factura se respalda con «Individual daily job timekeeping records», según el resumen de la cláusula FAR 52.232-7. Un cliente que paga por hora y puede auditar pide el registro diario; es el extremo exigente, no la práctica general.

Como criterio de esta base, lo que se carga una semana después se reconstruye con la agenda y la memoria, y lo que no dejó rastro (una llamada, una revisión corta) se pierde o se reparte a ojo. Los controles que traen los sistemas apuntan a eso: uno colorea los totales de cada día contra la jornada de la persona (verde si coincide, rojo si falta), lo que hace visible el día sin cargar pero no dice si las horas están en el proyecto correcto.

## Qué se puede hacer sin datos

Sin estudios que lo midan, quedan medidas de sentido común, todas criterio de esta base:

- Separar la hora como dato de la hora como meta: quien carga no debería ganar ni perder por lo que carga.
- Cargar el mismo día, con una descripción que diga qué se hizo.
- Revisar en la aprobación los totales contra la jornada y contra la [reserva](../Asignacion-de-personas/reserva-de-personas.md) de la persona en ese proyecto.
- Mirar la tendencia: un proyecto que nunca se pasa ni por una hora del presupuesto es una señal tan sospechosa como uno que se pasa siempre.
