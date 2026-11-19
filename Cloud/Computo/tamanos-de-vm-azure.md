---
resumen: >-
  Las familias de tamaño de VM de Azure, agrupadas por tipo de carga, con su uso típico; copiadas
  de Microsoft Learn el 2026-10-03, con enlace a la lista oficial de series.
estado: borrador
estabilidad: volatil
fuentes:
  - "Microsoft Learn, Sizes for virtual machines in Azure: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview"
  - "Microsoft Learn, B-family (burstable): https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/b-family"
  - "Microsoft Learn, NP-family (retiro): https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/fpga-accelerated/np-family"
  - "Microsoft Learn, Azure virtual machine sizes naming conventions: https://learn.microsoft.com/en-us/azure/virtual-machines/vm-naming-conventions"
aliases: [tamaños de VM, VM sizes, familias de VM, burstable VM, serie B]
creado: 2026-10-03
revisado:
---

# Tamaños de VM en Azure

Las familias de tamaño de VM de Azure, agrupadas por tipo de carga, con su uso típico; copiadas
de Microsoft Learn el 2026-10-03, con enlace a la lista oficial de series.

## La lista oficial de series

[Sizes for virtual machines in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview):
la lista de familias y de cada serie (Dsv6, Fasv7…), que cambia con cada generación de hardware.
Para elegir una serie concreta, se consulta ahí. Detalla qué tamaño darle a una
[Máquina virtual (Azure)](maquina-virtual-azure.md).

## Familias por tipo de carga

Copiados el 2026-10-03.

| Tipo | Familias | Uso típico |
|---|---|---|
| Propósito general | A, B, D, DC | Balance CPU/memoria: desarrollo, bases chicas y medianas, web de tráfico bajo o medio |
| Optimizado para cómputo | F, FX | Mucha CPU por GB: web de tráfico medio, appliances de red, procesos batch |
| Optimizado para memoria | E, Eb, EC, M | Mucha memoria por CPU: bases relacionales, caches grandes, analítica en memoria |
| Optimizado para almacenamiento | L | Alto throughput de disco: big data, bases SQL y NoSQL, data warehouse |
| GPU | NC, ND, NG, NV | Cómputo intensivo, entrenamiento e inferencia, escritorios virtuales |
| FPGA | NP | Inferencia, transcodificación de video; se retira el 31 de mayo de 2027 |
| HPC | HB, HC, HX | Simulación, dinámica de fluidos; HC se retira el 31 de mayo de 2027 |

- **Familia B (burstable)**: acumula créditos de CPU mientras está por debajo de su línea base y
  los gasta en picos. Sirve para cargas que pasan la mayor parte del tiempo en reposo; no admite
  Spot.
- **Letras en el nombre de la serie**: `a` es AMD, `p` es ARM, `d` es disco temporal local, `s`
  admite discos premium, `l` es poca memoria por vCPU.
