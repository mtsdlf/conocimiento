---
resumen: >-
  Cómo deshacer un commit o recuperar uno perdido en Git con `restore`, `revert`, `reset` y
  `reflog`, según el cambio esté o no publicado.
estado: borrador
estabilidad: semi
revisado:
creado: 2026-10-03
fuentes:
  - "Git Documentation, git-reflog: https://git-scm.com/docs/git-reflog"
  - "Git Documentation, git-reset: https://git-scm.com/docs/git-reset"
  - "Git Documentation, git-revert: https://git-scm.com/docs/git-revert"
  - "Git Documentation, git-restore: https://git-scm.com/docs/git-restore"
  - "Git Documentation, git-branch: https://git-scm.com/docs/git-branch"
  - "Git Documentation, git-config (gc.reflogExpire, gc.pruneExpire): https://git-scm.com/docs/git-config"
  - "Archivo/Desarrollo/git/git-mastery-manual.md y git-mecanismos-internos.md (originales, texto generado con IA; su `git branch restore` no existe y su secuencia con `switch -d` estaba mal)"
aliases: [Deshacer en Git, git reflog, git reset, git revert, Recuperar un branch borrado, Undo Git]
---

# Recuperar trabajo perdido en Git

Cómo deshacer un commit o recuperar uno perdido en Git con `restore`, `revert`, `reset` y
`reflog`, según el cambio esté o no publicado.

## Lo que el reflog guarda y lo que no

- Entender que un branch es un puntero a un commit: [Branch (Git)](branch-git.md). Casi toda recuperación es
  volver a apuntar un branch al commit correcto.
- Lo que nunca se commiteó no está en el reflog: los cambios descartados con `git restore` o
  `git reset --hard` se pierden. Antes de esos comandos, `git stash` los guarda.
- La pregunta que decide el comando: ¿el commit ya está en un remoto que otros usan? Si está,
  no se reescribe: se agrega un commit que lo deshace.

## Del comando según la situación al branch de rescate

1. **Elegí la operación según la situación**:

   | Situación | Comando |
   |---|---|
   | descartar cambios sin agregar de un archivo | `git restore <archivo>` |
   | sacar un archivo del [index](index-de-git.md) sin perder los cambios | `git restore --staged <archivo>` |
   | corregir el último commit, sin publicar | `git commit --amend` |
   | deshacer un commit publicado | `git revert <sha>` (crea un commit inverso) |
   | deshacer un merge publicado | `git revert -m 1 <sha-del-merge>` (`-m 1`: el primer padre es la línea principal) |
   | deshacer commits locales y conservar los cambios en el index | `git reset --soft HEAD~1` |
   | deshacer commits locales y dejar los cambios sin agregar | `git reset HEAD~1` (`--mixed`, el modo por defecto) |
   | deshacer commits locales y descartar los cambios | `git reset --hard HEAD~1` |
   | volver atrás un merge, rebase o reset recién hecho, sin publicar | `git reset --hard ORIG_HEAD` (`ORIG_HEAD` guarda dónde estaba HEAD antes de esa operación) |

2. **Si un commit se perdió** (por un `reset --hard`, un [rebase](rebase.md) o un branch borrado), buscalo en el
   reflog: `git reflog` lista cada posición que tuvo HEAD, la más reciente arriba, como
   `HEAD@{0}`, `HEAD@{1}`…

   ```text
   $ git reflog
   a1b2c3d HEAD@{0}: reset: moving to HEAD~3
   9f8e7d6 HEAD@{1}: commit: Agrega validación de SKU
   ```

3. **Creá un branch en ese punto**: `git branch rescate HEAD@{1}` o `git switch -c rescate 9f8e7d6`.
   No existe `git branch restore`: el comando es `git branch <nombre> <commit>`.
4. **Si el reflog no lo muestra** (por ejemplo, un commit que nunca estuvo en HEAD de este clon),
   buscá commits sueltos con `git fsck --lost-found`, que los deja en `.git/lost-found/`, o traelo de otro clon o de un
   [Mirror de Git](mirror-de-git.md).

Hay plazo: por defecto, las entradas del reflog duran 90 días, o 30 si el commit ya no es
alcanzable desde ningún branch (`gc.reflogExpire` y `gc.reflogExpireUnreachable`). Después,
`git gc` puede borrar los objetos sueltos con más de dos semanas (`gc.pruneExpire`).

## Los commits recuperados en el branch

`git log --oneline -5 rescate` muestra los commits recuperados, y `git status` no tiene cambios
inesperados.
