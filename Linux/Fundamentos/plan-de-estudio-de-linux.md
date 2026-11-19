---
resumen: >-
  Plan de seis meses, 10–12 h por semana, para pasar de usuario a administrador de Linux:
  objetivo, práctica, herramientas y mini-proyecto de cada mes, con la bibliografía.
estado: borrador
estabilidad: estable
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-track-6-meses.md"
  - "man 7 cgroups: https://man7.org/linux/man-pages/man7/cgroups.7.html"
  - "man 7 namespaces: https://man7.org/linux/man-pages/man7/namespaces.7.html"
aliases: [Linux track de 6 meses, Roadmap de Linux, Plan de Linux]
creado: 2026-10-03
revisado:
---

# Plan de estudio de Linux

Plan de seis meses, 10–12 h por semana, para pasar de usuario a administrador de Linux:
objetivo, práctica, herramientas y mini-proyecto de cada mes, con la bibliografía.

## De dónde sale el plan

Plan generado con una IA y revisado al migrarlo. Las notas del Tema explican los conceptos; el
orden de lectura está en [Linux por dentro](recorrido-linux-por-dentro.md).

## Los seis meses

**Entorno**: Ubuntu Server en una máquina virtual. WSL2 alcanza para el mes 1, pero no maneja
discos, USB ni el arranque de los meses 2 y 3.
**Nivel al terminar**: administración de sistemas, como base para DevOps.

### Mes 1. Arquitectura y espacio de usuario

- **Objetivo**: entender cómo está armado Linux y cómo se combinan sus herramientas.
- **Leer**: [Arquitectura de Linux](../arquitectura-de-linux.md), [Llamada al sistema](../llamada-al-sistema.md), [FHS](../fhs.md), [Pipe y redirección](../pipe-y-redireccion.md).
- **También**: shells y sus archivos (`.bashrc`, `.profile`), variables de entorno y `PATH`,
  secciones del manual (`man 7`, `apropos`, `whatis`, `tldr`).
- **Práctica**: recorrer `/proc/<PID>/` y `/sys`; un script que gestione logs, usuarios y un
  backup; un `chroot` mínimo con `debootstrap`.
- **Herramientas**: `find`, `xargs`, `grep`, `awk`, `sed`, `tee`, `cut`, `sort`, `uniq`, `diff`,
  `tar`, `gzip`, `rsync`, `scp`.
- **Mini-proyecto**: un script que junte CPU, RAM, disco y uptime y archive los resultados con
  rotación.

### Mes 2. Arranque, systemd y servicios

- **Objetivo**: entender cómo arranca Linux y cómo administra procesos y servicios.
- **Leer**: [Arranque de Linux](../arranque-de-linux.md), [Daemon](../daemon.md), [systemd](../systemd.md).
- **También**: señales, usuarios y grupos (`useradd`, `sudoers`, PAM, polkit), `cron`.
- **Práctica**: un servicio propio con dependencias; backups con timers; analizar el arranque
  con `systemd-analyze`.
- **Herramientas**: `systemctl`, `journalctl`, `loginctl`, `crontab`, `at`, `ps`, `top`, `htop`,
  `pstree`, `kill`, `renice`.
- **Mini-proyecto**: un servicio de systemd que corra un script de monitoreo, con su timer y sus
  logs en el journal.

### Mes 3. Sistemas de archivos, almacenamiento y kernel

- **Objetivo**: manejar el almacenamiento y las interfaces del kernel.
- **Leer**: [Pseudo-sistema de archivos](../pseudo-sistema-de-archivos.md), [FHS](../fhs.md).
- **También**: inodos, ACLs y capabilities; ext4, XFS, btrfs y ZFS; LVM, RAID y snapshots;
  tmpfs, loop devices, bind mounts y OverlayFS; `udev`.
- **Práctica**: crear y montar volúmenes LVM y configurar `fstab`; cambiar parámetros del kernel
  con `sysctl`; una regla udev que le dé un nombre fijo a un disco USB y una unidad `.mount` de
  systemd que lo monte (udev no debe montar por su cuenta).
- **Herramientas**: `lsblk`, `blkid`, `df`, `du`, `mount`, `fdisk`, `parted`, `mkfs`, `iostat`,
  `smartctl`.
- **Mini-proyecto**: backup incremental con `rsync` sobre snapshots de LVM.

### Mes 4. Red, namespaces y cgroups

- **Objetivo**: dominar la red moderna y el aislamiento del kernel.
- **Leer**: `man 7 namespaces` y `man 7 cgroups`; repasar [systemd](../systemd.md), que ordena los servicios en cgroups.
- **También**: `iproute2` y netlink; interfaces, rutas, bridges, VLANs y bonding; namespaces
  (`pid`, `net`, `mnt`, `uts`, `ipc`, `user`, `cgroup`); cgroups v2; cómo los usan Docker,
  Podman y Kubernetes.
- **Práctica**: dos namespaces de red con `ip netns` unidos por un par `veth`; un proceso aislado
  con `unshare`; límites de memoria y CPU con `systemd-run -p MemoryMax=…`, vistos con
  `systemd-cgls`.
- **Herramientas**: `ip`, `ss`, `bridge`, `nft`, `ufw` o `firewalld`, `lsns`, `unshare`, `nsenter`,
  `systemd-run`, `systemd-cgls`.
- **Mini-proyecto**: un "microcontenedor" a mano con `unshare`, `mount` y cgroups, sin Docker.

### Mes 5. Seguridad, auditoría y performance

- **Objetivo**: entender los mecanismos de seguridad y cómo auditar el sistema.
- **También**: permisos POSIX, ACLs y capabilities; SELinux, AppArmor y seccomp; PAM y sudoers;
  `auditd`; rotación de logs; tracing con `perf`, `ftrace` y `bpftrace`.
- **Práctica**: un perfil de AppArmor para un proceso; reglas con `auditctl` y búsqueda con
  `ausearch`; medir un proceso con `perf stat`.
- **Herramientas**: `auditctl`, `ausearch`, `perf`, `pidstat`, `iotop`, `sar`, `vmstat`,
  `bpftrace`, `journalctl`.
- **Mini-proyecto**: un perfil de AppArmor más un script de auditoría que registre eventos
  críticos y avise.

### Mes 6. Linux en producción

- **Objetivo**: juntar todo en un entorno parecido a producción.
- **También**: contenedores como namespaces + cgroups + OverlayFS; Docker, Podman y LXC;
  KVM, QEMU y libvirt; Ansible y SSH; monitoreo centralizado (Prometheus, exportar el journal);
  familias de distro (Debian, Red Hat, Arch, Alpine).
- **Práctica**: un contenedor a mano comparado con uno de Docker; un entorno reproducible con
  Ansible; ver cómo systemd integra cgroups, logs y red.
- **Herramientas**: `docker`, `podman`, `lxc`, `virt-manager`, `ansible`, `ssh`, `rsync`,
  `journalctl -o json`.
- **Proyecto final**: un entorno "mini-producción" con un servicio de systemd, logs
  centralizados, un contenedor aislado a mano con namespaces y cgroups, y monitoreo con alertas.

### Bibliografía

- Brian Ward, *How Linux Works*, 3.ª ed. (No Starch Press, 2021): https://nostarch.com/howlinuxworks3
- Robert Love, *Linux System Programming*, 2.ª ed. (O'Reilly, 2013).
- Daniel P. Bovet y Marco Cesati, *Understanding the Linux Kernel*, 3.ª ed. (O'Reilly, 2005);
  describe el kernel 2.6, así que sirve para los conceptos y no para los detalles actuales.
- David Calavera y Lorenzo Fontana, *Linux Observability with BPF* (O'Reilly, 2019).
- Brendan Gregg, performance y tracing en Linux: https://www.brendangregg.com/linuxperf.html
- Las páginas conceptuales del manual: `man 7 cgroups`, `man 7 namespaces`, `man 7 capabilities`.
- explainshell, para desarmar una línea de comandos: https://explainshell.com
