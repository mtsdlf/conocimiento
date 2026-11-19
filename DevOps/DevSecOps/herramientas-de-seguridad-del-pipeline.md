---
resumen: >-
  Las herramientas habituales para cada control de seguridad del pipeline (Gitleaks, Semgrep,
  Trivy, Checkov, ZAP, OPA/Conftest, Falco, Syft), con la fecha de la copia.
estado: borrador
estabilidad: volatil
fuentes:
  - "Gitleaks: https://github.com/gitleaks/gitleaks"
  - "Semgrep: https://docs.semgrep.dev/"
  - "Trivy: https://trivy.dev/"
  - "Checkov: https://www.checkov.io/"
  - "TerraGoat: https://github.com/bridgecrewio/terragoat"
  - "ZAP: https://www.zaproxy.org/"
  - "Conftest: https://www.conftest.dev/"
  - "Falco: https://falco.org/"
  - "Syft: https://github.com/anchore/syft"
  - "Archivo/DevOps/devsecops-pipeline-avanzado.md (original, texto generado con IA)"
aliases: [Herramientas DevSecOps]
creado: 2026-10-03
revisado:
---

# Herramientas de seguridad del pipeline

Las herramientas habituales para cada control de seguridad del pipeline (Gitleaks, Semgrep,
Trivy, Checkov, ZAP, OPA/Conftest, Falco, Syft), con la fecha de la copia.

## Dónde se consulta cada herramienta

Cada herramienta tiene su documentación oficial, enlazada en `fuentes`. Esta ficha solo dice
qué control cubre cada una; las opciones y versiones se consultan allí.

## Qué control cubre cada herramienta

Copiado el 2026-10-03 de la documentación de cada proyecto. Todas son de código abierto.

Siglas de la tabla (cada control se explica en [Seguridad en el pipeline](seguridad-en-el-pipeline.md)):

- **SAST**: análisis estático del código propio, sin ejecutarlo.
- **SCA**: análisis de las dependencias de terceros y sus vulnerabilidades.
- **DAST**: pruebas contra la aplicación en ejecución.
- **IaC**: infraestructura como código (Terraform, Helm, manifiestos de Kubernetes).
- **CVE**: identificador público de una vulnerabilidad conocida.
- **SBOM**: lista de componentes de un artefacto; ver [Cadena de suministro de software](cadena-de-suministro-de-software.md).
- **Rego**: el lenguaje de políticas de OPA; ver [Policy as code](policy-as-code.md).

| Control | Herramienta | Qué hace |
|---|---|---|
| Secretos | Gitleaks | busca contraseñas, claves y tokens en repositorios y archivos; corre como hook de pre-commit o en CI |
| SAST | Semgrep | análisis estático con reglas; la plataforma suma SCA y detección de secretos |
| SCA, imagen, IaC | Trivy | escanea repositorios, imágenes, artefactos y clústeres de Kubernetes; encuentra CVE y configuraciones inseguras, y genera SBOM |
| IaC | Checkov | escanea Terraform, CloudFormation, Kubernetes, Helm, plantillas ARM y otros antes de aplicarlos |
| DAST | ZAP (Zed Attack Proxy) | escáner de aplicaciones web en ejecución; hoy lo patrocina Checkmarx |
| Policy gate | OPA con Conftest | evalúa archivos de configuración contra políticas en Rego; ver [Policy as code](policy-as-code.md) |
| Ejecución | Falco | detecta comportamiento anómalo en hosts, contenedores y Kubernetes a partir de eventos del kernel |
| SBOM | Syft | genera el SBOM de una imagen o un sistema de archivos en SPDX o CycloneDX |

Para empezar alcanza con poco: Gitleaks como hook y en CI, y Trivy sobre el repositorio y la
imagen, cubren secretos, dependencias, IaC e imagen con dos herramientas. Es una inferencia
propia a partir de lo que cubre cada una, no una recomendación de las fuentes.

**TerraGoat no es un escáner.** Es un repositorio de Terraform vulnerable a propósito, para
practicar y probar escáneres como Checkov. No se ejecuta en un pipeline real ni se despliega.

Las herramientas de firma (cosign, gitsign) están en [Cadena de suministro de software](cadena-de-suministro-de-software.md), y
las de secretos para GitOps (SOPS, Sealed Secrets) en [Gestión de secretos](gestion-de-secretos.md).
