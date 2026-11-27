---
resumen: >-
  El artículo es el dato maestro de cada cosa que la empresa guarda, compra o vende: un código que la identifica, la unidad en que se cuenta con sus conversiones, y la decisión de si lleva stock o no. Todo movimiento y toda cantidad del tema cuelgan de un artículo.
estado: borrador
estabilidad: estable
fuentes:
  - "Bartholdi y Hackman, Warehouse & Distribution Science, versión 0.98.1 (16-ago-2019), cap. 2, p. 17-18 (SKU y slotting) y §3.3 (línea de pedido y línea de picking): https://www.warehouse-science.com/book/editions/wh-sci-0.98.1.pdf"
  - "Shopify, objeto ProductVariant de la Admin GraphQL API (variante y SKU), vía la nota de catálogo y stock: https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (2026-11-27), sección Artículo, unidad de medida (hueco declarado)"
  - "Inventario-y-depositos/.investigacion/operacion-del-deposito.md (2026-11-27)"
aliases: [artículo, ítem, item, producto, SKU, stock keeping unit, código de artículo, maestro de artículos, item master, unidad de medida, UOM, unit of measure, conversión de unidades]
creado: 2026-11-27
revisado:
---

# Artículo

El artículo es el dato maestro de cada cosa que la empresa guarda, compra o vende: un código que la identifica, la unidad en que se cuenta con sus conversiones, y la decisión de si lleva stock o no. Todo movimiento y toda cantidad del tema cuelgan de un artículo.

Es la primera coordenada de la fórmula de [existencias](existencias.md): sin artículo no hay cantidad. Cómo resuelve cualquier sistema los datos maestros en general (quién los da de alta, cómo se versionan) es del tema Software de gestión, todavía no armado. Acá va lo que el negocio necesita registrar del artículo para llevar stock.

## Un código por cada cosa que se cuenta por separado

Lleva código propio todo lo que se tiene que contar, ubicar o reponer por separado; esa es la regla que ordena el maestro de artículos, aunque el catálogo comercial muestre un solo producto. Una remera en tres talles y dos colores son seis cosas en el estante, y por eso seis códigos. En el modelo de una plataforma de tiendas la unidad que se vende es la variante, identificada por su SKU, y el stock cuelga de la variante; está en [catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md).

El campo usa SKU (stock keeping unit) en ese sentido. Bartholdi y Hackman llaman «slotting» a la disposición detallada que dice «exactly where each SKU should be located (for example, on the third shelf of the second section of aisle 2, oriented with case width to the front)». Lo que se ubica, se cuenta y se repone es el SKU, no el producto del catálogo.

De ahí sale el criterio para decidir si dos cosas son un artículo o dos (criterio de la base):

| Si las dos cosas... | Entonces |
|---|---|
| Se guardan en lugares distintos o se cuentan aparte | Son dos artículos |
| Tienen precio o costo distinto | Son dos artículos |
| Son la misma cosa de proveedores distintos, intercambiable para el cliente | Un artículo; el proveedor va en la compra o en el [lote](lote-y-serie.md) |
| Solo difieren en la partida o el vencimiento | Un artículo, seguido por [lote](lote-y-serie.md) |

> [!NOTE] Sin fuente todavía: una definición canónica de ítem y SKU (el APICS Dictionary no se pudo abrir) y una fuente sobre cómo se arma un código de artículo (significativo o correlativo).

## La unidad de medida y sus conversiones

Cada artículo tiene una unidad en la que se lleva el stock, y suele moverse en otras. Se compra por pallet, se guarda por caja y se vende por unidad. Bartholdi y Hackman dan el caso del depósito: un pedido de 15 unidades de un artículo que viene en cajas de 12 se convierte en dos líneas de picking, 1 caja y 3 unidades. El pedido habla en unidades; el depósito, en lo que tiene que levantar.

Para que eso funcione, el artículo guarda (criterio de la base):

- **Una unidad de stock**, la más chica en que se cuenta y se vende. Todos los saldos se llevan en ella.
- **Las conversiones** a las demás unidades: 1 caja = 12 unidades, 1 pallet = 40 cajas. Cada documento puede usar otra unidad, pero el movimiento se registra convertido.
- **Si la cantidad admite decimales.** Un artículo que se vende por kilo o por metro los necesita; uno que se vende por unidad, no.

El error típico, a juicio de la base, es tener la conversión en la cabeza del que carga: se recibe «10» pensando en cajas y el sistema suma 10 unidades. El [conteo](../Control-del-stock/conteo-ciclico.md) lo descubre después como una diferencia sin causa (criterio de la base).

> [!NOTE] Sin fuente todavía: una fuente primaria sobre unidad de medida y conversión en el maestro de artículos, y sobre el redondeo cuando una conversión no es exacta.

## Qué artículos llevan stock

No todo lo que se compra o se vende se cuenta. La distinción que hacen los sistemas de gestión es de tres clases (criterio de la base, sin fuente leída):

| Clase | Se cuenta | Ejemplo | Qué genera un movimiento |
|---|---|---|---|
| Con stock | Sí, por lugar y estado | mercadería de reventa, materia prima | recepción, salida, ajuste |
| Consumible | No: se da por usado al comprarlo | artículos de limpieza, cinta de embalar | nada en el stock; solo el gasto |
| Servicio | No hay nada que contar | flete, instalación, horas de soporte | nada |

La decisión importa porque un artículo con stock exige recibirlo, ubicarlo y contarlo, y uno sin stock no. Pasar un artículo de consumible a con stock más tarde pide un saldo inicial, que entra como un ajuste (ver [ajustes y mermas](../Control-del-stock/ajustes-y-mermas.md)).

> [!NOTE] Sin fuente todavía: la clasificación de artículos con stock, consumibles y servicios no se leyó en ninguna fuente; es la práctica habitual de los sistemas de gestión según la base.

## Qué más cuelga del artículo

El artículo es también el lugar donde se guardan las decisiones de las otras verticales sobre él:

- **Cómo se sigue**: sin seguimiento, por [lote](lote-y-serie.md) o por número de serie, y si tiene vencimiento.
- **Cómo se repone**: su [punto de pedido](../Reposicion/punto-de-pedido.md), su [stock de seguridad](../Reposicion/stock-de-seguridad.md) y su [lote económico](../Reposicion/lote-economico.md), que pueden variar por depósito.
- **Cuánta atención recibe**: su clase en la [clasificación ABC](../Reposicion/clasificacion-abc.md), que también fija cada cuánto se cuenta.
- **Dónde se guarda**: una ubicación fija o ninguna, en [ubicaciones](../Operacion-del-deposito/ubicaciones.md).

Lo que el artículo no guarda es su valor: el costo de cada entrada y el método de valuación son de Contabilidad, en [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md).
