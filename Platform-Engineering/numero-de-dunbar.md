---
tipo: concepto
resumen: >-
  Los números de Dunbar son los límites aproximados de personas con las que alguien sostiene
  distintos grados de confianza (unas 5, 15, 50, 150 y 500); acotan el tamaño de los equipos y de
  los grupos de equipos.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 3: https://teamtopologies.com/book"
aliases: [Dunbar's number, Números de Dunbar]
parte_de: []
requiere: []
relacionado: []
---

# Número de Dunbar

Los números de Dunbar son los límites aproximados de personas con las que alguien sostiene
distintos grados de confianza (unas 5, 15, 50, 150 y 500); acotan el tamaño de los equipos y de
los grupos de equipos.

## Por qué importa

Un grupo que supera estos límites pierde confianza entre sus miembros y necesita más coordinación
formal: reuniones, aprobaciones, documentos de traspaso. Skelton y Pais usan los números para
fijar tamaños máximos de equipos y de agrupaciones de equipos.

## Cómo funciona

El número parte del trabajo del antropólogo Robin Dunbar, que estimó en unas 150 las relaciones
estables que una persona puede mantener. Team Topologies usa la serie extendida:

| Personas | Límite |
|---|---|
| ~5 | relaciones personales cercanas |
| ~15 | confianza profunda |
| ~50 | confianza mutua |
| ~150 | personas cuyas capacidades se pueden recordar |
| ~500 | relaciones sociales efectivas |

De esa serie, Team Topologies saca agrupaciones compatibles:

- **un equipo**: de 5 a 8 personas, según la experiencia de la industria;
- **una familia o "tribu"** de equipos: hasta 50 personas;
- **una división o línea de negocio**: hasta 150 personas.

Los límites valen también para la arquitectura: según los autores, si un grupo de equipos crece
por encima de un número, el software que posee conviene partirlo en el mismo punto.

## Ejemplo

Un área de 200 ingenieros se parte en dos divisiones de menos de 150 personas. Cada división se
organiza en tribus de hasta 50, y cada tribu en equipos de 5 a 8.

## No confundir con

La ley de Brooks, que se explica en [Team-first](team-first.md): Dunbar acota cuánta gente cabe en un grupo de
confianza; Brooks dice que sumar gente a un equipo no aumenta su capacidad de inmediato.

## Relaciones

- Base de: [Team-first](team-first.md) — de estos límites sale el tamaño de un equipo estable.
