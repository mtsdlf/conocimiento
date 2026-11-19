---
resumen: >-
  Una capacidad de plataforma es una función que la plataforma ofrece a sus usuarios, como pedir
  una base de datos o desplegar un servicio, con dueño, contrato y ciclo de vida propios e
  independiente de la tecnología que la implementa.
estado: borrador
estabilidad: estable
fuentes:
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
aliases: [Platform capability, Capability]
creado: 2026-10-03
revisado:
---

# Capacidad de plataforma

Una capacidad de plataforma es una función que la plataforma ofrece a sus usuarios, como pedir
una base de datos o desplegar un servicio, con dueño, contrato y ciclo de vida propios e
independiente de la tecnología que la implementa.

## Cambiar la tecnología sin romper a los usuarios

Pensar en capacidades y no en herramientas permite cambiar la tecnología sin romper a los
usuarios. Si el contrato es "pedir una base PostgreSQL con backups diarios", el equipo de
plataforma puede pasar de máquinas virtuales a un operador de Kubernetes sin que nadie cambie su
código.

## Interfaz, proveedor y lo que define una capacidad

El white paper de la CNCF separa dos cosas:

- **la interfaz de la capacidad**: lo que ven los usuarios (API, CLI, portal), que construye el
  equipo de plataforma;
- **el proveedor de la capacidad**: lo que la implementa por detrás, que conviene tomar de
  servicios externos siempre que se pueda (un servicio administrado de la nube, [Crossplane](crossplane.md),
  un operador).

Una capacidad bien definida tiene:

- **dueño**: un equipo responsable de su evolución y su soporte;
- **contrato**: una interfaz versionada y documentada;
- **ciclo de vida**: cómo se crea, se cambia, se da de baja y se reemplaza su backend;
- **límites**: quién puede pedirla y cuánto, según la [Gobernanza de plataforma](gobernanza-de-plataforma.md).

Las capacidades se agrupan en dominios según quién responde por ellas: identidad, recursos,
despliegue, observabilidad, seguridad. En un diagrama de plataforma, cada caja es una capacidad
con su dueño, no una tecnología.

## Secretos como capacidad

"Secretos" es una capacidad: crear, rotar y auditar credenciales por API. Hoy la implementa
HashiCorp Vault; si mañana se pasa a un gestor de secretos de la nube, la API y su contrato no
cambian.

## Capacidad no es herramienta

Terraform o ArgoCD son proveedores posibles de una capacidad; la capacidad es lo
que el usuario puede hacer ("desplegar mi servicio"), no el programa que lo hace.

## Ver también

- [Internal Developer Platform](internal-developer-platform.md): una IDP es un conjunto de capacidades.
- [Plataforma API-first](plataforma-api-first.md): cada capacidad se ofrece por una API.
- [Observabilidad](../Operacion-de-la-plataforma/observabilidad.md): Effective Platform Engineering propone ofrecerla como una capacidad de la plataforma.
