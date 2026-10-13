---
tipo: concepto
resumen: >-
  En Azure, Microsoft Entra ID autentica a personas y aplicaciones y Azure RBAC autoriza qué puede
  hacer cada una; las managed identities y la federación OIDC evitan guardar secretos, y Key Vault
  guarda los que no se pueden evitar.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Understand Azure role definitions: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions"
  - "Microsoft Learn, What is Privileged Identity Management?: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure"
  - "Microsoft Learn, Managed identities for Azure resources: https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview"
  - "Microsoft Learn, Migrate Key Vault to Azure RBAC: https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-migration"
  - "Microsoft Learn, Key Vault soft-delete overview: https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview"
  - "Microsoft Learn, Use GitHub Actions to connect to Azure (OpenID Connect): https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección AZURE PAAS, Key Vault)"
aliases: [Entra ID, Azure RBAC, managed identity, identidad administrada, PIM, Key Vault, workload identity federation]
parte_de: []
requiere: []
relacionado: []
---

# Identidad y acceso en Azure

En Azure, Microsoft Entra ID autentica a personas y aplicaciones y Azure RBAC autoriza qué puede
hacer cada una; las managed identities y la federación OIDC evitan guardar secretos, y Key Vault
guarda los que no se pueden evitar.

## Por qué importa

Una credencial filtrada da acceso a todo lo que su identidad puede tocar, durante todo lo que dure.
Un diseño sin secretos de larga vida y con permisos mínimos y temporales achica las dos cosas: qué
se puede tocar y por cuánto tiempo.

## Cómo funciona

- **Entra ID** (antes Azure AD): el directorio de usuarios, grupos, aplicaciones y service
  principals, con acceso condicional y MFA.
- **Azure RBAC**: un rol asignado a una identidad en un ámbito (management group, suscripción,
  grupo de recursos o recurso). Los permisos del **plano de control** (crear una cuenta de
  Storage) son distintos de los del **plano de datos** (leer un blob), y uno no da el otro.
- **PIM** (Privileged Identity Management): los roles altos no quedan asignados todo el tiempo; se
  activan por un rato, con aprobación y MFA.
- **Managed identities**: una identidad que Azure administra para un recurso, sin contraseña que
  rotar. La *system-assigned* vive y muere con el recurso; la *user-assigned* es independiente, se
  comparte entre recursos y es la que Microsoft recomienda hoy.
- **Federación OIDC** (workload identity federation): un pipeline de GitHub Actions, Azure DevOps
  o HCP Terraform presenta un token de su plataforma y Entra ID lo canjea por un token de Azure.
  No hay secreto guardado en el pipeline.
- **Key Vault**: guarda secretos, claves y certificados. El modelo de permisos recomendado es
  RBAC, no las access policies. El borrado suave está siempre activo (retención configurable de 7 a
  90 días); la protección contra purga impide borrar definitivamente un secreto o el vault antes de
  que termine esa retención, es opcional, no se desactiva una vez activa y conviene en producción.

## Ejemplo

Una API en App Service lee la cadena de conexión de Key Vault con su managed identity, que tiene
el rol *Key Vault Secrets User* solo sobre ese vault. El pipeline que la despliega entra a Azure
por OIDC con un rol *Contributor* limitado al grupo de recursos. Nadie tiene una contraseña de
servicio en un archivo.

## No confundir con

[[azure-policy]]: RBAC decide quién puede hacer algo; Policy decide cómo tiene que quedar el
recurso, sin importar quién lo haga.

## Relaciones

- La usa: [[azure-landing-zone]] — identidad y acceso es una de sus áreas de diseño.
- La usa: [[landing-zone-con-terraform]] — el pipeline entra a Azure por OIDC.
- En otro Tema: [[gestion-de-secretos]] — secretos fuera del código en general;
  [[desplegar-en-aks-con-azure-pipelines]] — una service connection con federación de identidad.
