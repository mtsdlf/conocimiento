---
resumen: >-
  Transporte es cómo se mueve la carga entre dos lugares, mirado desde el cargador, la empresa que la manda: en qué modo viaja, con qué transportista y bajo qué relación, cuánto paga y cómo junta cargas y arma recorridos. Su costo no es solo la tarifa, porque el plazo y el tamaño de cada envío cambian el stock que hay que tener.
estado: borrador
estabilidad: estable
fuentes:
  - "Caplice, C. (MIT), Transportation Management: Fundamental Concepts, ESD.260, noviembre de 2006 (lect20; tres capas de red, componentes de la red operativa, ejemplo de Shenzhen a Kansas City, costo total con transporte, cadena de tiempos de 56 días): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/06ab054739b3882c4bda862570c7266b_lect20.pdf"
  - "Caplice, C. (MIT), Transportation Management: Operational Networks, ESD.260, noviembre de 2006 (lect21, diapositivas 4, 9 a 14 y 17: componentes, economías de escala, alcance y densidad, transportistas directos y consolidados, continuo de relaciones; leídas las diapositivas 1 a 28): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/3a09fc7ee1175120b31399b1ce06b175_lect21.pdf"
  - "Caplice, C. (MIT), Transportation Management: Vehicle Routing, ESD.260, noviembre de 2006 (quién resuelve problemas de ruteo; OCW lo rotula como lect23): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/80e2e998f1048e857b995376b03c8a13_lect23.pdf"
  - "MIT OCW, ESD.260J Logistics Systems, lista de clases (Transportation IV, Shipper perspective; Transportation VI, Carrier operations): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/pages/lecture-notes/"
  - "Rodrigue y Notteboom, 3.2 Transport Costs, en Rodrigue, The Geography of Transport Systems (economías de escala, costos de terminal y de línea, tarifa frente a costo, costo para el usuario, intermediarios, 10 % del costo del producto): https://transportgeography.org/contents/chapter3/transport-costs/"
  - "Rodrigue, 5.1 Transportation Modes, Modal Competition and Modal Shift (costo de terminal como costo fijo independiente de la distancia; leído hasta la sección 3): https://transportgeography.org/contents/chapter5/transportation-modes-modal-competition-modal-shift/"
  - "Wikipedia, Freight forwarder (secundaria; según el resumen): https://en.wikipedia.org/wiki/Freight_forwarder"
  - "Cadena-de-suministro-y-logistica/.investigacion/transporte.md (secciones 1 y 6) y transporte-2.md (secciones 1 y 6)"
aliases: [transporte, transporte de cargas, freight transportation, transportation management, gestión del transporte, cargador, dador de carga, shipper, transportista, carrier, consignatario, consignee, agente de carga, freight forwarder, economía de escala del transporte, economía de distancia, economía de densidad, economía de alcance, transportista directo, transportista consolidado, flota propia, private fleet, flota dedicada, dedicated fleet, transportista núcleo, core carrier, mercado spot]
creado: 2026-11-27
revisado:
---

# Transporte

Transporte es cómo se mueve la carga entre dos lugares, mirado desde el cargador, la empresa que la manda: en qué modo viaja, con qué transportista y bajo qué relación, cuánto paga y cómo junta cargas y arma recorridos. Su costo no es solo la tarifa, porque el plazo y el tamaño de cada envío cambian el stock que hay que tener.

Es la tercera parte de [Cadena de suministro y logística](../cadena-de-suministro-y-logistica.md). Recibe de [Red de distribución](../Red-de-distribucion/red-de-distribucion.md) los lugares entre los que se mueve la carga, y de [Despacho y entrega](../Despacho-y-entrega/despacho-y-entrega.md) los bultos que salen por la puerta. El documento del despacho y sus estados están en [despacho](../Despacho-y-entrega/despacho.md); acá van el viaje, el transportista y la tarifa. Cuando la carga cruza una frontera, [Comercio exterior](../Comercio-exterior/comercio-exterior.md) agrega los documentos y la aduana.

## Desde el lado del cargador

El campo parte el transporte en dos miradas. El curso de logística del MIT tiene una clase «Shipper perspective, strategies and approaches for design and management» y otra «Carrier operations and yield management». Esta vertical toma la primera: la de quien manda la carga, que es la que lleva el ERP de una empresa que vende, distribuye o fabrica. La operación del transportista (sus terminales, su flota, cómo llena su capacidad y fija precios) queda afuera, igual que la conducción de flotas y el mantenimiento de vehículos.

## Quién mueve la carga

| Actor | Qué hace |
|---|---|
| Cargador (shipper) | Manda la carga y decide cómo viaja. Caplice nombra a «retailers, distributors, manufacturers» |
| Transportista (carrier) | Mueve la carga con su vehículo y cobra el flete |
| Consignatario (consignee) | Recibe la carga en destino |
| Intermediario | Organiza el movimiento sin mover la carga |

Rodrigue describe a los intermediarios (agentes de carga, despachantes, depósitos, aseguradores) así: «These firms do not physically transport the goods. Still, they must facilitate the grouping, storage, and handling of freight, as well as the complex paperwork and the financial and legal transactions involved in international trade». Según el resumen de Wikipedia, el agente de carga (freight forwarder) «co-ordinates and organizes the movement of shipments on behalf of a shipper» y puede actuar como agente o como transportista él mismo. Rodrigue ve una tendencia a integrarlos en operadores logísticos, que están en [tercerización logística](../Red-de-distribucion/tercerizacion-logistica.md).

Caplice separa a los transportistas en dos clases, y la diferencia explica con quién negocia el cargador:

- **Directos**: el vehículo va de origen a destino con la carga de un cliente. Lista «Taxi, TL, Unit trains, Charter/private planes, Tramp services, Courier».
- **Consolidados**: juntan cargas de muchos clientes en una red con terminales de transbordo. Lista «Bus/rail transit, LTL, Rail, Airlines, Ocean carriers/liner service, Package delivery».

Las dos se mezclan: un contenedor o un vagón completo es un viaje directo que va adentro de una red consolidada («sub-consolidation»).

## Qué decide el cargador

Caplice describe la red de transporte en tres capas. La física es «The actual path that the product takes». La operativa trata cada arco como un modo con costo y distancia, y cada nodo como un punto de decisión. La estratégica es el conjunto de caminos completos de origen a destino, cada uno con «end to end cost, distance, and service characteristics». El cargador decide en la capa estratégica: compara caminos enteros. Su ejemplo de 2005-2006, zapatos de Shenzhen a Kansas City, pone «All Water Route: 35 days, $0.65/pair» contra «Land Bridge: 28 days, $0.75/pair»; las cifras sirven por la estructura (días y costo por unidad), no por el valor.

Las decisiones que salen de ahí tienen cada una su nota:

1. **En qué viaja**: el modo y si va en carga completa o consolidada. Está en [modos de transporte](modos-de-transporte.md).
2. **Cuánto paga y cómo lo contrata**: la tarifa, los recargos, el contrato, el mercado spot y la licitación. Está en [costo del flete](costo-del-flete.md). Quién paga el flete en una venta internacional lo fija el [Incoterm](../Comercio-exterior/incoterms.md).
3. **Qué junta y en qué orden reparte**: cuándo sale el vehículo, qué carga lleva y qué recorrido hace. Está en [consolidación y ruteo](consolidacion-y-ruteo.md).
4. **Con quién y bajo qué relación**: del mercado spot a la flota propia, abajo.

### El transporte entra en el costo del stock

Caplice lista cuatro maneras en que el transporte pesa en el costo del cargador: «Cost of transportation (Value & Structure)», «Lead Time (Value & Variability & Schedule)», «Capacity (Limits on Q)» y «Miscellaneous Factors». Un modo más lento alarga el plazo y sube el stock en tránsito; uno menos confiable sube el [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md); uno con capacidad chica limita el tamaño del [lote](../../Inventario-y-depositos/Reposicion/lote-economico.md). Por eso propone comparar modos con el costo total del stock más el flete, TC(Q) = vD + A(D/Q) + rv(Q/2 + kσL) + B_SO(D/Q)Pr[SO], y la regla «Pick mode with smaller TRC». Los términos son los de [reposición](../../Inventario-y-depositos/Reposicion/reposicion.md).

El plazo también varía. Un ejemplo de Caplice, de un fabricante de consumo masivo, suma «Total Lead Time = 56 days» en seis tramos con promedio y desvío: producción 15 (12), transporte interno 2 (2), carga y demora en puerto 2 (1), océano 26 (5), descarga y despacho 5 (2) y transporte interno 6 (3).

Rodrigue agrega que el costo para el usuario incluye «time costs, and costs related to possible inefficiencies and risks (e.g. unexpected delays)», pero que «Many shippers or freight forwarders are primarily guided by direct monetary costs». Como orden de magnitud general, «It is not uncommon for transport costs to account for 10% of the total cost of a product».

## Por qué cargar más abarata

El costo por unidad baja con el tamaño y con la densidad, por razones distintas:

| Economía | Qué dice la fuente |
|---|---|
| De escala por envío | «The larger the shipment size, the lower the unit transport cost» (Rodrigue). Para Caplice «captures allocation of fixed costs over many items» y «drives mode selection» |
| De escala de red | Para Caplice «this is less clear»: depende de la dirección de los flujos, y los transportistas consolidados tienen más costos fijos en terminales |
| De alcance | Servir varios carriles con un mismo transportista cuesta menos que con varios; «Reverse flow mitigates the cost of repositioning» (Caplice) |
| De densidad | Más clientes por zona y más envíos por cliente; «Strong for Consolidated Carriers» (Caplice) |

La economía de escala tiene un techo: según Rodrigue, la unidad de transporte más grande en una ruta no puede superar la demanda disponible «without impairing its profitability».

El costo por kilómetro también baja con la distancia, porque cargar y descargar cuesta lo mismo en un viaje corto que en uno largo. Rodrigue lo funda en la estructura de costos de terminal, que imponen «fixed costs incurred independent of the distance traveled», separados de los costos de línea, que son «a function of the distance». Los libros de texto llaman a esto economía de distancia; ninguna de las fuentes leídas usa ese nombre.

> [!NOTE] Sin fuente todavía: el término «economía de distancia» y su definición en un libro de texto de logística (Ballou o Chopra y Meindl, no leídos). El mecanismo tiene fuente; la etiqueta, no.

## Del mercado spot a la flota propia

Caplice ordena la relación con el transportista como un continuo «from one-off to ownership», con cinco puntos:

| Relación | Qué es (lectura de la base sobre los rótulos de la fuente) |
|---|---|
| Mercado spot (spot market) | Se busca transportista viaje por viaje, al precio del momento |
| Transportistas alternos (alternate carriers) | Los que se llaman cuando el principal no toma la carga |
| Transportistas núcleo (core carriers) | Los pocos con contrato que llevan la mayor parte |
| Flota dedicada (dedicated fleet) | Vehículos y choferes de un tercero asignados solo al cargador |
| Flota propia (private fleet) | Vehículos del cargador |

En un extremo, la fuente pone «Use for random & distressed traffic»; en el otro, «Use for most reliable and steady flows». La regla que se lee de ahí: cuanto más estable y predecible es un flujo, más conviene atarlo; lo imprevisto va al spot. Caplice menciona también contratos flexibles de «Shared Risk/Reward». Cómo se fija el precio en cada punto está en [costo del flete](costo-del-flete.md#cómo-se-contrata-el-flete).

## Lo que lleva un sistema del transporte

El sistema de un cargador guarda pocos objetos, y cada uno tiene su nota:

- **Transportista**, con el tipo de relación del continuo de arriba (dato que Caplice sugiere y que la base no vio en los sistemas abiertos consultados).
- **Método o servicio de envío**, ligado a un transportista y a un modo: [modos de transporte](modos-de-transporte.md#cómo-se-registran-el-modo-y-el-tramo).
- **Tramo** del envío, con su modo, transportista, costo y fechas: también en [modos de transporte](modos-de-transporte.md#cómo-se-registran-el-modo-y-el-tramo).
- **Tarifa y regla de cálculo**, y el costo real por tramo: [costo del flete](costo-del-flete.md#qué-guarda-un-sistema-de-la-tarifa).
- **Viaje de entrega**, con vehículo, chofer y paradas: su registro y sus estados están en [despacho](../Despacho-y-entrega/despacho.md#lo-que-un-sistema-guarda-del-despacho); lo que hace falta para armar el recorrido, en [consolidación y ruteo](consolidacion-y-ruteo.md#el-viaje-y-sus-paradas-en-un-sistema).

El documento del despacho, que junta lo que sale y recorre estados hasta la entrega, es de [despacho](../Despacho-y-entrega/despacho.md).

## Qué hay en Transporte

- [Modos de transporte](modos-de-transporte.md): camión, ferrocarril, barco, avión y ducto comparados; carga completa o consolidada; intermodal; el contenedor, el TEU y el marítimo.
- [Costo del flete](costo-del-flete.md): de qué se arma la tarifa, el peso facturable, los recargos, cómo se contrata (contrato, spot, licitación) y la auditoría de fletes.
- [Consolidación y ruteo](consolidacion-y-ruteo.md): qué carga va junta y cuándo sale; el problema de ruteo de vehículos, el algoritmo de ahorros y lo que se sabe de cuánto ahorra; el llenado del vehículo.
