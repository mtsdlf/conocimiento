# Investigación: vertical Red de distribución, segunda ronda

Fecha: 2026-11-27. Cubre solo los huecos declarados en `red-de-distribucion.md`. Se agotó el presupuesto de búsquedas web de la sesión durante esta ronda; lo que sigue se obtuvo abriendo URLs directamente. Lo que no se pudo abrir está en «Huecos».

Escala: A = autoridad, P = profundidad, E = ejemplos, U = unicidad (1 a 3). Marcas: [L] leído completo o la sección completa, [M] metadatos o abstract, [S] resumen secundario o del buscador. Los PDF se bajaron y se extrajo el texto (pdftotext); las citas son literales y los números de diapositiva son los impresos en cada diapositiva.

Aviso sobre las fuentes del MIT: la numeración de la página de apuntes de OCW no coincide con los archivos. La tabla de OCW rotula «17 Supply chain network design», pero el PDF `lect17` es otra cosa (stock de varios artículos y varios escalones, con DRP). El diseño de red y la agrupación por ubicación están en el PDF `lect25`. Se cita por nombre de archivo y número de diapositiva impreso, no por el número de sesión de la tabla. La sesión «26 Risk pooling strategies» figura sin PDF en OCW.

---

## 1. red-de-distribucion (entrada)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Chopra, S., «Designing the Distribution Network in a Supply Chain» (Kellogg, Northwestern; PDF con fecha de creación nov. 2002; es el texto del propio Chopra que antecede al capítulo del libro, con «Figure 4.x» y «Table 4.x» numeradas como capítulo 4 pero sin las tablas en el PDF) | https://transportation.tech.northwestern.edu/docs/research/core-topics/logistics-and-supply-chain-management/Chopra_DistributionSupplyChain.pdf | primaria (autor del libro) | 3/3/3/3 | [L] texto (las figuras y tablas 4.1 a 4.8 no vienen en el PDF: solo se ven sus pies) |
| Chopra y Meindl, Supply Chain Management 5e, diapositivas del editor (Pearson, ©2013), capítulo de diseño de la red de distribución, copia en SlideShare | https://www.slideshare.net/slideshow/supply-chain-management-chap-4/52277239 | primaria (material del editor, copia de terceros) | 2/1/1/1 | [S] (lectura resumida por la herramienta: lista de diseños y de factores, no las tablas) |
| Caplice, ESD.260 Logistics Systems, `lect25` «Transportation Management: Network & Hubs», dic. 2006, MIT CTL | https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/resources/lect25/ (PDF: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/421e474d22fae64f415aea445a34a254_lect25.pdf) | primaria (curso de posgrado) | 3/2/2/3 | [L] |

Qué es cada cosa: el libro (ediciones 3.ª a 7.ª) no se pudo abrir; se leyó el artículo de Chopra que desarrolla el mismo capítulo y las diapositivas del editor de la 5.ª edición solo por resumen. Quien escriba la nota debe citar el artículo como lo que es y no decir que leyó el capítulo.

### Afirmaciones

- Qué es distribución y por qué importa: «Distribution refers to the steps taken to move and store a product from the supplier stage to a customer stage in the supply chain. Distribution is a key driver of the overall profitability of a firm because it directly impacts both the supply chain cost and the customer experience.» (Chopra, sección 0) (URL de Chopra arriba) [L].
- Cómo se evalúa una red: «At the highest level, performance of a distribution network should be evaluated along two dimensions: 1. Customer needs that are met 2. Cost of meeting customer needs» (Chopra, sección 1) [L].
- Seis medidas de servicio que depende de la estructura de la red: «Response time», «Product variety», «Product availability», «Customer experience», «Order visibility», «Returnability». Definiciones del texto: tiempo de respuesta es «the time between when a customer places an order and receives delivery»; disponibilidad es «the probability of having a product in stock when a customer order arrives»; visibilidad es «the ability of the customer to track their order from placement to delivery»; devolubilidad es «the ease with which a customer can return unsatisfactory merchandise and the ability of the network to handle such returns» (Chopra, sección 1) [L]. Las mismas listas, con los mismos seis nombres, aparecen en las diapositivas 4 a 6 de la 5.ª edición (https://www.slideshare.net/slideshow/supply-chain-management-chap-4/52277239) [S].
- Cuatro costos que cambian con el diseño: «Inventories», «Transportation», «Facilities and handling», «Information» (Chopra, sección 1; igual en las diapositivas de la 5.ª edición) [L] y [S].
- Más instalaciones, más respuesta pero más costo: «a decrease in the response time customers desire increases the number of facilities required in the network» (Chopra, Fig. 4.1). Ejemplo del texto: Borders, «about 400 stores», entrega el mismo día; Amazon, «about a week», con «about 5 locations» [L]. Es un ejemplo de 2002, de los dos casos más conocidos del campo; en la nota va como ejemplo fechado.
- Curvas de costo: con más instalaciones sube el inventario («Amazon ... turn its inventory about twelve times a year, while Borders with about 400 facilities achieves only about two turns per year»); el transporte total baja «as long as inbound transportation economies of scale are maintained» y sube si se pierde esa economía; el costo de instalaciones baja al reducir su cantidad; el total «first decrease and then increase». «A firm should add facilities beyond the cost-minimizing point only if managers are confident that the increase in revenues because of better responsiveness is greater than the increase in costs because of the additional facilities.» (Chopra, sección 1, Figs. 4.2 y 4.3) [L].
- Las dos decisiones que definen el diseño: «1. Will product be delivered to the customer location or picked up from a preordained site? 2. Will product flow through an intermediary (or intermediate location)?» (Chopra, sección 2) [L].
- Los seis diseños, con el nombre literal del texto (la lista numerada de Chopra; las diapositivas 5e los nombran igual, con «last-mile» en vez de «last mile» y «customer pickup» en el quinto, y el texto de Chopra tiene la errata «costumer») [L] y [S]:
  1. «Manufacturer storage with direct shipping» (también llamado «drop shipping»: «All inventories are stored at the manufacturer»).
  2. «Manufacturer storage with direct shipping and in-transit merge» («in-transit merge combines pieces of the order coming from different locations so that the customer gets a single delivery»).
  3. «Distributor storage with package carrier delivery».
  4. «Distributor storage with last mile delivery».
  5. «Manufacturer / distributor storage with costumer pickup» (en el cuerpo: «Manufacturer or Distributor Storage with Consumer Pickup»).
  6. «Retail storage with customer pickup».
- Qué dice el texto de cada uno (los dos primeros y el último, que son los más distintos entre sí):
  - Envío directo: la ventaja es centralizar el stock; «The benefits from centralization are highest for high value, low volume items with unpredictable demand. The inventory benefits of aggregation are small for items with predictable demand and low value». Transporte caro por distancia y por perder la consolidación de la salida. Respuesta ejemplificada: eBags, procesar «1-5 days», transporte terrestre «3-11 business days», o sea «4-16 days». Requiere mucha infraestructura de información. Se vuelve difícil «if there are more than 20-30 sourcing locations».
  - Combinación en tránsito: mejor experiencia de cliente que el envío directo porque llega una sola entrega; «no more than four or five sourcing locations».
  - Almacén en el comercio o el mayorista, con transporte por paquetería: «requires a higher level of inventory because the distributor / retailer warehouse aggregates demand uncertainty to a lower level than the manufacturer»; Amazon: «about 12 turns» contra Borders «about 2 turns».
  - Entrega en el domicilio con reparto propio: transporte lo más caro; en grocery, «$30-$40 per home delivery» según el texto de 2002; no se debe dar como cifra vigente.
  - Retiro por el cliente: bajar costo de entrega, pero «Increased processing cost at the pickup site is the biggest hurdle».
  - Retail con retiro: «It is more expensive than all other options to provide a high level of product availability.»
- Combinar diseños es la regla: «Only niche companies will end up using a single distribution network. Most companies are best served by a combination of delivery networks.» Ejemplo de red híbrida: Grainger con stock local para lo rápido y de emergencia, centro nacional para lo medio, y «Very slow moving items are typically drop shipped from the manufacturer» (Chopra, sección 3) [L].
- Cuándo agrega valor un intermediario (distribuidor): hay «many small players at the customer stage, each requiring a small amount of the product at a time». Seis razones que lista el texto, entre ellas menor transporte de entrada por camión completo, menor transporte de salida por combinar productos de varios fabricantes, menor inventario porque el distribuidor «aggregates safety inventory rather than disaggregating at each retailer», y «A more stable order stream from distributor to manufacturer» (Chopra, sección 4) [L].
- Alcance: el texto aclara que habla de fabricante a consumidor final y que «When considering distribution between any other pair of stages ... many of the same options still apply» (sección 2) [L]. Para una nota agnóstica, esto autoriza a presentar los seis diseños como un patrón general, pero hay que decir que se formularon pensando en comercio minorista y electrónico.
- Lo que no se pudo ver: las ocho tablas (4.1 a 4.8) con la calificación de cada diseño en cada dimensión y la tabla de adecuación por tipo de producto. El texto describe en prosa cada comparación, que alcanza para una nota, pero la tabla de ranking (Tabla 4.7) y la de adecuación (Tabla 4.8) no están en el PDF.

### Discrepancias entre las dos fuentes de Chopra

- No hay contradicción de contenido: la lista de seis diseños, las dos decisiones, las seis medidas de servicio y los cuatro costos son los mismos. Hay dos diferencias de forma: el artículo es de 2002 y trae casos de la época (Webvan, Peapod, Gateway), el libro 5e (2013) tiene las diapositivas con otros casos que no se leyeron. Las cifras de ejemplo del artículo (turns, costos de entrega) son de 2001 y 2002 y no son actuales.

### Qué registra un sistema

Evidencia (documentación de sistemas abiertos; ver la sección 5): una red es un conjunto de ubicaciones con tipo y jerarquía, con una relación «se abastece desde» entre ellas, y una forma de mover producto entre ubicaciones con documentos y estados. Los tres diseños que más importan al software (envío directo, entrega por tránsito con cruce de muelle y almacén propio) aparecen como rutas parametrizables en un sistema abierto (ver sección 5). Chopra aporta qué hay que poder decir de un pedido según el diseño: visibilidad del pedido entre dos etapas (comercio y fabricante) y entregas parciales que se rastrean por separado hasta el punto de combinación («Up to the point of merge, the order from each manufacturer is tracked separately. After that the order can be tracked as a single unit.») (Chopra, sección 2.2) [L].

### Recurso canónico propuesto

El artículo de Chopra (URL de arriba): sección 2 completa (los seis diseños y sus comparaciones en prosa) y las secciones 1 y 3. Para la tabla de ranking hay que abrir el libro. Fijarse en las dos decisiones que definen los diseños y en que los diseños se combinan por tipo de producto.

---

## 2. diseno-de-la-red

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Caplice, ESD.260, `lect25`, diapositivas 2 a 11 (diseño de red de distribución) | https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/resources/lect25/ | primaria | 3/2/2/3 | [L] |
| Chopra, artículo de 2002 (sección 1, Figs. 4.1 a 4.3) | https://transportation.tech.northwestern.edu/docs/research/core-topics/logistics-and-supply-chain-management/Chopra_DistributionSupplyChain.pdf | primaria | 3/2/2/2 | [L] |

### Afirmaciones

- Qué es: «Network design is the selection of nodes and links that minimize total cost» (`lect25`, diap. 5) [L]. El problema se plantea con cuatro niveles de nodos (diap. 3 y 4: proveedor «V», planta «P», depósito «W», cliente «C»); cada instalación candidata es un nodo y cada flujo de envío un arco.
- Las tres preguntas del diseño de la red de distribución (`lect25`, diap. 6): «How many DCs should there be?», «Where should the DCs be located?», «For each SKU and each customer: which DC should serve the customer, and which plant should serve the DC?» [L].
- Los cuatro compromisos de costo y servicio (diap. 6): «Transportation Costs (Inbound versus Outbound)», «Facility Costs (Fixed versus Throughput)», «Inventory Costs (Cycle versus Safety Stock)», «Customer Service (Availability versus Order Cycle Time)» [L]. Es el mismo conjunto que Chopra (transporte, instalaciones, inventario, servicio), con la apertura entre fijo y variable y entre stock de ciclo y de seguridad que el artículo no tiene.
- La curva (diap. 7): gráfico de «Freight Cost», «Facility Costs», «Inventory Cost» y «Total Costs» contra «Number of Warehouses» de 0 a 20. Es la misma lógica de las Figs. 4.2 y 4.3 de Chopra. Solo es el dibujo, sin valores numéricos legibles en el texto extraído [L].
- Formulación para un modelo (diap. 8 y 9): minimizar costos de flujo más costos fijos por instalación abierta, sujeto a demanda satisfecha por cliente y producto, mediante programación lineal entera mixta. Tamaño del ejemplo de la diapositiva 8: «20 Plants, 30 Products/ Product Groups, 50 Potential DCs, and 400 Customers Regions» da «12,000,000 possible flows!»; la «better» de la diap. 9 con el flujo separado en entrada y salida da «50,000 (30k IB & 20k OB) possible flows» [L]. Verificación propia: 20×30×50×400 = 12.000.000, igual a la diapositiva; los 50.000 y su composición «30k IB y 20k OB» son lo que dice la diapositiva y no los recalculé.
- Problemas de los datos (diap. 10): «Demand Point Aggregation», «Demand over Time Periods», «Profiling freight cost data», «Fixed Costs: Periodic versus One-Time», «Cost Estimating Functions». Extensiones globales: «Freight Rate Availability», «Transfer Prices and Taxes», «Exchange Rates», «Duty and Duty Drawback». Preguntas que el modelo deja afuera: «What about Inventory?», «What about Customer Service?» [L]. Útil para decir en la nota qué no resuelve un modelo de localización.
- Despliegue de stock como segundo paso (diap. 11): «ICCij = COGi x ICC%ij x SSij» (costo de mantener stock del artículo i en el depósito j = costo de lo vendido × porcentaje de costo de mantener × stock de seguridad). Esto es, en cuentas, el vínculo entre el diseño de red y la decisión de stock de cada ubicación [L].
- Redes de transporte (diap. 12 a 27): directo contra concentrador. «Hub consolidation reduces costs», «Consolidation increases conveyance utilization», «Transportation has a fixed (per conveyance) cost». Desventajas (diap. 18): «Cost of operating the hub», «Circuity», «Impact on service levels», «Added time in-transit». Ejemplo de servicio estratégico (diap. 27): «Central Hub: 3 days, $100», «West/East Hub: 2 days, $120», «Direct: 1 day, $200» [L]. Esto cae en el tema de transporte, pero explica por qué el diseño de la red de distribución y el de la red de transporte se deciden juntos.
- Estratégico, táctico y operativo (diap. 2): «Strategic – longer scope and less data available (yr+)», «Tactical – shorter scope w/ planning data (week to yr)», «Operational – very short scope real data (daily)» [L]. Responde la pregunta de cada cuánto se revisa: la red es de plazo de año o más.
- Centro de gravedad y modelos de localización continuos: no aparecen en `lect25` (el texto extraído no contiene «center of gravity»). Siguen sin fuente (ver Huecos).
- Posponer (postponement): aparece en Chopra solo como ventaja del envío directo y del almacén («postponing customization until after the customer order has been placed»; Dell) (artículo de Chopra, sección 2.1) [L]. No hay un tratamiento propio en estas fuentes.

### Qué registra un sistema

Para un modelo de diseño de red según `lect25`: instalaciones candidatas (con costo fijo por instalación), flujos con costo por unidad entre cada par de nodos, demanda por zona de cliente y por producto o grupo, y el resultado (qué instalaciones abre y qué zona atiende cada una). Esto no es un registro operativo sino un escenario de planificación. En el lado operativo, ver sección 5.

### Recurso canónico propuesto

`lect25`, diapositivas 2 a 11, del curso ESD.260: las tres preguntas del diseño, los cuatro compromisos y los problemas de datos. Complemento: Chopra, sección 1, para las curvas y su interpretación en prosa.

---

## 3. centralizacion-del-stock

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Caplice, ESD.260, `lect25`, diapositivas 28 a 33 («Location Pooling» y «Lead Time Pooling») | https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/resources/lect25/ | primaria | 3/2/3/3 | [L] |
| Chopra, artículo de 2002, secciones 2.1 y 4 | https://transportation.tech.northwestern.edu/docs/research/core-topics/logistics-and-supply-chain-management/Chopra_DistributionSupplyChain.pdf | primaria | 3/2/2/2 | [L] |

Las demás fuentes de la vertical (Eppen 1979, Maister 1976, Oeser y Romano 2016, Bimpikis y Markakis 2016) siguen como en el informe anterior; no se reabrieron.

### Afirmaciones

- Ejemplo numérico de una fuente (Caplice, `lect25`, diap. 28): «Region has 3 sales/delivery teams», «Each team has its own inventory site», «Daily demand ~N(15, 4) within each territory», «Lead time to each territory site = 2 days», «Cycle service level set at 99.9%». Pregunta de la diapositiva: «How much safety stock should be in each territory? What if they pool to a common site?» [L].
- Resultado (diap. 29): «Note declining marginal benefit of pooling. Going from 1 to 3 – reduced SS by 42%. Going from 7 to 9 – reduced SS by 12%». El gráfico traza «Days of Supply» contra «Number of Stocking Points» de 1 a 10 [L]. Las cifras de la diapositiva coinciden con la ley de la raíz cuadrada. Verificación propia (no es de la fuente): 1 − 1/√3 = 42,3 % y 1 − √7/√9 = 11,8 %.
- Cuentas propias a partir del caso de la diapositiva 28, marcadas como ilustración y no atribuibles a la fuente, que no publica los valores (aquí se asume que el segundo parámetro de N(15, 4) es el desvío): z del 99,9 % = 3,09; stock de seguridad de cada sitio = 3,09 × 4 × √2 ≈ 17,5 unidades; con tres sitios separados ≈ 52,4; con un sitio común, 3,09 × 4 × √6 ≈ 30,3. La reducción es 1 − 30,3/52,4 ≈ 42 %, igual a la de la diapositiva. Si el 4 fuera la varianza, la reducción relativa es la misma, pero los valores absolutos cambian.
- La diapositiva 30 muestra el costo de la agrupación: el stock de ciclo. Con n sitios separados, cada uno pide «qi* = √(2 A Di / v r) = √(2 A D / (v r n))» y el costo total de reposición es «TRC* = √(2 n D A v r)», o sea, √n veces el del sitio común: la lógica de la raíz cuadrada va en sentido contrario para el stock de ciclo (se paga más pedidos fijos cuando se separa). Pregunta abierta de la diapositiva: «Impact on replenishment to the DC location. Other impacts?» [L].
- Agrupar en el tiempo de reposición (diap. 31 a 33, «Lead Time Pooling», adaptado de Cachon y Terwiesch 2005): tres incertidumbres, «Total demand uncertainty», «Allocation demand uncertainty», «Product mix uncertainty». «Consolidated Distribution: Keep inventory near customers; Hedge against allocation uncertainty». Caso: un proveedor que envía directo a 100 tiendas, plazo de reposición de 4 semanas, revisión cada 4 semanas, «Weekly demand in each store is iid ~N(75, 20)», «IFR = 99.5%»; propuesta con un centro de distribución regional, 4 semanas del proveedor al centro y 1 semana del centro a las tiendas. La diapositiva no da el resultado; plantea «What is the safety stock on hand in the system?» y «Who owns the pipeline inventory?» [L]. No hay solución numérica en la fuente.
- Por qué centralizar según Chopra: «The biggest advantage of drop shipping is the ability to centralize inventories at the manufacturer. A manufacturer can aggregate demand and provide a high level of product availability with lower levels of inventory than individual retailers.» y «The inventory benefits of aggregation are small for items with predictable demand and low value» (sección 2.1). Y el intermediario «aggregates safety inventory rather than disaggregating at each retailer» (sección 4) [L]. Chopra no da la fórmula ni la ley de la raíz cuadrada con nombre.
- Lo que se pierde al centralizar: según Chopra, tiempo de respuesta («Response times tend to be large when drop shipping is used ... shipping distances are on average longer from the manufacturer's centralized site») y transporte de salida más caro («Transportation costs are high with drop shipping because the average outbound distance to the end consumer is large and package carriers must be used») (sección 2.1) [L]. Esto cubre el hueco «lo que se pierde (plazo, costo de transporte)» del informe anterior.
- Evers y Beier: no se reintentó (sin presupuesto de búsqueda). Sigue como hueco.
- Fuentes del mismo documento: `lect17` (diap. 11) agrega para varios escalones que, con control descentralizado y lógica de lote y punto de pedido, se «Create and amplify "lumpy" demand» y se llega a «mal-distribution of available stock, hoarding of stock, and unnecessary stock outs» [L]. Va en Inventario y depósitos en lo que toca al punto de pedido; acá solo sirve de motivo para planificar la reposición entre escalones (DRP, otra vertical).

### Qué registra un sistema

La agrupación no es un objeto: es una consecuencia de la relación «qué ubicación abastece a cuál». Lo que sí se registra, según el ejemplo de Caplice: por ubicación, el parámetro de demanda (media y desvío) y el plazo de reposición, de los que sale el stock de seguridad; si se cambia la relación de abastecimiento hay que recalcular. Detalle del stock de seguridad: Inventario y depósitos.

### Recurso canónico propuesto

`lect25`, diapositivas 28 a 30, para el ejemplo con números, y la 29 en especial para el rendimiento decreciente (1→3 baja 42 %, 7→9 baja 12 %). Chopra, sección 2.1, para cuándo no conviene (demanda predecible y de poco valor).

---

## 4. tercerizacion-logistica

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| CSCMP, «Supply Chain Management Terms and Glossary», actualizado agosto de 2013 (222 páginas), copia archivada en arquivo.pt de la captura del 22 de mayo de 2016; la URL original de cscmp.org ya no da el PDF | https://arquivo.pt/wayback/20160522172303id_/http://cscmp.org/sites/default/files/user_uploads/resources/downloads/glossary-2013.pdf | primaria (glosario del cuerpo profesional) | 3/2/1/3 | [L] de las entradas citadas |
| Aurora University, «Supply Chain Management (SCM): 3PL vs 4PL» | https://online.aurora.edu/supply-chain-management-scm-3pl-vs-4pl/ | secundaria | 1/1/1/1 | [S] (cita al glosario de CSCMP; nada nuevo, no cuenta como fuente aparte) |
| Wikipedia, «Fourth-party logistics» (atribuye el término a Andersen Consulting, hoy Accenture, sin fecha) | https://en.wikipedia.org/wiki/Fourth-party_logistics | secundaria | 1/1/1/1 | [S] |

### Afirmaciones

- 3PL, según CSCMP (glosario de 2013): «Outsourcing all or much of a company's logistics operations to a specialized company. The term "3PL" was first used in the early 1970s to identify intermodal marketing companies (IMCs) in transportation contracts. Up to that point, contracts for transportation had featured only two parties, the shipper and the carrier. When IMCs entered the picture—as intermediaries that accepted shipments from the shippers and tendered them to the rail carriers—they became the third party to the contract, the 3PL. Definition has broadened to the point where these days, every company that offers some kind of logistics service for hire calls itself a 3PL.» (entrada «Third-Party Logistics (3PL)») [L]. Esta entrada es también el origen de los números: primera parte es el cargador, segunda el transportista, tercera el intermediario.
- La entrada «Third-Party Logistics Provider» del mismo glosario: «A firm which provides multiple logistics services for use by customers. Preferably, these services are integrated, or "bundled" together by the provider.» y «Among the services which they provide are transportation, warehousing, cross-docking, inventory management, packaging, and freight forwarding.» [L].
- Dato legal en la misma entrada, de Estados Unidos: en 2008 una ley declaró que la definición legal de 3PL es «A person who solely receives, holds, or otherwise transports a consumer product in the ordinary course of business but who does not take title to the product.» (CSCMP, glosario 2013) [L]. No es un dato general; la nota no debería usarlo salvo como ejemplo de que la definición legal difiere de la comercial. El glosario no da la norma ni su número; sin verificar.
- 4PL, según CSCMP: «Differs from third party logistics in the following ways; 1) 4PL organization is often a separate entity established as a joint venture or long-term contract between a primary client and one or more partners; 2) 4PL organization acts as a single interface between the client and multiple logistics service providers; 3) All aspects (ideally) of the client's supply chain are managed by the 4PL organization; and, 4) It is possible for a major third-party logistics provider to form a 4PL organization within its existing structure.» (entrada «Fourth-Party Logistics (4PL)») [L].
- Origen de la sigla 4PL, en la misma entrada: «The term was registered by Accenture as a trademark in 1996 and defined as "A supply chain integrator that assembles and manages the resources, capabilities, and technology of its own organization with those of complementary service providers to deliver a comprehensive supply chain solution.", but is no longer registered.» [L]. Wikipedia dice que lo definió «Andersen Consulting (now Accenture)», sin fecha; se apoya en lo mismo, no cuenta como fuente independiente. La definición original de Accenture se lee citada dentro del glosario de CSCMP, no en un documento de Accenture (sin abrir).
- Socio logístico líder: «Lead Logistics Partner (LLP): An organization that organizes other 3rd party logistics partners for outsourcing of logistics functions. An LLP serves as the client's primary supply chain management provider, defining processes and managing the provision and integration of logistics services through its own organization and those of its subcontractors.» (glosario CSCMP, remite a 4PL) [L]. La entrada de 4PL remite a «Lead Logistics Provider», pero la entrada que existe en esa edición se llama «Lead Logistics Partner».
- 2PL: el glosario de CSCMP 2013 no tiene entrada de «second-party logistics» ni de «1PL» (se buscó por «second-party», «2PL», «first-party»; solo hay la mención histórica de que antes del 3PL «contracts for transportation had featured only two parties, the shipper and the carrier»). Es decir, que 1PL y 2PL no son categorías definidas por CSCMP: son una convención de uso. La nota debería decirlo así y no inventar definición. No se encontró fuente con autoridad que las defina (hueco).
- Qué se terceriza, esquema de cobro, acuerdos de nivel de servicio, qué datos se intercambian: siguen sin fuente. Solo la lista de servicios del 3PL (transporte, almacenaje, cruce de muelle, administración de inventario, embalaje, agente de carga) de CSCMP.
- Dropship como forma de tercerizar el almacenaje: «Drop Ship: A customer fulfillment strategy where products are shipped directly from the manufacturer or distributor to a customer bypassing the retail or secondary distribution location. Intended to expedite delivery and reduce handling costs. Billing transactions occur in the normal manner, only the material flow is altered.» (glosario CSCMP) [L]. Sirve de definición del primer diseño de Chopra.

### Qué registra un sistema

Según la lista de servicios de CSCMP, un operador es una parte con varios servicios y, según la definición de 4PL, puede ser una sola interfaz sobre varios operadores. Sin documentación de sistemas consultada específicamente para el operador y su contrato (hueco). En los sistemas abiertos revisados (sección 5) el envío directo sí está modelado, con el proveedor como origen y el cliente como destino del mismo documento.

### Recurso canónico propuesto

El glosario de CSCMP (edición 2013, entradas «Third-Party Logistics (3PL)», «Fourth-Party Logistics (4PL)», «Lead Logistics Partner»): fijarse en el origen histórico del «tercero» y en que 2PL no está definido. Hay una edición más nueva en cscmp.org que no se pudo abrir (la URL de 2013 ya no responde); si la hay, conviene citar la vigente.

---

## 5. Qué registra un sistema: evidencia de sistemas abiertos (para toda la vertical)

Se usa como prueba de que un patrón es común, no como norma. En la nota no se nombran los productos.

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| Odoo 18.0, «Resupply warehouses» (reabastecer un depósito desde otro) | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/resupply_warehouses.html | primaria (documentación oficial) | 3/2/2/2 | [S] (leída vía la herramienta de resumen) |
| Odoo 18.0, «Dropshipping» | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping.html | primaria | 3/2/2/2 | [S] |
| Odoo 18.0, «Cross-docking» | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/cross_dock.html | primaria | 3/2/2/2 | [S] |
| Odoo 18.0, recepciones y entregas en dos pasos | https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps.html | primaria | 3/1/1/2 | [S] |
| ERPNext (documentación de Frappe), «Stock Entry» | https://docs.frappe.io/erpnext/user/manual/en/stock-entry | primaria | 3/2/2/2 | [S] |
| Apache OFBiz, modelo de datos del producto (`product-entitymodel.xml`) y datos semilla de estados (`ProductSeedData.xml`), rama principal | https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/entitydef/product-entitymodel.xml y https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/data/seed/ProductSeedData.xml | primaria (código fuente del modelo) | 3/3/1/3 | [L] de las entidades citadas |

Todos son documentación o código de productos concretos: tres productos, tres criterios distintos. Que coincidan en los objetos es el dato; la forma exacta de cada uno no.

### Lo que muestran

- Ubicación con tipo y jerarquía (OFBiz): la entidad `Facility` tiene `facilityId`, `facilityTypeId`, `parentFacilityId`, `ownerPartyId`, `facilityName`, `facilitySize`, `defaultDaysToShip`, `openedDate`, `closedDate`, `geoPointId`, `facilityLevel`; `defaultDaysToShip` se describe como «In the absence of a product specific days to ship in ProductFacility, this will be used». El tipo es una entidad aparte con jerarquía (`FacilityType.parentTypeId`), y los tipos semilla incluyen `WAREHOUSE`, `RETAIL_STORE`, `PLANT`, `OFFICE`, `CALL_CENTER`, `BUILDING`, `FLOOR`, `ROOM` (las instalaciones de la red y las de adentro del depósito viven en la misma tabla; `FacilityLocation` baja a pasillo, sección, nivel y posición) [L]. Hay también `FacilityGroup`, con jerarquía, para agrupar instalaciones.
- Parámetros por producto y ubicación (OFBiz): `ProductFacility` guarda, para cada par producto y ubicación, `minimumStock`, `reorderQuantity`, `daysToShip`, `replenishMethodEnumId` y `requirementMethodEnumId`: es decir, quién y cómo repone cada ubicación se define por par [L].
- Transferencia entre ubicaciones (OFBiz): `InventoryTransfer` tiene `inventoryTransferId`, `statusId`, `inventoryItemId`, `facilityId` (origen), `locationSeqId`, `facilityIdTo` (destino), `locationSeqIdTo`, `containerId`, `sendDate`, `receiveDate`, `comments`. Estados semilla del tipo `INVENTORY_XFER_STTS`: «Requested» (01), «Scheduled» (02), «En-Route» (03), «Complete» (04), «Cancelled» (99), con transiciones permitidas declaradas (de Solicitada se puede ir a Programada, En camino, Completa o Cancelada) [L]. Esto es evidencia de que una transferencia entre depósitos tiene origen, destino, fecha de envío, fecha de recepción y un ciclo de vida de cinco estados.
- Reabastecer un depósito desde otro (Odoo): cada depósito tiene un campo «Resupply From» con los depósitos que lo pueden abastecer; eso genera una ruta «X: Supply Product from Y» que se tilda por producto; se dispara con una regla de reabastecimiento (ubicación, ruta, cantidad mínima y máxima), con un pedido manual de reponer, o con una venta; el sistema crea una orden de entrega en el depósito de origen y una recepción en el de destino, y el stock en camino queda en una ubicación de tránsito entre depósitos («Physical Locations/Inter-warehouse transit»). La página no define estados de esas transferencias [S].
- Cruce de muelle (Odoo): con recepciones y entregas de dos pasos, la ruta de cruce de muelle crea «two linked transfers»: de la ubicación de entrada a la de salida (el cruce) y de la de salida al cliente; ambas empiezan en el estado «Waiting Another Operation» mientras el producto no se compró; al recibir se valida la interna y luego la entrega [S].
- Envío directo (Odoo): una venta de un producto con la ruta de envío directo habilitada «An associated request for quotation (RfQ) is automatically generated»; al confirmarla se crea «A dropship receipt» con origen en proveedores y destino en clientes; se valida cuando el proveedor entrega [S]. Es el diseño 1 de Chopra como flujo: un pedido de venta, un pedido de compra y un solo movimiento de producto del proveedor al cliente.
- Pasos de recepción y de entrega (Odoo): por depósito, «Incoming Shipments» y «Outgoing Shipments» pueden ser de uno o dos pasos (y tres para entregas, según la nota de la página); las ubicaciones de entrada y de salida se crean solas al elegir dos pasos [S]. Es de adentro del depósito; va en Inventario y depósitos.
- Tránsito entre ubicaciones (ERPNext): el movimiento entre depósitos es un «Stock Entry» con finalidad «Material Transfer»; hay «Source Warehouse» y «Target Warehouse»; «Add to Transit» lo parte en dos movimientos con un depósito de tipo «Transit» en el medio, que se cierra con «End Transit» [S]. Misma idea que Odoo (ubicación de tránsito), pero con dos documentos en vez de uno con estados.

### Qué dice esto para la nota

- El patrón común: ubicación con tipo y jerarquía, relación de abastecimiento entre ubicaciones, documento de transferencia con origen y destino, y una ubicación o estado de tránsito entre el envío y la recepción. Los tres productos coinciden en eso; difieren en si el tránsito es un estado del documento (OFBiz: «En-Route»), una ubicación (Odoo, ERPNext) o dos documentos (ERPNext con «Add to Transit»).
- Los parámetros de reposición por ubicación y producto (OFBiz `ProductFacility`; Odoo reglas de reabastecimiento con mínimo y máximo) son de Inventario y depósitos; acá solo se dice que la regla de «de dónde se repone» es lo que define la red.
- Nada de esto es la planificación (DRP) ni el pronóstico: los tres modelan la ejecución. Quien construya software de planificación tiene que traer la red como dato propio, no esperar que la ejecución la traiga.

---

## DRP (nota sobre el límite del tema, para quien escriba otra vertical)

No se pidió, pero salió de leer `lect17` y entra en este tema: Caplice (`lect17`, diap. 13 y 14) define: «DRP is simply the application of the MRP principles and techniques to distribution inventories» (atribuida a Andre Martin), con premisas «Layers of inventory create "lumpy" demand» y «Information replaces inventory», entradas «Base Level Usage Forecasts», «Distribution Network Design», «Inventory Status», «Ordering Data», y pasos «Requirements Implosion», «Net from Gross Requirements», «Requirements Time Phasing», «Planned Order Release» [L]. Ejemplo numérico completo de un plan de tres almacenes regionales y uno central en las diap. 15 a 21 (por ejemplo el almacén regional uno con «Q=50, SS=15, LT=1», uso por período 25, requerimiento bruto 40, recepciones planificadas de 50 en períodos alternos) [L]. Límites que la propia fuente da (diap. 22): «DRP does not determine lot size or safety stock», «DRP does not explicitly consider any costs» [L]. Definición de CSCMP: «Distribution Requirements Planning (DRP): A system of determining demands for inventory at distribution centers and consolidating demand information in reverse as input to the production and materials system.» (glosario 2013) [L]. Dos fuentes independientes (MIT y CSCMP) coinciden en la idea, con una diferencia: CSCMP lo describe como entrada del sistema de producción, MIT lo presenta como análogo a MRP aplicado a la distribución.

---

## Huecos

1. Chopra y Meindl, el libro: no se abrió ninguna edición. Lo leído es el artículo de Chopra de 2002 (mismo marco, seis diseños y mismos factores) y un resumen de las diapositivas de la 5.ª edición. Faltan las ocho tablas (4.1 a 4.8), en particular el ranking de los seis diseños por dimensión y la tabla de qué diseño conviene según tipo de producto.
2. MIT ESD.260: no hay PDF de la sesión «Risk pooling strategies» (OCW la lista sin archivo). La agrupación por ubicación y por plazo está en `lect25` y se leyó. El texto de OCW sobre «network design» está en `lect25` diap. 2 a 11 y no en el archivo `lect17` que le corresponde por el número de la tabla. No se leyeron `lect2`, `lect16` ni `lect20` en detalle (el de transporte fundamental, `lect20`, no se citó).
3. Ley de la raíz cuadrada con nombre y fórmula de una fuente: el ejemplo de Caplice da el caso y los porcentajes (42 % y 12 %), pero no escribe la fórmula ni los valores absolutos; los valores absolutos de este informe son cuenta propia. Eppen (1979) y Maister (1976): sin reabrir.
4. Evers y Beier: no se reintentó.
5. Centro de gravedad y modelos de localización continuos: sin fuente (no están en `lect25`).
6. 2PL y 1PL: no hay definición con autoridad; el glosario de CSCMP 2013 no las tiene. Falta el diccionario de ASCM (la página no entregó contenido) y un libro de texto.
7. 4PL de Accenture: solo la cita que hace CSCMP; no se abrió un documento de Accenture.
8. La edición vigente del glosario de CSCMP: no se abrió (la URL de 2013 en el sitio del cuerpo ya no responde y se usó la copia archivada).
9. Tercerización: esquemas de cobro, acuerdos de nivel de servicio y datos a intercambiar con el operador: sin fuente. Los informes de 3PL del informe anterior siguen sin abrirse.
10. Documentación de sistemas: las páginas de Odoo y ERPNext se leyeron por resumen [S], no completas; no se consultaron las reglas de reabastecimiento con detalle, ni la ruta «multi-step» de tres pasos de Odoo (las URL probadas dieron 404 o la página no la describe), ni nada de OFBiz fuera del modelo de datos y los estados semilla. Los estados de Odoo y de ERPNext para las transferencias entre depósitos no se obtuvieron (la página de Odoo dice que no los define).
11. Costo logístico por sector y datos de Argentina o la región: sin cambios.

## Discrepancias con el árbol

- Las dos listas de Chopra (seis diseños y dos decisiones) son un contenido propio y grande de la entrada de la vertical. Propuesta: que la nota de entrada (`red-de-distribucion`) lleve las dos decisiones, los seis diseños, las seis medidas de servicio y los cuatro costos, y que `diseno-de-la-red` lleve las tres preguntas de `lect25` (cuántos, dónde, a quién sirve cada uno), la curva y el modelo. Hoy las dos se solapan en la curva de costo total.
- La centralización del stock es, en Chopra, un argumento a favor de dos diseños (envío directo y almacén central), no un tema separado. En Caplice es una sección corta dentro del diseño (diapositivas 28 a 33, con el diseño en las 2 a 11 del mismo archivo). Confirma lo que ya proponía el informe anterior: nota propia por la discusión de supuestos, enlazada desde el diseño; si hay que reducir, fundirla.
- La tercerización (2PL, 3PL, 4PL) en CSCMP es de definiciones y de historia, y tiene poca relación con el diseño de red; el vínculo con la red es el envío directo y el cruce de muelle como servicios que se contratan. Se queda en esta vertical, pero conviene que la nota diga que 1PL y 2PL no son categorías con definición oficial.
- El campo no separa «red de distribución» de la red de transporte: Caplice trata el diseño de depósitos y el de concentradores de transporte en el mismo archivo (`lect25`). El árbol los separa entre esta vertical y transporte; la frontera es discutible, y la nota debería enlazar a transporte para concentradores.
