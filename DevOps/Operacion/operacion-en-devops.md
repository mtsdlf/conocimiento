---
resumen: >-
  La operación es la parte de DevOps que trata cómo se entiende lo que corre en producción: la
  telemetría que emite cada sistema y la práctica de definirla junto con cada cambio.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenTelemetry, Observability primer: https://opentelemetry.io/docs/concepts/observability-primer/"
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), sección 2.2.2 y cap. 5: https://livebook.manning.com/book/effective-platform-engineering/chapter-5"
aliases: [Operación de la plataforma, Operaciones]
creado: 2026-11-19
revisado:
---

# Operación

La operación es la parte de DevOps que trata cómo se entiende lo que corre en producción: la
telemetría que emite cada sistema y la práctica de definirla junto con cada cambio.

Dentro de [DevOps](../devops.md), empieza donde termina el [Despliegue](../Despliegue/despliegue.md):
lo que llega a producción se observa acá, y las fallas que se ven alimentan el
[postmortem sin culpa](../Cultura-y-medicion/postmortem-sin-culpa.md) y las
[métricas DORA](../Cultura-y-medicion/metricas-dora.md) de [Cultura y medición](../Cultura-y-medicion/cultura-y-medicion.md).
En una organización con platform team, Effective Platform Engineering propone ofrecer la
observabilidad como una [capacidad de la plataforma](../../Platform-Engineering/Plataforma-interna/capacidad-de-plataforma.md),
para que cada equipo arme sus alertas y tableros por
[self-service](../../Platform-Engineering/Plataforma-interna/self-service.md). Cómo se observa una
nube concreta está en la [operación en Azure](../../Cloud/Operacion/operacion.md).

## De la telemetría al criterio de aceptación

Un sistema es observable cuando se lo puede entender desde afuera con sus métricas, logs y traces,
incluso ante fallas que nadie anticipó; el monitoreo cubre las previstas. Observability-driven
development lleva eso al backlog: un ítem no está terminado hasta que su comportamiento se ve en
la observabilidad del sistema, y el presupuesto de error decide cuándo frenar para estabilizar.

## Qué hay adentro de operación

- [Observabilidad](observabilidad.md) — qué permite entender un sistema desde sus métricas, logs y traces, y en qué se diferencia del monitoreo. Leerla primero.
- [Observability-driven development](observability-driven-development.md) — cómo hacer de la telemetría y las alertas un criterio de aceptación de cada ítem del backlog.
