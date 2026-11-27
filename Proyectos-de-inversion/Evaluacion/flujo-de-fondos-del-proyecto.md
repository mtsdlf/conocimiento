---
resumen: >-
  El flujo de fondos del proyecto es la plata que entra y sale de la empresa, año por año, por hacer la inversión en lugar de no hacerla: la inversión inicial, el capital de trabajo que se inmoviliza y vuelve, los ingresos o ahorros, los costos, los impuestos y el valor residual al final. Es incremental, se mide en caja y no en ganancia, y deja afuera lo que ya se gastó.
estado: borrador
estabilidad: estable
fuentes:
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones del cap. 5 «Measuring Returns on Investments» (leído): https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/invretA.pdf"
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones del cap. 6 «Estimating Side Costs and Benefits» (leído): https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/invretB.pdf"
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones del cap. 4 «Risk Measurement and Hurdle Rates», sobre qué tasa va con qué flujo (leído en esa parte): https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/hurdlerate.pdf"
  - "OpenStax, Principles of Finance (2022), 16.5 (leído por extractor): https://openstax.org/books/principles-finance/pages/16-5-choosing-between-projects"
  - "Proyectos-de-inversion/.investigacion/evaluacion.md (2026-11-27), componente 1"
aliases: [flujo de fondos, flujo de caja del proyecto, project cash flow, flujos incrementales, incremental cash flows, flujo de fondos incremental, costo hundido, sunk cost, costo de oportunidad, opportunity cost, escudo fiscal de la amortización, depreciation tax shield, valor residual, salvage value, valor terminal, terminal value, capital de trabajo del proyecto, canibalización]
creado: 2026-11-27
revisado:
---

# Flujo de fondos del proyecto

El flujo de fondos del proyecto es la plata que entra y sale de la empresa, año por año, por hacer la inversión en lugar de no hacerla: la inversión inicial, el capital de trabajo que se inmoviliza y vuelve, los ingresos o ahorros, los costos, los impuestos y el valor residual al final. Es incremental, se mide en caja y no en ganancia, y deja afuera lo que ya se gastó.

Es la materia prima de la [evaluación](evaluacion-de-la-inversion.md): el [valor actual neto](valor-actual-neto.md), la [tasa interna de retorno](tasa-interna-de-retorno.md) y el [periodo de repago](periodo-de-repago.md) son tres maneras de leer la misma tabla. OpenStax lo dice en una línea, «Estimating cash flows from potential projects is prone to errors», y es donde la evaluación más se equivoca.

## Incremental: con el proyecto menos sin el proyecto

El flujo que cuenta es la diferencia entre la empresa con la inversión y la empresa sin ella. Damodaran pide usar los flujos «that occur as a consequence of the decision, rather than total cash flows». Una máquina nueva que reemplaza a una vieja se evalúa por lo que produce de más, lo que ahorra en mantenimiento y lo que se cobra al vender la vieja, y no por todo lo que produce.

Lo mismo vale para los costos que la empresa reparte. Si la administración central se prorratea por ventas, un proyecto nuevo recibe una parte aunque no agregue un solo administrativo. Según Damodaran, solo «the incremental component of allocated costs» entra en la evaluación; cargarle el prorrateo completo puede hacer rechazar proyectos que convenían.

## De la ganancia al flujo

La contabilidad registra por el [devengado](../../Contabilidad/Registro/devengado.md); la evaluación mira la plata. Damodaran da los tres pasos para pasar de una a otra:

1. **Sumar lo que no es plata.** La amortización baja la ganancia pero no sale de la caja: se suma de vuelta. La plata salió el día de la compra, como explica [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md#la-amortización-no-aparta-plata).
2. **Restar la inversión.** La compra del activo es salida de plata aunque no sea gasto del período.
3. **Ajustar por capital de trabajo.** Si el proyecto necesita más inventario o más crédito a clientes, esa plata queda inmovilizada. Damodaran: «Any increase in working capital reduces cash flows in that year»; al final del proyecto vuelve y hay que contarla («working capital investments need to be salvaged»). Olvidarlo «will overstate cash flows on that project». Cómo se mide el capital de trabajo de la empresa está en [capital de trabajo](../../Tesoreria/Caja-y-liquidez/capital-de-trabajo.md).

La amortización, aunque no sea plata, sí cambia los impuestos. Damodaran lo llama el beneficio fiscal de la amortización: «Tax Benefit = Depreciation * Tax Rate». Con una tasa del impuesto a la renta más alta, el beneficio es mayor. Lo que no se puede deducir no da beneficio y no cambia el flujo.

## Lo que no entra: el costo hundido

Un costo hundido es lo que ya se gastó y no se recupera aunque el proyecto se rechace. Damodaran da dos ejemplos, la prueba de mercado de un producto y la investigación previa de un remedio, y la regla: «sunk costs should not be considered since they are not incremental». Agrega que a la gente le cuesta mucho cumplirla: «managers find it almost impossible to ignore sunk costs».

En una empresa en marcha el caso típico es la obra a medio hacer. Si ya se gastaron 60 y faltan 40 para terminar, la pregunta es si los beneficios futuros valen esos 40, no si valen 100. La tendencia a seguir poniendo plata en algo porque ya se puso mucho es la escalada del compromiso, que está en [cerrar o cancelar](../../Gestion-de-proyectos/Gobierno-y-cierre/cerrar-o-cancelar.md).

## Lo que sí entra aunque no sea un pago: el costo de oportunidad

Un costo de oportunidad aparece cuando el proyecto usa algo que la empresa ya tiene. Según Damodaran, ese recurso «has to be priced on its next best alternative use», que puede ser:

- **venderlo**: lo que se cobraría, neto del impuesto a la ganancia de la venta;
- **alquilarlo**: el valor actual de los alquileres después de impuestos;
- **usarlo en otra parte del negocio**: lo que costaría reemplazarlo.

Un galpón propio que hoy se alquila a terceros no es gratis para el proyecto que lo va a ocupar: le cuesta el alquiler que se deja de cobrar. El costo de oportunidad de la plata misma, lo que rendiría en otro lado, no se pone en el flujo: va en la [tasa de corte](tasa-de-corte.md).

En el mismo grupo están los efectos sobre el resto de la empresa. Según Damodaran, los costos laterales incluyen las «lost revenues for other projects» (un producto nuevo que le quita ventas a uno viejo, lo que se llama canibalización) y los beneficios laterales, las sinergias que el proyecto le deja a otros.

## El financiamiento va en la tasa, no en el flujo

Los intereses del préstamo que paga la máquina no se restan del flujo si el flujo se descuenta con el costo de capital, porque esa tasa ya incluye lo que cuesta la deuda. Damodaran lo plantea como dos versiones coherentes: si los flujos se miden para los accionistas, después de pagar la deuda, la tasa es el costo del capital propio; si se miden «to capital (or the firm)», la tasa es el costo de capital. Mezclar las dos cuenta el costo de la deuda dos veces.

Para una pyme, lo práctico es la segunda versión: evaluar el proyecto sin mirar cómo se paga, y decidir el financiamiento aparte, con [costo del financiamiento](../../Tesoreria/Financiamiento/costo-del-financiamiento.md). Es una lectura de esta base sobre el planteo de Damodaran.

## Pesos de hoy o pesos de cada año

Los flujos y la tasa tienen que estar en la misma unidad. Damodaran: «If the cash flows are nominal (real), the discount rate has to be nominal (real)», y lo mismo con la moneda: flujos en dólares se descuentan con una tasa en dólares. Si se respeta, «the project conclusions should be identical, no matter what cash flows are used».

Para pasar de una moneda a otra usa la diferencia de inflaciones. En su caso de un parque en Brasil, con inflación esperada de 9 % en reales y 2 % en dólares, el costo de capital en reales sale de (1,0846) × (1,09 / 1,02) − 1 = 15,91 %. El mismo ajuste sirve para pasar de tasa nominal a real con la ecuación de Fisher, que está en [costo del financiamiento](../../Tesoreria/Financiamiento/costo-del-financiamiento.md#la-tasa-real-con-inflación). Cómo se aplica con la inflación argentina está en [proyectos de inversión en Argentina](../proyectos-de-inversion-en-argentina.md).

## Lo que queda al final: valor residual o valor terminal

Un proyecto con vida corta termina con un valor residual: lo que se espera cobrar por el activo y recuperar del capital de trabajo. Uno que se supone que sigue indefinidamente termina con un valor terminal, que Damodaran calcula como el flujo del año siguiente dividido por la diferencia entre el costo de capital y el crecimiento. En su caso de una mina de hierro de 1.250 millones de dólares, el activo se amortiza en diez años hasta un residual de 250 millones, el capital de trabajo es 20 % de las ventas y se recupera entero el décimo año.

## Una máquina con cifras supuestas

Una empresa evalúa una máquina de 30 que ahorra 8 por año durante cinco años. Las cifras son supuestas, para mostrar la cuenta. Se amortiza en línea recta, la misma cuota cada año (6 por año), el impuesto a la renta es 35 %, la máquina pide 2 más de repuestos en stock al principio, que se recuperan al final, y no vale nada a los cinco años.

| Año | 0 | 1 a 4 | 5 |
|---|---|---|---|
| Compra de la máquina | −30 | | |
| Capital de trabajo | −2 | | +2 |
| Ahorro después de impuestos (8 × 0,65) | | 5,2 | 5,2 |
| Beneficio fiscal de la amortización (6 × 0,35) | | 2,1 | 2,1 |
| **Flujo de fondos** | **−32** | **7,3** | **9,3** |

Mirado sin impuestos ni capital de trabajo, la máquina parece recuperarse en 3,75 años (30 / 8). Con el flujo bien armado, a una [tasa de corte](tasa-de-corte.md) del 12 % el [valor actual neto](valor-actual-neto.md) da −4,55 y la [tasa interna de retorno](tasa-interna-de-retorno.md) da 6,3 %: no conviene. Para que el valor actual neto llegue a cero, el ahorro tendría que ser de unos 9,9 por año. Las cuentas son de esta base. Qué tan seguro es ese ahorro es la pregunta del [análisis de sensibilidad](analisis-de-sensibilidad.md).

> [!NOTE] Sin fuente todavía: una explicación en prosa de un libro de texto de los componentes del flujo (los de Brealey, Myers y Allen o Berk y DeMarzo no se consiguieron). La nota se apoya en las presentaciones de Damodaran, que son diapositivas de clase.
