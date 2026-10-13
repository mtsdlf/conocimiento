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
[[estrategia-de-branching]] (con [[trunk-based-development]] y [[gitflow]]),
[[versionado-semantico]], [[conventional-commits]], [[gobernanza-de-repositorios]] y
[[monorepo-y-multirepo]].

## Cómo funciona por dentro (en orden de lectura)

- [[modelo-de-objetos-de-git]] — blobs, trees, commits y tags en una base direccionada por
  contenido; la base de todas las demás notas.
- [[index-de-git]] — el área donde se arma el próximo commit; leerla para commitear solo una
  parte de los cambios.
- [[branch-git]] — qué es un branch, HEAD y un tag, y por qué crearlos no cuesta nada.

## Integrar cambios

- [[merge-de-tres-vias]] — cómo combina Git dos branches que divergieron; leerla antes que rebase.
- [[resolver-conflictos-de-merge]] — pasos para cuando un merge o un rebase se frena en un
  conflicto, y cómo automatizar los que se repiten.
- [[rebase]] — reaplicar commits sobre otra base, cherry-pick y rebase interactivo; cuándo no usarlo.

## Deshacer y recuperar

- [[recuperar-trabajo-perdido-en-git]] — pasos para cuando se commiteó, se borró o se reseteó
  algo por error: qué comando usar según el cambio esté publicado o no.

## Automatizar y escalar

- [[hook-de-git]] — scripts que Git corre antes o después de un commit o un push; leerla para
  validar algo antes de que llegue al remoto.
- [[git-lfs]] — cómo versionar archivos binarios grandes sin inflar cada clon; leerla antes de
  agregar diseños, videos o datasets a un repo.
- [[git-en-repositorios-grandes]] — qué hacer cuando clonar o `git status` tardan: clon parcial,
  sparse checkout, worktrees y mantenimiento.
- [[mirror-de-git]] — copias completas de un repositorio para respaldo, CI o réplica.

## Consulta

- [[comandos-de-git]] — la ficha con los comandos del día a día y de mantenimiento, por tarea.

## Originales archivados

Los manuales en los que se basa este sub-Tema (texto generado con IA, con errores corregidos acá)
están en `Archivo/Desarrollo/git/` y `Archivo/DevOps/git/`.
