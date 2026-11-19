---
tipo: concepto
resumen: >-
  SOPS cifra los valores de archivos YAML, JSON, ENV o INI con claves age, PGP o KMS y deja en claro
  los nombres de los campos, para guardar secretos en Git y que la herramienta de GitOps los
  descifre al aplicar.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "SOPS, documentación: https://getsops.io/docs/"
  - "SOPS, repo: https://github.com/getsops/sops"
  - "Flux, Manage Kubernetes secrets with SOPS: https://fluxcd.io/flux/guides/mozilla-sops/"
  - "home-k8, lessons/sops-placeholder-bombs.md: https://github.com/mtsdlf/home-k8/blob/main/docs/lessons/sops-placeholder-bombs.md"
  - "home-k8, runbooks/sops-placeholders.md: https://github.com/mtsdlf/home-k8/blob/main/docs/runbooks/sops-placeholders.md"
aliases: [SOPS, Secrets OPerationS, getsops]
parte_de: []
requiere: []
relacionado: [secretos-en-terraform]
---

# SOPS

SOPS cifra los valores de archivos YAML, JSON, ENV o INI con claves age, PGP o KMS y deja en claro
los nombres de los campos, para guardar secretos en Git y que la herramienta de GitOps los
descifre al aplicar.

## Por qué importa

En GitOps el estado del clúster vive en Git, pero un secreto en texto plano en Git queda expuesto
para siempre en el historial. SOPS permite versionar el secreto junto al resto de los manifiestos:
el diff muestra qué clave cambió sin mostrar su valor. Nació en Mozilla en 2015 y es proyecto
Sandbox de la CNCF desde 2023.

## Cómo funciona

- **Qué cifra**: solo los valores finales del árbol (no los mapas ni las listas que los
  contienen); los nombres de los campos quedan legibles, por eso no deben contener información
  sensible.
- **Con qué**: claves criptográficas de age, PGP, AWS KMS, GCP KMS, Azure Key Vault, HuaweiCloud
  KMS o el transit de HashiCorp Vault. Un `.sops.yaml` con `creation_rules` dice qué clave usar
  según la ruta del archivo; `sops --encrypt --in-place archivo.yaml` cifra un archivo con esa
  regla.
- **Integridad**: SOPS calcula un código de autenticación (MAC) sobre todos los valores,
  así que agregar o quitar un valor sin la clave se detecta al descifrar.
- **Al aplicar**: en Flux, la herramienta de GitOps que aplica al clúster lo que está en Git, el
  componente kustomize-controller descifra los Secrets justo antes de aplicarlos. Flux pide que en
  un Secret de Kubernetes se cifren solo `data` o `stringData`, lo que se configura con
  `encrypted_regex` en `.sops.yaml`; por defecto SOPS cifra todos los valores.

**Riesgo del placeholder**: SOPS cifra cualquier valor, también un texto de relleno como
`REPLACE_ME`. El archivo se cifra, Flux lo descifra, Kubernetes crea el Secret y el pod arranca sin
error. El primero que valida el valor es la aplicación, con un mensaje que no menciona el
placeholder. La defensa es buscar los placeholders en los Secrets del clúster después de cada
instalación inicial (bootstrap).

## Ejemplo

En el homelab `home-k8`, un `cookie_secret` de oauth2-proxy quedó con un placeholder de 22 bytes.
oauth2-proxy lo rechazó con "invalid cookie secret length: 22", porque espera 16, 24 o 32 bytes, y
encontrar la causa llevó tiempo. Ahora el bootstrap incluye una búsqueda del placeholder en los
Secrets decodificados.

## No confundir con

Sealed Secrets, que cifra con una clave que vive en el clúster y solo ese clúster descifra. SOPS
usa claves externas (age, KMS), y el mismo archivo se puede descifrar en otra máquina con la clave.

## Relaciones

- Relacionado: [Secretos en Terraform](secretos-en-terraform.md) — la alternativa de dejar el secreto en un gestor y leerlo al aplicar.
- Ver también: [GitOps](../DevOps/gitops.md) (DevOps) — SOPS es lo que permite guardar secretos en el repo de GitOps.
