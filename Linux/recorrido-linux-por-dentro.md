---
tipo: recorrido
resumen: >-
  Orden de lectura para entender cómo funciona Linux por dentro, para quien sabe usar la terminal
  y quiere administrarlo.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [linux]
---

# Linux por dentro

Orden de lectura para entender cómo funciona Linux por dentro, para quien sabe usar la terminal
y quiere administrarlo.

1. [[arquitectura-de-linux]] — va primero porque todas las demás notas ubican su tema en una de
   estas capas.
2. [[llamada-al-sistema]] — la frontera entre las dos capas principales, que la arquitectura solo
   nombra.
3. [[daemon]] — los servicios del espacio de usuario, que hay que conocer antes de ver quién los
   arranca.
4. [[arranque-de-linux]] — cómo se levantan las capas en orden, del firmware al login.
5. [[systemd]] — el init que toma el control en el arranque y vigila los daemons.
6. [[pseudo-sistema-de-archivos]] — cómo el kernel se muestra como archivos; usa lo visto en
   arquitectura y los cgroups de systemd.
7. [[pipe-y-redireccion]] — la forma de combinar las herramientas de la terminal para
   inspeccionar todo lo anterior.

Para consultar: [[fhs]], [[comandos-de-linux]], [[recetas-de-pipes]] y
[[plan-de-estudio-de-linux]].

**Al terminar**: se sabe en qué capa buscar un problema, qué pasa en cada etapa del arranque,
cómo se administra un servicio y cómo leer y ajustar el kernel desde `/proc` y `/sys`. Para
practicar mes a mes, el siguiente paso es el [[plan-de-estudio-de-linux]].
