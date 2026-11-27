---
resumen: >-
  Definición es la parte del desarrollo que convierte una intención acordada en algo que se puede
  construir sin adivinar: qué cambia, con qué palabras del negocio, en qué tareas se parte y con qué
  ejemplos se comprueba que está terminado, sea una persona o un agente quien lo construya.
estado: borrador
estabilidad: estable
fuentes:
  - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
  - https://www.thoughtworks.com/radar/techniques/spec-driven-development
  - https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
  - https://arxiv.org/abs/2608.25202
  - https://arxiv.org/abs/1609.04886
  - https://arxiv.org/abs/2502.13069
  - https://code.claude.com/docs/en/best-practices
  - https://learn.chatgpt.com/guides/best-practices
  - https://standards.ieee.org/ieee/29148/6937
  - "Desarrollo/.investigacion/definicion.md y posicion-contraria.md (2026-11-27)"
aliases: [requisitos, ingeniería de requisitos, requirements, especificación y prueba, definir el trabajo]
creado: 2026-11-19
revisado:
---

# Definición

Definición es la parte del desarrollo que convierte una intención acordada en algo que se puede construir sin adivinar: qué cambia, con qué palabras del negocio, en qué tareas se parte y con qué ejemplos se comprueba que está terminado, sea una persona o un agente quien lo construya.

Dentro de [Desarrollo](../desarrollo.md) es el primer paso del ciclo técnico. Recibe de [Encargo](../Encargo/encargo.md) el alcance acordado con el cliente, con lo que entra, lo que no y cómo se va a aceptar ([alcance y aceptación](../Encargo/alcance-y-aceptacion.md)). Le pasa a [Construcción](../Construccion/construccion.md) tareas chicas, cada una con sus criterios. Esos mismos criterios son los que después usa [Verificación](../Verificacion/verificacion.md) para decir si lo construido hace lo que se pidió.

Antes de Definición está la decisión de qué construir, que es de Producto: el [descubrimiento](../../Producto/Descubrimiento/descubrimiento.md) elige una solución y [dar forma a una solución](../../Producto/Descubrimiento/dar-forma-a-una-solucion.md) la deja en un nivel de detalle con el que se puede apostar. Definición empieza cuando esa solución ya está elegida.

## Qué tiene que estar escrito antes de que se escriba código

Las guías de los fabricantes de agentes coinciden en lo mínimo que tiene que estar escrito para un agente. OpenAI pide estructurar el pedido con objetivo, contexto, restricciones y una condición de "Done when". Anthropic recomienda darle al agente "something it can run that comes back pass or fail" y, antes de dejarlo trabajar solo, preguntarse primero si sabe qué es estar terminado: "A goal condition, a spec file, or a failing test it has to turn green."

De ahí salen los cuatro productos de esta vertical, que se apoyan uno en otro:

| Se escribe | Responde | Componente |
|---|---|---|
| La especificación del cambio | qué tiene que hacer, con qué restricciones y qué queda abierto | [especificación](especificacion.md) |
| Las historias | para quién es y qué valor le da | [historia de usuario](historia-de-usuario.md) |
| Los ejemplos verificables | cómo se sabe que está terminado | [criterios de aceptación](criterios-de-aceptacion.md) |
| Las tareas | en qué pedazos se construye y se comprueba | [descomposición en tareas](descomposicion-en-tareas.md) |

Por debajo de los cuatro corre el [modelo de dominio](modelo-de-dominio.md): el vocabulario del negocio, que tiene que ser el mismo en la conversación con el cliente, en la especificación y en el código. Según blogs de practicantes, sin medición, un agente tiende a mezclar o inventar términos: dos palabras para la misma cosa pueden terminar como dos conceptos en el código.

## El documento gigante pierde peso, la especificación por tramos gana

El documento de requisitos completo, escrito al principio y congelado, pierde peso. Al mismo tiempo, el desarrollo guiado por especificaciones vuelve a poner un texto escrito antes del código, y lo hace el insumo principal del agente.

Lo que pierde peso es la forma, no la idea de escribir antes. Böckeler, que probó las herramientas de especificación para agentes, dice: "I'm very skeptical that lots of up-front spec design is a good idea" y "The past has shown that the best way for us to stay in control of what we're building are small, iterative steps". Según su resumen, el estudio de Agarwal y otros sobre la práctica real (21 entrevistas y 266 repositorios, preprint) encuentra que las especificaciones se usan de forma selectiva, sobre todo en funcionalidades nuevas, y que las que traen detalles de implementación tienden a quedar viejas. Menzies y otros, sobre 171 proyectos, no encontraron evidencia consistente de que arreglar un defecto tarde cueste mucho más (según su resumen), lo que debilita el argumento económico de especificar todo antes.

> [!IMPORTANT]
> No hay un estudio que compare el documento de requisitos completo con la especificación por tramos. Que pierda peso el documento único y congelado, y no la especificación de cada cambio chico, es criterio de esta base, apoyado en Böckeler (práctica) y en Menzies (indirecto). Las normas siguen describiendo documentos de requisitos: ISO/IEC/IEEE 29148:2018 "defines the construct of a good requirement, provides attributes and characteristics of requirements".

Criterio de esta base: de las normas sigue sirviendo el vocabulario de qué hace bueno a un requisito y la diferencia entre requisito y diseño. Cómo se aplica eso a una especificación chica está en [especificación](especificacion.md).

## La evidencia sobre especificar para agentes es mixta

El desarrollo guiado por especificaciones (spec-driven development) es una práctica emergente. Los tres niveles con que se lo describe (la especificación antes de la tarea, la que se conserva y evoluciona, y la que reemplaza al código como fuente) son una clasificación de Böckeler, no un estándar.

> [!IMPORTANT]
> No hay estudio empírico que respalde el desarrollo guiado por especificaciones con agentes. Hill (ESEM 2026), sobre 88.052 pull requests de 119 repositorios, no encontró efecto de la calidad de la especificación sobre defectos (p = 0,164) ni sobre retrabajo (p = 0,860); el propio autor aclara que lo medido son sobre todo enlaces a tickets y que ningún repositorio de la muestra versiona la salida de herramientas de especificación. A favor hay solo evidencia acotada, sobre generación de pruebas. Thoughtworks lo puso en "Assess" en su Radar de noviembre de 2025. El detalle está en [especificación](especificacion.md).

Las guías de Anthropic y OpenAI piden, como base de todo, un chequeo que dé pasa o falla; es práctica recomendada por los fabricantes, no resultado de estudios. Vive en [criterios de aceptación](criterios-de-aceptacion.md).

## La ambigüedad se cierra antes de construir

Los agentes no detectan bien lo que falta en un pedido. En el estudio Ambig-SWE (ICLR 2026), los modelos tuvieron dificultad para distinguir tareas bien especificadas de subespecificadas y por defecto no preguntaban; cuando se los dejaba interactuar, el rendimiento en las tareas subespecificadas mejoró hasta un 74 % (según su resumen). Por eso una especificación lleva sus preguntas abiertas y sus supuestos a la vista, y conviene que el agente esté configurado para preguntar.

La guía de Anthropic propone invertir la entrevista cuando el pedido no está pensado del todo: que el agente entreviste a la persona "until you could write the spec", y que la construcción arranque en una sesión nueva "so the build begins with a clean context and a written definition of done". Las preguntas que no se pueden contestar en la sala son las que hay que llevarle al cliente, y con eso se vuelve a [Encargo](../Encargo/encargo.md).

## Lo que esta vertical deja a otros temas

Las cualidades que el sistema tiene que tener además de su función (rendimiento, disponibilidad, seguridad, costo), que se suelen llamar requisitos no funcionales, son [características arquitectónicas](../../Arquitectura/Caracteristicas/caracteristicas-arquitectonicas.md) y viven en Arquitectura. Una especificación las nombra como criterio medible, y su forma ejecutable es una [fitness function](../../Arquitectura/Caracteristicas/fitness-function.md).

El prototipo como herramienta para decidir qué construir está en Producto: la [prueba de supuestos](../../Producto/Descubrimiento/prueba-de-supuestos.md) lo usa para probar una idea, y [dar forma a una solución](../../Producto/Descubrimiento/dar-forma-a-una-solucion.md) discute si un prototipo puede servir como especificación.

## Las notas de Definición

- [Especificación](especificacion.md): qué lleva el texto que fija un cambio, cómo se dimensiona, los tres niveles del desarrollo guiado por especificaciones y su evidencia.
- [Historia de usuario](historia-de-usuario.md): la unidad de valor: para quién, qué y para qué, con INVEST y el mapa de historias.
- [Criterios de aceptación](criterios-de-aceptacion.md): ejemplos concretos como contrato de terminado, del dado/cuando/entonces al chequeo que ejecuta un agente.
- [Descomposición en tareas](descomposicion-en-tareas.md): rebanadas verticales que se construyen y se verifican solas; el tamaño de tarea para un agente.
- [Modelo de dominio](modelo-de-dominio.md): el lenguaje del negocio, cómo se descubre con el cliente y cómo se fija para que el agente lo use.

Los casos de prueba de una API REST, que salen de los criterios, están en [diseñar casos de prueba de una API](../Verificacion/disenar-casos-de-prueba-de-api.md), en Verificación.
