---
tipo: concepto
resumen: >-
  La gestión de secretos mantiene credenciales fuera del código y del historial: almacenes
  externos, secretos de vida corta, cifrado para GitOps (SOPS, Sealed Secrets) y detección antes
  del commit.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "OWASP Top 10 CI/CD Security Risks (CICD-SEC-6, Insufficient Credential Hygiene): https://owasp.org/www-project-top-10-ci-cd-security-risks/"
  - "SOPS: https://getsops.io/"
  - "Sealed Secrets: https://github.com/bitnami-labs/sealed-secrets"
  - "External Secrets Operator: https://external-secrets.io/latest/"
  - "Gitleaks: https://github.com/gitleaks/gitleaks"
  - "Archivo/DevOps/devsecops-pipeline-avanzado.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-advanced-collaboration.md (original, texto generado con IA)"
aliases: [Secrets management, Manejo de secretos, Credenciales]
parte_de: [devsecops]
requiere: [devsecops]
relacionado: [seguridad-en-el-pipeline, gitops]
---

# Gestión de secretos

La gestión de secretos mantiene credenciales fuera del código y del historial: almacenes
externos, secretos de vida corta, cifrado para GitOps (SOPS, Sealed Secrets) y detección antes
del commit.

## Por qué importa

Un secreto que entra a un commit queda en el historial aunque se borre después, y cualquiera
con acceso al repositorio o a una copia lo puede leer. El pipeline agrava el problema: tiene
credenciales para el registry, la nube y los entornos, y OWASP pone el manejo pobre de
credenciales entre los diez riesgos principales del CI/CD.

## Cómo funciona

- **Almacén externo**: los secretos viven en un gestor (HashiCorp Vault, AWS Secrets Manager,
  Azure Key Vault) y la aplicación o el pipeline los piden al ejecutarse. En Kubernetes, External
  Secrets Operator los copia del gestor a un Secret del clúster.
- **Vida corta y mínimo privilegio**: cada automatización usa su propia identidad, con permisos
  mínimos y credenciales que expiran o rotan solas. Una deploy key (una clave SSH que da acceso a un solo
  repositorio) de solo lectura es mejor que un token personal con acceso a todo.
- **Cifrado en Git para GitOps**: [GitOps](gitops.md) necesita declarar todo en Git, secretos incluidos.
  **SOPS** cifra los valores de un YAML o JSON y deja las claves legibles, con claves de age o PGP
  (herramientas de cifrado de archivos) o con un KMS de nube (el servicio que guarda y usa
  claves de cifrado, como AWS KMS). **Sealed Secrets** cifra un Secret con la clave pública de un controlador, y solo ese
  controlador, dentro del clúster destino, puede descifrarlo.
- **Detección**: un hook de pre-commit con Gitleaks frena el secreto antes del commit, y el
  mismo escaneo corre en CI por si alguien saltó el hook.
- **Si ya se filtró**: revocar y rotar el secreto enseguida. Borrar el commit o reescribir el
  historial no alcanza, porque el valor ya pudo copiarse en clones, forks o logs.

## Ejemplo

Un servicio necesita la contraseña de su base de datos. La contraseña está en Vault; en el
repositorio de configuración hay un ExternalSecret (el recurso de External Secrets Operator que
dice qué traer del gestor) que pide `db/pagos` de Vault. El
clúster crea el Secret al aplicarlo y el valor nunca pasa por Git ni por los logs del pipeline.

## No confundir con

**Configuración**: una URL o un nivel de log no son secretos y pueden ir en claro en Git.
Mezclarlos con secretos lleva a cifrar todo o a no cifrar nada.

## Relaciones

- Parte de y requiere: [DevSecOps](devsecops.md) — es uno de los dominios de seguridad del ciclo de entrega.
- Relacionado: [Seguridad en el pipeline](seguridad-en-el-pipeline.md) — la detección de secretos es su primer control.
- Relacionado: [GitOps](gitops.md) — GitOps obliga a declarar los secretos en Git sin exponerlos.
