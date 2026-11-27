---
resumen: >-
  Pagos a proveedores es la parte de la tesorería que hace salir la plata que la empresa debe: toma la factura ya aprobada, decide cuándo pagarla, la paga en una corrida aprobada y cuida que el pago llegue a quien corresponde.
estado: vigente
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 9.6.1, 9.7.2 y 9.7.6 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "OpenStax, Principles of Finance (2022), 19.2 What Is Trade Credit? (leído): https://openstax.org/books/principles-finance/pages/19-2-what-is-trade-credit"
  - "FBI IC3, 2025 Internet Crime Report (leído en las partes citadas): https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf"
  - "AFP, 2026 Payments Fraud and Control Survey Report: Key Highlights (leído el resumen): https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf"
  - "Tesoreria/.investigacion/pagos-a-proveedores.md (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 6 (2026-11-27)"
aliases: [pagos a proveedores, pagos, accounts payable payments, vendor payments, supplier payments, de la factura al pago, invoice to pay]
creado: 2026-11-27
revisado: 2026-11-27
---

# Pagos a proveedores

Pagos a proveedores es la parte de la tesorería que hace salir la plata que la empresa debe: toma la factura ya aprobada, decide cuándo pagarla, la paga en una corrida aprobada y cuida que el pago llegue a quien corresponde.

Es el lado de salida de la [caja](../Caja-y-liquidez/caja-y-liquidez.md), como [crédito y cobranzas](../Credito-y-cobranzas/credito-y-cobranzas.md) es el de entrada. Cada pago que se programa baja la [posición de caja](../Caja-y-liquidez/posicion-de-caja.md) de una fecha y mueve la [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md). Si la proyección muestra que no alcanza, la vertical le pasa el problema a [financiamiento](../Financiamiento/financiamiento.md) o decide qué se demora. Todo lo gobierna la [política de tesorería](../politica-de-tesoreria.md), que fija quién aprueba, hasta qué monto y desde qué cuentas.

## De la factura aprobada al pago

La vertical empieza donde termina otra. Compras y abastecimiento, un tema todavía no escrito, pide la mercadería y la recibe; Contabilidad cruza la factura con el pedido y la recepción, y registra la deuda en [compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md). Desde ahí, la factura queda lista para pagar y empieza esta vertical, en tres pasos:

1. Programar. Se decide la fecha de pago de cada factura: el vencimiento que pactó el proveedor, antes si hay un descuento por pronto pago que conviene, o después si la caja no alcanza y se renegocia.
2. Correr. Las facturas que se pagan en la fecha se juntan en una propuesta, alguien con facultad la aprueba, se arma un lote por banco y medio de pago, y el banco lo ejecuta.
3. Cuidar. Antes y durante la corrida, se comprueba que cada pago va a la cuenta real del proveedor y que ninguna deuda se paga dos veces.

Después, la contabilidad registra el pago y lo concilia con el extracto en [conciliaciones](../../Contabilidad/Control-interno/conciliaciones.md). El recorrido completo, de la compra al pago, es del tema Procesos de negocio, todavía no escrito.

## Quién decide qué se paga

Compras decide que la factura se debe; la tesorería decide cuándo y cómo se paga. APQC no lo corta igual: pone aprobar y procesar pagos en cuentas a pagar (9.6.1.4 y 9.6.1.8) y deja en la tesorería las transferencias electrónicas (9.7.2.3), los flujos de caja (9.7.2.5) y los casos de fraude (9.7.6). Esta base pone el pago en la tesorería porque el mapa del área le dio el verbo pagar, y deja el registro en Contabilidad. En una empresa grande la frontera depende de cómo esté organizada; en una chica, la misma persona programa, corre y paga (lectura de esta base, sin fuente con método).

Que la misma persona haga todo es justo lo que la [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md) quiere evitar, y las [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md) dicen quién aprueba hasta qué monto. Esas dos notas son las dueñas de esos controles; esta vertical los aplica a la corrida.

## Cuánto cuesta pagar antes, a tiempo o tarde

El crédito del proveedor es plata que la empresa usa sin pagar interés mientras no venza, y por eso pagar antes de tiempo, sin un descuento a cambio, adelanta una salida de caja sin ganar nada. Cuando hay descuento, no tomarlo cuesta caro: con 2/10 neto 30, OpenStax calcula un costo anual de 36,73 %. Pagar tarde puede tener intereses o cargos pactados, y pagar a tiempo, según el mismo libro, ayuda a construir la historia crediticia de la empresa. La cuenta completa, con la versión capitalizada y otras condiciones, está en [programación de pagos](programacion-de-pagos.md).

## Cómo falla la salida de plata

La falla con más datos públicos es el pago que llega a una cuenta equivocada. El FBI recibió en 2025 denuncias por USD 3.046.598.558 de pérdidas por compromiso del correo empresarial, el engaño que cambia la cuenta bancaria de un proveedor real. En la encuesta de AFP de 2026, el 74 % de las organizaciones de Estados Unidos que respondieron fue blanco de ese engaño en 2025. Las otras fallas son el cheque robado o alterado, el pago duplicado y el pago que sale sin la aprobación que correspondía. Las cifras, los controles y lo que se hace cuando el pago ya salió están en [seguridad de los pagos](seguridad-de-los-pagos.md).

## Qué hay adentro de los pagos a proveedores

- [Programación de pagos](programacion-de-pagos.md): qué factura se paga en qué fecha, el costo de no tomar un descuento por pronto pago (la fórmula vive ahí) y las prioridades cuando la caja no alcanza.
- [Corrida de pagos](corrida-de-pagos.md): la propuesta, la aprobación, el lote, el archivo al banco, las firmas y cómo se modelan sus estados en un sistema.
- [Seguridad de los pagos](seguridad-de-los-pagos.md): el correo comprometido que cambia la cuenta del proveedor, el cheque, el pago duplicado y los controles con su eficacia según quienes los usan.

Los medios por los que sale la plata (transferencia, cheque, débito directo, tarjeta), cuándo se debitan y cuánto cuestan, están en [medios de cobro y pago](../Caja-y-liquidez/medios-de-cobro-y-pago.md); los de Argentina, como el cheque electrónico, en [tesorería en Argentina](../tesoreria-en-argentina.md).
