---
resumen: >-
  Un activo fijo es un bien que la empresa usa durante varios años (una máquina, un vehículo, un edificio); se registra por su costo y ese costo se reparte como gasto a lo largo de su vida útil mediante la amortización.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIC 16 Propiedades, planta y equipo, resumen oficial: https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/"
  - "IFRS Foundation, NIC 16, texto oficial (edición HTML 2026): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html"
  - "OpenStax, Principles of Financial Accounting (2019), 11.2 capitalizar o gastar: https://openstax.org/books/principles-financial-accounting/pages/11-2-analyze-and-classify-capitalized-costs-versus-expenses"
  - "OpenStax, Principles of Financial Accounting (2019), 11.3 métodos de depreciación: https://openstax.org/books/principles-financial-accounting/pages/11-3-explain-and-apply-depreciation-methods-to-allocate-capitalized-costs"
  - "OpenStax, Principles of Financial Accounting (2019), 11.5 cambio de estimación y baja: https://openstax.org/books/principles-financial-accounting/pages/11-5-describe-some-special-issues-in-accounting-for-long-term-assets"
  - "OpenStax, Principles of Finance, cap. 5, términos clave (vía buscador): https://openstax.org/books/principles-finance/pages/5-key-terms"
  - "Contabilidad/.investigacion/operaciones.md (2026-11-27)"
  - "Contabilidad/.investigacion/posicion-contraria.md, mito 3 (2026-11-27)"
aliases: [activos fijos, bienes de uso, propiedades planta y equipo, PP&E, property plant and equipment, fixed assets, amortización, depreciación, depreciation, amortización acumulada, accumulated depreciation, vida útil, useful life, valor residual, residual value, salvage value, NIC 16, IAS 16]
creado: 2026-11-27
revisado:
---

# Activos fijos y amortización

Un activo fijo es un bien que la empresa usa durante varios años (una máquina, un vehículo, un edificio); se registra por su costo y ese costo se reparte como gasto a lo largo de su vida útil mediante la amortización.

La norma que lo ordena es la NIC 16 (qué son las NIIF y quién las emite está en [normas contables](../Estados-contables/normas-contables.md)), que los llama propiedades, planta y equipo; en Argentina se dicen también bienes de uso. Los libros de Estados Unidos dicen depreciación donde acá se dice amortización. El plan de mantenimiento y las órdenes de trabajo de cada activo son del tema Activos y mantenimiento, todavía no escrito; de acá son el alta, la amortización y la baja.

## Capitalizar o gastar

Capitalizar es registrar un desembolso como activo en lugar de como gasto del período. La NIC 16 pide hacerlo si, y solo si, es probable que el bien traiga beneficios económicos futuros y su costo se puede medir con fiabilidad. El servicio diario (mano de obra, consumibles, repuestos chicos) va a resultados. OpenStax lo resume igual: el mantenimiento de rutina y las reparaciones menores se gastan, y las mejoras que alargan la vida o aumentan la capacidad se capitalizan. Una reparación que alarga la vida útil, entonces, sube el activo.

El costo es el precio de contado a la fecha de la compra, neto de descuentos, más los costos directamente atribuibles a dejarlo funcionando; OpenStax enumera envío, impuestos, armado y honorarios legales. Si el pago se difiere más allá del crédito normal, la diferencia con el precio de contado es interés. En el ejemplo de OpenStax 11.2, un terreno de $100.000 con una comisión de $8.000 queda registrado por $108.000. La compra de una máquina el 1 de enero de 2019:

| Cuenta | Debe | Haber |
|---|---|---|
| Máquinas | 5.000 | |
| Caja | | 5.000 |

Cada parte significativa de un activo con vida distinta se amortiza por separado. El terreno no se amortiza, porque su vida es ilimitada (salvo canteras y casos parecidos); el edificio que está encima, sí.

## Vida útil, valor residual y los tres métodos

La amortización reparte de forma sistemática el importe amortizable durante la vida útil. El importe amortizable es el costo menos el valor residual, lo que se espera recuperar al final. Empieza cuando el activo está disponible para usar y no se detiene porque esté parado. Según la NIC 16, se elige el método que mejor refleja cómo se consumen los beneficios del activo; un método basado en los ingresos que genera está prohibido desde una enmienda de 2014.

OpenStax 11.3 aplica los tres métodos a una máquina de serigrafía de $10.000, con valor residual de $1.000, vida de 5 años o 100.000 impresiones, y 20.000 impresiones el primer año y 30.000 el segundo:

| Método | Cálculo | Año 1 | Año 2 |
|---|---|---|---|
| Lineal | (10.000 − 1.000) / 5 | 1.800 | 1.800 |
| Unidades de producción | 9.000 / 100.000 = $0,09 por impresión | 1.800 | 2.700 |
| Saldo decreciente doble | 10.000 / 5 × 2; después (10.000 − 4.000) / 5 × 2 | 4.000 | 2.400 |

El asiento de cada año es el mismo, con el importe de la tabla:

| Cuenta | Debe | Haber |
|---|---|---|
| Amortización del período | 1.800 | |
| Amortización acumulada | | 1.800 |

La amortización acumulada resta del activo en el balance; el costo original queda a la vista. El método cambia en qué años se carga el costo. El saldo decreciente doble es un caso del saldo decreciente que la NIC 16 no nombra; en la tabla, OpenStax lo calcula sin restar el valor residual.

La vida útil, el valor residual y el método se revisan al menos en cada cierre, y un cambio es un cambio de estimación: no se corrige el pasado, se reparte lo que queda. En el ejemplo de OpenStax 11.5, una prensa de $58.000 con residual de $10.000 y 5 años de vida se amortiza $9.600 por año. A los 3 años lleva $28.800 acumulados y su valor en libros es $29.200. Si la empresa estima entonces 5 años más y un residual de $6.000, la amortización pasa a $23.200 / 5 = $4.640 por año.

## Vender o dar de baja un activo

Un activo se da de baja cuando se vende o cuando ya no se espera nada de él. El resultado es el precio neto de venta menos el valor en libros, y la NIC 16 aclara: "Gains shall not be classified as revenue". Con la prensa del ejemplo, vendida a $31.000 después de 3 años:

| Cuenta | Debe | Haber |
|---|---|---|
| Caja | 31.000 | |
| Amortización acumulada | 28.800 | |
| Prensas | | 58.000 |
| Resultado por venta de bienes de uso | | 1.800 |

Si la vende a $27.100, la pérdida es $2.100; a $29.200, no hay resultado. El asiento da de baja a la vez el costo y la amortización acumulada, por eso un activo vendido antes de terminar de amortizarse deja un resultado que depende de cuánto se había amortizado hasta esa fecha.

Si un activo pierde valor, puede corresponder una pérdida por deterioro. Eso lo regula otra norma, la NIC 36, que la investigación no cubrió: cuándo se reconoce y contra qué valor no sale de ninguna fuente leída. La NIC 16 también admite un modelo de revaluación que OpenStax no trata.

## La amortización no aparta plata

Quien no es contador suele creer que la amortización es plata que la empresa guarda para reponer la máquina. El asiento muestra lo contrario: Amortización del período contra Amortización acumulada, sin ninguna cuenta de caja o banco. Según OpenStax, la depreciación reparte el costo de tener el activo a lo largo de su vida útil, el valor en libros es la parte del costo que todavía no pasó a gasto, y ninguno de los dos sigue el valor de mercado.

La plata salió cuando se pagó la compra. La amortización solo decide en qué años ese desembolso aparece como gasto en el estado de resultados. Por eso el [estado de flujo de efectivo](../Estados-contables/estado-de-flujo-de-efectivo.md), cuando parte del resultado (método indirecto), la suma de vuelta: bajó la ganancia sin mover la caja. Si una empresa quiere tener fondos para reponer un activo, tiene que apartarlos con una decisión financiera, que es del tema Tesorería, todavía no escrito.

> [!NOTE] Sin fuente todavía: una fuente que nombre este malentendido como tal. La explicación sale del asiento y del concepto de OpenStax, y lo del flujo de efectivo, de un glosario de OpenStax leído por el buscador.

Para quien construye un sistema, el activo fijo pide (inferencia) su propio registro (fecha de alta, costo, vida útil, residual, método) para calcular la amortización de cada período, y la baja tiene que cancelar el costo y la amortización acumulada en el mismo asiento.
