---
resumen: >-
  Integración y entrega es la parte de DevOps que lleva cada cambio de la rama principal a un
  artefacto listo para producción con un pipeline automático: integración continua, entrega
  continua y despliegue continuo, y las herramientas que los implementan.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Integración y entrega

Integración y entrega es la parte de DevOps que lleva cada cambio de la rama principal a un
artefacto listo para producción con un pipeline automático: integración continua, entrega
continua y despliegue continuo, y las herramientas que los implementan.

Dentro de [DevOps](../devops.md), recibe de [Ramas y versiones](../Ramas-y-versiones/ramas-y-versiones.md)
una rama principal integrada seguido y le entrega a [Despliegue](../Despliegue/despliegue.md) un
artefacto que no cambia. Los controles de [DevSecOps](../DevSecOps/devsecops.md) corren como
etapas de su pipeline.

## Tres prácticas encadenadas

La integración continua integra los cambios de cada persona a la rama principal al menos una vez
por día, con build y pruebas automáticas. La entrega continua deja cada cambio validado listo para
producción; el paso final sigue siendo una decisión manual. El despliegue continuo saca esa
decisión: cada cambio que pasa todas las verificaciones llega solo a producción. Cada una requiere
la anterior, no al revés.

## El pipeline que las sostiene

Un evento del repositorio dispara etapas que van de lo más barato a lo más caro, y cada etapa es
un gate: si falla, las siguientes no corren. Se construye una sola vez, y el mismo artefacto,
identificado por el commit y nunca por "latest", avanza de entorno en entorno. Cuando muchos repos
necesitan el mismo pipeline, una definición central y versionada evita copiarlo en cada uno.

## Qué hay adentro de integración y entrega

- [Integración continua](integracion-continua.md) — integrar a la rama principal varias veces por día, con build y pruebas automáticas.
- [Entrega continua](entrega-continua.md) — cada cambio validado queda listo para producción; el paso final es manual.
- [Despliegue continuo](despliegue-continuo.md) — cada cambio que pasa las verificaciones llega solo a producción.
- [Pipeline de CI/CD](pipeline-de-ci-cd.md) — la secuencia de etapas que disparan los eventos de Git.
- [Pipeline reutilizable](pipeline-reutilizable.md) — una definición central y versionada que muchos repos invocan.

Las herramientas que implementan el pipeline:

- [GitHub Actions](GitHub-Actions/github-actions.md) — workflows, jobs, runners y actions, con sus notas de reutilización, environments, artifacts y secrets.
- [Tekton](tekton.md) — el framework de CI/CD nativo de Kubernetes: Tasks, Pipelines y Triggers.
- [Disparar Tekton desde Azure DevOps](disparar-tekton-desde-azure-devops.md) — pasos para lanzar un PipelineRun con cada push o PR de Azure Repos.
- [Desplegar en AKS con Azure Pipelines](desplegar-en-aks-con-azure-pipelines.md) — pasos para construir, subir a ACR y desplegar en AKS.
