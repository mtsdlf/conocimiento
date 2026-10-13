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

Para aprenderlo en orden: [[recorrido-devops]]. El Tema hermano es [[platform-engineering]]: la
organización de equipos y la plataforma interna que sostienen estas prácticas. Lo que DevOps no es
(un equipo intermedio entre Dev y Ops) está en [[anti-patron-equipo-devops]].

## Cultura y medición

- [[calms]] — las cinco dimensiones para describir y evaluar una adopción de DevOps; la puerta de entrada al Tema.
- [[flujo-de-valor]] — el recorrido de un cambio de la idea a producción y cómo acelerarlo.
- [[postmortem-sin-culpa]] — cómo analizar un incidente para mejorar el sistema y no castigar personas.
- [[metricas-dora]] — los indicadores de desempeño de entrega, con sus nombres actuales.

## Entrega continua (CI/CD)

- [[integracion-continua]] — integrar a la rama principal varias veces por día, con build y pruebas automáticas.
- [[entrega-continua]] — cada cambio validado queda listo para producción; el paso final es manual.
- [[despliegue-continuo]] — cada cambio que pasa las verificaciones llega solo a producción.
- [[pipeline-de-ci-cd]] — la secuencia de etapas que disparan los eventos de Git.
- [[pipeline-reutilizable]] — una definición central y versionada que muchos repos invocan.
- [[estrategias-de-despliegue]] — rolling, blue/green, canary y feature flags, según el riesgo.
- [[infraestructura-como-codigo]] — la infraestructura en archivos versionados que se aplican de forma repetible.

## CI/CD con GitHub Actions

- [[github-actions]] — workflows, jobs, runners y actions; la base de las otras cuatro.
- [[reutilizacion-en-github-actions]] — workflows reutilizables y actions propias.
- [[environment-de-github-actions]] — destinos de despliegue con reglas de protección y concurrencia.
- [[artifact-y-cache-de-github-actions]] — qué guarda un artifact, qué guarda la cache y las attestations.
- [[secret-de-github-actions]] — dónde se guardan los secrets y cómo los lee un workflow.

## CI/CD con Tekton y Azure

- [[tekton]] — el framework de CI/CD nativo de Kubernetes: Tasks, Pipelines y Triggers.
- [[disparar-tekton-desde-azure-devops]] — pasos para lanzar un PipelineRun con cada push o PR de Azure Repos.
- [[desplegar-en-aks-con-azure-pipelines]] — pasos para construir, subir a ACR y desplegar en AKS.

## Branching y versionado

- [[estrategia-de-branching]] — qué ramas existen y cómo se integran; leerla antes de las dos siguientes.
- [[trunk-based-development]] — una sola rama con ramas de vida corta y feature flags.
- [[gitflow]] — `main`, `develop` y ramas de feature, release y hotfix para entregas con versión.
- [[versionado-semantico]] — MAYOR.MENOR.PARCHE según el tipo de cambio.
- [[conventional-commits]] — mensajes de commit que permiten calcular la versión y el changelog.

Cómo funciona la herramienta Git (merge, rebase, reflog, LFS, mirrors) está en [[git]], en el Tema
Desarrollo.

## Repositorios a escala

- [[gobernanza-de-repositorios]] — ramas protegidas, checks obligatorios, CODEOWNERS y roles.
- [[monorepo-y-multirepo]] — cómo repartir el código en repositorios y cuándo conviene cada forma.
- [[coordinacion-entre-repositorios]] — versiones fijadas, bots de dependencias y release train en multirepo.
- [[trazabilidad-de-cambios]] — seguir cada despliegue hasta su commit, su revisión y su build, para auditoría.

## GitOps

- [[gitops]] — el estado deseado en Git y un agente que lo aplica; la puerta de entrada al grupo.
- [[reconciliacion-gitops]] — el bucle que corrige el drift y por qué GitOps despliega por pull.
- [[promocion-entre-entornos]] — cómo pasar un cambio de un entorno al siguiente con un PR.

## DevSecOps

- [[devsecops]] — la seguridad como responsabilidad compartida y automatizada en todo el ciclo.
- [[seguridad-en-el-pipeline]] — los controles automáticos por etapa del pipeline.
- [[herramientas-de-seguridad-del-pipeline]] — qué herramienta se usa para cada control, para consultar.
- [[cadena-de-suministro-de-software]] — SBOM, firma y procedencia de cada artefacto.
- [[gestion-de-secretos]] — credenciales fuera del código y del historial.
- [[policy-as-code]] — reglas de seguridad y cumplimiento evaluadas como código.

## Ver también

- [[observabilidad]] — métricas, logs y traces para entender qué hace el sistema; en Platform Engineering.
- [[finops]] — la responsabilidad sobre el costo de la nube; en el Tema Cloud.

## Pendiente

- SLO y SLI: sin nota todavía; van con [[observabilidad]] cuando se migre ese material.
- Ansible: hay solo un temario sin contenido, archivado en `Archivo/DevOps/ansible-roadmap.md`.
