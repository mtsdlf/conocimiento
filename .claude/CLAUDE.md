# CLAUDE.md — conocimiento

Este repo es un vault de Obsidian: la base de conocimiento compartida, la capa de lo general en la organización (skill `tsc-organizacion`). Todo se escribe y se mantiene con la skill `documentar` (the-software-co/skills), que reemplazó a `conocimiento`; lo propio de esta base está en `CONVENCIONES.md` y el Mapa raíz es `conocimiento.md`.

Lo que es de una empresa va a su repo (`tsc-negocio`, `lind-negocio`), y lo que es nuestro saber sobre emprender, a `fundar`.

Quien te habla puede no ser de sistemas: contale lo que cambia en castellano llano y encargate de git, en una rama propia y con un PR contra `main`.

## Los modos

Son los mismos en todos los repos de la organización (skill `tsc-organizacion`). Acá: **Entender** (contestar desde las notas, con enlaces, y decir lo que falta), **Crear** (un tema nuevo desde cero: entrevista, investigación y notas en borrador), **Volcar** (lo que alguien aprendió, a notas en borrador), **Confirmar** (pasar a vigente lo que una persona leyó), **Mantener** (lo viejo, roto o huérfano) y **Seguir** (los borradores sin confirmar y los issues abiertos). Todos con la skill `documentar`: Crear es su modo `nuevo` (o `ampliar`, si el tema ya existe), y Volcar y Mantener son sus modos del mismo nombre.

## Agent skills

### Issue tracker

Los issues viven en GitHub (`mtsdlf/conocimiento`), con el CLI `gh`. See `.claude/docs/agents/issue-tracker.md`.

### Triage labels

Las cinco etiquetas por defecto (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `.claude/docs/agents/triage-labels.md`.

### Domain docs

Single-context, dentro de `.claude/` para que Obsidian no los muestre (`.claude/GLOSSARY.md`, `.claude/docs/adr/`). See `.claude/docs/agents/domain.md`.
