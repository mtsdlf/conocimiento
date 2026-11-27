---
resumen: >-
  Producto y proceso es la parte de la producción que define de qué está hecho cada producto y cómo se fabrica: la lista de materiales, la ruta de fabricación con sus centros de trabajo y los cambios de ingeniería que las modifican. Son los datos maestros de fabricación, y de ellos dependen el plan, la orden, el costo y la calidad.
estado: vigente
estabilidad: estable
fuentes:
  - "Documentación de un sistema comercial, «Bill of materials (BOM)» y fórmulas (página del 2025-07-10): https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom"
  - "Diapositivas «Material Requirements Planning (MRP) for Dependent Demand Systems», SMU, curso 5362 (2004): https://s2.smu.edu/~barr/5362/2004/04p20MRP.pdf"
  - "Manual de Work Order de un sistema abierto: https://docs.frappe.io/erpnext/user/manual/en/work-order"
  - "Manual de Bill of Materials de un sistema abierto: https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials"
  - "ISA-88 en Wikipedia (resumen secundario): https://en.wikipedia.org/wiki/ISA-88"
  - "Wikipedia, «Engineering change order»: https://en.wikipedia.org/wiki/Engineering_change_order"
  - "Produccion/.investigacion/producto-y-proceso.md (2026-11-27), secciones 0 a 3; planificacion.md, costos.md y ejecucion-en-planta.md (2026-11-27)"
aliases: [producto y proceso, datos maestros de fabricación, manufacturing master data, datos de ingeniería, engineering data, ficha técnica, definición del producto, product definition, fabricación discreta, discrete manufacturing, fabricación por procesos, process manufacturing]
creado: 2026-11-27
revisado: 2026-11-27
---

# Producto y proceso

Producto y proceso es la parte de la producción que define de qué está hecho cada producto y cómo se fabrica: la lista de materiales, la ruta de fabricación con sus centros de trabajo y los cambios de ingeniería que las modifican. Son los datos maestros de fabricación, y de ellos dependen el plan, la orden, el costo y la calidad.

Es la primera de las cinco partes de [Producción](../produccion.md) y la única que no registra hechos: describe cómo debería hacerse cada producto. Las otras cuatro la leen. El artículo como registro (su código, su unidad, si lleva stock) es de Inventario y está en [artículo](../../Inventario-y-depositos/Existencias/articulo.md); acá se dice qué artículos entran en otro y por dónde pasan para convertirse en él.

## Dos datos maestros y quién los mantiene

La [lista de materiales](lista-de-materiales.md) dice qué lleva un producto y en qué cantidad. La [ruta de fabricación](ruta-de-fabricacion.md) dice por qué operaciones pasa, en qué [centro de trabajo](ruta-de-fabricacion.md#el-centro-de-trabajo-dónde-se-hace-y-cuánto-puede) y cuánto tarda cada una. Un sistema comercial resume la primera así: «A bill of materials (BOM) defines the components that are required in order to produce a product».

En muchos sistemas las dos cuelgan de la misma cabecera, y en otros la ruta es un maestro aparte que se aplica a varias listas. Esa es una decisión de diseño del sistema, no del dominio: lo que el dominio exige es una lista de componentes y una secuencia de operaciones con recurso y tiempo.

Quién los mantiene cambia de una empresa a otra. Como criterio de la base, lo habitual es que ingeniería de producto lleve la lista, que ingeniería de procesos o industrial lleve la ruta, y que nadie más las toque sin un [cambio de ingeniería](cambios-de-ingenieria.md). Wikipedia describe la orden de cambio como un documento «approved by the design activity», es decir, por quien diseña el producto.

> [!NOTE] Sin fuente todavía: quién mantiene la lista y la ruta en la práctica (ingeniería de producto, de procesos, planificación) y cómo se reparte esa responsabilidad en una pyme sin área de ingeniería.

## Qué hace cada parte de la producción con la lista y la ruta

Las otras cuatro verticales usan los mismos dos datos para cosas distintas. Por eso un error en la lista se multiplica en las compras, el programa y el costo.

| Parte | Qué toma | Para qué |
|---|---|---|
| [Planificación de la producción](../Planificacion-de-la-produccion/planificacion-de-la-produccion.md) | la lista para explotar componentes; las horas de la ruta por centro | el [MRP](../Planificacion-de-la-produccion/mrp.md) calcula qué comprar y fabricar; la [planificación de capacidad](../Planificacion-de-la-produccion/planificacion-de-capacidad.md), si el plan entra en la planta |
| [Ejecución en planta](../Ejecucion-en-planta/ejecucion-en-planta.md) | una copia de la lista y la ruta, en la versión vigente | la [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) sabe qué material entregar y qué operaciones seguir; el consumo automático descuenta según la lista |
| [Costos de producción](../Costos-de-produccion/costos-de-produccion.md) | cantidades, mermas, tiempos y costo por hora del centro | el [costo estándar del producto](../Costos-de-produccion/costo-estandar-del-producto.md) se acumula nivel por nivel |
| [Calidad](../Calidad/calidad.md) | la versión con que se fabricó cada lote | la [acción correctiva](../Calidad/accion-correctiva.md) que corrige una causa en el diseño termina en un cambio de ingeniería |

Las diapositivas de un curso de MRP listan sus entradas como «Master schedule, Bill of materials, Inventory records». Las mismas diapositivas ponen entre los requisitos del MRP «An accurate BOM». En un sistema abierto, el costo de la lista sale «from the Valuation Rate of the raw materials/sub-assemblies involved and the Operation costs». Que la orden de producción guarde la lista y la ruta que usó es inferencia de la base: las fuentes leídas no lo dicen.

## Discreta o por procesos: lista y ruta, o fórmula

La división en lista y ruta viene de la fabricación discreta: piezas que se cuentan por unidad y se ensamblan, como un mueble o una lámpara. En la fabricación por procesos (química, alimentos, bebidas) el campo usa otra forma, la fórmula o receta, que junta en un solo documento lo que en la discreta son dos.

Según el resumen secundario de la norma ISA-88, una receta contiene «a header, a formula, equipment requirements, a procedure, and other batch processing support information». La fórmula incluye insumos, parámetros y salidas, no solo proporciones. Un sistema comercial trata la fórmula como «a subtype of BOM that is typically used for process manufacturing», con rendimiento, coproductos y subproductos por versión.

| | Fabricación discreta | Fabricación por procesos |
|---|---|---|
| Qué lleva | lista de materiales | fórmula: insumos, parámetros y salidas |
| Cómo se hace | ruta de fabricación | procedimiento de la receta, ligado al equipo |
| Qué sale | por lo general, un producto | un producto con coproductos y subproductos, y un rendimiento que varía |
| Cómo se cuenta | unidades | kilos, litros, lotes |

La correspondencia de la tabla es inferencia de la base: ninguna fuente leída la hace. La fórmula se acerca a la lista más los parámetros, y el procedimiento a la ruta, pero jerárquico y atado al equipo. El detalle está en [la fórmula o receta](ruta-de-fabricacion.md#fórmula-o-receta-en-la-fabricación-por-procesos), dentro de la ruta.

> [!NOTE] Sin fuente todavía: la distinción entre fabricación discreta, repetitiva y por procesos en un texto del campo, y qué cambia en la orden de producción en cada una.

## Cómo se lleva sin software

Antes de cualquier sistema, la lista y la ruta son una ficha técnica por producto: una tabla de componentes con cantidades y otra de pasos con el puesto y los minutos. La versión va en el encabezado, con la fecha desde la que vale y la firma de quien la aprobó. En una planilla alcanza una hoja por producto con esas dos tablas, y un registro aparte de cambios con fecha y motivo (criterio de la base).

Lo que la planilla no hace sola es explotar varios niveles ni encontrar todos los productos que usan un componente. Con dos o tres niveles y pocos productos se hace a mano; con más, es el primer motivo para pasar a un sistema (inferencia de la base).

## Cómo fallan los datos maestros

- La lista no refleja lo que se hace en la planta: el consumo automático descuenta lo que dice la lista, así que una lista equivocada deja el stock equivocado sin que nadie cargue un error (inferencia de la base). Ver [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md).
- Los tiempos de la ruta son viejos o de catálogo: la capacidad y el costo estándar se calculan con ellos, así que un tiempo inflado esconde ineficiencia y uno corto genera variaciones en cada orden (inferencia de la base).
- Cambios sin control: alguien corrige la lista directamente, sin versión ni vigencia, y las órdenes abiertas quedan con una mezcla. Cómo se evita está en [cambios de ingeniería](cambios-de-ingenieria.md).
- Dos listas que se separan: ingeniería mantiene una y la planta otra, y ninguna es la verdadera; está en [lista de ingeniería y lista de fabricación](lista-de-materiales.md#lista-de-ingeniería-y-lista-de-fabricación).

## Lo que hay adentro de producto y proceso

- [Lista de materiales](lista-de-materiales.md): qué lleva un producto, con niveles, cantidad por unidad, merma, lista fantasma, de planificación, variantes, lista de ingeniería frente a la de fabricación, código de nivel más bajo y las salidas extra. Leerla primero.
- [Ruta de fabricación](ruta-de-fabricacion.md): cómo se hace, con operaciones en secuencia, centro de trabajo con su capacidad y eficiencia, los cuatro tiempos de una operación y la fórmula o receta en procesos.
- [Cambios de ingeniería](cambios-de-ingenieria.md): cómo cambian la lista y la ruta sin romper lo que está en curso, con solicitud y orden de cambio, versión, vigencia, qué pasa con el stock y quién aprueba.

La lista de repuestos de una máquina es otra cosa: dice qué piezas lleva el equipo para mantenerlo, no qué lleva un producto. Está en [jerarquía de activos](../../Activos-y-mantenimiento/Registro-de-activos/jerarquia-de-activos.md#componentes-y-lista-de-repuestos-del-equipo), de Activos y mantenimiento.
