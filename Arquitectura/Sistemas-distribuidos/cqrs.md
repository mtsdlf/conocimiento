---
resumen: >-
  CQRS (Command Query Responsibility Segregation) separa el modelo que actualiza los datos del modelo
  que los lee, para que cada uno tenga la forma que le sirve. Agrega complejidad y, para la mayoría de
  los sistemas, no hace falta.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, CQRS (2011-07-14): https://martinfowler.com/bliki/CQRS.html"
  - "Martin Fowler, What do you mean by Event-Driven? (2017-02-07): https://martinfowler.com/articles/201701-event-driven.html"
  - "Microsoft, CQRS pattern, Azure Architecture Center (2025-02-20): https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs"
  - "Chris Richardson, Pattern: Event sourcing, microservices.io: https://microservices.io/patterns/data/event-sourcing.html"
aliases: [Command Query Responsibility Segregation, separación de comandos y consultas, event sourcing]
creado: 2026-11-27
revisado: 2026-11-27
---

# CQRS

CQRS (Command Query Responsibility Segregation) separa el modelo que actualiza los datos del modelo que los lee, para que cada uno tenga la forma que le sirve. Agrega complejidad y, para la mayoría de los sistemas, no hace falta.

## Un modelo para escribir y otro para leer

En la mayoría de los sistemas, el mismo modelo (las mismas entidades y tablas) sirve para guardar un pedido y para mostrar el listado de pedidos. Esta base lo explica así: cuando las dos necesidades se separan mucho, ese modelo único queda incómodo para las dos: las escrituras necesitan validar reglas sobre un agregado y las lecturas necesitan vistas planas que junten datos de varios lados. CQRS los parte: los comandos van a un modelo de escritura y las consultas a uno de lectura. Fowler atribuye la descripción del patrón a Greg Young.

Azure lo describe en dos niveles:

| Nivel | Qué se separa | Qué cuesta |
|---|---|---|
| **Básico** | dos modelos en el código, sobre el mismo almacén | más código; ninguna sincronización |
| **Avanzado** | dos almacenes, uno optimizado para escribir y otro para leer | sincronizarlos, con mensajería y consistencia eventual |

La columna de costos es inferencia de esta base. En el nivel avanzado, cada cambio del modelo de escritura se publica para actualizar el de lectura. Azure pide para eso un [outbox](outbox.md) del lado que publica y un consumidor idempotente del lado que lee, porque los mensajes pueden llegar repetidos. Mientras el mensaje viaja, la lectura muestra un dato viejo: es consistencia eventual.

## Cuándo paga y cuándo no

Azure lista los beneficios: escalar lecturas y escrituras por separado, esquemas optimizados para cada lado, seguridad distinta para cada uno y consultas más simples. Los costos son la complejidad, la mensajería (duplicados, reintentos) y la consistencia eventual. No conviene, según Azure, cuando "the domain or the business rules are simple" o cuando alcanza una interfaz CRUD.

Fowler es más tajante: "for most systems CQRS adds risky complexity", y "you should be very cautious about using CQRS". Esta base lee el nivel básico como la versión barata que alcanza a muchos sistemas; el avanzado se suma cuando una medición lo pide, por ejemplo una carga de lectura que el modelo de escritura no aguanta. Es la regla de [Empezar simple](../Decisiones/empezar-simple.md) aplicada al modelo de datos.

## CQRS no es event-driven

Fowler aclara en 2017 que CQRS "isn't inherently event-based": es uno de los cuatro patrones que se confunden bajo "event-driven" (los otros tres están en [Event-driven](../Estilos/event-driven.md)). Se puede hacer CQRS con dos modelos sobre la misma base y sin un solo evento. Lo que sí dice Fowler en 2011 es que encaja bien con modelos orientados a eventos.

## Event sourcing: guardar los cambios en lugar del estado

Event sourcing guarda cada cambio de estado como un evento en una secuencia que solo crece, en lugar de guardar el estado actual. El saldo de una cuenta no está en una columna: se calcula sumando sus depósitos y extracciones. Según Richardson, eso da auditoría completa y consultas temporales (cómo estaba algo en una fecha).

Sus desventajas, según Richardson: es un estilo de programación poco familiar, y el almacén de eventos es difícil de consultar, "so queries typically require CQRS". Por eso suelen ir juntos: los eventos son el modelo de escritura y una o más vistas armadas a partir de ellos son el modelo de lectura. Azure avisa que la complejidad crece "specifically when combined with the Event Sourcing pattern".

Event sourcing también resuelve el problema del [outbox](outbox.md) por otro camino: si el evento es la escritura, no hay una base y un broker que mantener de acuerdo. Richardson lo nombra como alternativa al outbox.

> [!NOTE]
> Sin fuente todavía: los textos originales de Greg Young sobre CQRS (2010) no se leyeron, y no se encontró un postmortem de CQRS o event sourcing en producción.

Para leer más: Fowler (2011), por la advertencia de complejidad, y la página de Azure, por los dos niveles. Fijarse en el nivel básico (mismo almacén, dos modelos): es lo que alcanza a muchos sistemas, y el segundo nivel y el event sourcing son pasos que se dan con una medición en la mano.
