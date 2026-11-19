---
tipo: concepto
resumen: >-
  Team-first es el principio de que el equipo estable de cinco a nueve personas, y no el
  individuo, es la unidad de entrega y de ownership del software; cada parte del sistema tiene
  exactamente un equipo dueño.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 3: https://teamtopologies.com/book"
aliases: [Team-first thinking, Equipo como unidad de entrega]
parte_de: []
requiere: [numero-de-dunbar]
relacionado: []
---

# Team-first

Team-first es el principio de que el equipo estable de cinco a nueve personas, y no el
individuo, es la unidad de entrega y de ownership del software; cada parte del sistema tiene
exactamente un equipo dueño.

## Por qué importa

El trabajo asignado a individuos se coordina persona a persona y se pierde cuando alguien se va.
Según Skelton y Pais, un equipo cohesionado rinde varias veces más que sus integrantes por
separado, y por eso el trabajo se asigna solo a equipos.

## Cómo funciona

**Tamaño**: de cinco a nueve personas, según los [números de Dunbar](numero-de-dunbar.md).

**Estabilidad**: un equipo tarda de dos semanas a tres meses o más en cohesionarse. La ley de
Brooks advierte que sumar gente no aumenta la capacidad de inmediato. El modelo de Tuckman
describe cuatro etapas (forming, storming, norming, performing), pero Pamela Knight encontró que
el storming ocurre durante toda la vida del equipo, no solo al principio. Por eso se evita armar
equipos por proyecto y mover gente entre ellos.

**Ownership**: cada componente, librería o servicio tiene exactamente un equipo dueño; no hay
ownership compartido. El dueño da "continuidad del cuidado" y puede pensar en tres horizontes:
resultados del año, crecimiento de los próximos períodos y experimentos a muchos meses.

**Motivación**: Daniel Pink describe tres motores de la motivación intrínseca: autonomía,
maestría y propósito. Según Team Topologies, un equipo que atiende pedidos de muchos equipos
pierde autonomía, uno que cubre demasiadas tecnologías pierde maestría y uno con demasiados
dominios pierde propósito.

**Team API**: lo que un equipo ofrece a los demás (código, versionado, documentación, prácticas y
canales de comunicación) se diseña pensando en que otros equipos lo usen.

## Ejemplo

En lugar de asignar "migrar el login" a dos personas sueltas, la tarea va al equipo dueño de
identidad, que la prioriza en su backlog y responde por el servicio después de la migración.

## No confundir con

Un equipo de proyecto, que se arma para una entrega y se disuelve. Team-first pide equipos
duraderos a los que llega el trabajo, no gente que se reparte entre proyectos.

## Relaciones

- Requiere: [Número de Dunbar](numero-de-dunbar.md) — de ahí sale el tamaño del equipo.
- Base de: [Team Topologies](team-topologies.md) — el modelo da por sentado al equipo estable como unidad.
