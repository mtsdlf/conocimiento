---
tipo: concepto
resumen: >-
  Un pseudo-sistema de archivos (procfs, sysfs, devtmpfs, tmpfs) no guarda datos en disco: expone
  el estado del kernel y de los procesos como archivos que se leen y, a veces, se escriben para
  ajustar el kernel.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, secciones 8 y 12"
  - "man 5 proc: https://man7.org/linux/man-pages/man5/proc.5.html"
  - "man 5 sysfs: https://man7.org/linux/man-pages/man5/sysfs.5.html"
  - "man 5 tmpfs: https://man7.org/linux/man-pages/man5/tmpfs.5.html"
  - "Kernel docs, Documentation for /proc/sys: https://docs.kernel.org/admin-guide/sysctl/index.html"
aliases: [Sistema de archivos virtual, procfs, sysfs, devtmpfs, tmpfs, /proc, /sys]
parte_de: []
requiere: [arquitectura-de-linux]
relacionado: [systemd, fhs]
---

# Pseudo-sistema de archivos

Un pseudo-sistema de archivos (procfs, sysfs, devtmpfs, tmpfs) no guarda datos en disco: expone
el estado del kernel y de los procesos como archivos que se leen y, a veces, se escriben para
ajustar el kernel.

## Por qué importa

Gracias a ellos, las herramientas de siempre (`cat`, `grep`, `echo`) alcanzan para inspeccionar y
ajustar el kernel, sin programas especiales. `ps`, `free` y `top` no hacen magia: leen archivos de
`/proc`.

## Cómo funciona

| Pseudo-sistema | Montado en | Qué expone |
|---|---|---|
| procfs | `/proc` | un directorio por proceso (`/proc/<PID>/status`, `/proc/<PID>/fd/`), datos globales (`/proc/meminfo`, `/proc/cpuinfo`) y los parámetros del kernel en `/proc/sys` |
| sysfs | `/sys` | los objetos del kernel: dispositivos, drivers, buses y módulos, uno por directorio; dentro se monta otro pseudo-sistema, cgroup2, en `/sys/fs/cgroup` |
| devtmpfs | `/dev` | los nodos de dispositivo que crea el kernel; `udev` les ajusta nombres y permisos según `/etc/udev/rules.d/` |
| tmpfs | `/run`, a menudo `/tmp` | archivos comunes guardados en memoria, que se pierden al reiniciar |

Los **parámetros del kernel** de `/proc/sys` se leen y escriben como archivos, o con `sysctl`,
que traduce los puntos del nombre a barras. Un cambio así dura hasta el próximo reinicio; para que
persista se escribe en un archivo de `/etc/sysctl.d/`, que `sysctl --system` aplica sin reiniciar.
Escribir estos archivos requiere root.

## Ejemplo

Para que una máquina reenvíe paquetes entre interfaces (hacer de router):

```bash
cat /proc/sys/net/ipv4/ip_forward      # 0: apagado
sudo sysctl -w net.ipv4.ip_forward=1   # escribe 1 en ese mismo archivo
echo 'net.ipv4.ip_forward = 1' | sudo tee /etc/sysctl.d/90-router.conf   # persistente
```

## No confundir con

El VFS (Virtual File System). El VFS es la capa del kernel que da la misma interfaz (`open`,
`read`) a todos los sistemas de archivos, reales o no; un pseudo-sistema de archivos es uno de
los sistemas que se enchufan a esa capa.

## Relaciones

- Requiere: [Arquitectura de Linux](arquitectura-de-linux.md) — expone el kernel al espacio de usuario.
- Relacionado: [systemd](systemd.md) — usa los cgroups de `/sys/fs/cgroup` para seguir y limitar cada servicio.
- Relacionado: [FHS](fhs.md) — `/proc`, `/sys`, `/dev` y `/run` son directorios del estándar sin datos en disco.
