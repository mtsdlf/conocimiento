---
resumen: >-
  Las métricas de UX se dividen en dos familias que contestan preguntas distintas: las de un test con personas (éxito de tarea, tiempo, SUS), que cuantifican lo que pasó en esas sesiones, y las de comportamiento a escala (HEART, experimento A/B), que dicen cuántos y cuánto. El NPS es un cuestionario de lealtad declarada y se discute aparte.
estado: vigente
estabilidad: semi
fuentes:
  - "MeasuringU (Sauro), SUS: https://measuringu.com/sus/ (leída a través del resumen de una herramienta)"
  - "MeasuringU, NPS en UX: https://measuringu.com/nps-ux/ (leída a través del resumen de una herramienta)"
  - "Rodden, Hutchinson y Fu (2010), Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications, CHI (solo abstract): https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/"
  - "Bangor, Kortum y Miller (2008), An Empirical Evaluation of the System Usability Scale, Int. J. HCI 24(6):574-594, doi 10.1080/10447310802205776 (solo metadatos)"
  - "ISO 9241-11, definición de usabilidad (versión de 1998, vía W3C: https://www.w3.org/2002/Talks/0104-usabilityprocess/slide3-1.html y https://arxiv.org/pdf/1502.06792); edición de 2018 no leída"
  - "Kohavi y Thomke (2017), The Surprising Power of Online Experiments, HBR sept.-oct.: https://hbr.org/2017/09/the-surprising-power-of-online-experiments"
  - "Kohavi, Tang y Xu (2020), Trustworthy Online Controlled Experiments, Cambridge UP (solo metadatos): https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59"
  - "UX/.investigacion/investigacion-y-evaluacion.md y UX/.investigacion/posicion-contraria.md"
aliases: [métricas de usabilidad, UX metrics, SUS, System Usability Scale, HEART, NPS, Net Promoter Score]
creado: 2026-11-22
revisado: 2026-11-22
---

# Métricas de UX

Las métricas de UX se dividen en dos familias que contestan preguntas distintas: las de un test con personas (éxito de tarea, tiempo, SUS), que cuantifican lo que pasó en esas sesiones, y las de comportamiento a escala (HEART, experimento A/B), que dicen cuántos y cuánto. El NPS es un cuestionario de lealtad declarada y se discute aparte.

Cuantifican lo que la [evaluación](evaluacion.md) observa. Parten de la definición de usabilidad de ISO 9241-11, que la divide en eficacia, eficiencia y satisfacción en un contexto dado. En su versión de 1998 dice: "The extent to which a product can be used by specified users to achieve specified goals with effectiveness, efficiency and satisfaction in a specified context" (vía buscador; la edición de 2018 extiende la definición a "sistema, producto o servicio", pero su oración literal no se leyó).

## Qué mide cada componente de la usabilidad

La eficacia es la exactitud y completitud con que se logran los objetivos; la eficiencia, los recursos gastados para lograrlos; la satisfacción, la ausencia de incomodidad y las actitudes positivas (versión de 1998). La norma exige describir objetivos, contexto de uso y un valor meta por atributo, y no prescribe las medidas. En la práctica, el éxito de tarea mide eficacia, y el tiempo y los errores miden eficiencia: es la lectura habitual (Sauro y Lewis, no leídos).

## Métricas de un test con personas

Salen de un [test de usabilidad](test-de-usabilidad.md), con pocos participantes. Cuantifican lo que pasó en esas sesiones y no dicen qué proporción de todos los usuarios sufre el problema (lectura de esta base a partir del eje cualitativo y cuantitativo de NN/g).

SUS (System Usability Scale) es un cuestionario. Se puntúa así: en los ítems impares, la respuesta menos 1; en los pares, 5 menos la respuesta; se suman y se multiplican por 2,5, para una escala de 0 a 100. Según MeasuringU, el promedio de unos 500 estudios es 68. Por encima de 80,3 es una A (cerca del 10% superior), 68 equivale a una C y por debajo de 51 es una F. El puntaje 74 corresponde a cerca del percentil 70. MeasuringU dice que Brooke lo publicó en 1986; la cita de memoria es Brooke (1996), sin verificar. Bangor, Kortum y Miller (2008) reportan un estudio de más de 200 tests, con rangos de aceptabilidad (solo metadatos leídos).

SUS resume una impresión general. Ninguna fuente leída dice qué hay que arreglar a partir de su puntaje, y por ser un cuestionario declarado comparte, por inferencia, los límites del [autorreporte](../Investigacion/entrevista-de-usuario.md).

## Métricas a escala

Se obtienen del uso real de muchas personas, o de cuestionarios a muestras grandes. Dicen cuántos y cuánto, pero no por qué.

HEART (Rodden, Hutchinson y Fu, CHI 2010) propone cinco categorías: Happiness, Engagement, Adoption, Retention y Task success, y un proceso Goals-Signals-Metrics para ligar cada objetivo a una señal y a una métrica. Se leyó solo el abstract: las definiciones de cada categoría quedan sin verificar.

El NPS (Net Promoter Score) pregunta cuán probable es recomendar el producto en una escala de 0 a 10. Promotores son 9 y 10, pasivos 7 y 8, detractores de 0 a 6. El puntaje es el porcentaje de promotores menos el de detractores.

> [!IMPORTANT]
> Si el NPS sirve para medir UX está discutido. A favor, según MeasuringU: es una sola pregunta, la facilidad de uso explica entre 30% y 50% de la propensión a recomendar, y la intención de recomendar fue el mejor o el segundo mejor predictor de recompra o referidos en 11 de 14 industrias (citando a Reichheld, 2006).
>
> En contra, según la misma fuente: agrupar una escala de 11 puntos en tres grupos ensancha el margen de error a cerca del doble ("usually around twice as wide") y exige muestras mayores; es un síntoma de lealtad y no una causa, así que no dice qué arreglar; solo 68% de los promotores dijo haber recomendado en el último año (rango de 43% a 96%); y los puntajes dependen de la industria (cerca de 21% en software de consumo, cerca de 6% en cable). La lectura prudente: el NPS mide lealtad declarada, se relaciona en parte con la usabilidad y no reemplaza a SUS ni a las métricas de tarea.

## Dónde entra el experimento A/B

El experimento A/B reparte al azar el tráfico entre dos variantes y compara una métrica (descripción general de esta base, sin fuente leída en esta ronda). NN/g lo ubica como método conductual y sumativo. Las métricas de HEART son candidatas a métrica de un experimento. Kohavi, Tang y Xu (2020) lo tratan con métricas clave y un Overall Evaluation Criterion; los autores dicen que las empresas del libro corren más de 20.000 experimentos al año.

Su aporte es la causa: como solo el azar decide quién ve cada variante, la diferencia se atribuye al cambio. La lógica es la de la [incrementalidad](../../Marketing/Medicion/incrementalidad.md): solo un grupo de control mide lo que un cambio causa.

Tiene tres límites. El primero es el volumen: con poco tráfico, un experimento puede no distinguir una mejora real del azar (inferencia propia: no se leyó una fuente de tamaño de muestra de UX). El segundo es el porqué: un A/B dice qué variante ganó, no por qué, y ahí entra el test con personas. El tercero es el juicio previo: en Google y Bing, según Kohavi y Thomke (HBR, 2017), "only about 10% to 20% of experiments generate positive results"; en Microsoft, un tercio resulta efectivo, un tercio neutro y un tercio negativo. Esa tasa probablemente viene de empresas con sitios muy optimizados y mucho tráfico, y no de una tienda chica (inferencia de esta base).

> [!IMPORTANT]
> Hay una tensión entre el test con pocos usuarios y el experimento a escala. NN/g defiende decidir con pocos usuarios observados; Kohavi sostiene que los expertos "often misjudge which [ideas] will pay off" y que hay que medir. Esta base los trata como complementarios, porque cada uno contesta otra pregunta: el test dice por qué se traba la gente, el experimento dice cuánto cambia una métrica.

Cómo se diseña un experimento, con tamaño de muestra y fallas comunes, falta como nota propia (ver [Evaluación](evaluacion.md)).

## Qué leer

MeasuringU, [SUS](https://measuringu.com/sus/), por su puntuación y su escala por letras. Rodden et al. (2010), corto, para HEART. Kohavi, Tang y Xu (2020), capítulo 1, para las tasas de éxito (no leído).

> [!NOTE]
> Sin fuente todavía: la oración literal de ISO 9241-11:2018, las definiciones de cada categoría de HEART, la cita original de Brooke para SUS y el tamaño de muestra de un experimento. Las cifras de MeasuringU salen de un resumen que una herramienta hizo de cada página: conviene cotejarlas en el original antes de entrecomillarlas.
