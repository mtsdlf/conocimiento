---
tipo: mapa
resumen: >-
  Mapa del Tema Infraestructura: Terraform, red y despliegue de Kubernetes, certificados y DNS,
  secretos en Git y NetDevOps; el homelab de Matías se documenta en su propio repo.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# Infraestructura

Mapa del Tema Infraestructura: Terraform, red y despliegue de Kubernetes, certificados y DNS,
secretos en Git y NetDevOps; el homelab de Matías se documenta en su propio repo.

## Terraform

- [Módulo de Terraform](modulo-de-terraform.md) — qué es un módulo y cómo se diseña para que otro equipo lo use sin leerlo por dentro; es la base del grupo.
- [Estado remoto de Terraform](estado-remoto-de-terraform.md) — qué guarda el estado y por qué un equipo lo pone en un backend remoto con bloqueo.
- [Organizar entornos en Terraform](organizar-entornos-en-terraform.md) — cuándo separar dev, test y prod en carpetas y cuándo alcanzan los workspaces.
- [Secretos en Terraform](secretos-en-terraform.md) — dónde viven los secretos y qué hace (y qué no) `sensitive`.
- [Armar un pipeline de Terraform](pipeline-de-terraform.md) — los pasos de CI/CD desde `fmt` hasta un `apply` sobre un plan guardado.
- [Adoptar Terraform en un equipo](adoptar-terraform-en-un-equipo.md) — en qué orden un equipo pasa a Terraform, de los estándares al policy-as-code.

## Kubernetes: red y despliegue

- [Cilium](cilium.md) — qué es el CNI basado en eBPF, el reemplazo de kube-proxy y los modos de ruteo.
- [Default-deny de red en Kubernetes](default-deny-de-red-en-kubernetes.md) — qué implica prohibir todo el tráfico de un pod salvo lo permitido, y dónde quedan huecos.
- [Desplegar Kubernetes con Kubespray](desplegar-kubernetes-con-kubespray.md) — los pasos para instalar un clúster con Kubespray y Ansible.
- [Variables de Cilium en Kubespray](kubespray-variables-cilium.md) — las variables exactas de Kubespray para Cilium, copiadas con fecha.

## Certificados y DNS

- [Desafío ACME HTTP-01](desafio-acme-http-01.md) — cómo prueba un dominio el desafío HTTP-01 y cuándo conviene DNS-01.
- [Split-horizon DNS](split-horizon-dns.md) — por qué un mismo nombre resuelve distinto en la LAN y en internet, y su punto único de falla.

## Secretos en Git

- [SOPS](sops.md) — cómo cifrar los valores de un archivo de configuración para guardarlo en Git y que GitOps lo descifre al aplicar.

## NetDevOps

- [NetDevOps](netdevops.md) — qué cambia al tratar la configuración de red como código con pruebas y CI/CD.
- [Herramientas de NetDevOps](herramientas-de-netdevops.md) — qué herramienta cubre cada función, con enlace a su documentación.

## Homelab

El clúster `home-k8` de Matías se documenta en su repo, no en este Vault: runbooks, lessons, ADRs
y la capability matrix están en [github.com/mtsdlf/home-k8](https://github.com/mtsdlf/home-k8)
(carpeta `docs/`). El Vault guarda el concepto general; el repo, cómo está armado y operado ese
sistema. Algunas notas de arriba (default-deny, split-horizon, SOPS) lo usan como ejemplo.

## Otros Temas

- [Observabilidad](../Platform-Engineering/observabilidad.md) — monitoreo, logs y alertas viven en Platform-Engineering.
- [GitOps](../DevOps/gitops.md) — GitOps, la base de SOPS y de NetDevOps, vive en DevOps.
