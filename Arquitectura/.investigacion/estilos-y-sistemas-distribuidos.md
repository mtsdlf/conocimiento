# Investigación: Estilos/ y Sistemas-distribuidos/ (arquitectura de software hoy)

Fecha de la investigación: 2026-11-27. Lectores objetivo: ingenieros que programan y saben lo básico de servicios. Mirada: Chip Huyen (empezar simple, sumar piezas si la medición lo pide) sobre el canon de Richards y Ford.

Leyenda de marcas: [L] texto completo leído (vía WebFetch, que resume con un modelo chico: ver nota de método), [M] metadatos o abstract, [S] resumen secundario o del buscador.
Puntajes 1-3: Aut = autoridad, Prof = profundidad, Ej = ejemplos, Uni = unicidad.

Nota de método: WebFetch devuelve un resumen hecho por un modelo sobre la página, no el HTML crudo. Las citas literales entre comillas salieron de ese resumen; las páginas de Microsoft Learn y AWS vinieron casi completas (texto fuente). Antes de citar literalmente en una nota, conviene recotejar contra la página.

## 0. Sobre la división del árbol

- La división Estilos/ (monolito-modular, estilos-simples, event-driven, microservicios, elegir-un-estilo) coincide en lo grueso con la Parte II de Richards y Ford 2ª ed. (marzo 2025): capas, "The Modular Monolith Architecture", pipeline, microkernel, service-based, event-driven, space-based, SOA orquestada, microservicios, y después "elegir un estilo" y patrones. https://nealford.com/books/SAF2e.html [L]
- Hueco del árbol: falta service-based. Está en el canon como estilo propio (entre capas y microservicios, normalmente con base de datos compartida). Con la mirada "empezar simple" es el escalón natural entre monolito-modular y microservicios. Propuesta: sumarlo dentro de `microservicios` como "versión gruesa" o como nota aparte. No pude verificar su contenido en esta ronda (solo figura en el índice).
- Una distinción que el campo hace y el árbol puede perder: el monolito-modular y las capas se distinguen por el eje de partición (técnica vs de dominio), no por el despliegue. Kamil Grzybek define monolito como "a system that has exactly one deployment unit" y dice que la etiqueta no habla de calidad. https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer [L]
- Fowler (2017) avisa que "event-driven" mezcla cuatro cosas distintas: event notification, event-carried state transfer, event sourcing y CQRS. Conviene que `event-driven` (estilo) y `cqrs` (patrón) se escriban remitiéndose entre sí y que event sourcing quede como sección de `cqrs` y no como nota aparte. https://martinfowler.com/articles/201701-event-driven.html [L]
- Strangler fig y API gateway/BFF: en Newman y en Richardson aparecen en contexto de migración y de microservicios. Aceptable en Sistemas-distribuidos, pero strangler fig es más una técnica de evolución que de distribución; considerar enlazarlo desde `monolito-modular` y `microservicios`.
- Mediator vs broker: Richards y Ford (y Microsoft) lo tratan como dos topologías dentro del estilo event-driven, no como notas separadas. Coincide con el árbol.

## 1. Estilos/monolito-modular

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Richards y Ford, SAF 2ª ed., página del libro | https://nealford.com/books/SAF2e.html | Primaria (índice) | 3 | 1 | 1 | 3 | [M] |
| Fowler, "MonolithFirst" (3 jun 2015) | https://martinfowler.com/bliki/MonolithFirst.html | Primaria | 3 | 2 | 1 | 3 | [L] |
| Fowler, "Microservice Premium" (13 may 2015) | https://martinfowler.com/bliki/MicroservicePremium.html | Primaria | 3 | 2 | 1 | 2 | [L] |
| Shopify Engineering, "Under Deconstruction: The State of Shopify's Monolith" (16 sep 2020, Philip Müller) | https://shopify.engineering/shopify-monolith | Primaria (caso) | 3 | 3 | 3 | 3 | [L] |
| Grzybek, "Modular Monolith: A Primer" (2 dic 2019) | https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer | Primaria (practicante) | 2 | 3 | 2 | 3 | [L] |
| Richardson, patrón Monolithic Architecture | https://microservices.io/patterns/monolithic.html | Primaria | 3 | 2 | 1 | 2 | [L] |
| Prime Video Tech, post original (22 mar 2023, Marcin Kolny) | https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90 | Primaria (caso) | 3 | 3 | 3 | 3 | [S] (la URL redirige y no pude abrir el post; ver huecos) |
| InfoQ, Gancarz (3 may 2023) | https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/ | Secundaria buena (resume el post) | 2 | 2 | 2 | 1 | [L] |
| Cockcroft, "So many bad takes" (9 may 2023, actualizado 29 may 2023), vía The Stack | https://www.thestack.technology/prime-video-monolith-architecture-debate-bad-takes-adrian-cockcroft | Secundaria sobre primaria (paywall) | 2 | 1 | 1 | 3 | [S] parcial |

Nota: InfoQ, The New Stack y los demás medios sobre Prime Video parafrasean el mismo post: cuentan como una sola fuente (el post original).

### Afirmaciones

- Richards y Ford 2ª ed. se publicó en marzo 2025 (O'Reilly, ISBN 9781098175504) y agrega un capítulo "The Modular Monolith Architecture" que, según los autores, llena un hueco de la primera edición. https://nealford.com/books/SAF2e.html
- Fowler: "you shouldn't start a new project with microservices"; la mayoría de los sistemas de microservicios exitosos empezaron como monolito que creció; los que arrancaron como microservicios "often ran into serious trouble". Los límites de servicio son difíciles de acertar al inicio y refactorizar entre servicios es más duro que dentro de un monolito. Reconoce que la evidencia es escasa. https://martinfowler.com/bliki/MonolithFirst.html
- Fowler: "don't even consider microservices unless you have a system that's too complex to manage as a monolith"; el "premium" puede "slow down your development considerably". https://martinfowler.com/bliki/MicroservicePremium.html
- Shopify (2020): el monolito núcleo tenía unas 2,8 millones de líneas de Ruby y unos 500.000 commits, "hundreds of developers", 37 componentes, Packwerk aplicado en cerca de un tercio de ellos; el análisis inicial mostró que cada componente dependía de más de la mitad de los otros. Dicen que el objetivo es el "modular monolith" y que "While we're far from finished, we already reap the benefits". Packwerk reemplazó a Wedge (análisis en runtime, más de una hora) por análisis estático de referencias a constantes que corre en minutos y rechaza PRs que rompen la encapsulación. https://shopify.engineering/shopify-monolith
- Grzybek: la modularidad exige independencia, funcionalidad de negocio completa y una interfaz definida; los módulos deben ser cortes verticales de negocio; se comunican por contrato síncrono (fachada) o asíncrono (evento publicado). https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer
- Richardson: ventajas del monolito: operaciones locales, transacciones ACID, sin acoplamiento de runtime entre componentes; desventajas: base grande, poca autonomía de equipos, pipeline lento, un solo stack, sin escalado por subdominio; "These drawbacks become more severe as the application grows in size and complexity". https://microservices.io/patterns/monolithic.html
- Prime Video: el equipo de Video Quality Analysis tenía microservicios serverless (Step Functions orquestando Lambdas, S3 para frames y buffers, SNS para resultados) que alcanzaban cerca del 5% de la carga esperada; el costo venía de lecturas y escrituras a S3 y de transiciones de Step Functions (que además chocaban con el límite de la cuenta). Consolidaron la lógica en un único proceso sobre ECS en EC2, con datos en memoria; los costos bajaron 90%. Kolny: "We realized that distributed approach wasn't bringing a lot of benefits in our specific use case." https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/ [resumen del post]
- Discrepancia sobre cómo leer el caso: el titular y buena parte de la prensa lo leyó como "microservicios a monolito"; Cockcroft (ex Amazon/Netflix) lo lee como evolución planeada de un prototipo serverless ("Serverless First", "best practice") a un servicio único escalado horizontalmente y dice que el debate "se perdió el punto". https://www.thestack.technology/prime-video-monolith-architecture-debate-bad-takes-adrian-cockcroft Para la nota: es un caso sobre un componente de monitoreo con flujo de datos pesado entre etapas, no sobre un sistema de negocio completo; presentarlo como "el costo de pasar datos por la red entre pasos fuertemente acoplados", no como veredicto contra microservicios.

### Recurso canónico propuesto

- Primero: el capítulo "The Modular Monolith Architecture" de Richards y Ford 2ª ed. (no leído; solo índice). Fijarse en: qué eje de partición usa, cómo se hace cumplir el aislamiento entre módulos (comunicación, datos) y cómo califica el estilo en la tabla de características.
- Como lectura abierta y verificada: Shopify (2020) para "cómo se hace cumplir" (Packwerk, medir dependencias entre componentes) más Fowler MonolithFirst para el "por qué". Fijarse en el dato de que la mayoría de los componentes dependía de más de la mitad de los otros: la modularidad no se declara, se mide.
- Para "cómo falla lo distribuido": Prime Video, post original, con la lectura de Cockcroft al lado.

## 2. Estilos/estilos-simples (capas, pipeline, microkernel)

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Richards y Ford, SAF 2ª ed. (índice) | https://nealford.com/books/SAF2e.html | Primaria | 3 | 1 | 1 | 3 | [M] |
| Azure Architecture Center, "Architecture Styles" (ms.date 2025-09-25) | https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/ | Secundaria buena | 2 | 2 | 1 | 2 | [L] |

### Afirmaciones

- El libro tiene capítulos separados para layered, pipeline y microkernel. https://nealford.com/books/SAF2e.html
- Azure (N-tier): divide en capas lógicas y niveles físicos, cada capa solo llama hacia abajo; sirve para migrar aplicaciones ya en capas; "the horizontal layering can make it difficult to introduce changes without affecting multiple parts of the application". También describe Web-Queue-Worker (front web, cola, worker) para dominios simples con tareas pesadas, con el riesgo de que ambas piezas se vuelvan monolíticas. https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
- Azure plantea los estilos como restricciones: "Focus more on why you're selecting a specific style than on how to implement it. Be practical. Sometimes it's better to relax a constraint than to chase architectural purity." https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/

### Recurso canónico propuesto

- Los capítulos de capas, pipeline y microkernel de SAF 2ª ed. (no leídos). Fijarse en: la tabla de calificaciones de cada capítulo y el "cuándo no".
- Alternativa gratuita de Mark Richards: el informe "Software Architecture Patterns" (O'Reilly, 2ª ed.), cuyo apéndice trae puntajes por estilo; el sitio devolvió 403. https://www.oreilly.com/library/view/software-architecture-patterns/9781098134280/app01.html [S: solo vía buscador]

### Hueco

- No encontré fuente verificada para pipeline y microkernel con ejemplos reales (Unix pipes, plugins de IDE, Eclipse, Jenkins). Sin lectura del capítulo, hay que escribirlo marcado como borrador con ejemplos propios o sacar ejemplos de la documentación oficial de cada producto.

## 3. Estilos/event-driven

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Azure, "Event-Driven Architecture Style" (ms.date 2026-03-06) | https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven | Secundaria buena | 2 | 3 | 2 | 2 | [L] |
| Fowler, "What do you mean by Event-Driven?" (7 feb 2017) | https://martinfowler.com/articles/201701-event-driven.html | Primaria | 3 | 2 | 1 | 3 | [L] |

### Afirmaciones

- Fowler distingue cuatro cosas bajo "event-driven": event notification, event-carried state transfer, event sourcing y CQRS; "asynchronous communication is not a necessary part of event sourcing or CQRS". De event notification: "the source system doesn't really care much about the response", y su riesgo es que el flujo global se vuelve difícil de ver. https://martinfowler.com/articles/201701-event-driven.html
- Azure define dos topologías, que coinciden con broker y mediator de Richards y Ford. Broker: los componentes difunden eventos, sin coordinación central; sirve cuando el flujo es simple; "No component owns or is aware of the state of any multistep business transaction", así que las transacciones distribuidas son riesgosas y no hay mecanismo de reintento o replay. Mediator: un mediador mantiene el estado, maneja errores y reinicios y despacha comandos a canales (a menudo colas); más control y mejor consistencia, pero más acoplamiento y el mediador puede ser cuello de botella. https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven
- Azure, cuándo no: flujos simples de request-response donde bastan llamadas síncronas; transacciones que exigen consistencia fuerte; equipos sin experiencia operando sistemas asíncronos distribuidos. https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven
- Azure, desafíos concretos: consistencia eventual, orden y exactly-once, manejo de errores con dead-letter queue, pérdida de datos, observabilidad (incluir correlation ID en cada evento), evolución de esquemas, y el tamaño del payload (todos los atributos vs solo claves). https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven
- Pub/sub (sin log durable, no se ven eventos pasados) vs event streaming (log ordenado por partición, replay posible). Distinto de colas con competing consumers, donde cada mensaje lo procesa un solo consumidor. https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven

### Recurso canónico propuesto

- Fowler 2017 primero (corto, ordena el vocabulario), después el capítulo event-driven de Richards y Ford (no leído; fijarse en broker vs mediator y en la calificación de testeabilidad y simplicidad). Azure como lista de verificación de problemas operativos.
- Eventos y colas: las dos referencias cubren el contraste cola (un consumidor por mensaje) vs pub/sub vs log. No encontré una fuente canónica independiente de proveedor (por ejemplo "Enterprise Integration Patterns") leída; solo está enlazada desde Azure.

## 4. Estilos/microservicios

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Lewis y Fowler, "Microservices" (25 mar 2014) | https://martinfowler.com/articles/microservices.html | Primaria | 3 | 3 | 2 | 3 | [L] |
| Fowler, "Microservice Trade-Offs" (1 jul 2015) | https://martinfowler.com/articles/microservice-trade-offs.html | Primaria | 3 | 3 | 2 | 3 | [L] |
| Richardson, patrón Microservice Architecture | https://microservices.io/patterns/microservices.html | Primaria | 3 | 2 | 1 | 2 | [L] |
| Newman, Building Microservices 2ª ed., página del libro | https://samnewman.io/books/building_microservices_2nd_edition/ | Primaria (índice) | 3 | 1 | 1 | 2 | [M] |
| Newman, Monolith to Microservices, página del libro | https://samnewman.io/books/monolith-to-microservices/ | Primaria (índice) | 3 | 1 | 1 | 2 | [M] |
| Team Topologies, conceptos clave | https://teamtopologies.com/key-concepts | Primaria | 3 | 1 | 1 | 3 | [L] |
| Melvin Conway, página sobre la ley | https://www.melconway.com/Home/Conways_Law.html | Primaria | 3 | 1 | 1 | 3 | [L] |
| Azure, "Architecture Styles" | https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/ | Secundaria buena | 2 | 2 | 1 | 1 | [L] |

### Afirmaciones

- Lewis y Fowler (2014) listan nueve características: componentización vía servicios, organización por capacidades de negocio, productos no proyectos, endpoints inteligentes y tuberías tontas, gobierno descentralizado, gestión de datos descentralizada, automatización de infraestructura, diseño para la falla, diseño evolutivo. Costos que mencionan: las llamadas remotas son más caras que las locales, "Moving code is difficult across service boundaries", y sugieren que un equipo podría "begin with a monolith". https://martinfowler.com/articles/microservices.html
- Conway: el artículo cita a Conway (1968) "will produce a design whose structure is a copy of the organization's communication structure" y lo usa para justificar partir por capacidades de negocio y no por capas técnicas. https://martinfowler.com/articles/microservices.html Conway publicó "How Do Committees Invent?" en Datamation, abril de 1968 (Harvard Business Review lo había rechazado). https://www.melconway.com/Home/Conways_Law.html
- Fowler (2015), tres beneficios: límites de módulo firmes ("Putting the modules into separate services makes the boundaries firmer"), despliegue independiente, diversidad tecnológica. Tres costos: distribución ("remote calls are slow and are always at risk of failure"), consistencia eventual, complejidad operativa. Los factores blandos (calidad y colaboración del equipo) pesan más que la elección. https://martinfowler.com/articles/microservice-trade-offs.html
- Richardson: beneficios (autonomía de equipos, pipelines rápidos, flexibilidad de stack) y costos (operaciones distribuidas difíciles de entender, ineficiencias, consistencia eventual, acoplamiento de runtime que baja la disponibilidad, riesgo de acoplamiento de diseño con "lockstep changes"). Supone equipos pequeños y multifuncionales con DevOps. https://microservices.io/patterns/microservices.html
- Team Topologies: cuatro tipos de equipo (stream-aligned, enabling, complicated subsystem, platform) y tres modos de interacción (collaboration, X-as-a-Service, facilitation); "Nothing kills productivity faster than one team waiting on another team." La página no trata Conway ni la inverse Conway maneuver, así que esa relación hay que fundarla en otra fuente. https://teamtopologies.com/key-concepts
- Azure: microservicios sirven en dominios complejos con actualizaciones frecuentes, pero "Success requires mature development and DevOps practices". https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
- Newman 2ª ed.: reescritura completa de la 1ª; usa ocultamiento de información, acoplamiento, cohesión y DDD para hallar fronteras; Kubernetes "no cura" los problemas de microservicios; capítulos "Splitting the Monolith" y "Organizational Structures". La página no dice cuándo no usarlos. https://samnewman.io/books/building_microservices_2nd_edition/ Monolith to Microservices tiene una sección "When Might Microservices Be A Bad Idea?" (solo el título es visible). https://samnewman.io/books/monolith-to-microservices/

### Recurso canónico propuesto

- Fowler, "Microservice Trade-Offs" (2015) como eje de "cuándo valen lo que cuestan", complementado por el capítulo de microservicios de SAF 2ª ed. y el cap. 2 de Monolith to Microservices ("When Might Microservices Be A Bad Idea?"), ambos sin leer. Fijarse en: que los tres beneficios y los tres costos son medibles (cuántos equipos se pisan al desplegar, latencia de la cadena de llamadas), que es lo que pide la mirada de Chip Huyen.
- Para Conway: la fuente primaria (Conway 1968) más Team Topologies como modelo operativo.

### Hueco

- Ninguna de las páginas de libros trae el contenido de los capítulos; Newman 2ª ed. y Team Topologies (libro) quedan como [M]. Falta una fuente primaria sobre el "inverse Conway maneuver".

## 5. Estilos/elegir-un-estilo

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Richards y Ford, SAF 2ª ed., prefacio (O'Reilly) | https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/preface01.html | Primaria | 3 | 1 | 1 | 3 | [S] (403 al abrirlo; solo el buscador dice que cambiaron las calificaciones con estrellas y agregaron categorías) |
| Azure, "Architecture Styles" | https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/ | Secundaria buena | 2 | 2 | 1 | 2 | [L] |
| Richards, Software Architecture Patterns, apéndice | https://www.oreilly.com/library/view/software-architecture-patterns/9781098134280/app01.html | Primaria | 3 | 2 | 1 | 3 | [S] (403) |

### Afirmaciones

- Azure: empezar por el problema, los impulsores de negocio y las características de arquitectura priorizadas (por ejemplo "si el time to market es crítico, priorizar mantenibilidad, testeabilidad y confiabilidad"; con presupuesto ajustado, factibilidad y simplicidad). "Selecting and sustaining an architectural style isn't a one-time task. It requires ongoing measurement, validation, and refinement." https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
- Azure resume estilo por tipo de dominio: N-tier para dominio tradicional con pocas actualizaciones; Web-Queue-Worker para dominio simple con tareas pesadas; microservicios para dominio complicado con actualizaciones frecuentes; event-driven para IoT y tiempo real. https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
- El apéndice del informe de Richards puntúa cada estilo de 1 a 5 puntos por característica (1 es soporte pobre, 5 fuerte); la 2ª ed. del libro cambió algunas calificaciones y sumó categorías. Ambos dichos son del buscador, no verificados en la página. https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/preface01.html

### Recurso canónico propuesto

- La tabla de calificaciones por estilo del capítulo "Choosing the Appropriate Architecture Style" de SAF 2ª ed. Fijarse en: qué características puntúa cada estilo (despliegue, elasticidad, evolución, costo, simplicidad) y que las calificaciones son una heurística, no una medición. Como la tabla de la 2ª ed. no se pudo leer, no se puede copiar ni citar; hay que citar sin reproducir los valores o comprar o consultar el libro.

### Hueco

- No hay tabla de estrellas verificada de ningún estilo. Cualquier nota que dé puntajes sin esa lectura sería inventada.

## 6. Sistemas-distribuidos/outbox

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Richardson, Transactional Outbox | https://microservices.io/patterns/data/transactional-outbox.html | Primaria | 3 | 2 | 1 | 3 | [L] |
| Morling (Debezium), "Reliable Microservices Data Exchange With the Outbox Pattern" (19 feb 2019) | https://debezium.io/blog/2019/02/19/reliable-microservices-data-exchange-with-the-outbox-pattern/ | Primaria (implementación) | 2 | 3 | 3 | 2 | [L] |
| AWS Prescriptive Guidance, Transactional outbox | https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html | Secundaria buena | 2 | 2 | 2 | 1 | [L] |
| Azure, CQRS (menciona outbox + consumidor idempotente) | https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs | Secundaria buena | 2 | 1 | 1 | 1 | [L] |

### Afirmaciones

- Problema: actualizar la base y enviar un mensaje al broker de forma atómica, sin 2PC. Solución: guardar el mensaje en una tabla outbox en la misma transacción que la entidad de negocio; un relay lo lee y lo publica. "Messages are guaranteed to be sent if and only if the database transaction commits". Puede publicar un mensaje más de una vez, así que los consumidores deben ser idempotentes. El relay puede ser polling publisher o transaction log tailing. https://microservices.io/patterns/data/transactional-outbox.html
- Debezium: "we cannot have one shared transaction that would span the service's database as well as Apache Kafka"; el log de la base se lee con CDC; el ID de agregado como clave de partición mantiene el orden por agregado; semántica "at least once", con el UUID del evento en un header y una tabla de eventos procesados en el consumidor para deduplicar. https://debezium.io/blog/2019/02/19/reliable-microservices-data-exchange-with-the-outbox-pattern/
- AWS: explica el "dual write" (si la base se actualiza y la notificación falla, o al revés, queda inconsistente), ofrece outbox table o CDC (ejemplo DynamoDB Streams), y recomienda idempotencia y preservar el orden; si la transacción abarca servicios, saga. https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html
- Relación con las notas existentes: outbox resuelve el "publicar tras escribir" que saga e idempotencia dan por supuesto. Richardson dice que Saga y Domain event crean la necesidad del patrón y que event sourcing es una alternativa. https://microservices.io/patterns/data/transactional-outbox.html

### Recurso canónico propuesto

- Richardson (corto, define el problema) más el post de Debezium de Morling (implementación con CDC, orden, duplicados). Fijarse en: el modo de falla (escribir en dos sistemas sin transacción común), qué garantiza (at least once, no exactly once) y por eso la idempotencia del consumidor.
- Nota sin cubrir: el libro "Microservices Patterns" de Richardson (no leído).

## 7. Sistemas-distribuidos/cqrs (y event sourcing)

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Fowler, bliki CQRS (14 jul 2011) | https://martinfowler.com/bliki/CQRS.html | Primaria | 3 | 2 | 1 | 3 | [L] |
| Fowler, "What do you mean by Event-Driven?" (2017) | https://martinfowler.com/articles/201701-event-driven.html | Primaria | 3 | 2 | 1 | 2 | [L] |
| Azure, CQRS (ms.date 2025-02-20) | https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs | Secundaria buena | 2 | 3 | 3 | 2 | [L] |
| Richardson, Event sourcing | https://microservices.io/patterns/data/event-sourcing.html | Primaria | 3 | 2 | 1 | 2 | [L] |

### Afirmaciones

- Fowler (2011): CQRS separa el modelo que actualiza del modelo que lee; el patrón se lo describió Greg Young. Advertencia: "for most systems CQRS adds risky complexity"; "you should be very cautious about using CQRS". Encaja bien con modelos orientados a eventos. https://martinfowler.com/bliki/CQRS.html
- Fowler (2017): CQRS "isn't inherently event-based"; son cuatro patrones distintos y no hay que confundirlos. https://martinfowler.com/articles/201701-event-driven.html
- Azure: dos niveles; modelos separados en un solo almacén (el nivel básico) o almacenes distintos (más avanzado, exige sincronizar, con outbox e idempotencia en el consumidor). Beneficios: escalado independiente, esquemas optimizados, seguridad, consultas más simples. Costos: complejidad, mensajería (duplicados, reintentos), consistencia eventual. No conviene cuando "the domain or the business rules are simple" o basta una interfaz CRUD. https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
- Event sourcing: guardar cambios de estado como secuencia de eventos; da auditoría y consultas temporales; desventajas: estilo de programación poco familiar, y el event store es difícil de consultar, "so queries typically require CQRS". https://microservices.io/patterns/data/event-sourcing.html
- Azure sobre combinarlos: la complejidad crece "specifically when combined with the Event Sourcing pattern". https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs

### Recurso canónico propuesto

- Fowler 2011 (la advertencia de complejidad, que es el tono de la vertical) más el CQRS de Azure para los dos niveles. Fijarse en el primer nivel (mismo almacén, modelos de lectura y escritura separados): es la versión barata que alcanza a muchos sistemas; el segundo nivel y event sourcing son pasos a dar con medición.

### Hueco

- No leí los textos originales de Greg Young (CQRS Documents, 2010). El dato de que Young lo describió viene de Fowler.

## 8. Sistemas-distribuidos/api-gateway-y-bff

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Richardson, API Gateway | https://microservices.io/patterns/apigateway.html | Primaria | 3 | 2 | 1 | 3 | [L] |
| Newman, "Backends For Frontends" | https://samnewman.io/patterns/architectural/bff/ | Primaria | 3 | 3 | 2 | 3 | [L] |
| Azure, Backends for Frontends (ms.date 2025-03-19) | https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends | Secundaria buena | 2 | 2 | 2 | 1 | [L] |

### Afirmaciones

- Richardson: un API gateway es el punto de entrada único; enruta o abre en abanico a varios servicios, agrega resultados, adapta protocolos y maneja seguridad. Variante BFF: un gateway por tipo de cliente. Beneficios: oculta la partición en servicios, menos viajes de red para móvil ("An API gateway is essential for mobile applications"). Costos: otro componente que construir y operar, un salto de red más. https://microservices.io/patterns/apigateway.html
- Newman: un BFF es un componente de servidor dedicado a una experiencia de usuario, "tightly coupled to a specific user experience", mantenido normalmente por el mismo equipo que la interfaz; la regla "one experience, one BFF" es de Stewart Gleadow y el nombre lo puso Phil Calçado (SoundCloud). Riesgos: duplicación entre BFFs, hinchazón si un BFF sirve a muchos clientes ("the more types of clients you have using a single BFF, the more temptation there may be for it to become bloated"), costo de más servicios. https://samnewman.io/patterns/architectural/bff/
- Azure: no conviene si las interfaces hacen pedidos iguales o similares, o si hay una sola interfaz; con GraphQL con resolvers por frontend el BFF puede no aportar; el BFF solo debe tener lógica específica de cliente y lo transversal (autorización, monitoreo) va en el gateway. https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends
- Discrepancia de encuadre: Richardson trata BFF como una variante del gateway; Newman y Azure lo tratan como patrón propio y lo distinguen de un gateway genérico. La nota puede tener una sola página con las dos secciones, como propone el árbol.

### Recurso canónico propuesto

- Newman sobre BFF (la parte de duplicación y hinchazón) y Richardson para el gateway. Fijarse en la pregunta que Azure agrega: si ya hay un gateway y un solo cliente, probablemente el BFF todavía no hace falta.

### Hueco

- Falta una fuente de postmortem sobre un gateway que se volvió cuello de botella o punto único de falla (Azure y AWS solo lo advierten en abstracto, ver sección 9).

## 9. Sistemas-distribuidos/strangler-fig

### Fuentes

| Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|
| Fowler, bliki StranglerFigApplication (22 ago 2024) | https://martinfowler.com/bliki/StranglerFigApplication.html | Primaria | 3 | 3 | 2 | 3 | [L] |
| Azure, Strangler Fig (ms.date 2026-05-29) | https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig | Secundaria buena | 2 | 3 | 2 | 1 | [L] |
| AWS Prescriptive Guidance, Strangler fig | https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html | Secundaria buena | 2 | 2 | 1 | 1 | [L] |
| Newman, Monolith to Microservices (cap. 3) | https://samnewman.io/books/monolith-to-microservices/ | Primaria (índice) | 3 | 1 | 1 | 2 | [M] |

### Afirmaciones

- Fowler: la página tiene fecha 22 de agosto de 2024. Cuenta que en 2001 vio higueras estranguladoras en Queensland y que "a couple of years later" escribió una entrada breve. Esa entrada se llamaba "Strangler Application" y luego fue retitulada "Strangler Fig Application". La página no da el año de la entrada original, así que el "2004" del encargo no está confirmado. https://martinfowler.com/bliki/StranglerFigApplication.html
- Fowler: reemplazar un sistema serio "takes a long time, and the users can't wait for new features"; "the reduced risk and earlier value from the gradual approach outweigh its costs". Cita a Cartwright, Horn y Lewis (cuatro actividades: entender los resultados deseados, partir el problema, entregar las partes, cambiar la organización) y pide reflejar la ley de Conway. https://martinfowler.com/bliki/StranglerFigApplication.html
- Azure: una fachada (proxy) enruta pedidos entre el sistema viejo y el nuevo y se va corriendo el tráfico; cuándo no: pedidos que no se pueden interceptar, sistema pequeño que se reemplaza fácil, necesidad de apagar el viejo rápido; considerar capa anticorrupción y que la fachada no sea punto único de falla. Incluye el caso de partir una base de datos monolítica por dominio con CDC, con reversión posible hasta quitar los objetos viejos. https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig
- AWS: tres pasos (transform, coexist, eliminate) con un proxy HTTP en el perímetro; desventajas: no sirve para sistemas chicos, la fachada puede ser cuello de botella, hace falta plan de reversión por servicio. https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html
- Discrepancia: Azure habla de una fachada que luego se quita; AWS pone el API Gateway como el proxy. Fowler no fija el mecanismo, solo el enfoque gradual y las costuras. https://martinfowler.com/bliki/StranglerFigApplication.html

### Recurso canónico propuesto

- Fowler 2024 (el porqué y el vínculo con organización) más Azure (el mecanismo y el caso de la base de datos). Fijarse en: el costo de la arquitectura transicional y la reversión.
- Newman, cap. 3 de Monolith to Microservices ("Splitting the Monolith"), sin leer.

### Hueco

- Ningún caso de ingeniería publicado (Shopify, Prime Video u otro) usando strangler fig que pude citar con número; sería buen ejemplo para la nota.

## 10. Huecos declarados (resumen)

1. Tabla de calificaciones con estrellas de Richards y Ford (1ª y 2ª ed.): no encontrada; O'Reilly devolvió 403 y el buscador no mostró los valores.
2. Contenido de los capítulos de SAF 2ª ed. (modular monolith, capas, pipeline, microkernel, service-based, event-driven, microservicios, elegir estilo): solo el índice. Sin lectura, no se puede decir qué dice el "capítulo nuevo" más allá de que existe y llena un hueco de la 1ª ed.
3. Post original de Prime Video: la URL redirige a aboutamazon.com y no pude leerlo; los números (90%, 5% de la carga, Step Functions, S3) vienen de InfoQ, que resume el post. Cockcroft quedó parcial por paywall. Recomiendo recuperarlo (por ejemplo desde otra caché) antes de publicar la nota; si no, marcar [S].
4. Newman (ambos libros), Team Topologies (libro), Richardson ("Microservices Patterns") y Greg Young: sin acceso al texto; solo páginas de autor o resúmenes.
5. Inverse Conway maneuver: sin fuente primaria leída.
6. Pipeline y microkernel: sin fuente verificada con ejemplos reales.
7. Event-driven: sin fuente independiente de proveedor sobre colas vs eventos (Enterprise Integration Patterns solo enlazado).
8. Postmortems de fallas en gateways, outbox o CQRS en producción: no encontrados en las tres rondas; solo advertencias en abstracto.
9. Fecha original de la entrada de Fowler sobre strangler (el "2004" del encargo no se confirma; la página dice "a couple of years" después de 2001).
10. Shopify 2020 es anterior a hoy (2026-11-27): puede haber actualizaciones (por ejemplo la liberación de Packwerk, que el post solo prometía "soon"). No se verificó.
11. Service-based no tiene componente en el árbol (ver sección 0).
