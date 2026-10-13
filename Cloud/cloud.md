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

Para aprender redes en Azure en orden: [[recorrido-redes-en-azure]].

## Gobernanza e identidad

- [[azure-landing-zone]] — qué trae la base común de un entorno de Azure y cómo se reparte entre plataforma y proyectos.
- [[azure-policy]] — cómo se hacen cumplir reglas sobre los recursos (negar, auditar, desplegar lo que falta).
- [[identidad-y-acceso-en-azure]] — Entra ID, RBAC, PIM, managed identities, OIDC y Key Vault.
- [[landing-zone-con-terraform]] — cómo se despliega una landing zone en stacks de Terraform con estado propio.

## Redes

- [[virtual-network-azure]] — la red privada de Azure, sus subredes y la salida a internet; se lee primero.
- [[network-security-group]] — el filtro por IP y puerto de cada subred o NIC.
- [[ruteo-en-azure]] — rutas de sistema, UDR y BGP, y cómo forzar el paso por un firewall.
- [[vnet-peering]] — cómo se unen dos VNets y por qué no es transitivo.
- [[topologia-hub-and-spoke]] — lo compartido en el hub y cada proyecto aislado en su spoke.
- [[conectividad-hibrida-azure]] — VPN y ExpressRoute para unir la red propia con Azure.
- [[nat-gateway]] — IP de salida fija y sin agotamiento de SNAT.
- [[balanceadores-de-carga-azure]] — Front Door, Application Gateway y Load Balancer: cuál para qué.

## Acceso privado a servicios PaaS

- [[private-endpoint]] — una IP privada para una instancia de un PaaS; la forma recomendada.
- [[dns-privado-para-private-link]] — por qué el nombre tiene que resolver a la IP privada y cómo.
- [[service-endpoint]] — la alternativa sin IP privada, más barata y más limitada.
- [[network-security-perimeter]] — una frontera de acceso público alrededor de varios PaaS.

## Cómputo

- [[eleccion-de-computo-en-azure]] — VM, App Service, Functions, Container Apps o AKS: cuándo cada uno.
- [[maquina-virtual-azure]] — de qué depende una VM y qué se cobra aparte.
- [[azure-functions]] — serverless por eventos y qué cambia cada plan de hosting.
- [[durable-functions]] — flujos con estado sobre Functions y sus patrones.

## Datos, mensajería y operación

- [[almacenamiento-y-bases-de-datos-en-azure]] — Storage, SQL, Cosmos DB, Postgres/MySQL y Redis: qué resuelve cada uno.
- [[mensajeria-en-azure]] — Service Bus, Event Hubs y Event Grid: en qué se diferencian.
- [[azure-monitor]] — métricas, logs, trazas, alertas y el costo de los logs.
- [[alta-disponibilidad-y-dr-en-azure]] — zonas, regiones, backup y réplica según RTO y RPO.

## Diseño de soluciones

- [[arquitecturas-de-referencia-en-azure]] — tres combinaciones probadas de servicios.

## Cómo hacer

- [[verificar-conectividad-privada-en-azure]] — probar private endpoints, egreso por NAT y aislamiento entre spokes.
- [[disenar-una-solucion-en-azure]] — responder un diseño de solución paso a paso, p. ej. en una entrevista.

## Fichas

- [[tamanos-de-vm-azure]] — las familias de tamaño de VM con su uso típico (copiadas con fecha).

## Sub-Mapas

- [[finops]] — la práctica de FinOps según la FinOps Foundation y cómo bajar el costo en Azure.

## Otros Temas

- [[modulo-de-terraform]], [[estado-remoto-de-terraform]] y [[pipeline-de-terraform]] — la base
  de Terraform que usa la landing zone; viven en Infraestructura.
- [[split-horizon-dns]] — el principio detrás del DNS de Private Link, en Infraestructura.
- [[desplegar-en-aks-con-azure-pipelines]] — CI/CD hacia AKS, en DevOps.
- [[gobernanza-de-plataforma]], [[golden-path]] y [[observabilidad]] — la mirada de plataforma
  interna, en Platform-Engineering.
