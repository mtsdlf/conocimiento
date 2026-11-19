---
tipo: concepto
resumen: >-
  En GitHub Actions un artifact guarda archivos producidos por una ejecución para pasarlos entre
  jobs o bajarlos después, y la cache reutiliza dependencias entre ejecuciones para ahorrar tiempo;
  las attestations prueban de qué build salió un artifact.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Archivo/Automatizacion/github-actions-referencia.md"
  - "GitHub Docs, Workflow artifacts: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts"
  - "GitHub Docs, Dependency caching: https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching"
  - "GitHub Docs, Dependency caching reference: https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching"
  - "GitHub Docs, Artifact attestations: https://docs.github.com/en/actions/concepts/security/artifact-attestations"
aliases: [Workflow artifact, Dependency caching, Artifact attestation, actions/cache]
parte_de: []
requiere: [github-actions]
relacionado: []
---

# Artifact y cache de GitHub Actions

En GitHub Actions un artifact guarda archivos producidos por una ejecución para pasarlos entre
jobs o bajarlos después, y la cache reutiliza dependencias entre ejecuciones para ahorrar tiempo;
las attestations prueban de qué build salió un artifact.

## Por qué importa

Cada job corre en un runner nuevo y vacío. Sin artifact, el job de despliegue no ve el binario que
compiló el job de build; sin cache, cada ejecución vuelve a bajar todas las dependencias.

## Cómo funciona

| | Artifact | Cache |
|---|---|---|
| Qué guarda | Lo que produce un job: binarios, reportes de pruebas, logs | Lo que cambia poco: dependencias descargadas |
| Para qué | Pasarlo a otro job o verlo cuando terminó la ejecución | Acelerar la próxima ejecución |
| Cómo | `actions/upload-artifact` y `actions/download-artifact` | `actions/cache` con un `key` y `restore-keys` |
| Si falta | El job que lo espera falla | Se reconstruye, solo tarda más |

GitHub dice que no son intercambiables. Los artifacts y logs se guardan 90 días por defecto,
configurable hasta 90 en repositorios públicos y 400 en privados. La cache busca primero el `key` exacto y después el más
reciente que empiece con algún `restore-keys`. Borra las entradas sin uso por más de 7 días, y el
límite por defecto es de 10 GB por repositorio. Con runners self-hosted, la cache igual se guarda
en almacenamiento de GitHub; un almacenamiento propio solo existe en GitHub Enterprise Server. Los
pull requests desde forks solo leen la cache de la rama principal, para que no puedan envenenarla.

**Attestations**: una attestation es una afirmación firmada que liga un artifact con el
workflow, el repositorio, el commit, el evento y el environment que lo produjeron. La firma usa
la identidad OIDC del job: un token de vida corta que GitHub emite para esa ejecución. Se
verifica con `gh attestation verify`. Según GitHub, da SLSA Build Level 2 por sí sola: el build
corre en una plataforma hospedada que firma la procedencia, así que falsificarla exige un ataque
deliberado (los niveles de SLSA están en [Cadena de suministro de software](cadena-de-suministro-de-software.md)). No dice que el artifact sea seguro: solo de dónde salió.

## Ejemplo

El job `build` restaura `~/.npm` desde la cache con `key: npm-${{ hashFiles('package-lock.json') }}`,
compila, sube `dist/` como artifact y genera su attestation. El job `deploy` baja ese artifact.

## No confundir con

Un paquete o una imagen publicada. El artifact vive en la ejecución y vence; lo que se despliega
a largo plazo va a un registro, con la procedencia que describe
[Cadena de suministro de software](cadena-de-suministro-de-software.md).

## Relaciones

- Requiere: [GitHub Actions](github-actions.md) — jobs, runners y steps.
- Ver también: [Cadena de suministro de software](cadena-de-suministro-de-software.md) — las attestations son una pieza de la procedencia del software.
