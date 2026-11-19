---
tipo: como-hacer
resumen: >-
  Pasos para instalar un clúster de Kubernetes con Kubespray y Ansible en Debian o Ubuntu, con
  Cilium como CNI: requisitos, inventario, variables, `cluster.yml`, verificación, escalar y
  resetear.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Kubespray, README v2.32.0: https://github.com/kubernetes-sigs/kubespray/blob/v2.32.0/README.md"
  - "Kubespray, Getting started: https://github.com/kubernetes-sigs/kubespray/blob/v2.32.0/docs/getting_started/getting-started.md"
  - "Kubespray, release v2.27.0 (quita inventory_builder): https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.27.0"
  - "Cilium, Kubernetes without kube-proxy: https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/"
  - "Cilium, System requirements (puertos): https://docs.cilium.io/en/stable/operations/system_requirements/"
  - "Archivo/Infraestructura/kubespray-cilium.md"
aliases: [instalar Kubernetes con Kubespray, Kubespray]
parte_de: []
requiere: [cilium]
relacionado: []
---

# Desplegar Kubernetes con Kubespray

Pasos para instalar un clúster de Kubernetes con Kubespray y Ansible en Debian o Ubuntu, con
Cilium como CNI: requisitos, inventario, variables, `cluster.yml`, verificación, escalar y
resetear.

## Antes de empezar

- Entender qué modo de [Cilium](cilium.md), el plugin de red (CNI) que conecta los pods, conviene: túnel o ruteo nativo, con o sin kube-proxy.
- Una máquina de control con Git y Python, y acceso SSH a todos los nodos con un usuario que use
  sudo sin contraseña.
- Nodos con un sistema soportado por la versión de Kubespray elegida (la lista está en su README;
  la v2.32.0, de septiembre de 2026, soporta Debian Bookworm y Trixie y Ubuntu 22.04, 24.04 y
  26.04), hora sincronizada, nombres de host correctos y
  sin Docker: Kubespray instala containerd.
- El firewall abierto entre nodos para 6443 (apiserver), 2379–2380 (etcd), 10250 (kubelet) y el
  tráfico de Cilium (8472/UDP si usa túnel VXLAN, 4240/TCP para sus chequeos de salud).

## Pasos

1. **Clonar**: `git clone https://github.com/kubernetes-sigs/kubespray.git` y hacé checkout del
   último tag estable. La matriz de versiones de Kubernetes está en el README de ese tag.
2. **Dependencias**: en un virtualenv, corré `pip install -r requirements.txt`. Instala la versión
   de Ansible que ese tag exige.
3. **Inventario**: copiá `inventory/sample` a `inventory/micluster` y editá `inventory.ini` con los
   nodos en los grupos `kube_control_plane`, `kube_node` y `etcd`. El generador
   `contrib/inventory_builder` ya no existe: se quitó en la v2.27.0.
4. **Variables del clúster**: en `inventory/micluster/group_vars/k8s_cluster/k8s-cluster.yml` poné
   `kube_network_plugin: cilium`.
5. **Variables de Cilium**: en `inventory/micluster/group_vars/k8s_cluster/k8s-net-cilium.yml` elegí el modo; los
   valores están en [Variables de Cilium en Kubespray](kubespray-variables-cilium.md).
6. **Desplegar**: corré `ansible-playbook -i inventory/micluster/inventory.ini cluster.yml -b -v`.
7. **Verificar**: en un control plane, con `sudo` o con `KUBECONFIG=/etc/kubernetes/admin.conf`,
   `kubectl get nodes -o wide` debe mostrar todos los nodos
   `Ready`, y `kubectl -n kube-system get pods` los pods de Cilium y CoreDNS `Running`. Con
   cilium-cli (se descarga de github.com/cilium/cilium-cli/releases), `cilium status` y `cilium connectivity test` prueban la red de punta a punta.
8. **Escalar**: agregá el nodo al inventario y corré
   `ansible-playbook -i inventory/micluster/inventory.ini scale.yml -b`. Para sacar uno,
   `ansible-playbook -i inventory/micluster/inventory.ini remove-node.yml -b -e node=<nombre>`.
9. **Resetear**: `ansible-playbook -i inventory/micluster/inventory.ini reset.yml -b -e reset_confirmation=yes` desinstala Kubernetes y el CNI de todos
   los nodos del inventario. Es destructivo.

## Cómo saber que salió bien

Todos los nodos están `Ready`, `cilium status` no muestra errores y `cilium connectivity test`
termina sin fallas. Para usar kubectl sin sudo, copiá `/etc/kubernetes/admin.conf` a
`~/.kube/config` con tu usuario como dueño.

## Relaciones

- Requiere: [Cilium](cilium.md) — hay que elegir el modo de red antes de configurar.
- Detallado por: [Variables de Cilium en Kubespray](kubespray-variables-cilium.md) — las variables exactas del paso 5.
- Ver también: Kubespray es un conjunto de playbooks de Ansible; Ansible todavía no tiene nota (pendiente en [DevOps](../DevOps/devops.md)).
