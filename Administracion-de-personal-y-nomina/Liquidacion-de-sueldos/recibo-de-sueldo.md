---
resumen: >-
  El recibo de sueldo es el comprobante que el empleador le entrega al empleado en cada pago, con el detalle de lo que liquidó en el período: cada concepto con su base y su monto, el bruto, las deducciones y el neto. Con él, el empleado controla su sueldo y el empleador prueba qué pagó.
estado: borrador
estabilidad: estable
fuentes:
  - "OIT, Convenio sobre la protección del salario, 1949 (núm. 95), arts. 14 y 15 (copia de la Universidad de Minnesota): https://hrlibrary.umn.edu/instree/ilo95.html"
  - "GOV.UK, Payslips (ejemplo de país): https://www.gov.uk/payslips"
  - "GOV.UK, Make debt deductions from an employee's pay, sección Making payments: https://www.gov.uk/debt-deductions-from-employee-pay/print"
  - "Ley de Contrato de Trabajo 20.744, texto actualizado con la Ley 27.802, InfoLEG (arts. 138 y 139): https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm"
  - "Martin Fowler, Temporal Patterns, Time Narrative (según un extracto): https://martinfowler.com/eaaDev/timeNarrative.html"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-cargas-y-fundamentos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-huecos.md (2026-11-27)"
aliases: [recibo de haberes, recibo de sueldo, boleta de pago, colilla de pago, nómina (documento), payslip, pay stub, pay slip, recibo digital]
creado: 2026-11-27
revisado:
---

# Recibo de sueldo

El recibo de sueldo es el comprobante que el empleador le entrega al empleado en cada pago, con el detalle de lo que liquidó en el período: cada concepto con su base y su monto, el bruto, las deducciones y el neto. Con él, el empleado controla su sueldo y el empleador prueba qué pagó.

Es la salida visible de la [liquidación de sueldos](liquidacion-de-sueldos.md): una línea por cada [concepto de liquidación](conceptos-de-liquidacion.md) que tocó al empleado en el período. Los recibos de un período forman el [libro de sueldos](../Cargas-y-declaraciones/libro-de-sueldos.md) donde la ley lo exige (en la Argentina dejó de exigirse con la Ley 27.802; ver [libro de sueldos digital](../Cargas-y-declaraciones/libro-de-sueldos-digital.md)), y los mismos importes alimentan la declaración de [cargas](../Cargas-y-declaraciones/cargas-y-declaraciones.md).

## Lo que pide la OIT y lo que pide un país

La norma internacional pide información y deja el formato a cada país. El Convenio 95 de la OIT obliga a informar a los trabajadores «in an appropriate and easily understandable manner», antes de empezar y cuando cambien, de sus condiciones salariales, y «at the time of each payment of wages, of the particulars of their wages for the pay period concerned, in so far as such particulars may be subject to change» (art. 14). También pide registros adecuados «in an approved form and manner» (art. 15).

Cada país baja eso a un contenido mínimo. En el ejemplo del Reino Unido, el recibo tiene que mostrar:

- lo ganado antes y después de las deducciones;
- las deducciones que cambian en cada pago, como el impuesto y los aportes;
- las horas trabajadas, si el pago depende de ellas;
- las deducciones fijas, como la cuota de un préstamo, en el recibo o en una declaración aparte que se entrega antes del primer recibo y se actualiza cada año.

Además, un descuento por una orden de embargo se notifica por escrito con el recibo de cada pago. El recibo argentino pide bastante más (CUIT y CUIL, categoría, antigüedad, las contribuciones del empleador y un resumen del costo laboral) y está en [liquidación en la Argentina](liquidacion-en-argentina.md#el-recibo-de-la-lct).

## Las partes de un recibo

Si se juntan la OIT, el ejemplo británico y el argentino, un recibo tiene cuatro bloques. La agrupación es criterio de esta base; el bloque de contribuciones es obligatorio en la Argentina y no figura en lo leído del Reino Unido.

| Bloque | Qué lleva |
|---|---|
| Identificación | Empleador, empleado, período de liquidación, fecha de pago, categoría o puesto |
| Haberes | Cada concepto que suma, con su base o cantidad (horas, días) y su monto; el total bruto |
| Deducciones | Aportes, retención de impuestos, embargos, adelantos y préstamos; el neto, que es lo que se acredita |
| Contribuciones del empleador | Lo que el empleador paga a terceros por ese sueldo, cuando la ley lo pide |

El cálculo se controla cuando cada concepto muestra su base o su cantidad además del monto: «hora extra 50 %, 6 horas» se puede revisar; «hora extra 48.000», no.

## Cuándo y cómo se entrega

En el Reino Unido, el empleador elige si el recibo es impreso o electrónico («printed or electronic (online) payslips») y tiene que darlo en el día de pago o antes. No se exige para contratistas ni trabajadores independientes. La Argentina admite el recibo firmado de manera digital o electrónica (art. 139 de la LCT, en [liquidación en la Argentina](liquidacion-en-argentina.md#el-recibo-de-la-lct)).

## La conformidad del empleado

En la Argentina el empleado firma el recibo como constancia de que cobró (art. 138 LCT). La OIT no lo exige en el art. 14, y ninguna fuente agnóstica leída trata la firma ni qué vale una firma «en disconformidad».

> [!NOTE]
> Sin fuente todavía: la firma o conformidad del recibo como práctica general, y su valor de prueba fuera de la Argentina.

## Un recibo emitido no se corrige

Como criterio de esta base, un recibo entregado ya probó un pago y ya se declaró. Si después aparece un error o un aumento con fecha pasada, la corrección va en líneas nuevas del recibo del período abierto, que dicen a qué período corresponden. Como inferencia de esta base, también puede ir en un recibo propio. Fowler dice lo mismo de cualquier registro: las correcciones son entradas nuevas y no ediciones. El procedimiento está en [retroactivos y reliquidaciones](retroactivos-y-reliquidaciones.md).

Como inferencia de esta base, un sistema guarda el recibo tal como se emitió, con los importes y los textos de cada concepto, en lugar de regenerarlo desde los datos actuales. Si el concepto cambió de nombre o de fórmula, el recibo de marzo tiene que seguir diciendo lo que dijo en marzo. El plazo de conservación depende de cada país; en la Argentina, en [liquidación en la Argentina](liquidacion-en-argentina.md#el-recibo-de-la-lct).
