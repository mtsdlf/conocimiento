---
tipo: concepto
resumen: >-
  Un network security group (NSG) filtra el tráfico entrante y saliente de una subred o una NIC con
  reglas por origen, destino, puerto y protocolo; los application security groups (ASG) agrupan
  VMs para usarlas como origen o destino de esas reglas.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Network security groups: https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview"
  - "Microsoft Learn, Application security groups: https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups"
  - "Microsoft Learn, NSG flow logs overview (retiro): https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-overview"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección AZURE NETWORKING)"
aliases: [NSG, network security group, grupo de seguridad de red, ASG, application security group]
parte_de: []
requiere: [virtual-network-azure]
relacionado: []
---

# Network security group

Un network security group (NSG) filtra el tráfico entrante y saliente de una subred o una NIC con
reglas por origen, destino, puerto y protocolo; los application security groups (ASG) agrupan
VMs para usarlas como origen o destino de esas reglas.

## Por qué importa

Dentro de una [[virtual-network-azure]], por defecto todo habla con todo. El NSG es el primer
filtro y no tiene costo: separa la subred de aplicación de la de datos o deja entrar solo el
puerto 443 desde un balanceador.

## Cómo funciona

- **Reglas**: cada regla mira la 5-tupla (IP y puerto de origen, IP y puerto de destino,
  protocolo) y permite o niega. Se evalúan por prioridad, de 100 a 4096; la de número más bajo
  gana y corta la evaluación.
- **Con estado**: si una regla deja salir una conexión, la respuesta entra sin otra regla.
- **Reglas por defecto** (prioridad 65000 en adelante): permiten el tráfico dentro de la VNet y
  desde el balanceador de Azure, dejan salir a internet y niegan todo lo demás.
- **Dónde se asocia**: a una subred, a una NIC o a ambas. Si están las dos, el tráfico tiene que
  pasar las dos. Una práctica común es filtrar en la subred y dejar la NIC sin NSG.
- **Origen y destino**: una IP, un rango, una *service tag* (p. ej. `Storage`, `AzureCloud`) o un
  ASG. Con ASG, la regla dice "web puede hablar con datos en el 5432" sin listar IPs; todas las
  NICs de un ASG tienen que estar en la misma VNet.
- **Diagnóstico**: las *effective security rules* de una NIC muestran el resultado combinado. Los
  flow logs registran el tráfico real; los de NSG se retiran el 30 de septiembre de 2027 y ya no
  se pueden crear nuevos: se usan los flow logs de VNet.

## Ejemplo

La subred de datos tiene un NSG con dos reglas de entrada: prioridad 100, permitir TCP 5432 desde
el ASG `asg-web`; prioridad 4000, negar todo desde la service tag `VirtualNetwork`. La segunda hace
falta porque la regla por defecto deja pasar cualquier tráfico de la misma VNet. Una VM nueva del
frontend entra al ASG y ya puede llegar a la base, sin tocar el NSG.

## No confundir con

Un firewall (Azure Firewall o un NVA): inspecciona en capa 7, filtra por FQDN y centraliza el
egreso de varias VNets. El NSG filtra por IP y puerto en cada subred. Se usan juntos.

## Relaciones

- Requiere: [[virtual-network-azure]] — filtra tráfico entre sus subredes.
- La usa: [[verificar-conectividad-privada-en-azure]] — revisar las reglas efectivas es un paso del
  diagnóstico.
