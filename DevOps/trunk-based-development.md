---
tipo: concepto
resumen: >-
  En trunk-based development todos integran en una sola rama, el trunk, con ramas de vida corta
  (horas o pocos días) y esconden el trabajo incompleto con feature flags.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Paul Hammant y otros, Trunk Based Development: https://trunkbaseddevelopment.com/"
  - "DORA, Capabilities: Trunk-based development: https://dora.dev/capabilities/trunk-based-development/"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
aliases: [TBD, Desarrollo basado en trunk, Trunk-based]
parte_de: [estrategia-de-branching]
requiere: []
relacionado: [gitflow]
---

# Trunk-based development

En trunk-based development todos integran en una sola rama, el trunk, con ramas de vida corta
(horas o pocos días) y esconden el trabajo incompleto con feature flags.

## Por qué importa

Si nadie trabaja lejos del trunk, los merges son chicos y los conflictos aparecen el mismo día.
DORA lo asocia, con datos de 2016 y 2017, a mejor desempeño de entrega. Es la base práctica de
la [Integración continua](integracion-continua.md): sin integrar seguido a una rama común no hay integración continua.

## Cómo funciona

- **Una rama compartida**: `main` o `trunk`. Equipos muy chicos commitean directo; los más
  grandes usan ramas cortas con PR, que existen para la revisión y el CI, no para producir
  artefactos.
- **Ramas cortas**: DORA recomienda tres ramas activas o menos y que cada rama dure unas
  pocas horas antes de volver al trunk.
- **Sin congelamientos**: DORA también recomienda no congelar el código ni tener fases de
  integración aparte, porque el trunk ya está integrado todo el tiempo.
- **Trabajo incompleto oculto**: lo que no está listo entra apagado detrás de un feature flag,
  un interruptor de configuración que activa o desactiva una funcionalidad sin redesplegar (ver
  [Estrategias de despliegue](estrategias-de-despliegue.md)).
  Para cambios largos se usa branch by abstraction: una capa intermedia permite reemplazar una
  implementación por partes, sin rama larga.
- **Releases**: se publica desde el trunk, o desde una rama de release creada justo antes, que
  solo recibe correcciones y se borra después. Un error se corrige primero en el trunk.

## Ejemplo

Una desarrolladora empieza a las 10 una rama `feature/precio-dinamico`, abre el PR a las 14 y lo
mergea a las 16 con la funcionalidad apagada por un flag. Al día siguiente sigue con otra rama
corta. Producto prende el flag cuando la funcionalidad está completa.

## No confundir con

[Gitflow](gitflow.md): ahí `develop` y las ramas de release viven semanas, y la integración con `main` se
hace por lotes. En trunk-based la única rama de larga vida es el trunk.

## Relaciones

- Parte de: [Estrategia de branching](estrategia-de-branching.md) — una de las estrategias posibles.
- Relacionado: [Gitflow](gitflow.md) — la estrategia opuesta, con ramas de larga vida.
- Ver también: [Integración continua](integracion-continua.md) — la práctica que este modelo de ramas hace posible.
