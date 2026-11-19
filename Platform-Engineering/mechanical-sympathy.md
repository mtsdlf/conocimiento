---
tipo: concepto
resumen: >-
  Mechanical sympathy es entender cómo se comportan el hardware y la arquitectura de abajo para
  escribir software que trabaje a favor de ellos; una plataforma que los oculta del todo impide
  adquirirla.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), sección 3.3.4: https://livebook.manning.com/book/effective-platform-engineering/chapter-3/v-1/"
  - "Martin Thompson, Why Mechanical Sympathy? (2011): https://mechanical-sympathy.blogspot.com/2011/07/why-mechanical-sympathy.html"
aliases: [Simpatía mecánica]
parte_de: []
requiere: [golden-path]
relacionado: [carga-cognitiva]
---

# Mechanical sympathy

Mechanical sympathy es entender cómo se comportan el hardware y la arquitectura de abajo para
escribir software que trabaje a favor de ellos; una plataforma que los oculta del todo impide
adquirirla.

## Por qué importa

Según Effective Platform Engineering, ninguna abstracción ni mejora de SRE rinde tanto como esa
misma abstracción usada por desarrolladores que conocen los sistemas de abajo. Un camino
pavimentado o una barrera de protección (guardrail) puede funcionar como escudo e impedir que el
desarrollador aprenda cómo corre su software. El resultado es código con menos performance,
confiabilidad y sostenibilidad.

## Cómo funciona

El término es del piloto de Fórmula 1 Jackie Stewart. Un gran piloto entiende cómo funcionan los
sistemas mecánicos del auto y maneja de forma que saque lo mejor de ellos, sin ser el ingeniero
que los diseña. Martin Thompson lo llevó al software en 2011: escribir código que trabaje con el
hardware y no contra él.

En una plataforma, la tensión es con la reducción de [Carga cognitiva](carga-cognitiva.md). Un [Golden path](golden-path.md)
puede ahorrarle al desarrollador aprender Kubernetes para su primer despliegue. Lo que no
conviene es que le impida ver después qué pasa abajo: los manifiestos generados, los límites de
recursos, las métricas del pod. Como inferencia: la plataforma reduce lo que hay que saber para
empezar, pero deja a la vista lo que hace falta para mejorar.

## Ejemplo

Un servicio desplegado con una plantilla tiene picos de latencia. Si el desarrollador puede ver
que su pod tiene 256 MB de memoria y que el recolector de basura corre cada pocos segundos, ajusta
el límite. Si la plataforma solo le muestra "desplegado: OK", abre un ticket y espera.

## No confundir con

Saber operar la infraestructura. Mechanical sympathy es entender cómo se comporta el sistema que
el código usa, no construirlo ni mantenerlo: el piloto no arma el motor.

## Relaciones

- Requiere: [Golden path](golden-path.md) — es el límite de lo que un golden path debe ocultar.
- Relacionado: [Carga cognitiva](carga-cognitiva.md) — reducir carga sin esconder lo que el desarrollador necesita entender.
