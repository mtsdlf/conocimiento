---
tipo: concepto
resumen: >-
  NAT Gateway es el servicio de Azure que da a una o más subredes una IP pública fija de salida a
  internet y reparte los puertos SNAT de forma dinámica, lo que evita que fallen las conexiones
  salientes por agotamiento de puertos.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, What is Azure NAT Gateway?: https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview"
  - "Microsoft Learn, Default outbound access in Azure: https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access"
  - "Archivo/Cloud/azure-referencia-framework.md (original, red y gotchas de SNAT)"
aliases: [NAT Gateway, Azure NAT, SNAT, agotamiento de SNAT]
parte_de: []
requiere: [virtual-network-azure]
relacionado: []
---

# NAT Gateway

NAT Gateway es el servicio de Azure que da a una o más subredes una IP pública fija de salida a
internet y reparte los puertos SNAT de forma dinámica, lo que evita que fallen las conexiones
salientes por agotamiento de puertos.

## Por qué importa

Desde marzo de 2026, las subredes de las VNets nuevas son privadas por defecto: sin un método de
salida explícito, una VM no llega a internet (ver [Virtual Network (Azure)](virtual-network-azure.md)). Microsoft recomienda
NAT Gateway para la mayoría de los casos. Además, una IP de salida fija es lo que pide un tercero
para poner a la aplicación en su lista de IPs permitidas.

## Cómo funciona

- **Asociación**: a nivel de subred. Una subred tiene una sola NAT Gateway; una NAT Gateway puede
  servir a varias subredes de la misma VNet, pero no a varias VNets.
- **Solo salida**: no acepta conexiones entrantes no solicitadas; las respuestas a lo que salió sí
  vuelven.
- **SNAT**: cada conexión saliente usa un puerto de la IP pública. Con un balanceador o con IPs
  por instancia, cada VM tiene un cupo fijo de puertos y muchas conexiones concurrentes lo agotan:
  las llamadas fallan de forma intermitente. NAT Gateway reparte los puertos de todas sus IPs
  entre todas las VMs según la demanda.
- **Prioridad**: en la subred, NAT Gateway gana sobre el balanceador y las IPs públicas de las
  VMs; una UDR que manda `0.0.0.0/0` a un firewall gana sobre la NAT.
- **SKU**: Standard (zonal, hasta 16 IPs) y StandardV2 (redundante entre zonas, con IPv6 y flow
  logs), al mismo precio. StandardV2 pide IPs públicas StandardV2 y no se migra en el lugar.

## Ejemplo

Un servicio en 20 VMs llama a una API de pagos que solo acepta IPs registradas. Con una NAT
Gateway en la subred, todas salen por la misma IP pública y los errores de conexión que aparecían
en los picos desaparecen porque los puertos SNAT ya no se agotan.

## No confundir con

Azure Firewall como salida: también da una IP fija, pero inspecciona y registra el tráfico, sirve
a varias VNets desde el hub y cuesta bastante más. Si solo hace falta IP fija y escala de SNAT,
alcanza la NAT Gateway.

## Relaciones

- Requiere: [Virtual Network (Azure)](virtual-network-azure.md) — se asocia a sus subredes.
- La usa: [Topología hub-and-spoke](topologia-hub-and-spoke.md) — una NAT por spoke es la salida más barata.
- La usa: [Verificar la conectividad privada en Azure](verificar-conectividad-privada-en-azure.md) — el paso que comprueba la IP de salida.
