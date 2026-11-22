---
resumen: >-
  La reconciliación es el bucle que compara el estado deseado en Git con el estado real, corrige
  el drift y explica por qué GitOps despliega por pull y no por push.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenGitOps, GitOps Principles v1.0.0: https://opengitops.dev/"
  - "Argo CD, Automated Sync Policy: https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/"
  - "Argo CD, High Availability (caché del clúster con watch): https://argo-cd.readthedocs.io/en/stable/operator-manual/high_availability/"
  - "Argo CD, Architecture (detección de OutOfSync): https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/"
  - "Archivo/DevOps/gitops-principios.md (original, texto generado con IA)"
aliases: [Reconciliación, Reconciliation loop, Bucle de reconciliación, Drift]
creado: 2026-10-03
revisado:
---

# Reconciliación (GitOps)

La reconciliación es el bucle que compara el estado deseado en Git con el estado real, corrige
el drift y explica por qué GitOps despliega por pull y no por push.

## Por qué un despliegue no garantiza que el entorno siga igual

Un despliegue que se hace una vez no garantiza que el entorno siga igual: alguien edita un
recurso a mano, un despliegue falla a medias o se borra algo. La reconciliación detecta esa
diferencia, llamada **drift**, y la corrige o la avisa, sin esperar al próximo despliegue.

## El bucle, self-heal y prune, push y pull

Un agente dentro del entorno (Argo CD o Flux en Kubernetes) repite tres pasos:

1. Lee el estado deseado del repositorio.
2. Consulta el estado real del entorno por su API.
3. Calcula la diferencia y aplica lo necesario hasta que coincidan.

Los dos lados se observan distinto en Argo CD. El clúster se vigila con la API de watch de
Kubernetes, así que una edición manual se detecta casi enseguida y la aplicación pasa a
`OutOfSync`, el estado que muestra el drift. Git, en cambio, se consulta cada 120 segundos más
hasta 60 de variación aleatoria, salvo que un webhook avise antes. Con **self-heal** activo,
Argo CD corrige el drift 5 segundos después de detectarlo. Con **prune** activo, borra del
clúster lo que se borró de Git; por defecto no lo hace, como protección.

**Push y pull** son las dos formas de llevar un cambio a producción:

| Modelo | Quién aplica | Credenciales de producción |
|---|---|---|
| Push | el pipeline de CI, al final de su ejecución | las tiene el servidor de CI |
| Pull (GitOps) | el agente dentro del entorno | quedan dentro del entorno |

En el modelo push, el pipeline aplica una vez y no ve lo que pasa después. En el modelo pull, el
agente reconcilia siempre, y el CI solo necesita escribir en el repositorio de configuración.

## Un escalado manual que Argo CD revierte

Durante un incidente, alguien escala un Deployment de 3 a 6 réplicas con `kubectl`. Con
self-heal activo, Argo CD marca la aplicación como `OutOfSync` y vuelve a 3 réplicas en
segundos. El cambio que debía quedar se hace con un PR al repositorio, y entonces el agente lo
aplica.

## Reconciliar no es monitorear

**Monitoreo del servicio**: la reconciliación compara configuración declarada con configuración
real; no mide si el servicio responde bien. Eso es parte de la [Observabilidad](../Operacion/observabilidad.md).

## Ver también

- [GitOps](gitops.md) — es el cuarto principio de GitOps y da por sabido el resto.
