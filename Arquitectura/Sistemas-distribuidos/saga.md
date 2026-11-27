---
resumen: >-
  Una saga reemplaza una transacción distribuida por una secuencia de transacciones locales, cada
  una con una acción que la compensa si un paso posterior falla.
estado: vigente
estabilidad: estable
fuentes:
  - "Hector Garcia-Molina y Kenneth Salem, Sagas, SIGMOD 1987: https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf"
  - "Chris Richardson, Pattern: Saga, microservices.io: https://microservices.io/patterns/data/saga.html"
  - "Archivo/Arquitectura/mvp-ecommerce-arquitectura.md (original, texto generado con IA)"
  - "Archivo/Arquitectura/circuit-breaking-resilience4j.md (original)"
aliases: [Patrón saga, Saga pattern, Transacción compensable]
creado: 2026-10-03
revisado: 2026-11-27
---

# Saga

Una saga reemplaza una transacción distribuida por una secuencia de transacciones locales, cada
una con una acción que la compensa si un paso posterior falla.

## Por qué una compra entre servicios no cabe en una transacción

Cuando cada servicio tiene su propia base, una compra que reserva stock, cobra y crea el pedido
no cabe en una sola transacción ACID. Un commit en dos fases entre servicios bloquea recursos y
depende de que todos estén disponibles a la vez. La saga acepta que los pasos se confirmen por
separado y define cómo volver atrás. Garcia-Molina y Salem la describieron en 1987 para
transacciones largas dentro de una base de datos; Chris Richardson la adaptó a microservicios.

## Compensaciones, coreografía y orquestación

Cada paso es una transacción local que se confirma e informa su resultado. Si un paso falla, la
saga ejecuta, en orden inverso, la **compensación** de cada paso ya confirmado: una operación
nueva que deshace su efecto de negocio (cancelar una reserva, reembolsar un cobro). Una
compensación no borra el pasado: el reembolso queda registrado.

Hay dos formas de coordinarla, según microservices.io:

- **Coreografía**: cada servicio escucha los eventos del anterior y decide su paso. No hay un
  coordinador, pero el flujo queda repartido entre servicios.
- **Orquestación**: un orquestador (por ejemplo, un servicio de checkout) le dice a cada servicio qué
  hacer y lleva el estado. El flujo se lee en un solo lugar.

Una saga no tiene aislamiento: otro proceso puede ver el stock reservado antes de que la compra
termine. Los pasos y las compensaciones tienen que ser idempotentes, porque se reintentan ante
fallas de red, y eso lo resuelve una [clave de idempotencia](clave-de-idempotencia.md).

## Un checkout orquestado

Un checkout orquestado: (1) reservar stock con vencimiento, (2) crear el intento de pago,
(3) crear el pedido, (4) confirmar el pago y comprometer el stock. Si el paso 3 falla, el
orquestador cancela el intento de pago y libera la reserva. Si el proveedor de pagos no responde,
el pago queda pendiente y un proceso en segundo plano lo resuelve después.

## Compensación no es rollback

El rollback de una base de datos descarta cambios que nadie más vio; una
compensación es una operación de negocio nueva sobre cambios que ya se confirmaron.

## Ver también

- [Circuit breaker](circuit-breaker.md): una dependencia con el breaker abierto es una de las fallas que disparan compensaciones.
- [Degradación controlada](degradacion-controlada.md): decide si un paso fallido aborta la saga o queda pendiente.
- [Outbox](outbox.md): cada paso confirma su transacción local y publica su resultado; el outbox evita perder o inventar ese evento.
- [Event-driven](../Estilos/event-driven.md): coreografía y orquestación corresponden a las topologías broker y mediator.
