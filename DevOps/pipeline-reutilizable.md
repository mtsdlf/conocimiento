---
tipo: concepto
resumen: >-
  Un pipeline reutilizable es una definición de pipeline central y versionada (plantilla,
  reusable workflow o acción) que muchos repositorios invocan, para que cada servicio solo
  declare lo propio.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "GitHub Docs, Reuse workflows: https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows"
  - "GitLab Docs, Use CI/CD configuration from other files (include): https://docs.gitlab.com/ci/yaml/includes/"
  - "Archivo/DevOps/arquitectura-cicd-gitflow.md (diseño propio)"
  - "Archivo/DevOps/git-ecosystem-multi-repo.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
aliases: [Reusable pipeline, Plantilla de pipeline, Pipeline template]
parte_de: []
requiere: [pipeline-de-ci-cd]
relacionado: []
---

# Pipeline reutilizable

Un pipeline reutilizable es una definición de pipeline central y versionada (plantilla,
reusable workflow o acción) que muchos repositorios invocan, para que cada servicio solo
declare lo propio.

## Por qué importa

Con 50 servicios y un pipeline copiado en cada uno, agregar un escaneo de seguridad son 50 PRs, y
al año hay 50 variantes distintas. Con una definición central, el cambio se hace una vez y todos
los servicios lo reciben al subir de versión. Además, los servicios quedan con un archivo corto
en vez de un [[pipeline-de-ci-cd]] complejo.

## Cómo funciona

Cada plataforma tiene su mecanismo: en GitHub Actions, un workflow con el evento `workflow_call`
que otros llaman, o una acción propia; en GitLab CI, `include` de un archivo de otro proyecto.
El patrón es el mismo:

- **Repo del servicio**: un pipeline mínimo que llama a la definición central y le pasa
  parámetros (lenguaje, versión del runtime, destino de despliegue).
- **Definición central**: decide las etapas según el tipo de evento o de rama, y llama a piezas
  más chicas (build, pruebas, versionado, despliegue), una por responsabilidad.
- **Versionado**: cada pieza se publica con versión (`@v1`, `@v2`) y el servicio fija cuál usa.
  Un tag como `@v2` se puede mover a otro commit; por eso GitHub recomienda fijar por el SHA del
  commit cuando importa que nada cambie sin aviso. Un servicio elige `@v2` (recibe arreglos
  solo) o el SHA de `@v2` (cambia solo cuando lo actualiza).

Agregar un servicio es copiar el archivo mínimo; agregar una tecnología es sumar una pieza de
build y otra de pruebas. Las reglas comunes (escaneos de seguridad, revisión de licencias, gates
de calidad, es decir, etapas que frenan el pipeline si no se cumple un umbral) viven una sola
vez.

Es la forma técnica de un [[golden-path]]: el camino estándar para construir y desplegar.
Mantenerlo suele ser trabajo de un [[platform-team]], que lo ofrece como producto interno.

## Ejemplo

Un servicio en Go tiene un workflow corto que llama al workflow central, que declara
`on: workflow_call`:

```yaml
on: [push, pull_request]
jobs:
  ci:
    uses: mi-org/pipelines/.github/workflows/servicio.yml@v2
    with:
      runtime: go@1.23
      deploy_target: k8s
    secrets: inherit
```

Cuando el equipo de plataforma publica `@v3` con firma de imágenes, cada servicio la adopta
cambiando una línea.

## No confundir con

Un pipeline único obligatorio. La definición central cubre lo común; un servicio con
necesidades distintas puede agregar pasos propios o no usarla, igual que se sale de un golden
path.

## Relaciones

- Requiere: [[pipeline-de-ci-cd]] — es un pipeline, definido una vez para muchos repos.
- Ver también: [[golden-path]] — el pipeline reutilizable es su parte de construcción y despliegue.
- Ver también: [[platform-team]] — el equipo que suele mantenerlo.
- Ver también: [[reutilizacion-en-github-actions]] — cómo se hace en GitHub Actions.
