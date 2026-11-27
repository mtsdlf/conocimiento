---
resumen: >-
  La subcontratación es mandarle material propio a un tercero para que haga una o más operaciones de la fabricación y lo devuelva transformado. El material sigue siendo de la empresa mientras está en manos del tercero, y lo que se le paga es el servicio, no el producto.
estado: vigente
estabilidad: semi
fuentes:
  - "Documentación de Subcontracting de un sistema abierto: https://docs.frappe.io/erpnext/user/manual/en/subcontracting"
  - "APQC, Process Classification Framework 7.4 (2024), 4.1.1.3 «Define outsourcing policies»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Produccion/.investigacion/ejecucion-en-planta.md (sección 4), 2026-11-27"
aliases: [subcontratación, subcontracting, fasón, trabajo a fasón, façon, maquila, operación externa, outside operation, outside processing, tercerización de una operación, orden de subcontratación, subcontracting order, material en poder de terceros, stock en poder de terceros]
creado: 2026-11-27
revisado: 2026-11-27
---

# Subcontratación

La subcontratación es mandarle material propio a un tercero para que haga una o más operaciones de la fabricación y lo devuelva transformado. El material sigue siendo de la empresa mientras está en manos del tercero, y lo que se le paga es el servicio, no el producto.

Es un paso de la fabricación, dentro de [Ejecución en planta](ejecucion-en-planta.md): una operación de la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) que se hace afuera. Toca tres dominios. La decisión de hacer adentro o afuera es de Compras, en [hacer o comprar](../../Compras-y-abastecimiento/Abastecimiento-estrategico/hacer-o-comprar.md), y la política, según el PCF de APQC, es estrategia de producción: 4.1.1.3 «Define outsourcing policies». La orden al proveedor es de [Compras y abastecimiento](../../Compras-y-abastecimiento/compras-y-abastecimiento.md). El material que viaja es stock, y su registro es de [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md).

Se diferencia de comprar el componente terminado en que el material es propio: el proveedor no lo compra ni lo vende. Por eso hay que seguir un saldo de material en un lugar que no es de la empresa (lectura de la base).

## El recorrido en un sistema abierto

La única fuente leída es la documentación de un sistema abierto. Su recorrido tiene cinco pasos:

1. Orden de compra de subcontratación. Se pide el producto transformado al proveedor; la tarifa del renglón es el costo acordado del servicio.
2. Orden de subcontratación. Se calculan desde la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) las materias primas que hay que mandar.
3. Envío del material. Un movimiento de tipo «Send to Subcontractor» lleva el material de un depósito propio al del proveedor.
4. Recepción de subcontratación. Al recibir, se consume el material que estaba en el depósito del proveedor (la documentación lo compara con «a backflush for subcontracting»), entra el producto al depósito de aceptados y, si hay, se registra el desecho.
5. Recepción de compra sin movimiento de stock. La recepción del paso 4 ya actualizó el stock y la contabilidad.

En ese sistema, la base del consumo puede ser la lista de materiales o lo que efectivamente se mandó. Es la misma decisión que el [consumo automático](consumo-y-declaracion.md#el-consumo-automático) dentro de la planta, con una diferencia: el sobrante queda en el depósito del tercero y no en el propio (inferencia de la base).

En papel, el recorrido es un remito de salida con el material enviado, una planilla por proveedor con el saldo que tiene en su poder y el remito de vuelta con lo recibido y el desecho (criterio de la base).

> [!NOTE] Sin fuente todavía: la subcontratación en un libro de texto de planificación y control (Vollmann y otros, el capítulo de operaciones externas) y la práctica argentina del trabajo a fasón: qué remito acompaña el material y qué trata la parte impositiva. Lo de la Argentina, cuando tenga fuente, va en [Producción en la Argentina](../produccion-en-argentina.md).

## El material en poder del tercero

El material que está en el taller del proveedor es de la empresa y no está en su depósito. En [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md), el estado «de terceros» es el caso inverso (lo ajeno en el depósito propio), y lo propio en casa de otro se trata como un lugar más. Los sistemas modelan al proveedor como una [ubicación](../../Inventario-y-depositos/Operacion-del-deposito/ubicaciones.md) virtual, y el sistema abierto leído le asigna un depósito propio. Así, mandar material es una transferencia y no una salida: el stock sigue en el patrimonio y en el valor del inventario (lectura de la base).

Ese saldo es el que más se descuida. El proveedor recibe 1.000 kg de chapa, devuelve 400 piezas que según la lista llevan 2,3 kg cada una y declara 30 kg de recorte: el sistema espera 50 kg en su poder (cuenta de la base: 1.000 − 920 − 30). Si nadie lo concilia con el proveedor, ese saldo crece sin que nadie lo vea, y aparece recién cuando se cuenta o se deja de trabajar con él (inferencia de la base). El control de ese saldo es un conteo más; cómo se hace está en [Control del stock](../../Inventario-y-depositos/Control-del-stock/control-del-stock.md).

## Dónde corta con Compras e Inventario

| Qué | Quién es dueño | Dónde está |
|---|---|---|
| Hacer adentro o afuera | Compras, con la política de producción | [hacer o comprar](../../Compras-y-abastecimiento/Abastecimiento-estrategico/hacer-o-comprar.md) |
| Qué operación se hace afuera y con qué material | Producción | la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) y la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) |
| La orden al proveedor, su precio y su seguimiento | Compras | [tipos de orden](../../Compras-y-abastecimiento/Orden-de-compra/tipos-de-orden.md) y [solicitud de compra](../../Compras-y-abastecimiento/Orden-de-compra/solicitud-de-compra.md) |
| El envío, el saldo en poder del tercero y la recepción | Inventario | [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md) y [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md) |
| Lo que vuelve y no cumple | Calidad | [no conformidad](../Calidad/no-conformidad.md) |
| Cuánto costó | Costos | el servicio más el material, en el [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md) |

Las notas de Compras discrepan en un punto: [tipos de orden](../../Compras-y-abastecimiento/Orden-de-compra/tipos-de-orden.md#los-bordes-subcontratación-y-compra-de-activos) dice que la subcontratación termina en una orden al proveedor, y [solicitud de compra](../../Compras-y-abastecimiento/Orden-de-compra/solicitud-de-compra.md) lee que, de los propósitos de la solicitud, solo el de comprar termina en una orden. La documentación de subcontratación del sistema abierto empieza por una orden de compra de subcontratación, que es lo que sostiene la primera lectura.

## Qué guarda una subcontratación

Mínimo, según la documentación del sistema abierto y lo que pide el saldo:

- Proveedor, operación contratada y tarifa del servicio.
- El vínculo con la orden de compra y con la [orden de producción](orden-de-produccion.md), si la operación es parte de una.
- El material enviado: artículo, cantidad, lote, fecha y documento.
- Lo recibido: producto aceptado y rechazado, desecho y su valor, fecha y documento.
- El material consumido, con la base que se usó (la lista o lo enviado), y lo devuelto.
- El saldo de material en poder de cada proveedor, por artículo y lote.
