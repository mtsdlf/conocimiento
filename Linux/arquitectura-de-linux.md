---
tipo: concepto
resumen: >-
  Linux se organiza en capas: hardware, kernel (espacio del kernel) y espacio de usuario con
  bibliotecas, servicios, shells y aplicaciones; las llamadas al sistema son la única puerta entre
  los dos espacios.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, secciones 1 y 2.1"
  - "Brian Ward, How Linux Works, 3.ª ed. (No Starch Press, 2021), cap. 1: https://nostarch.com/howlinuxworks3"
  - "man 2 intro: https://man7.org/linux/man-pages/man2/intro.2.html"
aliases: [Arquitectura de Linux, Espacio de usuario, Espacio del kernel, User space, Kernel space]
parte_de: []
requiere: []
relacionado: []
---

# Arquitectura de Linux

Linux se organiza en capas: hardware, kernel (espacio del kernel) y espacio de usuario con
bibliotecas, servicios, shells y aplicaciones; las llamadas al sistema son la única puerta entre
los dos espacios.

## Por qué importa

Saber en qué capa vive cada cosa ordena el diagnóstico. Un "command not found" lo da el shell,
en el espacio de usuario, porque el programa no está en el `PATH`; un disco que no aparece en
`lsblk` es un problema del kernel (falta el driver) o del hardware. También explica por qué un proceso no puede tocar la memoria de otro: solo el kernel
accede directo al hardware.

## Cómo funciona

Las capas, de abajo hacia arriba:

| Capa | Qué contiene |
|---|---|
| Hardware | CPU, memoria, discos, placas de red |
| Kernel | gestión de procesos, memoria, sistemas de archivos, red y drivers |
| Interfaz de llamadas al sistema | los puntos de entrada controlados al kernel |
| Bibliotecas | la biblioteca C (glibc, musl) y otras compartidas |
| Servicios del sistema | el sistema de init y los daemons |
| Shells y aplicaciones | `bash`, `zsh`, utilidades de línea de comandos y programas gráficos |

El **espacio del kernel** corre con privilegios completos del procesador. El **espacio de
usuario** es todo lo demás: corre con privilegios reducidos y pide cada servicio al kernel
mediante una [Llamada al sistema](llamada-al-sistema.md).

El **shell** es un programa más del espacio de usuario: interpreta lo que se escribe y lanza
otros procesos. Por eso se puede cambiar `bash` por `zsh` o `fish` sin tocar el sistema; cada
uno lee sus propios archivos de configuración (`~/.bashrc`, `~/.zshrc`).

## Ejemplo

Al correr `cat /etc/hostname`, el shell crea un proceso para `cat`. `cat` usa funciones de la
biblioteca C, que hacen las llamadas `open` y `read`. El kernel lee el archivo del disco y le
devuelve los bytes, y `cat` los escribe en la terminal con otra llamada, `write`.

## No confundir con

Una distribución. Debian, Fedora o Arch comparten el kernel Linux y se diferencian en el espacio
de usuario: gestor de paquetes, versiones de bibliotecas y configuración por defecto.

## Relaciones

- Base de: [Llamada al sistema](llamada-al-sistema.md) — la puerta entre las dos capas principales.
- Base de: [Daemon](daemon.md) — los servicios que viven en el espacio de usuario.
- Base de: [Arranque de Linux](arranque-de-linux.md) — el orden en que se levantan las capas.
- Base de: [Pseudo-sistema de archivos](pseudo-sistema-de-archivos.md) — cómo el kernel se muestra al espacio de usuario.
- Detalle en: [FHS](fhs.md) — dónde vive cada capa en el árbol de directorios.
