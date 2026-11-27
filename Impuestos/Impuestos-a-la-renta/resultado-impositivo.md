---
resumen: >-
  El resultado impositivo es la ganancia sobre la que se paga el impuesto a la renta: se parte del resultado contable del ejercicio y se lo ajusta por lo que la ley trata distinto (gastos no deducibles, ingresos exentos, amortizaciones con otro ritmo, quebrantos de años anteriores).
estado: vigente
estabilidad: estable
fuentes:
  - "IFRS Foundation, IAS 12 Income Taxes, resumen de la norma (sección About): https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/"
  - "ARCA, Balance impositivo de personas jurídicas: https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/determinacion/balance-impositivo.asp"
  - "Ley de Impuesto a las Ganancias, t.o. 2019, art. 25 (quebrantos), biblioteca de ARCA: https://biblioteca.afip.gob.ar/dcp/LEY_C_020628_2019_12_05"
  - "Ley 27.802 (BO 06/03/2026), arts. 179, 181, 182 y 190: https://biblioteca.afip.gob.ar/dcp/LEY_C_027802_2026_02_27"
  - "Impuestos/.investigacion/impuestos-a-la-renta.md (2026-11-27)"
aliases: [resultado impositivo, ganancia neta imponible, renta imponible, base imponible del impuesto a la renta, taxable income, taxable profit, balance impositivo, conciliación fiscal, ajustes impositivos, diferencias permanentes, diferencias temporarias, temporary differences, permanent differences, gastos no deducibles, non-deductible expenses, ingresos exentos, quebranto, quebrantos impositivos, pérdida fiscal, tax loss carryforward, amortización impositiva, tax depreciation]
creado: 2026-11-27
revisado: 2026-11-27
---

# Resultado impositivo

El resultado impositivo es la ganancia sobre la que se paga el impuesto a la renta: se parte del resultado contable del ejercicio y se lo ajusta por lo que la ley trata distinto (gastos no deducibles, ingresos exentos, amortizaciones con otro ritmo, quebrantos de años anteriores).

Es la base del [impuesto a la renta](impuestos-a-la-renta.md) de una empresa. Las dos cifras salen del mismo registro, por [devengado](../../Contabilidad/Registro/devengado.md), pero responden a reglas distintas. La contabilidad muestra el resultado del negocio según las [normas contables](../../Contabilidad/Estados-contables/normas-contables.md); la ley tributaria define qué ganancia grava y qué gasto acepta. En la Argentina, ARCA lo resume así: la ganancia «será la que resulte del balance impositivo», con las rentas de la categoría «menos las deducciones admitidas por la ley».

## Ajustes de la utilidad contable a la ganancia imponible

El cálculo arranca en la última línea del [estado de resultados](../../Contabilidad/Estados-contables/estado-de-resultados.md) y suma o resta partidas. Cada ajuste responde a una pregunta: ¿la ley grava este ingreso? ¿acepta este gasto? ¿lo acepta en este ejercicio o en otro?

| Ajuste | Qué pasa | Sentido |
|---|---|---|
| Gasto no deducible | La contabilidad lo resta y la ley no lo acepta, en todo o por encima de un tope | se suma |
| Ingreso exento o no gravado | La contabilidad lo cuenta como ganancia y la ley no lo grava | se resta |
| Gasto que la ley acepta antes | Una amortización acelerada, por ejemplo | se resta ahora y se suma después |
| Gasto que la ley acepta después | Una previsión que solo se deduce cuando la pérdida se concreta | se suma ahora y se resta después |
| Quebranto de ejercicios anteriores | Una pérdida impositiva que la ley deja descontar en años siguientes | se resta |

La tabla es una clasificación armada por esta base. Los topes son un caso frecuente de gasto no deducible: la ley argentina, según la página de ARCA, admite los gastos de representación «hasta una suma equivalente al 1,50 % del monto total de las remuneraciones» del personal, y los honorarios de directores hasta el 25% de las utilidades contables o $12.500 por perceptor, lo que sea mayor. Lo que pasa del tope figura en la contabilidad y no reduce el impuesto.

## Diferencias permanentes y temporarias

Los ajustes se dividen en dos clases según si se compensan con el tiempo.

- Las permanentes (el gasto no deducible y el ingreso exento) nunca se revierten. Cambian el impuesto del ejercicio y la tasa efectiva para siempre.
- Las temporarias aparecen cuando la ley y la contabilidad reconocen la misma partida en ejercicios distintos. La suma de todos los años da igual, y lo que se adelanta un año se devuelve en otro.

La amortización es el ejemplo clásico de diferencia temporaria. La contabilidad reparte el costo de un activo en su vida útil ([activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md)); la ley puede fijar otro plazo o permitir uno acelerado para promover inversiones. En la Argentina, la Ley 27.802 de 2026 creó un régimen para micro, pequeñas y medianas empresas que permite amortizar los bienes muebles de una inversión productiva «en dos (2) cuotas anuales, iguales y consecutivas» (art. 182), con montos mínimos de inversión según el tamaño (art. 181).

## Un ejemplo con números

El ejemplo es ilustrativo, con una alícuota supuesta del 25% y sin las reglas de ningún país. Una empresa compra una máquina de 300. La amortiza en la contabilidad en 3 años (100 por año); la ley le deja amortizarla en 2 (150 por año). En el año 1 tiene además 40 de gastos por encima de un tope y 60 de un ingreso exento.

| Año 1 | Importe |
|---|---|
| Resultado contable antes del impuesto | 1.000 |
| + gasto no deducible (diferencia permanente) | 40 |
| − ingreso exento (diferencia permanente) | −60 |
| − amortización impositiva mayor que la contable (150 − 100, diferencia temporaria) | −50 |
| **Resultado impositivo** | **930** |
| Impuesto del ejercicio (25%) | 232,50 |

La diferencia de la máquina se revierte sola. En el año 2 la ley vuelve a deducir 50 más que la contabilidad; en el año 3 la contabilidad amortiza 100 y la ley 0, y el ajuste es +100. En tres años la suma es cero: la empresa pagó menos al principio y más al final.

## Impuesto diferido en la contabilidad

Si el resultado contable muestra 1.000 y el impuesto se calculó sobre 930, el gasto por impuesto del estado de resultados no guarda relación con la ganancia. La contabilidad lo corrige con el impuesto diferido, que reconoce hoy el impuesto que las diferencias temporarias van a generar o ahorrar más adelante.

La NIC 12 lo define desde el balance. Según el resumen de la IFRS Foundation, las diferencias temporarias son las que hay entre la base fiscal de un activo o pasivo y su valor contable, y surge un pasivo diferido «if an entity will pay tax if it recovers the carrying amount of another asset or liability». También puede surgir un activo diferido, entre otros casos, por «unused tax losses or unused tax credits», sujeto a condiciones. En el ejemplo, al cierre del año 1 la máquina vale 200 en la contabilidad y 150 para la ley: la diferencia de 50 al 25% da un pasivo diferido de 12,50, que se cancela en el año 3.

El registro es del tema Contabilidad, y la base todavía no tiene una nota sobre el impuesto diferido; el hueco queda a la vista hasta que se escriba en [Estados contables](../../Contabilidad/Estados-contables/estados-contables.md). La NIC 12 completa está en la página de la IFRS Foundation; conviene mirar la diferencia entre impuesto corriente y diferido y las condiciones para reconocer un activo por quebrantos.

## Quebrantos y su traslado a otros ejercicios

Si los ajustes dan negativo, la empresa tiene un quebranto, es decir, una pérdida impositiva. No paga impuesto ese año, y muchas leyes le dejan descontar la pérdida de las ganancias de los años siguientes, con un límite de años.

En la Argentina el plazo es de cinco años. El artículo 25 de la ley dice que, «Transcurridos CINCO (5) años» desde el de la pérdida, «no podrá hacerse deducción alguna del quebranto que aún reste». Algunos quebrantos, como los de acciones, derivados o juego, son «de naturaleza específica» y solo se compensan con ganancias de la misma clase. Desde la Ley 27.802, los quebrantos de ejercicios iniciados desde el 1 de enero de 2025 se actualizan por el índice de precios al consumidor hasta el ejercicio en que se usan (art. 190).

Sin actualización, un quebranto pierde valor con inflación mientras espera, igual que el saldo a favor que describe [pagos a cuenta](../Recaudacion-en-la-fuente/pagos-a-cuenta.md#el-saldo-inmovilizado-y-la-inflación). La otra corrección por inflación, el ajuste por inflación impositivo, también entra como ajuste del resultado y se explica en [Ganancias en Argentina](ganancias-en-argentina.md#ajuste-por-inflación-impositivo).

## Cómo falla

Lista armada por esta base, sin fuente externa.

- Calcular el impuesto sobre la utilidad contable, sin ajustes. Sobrestima o subestima el impuesto y, con él, los anticipos del año siguiente.
- Tratar una diferencia temporaria como permanente. La amortización acelerada parece un ahorro y es un diferimiento: el impuesto vuelve en los años siguientes.
- Perder un quebranto por vencimiento. Si nadie registra cuándo nació cada pérdida, el plazo vence sin usarla.
- Confundir quebranto con saldo a favor. El quebranto reduce la base de años futuros; el saldo a favor es impuesto pagado de más, que se compensa o se devuelve ([declaración y pago](../Cumplimiento/declaracion-y-pago.md)).
