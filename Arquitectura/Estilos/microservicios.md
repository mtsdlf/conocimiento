---
resumen: >-
  Microservicios es el estilo que parte el sistema en servicios chicos, uno por capacidad de negocio,
  cada uno con su base y su despliegue independiente. Da límites firmes, despliegue por separado y
  libertad de stack a cambio de distribución, consistencia eventual y más operación.
estado: vigente
estabilidad: semi
fuentes:
  - "James Lewis y Martin Fowler, Microservices (2014-03-25): https://martinfowler.com/articles/microservices.html"
  - "Martin Fowler, Microservice Trade-Offs (2015-07-01): https://martinfowler.com/articles/microservice-trade-offs.html"
  - "Chris Richardson, Pattern: Microservice Architecture: https://microservices.io/patterns/microservices.html"
  - "Melvin Conway, Conway's Law: https://www.melconway.com/Home/Conways_Law.html"
  - "Team Topologies, Key concepts: https://teamtopologies.com/key-concepts"
  - "Microsoft, Architecture styles, Azure Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/"
  - "Sam Newman, Building Microservices, 2ª ed., página del libro: https://samnewman.io/books/building_microservices_2nd_edition/"
  - "InfoQ, Newman en QCon 2020: https://www.infoq.com/news/2020/05/monolith-decomposition-newman/"
  - "Rafal Gancarz, InfoQ, sobre el caso Prime Video (2023-05-03): https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/"
  - "Marcin Kolny, Prime Video Tech (2023-03-22), no accesible: https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90"
  - "Adrian Cockcroft vía The Stack (2023-05-09): https://www.thestack.technology/prime-video-monolith-architecture-debate-bad-takes-adrian-cockcroft"
  - "DHH, Even Amazon can't make sense of serverless or microservices (2023-05-04): https://world.hey.com/dhh/even-amazon-can-t-make-sense-of-serverless-or-microservices-59625580"
aliases: [microservices, arquitectura de microservicios, microservice architecture]
creado: 2026-11-27
revisado: 2026-11-27
---

# Microservicios

Microservicios es el estilo que parte el sistema en servicios chicos, uno por capacidad de negocio, cada uno con su base y su despliegue independiente. Da límites firmes, despliegue por separado y libertad de stack a cambio de distribución, consistencia eventual y más operación.

## Las nueve características de Lewis y Fowler

El artículo que fijó el término (Lewis y Fowler, 2014) no da una definición sino nueve rasgos comunes: componentes como servicios, organización por capacidades de negocio, productos y no proyectos, endpoints inteligentes y tuberías tontas, gobierno descentralizado, datos descentralizados, automatización de infraestructura, diseño para la falla y diseño evolutivo.

Los mismos autores nombran los costos: las llamadas remotas son más caras que las locales y "Moving code is difficult across service boundaries". Por eso sugieren que un equipo podría "begin with a monolith", que es lo que el tema recomienda con el [monolito modular](monolito-modular.md).

## Partir por capacidad de negocio, como el equipo

Lewis y Fowler citan a Conway (1968): una organización "will produce a design whose structure is a copy of the organization's communication structure". De ahí sacan que los servicios se cortan por capacidad de negocio y no por capa técnica: un servicio de pedidos con su equipo, no un servicio de base de datos compartido por todos. Conway publicó el texto en Datamation en abril de 1968, después de que Harvard Business Review lo rechazara.

La ley y su uso deliberado, diseñar los equipos para obtener la arquitectura que se quiere, están en [Ley de Conway](../../Platform-Engineering/Organizacion-de-equipos/ley-de-conway.md) y [Maniobra inversa de Conway](../../Platform-Engineering/Organizacion-de-equipos/maniobra-inversa-de-conway.md), en Platform Engineering. Team Topologies lo resume desde el lado de los equipos: "Nothing kills productivity faster than one team waiting on another team."

## Tres beneficios y tres costos

Fowler ordenó la decisión en 2015 en tres beneficios y tres costos:

| Beneficio | Costo |
|---|---|
| Límites de módulo firmes: "Putting the modules into separate services makes the boundaries firmer" | Distribución: "remote calls are slow and are always at risk of failure" |
| Despliegue independiente de cada servicio | Consistencia eventual entre las bases de cada servicio |
| Diversidad tecnológica: cada servicio elige su stack | Complejidad operativa |

Fowler agrega que los factores blandos (la calidad del equipo y cómo colabora) pesan más que la elección del estilo. Richardson suma un costo menos visible: el acoplamiento de diseño, cuando cambiar una cosa obliga a cambiar varios servicios en "lockstep changes". Newman llama monolito distribuido al peor caso, el costo de la red sin la independencia (dato de un resumen secundario).

Según la lectura de esta base, los tres costos son medibles, y eso es lo que pide la mirada del tema: cuántos equipos se traban al desplegar, cuánta latencia suma la cadena de llamadas, cuántas operaciones cruzan servicios. Medir antes de partir es la regla de [Empezar simple](../Decisiones/empezar-simple.md); qué características pesar está en [Elegir un estilo](elegir-un-estilo.md).

## Lo que un sistema de microservicios necesita alrededor

Azure dice que sirven en dominios complejos con actualizaciones frecuentes, pero "Success requires mature development and DevOps practices". Richardson supone equipos chicos y multifuncionales, con DevOps. Esta base lo lee así: sin pipelines automatizados ni observabilidad, los costos de la tabla crecen sin los beneficios; eso es lo que cubren [DevOps](../../DevOps/devops.md) y una plataforma interna ([Platform Engineering](../../Platform-Engineering/platform-engineering.md)).

Cada costo de la distribución tiene un patrón en [Sistemas distribuidos](../Sistemas-distribuidos/sistemas-distribuidos.md):

- Una operación que toca varios servicios con base propia: [saga](../Sistemas-distribuidos/saga.md), y para publicar sus eventos sin perder ninguno, [outbox](../Sistemas-distribuidos/outbox.md).
- Una dependencia que falla y arrastra al resto: [circuit breaker](../Sistemas-distribuidos/circuit-breaker.md) y [degradación controlada](../Sistemas-distribuidos/degradacion-controlada.md).
- Varios clientes frente a muchos servicios: [API gateway y BFF](../Sistemas-distribuidos/api-gateway-y-bff.md).

## Microservicios por defecto

Newman, autor de *Building Microservices*, dijo en QCon 2020 que "Microservices should not be the default choice" y que no son "a good choice for most startups" (cita de InfoQ sobre la charla). DHH es más duro: los llama "perhaps the biggest siren song for needlessly complicating your system". Por qué el tema no los toma como punto de partida, con la posición de Tilkov en contra, está en [Lo que pierde peso](../Fundamentos/lo-que-pierde-peso.md).

## Prime Video: un caso que se lee de dos maneras

En marzo de 2023, el equipo de análisis de calidad de video de Prime Video contó que había juntado en un solo proceso un componente de monitoreo armado con funciones serverless orquestadas. El post original ya no se puede abrir (la URL redirige); los números que siguen vienen del resumen de InfoQ (el del 5 % también lo da DHH). El diseño distribuido pasaba los ítems intermedios entre pasos por almacenamiento de objetos, y el costo venía de esas lecturas y escrituras y de las transiciones del orquestador, que además chocaron con el límite de la cuenta cerca del 5 % de la carga esperada. Al consolidar todo en un proceso con los datos en memoria, el costo bajó un 90 %. Marcin Kolny, su autor: "We realized that distributed approach wasn't bringing a lot of benefits in our specific use case."

> [!IMPORTANT]
> Buena parte de la prensa, y DHH, lo leyó como "de microservicios a monolito" y como prueba contra el estilo. Adrian Cockcroft, ex Amazon y Netflix, lo lee como la evolución planeada de un prototipo serverless a un servicio único escalado horizontalmente, y dice que el debate se perdió el punto (su texto se leyó solo en parte, por un paywall). Otros comentaristas, vistos solo por buscador, dicen que es un monolito "only at the service level". La lectura de esta base: es un componente con mucho dato entre etapas fuertemente acopladas, no un sistema de negocio entero, y lo que muestra es el costo de pasar datos por la red entre pasos que no se separan. No es un veredicto sobre microservicios.

Para leer más: "Microservice Trade-Offs" de Fowler (2015) como eje de cuándo valen lo que cuestan; fijarse en que cada beneficio y cada costo se puede medir en el sistema propio. Después, el capítulo de microservicios de Richards y Ford (2ª ed.) y el capítulo 2 de *Monolith to Microservices* de Newman, "When Might Microservices Be A Bad Idea?"; ninguno de los dos se leyó.
