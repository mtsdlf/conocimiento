---
resumen: >-
  Una historia de usuario describe una funcionalidad desde quien la usa ("Como… quiero… para…")
  y se cierra con criterios de aceptación verificables; una épica agrupa historias de un mismo
  objetivo.
estado: borrador
estabilidad: estable
revisado:
creado: 2026-10-03
fuentes:
  - "Agile Alliance, User Stories: https://www.agilealliance.org/glossary/user-stories/"
  - "Agile Alliance, User Story Template: https://agilealliance.org/glossary/user-story-template/"
  - "Bill Wake, INVEST in Good Stories, and SMART Tasks (2003): https://xp123.com/invest-in-good-stories-and-smart-tasks/"
  - "Cucumber, Gherkin Reference: https://cucumber.io/docs/gherkin/reference/"
  - "Archivo/Desarrollo/epicas-historias-usuario-ecommerce.md (original)"
aliases: [User story, HU, Historia, Épica, Epic, Criterios de aceptación]
---

# Historia de usuario

Una historia de usuario describe una funcionalidad desde quien la usa ("Como… quiero… para…")
y se cierra con criterios de aceptación verificables; una épica agrupa historias de un mismo
objetivo.

## Para quién y para qué

Una especificación técnica ("agregar un endpoint con filtro por categoría") dice qué construir,
pero no para quién ni para qué; sin eso, no se puede decidir qué recortar ni cuándo está
terminada. La historia obliga a nombrar el usuario y el beneficio, y los criterios de aceptación
fijan cuándo está hecha.

## Connextra, las tres C, Gherkin e INVEST

La plantilla "Como [rol] quiero [acción] para [beneficio]" se conoce como formato Connextra: nació
en 2001 en esa empresa británica y Mike Cohn la difundió en *User Stories Applied*. Según la Agile
Alliance, una historia tiene tres partes, las tres C de Ron Jeffries:

- **Card** (tarjeta): la frase corta que la identifica.
- **Conversation** (conversación): los detalles se acuerdan hablando con quien la pide.
- **Confirmation** (confirmación): los criterios de aceptación que prueban que se cumplió.

Los criterios se escriben a menudo en la forma de Gherkin, **Dado** (contexto), **Cuando**
(acción) y **Entonces** (resultado observable). Cada criterio tiene que poder verificarse con un
sí o un no, y se convierte en uno o más casos de prueba
([Diseñar casos de prueba de una API](disenar-casos-de-prueba-de-api.md)).

Bill Wake propuso el chequeo INVEST: una buena historia es independiente, negociable, valiosa,
estimable, pequeña (entra en una iteración) y testeable. Si no es pequeña, es una **épica**: se
parte en historias, por ejemplo una por operación o por regla.

## Filtrar el catálogo por categoría

**Como** cliente de la tienda **quiero** filtrar productos por categoría **para** ver solo los que
me interesan.

- **Dado** que existe la categoría "Bebidas" con 12 productos, **cuando** consulto el catálogo
  filtrando por "Bebidas", **entonces** obtengo solo esos 12.
- **Dado** que la categoría no existe, **cuando** filtro por ella, **entonces** obtengo una lista
  vacía con un mensaje que lo indica.

Esta historia es parte de la épica "Gestión del catálogo", junto con búsqueda por nombre,
búsqueda por palabra clave y paginado.

## Historia y tarea técnica

Una tarea técnica. "Crear el índice GIN en la tabla de productos" no tiene usuario ni beneficio
visible: es un paso para cumplir una historia y se planifica dentro de ella.
