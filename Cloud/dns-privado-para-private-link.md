---
tipo: concepto
resumen: >-
  Para usar un private endpoint, el nombre público del servicio tiene que resolver a su IP privada:
  se logra con zonas DNS privadas privatelink.* vinculadas a las VNets y, desde la red propia, con
  Azure DNS Private Resolver.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Azure Private Endpoint DNS integration: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns-integration"
  - "Microsoft Learn, Azure Private Endpoint private DNS zone values: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns"
  - "Microsoft Learn, Private Link and DNS integration at scale: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/private-link-and-dns-integration-at-scale"
  - "Microsoft Learn, What is Azure DNS Private Resolver?: https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview"
  - "Microsoft Learn, What is IP address 168.63.129.16?: https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16"
  - "Archivo/Cloud/azure-homelab-landing-zone.md (original, §9 colisiones de DNS)"
aliases: [privatelink DNS, Private DNS Zone, DNS Private Resolver, PDZ]
parte_de: []
requiere: [private-endpoint]
relacionado: []
---

# DNS privado para Private Link

Para usar un private endpoint, el nombre público del servicio tiene que resolver a su IP privada:
se logra con zonas DNS privadas privatelink.* vinculadas a las VNets y, desde la red propia, con
Azure DNS Private Resolver.

## Por qué importa

El [[private-endpoint]] puede estar bien creado y la aplicación igual sale a la IP pública, porque
resolvió el nombre con un DNS que no conoce la zona privada. Con el acceso público apagado, eso
se ve como un 403 o un timeout que no parece un problema de DNS.

## Cómo funciona

1. Al crear el endpoint, el nombre público pasa a ser un CNAME a
   `cuenta.privatelink.blob.core.windows.net`.
2. Una **zona DNS privada** con ese nombre (`privatelink.blob.core.windows.net`) guarda el
   registro A con la IP del endpoint.
3. La zona se **vincula** a cada VNet que tiene que resolverla. El DNS de Azure (`168.63.129.16`)
   responde la IP privada solo en las VNets vinculadas.
4. **Desde la red propia**, el DNS local reenvía esos dominios al endpoint de entrada de un
   **DNS Private Resolver** en el hub, que consulta al DNS de Azure.

```mermaid
sequenceDiagram
  participant App as Carga en el spoke
  participant DNS as DNS de Azure (168.63.129.16)
  participant Zona as Zona privatelink.* vinculada
  participant PE as Private endpoint (NIC)
  App->>DNS: ¿cuenta.blob.core.windows.net?
  DNS->>Zona: CNAME a cuenta.privatelink.blob...
  Zona-->>DNS: A 10.1.2.4
  DNS-->>App: 10.1.2.4
  App->>PE: TLS a 10.1.2.4
```

**Una zona por servicio, compartida**: la guía de Microsoft centraliza las zonas `privatelink.*`
en la suscripción de conectividad y las vincula a todas las VNets. Dos endpoints del mismo
recurso en VNets distintas que comparten la zona pisan el mismo registro A: Microsoft recomienda
un solo endpoint por recurso en una red con DNS común.

## Ejemplo

Un homelab con el hub y dos spokes comparte las zonas de blob y de Key Vault, vinculadas a las
tres VNets. Cada recurso tiene un solo endpoint, en el spoke de su proyecto; así se evitó la
colisión de registros que habría aparecido con un segundo endpoint al mismo Storage desde el otro
spoke.

## No confundir con

[[split-horizon-dns]]: un nombre que resuelve distinto según quién pregunta. La zona `privatelink`
es un caso de eso dentro de Azure: el mismo nombre da la IP privada en las VNets vinculadas y la
pública en internet.

## Relaciones

- Requiere: [[private-endpoint]] — la zona guarda la IP del endpoint.
- Usa: [[conectividad-hibrida-azure]] — el camino desde la red propia hasta el resolver.
- En otro Tema: [[split-horizon-dns]] — el mismo principio aplicado a una LAN.
