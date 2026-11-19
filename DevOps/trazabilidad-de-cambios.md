---
tipo: concepto
resumen: >-
  La trazabilidad de cambios es poder seguir cada despliegue hasta su commit, su revisión y su
  build; da la evidencia de auditoría: aprobación, separación de funciones y cambios de
  emergencia.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "DORA, Capabilities: Streamlining change approval: https://dora.dev/capabilities/streamlining-change-approval/"
  - "GitHub Docs, Available rules for rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets"
  - "Archivo/DevOps/git/git-organizational-topology.md (original, texto generado con IA)"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-mastery-workflows.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
aliases: [Traceability, Audit trail, Evidencia de auditoría]
parte_de: []
requiere: []
relacionado: [gobernanza-de-repositorios, conventional-commits]
---

# Trazabilidad de cambios

La trazabilidad de cambios es poder seguir cada despliegue hasta su commit, su revisión y su
build; da la evidencia de auditoría: aprobación, separación de funciones y cambios de
emergencia.

## Por qué importa

Ante un incidente, la primera pregunta es qué cambió. Ante una auditoría (SOX, SOC 2, ISO 27001),
es quién aprobó ese cambio y si fue otra persona que quien lo escribió. Si la cadena commit →
revisión → build → despliegue queda registrada sola, las dos respuestas salen de la herramienta y
no de una planilla.

## Cómo funciona

Cada eslabón deja un registro con el SHA del commit como clave común:

| Control | Evidencia |
|---|---|
| Gestión de cambios | PR aprobado, vinculado a un issue |
| Separación de funciones | quien aprueba no es quien escribió ni quien hizo el último push |
| Calidad | resultado del CI asociado al commit |
| Artefacto | build identificado por el commit, con su digest (el hash del contenido, que cambia si cambia un byte) |
| Despliegue | entorno, fecha y actor, con la versión desplegada |
| Rollback | `git revert` o despliegue del tag anterior |

GitHub puede exigir que apruebe alguien distinto de la última persona que empujó a la rama. DORA
recomienda cumplir la separación de funciones con revisión de pares registrada en la plataforma,
más pruebas automáticas, en vez de un comité externo de aprobación: DORA reporta que ese comité
empeora el desempeño de entrega.

**Cambio de emergencia**: sale una rama de hotfix desde el tag de producción, con un grupo
reducido de aprobadores y revisión posterior. DORA propone que el proceso normal sea tan rápido
que sirva también para emergencias.

En las ramas compartidas no se reescribe el historial: se corrige con un commit nuevo o un revert,
para no romper la cadena. Los commits y tags firmados agregan prueba de autoría; la firma de
artefactos es parte de la [Cadena de suministro de software](cadena-de-suministro-de-software.md).

## Ejemplo

Producción falla después del despliegue `api:1.4.2`. El registro lleva al commit `d47c1f`, al PR
que lo aprobó una revisora distinta de la autora, y a la corrida de CI. Primero el equipo vuelve a
desplegar `1.4.1` para restablecer el servicio; después revierte el commit con un PR nuevo, que
genera la versión siguiente.

## No confundir con

La [Observabilidad](../Platform-Engineering/observabilidad.md), que explica qué hace el sistema en ejecución. La trazabilidad explica de
dónde salió lo que está desplegado.

## Relaciones

- Relacionado: [Gobernanza de repositorios](gobernanza-de-repositorios.md) — las reglas cuya aplicación queda como evidencia.
- Relacionado: [Conventional Commits](conventional-commits.md) — los mensajes que explican qué trae cada versión.
- Ver también: [Cadena de suministro de software](cadena-de-suministro-de-software.md) — la firma y la procedencia de los artefactos.
- Ver también: [Pipeline de CI/CD](pipeline-de-ci-cd.md) — el pipeline que identifica cada artefacto por su commit.
