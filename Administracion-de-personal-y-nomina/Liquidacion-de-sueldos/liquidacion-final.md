---
resumen: >-
  La liquidación final es la que se hace cuando termina la relación laboral: paga lo trabajado y no cobrado hasta el último día, la parte proporcional de los conceptos que se devengan por período, las vacaciones no gozadas y, según el motivo de la salida, el preaviso y la indemnización, y descuenta lo que el empleado deba.
estado: borrador
estabilidad: estable
fuentes:
  - "OIT, Convenio sobre la protección del salario, 1949 (núm. 95), art. 12 (copia de la Universidad de Minnesota): https://hrlibrary.umn.edu/instree/ilo95.html"
  - "IRS, Publication 15 (Circular E), 2026, sección 7, supplemental wages (ejemplo de país): https://www.irs.gov/publications/p15"
  - "Frappe HR, Salary Structure (documentación de producto, como evidencia de práctica; según un extracto): https://docs.frappe.io/hr/salary-structure"
  - "Ley de Contrato de Trabajo 20.744, texto actualizado con la Ley 27.802, InfoLEG (arts. 123, 156, 162, 231 a 233, 245 y 276): https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm"
  - "Ley 27.802 de Modernización Laboral, Boletín Oficial del 6/03/2026 (art. 54, que sustituye el art. 276 LCT): https://www.boletinoficial.gob.ar/detalleAviso/primera/339128/20260306"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-cargas-y-fundamentos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-huecos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/argentina-laboral.md (2026-11-27)"
aliases: [liquidación final, liquidación por baja, liquidación por egreso, finiquito, final pay, final settlement, termination pay, vacaciones no gozadas, indemnización por despido, severance pay]
creado: 2026-11-27
revisado:
---

# Liquidación final

La liquidación final es la que se hace cuando termina la relación laboral: paga lo trabajado y no cobrado hasta el último día, la parte proporcional de los conceptos que se devengan por período, las vacaciones no gozadas y, según el motivo de la salida, el preaviso y la indemnización, y descuenta lo que el empleado deba.

Es una [liquidación fuera de ciclo](liquidacion-de-sueldos.md#liquidaciones-fuera-de-ciclo): rara vez coincide con el fin del período y no puede esperar. La dispara la baja del [legajo](../Legajo/ingreso-y-egreso.md#lo-que-cierra-la-baja), que trae la fecha y el motivo del egreso. Cómo se decide y se conduce una salida, y qué le pasa al equipo que queda, es de [rotación y salidas](../../Liderazgo-y-direccion/Gestion-de-personas/rotacion-y-salidas.md); acá se calcula lo que se paga.

> [!WARNING]
> Lo argentino de esta nota es ley y dinero, copia al 27 de noviembre de 2026, con una sola fuente por artículo (el Boletín Oficial e InfoLEG publican el mismo texto), y no reemplaza a un abogado laboralista ni a un liquidador de sueldos. El aviso completo sobre la Ley 27.802 y su impugnación judicial está en [liquidación en la Argentina](liquidacion-en-argentina.md).

## El plazo para pagarla

La OIT pide que, al terminar el contrato, «a final settlement of all wages due shall be effected within a reasonable period of time having regard to the terms of the contract» (Convenio 95, art. 12). No fija días: cada país pone su plazo. Es la única fuente agnóstica leída sobre el plazo.

## De qué está hecha

La liquidación final junta conceptos de tres clases. Cuáles aplican depende del motivo de la salida, que es un dato del legajo.

| Parte | Qué paga | Aplica |
|---|---|---|
| Lo trabajado | Los días del último período hasta la fecha de egreso, con el mismo cálculo [proporcional por días](conceptos-de-liquidacion.md#proporcionales-por-días) que un ingreso a mitad de mes | Siempre |
| Lo proporcional que se devenga por período | La parte de los conceptos que se pagan una o dos veces por año y que el empleado fue ganando (en la Argentina, el aguinaldo del semestre) | Siempre, donde exista el concepto |
| Las vacaciones no gozadas | Los días de vacaciones ganados y no tomados, que ya no se pueden gozar | Siempre, donde la ley lo pida |
| El preaviso no dado | Los sueldos del plazo de aviso que la ley exige, si se despidió sin avisar | Despido sin preaviso |
| La indemnización | Una reparación por el fin de la relación, calculada sobre la antigüedad y el sueldo | Según el motivo: típicamente el despido sin causa |

La división en partes es criterio de esta base y sigue la ley argentina, la única leída con detalle. Las fuentes agnósticas confirman que estos conceptos existen como pagos: el IRS cuenta entre los pagos suplementarios el pago de licencias acumuladas y las indemnizaciones, y un software abierto de nómina tiene en su estructura salarial un valor por día para pagar licencias no tomadas («Leave Encashment Amount Per Day»).

## Vacaciones no gozadas

El saldo sale de [licencias y ausencias](../Tiempo-y-asistencia/licencias-y-ausencias.md): los días devengados en el año hasta la fecha de egreso, menos los tomados. En la Argentina las vacaciones no son compensables en dinero salvo lo que dispone el art. 156 para la extinción del contrato (art. 162 LCT). Según ese art. 156, la indemnización por vacaciones no gozadas equivale al salario del período de descanso proporcional a la fracción del año trabajada (art. 156 LCT).

Un saldo de licencias bien llevado durante toda la relación es lo que hace este cálculo posible; si el saldo no se llevó, la liquidación final lo reconstruye a mano (inferencia de esta base).

## La indemnización como concepto

La indemnización por despido es un monto que la ley pone a cargo del empleador cuando termina la relación sin una causa que la justifique. Su cálculo suele combinar tres piezas: una base (un sueldo de referencia), un multiplicador (la antigüedad) y límites (un tope y un piso). Esta descripción es inferencia de esta base a partir del caso argentino.

> [!NOTE]
> Sin fuente todavía: la indemnización por despido como concepto general y comparado entre países (los convenios de la OIT sobre terminación no se leyeron).

En la Argentina es la del art. 245 de la LCT, sustituido por la Ley 27.802: «un (1) mes de sueldo por cada año de servicio o fracción mayor de tres (3) meses», sobre la mejor remuneración mensual, normal y habitual del último año, con tope y piso. Es la misma cifra que da [rotación y salidas](../../Liderazgo-y-direccion/Gestion-de-personas/rotacion-y-salidas.md#el-límite-legal-en-argentina); la base, el tope, el piso, el preaviso y la integración del mes están en [liquidación en la Argentina](liquidacion-en-argentina.md#la-liquidación-final-en-la-argentina).

Para la liquidación, la base de la indemnización es otra base más: cada [concepto](conceptos-de-liquidacion.md#remunerativo-y-no-remunerativo) lleva una marca que dice si entra. En la Argentina, por ejemplo, el aguinaldo y las vacaciones no entran (art. 245).

## Lo que se descuenta

De la liquidación final salen las deducciones de siempre (aportes y retención sobre los conceptos que las llevan) y, como inferencia de esta base, lo pendiente del empleado: el saldo de un préstamo o un adelanto no recuperado. Si el tope de deducciones alcanza para descontar todo depende de la ley de cada país; esta base supone, sin fuente que lo trate para la baja, que en la Argentina rige también el tope del art. 133, en [liquidación en la Argentina](liquidacion-en-argentina.md#adelantos-deducciones-y-embargos). Como inferencia de esta base, un embargo vigente se aplica también a la liquidación final, según lo que la ley de cada país cuente como sueldo para el embargo ([conceptos de liquidación](conceptos-de-liquidacion.md#adelantos-préstamos-y-embargos)).

Cada parte va al [recibo de sueldo](recibo-de-sueldo.md) como un concepto separado, porque cada una tiene un tratamiento distinto frente a las [cargas](../Cargas-y-declaraciones/aportes-y-contribuciones.md) y la [retención](../Cargas-y-declaraciones/retencion-de-impuestos-sobre-sueldos.md).

## Cómo falla

- **Usar el motivo equivocado.** Una renuncia cargada como despido paga una indemnización que no correspondía, y al revés.
- **Saldo de vacaciones mal llevado.** Se pagan días ya tomados o se omiten días ganados.
- **Liquidar tarde.** Los créditos laborales vencidos se actualizan; en la Argentina, por IPC más 3 % anual (art. 276 LCT).
- **Mezclar todo en un solo concepto.** Sin separación, no se puede aplicar a cada parte su tratamiento frente a aportes e impuesto.

Salvo la actualización del art. 276, son inferencia de esta base sobre el modelo.
