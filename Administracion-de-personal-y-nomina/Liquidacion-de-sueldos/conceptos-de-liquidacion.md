---
resumen: >-
  Un concepto de liquidación es cada línea del cálculo del sueldo: un haber que suma (el básico, una hora extra, un adicional) o una deducción que resta (un aporte, una retención, un embargo), con su regla de cálculo, su base y su lugar en el orden. El sueldo de cada empleado es la suma de sus conceptos, del bruto al neto.
estado: vigente
estabilidad: estable
fuentes:
  - "OIT, Convenio sobre la protección del salario, 1949 (núm. 95), arts. 1, 8 y 10 (copia de la Universidad de Minnesota): https://hrlibrary.umn.edu/instree/ilo95.html"
  - "IRS, Publication 15 (Circular E), Employer's Tax Guide, 2026, secciones de wages, accountable plan, supplemental wages y employee's portion (ejemplo de país): https://www.irs.gov/publications/p15"
  - "IRS, Publication 15-A, préstamos sin interés: https://www.irs.gov/publications/p15a"
  - "IRS, Publication 15-B, regla general de beneficios (leída en parte): https://www.irs.gov/publications/p15b"
  - "GOV.UK, Special rules for student loans, sección de órdenes judiciales: https://www.gov.uk/guidance/special-rules-for-student-loans"
  - "GOV.UK, Make debt deductions from an employee's pay, versión imprimible completa: https://www.gov.uk/debt-deductions-from-employee-pay/print"
  - "GOV.UK, Payslips: https://www.gov.uk/payslips"
  - "15 U.S.C. 1672 y 1673, copia de Cornell LII: https://www.law.cornell.edu/uscode/text/15/1673"
  - "29 CFR 870.11, copia de Cornell LII: https://www.law.cornell.edu/cfr/text/29/870.11"
  - "Frappe HR, Salary Structure, Salary Component y Salary Slip (documentación de producto, como evidencia de práctica): https://docs.frappe.io/hr/salary-component"
  - "Frappe HR, Salary Structure: https://docs.frappe.io/hr/salary-structure"
  - "Frappe HR, Salary Slip: https://docs.frappe.io/hr/salary-slip"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-cargas-y-fundamentos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-huecos.md (2026-11-27)"
aliases: [concepto de liquidación, conceptos de nómina, haberes, deducciones, componente salarial, salary component, earnings and deductions, pay element, bruto a neto, gross to net, neto a bruto, grossing up, gross-up, remunerativo, no remunerativo, proporcional por días, embargo, garnishment]
creado: 2026-11-27
revisado: 2026-11-27
---

# Conceptos de liquidación

Un concepto de liquidación es cada línea del cálculo del sueldo: un haber que suma (el básico, una hora extra, un adicional) o una deducción que resta (un aporte, una retención, un embargo), con su regla de cálculo, su base y su lugar en el orden. El sueldo de cada empleado es la suma de sus conceptos, del bruto al neto.

Los conceptos son las reglas de la [liquidación de sueldos](liquidacion-de-sueldos.md). El [legajo](../Legajo/legajo.md) les da los datos (sueldo, categoría, antigüedad) y [tiempo y asistencia](../Tiempo-y-asistencia/tiempo-y-asistencia.md), las novedades en horas o días. El resultado de cada concepto es una línea del [recibo de sueldo](recibo-de-sueldo.md).

## Haberes, deducciones y contribuciones

Un software abierto de nómina separa ganancias («Earnings») y deducciones («Deductions») y agrega la contribución del empleador («Employer Contribution»), que, según la lectura de esta base, se calcula sin tocar el neto. El tema usa la misma división: los haberes forman el bruto, las deducciones lo bajan al neto y las [contribuciones](../Cargas-y-declaraciones/aportes-y-contribuciones.md) son costo del empleador.

Cada concepto tiene un monto cargado o una fórmula («Amount based on formula», en el software leído). La condición va junto a la fórmula; el ejemplo literal de la documentación es `300 if getdate(start_date).month == 2 else 200`.

La misma documentación tiene dos variantes: el concepto **informativo**, que se calcula y lo leen otros pero no suma ni resta («Statistical Component»), y el que **figura sin pagarse** («Do Not Include in Total»). Por cómo varían, los conceptos son **fijos** (el básico, del legajo), **variables** (horas extra, comisiones, de las novedades) o **eventuales** (un bono, un pago único); esa clasificación es criterio de esta base.

## La base de cálculo

Un concepto se calcula sobre otros. En el software leído las fórmulas usan la abreviatura de cada concepto; la documentación da un aporte patronal `BS * 0.12`, «12% of basic salary», y una base `gross_pay`.

La base puede ser una parte del bruto, porque cada concepto declara para qué bases cuenta: el software leído marca por concepto si está sujeto al impuesto («Is Tax Applicable»), y el préstamo estudiantil del Reino Unido toma como base «the same gross pay amount» que el aporte patronal. El armado de la base de los aportes y de la retención está en [aportes y contribuciones](../Cargas-y-declaraciones/aportes-y-contribuciones.md) y [retención de impuestos sobre sueldos](../Cargas-y-declaraciones/retencion-de-impuestos-sobre-sueldos.md).

## El orden de cálculo

Como un concepto lee el resultado de otros, el orden cambia el resultado: el valor hora antes que la hora extra, el bruto antes que los aportes, los aportes antes que la retención, y lo que ordena un tercero al final, sobre lo que queda. Es inferencia de esta base a partir de las dependencias de las fórmulas; ninguna fuente leída describe cómo un motor de nómina decide el orden.

El caso documentado es el orden entre deducciones en Inglaterra, Gales e Irlanda del Norte (Escocia difiere): con órdenes prioritarias se aplican primero las órdenes y después el préstamo estudiantil; con órdenes no prioritarias, el préstamo va antes que la orden.

> [!NOTE]
> Sin fuente todavía: cómo resuelve el orden de evaluación un motor de nómina (prioridad o secuencia por concepto, dependencias calculadas).

## Proporcionales por días

Quien entra o se va a mitad de mes, o tiene días sin goce, cobra la parte proporcional de los conceptos mensuales. En el software leído, un concepto con «Depends on Payment Days» se calcula sobre los días de pago, que salen de las licencias y la asistencia; la licencia sin goce cuenta como ausencia y la media jornada como media ausencia. Un ajuste global define sobre qué se calculan esos días («Calculate Payroll Working Days Based On»).

Un ejemplo, con criterio de esta base: con un básico mensual de 900.000 y un mes de 30 días, quien ingresó el día 21 cobra los días 21 a 30: 900.000 × 10 / 30 = 300.000. Con un divisor de días hábiles el resultado cambia; como criterio de esta base, la elección es de la ley o el convenio de cada lugar.

> [!NOTE]
> Sin fuente todavía: una regla agnóstica sobre el divisor mensual (30, días del mes o días hábiles).

## Del bruto al neto, y del neto al bruto

El neto se arma en cuatro escalones. Los haberes forman el bruto, los aportes del empleado se descuentan sobre su base, la retención del impuesto se calcula sobre lo que corresponda y al final van las demás deducciones (cuota sindical, adelantos, préstamos, embargos). El orden es inferencia de esta base; las piezas son las del asiento de sueldos de [operaciones](../../Contabilidad/Operaciones/operaciones.md#cómo-se-registran-los-sueldos), donde un bruto de 2.000 termina en un neto de 1.370 después de aportes, retenciones y otros descuentos.

El camino inverso aparece cuando se pacta un neto: un bono «de bolsillo», o el empleador que se hace cargo del aporte del empleado. El IRS describe el efecto sin nombrarlo: el aporte que el empleador paga por el empleado se suma a la base, ese aumento también paga aportes, y «This again increases the amount of the additional taxes that you must pay». Cada vuelta agrega algo, así que el bruto de un neto buscado sale iterando o despejando la fórmula (inferencia de esta base).

> [!NOTE]
> Sin fuente todavía: una definición oficial o técnica del cálculo neto a bruto («gross-up»).

## Remunerativo y no remunerativo

Un concepto es remunerativo cuando la ley lo trata como salario y entra en las bases de los aportes y las contribuciones. La línea la traza cada país; las fuentes leídas muestran tres ideas:

- Cuenta la naturaleza del pago, se llame como se llame. La OIT define el salario como la remuneración «however designated or calculated» que se paga por el trabajo (Convenio 95, art. 1). El IRS dice lo mismo para sus bases: incluye todo pago por servicios, en dinero o en otra forma, y «It doesn't matter how you measure or make the payments».
- Todo es sueldo salvo lo que la ley excluye. Según el IRS, un beneficio «is taxable and must be included in the recipient's pay unless the law specifically excludes it»; un reintegro de gastos queda afuera solo si es por gastos del trabajo, se justifica y se devuelve el exceso.
- Depende del propósito. Lo que cuenta como sueldo para un aporte, el impuesto o un embargo puede diferir: para las órdenes de retención, el Reino Unido incluye comisiones y horas extra y excluye las pagas legales por maternidad y despido.

Como inferencia de esta base, «remunerativo» se define base por base: cada concepto lleva una marca por cada base (aportes, contribuciones, impuesto, embargo, indemnización). La versión argentina, con el art. 103 bis y las sumas de convenio, está en [liquidación en la Argentina](liquidacion-en-argentina.md#remunerativo-y-no-remunerativo).

## Adelantos, préstamos y embargos

Como criterio de esta base, un adelanto de sueldo se descuenta del neto de su período, y un préstamo del empleador, en cuotas. La OIT solo permite deducciones dentro de los límites de la ley, el convenio o el laudo, informando al trabajador (art. 8). En el Reino Unido, una deducción fija como un préstamo se explica en el recibo o en una declaración aparte.

Un embargo es una retención por orden de un tercero, permitida solo dentro de los límites de la ley nacional y protegiendo lo necesario para el trabajador y su familia (OIT, art. 10). Los dos ejemplos de país leídos limitan distinto; las cifras tienen una sola fuente por país, la ley en EE. UU. y la guía oficial en el Reino Unido:

| | Estados Unidos | Reino Unido |
|---|---|---|
| Cómo se limita | Tope sobre el ingreso disponible: lo menor entre el 25 % semanal y lo que exceda 30 veces el salario mínimo federal por hora; 50 % a 65 % por manutención (15 U.S.C. 1673) | Piso: la orden trae un ingreso protegido («protected earnings rate») debajo del cual no se descuenta. Lo que no se pudo descontar se arrastra al próximo pago en una orden prioritaria y no se arrastra en una no prioritaria |
| Sobre qué base | Lo que queda después de las retenciones que manda la ley (15 U.S.C. 1672) | Una lista propia de lo que cuenta como sueldo para la orden |
| Prioridad entre embargos | «the priority is determined by State law or other Federal laws» (29 CFR 870.11) | Las órdenes prioritarias (manutención impaga o multas) van primero, en el orden en que llegaron, y después las no prioritarias, también por orden de llegada |

Con varios embargos, el tope es del conjunto: según el reglamento de EE. UU., si un embargo de impuestos ya toma 45 %, uno de manutención solo puede tomar la diferencia hasta su propio tope. Por eso van al final, en orden de prioridad. El tope argentino de adelantos y deducciones, los límites de embargo y la prioridad entre embargos están en [liquidación en la Argentina](liquidacion-en-argentina.md#adelantos-deducciones-y-embargos).

> [!NOTE]
> Sin fuente todavía: reglas agnósticas de cuánto se puede adelantar y cómo se recupera un adelanto o un préstamo.
