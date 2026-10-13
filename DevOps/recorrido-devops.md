---
tipo: recorrido
resumen: >-
  DevOps desde cero, para quien viene de desarrollo o de operaciones: de la cultura que lo
  sostiene a cómo un cambio llega a producción de forma automática, auditada y segura, y cómo se
  mide si la entrega mejora.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [devops]
---

# DevOps desde cero

DevOps desde cero, para quien viene de desarrollo o de operaciones: de la cultura que lo
sostiene a cómo un cambio llega a producción de forma automática, auditada y segura, y cómo se
mide si la entrega mejora.

1. [[calms]] — va primero porque nombra las cinco dimensiones que el resto del Recorrido desarrolla.
2. [[flujo-de-valor]] — el recorrido de un cambio hasta producción; las prácticas siguientes lo acortan.
3. [[integracion-continua]] — la primera práctica técnica: integrar seguido y validar cada cambio.
4. [[entrega-continua]] — extiende la integración hasta dejar cada cambio listo para producción.
5. [[despliegue-continuo]] — el paso siguiente: sin aprobación manual antes de producción.
6. [[pipeline-de-ci-cd]] — la automatización concreta que implementa los tres pasos anteriores.
7. [[estrategia-de-branching]] — cómo se organizan las ramas para que el pipeline integre seguido.
8. [[versionado-semantico]] — cómo se numeran los artefactos; va después del branching porque el tag de una rama decide cuándo se publica una versión.
9. [[infraestructura-como-codigo]] — la infraestructura en archivos versionados, que GitOps da por sabida.
10. [[gitops]] — cómo se despliega declarando el estado en Git en vez de empujar cambios.
11. [[reconciliacion-gitops]] — el mecanismo que hace funcionar a GitOps y corrige el drift.
12. [[devsecops]] — cómo la seguridad entra en cada etapa de todo lo anterior.
13. [[cadena-de-suministro-de-software]] — cómo probar que lo desplegado es lo que salió del build.
14. [[trazabilidad-de-cambios]] — cómo se audita: cada despliegue llevado hasta su commit, su revisión y su build.
15. [[metricas-dora]] — va al final porque mide el resultado de todas las prácticas anteriores.

Para consultar: [[herramientas-de-seguridad-del-pipeline]].

**Al terminar**: se sabe explicar cómo un cambio va del commit a producción, qué controles lo
protegen y con qué métricas se evalúa la entrega. El siguiente es [[recorrido-platform-engineering]],
que muestra cómo una plataforma interna ofrece estas prácticas a muchos equipos.
