---
resumen: >-
  Orden para que un equipo pase a gestionar su infraestructura con Terraform: estándares y estado
  remoto, módulos versionados, controles automáticos, pipeline y, al final, gobierno con
  policy-as-code.
estado: borrador
estabilidad: semi
fuentes:
  - "HashiCorp, Module creation - recommended pattern: https://developer.hashicorp.com/terraform/tutorials/modules/pattern-module-creation"
  - "HashiCorp, Running Terraform in automation: https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform"
  - "HashiCorp, Policy enforcement en HCP Terraform: https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement"
  - "HashiCorp, Private registry: https://developer.hashicorp.com/terraform/cloud-docs/registry"
  - "HashiCorp, Import: https://developer.hashicorp.com/terraform/language/import"
aliases: [plan de adopción de Terraform, migrar a Terraform]
creado: 2026-10-03
revisado:
---

# Adoptar Terraform en un equipo

Orden para que un equipo pase a gestionar su infraestructura con Terraform: estándares y estado
remoto, módulos versionados, controles automáticos, pipeline y, al final, gobierno con
policy-as-code.

## Lo que se apoya en lo anterior

Conviene entender qué es un [Módulo de Terraform](modulo-de-terraform.md), por qué el estado va en un
[backend remoto](estado-remoto-de-terraform.md), cómo se [separan
los entornos](organizar-entornos-en-terraform.md) y qué hace un [pipeline de Terraform](pipeline-de-terraform.md). Cada etapa se apoya en la anterior: un
pipeline sin estándares automatiza código inconsistente.

## Las diez etapas

1. **Estándares**: acordá la convención de nombres, las etiquetas obligatorias (dueño, equipo,
   entorno) y la estructura de carpetas. Todo cambio entra por PR con revisión.
2. **Estado**: creá un backend remoto con bloqueo y cifrado, con un estado por entorno.
3. **Piloto**: elegí un servicio o un entorno chico y llevalo a Terraform primero, para ajustar
   estándares y módulos antes de extender.
4. **Importar lo existente**: los recursos que ya existen se traen al estado con bloques `import`
   (o `terraform import`) en vez de recrearlos; `terraform plan` debe quedar sin cambios después de
   importar.
5. **Módulos**: armá los módulos de lo que se despliega siempre junto (red, almacenamiento, base
   de datos), con variables validadas, y publicalos con versión semántica en un registry privado o
   en un repo con tags. Si un recurso ya importado pasa a un módulo, un bloque `moved` le
   avisa a Terraform que es el mismo y evita que lo recree.
6. **Secretos**: sacá todo secreto del código y leelo de un gestor; ver [Secretos en Terraform](../Secretos/secretos-en-terraform.md).
7. **Controles locales**: sumá hooks de pre-commit con `terraform fmt`, `validate` (que necesita
   un `terraform init` previo) y `tflint`, para que el error aparezca antes del PR.
8. **Pipeline**: automatizá plan en cada PR, escaneo de seguridad, aprobación en producción y apply
   del plan guardado. Desde acá, nadie aplica cambios a mano.
9. **Extender**: repetí piloto e importación con el resto de los servicios, uno por vez.
10. **Gobierno**: si el equipo usa HCP Terraform (el servicio administrado de HashiCorp), definí
   políticas como código (policy-as-code) con Sentinel u OPA que frenen un
   run que no cumple (por ejemplo, un recurso sin etiqueta de dueño). Revisá cada tanto las
   versiones de módulos y providers desactualizadas.

## Nada se crea fuera de Terraform

Ningún recurso de los servicios migrados se crea fuera de Terraform; `terraform plan` en cada entorno no muestra
desvíos; y todo cambio de infraestructura tiene un PR con su plan.

## Ver también

- [Gobernanza de plataforma](../../Platform-Engineering/Plataforma-interna/gobernanza-de-plataforma.md) (Platform-Engineering) — policy-as-code como forma
  de gobierno de una plataforma.
