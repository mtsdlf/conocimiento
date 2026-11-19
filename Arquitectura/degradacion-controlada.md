---
resumen: >-
  Degradación controlada es decidir qué devuelve un servicio cuando falla una dependencia: datos
  parciales en lecturas, error explícito o estado "pendiente" en comandos críticos.
estado: borrador
estabilidad: estable
fuentes:
  - "Archivo/Arquitectura/circuit-breaking-resilience4j.md (original)"
  - "Resilience4j, Getting Started (Spring Boot 3), fallback methods: https://resilience4j.readme.io/docs/getting-started-3"
aliases: [Graceful degradation, Fallback, Degradación elegante]
creado: 2026-10-03
revisado:
---

# Degradación controlada

Degradación controlada es decidir qué devuelve un servicio cuando falla una dependencia: datos
parciales en lecturas, error explícito o estado "pendiente" en comandos críticos.

## Qué deja sin resolver un breaker abierto

Un [Circuit breaker](circuit-breaker.md) abierto evita esperar, pero deja la pregunta de qué responder. Si la
respuesta se improvisa en el código, una página de producto sin promociones puede terminar en un
error 500, y un checkout sin confirmación de stock puede terminar vendiendo algo que no hay. La
regla de degradación se decide por tipo de operación, antes de escribir el fallback.

## La estrategia según el tipo de operación

La pregunta que ordena la decisión es si una respuesta incompleta puede causar un efecto falso.

| Operación | Estrategia | Ejemplo |
|---|---|---|
| **Lectura** (listado, detalle) | datos parciales, valor en cache o marcador visible | sin promociones; precio guardado con la marca `estimated` |
| **Comando dudoso** (agregar al carrito) | aceptar y marcar para verificar después, o rechazar con 503 | ítem `unverified` que se valida en el checkout |
| **Comando crítico** (cobrar, reservar stock) | fallar rápido, sin inventar un resultado | 503 y reintento del cliente |
| **Integración externa asíncrona** (pago, email) | registrar como pendiente y reintentar en segundo plano | intento de pago `PENDING`; email en una tabla outbox |

En escritura, lo que no se puede degradar se aborta entero: un cambio a medias es peor que un
error. Si ya hubo efectos en otros servicios, se deshacen con las compensaciones de una [Saga](saga.md).

El fallback es el método que implementa la estrategia. Recibe la excepción, así que puede
distinguir un breaker abierto de un timeout o de un 4xx, que no conviene degradar porque indica un
error del que llama.

## Una página de producto con cuatro dependencias

Una página de producto llama a Precios, Inventario, Promociones e Imágenes. Si Promociones falla,
la página sale sin promociones. Si Inventario falla, muestra "consultar disponibilidad" en lugar
de afirmar que hay stock. Si Precios falla y no hay precio guardado, el producto no se puede
agregar al carrito.

## Degradar no es ocultar el error

Una degradación se ve: el marcador `estimated` o el texto "consultar
disponibilidad" le dicen al usuario y al frontend que el dato no es firme, y la falla queda en los
logs y las métricas.

## Ver también

- [Proteger un cliente HTTP con Resilience4j en Spring Boot](resilience4j-en-spring-boot.md): cómo se escribe un fallback en Java.
