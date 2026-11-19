---
tipo: concepto
resumen: >-
  Una estrategia de branching define qué ramas existen en un repositorio, cuánto viven y cómo se
  integran: trunk-based, GitHub Flow, GitLab Flow o Gitflow, según la cadencia de entrega.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Martin Fowler, Patterns for Managing Source Code Branches (2020): https://martinfowler.com/articles/branching-patterns.html"
  - "GitHub Docs, GitHub flow: https://docs.github.com/en/get-started/using-github/github-flow"
  - "Vincent Driessen, A successful Git branching model (2010, nota de 2020): https://nvie.com/posts/a-successful-git-branching-model/"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-advanced-collaboration.md (original, texto generado con IA)"
aliases: [Branching strategy, Modelo de ramas, Estrategia de ramas]
parte_de: []
requiere: []
relacionado: [gobernanza-de-repositorios, versionado-semantico]
---

# Estrategia de branching

Una estrategia de branching define qué ramas existen en un repositorio, cuánto viven y cómo se
integran: trunk-based, GitHub Flow, GitLab Flow o Gitflow, según la cadencia de entrega.

## Por qué importa

Cuanto más vive una rama sin integrarse, más difiere de la principal y más caro es el merge.
Según Fowler, los equipos de mejor desempeño en los informes State of DevOps integran mucho más
seguido que los de peor desempeño. La estrategia fija esa frecuencia para todo el equipo.

## Cómo funciona

Las estrategias se distinguen por cuántas ramas de larga vida tienen:

| Estrategia | Ramas de larga vida | Encaja con |
|---|---|---|
| [Trunk-based development](trunk-based-development.md) | solo `main` | despliegue varias veces por día |
| GitHub Flow | solo `main`; cada cambio en una rama corta con PR | servicios web que despliegan al mergear |
| GitLab Flow | `main` y ramas por entorno (`preprod`, `production`) | promoción controlada por etapas |
| [Gitflow](gitflow.md) | `main` y `develop`, más ramas de release y hotfix | software con versiones programadas |

Fowler desaconseja las ramas por entorno: la diferencia entre entornos conviene que viva en la
configuración, no en ramas distintas. En [GitOps](gitops.md) la promoción entre entornos se hace por
carpeta o por rama del repo de configuración; ver [Promoción entre entornos](promocion-entre-entornos.md).

**Rebase o merge como política de equipo**: rebasar es reaplicar los commits propios encima de
la punta actual de `main`. Una regla habitual es rebasar la rama propia antes del PR, para que el
historial quede lineal y el PR muestre solo los cambios propios, y no reescribir nunca una rama
compartida. El merge final puede ser un merge commit (conserva los commits de la rama) o un
squash (junta todos los commits del PR en uno solo). La mecánica de cada operación está en [Git](../Desarrollo/Git/git.md).

## Ejemplo

Un equipo que despliega un servicio web cada día elige GitHub Flow: rama `feature/login`, PR con
CI obligatorio, merge a `main` y despliegue automático. Otro equipo que publica una aplicación de
escritorio con versiones trimestrales y varias versiones soportadas elige Gitflow.

## No confundir con

La convención de nombres de ramas (`feature/<ticket>`). Los nombres son una regla de
[Gobernanza de repositorios](gobernanza-de-repositorios.md); la estrategia decide cuántas ramas viven y hacia dónde fluyen
los cambios.

## Relaciones

- Casos: [Trunk-based development](trunk-based-development.md) — la estrategia de una sola rama de larga vida.
- Casos: [Gitflow](gitflow.md) — la estrategia de ramas de release y hotfix.
- Relacionado: [Gobernanza de repositorios](gobernanza-de-repositorios.md) — las reglas que protegen las ramas que la estrategia define.
- Relacionado: [Versionado semántico](versionado-semantico.md) — el número que reciben los tags de las ramas que se publican.
- Ver también: [Integración continua](integracion-continua.md) — la práctica que exige integrar seguido a la rama principal.
