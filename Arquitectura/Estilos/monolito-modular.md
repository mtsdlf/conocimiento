---
resumen: >-
  Un monolito modular es un sistema con una sola unidad de despliegue, partido por dentro en módulos
  de dominio que se hablan solo por una interfaz definida. Tiene los límites de los microservicios sin
  el costo de la red.
estado: borrador
estabilidad: estable
fuentes:
  - "Kamil Grzybek, Modular Monolith: A Primer (2019-12-02): https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer"
  - "Martin Fowler, MonolithFirst (2015-06-03): https://martinfowler.com/bliki/MonolithFirst.html"
  - "Martin Fowler, MicroservicePremium (2015-05-13): https://martinfowler.com/bliki/MicroservicePremium.html"
  - "Chris Richardson, Pattern: Monolithic Architecture: https://microservices.io/patterns/monolithic.html"
  - "Philip Müller, Under Deconstruction: The State of Shopify's Monolith (2020-09-16): https://shopify.engineering/shopify-monolith"
  - "Stefan Tilkov, Don't start with a monolith (2015-06-09): https://www.martinfowler.com/articles/dont-start-monolith.html"
  - "Mark Richards y Neal Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), índice: https://nealford.com/books/SAF2e.html"
aliases: [modular monolith, monolito modular]
creado: 2026-11-27
revisado:
---

# Monolito modular

Un monolito modular es un sistema con una sola unidad de despliegue, partido por dentro en módulos de dominio que se hablan solo por una interfaz definida. Tiene los límites de los microservicios sin el costo de la red.

## Un despliegue, varios módulos de dominio

"Monolito" describe cómo se despliega el sistema, no si está bien hecho: Grzybek lo define como "a system that has exactly one deployment unit". Lo que lo vuelve modular es cómo se parte por dentro. Según Grzybek, un módulo tiene que ser independiente, cubrir una funcionalidad de negocio completa y exponer una interfaz definida. Los módulos son cortes verticales de negocio (pedidos, catálogo, pagos), no capas técnicas.

Un módulo habla con otro de dos formas, según Grzybek: por un contrato síncrono (una fachada que el otro módulo llama) o por uno asíncrono (un evento que publica y el otro escucha). Lo que no hace es leer las tablas o las clases internas del otro. Dónde se pone cada límite y cómo se mide el acoplamiento entre módulos está en [Modularidad](../Modularidad/modularidad.md).

La diferencia con la arquitectura en [capas](estilos-simples.md#capas-partir-por-función-técnica) es el eje de partición: las capas agrupan por función técnica y el monolito modular por dominio. La diferencia con los [microservicios](microservicios.md) es el despliegue: los mismos módulos, cada uno en su proceso, serían servicios.

Richards y Ford sumaron en la 2ª edición (2025) un capítulo propio, "The Modular Monolith Architecture", que según los autores llena un hueco de la primera. El capítulo no se leyó.

## Por qué el tema arranca por acá

Fowler sostiene que "you shouldn't start a new project with microservices". Su observación es que la mayoría de los sistemas de microservicios exitosos empezaron como un monolito que creció, y que los que arrancaron partidos en servicios "often ran into serious trouble". La razón que da: los límites entre servicios son difíciles de acertar al principio, y mover código entre servicios cuesta mucho más que moverlo entre módulos de un mismo proceso. Él mismo reconoce que la evidencia es escasa.

En "MicroservicePremium" lo dice más fuerte: "don't even consider microservices unless you have a system that's too complex to manage as a monolith". El premio que se paga por distribuir puede "slow down your development considerably".

Richardson resume qué da un solo despliegue: operaciones locales, transacciones ACID y ningún acoplamiento en tiempo de ejecución entre componentes. Y qué cuesta: una base de código grande, poca autonomía de los equipos, un pipeline lento, un solo stack y ningún escalado por subdominio. "These drawbacks become more severe as the application grows in size and complexity." Cuándo esos costos justifican pasar a otro estilo se decide con las [características](../Caracteristicas/caracteristicas-arquitectonicas.md) priorizadas, como cuenta [Elegir un estilo](elegir-un-estilo.md).

> [!IMPORTANT]
> Empezar por el monolito no es unánime, y Fowler lo admite ("by no means unanimous"). Stefan Tilkov, en el mismo sitio y seis días después, sostiene que para un sistema que va a terminar en microservicios "starting with a monolith is usually exactly the wrong thing to do": partirlo después es muy difícil porque los módulos comparten modelo de dominio, persistencia y transacciones. Tilkov acepta que su camino funciona mejor cuando el dominio ya se entiende bien. La disputa es sobre cuánto se conoce el dominio y cuántos equipos trabajan en paralelo, no sobre rendimiento; sigue en [Lo que pierde peso](../Fundamentos/lo-que-pierde-peso.md).

## La modularidad se mide: el monolito de Shopify

Shopify contó en 2020 el estado de su monolito: unos 2,8 millones de líneas de Ruby, unos 500.000 commits, "hundreds of developers" y 37 componentes. El primer análisis mostró que cada componente dependía de más de la mitad de los otros: los módulos estaban declarados, pero no separados. El objetivo explícito era un "modular monolith", y el post dice "While we're far from finished, we already reap the benefits".

Para hacer cumplir los límites, reemplazaron un análisis en tiempo de ejecución que tardaba más de una hora por un análisis estático de referencias entre componentes que corre en minutos y rechaza los cambios que rompen el encapsulamiento. En 2020 lo aplicaban en cerca de un tercio de los componentes. Un chequeo automático que falla el build cuando se viola un límite es, en el vocabulario de este tema, una [fitness function](../Caracteristicas/fitness-function.md); la equivalencia es de esta base, no del post. El post es de 2020 y no se verificó cómo siguió.

La lección que se lleva el tema: la modularidad no se declara, se mide.

## Hacia otro estilo, de a un módulo

Si un módulo necesita escalar o desplegarse aparte, se lo saca a un servicio propio con un [strangler fig](strangler-fig.md): el resto del sistema sigue andando mientras el tráfico se corre de a poco. El paso intermedio, pocos servicios grandes en lugar de muchos chicos, es [service-based](service-based.md).

Para leer más: el capítulo "The Modular Monolith Architecture" de Richards y Ford (2ª ed.), fijándose en qué eje de partición usa y cómo hace cumplir el aislamiento entre módulos en el código y en los datos. Como lectura abierta, el post de Shopify (2020) para el cómo y "MonolithFirst" de Fowler para el porqué; en Shopify, fijarse en el dato de las dependencias cruzadas antes de la herramienta.
