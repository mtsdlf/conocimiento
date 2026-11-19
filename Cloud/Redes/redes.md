---
resumen: >-
  Redes es la parte de Cloud que da a cada recurso una dirección privada, filtra y rutea su
  tráfico, une redes entre sí y con la red propia, y decide por dónde entra, sale y llega a los
  servicios PaaS.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Redes

Redes es la parte de Cloud que da a cada recurso una dirección privada, filtra y rutea su
tráfico, une redes entre sí y con la red propia, y decide por dónde entra, sale y llega a los
servicios PaaS.

Dentro de [Cloud](../cloud.md), la red es lo que conecta al [cómputo](../Computo/computo.md) con
los [datos operacionales](../Datos-operacionales/datos-operacionales.md) sin pasar por internet. Su
forma la fija la [landing zone](../Gobernanza-e-identidad/azure-landing-zone.md) de
[Gobernanza e identidad](../Gobernanza-e-identidad/gobernanza-e-identidad.md), que suele ser un
hub-and-spoke, y lo que procesa (el tráfico entre VNets, los private endpoints, el egreso) se paga
por GB, que es una de las palancas de [FinOps](../FinOps/finops.md).

## De la VNet al hub-and-spoke

Todo empieza en la VNet: una red privada por región, partida en subredes por propósito, cuyo
espacio de direcciones limita qué se puede unir después. Sobre ella, el NSG decide si un paquete
pasa y el ruteo decide por dónde va. El peering une dos VNets y no es transitivo; el hub-and-spoke
usa esa falta de transitividad para aislar a cada proyecto en su spoke y compartir en el hub lo
caro o delicado: el gateway, el firewall y el DNS. La conectividad híbrida suma la red propia por
VPN o ExpressRoute, a través del gateway del hub.

## Entrada y salida

El tráfico que entra pasa por un balanceador, elegido por dos preguntas: si es HTTP(S) y si es
global o de una región. El que sale necesita, desde marzo de 2026, un método explícito: una NAT
Gateway por subred, o un firewall en el hub cuando además hay que inspeccionar. El acceso a los
servicios PaaS sin IP pública es una subparte propia, porque tiene sus piezas y casi todas sus
fallas están en el DNS.

## Cómo se prueba

Una red privada se verifica desde adentro: el nombre del servicio resuelve a IP privada, la salida
tiene la IP de la NAT y otro spoke no responde. Si algo falla, se aísla la capa en orden:
aplicación, NSG, rutas efectivas, Network Watcher y flow logs.

## Qué hay adentro de la red

- [Virtual Network (Azure)](virtual-network-azure.md) — la red privada de Azure, sus subredes y la salida a internet. Leerla primero.
- [Network security group](network-security-group.md) — el filtro por IP y puerto de cada subred o NIC.
- [Ruteo en Azure](ruteo-en-azure.md) — rutas de sistema, UDR y BGP, y cómo forzar el paso por un firewall.
- [VNet peering](vnet-peering.md) — cómo se unen dos VNets y por qué no es transitivo.
- [Topología hub-and-spoke](topologia-hub-and-spoke.md) — lo compartido en el hub y cada proyecto aislado en su spoke.
- [Conectividad híbrida en Azure](conectividad-hibrida-azure.md) — VPN y ExpressRoute para unir la red propia con Azure.
- [NAT Gateway](nat-gateway.md) — IP de salida fija y sin agotamiento de SNAT.
- [Balanceadores de carga en Azure](balanceadores-de-carga-azure.md) — Front Door, Application Gateway y Load Balancer: cuál para qué.
- [Acceso privado a PaaS](Acceso-privado-a-PaaS/acceso-privado-a-paas.md) — private endpoint, su DNS, service endpoint y network security perimeter.
- [Verificar la conectividad privada en Azure](verificar-conectividad-privada-en-azure.md) — los pasos para probar private endpoints, egreso por NAT y aislamiento entre spokes.
