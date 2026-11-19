---
tipo: mapa
resumen: >-
  Cómo funciona Git por dentro y cómo se usa: el modelo de objetos, el index, los branches, merge
  y rebase, la recuperación, los hooks, LFS, los repositorios grandes, los mirrors y los comandos
  de cada día.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [desarrollo]
---

# Git

Cómo funciona Git por dentro y cómo se usa: el modelo de objetos, el index, los branches, merge
y rebase, la recuperación, los hooks, LFS, los repositorios grandes, los mirrors y los comandos
de cada día.

Este sub-Mapa trata la herramienta. Cómo se organiza un equipo alrededor de Git está en DevOps:
[Estrategia de branching](../../DevOps/estrategia-de-branching.md) (con [Trunk-based development](../../DevOps/trunk-based-development.md) y [Gitflow](../../DevOps/gitflow.md)),
[Versionado semántico](../../DevOps/versionado-semantico.md), [Conventional Commits](../../DevOps/conventional-commits.md), [Gobernanza de repositorios](../../DevOps/gobernanza-de-repositorios.md) y
[Monorepo y multirepo](../../DevOps/monorepo-y-multirepo.md).

## Cómo funciona por dentro (en orden de lectura)

- [Modelo de objetos de Git](modelo-de-objetos-de-git.md) — blobs, trees, commits y tags en una base direccionada por
  contenido; la base de todas las demás notas.
- [Index de Git](index-de-git.md) — el área donde se arma el próximo commit; leerla para commitear solo una
  parte de los cambios.
- [Branch (Git)](branch-git.md) — qué es un branch, HEAD y un tag, y por qué crearlos no cuesta nada.

## Integrar cambios

- [Merge de tres vías](merge-de-tres-vias.md) — cómo combina Git dos branches que divergieron; leerla antes que rebase.
- [Resolver conflictos de merge](resolver-conflictos-de-merge.md) — pasos para cuando un merge o un rebase se frena en un
  conflicto, y cómo automatizar los que se repiten.
- [Rebase](rebase.md) — reaplicar commits sobre otra base, cherry-pick y rebase interactivo; cuándo no usarlo.

## Deshacer y recuperar

- [Recuperar trabajo perdido en Git](recuperar-trabajo-perdido-en-git.md) — pasos para cuando se commiteó, se borró o se reseteó
  algo por error: qué comando usar según el cambio esté publicado o no.

## Automatizar y escalar

- [Hook de Git](hook-de-git.md) — scripts que Git corre antes o después de un commit o un push; leerla para
  validar algo antes de que llegue al remoto.
- [Git LFS](git-lfs.md) — cómo versionar archivos binarios grandes sin inflar cada clon; leerla antes de
  agregar diseños, videos o datasets a un repo.
- [Git en repositorios grandes](git-en-repositorios-grandes.md) — qué hacer cuando clonar o `git status` tardan: clon parcial,
  sparse checkout, worktrees y mantenimiento.
- [Mirror de Git](mirror-de-git.md) — copias completas de un repositorio para respaldo, CI o réplica.

## Consulta

- [Comandos de Git](comandos-de-git.md) — la ficha con los comandos del día a día y de mantenimiento, por tarea.

## Originales archivados

Los manuales en los que se basa este sub-Tema (texto generado con IA, con errores corregidos acá)
están en `Archivo/Desarrollo/git/` y `Archivo/DevOps/git/`.
