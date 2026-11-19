---
tipo: concepto
resumen: >-
  Una llamada al sistema (syscall) es el punto de entrada controlado por el que un programa en
  espacio de usuario le pide un servicio al kernel; casi siempre se usa a través de la biblioteca C.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, secciones 4.1 y 5"
  - "man 2 intro: https://man7.org/linux/man-pages/man2/intro.2.html"
  - "man 2 syscalls: https://man7.org/linux/man-pages/man2/syscalls.2.html"
  - "man 7 libc: https://man7.org/linux/man-pages/man7/libc.7.html"
aliases: [Syscall, System call, SCI, System Call Interface, Interfaz de llamadas al sistema]
parte_de: [arquitectura-de-linux]
requiere: [arquitectura-de-linux]
relacionado: []
---

# Llamada al sistema

Una llamada al sistema (syscall) es el punto de entrada controlado por el que un programa en
espacio de usuario le pide un servicio al kernel; casi siempre se usa a través de la biblioteca C.

## Por qué importa

Casi todo lo que un programa hace fuera de su propia memoria pasa por una llamada al sistema: abrir un
archivo, crear un proceso, mandar un paquete. Por eso observarlas muestra qué hace un programa
sin leer su código, y por eso son el lugar donde el kernel controla permisos.

## Cómo funciona

El programa pone el número de la llamada y sus argumentos en registros del procesador y ejecuta
una instrucción especial que pasa el control al kernel. El kernel verifica los argumentos y los
permisos, hace el trabajo y devuelve un resultado; si falla, devuelve un código de error que la
biblioteca C deja en `errno`.

Casi nadie hace esto a mano. La **biblioteca C** (glibc en la mayoría de las distribuciones, musl
en Alpine) ofrece funciones con el mismo nombre, como `open()` o `fork()`, que envuelven cada
llamada. Otras funciones de la biblioteca, como `printf()`, juntan datos y después hacen una
llamada (`write`).

Las llamadas se agrupan por área:

| Área | Ejemplos |
|---|---|
| Procesos | `fork`, `clone`, `execve`, `exit`, `waitpid` |
| Archivos | `open`, `read`, `write`, `close`, `stat` |
| Directorios y permisos | `mkdir`, `rename`, `unlink`, `chmod`, `chown` |
| Memoria | `brk`, `mmap`, `munmap`, `mprotect` |
| Comunicación entre procesos y red | `pipe`, `socket`, `connect`, `sendmsg` |
| Señales | `kill`, `sigaction` |
| Identidad y tiempo | `getuid`, `setuid`, `clock_gettime`, `nanosleep` |
| Administración | `mount`, `reboot`, `uname` |

La documentación de cada una está en la sección 2 del manual (`man 2 open`).

## Ejemplo

`strace ls` lista cada llamada que hace `ls`: `openat` sobre el directorio, `getdents64` para leer
sus entradas y `write` para imprimir los nombres. Si `ls` falla, la línea con `-1 EACCES` dice
qué llamada no tuvo permiso.

## No confundir con

Una función de biblioteca. `fopen()` y `malloc()` son de la biblioteca C y pueden resolver la
mayor parte del trabajo sin entrar al kernel; `ltrace` las muestra, mientras que `strace` muestra
solo las llamadas al sistema.

## Relaciones

- Parte de y requiere: [Arquitectura de Linux](arquitectura-de-linux.md) — es la frontera entre el espacio de usuario y el kernel.
- Detalle en: [Comandos de Linux](comandos-de-linux.md) — `strace`, `ltrace` y el resto de las herramientas de diagnóstico.
