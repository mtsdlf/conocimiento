---
tipo: concepto
resumen: >-
  Un stream-aligned team es un equipo alineado a un flujo continuo de trabajo de un segmento del
  negocio, que construye y entrega valor de punta a punta sin pasarle trabajo a otros equipos.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 5: https://teamtopologies.com/book"
  - "Team Topologies, Key concepts: https://teamtopologies.com/key-concepts"
aliases: [Equipo alineado al flujo, Stream-aligned]
parte_de: [team-topologies]
requiere: []
relacionado: []
---

# Stream-aligned team

Un stream-aligned team es un equipo alineado a un flujo continuo de trabajo de un segmento del
negocio, que construye y entrega valor de punta a punta sin pasarle trabajo a otros equipos.

## Por qué importa

Es el tipo de equipo principal de [Team Topologies](team-topologies.md): los otros tres tipos existen para bajarle
la carga. Cada traspaso a otro equipo agrega una cola de espera; un equipo que hace todo el
recorrido entrega más rápido y aprende de lo que pasa en producción.

## Cómo funciona

Un **flujo** (stream) es el trabajo continuo alineado a un dominio de negocio. El equipo se
alinea a uno solo, que puede ser:

- un producto o servicio;
- un conjunto de funcionalidades;
- un recorrido de usuario (user journey);
- un tipo de usuario (persona).

El equipo tiene lo necesario para llevar un cambio desde la idea hasta producción y operarlo
después. Werner Vogels, de Amazon, lo resumió en "you build it, you run it": quien construye el
servicio lo corre.

Según Skelton y Pais, un equipo de SRE también puede ser stream-aligned: responde por la
confiabilidad de aplicaciones grandes en producción y trabaja sobre todo con los stream-aligned
que las desarrollan.

## Ejemplo

El equipo de checkout de una tienda online decide, construye, despliega y monitorea todo lo que
pasa entre "agregar al carrito" y "pago confirmado". Para la base de datos usa el servicio del
[Platform team](platform-team.md) sin esperar a nadie.

## No confundir con

Un equipo por capa técnica (frontend, backend, base de datos). Ese equipo necesita a los otros
para entregar cualquier cambio, y la [Ley de Conway](ley-de-conway.md) hace que la arquitectura copie esas capas.

## Relaciones

- Parte de: [Team Topologies](team-topologies.md) — es uno de sus cuatro tipos de equipo.
- Base de: [Platform team](platform-team.md) — la plataforma existe para servir a estos equipos.
