---
resumen: >-
  Cilium es un CNI de Kubernetes basado en eBPF que conecta los pods, puede reemplazar a
  kube-proxy y aplica network policies, con ruteo por túnel (VXLAN) o nativo según la red de los
  nodos.
estado: borrador
estabilidad: estable
fuentes:
  - "Cilium, Introduction: https://docs.cilium.io/en/stable/overview/intro/"
  - "Cilium, Kubernetes without kube-proxy: https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/"
  - "Cilium, Routing: https://docs.cilium.io/en/stable/network/concepts/routing/"
  - "Cilium, 1.14 upgrade notes: https://docs.cilium.io/en/v1.14/operations/upgrade/"
  - "Cilium, PR #31286 (remueve strict/partial/disabled, sale en 1.16): https://github.com/cilium/cilium/pull/31286"
  - "Archivo/Infraestructura/kubespray-cilium.md"
aliases: [Cilium, CNI Cilium, kube-proxy replacement, KPR]
creado: 2026-10-03
revisado:
---

# Cilium

Cilium es un CNI de Kubernetes basado en eBPF que conecta los pods, puede reemplazar a
kube-proxy y aplica network policies, con ruteo por túnel (VXLAN) o nativo según la red de los
nodos.

## Red, balanceo y políticas en un solo componente

Un clúster de Kubernetes necesita un plugin de red (CNI) para que los pods tengan IP y se hablen
entre nodos. Cilium resuelve eso y, en el mismo componente, el balanceo de los Services, las
políticas de red hasta capa 7 y la observabilidad del tráfico con Hubble. Es un proyecto graduado
de la CNCF. Es quien aplica el [default-deny de red](default-deny-de-red-en-kubernetes.md).

## eBPF, reemplazo de kube-proxy y modos de ruteo

- **eBPF**: Cilium carga programas en el kernel de cada nodo que deciden qué hacer con cada
  paquete, en vez de cadenas largas de reglas de iptables.
- **Reemplazo de kube-proxy**: con `kubeProxyReplacement: true`, Cilium balancea los Services y
  kube-proxy no hace falta. Como sin kube-proxy no existe la ClusterIP del apiserver al arrancar, a
  Cilium hay que darle la dirección y el puerto reales del apiserver (`k8sServiceHost` y
  `k8sServicePort`). Los valores viejos `strict`, `partial` y `disabled` se deprecaron en 1.14 y
  se quitaron en 1.16: hoy el valor es `true` o `false`.
- **Ruteo por túnel** (el modo por defecto): los nodos arman una malla de túneles VXLAN (o Geneve)
  y el tráfico entre pods viaja encapsulado. Funciona en casi cualquier red, a cambio de 50 bytes
  de overhead por paquete con VXLAN, que bajan el MTU efectivo.
- **Ruteo nativo** (`routingMode: native`): los paquetes de los pods viajan sin encapsular, y la
  red tiene que saber rutear los CIDR de pods. Si todos los nodos están en el mismo segmento L2,
  `autoDirectNodeRoutes: true` alcanza; si no, las rutas las pone otro (BGP, la tabla de rutas de
  la nube o un router estático). En los dos casos se declara el rango que no se enmascara
  (`ipv4NativeRoutingCIDR`).

## Túnel o ruteo nativo según la red

Tres nodos en la misma VLAN de un homelab: ruteo nativo con `autoDirectNodeRoutes`, sin overhead
de túnel. Nodos en dos subredes de una nube sin rutas para los pods: túnel VXLAN. Kubespray instala Cilium
como CNI ([Desplegar Kubernetes con Kubespray](desplegar-kubernetes-con-kubespray.md)), y las
variables para cada modo están en [Variables de Cilium en Kubespray](kubespray-variables-cilium.md).

## Cilium y kube-proxy

Cilium no es kube-proxy, que solo implementa los Services con iptables o IPVS y no aplica políticas de red.
Cilium puede convivir con kube-proxy (`kubeProxyReplacement: false`) y seguir siendo el CNI.
