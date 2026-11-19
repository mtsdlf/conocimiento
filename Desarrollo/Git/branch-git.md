---
tipo: concepto
resumen: >-
  En Git, un branch es un archivo que guarda el hash de un commit y avanza con cada commit nuevo;
  HEAD apunta al branch actual, y un tag es un puntero que no avanza.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Scott Chacon y Ben Straub, Pro Git, 3.1 Branches in a Nutshell: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell"
  - "Scott Chacon y Ben Straub, Pro Git, 10.3 Git References: https://git-scm.com/book/en/v2/Git-Internals-Git-References"
  - "Git Documentation, git-tag (On Re-tagging): https://git-scm.com/docs/git-tag"
  - "Git Documentation, git-switch: https://git-scm.com/docs/git-switch"
  - "Archivo/Desarrollo/git/git-mastery-manual.md y git-mecanismos-internos.md (originales, texto generado con IA)"
aliases: [Branch, Rama (Git), HEAD, Ref, Referencia de Git, Tag (Git), Detached HEAD]
parte_de: []
requiere: [modelo-de-objetos-de-git]
relacionado: []
---

# Branch (Git)

En Git, un branch es un archivo que guarda el hash de un commit y avanza con cada commit nuevo;
HEAD apunta al branch actual, y un tag es un puntero que no avanza.

## Por qué importa

Como un branch son 41 bytes en un archivo, crearlo o borrarlo es instantáneo, y trabajar en un
branch por cambio no tiene costo. Entender que es solo un puntero explica qué se pierde y qué no
cuando se borra uno: los commits siguen en la base hasta que nada los alcanza.

## Cómo funciona

Las **refs** son nombres para hashes de commits:

| Ref | Dónde vive | Cómo se mueve |
|---|---|---|
| branch local | `.git/refs/heads/<nombre>` | avanza solo con cada commit hecho sobre él |
| branch remoto (`origin/main`) | `.git/refs/remotes/origin/<nombre>` | con `git fetch` (también el de `git pull`) y con `git push`: es la última posición conocida del remoto |
| tag | `.git/refs/tags/<nombre>` | no se mueve solo |
| HEAD | `.git/HEAD` | cambia con `git switch` o `git checkout` |

Con el tiempo, Git puede juntar muchas refs en el archivo `.git/packed-refs`; por eso conviene
leerlas con `git rev-parse <ref>` y no abriendo los archivos.

**HEAD** suele ser una ref simbólica: contiene `ref: refs/heads/main`, y un commit nuevo hace
avanzar a `main`. Si se hace checkout de un commit o de un tag, HEAD guarda un hash directo:
es el estado **detached HEAD**. Los commits hechos ahí no los alcanza ningún branch; para
conservarlos, `git switch -c <nombre>` crea un branch en ese punto.

Un **tag** liviano es solo la ref; uno **anotado** (`git tag -a`) apunta a un objeto tag con
autor, fecha, mensaje y firma opcional (`-s`). Por convención, los releases usan tags anotados. Un tag no es
inmutable: `git tag -f` lo mueve. La documentación de `git tag` desaconseja mover un tag ya
publicado, porque quien lo bajó conserva la versión vieja; si hubo un error, se publica otro tag.

## Ejemplo

```text
$ cat .git/HEAD
ref: refs/heads/feature/login
$ git rev-parse feature/login
3f2a7e1c…
$ git commit -m "Agrega el formulario"
$ git rev-parse feature/login
8d41b0a…            # el branch avanzó; main sigue donde estaba
```

## No confundir con

Una copia del código. Un branch no duplica archivos: los commits y los blobs son los mismos, y
solo cambia qué commit nombra el puntero.

## Relaciones

- Requiere: [Modelo de objetos de Git](modelo-de-objetos-de-git.md) — un branch apunta a un commit, que apunta a un tree.
- Base de: [Merge de tres vías](merge-de-tres-vias.md) — combina las puntas de dos branches.
- Base de: [Rebase](rebase.md) — mueve los commits de un branch a otra base.
- Base de: [Recuperar trabajo perdido en Git](recuperar-trabajo-perdido-en-git.md) — recuperar es volver a apuntar un branch a un commit.
- Ver también: [Estrategia de branching](../../DevOps/estrategia-de-branching.md) (DevOps) — qué branches tiene un equipo y cómo se integran.
