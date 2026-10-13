---
tipo: concepto
resumen: >-
  Un circuit breaker corta las llamadas a una dependencia que viene fallando: tras superar un
  umbral de errores en una ventana, pasa a abierto y responde enseguida, sin esperar el timeout.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Martin Fowler, CircuitBreaker (2014): https://martinfowler.com/bliki/CircuitBreaker.html"
  - "Resilience4j, CircuitBreaker: https://resilience4j.readme.io/docs/circuitbreaker"
  - "Microsoft, Circuit Breaker pattern, Azure Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker"
  - "Archivo/Arquitectura/circuit-breaking-resilience4j.md (original)"
aliases: [Cortacircuito, Circuit breaking, Disyuntor]
parte_de: []
requiere: []
relacionado: [saga]
---

# Circuit breaker

Un circuit breaker corta las llamadas a una dependencia que viene fallando: tras superar un
umbral de errores en una ventana, pasa a abierto y responde enseguida, sin esperar el timeout.

## Por qué importa

Si un servicio de precios tarda 30 segundos en fallar, cada pedido que lo llama ocupa un hilo
durante esos 30 segundos. Con suficiente tráfico, el que llama se queda sin hilos y falla también:
la falla se propaga en cascada. El circuit breaker corta esa cadena y le da tiempo a la
dependencia para recuperarse. Michael Nygard lo popularizó en *Release It!* (2007).

## Cómo funciona

El breaker envuelve cada llamada y tiene tres estados:

| Estado | Qué hace con una llamada | Cuándo cambia |
|---|---|---|
| **Cerrado** | la deja pasar y registra si falló o fue lenta | si la tasa de fallas de la ventana supera el umbral, pasa a abierto |
| **Abierto** | la rechaza enseguida, sin llamar a la dependencia | después de un tiempo de espera, pasa a semiabierto |
| **Semiabierto** | deja pasar unas pocas llamadas de prueba | si salen bien, vuelve a cerrado; si fallan, a abierto |

La ventana puede contar las últimas N llamadas o las de los últimos N segundos. Una llamada lenta
(más que un umbral de duración) puede contar como falla, porque una dependencia lenta hace el
mismo daño que una caída.

Se aplica en las llamadas síncronas a otro servicio o a un proveedor externo, en la clase cliente
que hace la llamada, para no mezclar la política con la lógica de negocio. No se aplica al acceso
a la base propia ni a los consumidores de una cola: ahí alcanzan los timeouts del driver y los
reintentos del broker. Siempre va con un timeout: sin timeout, una llamada colgada nunca cuenta
como falla.

## Ejemplo

Un servicio de carrito llama a Precios con una ventana de 20 llamadas y un umbral del 50 %. Si
11 de las últimas 20 fallan, el breaker se abre por 10 segundos y el carrito usa su
[[degradacion-controlada]]: muestra el último precio guardado marcado como estimado.

## No confundir con

Un retry. El retry repite una llamada que falló, pensando que la falla es pasajera; el breaker
deja de llamar porque la falla parece persistente. Se combinan: el retry absorbe fallas aisladas
y el breaker evita reintentar contra una dependencia caída.

## Relaciones

- Base de: [[degradacion-controlada]] — qué se devuelve cuando el breaker está abierto.
- Casos: [[resilience4j-en-spring-boot]] — una implementación en Java.
- Relacionado: [[saga]] — en un checkout, una falla con el breaker abierto dispara las compensaciones de la saga.
