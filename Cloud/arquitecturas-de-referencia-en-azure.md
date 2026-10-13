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
   [[balanceadores-de-carga-azure]]).
2. Cómputo: App Service, Container Apps o AKS, sin IP pública (ver
   [[eleccion-de-computo-en-azure]]).
3. Datos: SQL, Cosmos DB o Storage por [[private-endpoint]], con acceso público apagado; Redis como
   cache y Service Bus para desacoplar lo lento.
4. Seguridad: managed identity, Key Vault y Defender for Cloud.
5. Red: [[topologia-hub-and-spoke]] con firewall en el hub.
6. Operación: [[azure-monitor]] con alertas sobre los SLO.

**Por eventos**

- Event Grid dispara Functions o Container Apps cuando algo cambia.
- Service Bus lleva el trabajo que tiene que cumplirse en orden y sin perderse.
- Event Hubs recibe la telemetría masiva (ver [[mensajeria-en-azure]]).

**Analítica**

Ingesta (Event Hubs o Data Factory) → data lake (ADLS Gen2) → transformación (Databricks o
Fabric) → servicio (SQL o Cosmos DB) → reportes (Power BI), con catálogo y linaje en Purview.

## Ejemplo

Un portal de clientes usa la web global segura en dos regiones. La generación de facturas en PDF,
que tarda, se saca del request: la API deja un mensaje en Service Bus y un worker en Container
Apps lo procesa. Es la combinación de los dos primeros patrones.

## No confundir con

La [[azure-landing-zone]]: es la base común de todas las suscripciones. Estas arquitecturas son lo
que cada carga de trabajo despliega encima.

## Relaciones

- Requiere: [[balanceadores-de-carga-azure]] y [[eleccion-de-computo-en-azure]] — las dos
  decisiones que cada patrón toma.
- Usa: [[mensajeria-en-azure]], [[almacenamiento-y-bases-de-datos-en-azure]] y [[azure-monitor]].
- La usa: [[disenar-una-solucion-en-azure]] — como punto de partida.
