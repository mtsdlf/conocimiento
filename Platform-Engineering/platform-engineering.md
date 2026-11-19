---
tipo: mapa
resumen: >-
  Platform engineering es construir y operar plataformas internas para que los equipos de
  desarrollo entreguen software con autonomía, seguridad y menos carga cognitiva; este Mapa reúne
  las notas de Matías sobre organización de equipos, developer experience, la plataforma interna y
  el diagnóstico Dev–Ops.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# Platform Engineering

Platform engineering es construir y operar plataformas internas para que los equipos de
desarrollo entreguen software con autonomía, seguridad y menos carga cognitiva; este Mapa reúne
las notas de Matías sobre organización de equipos, developer experience, la plataforma interna y
el diagnóstico Dev–Ops.

Para aprenderlo en orden: [Platform engineering desde cero](recorrido-platform-engineering.md).

## Organización de equipos

- [Ley de Conway](ley-de-conway.md) — por qué el sistema copia la comunicación entre equipos; es la base del resto del grupo.
- [Maniobra inversa de Conway](maniobra-inversa-de-conway.md) — cómo diseñar los equipos para obtener la arquitectura buscada.
- [Número de Dunbar](numero-de-dunbar.md) — cuánta gente cabe en un equipo y en un grupo de equipos.
- [Team-first](team-first.md) — por qué el equipo estable, y no la persona, es la unidad de entrega.
- [Team Topologies](team-topologies.md) — el modelo de cuatro tipos de equipo y tres modos de interacción.
- [Stream-aligned team](stream-aligned-team.md) — el equipo principal, que entrega de punta a punta.
- [Platform team](platform-team.md) — el equipo que ofrece capacidades internas como producto.
- [Modo de interacción entre equipos](modo-de-interaccion-entre-equipos.md) — qué esperar de la relación entre dos equipos.

## Developer experience

- [Developer experience](developer-experience.md) — qué es DevEx y sus tres dimensiones.
- [Carga cognitiva](carga-cognitiva.md) — los tres tipos de carga y las técnicas para reducirla.
- [Mechanical sympathy](mechanical-sympathy.md) — por qué no conviene ocultarle todo al desarrollador.

## La plataforma interna

- [Internal Developer Platform](internal-developer-platform.md) — qué es una IDP y de qué partes se compone; la puerta de entrada al grupo.
- [Plataforma como producto](plataforma-como-producto.md) — qué cambia al tratar la plataforma como producto.
- [Capacidad de plataforma](capacidad-de-plataforma.md) — la unidad de lo que ofrece la plataforma, separada de la tecnología.
- [Self-service](self-service.md) — qué hace que pedir un recurso no necesite un ticket.
- [Plataforma API-first](plataforma-api-first.md) — por qué cada capacidad se expone primero como API.
- [Gobernanza de plataforma](gobernanza-de-plataforma.md) — cómo se da autonomía sin perder control ni trazabilidad.
- [Golden path](golden-path.md) — el camino estándar con plantillas para lo común.
- [Developer portal](developer-portal.md) — la interfaz web de la plataforma, como Backstage.
- [Crossplane](crossplane.md) — cómo ofrecer infraestructura como APIs declarativas sobre Kubernetes.

## Operar la plataforma

- [Observabilidad](observabilidad.md) — qué permite entender un sistema desde sus métricas, logs y traces, y en qué se diferencia del monitoreo.
- [Observability-driven development](observability-driven-development.md) — cómo hacer de la telemetría y las alertas un criterio de aceptación de cada ítem del backlog.

## Diagnóstico Dev–Ops

- [DevOps Topologies](devops-topologies.md) — los nueve Types y ocho Anti-Types de la relación Dev–Ops.
- [Anti-patrón del equipo DevOps](anti-patron-equipo-devops.md) — por qué un equipo "DevOps" intermedio se vuelve cuello de botella.
- [Evaluar la colaboración Dev–Ops de una organización](evaluar-la-colaboracion-dev-ops.md) — los pasos para diagnosticar una organización con entrevistas.
- [Cuestionario de colaboración Dev–Ops](cuestionario-de-colaboracion-dev-ops.md) — las 42 preguntas y la rúbrica, para usar en las entrevistas.

## Pendiente

- Service Catalog (registro de servicios, ownership y documentación): sin material todavía.
