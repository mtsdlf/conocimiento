---
resumen: >-
  Un merge de tres vías combina dos branches que divergieron a partir de su ancestro común:
  aplica los cambios de cada lado y marca conflicto donde los dos tocan las mismas líneas.
estado: borrador
estabilidad: estable
revisado:
creado: 2026-10-03
fuentes:
  - "Git Documentation, git-merge: https://git-scm.com/docs/git-merge"
  - "Git Documentation, merge-strategies: https://git-scm.com/docs/merge-strategies"
  - "Git 2.34.0 Release Notes (ort por defecto): https://raw.githubusercontent.com/git/git/master/Documentation/RelNotes/2.34.0.adoc"
  - "Git 2.50.0 Release Notes (recursive pasa a ser ort): https://raw.githubusercontent.com/git/git/master/Documentation/RelNotes/2.50.0.adoc"
  - "Archivo/Desarrollo/git/git-mecanismos-internos.md y Archivo/DevOps/git/git-advanced-collaboration.md, git-mastery-workflows.md y git-organizational-topology.md (originales, texto generado con IA)"
aliases: [Three-way merge, Merge (Git), git merge, Fast-forward, Estrategia de merge, ort]
---

# Merge de tres vías

Un merge de tres vías combina dos branches que divergieron a partir de su ancestro común:
aplica los cambios de cada lado y marca conflicto donde los dos tocan las mismas líneas.

## Por qué hace falta el ancestro común

Comparar solo las dos puntas de los [branches](branch-git.md) no alcanza: si una línea difiere, no se sabe quién la cambió. Con el
ancestro común como referencia, Git sabe qué lado cambió cada línea y resuelve solo la mayoría de
los casos.

## Base, ours, theirs y las estrategias

`git merge feature` estando en `main` toma tres commits:

```text
A---B---C---D   main  (ours = D)
     \
      E---F---G feature (theirs = G)
base = B  (git merge-base main feature)
```

Git calcula los cambios de B a D y de B a G. Lo que cambió de un solo lado se toma; lo que cambió
igual de los dos lados, también. Donde los dos lados cambiaron la misma zona de forma distinta,
hay conflicto: ver [Resolver conflictos de merge](resolver-conflictos-de-merge.md). El resultado es un **merge commit** con dos
padres, D y G.

Si `main` no hubiera avanzado desde que salió `feature` (sin C ni D, la punta de `main` sería B,
ancestro de G), no habría nada que combinar: Git hace **fast-forward** y solo mueve el puntero de `main` a G, sin crear un commit. `--no-ff` fuerza
el merge commit igual, para que quede registrado; `--ff-only` falla si no se puede avanzar.

La **estrategia** es el algoritmo que hace el merge:

| Estrategia | Qué hace |
|---|---|
| `ort` | la de defecto desde Git 2.34; detecta renombres y, si hay varios ancestros comunes (merges cruzados), primero los combina entre sí y usa ese resultado como base |
| `recursive` | la anterior; desde Git 2.50 es otro nombre de `ort` |
| `resolve` | tres vías entre dos heads, sin detección de renombres; trata con cuidado los merges cruzados |
| `octopus` | combina más de dos branches; se niega si hay conflictos |
| `ours` | se queda con el tree propio entero e ignora el otro lado |
| `subtree` | para combinar un proyecto que vive en un subdirectorio |

No confundir `-s ours` (descarta el otro lado entero) con `-X ours` (opción de `ort`: en los
bloques en conflicto, gana el lado propio; lo demás se combina). Existe `-X theirs`, pero no hay
estrategia `-s theirs`.

## Ana y Beto en config.py

Ana cambia la línea 10 de `config.py` en `main`; Beto, la 40 en `feature`. El merge toma las dos;
si ambos hubieran cambiado la 10, habría conflicto.

## Merge y rebase

Un [Rebase](rebase.md). El merge conserva los dos historiales y los une con un commit nuevo; el rebase
reescribe los commits de un lado para que el historial quede lineal.

## Ver también

- [Estrategia de branching](../../DevOps/Ramas-y-versiones/estrategia-de-branching.md) (DevOps) — merge commit o squash como política de equipo.
