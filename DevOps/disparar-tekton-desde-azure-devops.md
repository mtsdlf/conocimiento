---
tipo: como-hacer
resumen: >-
  Lanzar un PipelineRun de Tekton en OpenShift cada vez que hay un push o un pull request en Azure
  Repos, con un Service Hook de Azure DevOps y un EventListener protegido por un token guardado en
  un Secret.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Webhooks with Azure DevOps: https://learn.microsoft.com/en-us/azure/devops/service-hooks/services/webhooks"
  - "Microsoft Learn, Service hooks events (payloads de git.push y git.pullrequest.created): https://learn.microsoft.com/en-us/azure/devops/service-hooks/events"
  - "Microsoft Learn, Allowed address lists and network connections: https://learn.microsoft.com/en-us/azure/devops/organizations/security/allow-list-ip-url"
  - "Tekton, EventListeners: https://tekton.dev/docs/triggers/eventlisteners/"
  - "Tekton, Interceptors: https://tekton.dev/docs/triggers/interceptors/"
  - "Tekton, CEL expression extensions (compareSecret): https://tekton.dev/docs/triggers/cel_expressions/"
aliases: [Tekton Triggers con Azure DevOps, Webhook de Azure Repos a Tekton]
parte_de: []
requiere: [tekton]
relacionado: []
---

# Disparar Tekton desde Azure DevOps

Lanzar un PipelineRun de Tekton en OpenShift cada vez que hay un push o un pull request en Azure
Repos, con un Service Hook de Azure DevOps y un EventListener protegido por un token guardado en
un Secret.

## Antes de empezar

- Un clúster OpenShift con OpenShift Pipelines (Tekton Pipelines y Triggers) instalado.
- Un Pipeline ya aplicado que reciba el repositorio y la rama por params (ver [[tekton]]).
- Permiso de administrador del proyecto en Azure DevOps.
- Un token generado al azar, guardado en el gestor de contraseñas. Acá se escribe `<TOKEN>`.

## Pasos

1. Creá el Secret con el token en el namespace del EventListener:
   `oc create secret generic azure-webhook --from-literal=token=<TOKEN>`.
2. Aplicá un TriggerTemplate `azure-template` que cree el PipelineRun con los params `repo` y
   `rama`, y dos TriggerBinding que los llenen, porque cada evento trae la rama en otro campo:
   - `azure-push-binding` (evento `git.push`): `repo` = `$(body.resource.repository.name)` y
     `rama` = `$(body.resource.refUpdates[0].name)`;
   - `azure-pr-binding` (evento `git.pullrequest.created`): `repo` igual y
     `rama` = `$(body.resource.sourceRefName)`.
3. Aplicá el EventListener con un trigger por evento. Cada uno filtra por `eventType` y compara el
   header contra el Secret con `compareSecret`, en tiempo constante y sin escribir el token en el
   YAML:

   ```yaml
   apiVersion: triggers.tekton.dev/v1beta1
   kind: EventListener
   metadata:
     name: azure-repos
   spec:
     serviceAccountName: pipeline
     triggers:
       - name: push
         interceptors:
           - ref: {name: cel}
             params:
               - name: filter
                 value: >-
                   header.canonical('X-Webhook-Token').compareSecret('token', 'azure-webhook')
                   && body.eventType == 'git.push'
         bindings: [{ref: azure-push-binding}]
         template: {ref: azure-template}
       # el trigger "pr" repite lo mismo con 'git.pullrequest.created' y azure-pr-binding
   ```

4. Exponé el Service `el-azure-repos` con una Route con TLS, porque Microsoft pide que los
   webhooks usen solo HTTPS:
   `oc create route edge el-azure-repos --service=el-azure-repos --port=8080`.
5. En Azure DevOps, abrí **Project settings > Service hooks > Create subscription > Web Hooks** y
   creá una suscripción por evento: **Code pushed** y **Pull request created**, filtradas por
   repositorio y rama.
6. En la acción de cada una, pegá la URL `https://` de la Route, agregá el header
   `X-Webhook-Token: <TOKEN>` y dejá **Resource details to send** en **All**: con **Minimal**
   solo llegan campos como la URL y el ID, y los bindings no encuentran la rama.
7. Opcional: limitá el ingreso con una NetworkPolicy que acepte solo los rangos de IP de entrada
   que Microsoft publica para Azure DevOps (o el service tag `AzureDevOps` en un firewall de Azure).

## Cómo saber que salió bien

- **Test** en cada Service Hook devuelve 2xx y `oc get pipelinerun` muestra uno nuevo.
- Un `curl` a la Route sin el header no crea ningún PipelineRun.

## Relaciones

- Requiere: [[tekton]] — explica EventListener, interceptores, bindings y templates.
- Ver también: [[gestion-de-secretos]] — por qué el token vive en un Secret y no en el manifiesto.
