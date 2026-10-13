---
tipo: concepto
resumen: >-
  Un módulo de Terraform es un conjunto de recursos que se gestionan juntos, con variables tipadas
  y validadas, outputs y versión, para que otros equipos lo usen sin conocer su interior.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "HashiCorp, Modules: https://developer.hashicorp.com/terraform/language/modules"
  - "HashiCorp, Standard module structure: https://developer.hashicorp.com/terraform/language/modules/develop/structure"
  - "HashiCorp, Creating modules: https://developer.hashicorp.com/terraform/language/modules/develop"
  - "HashiCorp, Module creation - recommended pattern: https://developer.hashicorp.com/terraform/tutorials/modules/pattern-module-creation"
  - "HashiCorp, Module sources: https://developer.hashicorp.com/terraform/language/modules/sources"
  - "HashiCorp, Input variables: https://developer.hashicorp.com/terraform/language/values/variables"
  - "HashiCorp, depends_on: https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección Terraform)"
aliases: [módulo Terraform, Terraform module]
parte_de: []
requiere: []
relacionado: []
---

# Módulo de Terraform

Un módulo de Terraform es un conjunto de recursos que se gestionan juntos, con variables tipadas
y validadas, outputs y versión, para que otros equipos lo usen sin conocer su interior.

Así se describe un módulo reutilizable, que es el sentido habitual de la palabra. En sentido
técnico, cualquier carpeta con archivos `.tf` es un módulo.

## Por qué importa

Sin módulos, cada entorno copia los mismos bloques de recursos y una corrección se repite en todas
las copias. Con un módulo, quien lo usa pasa unos pocos parámetros y recibe una red o una base de
datos armada según el estándar del equipo.

## Cómo funciona

El **root module** es la carpeta donde se corre Terraform, y los
**child modules** son los que esa carpeta llama con bloques `module`. La estructura estándar que
recomienda HashiCorp es `main.tf`, `variables.tf`, `outputs.tf` y un `README.md`.

- **Entradas**: cada variable declara su `type` y, si hace falta, un bloque `validation` con una
  condición y un mensaje de error. Así un valor inválido falla en el `plan`, no en la nube.
- **Salidas**: los `outputs` exponen lo que otro módulo necesita.
- **Versión**: el módulo se publica con versión semántica, en un registry privado (un catálogo
  interno de módulos) o en un repo de Git con tags. Quien lo usa fija la versión (`version = "~> 2.1"` en un registry, `?ref=v2.1.0`
  en Git), y un cambio que rompe sube la versión mayor.

Entre módulos, las dependencias salen de usar outputs como entradas; HashiCorp deja `depends_on`
como último recurso, porque genera planes que reemplazan más de lo necesario.

HashiCorp propone que un módulo agrupe lo que se despliega siempre junto, sin cruzar límites de
permisos, y desaconseja módulos que solo envuelven un recurso: un buen módulo describe un concepto
de la arquitectura y cubre el caso común.

## Ejemplo

Un módulo `network` crea una red virtual de Azure y sus subredes. Recibe el rango de direcciones,
valida que sea un CIDR (como `10.0.0.0/16`) y devuelve los IDs de las subredes. Dev y prod lo
llaman con la versión `1.4.0` y distintos rangos.

## No confundir con

Un provider, que habla con la API de una nube y define los tipos de recurso; el módulo combina
recursos de uno o varios providers. Tampoco con [[crossplane]], que corre dentro de
Kubernetes y corrige desvíos todo el tiempo; Terraform aplica un plan cuando alguien lo ejecuta.

## Relaciones

- Base de: [[organizar-entornos-en-terraform]] — cada entorno es un root module que llama a módulos comunes.
- Base de: [[adoptar-terraform-en-un-equipo]] — armar módulos versionados es una etapa de la adopción.
- Ver también: [[capacidad-de-plataforma]] (Platform-Engineering) — una plataforma puede ofrecer
  módulos de Terraform como forma de proveer infraestructura.
- Ver también: [[golden-path]] (Platform-Engineering) — los módulos aprobados son el camino
  estándar para crear infraestructura.
