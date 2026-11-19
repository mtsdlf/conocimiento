---
resumen: >-
  Secretos es la parte de la infraestructura que decide dónde viven las claves y contraseñas que
  usan el aprovisionamiento y el clúster: cifradas dentro del repo o en un gestor que se lee al
  aplicar.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Secretos

Secretos es la parte de la infraestructura que decide dónde viven las claves y contraseñas que
usan el aprovisionamiento y el clúster: cifradas dentro del repo o en un gestor que se lee al
aplicar.

Dentro de la [infraestructura](../infraestructura.md), alimenta al
[Aprovisionamiento](../Aprovisionamiento/aprovisionamiento.md), donde el estado de Terraform es el
lugar en que un secreto se filtra sin avisar, y al
[Clúster de Kubernetes](../Cluster-de-kubernetes/cluster-de-kubernetes.md), donde Flux descifra los
Secrets al aplicar.

## En el repo o fuera del repo

Un secreto en texto plano en Git queda expuesto para siempre en el historial. Hay dos salidas. SOPS
cifra los valores del archivo y lo deja versionar junto al resto: lo descifra quien tiene la clave.
La otra es que el secreto nunca entre al repo: vive en un gestor, y Terraform lo lee al aplicar con
una identidad de corta vida, con valores ephemeral o argumentos write-only para que no quede en el
estado.

## Las dos notas de secretos

- [SOPS](sops.md) — cómo cifrar los valores de un archivo de configuración para guardarlo en Git y
  que GitOps lo descifre al aplicar.
- [Secretos en Terraform](secretos-en-terraform.md) — dónde viven los secretos y qué hace (y qué
  no) `sensitive`.
