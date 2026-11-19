---
resumen: >-
  Un network security perimeter (NSP) agrupa recursos PaaS de Azure que viven fuera de las VNets
  (Storage, Key Vault, Event Hubs) y les niega el acceso público salvo reglas explícitas de entrada
  y de salida; funciona en modo Transition o Enforced.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, What is a network security perimeter?: https://learn.microsoft.com/en-us/azure/private-link/network-security-perimeter-concepts"
aliases: [NSP, network security perimeter, perímetro de seguridad de red]
creado: 2026-10-03
revisado:
---

# Network security perimeter

Un network security perimeter (NSP) agrupa recursos PaaS de Azure que viven fuera de las VNets
(Storage, Key Vault, Event Hubs) y les niega el acceso público salvo reglas explícitas de entrada
y de salida; funciona en modo Transition o Enforced.

## Una sola frontera contra la fuga de datos

Un PaaS con acceso público puede recibir de cualquier origen y, peor, mandar datos a cualquier
destino. Configurar el firewall de cada recurso por separado deja huecos. El perímetro pone una
sola frontera alrededor de un grupo de recursos y deja registro de lo que entra y sale, lo que
corta la fuga de datos hacia destinos no autorizados.

## Miembros, reglas y modos

- **Miembros**: los recursos se asocian al perímetro. Entre miembros del mismo perímetro el
  tráfico se permite.
- **Reglas de acceso**: permiten entrada desde rangos de IP o suscripciones, y salida hacia
  FQDN concretos. Lo demás se niega.
- **Modos de cada asociación**:

| Modo | Qué hace | Cuándo |
|---|---|---|
| **Transition** (antes *Learning*) | Modo por defecto de cada asociación: registra el acceso y no corta lo que hoy funciona | Para conocer los patrones de acceso antes de cerrar |
| **Enforced** | Niega todo salvo el tráfico dentro del perímetro y lo que permite una regla | Cuando las reglas ya cubren el uso real |

- **Logs de acceso**: se envían por diagnostic settings a Log Analytics o Storage.
- **Estado**: disponible en todas las regiones públicas. La lista de servicios incorporados y su
  estado (GA o preview) cambia; está en la sección *Onboarded private link resources* de la doc.
- **Límite**: no admite tráfico por [Service endpoint](service-endpoint.md).

## De Transition a Enforced en dos semanas

Un Key Vault y una cuenta de Storage de un proyecto se asocian a un perímetro en modo Transition
durante dos semanas. Los logs muestran que solo un pipeline externo entra desde un rango fijo; se
agrega esa regla de entrada y se pasa a Enforced.

## Perímetro y private endpoint

El [Private endpoint](private-endpoint.md), que da una IP privada dentro de una VNet para llegar a un recurso. El
perímetro no mete al recurso en ninguna red: controla su acceso público. Se pueden usar juntos.
