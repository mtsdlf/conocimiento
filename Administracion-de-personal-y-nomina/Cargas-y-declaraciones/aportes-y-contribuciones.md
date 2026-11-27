---
resumen: >-
  Los aportes son lo que se le retiene al empleado de su sueldo para la seguridad social, y las contribuciones son lo que el empleador paga por su cuenta sobre ese mismo sueldo. Los dos se calculan como un porcentaje de una base, que la ley puede limitar con un tope, y conviven con otras cargas del empleador como el seguro de accidentes de trabajo.
estado: vigente
estabilidad: estable
fuentes:
  - "IRS, Publication 15 (Circular E), Employer's Tax Guide, 2026 (ejemplo de país; una sola fuente para las cifras): https://www.irs.gov/publications/p15"
  - "IRS, Publication 15-B, Employer's Tax Guide to Fringe Benefits (leída en parte): https://www.irs.gov/publications/p15b"
  - "GOV.UK, Running payroll (ejemplo de país, según un extracto): https://www.gov.uk/running-payroll"
  - "OIT, Convenio sobre la protección del salario, 1949 (núm. 95), arts. 1, 8 y 10 (copia de la Universidad de Minnesota): https://hrlibrary.umn.edu/instree/ilo95.html"
  - "Documentación de un software abierto de nómina, Salary Component (evidencia de práctica; según un resumen): https://docs.frappe.io/hr/salary-component"
  - "ARCA, Libro de Sueldos Digital, Guía 31, Topes a las bases de aportes: https://www.arca.gob.ar/LibrodeSueldosDigital/documentos/nuevos/G31-Topes-LSD.pdf"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-cargas-y-fundamentos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-huecos.md (2026-11-27)"
aliases: [aportes, contribuciones, aportes personales, contribuciones patronales, cargas patronales, cotizaciones, employee contributions, employer contributions, social security contributions, payroll taxes, FICA, base imponible, tope de aportes, wage base limit]
creado: 2026-11-27
revisado: 2026-11-27
---

# Aportes y contribuciones

Los aportes son lo que se le retiene al empleado de su sueldo para la seguridad social, y las contribuciones son lo que el empleador paga por su cuenta sobre ese mismo sueldo. Los dos se calculan como un porcentaje de una base, que la ley puede limitar con un tope, y conviven con otras cargas del empleador como el seguro de accidentes de trabajo.

Son la parte más grande de [cargas y declaraciones](cargas-y-declaraciones.md). Se calculan en la [liquidación de sueldos](../Liquidacion-de-sueldos/liquidacion-de-sueldos.md), con los mismos [conceptos de liquidación](../Liquidacion-de-sueldos/conceptos-de-liquidacion.md) que el sueldo, y se informan en la declaración periódica. La retención del impuesto sobre el sueldo se calcula con otra lógica y está en [retención de impuestos sobre sueldos](retencion-de-impuestos-sobre-sueldos.md).

## Lo que se retiene y lo que se paga encima

El aporte baja el neto y la contribución no. En un recibo, el aporte es una deducción y la contribución, si figura, es informativa. Un software abierto de nómina lo modela así: además de ganancias y deducciones tiene un tipo de concepto «Employer Contribution» (que no cambie lo que cobra el empleado es inferencia de esta base), y su documentación da como ejemplo un aporte patronal `BS * 0.12`, «12% of basic salary».

El ejemplo de EE. UU. muestra los dos lados con el mismo porcentaje (IRS, Pub. 15, 2026):

| Régimen | Aporte del empleado | Contribución del empleador | Tope de la base |
|---|---|---|---|
| Seguridad social | 6,2 % | 6,2 % | $184,500 en 2026 |
| Medicare | 1,45 % | 1,45 % | «no wage base limit» |

En el Reino Unido, la contribución del empleador se calcula sobre las ganancias que superan £242 por semana (GOV.UK, Running payroll, según un extracto). En la Argentina los porcentajes son distintos para cada lado y cada régimen, y están en [cargas sociales en la Argentina](cargas-sociales-en-argentina.md).

Las cifras de EE. UU. tienen una sola fuente en esta base y sirven para ver la estructura, no para liquidar.

## La base y el tope

La base es la suma de los conceptos que la ley sujeta a aportes. La OIT define el salario por su naturaleza y no por su nombre: «remuneration or earnings, however designated or calculated» que se paga por el trabajo (Convenio 95, art. 1). El IRS dice lo mismo desde la base de las cargas: «It doesn't matter how you measure or make the payments» (Pub. 15). Un pago llamado «premio» o «gratificación» sigue en la base, y solo una exclusión de la ley lo saca.

El tope limita la base sobre la que se calcula el aporte. En el ejemplo de EE. UU., la seguridad social se calcula hasta una base de $184,500 en 2026 y no sobre lo que pasa de ahí. Medicare no tiene techo. En la Argentina, los topes se fijan cada trimestre, valen para las bases de los aportes y «no aplican para las bases de contribuciones» (ARCA, Guía 31 del Libro de Sueldos Digital): el empleado deja de aportar arriba del tope, pero el empleador sigue contribuyendo sin ese tope.

Para quien construye el cálculo, de ahí salen tres reglas (inferencia de esta base sobre los ejemplos):

1. **Cada régimen tiene su propia base.** Un concepto puede contar para la seguridad social y no para el impuesto, o al revés. La marca va por concepto y por régimen, como explica [conceptos de liquidación](../Liquidacion-de-sueldos/conceptos-de-liquidacion.md#remunerativo-y-no-remunerativo).
2. **El tope tiene período.** Un tope anual obliga a acumular la base del año, y uno mensual se mira en cada período de liquidación. Si en un mes hay dos liquidaciones (un sueldo y un pago fuera de ciclo), el tope se aplica a la suma.
3. **El tope y la alícuota tienen vigencia.** Se guardan con la fecha desde la que valen, porque una [reliquidación](../Liquidacion-de-sueldos/retroactivos-y-reliquidaciones.md) de un mes viejo tiene que usar los valores de ese mes.

## Beneficios y reintegros dentro o fuera de la base

Un beneficio que no se paga en dinero también puede ser sueldo para las cargas. El IRS lo dice como regla general: «Any fringe benefit you provide is taxable and must be included in the recipient's pay unless the law specifically excludes it» (Pub. 15-B). Los equivalentes de dinero nunca entran en la excepción de los beneficios menores: «Cash and cash equivalent fringe benefits ... are never excludable as a de minimis benefit».

Los reintegros de gastos quedan afuera si cumplen tres condiciones: que sean gastos del trabajo y no un sueldo disfrazado, que se justifiquen y que el exceso se devuelva, cada cosa «within a reasonable period of time» (Pub. 15, «accountable plan»). Lo que no se rinde vuelve a la base. La rendición de esos gastos es de [gastos y rendiciones](../../Contabilidad/Operaciones/gastos-y-rendiciones.md), en Contabilidad.

Un caso que muestra cómo se encadena la base: si el empleador paga el aporte del empleado sin descontárselo, ese pago se suma al sueldo, y ese aumento vuelve a estar sujeto a aportes, «This again increases the amount of the additional taxes that you must pay» (Pub. 15). Es el cálculo de neto a bruto de [conceptos de liquidación](../Liquidacion-de-sueldos/conceptos-de-liquidacion.md#del-bruto-al-neto-y-del-neto-al-bruto).

## El seguro de accidentes de trabajo

Además de las contribuciones, el empleador suele estar obligado a cubrir a sus empleados contra accidentes y enfermedades del trabajo. En la Argentina, quien no puede autoasegurarse tiene que contratar una «Aseguradora de Riesgos del Trabajo (ART)» (Ley 24.557, art. 3 inc. 3). El detalle está en [cargas sociales en la Argentina](cargas-sociales-en-argentina.md#la-art-y-el-seguro-de-vida).

> [!NOTE]
> Sin fuente todavía: el principio internacional del seguro de accidentes de trabajo (los Convenios 102 y 121 de la OIT no se leyeron) y cómo se calcula la prima en algún país (alícuota sobre la nómina, suma fija por empleado o las dos).

## Los descuentos que la ley permite

Los aportes son el descuento obligatorio más común, y hay otros. La OIT permite descontar del salario solo «under conditions and to the extent prescribed by national laws or regulations or fixed by collective agreement or arbitration award», y pide informar al trabajador (Convenio 95, art. 8). El embargo es una retención por orden de un tercero, permitida solo «in a manner and within limits prescribed by national laws or regulations» y protegiendo lo necesario para el trabajador y su familia (art. 10).

De ahí salen tres familias de deducciones que el cálculo tiene que distinguir, porque tienen orden y límites distintos: las que impone la ley (aportes, retención del impuesto), las que acepta el trabajador (una cuota sindical, un préstamo, un adelanto; esta familia es inferencia de esta base) y las que ordena un tercero (embargos, cuotas alimentarias). Cómo se ordenan y con qué topes está en [conceptos de liquidación](../Liquidacion-de-sueldos/conceptos-de-liquidacion.md#adelantos-préstamos-y-embargos).

## Cómo se equivoca el cálculo de aportes

- **Un concepto mal marcado.** Un pago que debía aportar y no lo hizo genera una deuda del empleador, y una diferencia en la cuenta previsional del empleado.
- **El tope aplicado a la contribución.** Si el sistema usa la misma base topeada para los dos lados, el empleador contribuye de menos en los sueldos altos (en la Argentina el tope es solo de aportes).
- **La alícuota del mes equivocado.** Una reliquidación que usa la alícuota de hoy para un mes viejo.

Los tres son criterio de esta base. Se evitan guardando las marcas, los topes y las alícuotas con fecha, y controlando cada período contra el anterior.
