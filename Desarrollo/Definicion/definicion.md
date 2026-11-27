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

El documento de requisitos completo, escrito al principio y congelado, pierde peso, mientras el desarrollo guiado por especificaciones vuelve a poner un texto escrito antes del código como insumo principal del agente. Lo que pierde peso es la forma, no la idea de escribir antes: como criterio de esta base, sin un estudio que compare las dos, cede el documento único y gana la especificación por tramos; quién lo dice y con qué evidencia está en [lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-desarrollo.md#el-documento-de-requisitos-gigante-y-congelado).

Criterio de esta base: de las normas, que siguen describiendo documentos de requisitos, sirve el vocabulario de qué hace bueno a un requisito y la diferencia entre requisito y diseño. Cómo se aplica eso a una especificación chica está en [especificación](especificacion.md#qué-hace-bueno-a-un-requisito).

## La evidencia sobre especificar para agentes es mixta

El desarrollo guiado por especificaciones (spec-driven development) es una práctica emergente. Sus [tres niveles](especificacion.md#los-tres-niveles-del-desarrollo-guiado-por-especificaciones) son una clasificación de Böckeler, no un estándar.

> [!IMPORTANT]
> No hay estudio empírico que respalde el desarrollo guiado por especificaciones con agentes. Hill (ESEM 2026), sobre 88.052 pull requests de 119 repositorios, no encontró efecto de la calidad de la especificación sobre defectos (p = 0,164) ni sobre retrabajo (p = 0,860); el propio autor aclara que lo medido son sobre todo enlaces a tickets y que ningún repositorio de la muestra versiona la salida de herramientas de especificación. A favor hay solo evidencia acotada, sobre generación de pruebas. Thoughtworks lo puso en "Assess" en su Radar de noviembre de 2025. El detalle está en [especificación](especificacion.md).

Las guías de Anthropic y OpenAI piden, como base de todo, un chequeo que dé pasa o falla; es práctica recomendada por los fabricantes, no resultado de estudios. Vive en [criterios de aceptación](criterios-de-aceptacion.md).

## La ambigüedad se cierra antes de construir

Los agentes no detectan bien lo que falta en un pedido y por defecto no preguntan, según el estudio Ambig-SWE que se cuenta en [especificación](especificacion.md#las-partes-de-una-especificación-de-un-cambio); por eso una especificación lleva sus preguntas abiertas y sus supuestos a la vista, y conviene que el agente esté configurado para preguntar.

Cuando el pedido no está pensado del todo, la guía de Anthropic propone invertir la entrevista: el agente entrevista a la persona y la construcción arranca en una sesión nueva, como cuenta [especificación](especificacion.md#escribirla-con-el-agente-y-construir-con-otro-contexto). Las preguntas que no se pueden contestar en la sala son las que hay que llevarle al cliente, y con eso se vuelve a [Encargo](../Encargo/encargo.md).

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
