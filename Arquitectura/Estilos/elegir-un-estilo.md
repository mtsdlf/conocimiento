---
resumen: >-
  Elegir un estilo es ir de las características que el sistema tiene que cumplir, priorizadas, al
  estilo que mejor las sostiene, sabiendo que cada estilo gana en unas y pierde en otras. La elección
  se registra y se vuelve a medir: no se hace una sola vez.
estado: vigente
estabilidad: semi
fuentes:
  - "Microsoft, Architecture styles, Azure Architecture Center (2025-09-25): https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/"
  - "Mark Richards y Neal Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), índice: https://nealford.com/books/SAF2e.html"
  - "Richards y Ford, Fundamentals of Software Architecture, 2ª ed., prefacio (no leído, 403): https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/preface01.html"
  - "Mark Richards, Software Architecture Patterns, apéndice (no leído, 403): https://www.oreilly.com/library/view/software-architecture-patterns/9781098134280/app01.html"
  - "Martin Fowler, Microservice Trade-Offs (2015): https://martinfowler.com/articles/microservice-trade-offs.html"
aliases: [elegir un estilo de arquitectura, choosing an architecture style, selección de estilo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Elegir un estilo

Elegir un estilo es ir de las características que el sistema tiene que cumplir, priorizadas, al estilo que mejor las sostiene, sabiendo que cada estilo gana en unas y pierde en otras. La elección se registra y se vuelve a medir: no se hace una sola vez.

## Primero las características, después el estilo

El estilo no se elige por moda ni por lo que usa otra empresa: sale de qué tiene que cumplir el sistema. Azure propone empezar por el problema, los impulsores de negocio y las [características arquitectónicas](../Caracteristicas/caracteristicas-arquitectonicas.md) priorizadas. Da dos ejemplos: si el tiempo de salida al mercado es crítico, priorizar mantenibilidad, testeabilidad y confiabilidad; con presupuesto ajustado, factibilidad y simplicidad.

Priorizar quiere decir elegir pocas. Un sistema que quiere todas las características a la vez no tiene criterio para elegir, porque cada estilo compra unas a costa de otras: los [microservicios](microservicios.md) compran despliegue independiente y límites firmes a costa de simplicidad y consistencia, y el [monolito modular](monolito-modular.md) hace la compra inversa.

## Los pasos

1. Escribí las pocas características que más pesan, con un número cuando se pueda (latencia, costo por consulta, frecuencia de despliegue). Cómo se definen y se miden está en [Características](../Caracteristicas/caracteristicas.md).
2. Mirá el dominio: cuántas áreas de negocio tiene, cuánto cambia y cuántos equipos van a trabajar en paralelo. Ese número de equipos pesa por la [ley de Conway](../../Platform-Engineering/Organizacion-de-equipos/ley-de-conway.md).
3. Arrancá por el estilo más simple que cumpla las características priorizadas. En la escalera del tema, eso es un [estilo simple](estilos-simples.md) o un [monolito modular](monolito-modular.md); [service-based](service-based.md) y [microservicios](microservicios.md) entran cuando una característica medida lo pide.
4. Decidí aparte si las piezas se comunican por eventos ([event-driven](event-driven.md)): no es un escalón sino una forma de conectar, que se suma cuando el desacople temporal vale lo que cuesta.
5. Registrá la decisión y lo que la haría cambiar en un [ADR](../Decisiones/adr.md).
6. Convertí las características priorizadas en chequeos automáticos ([fitness functions](../Caracteristicas/fitness-function.md)) para saber cuándo el estilo dejó de alcanzar.

El paso 3 es la regla de [Empezar simple](../Decisiones/empezar-simple.md) aplicada al estilo. Si el sistema tiene un modelo de IA adentro, el [costo y la latencia](../Caracteristicas/costo-y-latencia.md) pasan al frente de la lista del paso 1.

## Estilo por tipo de dominio, según Azure

Azure resume una correspondencia gruesa entre el tipo de dominio y el estilo:

| Dominio | Estilo que sugiere |
|---|---|
| Tradicional, con pocas actualizaciones | N-tier ([capas](estilos-simples.md#capas-partir-por-función-técnica)) |
| Simple, con tareas pesadas en segundo plano | Web-Queue-Worker |
| Complicado, con actualizaciones frecuentes | [Microservicios](microservicios.md) |
| IoT y tiempo real | [Event-driven](event-driven.md) |

En lo que recogió la investigación, esa correspondencia no nombra el monolito modular ni service-based. Es un punto de partida, no un veredicto.

## La tabla de calificaciones del canon

Según el resumen del buscador, Richards y Ford califican cada estilo contra una lista de características, y el índice del libro muestra el capítulo "Choosing the Appropriate Architecture Style". Qué características puntúan (despliegue, elasticidad, evolución, costo, simplicidad, entre otras) es lo que habría que mirar en la tabla, no algo verificado.

> [!NOTE]
> Sin fuente todavía: la tabla de la 2ª edición no se leyó. O'Reilly devolvió 403, y según el resumen del buscador la 2ª edición cambió algunas calificaciones y sumó categorías, y el informe *Software Architecture Patterns* de Richards puntúa cada estilo de 1 a 5 por característica. Ninguno de esos valores se verificó, así que esta base no da puntajes por estilo: copiarlos sin la tabla sería inventarlos.

Según la lectura de esta base, aun con la tabla a mano sus calificaciones serían una heurística de práctica y no una medición del sistema propio.

## Una elección que se vuelve a medir

Azure lo dice así: "Selecting and sustaining an architectural style isn't a one-time task. It requires ongoing measurement, validation, and refinement." Cuando las mediciones muestran que el estilo dejó de alcanzar, el cambio se hace de a partes con un [strangler fig](strangler-fig.md) y se escribe un ADR nuevo que reemplaza al anterior.

Para leer más: el capítulo "Choosing the Appropriate Architecture Style" de Richards y Ford (2ª ed.), fijándose en qué características puntúa y en que las calificaciones son heurísticas. Como lectura abierta, la guía de estilos de Azure, por el orden de las preguntas, y "Microservice Trade-Offs" de Fowler para la decisión entre monolito y microservicios.
