---
tipo: concepto
resumen: >-
  DevOps Topologies es el catálogo de Matthew Skelton, ampliado por Manuel Pais, de nueve formas de
  organizar la relación entre Dev y Ops (Types 1 a 9) y ocho anti-patrones (Anti-Types A a H).
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Matthew Skelton y Manuel Pais, DevOps Topologies (CC BY-SA 4.0): https://web.devopstopologies.com/"
aliases: [DevOps Team Topologies, Types y Anti-Types de DevOps]
parte_de: []
requiere: []
relacionado: [team-topologies, anti-patron-equipo-devops]
---

# DevOps Topologies

DevOps Topologies es el catálogo de Matthew Skelton, ampliado por Manuel Pais, de nueve formas de
organizar la relación entre Dev y Ops (Types 1 a 9) y ocho anti-patrones (Anti-Types A a H).

## Por qué importa

Da nombres comunes para diagnosticar cómo colaboran desarrollo y operaciones y hacia dónde
moverlos. La primera versión es de 2013; el catálogo tiene licencia CC BY-SA 4.0.

## Cómo funciona

**Types** (formas que funcionan según el contexto):

| Type | Nombre | Idea |
|---|---|---|
| 1 | Dev and Ops Collaboration | especialistas que colaboran en objetivos comunes |
| 2 | Fully Shared Ops Responsibilities | operaciones dentro de los equipos de producto |
| 3 | Ops as Infrastructure-as-a-Service | operaciones como proveedor interno de nube |
| 4 | DevOps as an External Service | operaciones tercerizadas |
| 5 | DevOps Team with an Expiry Date | equipo temporal que acerca Dev y Ops |
| 6 | DevOps Advocacy Team | equipo que facilita la colaboración sin operar |
| 7 | SRE Team (Google Model) | SRE que puede rechazar software no operable |
| 8 | Container-Driven Collaboration | los contenedores marcan el límite entre Dev y Ops |
| 9 | Dev and DBA Collaboration | desarrollo y DBAs colaboran |

**Anti-Types** (formas que fallan):

| Anti-Type | Nombre | Idea |
|---|---|---|
| A | Dev and Ops Silos | "tirar por encima de la pared" |
| B | DevOps Team Silo | un equipo DevOps que se vuelve otro silo |
| C | Dev Don't Need Ops | desarrollo subestima lo operativo |
| D | DevOps as Tools Team | solo herramientas, sin colaboración |
| E | Rebranded SysAdmin | sysadmins renombrados sin otro cambio |
| F | Ops Embedded in Dev Team | lo operativo absorbido y postergado |
| G | Dev and DBA Silos | DBAs como guardianes que frenan |
| H | Fake SRE | SRE de nombre, misma separación |

## Ejemplo

Un equipo "DevOps" permanente que hace todos los despliegues es el Anti-Type B. Una salida es
convertirlo en un Type 5, con fecha de disolución, y llegar después al Type 1.

## No confundir con

[[team-topologies|Team Topologies]], el modelo posterior de los mismos autores, que generaliza el
diagnóstico a todos los tipos de equipo.

## Relaciones

- Relacionado: [[team-topologies]] — el modelo general que vino después.
- Relacionado: [[anti-patron-equipo-devops]] — el Anti-Type B, con nota propia.
- Base de: [[evaluar-la-colaboracion-dev-ops]] — el diagnóstico usa estos Types y Anti-Types.
