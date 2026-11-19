---
tipo: concepto
resumen: >-
  La seguridad de la cadena de suministro de software asegura que cada artefacto desplegado sea
  el que salió del build esperado, con SBOM, firma y verificación de procedencia.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "SLSA, especificación v1.2: https://slsa.dev/spec/v1.2/"
  - "Sigstore, documentación: https://docs.sigstore.dev/"
  - "Sigstore, Verifying signatures (cosign verify): https://docs.sigstore.dev/cosign/verifying/verify/"
  - "Sigstore, gitsign: https://github.com/sigstore/gitsign"
  - "SPDX (ISO/IEC 5962:2021): https://spdx.dev/"
  - "CycloneDX (ECMA-424): https://cyclonedx.org/"
  - "Archivo/DevOps/devsecops-pipeline-avanzado.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
aliases: [Supply chain security, Seguridad de la cadena de suministro, SLSA, SBOM]
parte_de: [devsecops]
requiere: [devsecops]
relacionado: [seguridad-en-el-pipeline]
---

# Cadena de suministro de software

La seguridad de la cadena de suministro de software asegura que cada artefacto desplegado sea
el que salió del build esperado, con SBOM, firma y verificación de procedencia.

## Por qué importa

Un atacante no necesita romper la aplicación si puede cambiar una dependencia, el servidor de
build o la imagen en el registry (el servidor donde se guardan las imágenes de contenedor). Escanear el código no lo detecta: hay que probar de dónde
salió cada artefacto.

## Cómo funciona

La cadena se asegura con cuatro piezas:

- **SBOM** (Software Bill of Materials): la lista de componentes, versiones y licencias de un
  artefacto. Los dos formatos estándar son SPDX (ISO/IEC 5962:2021) y CycloneDX (ECMA-424).
- **Procedencia** (provenance): un documento firmado que dice qué build produjo el artefacto, a
  partir de qué commit y con qué parámetros.
- **Firma**: el artefacto y sus documentos se firman. Con Sigstore, **cosign** firma imágenes y
  **gitsign** firma commits y tags de Git. Ambos permiten firmar sin claves de larga vida: Fulcio
  emite un certificado corto atado a una identidad OIDC (la cuenta de la persona o la identidad
  que el proveedor de CI le da al pipeline) y Rekor registra la firma en un log
  público de solo agregado.
- **Attestation**: el SBOM y la procedencia se firman y se adjuntan a la imagen en el registry
  como attestations, para que quien la descargue los encuentre junto a ella.
- **Verificación**: antes de desplegar, se comprueba firma y procedencia; si fallan, el
  despliegue se bloquea, por ejemplo con un admission controller (ver [Policy as code](policy-as-code.md)).

**SLSA** (Supply-chain Levels for Software Artifacts, versión 1.2) ordena estas garantías en
niveles. El track de Build tiene cuatro: L0 sin requisitos, L1 con procedencia disponible, L2 con
plataforma de build endurecida y L3 con builds aislados. La versión 1.2 suma un track de Source
para los controles del sistema de control de versiones.

La procedencia firma el vínculo artefacto-commit de la [Trazabilidad de cambios](trazabilidad-de-cambios.md).

## Ejemplo

El pipeline construye una imagen, genera su SBOM con Syft (una herramienta que lista los componentes de una imagen en SPDX o
CycloneDX), lo adjunta como attestation y firma la imagen con cosign usando la
identidad OIDC del pipeline. El clúster acepta la imagen solo si pasa:

```bash
cosign verify registry.example.com/pagos@sha256:<digest> \
  --certificate-identity=<identidad-del-pipeline> \
  --certificate-oidc-issuer=<emisor-oidc>
```

## No confundir con

**Escaneo de dependencias (SCA)**: dice si un componente tiene vulnerabilidades conocidas. La
cadena de suministro dice si el artefacto es el que se construyó.

## Relaciones

- Parte de y requiere: [DevSecOps](devsecops.md) — es uno de los dominios de seguridad del ciclo de entrega.
- Relacionado: [Seguridad en el pipeline](seguridad-en-el-pipeline.md) — el pipeline produce el SBOM, la firma y la procedencia.
- Ver también: [Trazabilidad de cambios](trazabilidad-de-cambios.md) — el vínculo artefacto-commit que la procedencia firma.
- Ver también: [Policy as code](policy-as-code.md) — la regla que bloquea imágenes sin firma válida.
