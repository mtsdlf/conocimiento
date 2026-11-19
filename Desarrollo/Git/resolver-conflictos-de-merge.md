---
tipo: como-hacer
resumen: >-
  Cómo resolver un conflicto de merge en Git: leer los marcadores, elegir o combinar cada bloque,
  continuar o abortar, y automatizar los conflictos repetidos con rerere y merge drivers.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Git Documentation, git-merge (How conflicts are presented): https://git-scm.com/docs/git-merge"
  - "Git Documentation, git-config (merge.conflictStyle): https://git-scm.com/docs/git-config"
  - "Git Documentation, git-rerere: https://git-scm.com/docs/git-rerere"
  - "Git Documentation, gitattributes (Defining a custom merge driver): https://git-scm.com/docs/gitattributes"
  - "Archivo/Desarrollo/git/git-mecanismos-internos.md y Archivo/DevOps/git/git-organizational-topology.md (originales, texto generado con IA)"
aliases: [Conflicto de merge, Merge conflict, rerere, Merge driver, Marcadores de conflicto]
parte_de: []
requiere: [merge-de-tres-vias]
relacionado: []
---

# Resolver conflictos de merge

Cómo resolver un conflicto de merge en Git: leer los marcadores, elegir o combinar cada bloque,
continuar o abortar, y automatizar los conflictos repetidos con rerere y merge drivers.

## Antes de empezar

- Entender qué son base, ours y theirs: [Merge de tres vías](merge-de-tres-vias.md).
- Activar una vez el estilo que muestra también la base, que hace legibles los conflictos:
  `git config --global merge.conflictStyle zdiff3` (desde Git 2.35; antes, `diff3`).

## Pasos

1. **Listá los archivos en conflicto**: `git status` (sección "Unmerged paths") o
   `git diff --name-only --diff-filter=U`.
2. **Leé cada bloque**. Con `zdiff3` tiene tres partes:

   ```text
   <<<<<<< HEAD
   timeout = 30
   ||||||| base
   timeout = 10
   =======
   timeout = 15
   >>>>>>> feature
   ```

   Arriba está el lado propio (`HEAD`, el branch actual), en el medio la base y abajo el branch que
   se integra. El texto de cada marcador varía.
   La base dice qué había antes: acá los dos lados cambiaron el mismo valor, y hay que decidir.
3. **Editá el archivo** hasta dejar el resultado correcto y borrá los marcadores. Para quedarte
   con un lado entero, usá `git restore --ours <archivo>` o `git restore --theirs <archivo>`.
   Si estás en un rebase, los lados se invierten: `ours` es la base nueva y `theirs`, tu commit.
4. **Marcá el archivo como resuelto**: `git add <archivo>`. `git diff --check` avisa si quedó
   algún marcador.
5. **Cerrá el merge**: `git merge --continue`. Si preferís volver al estado anterior,
   `git merge --abort`. En un rebase, los equivalentes son `git rebase --continue` y
   `git rebase --abort`.

## Automatizar conflictos repetidos

- **rerere** ("reuse recorded resolution"): con `git config --global rerere.enabled true`, Git
  guarda en `.git/rr-cache` cada conflicto con su resolución, y la reaplica si el mismo conflicto
  vuelve a aparecer. Revisá el resultado antes
  del `git add`.
- **Merge drivers**: en `.gitattributes` se elige cómo se combina cada tipo de archivo. Git trae
  `text` (el de defecto), `binary` (no combina: deja la versión propia y marca conflicto) y
  `union` (junta las líneas de los dos lados, útil para un `CHANGELOG`). Un driver propio se
  declara en la configuración:

  ```ini
  # .gitattributes:  *.json merge=json
  [merge "json"]
      name = merge de JSON
      driver = merge-json %O %A %B
  ```

  El comando recibe la base (`%O`), el lado propio (`%A`) y el otro (`%B`); tiene que dejar el
  resultado en el archivo `%A` y salir con 0 si combinó sin conflictos. Un driver escrito como
  `jq … %A %B > %A` vacía `%A` antes de leerlo, porque el shell abre la redirección primero:
  escribí a un archivo temporal y movelo.

## Cómo saber que salió bien

`git status` no muestra "Unmerged paths", `git log --graph -3` muestra el merge commit con dos
padres (en un rebase, los commits reaplicados en línea), y las pruebas pasan sobre el resultado.

## Relaciones

- Requiere: [Merge de tres vías](merge-de-tres-vias.md) — el conflicto es lo que queda sin resolver en las tres vías.
- Ver también: [Rebase](rebase.md) — un rebase genera los mismos conflictos, commit por commit.
