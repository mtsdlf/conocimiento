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

- [[modulo-de-terraform]] — qué es un módulo y cómo se diseña para que otro equipo lo use sin leerlo por dentro; es la base del grupo.
- [[estado-remoto-de-terraform]] — qué guarda el estado y por qué un equipo lo pone en un backend remoto con bloqueo.
- [[organizar-entornos-en-terraform]] — cuándo separar dev, test y prod en carpetas y cuándo alcanzan los workspaces.
- [[secretos-en-terraform]] — dónde viven los secretos y qué hace (y qué no) `sensitive`.
- [[pipeline-de-terraform]] — los pasos de CI/CD desde `fmt` hasta un `apply` sobre un plan guardado.
- [[adoptar-terraform-en-un-equipo]] — en qué orden un equipo pasa a Terraform, de los estándares al policy-as-code.

## Kubernetes: red y despliegue

- [[cilium]] — qué es el CNI basado en eBPF, el reemplazo de kube-proxy y los modos de ruteo.
- [[default-deny-de-red-en-kubernetes]] — qué implica prohibir todo el tráfico de un pod salvo lo permitido, y dónde quedan huecos.
- [[desplegar-kubernetes-con-kubespray]] — los pasos para instalar un clúster con Kubespray y Ansible.
- [[kubespray-variables-cilium]] — las variables exactas de Kubespray para Cilium, copiadas con fecha.

## Certificados y DNS

- [[desafio-acme-http-01]] — cómo prueba un dominio el desafío HTTP-01 y cuándo conviene DNS-01.
- [[split-horizon-dns]] — por qué un mismo nombre resuelve distinto en la LAN y en internet, y su punto único de falla.

## Secretos en Git

- [[sops]] — cómo cifrar los valores de un archivo de configuración para guardarlo en Git y que GitOps lo descifre al aplicar.

## NetDevOps

- [[netdevops]] — qué cambia al tratar la configuración de red como código con pruebas y CI/CD.
- [[herramientas-de-netdevops]] — qué herramienta cubre cada función, con enlace a su documentación.

## Homelab

El clúster `home-k8` de Matías se documenta en su repo, no en este Vault: runbooks, lessons, ADRs
y la capability matrix están en [github.com/mtsdlf/home-k8](https://github.com/mtsdlf/home-k8)
(carpeta `docs/`). El Vault guarda el concepto general; el repo, cómo está armado y operado ese
sistema. Algunas notas de arriba (default-deny, split-horizon, SOPS) lo usan como ejemplo.

## Otros Temas

- [[observabilidad]] — monitoreo, logs y alertas viven en Platform-Engineering.
- [[gitops]] — GitOps, la base de SOPS y de NetDevOps, vive en DevOps.
