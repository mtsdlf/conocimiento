---
tipo: ficha
resumen: >-
  Los comandos de administración de Linux agrupados por función: archivos, texto, procesos,
  monitoreo, red, usuarios, servicios, paquetes por familia de distro, módulos y performance.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, secciones 2.2 a 2.4, 5.2, 9, 11 y 12"
  - "Páginas de manual de Linux: https://man7.org/linux/man-pages/"
  - "Brendan Gregg, Linux Performance: https://www.brendangregg.com/linuxperf.html"
  - "explainshell (explica cada parte de una línea de comandos): https://explainshell.com"
aliases: [Comandos de administración de Linux, Chuleta de Linux, Cheat sheet de Linux]
parte_de: []
requiere: []
relacionado: []
---

# Comandos de Linux

Los comandos de administración de Linux agrupados por función: archivos, texto, procesos,
monitoreo, red, usuarios, servicios, paquetes por familia de distro, módulos y performance.

## Fuente

Cada comando trae su manual: `man <comando>`, `tldr <comando>` para ejemplos cortos, y
[explainshell](https://explainshell.com) para desarmar una línea entera. La mayoría viene de GNU
coreutils, util-linux, procps e iproute2.

## Valores

### Archivos, texto y permisos

| Función | Comandos |
|---|---|
| Archivos y directorios | `ls`, `cp`, `mv`, `rm`, `mkdir`, `ln`, `tree`, `file`, `stat`, `find` |
| Espacio en disco | `du`, `df` |
| Texto | `cat`, `less`, `grep`, `sed`, `awk`, `head`, `tail`, `sort`, `uniq`, `cut`, `tr`, `wc`, `diff`, `tee`, `xargs` |
| Permisos y dueños | `chmod`, `chown`, `chgrp`, `umask` |
| Archivos comprimidos | `tar`, `gzip`, `bzip2`, `xz`, `zip`, `unzip` |
| Copia remota | `ssh`, `scp`, `sftp`, `rsync`, `curl`, `wget` |

### Procesos, servicios y logs

| Función | Comandos |
|---|---|
| Procesos | `ps`, `pgrep`, `pkill`, `pstree`, `kill`, `nice`, `renice`, `jobs` |
| Servicios ([[systemd]]) | `systemctl start\|stop\|status\|enable <unidad>`, `systemd-analyze blame` |
| Logs | `journalctl -u <unidad>`, `journalctl -b`, `dmesg`, `logger` |
| Tareas programadas | `crontab -e`, `at`, `systemctl list-timers` |
| Sesiones | `loginctl`, `who`, `w` |

`service` y los scripts de `/etc/init.d` son la forma anterior a systemd.

### Monitoreo y performance

| Función | Comandos |
|---|---|
| Vista general | `top`, `htop`, `uptime`, `free`, `vmstat` |
| CPU y disco cada N segundos | `mpstat`, `iostat`, `pidstat`, `sar` |
| Disco por proceso | `iotop` |
| Archivos abiertos | `lsof` |
| Llamadas al sistema y de biblioteca | `strace`, `ltrace` |
| Perfilado | `perf`, `bpftrace` |
| Memoria del kernel | `slabtop` |

### Red

| Función | Comandos |
|---|---|
| Interfaces y rutas | `ip addr`, `ip link`, `ip route`, `ip neigh` |
| Sockets y puertos | `ss -tulpn` |
| Conectividad | `ping`, `traceroute`, `tracepath`, `nc`, `curl` |
| DNS | `dig`, `host`, `nslookup` |
| Captura de paquetes | `tcpdump` |
| Firewall | `nft`, `ufw` (Ubuntu), `firewall-cmd` (RHEL, Fedora) |
| Wi-Fi y NetworkManager | `nmcli`, `iw`, `rfkill` |

`ifconfig`, `route` y `netstat` (paquete net-tools) están en desuso: `ip` y `ss` los reemplazan.

### Usuarios y privilegios

| Función | Comandos |
|---|---|
| Usuarios | `useradd`, `usermod`, `userdel`, `passwd`, `chage` |
| Grupos | `groupadd`, `gpasswd` |
| Consultar | `id`, `whoami`, `getent passwd` |
| Privilegios | `sudo`, `su`, `visudo` |

### Discos e identificación del sistema

| Función | Comandos |
|---|---|
| Discos y particiones | `lsblk`, `blkid`, `fdisk`, `parted`, `mkfs`, `mount`, `umount` |
| Sistema | `uname -a`, `hostnamectl` |

### Paquetes por familia de distro

| Familia | Gestor | Base de datos |
|---|---|---|
| Debian, Ubuntu | `apt`, `dpkg` | `/var/lib/dpkg/`, repos en `/etc/apt/` |
| RHEL, Fedora | `dnf`, `rpm` | `/var/lib/rpm` (Fedora 36 en adelante: `/usr/lib/sysimage/rpm`), repos en `/etc/yum.repos.d/` |
| SUSE | `zypper`, `rpm` | `/var/lib/zypp/` |
| Arch | `pacman` | `/var/lib/pacman/` |
| Alpine | `apk` | `/lib/apk/db/` |

Los comandos que cambian el sistema (instalar, crear usuarios, `systemctl start`) se corren
con `sudo`.

```bash
apt update && apt upgrade        # Debian, Ubuntu
dnf install <paquete>            # RHEL, Fedora
pacman -Syu                      # Arch: actualizar todo
```

### Kernel: módulos y parámetros

| Función | Comandos |
|---|---|
| Módulos | `lsmod`, `modprobe <módulo>`, `modprobe -r <módulo>`, `modinfo`; viven en `/lib/modules/$(uname -r)/` |
| Parámetros | `sysctl -a`, `sysctl -w <clave>=<valor>`, `sysctl --system` (recarga `/etc/sysctl.d/`) |

## Relaciones

- Detalla: [[daemon]] y [[systemd]] — los comandos para ver y controlar servicios.
- Detalla: [[llamada-al-sistema]] — `strace` y `ltrace`.
- Detalla: [[pipe-y-redireccion]] — los comandos de texto que se combinan con pipes.
