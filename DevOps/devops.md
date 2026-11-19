---
tipo: mapa
resumen: >-
  DevOps es la forma de trabajo que une desarrollo y operaciones para entregar cambios chicos,
  frecuentes y confiables; este Mapa reúne las notas sobre cultura y medición, entrega continua,
  branching y versionado, repositorios, GitOps, DevSecOps y las herramientas de CI/CD.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# DevOps

DevOps es la forma de trabajo que une desarrollo y operaciones para entregar cambios chicos,
frecuentes y confiables; este Mapa reúne las notas sobre cultura y medición, entrega continua,
branching y versionado, repositorios, GitOps, DevSecOps y las herramientas de CI/CD.

Para aprenderlo en orden: [DevOps desde cero](recorrido-devops.md). El Tema hermano es [Platform Engineering](../Platform-Engineering/platform-engineering.md): la
organización de equipos y la plataforma interna que sostienen estas prácticas. Lo que DevOps no es
(un equipo intermedio entre Dev y Ops) está en [Anti-patrón del equipo DevOps](../Platform-Engineering/anti-patron-equipo-devops.md).

## Cultura y medición

- [CALMS](calms.md) — las cinco dimensiones para describir y evaluar una adopción de DevOps; la puerta de entrada al Tema.
- [Flujo de valor](flujo-de-valor.md) — el recorrido de un cambio de la idea a producción y cómo acelerarlo.
- [Postmortem sin culpa](postmortem-sin-culpa.md) — cómo analizar un incidente para mejorar el sistema y no castigar personas.
- [Métricas DORA](metricas-dora.md) — los indicadores de desempeño de entrega, con sus nombres actuales.

## Entrega continua (CI/CD)

- [Integración continua](integracion-continua.md) — integrar a la rama principal varias veces por día, con build y pruebas automáticas.
- [Entrega continua](entrega-continua.md) — cada cambio validado queda listo para producción; el paso final es manual.
- [Despliegue continuo](despliegue-continuo.md) — cada cambio que pasa las verificaciones llega solo a producción.
- [Pipeline de CI/CD](pipeline-de-ci-cd.md) — la secuencia de etapas que disparan los eventos de Git.
- [Pipeline reutilizable](pipeline-reutilizable.md) — una definición central y versionada que muchos repos invocan.
- [Estrategias de despliegue](estrategias-de-despliegue.md) — rolling, blue/green, canary y feature flags, según el riesgo.
- [Infraestructura como código](infraestructura-como-codigo.md) — la infraestructura en archivos versionados que se aplican de forma repetible.

## CI/CD con GitHub Actions

- [GitHub Actions](github-actions.md) — workflows, jobs, runners y actions; la base de las otras cuatro.
- [Reutilización en GitHub Actions](reutilizacion-en-github-actions.md) — workflows reutilizables y actions propias.
- [Environment de GitHub Actions](environment-de-github-actions.md) — destinos de despliegue con reglas de protección y concurrencia.
- [Artifact y cache de GitHub Actions](artifact-y-cache-de-github-actions.md) — qué guarda un artifact, qué guarda la cache y las attestations.
- [Secret de GitHub Actions](secret-de-github-actions.md) — dónde se guardan los secrets y cómo los lee un workflow.

## CI/CD con Tekton y Azure

- [Tekton](tekton.md) — el framework de CI/CD nativo de Kubernetes: Tasks, Pipelines y Triggers.
- [Disparar Tekton desde Azure DevOps](disparar-tekton-desde-azure-devops.md) — pasos para lanzar un PipelineRun con cada push o PR de Azure Repos.
- [Desplegar en AKS con Azure Pipelines](desplegar-en-aks-con-azure-pipelines.md) — pasos para construir, subir a ACR y desplegar en AKS.

## Branching y versionado

- [Estrategia de branching](estrategia-de-branching.md) — qué ramas existen y cómo se integran; leerla antes de las dos siguientes.
- [Trunk-based development](trunk-based-development.md) — una sola rama con ramas de vida corta y feature flags.
- [Gitflow](gitflow.md) — `main`, `develop` y ramas de feature, release y hotfix para entregas con versión.
- [Versionado semántico](versionado-semantico.md) — MAYOR.MENOR.PARCHE según el tipo de cambio.
- [Conventional Commits](conventional-commits.md) — mensajes de commit que permiten calcular la versión y el changelog.

Cómo funciona la herramienta Git (merge, rebase, reflog, LFS, mirrors) está en [Git](../Desarrollo/Git/git.md), en el Tema
Desarrollo.

## Repositorios a escala

- [Gobernanza de repositorios](gobernanza-de-repositorios.md) — ramas protegidas, checks obligatorios, CODEOWNERS y roles.
- [Monorepo y multirepo](monorepo-y-multirepo.md) — cómo repartir el código en repositorios y cuándo conviene cada forma.
- [Coordinación entre repositorios](coordinacion-entre-repositorios.md) — versiones fijadas, bots de dependencias y release train en multirepo.
- [Trazabilidad de cambios](trazabilidad-de-cambios.md) — seguir cada despliegue hasta su commit, su revisión y su build, para auditoría.

## GitOps

- [GitOps](gitops.md) — el estado deseado en Git y un agente que lo aplica; la puerta de entrada al grupo.
- [Reconciliación (GitOps)](reconciliacion-gitops.md) — el bucle que corrige el drift y por qué GitOps despliega por pull.
- [Promoción entre entornos](promocion-entre-entornos.md) — cómo pasar un cambio de un entorno al siguiente con un PR.

## DevSecOps

- [DevSecOps](devsecops.md) — la seguridad como responsabilidad compartida y automatizada en todo el ciclo.
- [Seguridad en el pipeline](seguridad-en-el-pipeline.md) — los controles automáticos por etapa del pipeline.
- [Herramientas de seguridad del pipeline](herramientas-de-seguridad-del-pipeline.md) — qué herramienta se usa para cada control, para consultar.
- [Cadena de suministro de software](cadena-de-suministro-de-software.md) — SBOM, firma y procedencia de cada artefacto.
- [Gestión de secretos](gestion-de-secretos.md) — credenciales fuera del código y del historial.
- [Policy as code](policy-as-code.md) — reglas de seguridad y cumplimiento evaluadas como código.

## Ver también

- [Observabilidad](../Platform-Engineering/observabilidad.md) — métricas, logs y traces para entender qué hace el sistema; en Platform Engineering.
- [FinOps](../Cloud/FinOps/finops.md) — la responsabilidad sobre el costo de la nube; en el Tema Cloud.

## Pendiente

- SLO y SLI: sin nota todavía; van con [Observabilidad](../Platform-Engineering/observabilidad.md) cuando se migre ese material.
- Ansible: hay solo un temario sin contenido, archivado en `Archivo/DevOps/ansible-roadmap.md`.
