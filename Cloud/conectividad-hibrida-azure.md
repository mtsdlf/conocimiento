---
tipo: concepto
resumen: >-
  La conectividad híbrida une una red propia con Azure de tres formas: VPN punto a sitio (un
  equipo), VPN sitio a sitio (una red por IPsec sobre internet) y ExpressRoute (un circuito
  privado); con gateway transit, los spokes usan el gateway del hub.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, What is Azure VPN Gateway?: https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways"
  - "Microsoft Learn, About VPN Gateway SKU consolidation and migration: https://learn.microsoft.com/en-us/azure/vpn-gateway/gateway-sku-consolidation"
  - "Microsoft Learn, What is Azure ExpressRoute?: https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction"
  - "Microsoft Learn, Virtual network peering (gateway transit): https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview"
aliases: [VPN Gateway, ExpressRoute, VPN sitio a sitio, VPN punto a sitio, gateway transit, S2S, P2S]
parte_de: []
requiere: [virtual-network-azure]
relacionado: []
---

# Conectividad híbrida en Azure

La conectividad híbrida une una red propia con Azure de tres formas: VPN punto a sitio (un
equipo), VPN sitio a sitio (una red por IPsec sobre internet) y ExpressRoute (un circuito
privado); con gateway transit, los spokes usan el gateway del hub.

## Por qué importa

Una aplicación en Azure que lee una base de la oficina, o un administrador que entra a una VM
sin IP pública, necesitan un camino privado entre las dos redes. La opción elegida fija el costo,
el ancho de banda y si el tráfico pasa por internet.

## Cómo funciona

| Opción | Qué conecta | Por dónde va | Cuándo |
|---|---|---|---|
| **VPN punto a sitio** (P2S) | Un equipo con un cliente VPN | Internet, cifrado (OpenVPN, IKEv2) | Personas que trabajan remoto |
| **VPN sitio a sitio** (S2S) | Un dispositivo VPN de la red propia con un VPN Gateway | Internet, IPsec | Una oficina; rápido de armar y barato |
| **ExpressRoute** | La red propia con Microsoft por un proveedor | Circuito privado, no internet | Ancho de banda estable, latencia predecible, cumplimiento |

- **El gateway** vive en una subred propia (`GatewaySubnet`) de la VNet. Las rutas de la red propia
  llegan por BGP (ver [Ruteo en Azure](ruteo-en-azure.md)).
- **Gateway transit**: en una [Topología hub-and-spoke](topologia-hub-and-spoke.md), el gateway está en el hub y cada spoke
  activa *use remote gateways* en su [VNet peering](vnet-peering.md). Una VNet tiene un solo gateway, propio o
  remoto.
- **SKU**: los SKU de VPN Gateway sin redundancia de zona (VpnGw1 a VpnGw5) no se pueden crear
  desde noviembre de 2025 y se migran a los AZ (VpnGw1AZ a VpnGw5AZ). El SKU Basic sigue, sin BGP.

## Ejemplo

Una empresa con dos oficinas pone un VPN Gateway en el hub con dos conexiones S2S. Los spokes de
cada proyecto usan ese gateway por gateway transit y llegan a la base de datos de la oficina por
IP privada, sin gateway propio.

## No confundir con

El [VNet peering](vnet-peering.md), que une dos VNets de Azure por el backbone de Microsoft sin gateway. La
conectividad híbrida une Azure con una red que no es de Azure.

## Relaciones

- Requiere: [Virtual Network (Azure)](virtual-network-azure.md) — el gateway vive en una subred de la VNet.
- Usa: [VNet peering](vnet-peering.md) y [Ruteo en Azure](ruteo-en-azure.md) — gateway transit y rutas BGP.
- La usa: [DNS privado para Private Link](dns-privado-para-private-link.md) — desde la red propia, los nombres `privatelink.*` se
  resuelven por este camino.
