---
resumen: >-
  En un repositorio grande, Git se vuelve usable descargando y mostrando menos: clon superficial o
  parcial, sparse checkout, worktrees y mantenimiento programado.
estado: borrador
estabilidad: estable
revisado:
creado: 2026-10-03
fuentes:
  - "Git Documentation, git-clone (--depth, --filter): https://git-scm.com/docs/git-clone"
  - "Git Documentation, partial-clone: https://git-scm.com/docs/partial-clone"
  - "Git Documentation, git-sparse-checkout: https://git-scm.com/docs/git-sparse-checkout"
  - "Git Documentation, git-worktree: https://git-scm.com/docs/git-worktree"
  - "Git Documentation, git-maintenance: https://git-scm.com/docs/git-maintenance"
  - "Git Documentation, scalar: https://git-scm.com/docs/scalar"
  - "Archivo/DevOps/git/git-scaling-performance.md (original, texto generado con IA)"
aliases: [Rendimiento de Git, Partial clone, Clon parcial, Shallow clone, Sparse checkout, git worktree, Scalar, Git a escala]
---

# Git en repositorios grandes

En un repositorio grande, Git se vuelve usable descargando y mostrando menos: clon superficial o
parcial, sparse checkout, worktrees y mantenimiento programado.

## Lo que se descarga y lo que se mira

Un clon normal descarga todos los objetos de toda la historia (ver
[Modelo de objetos de Git](modelo-de-objetos-de-git.md)). En un monorepo de años, eso puede ser decenas de GB y minutos de
espera en cada job de CI, y `git status` tarda porque recorre cientos de miles de archivos. Cada
técnica ataca una de esas dos cosas: lo que se descarga o lo que se mira.

## Siete técnicas y scalar

| Técnica | Comando | Qué ahorra | Para quién |
|---|---|---|---|
| **Clon superficial** | `git clone --depth=1` | la historia: trae solo el último commit | jobs de CI que solo construyen |
| **Clon parcial sin blobs** | `git clone --filter=blob:none` | el contenido de versiones viejas: los blobs se bajan al usarse | desarrollo diario; conserva `log` y `blame` |
| **Clon parcial sin trees** | `git clone --filter=tree:0` | también los directorios viejos | CI que necesita la historia de commits pero no los archivos |
| **Sparse checkout** | `git sparse-checkout set apps/web libs/ui` | archivos en disco: solo esas carpetas | quien trabaja en una parte de un monorepo |
| **Worktree** | `git worktree add ../hotfix release/2.3` | un segundo clon completo: es otro directorio de trabajo sobre el mismo `.git` | revisar un branch sin guardar el trabajo actual |
| **Mantenimiento** | `git maintenance start` | trabajo en primer plano: programa prefetch, commit-graph y repack incremental en segundo plano | repos que se usan todos los días |
| **Monitor de archivos** | `git config core.fsmonitor true` | `git status` lento: no recorre todo el árbol | árboles con muchos archivos |

El sparse checkout usa por defecto el **modo cone**, que acepta directorios y no patrones
sueltos, porque es mucho más rápido de evaluar; el modo sin cone está desaconsejado desde Git 2.37.

`scalar`, incluido en Git desde la 2.38, configura todo esto junto en un comando
(`scalar clone <url>`): clon parcial, sparse checkout, monitor de archivos y mantenimiento.

Los binarios grandes son otro problema: no se resuelven con estas técnicas sino con [Git LFS](git-lfs.md). Un
[mirror de Git](mirror-de-git.md) local, en cambio, sí acelera los clones de CI.

## Un job de CI y una persona de frontend

Un job de CI que solo compila usa `git clone --depth=1 --filter=blob:none`. Una persona del equipo
de frontend usa `scalar clone` y `git sparse-checkout set apps/web libs/ui`: su clon es chico y
`git status` responde rápido.

## Hacer viable un repo grande sin partirlo

Partir el repositorio. Pasar de monorepo a varios repos es una decisión de organización, con
otros costos; ver [Monorepo y multirepo](../../DevOps/Repositorios/monorepo-y-multirepo.md) en DevOps. Estas técnicas hacen viable un repo grande
sin partirlo.
