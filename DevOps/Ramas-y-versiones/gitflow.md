---
resumen: >-
  Gitflow es un modelo de branching con dos ramas de larga vida, `main` y `develop`, y ramas
  temporales `feature`, `release` y `hotfix`, pensado para software que se publica en versiones
  programadas.
estado: borrador
estabilidad: estable
fuentes:
  - "Vincent Driessen, A successful Git branching model (2010, nota de reflexión del 5 de marzo de 2020): https://nvie.com/posts/a-successful-git-branching-model/"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
aliases: [Git flow, Git-flow, GitFlow]
creado: 2026-10-03
revisado:
---

# Gitflow

Gitflow es un modelo de branching con dos ramas de larga vida, `main` y `develop`, y ramas
temporales `feature`, `release` y `hotfix`, pensado para software que se publica en versiones
programadas.

## Para qué software sirve, según Driessen

Gitflow separa lo que está en producción de lo que se está preparando, y permite estabilizar una
versión mientras se sigue desarrollando la siguiente. Vincent Driessen lo publicó en 2010. En una
nota de 2020 aclaró que no es un dogma: para equipos que hacen entrega continua recomienda algo
más simple, como GitHub Flow, y lo reserva para software versionado con varias versiones
soportadas a la vez.

## Las cinco ramas y sus merges

| Rama | Sale de | Vuelve a | Para qué |
|---|---|---|---|
| `main` | — | — | cada commit es una versión publicada, con su tag |
| `develop` | — | — | integración de lo que va en la próxima versión |
| `feature/*` | `develop` | `develop` | una funcionalidad |
| `release/*` | `develop` | `main` y `develop` | estabilizar una versión: solo correcciones y el cambio del número de versión |
| `hotfix/*` | `main` | `main` y `develop` | corregir producción sin esperar la próxima versión |

Driessen propone mergear con `--no-ff`, que crea siempre un merge commit: así el historial
muestra qué commits formaron cada funcionalidad y revertirla entera es más fácil. Al cerrar una
release o un hotfix se pone en `main` un tag (un nombre fijo que marca un commit, como
`2.4.0`), normalmente con
[Versionado semántico](versionado-semantico.md).

## Una release 2.4.0 y su hotfix

El equipo corta `release/2.4.0` desde `develop` un lunes. Durante la semana `develop` recibe
funcionalidades para la 2.5 y la release solo recibe correcciones. El viernes la release se
mergea a `main` con el tag `2.4.0` y de vuelta a `develop`. Si aparece un error en producción, se
abre `hotfix/2.4.1` desde `main`.

## Gitflow, trunk-based y la herramienta git-flow

[Trunk-based development](trunk-based-development.md), donde no hay `develop` ni ramas de release largas. Tampoco con la
herramienta de línea de comandos `git-flow`, que solo automatiza la creación y el cierre de
estas ramas.

## Ver también

- [Estrategia de branching](estrategia-de-branching.md) — una de las estrategias posibles.
