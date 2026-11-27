---
resumen: >-
  La recepción es el paso en que la mercadería que llega al depósito se descarga, se cuenta, se inspecciona y se ubica, y en que su cantidad entra al registro de stock. Lo que no pasa la inspección queda apartado y no se puede vender; lo que se recibe para salir enseguida puede cruzar el depósito sin guardarse (cross-docking).
estado: vigente
estabilidad: semi
fuentes:
  - "Bartholdi y Hackman, Warehouse & Distribution Science, versión 0.98.1 (16-ago-2019), §3.1-3.2 (recepción y guardado), §4.1 y §4.3 (efecto contable, funciones de un WMS) y §13.1-13.2 (cross-docking): https://www.warehouse-science.com/book/editions/wh-sci-0.98.1.pdf"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.4.3.2 «Receive, inspect, and store inbound deliveries»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "ERPNext, Quality Inspection (según su resumen): https://docs.frappe.io/erpnext/user/manual/en/quality-inspection"
  - "Inventario-y-depositos/.investigacion/operacion-del-deposito.md (2026-11-27), sección 2"
aliases: [recepción, recepción de mercadería, ingreso de mercadería, receiving, inbound, goods receipt, recibo, inspección de recepción, control de calidad en la recepción, incoming inspection, guardado, put-away, putaway, cuarentena, quarantine, cross-docking, cross-dock]
creado: 2026-11-27
revisado: 2026-11-27
---

# Recepción

La recepción es el paso en que la mercadería que llega al depósito se descarga, se cuenta, se inspecciona y se ubica, y en que su cantidad entra al registro de stock. Lo que no pasa la inspección queda apartado y no se puede vender; lo que se recibe para salir enseguida puede cruzar el depósito sin guardarse (cross-docking).

Es la puerta de entrada de [Operación del depósito](operacion-del-deposito.md). APQC 7.4 la nombra con los tres verbos juntos, 4.4.3.2 «Receive, inspect, and store inbound deliveries», y la base la toma igual: recibir incluye guardar. Lo que llega puede venir de un proveedor, de otro depósito propio, de la planta o de un cliente que devuelve.

## Qué es de Compras y qué es de acá

En la misma descarga trabajan dos dominios. Compras y abastecimiento mira si llegó lo pedido: compara lo recibido con la orden de compra, en [recepción contra lo pedido](../../Compras-y-abastecimiento/Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md), y si llegaron 90 de 100 decide qué se le reclama, en [diferencias y devoluciones](../../Compras-y-abastecimiento/Seguimiento-de-la-orden/diferencias-y-devoluciones.md). La factura del proveedor no entra en ese control: su cruce con la orden y la recepción es de Contabilidad, en [compras y cuentas a pagar](../../Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md#el-cruce-de-tres-vías-visto-desde-el-registro), y el recorrido entero está en [de la compra al pago](../../Procesos-de-negocio/de-la-compra-al-pago.md). Este tema cuenta lo que hay, lo inspecciona, aparta lo dudoso, lo ubica y suma el movimiento al stock. El conteo de acá es el dato que Compras usa para su control.

Bartholdi y Hackman marcan el efecto hacia los costados: la recepción dispara el pago al proveedor, igual que el despacho dispara la factura al cliente. Por eso una recepción mal registrada deja mal el stock y además hace pagar lo que no llegó (inferencia de la base).

## Los pasos de una recepción

1. **Aviso y turno.** El proveedor avisa qué manda y cuándo. Según Bartholdi y Hackman, no es raro que un depósito le dé al camión una ventana de 30 minutos.
2. **Descarga y registro de llegada.** Se escanea o se anota lo que bajó. Para el libro, ese registro es el que hace que la empresa asuma la propiedad, pague y sepa que tiene con qué atender pedidos.
3. **Conteo e inspección.** Se cuenta y se revisa, y se anotan las excepciones: daño, cantidades que no coinciden, descripciones equivocadas (los tres ejemplos son del libro).
4. **Decisión de estado.** Lo que está bien pasa a disponible; lo que espera inspección o la falló queda apartado.
5. **Guardado.** Se lleva a una [ubicación](ubicaciones.md) y se escanea la ubicación para registrar dónde quedó.

Si el artículo se controla por lote o por número de serie, el lote y el vencimiento se toman en el paso 3; sin ese dato no se puede elegir después qué sale primero. Está en [lote y serie](../Existencias/lote-y-serie.md).

## Lo que no pasa la inspección

La recepción es donde la mercadería entra en un estado que no se puede vender. La base llama cuarentena a ese estado y lo define en [estados del stock](../Existencias/estados-del-stock.md); acá importa el mecanismo. Bartholdi y Hackman ponen el aseguramiento de la calidad entre las funciones básicas de un sistema de gestión de depósitos. En un sistema abierto, según su resumen, la inspección se carga sobre el recibo en borrador, y para los artículos que tienen criterios de inspección no se puede confirmar el recibo hasta hacerla.

El diseño que sigue es criterio de la base. Lo recibido entra a la cantidad física de inmediato, porque está en el edificio, pero no a la disponible hasta que se libera; si se puede prometer igual es una decisión de cada empresa, que se discute en [estados del stock](../Existencias/estados-del-stock.md). Liberar, rechazar o devolver al proveedor son movimientos nuevos, no cambios del renglón de la recepción. Si lo apartado va a un lugar físico propio, conviene que sea una ubicación distinta, así el conteo no lo mezcla con lo bueno.

> [!NOTE] Sin fuente todavía: una definición canónica de cuarentena y de stock bloqueado, y cómo la modelan los sistemas grandes (como estado de la cantidad o como ubicación de rechazados). Las fuentes leídas solo muestran que la inspección puede frenar la confirmación del recibo.

Las devoluciones de clientes entran por el mismo camino: se reciben, se inspeccionan y se decide si vuelven a disponible, a reparación o a merma (criterio de la base). La logística de la devolución en una tienda online está en [devoluciones](../../Comercio-electronico/Operaciones-del-comercio/devoluciones.md).

## Dónde se guarda decide cuánto cuesta sacarlo

Bartholdi y Hackman insisten en que el lugar donde se guarda un producto determina en gran parte qué tan rápido y a qué costo se lo saca después. El guardado es el momento en que se aplica la política de [ubicaciones](ubicaciones.md): ubicación fija, la libre más cercana o por clases de rotación. Un error de guardado no se ve en la recepción: aparece semanas después, cuando alguien no encuentra el artículo en la [preparación de pedidos](preparacion-de-pedidos.md).

Según el mismo libro, que cita cifras de terceros sin segunda fuente, recibir representa cerca del 10 % del costo operativo de un centro de distribución típico y guardar cerca del 15 %.

## Cross-docking: recibir sin guardar

El cross-docking hace pasar la mercadería de la puerta de entrada a la de salida sin guardarla. Bartholdi y Hackman le atribuyen dos ventajas: menos inventario, porque todo fluye, y menos trabajo, porque no hay que guardar ni buscar después. Un centro de cross-docking separa las puertas donde se descarga de las puertas donde se carga.

En este tema basta saber que existe: la mercadería entra y sale sin pasar a una ubicación de guardado, y el registro tiene que reflejarlo igual con su entrada y su salida. Cómo se organiza una red con centros de cruce es de Cadena de suministro y logística, en [red de distribución](../../Cadena-de-suministro-y-logistica/Red-de-distribucion/red-de-distribucion.md#los-flujos-por-la-red).

## En la Argentina

La mercadería llega con remito, también cuando viene de otro depósito propio, y en algunas provincias con un código de operación de traslado. Qué se controla y qué se conforma al recibir está en [Inventario y depósitos en la Argentina](../inventario-y-depositos-en-argentina.md).
