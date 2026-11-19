---
resumen: >-
  El VNet peering conecta dos virtual networks de Azure por el backbone de Microsoft, en la misma
  región o entre regiones, para que se vean como una sola red; no es transitivo.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, Virtual network peering: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview"
  - "Microsoft Learn, How to configure subnet peering: https://learn.microsoft.com/en-us/azure/virtual-network/how-to-configure-subnet-peering"
  - "Microsoft Learn, Hub-spoke network topology in Azure: https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección AZURE NETWORKING, peering)"
aliases: [peering, VNet peering, global VNet peering, subnet peering]
creado: 2026-10-03
revisado:
---

# VNet peering

El VNet peering conecta dos virtual networks de Azure por el backbone de Microsoft, en la misma
región o entre regiones, para que se vean como una sola red; no es transitivo.

## La forma más simple de unir VNets

Es la forma más simple de unir redes en Azure: sin gateways, sin cifrado y sin cortar el servicio
al crearlo. Es la pieza de la [Topología hub-and-spoke](topologia-hub-and-spoke.md), donde cada spoke se une al hub.

## Tipos, transitividad, gateway transit y precio

- **Tipos**: *VNet peering* en la misma región y *global VNet peering* entre regiones. Funcionan
  entre suscripciones y entre tenants de Entra ID.
- **Dos lados**: el peering se crea en cada VNet; hasta que existen los dos, no hay tráfico.
- **No transitivo**: si A está peereada con B y B con C, A no llega a C. Para pasar por B hace
  falta un firewall o un NVA en B y una UDR (ver [Ruteo en Azure](ruteo-en-azure.md)).
- **Requisito**: los espacios de direcciones de las dos [VNets](virtual-network-azure.md) no se pueden superponer.
- **Gateway transit**: un spoke puede usar el VPN Gateway o el de ExpressRoute del hub para llegar
  a la red propia (opción *use remote gateways*). Una VNet tiene un solo gateway: el propio o el
  remoto (ver [Conectividad híbrida en Azure](conectividad-hibrida-azure.md)).
- **Precio**: crear el peering es gratis, pero se cobra el tráfico de entrada y de salida por el peering,
  más caro entre regiones.
- **Subnet peering**: conecta solo algunas subredes de cada VNet en lugar del espacio entero.
  A octubre de 2026 requiere habilitar la suscripción por formulario y se configura por CLI,
  PowerShell, API, ARM o Terraform, no por el portal.

**Cómo se comprueba**: las rutas efectivas de una NIC muestran, por cada rango de la VNet remota,
una ruta con next hop *VNet peering*. Si falta, el peering no está conectado en los dos lados.

## Dos spokes que no se ven

El hub `10.0.0.0/20` tiene peering con `spoke-app` (`10.1.0.0/20`) y con `spoke-data`
(`10.2.0.0/20`). Una VM de `spoke-app` llega al DNS del hub, pero no a `spoke-data`: no hay peering
entre los spokes y el peering no es transitivo.

## Peering y VPN VNet a VNet

Una conexión VNet a VNet por VPN Gateway: cifra el tráfico por IPsec, pasa por gateways y cuesta
más. Si existen las dos, el tráfico va por el peering.
