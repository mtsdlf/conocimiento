---
resumen: >-
  Nombres y certificados es la parte de la infraestructura que hace alcanzable un servicio por su
  nombre y con TLS: qué IP resuelve cada red para el mismo nombre y cómo se prueba el control de un
  dominio para obtener un certificado.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Nombres y certificados

Nombres y certificados es la parte de la infraestructura que hace alcanzable un servicio por su
nombre y con TLS: qué IP resuelve cada red para el mismo nombre y cómo se prueba el control de un
dominio para obtener un certificado.

Dentro de la [infraestructura](../infraestructura.md), expone los servicios del
[Clúster de Kubernetes](../Cluster-de-kubernetes/cluster-de-kubernetes.md), donde cert-manager
resuelve los desafíos ACME.

## Dónde se cruzan el DNS y el certificado

Las dos notas se condicionan. Con split-horizon DNS, un nombre puede existir solo en la LAN; un
nombre así no es alcanzable desde internet y no se puede validar por HTTP-01, que exige servir un
token por el puerto 80. Para esos casos, o detrás de un túnel, conviene DNS-01, que publica el
token en un registro TXT.

## Las dos notas de nombres y certificados

- [Split-horizon DNS](split-horizon-dns.md) — por qué un mismo nombre resuelve distinto en la LAN
  y en internet, y su punto único de falla.
- [Desafío ACME HTTP-01](desafio-acme-http-01.md) — cómo prueba un dominio el desafío HTTP-01 y
  cuándo conviene DNS-01.
