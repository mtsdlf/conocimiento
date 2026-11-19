---
resumen: >-
  El estado de Terraform registra qué recurso real corresponde a cada bloque de la configuración;
  guardarlo en un backend remoto con bloqueo deja que un equipo lo comparta sin que dos `apply` lo
  corrompan.
estado: borrador
estabilidad: estable
fuentes:
  - "HashiCorp, State: https://developer.hashicorp.com/terraform/language/state"
  - "HashiCorp, Remote state: https://developer.hashicorp.com/terraform/language/state/remote"
  - "HashiCorp, State locking: https://developer.hashicorp.com/terraform/language/state/locking"
  - "HashiCorp, Backend S3: https://developer.hashicorp.com/terraform/language/backend/s3"
  - "HashiCorp, Sensitive data in state: https://developer.hashicorp.com/terraform/language/state/sensitive-data"
  - "Terraform v1.11 changelog: https://github.com/hashicorp/terraform/blob/v1.11/CHANGELOG.md"
aliases: [Terraform state, tfstate, backend de Terraform, state locking]
creado: 2026-10-03
revisado:
---

# Estado remoto de Terraform

El estado de Terraform registra qué recurso real corresponde a cada bloque de la configuración;
guardarlo en un backend remoto con bloqueo deja que un equipo lo comparta sin que dos `apply` lo
corrompan.

## Por qué Terraform necesita el estado

Terraform compara tres cosas en cada `plan`: la configuración, el estado y la infraestructura real.
Sin el estado no sabe que la VM `web` ya existe y es la de tal ID, y propondría crearla de nuevo.
Con el estado en el disco de una persona, según HashiCorp, cada uno tiene que asegurarse de tener
la última versión y de que nadie más esté corriendo Terraform a la vez.

## Backend, bloqueo, secretos y salidas

- **Backend remoto**: se configura con un bloque `backend` dentro de `terraform { }`, y el estado vive en un almacenamiento compartido (HCP Terraform, el servicio de HashiCorp; un bucket S3,
  un container de Azure Storage, GCS). Todo el equipo y el pipeline leen y escriben el mismo.
- **Bloqueo**: antes de una operación que escribe el estado, Terraform toma un lock; si otro
  proceso lo tiene, falla con un error que muestra el ID del lock (o espera, si se pasó
  `-lock-timeout`). No todos los backends lo soportan: la documentación de cada uno
  lo dice. En S3, desde Terraform 1.11 el bloqueo nativo se activa con `use_lockfile = true` (un
  archivo `.tflock` en el bucket) y el bloqueo con DynamoDB quedó deprecado.
- **Secretos en el estado**: el estado es un archivo en texto plano que incluye los valores de
  los recursos y data sources, también los secretos, aunque estén marcados `sensitive`. Por eso no va en Git, y el
  backend necesita cifrado en reposo, control de acceso y auditoría. Lo que llega al estado define
  cómo se manejan los [Secretos en Terraform](../Secretos/secretos-en-terraform.md).
- **Compartir salidas**: otra configuración puede leer los outputs de este estado con el data
  source `terraform_remote_state`.

Cada entorno tiene su propio estado ([Organizar entornos en Terraform](organizar-entornos-en-terraform.md)),
y el [pipeline de Terraform](pipeline-de-terraform.md) usa el backend remoto y su bloqueo.

## Dos `apply` contra el estado de producción

El estado de producción vive en `s3://infra-state/prod/terraform.tfstate` con `use_lockfile`. Si
el pipeline está aplicando y alguien corre `terraform apply` desde su máquina, el segundo recibe un
error de lock en vez de pisar el estado. Si un proceso murió y dejó el lock tomado,
`terraform force-unlock <ID>` lo libera.

## Bloqueo del estado y `.terraform.lock.hcl`

El bloqueo del estado no es el archivo `.terraform.lock.hcl`. Ese fija las versiones de los providers y sí va en Git; el
bloqueo del estado es un lock temporal mientras corre una operación.
