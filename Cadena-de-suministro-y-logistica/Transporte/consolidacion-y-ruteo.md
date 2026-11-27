---
resumen: >-
  Consolidar es decidir qué cargas viajan juntas y cuándo sale el vehículo; rutear es decidir en qué orden visita las paradas. Las dos bajan el costo del flete repartiendo el costo fijo de cada viaje, y el ruteo es un problema de optimización que se resuelve con heurísticas desde 1959.
estado: borrador
estabilidad: estable
fuentes:
  - "Caplice, C. (MIT), Transportation Management: Operational Networks, ESD.260, noviembre de 2006 (lect21, diapositivas 4, 9, 15, 16, 26 y 27: componentes, formas de consolidación, estructuras de red, estimación de distancias): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/3a09fc7ee1175120b31399b1ce06b175_lect21.pdf"
  - "Caplice, C. (MIT), Transportation Management: Vehicle Routing, ESD.260, noviembre de 2006 (definición del VRP, algoritmo de ahorros con ejemplo, heurísticas, reglas prácticas, rutas fijas y dinámicas, restricciones reales, caso adaptado de Goentzel 2004): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/80e2e998f1048e857b995376b03c8a13_lect23.pdf"
  - "Higginson y Bookbinder (1995), Markovian Decision Processes in Shipment Consolidation, Transportation Science 29(3):242-255 (según el resumen): https://api.crossref.org/works/10.1287/trsc.29.3.242"
  - "Çetinkaya (2005), Coordination of Inventory and Shipment Consolidation Decisions: A Review of Premises, Models, and Justification (solo el título): https://doi.org/10.1007/0-387-23392-x_1"
  - "Dantzig y Ramser (1959), The Truck Dispatching Problem, Management Science 6(1):80-91 (según el resumen): https://doi.org/10.1287/mnsc.6.1.80"
  - "Clarke y Wright (1964), Scheduling of Vehicles from a Central Depot to a Number of Delivery Points, Operations Research 12(4):568-581 (según el resumen): https://doi.org/10.1287/opre.12.4.568"
  - "Laporte (2009), Fifty Years of Vehicle Routing, Transportation Science 43(4):408-416 (según el resumen): https://doi.org/10.1287/trsc.1090.0301"
  - "Weigel y Cao (1999), Applying GIS and OR Techniques to Solve Sears Technician-Dispatching and Home Delivery Problems, Interfaces 29(1):112-130 (según el resumen): https://api.crossref.org/works/10.1287/inte.29.1.112"
  - "Wikipedia, Milk run (secundaria, una línea): https://en.wikipedia.org/wiki/Milk_run"
  - "Wikipedia, Vehicle routing problem (secundaria; según el resumen): https://en.wikipedia.org/wiki/Vehicle_routing_problem"
  - "Martello, Pisinger y Vigo (2000), The Three-Dimensional Bin Packing Problem, Operations Research 48(2):256-267 (según el resumen): https://api.crossref.org/works/10.1287/opre.48.2.256.12386"
  - "Bortfeldt y Wäscher (2013), Constraints in container loading: A state-of-the-art review, European Journal of Operational Research 229(1):1-20 (solo el título): https://doi.org/10.1016/j.ejor.2012.12.006"
  - "Documentación de un ERP abierto, Delivery Trip (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/delivery-trip"
  - "Cadena-de-suministro-y-logistica/.investigacion/transporte.md (sección 4) y transporte-2.md (sección 4)"
aliases: [consolidación, consolidación de cargas, shipment consolidation, freight consolidation, consolidación temporal, consolidación espacial, ruteo, ruteo de vehículos, enrutamiento, vehicle routing, VRP, problema de ruteo de vehículos, vehicle routing problem, truck dispatching problem, viajante, TSP, algoritmo de ahorros, savings algorithm, Clarke y Wright, hoja de ruta, recorrido de reparto, milk run, recorrido de lechero, viaje de entrega, delivery trip, llenado del vehículo, planificación de cargas, load planning, cubicaje, bin packing, container loading]
creado: 2026-11-27
revisado:
---

# Consolidación y ruteo

Consolidar es decidir qué cargas viajan juntas y cuándo sale el vehículo; rutear es decidir en qué orden visita las paradas. Las dos bajan el costo del flete repartiendo el costo fijo de cada viaje, y el ruteo es un problema de optimización que se resuelve con heurísticas desde 1959.

Es la tercera decisión del cargador en [Transporte](transporte.md), después del [modo](modos-de-transporte.md) y del [costo del flete](costo-del-flete.md), que es lo que se busca bajar. Los pedidos llegan preparados desde [preparación de pedidos](../../Inventario-y-depositos/Operacion-del-deposito/preparacion-de-pedidos.md), de Inventario, y el documento que registra lo que sale es el [despacho](../Despacho-y-entrega/despacho.md). Dónde están los centros de consolidación es de [Red de distribución](../Red-de-distribucion/red-de-distribucion.md#los-flujos-por-la-red).

## Consolidar: qué viaja junto y cuándo sale

Higginson y Bookbinder (1995), según su resumen, definen la consolidación como «a logistics strategy that combines two or more orders or shipments so that a larger quantity can be dispatched on the same vehicle». Funciona porque cada viaje tiene un costo fijo, como explica [Transporte](transporte.md#por-qué-cargar-más-abarata).

Caplice distingue «Basic Forms of Consolidation: Vehicle, Temporal, Spatial». La lectura de la base sobre los tres rótulos:

| Forma | Qué junta | Qué se paga |
|---|---|---|
| De vehículo | pedidos de distintos clientes en un mismo vehículo | paradas y tiempo de reparto |
| Temporal | pedidos de distintos momentos, esperando para salir con más carga | demora para los primeros pedidos |
| Espacial | cargas de distintos orígenes o destinos, por un recorrido o una red de transbordo | desvío y manipuleo en el centro |

La taxonomía es de un solo curso; no se encontró en un libro de texto.

### Cuándo despachar

La consolidación temporal tiene una decisión central. Higginson y Bookbinder la plantean así: cada vez que entra un pedido, hay que elegir entre despacharlo ya (con todos los que esperan) o seguir juntando «until at least the arrival of the next order». Su resultado: «For private carriage, the optimal policy is of the control-limit type; for common carriage, it may not be». Una política de límite de control despacha cuando lo acumulado llega a un umbral. Con flota propia, la regla simple sirve; con transportista contratado, la tarifa puede hacerla subóptima (inferencia de la base sobre el resumen).

Esperar para juntar carga interactúa con el stock: el que espera es stock que no llegó. La revisión de Çetinkaya (2005) trata la coordinación de las dos decisiones; en Inventario, el tamaño del pedido está en [lote económico](../../Inventario-y-depositos/Reposicion/lote-economico.md).

### Las formas de la red

Caplice clasifica las redes operativas por cuántos orígenes y destinos tienen:

| Red | Variantes |
|---|---|
| Uno a uno | directo |
| Uno a muchos o muchos a uno | directo con «Milk Runs», «Consolidation within the Vehicle», «Pool / Zone Skipping», transbordo |
| Muchos a muchos | sin punto de transbordo; con centro de distribución o cross-docking; con milk runs; o con un «hub» |

El recorrido de lechero (milk run) es, en la única línea de Wikipedia que lo define, «a circular route»: una vuelta que junta o reparte en varias paradas. El cross-docking, donde la mercadería entra y sale sin guardarse, se opera en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md#cross-docking-recibir-sin-guardar).

> [!NOTE] Sin fuente todavía: una definición académica del milk run con un ejemplo. Solo hay los rótulos de Caplice y una línea de Wikipedia.

## Rutear: en qué orden se visitan las paradas

Caplice define el problema de ruteo de vehículos (VRP) como «One origin, many destinations, many capacitated vehicles. Find: Lowest cost tours of vehicles to destinations». Lo resuelven cargadores («retailers, distributors, manufacturers»), transportistas de carga consolidada y paquetería, y empresas de servicio (reparación, residuos, correo).

### De dónde viene

Dantzig y Ramser (1959) lo plantearon como «The Truck Dispatching Problem». Según su resumen, trataban de rutear camiones de nafta entre una terminal y muchas estaciones de servicio para que «total mileage covered by the fleet is a minimum», con un procedimiento de programación lineal. Aclaraban: «No practical applications of the method have been made as yet».

Clarke y Wright (1964), según su resumen, dieron «an iterative procedure that enables the rapid selection of an optimum or near-optimum route», programado para computadora pero «also suitable for hand computation». Laporte (2009), a los cincuenta años, resume que el campo produjo «highly sophisticated exact mathematical programming decomposition algorithms and powerful metaheuristics».

### Un problema difícil, con heurísticas

El VRP es NP-difícil: según Wikipedia, «Because the traveling salesman problem is NP-hard, so is the VRP». Caplice da la escala: elegir y ordenar una ruta de 10 paradas entre 20 clientes ya admite 670.442.572.800 formas. Caplice agrupa las heurísticas en tres familias:

1. **Rutear primero y agrupar después**: una sola vuelta que se corta en rutas.
2. **Agrupar primero y rutear después**: el barrido por sectores y el algoritmo de ahorros.
3. **Programación entera con generación de columnas**: cada columna es una ruta posible con su costo, cada fila una parada que hay que cubrir.

Sobre una solución se aplican mejoras locales (2-opt, 3-opt) y metaheurísticas (búsqueda tabú, recocido simulado, algoritmos genéticos, colonia de hormigas).

### El algoritmo de ahorros

Es el de Clarke y Wright, en la versión de Caplice. Se empieza sirviendo cada parada con un viaje propio desde el depósito. Para cada par de paradas i y j se calcula cuánto se ahorra si se visitan en una misma vuelta: «Savings = c0i + cj0 – cij», lo que cuestan las dos idas y vueltas menos el tramo que las une. Se juntan los pares de mayor ahorro mientras el ahorro sea positivo y entre en el vehículo.

En el ejemplo de Caplice, con cuatro paradas y capacidad de tres, los ahorros son S(3,4) = 36, S(2,3) = 22, S(1,2) = 17, S(2,4) = 16, S(1,3) = 6 y S(1,4) = –3. El recorrido total baja de 132 a 96 y luego a 74.

### Qué tan cerca del óptimo

Las fuentes no son comparables punto a punto, y se dan las dos con su contexto:

- Caplice (2006), para el viajante, un solo vehículo: el vecino más cercano queda «In practice 20% above optimal», y las inserciones, entre 9 % y 19 % por encima.
- Wikipedia (secundaria, sin la referencia abierta), para el VRP con metaheurísticas recientes: «within 0.5% to 1% of optimal on instances with hundreds or thousands of points».

### Cuánto se recorre sin rutear

Antes de rutear se puede estimar la distancia. Caplice, tomando a Larson y Odoni (1981), da para n paradas en una zona de área X: «E[d_TSP] ≈ k·√(nX)», con k = 0,7124 en distancias en línea recta (n > 25) y 0,7650 en una grilla de calles. La vuelta completa es «d_TOUR ≈ 2·d_LineHaul + d_Local»: ir a la zona, recorrerla y volver. La distancia por parada baja con la raíz de la densidad de paradas, y de ahí sale, como lectura de la base, la economía de densidad de [Transporte](transporte.md#por-qué-cargar-más-abarata).

### Rutas fijas o dinámicas

| | Fijas | Dinámicas |
|---|---|---|
| Cómo | se repiten en un ciclo, se diseñan con un pronóstico para los «heavy days» y se rehacen cada trimestre o año | cambian cada día según los envíos reales |
| A favor | el chofer conoce la ruta; fáciles de ejecutar | mejor uso de camiones y choferes; flexibles |
| En contra | ineficientes cuando la demanda varía | difíciles de optimizar y de sostener; lo ejecutado puede no seguir el plan |

### Dónde falla el modelo

Caplice lista lo que el problema de libro deja afuera: horarios y muelles, tipos de camión y trailer, compatibilidad entre pedido y vehículo (refrigerados, peligrosos), entre pedidos («lumber & light bulbs, bottled water & dehydrated food») y entre vehículo y lugar, clientes preferidos, habilidades de los choferes, tráfico y cambios en el día. Sus reglas para revisar un plan a ojo: «Good routes are "rounded", not "star shaped"», «Good routes don't cross themselves or others» y «Good solutions "look like a daisy"». Y aconseja «Never discount the salty expert who has been doing this longer than you've been alive».

## Cuánto ahorra rutear

No hay un estudio independiente que dé un ahorro típico. Lo que hay es esto:

- **Un caso de curso.** Caplice, adaptado de Goentzel (2004): de 10 rutas a 7, «30% savings», y de 2.006 a 1.345 millas, «32% improvement». Es un solo caso, sin método publicado en la diapositiva, que advierte «Difficult to evaluate quality by inspection».
- **Un caso de empresa.** Weigel y Cao (1999), según su resumen, cuentan un sistema de ruteo y programación con SIG para el servicio técnico y la entrega a domicilio de Sears, en Estados Unidos, con «over $9 million in one-time savings and over $42 million in annual savings». Es un solo caso, en dólares y sin decir contra qué base se compara.
- **Lo que dicen los vendedores.** Según Wikipedia, los proveedores de software de ruteo declaran ahorros de 5 % a 30 %. Es afirmación comercial, no evidencia con método.

## El llenado del vehículo

Decidir cómo se acomoda la carga adentro es un tercer problema, distinto de qué va junto y en qué orden. Martello, Pisinger y Vigo (2000), según su resumen, lo formalizan como empaquetar cajas rectangulares en el mínimo número de contenedores: «The problem is strongly NP-hard and extremely difficult to solve in practice», aunque muchas instancias de hasta 90 cajas se resuelven al óptimo en un tiempo razonable. Bortfeldt y Wäscher (2013) revisan las restricciones reales de la carga de contenedores; de esa revisión solo se leyó el título.

> [!NOTE] Sin fuente todavía: la práctica del llenado (peso por eje, orden de descarga según las paradas, estiba) y cómo lo registra un sistema.

## El viaje y sus paradas en un sistema

El **viaje de entrega** es el registro del recorrido de un vehículo con sus paradas. Sus datos y sus estados, como los lleva un ERP abierto, están en [despacho](../Despacho-y-entrega/despacho.md#lo-que-un-sistema-guarda-del-despacho); según el resumen de la documentación de ese sistema, las paradas se pueden traer desde los documentos de salida y la ruta se optimiza con un servicio de mapas externo.

De las restricciones que lista Caplice sale, como inferencia de la base, lo que un sistema de ruteo necesita conocer:

- **Parada**: cliente, dirección, peso, volumen y otras dimensiones del pedido, ventana horaria, tiempo de servicio y restricciones (refrigerado, peligroso, tipo de muelle).
- **Vehículo y chofer**: tipo de camión y trailer, capacidad en cada dimensión, habilidades y licencias del chofer, horarios.
- **Ruta**: depósito de salida, paradas en orden, vehículo, chofer, hora de salida, hora estimada por parada, distancia y costo.
- **Plan**: fijo o dinámico, y su horizonte.

> [!NOTE] Sin fuente todavía: un objeto «carga» que agrupe envíos en un vehículo, con lo que va adentro y en qué orden se descarga. Los estados de lo que sale y los del viaje de entrega están en [despacho](../Despacho-y-entrega/despacho.md#los-estados-que-recorre).
