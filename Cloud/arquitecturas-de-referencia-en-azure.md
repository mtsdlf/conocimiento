---
tipo: concepto
resumen: >-
  Tres combinaciones de servicios de Azure que se repiten en los diseños: una web global segura,
  un sistema por eventos y una plataforma analítica; cada una dice qué servicio va en cada capa y
  por qué.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Azure Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/"
  - "Microsoft Learn, Load-balancing options: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview"
  - "Microsoft Learn, Compare Azure messaging services: https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Patrones de referencia)"
aliases: [patrones de referencia en Azure, reference architectures]
parte_de: []
requiere: [balanceadores-de-carga-azure, eleccion-de-computo-en-azure]
relacionado: []
---

# Arquitecturas de referencia en Azure

Tres combinaciones de servicios de Azure que se repiten en los diseños: una web global segura,
un sistema por eventos y una plataforma analítica; cada una dice qué servicio va en cada capa y
por qué.

## Por qué importa

Un diseño no se arma servicio por servicio desde cero. Partir de una combinación conocida y
ajustarla a los requisitos es más rápido y evita olvidar una capa (el WAF, el DNS privado, las
alertas). El Azure Architecture Center publica versiones detalladas de cada una.

## Cómo funciona

**Web global segura**

1. Entrada: Front Door con WAF, que cachea y elige la región (ver
   [Balanceadores de carga en Azure](balanceadores-de-carga-azure.md)).
2. Cómputo: App Service, Container Apps o AKS, sin IP pública (ver
   [Elección de cómputo en Azure](eleccion-de-computo-en-azure.md)).
3. Datos: SQL, Cosmos DB o Storage por [Private endpoint](private-endpoint.md), con acceso público apagado; Redis como
   cache y Service Bus para desacoplar lo lento.
4. Seguridad: managed identity, Key Vault y Defender for Cloud.
5. Red: [Topología hub-and-spoke](topologia-hub-and-spoke.md) con firewall en el hub.
6. Operación: [Azure Monitor](azure-monitor.md) con alertas sobre los SLO.

**Por eventos**

- Event Grid dispara Functions o Container Apps cuando algo cambia.
- Service Bus lleva el trabajo que tiene que cumplirse en orden y sin perderse.
- Event Hubs recibe la telemetría masiva (ver [Mensajería en Azure](mensajeria-en-azure.md)).

**Analítica**

Ingesta (Event Hubs o Data Factory) → data lake (ADLS Gen2) → transformación (Databricks o
Fabric) → servicio (SQL o Cosmos DB) → reportes (Power BI), con catálogo y linaje en Purview.

## Ejemplo

Un portal de clientes usa la web global segura en dos regiones. La generación de facturas en PDF,
que tarda, se saca del request: la API deja un mensaje en Service Bus y un worker en Container
Apps lo procesa. Es la combinación de los dos primeros patrones.

## No confundir con

La [Azure landing zone](azure-landing-zone.md): es la base común de todas las suscripciones. Estas arquitecturas son lo
que cada carga de trabajo despliega encima.

## Relaciones

- Requiere: [Balanceadores de carga en Azure](balanceadores-de-carga-azure.md) y [Elección de cómputo en Azure](eleccion-de-computo-en-azure.md) — las dos
  decisiones que cada patrón toma.
- Usa: [Mensajería en Azure](mensajeria-en-azure.md), [Almacenamiento y bases de datos en Azure](almacenamiento-y-bases-de-datos-en-azure.md) y [Azure Monitor](azure-monitor.md).
- La usa: [Diseñar una solución en Azure](disenar-una-solucion-en-azure.md) — como punto de partida.
