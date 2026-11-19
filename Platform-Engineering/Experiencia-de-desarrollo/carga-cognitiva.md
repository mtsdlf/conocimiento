---
resumen: >-
  La carga cognitiva es el esfuerzo mental total que se usa en la memoria de trabajo; en un equipo
  de software se divide en intrínseca, extrínseca y pertinente, y una plataforma busca reducir las
  dos primeras.
estado: borrador
estabilidad: estable
fuentes:
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), sección 3.3: https://livebook.manning.com/book/effective-platform-engineering/chapter-3/v-1/"
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 3: https://teamtopologies.com/book"
  - "John Sweller, Cognitive Load During Problem Solving: Effects on Learning, Cognitive Science 12 (1988): https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog1202_4"
aliases: [Cognitive load]
creado: 2026-10-03
revisado:
---

# Carga cognitiva

La carga cognitiva es el esfuerzo mental total que se usa en la memoria de trabajo; en un equipo
de software se divide en intrínseca, extrínseca y pertinente, y una plataforma busca reducir las
dos primeras.

## Lo que el entorno le quita al problema de negocio

Un equipo tiene un límite de información que puede sostener, y lo que gasta en el entorno no lo
tiene para el problema de negocio. Según Effective Platform Engineering, la carga extrínseca que
nadie atiende es desperdicio puro. [Team Topologies](../Organizacion-de-equipos/team-topologies.md) la usa para decidir cuánto software puede
poseer un equipo.

## Intrínseca, extrínseca y pertinente

John Sweller la definió en 1988 como el esfuerzo mental total usado en la memoria de trabajo. Team
Topologies distingue tres tipos:

| Tipo | Qué es | Ejemplo |
|---|---|---|
| Intrínseca | lo propio del problema | entender la recursión; desplegar en Kubernetes |
| Extrínseca | lo que impone el entorno o cómo se presenta la información | "¿cómo se desplegaba esto?"; un error poco claro; una tarea manual repetida |
| Pertinente (germane) | lo que pide aprender o rendir alto | modelar la lógica de negocio |

La intrínseca no se elimina, pero se reduce con onboarding automatizado y plantillas. La
extrínseca sí se puede eliminar dentro de la plataforma. El objetivo es dejar más espacio para la
pertinente.

Según Effective Platform Engineering, se mide de forma subjetiva (los desarrolladores reportan su
estado) o cuantitativa (mediciones estructuradas), y se reduce con tres técnicas:

- **aceleradores**: formas estándar y automatizadas de usar la plataforma, como un
  [Golden path](../Plataforma-interna/golden-path.md);
- **una fuente central** de documentación, recursos y feedback, como un [Developer portal](../Plataforma-interna/developer-portal.md);
- **democratizar los datos**: los mismos datos en todo el ciclo de vida, como trazas
  distribuidas que muestran dónde se traba un request.

## 300 líneas de YAML para desplegar

Un equipo que despliega editando a mano 300 líneas de YAML de Kubernetes carga con lo extrínseco.
Si la plataforma le da un despliegue de un comando, esa carga desaparece y queda la intrínseca: qué
servicio desplegar y cómo se comporta.

## Reducir carga no es ocultarlo todo

Una plataforma que esconde por completo el sistema de abajo le
quita también lo que necesita entender para escribir buen código: eso es [Mechanical sympathy](mechanical-sympathy.md).

## Ver también

- [Developer experience](developer-experience.md): la carga cognitiva es una de sus tres dimensiones.
