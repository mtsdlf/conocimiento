---
tipo: concepto
resumen: >-
  Git guarda cada versión como snapshot en una base de objetos direccionada por contenido (blob,
  tree, commit, tag), donde el nombre de cada objeto es el hash de su contenido; los commits
  forman un grafo dirigido acíclico.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Scott Chacon y Ben Straub, Pro Git, 10.2 Git Objects: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects"
  - "Git Documentation, git-cat-file: https://git-scm.com/docs/git-cat-file"
  - "Git Documentation, git-init (--object-format): https://git-scm.com/docs/git-init"
  - "Git Documentation, hash-function-transition: https://git-scm.com/docs/hash-function-transition"
  - "Archivo/Desarrollo/git/git-mastery-manual.md y git-mecanismos-internos.md (originales, texto generado con IA)"
aliases: [Git objects, Objetos de Git, Base de objetos de Git, Git internals, DAG de commits]
parte_de: []
requiere: []
relacionado: []
---

# Modelo de objetos de Git

Git guarda cada versión como snapshot en una base de objetos direccionada por contenido (blob,
tree, commit, tag), donde el nombre de cada objeto es el hash de su contenido; los commits
forman un grafo dirigido acíclico.

## Por qué importa

Casi todo lo que hace Git se explica con este modelo: por qué un branch no cuesta nada, por qué
un rebase cambia los hashes, por qué un commit "perdido" se puede recuperar. Sin él, cada comando
es una receta para memorizar.

## Cómo funciona

La carpeta `.git/objects/` es una base clave–valor. Git comprime cada objeto con zlib y lo guarda
con el hash de su contenido como nombre: los dos primeros caracteres son la subcarpeta y el resto,
el archivo. Hay cuatro tipos:

| Objeto | Contiene |
|---|---|
| **blob** | el contenido de un archivo, sin nombre ni permisos |
| **tree** | un directorio: nombres, permisos y el hash de cada blob o tree hijo |
| **commit** | el hash del tree raíz, los padres, autor, committer, fecha y mensaje |
| **tag** (anotado) | un puntero a otro objeto, con autor, fecha, mensaje y firma opcional |

Un commit apunta al snapshot completo del proyecto, no a un diff. Los archivos que no cambiaron
reutilizan el mismo blob, porque tienen el mismo hash: cada contenido se guarda una sola vez.

Los padres forman el historial: un commit sin padre es la raíz, uno con un padre es lineal y uno
con dos o más es un merge. Como un objeto se nombra por su contenido, cambiar cualquier dato de un
commit (el mensaje, un padre) produce otro hash: un commit no se modifica, se reemplaza.

El hash por defecto es SHA-1. Git también soporta SHA-256 con `git init --object-format=sha256`;
un repositorio SHA-256 no interopera con uno SHA-1, y el proyecto planea cambiar el default en
Git 3.0.

Con el tiempo, `git gc` empaqueta los objetos sueltos en **packfiles**, que guardan unos objetos
como diferencias de otros parecidos; el modelo lógico no cambia.

## Ejemplo

```text
$ git cat-file -p HEAD
tree 9bc1dc4…
parent 3f2a7e1…
author Ana <ana@ejemplo.com> 1759500000 -0300
committer Ana <ana@ejemplo.com> 1759500000 -0300

Agrega validación de SKU
```

`git cat-file -p 9bc1dc4` lista el tree raíz con sus blobs y subdirectorios.

## No confundir con

Un sistema que guarda diferencias, como Subversion. Ahí una versión se reconstruye aplicando
deltas; en Git, cada commit ya nombra su snapshot completo, y la compresión por deltas es un
detalle del almacenamiento.

## Relaciones

- Base de: [Index de Git](index-de-git.md) — el index arma el tree del próximo commit.
- Base de: [Branch (Git)](branch-git.md) — un branch es un nombre para el hash de un commit.
- Ver también: [Comandos de Git](comandos-de-git.md) — los comandos de plumbing para inspeccionar objetos.
