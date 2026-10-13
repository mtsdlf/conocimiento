---
tipo: concepto
resumen: >-
  El estado de Terraform registra qué recurso real corresponde a cada bloque de la configuración;
  guardarlo en un backend remoto con bloqueo deja que un equipo lo comparta sin que dos `apply` lo
  corrompan.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "HashiCorp, State: https://developer.hashicorp.com/terraform/language/state"
  - "HashiCorp, Remote state: https://developer.hashicorp.com/terraform/language/state/remote"
  - "HashiCorp, State locking: https://developer.hashicorp.com/terraform/language/state/locking"
  - "HashiCorp, Backend S3: https://developer.hashicorp.com/terraform/language/backend/s3"
  - "HashiCorp, Sensitive data in state: https://developer.hashicorp.com/terraform/language/state/sensitive-data"
  - "Terraform v1.11 changelog: https://github.com/hashicorp/terraform/blob/v1.11/CHANGELOG.md"
aliases: [Terraform state, tfstate, backend de Terraform, state locking]
parte_de: []
requiere: []
relacionado: []
---

# Estado remoto de Terraform

El estado de Terraform registra qué recurso real corresponde a cada bloque de la configuración;
guardarlo en un backend remoto con bloqueo deja que un equipo lo comparta sin que dos `apply` lo
corrompan.

## Por qué importa

Terraform compara tres cosas en cada `plan`: la configuración, el estado y la infraestructura real.
Sin el estado no sabe que la VM `web` ya existe y es la de tal ID, y propondría crearla de nuevo.
Con el estado en el disco de una persona, según HashiCorp, cada uno tiene que asegurarse de tener
la última versión y de que nadie más esté corriendo Terraform a la vez.

## Cómo funciona

- **Backend remoto**: se configura con un bloque `backend` dentro de `terraform { }`, y el estado vive en un almacenamiento compartido (HCP Terraform, el servicio de HashiCorp; un bucket S3,
  un container de Azure Storage, GCS). Todo el equipo y el pipeline leen y escriben el mismo.
- **Bloqueo**: antes de una operación que escribe el estado, Terraform toma un lock; si otro
  proceso lo tiene, falla con un error que muestra el ID del lock (o espera, si se pasó
  `-lock-timeout`). No todos los backends lo soportan: la documentación de cada uno
  lo dice. En S3, desde Terraform 1.11 el bloqueo nativo se activa con `use_lockfile = true` (un
  archivo `.tflock` en el bucket) y el bloqueo con DynamoDB quedó deprecado.
- **Secretos en el estado**: el estado es un archivo en texto plano que incluye los valores de
  los recursos y data sources, también los secretos, aunque estén marcados `sensitive`. Por eso no va en Git, y el
  backend necesita cifrado en reposo, control de acceso y auditoría.
- **Compartir salidas**: otra configuración puede leer los outputs de este estado con el data
  source `terraform_remote_state`.

## Ejemplo

El estado de producción vive en `s3://infra-state/prod/terraform.tfstate` con `use_lockfile`. Si
el pipeline está aplicando y alguien corre `terraform apply` desde su máquina, el segundo recibe un
error de lock en vez de pisar el estado. Si un proceso murió y dejó el lock tomado,
`terraform force-unlock <ID>` lo libera.

## No confundir con

El archivo `.terraform.lock.hcl`. Ese fija las versiones de los providers y sí va en Git; el
bloqueo del estado es un lock temporal mientras corre una operación.

## Relaciones

- Base de: [[organizar-entornos-en-terraform]] — cada entorno tiene su propio estado.
- Base de: [[pipeline-de-terraform]] — el pipeline usa el backend remoto y su bloqueo.
- Base de: [[secretos-en-terraform]] — lo que llega al estado define cómo se manejan los secretos.
