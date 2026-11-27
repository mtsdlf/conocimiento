---
resumen: >-
  El análisis de riesgo de arquitectura busca, antes de comprometerse con un diseño, qué partes
  pueden fallar y cuánto daño harían; risk storming lo hace en grupo sobre un diagrama, y la matriz
  de riesgo ordena lo encontrado por impacto y probabilidad.
estado: vigente
estabilidad: estable
fuentes:
  - https://nealford.com/books/SAF2e.html
  - "Richards y Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), cap. 'Analyzing Architecture Risk' (no leído)"
  - https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/ch20.html
  - https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ch22.html
  - https://icepanel.io/blog/risk-storming
  - https://huyenchip.com/2025/01/07/agents.html
aliases: [risk storming, matriz de riesgo, architecture risk]
creado: 2026-11-27
revisado: 2026-11-27
---

# Análisis de riesgo

El análisis de riesgo de arquitectura busca, antes de comprometerse con un diseño, qué partes
pueden fallar y cuánto daño harían; risk storming lo hace en grupo sobre un diagrama, y la matriz
de riesgo ordena lo encontrado por impacto y probabilidad.

Richards y Ford le dedican un capítulo, "Analyzing Architecture Risk", en la parte de técnicas de
su libro, junto a las [decisiones](decisiones.md) y los [diagramas](diagramas.md). Según el
buscador, es el capítulo 20 de la 1ª edición y el 22 de la 2ª.

## La matriz: impacto por probabilidad

La matriz cruza dos preguntas sobre cada riesgo: cuánto daño haría si pasa y qué tan probable es
que pase. Un riesgo de mucho impacto y poca probabilidad (que se caiga la región entera del
proveedor) se trata distinto de uno de impacto medio y probabilidad alta (que una dependencia lenta
tumbe el checkout en cada pico). La matriz no resuelve nada: ordena qué mitigar primero. Según
resúmenes secundarios, el capítulo de Richards y Ford la presenta junto con risk storming.

> [!NOTE] Sin fuente todavía: la escala, los puntajes y los colores que usa el libro para la matriz
> (el capítulo no se pudo leer).

## Risk storming: buscar riesgos en grupo

Risk storming es una técnica colaborativa que se atribuye a Simon Brown (*Software Architecture for
Developers*). Según un resumen del capítulo, se hace sobre un diagrama de la arquitectura, en tres
fases:

1. **Identificación individual**: cada participante marca en el diagrama los riesgos que ve, sin
   mirar lo que marcan los demás, para que nadie influya en nadie.
2. **Consenso**: se juntan las marcas y se discute dónde coinciden y dónde no, hasta acordar qué
   riesgos hay.
3. **Mitigación**: para los riesgos acordados, qué cambio de diseño los reduce.

El diagrama es la condición (razonamiento de esta base): sin un dibujo compartido de la estructura, cada uno habla de un
sistema distinto. Por eso, según esta base, el análisis de riesgo se apoya en un modelo como C4
([diagramas](diagramas.md)), y lo que se decide al mitigar queda en un [ADR](adr.md).

> [!NOTE] Las fases salen de resúmenes secundarios que parafrasean el capítulo de Richards y Ford;
> no se leyó la fuente de Brown ni el libro.

## Los riesgos de una pieza que no es determinista

Un modelo de IA agrega riesgos que el diagrama no muestra solo con cajas: respuestas incorrectas,
costos que se disparan, un proveedor que cambia el modelo. Para los agentes, Huyen propone una forma
de medirlos: "To evaluate an agent, identify its failure modes and measure how often each of these
failure modes happens", y separa fallas de planificación, de herramientas y de eficiencia. Usar esa
lista de modos de falla como entrada del risk storming, y el
[análisis de errores](../Evaluacion-y-observabilidad/analisis-de-errores.md) como la forma de saber
su probabilidad real en producción, es inferencia de esta base. Las mitigaciones típicas son las
del [catálogo de patrones](../arquitectura.md#catálogo-de-patrones), como
[degradación controlada](../Sistemas-distribuidos/degradacion-controlada.md) o
[guardrails](../../IA/guardrails.md).

## Qué leer

Richards y Ford, 2ª ed., capítulo "Analyzing Architecture Risk". Fijarse en la matriz y en cómo se
conduce un risk storming. Sin acceso al libro, la descripción de Simon Brown es la alternativa.
