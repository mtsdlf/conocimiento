---
resumen: >-
  El contexto del repositorio es lo que el propio repositorio le da a un agente de código para
  trabajar bien en él: un archivo corto de instrucciones con lo que no se deduce del código, el
  material de consulta que se carga solo cuando hace falta y las reglas que se imponen con
  mecanismos deterministas.
estado: vigente
estabilidad: semi
fuentes:
  - "Anthropic, Best practices for Claude Code (leída 2026-11-27): https://code.claude.com/docs/en/best-practices"
  - "Anthropic, Effective context engineering for AI agents (2025-09-29): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  - "Gloaguen, Mündler, Müller, Raychev y Vechev, Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?, arXiv 2602.11988 (2026-02-12), abstract: https://arxiv.org/abs/2602.11988"
  - "Thoughtworks Technology Radar vol. 35, Agent instruction bloat (Caution, 2026-11-04): https://www.thoughtworks.com/en-au/radar/techniques/agent-instruction-bloat"
  - "Claude Code, Skills: https://code.claude.com/docs/en/skills"
  - https://agents.md
aliases: [archivo de instrucciones para agentes, context engineering, ingeniería de contexto, AGENTS.md, CLAUDE.md, instrucciones del repositorio]
creado: 2026-11-27
revisado: 2026-11-27
---

# Contexto del repositorio

El contexto del repositorio es lo que el propio repositorio le da a un agente de código para trabajar bien en él: un archivo corto de instrucciones con lo que no se deduce del código, el material de consulta que se carga solo cuando hace falta y las reglas que se imponen con mecanismos deterministas.

Es la parte de [Construcción](construccion.md) que prepara el terreno para el [agente de código](agente-de-codigo.md). El agente lee el repositorio por su cuenta; el contexto llena lo que el código no dice. El mismo principio, aplicado a sistemas que usan un modelo en producción, está en [contexto y RAG](../../Arquitectura/Sistemas-con-modelos/contexto-y-rag.md).

## El contexto como recurso que se gasta

Anthropic define la ingeniería de contexto como "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference", y su guía es buscar "the smallest possible set of high-signal tokens". El contexto de un modelo se degrada a medida que se llena, y por eso cada línea que el repositorio le impone al agente compite con lo que el agente necesita para la tarea. Según su resumen, las técnicas que propone son traer información justo cuando hace falta, compactar la conversación, guardar notas fuera de la ventana y delegar en subagentes que arrancan con contexto limpio.

## Qué va en el archivo de instrucciones

La guía de buenas prácticas de Anthropic dice que el archivo "works best when it only holds what Claude couldn't work out from the code itself" y nombra cuatro cosas:

1. Cómo se confirma el trabajo: los comandos exactos de prueba, typecheck y lint, y cómo correr una sola prueba.
2. Los "places where the code is misleading".
3. Las "decisions that aren't in the repo".
4. "Anything you've had to correct twice already."

La misma guía desaconseja describir la arquitectura y la estructura de carpetas, porque el agente lee el repositorio solo, y recomienda quedar por debajo de 200 líneas. Esta base considera que la primera de las cuatro es la que más pesa: un agente que sabe cómo comprobar su trabajo puede iterar hasta que pase, como se explica en [agente de código](agente-de-codigo.md).

Hay un formato abierto y compartido entre herramientas para este archivo, y cada herramienta tiene también su nombre propio y sus reglas de precedencia; los nombres y límites concretos están en la ficha [herramientas de agentes de código](herramientas-de-agentes-de-codigo.md).

## Lo que dice la evidencia sobre estos archivos

El único estudio encontrado sobre el efecto de estos archivos es un preprint de ETH Zürich (arXiv 2602.11988, presentado en un taller de ICLR 2026, sin revisión por pares en la versión leída). Según su resumen, los archivos de contexto "do not generally improve task success rates" y suben el costo de inferencia "by over 20% on average". Los resúmenes del repositorio, "despite being popular and recommended by model providers, don't help". Donde sí rinden es "for specifying non-standard coding practices".

> [!IMPORTANT]
> Las versiones del preprint discrepan sobre los archivos escritos por personas: según el resumen del buscador, la primera dice que mejoran un poco el resultado y la posterior, que no lo mejoran de forma significativa. Ninguna de las dos se leyó completa.

El Radar de Thoughtworks llega a lo mismo desde la práctica: pone "agent instruction bloat" en Caution porque los archivos "tend to grow long, contradictory, and stale". Recomienda convertir instrucciones en hooks o chequeos, reevaluarlas con cada modelo nuevo, borrar las que sobran y revelar el contexto de forma progresiva. Según la lectura de esta base, las tres fuentes van en contra de un archivo largo generado de una vez con un resumen de todo el repositorio.

## Reglas sin excepción, fuera de las instrucciones

Una instrucción es una sugerencia que el agente puede descartar. La guía de Anthropic lo dice así: "If something has to happen every time, make it a hook, a deny rule, or a managed setting." No leer los archivos de secretos, no tocar las migraciones o correr el formateador después de cada edición son reglas de ese tipo. Según la guía de Anthropic, escribirlas en mayúsculas en el archivo de instrucciones no las vuelve obligatorias.

Los mecanismos deterministas son de tres clases. Un hook del agente corre un script en un momento fijo de la sesión; el que corre antes de una acción puede bloquearla. Una regla de permisos niega el acceso a un archivo o a un comando. Un [hook de Git](Git/hook-de-git.md) o un paso de [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md) rechaza el cambio aunque lo haya hecho una persona. El formato y el estilo entran acá: el formateador y el linter corren solos y no necesitan una línea en las instrucciones. Qué secretos no debe ver un agente se decide en [configuración](Configuracion/configuracion.md), con la [gestión de secretos](../../DevOps/DevSecOps/gestion-de-secretos.md) de DevOps.

## Material que se carga cuando hace falta

Lo que es largo y se usa a veces (cómo se hace una migración, la guía de estilo de la API, un procedimiento de despliegue) no va en el archivo que se lee siempre. Va en documentos que el agente abre cuando la tarea lo pide. La documentación de skills de Anthropic lo justifica así: "a skill's body loads only when it's used, so long reference material costs almost nothing until you need it". El vocabulario del negocio, que tiene que ser el mismo en el código y en las notas, sale del [modelo de dominio](../Definicion/modelo-de-dominio.md).

## Cómo se mantiene

Esta base trata el archivo de instrucciones como código: se revisa en cada cambio y se poda cuando una regla pasó a un hook. Thoughtworks recomienda además reevaluar las instrucciones con cada modelo nuevo. Un criterio práctico de esta base, que sale de la lista de Anthropic: cuando hubo que corregir al agente dos veces por lo mismo, se agrega una línea; cuando una línea se puede imponer con un mecanismo, se mueve. Para que todo proyecto nuevo arranque con este contexto, va en la [plantilla de proyecto](plantilla-de-proyecto.md).
