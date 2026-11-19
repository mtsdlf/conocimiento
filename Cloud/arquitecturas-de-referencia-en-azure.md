---
resumen: >-
  Tres combinaciones de servicios de Azure que se repiten en los diseños: una web global segura,
  un sistema por eventos y una plataforma analítica; cada una dice qué servicio va en cada capa y
  por qué.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, Azure Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/"
  - "Microsoft Learn, Load-balancing options: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview"
  - "Microsoft Learn, Compare Azure messaging services: https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Patrones de referencia)"
aliases: [patrones de referencia en Azure, reference architectures]
creado: 2026-10-03
revisado:
---

# Arquitecturas de referencia en Azure

Tres combinaciones de servicios de Azure que se repiten en los diseños: una web global segura,
un sistema por eventos y una plataforma analítica; cada una dice qué servicio va en cada capa y
por qué.

## Partir de una combinación conocida

Un diseño no se arma servicio por servicio desde cero. Partir de una combinación conocida y
ajustarla a los requisitos es más rápido y evita olvidar una capa (el WAF, el DNS privado, las
alertas). El Azure Architecture Center publica versiones detalladas de cada una.
[Diseñar una solución en Azure](disenar-una-solucion-en-azure.md) parte de estas combinaciones.

## Las tres combinaciones

**Web global segura**

1. Entrada: Front Door con WAF, que cachea y elige la región (ver
   [Balanceadores de carga en Azure](Redes/balanceadores-de-carga-azure.md)).
2. Cómputo: App Service, Container Apps o AKS, sin IP pública (ver
   [Elección de cómputo en Azure](Computo/eleccion-de-computo-en-azure.md)).
3. Datos: SQL, Cosmos DB o Storage (ver
   [Almacenamiento y bases de datos en Azure](Datos-operacionales/almacenamiento-y-bases-de-datos-en-azure.md)) por [Private endpoint](Redes/Acceso-privado-a-PaaS/private-endpoint.md), con acceso público apagado; Redis como
   cache y Service Bus para desacoplar lo lento.
4. Seguridad: managed identity, Key Vault y Defender for Cloud.
5. Red: [Topología hub-and-spoke](Redes/topologia-hub-and-spoke.md) con firewall en el hub.
6. Operación: [Azure Monitor](Operacion/azure-monitor.md) con alertas sobre los SLO.

**Por eventos**

- Event Grid dispara Functions o Container Apps cuando algo cambia.
- Service Bus lleva el trabajo que tiene que cumplirse en orden y sin perderse.
- Event Hubs recibe la telemetría masiva (ver [Mensajería en Azure](Mensajeria/mensajeria-en-azure.md)).

**Analítica**

Ingesta (Event Hubs o Data Factory) → data lake (ADLS Gen2) → transformación (Databricks o
Fabric) → servicio (SQL o Cosmos DB) → reportes (Power BI), con catálogo y linaje en Purview.

## Un portal de clientes que combina dos patrones

Un portal de clientes usa la web global segura en dos regiones. La generación de facturas en PDF,
que tarda, se saca del request: la API deja un mensaje en Service Bus y un worker en Container
Apps lo procesa. Es la combinación de los dos primeros patrones.

## Arquitectura de una carga y landing zone

La [Azure landing zone](Gobernanza-e-identidad/azure-landing-zone.md): es la base común de todas las suscripciones. Estas arquitecturas son lo
que cada carga de trabajo despliega encima.
