---
resumen: >-
  La retención de impuestos sobre sueldos es el descuento que hace el empleador, en cada pago, del impuesto sobre la renta que le corresponde al empleado, para depositarlo al fisco a nombre de él. El empleador actúa como agente de retención y cobra por cuenta del fisco un impuesto que no es suyo, con los datos que le declara el empleado y un ajuste al cerrar el año.
estado: vigente
estabilidad: estable
fuentes:
  - "IRS, Publication 15 (Circular E), Employer's Tax Guide, 2026, PDF completo, sección 7 y calendario (ejemplo de país; una sola fuente para las alícuotas): https://www.irs.gov/pub/irs-pdf/p15.pdf"
  - "26 CFR 31.3402(g)-1, supplemental wage payments, copia de Cornell LII (ejemplo de país): https://www.law.cornell.edu/cfr/text/26/31.3402(g)-1"
  - "IRS, Publication 15-A (ejemplo de país, leída en parte): https://www.irs.gov/publications/p15a"
  - "GOV.UK, Running payroll (ejemplo de país, según un extracto): https://www.gov.uk/running-payroll"
  - "GOV.UK, Running payroll: reporting to HMRC (ejemplo de país, según un extracto): https://www.gov.uk/running-payroll/reporting-to-hmrc"
  - "RG AFIP 4003/2017, texto actualizado, arts. 1 y 21 (ejemplo de país): https://biblioteca.arca.gob.ar/dcp/REAG01004003_2017_03_02"
  - "ARCA, SiRADIG, ¿Qué es? (ejemplo de país): https://www.arca.gob.ar/572web/siradig/que-es.asp"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-cargas-y-fundamentos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-huecos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/argentina-cargas.md (2026-11-27)"
aliases: [retención, retención de ganancias, retención en la fuente, agente de retención, income tax withholding, withholding tax, PAYE, pay as you earn, impuesto sobre el sueldo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Retención de impuestos sobre sueldos

La retención de impuestos sobre sueldos es el descuento que hace el empleador, en cada pago, del impuesto sobre la renta que le corresponde al empleado, para depositarlo al fisco a nombre de él. El empleador actúa como agente de retención y cobra por cuenta del fisco un impuesto que no es suyo, con los datos que le declara el empleado y un ajuste al cerrar el año.

Es una de las cuatro cargas de [cargas y declaraciones](cargas-y-declaraciones.md) y la única que no es de la seguridad social. Se calcula en la [liquidación de sueldos](../Liquidacion-de-sueldos/liquidacion-de-sueldos.md), después de los [aportes](aportes-y-contribuciones.md), porque en muchos países los aportes se restan de la base del impuesto (inferencia de esta base sobre el orden de cálculo, que está en [conceptos de liquidación](../Liquidacion-de-sueldos/conceptos-de-liquidacion.md#el-orden-de-cálculo)). El impuesto sobre la renta como tal, con sus escalas y categorías, va a [impuestos a la renta](../../Impuestos/Impuestos-a-la-renta/impuestos-a-la-renta.md), y la retención vista como régimen del fisco, a [recaudación en la fuente](../../Impuestos/Recaudacion-en-la-fuente/recaudacion-en-la-fuente.md#retención-sobre-sueldos), los dos del tema Impuestos.

## Por qué retiene el empleador

Como criterio de esta base, el fisco cobra en el origen del pago porque ahí el dinero todavía no llegó al contribuyente. El empleador queda en el medio con una obligación propia: en EE. UU., lo retenido es un «trust fund tax», y quien no lo retiene o no lo deposita puede responder con la «trust fund recovery penalty» (IRS, Pub. 15). La retención mal hecha es deuda del empleador, aunque el impuesto sea del empleado.

Así el empleado paga el impuesto en cuotas, una por cada pago de sueldo, en lugar de pagarlo de una vez al final del año. Como criterio de esta base, si la retención está bien calibrada, al cerrar el año no debe nada ni le deben nada.

## Lo que declara el empleado

El empleador no conoce toda la situación del empleado: si tiene cónyuge o hijos a cargo, si paga un alquiler o un seguro que se deduce, si tiene otro empleo. Por eso cada sistema tiene un formulario por el que el empleado se lo informa, y el empleador calcula con eso.

| País (ejemplo) | Lo que declara el empleado | Con qué calcula el empleador |
|---|---|---|
| EE. UU. | el Form W-4, que se le pide a cada empleado nuevo | las tablas de la Pub. 15-T |
| Reino Unido | un código impositivo que asigna el fisco; si cambia, se corrige la declaración | el código de cada empleado |
| Argentina | el F.572 web, por el sistema SiRADIG, con deducciones, percepciones e ingresos de otro empleo | el régimen de la RG 4003/2017 |

El de la Argentina está en [Ganancias sobre sueldos en la Argentina](ganancias-sobre-sueldos-en-argentina.md). Los datos que declara el empleado viven en el [legajo](../Legajo/legajo.md#qué-datos-lleva-un-legajo) con su fecha, porque una deducción declarada en mayo cambia la retención desde mayo y no antes (inferencia de esta base).

## Los pagos que no son el sueldo de todos los meses

Un bono, una comisión o un pago retroactivo cambian el cálculo. Como criterio de esta base, la retención del mes los tomaría como si se repitieran todo el año. EE. UU. los llama «supplemental wages», e incluyen bonos, comisiones, licencias acumuladas que se pagan, indemnizaciones, «back pay» y «retroactive pay increases» (Pub. 15). El reglamento que la guía resume, 26 CFR 31.3402(g)-1, también cuenta el «back pay» entre esos pagos y fija la alícuota más alta sobre lo que pase de 1.000.000 de dólares en el año. Las alícuotas de 22 % y 37 % tienen una sola fuente, la Pub. 15. Da dos métodos:

1. **Una alícuota fija**, si el pago va identificado aparte del sueldo: «a flat 22% (no other percentage allowed)», y 37 % sobre lo que pase de $1 millón en el año.
2. **Sumarlo al sueldo del período**, calcular la retención del total y restar lo que ya se retuvo sobre el sueldo regular: «Withhold the remaining tax from the supplemental wages».

Los dos métodos dan resultados distintos sobre el mismo pago, y el ajuste anual corrige la diferencia (inferencia de esta base). Para el cálculo, un concepto eventual tiene que poder marcarse con su propio tratamiento frente a la retención.

Un beneficio también puede tener un tratamiento distinto en cada régimen. En EE. UU., el interés que el empleador no le cobra a un préstamo de más de $10,000 a tasa baja es compensación sujeta a las cargas de la seguridad social, «but not to federal income tax withholding» (Pub. 15-A).

## El ajuste al cerrar el año

Como el impuesto es anual y la retención es mensual o por pago, al final del año se recalcula todo con los datos definitivos y se ajusta. En el ejemplo de EE. UU., el empleador concilia los formularios trimestrales con el comprobante anual de cada empleado (Form W-2), le entrega una copia y presenta otra a la administración (Pub. 15). El calendario de la Pub. 15 pone las dos cosas «By January 31» del año siguiente: entregar a cada empleado su W-2 y presentar las copias ante la seguridad social. En la Argentina, el agente de retención practica una liquidación anual por cada empleado «hasta el último día hábil del mes de abril» del año siguiente, y una liquidación final cuando la relación termina (RG 4003/2017, art. 21).

La liquidación final es parte de la [liquidación final](../Liquidacion-de-sueldos/liquidacion-final.md) del empleado: al irse, se cierra su año fiscal con ese empleador, y el próximo empleador necesita el resultado (inferencia de esta base).

> [!NOTE]
> Sin fuente todavía: el ajuste anual del Reino Unido (la guía de retención de ese país no se leyó).

## Cómo se equivoca la retención

- **Un dato del empleado que no llegó.** Una deducción que el empleado no declaró, o declaró tarde, se corrige recién en el ajuste anual, y hasta ahí se retuvo de más.
- **Un pago eventual tratado como mensual.** Un bono grande calculado como si fuera el sueldo de todos los meses retiene de más ese mes.
- **Dos empleadores sin coordinar.** Si el empleado tiene otro empleo y no lo informa, cada empleador aplica las deducciones completas y la retención total queda corta (por eso el F.572 argentino pide los ingresos de otro empleo).

Los tres son criterio de esta base sobre los mecanismos descritos arriba.
