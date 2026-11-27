---
resumen: >-
  Los medios de cobro y pago son los caminos por los que la plata entra y sale de las cuentas (transferencia, cheque, débito directo, tarjeta y efectivo); vistos desde la caja, cada uno se distingue por quién lo inicia, cuándo se acredita, cuánto cuesta y quién lo puede revertir.
estado: borrador
estabilidad: semi
fuentes:
  - "AFP, 2026 Payments Fraud and Control Survey Report: Key Highlights (abril de 2026; 465 profesionales; datos de 2025), pp. 5 y 11 (leído el resumen público): https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf"
  - "FBI IC3, 2025 Internet Crime Report, proceso de congelamiento de fondos (leído en las partes citadas): https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf"
  - "APQC, Process Classification Framework 7.4 (2024), 9.6.3 y 9.7.2.3 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Wikipedia, Positive pay (según su resumen; artículo con aviso propio): https://en.wikipedia.org/wiki/Positive_pay"
  - "Wikipedia, Float (money supply) (según su resumen): https://en.wikipedia.org/wiki/Float_(money_supply)"
  - "Odoo 18, documentación de pagos por lotes (como evidencia de práctica): https://www.odoo.com/documentation/18.0/applications/finance/accounting/payments/batch.html"
  - "BCRA, texto ordenado Transferencias – Normas complementarias, al 08/09/2026, sección 3.4 (leído), solo para la definición de transferencia pull: https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-tr-nc.pdf"
  - "Tesoreria/.investigacion/pagos-a-proveedores.md, secciones 2 y 3 (2026-11-27)"
  - "Tesoreria/.investigacion/argentina.md, secciones 1 y 2, solo lo general (2026-11-27)"
aliases: [medios de cobro, medios de pago, medios de cobro y pago, payment methods, payment instruments, payment rails, transferencia, cheque, débito directo, direct debit, positive pay]
creado: 2026-11-27
revisado:
---

# Medios de cobro y pago

Los medios de cobro y pago son los caminos por los que la plata entra y sale de las cuentas (transferencia, cheque, débito directo, tarjeta y efectivo); vistos desde la caja, cada uno se distingue por quién lo inicia, cuándo se acredita, cuánto cuesta y quién lo puede revertir.

Son los mismos rieles vistos de dos lados: la transferencia que la empresa recibe de un cliente es la que el cliente envía. Por eso esta base los trata en una sola nota, dentro de [Caja y liquidez](caja-y-liquidez.md), que es donde pesa cuándo llega la plata. El medio decide qué aparece como en tránsito en la [posición de caja](posicion-de-caja.md) y en qué semana cae cada cobro en la [proyección de caja](proyeccion-de-caja.md).

## Las cuatro preguntas a cada medio

Por lectura de esta base, a cada medio se le hacen cuatro preguntas:

1. Quién lo inicia. En un medio de empuje (push) el que paga manda la plata: transferencia, cheque, efectivo. En uno de tiro (pull) el que cobra la pide y el que paga la autoriza: débito directo, tarjeta. La norma argentina usa esos nombres y define la transferencia pull como la que acredita los fondos «mediante el débito de la cuenta del cliente receptor de la solicitud y luego de que éste la haya autorizado».
2. Cuándo está la plata. Entre que el medio se usa y la plata se puede usar pasa la flotación, que puede ser de segundos o de días.
3. Cuánto cuesta. Una comisión fija, un porcentaje del monto o el costo de esperar.
4. Quién lo puede revertir. Un cheque se rechaza, un débito directo se desconoce, una tarjeta se contracarga; una transferencia ya acreditada, en general, solo vuelve si el que la recibió la devuelve.

La tabla resume las respuestas. Es lectura de esta base sobre las fuentes de cada sección, con los huecos marcados abajo.

| Medio | Quién lo inicia | Cuándo está la plata | Quién lo puede revertir |
|---|---|---|---|
| Transferencia | El que paga | Al instante o al día siguiente, según el sistema del país | Casi nadie, una vez acreditada |
| Cheque | El que paga lo emite; el que cobra lo deposita | Días después del depósito, cuando se compensa | El banco del que paga, si lo rechaza |
| Débito directo | El que cobra, con autorización previa | En la fecha del débito | El que paga, si lo desconoce |
| Tarjeta | El que cobra, con los datos del que paga | Según el plazo pactado con el procesador | El que paga, por un contracargo |
| Efectivo | El que paga | Al recibirlo; en el banco, al depositarlo | Nadie |

> [!NOTE] Sin fuente todavía: una fuente general y abierta sobre plazos de acreditación y reversión del débito directo y del efectivo. Lo de cada medio en la Argentina está leído en las normas del BCRA y va en [tesorería en Argentina](../tesoreria-en-argentina.md).

## El cheque, lento y todavía en uso

El cheque es el medio con más fraude según la encuesta y, por lectura de esta base, el de más flotación, y no desaparece. En la encuesta de la AFP de 2026 a 465 profesionales de Estados Unidos, «87% of organizations report using checks in 2025», y «68% of companies use checks for vendor payments because vendors require payment via checks». El 72 % planea seguir usándolos, pero entre quienes los usan, el 72 % dice que son el 25 % o menos de sus pagos.

El fraude se concentra ahí: el 58 % de las organizaciones que sufrieron fraude de pagos lo sufrió con cheques, y la encuesta dice que «Mail-theft-enabled check fraud is a large persistent problem». El control habitual es el positive pay: según el resumen de un artículo de referencia, la empresa le pasa al banco la lista de cheques emitidos y el banco paga solo los que coinciden en número, monto y beneficiario.

Para la caja, el cheque tiene dos tiempos: cuando se emite o se recibe, y cuando se compensa. Entre los dos está la flotación, que se explica en [posición de caja](posicion-de-caja.md). En la Argentina el cheque es además crédito y se puede descontar, y existe el cheque electrónico; está en [tesorería en Argentina](../tesoreria-en-argentina.md).

## Transferencias y archivos al banco

APQC le da un subproceso propio a la transferencia electrónica dentro de la gestión de caja: 9.7.2.3, «Process and oversee electronic fund transfers (EFTs)». Para pagar a muchos proveedores, los sistemas de gestión arman un lote y generan un archivo con un formato que depende de la región; la documentación de un sistema abierto nombra SEPA en Europa, NACHA en Estados Unidos e ISO 20022 como estándar internacional. El banco debita el lote como un solo movimiento, y la conciliación lo reparte entre los pagos. Cómo se arma y se aprueba el lote está en [corrida de pagos](../Pagos-a-proveedores/corrida-de-pagos.md).

La transferencia es rápida y casi irreversible, y por lectura de esta base eso la vuelve el blanco de los engaños por cambio de cuenta del proveedor (ver [seguridad de los pagos](../Pagos-a-proveedores/seguridad-de-los-pagos.md)). Recuperar plata enviada al exterior es un proceso aparte: en el informe del FBI de 2025, el proceso de congelamiento de fondos registró 3.574 incidentes nacionales y 326 internacionales, con 507.042.623 y 171.970.560 dólares congelados.

## Débito directo y pedidos de pago

En el débito directo la empresa que cobra le pide al banco del cliente que debite la cuenta, con una autorización que el cliente dio antes. Para quien cobra, la ventaja es que la fecha la elige él y la proyección acierta más; el riesgo es que el cliente lo desconozca después (lectura de esta base). La encuesta de la AFP registra los débitos automáticos de Estados Unidos (ACH) como el segundo medio con más fraude, en el 30 % de las organizaciones que lo sufrieron.

> [!NOTE] Sin fuente todavía: plazos y reglas generales de reversión del débito directo. La norma argentina de débito inmediato no se leyó.

## Tarjeta, billeteras y QR

Cobrar con tarjeta, billetera o QR lo explica Comercio electrónico: quién interviene y cuánto cuesta en [Pagos](../../Comercio-electronico/Pagos/pagos.md) y [costo de cobrar](../../Comercio-electronico/Pagos/costo-de-cobrar.md), los medios de la región en [medios de pago locales](../../Comercio-electronico/Pagos/medios-de-pago-locales.md) y el contracargo en [fraude y contracargos](../../Comercio-electronico/Pagos/fraude-y-contracargos.md). Lo que importa a la caja es una distinción de allá: acreditado no es disponible, y cobrar antes cuesta más.

Del lado del pago, la tarjeta corporativa es un medio para gastos chicos. APQC la gestiona en 9.6.3, «Manage corporate credit cards», con políticas y límites, emisión, cambio de límites y cancelación. En la encuesta de la AFP aparece en el 21 % de las organizaciones con fraude.

## Efectivo

> [!NOTE] Sin fuente todavía: el efectivo visto desde la tesorería (arqueo, fondo fijo, depósito y su costo de traslado y seguridad). El fondo fijo de gastos menores, si está, es de la contabilidad.

## Cómo se modela en un sistema

Por lectura de esta base, el medio es un atributo de cada cobro y cada pago, y de él dependen otros datos que la caja necesita:

- la fecha esperada de acreditación o débito, que alimenta lo en tránsito de la posición y la semana de la proyección;
- un estado que sigue al medio (emitido, entregado, depositado, acreditado, rechazado), porque un cheque rechazado tiene que volver a la cuenta del cliente;
- el costo, fijo o porcentual, que se registra como gasto bancario;
- la cuenta bancaria por la que entra o sale.

La ficha del cliente puede guardar el medio habitual entre sus [condiciones comerciales](../../Relacion-con-clientes/Registro-del-cliente/condiciones-comerciales.md).

## Cómo falla

La encuesta de la AFP mide qué medios sufrieron fraude en 2025, como porcentaje de las organizaciones que tuvieron fraude y no como tasa por operación: cheques 58 %, débitos ACH (la cámara de pagos electrónicos de Estados Unidos) 30 %, transferencias 25 %, tarjetas corporativas 21 %, créditos ACH 18 %, billeteras móviles 2 %, pagos rápidos 1 % y criptomonedas 1 %. Las otras fallas son de caja, por lectura de esta base: contar un cheque depositado como plata antes de que se compense, proyectar un cobro con tarjeta en la fecha de la venta y no en la del plazo pactado, y no registrar el costo del medio hasta que aparece en el extracto.
