# Domain Docs

How the engineering skills should consume this repo's domain documentation.

This repo is an Obsidian vault, so the domain docs live inside `.claude/` (hidden from Obsidian) instead of the usual root locations. The notes themselves, and their conventions, are in `CONVENCIONES.md` and `conocimiento.md`.

## Before exploring, read these

- **`.claude/GLOSSARY.md`**: the project's vocabulary.
- **`.claude/docs/adr/`**: read ADRs that touch the area you're about to work in.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved, **at these `.claude/` paths, not at the repo root**.

## File structure

Single-context:

```
/
├── .claude/
│   ├── GLOSSARY.md
│   └── docs/adr/
│       ├── 0001-....md
│       └── 0002-....md
├── conocimiento.md      ← Mapa raíz del vault
└── <Tema>/              ← notas
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a proposal, a hypothesis), use the term as defined in `.claude/GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (...), but worth reopening because…_
