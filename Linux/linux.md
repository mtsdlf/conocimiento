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

Para aprenderlo en orden: [[recorrido-linux-por-dentro]].

## Cómo está hecho

- [[arquitectura-de-linux]] — las capas del sistema y la frontera entre kernel y espacio de usuario; la puerta de entrada al Tema.
- [[llamada-al-sistema]] — cómo un programa le pide algo al kernel; leerla después de la arquitectura.
- [[daemon]] — qué son los procesos de fondo y qué servicios del sistema prestan.
- [[pseudo-sistema-de-archivos]] — cómo `/proc`, `/sys` y `/dev` exponen el kernel como archivos y cómo se ajusta el kernel en vivo.

## Arranque y servicios

- [[arranque-de-linux]] — qué pasa desde que se prende la máquina hasta el login.
- [[systemd]] — cómo el sistema de init arranca, supervisa y registra los servicios.

## La terminal

- [[pipe-y-redireccion]] — cómo se combinan comandos chicos conectando sus flujos de entrada y salida.

## Para consultar

- [[fhs]] — qué va en cada directorio del sistema y dónde están los logs y los archivos de usuarios.
- [[comandos-de-linux]] — los comandos de administración agrupados por función y por familia de distro.
- [[recetas-de-pipes]] — combinaciones de pipes listas para copiar.
- [[plan-de-estudio-de-linux]] — el plan de seis meses, con la práctica y el mini-proyecto de cada mes.

## Pendiente

- Namespaces, cgroups, seguridad (SELinux, AppArmor), almacenamiento (LVM) y contenedores: el plan los nombra, pero se escriben cuando se estudie ese mes.
