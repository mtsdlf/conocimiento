---
resumen: >-
  Azure Policy evalúa cada recurso contra reglas asignadas a un management group, una suscripción
  o un grupo de recursos y, según el efecto, lo niega, lo audita, lo modifica o despliega lo que
  le falta.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, What is Azure Policy?: https://learn.microsoft.com/en-us/azure/governance/policy/overview"
  - "Microsoft Learn, Azure Policy definitions effect basics: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Policy y pequeños ejemplos)"
aliases: [Azure Policy, política de Azure, initiative, policy set]
creado: 2026-10-03
revisado:
---

# Azure Policy

Azure Policy evalúa cada recurso contra reglas asignadas a un management group, una suscripción
o un grupo de recursos y, según el efecto, lo niega, lo audita, lo modifica o despliega lo que
le falta.

## Una regla que se cumple en la API

Una guía de "todo Storage sin acceso público" depende de que cada persona la recuerde. Una
política con efecto `deny` la hace cumplir en la API de Azure: el recurso que no cumple no se crea, venga del
portal, de Terraform o de un script. Son las reglas que heredan las suscripciones de una
[Azure landing zone](azure-landing-zone.md), y [Showback y chargeback](../FinOps/showback-y-chargeback.md) las usa para obligar las
etiquetas de asignación de costos.

## Definición, iniciativa, asignación y efectos

- **Definición**: una condición sobre las propiedades del recurso y un efecto.
- **Iniciativa** (policy set): un grupo de definiciones que se asigna junto, p. ej. un estándar
  de cumplimiento.
- **Asignación**: a un management group, una suscripción, un grupo de recursos o un recurso, y se
  hereda hacia abajo.
- **Efectos más usados**:

| Efecto | Qué hace |
|---|---|
| `deny` | Rechaza la creación o el cambio |
| `audit` | Lo permite y lo marca como no conforme |
| `modify` / `append` | Agrega o cambia propiedades, como etiquetas |
| `deployIfNotExists` | Despliega un recurso relacionado que falta, como el registro DNS de un private endpoint |
| `auditIfNotExists` | Marca si falta ese recurso relacionado |
| `denyAction` | Bloquea una acción, como borrar |
| `disabled` | Apaga la regla sin desasignarla |

- **Remediación**: lo ya existente no se corrige solo; una tarea de remediación aplica
  `deployIfNotExists` o `modify` a los recursos que estaban antes.

## Una iniciativa para el management group de proyectos

Una iniciativa asignada al management group de proyectos:

- `deny` si `publicNetworkAccess` está en `Enabled` en Storage, SQL o Cosmos DB.
- `modify` para heredar la etiqueta `centro-de-costo` del grupo de recursos.
- `deployIfNotExists` para crear el registro en la zona `privatelink.*` al crear un endpoint.

## Policy decide cómo, RBAC decide quién

Azure RBAC: decide **quién** puede hacer una acción. Policy decide **cómo** tiene que quedar el
recurso, sin importar quién lo cree. Un Owner tampoco puede crear un Storage público si una
política lo niega.

## Ver también

- [Policy as code](../../DevOps/DevSecOps/policy-as-code.md) — el mismo principio en el pipeline y en el clúster.
- [Gobernanza de plataforma](../../Platform-Engineering/Plataforma-interna/gobernanza-de-plataforma.md) — los límites del self-service.
