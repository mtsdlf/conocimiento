---
resumen: >-
  Aprovisionamiento es la parte de la infraestructura que crea y cambia los recursos con código
  (infraestructura como código): cómo se arman los módulos, dónde vive el estado, cómo se separan
  los entornos, cómo un pipeline aplica los cambios y dónde quedan los secretos.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Aprovisionamiento

Aprovisionamiento es la parte de la infraestructura que crea y cambia los recursos con código
(infraestructura como código): cómo se arman los módulos, dónde vive el estado, cómo se separan
los entornos, cómo un pipeline aplica los cambios y dónde quedan los secretos.

Dentro de la [infraestructura](../infraestructura.md), crea los recursos sobre los que corre el
resto. El concepto es la [infraestructura como código](infraestructura-como-codigo.md); las notas
de la vertical lo concretan con Terraform. Las credenciales salen de un gestor o van cifradas, como
explica la [gestión de secretos](../../DevOps/DevSecOps/gestion-de-secretos.md) de DevSecOps. Ofrecer
la infraestructura como API a otros equipos, en vez de como un repositorio de código, es lo que
hace [Crossplane](../../Platform-Engineering/Plataforma-interna/crossplane.md).

## Configuración, estado y realidad

En cada `plan`, Terraform compara la configuración, el estado y la infraestructura real. El estado
registra qué recurso real corresponde a cada bloque; un equipo lo guarda en un backend remoto con
bloqueo para que dos `apply` no lo corrompan. Como el estado guarda en texto plano todo valor que
pasa por un recurso, también los secretos, no va en Git.

## Módulos, entornos y pipeline

Un módulo agrupa recursos que se despliegan juntos, con variables validadas, outputs y versión.
Cada entorno (dev, test, prod) es una carpeta con su root module, su estado y sus credenciales,
que llama a los módulos comunes. Un pipeline lleva cada cambio de `fmt` a un `apply` del plan
guardado, con aprobación en producción. Un equipo adopta todo esto en orden: estándares y estado
primero, módulos después, el pipeline y, al final,
[policy-as-code](../../DevOps/DevSecOps/policy-as-code.md).

## Qué hay adentro de aprovisionamiento

- [Infraestructura como código](infraestructura-como-codigo.md) — describir la infraestructura en
  archivos versionados que se aplican de forma repetible. Leerla primero.
- [Módulo de Terraform](modulo-de-terraform.md) — qué es un módulo y cómo se diseña para que otro
  equipo lo use sin leerlo por dentro.
- [Estado remoto de Terraform](estado-remoto-de-terraform.md) — qué guarda el estado y por qué va
  en un backend remoto con bloqueo.
- [Organizar entornos en Terraform](organizar-entornos-en-terraform.md) — cuándo separar dev, test
  y prod en carpetas y cuándo alcanzan los workspaces.
- [Armar un pipeline de Terraform](pipeline-de-terraform.md) — los pasos de CI/CD desde `fmt`
  hasta un `apply` sobre un plan guardado.
- [Secretos en Terraform](secretos-en-terraform.md) — dónde viven los secretos y qué hace (y qué
  no) `sensitive`.
- [Adoptar Terraform en un equipo](adoptar-terraform-en-un-equipo.md) — en qué orden un equipo pasa
  a Terraform, de los estándares al policy-as-code.
