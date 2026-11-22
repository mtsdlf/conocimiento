---
resumen: >-
  Un experimento A/B reparte al azar a los usuarios entre dos o más variantes de una experiencia y compara una métrica, para saber qué causó un cambio y no solo qué lo acompañó. Exige volumen: con poco tráfico, como en un producto B2B chico o en el software que una consultora construye para un cliente, no distingue una mejora del azar y el método es otro.
estado: vigente
estabilidad: semi
fuentes:
  - "Ron Kohavi, Diane Tang y Ya Xu, Trustworthy Online Controlled Experiments (Cambridge University Press, 2020), frontmatter e índice (el cuerpo no se pudo leer): https://assets.cambridge.org/97811087/24265/frontmatter/9781108724265_frontmatter.pdf"
  - "Kohavi, Tang y Xu, cap. 3, Twyman's Law and Experimentation Trustworthiness (solo metadatos y resumen del buscador): https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/twymans-law-and-experimentation-trustworthiness/886425EC1B92BD23A0DC5E6817785190"
  - "Ron Kohavi y Stefan Thomke, The Surprising Power of Online Experiments, HBR sep-oct 2017, reimpresión R1705E: https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf"
  - "Kohavi et al., Online Controlled Experiments at Large Scale, KDD 2013 (solo abstract): https://exp-platform.com/large-scale/"
  - "Bing, Large Scale Experimentation at Bing (2013; vía buscador): https://blogs.bing.com/search-quality-insights/2013/08/08/large-scale-experimentation-at-bing"
  - "Kohavi et al., Statistical Challenges in Online Controlled Experiments, arXiv 2212.11366 (vía buscador): https://arxiv.org/pdf/2212.11366.pdf"
  - "Kohavi et al., Power Analysis is Essential (arXiv, 2025; vía buscador): https://arxiv.org/pdf/2512.24521"
  - "Kameleoon, Data accuracy pitfalls in A/B testing (blog de proveedor; vía buscador): https://www.kameleoon.com/endata-accuracy-pitfalls-ab-testing"
  - "Producto/.investigacion/medicion-y-monetizacion.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmación 5)"
aliases: [A/B test, test A/B, prueba A/B, experimento controlado en línea, online controlled experiment]
creado: 2026-11-22
revisado: 2026-11-22
---

# Experimento A/B

Un experimento A/B reparte al azar a los usuarios entre dos o más variantes de una experiencia y compara una métrica, para saber qué causó un cambio y no solo qué lo acompañó. Exige volumen: con poco tráfico, como en un producto B2B chico o en el software que una consultora construye para un cliente, no distingue una mejora del azar y el método es otro.

Dentro de la [medición](medicion-de-producto.md), es la herramienta que separa la causa de la correlación. Sirve para confirmar una métrica de [activación](activacion.md) y para saber si un cambio movió la [North Star](north-star.md) o sus métricas de entrada. El texto con método de esta vertical es el libro de Kohavi, Tang y Xu (2020), basado, según su frontmatter (vía buscador), en empresas que corren más de 20.000 experimentos controlados cada una.

## Por qué hay que probar: la mayoría de las ideas no mueve la métrica

La mayoría de los cambios que un equipo cree buenos no mejora lo que buscaba mejorar. Es la afirmación del campo con mejor evidencia, porque sale de experimentos reales, aunque las cifras varían según la fuente:

| Fuente | Qué dice | Cómo se leyó |
|---|---|---|
| Kohavi y Thomke, HBR 2017 | Google y Bing: "only about 10% to 20% of experiments generate positive results"; Microsoft: "one-third prove effective, one-third have neutral results, and one-third have negative results" | entero |
| Blog de Bing (2013) | "fewer than a third improve the metric they were built to move" | vía buscador |
| Diapositivas de Kohavi | en Microsoft, un tercio positivo y significativo, un tercio neutro, un tercio negativo | vía buscador |
| Revisión que cita a Kohavi (arXiv 2212.11366) | "more than 50% of ideas fail to generate meaningful improvements" | vía buscador |
| Kohavi et al., KDD 2013 | "many ideas impact key metrics by 1% and are not well estimated a-priori" | abstract |

El "un tercio" de las diapositivas es el de Microsoft, la misma cifra que da el HBR; en Bing la proporción es menor, como dicen el HBR y el blog. Las cinco son de la misma familia de autores y datos: no cuentan como fuentes independientes. Son de buscadores y plataformas con muchísimo tráfico, en productos ya muy optimizados. No se trasladan tal cual a un producto nuevo ni a un B2B chico, y no apareció un estudio sobre tasas de éxito en dominios sin optimizar. Lo que sí se traslada es la conclusión: el juicio previo del equipo acierta poco, así que hay que comprobar.

## Qué invalida un resultado

Un resultado sorprendente casi siempre es un error. Es la ley de Twyman, a la que el libro dedica el capítulo 3; según el resumen del buscador, sostiene que cualquier cifra que parezca interesante o distinta suele estar mal. Kohavi cuenta, en un documento propio leído por el buscador, que ante resultados sorprendentes "probably 9 out of 10 times we found an issue that invalidated the result".

Las fallas que el libro trata, según su índice y resúmenes del buscador:

- Mirar antes de tiempo. Revisar el p-valor una y otra vez mientras corre el experimento (peeking) equivale a hacer muchas pruebas de hipótesis y sube el error de tipo I: se declaran ganadoras variantes que no lo son.
- Falta de poder estadístico. Para efectos chicos, según el resumen de un paper de Kohavi y coautores de 2025, la mayoría de las organizaciones no tiene poder suficiente.
- Romper algo sin verlo. Las métricas de guarda (guardrail metrics) vigilan lo que no se quiere empeorar; el índice da como ejemplos la tasa de escritura de cookies y la latencia.
- Confundir el corto con el largo plazo. El índice tiene entradas para "novelty effect", "short-term effect" y "delayed experience": lo que gana en dos semanas puede no ganar en seis meses.

El abstract de KDD 2013 agrega "a high occurrence of false positives that we address".

## Cuándo un experimento no sirve

Un experimento necesita muchos usuarios para distinguir una mejora chica del azar. Con poco tráfico no tiene poder, y además aparece la maldición del ganador: un resultado significativo sobrestima el efecto real. Esto último lo dice un blog de un proveedor de herramientas de experimentación, no Kohavi.

Tres contextos quedan casi siempre afuera. Un producto B2B con pocas cuentas no junta la muestra. Una agencia de marketing digital con clientes chicos tampoco. Una consultora de software que construye un sistema para un cliente suele tener pocos usuarios por sistema. Que en esos casos un A/B formal casi nunca tenga muestra suficiente es una inferencia del informe de posición contraria, no una cita.

> [!NOTE]
> Sin fuente todavía: un tráfico mínimo concreto para correr un experimento y lo que dice el libro sobre su aplicación a productos chicos. El cuerpo del libro no se pudo leer.

Cuando falta volumen, la incertidumbre se reduce con otros métodos, que responden otra pregunta. La [prueba de supuestos](../Descubrimiento/prueba-de-supuestos.md) del descubrimiento ataca un riesgo antes de construir. La [entrevista de usuario](../../UX/Investigacion/entrevista-de-usuario.md) y el [test de usabilidad](../../UX/Evaluacion/test-de-usabilidad.md) dicen por qué la gente actúa como actúa. Ninguno mide cuánto cambió una métrica, pero el experimento tampoco lo mide si no tiene poder.

## Dónde termina el experimento de producto

El A/B de producto compara variantes de una experiencia: una pantalla o un flujo. Medir el efecto causal de un canal o una campaña es [incrementalidad](../../Marketing/Medicion/incrementalidad.md), en Marketing. La lógica es la misma: solo un grupo de control que no recibe el cambio mide lo que el cambio causa. La diferencia es qué se prueba y quién lo decide.

Cómo usa UX el experimento, junto con HEART y las métricas de un test con personas, está en [métricas de UX](../../UX/Evaluacion/metricas-de-ux.md#dónde-entra-el-experimento-ab).

## Leer a Kohavi, Tang y Xu

*Trustworthy Online Controlled Experiments* es la referencia del tema. Conviene leer la Parte I (capítulos 1 a 3: introducción, vocabulario y la ley de Twyman) y los capítulos de poder estadístico y de métricas de guarda, y fijarse en la distinción entre métrica de objetivo, métrica de guarda y métrica de calidad de datos, y en el chequeo de desbalance de muestra (sample ratio mismatch), que detecta cuando el reparto al azar falló.
