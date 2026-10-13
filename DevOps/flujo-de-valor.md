---
tipo: concepto
resumen: >-
  El flujo de valor es el recorrido de un cambio desde la idea hasta que llega al usuario en
  producción; mapearlo muestra esperas, traspasos manuales y lotes grandes, y achicar lotes y
  limitar el trabajo en curso lo acelera.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "DORA, Visibility of work in the value stream: https://dora.dev/capabilities/work-visibility-in-value-stream/"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
aliases: [Value stream, Value stream mapping, VSM, Mapa de flujo de valor]
parte_de: []
requiere: []
relacionado: [calms, metricas-dora]
---

# Flujo de valor

El flujo de valor es el recorrido de un cambio desde la idea hasta que llega al usuario en
producción; mapearlo muestra esperas, traspasos manuales y lotes grandes, y achicar lotes y
limitar el trabajo en curso lo acelera.

## Por qué importa

Cada área suele optimizar su tramo (desarrollo, pruebas, operaciones) y el cambio igual tarda
semanas. Mirar el flujo de punta a punta muestra que la mayor parte del tiempo no es trabajo
sino espera entre tramos. Es lo que la dimensión Lean de [[calms]] pide mejorar.

## Cómo funciona

El **value stream mapping** se arma con las personas de cada etapa: se sigue un cambio real
desde la idea hasta producción y se dibuja cada etapa con, según DORA, tres datos:

- **lead time**: cuánto tarda la etapa, contando la espera del traspaso (la suma de todas las
  etapas da el lead time total, que DORA mide desde el commit);
- **process time**: cuánto tarda el trabajo en sí, sin interrupciones;
- **%C/A** (porcentaje completo y correcto): cuánto de lo que llega a la etapa no hay que rehacer.

La diferencia entre lead time y process time es la espera. Los cuellos de botella típicos son
los traspasos manuales, la poca automatización de pruebas, la disputa por un entorno de pruebas
compartido y las aprobaciones burocráticas.

Para acelerar el flujo se aplican dos prácticas lean: **lotes chicos** (cambios pequeños que se
integran y despliegan seguido) y **límites al trabajo en curso** (WIP), visibles en un tablero
Kanban (una columna por etapa, con un máximo de tarjetas en cada una).

El repositorio también da señales del flujo. Las ramas que viven semanas indican integración
demorada; muchos reverts después de una versión indican revisión o pruebas flojas; pocos merges
con diffs enormes son el anti-patrón de lotes grandes.

## Ejemplo

Un cambio de una línea tarda 12 días en llegar a producción. El mapa muestra 2 horas de trabajo
y 3 esperas: 4 días por una revisión, 5 por un entorno de QA compartido y 3 por un comité de
cambios. Las [[metricas-dora]] dan el lead time total; el mapa dice dónde se pierde.

## No confundir con

El pipeline de CI/CD. El pipeline automatiza un tramo del flujo; el flujo de valor incluye
también lo manual y lo organizacional, desde la idea hasta el usuario. Organizar equipos
alrededor de un flujo es lo que hace un [[stream-aligned-team]].

## Relaciones

- Relacionado: [[calms]] — el flujo es el objeto de la dimensión Lean.
- Relacionado: [[metricas-dora]] — miden el resultado del flujo; el mapa explica la causa.
- Ver también: [[stream-aligned-team]] — el equipo organizado alrededor de un flujo de valor.
- Ver también: [[carga-cognitiva]] — los traspasos y las herramientas sueltas la aumentan.
