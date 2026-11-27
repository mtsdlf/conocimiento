---
resumen: >-
  La pirámide de pruebas es el modelo que reparte las pruebas automáticas por nivel: muchas rápidas y
  aisladas abajo, menos de integración en el medio y pocas de extremo a extremo arriba. Sus
  alternativas (el trofeo, el panal) discuten la forma; lo que comparten es probar en la frontera con
  pocas pruebas lentas.
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

La pirámide de pruebas es el modelo que reparte las pruebas automáticas por nivel: muchas rápidas y aisladas abajo, menos de integración en el medio y pocas de extremo a extremo arriba. Sus alternativas (el trofeo, el panal) discuten la forma; lo que comparten es probar en la frontera con pocas pruebas lentas.

## De dónde sale y qué recomienda

Mike Cohn popularizó la pirámide en 2009, en *Succeeding with Agile*, con tres capas: unidad, servicio e interfaz de usuario. Según Fowler, la había dibujado con Lisa Crispin en 2003-2004. El artículo de Ham Vocke en el sitio de Fowler admite que los nombres de las capas confunden y que el modelo es simplista.

La regla que deja es una sola: "Push your tests as far down the test pyramid as you can". Las pruebas de extremo a extremo por la interfaz son, para Fowler, "brittle, expensive to write, and time consuming to run", y sirven como "a second line of test defense". Cuando una de ellas falla, se escribe una prueba de nivel más bajo que reproduzca el error. La forma a evitar es el cono de helado: muchas pruebas manuales o por interfaz arriba y pocas rápidas abajo.

## Tres formas para la misma pregunta

> [!IMPORTANT]
> Cuántas pruebas poner en cada nivel está en discusión, y cada forma responde a un tipo de sistema.
> - **Pirámide** (Cohn, Fowler): mayoría de pruebas de unidad, porque son rápidas y señalan la falla con precisión.
> - **Panal** (Spotify, 2018, para microservicios): mayoría de pruebas de integración del servicio por sus puntos de interacción (REST o mensajes), pocas de detalle de implementación e idealmente ninguna que dependa de que otro sistema ande bien. El argumento: en microservicios la complejidad está en las interacciones, y muchas pruebas de unidad atan las pruebas a la implementación, de modo que refactorizar obliga a reescribirlas. El costo que admiten: pruebas más lentas (de milisegundos a pocos segundos) y mensajes de falla menos precisos.
> - **Trofeo** (Kent C. Dodds, para monolitos de una sola base de código, centrado en frontend): capas de análisis estático, unidad, integración y extremo a extremo, con integración como la más ancha. Su criterio: "The more your tests resemble the way your software is used, the more confidence they can give you."

Debajo del desacuerdo hay un problema de vocabulario. "Unidad" no tiene una definición común, y la discusión de porcentajes por nivel tapa lo que importa, según el resumen del texto de Dodds: pruebas rápidas, confiables y que fallen por buenas razones. Esta base toma eso como criterio y deja la forma como una decisión por tipo de sistema: en un servicio con pocas dependencias, la pirámide; en un sistema hecho de servicios que se hablan, el panal.

## Las pruebas de contrato

Una prueba de contrato verifica la frontera entre dos sistemas sin levantar los dos a la vez. Fowler distingue dos sentidos.

En el primero, la prueba comprueba que los dobles de prueba de un servicio externo respondan igual que el servicio real: "These check that all the calls against your test doubles return the same results as a call to the external service would." Como golpean el servicio real, corren cada tanto y no en cada commit.

En el segundo, el contrato lo dirige el consumidor. El equipo que consume la API publica lo que necesita de ella como pruebas, y el equipo proveedor corre copias de esas pruebas en su pipeline. Así el proveedor sabe antes de desplegar si rompe a alguien. El artículo de Vocke lo muestra con Pact y marca el límite: dentro de una organización se pueden cubrir todos los consumidores; en una API pública, normalmente no.

Esto es lo que le falta a [diseñar casos de prueba de una API](disenar-casos-de-prueba-de-api.md), que parte del contrato OpenAPI pero no verifica que proveedor y consumidores sigan de acuerdo. En una arquitectura de [microservicios](../../Arquitectura/Estilos/microservicios.md), las pruebas de contrato reemplazan buena parte de las de extremo a extremo.

## Qué cambia cuando las pruebas las escribe un agente

Con un agente, escribir muchas pruebas de unidad cuesta casi nada; el cuello pasa a ser que valgan algo y que no queden atadas a la implementación. Es inferencia de esta base: el argumento del panal pesa más cuando un agente refactoriza seguido. No se encontró un estudio que compare formas de suite con código escrito por agentes.

Las pruebas de contrato ganan peso por la misma razón. Un agente trabaja en una zona del código, y el contrato es el límite que no puede romper aunque cambie todo lo de adentro. Para saber si las pruebas que escribió un agente detectan fallas, la herramienta es la mutación, en [verificar lo que hizo un agente](verificar-lo-que-hizo-un-agente.md).

La guía de buenas prácticas de Anthropic para su agente de código (leída el 2026-11-27) pide darle "the exact test, typecheck, and lint commands, and how to run a single test file". Eso sirve a cualquier nivel, pero exige que las pruebas sean rápidas y deterministas: una suite lenta o inestable no le sirve al agente como señal.

## El recurso para leer

"The Practical Test Pyramid", de Ham Vocke en el sitio de Fowler: las secciones de pruebas de integración, de contrato y de extremo a extremo. Conviene fijarse en la regla de empujar las pruebas hacia abajo y en el apartado de contratos dirigidos por el consumidor. Cómo encaja la suite en el pipeline está en [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md).
