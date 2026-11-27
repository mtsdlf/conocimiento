---
resumen: >-
  Capas, pipeline y microkernel son los estilos de un solo despliegue que no parten el sistema por
  dominio: las capas lo parten por función técnica, el pipeline por etapas que se pasan datos y el
  microkernel en un núcleo chico con plugins.
estado: borrador
estabilidad: estable
fuentes:
  - "Mark Richards y Neal Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), índice: https://nealford.com/books/SAF2e.html"
  - "Microsoft, Architecture styles, Azure Architecture Center (2025-09-25): https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/"
aliases: [arquitectura en capas, layered architecture, n-tier, pipeline, pipes and filters, microkernel, arquitectura de plugins]
creado: 2026-11-27
revisado:
---

# Estilos simples

Capas, pipeline y microkernel son los estilos de un solo despliegue que no parten el sistema por dominio: las capas lo parten por función técnica, el pipeline por etapas que se pasan datos y el microkernel en un núcleo chico con plugins.

Richards y Ford dedican un capítulo a cada uno en la 2ª edición (2025). Esos capítulos no se leyeron; lo que sigue sale de la guía de estilos de Azure para las capas y es definición de esta base para pipeline y microkernel. Comparten con el [monolito modular](monolito-modular.md) el despliegue único y se diferencian de él en cómo agrupan el código.

## Capas: partir por función técnica

Una arquitectura en capas agrupa el código por lo que hace técnicamente: presentación, lógica de negocio, acceso a datos. Azure la describe como N-tier: capas lógicas que pueden ir en niveles físicos distintos, donde cada capa solo llama a la de abajo. Sirve, según Azure, para dominios tradicionales con pocas actualizaciones y para migrar aplicaciones que ya están en capas.

Su costo aparece cuando cambia una regla de negocio. Un cambio en "pedidos" toca la pantalla, el servicio y el repositorio, que viven en tres capas distintas. Azure lo dice así: "the horizontal layering can make it difficult to introduce changes without affecting multiple parts of the application". El [monolito modular](monolito-modular.md) gira ese eje: agrupa por dominio, y adentro de cada módulo puede haber capas.

Azure describe además Web-Queue-Worker, un primo cercano: un frontend web que atiende pedidos, una cola y un worker que hace las tareas pesadas. Sirve para dominios simples con trabajo pesado en segundo plano, con el riesgo de que el frontend y el worker crezcan hasta volverse monolitos cada uno.

## Pipeline: etapas que se pasan datos

> [!NOTE]
> Sin fuente todavía: el capítulo de pipeline de Richards y Ford no se leyó y no hay fuente verificada con ejemplos. La definición es de esta base.

Un pipeline parte el sistema en etapas (filtros) unidas por canales (tuberías): cada etapa recibe un dato, lo transforma y se lo pasa a la siguiente, sin saber quién viene antes o después. Se usa cuando el trabajo es una secuencia fija de transformaciones, como procesar archivos, transformar datos o compilar. Un sistema con modelos suele tener uno adentro (limpiar la entrada, armar el contexto, llamar al modelo, validar la salida); esa relación es inferencia de esta base y se desarrolla en [Sistemas con modelos](../Sistemas-con-modelos/sistemas-con-modelos.md).

El caso de Prime Video que cuenta [Microservicios](microservicios.md#prime-video-un-caso-que-se-lee-de-dos-maneras) muestra lo que pasa cuando las etapas de un pipeline con mucho dato entre pasos se reparten por la red.

## Microkernel: un núcleo y plugins

> [!NOTE]
> Sin fuente todavía: el capítulo de microkernel de Richards y Ford no se leyó y no hay fuente verificada con ejemplos. La definición es de esta base.

Un microkernel separa un núcleo chico, con lo mínimo para que el sistema funcione, de plugins que agregan capacidades y se enchufan por un contrato que define el núcleo. Sirve cuando el producto se extiende o se personaliza mucho por cliente o por caso de uso: lo que cambia va a los plugins y el núcleo casi no se toca. El riesgo es el contrato: si el núcleo cambia su interfaz, se rompen todos los plugins.

## Cuándo alcanza un estilo simple

Para un sistema chico, de un equipo, con un dominio que no se va a partir entre varios equipos, un estilo simple puede ser todo lo que hace falta. Cuándo conviene pasar a uno partido por dominio se decide desde las características, como cuenta [Elegir un estilo](elegir-un-estilo.md).

Para leer más: los capítulos de capas, pipeline y microkernel de Richards y Ford (2ª ed.), fijándose en la tabla de calificaciones de cada uno y en cuándo no usarlo.
