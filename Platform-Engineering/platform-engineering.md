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

Para aprenderlo en orden: [[recorrido-platform-engineering]].

## Organización de equipos

- [[ley-de-conway]] — por qué el sistema copia la comunicación entre equipos; es la base del resto del grupo.
- [[maniobra-inversa-de-conway]] — cómo diseñar los equipos para obtener la arquitectura buscada.
- [[numero-de-dunbar]] — cuánta gente cabe en un equipo y en un grupo de equipos.
- [[team-first]] — por qué el equipo estable, y no la persona, es la unidad de entrega.
- [[team-topologies]] — el modelo de cuatro tipos de equipo y tres modos de interacción.
- [[stream-aligned-team]] — el equipo principal, que entrega de punta a punta.
- [[platform-team]] — el equipo que ofrece capacidades internas como producto.
- [[modo-de-interaccion-entre-equipos]] — qué esperar de la relación entre dos equipos.

## Developer experience

- [[developer-experience]] — qué es DevEx y sus tres dimensiones.
- [[carga-cognitiva]] — los tres tipos de carga y las técnicas para reducirla.
- [[mechanical-sympathy]] — por qué no conviene ocultarle todo al desarrollador.

## La plataforma interna

- [[internal-developer-platform]] — qué es una IDP y de qué partes se compone; la puerta de entrada al grupo.
- [[plataforma-como-producto]] — qué cambia al tratar la plataforma como producto.
- [[capacidad-de-plataforma]] — la unidad de lo que ofrece la plataforma, separada de la tecnología.
- [[self-service]] — qué hace que pedir un recurso no necesite un ticket.
- [[plataforma-api-first]] — por qué cada capacidad se expone primero como API.
- [[gobernanza-de-plataforma]] — cómo se da autonomía sin perder control ni trazabilidad.
- [[golden-path]] — el camino estándar con plantillas para lo común.
- [[developer-portal]] — la interfaz web de la plataforma, como Backstage.
- [[crossplane]] — cómo ofrecer infraestructura como APIs declarativas sobre Kubernetes.

## Operar la plataforma

- [[observabilidad]] — qué permite entender un sistema desde sus métricas, logs y traces, y en qué se diferencia del monitoreo.
- [[observability-driven-development]] — cómo hacer de la telemetría y las alertas un criterio de aceptación de cada ítem del backlog.

## Diagnóstico Dev–Ops

- [[devops-topologies]] — los nueve Types y ocho Anti-Types de la relación Dev–Ops.
- [[anti-patron-equipo-devops]] — por qué un equipo "DevOps" intermedio se vuelve cuello de botella.
- [[evaluar-la-colaboracion-dev-ops]] — los pasos para diagnosticar una organización con entrevistas.
- [[cuestionario-de-colaboracion-dev-ops]] — las 42 preguntas y la rúbrica, para usar en las entrevistas.

## Pendiente

- Service Catalog (registro de servicios, ownership y documentación): sin material todavía.
