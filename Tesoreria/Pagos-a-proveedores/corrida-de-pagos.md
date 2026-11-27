---
resumen: >-
  La corrida de pagos es el ciclo periódico en que la empresa junta las facturas programadas, las aprueba, arma con ellas un lote por medio de pago y banco, lo manda al banco y después verifica que cada pago salió.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 9.6.1 y 9.7.2.3 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Documentación de pagos por lotes de un sistema de gestión abierto, versión 18 (leído; como evidencia de práctica): https://www.odoo.com/documentation/18.0/applications/finance/accounting/payments/batch.html"
  - "Documentación del registro de pagos de otro sistema de gestión abierto (leído; como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/payment-entry"
  - "Wikipedia, Two-person rule (según su resumen; fuente terciaria): https://en.wikipedia.org/wiki/Four-eyes_principle"
  - "EPC, SEPA Credit Transfer Scheme Customer-to-PSP Implementation Guidelines, EPC132-08, versión 1.0 (emitida el 28/11/2024, vigente desde el 5/10/2025) (leído en la introducción y el índice): https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2025-10/EPC132-08%20SCT%20C2PSP%20IG%202025%20V1.0.pdf"
  - "BCRA, Texto ordenado Reglamentación de la cuenta corriente bancaria (al 4/6/2026), 12.2 (leído): https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-ctacte.pdf"
  - "Tesoreria/.investigacion/pagos-a-proveedores.md, secciones 2 y 5 (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 6 (2026-11-27)"
  - "Tesoreria/.investigacion/pagos-y-politica-verificacion.md (2026-11-27)"
aliases: [corrida de pagos, payment run, pago por lotes, batch payment, lote de pagos, propuesta de pagos, payment proposal, archivo de pagos, payment file, orden de pago, firma conjunta, doble firma, two-person rule, four-eyes principle]
creado: 2026-11-27
revisado:
---

# Corrida de pagos

La corrida de pagos es el ciclo periódico en que la empresa junta las facturas programadas, las aprueba, arma con ellas un lote por medio de pago y banco, lo manda al banco y después verifica que cada pago salió.

Recibe de la [programación de pagos](programacion-de-pagos.md) qué se paga y cuándo, y entrega plata que sale de una cuenta bancaria. Es el punto donde se encuentran cuentas a pagar y tesorería: APQC pone la corrida en cuentas a pagar (9.6.1) y el movimiento electrónico de fondos en tesorería (9.7.2.3). En una empresa chica la hace la misma persona de punta a punta, y por eso, como lectura de esta base, los controles de [seguridad de los pagos](seguridad-de-los-pagos.md) pesan más ahí.

## Los pasos de una corrida

Ninguna fuente leída define la corrida paso a paso. La lista que sigue es una síntesis de esta base sobre los procesos de APQC y la documentación de dos sistemas de gestión abiertos, y falta validarla con una guía profesional:

1. Propuesta. Se listan las facturas aprobadas que vencen, o que pierden el descuento, hasta la fecha de la próxima corrida, y se marcan las que se pagan.
2. Aprobación. Quien tiene la facultad revisa la propuesta y la aprueba, entera o con exclusiones.
3. Lote. Los pagos aprobados se agrupan por cuenta de origen y por medio de pago.
4. Archivo y envío. El lote se convierte en un archivo con el formato del banco y se sube al portal del banco o se manda por un canal directo.
5. Firma en el banco. Los firmantes de la cuenta liberan el lote en el banco.
6. Ejecución. El banco procesa cada pago y puede rechazar alguno.
7. Verificación. Se compara lo enviado con lo que el banco debitó, y cada pago ejecutado cancela su factura.

APQC respalda que aprobar, procesar y transferir sean actos distintos: tiene un código para aprobar pagos (9.6.1.4 «Approve payments»), otro para procesarlos (9.6.1.8 «Process payments») y otro, ya en tesorería, para procesar y supervisar las transferencias electrónicas (9.7.2.3). También pone, antes de todo, verificar el archivo de pagos contra el maestro de proveedores (9.6.1.1 «Verify AP pay file with purchase order vendor master file»).

## El lote y sus reglas

La documentación de los dos sistemas abiertos muestra reglas que se repiten. Sirven como evidencia de práctica y no como norma, y los motivos que se dan abajo son lectura de esta base:

- Un medio por lote. En uno de ellos, todos los pagos de un lote usan el mismo medio de pago y salen de la misma cuenta bancaria. El motivo es que cada medio termina en un archivo o un canal distinto del banco.
- El lote validado no se toca. Una vez validado no se le agregan pagos; antes de validarlo se puede borrar. Sirve para que nada entre al lote después de la aprobación.
- Un pago, un proveedor. En el otro sistema, un registro de pago puede cancelar varias facturas del mismo proveedor, pero no de varios proveedores, y lo aplicado no puede superar el monto disponible.
- Deducciones con su cuenta. Las retenciones, las comisiones bancarias y las diferencias de cambio que se descuentan del pago van en un campo aparte, cada una a su cuenta.
- Anticipos sin factura. Un pago adelantado al proveedor se registra antes de la factura y queda sin aplicar hasta que llega.

El formato del archivo depende de la región: según la documentación de uno de los sistemas, SEPA en Europa, NACHA en Estados Unidos e ISO 20022 como estándar mundial. ISO 20022 es un estándar de mensajes en XML. En las transferencias SEPA, la orden de pago que la empresa le manda a su banco es el mensaje *Customer Credit Transfer Initiation* (pain.001.001.09 en la guía del EPC de 2025). Qué medio conviene para cada pago, cuándo se acredita y cuánto cuesta, está en [medios de cobro y pago](../Caja-y-liquidez/medios-de-cobro-y-pago.md); los de Argentina, en [tesorería en Argentina](../tesoreria-en-argentina.md).

## Quién aprueba y quién firma

La aprobación de la corrida aplica la matriz de [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md) a los pagos: quién aprueba hasta qué monto, y que un pago sin factura aprobada no se pueda emitir. La [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md) pide que quien prepara la propuesta no sea quien firma en el banco, y que quien da de alta la cuenta bancaria de un proveedor no libere sus pagos. Esas dos notas son las dueñas de esos controles; acá se suma cómo se aplican al lote.

El doble control tiene nombre propio: la regla de las dos personas, que exige que dos personas autorizadas intervengan en una acción. Según el resumen de Wikipedia, algunos sistemas exigen que dos usuarios aprueben una transferencia antes de procesarla, y algunas empresas exigen dos firmas en los cheques. En la encuesta de AFP de 2026, la firma de la gerencia por encima de un umbral es uno de los controles más usados contra el fraude de pagos ([seguridad de los pagos](seguridad-de-los-pagos.md)). El umbral y los firmantes los fija la [política de tesorería](../politica-de-tesoreria.md); las firmas registradas en cada banco, la nota de [cuentas bancarias](../Caja-y-liquidez/cuentas-bancarias.md).

En Argentina, el texto ordenado del BCRA distingue dos regímenes para las cuentas corrientes especiales con varios titulares. En las cuentas a orden recíproca o indistinta, el banco acepta los cheques librados por cualquiera de los titulares (12.2.1). En las de orden conjunta o colectiva, solo acepta cheques firmados por todos (12.2.2). Es una sola fuente, y regula a los titulares de la cuenta; para una sociedad, el texto pide identificar a sus autoridades y autorizados (1.3.1) pero no fija montos ni esquemas de firma.

> [!NOTE] Sin fuente todavía: los montos y esquemas de firma de una empresa en la práctica bancaria, la orden de pago como documento interno que respalda cada pago, y la aprobación por niveles dentro de una misma corrida.

## Lo que el banco devuelve

El extracto del banco suele traer un solo débito por el total del lote. Según la documentación de uno de los sistemas abiertos, al conciliar ese débito se reparte entre los pagos que lo forman, y si el banco rechazó una línea, el pago se saca del lote antes de cerrar la conciliación. La conciliación bancaria es de Contabilidad ([conciliaciones](../../Contabilidad/Control-interno/conciliaciones.md)); para la tesorería, un pago rechazado vuelve a ser una deuda que vence y, por lectura de esta base, tiene que entrar en la próxima corrida.

Mientras el lote está enviado y no ejecutado, la plata sigue en la cuenta pero ya está comprometida. La [posición de caja](../Caja-y-liquidez/posicion-de-caja.md) tiene que mostrar ese saldo comprometido aparte del disponible (lectura de esta base).

## Cómo se modela en un sistema

Por inferencia de esta base, a partir de los pasos y las reglas de arriba, una corrida necesita al menos:

- Estados que solo avanzan (propuesta, aprobada, enviada, ejecutada, verificada), con quién y cuándo pasó cada uno.
- Una aprobación atada a la versión del lote: si se agrega, se saca o se cambia un pago después de aprobar, la aprobación cae.
- Un bloqueo sobre cada factura incluida, para que no entre en otra corrida mientras esta no termina; es la defensa más directa contra el pago duplicado, que [seguridad de los pagos](seguridad-de-los-pagos.md) trata sin fuente todavía.
- La cuenta bancaria del proveedor congelada en el pago al momento de aprobar, y no leída de la ficha al generar el archivo.

Cómo se modelan el documento de pago y sus estados es del tema Software de gestión, todavía no escrito; el recorrido completo de la compra al pago, del tema Procesos de negocio, también sin escribir.
