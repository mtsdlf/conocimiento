---
tipo: concepto
resumen: >-
  Una máquina virtual de Azure es cómputo IaaS con control total del sistema operativo; depende de
  una VNet, una NIC, una IP, un NSG, discos y a veces una licencia, y varias de esas piezas se cobran aparte.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Virtual machines in Azure: https://learn.microsoft.com/en-us/azure/virtual-machines/overview"
  - "Microsoft Learn, Managed disks overview: https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview"
  - "Microsoft Learn, Availability options for Azure VMs: https://learn.microsoft.com/en-us/azure/virtual-machines/availability"
  - "Microsoft Learn, Orchestration modes for VM Scale Sets: https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes"
  - "Microsoft Learn, Azure Update Manager: https://learn.microsoft.com/en-us/azure/update-manager/workflow-update-manager"
  - "Microsoft Learn, Quickstart: create a Linux VM in the portal: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección AZURE IAAS)"
aliases: [VM, máquina virtual, virtual machine, Azure VM, VMSS, VM Scale Set]
parte_de: []
requiere: [virtual-network-azure]
relacionado: []
---

# Máquina virtual (Azure)

Una máquina virtual de Azure es cómputo IaaS con control total del sistema operativo; depende de
una VNet, una NIC, una IP, un NSG, discos y a veces una licencia, y varias de esas piezas se cobran aparte.

## Por qué importa

Es la opción para lo que no entra en un servicio administrado: software que pide un SO concreto,
drivers o licencias. El precio de la VM no es el costo total: los discos, las IPs públicas y la
licencia se suman (ver [Elección de cómputo en Azure](eleccion-de-computo-en-azure.md)).

## Cómo funciona

| Pieza | Para qué | Costo |
|---|---|---|
| [Virtual Network (Azure)](virtual-network-azure.md) | Que la VM hable con otros recursos | Sin costo propio |
| NIC | La conexión a la subred; el tamaño de la VM limita cuántas | Sin cargo |
| IP privada y, si hace falta, pública | Comunicación interna y externa | La pública se cobra |
| [Network security group](network-security-group.md) | Qué puertos se abren (22 sí, 80 no) | Sin cargo |
| Disco de SO y discos de datos | El sistema y los datos | Por tamaño y tipo de disco |
| Licencia del SO (Windows, a veces) | Ejecutar el SO | Por núcleos; baja con Azure Hybrid Benefit |

- **Datos en un disco aparte**: si la VM falla, el disco de datos se desconecta y se conecta a otra.
  El disco temporal local no se cobra, pero se pierde al redesplegar o desasignar la VM.
- **Cambiar de VNet** no se puede: se borra la VM, se conservan los discos y se crea otra en la
  VNet nueva.
- **Disponibilidad**: distribuir las VMs en zonas da el SLA más alto (99,99 %). Para varias VMs
  iguales, Microsoft recomienda VM Scale Sets en orquestación *Flexible*, que reparte entre zonas
  o dominios de error. Los availability sets quedan para regiones sin zonas.
- **Operación**: una managed identity en lugar de credenciales en la VM, Azure Update Manager para
  los parches y Azure Monitor Agent para métricas y logs. Para diagnosticar, la consola serie, el
  diagnóstico de arranque y Run Command.

## Ejemplo

Una VM Linux de prueba en un spoke, sin IP pública: NIC en la subred `test`, NSG que solo permite
SSH desde la subred de Bastion, disco de SO estándar y la salida a internet por la NAT Gateway de
la subred. Se cobran la VM, el disco y el tráfico; no hay IP pública que pagar.

## No confundir con

El tamaño de la VM: la familia y la serie definen CPU, memoria y discos; están en
[Tamaños de VM en Azure](tamanos-de-vm-azure.md).

## Relaciones

- Requiere: [Virtual Network (Azure)](virtual-network-azure.md) — la VM vive en una subred.
- Detallada en: [Tamaños de VM en Azure](tamanos-de-vm-azure.md) — qué familia elegir.
- La compara: [Elección de cómputo en Azure](eleccion-de-computo-en-azure.md) — cuándo una VM y cuándo algo más administrado.
