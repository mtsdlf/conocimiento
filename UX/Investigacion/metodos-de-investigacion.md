---
resumen: >-
  Los métodos de investigación de UX se eligen por la pregunta que hay que contestar y por la fase del producto: generativos para descubrir qué diseñar, evaluativos para comprobar una solución. NN/g los ordena por si miden lo que la gente dice o lo que hace, y si contestan por qué o cuántos.
estado: vigente
estabilidad: estable
fuentes:
  - "NN/g, When to Use Which User-Experience Research Methods: https://www.nngroup.com/articles/which-ux-research-methods/ (leída a través del resumen de una herramienta; el gráfico de 20 métodos es una imagen)"
  - "NN/g, Field Studies: https://www.nngroup.com/articles/field-studies/ (leída a través del resumen de una herramienta; una sola frase)"
  - "ISO 9241-210:2019, Human-centred design for interactive systems (listado público): https://www.iso.org/standard/77520.html"
  - "UX/.investigacion/investigacion-y-evaluacion.md"
aliases: [métodos de UX research, qué método usar, user research methods]
creado: 2026-11-22
revisado: 2026-11-22
---

# Métodos de investigación

Los métodos de investigación de UX se eligen por la pregunta que hay que contestar y por la fase del producto: generativos para descubrir qué diseñar, evaluativos para comprobar una solución. NN/g los ordena por si miden lo que la gente dice o lo que hace, y si contestan por qué o cuántos.

## Tres ejes para elegir

NN/g ubica cada método en tres dimensiones. La primera separa lo actitudinal ("what people say") de lo conductual ("what people do"). La segunda separa lo cualitativo, que sale de "observing or hearing them directly", de lo cuantitativo, que se recoge "indirectly, through a measurement or an instrument". La tercera describe el contexto de uso: natural (estudios de campo, encuestas de intercepción, analítica), guionado (benchmarking), limitado (diseño participativo, card sorting) o sin usar el producto (percepción de marca).

Las encuestas y el card sorting caen hacia lo actitudinal; el experimento A/B y el eyetracking, hacia lo conductual; el test de usabilidad y los estudios de campo, en el medio. Lo cualitativo responde por qué pasa algo y cómo arreglarlo, y lo cuantitativo, cuántos lo sufren y cuánto.

## El mapa por fase

NN/g reparte los métodos en tres momentos del producto. Esta nota agrupa los dos últimos como investigación evaluativa; NN/g habla de generativa, formativa y sumativa. La columna de preguntas es una glosa de esta base. El gráfico de NN/g es una imagen que no se pudo leer, así que la tabla sale del texto y no de las posiciones del gráfico.

| Fase | Investigación | Métodos | Pregunta que contesta |
|---|---|---|---|
| Definir qué hacer (Strategize) | Generativa | Estudio de campo, estudio de diario, entrevista, encuesta, diseño participativo, test de conceptos | ¿Quién es la persona, qué intenta resolver y en qué contexto? |
| Diseñar (Design) | Evaluativa, formativa | Card sorting, tree testing, test de usabilidad, test remoto | ¿Esta organización y este flujo se entienden? ¿Dónde se traba la gente? |
| Lanzar y medir (Launch & Assess) | Evaluativa, sumativa | Benchmark de usabilidad, test no moderado, experimento A/B, clickstream y analítica, encuesta | ¿Cuánto mejoró? ¿Cuántos completan la tarea? ¿Qué variante rinde más? |

La evaluación heurística no aparece en el texto de NN/g que se leyó. Esta base la ubica en el segundo renglón: la hacen evaluadores sin usuarios y alimenta el test de usabilidad (ubicación propia, no de la fuente).

## Dónde se solapan generativa y evaluativa

El test de usabilidad pertenece a las dos. NN/g lo coloca en la fase de diseño, como método formativo, y es a la vez una técnica de [Evaluación](../Evaluacion/evaluacion.md). La encuesta también aparece dos veces, en la fase generativa y en la sumativa. Esta base deja el mapa completo acá y manda el cómo de cada técnica a su nota: [test de usabilidad](../Evaluacion/test-de-usabilidad.md), [evaluación heurística](../Evaluacion/evaluacion-heuristica.md) y [métricas de UX](../Evaluacion/metricas-de-ux.md).

## Qué dice la norma sobre los métodos

ISO 9241-210:2019 "provides an overview of human-centred design activities" y "does not provide detailed coverage of the methods and techniques" (según el listado público de ISO, vía buscador). Da una visión de las actividades del ciclo de [diseño centrado en el usuario](../ux.md) y no nombra métodos. Asignar un método a cada actividad es una síntesis de esta base, con nombres de actividad que no se verificaron: la investigación generativa sirve a entender el contexto de uso, y la evaluativa a evaluar el diseño.

> [!NOTE]
> Sin fuente todavía: la redacción literal de las cuatro actividades de ISO 9241-210, que es norma paga y no se leyó completa. Las citas de NN/g salen de un resumen que una herramienta hizo de cada página: conviene cotejarlas en el original antes de entrecomillarlas.

## Combinar un método de decir con uno de hacer

Un método actitudinal sin uno conductual deja sin contrastar lo que la gente cuenta. Esta base propone entrevistar o encuestar para ver qué observar, observar o medir para ver qué hace, y volver a entrevistar para entender el porqué de lo medido (secuencia propuesta, sin fuente que la fije). La [entrevista de usuario](entrevista-de-usuario.md) sería el primer paso y su límite es el autorreporte. El [experimento A/B](../Evaluacion/metricas-de-ux.md#donde-entra-el-experimento-ab) mide la conducta a escala pero no dice por qué una variante gana.

## Leer el mapa de NN/g

El recurso de referencia es NN/g, [When to Use Which User-Experience Research Methods](https://www.nngroup.com/articles/which-ux-research-methods/). Conviene mirar la figura de los 20 métodos y el eje temporal de tres fases, que esta nota resume en la tabla desde el texto. Como respaldo normativo existe ISO 9241-210, de pago. Para el trabajo de campo, la nota de NN/g sobre [estudios de campo](https://www.nngroup.com/articles/field-studies/) dice que ocurre "in the user's natural environment".

## Qué métodos faltan en este mapa

Faltan como notas propias el mapa de recorrido, las personas, el estudio de campo con indagación contextual, la analítica, y las encuestas y cuestionarios. Están nombrados en la [entrada de Investigación](investigacion.md). Los dos métodos de arquitectura de información, card sorting y tree testing, esperan su nota en [Arquitectura de información](../Arquitectura-de-informacion/arquitectura-de-informacion.md). Para entender el trabajo que la persona quiere resolver, [jobs to be done](../../Marketing/Mercado-y-cliente/jobs-to-be-done.md) aporta un marco de preguntas.
