---
resumen: >-
  Los términos del tema Inventario y depósitos, cada uno con su nombre en inglés, una definición corta y la nota donde vive.
estado: borrador
estabilidad: estable
fuentes:
  - "ASCM, CPIM 2019 Excerpt, con definiciones del APICS Dictionary, 15.ª ed.: https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "Bartholdi y Hackman, Warehouse & Distribution Science, versión 0.98.1: https://www.warehouse-science.com/"
  - "Caplice, MIT ESD.260, lecciones 11 y 12 (políticas de inventario y stock de seguridad), según Inventario-y-depositos/.investigacion/reposicion.md"
  - "Inventario-y-depositos/.investigacion/ (cinco informes, 2026-11-27)"
aliases: [glosario de inventario, inventory glossary, glosario de depósito, términos de stock]
creado: 2026-11-27
revisado:
---

# Glosario de inventario y depósitos

Los términos del tema Inventario y depósitos, cada uno con su nombre en inglés, una definición corta y la nota donde vive.

Los sistemas usan nombres distintos para lo mismo, sobre todo en los estados del stock y en la reserva. Estas son las palabras que usa esta base, en un sentido cada una; donde la definición es criterio de la base y no de una fuente, lo dice la nota que la explica.

## Lo que se tiene

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Artículo | Item, SKU | Lo que se cuenta por separado: un código con su unidad de medida y sus reglas de stock | [artículo](../Existencias/articulo.md) |
| Unidad de medida | Unit of measure, UOM | En qué se cuenta un artículo (unidad, caja, kilo) y cómo se convierte entre unidades | [artículo](../Existencias/articulo.md) |
| Existencias | Stock on hand, inventory balance | La cantidad de un artículo en un lugar, de un lote o serie si lo lleva, y en un estado | [existencias](../Existencias/existencias.md) |
| Lote | Lot, batch | Un conjunto de unidades producidas o recibidas juntas, que comparten origen y vencimiento | [lote y serie](../Existencias/lote-y-serie.md) |
| Número de serie | Serial number | El identificador de una unidad individual | [lote y serie](../Existencias/lote-y-serie.md) |
| FIFO, FEFO | First in first out, first expired first out | El orden en que sale la mercadería: lo que entró primero, o lo que vence primero. Es físico; la PEPS de la valuación es de Contabilidad | [lote y serie](../Existencias/lote-y-serie.md) |
| Trazabilidad | Traceability | Poder seguir un lote o una unidad hacia atrás (de dónde vino) y hacia adelante (a quién se entregó) | [lote y serie](../Existencias/lote-y-serie.md) |

## Los estados y lo disponible

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Stock físico | On hand | Lo que está en el depósito, en cualquier estado menos en tránsito | [estados del stock](../Existencias/estados-del-stock.md) |
| Disponible | Available | Lo físico que se puede vender o usar: no está comprometido, en cuarentena ni bloqueado | [estados del stock](../Existencias/estados-del-stock.md) |
| Comprometido | Committed, allocated | Lo apartado para un pedido que todavía no salió | [estados del stock](../Existencias/estados-del-stock.md) |
| En cuarentena | Quarantine, quality inspection | Lo que espera inspección o una decisión de calidad | [estados del stock](../Existencias/estados-del-stock.md) |
| Bloqueado | Blocked | Lo que no se puede usar hasta que alguien decida (roto, vencido, retenido por un retiro de mercado) | [estados del stock](../Existencias/estados-del-stock.md) |
| En tránsito | In transit | Lo que salió de un depósito propio y no llegó al otro | [estados del stock](../Existencias/estados-del-stock.md) |
| Stock de terceros, consignación | Consignment | Lo que está en el depósito y es de otro (consignación o guarda); lo propio que está en casa de otro es un lugar más, sin estado propio | [estados del stock](../Existencias/estados-del-stock.md) |
| Disponible para prometer | Available-to-promise, ATP | La parte del stock y de lo que va a entrar que todavía no está comprometida, período por período | [disponible para prometer](../Existencias/disponible-para-prometer.md) |
| Posición de stock | Inventory position | Lo que hay, más lo pedido al proveedor que no llegó, menos lo que se debe y lo comprometido; es lo que se compara con el punto de pedido | [punto de pedido](../Reposicion/punto-de-pedido.md) |

## La operación del depósito

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Ubicación | Location, bin | Un lugar con dirección dentro del depósito (zona, pasillo, estante, nivel) | [ubicaciones](../Operacion-del-deposito/ubicaciones.md) |
| Ubicación fija o libre | Dedicated or shared storage | Cada artículo tiene su lugar, o va donde haya espacio | [ubicaciones](../Operacion-del-deposito/ubicaciones.md) |
| Zona de picking y zona de reserva | Forward area, reserve area | Donde se prepara de a poco y donde se guarda el grueso; «zona de reserva» es un lugar, no una reserva para un pedido | [ubicaciones](../Operacion-del-deposito/ubicaciones.md) |
| Recepción | Receiving, goods receipt | Descargar, contar, inspeccionar y registrar lo que llega | [recepción](../Operacion-del-deposito/recepcion.md) |
| Guardado | Put-away | Llevar lo recibido a su ubicación | [recepción](../Operacion-del-deposito/recepcion.md) |
| Cross-docking | Cross-docking | Pasar lo recibido directo a la salida, sin guardarlo | [recepción](../Operacion-del-deposito/recepcion.md) |
| Reserva | Reservation, allocation | Apartar stock disponible para un pedido; blanda si aparta una cantidad, dura si aparta unidades concretas de un lote y una ubicación | [reserva](../Operacion-del-deposito/reserva.md) |
| Preparación de pedidos | Order picking | Sacar de sus ubicaciones lo que pide cada pedido, por pedido, por lote, por zona o por ola | [preparación de pedidos](../Operacion-del-deposito/preparacion-de-pedidos.md) |
| Embalaje | Packing | Controlar y empacar lo preparado antes de la puerta de salida | [preparación de pedidos](../Operacion-del-deposito/preparacion-de-pedidos.md) |

## El control del stock

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Inventario permanente | Perpetual inventory | La cantidad se actualiza con cada movimiento | [control del stock](../Control-del-stock/control-del-stock.md) |
| Inventario periódico | Periodic inventory | La cantidad se conoce contando cada tanto | [control del stock](../Control-del-stock/control-del-stock.md) |
| Exactitud del registro | Inventory record accuracy, IRA | Cuánto coincide lo que dice el registro con lo que hay | [control del stock](../Control-del-stock/control-del-stock.md) |
| Conteo físico | Physical inventory | Contar todo el depósito de una vez | [conteo cíclico](../Control-del-stock/conteo-ciclico.md) |
| Conteo cíclico | Cycle counting | Contar una parte chica del stock por vez, según un calendario, sin frenar la operación | [conteo cíclico](../Control-del-stock/conteo-ciclico.md) |
| Ajuste | Inventory adjustment | El movimiento que corrige el registro para que coincida con lo contado | [ajustes y mermas](../Control-del-stock/ajustes-y-mermas.md) |
| Merma | Shrinkage | La mercadería que se pierde por rotura, vencimiento, robo o error, y que los ajustes dejan a la vista | [ajustes y mermas](../Control-del-stock/ajustes-y-mermas.md) |

## La reposición

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Punto de pedido | Reorder point, ROP | El nivel de la posición de stock en que se pide más | [punto de pedido](../Reposicion/punto-de-pedido.md) |
| Revisión continua o periódica | Continuous or periodic review | Mirar la posición de stock con cada movimiento, o cada cierto tiempo; de ahí salen las políticas (s, Q), (s, S), (R, S) y (R, s, S) | [punto de pedido](../Reposicion/punto-de-pedido.md) |
| Mínimo y máximo | Min-max | Pedir cuando se baja del mínimo, hasta llegar al máximo | [punto de pedido](../Reposicion/punto-de-pedido.md) |
| Lote económico | Economic order quantity, EOQ | La cantidad por pedido que hace mínimo el costo de pedir más el de mantener, con demanda constante | [lote económico](../Reposicion/lote-economico.md) |
| Stock de seguridad | Safety stock | Lo que se tiene de más para cubrir la variabilidad de la demanda y del plazo | [stock de seguridad](../Reposicion/stock-de-seguridad.md) |
| Nivel de servicio por ciclo | Cycle service level | La probabilidad de no quedarse sin stock en un ciclo de reposición | [stock de seguridad](../Reposicion/stock-de-seguridad.md) |
| Tasa de cumplimiento | Fill rate | La parte de la demanda que se atiende con el stock que hay | [stock de seguridad](../Reposicion/stock-de-seguridad.md) |
| Clasificación ABC | ABC analysis | Ordenar los artículos por su peso (en general, valor consumido) para mirar más a los pocos que pesan mucho | [clasificación ABC](../Reposicion/clasificacion-abc.md) |
| Rotación | Inventory turnover | Cuántas veces se renueva el inventario en un período | [indicadores de inventario](../Reposicion/indicadores-de-inventario.md) |
| Días de inventario, cobertura | Days of inventory, days of supply | Para cuántos días alcanza el stock: mirando hacia atrás, sobre el costo de lo vendido, o hacia adelante, sobre la demanda esperada | [indicadores de inventario](../Reposicion/indicadores-de-inventario.md) |

## En la Argentina

| Término | Qué es | Dónde |
|---|---|---|
| Remito | El documento que acompaña el traslado y la entrega de bienes | [Inventario y depósitos en la Argentina](../inventario-y-depositos-en-argentina.md) |
| COT | El código de operación de traslado que piden algunas provincias para mover mercadería | [Inventario y depósitos en la Argentina](../inventario-y-depositos-en-argentina.md) |
| CAI | El código de autorización de impresión que tiene que figurar en el remito | [Inventario y depósitos en la Argentina](../inventario-y-depositos-en-argentina.md) |
| DT-e | El documento de tránsito electrónico con que se mueven animales bajo control del SENASA | [Inventario y depósitos en la Argentina](../inventario-y-depositos-en-argentina.md) |

## Siglas

| Sigla | Qué es | Dónde |
|---|---|---|
| ATP | Available-to-promise, disponible para prometer | [disponible para prometer](../Existencias/disponible-para-prometer.md) |
| CSL | Cycle service level, nivel de servicio por ciclo | [stock de seguridad](../Reposicion/stock-de-seguridad.md) |
| IFR | Item fill rate, tasa de cumplimiento | [stock de seguridad](../Reposicion/stock-de-seguridad.md) |
| IOH | Inventory on hand, el stock en mano | [punto de pedido](../Reposicion/punto-de-pedido.md) |
| RMSE | Root mean square error, la raíz del error cuadrático medio del pronóstico | [punto de pedido](../Reposicion/punto-de-pedido.md) |
| EOQ | Economic order quantity, lote económico | [lote económico](../Reposicion/lote-economico.md) |
| WMS | Warehouse management system, sistema de gestión de depósitos | [operación del depósito](../Operacion-del-deposito/operacion-del-deposito.md) |
| APQC | La organización que publica el Process Classification Framework, la taxonomía de procesos que cita la base | [fundamentos](fundamentos-de-inventario-y-depositos.md) |
| ASCM | Association for Supply Chain Management, ex APICS: publica el diccionario del campo y la certificación CPIM | [fundamentos](fundamentos-de-inventario-y-depositos.md) |
| CPIM | La certificación de ASCM en planificación e inventario | [fundamentos](fundamentos-de-inventario-y-depositos.md) |
| SCOR | El modelo de referencia de procesos de la cadena de suministro | [fundamentos](fundamentos-de-inventario-y-depositos.md) |
