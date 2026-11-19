---
tipo: como-hacer
resumen: >-
  Armar un pipeline de Azure DevOps que construye la imagen, la sube a Azure Container Registry
  (ACR) y la despliega en Azure Kubernetes Service (AKS), con las service connections necesarias y
  el permiso de AKS para leer de ACR.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Archivo/DevOps/cicd-aks.md (original, texto generado con IA)"
  - "Microsoft Learn, Deploy to Azure Kubernetes Service with Azure Pipelines: https://learn.microsoft.com/en-us/azure/aks/devops-pipeline"
  - "Microsoft Learn, Use an Azure Resource Manager service connection: https://learn.microsoft.com/en-us/azure/devops/pipelines/library/connect-to-azure"
  - "Microsoft Learn, Integrate Azure Container Registry with AKS: https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration"
aliases: [CI/CD a AKS, Azure Pipelines a AKS, Pipeline ACR AKS]
parte_de: []
requiere: [pipeline-de-ci-cd]
relacionado: []
---

# Desplegar en AKS con Azure Pipelines

Armar un pipeline de Azure DevOps que construye la imagen, la sube a Azure Container Registry
(ACR) y la despliega en Azure Kubernetes Service (AKS), con las service connections necesarias y
el permiso de AKS para leer de ACR.

## Antes de empezar

- Un ACR y un clúster AKS en la misma suscripción, y un repositorio con un `Dockerfile`.
- Rol Owner (o User Access Administrator) para asignar roles en Azure.
- Entender las etapas de un [Pipeline de CI/CD](pipeline-de-ci-cd.md).

Hay tres permisos, y cada uno se configura aparte:

| Quién | Necesita | Cómo |
|---|---|---|
| El pipeline | Subir imágenes a ACR | Service connection de Docker Registry |
| El pipeline | Aplicar manifiestos en AKS | Service connection de Azure Resource Manager o de Kubernetes |
| Los nodos de AKS | Bajar imágenes de ACR | Rol `AcrPull` para la identidad del kubelet |

La identidad del kubelet es la identidad administrada con la que el agente de cada nodo baja
imágenes.

## Pasos

1. Creá la service connection de Azure Resource Manager en **Project settings > Service
   connections > New > Azure Resource Manager > App registration (automatic)** con credencial
   **Workload identity federation**, que Microsoft recomienda porque no guarda secretos. Limitá
   el alcance al grupo de recursos.
2. Dale a AKS permiso de lectura sobre ACR:
   `az aks update --name <aks> --resource-group <rg> --attach-acr <acr>`. Asigna `AcrPull`
   a la identidad del kubelet. Según Microsoft, así AKS se autentica solo contra ACR; el
   `imagePullSecret` queda para registros externos.
3. En **Pipelines > New pipeline**, elegí el repositorio y la plantilla **Deploy to Azure
   Kubernetes Service**. El paso 1 es requisito; además, el asistente crea una
   service connection nueva de Docker Registry hacia ACR, un environment con el namespace y los
   manifiestos `deployment.yml` y `service.yml`.
4. Revisá el `azure-pipelines.yml` generado: la etapa Build usa `Docker@2` con
   `command: buildAndPush` y publica los manifiestos como artifact; la etapa Deploy es un
   `deployment` sobre el environment y usa `KubernetesManifest@1` con `action: deploy` y la imagen
   con la etiqueta `$(tag)`. `tag` no es predefinida: la declara el bloque `variables`
   del mismo YAML.
5. Quitá el paso `KubernetesManifest@1` con `action: createSecret` y el input
   `imagePullSecrets` del deploy: después del paso 2 no hacen falta.
6. Guardá y corré el pipeline.

## Cómo saber que salió bien

- Las dos etapas terminan en verde y el environment muestra el deployment con la etiqueta nueva.
- `az aks check-acr --name <aks> --resource-group <rg> --acr <acr>.azurecr.io` confirma el acceso.
- `kubectl get pods` muestra los pods en `Running`, sin `ImagePullBackOff`.

## Relaciones

- Requiere: [Pipeline de CI/CD](pipeline-de-ci-cd.md) — las etapas y el artefacto que este pipeline concreta.
- Ver también: [Gestión de secretos](gestion-de-secretos.md) — por qué preferir workload identity federation a un secreto.
