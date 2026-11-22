---
resumen: >-
  Pasos de un pipeline de CI/CD para Terraform: fmt, validate, tflint, escaneo de seguridad con
  Checkov o Trivy, plan guardado como artefacto, aprobación en producción y apply del plan guardado
  solo desde ramas protegidas.
estado: borrador
estabilidad: semi
fuentes:
  - "HashiCorp, Running Terraform in automation: https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform"
  - "HashiCorp, terraform fmt: https://developer.hashicorp.com/terraform/cli/commands/fmt"
  - "HashiCorp, terraform validate: https://developer.hashicorp.com/terraform/cli/commands/validate"
  - "HashiCorp, terraform plan: https://developer.hashicorp.com/terraform/cli/commands/plan"
  - "TFLint: https://github.com/terraform-linters/tflint"
  - "Checkov, Terraform: https://www.checkov.io/7.Scan%20Examples/Terraform.html"
  - "Trivy, Terraform: https://trivy.dev/latest/docs/coverage/iac/terraform/"
  - "tfsec (consolidado en Trivy): https://github.com/aquasecurity/tfsec"
  - "Matias/Estudio/terraform-modulos-avanzados.md (CI/CD con Terraform)"
aliases: [CI/CD de Terraform, pipeline de infraestructura]
creado: 2026-10-03
revisado:
---

# Armar un pipeline de Terraform

Pasos de un pipeline de CI/CD para Terraform: fmt, validate, tflint, escaneo de seguridad con
Checkov o Trivy, plan guardado como artefacto, aprobación en producción y apply del plan guardado
solo desde ramas protegidas.

## Lo que tiene que estar antes del pipeline

- El estado en un backend remoto con bloqueo, que el pipeline toma al aplicar: [Estado remoto de Terraform](estado-remoto-de-terraform.md).
- Una identidad para el pipeline, sin claves fijas, que es la que lee los secretos: [Secretos en Terraform](secretos-en-terraform.md).
- Ramas protegidas en el repo: nadie hace push directo a `main`.

## Del `fmt` al `apply` del plan guardado

1. **Formato**: corré `terraform fmt -check -recursive`. Si hay archivos mal formateados, sale
   con código distinto de cero y los lista.
2. **Inicialización**: corré `terraform init -input=false` y definí `TF_IN_AUTOMATION=1` para que
   Terraform no sugiera comandos interactivos.
3. **Validación**: corré `terraform validate`. Chequea sintaxis y consistencia interna, no la nube
   ni el estado remoto.
4. **Lint**: corré `tflint --init` y después `tflint`. Detecta declaraciones sin usar y sintaxis
   deprecada; con el ruleset del proveedor (AWS, Azure o GCP) detecta además valores que
   validate no ve, como un tipo de instancia que no existe.
5. **Seguridad**: corré `checkov -d .` o `trivy config .`. Si hay un hallazgo grave, el job falla y
   el merge queda bloqueado. Qué cuenta como grave lo define el equipo, por ejemplo los hallazgos
   de severidad alta o crítica. tfsec ya no es la opción: su equipo concentra el trabajo en Trivy.
6. **Plan en el PR**: corré `terraform plan -input=false` en cada PR y publicá el resumen en el PR
   para que la revisión vea qué va a cambiar.
7. **Plan después del merge**: en la rama protegida, corré `terraform plan -input=false -out=tfplan`
   sobre el código ya mergeado y el estado actual. Guardá `tfplan` como artefacto con acceso
   restringido: contiene la configuración, el estado y los valores sensibles en texto plano.
8. **Aprobación**: si el destino es producción, el job se frena hasta que alguien con permiso lea
   ese plan y lo apruebe, por ejemplo con una regla de protección del entorno en el sistema de CI.
9. **Apply**: corré `terraform apply -input=false tfplan` con el plan aprobado. Si el estado cambió
   entre el plan y el apply, Terraform rechaza el plan y hay que volver al paso 7. Si el apply corre
   en otra máquina, restaurá el directorio de trabajo entero, incluido `.terraform`, en la misma
   ruta.

## Un plan posterior sin cambios

El PR muestra el plan y los checks en verde; el apply termina sin errores sobre el plan aprobado;
y un `terraform plan` posterior dice `No changes`.

El pipeline es la etapa de automatización de [Adoptar Terraform en un equipo](adoptar-terraform-en-un-equipo.md).

## Ver también

- [Pipeline de CI/CD](../../DevOps/Integracion-y-entrega/pipeline-de-ci-cd.md) (DevOps) — el pipeline de aplicaciones, con las mismas ideas.
