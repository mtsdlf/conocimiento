---
resumen: >-
  La maniobra inversa de Conway consiste en diseñar primero los equipos y sus interfaces para que
  la arquitectura de software deseada surja de esa estructura.
estado: borrador
estabilidad: estable
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 2 y 6: https://teamtopologies.com/book"
  - "Thoughtworks Technology Radar, Inverse Conway Maneuver (julio de 2014): https://www.thoughtworks.com/radar/techniques/inverse-conway-maneuver"
aliases: [Inverse Conway maneuver, Reverse Conway]
creado: 2026-10-03
revisado:
---

# Maniobra inversa de Conway

La maniobra inversa de Conway consiste en diseñar primero los equipos y sus interfaces para que
la arquitectura de software deseada surja de esa estructura.

## Elegir qué estructura copia el sistema

Si la [Ley de Conway](ley-de-conway.md) se cumple de todos modos, conviene elegir qué estructura va a copiar el
sistema en vez de pelear contra ella. La maniobra convierte una restricción en una herramienta de
diseño.

## Los cuatro criterios para trazar límites

Según Skelton y Pais, el término es de James Lewis, de Thoughtworks: la organización arma sus
equipos para que coincidan con la arquitectura que quiere, en vez de esperar que los equipos sigan
una arquitectura impuesta. Thoughtworks la sumó a su Technology Radar en julio de 2014 como
"evolucionar la estructura de equipos y de la organización para promover la arquitectura
deseada".

[Team Topologies](team-topologies.md) da cuatro criterios para trazar esos límites:

1. Elegir los límites del software según lo que un equipo puede sostener (ver [Team-first](team-first.md)).
2. Vigilar los monolitos ocultos y los acoplamientos en la cadena de entrega, como un pipeline o
   una base de datos compartidos.
3. Usar como límites los contextos acotados (bounded contexts) del dominio de negocio.
4. Considerar otros límites, como la frecuencia de cambio o el cumplimiento normativo, cuando el
   dominio no alcanza.

## Separar pagos empezando por el equipo

Una empresa quiere separar pagos como servicio independiente. Primero forma un equipo dueño de
pagos, con su propio backlog y una interfaz definida hacia los demás equipos. El servicio se
separa después, sobre ese límite, y los cambios de pagos dejan de esperar a otros equipos.

## Por qué no alcanza con cambiar el organigrama

Cambiar a quién reporta cada persona no cambia los caminos de
comunicación. La maniobra rediseña quién habla con quién y por qué interfaz; si eso no cambia, la
arquitectura tampoco.
