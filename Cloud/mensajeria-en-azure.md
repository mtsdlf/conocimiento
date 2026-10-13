---
tipo: concepto
resumen: >-
  Azure tiene tres servicios de mensajería: Service Bus para mensajes de negocio confiables, Event
  Hubs para streaming de muchos eventos y Event Grid para reaccionar a cambios; se diferencian en
  qué garantizan y en cuánto volumen manejan.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Compare Azure messaging services: https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Integración y SB vs EH vs EG)"
aliases: [Service Bus, Event Hubs, Event Grid, mensajería en Azure, colas en Azure]
parte_de: []
requiere: []
relacionado: []
---

# Mensajería en Azure

Azure tiene tres servicios de mensajería: Service Bus para mensajes de negocio confiables, Event
Hubs para streaming de muchos eventos y Event Grid para reaccionar a cambios; se diferencian en
qué garantizan y en cuánto volumen manejan.

## Por qué importa

Los tres "mandan mensajes", y elegir mal se nota tarde: un pedido que se procesa dos veces, una
telemetría que satura una cola, o un evento que nadie recibe. La pregunta que decide es qué
representa el mensaje: una orden que hay que cumplir, un flujo de datos o un aviso de que algo
cambió.

## Cómo funciona

| | Service Bus | Event Hubs | Event Grid |
|---|---|---|---|
| **Para qué** | Mensajería transaccional entre sistemas | Streaming de grandes volúmenes | Ruteo reactivo de eventos discretos |
| **El mensaje es** | Una orden ("cobrá este pedido") | Un dato de una serie (telemetría, logs) | Un aviso ("se creó un blob") |
| **Orden** | FIFO con sesiones | Por partición | Sin garantía |
| **Extras** | Transacciones, detección de duplicados, dead-letter | Consumer groups, Capture a Storage, protocolo Kafka | Filtros, fan-out a muchos suscriptores, MQTT |
| **Protocolos** | AMQP, HTTP | AMQP, Kafka, HTTP | MQTT, HTTP |

Los tres entregan *al menos una vez*: el consumidor tiene que tolerar duplicados. La detección de
duplicados de Service Bus descarta los reenvíos del productor, no las entregas repetidas al consumidor.

**Se combinan**: Event Grid avisa que llegó un archivo, una función lo lee y publica una orden en
Service Bus para que la procese un worker; la telemetría del worker va a Event Hubs.

## Ejemplo

Una plataforma de delivery usa Service Bus para los pedidos (una sesión por pedido mantiene el
orden de sus estados), Event Hubs para la posición GPS de los repartidores (miles por segundo,
leídas por análisis y por el mapa en vivo) y Event Grid para disparar el procesamiento cuando se
sube la foto de una entrega.

## No confundir con

API Management: un gateway para APIs HTTP síncronas, con políticas de throttling, autenticación y
versionado. No guarda mensajes.

## Relaciones

- La usa: [[arquitecturas-de-referencia-en-azure]] — el patrón por eventos combina los tres.
- La usa: [[azure-functions]] — los tres son disparadores comunes de una función.
