---
resumen: >-
  Cómputo es la parte de Cloud donde corre el código: VMs, App Service, Functions, Container Apps y
  AKS, ordenados por cuánto control dan y cuánta operación piden.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Cómputo

Cómputo es la parte de Cloud donde corre el código: VMs, App Service, Functions, Container Apps y
AKS, ordenados por cuánto control dan y cuánta operación piden.

Dentro de [Cloud](../cloud.md), el cómputo vive en una subred de [Redes](../Redes/redes.md), entra a
los [datos operacionales](../Datos-operacionales/datos-operacionales.md) con su managed identity,
se dispara o se desacopla con la [mensajería](../Mensajeria/mensajeria.md), y lo observa y replica
[Operación](../Operacion/operacion.md). Es donde más pesan las palancas de [FinOps](../FinOps/finops.md):
el tamaño, las reservas, Spot y el escalado a cero.

## El servicio más administrado que cumpla

La regla es usar el servicio más administrado que cumpla los requisitos. Cada escalón hacia más
control suma trabajo: parches del sistema operativo, actualizaciones del clúster, red y escalado.
En un extremo está la VM, con el SO entero y todo por operar; en el otro, Functions, que corre
código chico disparado por eventos y cuyo plan de hosting decide si escala a cero, si tiene cold
start y si entra a una VNet. App Service, Container Apps y AKS quedan en el medio.

## Lo que se cobra aparte

El precio de una VM no es su costo total: los discos, las IPs públicas y la licencia se suman, y
su tamaño (la familia y la serie) define CPU, memoria y discos. En Functions, el plan cambia el
costo y el comportamiento más que el código.

## Qué hay adentro del cómputo

- [Elección de cómputo en Azure](eleccion-de-computo-en-azure.md) — VM, App Service, Functions, Container Apps o AKS: cuándo cada uno. Leerla primero.
- [Máquina virtual (Azure)](maquina-virtual-azure.md) — de qué depende una VM y qué se cobra aparte.
- [Tamaños de VM en Azure](tamanos-de-vm-azure.md) — ficha con las familias de tamaño y su uso típico, copiadas el 2026-10-03.
- [Azure Functions](azure-functions.md) — serverless por eventos y qué cambia cada plan de hosting.
- [Durable Functions](durable-functions.md) — flujos con estado sobre Functions y sus patrones.
