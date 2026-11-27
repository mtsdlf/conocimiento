---
resumen: >-
  Un estilo de arquitectura es la forma general en que se arma un sistema: cómo se parte (por capas
  técnicas o por dominio) y cuántas unidades se despliegan por separado. Va del monolito modular,
  con un solo despliegue, a los microservicios, con uno por servicio.
estado: borrador
estabilidad: estable
fuentes:
  - "Mark Richards y Neal Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), índice: https://nealford.com/books/SAF2e.html"
  - "Kamil Grzybek, Modular Monolith: A Primer (2019): https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer"
  - "Microsoft, Architecture styles, Azure Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/"
  - "Martin Fowler, MonolithFirst (2015): https://martinfowler.com/bliki/MonolithFirst.html"
  - "Martin Fowler, What do you mean by Event-Driven? (2017): https://martinfowler.com/articles/201701-event-driven.html"
aliases: [estilos de arquitectura, architecture styles, estilos arquitectónicos]
creado: 2026-11-27
revisado:
---

# Estilos

Un estilo de arquitectura es la forma general en que se arma un sistema: cómo se parte (por capas técnicas o por dominio) y cuántas unidades se despliegan por separado. Va del monolito modular, con un solo despliegue, a los microservicios, con uno por servicio.

Los estilos reciben de [Características](../Caracteristicas/caracteristicas.md) qué tiene que cumplir el sistema y de [Modularidad](../Modularidad/modularidad.md) dónde van los límites entre piezas. Cuando el estilo reparte el sistema entre procesos que se hablan por la red, los problemas nuevos (fallas parciales, consistencia, bordes) se resuelven con los patrones de [Sistemas distribuidos](../Sistemas-distribuidos/sistemas-distribuidos.md). Por qué se eligió un estilo queda escrito en un [ADR](../Decisiones/adr.md).

## Dos ejes que separan un estilo de otro

Los estilos se distinguen por dos preguntas independientes. La primera es el eje de partición: si el código se agrupa por función técnica (presentación, negocio, datos) o por área de negocio (pedidos, catálogo, pagos). La segunda es cuántas unidades de despliegue hay. Grzybek define el monolito como "a system that has exactly one deployment unit" y aclara que la etiqueta no dice nada de su calidad.

| Estilo | Partición | Unidades de despliegue | Nota |
|---|---|---|---|
| Capas | técnica | una | [Estilos simples](estilos-simples.md) |
| Pipeline | por etapa de procesamiento | una, por lo general | [Estilos simples](estilos-simples.md) |
| Microkernel | núcleo más plugins | una | [Estilos simples](estilos-simples.md) |
| Monolito modular | de dominio | una | [Monolito modular](monolito-modular.md) |
| Service-based | de dominio, en pocos servicios grandes | pocas | [Service-based](service-based.md) |
| Event-driven | por reacción a eventos | varias | [Event-driven](event-driven.md) |
| Microservicios | de dominio, servicios chicos | una por servicio | [Microservicios](microservicios.md) |

La tabla es una síntesis de esta base sobre el índice de Richards y Ford (2ª ed., 2025), que trata cada uno de estos estilos en un capítulo propio, y sobre la guía de estilos de Azure. Los capítulos no se leyeron: la columna "Partición" de pipeline, microkernel y event-driven es inferencia.

Un monolito modular y una arquitectura en capas tienen el mismo despliegue y se diferencian solo en el eje de partición. Un monolito modular y los microservicios tienen la misma partición y se diferencian en el despliegue. Esa es la razón por la que el monolito modular es el punto de partida que recomienda el tema: deja los límites de dominio hechos sin pagar todavía el costo de la red.

## De un solo despliegue a muchos, y de vuelta

La escalera que sigue el tema va del estilo más barato al más caro de operar: [monolito modular](monolito-modular.md), después [service-based](service-based.md) con pocos servicios grandes, y recién después [microservicios](microservicios.md). Fowler lo resume en "you shouldn't start a new project with microservices"; la regla general del tema está en [Empezar simple](../Decisiones/empezar-simple.md). [Event-driven](event-driven.md) no es un escalón de esa escalera: es una forma de comunicar las piezas que se combina con cualquiera de los estilos distribuidos.

Pasar de un estilo a otro sin apagar el sistema es el trabajo del [strangler fig](strangler-fig.md). Cómo se elige el estilo de partida, desde las características priorizadas, está en [Elegir un estilo](elegir-un-estilo.md).

Azure plantea los estilos como restricciones que se aceptan a cambio de un beneficio: "Focus more on why you're selecting a specific style than on how to implement it. Be practical. Sometimes it's better to relax a constraint than to chase architectural purity."

## Lo que el tema deja afuera

Tres estilos o costumbres no tienen nota propia; por qué, con la posición contraria de cada uno, está en [Lo que pierde peso](../Fundamentos/lo-que-pierde-peso.md):

- **SOA con ESB**: la lógica de integración centralizada en un bus; lo que cae es el bus como lugar de la lógica, no el servicio como unidad.
- **Space-based**: nodos con una grilla de datos en memoria replicada, para escalar mucho; figura en el canon pero hay poca evidencia pública de uso.
- **Microservicios por defecto**: empezar un sistema nuevo partido en servicios chicos antes de conocer sus límites.

## Qué hay adentro de los estilos

- [Monolito modular](monolito-modular.md) — un despliegue partido por dentro en módulos de dominio; el punto de partida recomendado.
- [Estilos simples](estilos-simples.md) — capas, pipeline y microkernel: los estilos de un solo despliegue que no parten por dominio.
- [Service-based](service-based.md) — pocos servicios grandes, el paso intermedio entre el monolito y los microservicios.
- [Event-driven](event-driven.md) — piezas que reaccionan a eventos, en topología broker o mediator; los cuatro significados del término.
- [Microservicios](microservicios.md) — un servicio desplegable por capacidad de negocio; sus tres beneficios y sus tres costos.
- [Elegir un estilo](elegir-un-estilo.md) — cómo se va de las características priorizadas al estilo.
- [Strangler fig](strangler-fig.md) — reemplazar un sistema, o pasarlo a otro estilo, de a partes y sin apagarlo.
