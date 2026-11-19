---
resumen: >-
  La organización de equipos es la parte del platform engineering que decide cómo se arman los
  equipos que entregan software: de qué tamaño, quién es dueño de qué y cómo se relacionan entre sí.
estado: borrador
estabilidad: estable
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019): https://teamtopologies.com/book"
  - "Melvin E. Conway, How Do Committees Invent?, Datamation, abril de 1968: https://www.melconway.com/Home/Committees_Paper.html"
creado: 2026-11-19
revisado:
---

# Organización de equipos

La organización de equipos es la parte del platform engineering que decide cómo se arman los
equipos que entregan software: de qué tamaño, quién es dueño de qué y cómo se relacionan entre sí.

De acá salen las otras partes. El [platform team](platform-team.md), que construye la
[plataforma interna](../Plataforma-interna/plataforma-interna.md), es uno de los tipos de equipo
que define esta vertical. Recibe de [Experiencia de desarrollo](../Experiencia-de-desarrollo/experiencia-de-desarrollo.md)
el límite de [carga cognitiva](../Experiencia-de-desarrollo/carga-cognitiva.md) con que Team
Topologies decide cuánto software puede poseer un equipo. Y [Colaboración Dev–Ops](../Colaboracion-Dev-Ops/colaboracion-dev-ops.md)
diagnostica con DevOps Topologies, el antecedente de este modelo.

## Del equipo estable al modelo de cuatro tipos

Tres ideas sostienen la vertical. La ley de Conway dice que el sistema copia la estructura de
comunicación de quien lo diseña, y la maniobra inversa la usa a propósito: se diseñan primero los
equipos y sus interfaces para obtener la arquitectura buscada. Los números de Dunbar acotan el
tamaño de un equipo y de los grupos de equipos. Team-first pone al equipo estable como unidad de
entrega, con exactamente un equipo dueño por cada parte del sistema.

Team Topologies junta esas ideas con el límite de carga cognitiva. Define cuatro tipos de equipo
(stream-aligned, enabling, complicated-subsystem y platform) y tres modos de interacción
(collaboration, X-as-a-Service y facilitating). El stream-aligned es el tipo principal, y los
otros tres existen para bajarle la carga.

## Dónde se rompe la organización

Un equipo por capa técnica necesita a los otros para cualquier cambio, y la arquitectura termina
copiando esas capas. Un equipo de proyecto se disuelve al terminar la entrega y pierde la
continuidad del cuidado. Una collaboration que no termina nunca indica que el límite entre dos
equipos está mal puesto. Cambiar el organigrama sin cambiar quién habla con quién no cambia la
arquitectura.

## Las ocho notas de organización de equipos

- [Ley de Conway](ley-de-conway.md) — por qué el sistema copia la comunicación entre equipos; la base del resto.
- [Maniobra inversa de Conway](maniobra-inversa-de-conway.md) — diseñar los equipos para obtener la arquitectura buscada, con cuatro criterios para trazar límites.
- [Número de Dunbar](numero-de-dunbar.md) — cuánta gente cabe en un equipo, una tribu y una división.
- [Team-first](team-first.md) — por qué el equipo estable, y no la persona, es la unidad de entrega.
- [Team Topologies](team-topologies.md) — el modelo de cuatro tipos de equipo y tres modos de interacción.
- [Stream-aligned team](stream-aligned-team.md) — el equipo principal, que entrega de punta a punta.
- [Platform team](platform-team.md) — el equipo que ofrece capacidades internas como producto.
- [Modo de interacción entre equipos](modo-de-interaccion-entre-equipos.md) — qué esperar de la relación entre dos equipos y cuándo cambia.
