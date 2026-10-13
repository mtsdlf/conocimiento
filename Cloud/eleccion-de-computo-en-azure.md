---
tipo: concepto
resumen: >-
  En Azure se elige entre VMs, App Service, Functions, Container Apps y AKS según cuánto control
  hace falta, cuánta operación se acepta y cómo escala la carga; la regla es usar el servicio más
  administrado que cumpla los requisitos.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Choose an Azure compute service: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree"
  - "Microsoft Learn, Azure Container Apps overview: https://learn.microsoft.com/en-us/azure/container-apps/overview"
  - "Microsoft Learn, App Service networking features: https://learn.microsoft.com/en-us/azure/app-service/networking-features"
  - "Microsoft Learn, Azure Spring Apps retirement announcement: https://learn.microsoft.com/en-us/azure/spring-apps/basic-standard/retirement-announcement"
  - "Microsoft Learn, Microsoft Entra Workload ID with AKS: https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Compute, mini-guía y gotchas)"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección AZURE PAAS, App Service)"
aliases: [elegir cómputo en Azure, App Service, Container Apps, ACA, AKS, compute decision tree]
parte_de: []
requiere: []
relacionado: []
---

# Elección de cómputo en Azure

En Azure se elige entre VMs, App Service, Functions, Container Apps y AKS según cuánto control
hace falta, cuánta operación se acepta y cómo escala la carga; la regla es usar el servicio más
administrado que cumpla los requisitos.

## Por qué importa

Cada escalón hacia más control suma trabajo: parches del sistema operativo, actualizaciones del
clúster, red, escalado. Elegir AKS para una API simple paga ese trabajo sin necesitarlo; elegir
Functions para un proceso de horas choca con sus límites.

## Cómo funciona

| Servicio | Se elige cuando | Lo que hay que saber |
|---|---|---|
| **[[maquina-virtual-azure]]** (y VM Scale Sets) | Hace falta el SO entero: drivers, licencias, software legacy | Se opera todo: parches, backup, escalado |
| **App Service** | Una web o API HTTP, sin querer administrar SO | Slots para staging y swap (desde el plan Standard); la integración con VNet es solo de salida, la entrada privada es con private endpoint |
| **[[azure-functions]]** | Código chico disparado por eventos, con picos impredecibles | El plan decide cold start, escala a cero y acceso a la VNet |
| **Container Apps** | Contenedores y eventos sin administrar Kubernetes | Escala con KEDA, Dapr, revisiones con reparto de tráfico, jobs; escala a cero salvo con reglas de CPU o memoria |
| **AKS** | Hace falta Kubernetes completo: operadores, malla de servicios, control fino | Más operación: actualizaciones, red, seguridad del clúster |

**Para AKS**: la identidad de los pods es Entra Workload ID (reemplaza a pod identity) y la red
recomendada es Azure CNI con Cilium. Kubenet se retira el 31 de marzo de 2028.

**Retirados o por retirarse**: Azure Spring Apps no acepta clientes nuevos desde marzo de 2025 y
se retira el 31 de marzo de 2028; Microsoft propone Container Apps o AKS.

## Ejemplo

Un equipo tiene una API REST, un worker que procesa una cola y un sistema contable que solo corre
en Windows Server con una licencia vieja. La API va a App Service con slots, el worker a Container
Apps escalando por largo de cola (a cero de noche) y el contable a una VM.

## No confundir con

El plan de hosting de Functions o el workload profile de Container Apps: son decisiones dentro de
un servicio ya elegido, no entre servicios.

## Relaciones

- Detallada en: [[maquina-virtual-azure]] y [[azure-functions]] — los dos extremos de control.
- La usa: [[disenar-una-solucion-en-azure]] — el paso de elegir cómputo.
- En otro Tema: [[desplegar-en-aks-con-azure-pipelines]] — cómo llega una imagen a AKS.
