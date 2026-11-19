---
resumen: >-
  La experiencia de desarrollo es la parte del platform engineering que trata la fricción que viven
  los desarrolladores en su trabajo diario, el esfuerzo mental que les pide y hasta dónde conviene
  ocultarles el sistema de abajo.
estado: borrador
estabilidad: estable
fuentes:
  - "Abi Noda, Margaret-Anne Storey, Nicole Forsgren y Michaela Greiler, DevEx: What Actually Drives Productivity, ACM Queue (2023): https://queue.acm.org/detail.cfm?id=3595878"
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), sección 3.3: https://livebook.manning.com/book/effective-platform-engineering/chapter-3/v-1/"
creado: 2026-11-19
revisado:
---

# Experiencia de desarrollo

La experiencia de desarrollo es la parte del platform engineering que trata la fricción que viven
los desarrolladores en su trabajo diario, el esfuerzo mental que les pide y hasta dónde conviene
ocultarles el sistema de abajo.

Es lo que la [plataforma interna](../Plataforma-interna/plataforma-interna.md) intenta mejorar:
según internaldeveloperplatform.org, una IDP baja la carga cognitiva de los desarrolladores sin
quitarles el contexto que necesitan. La [organización de equipos](../Organizacion-de-equipos/organizacion-de-equipos.md)
usa el mismo límite, porque Team Topologies decide con la carga cognitiva cuánto software puede
poseer un equipo.

## Tres dimensiones y un límite

Noda, Storey, Forsgren y Greiler describen la developer experience con tres dimensiones: feedback
loops, carga cognitiva y flow state. El enfoque mide la fricción en lugar de contar la producción.

La carga cognitiva se divide en intrínseca, extrínseca y pertinente. La plataforma elimina la
extrínseca, reduce la intrínseca y deja más espacio para la pertinente. Según Effective Platform
Engineering, las técnicas son tres: aceleradores como un [golden path](../Plataforma-interna/golden-path.md),
una fuente central como un [developer portal](../Plataforma-interna/developer-portal.md) y los
mismos datos en todo el ciclo de vida.

El límite es la mechanical sympathy. Una plataforma que oculta del todo el sistema de abajo impide
entender cómo corre el software, y el código sale con menos performance y confiabilidad.

## Las tres notas de experiencia de desarrollo

- [Developer experience](developer-experience.md) — qué es DevEx y sus tres dimensiones, y cómo se mide.
- [Carga cognitiva](carga-cognitiva.md) — los tres tipos de carga y las técnicas para reducirla.
- [Mechanical sympathy](mechanical-sympathy.md) — por qué no conviene ocultarle todo al desarrollador.
