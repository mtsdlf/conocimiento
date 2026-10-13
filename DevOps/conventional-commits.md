---
tipo: concepto
resumen: >-
  Conventional Commits es una convención de mensajes de commit (`tipo(alcance): descripción`) que
  permite calcular la próxima versión y generar el changelog de forma automática.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Conventional Commits 1.0.0: https://www.conventionalcommits.org/en/v1.0.0/"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-mastery-workflows.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
aliases: [Commits convencionales, Conventional Commit]
parte_de: []
requiere: [versionado-semantico]
relacionado: [gobernanza-de-repositorios, trazabilidad-de-cambios]
---

# Conventional Commits

Conventional Commits es una convención de mensajes de commit (`tipo(alcance): descripción`) que
permite calcular la próxima versión y generar el changelog de forma automática.

## Por qué importa

Si el mensaje dice qué tipo de cambio es, una herramienta puede decidir el próximo número de
[[versionado-semantico]] sin que nadie lo elija a mano. El changelog sale agrupado por tipo, y en
un PR se ve de un vistazo qué cambia.

## Cómo funciona

El mensaje tiene una línea de encabezado, un cuerpo opcional y footers opcionales:

```text
<tipo>[alcance opcional]: <descripción>

[cuerpo opcional]

[footers opcionales]
```

La especificación 1.0.0 define dos tipos (`fix`, `feat`) y una señal de ruptura (`!` o
`BREAKING CHANGE`), cada uno con su efecto en la versión:

| Señal | Significa | Versión |
|---|---|---|
| `fix` | corrige un error | PARCHE |
| `feat` | agrega una funcionalidad | MENOR |
| `!` después del tipo, o footer `BREAKING CHANGE:` | cambio incompatible | MAYOR |

Otros tipos (`build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`) son
recomendaciones de la convención de Angular y de `@commitlint/config-conventional`; la
especificación los permite, pero no les asigna versión.

En la práctica, `commitlint` valida el formato en un hook local o en el CI, y herramientas como
`semantic-release` o `release-please` leen los commits desde el último tag, calculan la versión,
crean el tag y escriben las notas de release.

## Ejemplo

```text
feat(api)!: enviar un email cuando se despacha el pedido

BREAKING CHANGE: la notificación por email ahora es obligatoria
```

Si el último tag era `2.7.3`, este commit lleva la próxima versión a `3.0.0`. Con solo commits
`fix` desde `2.7.3`, sería `2.7.4`.

## No confundir con

Un commit atómico: Conventional Commits regula el mensaje, no el tamaño ni el contenido del
cambio. Un commit `feat` mal etiquetado produce una versión equivocada igual.

## Relaciones

- Requiere: [[versionado-semantico]] — la numeración que los tipos de commit alimentan.
- Relacionado: [[gobernanza-de-repositorios]] — el formato del mensaje se exige como check obligatorio.
- Relacionado: [[trazabilidad-de-cambios]] — el tipo y el alcance del commit explican cada versión.
