---
resumen: >-
  El punto de pedido es el nivel de la posición de stock en que se dispara un pedido de reposición: la demanda esperada durante el plazo de entrega más un stock de seguridad. Con él se arman las cuatro políticas clásicas, de revisión continua o periódica, que deciden cuándo pedir y cuánto.
estado: borrador
estabilidad: estable
fuentes:
  - "Caplice, C. (MIT CTL), Inventory Management: Probabilistic Demand, ESD.260 lección 11, octubre de 2006, diapositivas 5-9: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf"
  - "Caplice, C. (MIT CTL), Inventory Management: More Probabilistic Demand, ESD.260 lección 12, octubre de 2006, diapositivas 3-6: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/bc18dd1b2543535a61f826d00a8c6e42_lect12.pdf"
  - "Kök y Shang (2007), Inspection and Replenishment Policies for Systems with Inventory Record Inaccuracy, MSOM 9(2):185-205 (según el resumen del registro): https://doi.org/10.1287/msom.1060.0136"
  - "Inventario-y-depositos/.investigacion/reposicion.md (secciones 2 y 4)"
  - "Inventario-y-depositos/.investigacion/fundamentos-y-contraria.md (sección 4.1)"
aliases: [punto de pedido, punto de reorden, reorder point, ROP, stock mínimo, mínimo y máximo, min-max, revisión continua, revisión periódica, continuous review, periodic review, (s, Q), (s, S), (R, S), (R, s, S), order-up-to level, nivel máximo, doble cajón, two-bin system, posición de stock, inventory position]
creado: 2026-11-27
revisado:
---

# Punto de pedido

El punto de pedido es el nivel de la posición de stock en que se dispara un pedido de reposición: la demanda esperada durante el plazo de entrega más un stock de seguridad. Con él se arman las cuatro políticas clásicas, de revisión continua o periódica, que deciden cuándo pedir y cuánto.

Es la pieza que dice «cuándo» en una política de [reposición](reposicion.md). El «cuánto» lo pone un lote fijo, a menudo el [lote económico](lote-economico.md), o un nivel máximo; el colchón lo pone el [stock de seguridad](stock-de-seguridad.md).

## La fórmula del punto

Las clases del MIT lo escriben así:

s = x̂L + kσL

x̂L es la demanda pronosticada durante el plazo de entrega L, k es el factor de seguridad y σL es el error del pronóstico en ese plazo (la raíz del error cuadrático medio, RMSE). El segundo término, kσL, es el [stock de seguridad](stock-de-seguridad.md), y cómo se elige k depende del nivel de servicio que se busque.

Con el ejemplo del MIT: demanda de 13.000 unidades al año, plazo de 2 semanas y error del pronóstico de 1.316 unidades al año. La demanda en el plazo es 13.000 × 2/52 = 500 y su desvío, 1.316/√26 = 258. Para no quedarse sin stock en el 95 % de los ciclos, el MIT da un stock de seguridad de 423, así que el punto de pedido queda en 500 + 423 = 923 unidades. La suma final es cuenta de la base sobre los datos de la fuente.

El pronóstico que entra en la fórmula lo hace Cadena de suministro y logística; el punto de pedido solo lo usa.

## Qué se compara con el punto: la posición de stock

El punto se compara con la **posición de stock**, no con lo que hay en el estante. El MIT la define como «IP = Inventory Position = (IOH) + (Inv On Order) – (Backorders) – (Committed)»: lo que hay en mano, más lo pedido que todavía no llegó, menos lo que se debe a clientes y lo ya comprometido. Mirar solo el estante hace pedir dos veces lo mismo mientras el primer pedido viaja (inferencia de la base).

Lo comprometido sale de la [reserva](../Operacion-del-deposito/reserva.md), y los estados que suman o restan están en [estados del stock](../Existencias/estados-del-stock.md). Es la misma resta que hace el [disponible para prometer](../Existencias/disponible-para-prometer.md), con otro fin: aquel dice cuánto se le puede prometer a un cliente; esta, cuándo hay que pedir más.

## Las cuatro políticas

El MIT usa esta notación: «s = Order Point, S = Order-up-to Level, L = Order Lead Time, Q = Order Quantity, R = Review Period». La revisión es continua cuando R = 0 (se mira la posición después de cada movimiento) y periódica cuando R > 0 (se mira cada R días).

| Política | Revisión | Regla, literal | Nombre corriente |
|---|---|---|---|
| (s, Q) | continua | «Order Q if IP ≤ s» | doble cajón (two-bin system) |
| (s, S) | continua | «Order (S-IP) if IP ≤ s» | mínimo y máximo (min-max) |
| (R, S) | periódica | «Order S-IP every R time periods» | ciclo de reposición |
| (R, s, S) | periódica | «Order S-IP if IP ≤ s every R time periods, if IP>s then do not order» | híbrido |

El doble cajón es la versión física de (s, Q): cuando se vacía el primer cajón, se pide; el segundo cajón es el punto de pedido (lectura de la base). El «stock mínimo» de una planilla con alerta de reponer, como el de [planilla de stock](../../Planillas-de-calculo/Diseno-de-planillas/planilla-de-stock.md), es un punto de pedido puesto a ojo, sin la fórmula (lectura de la base).

## Continua o periódica

El MIT resume la diferencia en dos ventajas. La revisión continua es «Able to provide same level of service with less safety stock». La periódica permite «Coordination of replenishments» (pedir varios artículos juntos al mismo proveedor) y es «Able to predict workload».

La razón del primer punto: en la revisión periódica, el colchón tiene que cubrir el plazo más el período entre revisiones. El MIT lo traduce con un cambio de variables, de (s, Q) a (R, S): s pasa a S, Q pasa a D·R y L pasa a R + L. Con el mismo artículo y revisión cada 8 semanas, el pedido típico es 13.000 × 8/52 = 2.000, la demanda a cubrir es la de 10 semanas (2.500) y su desvío, 577. Con un fill rate del 95 % el MIT llega a «S = xR+L + kσR+L = 2500 + (.58)(577) = 2835 units», o sea, pedir hasta 2.835 unidades cada 8 semanas. Cómo sale k = 0,58 está en [stock de seguridad](stock-de-seguridad.md).

## Qué política para qué artículo

El MIT da una regla práctica por clase ABC y avisa: «No hard and fast rules, but some rules of thumb».

| Clase | Revisión continua | Revisión periódica |
|---|---|---|
| A | (s, S) | (R, s, S) |
| B | (s, Q) | (R, S) |
| C | manual, parecido a (R, S) | |

Las clases salen de la [clasificación ABC](clasificacion-abc.md).

## Cómo falla el punto de pedido

- **El registro está mal.** La posición de stock hereda el error del registro. DeHoratius y Raman encontraron inexacto el 65 % de los registros de un minorista (según el resumen; está en [control del stock](../Control-del-stock/control-del-stock.md)). Si el sistema cree que hay más, el punto no se cruza y el pedido no sale. Kök y Shang, según el resumen de su artículo, proponen con registros inexactos una política que inspecciona cuando el registro cae bajo un umbral y pide hasta un nivel que depende del tiempo desde la última inspección. Un [conteo cíclico](../Control-del-stock/conteo-ciclico.md) con niveles que dependen del estado rinde casi igual.
- **No se resta lo comprometido.** Si los pedidos de clientes no reservan, la posición incluye stock que ya es de otro.
- **El punto quedó fijo y la demanda cambió.** La fórmula usa un pronóstico; si nadie la recalcula, el punto de la temporada pasada dispara tarde o de más. Es criterio de la base.
- **Los supuestos de la fórmula no se cumplen.** Demanda normal, independiente y plazo fijo: los límites están en [stock de seguridad](stock-de-seguridad.md).

Para leer más: Caplice, lección 11, diapositivas 5 a 9, tiene el vocabulario y las cuatro políticas en cuatro páginas.
