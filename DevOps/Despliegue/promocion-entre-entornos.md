---
resumen: >-
  La promoción entre entornos en GitOps es cambiar el estado declarado de cada entorno (por
  carpeta o por rama) con un commit, revisado en un PR para los entornos protegidos. Ejemplo: el
  CI actualiza la imagen en `values.yaml` y Argo CD sincroniza.
estado: borrador
estabilidad: estable
fuentes:
  - "Kostis Kapelonis, Stop Using Branches for Deploying to Different GitOps Environments (2021): https://octopus.com/blog/stop-using-branches-deploying-different-gitops-environments"
  - "Argo CD, Best Practices: https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/"
  - "Argo CD Image Updater: https://argocd-image-updater.readthedocs.io/en/stable/"
  - "Archivo/DevOps/gitops-principios.md (original, texto generado con IA)"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-advanced-collaboration.md (original, texto generado con IA)"
aliases: [Promoción de entornos, Environment promotion]
creado: 2026-10-03
revisado:
---

# Promoción entre entornos

La promoción entre entornos en GitOps es cambiar el estado declarado de cada entorno (por
carpeta o por rama) con un commit, revisado en un PR para los entornos protegidos. Ejemplo: el
CI actualiza la imagen en `values.yaml` y Argo CD sincroniza.

## Promover es editar archivos en Git

En GitOps nadie despliega con un comando: promover una versión de desarrollo a staging y de
staging a producción es editar archivos en Git. Cómo se ordenan esos archivos decide si la
promoción es un cambio chico y revisable o un merge lleno de conflictos.

## Carpeta o rama por entorno

Hay dos formas de representar los entornos en el repositorio de configuración:

- **Una carpeta por entorno** (`envs/dev`, `envs/staging`, `envs/prod`), con una base común y
  overlays de Kustomize o archivos de valores de Helm por entorno. Promover es copiar la versión
  de una carpeta a la siguiente en un PR. Es la misma separación que usa la infraestructura
  ([organizar entornos en Terraform](../../Infraestructura/Aprovisionamiento/organizar-entornos-en-terraform.md)),
  aplicada a los manifiestos de la aplicación.
- **Una rama por entorno** (`dev`, `staging`, `prod`). Promover es mergear una rama en otra.

Kostis Kapelonis (2021) desaconseja las ramas por entorno: el merge arrastra cambios que no se
querían promover (por ejemplo, la cantidad de réplicas), los arreglos hechos en producción no
vuelven a los entornos anteriores y decenas de ramas de larga vida no escalan. Helm y Kustomize
ya modelan los entornos con archivos y carpetas, no con ramas. Se infiere que la carpeta por
entorno es la opción por defecto, salvo una razón concreta para ramas.

La protección del entorno sale de los permisos del repositorio: Argo CD recomienda que quien
puede cambiar el código no sea necesariamente quien puede escribir la configuración de
producción. Las reglas de esos permisos están en [Gobernanza de repositorios](../Repositorios/gobernanza-de-repositorios.md).

## `pagos:1.4.0` de dev a producción

1. El pipeline de CI construye la imagen `pagos:1.4.0` y la sube al registry.
2. El mismo pipeline hace un commit directo, sin PR, en el repositorio de configuración que
   cambia `image.tag` en `envs/dev/values.yaml`. Dev no está protegido, así que no hace falta
   revisión.
3. Argo CD detecta el commit y despliega en dev.
4. Para staging y producción, alguien abre un PR que cambia el mismo valor en
   `envs/staging/values.yaml` o `envs/prod/values.yaml`; al aprobarse, Argo CD despliega allí.

Argo CD Image Updater automatiza el paso 2: vigila el registry y escribe la nueva versión en Git.

## Promoción no es branching del código

**Estrategia de branching** del código: decide cómo se integra el código de la aplicación
([Estrategia de branching](../Ramas-y-versiones/estrategia-de-branching.md)). La promoción decide qué versión ya construida corre en cada
entorno, y vive en otro repositorio.

## Ver también

- [GitOps](gitops.md) — es la forma de desplegar en un modelo GitOps.
