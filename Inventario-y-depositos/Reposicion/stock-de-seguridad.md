---
resumen: >-
  El stock de seguridad es el stock que se tiene de más, por encima de la demanda esperada durante el plazo de reposición, para cubrir la incertidumbre de la demanda y del plazo. Se calcula como un factor de seguridad por el desvío de la demanda en el plazo, y el factor sale del nivel de servicio buscado; la fórmula es una aproximación que falla cuando la demanda no es normal ni independiente.
estado: vigente
estabilidad: estable
fuentes:
  - "Caplice, C. (MIT CTL), Inventory Management: Probabilistic Demand, ESD.260 lección 11, octubre de 2006, diapositivas 9-28 (remite a Silver, Pyke y Peterson, ecuaciones 7.19, 7.20 y 7.23): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf"
  - "Caplice, C. (MIT CTL), Inventory Management: More Probabilistic Demand, ESD.260 lección 12, octubre de 2006, diapositivas 3-6: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/bc18dd1b2543535a61f826d00a8c6e42_lect12.pdf"
  - "Wikipedia, Safety stock (fórmula con plazo variable, supuestos y límites): https://en.wikipedia.org/wiki/Safety_stock"
  - "Eppen y Martin (1988), Determining Safety Stock in the Presence of Stochastic Lead Time and Demand, Management Science 34(11):1380-1390 (según el resumen): https://doi.org/10.1287/mnsc.34.11.1380"
  - "Chopra, Reinhardt y Dada (2004), The Effect of Lead Time Uncertainty on Safety Stocks, Decision Sciences 35(1):1-24 (según el resumen): https://doi.org/10.1111/j.1540-5414.2004.02332.x"
  - "DeHoratius y Raman (2008), Inventory Record Inaccuracy: An Empirical Analysis, Management Science 54(4):627-641 (según el resumen): https://doi.org/10.1287/mnsc.1070.0789"
  - "Inventario-y-depositos/.investigacion/reposicion.md (sección 4)"
  - "Inventario-y-depositos/.investigacion/fundamentos-y-contraria.md (sección 4.3)"
aliases: [stock de seguridad, inventario de seguridad, existencia de seguridad, safety stock, SS, colchón, buffer stock, nivel de servicio, service level, nivel de servicio por ciclo, cycle service level, CSL, fill rate, tasa de cumplimiento, item fill rate, IFR, factor de seguridad, safety factor]
creado: 2026-11-27
revisado: 2026-11-27
---

# Stock de seguridad

El stock de seguridad es el stock que se tiene de más, por encima de la demanda esperada durante el plazo de reposición, para cubrir la incertidumbre de la demanda y del plazo. Se calcula como un factor de seguridad por el desvío de la demanda en el plazo, y el factor sale del nivel de servicio buscado; la fórmula es una aproximación que falla cuando la demanda no es normal ni independiente.

Es el segundo término del [punto de pedido](punto-de-pedido.md), s = x̂L + kσL, y una de las funciones del stock que lista [reposición](reposicion.md). Las fuentes lo tratan junto con el punto de pedido como un solo problema; está aparte porque se enlaza desde más lugares.

## La fórmula y el ejemplo

Stock de seguridad = k × σL

σL es el desvío de la demanda durante el plazo de entrega. En las clases del MIT es el error del pronóstico en ese plazo (la raíz del error cuadrático medio), no el desvío histórico de las ventas. k es el factor de seguridad: cuántos desvíos de colchón se ponen.

Si el desvío se conoce por semana y el plazo es de n semanas, el MIT da: «E[L] = nE[S]; VAR[L] = nVAR[S] so that σL = √n σS». La varianza crece con el plazo, y el desvío, con su raíz.

El ejemplo del MIT: demanda de 13.000 unidades al año, normal e independiente, plazo de 2 semanas, error del pronóstico de 1.316 al año. Da «σL=258 units and μL=500 units»: 13.000 × 2/52 = 500 y 1.316/√26 = 258. Para un nivel de servicio por ciclo del 95 %, k = 1,645 y el stock de seguridad es de unas 424 unidades; el MIT da 423.

## Dos maneras de medir el nivel de servicio

El k sale del nivel de servicio, y hay dos definiciones que dan números muy distintos para el mismo porcentaje. El MIT avisa: «Definitions in practice are fuzzy».

**Nivel de servicio por ciclo** (CSL, o P1): «Probability of no stockouts per replenishment cycle. Equal to one minus the probability of stocking out». Con demanda normal, el CSL es la probabilidad acumulada de la normal estándar en k. Un CSL del 95 % quiere decir que en 95 de cada 100 ciclos no se falta, sin importar cuánto se falta en los otros 5.

**Fill rate** (IFR, o P2): «Fraction of demand filled from IOH», la parte de la demanda que se atiende con lo que hay en mano. Se calcula con las unidades que se espera que falten por ciclo:

- «IFR = (Q − E[US])/Q = 1 − E[US]/Q = 1 − σL G[k]/Q», donde Q es el lote y E[US] las unidades faltantes esperadas.
- Con demanda normal, «E[US] = σL G(k)», donde G(k) es la función de pérdida de la normal estándar.
- Para despejar k: «G[k] = (Q/σL)(1 − IFR)».

La diferencia, en palabras del MIT: «IFR usually much higher than CSL for same SS. IFR depends on both s and Q while CSL is independent of all product characteristics». Con el ejemplo de 13.000 al año:

| Nivel buscado | Stock de seguridad por CSL | Stock de seguridad por fill rate |
|---|---|---|
| 99 % | 601 | 513 |
| 95 % | 423 | 348 |
| 90 % | 330 | 252 |
| 80 % | 217 | 148 |

Los valores son los de la tabla del MIT. Rehecha la cuenta con la misma fórmula, la fila del 95 % por fill rate da unas 339 unidades y no 348; las otras filas cierran. No se pudo saber de dónde sale la diferencia.

Quien pide «95 % de servicio» tiene que decir cuál de los dos; la diferencia, en este artículo, es de 75 unidades. De la fórmula del fill rate se desprende que un lote más grande lo sube con el mismo colchón, porque los faltantes de cada ciclo se reparten sobre más unidades.

Con revisión periódica, el MIT usa el fill rate. Para pedir cada 8 semanas con IFR = 0,95: «Gu[k] = (1-.95)(2000/577) = 0.1733 giving k=0.58», y el nivel máximo queda en 2.835 unidades. El resto de ese ejemplo está en [punto de pedido](punto-de-pedido.md).

## Cuando el costo de faltar se conoce

Si se sabe cuánto cuesta cada faltante, el k se puede despejar del costo en vez de elegir un nivel de servicio. El MIT da dos casos:

- Costo B1 por cada vez que se falta: si DB1/(√(2π) Q v σL r) < 1, se usa el k mínimo que se acepte; si no, k = √(2 ln(DB1/(√(2π) Q v σL r))).
- Costo B2 por unidad faltante: se elige k con p_u≥(k) = Qr/(D B2). Que p_u≥(k) sea la probabilidad de que una normal estándar alcance o supere k es lectura de la base.

A es el costo por pedido, D la demanda anual, Q el lote, v el costo unitario y r la tasa de mantener. Las raíces de estas dos fórmulas se perdieron al extraer el PDF y el informe las reconstruyó: hay que verificarlas contra Silver, Pyke y Peterson, ecuaciones 7.19 y 7.20.

## Cuando el plazo también varía

Las fórmulas del MIT suponen un plazo fijo. Con demanda y plazo aleatorios, Wikipedia da:

SS = z_α × √(E(L)·σD² + (E(D))²·σL²)

E(L) es el plazo medio, σD el desvío de la demanda por período, E(D) la demanda media por período y σL el desvío del plazo; z ≈ 1,65 para el 95 %. Con plazo fijo, el punto de pedido queda en ROP = L·E(D) + z_α·σD·√L. Ojo con la notación: en esta fórmula σL es el desvío del plazo, y en la del MIT es el desvío de la demanda en el plazo.

## Por qué la fórmula no da el número

Wikipedia lo dice sin vueltas: «No universal formula exists for safety stock, and application of the one above can cause serious damage». Los supuestos son demanda independiente, idénticamente distribuida y normal, con media y desvío constantes, y se rompen así:

- La demanda real no es negativa, y con un coeficiente de variación alto la normal sesga el resultado (tiende a sobrestimar).
- Las demandas sucesivas no son independientes.
- La estacionalidad y la tendencia rompen la constancia.
- El plazo es difícil de medir en cadenas con varios socios, y la oferta no siempre es estable.
- Lo perecedero se echa a perder antes de usarse como colchón.

Dos artículos primarios, leídos solo por su resumen, van en la misma dirección. Eppen y Martin (1988) sostienen que un procedimiento estándar de la literatura puede dar resultados lejos del nivel buscado cuando el plazo y la demanda son aleatorios, y presentan uno corregido («A correct procedure is presented.»). Chopra, Reinhardt y Dada (2004) argumentan que lo que la aproximación normal concluye sobre la variabilidad del plazo es erróneo en el rango de servicio donde opera la mayoría de las empresas, y que a veces conviene acortar el plazo antes que reducir su variabilidad.

Hay un supuesto más, que ninguna fórmula escribe: que el registro es exacto. DeHoratius y Raman encontraron inexacto el 65 % de casi 370.000 registros de 37 tiendas de un minorista (según el resumen). Si el registro está mal, el colchón calculado sobre él no cubre lo que dice cubrir. Cómo se corrige el número está en [control del stock](../Control-del-stock/control-del-stock.md).

En la base, la fórmula se da como punto de partida: un k y un σL razonables, y después se mira el nivel de servicio real con los [indicadores de inventario](indicadores-de-inventario.md) y se ajusta. Es criterio de la base.

## El stock de seguridad en una tienda online

En [catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md), el stock de seguridad aparece como una defensa contra la sobreventa: unidades que no se publican para que varios canales no vendan la misma. Es el mismo nombre con otro fin. Aquel colchón cubre el atraso del registro entre canales; este cubre la incertidumbre de la demanda y el plazo de reposición. La distinción es de la base.

Para leer más: Caplice, lección 11, diapositivas 9 a 24, y lección 12, diapositivas 3 a 6, con los dos ejemplos resueltos. Fijarse en que CSL y fill rate dan stocks distintos para el mismo porcentaje. El libro base que cita el MIT es Silver, Pyke y Peterson («SPP»); su edición posterior es de Silver, Pyke y Thomas, *Inventory and Production Management in Supply Chains*, capítulo de sistemas de punto de pedido (no leído).
