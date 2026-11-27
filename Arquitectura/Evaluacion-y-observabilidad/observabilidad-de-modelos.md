---
resumen: >-
  La observabilidad de un sistema con un modelo es registrar cada consulta con su entrada, su
  salida y sus pasos intermedios, más las métricas del modelo y del sistema, para poder seguir qué
  le pasó a cada consulta y de dónde vino una falla.
estado: borrador
estabilidad: semi
fuentes:
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://opentelemetry.io/docs/specs/semconv/gen-ai/
  - https://github.com/open-telemetry/semantic-conventions-genai
  - https://hamel.dev/blog/posts/evals/
aliases: [observability, monitoreo, monitoring, trazas de LLM]
creado: 2026-11-27
revisado:
---

# Observabilidad

La observabilidad de un sistema con un modelo es registrar cada consulta con su entrada, su salida y
sus pasos intermedios, más las métricas del modelo y del sistema, para poder seguir qué le pasó a
cada consulta y de dónde vino una falla.

Es el comienzo del [bucle](evaluacion-y-observabilidad.md): sin trazas no hay
[análisis de errores](analisis-de-errores.md), y sin análisis de errores la
[evaluación](evaluacion.md) mide a ciegas. En Huyen es una sección del capítulo 10, "Monitoring and
Observability", junto a la arquitectura del sistema. Según ella, importa en proyectos de cualquier
tamaño, y más cuanto más complejo es el sistema.

## Log everything: métricas, logs y trazas

Huyen separa tres cosas. Las métricas resumen: del modelo ("accuracy, toxicity, and hallucination
rate") y del sistema (latencia, costo, errores, que se ven en
[costo y latencia](../Caracteristicas/costo-y-latencia.md)). Los logs guardan cada evento. Las
trazas unen los eventos de una misma consulta.

Su regla para los logs es amplia: "The philosophy for logging is simple: log everything." Y
concreta: "Log the query, the output, and the intermediate outputs." Lo intermedio es lo que
distingue a un sistema con modelos de un servicio web común: el contexto recuperado, el prompt
armado, la elección del [router](../Sistemas-con-modelos/router-y-gateway-de-modelos.md), si
respondió la [cache](../Sistemas-con-modelos/cache-de-modelos.md), cada llamada a herramienta de un
[agente](../Sistemas-con-modelos/agente.md) y lo que bloqueó un [guardrail](../../IA/guardrails.md).

## Seguir una consulta paso a paso

La traza es la unidad que se lee. Huyen: "Ideally, you should be able to trace each query's
transformation through the system step-by-step." Una respuesta mala se explica mirando su traza: si
el contexto no traía el dato, la falla es de recuperación; si lo traía y el modelo lo ignoró, es del
prompt o del modelo. Husain usa esas trazas como insumo de su nivel 2 de evaluación, donde personas o
un [juez](ia-como-juez.md) las califican.

Registrar no alcanza: alguien tiene que leer. Huyen recomienda inspeccionar a mano datos de
producción todos los días.

## Un vocabulario común: las convenciones GenAI de OpenTelemetry

OpenTelemetry, el estándar abierto de telemetría, tiene convenciones semánticas para sistemas con
modelos generativos. Su página original ahora dice "GenAI semantic conventions have moved to the
OpenTelemetry GenAI semantic conventions repository". Según el README de ese repositorio, cubren
spans, métricas y eventos para clientes de modelos generativos, para MCP y convenciones por proveedor.
La ventaja de seguirlas, inferencia de esta base, es que las trazas se pueden leer con cualquier
herramienta que las entienda, sin atarse a una.

> [!NOTE]
> Sin fuente todavía: el estado de estabilidad de las convenciones GenAI (el README no lo dice), los
> nombres exactos de los atributos y los spans de agentes. Según resultados del buscador, sin
> verificar en la especificación, el contenido de los mensajes se captura solo si se activa
> (*opt-in*), y hay registros viejos que marcan ese atributo como movido o deprecado: no se sabe cuál
> refleja el estado actual. El siguiente paso es leer los documentos de spans del repositorio.

## Lo que se registra también se filtra

"Log everything" choca con la privacidad: los prompts y las salidas pueden traer datos personales,
y la traza completa los guarda. El post de Huyen no trata cómo redactarlos; sobre privacidad solo dice
"There's no airtight way to eliminate potential leaks when using third-party APIs."

> [!NOTE]
> Sin fuente todavía: cómo se redactan datos personales en logs y trazas de un sistema con modelos,
> cuánto tiempo se retienen y cómo se pide consentimiento. Ninguna fuente primaria leída lo trata.

## Qué leer para instrumentar

Huyen, ["Building A Generative AI Platform"](https://huyenchip.com/2024/07/25/genai-platform.html),
sección "Observability": fijarse en métricas, logs y trazas y en registrar lo intermedio. Para el
vocabulario, el repositorio
[semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai): fijarse
en qué es opt-in. Las herramientas concretas de trazado no se investigaron.
