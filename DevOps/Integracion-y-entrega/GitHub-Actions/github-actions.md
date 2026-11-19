---
resumen: >-
  GitHub Actions es la plataforma de CI/CD integrada en GitHub: un evento del repositorio dispara
  un workflow escrito en YAML, cuyos jobs corren en paralelo sobre runners y ejecutan steps que
  pueden usar actions reutilizables.
estado: borrador
estabilidad: estable
fuentes:
  - "Archivo/Automatizacion/github-actions-referencia.md"
  - "GitHub Docs, Understanding GitHub Actions: https://docs.github.com/en/actions/get-started/understand-github-actions"
  - "GitHub Docs, Contexts reference: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts"
  - "GitHub Docs, Expressions: https://docs.github.com/en/actions/reference/workflows-and-actions/expressions"
aliases: [GHA, GitHub Actions workflow]
creado: 2026-10-03
revisado:
---

# GitHub Actions

GitHub Actions es la plataforma de CI/CD integrada en GitHub: un evento del repositorio dispara
un workflow escrito en YAML, cuyos jobs corren en paralelo sobre runners y ejecutan steps que
pueden usar actions reutilizables.

## El pipeline en el mismo repositorio

El pipeline vive en el mismo repositorio que el código, en `.github/workflows/`, y se revisa en
el mismo pull request. Es la forma habitual de hacer [Integración continua](../integracion-continua.md) en proyectos alojados
en GitHub, sin un servidor de CI aparte.

## Workflow, event, job, step, action y runner

- **Workflow**: un archivo YAML en `.github/workflows/` con uno o más jobs. Un repositorio puede
  tener varios.
- **Event**: lo que dispara el workflow: `push`, `pull_request`, un horario (`schedule`), una
  ejecución manual (`workflow_dispatch`) o una llamada a la API.
- **Job**: una lista de steps que corren en orden sobre el mismo runner, por eso comparten
  archivos. Los jobs corren en paralelo salvo que uno declare `needs` sobre otro. Una `matrix`
  repite el mismo job con distintas combinaciones de variables, por ejemplo tres versiones de
  Node.
- **Step**: un comando de shell o el uso de una action.
- **Action**: una unidad reutilizable de pasos, propia o del Marketplace (el catálogo público de
  actions de GitHub), como `actions/checkout`.
- **Runner**: la máquina que ejecuta un job por vez. GitHub ofrece runners Ubuntu, Windows y
  macOS, cada uno en una VM nueva por ejecución; los self-hosted cubren hardware o redes propias.

Dentro del YAML, las **expresiones** `${{ ... }}` leen **contexts**: objetos con datos de la
ejecución, como `github.ref`, `secrets` o `matrix`. La mayoría de los contexts se pueden usar
antes de mandar el job al runner, por ejemplo en un `if:`; algunos, como `runner`, solo existen
con el job corriendo, igual que las variables de entorno por defecto.

## Un build que espera a dos variantes de test

El job `build` corre solo si pasan las dos variantes de `test`:

```yaml
on: pull_request
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm test
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
```

## Un workflow no es una action

Una action. La action es una pieza que un step usa; el workflow es el proceso entero que orquesta
jobs y steps. Las formas de reutilizar ambos están en [Reutilización en GitHub Actions](reutilizacion-en-github-actions.md).

## Qué hay adentro de un workflow

Cuatro notas detallan partes de un workflow:

- [Reutilización en GitHub Actions](reutilizacion-en-github-actions.md) — workflows reutilizables y actions propias.
- [Environment de GitHub Actions](environment-de-github-actions.md) — destinos de despliegue con reglas de protección y concurrencia.
- [Artifact y cache de GitHub Actions](artifact-y-cache-de-github-actions.md) — qué guarda un artifact, qué guarda la cache y las attestations.
- [Secret de GitHub Actions](secret-de-github-actions.md) — dónde se guardan los secrets y cómo los lee un workflow.

## Ver también
- [Pipeline de CI/CD](../pipeline-de-ci-cd.md) — el concepto general que un workflow implementa.
