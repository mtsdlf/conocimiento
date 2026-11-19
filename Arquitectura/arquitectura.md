---
tipo: mapa
resumen: >-
  Patrones de arquitectura de software para sistemas distribuidos: cómo se organizan las APIs
  entre servicios y cómo se resiste a las fallas de una dependencia.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# Arquitectura

Patrones de arquitectura de software para sistemas distribuidos: cómo se organizan las APIs
entre servicios y cómo se resiste a las fallas de una dependencia.

Las herramientas y prácticas de quien escribe el código (Git, YAML, configuración, pruebas de
API) están en el Mapa de [Desarrollo](../Desarrollo/desarrollo.md). Cómo una plataforma interna expone sus capacidades
está en [Plataforma API-first](../Platform-Engineering/plataforma-api-first.md), en Platform-Engineering.

## Organización de APIs

- [API-led connectivity](api-led-connectivity.md) — las capas System, Process y Experience; leerla primero si se diseña
  un sistema con varios servicios.
- [Multi-tenancy](multi-tenancy.md) — servir a varios clientes desde una misma instancia sin mezclar sus datos;
  leerla antes de diseñar el modelo de datos de un SaaS.

## Resiliencia ante fallas

- [Circuit breaker](circuit-breaker.md) — cortar las llamadas a una dependencia que viene fallando; la base de las
  dos siguientes.
- [Degradación controlada](degradacion-controlada.md) — qué devolver cuando una dependencia falla, según sea una lectura o
  un comando crítico; leerla antes de escribir un fallback.
- [Proteger un cliente HTTP con Resilience4j en Spring Boot](resilience4j-en-spring-boot.md) — pasos para proteger un cliente HTTP con circuit breaker,
  retry y fallback, en un servicio Java.

## Consistencia entre servicios

- [Saga](saga.md) — una secuencia de transacciones locales con compensaciones; leerla cuando una
  operación toca varios servicios con base propia y no cabe en una transacción.
- [Clave de idempotencia](clave-de-idempotencia.md) — reintentar una operación sin repetir su efecto; leerla al diseñar
  cualquier `POST` que el cliente pueda reintentar, como un pago.

## Originales archivados

Los documentos de diseño de un MVP de e-commerce multi-tenant, de los que salen varias de estas
notas, están sin cambios en `Archivo/Arquitectura/` (`mvp-ecommerce-arquitectura.md` y
`circuit-breaking-resilience4j.md`). Son de un proyecto propio, cuyo frontend está en el repo
`SmallTechCo/ventos-ecommerce-front`.
