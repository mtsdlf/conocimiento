---
resumen: >-
  Azure rutea por defecto entre subredes, VNets conectadas, la red propia e internet con rutas de
  sistema; las route tables (UDR) y las rutas BGP las reemplazan, por ejemplo para forzar que el
  tráfico pase por un firewall.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, Virtual network traffic routing: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview"
  - "Microsoft Learn, Virtual network peering (service chaining): https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview"
aliases: [UDR, user-defined route, route table, tabla de rutas, service chaining]
creado: 2026-10-03
revisado:
---

# Ruteo en Azure

Azure rutea por defecto entre subredes, VNets conectadas, la red propia e internet con rutas de
sistema; las route tables (UDR) y las rutas BGP las reemplazan, por ejemplo para forzar que el
tráfico pase por un firewall.

## Cuándo hace falta tocar el ruteo

En una [Virtual Network (Azure)](virtual-network-azure.md) no hay router que configurar: el ruteo ya funciona. Hace falta
tocarlo cuando el tráfico tiene que pasar por un punto de control (un firewall en el hub) o cuando
la red propia anuncia rutas que Azure tiene que conocer.

## Rutas de sistema, UDR y BGP

Hay tres orígenes de rutas:

| Origen | Qué hace | Se puede borrar |
|---|---|---|
| **Sistema** | Azure las crea en cada subred: el espacio de la VNet, `0.0.0.0/0` a internet, y los rangos privados que no son de la VNet con next hop *None* (se descartan). Se suman las de peering y gateway al crearlos | No, solo reemplazar |
| **UDR** (route table) | Rutas propias; una route table por subred, como máximo | Sí |
| **BGP** | Las que anuncia la red propia por un VPN Gateway o ExpressRoute; llegan a todas las subredes | Se puede apagar la propagación por route table |

**Cuál gana**: primero el prefijo más largo; si empatan, UDR antes que BGP y BGP antes que sistema.

**Service chaining**: una UDR en un spoke con `0.0.0.0/0` y next hop la IP de un firewall o un NVA
(network virtual appliance: una VM que hace de firewall o router) en el hub peereado hace que todo el egreso pase por ahí. El next hop también puede ser un VPN
Gateway, pero no un gateway de ExpressRoute. Es lo que centraliza el egreso en el hub de una
[Topología hub-and-spoke](topologia-hub-and-spoke.md); las rutas BGP de la red propia llegan por la
[Conectividad híbrida en Azure](conectividad-hibrida-azure.md).

## El egreso de un spoke por el firewall del hub

El spoke `10.1.0.0/20` tiene una route table con `0.0.0.0/0 → 10.0.1.4` (Azure Firewall en el hub).
Una VM del spoke que llama a una API pública sale por el firewall, que registra el FQDN. Las rutas
efectivas de la NIC muestran la UDR como activa y la ruta de sistema a internet como inválida.

## La ruta decide por dónde, el NSG si pasa

El [Network security group](network-security-group.md), que decide si un paquete pasa; la ruta decide por dónde va. Un
paquete puede tener ruta y estar bloqueado, o estar permitido y no tener ruta.
