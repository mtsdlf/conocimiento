---
resumen: >-
  La orden de producción es el documento que autoriza fabricar una cantidad de un artículo para una fecha, con la versión de la lista de materiales y de la ruta que se va a usar, y que junta lo planificado con lo que de verdad pasó. Nace de una orden planificada que se libera y termina cuando se cierra, que no es lo mismo que terminarla.
estado: borrador
estabilidad: semi
fuentes:
  - "Documentación de Work Order de un sistema abierto (reserva al emitir, almacenes, programación, Stop, estados por operación): https://docs.frappe.io/erpnext/user/manual/en/work-order"
  - "Definición del campo de estado del Work Order de ese sistema (código fuente, rama develop): https://raw.githubusercontent.com/frappe/erpnext/develop/erpnext/manufacturing/doctype/work_order/work_order.json"
  - "Documentación de Job Card del mismo sistema (la hoja de cada operación): https://docs.frappe.io/erpnext/user/manual/en/job-card"
  - "Código del modelo de orden de fabricación de otro sistema abierto (rama 18.0), campo de estado y de disponibilidad con su texto de ayuda: https://raw.githubusercontent.com/odoo/odoo/18.0/addons/mrp/models/mrp_production.py"
  - "ANSI/ISA-95.00.03-2013, vista previa (Job Order, antes Production Work Order): https://www.isa.org/getmedia/506c4c83-c2d3-4807-83e7-682fd98c17f8/ISA-95-00-03-2013-preview.pdf"
  - "ISA, ISA-88 Series of Standards (alcance de la serie): https://www.isa.org/standards-and-publications/isa-standards/isa-88-standards"
  - "APQC, Process Classification Framework 7.4 (2024), 4.3.1.4 y 4.3.1.7: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Produccion/.investigacion/ejecucion-en-planta.md (sección 1) y ejecucion-en-planta-2.md (sección 6), 2026-11-27"
aliases: [orden de producción, orden de fabricación, orden de trabajo de producción, production order, manufacturing order, MO, work order, job order, Production Work Order, orden liberada, released order, orden planificada, planned order, orden firme, firm planned order, liberar la orden, cerrar la orden, hoja de operación, tarjeta de trabajo, job card, orden discreta, orden repetitiva, orden de proceso, process order]
creado: 2026-11-27
revisado:
---

# Orden de producción

La orden de producción es el documento que autoriza fabricar una cantidad de un artículo para una fecha, con la versión de la lista de materiales y de la ruta que se va a usar, y que junta lo planificado con lo que de verdad pasó. Nace de una orden planificada que se libera y termina cuando se cierra, que no es lo mismo que terminarla.

Es el centro del registro de [Ejecución en planta](ejecucion-en-planta.md). Viene del [MRP](../Planificacion-de-la-produccion/mrp.md), que propone qué fabricar, o de un pedido cuando se fabrica contra pedido (ver [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md)). ISA-95 la llama Job Order desde 2013; antes, Production Work Order. Su equivalente en mantenimiento es la [orden de trabajo](../../Activos-y-mantenimiento/Orden-de-trabajo/orden-de-trabajo.md), y en compras, la [orden de compra](../../Compras-y-abastecimiento/Orden-de-compra/orden-de-compra.md).

## Planificada, firme y liberada: vocabulario sin fuente leída

La tradición de planificación distingue la orden planificada (una sugerencia del MRP que la próxima corrida puede cambiar), la firme (que el planificador congela para que el cálculo no la mueva) y la liberada (que ya está en la planta). La distinción entre planificada y firme es del MRP y se explica en [MRP](../Planificacion-de-la-produccion/mrp.md#órdenes-planificadas-firmes-y-mensajes-de-acción), con la definición de unas diapositivas de curso. La base la usa como criterio, pero no la leyó en una fuente primaria.

> [!NOTE] Sin fuente todavía: las entradas de orden planificada, orden firme y orden liberada del diccionario de ASCM (ex APICS).

## Los estados en dos sistemas abiertos

Los dos sistemas abiertos leídos tienen listas de estados distintas, leídas en su código.

| Momento | Primer sistema (10 estados) | Segundo sistema (6 estados), con su ayuda |
|---|---|---|
| Se arma | «Draft» | «Draft: The MO is not confirmed yet.» |
| Se confirma o se emite | «Submitted», «Not Started» | «Confirmed: The MO is confirmed, the stock rules and the reordering of the components are trigerred.» |
| Se reserva material | «Stock Reserved», «Stock Partially Reserved» | un campo aparte de disponibilidad: «Waiting», «Ready», «Waiting Another Operation» |
| Se trabaja | «In Process» | «In Progress: The production has started (on the MO or on the WO).» |
| Se termina de producir | «Completed» | «To Close: The production is done, the MO has to be closed.» |
| Se cierra | «Closed» | «Done: The MO is closed, the stock moves are posted.» |
| Se detiene o se anula | «Stopped», «Cancelled» | «Cancelled: The MO has been cancelled, can't be confirmed anymore.» |

Los dos separan terminar de cerrar. Terminar es que la producción acabó; cerrar es congelar la orden para que su stock y su costo queden firmes. En el primer sistema, una orden detenida se puede reabrir: «You can also re-open the stopped Work Order». El primero guarda la reserva como estado; el segundo, como un campo independiente del avance. No es un estándar: son dos decisiones de diseño que coinciden (lectura de la base).

Las operaciones de la orden tienen su propio estado. En el primer sistema: «Pending, Work In Progress, or Completed».

Con eso, la base usa estos estados en el tema (criterio de la base): planificada y firme, que son de la planificación; liberada, en curso, terminada y cerrada, que son de la planta; y detenida y anulada, que pueden pasar en cualquier momento antes del cierre.

## Qué se controla al liberarla

Liberar es comprometer material y capacidad. Los controles que muestran los sistemas leídos:

- **Material.** Al emitir la orden, el primer sistema hace que «Raw materials are reserved in the source warehouses». El segundo, al confirmarla, dispara las reglas de stock y la reposición de los componentes, y marca si el material está «Ready» o «Waiting». La reserva como operación es de Inventario: ver [reserva](../../Inventario-y-depositos/Operacion-del-deposito/reserva.md).
- **Capacidad.** El primer sistema programa las operaciones «serially after the planned start date based on the Workstation availability». La regla está en [programación de planta](programacion-de-planta.md).
- **Lugares.** En el primer sistema, «Warehouses are mandatory for submitting a Work Order»: el de origen del material, el de producción en proceso, el de destino del terminado y el de desecho.
- **Lote.** El PCF de APQC crea el lote al programar y al liberar: 4.3.1.4 «Schedule production orders and create lots» y 4.3.1.7 «Release production orders and create lots».
- **Versión.** La orden toma la versión vigente de la lista y la ruta y la guarda, para que la [trazabilidad de lotes](../Calidad/trazabilidad-de-lotes.md) pueda separar lo fabricado antes y después de un [cambio de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md).

Que la orden no se libere sin estos controles es criterio de la base. Lo que se libera sin material espera en la planta y sube la producción en proceso, como muestra la ley de Little en [Ejecución en planta](ejecucion-en-planta.md#la-ley-de-little-ordena-la-planta).

> [!NOTE] Sin fuente todavía: un control de herramientas, instrucciones de trabajo o habilitación del operario al liberar. Ninguna fuente leída lo describe.

## La hoja de cada operación

La orden copia la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md) y registra, operación por operación, lo que pasó. El primer sistema lo hace con una tarjeta de trabajo que «stores actual production information about a particular Operation performed on a particular Workstation», con este recorrido: «Move Materials > Start Job > Complete Job > Submit». Guarda tiempos, cantidad terminada y quién la hizo. Si una operación se hace afuera, la orden espera lo que vuelve del tercero: ver [subcontratación](subcontratacion.md).

En papel es la hoja de ruta que viaja con el trabajo: cada puesto anota la hora de inicio y fin, las piezas buenas y las malas, y firma (criterio de la base). Esa hoja alimenta el [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md) y la [eficiencia global del equipo](eficiencia-global-del-equipo.md).

## Qué se registra al cerrarla

El cierre convierte una orden viva en un hecho. En el segundo sistema, cerrar es el momento en que «the stock moves are posted». Al cerrar, según lo que piden las notas vecinas:

- La cantidad final buena y rechazada, que el primer sistema deja terminar en parte. Ver [consumo y declaración](consumo-y-declaracion.md).
- Los consumos finales por componente y la devolución al depósito de lo que sobró.
- Las horas de cada operación.
- El costo, que pasa de producción en proceso a productos terminados, y las variaciones contra el estándar. Ver [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md).

Cerrar tarde deja el costo abierto; cerrar sin declarar todo deja un consumo que ya no se puede imputar. Por eso la base separa terminar (lo decide la planta) de cerrar (lo controla quien costea) (criterio de la base).

## Orden discreta, repetitiva y por procesos

Los sistemas comerciales distinguen tres formas de orden: la discreta, la repetitiva y la de procesos. Cada uno las define a su manera, y no se encontró una definición abierta y seria que las separe.

Lo único con fuente es el lado de procesos. ISA presenta la serie ISA-88 como normas de control por lotes que «bring clarity, structure and consistency to batch processing in pharmaceuticals, food and beverage industries, chemicals and other batch processing industries». En esa forma de fabricar no hay lista y ruta separadas sino una receta; la receta de control es la copia que se usa para un lote, como cuenta [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#fórmula-o-receta-en-la-fabricación-por-procesos).

Como inferencia de la base, lo que cambia para la orden es esto:

| Forma | Qué pide la orden | Qué se declara |
|---|---|---|
| Discreta | una cantidad de un artículo, con fecha | piezas buenas y rechazadas |
| Repetitiva | un ritmo en una línea, por período, sin una orden por lote | cantidades por turno o por día |
| Por procesos | un lote con su receta de control | cantidades por salida, con merma y subproductos |

> [!NOTE] Sin fuente todavía: definiciones de orden discreta, repetitiva y de procesos en el diccionario de ASCM o en un libro de texto, y el texto de ISA-88.00.01 (de pago). La tabla es inferencia de la base.

## Qué guarda una orden de producción

Mínimo, según la documentación de los dos sistemas abiertos:

- Artículo, cantidad, unidad, fechas de inicio y entrega planificadas, y fechas reales.
- La versión de la lista y la ruta usadas.
- El estado de la orden y, aparte, la disponibilidad del material.
- Los lugares: origen del material, producción en proceso, destino y desecho.
- Por componente: cantidad requerida, entregada, consumida y devuelta.
- Por operación: centro de trabajo, estado, cantidad terminada, tiempos reales y quién la hizo.
- El origen: el pedido de venta, el proyecto o la orden planificada que la generó.
- El lote o los lotes que produce.
