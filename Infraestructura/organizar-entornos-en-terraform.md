---
tipo: concepto
resumen: >-
  En Terraform, dev, test y prod se separan con una carpeta por entorno, cada una con su root
  module, su estado y sus credenciales, que llama a módulos comunes; los workspaces alcanzan solo
  cuando los entornos son casi iguales y comparten acceso.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "HashiCorp, Workspaces: https://developer.hashicorp.com/terraform/cli/workspaces"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección Terraform)"
aliases: [entornos en Terraform, workspaces de Terraform, carpeta por entorno]
parte_de: []
requiere: [modulo-de-terraform, estado-remoto-de-terraform]
relacionado: []
---

# Organizar entornos en Terraform

En Terraform, dev, test y prod se separan con una carpeta por entorno, cada una con su root
module, su estado y sus credenciales, que llama a módulos comunes; los workspaces alcanzan solo
cuando los entornos son casi iguales y comparten acceso.

## Por qué importa

Un error en dev no debería poder romper prod. Si los dos entornos comparten estado o
credenciales, un `apply` equivocado alcanza a ambos. La forma de organizar el repo decide cuán
aislados quedan y cuánto código se repite.

## Cómo funciona

- **Carpeta por entorno**: `environments/dev`, `environments/test` y `environments/prod` tienen
  cada una un root module chico que llama a los [[modulo-de-terraform|módulos]] comunes. Si los
  módulos están en el mismo repo (`modules/`), se llaman por ruta y todos los entornos usan la misma
  copia; si se publican en un registry o en un repo con tags, cada entorno fija su versión. Los
  valores propios de cada entorno (tamaños, rangos, nombres) van en sus argumentos o en un
  `terraform.tfvars` de la carpeta. Cada carpeta tiene su propio backend, con lo que
  cada entorno tiene su [[estado-remoto-de-terraform|estado]] y puede usar credenciales distintas.
- **Workspaces de la CLI**: varias instancias de estado sobre la misma configuración y el mismo
  backend. HashiCorp aclara que, por compartir backend, no son un mecanismo de aislamiento adecuado
  cuando los entornos necesitan credenciales y controles de acceso distintos; para eso recomienda
  configuraciones separadas que reutilicen módulos.
- **Repos por dominio**: en organizaciones grandes, una práctica habitual (criterio de Matías, no
  regla de HashiCorp) es separar red, seguridad y cargas de trabajo en repos distintos, cada uno con
  su estado y su pipeline.

## Ejemplo

Un equipo tiene dev y prod en suscripciones de Azure distintas. Usa `environments/dev` y
`environments/prod`, cada una con su backend y su identidad de despliegue, y las dos llaman al
módulo `network` publicado en el registry privado, versión `1.4.0`. Para probar la `1.5.0`, cambia solo la de dev.

## No confundir con

Los workspaces de HCP Terraform. En HCP Terraform un workspace es una unidad con su propio estado,
variables y permisos, más parecida a una carpeta por entorno que a un workspace de la CLI.

## Relaciones

- Requiere: [[modulo-de-terraform]] — cada entorno llama a los módulos comunes.
- Requiere: [[estado-remoto-de-terraform]] — la separación real es un estado por entorno.
- La usa: [[adoptar-terraform-en-un-equipo]] — la estructura de entornos se fija al empezar.
