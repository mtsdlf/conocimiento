---
resumen: >-
  La planificación de la distribución (DRP) calcula, período por período, cuánto tiene que recibir cada depósito y cuándo hay que mandárselo, restando del pronóstico lo que hay y lo que ya viene. Los pedidos planificados de cada depósito se suman como necesidades del depósito que lo abastece, y así hasta la fábrica o el proveedor.
estado: borrador
estabilidad: estable
fuentes:
  - "Gershwin, S. B., Material Requirements Planning, diapositivas de MIT 2.853/2.854 (MIT OCW, otoño de 2016), diapositivas 3, 6, 10 a 14, 19, 23, 25 a 27, 31 a 34: https://ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/4eec617bb52d64f4ea1bed6d9905bc00_MIT2_854F16_MatrialRequire.pdf"
  - "Documentación de ayuda de un ERP comercial, versión 4.6C, Distribution Resource Planning (DRP): https://help.sap.com/saphelp_46c/helpdata/en/84/f1065301f011d295a90000e81d646f/content.htm"
  - "Domański y Adamczak, Planning of material flows in the supply chain based on algorithms of ERP systems (diapositivas de un curso de DRP I; solo el resumen del buscador, el servidor no respondió): https://old2.kgk.uni-obuda.hu/sites/default/files/Planning-of-material-flows-in-the-supply-chain-based-on-algorithms-of-ERP.pdf (según el resumen)"
  - "CSCMP, Supply Chain Management Terms and Glossary (2013), entrada DRP (copia no oficial): https://www.cisco-eagle.com/uploads/cscmp/cscmp-glossary.pdf"
  - "APQC, Process Classification Framework 7.4 (2024), 4.1.5 «Plan distribution requirements», 4.1.6 y 4.1.7: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Documentación de un ERP abierto, Master production schedule (rama 19.0): https://github.com/odoo/documentation/blob/19.0/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst"
  - "Campos de Master Production Schedule Item de otro ERP abierto (rama develop): https://github.com/frappe/erpnext/tree/develop/erpnext/manufacturing/doctype"
  - "Entidad MrpEvent de un tercer ERP abierto (rama trunk): https://github.com/apache/ofbiz-framework/blob/trunk/applications/datamodel/entitydef/manufacturing-entitymodel.xml"
  - "Cadena-de-suministro-y-logistica/.investigacion/planificacion-3.md, planificacion.md (sección 5), planificacion-2.md (sección 2) y fundamentos-y-contraria-2.md (secciones 2.1 y 10)"
aliases: [planificación de la distribución, planificación de requerimientos de distribución, distribution requirements planning, distribution resource planning, DRP, DRP II, plan de distribución, necesidades brutas, gross requirements, necesidades netas, net requirements, stock proyectado, projected on-hand, pedido planificado, planned order, recepción programada, scheduled receipt, neteo, netting, despliegue, deployment]
creado: 2026-11-27
revisado:
---

# Planificación de la distribución

La planificación de la distribución (DRP) calcula, período por período, cuánto tiene que recibir cada depósito y cuándo hay que mandárselo, restando del pronóstico lo que hay y lo que ya viene. Los pedidos planificados de cada depósito se suman como necesidades del depósito que lo abastece, y así hasta la fábrica o el proveedor.

El glosario del CSCMP lo define como «A system of determining demands for inventory at distribution centers and consolidating demand information in reverse as input to the production and materials system». APQC lo llama 4.1.5, «Plan distribution requirements». Es el plan por artículo y depósito de [Planificación](planificacion.md): toma el [pronóstico de demanda](pronostico-de-demanda.md) de cada lugar y lo convierte en traslados. Los lugares y sus vínculos son de la [Red de distribución](../Red-de-distribucion/red-de-distribucion.md).

## La misma cuenta que el MRP

El DRP aplica a una red de depósitos la cuenta que el MRP aplica a una lista de materiales. Unas diapositivas de un curso de DRP, según el resumen del buscador, lo presentan así: adapta el MRP a redes de distribución de varios niveles. La cuenta, como la explican las diapositivas de MIT 2.854 sobre el MRP:

- **Necesidades brutas**: «What must be delivered in the future, and when». En un depósito, el pronóstico más los pedidos de clientes ya tomados.
- **Recepciones programadas**: lo que ya se pidió y todavía no llegó.
- **Stock proyectado**: lo que va a quedar al final de cada período.
- **Necesidades netas**: «(Gross requirements) – (On-hand inventory)», lo que falta después de usar el stock.
- **Recepciones de pedidos planificados**: lo que tiene que llegar para cubrir lo neto, ajustado al tamaño de lote.
- **Lanzamientos de pedidos planificados**: lo mismo, corrido hacia atrás por el plazo. «Lead times are 1 week. Therefore, order release must occur one week before delivery is required.»

El tiempo se divide en períodos: «time buckets — days, weeks, or whatever is convenient». El stock de seguridad entra como piso: MIT lo define como «the planned minimal inventory level», en lugar de cero.

## La tabla por período, con el ejemplo de MIT

El ejemplo de MIT (diapositivas 11 a 14) parte de 30 unidades en stock, lotes de 75 y plazo de una semana:

| Semana | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Necesidades brutas | 15 | 20 | 50 | 10 | 30 | 30 | 30 | 30 |
| Necesidades netas | 0 | 5 | 50 | 10 | 30 | 30 | 30 | 30 |
| Recepciones planificadas | | 75 | | | 75 | | 75 | |
| Lanzamientos planificados | 75 | | | 75 | | 75 | | |

MIT lo cuenta así: «15 of the initial 30 units of inventory are used to satisfy Week 1 demand. The remaining 15 units are 5 less than required to satisfy Week 2 demand». Con lotes de 75, «The first arrival must occur in Week 2», «75 units last until Week 4, so plan arrival in Week 5», y lo mismo en la semana 7. Cada lanzamiento sale una semana antes de su llegada. La fila de recepciones se reconstruyó del texto de las diapositivas, porque la tabla extraída del PDF quedó corrida una columna.

MIT da tres reglas de lote: «Lot-for-lot» (lo neto de cada período), «Fixed order period» (lo neto de P períodos) y «Fixed order quantity», donde el lote puede salir del [lote económico](../../Inventario-y-depositos/Reposicion/lote-economico.md).

## Cómo los pedidos de los depósitos se vuelven necesidades del central

En el MRP, «The planned order releases for Level 0 are the gross requirements for Level 1». En el DRP, el nivel de abajo es el depósito que vende y el de arriba, el que lo abastece: los lanzamientos planificados de cada depósito se suman y son las necesidades brutas del central. El resumen de las diapositivas del curso de DRP lo dice como que el programa de pedidos del eslabón de abajo se vuelve automáticamente el pronóstico del de arriba. Un ERP comercial lo implementa igual: «The DRP run in the distribution centers creates calls for stock transfer purchase requisitions in the supplying plants», y «A DRP run for the supplying plants creates planned orders for production».

Un ejemplo de la base (no de una fuente), con la misma cuenta. Un central abastece a dos depósitos durante seis semanas.

**Depósito A**: vende 20 por semana, tiene 40, stock de seguridad 10, lote de 50, una semana de viaje desde el central.

| Semana | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Necesidades brutas | 20 | 20 | 20 | 20 | 20 | 20 |
| Stock proyectado (inicio 40) | 20 | 50 | 30 | 10 | 40 | 20 |
| Necesidades netas | 0 | 10 | 0 | 0 | 20 | 0 |
| Recepciones planificadas | | 50 | | | 50 | |
| Lanzamientos planificados | 50 | | | 50 | | |

**Depósito B**: vende 15 por semana, tiene 45, stock de seguridad 5, lote de 40, dos semanas de viaje.

| Semana | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Necesidades brutas | 15 | 15 | 15 | 15 | 15 | 15 |
| Stock proyectado (inicio 45) | 30 | 15 | 40 | 25 | 10 | 35 |
| Necesidades netas | 0 | 0 | 5 | 0 | 0 | 10 |
| Recepciones planificadas | | | 40 | | | 40 |
| Lanzamientos planificados | 40 | | | 40 | | |

**Central**: sus necesidades brutas son la suma de los lanzamientos de A y B. Tiene 120, sin stock de seguridad, repone lote por lote desde la fábrica o el proveedor con dos semanas de plazo.

| Semana | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Necesidades brutas (A + B) | 90 | 0 | 0 | 90 | 0 | 0 |
| Stock proyectado (inicio 120) | 30 | 30 | 30 | 0 | 0 | 0 |
| Necesidades netas | 0 | 0 | 0 | 60 | 0 | 0 |
| Recepciones planificadas | | | | 60 | | |
| Lanzamientos planificados | | 60 | | | | |

Los depósitos venden parejo (35 por semana entre los dos) y el central ve dos golpes de 90. El lanzamiento de 60 de la semana 2 es lo que el central le pasa a Compras o a Producción. Si un depósito tuviera más de un origen, la red tiene que decir de cuál sale cada parte; el ERP comercial pide de antemano «a distribution network, including identification of quota arrangements and lead times».

## Frente al punto de pedido

El [punto de pedido](../../Inventario-y-depositos/Reposicion/punto-de-pedido.md), de Inventario, mira la posición de stock de un artículo en un lugar y dispara cuando cruza el umbral. El DRP proyecta hacia adelante y en toda la red. En el ejemplo, un central con punto de pedido se entera de los 90 de la semana 4 cuando llega la solicitud; con DRP lo ve en la semana 1 y lanza a tiempo (inferencia de la base).

| | Punto de pedido | DRP |
|---|---|---|
| Mira | el pasado y la posición de hoy | el pronóstico de los períodos que vienen |
| Alcance | un artículo en un lugar | un artículo en todos los lugares, encadenados |
| Dispara | cuando la posición cruza el punto | cuando el stock proyectado cae bajo el piso |
| Lo que ve el de arriba | los pedidos cuando llegan | los pedidos planificados antes de que salgan |
| Familia | tirar | empujar (MIT: «MRP is a push system») |

La tabla es síntesis de la base. Una empresa puede usar los dos: DRP entre el central y los depósitos, y un mínimo en cada local para lo que no se pronostica bien. Elegir es de Planificación; cómo se calcula el punto, de Inventario.

## Cómo falla el DRP

MIT enumera los problemas del MRP, que son los mismos:

- **Supone certeza.** «MRP is deterministic but reality is not. Therefore, the system needs safety stock and safety lead times.» El DRP hereda el error de cada [pronóstico de demanda](pronostico-de-demanda.md) de la red.
- **Supone capacidad infinita.** Calcula lo que hace falta, no lo que el central, el camión o la fábrica pueden. Por eso «it frequently produces non-optimal or infeasible schedules» y «it requires constant manual intervention».
- **Es nervioso.** «Nervousness — drastic changes in schedules due to small deviations from plans». Un cambio chico en un depósito mueve un lote en el central. MIT propone congelar las primeras semanas del plan y pregunta: «What price is paid for freezing?»
- **Pasa los lotes hacia arriba.** El central ve golpes aunque la venta sea pareja, como en el ejemplo. Es una de las causas del [efecto látigo](efecto-latigo.md), la agrupación de pedidos.

> [!NOTE] Sin fuente todavía: cómo se reparte el stock del central cuando no alcanza para todos los depósitos (el reparto justo, «fair share», o el despliegue). El ERP comercial nombra la función de despliegue («deployment function») sin describirla.

APQC lista lo que la red le impone al plan: restricciones de depósito, de inventario, de transporte y de almacenaje (4.1.6), y políticas de despliegue dinámico (4.1.7.3). Juntar la carga de varios depósitos en un camión es 4.1.5.9, «Calculate and optimize destination load plans», que en esta base es [consolidación y ruteo](../Transporte/consolidacion-y-ruteo.md).

## Lo que guarda un sistema para planificar la distribución

Los tres ERP abiertos consultados implementan el plan por períodos para la producción, no un DRP de depósitos; muestran el patrón común:

- **La grilla por artículo, lugar y período**: uno guarda filas de stock inicial, demanda pronosticada, demanda indirecta, reposición y stock pronosticado, con períodos anuales, mensuales, semanales o diarios. Su «demanda indirecta» es la fila de lo que piden otros niveles: el mismo mecanismo que suma los lanzamientos de los depósitos en el central.
- **La fecha de lanzamiento** separada de la fecha de entrega, con el plazo acumulado: otro la guarda como `order_release_date`.
- **Un evento por movimiento planificado**: el tercero registra producto, fecha, cantidad, lugar y un lugar de destino (`facilityIdTo`) para los traslados.
- **La sugerencia no es la orden**: el primero sugiere cantidades y no crea órdenes solo, y marca con colores si la orden generada coincide con lo sugerido.

Lo que agrega la base para un DRP de depósitos:

- **El árbol de la red**: qué lugar abastece a cuál, con plazo de viaje y proporción si hay más de un origen.
- **Parámetros por artículo y lugar**: stock de seguridad, regla de lote, plazo.
- **El pedido planificado de traslado**, con origen, destino, fecha de lanzamiento y de llegada, que al confirmarse pasa a ser una transferencia entre depósitos. La salida y la entrada del traslado se registran en Inventario; el viaje, en [Transporte](../Transporte/transporte.md).
- **Una zona congelada** del horizonte, para que el plan no cambie todos los días.

Para leer más: las diapositivas de MIT 2.854 sobre MRP, de la 10 a la 25, tienen la cuenta completa con un ejemplo en ocho semanas.
