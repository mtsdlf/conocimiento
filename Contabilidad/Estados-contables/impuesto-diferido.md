---
resumen: >-
  El impuesto diferido es el impuesto a las ganancias que una empresa va a pagar o ahorrar más adelante porque la contabilidad y la ley reconocen las mismas partidas en años distintos; se registra como activo o pasivo para que el gasto por impuesto de cada año guarde relación con su resultado contable.
estado: vigente
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIC 12 Impuesto a las ganancias, texto oficial (edición HTML 2026), párr. 5 a 10, 12, 15 a 17, 21, 22, 24 a 29, 34 a 36, 46 a 63, 71, 74 y 81: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias12.html"
  - "IFRS Foundation, proyecto completado Income taxes (2016): https://www.ifrs.org/projects/completed-projects/2016/income-taxes/"
  - "IASB, staff paper 19E, Income Taxes, feedback from the 2015 Agenda Consultation (mayo de 2016), párr. 18 y 19: https://www.ifrs.org/content/dam/ifrs/meetings/2016/may/iasb/income-taxes/ap19e-appendix-e-feedbackback-from-2015-consult-agenda.pdf"
  - "Brouwer y Naarding, Making Deferred Taxes Relevant (octubre de 2017), resumen e introducción: https://www.ifrs.org/-/media/feature/events-and-conferences/2017/november/deferred-taxes.pdf?la=en"
  - "Görlitz y Dobler, Financial accounting for deferred taxes: a systematic review of empirical evidence, Management Review Quarterly (2021), según su resumen: https://pmc.ncbi.nlm.nih.gov/articles/PMC8475851/"
  - "Contabilidad/.investigacion/impuesto-diferido.md (2026-11-27)"
aliases: [impuesto diferido, deferred tax, impuestos diferidos, deferred taxes, activo por impuesto diferido, deferred tax asset, pasivo por impuesto diferido, deferred tax liability, diferencia temporaria, temporary difference, diferencias temporarias, base fiscal, tax base, impuesto corriente, current tax, NIC 12, IAS 12, método del impuesto diferido, gasto por impuesto a las ganancias, income tax expense, tasa efectiva]
creado: 2026-11-27
revisado: 2026-11-27
---

# Impuesto diferido

El impuesto diferido es el impuesto a las ganancias que una empresa va a pagar o ahorrar más adelante porque la contabilidad y la ley reconocen las mismas partidas en años distintos; se registra como activo o pasivo para que el gasto por impuesto de cada año guarde relación con su resultado contable.

Cómo se pasa del resultado contable al impositivo, qué ajustes hace la ley y cuánto se paga son del tema Impuestos ([resultado impositivo](../../Impuestos/Impuestos-a-la-renta/resultado-impositivo.md)). Acá queda cómo se registra lo que sale de ahí. La norma que lo ordena es la NIC 12; en Argentina, las empresas que no aplican las NIIF siguen la RT 54, que deja no registrarlo a la pequeña y, si le cuesta un esfuerzo desproporcionado, a la mediana ([impuesto diferido en Argentina](impuesto-diferido-en-argentina.md)).

## Corriente más diferido

El gasto por impuesto del [estado de resultados](estado-de-resultados.md) tiene dos partes: «Tax expense (tax income) comprises current tax expense (current tax income) and deferred tax expense (deferred tax income)» (NIC 12, párr. 6).

- **El impuesto corriente** es el de la declaración jurada del año: «the amount of income taxes payable (recoverable) in respect of the taxable profit (tax loss) for a period» (párr. 5). Lo que no se pagó es pasivo, y lo pagado de más (por anticipos o retenciones), activo (párr. 12).
- **El impuesto diferido** es la variación, entre un cierre y el siguiente, de los activos y pasivos por el impuesto que van a generar o ahorrar las diferencias que todavía no se revirtieron.

Sin el diferido, una empresa que amortiza una máquina más rápido para la ley que para la contabilidad muestra un gasto por impuesto bajo los primeros años y alto los últimos, aunque su resultado contable sea igual todos los años. El diferido corrige eso.

## Base fiscal y diferencia temporaria

La NIC 12 no parte del estado de resultados sino del [balance](balance.md). Para cada activo y cada pasivo compara dos números:

- **el valor contable**, el que muestra el balance;
- **la base fiscal**, lo que la ley le reconoce. La de un activo es «the amount that will be deductible for tax purposes against any taxable economic benefits that will flow to an entity when it recovers the carrying amount of the asset» (párr. 7). El ejemplo de la norma: una máquina costó 100 y ya se dedujeron 30 de amortización impositiva; su base fiscal es 70. La de un pasivo es su valor contable menos lo que se va a deducir por él en el futuro (párr. 8).

La diferencia entre los dos es una **diferencia temporaria** (párr. 5). Si al recuperar el activo se va a pagar más impuesto, es imponible y genera un pasivo diferido; si se va a pagar menos, es deducible y genera un activo diferido. Dos ejemplos de la norma, con una tasa del 25%:

| Partida | Valor contable | Base fiscal | Diferencia | Resultado |
|---|---|---|---|---|
| Un bien que costó 150, con 90 de amortización impositiva acumulada (párr. 16) | 100 | 60 | 40 imponible | pasivo diferido de 10 |
| Una previsión por garantías de 100 que se deduce cuando se paga (párr. 25) | 100 (pasivo) | 0 | 100 deducible | activo diferido de 25, si es probable que haya ganancias contra las que deducirla |

La amortización impositiva acelerada es el caso típico de pasivo diferido; si la impositiva es más lenta que la contable, aparece un activo (párr. 17(b)).

Lo que nunca se revierte, como un gasto que la ley no acepta o un ingreso exento, no genera diferido. La práctica y la nota de Impuestos lo llaman diferencia permanente; la NIC 12 no usa esa palabra: lo resuelve diciendo que esas partidas tienen base fiscal igual a su valor contable (párr. 7 y 8), y su efecto aparece en la conciliación de la tasa (párr. 81(c)).

## Una máquina en tres años

El ejemplo es el de [resultado impositivo](../../Impuestos/Impuestos-a-la-renta/resultado-impositivo.md#un-ejemplo-con-números): una máquina de 300 que la contabilidad amortiza en 3 años (100 por año) y la ley en 2 (150 por año), con alícuota del 25%. El año 1 tiene además 40 de gasto no deducible y 60 de ingreso exento. Para los años 2 y 3 se suponen 1.000 de resultado contable sin otras diferencias; esas cifras son supuestas y el cálculo está verificado.

| Cierre | Valor contable | Base fiscal | Diferencia imponible | Pasivo diferido (25%) | Variación |
|---|---|---|---|---|---|
| Año 1 | 200 | 150 | 50 | 12,50 | +12,50 |
| Año 2 | 100 | 0 | 100 | 25,00 | +12,50 |
| Año 3 | 0 | 0 | 0 | 0 | −25,00 |

El pasivo diferido llega a 25 al cierre del año 2 y se cancela en el año 3, cuando la ley ya no deja deducir nada y el impuesto corriente sube.

| | Año 1 | Año 2 | Año 3 |
|---|---|---|---|
| Resultado contable antes del impuesto | 1.000 | 1.000 | 1.000 |
| Resultado impositivo | 930 | 950 | 1.100 |
| Impuesto corriente (25%) | 232,50 | 237,50 | 275,00 |
| Impuesto diferido | 12,50 | 12,50 | −25,00 |
| **Gasto por impuesto** | **245,00** | **250,00** | **250,00** |

El resultado impositivo del año 1 es 1.000 + 40 − 60 − 50 = 930. Los asientos del año 1:

| Cuenta | Debe | Haber |
|---|---|---|
| Impuesto a las ganancias corriente | 232,50 | |
| Impuesto a las ganancias a pagar | | 232,50 |
| Impuesto a las ganancias diferido | 12,50 | |
| Pasivo por impuesto diferido | | 12,50 |

El año 2 repite la forma con 237,50 y 12,50. En el año 3 el diferido se da vuelta: Pasivo por impuesto diferido 25 al debe, Impuesto a las ganancias diferido 25 al haber, y el gasto queda en 275 − 25 = 250. En los tres años la suma del diferido es cero.

El gasto de los años 2 y 3 es exactamente el 25% del resultado contable. El del año 1 no, por las partidas que nunca se revierten, y eso es lo que muestra la conciliación que pide la norma (párr. 81(c)): 1.000 × 25% = 250, más 10 por el gasto no deducible (40 × 25%), menos 15 por el ingreso exento (60 × 25%), da 245, una tasa efectiva del 24,5%.

## Cuándo no se reconoce

El pasivo diferido se reconoce por todas las diferencias imponibles, salvo las que nacen del reconocimiento inicial de la llave de negocio, o del de un activo o pasivo en una operación que no es una combinación de negocios, no afecta ni el resultado contable ni el impositivo y no genera a la vez diferencias imponibles y deducibles iguales (párr. 15). Ese último requisito se sumó en 2021: por él, un [arrendamiento](../Operaciones/arrendamientos.md) puede generar diferido desde el inicio, según lo que diga la ley fiscal (párr. 22A).

El activo diferido tiene una condición más: se reconoce «to the extent that it is probable that taxable profit will be available» contra la cual usarlo (párr. 24). Lo mismo vale para los quebrantos, las pérdidas impositivas que la ley deja descontar en años siguientes (párr. 34). La norma advierte que tener quebrantos sin usar «is strong evidence that future taxable profit may not be available»; con pérdidas recientes, el activo solo se reconoce si hay diferencias imponibles suficientes o «convincing other evidence» (párr. 35). Al cierre se revisa y se reduce si dejó de ser probable (párr. 56). Cuánto dura un quebranto lo dice la ley de cada país: en Argentina, cinco años, según [resultado impositivo](../../Impuestos/Impuestos-a-la-renta/resultado-impositivo.md#quebrantos-y-su-traslado-a-otros-ejercicios).

## Con qué tasa y sin descontar

El diferido se mide con la tasa que se espera que rija cuando la diferencia se revierta, según las leyes «enacted or substantively enacted by the end of the reporting period» (párr. 47); si la escala es progresiva, con la tasa promedio esperada para esos años (párr. 49). Un cambio de alícuota cambia el saldo aunque la diferencia no cambie, y el efecto va a resultados (párr. 60).

No se descuenta: «Deferred tax assets and liabilities shall not be discounted» (párr. 53). La norma lo justifica en que descontar exigiría programar la reversión de cada diferencia, y en que permitirlo sin exigirlo haría incomparables a las empresas (párr. 54). La RT 54 argentina, en cambio, deja elegir.

## Dónde va el gasto y cómo se presenta

El impuesto sigue a la partida que lo originó (párr. 57): el de una partida de resultados va a resultados, y el de una partida que se registra en el otro resultado integral, como una revaluación de bienes de uso, va ahí (párr. 61A y 62).

Los activos y pasivos diferidos se compensan «if, and only if» la empresa tiene derecho legal a compensar y son del mismo fisco (párr. 74). El texto de la NIC 12 de 2026 ya no dice si van como corrientes o no corrientes: esa regla está en la norma de presentación, que la investigación no leyó.

Para quien construye un sistema, el diferido no sale de un documento sino de un cálculo de cierre: hace falta llevar, para cada activo y pasivo con diferencia, su valor contable y su base fiscal, con su propio registro de amortización impositiva al lado del contable. Es una inferencia sobre el mecanismo, no el texto de la norma. El asiento se arma como un [ajuste de cierre](ajustes-de-cierre.md) más.

## Lo que se le critica

> [!IMPORTANT]
> **Disputado: si el impuesto diferido informa algo útil.**
> - **Brouwer y Naarding** (2017) sostienen que el enfoque de balance de la NIC 12 «provides insufficient value-relevant information to investors, since there is only a weak relationship between deferred tax balances and future tax cash flows», y proponen reconocer solo las diferencias que vayan a generar pagos reales y medirlas descontadas. Es un trabajo de posición, presentado en un evento de la IFRS Foundation.
> - **La revisión de Görlitz y Dobler** (2021) encuentra, según su resumen, «substantial evidence for the value relevance of various deferred tax items»; en el cuerpo, leído en parte, los activos diferidos pesan más que los pasivos.
> - **El IASB**, después de consultar en 2015, decidió en 2016 no reemplazar ni modificar la NIC 12 y no seguir investigando. En esa consulta, de 63 respuestas que pusieron prioridad, 13 la pusieron alta, 24 media y 26 baja; varios usuarios pidieron más información sobre los impuestos pagados y la tasa futura (staff paper 19E, párr. 18 y 19); ninguno de los motivos citados pide eliminar el diferido (lectura propia).

> [!NOTE] Sin fuente todavía: los ejemplos ilustrativos de la NIC 12 (su parte B, con asientos oficiales) y la regla de presentación corriente o no corriente en la norma de presentación vigente.

## Qué leer de la norma

La NIC 12 en la página de la IFRS Foundation: los párrafos 5 a 10 (definiciones y base fiscal), 15 a 17 y 24 a 25 (los ejemplos con números), 34 a 36 (quebrantos), 46 a 56 (medición) y 57 a 63 (dónde va el gasto). Conviene leer la base fiscal con los ejemplos al pie de los párrafos 7 y 8, que resuelven casi todos los casos que un sistema necesita.
