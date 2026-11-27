---
resumen: >-
  Service-based es el estilo que parte el sistema por dominio en unos pocos servicios grandes,
  desplegados por separado y que suelen compartir la base de datos. Es el escalón intermedio entre el
  monolito modular y los microservicios.
estado: vigente
estabilidad: semi
fuentes:
  - "Mark Richards y Neal Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), índice: https://nealford.com/books/SAF2e.html"
aliases: [service-based architecture, arquitectura basada en servicios]
creado: 2026-11-27
revisado: 2026-11-27
---

# Service-based

Service-based es el estilo que parte el sistema por dominio en unos pocos servicios grandes, desplegados por separado y que suelen compartir la base de datos. Es el escalón intermedio entre el monolito modular y los microservicios.

> [!NOTE]
> Sin fuente todavía: Richards y Ford lo tratan como estilo propio en la 2ª edición (2025), pero solo se leyó el índice. Que los servicios sean pocos y que compartan la base es lo que la investigación recogió como rasgo del canon, sin la página que lo diga; falta leer el capítulo.

## Pocos servicios grandes sobre una base compartida

Un sistema service-based toma los módulos de dominio de un [monolito modular](monolito-modular.md) y los despliega como unos pocos servicios, cada uno con un área de negocio entera (pedidos, catálogo, facturación). A diferencia de los [microservicios](microservicios.md), los servicios no son chicos ni tienen cada uno su base: lo habitual es que compartan una.

Compartir la base es lo que lo abarata. Las transacciones que cruzan dominios siguen siendo locales a la base y no hace falta una [saga](../Sistemas-distribuidos/saga.md) ni un [outbox](../Sistemas-distribuidos/outbox.md) para cada operación que toca dos servicios. A cambio, el esquema de la base acopla a los servicios: un cambio de tabla puede obligar a desplegar varios a la vez. Ese razonamiento es de esta base, no de la fuente.

## Por qué es el escalón natural

Con la regla de [empezar simple](../Decisiones/empezar-simple.md), cada paso hacia la distribución tiene que estar justificado por una característica que el paso anterior no cumple. Service-based permite desplegar y escalar por separado unas pocas áreas sin pagar todavía el costo entero de los microservicios: muchos servicios, muchas bases, consistencia eventual. La investigación lo propuso como escalón entre el monolito modular y los microservicios, y así lo usa el tema; es una lectura de esta base sobre el canon.

Para pasar de un monolito a servicios grandes se usa el mismo mecanismo que para cualquier migración, el [strangler fig](strangler-fig.md). Cómo decidir si hace falta está en [Elegir un estilo](elegir-un-estilo.md).

Para leer más: el capítulo de service-based de Richards y Ford (2ª ed.), fijándose en cuántos servicios recomienda, cómo trata la base compartida y cómo califica el estilo frente a los microservicios.
