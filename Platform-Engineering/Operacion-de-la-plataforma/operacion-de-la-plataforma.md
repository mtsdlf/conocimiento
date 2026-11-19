---
resumen: >-
  La operación de la plataforma es la parte del platform engineering que trata cómo se entiende lo
  que corre en producción: la telemetría que emite cada sistema y la práctica de definirla junto
  con cada cambio.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenTelemetry, Observability primer: https://opentelemetry.io/docs/concepts/observability-primer/"
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), sección 2.2.2 y cap. 5: https://livebook.manning.com/book/effective-platform-engineering/chapter-5"
creado: 2026-11-19
revisado:
---

# Operación de la plataforma

La operación de la plataforma es la parte del platform engineering que trata cómo se entiende lo
que corre en producción: la telemetría que emite cada sistema y la práctica de definirla junto
con cada cambio.

Effective Platform Engineering propone ofrecer la observabilidad como una
[capacidad de la plataforma](../Plataforma-interna/capacidad-de-plataforma.md), y que cada equipo
arme sus alertas y tableros por [self-service](../Plataforma-interna/self-service.md). Un
[golden path](../Plataforma-interna/golden-path.md) que trae la telemetría conectada de fábrica
cumple buena parte de lo que pide observability-driven development.

## De la telemetría al criterio de aceptación

Un sistema es observable cuando se lo puede entender desde afuera con sus métricas, logs y traces,
incluso ante fallas que nadie anticipó; el monitoreo cubre las previstas. Observability-driven
development lleva eso al backlog: un ítem no está terminado hasta que su comportamiento se ve en
la observabilidad del sistema, y el presupuesto de error decide cuándo frenar para estabilizar.

## Las dos notas de operación

- [Observabilidad](observabilidad.md) — qué permite entender un sistema desde sus métricas, logs y traces, y en qué se diferencia del monitoreo. Leerla primero.
- [Observability-driven development](observability-driven-development.md) — cómo hacer de la telemetría y las alertas un criterio de aceptación de cada ítem del backlog.
