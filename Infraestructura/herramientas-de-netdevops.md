---
tipo: ficha
resumen: >-
  Herramientas de NetDevOps por función (fuente de verdad, modelos y protocolos, plantillas,
  automatización, validación, pruebas y laboratorio), cada una con enlace a su documentación.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "https://netboxlabs.com/docs/netbox/"
  - "https://docs.nautobot.com/projects/core/en/stable/"
  - "https://www.openconfig.net/"
  - "https://www.rfc-editor.org/rfc/rfc7950"
  - "https://www.rfc-editor.org/rfc/rfc6241"
  - "https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md"
  - "https://jinja.palletsprojects.com/en/stable/"
  - "https://docs.ansible.com/ansible/latest/network/getting_started/index.html"
  - "https://nornir.readthedocs.io/en/latest/"
  - "https://napalm.readthedocs.io/en/latest/"
  - "https://github.com/ktbyers/netmiko"
  - "https://batfish.org/"
  - "https://developer.cisco.com/docs/pyats/"
  - "https://containerlab.dev/"
  - "Archivo/Infraestructura/netdevops-fundamentos.md (§6 y §9.1)"
aliases: [herramientas de automatización de redes]
parte_de: []
requiere: []
relacionado: [netdevops]
---

# Herramientas de NetDevOps

Herramientas de NetDevOps por función (fuente de verdad, modelos y protocolos, plantillas,
automatización, validación, pruebas y laboratorio), cada una con enlace a su documentación.

## Fuente

Cada fila enlaza a la documentación oficial; las descripciones salen de ahí (consultadas el
2026-10-03).

## Valores

| Función | Herramienta | Qué es |
|---|---|---|
| Fuente de verdad | [NetBox](https://netboxlabs.com/docs/netbox/) | IPAM (gestión de direcciones IP) y DCIM (inventario de equipos y racks) con API, pensada como fuente de verdad para automatizar la red |
| Fuente de verdad | [Nautobot](https://docs.nautobot.com/projects/core/en/stable/) | fuente de verdad y plataforma de automatización de red, open source |
| Modelos de datos | [YANG](https://www.rfc-editor.org/rfc/rfc7950) (RFC 7950) | lenguaje para modelar configuración, estado, RPC y notificaciones |
| Modelos de datos | [OpenConfig](https://www.openconfig.net/) | modelos YANG neutrales al fabricante, definidos por operadores |
| Protocolo | [NETCONF](https://www.rfc-editor.org/rfc/rfc6241) (RFC 6241) | instala, cambia y borra la configuración de un equipo por RPC en XML |
| Protocolo y telemetría | [gNMI](https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md) | protocolo sobre gRPC para leer y cambiar configuración y para streaming de telemetría |
| Plantillas | [Jinja](https://jinja.palletsprojects.com/en/stable/) | motor de plantillas de Python; genera la configuración desde datos |
| Automatización | [Ansible](https://docs.ansible.com/ansible/latest/network/getting_started/index.html) | automatización sin agente, por SSH o HTTPS, para muchos fabricantes |
| Automatización | [Nornir](https://nornir.readthedocs.io/en/latest/) | framework de automatización escrito en Python y usado desde Python |
| Abstracción | [NAPALM](https://napalm.readthedocs.io/en/latest/) | biblioteca de Python con una API única para distintos sistemas operativos de red |
| Conexión | [Netmiko](https://github.com/ktbyers/netmiko) | biblioteca que simplifica las conexiones por CLI a equipos de varios fabricantes |
| Validación | [Batfish](https://batfish.org/) | analiza configuraciones para encontrar errores antes de desplegarlas |
| Pruebas | [pyATS](https://developer.cisco.com/docs/pyats/) | framework de pruebas y automatización de red de Cisco |
| Laboratorio | [Containerlab](https://containerlab.dev/) | levanta topologías de red en contenedores, útil para probar en CI |

## Relaciones

- Detalla: [NetDevOps](netdevops.md) — las herramientas concretas de cada paso del pipeline.
