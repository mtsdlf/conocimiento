---
tipo: concepto
resumen: >-
  El versionado semántico (SemVer) numera las versiones como MAYOR.MENOR.PARCHE según el tipo de
  cambio en la API pública, con sufijos de pre-release para versiones candidatas.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Tom Preston-Werner, Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
aliases: [SemVer, Semantic Versioning, Versionado semántico]
parte_de: []
requiere: []
relacionado: [estrategia-de-branching, gitflow, coordinacion-entre-repositorios]
---

# Versionado semántico

El versionado semántico (SemVer) numera las versiones como MAYOR.MENOR.PARCHE según el tipo de
cambio en la API pública, con sufijos de pre-release para versiones candidatas.

## Por qué importa

El número le dice a quien depende del software si actualizar puede romperle algo. Con esa
garantía, un bot puede subir los parches solo y dejar los cambios mayores para revisión humana.

## Cómo funciona

La **API pública** es lo que otros usan del software y prometen no romper: funciones y clases de
una biblioteca, endpoints de un servicio, opciones de una línea de comandos. La especificación
exige declararla; en una aplicación sin API, el equipo decide qué cuenta como contrato (por
ejemplo, el formato de sus archivos o su configuración). Según la especificación 2.0.0:

- **MAYOR** sube con un cambio incompatible de la API pública.
- **MENOR** sube con funcionalidad nueva compatible hacia atrás.
- **PARCHE** sube con correcciones compatibles hacia atrás.
- Al subir uno, los de la derecha vuelven a 0: de `1.4.2` a `1.5.0`. Si una versión junta
  cambios de varios tipos, sube solo el más alto: un arreglo y una funcionalidad nueva dan
  `1.5.0`, no `1.5.1`.
- **0.y.z** es desarrollo inicial: cualquier cosa puede cambiar. `1.0.0` define la API pública.
- **Pre-release**: un guion y identificadores separados por puntos, como `1.0.0-rc.1`. Una
  pre-release tiene menor precedencia que la versión normal.
- **Metadatos de build**: un signo `+`, como `1.0.0+20261003`. No cuentan para la precedencia.

El orden de precedencia de ejemplo de la especificación es `1.0.0-alpha < 1.0.0-alpha.1 <
1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0`.

La especificación aclara que `v1.2.3` no es una versión semántica: la versión es `1.2.3`, y la
`v` es solo una convención común en los tags de Git.

## Ejemplo

Una biblioteca en `2.3.1` agrega un parámetro opcional: pasa a `2.4.0`. Después quita un método
público: pasa a `3.0.0`. Antes de publicarla saca `3.0.0-rc.1` para que la prueben otros equipos.
Si los mensajes de commit siguen [[conventional-commits]], el pipeline calcula ese número solo.

## No confundir con

El número de build o la fecha de publicación (CalVer, como `2026.10`). SemVer comunica
compatibilidad, no cuándo se publicó.

## Relaciones

- La usa: [[conventional-commits]] — la convención de commits que calcula la próxima versión con estas reglas.
- Relacionado: [[estrategia-de-branching]] — define qué ramas producen versiones publicables.
- Relacionado: [[gitflow]] — pone un tag de versión en `main` al cerrar cada release.
- Relacionado: [[coordinacion-entre-repositorios]] — fija las versiones de las que depende cada repo.
