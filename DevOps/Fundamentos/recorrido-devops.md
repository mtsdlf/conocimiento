---
resumen: >-
  DevOps desde cero, para quien viene de desarrollo o de operaciones: de la cultura que lo
  sostiene a cómo un cambio llega a producción de forma automática, auditada y segura, y cómo se
  mide si la entrega mejora.
estado: borrador
estabilidad: semi
fuentes: []
creado: 2026-10-03
revisado:
---

# DevOps desde cero

DevOps desde cero, para quien viene de desarrollo o de operaciones: de la cultura que lo
sostiene a cómo un cambio llega a producción de forma automática, auditada y segura, y cómo se
mide si la entrega mejora.

Va por las seis partes de [DevOps](../devops.md) en el orden en que un cambio las necesita; la
entrada de cada parte lista lo que el recorrido salta.

1. [CALMS](calms.md) — va primero porque nombra las cinco dimensiones que el resto del Recorrido desarrolla.
2. [Flujo de valor](../Cultura-y-medicion/flujo-de-valor.md) — el recorrido de un cambio hasta producción; las prácticas siguientes lo acortan.
3. [Integración continua](../Integracion-y-entrega/integracion-continua.md) — la primera práctica técnica: integrar seguido y validar cada cambio.
4. [Entrega continua](../Integracion-y-entrega/entrega-continua.md) — extiende la integración hasta dejar cada cambio listo para producción.
5. [Despliegue continuo](../Integracion-y-entrega/despliegue-continuo.md) — el paso siguiente: sin aprobación manual antes de producción.
6. [Pipeline de CI/CD](../Integracion-y-entrega/pipeline-de-ci-cd.md) — la automatización concreta que implementa los tres pasos anteriores.
7. [Estrategia de branching](../Ramas-y-versiones/estrategia-de-branching.md) — cómo se organizan las ramas para que el pipeline integre seguido.
8. [Versionado semántico](../Ramas-y-versiones/versionado-semantico.md) — cómo se numeran los artefactos; va después del branching porque el tag de una rama decide cuándo se publica una versión.
9. [Infraestructura como código](../Despliegue/infraestructura-como-codigo.md) — la infraestructura en archivos versionados, que GitOps da por sabida.
10. [GitOps](../Despliegue/gitops.md) — cómo se despliega declarando el estado en Git en vez de empujar cambios.
11. [Reconciliación (GitOps)](../Despliegue/reconciliacion-gitops.md) — el mecanismo que hace funcionar a GitOps y corrige el drift.
12. [DevSecOps](../DevSecOps/devsecops.md) — cómo la seguridad entra en cada etapa de todo lo anterior.
13. [Cadena de suministro de software](../DevSecOps/cadena-de-suministro-de-software.md) — cómo probar que lo desplegado es lo que salió del build.
14. [Trazabilidad de cambios](../Repositorios/trazabilidad-de-cambios.md) — cómo se audita: cada despliegue llevado hasta su commit, su revisión y su build.
15. [Métricas DORA](../Cultura-y-medicion/metricas-dora.md) — va al final porque mide el resultado de todas las prácticas anteriores.

Para consultar: [Herramientas de seguridad del pipeline](../DevSecOps/herramientas-de-seguridad-del-pipeline.md).

**Al terminar**: se sabe explicar cómo un cambio va del commit a producción, qué controles lo
protegen y con qué métricas se evalúa la entrega. El siguiente es [Platform engineering desde cero](../../Platform-Engineering/Fundamentos/recorrido-platform-engineering.md),
que muestra cómo una plataforma interna ofrece estas prácticas a muchos equipos.
