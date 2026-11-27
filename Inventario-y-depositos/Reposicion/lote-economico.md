---
resumen: >-
  El lote económico (EOQ) es la cantidad por pedido que hace mínimo el costo de pedir más el de mantener, cuando la demanda es constante: Q* = √(2DK/h). Lo publicó Ford Whitman Harris en 1913; R. H. Wilson lo difundió después. Es una aproximación con supuestos fuertes. Sirve porque el costo cambia poco cerca del óptimo (criterio de la base, por el ejemplo numérico de abajo).
estado: borrador
estabilidad: estable
fuentes:
  - "Harris, F. W. (1913), How many parts to make at once, Factory, The Magazine of Management, febrero de 1913, 10:135-136, 152; reimpreso en Operations Research 38(6):947-950, 1990 (según el registro): https://doi.org/10.1287/opre.38.6.947"
  - "Ford Whitman Harris and the Economic Order Quantity Model, Operations Research 38(6):937-946, 1990 (según el resumen): https://doi.org/10.1287/opre.38.6.937"
  - "Erlenkotter, D. (2014), Ford Whitman Harris's economical lot size model, International Journal of Production Economics 155:12-15 (metadatos): https://doi.org/10.1016/j.ijpe.2013.12.008"
  - "Wikipedia, Economic order quantity (fórmula, ejemplo numérico, supuestos, Wilson y la crítica de Cargal): https://en.wikipedia.org/wiki/Economic_order_quantity"
  - "Caplice, C. (MIT CTL), Inventory Management: Probabilistic Demand, ESD.260 lección 11, octubre de 2006, diapositivas 11 y 18: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf"
  - "Caplice, C. (MIT CTL), Inventory Management: More Probabilistic Demand, ESD.260 lección 12, diapositiva 5: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/bc18dd1b2543535a61f826d00a8c6e42_lect12.pdf"
  - "Inventario-y-depositos/.investigacion/reposicion.md (sección 3)"
  - "Inventario-y-depositos/.investigacion/fundamentos-y-contraria.md (secciones 2 y 4.2)"
aliases: [lote económico, lote económico de compra, cantidad económica de pedido, economic order quantity, EOQ, fórmula de Wilson, fórmula de Harris, economic lot size, tamaño de lote, stock de ciclo, cycle stock]
creado: 2026-11-27
revisado:
---

# Lote económico

El lote económico (EOQ) es la cantidad por pedido que hace mínimo el costo de pedir más el de mantener, cuando la demanda es constante: Q* = √(2DK/h). Lo publicó Ford Whitman Harris en 1913; R. H. Wilson lo difundió después. Es una aproximación con supuestos fuertes. Sirve porque el costo cambia poco cerca del óptimo (criterio de la base, por el ejemplo numérico de abajo).

Contesta el «cuánto» de una política de [reposición](reposicion.md), y es la Q de la política (s, Q) del [punto de pedido](punto-de-pedido.md). Dimensiona el stock de ciclo: en promedio, la mitad del lote está en el depósito.

## La fórmula y lo que pesa en ella

Q* = √(2DK/h)

D es la demanda anual, K el costo fijo de cada pedido y h el costo anual de mantener una unidad. El costo total del año es T = PD + KD/Q + hQ/2, con P el precio unitario. KD/Q son los pedidos del año por lo que cuesta cada uno; hQ/2 es el stock promedio por lo que cuesta guardarlo. Pedir más grande baja el primer término y sube el segundo, y Q* es donde se igualan.

El precio no aparece en Q*: «Q* is independent of P; it is a function of only K, D, h». Pero h suele calcularse como un porcentaje del precio (la tasa de mantener de [reposición](reposicion.md)), así que el precio entra por ahí. En la notación del MIT, con A el costo por pedido, v el costo unitario y r la tasa anual, h = v·r.

## Dos ejemplos con las cuentas

El ejemplo de la entrada de Wikipedia: D = 10.000 unidades al año, K = 40 por pedido, P = 50 y h = 4 + 50 × 2 % = 5 por unidad y año.

- Q* = √(2 × 10.000 × 40 / 5) = √160.000 = 400 unidades, o 25 pedidos al año.
- Costo total con 400: 502.000. Con 500: 502.050. Con 300: 502.083,33.

El ejemplo del MIT: «EOQ = 228 units (A=50 $/order, r=10%, v=250 $/item)», con D = 13.000 al año. La cuenta da √(2 × 50 × 13.000 / (0,10 × 250)) = √52.000 ≈ 228.

## Por qué equivocarse un poco cuesta poco

El primer ejemplo muestra lo plano que es el costo cerca del óptimo. Sin el precio de compra, que no cambia con el lote, el costo de pedir más el de mantener es 2.000 en el óptimo. Pedir 500 (un 25 % más) lo sube a 2.050, un 2,5 %; pedir 300 (un 25 % menos), a 2.083,33, un 4,2 %. Las proporciones son cuenta de la base sobre los números de la fuente.

Por eso el EOQ sirve aunque sus datos sean aproximados: un costo de pedir o una tasa de mantener mal estimados mueven poco el costo total. También por eso conviene redondear el lote a lo que el proveedor vende (una caja, un pallet) sin culpa. Esta conclusión práctica es inferencia de la base.

## Los supuestos, y dónde se rompen

La fórmula vale bajo supuestos que la misma fuente enumera:

| Supuesto | Dónde se rompe |
|---|---|
| «EOQ applies only when demand for a product is constant over a period of time» | demanda estacional, con tendencia o con promociones |
| Cada pedido llega completo cuando el stock llega a cero | entregas parciales; plazo variable, que pide [stock de seguridad](stock-de-seguridad.md) |
| Costo fijo por pedido | fletes por escalón, preparación que se puede reducir |
| Un solo artículo por pedido | pedidos conjuntos de varios artículos al mismo proveedor |
| Costo de mantener por unidad y por año | depósito con capacidad fija; productos que vencen |

La segunda columna es lectura de la base. Wikipedia recoge que el EOQ fue criticado por «their restrictive set of assumptions», y la observación de Cargal (2003): la fórmula se pensó para el cálculo a mano, y hoy una planilla permite supuestos más realistas.

> [!NOTE] Sin fuente todavía: cuánto se pierde por usar el EOQ con demanda variable, cómo cambia con descuentos por cantidad y la crítica de lean, que trata el costo de preparación como algo que se reduce y no como un dato (está en el campo, pero no se leyó un texto que la plantee contra el EOQ).

## Del lote fijo a la revisión periódica

Con revisión periódica, el lote deja de ser una cantidad fija: cada R días se pide lo que falta hasta un máximo. El MIT traduce una política en la otra con Q → D·R: lo que se pide en promedio es la demanda del período. Con el EOQ se puede elegir el período: 13.000 al año en lotes de 228 son unos 57 pedidos, algo más de uno por semana. La cuenta es de la base. Las políticas están en [punto de pedido](punto-de-pedido.md).

## Harris, no Wilson

Ford Whitman Harris publicó el modelo en febrero de 1913, en la revista *Factory, The Magazine of Management*, con el título «How many parts to make at once». Según el resumen de la reimpresión de 1990, su lógica era que el costo del capital inmovilizado limita cuántas piezas conviene hacer por tanda, y el costo de preparación fija el otro extremo.

El artículo quedó olvidado. Un estudio de 1990 en *Operations Research* empieza: «Ford Whitman Harris first presented the familiar economic order quantity (EOQ) model in a paper published in 1913», y cuenta, según su resumen, que el modelo pasó inadvertido hasta su redescubrimiento en 1988. Erlenkotter (2014) lo llama «one of the most cited and applied results in production and operations management».

La difusión se atribuye a R. H. Wilson, que publicó «A Scientific Routine for Stock Control» en *Harvard Business Review* en 1934 (una sola fuente secundaria). De ahí el nombre «fórmula de Wilson» (que sea corriente en castellano es lectura de la base). Decir que la inventó Wilson es un error documentado.

> [!IMPORTANT] Fecha discutida: el registro de la reimpresión dice febrero de 1913. Otros trabajos de Erlenkotter (1989 y 1990) hablan del modelo «de 1915», según el informe de la base. Para zanjarlo hay que leer a Harris o a Erlenkotter (1990).

Para leer más: el artículo de Harris reimpreso en *Operations Research* 38(6), 1990, son cuatro páginas; fijarse en que plantea el problema como preparación contra capital inmovilizado, que es el mismo tironeo de hoy.
