---
resumen: >-
  El pago de sueldos es la parte de la tesorería que hace llegar el neto de cada liquidación a la cuenta de cada empleado el día que corresponde: tener la plata en la cuenta de la empresa a tiempo, mandar el lote al banco, verificar que se acreditó y prever en la caja las cargas que vencen después.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 7.5.4, 9.5.2.5, 9.5.3.3 y 9.7.2 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "OIT, Convenio 95 sobre la protección del salario (1949), art. 12, copia de la Universidad de Minnesota (leído): https://hrlibrary.umn.edu/instree/ilo95.html"
  - "OpenStax, Principles of Financial Accounting, 12.5, nómina (leído): https://openstax.org/books/principles-financial-accounting/pages/12-5-record-transactions-incurred-in-preparing-payroll"
  - "CFPB, opinión consultiva Non-application to Earned Wage Access Products (Federal Register 2025-23735, 23/12/2025), nota 3 (leída): https://www.federalregister.gov/documents/2025/12/23/2025-23735/truth-in-lending-regulation-z-non-application-to-earned-wage-access-products"
  - "Tesoreria/.investigacion/pago-de-sueldos.md (2026-11-27)"
aliases: [pago de sueldos, pago de la nómina, pago de haberes, payroll payment, payroll disbursement, paying payroll, pago de salarios, acreditación de sueldos]
creado: 2026-11-27
revisado:
---

# Pago de sueldos

El pago de sueldos es la parte de la tesorería que hace llegar el neto de cada liquidación a la cuenta de cada empleado el día que corresponde: tener la plata en la cuenta de la empresa a tiempo, mandar el lote al banco, verificar que se acreditó y prever en la caja las cargas que vencen después.

Empieza donde termina la [liquidación de sueldos](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-de-sueldos.md): un lote cerrado que dice cuánto cobra cada uno. La liquidación es dueña del cálculo, del [recibo](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/recibo-de-sueldo.md) y de las reglas sobre el medio de pago que fija la ley; acá se ejecuta el pago. Es el paso 6 del recorrido [de la contratación a la baja](../../Procesos-de-negocio/de-la-contratacion-a-la-baja.md), entre el lote cerrado y la conciliación del extracto, que hace [Contabilidad](../../Contabilidad/Control-interno/conciliaciones.md).

APQC hace el mismo corte. Pone «Process and distribute payments» en la nómina (9.5.2.5) y el movimiento de fondos, la proyección y la relación con los bancos en la tesorería (9.7.2.3, 9.7.2.4 y 9.7.2.7).

## En qué se diferencia de pagar a un proveedor

El sueldo sale por los mismos rieles que el pago a un proveedor, la transferencia en lote de [medios de cobro y pago](../Caja-y-liquidez/medios-de-cobro-y-pago.md#transferencias-y-archivos-al-banco). Lo que cambia es cuánto decide la tesorería:

| | Pago a proveedores | Pago de sueldos |
|---|---|---|
| La fecha | La elige la tesorería entre el vencimiento y el descuento ([programación de pagos](../Pagos-a-proveedores/programacion-de-pagos.md)) | La fija la ley o el convenio, y es la misma para todos |
| Si la caja no alcanza | Se renegocia o se estira | No se estira: el salario tiene protección propia ([fondeo y calendario](fondeo-y-calendario.md#cuando-la-plata-no-alcanza)) |
| A quién | Pocos pagos grandes, a empresas | Muchos pagos chicos, a personas |
| El medio | Lo acuerdan las partes | Lo limita la ley ([el pago de sueldos](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-de-sueldos.md#el-pago-de-sueldos), según el Convenio 95 de la OIT) |
| La cuenta destino | La de la ficha del proveedor | La del legajo del empleado, que la elige él |

Cada pago de sueldos son dos salidas con fechas distintas, en lectura de esta base sobre OpenStax (12.5) y las reglas de depósito de cargas: el neto, el día de pago, y lo retenido más las contribuciones, en el vencimiento de cada organismo. La segunda es plata de terceros que la empresa tiene en su cuenta hasta esa fecha.

## El ciclo de cada pago

1. Lote cerrado. La liquidación entrega el total de netos y, por cada empleado, su cuenta y su importe.
2. Fondeo. La tesorería deja la plata en la cuenta de la que sale el pago, antes de la hora de corte del banco ([fondeo y calendario](fondeo-y-calendario.md)).
3. Archivo y control. Se genera el archivo del banco y se compara su suma con el total de netos, y cada cuenta con la del legajo ([cuentas y acreditación](cuentas-y-acreditacion.md)).
4. Liberación. Alguien distinto de quien liquidó libera el lote en el banco (lectura de esta base), con las firmas que pida la [política de tesorería](../politica-de-tesoreria.md).
5. Acreditación. El banco reparte el lote; las cuentas que no existen o están cerradas vuelven como rechazos.
6. Verificación. Se compara lo debitado con lo enviado, se paga de nuevo lo rechazado y el extracto pasa a la conciliación.
7. Cargas. Las retenciones y contribuciones del período salen en su propio vencimiento.

Los pasos 3 y 4 vienen del traspaso «lote a Tesorería» del recorrido, donde la suma del archivo tiene que coincidir con el total de netos y cada cuenta con la del legajo. La separación entre quien liquida y quien libera no tiene fuente con método leída: APQC separa los dos actos, pero no dice que tengan que hacerlos personas distintas.

## Por qué el día de pago es fijo

El Convenio 95 de la OIT pide que el salario se pague «regularly», a intervalos que fijen la ley, el convenio o el laudo (art. 12). La frecuencia (semanal, quincenal, mensual) la decide cada país y cada convenio, y su lado legal está en [frecuencias y período de liquidación](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-de-sueldos.md#frecuencias-y-período-de-liquidación).

La frecuencia también le cuesta a la caja. La CFPB, el regulador financiero de consumidores de Estados Unidos, recuerda que el pago periódico responde a la eficiencia de procesar la nómina y al «employers' cash management», y que pagar más seguido choca con «additional costs in both time and money to run payroll more frequently, cash flow limitations, and inertia» (opinión de diciembre de 2025, nota 3). En lectura de esta base, el empleador que paga una vez por mes usa el trabajo del mes antes de pagarlo, y el pago a demanda que se describe en [fondeo y calendario](fondeo-y-calendario.md#el-pago-a-demanda) es la respuesta del mercado a ese desfase.

## Cómo falla el pago de sueldos

- **La plata llega tarde al banco.** El archivo pasa la hora de corte y espera la ventana siguiente: el sueldo se acredita tarde, o sale por el carril del mismo día con su tope ([fondeo y calendario](fondeo-y-calendario.md#cuándo-tiene-que-estar-la-plata)).
- **Un sueldo va a una cuenta ajena.** Alguien cambió la cuenta del empleado con un correo falso o con su contraseña robada ([cuentas y acreditación](cuentas-y-acreditacion.md#el-desvío-de-sueldos)).
- **El archivo no es el lote.** Se agrega o se cambia una línea después de aprobar, o se paga a un empleado que ya no está; la defensa es comparar el archivo con el lote cerrado.
- **Se olvidan las cargas.** La proyección muestra el neto y no las retenciones, que vencen días después y son plata de terceros ([fondeo y calendario](fondeo-y-calendario.md#las-cargas-tienen-su-propio-calendario)).

## Qué hay adentro del pago de sueldos

- [Cuentas y acreditación](cuentas-y-acreditacion.md): la cuenta de la empresa de la que sale el sueldo, la cuenta del empleado, el archivo, cuándo tiene la plata el empleado, los rechazos y las reversas, y el desvío de sueldos.
- [Fondeo y calendario](fondeo-y-calendario.md): cuándo tiene que estar la plata, el calendario del año con los pagos extraordinarios y las cargas, qué pasa si no alcanza y el pago a demanda.
- [Pago de sueldos en Argentina](pago-de-sueldos-en-argentina.md): la cuenta sueldo del BCRA, el lote que se cobra al día siguiente, lo que cobra el banco, el calendario de la LCT y de ARCA, y la mora.
