---
resumen: >-
  El estado de resultados muestra los ingresos, los costos y los gastos de un período y el resultado que queda, ganancia o pérdida, medido por lo devengado y no por lo cobrado y pagado.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIC 1 Presentation of Financial Statements (página de la norma, según su resumen): https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/"
  - "IFRS Foundation, NIIF 18 Presentation and Disclosure in Financial Statements (página, según su resumen): https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/"
  - "OpenStax, Principles of Financial Accounting (2019), 6.6 Describe and Prepare Multi-Step and Simple Income Statements for Merchandising Companies (según extractos del buscador): https://openstax.org/books/principles-financial-accounting/pages/6-6-describe-and-prepare-multi-step-and-simple-income-statements-for-merchandising-companies"
  - "OpenStax, Principles of Financial Accounting (2019), 5.4 Appendix: Complete a Comprehensive Accounting Cycle for a Business: https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business"
  - "Contabilidad/.investigacion/estados-contables.md (2026-11-27)"
aliases: [estado de resultados, cuenta de pérdidas y ganancias, estado de pérdidas y ganancias, income statement, profit and loss, P&L, statement of profit or loss, estado del resultado integral, otro resultado integral, other comprehensive income, margen bruto, gross margin, resultado operativo, operating profit]
creado: 2026-11-27
revisado:
---

# Estado de resultados

El estado de resultados muestra los ingresos, los costos y los gastos de un período y el resultado que queda, ganancia o pérdida, medido por lo devengado y no por lo cobrado y pagado.

Junta los saldos de las cuentas de ingresos y gastos, que el [registro](../Registro/registro-contable.md) lleva aparte del patrimonio durante el período. Como se arma con el [devengado](../Registro/devengado.md), una venta facturada y no cobrada ya suma, y un sueldo devengado y no pagado ya resta. Por eso su resultado no coincide con la variación de la caja, y esa diferencia la explica el [estado de flujo de efectivo](estado-de-flujo-de-efectivo.md). El resultado del período pasa después al patrimonio del [balance](balance.md), a través del estado de cambios en el patrimonio (ver la [entrada de la vertical](estados-contables.md)).

## Un solo paso o varios pasos

OpenStax enseña dos formatos para el mismo contenido:

- El de un solo paso suma todos los ingresos, suma todos los gastos en categorías generales y los resta. No distingue lo operativo de lo que no lo es.
- El de varios pasos separa el costo de lo vendido de los gastos operativos, muestra el margen bruto y el resultado operativo, y deja aparte los otros ingresos y gastos.

Los resultados intermedios del formato de varios pasos responden preguntas distintas. El margen bruto (ventas menos [costo de lo vendido](../Operaciones/costo-de-lo-vendido.md)) dice cuánto deja la mercadería o el servicio antes de pagar la estructura. El resultado operativo resta los gastos de vender y administrar, y dice si la actividad principal gana plata. Lo que viene después (intereses, ventas de activos, impuesto a las ganancias) depende de cómo se financia la empresa y de hechos que no se repiten.

## El estado de resultados de Clip'em Cliff, agosto de 2019

OpenStax cierra su ciclo contable completo con un estado de un solo paso (cifras en dólares):

| Concepto | Importe |
|---|---|
| Ingresos por servicios | 10.300 |
| Ingresos por intereses | 350 |
| **Ingresos totales** | **10.650** |
| **Gastos totales** | **10.625** |
| **Resultado neto** | **25** |

El mismo contenido en varios pasos separaría los intereses como un ingreso no operativo. Si todos los gastos fueran operativos (el informe de investigación no trae su desglose, así que es un supuesto), el resultado operativo sería 10.300 − 10.625 = −325, una pérdida que los $350 de intereses convierten en una ganancia de $25. El ejemplo muestra para qué sirve el formato de varios pasos: el de un solo paso esconde que el servicio, en ese mes, no cubrió sus gastos.

> [!NOTE]
> Sin fuente todavía: un estado de varios pasos con margen bruto y cifras de fuente (OpenStax 6.6 completo no se leyó).

Al cierre, las cuentas de ingresos y gastos se vuelcan al patrimonio con los asientos de cierre. Con los totales de Clip'em Cliff, ese paso está en [ajustes de cierre](ajustes-de-cierre.md).

## Gastos por naturaleza o por función

Los gastos se pueden agrupar de dos maneras. Por naturaleza, según qué se consumió: sueldos, alquileres, amortizaciones, materiales. Por función, según para qué se gastó: costo de lo vendido, gastos de comercialización, gastos de administración. Una misma liquidación de sueldos cae en una sola línea en el primer caso y se reparte entre varias en el segundo.

> [!NOTE]
> Sin fuente todavía: el texto de los párrafos 99 a 105 de la NIC 1 (cuándo se usa cada análisis y qué se revela si se elige por función) y el párrafo 82 (partidas mínimas). La descripción de arriba es la distinción que se enseña habitualmente, sin una fuente leída que la respalde.

Para quien construye un sistema, la elección importa en el diseño: un gasto registrado por naturaleza solo se puede presentar por función si cada asiento lleva además a qué función corresponde (por ejemplo, en un centro de costo). Es una inferencia; las dimensiones que se cuelgan del asiento están en [centros de costo](../Contabilidad-de-gestion/centros-de-costo.md).

## El otro resultado integral

La NIC 1 llama al estado *estado del resultado y otro resultado integral*: además del resultado del período, el mismo estado presenta el otro resultado integral.

> [!NOTE]
> Sin fuente todavía: qué partidas forman el otro resultado integral y cuándo se reclasifican al resultado.

## Lo que cambia con la NIIF 18

La NIIF 18 reemplaza a la NIC 1 para los ejercicios anuales que empiezan el 1 de enero de 2027 o después, y admite aplicarla antes. Según el resumen de su página, la norma hace tres cambios que tocan a este estado:

1. Define dos subtotales que el estado tiene que mostrar: el resultado operativo y el resultado antes de financiación e impuestos. La NIC 1 no definía el resultado operativo.
2. Suma requisitos sobre las medidas de desempeño que define la propia gerencia.
3. Muda partes de la NIC 1 a la NIC 8 y a la NIIF 7.

Junto con la NIIF 18, una enmienda a la NIC 7 hace que el estado de flujo de efectivo por el método indirecto parta del resultado operativo (ver [estado de flujo de efectivo](estado-de-flujo-de-efectivo.md)).

> [!NOTE]
> Sin fuente todavía: el texto de la NIIF 18 (las categorías en que divide los ingresos y gastos y qué exige revelar sobre las medidas de la gerencia). Se leyó solo el resumen de su página.
