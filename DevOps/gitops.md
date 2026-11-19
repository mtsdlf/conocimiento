---
tipo: concepto
resumen: >-
  GitOps es operar sistemas declarando el estado deseado en Git, y que un agente dentro del
  entorno lo traiga y lo aplique de forma continua.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "OpenGitOps, GitOps Principles v1.0.0: https://opengitops.dev/"
  - "Argo CD, Best Practices (repositorio de configuración separado): https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/"
  - "Archivo/DevOps/gitops-principios.md (original, texto generado con IA)"
aliases: [GitOps]
parte_de: []
requiere: []
relacionado: [devsecops, gestion-de-secretos]
---

# GitOps

GitOps es operar sistemas declarando el estado deseado en Git, y que un agente dentro del
entorno lo traiga y lo aplique de forma continua.

## Por qué importa

Sin GitOps, el estado de producción depende de quién corrió qué comando y cuándo. Con GitOps,
cada cambio es un commit revisado en un PR: el historial de Git es la auditoría, y volver atrás
es revertir un commit. Además, el pipeline de CI ya no necesita credenciales de producción,
porque el agente aplica los cambios desde adentro.

## Cómo funciona

El proyecto OpenGitOps (CNCF) fija cuatro principios en su versión 1.0.0:

1. **Declarativo**: el estado deseado del sistema se expresa de forma declarativa (manifiestos
   de Kubernetes, valores de Helm, código de infraestructura).
2. **Versionado e inmutable**: el estado deseado se guarda en un almacén que impone
   inmutabilidad y versionado, y conserva el historial completo. Git es el caso habitual.
3. **Traído automáticamente**: agentes de software traen las declaraciones desde la fuente, sin
   que nadie las empuje.
4. **Reconciliado continuamente**: los agentes observan el estado real y lo llevan al deseado.
   Ese bucle se explica en [Reconciliación (GitOps)](reconciliacion-gitops.md).

Argo CD recomienda guardar los manifiestos en un repositorio distinto del código de la
aplicación. Así un cambio de configuración no dispara un build, el historial muestra solo los
cambios de entorno, y quien programa no necesita permiso para tocar producción.

GitOps es la forma natural de operar una [Internal Developer Platform](../Platform-Engineering/internal-developer-platform.md): con
[Crossplane](../Platform-Engineering/crossplane.md), la misma idea declarativa se extiende de las aplicaciones a la infraestructura.
Los manifiestos suelen salir de la [Infraestructura como código](infraestructura-como-codigo.md).

## Ejemplo

Un equipo cambia la imagen de su servicio de `v1.2.3` a `v1.2.4` en el repositorio de
configuración y abre un PR. Al mergearlo, Argo CD detecta el commit en su siguiente consulta y
actualiza el Deployment del clúster. Si alguien edita el Deployment a mano, Argo CD lo marca
como desincronizado y, con self-heal activo (la opción que corrige sola las ediciones manuales),
lo vuelve al valor de Git. Ese bucle se detalla en [Reconciliación (GitOps)](reconciliacion-gitops.md).

## No confundir con

**Infraestructura como código**: describe el estado en archivos, pero se puede aplicar a mano o
desde un pipeline que empuja. GitOps suma el agente que trae y reconcilia de forma continua.

## Relaciones

- Partes: [Reconciliación (GitOps)](reconciliacion-gitops.md) — el bucle que aplica el estado de Git.
- Partes: [Promoción entre entornos](promocion-entre-entornos.md) — cómo un cambio pasa de un entorno al siguiente.
- Relacionado: [DevSecOps](devsecops.md) — los PR de GitOps son el punto donde se aplican los controles de seguridad.
- Relacionado: [Gestión de secretos](gestion-de-secretos.md) — Git no puede guardar secretos en claro, y GitOps necesita una forma de declararlos.
- Ver también: [Internal Developer Platform](../Platform-Engineering/internal-developer-platform.md) — la plataforma que GitOps suele operar.
- Ver también: [Crossplane](../Platform-Engineering/crossplane.md) — la extensión de GitOps a recursos de infraestructura.
