---
resumen: >-
  La observabilidad es cuánto permiten los datos que emite un sistema (métricas, logs y traces)
  entender qué está haciendo y por qué, incluso ante fallas que nadie anticipó.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenTelemetry, Observability primer: https://opentelemetry.io/docs/concepts/observability-primer/"
  - "Charity Majors, Observability — A Manifesto, Honeycomb: https://www.honeycomb.io/blog/observability-a-manifesto"
  - "Rob Ewaschuk, Monitoring Distributed Systems, en Site Reliability Engineering (Google): https://sre.google/sre-book/monitoring-distributed-systems/"
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), cap. 5, Evolutionary observability: https://livebook.manning.com/book/effective-platform-engineering/chapter-5"
aliases: [Observability, O11y, Telemetría]
creado: 2026-10-03
revisado:
---

# Observabilidad

La observabilidad es cuánto permiten los datos que emite un sistema (métricas, logs y traces)
entender qué está haciendo y por qué, incluso ante fallas que nadie anticipó.

## Las fallas que nadie anticipó

Un sistema distribuido falla de formas nuevas: una combinación de versión, región y tipo de
cliente que nunca se probó. OpenTelemetry llama a esas fallas "unknown unknowns". Con buena
observabilidad, la causa se encuentra haciendo preguntas a los datos que ya existen, sin
desplegar código nuevo para medir.

## Métricas, logs y traces

Según OpenTelemetry, un sistema es observable cuando se lo puede entender desde afuera, sin
conocer su funcionamiento interno. Para eso tiene que estar **instrumentado**: emitir
**telemetría**, que llega en tres señales principales.

| Señal | Qué es | Responde |
|---|---|---|
| **Métrica** | un número agregado en el tiempo (pedidos por segundo, latencia p99) | ¿algo cambió y cuánto? |
| **Log** | un mensaje con fecha y hora que emite un componente | ¿qué pasó en ese momento? |
| **Trace** | el camino de un pedido a través de los servicios, hecho de **spans** (una operación cada uno) | ¿dónde se fue el tiempo o dónde falló? |

Las señales rinden más cuando comparten contexto: si cada log lleva el ID del trace, de la
métrica que se disparó se pasa al pedido concreto y de ahí a sus logs. OpenTelemetry es el
estándar abierto de la CNCF (Cloud Native Computing Foundation) para instrumentar y transportar las tres señales sin atarse a un
proveedor.

Sobre la telemetría se definen los **SLI** (una medida del servicio desde el punto de vista del
usuario) y los **SLO** (el objetivo para esa medida), que convierten los datos en confiabilidad
acordada.

## La latencia p99 del checkout

La latencia p99 del checkout (la que no supera el 99 % de los pedidos) sube de 300 ms a 2 s, pero solo para algunos usuarios. La métrica
muestra cuándo empezó. Los traces de los pedidos lentos tienen en común un span al servicio de
pagos de una región. Los logs de esos spans muestran reintentos contra un proveedor externo.

## Observabilidad y monitoreo

Google define monitoreo como juntar, procesar, agregar y mostrar datos cuantitativos
del sistema en tiempo real. Según Charity Majors, el monitoreo cubre los problemas previstos, con
tableros y alertas armados de antemano; la observabilidad permite investigar los que nadie
previó. El monitoreo es una de las cosas que se hacen con la telemetría.

## Ver también

- [Observability-driven development](observability-driven-development.md): la práctica que pide definir la telemetría junto con cada cambio.
- [Capacidad de plataforma](../Plataforma-interna/capacidad-de-plataforma.md): Effective Platform Engineering propone ofrecer la observabilidad como una capacidad de la plataforma.
