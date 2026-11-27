---
resumen: >-
  Un retroactivo es un pago que corresponde a un período de liquidación ya cerrado, como un aumento firmado hoy que vale desde hace tres meses; la reliquidación es el cálculo que lo resuelve, comparando lo que correspondía con lo que se pagó y liquidando la diferencia en un período abierto, sin editar lo ya pagado y declarado.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, Temporal Patterns, Time Narrative (según un extracto): https://martinfowler.com/eaaDev/timeNarrative.html"
  - "GOV.UK, Running payroll: reporting to HMRC (según un extracto; ejemplo de país): https://www.gov.uk/running-payroll/reporting-to-hmrc"
  - "IRS, Publication 15 (Circular E), 2026, sección 7, supplemental wages (ejemplo de país): https://www.irs.gov/publications/p15"
  - "Frappe HR, Additional Salary (documentación de producto, como evidencia de práctica; según un extracto): https://docs.frappe.io/hr/additional-salary"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-cargas-y-fundamentos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-huecos.md (2026-11-27)"
aliases: [retroactivo, retroactivos, reliquidación, diferencias de sueldo, ajuste retroactivo, aumento retroactivo, back pay, retroactive pay, arrears, payroll recalculation, retro pay]
creado: 2026-11-27
revisado:
---

# Retroactivos y reliquidaciones

Un retroactivo es un pago que corresponde a un período de liquidación ya cerrado, como un aumento firmado hoy que vale desde hace tres meses; la reliquidación es el cálculo que lo resuelve, comparando lo que correspondía con lo que se pagó y liquidando la diferencia en un período abierto, sin editar lo ya pagado y declarado.

Es el caso que pone a prueba toda la [liquidación de sueldos](liquidacion-de-sueldos.md). Los retroactivos aparecen por un aumento de convenio o individual firmado tarde, una novedad que llegó después del cierre (horas extra de la última semana, una licencia mal cargada) o un error de cálculo que se descubre meses después. En los tres casos lo pagado ya está en un [recibo de sueldo](recibo-de-sueldo.md) entregado, en el asiento contable y en la declaración de [cargas](../Cargas-y-declaraciones/cargas-y-declaraciones.md).

## La fecha del hecho y la fecha de registro

Fowler, en la página Time Narrative, abre su explicación de los patrones temporales con un sistema de nómina: «Imagine we have a payroll system that knows that en employee has a rate of $100/day starting on January 1», y muestra qué pasa cuando llega un cambio retroactivo. Distingue dos tiempos: cuándo pasó algo (la fecha del hecho) y cuándo se supo (la fecha de registro).

El [legajo](../Legajo/legajo.md#la-historia-del-legajo-con-sus-dos-fechas) guarda las dos fechas en cada cambio, y la reliquidación las usa para contestar dos preguntas distintas. Con las fechas del caso del legajo, un aumento de 1.000.000 a 1.100.000 firmado el 10 de mayo y vigente desde el 1 de marzo:

| Período | Lo que correspondía (fecha del hecho) | Lo que se liquidó (lo registrado al cierre) | Diferencia |
|---|---|---|---|
| Marzo | 1.100.000 | 1.000.000 | 100.000 |
| Abril | 1.100.000 | 1.000.000 | 100.000 |
| Mayo | 1.100.000 | se liquida con el aumento ya cargado | 0 |

La diferencia de 200.000 se paga en mayo como un concepto de retroactivo, con la indicación de a qué períodos corresponde. Las cifras son un ejemplo de esta base.

## Corregir con movimientos nuevos

La regla de Fowler es que una corrección no se edita sobre lo registrado: se registra como una entrada nueva, con su propia fecha de registro. Cambiar hacia atrás el tiempo de registro «break the integrity of the record», y según él no hay situación retroactiva que no se pueda resolver con la dimensión de la fecha del hecho, «unless fraud is one of your requirements».

En la nómina eso significa que marzo no se reabre. El recibo de marzo queda como se emitió, y mayo lleva líneas nuevas que suman la diferencia. Es el mismo principio que el [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) aplica al stock o a una cuenta corriente: filas que no se editan y un saldo que se calcula sumándolas. Lo pagado a un empleado por marzo es la suma de lo liquidado en marzo y de todos los retroactivos que dicen «marzo».

Las fuentes leídas muestran dos formas de llevar la diferencia al período abierto:

- **Como un pago adicional dentro del recibo del mes.** Un software abierto de nómina trata los atrasos como un tipo de pago adicional, junto al bono o el incentivo («such as a bonus, allowance, arrears, or incentive»).
- **Como una declaración corregida.** En el ejemplo del Reino Unido, un error en la declaración de un pago se corrige mandando una declaración corregida «as soon as possible».

Una tercera forma posible es un recibo complementario aparte del recibo del mes; ninguna fuente leída la describe.

## Lo que arrastra un retroactivo

El aumento del básico no cambia solo el básico. Todo [concepto](conceptos-de-liquidacion.md) que lo usa como base cambia también: las horas extra de marzo, el adicional por antigüedad, los aportes y la retención. Por eso la reliquidación correcta recalcula el período completo con los datos vigentes a la fecha del hecho y lo compara, concepto por concepto, con lo que se liquidó. Es inferencia de esta base a partir del modelo de conceptos que dependen de otros.

Fowler sugiere otra salida para explicar resultados pasados sin un modelo de dos fechas completo: guardar una traza detallada del cálculo. Aplicado a la nómina (inferencia de esta base), guardar con cada recibo los datos de entrada y la versión de cada fórmula permite reproducir marzo como se liquidó y como debió liquidarse.

El impuesto trata al retroactivo como un pago aparte. En el ejemplo de EE. UU., según la guía del IRS (una sola fuente), los «supplemental wages» incluyen el «back pay» y los «retroactive pay increases», y se les retiene un 22 % fijo (37 % sobre lo que supere 1 millón de dólares en el año) o se suman al sueldo regular y se calcula como un solo pago. Si el retroactivo cambia también las bases declaradas de meses anteriores depende de cada país; está en [cargas y declaraciones](../Cargas-y-declaraciones/cargas-y-declaraciones.md) y en [retención de impuestos sobre sueldos](../Cargas-y-declaraciones/retencion-de-impuestos-sobre-sueldos.md).

## Cómo falla una reliquidación

- **Editar el período cerrado.** Se pierde qué se pagó y el recibo entregado deja de coincidir con el sistema y con lo declarado.
- **Pagar solo la diferencia del básico.** Quedan sin ajustar los conceptos que dependían de él.
- **Perder la fecha de registro.** Sin ella, el sistema no sabe con qué sueldo se liquidó marzo y no puede calcular cuánto faltó.
- **Pagar dos veces.** Si el retroactivo no queda marcado con el período al que corresponde, una segunda reliquidación lo vuelve a pagar.

Son fallas que esta base deduce del modelo; ninguna fuente leída las enumera.
