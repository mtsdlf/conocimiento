---
resumen: >-
  Despliegue es la parte de DevOps que lleva una versión ya construida a cada entorno y la mantiene
  igual a lo declarado: cómo se reemplaza una versión por otra, cómo se describe la infraestructura
  y cómo GitOps aplica y promueve el estado guardado en Git.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Despliegue

Despliegue es la parte de DevOps que lleva una versión ya construida a cada entorno y la mantiene
igual a lo declarado: cómo se reemplaza una versión por otra, cómo se describe la infraestructura
y cómo GitOps aplica y promueve el estado guardado en Git.

Dentro de [DevOps](../devops.md), recibe el artefacto que produce
[Integración y entrega](../Integracion-y-entrega/integracion-y-entrega.md); el
[despliegue continuo](../Integracion-y-entrega/despliegue-continuo.md) depende de que acá haya un
despliegue gradual con rollback. Los PR de GitOps son donde [DevSecOps](../DevSecOps/devsecops.md)
aplica sus controles antes de desplegar.

## Dentro de un entorno y entre entornos

Las estrategias de despliegue (recreate, rolling, blue/green, canary y feature flags) cambian la
versión dentro de un entorno y deciden cuánta gente ve la nueva, cuánto tiempo y cómo se vuelve
atrás. La promoción entre entornos decide cuándo una versión pasa de staging a producción. Las dos
suponen artefactos inmutables: la versión vieja sigue existiendo y se puede volver a ella.

## Del push al pull

La infraestructura como código describe servidores, redes y servicios en archivos versionados,
pero se puede aplicar a mano o desde un pipeline que empuja. GitOps suma un agente dentro del
entorno que trae el estado deseado de Git y lo reconcilia de forma continua: corrige el drift, y
las credenciales de producción quedan dentro del entorno en vez de en el servidor de CI.

## Qué hay adentro de despliegue

- [Estrategias de despliegue](estrategias-de-despliegue.md) — rolling, blue/green, canary y feature flags, según el riesgo.
- [Infraestructura como código](infraestructura-como-codigo.md) — la infraestructura en archivos versionados que se aplican de forma repetible.
- [GitOps](gitops.md) — el estado deseado en Git y un agente que lo aplica; la puerta de entrada a las dos siguientes.
- [Reconciliación (GitOps)](reconciliacion-gitops.md) — el bucle que corrige el drift y por qué GitOps despliega por pull.
- [Promoción entre entornos](promocion-entre-entornos.md) — cómo pasar un cambio de un entorno al siguiente con un PR.
