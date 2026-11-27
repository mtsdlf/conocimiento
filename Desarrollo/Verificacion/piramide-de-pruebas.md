---
resumen: >-
  La pirámide de pruebas es el modelo que reparte las pruebas automáticas por nivel: muchas rápidas y
  aisladas abajo, menos de integración en el medio y pocas de extremo a extremo arriba. Sus
  alternativas (el trofeo, el panal) discuten la forma; esta base toma como criterio propio que lo común es
  probar en la frontera con pocas pruebas lentas.
estado: borrador
estabilidad: estable
fuentes:
  - https://martinfowler.com/articles/practical-test-pyramid.html
  - https://martinfowler.com/bliki/TestPyramid.html
  - https://engineering.atspotify.com/2018/01/testing-of-microservices/
  - https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications
  - https://martinfowler.com/bliki/ContractTest.html
  - https://code.claude.com/docs/en/best-practices
aliases: [test pyramid, pirámide de tests, testing trophy, trofeo de pruebas, testing honeycomb, panal de pruebas, pruebas de contrato, contract testing, consumer-driven contracts]
creado: 2026-11-27
revisado:
---

# Pirámide de pruebas

La pirámide de pruebas es el modelo que reparte las pruebas automáticas por nivel: muchas rápidas y aisladas abajo, menos de integración en el medio y pocas de extremo a extremo arriba. Sus alternativas (el trofeo, el panal) discuten la forma; esta base toma como criterio propio que lo común es probar en la frontera con pocas pruebas lentas.

## De dónde sale y qué recomienda

Según el artículo de Ham Vocke en el sitio de Fowler, Mike Cohn introdujo la pirámide en *Succeeding with Agile* (libro que esta base no leyó), con tres capas: unidad, servicio e interfaz de usuario. Fowler agrega que Cohn la popularizó en 2009 y que la había dibujado con Lisa Crispin en 2003-2004. El mismo artículo admite que los nombres de las capas confunden y que el modelo es simplista.

La regla que deja es una sola: "Push your tests as far down the test pyramid as you can". Las pruebas de extremo a extremo por la interfaz son, para Fowler, "brittle, expensive to write, and time consuming to run", y sirven como "a second line of test defense". Cuando una de ellas falla, se escribe una prueba de unidad que reproduzca el error. Vocke advierte: "Watch out that you don't end up with a test ice-cream cone".

## Tres formas para la misma pregunta

> [!IMPORTANT]
> Cuántas pruebas poner en cada nivel está en discusión, y cada forma responde a un tipo de sistema.
> - **Pirámide** (Cohn, Fowler): mayoría de pruebas de unidad, con pocas de extremo a extremo arriba.
> - **Panal** (Spotify, 2018, para microservicios): mayoría de pruebas de integración del servicio por sus puntos de interacción (REST o mensajes), pocas de detalle de implementación e idealmente ninguna que dependa de que otro sistema ande bien. El argumento: en microservicios la complejidad está en las interacciones, y muchas pruebas de unidad atan las pruebas a la implementación, de modo que refactorizar obliga a reescribirlas. El costo que admiten: pruebas más lentas (de milisegundos a pocos segundos) y mensajes de falla menos precisos.
> - **Trofeo** (Kent C. Dodds, para monolitos de una sola base de código, centrado en frontend): capas de análisis estático, unidad, integración y extremo a extremo, con integración como la más ancha. Su criterio: "The more your tests resemble the way your software is used, the more confidence they can give you."

Debajo del desacuerdo hay un problema de vocabulario. "Unidad" no tiene una definición común, y la discusión de porcentajes por nivel tapa lo que importa, según el resumen del texto de Dodds: pruebas rápidas, confiables y que fallen por buenas razones. Esta base toma eso como criterio. Elegir la forma según el tipo de sistema (la pirámide para un servicio con pocas dependencias, el panal para servicios que se hablan) también es criterio de esta base: ninguna fuente leída lo compara.

## Las pruebas de contrato

Una prueba de contrato verifica la frontera entre dos sistemas sin levantar los dos a la vez. Fowler distingue dos sentidos.

En el primero, la prueba comprueba que los dobles de prueba de un servicio externo respondan igual que el servicio real: "These check that all the calls against your test doubles return the same results as a call to the external service would." Corren periódicamente y no en cada commit.

En el segundo, el contrato lo dirige el consumidor. El equipo que consume la API publica lo que necesita de ella como pruebas, y el equipo proveedor corre copias de esas pruebas en su pipeline. El artículo de Vocke lo muestra con Pact y marca el límite: dentro de una organización se pueden cubrir todos los consumidores; en una API pública, normalmente no.

Esto es lo que le falta a [diseñar casos de prueba de una API](disenar-casos-de-prueba-de-api.md), que parte del contrato OpenAPI pero no verifica que proveedor y consumidores sigan de acuerdo. Como criterio de esta base, en una arquitectura de [microservicios](../../Arquitectura/Estilos/microservicios.md) las pruebas de contrato son una forma de empujar hacia abajo las de extremo a extremo; ninguna fuente leída lo mide.

## Qué cambia cuando las pruebas las escribe un agente

Con un agente, escribir muchas pruebas de unidad cuesta casi nada; el cuello pasa a ser que valgan algo y que no queden atadas a la implementación. Es inferencia de esta base: el argumento del panal pesa más cuando un agente refactoriza seguido. No se encontró un estudio que compare formas de suite con código escrito por agentes.

Por inferencia de esta base, las pruebas de contrato ganan peso por la misma razón: un agente trabaja en una zona del código, y el contrato es el límite que no debería romper aunque cambie todo lo de adentro. Para saber si las pruebas que escribió un agente detectan fallas, la herramienta es la mutación, en [verificar lo que hizo un agente](verificar-lo-que-hizo-un-agente.md).

La guía de buenas prácticas de Anthropic para su agente de código (leída el 2026-11-27) pide darle "the exact test, typecheck, and lint commands, and how to run a single test file". Eso sirve a cualquier nivel. Que exija pruebas rápidas y deterministas es inferencia de esta base: una suite lenta o inestable le daría al agente una señal pobre.

## El recurso para leer

"The Practical Test Pyramid", de Ham Vocke en el sitio de Fowler: las secciones de pruebas de integración, de contrato y de extremo a extremo. Conviene fijarse en la regla de empujar las pruebas hacia abajo y en el apartado de contratos dirigidos por el consumidor. Cómo encaja la suite en el pipeline está en [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md).
