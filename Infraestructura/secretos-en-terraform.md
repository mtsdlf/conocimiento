---
tipo: concepto
resumen: >-
  En Terraform los secretos no se escriben en el código ni en tfvars: se leen de un gestor con una
  identidad de corta vida, y como `sensitive` solo los oculta de la salida, se usan valores
  ephemeral o argumentos write-only para que no queden en el estado.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "HashiCorp, Input variables (sensitive, ephemeral): https://developer.hashicorp.com/terraform/language/values/variables"
  - "HashiCorp, Outputs: https://developer.hashicorp.com/terraform/language/values/outputs"
  - "HashiCorp, Ephemeral resources: https://developer.hashicorp.com/terraform/language/resources/ephemeral"
  - "HashiCorp, Write-only arguments: https://developer.hashicorp.com/terraform/language/manage-sensitive-data/write-only"
  - "HashiCorp, Dynamic provider credentials: https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials"
  - "azurerm, data source azurerm_key_vault_secret: https://github.com/hashicorp/terraform-provider-azurerm/blob/main/website/docs/d/key_vault_secret.html.markdown"
  - "azurerm, ephemeral azurerm_key_vault_secret: https://github.com/hashicorp/terraform-provider-azurerm/blob/main/website/docs/ephemeral-resources/key_vault_secret.html.markdown"
  - "Terraform v1.10 changelog: https://github.com/hashicorp/terraform/blob/v1.10/CHANGELOG.md"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección Terraform)"
aliases: [secrets en Terraform, sensitive, ephemeral, write-only]
parte_de: []
requiere: [estado-remoto-de-terraform]
relacionado: [sops]
---

# Secretos en Terraform

En Terraform los secretos no se escriben en el código ni en tfvars: se leen de un gestor con una
identidad de corta vida, y como `sensitive` solo los oculta de la salida, se usan valores
ephemeral o argumentos write-only para que no queden en el estado.

## Por qué importa

Un secreto en un `.tf` o en un `tfvars` versionado queda en el historial de Git para siempre. Y
aunque no esté en Git, Terraform guarda en el [[estado-remoto-de-terraform|estado]] y en los
archivos de plan, en texto plano, todo valor que pase por un recurso o un data source.

## Cómo funciona

- **De dónde sale el secreto**: de un gestor (Azure Key Vault, HashiCorp Vault, AWS Secrets
  Manager), que Terraform consulta cada vez que corre.
- **Con qué identidad**: sin claves fijas. En Azure, una managed identity (identidad que Azure
  asigna a un recurso) o un service principal que se autentica por OIDC con un token de corta vida
  del sistema de CI; HCP Terraform genera credenciales dinámicas por OIDC que se descartan al
  terminar cada run.
- **`sensitive = true`** en variables y outputs: oculta el valor en la salida de la CLI, pero
  Terraform lo sigue guardando en el estado, y `terraform output -json` lo muestra.
- **Valores ephemeral** (Terraform 1.10 en adelante): variables, outputs y recursos ephemeral no
  se guardan en el estado ni en el plan. El provider de Azure tiene una versión ephemeral de
  `azurerm_key_vault_secret`; la versión data source guarda el secreto en el estado.
- **Argumentos write-only** (Terraform 1.11 en adelante): un argumento como `password_wo` recibe
  un valor que el provider de Terraform envía a la API y no se guarda. Como Terraform no recuerda
  el valor, no detecta que cambió: para rotarlo se sube el argumento de versión que lo acompaña
  (por ejemplo `password_wo_version`).

El acceso al gestor se da con permisos mínimos: la identidad del pipeline lee solo los secretos de
su entorno.

## Ejemplo

Una base de datos necesita su contraseña de administrador. El pipeline se autentica en Azure por
OIDC, el root module lee la contraseña con el recurso ephemeral `azurerm_key_vault_secret` y la
pasa al argumento write-only de la base. El estado registra la base, pero no la contraseña.

## No confundir con

[[sops]]. SOPS guarda el secreto cifrado dentro del repo y lo descifra quien tiene la clave; acá el
secreto nunca entra al repo, vive en el gestor y Terraform lo lee al aplicar.

## Relaciones

- Requiere: [[estado-remoto-de-terraform]] — el estado es donde un secreto se filtra sin avisar.
- Relacionado: [[sops]] — la otra forma de tener secretos junto al código.
- La usa: [[pipeline-de-terraform]] — el pipeline es quien se autentica y lee los secretos.
