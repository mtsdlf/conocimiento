---
tipo: concepto
resumen: >-
  Una Virtual Network (VNet) es la red privada y aislada de Azure en una región: se divide en
  subredes, abarca todas las zonas de disponibilidad de la región y no tiene costo propio.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, What is Azure Virtual Network?: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview"
  - "Microsoft Learn, Default outbound access in Azure: https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access"
  - "Microsoft Learn, Azure Resource Manager vs. classic deployment: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/deployment-models"
aliases: [VNet, Virtual Network, red virtual de Azure]
parte_de: []
requiere: []
relacionado: []
---

# Virtual Network (Azure)

Una Virtual Network (VNet) es la red privada y aislada de Azure en una región: se divide en
subredes, abarca todas las zonas de disponibilidad de la región y no tiene costo propio.

## Por qué importa

Casi todo lo que tiene IP privada en Azure vive en una VNet: VMs, nodos de AKS, private endpoints,
gateways. El espacio de direcciones que se elige al crearla limita qué se puede conectar después:
dos VNets con rangos superpuestos no se pueden unir por peering.

## Cómo funciona

- **Espacio de direcciones y subredes**: la VNet tiene uno o más rangos privados (p. ej.
  `10.1.0.0/20`) y se parte en subredes por propósito: aplicación, datos, private endpoints.
  Algunos servicios piden subred propia (el gateway, el DNS Private Resolver).
- **Zonas**: una VNet y sus subredes cubren todas las zonas de la región; una VM zonal no obliga a
  partir la red por zona.
- **Precio**: la VNet es gratis; se cobran los recursos y el tráfico entre VNets.
- **Salida a internet**: desde el 31 de marzo de 2026, las subredes de VNets nuevas creadas con
  las API actuales son privadas por defecto (`defaultOutboundAccess=false`): una VM no sale a
  internet sin un método explícito, como una [[nat-gateway]]. Las VNets existentes y las creadas
  con versiones de API anteriores conservan el acceso de salida por defecto.
- **Lo que se le suma**: el filtrado con [[network-security-group]], el ruteo con
  [[ruteo-en-azure]], la conexión con otras VNets por [[vnet-peering]] y con la red propia por
  [[conectividad-hibrida-azure]].

**Para llegar a un servicio PaaS** desde la VNet hay tres formas:

1. Desplegar una instancia dedicada del servicio dentro de la VNet (p. ej. App Service Environment).
2. Un [[private-endpoint]]: una IP privada en la subred para una instancia del servicio.
3. Un [[service-endpoint]]: la subred se identifica ante el servicio, que sigue con IP pública.

## Ejemplo

Un proyecto usa `10.1.0.0/20` con tres subredes: `app` (`10.1.1.0/24`), `pe` para private
endpoints (`10.1.2.0/24`) y `test` (`10.1.3.0/24`). El hub usa `10.0.0.0/20`, así que el peering
entre los dos funciona sin conflictos.

## No confundir con

Una VNet clásica: el modelo de despliegue clásico está retirado y todo recurso nuevo se crea con
Azure Resource Manager.

## Relaciones

- Base de: [[network-security-group]], [[ruteo-en-azure]], [[vnet-peering]], [[private-endpoint]],
  [[service-endpoint]], [[nat-gateway]] y [[conectividad-hibrida-azure]].
