# Investigación: impuesto diferido (Contabilidad)

Fecha de la investigación: 2026-11-27. Lectores de destino: quien construye software de gestión y no es contador. Qué se paga, la alícuota y cómo se declara son del tema Impuestos y no se desarrollan; acá solo cómo se registra.

Leyenda de lectura: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en Autoridad (A), Profundidad (P), Ejemplos (E), Unicidad (U).

---

## Componente 1: `impuesto-diferido` (general, NIC 12)

### Tabla de fuentes

| # | Fuente | URL | Tipo | Lectura | A | P | E | U |
|---|---|---|---|---|---|---|---|---|
| 1.1 | IAS 12 Income Taxes, texto oficial edición 2026 (IFRS Foundation) | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias12.html | Primaria | [L] párrafos 1-99 y ejemplos incluidos en el texto (párr. 16, 22, 25, 26(d), 52A, 81). No incluye la Parte B (Illustrative Examples) | 3 | 3 | 2 | 3 |
| 1.2 | Base de conocimiento: `Impuestos/Impuestos-a-la-renta/resultado-impositivo.md`, sección «Impuesto diferido en la contabilidad» y tabla de ejemplo | ruta local | Interna | [L] | 1 | 1 | 2 | 1 |

Hueco de fuente: los Illustrative Examples de la NIC 12 (Parte B, con ejemplos de cifras y asientos) no se pudieron bajar (la URL probada devolvió 404). Por eso el ejemplo numérico de abajo es propio, marcado como cifras supuestas.

### Afirmaciones con párrafo (NIC 12, edición 2026)

**Corriente frente a diferido**
- Definición de impuesto corriente: "Current tax is the amount of income taxes payable (recoverable) in respect of the taxable profit (tax loss) for a period." (párr. 5). Pasivo por impuesto diferido: "the amounts of income taxes payable in future periods in respect of taxable temporary differences" (párr. 5).
- El gasto total es la suma: "Tax expense (income) comprises current tax expense (current tax income) and deferred tax expense (deferred tax income)." (párr. 6). Definición de "tax expense": "the aggregate amount included in the determination of profit or loss for the period in respect of current tax and deferred tax" (párr. 5).
- Corriente: "Current tax for current and prior periods shall, to the extent unpaid, be recognised as a liability." Si lo pagado excede lo debido, el exceso es un activo (párr. 12). Un quebranto que se puede retrotraer para recuperar impuesto de un período anterior se reconoce como activo (párr. 13).
- La norma parte del balance. Principio fundamental: reconocer un pasivo (activo) diferido "whenever recovery or settlement of the carrying amount of an asset or liability would make future tax payments larger (smaller) than they would be if such recovery or settlement were to have no tax consequences" (párr. 10; objetivo).

**Base fiscal y diferencias temporarias**
- "The tax base of an asset is the amount that will be deductible for tax purposes against any taxable economic benefits that will flow to an entity when it recovers the carrying amount of the asset. If those economic benefits will not be taxable, the tax base of the asset is equal to its carrying amount." (párr. 7). Ejemplo literal 1: "A machine cost 100. For tax purposes, depreciation of 30 has already been deducted ... The tax base of the machine is 70." Ejemplo 2: intereses a cobrar de 100 gravados por percibido, base fiscal nula. Ejemplo 3: deudores por ventas de 100 ya incluidos en la ganancia imponible, base 100.
- Base fiscal de un pasivo: "its carrying amount, less any amount that will be deductible for tax purposes in respect of that liability in future periods" (párr. 8). Ejemplo 4: multas devengadas de 100 no deducibles, base 100 y no hay diferencia deducible; ejemplo 1: gastos devengados de 100 que se deducen por pagado, base nula.
- Partidas sin activo o pasivo contable pero con base fiscal, como costos de investigación gastados y deducibles después: diferencia deducible con carrying amount nulo (párr. 9, 26(b)).
- Diferencias temporarias: "differences between the carrying amount of an asset or liability in the statement of financial position and its tax base" (párr. 5). Imponibles: darán montos imponibles en períodos futuros al recuperar o liquidar el valor contable. Deducibles: darán montos deducibles (párr. 5).
- Ejemplo de la norma de imponible (párr. 16): "An asset which cost 150 has a carrying amount of 100. Cumulative depreciation for tax purposes is 90 and the tax rate is 25%." Base fiscal 60; diferencia imponible 40; "the entity recognises a deferred tax liability of 10 (40 at 25%)".
- Ejemplo de deducible (párr. 25): previsión por garantías de 100, deducible solo al pagar, tasa 25%. Base fiscal nula, diferencia deducible 100, "the entity recognises a deferred tax asset of 25 (100 at 25%), provided that it is probable that the entity will earn sufficient taxable profit".
- Amortización acelerada genera pasivo: "A taxable temporary difference arises, and results in a deferred tax liability, when tax depreciation is accelerated (if tax depreciation is less rapid than accounting depreciation, a deductible temporary difference arises, and results in a deferred tax asset)" (párr. 17(b)). Otros ejemplos de imponible: intereses gravados por percibido (17(a)), desarrollo capitalizado y deducido al gastarse (17(c)). Ejemplos de deducibles: beneficios de retiro (26(a)), costos de investigación (26(b)), pasivos asumidos en una combinación de negocios (26(c)), activos a valor razonable con base fiscal mayor (26(d); ejemplo de título de deuda con valor razonable 918 y base 1.000, diferencia deducible 82).

**Diferencias que no son temporarias (permanentes)**
- Verificado con búsqueda en el texto: las palabras "permanent", "non-temporary" no aparecen en la NIC 12. Aparece "timing differences" una sola vez, en el párrafo 17: "Such temporary differences are often described as timing differences". Y la nota al párrafo 18 aclara que hay temporarias que no son de timing.
- Lo que la norma sí hace con lo que nunca se revierte: lo trata por base fiscal. Si el beneficio económico no será gravable, la base fiscal del activo es igual a su valor contable y no hay diferencia (párr. 7 y ejemplos 3, 4 y 5). Los dividendos a cobrar no gravados: base 100, no hay diferencia imponible (ejemplo 4 del párr. 7). Multas no deducibles: base igual al valor contable (ejemplo 4 del párr. 8). La norma ofrece también el análisis alternativo (base nula con tasa nula), con el mismo resultado: no hay diferido.
- Estos efectos aparecen luego en la conciliación de la tasa (párr. 81(c), 84): ingresos exentos y gastos no deducibles "may affect" la relación entre gasto y utilidad contable (párr. 84). Entonces, "diferencia permanente" es vocabulario de práctica y del enfoque anterior (resultado), no de la NIC 12. Es el concepto que usa la nota de Impuestos de la base.

**Reconocimiento de pasivos y excepciones**
- "A deferred tax liability shall be recognised for all taxable temporary differences, except to the extent that the deferred tax liability arises from: (a) the initial recognition of goodwill; or (b) the initial recognition of an asset or liability in a transaction which: (i) is not a business combination; (ii) at the time of the transaction, affects neither accounting profit nor taxable profit (tax loss); and (iii) at the time of the transaction, does not give rise to equal taxable and deductible temporary differences." (párr. 15). El inciso (iii) es la modificación de mayo de 2021 (arrendamientos y desmantelamientos); el párr. 22A lo ilustra con el arrendatario: "an entity recognises any resulting deferred tax liability and asset".
- Razón de la excepción de la llave de negocio: "goodwill is measured as a residual and the recognition of the deferred tax liability would increase the carrying amount of goodwill" (párr. 21). Si después se deteriora, la reducción del pasivo no reconocido tampoco se reconoce (21A). Pero si la llave es deducible fiscalmente en cuotas, el pasivo que surge después del reconocimiento inicial sí se reconoce (21B, ejemplo con CU100 y 20% anual).
- Ejemplo de la excepción de reconocimiento inicial (párr. 22(c)): activo de 1.000, vida 5 años, tasa 40%, depreciación no deducible: "The entity does not recognise the resulting deferred tax liability of 400 because it results from the initial recognition of the asset." Al año siguiente, valor 800 y pasivo no reconocido de 320. Razón: ajustar el valor del activo por el mismo monto "would make the financial statements less transparent".
- Inversiones en subsidiarias, sucursales, asociadas y negocios conjuntos: pasivo reconocido salvo que (a) la controladora controle el momento de la reversión y (b) sea probable que no se revierta en el futuro previsible (párr. 39). Activos solo si es probable que se reviertan y haya ganancia imponible (párr. 44).

**Activos y la condición de probabilidad**
- "A deferred tax asset shall be recognised for all deductible temporary differences to the extent that it is probable that taxable profit will be available against which the deductible temporary difference can be utilised" (párr. 24), con la misma excepción de reconocimiento inicial. Para quebrantos y créditos no usados: "to the extent that it is probable that future taxable profit will be available" (párr. 34).
- Probabilidad: hay base suficiente si existen diferencias imponibles de la misma autoridad y entidad que se revertirán en el mismo período o en períodos a donde se traslade el quebranto (párr. 28); si no, se mira la ganancia imponible futura, sin contar las deducciones de la reversión misma ni los montos que surgirán de nuevas diferencias deducibles (párr. 29(a)(i)-(ii)), o las oportunidades de planificación fiscal (párr. 29(b), 30).
- Historia de pérdidas: "the existence of unused tax losses is strong evidence that future taxable profit may not be available"; con pérdidas recientes se reconoce solo si hay diferencias imponibles suficientes o "convincing other evidence" (párr. 35). Criterios (párr. 36): diferencias imponibles suficientes antes del vencimiento, ganancias probables antes del vencimiento, pérdidas por causas identificables que es improbable que se repitan, y planificación fiscal.
- Revisión al cierre: se reduce el activo en la medida en que ya no es probable la ganancia y se revierte la reducción si lo vuelve a ser (párr. 56); los activos no reconocidos se reevalúan (párr. 37).
- Información a revelar: monto del activo y naturaleza de la evidencia cuando depende de ganancias mayores que las que surgen de revertir diferencias imponibles y la entidad tuvo pérdida este año o el anterior (párr. 82).

**Medición**
- Corriente: al monto que se espera pagar, con tasas y leyes "enacted or substantively enacted by the end of the reporting period" (párr. 46).
- Diferido: "measured at the tax rates that are expected to apply to the period when the asset is realised or the liability is settled, based on tax rates (and tax laws) that have been enacted or substantively enacted by the end of the reporting period" (párr. 47). El anuncio de gobierno con efecto sustantivo de sanción cuenta (párr. 48). Con escalas progresivas, se usan tasas promedio de los períodos de reversión (párr. 49). Debe reflejar la forma esperada de recuperar o liquidar (párr. 51).
- Sin descuento: "Deferred tax assets and liabilities shall not be discounted." (párr. 53). Razón: "The reliable determination of deferred tax assets and liabilities on a discounted basis requires detailed scheduling of the timing of the reversal of each temporary difference"; permitirlo sin exigirlo "would result in deferred tax assets and liabilities which would not be comparable between entities". "This Standard does not require or permit the discounting" (párr. 54). Si el valor contable ya está descontado (jubilaciones), las diferencias se calculan sobre ese valor (párr. 55).
- Un cambio de tasa o de leyes cambia el saldo diferido aunque no cambie la diferencia, y va a resultados salvo que se vincule a partidas fuera de resultados (párr. 60, 63).

**Dónde va el gasto**
- Regla: "Accounting for the current and deferred tax effects of a transaction or event is consistent with the accounting for the transaction or event itself." (párr. 57). Resultados: "Current and deferred tax shall be recognised as income or an expense and included in profit or loss for the period" salvo lo que provenga de una transacción fuera de resultados o de una combinación de negocios (párr. 58). La mayoría de los diferidos nacen de ingresos y gastos que se reconocen en otro período fiscal y van a resultados (párr. 59).
- Otro resultado integral: lo que se refiere a partidas allí reconocidas, por ejemplo la revaluación de propiedades, planta y equipo (párr. 61A(a), 62). Patrimonio directo: ajustes por cambio de política o corrección de errores (con retroactividad) y el componente de patrimonio de un instrumento compuesto (párr. 61A(b), 62A, 23).
- Si no se puede determinar con precisión, se asigna "reasonable pro rata" (párr. 63). Los impuestos de dividendos siguen el origen de las utilidades que los generaron (párr. 57A).
- Combinaciones de negocios: el diferido afecta la llave o la ganancia por compra ventajosa (párr. 66).

**Presentación y compensación**
- Corrientes: se compensan solo con derecho legal a compensar e intención de liquidar neto o simultáneamente (párr. 71).
- Diferidos: se compensan "if, and only if" la entidad tiene derecho legal a compensar corrientes y ambos corresponden a impuestos de la misma autoridad sobre la misma entidad (o entidades distintas que liquidarán neto) (párr. 74). Razón: evitar el calendario detallado (párr. 75).
- El gasto va en la categoría de impuesto a las ganancias del estado de resultados (párr. 77; la edición 2026 remite a IFRS 18 en el párr. 78 y 81(ab)). Los párrafos 69-70, que fijaban la presentación en el estado de situación (antes: no corriente), figuran como "[Deleted]": el texto de la NIC 12 de esta edición no trae regla de clasificación corriente o no corriente del diferido (está en otra norma; no verificado, hueco).
- Información: componentes del gasto (párr. 79-80), impuesto de cada componente de otro resultado integral (81(ab)), explicación de la relación entre gasto y utilidad contable con una conciliación numérica de gasto contra "the product of accounting profit multiplied by the applicable tax rate(s)" o de la tasa efectiva contra la aplicable (81(c)), cambios de tasa (81(d)), diferencias y quebrantos sin activo con vencimiento (81(e)), saldos por tipo de diferencia (81(g)).
- Ejemplo de conciliación en el texto (ilustra el 81(c)): utilidad contable 2.500 (19X1) y 3.000 (19X2); impuesto a la tasa nacional del 30%: 750 y 900; gastos no deducibles +60 y +30; menor tasa del país B −50 y −150; gasto 760 y 780.

### Verificación del ejemplo de la base (máquina) contra la NIC 12

Datos de la nota de Impuestos: costo 300, amortización contable 100/año en 3 años, impositiva 150, 150, 0; alícuota 25%; resultado contable 1.000. En el año 1 hay además gasto no deducible 40 e ingreso exento 60 (diferencias que la NIC 12 no llama permanentes).

Coherencia: es coherente con los párrafos 5, 7, 16 y 17(b), con dos observaciones.

1. Al cierre del año 1: valor contable 200 (300 − 100), base fiscal 150 (300 − 150); diferencia imponible 50; pasivo 12,50 (50 × 25%). Coincide.
2. La nota dice que el pasivo de 12,50 "se cancela en el año 3". Es incompleto: al cierre del año 2 el valor contable es 100 y la base fiscal 0 (300 − 150 − 150), así que la diferencia crece a 100 y el pasivo a 25. Recién el año 3 lo cancela por completo (valor contable 0, base 0). El ajuste de 12,50 es el del año 1; el año 2 suma otros 12,50; el año 3 suma +100 al resultado impositivo y libera 25. Sugerencia para la base: redactar «llega a 25 al cierre del año 2 y se cancela en el año 3».
3. Las diferencias permanentes (40 y −60) no generan diferido; solo cambian el impuesto corriente y la conciliación.
4. La excepción de reconocimiento inicial (párr. 15(b)) no aplica: la máquina se compra y su costo es deducible, afecta el resultado fiscal por la vía de amortizaciones.

### Ejemplo con asientos (cifras supuestas, cálculo verificado)

Cifras supuestas: se toma la tabla de la nota de Impuestos para el año 1 y se supone para los años 2 y 3 un resultado contable antes del impuesto de 1.000 cada año, sin diferencias permanentes. Alícuota 25% constante. El pago del impuesto y los anticipos no se modelan (el pasivo corriente figura como «a pagar»).

Saldos de la máquina:

| Cierre | Valor contable | Base fiscal | Diferencia imponible | Pasivo diferido (25%) | Variación |
|---|---|---|---|---|---|
| Año 1 | 200 | 150 | 50 | 12,50 | +12,50 |
| Año 2 | 100 | 0 | 100 | 25,00 | +12,50 |
| Año 3 | 0 | 0 | 0 | 0 | −25,00 |

Impuesto corriente:

| | Año 1 | Año 2 | Año 3 |
|---|---|---|---|
| Resultado contable antes del impuesto | 1.000 | 1.000 | 1.000 |
| + no deducible / − exento (permanentes) | +40 − 60 | 0 | 0 |
| Ajuste por amortización (fiscal − contable) | −50 | −50 | +100 |
| Resultado impositivo | 930 | 950 | 1.100 |
| Impuesto corriente (25%) | 232,50 | 237,50 | 275,00 |
| Impuesto diferido (variación del pasivo) | 12,50 | 12,50 | −25,00 |
| **Gasto por impuesto total** | **245,00** | **250,00** | **250,00** |

Verificación cruzada: año 1, (1.000 + 40 − 60) × 25% = 245; años 2 y 3, 1.000 × 25% = 250. Tres años: corriente 745 + diferido 0 = 745 = impuestos efectivamente a pagar; el diferido se anula.

Asientos (debe / haber):

Año 1
- Gasto por impuesto a las ganancias corriente 232,50 / Impuesto a las ganancias a pagar 232,50
- Gasto por impuesto a las ganancias diferido 12,50 / Pasivo por impuesto diferido 12,50
- Total gasto del año 1 en resultados: 245,00.

Año 2
- Gasto por impuesto corriente 237,50 / Impuesto a las ganancias a pagar 237,50
- Gasto por impuesto diferido 12,50 / Pasivo por impuesto diferido 12,50 (saldo 25,00)
- Total: 250,00.

Año 3
- Gasto por impuesto corriente 275,00 / Impuesto a las ganancias a pagar 275,00
- Pasivo por impuesto diferido 25,00 / Ingreso por impuesto diferido 25,00 (saldo 0)
- Total: 275 − 25 = 250,00.

Conciliación del año 1 (estilo párr. 81(c)): resultado contable 1.000 × 25% = 250,00; + efecto del gasto no deducible 40 × 25% = +10,00; − efecto del ingreso exento 60 × 25% = −15,00; gasto por impuesto 245,00 (tasa efectiva 24,5%).

### Recurso canónico del componente 1

La NIC 12 en la edición vigente de la IFRS Foundation (fuente 1.1), párrafos 5-10 (definiciones y base fiscal), 15-17 y 24-25 (ejemplos numéricos), 34-36 (quebrantos), 46-56 (medición) y 57-63 (dónde va el gasto). Para ejemplos con cifras y asientos completos, la Parte B (Illustrative Examples) de la misma norma, que queda como hueco (ver abajo).

### Huecos del componente 1

- Illustrative Examples de la NIC 12 (Parte B) no leídos; el ejemplo con asientos es propio.
- Clasificación corriente o no corriente del diferido en IFRS: no está en la NIC 12 de esta edición; falta verificar en la norma de presentación (IAS 1 / IFRS 18).
- IFRIC 23 (incertidumbre sobre tratamientos fiscales) está citada en una nota de la NIC 12 pero no se leyó.
- Pilar Dos (párr. 88A-88D) queda fuera.

---

## Componente 2: `impuesto-diferido-en-argentina` (RT 54)

### Tabla de fuentes

| # | Fuente | URL | Tipo | Lectura | A | P | E | U |
|---|---|---|---|---|---|---|---|---|
| 2.1 | RT 54 (T.O. RT 59 y modificatorias, incluye RT 59, RT 62 y Res. JG 656/2025), adoptada por el CPCE CABA, sección «Contabilización del impuesto a las ganancias» párr. 570-600, párr. 83, 176-200, 332-336 y apartados de transición | https://consejo.org.ar/storage/attachments/Resolucion%20Tecnica%20N%2054%20(TO%20RT%2059%20y%20modi-7TbUsld18i.pdf | Primaria | [L] los párrafos citados; el resto del texto, solo por búsqueda de palabras | 3 | 3 | 1 | 3 |
| 2.2 | RT 62 (Res. CD 70/2025 del CPCE CABA, 17/12/2025; capítulo 12 «Estados contables de entidades cooperativas») | (descarga local; mismo sitio del Consejo) | Primaria | [L] parcial: resolución y búsqueda de palabras sobre el anexo | 3 | 1 | 1 | 2 |
| 2.3 | NIC 12 (fuente 1.1) | idem | Primaria | [L] | 3 | 3 | 2 | 3 |
| 2.4 | Base: `Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md` | ruta local | Interna | [L] parcial (alícuota, ajuste por inflación impositivo) | 1 | 1 | 1 | 1 |

### Afirmaciones con párrafo (RT 54)

**Quién puede no aplicar el método del impuesto diferido**
- Pequeña: "Una entidad pequeña podrá reconocer exclusivamente el gasto y el pasivo por impuesto a las ganancias corriente. En este caso, la entidad no reconocerá activos ni pasivos por impuestos diferidos." (párr. 572). Es el método del impuesto a pagar, con otro nombre: la RT 54 no usa esa expresión; usa «reconocer exclusivamente» el corriente (verificado por búsqueda en el texto).
- Mediana: "En la medida en que reconocer activos y pasivos por impuestos diferidos implique un costo o esfuerzo desproporcionado, según la evaluación establecida en el párrafo 83, una entidad mediana podrá reconocer exclusivamente el gasto y el pasivo por impuesto a las ganancias corriente." (párr. 573). Es un tratamiento alternativo (listado entre los casos del párr. 83 en las disposiciones generales).
- No pequeña: "Una entidad que no es pequeña, de corresponder, aplicará el método del impuesto diferido" (párr. 578). La excepción por costo o esfuerzo desproporcionado se usa con criterio restrictivo: "solo cuando esta Resolución Técnica u otras normas contables establezcan un tratamiento permitido" (párr. 83(a)). El párr. 83 exige evaluar costo y beneficio juntos, no uno solo.
- Categorías (párr. 6 y 7): pequeña si en el ejercicio anterior los ingresos son iguales o inferiores a un importe que define la FACPCE; mediana si superan ese importe y son menores o iguales a otro que define la FACPCE; la RT no trae las cifras, solo remite a la FACPCE, y excluye entidades financieras, aseguradoras y otras (párr. 6 y 7). Las cifras no se verificaron (hueco).
- Definición de impuesto a las ganancias: "Equivale a la suma algebraica del impuesto a las ganancias corriente y el impuesto a las ganancias diferido (cuando este se contabiliza)" (párr. 571). Impuesto corriente: "Importe determinado en función de las ganancias fiscales del período actual, según surge de la presentación impositiva" (párr. 571).

**Excepciones**
- Pasivos (párr. 582): no se reconocen los que procedan de (a) "Un valor llave que no es deducible impositivamente"; (b) el reconocimiento inicial de un activo o pasivo en una transacción que "no es una combinación de negocios; y a la fecha de la transacción no afecta el resultado contable ni el impositivo"; (c) inversiones en sucursales, controladas, vinculadas o negocios conjuntos si la inversora controla el momento de reversión y es improbable que se reviertan en el futuro previsible.
- Podrán no reconocerse (opción, párr. 583): diferencias en terrenos y otros activos no amortizables no destinados a la venta cuando es improbable que se reviertan en un futuro previsible; y ciertos tipos de hacienda cuya venta probablemente no genere mayores pagos (por ejemplo, el mantenimiento del número de cabezas). Esta opción no existe en la NIC 12.
- Activos (párr. 584): no se reconocen los de reconocimiento inicial con el mismo criterio, ni los de inversiones si es improbable que se reviertan o que haya ganancias imponibles suficientes.
- Contraste con la NIC 12: la RT 54 no tiene el inciso (iii) del párr. 15(b) NIC 12 ("does not give rise to equal taxable and deductible temporary differences", enmienda de 2021) ni el párr. 22A (arrendamientos). Es una diferencia textual entre ambas.

**Reconocimiento de activos y quebrantos**
- Pasivo por diferencias imponibles "siempre que sea probable que la recuperación o la cancelación de la medición contable de un activo o pasivo vaya a producir pagos fiscales mayores"; activo por diferencias deducibles si producirá pagos menores; activo por quebrantos o créditos no utilizados "siempre que resulte probable su deducción de ganancias imponibles futuras" (párr. 580).
- Quebrantos: "solo en la medida en que estime probable la obtención de ganancias imponibles futuras suficientes", considerando causas identificables cuya repetición es improbable, el límite temporal de las normas, pasivos diferidos que permitan estimar importes imponibles futuros y oportunidades de planificación fiscal (párr. 581). Mismo contenido que los párr. 34-36 y 30 de la NIC 12, sin la regla de «convincing other evidence» ante historia de pérdidas.
- Valor recuperable: "Una entidad no podrá medir ningún activo por impuesto diferido por encima de su valor recuperable, que es el importe máximo de beneficios imponibles futuros ..." (párr. 591); se reconoce desvalorización cuando es improbable su recuperación (592), se revierte cuando desaparecen las causas (593), con contrapartida en el impuesto a las ganancias (594-595). Es un esquema de desvalorización, no de «no reconocer»: más cerca del modelo anterior que de la NIC 12.

**Medición**
- Procedimiento: comparar valor contable con base fiscal, determinar imponibles y deducibles y "multiplicar tales diferencias temporarias por la tasa (alícuota) fiscal" (párr. 585); los quebrantos, pérdida por tasa (586).
- Tasa: "Alícuota que se espera rija en el momento estimado de reversión de las diferencias temporarias o compensación de pérdidas fiscales, de acuerdo con normas legales aprobadas a la fecha de los estados contables"; con escalas progresivas, la tasa promedio estimada para los períodos de reversión o la del impuesto del período actual (párr. 571). La NIC 12 dice «enacted or substantively enacted» y permite anuncios con efecto sustantivo (párr. 47-48); la RT 54 dice «normas legales aprobadas» y no menciona el anuncio.
- Descuento: "Una entidad podrá medir la totalidad de los pasivos y activos por impuestos diferidos: a) a su valor nominal; o b) a su valor descontado utilizando una tasa del momento de la medición que refleje las evaluaciones del mercado sobre el valor tiempo del dinero y los riesgos específicos de la operación." (párr. 587). Es una opción de política contable y se aplica a la totalidad. Contraste directo con la NIC 12 (párr. 53-54): "Deferred tax assets and liabilities shall not be discounted." El corriente se mide a valor nominal (párr. 574). Si se descuenta, se revela valor nominal y descontado por año de reversión y la tasa (párr. 599(i)).
- Base fiscal (párr. 588-590): activo, el importe deducible de beneficios futuros, o su medición contable si ya tributó o está exento; pasivo, la medición contable menos lo deducible en el futuro (ejemplos de la RT: multas no deducibles igual a la medición contable; previsión para juicios deducible en el futuro igual a cero; anticipos de clientes que ya tributaron) y partidas no reconocidas que tienen base fiscal.
- El gasto o ingreso diferido es la variación entre los saldos netos de cierre y de inicio (párr. 579).
- Revaluación de bienes de uso: el aumento del pasivo diferido por cada revaluación se imputa contra el saldo por revaluación, y su reversión posterior, a resultados (párr. 334-336; 332 salvo entidad pequeña que opte por el 572). Es el equivalente de la regla de «outside profit or loss» (NIC 12 párr. 61A, 62).

**Presentación y revelación**
- Compensación: "solo si tiene el derecho exigible legalmente de compensar sus importes (por ejemplo, porque se vinculan con la misma autoridad fiscal)" (párr. 596); no exige la intención de liquidar neto, a diferencia del 74(b)(ii) NIC 12 (ahí aplica a entidades distintas; para la misma entidad y autoridad, la NIC 12 también exige el derecho a compensar corrientes).
- Se presenta como rubro no corriente, dentro de deudas fiscales u otros créditos en moneda, o como partida separada (párr. 597); en la lista de rubros figuran "Activo neto por impuesto diferido" (párr. 609 n) y "Pasivo neto por impuesto diferido" (párr. 610 f). Corriente: neto de anticipos y retenciones (párr. 575), dentro de deudas fiscales u otros créditos (576).
- Gasto: dentro de la misma sección del estado de resultados o de evolución del patrimonio donde están las partidas que le dieron origen; neto de impuestos en resultados (operaciones que continúan; discontinuadas) y en evolución del patrimonio (resultados diferidos; ajustes de ejercicios anteriores) (párr. 577, 598).
- Notas (párr. 599): composición corriente y diferido; saldo inicial, variación y final por tipo; cambios de tasa; motivos de activos por pérdidas fiscales con pérdida actual o anterior; importes por diferencia y quebranto; conciliación entre el gasto y "el impuesto teórico (que surge de multiplicar el resultado contable por la tasa fiscal vigente)", excepto que sea pequeña o mediana que opta por no presentarla o cualquier entidad que ajusta por inflación y opta por no presentarla (599(f)(i)-(ii)); pasivos o activos no reconocidos por excepciones; diferencias y quebrantos sin activo, con fecha de validez; valor nominal y descontado si se descuenta.

**Cambio de categoría**
- Una entidad que pasa de mediana a pequeña (en la fecha de aplicación inicial) y opta por no aplicar el método: "al ser un cambio que no podría haber efectuado aplicando las normas anteriores, considerará tal modificación de criterio como si tratara de un cambio obligatorio de política contable" (apartado de transición, Ejemplos «tipo 1», Ejemplo 1, línea 16031 del texto; el ejemplo remite a la clasificación según la RT 41).
- Régimen permanente: informar en notas si en el ejercicio modificó políticas o comenzó o cesó un tratamiento permitido por un cambio de categoría, y si el ejercicio siguiente debe cambiar de categoría (párr. 9 de la sección de categorías, líneas 1219 y siguientes). El texto sobre el efecto contable del cambio de política (retroactivo, etc.) no se leyó en esta ronda (hueco).

**Interacción con el ajuste por inflación**
- Una entidad que aplique el método reconoce los saldos diferidos de la comparación entre la medición contable "(en moneda de cierre)" y la base fiscal (párr. 194).
- Si ajusta por inflación, puede no revelar la conciliación entre el gasto y el impuesto teórico (párr. 195, 599(f)(ii)).
- La RT 54 no menciona en los párrafos 571-599 ni en los de inflación el ajuste por inflación impositivo, ni el efecto de los quebrantos actualizados: se busca «inflación impositivo» y «ajuste por inflación ... impositiv» y no hay resultado. La base fiscal es la que resulte de la ley («Valuación fiscal o medición de los activos y pasivos resultante de aplicar las normas de la legislación referida al impuesto a las ganancias», párr. 571), por lo que si la ley ajusta la base, esa base ajustada es la que se compara. La consecuencia es una lectura propia, no un texto de la norma.
- Cruce con la base: la nota de Ganancias en Argentina dice que el ajuste impositivo es distinto del contable y solo corre pasado el umbral del 100% en 36 meses (art. 106), y que el quebranto desde la Ley 27.802 se actualiza por IPC (art. 190). Ambas cosas cambian la base fiscal de los bienes y de los quebrantos que se comparan; conviene decirlo en la nota como consecuencia, sin atribuirlo a la RT.

**RT 62**
- La RT 62 incorpora a la RT 54 el capítulo 12 «Estados contables de entidades cooperativas: cuestiones específicas» (considerandos g y Art. 1 de la Res. CD 70/2025). Búsqueda de «impuesto a las ganancias», «impuesto diferido», «572» y «573» en el texto descargado: sin resultados. No cambia la sección de impuesto diferido. Vigencia: para estados contables emitidos desde la publicación en el Boletín Oficial de la CABA (Art. 3). Salvedad: el texto descargado es la Segunda Parte (resolución del Consejo y anexo); no se leyó párrafo por párrafo.
- La RT 59 (T.O. de la RT 54, aprobada el 30/6/2024) es el texto vigente que se leyó (considerando c). Cambios entre RT 54 original y RT 59 en esta sección: no verificados.

### Contraste NIC 12 y RT 54, resumen

| Tema | NIC 12 | RT 54 |
|---|---|---|
| Quién aplica | Toda entidad en su alcance | No pequeña; mediana puede no aplicarlo si es desproporcionado (573); pequeña puede no aplicarlo (572) |
| Descuento | Prohibido (53-54) | Opción: nominal o descontado (587) |
| Tasa | Sancionada o sustancialmente sancionada (47-48) | Normas legales aprobadas (571) |
| Excepciones | Llave, reconocimiento inicial con (iii), subsidiarias (15, 39) | Llave no deducible, reconocimiento inicial sin (iii), inversiones (582); además opción para terrenos y hacienda (583) |
| Activos | Probabilidad de ganancias (24, 34-36, 56) | Probabilidad (580-581) y desvalorización contra valor recuperable (591-595) |
| Compensación | Derecho legal e intención (74) | Derecho legal (596) |
| Clasificación | Sin regla en esta edición | No corriente (597) |
| Conciliación | Obligatoria (81(c)) | Pequeñas y medianas pueden omitirla; toda entidad que ajusta por inflación puede omitirla (599(f)) |

### Recurso canónico del componente 2

La RT 54 (T.O. RT 59 y modificatorias), párrafos 571-600, publicada por el CPCE CABA (fuente 2.1), con el párrafo 83 y el apartado de transición como complemento. Para la nota: párr. 572-573 (quién), 580-584 (reconocimiento y excepciones), 587 (descuento), 596-599 (presentación).

### Huecos del componente 2

- La RT 17 no se descargó: no se verificó qué permitía respecto del descuento ni del método del impuesto a pagar; solo consta que la RT 54 lo permite (párr. 587).
- Importes de ingresos que separan pequeña, mediana y grande: definidos por la FACPCE, fuera del texto leído.
- Efecto contable detallado del cambio de política al pasar de categoría: no leído.
- Interacción con el ajuste por inflación impositivo: la RT no la trata expresamente; falta una fuente secundaria (informe profesional, doctrina) que lo explique. No se buscó, por límite de rondas.
- Comparación RT 54 original frente a RT 59 en esta sección: no hecha.

---

## Posición contraria: críticas documentadas al impuesto diferido

### Tabla de fuentes

| # | Fuente | URL | Tipo | Lectura | A | P | E | U |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Görlitz y Dobler, «Financial accounting for deferred taxes: a systematic review of empirical evidence», Management Review Quarterly (publicado en línea en 2021) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8475851/ | Secundaria académica (revisión sistemática) | [S] primeros 100.000 de 195.425 caracteres, vía el lector de la herramienta | 2 | 3 | 1 | 3 |
| 3.2 | Brouwer y Naarding, «Making Deferred Taxes Relevant» (octubre de 2017), documento presentado en un evento de la IFRS Foundation | https://www.ifrs.org/-/media/feature/events-and-conferences/2017/november/deferred-taxes.pdf?la=en | Primaria académica (paper de trabajo) | [L] resumen e introducción | 2 | 2 | 1 | 3 |
| 3.3 | IASB, staff paper 19E (mayo 2016), «Income Taxes feedback from the 2015 Agenda Consultation» | https://www.ifrs.org/content/dam/ifrs/meetings/2016/may/iasb/income-taxes/ap19e-appendix-e-feedbackback-from-2015-consult-agenda.pdf | Primaria (emisor de normas) | [L] párrafos 7-19 | 3 | 2 | 1 | 3 |
| 3.4 | IFRS Foundation, página del proyecto completado «Income taxes» | https://www.ifrs.org/projects/completed-projects/2016/income-taxes/ | Primaria | [L] | 3 | 1 | 1 | 2 |

### Afirmaciones

**El emisor de normas dejó la NIC 12 como estaba**
- La IASB decidió en mayo de 2016 "not to develop a replacement to, or amendment of, IAS 12" y "not to carry out further research in this area", tras la consulta de agenda 2015 y una revisión de las investigaciones (3.4). Es la posición institucional: las críticas conviven con una norma sin cambios.

**Lo que dijeron usuarios y preparadores (3.3)**
- 70 de 119 cartas comentaron el proyecto; en la prioridad (63 respuestas): 13 la pusieron alta, 24 media y 26 baja (párr. 18). Entre quienes la pusieron baja: "IAS 12 is not fundamentally broken" (18(c)(i)).
- Entre quienes la pusieron alta: "the time value of money is not reflected under the current Standard" (18(a)(iii)); y "investors found it difficult to make assumptions about future taxes based on the current information disclosed" (18(a)(i)). Media: "deferred tax accounting is complex and should be simplified" (18(b)(iv)).
- Encuesta en línea, 169 respuestas: 27 la pusieron alta (10 usuarios), 69 media (36 usuarios), 29 baja (17 usuarios) (párr. 19). Motivos de la prioridad alta: "Preparers tend not to account for deferred tax assets and create a too low tax rate for later years (one user)"; "Forward looking information, including key drivers of tax expense (taxes paid), is missing" (varios usuarios); "Deferred tax is too complex and amounts should be discounted (one non-user)" (19(a)).
- Lectura: la crítica de los usuarios en este documento es de información faltante (tasas efectivas, impuestos pagados), no de eliminar el diferido. No se encontró en esta fuente un testimonio directo de analistas que ignoran el diferido (hueco).

**Relevancia valorativa y flujos de caja (3.1, 3.2)**
- Brouwer y Naarding: "Empirical evidence, particularly from more recent research, indicates that the current comprehensive balance sheet approach of IAS 12 provides insufficient value-relevant information to investors, since there is only a weak relationship between deferred tax balances and future tax cash flows (e.g. see Laux, 2013)." (introducción). Conclusiones del resumen: reconocer diferidos "only ... for temporary differences that will result in actual future tax payments and/or tax receipts"; la asignación parcial en lugar de la completa; y medir "on a discounted basis to address time value".
- Argumentan también que la crítica al modelo de balance integral lleva décadas ("has been criticised for several decades") y que la IASB "insufficiently considered the empirical academic results" (introducción). Es un paper de posición, no una evidencia neutral: el segundo autor figura con correo personal y el primero con afiliación a una firma de auditoría y a la universidad.
- Revisión sistemática (3.1, según el lector, no verificado en el texto completo): los diferidos son percibidos como relevantes por el mercado ("The capital market perceives deferred taxes as value relevant"), con activos y provisión de valuación más relevantes que los pasivos, cuyos resultados varían; "analysts correctly value the information inherent in deferred tax variables". Es la evidencia contraria a la tesis de que se ignoran.
- Críticas citadas en la revisión: bajo la visión de pasivo, los flujos de caja diferidos son inciertos y su valor presente está cerca de cero; "the replacement of reversed deferred taxes by new deferred taxes delays the final reversal of deferred taxes indefinitely"; y la prohibición de descontar "leads to an overstatement of deferred taxes".
- Cita secundaria de la búsqueda (sin verificar en origen): Amir, Kirschenheiter y Willard (1997) como fuente de que el valor de los diferidos es el valor presente de los beneficios fiscales; un estudio alemán de 2024 sobre firmas del HDAX que no encuentra efecto significativo de los activos diferidos en el valor de mercado. [S]

**Discusión sobre el descuento**
- Hay posiciones enfrentadas con textos de fuente: la NIC 12 lo prohíbe por impracticabilidad y comparabilidad (párr. 54); la RT 54 lo permite (587); los académicos lo reclaman (3.1, 3.2); los usuarios solo lo señalan en uno de los motivos (3.3).

### Recurso canónico de la posición contraria

El staff paper 19E de la IASB (3.3) para saber qué dijeron usuarios y preparadores, y el paper de Brouwer y Naarding (3.2) para el argumento académico completo. La revisión sistemática de Görlitz y Dobler (3.1) para el contrapeso empírico; conviene leerla completa antes de citar cifras.

### Huecos de la posición contraria

- No hay una fuente primaria que muestre a analistas que ignoran el impuesto diferido; la revisión empírica va en sentido contrario (el mercado lo valora).
- La revisión de Görlitz y Dobler se leyó solo en su primera mitad y por resumen automático; las frases entre comillas son del lector y deben cotejarse con el texto.
- Estudios de Laux (2013), Amir et al. (1997) y el estudio HDAX 2024 no se leyeron.
- Críticas de emisores de normas distintos de la IASB (FASB, EFRAG/ASB 2011) apenas mencionadas (el paper 3.2 cita el documento de discusión EFRAG-ASB de 2011); no leídos.
- Contexto latinoamericano o argentino de la crítica: no buscado.
