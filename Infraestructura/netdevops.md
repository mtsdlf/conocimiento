---
tipo: concepto
resumen: >-
  NetDevOps aplica prácticas de desarrollo (Git, CI/CD, pruebas, telemetría) a la red: la
  configuración se genera desde código versionado, se valida antes de aplicarse y se compara contra
  el estado real.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Julio Gomez, NetDevOps (repo listado en Cisco Code Exchange): https://github.com/juliogomez/netdevops"
  - "Cisco DevNet, Network Automation Delivery Model, CI/CD: https://developer.cisco.com/docs/network-automation-delivery-model/cicd/"
  - "Batfish, README: https://github.com/batfish/batfish"
  - "Archivo/Infraestructura/netdevops-fundamentos.md (original en inglés, traducido y condensado)"
aliases: [NetDevOps, network as code, red como código, automatización de redes]
parte_de: []
requiere: []
relacionado: [herramientas-de-netdevops]
---

# NetDevOps

NetDevOps aplica prácticas de desarrollo (Git, CI/CD, pruebas, telemetría) a la red: la
configuración se genera desde código versionado, se valida antes de aplicarse y se compara contra
el estado real.

## Por qué importa

La red tradicional se configura a mano, equipo por equipo, por CLI o SSH. Así un cambio es difícil
de revisar, de repetir y de deshacer, y la documentación queda vieja apenas se escribe. NetDevOps
busca que un cambio de red pase por los mismos controles que un cambio de código: revisión, pruebas
automáticas y un registro de quién cambió qué.

## Cómo funciona

- **Red como código**: la intención (topología, VLAN, rutas, ACL) se describe en archivos de datos
  (YAML o JSON) y plantillas, guardados en Git. Según el repo NetDevOps de Julio Gomez, el sistema
  de control de versiones pasa a ser la única fuente de verdad de la configuración.
- **Fuente de verdad del inventario**: Git guarda la intención y las plantillas; una base como
  NetBox guarda el inventario (equipos, direcciones, enlaces) y las plantillas leen de ahí. Son dos
  fuentes de verdad, cada una de un tipo de dato.
- **Pipeline**: cada cambio entra por un pull request. El CI chequea sintaxis, genera la
  configuración y la valida antes de tocar un equipo; una herramienta como Batfish analiza las
  configuraciones y detecta, por ejemplo, una ACL que corta tráfico que no debía. Cisco DevNet
  recomienda que el pipeline sea el único camino para llegar a producción.
- **Verificación continua**: después de aplicar, un sistema de monitoreo recibe la telemetría de
  los equipos, la compara con el estado declarado y avisa cuando hay un desvío (drift).

El flujo completo: cambio en Git → validación y simulación → revisión del PR → despliegue por API o
Ansible → verificación → telemetría.

## Ejemplo

Para agregar una VLAN, alguien edita el archivo de datos del sitio y abre un PR. El CI genera la
configuración de cada switch con una plantilla Jinja, la carga en un laboratorio virtual (por ejemplo, con Containerlab) y
prueba que cada red alcanza a las que debe alcanzar. Al aprobarse el PR, el pipeline aplica el cambio y la telemetría confirma que la VLAN
existe en todos los equipos.

## No confundir con

Un script suelto que configura equipos. Automatizar sin versionar ni validar repite los errores
más rápido; NetDevOps exige además Git como fuente de verdad, pruebas antes del cambio y
verificación después.

## Relaciones

- Relacionado: [[herramientas-de-netdevops]] — qué herramienta cubre cada paso del pipeline.
- Ver también: [[observabilidad]] — la telemetría de red se trata como cualquier otra señal de
  observabilidad.
- Ver también: [[gitops]] (DevOps) — la misma idea de Git como fuente de verdad,
  aplicada a la red.
