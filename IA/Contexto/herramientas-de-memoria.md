---
resumen: >-
  Cómo implementan la memoria una API de agentes, un producto de memoria y dos asistentes de chat
  comerciales, copiado de sus páginas el 2026-11-27.
estado: vigente
estabilidad: volatil
fuentes:
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
  - https://arxiv.org/abs/2504.19413
  - https://help.openai.com/en/articles/8590148-memory-faq
  - https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-conversations
creado: 2026-11-27
revisado: 2026-11-27
---

# Herramientas de memoria

Cómo implementan la memoria una API de agentes, un producto de memoria y dos asistentes de chat
comerciales, copiado de sus páginas el 2026-11-27.

Implementa el componente [Memoria](memoria.md). Las fuentes vivas están en `fuentes`. Todo esto cambia seguido: antes de usarlo,
volvé a la página.

## La herramienta de memoria de la API de Anthropic

[Documentación](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool). Corre del
lado del cliente: el modelo pide operaciones de archivo sobre un directorio `/memories` y la
aplicación las ejecuta con su propio almacenamiento.

| Pieza | Valor |
|---|---|
| Operaciones | `view`, `create`, `str_replace`, `insert`, `delete`, `rename` |
| Instrucción que agrega el sistema | "ASSUME INTERRUPTION: Your context window might be reset at any moment" |
| Relación con la compactación | la compactación resume el historial; la memoria "preserves the information that must survive summarization" |
| Riesgos que nombra | recorrido de directorios (`/memories/../../secrets.env`), tamaño de archivos, memorias viejas, datos sensibles (el modelo "usually refuses", la garantía va en el código) |

## Mem0: resumir y recuperar

Según el abstract del preprint ([arXiv 2504.19413](https://arxiv.org/abs/2504.19413), abril de 2025,
sin revisión por pares, escrito por los autores del producto), sobre el benchmark LOCOMO: "26%
relative improvements in the LLM-as-a-Judge metric over OpenAI", 91% menos de latencia en el
percentil 95 y más de 90% de ahorro de tokens frente a pasar todo el contexto.

## La memoria en dos asistentes de chat

| | ChatGPT | Claude |
|---|---|---|
| Fuente | [Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq) | [Chat search y memoria](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-conversations) |
| Mecanismos | memorias guardadas ("saved memories") y referencia al historial de chats | guarda "individual topics as you chat"; búsqueda en chats pasados |
| Separación | apagar las memorias guardadas apaga también la referencia al historial | una memoria separada por proyecto |
| Sin memoria | los chats temporales "do not create or update memories" | modo incógnito, pausa y reinicio |
| Temas sensibles | (no se leyó) | salud, política y religión no se guardan por defecto |
| Borrar un chat | no borra las memorias guardadas | no borra las memorias que salieron de él |
| Equipos | (no se leyó) | depende de quien administra; las organizaciones creadas desde el 2026-10-31 arrancan con memoria activada |
