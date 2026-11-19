---
tipo: concepto
resumen: >-
  En GitHub Actions la lógica repetida se reutiliza de dos formas: con workflows reutilizables,
  que un workflow llama como si fueran un job, o con actions propias de tres tipos: composite,
  JavaScript y contenedor Docker.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Archivo/Automatizacion/github-actions-referencia.md"
  - "GitHub Docs, Reusing workflow configurations: https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations"
  - "GitHub Docs, Reuse workflows: https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows"
  - "GitHub Docs, Custom actions: https://docs.github.com/en/actions/concepts/workflows-and-actions/custom-actions"
  - "GitHub Docs, Secure use reference: https://docs.github.com/en/actions/reference/security/secure-use"
aliases: [Reusable workflow, Workflow reutilizable, Composite action, Custom action]
parte_de: [github-actions]
requiere: [github-actions]
relacionado: []
---

# Reutilización en GitHub Actions

En GitHub Actions la lógica repetida se reutiliza de dos formas: con workflows reutilizables,
que un workflow llama como si fueran un job, o con actions propias de tres tipos: composite,
JavaScript y contenedor Docker.

## Por qué importa

Sin reutilizar, cada repositorio copia el mismo YAML de build y despliegue, y un arreglo hay que
hacerlo en decenas de lugares. Una definición central y versionada es la base de un
[Pipeline reutilizable](pipeline-reutilizable.md).

## Cómo funciona

**Workflow reutilizable**: declara `on: workflow_call` con sus inputs y secrets. El workflow que lo
usa (el *caller*) lo invoca desde un job con `uses: org/repo/.github/workflows/build.yml@<ref>`, y
el reutilizado (el *called*) aporta jobs enteros, con su propio runner y su log por job. Recibe
secrets explícitos o con `secrets: inherit`, y admite hasta diez niveles de anidamiento.

**Action propia**: se describe en un `action.yml` y se usa como un step. No lee secrets por su
cuenta: el workflow que la usa se los pasa como input (`with:`) o como variable de entorno
(`env:`).

| Tipo | Corre en | Cuándo |
|---|---|---|
| Composite | El runner del job | Agrupar varios steps de shell o de otras actions |
| JavaScript | El runner, sin contenedor | Lógica propia rápida, en Linux, Windows y macOS |
| Contenedor Docker | Un contenedor, solo en runners Linux | Necesita herramientas o un entorno fijo |

Según GitHub, las Docker son más lentas que las JavaScript.

**Versionado**: según GitHub, fijar la referencia a un SHA completo es la única forma de usar una
versión inmutable. Un tag es más cómodo, pero quien controla el repositorio puede moverlo.

**Cuál elegir**: si lo repetido es un proceso entero, con varios jobs, runners propios o secrets,
va un workflow reutilizable; si son unos pocos pasos dentro de un job ajeno, una composite action.

## Ejemplo

Diez servicios llaman al mismo build; cada uno solo declara su imagen y pasa el secret:

```yaml
jobs:
  build:
    uses: platform/ci/.github/workflows/build.yml@<sha>
    with:
      image-name: pagos
    secrets:
      registry-token: ${{ secrets.REGISTRY_TOKEN }}
```

## No confundir con

Una composite action. Corre como un step dentro del job del caller, no puede usar secrets por su
cuenta y aparece como un solo step en el log; un workflow reutilizable aporta jobs completos.

## Relaciones

- Parte de y requiere: [GitHub Actions](github-actions.md) — workflows, jobs, steps y actions.
- Ver también: [Pipeline reutilizable](pipeline-reutilizable.md) — el patrón general que estas piezas implementan.
