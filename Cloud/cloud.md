---
tipo: mapa
resumen: >-
  Mapa del Tema Cloud: Azure (gobernanza, redes, cómputo, datos, mensajería, observabilidad,
  HA/DR y diseño de soluciones) y FinOps; sirve de consulta y, para redes, como camino de
  aprendizaje.
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# Cloud

Mapa del Tema Cloud: Azure (gobernanza, redes, cómputo, datos, mensajería, observabilidad,
HA/DR y diseño de soluciones) y FinOps; sirve de consulta y, para redes, como camino de
aprendizaje.

Para aprender redes en Azure en orden: [Redes en Azure para quien ya sabe redes](recorrido-redes-en-azure.md).

## Gobernanza e identidad

- [Azure landing zone](azure-landing-zone.md) — qué trae la base común de un entorno de Azure y cómo se reparte entre plataforma y proyectos.
- [Azure Policy](azure-policy.md) — cómo se hacen cumplir reglas sobre los recursos (negar, auditar, desplegar lo que falta).
- [Identidad y acceso en Azure](identidad-y-acceso-en-azure.md) — Entra ID, RBAC, PIM, managed identities, OIDC y Key Vault.
- [Landing zone con Terraform](landing-zone-con-terraform.md) — cómo se despliega una landing zone en stacks de Terraform con estado propio.

## Redes

- [Virtual Network (Azure)](virtual-network-azure.md) — la red privada de Azure, sus subredes y la salida a internet; se lee primero.
- [Network security group](network-security-group.md) — el filtro por IP y puerto de cada subred o NIC.
- [Ruteo en Azure](ruteo-en-azure.md) — rutas de sistema, UDR y BGP, y cómo forzar el paso por un firewall.
- [VNet peering](vnet-peering.md) — cómo se unen dos VNets y por qué no es transitivo.
- [Topología hub-and-spoke](topologia-hub-and-spoke.md) — lo compartido en el hub y cada proyecto aislado en su spoke.
- [Conectividad híbrida en Azure](conectividad-hibrida-azure.md) — VPN y ExpressRoute para unir la red propia con Azure.
- [NAT Gateway](nat-gateway.md) — IP de salida fija y sin agotamiento de SNAT.
- [Balanceadores de carga en Azure](balanceadores-de-carga-azure.md) — Front Door, Application Gateway y Load Balancer: cuál para qué.

## Acceso privado a servicios PaaS

- [Private endpoint](private-endpoint.md) — una IP privada para una instancia de un PaaS; la forma recomendada.
- [DNS privado para Private Link](dns-privado-para-private-link.md) — por qué el nombre tiene que resolver a la IP privada y cómo.
- [Service endpoint](service-endpoint.md) — la alternativa sin IP privada, más barata y más limitada.
- [Network security perimeter](network-security-perimeter.md) — una frontera de acceso público alrededor de varios PaaS.

## Cómputo

- [Elección de cómputo en Azure](eleccion-de-computo-en-azure.md) — VM, App Service, Functions, Container Apps o AKS: cuándo cada uno.
- [Máquina virtual (Azure)](maquina-virtual-azure.md) — de qué depende una VM y qué se cobra aparte.
- [Azure Functions](azure-functions.md) — serverless por eventos y qué cambia cada plan de hosting.
- [Durable Functions](durable-functions.md) — flujos con estado sobre Functions y sus patrones.

## Datos, mensajería y operación

- [Almacenamiento y bases de datos en Azure](almacenamiento-y-bases-de-datos-en-azure.md) — Storage, SQL, Cosmos DB, Postgres/MySQL y Redis: qué resuelve cada uno.
- [Mensajería en Azure](mensajeria-en-azure.md) — Service Bus, Event Hubs y Event Grid: en qué se diferencian.
- [Azure Monitor](azure-monitor.md) — métricas, logs, trazas, alertas y el costo de los logs.
- [Alta disponibilidad y DR en Azure](alta-disponibilidad-y-dr-en-azure.md) — zonas, regiones, backup y réplica según RTO y RPO.

## Diseño de soluciones

- [Arquitecturas de referencia en Azure](arquitecturas-de-referencia-en-azure.md) — tres combinaciones probadas de servicios.

## Cómo hacer

- [Verificar la conectividad privada en Azure](verificar-conectividad-privada-en-azure.md) — probar private endpoints, egreso por NAT y aislamiento entre spokes.
- [Diseñar una solución en Azure](disenar-una-solucion-en-azure.md) — responder un diseño de solución paso a paso, p. ej. en una entrevista.

## Fichas

- [Tamaños de VM en Azure](tamanos-de-vm-azure.md) — las familias de tamaño de VM con su uso típico (copiadas con fecha).

## Sub-Mapas

- [FinOps](FinOps/finops.md) — la práctica de FinOps según la FinOps Foundation y cómo bajar el costo en Azure.

## Otros Temas

- [Módulo de Terraform](../Infraestructura/modulo-de-terraform.md), [Estado remoto de Terraform](../Infraestructura/estado-remoto-de-terraform.md) y [Armar un pipeline de Terraform](../Infraestructura/pipeline-de-terraform.md) — la base
  de Terraform que usa la landing zone; viven en Infraestructura.
- [Split-horizon DNS](../Infraestructura/split-horizon-dns.md) — el principio detrás del DNS de Private Link, en Infraestructura.
- [Desplegar en AKS con Azure Pipelines](../DevOps/desplegar-en-aks-con-azure-pipelines.md) — CI/CD hacia AKS, en DevOps.
- [Gobernanza de plataforma](../Platform-Engineering/gobernanza-de-plataforma.md), [Golden path](../Platform-Engineering/golden-path.md) y [Observabilidad](../Platform-Engineering/observabilidad.md) — la mirada de plataforma
  interna, en Platform-Engineering.
