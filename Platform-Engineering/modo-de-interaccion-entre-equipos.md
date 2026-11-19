---
tipo: concepto
resumen: >-
  Los modos de interacción de Team Topologies (collaboration, X-as-a-Service y facilitating)
  definen qué esperar de la relación entre dos equipos durante un período.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 7 y 8: https://teamtopologies.com/book"
  - "Team Topologies, Key concepts: https://teamtopologies.com/key-concepts"
aliases: [Team interaction modes, Modos de interacción]
parte_de: [team-topologies]
requiere: []
relacionado: []
---

# Modo de interacción entre equipos

Los modos de interacción de Team Topologies (collaboration, X-as-a-Service y facilitating)
definen qué esperar de la relación entre dos equipos durante un período.

## Por qué importa

Según la [Ley de Conway](ley-de-conway.md), la comunicación entre equipos termina en la arquitectura. Si no se
dice cómo se relacionan dos equipos, cada uno supone algo distinto: uno espera reuniones diarias y
el otro una API documentada. Nombrar el modo fija esas expectativas.

## Cómo funciona

| Modo | Qué pasa | Cuándo conviene |
|---|---|---|
| Collaboration | dos equipos trabajan juntos un tiempo definido para descubrir algo nuevo (una API, una práctica, una tecnología) | hay mucha incertidumbre |
| X-as-a-Service | un equipo ofrece algo y el otro lo consume, con poca interacción | lo ofrecido ya es estable |
| Facilitating | un equipo ayuda y acompaña a otro a superar un obstáculo o aprender una práctica | es el modo típico de un enabling team |

Los modos cambian con el tiempo. Un [Platform team](platform-team.md) suele empezar en collaboration con un
stream-aligned para diseñar una capacidad nueva y pasa a X-as-a-Service cuando la capacidad se
estabiliza. Una collaboration que no termina nunca indica que el límite entre los equipos está
mal puesto.

Según Skelton y Pais, la organización ajusta los modos y la estructura de equipos con lo que
observa (organizational sensing): el flujo de entrega, las señales de carga cognitiva, la salud y
la autonomía de los equipos, y los cambios que pide la arquitectura.

## Ejemplo

El platform team y el equipo de checkout colaboran seis semanas para definir cómo se piden colas
de mensajes. Cuando la API queda estable, checkout la consume como servicio y la relación pasa a
X-as-a-Service.

## No confundir con

La Team API de un equipo (descrita en [Team-first](team-first.md)), que es lo que el equipo ofrece: código,
documentación, canales. El modo es cómo se relacionan dos equipos concretos en un momento dado.

## Relaciones

- Parte de: [Team Topologies](team-topologies.md) — es uno de los dos ejes del modelo, junto con los tipos de equipo.
