---
resumen: >-
  Una historia de usuario describe una funcionalidad desde quien la usa ("Como… quiero… para…")
  y se cierra con criterios de aceptación verificables; una épica agrupa historias de un mismo
  objetivo.
estado: borrador
estabilidad: estable
fuentes:
  - "Agile Alliance, User Stories: https://www.agilealliance.org/glossary/user-stories/"
  - "Agile Alliance, User Story Template: https://agilealliance.org/glossary/user-story-template/"
  - "Mountain Goat Software, User Stories: https://www.mountaingoatsoftware.com/agile/user-stories"
  - "Mike Cohn, User Stories Applied (Addison-Wesley, 2004) (no leído): https://www.mountaingoatsoftware.com/books/user-stories-applied"
  - "Bill Wake, INVEST in Good Stories, and SMART Tasks (2003): https://xp123.com/invest-in-good-stories-and-smart-tasks/"
  - "Jeff Patton Associates, User Story Mapping: https://www.jpattonassociates.com/user-story-mapping/"
  - "Jeff Patton, User Story Mapping (O'Reilly, 2014) (no leído): https://www.oreilly.com/library/view/user-story-mapping/9781491904893/"
  - "Archivo/Desarrollo/epicas-historias-usuario-ecommerce.md (original)"
aliases: [User story, HU, Historia, Épica, Epic]
creado: 2026-10-03
revisado:
---

# Historia de usuario

Una historia de usuario describe una funcionalidad desde quien la usa ("Como… quiero… para…") y se cierra con criterios de aceptación verificables; una épica agrupa historias de un mismo objetivo.

En [Definición](definicion.md), la historia es la unidad de valor: lo que el cliente puede ver, usar y aceptar. La [especificación](especificacion.md) agrega el detalle que necesita quien construye, los [criterios de aceptación](criterios-de-aceptacion.md) dicen cuándo está terminada y la [descomposición en tareas](descomposicion-en-tareas.md) la parte en unidades de trabajo para una persona o un agente.

## Para quién y para qué

Una especificación técnica ("agregar un endpoint con filtro por categoría") dice qué construir, pero no para quién ni para qué; sin eso, no se puede decidir qué recortar ni cuándo está terminada. La historia obliga a nombrar al usuario y el beneficio. Para Cohn es "a short description of desired functionality", contada desde quien la necesita.

La plantilla más usada es "Como [rol] quiero [acción] para [beneficio]". Según la Agile Alliance, ese formato de rol, funcionalidad y razón se inventó en 2001 en Connextra, una empresa del Reino Unido, y por eso se lo llama formato Connextra. La versión de Cohn es "As a [type of user], I [need/want/am required] to [do something], so that [reason or benefit]".

## La tarjeta, la conversación y la confirmación

Ron Jeffries describió la historia en tres partes, que Cohn y la Agile Alliance recogen como las tres C. La tarjeta (*card*) es la frase corta que la identifica. La conversación (*conversation*) es donde se acuerdan los detalles con quien la pide: "The conversation is where understanding grows." La confirmación (*confirmation*) son los criterios de aceptación que prueban que se cumplió.

La historia, entonces, no es una especificación completa: es el motivo de una conversación. Con agentes eso se nota más, porque el agente no estuvo en la conversación. Lo que se acordó hablando tiene que quedar escrito en la especificación y en los criterios, o el agente no lo va a saber.

Los criterios se escriben a menudo como dado, cuando, entonces: un contexto, una acción y un resultado observable, que se contestan con un sí o un no. Cómo se escriben, cómo se descubren con Example Mapping y cómo se convierten en un chequeo que ejecuta un agente está en [criterios de aceptación](criterios-de-aceptacion.md).

## El chequeo INVEST

Bill Wake propuso en 2003 el chequeo INVEST: una buena historia es independiente, negociable, valiosa, estimable, pequeña (entra en una iteración) y testeable. Si no es pequeña, es una épica y se parte en historias, por ejemplo una por operación o una por regla de negocio. Los patrones para partirla sin cortar por capas están en [descomposición en tareas](descomposicion-en-tareas.md).

## El mapa de historias

Una lista plana de historias no muestra cómo se relacionan ni qué falta. Jeff Patton propuso ordenarlas en un mapa: "A user story map arranges user stories into a useful model" del sistema, que sirve para ver huecos y planear entregas que den valor. El método combina el modelado de tareas de Constantine y Lockwood con talleres de escritura de historias, y su forma de planificar se describió primero en el artículo "How You Slice It" (*Better Software*, enero de 2005).

La columna vertebral del mapa, el esqueleto andante y los cortes de entrega se explican en [dar forma a una solución](../../Producto/Descubrimiento/dar-forma-a-una-solucion.md), en Producto, porque el mapa decide qué entra en cada entrega antes de que haya historias para escribir. Cómo se convierten esos cortes en incrementos para el cliente está en [plan de entregas](../Encargo/plan-de-entregas.md).

## Filtrar el catálogo por categoría

Como cliente de la tienda quiero filtrar productos por categoría para ver solo los que me interesan.

La historia es parte de la épica "Gestión del catálogo", junto con búsqueda por nombre, búsqueda por palabra clave y paginado. Sus criterios, escritos como dado/cuando/entonces, están en [criterios de aceptación](criterios-de-aceptacion.md#dado-cuando-entonces).

## Historia y tarea técnica

Una tarea técnica, como "crear el índice GIN en la tabla de productos", no tiene usuario ni beneficio visible. Es un paso para cumplir una historia y se planifica dentro de ella. Si una historia necesita varias tareas técnicas, cada una lleva su propio chequeo, como se explica en [descomposición en tareas](descomposicion-en-tareas.md).
