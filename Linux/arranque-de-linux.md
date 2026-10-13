---
tipo: concepto
resumen: >-
  El arranque de Linux es la secuencia firmware → gestor de arranque → kernel con initramfs →
  PID 1 (init) → servicios → login.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Original archivado (generado con IA): Archivo/Linux/linux-componentes-sistema.md, sección 7"
  - "man 7 bootup: https://man7.org/linux/man-pages/man7/bootup.7.html"
  - "man 7 boot: https://man7.org/linux/man-pages/man7/boot.7.html"
  - "Kernel docs, Using the initial RAM disk (initrd): https://docs.kernel.org/admin-guide/initrd.html"
aliases: [Boot sequence, Secuencia de arranque, Boot de Linux]
parte_de: []
requiere: [arquitectura-de-linux]
relacionado: []
---

# Arranque de Linux

El arranque de Linux es la secuencia firmware → gestor de arranque → kernel con initramfs →
PID 1 (init) → servicios → login.

## Por qué importa

Cuando una máquina no arranca, la última etapa que se completó dice dónde buscar. No es lo mismo
quedarse en el menú de GRUB (gestor de arranque) que en una consola de emergencia del initramfs
(no encontró el disco raíz) o en un servicio que no levanta (init).

## Cómo funciona

1. **Firmware** (BIOS o UEFI): inicializa el hardware mínimo y busca un gestor de arranque en un
   disco. Con UEFI, el firmware también puede cargar el kernel directo.
2. **Gestor de arranque** (GRUB, systemd-boot): carga en memoria el kernel y la imagen
   **initramfs**, y le pasa al kernel su línea de comandos, por ejemplo `root=UUID=… ro` (qué disco es la raíz y que se monte primero en solo lectura).
3. **Kernel**: inicializa CPU, memoria y drivers, y descomprime el initramfs en un sistema de
   archivos en memoria. Ese sistema mínimo trae los drivers y las herramientas para encontrar y
   montar el disco raíz real, aunque esté cifrado o en LVM.
4. **Cambio de raíz y PID 1**: montado el disco raíz, se pasa a él y se ejecuta el primer proceso
   del sistema, el **init** (PID 1). En la mayoría de las distribuciones es [[systemd]].
5. **Servicios**: init monta los sistemas de archivos de `/etc/fstab`, configura nombre y red, y
   arranca los [[daemon]] habilitados.
6. **Login**: init lanza `getty` en las consolas o un gestor de pantalla. Al entrar, el shell lee
   sus archivos de inicio (`~/.profile`, `~/.bashrc`).

## Ejemplo

Después de cambiar de disco, el sistema cae a una consola `(initramfs)`. El kernel arrancó, pero
el initramfs no encontró el disco `root=UUID=…` que le pasó GRUB, porque el disco nuevo tiene otro
UUID. El arreglo está en la línea de comandos del kernel que arma el gestor de arranque, no en
los servicios.

## No confundir con

El arranque de un servicio. `systemctl start` levanta un servicio con el sistema ya andando; el
arranque es la secuencia que lleva de la máquina apagada al sistema en funcionamiento.

## Relaciones

- Requiere: [[arquitectura-de-linux]] — la secuencia levanta primero el kernel y después el espacio de usuario.
- Base de: [[systemd]] — el init que toma el control en el paso 4.
