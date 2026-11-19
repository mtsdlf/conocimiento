---
resumen: >-
  Un secret de GitHub Actions es una variable cifrada, definida a nivel de organización,
  repositorio o environment, que un workflow lee solo si la nombra y que GitHub tapa en los logs.
estado: borrador
estabilidad: estable
fuentes:
  - "Archivo/Automatizacion/github-actions-referencia.md"
  - "GitHub Docs, Secrets: https://docs.github.com/en/actions/concepts/security/secrets"
  - "GitHub Docs, Secrets reference: https://docs.github.com/en/actions/reference/security/secrets"
  - "GitHub Docs, Secure use reference: https://docs.github.com/en/actions/reference/security/secure-use"
aliases: [GitHub secret, Actions secret, Secreto de GitHub Actions]
creado: 2026-10-03
revisado:
---

# Secret de GitHub Actions

Un secret de GitHub Actions es una variable cifrada, definida a nivel de organización,
repositorio o environment, que un workflow lee solo si la nombra y que GitHub tapa en los logs.

## Por qué el valor no va en el YAML

Un workflow necesita credenciales para publicar una imagen o desplegar, y el YAML está en el
repositorio a la vista de todos. El secret mantiene el valor fuera del código y limita qué
workflows y qué jobs lo reciben.

## Niveles, cifrado, redacción y buenas prácticas

- **Dónde se crea**: en **Settings > Secrets and variables > Actions** del repositorio o de la
  organización, o en la página del environment.
- **Niveles**: organización (compartido entre repositorios, con una política de cuáles lo ven),
  repositorio y environment. Si el mismo nombre existe en los tres, gana el del environment.
- **Cifrado**: el valor se cifra con una sealed box de libsodium antes de llegar a GitHub, y se
  descifra recién para inyectarlo en el runner.
- **Acceso explícito**: un step lo recibe solo si el workflow lo pasa con `${{ secrets.NOMBRE }}`
  como input o variable de entorno.
- **Redacción**: GitHub reemplaza el valor en los logs. Si el valor se transforma (Base64, URL), la
  redacción puede fallar; por eso cada valor sensible va en su propio secret, nunca dentro de un
  JSON o YAML.
- **Límites**: 48 KB por secret; hasta 100 por repositorio y 1.000 por organización.

**Buenas prácticas**, según GitHub:

- permisos mínimos, y solo lectura si alcanza;
- una GitHub App antes que un token personal: permisos finos, tokens de vida corta y sin depender
  de un usuario que puede irse;
- con un token personal, el fine-grained con los permisos mínimos;
- para la nube, OIDC (OpenID Connect) en vez de una credencial de larga vida: el workflow cambia
  un token de vida corta que emite GitHub por un acceso temporal en el proveedor;
- el `GITHUB_TOKEN`, el token que GitHub crea en cada ejecución para operar sobre el propio
  repositorio, con permisos de solo lectura por defecto, ampliados por job.

## `REGISTRY_TOKEN` solo para el job deploy

El secret `REGISTRY_TOKEN` vive en el environment `production`. Solo el job `deploy`, que declara
ese environment y pasó su aprobación, lo recibe como variable de entorno.

## Un secret no es una variable de configuración

Una variable de configuración (`vars`). Las variables no se cifran ni se tapan en los logs: son
para valores no sensibles, como una región o un nombre de imagen.

## Ver también

- [GitHub Actions](github-actions.md) — workflows, jobs y steps.
- [Environment de GitHub Actions](environment-de-github-actions.md) — el nivel más restringido para guardar un secret.
- [Gestión de secretos](../../DevSecOps/gestion-de-secretos.md) — la práctica general de mantener credenciales fuera del código.
