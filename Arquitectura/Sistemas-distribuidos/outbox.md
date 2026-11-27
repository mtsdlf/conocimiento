---
resumen: >-
  El outbox guarda el mensaje que hay que publicar en una tabla de la misma base y en la misma
  transacción que el cambio de negocio; un proceso aparte lo lee y lo publica en el broker. Así no se
  pierde ni se inventa un evento cuando falla algo entre escribir y publicar.
estado: borrador
estabilidad: estable
fuentes:
  - "Chris Richardson, Pattern: Transactional outbox, microservices.io: https://microservices.io/patterns/data/transactional-outbox.html"
  - "Gunnar Morling, Reliable Microservices Data Exchange With the Outbox Pattern (2019-02-19): https://debezium.io/blog/2019/02/19/reliable-microservices-data-exchange-with-the-outbox-pattern/"
  - "AWS Prescriptive Guidance, Transactional outbox pattern: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html"
  - "Microsoft, CQRS pattern, Azure Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs"
aliases: [transactional outbox, outbox pattern, patrón outbox, bandeja de salida]
creado: 2026-11-27
revisado:
---

# Outbox

El outbox guarda el mensaje que hay que publicar en una tabla de la misma base y en la misma transacción que el cambio de negocio; un proceso aparte lo lee y lo publica en el broker. Así no se pierde ni se inventa un evento cuando falla algo entre escribir y publicar.

## La escritura doble

Un servicio de pedidos guarda un pedido en su base y publica el evento "pedido creado" para que lo escuchen stock y facturación. Son dos escrituras en dos sistemas distintos, y no hay una transacción que abarque las dos: Morling lo dice para su caso, "we cannot have one shared transaction that would span the service's database" y el broker. AWS llama a esto "dual write". Si la base se actualiza y la publicación falla, el pedido existe y nadie se entera. Si se publica primero y la base falla, los demás reaccionan a un pedido que no existe.

Richardson presenta el patrón como la solución sin commit en dos fases. Las fuentes leídas no explican por qué se descarta ese commit, así que la base no lo deduce.

## Una tabla en la misma transacción, y un relay

El outbox convierte la escritura doble en una sola. En la transacción que guarda el pedido se inserta también una fila en una tabla `outbox` con el evento. Un proceso aparte, el relay, lee esa tabla y publica en el broker. Richardson lo resume: "Messages are guaranteed to be sent if and only if the database transaction commits".

El relay se arma de dos formas, según Richardson:

| Relay | Cómo lee | Qué cuesta |
|---|---|---|
| **Polling publisher** | consulta la tabla cada tanto y publica las filas nuevas | carga de consultas sobre la base y algo de demora |
| **Transaction log tailing** | lee el log de transacciones de la base con captura de cambios (CDC) | una pieza más que operar, atada al motor de base |

La columna de costos es inferencia de esta base. Morling describe la segunda: el log de la base se lee con CDC y el ID del agregado (el pedido) va como clave de partición, para que los eventos de un mismo pedido lleguen en orden. AWS da como ejemplo los streams de cambios de una base NoSQL. Qué herramienta implementa cada variante es dato de la capa operativa.

## Al menos una vez, y por eso consumidores idempotentes

El outbox no garantiza que cada evento llegue exactamente una vez. Por ejemplo, si el relay publica y se cae antes de marcar la fila como enviada, la vuelve a publicar. La semántica es "at least once" (Morling), y Richardson lo dice igual: el relay puede publicar un mensaje más de una vez.

Por eso el consumidor tiene que ser idempotente. Morling manda el UUID del evento en un header, y el consumidor guarda en una tabla los IDs ya procesados para descartar los repetidos. Es la misma idea que la [clave de idempotencia](clave-de-idempotencia.md) de una API, aplicada a mensajes. AWS agrega que hay que preservar el orden; Azure recomienda el mismo par, outbox más consumidor idempotente, para sincronizar los dos modelos de [CQRS](cqrs.md).

## Dónde aparece

Richardson dice que la [saga](saga.md) y los eventos de dominio son los que crean la necesidad: cada paso de una saga confirma su transacción local y publica su resultado, y ese "publicar después de escribir" es justo el problema que el outbox resuelve. Lo mismo vale para cualquier componente de un sistema [event-driven](../Estilos/event-driven.md) que publique tras escribir en su base, y, por inferencia de esta base, para los pendientes que deja una [degradación controlada](degradacion-controlada.md), como un email que se manda en segundo plano.

Richardson nombra una alternativa: con [event sourcing](cqrs.md#event-sourcing-guardar-los-cambios-en-lugar-del-estado), el evento es la escritura, y no hay dos cosas que sincronizar.

> [!NOTE]
> Sin fuente todavía: un postmortem de una falla en producción por escritura doble o por un outbox mal operado.

Para leer más: Richardson, que es corto y define el problema, y después el post de Morling (2019), por la implementación con CDC, el orden y los duplicados. Fijarse en el modo de falla (dos sistemas sin transacción común), en lo que garantiza (al menos una vez, no exactamente una vez) y en por qué eso obliga a la idempotencia del consumidor.
