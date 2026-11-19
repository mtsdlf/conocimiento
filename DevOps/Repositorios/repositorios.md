---
resumen: >-
  Repositorios es la parte de DevOps que trata cómo se reparte el código entre repositorios y qué
  reglas lo gobiernan: quién cambia qué, cómo se coordinan las versiones entre repos y cómo se
  sigue cada despliegue hasta su commit.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Repositorios

Repositorios es la parte de DevOps que trata cómo se reparte el código entre repositorios y qué
reglas lo gobiernan: quién cambia qué, cómo se coordinan las versiones entre repos y cómo se
sigue cada despliegue hasta su commit.

Dentro de [DevOps](../devops.md), protege las ramas que define
[Ramas y versiones](../Ramas-y-versiones/ramas-y-versiones.md). La trazabilidad se apoya en el SHA
que el [pipeline de CI/CD](../Integracion-y-entrega/pipeline-de-ci-cd.md) pone en cada artefacto, y
la firma de esos artefactos sigue en la
[cadena de suministro de software](../DevSecOps/cadena-de-suministro-de-software.md).

## Uno o muchos repositorios

Lo que se despliega junto conviene que viva junto: la elección sigue la frontera de integración y
despliegue, no el tamaño del equipo. En un monorepo, un cambio que toca varios componentes es un
solo commit. En multirepo son varios PRs, y hay que coordinar versiones fijadas, bots que
actualizan dependencias y un release train que compone las versiones de una release.

## Reglas que dejan evidencia

Las reglas las aplica la plataforma, no la memoria de alguien: ramas protegidas, checks
obligatorios, CODEOWNERS y roles, con la idea de que las personas deciden y los bots ejecutan. Cada
eslabón (PR aprobado, CI, build, despliegue) deja un registro con el SHA del commit como clave
común, y eso es la evidencia de auditoría. DORA recomienda cumplir la separación de funciones con
revisión de pares registrada en la plataforma en vez de un comité externo de aprobación.

## Qué hay adentro de repositorios

- [Gobernanza de repositorios](gobernanza-de-repositorios.md) — ramas protegidas, checks obligatorios, CODEOWNERS y roles.
- [Monorepo y multirepo](monorepo-y-multirepo.md) — cómo repartir el código en repositorios y cuándo conviene cada forma.
- [Coordinación entre repositorios](coordinacion-entre-repositorios.md) — versiones fijadas, bots de dependencias y release train en multirepo.
- [Trazabilidad de cambios](trazabilidad-de-cambios.md) — seguir cada despliegue hasta su commit, su revisión y su build, para auditoría.
