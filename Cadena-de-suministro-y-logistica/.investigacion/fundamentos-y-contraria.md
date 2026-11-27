# Fundamentos y posición contraria: Cadena de suministro y logística

Ángulo: historia, marcos, escuelas y debates, evidencia en contra, dónde se produce el saber, glosario.

## Advertencia de método (leer primero)

- El presupuesto de WebSearch de la sesión se agotó después de una sola búsqueda. El resto salió de WebFetch sobre páginas puntuales. Varias fuentes primarias dieron 403 o 404 (repositorio de Penn, ScienceDirect, HBR sin texto, ASCM sin contenido).
- Por eso casi todo lo verificado viene de Wikipedia (secundaria, puntaje bajo en autoridad) o del texto libre de FPP3. Lo que figura como "memoria" es conocimiento del redactor, sin URL abierta en esta sesión: hay que verificarlo antes de escribirlo en la nota. No lo traten como confirmado.
- Marcas: [L] leído completo o sección completa; [M] metadatos o abstract; [S] resumen secundario o del buscador; [Mem] de memoria, sin verificar.
- Puntajes (1 a 3): A autoridad, P profundidad, E ejemplos, U unicidad.

## 1. Historia

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| https://en.wikipedia.org/wiki/Supply_chain_management | secundaria | 1/2/2/1 | [S] (primeros 100.000 de 257.623 caracteres) |
| https://en.wikipedia.org/wiki/Ideal_X | secundaria | 1/1/2/1 | [S] |
| https://en.wikipedia.org/wiki/Intermodal_container | secundaria | 1/2/2/1 | [S] (primeros 100.000 de 186.006) |
| https://en.wikipedia.org/wiki/Sales_and_operations_planning | secundaria | 1/2/1/1 | [S] |
| Oliver y Webber (1982), "Supply-chain management: logistics catches up with strategy", Outlook, Booz Allen Hamilton | primaria | 3/3/2/3 | [Mem], no localizada |
| Levinson, *The Box* (2006, Princeton UP) | primaria (libro) | 3/3/3/3 | [Mem] |

### Afirmaciones

- El término. Wikipedia atribuye a Keith Oliver, consultor de Booz Allen Hamilton, haberlo llevado al dominio público en 1982: Oliver "introduced the term 'supply chain management' to the public domain in an interview for the Financial Times." Esa página no menciona a Webber. La atribución "Oliver y Webber 1982" del brief es el artículo de Outlook, que no pude abrir. Hay que verificarlo contra el original antes de citar a Webber. https://en.wikipedia.org/wiki/Supply_chain_management
- Popularización: Handfield y Nichols (1999), *Introduction to Supply Chain Management*, "the seminal book that helped make the term widely adopted" (paráfrasis de Wikipedia); el término se generaliza a mediados de los noventa. https://en.wikipedia.org/wiki/Supply_chain_management
- Antes del término: la página lista la línea de montaje (principios del siglo XX), el EDI (años sesenta) y la especialización en los ochenta (corredores de transporte, gestión de depósitos, transportistas sin activos). https://en.wikipedia.org/wiki/Supply_chain_management
- Contenedor: el Ideal X, un petrolero T2 convertido, zarpó el 26 de abril de 1956 de Port Newark a Houston con 58 contenedores. https://en.wikipedia.org/wiki/Ideal_X . McLean compró Pan-Atlantic Steamship en 1955 (luego Sea-Land); "ISO standards for containers were published between 1968 and 1970" (la página dice que las publicó la "International Maritime Organization", lo cual es un error aparente: es ISO). Los primeros estándares internacionales vinieron del Bureau International des Containers en 1933 y 1935. https://en.wikipedia.org/wiki/Intermodal_container
- Discrepancia: la página del contenedor da 1956 como "widespread use around 1956" y no fecha el Ideal X; la página de Ideal X sí da el 26/4/1956. Se usa la segunda.
- S&OP: "The term and modern meaning are 'generally attributed to Richard Ling,' then a consultant at Oliver Wight, in the 1980s." Empezó con la planificación agregada de producción de los años cincuenta, pasó a MRP II hacia 1985 y tomó su sentido actual. Proceso táctico de hasta 18 meses, típicamente mensual. https://en.wikipedia.org/wiki/Sales_and_operations_planning . Es un solo resumen secundario; falta fuente primaria (Wallace, Stahl, *Sales and Operations Planning*; Oliver Wight).
- MRP y DRP (años sesenta y setenta; Orlicky 1975; DRP en Martin, *Distribution Resource Planning*, 1983): [Mem], sin fuente abierta. Es hueco.
- Logística militar y distribución física (Jomini; Heskett, Glaskowsky e Ivie, *Business Logistics*, 1964; la National Council of Physical Distribution Management, hoy CSCMP): [Mem], hueco.
- Forrester: la página del efecto látigo lo ubica en *Industrial Dynamics* (1961). El brief dice 1958 (artículo de Harvard Business Review, "Industrial Dynamics: A Major Breakthrough for Decision Makers"). Las dos fechas son verdaderas para dos textos distintos: el artículo de HBR es de 1958 [Mem] y el libro de 1961. https://en.wikipedia.org/wiki/Bullwhip_effect
- SCOR: "developed in 1996 by the consulting firm PRTM (now part of PwC) and AMR Research (now part of Gartner)"; el Supply Chain Council lo respaldó y hoy es parte de ASCM. https://en.wikipedia.org/wiki/Supply-chain_operations_reference
- Crisis 2020 a 2022 y resiliencia: ver sección 3.3.

### Qué registra un sistema (historia)

Nada directo. Sí conviene que la nota diga qué dejó cada hito en los sistemas: el contenedor dejó el identificador de unidad de carga (código y tipo ISO), el EDI dejó los mensajes entre empresas, MRP y DRP dejaron la explosión de necesidades por nivel y por tiempo.

### Recurso canónico

Levinson, *The Box*, caps. 1 a 3 y 9, para la historia del contenedor. Para el origen del término, el artículo de Oliver y Webber (1982), que conviene conseguir. Hueco: no pude leer ninguno.

## 2. Marcos

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| https://en.wikipedia.org/wiki/Supply-chain_operations_reference | secundaria | 1/2/1/1 | [S] |
| ASCM, SCOR Digital Standard (ascm.org/corporate-transformation/standards-tools/scor-ds/) | primaria | 3/3/2/3 | no leída: la página devolvió contenido vacío |
| APQC PCF 7.4 (PDF del brief) | primaria | 3/3/2/3 | no abierta |
| ASCM, programas CSCP, CLTD, CPIM | primaria | 3/1/1/3 | no abierta |

### Afirmaciones

- Procesos de SCOR DS (versión 2022 según Wikipedia): Plan, Source, Transform ("expanded from Make"), Order y Fulfill (partición del antiguo Deliver), Return y Orchestrate (nuevo; "strategy, business rules, technology, and human resources"). La versión 12.0 usaba Plan, Source, Make, Deliver, Return y Enable. https://en.wikipedia.org/wiki/Supply-chain_operations_reference . Coincide con los siete procesos del brief.
- Métricas de nivel 1: Wikipedia solo dice que son los cálculos que miden el posicionamiento deseado y no las nombra. Los cinco atributos del brief (confiabilidad, capacidad de respuesta, agilidad, costo, activos) son [Mem] y deben verificarse contra el estándar de ASCM. Una pregunta abierta: en el SCOR 12 eran Reliability, Responsiveness, Agility, Costs y Asset Management Efficiency; en el DS pueden figurar con otros nombres.
- Qué cae en este tema según los límites: Plan (pronóstico y S&OP), Order (captación y gestión del pedido hasta la salida), Fulfill (de la puerta del depósito en adelante, el transporte y la entrega) y Return (devolución en la red); la parte de Fulfill que es de adentro del depósito va a Inventario y depósitos; Source es de Compras; Transform es de Producción; Orchestrate cruza todo. [Mem + límites del brief]
- APQC PCF 4.1 y 4.4: no pude leer el PDF. En versiones anteriores del PCF la categoría 4 es "Deliver physical products" (4.1 planificación de la cadena, 4.4 entrega/logística). Verificar la numeración en la 7.4. Hueco.
- ASCM CSCP, CLTD y CPIM: no verificados; sirven de mapa del cuerpo de conocimiento (CLTD cubre logística, transporte y distribución; CPIM, planificación e inventario; CSCP, el extremo a extremo) [Mem].

### Qué registra un sistema

SCOR es de procesos y métricas, no de objetos. De los atributos se derivan objetos medibles: pedido (fecha prometida, fecha de entrega real, completo o no), pronóstico y plan (versión, nivel de agregación), envío (origen, destino, hitos), devolución (motivo, disposición). Es inferencia, no cita.

### Recurso canónico

El SCOR Digital Standard de ASCM (definiciones de procesos y métricas, de nivel 1 a 3). En qué fijarse: las definiciones de cálculo de cada métrica (qué cuenta como "pedido perfecto"). Hueco: no se pudo leer.

## 3. Escuelas y debates

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| https://en.wikipedia.org/wiki/Supply_chain_resilience | secundaria | 1/2/2/1 | [S] |
| https://en.wikipedia.org/wiki/Lean_manufacturing | secundaria | 1/1/1/1 | [S] |
| Fisher (1997), HBR, https://hbr.org/1997/03/what-is-the-right-supply-chain-for-your-product | primaria | 3/3/3/3 | [M] solo la primera frase del resumen |
| Naylor, Naim y Berry (1999), Int. J. Production Economics 62 | primaria | 3/3/2/3 | [Mem] |
| Sheffi, *The Resilient Enterprise* (2005); Ivanov | primarias | 3/3/2/3 | [Mem] |
| Ptak y Smith, *Demand Driven Material Requirements Planning* | primaria (de parte) | 2/3/2/2 | [Mem] |

### 3.1 Empujar y tirar, punto de desacople

Los datos son [Mem]; no se pudo abrir una fuente (la página de postponement dio 404). Definición a verificar en Chopra y Meindl: en un sistema "push" se actúa según pronóstico; en "pull", según el pedido real; el punto de desacople es donde se pasa de uno a otro. La página de lean dice que Ohno programaba "following actual sales rather than production targets", lo que describe pull como "build-to-order". https://en.wikipedia.org/wiki/Lean_manufacturing

### 3.2 Eficiente frente a que responde (Fisher 1997)

HBR da solo la apertura del resumen: "Never has so much technology and brainpower been applied to improving supply chain performance." https://hbr.org/1997/03/what-is-the-right-supply-chain-for-your-product . La tesis (productos funcionales con cadena eficiente, innovadores con cadena que responde) es [Mem]. Hay que leer el artículo para citar la matriz.

### 3.3 Lean, ágil y leagility; eficiencia frente a resiliencia

- Leagility (Naylor, Naim y Berry 1999): lean aguas arriba del punto de desacople, ágil aguas abajo. [Mem], sin verificar.
- Resiliencia: se define como "the capacity of a supply chain to persist, adapt, or transform in the face of change." Sheffi y Rice: resiliencia por redundancia (capacidad ociosa, stock de seguridad) o por flexibilidad (procesos intercambiables). Ivanov, a partir del COVID-19, propone la "viable supply chain" que combina resiliencia, agilidad y sostenibilidad. https://en.wikipedia.org/wiki/Supply_chain_resilience
- Justo a tiempo: sus críticos señalan que quien depende de entregas JIT queda varado ante una disrupción porque tiene "little or no inventory to work with." https://en.wikipedia.org/wiki/Lean_manufacturing
- Relocalizar: la OCDE estimó que relocalizar dentro de las fronteras nacionales podría reducir el comercio global "more than 18 percent" y el PIB real global "more than 5 percent", sin mejorar de forma consistente la resiliencia. En la encuesta 2024 de McKinsey, el 60 por ciento de los encuestados regionalizaba y los colchones de inventario ya no eran la táctica preferida. Todo esto es dato de Wikipedia sobre fuentes que no abrí; la afirmación de la OCDE hay que leerla en el informe original. https://en.wikipedia.org/wiki/Supply_chain_resilience

### 3.4 DDMRP

No pude abrir ninguna fuente (las dos URL de Wikipedia dieron 404). Lo que se sabe de memoria: lo propuso el Demand Driven Institute (Ptak y Smith); su lógica es reponer a partir de buffers dimensionados y consumo real, en lugar de pronosticar. La evidencia independiente (estudios con método, no del instituto ni de consultoras) es escasa, pero no pude confirmarlo con una búsqueda. Se declara hueco y la nota debe decir "evidencia independiente: no encontrada", no "no existe". Esto cae más en Producción y en Inventario que en este tema; solo la crítica a "planificar por pronóstico" es de acá.

### Qué registra un sistema

- Punto de desacople: una configuración por artículo o familia (dónde se mantiene stock y dónde se arma bajo pedido), con atributos de lead time.
- Buffers de DDMRP, si se menciona: zonas de buffer por posición, estado (verde, amarillo, rojo). Describe qué datos lleva, no que sea la norma.
- Escenario de contingencia: proveedor o ruta alternativos como objetos con prioridad. Inferencia.

### Recursos canónicos

Fisher (1997) completo; Chopra y Meindl, capítulo de diseño de red; MIT ESD.260J (https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/, CC BY-NC-SA 4.0, Caplice y Sheffi, "a survey of the fundamental analytic tools, approaches, and techniques" [S]; las notas de clase individuales no se listaron en la página).

## 4. La posición contraria

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Cachon, Randall y Schmidt (2007), MSOM 9(4):457-479, doi 10.1287/msom.1060.0149 (vía buscador) | primaria | 3/3/2/3 | [S] (solo fragmentos de abstract; el repositorio de Penn dio 403) |
| https://en.wikipedia.org/wiki/Bullwhip_effect | secundaria | 1/2/2/1 | [S] |
| https://en.wikipedia.org/wiki/Makridakis_Competitions | secundaria | 1/2/2/1 | [S] |
| https://en.wikipedia.org/wiki/Sales_and_operations_planning | secundaria | 1/1/1/1 | [S] |
| https://otexts.com/fpp3/simple-methods.html y /accuracy.html | primaria (libro libre) | 3/3/2/3 | [L] (secciones) |
| M4: Makridakis, Spiliotis y Assimakopoulos (2020), IJF 36(1); M5: IJF 38(4) 2022 | primarias | 3/3/3/3 | M5 en ScienceDirect dio 403; no leídos |
| Tavares Thomé et al. (2012), "Sales and operations planning and the firm performance" | primaria | 3/3/2/3 | solo el título, vía Wikipedia |

### 4.1 El efecto látigo es menos común de lo que dicen los libros

- Lo que dicen los libros: Lee, Padmanabhan y Whang (1997) explican la amplificación con cuatro causas: "demand signal processing, rationing game, order batching, and price variations." Wikipedia cita una fluctuación de 5 por ciento en el punto de venta leída hasta como "up to forty percent" aguas arriba. https://en.wikipedia.org/wiki/Bullwhip_effect
- Evidencia contra: Cachon, Randall y Schmidt midieron el efecto con datos agregados de industrias de EE.UU., definiendo que una industria lo muestra si la varianza de lo que recibe supera la de sus ventas. Resultado: "Wholesale industries exhibit a bullwhip effect, but retail industries generally do not exhibit the effect, nor do most manufacturing industries." Esta cita viene de un resumen del buscador, no del abstract completo. Verificar en https://doi.org/10.1287/msom.1060.0149 o en https://repository.upenn.edu/oid_papers/137 .
- Matiz de Wikipedia: "previous research is said to show that order smoothing and the bullwhip effect coexist in industry." Es decir, hay industrias que suavizan pedidos.
- Límite de lo agregado: datos agregados por industria no se dejan trasladar directo a una empresa; el estudio no dice que un fabricante concreto no sufra el látigo.
- Implicación para la nota: decir que el efecto látigo es un mecanismo real y documentado, y que su frecuencia es empírica y desigual según el eslabón.

### 4.2 S&OP no siempre mejora el desempeño

- Hay un estudio empírico (Tavares Thomé et al. 2012) del que solo consta el título; no pude leer sus resultados. Wikipedia dice explícitamente que la página no reporta hallazgos y que los modelos de madurez son "descriptive, prescriptive, and comparative tools, not measures of performance outcomes." https://en.wikipedia.org/wiki/Sales_and_operations_planning
- La literatura (Grimson y Pyke 2007; Tuomikangas y Kaipia 2014; Thomé, Hollmann y Carmo 2014) discute que el efecto depende de la madurez y de la integración. [Mem], sin fuente. Hueco: no hay una cita verificada de "S&OP no mejora".

### 4.3 Ley de la raíz cuadrada

- Maister (1976) y la ley: [Mem]; el stock de seguridad agregado crece con la raíz del número de depósitos (si las demandas son independientes y de igual varianza). Wikipedia dice solo que el beneficio del agrupamiento "is greatest 'When demands from markets are negatively correlated'" y que baja cuando la correlación positiva sube; no menciona la ley. https://en.wikipedia.org/wiki/Risk_pooling
- Por qué exagera: con demandas correlacionadas el ahorro es menor; con lead times, costos de transporte y niveles de servicio distintos, la ley deja de valer (Zinn, Levy y Bowersox 1989 sobre la reducción del inventario con consolidación parcial; Eppen 1979 para el caso normal). [Mem], sin fuente abierta. Hueco: hay que leer a Eppen (1979) y a Zinn et al. (1989) antes de afirmarlo.
- Atención: el stock de seguridad por artículo es de Inventario y depósitos; la nota de este tema solo trata la consolidación de depósitos en la red.

### 4.4 Los pronósticos complejos no les ganan a los simples (competencias M)

- M1 (1982): "Statistically sophisticated or complex methods do not necessarily provide more accurate forecasts than simpler ones." M3 (2000, 3.003 series) llegó a conclusiones similares. https://en.wikipedia.org/wiki/Makridakis_Competitions
- M4 (2018): de los 17 métodos más precisos, 12 eran combinaciones de enfoques mayormente estadísticos; los seis métodos de ML puro fueron mal, "none of them being more accurate than Comb"; el ganador, de Slawek Smyl, fue un híbrido estadístico y de ML y fue casi 10 por ciento más preciso que la combinación de referencia por sMAPE. Conclusión citada: "hybrid approaches and combination of methods is the way forward." https://en.wikipedia.org/wiki/Makridakis_Competitions
- M5 (2020): datos de Walmart, unas 42.000 series jerárquicas; los mejores fueron ML puro y "better than all statistical benchmarks and their combinations", con ensambles. https://en.wikipedia.org/wiki/Makridakis_Competitions . Es decir, la regla "simple gana" ya no vale en M5. La nota debe decirlo: depende de la serie, del volumen y de si hay datos jerárquicos y exógenos.
- La referencia obligada son los métodos simples como piso: media, ingenuo, ingenuo estacional y deriva, que "will serve as benchmarks rather than the method of choice" (Hyndman y Athanasopoulos). https://otexts.com/fpp3/simple-methods.html [L]
- Las métricas: el MAPE es "infinite or undefined" con ceros y "put a heavier penalty on negative errors than on positive errors"; el MASE escala por el error de un pronóstico ingenuo, y es menor que uno si mejora al ingenuo. https://otexts.com/fpp3/accuracy.html [L] (importa en demanda intermitente, que tiene muchos ceros).

### 4.5 "El pronóstico siempre está mal"

Es un eslogan: es cierto que todo pronóstico tiene error, pero la cuestión útil es cuánto error y qué decisión cambia. Se apoya en la lógica de medir contra una referencia simple (MASE, FPP3) y en que lo agregado se pronostica mejor que lo detallado [Mem]. La nota debe traducirlo a "no hay pronóstico sin error; hay error medible y gestionable". Sin fuente puntual leída para "agregado mejor que detallado".

### 4.6 Concepciones erróneas documentadas

- "Cadena de suministro es solo logística": la distinción histórica ya aparece en el origen del término (logística ligada a la estrategia, Oliver y Webber, título del artículo: "logistics catches up with strategy"). CSCMP separa logística como parte de la gestión de la cadena [Mem]. Hueco: hay que citar la definición del CSCMP o del diccionario de ASCM.
- "Tercerizar siempre baja costos": no encontré fuente leída; hay literatura sobre costos de transacción y de coordinación (Williamson) y sobre reintegración tras tercerizar [Mem]. Hueco.
- "Más inventario protege, menos inventario ahorra": la discusión de resiliencia muestra que depende. https://en.wikipedia.org/wiki/Supply_chain_resilience

### Qué registra un sistema

- Pronóstico: serie (artículo, ubicación, período), versión, método, valor pronosticado, error medido contra lo real y contra una referencia ingenua. Estado de la versión (borrador, consensuada).
- S&OP: ciclo (mensual), versiones de plan de demanda y de oferta, supuestos, decisiones y responsable.
- Medida de variabilidad: pedido recibido frente a venta, por eslabón, para detectar amplificación.
- Inferencia a partir de las fuentes de este ángulo, no cita.

### Recurso canónico

Cachon, Randall y Schmidt (2007) completo; Hyndman y Athanasopoulos, FPP3, cap. 5 (benchmarks) y 5.8 (precisión); Makridakis et al., M4 y M5 en IJF.

## 5. Dónde se produce el saber del campo

Todo [Mem]: no se verificó en esta sesión.

- Revistas: Journal of Operations Management; Journal of Business Logistics (CSCMP); International Journal of Physical Distribution & Logistics Management; International Journal of Forecasting; Transportation Science; Manufacturing & Service Operations Management (INFORMS), donde apareció Cachon et al.; International Journal of Production Economics (Naylor et al.).
- Asociaciones: ASCM (certificaciones CSCP, CLTD, CPIM; diccionario; SCOR) y CSCMP (definiciones, informe anual State of Logistics).
- Libros de texto: Chopra y Meindl; Simchi-Levi et al.; Ballou; Silver, Pyke y Thomas; Hyndman y Athanasopoulos (libre en https://otexts.com/fpp3/).
- Cursos abiertos: MIT OCW ESD.260J Logistics Systems, Fall 2006, Caplice y Sheffi, CC BY-NC-SA 4.0. https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/ [S]. MITx MicroMasters en Supply Chain Management: sin verificar el estado actual del programa.
- Por tipo de pregunta: "cómo falla" va a las revistas empíricas (JOM, MSOM); "cómo se decide", a los libros de texto y a OR; "qué hay hoy", a informes fechados de consultoras (secundaria marcada).

## 6. Glosario (48 términos)

Definiciones cortas redactadas por el redactor del informe a partir de lo que dice cada concepto en los libros de texto; **no se pudo leer el diccionario de ASCM** ni extractos. Hay que contrastarlas antes de publicarlas. Las que tienen fuente abierta llevan URL.

| Español | Inglés | Definición corta |
|---|---|---|
| cadena de suministro | supply chain | red de empresas y actividades que llevan un producto desde la materia prima hasta el cliente |
| gestión de la cadena de suministro | supply chain management | coordinación de esa red; término popularizado desde 1982 (ver sección 1) |
| logística | logistics | planificación y ejecución del flujo y almacenamiento de bienes; parte de la gestión de la cadena |
| distribución física | physical distribution | el movimiento de producto terminado hacia el cliente, antecedente de la logística |
| pronóstico de demanda | demand forecast | estimación de la demanda futura |
| planificación de la demanda | demand planning | proceso de generar y acordar el pronóstico |
| S&OP | sales and operations planning | proceso mensual que alinea demanda y oferta; https://en.wikipedia.org/wiki/Sales_and_operations_planning |
| planificación de requerimientos de distribución | distribution requirements planning (DRP) | reposición planificada de depósitos de quien no fabrica |
| MRP | material requirements planning | explosión de necesidades de materiales (es de Producción) |
| efecto látigo | bullwhip effect | pedidos más variables que la demanda, y más cuanto más arriba |
| agrupamiento de riesgo | risk pooling | agregar demanda reduce la variabilidad relativa; https://en.wikipedia.org/wiki/Risk_pooling |
| ley de la raíz cuadrada | square root law | stock de seguridad crece con la raíz del número de depósitos (ver 4.3) |
| empujar | push | actuar según pronóstico |
| tirar | pull | actuar según el pedido real |
| punto de desacople | decoupling point | donde la cadena pasa de pronóstico a pedido real |
| posposición | postponement | retrasar la diferenciación del producto hasta conocer el pedido |
| cadena eficiente | efficient supply chain | minimiza costo; para productos funcionales (Fisher) |
| cadena que responde | responsive supply chain | prioriza velocidad y flexibilidad; para productos innovadores (Fisher) |
| lean | lean | eliminar desperdicio |
| ágil | agile | responder rápido a la variación |
| leagility | leagility | lean aguas arriba, ágil aguas abajo del desacople |
| justo a tiempo | just-in-time (JIT) | recibir lo necesario cuando se necesita, con poco inventario |
| por si acaso | just-in-case | mantener colchones por si hay disrupción |
| resiliencia | resilience | "the capacity of a supply chain to persist, adapt, or transform in the face of change" https://en.wikipedia.org/wiki/Supply_chain_resilience |
| redundancia | redundancy | capacidad o stock de reserva |
| flexibilidad | flexibility | procesos intercambiables |
| relocalización cercana | nearshoring | mover producción o compras a un país cercano |
| relocalización | reshoring | traer producción al país de origen |
| red de distribución | distribution network | depósitos, centros y rutas que sirven a los clientes |
| centro de distribución | distribution center | depósito que recibe y despacha |
| consolidación | consolidation | juntar envíos para aprovechar el transporte |
| carga completa | full truckload (FTL) | un camión para un cliente |
| carga fraccionada | less-than-truckload (LTL) | un camión compartido |
| multimodal | intermodal | un envío con varios modos usando la misma unidad de carga |
| contenedor | container | unidad de carga normalizada (ISO) |
| flete | freight | carga transportada o su precio |
| transportista | carrier | quien transporta |
| operador logístico | third-party logistics (3PL) | tercero que presta servicios logísticos |
| tiempo de entrega | lead time | desde el pedido hasta la recepción |
| nivel de servicio | service level | probabilidad o proporción de satisfacer la demanda |
| pedido perfecto | perfect order | pedido completo, a tiempo, sin daño y con documentos correctos [Mem] |
| error de pronóstico | forecast error | real menos pronosticado |
| MAPE | mean absolute percentage error | error porcentual absoluto medio; falla con ceros (https://otexts.com/fpp3/accuracy.html) |
| MASE | mean absolute scaled error | error medio escalado por el pronóstico ingenuo (misma URL) |
| método ingenuo | naive method | pronóstico igual al último valor observado (https://otexts.com/fpp3/simple-methods.html) |
| demanda intermitente | intermittent demand | demanda con muchos períodos en cero |
| SCOR | Supply Chain Operations Reference | modelo de procesos y métricas de ASCM (ver sección 2) |
| CSCMP | Council of Supply Chain Management Professionals | asociación profesional |
| ASCM | Association for Supply Chain Management | asociación; incluye al ex Supply Chain Council |
| Incoterms | Incoterms | reglas de la ICC sobre quién asume costo y riesgo del transporte [Mem] |
| trazabilidad | traceability | poder seguir un envío o lote por la cadena |

Son 48 filas. Las demás definiciones son [Mem].

## Huecos

- No se leyó ningún artículo primario completo. Lo de la sección 4 (látigo, competencias M, raíz cuadrada, S&OP) se apoya en resúmenes secundarios y en un fragmento de abstract.
- Sin leer: SCOR DS (atributos de nivel 1 con sus nombres exactos), APQC PCF 7.4 (4.1 y 4.4), diccionario de ASCM, Fisher 1997, Naylor et al. 1999, Maister 1976, Eppen 1979, M5 en IJF.
- Sin fuente: DDMRP (evidencia independiente), "tercerizar siempre baja costos", MRP/DRP históricos, logística militar.
- Presupuesto de búsquedas agotado: pedir más búsquedas (CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION) o reintentar luego para estos puntos.
- Sheffi, Ivanov y OCDE: solo vía Wikipedia.

## Discrepancias y árbol

- Autoría del término: Wikipedia dice Oliver solo (entrevista del Financial Times, 1982); el brief dice Oliver y Webber (artículo de Outlook). Probablemente ambos son ciertos para dos hechos distintos; verificar.
- Forrester: 1958 (artículo de HBR) frente a 1961 (*Industrial Dynamics*); citar los dos con su texto.
- Fecha del contenedor: 1956 (Ideal X, 26/4/1956) frente a la fecha general "around 1956" de la otra página.
- M4 y M5 discrepan en la lección: en M4, ML puro no ganó; en M5 sí. La nota no puede afirmar "lo simple gana" sin matizar.
- Árbol: la división de SCOR (Plan, Order, Fulfill, Return) no coincide con los límites del tema (SCOR Source y Transform son de otros temas; Fulfill queda partido entre este tema e Inventario y depósitos). Sugiero que la nota de marcos incluya una tabla "qué proceso de SCOR es de qué tema". La nota de "posición contraria" puede ir dentro de cada mecanismo (látigo, S&OP, raíz cuadrada, pronóstico) y no como nota aparte, porque el brief pide afirmar con su evidencia en contra al lado.
