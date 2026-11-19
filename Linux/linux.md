---
tipo: mapa
resumen: >-
  Cómo está hecho y cómo se administra un sistema Linux: arquitectura, arranque, servicios,
  sistema de archivos y la terminal; para quien estudia administración de sistemas.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# Linux

Cómo está hecho y cómo se administra un sistema Linux: arquitectura, arranque, servicios,
sistema de archivos y la terminal; para quien estudia administración de sistemas.

Para aprenderlo en orden: [Linux por dentro](recorrido-linux-por-dentro.md).

## Cómo está hecho

- [Arquitectura de Linux](arquitectura-de-linux.md) — las capas del sistema y la frontera entre kernel y espacio de usuario; la puerta de entrada al Tema.
- [Llamada al sistema](llamada-al-sistema.md) — cómo un programa le pide algo al kernel; leerla después de la arquitectura.
- [Daemon](daemon.md) — qué son los procesos de fondo y qué servicios del sistema prestan.
- [Pseudo-sistema de archivos](pseudo-sistema-de-archivos.md) — cómo `/proc`, `/sys` y `/dev` exponen el kernel como archivos y cómo se ajusta el kernel en vivo.

## Arranque y servicios

- [Arranque de Linux](arranque-de-linux.md) — qué pasa desde que se prende la máquina hasta el login.
- [systemd](systemd.md) — cómo el sistema de init arranca, supervisa y registra los servicios.

## La terminal

- [Pipe y redirección](pipe-y-redireccion.md) — cómo se combinan comandos chicos conectando sus flujos de entrada y salida.

## Para consultar

- [FHS](fhs.md) — qué va en cada directorio del sistema y dónde están los logs y los archivos de usuarios.
- [Comandos de Linux](comandos-de-linux.md) — los comandos de administración agrupados por función y por familia de distro.
- [Recetas de pipes](recetas-de-pipes.md) — combinaciones de pipes listas para copiar.
- [Plan de estudio de Linux](plan-de-estudio-de-linux.md) — el plan de seis meses, con la práctica y el mini-proyecto de cada mes.

## Pendiente

- Namespaces, cgroups, seguridad (SELinux, AppArmor), almacenamiento (LVM) y contenedores: el plan los nombra, pero se escriben cuando se estudie ese mes.
