---
tipo: concepto
resumen: >-
  Un service endpoint extiende la identidad de una subred a un servicio PaaS de Azure por el
  backbone de Microsoft, para que el servicio acepte solo el tráfico de esa subred; el servicio
  sigue teniendo IP pública.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Virtual network service endpoints: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview"
  - "Microsoft Learn, Azure Private Link FAQ: https://learn.microsoft.com/en-us/azure/private-link/private-link-faq"
aliases: [service endpoint, VNet service endpoint, punto de conexión de servicio]
parte_de: []
requiere: [virtual-network-azure]
relacionado: [private-endpoint]
---

# Service endpoint

Un service endpoint extiende la identidad de una subred a un servicio PaaS de Azure por el
backbone de Microsoft, para que el servicio acepte solo el tráfico de esa subred; el servicio
sigue teniendo IP pública.

## Por qué importa

Es la forma más barata de restringir un Storage o un SQL a una red: no tiene costo extra, no
agrega recursos y no toca el DNS. Sirve cuando alcanza con "solo esta subred puede entrar" y no
hace falta una IP privada.

## Cómo funciona

1. Se habilita el service endpoint de un servicio (p. ej. `Microsoft.Storage`) en una subred de
   la [Virtual Network (Azure)](virtual-network-azure.md).
2. Desde ese momento, el tráfico de la subred al servicio va por el backbone y llega con la IP
   privada de origen, no con una pública.
3. En el firewall del servicio se agrega una regla de red virtual que permite esa subred y se
   niega el resto.

**Límites**:

- El DNS sigue resolviendo la IP pública del servicio.
- No sirve para tráfico desde la red propia por VPN o ExpressRoute.
- En Azure SQL aplica solo dentro de la misma región.
- Solo tráfico TCP: un ping (ICMP) no sirve para probarlo.
- La lista de servicios compatibles cambia; está en la página de Microsoft de la fuente.

**Recomendación**: Microsoft recomienda Private Link y private endpoints para el acceso privado a
servicios de Azure. El service endpoint queda para casos simples o de bajo costo.

## Ejemplo

Una cuenta de Storage con logs se configura para aceptar solo la subred `app` de un spoke. Las VMs
de esa subred escriben sin cambios en la aplicación; un intento desde internet o desde otra
subred recibe 403.

## No confundir con

El [Private endpoint](private-endpoint.md): crea una NIC con IP privada para una instancia del servicio, accesible
también desde la red propia, y cuesta por hora y por GB. El service endpoint no crea IP privada
y abre el acceso al servicio, no a una instancia.

## Relaciones

- Requiere: [Virtual Network (Azure)](virtual-network-azure.md) — se habilita por subred.
- Relacionado: [Private endpoint](private-endpoint.md) — la alternativa recomendada, con IP privada.
