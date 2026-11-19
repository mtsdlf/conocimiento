---
resumen: >-
  Gobernanza e identidad es la parte de Cloud que fija la base común de un entorno: la jerarquía de
  suscripciones, las reglas que cada recurso tiene que cumplir, quién puede hacer qué y cómo se
  despliega todo eso como código.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Gobernanza e identidad

Gobernanza e identidad es la parte de Cloud que fija la base común de un entorno: la jerarquía de
suscripciones, las reglas que cada recurso tiene que cumplir, quién puede hacer qué y cómo se
despliega todo eso como código.

Dentro de [Cloud](../cloud.md), es lo que todas las demás partes heredan. La red de la plataforma
es la [topología hub-and-spoke](../Redes/topologia-hub-and-spoke.md) de [Redes](../Redes/redes.md);
las identidades que se definen acá son las que usan el [cómputo](../Computo/computo.md) y los
pipelines; y las etiquetas que obliga una política son las que [FinOps](../FinOps/finops.md) usa
para repartir la factura.

## Plataforma y cargas de trabajo

Una landing zone separa lo compartido de lo de cada proyecto. La plataforma tiene las suscripciones
de identidad, de conectividad y de administración; cada carga de trabajo recibe su propia
suscripción bajo un management group que le aplica políticas. La jerarquía va de management groups
a suscripciones, grupos de recursos y recursos, y lo que se asigna arriba se hereda hacia abajo.

## Quién puede y cómo tiene que quedar

Dos mecanismos se reparten el control. Azure RBAC decide quién puede hacer una acción, con roles
altos que se activan por un rato con PIM y managed identities u OIDC en lugar de secretos. Azure
Policy decide cómo tiene que quedar el recurso, sin importar quién lo cree: un Owner tampoco puede
crear un Storage público si una política lo niega.

## Como código

La landing zone se despliega en stacks de Terraform con estado propio, uno por capa de plataforma
y uno por pieza de cada proyecto, que se leen entre sí por remote state y corren en orden desde un
pipeline que entra a Azure por OIDC.

## Las cuatro notas de gobernanza e identidad

- [Azure landing zone](azure-landing-zone.md) — qué trae la base común, cómo se reparte entre plataforma y proyectos y sus ocho áreas de diseño. Leerla primero.
- [Azure Policy](azure-policy.md) — definiciones, iniciativas, asignaciones y efectos para negar, auditar, modificar o desplegar lo que falta.
- [Identidad y acceso en Azure](identidad-y-acceso-en-azure.md) — Entra ID, RBAC, PIM, managed identities, OIDC y Key Vault.
- [Landing zone con Terraform](landing-zone-con-terraform.md) — cómo se parte la landing zone en stacks con estado propio y en qué orden se despliegan.
