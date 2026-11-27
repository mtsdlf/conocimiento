---
resumen: >-
  Las categorías de herramientas para seguir el trabajo de un proyecto (trackers de tareas, tableros, portafolio y observabilidad de agentes), con dos o tres ejemplos de cada una, copiadas el 2026-11-27 sin precios.
estado: borrador
estabilidad: volatil
fuentes:
  - "monday.com, Linear or Jira (blog de un vendedor; según un resumen): https://monday.com/blog/rnd/linear-or-jira/"
  - "Tech Insider, Best project management software 2026 (comparativo de terceros; según un resumen): https://tech-insider.org/au/best-project-management-software-2026/"
  - "OpenTelemetry, semantic conventions for GenAI agent spans (según un resumen; estado Development): https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/index.md"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md"
aliases: [herramientas de gestión de proyectos, project management tools, trackers, issue trackers, tableros kanban, observabilidad de agentes, LLM observability]
creado: 2026-11-27
revisado:
---

# Herramientas de seguimiento

Las categorías de herramientas para seguir el trabajo de un proyecto (trackers de tareas, tableros, portafolio y observabilidad de agentes), con dos o tres ejemplos de cada una, copiadas el 2026-11-27 sin precios.

Implementan lo que describen [trabajo en curso y colas](trabajo-en-curso-y-colas.md), [medir el avance](medir-el-avance.md) e [informar el estado](informar-el-estado.md). La herramienta cambia; el mecanismo queda.

Copiado el 2026-11-27 de comparativos de terceros y blogs de vendedores, leídos como resumen. Los ejemplos no son recomendaciones ni una lista completa, y no se verificó en el sitio oficial de cada una que sigan con ese nombre y esas funciones. Los precios se dejaron afuera a propósito: las fuentes no coincidían y ninguna era oficial.

| Categoría | Para qué sirve | Ejemplos | Qué se vio |
|---|---|---|---|
| Trackers de tareas | registrar piezas, su estado y quién las tiene; sacar tiempo de entrega y rendimiento | Jira, Linear, GitHub Projects | blogs de vendedores describen a Linear y Jira como pensados para equipos de ingeniería |
| Tableros y trabajo entre áreas | ver el trabajo en curso por etapa en proyectos que cruzan áreas | Trello, Asana, monday.com | comparativos describen a Asana y monday.com como más adecuados a trabajo de varias áreas |
| Portafolio y planificación | ver varios proyectos juntos, cronogramas y capacidad | Planview, Smartsheet, Microsoft Project | sin datos de funciones en las fuentes consultadas |
| Observabilidad de agentes | registrar cada paso de un agente y los tokens que consume | convenciones GenAI de OpenTelemetry, Datadog LLM Observability | ver abajo |

## Lo que se puede registrar hoy del trabajo de un agente

Las convenciones semánticas de OpenTelemetry para IA generativa definen pasos de agente (crear e invocar un agente) y atributos de uso de tokens de entrada y de salida. Estaban en estado "Development" al copiarlas, según un resumen de la especificación. No definen un atributo de costo ni uno de tarea: el costo se calcula multiplicando tokens por el precio del proveedor, y el costo por tarea hay que armarlo sumando los pasos de la tarea (esto último no se verificó en la especificación).

> [!NOTE] Sin fuente todavía: qué herramientas siguen el trabajo de agentes junto con el de personas en un mismo tablero, más allá de las convenciones de OpenTelemetry.

La entrada de la vertical es [Seguimiento](seguimiento.md).
