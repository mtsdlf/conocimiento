---
resumen: >-
  En un software de gestión, la deuda con cada cliente y con cada proveedor se modela como partidas. Cada comprobante deja una partida por vencimiento con su saldo pendiente, y cada cobro o pago deja una partida de signo contrario. Una aplicación registra cuánto de una cancela a la otra. El saldo de la cuenta corriente no se guarda aparte: es la suma de las partidas, y la antigüedad se calcula sobre las que siguen abiertas.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, Account y Patterns for Accounting (según el lector de la página): https://martinfowler.com/eaaDev/Account.html y https://www.martinfowler.com/eaaDev/AccountingNarrative.html"
  - "OASIS, UBL 2.1, UBL-CommonAggregateComponents-2.1.xsd (PaymentTerms) y UBL-Invoice-2.1.xsd: https://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd"
  - "OpenPeppol, BIS Billing 3.0, reglas BR-CO-16 y BR-CO-25: https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/BR-CO-25/"
  - "OpenPeppol, BIS Billing 3.0, cbc:DueDate y cac:PaymentTerms (según el lector de la página): https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-PaymentTerms/"
  - "ASC X9, IR 01-2022, ISO 20022 Remittance Content Market Guide (14/2/2022): https://eact.eu/Core/Images/EACT_PDFs/ISO-20022-Remittance-Content-Market-Guide-February-2022.pdf"
  - "European Payments Council, EPC115-06 SCT Inter-PSP Implementation Guidelines 2025 v1.0: https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2025-10/EPC115-06%20SCT%20Inter-PSP%20IG%202025%20V1.0.pdf"
  - "ISO 11649:2009, extracto público: https://cdn.standards.iteh.ai/samples/50649/a769e57fc5a34724bac3a5d18a2b8407/ISO-11649-2009.pdf"
  - "IAS 21 (NIC 21), párrafos 28 y 29, en una copia del texto IFRS alojada por una universidad: https://ktkt.uel.edu.vn/Resources/Docs/SubDomain/ktkt/VanBan/IAS/ias21_en.pdf"
  - "Documentación de un software de gestión para servicios públicos, Open-Item Versus Balance-Forward Accounting (como evidencia de práctica, según el lector de la página): https://docs.oracle.com/en/industries/energy-water/ccb/29011/ccb-user-guides/Topics/C1_03Finan_Open_Item_Versus_Balance_Forward_.html"
  - "Documentación de un ERP, partidas residuales (como evidencia de práctica, según el lector de la página): https://help.sap.com/saphelp_46c/helpdata/en/01/a9bba1455711d182b40000e829fbfe/content.htm"
  - "Glendale Community College, Chapter Four, Accounts Receivable, apunte de curso sobre un software contable (según el resumen del buscador): https://gcc.glendale.edu/ckloezem/Book/arbasics.doc"
  - "Documentación de un software de gestión para la construcción, resúmenes de cuenta (como evidencia de práctica, según el resumen del buscador): https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/statements"
  - "Software-de-gestion/.investigacion/modelo-de-la-deuda.md (2026-11-27)"
aliases: [cuenta corriente en el sistema, modelo de la deuda, partida abierta, partidas abiertas, open item, open items, saldo corriente, balance forward, vencimiento, due date, cuotas, installments, condición de pago, payment terms, aplicación, aplicación de pagos, imputación, application, allocation, desaplicar, compensación, netting, partida residual, residual item, remesa estructurada, structured remittance, referencia del acreedor, creditor reference, RF]
creado: 2026-11-27
revisado:
---

# Cuenta corriente y aplicación

En un software de gestión, la deuda con cada cliente y con cada proveedor se modela como partidas. Cada comprobante deja una partida por vencimiento con su saldo pendiente, y cada cobro o pago deja una partida de signo contrario. Una aplicación registra cuánto de una cancela a la otra. El saldo de la cuenta corriente no se guarda aparte: es la suma de las partidas, y la antigüedad se calcula sobre las que siguen abiertas.

La contabilidad ya dice qué es una cuenta corriente: el libro auxiliar de cada cliente y proveedor, cuya suma tiene que coincidir con la cuenta de control del mayor ([cuentas corrientes](../../Contabilidad/Registro/cuentas-corrientes.md)). La tesorería dice qué tarea es aplicar un cobro y qué casos aparecen ([aplicación de cobros](../../Tesoreria/Credito-y-cobranzas/aplicacion-de-cobros.md)). El modelo de datos que sostiene las dos cosas combina columnas: la partida es un [movimiento](registro-de-movimientos-y-dimensiones.md), su vencimiento es una [fecha](fechas-vigencias-y-cierre.md) y su importe lleva [moneda](cantidades-unidades-y-monedas.md).

## Partidas abiertas o saldo corriente

Hay dos maneras de llevar lo que debe un cliente, y la documentación de los productos las nombra como *open item* y *balance forward*. La tabla resume la documentación de un software de facturación de servicios públicos, según el lector de la página y no con su texto literal:

| Método | Cómo trata un cobro | Qué cuenta como deuda vencida |
|---|---|---|
| Partidas abiertas | se aplica a facturas y ajustes concretos | solo las partidas que no se cancelaron |
| Saldo corriente | no se asocia a una factura: baja el saldo | los débitos envejecen y el cobro cancela primero lo más viejo |

Según un apunte de curso sobre un software contable, leído por el resumen del buscador, con partidas abiertas «The invoice is considered an open item (invoice) until its balance is $0», y con saldo corriente «The balance is the amount due for the customer and is not listed by invoice number».

Las fuentes leídas no fijan un criterio general para elegir. En la documentación de un software de facturación de servicios públicos, el método se define por clase de cliente: saldo corriente para los residenciales, partidas abiertas para los industriales y comerciales. Otro producto deja aplicar los cobros por partidas y emitir el resumen de cuenta como saldo corriente, así que la palabra también puede referirse al formato del resumen. Todo esto es evidencia de práctica y de fuentes secundarias, leída por el lector de la página o por el resumen del buscador. El pasaje de un libro de texto de sistemas contables que defina los dos métodos no se encontró.

En lectura de esta base, un sistema para empresas que se facturan entre sí lleva partidas abiertas. Hay tres motivos, y cada uno está en otra nota de la base: la antigüedad se calcula por comprobante ([cuentas corrientes](../../Contabilidad/Registro/cuentas-corrientes.md#lo-que-un-registro-tiene-que-poder-hacer)), el cliente discute facturas concretas ([disputas y deducciones](../../Tesoreria/Credito-y-cobranzas/gestion-de-la-cobranza.md#disputas-y-deducciones)) y las retenciones se practican sobre facturas concretas. El saldo corriente sirve cuando se le factura lo mismo cada mes a muchos clientes chicos.

## Del comprobante a sus vencimientos

Una factura deja una partida por cada vencimiento. La [condición de pago](../../Tesoreria/Credito-y-cobranzas/credito-a-clientes.md#la-condición-de-pago-y-los-plazos-usuales) dice cuántas partidas, cuándo vence cada una y si hay descuento por pronto pago. Vive en las [condiciones comerciales](../../Relacion-con-clientes/Registro-del-cliente/condiciones-comerciales.md) del cliente y se copia al comprobante.

UBL 2.1 permite que una factura lleve varios juegos de condiciones de pago (`PaymentTerms`, cardinalidad 0..n en el esquema de la factura); la BIS Billing 3.0 de OpenPeppol, que implementa EN 16931, lo restringe a uno. Cada juego puede llevar:

- `PaymentDueDate`, «The due date for these payment terms», o `InstallmentDueDate`, el vencimiento de una cuota;
- `PaymentPercent` o `Amount`, la parte del total que cubre (si el total no se divide exacto, el centavo que sobra va a una de las cuotas, como en el reparto de [importes con moneda](cantidades-unidades-y-monedas.md#importes-con-moneda));
- `SettlementDiscountPercent`, `SettlementDiscountAmount` y `SettlementPeriod`, el descuento por pronto pago y su plazo;
- `PenaltySurchargePercent` y `PenaltyAmount`, el recargo por pagar después.

EN 16931, el modelo europeo, es más angosto. Tiene una sola fecha de vencimiento estructurada (BT-9) y las condiciones como texto libre (BT-20), y exige una de las dos si queda algo por pagar: «In case the Amount due for payment (BT-115) is positive, either the Payment due date (BT-9) or the Payment terms (BT-20) shall be present» (BR-CO-25). Lo que queda por pagar es el total con IVA, menos lo ya pagado, más el redondeo (BR-CO-16). En lectura de esta base, así viaja en la misma factura un anticipo cobrado antes de facturar.

En lectura de esta base, el sistema calcula los vencimientos al confirmar el comprobante y los guarda en las partidas, como pide [programación de pagos](../../Tesoreria/Pagos-a-proveedores/programacion-de-pagos.md#la-condición-de-pago-fija-dos-fechas) del lado de los proveedores. Si los recalculara cada vez a partir de la condición, un cambio en la ficha del cliente movería los vencimientos de facturas ya emitidas.

## El saldo es una suma, no un campo

Fowler lo dice para cualquier cuenta: «The value, or balance, of the Account is derived as the sum of all the Accounting Entrys». Permite guardar el saldo actual como caché, para no sumar cada vez, y reemplazar asientos viejos por uno consolidado, a costa de perder el detalle. Sus patrones no hablan de facturas ni de partidas abiertas. Aplicarlos a la cuenta corriente es lectura de esta base.

Con partidas, hay dos saldos y los dos se derivan:

- El saldo de una partida es su importe menos lo que se le aplicó.
- El saldo de la cuenta corriente es la suma de las partidas, abiertas o no.

Guardar el saldo de la cuenta en un campo que se actualiza por separado es la falla que [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md#saldo-calculado-saldo-guardado-o-los-dos) describe para cualquier saldo. La conciliación del [auxiliar contra su cuenta de control](../../Contabilidad/Control-interno/conciliaciones.md#el-auxiliar-contra-su-cuenta-de-control) es lo que la detecta.

## La aplicación como registro propio

La aplicación une una partida deudora (una factura, una nota de débito) con una acreedora (un cobro, una nota de crédito, un anticipo) por un importe y en una fecha. En lectura de esta base, conviene que sea un registro propio, con sus dos partidas, su importe, su fecha y su moneda, y no un campo «pagado» dentro de la factura. Ninguna fuente leída la formula como patrón de datos. La guía de remesas de ISO 20022 de X9 y la documentación de un ERP muestran el comportamiento que el registro tiene que sostener.

Con la aplicación como registro, los casos de [aplicación de cobros](../../Tesoreria/Credito-y-cobranzas/aplicacion-de-cobros.md#los-casos-que-el-sistema-tiene-que-prever) se vuelven reglas sobre los datos (lectura de esta base):

- El importe aplicado no supera el saldo de ninguna de las dos partidas.
- Un cobro que paga varias facturas son varias aplicaciones, y una factura pagada en cuotas recibe varias.
- Lo que sobra de un cobro queda como partida acreedora abierta, disponible para aplicarla después. No se pierde ni se aplica «a cuenta» del saldo.
- Desaplicar es anular la aplicación. El cobro y la factura quedan como estaban, con su saldo de vuelta.
- Una nota de crédito se aplica a la factura que corrige igual que un cobro, sin mover plata.
- Si la misma [parte](datos-maestros-y-partes.md#la-parte-persona-u-organización-con-roles) es cliente y proveedor, una aplicación puede unir una partida de cobrar con una de pagar. Es una compensación, y suele pedir un acuerdo y un permiso propio.

La documentación de un ERP muestra dos maneras de llevar un cobro parcial. En la primera, la factura y el cobro quedan abiertos y se cancelan juntos cuando la factura se salda. En la segunda, los dos se cancelan y nace una partida residual: «A residual item results when a payment is made for less than the actual amount outstanding», con referencia a la factura original. Con un registro de aplicación, la primera sale sola y la segunda no hace falta (lectura de esta base).

## La remesa estructurada permite aplicar sin intervención

Aplicar en forma automática depende de que el cobro diga qué cancela. La guía de X9 sobre el contenido de remesas en ISO 20022 lo pide así:

- «Structured data is strongly preferred to allow automation.»
- «Referred Document Information should always be provided. In most cases, this would be the invoice number and date.»
- Por cada documento referido, la remesa puede llevar el importe debido, el descuento aplicado, la nota de crédito, los impuestos y el importe remitido. Esos importes deberían sumar lo remitido «to fully explain the payment», aunque «there is no arithmetic check».
- Cuando la remesa viaja separada del pago, hace falta un dato que una las dos: «A linking identifier is a single pre-determined (known) piece of data that brings two transactions together for reconciliation».

La referencia del acreedor resuelve el caso en que el cliente no copia el número de factura. Quien factura genera una referencia y la imprime en el comprobante. Quien paga la devuelve en la transferencia, y el sistema la busca entre sus partidas. ISO 11649 define la referencia RF, «designed for use in an automated processing environment», con un dígito verificador para validarla. En las guías de la transferencia SEPA, la referencia del acreedor va en la información estructurada y, si su emisor figura como ISO, tiene que ser una RF. Esas guías no obligan al banco receptor a validar el dígito.

Una guía de Swift avisa que la información de remesa se trunca al pasar de un banco a otro, según el resumen del buscador. El sistema tiene que poder terminar en el caso que no se empareja: el cobro sin identificar de [aplicación de cobros](../../Tesoreria/Credito-y-cobranzas/aplicacion-de-cobros.md#el-cobro-sin-identificar).

## Moneda extranjera: la diferencia nace al aplicar

Una factura en dólares se registra al tipo de cambio de su fecha, y el cobro, al del día en que se cobra. La NIC 21 manda la diferencia a resultados: «When monetary items arise from a foreign currency transaction and there is a change in the exchange rate between the transaction date and the date of settlement, an exchange difference results» (párrafo 29). Si la factura se cobra en el mismo ejercicio, toda la diferencia va a ese ejercicio. Si pasa un cierre en el medio, cada ejercicio reconoce el cambio de su propio período. La norma completa está en [moneda extranjera](../../Contabilidad/Operaciones/moneda-extranjera.md).

Para el modelo, en lectura de esta base, la partida guarda el importe en la moneda de la operación y su equivalente en la moneda de la empresa ([cantidades, unidades y monedas](cantidades-unidades-y-monedas.md#importes-con-moneda)). La aplicación cancela en la moneda de la operación, y la diferencia en moneda de la empresa sale como un movimiento aparte, generado por la aplicación. Si la partida pasó por una reexpresión al cierre, la diferencia se mide desde el último importe reexpresado y no desde el original.

## Los impuestos que cancelan deuda: retenciones y percepciones

La [recaudación en la fuente](../../Impuestos/Recaudacion-en-la-fuente/recaudacion-en-la-fuente.md) cruza la cuenta corriente por los dos lados (lectura de esta base sobre esa nota):

- La percepción la calcula el [motor de impuestos](motor-de-impuestos.md) al facturar y es parte de lo que el cliente debe. Entra en la partida de la factura.
- La retención se practica al pagar. Quien paga entrega menos plata y un comprobante de retención, y la factura se cancela con las dos cosas. Para el modelo, el comprobante de retención es otra partida acreedora que se aplica a la factura, con su número y su régimen.

Del lado del cobro, la retención sufrida es un [pago a cuenta](../../Impuestos/Recaudacion-en-la-fuente/pagos-a-cuenta.md) de un impuesto propio, que la contabilidad lleva a una cuenta de impuestos y no a una pérdida. El momento en que cancela la factura (al recibir el certificado o al validarlo) sigue sin fuente, como dice [las retenciones sufridas](../../Tesoreria/Credito-y-cobranzas/aplicacion-de-cobros.md#las-retenciones-sufridas). El caso argentino está en [impuestos y cuenta corriente en la Argentina](impuestos-y-cuenta-corriente-en-argentina.md#el-recibo-y-la-orden-de-pago-con-retenciones).

## Vencida, morosa y con intereses

La antigüedad se calcula sobre el saldo de cada partida abierta y su vencimiento, no sobre la fecha de la factura. Así lo pide la [gestión de la cobranza](../../Tesoreria/Credito-y-cobranzas/gestion-de-la-cobranza.md) para saber a quién reclamar y la [previsión para incobrables](../../Contabilidad/Registro/cuentas-corrientes.md#la-antigüedad-de-saldos) para estimar lo que no se va a cobrar. Una factura en tres cuotas puede tener una vencida, una por vencer y una cobrada.

El interés por mora nace del vencimiento de una partida y del tiempo que pasa sin cancelarla. La regla europea que lo fija sin necesidad de reclamo está en [lo que dice la ley europea sobre plazos y mora](../../Tesoreria/Credito-y-cobranzas/credito-a-clientes.md#lo-que-dice-la-ley-europea-sobre-plazos-y-mora). La documentación de un ERP calcula el interés sobre partidas abiertas o ya canceladas, desde el vencimiento neto, según el resumen del buscador. En lectura de esta base, el interés se registra como una partida nueva, una nota de débito con referencia a la partida que lo generó, y no como un aumento de la factura original.

## Cómo falla el modelo

- Aplicar a cuenta. El cobro baja el saldo y no cancela ninguna partida: la antigüedad sigue mostrando deuda vieja.
- El saldo en un campo. Se actualiza por un camino y las partidas por otro, y la cuenta corriente deja de coincidir con su control.
- Editar el cobro para corregir una aplicación. Se pierde qué se había aplicado y cuándo; desaplicar y volver a aplicar deja el rastro.
- Vencimientos recalculados. Un cambio en la condición de pago del cliente mueve los vencimientos de facturas viejas.
- Notas de crédito sueltas. Si solo los cobros se pueden aplicar, la nota de crédito queda como saldo a favor y la factura que corrige sigue vencida.
- Diferencia de cambio sin registro. Se aplica en dólares y nadie mide la diferencia en pesos, que aparece después como un descuadre del auxiliar.

Las seis son lectura de esta base: ninguna fuente leída enumera las fallas del modelo.

Para leer más: el esquema `UBL-CommonAggregateComponents-2.1.xsd`, en el tipo `PaymentTermsType`, para ver todo lo que puede llevar un vencimiento; y la guía de X9 IR 01-2022, en el grupo de importes del documento referido, por los ejemplos de un pago que cubre una factura y una nota de crédito.
