---
resumen: >-
  Un daemon es un proceso de fondo sin terminal que presta un servicio del sistema (red,
  dispositivos, logs, tareas programadas, seguridad); en Linux moderno lo arranca y vigila el
  sistema de init.
estado: borrador
estabilidad: estable
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, secciones 3.2 a 3.7"
  - "man 7 daemon: https://man7.org/linux/man-pages/man7/daemon.7.html"
aliases: [Demonio, Servicio del sistema, Proceso de fondo]
creado: 2026-10-03
revisado:
---

# Daemon

Un daemon es un proceso de fondo sin terminal que presta un servicio del sistema (red,
dispositivos, logs, tareas programadas, seguridad); en Linux moderno lo arranca y vigila el
sistema de init.

## Qué hace un daemon en un servidor

Los daemons forman la capa de servicios del espacio de usuario en la
[Arquitectura de Linux](arquitectura-de-linux.md). Casi todo lo que un servidor hace sin que nadie escriba un comando lo hace un daemon: aceptar
conexiones SSH, crear los dispositivos de `/dev`, guardar logs, correr tareas programadas. Saber
qué daemon cubre cada área dice a quién mirar cuando esa área falla.

## Daemon clásico y daemon moderno

El manual de Linux (`man 7 daemon`) distingue dos estilos. El **daemon clásico** (SysV) se
separaba solo de la terminal: hacía dos `fork`, cerraba sus descriptores y escribía un archivo
con su PID. El **daemon moderno** no hace nada de eso: corre en primer plano, escribe sus logs en
la salida estándar y deja que [systemd](systemd.md) lo ponga en el fondo, lo reinicie si se cae y guarde lo
que imprime.

### Los daemons más comunes, por área

Por convención, el nombre termina en `d`.

| Área | Daemons |
|---|---|
| Dispositivos | `systemd-udevd` (crea los nodos de `/dev`), `udisksd`, `upowerd` |
| Comunicación y permisos | `dbus-daemon` (bus de mensajes entre procesos), `polkitd` |
| Red | `sshd`, `NetworkManager` o `systemd-networkd`, `systemd-resolved` (DNS), `avahi-daemon` |
| Almacenamiento | `dmeventd` (LVM), `mdmon` (RAID por software), `rpc.mountd` (servidor NFS), `smbd` (Samba) |
| Logs | `systemd-journald`, `rsyslogd` |
| Tareas programadas | `crond`, `atd` (o los timers de systemd) |
| Seguridad | `auditd`, `fail2ban` |
| Sesión | `systemd-logind`, el gestor de pantalla (`gdm`, `sddm`) |

## Mirar el daemon de SSH

`systemctl status sshd` (o `ssh` en Debian) muestra si el daemon de SSH corre, desde cuándo, su
PID y sus últimas líneas de log. Si el puerto 22 no responde, ese es el primer lugar que se mira. Los comandos para ver y controlar
servicios están en [Comandos de Linux](comandos-de-linux.md).

## Daemon y proceso en segundo plano

Un daemon no es un proceso en segundo plano de la terminal (`comando &`). Ese proceso sigue atado a la sesión de
quien lo lanzó y muere al cerrarla; un daemon pertenece al sistema y lo vigila el init.
