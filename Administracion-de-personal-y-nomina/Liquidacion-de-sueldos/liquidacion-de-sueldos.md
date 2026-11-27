---
resumen: >-
  La liquidación de sueldos es el cálculo, para cada período de liquidación, de cuánto se le paga a cada empleado y cuánto se le descuenta. Junta los datos del legajo y las novedades del período, los pasa por los conceptos de liquidación y deja un recibo por persona, la base de las cargas y el documento que va a la contabilidad.
estado: borrador
estabilidad: estable
fuentes:
  - "OIT, Convenio sobre la protección del salario, 1949 (núm. 95), arts. 3, 5, 8, 10, 11, 12 y 13 (copia de la Universidad de Minnesota): https://hrlibrary.umn.edu/instree/ilo95.html"
  - "GOV.UK, Running payroll (ejemplo de país): https://www.gov.uk/running-payroll"
  - "GOV.UK, Running payroll: reporting to HMRC (según un extracto): https://www.gov.uk/running-payroll/reporting-to-hmrc"
  - "Nacha, ACH Network (según un resumen): https://www.nacha.org/ach-network"
  - "Frappe HR, Payroll Entry y Additional Salary (documentación de producto, como evidencia de práctica): https://docs.frappe.io/hr/payroll-entry"
  - "Frappe HR, Additional Salary: https://docs.frappe.io/hr/additional-salary"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-cargas-y-fundamentos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-huecos.md (2026-11-27)"
aliases: [liquidación de sueldos, liquidación de haberes, nómina, payroll, payroll processing, ciclo de nómina, payroll cycle, pago de sueldos, embargo de sueldo, wage garnishment, adelanto de sueldo]
creado: 2026-11-27
revisado:
---

# Liquidación de sueldos

La liquidación de sueldos es el cálculo, para cada período de liquidación, de cuánto se le paga a cada empleado y cuánto se le descuenta. Junta los datos del legajo y las novedades del período, los pasa por los conceptos de liquidación y deja un recibo por persona, la base de las cargas y el documento que va a la contabilidad.

Dentro de [Administración de personal y nómina](../administracion-de-personal-y-nomina.md) es la vertical que convierte registros en dinero. Lee del [legajo](../Legajo/legajo.md) el sueldo, la categoría y la modalidad vigentes en el período, y de [tiempo y asistencia](../Tiempo-y-asistencia/tiempo-y-asistencia.md) las novedades (horas extra, licencias, faltas). Le pasa a [cargas y declaraciones](../Cargas-y-declaraciones/cargas-y-declaraciones.md) la base sobre la que se calculan los aportes, las contribuciones y la retención, y a la contabilidad el documento del asiento. Sin software, es una planilla por empleado y un recibo a mano; con software, un lote que procesa a todos a la vez.

## El ciclo de cada período

Cada período de liquidación recorre los mismos siete pasos. Las fuentes leídas describen el centro del ciclo (calcular, emitir recibos, informar y pagar); el orden completo y los pasos de control y cierre son criterio de esta base.

1. **Novedades.** Se juntan los cambios del período: altas y bajas, cambios de sueldo con su fecha, horas extra y licencias aprobadas, pagos únicos. Una novedad que llega después del cierre ya no entra en este período y pasa a una [reliquidación](retroactivos-y-reliquidaciones.md).
2. **Cálculo.** Cada empleado pasa por sus [conceptos de liquidación](conceptos-de-liquidacion.md), del bruto al neto. En un software abierto de nómina, el cálculo corre como un lote que procesa a muchos empleados a la vez y genera un recibo por empleado sin duplicar los ya creados.
3. **Control y cuadre.** Se compara contra el período anterior y se explican las diferencias. Como criterio de esta base, el cuadre mínimo es que la suma de los netos más las deducciones dé el total de los haberes.
4. **Aprobación.** Alguien distinto de quien liquidó acepta el lote. Es criterio de esta base: cualquier pago gana con la separación de tareas.
5. **Cierre.** El período queda cerrado y lo liquidado deja de editarse. Cualquier corrección posterior se hace con movimientos nuevos, como en [retroactivos y reliquidaciones](retroactivos-y-reliquidaciones.md).
6. **Pago.** Se paga el neto de cada empleado y se emite el [recibo de sueldo](recibo-de-sueldo.md).
7. **Contabilización.** El lote cerrado es el documento del asiento de sueldos y cargas, que está en [operaciones](../../Contabilidad/Operaciones/operaciones.md#cómo-se-registran-los-sueldos), dentro de Contabilidad. Allá el sueldo se devenga cuando el empleado trabaja, sin esperar al pago, y el pago es otro asiento. El software abierto leído hace lo mismo: registra el devengamiento contra una cuenta de sueldos a pagar al confirmar los recibos y, aparte, un único asiento por el pago.

El ciclo se ata al calendario de las cargas. En el ejemplo del Reino Unido, en cada día de pago el empleador calcula impuesto y aportes, produce los recibos e informa al fisco «on or before» el día de pago. Lo que se declara y cuándo vence está en [cargas y declaraciones](../Cargas-y-declaraciones/cargas-y-declaraciones.md).

> [!NOTE]
> Sin fuente todavía: una descripción agnóstica del ciclo con sus pasos de control, aprobación y cierre (el Body of Knowledge de los profesionales de nómina no se pudo leer).

## Frecuencias y período de liquidación

La OIT pide que el salario se pague con regularidad, «Wages shall be paid regularly», y deja los intervalos a la ley nacional, al convenio colectivo o al laudo (Convenio 95, art. 12). No impone mensual, quincenal ni semanal. Por eso la frecuencia es un dato de cada grupo de empleados, y el software abierto leído la pide al crear el lote («Select the Payroll Frequency»). En la Argentina, el mensualizado cobra al vencimiento de cada mes calendario y hay plazos para pagar, en [liquidación en la Argentina](liquidacion-en-argentina.md).

## Liquidaciones fuera de ciclo

Hay pagos que no esperan al período, como la [liquidación final](liquidacion-final.md) de quien se va a mitad de mes. Las fuentes leídas los resuelven de dos maneras:

- Un pago adicional que entra al próximo lote. El software abierto leído registra un pago adicional para un empleado, con una fecha única o recurrente entre dos fechas, que se incorpora al recibo si la fecha cae en el período procesado; puede incluso reemplazar el monto de un concepto («Overwrite Salary Structure Amount»).
- Una liquidación aparte, con su propia declaración. El Reino Unido admite un pago extra con su propia declaración, que tiene que llegar antes del siguiente informe regular.

## El pago de sueldos

La liquidación dice cuánto se le paga a cada uno. La transferencia, la posición de caja y la conciliación del banco son del tema Tesorería y finanzas de la empresa en marcha, todavía no escrito. Acá quedan las reglas que limitan cómo y cuánto se paga.

Sobre el medio de pago, el Convenio 95 de la OIT pide pagar en moneda de curso legal, prohíbe los vales y los cupones, y dice que la autoridad puede permitir el cheque o el giro donde sea costumbre o necesario (art. 3). El pago va directo al trabajador, salvo lo que diga la ley o lo que él acepte (art. 5), y el pago en efectivo se hace en día laborable y en el lugar de trabajo o cerca (art. 13). La OIT no menciona la transferencia; en la Argentina, la ley obliga a pagar por acreditación en una cuenta sueldo ([liquidación en la Argentina](liquidacion-en-argentina.md#cuenta-sueldo-y-plazo-de-pago)).

Con transferencia, la liquidación termina en un archivo con un registro por empleado (cuenta y neto) que el banco procesa. En el ejemplo de EE. UU., según un resumen de la página del operador de la red, el depósito de sueldos está en la cuenta del empleado «by 9 a.m.» del día de pago, y el día de pago que cae en fin de semana o feriado se paga el viernes anterior.

> [!NOTE]
> Sin fuente todavía: el formato de los archivos de pago de sueldos (tipos de registro y campos) de alguna red bancaria.

Los adelantos, los préstamos y los embargos vuelven a la liquidación como deducciones del neto, con límites. La OIT solo permite deducciones en las condiciones y hasta el límite que fijen la ley, el convenio o el laudo (art. 8), y permite embargar el salario solo en la forma y los límites de la ley nacional, protegiendo lo necesario para mantener al trabajador y su familia (art. 10). Como criterio de esta base, un adelanto o un préstamo es un descuento que acepta el trabajador. Un embargo es una retención por orden de un tercero (un juez, el fisco, quien cobra una cuota alimentaria), con su propia prioridad. El cálculo de cada uno y su orden están en [conceptos de liquidación](conceptos-de-liquidacion.md#adelantos-préstamos-y-embargos); los anticipos para gastos que se rinden no son adelantos de sueldo y están en [gastos y rendiciones](../../Contabilidad/Operaciones/gastos-y-rendiciones.md).

Si la empresa quiebra, la OIT pide que los trabajadores sean acreedores privilegiados y que el salario privilegiado se pague entero antes que a los acreedores comunes (art. 11).

## Cómo falla la liquidación

La mayoría de los errores nace en un dato de entrada: un cambio de sueldo cargado sin fecha del hecho, una licencia aprobada después del cierre, un concepto mal configurado que se repite en todos los recibos. Esa idea ordena el [tema](../administracion-de-personal-y-nomina.md), y las fallas públicas de sistemas de nómina que la ilustran, con sus cifras, están en [Fundamentos](../Fundamentos/fundamentos-de-administracion-de-personal.md). Como criterio de esta base, dos prácticas protegen: el control contra el período anterior y no editar un período cerrado.

## Qué hay adentro de la liquidación de sueldos

- [Conceptos de liquidación](conceptos-de-liquidacion.md): haberes y deducciones, base de cálculo, orden, proporcionales, bruto a neto y neto a bruto, y la idea de remunerativo; leelo antes que lo demás.
- [Recibo de sueldo](recibo-de-sueldo.md): qué tiene que mostrar el comprobante de cada pago, cuándo se entrega y la conformidad.
- [Retroactivos y reliquidaciones](retroactivos-y-reliquidaciones.md): cómo se paga la diferencia de un período cerrado sin editarlo, con la fecha del hecho y la fecha de registro.
- [Liquidación final](liquidacion-final.md): lo que se paga cuando termina la relación: lo proporcional, las vacaciones no gozadas y la indemnización.
- [Liquidación en la Argentina](liquidacion-en-argentina.md): aguinaldo, recibo de la LCT, plazo de pago, cuenta sueldo, sumas no remunerativas, indemnización, preaviso, Fondo de Asistencia Laboral y embargos.
