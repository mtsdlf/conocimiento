---
tipo: concepto
resumen: >-
  En Azure, la alta disponibilidad se logra repartiendo en zonas de una región y la recuperación
  ante desastres (DR) copiando a otra región; cuánto se invierte en cada una lo fijan el RTO y el
  RPO que pide el negocio.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Azure reliability documentation: https://learn.microsoft.com/en-us/azure/reliability/"
  - "Microsoft Learn, Azure region pairs and nonpaired regions: https://learn.microsoft.com/en-us/azure/reliability/regions-paired"
  - "Microsoft Learn, What is Azure Backup?: https://learn.microsoft.com/en-us/azure/backup/backup-overview"
  - "Microsoft Learn, About Site Recovery: https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview"
  - "Archivo/Cloud/azure-referencia-framework.md (original, HA/DR y HA/DR para SQL)"
aliases: [HA, DR, alta disponibilidad, disaster recovery, RTO, RPO, zonas de disponibilidad]
parte_de: []
requiere: []
relacionado: []
---

# Alta disponibilidad y DR en Azure

En Azure, la alta disponibilidad se logra repartiendo en zonas de una región y la recuperación
ante desastres (DR) copiando a otra región; cuánto se invierte en cada una lo fijan el RTO y el
RPO que pide el negocio.

## Por qué importa

Cada nivel de resiliencia cuesta: duplicar en otra región puede duplicar la factura. Sin un
**RTO** (cuánto puede estar caído el servicio) y un **RPO** (cuántos datos se pueden perder) acordados, se
gasta de más o se descubre en el incidente que no alcanzaba.

## Cómo funciona

- **Zonas de disponibilidad**: datacenters separados dentro de una región. Un servicio
  *zone-redundant* reparte solo; uno *zonal* se fija a una zona y la redundancia se arma a mano.
  Protegen contra la caída de un datacenter.
- **Regiones**: protegen contra la caída de una región entera. Muchas regiones tienen pareja
  (actualizaciones escalonadas y prioridad de recuperación), pero varias nuevas no la tienen y se
  apoyan solo en zonas; la región de DR se elige igual.
- **Azure Backup**: copias con retención, borrado suave e inmutabilidad, en un Recovery Services
  vault o un Backup vault. Protege contra errores y ransomware, no da continuidad.
- **Site Recovery**: replica VMs a otra región o desde la red propia a Azure y orquesta el
  failover y el failback, con pruebas que no cortan producción.

**La réplica de cada servicio de datos**:

| Servicio | HA en la región | DR a otra región |
|---|---|---|
| Azure SQL | Base con redundancia de zona | Failover groups |
| Cosmos DB | Redundancia de zona | Escrituras o lecturas en varias regiones |
| Storage | ZRS | GZRS o GRS |
| VMs | Scale set en zonas | Site Recovery |

Un plan de DR que nunca se probó no cuenta: el failover se ensaya con fecha.

## Ejemplo

Un sistema de turnos acepta 4 horas caído y 15 minutos de datos perdidos. Va en una región con
App Service y Azure SQL zone-redundant; un failover group replica la base a otra región y el
cómputo se recrea allá con IaC en menos de una hora, dentro de las 4 horas aceptadas. Una vez por trimestre se prueba el failover.

## No confundir con

El backup: recupera datos borrados o corruptos, pero restaurar puede llevar horas. La DR mantiene
una copia viva lista para atender.

## Relaciones

- Usa: [Almacenamiento y bases de datos en Azure](almacenamiento-y-bases-de-datos-en-azure.md) — las opciones de réplica de cada servicio.
- La usa: [Diseñar una solución en Azure](disenar-una-solucion-en-azure.md) — el paso de HA y DR.
