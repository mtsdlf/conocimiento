---
resumen: >-
  El uso de herramientas (function calling) es el mecanismo por el que un modelo pide ejecutar una
  función que la aplicación declaró: el modelo emite la llamada con sus argumentos y la aplicación
  la ejecuta y le devuelve el resultado. MCP es el protocolo abierto que estandariza cómo se
  ofrecen esas herramientas.
estado: borrador
estabilidad: semi
fuentes:
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
  - https://developers.openai.com/api/docs/guides/function-calling
  - https://www.anthropic.com/engineering/writing-tools-for-agents
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://huyenchip.com/2025/01/07/agents.html
  - https://www.anthropic.com/news/model-context-protocol
  - https://modelcontextprotocol.io/specification/latest
  - https://modelcontextprotocol.io/specification/latest/changelog
  - https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
  - https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
aliases: [tool use, function calling, llamada a funciones, llamadas a herramientas, tool calling, MCP, Model Context Protocol]
creado: 2026-11-27
revisado:
---

# Uso de herramientas

El uso de herramientas (function calling) es el mecanismo por el que un modelo pide ejecutar una
función que la aplicación declaró: el modelo emite la llamada con sus argumentos y la aplicación
la ejecuta y le devuelve el resultado. MCP es el protocolo abierto que estandariza cómo se
ofrecen esas herramientas.

Es lo que convierte un modelo que solo escribe texto en un [agente](agente.md) que actúa. Las tres
clases de herramientas de Huyen (las que agregan conocimiento, las que extienden capacidad y las
acciones de escritura) están en [Agente](agente.md#herramientas-planificación-y-las-acciones-de-escritura);
acá va el mecanismo, el diseño y el protocolo.

## El modelo emite la llamada, la aplicación la ejecuta

El modelo no ejecuta nada. La documentación de Anthropic lo define así: "Tool use (also called
function calling) lets Claude call functions that you define or that Anthropic provides", y la de
OpenAI describe el mismo circuito con otros nombres de campo. El viaje de ida y vuelta tiene cuatro
pasos:

1. La aplicación manda el pedido con la lista de herramientas: cada una con nombre, descripción y
   un esquema JSON de sus parámetros.
2. El modelo, en lugar de contestar, emite un bloque estructurado con el nombre de la herramienta y
   los argumentos, y corta la respuesta ahí.
3. La aplicación ejecuta la función con esos argumentos, en su propio código y con sus permisos.
4. La aplicación devuelve el resultado al modelo como un mensaje más, y el modelo sigue: contesta o
   pide otra herramienta.

Un agente es ese circuito repetido hasta que el modelo deja de pedir herramientas. Cuántas vueltas
da y en qué orden lo decide el modelo; en un [workflow](patrones-de-flujo.md) lo decide el código.
Que la ejecución quede del lado de la aplicación es lo que permite poner controles en el paso 3:
validar los argumentos, pedir aprobación humana o negar la acción (ver
[Fallas de agentes](fallas-de-agentes.md#qué-puede-romper-un-agente-que-actúa)).

Las dos documentaciones ofrecen además cómo forzar el comportamiento: que el modelo elija solo,
que tenga que usar alguna herramienta, que use una en particular o que no use ninguna (en OpenAI,
el parámetro `tool_choice`).

## Esquema estricto y argumentos inventados

La llamada es texto generado, así que puede salir mal formada. Los dos proveedores ofrecen un modo
estricto que garantiza que los argumentos respeten el esquema: Anthropic pide agregar
`strict: true` "to ensure Claude's tool calls always match your schema exactly", y OpenAI exige
además que el esquema no admita propiedades extra y que todas las propiedades sean obligatorias. Es
la misma técnica que las [salidas estructuradas](../Modelos/muestreo.md): restringir lo que el
modelo puede emitir.

El modo estricto garantiza la forma, no el contenido. Ante un parámetro obligatorio que el usuario
no dio, la documentación de Anthropic advierte que el modelo puede preguntar, "But it might also
infer a reasonable value": un argumento inventado con forma correcta es una
[alucinación](../Modelos/alucinacion.md) que entra al sistema como dato. Por eso la validación de
los argumentos va en la aplicación, no en el esquema (lectura de esta base).

## Una herramienta también es un prompt

El nombre, la descripción y el esquema de cada herramienta entran en la
[ventana de contexto](../Contexto/ingenieria-de-contexto.md) en cada llamada: se cobran como tokens
de entrada y el modelo los lee para decidir. Anthropic suma además un prompt de sistema propio para
el uso de herramientas, de cientos de tokens según el modelo. Por eso Anthropic pide para las
definiciones de herramientas tanta ingeniería como para el [prompt](../Contexto/prompt.md):
"Carefully craft your agent-computer interface (ACI) through thorough tool documentation and
testing".

"Tools are a new kind of software which reflects a contract between deterministic systems and
non-deterministic agents", escribe Anthropic ("Writing effective tools for agents", 2025-09-11).
De ese texto y de "Building effective agents" (2024-12) salen estas reglas de diseño:

| Regla | Qué dice la fuente |
|---|---|
| Pocas herramientas de alto impacto | "More tools don't always lead to better outcomes"; evitar "tools that merely wrap existing software functionality or API endpoints" |
| Nombres agrupados | "Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools" |
| Respuestas cortas y legibles | paginar, filtrar y truncar; el agente de código de Anthropic limita las respuestas de herramientas a 25.000 tokens por defecto |
| Errores que dicen qué corregir | que "clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks" |
| Parámetros que no se pueden malinterpretar | "instead of a parameter named `user`, try a parameter named `user_id`" |
| Diseño a prueba de errores (*poka-yoke*) | en SWE-bench, cambiar la herramienta para que "always require absolute filepaths" eliminó los errores con rutas relativas |

Cuántas herramientas son demasiadas no tiene un número firme. La guía de OpenAI sugiere, como
orientación, "fewer than 20 functions available at the start of a turn", y los dos proveedores
ofrecen una búsqueda de herramientas para cargar solo las que la tarea pide.

## MCP: escribir la herramienta una vez

MCP (Model Context Protocol) estandariza cómo una aplicación descubre y llama herramientas que
escribió otro. Anthropic lo anunció en noviembre de 2024 con el problema que ataca: "Every new data
source requires its own custom implementation". Sin un protocolo, cada aplicación reimplementa cada
integración; con él, un servidor MCP sirve a cualquier aplicación que hable el protocolo. Se
inspira en el Language Server Protocol, que hizo lo mismo con los lenguajes de programación en los
editores.

La especificación define tres roles, con mensajes en JSON-RPC 2.0:

- **Host**: la aplicación que aloja al modelo e inicia las conexiones.
- **Cliente**: el conector, dentro del host, que habla con un servidor.
- **Servidor**: el servicio que ofrece *tools* ("Functions for the AI model to execute"),
  *resources* (datos y contexto) y *prompts* (plantillas para el usuario).

El cliente, a su vez, puede ofrecerle al servidor *elicitation*: que el servidor le pida un dato
al usuario en medio de una operación. Una herramienta MCP es, para el modelo, una herramienta más:
termina en el mismo circuito de cuatro pasos. Lo que MCP cambia es quién la escribe y dónde corre.

El protocolo cambió mucho en dos años. La versión vigente al 2026-11-27 es la 2026-07-28, que lo
volvió sin estado: cada pedido lleva su versión de protocolo y las capacidades del cliente, en lugar
de negociarlas una vez al abrir la sesión. La historia de versiones, el traspaso a una fundación y
las cifras de adopción están en la ficha [Versiones de MCP](versiones-de-mcp.md).

## Lo que conectar una herramienta le abre al sistema

La especificación de MCP lo dice sin rodeos: "Tools represent arbitrary code execution and must be
treated with appropriate caution", y las descripciones de las herramientas "should be considered
untrusted, unless obtained from a trusted server". También pide que el host obtenga "explicit user
consent before invoking any tool", y admite su límite: "MCP itself cannot enforce these security
principles at the protocol level". La seguridad queda en manos de quien implementa el host.

Dos riesgos salen del mecanismo mismo:

- **El resultado de una herramienta entra al contexto.** Una página, un mail o un documento que
  trae una herramienta puede contener instrucciones hostiles; es la
  [inyección de prompt](../Contexto/inyeccion-de-prompt.md). Willison (2025-06-16) llama "trifecta
  letal" a juntar en un agente acceso a datos privados, contenido no confiable y una salida al
  exterior, y advierte que MCP "encourages users to mix and match tools from different sources".
- **Cada herramienta suma poder.** OWASP (LLM06:2025, *Excessive Agency*) pone la causa en la
  funcionalidad, los permisos y la autonomía excesivos. Las defensas (mínimo privilegio, aprobación
  humana, autorización en el sistema de destino) están en
  [Fallas de agentes](fallas-de-agentes.md#qué-puede-romper-un-agente-que-actúa).

Una herramienta de escritura que el agente puede reintentar necesita además una
[clave de idempotencia](../../Arquitectura/Sistemas-distribuidos/clave-de-idempotencia.md), porque
el modelo puede repetir una llamada que ya se ejecutó.

## Qué leer sobre herramientas

Para el mecanismo, la documentación ["Tool use with Claude"](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview):
el circuito completo sirve aunque se use otro proveedor, porque la forma es la misma. Para el
diseño, ["Writing effective tools for agents"](https://www.anthropic.com/engineering/writing-tools-for-agents)
entero: fijarse en por qué no conviene envolver cada endpoint. Para MCP, la
[especificación](https://modelcontextprotocol.io/specification/latest), su resumen y la sección
"Security and Trust & Safety", antes que el anuncio.

> [!NOTE]
> Sin fuente todavía: el capítulo de Huyen sobre herramientas (cap. 6, p. 278), la documentación
> de function calling de Google y un estudio con método sobre incidentes reales con servidores MCP
> (herramientas con descripciones envenenadas).
