---
resumen: >-
  La hoja de horas es el documento en que una persona carga sus horas imputadas de un período, por proyecto y tarea, y las envía para que alguien las apruebe. Pasa por borrador, enviada, aprobada o devuelta; al aprobarse genera el costo y la venta sin facturar del proyecto, y desde ahí una corrección se hace revirtiendo, no editando.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Project Operations, Time entry overview, UI behavior y Time entry configurations (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/time/time-entry-overview"
  - "Microsoft Learn, Project Operations, Approvals overview (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/approvals/approvals-overview"
  - "Microsoft Learn, Project Operations, Recall and cancel approvals (como evidencia de práctica): https://learn.microsoft.com/en-us/dynamics365/project-operations/approvals/recall-cancel"
  - "ERPNext, Timesheet (según resumen): https://docs.frappe.io/erpnext/user/manual/en/timesheet"
  - "Odoo 19, Timesheets (según resumen): https://www.odoo.com/documentation/19.0/applications/services/timesheets.html"
  - "WilmerHale (2010), Slice of History: Reginald Heber Smith and the Birth of the Billable Hour (según resumen): https://www.wilmerhale.com/en/insights/publications/slice-of-history-reginald-heber-smith-and-the-birth-of-the-billable-hour-august-9-2010"
  - "FAR 52.232-7 Payments under Time-and-Materials and Labor-Hour Contracts (según resumen): https://www.acquisition.gov/far/52.232-7"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 3)"
  - "Servicios-profesionales-y-proyectos/.investigacion/asignacion-y-horas.md (secciones 2.2 y 2.3)"
aliases: [hoja de horas, timesheet, planilla de horas, parte de horas, time sheet, aprobación de horas, timesheet approval]
creado: 2026-11-27
revisado:
---

# Hoja de horas

La hoja de horas es el documento en que una persona carga sus horas imputadas de un período, por proyecto y tarea, y las envía para que alguien las apruebe. Pasa por borrador, enviada, aprobada o devuelta; al aprobarse genera el costo y la venta sin facturar del proyecto, y desde ahí una corrección se hace revirtiendo, no editando.

Es la forma concreta del [registro de horas](registro-de-horas.md). Lo que aprueba alimenta la [facturación por hora](../Facturacion-del-proyecto/facturacion-por-hora.md) y el [trabajo en curso](../Facturacion-del-proyecto/trabajo-en-curso.md), y lo que se carga mal se discute en [calidad del registro](calidad-del-registro.md).

## Qué lleva cada línea

La primera hoja de horas documentada, la que Reginald Heber Smith armó hacia 1920 en un estudio jurídico de Boston, era «a form on which you wrote the name of the client, the name of the case», más la descripción del trabajo y el tiempo. La unidad mínima era una décima de hora, porque «I can more easily add, subtract, and divide on the decimal system»: de ahí los seis minutos que todavía usan muchos estudios (según el resumen de la historia que publica ese estudio).

Los sistemas actuales guardan lo mismo con más dimensiones:

| Dato | Para qué sirve |
|---|---|
| Persona y fecha | Quién y qué día; la suma por día se compara con la jornada |
| Proyecto y tarea | A qué se imputa; la tarea es opcional en algunos sistemas |
| Rol o tipo de actividad | De dónde sale la tarifa y el costo, según [roles y habilidades](../Asignacion-de-personas/roles-y-habilidades.md#tarifa-por-rol-o-por-persona) |
| Duración | Cuánto; un sistema permite fijar un intervalo mínimo de 1 a 60 minutos y redondea al múltiplo mayor |
| Facturable o no | Si se cobra; quién lo decide se explica en [registro de horas](registro-de-horas.md#quién-decide-si-una-hora-se-cobra) |
| Descripción | Qué se hizo; es lo que el cliente lee si la factura lo detalla |
| Costo y tarifa | Dos valores separados, que se fijan al enviar o al aprobar |

Un sistema también limita la duración por día (configurable, por defecto 24 horas). Otro colorea los totales de cada día contra la jornada de la persona: verde si coincide, naranja si excede, rojo si falta.

## El período de la hoja

Dos de los sistemas leídos cargan en una grilla semanal, con vista por día o por mes. Como criterio de esta base, la semana es la unidad de carga, no necesariamente la de aprobación ni la de factura.

> [!NOTE]
> Sin fuente todavía: el cierre del período (una fecha después de la cual no se cargan más horas de una semana o un mes) no aparece en ninguna de las fuentes leídas. Tampoco hay fuente sobre la jerarquía de proyecto, tarea y actividad como práctica recomendada.

La frecuencia de carga sí tiene un caso extremo documentado. En los contratos por tiempo y materiales del Estado de los Estados Unidos, cada factura se respalda con «Individual daily job timekeeping records», según el resumen de la cláusula FAR 52.232-7 (una sola fuente, leída por resumen). Es una exigencia de un cliente público estadounidense, no práctica general; muestra hasta dónde puede pedir un cliente que el registro sea diario.

## Los estados y quién aprueba

Un sistema de gestión de servicios documenta cuatro estados:

1. **Borrador.** La hora nace así y solo en borrador se puede borrar.
2. **Enviada.** «After you submit time entries, you can't edit them.» La persona puede retirarla y volver a editarla mientras nadie la aprobó.
3. **Aprobada.** Crea los valores reales del proyecto: «If the entry is related to a project, the actuals are created when you approve it».
4. **Devuelta.** El aprobador la rechazó; vuelve a la persona con un comentario visible para corregir y reenviar.

En ese sistema aprueban los miembros del equipo marcados como aprobadores del proyecto, y además se puede configurar el jefe de cada persona. Un sistema abierto bloquea la tarifa de venta y el costo al enviar la hoja («Billing Rate and Costing rate get locked») y factura desde la hoja enviada. Otro tiene la validación como permiso («validate all employees' timesheets»), sin un flujo de varios pasos documentado.

Los sistemas difieren (uno bloquea la tarifa al enviar la hoja, otro factura desde la hoja enviada), pero como lectura de esta base la aprobación es el punto en que la hora deja de ser de la persona y pasa a ser del proyecto: desde ahí cuenta como costo, como venta sin facturar si el contrato es por tiempo y materiales, y como base de la utilización. En un proyecto a precio cerrado, el mismo sistema crea solo el costo.

## Corregir una hora aprobada o facturada

El sistema documentado ofrece tres caminos, según quién corrige y si la hora ya se facturó:

| Situación | Qué se hace | Efecto |
|---|---|---|
| Quien aprobó quiere corregir | Cancela la aprobación: la hora vuelve a enviada, cambia cantidad facturable o tipo y aprueba de nuevo | Los valores originales quedan ajustados y se crean reversas |
| Quien cargó quiere corregir | Pide el retiro con un motivo obligatorio; si el aprobador lo acepta, la hora vuelve devuelta | La persona edita, reenvía o borra |
| La hora ya está en una factura | No se puede retirar: «You can't create a recall request for an approved time [...] that the system already invoiced» | Solo después de una factura correctiva que acredite la original entera |

El patrón es el de un [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md#un-error-se-corrige-con-otro-movimiento): la hora aprobada no se edita, se revierte con un movimiento de signo contrario y se vuelve a cargar. Al revertir, el gasto registrado y la venta pendiente del proyecto dejan de contarla.

La corrección de una hora facturada toca la factura, que es de [facturación del proyecto](../Facturacion-del-proyecto/facturacion-del-proyecto.md), y lo que ya se le pagó a la persona no cambia: la asistencia es otro registro (ver [registro de horas](registro-de-horas.md#la-hora-imputada-no-es-la-asistencia)).

## Sin software

Una planilla con una fila por persona, día, proyecto y horas, más una columna de estado, hace lo mismo. Como criterio de esta base, lo que una planilla no da por sí sola es el bloqueo: si una fila aprobada se puede pisar, se pierde la regla del movimiento, y conviene corregir agregando una fila negativa con el motivo.
