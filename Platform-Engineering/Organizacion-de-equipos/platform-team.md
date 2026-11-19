---
resumen: >-
  Un platform team es un equipo que ofrece capacidades internas como un producto, para que los
  stream-aligned teams entreguen con autonomía y con menos carga cognitiva.
estado: borrador
estabilidad: estable
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 5 y 8: https://teamtopologies.com/book"
  - "Team Topologies, Key concepts: https://teamtopologies.com/key-concepts"
aliases: [Equipo de plataforma, Platform]
creado: 2026-10-03
revisado:
---

# Platform team

Un platform team es un equipo que ofrece capacidades internas como un producto, para que los
stream-aligned teams entreguen con autonomía y con menos carga cognitiva.

## Resolver una vez para todos los stream-aligned

Si cada [Stream-aligned team](stream-aligned-team.md) tiene que montar su propia base de datos, su pipeline y su
monitoreo, gasta su carga cognitiva en lo que no es su negocio. El platform team resuelve eso una
vez para todos, como servicio.

## Qué ofrece y cómo se relaciona

[Team Topologies](team-topologies.md) lo define como un grupo de equipos que ofrece "un producto interno convincente
para acelerar la entrega". Según los autores, los equipos de producto necesitan autonomía para
provisionar sus propios entornos y recursos; el foco del platform team es dar servicios
self-service de calidad que cubran esas necesidades y, a la vez, el control de riesgo y
cumplimiento que pide la organización.

Para lograrlo, el platform team:

- trata lo que ofrece como un producto, con usuarios internos y feedback
  ([Plataforma como producto](../Plataforma-interna/plataforma-como-producto.md));
- se relaciona con los stream-aligned sobre todo en modo X-as-a-Service, y en modo collaboration
  cuando descubre una capacidad nueva con ellos (ver [Modo de interacción entre equipos](modo-de-interaccion-entre-equipos.md));
- construye y opera la [Internal Developer Platform](../Plataforma-interna/internal-developer-platform.md).

Según Skelton y Pais, el modelo funciona solo con madurez técnica y cultural, escala suficiente
y disciplina de ingeniería; no todas las organizaciones lo necesitan desde el principio.

## Una base PostgreSQL por API

El platform team de una empresa ofrece "pedir una base PostgreSQL" por API. Un stream-aligned la
pide, la recibe en minutos con backups y monitoreo, y el platform team mide cuántos equipos la
usan y qué les falta.

## Cuándo deja de ser un platform team

Si los equipos le piden despliegues por ticket y el
platform team los ejecuta, cayó en el [Anti-patrón del equipo DevOps](../Colaboracion-Dev-Ops/anti-patron-equipo-devops.md).
