---
resumen: >-
  El motor de impuestos es la parte del software de gestión que decide, renglón por renglón, qué impuestos lleva un comprobante, sobre qué base y con qué alícuota. Lo decide con la categoría fiscal del artículo, la condición fiscal de la parte, el lugar y la fecha. Después junta los renglones por categoría y alícuota y redondea con una regla que fija la norma o, si la norma deja elegir, el diseño.
estado: borrador
estabilidad: estable
fuentes:
  - "OASIS, UBL 2.1, UBL-CommonAggregateComponents-2.1.xsd (TaxTotal, TaxSubtotal, TaxCategory): http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/common/UBL-CommonAggregateComponents-2.1.xsd"
  - "OpenPeppol, Peppol BIS Billing 3.0, §8 a §10 (implementación de EN 16931): https://docs.peppol.eu/poacc/billing/3.0/bis/"
  - "OpenPeppol, reglas de negocio de EN 16931 en UBL (BR-CO-04, BR-CO-14, BR-CO-17, BR-S-08): https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/"
  - "OpenPeppol, lista de códigos UNCL5305: https://docs.peppol.eu/poacc/billing/3.0/codelist/UNCL5305/"
  - "CEF eInvoicing, schematron de validación de EN 16931 para UBL, aserción BR-CO-17: https://raw.githubusercontent.com/ConnectingEurope/eInvoicing-EN16931/master/ubl/schematron/preprocessed/EN16931-UBL-validation-preprocessed.sch"
  - "Streamlined Sales and Use Tax Agreement, texto enmendado al 20/5/2025, secciones 202, 203, 305, 306, 324, 325 y 329: https://www.streamlinedsalestax.org/docs/default-source/agreement/ssuta/ssuta-as-amended-through-05-20-25-with-hyperlinks-and-compiler-notes-at-end.pdf"
  - "HMRC, VAT Notice 700, §17.5 a §17.6: https://www.gov.uk/guidance/vat-guide-notice-700"
  - "Software-de-gestion/.investigacion/motor-de-impuestos.md (2026-11-27)"
aliases: [motor de impuestos, motor fiscal, tax engine, cálculo de impuestos, determinación de impuestos, tax determination, impuesto por renglón, impuesto por línea, categoría fiscal, código fiscal, tax category, tax code, redondeo del impuesto, tax rounding, redondeo por línea, redondeo por total, impuesto incluido, tax included, impuesto sobre impuesto, compound tax, desglose de IVA, VAT breakdown]
creado: 2026-11-27
revisado:
---

# Motor de impuestos

El motor de impuestos es la parte del software de gestión que decide, renglón por renglón, qué impuestos lleva un comprobante, sobre qué base y con qué alícuota. Lo decide con la categoría fiscal del artículo, la condición fiscal de la parte, el lugar y la fecha. Después junta los renglones por categoría y alícuota y redondea con una regla que fija la norma o, si la norma deja elegir, el diseño.

No es una columna técnica más: combina varias. Lee [datos maestros](datos-maestros-y-partes.md) (el artículo y la parte), busca [datos con vigencia](fechas-vigencias-y-cierre.md#vigencias-datos-que-valen-desde-y-hasta) (las alícuotas), redondea importes como pide [cantidades, unidades y monedas](cantidades-unidades-y-monedas.md) y deja su resultado dentro del [documento](documento-y-estados.md) que se confirma. El saber tributario de fondo es de [Impuestos](../../Impuestos/impuestos.md): qué es la [base y la alícuota](../../Impuestos/Obligacion-tributaria/hecho-imponible-y-base.md), quién es [sujeto](../../Impuestos/Obligacion-tributaria/sujetos-del-impuesto.md), qué país cobra según el [lugar de la operación](../../Impuestos/Impuestos-al-consumo/lugar-de-la-operacion.md). Acá va cómo lo calcula un sistema. Lo propio de la Argentina está en [impuestos y cuenta corriente en la Argentina](impuestos-y-cuenta-corriente-en-argentina.md).

## Lo que entra y lo que sale de cada renglón

El impuesto de un renglón depende del producto, de las partes, del lugar y de la fecha, como explica [de qué depende el impuesto de un renglón](../../Impuestos/Obligacion-tributaria/hecho-imponible-y-base.md#de-qué-depende-el-impuesto-de-un-renglón). Para el motor, cada uno de esos datos sale de un lugar distinto del sistema (lectura de esta base):

| Dato | De dónde lo toma el motor | Qué decide |
|---|---|---|
| Categoría fiscal del artículo | el maestro del artículo | si el bien o el servicio va a la alícuota general, a una reducida, exento o fuera del impuesto |
| Condición fiscal de la parte | el maestro del cliente o del proveedor, con sus certificados | si se discrimina el impuesto, si hay exención o inversión del sujeto pasivo, si corresponde percibir |
| Lugar | la dirección de entrega o de prestación y la del vendedor | qué jurisdicción cobra y, donde hay varias superpuestas, cuáles se suman |
| Fecha del hecho | el documento | qué alícuota está vigente |
| Tipo de operación | el documento (venta, compra, devolución, exportación) | el signo y los regímenes que aplican |

Lo que sale es, por cada impuesto del renglón, una categoría, una alícuota y la base. Según qué estándar se siga, también el importe. Ese resultado se guarda en el renglón: el comprobante lo muestra y las [reglas de contabilización](registro-de-movimientos-y-dimensiones.md#del-documento-al-movimiento-las-reglas-de-contabilización) lo convierten en el asiento del débito o del crédito fiscal.

Ningún estándar de factura dice cómo se determina la categoría. EN 16931, el modelo europeo de factura electrónica, exige que cada renglón la lleve: «Each Invoice line (BG-25) shall be categorized with an Invoiced item VAT category code (BT-151)» (regla BR-CO-04). De dónde sale queda fuera del estándar. Esa determinación es justamente el trabajo del motor.

## La categoría fiscal mezcla tasa, exención y mecanismo

La lista UNCL5305, que usa EN 16931, no es una lista de alícuotas. Según la versión que publica OpenPeppol, sus códigos son estos:

| Código | Nombre en la lista | Qué combina |
|---|---|---|
| S | «Standard rate» | alícuota positiva (BR-S-05) |
| Z | «Zero rated goods» | tasa cero |
| E | «Exempt from Tax» | exención |
| AE | «Vat Reverse Charge» | inversión del sujeto pasivo |
| K | «VAT exempt for EEA intra-community supply of goods and services» | entrega dentro de la Unión |
| G | «Free export item, VAT not charged» | exportación |
| O | «Services outside scope of tax» | fuera del impuesto; el renglón no lleva alícuota (BR-O-05) |
| L, M, B | impuestos de Canarias, de Ceuta y Melilla, y un caso de Italia | regímenes territoriales |

Las reglas BR-Z, BR-E y BR-AE fijan en cero el impuesto de las categorías que no lo cobran. Una misma alícuota de cero, entonces, puede ser tasa cero, exención o inversión, y cada una tiene consecuencias distintas para el crédito de quien vende ([exento no es lo mismo que tasa cero](../../Impuestos/Impuestos-al-consumo/iva.md#exento-no-es-lo-mismo-que-tasa-cero)). Por eso el motor guarda la categoría y no solo el porcentaje.

La consecuencia de diseño es una lectura de esta base. La categoría del renglón no es un campo del artículo: sale de cruzar el artículo con la parte y el lugar. El mismo producto va a S para un cliente local, a AE para una empresa de otro país que liquida el impuesto y a G si se exporta. Esa cruza se guarda mejor como una tabla de reglas configurable que como código: es el [nivel de conocimiento](configurar-o-personalizar.md#el-nivel-de-conocimiento-comportamiento-guardado-como-datos) aplicado a los impuestos. Así, cuando cambia la norma, alguien carga una regla y no hace falta reprogramar.

## Alícuotas y límites con fecha de vigencia

Una alícuota es un dato con vigencia: una nota de crédito sobre una factura vieja tiene que usar la tasa de ese día, no la de hoy ([vigencias](fechas-vigencias-y-cierre.md#vigencias-datos-que-valen-desde-y-hasta)). Donde varias jurisdicciones cobran a la vez sobre la misma venta, también cambian los límites de cada una.

El acuerdo de los estados de EE. UU. para simplificar el impuesto a las ventas (Streamlined Sales and Use Tax Agreement, SSUTA) es el texto más detallado leído sobre cómo se mantiene ese dato. Su sección 305 obliga a cada estado miembro a:

- Hacer valer los cambios de alícuotas locales «only on the first day of a calendar quarter after a minimum of sixty days' notice to sellers», y lo mismo con los cambios de límites.
- Mantener «a database of all sales and use tax rates for all of the jurisdictions levying taxes within the state», y otra de cambios de límites con «the effective date of the change».
- Asignar alícuota y jurisdicción a cada código postal de cinco y de nueve dígitos. Si un código de nueve dígitos abarca más de una alícuota, «the state must assign the lowest combined tax rate».

Para servicios que se facturan por período, la sección 329 decide qué alícuota rige cuando el cambio cae en medio. Si la alícuota sube, «the new rate shall apply to the first billing period starting on or after the effective date»; si baja, rige para las facturas emitidas desde la fecha del cambio. Es un ejemplo de regla que el motor no puede deducir y tiene que traer configurada.

## Del renglón al resumen del comprobante

Los estándares de factura separan lo que va en cada renglón de lo que va en el total del comprobante. UBL 2.1, el vocabulario de documentos de negocio de OASIS, lo modela así:

- `TaxTotal` es «the total tax amount for a particular taxation scheme» y es la suma de los subtotales de cada categoría.
- `TaxSubtotal` lleva la base (`TaxableAmount`, «the net amount to which the tax percent (rate) is applied»), el porcentaje y el importe de una categoría.
- `TaxCategory` lleva el código, el porcentaje y, si hay exención, su motivo.
- `RoundingAmount` es «the rounding amount (positive or negative) added to the calculated tax total».

EN 16931 restringe ese vocabulario. El renglón lleva solo la categoría y la alícuota, sin importe de impuesto. El importe se calcula una vez por cada combinación de categoría y alícuota: «One VAT Breakdown shall be provided for each distinct combination of VAT category code and VAT rate» (BIS Billing 3.0, §10.4). La base de cada combinación es la suma de los netos de sus renglones, más los recargos y menos los descuentos del pie que llevan esa misma categoría (BR-S-08). El impuesto de la combinación es su base por la alícuota, «rounded to two decimals» (BR-CO-17), y el impuesto del comprobante es la suma de esos importes (BR-CO-14).

Que el importe exista solo en el resumen es la lectura de esta base sobre esas reglas: ninguna frase del estándar lo dice así.

## Redondear por renglón o por total

Redondear el impuesto de cada renglón y sumar no da lo mismo que sumar las bases y redondear una vez. Un ejemplo de esta base: tres renglones de 10,25 al 21 %.

| Forma | Cuenta | Impuesto |
|---|---|---|
| Por renglón | 2,1525 redondeado a 2,15, tres veces | 6,45 |
| Por total de la alícuota | 30,75 × 21 % = 6,4575, redondeado | 6,46 |

Un centavo por comprobante parece poco, pero sobre miles de comprobantes separa el libro de IVA de lo que el cliente registró como crédito. Las normas leídas no coinciden en cuál es la forma correcta:

| Fuente | Qué pide |
|---|---|
| EN 16931 (BIS Billing 3.0, §9 y BR-CO-17) | redondear el neto de cada renglón a dos decimales y el impuesto una vez por categoría y alícuota; «Results from calculations involving already rounded amounts are not subject to rounding» |
| HMRC, VAT Notice 700 (Reino Unido), §17.5 | quien factura puede redondear hacia abajo el total al penique entero; si calcula por renglón, redondea cada uno a 0,1 o a 1 penique, y «Whatever you decide, you must be consistent» |
| HMRC, VAT Notice 700, §17.6 | el minorista que calcula por renglón o por factura «must not round the VAT figure down», pero puede redondear cada cálculo hacia arriba o hacia abajo |
| SSUTA, sección 324 (EE. UU.) | calcular hasta el tercer decimal y redondear al centavo hacia arriba «whenever the third decimal place is greater than four»; cada estado deja elegir «on an item or an invoice basis» y aplicar el redondeo a la suma de los impuestos estatales y locales |
| Manual del web service de factura electrónica de ARCA (Argentina) | no fija una forma; acepta diferencias chicas entre lo informado y lo calculado ([impuestos y cuenta corriente en la Argentina](impuestos-y-cuenta-corriente-en-argentina.md#la-tolerancia-del-fisco-al-redondeo)) |

En el código del validador oficial de EN 16931, la comprobación de BR-CO-17 acepta un importe que difiere en menos de una unidad de moneda del calculado. La regla escrita pide redondear a dos decimales. La diferencia sale de leer el código del validador, y ninguna documentación leída la explica.

Lo que sale para el diseño, en lectura de esta base:

1. La regla de redondeo es configuración, por empresa y por jurisdicción, porque cada fisco puede pedir una distinta.
2. El sistema usa la misma regla en el comprobante, en el libro fiscal y en el asiento. Si la factura redondea por total y el libro suma renglones redondeados, el libro no cierra contra el débito fiscal.
3. Si el impuesto se calcula por total pero algo pide el importe por renglón (un costo por artículo, una devolución parcial), el total se reparte entre los renglones y la diferencia de centavos va a uno de ellos. Es el reparto del patrón *Money* que describe [cantidades, unidades y monedas](cantidades-unidades-y-monedas.md#importes-con-moneda).
4. En una compra, el comprobante es del proveedor. El sistema registra los importes que el proveedor informó y recalcula solo para avisar si la diferencia supera una tolerancia.

## Precio con impuesto incluido e impuesto sobre impuesto

UBL tiene un indicador, `TaxIncludedIndicator`, que dice si el impuesto ya está dentro del importe. Para el impuesto que se calcula sobre otro, `TaxSubtotal` lleva `CalculationSequenceNumeric`: el orden en que se aplican varios impuestos, que vale 1 para todos cuando el orden no cambia el resultado. También admite impuestos por unidad (`PerUnitAmount`) y por tramos (`TierRange`). EN 16931 trabaja con precios netos de IVA en el renglón y no usa estas piezas.

Con el precio final dado, el motor hace la cuenta al revés: el neto es el precio dividido por uno más la alícuota, y el impuesto es la diferencia. Con dos impuestos en cascada, el orden de aplicación cambia el neto. Las dos cosas son lectura de esta base: ninguna fuente primaria leída fija la fórmula ni dónde se redondea al hacer la cuenta al revés. El caso argentino de la factura al consumidor final, que muestra el IVA contenido, está en [impuestos y cuenta corriente en la Argentina](impuestos-y-cuenta-corriente-en-argentina.md#la-factura-al-consumidor-final-y-el-iva-contenido).

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre la cuenta al revés desde un precio con impuesto incluido (fórmula y punto de redondeo), y sobre el orden de aplicación de impuestos compuestos fuera del vocabulario de UBL.

## El cálculo queda congelado en el documento

Al confirmar el comprobante, el resultado del motor pasa a ser parte del documento y no se vuelve a calcular (lectura de esta base). Hay tres razones, cada una con su columna:

- La alícuota o la regla pueden cambiar después, y la factura emitida no cambia: el impuesto ya se informó ([comprobante fiscal](../../Impuestos/Cumplimiento/comprobante-fiscal.md#la-factura-no-se-borra-nota-de-crédito-y-nota-de-débito)).
- La nota de crédito copia la categoría y la alícuota del renglón que corrige, no las que el motor daría hoy.
- Los [registros fiscales](../../Impuestos/Cumplimiento/registros-fiscales.md) y los [reportes legales](reportes-operativos-y-legales.md) suman lo guardado. Si se recalculara al listar, el libro de un mes cerrado cambiaría.

La [auditoría de cambios](auditoria-de-cambios.md) cubre el otro lado: quién cambió una regla o una alícuota en la tabla del motor, y desde cuándo vale.

## Motor propio o servicio externo

Un sistema puede calcular con tablas propias o llamar a un servicio que mantiene las tablas y devuelve el impuesto de cada renglón. El SSUTA da nombre a las dos cosas:

- Un sistema certificado (certified automated system) es el «Software certified under the Agreement to calculate the tax imposed by each jurisdiction on a transaction, determine the amount of tax to remit to the appropriate state, and maintain a record of the transaction» (sección 202).
- Un proveedor certificado (certified service provider) es «An agent certified under the Agreement to perform the seller's sales and use tax functions», salvo el impuesto sobre sus propias compras (sección 203).

La diferencia que importa es quién paga por el error. El estado releva a vendedores y proveedores certificados de responsabilidad por cobrar de menos o de más cuando confiaron en «erroneous data provided by a member state on tax rates, boundaries, or taxing jurisdiction assignments» (sección 306). Un vendedor que usa un sistema certificado por el estado, aunque sea propio, se presume con práctica comercial razonable (sección 325).

En lectura de esta base, la pregunta de diseño tiene dos partes: quién mantiene al día las tablas de alícuotas, límites y categorías, y quién responde cuando están mal. Con un servicio externo, el motor pasa a ser una [integración](integracion-y-migracion.md) con un sistema que manda en ese dato, y el comprobante tiene que poder emitirse, o esperar, cuando el servicio no responde.

## Lo que también calcula el motor: la recaudación en la fuente

Además del impuesto de la operación, el motor de quien es [agente de recaudación](../../Impuestos/Recaudacion-en-la-fuente/agente-de-recaudacion.md) calcula las percepciones que suma a la factura. Una percepción se calcula como un impuesto más del comprobante, con su base, su alícuota y su vigencia, pero la alícuota suele depender del cliente y no del artículo ([retención y percepción](../../Impuestos/Recaudacion-en-la-fuente/recaudacion-en-la-fuente.md#retención-y-percepción)). La retención, en cambio, se practica al pagar y no en la factura: se modela en la [cuenta corriente](cuenta-corriente-y-aplicacion.md#los-impuestos-que-cancelan-deuda-retenciones-y-percepciones).

## Cómo falla el motor

- La alícuota como único dato del artículo. Funciona hasta que el mismo producto se vende a un exento, a un extranjero o a otra provincia. El artículo necesita una categoría, y la alícuota sale de la regla.
- Recalcular documentos confirmados. Una reimpresión o un listado que vuelve a pasar por el motor cambia comprobantes ya informados.
- Dos reglas de redondeo. El comprobante redondea por total y el libro por renglón, o al revés, y el débito fiscal no cierra por centavos que nadie sabe explicar.
- La exención sin su certificado. Un cliente queda marcado como exento para siempre, sin la vigencia del certificado que lo justifica ([certificado de exclusión](../../Impuestos/Recaudacion-en-la-fuente/pagos-a-cuenta.md)).
- Confundir tasa cero con exento. Las dos dan cero en la factura, pero no en el crédito fiscal de quien vende.

Las cinco son lectura de esta base sobre las reglas de arriba.

Para leer más: las secciones 8 a 10 de la BIS Billing 3.0 de OpenPeppol, con el ejemplo del §10.4, donde renglones de dos categorías terminan en dos subtotales; fijarse en que el importe de impuesto no aparece en el renglón. Para el redondeo, el §17.5 de la VAT Notice 700 de HMRC y la sección 324 del SSUTA, por quién elige el nivel de redondeo.
