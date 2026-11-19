---
tipo: ficha
resumen: >-
  La tabla de directorios del Filesystem Hierarchy Standard: qué va en /etc, /usr, /var y el
  resto, con las rutas de logs y de usuarios más consultadas.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, secciones 6, 10 y 11"
  - "Filesystem Hierarchy Standard 3.0 (Linux Foundation, 2015): https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html"
  - "man 7 hier: https://man7.org/linux/man-pages/man7/hier.7.html"
aliases: [Filesystem Hierarchy Standard, FHS, Árbol de directorios de Linux, Jerarquía de directorios]
parte_de: []
requiere: [arquitectura-de-linux]
relacionado: [pseudo-sistema-de-archivos]
---

# FHS

La tabla de directorios del Filesystem Hierarchy Standard: qué va en /etc, /usr, /var y el
resto, con las rutas de logs y de usuarios más consultadas.

## Fuente

El estándar completo es el [FHS 3.0](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html),
mantenido por la Linux Foundation. En cada máquina, `man 7 hier` describe la jerarquía que usa esa
distribución.

## Valores

### Directorios de la raíz

| Directorio | Qué contiene |
|---|---|
| `/` | la raíz del árbol; todo cuelga de acá |
| `/bin`, `/sbin` | comandos esenciales para arrancar y reparar (`ls`, `bash`, `fsck`, `ip`) |
| `/lib`, `/lib64` | bibliotecas compartidas de esos comandos y módulos del kernel |
| `/boot` | kernel (`vmlinuz`), initramfs y configuración del gestor de arranque |
| `/dev` | nodos de dispositivo (`/dev/sda`, `/dev/null`) |
| `/etc` | configuración de la máquina, sin binarios (`/etc/fstab`, `/etc/ssh/sshd_config`) |
| `/home` | datos personales de cada usuario |
| `/root` | directorio personal del usuario `root` |
| `/media`, `/mnt` | montajes de medios removibles y montajes temporales a mano |
| `/opt` | paquetes de terceros instalados como un bloque |
| `/proc`, `/sys` | estado del kernel y de los procesos, sin datos en disco |
| `/run` | datos de ejecución (PID, sockets), en memoria y borrados al reiniciar |
| `/srv` | datos que sirve la máquina (web, FTP) |
| `/tmp` | temporales; muchas distribuciones lo montan en memoria |
| `/usr` | programas y datos compartibles, de solo lectura: `/usr/bin`, `/usr/lib`, `/usr/share` |
| `/usr/local` | software compilado o instalado a mano, con la misma estructura que `/usr` |
| `/var` | datos que cambian: logs, caches, colas, bases de datos |
| `/var/lib` | estado persistente de cada programa |
| `/var/cache` | caches que se pueden borrar y regenerar |
| `/var/spool` | colas de trabajo pendientes (impresión, correo) |
| `/var/tmp` | temporales que sobreviven a un reinicio |

En Fedora, Debian 12, Ubuntu y Arch, `/bin`, `/sbin` y `/lib` son enlaces a sus pares de `/usr`
(el "/usr unificado", una decisión de las distribuciones que el FHS 3.0 no recoge); las rutas
viejas siguen funcionando.

### Logs

| Ruta | Qué guarda |
|---|---|
| `/var/log/journal/` | el journal de systemd, si es persistente |
| `/var/log/syslog` (Debian, Ubuntu) o `/var/log/messages` (RHEL, Fedora) | log general, si hay rsyslog |
| `/var/log/auth.log` (Debian, Ubuntu) o `/var/log/secure` (RHEL, Fedora) | autenticación |
| `/var/log/kern.log` (Debian, Ubuntu) | mensajes del kernel (los mismos que `dmesg`); en otras distros, `journalctl -k` |
| `/var/log/<programa>/` | logs propios de una aplicación, como `nginx` |
| `/etc/rsyslog.conf` | configuración de rsyslog |

### Usuarios y permisos

| Archivo | Qué guarda |
|---|---|
| `/etc/passwd` | usuarios: UID, grupo, directorio personal y shell |
| `/etc/shadow` | hashes de contraseñas; solo lo lee root |
| `/etc/group` | grupos y sus miembros |
| `/etc/sudoers` y `/etc/sudoers.d/` | quién puede usar `sudo`; se editan con `visudo` |
| `/etc/security/limits.conf` | límites de recursos por usuario |

## Relaciones

- Detalla y requiere: [Arquitectura de Linux](arquitectura-de-linux.md) — dónde vive cada capa en el árbol.
- Relacionado: [Pseudo-sistema de archivos](pseudo-sistema-de-archivos.md) — explica los directorios sin datos en disco.
