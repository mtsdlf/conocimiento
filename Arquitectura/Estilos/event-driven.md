---
resumen: >-
  Event-driven es el estilo en que las piezas de un sistema se comunican publicando eventos (algo que
  pasó) y reaccionando a los de otras, en lugar de llamarse directo. Se arma en dos topologías: broker,
  sin coordinador, y mediator, con uno que lleva el estado del flujo.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, What do you mean by Event-Driven? (2017-02-07): https://martinfowler.com/articles/201701-event-driven.html"
  - "Microsoft, Event-driven architecture style, Azure Architecture Center (2026-03-06): https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven"
  - "Mark Richards y Neal Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), índice: https://nealford.com/books/SAF2e.html"
aliases: [event-driven architecture, EDA, arquitectura orientada a eventos, arquitectura dirigida por eventos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Event-driven

Event-driven es el estilo en que las piezas de un sistema se comunican publicando eventos (algo que pasó) y reaccionando a los de otras, en lugar de llamarse directo. Se arma en dos topologías: broker, sin coordinador, y mediator, con uno que lleva el estado del flujo.

## Cuatro cosas distintas bajo el mismo nombre

Fowler avisó en 2017 que "event-driven" mezcla cuatro patrones que no conviene confundir:

| Patrón | Qué hace | Dónde sigue en la base |
|---|---|---|
| **Event notification** | un sistema avisa que algo cambió y no espera respuesta | esta nota |
| **Event-carried state transfer** | el evento lleva los datos, y el que escucha guarda su copia para no tener que preguntar | esta nota |
| **Event sourcing** | el estado se guarda como la secuencia de eventos que lo produjeron | [CQRS](../Sistemas-distribuidos/cqrs.md#event-sourcing-guardar-los-cambios-en-lugar-del-estado) |
| **CQRS** | el modelo que escribe es distinto del que lee | [CQRS](../Sistemas-distribuidos/cqrs.md) |

Fowler aclara que "asynchronous communication is not a necessary part of event sourcing or CQRS": se pueden usar sin un broker de por medio. De la notificación dice que "the source system doesn't really care much about the response", y que su riesgo es que el flujo completo deja de verse en un solo lugar.

## Broker y mediator

Azure describe dos topologías, que coinciden con las que usan Richards y Ford (cuyo capítulo no se leyó).

En **broker**, cada componente publica sus eventos y los demás reaccionan, sin nadie que coordine. Sirve cuando el flujo es simple. Su límite, según Azure: "No component owns or is aware of the state of any multistep business transaction". Por eso las transacciones que cruzan varios pasos son riesgosas y no hay un lugar natural para reintentar o reprocesar.

En **mediator**, un mediador recibe el evento inicial, lleva el estado del flujo, maneja errores y reinicios y despacha comandos a cada paso, muchas veces por colas. Da más control y mejor consistencia, a cambio de más acoplamiento, y el mediador puede volverse cuello de botella.

Es la misma elección que tiene una [saga](../Sistemas-distribuidos/saga.md) entre coreografía y orquestación; la correspondencia (broker con coreografía, mediator con orquestación) es lectura de esta base.

## Colas, pub/sub y logs de eventos

Azure distingue tres formas de mover mensajes, que cambian lo que el estilo puede hacer:

- **Cola con consumidores que compiten**: cada mensaje lo procesa un solo consumidor. Reparte trabajo.
- **Pub/sub**: cada suscriptor recibe una copia del evento, pero no hay un log durable: quien se suscribe tarde no ve los eventos pasados.
- **Event streaming**: un log ordenado por partición que se puede releer desde cualquier punto (replay).

Qué servicio de nube implementa cada forma está en [Mensajería](../../Cloud/Mensajeria/mensajeria.md), en Cloud.

## Lo que cuesta operarlo

Azure lista los problemas que aparecen en producción: consistencia eventual entre las piezas, orden y entrega exactamente una vez, errores que van a una cola de mensajes muertos, pérdida de datos, observabilidad, evolución de los esquemas de evento y tamaño del payload (mandar todos los atributos o solo las claves). Para la observabilidad pide un correlation ID en cada evento, que permite seguir un flujo entre servicios; cómo se arma eso está en [Observabilidad](../../DevOps/Operacion/observabilidad.md), en DevOps.

Dos de esos problemas tienen patrón propio en la base. Publicar un evento después de escribir en la base sin perder ninguno es el [outbox](../Sistemas-distribuidos/outbox.md). Procesar dos veces el mismo evento sin repetir el efecto pide consumidores idempotentes, con la misma idea que la [clave de idempotencia](../Sistemas-distribuidos/clave-de-idempotencia.md).

## Cuándo no conviene

Azure lo desaconseja en tres casos: flujos simples de pedido y respuesta donde alcanzan llamadas síncronas, transacciones que exigen consistencia fuerte y equipos sin experiencia operando sistemas asíncronos distribuidos. Para esta base, event-driven no es un escalón entre el [monolito modular](monolito-modular.md) y los [microservicios](microservicios.md): es una forma de comunicar piezas que se suma cuando el desacople temporal vale lo que cuesta.

Para leer más: primero Fowler (2017), que es corto y ordena el vocabulario; después el capítulo event-driven de Richards y Ford (2ª ed.), fijándose en broker contra mediator y en cómo califica la testeabilidad y la simplicidad. La página de Azure sirve como lista de verificación antes de poner el estilo en producción.
