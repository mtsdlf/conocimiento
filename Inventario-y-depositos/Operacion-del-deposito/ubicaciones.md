---
resumen: >-
  Una ubicación es un lugar del depósito con una dirección única donde puede haber stock, desde una porción de estante hasta las horquillas de un autoelevador. Las ubicaciones se ordenan en jerarquía (depósito, zona, ubicación) y se asignan a los artículos de manera fija o libre, una decisión que cambia cuánto espacio se aprovecha y cuánto control hace falta.
estado: borrador
estabilidad: estable
fuentes:
  - "Bartholdi y Hackman, Warehouse & Distribution Science, versión 0.98.1 (16-ago-2019), §2.4 (ubicación fija y compartida), cap. 2 p. 17-18 (slotting), §3.2-3.3 y §4.2 (stock locator): https://www.warehouse-science.com/book/editions/wh-sci-0.98.1.pdf"
  - "De Koster, Le-Duc y Roodbergen (2007), Design and control of warehouse order picking: a literature review, EJOR 182(2), 481-501, §4.1-4.3: https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf"
  - "Odoo 17.0, Use locations (jerarquía y tipos de ubicación; según su resumen): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations.html"
  - "Inventario-y-depositos/.investigacion/operacion-del-deposito.md (2026-11-27), sección 1"
aliases: [ubicación, ubicaciones, location, storage location, bin, posición, dirección de ubicación, direccionamiento, ubicación fija, dedicated storage, ubicación libre, ubicación compartida, shared storage, random storage, slotting, zona de picking, forward area, zona de reserva, reserve area, forward-reserve, stock locator]
creado: 2026-11-27
revisado:
---

# Ubicaciones

Una ubicación es un lugar del depósito con una dirección única donde puede haber stock, desde una porción de estante hasta las horquillas de un autoelevador. Las ubicaciones se ordenan en jerarquía (depósito, zona, ubicación) y se asignan a los artículos de manera fija o libre, una decisión que cambia cuánto espacio se aprovecha y cuánto control hace falta.

Es lo que responde el «dónde» de la cantidad de [Existencias](../Existencias/existencias.md): el stock de un artículo es la suma de lo que hay en cada ubicación. Las demás piezas de [Operación del depósito](operacion-del-deposito.md) la usan: la [recepción](recepcion.md) decide en cuál guardar, la [preparación de pedidos](preparacion-de-pedidos.md) camina entre ellas y el [conteo cíclico](../Control-del-stock/conteo-ciclico.md) puede organizarse por lugar.

## Cómo se arma una dirección

Bartholdi y Hackman parten de que cada lugar de guardado tiene una dirección única, tanto los fijos (un tramo de estante) como los móviles (las horquillas de un autoelevador). Un plano detallado del depósito dice dónde va cada artículo con la geometría completa; su ejemplo nombra el estante, la sección del estante y el pasillo. La ubicación es un recurso caro: cuesta alquiler, clima, seguridad y equipamiento.

En la práctica de los sistemas, las ubicaciones forman un árbol padre e hijo, con rutas del tipo depósito, existencias, zona A, heladera 1. La forma corriente, que la base adopta como vocabulario, es esta:

| Nivel | Qué es | Ejemplo |
|---|---|---|
| Depósito | un edificio o una sede con stock propio | el depósito central |
| Zona | un sector con una regla común (temperatura, rotación, función) | la cámara de frío, la zona de picking |
| Ubicación | el lugar exacto donde se apoya la mercadería | pasillo 2, sección 4, estante 3 |

La dirección conviene que se lea en el orden en que se camina (pasillo, sección, nivel), así quien prepara la sigue sin mapa; esto es criterio de la base.

## Ubicaciones que no son lugares

Los sistemas también modelan como ubicaciones lugares que no existen en el edificio: el proveedor, el cliente, la producción, el tránsito entre depósitos y la pérdida de inventario. Según el resumen de un sistema abierto, son tipos de ubicación «virtual». La ventaja es que toda salida y toda entrada quedan como un movimiento de una ubicación a otra: una venta va de un estante al cliente, una rotura va del estante a la ubicación de pérdidas. Los estados que resultan están en [estados del stock](../Existencias/estados-del-stock.md), y el registro de la merma, en [ajustes y mermas](../Control-del-stock/ajustes-y-mermas.md).

## Ubicación fija o ubicación libre

La decisión central es si cada artículo tiene su lugar o si va donde haya lugar. Bartholdi y Hackman la plantean como almacenamiento dedicado frente a compartido:

| | Ubicación fija (dedicada) | Ubicación libre (compartida) |
|---|---|---|
| Regla | cada ubicación es de un artículo y solo ese puede ir ahí | un artículo puede estar en varias ubicaciones; la que se vacía se reasigna |
| Espacio | en promedio se usa cerca del 50 % de la capacidad | se aprovecha más |
| Quien trabaja | aprende dónde está cada cosa | no puede aprenderlo; hay que dirigirlo con un sistema |
| Exigencia | baja | más software y procesos más disciplinados |

El ejemplo del libro: un artículo con dos semanas de stock repartido en dos ubicaciones iguales, que se prepara de a una por vez, ocupa el espacio al 75 % la primera semana y al 50 % la segunda, 62,5 % en el período. Con ubicación fija, el lugar queda reservado aunque esté vacío.

La ubicación libre pide llevar un segundo inventario, de lugares y no de productos: qué ubicaciones están vacías, de qué tamaño y cuánto peso soportan. Bartholdi y Hackman llaman «stock locator» a la capacidad de llevar los dos inventarios y es la que permite que el sistema diga dónde guardar y de dónde sacar.

Su falla típica también la describen ellos: si se manda a alguien a buscar un artículo al otro lado del depósito, puede tentarse de sacarlo de una ubicación más cómoda. El total cuadra y las dos ubicaciones quedan mal. Esa diferencia aparece en el [conteo cíclico](../Control-del-stock/conteo-ciclico.md).

## A qué ubicación va cada artículo

De Koster, Le-Duc y Roodbergen enumeran cinco políticas de asignación: al azar, a la ubicación libre más cercana, dedicada, por rotación total y por clases. La asignación por clases agrupa los artículos según su rotación y pone los de mayor movimiento cerca de la puerta; es la misma lógica que la [clasificación ABC](../Reposicion/clasificacion-abc.md), usada para el espacio en vez de para las compras. La revisión compara los resultados de las políticas, pero esa parte se leyó solo en parte y queda sin citar.

> [!NOTE] Sin fuente todavía: las reglas de guardado de un sistema de gestión de depósitos (por categoría, por capacidad, por lote) no se leyeron; la página de un sistema abierto que las describe no se pudo abrir.

## La zona de reserva y la zona de picking

Muchos depósitos separan el stock a granel de lo que se prepara. De Koster, Le-Duc y Roodbergen lo dicen así: suele ser eficiente separar la zona de reserva de la zona de picking, porque cuanto más chica la zona donde se prepara, más cortas las caminatas. La zona de picking tiene poco de cada artículo y a mano; la de reserva, el resto, en pallets o en altura.

La palabra «reserva» acá nombra un lugar. No tiene relación con la [reserva](reserva.md) de stock para un pedido, que es apartar una cantidad sin moverla; en esta base, el lugar se dice siempre «zona de reserva».

## La reposición de la zona de picking

Separar las zonas crea un trabajo nuevo: bajar mercadería de la zona de reserva a la de picking antes de que se vacíe. Bartholdi y Hackman advierten que reponer cuesta más que preparar una línea, y dan como regla práctica una persona que repone cada cinco que preparan. Es un movimiento entre ubicaciones: no cambia la cantidad del artículo, solo dónde está.

Esta reposición interna es de esta vertical. La de [Reposición](../Reposicion/reposicion.md) es otra cosa: cuándo y cuánto pedirle afuera al proveedor, con el [punto de pedido](../Reposicion/punto-de-pedido.md). Las dos usan la misma lógica de un mínimo que dispara la orden, y por eso se confunden; el criterio de la base es que la que mueve dentro del depósito es de acá y la que compra es de allá. Si la zona de picking se queda vacía con stock en la reserva, la [preparación de pedidos](preparacion-de-pedidos.md) se frena aunque el sistema muestre disponible.

> [!NOTE] Sin fuente todavía: cómo se fija el mínimo de una ubicación de picking y si la reposición se dispara por mínimo, por ola o por demanda del día.
