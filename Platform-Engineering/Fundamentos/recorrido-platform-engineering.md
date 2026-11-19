---
resumen: >-
  Platform engineering desde cero, para quien conoce el desarrollo de software pero no el diseño
  de equipos ni de plataformas: de por qué los equipos se organizan como se organizan a cómo se
  diseña una plataforma interna y cómo se diagnostica la colaboración Dev–Ops.
estado: borrador
estabilidad: semi
creado: 2026-10-03
revisado:
---

# Platform engineering desde cero

Platform engineering desde cero, para quien conoce el desarrollo de software pero no el diseño
de equipos ni de plataformas: de por qué los equipos se organizan como se organizan a cómo se
diseña una plataforma interna y cómo se diagnostica la colaboración Dev–Ops.

El orden cruza las cinco partes del tema: arranca por la [organización de equipos](../Organizacion-de-equipos/organizacion-de-equipos.md) y la [experiencia de desarrollo](../Experiencia-de-desarrollo/experiencia-de-desarrollo.md), sigue por la [plataforma interna](../Plataforma-interna/plataforma-interna.md) y su [operación](../Operacion-de-la-plataforma/operacion-de-la-plataforma.md), y termina en la [colaboración Dev–Ops](../Colaboracion-Dev-Ops/colaboracion-dev-ops.md).

1. [Ley de Conway](../Organizacion-de-equipos/ley-de-conway.md) — va primero porque todo lo demás asume que el sistema copia a los equipos.
2. [Maniobra inversa de Conway](../Organizacion-de-equipos/maniobra-inversa-de-conway.md) — el uso deliberado de la ley anterior.
3. [Número de Dunbar](../Organizacion-de-equipos/numero-de-dunbar.md) — los límites de tamaño que necesita el paso siguiente.
4. [Team-first](../Organizacion-de-equipos/team-first.md) — el equipo estable como unidad, con el tamaño que fija Dunbar.
5. [Developer experience](../Experiencia-de-desarrollo/developer-experience.md) — el marco donde vive la carga cognitiva.
6. [Carga cognitiva](../Experiencia-de-desarrollo/carga-cognitiva.md) — el límite que Team Topologies y la plataforma intentan proteger.
7. [Team Topologies](../Organizacion-de-equipos/team-topologies.md) — reúne los tres pasos anteriores en un modelo de equipos.
8. [Stream-aligned team](../Organizacion-de-equipos/stream-aligned-team.md) — el tipo principal; los demás existen para servirlo.
9. [Modo de interacción entre equipos](../Organizacion-de-equipos/modo-de-interaccion-entre-equipos.md) — cómo se relacionan los equipos del modelo.
10. [Plataforma como producto](../Plataforma-interna/plataforma-como-producto.md) — el enfoque que distingue a un platform team de un equipo de infraestructura.
11. [Platform team](../Organizacion-de-equipos/platform-team.md) — el equipo que sirve a los stream-aligned con ese enfoque.
12. [Internal Developer Platform](../Plataforma-interna/internal-developer-platform.md) — lo que construye el platform team.
13. [Capacidad de plataforma](../Plataforma-interna/capacidad-de-plataforma.md) — la unidad de lo que ofrece la plataforma.
14. [Self-service](../Plataforma-interna/self-service.md) — cómo se consumen esas capacidades.
15. [Plataforma API-first](../Plataforma-interna/plataforma-api-first.md) — por qué cada capacidad se expone como API.
16. [Gobernanza de plataforma](../Plataforma-interna/gobernanza-de-plataforma.md) — los límites del self-service, aplicados en la API.
17. [Golden path](../Plataforma-interna/golden-path.md) — las plantillas que bajan la carga cognitiva.
18. [Developer portal](../Plataforma-interna/developer-portal.md) — dónde el desarrollador encuentra los golden paths y el catálogo.
19. [Mechanical sympathy](../Experiencia-de-desarrollo/mechanical-sympathy.md) — hasta dónde conviene que el golden path oculte lo de abajo.
20. [Crossplane](../Plataforma-interna/crossplane.md) — una forma concreta de implementar capacidades de infraestructura.
21. [Observabilidad](../Operacion-de-la-plataforma/observabilidad.md) — qué permite entender un sistema desde sus métricas, logs y traces, y en qué se diferencia del monitoreo.
22. [Observability-driven development](../Operacion-de-la-plataforma/observability-driven-development.md) — cómo hacer de la telemetría y las alertas un criterio de aceptación de cada ítem del backlog.
23. [DevOps Topologies](../Colaboracion-Dev-Ops/devops-topologies.md) — el vocabulario para diagnosticar organizaciones reales.
24. [Anti-patrón del equipo DevOps](../Colaboracion-Dev-Ops/anti-patron-equipo-devops.md) — el anti-patrón más común, visto con todo lo anterior.
25. [Evaluar la colaboración Dev–Ops de una organización](../Colaboracion-Dev-Ops/evaluar-la-colaboracion-dev-ops.md) — cómo aplicar el diagnóstico con entrevistas.

Para consultar: [Cuestionario de colaboración Dev–Ops](../Colaboracion-Dev-Ops/cuestionario-de-colaboracion-dev-ops.md).

**Al terminar**: podés explicar por qué una organización arma un platform team, qué debe ofrecer
su plataforma y cómo diagnosticar en qué punto está una organización. El siguiente paso es la entrada del tema,
[Platform Engineering](../platform-engineering.md).
