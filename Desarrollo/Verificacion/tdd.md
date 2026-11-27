---
resumen: >-
  TDD (desarrollo guiado por pruebas) es escribir primero una prueba que falla, después el código
  que la hace pasar y por último ordenar el código. Con agentes vale sobre todo como señal de
  retroalimentación y definición de terminado; su efecto sobre la calidad no está probado.
estado: borrador
estabilidad: semi
fuentes:
  - https://arxiv.org/abs/1611.05994
  - https://arxiv.org/abs/2011.11942
  - https://helda.helsinki.fi/server/api/core/bitstreams/28435ba6-f068-4f28-983a-47d703536365/content
  - https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
  - https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
  - https://code.claude.com/docs/en/best-practices
  - https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code
aliases: [test-driven development, desarrollo guiado por pruebas, test first, prueba primero, rojo-verde-refactor, red-green-refactor]
creado: 2026-11-27
revisado:
---

# TDD

TDD (desarrollo guiado por pruebas) es escribir primero una prueba que falla, después el código que la hace pasar y por último ordenar el código. Con agentes vale sobre todo como señal de retroalimentación y definición de terminado; su efecto sobre la calidad no está probado.

El ciclo se conoce como rojo, verde, refactor: la prueba falla (rojo), el código mínimo la hace pasar (verde) y después se mejora la forma sin cambiar el comportamiento, que es [refactorizar](../Evolucion/refactorizar.md). Nació como práctica de Extreme Programming, con Kent Beck.

## Lo que dice la evidencia

> [!IMPORTANT]
> La evidencia causal de que TDD mejora la calidad o la productividad es nula o mixta.
> - **En contra del orden.** Fucci et al. (IEEE TSE, 2017; 82 datos de 39 profesionales) separaron cuatro características del proceso. Según su resumen, la secuencia (probar antes o después) no tuvo influencia importante; la granularidad y la uniformidad de los pasos se asociaron con más calidad y productividad. Concluyen que los beneficios atribuidos a TDD pueden venir de pasos finos y constantes, no del orden.
> - **En contra de la calidad.** Una familia de 12 experimentos con metaanálisis (Santos, Vegas, Dieste et al.) halló, según su resumen, que los novatos lograron "slightly higher code quality" con prueba después iterativa que con TDD, y que la tarea pesó más que el método. Casi todo viene del mismo grupo de investigación y de estudios con estudiantes.
> - **A favor.** Un metaanálisis de 25 estudios (Rafique y Mišić, IEEE TSE, 2013) encontró mejoras de calidad y resultados mixtos en productividad, con la experiencia de los participantes como factor; esto llega por una tesis que lo resume, no por el original. Los mismos estudios críticos hallan, según resúmenes, suites más grandes y con más capacidad de detectar fallas.
>
> Lo que esta base afirma, como criterio de la escuela de Beck y Farley: TDD vale como contrato y retroalimentación. No promete menos defectos.

## Qué pasa cuando el que escribe es un agente

Beck distingue dos formas de trabajar con agentes. "In vibe coding you don't care about the code, just the behavior of the system"; en cambio, "In augmented coding you care about the code, its complexity, the tests, & their coverage." Su prompt de sistema le exigía TDD y commitear solo con todas las pruebas pasando, y una de sus señales de alarma era "Any indication that the genie was cheating, for example by disabling or deleting tests."

Birgitta Böckeler probó TDD dentro del ciclo de un agente, en el sitio de Fowler, con una evaluación chica en la que un modelo genera y otro juzga. El juez no vio ventaja clara de TDD y a menudo puntuó mejor las soluciones sin TDD; los puntajes de mutación fueron parecidos y las corridas con TDD usaron "roughly 3x or more" tokens. Los agentes "often write the implementation first and generate tests after, skip confirming the red step". Encontró pruebas tautológicas, que recalculan el resultado esperado con la misma implementación, y una prueba que fijaba un bug. Su conclusión: "Watching a test go red is only proof of anything if someone is checking why it went red." Dejó de pedir prueba primero y se apoya en mutación, análisis estático y escenarios aprobados de antemano.

Es una evaluación pequeña, con un modelo como juez y sin fecha visible en la página: sirve como señal, no como prueba.

## La prueba como definición de terminado

Lo que sobrevive con agentes es la prueba como contrato de terminado. La guía de buenas prácticas de Anthropic para su agente de código (leída el 2026-11-27) da un ejemplo: el pedido débil es "fix the login bug"; el fuerte pide escribir una prueba que reproduzca el fallo y después arreglarlo. Y pide evidencia, "the command it ran and its output", en lugar de un "pasan todas las pruebas" a secas.

En la práctica eso se traduce así:

1. Escribí (o aprobá, si la escribe el agente) la prueba de aceptación antes de pedir la implementación. Sale de los [criterios de aceptación](../Definicion/criterios-de-aceptacion.md).
2. Comprobá que falla por la razón correcta, no por un error de compilación o de configuración.
3. Dejá que el agente itere hasta que pase, y pedile la salida del comando.
4. Revisá que no haya borrado, desactivado ni ablandado pruebas para llegar al verde: es la primera señal de [verificar lo que hizo un agente](verificar-lo-que-hizo-un-agente.md).

Thoughtworks, en su Radar de noviembre de 2025, recomienda reforzar "established practices such as TDD and static analysis" frente a la complacencia con el código generado. Ahí TDD vale como control, no como método de diseño probado.

## El ritual que pierde peso

Pierde peso el ciclo rojo-verde-refactor como ritual obligatorio para cada línea que escribe un agente, y la cobertura como objetivo. TDD sigue vigente como práctica de diseño para una persona y como la forma de pedir una prueba que reproduzca un bug. Dónde se ubica la prueba en la suite está en la [pirámide de pruebas](piramide-de-pruebas.md).

Para leer: el resumen de Fucci et al. (2017) para ver qué pesa del proceso, y el artículo de Böckeler para ver cómo se comporta un agente, en el apartado de adherencia y costo.
