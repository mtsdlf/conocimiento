---
tipo: concepto
resumen: >-
  Un private endpoint es una NIC con IP privada en una subred que da acceso, por Private Link, a
  una instancia concreta de un servicio PaaS (una cuenta de Storage, un Key Vault), para poder
  apagar su acceso público.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, What is a private endpoint?: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview"
  - "Microsoft Learn, What is Azure Private Link?: https://learn.microsoft.com/en-us/azure/private-link/private-link-overview"
  - "Azure, Private Link pricing: https://azure.microsoft.com/en-us/pricing/details/private-link/"
  - "Archivo/Cloud/azure-homelab-landing-zone.md (original, §4)"
aliases: [private endpoint, Private Link, PE, endpoint privado]
parte_de: []
requiere: [virtual-network-azure]
relacionado: [service-endpoint, network-security-perimeter]
---

# Private endpoint

Un private endpoint es una NIC con IP privada en una subred que da acceso, por Private Link, a
una instancia concreta de un servicio PaaS (una cuenta de Storage, un Key Vault), para poder
apagar su acceso público.

## Por qué importa

Un servicio PaaS nace con una IP pública. Con un private endpoint, la aplicación llega al
servicio por una IP de su propia [Virtual Network (Azure)](virtual-network-azure.md) y el servicio puede quedar con
*public network access: Disabled*. Es la pieza de un diseño "privado por defecto", y Microsoft la
recomienda sobre los service endpoints.

## Cómo funciona

- **Una IP por instancia**: el endpoint apunta a un recurso, no al servicio entero. Desde esa IP
  no se llega a la cuenta de Storage de otro cliente, lo que corta una vía de fuga de datos.
- **Un endpoint por subrecurso**: en Storage, `blob` y `file` llevan endpoints distintos.
- **Alcance**: la IP es accesible desde la VNet, desde VNets peereadas y desde la red propia por
  VPN o ExpressRoute.
- **DNS**: el cliente sigue usando el nombre público (`cuenta.blob.core.windows.net`). Para que
  resuelva a la IP privada hace falta la zona `privatelink.*`; es la parte que más falla (ver
  [DNS privado para Private Link](dns-privado-para-private-link.md)).
- **Precio**: cada endpoint se cobra por hora más los GB procesados de entrada y de salida.
- **Gobernanza**: [Azure Policy](azure-policy.md) puede negar los recursos con acceso público y crear el registro
  DNS de cada endpoint automáticamente.

## Ejemplo

El spoke `app` tiene la subred `pe` (`10.1.2.0/24`) con dos endpoints: uno a la cuenta de Storage y
otro al Key Vault del proyecto. Los dos servicios tienen el acceso público apagado. Desde la
subred `app`, el nombre del blob resuelve a `10.1.2.4`; desde internet, la conexión se rechaza.

## No confundir con

- [Service endpoint](service-endpoint.md): la subred se identifica ante el servicio, pero el servicio sigue con IP
  pública y no se llega desde la red propia. El private endpoint da una IP privada real.
- [Network security perimeter](network-security-perimeter.md): limita el acceso público de varios PaaS como grupo, sin poner
  IPs en una VNet.

## Relaciones

- Requiere: [Virtual Network (Azure)](virtual-network-azure.md) — la NIC vive en una subred.
- Base de: [DNS privado para Private Link](dns-privado-para-private-link.md) — sin DNS privado, el endpoint no se usa.
- Relacionado: [Service endpoint](service-endpoint.md) — la alternativa más vieja, sin IP privada.
- Relacionado: [Network security perimeter](network-security-perimeter.md) — otra forma de cerrar el acceso público a un PaaS.
