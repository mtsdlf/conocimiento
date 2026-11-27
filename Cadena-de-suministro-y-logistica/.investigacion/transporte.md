# Investigación: vertical Transporte

Advertencia de método, al principio porque condiciona todo. El presupuesto de búsqueda web de la sesión se agotó antes de la primera consulta, así que no hubo rondas de búsqueda: solo pude abrir URLs que ya conocía. No leí ninguno de los libros de texto (Ballou, Chopra y Meindl, Simchi-Levi) ni los dos papers fundacionales completos (el acceso a INFORMS devolvió 403); de los papers tengo solo los metadatos de Crossref. Lo que sigue se apoya sobre todo en dos presentaciones de Caplice (MIT) que sí leí enteras y en Wikipedia como fuente secundaria. Los componentes costo-del-flete y modos-de-transporte quedan flojos en fuentes primarias. Todo lo que dice «hueco» es un hueco real.

Escala de puntaje: A = autoridad, P = profundidad, E = ejemplos, U = unicidad (1 a 3). Marcas: [L] leído completo, [M] metadatos, [S] resumen secundario.

---

## 0. Fuentes usadas en toda la vertical

| Id | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| F1 | Caplice, «Transportation Management: Fundamental Concepts», MIT ESD.260, nov. 2006 (diapositivas, lect20) | https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/06ab054739b3882c4bda862570c7266b_lect20.pdf | primaria (material de curso) | 3 | 2 | 3 | 3 | [L] (texto extraído con pdftotext; las figuras no) |
| F2 | Caplice, «Transportation Management: Vehicle Routing», MIT ESD.260, nov. 2006 (diapositivas) | https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/80e2e998f1048e857b995376b03c8a13_lect23.pdf | primaria (material de curso) | 3 | 2 | 3 | 3 | [L] |
| F3 | Página del curso ESD.260J con la lista de clases | https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/pages/lecture-notes/ | primaria | 3 | 1 | 1 | 2 | [L] |
| F4 | Dantzig y Ramser (1959), «The Truck Dispatching Problem», Management Science 6(1), 80-91 | https://doi.org/10.1287/mnsc.6.1.80 (metadatos en https://api.crossref.org/works/10.1287/mnsc.6.1.80) | primaria | 3 | (3) | (2) | 3 | [M] solo metadatos |
| F5 | Clarke y Wright (1964), «Scheduling of Vehicles from a Central Depot to a Number of Delivery Points», Operations Research 12(4), 568-581 | https://doi.org/10.1287/opre.12.4.568 (metadatos en https://api.crossref.org/works/10.1287/opre.12.4.568) | primaria | 3 | (3) | (2) | 3 | [M] |
| F6 | Wikipedia, Vehicle routing problem | https://en.wikipedia.org/wiki/Vehicle_routing_problem | secundaria | 1 | 2 | 1 | 1 | [S] |
| F7 | Wikipedia, Dimensional weight | https://en.wikipedia.org/wiki/Dimensional_weight | secundaria | 1 | 2 | 2 | 1 | [S] |
| F8 | Wikipedia, Less than truckload shipping | https://en.wikipedia.org/wiki/Less_than_truckload_shipping | secundaria | 1 | 1 | 1 | 1 | [S] |
| F9 | Wikipedia, Intermodal container | https://en.wikipedia.org/wiki/Intermodal_container | secundaria (cita ISO 668) | 2 | 2 | 2 | 1 | [S], primeros 100.000 de 186.000 caracteres |
| F10 | Wikipedia, Intermodal freight transport | https://en.wikipedia.org/wiki/Intermodal_freight_transport | secundaria | 1 | 1 | 1 | 1 | [S] |
| F11 | Wikipedia, Freight forwarder | https://en.wikipedia.org/wiki/Freight_forwarder | secundaria (cita FIATA y 49 U.S.C. 13102) | 1 | 2 | 1 | 1 | [S] |
| F12 | Wikipedia, Freight audit | https://en.wikipedia.org/wiki/Freight_audit | secundaria, marcada «necesita citas» | 1 | 1 | 1 | 1 | [S] |
| F13 | Wikipedia, Transportation management system | https://en.wikipedia.org/wiki/Transportation_management_system | secundaria | 1 | 1 | 1 | 1 | [S] |
| F14 | Wikipedia, Bill of lading | https://en.wikipedia.org/wiki/Bill_of_lading | secundaria | 1 | 2 | 1 | 1 | [S] |
| F15 | ICC, página de Incoterms 2020 | https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/ | primaria (el editor de las reglas), pero es página comercial | 3 | 1 | 1 | 3 | [S] |
| F16 | Documentación de un ERP abierto (envío con proveedor externo) | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.html | primaria sobre sí misma; evidencia de patrón, no norma | 1 | 1 | 2 | 1 | [S] |
| F17 | Documentación de otro ERP abierto (Viaje de entrega) | https://docs.frappe.io/erpnext/user/manual/en/delivery-trip | idem | 1 | 1 | 1 | 1 | [S] |
| F18 | Wikipedia, Milk run | https://en.wikipedia.org/wiki/Milk_run | secundaria | 1 | 1 | 1 | 1 | [S] |

Las figuras de F1 y F2 («removed due to copyright») no están en el texto. Las dos presentaciones son de 2006, material estable pero con ejemplos de EE.UU. Observación práctica: el enlace que OCW rotula como «Transportation IV: Shipper perspective» (lect23) entrega en realidad la presentación de ruteo de vehículos (F2); y la clase 22 (ruteo) figura en la lista sin PDF. Conviene citar F2 por su título interno y no por el rótulo de OCW.

---

## 1. transporte (entrada)

### Qué se afirma

- Quién necesita resolver el transporte: F2 dice que quienes resuelven problemas de ruteo son «Shippers – retailers, distributors, manufacturers», «Carriers – LTL, package» y «Service companies – repair, waste, utility, postal, snow removal». Es la forma más limpia de distinguir cargador (shipper) de transportista (carrier). https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/80e2e998f1048e857b995376b03c8a13_lect23.pdf
- La misma serie de clases tiene dos lados: «Transportation IV: Shipper perspective, strategies and approaches for design and management» y «Transportation VI: Carrier operations and yield management». O sea, el campo ya parte el transporte en la mirada del cargador y la del transportista. https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/pages/lecture-notes/
- Tres capas de red (F1): física («The actual path that the product takes from origin to destination»), operativa («Each arc is a specific mode with costs, distance, etc. Each node is a decision point») y estratégica («A series of paths through the network from origin to destination. Each represents a complete option and has end to end cost, distance, and service characteristics»). La red operativa tiene cuatro componentes: «Loading/Unloading», «Local-Routing (Vehicle Routing)», «Line-Haul», «Sorting». https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/06ab054739b3882c4bda862570c7266b_lect20.pdf
- La decisión de modo/ruta se juzga en términos de la red estratégica. Ejemplo de F1: «Air: 3 days, $??/pair», «All Water Route: 35 days, $0.65/pair», «Land Bridge: 28 days, $0.75/pair» (zapatos de Shenzhen a Kansas City). Es un ejemplo de 2005-2006, útil por la estructura (días y costo por unidad por camino completo), no por las cifras.
- El transporte entra en el costo total del cargador por varias vías: F1 lista «Cost of transportation (Value & Structure)», «Lead Time (Value & Variability & Schedule)», «Capacity (Limits on Q)» y «Miscellaneous Factors». O sea, el transporte no es solo la tarifa: cambia el tamaño de lote, el stock en tránsito y el stock de seguridad. F1 muestra la fórmula TC(Q) = vD + A(D/Q) + rv(Q/2 + kσL) + B_SO (D/Q) Pr[SO] y la regla «Pick mode with smaller TRC» para elegir entre un modo caro y estable (aéreo) y uno barato y variable (ferrocarril). Esto cruza con Inventario y depósitos: nombrarlo y enlazar, no desarrollar.
- Cadena de tiempos con variabilidad (F1, un fabricante de consumo masivo): «Total Lead Time = 56 days», con tramos 15 (12) producción, 2 (2) transporte interno, 2 (1) carga y demora en puerto, 26 (5) océano, 5 (2) descarga y despacho, 6 (3) transporte interno; formato promedio (desvío).
- Intermediarios: un agente de carga (freight forwarder) «co-ordinates and organizes the movement of shipments on behalf of a shipper», normalmente no mueve la carga él mismo, y puede actuar como principal (transportista) o como agente, o ambos. Un NVOCC presta transporte oceánico sin operar los buques y puede emitir su propio conocimiento de embarque (house bill). https://en.wikipedia.org/wiki/Freight_forwarder (secundaria; cita a FIATA y 49 U.S.C. 13102, no leídos).
- Roles en el conocimiento de embarque: cargador (shipper) entrega la carga al transportista y recibe el documento como recibo; consignatario (consignee) es el nombrado o tenedor legítimo con derecho a recibir. Funciones del conocimiento: recibo, evidencia del contrato de transporte, título de propiedad (no el sea waybill, que no es transferible). https://en.wikipedia.org/wiki/Bill_of_lading
- Economías de escala y de distancia: el curso de Caplice las trata como estructura de la función de costo (variable por unidad, fijo por envío, mixto, con mínimo, con descuentos incrementales; F1). No encontré en lo leído la definición explícita de «economía de distancia» (costo por unidad de distancia decreciente porque los costos fijos de carga y descarga se reparten). Esa definición es de Ballou y de Chopra y Meindl, y no la verifiqué: hueco.

### Qué registra un sistema

Según F1, F2, F13, F16, F17 (evidencia de patrón, no norma):
- Partes: cargador, transportista, consignatario, intermediario; con direcciones y condiciones.
- Envío (shipment): origen, destino, bultos o unidades de manejo, peso y volumen, modo, transportista asignado, referencia de seguimiento. F16: en la orden de entrega hay un campo transportista y una referencia de seguimiento.
- Documento de transporte (conocimiento de embarque, carta de porte, guía): cargador, consignatario, transportista, descripción de la carga.
- Estados típicos de seguimiento según F13: salidas, llegadas, despacho aduanero, alertas por demora.
Estados concretos de envío: hueco, no los vi en las fuentes (F17 no documenta estados).

### Recurso canónico
Caplice, F1 completa (32 diapositivas aprox.): fijarse en las tres capas de red, la función de costo de transporte y la tabla de comparación de modos. Complemento sugerido, no leído: Chopra y Meindl, capítulo sobre transporte (cap. 14 en 6.ª ed. según mi memoria, a verificar); Ballou, capítulos de transporte.

---

## 2. modos-de-transporte

### Qué se afirma

- Matriz de comparación de modos de F1 (camión, ferrocarril, aéreo, agua), literal:
  - Costo operativo: camión «Moderate», ferrocarril «Low», aéreo «High», agua «Low».
  - Cobertura: camión «Pt to Pt»; los otros «Terminal to Terminal».
  - Competencia: camión «Many», ferrocarril «Few», aéreo «Moderate», agua «Few».
  - Tipo de tráfico: camión «All Types»; ferrocarril «Low to Mod Value, Mod to High density»; aéreo «High value, Low density»; agua «Low value, High density».
  - Capacidad (toneladas): camión «10 – 25», ferrocarril «50 – 12,000», aéreo «5 – 12», agua «1,000 – 6,000».
  - Velocidad: camión moderada, ferrocarril lenta, aéreo rápida, agua lenta.
  - Disponibilidad: camión alta, ferrocarril moderada, aéreo moderada, agua baja.
  - Consistencia del tiempo de entrega: camión alta, ferrocarril moderada, aéreo moderada, agua baja.
  - Pérdida y daño: camión baja, ferrocarril alta, aéreo baja, agua moderada.
  https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/06ab054739b3882c4bda862570c7266b_lect20.pdf
  La matriz es de 2006 y de contexto estadounidense; las clasificaciones son cualitativas. Faltan ductos y multimodal en esa tabla (F1 menciona ductos como infraestructura privada: «Privately built (rails, pipelines)»).
- Infraestructura (F1): guideway libre (aire, océano, ríos), pública (rutas) o privada (rieles, ductos); terminales públicas (puertos, aeropuertos) o privadas; control público o privado. «The physical network is the primary differentiator between transportation systems in established versus remote locations.»
- Contenedores (F1): «Airtight, Stackable, Lockable»; ISO de 8,5 x 8 pies; TEU (20 pies): volumen 33 m3, carga útil 24,8 t; FEU (40 pies): 67 m3, 28,8 t; doméstico EE.UU. de 53 pies: 111 m3, 20,5 t. Pallets: el de 48 x 40 pulgadas es el más usado en EE.UU. (27 % de todos los pallets); el europalet de 1200 x 800 mm es el estándar europeo.
- TEU según F9: «a measure of containerized cargo capacity equal to one standard 20-foot (6.1 m) long container»; no considera la altura; un 45 pies cuenta como dos TEU, igual que un 40; dos TEU equivalen a un FEU. Alrededor del 90 % de los contenedores son de 20 o 40 pies nominales y los de 40 pies son cerca del 70 % del volumen mundial en TEU. Masa bruta máxima ISO: 36.000 kg (ISO 668:2013, enmienda de 2016). Las dos fuentes difieren levemente en la carga útil porque son de épocas y alcances distintos (F1 2006, F9 con ISO vigente); no hay contradicción de fondo. https://en.wikipedia.org/wiki/Intermodal_container
- FCL frente a LCL: F9 se cortó antes de tratarlos y F1 no los menciona. Hueco: no tengo fuente leída para FCL/LCL.
- FTL frente a LTL (F8): LTL cubre desde un paquete hasta un camión completo; los transportistas de paquetería manejan piezas de menos de unos 150 lb (68 kg); en FTL el transportista suele llevar carga de un solo cargador, que «effectively rents a trailer, typically paying a per-mile rate»; el LTL usa una red radial (terminales locales y hubs que consolidan por región), con tiempos de tránsito más largos; su ventaja es el costo. https://en.wikipedia.org/wiki/Less_than_truckload_shipping Fuente débil (cita a XPO 2023, una página comercial; referencia en https://www.xpo.com/resource-center/ltl/what-is-less-than-truckload/, no leída).
- Intermodal: F10 lo define como un sistema en que «at least two means of transport are used» sin cambiar la unidad de carga. No define multimodal ni transporte combinado; la distinción entre intermodal, multimodal y combinado queda sin fuente leída (hueco). Las ventajas citadas (costos externos por tonelada-km de un tren intermodal cercanos al 28 % de un camión, según Forkenbrock 2001) son de EE.UU.; no las leí en el original (https://www.sciencedirect.com/science/article/pii/S0965856499000610).
- Variantes operativas en F1: sobre camión y rieles aparecen «Trailer on Flat Car (TOFC)» y «Container on Flat Car (COFC) Double Stack»; en el caso de los zapatos, camión 2,5 a 3 días y ferrocarril 5 a 10 días de Nueva York a Kansas City, océano 26 días en promedio.
- Marítimo (contenedor, carga suelta, granel) y ductos: sin fuente leída. Hueco.

### Qué registra un sistema
- Modo y servicio como atributos del envío y de la tarifa (camión, tren, aéreo, marítimo, multimodal); tipo de equipo (contenedor de 20 o 40 pies, semirremolque de 53 pies, pallet).
- Unidad de manejo: pallet, bulto, contenedor, con tipo, peso, volumen. Contenedor con número, tamaño y precinto. Unidad de medida TEU para la capacidad de naves y la facturación.
- Tramos: un envío intermodal es una secuencia de tramos (arcos de la red operativa de F1), cada uno con modo, origen, destino, transportista, tiempo y costo.
- Estados: sin fuente leída para modo concreto (hueco).

### Recurso canónico
F1, de la diapositiva «Mode Comparison Matrix» en adelante, para la comparación; F9 sección Specifications para contenedores. Pendiente de leer: Ballou cap. de modos (tabla de características por modo) y la norma ISO 668 (de pago).

---

## 3. costo-del-flete

### Qué se afirma

- Peso facturable: F7 dice «Dimensional weight is calculated as (length × width × height) / (dimensional factor)» y «The shipping fee is based upon the dimensional weight or the actual weight, whichever is greater». Divisores: aéreo IATA 166 pulg3/lb, cerca de 6.000 cm3/kg («common for IATA shipments», sin cita en la página); mensajería DHL Express 5.000 cm3/kg, FedEx y UPS 139 pulg3/lb (5.000 cm3/kg), algunos servicios de UPS 6.000; USPS 7.000 cm3/kg para Priority Mail nacional. Ejemplo: caja de 10 lb de 18 x 18 x 18 pulg se factura a 36 lb (5.832 / 166 ≈ 35,1, redondeado hacia arriba). https://en.wikipedia.org/wiki/Dimensional_weight Secundaria; los divisores concretos cambian y son de empresas de paquetería, no de carga entre empresas: el divisor lo fija cada transportista o cada tarifa, no hay uno universal. Para carga general terrestre y marítima el divisor típico no aparece en lo leído (hueco).
- Estructuras de tarifa que muestra F1 (como funciones de costo por envío): puramente variable por unidad, puramente fija por envío, mixta (fija más variable), «Variable Cost / Unit with a Minimum» y «Incremental Discounts». Es la manera canónica de modelar una tarifa por escalas. Y el costo de transporte por envío por modo se grafica como «cf + cv + r·v·tm» (costo fijo, variable y costo de tener el stock en tránsito), con la conclusión de que cada modo gana en un rango de tamaño de envío (diapositiva «Transport vs. Inventory Costs»; las curvas no están en el texto extraído, lo leí por la fórmula y los rótulos).
- Tarifas por tabla y por contrato: F1/F2 no las desarrollan; F3 lista «Transportation IV: Shipper perspective» (PDF lect23, que en realidad no trae esto: ver observación arriba) y «Transportation V: Procurement and use of combinatorial auctions» sin PDF. Hueco: no pude leer ni la licitación de fletes ni las subastas combinatorias, ni tarifas por contrato frente a spot.
- Cargo por combustible, recargos: sin fuente leída. Hueco.
- Liquidación y auditoría (freight audit): F12 la define como «the process of examining, adjusting, and verifying freight bills for accuracy» y distingue tres modelos: manual interno, software empaquetado o tercerizado, a menudo con pago por contingencia; auditoría a nivel envío o a nivel factura; la auditoría posterior al pago puede recuperar pagos de más. No da tasas de error ni pasos. Fuente débil (marcada «needs more citations»). https://en.wikipedia.org/wiki/Freight_audit Un sistema TMS cubre «freight audit and payment» según F13, sin más detalle. https://en.wikipedia.org/wiki/Transportation_management_system (la única referencia de F13 es un Magic Quadrant de Gartner de 2021, sobre el tamaño de mercado).
- Quién paga el flete / Incoterms: el ICC dice que las reglas dan «Clear allocation of cost, risk, and obligations», reflejan la práctica «in contracts for the sale and purchase of goods» (B2B), los costos de cada regla se listan juntos en los artículos A9/B9 y la carga (A4) y el despacho de exportación/importación (A7) tienen obligaciones propias. La página no dice qué dejan afuera (propiedad, precio, pago, contrato de transporte): para eso hace falta el texto de las reglas, que es de pago. Hueco. https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/ Sugerencia: solo nombrarlo en la nota y enviar al tema de comercio exterior.
- Precio de un ERP abierto como patrón: el método de envío tiene proveedor, nivel de integración («Get Rate» para estimar o «Create Shipment» para crear etiquetas), margen sobre la tarifa («an additional percentage amount added to the base shipping rate»), envío gratis sobre un monto, seguro como porcentaje; el costo se calcula con el peso total y la distancia entre depósito y cliente. https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.html Es paquetería de comercio electrónico, no carga entre empresas: sirve como evidencia de que la tarifa se arma por peso, distancia y reglas, pero no cubre contratos ni recargos.

### Qué registra un sistema
- Tarifa: transportista, origen y destino (zonas), modo y servicio, unidad de cobro (peso, volumen, pallet, contenedor, km), escalas, mínimo, vigencia, recargos (combustible y otros), moneda. Los atributos salen de las funciones de costo de F1 y de F16; vigencia y recargos son de práctica: sin fuente leída.
- Cálculo del flete: peso real, peso volumétrico, peso facturable (el mayor), divisor aplicado.
- Factura del transportista y liquidación: factura, envíos que cubre, tarifa esperada contra cobrada, diferencia, estado de la auditoría (F12 solo da los niveles envío/factura y los tres modelos).
- Estados de la auditoría y de pago: hueco.

### Recurso canónico
Lo mejor que leí es F1 (funciones de costo y comparación de modos). Para tarifas y licitación, el recurso a leer es la clase «Transportation IV» y «V» de OCW (no accesible en PDF desde mi ruta) y Ballou, capítulo de tarifas y cotización. Para Incoterms, la publicación oficial de ICC (de pago).

---

## 4. consolidacion-y-ruteo

### Qué se afirma

- Origen del problema de ruteo: Dantzig y Ramser (1959), «The Truck Dispatching Problem», Management Science 6(1), 80-91 (Crossref lo cuenta citado 3.925 veces). F6 dice que apareció como «the truck dispatching problem» aplicado a la entrega de nafta. https://doi.org/10.1287/mnsc.6.1.80
- Clarke y Wright (1964), «Scheduling of Vehicles from a Central Depot to a Number of Delivery Points», Operations Research 12(4), 568-581 (2.963 citas en Crossref; autores de la Cooperative Wholesale Society de Manchester y de la Universidad de Manchester). https://doi.org/10.1287/opre.12.4.568 No pude leer el abstract: cualquier descripción del contenido sale de F2, no del original.
- Algoritmo de ahorros (F2): «Serve each node directly»; calcular el ahorro de combinar dos nodos en un mismo recorrido; juntar si el ahorro es positivo. Fórmula literal de F2: «Savings = c0i + cj0 – cij», con ejemplo numérico: S(1,2) = 10 + 15 – 8 = 17; S(1,3) = 6; S(1,4) = –3; S(2,3) = 22; S(2,4) = 16; S(3,4) = 36; capacidad máxima 3; la longitud total baja de 132 a 96 y luego a 74. https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/80e2e998f1048e857b995376b03c8a13_lect23.pdf
- Definición del problema (F2): VRP = «One origin, many destinations, many capacitated vehicles. Find: Lowest cost tours of vehicles to destinations». Es NP-hard (F2, F6). F6: «Because the traveling salesman problem is NP-hard, so is the VRP». Crecimiento combinatorio de F2: elegir y secuenciar una ruta de 10 paradas entre 20 clientes ya da 670.442.572.800 formas.
- Clases de problemas (F2): reparto comercial, recolección comercial, recolección y entrega mixta (LTL y paquetería), citas residenciales, barrido residencial. Variantes académicas (F2, F6): multidepósito (MDVRP), con ventanas horarias (VRPTW), con recolección y entrega (VRPPD), con retornos (VRPB), de inventario (IRP), estocástico y dinámico. «More dimensions» (F2): múltiples dimensiones del pedido (volumen, peso), mezcla de recolección y entrega, ventana horaria, inventario administrado por el proveedor.
- Familias de heurísticas (F2): rutear primero y agrupar después (curva que llena el espacio); agrupar primero y rutear después (barrido, ahorros de Clarke y Wright); óptimo por programación entera con generación de columnas (cada columna es una ruta con su costo; cada fila una parada; una parada debe ser cubierta). Mejora local: 2-opt, 3-opt; metaheurísticas: búsqueda tabú, colonia de hormigas, recocido simulado, algoritmos genéticos.
- Calidad de las heurísticas: F2 da para el viajante «Nearest Neighbor ... In practice 20% above optimal» e inserción «19% / 9% / 16% / 11% above optimal» (más cercano, más lejano, más barato, aleatorio). Sobre VRP, F6: las metaheurísticas recientes pueden llegar «within 0.5% to 1% of optimal on instances with hundreds or thousands of points» (secundaria, sin que yo haya abierto la referencia). Discrepancia a notar: F2 es de 2006 y habla del viajante; F6 es de 2021 y habla de VRP con metaheurísticas. No son comparables punto a punto: dar las dos con su contexto.
- Cuánto ahorra un ruteo: F2 muestra un caso (adaptado de Goentzel 2004): de 10 rutas a 7, «30% savings», y de 2.006 a 1.345 millas, «32% improvement», con la advertencia «Difficult to evaluate quality by inspection». Es un solo caso de un material de curso, sin método publicado en la diapositiva. F6 dice que los proveedores de software de ruteo declaran ahorros de 5 % a 30 %, citando un volumen de Springer de 2007 (no leído); es afirmación de vendedores, así que va marcada como práctica comercial, no como evidencia con método. Hueco: no encontré un estudio empírico independiente de ahorros.
- Reglas prácticas (F2): «Good routes are "rounded", not "star shaped"», «Good routes don't cross themselves or others», «Good sectors are "pie shaped", not "checker board"», «Good solutions "look like a daisy"». Buenas prácticas: «Always use a Preview-Analyze-Review methodology», «Periodically visit the internal logic within the TMS», «Never discount the salty expert who has been doing this longer than you've been alive».
- Límites prácticos (F2): lista de restricciones del mundo real: configuración y horarios de muelles, tipos de trailer y de camión, mamparas móviles, compatibilidad pedido-vehículo, pedido-pedido y vehículo-sitio, clientes preferenciales, preferencias y habilidades de los choferes, tráfico, despacho en tiempo real, carga de combustible y mantenimiento. Interacciones por elemento: camión y trailer, vehículo y cliente, vehículo y pedido (materiales peligrosos, refrigeración), vehículo y chofer, pedido y pedido («lumber & light bulbs, bottled water & dehydrated food»).
- Rutas fijas frente a dinámicas (F2): fijas se repiten en un ciclo, se rediseñan con cambios de cartera (trimestral o anual), se basan en pronóstico y diseñan para los «heavy days»; ventajas: conocimiento del chofer y facilidad de ejecución; desventaja: ineficiencia por variabilidad. Dinámicas cambian a diario según los envíos reales; ventajas: uso de camiones y choferes y flexibilidad; desventajas: difícil de optimizar y de mantener el proceso, y la ejecución puede no coincidir con el plan.
- Niveles de herramienta (F2): planificación manual («Cheap and easy», pero no genera soluciones múltiples ni es fácil de evaluar), GIS interactivo, heurísticas automáticas. La lista sigue (el texto que leí llega hasta heurísticas automáticas; después hay más diapositivas que no revisé a fondo).
- Consolidación: F1 muestra en la red operativa la recolección, el hub con clasificación principal y la distribución, que es el esquema de consolidación del LTL (también F8: «hubs consolidate it by destination region»). Consolidación por tiempo o por destino como política del cargador: sin fuente leída. Recorrido de lechero (milk run): F18 solo dice «In logistics, a milk run is a circular route» y cita a Meusel (1995); fuente mínima, hueco. https://en.wikipedia.org/wiki/Milk_run
- Planificación de cargas (llenado del camión, bin packing, cubicaje): sin fuente leída. Hueco total. F2 solo menciona las dimensiones del pedido (volumen y peso).
- Software: F2 aconseja «Periodically visit the internal logic within the TMS». F13 lista las funciones de planificación de un TMS (optimización de rutas y cargas, simulación de costos, agrupamiento de órdenes), sin cita específica.

### Qué registra un sistema
Según F2, F13, F17:
- Orden o parada: cliente, dirección, mercadería (peso, volumen, otras dimensiones), ventana horaria, tiempo de servicio, compatibilidades y restricciones (peligrosos, refrigeración, muelle).
- Vehículo y chofer: tipo de camión y trailer, capacidad por dimensión, habilidades y licencias, horarios de trabajo y de mantenimiento.
- Ruta o viaje: depósito de salida, secuencia de paradas, vehículo, chofer, hora de salida, hora estimada de llegada por parada, distancia y costo. F17: el viaje de entrega tiene chofer, vehículo, fecha y hora de salida, paradas por cliente, estimación de llegada y optimización de ruta; estados no documentados en esa página.
- Plan: fijo o dinámico, horizonte (diario, semanal), con métricas de utilización.
- Carga planificada: qué va en cada vehículo, en qué orden de descarga: hueco sobre su modelo de datos.

### Recurso canónico
F2 completa para el ruteo (explica el problema, las familias de heurísticas, el algoritmo de ahorros con ejemplo, los límites reales); los dos papers originales (F4, F5) como citas históricas, que no pude abrir. Complemento sugerido, sin leer: Toth y Vigo, The Vehicle Routing Problem (SIAM, 2002) y Golden, Raghavan y Wasil (2008) para el estado del arte; y Chopra y Meindl o Simchi-Levi para consolidación.

---

## 5. Huecos

1. Sin lectura de libros de texto: Ballou, Chopra y Meindl, Simchi-Levi. Quedan sin fuente primaria: economías de escala y distancia (definición), decisiones del cargador (modo, flota propia o contratada, consolidar), características por modo en una tabla de libro, tarifas y recargos.
2. Costo del flete: sin fuente leída sobre tarifas por tabla y por contrato, licitación, recargo de combustible, divisores de peso volumétrico del transporte de carga entre empresas (solo mensajería), auditoría con método (solo F12, débil), clase de carga (NMFC aparece solo nombrada en F8).
3. Modos: sin fuente sobre marítimo (contenedor, suelta, granel), ductos, multimodal frente a intermodal frente a combinado, FCL y LCL.
4. Consolidación: sin fuente sobre consolidación por tiempo o por destino, sobre milk run (solo una definición de una línea), ni sobre planificación de cargas (bin packing).
5. Ahorros del ruteo y calidad de las heurísticas: sin estudio empírico independiente; lo que tengo es un caso de curso (F2), cifras de vendedores y una afirmación de Wikipedia con cita no abierta.
6. Los dos papers originales: solo metadatos; ninguna afirmación sobre su contenido salvo la que viene de F2 y F6.
7. Las clases de MIT sobre perspectiva del cargador, adquisición con subastas combinatorias y operaciones del transportista (y la 22, ruteo): la 22 y la 24 no tienen PDF; la 25 (https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/resources/lect25/) no la abrí; la 21 (https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/resources/lect21/) tampoco.
8. Estados de envío y de viaje en sistemas abiertos: las páginas leídas no los documentan. Habría que abrir el modelo de datos o los estados del documento de entrega.
9. Dos fuentes independientes para lo de plata: las tarifas y el precio no tienen dos fuentes independientes; tiene una sola (F1 para las estructuras de costo). Los Incoterms tienen una sola (ICC).

## 6. Discrepancias con el árbol

- La división propuesta (actores, modos, costo del flete, consolidación y ruteo) sigue razonablemente cómo parte el campo la vertical: el curso de MIT que leí separa conceptos y redes, análisis operativo, ruteo, perspectiva del cargador, adquisición y operación del transportista (F3). Dos ajustes:
  1. El campo trata la compra del transporte (licitación, contratos, subastas) como un bloque propio (Transportation IV y V en F3). Si el costo-del-flete absorbe tarifas, licitación y auditoría, la nota puede quedar demasiado larga; conviene que licitación tenga su subsección o su nota.
  2. La planificación de cargas (llenado del camión) y la consolidación de política (por tiempo o por destino) no son lo mismo que el ruteo: una decide qué carga va junta, la otra el orden de las paradas. El árbol los junta en consolidacion-y-ruteo; con las fuentes que hay, el ruteo está bien cubierto y el llenado no. Si no aparecen fuentes, bajar el llenado a una mención.
- La mirada del transportista (operación, hubs, gestión de ingresos) es otra mitad del campo (F3, «Transportation VI»). El árbol está escrito desde el cargador; está bien para quien construye un ERP o un TMS de cargador, pero hay que decirlo en la entrada.
- Hay que cuidar el borde con el costo del envío de paquetería de la tienda, que ya está en otra nota: F7 y F16 mezclan paquetería y carga entre empresas. Los divisores de 5.000 y 6.000 son de mensajería y aéreo, no de carga completa.
- F2 en OCW está rotulado como «Shipper perspective»; citar por el título del PDF.
