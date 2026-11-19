---
resumen: >-
  Especificación y prueba es la parte del desarrollo que fija qué se construye, para quién y
  cuándo está terminado, y lo convierte en casos de prueba verificables.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Especificación y prueba

Especificación y prueba es la parte del desarrollo que fija qué se construye, para quién y
cuándo está terminado, y lo convierte en casos de prueba verificables.

Dentro de [Desarrollo](../desarrollo.md), es lo primero: lo que se especifica acá es lo que después se
genera, se configura y se versiona. Algunas categorías de prueba vienen de patrones del tema
Arquitectura, como la [clave de idempotencia](../../Arquitectura/clave-de-idempotencia.md) y el
[multi-tenancy](../../Arquitectura/multi-tenancy.md).

## De la historia al caso de prueba

Una historia de usuario describe la funcionalidad desde quien la usa ("Como… quiero… para…") y se
cierra con criterios de aceptación que se verifican con un sí o un no. Si no entra en una
iteración, es una épica y se parte en historias.

Cada criterio de aceptación se convierte en uno o más casos de prueba. En una API REST, cada caso
sigue el mismo formato y la suite recorre una lista de categorías, del camino feliz a la
concurrencia. Los casos ambiguos (un campo desconocido, un `pageSize` excesivo) se fijan en el
contrato antes de escribir el resultado esperado.

## Las dos notas de especificación y prueba

- [Historia de usuario](historia-de-usuario.md) — cómo se describe una funcionalidad y sus criterios de aceptación;
  leerla antes de escribir el backlog de una funcionalidad.
- [Diseñar casos de prueba de una API](disenar-casos-de-prueba-de-api.md) — pasos para armar la suite de casos de una API REST.
