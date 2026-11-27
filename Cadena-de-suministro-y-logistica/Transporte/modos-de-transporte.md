---
resumen: >-
  Los modos de transporte son las formas físicas de mover la carga: por tierra (camión, ferrocarril, ducto), por agua y por aire. Se distinguen por costo, velocidad, capacidad y confiabilidad, y se combinan en una cadena intermodal en la que el contenedor viaja como unidad de carga sin abrirse.
estado: vigente
estabilidad: estable
fuentes:
  - "Caplice, C. (MIT), Transportation Management: Fundamental Concepts, ESD.260, noviembre de 2006 (lect20; Mode Comparison Matrix, infraestructura, contenedores y pallets, TOFC y COFC, caso de los zapatos): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/06ab054739b3882c4bda862570c7266b_lect20.pdf"
  - "Caplice, C. (MIT), Transportation Management: Operational Networks, ESD.260, noviembre de 2006 (lect21, diapositiva 14: transportistas directos y consolidados): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/3a09fc7ee1175120b31399b1ce06b175_lect21.pdf"
  - "Rodrigue, 5.1 Transportation Modes, Modal Competition and Modal Shift, The Geography of Transport Systems (características y tipos de modos, comparación por modo; leído hasta la sección 3): https://transportgeography.org/contents/chapter5/transportation-modes-modal-competition-modal-shift/"
  - "Rodrigue, 5.3 Intermodal Transportation and Containerization (definición de intermodal, contenedor y TEU, umbrales de distancia, costos y escala del buque, contenedores vacíos, aéreo; leídas en parte las secciones 1, 3, 4 y 5): https://transportgeography.org/contents/chapter5/intermodal-transportation-containerization/"
  - "Rodrigue, 5.4 Maritime Transportation (granel, carga fraccionada, servicio regular y tramp, tiempo de navegación, carga contenedorizada; solo esos párrafos): https://transportgeography.org/contents/chapter5/maritime-transportation/"
  - "Rodrigue y Notteboom, 3.2 Transport Costs (costos operativos y de terminal por modo, energía): https://transportgeography.org/contents/chapter3/transport-costs/"
  - "Wikipedia, Intermodal container (secundaria, cita ISO 668; según el resumen): https://en.wikipedia.org/wiki/Intermodal_container"
  - "Wikipedia, Less than truckload shipping (secundaria y débil; según el resumen): https://en.wikipedia.org/wiki/Less_than_truckload_shipping"
  - "Wikipedia, Intermodal freight transport (secundaria; según el resumen): https://en.wikipedia.org/wiki/Intermodal_freight_transport"
  - "Modelo de datos de un ERP abierto, entidades de envío (ShipmentMethodType, CarrierShipmentMethod, ShipmentRouteSegment, ShipmentPackageRouteSeg; según el resumen): https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/entitydef/shipment-entitymodel.xml"
  - "Datos semilla de estados del mismo ERP abierto (estados del servicio del transportista por tramo; según el resumen): https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/data/seed/ProductSeedData.xml"
  - "Cadena-de-suministro-y-logistica/.investigacion/transporte.md (sección 2) y transporte-2.md (sección 2)"
aliases: [modos de transporte, modo de transporte, transportation modes, transporte carretero, autotransporte, camión, ferrocarril, transporte ferroviario, transporte marítimo, transporte fluvial, transporte aéreo, ducto, pipeline, carga completa, FTL, TL, full truckload, carga consolidada, LTL, less than truckload, intermodal, multimodal, contenedor, container, TEU, FEU, high cube, granel, bulk, carga fraccionada, break-bulk, servicio regular, liner, tramp, TOFC, COFC, pallet, europalet, tramo, segmento de ruta]
creado: 2026-11-27
revisado: 2026-11-27
---

# Modos de transporte

Los modos de transporte son las formas físicas de mover la carga: por tierra (camión, ferrocarril, ducto), por agua y por aire. Se distinguen por costo, velocidad, capacidad y confiabilidad, y se combinan en una cadena intermodal en la que el contenedor viaja como unidad de carga sin abrirse.

Elegir el modo es la primera decisión del cargador en [Transporte](transporte.md). Lo que cuesta cada uno y cómo se cobra está en [costo del flete](costo-del-flete.md). Para la paquetería de una tienda online, los [transportistas y agregadores](../../Comercio-electronico/Operaciones-del-comercio/Envios-y-logistica/transportistas-y-agregadores.md) de Comercio electrónico.

## Cómo se comparan los modos

Rodrigue clasifica los modos por atributos técnicos («speed, capacity, and motive technology»), operativos (límites de velocidad, seguridad, horarios) y comerciales (la demanda y quién es dueño). Para él, la competencia entre modos «depends primarily upon the distance traveled, the quantities shipped, and their value».

La matriz de Caplice (MIT, 2006, contexto de Estados Unidos) los compara así, con sus palabras:

| | Camión | Ferrocarril | Aéreo | Agua |
|---|---|---|---|---|
| Costo operativo | «Moderate» | «Low» | «High» | «Low» |
| Cobertura | «Pt to Pt» | terminal a terminal | terminal a terminal | terminal a terminal |
| Competidores | «Many» | «Few» | «Moderate» | «Few» |
| Tráfico típico | «All Types» | «Low to Mod Value, Mod to High density» | «High value, Low density» | «Low value, High density» |
| Capacidad (toneladas) | 10 – 25 | 50 – 12.000 | 5 – 12 | 1.000 – 6.000 |
| Velocidad | moderada | lenta | rápida | lenta |
| Disponibilidad | alta | moderada | moderada | baja |
| Consistencia del plazo | alta | moderada | moderada | baja |
| Pérdida y daño | baja | alta | baja | moderada |

Rodrigue lo cuenta en prosa y coincide en el fondo:

- Camión: «road transport tends to be most competitive over short distances and for small bundles of goods». En la matriz de Caplice es el único cuya cobertura es punto a punto.
- Ferrocarril: «the land transportation mode offering the highest capacity, with a 23,000 tons fully loaded coal unit train being the heaviest load ever carried».
- Ducto: mueve líquidos como derivados del petróleo «over long distances cost-effectively».
- Marítimo: «the most effective mode of moving large quantities of cargo over long distances». Su ventaja «does not rest on its speed, but on its capacity and on the continuity of its services».
- Aéreo: «The core advantage of air transportation is speed and flexibility in network configuration».

En costos, Rodrigue señala que «operating costs are high for air transport, terminal costs are significant for maritime transport», y que la energía es «nearly half of their operating costs» en el marítimo y el aéreo.

Da también una regla de distancia, como orientación y no como norma: camión por debajo de 500 km, ferrocarril entre 500 y 750 km y marítimo por encima de 750 km, con variaciones «according to the geographical setting». Agrega que «Distances above 500 km (longer than one day of trucking) usually require intermodal transportation». Es una sola fuente y las distancias dependen del país.

## Carga completa o consolidada

En camión, la carga viaja de dos maneras. En **carga completa** (FTL o TL), según el resumen de Wikipedia, el transportista lleva la carga de un solo cargador, que «effectively rents a trailer, typically paying a per-mile rate». En **carga consolidada** (LTL), el transportista junta envíos de muchos cargadores en una red de terminales locales y centros que consolidan por región; el viaje tarda más y cuesta menos. Por debajo está la paquetería, que maneja piezas de menos de unos 68 kg (150 libras). La fuente es secundaria y débil.

La diferencia es la misma que separa al transportista directo del consolidado en [Transporte](transporte.md#quién-mueve-la-carga). Juntar cargas propias para llenar un vehículo es una decisión del cargador, que está en [consolidación y ruteo](consolidacion-y-ruteo.md).

## Intermodal: un viaje, varios modos

Rodrigue define: «Intermodalism involves using at least two different modes in a trip from an origin to a destination through an intermodal transport chain». La clave es que «The entire trip is seen as a whole rather than as a series of legs, each marked by an individual operation with separate sets of documentation and rates». Según el resumen de Wikipedia, la unidad de carga no cambia entre un modo y otro.

Caplice muestra dos formas de montar el camión sobre el tren: el semirremolque sobre vagón plano («Trailer on Flat Car», TOFC) y el contenedor apilado de a dos («Container on Flat Car (COFC) Double Stack»). En su caso de los zapatos, de Nueva York a Kansas City, el camión tarda de 2,5 a 3 días y el ferrocarril de 5 a 10.

El aéreo casi no entra en estas cadenas: Rodrigue dice que solo usa camión para «"first and last miles"» y que sus unidades de carga «are not readily convertible with other modes».

> [!NOTE] Sin fuente todavía: la diferencia entre intermodal, multimodal y transporte combinado. Rodrigue tiene una sección «Intermodalism, Multimodalism and Transmodalism», pero en lo leído no define «multimodal». La definición jurídica (un solo contrato y un operador responsable de punta a punta) no se verificó.

## El marítimo y el contenedor

### Granel, carga general y contenedor

Rodrigue separa dos clases de carga marítima. El **granel** (petróleo, minerales, granos) va en buques especializados, «has a single origin, destination, and client and is prone to economies of scale». La **carga fraccionada** (break-bulk) es «general cargo that has been packaged in some way with the use of bags, boxes, drums, and particularly containers», con muchos orígenes, destinos y clientes. La carga general viaja en **servicios regulares** (liner), con «a regularly scheduled service between fixed ports of call», o en buques **tramp**, que «have no schedule».

El borde se corre: «it is possible, and increasingly common, to ship grain and oil, both bulk cargoes, in a container». La carga contenedorizada pasó de «9.8% of total tons-km in 2000 to 15.2% in 2021».

### El contenedor y el TEU

El contenedor es, para Rodrigue, «A large standard size metal box into which cargo is packed for shipment aboard specially configured transport modes (ISO 668)». Lo que cambia es que «the container, therefore, serves as the load unit rather than the cargo contained therein».

El **TEU** (twenty-foot equivalent unit) es la medida de capacidad: un contenedor de 20 pies de largo, 8 de ancho y 8'6" de alto. Como la mayoría ahora mide 40 pies, también se usa el **FEU**, y un FEU son dos TEU. El «high cube» es un pie más alto (9'6"). Según Rodrigue, el término lo usó por primera vez Richard F. Gibney en 1969. Según el resumen de Wikipedia, el TEU no considera la altura y uno de 45 pies cuenta como dos TEU.

Las dos fuentes dan capacidades algo distintas, de épocas distintas:

| Dato | Caplice (2006) | Wikipedia, con ISO 668 vigente |
|---|---|---|
| 20 pies (1 TEU) | 33 m³, carga útil 24,8 t | |
| 40 pies (1 FEU) | 67 m³, carga útil 28,8 t | |
| Masa bruta máxima | | 36.000 kg (ISO 668:2013, enmienda de 2016) |
| Participación | | cerca del 90 % de los contenedores son de 20 o 40 pies; los de 40, cerca del 70 % del volumen en TEU |

Caplice suma el doméstico de 53 pies de Estados Unidos (111 m³, 20,5 t) y dos pallets: el de 48 × 40 pulgadas, el más usado en ese país (27 % de todos los pallets), y el europalet de 1200 × 800 mm.

### Lo que hizo el contenedor con el costo

Rodrigue da cifras de una sola fuente académica, sin cruzar:

- «Relatively to bulk, container transportation reduces transport costs considerably, about 20 times less». El flete marítimo, que antes era «between 5 and 10% of the retail price», bajó a «about 1.5%».
- El buque más grande abarata cada caja: «A 5,000 TEU containership has operating costs per container 50% lower than a 2,500 TEU vessel». Los mayores pasaron de 6.000 TEU en 1996 a más de 22.000 hacia 2022.
- El buque pasa menos tiempo en puerto: el tiempo navegando era «around 25%» del año en los de carga fraccionada y es «around 70% for containerships».
- El comercio es desparejo y deja cajas vacías: «About 2.5 million TEUs of empty containers are stored in yards and depots worldwide», cerca del 20 % del movimiento portuario. Reposicionarlas cuesta tiempo y plata. Rodrigue agrega, por separado, que si un país importa mucho más de lo que exporta, el flete de importación tiende a ser más caro que el de exportación.

> [!NOTE] Sin fuente todavía: contenedor completo (FCL) frente a carga consolidada en contenedor (LCL), y cifras corrientes de fletes y flota marítima (UNCTAD, Review of Maritime Transport, no accesible).

## Cómo se registran el modo y el tramo

Un envío no siempre es un solo viaje: puede ser una secuencia de tramos con modos y transportistas distintos. Lo que muestran los sistemas abiertos consultados, según el resumen de su modelo de datos:

- Método de envío: un tipo de servicio (camión, aéreo, marítimo) ligado a un transportista, con el código de servicio que usa ese transportista.
- Tramo del envío (segmento de ruta): origen y destino, transportista y método, peso facturable con su unidad, costo real separado en transporte, servicio y otros, fechas estimadas y reales de salida y llegada, y número de seguimiento. Cada tramo tiene además un estado del servicio del transportista, que está en [despacho](../Despacho-y-entrega/despacho.md#los-estados-que-recorre).
- Bulto por tramo: el paquete con su código de seguimiento, sus costos, el monto asegurado y el contra reembolso.

De las fuentes de este tema sale además, como inferencia de la base: el contenedor como unidad de manejo con número, tamaño (TEU o FEU) y precinto, y el TEU como unidad para la capacidad. Los umbrales de distancia de Rodrigue no son datos de sistema; si un sistema sugiere el modo, son reglas que carga el usuario.

> [!NOTE] Sin fuente todavía: los estados de un envío según el modo (marítimo, aéreo, carretero). Los estados del documento de salida están en [despacho](../Despacho-y-entrega/despacho.md).
