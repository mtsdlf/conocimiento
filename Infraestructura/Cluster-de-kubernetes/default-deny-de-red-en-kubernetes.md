---
resumen: >-
  Con una política de red default-deny, todo tráfico de un pod está prohibido salvo lo permitido;
  obliga a habilitar DNS, el apiserver para los controladores y cada destino externo, y solo cubre
  los pods que su selector alcanza.
estado: borrador
estabilidad: estable
fuentes:
  - "Kubernetes, Network Policies: https://kubernetes.io/docs/concepts/services-networking/network-policies/"
  - "Kubernetes, Pod Security Admission: https://kubernetes.io/docs/concepts/security/pod-security-admission/"
  - "Cilium, Policy enforcement: https://docs.cilium.io/en/stable/security/policy/intro/"
  - "Cilium, Layer 3 (entities, toFQDNs): https://docs.cilium.io/en/stable/security/policy/layer3/"
  - "home-k8, lessons/cnp-apiserver-egress.md: https://github.com/mtsdlf/home-k8/blob/main/docs/lessons/cnp-apiserver-egress.md"
  - "home-k8, lessons/psa-vs-cnp.md: https://github.com/mtsdlf/home-k8/blob/main/docs/lessons/psa-vs-cnp.md"
  - "home-k8, lessons/b2-region-locking.md: https://github.com/mtsdlf/home-k8/blob/main/docs/lessons/b2-region-locking.md"
aliases: [default deny, network policy default-deny, deny por defecto]
creado: 2026-10-03
revisado:
---

# Default-deny de red en Kubernetes

Con una política de red default-deny, todo tráfico de un pod está prohibido salvo lo permitido;
obliga a habilitar DNS, el apiserver para los controladores y cada destino externo, y solo cubre
los pods que su selector alcanza.

## Acotar el daño de un pod comprometido

Sin ninguna política de red, un pod de Kubernetes puede hablar con cualquier otro pod y con internet. Si una
aplicación queda comprometida, nada le impide sacar datos. Default-deny invierte la regla: lo que
no está permitido no pasa, y el daño de un pod comprometido queda acotado.

## Qué se rompe al activarlo

Un pod queda aislado en una dirección (ingress o egress) cuando alguna política lo selecciona para
esa dirección; a partir de ahí solo pasa lo que alguna política permite. En [Cilium](cilium.md), el CNI que aplica estas políticas y aporta entidades y reglas por FQDN, una
`CiliumClusterwideNetworkPolicy` hace lo mismo para todo el clúster.

Tres cosas se rompen apenas se activa y hay que permitirlas:

- **DNS**: la propia documentación de Kubernetes avisa que un deny de egress también bloquea DNS.
- **El apiserver**: todo controlador (cert-manager, external-dns, operadores) lista y observa
  recursos por la API de Kubernetes. Sin egress al apiserver falla con timeouts. En Cilium se
  permite con la entidad `kube-apiserver`, sin depender de la IP.
- **Destinos externos por nombre**: una regla `toFQDNs` de Cilium permite un destino por nombre
  en vez de por IP. Funciona solo si el DNS del pod pasa por el proxy DNS de Cilium, es decir, si
  la política tiene además una regla L7 de DNS. `matchName` cubre un nombre exacto; los SDK de S3
  usan URLs `<bucket>.s3.<región>.<proveedor>`, así que hace falta además
  `matchPattern: "*.s3.<región>.<proveedor>"`. Sin él, el tráfico se corta con un timeout sin
  mensaje útil.

## El hueco del selector

Una política cluster-wide cubre solo los pods que su selector alcanza.
Es común excluir del deny a los namespaces de sistema, y una forma de hacerlo es seleccionar por la
etiqueta de namespace de Pod Security Admission: aplicar el deny donde
`pod-security.kubernetes.io/enforce` es `baseline` o `restricted`. El efecto lateral es que todo
namespace `privileged` queda afuera, y sus pods salen a cualquier lado. En esos namespaces, cada
aplicación necesita su propia política con su deny y sus permisos.

## Controladores sin apiserver en `home-k8`

En el homelab `home-k8`, al activar el deny cluster-wide, cert-manager, external-dns y reflector
fallaron con `dial tcp <ClusterIP del apiserver>:443: i/o timeout`. Una regla de egress a
`kube-apiserver` en cada uno lo resolvió.

## Default-deny y Pod Security Admission

Pod Security Admission es otra cosa: decide qué puede hacer un pod dentro del nodo (privilegios, volúmenes
del host), no con quién habla por la red.
