---
resumen: >-
  La infraestructura como código es describir servidores, redes y servicios en archivos
  versionados que una herramienta aplica de forma repetible e idempotente, en vez de
  configurarlos a mano.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, InfrastructureAsCode: https://martinfowler.com/bliki/InfrastructureAsCode.html"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
aliases: [Infrastructure as code, IaC]
creado: 2026-10-03
revisado:
---

# Infraestructura como código

La infraestructura como código es describir servidores, redes y servicios en archivos
versionados que una herramienta aplica de forma repetible e idempotente, en vez de
configurarlos a mano.

## Por qué no configurar a mano

Un servidor configurado a mano no se puede reproducir, nadie sabe qué tiene y cada entorno
termina distinto del otro. Con la infraestructura en código, crear un entorno nuevo es correr
una herramienta, cada cambio pasa por revisión y el historial del repositorio dice quién cambió
qué y cuándo.

## Prácticas, propiedades y herramientas

Fowler la define como manejar la infraestructura con código fuente "que se trata como cualquier
sistema de software", y lista sus prácticas: archivos de definición en lugar de cambios
manuales, control de versiones, pruebas continuas, cambios chicos y despliegues sin corte.

Tres propiedades que conviene distinguir:

- **Declarativa o imperativa**: la declarativa describe el estado final y la herramienta calcula
  los pasos; la imperativa lista los pasos.
- **Idempotente**: aplicar dos veces la misma definición no cambia nada la segunda vez.
- **Inmutable**: un recurso que cambia se reemplaza por uno nuevo en vez de modificarse.

Las herramientas se agrupan por categoría: aprovisionamiento (Terraform, Pulumi), configuración
(Ansible, Puppet, Chef), imágenes (Dockerfile) y orquestación (manifiestos de Kubernetes, Helm).

En el [Pipeline de CI/CD](../Integracion-y-entrega/pipeline-de-ci-cd.md), un PR corre el formato y el plan (qué cambiaría) como verificación;
el merge a la rama principal aplica el cambio con una cuenta de servicio del pipeline, no la de una persona. Los entornos
se modelan como carpetas con diferencias chicas entre sí (overlays). Una tarea periódica compara
la infraestructura real con el código y avisa el **drift**; si además lo corrige sola, es
[GitOps](gitops.md).

## Un entorno de QA copiado de staging

Un equipo necesita un entorno de pruebas igual a producción. En vez de pedir tickets, copia la
carpeta `envs/staging` a `envs/qa`, cambia el tamaño de las máquinas y abre un PR. El pipeline
muestra el plan; al aprobarse, el entorno queda creado en 20 minutos.

## Infraestructura como código no es un script suelto

Automatizar con scripts sueltos. Un script que crea un servidor no es idempotente ni describe
el estado: correrlo dos veces crea dos servidores. Tampoco es lo mismo que ofrecer la
infraestructura como API a otros equipos, que es lo que hace [Crossplane](../../Platform-Engineering/Plataforma-interna/crossplane.md).
