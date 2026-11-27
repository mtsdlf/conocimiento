---
resumen: >-
  El lote agrupa unidades de un artículo que se recibieron, fabricaron o vencen juntas, y el número de serie identifica una sola unidad; los dos permiten rastrear de dónde vino y a dónde fue cada cosa, y decidir qué sale primero (FIFO, FEFO).
estado: borrador
estabilidad: estable
fuentes:
  - "Odoo 17, Lots (lote, retiros de mercado, vencimiento y estrategia de salida; según el resumen leído): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots.html"
  - "Frappe/ERPNext, Serial No (registro por unidad; según el resumen leído): https://docs.frappe.io/erpnext/user/manual/en/serial-no"
  - "NIC 2 vía la nota de costo de lo vendido (FIFO como fórmula de costo): Contabilidad/Operaciones/costo-de-lo-vendido.md"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (2026-11-27), sección Lote y número de serie"
  - "ANMAT, Trazabilidad de medicamentos (solo la página, sin las normas): https://www.anmat.gob.ar/webanmat/Trazabilidad/trazabilidad_home.asp"
  - "SENASA, Sistema de identificación electrónica de animales (según su resumen): https://www.argentina.gob.ar/senasa/sistema-de-identificacion-electronica-de-animales"
  - "Inventario-y-depositos/.investigacion/argentina.md (2026-11-27), sección 4, Trazabilidad obligatoria"
aliases: [lote, partida, lot, batch, número de serie, serie, serial number, trazabilidad, traceability, vencimiento, fecha de vencimiento, expiration date, FIFO, FEFO, LIFO, PEPS físico, first expired first out, retiro de mercado, recall]
creado: 2026-11-27
revisado:
---

# Lote y serie

El lote agrupa unidades de un artículo que se recibieron, fabricaron o vencen juntas, y el número de serie identifica una sola unidad; los dos permiten rastrear de dónde vino y a dónde fue cada cosa, y decidir qué sale primero (FIFO, FEFO).

Son la tercera coordenada de la fórmula de [existencias](existencias.md): con lote o serie, una cantidad ya no es «40 frascos» sino «25 del lote A, que vence en marzo, y 15 del lote B». Si un [artículo](articulo.md) se sigue por lote, por serie o sin seguimiento se decide en su ficha y afecta a todo el recorrido por el depósito.

## Lote y serie, lado a lado

Un sistema abierto define el lote como una de las dos maneras de identificar y seguir productos, útil «particularly for product recalls or expiration dates» (según el resumen leído). Otro sistema abierto guarda un registro por cada número de serie con la garantía y el vencimiento, su estado actual y el vínculo con el proveedor, el cliente y el documento que lo movió; solo una unidad en estado disponible se puede entregar (según el resumen leído).

| | Lote | Número de serie |
|---|---|---|
| Identifica | Un grupo de unidades | Una unidad |
| Cantidad por identificador | Cualquiera | Siempre una |
| Para qué se usa | Retiros de mercado, vencimiento, control de calidad por partida | Garantía, servicio técnico, robo, equipos de valor |
| Ejemplos típicos | alimentos, medicamentos, pinturas, insumos químicos | electrodomésticos, celulares, herramientas eléctricas |
| Qué se registra en cada movimiento | El lote y la cantidad | Cada número, uno por uno |

Los ejemplos de la tabla son criterio de la base. Un artículo puede llevar los dos: un equipo médico con número de serie que además pertenece a un lote de fabricación.

> [!NOTE] Sin fuente todavía: las definiciones canónicas de lote y de número de serie (APICS Dictionary) no se pudieron abrir; las de arriba salen de la documentación de dos sistemas.

## El orden de salida: FIFO, FEFO y LIFO

Cuando un artículo tiene varios lotes, alguien decide de cuál sale cada pedido. Un sistema abierto llama a esa regla estrategia de salida y ofrece «(FIFO, LIFO, or FEFO)», sin explicar cada una en la página leída. Las siglas significan:

| Regla | Sale primero | Cuándo conviene (criterio de la base) |
|---|---|---|
| FIFO (first in, first out) | Lo que entró antes | Mercadería que envejece, se deteriora o pasa de moda |
| FEFO (first expired, first out) | Lo que vence antes | Todo lo que tiene fecha de vencimiento: puede haber entrado después y vencer antes |
| LIFO (last in, first out) | Lo que entró último | Mercadería a granel que no se deteriora, apilada de modo que lo último queda adelante |

Esta regla es física: dice qué unidades se levantan del estante. No es la fórmula de costo PEPS (FIFO en inglés) de la contabilidad, que supone qué costo sale aunque en el estante haya salido otra cosa; esa está en [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md). Una empresa puede despachar por FEFO y valuar por promedio ponderado (inferencia de la base).

## Qué cambia en el depósito cuando un artículo lleva lote o serie

El seguimiento se paga en cada paso donde se mueve mercadería, porque cada paso tiene que registrar qué lote o qué número tocó (criterio de la base):

1. **Recepción.** Se anota el lote del proveedor o se asigna uno propio, con su fecha de vencimiento, o se lee cada número de serie. Un lote dudoso queda en cuarentena hasta que lo inspeccionan. Está en [recepción](../Operacion-del-deposito/recepcion.md), y el estado, en [estados del stock](estados-del-stock.md).
2. **Ubicación.** Dos lotes del mismo artículo pueden ir a la misma [ubicación](../Operacion-del-deposito/ubicaciones.md) o a ubicaciones distintas; si se mezclan, el preparador tiene que poder distinguirlos.
3. **Reserva.** Al apartar stock para un pedido se decide si se aparta un lote concreto o solo una cantidad, y la regla de salida elige cuál. Está en [reserva](../Operacion-del-deposito/reserva.md).
4. **Preparación.** El preparador confirma el lote o el número que levantó; si toma otro, el registro tiene que seguir a lo físico. Está en [preparación de pedidos](../Operacion-del-deposito/preparacion-de-pedidos.md).
5. **Salida.** El documento que acompaña la mercadería lleva el lote o la serie, y así queda el vínculo con el cliente que permite un retiro de mercado.
6. **Vencimiento.** Lo que vence sin salir pasa a bloqueado y después a merma, con un ajuste ([ajustes y mermas](../Control-del-stock/ajustes-y-mermas.md)).

El costo es trabajo y error: cada lectura de más es tiempo, y cada lote mal cargado deja el rastro roto justo cuando hace falta. Por eso conviene seguir por lote solo lo que lo necesita: lo que vence, lo que una norma obliga a rastrear o lo que se retira por partida (criterio de la base).

## El rastreo hacia atrás y hacia adelante

La razón de llevar lote o serie es poder contestar dos preguntas el día de un problema. Hacia atrás: este lote o esta unidad, ¿de qué proveedor y de qué recepción vino? Hacia adelante: ¿a qué clientes fue cada unidad de este lote? Con las dos, un retiro de mercado se limita a los clientes que recibieron ese lote, y no a todos los que compraron el artículo (criterio de la base).

Hay rubros donde el rastreo es obligatorio. En la Argentina existe un régimen de trazabilidad de medicamentos a cargo de la ANMAT, según su página, y la identificación electrónica individual de bovinos, bubalinos y cérvidos con fines comerciales es obligatoria desde el 1/1/2026, según el SENASA. Lo que eso pide a un depósito está en [Inventario y depósitos en la Argentina](../inventario-y-depositos-en-argentina.md).

> [!NOTE] Sin fuente todavía: el detalle de la norma de trazabilidad de medicamentos (quién informa qué movimiento) y una fuente canónica sobre FEFO.
