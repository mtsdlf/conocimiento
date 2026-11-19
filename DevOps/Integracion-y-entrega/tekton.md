---
resumen: >-
  Tekton es un framework de CI/CD nativo de Kubernetes: define Tasks y Pipelines como recursos del
  clúster, con params y workspaces, y los dispara ante eventos externos con Tekton Triggers.
estado: borrador
estabilidad: estable
fuentes:
  - "Tekton, Tasks: https://tekton.dev/docs/pipelines/tasks/"
  - "Tekton, Pipelines: https://tekton.dev/docs/pipelines/pipelines/"
  - "Tekton, Workspaces: https://tekton.dev/docs/pipelines/workspaces/"
  - "Tekton, Triggers: https://tekton.dev/docs/triggers/"
  - "Tekton, EventListeners: https://tekton.dev/docs/triggers/eventlisteners/"
aliases: [Tekton Pipelines, Tekton Triggers, OpenShift Pipelines]
creado: 2026-10-03
revisado:
---

# Tekton

Tekton es un framework de CI/CD nativo de Kubernetes: define Tasks y Pipelines como recursos del
clúster, con params y workspaces, y los dispara ante eventos externos con Tekton Triggers.

## El pipeline dentro del clúster

Un [Pipeline de CI/CD](pipeline-de-ci-cd.md) en Tekton vive en el mismo clúster donde se despliega: se versiona como
cualquier manifiesto, escala con los nodos y no necesita un servidor de CI aparte. OpenShift lo
distribuye como OpenShift Pipelines.

## Tasks, Pipelines, params, workspaces y Triggers

- **Step**: un contenedor que corre una herramienta hasta terminar o fallar.
- **Task**: una lista ordenada de steps. Cada Task corre como un Pod (el grupo de contenedores
  que Kubernetes programa junto en un nodo).
- **Pipeline**: un grafo de Tasks. Por defecto las Tasks corren en paralelo; el orden se fija con
  `runAfter` o al usar el resultado de otra Task.
- **TaskRun y PipelineRun**: cada ejecución concreta, con los valores de esa vez.

Dos mecanismos separan la definición de la ejecución:

- **Params**: valores que la Task o el Pipeline declaran y el Run provee, como la URL del
  repositorio o la rama. Se leen con `$(params.nombre)`.
- **Workspaces**: partes del sistema de archivos que la Task declara y el Run vincula a un volumen
  real: `emptyDir`, un PVC (un pedido de disco persistente), un `volumeClaimTemplate`, un Secret
  o un ConfigMap. Así una Task clona el código en un workspace y la siguiente lo compila desde ahí.

```yaml
apiVersion: tekton.dev/v1
kind: Task
metadata:
  name: saludar
spec:
  params:
    - name: mensaje
      type: string
  workspaces:
    - name: fuente
  steps:
    - name: echo
      image: alpine
      script: echo "$(params.mensaje)" && ls $(workspaces.fuente.path)
```

**Tekton Triggers** agrega la entrada por eventos, es decir, por webhooks: llamadas HTTP que un
servicio como Azure Repos o GitHub hace cuando pasa algo, con el detalle en JSON.

- **EventListener**: recibe el webhook en un Service `el-<nombre>` (puerto 8080 por defecto).
- **Interceptor**: valida o filtra el evento antes de usarlo, por ejemplo con una expresión CEL
  (Common Expression Language, un lenguaje chico de condiciones).
- **TriggerBinding**: extrae campos del JSON del evento.
- **TriggerTemplate**: crea el PipelineRun con esos campos como params.

```mermaid
flowchart LR
  W[Webhook] --> EL[EventListener] --> I[Interceptor] --> TB[TriggerBinding] --> TT[TriggerTemplate] --> PR[PipelineRun]
```

## De un push en el EventListener a Argo CD

Argo CD es el agente de [GitOps](../Despliegue/gitops.md) que aplica en el clúster lo que hay en un repositorio. Un push llega al EventListener; el TriggerBinding toma la URL del repositorio y la rama; el
TriggerTemplate crea un PipelineRun que clona, construye la imagen y actualiza `values.yaml` en el
repositorio GitOps; Argo CD detecta el commit y despliega (ver [Promoción entre entornos](../Despliegue/promocion-entre-entornos.md)).

## Tekton ejecuta, Argo CD reconcilia

Argo CD. Tekton ejecuta pasos (CI, empaquetado); Argo CD reconcilia el estado declarado en Git con
el clúster (ver [GitOps](../Despliegue/gitops.md)). Suelen usarse juntos.

## Ver también

- [Disparar Tekton desde Azure DevOps](disparar-tekton-desde-azure-devops.md) — la guía para conectar Triggers con Azure Repos.
