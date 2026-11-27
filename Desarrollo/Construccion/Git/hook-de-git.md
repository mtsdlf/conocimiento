---
resumen: >-
  Un hook de Git es un script que Git ejecuta en un evento de su ciclo (antes de un commit, al
  recibir un push); del lado del cliente ayuda a quien desarrolla, y del lado del servidor impone
  reglas.
estado: borrador
estabilidad: estable
revisado:
creado: 2026-10-03
fuentes:
  - "Git Documentation, githooks: https://git-scm.com/docs/githooks"
  - "Scott Chacon y Ben Straub, Pro Git, 8.3 Git Hooks: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks"
  - "Git Documentation, git-config (core.hooksPath): https://git-scm.com/docs/git-config"
  - "pre-commit, A framework for managing and maintaining multi-language pre-commit hooks: https://pre-commit.com/"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
aliases: [Git hook, Hooks de Git, pre-commit, pre-receive, commit-msg, core.hooksPath]
---

# Hook de Git

Un hook de Git es un script que Git ejecuta en un evento de su ciclo (antes de un commit, al
recibir un push); del lado del cliente ayuda a quien desarrolla, y del lado del servidor impone
reglas.

## Avisar antes del commit, rechazar en el servidor

Un formateador o un detector de secretos que corre solo en CI avisa minutos después del push,
cuando el secreto ya salió de la máquina. Un hook local avisa antes del commit. Y un hook de
servidor es la única forma, en un servidor Git propio, de rechazar un push que no cumple una
regla.

## Hooks de cliente y de servidor

Un hook es un archivo ejecutable (con permiso de ejecución) en `.git/hooks/`, con el nombre del
evento. Si un hook que corre antes de la acción (`pre-commit`, `commit-msg`, `pre-push`,
`pre-receive`, `update`) sale con un código distinto de cero, Git cancela la operación.

| Lado | Hook | Cuándo corre | Uso típico |
|---|---|---|---|
| cliente | `pre-commit` | antes de crear el commit | formato, lint, secretos |
| cliente | `commit-msg` | con el mensaje ya escrito | validar el formato del mensaje |
| cliente | `pre-push` | antes de enviar | pruebas rápidas |
| cliente | `post-checkout`, `post-merge` | después de cambiar de branch o de un merge | reinstalar dependencias |
| servidor | `pre-receive` | al recibir un push, antes de actualizar refs | rechazar commits sin firma o pushes a ramas protegidas |
| servidor | `update` | una vez por ref | lo mismo, ref por ref |
| servidor | `post-receive` | después de actualizar | notificar, disparar un despliegue |

Los hooks del cliente **no se clonan**: `.git/hooks/` no se versiona. Para compartirlos, el equipo
los guarda en una carpeta del repo y cada persona apunta Git ahí con
`git config core.hooksPath .githooks`, o usa un gestor como el framework pre-commit, que lee un
`.pre-commit-config.yaml` versionado. Como cualquiera puede saltarlos con `git commit
--no-verify`, las mismas verificaciones corren también en CI.

En GitHub o GitLab en la nube no se instalan hooks de servidor; el equivalente son las reglas de
protección de ramas y los checks obligatorios.

## Gitleaks en pre-commit

`.pre-commit-config.yaml` con Gitleaks: al hacer `git commit`, el framework corre Gitleaks sobre
los archivos agregados al index y, si encuentra una clave, el commit no se crea.

## Hook y webhook

Un webhook. El webhook lo dispara la plataforma (GitHub, GitLab) y manda un HTTP POST a otro
sistema, por ejemplo un servidor de CI; no lo ejecuta Git ni corre en la máquina de quien
desarrolla.

## Ver también

- [Gestión de secretos](../../../DevOps/DevSecOps/gestion-de-secretos.md) (DevOps) — la detección de secretos en pre-commit.
- [Conventional Commits](../../../DevOps/Ramas-y-versiones/conventional-commits.md) (DevOps) — el formato que valida un hook `commit-msg`.
- [Gobernanza de repositorios](../../../DevOps/Repositorios/gobernanza-de-repositorios.md) (DevOps) — las reglas que imponen los hooks de servidor o la plataforma.
