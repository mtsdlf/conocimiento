---
tipo: concepto
resumen: >-
  Team Topologies es el modelo de Matthew Skelton y Manuel Pais que organiza la entrega de software
  con cuatro tipos de equipo y tres modos de interacción, para lograr un flujo rápido sin superar
  la carga cognitiva de cada equipo.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019): https://teamtopologies.com/book"
  - "Team Topologies, Key concepts: https://teamtopologies.com/key-concepts"
aliases: [Team Topologies]
parte_de: []
requiere: [team-first, carga-cognitiva, ley-de-conway]
relacionado: [devops-topologies, maniobra-inversa-de-conway]
---

# Team Topologies

Team Topologies es el modelo de Matthew Skelton y Manuel Pais que organiza la entrega de software
con cuatro tipos de equipo y tres modos de interacción, para lograr un flujo rápido sin superar
la carga cognitiva de cada equipo.

## Por qué importa

El modelo anterior (silos funcionales, outsourcing, traspasos repetidos entre equipos) supone que
la entrega es lineal: especificación, diseño, desarrollo, test, release y operación. Según los
autores, esa secuencia no aguanta la velocidad de cambio actual. Team Topologies organiza equipos
estables según el flujo de trabajo: por área de negocio, no por conocimiento técnico.

## Cómo funciona

Parte de tres ideas: el equipo estable como unidad ([[team-first]]), el límite de
[[carga-cognitiva]] de cada equipo y la [[ley-de-conway]]. Sobre eso define cuatro tipos de
equipo:

| Tipo | Qué hace |
|---|---|
| [[stream-aligned-team\|Stream-aligned]] | entrega valor de punta a punta en un flujo de trabajo del negocio; es el tipo principal |
| Enabling | ayuda a un stream-aligned a superar obstáculos o aprender una práctica, y detecta capacidades que faltan |
| Complicated-subsystem | se ocupa de una parte que pide matemática o una especialidad técnica profunda |
| [[platform-team\|Platform]] | ofrece un producto interno que acelera la entrega de los demás |

Los otros tres tipos existen para bajar la carga de los stream-aligned. Una organización empieza
con varios stream-aligned y suma los demás cuando hacen falta. Los tipos se repiten a escala: un
grupo de equipos puede funcionar, como conjunto, de platform team para otros grupos.

La relación entre dos equipos se fija con un [[modo-de-interaccion-entre-equipos]]:
collaboration, X-as-a-Service o facilitating. La estructura cambia con el tiempo según las
señales que da la organización.

## Ejemplo

Una tienda online tiene tres stream-aligned (catálogo, checkout, logística), un platform team que
ofrece despliegue y bases de datos, y un enabling team que durante dos meses enseña pruebas de
contrato a checkout.

## No confundir con

[[devops-topologies|DevOps Topologies]], el catálogo anterior de los mismos autores, que solo
describe la relación entre Dev y Ops. Team Topologies lo generaliza a toda la organización de
equipos. La [[maniobra-inversa-de-conway]] es la técnica que el modelo aplica al trazar límites.

## Relaciones

- Requiere: [[team-first]], [[carga-cognitiva]] y [[ley-de-conway]] — las tres ideas de las que parte.
- Incluye: [[stream-aligned-team]], [[platform-team]], [[modo-de-interaccion-entre-equipos]].
- Relacionado: [[devops-topologies]] — el antecedente acotado a Dev y Ops.
- Relacionado: [[maniobra-inversa-de-conway]] — cómo se eligen los límites entre equipos.
