---
resumen: >-
  Observability-driven development (ODD) extiende TDD a la operación: cada ítem del backlog
  incluye, como criterio de aceptación, la telemetría y las alertas que muestran qué hace el
  software en producción.
estado: borrador
estabilidad: estable
fuentes:
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), sección 2.2.2, Observability-driven development: https://livebook.manning.com/book/effective-platform-engineering/chapter-2"
aliases: [ODD, Observability-driven design, Desarrollo guiado por observabilidad]
creado: 2026-10-03
revisado:
---

# Observability-driven development

Observability-driven development (ODD) extiende TDD a la operación: cada ítem del backlog
incluye, como criterio de aceptación, la telemetría y las alertas que muestran qué hace el
software en producción.

En TDD (test-driven development) se escribe el test antes que el código; en ODD se define antes
cómo se va a ver el código funcionando.

## Lo que los tests no muestran

Un cambio que pasa todos sus tests todavía puede fallar en producción, y si no emite datos nadie
se entera hasta que se queja un usuario. Effective Platform Engineering propone ODD para que el
equipo de plataforma sepa en todo momento qué hace el software nuevo.

## Los cinco principios de ODD

ODD suma un criterio de aceptación a todo el trabajo del backlog: el ítem no está terminado
hasta que su comportamiento se ve en la [Observabilidad](observabilidad.md) del sistema. El libro resume la
práctica en cinco principios:

1. **Instrumentación como código**: las métricas, los logs y los traces se escriben con el
   código, en el mismo cambio, no en una tarea aparte.
2. **Contexto y trazas**: los datos llevan contexto suficiente, y los traces distribuidos siguen
   un pedido entre servicios para ubicar rápido dónde está un problema.
3. **Métricas y logs accionables**: se eligen pocas métricas que digan algo sobre salud,
   rendimiento y errores, y logs estructurados que se puedan consultar.
4. **Alertas automáticas y monitoreo self-service**: cada equipo arma sus tableros y alertas sin
   depender de un equipo central.
5. **Mejora continua con feedback**: los datos se usan para encontrar causas de fondo, y el
   presupuesto de error (error budget: cuánta falla tolera el objetivo de confiabilidad en un
   período) decide cuándo seguir sumando funciones y cuándo frenar para estabilizar.

## La historia de pagar con transferencia

La historia "pagar con transferencia" trae sus criterios funcionales y, además, estos de
observabilidad: una métrica de pagos por transferencia con éxito y con error, un span propio
dentro del trace del checkout, un log estructurado con el ID del pago y una alerta si los
errores pasan del 2 % en 10 minutos. La historia se cierra cuando todo eso se ve en staging.

## ODD y TDD

Un test prueba antes del despliegue que el código hace lo esperado en casos conocidos; ODD
deja preparado lo necesario para ver qué hace después del despliegue, con usuarios y datos
reales. ODD no reemplaza los tests.

## Ver también

- [Golden path](../../Platform-Engineering/Plataforma-interna/golden-path.md): una plantilla que trae la telemetría conectada de fábrica cumple buena parte de ODD sin esfuerzo extra.
- [Self-service](../../Platform-Engineering/Plataforma-interna/self-service.md): el cuarto principio pide que cada equipo cree sus alertas y tableros sin ticket.
