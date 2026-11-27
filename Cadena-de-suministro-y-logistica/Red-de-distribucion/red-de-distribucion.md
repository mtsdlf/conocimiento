---
resumen: >-
  La red de distribución es el conjunto de lugares por los que pasa la mercadería entre el proveedor y el cliente (plantas, depósitos, centros de distribución, comercios) y los caminos que la unen. Se diseña eligiendo dónde se guarda el stock y por dónde viaja, y se juzga por dos cosas: qué necesidades del cliente cubre y cuánto cuesta cubrirlas.
estado: vigente
estabilidad: estable
fuentes:
  - "Chopra, S., Designing the Distribution Network in a Supply Chain, Kellogg School of Management, Northwestern University (PDF de noviembre de 2002, texto del autor que antecede al capítulo 4 de Chopra y Meindl, Supply Chain Management; se leyó el artículo, no el libro), secciones 0 a 4: https://transportation.tech.northwestern.edu/docs/research/core-topics/logistics-and-supply-chain-management/Chopra_DistributionSupplyChain.pdf"
  - "Chopra y Meindl, Supply Chain Management, 5.ª ed. (Pearson, 2013), diapositivas del editor del capítulo de diseño de la red de distribución, diapositivas 4 a 6 (según el resumen): https://www.slideshare.net/slideshow/supply-chain-management-chap-4/52277239"
  - "Caplice, C. (MIT CTL), Transportation Management: Network & Hubs, ESD.260 Logistics Systems, archivo lect25, diciembre de 2006, diapositivas 3 a 6 y 12 a 18: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/421e474d22fae64f415aea445a34a254_lect25.pdf"
  - "CSCMP, Supply Chain Management Terms and Glossary, agosto de 2013, entradas «Drop Ship» y «Third-Party Logistics Provider» (copia archivada): https://arquivo.pt/wayback/20160522172303id_/http://cscmp.org/sites/default/files/user_uploads/resources/downloads/glossary-2013.pdf"
  - "CSCMP y Kearney, 36.º State of Logistics Report (2025), según FreightWaves (según el resumen): https://www.freightwaves.com/?p=536936"
  - "CSCMP y Kearney, 37.º State of Logistics Report (2026), según Logistics Management (según el resumen): https://www.logisticsmgmt.com/article/37th_state_of_logistics_stronger_through_disruption/ai"
  - "SupplyChainBrain, Business logistics costs in the U.S. reach an all-time high (resultado del buscador, según el resumen): https://www.supplychainbrain.com/logistics/all-logistics/article/15875773/business-logistics-costs-in-the-us-reach-an-all-time-high"
  - "Documentación de sistemas abiertos: un ERP abierto (reabastecer un depósito desde otro, envío directo y cross-docking, versión 18.0, según el resumen), otro ERP abierto (Stock Entry, según el resumen) y el modelo de datos de un tercero (entidades Facility, FacilityType e InventoryTransfer y estados semilla INVENTORY_XFER_STTS), según Cadena-de-suministro-y-logistica/.investigacion/red-de-distribucion-2.md, sección 5"
  - "Cadena-de-suministro-y-logistica/.investigacion/red-de-distribucion.md (sección 1)"
  - "Cadena-de-suministro-y-logistica/.investigacion/red-de-distribucion-2.md (secciones 1 y 5)"
aliases: [red de distribución, red logística, distribution network, supply chain network, diseño de la red de distribución, distribution network design, eslabones de la cadena, nodos, centro de distribución, CD, distribution center, DC, envío directo, drop shipping, drop ship, combinación en tránsito, in-transit merge, cross-docking, cross-dock, costo logístico total, total logistics cost, State of Logistics]
creado: 2026-11-27
revisado: 2026-11-27
---

# Red de distribución

La red de distribución es el conjunto de lugares por los que pasa la mercadería entre el proveedor y el cliente (plantas, depósitos, centros de distribución, comercios) y los caminos que la unen. Se diseña eligiendo dónde se guarda el stock y por dónde viaja, y se juzga por dos cosas: qué necesidades del cliente cubre y cuánto cuesta cubrirlas.

Es la parte de [Cadena de suministro y logística](../cadena-de-suministro-y-logistica.md) que fija los lugares. [Planificación](../Planificacion/planificacion.md) dice cuánto mandar a cada uno y cuándo, con la [planificación de la distribución](../Planificacion/planificacion-de-la-distribucion.md); [Transporte](../Transporte/transporte.md) mueve la carga por los caminos que la red define; [Despacho y entrega](../Despacho-y-entrega/despacho-y-entrega.md) registra cada salida y cada llegada. Lo que pasa adentro de cada depósito (recibir, guardar, preparar) es de [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md).

## Los eslabones y cómo se juzga la red

Chopra define la distribución como «the steps taken to move and store a product from the supplier stage to a customer stage in the supply chain». Las clases del MIT plantean la red con cuatro niveles de nodos: proveedor, planta, depósito y cliente. Cada lugar es un nodo y cada camino por donde se manda mercadería, un arco. Entre el depósito y el cliente final puede haber un distribuidor o un comercio, que son más eslabones con stock propio.

Según Chopra, una red se evalúa «along two dimensions: 1. Customer needs that are met 2. Cost of meeting customer needs». Del lado del cliente lista seis medidas que dependen de la forma de la red: tiempo de respuesta («the time between when a customer places an order and receives delivery»), variedad de productos, disponibilidad («the probability of having a product in stock when a customer order arrives»), experiencia del cliente, visibilidad del pedido y devolubilidad (qué tan fácil es devolver y cómo lo maneja la red). Del lado del costo nombra cuatro: inventario, transporte, instalaciones y manipulación, e información. Las diapositivas de la 5.ª edición del libro traen las mismas dos listas (según el resumen).

## Las dos decisiones y los seis diseños

Para Chopra, dos preguntas definen una red: «1. Will product be delivered to the customer location or picked up from a preordained site? 2. Will product flow through an intermediary (or intermediate location)?». Las combinaciones dan seis diseños:

| Diseño (nombre en Chopra) | Dónde está el stock | Cómo llega al cliente | Lo que dice el artículo |
|---|---|---|---|
| Envío directo desde el fabricante («Manufacturer storage with direct shipping», drop shipping) | en el fabricante | el fabricante lo manda al cliente | centraliza el stock; responde lento y el transporte es caro porque las distancias son largas; se complica con «more than 20-30 sourcing locations» |
| Envío directo con combinación en tránsito («... and in-transit merge») | en varios fabricantes | las partes se juntan en el camino y llegan en una sola entrega | mejor experiencia que el anterior; «no more than four or five sourcing locations» |
| Almacén del distribuidor con paquetería («Distributor storage with package carrier delivery») | en el depósito del distribuidor o del comercio | por una empresa de paquetería | más stock que el envío directo, porque agrega la incertidumbre en un nivel más bajo |
| Almacén del distribuidor con última milla («Distributor storage with last mile delivery») | en el depósito del distribuidor | reparto propio hasta el domicilio | el transporte más caro de todos, según la lectura del informe |
| Almacén con retiro por el cliente («Manufacturer / distributor storage with customer pickup») | en el fabricante o el distribuidor | el cliente retira en un punto | «Increased processing cost at the pickup site is the biggest hurdle» |
| Comercio con retiro («Retail storage with customer pickup») | en el local | el cliente se lo lleva | «It is more expensive than all other options to provide a high level of product availability» |

El artículo es de 2002 y piensa en el comercio minorista y el electrónico, pero aclara que, entre otras etapas de la cadena, «many of the same options still apply». Sus cifras de ejemplo (rotaciones, costo por entrega a domicilio) son de esos años y no se usan como valores vigentes. Las tablas del libro que califican cada diseño por dimensión y por tipo de producto no se leyeron.

Casi ninguna empresa usa un solo diseño. Chopra lo dice así: «Only niche companies will end up using a single distribution network. Most companies are best served by a combination of delivery networks». Su ejemplo es un distribuidor industrial con stock local para lo urgente, un centro nacional para lo de rotación intermedia, y «Very slow moving items are typically drop shipped from the manufacturer».

## Cuándo conviene un intermediario

Un distribuidor agrega valor cuando hay «many small players at the customer stage, each requiring a small amount of the product at a time», según Chopra. Entre sus razones: el transporte de entrada se abarata porque llega en camión completo, el de salida porque combina productos de varios fabricantes, y el stock baja porque el distribuidor «aggregates safety inventory rather than disaggregating at each retailer». Ese último efecto es la [centralización del stock](centralizacion-del-stock.md). También le da al fabricante «A more stable order stream», lo que se conecta con el [efecto látigo](../Planificacion/efecto-latigo.md).

## Los flujos por la red

Sobre esos lugares, la mercadería sigue unos pocos caminos que un sistema tiene que poder representar:

- Por depósito. Entra, se guarda, se prepara y sale. Es el flujo de los diseños con almacén; lo de adentro está en [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md).
- Envío directo. CSCMP lo define como «A customer fulfillment strategy where products are shipped directly from the manufacturer or distributor to a customer bypassing the retail or secondary distribution location», y agrega que «Billing transactions occur in the normal manner, only the material flow is altered». La factura sigue el camino de siempre; la mercadería, no.
- Cross-docking. La mercadería entra a un centro y sale hacia otro destino sin guardarse. Desde la red es el centro donde se juntan las cargas (lectura de la base); según el MIT, «Hub consolidation reduces costs» porque el transporte tiene un costo fijo por vehículo, a cambio de operar el centro, desviarse («Circuity») y sumar «Added time in-transit». Cómo se opera adentro del centro está en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md#cross-docking-recibir-sin-guardar); cómo se arman los recorridos, en [consolidación y ruteo](../Transporte/consolidacion-y-ruteo.md).
- Transferencia entre depósitos. Un depósito propio abastece a otro. La salida y la entrada son movimientos de Inventario, y en el medio el stock queda [en tránsito](../../Inventario-y-depositos/Existencias/estados-del-stock.md); el viaje es de [Transporte](../Transporte/transporte.md) y de [despacho](../Despacho-y-entrega/despacho.md). En la Argentina lleva remito, como explica [Inventario y depósitos en la Argentina](../../Inventario-y-depositos/inventario-y-depositos-en-argentina.md).
- De vuelta. Lo que el cliente devuelve recorre la red al revés; es la [logística inversa](../Despacho-y-entrega/logistica-inversa.md), y la devolubilidad de Chopra mide qué tan bien lo hace la red.

## El costo logístico total

Las decisiones de la red se juzgan por la suma de los costos y no por uno solo. Más depósitos acercan el stock al cliente y bajan el tiempo de respuesta, pero suben el inventario y el costo de las instalaciones. Menos depósitos hacen lo contrario y alargan los viajes. Chopra lo resume en que el costo total, al sumar instalaciones, «first decrease and then increase»; la curva y su lectura están en [diseño de la red](diseno-de-la-red.md).

Para un país, el indicador conocido es el costo logístico como porcentaje del PIB; el que se publica cada año es el de Estados Unidos, de una fuente de la industria (CSCMP y Kearney). Según la prensa, la 36.ª edición (2025) dio USD 2,58 billones para 2024, «about 8.8% of nominal GDP», y la 37.ª (julio de 2026), «$2.4 trillion, or 7.8% of GDP», sin decir de qué año, contra «$2.6 trillion and 8.7% of GDP in 2025». Las dos no encajan del todo (8,8 % y 8,7 % con montos parecidos): puede ser un dato revisado o dos años distintos, y sin abrir los informes no se sabe. Para 2022, otra cobertura da 9,1 %, «the highest mark of all time». Es un indicador de país, útil para tendencias y no para comparar una empresa.

> [!NOTE] Sin fuente todavía: el costo logístico como porcentaje de las ventas de una empresa, por rubro, y cualquier indicador de costo logístico para la Argentina o la región.

## Qué tiene que poder representar un sistema de la red

Los tres sistemas abiertos consultados coinciden en cuatro piezas, aunque cada uno las resuelve distinto:

- Ubicación con tipo y jerarquía. Uno guarda cada instalación con su tipo (depósito, local, planta), su instalación madre, su dueño, fechas de apertura y cierre, ubicación geográfica y días de despacho por defecto. Las [ubicaciones](../../Inventario-y-depositos/Operacion-del-deposito/ubicaciones.md) de adentro del depósito viven en la misma tabla.
- Relación de abastecimiento. Otro tiene, en cada depósito, la lista de depósitos que lo pueden abastecer, y de ahí sale una ruta que se habilita por producto (según el resumen). Esa relación es la red: dice qué demanda se agrupa en qué lugar.
- Transferencia con origen, destino y tránsito. El primero registra origen, destino, fecha de envío y de recepción, y cinco estados: «Requested», «Scheduled», «En-Route», «Complete» y «Cancelled». Los otros dos ponen el stock en camino en una ubicación de tránsito; las dos formas están comparadas en [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md#estado-o-ubicación-dos-maneras-de-modelarlo).
- Envío directo como un solo movimiento. En uno, la venta genera un pedido de compra al proveedor y un único movimiento del proveedor al cliente (según el resumen). Para la combinación en tránsito, Chopra pide además seguir cada parte por separado: «Up to the point of merge, the order from each manufacturer is tracked separately».

Los tres registran la ejecución, no la planificación: quien construye un planificador tiene que traer la red como dato propio (inferencia de la base).

## Qué hay en Red de distribución

- [Diseño de la red](diseno-de-la-red.md): cuántos depósitos y dónde, las tres preguntas del diseño, la curva de costo total contra cantidad de instalaciones y qué deja afuera un modelo.
- [Centralización del stock](centralizacion-del-stock.md): cuánto stock de seguridad se ahorra al agrupar ubicaciones, la ley de la raíz cuadrada con el ejemplo del MIT, sus supuestos y su crítica.
- [Tercerización logística](tercerizacion-logistica.md): qué es un 3PL y un 4PL según CSCMP, qué se contrata y qué dice el estudio anual de la industria.
