---
resumen: >-
  La reposición es la decisión de cuándo y cuánto traer de cada artículo para que el stock cumpla su función sin costar de más. Se apoya en una cuenta de tres costos (pedir, mantener y quedarse sin stock) y en unas pocas políticas que miran la posición de stock y disparan un pedido.
estado: vigente
estabilidad: estable
fuentes:
  - "Caplice, C. (MIT CTL), Inventory Management: Probabilistic Demand, ESD.260 lección 11, octubre de 2006, diapositivas 5-12 y 25 (remite a Silver, Pyke y Peterson como libro de texto): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf"
  - "Trusted Institute, Inventory Planning Fundamentals and Functions (material de preparación CPIM, secundario; no cita el Diccionario APICS): https://trustedinstitute.com/concept/cpim/inventory-management/inventory-planning-fundamentals/"
  - "Hopp y Spearman (2004), To Pull or Not to Pull: What Is the Question?, MSOM 6(2):133-148 (según el resumen del registro): https://doi.org/10.1287/msom.1030.0028"
  - "Inventario-y-depositos/.investigacion/reposicion.md (sección 1)"
  - "Inventario-y-depositos/.investigacion/fundamentos-y-contraria.md (secciones 3 y 4.5)"
aliases: [reposición, reabastecimiento, replenishment, política de inventario, inventory policy, funciones del inventario, costos del inventario, costo de mantener, holding cost, carrying cost, costo de pedir, ordering cost, costo de faltante, stockout cost]
creado: 2026-11-27
revisado: 2026-11-27
---

# Reposición

La reposición es la decisión de cuándo y cuánto traer de cada artículo para que el stock cumpla su función sin costar de más. Se apoya en una cuenta de tres costos (pedir, mantener y quedarse sin stock) y en unas pocas políticas que miran la posición de stock y disparan un pedido.

Es la cuarta parte de [Inventario y depósitos](../inventario-y-depositos.md). Lee de [Existencias](../Existencias/existencias.md) cuánto hay y en qué [estado](../Existencias/estados-del-stock.md), y le pasa a Compras y abastecimiento la cantidad a pedir; a quién se le compra y en qué condiciones es de Compras. Lo que llega entra por la [recepción](../Operacion-del-deposito/recepcion.md). Todas sus cuentas suponen que el número del registro es el del estante, y eso lo cuida [Control del stock](../Control-del-stock/control-del-stock.md).

## Para qué se tiene stock

El stock existe porque cumple funciones distintas, y cada función se dimensiona con una herramienta distinta. El material de preparación de la certificación CPIM (fuente secundaria) lista siete:

| Función | Qué es | Dónde se decide |
|---|---|---|
| Anticipación | «Inventory built up in advance to meet expected increases in demand» | pronóstico y plan agregado, de Cadena de suministro y logística |
| Ciclo | «The portion of inventory that results from ordering or producing in lots or batches» | [lote económico](lote-economico.md) |
| Seguridad | colchón contra la incertidumbre de la demanda y del plazo | [stock de seguridad](stock-de-seguridad.md) |
| Fluctuación | «Inventory carried to cover random, unpredictable variations in supply and demand» | casi sinónimo de seguridad |
| Cobertura (hedge) | compra contra un aumento de precio o una escasez | Compras y abastecimiento |
| Tránsito (pipeline) | «Inventory that is currently in transit between locations in the supply chain» | Cadena de suministro y logística |
| Desacople | «Inventory held between stages of a production process or supply chain» | Producción, o la cadena |

Lo que va entre comillas es de la fuente; las descripciones sin comillas (seguridad, cobertura) y la columna «Dónde se decide» son criterio de la base. Reposición se queda con el stock de ciclo y el de seguridad; los demás se nombran para no confundirlos.

> [!NOTE] Sin fuente todavía: la lista de funciones del Diccionario APICS. Una búsqueda atribuyó al CPIM Learning System otra lista de seis (anticipación, cobertura, ciclo, fluctuación, transporte y repuestos de servicio), solo de forma secundaria.

## Los tres costos que se equilibran

Toda política de reposición equilibra tres costos:

- **Pedir o preparar**: lo que cuesta cada pedido, sin importar su tamaño (armarlo, recibirlo, preparar una máquina).
- **Mantener**: lo que cuesta tener una unidad guardada durante un año. Se expresa como porcentaje anual del valor del artículo. La misma fuente CPIM dice «often 20-35% annually» (un solo dato secundario) y lo desglosa en capital inmovilizado, almacenaje, riesgo (obsolescencia, rotura, hurto) y seguros e impuestos.
- **Faltante**: lo que se pierde por no tener stock cuando se lo pide (la venta, el cliente, una línea parada).

Las clases del MIT escriben el costo total relevante como «TRC = OrderCosts + HoldingCosts + StockOutCosts», con esta forma:

TRC = A(D/Q) + (Q/2 + kσL)vr + B1(D/Q)p_u≥(k)

A es el costo por pedido, D la demanda anual, Q la cantidad por pedido, v el costo unitario y r la tasa anual de mantener. El primer término son los pedidos del año; el segundo, el stock promedio (la mitad del lote más el stock de seguridad kσL) por lo que cuesta tenerlo; el tercero, el costo B1 de cada faltante por la probabilidad de faltar en cada ciclo. Los ejemplos del MIT usan r = 10 %, que es un dato de ejemplo y no del campo.

Pedir más seguido baja el stock promedio y sube los pedidos; pedir menos seguido baja los pedidos y sube el stock. Ese tironeo es el [lote económico](lote-economico.md). Subir el colchón baja los faltantes y sube el costo de mantener, y ese es el [stock de seguridad](stock-de-seguridad.md).

## Cómo se arma una política de reposición

Una política contesta dos preguntas: cuándo pedir y cuánto. Mira la **posición de stock**, que el MIT define como «IP = Inventory Position = (IOH) + (Inv On Order) – (Backorders) – (Committed)»: lo que hay en mano, más lo pedido que todavía no llegó, menos lo que se debe a clientes y lo que ya está comprometido. Lo comprometido sale de la [reserva](../Operacion-del-deposito/reserva.md), y es la misma resta que hace el [disponible para prometer](../Existencias/disponible-para-prometer.md).

Con eso, cada artículo recibe una política hecha de piezas que tienen nota propia:

1. Cuándo pedir: el [punto de pedido](punto-de-pedido.md), con revisión continua o cada cierto período.
2. Cuánto pedir: un lote fijo, a menudo el [lote económico](lote-economico.md), o lo que falte hasta un máximo.
3. Con qué colchón: el [stock de seguridad](stock-de-seguridad.md), que sale del nivel de servicio buscado.
4. Con cuánta atención: la [clasificación ABC](clasificacion-abc.md) dice qué artículos merecen la política más fina.

Los [indicadores de inventario](indicadores-de-inventario.md) dicen después si la política funcionó: cuántas veces rota el stock, cuántos días cubre, qué nivel de servicio se logró.

## Dónde termina la reposición

La reposición de este tema es la que decide artículo por artículo, mirando la posición de stock. Tres decisiones vecinas quedan afuera:

- El pronóstico de la demanda, el plan agregado (S&OP) y la reposición planificada por períodos en quien no fabrica (DRP) son de Cadena de suministro y logística. El punto de pedido usa un pronóstico, pero no lo hace.
- A quién se le compra, a qué precio y con qué orden de compra es de Compras y abastecimiento.
- Lo que se fabrica con lista de materiales se planifica con MRP, que es de Producción.

## Cómo falla una política de reposición

Las fórmulas de este tema son aproximaciones: suponen demanda estable, plazos conocidos y un registro exacto. Cada nota dice sus supuestos y dónde se rompen. La falla más común está antes de la fórmula: si el registro miente, la posición de stock miente, y el punto de pedido dispara tarde o no dispara.

Lean discute el punto de partida y ve el stock como un desperdicio que esconde problemas. Hopp y Spearman, según el resumen de su artículo, definen lean como «fundamentally about minimizing the cost of buffering variability»: no elimina el colchón, busca que cueste menos. La discusión entre las escuelas está en [Fundamentos](../Fundamentos/fundamentos-de-inventario-y-depositos.md).

## Qué hay en Reposición

- [Punto de pedido](punto-de-pedido.md): cuándo pedir; las cuatro políticas de revisión continua y periódica, el mínimo y máximo, y la fórmula del punto.
- [Lote económico](lote-economico.md): cuánto pedir con el EOQ de Harris, su ejemplo, sus supuestos y por qué el error cerca del óptimo cuesta poco.
- [Stock de seguridad](stock-de-seguridad.md): el colchón contra la incertidumbre, las dos maneras de medir el nivel de servicio y los límites de la fórmula.
- [Clasificación ABC](clasificacion-abc.md): qué artículos mirar más, por valor y, con XYZ, por variabilidad; también fija la frecuencia del conteo.
- [Indicadores de inventario](indicadores-de-inventario.md): rotación, días de inventario, nivel de servicio, exactitud y lo que todavía no tiene fuente.
