---
resumen: >-
  Los criterios de aceptación son los ejemplos concretos y verificables que dicen cuándo un cambio
  está terminado; escritos como contexto, acción y resultado observable, se convierten en pruebas, y
  con agentes de código son el contrato de terminado que da pasa o falla.
estado: borrador
estabilidad: estable
fuentes:
  - https://www.manning.com/books/specification-by-example
  - https://martinfowler.com/bliki/GivenWhenThen.html
  - https://cucumber.io/docs/gherkin/reference/
  - https://cucumber.io/blog/bdd/example-mapping-introduction/
  - https://code.claude.com/docs/en/best-practices
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://www.mountaingoatsoftware.com/agile/user-stories
aliases: [acceptance criteria, criterio de aceptación, dado cuando entonces, given when then, Gherkin, BDD, especificación por ejemplos, specification by example, example mapping, definición de terminado]
creado: 2026-11-27
revisado:
---

# Criterios de aceptación

Los criterios de aceptación son los ejemplos concretos y verificables que dicen cuándo un cambio está terminado; escritos como contexto, acción y resultado observable, se convierten en pruebas, y con agentes de código son el contrato de terminado que da pasa o falla.

En la [historia de usuario](historia-de-usuario.md) son la confirmación, la tercera de las tres C de Ron Jeffries que recoge Cohn. En una [especificación](especificacion.md) son la parte de "terminado". Cada [tarea](descomposicion-en-tareas.md) tiene los suyos. Del otro lado, [Verificación](../Verificacion/verificacion.md) los convierte en pruebas, y el cliente acepta un incremento contra ellos en [alcance y aceptación](../Encargo/alcance-y-aceptacion.md).

## Ejemplos antes que reglas

Una regla en prosa ("el sistema valida el stock") deja abierto qué pasa en cada caso. Un ejemplo ("con 3 unidades en stock, un pedido de 5 se rechaza") no. Adzic, en *Specification by Example*, describe un ciclo que va de derivar el alcance desde los objetivos a especificar en colaboración, ilustrar con ejemplos, refinar y automatizar la validación sin cambiar las especificaciones; el resultado es documentación viva (según su descripción e índice, el libro no se leyó).

Criterio de esta base: un criterio sirve si se puede contestar con un sí o un no, y si lo puede contestar alguien que no lo escribió.

## Dado, cuando, entonces

La forma más usada es dado/cuando/entonces (*given-when-then*), que Fowler define como "a style of representing tests", desarrollado por Daniel Terhorst-North y Chris Matts dentro de BDD. Dado fija el estado inicial; cuando, la acción o el evento; entonces, el resultado. Gherkin, el lenguaje de Cucumber, la formaliza y da reglas que valen aunque no se use la herramienta:

- El entonces afirma "an observable outcome", algo que ve el usuario o un sistema externo, y no estado interno como un registro en la base.
- De tres a cinco pasos por ejemplo, y un contexto común (*Background*) corto, de menos de unas cuatro líneas.
- "Describe behavior, not implementation".
- Los ejemplos de una misma regla de negocio se agrupan bajo `Rule`, y los que solo cambian datos van en una tabla de ejemplos (*Scenario Outline*).

Para la historia "como cliente de la tienda quiero filtrar productos por categoría para ver solo los que me interesan":

- Dado que existe la categoría "Bebidas" con 12 productos, cuando consulto el catálogo filtrando por "Bebidas", entonces obtengo solo esos 12.
- Dado que la categoría "Vinos" no existe, cuando filtro por ella, entonces obtengo una lista vacía con un mensaje que lo indica.
- Dado que "Bebidas" tiene 12 productos y 2 están sin stock, cuando filtro por "Bebidas", entonces los 2 aparecen marcados como sin stock.

Lectura de esta base: el tercer ejemplo es el que un agente no adivina, porque fija una regla que no estaba en la frase de la historia. En una API REST, cada uno de estos ejemplos se vuelve uno o más casos de prueba, como se arma en [diseñar casos de prueba de una API](../Verificacion/disenar-casos-de-prueba-de-api.md).

Gherkin no obliga a nada: el valor está en los ejemplos concretos, no en la sintaxis. Escribirlos en prosa ordenada alcanza si no se van a ejecutar con Cucumber. Esto es lectura de esta base; no hay fuente que mida el costo de mantener escenarios en Gherkin.

## Encontrar los ejemplos con Example Mapping

Example Mapping, de Matt Wynne, es una conversación corta para sacar los criterios antes de construir. Se usan tarjetas de cuatro colores: amarilla para la historia, azules para las reglas, verdes para los ejemplos de cada regla y rojas para las preguntas que nadie en la sala puede contestar. Wynne calcula "about 25 minutes" para una historia bien entendida y de tamaño razonable, y cierra con una votación rápida de si está lista.

El mapa también diagnostica. Muchas tarjetas rojas dicen que falta aprender antes de construir; muchas azules, que la historia es grande y hay que [partirla](descomposicion-en-tareas.md); una regla con muchos ejemplos puede ser varias reglas. Las rojas son la lista de preguntas para el cliente antes de soltar a un agente, una conexión que hace esta base con la evidencia de que los agentes no detectan bien lo que falta (está en [especificación](especificacion.md)).

## El criterio que un agente ejecuta

Con agentes, el criterio deja de ser texto para leer y pasa a ser algo que se corre. Anthropic recomienda darle al agente "something it can run that comes back pass or fail": una prueba, el código de salida del build, un linter, una comparación contra un archivo de referencia o una captura contra el diseño. También pide evidencia, el comando y su salida, porque que diga que todas las pruebas pasan dice poco.

La razón es una falla documentada. En un arnés para trabajos largos, Anthropic vio que el agente tendía a "declare the job done" demasiado pronto y a marcar funcionalidades como completas sin probarlas. El arnés expande el pedido en una lista de funcionalidades en JSON, todas marcadas al principio como falladas, donde el agente solo podía cambiar el estado; eligieron JSON porque los modelos lo alteran menos que Markdown. Las pruebas de punta a punta con automatización de navegador mejoraron mucho el resultado frente a pruebas unitarias y llamadas sueltas.

Regla de esta base: un criterio que no se puede ejecutar se acepta solo si una persona lo comprueba, y eso se dice en el criterio. Cómo se escribe la prueba antes que el código está en [TDD](../Verificacion/tdd.md); a qué nivel conviene cada prueba, en [pirámide de pruebas](../Verificacion/piramide-de-pruebas.md); y cómo se revisa que el agente no haya hecho trampa con las pruebas, en [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md).

Los criterios sobre cualidades (rendimiento, seguridad, costo) se escriben con número y se ejecutan como [fitness function](../../Arquitectura/Caracteristicas/fitness-function.md).
