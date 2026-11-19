---
resumen: >-
  systemd es el sistema de init más usado en Linux: corre como PID 1 y arranca y supervisa
  servicios descritos en unidades (service, socket, timer, target, mount), con journald para los
  logs.
estado: borrador
estabilidad: estable
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, secciones 3.1 y 10; Archivo/Linux/linux-track-6-meses.md, mes 2"
  - "man 1 systemd: https://man7.org/linux/man-pages/man1/systemd.1.html"
  - "man 5 systemd.unit: https://man7.org/linux/man-pages/man5/systemd.unit.5.html"
  - "man 8 systemd-journald.service: https://man7.org/linux/man-pages/man8/systemd-journald.service.8.html"
  - "Sitio del proyecto: https://systemd.io/"
aliases: [Init, PID 1, Unidad de systemd, journald]
creado: 2026-10-03
revisado:
---

# systemd

systemd es el sistema de init más usado en Linux: corre como PID 1 y arranca y supervisa
servicios descritos en unidades (service, socket, timer, target, mount), con journald para los
logs.

## Administrar Linux es escribir unidades

Debian, Ubuntu, Fedora, RHEL, SUSE y Arch lo usan por defecto, así que administrar un servidor
Linux es, en gran parte, escribir y leer unidades de systemd. Además, cubre con un solo sistema lo
que antes hacían tres herramientas separadas: los scripts de `/etc/init.d`, `cron` y `syslog`,
que igual pueden seguir instalados.

## Unidades, dependencias y cgroups

systemd toma el control en el paso 4 del [Arranque de Linux](arranque-de-linux.md). Cada cosa que systemd gestiona es una **unidad**, un archivo de texto con el tipo como extensión:

| Tipo | Qué describe |
|---|---|
| `.service` | un proceso o [Daemon](daemon.md) y cómo arrancarlo, pararlo y reiniciarlo |
| `.socket` | un socket que systemd abre y que arranca el servicio al primer pedido |
| `.timer` | un horario que activa otra unidad; reemplaza a `cron` |
| `.target` | un grupo de unidades que marca un estado del sistema, como `multi-user.target` (antes, los runlevels numerados) |
| `.mount` | un punto de montaje |

Las unidades declaran qué necesitan (`Requires=`) y en qué orden van (`After=`); son dos cosas
separadas. systemd arranca en paralelo todo lo que no depende entre sí. Cada servicio corre en su propio grupo de control (cgroup), visible en
`/sys/fs/cgroup` (un [Pseudo-sistema de archivos](pseudo-sistema-de-archivos.md)): así systemd sabe qué procesos le pertenecen y puede limitarles CPU o memoria.

## journald

**journald** recibe la salida y los mensajes de todos los servicios y los guarda en un journal
binario e indexado, que se consulta con `journalctl`. Si existe `/var/log/journal`, el journal
persiste entre reinicios; si no, vive en `/run/log/journal` y se pierde. Un servicio clásico como
rsyslog puede leer del journal y escribir los archivos de texto de `/var/log`.

## Un script de monitoreo cada 15 minutos

Un script de monitoreo que debe correr cada 15 minutos lleva dos unidades: `monitor.service`, que
lo ejecuta, y `monitor.timer`, con `OnCalendar=*:0/15`. `systemctl enable --now monitor.timer` lo
activa, y `journalctl -u monitor.service` muestra la salida de cada corrida. `systemctl`, `journalctl` y `systemd-analyze` están en
[Comandos de Linux](comandos-de-linux.md).

## systemd y el init en general

systemd no es el init en general. PID 1 es un rol; systemd es una implementación. OpenRC (Alpine, Gentoo),
runit y SysVinit cumplen el mismo rol con otro diseño.
