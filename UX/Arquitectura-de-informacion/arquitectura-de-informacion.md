---
resumen: >-
  La arquitectura de información decide cómo se agrupa, se nombra y se encuentra el contenido de un producto: es la estructura y el vocabulario que la interacción después recorre.
estado: borrador
estabilidad: estable
fuentes:
  - "Louis Rosenfeld, Peter Morville y Jorge Arango, Information Architecture: For the Web and Beyond, 4.ª ed., O'Reilly, octubre de 2015 (solo índice y ficha, vía https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/part02.html)"
  - "NN/g, Tankala y Sherwin, Card Sorting: Uncover Users' Mental Models for Better Information Architecture, 2 de febrero de 2024: https://www.nngroup.com/articles/card-sorting-definition/"
  - "NN/g, Laubheimer, Tree Testing, 6 de agosto de 2023: https://www.nngroup.com/articles/tree-testing/"
  - "NN/g, Budiu, Information Scent: How Users Decide Where to Go Next, 2 de febrero de 2020: https://www.nngroup.com/articles/information-scent/"
  - "UX/.investigacion/arquitectura-e-interaccion.md"
aliases: [AI, information architecture, IA]
creado: 2026-11-22
revisado:
---

# Arquitectura de información

La arquitectura de información decide cómo se agrupa, se nombra y se encuentra el contenido de un producto: es la estructura y el vocabulario que la interacción después recorre.

Es la capa que ordena lo que hay antes de decidir cómo se opera. Recibe de [Investigación](../Investigacion/investigacion.md) el lenguaje y las tareas de la gente, y le entrega a [Interacción](../Interaccion/interaccion.md) una estructura para recorrer. Esta base la apoya en el [modelo mental](../Percepcion-y-decision/modelo-mental.md): infiere que una organización funciona cuando coincide con cómo la persona cree que están agrupadas las cosas, sin una fuente que lo mida.

## Los cuatro sistemas de Rosenfeld, Morville y Arango

El libro de referencia del campo, *Information Architecture: For the Web and Beyond* (4.ª edición, 2015), se organiza en cuatro sistemas: organización, etiquetado, navegación y búsqueda. Esa división se tomó de resúmenes: el índice de la editorial muestra que la segunda parte cubre la anatomía de una arquitectura, la organización y el etiquetado, y un registro de biblioteca lista además navegación y búsqueda. No se pudo leer la definición literal de cada sistema, así que lo que sigue es la lectura de esta base.

| Sistema | Qué decide | Dónde está |
|---|---|---|
| Organización | Cómo se agrupa y se ordena el contenido | Esta nota |
| Etiquetado | Cómo se llama cada grupo, enlace y botón | Esta nota |
| Navegación | Cómo se mueve la persona por la estructura | [Navegación](navegacion.md) |
| Búsqueda | Cómo se encuentra el contenido sin recorrer la estructura | Esta nota, en pocas líneas; falta su nota |

La frontera con la interacción es una síntesis de esta base, sin una fuente que la formule así: la arquitectura decide cómo se agrupa, se llama y se encuentra el contenido; la interacción decide cómo se opera (controles, estados, respuesta).

## Organizar es elegir cómo agrupar

Todo catálogo de contenido admite varios agrupamientos posibles: por tema, por tarea, por tipo de usuario, por fecha. Es una inferencia de esta base que la elección importa porque la persona busca con el agrupamiento que ya tiene en la cabeza. El método para averiguarlo es el card sorting: según NN/g, los participantes "place individually labeled cards into groups according to criteria that make the most sense to them". Lo que agrupan informa sobre sus modelos mentales y no es todavía un diseño terminado.

Un recurso canónico para este tema es el libro de Rosenfeld, Morville y Arango, en los capítulos de sistemas de organización y de etiquetado (los números de capítulo del índice de O'Reilly están por verificar). Los capítulos no se leyeron; la investigación sugiere fijarse en la distinción entre esquemas de organización exactos (alfabético, cronológico) y ambiguos (por tema), y en el etiquetado con el lenguaje del usuario y no el de la empresa.

## Las etiquetas alimentan el olor de información

Esta base infiere que una etiqueta ambigua o interna esconde el contenido aunque esté bien ubicado; ninguna fuente leída lo mide. La teoría del olor de información (information scent) da el mecanismo: según NN/g, el olor de una fuente es la "imperfect estimate" que hace el usuario del valor que le entregará, derivada de una representación de la fuente, y en un menú esa representación es la etiqueta. Las guías de NN/g piden etiquetas específicas y autoexplicativas (evitar "Más"), en el lenguaje del público y coherentes con el destino. El detalle está en [Navegación](navegacion.md).

## Cómo se comprueba una estructura

El card sorting averigua cómo agrupa la gente antes de diseñar. El árbol de prueba (tree testing) comprueba después una jerarquía propuesta: según el resumen de NN/g, se pide a usuarios que encuentren dónde estaría un recurso dentro de categorías anidadas. El método vive en [Evaluación](../Evaluacion/evaluacion.md) y se elige con la tabla de [métodos de investigación](../Investigacion/metodos-de-investigacion.md).

## Qué hay adentro

- [Navegación](navegacion.md): los tipos de navegación, las migas de pan, el olor de información y la evidencia sobre menú hamburguesa y mega menús, con fechas.

## Qué falta

Quedan por escribir, y no tienen nota todavía: el card sorting como práctica, el árbol de prueba, la búsqueda y los filtros (con las facetas para catálogos) y el etiquetado como nota propia.

> [!NOTE]
> Sin fuente todavía: facetas para catálogos de producto, y la definición literal de cada uno de los cuatro sistemas en el libro de Rosenfeld, Morville y Arango.
