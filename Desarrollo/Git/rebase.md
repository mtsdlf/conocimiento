---
resumen: >-
  Rebase reaplica los commits de un branch sobre otra base, creando commits nuevos con hashes
  nuevos; por eso no se usa sobre branches compartidos. Incluye cherry-pick y el rebase
  interactivo.
estado: borrador
estabilidad: estable
revisado:
creado: 2026-10-03
fuentes:
  - "Git Documentation, git-rebase: https://git-scm.com/docs/git-rebase"
  - "Git Documentation, git-cherry-pick: https://git-scm.com/docs/git-cherry-pick"
  - "Scott Chacon y Ben Straub, Pro Git, 3.6 Rebasing (The Perils of Rebasing): https://git-scm.com/book/en/v2/Git-Branching-Rebasing"
  - "Archivo/Desarrollo/git/git-mastery-manual.md y git-mecanismos-internos.md, y Archivo/DevOps/git/git-organizational-topology.md (originales, texto generado con IA)"
aliases: [git rebase, Rebasar, Cherry-pick, Rebase interactivo, Autosquash, Reescribir el historial]
---

# Rebase

Rebase reaplica los commits de un branch sobre otra base, creando commits nuevos con hashes
nuevos; por eso no se usa sobre branches compartidos. Incluye cherry-pick y el rebase
interactivo.

## Un PR con solo los cambios propios

Un branch que salió de `main` hace una semana muestra, en su PR, cambios mezclados con los de
otros. Rebasarlo sobre la punta actual de `main` deja solo los cambios propios, en un historial
lineal que se lee y se bisecta más fácil. El costo es reescribir commits: si alguien más ya los
tenía, sus copias quedan huérfanas.

## Reaplicar commits y la regla de Pro Git

`git rebase main` estando en `feature`:

1. busca el ancestro común de `feature` y `main`;
2. toma cada commit de `feature` posterior a ese ancestro como un parche;
3. lo aplica, uno por uno, sobre la punta de `main`, y crea un commit nuevo con otro padre y, por
   lo tanto, otro hash (ver [Modelo de objetos de Git](modelo-de-objetos-de-git.md));
4. mueve el [branch](branch-git.md) `feature` al último commit nuevo.

Si un parche choca, el rebase para en ese commit con un conflicto, que se resuelve como en un
merge: ver [Resolver conflictos de merge](resolver-conflictos-de-merge.md).

Los commits viejos no se borran: siguen en el reflog hasta que vence. Por eso un rebase mal hecho
se deshace; ver [Recuperar trabajo perdido en Git](recuperar-trabajo-perdido-en-git.md).

La regla de Pro Git: no se rebasan commits que ya existen fuera del repositorio propio y sobre los
que otros pudieron basar trabajo. Si hay que publicar un branch propio rebasado, se usa
`git push --force-with-lease`, que falla si el remoto cambió desde el último fetch.

Variantes:

- **Rebase interactivo** (`git rebase -i HEAD~5`): una lista editable para reordenar, juntar
  (`squash`, `fixup`), editar o borrar commits. Con `git commit --fixup <sha>` y
  `git rebase -i --autosquash`, los arreglos se juntan solos con su commit.
- **`--rebase-merges`**: conserva los merge commits del branch en lugar de aplanarlos.
- **`--update-refs`** (Git 2.38): mueve también los branches que apuntaban a commits rebasados,
  útil con PRs apilados.
- **Cherry-pick** (`git cherry-pick <sha>`): aplica un solo commit sobre el branch actual, con
  hash nuevo. Con `-x`, el mensaje anota "(cherry picked from commit …)", para trazar un hotfix
  llevado a un branch de release.

## Rebasar una feature sobre origin/main

```bash
git switch feature/login
git fetch origin
git rebase origin/main            # reaplica los 3 commits de la feature sobre main
git push --force-with-lease       # el branch es solo mío: se puede reescribir
```

## Rebase y merge

Un [Merge de tres vías](merge-de-tres-vias.md). El merge no toca los commits existentes y agrega uno que une los dos
historiales; es seguro sobre branches compartidos. El rebase da un historial lineal a cambio de
reescribir.

## Ver también

- [Estrategia de branching](../../DevOps/Ramas-y-versiones/estrategia-de-branching.md) (DevOps) — rebasar antes del PR como política de equipo.
