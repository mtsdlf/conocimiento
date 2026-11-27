---
resumen: >-
  Refactorizar es cambiar la estructura interna del código sin cambiar su comportamiento observable,
  en pasos chicos y con pruebas que lo confirmen. Con pruebas que fijen el comportamiento, es el
  trabajo mejor acotado que se le puede dar a un agente.
estado: vigente
estabilidad: estable
fuentes:
  - https://martinfowler.com/books/refactoring.html
  - https://engineering.atspotify.com/2018/01/testing-of-microservices/
  - https://arxiv.org/abs/2511.04824
  - https://arxiv.org/pdf/2605.21453
  - https://www.gitclear.com/ai_assistant_code_quality_2025_research
  - https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
aliases: [refactoring, refactorización, refactor, reestructurar código]
creado: 2026-11-27
revisado: 2026-11-27
---

# Refactorizar

Refactorizar es cambiar la estructura interna del código sin cambiar su comportamiento observable, en pasos chicos y con pruebas que lo confirmen. Con pruebas que fijen el comportamiento, es el trabajo mejor acotado que se le puede dar a un agente.

## El catálogo de Fowler como vocabulario

La referencia es *Refactoring*, de Martin Fowler: la primera edición es de 1999 y la segunda, de 2018. Según la página del libro, la segunda edición recorre de punta a punta un caso inicial, tiene capítulos sobre malos olores del código y sobre el papel de las pruebas, y un catálogo de unas setenta refactorizaciones, cada una con su motivación, su mecánica y un ejemplo.

El catálogo da un nombre a cada cambio, y esos nombres sirven para pedirle un cambio preciso a un agente y para revisar lo que hizo. Un pedido como "extraé esta función y no cambies nada más" se verifica mejor que "mejorá este código" (inferencia de esta base).

## Por qué sin pruebas no es refactorizar

La definición hace de la refactorización una especificación verificable: después del cambio, todo lo que el sistema hacía tiene que seguir igual. Para esta base, la forma barata de comprobarlo es una suite que fije ese comportamiento y se corra después de cada paso; sin ella, el cambio de forma queda sin verificar (inferencia propia, sin fuente).

Por eso el orden importa. Si el código no tiene pruebas, primero se escriben pruebas de caracterización sobre lo que hace hoy, como se explica en [sistema heredado](sistema-heredado.md), y recién después se refactoriza. Si las pruebas están atadas a la implementación (prueban cómo está hecho y no qué hace), refactorizar obliga a cambiarlas; ese es el argumento del panal de Spotify contra muchas pruebas de unidad finas, en la [pirámide de pruebas](../Verificacion/piramide-de-pruebas.md).

Refactorizar es también la forma de pagar la [deuda técnica](deuda-tecnica.md): de a pasos, en las zonas que cambian seguido, como parte del trabajo normal.

## Lo que hacen los agentes cuando refactorizan

Hay estudios recientes, todos preprints conocidos por su resumen. Uno, sobre pull requests de agentes en repositorios Java, encontró 15.451 refactorizaciones en 12.256 PRs; los agentes apuntan a refactorizar en 26,1 % de sus commits, y las motivaciones son mantenibilidad (52,5 %) y legibilidad (28,1 %). Las cifras de commits cambian entre versiones del paper. Otro estudio, en Python, halló que una fracción grande de los PRs de refactorización de agentes se acepta aunque introduzcan problemas nuevos de lint y de seguridad.

> [!NOTE]
> Sin fuente todavía: los estudios hallados detectan refactorizaciones con herramientas de análisis y miden malos olores, pero ninguno verifica ejecutando pruebas si el agente preservó el comportamiento. No se sabe con evidencia qué tan seguido un agente cambia lo que el código hace cuando dice que solo lo reordenó.

A la vez, según GitClear (que vende análisis de código), el código movido, que es la señal de refactorización en un diff, bajó a menos de la mitad de las líneas cambiadas entre 2020 y 2024 (las cifras están en [deuda técnica](deuda-tecnica.md#la-deuda-que-acumula-un-agente)). Esta base lo lee como señal de que se refactoriza menos justo cuando la herramienta lo hace más barato, aunque el estudio es observacional y no prueba la causa.

## Cómo se le pide una refactorización a un agente

1. Comprobá que hay pruebas que cubren el comportamiento de la zona; si no, escribilas antes.
2. Pedí una refactorización con nombre del catálogo, en una zona acotada.
3. Exigí que las pruebas no cambien: si el agente tuvo que tocar una prueba para que pase, cambió comportamiento o la prueba estaba atada a la implementación. Tocar pruebas es la primera señal de [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md).
4. Corré la suite completa y pedile la salida.
5. Revisá que el diff haga solo lo pedido.

Böckeler encontró una prueba escrita por un agente que fijaba un bug: si la suite consagra un error, refactorizar lo preserva. Las pruebas confirman que no cambió nada, no que lo que había estaba bien.

## Lo mecánico pierde peso

[Pierde peso](../Fundamentos/lo-que-pierde-peso-en-desarrollo.md#lo-que-pierde-peso-en-cada-etapa) hacer a mano, por rutina, los cambios mecánicos (renombres, extracciones) que un agente hace con pruebas. El catálogo de Fowler no pierde peso: es el vocabulario para pedir y para revisar. Cuando el cambio de forma toca miles de archivos a la vez, deja de ser una refactorización local y pasa a ser una [migración](migraciones-y-actualizaciones.md).

Para leer: *Refactoring*, segunda edición, el capítulo 1 (el ejemplo completo) y el capítulo sobre pruebas; el catálogo, como consulta.
