---
resumen: >-
  Mensajería es la parte de Cloud que lleva órdenes, flujos de eventos y avisos entre sistemas para
  que no se llamen directamente.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Mensajería

Mensajería es la parte de Cloud que lleva órdenes, flujos de eventos y avisos entre sistemas para
que no se llamen directamente.

Dentro de [Cloud](../cloud.md), la mensajería desacopla las piezas del
[cómputo](../Computo/computo.md): un aviso dispara una función, una orden la procesa un worker y
la telemetría se junta para análisis. El patrón por eventos de las
[arquitecturas de referencia](../arquitecturas-de-referencia-en-azure.md) se arma con ella.

## Qué representa el mensaje

La pregunta que decide es qué representa el mensaje: una orden que hay que cumplir, un flujo de
datos o un aviso de que algo cambió. Cada respuesta lleva a un servicio distinto, y elegir mal se
nota tarde: un pedido que se procesa dos veces, una telemetría que satura una cola o un evento que
nadie recibe. Los tres servicios entregan al menos una vez, así que el consumidor tiene que tolerar
duplicados.

## La nota de mensajería

- [Mensajería en Azure](mensajeria-en-azure.md) — Service Bus, Event Hubs y Event Grid: qué garantiza cada uno, cuánto volumen maneja y cómo se combinan.
