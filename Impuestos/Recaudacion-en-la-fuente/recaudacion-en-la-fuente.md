---
resumen: >-
  La recaudación en la fuente es el mecanismo por el que un tercero que interviene en una operación cobra un impuesto por cuenta del fisco antes de que el contribuyente lo declare: quien paga le descuenta una parte al que cobra (retención) o quien cobra le suma un recargo al que paga (percepción), y el contribuyente después lo computa a cuenta de su impuesto.
estado: borrador
estabilidad: estable
fuentes:
  - "IMF, Tax Law Design and Drafting, vol. 2, cap. 14 «Individual Income Tax» (Burns y Krever, 1998), secciones sobre terminología y PAYE: https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch14.pdf"
  - "Harrison y Krelove, «VAT Refunds: A Review of Country Experience», IMF Working Paper WP/05/218 (2005): https://www.imf.org/external/pubs/ft/wp/2005/wp05218.pdf"
  - "IRS, Publication 5869, Tax Gap Projections for Tax Year 2022 (análisis de visibilidad TY 2014-2016): https://www.irs.gov/pub/irs-pdf/p5869.pdf"
  - "Kleven, Knudsen, Kreiner, Pedersen y Saez, «Unwilling or Unable to Cheat? Evidence from a Tax Audit Experiment in Denmark», NBER WP 15769 (abstract): https://www.nber.org/papers/w15769"
  - "Impuestos/.investigacion/recaudacion-en-la-fuente.md (2026-11-27)"
aliases: [recaudación en la fuente, retención en la fuente, retenciones y percepciones, withholding, withholding tax, tax withholding, collection at source, regímenes de recaudación, PAYE]
creado: 2026-11-27
revisado:
---

# Recaudación en la fuente

La recaudación en la fuente es el mecanismo por el que un tercero que interviene en una operación cobra un impuesto por cuenta del fisco antes de que el contribuyente lo declare: quien paga le descuenta una parte al que cobra (retención) o quien cobra le suma un recargo al que paga (percepción), y el contribuyente después lo computa a cuenta de su impuesto.

Esta parte cruza a las demás. No es un impuesto más, sino una forma de cobrar los [impuestos al consumo](../Impuestos-al-consumo/impuestos-al-consumo.md) y los [impuestos a la renta](../Impuestos-a-la-renta/impuestos-a-la-renta.md) antes de tiempo. Lo que se recauda así se computa y se informa en el ciclo de [cumplimiento](../Cumplimiento/cumplimiento.md).

## Retención y percepción

Las dos tienen el mismo fin y miran la operación desde puntas opuestas. En ambas intervienen tres partes: el fisco, el contribuyente que debe el impuesto y un tercero, el agente, que lo cobra por cuenta del fisco.

| | Retención | Percepción |
|---|---|---|
| Quién es el agente | quien paga | quien cobra |
| Qué hace | descuenta una parte del pago | suma un importe a lo que cobra |
| Quién sufre la recaudación | el que cobra (un proveedor, un empleado) | el que paga (un cliente) |
| Ejemplo | una empresa le paga a un proveedor 100 y le transfiere 97 | un mayorista factura 100 y cobra 103 |
| Qué recibe quien la sufre | un certificado de retención | la percepción detallada en la factura |

En los dos casos, lo que el agente cobró no es suyo: lo deposita en el fisco. Quien la sufrió lo descuenta de su propio impuesto, como si lo hubiera pagado por adelantado. La recaudación en la fuente no cambia cuánto se debe sino cuándo y por mano de quién se paga.

El Fondo Monetario Internacional, en su manual de diseño de leyes tributarias, separa la obligación de pagar el impuesto propio de «the obligation to withhold tax from payments to other persons». Por eso recomienda no llamar *taxpayer* (contribuyente) al que retiene, sino «withholding agent» o «representative taxpayer». En la terminología de [sujetos del impuesto](../Obligacion-tributaria/sujetos-del-impuesto.md), el agente es un responsable por deuda ajena.

## A cuenta o definitiva

La retención puede ser a cuenta o definitiva. A cuenta, el contribuyente igual declara y la resta de lo que debe; que sea lo habitual entre empresas es inferencia de esta base, sin fuente. Definitiva, la retención es todo el impuesto y el contribuyente no declara nada más por ese ingreso.

Según el FMI, en los países donde la retención sobre sueldos es definitiva, «most employees (and therefore most income taxpayers) pay tax through final withholding and do not file returns». El FMI da también el caso de los intereses (más abajo). Suele aplicarse sobre el monto bruto y con una alícuota más baja que la ordinaria, porque no toma en cuenta los gastos.

## Por qué los fiscos cobran en la fuente

Los fiscos usan este mecanismo por tres razones. Solo la tercera tiene respaldo en la fuente leída; las otras dos son inferencia de esta base:

1. Cobran antes. El impuesto entra al pagar, no semanas o meses después, al vencer la declaración del contribuyente.
2. Controlan. Cada retención o percepción deja un registro hecho por un tercero, que el fisco cruza con lo que declara el contribuyente.
3. Alcanzan a quien no declara. Si el contribuyente no se inscribe o no declara, al menos se cobró una parte. El FMI cuenta que Alemania tenía un impuesto progresivo sobre intereses, «collected very little on it and introduced a withholding tax in 1994 in order to be able to collect at least some».

La evidencia empírica muestra que el cumplimiento sube mucho cuando un tercero informa o retiene:

| Ingreso | Subdeclaración | Fuente |
|---|---|---|
| Con información de terceros y retención sustancial (EE. UU.) | 1 % | IRS, tax gap TY 2014-2016 |
| Con información de terceros, sin retención (EE. UU.) | 6 % | IRS, tax gap TY 2014-2016 |
| Con poca o ninguna información (cuentapropistas no agrícolas, EE. UU.) | 55 % | IRS, tax gap TY 2014-2016 |
| Informado por terceros (Dinamarca, experimento aleatorio) | 0,3 % | Kleven et al., 2011 (según su resumen) |
| Autodeclarado (Dinamarca) | 37 % | Kleven et al., 2011 (según su resumen) |

Esas cifras son del impuesto a la renta de personas. Que el efecto sea parecido en las retenciones y percepciones entre empresas es una inferencia razonable que ninguna de las dos fuentes mide.

## Lo que le cuesta a la empresa

Una empresa carga con la recaudación en la fuente por los dos lados.

- Como agente, hace un trabajo administrativo para el fisco sin cobrar por él: consulta la condición de cada contraparte, calcula, emite certificados, deposita e informa. Si se equivoca o no retiene, responde con su propio patrimonio. Está en [agente de recaudación](agente-de-recaudacion.md).
- Como quien la sufre, adelanta impuesto que todavía no debe. Si lo que le retienen y le perciben supera lo que va a deber, se le acumula un saldo a favor que puede tardar en recuperar. Está en [pagos a cuenta](pagos-a-cuenta.md).

Un documento de trabajo del FMI sobre devoluciones de IVA dice que en varios países, «particularly in Latin America and West Africa», empresas y organismos públicos tienen que retener IVA de los pagos a sus proveedores, y que estos esquemas tienen desventajas: «refund claims can proliferate under these arrangements, especially if withholding rates are set too high». Que con inflación ese saldo además pierda valor mientras espera es inferencia de esta base.

## Retención sobre sueldos

El caso más extendido es la retención del impuesto a la renta sobre sueldos. El empleador es agente: calcula el impuesto de cada empleado según lo que gana, se lo descuenta del recibo y lo deposita. El manual del FMI lo llama PAYE.

Acá entra solo el empleador como agente. El cálculo de la retención en el recibo, junto con los aportes y las contribuciones, va al tema Administración de personal y nómina (todavía no escrito).

## Notas de este tema

- [Agente de recaudación](agente-de-recaudacion.md) — lo que hace la empresa designada para retener o percibir: designación, consulta de la contraparte, cálculo, certificado, depósito y su responsabilidad si falla.
- [Pagos a cuenta](pagos-a-cuenta.md) — lo que hace quien sufre la retención o la percepción: guardar el certificado, computarlo, el saldo a favor, la devolución y la exclusión.
- [Retenciones y percepciones en Argentina](retenciones-y-percepciones-en-argentina.md) — los regímenes de IVA, Ganancias e Ingresos Brutos, SICORE y SIRE, SIRCREB, SIRTAC y los certificados de exclusión, con su norma.
