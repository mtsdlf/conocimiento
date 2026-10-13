---
tipo: concepto
resumen: >-
  Un daemon es un proceso de fondo sin terminal que presta un servicio del sistema (red,
  dispositivos, logs, tareas programadas, seguridad); en Linux moderno lo arranca y vigila el
  sistema de init.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, secciones 3.2 a 3.7"
  - "man 7 daemon: https://man7.org/linux/man-pages/man7/daemon.7.html"
aliases: [Demonio, Servicio del sistema, Proceso de fondo]
parte_de: [arquitectura-de-linux]
requiere: [arquitectura-de-linux]
relacionado: []
---

# Daemon

Un daemon es un proceso de fondo sin terminal que presta un servicio del sistema (red,
dispositivos, logs, tareas programadas, seguridad); en Linux moderno lo arranca y vigila el
sistema de init.

## Por qué importa

Casi todo lo que un servidor hace sin que nadie escriba un comando lo hace un daemon: aceptar
conexiones SSH, crear los dispositivos de `/dev`, guardar logs, correr tareas programadas. Saber
qué daemon cubre cada área dice a quién mirar cuando esa área falla.

## Cómo funciona

El manual de Linux (`man 7 daemon`) distingue dos estilos. El **daemon clásico** (SysV) se
separaba solo de la terminal: hacía dos `fork`, cerraba sus descriptores y escribía un archivo
con su PID. El **daemon moderno** no hace nada de eso: corre en primer plano, escribe sus logs en
la salida estándar y deja que [[systemd]] lo ponga en el fondo, lo reinicie si se cae y guarde lo
que imprime.

Por convención, el nombre termina en `d`. Los más comunes, por área:

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

## Ejemplo

`systemctl status sshd` (o `ssh` en Debian) muestra si el daemon de SSH corre, desde cuándo, su
PID y sus últimas líneas de log. Si el puerto 22 no responde, ese es el primer lugar que se mira.

## No confundir con

Un proceso en segundo plano de la terminal (`comando &`). Ese proceso sigue atado a la sesión de
quien lo lanzó y muere al cerrarla; un daemon pertenece al sistema y lo vigila el init.

## Relaciones

- Parte de y requiere: [[arquitectura-de-linux]] — es la capa de servicios del espacio de usuario.
- Base de: [[systemd]] — hay que saber qué es un daemon antes de ver cómo systemd los arranca y supervisa.
- Detalle en: [[comandos-de-linux]] — los comandos para ver y controlar servicios.
