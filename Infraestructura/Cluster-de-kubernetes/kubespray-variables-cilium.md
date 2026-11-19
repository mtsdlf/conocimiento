---
resumen: >-
  Variables de Kubespray para usar Cilium como CNI, con y sin kube-proxy y con ruteo nativo o por
  túnel, copiadas el 2026-10-03 de Kubespray v2.32.0, con enlace a los archivos de ejemplo.
estado: borrador
estabilidad: volatil
fuentes:
  - "Kubespray v2.32.0, k8s-net-cilium.yml de ejemplo: https://github.com/kubernetes-sigs/kubespray/blob/v2.32.0/inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml"
  - "Kubespray v2.32.0, defaults del rol cilium: https://github.com/kubernetes-sigs/kubespray/blob/v2.32.0/roles/network_plugin/cilium/defaults/main.yml"
  - "Kubespray v2.32.0, plantilla de valores de Helm: https://github.com/kubernetes-sigs/kubespray/blob/v2.32.0/roles/network_plugin/cilium/templates/values.yaml.j2"
  - "Kubespray v2.32.0, versiones por defecto: https://github.com/kubernetes-sigs/kubespray/blob/v2.32.0/roles/kubespray_defaults/defaults/main/download.yml"
  - "Archivo/Infraestructura/kubespray-cilium.md"
aliases: [k8s-net-cilium.yml, variables de Cilium en Kubespray]
creado: 2026-10-03
revisado:
---

# Variables de Cilium en Kubespray

Variables de Kubespray para usar Cilium como CNI, con y sin kube-proxy y con ruteo nativo o por
túnel, copiadas el 2026-10-03 de Kubespray v2.32.0, con enlace a los archivos de ejemplo.

Cada variable corresponde a un modo de [Cilium](cilium.md), y el paso 5 de
[Desplegar Kubernetes con Kubespray](desplegar-kubernetes-con-kubespray.md) las usa.

## El archivo de ejemplo de Kubespray

El archivo de ejemplo es
[`inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml`](https://github.com/kubernetes-sigs/kubespray/blob/v2.32.0/inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml)
en el tag v2.32.0 (cambiando el tag en la URL se ve el de otra versión), y los valores por defecto
están en el rol `network_plugin/cilium`. Ante una versión nueva de
Kubespray, se relee ese archivo antes de copiar lo de abajo.

## Las variables, por modo

Copiados el 2026-10-03 de Kubespray v2.32.0, que instala Cilium 1.20.2 por defecto.

**`k8s-cluster.yml`**:

```yaml
kube_network_plugin: cilium
```

**`k8s-net-cilium.yml`, sin kube-proxy y con ruteo nativo** (todos los nodos en el mismo
segmento de red L2):

```yaml
cilium_kube_proxy_replacement: true
cilium_tunnel_mode: disabled          # disabled = routingMode: native en Helm
cilium_native_routing_cidr: "10.233.64.0/18"   # el CIDR de pods (kube_pods_subnet)
cilium_auto_direct_node_routes: true  # solo si todos los nodos comparten L2
cilium_enable_bpf_masquerade: true
cilium_enable_hubble: false          # true para ver el tráfico con Hubble
```

**`k8s-net-cilium.yml`, con kube-proxy y túnel** (redes sin rutas para los pods):

```yaml
cilium_kube_proxy_replacement: false
cilium_tunnel_mode: vxlan             # o geneve
```

| Variable | Por defecto | Qué controla |
|---|---|---|
| `cilium_kube_proxy_replacement` | `false` | `true` o `false`; con `true`, kubeadm no instala kube-proxy |
| `cilium_tunnel_mode` | `vxlan` | `vxlan`, `geneve` o `disabled` (ruteo nativo) |
| `cilium_native_routing_cidr` | `""` | rango que no se enmascara en ruteo nativo |
| `cilium_auto_direct_node_routes` | `false` | rutas directas entre nodos; requiere L2 común |
| `cilium_enable_bpf_masquerade` | `false` | masquerading con eBPF en lugar de iptables |
| `cilium_enable_hubble` | `false` | observabilidad del tráfico con Hubble |

Nombres que cambiaron respecto de guías de 2024 y anteriores: `cilium_kube_proxy_replacement:
strict` ya no es un valor documentado (es `true`); `cilium_bpf_masquerade` pasó a
`cilium_enable_bpf_masquerade`; `cilium_hubble_enabled` pasó a `cilium_enable_hubble`.

Sin kube-proxy, Cilium necesita la dirección real del apiserver (`k8sServiceHost` y
`k8sServicePort`); Kubespray la completa automáticamente, no hace falta declararla.
