---
tipo: recorrido
resumen: >-
  Platform engineering desde cero, para quien conoce el desarrollo de software pero no el diseño
  de equipos ni de plataformas: de por qué los equipos se organizan como se organizan a cómo se
  diseña una plataforma interna y cómo se diagnostica la colaboración Dev–Ops.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [platform-engineering]
---

# Platform engineering desde cero

Platform engineering desde cero, para quien conoce el desarrollo de software pero no el diseño
de equipos ni de plataformas: de por qué los equipos se organizan como se organizan a cómo se
diseña una plataforma interna y cómo se diagnostica la colaboración Dev–Ops.

1. [Ley de Conway](ley-de-conway.md) — va primero porque todo lo demás asume que el sistema copia a los equipos.
2. [Maniobra inversa de Conway](maniobra-inversa-de-conway.md) — el uso deliberado de la ley anterior.
3. [Número de Dunbar](numero-de-dunbar.md) — los límites de tamaño que necesita el paso siguiente.
4. [Team-first](team-first.md) — el equipo estable como unidad, con el tamaño que fija Dunbar.
5. [Developer experience](developer-experience.md) — el marco donde vive la carga cognitiva.
6. [Carga cognitiva](carga-cognitiva.md) — el límite que Team Topologies y la plataforma intentan proteger.
7. [Team Topologies](team-topologies.md) — reúne los tres pasos anteriores en un modelo de equipos.
8. [Stream-aligned team](stream-aligned-team.md) — el tipo principal; los demás existen para servirlo.
9. [Modo de interacción entre equipos](modo-de-interaccion-entre-equipos.md) — cómo se relacionan los equipos del modelo.
10. [Plataforma como producto](plataforma-como-producto.md) — el enfoque que distingue a un platform team de un equipo de infraestructura.
11. [Platform team](platform-team.md) — el equipo que sirve a los stream-aligned con ese enfoque.
12. [Internal Developer Platform](internal-developer-platform.md) — lo que construye el platform team.
13. [Capacidad de plataforma](capacidad-de-plataforma.md) — la unidad de lo que ofrece la plataforma.
14. [Self-service](self-service.md) — cómo se consumen esas capacidades.
15. [Plataforma API-first](plataforma-api-first.md) — por qué cada capacidad se expone como API.
16. [Gobernanza de plataforma](gobernanza-de-plataforma.md) — los límites del self-service, aplicados en la API.
17. [Golden path](golden-path.md) — las plantillas que bajan la carga cognitiva.
18. [Developer portal](developer-portal.md) — dónde el desarrollador encuentra los golden paths y el catálogo.
19. [Mechanical sympathy](mechanical-sympathy.md) — hasta dónde conviene que el golden path oculte lo de abajo.
20. [Crossplane](crossplane.md) — una forma concreta de implementar capacidades de infraestructura.
21. [DevOps Topologies](devops-topologies.md) — el vocabulario para diagnosticar organizaciones reales.
22. [Anti-patrón del equipo DevOps](anti-patron-equipo-devops.md) — el anti-patrón más común, visto con todo lo anterior.
23. [Evaluar la colaboración Dev–Ops de una organización](evaluar-la-colaboracion-dev-ops.md) — cómo aplicar el diagnóstico con entrevistas.

Para consultar: [Cuestionario de colaboración Dev–Ops](cuestionario-de-colaboracion-dev-ops.md).

**Al terminar**: podés explicar por qué una organización arma un platform team, qué debe ofrecer
su plataforma y cómo diagnosticar en qué punto está una organización. El siguiente paso es el Mapa
[Platform Engineering](platform-engineering.md).
