---
tipo: concepto
resumen: >-
  Un pipe conecta la salida estándar de un comando con la entrada del siguiente, y una redirección
  conecta un flujo (stdin, stdout, stderr) con un archivo; juntos permiten armar tareas combinando
  programas pequeños, como propone la filosofía Unix.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original reemplazado: nota linux-pipes-unix (secciones A, B, C.5 y D), borrada al migrar"
  - "Bash Reference Manual, Pipelines: https://www.gnu.org/software/bash/manual/html_node/Pipelines.html"
  - "Bash Reference Manual, Redirections: https://www.gnu.org/software/bash/manual/html_node/Redirections.html"
  - "Bash Reference Manual, Lists of Commands: https://www.gnu.org/software/bash/manual/html_node/Lists.html"
  - "Bash Reference Manual, Process Substitution: https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html"
  - "man 7 pipe: https://man7.org/linux/man-pages/man7/pipe.7.html"
aliases: [Pipe, Tubería, Redirección, stdin, stdout, stderr, Filosofía Unix]
parte_de: []
requiere: []
relacionado: []
---

# Pipe y redirección

Un pipe conecta la salida estándar de un comando con la entrada del siguiente, y una redirección
conecta un flujo (stdin, stdout, stderr) con un archivo; juntos permiten armar tareas combinando
programas pequeños, como propone la filosofía Unix.

## Por qué importa

La filosofía Unix pide programas que hagan una sola cosa bien y que se puedan combinar. Los pipes
son lo que hace posible esa combinación: `grep`, `sort` y `uniq` no saben nada de logs, pero
encadenados cuentan errores por IP sin escribir un programa nuevo.

## Cómo funciona

Todo proceso arranca con tres **flujos estándar**, numerados: 0 es la entrada (**stdin**), 1 la
salida (**stdout**) y 2 los errores (**stderr**). Por defecto, los tres apuntan a la terminal.

Un **pipe** (`a | b`) es un buffer del kernel: el shell arranca `a` y `b` a la vez y conecta el
stdout de `a` con el stdin de `b`. El stderr no pasa por el pipe, así que los errores siguen
saliendo en pantalla. El código de salida de un pipe es el del último comando; con
`set -o pipefail`, falla si falla cualquiera.

Una **redirección** cambia adónde apunta un flujo:

| Forma | Efecto |
|---|---|
| `> f`, `>> f` | stdout a un archivo, pisándolo o agregando al final |
| `< f` | stdin desde un archivo |
| `2> f` | stderr a un archivo |
| `> f 2>&1` (en bash, también `&> f`) | stdout y stderr al mismo archivo |

El orden importa: `> f 2>&1` manda los dos al archivo, pero `2>&1 > f` deja los errores en la
terminal, porque copia el destino de stdout antes de cambiarlo.

La **sustitución de procesos** de bash, `>(comando)` y `<(comando)`, presenta la entrada o la
salida de un comando como si fuera un archivo. Sirve para usar un pipe donde un programa espera
un nombre de archivo: `diff <(sort a.txt) <(sort b.txt)`.

Además, los comandos se encadenan por resultado: `a ; b` corre los dos siempre, `a && b` corre
`b` solo si `a` terminó bien y `a || b` solo si falló.

## Ejemplo

`grep ERROR app.log 2> errores.txt | wc -l` cuenta las líneas con ERROR; si `app.log` no existe,
el aviso de `grep` va a `errores.txt` y no se cuenta como una línea más.

## No confundir con

Un pipe con nombre (FIFO, creado con `mkfifo`). Funciona igual, pero tiene un nombre en el sistema de
archivos (sin guardar datos en disco) y conecta procesos que no lanzó el mismo shell.

## Relaciones

- Base de: [[recetas-de-pipes]] — las combinaciones listas para usar.
- Detalle en: [[comandos-de-linux]] — los comandos de texto que se combinan con pipes.
