---
tipo: concepto
resumen: >-
  La ley de Conway dice que una organización que diseña un sistema produce un diseño que copia su
  estructura de comunicación; por eso la forma en que se comunican los equipos limita las
  arquitecturas posibles.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Melvin E. Conway, How Do Committees Invent?, Datamation, abril de 1968: https://www.melconway.com/Home/Committees_Paper.html"
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 2: https://teamtopologies.com/book"
aliases: [Conway's law, Ley de Conway]
parte_de: []
requiere: []
relacionado: []
---

# Ley de Conway

La ley de Conway dice que una organización que diseña un sistema produce un diseño que copia su
estructura de comunicación; por eso la forma en que se comunican los equipos limita las
arquitecturas posibles.

## Por qué importa

Una arquitectura que no coincide con la comunicación real entre equipos no se sostiene: el sistema
termina copiando cómo se habla la gente. Según Skelton y Pais, el diseño de la organización acota
el "espacio de búsqueda de soluciones" del software antes de que alguien dibuje un diagrama.

## Cómo funciona

Melvin Conway la formuló en 1968, en el artículo "How Do Committees Invent?": las organizaciones
que diseñan sistemas están obligadas a producir diseños que copian sus estructuras de
comunicación. Eric S. Raymond la resumió así: si cuatro grupos trabajan en un compilador, sale un
compilador de cuatro pasadas.

La estructura que cuenta no es solo el organigrama. Niels Pflaeging, citado en Team Topologies,
distingue tres estructuras:

- **formal**: el organigrama, que sirve para el cumplimiento;
- **informal**: la influencia entre personas;
- **de creación de valor**: cómo se hace el trabajo de verdad, según la reputación entre personas
  y entre equipos.

Las personas hablan con quien necesitan para terminar su trabajo, no con quien marca la línea del
organigrama. Esa comunicación real es la que el sistema copia.

Más comunicación no siempre es mejor. Según Team Topologies, la comunicación de todos con todos
tiende a producir sistemas monolíticos, enredados y acoplados, que no permiten un flujo rápido.
Por eso conviene definir interfaces entre equipos que digan qué trabajo pide colaboración
estrecha y cuál no.

## Ejemplo

Tres equipos separados por capa (frontend, backend y base de datos) que se coordinan por tickets
terminan con tres capas de contratos rígidos, aunque el producto pida cortes por funcionalidad.

## No confundir con

La [[maniobra-inversa-de-conway]] es el uso deliberado de esta ley: diseñar primero los equipos
para obtener la arquitectura buscada. La ley describe lo que pasa; la maniobra actúa sobre eso.

## Relaciones

- Base de: [[maniobra-inversa-de-conway]] — la maniobra aplica esta ley al revés.
- Base de: [[team-topologies]] — el modelo diseña equipos contando con que el sistema los va a copiar.
