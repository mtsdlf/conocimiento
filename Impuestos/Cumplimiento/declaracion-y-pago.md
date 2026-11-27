---
resumen: >-
  Declarar y pagar es el paso en que la empresa calcula lo que debe de cada impuesto en el período, lo informa al fisco en una declaración jurada antes del vencimiento y paga el saldo, descontando lo que ya adelantó; si adelantó de más, le queda un saldo a favor que se arrastra, se compensa o se pide en devolución.
estado: vigente
estabilidad: estable
fuentes:
  - "FMI, Tax Law Design and Drafting, vol. 1 (1996), cap. 4, secciones II.D (Returns), II.H (Installment Payment Arrangements) y II.J (Interest): https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch4.pdf"
  - "Directiva 2006/112/CE del Consejo, arts. 183, 206, 250 y 252, texto de 2006 (copia del BOE): https://www.boe.es/doue/2006/347/L00001-00118.pdf"
  - "CIAT, Modelo de Código Tributario (2015), índice y tabla de cambios (la extracción del PDF perdió letras y cifras): https://www.ciat.org/Biblioteca/DocumentosTecnicos/Espanol/2015_Modelo_Codigo_Tributario_CIAT.pdf"
  - "World Bank Group y PwC, Paying Taxes 2020, fact sheet de América del Sur (leído el 2026-11-27): https://archive.doingbusiness.org/content/dam/doingBusiness/pdf/db2020/SouthAmerica_PT2020_FS.pdf"
  - "World Bank Group y PwC, Paying Taxes 2020, informe completo, sección del post-filing index (leído el 2026-11-27): https://archive.doingbusiness.org/content/dam/doingBusiness/pdf/db2020/PayingTaxes2020.pdf"
  - "Impuestos/.investigacion/cumplimiento.md (2026-11-27)"
aliases: [declaración jurada, DDJJ, declaración de impuestos, tax return, VAT return, autoliquidación, self-assessment, liquidación administrativa, administrative assessment, vencimiento, período fiscal, anticipo, saldo a favor, excedente, compensación, offset, devolución, refund, declaración rectificativa, rectificativa, amended return, pago fuera de término, liquidar impuestos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Declaración y pago

Declarar y pagar es el paso en que la empresa calcula lo que debe de cada impuesto en el período, lo informa al fisco en una declaración jurada antes del vencimiento y paga el saldo, descontando lo que ya adelantó; si adelantó de más, le queda un saldo a favor que se arrastra, se compensa o se pide en devolución.

Este paso del [cumplimiento](cumplimiento.md) cierra el período. Recibe los datos de los [registros fiscales](registros-fiscales.md), que salen de cada [comprobante fiscal](comprobante-fiscal.md). Lo que se suma y se resta depende del impuesto: el [IVA](../Impuestos-al-consumo/iva.md) liquida débito menos crédito, el impuesto a la renta parte del [resultado impositivo](../Impuestos-a-la-renta/resultado-impositivo.md), y los dos descuentan los [pagos a cuenta](../Recaudacion-en-la-fuente/pagos-a-cuenta.md).

Esta nota es dueña de cuánto se debe y cuándo vence. Pagar y tener la caja ese día es de [Tesorería](../../Tesoreria/tesoreria.md), que pone los impuestos como salidas en la [proyección de caja](../../Tesoreria/Caja-y-liquidez/proyeccion-de-caja.md).

## Quién calcula el impuesto: autoliquidación o liquidación del fisco

Hay dos formas de determinar cuánto se debe:

- Liquidación administrativa: el contribuyente informa los datos y el fisco calcula el impuesto. Según el FMI, muchos países lo hacen así con algunos impuestos: la administración «assesses the amount of tax due based on information provided to it, usually by the taxpayer».
- Autoliquidación: el contribuyente calcula el impuesto, lo declara y lo paga; el fisco lo revisa después. El FMI dice que la eficiencia empuja a los países hacia este sistema, que se puede introducir por etapas, «starting with larger enterprises».

En los impuestos de una empresa (IVA, renta, lo retenido como agente) lo habitual es la autoliquidación. En ambos sistemas la declaración da al fisco la información para que pueda «either determine the amount of tax owed or check on the taxpayer's calculations» (FMI).

En la autoliquidación el error es del contribuyente: si el cálculo estaba mal, el fisco lo determina de nuevo en una [fiscalización](fiscalizacion-y-sanciones.md) y cobra la diferencia con intereses y, si corresponde, una multa.

## La declaración jurada

En la declaración jurada el contribuyente informa los datos del período y el impuesto que resulta, bajo su responsabilidad. «Jurada» significa que lo declarado lo compromete: si es falso, la sanción es más grave que la de un error (inferencia de la base; ninguna fuente leída lo dice).

La Directiva europea pide que la declaración del IVA tenga «todos los datos necesarios para determinar la cuota del impuesto exigible y las deducciones a practicar» (art. 250). En la práctica (descripción de la base), una declaración de IVA resume:

1. el débito fiscal de las ventas del período, por alícuota;
2. el crédito fiscal de las compras del período;
3. el saldo a favor que venía del período anterior;
4. las retenciones, percepciones y pagos a cuenta sufridos;
5. el saldo: a pagar o a favor.

Una declaración en cero también se presenta. No haber vendido no exime de declarar (inferencia de la base: es la regla general en los regímenes de autoliquidación, no se leyó una fuente que lo diga en general).

## Períodos y vencimientos

Cada impuesto tiene su período y su vencimiento. El vencimiento suele caer en los días siguientes al cierre y, en muchos países, se escalona según el último dígito del número de identificación fiscal, para que no presenten todos el mismo día. Es práctica extendida, contada como inferencia de la base; no se leyó una fuente comparada.

| Impuesto | Período habitual | Vencimiento |
|---|---|---|
| IVA | mensual (en la UE, de uno a tres meses; nunca más de un año) | en la UE, hasta dos meses después del cierre del período (art. 252) |
| Impuesto a la renta | anual, con anticipos durante el año | después del cierre del ejercicio (inferencia de la base) |
| Lo retenido o percibido como agente | lo fija cada régimen | lo fija cada régimen |

La tabla es general; cada país fija sus fechas. El calendario argentino está en [impuestos en Argentina](../impuestos-en-argentina.md).

Presentar y pagar son obligaciones distintas. La Directiva europea las junta (los sujetos pasivos «deberán abonar el importe neto del IVA en el momento de presentar la declaración», art. 206) pero deja que cada país fije otro plazo. Presentar sin pagar deja una deuda declarada que el fisco cobra sin discutirla; pagar sin presentar deja un pago sin imputar y una declaración omitida (inferencia de la base).

## Anticipos

Un anticipo es un pago a cuenta del impuesto de un período que no terminó. Se usa sobre todo en el impuesto a la renta: el fisco pide cuotas durante el año, calculadas en general sobre el impuesto del año anterior (descripción de la base; no se leyó una fuente agnóstica sobre anticipos). Al cierre, la declaración anual resta los anticipos pagados. La Directiva europea admite que los países acepten «pagos a cuenta» del IVA (art. 206).

El anticipo es un adelanto del propio contribuyente; la retención y la percepción las cobra un tercero. Todos se restan igual en la declaración (ver [pagos a cuenta](../Recaudacion-en-la-fuente/pagos-a-cuenta.md)). Cómo se calculan los anticipos del impuesto a la renta está en [impuestos a la renta](../Impuestos-a-la-renta/impuestos-a-la-renta.md).

## Saldo a favor: técnico o de libre disponibilidad

El saldo a favor aparece cuando lo que se resta supera a lo que se debe. Tiene dos orígenes (descripción de la base; cada país pone sus reglas):

- Saldo técnico: sale de la mecánica del impuesto, como un IVA con más crédito que débito. Lo habitual es que solo se use contra el mismo impuesto en los períodos siguientes.
- Saldo de libre disponibilidad: sale de pagos de más, retenciones o percepciones que superan el impuesto. Suele poder usarse contra otros impuestos o pedirse en devolución.

Los nombres son argentinos (ver [IVA en Argentina](../Impuestos-al-consumo/iva-en-argentina.md)); el concepto es general. La Directiva europea deja elegir a cada país: el excedente se puede «trasladar al período impositivo siguiente, o bien proceder a la devolución», y se pueden negar las dos cosas «cuando el excedente sea insignificante» (art. 183).

Por qué las retenciones y percepciones acumulan saldo, y los caminos para usarlo (arrastrarlo, compensarlo, pedir la devolución o la exclusión del régimen), están en [pagos a cuenta](../Recaudacion-en-la-fuente/pagos-a-cuenta.md). El modelo de código del CIAT prevé además formas de compensación automática.

La devolución es la vía más lenta. Según el fact sheet de *Paying Taxes 2020* (datos de 2018), obtener una devolución de IVA lleva 27,3 semanas y 18,2 horas de trabajo (promedios mundiales), y en América del Sur la devolución estaba disponible para la empresa del caso solo en dos economías. Los países la restringen, según el informe completo, por «significant levels of fraud and a lack of fiscal resources to pay the refund». El FMI recomienda que el fisco pague intereses cuando devuelve tarde, igual que los cobra.

## Declaración rectificativa

Si la empresa descubre un error en una declaración presentada, presenta una rectificativa (o declaración sustitutiva) que reemplaza a la anterior. Si el error era a favor del fisco, se paga la diferencia con intereses. Si era a favor del contribuyente, la rectificativa genera un saldo a favor o un pedido de devolución, que el fisco suele revisar antes de aceptar.

El Modelo de Código Tributario del CIAT trata la rectificación de la autoliquidación a pedido del contribuyente y la liga con la devolución. *Paying Taxes* mide cuánto cuesta corregir una declaración de renta: 14,6 horas y, si el fisco abre una revisión, 25,5 semanas (el informe da las 25,5 semanas como promedio mundial).

Rectificar antes de que el fisco lo detecte cambia la sanción: el modelo del CIAT prevé que quien repara de forma espontánea fuera de plazo pague un recargo y evite la multa, y prevé reducir la sanción si se repara (según su índice y su tabla de cambios; el texto no se pudo leer). Los porcentajes los fija cada país (ver [fiscalización y sanciones](fiscalizacion-y-sanciones.md)).

## Pago fuera de término

Pagar después del vencimiento genera intereses (desde cuándo corren lo fija cada país; ninguna fuente leída lo precisa). El FMI insiste en que el interés no es una multa: «Interest reflects the time value of money and should therefore never be waived». La multa, si corresponde, se suma aparte. Quien no puede pagar puede pedir un plan de pagos, que no corta los intereses (FMI). Ambos temas están en [fiscalización y sanciones](fiscalizacion-y-sanciones.md).

Para leer más: FMI, *Tax Law Design and Drafting*, volumen 1, capítulo 4, sección II.D («Returns and Record Keeping»), por la diferencia entre autoliquidación y liquidación administrativa, y sección II.J («Interest»), por qué el interés no es una sanción.
