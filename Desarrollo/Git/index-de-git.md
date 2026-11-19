---
tipo: concepto
resumen: >-
  El index (staging area) es el archivo `.git/index` que guarda el próximo commit: está entre el
  directorio de trabajo y el historial, y permite elegir qué cambios entran.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Scott Chacon y Ben Straub, Pro Git, 1.3 What is Git? (The Three States): https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F"
  - "Git Documentation, git-add (--patch): https://git-scm.com/docs/git-add"
  - "Git Documentation, git-restore: https://git-scm.com/docs/git-restore"
  - "Git Documentation, gitformat-index: https://git-scm.com/docs/gitformat-index"
  - "Archivo/Desarrollo/git/git-mastery-manual.md y git-mecanismos-internos.md (originales, texto generado con IA)"
aliases: [Staging area, Index, Área de preparación, Stage, Los tres estados de Git]
parte_de: []
requiere: [modelo-de-objetos-de-git]
relacionado: []
---

# Index de Git

El index (staging area) es el archivo `.git/index` que guarda el próximo commit: está entre el
directorio de trabajo y el historial, y permite elegir qué cambios entran.

## Por qué importa

Una tarde de trabajo suele mezclar un arreglo, un cambio de formato y un log de depuración. El
index permite commitear solo el arreglo, aunque esté en el mismo archivo que lo demás, y dejar un
historial donde cada commit hace una sola cosa.

## Cómo funciona

Un archivo puede estar en tres lugares, y cada comando lo mueve entre ellos:

| Lugar | Qué es | Comandos que lo cambian |
|---|---|---|
| **Directorio de trabajo** | los archivos que se editan | el editor; `git restore <archivo>` lo vuelve al index |
| **Index** | la lista de rutas con el hash del blob de cada una: el snapshot del próximo commit | `git add`, `git restore --staged`, `git rm` |
| **Repositorio** | los commits, en `.git/objects` | `git commit` |

`git add` no es una marca que sigue al archivo: guarda su contenido de ese momento como blob y
anota el hash en el index (si el archivo es nuevo, además empieza a versionarse). Si el archivo cambia después del `add`, el commit lleva la versión vieja
hasta el próximo `add`. `git commit` convierte el index en trees y escribe un commit nuevo que
apunta a ellos; ver [Modelo de objetos de Git](modelo-de-objetos-de-git.md).

`git add -p` muestra cada bloque de cambios (hunk) y pregunta si entra. Así se commitea una parte
de un archivo.

`git status` compara los tres lugares: "Changes to be committed" es la diferencia entre el index y
el último commit, y "Changes not staged" es la diferencia entre el directorio de trabajo y el
index. `git diff` muestra la segunda; `git diff --staged`, la primera.

## Ejemplo

```bash
git add -p servicio.py        # elegir solo el hunk del arreglo
git diff --staged             # revisar qué entra
git commit -m "Corrige el redondeo del total"
git restore servicio.py       # descartar el log de depuración que quedó sin agregar
```

## No confundir con

El stash. El index arma el próximo commit; `git stash` guarda aparte los cambios del directorio
de trabajo y del index para limpiar el árbol y retomarlos después.

## Relaciones

- Requiere: [Modelo de objetos de Git](modelo-de-objetos-de-git.md) — el index guarda hashes de blobs y se convierte en trees.
- Ver también: [Recuperar trabajo perdido en Git](recuperar-trabajo-perdido-en-git.md) — cómo sacar algo del index o volver atrás un commit.
