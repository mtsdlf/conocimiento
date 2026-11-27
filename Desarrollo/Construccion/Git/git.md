---
resumen: >-
  Git es el sistema de control de versiones del desarrollo: guarda cada versión como snapshot en
  una base de objetos direccionada por contenido, nombra commits con punteros baratos y combina
  historiales que divergieron.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-10-03
revisado:
---

# Git

Git es el sistema de control de versiones del desarrollo: guarda cada versión como snapshot en
una base de objetos direccionada por contenido, nombra commits con punteros baratos y combina
historiales que divergieron.

Dentro de [Construcción](../construccion.md), en [Desarrollo](../../desarrollo.md), versiona lo que sale de
la [plantilla de proyecto](../plantilla-de-proyecto.md), y
[Configuración](../Configuracion/configuracion.md) decide qué queda fuera del historial. Esta parte trata la
herramienta. Cómo se organiza un equipo alrededor de Git está en DevOps:
[Estrategia de branching](../../../DevOps/Ramas-y-versiones/estrategia-de-branching.md) (con [Trunk-based development](../../../DevOps/Ramas-y-versiones/trunk-based-development.md) y [Gitflow](../../../DevOps/Ramas-y-versiones/gitflow.md)),
[Versionado semántico](../../../DevOps/Ramas-y-versiones/versionado-semantico.md), [Conventional Commits](../../../DevOps/Ramas-y-versiones/conventional-commits.md), [Gobernanza de repositorios](../../../DevOps/Repositorios/gobernanza-de-repositorios.md) y
[Monorepo y multirepo](../../../DevOps/Repositorios/monorepo-y-multirepo.md).

## Objetos, index y punteros

Casi todo lo que hace Git se explica con su modelo de objetos. Un blob guarda el contenido de un
archivo, un tree un directorio y un commit el tree raíz con sus padres; cada objeto se nombra por
el hash de su contenido, así que un commit no se modifica, se reemplaza. El index está entre el
directorio de trabajo y el historial, y arma el próximo commit. Un branch es solo un archivo con
el hash de un commit: crearlo no cuesta nada, y borrarlo no borra los commits.

## Integrar, deshacer y recuperar

Dos branches que divergieron se integran de dos formas. El merge de tres vías combina las puntas a
partir del ancestro común y marca conflicto donde los dos lados tocan las mismas líneas. El rebase
reaplica los commits de un lado sobre otra base, con hashes nuevos, y por eso no se usa sobre
branches compartidos. Como los commits viejos siguen en el reflog hasta que vence, casi toda
recuperación es volver a apuntar un branch al commit correcto.

## Automatizar y escalar

Los hooks corren scripts en eventos del ciclo de Git: del lado del cliente ayudan a quien
desarrolla y del lado del servidor imponen reglas. En un repositorio grande, Git se vuelve usable
descargando y mostrando menos; los binarios grandes se resuelven aparte, con LFS. Un mirror copia
todas las refs del original, para respaldo, cache de CI o réplica.

## Lo que hay adentro de Git

En orden de lectura, de lo de adentro a lo de afuera:

- [Modelo de objetos de Git](modelo-de-objetos-de-git.md) — blobs, trees, commits y tags en una base direccionada por
  contenido; la base de todas las demás notas.
- [Index de Git](index-de-git.md) — el área donde se arma el próximo commit; leerla para commitear solo una
  parte de los cambios.
- [Branch (Git)](branch-git.md) — qué es un branch, HEAD y un tag, y por qué crearlos no cuesta nada.
- [Merge de tres vías](merge-de-tres-vias.md) — cómo combina Git dos branches que divergieron; leerla antes que rebase.
- [Resolver conflictos de merge](resolver-conflictos-de-merge.md) — pasos para cuando un merge o un rebase se frena en un
  conflicto, y cómo automatizar los que se repiten.
- [Rebase](rebase.md) — reaplicar commits sobre otra base, cherry-pick y rebase interactivo; cuándo no usarlo.
- [Recuperar trabajo perdido en Git](recuperar-trabajo-perdido-en-git.md) — pasos para cuando se commiteó, se borró o se reseteó
  algo por error: qué comando usar según el cambio esté publicado o no.
- [Hook de Git](hook-de-git.md) — scripts que Git corre antes o después de un commit o un push; leerla para
  validar algo antes de que llegue al remoto.
- [Git LFS](git-lfs.md) — cómo versionar archivos binarios grandes sin inflar cada clon; leerla antes de
  agregar diseños, videos o datasets a un repo.
- [Git en repositorios grandes](git-en-repositorios-grandes.md) — qué hacer cuando clonar o `git status` tardan: clon parcial,
  sparse checkout, worktrees y mantenimiento.
- [Mirror de Git](mirror-de-git.md) — copias completas de un repositorio para respaldo, CI o réplica.
- [Comandos de Git](comandos-de-git.md) — la ficha con los comandos del día a día y de mantenimiento, por tarea.

Los manuales en los que se basa esta parte (texto generado con IA, con errores corregidos acá)
están en `Archivo/Desarrollo/git/` y `Archivo/DevOps/git/`.
