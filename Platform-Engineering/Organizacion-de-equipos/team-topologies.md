---
resumen: >-
  Team Topologies es el modelo de Matthew Skelton y Manuel Pais que organiza la entrega de software
  con cuatro tipos de equipo y tres modos de interacción, para lograr un flujo rápido sin superar
  la carga cognitiva de cada equipo.
estado: borrador
estabilidad: estable
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019): https://teamtopologies.com/book"
  - "Team Topologies, Key concepts: https://teamtopologies.com/key-concepts"
aliases: [Team Topologies]
creado: 2026-10-03
revisado:
---

# Team Topologies

Team Topologies es el modelo de Matthew Skelton y Manuel Pais que organiza la entrega de software
con cuatro tipos de equipo y tres modos de interacción, para lograr un flujo rápido sin superar
la carga cognitiva de cada equipo.

## Por qué la entrega lineal no aguanta

El modelo anterior (silos funcionales, outsourcing, traspasos repetidos entre equipos) supone que
la entrega es lineal: especificación, diseño, desarrollo, test, release y operación. Según los
autores, esa secuencia no aguanta la velocidad de cambio actual. Team Topologies organiza equipos
estables según el flujo de trabajo: por área de negocio, no por conocimiento técnico.

## Cuatro tipos de equipo y tres modos de interacción

Parte de tres ideas: el equipo estable como unidad ([Team-first](team-first.md)), el límite de
[Carga cognitiva](../Experiencia-de-desarrollo/carga-cognitiva.md) de cada equipo y la [Ley de Conway](ley-de-conway.md). Sobre eso define cuatro tipos de
equipo:

| Tipo | Qué hace |
|---|---|
| [Stream-aligned](stream-aligned-team.md) | entrega valor de punta a punta en un flujo de trabajo del negocio; es el tipo principal |
| Enabling | ayuda a un stream-aligned a superar obstáculos o aprender una práctica, y detecta capacidades que faltan |
| Complicated-subsystem | se ocupa de una parte que pide matemática o una especialidad técnica profunda |
| [Platform](platform-team.md) | ofrece un producto interno que acelera la entrega de los demás |

Los otros tres tipos existen para bajar la carga de los stream-aligned. Una organización empieza
con varios stream-aligned y suma los demás cuando hacen falta. Los tipos se repiten a escala: un
grupo de equipos puede funcionar, como conjunto, de platform team para otros grupos.

La relación entre dos equipos se fija con un [Modo de interacción entre equipos](modo-de-interaccion-entre-equipos.md):
collaboration, X-as-a-Service o facilitating. La estructura cambia con el tiempo según las
señales que da la organización.

## Una tienda online con tres flujos

Una tienda online tiene tres stream-aligned (catálogo, checkout, logística), un platform team que
ofrece despliegue y bases de datos, y un enabling team que durante dos meses enseña pruebas de
contrato a checkout.

## El antecedente y la técnica de límites

[DevOps Topologies](../Colaboracion-Dev-Ops/devops-topologies.md), el catálogo anterior de los mismos autores, que solo
describe la relación entre Dev y Ops. Team Topologies lo generaliza a toda la organización de
equipos. La [Maniobra inversa de Conway](maniobra-inversa-de-conway.md) es la técnica que el modelo aplica al trazar límites.
