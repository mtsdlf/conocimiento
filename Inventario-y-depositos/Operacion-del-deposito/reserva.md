---
resumen: >-
  La reserva es apartar una cantidad del stock disponible para un pedido, sin moverla del estante, para que no se le prometa a otro. Su resultado es stock comprometido; las decisiones que la definen son en qué momento se reserva, si se aparta una cantidad o una unidad concreta (de qué lote y de qué ubicación) y cuándo se libera.
estado: borrador
estabilidad: semi
fuentes:
  - "ASCM/APICS, CPIM 6.1 (2019) Excerpt, sección F, definición de «Available inventory» del APICS Dictionary: https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "Bartholdi y Hackman, Warehouse & Distribution Science, versión 0.98.1 (16-ago-2019), §3.3 (chequeo de disponibilidad al recibir el pedido): https://www.warehouse-science.com/book/editions/wh-sci-0.98.1.pdf"
  - "SCOR 6.0 Quick Reference, D1.3 «Reserve Inventory and Determine Delivery Date»: https://www2.isye.gatech.edu/~lfm/8851/Sources/SCOR/SCORv6quickref.pdf"
  - "Odoo 17.0, Reservation methods (según su resumen): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/reservation_methods.html"
  - "Microsoft Learn, Inventory Visibility: available to promise (fórmula de disponible con reserva blanda y física): https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-available-to-promise"
  - "Inventario-y-depositos/.investigacion/operacion-del-deposito.md (2026-11-27), sección 3"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (2026-11-27), estados del stock"
aliases: [reserva, reserva de stock, reservar, apartar stock, reservation, stock reservation, inventory reservation, asignación, allocation, compromiso de stock, reserva blanda, soft reservation, soft allocation, reserva dura, reserva física, hard reservation, hard allocation, liberación de la reserva]
creado: 2026-11-27
revisado:
---

# Reserva

La reserva es apartar una cantidad del stock disponible para un pedido, sin moverla del estante, para que no se le prometa a otro. Su resultado es stock comprometido; las decisiones que la definen son en qué momento se reserva, si se aparta una cantidad o una unidad concreta (de qué lote y de qué ubicación) y cuándo se libera.

Es el puente entre la venta y el depósito. El [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) confirmado pide la reserva; la reserva baja lo disponible, que es lo que consulta el [disponible para prometer](../Existencias/disponible-para-prometer.md); y la [preparación de pedidos](preparacion-de-pedidos.md) la consume cuando saca la mercadería. La reserva no mueve nada: cambia el estado de una cantidad, de disponible a comprometido. Los estados se definen en [estados del stock](../Existencias/estados-del-stock.md).

## Lo que la reserva le resta a lo disponible

El APICS Dictionary, citado por el CPIM, define el inventario disponible como el saldo físico menos las asignaciones, las reservas, los pedidos pendientes de entrega y, por lo general, lo retenido por problemas de calidad. La reserva es entonces una de las restas que separan lo que hay de lo que se puede vender. Con el ejemplo del tema: de 100 unidades en el estante, si 60 están reservadas para otros pedidos y 15 en cuarentena, se pueden prometer 25.

Las fuentes no lo nombran igual. SCOR 6.0 pone en un mismo paso reservar el stock y fijar la fecha de entrega, D1.3 «Reserve Inventory and Determine Delivery Date». Bartholdi y Hackman no usan la palabra: dicen que al llegar un pedido el depósito verifica que haya stock para despacharlo y que el sistema identifica los faltantes. La base separa las dos cosas: la fecha que se le dice al cliente es de Relación con clientes, en [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md); el cálculo y la reserva son de acá.

## En qué momento se reserva

Un sistema abierto ofrece, según su resumen, tres momentos:

| Momento | Qué hace | Cuándo conviene (criterio de la base) |
|---|---|---|
| Al confirmar el pedido | reserva apenas se confirma, si hay stock | venta de lo que está en el estante, entrega inmediata |
| Manual | alguien revisa la disponibilidad y reserva a mano | pocos pedidos grandes, o stock escaso que se reparte por decisión comercial |
| Antes de la fecha programada | reserva una cantidad de días antes de la entrega (por defecto, 0) | pedidos con entrega a semanas, para no inmovilizar stock que hoy podría venderse |

Reservar temprano protege al cliente que pidió primero y le quita stock a la venta de hoy. Reservar tarde deja vender más, pero un pedido confirmado puede quedarse sin mercadería. No hay una respuesta de fuente: la elección depende de cuánto pesa cada error en el negocio.

## Reservar una cantidad o reservar una unidad

La práctica distingue dos profundidades de reserva. Un sistema de un proveedor grande calcula lo disponible restando por separado la reserva blanda y la reserva física, y deja configurar cuáles se restan: son cantidades distintas. Las definiciones que siguen son criterio de la base, porque no se leyó una canónica:

- **Reserva blanda**: aparta una cantidad del artículo en un depósito, sin decir cuál unidad. Basta para que el disponible no se prometa dos veces.
- **Reserva dura (física)**: aparta unidades concretas, de un lote o número de serie y una ubicación determinados. Es la que necesita la preparación para saber qué sacar.

Lo común (criterio de la base) es reservar blando al confirmar y endurecer cerca de la preparación, cuando se elige de qué lote y de qué ubicación sale. Elegir el lote sigue la regla de salida del artículo: el que entró primero (FIFO) o el que vence primero (FEFO), que están en [lote y serie](../Existencias/lote-y-serie.md). Endurecer demasiado temprano ata el pedido a un lote que quizás vence antes de la entrega, o a una ubicación que después se reorganiza.

> [!NOTE] Sin fuente todavía: una definición canónica de reserva blanda y dura (o de asignación y reserva en el sentido del APICS Dictionary) y de cómo se asigna el lote al reservar.

## Cuándo se libera

Una reserva termina de tres maneras: la consume la salida, cuando se prepara y se despacha el pedido; se libera porque el pedido se anula, se cierra o se cambia (está en [cambios y cancelaciones](../../Relacion-con-clientes/Pedido-de-venta/cambios-y-cancelaciones.md)); o se libera porque venció. Que tenga que haber un evento explícito para cada salida es criterio de la base: una reserva que nadie libera sigue restando de lo disponible para siempre.

> [!NOTE] Sin fuente todavía: si los sistemas vencen las reservas por tiempo y con qué plazo, y cómo se repara una reserva que quedó huérfana.

## Cómo falla la reserva

Las fallas son criterio de la base:

- **No reservar.** Dos pedidos se llevan la misma unidad y el error aparece en el estante, cuando el segundo no la encuentra.
- **Reservas huérfanas.** Pedidos anulados que no liberaron su reserva: el sistema dice que no hay y el estante está lleno.
- **Reservar sobre un número falso.** Si el registro no coincide con el estante, la reserva aparta algo que no existe. El problema es de [Control del stock](../Control-del-stock/control-del-stock.md).
- **Reservar en varios canales a la vez.** Cada canal aparta contra su propia copia del número; en una tienda online es la sobreventa, que está en [catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md).

En un sistema, la reserva se guarda como un movimiento más, que no cambia la cantidad física sino la comprometida, con el patrón de [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).
