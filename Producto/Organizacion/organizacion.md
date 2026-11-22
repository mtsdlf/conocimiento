---
resumen: >-
  La organización de producto es quién hace el trabajo de producto y cuánto se le delega: los roles que se reparten las decisiones y el tipo de equipo, desde el que recibe una lista de funcionalidades hasta el que recibe un problema para resolver.
estado: vigente
estabilidad: estable
fuentes:
  - "Ken Schwaber y Jeff Sutherland, The Scrum Guide (2020): https://scrumguides.org/scrum-guide.html"
  - "Marty Cagan, Product vs. Feature Teams (SVPG, 2019): https://www.svpg.com/product-vs-feature-teams/"
  - "ISPMA, Software Product Management Body of Knowledge: https://ispma.org/bok/"
  - "Pragmatic Institute Framework, según resúmenes: https://pragmaticinstitute.com/framework"
  - "Melegati et al., Product managers in software startups: A grounded theory, Information and Software Technology 174:107516 (2024), solo metadatos: https://doi.org/10.1016/j.infsof.2024.107516"
  - "DORA, Team experimentation: https://dora.dev/capabilities/team-experimentation/"
  - "Nielsen Norman Group, Teams aren't empowered: https://www.nngroup.com/articles/teams-arent-empowered/"
  - "Scrum.org, Product team empowerment anti-patterns, según el buscador: https://www.scrum.org/resources/blog/product-team-empowerment-anti-patterns"
  - "Producto/.investigacion/organizacion-y-fundamentos.md"
  - "Producto/.investigacion/posicion-contraria.md"
aliases: [organización de producto, product organization, equipos de producto]
creado: 2026-11-22
revisado: 2026-11-22
---

# Organización

La organización de producto es quién hace el trabajo de producto y cuánto se le delega: los roles que se reparten las decisiones y el tipo de equipo, desde el que recibe una lista de funcionalidades hasta el que recibe un problema para resolver.

Cruza todo el ciclo de [Producto](../producto.md). Decide quién escribe la [estrategia](../Estrategia/estrategia.md), quién hace el [descubrimiento](../Descubrimiento/descubrimiento.md) y quién ordena la [planificación](../Planificacion-y-entrega/planificacion-y-entrega.md). Un mismo método funciona distinto según a quién se le da: pedirle [resultados](../Estrategia/resultados-y-entregables.md) a un equipo que no puede elegir qué construir no cambia nada.

## Tres formas de cortar el trabajo de producto

El campo no se pone de acuerdo en qué es un "rol de producto", porque cada fuente corta por otro eje. El Scrum Guide define responsabilidades dentro de un equipo: el Product Owner es "accountable for maximizing the value of the product resulting from the work of the Scrum Team". Los marcos formales, ISPMA y Pragmatic Institute, dividen el dominio en actividades, como estrategia o lanzamiento, sin asignarlas a un cargo. Cagan, en SVPG, divide por modelo de equipo: lo que hace un product manager depende de si el equipo es empoderado o de funcionalidades.

| Corte | Fuente | Pregunta que contesta |
|---|---|---|
| Por rol | Scrum Guide 2020 | ¿Quién responde por el valor y por el backlog? |
| Por actividad | ISPMA, Pragmatic Institute | ¿Qué trabajo hay que hacer, lo haga quien lo haga? |
| Por modelo | Cagan (SVPG) | ¿Qué se le delega al equipo: un problema o una lista? |

En la práctica, un cargo con el mismo nombre hace cosas distintas en cada empresa. Melegati y coautores (2024), en una teoría fundamentada sobre startups, describen el rol de product manager como "multidisciplinary and ill-defined, dependent on the context" (según el abstract). Los cargos uno por uno, con el Product Owner de Scrum, product ops y product marketing, están en [roles de producto](roles-de-producto.md).

## El trío y lo que le toca a cada uno

En la escuela que ordena este tema, un producto lo hacen juntos los tres roles del [trío de producto](../Descubrimiento/descubrimiento-continuo.md#el-trío-de-producto), y cómo se reparten entre ellos los riesgos de una idea está en [cuatro riesgos](../Descubrimiento/cuatro-riesgos.md). Diseño se estudia en [UX](../../UX/ux.md).

## Qué se le delega al equipo

La decisión central de esta vertical es qué recibe un equipo. Cagan distingue tres tipos. Un equipo de entrega solo ejecuta. Un equipo de funcionalidades recibe "a prioritized list that is called the roadmap" y entrega lo que dice la lista. Un equipo de producto, al que esta base llama equipo empoderado, recibe un problema y es "empowered to figure out the best way to solve the problems they've been asked to solve", y se lo juzga por resultados.

La evidencia es escasa. DORA encontró que la libertad del equipo para probar ideas y cambiar especificaciones sin aprobación externa mejora el desempeño de entrega de software. Eso no prueba la tesis de Cagan sobre resultados de negocio.

> [!IMPORTANT]
> No hay estudios con método que comparen equipos empoderados con equipos de funcionalidades. La disputa es entre escuelas, todas con evidencia de practicante: Cagan (el equipo recibe problemas), Shape Up (un grupo chico moldea el trabajo y el equipo lo ejecuta en ciclos de seis semanas), Scrum (el Product Owner ordena el backlog) y "Founder Mode" de Paul Graham (el fundador se mete en los detalles). Cada posición, con sus críticas, está en [equipo empoderado](equipo-empoderado.md).

## Cómo falla la organización de producto

Las fallas que describen las fuentes se parecen. Un equipo con nombre de "empoderado" decide cosas que no importan, porque las dependencias con otros equipos le dejan poco margen (NN/g, sin datos). Un product manager termina haciendo gestión de proyecto: Cagan dice que en un equipo de funcionalidades "the product manager role is mainly project manager". Y la organización copia el vocabulario sin cambiar quién decide, lo que Scrum.org llama teatro: "aspiration without capability is just theater" (según el buscador).

La forma de los equipos dentro de una organización de software, con los tipos de equipo y cómo interactúan, se estudia en [Team Topologies](../../Platform-Engineering/Organizacion-de-equipos/team-topologies.md), del tema Platform Engineering.

## Lo que hay en Organización

- [Roles de producto](roles-de-producto.md): los cargos cruzados con las actividades y el modelo de equipo, con el product manager, el Product Owner de Scrum, product ops, product marketing y la diferencia con un project manager.
- [Equipo empoderado](equipo-empoderado.md): equipos empoderados, de funcionalidades y de entrega, con la evidencia de DORA y la disputa con founder mode.

## Qué falta

Faltan estas notas:

- Product ops a fondo: los tres pilares de Perri y Tilles, cuándo hace falta y su crítica como "teatro". Hoy se trata en pocas líneas dentro de [roles de producto](roles-de-producto.md).
- Escalar producto con varios equipos: cómo se reparte un producto entre equipos y quién cuida la coherencia del conjunto.
