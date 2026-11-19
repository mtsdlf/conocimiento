---
resumen: >-
  Azure tiene tres balanceadores principales: Front Door (global, capa 7, con CDN y WAF),
  Application Gateway (regional, capa 7, con WAF) y Load Balancer (capa 4, regional o global);
  se elige por alcance y por capa.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, Load-balancing options: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview"
  - "Microsoft Learn, Azure Front Door overview: https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview"
  - "Microsoft Learn, Azure Load Balancer SKUs (retiro de Basic): https://learn.microsoft.com/en-us/azure/load-balancer/skus"
  - "Archivo/Cloud/azure-referencia-framework.md (original, entrada y salida, preguntas típicas)"
aliases: [Front Door, Application Gateway, App Gateway, Load Balancer, Traffic Manager, balanceo de carga]
creado: 2026-10-03
revisado:
---

# Balanceadores de carga en Azure

Azure tiene tres balanceadores principales: Front Door (global, capa 7, con CDN y WAF),
Application Gateway (regional, capa 7, con WAF) y Load Balancer (capa 4, regional o global);
se elige por alcance y por capa.

## Dos preguntas para elegir

Elegir el equivocado obliga a rehacer la entrada: un Load Balancer no termina TLS ni rutea por
ruta de URL, y un Application Gateway no reparte tráfico entre regiones. La guía de Microsoft
decide con dos preguntas: ¿el tráfico es HTTP(S)? ¿Es global o de una región?

## Front Door, Application Gateway, Load Balancer y Traffic Manager

| Servicio | Alcance | Capa | Para qué |
|---|---|---|---|
| **Front Door** | Global | 7 (HTTP/S) | Entrada pública de una app en varias regiones: CDN, caché, WAF, Private Link a los orígenes |
| **Application Gateway** | Regional | 7 (y proxy TCP/TLS) | Ruteo por host o ruta, terminación TLS, mTLS, WAF; detrás de Front Door o solo si la app es regional |
| **Load Balancer** | Regional o global | 4 (TCP/UDP) | Tráfico no HTTP, backends de VMs, balanceo interno entre capas |
| **Traffic Manager** (cuarta opción, solo DNS) | Global | DNS | Reparte por DNS entre regiones o nubes; no ve el tráfico |

- **SKU**: el Load Balancer Basic y las IPs públicas Basic se retiraron el 30 de septiembre de
  2025, y Application Gateway v1 el 28 de abril de 2026. Todo diseño nuevo usa Standard y v2.
- **Combinación común**: Front Door con WAF adelante, Application Gateway por región y el cómputo
  privado atrás. Es la entrada de la web global segura de las
  [Arquitecturas de referencia en Azure](../arquitecturas-de-referencia-en-azure.md); lo que va detrás se elige con la
  [Elección de cómputo en Azure](../Computo/eleccion-de-computo-en-azure.md).
- **Lo que suele fallar**: las sondas de salud. Si la sonda pide una ruta que tarda o devuelve
  401, el balanceador saca a todos los backends.

## Una tienda en dos regiones

Una tienda con usuarios en Europa y América despliega en dos regiones. Front Door recibe el
tráfico, cachea las imágenes y manda cada pedido a la región más cercana y sana. En cada región,
un Load Balancer interno reparte entre las VMs de la API.

## Balanceador y NAT Gateway

Una [NAT Gateway](nat-gateway.md), que da salida a internet a una subred; los balanceadores reciben tráfico de
entrada. Un Load Balancer público también puede dar salida, con reglas de salida, pero con un cupo
fijo de puertos por VM.
