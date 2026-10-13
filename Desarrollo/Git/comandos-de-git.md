---
tipo: ficha
resumen: >-
  Los comandos de Git del día a día y de mantenimiento, agrupados por tarea: sincronizar, stash,
  diff y log, tags, bisect, submódulos, firma, plumbing y mantenimiento.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Git Documentation (referencia de cada comando): https://git-scm.com/docs"
  - "Git Documentation, gitrevisions (A..B, A...B): https://git-scm.com/docs/gitrevisions"
  - "Git Documentation, git-filter-branch (advertencia y alternativa filter-repo): https://git-scm.com/docs/git-filter-branch"
  - "Archivo/Desarrollo/git/git-mastery-manual.md y git-mecanismos-internos.md, y Archivo/DevOps/git/ (originales, texto generado con IA, comandos verificados contra la documentación)"
aliases: [Chuleta de Git, Git cheat sheet, Comandos Git]
parte_de: []
requiere: []
relacionado: []
---

# Comandos de Git

Los comandos de Git del día a día y de mantenimiento, agrupados por tarea: sincronizar, stash,
diff y log, tags, bisect, submódulos, firma, plumbing y mantenimiento.

## Fuente

La referencia completa de cada comando está en [git-scm.com/docs](https://git-scm.com/docs);
`git <comando> --help` abre la misma página. Esta ficha agrupa los usos comunes, verificados
contra esa documentación el 2026-10-03. Deshacer y recuperar está en
[[recuperar-trabajo-perdido-en-git]].

## Valores

**Branches y sincronización**

| Tarea | Comando |
|---|---|
| crear un branch y pasarse a él | `git switch -c feature/x` |
| volver al branch anterior | `git switch -` |
| traer cambios sin integrarlos | `git fetch origin`; con `-p` borra las refs remotas que ya no existen |
| traer e integrar | `git pull` (fetch + merge); `git pull --rebase` para rebasar |
| publicar un branch y seguirlo | `git push -u origin feature/x` |
| publicar un branch reescrito propio | `git push --force-with-lease` |
| borrar un branch ya integrado | `git branch -d feature/x` (`-D` si no está integrado) |

**Guardar trabajo a medias**: `git stash push -m "wip"`, `git stash list`, `git stash pop`
(aplica y borra) o `git stash apply` (aplica y conserva).

**Diferencias e historial**

| Tarea | Comando |
|---|---|
| cambios sin agregar / agregados | `git diff` / `git diff --staged` |
| estado corto con el branch | `git status -sb` |
| grafo del historial | `git log --oneline --graph --decorate --all` |
| commits que agregaron o quitaron un texto | `git log -S"nombreFuncion"` |
| historia de un archivo renombrado | `git log --follow -- ruta/archivo` |
| quién cambió cada línea | `git blame -L 10,40 ruta/archivo` |
| commits en B que no están en A | `git log A..B` (`A...B`: los de uno u otro, no de ambos) |
| ancestro común | `git merge-base A B` |
| traer un archivo de otro branch | `git restore --source=otra-rama -- ruta/archivo` |

**Tags**: `git tag -a v1.2.0 -m "Release 1.2.0"` (anotado), `git push origin v1.2.0` o
`git push --follow-tags` (envía los tags anotados de los commits que se envían),
`git describe --tags --abbrev=0` (último tag alcanzable).

**Buscar el commit que rompió algo**: `git bisect start`, `git bisect bad`,
`git bisect good v1.1.0`; con un script que sale 0 si el commit anda bien, 125 si no se puede
probar y otro valor entre 1 y 127 si anda mal, `git bisect run ./prueba.sh` lo resuelve solo;
`git bisect reset` al terminar.

**Submódulos**: `git submodule add <url> vendor/lib`; después de clonar,
`git submodule update --init --recursive`.

**Firma**: `git config --global commit.gpgsign true` y `user.signingkey`; con `gpg.format ssh`
se firma con una clave SSH. `git log --show-signature` verifica.

**Plumbing (inspección)**

| Comando | Qué hace |
|---|---|
| `git cat-file -t <sha>` / `-p <sha>` | tipo / contenido de un objeto |
| `git hash-object <archivo>` | hash que tendría el archivo como blob |
| `git ls-tree HEAD` | entradas del tree raíz de un commit |
| `git rev-parse HEAD` | hash al que resuelve una ref |
| `git rev-list --count A..B` | cantidad de commits entre dos refs |

**Mantenimiento**

| Comando | Qué hace |
|---|---|
| `git gc` | empaqueta objetos y borra los inalcanzables vencidos |
| `git maintenance start` | programa el mantenimiento en segundo plano |
| `git fsck` | verifica la integridad y conectividad de los objetos |
| `git count-objects -vH` | tamaño de los objetos sueltos y empaquetados |
| `git clean -n` y luego `-fd` | lista y después borra archivos no versionados |

Para reescribir la historia en masa (sacar un archivo de todos los commits), la documentación de
`git filter-branch` desaconseja ese comando y recomienda la herramienta aparte `git filter-repo`.

## Relaciones

- Detalla: [[modelo-de-objetos-de-git]], [[branch-git]], [[merge-de-tres-vias]] y [[rebase]] — los conceptos detrás de estos comandos.
