---
resumen: >-
  Automatización de red es la parte de la infraestructura que configura la red como código, con
  Git, pruebas y CI/CD (NetDevOps), y las herramientas que cubren cada paso.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Automatización de red

Automatización de red es la parte de la infraestructura que configura la red como código, con
Git, pruebas y CI/CD (NetDevOps), y las herramientas que cubren cada paso.

Dentro de la [infraestructura](../infraestructura.md), lleva a los equipos de red la misma idea
que el [Aprovisionamiento](../Aprovisionamiento/aprovisionamiento.md) aplica a la nube y GitOps al
clúster: Git como fuente de verdad.

## De la configuración a mano al pipeline

La red tradicional se configura equipo por equipo, por CLI o SSH, y un cambio es difícil de
revisar, repetir y deshacer. Con NetDevOps, la intención vive en archivos de datos y plantillas en
Git, el inventario en una fuente de verdad como NetBox, cada cambio entra por un PR que se valida
antes de tocar un equipo, y la telemetría compara después el estado real con el declarado.

## Las dos notas de automatización de red

- [NetDevOps](netdevops.md) — qué cambia al tratar la configuración de red como código con pruebas
  y CI/CD.
- [Herramientas de NetDevOps](herramientas-de-netdevops.md) — ficha con la herramienta de cada
  función, con enlace a su documentación, consultada el 2026-10-03.
