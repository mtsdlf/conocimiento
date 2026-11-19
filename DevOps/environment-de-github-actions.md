---
tipo: concepto
resumen: >-
  Un environment de GitHub Actions es un destino de despliegue con nombre, como production o
  staging, que exige reglas de protección antes de correr el job y guarda sus propios secrets; con
  `concurrency` se evita desplegar dos veces a la vez.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Archivo/Automatizacion/github-actions-referencia.md"
  - "GitHub Docs, Deployment environments: https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments"
  - "GitHub Docs, Deployments and environments reference: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments"
  - "GitHub Docs, Concurrency: https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency"
aliases: [Environment, Deployment environment, Entorno de despliegue de GitHub]
parte_de: []
requiere: [github-actions]
relacionado: [secret-de-github-actions]
---

# Environment de GitHub Actions

Un environment de GitHub Actions es un destino de despliegue con nombre, como production o
staging, que exige reglas de protección antes de correr el job y guarda sus propios secrets; con
`concurrency` se evita desplegar dos veces a la vez.

## Por qué importa

Separa quién puede desplegar a producción de quién puede escribir el workflow. Las credenciales de
producción solo llegan a un job que pasó las reglas del environment, no a cualquier job del
repositorio.

## Cómo funciona

El environment se crea en **Settings > Environments > New environment** del repositorio, donde se
le cargan reglas y secrets. Un job lo usa con `environment: production`; cada job referencia uno
solo. Si el workflow nombra un environment que no existe, GitHub lo crea vacío, sin reglas. Antes
de mandar el job al runner, GitHub evalúa las reglas de protección:

- **Revisores obligatorios**: hasta seis personas o equipos, con la opción de impedir que quien
  disparó el despliegue lo apruebe.
- **Wait timer**: una espera de 1 a 43.200 minutos.
- **Ramas y tags permitidos**: por ejemplo, solo `main`.
- **Reglas propias**: una app externa que aprueba o rechaza.

Los secrets del environment se leen recién cuando el job pasó las reglas y llegó al runner. En
repositorios privados, los revisores y el wait timer requieren GitHub Enterprise; las ramas y
tags permitidos, al menos GitHub Pro o Team.

**Evitar despliegues simultáneos**: por defecto pueden correr varias ejecuciones a la vez. Con
`concurrency: production` a nivel de workflow o de job, solo corre una ejecución del grupo y
queda una sola pendiente: si llega otra, la nueva reemplaza a la pendiente anterior, que se
cancela. Con
`cancel-in-progress: true` también se cancela la que está corriendo, útil para linters sobre
commits viejos pero no para despliegues.

## Ejemplo

El job `deploy` usa `environment: production`, con un revisor obligatorio y solo la rama `main`
permitida, y `concurrency: production`. Dos merges seguidos producen un despliegue por vez, cada
uno aprobado por una persona.

## No confundir con

Un entorno de infraestructura. El environment de GitHub es una regla y un lugar para secrets; el
clúster o la cuenta de nube a la que apunta se configura aparte, y su paso de un entorno al
siguiente se describe en [Promoción entre entornos](promocion-entre-entornos.md).

## Relaciones

- Requiere: [GitHub Actions](github-actions.md) — jobs y workflows.
- Relacionado: [Secret de GitHub Actions](secret-de-github-actions.md) — el environment es uno de los tres niveles donde se guardan secrets.
- Ver también: [Promoción entre entornos](promocion-entre-entornos.md) — el concepto general de pasar un cambio de staging a producción.
