---
resumen: >-
  Ficha con los nombres de archivos, mecanismos y comandos con que dos herramientas de agentes de
  código y un formato abierto resuelven el contexto del repositorio, la verificación y el trabajo
  en paralelo, copiados de su documentación el 2026-11-27.
estado: vigente
estabilidad: volatil
fuentes:
  - "Anthropic, Best practices for Claude Code (leída 2026-11-27): https://code.claude.com/docs/en/best-practices"
  - "Claude Code, Skills: https://code.claude.com/docs/en/skills"
  - "OpenAI, Codex: AGENTS.md: https://learn.chatgpt.com/docs/agent-configuration/agents-md"
  - https://agents.md
creado: 2026-11-27
revisado: 2026-11-27
---

# Herramientas de agentes de código

Ficha con los nombres de archivos, mecanismos y comandos con que dos herramientas de agentes de código y un formato abierto resuelven el contexto del repositorio, la verificación y el trabajo en paralelo, copiados de su documentación el 2026-11-27.

Implementa lo que explican [contexto del repositorio](contexto-del-repositorio.md) y [agente de código](agente-de-codigo.md). Las herramientas cambian de nombres y comandos seguido; ante la duda, manda la documentación enlazada en cada fila. La documentación se leyó con una herramienta que extrae por pregunta, no completa.

## El archivo de instrucciones

| Herramienta o formato | Archivo | Cómo se combina | Límite | Fuente |
|---|---|---|---|---|
| AGENTS.md (formato abierto) | `AGENTS.md` | en un monorepo, "the closest one takes precedence"; "explicit user chat prompts override everything" | no declarado | [agents.md](https://agents.md) |
| Codex (OpenAI) | `AGENTS.md`, con `AGENTS.override.md` primero | junta los archivos desde la raíz del repositorio hasta el directorio actual, uno por directorio | 32 KiB combinados por defecto (`project_doc_max_bytes`); lo que excede se descarta | [Codex: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| Claude Code (Anthropic) | `CLAUDE.md` | no relevado en esta ficha | la guía recomienda quedar por debajo de 200 líneas | [Best practices](https://code.claude.com/docs/en/best-practices) |

Según agents.md, el formato lo administra la Agentic AI Foundation, bajo la Linux Foundation, lo usan "over 60k open-source projects" y lo leen más de 20 herramientas.

> [!NOTE] Sin fuente todavía: no se confirmó si Claude Code lee también `AGENTS.md` además de `CLAUDE.md`; verificar en <https://code.claude.com/docs/en/memory> antes de recomendar un archivo común para las dos herramientas.

## Mecanismos de Claude Code

| Para qué | Mecanismo | Qué dice la documentación |
|---|---|---|
| Regla sin excepción | hook `PreToolUse` | corre antes de cada acción; si sale con código 2, la bloquea |
| No terminar sin verificar | hook `Stop` | impide que la sesión termine hasta que pase, por ejemplo, el typecheck |
| Objetivo verificable | `/goal` | la guía lo lista entre las formas de pedir una verificación; no se relevó su detalle |
| Material de consulta | skills (`SKILL.md`) | el cuerpo se carga solo cuando se usa; se sugiere `SKILL.md` por debajo de 500 líneas; siguen el estándar abierto Agent Skills (agentskills.io) |
| Sesión en paralelo | `claude -w <nombre>` | abre la sesión en un git worktree nuevo |
| Archivos que el worktree no trae | `.worktreeinclude`, `worktree.symlinkDirectories` | un worktree es un checkout nuevo sin archivos ignorados ni dependencias; se copian, se enlazan o se instalan con el comando escrito en `CLAUDE.md` |
| Cambio mecánico grande | `/batch` | lo divide en 5 a 30 unidades, cada una con su worktree y su PR |

Fuente de la tabla: [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) y [Skills](https://code.claude.com/docs/en/skills).
