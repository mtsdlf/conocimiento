---
resumen: >-
  Las versiones de la especificación de MCP desde 2024, con lo que cambió en cada una, quién
  gobierna el protocolo y las cifras de adopción publicadas, copiado el 2026-11-27.
estado: borrador
estabilidad: volatil
fuentes:
  - https://modelcontextprotocol.io/specification/latest
  - https://modelcontextprotocol.io/specification/latest/changelog
  - https://modelcontextprotocol.io/specification/2025-11-25/changelog
  - https://modelcontextprotocol.io/specification/2025-06-18/changelog
  - https://modelcontextprotocol.io/specification/2025-03-26/changelog
  - https://www.anthropic.com/news/model-context-protocol
  - https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
aliases: [historia de MCP, MCP specification versions, versiones de la especificación de MCP]
creado: 2026-11-27
revisado:
---

# Versiones de MCP

Las versiones de la especificación de MCP desde 2024, con lo que cambió en cada una, quién
gobierna el protocolo y las cifras de adopción publicadas, copiado el 2026-11-27.

Implementa el protocolo descrito en [Uso de herramientas](uso-de-herramientas.md#mcp-escribir-la-herramienta-una-vez).
La fuente viva es la [especificación vigente](https://modelcontextprotocol.io/specification/latest)
y su [registro de cambios](https://modelcontextprotocol.io/specification/latest/changelog); cada
versión anterior tiene el suyo en `specification/<versión>/changelog`.

## Las versiones de la especificación

La especificación se versiona por fecha. Copiado de los registros de cambios el 2026-11-27:

| Versión | Qué cambió (los cambios mayores, resumidos) |
|---|---|
| 2024-11-05 | Primera versión pública. Anthropic anunció el protocolo el 2024-11-25. |
| 2025-03-26 | Marco de autorización basado en OAuth 2.1; el transporte HTTP+SSE se reemplaza por "Streamable HTTP"; se suma el envío de mensajes JSON-RPC en lote; anotaciones de herramientas que dicen, por ejemplo, "whether it is read-only or destructive"; audio como tipo de contenido. |
| 2025-06-18 | Se quita el envío en lote; salida estructurada de herramientas; los servidores pasan a ser *OAuth Resource Servers* y los clientes tienen que usar Resource Indicators (RFC 8707) "to prevent malicious servers from obtaining access tokens"; nueva página de buenas prácticas de seguridad; *elicitation* (el servidor le pide un dato al usuario); enlaces a recursos en los resultados. |
| 2025-11-25 | Íconos en herramientas y recursos; consentimiento de permisos por etapas; guía para nombrar herramientas; *elicitation* por URL; el muestreo puede usar herramientas; registro de clientes por *Client ID Metadata Documents*; tareas experimentales (pedidos durables con consulta periódica); los errores de validación de argumentos vuelven como errores de la herramienta "to enable model self-correction"; JSON Schema 2020-12 como dialecto por defecto; estructura de gobierno formal. |
| 2026-07-28 (vigente) | El protocolo pasa a ser sin estado: se quitan las sesiones y el saludo inicial (`initialize`), y cada pedido lleva su versión y las capacidades del cliente; nuevo `server/discover` para anunciar versiones y capacidades; suscripciones por un único flujo; las tareas salen del núcleo a una extensión oficial; patrón de pedidos de varias vueltas (*Multi Round-Trip Requests*) en lugar de pedidos iniciados por el servidor; los servidores "SHOULD return tools from `tools/list` in a deterministic order" para mejorar el acierto del cache de prompts; se declaran obsoletas las funciones Roots, Sampling y Logging, con una ventana mínima de doce meses antes de quitarlas. |

La especificación vigente define como extensiones opcionales Tasks, Skills over MCP y MCP Apps
(interfaces interactivas dentro de la conversación).

## Quién gobierna el protocolo

| Fecha | Hecho | Fuente |
|---|---|---|
| 2024-11-25 | Anthropic anuncia MCP como estándar abierto | anuncio de Anthropic |
| 2025-11-25 | La especificación formaliza su estructura de gobierno, grupos de trabajo y niveles de SDK | registro de cambios 2025-11-25 |
| 2025-12-09 | Anthropic dona MCP a la Agentic AI Foundation, "a directed fund under the Linux Foundation", "co-founded by Anthropic, Block and OpenAI" | anuncio de Anthropic |

## Cifras de adopción

Según Anthropic, al 2025-12-09: "more than 10,000 active public MCP servers" y "97M+ monthly SDK
downloads across Python and TypeScript", con clientes como "ChatGPT, Cursor, Gemini, Microsoft
Copilot, Visual Studio Code". Son cifras de la parte interesada; la Linux Foundation repite la misma
cifra de servidores, así que no es una segunda fuente.

> [!NOTE]
> Sin fuente todavía: una medición independiente de la adopción de MCP.
