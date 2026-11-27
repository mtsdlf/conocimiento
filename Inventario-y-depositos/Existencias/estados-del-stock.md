---
resumen: >-
  Los estados del stock reparten la cantidad de un artículo según lo que se puede hacer con ella: físico, disponible, comprometido, en tránsito, en cuarentena, bloqueado y de terceros. La misma pila de cajas puede tener unidades en varios estados, y solo las disponibles se pueden prometer.
estado: vigente
estabilidad: estable
fuentes:
  - "Microsoft Learn, Inventory Visibility: available-to-promise (fórmula de disponible con PhysicalInvent, OnHand, Unrestricted, QualityInspection, Inbound, ReservPhysical, SoftReservePhysical, Outbound): https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-available-to-promise"
  - "Odoo 17, Use locations (tipos de ubicación: proveedor, vista, interna, cliente, pérdida de inventario, producción, tránsito; según el resumen leído): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations.html"
  - "ERPNext, Quality Inspection (la recepción no se confirma sin inspección; según el resumen leído): https://docs.frappe.io/erpnext/user/manual/en/quality-inspection"
  - "Trusted Institute, Inventory Planning Fundamentals and Functions (preparación CPIM; inventario de transporte, fuente secundaria): https://trustedinstitute.com/concept/cpim/inventory-management/inventory-planning-fundamentals/"
  - "ASCM/APICS, CPIM 6.1 (2019) Excerpt, sección F (ATP como «uncommitted portion»): https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (2026-11-27), sección Estados del stock"
  - "Inventario-y-depositos/.investigacion/operacion-del-deposito.md y reposicion.md (2026-11-27)"
aliases: [estados del stock, estados de inventario, inventory status, stock status, stock físico, on hand, disponible, available, comprometido, committed, reservado, reserved, en tránsito, in transit, en cuarentena, quarantine, en inspección, quality inspection, bloqueado, blocked stock, stock de terceros, consignación, consignment]
creado: 2026-11-27
revisado: 2026-11-27
---

# Estados del stock

Los estados del stock reparten la cantidad de un artículo según lo que se puede hacer con ella: físico, disponible, comprometido, en tránsito, en cuarentena, bloqueado y de terceros. La misma pila de cajas puede tener unidades en varios estados, y solo las disponibles se pueden prometer.

Son la cuarta coordenada de la fórmula de [existencias](existencias.md). Esta es la lista que usa todo el tema: [disponible para prometer](disponible-para-prometer.md) decide cuáles suma y cuáles resta, [reserva](../Operacion-del-deposito/reserva.md) pasa unidades de disponible a comprometido, [recepción](../Operacion-del-deposito/recepcion.md) las deja en cuarentena y [ajustes y mermas](../Control-del-stock/ajustes-y-mermas.md) da de baja las bloqueadas.

## Un ejemplo: 100 en el sistema, 25 para vender

Un artículo tiene 100 unidades en el depósito. De ellas, 60 están apartadas para pedidos que todavía no salieron y 15 llegaron ayer y esperan inspección. Para un pedido nuevo quedan 25. Las tres cifras son ciertas a la vez: hay 100, hay 60 comprometidas y hay 25 disponibles. Un sistema que guarda una sola cantidad no puede decir eso, y el vendedor promete 100 (ejemplo de la base).

## La lista de estados

La base usa estos estados en todo el tema. Las definiciones son criterio de la base, armado sobre la práctica de los sistemas citados en la sección siguiente:

| Estado | Qué cuenta | Está en el depósito | Se puede prometer | Qué lo pone y qué lo saca |
|---|---|---|---|---|
| Físico | Todo lo que está en el lugar, en cualquiera de los estados de abajo salvo en tránsito | Sí | No como tal: es la suma | Lo suman la recepción y las transferencias que llegan; lo restan las salidas y los ajustes |
| Disponible | Lo que está y se puede usar sin quitárselo a nadie | Sí | Sí | Lo libera la inspección o la reserva que se cancela; lo consume la reserva |
| Comprometido | Lo apartado para un pedido que todavía no salió | Sí | No | Lo pone la [reserva](../Operacion-del-deposito/reserva.md); lo saca la salida o la cancelación |
| En cuarentena | Lo que espera inspección o una decisión de calidad | Sí | Según la regla de cada empresa | Lo pone la [recepción](../Operacion-del-deposito/recepcion.md) o un reclamo; lo saca la inspección, a disponible o a bloqueado |
| Bloqueado | Lo que no se puede usar: roto, vencido, retenido por un retiro de mercado | Sí | No | Lo pone una inspección, un conteo o el vencimiento; lo saca la reparación o un [ajuste](../Control-del-stock/ajustes-y-mermas.md) |
| En tránsito | Lo que salió de un lugar propio y no llegó a otro | No | Según la regla de cada empresa | Lo pone la salida de una transferencia; lo saca la recepción en el destino |
| De terceros | Lo que está en el depósito pero no es de la empresa | Sí | No, salvo acuerdo | Lo ponen la recepción en consignación o en guarda; lo saca la devolución o la compra |

La relación entre ellos, para un artículo en un lugar, es (criterio de la base):

> físico = disponible + comprometido + en cuarentena + bloqueado

Lo de terceros se cuenta aparte, porque está en el estante pero no en el patrimonio: entra en el conteo físico y no en el valor de [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md). Lo propio que está en casa de un cliente en consignación es el caso inverso: es de la empresa y no está en su depósito. La base lo trata como un lugar más, sin nota propia. El inventario en proceso de una planta también es un estado, y es de Producción, en [Ejecución en planta](../../Produccion/Ejecucion-en-planta/ejecucion-en-planta.md).

Las cantidades por recibir (lo pedido al proveedor que todavía no salió de su depósito) no son un estado del stock, porque todavía no son stock. Sí entran en el cálculo de lo que se puede prometer a futuro y en la posición de stock de [punto de pedido](../Reposicion/punto-de-pedido.md).

## Cómo lo resuelve la práctica

Ninguna fuente leída define la lista entera; cada sistema guarda un juego distinto, y eso confirma que los estados son una decisión de diseño.

- **El ERP de un proveedor grande** calcula lo disponible sumando como oferta «PhysicalInvent + OnHand + Unrestricted + QualityInspection + Inbound» y restando como demanda «ReservPhysical + SoftReservePhysical + Outbound». Separa lo que está en inspección de calidad, la reserva blanda y la reserva física, y advierte que «The default ATP calculated formula is for reference»: qué se suma es configurable. En la fórmula por defecto, lo que está en inspección suma como oferta.
- **Un sistema abierto** modela algunos estados como ubicaciones: tiene ubicaciones de tránsito y de pérdida de inventario, además de las internas (según el resumen leído). Mover a cuarentena sería, ahí, mover a otra ubicación (inferencia de la base: la fuente no menciona la cuarentena).
- **Otro sistema abierto** no deja confirmar la recepción de un artículo con criterios de calidad hasta que se hace la inspección (según el resumen leído); la cuarentena queda antes de que el stock exista (inferencia de la base).
- **Una plataforma de tiendas** parte el stock en `incoming`, `on_hand`, `available`, `committed`, `reserved`, `damaged`, `safety_stock` y `quality_control`; está en [catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md).

El material de preparación del CPIM llama inventario de transporte a «Inventory that is currently in transit between locations in the supply chain» (fuente secundaria). ASCM define lo disponible para prometer como «the uncommitted portion», es decir, todo lo que no es comprometido; la nota [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md) trae la definición completa.

## Estado o ubicación: dos maneras de modelarlo

Hay dos diseños, y los dos funcionan (inferencia de la base sobre la práctica de arriba):

| | Estado como atributo | Estado como ubicación |
|---|---|---|
| Cómo se ve | Cada saldo lleva un campo de estado | La cuarentena, el tránsito o la merma son ubicaciones, reales o virtuales |
| Cambiar de estado | Un movimiento que cambia el atributo sin mover la caja | Una transferencia entre ubicaciones |
| Conviene cuando | El estado cambia sin que la mercadería se mueva (una reserva, un bloqueo por retiro de mercado) | El estado coincide con un lugar físico (la jaula de cuarentena, el camión) |

Lo comprometido casi nunca es una ubicación, porque la reserva no mueve la mercadería; en la mayoría de los casos se resuelve como atributo o como un saldo calculado a partir de los pedidos. La cuarentena y el tránsito, en cambio, suelen ser lugares.

## Qué decide quien diseña

- **Qué estados existen.** Un comercio con un local necesita físico, disponible y comprometido. La cuarentena aparece con la inspección de lo que llega; el tránsito, con el segundo depósito; lo de terceros, con la consignación.
- **Si la cuarentena y el tránsito se pueden prometer.** La fórmula por defecto citada arriba suma lo que está en inspección. Prometer lo que puede ser rechazado es un riesgo que alguien decide (criterio de la base); el cálculo está en [disponible para prometer](disponible-para-prometer.md).
- **Si existe la reserva blanda.** Un pedido que todavía no aparta unidades concretas compromete igual una cantidad. Cómo se aparta y se libera está en [reserva](../Operacion-del-deposito/reserva.md).
- **Quién puede cambiar un estado.** Pasar de bloqueado a disponible es, en la práctica, dar de alta mercadería; la regla de quién lo aprueba está en [ajustes y mermas](../Control-del-stock/ajustes-y-mermas.md) y en [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md).

> [!NOTE] Sin fuente todavía: una definición canónica de stock en tránsito, en cuarentena, bloqueado y en consignación (APICS Dictionary u otro); las definiciones de la tabla son de la base.
