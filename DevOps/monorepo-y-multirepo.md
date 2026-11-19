---
tipo: concepto
resumen: >-
  Monorepo y multirepo son dos formas de repartir el código: un repositorio con todo, o uno por
  servicio o componente; se elige según la unidad de despliegue y de integración.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Rachel Potvin y Josh Levenberg, Why Google Stores Billions of Lines of Code in a Single Repository, Communications of the ACM 59 (2016): https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/"
  - "Archivo/DevOps/git/git-scaling-performance.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-mastery-workflows.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-advanced-collaboration.md (original, texto generado con IA)"
  - "Archivo/DevOps/git-ecosystem-multi-repo.md (original, texto generado con IA)"
aliases: [Monorepo, Multirepo, Polyrepo]
parte_de: []
requiere: []
relacionado: [coordinacion-entre-repositorios]
---

# Monorepo y multirepo

Monorepo y multirepo son dos formas de repartir el código: un repositorio con todo, o uno por
servicio o componente; se elige según la unidad de despliegue y de integración.

## Por qué importa

La elección decide cuánto cuesta un cambio que toca varios componentes. En un monorepo es un solo
commit; en multirepo son varios PRs coordinados. También decide cómo se reparten permisos,
pipelines y dueños.

## Cómo funciona

| | Monorepo | Multirepo |
|---|---|---|
| Cambio entre componentes | un commit atómico | un PR por repo y orden de publicación |
| Versiones de dependencias | una sola para todo | cada repo fija las suyas; aparece la deriva* |
| CI | grande; necesita construir solo lo que cambió | chico y aislado por repo |
| Permisos y dueños | por ruta, con CODEOWNERS | por repo |

*La **deriva** es que distintos repos terminen usando versiones distintas de la misma
dependencia. Un esquema híbrido junta en un repo las bibliotecas compartidas y deja cada
servicio en el suyo.

La regla es elegir por la frontera de integración y despliegue, no por el tamaño del equipo: lo
que se despliega junto conviene que viva junto. Por la [Ley de Conway](../Platform-Engineering/ley-de-conway.md), la forma de repartir
los repos termina pareciéndose a cómo se reparten los equipos, y viceversa.

En multirepo, además del código de cada servicio, suele haber repos aparte para la
infraestructura como código (las definiciones de clústeres y redes que aplica Terraform o un
agente GitOps) y para las plantillas compartidas. Las versiones fijadas, los bots de
actualización y los manifiestos que mantienen todo alineado se explican en
[Coordinación entre repositorios](coordinacion-entre-repositorios.md).

Un monorepo grande necesita herramientas para no clonar ni construir todo: clon parcial, sparse
checkout y builds por ruta. La mecánica está en [Git](../Desarrollo/Git/git.md).

## Ejemplo

Google guarda casi todo su código en un solo repositorio usado por decenas de miles de
desarrolladores, con herramientas propias para sostenerlo (Potvin y Levenberg, 2016). Una
empresa con veinte microservicios que despliegan por separado suele elegir multirepo y resolver
la coordinación con bots y manifiestos.

## No confundir con

Monolito y microservicios: son la arquitectura del sistema, no la organización del código. Un
monorepo puede contener muchos microservicios, y un monolito puede depender de varios repos.

## Relaciones

- Relacionado: [Coordinación entre repositorios](coordinacion-entre-repositorios.md) — lo que hay que resolver cuando se elige multirepo.
- Ver también: [Ley de Conway](../Platform-Engineering/ley-de-conway.md) — por qué la división de repos copia la de los equipos.
