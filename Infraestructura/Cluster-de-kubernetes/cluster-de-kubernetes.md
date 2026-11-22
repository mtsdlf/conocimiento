---
resumen: >-
  El clúster de Kubernetes es la parte de la infraestructura donde corren las cargas: acá, cómo se
  instala con Kubespray, cómo Cilium conecta los pods y cómo una política default-deny limita con
  quién habla cada uno.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Clúster de Kubernetes

El clúster de Kubernetes es la parte de la infraestructura donde corren las cargas: acá, cómo se
instala con Kubespray, cómo Cilium conecta los pods y cómo una política default-deny limita con
quién habla cada uno.

Dentro de la [infraestructura](../infraestructura.md), corre sobre los recursos que crea el
[Aprovisionamiento](../Aprovisionamiento/aprovisionamiento.md); sus servicios se hacen alcanzables
con [Nombres y certificados](../Nombres-y-certificados/nombres-y-certificados.md). Lo que corre en
él lo aplica [GitOps](../../DevOps/Despliegue/gitops.md) desde Git, y sus Secrets llegan cifrados con
[SOPS](../../DevOps/DevSecOps/sops.md), como explica la
[gestión de secretos](../../DevOps/DevSecOps/gestion-de-secretos.md).

## La red del clúster se elige antes de instalar

Un clúster necesita un CNI para que los pods tengan IP y se hablen entre nodos. Con Cilium, la
decisión es el modo: túnel VXLAN, que funciona en casi cualquier red a cambio de overhead, o ruteo
nativo, que exige que la red sepa rutear los CIDR de pods; y con o sin kube-proxy. Esa decisión va
antes de configurar Kubespray, que instala Cilium como CNI.

## Cerrar el tráfico por defecto

Sin políticas, un pod habla con cualquier otro y con internet. Con default-deny, solo pasa lo
permitido, y apenas se activa hay que habilitar DNS, el apiserver para los controladores y cada
destino externo. El hueco está en el selector: los pods que la política no alcanza quedan afuera.

## Lo que hay adentro del clúster

- [Cilium](cilium.md) — el CNI basado en eBPF, el reemplazo de kube-proxy y los modos de ruteo.
  Leerla primero.
- [Default-deny de red en Kubernetes](default-deny-de-red-en-kubernetes.md) — qué implica prohibir
  todo el tráfico de un pod salvo lo permitido, y dónde quedan huecos.
- [Desplegar Kubernetes con Kubespray](desplegar-kubernetes-con-kubespray.md) — los pasos para
  instalar un clúster con Kubespray y Ansible.
- [Variables de Cilium en Kubespray](kubespray-variables-cilium.md) — ficha con las variables
  exactas de Kubespray v2.32.0 para Cilium, copiadas el 2026-10-03.
