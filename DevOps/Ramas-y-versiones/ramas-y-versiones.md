---
resumen: >-
  Ramas y versiones es la parte de DevOps que decide cómo se integra el código en un repositorio y
  cómo se numera lo que se publica: la estrategia de branching, el versionado semántico y los
  mensajes de commit que calculan la versión.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Ramas y versiones

Ramas y versiones es la parte de DevOps que decide cómo se integra el código en un repositorio y
cómo se numera lo que se publica: la estrategia de branching, el versionado semántico y los
mensajes de commit que calculan la versión.

Dentro de [DevOps](../devops.md), fija cuánto vive una rama antes de integrarse, que es lo que
define a la [integración continua](../Integracion-y-entrega/integracion-continua.md). Las reglas que
protegen esas ramas están en [Repositorios](../Repositorios/repositorios.md). Las ramas del código
no se repiten como ramas de entorno: cómo pasa una versión de un entorno al siguiente está en
[Promoción entre entornos](../Despliegue/promocion-entre-entornos.md).

## Cuántas ramas de larga vida

Las estrategias se distinguen por cuántas ramas de larga vida tienen. Trunk-based development deja
solo `main`, con ramas que duran horas y el trabajo incompleto apagado detrás de un feature flag.
Gitflow suma `develop` y ramas de release y hotfix, para software con versiones programadas y
varias versiones soportadas a la vez. Cuanto más vive una rama sin integrarse, más caro es el
merge; por eso la elección sigue la cadencia de entrega.

## Del commit al número de versión

El versionado semántico numera MAYOR.MENOR.PARCHE según el tipo de cambio en la API pública.
Conventional Commits pone ese tipo en el mensaje (`fix` da PARCHE, `feat` da MENOR y `!` o
`BREAKING CHANGE` da MAYOR), y con eso una herramienta calcula la versión, crea el tag y escribe el
changelog sin que nadie elija el número a mano.

## Qué hay adentro de ramas y versiones

- [Estrategia de branching](estrategia-de-branching.md) — qué ramas existen y cómo se integran; leerla antes de las dos siguientes.
- [Trunk-based development](trunk-based-development.md) — una sola rama con ramas de vida corta y feature flags.
- [Gitflow](gitflow.md) — `main`, `develop` y ramas de feature, release y hotfix para entregas con versión.
- [Versionado semántico](versionado-semantico.md) — MAYOR.MENOR.PARCHE según el tipo de cambio.
- [Conventional Commits](conventional-commits.md) — mensajes de commit que permiten calcular la versión y el changelog.
