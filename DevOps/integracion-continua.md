---
tipo: concepto
resumen: >-
  La integración continua es la práctica de integrar los cambios de cada persona a la rama
  principal al menos una vez por día, con un build y pruebas automáticas que validan cada
  integración.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Martin Fowler, Continuous Integration (revisión 2024): https://martinfowler.com/articles/continuousIntegration.html"
  - "GitHub Docs, Managing a merge queue: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue"
  - "Archivo/DevOps/cicd-fundamentos.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-automation-integration.md (original, texto generado con IA)"
  - "Archivo/DevOps/git/git-organizational-topology.md (original, texto generado con IA)"
aliases: [Continuous integration, CI]
parte_de: []
requiere: []
relacionado: [pipeline-de-ci-cd]
---

# Integración continua

La integración continua es la práctica de integrar los cambios de cada persona a la rama
principal al menos una vez por día, con un build y pruebas automáticas que validan cada
integración.

## Por qué importa

Cuanto más tiempo vive un cambio sin integrar, más difícil es juntarlo con el de los demás. La
integración continua detecta el conflicto o la regresión minutos después de causarlo, cuando
todavía es chico, y mantiene la rama principal siempre en un estado desplegable. Es la base de
la [[entrega-continua]].

## Cómo funciona

Martin Fowler la define como integrar los cambios con los del resto del equipo "al menos una vez
por día". Sus prácticas centrales son:

- **Build que se prueba solo**: cada integración compila el código, arma lo que se va a
  desplegar (el build) y corre las pruebas automáticas.
- **Build roto, prioridad uno**: nadie tiene una tarea más urgente que arreglarlo; revertir el
  commit suele ser lo más rápido.
- **Build rápido**: Fowler propone unos diez minutos; un build lento desalienta integrar seguido.

Cada push o pull request (PR: el pedido de integrar una rama, que otros revisan) dispara el [[pipeline-de-ci-cd]], que corre linters, pruebas unitarias
y escaneos, y reporta el resultado en el commit. El merge se permite solo con todo en verde.

En repositorios con muchos merges por día aparece un problema: dos PRs pasan sus pruebas por
separado y juntos rompen la rama. El **merge queue** de GitHub (merge train en GitLab) lo
resuelve: arma una rama temporal con la rama principal, los PRs que están antes en la cola y el
PR nuevo, y la prueba antes de integrar, en orden de llegada.

## Ejemplo

Cinco personas trabajan en un servicio con ramas que viven menos de un día. Cada PR corre el
build en 8 minutos; si una prueba falla, el autor la arregla o revierte antes de seguir. Nunca
hay una "semana de integración" antes de una versión.

## No confundir con

Tener un servidor de CI. Correr un pipeline sobre ramas que viven semanas no es integración
continua: el cambio sigue sin integrarse con el de los demás. La frecuencia de integración a la
rama principal es lo que la define; ver [[estrategia-de-branching]].

## Relaciones

- Relacionado: [[pipeline-de-ci-cd]] — la automatización que valida cada integración.
- Base de: [[entrega-continua]] — no hay entrega continua sin integración continua.
- Ver también: [[estrategia-de-branching]] — decide cuánto vive una rama antes de integrarse.
